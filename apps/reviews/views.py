from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.template import RequestContext, loader
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from apps.reviews.models import *
from django.db.models import F
from apps.reviews.forms import ReviewForm
from django.utils import timezone
from django.contrib import messages
from django.contrib.messages import get_messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
import pdb

class UpdateIfCurrentAuthorMixin(object):
    """
    View mixin that makes sure the current author can
    only edit their own content
    """
    def dispatch(self, request, *args, **kwargs):
        handler = super(UpdateView, self).dispatch(request, *args, **kwargs)

        if self.object.author != request.user:
            user = request.user
            return render_to_response('reviews/permission_denied.html', { 'user': user })
        return handler

class DeleteIfCurrentAuthorMixin(object):
    """
    View mixin that makes sure the current author can
    only delete their own content
    """
    def dispatch(self, request, *args, **kwargs):
        handler = super(DeleteView, self).dispatch(request, *args, **kwargs)

        if self.object.author != request.user:
            user = request.user
            return render_to_response('reviews/permission_denied.html', { 'user': user })
        return handler


def index(request):
    recent_reviews = Review.objects.order_by('-pub_date')
    most_liked = Like.objects.order_by('-total_likes')
    if len(recent_reviews) > 10:
        recent_reviews = Review.objects.order_by('pub_date')[10]

    if len(most_liked) > 10:
        most_liked = most_liked = Like.objects.order_by('total_likes')[10]

    context = RequestContext(request, {'recent_reviews': recent_reviews, 'most_liked': most_liked })
    return render(request, 'reviews/index.html', context)

class ReviewDetail(DetailView):
    model = Review

    def get_context_data(self, **kwargs):
        context = super(ReviewDetail, self).get_context_data(**kwargs)
        context['pros'] = context['review'].pros.split('\n')
        context['cons'] = context['review'].cons.split('\n')
        return context

class ReviewList(ListView):
    model = Review

    def get_context_data(self, **kwargs):
        context = super(ReviewList, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        """ Checks if user has liked any reviews. If the user has, then context['liked'] is true, else false. This
        will get passed in to template so that the like button will turn into a unlike button and vice versa  """
        try:
            user_liked = Like.objects.get(user=user, review_id=self.request.GET['review_id'])
        except:
            user_liked = None

        if user_liked:
            liked = True
        else:
            liked = False
        context['liked'] = liked

        return context

class ReviewCreate(CreateView):
    model = Review
    success_url = reverse_lazy('reviews:review_list')
    form_class = ReviewForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(ReviewCreate, self).form_valid(form)

class ReviewUpdate(UpdateIfCurrentAuthorMixin, UpdateView):
    model = Review
    success_url = reverse_lazy('reviews:review_list')
    form_class = ReviewForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(ReviewUpdate, self).form_valid(form)

class ReviewDelete(DeleteIfCurrentAuthorMixin, DeleteView):
    model = Review
    success_url = reverse_lazy('reviews:review_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(ReviewDelete, self).form_valid(form)


def like(request):
    if request.method == 'GET':
        user = request.user
        review = get_object_or_404(Review, id=request.GET['review_id'])
        like = Like.objects.get_or_create(review_id=review.id)

        try:
            user_liked = Like.objects.get(user=user, review_id=review.id)
        except:
            user_liked = None

        if user_liked:
            user_liked.total_likes -= 1
            user_liked.user.remove(request.user)
            user_liked.save()
            likes = user_liked.total_likes

        else:
            list(like)
            like[0].user.add(request.user)
            like[0].total_likes += 1
            like[0].save()
            likes = like[0].total_likes

    return HttpResponse(likes)

'''Review Lists for Consoles'''
def PS4ReviewList(request):
    ps4 = Console.objects.get(name='PS4')
    review_list = ps4.reviews.all()
    context = RequestContext(request, {'review_list': review_list })
    return render(request, 'reviews/ps4.html', context)

def XboxOneReviewList(request):
    xbox_one = Console.objects.get(name='Xbox One')
    review_list = xbox_one.reviews.all()
    context = RequestContext(request, {'review_list': review_list })
    return render(request, 'reviews/xbox-one.html', context)

def WiiUReviewList(request):
    wii_u = Console.objects.get(name='Nintendo Wii U')
    review_list = wii_u.reviews.all()
    context = RequestContext(request, {'review_list': review_list })
    return render(request, 'reviews/nintendo-wii-u.html', context)

def DSReviewList(request):
    ds = Console.objects.get(name='Nintendo DS')
    review_list = ds.reviews.all()
    context = RequestContext(request, {'review_list': review_list })
    return render(request, 'reviews/nintendo-ds.html', context)


def PCReviewList(request):
    pc = Console.objects.get(name='PC')
    review_list = pc.reviews.all()
    context = RequestContext(request, {'review_list': review_list })
    return render(request, 'reviews/pc.html', context)

def PSVitaReviewList(request):
    ps_vita = Console.objects.get(name='PS Vita')
    review_list = ps_vita.reviews.all()
    context = RequestContext(request, {'review_list': review_list })
    return render(request, 'reviews/ps-vita.html', context)



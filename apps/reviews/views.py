from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
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


def index(request):
    context = RequestContext(request, {})
    return render(request, 'reviews/index.html', context)

class ReviewDetail(DetailView):
    model = Review

    def get_context_data(self, **kwargs):
        context = super(ReviewDetail, self).get_context_data(**kwargs)
        context['pros'] = context['review'].pros.split(', ')
        context['cons'] = context['review'].cons.split(', ')
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

class ReviewUpdate(UpdateView):
    model = Review
    success_url = reverse_lazy('reviews:review_list')
    form_class = ReviewForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(ReviewUpdate, self).form_valid(form)


class ReviewDelete(DeleteView):
    model = Review
    success_url = reverse_lazy('reviews:review_list')

def like(request, id):
    if request.method == 'POST':
        user = request.user
        review = get_object_or_404(Review, id=id)
        like = Like.objects.get_or_create(review_id=review.id)

        try:
            user_liked = Like.objects.get(user=user, review_id=review.id)
        except:
            user_liked = None

        if user_liked:
            user_liked.total_likes -= 1
            user_liked.user.remove(request.user)
            user_liked.save()

        else:
            list(like)
            like[0].user.add(request.user)
            like[0].total_likes += 1
            like[0].save()

    return redirect(reverse_lazy('reviews:review_list'))

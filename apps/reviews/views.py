from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from apps.reviews.models import Review
from apps.reviews.forms import ReviewForm
from django.utils import timezone
from django.contrib.auth import authenticate


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
        return context

class ReviewCreate(CreateView):
    model = Review
    success_url = reverse_lazy('reviews:review_list')
    form_class = ReviewForm

class ReviewUpdate(UpdateView):
    model = Review
    success_url = reverse_lazy('reviews:review_list')
    form_class = ReviewForm

class ReviewDelete(DeleteView):
    model = Review
    success_url = reverse_lazy('reviews:review_list')


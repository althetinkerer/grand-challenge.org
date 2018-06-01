# -*- coding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files import File
from django.views.generic import ListView, CreateView, DetailView

from grandchallenge.algorithms.forms import AlgorithmForm, JobForm
from grandchallenge.algorithms.models import Algorithm, Job


class AlgorithmList(ListView):
    model = Algorithm


class AlgorithmCreate(LoginRequiredMixin, CreateView):
    # TODO: Permissions
    model = Algorithm
    form_class = AlgorithmForm

    def form_valid(self, form):
        # TODO: taken from evaluation uploads, create mixin?
        form.instance.creator = self.request.user

        uploaded_file = form.cleaned_data['chunked_upload'][0]
        with uploaded_file.open() as f:
            form.instance.image.save(uploaded_file.name, File(f))

        # TODO: Run nbconvert on the description and get the html

        return super().form_valid(form)


class AlgorithmDetail(DetailView):
    model = Algorithm


class JobList(ListView):
    model = Job


class JobCreate(CreateView):
    model = Job
    form_class = JobForm


class JobDetail(DetailView):
    model = Job

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Ad


# def home(request):
#     context = {
#         'ads': Ad.objects.all()
#     }
#     return render(request, 'adboard/home.html', context=context)


class AdListView(ListView):
    model = Ad
    template_name = 'adboard/home.html'
    context_object_name = 'ads'
    ordering = ['-pub_date']


class AdDetailView(DetailView):
    model = Ad


class AdCreateView(LoginRequiredMixin, CreateView):
    model = Ad
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AdUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Ad
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        ad = self.get_object()
        if self.request.user == ad.author:
            return True
        return False


class AdDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Ad
    success_url = '/adboard'

    def test_func(self):
        ad = self.get_object()
        if self.request.user == ad.author:
            return True
        return False

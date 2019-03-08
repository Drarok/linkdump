from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView

from .forms import LinkForm
from .models import Link


class Index(LoginRequiredMixin, TemplateView):
    template_name = 'links/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_links = self.request.user.links.all()
        paginator = Paginator(all_links, 50)
        page = self.request.GET.get('page')
        context['links'] = paginator.get_page(page)
        return context


class Add(LoginRequiredMixin, CreateView):
    form_class = LinkForm
    model = Link
    success_url = reverse_lazy('links:list')

    def form_valid(self, form):
        form.instance.user_id = self.request.user.pk
        return super().form_valid(form)


class Edit(LoginRequiredMixin, UpdateView):
    form_class = LinkForm
    model = Link
    success_url = reverse_lazy('links:list')


class Delete(LoginRequiredMixin, DeleteView):
    model = Link
    success_url = reverse_lazy('links:list')

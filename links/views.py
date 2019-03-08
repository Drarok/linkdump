from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView, FormView, CreateView

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


@login_required
@require_http_methods(['GET', 'POST'])
def edit(request, link_id):
    instance = get_object_or_404(Link, pk=link_id, user=request.user)
    form = LinkForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if request.POST.get('delete', None) == 'yes':
            instance.delete()
            return redirect('links:list')
        if form.is_valid():
            form.save()
            return redirect('links:list')
    return render(request, 'links/form.html', {'form': form})

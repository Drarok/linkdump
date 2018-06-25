from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_GET, require_http_methods

from .forms import LinkForm
from .models import Link


@login_required
@require_GET
def index(request):
    all_links = request.user.links.all()
    paginator = Paginator(all_links, 50)
    page = request.GET.get('page')
    context = {
        'links': paginator.get_page(page),
    }
    return render(request, 'links/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def add(request):
    form = LinkForm(request.POST or None, initial={'user': request.user})
    if request.method == 'POST':
        form.instance.user_id = request.user.pk
        if form.is_valid():
            form.save()
            return redirect('links')
    return render(request, 'links/form.html', {'form': form})


@login_required
@require_http_methods(['GET', 'POST'])
def edit(request, link_id):
    instance = get_object_or_404(Link, pk=link_id, user=request.user)
    form = LinkForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('links')
    return render(request, 'links/form.html', {'form': form})

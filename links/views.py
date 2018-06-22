from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Link


def index(request):
    all_links = Link.objects.all()
    paginator = Paginator(all_links, 50)
    page = request.GET.get('page')
    context = {
        'links': paginator.get_page(page),
    }
    return render(request, 'links/index.html', context)

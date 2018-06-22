from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render


@login_required
def index(request):
    all_links = request.user.links.all()
    paginator = Paginator(all_links, 50)
    page = request.GET.get('page')
    context = {
        'links': paginator.get_page(page),
    }
    return render(request, 'links/index.html', context)

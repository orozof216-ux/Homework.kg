from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models
from django.core.paginator import Paginator
from django.db.models import F


def seacrh_view(request):
    query = request.GET.get('s', '')
    if query:
        query_blog = models.Blog.objects.filter(title__icontains=query)
    else:
        return HttpResponse('Блог не найден')

    return render(request,'blog_list.html', {'blog': query_blog})






def blog_detail_view(request, id):
    if request.method == 'GET':
        blog_id = get_object_or_404(models.Blog, id=id)
        views_blog = request.session.get('viewd_blog', [])

        if id not  in views_blog:
            blog_id.views =  F("views") + 1
            blog_id.save()
            blog_id.refresh_from_db()
    
        views_blog.append(id)
        request.session['viewd_blog'] = views_blog


    return render(request, 'blog_detail.html', {'blog_id': blog_id})


def blog_list_view(request):
    if request.method == 'GET':
        query_blog = models.Blog.objects.all().order_by('-id')
        paginator = Paginator(query_blog, 2)
        page = request.GET.get('page')
        page_obj = paginator.get_page(page)
    return render(request, 'blog_list.html', {'blog': page_obj})







# Create your views here.
def message(request):
    return HttpResponse('Это мой первый проект на DJANGO')

def emodji(request):
    return HttpResponse('😀😄🤬🫨🙃💩')
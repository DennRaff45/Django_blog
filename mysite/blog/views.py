from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

"""Указанная функция извлекает объект, соответствующий передан-
ным параметрам, либо исключение HTTP с кодом состояния, равным 404 (не
найдено), если объект не найден"""


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    return render(request,
                  'blog/post/detail.html',
                  {'post': post}
                  )


"В этом представлении извлекаются все посты со статусом PUBLISHED используя менеджер published"


def post_list(request):
    posts = Post.published.all()
    "Постраничная разбивка с 3 постами на страницу"
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        "Если page_number находится вне диапазона, то выдать последнюю страницу"
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'blog/post/list.html',
                  {'posts': posts})

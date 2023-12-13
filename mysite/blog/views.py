from django.shortcuts import render, get_object_or_404
from .models import Post

"""Указанная функция извлекает объект, соответствующий передан-
ным параметрам, либо исключение HTTP с кодом состояния, равным 404 (не
найдено), если объект не найден"""


def post_detail(request, pk):
    post = get_object_or_404(Post,
                             pk=pk,
                             status=Post.Status.PUBLISHED)

    return render(request,
                  'blog/post/detail.html',
                  {'post': post}
                  )


"В этом представлении извлекаются все посты со статусом PUBLISHED используя менеджер published"


def post_list(request):
    posts = Post.published.all()
    return render(request,
                  'blog/post/list.html',
                  {'posts': posts})

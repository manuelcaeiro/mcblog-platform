from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from .models import Post


def user_is_post_author(function):
    def wrap(request, pk):
        post = Post.objects.get(pk=pk)
        if post.author == request.user:
            return function(request, pk)
        else:
            #messages.error(request, "You are not the author of this post.")
            raise PermissionDenied
        
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
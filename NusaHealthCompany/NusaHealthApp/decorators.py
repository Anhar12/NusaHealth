from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from functools import wraps

def admin_required():
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.is_superuser and request.user.is_staff:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('sign-in')
        return _wrapped_view
    return decorator
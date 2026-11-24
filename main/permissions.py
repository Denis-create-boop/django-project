from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied
from django.contrib.auth.views import redirect_to_login
from functools import wraps

def can_manage(user):
    return user.is_authenticated and user.is_active and user.is_superuser

def manager_required(view):
    @wraps(view)
    def wrapped(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect_to_login(request.get_full_path(), login_url='/login/')
        if not can_manage(request.user):
            raise PermissionDenied
        return view(request, *args, **kwargs)
    return wrapped

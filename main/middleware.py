from django.core.exceptions import PermissionDenied
from django.contrib.auth.views import redirect_to_login
from .permissions import can_manage

class CatalogPermissionsMiddleware:
    """Restrict every existing catalog write route, including direct requests."""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        match = request.resolver_match
        name = match.url_name if match else ''
        name = name or ''
        if name == 'add' or name.startswith('create_') or name.endswith(('-update', '-delete')):
            if not request.user.is_authenticated:
                return redirect_to_login(request.get_full_path(), login_url='/login/')
            if not can_manage(request.user):
                raise PermissionDenied
        return None

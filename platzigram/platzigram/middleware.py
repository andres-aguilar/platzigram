from django.urls import reverse
from django.shortcuts import redirect


class ProfileContetitionMiddleware:
    """ ProfileContetitionMiddleware """

    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        # import pdb; pdb.set_trace()
        if not request.user.is_anonymous:
            profile = request.user.profile

            if not profile.picture or not profile.biography:
                if request.path not in [reverse('update_profile'), reverse('logout')]:
                    return redirect('update_profile')

        response = self.get_response(request)
        return response
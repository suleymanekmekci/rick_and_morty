from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect,HttpResponseNotFound
from django.shortcuts import get_object_or_404
from .utils import APIAccess

# Create your views here.

def index(request):
    page = int(request.GET.get('page', 1))
    api_access = APIAccess(page)
    episode = api_access.get_current_episode()

    next_episode_check = APIAccess(page + 1).get_current_episode()
    if episode:
        context = {
            "page": page,
            "next_page" : page + 1,
            "previous_page" : page - 1,
            "episode": episode,
            "is_next_page" : True if next_episode_check else False
        }

    # if request.method == "GET":
    return render(request=request, context=context, template_name='index.html')


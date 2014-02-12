from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext

def global_settings(request):
    """Returns extra variables to the context """
    return{'MEDIA_URL': settings.MEDIA_URL, 
           'ROOT_URL': settings.ROOT_URL,
           }

def render_response(req, *args, **kwargs):
    kwargs['context_instance'] = RequestContext(req)
    return render_to_response(*args, **kwargs)

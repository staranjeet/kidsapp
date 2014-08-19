from django.core.context_processors import csrf
from django.template import RequestContext
from django.template import loader, Context
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, \
    HttpResponseRedirect, HttpResponseNotFound
from django.conf import settings
import json
# Create your views here.
def home(request):
	return render_to_response('index.html', context_instance=RequestContext(request))

def level1(request):
	return render_to_response('level1.html', context_instance=RequestContext(request))

def level2(request):
	return render_to_response('level2.html', context_instance=RequestContext(request))

def level3(request):
	return render_to_response('level3.html', context_instance=RequestContext(request))

def level4(request):
	return render_to_response('level4.html', context_instance=RequestContext(request))

	# return HttpResponse("Coming soon level4 page !!!!")


# def home(request):    
#     """ landing page. """
#     c = {}
#     c.update(csrf(request))
#     return render_to_response('index.html', context_instance=RequestContext(request))
# # 	return HttpResponse("This page is under construction")

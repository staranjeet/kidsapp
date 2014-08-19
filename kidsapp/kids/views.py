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
	return HttpResponse("Coming soon Home page  !!!!")

def level1(request):
	return HttpResponse("Coming soon level1 page !!!!")

def level2(request):
	return HttpResponse("Coming soon level2 page !!!!")

def level3(request):
	return HttpResponse("Coming soon level3 page !!!!")

def level4(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('index.html', context_instance=RequestContext(request))

	# return HttpResponse("Coming soon level4 page !!!!")


# def home(request):    
#     """ landing page. """
#     c = {}
#     c.update(csrf(request))
#     return render_to_response('index.html', context_instance=RequestContext(request))
# # 	return HttpResponse("This page is under construction")

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
def levels(request):
	return render_to_response('levels.html', context_instance=RequestContext(request))
def parallax(request):
	return render_to_response('parallax.html', context_instance=RequestContext(request))

def level11(request):
	return render_to_response('level11.html', context_instance=RequestContext(request))

def level12(request):
	return render_to_response('1_2.html', context_instance=RequestContext(request))

def level13(request):
	return render_to_response('1_3.html', context_instance=RequestContext(request))

def level14(request):
	return render_to_response('1_4.html', context_instance=RequestContext(request))

def level15(request):
	return render_to_response('level15.html', context_instance=RequestContext(request))

def level21(request):
	return render_to_response('2_1.html', context_instance=RequestContext(request))

def level22(request):
	return render_to_response('2_2.html', context_instance=RequestContext(request))

def level23(request):
	return render_to_response('2_3.html', context_instance=RequestContext(request))

def level24(request):
	return render_to_response('2_4.html', context_instance=RequestContext(request))
def level25(request):
	return render_to_response('level25.html', context_instance=RequestContext(request))


def level31(request):
	return render_to_response('3_1.html', context_instance=RequestContext(request))

def level32(request):
	return render_to_response('3_2.html', context_instance=RequestContext(request))

def level33(request):
	return render_to_response('3_3.html', context_instance=RequestContext(request))

def level34(request):
	return render_to_response('3_4.html', context_instance=RequestContext(request))

def level41(request):
	return render_to_response('4_1.html', context_instance=RequestContext(request))

def level42(request):
	return render_to_response('4_2.html', context_instance=RequestContext(request))

def level43(request):
	return render_to_response('4_3.html', context_instance=RequestContext(request))

def level44(request):
	return render_to_response('4_4.html', context_instance=RequestContext(request))
def level45(request):
	return render_to_response('4_5.html', context_instance=RequestContext(request))

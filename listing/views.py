import yaml
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from listing.models import Property
from django.core.paginator import Paginator

def index(request):
	properties = Property.objects.all()
	#current_properties = None
	#if properties:
		#paginator = Paginator(properties, 15) # 15 per page
		#page = request.GET.get('page', 1)	
		#current_properties = paginator.page(page)
	return render_to_response('listing/index.html',
		{'properties': properties,'all_properties': properties},
		context_instance=RequestContext(request))

def detail(request, property_id):
	prop = get_object_or_404(Property, pk=property_id)
	return render_to_response('listing/detail.html', {'property': prop}, context_instance=RequestContext(request))	

def init(request):
	with open(request.POST.get('file_path'), 'r') as stream:
		properties = yaml.load(stream)['properties']

	map(lambda prop: Property.objects.create(**prop), properties)

	return HttpResponseRedirect(reverse(index))

def delete(request):
	Property.objects.all().delete()	
	return HttpResponseRedirect(reverse(index))
from data.models import Info, Detail
from django.core.serializers.json import DjangoJSONEncoder
from django.forms.models import model_to_dict
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.utils import simplejson
import twitter
import json

CONSUMER_KEY = 'lqbJBMhff9WQPF2RcNR8g'
CONSUMER_SECRET = 'dxQkE08TVnsUY2AqomHwJIRkke1kKQQLjHNrCF24s'
OAUTH_TOKEN = '14410838-pDUL6xMHcnB2vawEOsy4MbsX9MPRElzrF1PoYYv2M'
OAUTH_TOKEN_SECRET = 'TGFlChHw0JBVe1rPXOH30CuE9ObkhAEDic0THrL22c'
WORLD_WOE_ID = 1 


def index(request):
    info_list = Info.objects.all().order_by('id')
    return render_to_response('data/index.html', {'info_list': info_list})

def tester2(request):   
    bundle = []
    details = Detail.objects.filter(info=request.GET['id']).order_by('id')
    for detail in details:
        dict_detail = model_to_dict(detail)
        bundle.append(dict_detail)
    return HttpResponse(simplejson.dumps(bundle, cls=DjangoJSONEncoder, indent=4))

def tester(request):   
    bundle = []
    infos = Info.objects.all().order_by('id')
    for info in infos:
        dict_info = model_to_dict(info)
        dict_info['details'] = [];
        details = Detail.objects.filter(info=info).order_by('id')
        for detail in details:
            dict_info['details'].append(model_to_dict(detail))    
        bundle.append(dict_info)
    return HttpResponse(simplejson.dumps(bundle, cls=DjangoJSONEncoder, indent=4))  

def trends(request):
    #http://nbviewer.ipython.org/urls/raw.github.com/ptwobrussell/Mining-the-Social-Web/master/ipython_notebooks/Chapter1.ipynb
    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)   
    twitter_api = twitter.Twitter(domain='api.twitter.com', api_version='1.1', auth=auth)
    world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID) 
    return HttpResponse(json.dumps(world_trends, indent=1))
# Create your views here.

from django.shortcuts import render_to_response
from models import *


def HomePage(request):
    topic_list = TopicAreas.objects.filter(homepage=1).order_by('topic_key')
    return render_to_response('home.html', {"topic_list": topic_list})


def AboutMe(request):
    return render_to_response('about.html')


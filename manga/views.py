from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
import subprocess
import os
from django.utils.datastructures import MultiValueDictKeyError
from .models import Manga
# from . models import User, Job
# import requests
import json
# Create your views here.
# templates_path = "F:\\Projects\\FastManga\\manga\\templates"

def home(request):
    template = loader.get_template('manga/home.html')
    # return render(request, templates_path + '\\manga\\home.html')
    context = {}
    return HttpResponse(template.render(context, request))

def login(request):
    return HttpResponse("day la trang dang nhap")

def register(request):
    return HttpResponse("day la trang dang ky")

def all_manga(request):
    return HttpResponse("day la trang view truyen")

def detail_manga(request, manga_id):
    manga = Manga.objects.get(code=manga_id)
    return HttpResponse("day la trang detail manga", manga_id)

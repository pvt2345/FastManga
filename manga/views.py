from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
import subprocess
import os
from django.utils.datastructures import MultiValueDictKeyError
from .models import Manga, Chapter, User, Author
# from . models import User, Job
# import requests
import json
from .utils import top3recentchapter, updated_time_templates
# templates_path = "F:\\Projects\\FastManga\\manga\\templates"
def home(request):
    template = loader.get_template('manga/home.html')
    # return render(request, templates_path + '\\manga\\home.html')
    manga_query_set = Manga.objects.order_by('-last_updated')[:12]
    # for item in mangas:
    mangas = []
    #lấy ra mangas + top 3 chap gần nhất + thời gian từng chap
    for item in manga_query_set:
        top3_recent_chap_list = [{'time_text' : updated_time_templates(chap), 'main' : chap} for chap in top3recentchapter(item)]
        mangas.append({'main' : item, 'top3_recent_chap_list' : top3_recent_chap_list})

    top_10_popular_manga_query_set = Manga.objects.order_by('-views')[:10]
    # top_8_popular_manga_most_recent_chapter_name = [item.chapter_set.order_by('-last_updated')[0].name for item in top_8_popular_manga]

    #lấy ra top 10 popular manga + tên chap gần nhất
    top_10_popular_mangas = []
    for item in top_10_popular_manga_query_set:
        most_recent_chapter_name = item.chapter_set.order_by('-last_updated')[0].name
        top_10_popular_mangas.append({'main' : item, 'most_recent_chapter_name' : most_recent_chapter_name})

    context = {
        'mangas' : mangas,
        'top_10_popular_mangas' : top_10_popular_mangas,
    }

    print(top_10_popular_mangas)
    return HttpResponse(template.render(context, request))

def login(request):
    return HttpResponse("day la trang dang nhap")

def register(request):
    return HttpResponse("day la trang dang ky")

def all_manga(request):
    return HttpResponse("day la trang view truyen")

def detail_manga(request, manga_code):

    top_10_popular_manga_query_set = Manga.objects.order_by('-views')[:10]
    top_10_popular_mangas = []
    for item in top_10_popular_manga_query_set:
        most_recent_chapter_name = item.chapter_set.order_by('-last_updated')[0].name
        top_10_popular_mangas.append({'main' : item, 'most_recent_chapter_name' : most_recent_chapter_name})

    manga = Manga.objects.get(code=manga_code)
    genres = manga.genre.all()
    authors = manga.author.all()
    chapters_query_set = manga.chapter_set.all()
    # rating = 
    template = loader.get_template('manga/manga.html')
    chapters_updated_text = [updated_time_templates(item) for item in chapters_query_set]
    chapters = []
    for i in range(len(chapters_query_set)):
        chapters.append({'main' : chapters_query_set[i], 'updated_text' : chapters_updated_text[i] })
    context = {
        'manga' : manga,
        'genres' : genres,
        'chapters' : chapters,
        'first_author': authors[0],
        'first_genre' : genres[0],
        'top_10_popular_mangas' : top_10_popular_mangas
    }
    if len(authors) > 1:
        context['remain_authors'] = authors[1:]

    if len(genres) > 1:
        context['remain_genres'] = genres[1:]

    manga.views += 1
    manga.save()

    print(context)
    return HttpResponse(template.render(context, request))
    
def chapter(request):
    return HttpResponse("day la trang chapter")
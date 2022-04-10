from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
import sqlite3
import random
# Create your views here.

#Post.objects.all()
def home(request):
    context = {
        'posts':Post.objects.all().order_by('-id')
    }
    return render(request, "home.html", context)

def getPost(request, url):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM home_post WHERE url LIKE ?', ('%' + url + '%',))
    postResult = [dict(title=ra[0], content=ra[1], thumbnail=ra[2], datePosted=ra[3], category=ra[4]) for ra in cursor.fetchall()]
    return render(request, 'result.html', {'postResults':postResult, 'title':postResult[0]["title"]})

# def getCategory(request):
#     context = {
#         'posts':Post.objects.all().order_by('-id')
#     }
#     return render(request, 'home.html', context)

def aboutPage(request):
    return render(request, 'about.html')

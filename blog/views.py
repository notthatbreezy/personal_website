# Create your views here.

from django.shortcuts import render_to_response
from models import *
from django.core.paginator import Paginator, InvalidPage, EmptyPage


def Blog(request):
    """Main listing."""
    posts = Post.objects.all().order_by("-created")
    paginator = Paginator(posts, 2)
    recent_posts = Post.objects.all().order_by("-created")[:4]
    links = LinksToRead.objects.all()

    try:
        page = int(request.GET.get("page", '1'))
    except ValueError:
        page = 1

    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)

    return render_to_response("BlogTemplate.html", {"posts": posts, "links": links, "recentposts": recent_posts})


def Article(request, post_num):
    """Page for Post"""
    post = Post.objects.get(pk=post_num)
    posts = Post.objects.all().order_by("-created")
    paginator = Paginator(posts, 2)
    recent_posts = Post.objects.all().order_by("-created")[:4]
    links = LinksToRead.objects.all()

    try:
        page = int(request.GET.get("page", '1'))
    except ValueError:
        page = 1

    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)
    return render_to_response("BlogTemplate.html", {"post": post, "posts": posts, "links": links, "recentposts": recent_posts})


def CodeAndData(request):
    """Page for Code and Data"""
    recent_posts = Post.objects.all().order_by("-created")[:4]
    links = LinksToRead.objects.all()
    posts = Code.objects.all().order_by("-created")

    return render_to_response("OtherContentTemplate.html", {"posts": posts, "links": links, "recentposts": recent_posts})


def ProjectContent(request):
    """Page for Projects that I'm Working on"""
    recent_posts = Post.objects.all().order_by("-created")[:4]
    links = LinksToRead.objects.all()
    posts = Projects.objects.all()

    return render_to_response("OtherContentTemplate.html", {"posts": posts, "links": links, "recentposts": recent_posts})


def ResearchContent(request):
    """Page for Projects that I'm Working on"""
    recent_posts = Post.objects.all().order_by("-created")[:4]
    links = LinksToRead.objects.all()
    posts = Research.objects.all()

    return render_to_response("OtherContentTemplate.html", {"posts": posts, "links": links, "recentposts": recent_posts})

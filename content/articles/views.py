import json

from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt

from articles.models import Article


@csrf_exempt
@login_required
def add_article(request):
    """
    This method helps one to add article and persist it in the db.
    In the post request we would get the title, content and the author details.
    :param request:
    :return:
    """
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        title = body["title"]
        content = body["Content"]
        author_name = body["Author"]

        try:
            article = Article(title=title, content=content,
                              author_name=author_name)
            article.save()
            return JsonResponse({"status": True})
        except Exception:
            return JsonResponse({"status": True})
    else:
        return render_to_response('add.html', {"user": request.user})


def listing_article(request):
    """
    This API helps one to view all the articles listed so far.
    :param request:
    :return:
    """

    if request.method == 'GET':
        can_vote = False
        article_list = Article.objects.all().order_by('-count')
        page = request.GET.get('page', 1)
        paginator = Paginator(article_list, 3)
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            articles = paginator.page(1)
        except EmptyPage:
            articles = paginator.page(paginator.num_pages)
        if request.user.is_authenticated:
            can_vote = True
        return render_to_response('list.html', {"result": articles,
                                                "can_vote": can_vote,
                                                "user": request.user})


@csrf_exempt
@login_required
def vote(request):
    """
    This API captures the vote the user would have voted
    for and persists it in the database.
    :param request:
    :return:
    """
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        article_id = body['article_id']
        try:
            article = Article.objects.get(id=article_id)
            article_count = article.count + 1
            article.count = article_count
            article.save()
            return JsonResponse({"status": True})
        except Exception:
            return JsonResponse({"status": False})

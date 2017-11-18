from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Question

def index(req):
  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  context = { 'latest_question_list': latest_question_list }
  return render(req, 'polls/index.html', context)

def detail(req, question_id):
  return HttpResponse("You're looking at question %s." % question_id)

def results(req, question_id):
  res = "You're looking at the results of question %s."
  return HttpResponse(res % question_id)

def vote(req, question_id):
  return HttpResponse("You're voting on question %s." % question_id)
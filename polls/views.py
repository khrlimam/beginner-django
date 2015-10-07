from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Questions
from django import middleware
# Create your views here.

def index(request):
    latest_question_list = Questions.objects.order_by('-pub_date')[:5]
    template = 'polls/index.html'
    context = {'latest_question_list': latest_question_list}
    return render(request, template, context)

def detail(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    return render(request, "polls/detail.html", {'question':question})
    
def results(request, question_id):
    response = 'Your\'re looking at results of the question id %s.'
    return HttpResponse(response % question_id)
    
def vote(request, question_id):
    return HttpResponse("You're vooting on question id %s" % question_id)
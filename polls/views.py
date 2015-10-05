from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, RequestContext
from .models import Questions
# Create your views here.

def index(request):
    latest_question_list = Questions.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {'latest_question_list': latest_question_list})
    return HttpResponse(template.render(context))

def detail(request, question_id):
    return HttpResponse('You\'re looking question at %s' % question_id)
    
def results(request, question_id):
    response = 'Your\'re looking at results of the question id %s.'
    return HttpResponse(response % question_id)
    
def vote(request, question_id):
    return HttpResponse("You're vooting on question id %s" % question_id)
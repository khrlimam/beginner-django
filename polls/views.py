from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .models import Questions, Choices


# Create your views here.

def index(request):
    latest_question_list = Questions.objects.order_by('-pub_date')[:5]
    template = 'polls/index.html'
    context = {'latest_question_list': latest_question_list}
    return render(request, template, context)


def detail(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    return render(request, "polls/detail.html", {'question': question})


def results(request, question_id):
    q = Questions.objects.get(pk=question_id)
    return render(request, 'polls/result.html', {
        'success_message':'Successfully adding vote to choice of question %s' % q.question_text})


def vote(request, question_id):
    p = get_object_or_404(Questions, pk=question_id)
    try:
        selected_choice = p.choices_set.get(pk=request.POST['choice'])
    except(KeyError, Choices.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'error_message': 'You have to choice something!',
            'question':p})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:result', args=(p.id,)))

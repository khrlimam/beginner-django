from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from django.utils import timezone

from .models import Questions, Choices


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        # with filter pub_date__lte we filter the question that published less or equal to recent time
        return Questions.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailsView(generic.DetailView):
    model = Questions
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Questions.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Questions
    template_name = 'polls/result.html'


def vote(request, question_id):
    q = get_object_or_404(Questions, pk=question_id)
    try:
        selected_choice = q.choices_set.get(pk=request.POST['choice'])
    except(KeyError, Choices.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'error_message': 'You have to choose something!',
            'question': q})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:result', args=(q.id,)))

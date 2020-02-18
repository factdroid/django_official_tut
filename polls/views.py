from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from polls.models import Question, Choice
from django.urls import reverse
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


# This is adding another view: About
def about(request):
    return HttpResponse("This is the about view")


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    context_dict = {}
    context_dict['question'] = get_object_or_404(Question, pk=question_id)
    try:
        context_dict['selected_choice'] = context_dict['question'].choice_set.get(pk=request.POST['choice'])      
    except (KeyError, Choice.DoesNotExist):
        context_dict['error_message'] = "You didn't select a choice!"
        return render(request, 'polls/detial.html', context=context_dict)
    else:
        context_dict['selected_choice'].votes += 1
        context_dict['selected_choice'].save()
        return HttpResponseRedirect(reverse('polls:results', args=(context_dict['question'].id,)))
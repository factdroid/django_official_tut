from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from polls.models import Question


def index(request):
    context_dict = {}
    context_dict['list_of_questions'] = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'polls/index.html', context=context_dict)


# This is adding another view: About
def about(request):
    return HttpResponse("This is the about view")


def detail(request, question_id):
    context_dict = {}
    context_dict['question'] = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", context=context_dict)


def results(request, question_id):
    response = "You're looking at the results for question %s." % question_id
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

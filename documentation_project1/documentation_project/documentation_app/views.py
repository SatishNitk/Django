from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Choice,Question
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.views import generic
# Create your views here.

def index(request):
	return HttpResponse("<h1>hi there welcome to documentaion app by django</h1>")

# handle 404 exception
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'documentation_app/details.html', {'question': question})
    
#handle 404 with shortcut way
def detail404(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'documentation_app/details.html', {'question': question})

class DetailView(generic.DetailView):
    model = Question
    template_name = 'documentation_app/details.html'


# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'documentation_app/results.html', {'question': question})

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'documentation_app/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'documentation_app/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('documentation_app:results', args=(question.id,)))

def latest_question(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ','.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


# bottom all continuoud three method are for same purpose

# never try to use double __ it will give circular_inport problem
def latest_questionhtml(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('documentation_app/index.html')
    context = {
      'latest_question_list' : latest_question_list,
    }
    return HttpResponse(template.render(context,request))

#above code changed to listview
class LatestQuestionhtmView(generic.ListView):
    template_name = 'documentation_app/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


def latest_questionhtml1(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'documentation_app/index.html', context)






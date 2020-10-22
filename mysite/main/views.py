from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Question, Choice
from .forms import CreateNewPoll
from django.template import loader
from django.views import generic
from django.urls import reverse

# Create your views here.

def index(response, id):
    question = Question.objects.get(id=id)

    if response.method == "POST":
        if response.POST.get("newChoice"):
            txt = response.POST.get("new")
            question.choice_set.create(choice_text=txt, votes=0)
        elif response.POST.get("vote"):
            return HttpResponseRedirect("/%i/vote" %question.id)

    return render(response, "main/questions.html", {"question":question})

def home(request):
    context = {
        'questions': Question.objects.all()
    }
    return render(request, "main/home.html", context)

def create(response):
    if response.method == "POST":
        form = CreateNewPoll(response.POST)
        
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = Question(question_text=n)
            t.save()
            response.user.question.add(t)

        return HttpResponseRedirect("/%i" %t.id)

    else:
        form = CreateNewPoll()
    return render(response, "main/create.html", {"form": form})

def view(request):
    question = Question.objects.all()
    
    return render(request, "main/view.html", {"question":question})

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'main/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'main/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('main:results', args=(question_id,)))

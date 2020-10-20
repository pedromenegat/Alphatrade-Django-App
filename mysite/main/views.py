from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from .forms import CreateNewPoll

# Create your views here.

def index(response, id):
    question = Question.objects.get(id=id)
    return render(response, "main/questions.html", {"question":question})

def home(response):
    return render(response, "main/home.html", {})

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

def view(response):
    return render(response, "main/view.html", {})
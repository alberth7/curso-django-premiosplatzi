from ast import arg
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question

# Create your views here.

# def index(request):
#     latest_question_list = Question.objects.all()
#     return render(request, "polls/index.html", {
#         "latest_question_list": latest_question_list
#     })



'''
The first
'''
# def index(request):
#     return HttpResponse("Esta es la pagina principal de Platzi App.")

# def detail(request, question_id):
#     return HttpResponse(f"Estas viendo la pregunta numero {question_id}")
''''''

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions"""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]


# def detail(request, question_id):
#     #question = Question.objects.get(pk=question_id)
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/detail.html",{
#         "question": question
#     })


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


'''
The first
'''

# def results(request, question_id):
#    return HttpResponse(f"Estas viendo los resultados de la pregunta numero {question_id}")
''''''
# def results(request, question_id):
#     question = get_object_or_404(Question, pk = question_id)
#     return render(request, "polls/results.html", {
#         "question": question
#     })

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


'''
The first
'''
# def vote(request, question_id):
#     return HttpResponse(f"Estás votando a la pregunta número {question_id}")
''''''

def vote(request, question_id):
    question =  get_object_or_404(Question, pk = question_id)
    try:
         # choice hace referencia al name de detail.html
        selected_choice = question.choice_set.get(pk=request.POST["choice"]) 

    except(KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html",{
            "question": question,
            "error_message": "No elegiste una respuesta"
        })
    # SI todo salio bien
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))
    # HttpResponseRedirect verifica que el susuario no envie dos veces el mismo formulario


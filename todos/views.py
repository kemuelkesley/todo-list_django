from django.shortcuts import render

from .models import Todo


def todo_list(request):
    # nome = "Rafael"
    # alunos = ["Kemuel kesley", "Ariel Sardinha", "Anna Beatriz"]
    todos = Todo.objects.all()
    return render(request, "todos/todo_list.html", {"todos": todos})

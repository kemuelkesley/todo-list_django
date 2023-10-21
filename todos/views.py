from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Todo


# def todo_list(request):
#     nome = "Rafael"
#     alunos = ["Kemuel kesley", "Ariel Sardinha", "Anna Beatriz"]
#     todos = Todo.objects.all()
#     return render(request, "todos/todo_list.html", {"todos": todos})


class TodoListView(ListView):
    model = Todo


class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")


class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")


class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")

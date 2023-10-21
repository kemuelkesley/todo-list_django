from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy

from django.shortcuts import get_object_or_404, redirect
from datetime import date

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


class TodoCompleteView(View):
    def get(self, request, pk):
        Todo.objects.get(pk=pk)
        todo = get_object_or_404(Todo, pk=pk)
        todo.mark_has_complete()
        todo.save()

        return redirect("todo_list")

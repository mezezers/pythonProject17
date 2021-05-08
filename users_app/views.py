from django.shortcuts import render
from django.views.generic import ListView, View,  DetailView, UpdateView, DeleteView, ListView
from users_app.models import User
from django.urls import reverse_lazy
from .forms import UserAddForm


class AddUserView(View):
    def post(self, request):

        form = UserAddForm(request.POST)
        if form.is_valid():
            u = form.save()
            users = User.objects.all()

            return render(request, 'index.html', {'users': users})

    def get(self, request):
        form_class = UserAddForm

        return render(request, 'userdetails.html', {
            'form': form_class,
        })


class IndexView(ListView):
    model = User

class GetUserView(DetailView):
    model = User

class EditUserView(UpdateView):
    model = User
    fields = ['username', 'email']
    success_url = reverse_lazy('main')

class DeleteUserView(DeleteView):
    model = User
    success_url = reverse_lazy('main')





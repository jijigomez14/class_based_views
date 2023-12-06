from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import LoginTable

class LoginCreate(CreateView):
    # specify the model for create view
    model = LoginTable

    # specify the fields to be displayed
    fields = ['username', 'password']

    # specify the template name
    template_name = 'login.html'  # Replace 'your_template_name.html' with the actual template name

from django.views.generic.list import ListView
from .models import LoginTable

class LoginListView(ListView):
    model = LoginTable
    template_name = 'login_list.html'  # Replace with the actual template name
    context_object_name = 'login_list'  # Specify the variable name in the template for the queryset



from django.views.generic.detail import DetailView
from .models import LoginTable

class LoginDetailView(DetailView):
    model = LoginTable
    template_name = 'login_detail.html'  # Replace with the actual template name
    context_object_name = 'login'  # Specify the variable name in the template for the object


from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .models import LoginTable

class LoginUpdateView(UpdateView):
    model = LoginTable
    template_name = 'login_update.html'  # Replace with the actual template name
    fields = ['username', 'password']

    def get_success_url(self):
        return reverse_lazy('login_list')

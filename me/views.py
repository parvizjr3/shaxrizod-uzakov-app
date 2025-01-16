from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.urls import reverse_lazy
from .forms import ContactForm
from .models import Contact



# bu index view template uchun
# class IndexView(TemplateView):
#     template_name = 'index.html'


from .models import Work
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['works'] = Work.objects.all()  # Fetch all works from the database
        return context


#bu rahmat template uchun
class ThankYouView(TemplateView):
    template_name = 'thank_you.html'



# bu dashboard niki
class DashboardView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'dashboard.html'
    login_url = 'me:login'  # Redirect to login page if not logged in

    def test_func(self):
        return self.request.user.is_superuser  # or any other condition you prefer


class ContactView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'index.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('me:thank_you')  # Redirect to the thank you page
        return render(request, 'index.html', {'form': form})

# bu crud amallari, CONTACKT LIST UCHUN
class ContactListView(LoginRequiredMixin, ListView):
    model = Contact
    template_name = 'contact_list.html'
    context_object_name = 'contacts'
    login_url = 'me:login'  # Redirect to login page if not logged in



class ContactCreateView(LoginRequiredMixin, CreateView):
    model = Contact
    template_name = 'contact_form.html'
    fields = ['name', 'surname', 'email', 'phone_number', 'message']
    success_url = reverse_lazy('me:contact_list')
    login_url = 'me:login'  # Redirect to login page if not logged in

class ContactUpdateView(LoginRequiredMixin, UpdateView):
    model = Contact
    template_name = 'contact_form.html'
    fields = ['name', 'surname', 'email', 'phone_number', 'message']
    success_url = reverse_lazy('me:contact_list')
    login_url = 'me:login'  # Redirect to login page if not logged in

class ContactDeleteView(LoginRequiredMixin, DeleteView):
    model = Contact
    template_name = 'contact_confirm_delete.html'
    success_url = reverse_lazy('me:contact_list')
    login_url = 'me:login'  # Redirect to login page if not logged in

class ContactDetailView(LoginRequiredMixin, DetailView):
    model = Contact
    template_name = 'contact_detail.html'
    context_object_name = 'contact'
    login_url = 'me:login'  # Redirect to login page if not logged in

################################################################################################3



from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Work  # Assuming the model is named Work

class WorkListView(LoginRequiredMixin, ListView):
    model = Work
    template_name = 'work_list.html'
    context_object_name = 'works'
    login_url = 'me:login'  # Redirect to login page if not logged in

from .forms import WorkForm 
from django.views.generic import CreateView
from .models import Work

class WorkCreateView(CreateView):
    model = Work
    form_class = WorkForm  # Use the custom form
    template_name = 'work_form.html'
    success_url = reverse_lazy('me:work_list')



from django.urls import reverse_lazy
from django.views.generic import UpdateView
from .models import Work
from .forms import WorkForm  # Import the correct form

class WorkUpdateView(UpdateView):
    model = Work
    form_class = WorkForm  # Make sure you're using the correct form
    template_name = 'work_form.html'
    success_url = reverse_lazy('me:work_list')  




class WorkDeleteView(LoginRequiredMixin, DeleteView):
    model = Work
    template_name = 'work_confirm_delete.html'
    success_url = reverse_lazy('me:work_list')
    login_url = 'me:login'  # Redirect to login page if not logged in

class WorkDetailView(LoginRequiredMixin, DetailView):
    model = Work
    template_name = 'work_detail.html'
    context_object_name = 'work'
    login_url = 'me:login'  # Redirect to login page if not logged in




#########################################################33



from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Category  # Assuming the model is named Category

# List view for displaying categories
class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'
    login_url = 'me:login'  # Redirect to login page if not logged in

# Create view for adding a new category
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .models import Category
from .forms import CategoryForm

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm  # Use the custom form
    template_name = 'category_form.html'
    success_url = reverse_lazy('me:category_list')
    login_url = 'me:login'  # Redirect to login page if not logged in





# Update view for editing an existing category
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from .models import Category
from .forms import CategoryForm

class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm  # Use the custom form for editing
    template_name = 'category_form.html'
    success_url = reverse_lazy('me:category_list')
    login_url = 'me:login'  # Redirect to login page if not logged in

# Delete view for deleting a category
class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'category_confirm_delete.html'
    success_url = reverse_lazy('me:category_list')
    login_url = 'me:login'  # Redirect to login page if not logged in

# Detail view for viewing a specific category
class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category
    template_name = 'category_detail.html'
    context_object_name = 'category'
    login_url = 'me:login'  # Redirect to login page if not logged in




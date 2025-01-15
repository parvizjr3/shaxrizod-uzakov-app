from django.urls import path
from django.contrib.auth import views as auth_views

from .views import (
    IndexView,
    ContactView,
    ThankYouView,
    DashboardView,
    ContactListView,
    ContactCreateView,
    ContactUpdateView,
    ContactDeleteView,
    ContactDetailView,
    CategoryListView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView,
    CategoryDetailView,  # Import CategoryDetailView
    WorkListView,
    WorkCreateView,
    WorkUpdateView,
    WorkDeleteView,
    WorkDetailView,  # Import WorkDetailView
)

# me/urls.py
app_name = 'me'  # Only declare app_name once

urlpatterns = [
    path('', IndexView.as_view(), name='index_page'),
    path('contact/', ContactView.as_view(), name='contact_view'),
    path('thank-you/', ThankYouView.as_view(template_name="thank_you.html"), name="thank_you"),
    
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),


    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    

    # CRUD operations for contacts
    path('dashboard/contacts/', ContactListView.as_view(), name='contact_list'),
    path('dashboard/contacts/add/', ContactCreateView.as_view(), name='contact_add'),
    path('dashboard/contacts/<int:pk>/edit/', ContactUpdateView.as_view(), name='contact_edit'),
    path('dashboard/contacts/<int:pk>/delete/', ContactDeleteView.as_view(), name='contact_delete'),
    path('dashboard/contacts/<int:pk>/', ContactDetailView.as_view(), name='contact_detail'),

    # CRUD operations for categories
    path('dashboard/categories/', CategoryListView.as_view(), name='category_list'),
    path('dashboard/categories/add/', CategoryCreateView.as_view(), name='category_create'),
    path('dashboard/categories/<int:pk>/edit/', CategoryUpdateView.as_view(), name='category_update'),
    path('dashboard/categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
    path('dashboard/categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),  # Add Category Detail

    # CRUD operations for works
    path('dashboard/works/', WorkListView.as_view(), name='work_list'),
    path('dashboard/works/add/', WorkCreateView.as_view(), name='work_create'),
    path('dashboard/works/<int:pk>/edit/', WorkUpdateView.as_view(), name='work_edit'),
    path('dashboard/works/<int:pk>/delete/', WorkDeleteView.as_view(), name='work_delete'),
    path('dashboard/works/<int:pk>/', WorkDetailView.as_view(), name='work_detail'),  # Add Work Detail
]

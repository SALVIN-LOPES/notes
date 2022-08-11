
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.getRoutes,name='routes'),
    path('notes/',views.getNotes,name='notes'),
    path('notes/<str:pk>/',views.getNote,name='note'),
    # path('notes/<str:pk>/update/',views.updateNote,name='update-note'),
    # path('notes/<str:pk>/delete/',views.deleteNote,name='delete-note'),

]

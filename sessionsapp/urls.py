from django.urls import path,include
from . import views

urlpatterns = [
    path('home/', views.home_page, name = "home"),
    path("savingSession", views.saving_session, name = "saveSessions"),
    path("viewingSession", views.view_sessionData, name = "viewSession"),
    path("deletingSession", views.delete_session_data, name = "deletingSession"),
]

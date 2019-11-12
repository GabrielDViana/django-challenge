from django.urls import path

from . import views
from .views import LaunchDetailView, LaunchesListView

urlpatterns = [
    path('upcoming/', views.upcoming, name='upcoming'),
    path('', LaunchesListView.as_view()),
    path('<pk>', LaunchDetailView.as_view()),
]
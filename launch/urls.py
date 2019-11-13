from django.urls import path

from . import views
from .views import LaunchDetailView, LaunchesListView

urlpatterns = [
    path('upcoming/', views.upcoming_launches, name='upcoming'),
    path('past/', views.past_launches, name='upcoming'),
    path('next/', views.next_launch, name='upcoming'),
    path('latest/', views.latest_launch, name='upcoming'),
    path('', LaunchesListView.as_view()),
    path('<pk>', LaunchDetailView.as_view()),
]
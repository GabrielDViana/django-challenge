from django.urls import path

from . import views
from .views import LaunchDetailView, LaunchesListView

urlpatterns = [
    path('upcoming/', views.upcoming_launches, name='upcoming'),
    path('past_launches/', views.past_launches, name='upcoming'),
    path('next_launch/', views.next_launch, name='upcoming'),
    path('latest_launch/', views.latest_launch, name='upcoming'),
    path('', LaunchesListView.as_view()),
    path('<pk>', LaunchDetailView.as_view()),
]
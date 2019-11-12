from django.urls import path

from .views import LaunchDetailView, LaunchesListView

urlpatterns = [
    path('', LaunchesListView.as_view()),
    path('<pk>', LaunchDetailView.as_view()),
]
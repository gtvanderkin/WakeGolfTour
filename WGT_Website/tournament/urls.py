from django.urls import path
from . import views

urlpatterns = [
    path('', views.TournamentListView.as_view(), name='tournament_list',),
    path('<int:pk>/', views.TournamentDetailView.as_view(), name='tournament_detail')
]

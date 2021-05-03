from django.urls import path
from . import views

urlpatterns = [
    path('', views.GolferListView.as_view(), name='golfer_list',),
    path('<int:pk>/', views.GolferDetailView.as_view(), name='golfer_detail'),
    path('<int:pk>/round_scores/', views.GolferRoundScoresView.as_view(), name='golfer_round_scores')
]

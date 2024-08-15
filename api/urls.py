from django.urls import path
from .views import ProfessorAPIView, ProfessorReadAPIView

urlpatterns = [
    path('professors/', ProfessorAPIView.as_view()),
    path('professors/<int:pk>/', ProfessorAPIView.as_view()),
    path('read/professors/<int:pk>/', ProfessorReadAPIView.as_view()),
    path('read/professors/', ProfessorReadAPIView.as_view()),
]
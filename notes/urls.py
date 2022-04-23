from django.urls import path
from notes import views


urlpatterns = [
    path('', views.ListCreateNoteAPIView.as_view()),
    path('<int:pk>/', views.RetrieveUpdateDestroyNoteAPIView.as_view())
]

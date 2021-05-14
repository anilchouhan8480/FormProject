from django.urls import path
from . import views


urlpatterns = [
  path('mform/', views.mform),
  path('delete/<int:id>/', views.delete_article, name="del_article"),
  path('update/<int:id/', views.update_article, name="up_article")
]
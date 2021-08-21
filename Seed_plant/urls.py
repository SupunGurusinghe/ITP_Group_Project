from django.urls import path
from . import views

urlpatterns = [
    path('SeedPlanSection/', views.seed_plan_section),
]
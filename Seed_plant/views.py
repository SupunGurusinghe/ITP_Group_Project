from django.shortcuts import render
from django.http import HttpResponse

# Create seed_plan_section.


def seed_plan_section(request):
    return render(request, 'seed_plan_section.html')

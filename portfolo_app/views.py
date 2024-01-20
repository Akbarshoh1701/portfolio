from django.shortcuts import render
from django.views import View


# from django.views.generic import TemplateView

# Create your views here.
class IndexPich(View):
    def get(self, request):
        return render(request, "index.html")

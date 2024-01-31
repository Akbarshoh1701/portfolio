from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect
from django.views import View

from .forms import ContactForm
from .models import About, Fact, Skills, Sumary, Education, ProfessionalExperience, Portfolio, TypeService, \
    Testimonials, Contact, Category, Home, PortfolioImage


# from django.views.generic import TemplateView
# Create your views here.
class IndexPage(View):
    def get(self, request, portfolio_image=None):
        form = ContactForm()
        about = About.objects.first()
        fact = Fact.objects.all()
        skills = Skills.objects.all()
        sumary = Sumary.objects.first()
        education = Education.objects.all()
        professionale_experience = ProfessionalExperience.objects.all()
        portfolio = Portfolio.objects.all()
        typeservice = TypeService.objects.all()
        testimonials = Testimonials.objects.all()
        cantact = Contact.objects.first()
        category = Category.objects.all()
        home = Home.objects.first()

        context = {
            'form': form,
            'about': about,
            'fact': fact,
            'skills': skills,
            'sumary': sumary,
            'educations': education,
            'prof_experience': professionale_experience,
            'portfolio': portfolio,
            'typeservice': typeservice,
            'testimonials': testimonials,
            'cantact': cantact,
            'category': category,
            'portfolio_image': portfolio_image,
            'home': home
        }

        return render(request, "index.html", context)

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homepage")
        else:
            return HttpResponseNotAllowed(['GET'])


def PortfolioDetail(request, pk):
    obj = Portfolio.objects.get(id=pk)
    context = {
        "obj": obj
    }
    return render(request, 'portfolio-details.html', context)


def post(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("homepage")
    else:
        return HttpResponseNotAllowed(['GET'])

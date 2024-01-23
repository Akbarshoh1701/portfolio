from django.contrib import admin
from .models import (About, Fact, Skills, Sumary, Education, ProfessionalExperience, Portfolio,
                     TypeService, Testimonials, Contact, Category)

# Register your models here.

admin.site.register([About, Fact, Skills, Sumary, Education, ProfessionalExperience, Portfolio,
                     TypeService,  Testimonials, Contact, Category])



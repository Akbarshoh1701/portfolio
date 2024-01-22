from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register([About, Fact, Skills, Programs, Resume, Sumary, Education, ProfessionalExperience, Portfolio,
                     Services, TypeService,  Testimonials, Comment, Contact, ])

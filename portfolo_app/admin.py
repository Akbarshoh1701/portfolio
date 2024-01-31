from django.contrib import admin
from .models import (Home, About, Fact, Skills, Sumary, Education, ProfessionalExperience, Portfolio,
                     TypeService, Testimonials, Contact, Category, PortfolioImage, Message)

# Register your models here.

admin.site.register([Home, About, Fact, Skills, Sumary, Education, ProfessionalExperience, Portfolio,
                     TypeService, Testimonials, Contact, PortfolioImage, Message])


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    list_display_links = ['slug', 'name']
    prepopulated_fields = {'slug': ("name",)}

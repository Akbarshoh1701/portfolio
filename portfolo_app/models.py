from django.db import models


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class About(BaseModel):
    about_info = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    name_custom = models.CharField(max_length=255)
    birthday = models.DateField()
    website = models.CharField(max_length=255)
    phone = models.IntegerField()
    city = models.TextField(max_length=255)
    age = models.SmallIntegerField()
    degree = models.TextField(max_length=255)
    phemailone = models.EmailField()
    freelance = models.TextField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name + "About"


class Fact(BaseModel):
    name = models.CharField(max_length=255)
    title = models.TextField()
    img = models.ImageField()
    number = models.IntegerField()

    def __str__(self):
        return self.name + 'Fact'


class Skills(BaseModel):
    name = models.TextField(max_length=255)
    percent = models.SmallIntegerField()

    def __str__(self):
        return self.name + 'Skills'


class Sumary(BaseModel):
    name = models.CharField(max_length=255)
    text = models.TextField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name + 'Sumary'


class Education(BaseModel):
    title = models.CharField(max_length=255)
    start_year = models.IntegerField()
    end_year = models.IntegerField(null=True, blank=True)
    where_he_studied = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.title + 'Educatin'


class ProfessionalExperience(BaseModel):
    title = models.CharField(max_length=255)
    start_year = models.IntegerField()
    end_year = models.IntegerField(null=True, blank=True)
    where_it_works = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.title + 'ProfessionalExperience'


class Category(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)


class Portfolio(BaseModel):
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="portfolios")
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='portfolio')
    text = models.CharField(max_length=255)
    data = models.DateTimeField()
    url = models.URLField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name + 'Portfolio'


class TypeService(BaseModel):
    title = models.CharField(max_length=255)
    text = models.TextField()
    img = models.ImageField()

    def __str__(self):
        return self.title + 'TypeService'


class Testimonials(BaseModel):
    name = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    img = models.ImageField()
    text = models.TextField()

    def __str__(self):
        return self.name


class Contact(BaseModel):
    location = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    call = models.IntegerField()

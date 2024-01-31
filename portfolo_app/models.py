from django.db import models


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Home(BaseModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='static/assets/img/portfolio')


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
        return self.name


class Fact(BaseModel):
    CATEGORY = (
        ('bi bi-emoji-smile', 'Happy Clients'),
        ('bi bi-journal-richtext', 'Projects'),
        ('bi bi-headset', 'Hours Of Support'),
        ('bi bi-people', 'Hard Workers'),
    )
    name = models.CharField(max_length=255)
    title = models.TextField()
    img = models.CharField(max_length=255, choices=CATEGORY)
    number = models.IntegerField()

    def __str__(self):
        return self.name + 'Fact'


class Skills(BaseModel):
    name = models.TextField(max_length=255, unique=True)
    percent = models.SmallIntegerField()

    def __str__(self):
        return self.name


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
    end_year = models.IntegerField(null=True, blank=True, default=1)
    where_he_studied = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.title


class ProfessionalExperience(BaseModel):
    title = models.CharField(max_length=255)
    start_year = models.IntegerField()
    end_year = models.IntegerField(null=True, blank=True, default=1)
    where_it_works = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.title + 'ProfessionalExperience'


class Category(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Portfolio(BaseModel):
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="portfolios")
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/assets/img/portfolio')
    text = models.CharField(max_length=255)
    data = models.DateTimeField()
    url = models.URLField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name + 'Portfolio'


class PortfolioImage(BaseModel):
    portfolio_id = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='images')
    img = models.ImageField(upload_to='static/assets/img/portfolio')


class TypeService(BaseModel):
    SERVICE = (
        ('bi bi-briefcase', 'Lorem Ipsum'),
        ('bi bi-card-checklist', 'pitichka'),
        ('bi bi-bar-chart', 'antina'),
        ('bi bi-binoculars', 'durben'),
        ('bi bi-brightness-high', 'quyosh'),
        ('bi bi-calendar4-week', 'kalindar'),

    )
    # IKONKA = (
    #     ('bx bxs-quote-alt-left quote-icon-left', 'bog'),
    #
    # )
    title = models.CharField(max_length=255)
    text = models.TextField()
    img = models.CharField(max_length=255, choices=SERVICE)

    def __str__(self):
        return self.title


class Testimonials(BaseModel):
    name = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    img = models.ImageField(upload_to='static/assets/img/portfolio')
    text = models.TextField()

    def __str__(self):
        return self.name


class Contact(BaseModel):
    location = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    call = models.CharField(max_length=255)
    address = models.CharField(max_length=255)


# class Product(models.Model):
#     name = models.CharField(max_length=255)
#
# class ProductComment(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     comment = models.CharField(max_length=255)
class Message(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    text = models.TextField(max_length=255)

    def __str__(self):
        return self.name

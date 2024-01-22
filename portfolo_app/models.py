from django.db import models


# Create your models here.

class About(models.Model):
    about_info = models.CharField(max_length=255)
    name_feld = models.CharField(max_length=255)
    name_filt_custom = models.CharField(max_length=255)
    birthday = models.DateField()
    webbsite = models.CharField(max_length=255)
    phone = models.IntegerField()
    city = models.TextField(max_length=255)
    age = models.IntegerField()
    degree = models.TextField(max_length=255)
    phemailone = models.EmailField()
    freelance = models.TextField(max_length=255)
    description = models.CharField(max_length=255)

class Fact(models.Model):
    name = models.CharField(max_length=255)
    title = models.TextField()
    img = models.ImageField()
    number = models.IntegerField()
    tex_img = models.CharField(max_length=255)

class Skills(models.Model):
    name = models.TextField(max_length=255)
    text = models.TextField()

class Programs(models.Model):
    taytil = models.CharField(max_length=255)
    interest = models.IntegerField()
    skills = models.ForeignKey(Skills, on_delete=models.CASCADE)


class Resume(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

class Sumary(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)


class Education(models.Model):
    taytel = models.CharField(max_length=255)
    start_year = models.IntegerField()
    end_year = models.IntegerField(null=True, blank=True)
    where_he_studied = models.CharField(max_length=255)
    text = models.TextField()
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)

    def is_currently_enrolled(self):
        return self.end_year is None

    def save(self, *args, **kwargs):
        if self.is_currently_enrolled():
            self.end_year = timezone.now().year
        super().save(*args, **kwargs)

class ProfessionalExperience(models.Model):
    taytel = models.CharField(max_length=255)
    start_year = models.IntegerField()
    end_year = models.IntegerField(null=True, blank=True)
    where_it_works = models.CharField(max_length=255)
    text = models.TextField()
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)

    def is_currently_enrolled(self):
        return self.end_year is None

    def save(self, *args, **kwargs):
        if self.is_currently_enrolled():
            self.end_year = timezone.now().year
        super().save(*args, **kwargs)

class Portfolio(models.Model):
    titel = models.CharField(max_length=255)



class Services(models.Model):
    titel = models.CharField(max_length=255)

class TypeService(models.Model):
    titel = models.CharField(max_length=255)
    text = models.TextField()
    img = models.ImageField()
    services = models.ForeignKey(Services, on_delete=models.CASCADE)

class Testimonials(models.Model):
    text = models.TextField()


class Comment(models.Model):
    name = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    img = models.ImageField()
    text = models.TextField()


class Contact(models.Model):
    titel = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    call = models.IntegerField()
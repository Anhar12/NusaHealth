from django.db import models

# Create your models here.
class Logo(models.Model):
    primary_logo = models.ImageField(upload_to='logos/', blank=True, null=True, help_text="Upload primary logo")
    secondary_logo = models.ImageField(upload_to='logos/', blank=True, null=True, help_text="Upload secondary logo")

    def __str__(self):
        return "Logo Settings"
    
class ImageSlider(models.Model):
    image1 = models.ImageField(upload_to='image_slider/', blank=True, null=True, help_text="Upload slider image 1")
    image2 = models.ImageField(upload_to='image_slider/', blank=True, null=True, help_text="Upload slider image 2")
    image3 = models.ImageField(upload_to='image_slider/', blank=True, null=True, help_text="Upload slider image 3")
    image4 = models.ImageField(upload_to='image_slider/', blank=True, null=True, help_text="Upload slider image 4")
    image5 = models.ImageField(upload_to='image_slider/', blank=True, null=True, help_text="Upload slider image 5")

    def __str__(self):
        return f"Slider Image {self.id}"
    
class HeroSection(models.Model):
    hero_text = models.TextField(help_text="Hero section text", blank=True, null=True)
    hero_image = models.ImageField(upload_to='hero_section/', blank=True, null=True, help_text="Hero section image")

    def __str__(self):
        return "Hero Section Settings"
    
class ServiceSection(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True, help_text="Service title")
    description = models.TextField(help_text="Service description", blank=True, null=True)
    image = models.ImageField(upload_to='services/', blank=True, null=True, help_text="Service image")

    def __str__(self):
        return self.title
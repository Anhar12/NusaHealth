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
    service_title1 = models.CharField(max_length=100, blank=True, null=True, help_text="Service title")
    service_description1 = models.TextField(help_text="Service description", blank=True, null=True)
    service_image1 = models.ImageField(upload_to='services/', blank=True, null=True, help_text="Service image")
    
    service_title2 = models.CharField(max_length=100, blank=True, null=True, help_text="Service title")
    service_description2 = models.TextField(help_text="Service description", blank=True, null=True)
    service_image2 = models.ImageField(upload_to='services/', blank=True, null=True, help_text="Service image")
    
    service_title3 = models.CharField(max_length=100, blank=True, null=True, help_text="Service title")
    service_description3 = models.TextField(help_text="Service description", blank=True, null=True)
    service_image3 = models.ImageField(upload_to='services/', blank=True, null=True, help_text="Service image")

    def __str__(self):
        return f"{self.title1}, {self.title2}, {self.title3}"
      
# ================= Blog Model =======================
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                self).get_queryset()\
                    .filter(status='published')

class Post(models.Model):
    STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                               related_name='blog_posts', on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                                choices=STATUS_CHOICES,
                                default='draft')
    tags = TaggableManager()
    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.
    class Meta:
         ordering = ('-publish',)
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:post_detail',
                        args=[self.publish.year,
                            self.publish.strftime('%m'),
                            self.publish.strftime('%d'),
                            self.slug])
                            
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
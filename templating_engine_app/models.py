from django.db import models

# Create your models here.
# Filename: models.py
from django.db import models

# Create your models here.
class Pet(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, editable=False)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='pet_images', blank=True, null=True)

    def __str__(self):
        return self.name
    
    def get_image_url(self):
        if self.image:
            return self.image.url
        return ''

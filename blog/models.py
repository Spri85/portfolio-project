from django.db import models


# Create a Blog model
# - title
# - public_date
# - body
# - image
class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

# Add Blog app to the settings - ok

# Create a migration - python manage.py makemigrations - ok

# Migrate - python manage.py migrate - ok

# Add to the admin

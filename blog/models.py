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

    def summary(self):
        if len(self.body) > 100:
            return (self.body[:100]+'...')
        self.body

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def __str__(self):
        return self.title

# Add Blog app to the settings - ok

# Create a migration - python manage.py makemigrations - ok

# Migrate - python manage.py migrate - ok

# Add to the admin

from django.db import models

# Create your models here.
# Models are Basically database tables. to create a database table we have to create a model and
# Model is created using the class key word and inheret from the parent class models.model
class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.top_name

class WebPage(models.Model):
    # topic = models.ForeignKey(Topic) in older versions of Django it does on_delete=CASCADE by default
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(WebPage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)

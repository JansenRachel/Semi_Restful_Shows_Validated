from django.db import models
from django.db.models.fields import DateField, DateTimeField

# class Network(models.Model):
#     name = models.CharField(max_length=255)
#     created_at = DateField(auto_now_add=True)
#     updated_at = DateField(auto_now=True)
#     def __repr__(self):
#         return f"<Network object: {self.name} ({self.id})>"
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        if len(postData['title']) < 2:
            errors["title"] = "Title name should be at least 2 characters"

        if len(postData['network']) < 3:
            errors["network"] = "Network name should be at least 3 characters"
        
        if len(postData['desc']) < 10:
            errors["desc"] = "Description should be at least 10 characters"
        
        return errors


class Show(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    desc = models.TextField()
    # network = models.ForeignKey(Network, related_name="shows", on_delete=models.CASCADE)
    network = models.CharField(max_length=255)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    objects = ShowManager()
    def __repr__(self):
        return f"<Show object: {self.title} ({self.id})>"

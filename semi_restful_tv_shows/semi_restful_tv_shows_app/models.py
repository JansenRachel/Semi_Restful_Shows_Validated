from django.db import models
from django.db.models.fields import DateField, DateTimeField

# class Network(models.Model):
#     name = models.CharField(max_length=255)
#     created_at = DateField(auto_now_add=True)
#     updated_at = DateField(auto_now=True)
#     def __repr__(self):
#         return f"<Network object: {self.name} ({self.id})>"

class Show(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    desc = models.TextField()
    # network = models.ForeignKey(Network, related_name="shows", on_delete=models.CASCADE)
    network = models.CharField(max_length=255)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    def __repr__(self):
        return f"<Show object: {self.title} ({self.id})>"
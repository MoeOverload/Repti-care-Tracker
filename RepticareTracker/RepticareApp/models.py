from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    
    # future-proof fields (optional for now)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
class Reptile(models.Model):
    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="reptiles"
        
    )
    reptile_name = models.CharField("reptile name", max_length=30)
    reptile_species = models.CharField("reptile_species", max_length=60)
    def __str__(self):
        return self.reptile_name

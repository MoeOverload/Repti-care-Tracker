from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.


#user profile model
class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    
    # future-proof fields (optional for now)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


#reptile model   
class Reptile(models.Model):
    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="reptiles"  
    )
    
    reptile_name = models.CharField("reptile name", max_length=30)
    reptile_species = models.CharField("reptile_species", max_length=60)
    estimated_age_months = models.IntegerField("reptile_estimated_age",null=True, blank=True)
    estimated_age_record_date = models.DateField("reptile_age_record_date",null=True, blank=True)

    @property
    def current_age_months(self):
        if self.estimated_age_months is None or self.estimated_age_record_date is None:
            return None

        today = date.today()
        months_passed = (today.year - self.estimated_age_record_date.year) * 12 + (
            today.month - self.estimated_age_record_date.month
        )

        return self.estimated_age_months + months_passed
    @property
    def age_display(self):
        months = self.current_age_months
        if months is None:
            return "Unknown"

        years = months // 12
        rem_months = months % 12

        if years:
            return f"{years}y {rem_months}m"
        return f"{rem_months}m"
    
    def __str__(self):
        return self.reptile_name


#terraium model
class Terrarium(models.Model):
    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="terrariums"
    )
    reptile = models.OneToOneField(
        Reptile,
        on_delete=models.CASCADE,
        related_name="terrarium"
    )
    terrarium_nickname = models.CharField("terrarium_nickname",max_length=30)


#food model
class FeederType(models.Model):
    name = models.CharField(max_length=60)
    species = models.CharField(max_length=60, blank=True)
    default_unit = models.CharField(
        max_length=10,
        choices = [
            ("count", "Count"),
            ("g","Grams"),
        ]
    )
    notes = models.TextField(blank=True)
    def __str__(self):
        return self.name

#reptile weight log modal
class WeightLog(models.Model):
    reptile = models.ForeignKey(
        Reptile,
        on_delete=models.CASCADE,
        related_name="weights"
    )
    weight = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )
    notes = models.TextField(blank = True)
    recorded_on = models.DateField(auto_now_add=True)


#reptile feed log
class FeedLog(models.Model):
    reptile = models.ForeignKey(
        Reptile,
        on_delete =models.CASCADE,
        related_name="feedings"
    )
    feeder = models.ForeignKey(
        FeederType,
        on_delete=models.PROTECT        
    )
    quantity = models.DecimalField(
        max_digits= 6,
        decimal_places=2
    )
    fed_on = models.DateField()
    notes = models.TextField(blank=True)


#terrarium enviroment log
class TerrariumLog(models.Model):
    terrarium = models.ForeignKey(
        Terrarium,
        on_delete=models.PROTECT,
        related_name="enviroment_logs"
    )
    highest_temp = models.IntegerField(null=True,blank=True)
    lowest_temp = models.IntegerField(null=True,blank=True)
    highest_humidity = models.IntegerField(null=True,blank=True)
    lowest_humidity = models.IntegerField(null=True,blank=True)
    date_recorded = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True)
from django.contrib import admin
from .models import Profile, Reptile, Terrarium, TerrariumLog,FeederType,FeedLog,WeightLog
# Register your models here.
admin.site.register(Profile)
admin.site.register(Reptile)
admin.site.register(Terrarium)
admin.site.register(TerrariumLog)
admin.site.register(FeederType)
admin.site.register(FeedLog)
admin.site.register(WeightLog)
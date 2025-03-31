from django.contrib import admin


# AKTUÁLNÍ DEN

from .models import aktualniden
class aktualnidenAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.save()
        
admin.site.register(aktualniden)

# JÍDLO + PITÍ

from .models import food_drink
class food_drinkAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.save()
        
admin.site.register(food_drink)
from django.contrib import admin

from .models import Hracipepa
from .models import pepaspanek
from .models import pepa_zakladni_staty

class HracipepaAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.save()  # Spustí přepsanou metodu save()
        
class pepspanekAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.save()  # Spustí přepsanou metodu save()

class pepa_zakladni_statyAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.save()  # Spustí přepsanou metodu save()

admin.site.register(Hracipepa, HracipepaAdmin)
admin.site.register(pepaspanek, pepspanekAdmin)
admin.site.register(pepa_zakladni_staty, pepa_zakladni_statyAdmin)

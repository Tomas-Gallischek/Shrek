from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from pepaapp.models import Hracipepa
from .models import aktualniden

def aktualizovat_den(request):
    if request.method == 'POST':
        aktualni_den = request.POST.get('aktualni_den')
        if aktualni_den:
            try:
                aktualni_den = int(aktualni_den)
                den_obj = aktualniden.objects.get(id=1)
                den_obj.cislo_dne = aktualni_den
                den_obj.save()
            except aktualniden.DoesNotExist:
                novy_den = aktualniden(cislo_dne=aktualni_den)
                novy_den.save()
            except ValueError:
                # Zpracuj případ, kdy 'aktualni_den' nelze převést na integer
                # Můžeš například přidat chybovou hlášku do kontextu šablony
                pass  # Prozatím necháme prázdné, ale doporučuji zde něco udělat

        return redirect('adminpage')
    else:  # request.method == 'GET'
        return render(request, 'adminapp/aktualni_den.html')

def adminpage(request):
    return render(request, 'adminapp/main_admin_page.html')
    

def statistiky(request):
    return render(request, 'adminapp/statistiky_avataru.html')
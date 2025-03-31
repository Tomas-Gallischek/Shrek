# IMPORT - FUNKCE:
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from adminapp.views import aktualizovat_den
from django.db.models import Sum
from django.db.models import Avg, Sum

# IMPORT - MODELY:
from .models import pepa_zakladni_staty
from pepaapp.models import Hracipepa
from adminapp.models import aktualniden
from adminapp.models import food_drink

# ZÁKLADNÍ STATY
zakladni_staty = pepa_zakladni_staty.objects.get(id=1)

# AKTUÁLNÍ DEN
aktualni_den_objekt = aktualniden.objects.get(id=1)
aktualni_den = aktualni_den_objekt.cislo_dne

# BMI
pepa_BMI = (((zakladni_staty.vaha)/((zakladni_staty.vyska)/100)**2))
pepa_BMI = round(pepa_BMI, 2)

# DENNÍ PRŮMĚR KROKŮ - DNES
if aktualni_den >= 1 and aktualni_den <= 12:
    sloupec = f'kroky{aktualni_den}'
    dnesni_prumer_kroku = Hracipepa.objects.filter(tym="pepa").aggregate(Avg(sloupec))[f'{sloupec}__avg']
else:
    dnesni_prumer_kroku = None

# DENNÍ PRŮMĚR KROKŮ - VČERA

vcera = ((aktualni_den_objekt.cislo_dne)-(1))
if vcera >= 1 and vcera <= 12:
    sloupec = f'kroky{vcera}'
    vcerejsi_prumer_kroku = Hracipepa.objects.filter(tym="pepa").aggregate(Avg(sloupec))[f'{sloupec}__avg']
else:
    vcerejsi_prumer_kroku = None


# SOUČET KROKŮ ZA JEDNOTLIVÉ DNY CELÝ TÝM
agregovane_hodnoty = Hracipepa.objects.filter(tym="pepa").aggregate(
    sum_kroky1=Sum('kroky1'),
    sum_kroky2=Sum('kroky2'),
    sum_kroky3=Sum('kroky3'),
    sum_kroky4=Sum('kroky4'),
    sum_kroky5=Sum('kroky5'),
    sum_kroky6=Sum('kroky6'),
    sum_kroky7=Sum('kroky7'),
    sum_kroky8=Sum('kroky8'),
    sum_kroky9=Sum('kroky9'),
    sum_kroky10=Sum('kroky10'),
    sum_kroky11=Sum('kroky11'),
    sum_kroky12=Sum('kroky12'),
)
suma_kroky = sum(agregovane_hodnoty.values())

# CELKOVÝ POČET KROKŮ - JEDNOTLIVÍ HRÁČI
hraci = Hracipepa.objects.filter(tym="pepa")
for hrac in hraci:
    hrac.celkem_kroku = (
        hrac.kroky1 + hrac.kroky2 + hrac.kroky3 + hrac.kroky4 +
        hrac.kroky5 + hrac.kroky6 + hrac.kroky7 + hrac.kroky8 +
        hrac.kroky9 + hrac.kroky10 + hrac.kroky11 + hrac.kroky12
    )

# KOLIK KM ZA DEN PEPA UŠEL

pepa_km_vcera = round((((vcerejsi_prumer_kroku)*(zakladni_staty.delkakroku)/100)/1000), 2)

# JÍDLO A PITÍ

jidlo = food_drink.objects.first()

def pepa_main_page(request):
    context = {}
    context['celkem_kroku'] = suma_kroky
    context['aktualni_den'] = aktualni_den
    context['pepa_vaha'] = zakladni_staty.vaha
    context['pepa_vyska'] = zakladni_staty.vyska
    context['pepa_vek'] = zakladni_staty.vek
    context['pepa_pohlavi'] = zakladni_staty.pohlavi
    context['BMI'] = pepa_BMI
    context['delka_kroku'] = zakladni_staty.delkakroku
    context['denni_prumer_kroku'] = round(dnesni_prumer_kroku)
    context['vcerejsi_prumer_kroku'] = round(vcerejsi_prumer_kroku)
    context['vcera'] = vcera
    context['pepa_km_vcera'] = pepa_km_vcera
    context['jidlo'] = jidlo

    return render(request, 'pepaapp/pepa_main_page.html', context)


def full_tym(request):
    hraci = Hracipepa.objects.filter(tym="pepa")
    return render(request, 'pepaapp/pepa_full_tym.html', {
        'pepa_vsichni_hraci': hraci
    })


def leaderboard(request):
    return render(request, 'pepaapp/pepa_leaderboard', {
        'vsichni_hraci': hraci,
    })

def detail_hrace(request, id):
    hracid = Hracipepa.objects.get(id=id)
    hraci = Hracipepa.objects.all()
    hracid.celkem_kroku = hracid.kroky1 + hracid.kroky2 + hracid.kroky3 + hracid.kroky4 + hracid.kroky5 + hracid.kroky6 + hracid.kroky7 + hracid.kroky8 + hracid.kroky9 + hracid.kroky10 + hracid.kroky11 + hracid.kroky12

    return render(request, 'pepaapp/pepa_detail_hrace.html', {
        'pepa_vsichni_hraci': hraci,
        'jmeno': hracid.jmeno,
        'prijmeni': hracid.prijmeni,
        'kroky1' : hracid.kroky1,
        'kroky2' : hracid.kroky2,
        'kroky3' : hracid.kroky3,
        'kroky4' : hracid.kroky4,
        'kroky5' : hracid.kroky5,
        'kroky6' : hracid.kroky6,
        'kroky7' : hracid.kroky7,
        'kroky8' : hracid.kroky8,
        'kroky9' : hracid.kroky9,
        'kroky10' : hracid.kroky10,
        'kroky11' : hracid.kroky11,
        'kroky12' : hracid.kroky12,
        'kroky_celkem': hracid.celkem_kroku,
    })

def detail_statistika(request):
    return render(request, 'pepaapp/pepa_detail_statistika.html')

def jednotlive_dny(request):
    return render(request, 'pepaapp/pepa_jednotlive_dny.html')


#PROMĚNNÉ K VYTVOŘENÍ:


# BONUSOVÁ VÁHA = Váha jídla + výbavy

# KAPACITA - Podle batohu

# VOLNÁ KAPACITA = Kapacita batohu - kapacita vybavení - kapacita jídla 

# km/den = průměrný počet kroků * délka kroku (v metrech)

# KAŽDÝ KUS VYBAVENÍ MÁ STANOVENÉ: Váhu, V, typ bonusu, hodnotu bonusu a cenu

# kcal. PŘÍJEM JÍDLO - To co pepa snědl
# kcla. PŘÍJEM PITÍ - To co pepa vypil
# kcal. PŘÍJEM CELKEM - suma
#BMR - 10*VÁHA, + 6,25*VÝŠKA - 5*VĚK +5
#kcal. VÝDEJ AKTIVITA - Podle databáze 
#kcal. VÝDEJ CELKEM - Aktivita + bazál
#kcal. ROZDÍL - Příjem celkem - výdej celkem

#nabírání/hudnutí - Databáze na základě kacl.ROZDÍLU

# NOSNOST - Na základě "základní váhy"

# CELKOVÁ VÁHA - Základ + Hubnutí/přibírání + zátěž (Kalorický výdej počítat podle tohoto) <- zvážit to hudbnutí kvůli cyklickému odkazu 

# ÚNAVA - Na základě databáze (ovlivněna základní únavou, denní únavou z jídla, z pití)

# ODPOČINEK - Databáze na základě odpočinku
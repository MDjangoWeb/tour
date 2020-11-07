from django.shortcuts import render, redirect
from django.contrib import messages
from .models import SayohatJoylar,Murojat, FoyRoyxat
# Create your views here.

def Asosiy(request):
    active = 'active'
    joylar = SayohatJoylar.objects.all().order_by('-id')[:6]
    return render(request, 'index.html',{'joylar': joylar, 'asosiy_active':active})

def Malumot(request):
    active = 'active'
    return render(request, 'about.html', {'malumot_active':active})


def Aloqa(request):
    active = 'active'
    if request.method == 'POST':
        ism = request.POST['ism']
        tel = request.POST['tel']
        mavzu = request.POST['mavzu']
        xabar = request.POST['xabar']

        yangi_murojat = Murojat(ism=ism, tel=tel, mavzu=mavzu, xabar=xabar)
        yangi_murojat.save();
        messages.info(request, "Murojatingiz uchun raxmat, Tez orada siz bilan aloqaga chiqamiz")
        return redirect('/aloqa')
    return render(request, 'contact.html',{'aloqa_active':active})

def Joylar(request):
    joylar = SayohatJoylar.objects.all()
    return render(request, 'destinations.html', {'joylar':joylar})

def Yangiliklar(request):
    active = 'active'
    return render(request, 'news.html',{'yangilik_active':active})


def Qidiruv(request):
    if request.method == "POST":
        shahar = request.POST['shahar']
        narxi = request.POST['narxi']

        qidiruv_natija1 = SayohatJoylar.objects.filter(nomi__contains = shahar)
        qidiruv_natija = qidiruv_natija1.filter(narx__contains = narxi)
        
        if qidiruv_natija:
            print("borrrrrrrrrr!!!!!!!!!!")
            print(qidiruv_natija)
        else:
            print("none??????")
            qidiruv_natija = qidiruv_natija1
        # for natija in qidiruv_natija1:
        #     if (natija.narx >= int(narxi) - 10) or (natija.narx <= int(narxi) + 10):
        #         qidiruv_natija = natija
    return render(request, 'destinations.html', {'joylar': qidiruv_natija})


def RoyxatdanUtish(request):
    if request.method == 'POST':
        ismi = request.POST['ismi']
        email = request.POST['email']

        if FoyRoyxat.objects.get(email=email):
            messages.info(request, "Bu E-mail ro'yxatdan o'tgan")
            return redirect('/')
        else:
            yangi_azo = FoyRoyxat(ismi=ismi, email=email)
            yangi_azo.save();
            messages.info(request, "Endi Yangiliklarimizdan birinchilardan bo'lib xabar topasiz!!")
            return redirect('/')

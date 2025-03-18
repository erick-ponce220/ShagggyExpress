from django.shortcuts import render
from django.http import HttpResponse
from shopApp.models import Product, Contacts

# Create your views here.
def index(request):
    product_list = Product.objects.all()
    special_offers = Product.objects.filter(product_is_offer=True)
    my_context = {
        'user' : 'Erick',
        'message' : 'Fuera de mi cesped!', 
        'special_offers' : special_offers,
        'product_list' : product_list,
        'special_offers_2' : [
            {
                'name' : 'Mascarilla hidratante de sabila',
                'cost' : 125.00,
                'image': 'https://i1.perfumesclub.com/grande/110468.jpg',
            },
            {
                'name' : 'Emulador de videojuegos portatil N64',
                'cost' : 450.00,
                'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQl38YJdMpwQJUUEvcs6f_lPrfs1SA61hqD5Q&s',
            },
            {
                'name' : 'Reloj de pulsera gotico de snoopy',
                'cost' : 169.00,
                'image': 'https://m.media-amazon.com/images/I/81hiL2BX-rL.jpg',
            },
            {
                'name' : 'Camisa para caballero de algodon',
                'cost' : 200.00,
                'image': 'https://ae01.alicdn.com/kf/S2af67e4f54c64e0dbd1f0d66382a3c46E/AIOPESON-Nueva-oto%C3%B1o-Camisa-denim-de-hombre-de-algod%C3%B3n-de-color-s%C3%B3lido-Camisa-informal-de-manga-larga-con-un-bolsillo-.jpg',
            },
            {
                'name' : 'Carro de Toretto tamaño a escala de Lego',
                'cost' : 346.00,
                'image': 'https://m.media-amazon.com/images/I/81EBHsrXfnL.jpg',
            },

        ],
    }
    return render(request, 'shopApp/index.html', context=my_context)
    #return HttpResponse("Hola mundo desde Django")

def about(request):
    active_contacts = Contacts.objects.filter(contact_active=True)  #Filtra los contactos activos
    context = {
        'active_contacts': active_contacts  #Pasa los contactos activos al contexto
    }
    return render(request, 'shopApp/about.html', context=context)
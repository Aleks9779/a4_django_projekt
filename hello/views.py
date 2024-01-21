from django.http import HttpResponse
from .models import Product

def products_under_price(request, price):
    products = Product.objects.filter(price__lt=price)
    return HttpResponse(products)

from django.shortcuts import render
from django.http import JsonResponse

# Funktion für HTML-Ausgabe
def products_html(request, price):
    products = Product.objects.filter(price__lt=price)
    return render(request, 'products.html', {'products': products})

# Funktion für JSON-Ausgabe
def products_json(request, price):
    products = list(Product.objects.filter(price__lt=price).values())
    return JsonResponse({'products': products})

from django.core.mail import send_mail
from django.conf import settings

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = f"Neue Kontaktanfrage von {name}"
        recipient_list = ['info@deinedomain.com']
        send_mail(subject, message, email, recipient_list)
        # Füge eine Bestätigungsnachricht oder Logik hinzu
        return render(request, 'thank_you.html')
    return render(request, 'contact.html')

### Das ist extra - nicht notwendig
from django.core.mail import send_mail
from django.conf import settings

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        send_mail(
            f"Neue Kontaktanfrage von {name}",
            message,
            settings.EMAIL_HOST_USER,
            ['empfaenger@emailadresse.com'],
            fail_silently=False,
        )

        return render(request, 'thank_you.html')
    return render(request, 'contact.html')
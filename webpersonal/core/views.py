from django.shortcuts import render, HttpResponse

html_base = ('''
        <h1>Mi web personal</h1>
        <h2>Portada</h2>
        <ul>
            <li><a href="/">Inicio</a></li>
            <li><a href="/about/">Acerca de</a></li>
            <li><a href="/portfolio/">Portafolio</a></li>
            <li><a href="/contact/">Contacto</a></li>
        </ul>
    ''')

# Create your views here.

def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def portfolio(request):
    return render(request, "core/portafolio.html")

def contact(request):
    return render(request, "core/contact.html")
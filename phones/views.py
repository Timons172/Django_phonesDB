from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    all_phones = Phone.objects.all()
    phones = all_phones
    pages_sorted = request.GET.get('sort', '')

    if pages_sorted == 'max_price':
        phones = all_phones.order_by('-price')

    elif pages_sorted == 'min_price':
        phones = all_phones.order_by('price')

    elif pages_sorted == 'name':
        phones = all_phones.order_by('name')

    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)

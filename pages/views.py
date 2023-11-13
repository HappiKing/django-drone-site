from django.shortcuts import render

# Create your views here.
def mainpage(request):
    return render(request, 'pages/mainpage.html')

def company(request):
    return render(request, 'pages/company_info.html')

def product(request):
    return render(request, 'pages/product.html')

def product_option(request):
    return render(request, 'pages/product_option.html')

def support(request):
    return render(request, 'pages/support.html')
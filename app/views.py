from django.shortcuts import render, redirect
from .models import product  # Assuming your model is named 'Product'
from .forms import productForm  # Assuming your form is named 'ProductForm'

# Create your views here.
def index(request):
    return render(request, 'index.html')

def addp(request):
    if request.method == 'POST':
        form = productForm(request.POST)  # Use the form class here
        if form.is_valid():
            form.save()  # Save the form, which will create a Product instance
            return redirect('adds')  # Use 'adds' as the URL name
        else:
            return redirect('addf')  # Use 'addf' as the URL name
    else:
        form = productForm()  # Initialize an empty form on GET request
        return render(request, 'addp.html', {'form': form})

def adds(request):
    return render(request, 'adds.html')

def addf(request):
    return render(request, 'addf.html')

def plist(request):
    products = product.objects.all()  # Fetch all products from the database
    return render(request, 'plist.html', {'products': products})

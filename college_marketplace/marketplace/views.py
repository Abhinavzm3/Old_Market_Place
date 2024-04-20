# from django.contrib.auth import login, authenticate,logout
# from django.contrib.auth.forms import UserCreationForm
# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from .forms import ProductForm, SignUpForm, LoginForm

# from django.shortcuts import render, redirect,get_list_or_404,get_object_or_404
# from .models import Product
# from .forms import ProductForm


# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('front_page')
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})

# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('front_page')
#     else:
#         form = LoginForm()
#     return render(request, 'login.html', {'form': form})



# @login_required





# def remove_product(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     if request.user == product.user:  # Assuming 'user' is the ForeignKey field in the Product model representing the user who added the product
#         product.delete()
#     return redirect('front_page')


# def front_page(request):
#     products = Product.objects.all()
#     return render(request, 'front_page.html', {'products': products})
# def signout(request):
#     logout(request)
#     return redirect('front_page')

# # def add_product(request):
# #     if request.method == 'POST':
# #         form = ProductForm(request.POST)
# #         if form.is_valid():
# #             form.save()
# #             return redirect('front_page')
# #     else:
# #         form = ProductForm()
# #     return render(request, 'add_product.html', {'form': form})
# def add_product(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('front_page')
#     else:
#         form = ProductForm()
#     return render(request, 'add_product.html', {'form': form})



from django.contrib.auth.decorators import user_passes_test


from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm, SignUpForm, LoginForm
from .forms import ProductForm
from django.contrib.auth.decorators import login_required



from datetime import timedelta
from django.utils import timezone




# def front_page(request):
#     products = Product.objects.all()
#     return render(request, 'front_page.html', {'products': products,'user': request.user})


def front_page(request):
    one_week_ago = timezone.now() - timedelta(days=20)
    query = request.GET.get('q')
    category = request.GET.get('category')
    products = Product.objects.all()
    
    if query:
        products = products.filter(name__icontains=query)

    if category:
        products = products.filter(category=category)

    products = products.filter(created_at__gte=one_week_ago).order_by('-created_at')

    return render(request, 'front_page.html', {'products': products, 'user': request.user, 'category': category})









@login_required


def remove_product(request, product_id):
    product = get_object_or_404(Product, id=product_id, user=request.user)
    product.delete()
    return redirect('front_page')

def about(request):
    return render(request, 'about.html')




def signout(request):
    logout(request)
    return redirect('front_page')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('front_page')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('front_page')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})



@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('front_page')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})



@user_passes_test(lambda u: u.is_superuser)
def admin_remove_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('front_page')

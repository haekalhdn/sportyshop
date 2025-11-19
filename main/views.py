from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from main.models import Product

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_product = Product.objects.create(
            user=request.user,
            name=data["name"],
            price=int(data["price"]),
            description=data["description"],
            thumbnail=data["thumbnail"],
            category=data["category"],
            stock=int(data["stock"]),
            is_featured=data["is_featured"]
        )
        new_product.save()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)


@login_required(login_url='/login')
def show_main(request):
    context = {
        'npm' : '2406431536',
        'name': request.user.username,
        'class': 'PBP C',
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def show_xml_by_id(request, product_id):
    try:
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, product_id):
   try:
       product_item = Product.objects.get(pk=product_id)
       json_data = serializers.serialize("json", [product_item])
       return HttpResponse(json_data, content_type="application/json")
   except Product.DoesNotExist:
       return HttpResponse(status=404)

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    filter_type = request.GET.get("filter", "all")

    if filter_type == "my" and request.user.is_authenticated:
        product_list = Product.objects.filter(user=request.user)
    else:
        product_list = Product.objects.all()

    data = [
        {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'category_display': product.get_category_display(),
            'is_featured': product.is_featured,
            'is_product_hot': product.is_product_hot,
            'stock': product.stock,
            'product_views': product.product_views,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'user_id': product.user.id if product.user else None,
            'username': product.user.username if product.user else 'Anonymous',
        }
        for product in product_list
    ]

    return JsonResponse(data, safe=False)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.increment_views()

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

@csrf_exempt
@require_POST
@login_required(login_url='/login')
def create_product_ajax(request):
    try:
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        thumbnail = request.POST.get("thumbnail")
        category = request.POST.get("category")
        stock = request.POST.get("stock")
        is_featured = request.POST.get("is_featured") == 'on'

        if not all([name, price, description, thumbnail, category, stock]):
            return JsonResponse({
                'status': 'error',
                'message': 'All fields are required!'
            }, status=400)

        new_product = Product(
            name=name,
            price=int(price),
            description=description,
            thumbnail=thumbnail,
            category=category,
            stock=int(stock),
            is_featured=is_featured,
            user=request.user
        )
        new_product.save()

        return JsonResponse({
            'status': 'success',
            'message': 'Product created successfully!',
            'product_id': new_product.id
        }, status=201)

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)

@csrf_exempt
@require_POST
@login_required(login_url='/login')
def update_product_ajax(request, id):
    try:
        product = get_object_or_404(Product, pk=id)

        if product.user != request.user:
            return JsonResponse({
                'status': 'error',
                'message': 'You are not authorized to edit this product!'
            }, status=403)

        product.name = request.POST.get("name", product.name)
        product.price = int(request.POST.get("price", product.price))
        product.description = request.POST.get("description", product.description)
        product.thumbnail = request.POST.get("thumbnail", product.thumbnail)
        product.category = request.POST.get("category", product.category)
        product.stock = int(request.POST.get("stock", product.stock))
        product.is_featured = request.POST.get("is_featured") == 'on'

        product.save()

        return JsonResponse({
            'status': 'success',
            'message': 'Product updated successfully!'
        }, status=200)

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)

@csrf_exempt
@require_POST
@login_required(login_url='/login')
def delete_product_ajax(request, id):
    try:
        product = get_object_or_404(Product, pk=id)

        if product.user != request.user:
            return JsonResponse({
                'status': 'error',
                'message': 'You are not authorized to delete this product!'
            }, status=403)

        product.delete()

        return JsonResponse({
            'status': 'success',
            'message': 'Product deleted successfully!'
        }, status=200)

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)

@csrf_exempt
@require_POST
def login_ajax(request):
    try:
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            return JsonResponse({
                'status': 'error',
                'message': 'Username and password are required!'
            }, status=400)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            response = JsonResponse({
                'status': 'success',
                'message': 'Login successful!',
                'username': user.username
            }, status=200)
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            return JsonResponse({
                'status': 'error',
                'message': 'Invalid username or password!'
            }, status=401)

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)

@csrf_exempt
@require_POST
def register_ajax(request):
    try:
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if not all([username, password1, password2]):
            return JsonResponse({
                'status': 'error',
                'message': 'All fields are required!'
            }, status=400)

        if password1 != password2:
            return JsonResponse({
                'status': 'error',
                'message': 'Passwords do not match!'
            }, status=400)

        form = UserCreationForm({
            'username': username,
            'password1': password1,
            'password2': password2
        })

        if form.is_valid():
            form.save()
            return JsonResponse({
                'status': 'success',
                'message': 'Registration successful! Please login.'
            }, status=201)
        else:
            errors = []
            for _, error_list in form.errors.items():
                for error in error_list:
                    errors.append(error)

            return JsonResponse({
                'status': 'error',
                'message': ' '.join(errors)
            }, status=400)

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)

@login_required(login_url='/login')
def logout_ajax(request):
    try:
        logout(request)
        response = JsonResponse({
            'status': 'success',
            'message': 'Logout successful!'
        }, status=200)
        response.delete_cookie('last_login')
        return response
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)

from django.shortcuts import render , get_object_or_404,redirect
from .forms import LoginForm, UserRegistrationForm
from mainapp.models import Item
from django.contrib.auth import authenticate,login

def index(request):
    items = Item.objects.all()
    item1=items[:4]
    item2=items[4:]
    return render(request, 'mainapp/index.html',{
        'item1': item1,
        'item2':item2,
    })

def products(request):
    items = Item.objects.all()
    item1=items[:4]
    item2=items[4:]
    return render(request, 'mainapp/products.html', {
         'item1': item1,
         'item2':item2,
    })

def product_details(request, pk):
    item1=Item.objects.all()
    item2=item1[:4]
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'mainapp/details.html', {
        'items': item,
        'item2':item2,
    })

def account(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        form = LoginForm(request.POST)
        
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect('mainapp:account')
        # Note: You can use 'elif' instead of 'if' here
        elif form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])  # Fix password retrieval
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('mainapp:index')
                else:
                    return render(request, 'mainapp/account.html', {'form': form})
            else:
                return render(request, 'mainapp/account.html', {'form': form})
    else:
        user_form = UserRegistrationForm()
        form = LoginForm()
        
    return render(request, 'mainapp/account.html', {'user_form': user_form, 'form': form})  # Pass both forms to the template


# def cart(request):
#     items=Item.objects.all()
#     item1=items[0:3]
#     return render(request, 'mainapp/cart.html',{
#         'item1':item1
#     })


# def add_to_cart(request, product_id):
#     if request.user.is_authenticated:
#         user = request.user
#         product = Item.objects.get(pk=product_id)
#         cart_item, created = CartItem.objects.get_or_create(user=user, product=product)
#         if not created:
#             cart_item.quantity += 1
#             cart_item.save()
#         return render('mainapp:cart')
#     else:
#         # Handle non-authenticated users (e.g., redirect to login page)
#         pass

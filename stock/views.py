from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from stock.forms import ProductForm
from stock.models import Account, Product


def list_account(request):
    accounts = Account.objects.all()
    data = {
        'accounts': accounts
    }
    return render(request, 'stock/list_account.html', data)


def list_product(request):
    products = Product.objects.all()
    data = {
        'products': products
    }
    return render(request, 'stock/list_product.html', data)


def detail_account(request, pk):
    account = Account.objects.get(pk=pk)
    data = {
        'account': account
    }
    return render(request, 'stock/detail_account.html', data)


def detail_product(request, pk):
    product = Product.objects.get(pk=pk)
    data = {
        'product': product
    }
    return render(request, 'stock/detail_product.html', data)


# def create_account(request, account=None):
#     if request.method=='POST':
#         form = AccountForm(request.POST, instance=account)
#         if form.is_valid():
#             account = form.save()
#             return redirect(account)
#     else:
#         form = AccountForm(instance=account)
#
#     return render(request, 'stock/create_account.html', {
#         'form': form,
#     })

def create_account(request, account=None):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        phone = request.POST.get('phone', None)
        address = request.POST.get('address', None)  # request.POST의 딕셔너리에서 content가 키인 value를 가져오고 없으면 none리턴
        if name and phone and address:
            account = Account.objects.create(
                name=name,
                phone=phone,
                address=address
            )
            return redirect('stock:detail_account', account.pk)  # redirect: 인자로 받은 url로 이동
    return render(request, 'stock/create_account.html')


def edit_account(request, pk):
    account = Account.objects.get(pk=pk)
    if request.method == 'GET':
        return render(request, 'stock/edit_account.html', {'account': account})
    elif request.method == 'POST':
        name = request.POST.get('name', None)
        phone = request.POST.get('phone', None)
        address = request.POST.get('address', None)

        account.name = name
        account.phone = phone
        account.address = address

        account.save()
        return redirect('stock:detail_account', account.pk)


def delete_account(request, pk):
    account = Account.objects.get(pk=pk)
    account.delete()
    return redirect('stock:list_account')


def create_product(request, item=None):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save()  # ModelForm에서 제공
            return redirect('stock:detail_product', item.pk)  # 이부분 인강이랑 같게 했을 때 왜 안되는지 모르겠음.
    else:
        form = ProductForm(instance=item)

    return render(request, 'stock/create_product.html', {
        'form': form,
    })


def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return create_product(request, product)


def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return redirect('stock:list_product')


def left_add(request, pk):
    product = Product.objects.get(pk=pk)
    product.left += 1
    product.save()
    return redirect('stock:list_product')


def left_sub(request, pk):
    product = Product.objects.get(pk=pk)
    if product.left > 0:
        product.left -= 1
        product.save()
    return redirect('stock:list_product')

from django.shortcuts import render
from django.db.models import Q
import math
# Create your views here.
from .models import *

def getPriceRangeValue(priceRange):
    if priceRange == 1: return (0, 5)
    if priceRange == 2: return (5, 10)
    if priceRange == 3: return (10, 20)
    if priceRange == 4: return (20, None)
    return (None, None)

def index(request):
    PAGE_SIZE = 5
    page = int(request.GET.get('page') or 1)
    categoryId = request.GET.get('categoryId', '')
    categoryId = int(categoryId) if categoryId else ''

    priceRange = request.GET.get('priceRange', '')
    priceRange = int(priceRange) if priceRange else ''
    minPrice, maxPrice = getPriceRangeValue(priceRange)

    keyword = request.GET.get('keyword', '')
    productList = Product.objects.filter(
                    Q(name__icontains=keyword)|Q(code__icontains=keyword))
    
    if minPrice: 
        productList = productList.filter(price__gte=minPrice) 

    if maxPrice:
        productList = productList.filter(price__lte=maxPrice)

    if categoryId:
        productList = productList.filter(category__id=categoryId)

    productList = productList.order_by('-price', 'name')

    start = (page-1) * PAGE_SIZE
    end = start + PAGE_SIZE
    total = len(productList)                 # Tổng số bản ghi
    num_page = math.ceil(total / PAGE_SIZE)  # Tổng số trang
    prev_page = max(page - 1, 1)             # Trang trước
    next_page = min(page + 1, num_page)      # Trang sau
    productList = productList[start:end]

    categoryList = Category.objects.all()
    context = {
        'priceRange': priceRange,
        'categoryId': categoryId,
        'keyword': keyword,
        'categoryList': categoryList,
        'start': start, 'total': total, 'num_page': num_page,
        'page': page, 'prev_page': prev_page, 'next_page': next_page,
        'productList':  productList
    }
    return render(request, 'index.html' , context)
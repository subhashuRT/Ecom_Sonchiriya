from django.shortcuts import get_object_or_404, render
from .models import Product
from all_category.models import Category
from django.core.paginator import Paginator
# Create your views here.

def shop(request,category_slug= None):
    categories = None
    products = None
    if category_slug !=None:
        categories = get_object_or_404(Category,slug = category_slug )
        products = Product.objects.filter(category = categories,is_available = True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()
    context = {"products":products,"product_count":product_count}
    return render(request, "shop/shop.html",context)

    
def index(request):
    product_objects = Product.objects.all()

    #Search code
    item_name = request.GET.get("item_name")
    if item_name != "" and item_name != None:
        product_objects = product_objects.filter(items__icontains=item_name)


    # #paginator code change 4 to the number you want
    # paginator = Paginator(product_objects,3)
    # page = request.GET.get("page")
    # product_objects = paginator.get_page(page) 

    return render(request, 'index.html',{"product_objects": product_objects})


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug = category_slug, slug = product_slug)
    except Exception as e:
        raise e
    context = {'single_product' : single_product,}
    return render(request, 'shop/product_detail.html',context)

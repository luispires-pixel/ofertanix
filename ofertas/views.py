from django.shortcuts import render, get_object_or_404, redirect

from .models import Product, Category, Click


def home(request):
    products = Product.objects.filter(active=True).select_related("category")
    categories = Category.objects.filter(product__active=True).distinct()

    return render(
        request,
        "ofertas/home.html",
        {
            "products": products,
            "categories": categories,
        },
    )


def go(request, pk):
    product = get_object_or_404(Product, pk=pk, active=True)

    Click.objects.create(
        product=product,
        referrer=request.META.get("HTTP_REFERER", "")[:500],
    )

    return redirect(product.affiliate_url)
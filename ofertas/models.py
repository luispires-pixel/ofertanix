from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField("nome", max_length=80, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    icon = models.CharField("emoji", max_length=12, default="🛍️")
    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        ordering = ["name"]
    def save(self, *args, **kwargs):
        if not self.slug: self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    def __str__(self): return self.name

class Product(models.Model):
    PLATFORMS = [("Mercado Livre","Mercado Livre"),("Shopee","Shopee"),("Amazon","Amazon"),("Outra","Outra")]
    name = models.CharField("nome", max_length=180)
    description = models.TextField("descrição", blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="categoria")
    platform = models.CharField("plataforma", max_length=30, choices=PLATFORMS)
    affiliate_url = models.URLField("link de afiliado", max_length=1000)
    image_url = models.URLField("URL da imagem", blank=True, max_length=1000)
    image = models.ImageField("imagem enviada", upload_to="products/", blank=True)
    current_price = models.DecimalField("preço atual", max_digits=10, decimal_places=2)
    old_price = models.DecimalField("preço antigo", max_digits=10, decimal_places=2, null=True, blank=True)
    featured = models.BooleanField("destaque", default=False)
    active = models.BooleanField("publicado", default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-featured", "-created_at"]
        verbose_name = "produto"
        verbose_name_plural = "produtos"
    def __str__(self): return self.name
    @property
    def discount(self):
        if self.old_price and self.old_price > self.current_price:
            return round((1 - self.current_price / self.old_price) * 100)
        return 0

class Click(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="clicks")
    created_at = models.DateTimeField(auto_now_add=True)
    # Não armazenamos IP; evitamos coletar dado pessoal desnecessário.
    referrer = models.CharField(max_length=500, blank=True)
    class Meta:
        verbose_name = "clique registrado"
        verbose_name_plural = "cliques registrados"
        ordering = ["-created_at"]
    def __str__(self): return f"{self.product} - {self.created_at:%d/%m/%Y %H:%M}"

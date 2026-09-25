from django.contrib import admin
from .models import Category, Product, Click
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","slug","icon")
    prepopulated_fields = {"slug": ("name",)}
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","category","platform","current_price","featured","active")
    list_filter = ("active","featured","platform","category")
    search_fields = ("name","description")
    list_editable = ("current_price","featured","active")
@admin.register(Click)
class ClickAdmin(admin.ModelAdmin):
    list_display = ("product","created_at","referrer")
    list_filter = ("created_at","product")
    readonly_fields = ("product","created_at","referrer")
    def has_add_permission(self, request): return False
    def has_change_permission(self, request, obj=None): return False

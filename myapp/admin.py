from django.contrib import admin
from .models import Car, Rental
class RentalInline(admin.TabularInline):  
    model = Rental  
    extra = 1  

@admin.register(Car)  
class CarAdmin(admin.ModelAdmin):  
    list_display = ("brand", "model", "year", "price_per_day", "available")  
    list_filter = ("available", "brand", "year")  
    search_fields = ("brand", "model")  
    inlines = [RentalInline]
    
@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ("user", "car", "start_date", "end_date", "total_price")
    list_filter = ("start_date", "end_date", "car")
    search_fields = ("user__username", "car__brand", "car__model")


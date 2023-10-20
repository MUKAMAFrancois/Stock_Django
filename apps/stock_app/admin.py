from django.contrib import admin
from apps.stock_app.models import Product_Model,Purchase_History,Sales_History

# Register your models here.

admin.site.site_header='Stock MS Mukama.'
@admin.register(Product_Model)
class Product_ModelAdmin(admin.ModelAdmin):
    list_display=['id','product_name','items_instock','category','unit_price']
    list_filter=['category','product_name']
    search_fields=['product_name','category']

    ordering=('-items_instock',)

@admin.register(Purchase_History)
class Purchase_HistoryAdmin(admin.ModelAdmin):
    list_display=['id','product','quantity_added','purchase_date']
    list_filter=['product','product__category']
    ordering=('-purchase_date',)
admin.site.register(Sales_History)






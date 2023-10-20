
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('home/',views.home,name='index_home'),
    path('full_details/<int:id>/',views.details,name='full_details'),
    path('add_record/',views.Add_Record.as_view(),name='add_record'),
    path('update_record/<int:pk>/', views.Edit_Record.as_view(),name='edit_record'),
    path('delete_record/<int:pk>/',views.Delete_Record.as_view(),name='delete_record'),

    #export to csv

    path('export_to_csv/',views.export_csv, name='export_csv'),
    #export to pdf

    path('export_to_pdf/', views.pdf_export, name='export_pdf'),
    
    # Add $ Receive
    path('get_item/<int:id>/',views.get_item, name='get_item'),
   # path('add_quantity/<int:id>/',views.add_quantity,name='add_quantity'),

    # Historic
     path('purchase_history/', views.purchase_history, name='purchase_history'),
      path('sales_history/', views.sales_history, name='sales_history'),
     path('add_purchase_history/<int:id>/', views.add_purchase_history, name='add_purchase_history'),
    # path('make_sales/<int:id>/',views.add_sales_history, name='sales_made')

    #Statistics

    path('statistics/purchases/',views.stat_purchases, name='stat_purchases')

  
]

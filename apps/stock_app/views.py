from django.shortcuts import render, redirect, get_object_or_404
from apps.stock_app.models import Product_Model,Purchase_History
from apps.stock_app.forms import *
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#pdf
from django.http import FileResponse
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
import io


import csv
from django.http import HttpResponse
from datetime import date
from django.db.models import Sum

from collections import defaultdict
from django.http import JsonResponse

# Create your views here.




 

def home(request):
    records=Product_Model.objects.all()
    paginator = Paginator(records, 5)  # Show 5 records per page
    page = request.GET.get('page')
    try:
        records=paginator.page(page)
    except PageNotAnInteger:
        records=paginator.page(1)
    except EmptyPage:
        records = paginator.page(paginator.num_pages)

    form=Search_Form(request.POST or None)
    if request.method=='POST':
        records=Product_Model.objects.filter(category__icontains=form['category'].value(),product_name__icontains=form['product_name'].value())

    dicti={
        "records":records,
        "form":form,
        
    }

    return render(request,'stock_app/home.html',dicti)
 



""" def home(request):
    records = Product_Model.objects.all()
    form = Search_Form(request.POST or None)
    
    # Fetch profit for each product
    profits = [record.profitability.calculate_profit() for record in records]

    if request.method == 'POST':
        records = Product_Model.objects.filter(
            category__icontains=form['category'].value(),
            product_name__icontains=form['product_name'].value()
        )

        # Refetch profits for the filtered products
        profits = [record.profitability.calculate_profit() for record in records]

    dicti = {
        "records": records,
        "form": form,
        "profits": profits,  # Include profits in the context
    }

    return render(request,'stock_app/home. html',dicti)"""
    



def details(request,id):
    item=get_object_or_404(Product_Model,pk=id)
    data={
        "item":item,
    }

    return render(request,'stock_app/details.html',data)

    

class Add_Record(CreateView):
    model=Product_Model
    form_class=Product_ModelForm
    template_name='stock_app/add_record.html'
    success_url=reverse_lazy('index_home')

    def form_valid(self,form):
        messages.success(self.request,'Item Added successfully')
        return super().form_valid(form)



class Edit_Record(UpdateView):
    form_class=Product_ModelForm
    model=Product_Model
    template_name='stock_app/edit_record.html'
    success_url=reverse_lazy('index_home')

    def form_valid(self,form):
        messages.success(self.request,'Item Updated successfully')
        return super().form_valid(form)

class Delete_Record(DeleteView):
    model=Product_Model
    template_name='stock_app/delete_record.html'
    success_url=reverse_lazy('index_home')

    def form_valid(self,form):
        messages.success(self.request,'Item Deleted Successfully')
        return super().form_valid(form)


#csv



def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="records.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'Name','Items','Category','Unit(Rwf)','Cost(Rwf)','Remain(i)','Profit(Rwf)'])

    records = Product_Model.objects.all()  
    for record in records:
        writer.writerow([record.id, record.product_name, record.category, record.unit_price, record.selling_price, record.selling_price, record.selling_price])

    return response


# pdf

def pdf_export(request):
    # Create bytestream buffer
    buffer = io.BytesIO()
    # Create canvas
    canva = canvas.Canvas(buffer, pagesize=letter, bottomup=0)
    text_object = canva.beginText()
    text_object.setTextOrigin(inch, inch)  # Inch by inch
    text_object.setFont("Helvetica", 14)  # 14 is fontsize

    # Add lines of text
    records = Product_Model.objects.all()
    text_lines = []

    for record in records:
        text_lines.append(f'ID: {record.id}')
        text_lines.append(f'Name: {record.product_name}')
        text_lines.append(f'Category: {record.category}')
        text_lines.append(f'Purchasing price: {record.unit_price}')
        text_lines.append(f'Selling price: {record.selling_price}')
        text_lines.append(' ')

    for line in text_lines:
        text_object.textLine(line)
    
    # Finish
    canva.drawText(text_object)
    canva.showPage()
    canva.save()
    buffer.seek(0)

    # Return the PDF as an attachment
    return FileResponse(buffer, as_attachment=True, filename='records_.pdf')
 

def get_item(request,id):
    queryset=Product_Model.objects.get(pk=id)
    form=Get_ItemForm(request.POST or None, instance=queryset)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.items_instock -=instance.qty_sold
        messages.success(request,"Issued Successfully." 
                         + str(instance.items_instock) + " " + str(instance.product_name)
                           + "s"+ " Left in stock.")
        instance.save()
        return redirect('/stock/full_details/'+str(instance.id)+"/")
    context={
        'queryset':queryset,
        'form':form,
    }
    return render(request,'stock_app/get_item.html',context) 



""" def add_quantity(request,id):
        queryset=Product_Model.objects.get(pk=id)
        form=Add_Stock(request.POST or None, instance=queryset)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.items_instock +=instance.qty_added
            messages.success(request,"Items Added Successfully." 
                            + str(instance.items_instock) + " " + str(instance.product_name)
                            + "s"+ " Left in stock.")
            instance.save()
            return redirect('/stock/full_details/'+str(instance.id)+"/")
        context={
            'queryset':queryset,
            'form':form,
        }
        return render(request,'stock_app/add_stock.html',context) """





def purchase_history(request):
    purchases = Purchase_History.objects.all()
    form = PurchaseHistoryFilterForm(request.GET)
    # we have to filter the records before applying pagination. 
    if form.is_valid():
        start_date=form.cleaned_data.get('start_date')
        end_date=form.cleaned_data.get('end_date')
        
        if start_date:
            purchases=purchases.filter(purchase_date__gte=start_date)
        if end_date:
            purchases=purchases.filter(purchase_date__lte=end_date)
    else:
        purchases = Purchase_History.objects.all()

        """
        __gte stands for "greater than or equal to." It's used to find records 
        where the specified date field is greater than or equal to the provided date.
          In this case, it filters the records where purchase_date is greater than or equal to start_date.

__lte stands for "less than or equal to."
 It's used to find records where the specified date field is less than or equal to the provided date. 
 In this case, it filters the records where purchase_date is less than or equal to end_date
        
        """

    paginator = Paginator(purchases, 10)  # Show 10 records per page

    page = request.GET.get('page')
    try:
        purchases = paginator.page(page)
    except PageNotAnInteger:
        # If the page is not an integer, deliver the first page.
        purchases = paginator.page(1)
    except EmptyPage:
        # If the page is out of range (e.g. 9999), deliver the last page.
        purchases = paginator.page(paginator.num_pages)

  

    context = {
        'purchases': purchases,
        'form':form,
    }
    return render(request, 'stock_app/purchase_history.html', context)



def sales_history(request):
    sales = Sales_History.objects.all()
    form=Sales_History_Filter_Form(request.GET)

    if form.is_valid():
        start_date=form.cleaned_data.get('start_date')
        end_date=form.cleaned_data.get('end_date')

        if start_date:
            sales=sales.filter(sold_on__gte=start_date)
        if end_date:
            sales=sales.filter(sold_on__lte=end_date)
    else:
        sales=Sales_History.objects.all()

    paginator = Paginator(sales, 10)  # Show 10 records per page

    page = request.GET.get('page')
    try:
        sales = paginator.page(page)
    except PageNotAnInteger:
        # If the page is not an integer, deliver the first page.
        sales = paginator.page(1)
    except EmptyPage:
        # If the page is out of range (e.g. 9999), deliver the last page.
        purchases = paginator.page(paginator.num_pages)

    context = {
        'sales': sales,
        'form':form,
    }
    return render(request, 'stock_app/sales_history.html', context)








def add_purchase_history(request,id):
    product = get_object_or_404(Product_Model, pk=id)

    if request.method == 'POST':
        form = PurchaseHistoryForm(request.POST)
        if form.is_valid():
            purchase_history = form.save(commit=False)
            purchase_history.product = product
            purchase_history.purchase_date = date.today()  
            purchase_history.save()

            # Update the product's 'items_instock' field.
            product.items_instock += purchase_history.quantity_added
            product.save()

            messages.success(request, f"{purchase_history.quantity_added} items added to {product.product_name} stock.")
            return redirect('/stock/full_details/'+str(product.id)+"/")

    else:
        form = PurchaseHistoryForm()

    return render(request, 'stock_app/add_purchase_history.html', {'form': form, 'product': product})


""" def add_sales_history(request,id):
    product = get_object_or_404(Product_Model, pk=id)

    if request.method == 'POST':
        form = Sales_HistoryForm(request.POST)
        if form.is_valid():
            sales_history = form.save(commit=False)
            sales_history.product = product
            sales_history.purchase_date = date.today()  
            sales_history.save()

            # Update the product's 'items_instock' field.
            product.items_instock -= sales_history .quantity_sold
            product.save()

            messages.success(request, f"{sales_history.quantity_sold} items Taken out from {product.product_name} stock.")
            return redirect('/stock/full_details/'+str(product.id)+"/")

    else:
        form = Sales_HistoryForm()

    return render(request, 'stock_app/add_sales_history.html', {'form': form, 'product': product}) """



def stat_purchases(request):
    # Calculate the total quantity purchased for each category
    categories = Product_Model.objects.values('category').distinct()
    products = Product_Model.objects.values('product_name').distinct()
    category_totals = []
    products_totals = []

    for category in categories:
        total_qty_purchased = Purchase_History.objects.filter(product__category=category['category']).aggregate(total=Sum('quantity_added'))['total']
        category_totals.append({'category': category['category'], 'total_qty_purchased': total_qty_purchased})
    
    for item in products:
        total_qty_purchased = Purchase_History.objects.filter(product__product_name=item['product_name']).aggregate(total=Sum('quantity_added'))['total']
        products_totals.append({'product': item['product_name'], 'total_qty_purchased': total_qty_purchased})

    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest' and request.method == 'GET':
        # Get time filter form data from request
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')

        # Add checks for valid start_date and end_date
        if start_date and end_date:
            # Filter data for the specified date range
            category_totals = Purchase_History.objects.filter(purchase_date__range=(start_date, end_date)).values('product__category').annotate(total_qty_purchased=Sum('quantity_added'))
            products_totals = Purchase_History.objects.filter(purchase_date__range=(start_date, end_date)).values('product__product_name').annotate(total_qty_purchased=Sum('quantity_added'))
            
            # Prepare the data to send back as JSON
            chart1_data = list(category_totals)
            chart3_data = list(products_totals)

            return JsonResponse({'chart1_data': chart1_data, 'chart3_data': chart3_data})

    # For non-AJAX or non-GET requests, render the initial page
 

    context = {
        'chart1_data': category_totals,
        'chart3_data': products_totals,
        'time_filter_form': TimeFilterForm()
    }

    return render(request, 'stock_app/purchase_statistics.html', context)



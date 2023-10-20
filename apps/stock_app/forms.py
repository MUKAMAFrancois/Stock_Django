from apps.stock_app.models import *
from django import forms

class Product_ModelForm(forms.ModelForm):
    class Meta:
        model=Product_Model
        fields=['product_name','items_instock','category','unit_price',
                'mgf_date','expiry_date','selling_price','description']
        # Validation of forms

        def clean_product_name(self):
            name_product=self.cleaned_data.get('product_name')
            if not name_product:
                raise forms.ValidationError("This Field is Required")
            
            for product in Product_Model.objects.all():
                if product.product_name == name_product:
                    raise forms.ValidationError(name_product+ "Exists!")
            return name_product
  

class Search_Form(forms.ModelForm):
    class Meta:
        model=Product_Model
        fields=['category','product_name']   

class Get_ItemForm(forms.ModelForm):
    class Meta:
        model=Product_Model
        fields=['qty_sold','sold_by']

#class Add_Stock(forms.ModelForm):
#    class Meta:
 #       model=Product_Model
  #      fields=['qty_added']


class PurchaseHistoryForm(forms.ModelForm):
    class Meta:
        model = Purchase_History
        fields = ['quantity_added']

class Sales_HistoryForm(forms.ModelForm):
    class Meta:
        model = Sales_History
        fields = ['quantity_sold']





class PurchaseHistoryFilterForm(forms.Form):
    start_date = forms.DateField(label='Start Date', required=False, widget=forms.TextInput(attrs={'type': 'date'}))
    end_date = forms.DateField(label='End Date', required=False, widget=forms.TextInput(attrs={'type': 'date'}))

class Sales_History_Filter_Form(forms.Form):
    start_date=forms.DateField(label='From ', required=False,widget=forms.TextInput(attrs={'type':'date'}))
    end_date=forms.DateField(label='Up to ', required=False, widget=forms.TextInput(attrs={'type':'date'}))



class TimeFilterForm(forms.Form):
    start_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

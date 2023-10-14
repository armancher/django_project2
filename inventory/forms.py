from django import forms
from inventory.models import Inventory, Product, Order, Tag


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ('name', 'address', 'phone_number')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number.isdigit():
            raise forms.ValidationError('Phone number must be digit')
        if phone_number.startswith('09'):
            raise forms.ValidationError('Phone number can not be a mobile number')
        return phone_number


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('price', 'tag', 'inventory')
        widgets = {
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'tag': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'inventory': forms.Select(attrs={'class': 'form-control'}),
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('weight', 'product')
        widgets = {
            'weight': forms.TextInput(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

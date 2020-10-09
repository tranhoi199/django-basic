from django import forms 

from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder":"Your title"}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
        "class":"new-class-name two",
        "placeholder":"Your description",
    }))
    price = forms.DecimalField(initial=199.99)
    class Meta:
        model = Product 
        fields = [
            'title',
            'description',
            'price'
        ]
    # def clean_title(self, *args, **kwargs):
    #     title = self.cleaned_data.get('title')
    #     if "CFE" in title:
    #         return title
    #     else:
    #         raise forms.ValidationError("This is not a validation")

class RawProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder":"Your title"}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
        "class":"new-class-name two",
        "placeholder":"Your description",
    }))
    price = forms.DecimalField(initial=199.99)
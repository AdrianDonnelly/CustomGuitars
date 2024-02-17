from django import forms
from .models import ProductReview

class ProductReview(forms.ModelForm):
    review = forms.CharField(widget=forms.Textarea(attrs={'review':"Write review:"}))
    
    class Meta:
        model = ProductReview
        fields = ['review','rating']
    


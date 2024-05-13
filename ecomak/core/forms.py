from django import forms
from stripe import Review
from core.models import ProductReview

RATING = (
    (1,'★☆☆☆☆'),
    (2,'★★☆☆☆'),
    (3,'★★★☆☆'),
    (4,'★★★★☆'),
    (5,'★★★★★'),
)


# class ProductReviewForm(forms.ModelForm):
#     review = forms.CharField(widget=forms.Textarea(attrs={
#         'placeholder': 'Write review',
#         'name': 'review',  # Adding name attribute for the review field
#     }))
#     rating = forms.ChoiceField(choices=RATING, widget=forms.Select(attrs={
#         'name': 'rating',  # Adding name attribute for the rating field
#     }))

#     class Meta:
#         model = ProductReview
#         fields = ["review", "rating"]

class ProductReviewForm(forms.ModelForm):
    review = forms.CharField(widget=forms.Textarea(attrs={'placeholder':"Write Review"}))

    class Meta: 
        model = ProductReview
        fields = ['review','rating']

        

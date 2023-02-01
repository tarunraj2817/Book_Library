from django import forms
from .models import AuthorDeatils,BookDetails,PublicationDetails

class AuthorForm(forms.ModelForm):
    class Meta:
        model = AuthorDeatils
        fields = "__all__"

class BookForm(forms.ModelForm):
    class Meta:
        model = BookDetails
        fields = "__all__"

class PublicationForm(forms.ModelForm):
    class Meta:
        model = PublicationDetails
        fields = "__all__"

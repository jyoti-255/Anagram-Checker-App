from django import forms
class AnagramForm(forms.Form):
   word1=forms.CharField(label='First Word',max_length=100)
   word2=forms.CharField(label='Second Word',max_length=100)
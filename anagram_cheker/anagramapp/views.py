from django.shortcuts import render
from .forms import AnagramForm

def is_anagram(word1, word2):
    return sorted(word1.lower()) == sorted(word2.lower())

def home(request):
    result = None
    form = AnagramForm()  
    if request.method == 'POST':
        form = AnagramForm(request.POST)
        if form.is_valid():
            word1 = form.cleaned_data['word1']
            word2 = form.cleaned_data['word2']
            result = is_anagram(word1, word2)
    
    return render(request, "home.html", {"form": form, "result": result})

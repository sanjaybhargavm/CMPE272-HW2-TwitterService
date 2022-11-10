from django.http import HttpResponse
from django.shortcuts import redirect, render

## Author: Sanjay Bhargav Madamanchi

def load_home_page(request):
    
    content = ''
    if request.method == 'POST':
        content = request.POST.get('content', '')
    
    if content:
        print('Content:' + content);
        return redirect('home')
        
    return render(request, 'home.html')



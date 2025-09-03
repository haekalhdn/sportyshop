from django.shortcuts import render
def show_main(request):
    context = {
        'npm' : '2406431536',
        'name': 'Haekal Handrian',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
# Create your views here.

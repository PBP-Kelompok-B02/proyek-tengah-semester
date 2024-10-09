from django.shortcuts import render


def show_main(request):
    context = {
        'group' : 'PBP B02',
    }

    return render(request, "main.html", context)

# Create your views here.

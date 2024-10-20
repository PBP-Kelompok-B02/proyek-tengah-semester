from django.shortcuts import render


def show_main(request):
    context = {
        'group' : 'PBP B02',
    }

    return render(request, "main.html", context)

def show_detail(request, id):
    context = {
        "id" : id
    }

    return render(request, "detail-makanan.html", context)

from django.shortcuts import render


def main_index(request):

    ctx = {

    }
    return render(request, 'main/index.html', ctx)


def contact(request):

    ctx = {

    }
    return render(request, 'main/contact.html', ctx)

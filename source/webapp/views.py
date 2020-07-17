from django.shortcuts import render


def index_view(request):
    return render(request, 'index.html')


def answer_view(request):
    first_price = request.GET.getlist('first_price')[0]
    second_price = request.GET.getlist('second_price')[0]
    consider = request.GET.getlist('consider')[0]
    if consider == 'add':
        total = int(first_price) + int(second_price)
        context = {
            'first_price': request.GET.getlist('first_price')[0],
            'second_price': request.GET.getlist('second_price')[0],
            'consider': '+',
            'total': total,
        }
        total_new = str(total)
        return render(request, 'answer.html', context)
    elif consider == 'subtract':
        total = int(first_price) - int(second_price)
        context = {
            'first_price': request.GET.getlist('first_price')[0],
            'second_price': request.GET.getlist('second_price')[0],
            'consider': '-',
            'total': total,
        }
        return render(request, 'answer.html', context)
    elif consider == 'multiply':
        total = int(first_price) * int(second_price)
        context = {
            'first_price': request.GET.getlist('first_price')[0],
            'second_price': request.GET.getlist('second_price')[0],
            'consider': '*',
            'total': total,
        }
        return render(request, 'answer.html', context)
    elif consider == 'divide':
        total = int(first_price) / int(second_price)
        context = {
            'first_price': request.GET.getlist('first_price')[0],
            'second_price': request.GET.getlist('second_price')[0],
            'consider': ':',
            'total': total,
        }
        return render(request, 'answer.html', context)

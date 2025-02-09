# from django.shortcuts import render


# from ice_cream.models import IceCream


# def index(request):
#     template_name = 'homepage/index.html'
#     # ice_cream_list = IceCream.objects.all()
#     ice_cream_list = IceCream.objects.values(
#             'id', 'title', 'description'
#         ).filter(is_on_main=True)
#     context = {
#         'ice_cream_list': ice_cream_list,
#     }
#     return render(request, template_name, context)


# homepage/views.py
from django.shortcuts import render

from ice_cream.models import IceCream

def index(request):
    template_name = 'homepage/index.html'
    # Заключаем вызов методов в скобки
    # (это стандартный способ переноса длинных строк в Python);
    # каждый вызов пишем с новой строки, так проще читать код:
    ice_cream_list = IceCream.objects.values(
            'id', 'title', 'description'
        # Верни только те объекты, у которых в поле is_on_main указано True:
        ).filter(is_on_main=True)
    # .exclude(is_published=False)
    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template_name, context)

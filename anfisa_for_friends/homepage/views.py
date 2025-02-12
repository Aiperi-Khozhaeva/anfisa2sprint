from django.db.models import Q
from django.shortcuts import render

from ice_cream.models import IceCream

def index(request):
    template_name = 'homepage/index.html'
    # Заключаем вызов методов в скобки
    # (это стандартный способ переноса длинных строк в Python);
    # каждый вызов пишем с новой строки, так проще читать код:

    ice_cream_list = IceCream.objects.values(
            'id', 'title', 'description'
        ).filter(
            is_published=True, is_on_main=True
            # Q(is_published=True)
            # & Q(is_on_main=True)
            # | Q(title__contains='пломбир')
            # & Q(is_published=True)
            ).order_by('title')[1:4]

    context = {
        'ice_cream_list': ice_cream_list,
    }

    return render(request, template_name, context)


"""========================================================================="""

    # categories = Category.objects.values(
    #     'id', 'output_order', 'title'
    # ).order_by(
    #     'output_order', 'title'
    # )

    # context = {
    #     # 'ice_cream_list': ice_cream_list,
    #     'categories': categories
    # }

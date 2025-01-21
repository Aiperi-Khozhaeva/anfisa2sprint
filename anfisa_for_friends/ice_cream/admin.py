from django.contrib import admin

# Register your models here.
from .models import Category
admin.site.register(Category)

from .models import Topping
admin.site.register(Topping)


from .models import Wrapper
admin.site.register(Wrapper)

from .models import IceCream
# admin.site.register(IceCream)

admin.site.empty_value_display = 'Не задано'

class IceCreamAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper'
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category'
    )
    search_fields = ('title',) 
    list_filter = ('category',)
    list_display_links = ('title',)

    empty_value_display = 'Не задано'
    filter_horizontal = ('toppings',)

admin.site.register(IceCream, IceCreamAdmin)

...

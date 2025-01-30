from django.contrib import admin


from .models import Category
# admin.site.register(Category)


from .models import Topping
admin.site.register(Topping)


from .models import Wrapper
admin.site.register(Wrapper)


from .models import IceCream
# admin.site.register(IceCream)

admin.site.empty_value_display = 'Не задано'

class IceCreamInline(admin.TabularInline):
    model = IceCream
    extra = 0

class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        IceCreamInline,
    )
    list_display = (
        'title',
    )

admin.site.register(Category, CategoryAdmin)


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

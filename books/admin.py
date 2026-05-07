from django.contrib import admin
from .models import Class, Category, Book


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'book_count', 'created_at')
    search_fields = ('name',)
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at')

    def book_count(self, obj):
        return obj.book_set.count()

    book_count.short_description = 'Books'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'book_count', 'created_at')
    search_fields = ('name',)
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at')

    def book_count(self, obj):
        return obj.book_set.count()

    book_count.short_description = 'Books'


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'class_name',
        'category',
        'publication',
        'created_at',
    )

    list_filter = (
        'category',
        'class_name',
        'publication',
        'created_at',
    )

    search_fields = (
        'name',
        'about',
        'category__name',
        'class_name__name',
    )

    autocomplete_fields = (
        'category',
        'class_name',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
    )

    fieldsets = (
        ('Basic Information', {
            'fields': (
                'name',
                'about',
            )
        }),

        ('Relations', {
            'fields': (
                'class_name',
                'category',
            )
        }),

        ('Files', {
            'fields': (
                'image',
                'file',
            )
        }),

        ('Dates', {
            'fields': (
                'publication',
                'created_at',
                'updated_at',
            )
        }),
    )

    ordering = ('-created_at',)
    date_hierarchy = 'publication'
    save_on_top = True
    list_per_page = 20

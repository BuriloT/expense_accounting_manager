from django.contrib import admin

from api.models import Category, Organization, Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount', 'category', 'organization',
                    'user', 'description', 'time')
    list_filter = ('time', 'amount')
    search_fields = ('user__username', 'organization__name',
                     'category__name', 'description')
    empty_value_display = '-пусто-'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_filter = ('name', 'description')
    search_fields = ('name', 'description')
    empty_value_display = '-пусто-'


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_filter = ('name', 'description')
    search_fields = ('name', 'description')
    empty_value_display = '-пусто-'

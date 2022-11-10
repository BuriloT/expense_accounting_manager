from django.contrib import admin

from users.models import User, UserCategory


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name',
                    'balance', 'is_staff')
    list_filter = ('username', 'email', 'balance')


@admin.register(UserCategory)
class UserCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'user')

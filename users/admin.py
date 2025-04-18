from django.contrib import admin

from users.models import User, Payment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')

@admin.register(Payment)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'payment_amount', 'payment_method')
    search_fields = ('user', 'payment_method')

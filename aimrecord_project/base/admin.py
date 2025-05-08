from django.contrib import admin
from .models import Competition
from .models import Profile

admin.site.register(Competition)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'verified')  # Какие поля показывать в списке
    list_filter = ('verified',)  # Фильтры справа
    search_fields = ('user__username',)  # Поиск по связанному пользователю

# Register your models here.

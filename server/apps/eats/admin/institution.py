from django.contrib import admin

from apps.eats.models import Institution


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'address', 'owner',
    )
    readonly_fields = (
        'latitude', 'longitude', 'average_food_cost', 'owner'
    )

from django.contrib import admin

from .models import Flat, Complaint, Owner


class FlatAdmin(admin.ModelAdmin):
    search_fields = ("town", "address", "owner")
    readonly_fields = ("created_at",)
    list_display = (
        "address",
        "price",
        "new_building",
        "construction_year",
        "town",
        "get_owners",
    )

    def get_owners(self, obj):
        return ", ".join([owner.full_name for owner in obj.owners.all()])
    get_owners.short_description = 'Владельцы'
    
    list_editable = ("new_building",)
    list_filter = ("new_building", "rooms_number", "has_balcony")
    raw_id_fields = ("likes",)


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ("flat",)
    list_display = ("user", "flat", "text")


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ("flats",)
    list_display = ["full_name", "phonenumber", "pure_phone"]


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)

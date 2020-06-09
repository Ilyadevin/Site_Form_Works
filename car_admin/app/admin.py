from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm


class CarAdmin(admin.ModelAdmin):
    pass


class ReviewAdmin(admin.ModelAdmin):
    form = ReviewAdminForm


class SearchForNames(admin.ModelAdmin.search_fields):
    search_fields = ['BRAND', 'REVIEW COUNT']


admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)

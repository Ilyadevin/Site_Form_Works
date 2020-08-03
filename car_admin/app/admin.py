from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm


class ReviewAdmin(admin.ModelAdmin):
    model = "qwe"
    review = Review
    form = ReviewAdminForm


admin.site.register(Car, ReviewAdmin)
admin.site.register(Review, ReviewAdmin)
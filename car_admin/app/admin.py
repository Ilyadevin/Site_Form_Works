from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm


class ReviewAdmin(admin.ModelAdmin):
    model = Car
    review = Review
    form = ReviewAdminForm


admin.site.register(Review, ReviewAdmin)

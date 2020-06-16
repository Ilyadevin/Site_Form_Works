from django import forms


class ReviewAdminForm(forms.ModelForm):
    brand = forms.CharField(label='Brand', max_length=15)
    mark = forms.CharField(label='Mark', max_length=64)
    review = forms.CharField(label='Review', )

    class Meta:
        fields = ('car', 'title', 'text')

from django import forms


class ReviewAdminForm(forms.ModelForm):
    brand = forms.CharField(label='brand', max_length=15)
    mark = forms.CharField(label='model', max_length=64)
    review = forms.CharField(label='Review', )

    class Meta:
        fields = ('car', 'title', 'text')

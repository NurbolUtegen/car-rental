from django import forms
from .models import Rental

class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['car', 'customer', 'start_date', 'end_date']
        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date": forms.DateInput(attrs={"type": "date"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        car = cleaned_data.get("car")
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        if car and start_date and end_date:
            overlapping_rentals = Rental.objects.filter(
                car=car,
                end_date__gte=start_date,
                start_date__lte=end_date
            ).exists()

            if overlapping_rentals:
                raise forms.ValidationError("Эта машина уже арендована на указанные даты.")

        return cleaned_data

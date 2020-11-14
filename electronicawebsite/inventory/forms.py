import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class OrderProductForm(forms.Form):
    order_date = forms.DateField(help_text="Enter the date")

    def clean_renewal_date(self):
        data = self.cleaned_data['order_date']

        # Check the data is not in the past
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - can´t order in past'))

        # Check id a date is in the allowed range (+4 weeks from today)
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - order more than 4 weeks ahead'))

        # Remember to always return the cleaned data.
        return data

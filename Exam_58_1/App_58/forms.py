from django import forms

class BMICalculatorForm(forms.Form):
    height = forms.FloatField(
        label='Height (cm)',
        min_value=1,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    weight = forms.FloatField(
        label='Weight (kg)',
        min_value=1,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
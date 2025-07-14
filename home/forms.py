from django import forms

class FlavourForm(forms.Form):
    flavour = forms.ChoiceField(
        choices=[
            ('chocolate', 'Chocolate'),
            ('vanilla', 'Vanilla'),
            ('strawberry', 'Strawberry'),
            ('butterscotch', 'Butterscotch'),
            ('mango', 'Mango'),
        ],
        widget=forms.Select(attrs={'class': 'form-select'})
    )

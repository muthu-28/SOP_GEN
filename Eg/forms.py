# myapp/forms.py
from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["email", "full_name", "age", "highest_education", "institute", "country",]


class SopForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ["dept","work_exp", "inscanada", "POS", "feepaid", "amount", "completed_gic", "gicamount"]


class LastForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ["read", "write", "speak", "listen"]


from django.contrib.auth.forms import UserCreationForm

from restaurant_app.models import Cook


class CookCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + ("years_of_experience", )

    # def clean_license_number(self):
    #     license_num = self.cleaned_data.get("license_number")
    #     if len(license_num) != 8:
    #         raise forms.ValidationError(
    #             "Length of license number must be only 8 characters"
    #         )
    #     if not license_num[:3].isalpha() and not license_num[:3].isupper():
    #         raise forms.ValidationError(
    #             "First 3 characters must be uppercase letters"
    #         )
    #     if not license_num[3:].isdigit():
    #         raise forms.ValidationError("Last 5 characters must be digits")
    #
    #     return license_num
from django import forms
from django.core import validators

#custom Validation function
# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError("NAME NEEDS TO STARTS WITH Z")

class FormName(forms.Form):
    name = forms.CharField() #name = forms.CharField(validators=[check_for_z]) custom validation function goes here if defined
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter Your Email Again:')
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()  # returns all the clean data for the entire form
        email = all_clean_data['email'] #all_clean_data is a dictionary containing all the clean data from the form
        vmail = all_clean_data['verify_email']
        print(all_clean_data)
        if email.casefold() != vmail.casefold():
            raise forms.ValidationError("MAKE SURE EMAILS MATCH!")


    # botcatcher = forms.CharField(required=False,
    #                             widget=forms.HiddenInput,
    #                             validators=[validators.MaxLengthValidator(0)]) #this is using build in validator but don't forget to import Validators




    # This how we can use form validation. A bot might try breaking your website so below is a botcatcher
    # Pretty much you will never do this clean_botcatcher because there are django built-in Validators
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("GOTCHA BOT!")
    #     return botcatcher

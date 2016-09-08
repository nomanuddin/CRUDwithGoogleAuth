from UserAdmin.models import *
from django.forms import ModelForm


#for createion of users
class UserDataForm(ModelForm):
    class Meta:
        model = userdata
        fields = ['first_name','last_name','iban']

#for cleaning of data
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        return last_name

    def clean_iban(self):
        iban = self.cleaned_data.get('iban')
        return iban

#for reading users details // iban and first name can also be added
class UserReadForm(ModelForm):
    class Meta:
        model = userdata
        exclude = ['first_name','iban']

    def clean_first_name(self):
        last_name = self.cleaned_data.get('last_name')
        return last_name


# for deletion
class UserDeleteForm(ModelForm):
    class Meta:
        model = userdata
        exclude = ['first_name','last_name']

    def clean_iban(self):
        iban = self.cleaned_data.get('iban')
        return iban
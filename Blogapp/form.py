#coding: utf-8
from django import forms
from django.utils.translation import ugettext_lazy as _


class RegisterForm(forms.Form):
    username = forms.CharField(label=_(u'用户名'), max_length=30)
    password1 = forms.CharField(label=_(u'密码'), widget=forms.PasswordInput())
    password2 = forms.CharField(label=_(u'确认密码'), widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()

        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(_(u'两次密码输入不一致'))
        return cleaned_data
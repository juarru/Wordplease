# -*- coding: utf-8 -*-

from django import forms

class LoginForm(forms.Form):

    login_username = forms.CharField()
    login_password = forms.CharField()


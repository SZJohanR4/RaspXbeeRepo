from django import forms

class loginForm(forms.Form):
    user_name=forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class':'form-control', 'id':'usuario', 'placeholder':'Usuario'}))
    password=forms.CharField(max_length=40,widget=forms.PasswordInput(attrs={'class':'form-control', 'id':'password', 'placeholder':'Password'}))

from django import forms

class EmployeeForm(forms.Form):
	name = forms.CharField()
	age = forms.IntegerField()
	salary = forms.CharField()
	address = forms.CharField()
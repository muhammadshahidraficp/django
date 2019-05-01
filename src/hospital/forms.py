from django import forms

class ContactForm(forms.Form):
	firstname=forms.CharField(
				widget=forms.TextInput(
					attrs={
						"class":"form-control",
						"placeholder":"First Name"
						}
				)
			)
	email = forms.EmailField(
		  widget=forms.EmailInput(
				attrs={
					"class":"form-control",
					"placeholder":"Email"
				}
				)
		   )
	content = forms.CharField(
		widget=forms.Textarea(
			attrs={
				"class":"form-control",
				"placeholder":"Your content"
				}
			)
		)

	def clean_email(self):
	 email = self.cleaned_data.get("email")
	 if not "gmail.com" in email:
		 raise forms.ValidationError("Email has to be gmail.com")
	 return email    

class LoginForm(forms.Form):
   username = forms.CharField(widget=forms.TextInput(
			attrs={
				"class":"form-control",
				"placeholder":"muhammedmsr"
				}
			)
        )
   password =forms.CharField(
   		widget=forms.PasswordInput(
			attrs={
				"class":"form-control",
				"placeholder":"*******"
				}
			)
		)	 
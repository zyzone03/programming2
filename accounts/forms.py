from django import forms 
from django.contrib.auth.forms import USerCreationForm
from django.contrib.auth import get_user_model


class SignupForm(USerCreationForm):
	class Meta:
		fields = USerCreationForm.Meta.fields + ('email',)

		def clean_email(self):
			email = self.cleaned_data.get('email', None)
			if email:
				User = get_user_model()
				if User.objects.filter(email=email).exists():
					raise forms.ValidationError('중복된 이메일')
			return email
			
from django import forms
from noticias.models import Noticia

class ProfileForm(forms.ModelForm):

	class Meta:
		model = Profile
		fields = ['titulo','descripcion','imagen']

	def datos(self):
		return self.data

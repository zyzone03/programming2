from django.db import models
from django import forms
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator
from programming2.utils import random_name_upload_to

def min_length_validator(value):
	if len(value) < 3:
		raise forms.ValidationError('3글자 이상 입력해주세요')

import re

def phone_validator(value):
	number = ''.join(re.findall(r'\d+', value))
	if not re.match(r'^01[01678]\d{7,8}$', number):
		raise forms.ValidationError('휴대폰 번호 입력!')
	# return RegexValidator(r'^01[01678]\d{7,8}$',
	# 	message = '휴대폰 번호 입력해주세요')(number)



class PhoneField(models.CharField):
	def __init__(self, *args, **kwargs):
		kwargs.setdefault('max_length', 11)
		super(PhoneField, self).__init__(*args, **kwargs)
		self.validators.append(phone_validator)

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=100, validators=[min_length_validator],
		help_text='제목을 100자 이내로 입력하세요')
	content = models.TextField()
	photo = models.ImageField(blank=True, upload_to=random_name_upload_to)
	phone = PhoneField(max_length=20, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	#기본적으로 timezone 정보를 담음
	updated_at = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:post_detail', args=[self.pk])

class Comment(models.Model):
	post = models.ForeignKey(Post)
	message = models.TextField(blank=True)

	def __str__(self):
		return self.message

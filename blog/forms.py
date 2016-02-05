from django import forms 
from blog.models import Post, Comment

class PostForm(forms.ModelForm):
	is_agree = forms.BooleanField(label = "약관동의",
		error_messages={'required': "동의하셔야 이용 가능합니다."})
	class Meta:
		model = Post
		fields = '__all__'


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		#fields = '__all__'
		#특정 필드 지정해줘서 메시지만 띄우면 댓글마다 일일이 포스트 지정 필요 없음
		#fields = ('message') -> 이것은 튜플이 아니라 string
		fields = ['message'] #그래서 안전하게 list로 해주는 것이 좋음
		

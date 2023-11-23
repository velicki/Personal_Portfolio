from django import forms
from django.forms import ModelForm
from .models import Project, About, Topic

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

class AboutForm(ModelForm):
    class Meta:
        model = About
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AboutForm, self).__init__(*args, **kwargs)
        self.fields['body'].widget = forms.Textarea(attrs={
            'id': 'myTextarea'})

class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'


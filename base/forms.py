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

class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'


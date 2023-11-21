from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count
from .models import Project, Topic, About
from .forms import ProjectForm, AboutForm, TopicForm



def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    qt = request.GET.get('qt') if request.GET.get('qt') != None else ''
    if q == '' and qt == '':
        project = About.objects.all()
    elif q != '':
        project = Project.objects.filter(
            Q(topic__name__icontains=q) |
            Q(name__icontains=q) |
            Q(description__icontains=q))
    else:
        project = Project.objects.filter(topic__name__icontains=qt)
    topics = Topic.objects.annotate(project_count=Count('project'))
    context = {'project':project, 'topics':topics, 'q':q, 'qt':qt}
    return render(request, 'base/home.html', context)

def projects(request, pk):
    projects = Project.objects.get(id=pk)
    topics = Topic.objects.annotate(project_count=Count('project'))
    context = {'projects':projects, 'topics':topics}
    return render(request, 'base/projects.html', context)

@login_required(login_url='home')
def projectForm(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    topics = Topic.objects.annotate(project_count=Count('project'))
    context = {'form': form, 'topics':topics}
    return render(request, 'base/project_form.html', context)

@login_required(login_url='home')
def updateProject(request, pk):
    projects = Project.objects.get(id=pk)
    form = ProjectForm(instance=projects)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=projects)
        if form.is_valid():
            form.save()
            return redirect('home')
    topics = Topic.objects.annotate(project_count=Count('project'))
    context = {'form': form, 'topics':topics}
    return render(request, 'base/project_form.html', context)

@login_required(login_url='home')
def updateTopic(request, pk):
    topic = Topic.objects.get(id=pk)
    form = TopicForm(instance=topic)
    if request.method == 'POST':
        form = TopicForm(request.POST, instance=topic)
        if form.is_valid():
            form.save()
            return redirect('add-topic')
    #topic = Topic.objects.all()
    topics = Topic.objects.annotate(project_count=Count('project'))
    add = 'Edit this'
    context = {'form': form, 'topics':topics, 'topic':topic, 'add':add}
    return render(request, 'base/topic_form.html', context)

@login_required(login_url='home')
def newTopic(request):
    form = TopicForm()
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add-topic')
    topic = Topic.objects.all()
    topics = Topic.objects.annotate(project_count=Count('project'))
    add = 'Add new'
    context = {'form': form, 'topics':topics, 'topic':topic, 'add':add}
    return render(request, 'base/topic_form.html', context)

@login_required(login_url='home')
def updateAbout(request, pk):
    projects = About.objects.get(id=pk)
    form = AboutForm(instance=projects)
    if request.method == 'POST':
        form = AboutForm(request.POST, instance=projects)
        if form.is_valid():
            form.save()
            return redirect('home')
    topics = Topic.objects.annotate(project_count=Count('project'))
    context = {'form': form, 'topics':topics}
    return render(request, 'base/about_form.html', context)

@login_required(login_url='home')
def deleteProject(request, pk):
    projects = Project.objects.get(id=pk)
    if request.method == 'POST':
        projects.delete()
        return redirect('home')
    topics = Topic.objects.annotate(project_count=Count('project'))
    return render(request, 'base/delete.html', {'obj':projects, 'topics':topics})

@login_required(login_url='home')
def deleteTopic(request, pk):
    topic = Topic.objects.get(id=pk)
    if request.method == 'POST':
        topic.delete()
        return redirect('add-topic')
    topics = Topic.objects.annotate(project_count=Count('project'))
    return render(request, 'base/delete.html', {'obj':topic, 'topics':topics})

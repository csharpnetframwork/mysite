from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from django.contrib import messages
from .models import Idea, Comment, Like
from .forms import IdeaForm, CommentForm, RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('idea_list')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def idea_list(request):
    category = request.GET.get('category', '')
    if category:
        ideas = Idea.objects.filter(category=category).order_by('-created_at')
    else:
        ideas = Idea.objects.all().order_by('-created_at')
    return render(request, 'ideas/idea_list.html', {'ideas': ideas, 'current_category': category})

@login_required
def create_idea(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST)
        if form.is_valid():
            idea = form.save(commit=False)
            idea.user = request.user
            idea.save()
            messages.success(request, 'Your idea has been posted!')
            return redirect('idea_list')
    else:
        form = IdeaForm()
    return render(request, 'ideas/create_idea.html', {'form': form})

@login_required
def edit_idea(request, pk):
    idea = get_object_or_404(Idea, pk=pk, user=request.user)
    if request.method == 'POST':
        form = IdeaForm(request.POST, instance=idea)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your idea has been updated!')
            return redirect('idea_list')
    else:
        form = IdeaForm(instance=idea)
    return render(request, 'ideas/edit_idea.html', {'form': form})

@login_required
def delete_idea(request, pk):
    idea = get_object_or_404(Idea, pk=pk, user=request.user)
    idea.delete()
    messages.success(request, 'Your idea has been deleted!')
    return redirect('idea_list')

@login_required
def like_idea(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    Like.objects.get_or_create(idea=idea, user=request.user)
    return redirect('idea_list')

@login_required
def comment_idea(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.idea = idea
            comment.save()
            messages.success(request, 'Your comment has been added!')
            return redirect('idea_list')
    else:
        form = CommentForm()
    return render(request, 'ideas/comment_idea.html', {'form': form, 'idea': idea})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully!')
    return redirect('idea_list')
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful! Welcome to our community!')
            return redirect('idea_list')
        else:
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
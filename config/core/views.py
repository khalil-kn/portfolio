from django.shortcuts import render, get_object_or_404,redirect 
from .models import Project
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages
import time



def home(request):
    projects = Project.objects.all().order_by('-created_at')[:3]

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.cleaned_data.get('honeypot'):
        # silently ignore bot
            return redirect('/#Contact') 

        # Anti-spam cooldown
        last_submission = request.session.get('last_submission_time')

        if last_submission and time.time() - last_submission < 10:
            messages.error(request, "Please wait before sending another message.")
            return redirect('/#Contact')

        if form.is_valid():
            form.save()

            request.session['last_submission_time'] = time.time()

            messages.success(request, "Message sent successfully!")
            return redirect('/#Contact')

        else:
            messages.error(request, "Please correct the errors below.")

    else:
        form = ContactForm()

    return render(request, 'core/home.html', {
        'projects': projects,
        'form': form
    })

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    return render(request, 'core/project_detail.html', {'project': project})

def projects_list(request):
    tag = request.GET.get("tag")

    projects = Project.objects.all()

    if tag:
        projects = projects.filter(tags__name=tag)

    return render(request, "core/projects.html", {
        "projects": projects,
        "active_tag": tag
    })

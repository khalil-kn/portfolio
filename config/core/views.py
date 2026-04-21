from django.shortcuts import render, get_object_or_404,redirect 
from .models import Project


def home(request):
    projects = Project.objects.all().order_by('-created_at')[:3]
    return render(request, 'core/home.html', {'projects': projects})


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




from .forms import ContactForm

def home(request):
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # refresh page after submit

    return render(request, "core/home.html", {
        "form": form
    })
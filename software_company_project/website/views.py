from django.http import HttpResponse
from django.shortcuts import redirect, render

from website import models

# Create your views here.
def home(req):
    heading = models.Heading.objects.all()
    feature = models.Feature.objects.all()
    about = models.About.objects.all()
    services = models.ServicesHomePageModel.objects.all()
    serviceTab = models.ServiceTab.objects.all()
    challenge = models.Challenge.objects.all()
    partners = models.Partners.objects.all()
    partnersTwo = models.Partners.objects.all()
    solutions = models.Solutions.objects.all()
    obj = {
            "heading":heading,
            "feature":feature,
            "about":about,
            "services":services,
            "serviceTab":serviceTab,
            "challenge":challenge,
            "partners":partners,
            "partnersTwo":partnersTwo,
            "solutions":solutions,
        }
    return render(req,"index.html",obj)

def about(req):
    return render(req,"about.html")

def services(req):
    return render(req,"services.html")

def blog(req):
    return render(req,"blog.html")

def contact(req):
    return render(req,"contact.html")

def save_form(req):
    user = models.Contact(
        user_name = req.POST['user_name'],
        user_phone_number = req.POST['user_phone_number'],
        user_email = req.POST['user_email'],
        user_msg_subject = req.POST['user_msg_subject'],
        user_message = req.POST['user_message']
    )
    user.save()
    return redirect('/')
    # return HttpResponse("data received")
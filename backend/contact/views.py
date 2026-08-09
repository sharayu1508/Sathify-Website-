from django.shortcuts import render
from .models import ContactMessage


def contact(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )

        return render(request, "contact/index5.html", {
            "success": "Your message has been sent successfully!"
        })

    return render(request, "contact/index5.html")
def about(request):
    return render(request, 'contact/about.html')
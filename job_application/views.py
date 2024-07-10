from django.shortcuts import render
from .forms import ApplicationForm
from .models import FormDatabase
from django.contrib import messages
from data_check import get_data


def index(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            firstName = form.cleaned_data['first_name']
            lastName = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            date = form.cleaned_data['date']
            occupation = form.cleaned_data['occupation']

            emailList = get_data()
            if email in emailList:
                messages.success(request, f"{firstName}, your data was not submitted as this "
                                 f"email already exists in a previous application!")
            else:
                FormDatabase.objects.create(firstName=firstName, lastName=lastName,
                                            email=email, date=date, occupation=occupation)
                messages.success(request, f"{firstName}, your form was submitted successfully!")

    return render(request, 'index.html')

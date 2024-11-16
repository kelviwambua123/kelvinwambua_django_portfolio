from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm 

# Render the contact page
def contact(request):
    return render(request, 'contact.html') #homepage

# Handle the contact form submission
def contact_form(request):
    if request.method == 'POST':  # Fixed case sensitivity
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Ensure 'success' is defined in your URLs
    else:
        form = ContactForm()  # Moved to else block
    
    return render(request, 'contact_form.html', {'form': form})

# Render the success page
def success(request):  # Fixed indentation
    return render(request, 'success.html')

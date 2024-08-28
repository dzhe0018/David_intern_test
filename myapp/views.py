from django.shortcuts import render, redirect
from .forms import EntryForm

def entry_form_view(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a new URL after successful form submission
    else:
        form = EntryForm()

    return render(request, 'myapp/entry_form.html', {'form': form})
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def success_view(request):
    return render(request, 'myapp/success.html')

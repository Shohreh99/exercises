from django.shortcuts import render
from .forms import MyForm


def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # ... process the data further
    else:
        form = MyForm()

    return render(request, 'exercises/my_template.html', {'form': form})



from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .forms import PersonForm

@login_required
def person_list(request):
    persons = Person.objects.all()
    return render(request, 'list_person.html', {'persons': persons})


@login_required
def person_new(request):
    form = PersonForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'new_person.html', {'form': form})


@login_required
def person_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'new_person.html', {'form': form})


@login_required
def person_delete(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)
    if request.method == 'POST':
        person.delete()
        return redirect('person_list')
    return render(request, 'delete_person.html', {'person': person})
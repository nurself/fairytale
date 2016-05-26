from .forms import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

def suit_list(request):
    suits = Suit.objects.order_by('type')
    types = SuitType.objects.all()
    branches = Branch.objects.all()
    return render(request, 'world/suit_list.html', {'suits': suits, 'types': types, 'branches': branches})

def suit_detail(request, pk):
    suit = get_object_or_404(Suit, pk=pk)
    return render(request, 'world/suit_detail.html', {'suit': suit})

def suit_new(request):
    if request.method == "POST":
        form = SuitForm(request.POST)
        if form.is_valid():
            suit = form.save(commit=False)
            suit.save()
            return redirect('world.views.suit_detail', pk=suit.pk)
    else:
        form = SuitForm()
    return render(request, 'world/suit_edit.html', {'form': form})


def suit_edit(request, pk):
    suit = get_object_or_404(Suit, pk=pk)
    if request.method == "POST":
        form = SuitForm(request.POST, instance=suit)
        if form.is_valid():
            suit = form.save(commit=False)
            suit.save()
            return redirect('world.views.suit_detail', pk=suit.pk)
    else:
        form = SuitForm(instance=suit)
    return render(request, 'world/suit_edit.html', {'form': form})


def agreement_list(request):
    agreements = Agreement.objects.order_by('-published_date')
    return render(request, 'world/agreement_list.html', {'agreements': agreements})


def agreement_detail(request, pk):
    agreement = get_object_or_404(Agreement, pk=pk)
    return render(request, 'world/agreement_detail.html', {'agreement': agreement})
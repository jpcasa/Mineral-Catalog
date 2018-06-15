from random import randint

from django.shortcuts import render, get_object_or_404
from django.forms.models import model_to_dict
from django.db import IntegrityError

from .models import Mineral
import json

# Create your views here.
def make_mineral_dict(mineral):
    """Creates a Dict to store JSON mineral data"""
    fields = {
        'name': None,
        'image filename': None,
        'image caption': None,
        'category': None,
        'formula': None,
        'strunz classification': None,
        'crystal system': None,
        'unit cell': None,
        'color': None,
        'crystal symmetry': None,
        'cleavage': None,
        'mohs scale hardness': None,
        'luster': None,
        'streak': None,
        'diaphaneity': None,
        'optical properties': None,
        'refractive index': None,
        'crystal habit': None,
        'specific gravity': None
    }
    for key, value in mineral.items():
        fields[key] = value
    return fields


def add_minerals_to_db():
    """Adds the minerals to the database"""
    with open('minerals.json', encoding='utf-8') as file:
        minerals = json.load(file)
        for mineral in minerals:
            try:
                fields = make_mineral_dict(mineral)
                Mineral(
                    name=fields['name'],
                    image_filename=fields['image filename'],
                    image_caption=fields['image caption'],
                    category=fields['category'],
                    formula=fields['formula'],
                    strunz_classification=fields['strunz classification'],
                    crystal_system=fields['crystal system'],
                    unit_cell=fields['unit cell'],
                    color=fields['color'],
                    crystal_symmetry=fields['crystal symmetry'],
                    cleavage=fields['cleavage'],
                    mohs_scale_hardness=fields['mohs scale hardness'],
                    luster=fields['luster'],
                    streak=fields['streak'],
                    diaphaneity=fields['diaphaneity'],
                    optical_properties=fields['optical properties'],
                    refractive_index=fields['refractive index'],
                    crystal_habit=fields['crystal habit'],
                    specific_gravity=fields['specific gravity']
                ).save()
            except IntegrityError:
                pass


def get_mineral_fields(mineral):
    """Returns the list of fields and values for each mineral"""
    fields = {}
    options = Mineral._meta
    min_fields = []
    ignore = ['id','name','image_caption','image_filename','category','formula']

    for field in sorted(options.concrete_fields + options.many_to_many):
        fields[field.name] = field

    for f in fields:
        val = getattr(mineral, f)
        if val != '' and f not in ignore:
            min_fields.append({
                'name': f,
                'value': val
            })

    return min_fields


def get_random_mineral_id():
    minerals = Mineral.objects.all()
    return randint(0, minerals.count())


def mineral_list(request):
    minerals = Mineral.objects.all()
    random_mineral = get_random_mineral_id()
    if minerals.count() == 0:
        add_minerals_to_db()
    return render(request, 'minerals/mineral_list.html', {
        'minerals': minerals,
        'random_mineral': random_mineral
    })


def mineral_detail(request, pk):
    mineral = get_object_or_404(Mineral, pk=pk)
    min_fields = get_mineral_fields(mineral)
    random_mineral = get_random_mineral_id()
    return render(request, 'minerals/mineral_detail.html', {
        'mineral': mineral,
        'fields': min_fields,
        'random_mineral': random_mineral
    })

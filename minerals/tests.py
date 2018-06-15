from django.urls import reverse
from django.test import TestCase

from .models import Mineral

# Create your tests here.
class MineralModelTests(TestCase):
    def test_mineral_creation(self):
        mineral = Mineral.objects.create(
            name='Something',
            image_filename='Something',
            image_caption='Something',
            category='Something',
            formula='Something',
            strunz_classification='Something',
            color='Something',
            crystal_system='Something',
            unit_cell='Something',
            crystal_symmetry='Something',
            cleavage='Something',
            mohs_scale_hardness='Something',
            luster='Something',
            streak='Something',
            diaphaneity='Something',
            optical_properties='Something',
            group='Something',
            refractive_index='Something',
            crystal_habit='Something',
            specific_gravity='Something',
        )
        self.assertIn(mineral, Mineral.objects.all())


class MineralViewsTests(TestCase):
    def setUp(self):
        self.mineral = Mineral.objects.create(
            name='Something',
            image_filename='Something',
            image_caption='Something',
            category='Something',
            formula='Something',
            strunz_classification='Something',
            color='Something',
            crystal_system='Something',
            unit_cell='Something',
            crystal_symmetry='Something',
            cleavage='Something',
            mohs_scale_hardness='Something',
            luster='Something',
            streak='Something',
            diaphaneity='Something',
            optical_properties='Something',
            group='Something',
            refractive_index='Something',
            crystal_habit='Something',
            specific_gravity='Something',
        )
        self.mineral2 = Mineral.objects.create(
            name='Something 2',
            image_filename='Something 2',
            image_caption='Something 2',
            category='Something 2',
            formula='Something 2',
            strunz_classification='Something 2',
            color='Something 2',
            crystal_system='Something 2',
            unit_cell='Something 2',
            crystal_symmetry='Something 2',
            cleavage='Something 2',
            mohs_scale_hardness='Something 2',
            luster='Something 2',
            streak='Something 2',
            diaphaneity='Something 2',
            optical_properties='Something 2',
            group='Something 2',
            refractive_index='Something 2',
            crystal_habit='Something 2',
            specific_gravity='Something 2',
        )

    def test_mineral_list_view(self):
        resp = self.client.get(reverse('minerals:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertIn(self.mineral2, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/mineral_list.html')
        self.assertContains(resp, self.mineral.name)

    def test_course_detail_view(self):
        resp = self.client.get(reverse('minerals:detail',
                                       kwargs={'pk': self.mineral.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral, resp.context['mineral'])
        self.assertTemplateUsed(resp, 'minerals/mineral_detail.html')

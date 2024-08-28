from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from .models import Entry

class EntryFormTests(TestCase):
    def test_form_submission(self):
        response = self.client.post(reverse('entry_form'), {'name': 'John Doe', 'age': '30'})
        self.assertEqual(response.status_code, 302)  # Check for redirection
        self.assertRedirects(response, reverse('success'))  # Check for redirection to success page
        self.assertTrue(Entry.objects.filter(name='John Doe', age=30).exists())  # Check if data is saved

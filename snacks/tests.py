  
from django.test import TestCase 
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Snack

class SnacksCRUDTests(TestCase):
    
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'amarh',
            password = '112233ni'
        )
        self.snack = Snack.objects.create(
            title = 'kabab',
            description  = 'mmm',
            purchaser = self.user
        )


    def test_snack_list_view(self):
        url = reverse('snack_list')
        actual_status_code = self.client.get(url).status_code
        self.assertEqual(actual_status_code, 200)

    def test_snack_details_view(self):
        response = self.client.get(reverse('snack_detail', args='1'))
        self.assertEqual(response.status_code, 200)

    def test_snack_update_view(self):
        response = self.client.post(reverse('snack_update', args='1'), {
            'title':'mansaf' ,
        })
        self.assertContains(response, 'mansaf')
        
   
    def test_snack_create_view(self):
        response = self.client.post(reverse("snack_create"),
            {
                "title": "apple",
                "description": "love it",
                "purchaser": self.user
            })

     
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'apple')
        self.assertContains(response, 'love it')
        self.assertContains(response, 'amarh')


    def test_snack_delete_view(self):
        response = self.client.get(reverse("snack_delete", args="1"))
        self.assertEqual(response.status_code, 200)

    def test_queris(self):
      self.assertNumQueries(2)  
      self.assertEqual(Snack.objects.get(pk=1).title,'kabab')  
   
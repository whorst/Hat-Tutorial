from django.test import TestCase

from models import Person
from forms import valid_phone_number

class PersonTest(TestCase):


    def test_invalid_phone_number_is_identified(self):
        '''
        Will test that an entry of an invalid phone number into the respective text box will return False.
        '''

        self.assertEqual(valid_phone_number('73-8704'), False)


    def test_valid_phone_number_is_identified(self):
        '''
        Will test that an entry of an valid phone number into the respective text box will return True.
        '''

        self.assertEqual(valid_phone_number('734-111-8704'), True)

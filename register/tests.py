from django.test import TestCase

from models import Person


class PersonTest(TestCase):

    def test_invalid_phone_number_is_identified(self):
        '''
        Will test that there an entry of an invalid phone number into the respective text box will return False.
        '''

        person = Person(phone_number = '734-854-8704')
        self.assertEqual(person.valid_phone_number(), True)




def create_person(phone_number_test):
    return Person.objects.create(phone_number = phone_number_test)

import datetime
from django.http import response

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Question
# Create your tests here.

class QuestionModelTests(TestCase):
    
    def test_was_published_recently_with_future_questions(self):
        """ was_publiched_recently returns False for questions whose pub_date is in the future"""
        time =  timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text =  "Quien es el mejor COurse Director de Platzi",pub_date = time)
        self.assertIs(future_question.was_published_recently(), False)

def create_question(question_text, days):
    '''
     Create a question with the given "question_Text, and publisehd the given number of days offset to now
     (negative for questions published in the past, positive questions that have yet to be published
    '''
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):

    def test_no_question(self):
        """If no question exist, an appropiate message is displayed"""
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are avaible.")
        self.assertQuerysetEqual(response.context["latest_question_list"],[])

    def test_future_question(self):
        '''
        Question with a pub_date in the future aren't displayed on the index page
        '''
        create_question("Future question", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are avaible.")
        self.assertQuerysetEqual(response.context["latest_question_list"],[])


    def test_past_question(self):
        '''
        Questions qieht a pub_date in the past are displayed on the index
        '''
        question = create_question("Past question", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context["latest_question_list"],[question])



    def test_questions_with_future_pub_date(self):
        """
            Questions with a pub_date greater than the current date should not appear in the Index View.
        """
        Question(question_text='Present Question', pub_date=timezone.now()).save()
        Question(question_text='Future Question', pub_date=timezone.now() + datetime.timedelta(days=30)).save()

        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Present Question")
        self.assertNotContains(response, "Future Question")
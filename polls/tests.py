import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question


class QuestionModelTests(TestCase):
def  test_was_published_recently_with_old_question ( self ): 

    time  =  timezone . ahora ()  -  fecha y hora . timedelta ( días = 1 ,  segundos = 1 ) 
    old_question  =  Question ( pub_date = time ) 
    self . afirmarIs ( antigua_pregunta . fue_publicada_recientemente(),  Falso ) 

def  test_was_published_recently_with_recent_question ( self ): 
   
    Time  =  timezone . ahora ()  -  fecha y hora . timedelta ( horas = 23 ,  minutos = 59 ,  segundos = 59 ) 
    Recent_question  =  Question ( pub_date = time ) 
    self. afirmarIs ( reciente_pregunta . was_published_recently (),  True )
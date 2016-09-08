from django.conf.urls import url
from quizapp import views
urlpatterns = [
	url(r"^$", views.start, name="start_page"),
	url(r"^quiz/([0-9]+)/$", views.quiz, name="quiz_page"),
	url(r"^quiz/([0-9]+)/question/([0-9]+)/$", views.question, name="question_page"),
	url(r"^quiz/([0-9]+)/results/$", views.results, name="results_page"),
]
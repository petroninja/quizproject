from django.shortcuts import render
from quizapp.models import Quiz

# Create your views here.
def start(request):
	context = {
		"quizzes": Quiz.objects.all(),
	}
	return render(request, "quiz/start.html", context)

def quiz(request, quiz_number):
	context = {
		"quiz": quizzes[int(quiz_number) - 1],
		"quiz_number": quiz_number,
	}
	return render(request, "quiz/quiz.html", context)

def question(request, quiz_number, question_number):
	context = {
		"quiz": quizzes[int(quiz_number) - 1],
		"question_number": question_number,
	    "question": "Why do Java programmers need glasses?",
		"answer1": "Because they don’t C++",
	   	"answer2": "Because they don’t C#",
	    "answer3": "I have absolutely no clue",
	    "quiz_number": quiz_number,
	}
	return render(request, "quiz/question.html", context)

def results(request, quiz_number):
	context = {
		"quiz": quizzes[int(quiz_number) - 1],
	    "correct": 12,
	    "total": 20,
		"quiz_number": quiz_number,
	}
	return render(request, "quiz/results.html", context)
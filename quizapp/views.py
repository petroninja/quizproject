from django.shortcuts import render

quizzes = [
	{
		"quiz_number": 1,
   	    "name": "Programmerarhumor",
	    "description": "Fattar du eller är du en noob?"	
	},
	{
		"quiz_number": 2,
   	   	"name": "Största fotbollslagen",
	   	"description": "Kan du dina lag?"
	},
	{
		"quiz_number": 3,
   		"name": "Klassiska böcker",
	   	"description": "Hur bra kan du dina klassiker?"
	},
]

# Create your views here.
def start(request):
	context = {
		"quizzes": quizzes,
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
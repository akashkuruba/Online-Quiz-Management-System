from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Quiz, Attempt

def home(request):
    return render(request, "home.html", {"quizzes": Quiz.objects.filter(is_published=True)})

def register(request):
    form = UserCreationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        login(request, form.save())
        return redirect("home")
    return render(request, "registration/register.html", {"form": form})

@login_required
def take_quiz(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk, is_published=True)
    questions = quiz.questions.prefetch_related("choices")
    if request.method == "POST":
        score = 0
        for q in questions:
            picked = request.POST.get(f"q{q.id}")
            if picked and q.choices.filter(pk=picked, is_correct=True).exists():
                score += 1
        attempt = Attempt.objects.create(user=request.user, quiz=quiz, score=score, total=questions.count())
        return redirect("result", pk=attempt.pk)
    return render(request, "take.html", {"quiz": quiz, "questions": questions})

@login_required
def result(request, pk):
    attempt = get_object_or_404(Attempt, pk=pk, user=request.user)
    return render(request, "result.html", {"attempt": attempt})

@login_required
def my_results(request):
    return render(request, "my_results.html", {"attempts": Attempt.objects.filter(user=request.user)})

def leaderboard(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    best = {}
    for a in Attempt.objects.filter(quiz=quiz).select_related("user"):
        if a.user_id not in best or a.percent > best[a.user_id].percent:
            best[a.user_id] = a
    rows = sorted(best.values(), key=lambda a: -a.percent)[:20]
    return render(request, "leaderboard.html", {"quiz": quiz, "rows": rows})

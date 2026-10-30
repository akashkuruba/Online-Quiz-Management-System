from django.conf import settings
from django.db import models

class Quiz(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    time_limit_minutes = models.PositiveIntegerField(default=10)
    pass_percent = models.PositiveIntegerField(default=50)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "quizzes"
        ordering = ["-created_at"]
    def __str__(self): return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name="questions", on_delete=models.CASCADE)
    text = models.TextField()
    order = models.PositiveIntegerField(default=0)
    class Meta: ordering = ["order", "id"]
    def __str__(self): return self.text[:60]

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name="choices", on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    def __str__(self): return self.text

class Attempt(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    taken_at = models.DateTimeField(auto_now_add=True)
    class Meta: ordering = ["-taken_at"]
    @property
    def percent(self): return round(100 * self.score / self.total) if self.total else 0
    @property
    def passed(self): return self.percent >= self.quiz.pass_percent

from django.contrib import admin
from .models import Quiz, Question, Choice, Attempt

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("text", "quiz", "order")
    list_filter = ("quiz",)
    inlines = [ChoiceInline]

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 0
    show_change_link = True

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ("title", "time_limit_minutes", "pass_percent", "is_published", "created_at")
    list_filter = ("is_published",)
    search_fields = ("title",)
    inlines = [QuestionInline]

@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    list_display = ("user", "quiz", "score", "total", "taken_at")
    list_filter = ("quiz",)

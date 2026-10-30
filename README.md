# QuizHub – Online Quiz Management System (Django)

## Run on any laptop (needs Python 3.10+)
    python -m venv venv
    venv\Scripts\activate          (Windows)   |   source venv/bin/activate   (Mac/Linux)
    pip install -r requirements.txt
    python manage.py makemigrations quiz
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver

Open http://127.0.0.1:8000/

## Use it
- Admin/teacher: log in at /admin/ → add a Quiz, then questions with choices (tick the correct one).
- Students: Register → take quizzes (timed, auto-submit) → see score, history, leaderboard.
- Share on your Wi-Fi: `python manage.py runserver 0.0.0.0:8000`, then open http://<your-laptop-IP>:8000
- Before public hosting: set DEBUG=False, a new SECRET_KEY and ALLOWED_HOSTS in quizsite/settings.py.

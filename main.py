from datetime import date
from user import User
from task import Task

today = date.today()

user = User("Irlan", "Chefe", "gerência")
user.create_user()
user.show_users()
user.edit_user()
user.show_users()
task = Task(
    "taskarefa de teste", "Tarefa para calcular horas", 
    date(2025, 7, 30), user, "backLog", "Normal"
)
task.create_task()
task.show_tasks()

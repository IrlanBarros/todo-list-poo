from datetime import date
today = date.today()

tasks_list = []

class Task:
    def __init__(
        self, title, description, completion_date, 
        responsible, status, priority
    ):
        self.title = title
        self.description = description
        self.criation_date = today
        self.completion_date = completion_date
        self.responsible = responsible
        self.status = status
        self.priority = priority
        self.id = len(tasks_list) + 1
        
    def create_task(self):
        tasks_list.append(self)
        
    def edit_task(self):
        self.edited = False
        
        for task in tasks_list:
            if self.id == task.id:
                self.edited = True
        
        if not (self.edited):
            print(f"{task.name} não é um usuário válido")
            return
           
        self.title = input("Digite o novo título da tarefa: ") 
        self.description = input("Digite a nova descrição da tarefa: ")
        print(f"Tarefa: {task.title} editada com sucesso!")
        
    def delete_task(self):
        self.deleted = False
        
        for task in tasks_list:
            if self.id == task.id:
                self.deleted = True
        
        if not (self.deleted):
            print(f"{task.title} não é uma tarefa cadastrada")
            return
            
        tasks_list.remove(self)
        print(f"Tarefa: {task.title} deletada com sucesso!")
        
    def show_task(self):
        print(
            f"Título: {self.title} || Data de entrega: {self.completion_date} ||"
            + f" Responsável: {self.responsible.name}"
        )
        
    def show_tasks(self):
        if (len(tasks_list) == 0):
            print("Não existem tarefas no momento")
            return
        for task in tasks_list:
            print(
                f"Id: {task.id} || Título: {task.title} ||" 
                + f" Data de entrega: {self.completion_date} ||" 
                + f" Responsável: {self.responsible.name}"
            )
    
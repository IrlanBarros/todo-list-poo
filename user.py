users_list = []

class User:
    def __init__(self, name, role, sector):
        self.name = name
        self.role = role
        self.sector = sector
        self.id = len(users_list) + 1
        
    def create_user(self):
        users_list.append(self)
        
    def edit_user(self):
        self.edited = False
        
        for user in users_list:
            if self.id == user.id:
                self.edited = True
        
        if not (self.edited):
            print(f"{user.name} não é um usuário válido")
            return
            
        self.name = input("Digite o novo nome do usuário: ")
        self.role = input("Digite o novo cargo do usuário: ")
        self.sector = input("Digite o novo setor do usuário: ")
        print(f"Usuário: {user.name} editado com sucesso!")
      
    def delete_user(self):
        self.deleted = False
        
        for user in users_list:
            if self.id == user.id:
                self.deleted = True
        
        if not (self.deleted):
            print(f"{user.name} não é um usuário válido")
            return
            
        users_list.remove(self)
        print(f"Usuário: {user.name} deletado com sucesso!")
      
    def show_user(self, user):
        print(f"Nome: {user.name} || Cargo: {user.role}")
        
    def show_users(self):
        if (len(users_list) == 0):
            print("Não existem usuários")
            return
        for user in users_list:
            print(
                f"Id: {user.id} || Nome: {user.name} ||" 
                + f"Cargo: {user.role} || Setor: {user.sector}"
            )

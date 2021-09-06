class User:
    id = 0

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.id = User.generate_id()

    @staticmethod
    def generate_id():
        User.id += 1
        return User.id

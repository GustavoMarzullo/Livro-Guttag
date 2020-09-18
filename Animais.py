class animal(object):
    def __init__(self,nome,sexo,idade):
        self.nome= nome
        self.sexo=sexo
        self.idade=idade
    def get_idade(self):
        return self.idade
    def get_nome(self):
        return self.nome
    def get_sexo(self):
         return self.sexo
    def set_idade(self,novaidade):
        self.idade= novaidade
    def set_nome(self,novonome):
        self.nome=novonome
    def set_sexo(self,novosexo):
        self.nome=novosexo
    def __str__(self):
        return "animal:"+str(self.name)+":"+str(self.age)
class cachorro(animal):
    id=1
    self.rid=cachorro.tag
    cachorro.tag+=1
    def fala(self):
        print('au au')
    

    


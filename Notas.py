class agricolas(object):
    def __init__(self,idade,faculdade,curso,apelido,orientacao_sexual):
        self.idade=idade
        self.faculdade=faculdade
        self.curso=curso
        self.apelido=apelido
        self.orientacao_sexual=orientacao_sexual
    def qual_idade(self):
        return self.idade
    def qual_faculdade(self):
        return self.faculdade
    def qual_curso(self):
        return self.curso
    def qual_apelido(self):
        return self.apelido
    def qual_orientacao_sexual(self):
        return self.orientacao_sexual
    def pode_pegar(self,outro):
        if self.orientacao_sexual=='Bi'or self.orientacao_sexual=='Gay' :
            if outro.orientacao_sexual=='hétero':
                print('Não')
            else:
                print('Sim')
        else:
            print('Não')



Lucas=agricolas(22,'UFRJ','Química','Cracudo Otacu','Bi')
Igor=agricolas(22,'UFRJ','Filosofia','Igor 44','Hétero')
Luis=agricolas(21,'UFF','Química','JN','Bi')
Kevin=agricolas(21,'UniRio','BSI','Kevinho','Bi')
Leonardo=agricolas(20,'UFRRJ','Eng. Química','LeozinhoFutsal','"hétero"')
Natanael=agricolas(20,'Casa do Senhor','Louvor','Omena','hétero')
Mateus=agricolas(20,'UFRJ','Eng. Química','Rato','Bi')
Guilherme=agricolas(20,'UFF','Farmácia','Biscoito','hétero')
Gustavo=agricolas(20,'UERJ','Eng. Química','Marzullo','hétero')


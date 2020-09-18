class notas(object):
    def __init__(self):
        self.estudantes=[]
        self.notas={}
        self.isSorted=True
    def addEstudantes(self,estudante):
        if estudante in self.estudantes:
            raise ValueError('Estudante Duplicado')
        self.estudantes.append(estudante)
        self.notas[estudante.getIdNum()]=()
        self.isSorted=False
    def addNota(self,estudante,nota):
        try:
            self.notas[estudante.getIdNum()].append(nota)
        except:
            raise ValueError('Estudante não cadastrado.')
    def verNota(self, estudante):
        try:
            return self.notas[estudante.getIdNum()][:]
        except:
            raise ValueError('Estudante não cadastrado.')
    def verEstudantes(self):
        if not self.isSorted:
            self.estudantes.sort()
            self.isSorted = True
        return self.estudantes[:]

def gradeReport(course):
    for s in course.verEstudantes():
        tot=0.0
        numGrades=0
        for g in course.getgrades(s):
            tot+=g
            numgrades+=1
        try:
            average = tot/numGrades
            report = report + '\n'\
            + str(s) + '\'s mean grade is ' + str(average)
        except ZeroDivisionError:
            report = report + '\n'\
            + str(s) + ' has no grades'
    return report

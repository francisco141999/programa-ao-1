class aluno():

 def __init__(self, nome, numero_aluno):
        
        self.nome = nome
        self.numero_aluno = numero_aluno 

 def __str__(self):
     return "O nome do aluno é {} e o numero de aluno é {}".format(self.numero,(self.nome).title())

 def __igual__(self):
 self.numero_aluno == self.numero_aluno
    return False

if __name__ =="__main__":

    A1 = aluno(1,"Francisco")
    print (A1)
    A2 = aluno(2,"Ricardo")
    print(A2)

class turma():
    def __init__(self, nome,ano,lista_alunos,total_alunos):
        
        self.nome = nome
        self.ano = ano 
        self.lista_alunos =[]
        self.total_alunos = 0 
    

    def __verificao_se_existe(self):
        for i in range (self.total_alunos)
          if self.lista_alunos[i]= 
           return False
         return True  
 
    
     def _insere_aluno(self,aluno):
        if self.__verificao_se_existe       
            self.lista_alunos.append(aluno)
            self.total_alunos += 1 
            

            



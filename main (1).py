class Estado: 
    def __init__(self, sigla, nome): 
        self.sigla = sigla 
        self.nome = nome 
        self.proximo = None 

class Hash:  #[EXIGÊNCIA DE CÓDIGO 5 de 7];
    def __init__(self): 
        self.tamanho = 10 
        self.tabela = [None] * self.tamanho #[EXIGÊNCIA DE CÓDIGO 1 de 7]

    def funcao_hash(self, sigla): 
        if sigla == "DF": 
            return 7 
        else: 
            char1_ascii = ord(sigla[0]) 
            char2_ascii = ord(sigla[1]) 
            return (char1_ascii + char2_ascii) % self.tamanho 
            
    def inserir(self, estado): #[EXIGÊNCIA DE CÓDIGO 2 de 7];
        posicao = self.funcao_hash(estado.sigla) 
        if self.tabela[posicao] is None: 
            self.tabela[posicao] = estado 
        else: #[EXIGÊNCIA DE CÓDIGO 3 de 7];
            estado.proximo = self.tabela[posicao] 
            self.tabela[posicao] = estado 
             
    def imprimir(self): #[EXIGÊNCIA DE CÓDIGO 4 de 7];
        for i, estado in enumerate(self.tabela): 
            estados_na_posicao = [] 
            while estado: 
                estados_na_posicao.append(estado.sigla) 
                estado = estado.proximo 
            estados_na_posicao.append("None")   

            print(f"{i}: {'->'.join(estados_na_posicao)}") 

estados = [ #[EXIGÊNCIA DE CÓDIGO 6 de 7];
    Estado("AC", "Acre"), 
    Estado("AL", "Alagoas"), 
    Estado("AP", "Amapa"), 
    Estado("AM", "Amazonas"), 
    Estado("BA", "Bahia"), 
    Estado("CE", "Ceara"), 
    Estado("ES", "Espirito Santo"), 
    Estado("GO", "Goias"), 
    Estado("MA", "Maranhão"), 
    Estado("MT", "Mato Grosso"), 
    Estado("MS", "Mato Grosso do Sul"), 
    Estado("MG", "Minas Gerais"), 
    Estado("PA", "Para"), 
    Estado("PB", "Paraiba"), 
    Estado("PR", "Parana"), 
    Estado("PE", "Pernambuco"), 
    Estado("PI", "Piaui"), 
    Estado("RJ", "Rio de Janeiro"), 
    Estado("RN", "Rio Grande do Norte"), 
    Estado("RS", "Rio Grande do Sul"), 
    Estado("RO", "Rondonia"), 
    Estado("RR", "Roraima"), 
    Estado("SC", "Santa Catarina"), 
    Estado("SP", "Sao Paulo"), 
    Estado("SE", "Sergipe"), 
    Estado("TO", "Tocantins"), 
    Estado("DF", "Distrito Federal") ] 
    
tabela_hash = Hash()  #instanciando Hash vazio (None)
tabela_hash.imprimir() #[EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 3];
print("\n") 

for i in range(len(estados)): 
    tabela_hash.inserir(estados[i]) #inserindo estados no hash. [EXIGÊNCIA DE CÓDIGO 7 de 7];
    
#imprimindo a tabela hash sem o estado fictício 
tabela_hash.imprimir() #[EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 3]; 
print("\n") 

estado_ficticio = Estado("RA", "Robson Augusto dos Santos") #declarando estado ficticio
tabela_hash.inserir(estado_ficticio) #inserindo estado ficticio
tabela_hash.imprimir() #[EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 3];
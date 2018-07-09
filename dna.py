import numpy as np

class DNA:
    def __init__(self,INFO,genes = None):
        self.maxforce = 5
        self.info = INFO
        if genes:
            self.genes = genes
        else:
            self.genes = []
            for i in range(0,self.info["maxcount"]):
                temp = np.random.rand()*2*np.pi
                self.genes.append( self.maxforce*np.array([np.cos(temp), np.sin(temp)]) )

    def crossover(self,partner):
        newgenes = []
        midpoint = np.random.randint(len(self.genes))
        for i in range(0 , len(self.genes)):
            if i > midpoint:
                newgenes.append(self.genes[i])
            else:
                newgenes.append(partner.genes[i])

        return DNA(INFO = self.info, genes = newgenes)
   
    def mutation(self):
        for i in range(0,len(self.genes)):
            if np.random.rand() < 0.01:
                temp = np.random.rand()*2*np.pi   
                self.genes[i] = self.maxforce*np.array([np.cos(temp), np.sin(temp)])

            
            

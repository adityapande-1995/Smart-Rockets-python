import numpy as np
import rocket as R

class Population:
    def __init__(self,INFO):
        self.info = INFO
        self.popsize = 10
        self.rockets = [R.Rocket(self.info) for i in range(0,self.popsize)]       
        self.matingpool = []

    def evaluate(self):
        maxfit = 0
        for i in range(0,self.popsize):
            self.rockets[i].calcFitness()
            if self.rockets[i].fitness > maxfit:
                maxfit = self.rockets[i].fitness
        
        for i in range(0,self.popsize):
            self.rockets[i].fitness /= maxfit
        
        self.matingpool = []
        for i in range(0,self.popsize):
            n = int(self.rockets[i].fitness*100)
            for j in range(0,n):
                self.matingpool.append(self.rockets[i])

        print("Maximum fitness: ", maxfit, "\n")
        # for roc in self.rockets:
        #     if roc.crashed:
        #         print("Crashed at :",roc.pos, " type: ",roc.crash_type)

    def selection(self):
        newRockets = []
        for i in range(0,len(self.rockets)):
            parentA = self.matingpool[ np.random.randint(len(self.matingpool)) ].dna
            parentB = self.matingpool[ np.random.randint(len(self.matingpool)) ].dna
            child = parentA.crossover(parentB)
            child.mutation()
            newRockets.append(R.Rocket(self.info, dna = child))

        self.rockets = newRockets
  
    def run(self):
        for roc in self.rockets:
            roc.update()
            roc.show()
            


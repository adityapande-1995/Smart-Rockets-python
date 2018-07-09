import pygame
import numpy as np
import dna as D

class Rocket:
    def __init__(self, INFO, dna=None):
        self.info = INFO
        self.trail = [ np.random.rand(2) for i in range(0,10) ]
        self.pos = np.array([ self.info["width"]/2, self.info["height"] - 50 ]) # position of centre
        #self.trail.append(self.pos); del self.trail[0]

        angle = (np.random.rand()*2 - 1)*np.pi/2    # -pi/4 to pi/4
        self.vel = [np.cos(angle), np.sin(angle)]
        self.acc = np.random.rand(2)*2 -1

        self.completed = False
        self.crashed = False

        if dna:
            self.dna = dna
        else:
            self.dna = D.DNA(self.info)

    def applyForce(self,force):
        self.acc += force

    def calcFitness(self):
        d = np.sqrt( (self.pos[0] - self.info["target"][0])**2 + (self.pos[1] - self.info["target"][1])**2 )
        self.fitness = map(d, 0, self.info["width"],self.info["width"], 0)
        if self.completed:
            self.fitness *= 10
        if self.crashed:
            self.fitness /= 10

    def update(self):
        d = np.sqrt( (self.pos[0] - self.info["target"][0])**2 + (self.pos[1] - self.info["target"][1])**2 )
        if d < 10:
            self.completed = True
            self.pos = np.copy(self.info["target"])
        
        rcx,rcy,rw,rh = self.info["rcx"], self.info["rcy"], self.info["rw"], self.info["rh"] 
        if (self.pos[0] > (rcx - rw/2) and self.pos[0] < (rcx + rw/2) and self.pos[1] > (rcy - rh/2) and self.pos[1] < (rcy + rh/2)):
            self.crashed = True; self.crash_type = 1
        if (self.pos[0] > self.info["width"] or self.pos[0] < 0):
            self.crashed = True ; self.crash_type = 2
        if (self.pos[1] > self.info["height"] or self.pos[1] < 0):
            self.crashed = True ; self.crash_type = 3

        self.applyForce( self.dna.genes[self.info["loopcount"]] )
        if (not self.completed and not self.crashed):
            self.vel += self.acc
            self.pos += self.vel
            #self.trail.append(self.pos)
            #del self.trail[0]
            self.acc *= 0
            self.vel = 1*normalize(self.vel)
    
    def show(self):
        rwidth, rheight = 5,20
        t1 = rotate(p = (self.pos[0] - rwidth/2, self.pos[1] - rheight/2), c = self.pos, v = self.vel) 
        t2 = rotate(p = (self.pos[0] + rwidth/2, self.pos[1] - rheight/2), c = self.pos, v = self.vel)
        t3 = rotate(p = (self.pos[0] + rwidth/2, self.pos[1] + rheight/2), c = self.pos, v = self.vel)
        t4 = rotate(p = (self.pos[0] - rwidth/2, self.pos[1] + rheight/2), c = self.pos, v = self.vel)
        pygame.draw.polygon(self.info["screen"],(255,0,0), [t1,t2,t3,t4])
        #pygame.draw.aalines(self.info["screen"],(255,255,0), False, self.trail

        


# Other functions
def rotate(p,c,v):
    v1 = normalize(v)
    x = (p[0] - c[0])*v1[0] - (p[1] - c[1])*v1[1] + c[0]
    y = (p[0] - c[0])*v1[1] + (p[1] - c[1])*v1[0] + c[1]
    return np.array([x,y])

def map(n, start1, stop1, start2, stop2):
    return ((n-start1)/(stop1-start1))*(stop2-start2)+start2
    
def normalize(v):
    return v/np.sqrt(v[0]**2 + v[1]**2)

# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 12:49:00 2018

@author: INF-322
"""

import random

modelEnd = [9,9,9,9,9,9,9,9,9,9] 
largeIndividual = 10 

num = 100 #Cantidad de individuos
generation = 1000 #Generaciones
pressure = 3 #individual>2
mutation_chance = 0.2



def individual(min, max):
    return[random.randint(min, max) for i in range(largeIndividual)]

def newPopulation():
    return [individual(0,10) for i in range(num)]

# Funcion objetivo
def functionType(individual):
    fitness = 0
    for i in range(len(individual)):
        if individual[i] == modelEnd[i]:
            fitness += 1
    return fitness

def selection_and_reproduction(population):
    evaluating = [ (functionType(i), i) for i in population]
    print("eval",evaluating)
    evaluating = [i[1] for i in sorted(evaluating)]
    print("eval",evaluating)
    population = evaluating
    selected = evaluating[(len(evaluating)-pressure):]
    for i in range(len(population)-pressure):
        pointChange = random.randint(1,largeIndividual-1)
        father = random.sample(selected, 2)
        population[i][:pointChange] = father[0][:pointChange]
        population[i][pointChange:] = father[1][pointChange:]       
    return population

def mutation(population):
    for i in range(len(population)-pressure):
        if random.random() <= mutation_chance: 
            pointChange = random.randint(1,largeIndividual-1) 
            new_val = random.randint(0,9) 
            while new_val == population[i][pointChange]:
                new_val = random.randint(0,9)
            population[i][pointChange] = new_val
    return population


# Principal
population = newPopulation()
print("\nPopulation Begin:\n%s"%(population))
population = selection_and_reproduction(population)
print("\Selection Population:\n%s"%(population))
population = mutation(population)
print("\Mutation Population:\n%s"%(population))

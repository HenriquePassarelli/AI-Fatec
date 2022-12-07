""" 
    ## requirements

    linux users - sudo apt install python3-tk
    pip3 install scipy
    Reference - https://github.com/MUZAMMILPERVAIZ/Genetic-Algorithm-Python/blob/main/8Queens-Genetic-Algorithm.py

    run - python3 vacuum_cleaner_2.py

 """
import random
import  numpy as np


POPULATION_SIZE = 10
LEN_CHROMOSOME = 8
split1 = 5
split2= 8

def create_chromosome():
    chromosome = []
    for i in range(LEN_CHROMOSOME):
        chromosome.append(random.randint(0,8))
    return chromosome


def create_population():
    population = []
    for i in range(POPULATION_SIZE):
        a = create_chromosome()
        population.append(a)
    return population


def cost(chromosome_tuple):
    return chromosome_tuple[1]


def fitness(chromosome):
        clashes = 0;
# calculate row and column clashes
# just subtract the unique length of array from total length of array
# [1,1,1,2,2,2] - [1,2] => 4 clashes
        row_col_clashes = abs(len(chromosome) - len(np.unique(chromosome)))
        clashes += row_col_clashes
# calculate diagonal clashes
        for i in range(len(chromosome)):
            for j in range(len(chromosome)):
                if ( i != j):
                    dx = abs(i-j)
                    dy = abs(chromosome[i] - chromosome[j])
                    if(dx == dy):
                        clashes += 1

        return 28 - clashes


def population_with_fitness(population):
    pop_fit = []
    for i in population:
        a = (i, fitness(i))
        pop_fit.append(a)

    return sorted(pop_fit, key=cost, reverse=True)


def selection(population):
    print(len(population[:4]))
    return population[:4]


def crossover(selection):
    cross_list = []
    for i in range(0, len(selection), 2):
        p1 = selection[i][0]
        p2 = selection[i + 1][0]

        c1 = p1[:split1] + p2[split1:split2]+ p1[split2:]
        c2 = p2[:split1] + p1[split1:split2] + p2[split2:]

        cross_list.append(p1)
        cross_list.append(p2)
        cross_list.append(c1)
        cross_list.append(c2)
    return cross_list


def mutation(crs):
    mut = []
    for a in crs:
        ind = random.randint(0, len(a) - 1)
        if a[ind] == 1:
            a[ind] = 0
        else:
            a[ind] = 1
        mut.append(a)
    return mut


def show(pop, generation):
    print()
    print('Generation no [', generation, ']', 'Best Chromosome: ', pop[0][0], 'Fitness: ', pop[0][1])
    print(80 * '-')
    for no, i in enumerate(pop):
        print('chromosome # ', no + 1, '<<<', i[0], '>>>', 'Fitness:', i[1])


Population = None

for i in range(100):
    if Population is None:
        Population = create_population()
        Population1 = population_with_fitness(Population)
    else:
        show(Population1, i)
        Population1 = selection(Population1)
        print('selection', Population1)
        Population1 = crossover(Population1)
        Population1 = mutation(Population1)
        Population1 = population_with_fitness(Population1)

        if (Population1[0][1] == 28):
            show(Population1, i)
            break
import time
import random



class Genetic:
    def __init__(self, target, population_number):
        self.gene_pool = '''abcçdefgğhıijklmnoöpqrsştuüvwxyzABCÇDEFGĞHİIJKLMNOÖPQRŞSTUÜVWXYZ '''
        self.target = target
        self.population_number = population_number
        self.target_text_length = len(target)
        self.population = []
        self.next_generation = []
        self.found = False
        self.generation_timer = 0
        self.found_text = ""

    class Member:

        def __init__(self,chromosome):
            self.chromosome = chromosome
            self.fitness = 0


    def random_gene(self):
        gene = random.choice(self.gene_pool)

        return gene

    def create_chromosome (self):
        chromosome = [self.random_gene() for i in range(self.target_text_length)]
        return chromosome

    def calculateFitness(self):
        for Member in self.population:
            Member.Fitness = 0
            for i in range(self.target_text_length):
                if Member.chromosome[i] == self.target[i]:
                    Member.Fitness += 1

            if Member.Fitness == self.target_text_length:
                self.found_text = Member.chromosome
                self.found = True

    def crossover(self):
        last_best = int((90* self.population_number)/100)
        
        self.next_generation = []
        self.next_generation.extend(self.population[last_best:])


        while True:
            if len(self.next_generation) < self.population_number:
                member1 =random.choice(self.population[last_best:]).chromosome
                member2 = random.choice(self.population[last_best:]).chromosome

                new_member = []

                for gene1, gene2 in zip(member1, member2):
                    prob =  random.random()
                    if prob < 0.47:
                        new_member.append(gene1)
                    elif prob < 0.94:
                        new_member.append(gene2)
                    else:
                        new_member.append(self.random_gene())

                
                self.next_generation.append(self.Member(new_member))
                
            else:
                break

        self.population = self.next_generation

    def main(self):
        for i in range(self.population_number):
            self.population.append(self.Member(self.create_chromosome()))

        while not self.found:
            self.calculateFitness()
            self.population = sorted(self.population, key=lambda Member: Member.Fitness)
            self.crossover()
            self.generation_timer+=1
            


        print(f"Buldun:{self.found_text}, Adım: {self.generation_timer}")

target = "Emre yildiz"
population_number = 100
go = Genetic(target,population_number)
go.main()
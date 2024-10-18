class House:
    def __init__(self,name,number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def gp_to(self,new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('такого этажа не существует')
        else:
            for new_floor in range(new_floor+1):
                if new_floor < 1:
                    continue
            print(new_floor)
    def __str__(self):
        return f'название: {self.name},количество этажей: {self.number_of_floors}'


    def __len__(self):
        return self.number_of_floors


h1 = House('дом 1',9)
h2 = House('дом 2',4)
h1.gp_to(10)
h2.gp_to(3)
print(h1.name,h1.number_of_floors)
print(h2.name,h2.number_of_floors)
print(h1)
print(h2)

print(len(h1))
print(len(h2))
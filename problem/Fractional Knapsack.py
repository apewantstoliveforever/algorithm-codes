class ItemValue:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value
        self.cost = value//weight
    def __lt__(self, other):
        return self.cost < other.cost

class FractionalKnapsack:
    iValues = []
    def Cacalute(self, name, weight, value, capacity):
        for i in range(len(name)):
            n = ItemValue(name[i], weight[i], value[i])
            self.iValues.append(n)
        self.iValues.sort(reverse = True)
        totalValue = 0
        for i in self.iValues:
            curname = i.name
            curweight = int(i.weight)
            curvalue = int(i.value)
            if capacity - curweight >= 0:
                capacity -= curweight
                totalValue += curvalue
            else:
                fraction = capacity/ curweight
                totalValue += curvalue * fraction
                capacity = int(capacity - (fraction * curweight))
                break
        return totalValue
    def print(self):
        for i in self.iValues:
            print(i.name)



f = FractionalKnapsack()
name = ['A', 'D', 'C', 'F']
weight = [10, 40, 20, 30]
value = [60, 40, 100, 120]
print(f.Cacalute(name, weight, value, 50))
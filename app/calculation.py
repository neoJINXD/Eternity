__note__ = '''
t = Calculation()
t.sd([1, 4, 7, 2, 6])
'''

class Calculation:
    def __init__(self):
        self.values = []

    def dump(self):
        print(self.values)

    def mad(self, *arg):
        sum = 0        
        self.values = list(arg)
        for e in self.values:
            sum += e
        size = len(self.values)
        mean = sum/size
        distance = 0
        for e in self.values:
            distance += (mean-e, e-mean)[e-mean>0]
        result = distance/size
        #print(result)
        return result

    def std(self, *arg):
        sum = 0        
        self.values = list(arg)
        for e in self.values:
            sum += e
        size = len(self.values)
        mean = sum/size
        distance_square = 0
        for e in self.values:
            distance_square += (e-mean)*(e-mean)
        result = (distance_square/size)**(.5)
        #print(result)
        return result

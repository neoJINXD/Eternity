__note__ = '''
t = Calculation()
t.sd([1, 4, 7, 2, 6])
'''

class Calculation:
    def __init__(self):
        self.values = []

    def dump(self):
        print(self.values)

    def cal_mean(self, arg):
        total = 0
        for e in arg:
            total += e
        size = len(arg)
        result = total / size
        return result

    def mad(self, *arg):
        values = list(arg)
        size = len(arg)
        mean = cal_mean(values)
        distance = 0
        for e in self.values:
            distance += (mean-e, e-mean)[e-mean>0]
        result = distance/size
        #print(result)
        return result

    def std(self, *arg):
        values = list(arg)
        size = len(values)
        mean = cal_mean(values)
        distance_square = 0
        for e in self.values:
            distance_square += (e-mean)*(e-mean)
        result = (distance_square/size)**(.5)
        #print(result)
        return result

class kuvvet3():
    def __init__(self,max):
        self.max=max
        self.kuvvet=0

    def __iter__(self):
        return self

    def __next__(self):
        if self.kuvvet<self.max:
            sonuc=3**self.kuvvet
            self.kuvvet+=1
            return sonuc
        else:
            self.kuvvet=0
            raise StopIteration

a=kuvvet3(6)
b=iter(a)
for i in a:
    print(i)
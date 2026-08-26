#lamba anonymous function
#x = lambda a : a + 10
#print(x(5)) #15
#print(x(6)) #16

#x = lambda a, b, c : a + b + c
#print(x(5, 6, 2)) #13
#print(x(1, 2, 3)) #6

def new(i):
    return lambda a : a * i

double = new(2)
triple = new(3)

print(double(5)) #10
print(triple(5)) #15
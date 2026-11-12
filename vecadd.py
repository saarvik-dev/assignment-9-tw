n = int(input("Enter size of vectors: "))

a = []
b = []

print("Enter first vector:")
for i in range(n):
    a.append(int(input("Enter element: ")))

print("Enter second vector:")
for i in range(n):
    b.append(int(input("Enter element: ")))

c = []

for i in range(n):
    c.append(a[i] + b[i])

print("Resultant vector:", c)

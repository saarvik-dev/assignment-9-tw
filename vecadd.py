# Input two vectors
a = list(map(int, input("Enter first vector elements: ").split()))
b = list(map(int, input("Enter second vector elements: ").split()))

# Calculate dot product
dot_product = sum(a[i] * b[i] for i in range(len(a)))

print("Dot product:", dot_product)

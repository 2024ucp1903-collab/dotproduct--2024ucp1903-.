v1 = list(map(float, input("Enter the first vector (space-separated): ").split()))
v2 = list(map(float, input("Enter the second vector (space-separated): ").split()))

if len(v1) != len(v2):
    print("Error: Vectors must have the same length.")
else:
    dot_product = sum(a * b for a, b in zip(v1, v2))
    print("Dot product for JatinBabe:", dot_product)

print("baba")
print("baba again because why not")
print("baba part 3")




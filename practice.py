k = 1

while k < 5:
    print(k)
    k += 1

l = 10

while l > 0:
    print(l)
    l-= 1


# Break

marks = 200

while marks < 500:
    print(marks)
    if marks == 400:
        break
    marks +=10

# Continue

numbers = 1

while numbers < 20:
    numbers+=1
    if numbers == 11:
        continue
    print(numbers)


colors = ["red", "blue"]

for col in colors:
    print(col)

colors_new = ("green", "orange")

for newcol in colors_new:
    print(newcol)

for i in range(20):
    print(i)


rows = 10

for i in range(1, rows+1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

for i in range(rows, 0, - 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()


rows = 10

for a in range(0, rows + 1):
    for b in range(0, a + 1):
        print("*", end=" ")
    print()

for a in range(rows, 0, -1):
    for b in range(0, a + 1):
        print("*", end=" ")
    print()
# nested loop = The "inner loop" will finish all of it's iterations before finishing one iteration of the "outer loop"

rows = int(input("How many rows?: "))
colummns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(colummns):
        print(symbol, end="")
    print()
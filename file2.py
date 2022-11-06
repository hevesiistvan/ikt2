for x in range(1,6,1):
    szam = int(input("Adj meg egy számot: "))
    if szam %2 ==0 and szam %3 ==0:
        print("Osztható")
    else:
        print("Nem osztható")

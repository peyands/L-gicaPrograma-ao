n=int(input("digite um número: "))
if (n>1):
    for i in range(2,n):
        if (n % i==0):
            print("é um número primo")
            break
        else:
            print("é um número primo")
            break
else:
    print("não é um número primo")
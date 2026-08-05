def cuenta_regresiva(n):
    if n == 0:
        return 
    print(n)
    cuenta_regresiva(n - 1)

cuenta_regresiva(10)

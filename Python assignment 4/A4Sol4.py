def isVow(a):
    tup=('a','e','i','o','u',
            'A','E','I','O','U')

    if a in tup:
        return True
    else:
        return False

print(isVow('z'))                    
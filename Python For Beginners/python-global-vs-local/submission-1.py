###Global Scope n = 100
n = 100

###Local scope
def print_local_variable() -> None:
    num = 100
    print(num)

print_local_variable()
print(n)

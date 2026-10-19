#SCOPES: determines visibility and lifetime of a variable.
# There are 4 types of Scopes. Mainly, looking at 2:
# 1. Global Scope: Variables defined at the top of any script or they are visible throughout the script. Let's look at [n = 10]
#2. Local scope: variables defined inside any function, invisible [add_one(n):]
def add_one(n):
    n = n + 1
    print(n)  

n = 10

add_one(n)     # Output: 11

print(n)       # Output: ?

import math 

def gameWithCells(n, m): 
    packages_in_rows = math.ceil(n / 2) 
    packages_in_columns = math.ceil(m / 2) 
    total_packages = packages_in_rows * packages_in_columns 

    return total_packages 
n, m = map(int, input().split()) 
result = gameWithCells(n, m) 
print(result)

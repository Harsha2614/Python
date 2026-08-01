n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
print()
def alphabet_x_pattern(n):
    for i in range(n):
        for j in range(n):
            if i == j or i + j == n - 1:
                # chr(65) is 'A', chr(66) is 'B', etc.
                print(chr(65 + j), end=" ")
            else:
                print(" ", end=" ")
        print()

alphabet_x_pattern(5)

print()

def concentric_pattern(n):
    size = 2 * n - 1
    for i in range(size):
        for j in range(size):
            # The value is determined by the distance to the nearest edge
            val = n - min(i, j, size - 1 - i, size - 1 - j)
            print(val, end=" ")
        print()

concentric_pattern(4)

print()

def matrix_star_x(n):
    for i in range(n):
        for j in range(n):
            # Logic for both diagonals
            if i == j or i + j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

matrix_star_x(7)

print()
 
def alpha_expansion(n):
    # First row is a number
    print(1) 
    
    # Subsequent rows use lowercase letters
    for i in range(1, n):
        char_code = 97  # ASCII for 'a'
        for j in range(i + 1):
            print(chr(char_code + j), end=" ")
        print()

alpha_expansion(4)

print()

def floyds_triangle(rows):
    num = 1
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(num, end=" ")
            num += 1
        print()
floyds_triangle(5)
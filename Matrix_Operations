import random

def generate_random_matrix(rows, cols):
  
    return [[random.randint(1, 100) for _ in range(cols)] for _ in range(rows)]

def get_column_sum(matrix, column_index):
   
    column_sum = sum(row[column_index] for row in matrix if column_index < len(row))
    return column_sum

def get_row_average(matrix, row_index):
   
    if row_index < len(matrix):
        row = matrix[row_index]
        row_average = sum(row) / len(row)
        return row_average
    else:
        raise IndexError("Row index out of range.")


rows = 4
cols = 5
matrix = generate_random_matrix(rows, cols)

print("Random Matrix:")
for row in matrix:
    print(row)

column_index = 2
column_sum = get_column_sum(matrix, column_index)
print(f"\nSum of column {column_index}: {column_sum}")

row_index = 1
row_average = get_row_average(matrix, row_index)
print(f"Average of row {row_index}: {row_average}")

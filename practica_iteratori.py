def generate_pascals_triangle(rows):
    triangle = []

    for row in range(rows):
        if row == 0:
            triangle.append([1])
        else:
            prev_row = triangle[row - 1]
            new_row = [1]

            for i in range(1, row):
                new_row.append(prev_row[i - 1] + prev_row[i])

            new_row.append(1)
            triangle.append(new_row)

    return triangle

def print_pascals_triangle(triangle):
    for row in triangle:
        print(" ".join(str(num) for num in row))


if __name__ == "__main__":
    num_rows = int(input())
    pascals_triangle = generate_pascals_triangle(num_rows)
    print(pascals_triangle)

    print_pascals_triangle(pascals_triangle)




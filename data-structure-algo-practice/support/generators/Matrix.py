class Matrix:

    @staticmethod
    def generate(x, y):
        x = [0] * x
        matrix = [x] * y
        return matrix

    @staticmethod
    def generate_square(size):
        x = [0] * size
        matrix = [x] * size
        return matrix

    @staticmethod
    def in_bounds(matrix, x, y):
        total_x = len(matrix[0])
        total_y = len(matrix)

        if (x > 0 and x < total_x):
            if(y > 0 and y < total_y):
                return True

        return False

    @staticmethod
    def pretty_print(matrix):
        for row in matrix:
            print(row)

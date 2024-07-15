def transpose(matrix):
    new_matrix = []
    for i in range(len(matrix[0])):
        new_matrix.append(list(map(lambda x: x[i], matrix)))
    return new_matrix
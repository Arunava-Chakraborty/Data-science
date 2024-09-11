# Example dataset with 3 samples and 2 features
X = [
    [2.5, 2.4],
    [0.5, 0.7],
    [2.2, 2.9]
]

def mean(X):
    mean_values = []
    for j in range(len(X[0])):  # For each column
        col_sum = 0
        for i in range(len(X)):  # For each row
            col_sum += X[i][j]
        mean_values.append(col_sum / len(X))
    return mean_values

def subtract_mean(X, mean_values):
    centered_data = []
    for i in range(len(X)):
        centered_row = []
        for j in range(len(X[0])):
            centered_row.append(X[i][j] - mean_values[j])
        centered_data.append(centered_row)
    return centered_data

def transpose(X):
    transposed = []
    for j in range(len(X[0])):  # For each column
        transposed_row = []
        for i in range(len(X)):  # For each row
            transposed_row.append(X[i][j])
        transposed.append(transposed_row)
    return transposed

def matrix_multiply(A, B):
    result = []
    for i in range(len(A)):  # For each row in A
        result_row = []
        for j in range(len(B[0])):  # For each column in B
            sum_product = 0
            for k in range(len(A[0])):  # For each element in row of A and column of B
                sum_product += A[i][k] * B[k][j]
            result_row.append(sum_product)
        result.append(result_row)
    return result

def covariance_matrix(X):
    n_samples = len(X)
    transposed_X = transpose(X)
    cov_matrix = []
    for i in range(len(transposed_X)):
        cov_row = []
        for j in range(len(transposed_X)):
            sum_product = 0
            for k in range(n_samples):
                sum_product += transposed_X[i][k] * transposed_X[j][k]
            cov_row.append(sum_product / (n_samples - 1))
        cov_matrix.append(cov_row)
    return cov_matrix


def pca(X, n_components):
    # Step 1: Calculate the mean of each feature
    mean_values = mean(X)

    # Step 2: Subtract the mean from the data
    centered_X = subtract_mean(X, mean_values)

    # Step 3: Calculate the covariance matrix
    cov_matrix = covariance_matrix(centered_X)

    # Step 4: Calculate eigenvalues and eigenvectors (simplified, usually use numerical methods)
    # This is a complex step, for simplicity, we'll assume precomputed eigenvalues/eigenvectors
    eigenvalues = [1.0, 0.5]  # Example eigenvalues
    eigenvectors = [[0.6, 0.4], [0.4, 0.6]]  # Example eigenvectors

    # Step 5: Sort eigenvectors by eigenvalues
    # Already sorted in this case, but usually done by sorting eigenvalues and reordering eigenvectors

    # Step 6: Select the top 'n_components' eigenvectors
    selected_eigenvectors = eigenvectors[:n_components]

    # Step 7: Transform the data
    transformed_data = matrix_multiply(centered_X, transpose(selected_eigenvectors))

    return transformed_data


# Perform PCA, reducing to 1 principal component
transformed_data = pca(X, n_components=1)

print("Transformed Data:")
for row in transformed_data:
    print(row)

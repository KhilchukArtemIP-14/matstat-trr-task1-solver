import numpy as np

def GetParameters(predictors,y_feedback):

    x = np.column_stack((np.ones((len(predictors[0]), 1)), *predictors))

    print(f"Matrix of x:\n", x)

    y = np.reshape(y_feedback, (-1, 1))  # Reshape y_feedback into a column vector
    print(f"Matrix of y:\n", y)

    X_transpose = np.transpose(x)  # Transpose of X
    XTX_inverse = np.linalg.inv(np.dot(X_transpose, x))  # Inverse of X^T X
    XT_y = np.dot(X_transpose, y)  # X^T y
    b = np.dot(XTX_inverse, XT_y)  # Calculate b

    print("Betas:")
    for i in range(len(b)):
        print(f"\n\tBeta_{i}:{b[i][0]}")
    return b
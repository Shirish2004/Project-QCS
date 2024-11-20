import numpy as np 
import cmath as cm
import math
import numpy as np
from sympy import sympify

def create_matrix():
    """
    Function to create a 2x2 matrix with user input.
    
    Instructions for Users:
    - Enter numbers row by row.
    - You can input real numbers, complex numbers, or mathematical expressions:
        Examples:
        - Real number: 0.707
        - Complex number: 1+2j
        - Mathematical expression: 1/sqrt(3), sqrt(2), or 1/3
    - If an input is invalid, you will be asked to re-enter the value.
    
    Returns:
        np.ndarray: A 2x2 numpy array representing the user-defined matrix.
    """
    print("Please follow the instructions below to enter your 2x2 matrix:\n")
    print("Instructions:")
    print("- Enter the entries row by row.")
    print("- Use real numbers, complex numbers (e.g., 1+2j), or mathematical expressions (e.g., 1/sqrt(3)).")
    print("- Press Enter after each entry.\n")

    row = 2
    col = 2
    matrix = []
    
    for i in range(row):
        a = []
        for c in range(col):
            while True:
                try:
                    entry = input(f"Enter entry ({i+1},{c+1}): ")
                    a.append(complex(sympify(entry).evalf()))
                    break
                except Exception as e:
                    print(f"Invalid input. Please try again. Error: {e}")
        matrix.append(a)

    return np.array(matrix),row,col

def write_matrix(matrix,row,col):
    print("\nYour entered matrix is below:")
    for r in range(row):
        for c in range(col):
            print(matrix[r][c], end=" ")
        print()
    
    print("\nThank you! Returning the matrix for further processing.\n")

def check_unitary(mat):
    """
    Function that checks if the matrix is unitary
    """
    identity_mat = np.identity(mat.shape[0])
    if not np.allclose(mat.dot(mat.conj().T), identity_mat):
        print("The matrix is not unitary. Please enter a unitary matrix.")
        return False
    return True



def complex_to_polar(z):
    """
    Converts a complex number into its polar form.
    """
    r = np.abs(z)
    theta = np.angle(z)
    return r, theta

def det_U(mat):
    determinant = np.linalg.det(mat)
    return determinant

def reconstruct_matrix(phi, theta, omega):
    """
    Reconstructs the matrix using the given rotation angles phi, theta, and omega.
    """
    m00 = (np.cos(theta / 2)) * (np.cos((phi + omega) / 2) - 1j * np.sin((phi + omega) / 2))
    m01 = -(np.sin(theta / 2)) * (np.cos((phi - omega) / 2) + 1j * np.sin((phi - omega) / 2))
    m10 = (np.sin(theta / 2)) * (np.cos((phi - omega) / 2) - 1j * np.sin((phi - omega) / 2))
    m11 = (np.cos(theta / 2)) * (np.cos((phi + omega) / 2) - 1j * np.sin((phi + omega) / 2))

    reconstructed = np.array([[m00, m01], [m10, m11]])
    return reconstructed



def calculate_phase_difference(original_matrix, reconstructed_matrix):
    """
    Calculates the phase difference between the original and reconstructed matrices.
    """
    original_flat = original_matrix.flatten()
    reconstructed_flat = reconstructed_matrix.flatten()
    
    for o, r in zip(original_flat, reconstructed_flat):
        if o != 0:
            real = o.real
            img = o.imag
            if real != 0:
                phase_difference = math.acos(real)
            else :
                phase_difference = math.asin(img)
            break
    else:
        raise ValueError("Both matrices are zero matrices; phase difference is undefined.")
    phase_difference = math.degrees(phase_difference)
    exponential_form = f"e^(i*{phase_difference})"
    return phase_difference, exponential_form




def main():
    """
    Main function that calculates the required values of alpha, beta, gamma, 
    and the phase difference, and reconstructs the matrix.
    """
    mat, row, col = create_matrix()
    write_matrix(mat, row, col)
    
    if check_unitary(mat):
        deter_unit = det_U(mat)
        print(f"The determinant of the matrix is: {deter_unit}")
        _, beta = complex_to_polar(deter_unit)
        a, c = mat[0][0], mat[1][0]
        r, alpha = complex_to_polar(a)
        s, gamma = complex_to_polar(c)
        theta = 2 * math.acos(r)
        omega = gamma - alpha 
        phi = beta - gamma - alpha 
        print(f"Rotation angles in radians: Phi = {phi:.1f}, Theta = {theta:.1f}, Omega = {omega:.1f}")
        print(f"Rotation angles in degrees: Phi = {math.degrees(phi):.1f}, Theta = {math.degrees(theta):.1f}, Omega = {math.degrees(omega):.1f}")
        reconstructed_matrix = reconstruct_matrix(phi, theta, omega)
        print("\nReconstructed Matrix (rounded to 1 decimal):")
        print(np.round(reconstructed_matrix, 1)) 
        phase_diff, exp_form = calculate_phase_difference(mat, reconstructed_matrix)
        print(f"\nPhase Difference (degrees): {phase_diff:.1f}")
        print(f"Phase Difference (exponential form): {exp_form}")
        print("\nThus, the reconstructed matrix can be expressed as:")
        print(f"{np.round(reconstructed_matrix, 1)} ≈ {exp_form} * {np.round(mat, 1)}")
    else:
        print("The input matrix is not unitary. Please enter a valid unitary matrix.")
        main()

    return beta

if __name__ == "__main__":
    main()
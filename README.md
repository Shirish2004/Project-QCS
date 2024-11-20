
# Unitary Matrix Visualizations and Decompositions

---

## Project Description

This project involves visualizing and decomposing unitary matrices for understanding their properties, applications, and their rotational decomposition. It uses the **Manim** animation library to create illustrative scenes for educational purposes in quantum mechanics and linear algebra.

---

## Files in the Project

1. **`animation.py`**:
   - Focuses on visualizing basic quantum gates like the Pauli matrices and their representations.
   - Includes `IntroScene` to generate the introduction scene.
   - Introduces the relation between unitary matrices and fundamental quantum transformations.

2. **`decomposing_unitary.py`**:
   - Visualizes the decomposition of a general unitary matrix \( U \) into rotation matrices \( R_x \), \( R_y \), and \( R_z \).
   - Includes step-by-step parameterization and visual aids for better understanding.

3. **`main.py`**:
   - A command-line interface to interact with the user for creating 2x2 matrices.
   - Performs validation of unitarity, calculates rotation angles (\( \phi, 	heta, \omega \)), reconstructs the matrix, and evaluates the phase difference between the original and reconstructed matrices.

4. **`unitary_matrix.py`**:
   - Introduces the basic definitions and properties of unitary matrices.
   - Highlights their role in quantum computing through examples of quantum gates and applications.

---

## Dependencies

- **Python Version**: 3.10 or above
- **Key Libraries**:
  - `manim`
  - `numpy`
  - `sympy`

---

## Environment Setup with Conda

To set up the environment for this project:

1. **Create a Conda Environment**:
   ```bash
   conda create -n manim_env python=3.10 -y
   ```
2. **Activate the Environment**:
   ```bash
   conda activate manim_env
   ```
3. **Install Dependencies**:
   ```bash
   pip install manim numpy sympy
   ```

---

## Running the Project

1. **Run Manim Animation Files**:
   - Each Manim file generates specific scenes. Use the following commands to render them:

   - **Run `unitary_matrix.py`**:
     ```bash
     manim -pql unitary_matrix.py UnitaryMatrices
     ```
     This renders the scene explaining unitary matrices, their properties, and applications.

   - **Run `decomposing_unitary.py`**:
     ```bash
     manim -pql decomposing_unitary.py DecomposingUnitary
     ```
     This creates a visualization of the decomposition process for unitary matrices.

   - **Run `animation.py`** (Generates Introduction Scene with `IntroScene`):
     ```bash
     manim -pql animation.py IntroScene
     ```
     This visualizes the Pauli matrices and their significance in quantum mechanics.

2. **Run the Main Script (`main.py`)**:
   - Use this script to interactively create and analyze 2x2 unitary matrices.
   - **Run Command**:
     ```bash
     python main.py
     ```
   - **Functionality**:
     - Accepts user input for a 2x2 matrix.
     - Validates if the matrix is unitary.
     - Computes decomposition angles (\( \phi, 	heta, \omega \)), reconstructs the matrix, and calculates the phase difference.

---

## Additional Notes

- Ensure `manim` is properly installed and configured. Test the installation with:
  ```bash
  manim -h
  ```
- Rendered videos are stored in the `media` folder generated by Manim in the project directory.

--- 

## Contact
For questions or issues, please reach out to the project maintainer.

from manim import *

class IntroScene(Scene):
    def construct(self):
        # Title
        title = Text(
            "QCS Project: Expressing Unitary Matrix in terms of Rotation Matrices (1-Qubit System)",
            font_size=36,
            color=BLUE,
        ).to_edge(UP, buff=0.75)  # Add spacing above title
        self.play(FadeIn(title, shift=UP), run_time=2)
        
        # Subtitle
        subtitle = Text(
            "Project Presented by Shubham and Shirish",
            font_size=28,
            color=WHITE,
        ).next_to(title, DOWN, buff=1.5)  # Add spacing between title and subtitle
        self.play(FadeIn(subtitle, shift=DOWN), run_time=2)

        # Unitary Matrix Relation
        unitary_relation = MathTex(
            r"U = e^{i\alpha} \cdot R_x(\phi) \cdot R_y(\theta) \cdot R_z(\omega)",
            font_size=32,
        ).next_to(subtitle, DOWN, buff=0.8)  # Add spacing below subtitle
        self.play(Write(unitary_relation), run_time=2)

        # Pauli Matrices (Displayed in a Column)
        pauli_x = MathTex(r"\sigma_x = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}", font_size=30)
        pauli_y = MathTex(r"\sigma_y = \begin{bmatrix} 0 & -i \\ i & 0 \end{bmatrix}", font_size=30)
        pauli_z = MathTex(r"\sigma_z = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}", font_size=30)

        pauli_x.to_edge(LEFT, buff=1).shift(UP * 1.5)
        pauli_y.next_to(pauli_x, DOWN, buff=1)
        pauli_z.next_to(pauli_y, DOWN, buff=1)

        # Animate Pauli Matrices
        self.play(
            Write(pauli_x),
            Write(pauli_y),
            Write(pauli_z),
            run_time=3,
        )

        # Hold the scene for 5 seconds
        self.wait(5)

        # Fade out everything
        self.play(
            FadeOut(title, shift=UP),
            FadeOut(subtitle, shift=DOWN),
            FadeOut(unitary_relation, shift=DOWN),
            FadeOut(pauli_x),
            FadeOut(pauli_y),
            FadeOut(pauli_z),
        )

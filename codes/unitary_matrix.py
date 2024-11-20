from manim import *

class UnitaryMatrices(Scene):
    def construct(self):
        # Scene Title
        title = Text("Unitary Matrices", font_size=50).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Matrix Example and Definition
        matrix_example = MathTex(
            r"U = \begin{pmatrix} a & b \\ c & d \end{pmatrix}",
            r"a,b,c,d \in C",
            font_size=40
        ).shift(UP * 2)
        
        definition = VGroup(
            Tex(r"A unitary matrix $U$ is defined as:", font_size=40),
            MathTex(r"U^\dagger U = UU^\dagger = I", font_size=40)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(matrix_example, DOWN)
        
        definition_explanation = VGroup(
            Tex(r"$U^\dagger$ is the conjugate transpose of U", font_size=35),
            Tex(r"$I$ is the identity matrix", font_size=35)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(definition, DOWN, buff=0.5)

        # Animate matrix and definition
        self.play(Write(matrix_example))
        self.play(
            Write(definition[0]),
            Write(definition[1]),
            run_time=2
        )
        self.play(
            FadeIn(definition_explanation[0], shift=UP * 0.5),
            FadeIn(definition_explanation[1], shift=UP * 0.5),
            run_time=2
        )
        self.wait(3)

        # Properties Section
        properties_title = Text("Properties", font_size=45).to_edge(UP)
        properties = VGroup(
            Tex(r"1. Eigenvalues: $|\lambda| = 1$", font_size=35),
            Tex(r"2. Determinant: $|\det(U)| = 1$", font_size=35),
            Tex(r"3. Columns form orthonormal basis", font_size=35),
            Tex(r"4. Length-preserving transformation", font_size=35)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).shift(DOWN * 0.5)

        # Transition to properties
        self.play(
            ReplacementTransform(title, properties_title),
            FadeOut(matrix_example),
            FadeOut(definition),
            FadeOut(definition_explanation),
            run_time=1.5
        )

        # Animate properties one by one
        for prop in properties:
            self.play(Write(prop), run_time=1)
        self.wait(3)

        # Applications Section
        applications_title = Text("Applications in Quantum Computing", font_size=45).to_edge(UP)
        applications = VGroup(
            Tex(r"1. Quantum Gates", font_size=35),
            MathTex(r"\text{e.g., } X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}", font_size=35),
            Tex(r"2. State Transformations", font_size=35)
            # Tex(r"3. Quantum Algorithms", font_size=35)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).shift(DOWN * 0.5)

        # Transition to applications
        self.play(
            ReplacementTransform(properties_title, applications_title),
            FadeOut(properties),
            run_time=1.5
        )

        # Animate applications
        self.play(Write(applications), run_time=3)
        self.wait(3)

        
        self.play(
            FadeOut(applications_title),
            FadeOut(applications),
            run_time=1.5
        )
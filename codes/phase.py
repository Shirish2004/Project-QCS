from manim import *
import numpy as np

class PhaseDifference(Scene):
    def construct(self):
        # Scene 1: Title and Introduction
        title = Text("Calculating Phase Difference", font_size=50).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introduction with better spacing
        intro_text = VGroup(
            Tex(r"Using the decomposition parameters:", font_size=36),
            MathTex(r"\phi, \omega, \text{ and } \theta", font_size=36),
            Tex(r"to reconstruct the unitary matrix.", font_size=36)
        ).arrange(DOWN, buff=0.5).next_to(title, DOWN, buff=1)
        
        self.play(Write(intro_text), run_time=2)
        self.wait(2)

        # Scene 2: Matrix Reconstruction
        matrix_title = Text("Reconstructed Matrix (Euler Form)", font_size=44).to_edge(UP)
        
        matrix_formula = MathTex(
            r"R(\theta, \phi, \omega) = \begin{pmatrix} "
            r"m_{00} & m_{01} \\ m_{10} & m_{11} \end{pmatrix}",
            font_size=40
        ).next_to(matrix_title, DOWN, buff=1)

        # Transition to matrix section
        self.play(
            ReplacementTransform(title, matrix_title),
            FadeOut(intro_text),
            Write(matrix_formula),
            run_time=2
        )
        self.wait(1)

        # Matrix elements with improved spacing and size
        elements_title = Tex("Matrix Elements:", font_size=30).next_to(matrix_formula, DOWN, buff=0.5)
        elements = VGroup(
            MathTex(r"m_{00} = \cos(\tfrac{\theta}{2})[\cos(\tfrac{\phi + \omega}{2}) - i \sin(\tfrac{\phi + \omega}{2})], or \cos(\tfrac{\theta}{2})e^{-i\tfrac{\phi + \omega}{2}}", font_size=32),
            MathTex(r"m_{01} = -\sin(\tfrac{\theta}{2})[\cos(\tfrac{\phi - \omega}{2}) + i \sin(\tfrac{\phi - \omega}{2})], or -\sin(\tfrac{\theta}{2})e^{i\tfrac{\phi - \omega}{2}}", font_size=32),
            MathTex(r"m_{10} = \sin(\tfrac{\theta}{2})[\cos(\tfrac{\phi - \omega}{2}) - i \sin(\tfrac{\phi - \omega}{2})], or \sin(\tfrac{\theta}{2})e^{-i\tfrac{\phi - \omega}{2}}", font_size=32),
            MathTex(r"m_{11} = \cos(\tfrac{\theta}{2})[\cos(\tfrac{\phi + \omega}{2}) - i \sin(\tfrac{\phi + \omega}{2})], or \cos(\tfrac{\theta}{2})e^{-i\tfrac{\phi + \omega}{2}}", font_size=32)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        
        elements.next_to(elements_title, DOWN, buff=0.5)
        elements_group = VGroup(elements_title, elements)

        self.play(
            Write(elements_title),
            run_time=1
        )
        for element in elements:
            self.play(Write(element), run_time=1)
        self.wait(4)

        # Scene 3: Phase Factor Calculation
        psi_title = Text("Estimating Phase Factor (ψ)", font_size=44).to_edge(UP)
        
        psi_explanation = VGroup(
            Tex(r"The phase factor $\psi$ is calculated by comparing", font_size=36),
            MathTex(r"\text{Reconstructed Matrix} = e^{i\psi} \cdot U", font_size=36),
            Tex(r"where U is the target unitary matrix.", font_size=36)
        ).arrange(DOWN, buff=0.5).next_to(psi_title, DOWN, buff=1)

        self.play(
            FadeOut(matrix_formula),
            FadeOut(elements_group),
            ReplacementTransform(matrix_title, psi_title),
            FadeOut(matrix_formula),
            FadeOut(elements_group),
            Write(psi_explanation),
            run_time=2
        )
        self.wait(2)

        # Phase comparison equation
        comparison = VGroup(
            MathTex(r"\cos(\psi) + i\sin(\psi) = \frac{U_{ij}}{R_{ij}}", font_size=40),
            Tex(r"where $i,j$ are indices of any non-zero element", font_size=32)
        ).arrange(DOWN, buff=0.5).next_to(psi_explanation, DOWN, buff=1)

        self.play(Write(comparison), run_time=2)
        self.wait(2)

        # Scene 4: Final Matrix
        final_title = Text("Final Reconstructed Matrix", font_size=44).to_edge(UP)
        
        final_equation = MathTex(
            r"U = e^{i\psi} R(\theta, \phi, \omega)",
            font_size=40
        ).next_to(final_title, DOWN, buff=1)

        summary = VGroup(
            Tex(r"This completes the reconstruction process:", font_size=36),
            Tex(r"1. Calculate matrix elements using $\theta, \phi, \omega$", font_size=32),
            Tex(r"2. Determine phase factor $\psi$", font_size=32),
            Tex(r"3. Combine to get final unitary matrix", font_size=32)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(final_equation, DOWN, buff=1)

        self.play(
            ReplacementTransform(psi_title, final_title),
            FadeOut(psi_explanation),
            FadeOut(comparison),
            Write(final_equation),
            run_time=2
        )
        
        for line in summary:
            self.play(Write(line), run_time=0.8)
        self.wait(2)

        # Closing Scene
        closing_title = Text("Thank You!", font_size=50).to_edge(UP)
        closing_text = Tex(
            r"Understanding decomposition of unitary matrices in terms of rotational matrices",
            font_size=36
        ).next_to(closing_title, DOWN, buff=1)

        self.play(
            ReplacementTransform(final_title, closing_title),
            FadeOut(final_equation),
            FadeOut(summary),
            # Write(closing_text),
            run_time=2
        )
        self.wait(2)

        # Final fadeout
        self.play(
            FadeOut(closing_title),
            # FadeOut(closing_text),
            run_time=1.5
        )
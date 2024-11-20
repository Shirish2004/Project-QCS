from manim import *

class DecomposingUnitary(Scene):
    def construct(self):
        # Scene Title with more emphasis
        title = Text("Decomposing Unitary Matrices", font_size=50).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Initial Unitary Matrix Setup
        unitary_matrix = MathTex(
            r"U = \begin{pmatrix} a & b \\ c & d \end{pmatrix}",
            font_size=44
        ).shift(UP * 2)

        # Properties with better spacing
        properties = VGroup(
            Tex(r"From Definition:", font_size=30),
            MathTex(r"\ U^\dagger U = UU^\dagger = I", font_size=30),
            MathTex(r" \implies |a|^{2} + |c|^{2} = 1, and |b|^{2} + |d|^{2} = 1", font_size=30)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(unitary_matrix, DOWN, buff=0.75)

        # Animate initial setup
        self.play(Write(unitary_matrix))
        for prop in properties:
            self.play(Write(prop), run_time=1)
        self.wait(2)
        properties2 = VGroup(
            MathTex(r" \ U^{-1} = U^\dagger", font_size=30),
            MathTex(r"\implies \tfrac{1}{\det(U)} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix} = \begin{pmatrix} a^{*} & c^{*} \\ b^{*} & d^{*} \end{pmatrix} ", font_size=30),
            MathTex(r"\implies d = a^{*}\det(U),  \& \text{b} = -c^{*}\det(U)", font_size=30),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(unitary_matrix, DOWN, buff=0.3)
        self.play(FadeOut(properties),
                  run_time=1)
        for prop in properties2:
            self.play(Write(prop), run_time=1)
        self.wait(2)
        properties3 = VGroup(
            MathTex(r"\ \det(U) = e^{i\beta}, \text{ for some } \beta \in R", font_size=30),
            MathTex(r"d = a^{*}e^{i\beta}, \text{ and b } = -c^{*}e^{i\beta}", font_size=30),
            MathTex(r"\ U = \begin{pmatrix} a & -c^{*}e^{i\beta} \\ c & a^{*}e^{i\beta} \end{pmatrix}", font_size=30)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(unitary_matrix, DOWN, buff=0.3)
        self.play(FadeOut(properties2),
                  run_time=1)
        for prop in properties3:
            self.play(Write(prop), run_time=1)
        self.wait(2)
        properties4 = VGroup(
            MathTex(r"\text{Since a,c} \in C", font_size=30),
            MathTex(r"a = re^{i\alpha}, \text{ and } c = se^{i\gamma}, \text{where r,s,} \alpha, \gamma \in R", font_size=30),
            MathTex(r"\text{Now } |a|^{2} + |c|^{2} = 1 \implies r^{2} + s^{2} = 1", font_size=30),
            Tex(r"Parameterization : ",font_size = 30),
            MathTex(r" r = \cos(\tfrac{\theta}{2}), \& s = \sin(\tfrac{\theta}{2}) \text{ for some } \theta \in R",font_size=30),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(unitary_matrix, DOWN, buff=0.3)
        self.play(FadeOut(properties3),
                  run_time=1)
        for prop in properties4:
            self.play(Write(prop), run_time=1)
        self.wait(2)
        properties5 = VGroup(
            MathTex(r"a = e^{i\alpha}\cos(\tfrac{\theta}{2}), \text{ and } c = e^{i\gamma}\sin(\tfrac{\theta}{2}))",font_size=30),
            MathTex(r"a^{*} = e^{-i\alpha}\cos(\tfrac{\theta}{2}, \text{ and } c^{*} = e^{-i\gamma}\sin(\tfrac{\theta}{2}))",font_size=30),
            MathTex(r"\ U = \begin{pmatrix} e^{i\alpha}\cos(\tfrac{\theta}{2}) & \-e^{i(\beta-\gamma)}\sin(\tfrac{\theta}{2}) \\ e^{i\gamma}\sin(\tfrac{\theta}{2}) & e^{i(\beta-\alpha)}\cos(\tfrac{\theta}{2}) \end{pmatrix}}",font_size=30),
            MathTex(r"\ U = e^{i(\tfrac{\beta}{2})}\begin{pmatrix} e^{i(\alpha -\tfrac{\beta}{2})}\cos(\tfrac{\theta}{2}) & \-e^{i(\tfrac{\beta}{2}-\gamma)}\sin(\tfrac{\theta}{2}) \\ e^{(-i\gamma -\tfrac{\beta}{2})}\sin(\tfrac{\theta}{2}) & e^{i(\tfrac{\beta}{2}-\alpha)}\cos(\tfrac{\theta}{2}) \end{pmatrix}}",font_size=30)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(unitary_matrix, DOWN, buff=0.3)
        self.play(FadeOut(properties4),
                  run_time=1)
        for prop in properties5:
            self.play(Write(prop), run_time=1)
        self.wait(2)
        properties6 = VGroup(
            MathTex(r"\ U = \begin{pmatrix} e^{-i(\tfrac{\beta}{2} -\tfrac{\alpha}{2}-\tfrac{\alpha}{2}-\tfrac{\gamma}{2}+\tfrac{\gamma}{2})}\cos(\tfrac{\theta}{2}) & \-e^{i(\tfrac{\beta}{2}-\tfrac{\gamma}{2}-\tfrac{\gamma}{2}+\tfrac{\alpha}{2}-\tfrac{\alpha}{2})}\sin(\tfrac{\theta}{2}) \\ e^{-i(\tfrac{\beta}{2}-\tfrac{\gamma}{2}-\tfrac{\gamma}{2}+\tfrac{\alpha}{2}-\tfrac{\alpha}{2})}\sin(\tfrac{\theta}{2}) & e^{i(\tfrac{\beta}{2} -\tfrac{\alpha}{2}-\tfrac{\alpha}{2}-\tfrac{\gamma}{2}+\tfrac{\gamma}{2})}\cos(\tfrac{\theta}{2}) \end{pmatrix}}",font_size=30),
            MathTex(r"\ U = \begin{pmatrix} e^{-i(\tfrac{\phi + \omega}{2})}\cos(\tfrac{\theta}{2}) & \-e^{i(\tfrac{\phi -\omega}{2}}\sin(\tfrac{\theta}{2}) \\ e^{(-i\tfrac{\phi -\omega}{2})}\sin(\tfrac{\theta}{2}) & e^{i(\tfrac{\phi + \omega}{2})}\cos(\tfrac{\theta}{2}) \end{pmatrix}}",font_size=30),
            MathTex(r"\text{Where, } \phi = \beta - \alpha - \gamma, \omega = \gamma -\alpha",font_size=30)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).next_to(unitary_matrix, DOWN, buff=0.3)
        self.play(FadeOut(properties5),
                  run_time=1)
        for prop in properties6:
            self.play(Write(prop), run_time=1)
        self.wait(2)

        # Decomposition Introduction
        decomp_title = Text("Rotational Decomposition", font_size=45).to_edge(UP)
        
        # Main decomposition equation with color coding
        decomp_eq = MathTex(
            r"U = ", r"e^{i\psi}", r"R_z(\phi)", r"R_y(\theta)", r"R_z(\omega)",
            font_size=44
        ).shift(UP * 2)  # Moved up slightly
        
        # Color coding for clarity
        decomp_eq[1].set_color(YELLOW)  # Phase factor
        decomp_eq[2].set_color(BLUE)    # First Z rotation
        decomp_eq[3].set_color(GREEN)   # Y rotation
        decomp_eq[4].set_color(RED)     # Second Z rotation

        # Transition to decomposition
        self.play(
            FadeOut(properties6),
            ReplacementTransform(title, decomp_title),
            FadeOut(unitary_matrix),
            run_time=3
        )
        self.play(Write(decomp_eq), run_time=2)
        self.wait(1)

        # Rotation Matrices with color matching
        rotations = VGroup(
            MathTex(
                r"R_z(\phi) = \begin{pmatrix} e^{-i\phi/2} & 0 \\ 0 & e^{i\phi/2} \end{pmatrix}",
                font_size=40
            ).set_color(BLUE),
            MathTex(
                r"R_y(\theta) = \begin{pmatrix} \cos(\theta/2) & -\sin(\theta/2) \\ \sin(\theta/2) & \cos(\theta/2) \end{pmatrix}",
                font_size=40
            ).set_color(GREEN),
            MathTex(
                r"R_z(\omega) = \begin{pmatrix} e^{-i\omega/2} & 0 \\ 0 & e^{i\omega/2} \end{pmatrix}",
                font_size=40
            ).set_color(RED)
        ).arrange(DOWN, buff=0.5).shift(DOWN * 0.5)  # Increased buffer and adjusted position

        # Show rotation matrices
        for rotation in rotations:
            self.play(Write(rotation), run_time=3)
        self.wait(2)

        # First set of steps
        steps = VGroup(
            Tex(r"Finding angles $\phi, \theta, \omega$:", font_size=35),
            MathTex(r"\bullet\ \phi = \beta - \gamma - \alpha", font_size=35),
            MathTex(r"\bullet\ \theta = 2\arccos(|a|)", font_size=35),
            MathTex(r"\bullet\ \omega = \gamma - \alpha", font_size=35),
            MathTex(r"If \det(U) = x+iy, \text{ then } \beta = \arctan(\tfrac{y}{x})",font_size = 30)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)  # Reduced buffer for better spacing

        # Transition to first steps
        self.play(
            FadeOut(rotations),
            run_time=3
        )
        
        # Position steps in upper half of screen
        steps.next_to(decomp_eq, DOWN, buff=0.75)
        
        # Show first set of steps
        for step in steps:
            self.play(Write(step), run_time=1)
        self.wait(2)

        # Second set of steps
        steps2 = VGroup(
            Tex(r"Where we estimate $\alpha$ and $\gamma$ from:", font_size=40),  # Fixed typo
            MathTex(r"a = re^{i\alpha}, \text{ where } r = |a|", font_size=35),  # Simplified
            MathTex(r"c = se^{i\gamma}, \text{ where } s = |c|", font_size=35)   # Simplified
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)

        self.play(
            FadeOut(steps),
            run_time=3
        )
        # Position second set of steps below first set
        steps2.next_to(decomp_eq, DOWN, buff=0.75)
        
        # Show second set of steps
        for step in steps2:
            self.play(Write(step), run_time=1)
        self.wait(2)
        # Final summary
        summary = VGroup(
            Tex(r"This decomposition:", font_size=40),
            Tex(r"$\bullet$ Represents any $2\times2$ unitary matrix", font_size=35),
            Tex(r"$\bullet$ Uses only three rotation angles", font_size=35),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        # Show summary by replacing both sets of steps
        self.play(
            FadeOut(steps2),
            FadeIn(summary.next_to(decomp_eq, DOWN, buff=0.75)),  # Position summary below equation
            run_time=3
        )
        self.wait(2)
        closing_title = Text("Thank You!", font_size=50).to_edge(UP)
        # Clean fadeout
        self.play(
            ReplacementTransform(decomp_title, closing_title),
            FadeOut(decomp_title),
            FadeOut(decomp_eq),
            FadeOut(summary),
            FadeOut(closing_title),
            run_time=3
        )
from manim import *
from animation import IntroScene
from unitary_matrix import UnitaryMatrices
from decomposing_unitary import DecomposingUnitary
from phase import PhaseDifference

class CombinedScenes(Scene):
    def construct(self):
        # IntroScene
        intro_scene = IntroScene()
        intro_scene.construct()
        for mobject in intro_scene.mobjects:
            self.add(mobject)  # Add each mobject from IntroductionScene to this scene
        self.wait(2)
        self.remove(*intro_scene.mobjects)  # Remove all mobjects for a clean slate

        # UnitaryMatrices
        unitary_scene = UnitaryMatrices()
        unitary_scene.construct()
        for mobject in unitary_scene.mobjects:
            self.add(mobject)  # Add each mobject from UnitaryMatrices
        self.wait(2)
        self.remove(*unitary_scene.mobjects)

        # DecomposingUnitary
        decompose_scene = DecomposingUnitary()
        decompose_scene.construct()
        for mobject in decompose_scene.mobjects:
            self.add(mobject)  # Add each mobject from DecomposingUnitary
        self.wait(2)
        self.remove(*decompose_scene.mobjects)

        # PhaseDifference
        phase_scene = PhaseDifference()
        phase_scene.construct()
        for mobject in phase_scene.mobjects:
            self.add(mobject)  # Add each mobject from PhaseDifference
        self.wait(2)
import manimgx as m

class CenaDark(m.ThreeDScene):
    def construct(self):
        # Define o ângulo da câmera 3D
        self.set_camera_orientation(phi=65 * m.DEGREES, theta=-45 * m.DEGREES)
        
        # Cria um cubo escuro com bordas brilhantes
        cubo = m.Cube(side_length=3, fill_opacity=0.8, color=m.DARK_GREY, stroke_color=m.WHITE)
        
        # Anima a criação do cubo e depois gira a câmera
        self.play(m.Create(cubo), run_time=2)
        self.begin_ambient_camera_rotation(rate=0.5)
        self.wait(4)

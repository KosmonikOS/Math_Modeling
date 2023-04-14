import sympy as sy
class ThreeEdgeManipulatorForPlane:
    def __init__(self,r1,r2,r3):
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3
    def findAngles(self,destX,destY):
        if (destX * 2 + destY * 2) ** 0.5 > self.r1 + self.r2 + self.r3:
            return []
        φ1,φ2,φ3 = sy.symbols('φ1, φ2, φ3')
        equation1 = self.r1*sy.cos(φ1) + self.r2*sy.cos(φ1 + φ2) + self.r3*sy.cos(φ1 + φ2 + φ3) - destX
        equation2 = self.r1*sy.sin(φ1) + self.r2*sy.sin(φ1 + φ2) + self.r3*sy.sin(φ1 + φ2 + φ3) - destY
        result = sy.solve((equation1, equation2),(φ1,φ2,φ3))
        return result
import sympy as sy
class ThreeEdgeManipulatorForPlane:
    def __init__(self,r1,r2,r3):
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3
    def findAngles(self,destX,destY):
        if (destX ** 2 + destY ** 2) ** 0.5 > self.r1 + self.r2 + self.r3: return []
        φ1,φ2,φ3 = sy.symbols('φ1, φ2, φ3')
        equation1 = 2 * self.r1 * self.r3 * sy.cos(φ3 + φ2) + 2 * self.r2 * self.r3 * sy.cos(φ3) + 2 * self.r1 * self.r2 * sy.cos(φ2) + self.r3 ** 2 +self.r2 ** 2 +self.r3 ** 2 - destX ** 2 - destY ** 2
        firstResult = sy.solve(equation1,(φ2,φ3))
        if len(firstResult) == 0: return []
        φ2 = firstResult[0][0]
        equation2 = sy.cos(φ1) * self.r1 + self.r2 * sy.cos(φ1 + φ2) + self.r3 * sy.cos(φ1 + φ2 + φ3) - destX
        secondResult = sy.solve(equation2,(φ1,φ3))
        return [secondResult[0][0],φ2,φ3]
import sympy as sy
class TwoEdgeManipulatorForPlane:
    def __init__(self,r1,r2):
        self.r1 = r1
        self.r2 = r2
    def findAngles(self,destX,destY):
        distance = (destX ** 2 + destY ** 2) ** 0.5
        if(distance > self.r1 + self.r2
           or distance < max(self.r1,self.r2) - min(self.r1,self.r2)): return []
        φ1,φ2 = sy.symbols('φ1, φ2')
        equationX = self.r1 * sy.cos(φ1) + self.r2 * sy.cos(φ1 + φ2) - destX
        equationY = self.r1 * sy.sin(φ1) + self.r2 * sy.sin(φ1 + φ2) - destY
        result = sy.solve((equationX,equationY),(φ1,φ2))
        return result

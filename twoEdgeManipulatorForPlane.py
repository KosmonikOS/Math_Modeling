import sympy as sy
class TwoEdgeManipulatorForPlane:
    def __init__(self,r1,r2):
        self.r1 = r1
        self.r2 = r2
    def tryToReach(self,destX,destY):
        #x2 = r1 cos(φ1) + r2 cos(φ1 + φ2), y2 = r1 sin(φ1) + r2 sin(φ1 + φ2)
        φ1,φ2 = sy.symbols('φ1, φ2')
        equationX = self.r1 * sy.cos(φ1) + self.r2 * sy.cos(φ1 + φ2) - destX
        equationY = self.r1 * sy.sin(φ1) + self.r2 * sy.sin(φ1 + φ2) - destY
        result = sy.solve((equationX,equationY),(φ1,φ2))
        return result

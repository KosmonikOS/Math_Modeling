import numpy as np
import sympy as sy
class ThreeEdgeManipulatorForSpace:
    def __init__(self,r1,r2,r3):
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3
    def findAngles(self,destX,destY,destZ):
        if np.sqrt(destX ** 2 + destY ** 2 + destZ ** 2) > (self.r1 + self.r2 + self.r3):
            print('End-effecter is outside the workspace')
            return []
        if destY != 0:
            φ1 = np.arctan(destX / destY)
        else:
            φ1 = 0 if destX > 0 else np.pi
        φ2,φ3 = sy.symbols('φ2, φ3')
        equation1 = self.r2 * np.cos(φ1) * sy.cos(φ2) + self.r3 * np.cos(φ1) * sy.cos(φ2 + φ3) - (destX - self.r1 * np.cos(φ1))
        equation2 = self.r2 * np.cos(φ1) * sy.sin(φ2) + self.r3 * np.cos(φ1) * sy.sin(φ2 + φ3) - destZ * np.cos(φ1)
        result = sy.solve((equation1,equation2),(φ2,φ3))
        if len(result) == 0: return []
        return [φ1, result[0][0], result[1][0]]
    def findPosition(self, φ1, φ2, φ3):
        x3 = (self.r1 + self.r2*sy.cos(φ2) + self.r3*sy.cos(φ2 + φ3))*sy.cos(φ1)
        y3 = (self.r1 + self.r2*sy.cos(φ2) + self.r3*sy.cos(φ2 + φ3))*sy.sin(φ1)
        z3 = self.r2*sy.sin(φ2) + self.r3*sy.sin(φ2 + φ3)
        return np.array([x3, y3, z3])

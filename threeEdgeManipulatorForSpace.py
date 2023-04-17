import numpy as np
import sympy as sy
class ThreeEdgeManipulatorForSpace:
    def __init__(self,r1,r2,r3):
        self.L12 = r1
        self.L23 = r2
        self.L34 = r3
    def findAngles(self,destX,destY,destZ):
        if np.sqrt(destX ** 2 + destY ** 2 + destZ ** 2) > (self.L12 + self.L23 + self.L34):
            print('End-effecter is outside the workspace')
            return []
        if destY != 0:
            φ1 = np.arctan(destX / destY)
        else:
            φ1 = 0 if destX > 0 else np.pi
        x2 = self.L12 * np.cos(φ1)
        y2 = self.L12 * np.sin(φ1)
        C = np.sqrt((destX-x2) ** 2 + (destY-y2) ** 2 + (destZ) ** 2)

        if (self.L23 + self.L34) < C or np.abs(self.L23 - self.L34) > C:
            print('End-effecter is outside the workspace')
            return []
            
        a = np.rad2deg(np.arccos((self.L23 ** 2 + self.L34 ** 2 - C ** 2) / (2 * self.L23 * self.L34)))
        b = np.rad2deg(np.arccos((self.L23 ** 2 + C ** 2 - self.L34 ** 2) / (2 * self.L23 * C)))

        
        J1a = np.rad2deg(np.arctan2(destZ, np.sqrt((destX-x2)**2+(destY-y2)**2))) - b
        J2a = 180 - a
        

        J1b = np.rad2deg(np.arctan2(destZ, np.sqrt((destX-x2)**2+(destY-y2)**2))) + b
        J2b = -(180 - a)
        return [[φ1,J1a,J2a],[φ1,J1b,J2b]]
    def findPosition(self, φ1, φ2, φ3):
        x3 = (self.L12 + self.L23*sy.cos(φ2) + self.L34*sy.cos(φ2 + φ3))*sy.cos(φ1)
        y3 = (self.L12 + self.L23*sy.cos(φ2) + self.L34*sy.cos(φ2 + φ3))*sy.sin(φ1)
        z3 = self.L23*sy.sin(φ2) + self.L34*sy.sin(φ2 + φ3)
        return np.array([x3, y3, z3])

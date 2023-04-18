import numpy as np
import sympy as sy
import matplotlib.pyplot as plt
class ThreeEdgeManipulatorForSpace:
    def __init__(self,r1,r2,r3):
        self.L12 = r1
        self.L23 = r2
        self.L34 = r3
    def findAngles(self,destX,destY,destZ):
        if np.sqrt(destX ** 2 + destY ** 2 + destZ ** 2) > (self.L12 + self.L23 + self.L34):
            print('End-effecter is outside the workspace')
            return
        if destY != 0:
            J1 = np.arctan(destX / destY)
        else:
            J1 = 0 if destX > 0 else np.pi
        x2 = self.L12 * np.cos(J1)
        y2 = self.L12 * np.sin(J1)
        C = np.sqrt((destX-x2) ** 2 + (destY-y2) ** 2 + (destZ) ** 2)

        if (self.L23 + self.L34) < C or np.abs(self.L23 - self.L34) > C:
            print('End-effecter is outside the workspace')
            return            
        a = np.rad2deg(np.arccos((self.L23 ** 2 + self.L34 ** 2 - C ** 2) / (2 * self.L23 * self.L34)))
        b = np.rad2deg(np.arccos((self.L23 ** 2 + C ** 2 - self.L34 ** 2) / (2 * self.L23 * C)))
    
        J2a = np.rad2deg(np.arctan2(destZ, np.sqrt((destX-x2)**2+(destY-y2)**2))) - b
        J3a = 180 - a
    
        J2b = np.rad2deg(np.arctan2(destZ, np.sqrt((destX-x2)**2+(destY-y2)**2))) + b
        J3b = -(180 - a)
        print(f"Angles are ({J1:.2f}, {J2a:.2f}, {J3a:.2f}) for elbow-down configuration")
        print(f"Angles are ({J1:.2f}, {J2b:.2f}, {J3b:.2f}) for elbow-up configuration")

        La = self.L23 * np.cos(J2a) + np.sqrt((x2)**2+(y2)**2)
        x3a = La * np.cos(J1)
        y3a = La * np.sin(J1)
        z3a = self.L23 * np.sin(J2a)

        Lb = self.L23 * np.cos(J2b) + np.sqrt((x2)**2+(y2)**2)
        x3b = Lb * np.cos(J1)
        y3b = Lb * np.sin(J1)
        z3b = self.L23 * np.sin(J2b)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot([0, x2], [0, y2], 'b')
        ax.plot([x2,x3a],[y2,y3a],[0,z3a],'b')
        ax.plot([x3a, destX], [y3a,destY],[z3a,destZ], 'b')
        ax.plot([x2,x3b],[y2,y3b],[0,z3b],'g', linestyle='--')
        ax.plot([x3b, destX], [y3b,destY],[z3b,destZ],'g', linestyle='--')
        ax.plot([0], [0], 'ro')
        ax.plot([destX], [destY],[destZ], 'ro')
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')
        plt.title('Inverse Kinematics 3-Links Spatial Manipulator')
        plt.show()

    def findPosition(self, φ1, φ2, φ3):
        x3 = (self.L12 + self.L23*sy.cos(φ2) + self.L34*sy.cos(φ2 + φ3))*sy.cos(φ1)
        y3 = (self.L12 + self.L23*sy.cos(φ2) + self.L34*sy.cos(φ2 + φ3))*sy.sin(φ1)
        z3 = self.L23*sy.sin(φ2) + self.L34*sy.sin(φ2 + φ3)
        return np.array([x3, y3, z3])

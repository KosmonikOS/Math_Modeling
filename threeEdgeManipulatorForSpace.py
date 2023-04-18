import numpy as np
import matplotlib.pyplot as plt
class ThreeEdgeManipulatorForSpace:
    def __init__(self,L12, L23,L34):
        self.L12 = L12
        self.L23 = L23
        self.L34 = L34
    def solveInversedKinematics(self,destX,destY,destZ):
        if np.sqrt(destX ** 2 + destY ** 2 + destZ ** 2) > (self.L12 + self.L23 + self.L34):
            print('End-effecter is outside the workspace')
            return
        if destX != 0:
            J1 = np.arctan2(destY,destX) #Need to check
        else:
            J1 = 0 if destX > 0 else np.pi
        x2 = self.L12 * np.cos(J1) * np.sign(destX)
        y2 = self.L12 * np.sin(J1) * np.sign(destY)
        C = np.sqrt((destX-x2) ** 2 + (destY-y2) ** 2 + (destZ) ** 2)

        if (self.L23 + self.L34) < C or np.abs(self.L23 - self.L34) > C:
            print('End-effecter is outside the workspace')
            return            
        a = np.arccos((self.L23 ** 2 + self.L34 ** 2 - C ** 2) / (2 * self.L23 * self.L34))
        b = np.arccos((self.L23 ** 2 + C ** 2 - self.L34 ** 2) / (2 * self.L23 * C))
    
        J2a = np.arctan2(destZ, np.sqrt((destX-x2)**2+(destY-y2)**2)) - b
        J3a = np.pi - a
    
        J2b = np.arctan2(destZ, np.sqrt((destX-x2)**2+(destY-y2)**2)) + b
        J3b = -(np.pi - a)
        print(f"Angles are ({(np.rad2deg(J1)):.2f}, {np.rad2deg(J2a):.2f}, {np.rad2deg(J3a):.2f}) for elbow-down configuration")
        print(f"Angles are ({np.rad2deg(J1):.2f}, {np.rad2deg(J2b):.2f}, {np.rad2deg(J3b):.2f}) for elbow-up configuration")

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
        ax.plot([x2], [y2], 'bo')
        ax.plot([x3a], [y3a],[z3a],'bo')
        ax.plot([x3b], [y3b],[z3b],'go')
        ax.plot([0], [0], 'ro')
        ax.plot([destX], [destY],[destZ], 'ro')
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')
        plt.title('Inverse Kinematics 3-Links Spatial Manipulator')
        plt.show()
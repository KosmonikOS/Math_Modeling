import numpy as np
import matplotlib.pyplot as plt
class ThreeEdgeManipulatorForPlane:
    def __init__(self,L12, L23,L34):
        self.L12 = L12
        self.L23 = L23
        self.L34 = L34
    def solveInversedKinematics(self,xe, ye, g):
        x3 = xe - (self.L34 * np.cos(np.deg2rad(g)))
        y3 = ye - (self.L34 * np.sin(np.deg2rad(g)))
        C = np.sqrt(x3 ** 2 + y3 ** 2)

        if (self.L12 + self.L23) < C or np.abs(self.L12 - self.L23) > C:
            print('End-effecter is outside the workspace')
            return
            
        a = np.rad2deg(np.arccos((self.L12 ** 2 + self.L23 ** 2 - C ** 2) / (2 * self.L12 * self.L23)))
        b = np.rad2deg(np.arccos((self.L12 ** 2 + C ** 2 - self.L23 ** 2) / (2 * self.L12 * C)))

        
        J1a = np.rad2deg(np.arctan2(y3, x3)) - b
        J2a = 180 - a
        J3a = g - J1a - J2a

        J1b = np.rad2deg(np.arctan2(y3, x3)) + b
        J2b = -(180 - a)
        J3b = g - J1b - J2b

        print(f"Angles are ({J1a:.2f}, {J2a:.2f}, {J3a:.2f}) for elbow-down configuration")
        print(f"Angles are ({J1b:.2f}, {J2b:.2f}, {J3b:.2f}) for elbow-up configuration")
    
        x2a = self.L12*np.cos(np.deg2rad(J1a))
        y2a = self.L12*np.sin(np.deg2rad(J1a))
        x2b = self.L12*np.cos(np.deg2rad(J1b))
        y2b = self.L12*np.sin(np.deg2rad(J1b))
        r = self.L12 + self.L23 + self.L34
        plt.plot([0, x2a], [0, y2a], 'b')
        plt.plot([x2a, x3], [y2a, y3], 'b')
        plt.plot([x3, xe], [y3, ye], 'b')
        plt.plot([0, x2b], [0, y2b], 'g', linestyle='--')
        plt.plot([x2b, x3], [y2b, y3], 'g', linestyle='--')
        plt.plot([0, x2a, x3], [0, y2a, y3], 'bo')
        plt.plot([x2b], [y2b], 'go')
        plt.plot([0], [0], 'ro')
        plt.plot([xe], [ye], 'ro')
        plt.grid()
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Inverse Kinematics 3-Links Planar Manipulator')
        plt.show()

# Inverse Kinematics Solver for N-Links Manipulators

This project is a Python implementation of the inverse kinematics solver for manipulators. The solver uses both geometric and algebraic approachs to compute the joint angles necessary to achieve a desired end-effector position.

## Implemented Manipulators

### 2-Links Planar Manipulator

This manipulator consists of two links connected by revolute joints in a planar configuration.

### 3-Links Planar Manipulator

This manipulator consists of three links connected by revolute joints in a planar configuration.

### 3-Links Spatial Manipulator

This manipulator consists of three links connected by revolute joints in a spatial configuration.

## Requirements

The following packages are required to run the solver:

- NumPy
- SymPy
- Matplotlib

## Sources

The following sources were used to implement the solver:

- О.М. Киселёв "Математические основы роботехники" 2019
- Juecoree "Forward and Reverse Kinematics for 3R Planar Manipulator"

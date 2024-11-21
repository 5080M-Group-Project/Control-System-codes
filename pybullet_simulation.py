import pybullet
import pybullet_data
import os
import time

pybullet.connect(pybullet.GUI)
obj = pybullet.loadURDF(os.path.join(pybullet_data.getDataPath(), "plane.urdf"), 0, 0, -1)
subj = pybullet.loadURDF(os.path.join(os.getcwd(), "robot_description/urdf/robot_description.urdf"))
pybullet.setGravity(0,0,-9.8)

while True:
  pybullet.stepSimulation()
  posAndOrn = pybullet.getBasePositionAndOrientation(subj)

  # jointIndex = 1 refers to the left wheel
  pybullet.setJointMotorControl2(bodyUniqueId=subj, jointIndex=1, controlMode=pybullet.VELOCITY_CONTROL, targetVelocity=20.0)
  # jointIndex = 0 refers to the right wheel
  pybullet.setJointMotorControl2(bodyUniqueId=subj, jointIndex=0, controlMode=pybullet.VELOCITY_CONTROL, targetVelocity=-20.0)
  time.sleep(1/240)
baxter_interface ROS Noetic fork
===============================

This is a ROS Noetic/Python3 compatible fork of the baxter_interface repository. Other ROS Noetic compatible Baxter packages can be found here:


+------------------+-----------------------------------------------------+
| baxter_interface | https://github.com/maymohan/baxter                  |
+------------------+-----------------------------------------------------+
| baxter_tools     | https://github.com/maymohan/baxter_tools            |
+------------------+-----------------------------------------------------+
| baxter_common    | https://github.com/maymohan/baxter_examples         |
+------------------+-----------------------------------------------------+
| baxter_examples  | https://github.com/maymohan/baxter_common           |
+------------------+-----------------------------------------------------+
| baxter_pykdl     | https://github.com/maymohan/baxter_pykdl            |
+------------------+-----------------------------------------------------+
| baxter_simulator | https://github.com/maymohan/baxter_simulator        |
+------------------+-----------------------------------------------------+

Details of the original repositories are below.


baxter_interface
----------------

Python interface classes and action servers for control of
the Baxter Research Robot from Rethink Robotics

Code & Tickets
--------------

+-----------------+----------------------------------------------------------------+
| Documentation   | http://sdk.rethinkrobotics.com/wiki                            |
+-----------------+----------------------------------------------------------------+
| Issues          | https://github.com/RethinkRobotics/baxter_interface/issues     |
+-----------------+----------------------------------------------------------------+
| Contributions   | http://sdk.rethinkrobotics.com/wiki/Contributions              |
+-----------------+----------------------------------------------------------------+

baxter_interface Repository Overview
------------------------------------

::

     .
     |
     +-- src/                                  baxter_interface api
     |   +-- baxter_interface/                 baxter component classes
     |       +-- analog_io.py
     |       +-- camera.py
     |       +-- digital_io.py
     |       +-- gripper.py
     |       +-- head.py
     |       +-- limb.py
     |       +-- navigator.py
     |       +-- robot_enable.py
     |       +-- robust_controller.py
     |       +-- settings.py
     |   +-- baxter_control/                   generic control utilities
     |   +-- baxter_dataflow/                  timing/program flow utilities
     |   +-- joint_trajectory_action/          joint trajectory action implementation
     |   +-- gripper_action/                   gripper action implementation
     |   +-- head_action/                      head action implementation
     |
     +-- scripts/                              action server executables
     |   +-- joint_trajectory_action_server.py
     |   +-- gripper_action_server.py
     |   +-- head_action_server.py
     |
     +-- cfg/                                  dynamic reconfigure action configs


Other Baxter Repositories
-------------------------

+------------------+-----------------------------------------------------+
| baxter           | https://github.com/RethinkRobotics/baxter           |
+------------------+-----------------------------------------------------+
| baxter_tools     | https://github.com/RethinkRobotics/baxter_tools     |
+------------------+-----------------------------------------------------+
| baxter_examples  | https://github.com/RethinkRobotics/baxter_examples  |
+------------------+-----------------------------------------------------+
| baxter_common    | https://github.com/RethinkRobotics/baxter_common    |
+------------------+-----------------------------------------------------+
| baxter_pykdl     | https://github.com/RethinkRobotics/baxter_pykdl     |
+------------------+-----------------------------------------------------+
| baxter_simulator | https://github.com/RethinkRobotics/baxter_simulator |
+------------------+-----------------------------------------------------+

Latest Release Information
--------------------------

http://sdk.rethinkrobotics.com/wiki/Release-Changes

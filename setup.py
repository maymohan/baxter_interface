#!/usr/bin/env python3
from setuptools import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup()
d['packages'] = ['baxter_interface', 'baxter_control', 'baxter_dataflow',
                 'joint_trajectory_action', 'gripper_action', 'head_action']
d['package_dir'] = {'': 'src'}

setup(**d)

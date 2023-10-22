# Copyright (c) 2022, NVIDIA CORPORATION & AFFILIATES, ETH Zurich, and University of Toronto
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""Configuration for the Universal Robots.

The following configuration parameters are available:

* :obj:`UR10_CFG`: The UR10 arm without a gripper.

Reference: https://github.com/ros-industrial/universal_robot
"""


from omni.isaac.orbit.actuators.group import ActuatorGroupCfg
from omni.isaac.orbit.actuators.group.actuator_group_cfg import ActuatorControlCfg
from omni.isaac.orbit.actuators.model import ImplicitActuatorCfg
from omni.isaac.orbit.utils.assets import ISAAC_ORBIT_NUCLEUS_DIR, ISAAC_NUCLEUS_DIR
from omni.isaac.orbit.actuators.config.robotiq import ROBOTIQ_2F85_MIMIC_GROUP_CFG

from ..single_arm import SingleArmManipulatorCfg

_UR10_ARM_INSTANCEBALE_USD = f"{ISAAC_ORBIT_NUCLEUS_DIR}/Robots/UniversalRobots/UR10/ur10_instanceable.usd"

UR10_CFG = SingleArmManipulatorCfg(
    meta_info=SingleArmManipulatorCfg.MetaInfoCfg(
        usd_path=_UR10_ARM_INSTANCEBALE_USD,
        arm_num_dof=6,
        tool_num_dof=0,
        tool_sites_names=None,
    ),
    init_state=SingleArmManipulatorCfg.InitialStateCfg(
        dof_pos={
            "shoulder_pan_joint": 0.0,
            "shoulder_lift_joint": -1.712,
            "elbow_joint": 1.712,
            "wrist_1_joint": 0.0,
            "wrist_2_joint": 0.0,
            "wrist_3_joint": 0.0,
        },
        dof_vel={".*": 0.0},
    ),
    ee_info=SingleArmManipulatorCfg.EndEffectorFrameCfg(body_name="ee_link"),
    actuator_groups={
        "arm": ActuatorGroupCfg(
            dof_names=[".*"],
            model_cfg=ImplicitActuatorCfg(velocity_limit=100.0, torque_limit=87.0),
            control_cfg=ActuatorControlCfg(
                command_types=["p_abs"],
                stiffness={".*": None},
                damping={".*": None},
            ),
        ),
    },
)
"""Configuration of UR-10 arm using implicit actuator models."""

# _UR5_ARM_INSTANCEBALE_USD = f"omniverse://localhost/Users/kdharmarajan/ur5e.usd"
_UR5_ARM_INSTANCEBALE_USD = f"omniverse://localhost/Users/kdharmarajan/ur5e_with_gripper.usd"
# _UR5_ARM_INSTANCEBALE_USD = f"{ISAAC_NUCLEUS_DIR}/Robots/UniversalRobots/ur5e/ur5e.usd"

UR5_EE_INFO = SingleArmManipulatorCfg.EndEffectorFrameCfg(body_name="ee_link")
UR5_EE_INFO.rot_offset = (-0.7071071, 0.0, -0.7071064, 0.0)
UR5_EE_INFO.pos_offset = (0.13, 0.0, 0.0)

UR5_CFG = SingleArmManipulatorCfg(
    meta_info=SingleArmManipulatorCfg.MetaInfoCfg(
        usd_path=_UR5_ARM_INSTANCEBALE_USD,
        arm_num_dof=6,
        tool_num_dof=6,
        tool_sites_names=["robotiq_85_right_finger_tip_link"],
    ),
    init_state=SingleArmManipulatorCfg.InitialStateCfg(
        dof_pos={
            "shoulder_pan_joint": 0.0,
            "shoulder_lift_joint": -1.712,
            "elbow_joint": 1.712,
            "wrist_1_joint": 0.0,
            "wrist_2_joint": 0.0,
            "wrist_3_joint": 0.0,
        },
        dof_vel={".*": 0.0},
    ),
    ee_info=UR5_EE_INFO,
    actuator_groups={
        "arm": ActuatorGroupCfg(
            dof_names=["shoulder_pan_joint", "shoulder_lift_joint", "elbow_joint", "wrist_1_joint", "wrist_2_joint", "wrist_3_joint"],
            model_cfg=ImplicitActuatorCfg(velocity_limit=50.0, torque_limit=50.0),
            control_cfg=ActuatorControlCfg(
                command_types=["p_abs"],
                stiffness={".*": None},
                damping={".*": None},
            ),
        ),
        "gripper": ROBOTIQ_2F85_MIMIC_GROUP_CFG,
    },
)

from omni.isaac.orbit.actuators.group import ActuatorGroupCfg
from omni.isaac.orbit.actuators.group.actuator_group_cfg import ActuatorControlCfg
from omni.isaac.orbit.actuators.model import ImplicitActuatorCfg
from omni.isaac.orbit.utils.assets import ISAAC_ORBIT_NUCLEUS_DIR, ISAAC_NUCLEUS_DIR
from omni.isaac.orbit.actuators.config.kinova import KINOVA_S300_MIMIC_GROUP_CFG

from ..single_arm import SingleArmManipulatorCfg

_JACO_INSTANCEBALE_USD = f"{ISAAC_NUCLEUS_DIR}/Robots/Kinova/Jaco2/J2N6S300/j2n6s300_instanceable.usd"
print(_JACO_INSTANCEBALE_USD)

JACO_CFG = SingleArmManipulatorCfg(
    meta_info=SingleArmManipulatorCfg.MetaInfoCfg(
        usd_path=_JACO_INSTANCEBALE_USD,
        arm_num_dof=6,
        tool_num_dof=3,
        # tool_sites_names=["j2n6s300_link_finger_1", "j2n6s300_link_finger_2", "j2n6s300_link_finger_3"],
    ),
    init_state=SingleArmManipulatorCfg.InitialStateCfg(
        dof_pos={
            "j2n6s300_joint_1": 4.8055,
            "j2n6s300_joint_2": 2.9211,
            "j2n6s300_joint_3": 0.9989,
            "j2n6s300_joint_4": 4.2076,
            "j2n6s300_joint_5": 1.4420,
            "j2n6s300_joint_6": 1.3220,
            "j2n6s300_joint_finger_*": 0.0
        },
        dof_vel={".*": 0.0},
    ),
    ee_info=SingleArmManipulatorCfg.EndEffectorFrameCfg(body_name="j2n6s300_end_effector"),
    actuator_groups={
        "arm": ActuatorGroupCfg(
            dof_names=["j2n6s300_joint_[1-6]"],
            model_cfg=ImplicitActuatorCfg(velocity_limit=100.0, torque_limit=20.0),
            control_cfg=ActuatorControlCfg(
                command_types=["p_abs"],
                stiffness={".*": 1000.0},
                damping={".*": 80.0},
            ),
        ),
        "gripper": KINOVA_S300_MIMIC_GROUP_CFG,
    },
)

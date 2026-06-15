"""Locomotion action presets for the Elf3 robot."""

from holosoma.config_types.action import ActionManagerCfg, ActionTermCfg

elf3_29dof_joint_pos = ActionManagerCfg(
    terms={
        "joint_control": ActionTermCfg(
            func="holosoma.managers.action.terms.joint_control:JointPositionActionTerm",
            params={},
            scale=1.0,
            clip=None,
        ),
    }
)

__all__ = ["elf3_29dof_joint_pos"]

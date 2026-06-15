"""Default action manager configurations."""

from holosoma.config_values.loco.g1.action import g1_29dof_joint_pos
from holosoma.config_values.loco.elf3.action import elf3_29dof_joint_pos
from holosoma.config_values.loco.t1.action import t1_29dof_joint_pos

none = None

DEFAULTS = {
    "none": none,
    "elf3_29dof_joint_pos": elf3_29dof_joint_pos,
    "t1_29dof_joint_pos": t1_29dof_joint_pos,
    "g1_29dof_joint_pos": g1_29dof_joint_pos,
}

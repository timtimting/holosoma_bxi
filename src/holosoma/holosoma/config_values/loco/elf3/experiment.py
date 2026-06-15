from dataclasses import replace

from holosoma.config_types.experiment import ExperimentConfig, NightlyConfig, TrainingConfig
from holosoma.config_values import (
    action,
    algo,
    command,
    curriculum,
    observation,
    randomization,
    reward,
    robot,
    simulator,
    termination,
    terrain,
)

elf3_29dof = ExperimentConfig(
    env_class="holosoma.envs.locomotion.locomotion_manager.LeggedRobotLocomotionManager",
    training=TrainingConfig(project="hv-elf3-manager", name="elf3_29dof_manager", num_envs=1),
    algo=replace(
        algo.ppo,
        config=replace(algo.ppo.config, num_learning_iterations=25000, save_interval=1000, use_symmetry=True),
    ),
    simulator=simulator.mujoco,
    robot=robot.elf3_29dof,
    terrain=terrain.terrain_locomotion_mix,
    observation=observation.elf3_29dof_loco_single_wolinvel,
    action=action.elf3_29dof_joint_pos,
    termination=termination.elf3_29dof_termination,
    randomization=randomization.elf3_29dof_randomization,
    command=command.elf3_29dof_command,
    curriculum=curriculum.elf3_29dof_curriculum,
    reward=reward.elf3_29dof_loco,
    nightly=NightlyConfig(
        iterations=10000,
        metrics={"Episode/rew_tracking_ang_vel": [0.6, "inf"], "Episode/rew_tracking_lin_vel": [0.5, "inf"]},
    ),
)

elf3_29dof_fast_sac = ExperimentConfig(
    env_class="holosoma.envs.locomotion.locomotion_manager.LeggedRobotLocomotionManager",
    training=TrainingConfig(project="hv-elf3-manager", name="elf3_29dof_fast_sac_manager", num_envs=1),
    algo=replace(
        algo.fast_sac,
        config=replace(algo.fast_sac.config, num_learning_iterations=50000, save_interval=1000, use_symmetry=True),
    ),
    simulator=simulator.mujoco,
    robot=robot.elf3_29dof,
    terrain=terrain.terrain_locomotion_mix,
    observation=observation.elf3_29dof_loco_single_wolinvel,
    action=action.elf3_29dof_joint_pos,
    termination=termination.elf3_29dof_termination,
    randomization=randomization.elf3_29dof_randomization,
    command=command.elf3_29dof_command,
    curriculum=curriculum.elf3_29dof_curriculum_fast_sac,
    reward=reward.elf3_29dof_loco_fast_sac,
    nightly=NightlyConfig(
        iterations=50000,
        metrics={"Episode/rew_tracking_ang_vel": [0.7, "inf"], "Episode/rew_tracking_lin_vel": [0.75, "inf"]},
    ),
)

__all__ = ["elf3_29dof", "elf3_29dof_fast_sac"]

from lerobot.cameras.opencv.configuration_opencv import OpenCVCameraConfig
from lerobot.datasets.lerobot_dataset import LeRobotDataset
from lerobot.datasets.utils import hw_to_dataset_features
from lerobot.policies.act.modeling_act import ACTPolicy
from lerobot.robots.so101_follower import SO101FollowerConfig, SO101Follower
from lerobot.utils.control_utils import init_keyboard_listener
from lerobot.utils.utils import log_say
from lerobot.utils.visualization_utils import _init_rerun
from lerobot.record import record_loop

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from constants import (
    FOLLOWER_PORT,
    CAM_IDX,
    CAM_WIDTH,
    CAM_HEIGHT,
    CAM_FPS,
    HF_USER,
)

NUM_EPISODES = 5
FPS = CAM_FPS
EPISODE_TIME_SEC = 60
TASK_DESCRIPTION = "Dance same with camera evaluation"
POLICY_REPO_ID = f"{HF_USER}/dance_same_with_cam_policy"  # From training command
EVAL_DATASET_NAME = f"{HF_USER}/eval_dance_same_with_cam"

# Create the robot configuration
camera_config = {
    "front": OpenCVCameraConfig(
        index_or_path=CAM_IDX, width=CAM_WIDTH, height=CAM_HEIGHT, fps=FPS
    )
}

robot_config = SO101FollowerConfig(
    port=FOLLOWER_PORT,
    id="follow_arm",
    cameras=camera_config,
)

# Initialize the robot
robot = SO101Follower(robot_config)

# Initialize the policy
policy = ACTPolicy.from_pretrained(POLICY_REPO_ID)

# Configure the dataset features
action_features = hw_to_dataset_features(robot.action_features, "action")
obs_features = hw_to_dataset_features(robot.observation_features, "observation")
dataset_features = {**action_features, **obs_features}

# Create the dataset
dataset = LeRobotDataset.create(
    repo_id=EVAL_DATASET_NAME,
    fps=FPS,
    features=dataset_features,
    robot_type=robot.name,
    use_videos=True,
    image_writer_threads=4,
)

# Initialize the keyboard listener and rerun visualization
_, events = init_keyboard_listener()
_init_rerun(session_name="recording")

# Connect the robot
robot.connect()

for episode_idx in range(NUM_EPISODES):
    log_say(
        f"Running inference, recording eval episode {episode_idx + 1} of {NUM_EPISODES}"
    )

    # Run the policy inference loop
    record_loop(
        robot=robot,
        events=events,
        fps=FPS,
        policy=policy,
        dataset=dataset,
        control_time_s=EPISODE_TIME_SEC,
        single_task=TASK_DESCRIPTION,
        display_data=True,
    )

    dataset.save_episode()

# Clean up
robot.disconnect()
dataset.push_to_hub()

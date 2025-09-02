import time

from lerobot.datasets.lerobot_dataset import LeRobotDataset
from lerobot.robots.so101_follower.config_so101_follower import SO101FollowerConfig
from lerobot.robots.so101_follower.so101_follower import SO101Follower
from lerobot.utils.robot_utils import busy_wait
from lerobot.utils.utils import log_say

episode_idx = 0
DATASET_NAME = "KristinWei/dance_same"

robot_config = SO101FollowerConfig(
    port="/dev/ttyACM0",
    id="follow_arm",
)

robot = SO101Follower(robot_config)
robot.connect()

dataset = LeRobotDataset(DATASET_NAME, episodes=[episode_idx])
actions = dataset.hf_dataset.select_columns("action")

log_say(f"Replaying episode {episode_idx}")
for idx in range(dataset.num_frames):
    t0 = time.perf_counter()

    action = {
        name: float(actions[idx]["action"][i])
        for i, name in enumerate(dataset.features["action"]["names"])
    }
    robot.send_action(action)

    busy_wait(1.0 / dataset.fps - (time.perf_counter() - t0))

robot.disconnect()

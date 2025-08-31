from lerobot.teleoperators.so101_leader import SO101LeaderConfig, SO101Leader
from lerobot.robots.so101_follower import SO101FollowerConfig, SO101Follower

from constants import FOLLOWER_PORT, LEADER_PORT

robot_config = SO101FollowerConfig(
    port=FOLLOWER_PORT,
    id="follow_arm",
)

teleop_config = SO101LeaderConfig(
    port=LEADER_PORT,
    id="leader_arm",
)

robot = SO101Follower(robot_config)
teleop_device = SO101Leader(teleop_config)
robot.connect()
teleop_device.connect()

while True:
    action = teleop_device.get_action()
    robot.send_action(action)

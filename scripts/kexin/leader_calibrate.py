from lerobot.robots.so101_follower import SO101FollowerConfig, SO101Follower
from lerobot.teleoperators.so101_leader import SO101LeaderConfig, SO101Leader

follower_config = SO101FollowerConfig(
    port="/dev/ttyACM0",
    id="follow_arm",
)

leader_config = SO101LeaderConfig(
    port="/dev/ttyACM1",
    id="leader_arm",
)

follower = SO101Follower(follower_config)
follower.connect(calibrate=False)
follower.calibrate()
follower.disconnect()

leader = SO101Leader(leader_config)
leader.connect(calibrate=False)
leader.calibrate()
leader.disconnect()

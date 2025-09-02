from utils import get_hf_user

FOLLOWER_PORT = "/dev/ttyACM0"
LEADER_PORT = "/dev/ttyACM1"

TASK_NAME = "dance_same_with_cam"
# HF_USER = get_hf_user()
HF_USER = "kandj"  # use org name
DATASET_NAME = f"{HF_USER}/{TASK_NAME}"

CAM_IDX = 32
# get from running camera_check.py
CAM_WIDTH = 1920 
CAM_HEIGHT = 1080
CAM_FPS = 5

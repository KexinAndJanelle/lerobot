from lerobot.cameras.opencv.configuration_opencv import OpenCVCameraConfig
from lerobot.cameras.opencv.camera_opencv import OpenCVCamera
from lerobot.cameras.configs import ColorMode, Cv2Rotation

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from constants import CAM_IDX

# Construct an `OpenCVCameraConfig` with your desired FPS, resolution, color mode, and rotation.
config = OpenCVCameraConfig(
    index_or_path=CAM_IDX,
    fps=15,
    width=1920,
    height=1080,
    color_mode=ColorMode.RGB,
    rotation=Cv2Rotation.NO_ROTATION,
)

# Instantiate and connect an `OpenCVCamera`, performing a warm-up read (default).
camera = OpenCVCamera(config)
camera.connect()

# Read frames asynchronously in a loop via `async_read(timeout_ms)`
try:
    for i in range(10):
        frame = camera.async_read(timeout_ms=300)
        print(f"Async frame {i} shape:", frame.shape)
finally:
    camera.disconnect()

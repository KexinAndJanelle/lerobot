#!/usr/bin/env python

# Copyright 2024 The HuggingFace Inc. team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Imitation learning training script that wraps the main training pipeline.

This script provides a command-line interface for training imitation learning policies
using the LeRobot framework. It supports various policy types (ACT, Diffusion, etc.)
and can work with different datasets.

Usage example:
    python imitation_train.py \
      --dataset.repo_id=${HF_USER}/so101_test \
      --policy.type=act \
      --output_dir=outputs/train/act_so101_test \
      --job_name=act_so101_test \
      --policy.device=cuda \
      --wandb.enable=true \
      --policy.repo_id=${HF_USER}/my_policy
"""

import sys
from pathlib import Path

# Add the src directory to the path so we can import lerobot modules
src_path = Path(__file__).parent.parent.parent / "src"
sys.path.insert(0, str(src_path))

from lerobot.scripts.train import main as train_main


def main():
    """Main entry point for imitation training."""
    # The train_main function already handles all CLI parsing and training logic
    # We just need to call it directly
    train_main()


if __name__ == "__main__":
    main()
```bash
# cuda
lerobot-train \
  --dataset.repo_id=janelleopj/dance_same_with_cam \
  --policy.type=act \
  --output_dir=outputs/train/dance_same_with_cam \
  --job_name=act_dance_same_with_cam \
  --policy.device=cuda \
  --policy.repo_id=janelleopj/my_policy

# cpu
lerobot-train \
  --dataset.repo_id=janelleopj/dance_same_with_cam \
  --policy.type=act \
  --output_dir=outputs/train/dance_same_with_cam \
  --job_name=act_dance_same_with_cam \
  --policy.device=cpu \
  --policy.repo_id=janelleopj/my_policy
```

# Resume training

```bash
# cuda
cd lerobot
python src/lerobot/scripts/train.py \
  --dataset.repo_id=janelleopj/dance_same_with_cam \
  --policy.type=act \
  --output_dir=outputs/train/dance_same_with_cam_test0 \
  --job_name=act_dance_same_with_cam \
  --policy.device=cuda \
  --policy.repo_id=KristinWei/dance_same_with_cam_policy \
  --resume=true \
  --config_path=outputs/train/dance_same_with_cam_test0/checkpoints/last/pretrained_model/train_config.json
```
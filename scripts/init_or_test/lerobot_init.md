# find ports
make sure `pip install -e ".[feetech]"` is done, and then run `lerobot-find-port`
default setting for the scripts:
- folower: /dev/ttyACM0
- leader: /dev/ttyACM1

## enable serial ports permission
if you are using a linux system, you may need to run the following commands to enable
`sudo chmod 666 /dev/ttyACM0`
`sudo chmod 666 /dev/ttyACM1`

# huggingface token
`hf auth login --token ${HUGGINGFACE_TOKEN} --add-to-git-credential`
`echo 'export HF_USER=$(hf auth whoami | head -n 1)' >> ~/.bashrc`

# check which camera
open camera with external software (like cheese) then run on terminal:
`lsof /dev/video*`
(find /dev/videoXX)

or run `v4l2-ctl --list-devices` to list all video devices, run `sudo apt install v4l-utils` if not installed
# ports:
- folower: /dev/ttyACM0
- leader: /dev/ttyACM1

## enable serial ports permission
if you are using a linux system, you may need to run the following commands to enable
`sudo chmod 666 /dev/ttyACM0`
`sudo chmod 666 /dev/ttyACM1`

# huggingface token
huggingface-cli login --token ${HUGGINGFACE_TOKEN} --add-to-git-credential
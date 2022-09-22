eval "$(conda shell.bash hook)"
if [ -d "/home/parmpal/anaconda3/envs/yolochk" ] 
then
	echo "Enviornment exists. run "
	echo "conda activate yolochk"
else
	echo "Enviornment not exist not exists."
	conda create -n yolochk python==3.8.5 -y
	conda activate yolochk
	pip install -r requirementyolo.txt
	pip uninstall torch
	conda install pytorch==1.12.0 torchvision==0.13.0 torchaudio==0.12.0 cudatoolkit=11.3 -c pytorch -y
	echo "Enviornment Installed. run "
	echo "conda activate yolochk"
	
fi

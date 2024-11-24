```shell
docker build -t bubulamb/python:transformers .
```

build docker image `user/repo:tag` based on `Dockerfile`

------------------
build singularity image

```shell
module load singularity/3.11.3 
singularity build python_transformers.sif docker://user/repo:tag
```

--------------------

use docker image to run your script

```shell
singularity exec --bind /path/to/your/host/directory:/mnt python_3.10.sif python /mnt/your_script.py
```
Replace `/path/to/your/host/directory` with the actual path to the directory you want to mount.

`python_3.10.sif` should be replaced with the actual name of the SIF file you created.

`your_script.py` should be replaced with the name of your Python script.

* how to use singularity in hpc

[Example of Singularity](https://connectpolyu-my.sharepoint.com/personal/itsupres_connect_polyu_hk/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fitsupres%5Fconnect%5Fpolyu%5Fhk%2FDocuments%2FResearchWebPage%2FSHPC%2FOOD%2FSHPC%5Fsingularity%5Fexample%2Epdf&parent=%2Fpersonal%2Fitsupres%5Fconnect%5Fpolyu%5Fhk%2FDocuments%2FResearchWebPage%2FSHPC%2FOOD&ga=1)

[Example of Tensorflow with GPU using Singularity](https://connectpolyu-my.sharepoint.com/personal/itsupres_connect_polyu_hk/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fitsupres%5Fconnect%5Fpolyu%5Fhk%2FDocuments%2FResearchWebPage%2FSHPC%2FOOD%2FSHPC%5Ftensorflow%5Fgpu%5Fsingularity%5Fexample%2Epdf&parent=%2Fpersonal%2Fitsupres%5Fconnect%5Fpolyu%5Fhk%2FDocuments%2FResearchWebPage%2FSHPC%2FOOD&ga=1)

```shell
singularity exec --bind /path/to/your/host/directory:/mnt python_3.10.sif python /mnt/your_script.py

```

`singularity exec`: Command to execute a program within the Singularity container.

`--bind /path/to/your/host/directory:/mnt`: This option mounts the specified host directory to the /mnt directory in the Singularity container.

`python /mnt/your_script.py`: This is the command that runs your script inside the container.

**HPC:**

```shell
#!/bin/bash

#SBATCH --partition=h07gpuq1
#SBATCH --time=1-00:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=6
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=30000M
#SBATCH -J "bubu-kaggle"
#SBATCH --gres=gpu:1

PATH="/puhome/24112456g/kaggleMATH/"
SCRIPT_PATH="/puhome/24112456g/kaggleMATH/zqy/code/singular_qwen.py"

module load singularity/3.11.3

singularity exec --bind /puhome/24112456g/kaggleMATH/:/mnt/kaggleMATH ~/python_transformers.sif python /mnt/kaggleMATH/zqy/code/singular_qwen.py
# 用$PATH会报错，不知道为什么，就直接用路径了
```

`singular.sh`
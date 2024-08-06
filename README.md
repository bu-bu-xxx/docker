# tensorflow docker

[tensorflow docker安装指南](https://www.tensorflow.org/install/docker?hl=zh-tw)

1. 在本機主體機器上[安裝 Docker](https://docs.docker.com/install/)。

2. 如要在 Linux 上支援 GPU，請

   安裝 NVIDIA Docker 支援

   - 請使用 `docker -v` 記下您的 Docker 版本。19.03 **以前**的版本需要使用 nvidia-docker2 和 `--runtime=nvidia` 旗標。19.03 **以後**的版本則需要使用 `nvidia-container-toolkit` 套件和 `--gpus all` 旗標。您可以在上方網頁連結中找到這兩個選項。

![image-20240806044930034](./assets/image-20240806044930034.png)

> docker 依赖于cuda driver, 所以驱动版本不兼容会导致docker检测不到gpu

[NVIDIA container toolkit 仓库](https://github.com/NVIDIA/nvidia-container-toolkit)

[NVIDIA container toolkit installation guidance](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)

安装完需要`sudo systemctl restart docker.service`

* docker hub

```	
bubulamb/tensorflow-jupyter-gpu
```

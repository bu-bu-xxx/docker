# 基础镜像（与 compose 配置一致）
FROM pytorch/pytorch:2.7.0-cuda12.8-cudnn9-devel

# 声明构建参数（从 compose 接收）
ARG USER_UID=1000
ARG USER_GID=1000
ARG USER_NAME=appuser

# 创建用户组和用户（固定组名，但使用动态 GID）
RUN groupadd -g $USER_GID $USER_NAME && \
    useradd -m -s /bin/bash -u $USER_UID -g $USER_GID $USER_NAME 

# 切换用户身份（注意：必须在容器启动前切换）
USER $USER_UID:$USER_GID

# 设置工作目录（与 compose 挂载目录对应）
WORKDIR /learningFile
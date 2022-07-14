ARG IMAGE_NAME=docker.io/nvidia/cuda
FROM ${IMAGE_NAME}:11.7.0-runtime-ubuntu22.04 as base

ENV NV_CUDA_LIB_VERSION 11.7.0-1

FROM base as base-amd64

ENV NV_NVTX_VERSION 11.7.50-1
ENV NV_LIBNPP_VERSION 11.7.3.21-1
ENV NV_LIBNPP_PACKAGE libnpp-11-7=${NV_LIBNPP_VERSION}
ENV NV_LIBCUSPARSE_VERSION 11.7.3.50-1

ENV NV_LIBCUBLAS_PACKAGE_NAME libcublas-11-7
ENV NV_LIBCUBLAS_VERSION 11.10.1.25-1
ENV NV_LIBCUBLAS_PACKAGE ${NV_LIBCUBLAS_PACKAGE_NAME}=${NV_LIBCUBLAS_VERSION}

LABEL maintainer "NVIDIA CORPORATION <cudatools@nvidia.com>"

RUN apt-get update && apt-get install -y --no-install-recommends \
    cuda-libraries-11-7=${NV_CUDA_LIB_VERSION} \
    ${NV_LIBNPP_PACKAGE} \
    cuda-nvtx-11-7=${NV_NVTX_VERSION} \
    libcusparse-11-7=${NV_LIBCUSPARSE_VERSION} \
    ${NV_LIBCUBLAS_PACKAGE} \
    && rm -rf /var/lib/apt/lists/*

# Keep apt from auto upgrading the cublas and nccl packages. See https://gitlab.com/nvidia/container-images/cuda/-/issues/88
RUN apt-mark hold ${NV_LIBCUBLAS_PACKAGE_NAME}

RUN apt-get update && apt-get install -y --no-install-recommends
RUN apt-get -qq -y install wget

# Install miniconda
ENV CONDA_DIR /opt/conda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && /bin/bash ~/miniconda.sh -b -p /opt/conda

# Put conda in path so we can use conda activate
ENV PATH=$CONDA_DIR/bin:$PATH

RUN conda create -n poopy spacy spacy-transformers pandas pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch 

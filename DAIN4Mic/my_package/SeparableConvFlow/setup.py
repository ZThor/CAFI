import os
import json
from setuptools import setup, find_packages

from torch.utils.cpp_extension import BuildExtension, CUDAExtension
import torch

with open('../../compiler_args.json') as f:
    extra_compile_args = json.load(f)
setup(
    name='separableconvflow_cuda',
    ext_modules=[
        CUDAExtension('separableconvflow_cuda', [
            'separableconvflow_cuda.cc',
            'separableconvflow_cuda_kernel.cu'
        ], extra_compile_args=extra_compile_args)
    ],
    cmdclass={
        'build_ext': BuildExtension
    })

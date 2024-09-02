Required NVidia GPU, CUDA 11.8/12.1

1. CUDA 11.8 `pip install torch==2.1.0 torchvision==0.16.0 xformers --index-url https://download.pytorch.org/whl/cu118` OR CUDA 12.1 `pip3 install torch==2.1.0 torchvision==0.16.0 xformers --index-url https://download.pytorch.org/whl/cu121`
2. `pip install git+https://github.com/popraf/StreamDiffusion.git@main#egg=streamdiffusion[tensorrt]`
3. windows only `pip install --force-reinstall pywin32`
4. `python -m streamdiffusion.tools.install-tensorrt`
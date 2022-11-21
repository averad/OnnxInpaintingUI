# OnnxInpaintingUI
UI for ONNX based Stable Diffusion Inpainting

## Requirements
- Python 3.10 or earlier installed (https://www.python.org/downloads/)
- Git installed (https://gitforwindows.org/)

## Installation
### Create a Folder to Store Stable Diffusion Related Files
- Open File Explorer and navigate to your prefered storage location.
- Create a new folder named "Stable Diffusion" and open it.
- In the navigation bar, in file explorer, highlight the folder path and type `cmd` and press enter.

### Install 🤗 diffusers
The following steps creates a virtual environment (using venv) named sd_env (in the folder you have the cmd window opened to). Then it  installs diffusers ([latest from main branch](https://github.com/huggingface/diffusers)), transformers, onnxruntime, onnx, onnxruntime-directml, protobuf and gradio:
```bash
pip install virtualenv
python -m venv sd_env
sd_env\scripts\activate
python -m pip install --upgrade pip
pip install git+https://github.com/huggingface/diffusers.git
pip install transformers onnxruntime onnx torch ftfy spacy scipy gradio
pip install onnxruntime-directml --force-reinstall
pip install protobuf==3.20.1
```
To exit the virtual environment, close the command prompt. To start the virtual environment go to the scripts folder in sd_env and open a command prompt. Type activate and the virtual environment will activate.

## Running OnnxInpaintingUI
```bash
sd_env\scripts\activate
python inpainting_ui.py
```

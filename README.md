Video demonstration: https://youtu.be/6v8h8LPFRls

# Description
Tensorflow model adapted for DSCVL. 

https://github.com/tensorflow/models/tree/master/research/object_detection

# Dependencies
Tested, developed, and executed on Windows 10, build 1803
1. Python 3.5.2 - https://www.python.org/downloads/release/python-352/
2. Tensorflow-gpu to run visualization recommended
	- `pip3 install --upgrade tensorflow-gpu`
3. RPlidar A1 - https://www.slamtec.com/en/lidar/a1
	- `pip3 install rplidar`
4. Matplotlib
	- `pip3 install matplotlib`
5. Pillow
	- `pip3 install pillow`
6. OpenCV 3.4.0.12
	- `pip3 install opencv-python==3.4.0.12`
7. CP210x USB to UART Bridge VCP Driver (If on Windows 10, build 1803, please see below)
	- https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers

### Tensorflow-gpu
3. Nvidia CUDA Toolkit 9.0.176 
4. Nvidia CUDnn v7.0.4 for CUDA 9.0

## Windows 10, build 1803 Driver Fix
The CP210x USB to UART Bridge VCP Driver, required for RPlidar A1, does not meet Windows driver INF requirements and will not install.

[Read more](https://web.archive.org/web/20190414053931/https://www.silabs.com/community/interface/forum/_jcr_content/content/primary/qna.social.0.30)

[Instructions to enable unsigned driver installation](https://web.archive.org/web/20161214162911/https://www.maketecheasier.com/install-unsigned-drivers-windows10/)

My modified driver download
	- https://drive.google.com/file/d/1jKxpAml_JoFPP2b4fXIjJWZ2_udghgj9/view?usp=sharing

# Run Visualization
1. Install all dependencies
2. Clone repository
	- `git clone https://github.com/DSCVL/DSCVL-Vision.git`
3. In file `lam_helper.py`, replace line 71 `PORT_NAME = 'COM15'` with the COM port that the RPlidar A1 is connected to.
4. Ensure web cam and RPlidar are plugged in, execute with `main.py`
	- `python main.py`

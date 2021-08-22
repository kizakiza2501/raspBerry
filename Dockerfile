# FROM raspbian/stretch
FROM sdhibit/rpi-raspbian
USER root

RUN apt update
RUN apt upgrade -y

RUN apt install -y libhdf5-dev libqtwebkit4 libqt4-test libatlas-base-dev libjasper-dev

RUN apt install python3-dev -y
RUN apt install python3-pip -y
RUN apt install python3-picamera -y

RUN pip3 install pip -U
RUN pip3 install setuptools -U

RUN pip3 install numpy==1.18.1
RUN pip3 install scipy==1.3.3
RUN pip3 install scikit-learn==0.21.3
RUN pip3 install matplotlib
RUN pip3 install pandas==0.25.3
RUN pip3 install seaborn==0.8.0
RUN pip3 install tensorflow==1.14.0
RUN pip3 install keras
RUN pip3 install flask flask_cors -U
RUN pip3 install opencv_python

RUN apt-get update
RUN apt-get install python-picamera python3-picamera -y
RUN apt-get install python-opencv -y

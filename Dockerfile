FROM python:3.6

MAINTAINER biranchi125@gmail.com



#COPY . /app
#RUN python -m pip install -r /app/requirements.txt 

# CMD ["python", "/app/GNNSCModel.py"]
#CMD ["sh", "/app/train2.sh"]



COPY . .
RUN python -m pip install -r requirements.txt 
CMD ["python", "AMEVulDetector.py", "--model", "EncoderWeight", "--epochs", "10"]


# python3 AMEVulDetector.py --model EncoderWeight --lr 0.002 --dropout 0.2 --epochs 100 --batch_size 32

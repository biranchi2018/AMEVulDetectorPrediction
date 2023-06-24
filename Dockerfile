FROM python:3.6-slim

MAINTAINER biranchi125@gmail.com

COPY . .
RUN python -m pip install -r requirements.txt 
CMD ["python", "AMEVulDetector.py", "--model", "EncoderWeight", "--epochs", "10"]

# CMD ["python", "preprocessing.py"]

# python3 AMEVulDetector.py --model EncoderWeight --lr 0.002 --dropout 0.2 --epochs 100 --batch_size 32

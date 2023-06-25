FROM python:3.6-slim

MAINTAINER biranchi125@gmail.com

COPY . .
RUN python -m pip install -r requirements.txt 
CMD ["python", "AMEVulDetectorPrediction.py"]

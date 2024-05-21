FROM python:3.11.4-slim
RUN apt-get update && \
    apt-get install -y python3
WORKDIR /repaso
COPY scrapper.py ./

CMD ["python", "scrapper.py"]


FROM python:3.11.5-slim
RUN pip install aiohttp 
WORKDIR /Actividad7-C8286
COPY ejerasyncio.py ./

CMD ["python", "ejerasyncio.py"]


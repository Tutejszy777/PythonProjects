FROM python:3.9-slim

WORKDIR /app

COPY file_server.py /app/file_server.py

RUN mkdir -p /app/received_files

EXPOSE 5000

CMD ["python", "file_server.py"]
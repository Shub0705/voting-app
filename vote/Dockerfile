FROM python:3.10-slim
WORKDIR /app
RUN pip install flask redis
COPY app.py .
EXPOSE 80
CMD ["python", "app.py"]


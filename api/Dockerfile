FROM python:3
ADD . /app
WORKDIR /app
EXPOSE 5000
RUN pip install -r requirements.txt
ENV NAME World
ENTRYPOINT ["python", "app.py"]
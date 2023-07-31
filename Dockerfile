FROM python:3.8
WORKDIR /ouvidoria
COPY . /ouvidoria

#RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD ["python", "./ouvidoria.py"]

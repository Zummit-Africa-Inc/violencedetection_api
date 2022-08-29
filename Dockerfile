FROM tensorflow/tensorflow

WORKDIR /app

RUN apt-get -y update  && apt-get install -y \
  wget 

RUN pip install --upgrade setuptools 

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000:8000

RUN python download.py

CMD uvicorn app:app --reload --host 0.0.0.0 --port 8000
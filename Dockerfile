FROM ubuntu:latest

RUN apt-get update -y && apt-get install python3 python3-pip python3-dev -y
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
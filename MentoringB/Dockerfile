# write down the Dockerfile!
# python, flask are required and etc...
# The container open port number is 5000

FROM python:3.6.10

EXPOSE 5000

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt


CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0"]
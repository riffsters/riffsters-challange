FROM python:2.7
ENV AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}
ENV AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}
ADD . /code

WORKDIR /code

RUN pip install -r requirements.txt

CMD python app_api.py

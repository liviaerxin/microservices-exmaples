FROM python:3.7-slim

LABEL Author="1yue8haogaoqi"
LABEL E-mail="1yue8haogaoqi@gmail.com"

RUN pip install pipenv && \
  apt-get update && \
  apt-get install -y --no-install-recommends gcc python3-dev libssl-dev


WORKDIR /app

# both files are explicitly required!
COPY Pipfile Pipfile.lock ./

RUN pipenv sync && \
  pipenv install --deploy --system && \
  apt-get remove -y gcc python3-dev libssl-dev && \
  apt-get autoremove -y && \
  pip uninstall pipenv -y

ADD . /app

EXPOSE 8000

CMD ["pthon", "app.py"]
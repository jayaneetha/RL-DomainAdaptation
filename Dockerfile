FROM jayaneetha/images:tf2.1.0-gpu-py3.6.8-base

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY rl /app/rl
COPY datastores /app/datastores
COPY *.py ./

RUN sudo chown -R user rl
RUN sudo chown -R user datastores
RUN sudo chown user *.py

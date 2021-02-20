FROM python:3.8
LABEL maintainer "George Fiotakis, gfiotakis@core-innovation.com" 

RUN pip3 install numpy 

# TA-Lib
RUN wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz && \
  tar -xvzf ta-lib-0.4.0-src.tar.gz && \
  cd ta-lib/ && \
  ./configure --prefix=/usr && \
  make && \
  make install

RUN rm -R ta-lib ta-lib-0.4.0-src.tar.gz

COPY ./app /app

RUN apt-get install libssl-dev libffi-dev
WORKDIR /app

RUN pip3 install -U setuptools
RUN pip3 install -r requirements.txt

RUN python3 -m pip install dnspython

ENTRYPOINT ["python3", "app.py" ]

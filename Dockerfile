FROM python:3.9-slim

WORKDIR /app

RUN apt-get -y update \
 && apt-get -y install unixodbc-dev \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "main_app_streamlit.py", "--server.port=8501", "--server.address=0.0.0.0"]
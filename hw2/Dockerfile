FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

WORKDIR /app

COPY /artifacts/ /app/

COPY another_module_2_2.py /app/

COPY requirements.txt /app/
RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python3", "another_module_2_2.py"]
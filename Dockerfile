FROM postgres:13

RUN apt-get update && apt-get install -y curl python3-pip

RUN pip3 install patroni[etcd] psycopg2-binary

COPY patroni.yml /opt/patroni.yml

CMD ["patroni", "/opt/patroni.yml"]
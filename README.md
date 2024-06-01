Требования:
    Установленный Docker
    Установленный Docker Compose
    Установленный Python 3 и pip
    Зеркала Docker (если необходимы)

Шаг 1: Подготовка окружения
1. Установите Docker и Docker Compose:

    sudo apt-get update
    sudo apt-get install -y docker.io docker-compose

2. Убедитесь, что Docker и Docker Compose установлены правильно:

    docker --version
    docker-compose --version

3. Настройте зеркала Docker (если необходимы):

Создайте или отредактируйте файл /etc/docker/daemon.json:

    sudo nano /etc/docker/daemon.json

Добавьте следующие строки (пример для зеркала https://mirror.gcr.io):

    {
    "registry-mirrors": ["https://mirror.gcr.io"]
    }

Вы можете заменить https://mirror.gcr.io на любой другой из списка рабочих зеркал:

    https://huecker.io
    https://mirror.gcr.io
    https://daocloud.io
    https://c.163.com/
    https://registry.docker-cn.com

Перезапустите Docker:

    sudo systemctl daemon-reload
    sudo systemctl restart docker

Шаг 2: Подготовка проекта
1. Клонируйте репозиторий с проектом или скопируйте файлы в директорию /opt/postgres-cluster:

    mkdir -p /opt/postgres-cluster
    cd /opt/postgres-cluster

2. Необходимые файлы в директории:

    docker-compose.yml
    haproxy.cfg
    insert_rows.py

3. Создайте необходимые директории для данных PostgreSQL:

    mkdir -p /opt/postgres-cluster/data0
    mkdir -p /opt/postgres-cluster/data1

Шаг 3: Запуск проекта
1. Перейдите в директорию /opt/postgres-cluster:

    cd /opt/postgres-cluster

2. Запустите контейнеры:

    docker-compose up -d

3. Убедитесь, что все контейнеры запущены:

    docker-compose ps

Шаг 4: Запуск скрипта для вставки данных
1. Убедитесь, что у вас установлен модуль psycopg2 для Python:

    pip3 install psycopg2-binary

2. Запустите скрипт для вставки данных:

    python3 /opt/postgres-cluster/insert_rows.py

Шаг 5: Проверка отказоустойчивости
1. Откройте новое окно терминала и остановите один из экземпляров PostgreSQL, например postgres0:

    docker-compose stop postgres0

2. Наблюдайте за скриптом вставки данных в основном окне терминала. Он должен продолжить вставку данных через оставшийся экземпляр postgres1.

3. Перезапустите экземпляр postgres0:

    docker-compose start postgres0

4. Проверьте синхронизацию данных между экземплярами:

    docker exec -it postgres0 psql -U postgres -d postgres -c "SELECT * FROM test_table;"
    docker exec -it postgres1 psql -U postgres -d postgres -c "SELECT * FROM test_table;"

Заключительные шаги
1. Убедитесь, что все контейнеры работают корректно:

    docker-compose ps

2. Проверьте логи контейнеров для проверки возможных ошибок:

    docker-compose logs
# Используем базовый образ, переданный как аргумент
FROM selenium/standalone-chrome:130.0

# Установка Python, pip и необходимых пакетов
USER root
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv openjdk-11-jre && \
    apt-get clean

# Устанавливаем рабочую директорию
WORKDIR /usr/workspace

# Копируем requirements.txt для установки зависимостей
COPY ./requirements.txt /usr/workspace

# Устанавливаем зависимости
RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt || pip3 install -r requirements.txt --break-system-packages
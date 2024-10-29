# Базовый образ
FROM python:3.14.0a1-alpine3.20

# Установка Chrome и ChromeDriver
RUN apk update && \
    apk add --no-cache chromium chromium-chromedriver

# Установка зависимостей для Chrome
RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub && \
    wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.30-r0/glibc-2.30-r0.apk && \
    wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.30-r0/glibc-bin-2.30-r0.apk && \
    apk add --allow-untrusted glibc-2.30-r0.apk glibc-bin-2.30-r0.apk && \
    rm *.apk

# Установка Java и Allure
RUN apk add openjdk11-jre curl tar && \
    curl -o allure-2.13.8.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.8/allure-commandline-2.13.8.tgz && \
    tar -zxvf allure-2.13.8.tgz -C /opt/ && \
    ln -s /opt/allure-2.13.8/bin/allure /usr/bin/allure && \
    rm allure-2.13.8.tgz

# Установка Selenium Server
RUN curl -o selenium-server.jar -Ls https://selenium-release.storage.googleapis.com/4.0/selenium-server-4.0.0.jar

# Настройка рабочего каталога
WORKDIR /usr/workspace
COPY ./requirements.txt /usr/workspace
RUN pip install -r requirements.txt

# Конфигурация запуска
CMD ["java", "-jar", "selenium-server.jar", "node", "--config", "/path/to/node-config.json"]
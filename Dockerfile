FROM python:3.7

RUN apt-get update

RUN curl -sL https://deb.nodesource.com/setup_lts.x | bash -
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y nodejs

WORKDIR /app

COPY . /app

RUN apt-get install python3-pip -y
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

RUN rm -rf node_modules/*
RUN npm install

EXPOSE 8080

CMD ["npm", "start"]
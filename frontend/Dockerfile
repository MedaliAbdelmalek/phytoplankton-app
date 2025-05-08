FROM node:20-slim

WORKDIR /app

COPY package.json ./


RUN yarn install --production=false

COPY . .

CMD ["yarn", "dev"]
FROM node:17-alpine3.12 AS development
ENV NODE_ENV development

#adding a work directory
WORKDIR /frontend

#Cache and Install dependncies
COPY package.json .
COPY yarn.lock .
RUN yarn install

#Copy app files
COPY . .

#Expose port
EXPOSE 3000

#Start the app
CMD ["yarn", "dev"]



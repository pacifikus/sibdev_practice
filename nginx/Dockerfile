FROM python:3.7-slim AS server

RUN mkdir /server
WORKDIR /server

COPY ./server/requirements.txt /server/
RUN pip install -r requirements.txt

COPY ./server /server

RUN python ./manage.py collectstatic

#########################################

FROM nginx:1.13

RUN rm -v /etc/nginx/conf.d/default.conf
COPY ./nginx/nginx.conf /etc/nginx/conf.d

RUN mkdir /nginx
COPY --from=server /server/staticfiles /nginx/static

FROM python
RUN mkdir -p /home/GoFundMe
COPY . /home/GoFundMe
CMD ["python3", "/Users/omarelbasiouny/PycharmProjects/pythonProject1/main.py"]
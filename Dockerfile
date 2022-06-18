FROM python
RUN mkdir -p /home/GoFundMe
COPY . /home/GoFundMe
CMD ["python3","/home/GoFundMe/main.py"]
  
FROM tiangolo/uwsgi-nginx-flask:python3.8
WORKDIR /app/
COPY classifier.pkl .
COPY requirements.txt .
RUN pip install -r ./requirements.txt
#EXPOSE 8000
COPY main.py  /app/
CMD ["python", "main.py"]

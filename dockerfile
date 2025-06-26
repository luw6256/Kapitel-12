FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
#COPY requirements.txt requirements.txt
#RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -r requirements.txt

#COPY ../../data/export.py .
COPY unfassbargutepythonfile.py .


# Definiere den Port, der vom Container freigegeben wird. nur für Docker compose nötig
# EXPOSE 9110

CMD ["python", "unfassbargutepythonfile.py"]
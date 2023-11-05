FROM python:3.8.18-slim
LABEL authors="Bhuvaneshwaran"
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host" ,"0.0.0.0", "--port" ,"8000"]
#ENTRYPOINT ["top", "-b"]
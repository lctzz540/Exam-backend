FROM python:3
WORKDIR /Users/thangle/Documents/test/backend
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["uvicorn","api:app", "--host=0.0.0.0", "--reload"]

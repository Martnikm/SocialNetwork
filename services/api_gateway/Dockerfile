FROM python:3.9
WORKDIR /app
COPY requir.txt .
RUN pip install -r requir.txt
COPY . .
CMD ["python", "app.py"]

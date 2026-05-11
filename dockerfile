FROM python:3.10-slim
WORKDIR /app

# Копируем список зависимостей
COPY requirements.txt .

# Устанавливаем библиотеки внутри образа
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальной код
COPY app.py .

CMD ["python", "app.py"]
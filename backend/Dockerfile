FROM python:3.10-slim

WORKDIR /app

RUN useradd -m myuser
USER myuser

# Копируем список зависимостей
COPY --chown=myuser:myuser requirements.txt .

# Устанавливаем библиотеки внутри образа
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальной код
COPY --chown=myuser:myuser app.py .

USER myuser

CMD ["python", "app.py"]
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV OPENAI_API_KEY=${OPENAI_API_KEY}
ENV DATABASE_URL=${DATABASE_URL}
ENV JWT_SECRET_KEY=${JWT_SECRET_KEY}

CMD ["uvicorn", "api.src.main:app", "--reload"]
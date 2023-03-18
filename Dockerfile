FROM python:3.8 as builder

COPY requirements.txt .

RUN pip install --user -r requirements.txt

FROM python:3.8-slim
WORKDIR /code

COPY --from=builder /root/.local /root/.local
COPY ./bot .

ENV PATH=/root/.local:$PATH

CMD ["python", "main.py"]

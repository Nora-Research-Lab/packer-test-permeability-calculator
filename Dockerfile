FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py packer_test_permeability_calculator.py /app/
EXPOSE 7860
CMD ["python", "app.py"]

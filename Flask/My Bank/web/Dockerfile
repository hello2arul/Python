FROM python:3
WORKDIR /usr/src/app
COPY modules_required.txt ./
RUN pip install --no-cache-dir -r modules_required.txt
COPY . .
CMD [ "python", "app.py" ]

FROM python:3
WORKDIR /usr/src/app
COPY modules_required.txt ./
RUN pip install --no-cache-dir -r modules_required.txt
COPY . .
RUN pip install ./en_core_web_sm-2.0.0.tar.gz
CMD [ "python", "app.py" ]

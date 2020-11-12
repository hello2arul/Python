# pulls a linux image with python install
FROM python
# set a directory to copy the app 
WORKDIR /usr/src/app
# copy the text file with modules to the current working directory
COPY modules_required.txt ./
# recursively install everything in the text file
RUN pip install --no-cache-dir -r modules_required.txt
# copy all the files from the current project to the working directory of the container
COPY . .
# run the app
CMD [ "python", "app.py" ]

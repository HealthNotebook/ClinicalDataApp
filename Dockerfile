FROM python:3.9
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
# Copy the CONTENTS of app, not the folder itself
COPY ./app /code/

# Run main.py directly from the current directory
CMD ["python", "main.py"]
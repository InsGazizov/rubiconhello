    FROM python:3.13-alpine 

    WORKDIR /testpy

    COPY ./testpython.py /testpy

    CMD ["python", "testpython.py"]



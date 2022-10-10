# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip install -r requirement.txt

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

RUN echo "0" > post_requests.txt

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]

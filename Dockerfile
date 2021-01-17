FROM python:3.8.5
LABEL author="Richard Crouch"
LABEL description="Metmini Miscellaneous Functions microservice"

# Generate logs in unbuffered mode
ENV PYTHONUNBUFFERED=1

# Install Python dependencies
RUN pip3 install pipenv
COPY Pipfile* ./
RUN pipenv install --system --deploy

# Copy application and files
RUN mkdir /app
COPY app/*.py /app/
WORKDIR /app

# see value in definitions.py
EXPOSE 9505

# run Python unbuffered so the logs are flushed
CMD ["python3", "-u", "metmini_misc_service.py"]
#CMD ["tail", "-f", "/dev/null"]

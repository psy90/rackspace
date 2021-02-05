FROM python:3.7

MAINTAINER Prashant

# Create app directory
WORKDIR /usr/src/app

# Copy current directory files to working directory
COPY . .

# Run the billing script
CMD [ "python3", "billing_system.py" ]

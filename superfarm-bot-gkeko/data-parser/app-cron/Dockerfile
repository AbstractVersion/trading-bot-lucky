FROM python:3.6-stretch
LABEL mainteiner="George Fiotakis g.fiotakis@core-innovation.com"

USER root
# Add crontab file in the cron directory
ADD crontab /etc/cron.d/script-cron
COPY data-parser.py /cron-script.py

RUN python3 -m venv /opt/venv

COPY requirements.txt /requirements.txt

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/script-cron

RUN chmod 0744 /cron-script.py

# Create the log file to be able to run tail
# RUN touch /var/log/cron.log

#Install Cron -> https://stackoverflow.com/questions/37458287/how-to-run-a-cron-job-inside-a-docker-container
RUN apt-get update -qq
RUN apt-get -y install -qq --allow-remove-essential cron
RUN /opt/venv/bin/pip install -r /requirements.txt
# RUN pip3 install -r /requirements.txt
RUN python3 -m pip install requests

# Run the command on container startup
# CMD [ "cron", "&&", "tail", "-f", "/var/log/cron.log"]
# Instead of wirting the logs to a file on var and tail it out, 
# we persist the script output directely oon the stdout of the container. check the crontab file
CMD ["cron", "-f"]

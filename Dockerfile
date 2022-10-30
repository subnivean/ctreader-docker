FROM python:3.10

RUN apt update && apt upgrade -y

RUN apt install -y python3-serial
#                   python3-rpi.gpio

# UPDATE: Don't run this here - this
# only works from the host machine!
#COPY lcl-rpict-package_latest.deb .
#RUN dpkg -i lcl-rpict-package_latest.deb

COPY requirements.txt .
RUN python -mpip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

#ENV USER appuser
#ENV HOME /home/$USER

#RUN useradd -m -d $HOME -s /bin/bash $USER
RUN mkdir /appdata
#RUN chown $USER.$USER /appdata

#USER $USER

#ENV BASH /bin/bash

#RUN cp /etc/bash.bashrc /root/.bashrc
# This file will have to be re-sourced
# on each login, as far as I can tell
# (the root user is forced into a non-login
# mode)
COPY bash.bash_aliases /root/.bash_aliases

WORKDIR /app
COPY ./src .

CMD ["python", "app.py"]

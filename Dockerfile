FROM ubuntu

EXPOSE 8080
EXPOSE 8888
EXPOSE 80
EXPOSE 4444

ENTRYPOINT ["http://localhost:8888"]

ENV TZ=Europe/Kiev
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /tmp/opencart

COPY . .

RUN apt-get update -y
RUN apt-get install python3-pip -y
RUN apt-get install -y wget xvfb unzip

# We need wget to set up the PPA and xvfb to have a virtual screen and unzip to install the Chromedriver
RUN apt-get install -y --no-install-recommends wget gnupg curl unzip

# Set up the Chrome PPA
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list

# Update the package list and install chrome
RUN apt-get update -y
RUN apt-get install -y google-chrome-stable

# Set up Chromedriver Environment variables
ENV CHROMEDRIVER_VERSION 83.0.4103.39
ENV CHROMEDRIVER_DIR /usr/bin/chromedriver

#Chromedriver might need these packages:
RUN apt-get install libxi6 libgconf-2-4 -y

# Download and install Chromedriver
RUN wget -q --continue -P $CHROMEDRIVER_DIR "http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip"
RUN unzip $CHROMEDRIVER_DIR/chromedriver_linux64.zip -d $CHROMEDRIVER_DIR

RUN chown root:root $CHROMEDRIVER_DIR
RUN chmod +x $CHROMEDRIVER_DIR

# Put Chromedriver into the PATH
ENV PATH $CHROMEDRIVER_DIR:$PATH

RUN apt-get install -y mysql-server
RUN apt-get install -y libmysqlclient-dev

RUN pip3 install -r requirements.txt

CMD ["pytest", "tests/test_main_page.py"]
CMD ["docker container prune -a"]
CMD ["docker image prune -a"]

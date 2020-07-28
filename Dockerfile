FROM joyzoursky/python-chromedriver

WORKDIR /tmp/ticketland

COPY . .

RUN pip3 install -r requirements.txt

RUN pytest -v tests/test_main_page.py --alluredir=logs/allure-log
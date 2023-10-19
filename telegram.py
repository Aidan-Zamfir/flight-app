import requests
import secrets

MSG = "NEW FILE (FlightAPP) TEST 2"


def send_message():
    xx = f"https://api.telegram.org/bot{secrets.TELE_TOK}/sendMessage?chat_id=@{secrets.GROUP_ID}&text={MSG}"
    x = requests.get(xx)


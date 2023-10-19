import requests
import secrets

MSG = "NEW FILE (FlightAPP) TEST"

def main():
    xx = f"https://api.telegram.org/bot{secrets.TELE_TOK}/sendMessage?chat_id=@{secrets.GROUP_ID}&text={MSG}"
    x = requests.get(xx)



if __name__ == "__main__":
    main()
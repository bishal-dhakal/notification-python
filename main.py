import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="Please Drink Water Now",
            message="Water is essentail for human body. Drink enough water",
            app_icon="C:\\Users\\97798\\Downloads\\python\\notification\\glass.ico",
            timeout=10
        )
        time.sleep(60*60)
import time
import pyotp

key = "Algo8.0"

totp = pyotp.TOTP(key)

print(totp.now())

time.sleep(30)

print(totp.now())

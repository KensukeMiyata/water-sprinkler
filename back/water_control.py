import RPi.GPIO as GPIO
import time

# ボタンPIN
Button_PIN = 17
# リレーモジュールPIN
Relay_PIN = 4

# リレー有効の場合はTrue
RELAY_STATUS = False

# 初期化処理
def setup():
    GPIO.setwarnings(True)
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(Button_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(Relay_PIN, GPIO.IN)

# ボタン検知待ち
def button_detect_loop():
    GPIO.add_event_detect(Button_PIN, GPIO.FALLING, callback=button_detect, bouncetime=200)
    while True:
        pass

# ボタン検知
def button_detect(ev=None):
    # ボタン用GPIOのinput値は、押下中=0, 押下なし=1のため
    while not GPIO.input(Button_PIN):
        relay_on()
        time.sleep(0.1)
    
    # 上記ループを抜ける場合リレー状態をOFFにしておく
    relay_off()

# リレーモジュールをONにする
def relay_on():
    global RELAY_STATUS

    if RELAY_STATUS is not True:
        # リレーON
        GPIO.setup(Relay_PIN, GPIO.OUT)
        RELAY_STATUS = True

# リレーモジュールをOFFにする
def relay_off():
    global RELAY_STATUS

    if RELAY_STATUS is not False:
        # リレーOFF
        GPIO.setup(Relay_PIN, GPIO.IN)
        RELAY_STATUS = False

# 終了処理
def destroy():
    GPIO.setup(Relay_PIN, GPIO.IN)
    GPIO.cleanup()

if __name__ == '__main__':
    try:
        # 初期化
        setup()
        # ボタン押下待ち
        button_detect_loop()

    except:
        print("error")
    
    finally:
        destroy()
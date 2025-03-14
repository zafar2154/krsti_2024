import time
from adafruit_servokit import ServoKit
import RPi.GPIO as GPIO

# Inisialisasi objek ServoKit untuk mengontrol PCA9685
kit = ServoKit(channels=16)

# Mengatur frekuensi PWM (biasanya 50Hz untuk servo)
kit.frequency = 250

#pin GPIO
mic_pin =7
GPIO.setmode(GPIO.BCM)
GPIO.setup(mic_pin, GPIO.IN)

kit.servo[6].angle = 180
kit.servo[7].angle = 30

# Mendefinisikan saluran yang digunakan untuk masing-masing servo
servo_channel_1 = 1
servo_channel_2 = 2
servo_channel_3 = 3
servo_channel_4 = 4
servo_channel_0 = 0
servo_channel_8 = 8
servo_channel_9 = 9
servo_channel_11 = 11
servo_channel_12 = 12
servo_channel_13 = 13
servo_channel_14 = 14
servo_channel_15 = 15

def kepala(angle_8, angle_9):
    kit.servo[servo_channel_9].angle = angle_9 #gerakan ke bawah atas
    kit.servo[servo_channel_8].angle = angle_8 #gerakan ke kanan kiri
    
def pundak(angle_4, angle_11):
    kit.servo[servo_channel_4].angle = angle_4 #kanan
    kit.servo[servo_channel_11].angle = angle_11 #kiri

def bahu(angle_3, angle_12):
    kit.servo[servo_channel_3].angle = angle_3 #kanan
    kit.servo[servo_channel_12].angle = angle_12 #kiri

def sikut(angle_2, angle_13):
    kit.servo[servo_channel_2].angle = angle_2 #kanan
    kit.servo[servo_channel_13].angle = angle_13 #kanan

def pergelangan(angle_1, angle_14):
    kit.servo[servo_channel_1].angle = angle_1 #kanan
    kit.servo[servo_channel_14].angle = angle_14 #kiri

#INISIALISASI
kepala(90, 90)
time.sleep(2)
pergelangan(90,90) 
time.sleep(2)
sikut(180,0)
time.sleep(2)
bahu(60,150)
time.sleep(2)
pundak(180,0)
time.sleep(2)
    
def salam() :
    pundak(90,90)
    time.sleep(2)
    bahu(60,150)
    time.sleep(2)
    sikut(90,90)
    time.sleep(2)
    pergelangan(180,0)
    time.sleep(2)
    kepala(90, 180)
    time.sleep(2)
    pass

def INISIALISASI():
    kepala(90, 90)
    time.sleep(2)
    pergelangan(90,90) 
    time.sleep(2)
    sikut(180,0)
    time.sleep(2)
    bahu(60,150)
    time.sleep(2)
    pundak(180,0)
    time.sleep(2)
    pass

def tarian_kupu_kupu():
    pundak(0,180)
    time.sleep(2)
    bahu(30,180)
    time.sleep(2)
    bahu(60,120)
    time.sleep(2)
    bahu(30,180)
    time.sleep(2)
    bahu(60,120)
    time.sleep(2)
    pass

def Loop_utama():
    counter = 0
    while counter < 2 :
        #TAMPOL MUKA
        pundak(50,90)
        time.sleep(2)
        kepala(0, 90)
        time.sleep(2)
        sikut(90,90)
        time.sleep(2)
        kepala(180, 90)
        time.sleep(2)
        pergelangan(0,0)
        time.sleep(2)
        kepala(90, 90)
        time.sleep(2)
        
        #LEBAR
        pergelangan(90,90)
        time.sleep(2)
        sikut(180,0)
        time.sleep(2)
        bahu(0,150)
        time.sleep(2)
        pergelangan(180,180)
        time.sleep(2)
        pergelangan(180,180)
        time.sleep(2)
        pergelangan(90,90)
        time.sleep(2)
        sikut(180,0)
        time.sleep(2)
        bahu(0,150)
        time.sleep(2)
        kepala(180, 90)
        time.sleep(2)
        pergelangan(180,180)
        time.sleep(2)
        kepala(0, 90)
        time.sleep(2)
        pergelangan(180,180)
        time.sleep(2)
        kepala(90, 90)
        time.sleep(2)
        
        #TAMPOL MUKA
        pundak(50,90)
        time.sleep(2)
        kepala(0, 90)
        time.sleep(2)
        sikut(90,90)
        time.sleep(2)
        kepala(180, 90)
        time.sleep(2)
        pergelangan(0,0)
        time.sleep(2)
        kepala(90, 90)
        time.sleep(2)
        
        #LEBAR ATAS
        pergelangan(90,90)
        time.sleep(2)
        sikut(180,0)
        time.sleep(2)
        pundak(180,180)
        time.sleep(2)
        kepala(0, 90)
        time.sleep(2)
        bahu(60,150)
        time.sleep(2)
        kepala(180, 90)
        time.sleep(2)
        pergelangan(180,180)
        time.sleep(2)
        kepala(90, 90)
        time.sleep(2)
        
        #TAMPOL MUKA
        pundak(50,90)
        time.sleep(2)
        kepala(0, 90)
        time.sleep(2)
        sikut(90,90)
        time.sleep(2)
        kepala(180, 90)
        time.sleep(2)
        pergelangan(0,0)
        time.sleep(2)
        kepala(90, 90)
        time.sleep(2)
        
        #LEBAR bawah
        pergelangan(90,90)
        time.sleep(2)
        sikut(180,0)
        time.sleep(2)
        pundak(0,0)
        time.sleep(2)
        kepala(0, 90)
        time.sleep(2)
        bahu(60,150)
        time.sleep(2)
        kepala(180, 90)
        time.sleep(2)
        pergelangan(0,0)
        time.sleep(2)
        kepala(90, 90)
        time.sleep(2)
        counter += 1
        pass
try:   
    while True:
            print("Suara terdeteksi!")
            salam() # Contoh reaksi terhadap deteksi suara
            time.sleep(2)
            INISIALISASI()
            time.sleep(2)
            tarian_kupu_kupu()
            time.sleep(2)
            Loop_utama()
            time.sleep(2)
            INISIALISASI()
            break 
        
except KeyboardInterrupt :
    GPIO.cleanup()
    

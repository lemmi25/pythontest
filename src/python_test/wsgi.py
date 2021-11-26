from greeting import app
import os

os.system('ip link set can0 type can bitrate 500000')
os.system('ip link set can0 up')

if __name__ == "__main__":
    app.run()

import serial
import datetime
import playsound
import pyautogui

timeFormat = "%Y-%m-%d %H:%M:%S.%f"
log = "log.txt"
port = "\\.\\COM3"
ser = serial.Serial(port, 115200, timeout=0)
commands = [b'\x01', b'\x02', b'\x04', b'\x08', b'\x10', b'\x20', b'\x40', b'\x80']
ins = {b'\x01': 1, b'\x02': 2, b'\x04': 3, b'\x08': 4, b'\x10': 5, b'\x20': 6, b'\x40': 7, b'\x80': 8}
recording__ = ["Cmd 1 - switch to scene 1.",  # 切换到场景1
               "Cmd 2 - switch to scene 2.",  # 切换到场景2
               "Cmd 3 - record changed: win +1.",  # 修改战绩：胜场+1
               "Cmd 4 - record changed: lose +1.",  # 修改战绩：负场+1
               "Cmd 5 - record changed: all reset to zero.",  # 修改战绩：归零
               "Cmd 6 - turn on/off mic.",  # 打开/关闭麦克风
               "Cmd 7 - turn on/off camera",  # 打开/关闭摄像头
               "Cmd 8 - start/stop recording."  # 开始/停止录像
               ]
msgs = recording__
wins = 0
loses = 0
recordFile = open("record.txt", "w", encoding="utf8")
recordFile.write("今日战绩\n" + str(wins) + "胜 - " + str(loses) + "负")
recordFile.close()


# window = tk.Tk()
# window.geometry("500x500")


def write_log(fileName, msg: str):
    file = open(fileName, "a+")
    file.write("[" + datetime.datetime.now().strftime(timeFormat)
               + "] " + msg + "\n")
    file.close()


def update_record(filename="record.txt"):
    global wins, loses
    rf = open(filename, "w", encoding="utf8")
    # meaning record file
    rf.write("今日战绩\n" + str(wins) + "胜 - " + str(loses) + "负")
    rf.close()


def press_action(s: bytes):
    global wins, loses
    write_log(log, "String input: " + str(s))
    write_log(log, msgs[ins[s] - 1])
    if ins[s] == 1:
        pyautogui.hotkey('ctrl', 'alt', 'c')
    elif ins[s] == 2:
        pyautogui.hotkey('ctrl', 'alt', 'v')
    elif ins[s] == 3:
        wins += 1
        update_record()
    elif ins[s] == 4:
        loses += 1
        update_record()
    elif ins[s] == 5:
        wins = 0
        loses = 0
        update_record()
    elif ins[s] == 6:
        pyautogui.hotkey('ctrl', 'alt', 'w')
    elif ins[s] == 7:
        pyautogui.hotkey('ctrl', 'shift', 'c')
    elif ins[s] == 8:
        pyautogui.hotkey('ctrl', 'alt', 'e')


with open("log.txt", "w", encoding="utf8") as f:
    f.write("[" + datetime.datetime.now().strftime(timeFormat)
            + "] Connected to serial " + ser.name + "\n")
while True:
    c = ser.read()
    if c in commands:
        press_action(c)

import os
import platform

def shutdown():
    """Завершение работы системы"""
    if platform.system() == "Windows":
        os.system("shutdown /s /t 1")
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        os.system("sudo shutdown -h now")
    else:
        raise NotImplementedError("Команда завершения работы не поддерживается на этой операционной системе")

def reboot():
    """Перезагрузка системы"""
    if platform.system() == "Windows":
        os.system("shutdown /r /t 1")
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        os.system("sudo reboot")
    else:
        raise NotImplementedError("Команда перезагрузки не поддерживается на этой операционной системе")

def sleep():
    """Отправка системы в режим сна"""
    if platform.system() == "Windows":
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    elif platform.system() == "Linux":
        os.system("systemctl suspend")
    elif platform.system() == "Darwin":
        os.system("pmset sleepnow")
    else:
        raise NotImplementedError("Команда сна не поддерживается на этой операционной системе")

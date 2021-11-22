
import time
import sys
import subprocess

from time import sleep

def config_gpio():
        cmd = "/usr/bin/sudo /usr/local/bin/gpio mode 11 in"
        subprocess.check_output(cmd, shell=True)
        cmd = "/usr/bin/sudo /usr/local/bin/gpio mode 11 down"
        subprocess.check_output(cmd, shell=True)
        cmd = "/usr/bin/sudo /usr/local/bin/gpio mode 6 out"
        subprocess.check_output(cmd, shell=True)
        cmd = "/usr/bin/sudo /usr/local/bin/gpio write 6 1"
        subprocess.check_output(cmd, shell=True)


def shut_down():
        print("Shutdown")
        command = "/usr/bin/sudo /sbin/shutdown -h now"
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        cmd = "/usr/bin/sudo /usr/local/bin/gpio write 6 0"
        test = subprocess.check_output(cmd, shell=True).decode(sys.stdout.encoding)
        output = process.communicate()[0]
        print(output)

def main():
        config_gpio()
        while True:
                sleep(5)
                cmd = "gpio read 11 | cut -d' ' -f1"
                Shutdown_Status = subprocess.check_output(cmd, shell=True).decode(sys.stdout.encoding)
                print (int(Shutdown_Status))
                if int(Shutdown_Status) == 0:
                        shut_down()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass

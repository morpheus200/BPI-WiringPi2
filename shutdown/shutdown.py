import time
import sys
import subprocess

from time import sleep


def shut_down():
        print("Shutdown")
        command = "/usr/bin/sudo /sbin/shutdown -h now"
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output = process.communicate()[0]
        print(output)

def main():
        while True:
                sleep(5)
                cmd = "gpio read 11 | cut -d' ' -f1"
                Shutdown_Status = subprocess.check_output(cmd, shell=True).decode(sys.stdout.encoding)
                if int(Shutdown_Status) == 0:
                        shut_down()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass

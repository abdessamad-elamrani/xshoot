# dont forget install paramiko-expect :  pip install paramiko-expect !
import locale

import paramiko
from paramiko_expect import SSHClientInteraction
import logging
from logging.handlers import RotatingFileHandler
import time
from datetime import datetime
import os
from logging.handlers import TimedRotatingFileHandler


class Monitorer:

    def __init__(self, host, user, passwd, sla, commands, iterations, folder_path, size_or_time):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.sla = sla
        self.commands = commands
        self.iterations = iterations
        self.folder_path = folder_path
        self.size_or_time = size_or_time

    def start(self):
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=self.host, username=self.user, password=self.passwd)
        interact = SSHClientInteraction(client, timeout=10, display=False)

        #========== defining and preparing logger ============
        log_formatter = logging.Formatter('%(message)s')
        newdirectory_name = 'Fw__'+self.host+'__'+str(datetime.now().strftime("%d%b-%I%p-%Mmin"))
        #folderpath = "C:\Temp"
        fullpath = self.folder_path + "\\" + newdirectory_name
        os.mkdir(fullpath)
        logpath = fullpath+'\\log'

        #### if logging is TimeBased  ## default is 10min ! need to expose it later
        if self.size_or_time == 't':
            mylogger = logging.getLogger("Rotating Log")
            mylogger.setLevel(logging.INFO)
            # when="m" means seconds ! change to seconds or hours
            handler = TimedRotatingFileHandler(logpath, when="s", interval=5, backupCount=5)
            mylogger.addHandler(handler)

        #### Otherwise its SizeBased
        else:
            my_handler = RotatingFileHandler(logpath, mode='a', maxBytes=5 * 1024,
                                             backupCount=2, encoding=None, delay=0)
            my_handler.setFormatter(log_formatter)
            my_handler.setLevel(logging.INFO)
            mylogger = logging.getLogger('root')
            mylogger.setLevel(logging.INFO)
            mylogger.addHandler(my_handler)

        #======================== Loop Iterations, and Execute and Log commands =====================


        for i in range(self.iterations):
            print("################## starting next iteration ####################")
            print(datetime.now())
            print("#####################################################")

            for x in self.commands:
                interact.send(x)
                interact.expect(".*#.*")
                cmd_output_uname = interact.current_output_clean
                #print(cmd_output_uname)
                mylogger.info(cmd_output_uname)
                # lets sleep for 10sec
                print("")
                print("")
            print("########### waiting ", self.sla, "sec before next iteration #############")
            print(datetime.now())
            print("#####################################################")
            time.sleep(self.sla)
            print("")

        print("\n\n\ndone!\n\n")

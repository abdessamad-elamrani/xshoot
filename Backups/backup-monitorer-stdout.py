# dont forget install paramiko-expect :  pip install paramiko-expect !
import paramiko
import time
from datetime import datetime
from paramiko_expect import SSHClientInteraction


class Monitorer:

    def __init__(self, host, user, passwd, sla, commands, iterations):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.sla = sla
        self.commands = commands
        self.iterations = iterations

    def start(self):
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=self.host, username=self.user, password=self.passwd)
        interact = SSHClientInteraction(client, timeout=10, display=False)

        for i in range(self.iterations):
            print("################## starting next iteration ####################")
            print(datetime.now())
            print("#####################################################")

            for x in self.commands:
                interact.send(x)
                interact.expect(".*#.*")
                cmd_output_uname = interact.current_output_clean
                print(cmd_output_uname)
                # lets sleep for 10sec
                print("")
                print("")
            print("########### waiting ", self.sla, "sec before next iteration #############")
            print(datetime.now())
            print("#####################################################")
            time.sleep(self.sla)
            print("")

        print("\n\n\ndone!\n\n")

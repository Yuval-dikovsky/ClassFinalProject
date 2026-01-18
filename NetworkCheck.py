
"""
Checks network connection
"""

import subprocess
import platform

def network_check():
    """
    Starts a subprocess to check the network connection by pinging google.com. Sends any output to devnull. Catches exception if ping returns a non-zero exit code.
    returns "Connected" if ping works, "Not Connected" otherwise, "Unexpected error" if the ping command cannot be executed or
    another exception occurs.
    """
    try:
        #pings 8.8.8.8 4 times, sending output to devnull and raising error. Tested on Windows Linux and macOS
        if platform.system().lower() == "windows":
            icmp_flag = "-n"
        else:
            icmp_flag = "-c"
        subprocess.run(("ping",icmp_flag, "4", "8.8.8.8"), stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL, check=True)
        return "Connected"
    except subprocess.CalledProcessError:
        return "Not connected"



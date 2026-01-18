
import requests, platform, winreg , psutil, subprocess

"""
Provide the full information about the PC and public IP details
"""
def ip_details():
    """
    return IP details: status,message,country,city,isp,org,proxy,hosting,query
    """
    url = "http://ip-api.com/json/?fields=status,message,country,city,isp,org,proxy,hosting,query"
    #Using http get to retrieve from ip-api API with 5 sec timeout so the program won't hang forever
    res = requests.get(url, timeout=5)
    res_json = res.json()
    details = ""
    for key, value in res_json.items():
        details += f"{key.capitalize()}: {value}\n"
    return details


def get_gpu_model():
    """
    Finds the GPU model based on the specific OS using built in tools in the OS. Works with all gpu vendors.
    return GPU model if successful.
    In case of exception an error string returns
    """
    try:
        match platform.system().lower():
            case "windows":
                #returns the GPU in window
                gpu_windows = subprocess.check_output('powershell -Command "Get-CimInstance -ClassName win32_VideoController | Select-Object -ExpandProperty Name"',shell=True).decode().strip()
                return gpu_windows
            case "linux":
                # returns the GPU in Linux
                gpu_linux = subprocess.check_output("lspci | grep -i -e vga -e display | cut -d'[' -f2 | cut -d']' -f1",shell=True).decode().strip()
                return gpu_linux
            case "darwin":
                # returns the GPU in macOS
                gpu_mac = subprocess.check_output("system_profiler SPDisplaysDataType | grep 'Chipset Model' | cut -d':' -f2 | cut -c2-",shell=True).decode().strip()
                return gpu_mac
                #Other OS aren't supported
            case _:
                return "Unsupported OS"
    except subprocess.CalledProcessError:
        return "Command failed to run"
    except FileNotFoundError:
        return "Required tool to run was not found"
    except Exception as e:
        return f"Error: {e}"

def get_cpu_brand():
    """
    returns cpu brand
    """
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                         r"HARDWARE\DESCRIPTION\System\CentralProcessor\0")
    return winreg.QueryValueEx(key, "ProcessorNameString")[0]

def pc_specs():
    """
    returns pc specs including OS CPU GPU RAM and disk.
    """
    gpu_model = get_gpu_model()
    cpu_brand = get_cpu_brand()
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage("/")
    return (
        f"OS: {platform.system()} {platform.release()}\n"
        f"CPU: {cpu_brand}\n"
        f"GPU: {gpu_model}\n"
        f"Total RAM: {ram.total // (1024 ** 3)}GB\n"
        f"Used RAM: {ram.used // (1024 ** 3)}GB\n"
        f"Free RAM: {ram.free // (1024 ** 3)}GB\n"
        f"Total Storage: {disk.total // (1024 ** 3)}GB\n"
        f"Used Storage: {disk.used // (1024 ** 3)}GB\n"
        f"Free storage: {disk.free // (1024 ** 3)}GB"
    )












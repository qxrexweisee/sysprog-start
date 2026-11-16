
import ctypes

pid = ctypes.windll.kernel32.GetCurrentProcessId()
print(f"agent v0 (python), pid={pid}")
input("Press Enter to exit")

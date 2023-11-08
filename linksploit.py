from exploits import command_line_injection
from exploits import moon_exploit

settings = {
  # default ip and port for Linksys, can be changed using set command
  "target": "192.168.1.1",
  "port": "80",

  # username and password to use for command line injections 
  "username": "admin",
  "password": "admin",

  # default settings for http requests
  "timeout": 10.0,
  "verify": False,
  "allow_redirects" : False,

  # default settings for linksploit
  "exploit" : "moon"
}

def print_settings():
  print()
  for key in settings:
    print(f"{key}: {settings[key]}")
  print()

def change_settings(cmd : str):
  if cmd.count(" ") > 2:
    print("Too many arguments. Expected 'set [setting] [value]")
    return
  elif cmd.count(" ") < 2:
    print("Too few arguments. Expected 'set [setting] [value]")
    return

  _, setting, value = cmd.split(" ")

  if setting not in settings:
    print("Setting does not exist")
    return
  
  try:
    if setting == "exploit" and value not in ["moon", "ping"]:
      print(f"Setting for exploit must be either 'moon' or 'ping'")
      return
    
    if setting == "verify" or setting == "allow_redirects":
      if value.lower() == "true":
        settings[setting] = True
      elif value.lower() == "false":
        settings[setting] = False
      else:
        print(f"Invalid setting for {setting}")
        return

    else:
      settings[setting] = type(settings[setting])(value) # need to preserve the type of the setting

    print(f"{setting} is now set to {settings[setting]}")
  except:
    print(f"Invalid setting for {setting}")



def main():
  while(1):
    cmd = input(">> ")
    exploit = settings["exploit"]

    if cmd == "exit":
      print("Goodbye!")
      return
    elif cmd.startswith("set "):
      change_settings(cmd)
    elif cmd == "settings":
      print_settings()
    elif exploit == "moon":
      moon_exploit(settings = settings, cmd = cmd)
    else:
      command_line_injection(settings = settings, cmd = cmd)

main()

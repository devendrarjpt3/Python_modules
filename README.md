# Python_modules
**import os**
The os module in Python provides a way to interact with the operating system. It allows you to perform tasks such as working with files and directories, managing environment variables, and executing system commands. The module is part of Python's standard library.
  print(os.getcwd())  # Prints the current working directory
  os.chdir("/path/for/change/directory")  # Change the working directory
  print(os.listdir("."))  # Lists all files and folders in the current directory
  os.mkdir("NewFolder")
  #os.rmdir("NewFolder")  # Removes the "NewFolder" directory
File INfo:
  info = os.stat("osModule.py")  # Get file information
  print(info.st_size)  # Prints the file size in bytes
  Executing System Commands:
  os.system("ls -l")  # Runs `ls -l` command in Linux/macOS
  os.system("pwd")
**import sys**
The sys module in Python provides access to system-specific parameters and functions. It allows you to interact with the Python runtime environment, handle command-line arguments, manage standard input/output, and control the interpreter.

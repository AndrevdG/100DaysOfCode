# Creating a virtual environment for python and requirements.txt and using in VS Code
1. Within the subfolder where your project lives: python -m venv .venv
_Optionally you can also provide a path, like python -m venv myfolder/mysubfolder/.venv_
2. You can rightclick your folder in VS Code explorer and select 'open in integrated terminal'. 
You can then run './venv/Scripts/Activate.ps1' to activate the virtual environment
3. In VS Code, press ctrl-shift-p (command palette) and type **python: Select interpreter**. 
Select '.venv/Scripts/python.exe' to bind VS Code to the virtual environment
4. When using requirements.txt to add packages from git, make sure to use https (git port seems blocked?)
for instance: _-e git+https://github.com/jazzband/prettytable.git#egg=prettytable_
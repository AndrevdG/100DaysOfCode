# Creating a virtual environment for python (.venv) 
- Within the subfolder where your project lives: python -m venv .venv
_Optionally you can also provide a path, like python -m venv myfolder/mysubfolder/.venv_
- You can rightclick your folder in VS Code explorer and select 'open in integrated terminal'. 
You can then run './venv/Scripts/Activate.ps1' to activate the virtual environment
- In VS Code, press ctrl-shift-p (command palette) and type **python: Select interpreter**. 
Select '.venv/Scripts/python.exe' to bind VS Code to the virtual environment



# Requirements.txt and using in VS Code
- Installing packages from requirements.txt is done with: pip install -r .\requirements.txt
- When using requirements.txt to add packages from git, make sure to use https (git port seems blocked?)
for instance: _-e git+https://github.com/jazzband/prettytable.git#egg=prettytable_


# Best practise naming convention (from PEP8)
- Use clear and readable naming (not 'a' but 'count')
- Constants should be all caps: MY_GLOBAL_VAR (and are generally defined on module level)
- Class names should use PascalCase: CoffeeMaker
- Function and variable names: lowercase with words seperated by underscores as needed
- Method names and Instance variables: lowercase with words seperated by underscores as needed
- For more specifics, see [Pep8](https://peps.python.org/pep-0008)
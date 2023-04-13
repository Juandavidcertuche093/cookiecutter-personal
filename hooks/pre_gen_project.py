
"""
import os
import sys 

# esto va a remplazar "cookiecutter_personal" del cookiecutter.json
project_slug = "{{ cookiecutter.project_slug }}"

#esto me marca los colores cuando salga erro o cuando este bien (azu o rojo)
ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

#esto nos sirve para cuando haya una x en el nombre del proyecto se ejecute un erro ("x")
if project_slug.startswith("x"):
   print(f"{ERROR_COLOR}ERROR: {project_slug=} is not a valid name for this template.{RESET_ALL}")

   sys.exit(1)



# estos son los mensajes si todo salio bn (en azul)
print(f"{MESSAGE_COLOR}Let's do it! You're are going to create something awesome!")
print(f"Creating project at { os.getcwd() }{RESET_ALL}")   

"""
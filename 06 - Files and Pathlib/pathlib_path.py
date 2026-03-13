#Now we will see the advantages for PATH
from pathlib import Path
ruta_base=Path.home()

# ABSOLUTE route to get to the final file
ruta=Path(ruta_base,"Curso Python","Día 6","practicas_path.py")

# RELATIVE route to get to the final file, does NOT contain the home
ruta=Path("Curso Python","Día 6","practicas_path.py")

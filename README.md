This repository is possibly outdated
Este Repositorio se probablemente se encuentra desactualizado

Repository migrated to https://gitlab.com/fandres323/pyqwt-Temperatura-pinguino
Repositorio migrado a https://gitlab.com/fandres323/pyqwt-Temperatura-pinguino


# Adquisición de datos mediante python, PyQt + pyqwt con la interfaz USB en Modo BULK desde board pinguino.
==============================================================

Un pequeño ejemplo de el uso de la especificación USB en modo BULK “PC – board pinguino” , programando la interfaz gráfica de usuario con PyQt4, pyqwt y programado desde python 2x. 
Usando la board pinguino para adquirir los datos desde un lm35.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

- @author: fAnDrEs					(fabian.salamanca@openmailbox.org)

- class Pinguino by Marin Purgar 				(marin.purgar@gmail.com >>

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Se divide en 5 sesiones

| Sesión | Propósito |
| ------- | --------- |
| sesión 1 |  Se crea la interfaz gráfica con la herramienta Qt Designer[4]. |
| sesión 2 |  Agregando lanzador, clase pinguino y ajustando interfaz. |
| sesión 3 |  Testeando objetos QwtThermo y QLCDNumber. |
| sesión 4 |  Llamada constante (cada 1 segundo) a la funcion de adquicion de datos de la board pinguino |
| sesión 5 |  Adquisición de datos de la board pinguino. |


# REQUERIMIENTOS
 
- Python desde luego 2.x
- PyQt4
- Pyqwt
- Qt4-Designer 
- IDE o cualquier editor de texto
- Board pinguino (Bootlce V2x)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# DOCUMENTACIÓN
 
- PyQt4  -------> https://wiki.python.org/moin/PyQt
- PyQt4 -------> http://pyqt.sourceforge.net/Docs/PyQt4/|_ PyQt4 -------> http://zetcode.com/gui/pyqt4/
- Clases -------> http://pyqt.sourceforge.net/Docs/PyQt4/classes.html|
- pyqwt --------> http://pyqwt.sourceforge.net/
- pykde4 ------> http://api.kde.org/pykde-4.3-api/allclasses.html
- pykde --------> http://techbase.kde.org/Development/Languages/Python


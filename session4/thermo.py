# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 18:28:11 2014

<< Pinguino by Marin Purgar (marin.purgar@gmail.com)                          >>

@author: fAnDrEs
"""

import sys    
# Importar modulo Qt
from PyQt4 import QtCore,QtGui
# Importar el código del modulo compilado UI
from thermoUi import Ui_Form
# Importamos Modulos para el manejo de USB
import usb

#-------------------------------------------------------------------------------
# main
#-------------------------------------------------------------------------------
# Crear una clase para nuestra ventana principal
class Principal(QtGui.QFrame):
    def __init__(self):
        QtGui.QFrame.__init__(self)
        
        # Esto es siempre igual.
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        #Centramos el frame
        self.centrar()
        
        # Conectamos la senal de click del boton (boton_conectar) con el metodo inicio
        self.connect(self.ui.boton_conectar, QtCore.SIGNAL("clicked()"), self.inicio)
                
        
    def inicio(self):
        # Conexcion pinguino
        self.pinguino = Pinguino()
        if self.pinguino.pinguinoOpen() == None:
            print >> sys.stderr, "Unable to open Pinguino device!"
            self.pinguino.pinguinoClose() # Cerrar aplicacion de manera correcta.
        else: 
            # Activamos en la GUI el elemento QWT [qwtThermo]
            self.ui.qwt_Thermo.setEnabled(True) 
            # Cmbiamos el boton_salir a un boton que termine la aplicacion
            #self.ui.boton_conectar.setText("Salir")
            #self.ui.boton_conectar.setToolTip(u"Termina correctamente la Conexión y cierra la aplicación")               
            self.ui.boton_conectar.setEnabled(False)
                    
            # Timer
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.termperatura)
            self.timer.start(1000) #se ejecutará la self.temperatura() cada 1000 mili segundos 
                
        
        
        """ Metodos para qwtTermo """
        #self.ui.qwt_Thermo.setValue(40) # Asigna valor al elemento qwtThermo
        #self.ui.qwt_Thermo.setPipeWidth(20) # Cambia anchura del pipe(barra termomentro)
        #self.ui.qwt_Thermo.setAlarmLevel(50) Cambia el nivel de alarma [entero]
        #self.ui.qwt_Thermo.setAlarmColor(QtGui.QColor(0, 177, 0)) # cambia el Color de la ararma
        #print self.ui.qwt_Thermo.alarmEnabled() # retorna True si existe alarma
        #print self.ui.qwt_Thermo.alarmLevel() # Retorna el valor en el cual se activa la alarma

        # Cambio alarm Brush de alarm
        #brush = QtGui.QBrush(QtGui.QColor(0 , 0, 170))
        #brush.setStyle(QtCore.Qt.SolidPattern)
        #self.ui.qwt_Thermo.setAlarmBrush(brush)
        
        """Metodos QLCDNumber """
        #self.ui.lcdNumber_1.display(60) # Muestra un valor en el LCD
        # Sinal = overFlow
        #print self.ui.lcdNumber_1.value() # Retorta valor de QLCDNumber
        #print self.ui.lcdNumber_1.intValue() # Recorta valor de QLCDNumber en entero
        #self.ui.lcdNumber_1.setDisabled(True)# Desactiva el LCD
        #self.ui.lcdNumber_1.setNumDigits(1) # Numero de digitos que muestra el LCD
        #print self.ui.lcdNumber_1.numDigits()  # Numero de digitos que esta mostrando el LCD
        


#-------------------------------------------------------------------------------
    def centrar(self):
            screen = QtGui.QDesktopWidget().screenGeometry() # obtiene resolucion del usuario
            size =  self.geometry() 
            self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
            
#-------------------------------------------------------------------------------
    def termperatura(self):
        self.INTERVAL = 100 # intervalo (tiempo) de lectura 
        deg = unichr(176).encode("utf-8")
        self.myString = ''

        # Obtiene los datos de la targeta Pinguino 
        try :
            for i in self.pinguino.pinguinoRead(2, self.INTERVAL):
                self.myString += chr(i)
                
        except usb.USBError as err:
            pass

        #print  "Valor que llega",self.myString  #debug
        #print type(self.myString) #debug
        #print int(self.myString) #debug
        if len(self.myString) > 0:
            #print "entro" #debug
            self.termperatura = int(self.myString)
            self.ui.qwt_Thermo.setValue(self.termperatura) # Asigna valor al elemento qwtThermo
            self.ui.lcdNumber_1.display(self.termperatura) # Muestra un valor en el LCD
            # Calculamos la diferencia entre la alarma y el valor mostrado 
            if (self.ui.lcdNumber_1.value() - self.ui.qwt_Thermo.alarmLevel())  > 0 :
                self.ui.lcdNumber_2.display(self.ui.lcdNumber_1.value() - self.ui.qwt_Thermo.alarmLevel()) 
            
            
            
#-------------------------------------------------------------------------------
# Pinguino Class by Marin Purgar (marin.purgar@gmail.com)
#-------------------------------------------------------------------------------

class Pinguino():

    VENDOR = 0x04D8
    PRODUCT = 0xFEAA
    #CONFIGURATION = 0x01 # if bootloader v4.x
    CONFIGURATION = 0x03 # if bootloader v2.x
    #print type(CONFIGURATION)
    INTERFACE = 0
       #ENDPOINT_IN = 0x81 # if bootloader v4.x
    ENDPOINT_IN = 0x82 # if bootloader v2.x
    ENDPOINT_OUT = 0x01

    device = None
    handle = None

    def __init__(self,):
        for bus in usb.busses():
            #print usb.busses()
            for dev in bus.devices:
                #print "vendor",dev.idVendor
                #print "idproduct",dev.idProduct
                if dev.idVendor == self.VENDOR and dev.idProduct == self.PRODUCT:
                    self.device = dev
        return None

    def pinguinoOpen(self):
        if not self.device:
            print >> sys.stderr, "Unable to find device!"
            return None
        try:
            self.handle = self.device.open()
            self.handle.setConfiguration(self.CONFIGURATION)
            self.handle.claimInterface(self.INTERFACE)
        except usb.USBError, err:
            print >> sys.stderr, err
            self.handle = None
        return self.handle

    def pinguinoClose(self):
        try:
            self.handle.releaseInterface()
        except Exception, err:
            print >> sys.stderr, err
        self.handle, self.device = None, None

    def pinguinoRead(self, length, timeout = 0):
        return self.handle.bulkRead(self.ENDPOINT_IN, length, timeout)

    def pinguinoWrite(self, buffer, timeout = 0):
        return self.handle.bulkWrite(self.ENDPOINT_OUT, buffer, timeout)
        
#-------------------------------------------------------------------------------
# 
#-------------------------------------------------------------------------------
def main():
    # Nuevamente, esto es estándar, será igual en cada
    # aplicación que escribas
    app = QtGui.QApplication(sys.argv)
    # Se crea una instancia de la clase
    ventana=Principal()
    # Se muestra el elemento en pantalla
    ventana.show()
    # Se ejecuta y expera a que termine la aplicación
    sys.exit(app.exec_())
    # Cierra la conexcion con el pinguino Correctamente
    Pinguino.pinguinoClose()

if __name__ == "__main__":
    main()
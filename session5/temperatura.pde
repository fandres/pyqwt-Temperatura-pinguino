/*-----------------------------------------------------
Author:  --<fandres>
Date: 2014-04-03
Description: Adquiere informacion de un lm35 y lo envia a host.Pro
Programa Host [Python]: https://github.com/fandres/pyqwt-Temperatura-pinguino/tree/master/session5
-----------------------------------------------------*/


#include <stdlib.h>   // la necesitaremos para la función "itoa()"

char enviado[64];   // Cadena a ser enviada.
int entero = 0;     // Donde almacenamos temporalmente el valor leido.

void setup()
{
    pinMode(13, INPUT);  // pin 13 de la board pinguino como salida.
}

//-------------------------loop()---------------------//
void loop()
{
    
    entero = analogRead(13);    // Leyendo del Pin13
    itoa(entero,enviado,10);    // Conversión de int a string
    BULK.write(enviado, 4);    // Enviado los datos al host
    delay(500);                // Esperamos 500 milisegundos. 
}

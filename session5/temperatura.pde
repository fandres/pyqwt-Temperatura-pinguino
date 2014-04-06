/*-----------------------------------------------------
Author:  --<fandres>
Date: 2014-04-03
Description:lm35....
first release	14/09/2010
last update	17/07/2013

-----------------------------------------------------*/

//int temperatura;
int entero;
unsigned char caracter;

void setup()
{
    entero = 0;
    caracter = 0;
    pinMode(13, INPUT);  
    
    pinMode(0,OUTPUT);
    digitalWrite(0,LOW);
}

void loop()
{
    //temperatura = analogRead(13); 

    entero = 50;
    caracter = (unsigned char)entero;
    
    USB.send(caracter, 2);
    
    digitalWrite(0,HIGH);
    toggle(USERLED);
    delay(1000);
			

}

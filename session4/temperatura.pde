/*-----------------------------------------------------
Author:  --<fandres>
Date: 2014-04-03
Description:lm35....
first release	14/09/2010
last update	17/07/2013

-----------------------------------------------------*/


void setup()
{
    pinMode(13, INPUT);  
}

void loop()
{
    analogRead(13); 
    USB.send("60", 2);			// send 15 bytes on usb bus
    toggle(USERLED);		                    // blinked user led for visual debug
    delay(1000);			                      // wait for 1 sec. before next sending
}

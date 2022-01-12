#include <TM1638plus.h>
TM1638plus tm(D7, D6, D5, false);

uint8 lastInput = 0b11111111;

void setup()
{
    tm.displayBegin();
    Serial.begin(115200);
    for (int i = 0; i < 8; i++)
    {
        tm.displayHex(i, 0);
    }
}

void loop()
{
    uint8 key = tm.readButtons();
    if(key != 0 && key != lastInput)
        Serial.write(key);
        lastInput = key;
}

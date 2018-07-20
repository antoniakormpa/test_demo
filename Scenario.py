# This example will set one of our Testboard's outputs, which has a DAC controller that allows it to output an analog value of anywhere from 0 to 3.3V.
#
# The goal of this example is to show you how you can drive an analog input on your device from the Testboard. 
#
# In our particular example, we are only setting a value and not asserting anything. Of course this would never be a real world example, it's only for educational purposes

import time
from Spanner import Spanner
from Testboard import Testboard


TESTBOARD_ID = "250020001047343438323536"

testboard = Testboard(TESTBOARD_ID)

DAC1 = "A4"

def set_analog_output():
    # Our Product's Input will be connected the Testboard's Pin A6, which is where the DAC1 output is.
    # In this example, let's say we want to give out 2V. Our analogWrite value can be from 0 to 4095, which corresponds to a range of 0-3.3V. By doing the calculation (2/3.3*4096), we get a value of about 2482.
    value = testboard.analogWrite(DAC1, 2482)
    print(value)

if __name__ == "__main__":

    set_analog_output()

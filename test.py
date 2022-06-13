from rpi_rf import RFDevice
import click
def cmd_to_code(argument):
    switcher={
     "A":3158956,
     "a":3985788,
     "B":4020981,
     "b":3533717,
     "C":3886478,
     "c":3564062,
    }
    return switcher.get(argument,0)
rfdevice = RFDevice(15)
rfdevice.enable_tx()
rfdevice.tx_repeat = 10
cmd=" "
print ("Command [A,a,B,b,C,c] [x,X] for exit")
while not (cmd=='x' or cmd=='X'):
    cmd=click.getchar()
    code=cmd_to_code(cmd)
    if (code>0):
        print ("command ",cmd,"code", code)
        rfdevice.tx_code(code, 4)

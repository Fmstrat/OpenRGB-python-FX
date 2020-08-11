import openrgb , time , RGBModes
from openrgb.utils import DeviceType , RGBColor , ModeData , ModeColors , ModeDirections

client = openrgb.OpenRGBClient()

Dlist = client.devices

def SetDeviceColors(R , G , B):#device , led , R , G , B):
    for i in Dlist:
        i.set_color(RGBColor(R,G,B))
        time.sleep(0.0003)

def wait():
    time.sleep(0.003)

def DebugRGB(R , G , B):
    Debug = 0
    if Debug == 1:
        print(R , G , B)
    else:
        return


def SpectrumCycle():
    for Device in Dlist:
        Device.set_mode(RGBModes.SupportedModes(Device.name , 'cycling'))
        wait()

def Rainbow():
    for Device in Dlist:
        Device.set_mode(RGBModes.SupportedModes(Device.name , 'rainbow'))
        wait()

# This section is for custom modes
def CustomSpectrumCycle():
    R = G = B = 0
    RedoLoop = 0
    while 1 == 1:
        if RedoLoop == 1:
            RedoLoop = 0
        R += 1
        DebugRGB(R , G , B)
        SetDeviceColors(R , G , B)
        time.sleep(0.001)
        if R == 255:
            while 1 == 1:
                if RedoLoop == 1:
                    break
                G += 1
                DebugRGB(R , G , B)
                SetDeviceColors(R , G , B)
                time.sleep(0.001)
                if G == 255:
                    while 1 == 1:
                        if RedoLoop == 1:
                            break
                        R -= 1
                        DebugRGB(R , G , B)
                        SetDeviceColors(R , G , B)
                        time.sleep(0.001)
                        if R == 0:
                            while 1 == 1:
                                if RedoLoop == 1:
                                    break
                                B += 1
                                DebugRGB(R , G , B)
                                SetDeviceColors(R , G , B)
                                time.sleep(0.001)
                                if B == 255:
                                    while 1 == 1:
                                        if RedoLoop == 1:
                                            break
                                        G -= 1
                                        DebugRGB(R , G , B)
                                        SetDeviceColors(R , G , B)
                                        time.sleep(0.001)
                                        if G == 0:
                                            while 1 == 1:
                                                if RedoLoop == 1:
                                                    break
                                                R += 1
                                                DebugRGB(R , G , B)
                                                SetDeviceColors(R , G , B)
                                                time.sleep(0.001)
                                                if R == 255:
                                                    while 1 == 1:
                                                        if RedoLoop == 1:
                                                            break
                                                        B -= 1
                                                        DebugRGB(R , G , B)
                                                        SetDeviceColors(R , G , B)
                                                        time.sleep(0.001)
                                                        if B == 0:
                                                            while 1 == 1:
                                                                if RedoLoop == 1:
                                                                    break
                                                                G += 1
                                                                B += 1
                                                                DebugRGB(R , G , B)
                                                                SetDeviceColors(R , G , B)
                                                                time.sleep(0.001)
                                                                if (str(R) + str(G) + str(B)) == "255255255":
                                                                    while 1 == 1:
                                                                        R -= 1
                                                                        G -= 1
                                                                        B -= 1
                                                                        DebugRGB(R , G , B)
                                                                        SetDeviceColors(R , G , B)
                                                                        time.sleep(0.001)
                                                                        if B == 0:
                                                                            RedoLoop = 1
                                                                            break
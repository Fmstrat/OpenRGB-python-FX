import sys, openrgb, time, random, colorsys
from openrgb.utils import RGBColor
client = openrgb.OpenRGBClient()

def CreateCBase(): #this is only to stop errors from appearing in this file, it is NOT a template
    return [1,2,3]

#---------------------Color Base generators----------------------------------
def CreateCBaseFTB(C = (255,255,255)):
    """Creates a data base of 255 colors to index for use later\n
    So you can grab an RGB color with ``Cbase[num]`` and have a color code\n
    I am not sure if this makes it faster or not but I would assume since it doesn't have to do the math to find out what color it should be
    """
    RunThrough = 0 # determines the amount of passes made
    DevideBase = 0 # the highest value of C (RGB color code)
    BaseC = C #to preserve C for use later (mostly for devision)
    CBase = [] # an empty list to drop the color base into
    for i in C:
        if i > DevideBase:
            DevideBase = i # Redefines DevideBase to be the actually highest instead of 0
    while (C[0] + C[1] + C[2]) > 0: # create a color base for the effect for use later until all three added is == 0 (fade to black)
        AddC = []
        for i in C:
            if (BaseC[C.index(i)] != 0) & (int(BaseC[C.index(i)]) != int(DevideBase)): # the first portion ensure that it isn't trying to devide by 0. the second is to ensure that it doesn't try to devide a number by itself and waste time
                if RunThrough % int(DevideBase / BaseC[C.index(i)]) == 0: # I forgot how this works but it does
                    i -= 1
            else:
                if i > 0: # only subtract if it is greater than 0 (to avoid the SDK yelling at me)
                    i -= 1 # subtract
            AddC = AddC + [i] # add all the numbers together again to get the color code
        RunThrough += 1 # increase the pass amount
        #print(AddC) # print the color code for debugging (will be commented for release)
        C = AddC # This is neccisary for ensure it doesn't get stuck in a loop due to it comparing a static value in the While loop
        CBase = CBase + [C]
    return CBase
# ^ This one is Fade to black (you can reverse from black to original using reverse(Cbase) )

def CreateCBaseRainbow(CycleSpeed=15):
    Cbase = []
    CycleSpeed = 300
    hue_range = CycleSpeed
    for i in range(hue_range):
        color = colorsys.hsv_to_rgb(i / hue_range, 1.0, 1.0)

        # Split RGB values
        R = int(color[0] * 255)
        G = int(color[1] * 255)
        B = int(color[2] * 255)
        Cbase += [RGBColor(R,G,B)]
    return(Cbase)
#rainbow wave creation

#---------------------User input---------------------------------------------

def UserInput():
    """It will always return 5 things;\n
    Color1, Color2, Speed, Devices for reversal, Devices that are enables in the form of\n
    None/int, None/int, None/int, None/list, None/list. None is for a blank argument so make sure you add ``if == none`` to catch it"""
    Color1 = Color2 = Speed = ReversedDevice = OnlySet = None
    for arg in sys.argv:
        if arg == '--C1':
            Pos = sys.argv.index(arg) + 1
            R, G, B = sys.argv[Pos:(Pos + 3)]
            Color1 = RGBColor(int(R),int(G),int(B))
        elif arg == '--C2':
            Pos = sys.argv.index(arg) + 1
            R, G, B = sys.argv[Pos:(Pos + 3)]
            Color2 = RGBColor(int(R),int(G),int(B))
        elif arg == '--reversed':
            ReversedDevices = (sys.argv.index(arg) + 1) # Will point to where the device(s) that need to be reversed are
            ReversedDevice = []
            if ' , ' in sys.argv[ReversedDevices]:
                for i in sys.argv[ReversedDevices].split(' , '):
                    for D in client.devices:
                        if D.name.strip().casefold() == i.strip().casefold():
                            ReversedDevice += [D]
            else:
                for D in client.devices:
                    if D.name.strip().casefold() == sys.argv[ReversedDevices].strip().casefold():
                        ReversedDevice += [D]
        elif arg == '--only-set':
            AllowedDevices = (sys.argv.index(arg) + 1) # Will point to where the device(s) that are allowed are
            OnlySet = []
            if ' , ' in sys.argv[AllowedDevices]:
                for i in sys.argv[AllowedDevices].split(' , '):
                    for D in client.devices:
                        if D.name.strip().casefold() == i.strip().casefold():
                            OnlySet += [D]
            else:
                for D in client.devices:
                    if D.name.strip().casefold() == sys.argv[AllowedDevices].strip().casefold():
                        OnlySet += [D]
        elif arg == '--speed':
            Speed = int(sys.argv[(sys.argv.index(arg) + 1)])
        else:
            pass
    return(Color1, Color2, Speed, ReversedDevice, OnlySet)

#---------------------Set to Static------------------------------------------
def SetStatic(Dlist):
    """A quick function I use to make sure that everything is in direct or static mode"""
    for Device in Dlist:
        time.sleep(0.1)
        try:
            Device.set_mode('direct')
            print('Set %s successfully'%Device.name)
        except:
            try:
                Device.set_mode('static')
                print('error setting %s\nfalling back to static'%Device.name)
            except:
                print("Critical error! couldn't set %s to static or direct"%Device.name)
# Some notes on this one ^
# time is a module that you need to import to use this
# Client is what I name a variable (client = openrgb.OpenRGBClient())

#-------------------Random color generator-----------------------------------
def RandomColor(MinVal=200):
    """
    MinVal will be the smallest number you are ok with
    The higher the number, the brighter the resulting color will be
    """
    while True:
        CR = random.randint(0,255)
        CG = random.randint(0,255)
        CB = random.randint(0,255)
        if (CR + CG + CB) >= MinVal:
            return CR, CG, CB
# You need to have "random" imported for this one
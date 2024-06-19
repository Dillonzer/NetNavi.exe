
from consts import Consts
from chips import Chips
from crust import Crust
from program_advance import ProgramAdvance

class NetNavi():
    def __init__(self):
        self.token = Consts.TOKEN
        self.botId = Consts.BOT_ID

        self.chipDict = {}
        self.chipDict[Consts.BN1] = Chips(Consts.BN1)
        self.chipDict[Consts.BN2] = Chips(Consts.BN2)
        self.chipDict[Consts.BN3] = Chips(Consts.BN3)
        self.chipDict[Consts.BN4] = Chips(Consts.BN4)
        self.chipDict[Consts.BN5] = Chips(Consts.BN5)
        self.chipDict[Consts.BN6] = Chips(Consts.BN6)  

        self.crustDict = {}
        self.crustDict[Consts.BN3] = Crust(Consts.BN3)
        self.crustDict[Consts.BN4] = Crust(Consts.BN4)
        self.crustDict[Consts.BN5] = Crust(Consts.BN5)
        self.crustDict[Consts.BN6] = Crust(Consts.BN6) 
        
        self.paDict = {}
        self.paDict[Consts.BN1] = ProgramAdvance(Consts.BN1)
        self.paDict[Consts.BN2] = ProgramAdvance(Consts.BN2)
        self.paDict[Consts.BN3] = ProgramAdvance(Consts.BN3)
        self.paDict[Consts.BN4] = ProgramAdvance(Consts.BN4)
        self.paDict[Consts.BN5] = ProgramAdvance(Consts.BN5)
        self.paDict[Consts.BN6] = ProgramAdvance(Consts.BN6) 


    
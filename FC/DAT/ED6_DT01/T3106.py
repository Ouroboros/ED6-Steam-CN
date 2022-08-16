import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3106_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3106   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3106.x'
    header.mapIndex       = 1
    header.bgm            = 92
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000000,
            dword_08        = 0x00001770,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 45,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 0,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10000 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
    ]

# id: 0x10001 offset: 0xCA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '人',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '人',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '人',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '人',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x14A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x14A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x14A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x14A
@scena.Code('Init')
def Init():
    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_02_16F)

    Return()

# id: 0x0001 offset: 0x152
@scena.Code('func_01_152')
def func_01_152():
    OP_6F(0x000D, 40)
    OP_70(0x000D, 0)
    OP_6F(0x000B, 0)
    OP_70(0x000B, 40)

    Return()

# id: 0x0002 offset: 0x16F
@scena.Code('func_02_16F')
def func_02_16F():
    EventBegin(0x00)
    CameraMove(42710, 0, 50480, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(9130, 0)
    OP_6C(225000, 0)
    OP_6E(369, 0)
    FadeIn(2000, 0)
    OP_6C(235000, 4000)
    Fade(1000)
    MapSetFlags(0x00000001)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0000, 0x0004)
    ChrSetPos(0x0000, 58530, 0, 24930, 0)
    CameraMove(58530, 0, 24930, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3460, 0)
    OP_6C(225000, 0)
    OP_6E(369, 0)
    OP_0D()
    Fade(2000)
    OP_71(0x002E, 0x0004)
    OP_71(0x0037, 0x0004)
    OP_79(0x00, 0x0002)
    OP_79(0x01, 0x0002)
    OP_79(0x02, 0x0002)
    OP_79(0x04, 0x0002)
    OP_79(0x03, 0x0002)
    OP_79(0x0B, 0x0002)
    OP_79(0x05, 0x0002)
    OP_79(0x06, 0x0002)
    OP_79(0x07, 0x0002)
    OP_79(0x08, 0x0002)
    OP_79(0x09, 0x0002)
    OP_79(0x0A, 0x0002)
    OP_79(0x0C, 0x0002)
    OP_7B()
    OP_0D()

    @scena.Lambda('lambda_026E')
    def lambda_026E():
        ChrWalkTo(0x0000, 58870, 0, 56450, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_026E)

    OP_72(0x0026, 0x0004)
    Sleep(100)

    @scena.Lambda('lambda_0293')
    def lambda_0293():
        ChrWalkTo(0x0000, 58870, 0, 56450, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0293)

    OP_71(0x002F, 0x0004)
    Sleep(100)

    @scena.Lambda('lambda_02B8')
    def lambda_02B8():
        ChrWalkTo(0x0000, 58870, 0, 56450, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_02B8)

    OP_72(0x003D, 0x0004)
    Sleep(100)

    @scena.Lambda('lambda_02DD')
    def lambda_02DD():
        ChrWalkTo(0x0000, 58870, 0, 56450, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_02DD)

    OP_71(0x0008, 0x0004)
    Sleep(200)

    @scena.Lambda('lambda_0302')
    def lambda_0302():
        ChrWalkTo(0x0000, 58870, 0, 59000, 16000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0302)

    OP_71(0x001E, 0x0004)
    Sleep(200)

    OP_72(0x0027, 0x0004)
    Sleep(100)

    OP_71(0x0030, 0x0004)
    Sleep(100)

    OP_72(0x003A, 0x0004)
    Sleep(100)

    OP_71(0x0005, 0x0004)
    Sleep(100)

    OP_71(0x001D, 0x0004)
    Sleep(200)

    OP_71(0x001C, 0x0004)
    Sleep(200)

    OP_72(0x0028, 0x0004)
    Sleep(100)

    OP_71(0x0031, 0x0004)
    Sleep(100)

    OP_72(0x003F, 0x0004)
    Sleep(100)

    OP_71(0x000A, 0x0004)
    Sleep(100)

    OP_71(0x001B, 0x0004)
    Sleep(100)

    OP_71(0x001A, 0x0004)
    Sleep(200)

    WaitForThreadExit(0x0000, 0x0001)
    Fade(1000)
    OP_6C(270000, 0)

    @scena.Lambda('lambda_03B2')
    def lambda_03B2():
        ChrWalkTo(0x0000, 5050, 0, 59070, 14000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_03B2)

    Sleep(800)

    OP_72(0x0029, 0x0004)
    Sleep(100)

    OP_71(0x0032, 0x0004)
    Sleep(100)

    OP_71(0x0019, 0x0004)
    Sleep(200)

    OP_72(0x002A, 0x0004)
    Sleep(100)

    OP_71(0x0033, 0x0004)
    Sleep(200)

    OP_72(0x002B, 0x0004)
    Sleep(100)

    OP_71(0x0034, 0x0004)
    Sleep(100)

    OP_71(0x0018, 0x0004)
    Sleep(200)

    OP_72(0x002C, 0x0004)
    Sleep(100)

    OP_71(0x0035, 0x0004)
    Sleep(100)

    OP_72(0x003E, 0x0004)
    Sleep(100)

    OP_71(0x0009, 0x0004)
    Sleep(100)

    OP_71(0x0017, 0x0004)
    Sleep(200)

    OP_72(0x002D, 0x0004)
    Sleep(100)

    OP_71(0x0036, 0x0004)
    Sleep(100)

    OP_72(0x002E, 0x0004)
    Sleep(100)

    OP_71(0x0039, 0x0004)
    Sleep(100)

    OP_72(0x003B, 0x0004)
    Sleep(100)

    OP_71(0x0006, 0x0004)
    Sleep(100)

    OP_72(0x003C, 0x0004)
    Sleep(100)

    OP_71(0x0007, 0x0004)
    Sleep(100)

    OP_71(0x001F, 0x0004)
    Sleep(200)

    PlaySE(91, 0x01, 0x64)
    OP_71(0x0016, 0x0004)
    Sleep(100)

    OP_71(0x0015, 0x0004)
    Sleep(200)

    OP_71(0x0014, 0x0004)
    Sleep(100)

    OP_71(0x0013, 0x0004)
    Sleep(200)

    @scena.Lambda('lambda_04DB')
    def lambda_04DB():
        ChrWalkTo(0x0000, 5050, 0, 59070, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_04DB)

    OP_71(0x0012, 0x0004)
    Sleep(100)

    @scena.Lambda('lambda_0500')
    def lambda_0500():
        ChrWalkTo(0x0000, 5050, 0, 59070, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0500)

    OP_71(0x0011, 0x0004)
    Sleep(200)

    @scena.Lambda('lambda_0525')
    def lambda_0525():
        ChrWalkTo(0x0000, 5050, 0, 59070, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0525)

    OP_71(0x0010, 0x0004)
    Sleep(100)

    @scena.Lambda('lambda_054A')
    def lambda_054A():
        ChrWalkTo(0x0000, 5050, 0, 59070, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_054A)

    OP_71(0x000F, 0x0004)
    Sleep(200)

    @scena.Lambda('lambda_056F')
    def lambda_056F():
        ChrWalkTo(0x0000, 5050, 0, 59070, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_056F)

    Sleep(100)

    TerminateThread(0x0000, 0x01)
    Sleep(500)

    OP_23(0x005B)
    PlaySE(154, 0x00, 0x64)
    OP_7C(0, 100, 3000, 100)
    OP_72(0x000D, 0x0008)
    OP_72(0x000B, 0x0008)
    OP_6F(0x000D, 0)
    OP_6F(0x000B, 0)
    OP_70(0x000D, 0)
    OP_70(0x000B, 0)
    OP_72(0x000D, 0x0020)
    OP_72(0x000B, 0x0020)
    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(1000)

    MapClearFlags(0x00000001)
    ChrSetPos(0x0008, 16280, 0, 62960, 309)
    ChrSetPos(0x0009, 17870, 0, 53190, 180)
    ChrSetPos(0x000A, 17870, 0, 53190, 180)
    ChrSetPos(0x000B, 36140, 500, 52730, 180)
    ChrSetFlags(0x0008, 0x0040)
    ChrSetFlags(0x0009, 0x0040)
    ChrSetFlags(0x000A, 0x0040)
    ChrSetFlags(0x000B, 0x0040)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetFlags(0x0009, 0x0004)
    ChrSetFlags(0x000A, 0x0004)
    ChrSetFlags(0x000B, 0x0004)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    CameraMove(31790, 0, 58850, 0)
    OP_67(0, 2430, -10000, 0)
    CameraSetDistance(4190, 0)
    OP_6C(264000, 0)
    OP_6E(369, 0)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_06C1')
    def lambda_06C1():
        CameraMove(11640, 0, 59040, 10000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_06C1)

    @scena.Lambda('lambda_06D9')
    def lambda_06D9():
        OP_6C(270000, 10000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_06D9)

    OP_0D()
    Sleep(2000)

    OP_72(0x003E, 0x0010)
    OP_70(0x003E, 100)
    Sleep(400)

    CreateThread(0x000B, 0x01, 0x00, func_06_864)
    Sleep(1000)

    OP_72(0x003B, 0x0010)
    OP_70(0x003B, 100)
    Sleep(500)

    CreateThread(0x0009, 0x01, 0x00, func_04_7B7)
    Sleep(500)

    OP_72(0x003C, 0x0010)
    OP_70(0x003C, 100)
    CreateThread(0x0008, 0x01, 0x00, func_03_759)
    Sleep(500)

    CreateThread(0x000A, 0x01, 0x00, func_05_804)
    Sleep(3000)

    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T3172._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x759
@scena.Code('func_03_759')
def func_03_759():
    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrWalkTo(0x00FE, 15890, 0, 59960, 3000, 0x00)
    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrSetDirection(0x00FE, 284, 400)
    Sleep(1000)

    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrSetDirection(0x00FE, 96, 400)

    Return()

# id: 0x0004 offset: 0x7B7
@scena.Code('func_04_7B7')
def func_04_7B7():
    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrWalkTo(0x00FE, 18050, 0, 55260, 2000, 0x00)
    ChrWalkTo(0x00FE, 15280, 0, 56560, 2000, 0x00)
    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    Return()

# id: 0x0005 offset: 0x804
@scena.Code('func_05_804')
def func_05_804():
    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrWalkTo(0x00FE, 18050, 0, 55260, 3000, 0x00)
    ChrWalkTo(0x00FE, 17840, 0, 55930, 3000, 0x00)
    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(500)

    ChrTurnDirection(0x0009, 0x00FE, 400)
    ChrTurnDirection(0x00FE, 0x0009, 400)

    Return()

# id: 0x0006 offset: 0x864
@scena.Code('func_06_864')
def func_06_864():
    ChrWalkTo(0x00FE, 35930, 500, 54150, 2000, 0x00)
    ChrClearFlags(0x00FE, 0x0004)
    ChrWalkTo(0x00FE, 36290, 0, 55350, 2000, 0x00)
    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrSetDirection(0x00FE, 90, 400)
    ChrSetDirection(0x00FE, 90, 270)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T1501_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1501   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, 'New Ansel Path'),
    TXT(0x02, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1501.x'
    header.mapIndex       = 1
    header.bgm            = 84
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x29D
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
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

# id: 0x10001 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
    ]

# id: 0x10002 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -8640,
            z                   = 0,
            y                   = 96040,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0xC8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0xC8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0xC8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xC8
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_DE',
    )

    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 0x0002)

    Jump('loc_F1')

    def _loc_DE(): pass

    label('loc_DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_F1',
    )

    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(0, 0x0003)

    def _loc_F1(): pass

    label('loc_F1')

    Return()

# id: 0x0001 offset: 0xF2
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFDC998, 0xFFFEE2D8, 0x00230046)
    OP_22(0x01CC, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x10A
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x00)
    OP_DB()
    SetChrFlags(0x0000, 0x0080)
    SetChrPos(0x0000, -10100, 0, 50030, 0)
    OP_6D(-10100, 0, 50030, 0)
    OP_67(0, 9320, -10000, 0)
    OP_6B(6520, 0)
    OP_6C(235000, 0)
    OP_6E(315, 0)
    OP_82(0x81, 0x00)
    OP_82(0x82, 0x00)
    FadeIn(1000, 0)
    OP_0D()

    @scena.Lambda('lambda_0176')
    def lambda_0176():
        OP_6D(-11250, 0, 47500, 8000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0176)

    @scena.Lambda('lambda_018E')
    def lambda_018E():
        OP_67(0, 6590, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_018E)

    @scena.Lambda('lambda_01A6')
    def lambda_01A6():
        OP_6B(5880, 8000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_01A6)

    OP_6E(256, 7000)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x02000000)
    OP_DC()
    OP_A2(0x10F0)
    NewScene('ED6_DT21/T1511._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x1D7
@scena.Code('func_03_1D7')
def func_03_1D7():
    EventBegin(0x00)
    OP_DB()
    SetChrFlags(0x0000, 0x0080)
    SetChrPos(0x0000, -10100, 0, 50030, 0)
    OP_6D(-5570, 0, 47640, 0)
    OP_67(0, 9000, -10000, 0)
    OP_6B(4650, 0)
    OP_6C(142000, 0)
    OP_6E(390, 0)
    OP_82(0x81, 0x00)
    OP_82(0x82, 0x00)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_0242')
    def lambda_0242():
        OP_6D(-3630, 0, 45060, 7000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0242)

    @scena.Lambda('lambda_025A')
    def lambda_025A():
        OP_6B(4400, 7000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_025A)

    Sleep(1500)

    Sleep(1500)

    Sleep(1500)

    Sleep(1500)

    FadeOut(1000, 0, -1)
    SetMapFlags(0x02000000)
    OP_DC()
    OP_A2(0x10F1)
    NewScene('ED6_DT21/T1511._SN', 109, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

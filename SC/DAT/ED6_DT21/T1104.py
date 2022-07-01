import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T1104_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1104   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, 'Soldier'),
    TXT(0x02, 'Soldier'),
    TXT(0x03, 'Soldier'),
    TXT(0x04, 'Soldier'),
    TXT(0x05, 'West Bose Highway'),
    TXT(0x06, 'East Bose Highway'),
    TXT(0x07, 'Bose - South Block'),
    TXT(0x08, 'Bose International Port'),
    TXT(0x09, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1104.x'
    header.mapIndex       = 1
    header.bgm            = 11
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x6AF
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
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
    ]

# id: 0x10002 offset: 0xB2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 4530,
            z                   = 0,
            y                   = 45190,
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
        ScenaNpcData(
            x                   = 87650,
            z                   = 0,
            y                   = 60410,
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
        ScenaNpcData(
            x                   = 47990,
            z                   = -3000,
            y                   = 29310,
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
        ScenaNpcData(
            x                   = 47940,
            z                   = 0,
            y                   = 93220,
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

# id: 0x10003 offset: 0x1B2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x1B2
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 25200,
            y           = 0,
            z           = 57940,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000004,
        ),
        ScenaEventData(
            x           = 18880,
            y           = 0,
            z           = 76030,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000005,
        ),
        ScenaEventData(
            x           = 36200,
            y           = 0,
            z           = 79200,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000006,
        ),
        ScenaEventData(
            x           = 59000,
            y           = 0,
            z           = 79200,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000007,
        ),
        ScenaEventData(
            x           = 38540,
            y           = 0,
            z           = 59990,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000008,
        ),
        ScenaEventData(
            x           = 48040,
            y           = 100,
            z           = 69500,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000008,
        ),
        ScenaEventData(
            x           = 57480,
            y           = 0,
            z           = 60010,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000008,
        ),
        ScenaEventData(
            x           = 48010,
            y           = 0,
            z           = 50550,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000008,
        ),
        ScenaEventData(
            x           = 67340,
            y           = -500,
            z           = 73070,
            range       = 1500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000009,
        ),
        ScenaEventData(
            x           = 72240,
            y           = 0,
            z           = 44910,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000000A,
        ),
        ScenaEventData(
            x           = 47960,
            y           = 0,
            z           = 85570,
            range       = 1000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000000B,
        ),
    )

# id: 0x10005 offset: 0x312
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x312
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_32E',
    )

    OP_A3(0x10F0)
    SetMapFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, 0x0003)

    def _loc_32E(): pass

    label('loc_32E')

    Return()

# id: 0x0001 offset: 0x32F
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFEC780, 0xFFFEF660, 0x00230041)
    OP_71(0x0012, 0x0004)
    OP_71(0x0013, 0x0004)
    OP_71(0x0014, 0x0004)
    OP_71(0x0015, 0x0004)
    OP_71(0x0016, 0x0004)
    OP_71(0x0017, 0x0004)
    OP_71(0x0018, 0x0004)
    OP_71(0x0019, 0x0004)
    OP_71(0x001A, 0x0004)
    OP_71(0x001B, 0x0004)
    OP_71(0x001C, 0x0004)
    OP_71(0x001D, 0x0004)
    OP_71(0x001E, 0x0004)
    OP_71(0x0020, 0x0004)

    Return()

# id: 0x0002 offset: 0x388
@scena.Code('ReInit')
def ReInit():
    ExecExpressionWithReg(
        0x0001,
        (
            Expr.Rand,
            (Expr.PushLong, 0xE),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3AD',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_4EF')

    def _loc_3AD(): pass

    label('loc_3AD')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3C6',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000640)

    Jump('loc_4EF')

    def _loc_3C6(): pass

    label('loc_3C6')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3DF',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x0000060E)

    Jump('loc_4EF')

    def _loc_3DF(): pass

    label('loc_3DF')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3F8',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005DC)

    Jump('loc_4EF')

    def _loc_3F8(): pass

    label('loc_3F8')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_411',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AA)

    Jump('loc_4EF')

    def _loc_411(): pass

    label('loc_411')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_42A',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x00000578)

    Jump('loc_4EF')

    def _loc_42A(): pass

    label('loc_42A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_443',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x00000546)

    Jump('loc_4EF')

    def _loc_443(): pass

    label('loc_443')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_45C',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000677)

    Jump('loc_4EF')

    def _loc_45C(): pass

    label('loc_45C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_475',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000645)

    Jump('loc_4EF')

    def _loc_475(): pass

    label('loc_475')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_48E',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x00000613)

    Jump('loc_4EF')

    def _loc_48E(): pass

    label('loc_48E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4A7',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005E1)

    Jump('loc_4EF')

    def _loc_4A7(): pass

    label('loc_4A7')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4C0',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AF)

    Jump('loc_4EF')

    def _loc_4C0(): pass

    label('loc_4C0')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4D9',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x0000057D)

    Jump('loc_4EF')

    def _loc_4D9(): pass

    label('loc_4D9')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4EF',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x0000054B)

    def _loc_4EF(): pass

    label('loc_4EF')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_504',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_4EF')

    def _loc_504(): pass

    label('loc_504')

    Return()

# id: 0x0003 offset: 0x505
@scena.Code('func_03_505')
def func_03_505():
    EventBegin(0x00)
    OP_DB()
    OP_12(0x00009470, 0x000249F0, 0x00000000)
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrPos(0x0000, 36740, 6050, 48800, 0)
    OP_6D(50290, 6050, 61890, 0)
    OP_67(0, 16239, -10000, 0)
    OP_6B(2650, 0)
    OP_6C(215000, 0)
    OP_6E(485, 0)
    SetChrPos(0x0008, 57480, 410, 60010, 90)
    SetChrPos(0x0009, 38540, 410, 59990, 270)
    SetChrPos(0x000A, 48010, 420, 50550, 180)
    SetChrPos(0x000B, 48040, 300, 69500, 0)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)

    @scena.Lambda('lambda_05D0')
    def lambda_05D0():
        OP_6C(12000, 13000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_05D0)

    FadeIn(1000, 0)
    Sleep(2000)

    Sleep(2000)

    Sleep(2000)

    Sleep(2000)

    OP_12(0x00009470, 0x0001FBD0, 0x00001F40)

    @scena.Lambda('lambda_060A')
    def lambda_060A():
        OP_6D(58130, 6050, 76500, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_060A)

    @scena.Lambda('lambda_0622')
    def lambda_0622():
        OP_67(0, 7200, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0622)

    @scena.Lambda('lambda_063A')
    def lambda_063A():
        OP_6B(4410, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_063A)

    @scena.Lambda('lambda_064A')
    def lambda_064A():
        OP_6E(211, 8000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_064A)

    WaitForThreadExit(0x0101, 0x0000)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_DC()
    SetMapFlags(0x02000000)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/T1124._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0x677
@scena.Code('func_04_677')
def func_04_677():
    SetPlaceName(0x002A)

    Return()

# id: 0x0005 offset: 0x67B
@scena.Code('func_05_67B')
def func_05_67B():
    SetPlaceName(0x0026)

    Return()

# id: 0x0006 offset: 0x67F
@scena.Code('func_06_67F')
def func_06_67F():
    SetPlaceName(0x0025)

    Return()

# id: 0x0007 offset: 0x683
@scena.Code('func_07_683')
def func_07_683():
    SetPlaceName(0x0020)

    Return()

# id: 0x0008 offset: 0x687
@scena.Code('func_08_687')
def func_08_687():
    SetPlaceName(0x0028)

    Return()

# id: 0x0009 offset: 0x68B
@scena.Code('func_09_68B')
def func_09_68B():
    SetPlaceName(0x002B)

    Return()

# id: 0x000A offset: 0x68F
@scena.Code('func_0A_68F')
def func_0A_68F():
    SetPlaceName(0x0021)

    Return()

# id: 0x000B offset: 0x693
@scena.Code('func_0B_693')
def func_0B_693():
    SetPlaceName(0x0027)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

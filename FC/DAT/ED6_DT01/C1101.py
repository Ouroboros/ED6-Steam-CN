import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C1101_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1101   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '吉尔'),
    TXT(0x02, '空贼'),
    TXT(0x03, '空贼'),
    TXT(0x04, '空贼'),
    TXT(0x05, '空贼'),
    TXT(0x06, '空贼艇'),
    TXT(0x07, '空贼艇（影）'),
    TXT(0x08, '摩尔根将军'),
    TXT(0x09, '王国军军官'),
    TXT(0x0A, '王国军士兵'),
    TXT(0x0B, '王国军士兵'),
    TXT(0x0C, '王国军士兵'),
    TXT(0x0D, '王国军士兵'),
    TXT(0x0E, '王国军士兵'),
    TXT(0x0F, '王国军士兵'),
    TXT(0x10, '王国军士兵'),
    TXT(0x11, '王国军士兵'),
    TXT(0x12, '王国军士兵'),
    TXT(0x13, '王国军士兵'),
    TXT(0x14, '王国军士兵'),
    TXT(0x15, '王国军士兵'),
    TXT(0x16, '王国军士兵'),
    TXT(0x17, '王国军士兵'),
    TXT(0x18, '王国军士兵'),
    TXT(0x19, '王国军士兵'),
    TXT(0x1A, '王国军士兵'),
    TXT(0x1B, '王国军士兵'),
    TXT(0x1C, ' '),
    TXT(0x1D, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'C1101.x'
    header.mapIndex       = 49
    header.bgm            = 30
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x3831
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
            word_3A         = 49,
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
        ('ED6_DT07/CH02120._CH', 'ED6_DT07/CH02120P._CP'),
        ('ED6_DT07/CH00300._CH', 'ED6_DT07/CH00300P._CP'),
        ('ED6_DT07/CH00304._CH', 'ED6_DT07/CH00304P._CP'),
        ('ED6_DT07/CH00305._CH', 'ED6_DT07/CH00305P._CP'),
        ('ED6_DT07/CH00306._CH', 'ED6_DT07/CH00306P._CP'),
        ('ED6_DT07/CH01380._CH', 'ED6_DT07/CH01380P._CP'),
        ('ED6_DT07/CH00360._CH', 'ED6_DT07/CH00360P._CP'),
        ('ED6_DT07/CH00364._CH', 'ED6_DT07/CH00364P._CP'),
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00101._CH', 'ED6_DT07/CH00101P._CP'),
        ('ED6_DT07/CH00110._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT07/CH00111._CH', 'ED6_DT07/CH00111P._CP'),
        ('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP'),
        ('ED6_DT07/CH00121._CH', 'ED6_DT07/CH00121P._CP'),
        ('ED6_DT07/CH00122._CH', 'ED6_DT07/CH00122P._CP'),
        ('ED6_DT07/CH00301._CH', 'ED6_DT07/CH00301P._CP'),
        ('ED6_DT07/CH02080._CH', 'ED6_DT07/CH02080P._CP'),
        ('ED6_DT07/CH01650._CH', 'ED6_DT07/CH01650P._CP'),
        ('ED6_DT07/CH01600._CH', 'ED6_DT07/CH01600P._CP'),
        ('ED6_DT07/CH00361._CH', 'ED6_DT07/CH00361P._CP'),
    ]

# id: 0x10002 offset: 0x14A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -1550,
            z                   = 0,
            y                   = 400,
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
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0080,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0080,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0080,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x4CA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x4CA
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -31320,
            y           = -1000,
            z           = -13400,
            range       = -30300,
            dword_10    = 0x000003E8,
            dword_14    = 0xFFFFBF28,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000C,
        ),
        ScenaEventData(
            x           = 9230,
            y           = -1000,
            z           = 28440,
            range       = 6690,
            dword_10    = 0x000003E8,
            dword_14    = 0x00006B6C,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000D,
        ),
    )

# id: 0x10005 offset: 0x50A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x50A
@scena.Code('PreInit')
def PreInit():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000068, 'loc_526'),
        (0x0000006C, 'loc_538'),
        (0x0000006D, 'loc_54E'),
        (0x0000006E, 'loc_54E'),
        (0x0000006F, 'loc_54E'),
        (-1, 'loc_56C'),
    )

    def _loc_526(): pass

    label('loc_526')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0064, 0, 0x320)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_535',
    )

    SetScenaFlags(ScenaFlag(0x0064, 0, 0x320))
    Event(0, 0x0004)

    def _loc_535(): pass

    label('loc_535')

    Jump('loc_56C')

    def _loc_538(): pass

    label('loc_538')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 0, 0x328)),
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 1, 0x329)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_54B',
    )

    SetScenaFlags(ScenaFlag(0x0065, 1, 0x329))
    Event(0, 0x0009)

    def _loc_54B(): pass

    label('loc_54B')

    Jump('loc_56C')

    def _loc_54E(): pass

    label('loc_54E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0064, 5, 0x325)),
            (Expr.TestScenaFlags, ScenaFlag(0x0064, 4, 0x324)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0064, 3, 0x323)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 0, 0x328)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_569',
    )

    SetScenaFlags(ScenaFlag(0x0065, 0, 0x328))
    Event(0, 0x0008)

    def _loc_569(): pass

    label('loc_569')

    Jump('loc_56C')

    def _loc_56C(): pass

    label('loc_56C')

    Return()

# id: 0x0001 offset: 0x56D
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0064, 0, 0x320)),
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 1, 0x329)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_592',
    )

    OP_1B(0x00, 0x00, 0x000A)
    OP_1B(0x01, 0x00, 0x000B)
    OP_1B(0x02, 0x00, 0x000C)
    OP_1B(0x03, 0x00, 0x000C)
    OP_1B(0x05, 0x00, 0x000D)

    def _loc_592(): pass

    label('loc_592')

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x387),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5A7',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x57),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_5A7(): pass

    label('loc_5A7')

    Return()

# id: 0x0002 offset: 0x5A8
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5BD',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_5BD(): pass

    label('loc_5BD')

    Return()

# id: 0x0003 offset: 0x5BE
@scena.Code('func_03_5BE')
def func_03_5BE():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5D3',
    )

    OP_99(0x00FE, 0x00, 0x03, 1000)

    Jump('func_03_5BE')

    def _loc_5D3(): pass

    label('loc_5D3')

    Return()

# id: 0x0004 offset: 0x5D4
@scena.Code('func_04_5D4')
def func_04_5D4():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(-13820, 0, -21910, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6C(315000, 0)
    SetChrPos(0x0101, -14020, 0, -25740, 0)
    SetChrPos(0x0102, -13880, 0, -27430, 0)
    SetChrPos(0x0103, -12570, 0, -26210, 0)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x0008, -2330, 0, 540, 270)
    SetChrPos(0x0009, -5040, 0, 1610, 120)
    SetChrPos(0x000A, -6710, 0, 660, 132)
    SetChrPos(0x000B, -5140, 0, -1420, 66)
    SetChrPos(0x000C, -6480, 0, -1100, 68)
    OP_72(0x0000, 0x0004)
    OP_72(0x0001, 0x0004)
    OP_A1(0x000D, 0x0000)
    SetChrPos(0x000D, 9990, 0, -2360, 341)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010021756V#003F#5P真耀眼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021757V#505F唔，那是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021758V#012F#5P（别出声，艾丝蒂尔……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)

    ChrTalk(
        0x0103,
        (
            '#0030021759V#022F#5P（这次还真是中了大奖……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0771')
    def lambda_0771():
        CameraMove(-7840, 0, 13100, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0771)

    @scena.Lambda('lambda_0789')
    def lambda_0789():
        OP_67(0, 5220, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0789)

    @scena.Lambda('lambda_07A1')
    def lambda_07A1():
        CameraSetDistance(9500, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_07A1)

    @scena.Lambda('lambda_07B1')
    def lambda_07B1():
        OP_6C(25000, 10000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_07B1)

    OP_21()
    PlayBGM(87)
    Sleep(6000)

    @scena.Lambda('lambda_07C9')
    def lambda_07C9():
        CameraMove(-4300, 3000, -10, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_07C9)

    @scena.Lambda('lambda_07E1')
    def lambda_07E1():
        OP_6E(138, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_07E1)

    Sleep(4000)

    ChrTalk(
        0x0008,
        (
            '#0290021760V#201F#2P先把重型物资放在一边，\n',
            '食品和贵重物品要优先处理。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290021761V尽量快一点。\n',
            '再磨磨蹭蹭的敌人可就来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2P#1K收到！吉尔大哥。',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x000A,
        (
            '#1P#1K收到！吉尔大哥。',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x000B,
        (
            '#4P#1K收到！吉尔大哥。',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x000C,
        (
            '#1270021765V#3P#1K收到！吉尔大哥。',
            TxtCtl.Enter,
        ),
    )

    Sleep(500)

    OP_56(0x01)
    OP_59()
    Sleep(100)

    Fade(1000)
    CameraMove(-13820, 0, -21910, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(332, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010021766V#580F（定期船在这种地方……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021767V（那个孩子所说的\n',
            '　果然不是梦啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021768V#020F（这里是……\n',
            '　露天挖掘用的峡谷吗……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021769V（果然是个绝妙的隐蔽场所。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021770V#012F（不会轻易被发现呢。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020021771V（那些空贼搬运的\n',
            '　是定期船装载的货物吧？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021772V#006F（这些以后再说吧！）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021773V（在他们还没逃跑之前，\n',
            '　一定要把他们全部逮住！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    CameraMove(-4110, 0, 490, 0)
    OP_67(0, 5220, -10000, 0)
    CameraSetDistance(5070, 0)
    OP_6C(69000, 0)
    OP_6E(213, 0)
    SetChrChipByIndex(0x0101, 8)
    SetChrChipByIndex(0x0102, 10)
    SetChrChipByIndex(0x0103, 12)
    SetChrPos(0x0101, -10010, 0, -10600, 26)
    SetChrPos(0x0102, -9790, 0, -12210, 25)
    SetChrPos(0x0103, -8430, 0, -11060, 23)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0290021774V#203F哈，这是第三个来回了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290021775V真是的，大哥一来\n',
            '就拼命地使唤我这个做弟弟的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290021776V#200F不过算了，这次运完之后，\n',
            '就可以不慌不忙地要求赎金了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021777V#1P到此为止了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_0C1F')
    def lambda_0C1F():
        ChrTurnDirection(0x00FE, 0x0101, 800)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0C1F)

    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_0C44')
    def lambda_0C44():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0C44)

    Sleep(50)

    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_0C6E')
    def lambda_0C6E():
        ChrTurnDirection(0x00FE, 0x0101, 800)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0C6E)

    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_0C93')
    def lambda_0C93():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0C93)

    Sleep(50)

    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#0290021778V#201F#5P什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0CCA')
    def lambda_0CCA():
        CameraMove(-4960, 0, -4910, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0CCA)

    @scena.Lambda('lambda_0CE2')
    def lambda_0CE2():
        OP_6C(69000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0CE2)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010021779V#502F只要世上仍存一丝罪恶之源，\n',
            '燃烧的真实与正义之火就不会消失……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010021780V#508F#3S代表爱与正义的游击士，堂堂登场！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0103, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0009, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x000A, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x000B, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x000C, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0008, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    OP_63(0x0102)
    OP_63(0x0103)
    OP_63(0x0008)
    OP_63(0x0009)
    OP_63(0x000A)
    OP_63(0x000B)
    OP_63(0x000C)

    ChrTalk(
        0x0101,
        (
            '#0010021781V#505F咦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021782V#018F爱与正义……好像有点那个了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021783V#025F真是的。\n',
            '马上就开始得意忘形了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0101,
        (
            '#0010021784V#503F怎、怎么了……\n',
            '我这叫做开门见山嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0009, 6)
    SetChrChipByIndex(0x000C, 6)
    SetChrChipByIndex(0x000A, 6)
    SetChrChipByIndex(0x000B, 6)
    SetChrChipByIndex(0x0008, 1)
    SetChrChipByIndex(0x0008, 15)
    ChrWalkTo(0x0008, -4100, 0, -1970, 5000, 0x00)
    SetChrChipByIndex(0x0008, 1)

    ChrTalk(
        0x0008,
        (
            '#0290021785V#201F你们是……\n',
            '和乔丝特交过手的那些人！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290021786V消、消息有误！\n',
            '似乎来得太早了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021787V#509F#2P消息有误？来得太早了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021788V听不明白你在说什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021789V#022F#2P基于游击士协会的规定， \n',
            '你们涉嫌抢劫定期船以及挟持乘客，\n',
            '现以协会的名义将你们逮捕归案。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021790V给我束手就擒吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0290021791V#201F等、等一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290021792V难道说你们……\n',
            '靠三个人就想逮捕我们？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021793V#009F#2P什么呀，一看就知道了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0290021794V#204F嗯，原来如此。\n',
            '和那些家伙没关系啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290021795V#201F要是这样就早点说嘛……\n',
            '就让你们先暂时睡一会儿吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0008, 15)

    @scena.Lambda('lambda_115E')
    def lambda_115E():
        OP_92(0x00FE, 0x0103, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_115E)

    Sleep(50)

    SetChrChipByIndex(0x000C, 19)

    @scena.Lambda('lambda_117D')
    def lambda_117D():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_117D)

    Sleep(50)

    SetChrChipByIndex(0x000B, 19)

    @scena.Lambda('lambda_119C')
    def lambda_119C():
        OP_92(0x00FE, 0x0102, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_119C)

    Sleep(50)

    SetChrChipByIndex(0x0009, 19)

    @scena.Lambda('lambda_11BB')
    def lambda_11BB():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_11BB)

    Sleep(50)

    SetChrChipByIndex(0x000A, 19)

    @scena.Lambda('lambda_11DA')
    def lambda_11DA():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_11DA)

    SetChrFlags(0x0101, 0x1000)
    SetChrFlags(0x0102, 0x1000)
    SetChrFlags(0x0103, 0x1000)
    SetChrChipByIndex(0x0103, 13)

    @scena.Lambda('lambda_1203')
    def lambda_1203():
        CameraMove(-3960, 0, -3910, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1203)

    @scena.Lambda('lambda_121B')
    def lambda_121B():
        OP_92(0x00FE, 0x0008, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_121B)

    Sleep(50)

    SetChrChipByIndex(0x0101, 9)

    @scena.Lambda('lambda_123A')
    def lambda_123A():
        OP_92(0x00FE, 0x000C, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_123A)

    Sleep(50)

    SetChrChipByIndex(0x0102, 11)

    @scena.Lambda('lambda_1259')
    def lambda_1259():
        OP_92(0x00FE, 0x000B, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1259)

    Sleep(300)

    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0103, 0xFF)
    ClearChrFlags(0x0101, 0x1000)
    ClearChrFlags(0x0102, 0x1000)
    ClearChrFlags(0x0103, 0x1000)
    Battle(0x00000387, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x00)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_12B7'),
        (-1, 'loc_12BC'),
    )

    def _loc_12B7(): pass

    label('loc_12B7')

    OP_B4(0x00)

    Jump('loc_12BC')

    def _loc_12BC(): pass

    label('loc_12BC')

    CameraMove(-5750, 0, -5350, 0)
    OP_67(0, 5220, -10000, 0)
    CameraSetDistance(5070, 0)
    OP_6C(69000, 0)
    OP_6E(212, 0)

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0008, 2)
    SetChrChipByIndex(0x0009, 7)
    SetChrChipByIndex(0x000A, 7)
    SetChrChipByIndex(0x000B, 7)
    SetChrChipByIndex(0x000C, 7)

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0103,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0101, 8)
    SetChrChipByIndex(0x0102, 10)
    SetChrChipByIndex(0x0103, 12)
    SetChrPos(0x0008, -5830, 0, -4580, 216)
    SetChrPos(0x0009, -4000, 0, -5410, 258)
    SetChrPos(0x000A, -4760, 0, -2930, 184)
    SetChrPos(0x000B, -8260, 0, -3290, 156)
    SetChrPos(0x000C, -2270, 0, -3270, 232)
    SetChrPos(0x0101, -9950, 0, -7740, 49)
    SetChrPos(0x0102, -9710, 0, -9600, 31)
    SetChrPos(0x0103, -7170, 0, -8440, 358)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0290021796V#203F疼疼疼……\n',
            '还挺厉害的嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290021797V#200F不愧是打败过乔丝特的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021798V#502F奉承我们也没有用。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021799V#005F你们还是乖乖地投降吧。\n',
            '还有，把乘客们都放出来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0290021800V#202F哈哈哈！\n',
            '看起来你们真的什么都不知道。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290021801V真是一群多管闲事的傻瓜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021802V#509F你、你说什么～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021803V#016F……小心！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    LoadEffect(0x00, 'map\\\\mp004_00.eff')
    OP_99(0x0008, 0x03, 0x00, 1000)
    SetChrChipByIndex(0x0008, 1)

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0008, 3)

    @scena.Lambda('lambda_158D')
    def lambda_158D():
        OP_6C(50000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_158D)

    OP_99(0x0008, 0x00, 0x03, 1000)
    OP_99(0x0008, 0x00, 0x03, 1000)
    WaitForThreadExit(0x0101, 0x0002)
    SetChrChipByIndex(0x0008, 4)
    OP_26(127)
    SetChrPos(0x0023, -7460, -3000, -6780, 339)
    PlayEffect(0x00, 0xFF, 0x0008, 250, 900, 330, 0, 0, 0, 1000, 1000, 1000, 0x0023, 0, 0, 0, 0)
    OP_99(0x0008, 0x00, 0x01, 1000)
    Sleep(1300)

    PlaySE(127, 0x00, 0x64)
    OP_11(0xFF, 0xFF, 0xFF, 42000, 95000, 0)
    SetMapFlags(0x00000010)
    OP_12(0x00002C24, 0x0000E09C, 0x000007D0)
    Sleep(2000)

    ChrTalk(
        0x0101,
        (
            '#0010021804V#580F这、这是什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021805V#024F糟了，是烟雾弹！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    PlaySE(121, 0x00, 0x64)
    PlaySE(204, 0x00, 0x64)
    PlaySE(205, 0x00, 0x64)
    SetChrPos(0x0008, 2280, 0, -8280, 117)

    ChrTalk(
        0x0008,
        (
            '#0290021806V#202F啊～哈哈哈哈哈！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290021807V虽然货物没搬光有点不甘心，\n',
            '但是我就先忍了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290021808V再见啦，各位游击士！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x000D, 6450, 100, -820, 341)
    SetChrPos(0x000E, 6450, 100, -820, 341)
    LoadEffect(0x01, 'map\\\\mp021_00.eff')
    PlayEffect(0x01, 0x02, 0x000E, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    OP_72(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    SetChrFlags(0x000D, 0x0004)
    SetChrFlags(0x000D, 0x0040)
    OP_A1(0x000D, 0x0000)
    OP_A1(0x000E, 0x0001)

    @scena.Lambda('lambda_17B7')
    def lambda_17B7():
        ChrTurnDirection(0x00FE, 0x000D, 0)
        Yield()

        Jump('lambda_17B7')

    DispatchAsync2(0x0101, 0x0001, lambda_17B7)

    @scena.Lambda('lambda_17C8')
    def lambda_17C8():
        ChrTurnDirection(0x00FE, 0x000D, 0)
        Yield()

        Jump('lambda_17C8')

    DispatchAsync2(0x0103, 0x0001, lambda_17C8)

    @scena.Lambda('lambda_17D9')
    def lambda_17D9():
        ChrTurnDirection(0x00FE, 0x000D, 0)
        Yield()

        Jump('lambda_17D9')

    DispatchAsync2(0x0102, 0x0001, lambda_17D9)

    CreateThread(0x000D, 0x01, 0x00, 0x0005)
    CreateThread(0x000E, 0x01, 0x00, 0x0006)

    @scena.Lambda('lambda_17F8')
    def lambda_17F8():
        OP_6C(26000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_17F8)

    Sleep(1000)

    @scena.Lambda('lambda_180D')
    def lambda_180D():
        CameraSetDistance(6000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_180D)

    OP_12(0x0000A794, 0x0001BD50, 0x00002710)
    Sleep(1000)

    @scena.Lambda('lambda_182F')
    def lambda_182F():
        CameraMove(-8130, 0, -15090, 4000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_182F)

    CreateThread(0x0103, 0x03, 0x00, 0x0007)
    Sleep(5000)

    @scena.Lambda('lambda_1853')
    def lambda_1853():
        CameraMove(-9300, 0, -10850, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_1853)

    CameraSetDistance(5170, 2000)
    OP_20(0x000005DC)
    Fade(1000)
    ClearMapFlags(0x00000010)
    OP_0D()
    OP_21()
    PlayBGM(30)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010021809V#007F咳，咳咳……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021810V好像进到眼睛里了～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021811V#012F别担心，没有毒……\n',
            '好像只是普通的发烟筒而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0103, 0xFF)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)

    ExecExpressionWithValue(
        0x0103,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0103, 65535)
    ChrWalkTo(0x0103, -8240, 0, -11420, 2000, 0x00)
    OP_62(0x0103, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(2000)

    OP_63(0x0103)

    ChrTalk(
        0x0103,
        (
            '#0030021812V#022F……已经看不到他们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021813V#025F哎呀呀，跟上次一样，\n',
            '这次也被他们逃掉了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021814V这下可好了，\n',
            '就算给我降级的处分我也无话可说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0102, 65535)
    ChrTurnDirection(0x0102, 0x0103, 400)

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0101, 65535)
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010021815V#009F真是的，雪拉姐……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021816V老是这样，\n',
            '不要把过错都揽到自己一个人身上嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021817V#012F我们也应该承担\n',
            '被他们逃掉的责任。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020021818V与其在这里后悔，\n',
            '倒不如想想现在能做些什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030021819V#026F#4P呼，真是的……\n',
            '我们的立场好像颠倒了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021820V#020F不过幸好把定期船夺回来了。\n',
            '我们赶快进去调查看看吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021821V也许里面还有乘客。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021822V#006F……嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0101, -12570, 0, -19040, 0)
    SetChrPos(0x0102, -12570, 0, -19040, 0)
    SetChrPos(0x0103, -12570, 0, -19040, 0)
    CameraMove(-12570, 0, -19040, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(500)

    OP_28(0x0036, 0x01, 0x0200)
    OP_28(0x0036, 0x01, 0x0400)
    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0005 offset: 0x1C23
@scena.Code('func_05_1C23')
def func_05_1C23():
    @scena.Lambda('lambda_1C29')
    def lambda_1C29():
        ChrMoveTo(0x00FE, -64870, 4000, -57810, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1C29)

    @scena.Lambda('lambda_1C44')
    def lambda_1C44():
        SetChrDirection(0x00FE, 200, 30)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1C44)

    Sleep(1000)

    @scena.Lambda('lambda_1C57')
    def lambda_1C57():
        ChrMoveTo(0x00FE, -25870, 19000, -67810, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1C57)

    Sleep(500)

    @scena.Lambda('lambda_1C77')
    def lambda_1C77():
        ChrMoveTo(0x00FE, -25870, 19000, -67810, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1C77)

    Sleep(500)

    OP_B0(0x0000, 0x1E)
    OP_6F(0x0000, 160)
    OP_70(0x0000, 200)

    @scena.Lambda('lambda_1CA9')
    def lambda_1CA9():
        SetChrDirection(0x00FE, 200, 30)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1CA9)

    Sleep(200)

    @scena.Lambda('lambda_1CBC')
    def lambda_1CBC():
        SetChrDirection(0x00FE, 200, 28)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1CBC)

    Sleep(200)

    @scena.Lambda('lambda_1CCF')
    def lambda_1CCF():
        SetChrDirection(0x00FE, 200, 26)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1CCF)

    Sleep(200)

    @scena.Lambda('lambda_1CE2')
    def lambda_1CE2():
        SetChrDirection(0x00FE, 200, 24)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1CE2)

    Sleep(200)

    @scena.Lambda('lambda_1CF5')
    def lambda_1CF5():
        SetChrDirection(0x00FE, 200, 22)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1CF5)

    Sleep(200)

    @scena.Lambda('lambda_1D08')
    def lambda_1D08():
        SetChrDirection(0x00FE, 200, 20)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1D08)

    Sleep(200)

    @scena.Lambda('lambda_1D1B')
    def lambda_1D1B():
        SetChrDirection(0x00FE, 200, 18)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1D1B)

    Sleep(200)

    @scena.Lambda('lambda_1D2E')
    def lambda_1D2E():
        SetChrDirection(0x00FE, 200, 16)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1D2E)

    Sleep(200)

    @scena.Lambda('lambda_1D41')
    def lambda_1D41():
        SetChrDirection(0x00FE, 200, 15)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1D41)

    OP_6F(0x0000, 200)
    OP_70(0x0000, 240)

    @scena.Lambda('lambda_1D5D')
    def lambda_1D5D():
        ChrMoveTo(0x00FE, -25870, 15000, -67810, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1D5D)

    Sleep(500)

    @scena.Lambda('lambda_1D7D')
    def lambda_1D7D():
        SetChrDirection(0x00FE, 200, 20)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1D7D)

    @scena.Lambda('lambda_1D8B')
    def lambda_1D8B():
        ChrMoveTo(0x00FE, -25870, 15000, -67810, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1D8B)

    Sleep(500)

    @scena.Lambda('lambda_1DAB')
    def lambda_1DAB():
        ChrMoveTo(0x00FE, -25870, 15000, -67810, 22000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1DAB)

    Sleep(500)

    @scena.Lambda('lambda_1DCB')
    def lambda_1DCB():
        ChrMoveTo(0x00FE, -25870, 15000, -67810, 24000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1DCB)

    Sleep(500)

    @scena.Lambda('lambda_1DEB')
    def lambda_1DEB():
        ChrMoveTo(0x00FE, -25870, 15000, -67810, 26000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1DEB)

    Sleep(500)

    @scena.Lambda('lambda_1E0B')
    def lambda_1E0B():
        ChrMoveTo(0x00FE, -25870, 15000, -67810, 28000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1E0B)

    Sleep(500)

    @scena.Lambda('lambda_1E2B')
    def lambda_1E2B():
        ChrMoveTo(0x00FE, -25870, 15000, -67810, 30000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1E2B)

    Sleep(500)

    WaitForThreadExit(0x00FE, 0x0002)
    OP_71(0x0000, 0x0004)

    Return()

# id: 0x0006 offset: 0x1E50
@scena.Code('func_06_1E50')
def func_06_1E50():
    @scena.Lambda('lambda_1E56')
    def lambda_1E56():
        ChrMoveTo(0x00FE, -64870, 1000, -57810, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1E56)

    @scena.Lambda('lambda_1E71')
    def lambda_1E71():
        SetChrDirection(0x00FE, 200, 30)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1E71)

    Sleep(1000)

    @scena.Lambda('lambda_1E84')
    def lambda_1E84():
        ChrMoveTo(0x00FE, -25870, 1000, -67810, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1E84)

    Sleep(500)

    @scena.Lambda('lambda_1EA4')
    def lambda_1EA4():
        ChrMoveTo(0x00FE, -25870, 1000, -67810, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1EA4)

    Sleep(500)

    OP_B0(0x0000, 0x1E)
    OP_6F(0x0000, 160)
    OP_70(0x0000, 200)

    @scena.Lambda('lambda_1ED6')
    def lambda_1ED6():
        SetChrDirection(0x00FE, 200, 30)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1ED6)

    Sleep(200)

    @scena.Lambda('lambda_1EE9')
    def lambda_1EE9():
        SetChrDirection(0x00FE, 200, 28)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1EE9)

    Sleep(200)

    @scena.Lambda('lambda_1EFC')
    def lambda_1EFC():
        SetChrDirection(0x00FE, 200, 26)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1EFC)

    Sleep(200)

    @scena.Lambda('lambda_1F0F')
    def lambda_1F0F():
        SetChrDirection(0x00FE, 200, 24)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1F0F)

    Sleep(200)

    @scena.Lambda('lambda_1F22')
    def lambda_1F22():
        SetChrDirection(0x00FE, 200, 22)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1F22)

    Sleep(200)

    @scena.Lambda('lambda_1F35')
    def lambda_1F35():
        SetChrDirection(0x00FE, 200, 20)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1F35)

    Sleep(200)

    @scena.Lambda('lambda_1F48')
    def lambda_1F48():
        SetChrDirection(0x00FE, 200, 18)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1F48)

    Sleep(200)

    @scena.Lambda('lambda_1F5B')
    def lambda_1F5B():
        SetChrDirection(0x00FE, 200, 16)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1F5B)

    Sleep(200)

    @scena.Lambda('lambda_1F6E')
    def lambda_1F6E():
        SetChrDirection(0x00FE, 200, 15)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1F6E)

    OP_6F(0x0000, 200)
    OP_70(0x0000, 240)

    @scena.Lambda('lambda_1F8A')
    def lambda_1F8A():
        ChrMoveTo(0x00FE, -25870, 1000, -67810, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1F8A)

    Sleep(500)

    @scena.Lambda('lambda_1FAA')
    def lambda_1FAA():
        SetChrDirection(0x00FE, 200, 20)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1FAA)

    @scena.Lambda('lambda_1FB8')
    def lambda_1FB8():
        ChrMoveTo(0x00FE, -25870, 1000, -67810, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1FB8)

    Sleep(500)

    @scena.Lambda('lambda_1FD8')
    def lambda_1FD8():
        ChrMoveTo(0x00FE, -25870, 1000, -67810, 22000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1FD8)

    Sleep(500)

    @scena.Lambda('lambda_1FF8')
    def lambda_1FF8():
        ChrMoveTo(0x00FE, -25870, 1000, -67810, 24000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1FF8)

    Sleep(500)

    @scena.Lambda('lambda_2018')
    def lambda_2018():
        ChrMoveTo(0x00FE, -25870, 1000, -67810, 26000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2018)

    Sleep(500)

    @scena.Lambda('lambda_2038')
    def lambda_2038():
        ChrMoveTo(0x00FE, -25870, 1000, -67810, 28000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2038)

    Sleep(500)

    @scena.Lambda('lambda_2058')
    def lambda_2058():
        ChrMoveTo(0x00FE, -25870, 1000, -67810, 30000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2058)

    Sleep(500)

    WaitForThreadExit(0x00FE, 0x0002)
    OP_71(0x0000, 0x0004)

    Return()

# id: 0x0007 offset: 0x207D
@scena.Code('func_07_207D')
def func_07_207D():
    Sleep(2000)

    OP_24(0x0079, 0x5F)
    OP_24(0x00CC, 0x5F)
    OP_24(0x00CD, 0x5F)
    Sleep(200)

    OP_24(0x0079, 0x5A)
    OP_24(0x00CC, 0x5A)
    OP_24(0x00CD, 0x5A)
    Sleep(200)

    OP_24(0x0079, 0x55)
    OP_24(0x00CC, 0x55)
    OP_24(0x00CD, 0x55)
    Sleep(200)

    OP_24(0x0079, 0x50)
    OP_24(0x00CC, 0x50)
    OP_24(0x00CD, 0x50)
    Sleep(200)

    OP_24(0x0079, 0x46)
    OP_24(0x00CC, 0x46)
    OP_24(0x00CD, 0x46)
    Sleep(200)

    OP_24(0x0079, 0x3C)
    OP_24(0x00CC, 0x3C)
    OP_24(0x00CD, 0x3C)
    Sleep(200)

    OP_24(0x0079, 0x32)
    OP_24(0x00CC, 0x32)
    OP_24(0x00CD, 0x32)
    Sleep(200)

    OP_23(0x0079)
    OP_23(0x00CC)
    OP_23(0x00CD)

    Return()

# id: 0x0008 offset: 0x2103
@scena.Code('func_08_2103')
def func_08_2103():
    EventBegin(0x00)
    CameraMove(-11700, 7200, 16590, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(314000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -5960, 7200, 16680, 90)
    SetChrPos(0x0102, -4940, 7200, 15330, 51)
    SetChrPos(0x0103, -4230, 7200, 16900, 244)
    FadeIn(1000, 0)
    CameraMove(-5220, 7200, 16540, 3000)

    ChrTalk(
        0x0101,
        (
            '#0010021844V#007F#5P虽然已经调查了一遍，\n',
            '可是一个人也没有发现……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021845V#015F看样子乘客被空贼\n',
            '用空贼飞艇带走的可能性很高。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020021846V#012F……大概，是到他们的据点去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021847V#003F#5P唔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021848V好不容易\n',
            '才找到的线索就这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021849V#020F好了好了。\n',
            '不要这么愁眉苦脸的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021850V现在并不是\n',
            '一点线索都没有哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021851V#027F你们想想，为什么那帮家伙\n',
            '会把定期船藏在这种地方呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021852V#004F#5P哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021853V#026F正如刚才所见，\n',
            '定期船内的导力完全停止了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021854V这也就意味着，\n',
            '导力引擎被他们拿走了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021855V众所周知，导力器中的导力\n',
            '在经过一段时间后会自动回复。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021856V#022F而那些家伙多次\n',
            '来回运送大量的货物。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021857V考虑这样做所花费的时间和带来的风险，\n',
            '用定期船把货物运往自己的据点\n',
            '效率反倒应该高得多吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021858V#006F#5P啊，确实……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021859V那么，空贼把定期船\n',
            '藏在这个地方的原因就是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021860V#505F嗯，仔细考虑一下的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        10,
        0,
        (
            TXT(0x00, '【为了挑选货物】\n'),
            TXT(0x01, '【为了把人质转移到空贼飞艇上】\n'),
            TXT(0x02, '【为了抢夺导力引擎】\n'),
            TXT(0x03, '【为了逃避王国军的搜捕】\n'),
            TXT(0x04, '【因为据点在特殊的地方】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_25C0'),
        (0x00000001, 'loc_2646'),
        (0x00000002, 'loc_26DC'),
        (0x00000003, 'loc_2762'),
        (0x00000004, 'loc_280E'),
        (-1, 'loc_283A'),
    )

    def _loc_25C0(): pass

    label('loc_25C0')

    ChrTalk(
        0x0103,
        (
            '#0030021861V#026F确实，这里比较宽阔，\n',
            '挑选货物时也许很方便。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021862V#027F但是，这却无法构成\n',
            '空贼把定期船藏在这个地方的理由。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_2B(0x0035, 0x0001)

    Jump('loc_283A')

    def _loc_2646(): pass

    label('loc_2646')

    ChrTalk(
        0x0103,
        (
            '#0030021863V#026F确实，在把人质转移到空贼飞艇上的过程中，\n',
            '定期船必须要着陆。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021864V#027F但是，这却无法构成\n',
            '空贼把定期船藏在这个地方的理由。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_2B(0x0035, 0x0001)

    Jump('loc_283A')

    def _loc_26DC(): pass

    label('loc_26DC')

    ChrTalk(
        0x0103,
        (
            '#0030021865V#026F确实，要把引擎拔除的话，\n',
            '定期船必须要着陆。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021866V#027F但是，这却无法构成\n',
            '空贼把定期船藏在这个地方的理由。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_2B(0x0035, 0x0001)

    Jump('loc_283A')

    def _loc_2762(): pass

    label('loc_2762')

    ChrTalk(
        0x0103,
        (
            '#0030021867V#026F确实，定期船很大，\n',
            '很容易会被王国军发现……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021868V#027F所以把它藏在\n',
            '据点以外的场所的可能性很高。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021869V但是，这个解释\n',
            '也不能说是决定性的理由。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_2B(0x0035, 0x0002)

    Jump('loc_283A')

    def _loc_280E(): pass

    label('loc_280E')

    ChrTalk(
        0x0103,
        (
            '#0030021870V#021F对，就是因为这个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_2B(0x0035, 0x0003)

    Jump('loc_283A')

    def _loc_283A(): pass

    label('loc_283A')

    Sleep(400)

    ChrTalk(
        0x0103,
        (
            '#0030021871V#020F根据我的推测，\n',
            '他们的据点应该是个地形特殊的地方。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021872V１０～１５亚矩……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021873V也就是说只能让空贼飞艇\n',
            '这种小型艇降落的特殊场所。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021874V#008F#5P原、原来是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021875V#015F像山峦、峡谷这样\n',
            '高低差很大的复杂地形……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020021876V#012F应该是最值得怀疑的地方吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021877V#022F对，我也这么想。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021878V#522F如果真是那样的话……\n',
            '那真是超出我们能力范围了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021879V他们的据点很有可能\n',
            '是在步行所涉足不到的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021880V#505F#5P那、那怎么办呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021881V#025F是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021882V虽然让人失望，但现在唯有\n',
            '向军队说明情况并请求他们协助了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021883V毕竟他们拥有军用飞艇啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021884V#009F#5P哎～……\n',
            '搞了半天还是要依靠军队啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021885V#010F这艘定期船的事情\n',
            '最后肯定要报告给军队的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020021886V不管他们的态度怎么样，\n',
            '我认为现在还是合作比较好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020021887V这也是为了早点解放人质啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021888V#007F#5P嗯，是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021889V现在不是任性的时候啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021890V#020F总之，我们先回游击士协会\n',
            '向卢格兰爷爷汇报一下吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021891V使用协会的导力通信器，\n',
            '就可以和哈肯大门联络了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0036, 0x01, 0x0800)
    OP_28(0x0036, 0x01, 0x1000)
    EventEnd(0x00)

    Return()

# id: 0x0009 offset: 0x2C36
@scena.Code('func_09_2C36')
def func_09_2C36():
    EventBegin(0x00)
    CameraMove(-9690, 2130, 10650, 0)
    OP_67(0, 7660, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(293, 0)
    SetChrPos(0x0101, -10200, 1630, 9500, 180)
    SetChrPos(0x0103, -9190, 1620, 9480, 180)
    SetChrPos(0x0102, -9720, 2020, 10410, 180)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x0017, 0x0080)
    ClearChrFlags(0x0018, 0x0080)
    ClearChrFlags(0x0019, 0x0080)
    ClearChrFlags(0x001A, 0x0080)
    ClearChrFlags(0x001B, 0x0080)
    ClearChrFlags(0x001C, 0x0080)
    ClearChrFlags(0x001D, 0x0080)
    ClearChrFlags(0x001E, 0x0080)
    ClearChrFlags(0x001F, 0x0080)
    ClearChrFlags(0x0020, 0x0080)
    ClearChrFlags(0x0021, 0x0080)
    ClearChrFlags(0x0022, 0x0080)
    SetChrPos(0x0010, -9650, 0, 2260, 0)
    SetChrPos(0x0011, -11190, 0, 2770, 24)
    SetChrPos(0x0012, -12650, 0, 3420, 24)
    SetChrPos(0x0013, -14120, 0, 4070, 24)
    SetChrPos(0x0014, -15860, 0, 4850, 24)
    SetChrPos(0x0015, -16590, 0, 3200, 24)
    SetChrPos(0x0016, -14940, 0, 2470, 24)
    SetChrPos(0x0017, -13390, 0, 1780, 24)
    SetChrPos(0x0018, -11940, 0, 1130, 24)
    SetChrPos(0x0019, -10330, 0, 610, 24)
    SetChrPos(0x001A, -8189, 0, 2810, 336)
    SetChrPos(0x001B, -6820, 0, 3430, 336)
    SetChrPos(0x001C, -5550, 0, 4000, 336)
    SetChrPos(0x001D, -4190, 0, 4600, 336)
    SetChrPos(0x001E, -8870, 0, 510, 336)
    SetChrPos(0x001F, -7450, 0, 1150, 336)
    SetChrPos(0x0020, -6170, 0, 1720, 336)
    SetChrPos(0x0021, -4870, 0, 2300, 336)
    SetChrPos(0x0022, -3390, 0, 2960, 336)
    OP_72(0x0005, 0x0004)
    OP_72(0x0006, 0x0004)
    FadeIn(1000, 0)
    OP_20(0x000005DC)
    OP_0D()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010021892V#580F#5P哎、哎哎～～！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021893V这、这是怎么回事啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021894V#017F#5P哈……\n',
            '这真是意料之外的来者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021895V#025F#5P唔，看来这次\n',
            '连联络的功夫也省了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    PlayBGM(101)
    Fade(2000)
    CameraMove(9600, 0, -2009, 0)
    OP_67(0, 13000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(280000, 0)
    OP_6E(483, 0)

    @scena.Lambda('lambda_2FAA')
    def lambda_2FAA():
        OP_67(0, 6570, -10000, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2FAA)

    Sleep(2500)

    @scena.Lambda('lambda_2FC7')
    def lambda_2FC7():
        OP_6C(39000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2FC7)

    @scena.Lambda('lambda_2FD7')
    def lambda_2FD7():
        OP_6E(350, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2FD7)

    CameraMove(-10180, 340, 6490, 6000)

    ChrTalk(
        0x0010,
        (
            '#2420021896V#2P发现一干\n',
            '手持武器的嫌疑犯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#2450021897V#2P你们！\n',
            '老实举起手来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#2440021898V#5P真是世态炎凉啊，\n',
            '连小女孩也做起空贼来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021899V#509F谁、谁是空贼啊！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021900V没看到我身上的徽章吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x000F, -9410, 0, -4900, 0)
    ClearChrFlags(0x000F, 0x0080)

    NpcTalk(
        0x000F,
        '老人的声音',
        (
            '#0600021901V#1P哼，游击士的徽章吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000F,
        '老人的声音',
        (
            '#0600021902V#1P凭这种东西\n',
            '就能证明自身的清白？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3149')
    def lambda_3149():
        ChrWalkTo(0x00FE, -9640, 0, 4560, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_3149)

    Sleep(500)

    @scena.Lambda('lambda_3169')
    def lambda_3169():
        ChrTurnDirection(0x00FE, 0x000F, 400)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_3169)

    @scena.Lambda('lambda_3177')
    def lambda_3177():
        ChrTurnDirection(0x00FE, 0x000F, 400)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_3177)

    WaitForThreadExit(0x0019, 0x0001)

    @scena.Lambda('lambda_318A')
    def lambda_318A():
        ChrMoveTo(0x00FE, -10850, 0, 780, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0002, lambda_318A)

    @scena.Lambda('lambda_31A5')
    def lambda_31A5():
        ChrMoveTo(0x00FE, -8350, 0, 550, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0002, lambda_31A5)

    @scena.Lambda('lambda_31C0')
    def lambda_31C0():
        ChrTurnDirection(0x00FE, 0x000F, 0)
        Yield()

        Jump('lambda_31C0')

    DispatchAsync2(0x0019, 0x0001, lambda_31C0)

    @scena.Lambda('lambda_31D1')
    def lambda_31D1():
        ChrTurnDirection(0x00FE, 0x000F, 0)
        Yield()

        Jump('lambda_31D1')

    DispatchAsync2(0x001E, 0x0001, lambda_31D1)

    @scena.Lambda('lambda_31E2')
    def lambda_31E2():
        ChrTurnDirection(0x00FE, 0x000F, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_31E2)

    WaitForThreadExit(0x0010, 0x0001)

    @scena.Lambda('lambda_31F5')
    def lambda_31F5():
        ChrMoveTo(0x00FE, -8850, 0, 1900, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_31F5)

    @scena.Lambda('lambda_3210')
    def lambda_3210():
        ChrTurnDirection(0x00FE, 0x000F, 0)
        Yield()

        Jump('lambda_3210')

    DispatchAsync2(0x0010, 0x0001, lambda_3210)

    @scena.Lambda('lambda_3221')
    def lambda_3221():
        CameraMove(-9140, 1050, 8950, 3500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3221)

    @scena.Lambda('lambda_3239')
    def lambda_3239():
        OP_6E(306, 3500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3239)

    WaitForThreadExit(0x000F, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010021903V#004F摩、摩尔根将军！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021904V#014F为什么会在这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0600021905V#163F根据各部队的报告，\n',
            '这里尚未进行细致的搜查。\n',
            '我们来这里也是理所当然的事情……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600021906V#160F但是，万万没想到\n',
            '你们竟然和空贼勾结。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021907V#022F在没有真凭实据之前，\n',
            '请不要这样随意下结论。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021908V我们只是先你们一步\n',
            '到这里做现场调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0600021909V#161F那么空贼在哪里？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600021910V船内的乘客又在哪里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021911V#013F只差一步就能抓住那些空贼了，\n',
            '这是我们的疏忽。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020021912V作为人质的乘客也不在定期船里面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0600021913V#163F哼，真是不打自招……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600021914V原来在我们到来之前，\n',
            '你们已经向空贼通风报信了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021915V#005F等、等一下！\n',
            '你这样说实在是太过分了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x000F,
        (
            '#0600021916V#162F#5S这是我该讲的台词！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x000F,
        (
            '#0600021917V#162F#3S来人！\n',
            '把这三个嫌疑犯抓起来！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    OP_28(0x0036, 0x01, 0x2000)
    FadeOut(1500, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T1401._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000A offset: 0x356D
@scena.Code('func_0A_356D')
def func_0A_356D():
    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3585',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_358C')

    def _loc_3585(): pass

    label('loc_3585')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_358C(): pass

    label('loc_358C')

    @scena.Lambda('lambda_3592')
    def lambda_3592():
        ChrTurnDirection(0x0101, 0x0103, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3592)

    @scena.Lambda('lambda_35A0')
    def lambda_35A0():
        ChrTurnDirection(0x0102, 0x0103, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_35A0)

    ChrTalk(
        0x0103,
        (
            '#0030021828V#020F没有去别的地方的时间了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021829V现在最重要的是调查定期船。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 0, 0, 2000, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x000B offset: 0x3617
@scena.Code('func_0B_3617')
def func_0B_3617():
    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_362F',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_3636')

    def _loc_362F(): pass

    label('loc_362F')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_3636(): pass

    label('loc_3636')

    @scena.Lambda('lambda_363C')
    def lambda_363C():
        ChrTurnDirection(0x0101, 0x0103, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_363C)

    @scena.Lambda('lambda_364A')
    def lambda_364A():
        ChrTurnDirection(0x0102, 0x0103, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_364A)

    ChrTalk(
        0x0103,
        (
            '#0030021828V#020F没有去别的地方的时间了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021829V现在最重要的是调查定期船。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, -2000, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x000C offset: 0x36C1
@scena.Code('func_0C_36C1')
def func_0C_36C1():
    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_36D9',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_36E0')

    def _loc_36D9(): pass

    label('loc_36D9')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_36E0(): pass

    label('loc_36E0')

    @scena.Lambda('lambda_36E6')
    def lambda_36E6():
        ChrTurnDirection(0x0101, 0x0103, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_36E6)

    @scena.Lambda('lambda_36F4')
    def lambda_36F4():
        ChrTurnDirection(0x0102, 0x0103, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_36F4)

    ChrTalk(
        0x0103,
        (
            '#0030021828V#020F没有去别的地方的时间了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021829V现在最重要的是调查定期船。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 2000, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x000D offset: 0x376B
@scena.Code('func_0D_376B')
def func_0D_376B():
    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3783',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_378A')

    def _loc_3783(): pass

    label('loc_3783')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_378A(): pass

    label('loc_378A')

    @scena.Lambda('lambda_3790')
    def lambda_3790():
        ChrTurnDirection(0x0101, 0x0103, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3790)

    @scena.Lambda('lambda_379E')
    def lambda_379E():
        ChrTurnDirection(0x0102, 0x0103, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_379E)

    ChrTalk(
        0x0103,
        (
            '#0030021828V#020F没有去别的地方的时间了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021829V现在最重要的是调查定期船。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 0, 0, -2000, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

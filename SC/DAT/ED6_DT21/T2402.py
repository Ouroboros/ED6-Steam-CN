import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T2402_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2402   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '特蕾莎院长'),
    TXT(0x02, '克拉姆'),
    TXT(0x03, '波利'),
    TXT(0x04, '玛丽'),
    TXT(0x05, '达尼艾尔'),
    TXT(0x06, '鸡'),
    TXT(0x07, '鸡'),
    TXT(0x08, '鸡'),
    TXT(0x09, '目标用照相机'),
    TXT(0x0A, '梅威海道方向'),
    TXT(0x0B, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2402.x'
    header.mapIndex       = 1
    header.bgm            = 15
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x3173
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
        ('ED6_DT07/CH02570._CH', 'ED6_DT07/CH02570P._CP'),
        ('ED6_DT07/CH02590._CH', 'ED6_DT07/CH02590P._CP'),
        ('ED6_DT07/CH02500._CH', 'ED6_DT07/CH02500P._CP'),
        ('ED6_DT07/CH02630._CH', 'ED6_DT07/CH02630P._CP'),
        ('ED6_DT07/CH02640._CH', 'ED6_DT07/CH02640P._CP'),
        ('ED6_DT07/CH01720._CH', 'ED6_DT07/CH01720P._CP'),
        ('ED6_DT26/CH20237._CH', 'ED6_DT26/CH20237P._CP'),
        ('ED6_DT26/CH20272._CH', 'ED6_DT26/CH20272P._CP'),
    ]

# id: 0x10002 offset: 0xEA
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
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = 44200,
            z                   = 240,
            y                   = 18540,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = 44200,
            z                   = 240,
            y                   = 18540,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = 44200,
            z                   = 240,
            y                   = 18540,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0080,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 1060,
            z                   = 0,
            y                   = -23220,
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

# id: 0x10003 offset: 0x22A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x22A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -1820,
            y           = 0,
            z           = 2670,
            range       = 2120,
            dword_10    = 0x000007D0,
            dword_14    = 0x0000157C,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000D,
        ),
    )

# id: 0x10005 offset: 0x24A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -186,
            triggerZ            = 0,
            triggerY            = 32147,
            triggerRange        = 400,
            actorX              = -186,
            actorZ              = 1250,
            actorY              = 32147,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x26E
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2CE',
    )

    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, -3270, 0, 9200, 270)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0416, 2, 0x20B2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_298',
    )

    SetChrFlags(0x0009, 0x0010)

    def _loc_298(): pass

    label('loc_298')

    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x000A, 2970, 0, 27510, 45)
    CreateThread(0x000A, 0x00, 0x00, 0x0004)
    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, 13060, 0, 20500, 90)

    Jump('loc_3AE')

    def _loc_2CE(): pass

    label('loc_2CE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_2D8',
    )

    Jump('loc_3AE')

    def _loc_2D8(): pass

    label('loc_2D8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_348',
    )

    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, 8320, -170, 15270, 270)
    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x000C, -6449, -198, 20931, 90)
    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x000A, 7012, 0, 23975, 180)
    ChrTurnDirection(0x000A, 0x0009, 0)
    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, 4690, 0, 26500, 220)
    CreateThread(0x000B, 0x00, 0x00, 0x0003)

    Jump('loc_3AE')

    def _loc_348(): pass

    label('loc_348')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Return,
        ),
        'loc_3AE',
    )

    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, -9630, 40, 16570, 270)
    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x000C, 9460, 10, 19760, 270)
    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x000A, 2970, 0, 27510, 47)
    CreateThread(0x000A, 0x00, 0x00, 0x0004)
    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, 5190, 0, 29630, 225)

    def _loc_3AE(): pass

    label('loc_3AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_3C1',
    )

    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 0x000E)

    def _loc_3C1(): pass

    label('loc_3C1')

    Return()

# id: 0x0001 offset: 0x3C2
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFE0C00, 0xFFFE5A20, 0x00230067)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_3E6',
    )

    OP_10(0x00, 0x00)
    OP_10(0x02, 0x01)

    def _loc_3E6(): pass

    label('loc_3E6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3FE',
    )

    OP_72(0x0000, 0x0010)
    OP_65(0x00, 0x0001)

    Jump('loc_402')

    def _loc_3FE(): pass

    label('loc_3FE')

    OP_64(0x00, 0x0001)

    def _loc_402(): pass

    label('loc_402')

    Return()

# id: 0x0002 offset: 0x403
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
        'loc_428',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_56A')

    def _loc_428(): pass

    label('loc_428')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_441',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000640)

    Jump('loc_56A')

    def _loc_441(): pass

    label('loc_441')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_45A',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x0000060E)

    Jump('loc_56A')

    def _loc_45A(): pass

    label('loc_45A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_473',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005DC)

    Jump('loc_56A')

    def _loc_473(): pass

    label('loc_473')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_48C',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AA)

    Jump('loc_56A')

    def _loc_48C(): pass

    label('loc_48C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4A5',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x00000578)

    Jump('loc_56A')

    def _loc_4A5(): pass

    label('loc_4A5')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4BE',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x00000546)

    Jump('loc_56A')

    def _loc_4BE(): pass

    label('loc_4BE')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4D7',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000677)

    Jump('loc_56A')

    def _loc_4D7(): pass

    label('loc_4D7')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4F0',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000645)

    Jump('loc_56A')

    def _loc_4F0(): pass

    label('loc_4F0')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_509',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x00000613)

    Jump('loc_56A')

    def _loc_509(): pass

    label('loc_509')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_522',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005E1)

    Jump('loc_56A')

    def _loc_522(): pass

    label('loc_522')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_53B',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AF)

    Jump('loc_56A')

    def _loc_53B(): pass

    label('loc_53B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_554',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x0000057D)

    Jump('loc_56A')

    def _loc_554(): pass

    label('loc_554')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_56A',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x0000054B)

    def _loc_56A(): pass

    label('loc_56A')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_57F',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_56A')

    def _loc_57F(): pass

    label('loc_57F')

    Return()

# id: 0x0003 offset: 0x580
@scena.Code('func_03_580')
def func_03_580():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_663',
    )

    OP_8E(0x00FE, 4965, 37, 23700, 2000, 0x00)
    Sleep(1000)

    OP_8B(0x00FE, 0x00000416, 0x000065E7, 0x0190)
    Sleep(200)

    OP_8E(0x00FE, 1046, 0, 26087, 2000, 0x00)
    Sleep(1000)

    OP_8B(0x00FE, 0x000002D3, 0x00005565, 0x0190)
    Sleep(200)

    OP_8E(0x00FE, 723, 26, 21861, 2000, 0x00)
    Sleep(1000)

    OP_8B(0x00FE, 0x000010BE, 0x00006B64, 0x0190)
    Sleep(200)

    OP_8E(0x00FE, 4286, 0, 27492, 2000, 0x00)
    Sleep(1000)

    OP_8B(0x00FE, 0xFFFFF991, 0x00004BAE, 0x0190)
    Sleep(200)

    OP_8E(0x00FE, -1647, 189, 19374, 2000, 0x00)
    Sleep(1000)

    OP_8B(0x00FE, 0x00001365, 0x00005C94, 0x0190)
    Sleep(200)

    Jump('func_03_580')

    def _loc_663(): pass

    label('loc_663')

    Return()

# id: 0x0004 offset: 0x664
@scena.Code('func_04_664')
def func_04_664():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_687',
    )

    OP_8D(0x00FE, 1350, 26320, 3220, 28450, 2000)

    Jump('func_04_664')

    def _loc_687(): pass

    label('loc_687')

    Return()

# id: 0x0005 offset: 0x688
@scena.Code('func_05_688')
def func_05_688():
    SetChrFlags(0x00FE, 0x0040)
    SetChrFlags(0x00FE, 0x0004)
    OP_8D(0x00FE, -8760, 13210, 8700, 24630, 0)

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            Expr.Rand,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_6B6(): pass

    label('loc_6B6')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_7DA',
    )

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0xBB8),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Gtr,
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0xBB8),
            Expr.Sub,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Lss,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0xBB8),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Gtr,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0xBB8),
            Expr.Sub,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_79F',
    )

    If(
        (
            (Expr.PushLong, 0x2238),
            Expr.Neg,
            (Expr.PushLong, 0x3E8),
            Expr.Add,
            (Expr.GetChrWork, 0xFE, 0x1),
            Expr.Lss,
            (Expr.PushLong, 0x339A),
            (Expr.PushLong, 0x3E8),
            Expr.Add,
            (Expr.GetChrWork, 0xFE, 0x3),
            Expr.Lss,
            Expr.Nez64,
            (Expr.PushLong, 0x21FC),
            (Expr.PushLong, 0x3E8),
            Expr.Sub,
            (Expr.GetChrWork, 0xFE, 0x1),
            Expr.Gtr,
            Expr.Nez64,
            (Expr.PushLong, 0x6036),
            (Expr.PushLong, 0x3E8),
            Expr.Sub,
            (Expr.GetChrWork, 0xFE, 0x3),
            Expr.Gtr,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_774',
    )

    SetChrFlags(0x00FE, 0x0020)
    ChrTurnDirection(0x00FE, 0x0000, 0)
    ClearChrFlags(0x00FE, 0x0020)

    @scena.Lambda('lambda_0761')
    def lambda_0761():
        OP_94(0x00, 0x00FE, 0x00B4, 0x0000012C, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0761)

    Jump('loc_797')

    def _loc_774(): pass

    label('loc_774')

    @scena.Lambda('lambda_077A')
    def lambda_077A():
        OP_8D(0x00FE, -8760, 13210, 8700, 24630, 6000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_077A)

    Sleep(200)

    def _loc_797(): pass

    label('loc_797')

    Sleep(30)

    Jump('loc_7D7')

    def _loc_79F(): pass

    label('loc_79F')

    Sleep(50)

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x28),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7D7',
    )

    TerminateThread(0x00FE, 0x02)

    @scena.Lambda('lambda_07BF')
    def lambda_07BF():
        OP_8D(0x00FE, -8760, 13210, 8700, 24630, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_07BF)

    def _loc_7D7(): pass

    label('loc_7D7')

    Jump('loc_6B6')

    def _loc_7DA(): pass

    label('loc_7DA')

    Return()

# id: 0x0006 offset: 0x7DB
@scena.Code('func_06_7DB')
def func_06_7DB():
    OP_22(0x0074, 0x00, 0x64)
    Sleep(300)

    OP_22(0x0074, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上着锁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0007 offset: 0x821
@scena.Code('func_07_821')
def func_07_821():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_BF6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041D, 3, 0x20EB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A08',
    )

    OP_8C(0x00FE, 90, 0)
    OP_62(0x00FE, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#0410360402V#1714F啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0410360403V#1712F嗯……那个……\n',
            '是约修亚……对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360404V#1054F嗯……\n',
            '玛丽，好久不见。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360405V穿着奇怪的衣服\n',
            '没吓到你吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(500)

    ChrTalk(
        0x00FE,
        (
            '#0410360406V#1716F没、没有那种事！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0410360407V#1710F怎么说呢……\n',
            '好帅哦，那衣服！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360408V#1049F哈哈……谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0410360409V#1718F啊，老师在里面\n',
            '你去见她吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0410360410V#1903F嘿嘿……她一定会很高兴的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)
    OP_A2(0x20EB)

    Jump('loc_BF3')

    def _loc_A08(): pass

    label('loc_A08')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_AF4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_A7D',
    )

    ChrTurnDirection(0x00FE, 0x0102, 0)

    ChrTalk(
        0x00FE,
        (
            '#0410360411V#1718F老师在里面\n',
            '你去见她吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0410360410V#1903F嘿嘿……她一定会很高兴的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AF1')

    def _loc_A7D(): pass

    label('loc_A7D')

    ChrTalk(
        0x00FE,
        (
            '#0410360413V#1716F自从那个奇怪的贝壳出现以后\n',
            '信也没法送到……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0410360414V#1713F在王都的科洛丝姐姐\n',
            '不要紧吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AF1(): pass

    label('loc_AF1')

    Jump('loc_BF3')

    def _loc_AF4(): pass

    label('loc_AF4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_B62',
    )

    ChrTurnDirection(0x00FE, 0x0102, 0)

    ChrTalk(
        0x00FE,
        (
            '#0410360411V#1718F老师在里面\n',
            '你去见她吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0410360410V#1903F嘿嘿……她一定会很高兴的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BF3')

    def _loc_B62(): pass

    label('loc_B62')

    ChrTalk(
        0x00FE,
        (
            '#0410360417V#1718F没有导力器\n',
            '大家也都不在乎。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0410360418V蛋和蔬菜都有，\n',
            '有柴的话还能用火……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0410360419V就算吸尘器不能用\n',
            '有扫帚就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BF3(): pass

    label('loc_BF3')

    Jump('loc_D6C')

    def _loc_BF6(): pass

    label('loc_BF6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_CCD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_C74',
    )

    ChrTalk(
        0x00FE,
        (
            '#0410210345V#1718F我们这里的鸡生的蛋\n',
            '很好吃的哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0410210346V#1900F是不是因为让它们悠闲长大的关系呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CCA')

    def _loc_C74(): pass

    label('loc_C74')

    OP_A2(0x0003)

    ChrTalk(
        0x00FE,
        (
            '#0410210347V#1710F要赶快把蛋收走才行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0410210348V再不赶快\n',
            '会被大家踩烂的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CCA(): pass

    label('loc_CCA')

    Jump('loc_D6C')

    def _loc_CCD(): pass

    label('loc_CCD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Return,
        ),
        'loc_D6C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_D0D',
    )

    ChrTalk(
        0x00FE,
        (
            '#0410210349V#1716F波利真是\n',
            '天真烂漫啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D6C')

    def _loc_D0D(): pass

    label('loc_D0D')

    OP_A2(0x0003)

    ChrTalk(
        0x00FE,
        (
            '#0410210350V#1716F居然说还想见见\n',
            '那个白衣男人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0410210351V波利真是\n',
            '天真烂漫啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D6C(): pass

    label('loc_D6C')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0xD70
@scena.Code('func_08_D70')
def func_08_D70():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1021',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041D, 4, 0x20EC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E5B',
    )

    ChrTurnDirection(0x00FE, 0x0102, 0)

    ChrTalk(
        0x0102,
        (
            '#0020360444V#1040F波利，好久不见呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0430360445V#1733F咦～\n',
            '是约修亚啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0430360446V但是，好像\n',
            '感觉不一样～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0430360447V#1732F不过，还是\n',
            '很帅就行了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360448V#1054F哈哈……谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)
    OP_A2(0x20EC)

    Jump('loc_101E')

    def _loc_E5B(): pass

    label('loc_E5B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_F58',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_ED1',
    )

    ChrTurnDirection(0x00FE, 0x0102, 0)

    ChrTalk(
        0x00FE,
        (
            '#0430360449V#1730F约修亚，好像\n',
            '感觉不一样～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0430360447V#1732F不过，这个\n',
            '也很帅就是了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F55')

    def _loc_ED1(): pass

    label('loc_ED1')

    ChrTalk(
        0x00FE,
        (
            '#0430360451V#1730F外面的士兵，\n',
            '总觉得有些慌张呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0430360452V波利从后面跟他搭话，\n',
            '竟然一下子跳起来了～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0430360453V真好玩～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F55(): pass

    label('loc_F55')

    Jump('loc_101E')

    def _loc_F58(): pass

    label('loc_F58')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_FC7',
    )

    ChrTurnDirection(0x00FE, 0x0102, 0)

    ChrTalk(
        0x00FE,
        (
            '#0430360449V#1730F约修亚，好像\n',
            '感觉不一样～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0430360447V#1732F不过，这个\n',
            '也很帅就是了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_101E')

    def _loc_FC7(): pass

    label('loc_FC7')

    ChrTalk(
        0x00FE,
        (
            '#0430360456V#1733F飞船\n',
            '就是在天上飞的船吧～？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0430360457V为什么海边会有那个～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_101E(): pass

    label('loc_101E')

    Jump('loc_12D2')

    def _loc_1021(): pass

    label('loc_1021')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_10E1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_106D',
    )

    ChrTalk(
        0x00FE,
        (
            '#0430210352V#1730F最近的克拉姆，\n',
            '很努力的帮忙干活哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10DE')

    def _loc_106D(): pass

    label('loc_106D')

    OP_A2(0x0002)

    ChrTalk(
        0x00FE,
        (
            '#0430210353V#1730F最近的克拉姆，\n',
            '很努力的帮忙干活哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0430210354V#1732F不过嘛～恶作剧\n',
            '也很努力就是了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10DE(): pass

    label('loc_10DE')

    Jump('loc_12D2')

    def _loc_10E1(): pass

    label('loc_10E1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Return,
        ),
        'loc_12D2',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1270',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_112C',
    )

    ChrTalk(
        0x00FE,
        (
            '#0430210355V#1732F白衣叔叔，\n',
            '还没来吗～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_126D')

    def _loc_112C(): pass

    label('loc_112C')

    ChrTurnDirection(0x00FE, 0x0109, 0)
    OP_A2(0x0002)

    ChrTalk(
        0x00FE,
        (
            '#0430210356V#1731F啊，是凯文老师～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0430210357V#1732F对了，老师……\n',
            '还能再碰到白衣叔叔吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180210358V#1064F咦……！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180210359V#1068F嗯、嗯～不知道啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180210360V凯文老师\n',
            '也不知道叔叔的行程表啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0430210361V#1733F咦～好想见啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0430210362V#1731F因为他滴溜溜地转\n',
            '好像很开心的样子哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_126D(): pass

    label('loc_126D')

    Jump('loc_12D2')

    def _loc_1270(): pass

    label('loc_1270')

    ChrTalk(
        0x00FE,
        (
            '#0430210363V#1730F真想再见到\n',
            '白衣叔叔啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0430210364V因为他滴溜溜地转\n',
            '好像很开心的样子哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12D2(): pass

    label('loc_12D2')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x12D6
@scena.Code('func_09_12D6')
def func_09_12D6():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_137F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_131B',
    )

    ChrTalk(
        0x00FE,
        (
            '#0420210365V#1720F科洛丝姐姐，\n',
            '还不来玩吗～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_137C')

    def _loc_131B(): pass

    label('loc_131B')

    OP_A2(0x0001)

    ChrTalk(
        0x00FE,
        (
            '#0420210366V#1720F科洛丝姐姐，\n',
            '还不来玩吗～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0420210367V#1721F想请她烤馅饼\n',
            '吃得饱饱的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_137C(): pass

    label('loc_137C')

    Jump('loc_1418')

    def _loc_137F(): pass

    label('loc_137F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Return,
        ),
        'loc_1418',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_13BF',
    )

    ChrTalk(
        0x00FE,
        (
            '#0420210368V#1722F嗯～那个白影\n',
            '是什么呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1418')

    def _loc_13BF(): pass

    label('loc_13BF')

    OP_A2(0x0001)

    ChrTalk(
        0x00FE,
        (
            '#0420210369V#1722F嗯～那个白影\n',
            '是什么呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0420210370V要是幽灵\n',
            '应该会更可怕吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1418(): pass

    label('loc_1418')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x141C
@scena.Code('func_0A_141C')
def func_0A_141C():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_19F9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0416, 2, 0x20B2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_180A',
    )

    EventBegin(0x00)
    Fade(1000)
    OP_6D(-2350, 0, 9510, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2560, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0102, -2300, 0, 8780, 270)
    SetChrPos(0x0101, -2260, 0, 9660, 270)
    SetChrPos(0x00F8, -1470, 0, 8720, 270)
    SetChrPos(0x00F9, -1410, 0, 9580, 270)
    OP_8C(0x00FE, 270, 0)
    OP_4A(0x00FE, 255)
    OP_0D()
    OP_62(0x0009, 0x00000000, 1700, 0x0E, 0x0F, 0x000000FA, 0x02)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#0400360420V#773F#5P呜～劈柴\n',
            '果然好辛苦哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400360421V但是，要是我不做的话\n',
            '老师会为难的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360422V#1040F#2P呀，克拉姆。\n',
            '看起来似乎很有精神啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_8C(0x0009, 90, 600)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0400360423V#774F#6P#3S啊啊啊啊！#2S',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400360424V#3S约、约修亚哥哥！！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360425V#1049F#2P好久不见了，克拉姆。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360426V#1040F听说你在努力帮忙干活，\n',
            '艾丝蒂尔都告诉我了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0400360427V#770F#6P当、当然了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400360428V#770F除草和喂鸡\n',
            '都没偷懒哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400360429V为了老师和大家\n',
            '我非努力不可啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360430V#1053F#2P嗯，就是这股志气。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360431V#1054F虽然现在许多事都很麻烦，\n',
            '但还是希望你能多帮助大家。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360432V为了让状况尽快转好\n',
            '我们也在拼命努力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0400360433V#771F#6P嘿嘿，明白了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400360434V#770F我也不能输给哥哥你们，\n',
            '要努力才行！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x00FE, 0x0010)
    OP_A2(0x0000)
    OP_A2(0x20B2)
    EventEnd(0x00)
    OP_4B(0x00FE, 255)

    Jump('loc_19F6')

    def _loc_180A(): pass

    label('loc_180A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_18F8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1885',
    )

    ChrTurnDirection(0x00FE, 0x0102, 0)

    ChrTalk(
        0x0009,
        (
            '#0400360435V#770F不能输给哥哥你们，\n',
            '要努力才行！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400360436V老师和孤儿院的大家\n',
            '由我来守护！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18F5')

    def _loc_1885(): pass

    label('loc_1885')

    ChrTalk(
        0x0009,
        (
            '#0400360437V#770F老师说了……\n',
            '科洛丝姐姐返回王都后\n',
            '还是在不断努力。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400360438V#771F好～我也不能输给她！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18F5(): pass

    label('loc_18F5')

    Jump('loc_19F6')

    def _loc_18F8(): pass

    label('loc_18F8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_196C',
    )

    ChrTurnDirection(0x00FE, 0x0102, 0)

    ChrTalk(
        0x0009,
        (
            '#0400360435V#770F不能输给哥哥你们，\n',
            '要努力才行！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400360436V老师和孤儿院的大家\n',
            '由我来守护！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19F6')

    def _loc_196C(): pass

    label('loc_196C')

    ChrTalk(
        0x0009,
        (
            '#0400360441V#772F附近的海岸好像\n',
            '停着飞船。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400360442V我真是超级想去看，\n',
            '但是还有活没干完……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400360443V#773F呜～先忍耐一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19F6(): pass

    label('loc_19F6')

    Jump('loc_1D0A')

    def _loc_19F9(): pass

    label('loc_19F9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0245, 7, 0x122F)),
            Expr.Return,
        ),
        'loc_1B3D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1A59',
    )

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x0009,
        (
            '#0400210329V#770F跟哥哥问声好哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400210330V那么，赶快\n',
            '除草吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B3A')

    def _loc_1A59(): pass

    label('loc_1A59')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_1ABE',
    )

    ChrTalk(
        0x0009,
        (
            '#0400210331V#770F这田里的苗\n',
            '才刚刚种下呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400210332V还很幼小柔弱\n',
            '所以要细心除草。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B3A')

    def _loc_1ABE(): pass

    label('loc_1ABE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Return,
        ),
        'loc_1B3A',
    )

    ChrTalk(
        0x0009,
        (
            '#0400210333V#770F杂草如果不连根拔起\n',
            '很快就会再长出来的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400210334V看着吧，杂草们。\n',
            '见识见识克拉姆的力量吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B3A(): pass

    label('loc_1B3A')

    Jump('loc_1D0A')

    def _loc_1B3D(): pass

    label('loc_1B3D')

    ChrTurnDirection(0x00FE, 0x0101, 0)
    OP_A2(0x122F)
    OP_A2(0x0000)

    ChrTalk(
        0x0009,
        (
            '#0400210335V#773F呜～约修亚哥哥\n',
            '不在一起真可惜。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400210336V我这么努力，\n',
            '真想让他看看……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210337V#1003F…………………………\n',
            '…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0400210338V#772F对了，艾丝蒂尔姐姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400210339V如果见到哥哥，\n',
            '一定要跟他说哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400210340V我和大家一起\n',
            '在这里努力呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210341V#1025F克拉姆……………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210342V#1006F…………嗯，明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210343V我一定转达给约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0400210344V#770F嗯，约定了哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1D0A(): pass

    label('loc_1D0A')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x1D0E
@scena.Code('func_0B_1D0E')
def func_0B_1D0E():
    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1D91',
    )

    CreateThread(0x00FE, 0x02, 0x00, 0x000C)
    OP_22(0x0191, 0x00, 0x64)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Rand,
            (Expr.PushLong, 0xA),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1D91',
    )

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['新鲜鸡蛋'], 1)"),
            Expr.Return,
        ),
        'loc_1D91',
    )

    TalkBegin(0x00FE)
    OP_A2(0x0004)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['新鲜鸡蛋']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FE)

    def _loc_1D91(): pass

    label('loc_1D91')

    Return()

# id: 0x000C offset: 0x1D92
@scena.Code('func_0C_1D92')
def func_0C_1D92():
    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x7),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1DAD',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Yield()

    Jump('func_0C_1D92')

    def _loc_1DAD(): pass

    label('loc_1DAD')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x000D offset: 0x1DB8
@scena.Code('func_0D_1DB8')
def func_0D_1DB8():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 6, 0x1216)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2D2A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1DD1',
    )

    Call(0, 0x000F)

    def _loc_1DD1(): pass

    label('loc_1DD1')

    EventBegin(0x00)
    Fade(1000)
    ClearMapFlags(0x00000010)
    SetMapFlags(0x10000000)
    ClearMapFlags(0x00000001)
    SetChrFlags(0x0109, 0x0040)
    SetChrFlags(0x0008, 0x0040)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000F, 0x0080)
    SetChrPos(0x0101, -390, 0, 3340, 0)
    SetChrPos(0x00F7, 450, 0, 2620, 0)
    OP_6D(170, 0, 3940, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(359000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010210001V#1004F#5P啊啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_C8(0x0200, 0x0046, 'C_PLAC05._CH', 0x01, 0x07D0)
    ShowPlaceName('玛西亚孤儿院')

    @scena.Lambda('lambda_1ECD')
    def lambda_1ECD():
        OP_6D(320, 0, 32530, 6000)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_1ECD)

    @scena.Lambda('lambda_1EE5')
    def lambda_1EE5():
        OP_67(0, 9500, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1EE5)

    @scena.Lambda('lambda_1EFD')
    def lambda_1EFD():
        OP_6B(4210, 6000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_1EFD)

    @scena.Lambda('lambda_1F0D')
    def lambda_1F0D():
        OP_6C(45000, 6000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_1F0D)

    WaitForThreadExit(0x0008, 0x0000)
    WaitForThreadExit(0x0008, 0x0001)
    WaitForThreadExit(0x0008, 0x0002)
    WaitForThreadExit(0x0008, 0x0003)
    SetChrPos(0x0101, -620, 0, 17860, 0)
    SetChrPos(0x00F7, 680, 70, 17860, 0)

    @scena.Lambda('lambda_1F53')
    def lambda_1F53():
        OP_8E(0x00FE, -170, 10, 27040, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1F53)

    Sleep(300)

    @scena.Lambda('lambda_1F73')
    def lambda_1F73():
        OP_8E(0x00FE, 1080, 0, 26720, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0000, lambda_1F73)

    Sleep(2000)

    Fade(500)
    OP_6D(510, 0, 28590, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x00F7, 0x0000)
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 6540, 0, 33360, 230)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_204B',
    )

    ChrTalk(
        0x0106,
        (
            '#0050210002V#052F哦，这可真令人吃惊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050210003V烧成那样，\n',
            '居然还能复原。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20A4')

    def _loc_204B(): pass

    label('loc_204B')

    ChrTalk(
        0x0103,
        (
            '#0030210004V#020F呼～听说\n',
            '发生了纵火事件……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030210005V这样看来\n',
            '完全感觉不到呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_20A4(): pass

    label('loc_20A4')

    ChrTalk(
        0x0101,
        (
            '#0010210006V#1008F#6P房子都变新了，\n',
            '还和原来一样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210007V……太好了……真是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '女性的声音',
        (
            '#0390210008V#6P艾丝蒂尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_214C')
    def lambda_214C():
        OP_6D(3480, 0, 30020, 1500)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_214C)

    @scena.Lambda('lambda_2164')
    def lambda_2164():
        OP_67(0, 9500, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2164)

    ChrTurnDirection(0x0101, 0x0008, 400)
    Sleep(300)

    ChrTurnDirection(0x00F7, 0x0008, 400)
    WaitForThreadExit(0x0008, 0x0001)
    WaitForThreadExit(0x0008, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010210009V#1018F#5P特蕾莎老师！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_21C0')
    def lambda_21C0():
        OP_6C(0, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_21C0)

    @scena.Lambda('lambda_21D0')
    def lambda_21D0():
        OP_8E(0x00FE, 3180, 0, 29590, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_21D0)

    Sleep(200)

    @scena.Lambda('lambda_21F0')
    def lambda_21F0():
        OP_8E(0x00FE, 3910, 0, 30310, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_21F0)

    Sleep(500)

    @scena.Lambda('lambda_2210')
    def lambda_2210():
        OP_8E(0x00FE, 3810, 0, 28270, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0000, lambda_2210)

    WaitForThreadExit(0x0008, 0x0000)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x00F7, 0x0000)
    ChrTurnDirection(0x00F7, 0x0008, 400)
    WaitForThreadExit(0x0008, 0x0003)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_23C6',
    )

    ChrTalk(
        0x0008,
        (
            '#0390210010V#751F#2P呵呵。\n',
            '果然是你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390210011V欢迎。\n',
            '终于来了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0106, 400)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0390210012V#753F#2P还有……\n',
            '你是阿加特？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050210013V#051F啊啊。\n',
            '好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0390210014V#750F#2P以前因为克拉姆的事\n',
            '承蒙你关照了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390210015V那之后好久不见了。\n',
            '那时真是承蒙关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050210016V#051F#6P哪里，没事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050210017V倒是我到现在\n',
            '都没来打个招呼，真是抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_251C')

    def _loc_23C6(): pass

    label('loc_23C6')

    ChrTalk(
        0x0008,
        (
            '#0390210010V#751F#2P呵呵。\n',
            '果然是你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390210011V欢迎。\n',
            '终于来了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0103, 400)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0390210020V#753F#2P这位是……\n',
            '初次见面吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030210021V#020F#6P我是这孩子的前辈，\n',
            '游击士雪拉扎德·哈维。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030210022V#021F我听说过不少\n',
            '院长老师的事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030210023V说是茶道高人，\n',
            '也是大家的母亲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0390210024V#751F#2P哎呀……\n',
            '真不好意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_251C(): pass

    label('loc_251C')

    ChrTalk(
        0x0101,
        (
            '#0010210025V#1017F#6P那、那个，孤儿院重建了，\n',
            '真是恭喜了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210026V和从前一模一样我还吃了一惊呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#0390210027V#750F#2P多亏了玛诺利亚村和从业人员们的\n',
            '一番好意，就做成了这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390210028V还是觉得这个气氛\n',
            '才是玛西亚孤儿院啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210029V#1016F#6P啊哈哈……\n',
            '嗯，真的是这样呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210030V#1017F嗯……\n',
            '那些孩子们在里面吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0390210031V#750F#2P刚刚去玛诺利亚村\n',
            '上学去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390210032V每周有一次，巡回神父\n',
            '会来开主日学校……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210033V#1015F#6P这样啊……怎么办呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210034V本想打个招呼，顺便\n',
            '问孩子们一些事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0390210035V#753F#2P事情……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390210036V难道是波利看到\n',
            '『白衣叔叔』的事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210037V#1011F#6P啊，大概是了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210038V是吗，目击者\n',
            '是波利啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210039V确实那孩子，\n',
            '感觉特别敏锐呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0390210040V#751F#2P孩子们回来之前\n',
            '请到里面等吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390210041V我给你们准备茶点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210042V#1011F#6P谢、谢谢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210043V#1003F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_290E',
    )

    OP_62(0x0106, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    OP_22(0x0026, 0x00, 0x64)
    Sleep(1000)

    OP_8C(0x0106, 315, 400)

    ChrTalk(
        0x0106,
        (
            '#0050210044V#052F嗯，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_295A')

    def _loc_290E(): pass

    label('loc_290E')

    OP_62(0x0103, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    OP_22(0x0026, 0x00, 0x64)
    Sleep(1000)

    OP_8C(0x0103, 315, 400)

    ChrTalk(
        0x0103,
        (
            '#0030210045V#023F怎么了、艾丝蒂尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_295A(): pass

    label('loc_295A')

    ChrTalk(
        0x0101,
        (
            '#0010210046V#1025F#6P特蕾莎老师……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210047V约修亚的事……你都没问呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0390210048V#757F#2P…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390210049V#754F……科洛丝\n',
            '告诉我了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390210050V那孩子似乎非常烦恼，\n',
            '于是来找我商量……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390210051V#756F艾丝蒂尔……\n',
            '你也经受了各种痛苦呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210052V#1026F#6P……啊…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210053V#1016F啊哈哈……讨厌啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210054V……要是老师\n',
            '安慰我……我……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210055V#1027F会忍不住的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x0101, 6)
    SetChrSubChip(0x0101, 0)
    OP_0D()
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2B50',
    )

    ChrTalk(
        0x0106,
        (
            '#0050210056V#552F………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B73')

    def _loc_2B50(): pass

    label('loc_2B50')

    ChrTalk(
        0x0103,
        (
            '#0030210057V#522F艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B73(): pass

    label('loc_2B73')

    ChrTalk(
        0x0008,
        (
            '#0390210058V#754F#2P…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390210059V#750F不需要忍耐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390210060V因为最重要的人\n',
            '从自己身边消失了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2BF9')
    def lambda_2BF9():
        OP_6D(3360, 0, 29840, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2BF9)

    OP_8E(0x0008, 3500, 0, 29740, 1000, 0x00)
    SetChrChipByIndex(0x0008, 7)
    SetChrSubChip(0x0008, 0)
    OP_99(0x0008, 0x00, 0x01, 0x000003E8)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010210061V#1027F#6P……啊………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0390210062V#754F#2P什么也不用说了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390210063V虽然无法\n',
            '代替你的母亲……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390210064V暂时就这样……\n',
            '让我抱着你吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2CE2')
    def lambda_2CE2():
        OP_6D(-150, 0, 38820, 4000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2CE2)

    @scena.Lambda('lambda_2CFA')
    def lambda_2CFA():
        OP_67(0, 9500, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2CFA)

    Sleep(2000)

    FadeOut(2000, 0, -1)
    OP_0D()
    Sleep(1000)

    NewScene('ED6_DT21/T2412._SN', 100, 0, 0)
    IdleLoop()

    def _loc_2D2A(): pass

    label('loc_2D2A')

    Return()

# id: 0x000E offset: 0x2D2B
@scena.Code('func_0E_2D2B')
def func_0E_2D2B():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2D3C',
    )

    Call(0, 0x000F)

    def _loc_2D3C(): pass

    label('loc_2D3C')

    EventBegin(0x00)
    ClearMapFlags(0x00000001)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x0101, 470, 0, -2190, 0)
    SetChrPos(0x00F7, -200, 0, -3480, 8)
    SetChrPos(0x0109, 1300, 0, -2780, 0)
    SetChrPos(0x0008, 390, 0, 480, 185)
    SetChrPos(0x0009, 1160, 0, -90, 196)
    SetChrPos(0x000A, -80, 0, 940, 186)
    SetChrPos(0x000B, -1070, 0, 370, 193)
    SetChrPos(0x000C, 2210, 0, 150, 208)
    OP_4A(0x0009, 255)
    OP_4A(0x000A, 255)
    OP_4A(0x000B, 255)
    OP_4A(0x000C, 255)
    OP_6D(1020, 0, -510, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(2000, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2ECC',
    )

    ChrTalk(
        0x0008,
        (
            '#0390210316V#750F艾丝蒂尔、阿加特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390210317V在卢安地区期间，\n',
            '方便的话请再来吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390210318V神父有课的时候\n',
            '也请务必来走走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F60')

    def _loc_2ECC(): pass

    label('loc_2ECC')

    ChrTalk(
        0x0008,
        (
            '#0390210319V#750F艾丝蒂尔。\n',
            '雪拉扎德小姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390210317V在卢安地区期间，\n',
            '方便的话请再来吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390210318V神父也是，授课的时候\n',
            '也请务必来走走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2F60(): pass

    label('loc_2F60')

    ChrTalk(
        0x0101,
        (
            '#0010210322V#1017F#6P嗯，我们会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180210323V#1061F呀～有机会\n',
            '我会再来拜访的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0400210324V#771F凯文哥哥，再见哦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400210325V#770F还有艾丝蒂尔姐姐！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400210326V下次要把约修亚哥哥\n',
            '一起带来哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210327V#1016F#6P啊，嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210328V#1006F虽然不知道要到什么时候，\n',
            '但一定会一起来玩的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1500, 0, -1)
    OP_0D()
    Sleep(500)

    OP_A2(0x10F0)
    NewScene('ED6_DT21/R2200._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000F offset: 0x30BA
@scena.Code('func_0F_30BA')
def func_0F_30BA():
    FadeOut(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)

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
        100,
        0,
        (
            TXT(0x00, '【◇选择雪拉扎德为队友】\n'),
            TXT(0x01, '【◇选择阿加特为队友】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_3134'),
        (0x00000001, 'loc_313A'),
        (-1, 'loc_3140'),
    )

    def _loc_3134(): pass

    label('loc_3134')

    OP_A2(0x1200)

    Jump('loc_3140')

    def _loc_313A(): pass

    label('loc_313A')

    OP_A2(0x1201)

    Jump('loc_3140')

    def _loc_3140(): pass

    label('loc_3140')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_314E',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_3152')

    def _loc_314E(): pass

    label('loc_314E')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_3152(): pass

    label('loc_3152')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

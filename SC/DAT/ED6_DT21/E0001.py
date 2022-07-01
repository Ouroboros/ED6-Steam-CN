import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import E0001_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('E0001   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '凯文神父'),
    TXT(0x02, '目标用照相机'),
    TXT(0x03, '科洛丝'),
    TXT(0x04, '基库'),
    TXT(0x05, '奥利维尔'),
    TXT(0x06, '提妲'),
    TXT(0x07, '雪拉扎德'),
    TXT(0x08, '阿加特'),
    TXT(0x09, '金'),
    TXT(0x0A, '乘客'),
    TXT(0x0B, '乘客'),
    TXT(0x0C, '乘客'),
    TXT(0x0D, '乘客'),
    TXT(0x0E, '提克'),
    TXT(0x0F, '莫莉'),
    TXT(0x10, '安敦'),
    TXT(0x11, '利库斯'),
    TXT(0x12, '法尔茨'),
    TXT(0x13, '诺蒂亚'),
    TXT(0x14, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'event'
    header.mapModel       = 'E0001.x'
    header.mapIndex       = 1
    header.bgm            = 1
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x6688
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
        ('ED6_DT27/CH03080._CH', 'ED6_DT27/CH03080P._CP'),
        ('ED6_DT07/CH00040._CH', 'ED6_DT07/CH00040P._CP'),
        ('ED6_DT07/CH02320._CH', 'ED6_DT07/CH02320P._CP'),
        ('ED6_DT07/CH02323._CH', 'ED6_DT07/CH02323P._CP'),
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT26/CH20311._CH', 'ED6_DT26/CH20311P._CP'),
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT07/CH00050._CH', 'ED6_DT07/CH00050P._CP'),
        ('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP'),
        ('ED6_DT07/CH01470._CH', 'ED6_DT07/CH01470P._CP'),
        ('ED6_DT07/CH01170._CH', 'ED6_DT07/CH01170P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT27/CH03085._CH', 'ED6_DT27/CH03085P._CP'),
        ('ED6_DT07/CH00004._CH', 'ED6_DT07/CH00004P._CP'),
        ('ED6_DT26/CH20236._CH', 'ED6_DT26/CH20236P._CP'),
        ('ED6_DT06/CH20045._CH', 'ED6_DT06/CH20045P._CP'),
        ('ED6_DT26/CH20241._CH', 'ED6_DT26/CH20241P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
    ]

# id: 0x10002 offset: 0x16A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
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
            x                   = 3200,
            z                   = 5000,
            y                   = -4800,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
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
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x01C4,
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
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
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
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 59030,
            z                   = -1800,
            y                   = 54020,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = -2220,
            z                   = 5000,
            y                   = -2440,
            direction           = 128,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = 59030,
            z                   = -1800,
            y                   = 54020,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            x                   = -3200,
            z                   = 5000,
            y                   = 180,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            x                   = -3200,
            z                   = 5000,
            y                   = 3860,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            x                   = -3200,
            z                   = 5000,
            y                   = 4800,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = -480,
            z                   = 5000,
            y                   = -10950,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            x                   = 480,
            z                   = 5000,
            y                   = -10950,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            x                   = -3200,
            z                   = 5000,
            y                   = -4050,
            direction           = 265,
            word_0E             = 0,
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            x                   = -3200,
            z                   = 5000,
            y                   = -5190,
            direction           = 271,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
        ),
    )

# id: 0x10003 offset: 0x3CA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x3CA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x3CA
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x3CA
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 2, 0x1A02)),
            Expr.Return,
        ),
        'loc_3EA',
    )

    SetChrPos(0x000E, 3200, 5000, -4800, 90)
    ClearChrFlags(0x000E, 0x0080)

    Jump('loc_530')

    def _loc_3EA(): pass

    label('loc_3EA')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_414',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0300, 6, 0x1806)),
            Expr.Return,
        ),
        'loc_411',
    )

    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x0017, 0x0080)
    ClearChrFlags(0x0018, 0x0080)

    def _loc_411(): pass

    label('loc_411')

    Jump('loc_530')

    def _loc_414(): pass

    label('loc_414')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000066, 'loc_428'),
        (0x00000067, 'loc_428'),
        (0x00000068, 'loc_428'),
        (-1, 'loc_436'),
    )

    def _loc_428(): pass

    label('loc_428')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 2, 0x1602)),
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_433',
    )

    def _loc_433(): pass

    label('loc_433')

    Jump('loc_436')

    def _loc_436(): pass

    label('loc_436')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 2, 0x1602)),
            Expr.Return,
        ),
        'loc_4B6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_45D',
    )

    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, 3200, 5000, -3870, 180)

    Jump('loc_473')

    def _loc_45D(): pass

    label('loc_45D')

    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x000C, 3200, 5000, -3870, 270)

    def _loc_473(): pass

    label('loc_473')

    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000A, 3200, 5000, -5220, 0)
    SetChrPos(0x000B, 3860, 6000, -4520, 270)
    SetChrChipByIndex(0x000B, 3)
    SetChrSubChip(0x000B, 0)
    ClearChrFlags(0x0019, 0x0080)
    ClearChrFlags(0x001A, 0x0080)

    Jump('loc_530')

    def _loc_4B6(): pass

    label('loc_4B6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 3, 0x1403)),
            Expr.Return,
        ),
        'loc_530',
    )

    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x0011, -1700, 5000, -3890, 0)
    SetChrPos(0x0012, -2750, 5000, -1370, 225)
    SetChrPos(0x0013, -2410, 5000, -6360, 45)
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0014, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 7, 0x1407)),
            Expr.Return,
        ),
        'loc_530',
    )

    SetChrPos(0x000B, 3730, 6000, -5280, 270)
    SetChrChipByIndex(0x000B, 3)
    SetChrSubChip(0x000B, 0)
    ClearChrFlags(0x000B, 0x0080)

    def _loc_530(): pass

    label('loc_530')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 3, 0x10F3)),
            Expr.Return,
        ),
        'loc_541',
    )

    OP_A3(0x10F3)
    Event(0, 0x001E)

    Jump('loc_587')

    def _loc_541(): pass

    label('loc_541')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Return,
        ),
        'loc_552',
    )

    OP_A3(0x10F2)
    Event(0, 0x001D)

    Jump('loc_587')

    def _loc_552(): pass

    label('loc_552')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_563',
    )

    OP_A3(0x10F1)
    Event(0, 0x001C)

    Jump('loc_587')

    def _loc_563(): pass

    label('loc_563')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 3, 0x1003)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_572',
    )

    Event(0, 0x0015)

    Jump('loc_587')

    def _loc_572(): pass

    label('loc_572')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            (Expr.TestScenaFlags, ScenaFlag(0x0300, 6, 0x1806)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_587',
    )

    Event(0, 0x001B)

    def _loc_587(): pass

    label('loc_587')

    Return()

# id: 0x0001 offset: 0x588
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 3, 0x1003)),
            Expr.Return,
        ),
        'loc_599',
    )

    OP_22(0x0079, 0x01, 0x46)
    OP_22(0x01C3, 0x00, 0x64)

    def _loc_599(): pass

    label('loc_599')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5AE',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x53),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_5AE(): pass

    label('loc_5AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 4, 0x1004)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5BF',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_5BF(): pass

    label('loc_5BF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5F1',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x66),
            Expr.Equ,
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x67),
            Expr.Equ,
            Expr.Or,
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x68),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_5F1',
    )

    Call(0, 0x0020)

    def _loc_5F1(): pass

    label('loc_5F1')

    Return()

# id: 0x0002 offset: 0x5F2
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
        'loc_617',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_759')

    def _loc_617(): pass

    label('loc_617')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_630',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000640)

    Jump('loc_759')

    def _loc_630(): pass

    label('loc_630')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_649',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x0000060E)

    Jump('loc_759')

    def _loc_649(): pass

    label('loc_649')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_662',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005DC)

    Jump('loc_759')

    def _loc_662(): pass

    label('loc_662')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_67B',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AA)

    Jump('loc_759')

    def _loc_67B(): pass

    label('loc_67B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_694',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x00000578)

    Jump('loc_759')

    def _loc_694(): pass

    label('loc_694')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6AD',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x00000546)

    Jump('loc_759')

    def _loc_6AD(): pass

    label('loc_6AD')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6C6',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000677)

    Jump('loc_759')

    def _loc_6C6(): pass

    label('loc_6C6')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6DF',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000645)

    Jump('loc_759')

    def _loc_6DF(): pass

    label('loc_6DF')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6F8',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x00000613)

    Jump('loc_759')

    def _loc_6F8(): pass

    label('loc_6F8')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_711',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005E1)

    Jump('loc_759')

    def _loc_711(): pass

    label('loc_711')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_72A',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AF)

    Jump('loc_759')

    def _loc_72A(): pass

    label('loc_72A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_743',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x0000057D)

    Jump('loc_759')

    def _loc_743(): pass

    label('loc_743')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_759',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x0000054B)

    def _loc_759(): pass

    label('loc_759')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_76E',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_759')

    def _loc_76E(): pass

    label('loc_76E')

    Return()

# id: 0x0003 offset: 0x76F
@scena.Code('func_03_76F')
def func_03_76F():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_792',
    )

    OP_8D(0x00FE, -2000, -5830, 320, -2950, 2000)

    Jump('func_03_76F')

    def _loc_792(): pass

    label('loc_792')

    Return()

# id: 0x0004 offset: 0x793
@scena.Code('func_04_793')
def func_04_793():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_7B6',
    )

    OP_8D(0x00FE, -2220, -2440, -3190, -5300, 2000)

    Jump('func_04_793')

    def _loc_7B6(): pass

    label('loc_7B6')

    Return()

# id: 0x0005 offset: 0x7B7
@scena.Code('func_05_7B7')
def func_05_7B7():
    @scena.Lambda('lambda_07BD')
    def lambda_07BD():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_07BD')

    DispatchAsync2(0x0013, 0x0001, lambda_07BD)

    def _loc_7C8(): pass

    label('loc_7C8')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_7DD',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_7C8')

    def _loc_7DD(): pass

    label('loc_7DD')

    Return()

# id: 0x0006 offset: 0x7DE
@scena.Code('func_06_7DE')
def func_06_7DE():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_8B0',
    )

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Leq,
            Expr.Return,
        ),
        'loc_814',
    )

    SetChrSubChip(0x00FE, 0)
    Sleep(50)

    SetChrSubChip(0x00FE, 1)
    Sleep(50)

    SetChrSubChip(0x00FE, 2)

    Jump('loc_82D')

    def _loc_814(): pass

    label('loc_814')

    SetChrSubChip(0x00FE, 0)
    Sleep(150)

    SetChrSubChip(0x00FE, 1)
    Sleep(150)

    SetChrSubChip(0x00FE, 2)

    def _loc_82D(): pass

    label('loc_82D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_83A',
    )

    OP_A3(0x000A)

    Jump('loc_876')

    def _loc_83A(): pass

    label('loc_83A')

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x5),
            Expr.Leq,
            Expr.Return,
        ),
        'loc_876',
    )

    Sleep(80)

    SetChrSubChip(0x00FE, 3)
    Sleep(100)

    SetChrSubChip(0x00FE, 4)
    Sleep(150)

    SetChrSubChip(0x00FE, 3)
    Sleep(100)

    SetChrSubChip(0x00FE, 2)
    OP_A2(0x000A)

    def _loc_876(): pass

    label('loc_876')

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Leq,
            Expr.Return,
        ),
        'loc_899',
    )

    Sleep(50)

    SetChrSubChip(0x00FE, 1)
    Sleep(50)

    Jump('loc_8AD')

    def _loc_899(): pass

    label('loc_899')

    SetChrSubChip(0x00FE, 2)
    Sleep(150)

    SetChrSubChip(0x00FE, 1)
    Sleep(150)

    def _loc_8AD(): pass

    label('loc_8AD')

    Jump('func_06_7DE')

    def _loc_8B0(): pass

    label('loc_8B0')

    Return()

# id: 0x0007 offset: 0x8B1
@scena.Code('func_07_8B1')
def func_07_8B1():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 2, 0x1602)),
            Expr.Return,
        ),
        'loc_AFE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_A7C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 0, 0x1608)),
            Expr.Return,
        ),
        'loc_A75',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9DD',
    )

    TalkBegin(0x000A)
    OP_4A(0x000A, 255)
    OP_A2(0x0000)

    ChrTalk(
        0x000A,
        (
            '#0060240451V#542F其实那派对的事情\n',
            '利贝尔通讯发了报道……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060240452V自那之后，从社交界到市民，\n',
            '尤莉亚小姐的倾慕者都急速增加了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060240453V#045F不过这么多的男人围着一个女人\n',
            '不觉得有些可怜吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240454V#1015F嗯～难道不是自作自受吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x000A, 255)
    TalkEnd(0x000A)

    Jump('loc_A72')

    def _loc_9DD(): pass

    label('loc_9DD')

    TalkBegin(0x000A)
    OP_4A(0x000A, 255)

    ChrTalk(
        0x000A,
        (
            '#0060240451V#542F其实那派对的事情\n',
            '利贝尔通讯发了报道……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060240456V自那之后，从社交界到市民，\n',
            '尤莉亚小姐的倾慕者都急速增加了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x000A, 255)
    TalkEnd(0x000A)

    def _loc_A72(): pass

    label('loc_A72')

    Jump('loc_A79')

    def _loc_A75(): pass

    label('loc_A75')

    Call(0, 0x0019)
    def _loc_A79(): pass

    label('loc_A79')

    Jump('loc_AFB')

    def _loc_A7C(): pass

    label('loc_A7C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 5, 0x1605)),
            Expr.Return,
        ),
        'loc_AF7',
    )

    TalkBegin(0x000A)
    OP_4A(0x000A, 255)

    ChrTalk(
        0x000A,
        (
            '#0060240583V#048F呵呵，连我也\n',
            '不由得想给老师他们\n',
            '写信了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060240584V不知道现在怎样了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x000A, 255)
    TalkEnd(0x000A)

    Jump('loc_AFB')

    def _loc_AF7(): pass

    label('loc_AF7')

    Call(0, 0x0017)

    def _loc_AFB(): pass

    label('loc_AFB')

    Jump('loc_B0A')

    def _loc_AFE(): pass

    label('loc_AFE')

    OP_4A(0x000A, 255)
    Call(0, 0x0016)
    OP_4B(0x000A, 255)
    def _loc_B0A(): pass

    label('loc_B0A')

    Return()

# id: 0x0008 offset: 0xB0B
@scena.Code('func_08_B0B')
def func_08_B0B():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 0, 0x1608)),
            Expr.Return,
        ),
        'loc_CED',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C1C',
    )

    TalkBegin(0x000C)
    CreateThread(0x000C, 0x00, 0x00, 0x0006)
    OP_A2(0x0001)

    ChrTalk(
        0x000C,
        (
            '#0040240457V#034F嘿嘿，不愧是王室亲卫队里\n',
            '倍受称誉的女骑士……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040240458V#032F但是，我热情的火焰\n',
            '绝不会就此熄灭！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040240459V#530F实在不行的话，\n',
            '就全裸弹奏鲁特琴\n',
            '歌唱出对她的爱意吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240460V#1019F呜唔……可以想象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x000C, 255)
    TalkEnd(0x000C)

    Jump('loc_CEA')

    def _loc_C1C(): pass

    label('loc_C1C')

    TalkBegin(0x000C)
    CreateThread(0x000C, 0x00, 0x00, 0x0006)

    ChrTalk(
        0x000C,
        (
            '#0040240457V#034F嘿嘿，不愧是王室亲卫队里\n',
            '倍受称誉的女骑士……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040240458V#032F但是，我热情的火焰\n',
            '绝不会就此熄灭！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040240463V实在不行的话，\n',
            '#530F就全裸弹奏鲁特琴\n',
            '歌唱出对她的爱意吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000C)

    def _loc_CEA(): pass

    label('loc_CEA')

    Jump('loc_CF1')

    def _loc_CED(): pass

    label('loc_CED')

    Call(0, 0x0019)
    def _loc_CF1(): pass

    label('loc_CF1')

    SetChrChipByIndex(0x000C, 17)
    SetChrSubChip(0x000C, 0)
    OP_4B(0x000C, 255)

    Return()

# id: 0x0009 offset: 0xD00
@scena.Code('func_09_D00')
def func_09_D00():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 5, 0x1605)),
            Expr.Return,
        ),
        'loc_DB4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 6, 0x1606)),
            Expr.Return,
        ),
        'loc_DAD',
    )

    TalkBegin(0x000D)
    OP_4A(0x000D, 255)

    ChrTalk(
        0x000D,
        (
            '#0070240407V#061F说到这个，之前在王都\n',
            '第一次看到埃尔赛尤号的时候,\n',
            '感觉真是一艘好漂亮的飞船呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070240408V嘿嘿……不知道还能再见到吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x000D, 255)
    TalkEnd(0x000D)

    Jump('loc_DB1')

    def _loc_DAD(): pass

    label('loc_DAD')

    Call(0, 0x0018)

    def _loc_DB1(): pass

    label('loc_DB1')

    Jump('loc_DB8')

    def _loc_DB4(): pass

    label('loc_DB4')

    Call(0, 0x0017)
    def _loc_DB8(): pass

    label('loc_DB8')

    Return()

# id: 0x000A offset: 0xDB9
@scena.Code('func_0A_DB9')
def func_0A_DB9():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 2, 0x1A02)),
            Expr.Return,
        ),
        'loc_E29',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 6, 0x1A06)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DCF',
    )

    Call(0, 0x001F)

    Jump('loc_E29')

    def _loc_DCF(): pass

    label('loc_DCF')

    TalkBegin(0x000E)

    ChrTalk(
        0x000E,
        (
            '#0030300412V#027F我再稍微\n',
            '吹吹风就回座位。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300413V你也要在着陆前回去哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000E)

    def _loc_E29(): pass

    label('loc_E29')

    Return()

# id: 0x000B offset: 0xE2A
@scena.Code('func_0B_E2A')
def func_0B_E2A():
    TalkBegin(0x0011)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_E70',
    )

    ChrTalk(
        0x00FE,
        (
            '哇～是白隼耶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好酷～\n',
            '是那位姐姐的宠物吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x00FE, 255)

    Jump('loc_EA7')

    def _loc_E70(): pass

    label('loc_E70')

    ChrTalk(
        0x00FE,
        (
            '听说蔡斯\n',
            '有个会自己动的楼梯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好想乘乘看啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EA7(): pass

    label('loc_EA7')

    TalkEnd(0x0011)

    Return()

# id: 0x000C offset: 0xEAB
@scena.Code('func_0C_EAB')
def func_0C_EAB():
    TalkBegin(0x0012)

    ChrTalk(
        0x00FE,
        (
            '比起会动的楼梯，\n',
            '温泉更好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听说是很大很大\n',
            '的澡堂哦～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0012)

    Return()

# id: 0x000D offset: 0xEF4
@scena.Code('func_0D_EF4')
def func_0D_EF4():
    TalkBegin(0x0013)

    ChrTalk(
        0x00FE,
        (
            '喂喂，\n',
            '不要那样动来动去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样会给其它乘客添麻烦的，知道吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0013)

    Return()

# id: 0x000E offset: 0xF42
@scena.Code('func_0E_F42')
def func_0E_F42():
    TalkBegin(0x0014)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_FF0',
    )

    ChrTalk(
        0x00FE,
        (
            '哼哼，别看我这个样子，\n',
            '我可是个军事迷哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我喜欢的战车是帝国陆军用的\n',
            '莱恩福尔特ＬＰ－Ⅲ初期型。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和百日战役当时的后期型相比\n',
            '优点在于它耗油量更小。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1049')

    def _loc_FF0(): pass

    label('loc_FF0')

    ChrTalk(
        0x00FE,
        (
            '嗯～可惜……\n',
            '看不到雷斯顿要塞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '果然那附近的空域\n',
            '好像连定期船也不能接近呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    def _loc_1049(): pass

    label('loc_1049')

    TalkEnd(0x0014)

    Return()

# id: 0x000F offset: 0x104D
@scena.Code('func_0F_104D')
def func_0F_104D():
    TalkBegin(0x0015)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_10B8',
    )

    ChrTalk(
        0x00FE,
        (
            '我正要去柏斯的哈肯大门\n',
            '参观呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然也想顺路去趟洛连特\n',
            '不过还是想先看看哈肯大门啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1148')

    def _loc_10B8(): pass

    label('loc_10B8')

    ChrTalk(
        0x00FE,
        (
            '我正要去柏斯的哈肯大门\n',
            '参观呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在百日战役相关的历史遗迹中，\n',
            '这里可以说是最重要的地方呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我打算花足够的时间\n',
            '仔仔细细看个够。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    def _loc_1148(): pass

    label('loc_1148')

    TalkEnd(0x0015)

    Return()

# id: 0x0010 offset: 0x114C
@scena.Code('func_10_114C')
def func_10_114C():
    TalkBegin(0x0016)

    ChrTalk(
        0x00FE,
        (
            '到了哈肯大门\n',
            '要拍很多照片哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '早就想拍一次\n',
            '那么有魄力的建筑物了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0016)

    Return()

# id: 0x0011 offset: 0x119F
@scena.Code('func_11_119F')
def func_11_119F():
    UnlockAchievement(0x01, 0x01, 0x00, 0x00)
    TalkBegin(0x0017)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_11F9',
    )

    ChrTalk(
        0x00FE,
        (
            '我可不是在王都\n',
            '默默无闻的我了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在某个地方，\n',
            '一定有人需要我！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1267')

    def _loc_11F9(): pass

    label('loc_11F9')

    ChrTalk(
        0x00FE,
        (
            '我可不是在王都\n',
            '默默无闻的我了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今后要积极地\n',
            '向周边地区发展。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在某个地方，\n',
            '一定有人需要我！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0007)

    def _loc_1267(): pass

    label('loc_1267')

    TalkEnd(0x0017)

    Return()

# id: 0x0012 offset: 0x126B
@scena.Code('func_12_126B')
def func_12_126B():
    TalkBegin(0x0018)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_12CC',
    )

    ChrTalk(
        0x00FE,
        (
            '安敦那家伙\n',
            '突然说要去柏斯呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他就是这样一个人，\n',
            '所以我也跟着来看看情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_135E')

    def _loc_12CC(): pass

    label('loc_12CC')

    ChrTalk(
        0x00FE,
        (
            '安敦那家伙\n',
            '突然说要去柏斯呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他就是这样一个人，\n',
            '所以我也跟着来看看情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，虽然不知道会变成怎样，\n',
            '就先悠闲地参观一下城市吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)

    def _loc_135E(): pass

    label('loc_135E')

    TalkEnd(0x0018)

    Return()

# id: 0x0013 offset: 0x1362
@scena.Code('func_13_1362')
def func_13_1362():
    TalkBegin(0x0019)

    ChrTalk(
        0x00FE,
        (
            '啊～可以的话真想\n',
            '再好好享受一下温泉啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0019)

    Return()

# id: 0x0014 offset: 0x1398
@scena.Code('func_14_1398')
def func_14_1398():
    TalkBegin(0x001A)

    ChrTalk(
        0x00FE,
        (
            '速度就是生命,\n',
            '杂志记者真是永不能停歇啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '刚回来就马上要写 \n',
            '关于地震的报告了。 ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x001A)

    Return()

# id: 0x0015 offset: 0x13F8
@scena.Code('func_15_13F8')
def func_15_13F8():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_23(0x0079)
    OP_23(0x01C3)
    OP_D2(0x00260157, 0x0026015C, 0x16)
    LoadEffect(0x00, 'map\\\\mp044_00.eff')
    Sleep(500)

    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0020190142V我的艾丝蒂尔……\n',
            '如太阳般耀眼的你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020190143V和你在一起的时光虽然幸福\n',
            '但同时，也非常痛苦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020190144V就像明亮的光芒会投下浓重的阴影……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020190145V与你在一起相处得越久\n',
            '我，也对自己令人憎恶的本性\n',
            '认识得更加深刻……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020190146V所以，我甚至曾经想过，\n',
            '要是当初没遇见你该多好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Sleep(500)

    SetChrPos(0x0101, 2660, 5000, -4840, 92)
    OP_6D(-3180, 3500, 2710, 0)
    OP_67(0, 4270, -10000, 0)
    OP_6B(12000, 0)
    OP_6C(149000, 0)
    OP_6E(262, 0)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_22(0x0079, 0x01, 0x46)
    OP_22(0x01C3, 0x00, 0x64)
    OP_C8(0x0200, 0x0046, 'C_PLAC07._CH', 0x01, 0x07D0)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_15F3')
    def lambda_15F3():
        OP_6D(3190, 5000, -4610, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_15F3)

    @scena.Lambda('lambda_160B')
    def lambda_160B():
        OP_67(0, 8000, -10000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_160B)

    Sleep(4000)

    @scena.Lambda('lambda_1628')
    def lambda_1628():
        OP_6C(45000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1628)

    @scena.Lambda('lambda_1638')
    def lambda_1638():
        OP_6B(3000, 6000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_1638)

    @scena.Lambda('lambda_1648')
    def lambda_1648():
        OP_6E(262, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1648)

    Sleep(6000)

    SetChrPos(0x0008, -3160, 5000, -1280, 267)
    ClearChrFlags(0x0008, 0x0008)

    ChrTalk(
        0x0101,
        (
            '#0010190147V#588F………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190148V我……\n',
            '伤害了约修亚吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190149V竟然说没遇见我该有多好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190150V……我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '青年的声音',
        (
            '#0180190151V#2P不行，不行啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    SetChrPos(0x0008, -2960, 5000, 1050, 177)
    ClearChrFlags(0x0008, 0x0080)
    Sleep(500)

    @scena.Lambda('lambda_176C')
    def lambda_176C():
        ChrTurnDirection(0x0101, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_176C)

    @scena.Lambda('lambda_177A')
    def lambda_177A():
        OP_6D(1780, 5000, -4750, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_177A)

    @scena.Lambda('lambda_1792')
    def lambda_1792():
        OP_67(0, 8000, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1792)

    @scena.Lambda('lambda_17AA')
    def lambda_17AA():
        OP_6C(314000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_17AA)

    Sleep(800)

    @scena.Lambda('lambda_17BF')
    def lambda_17BF():
        OP_8E(0x0008, -2140, 5000, -1130, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_17BF)

    WaitForThreadExit(0x0008, 0x0000)

    @scena.Lambda('lambda_17DF')
    def lambda_17DF():
        OP_8E(0x0008, -830, 5000, -3800, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_17DF)

    OP_8C(0x0101, 273, 500)
    WaitForThreadExit(0x0008, 0x0000)
    OP_8C(0x0008, 80, 1000)

    ChrTalk(
        0x0101,
        (
            '#0010190152V#4P#587F……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_182D')
    def lambda_182D():
        OP_8E(0x0008, 650, 5000, -4340, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_182D)

    WaitForThreadExit(0x0008, 0x0000)

    NpcTalk(
        0x0008,
        '外表轻浮的青年',
        (
            '#0180190153V#1061F#5P晴空万里的蓝天！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190154V还有，微风轻拂的面庞！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190155V#1060F此情此景，像你这般可爱的女孩，\n',
            '却一副失魂落魄的表情……这可不行啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190156V连女神也会黯然神伤的哦，真的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190157V#4P#587F唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '外表轻浮的青年',
        (
            '#0180190158V#1064F#5P啊，怎么了？\n',
            '我绝对不是可疑人物哦～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190159V#1065F只不过刚一上船\n',
            '我就注意到你了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190160V#1062F看你好像没精打采的样子，\n',
            '就想用我的连珠妙语让你重展笑颜。\n',
            '呵呵，仅此而已啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190161V#4P#004F……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190162V#587F嗯……\n',
            '虽然不知道你是谁，不过，谢谢你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '外表轻浮的青年',
        (
            '#0180190163V#1061F#5P不过说白了，\n',
            '其实，只是搭讪而已啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190164V#1060F怎样，不介意的话，\n',
            '一起到下面的展望室逛逛吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190165V那里可以点饮料喝，\n',
            '让我请客怎样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190166V#4P#587F啊…那、那个……\n',
            '你的好意我心领了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190167V不过我没什么心情……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190168V#003F……对不起……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '外表轻浮的青年',
        (
            '#0180190169V#1065F#5P嗯～这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190170V#1060F那么，搭讪就到此为止，\n',
            '看来还是转回我的本职工作比较好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190171V毕竟引导迷途羔羊也是我的工作嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190172V#4P#004F本职工作……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '外表轻浮的青年',
        (
            '#0180190173V#1071F#5P呵呵，看这个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x0008, 22)
    SetChrSubChip(0x0008, 0)
    OP_0D()
    OP_22(0x00D8, 0x00, 0x64)

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(500)

    PlayEffect(0x00, 0x00, 0x0008, 0, 550, 700, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x0080, 0x00, 0x64)
    OP_83(0x00, 0x02)
    Sleep(1000)

    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '外表轻浮的青年\n',
            '露出佩戴在腰间且刻有杯子图案的吊坠。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#0010190174V#4P#004F咦，这个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190175V记得是七耀教会的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Fade(250)
    SetChrChipByIndex(0x0008, 0)
    SetChrSubChip(0x0008, 0)
    OP_0D()
    Sleep(200)

    NpcTalk(
        0x0008,
        '外表轻浮的青年',
        (
            '#0180190176V#1060F#5P答对了。\n',
            '是『星杯纹章』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190177V我叫凯文·格拉汉姆。\n',
            '别看我这样，我也是七耀教会的神父呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190178V#4P#501F哦～是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190179V#505F……这，是开玩笑的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0180190180V#1061F#5P怎么会？\n',
            '我可是相当严肃认真的神父啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190181V一天三次的礼拜从来没少过，\n',
            '你看，连圣典也是寸步不离地带着……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190182V#1062F………………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190183V#1068F抱歉，我忘在座位上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190184V#4P#007F……真是毫无说服力啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190185V#586F呵呵……\n',
            '真是奇怪的大哥哥啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0180190186V#1061F#5P啊！刚才你笑了一下吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190187V#1061F嗯嗯。\n',
            '对嘛～可爱的女孩子就是要保持笑容才行啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190188V#1060F嗯，总之就是这样，\n',
            '方便的话，让我以神父的身份倾听你的心声吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190189V这绝不是搭讪，我向空之女神发誓。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190190V#4P#586F啊……嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190191V可、可是…\n',
            '要怎样说才好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190192V#587F我……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190193V#003F……呜…………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x0101, 16)
    SetChrFlags(0x0101, 0x0002)
    SetChrSubChip(0x0101, 1)
    OP_0D()
    Sleep(500)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0008,
        (
            '#0180190194V#1064F#5P哎，慢着慢着……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190195V虽然不知道是怎么回事！\n',
            '抱歉，是我不好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190196V#4P#588F呜，哎……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190197V呜呜呜呜……啊啊啊啊啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x0101, 15)
    SetChrFlags(0x0101, 0x0002)
    SetChrSubChip(0x0101, 1)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010190198V#4P#589F#4S呜哇啊啊啊啊啊啊啊……！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0180190199V#1068F#5P啊～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8E(0x0008, 1600, 5000, -5200, 1000, 0x00)
    ChrTurnDirection(0x0008, 0x0101, 400)
    Fade(500)
    SetChrChipByIndex(0x0008, 14)
    SetChrFlags(0x0008, 0x0002)
    SetChrSubChip(0x0008, 5)
    OP_0D()
    OP_1D(0x01)
    SetMapFlags(0x02000000)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0180190200V#1060F#5P好了好了，乖孩子。\n',
            '你一直强忍到现在啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190201V尽情地哭到你觉得好受为止吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010190202V#4P#589F#4S呜啊啊啊啊……！#2S',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190203V#4S呜哇啊啊啊啊啊啊啊啊……！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    CloseMessageWindow()

    @scena.Lambda('lambda_243B')
    def lambda_243B():
        OP_6D(-1960, 5000, 16820, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_243B)

    FadeOut(5000, 0, -1)
    OP_0D()
    OP_23(0x0079)
    OP_23(0x01C3)
    Sleep(2000)

    NewScene('ED6_DT21/E0011._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0016 offset: 0x246D
@scena.Code('func_16_246D')
def func_16_246D():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 7, 0x1407)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2B2D',
    )

    EventBegin(0x00)
    Fade(1000)
    OP_6D(3240, 5000, -4260, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 3200, 5000, -3800, 180)
    ChrTurnDirection(0x000A, 0x0101, 0)
    OP_0D()

    ChrTalk(
        0x000A,
        (
            '#0060220343V#040F艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060220344V难道你是\n',
            '在船内散步吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200148V#1016F#5P嘿嘿，算是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220346V#1011F说起来科洛丝\n',
            '平时怎样回王都的呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220347V让亲卫队的人接送吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060220348V#045F呵呵，怎么会。\n',
            '我是搭定期船回去的哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060220349V#040F新年的仪式，还有女王诞辰庆典。\n',
            '每年都回王都两次呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220350V#1006F#5P那你经常\n',
            '搭乘定期船啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220351V#1015F啊，这样的话……\n',
            '基库怎么办呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220352V在科洛丝之后\n',
            '悠闲地飞来王都？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060220353V#542F啊，基库的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x000B, 15000, 8000, -4760, 270)
    ClearChrFlags(0x000B, 0x0080)
    ChrTurnDirection(0x000A, 0x000B, 400)

    @scena.Lambda('lambda_26F4')
    def lambda_26F4():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_26F4')

    DispatchAsync2(0x000A, 0x0001, lambda_26F4)

    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0060220354V#040F#6P基库，过来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220355V#1004F#5P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x008C, 0x00, 0x64)
    OP_22(0x0197, 0x00, 0x64)

    @scena.Lambda('lambda_275B')
    def lambda_275B():
        OP_6D(10210, 5000, -3880, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_275B)

    @scena.Lambda('lambda_2773')
    def lambda_2773():
        OP_67(0, 6500, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2773)

    @scena.Lambda('lambda_278B')
    def lambda_278B():
        OP_6C(55000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_278B)

    WaitForThreadExit(0x0101, 0x0001)
    OP_4A(0x0011, 255)

    @scena.Lambda('lambda_27A4')
    def lambda_27A4():
        ChrTurnDirection(0x0011, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_27A4)

    OP_A2(0x0009)

    @scena.Lambda('lambda_27B5')
    def lambda_27B5():
        OP_6D(4360, 5000, -4030, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_27B5)

    ClearChrFlags(0x000B, 0x0001)
    OP_8F(0x000B, 3730, 6000, -5280, 5000, 0x00)
    SetChrChipByIndex(0x000B, 3)
    SetChrSubChip(0x000B, 3)
    Sleep(100)

    SetChrSubChip(0x000B, 4)
    Sleep(100)

    SetChrSubChip(0x000B, 0)
    TerminateThread(0x000A, 0x01)
    OP_8C(0x000A, 90, 400)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010220356V#1004F#5P哎哎！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x0101, 400)

    ChrTalk(
        0x000B,
        (
            '#0440220357V#310F啾？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060220358V#542F#6P呵呵，抱歉哦。\n',
            '只是叫你来一下而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220359V#1008F#5P吓，吓我一跳……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220360V基库居然\n',
            '跟着这艘船飞过来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0440220361V#311F啾⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0101, 400)

    ChrTalk(
        0x000A,
        (
            '#0060220362V#041F#4P基库可以以时速１８００塞尔矩\n',
            '进行水平飞行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060220363V这艘定期船的时速\n',
            '差不多也就９００塞尔矩……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060220364V对基库来说\n',
            '一路跟过来的感觉\n',
            '可能就跟散步差不多吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210884V#1011F#5P这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220366V#1016F越来越感觉这小家伙\n',
            '不是一般的厉害了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0440220367V#311F啾～㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060220368V#048F#4P基库会帮忙进行\n',
            '亲卫队的传令工作，\n',
            '也是因为它有这样的速度。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060220369V不能使用导力通信的时候，\n',
            '没有什么东西\n',
            '能比基库更快地传递情报了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220370V#1006F#5P原来如此……\n',
            '逮捕市长的时候也是这样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1407)
    EventEnd(0x00)

    Jump('loc_2B94')

    def _loc_2B2D(): pass

    label('loc_2B2D')

    TalkBegin(0x000A)

    ChrTalk(
        0x000A,
        (
            '#0060220371V#047F这风好舒服啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060220372V#048F看这情况，蔡斯地区\n',
            '说不定也是好天气呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000A)

    def _loc_2B94(): pass

    label('loc_2B94')

    Return()

# id: 0x0017 offset: 0x2B95
@scena.Code('func_17_2B95')
def func_17_2B95():
    EventBegin(0x00)
    FadeOut(500, 0, -1)
    OP_0D()
    OP_4A(0x000A, 255)
    OP_4A(0x000D, 255)
    OP_6D(2940, 5000, -4240, 0)
    OP_67(0, 5740, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(49000, 0)
    OP_6E(258, 0)
    SetChrPos(0x0101, 1300, 5000, -4640, 109)
    ChrTurnDirection(0x000A, 0x0101, 0)
    ChrTurnDirection(0x000D, 0x0101, 0)
    Sleep(500)

    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x000D,
        (
            '#0070240330V#061F啊，姐姐！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0440240503V#311F#2P啾！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060240504V#040F#2P艾丝蒂尔。\n',
            '又出来散步吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240505V#1006F#6P嗯，算是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240506V科洛丝你们已经\n',
            '开始增进感情了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060240507V#048F#2P呵呵，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0070240508V#560F嘿嘿，我和基库\n',
            '也很熟了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x000B, 400)

    ChrTalk(
        0x000D,
        (
            '#0070240509V#061F对吧，基库⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0440240430V#311F#2P啾～㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240511V#1001F#6P啊哈哈，那太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x0101, 400)

    ChrTalk(
        0x000D,
        (
            '#0070240512V#060F啊，另外科洛丝姐姐\n',
            '还告诉我学院祭的事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070240513V姐姐你们\n',
            '在戏剧里面演骑士对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240514V#1008F#6P嘿嘿，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240515V#1006F别看我们这样，\n',
            '那骑士装束还大受好评呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0070240516V#560F哇～真好啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070240517V#561F我也好想看\n',
            '姐姐们演戏啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x000D, 400)

    ChrTalk(
        0x000A,
        (
            '#0060240518V#041F呵呵，明年的学院祭\n',
            '一定要来玩哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060240519V我们一定热烈欢迎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x000A, 400)

    ChrTalk(
        0x000D,
        (
            '#0070240520V#560F哇，可以吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070240521V嗯～那个时候\n',
            '爸爸他们也回来了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070240522V#061F跟爷爷商量一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0101, 400)

    ChrTalk(
        0x000A,
        (
            '#0060240523V#048F#2P呵呵，不过这样一来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060240524V明年也要拜托艾丝蒂尔你们\n',
            '来演出才行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_301E')
    def lambda_301E():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_301E)

    ChrTalk(
        0x0101,
        (
            '#0010240525V#1016F#6P要，要再来一次\n',
            '还是饶了我吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240526V#1025F这么说来……\n',
            '提妲的爸爸妈妈\n',
            '好像因工作出国去了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0070240345V#560F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070240528V到导力器还没有普及的国家\n',
            '去做技术指导了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070240529V已经快两年都没回来了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240530V#1015F#6P嗯～还真久啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240349V有互通书信吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0070240350V#061F嗯，一个月一次吧⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070240351V#060F前不久我写了姐姐们的事，\n',
            '收到了爸妈的回信……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070240534V要我代他们向你们问好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240535V#1016F#6P嘿嘿，是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240354V#1006F话说回来，提妲的父母\n',
            '是怎样的人呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240355V妈妈一定像提妲吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0070240356V#064F嗯～怎么说呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070240357V#060F性格很外向，\n',
            '很有活力的感觉吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070240540V#061F经常会和爷爷\n',
            '扭在一起吵个不停呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240541V#1004F#6P扭、扭在一起……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x000D, 400)

    ChrTalk(
        0x000A,
        (
            '#0060240542V#045F呵呵……\n',
            '真是有活力的妈妈啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x000A, 400)

    ChrTalk(
        0x000D,
        (
            '#0070240543V#067F啊，其实并不是\n',
            '关系不好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070240544V爸爸说，那也是\n',
            '父女之间关系好的表现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240545V#1016F#6P是，是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240363V#1011F那么\n',
            '爸爸是怎样的人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x0101, 400)

    ChrTalk(
        0x000D,
        (
            '#0070240364V#560F嗯，是个很沉静\n',
            '又很壮实的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070240365V听说十多年前\n',
            '曾经当过游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240549V#1004F#6P咦，是这样吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0070240550V#060F由于受伤退出之后\n',
            '就改行当设计技师了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070240551V妈妈倒是说过\n',
            '他以前很有名的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240552V#1006F#6P哦～这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240370V#1001F嗯～等他们回来之后\n',
            '真想见见两人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0070240554V#061F嗯，我也想介绍给姐姐认识，\n',
            '等他们回来以后记得来玩哦⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x000A, 400)

    ChrTalk(
        0x000D,
        (
            '#0070240555V#560F科洛丝姐姐到时候\n',
            '也一定要来玩哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060240556V#041F好，我很乐意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0440240557V#310F#2P啾啾！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x000B, 400)

    ChrTalk(
        0x000D,
        (
            '#0070240558V#061F啊，当然\n',
            '基库也要一起来哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0440240430V#311F#2P啾～㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(500, 0, -1)
    OP_0D()
    OP_6D(1300, 5000, -4640, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrTurnDirection(0x000A, 0x000D, 0)
    ChrTurnDirection(0x000D, 0x000A, 0)
    OP_4B(0x000A, 255)
    OP_4B(0x000D, 255)
    Sleep(500)

    FadeIn(1000, 0)
    OP_A2(0x1605)
    EventEnd(0x00)

    Return()

# id: 0x0018 offset: 0x370C
@scena.Code('func_18_370C')
def func_18_370C():
    EventBegin(0x00)
    FadeOut(500, 0, -1)
    OP_0D()
    OP_4A(0x000A, 255)
    OP_4A(0x000D, 255)
    OP_6D(2940, 5000, -4240, 0)
    OP_67(0, 5740, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(49000, 0)
    OP_6E(258, 0)
    SetChrPos(0x0101, 1300, 5000, -4640, 109)
    ChrTurnDirection(0x000A, 0x0101, 0)
    ChrTurnDirection(0x000D, 0x0101, 0)
    Sleep(500)

    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x000D,
        (
            '#0070240386V#560F对了姐姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070240561V你知道这甲板上的风\n',
            '为什么会这么平静吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240562V#1004F#6P因为风本来就很平静……\n',
            '是这样吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0070240389V#060F不是。\n',
            '其实这个速度和高度\n',
            '应该会引起很大的风的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070240390V不要说聊天了,\n',
            '连站都会站不稳的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240565V#1015F#6P是，是这样吗……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x000D, 400)

    ChrTalk(
        0x000A,
        (
            '#0060240566V#040F也就是说，有什么装置\n',
            '可以克服这一点吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x000A, 400)

    ChrTalk(
        0x000D,
        (
            '#0070240393V#560F是的，这就是让飞船浮上天空的\n',
            '『飞翔引擎』它另外的作用。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070240394V#061F这个机关运转的时候，\n',
            '反重力的力场\n',
            '会覆盖整艘飞船……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070240395V据说这个力场同时也会\n',
            '缓和风与惯性的影响。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240570V#1019F#6P（……科洛丝，你懂吗？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060240571V#045F（一半一半……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x0101, 400)

    ChrTalk(
        0x000D,
        (
            '#0070240398V#060F不过，要启动飞翔引擎\n',
            '需要大量的导力……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070240399V为此就需要\n',
            '高输出功率的『导力引擎』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220485V#1006F#6P原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240401V决定飞船性能的就是引擎，\n',
            '原来指的是这个意思啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060240576V#040F这么说来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060240577V这次，开发给埃尔赛尤号\n',
            '使用的新型引擎，\n',
            '性能似乎相当厉害吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x000A, 400)

    ChrTalk(
        0x000D,
        (
            '#0070240404V#061F是的，我看了性能表，\n',
            '感觉和以前真的有天壤之别。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070240405V我想这都是多亏了开发小组和\n',
            '维修班各位的努力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060240580V#048F这样啊……\n',
            '尤莉亚小姐也会很高兴吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(500, 0, -1)
    OP_0D()
    OP_6D(1300, 5000, -4640, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrTurnDirection(0x000A, 0x000D, 0)
    ChrTurnDirection(0x000D, 0x000A, 0)
    OP_4B(0x000A, 255)
    OP_4B(0x000D, 255)
    Sleep(500)

    FadeIn(1000, 0)
    OP_A2(0x1606)
    EventEnd(0x00)

    Return()

# id: 0x0019 offset: 0x3CAF
@scena.Code('func_19_3CAF')
def func_19_3CAF():
    EventBegin(0x00)
    OP_20(0x000003E8)
    FadeOut(500, 0, -1)
    OP_0D()
    OP_4A(0x000A, 255)
    OP_4A(0x000C, 255)
    SetChrChipByIndex(0x000C, 18)
    SetChrSubChip(0x000C, 0)
    SetChrFlags(0x000C, 0x0020)
    OP_6D(2940, 5000, -4240, 0)
    OP_67(0, 5740, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(49000, 0)
    OP_6E(258, 0)
    SetChrPos(0x0101, 1300, 5000, -4640, 109)
    ChrTurnDirection(0x000A, 0x0101, 0)
    ChrTurnDirection(0x000C, 0x0101, 0)
    Sleep(500)

    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x000C,
        (
            '#0040240409V#031F呀，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040240410V欢迎来到我奥利维尔·朗海姆的\n',
            '独奏会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240411V#1007F#6P你在装模作样些什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240412V#1019F科洛丝也不必特地\n',
            '来捧场嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060240413V#045F#2P呵呵，来到甲板上\n',
            '就听到演奏\n',
            '于是擅自欣赏起来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060240414V#048F真是非常精彩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x000A, 400)
    Sleep(500)

    ChrTalk(
        0x000C,
        (
            '#0040240415V#035F呼……\n',
            '得您称誉实在是光荣至极。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040240416V#037F如何，殿下。\n',
            '到达王都之前请务必和我\n',
            '单独畅谈一下音乐理念……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0440240417V#310F#2P啾～？（瞪）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0040240418V#033F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x000B, 400)

    @scena.Lambda('lambda_3F45')
    def lambda_3F45():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_3F45)

    ChrTalk(
        0x000C,
        (
            '#0040240419V#036F#6P嗯，基库。\n',
            '这叫做社交辞令……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060240420V#040F哎呀，原来是社交辞令吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x000A, 400)

    ChrTalk(
        0x000C,
        (
            '#0040240421V#035F呼，当然\n',
            '如果找到空隙就可以用各种手段\n',
            '把您弄到手……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0440240422V#310F#3S#2P啾！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x0197, 0x00, 0x64)
    OP_22(0x008C, 0x01, 0x64)
    SetChrSubChip(0x000B, 0)
    Sleep(100)

    SetChrSubChip(0x000B, 4)
    Sleep(100)

    SetChrSubChip(0x000B, 3)
    Sleep(100)

    SetChrChipByIndex(0x000B, 2)
    OP_A2(0x0002)
    CreateThread(0x000B, 0x01, 0x00, 0x001A)
    Sleep(500)

    OP_62(0x000C, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x00)
    OP_8C(0x000C, 90, 400)
    Sleep(400)

    OP_8C(0x000C, 0, 400)

    ChrTalk(
        0x000C,
        (
            '#0040240423V#036F哇哇……\n',
            '住手啊基库！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040240424V对不起！\n',
            '都是我不好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240425V#1001F#6P啊哈哈，基库\n',
            '真是个称职的护卫嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A3(0x0002)
    OP_A6(0x0003)
    OP_8E(0x000B, 3860, 6000, -4520, 1500, 0x00)
    OP_8C(0x000B, 275, 0)
    OP_23(0x008C)
    SetChrChipByIndex(0x000B, 3)
    SetChrSubChip(0x000B, 3)
    Sleep(100)

    SetChrSubChip(0x000B, 4)
    Sleep(100)

    SetChrSubChip(0x000B, 0)
    Sleep(100)

    OP_63(0x000C)
    Sleep(500)

    ChrTurnDirection(0x000C, 0x0101, 400)

    ChrTalk(
        0x000C,
        (
            '#0040240426V#034F哈哈哈哈……\n',
            '吃，吃苦头了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060240427V#041F呵呵……\n',
            '不好意思，奥利维尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060240428V#542F不过，刚才那样\n',
            '也是基库的爱情表现。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060240429V它在跟奥利维尔\n',
            '开玩笑呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0440240430V#311F#2P啾～㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x000A, 400)

    ChrTalk(
        0x000C,
        (
            '#0040240431V#035F哎呀呀，这真是光荣之至。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040240432V#030F不过，和利贝尔一样\n',
            '看来殿下的防守真是坚固啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060240433V#048F呵呵……\n',
            '那也要视对象而定啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240434V#1007F#6P真是个随便的家伙……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240435V#1019F你啊，到了王都后\n',
            '可要克制一点哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240436V尤莉亚小姐她们几位\n',
            '可不是喜欢开玩笑的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x0101, 400)

    ChrTalk(
        0x000C,
        (
            '#0040240437V#033F哦哦，那位威风凛凛的女士吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040240438V#030F那种有男子汉气概\n',
            '威风凛凛的女性也令人憧憬呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040240439V#031F呼，如果有机会\n',
            '还真想亲近亲近……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060240440V#049F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000C, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTurnDirection(0x000C, 0x000A, 400)

    ChrTalk(
        0x000C,
        (
            '#0040240441V#033F哎，哎呀？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000A, 400)

    ChrTalk(
        0x0101,
        (
            '#0010240442V#1004F#6P怎么了，科洛丝？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060240443V#043F那个，或许对尤莉亚小姐\n',
            '的确不能开这种玩笑也说不定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060240444V以前在王城的派对上，\n',
            '有人喝醉了酒\n',
            '跑来纠缠我……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060240445V尤莉亚小姐\n',
            '用剑把那个人的衣服……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0040240446V#036F咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240447V#1008F#6P唔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240448V#1013F…………全裸？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0060240449V#540F#2P（咽口水）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0040240450V#036F浑身打冷战……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(500, 0, -1)
    OP_0D()
    OP_6D(1300, 5000, -4640, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_8C(0x000A, 0, 0)
    OP_8C(0x000C, 270, 0)
    OP_4B(0x000A, 255)
    ClearChrFlags(0x000C, 0x0020)
    SetChrChipByIndex(0x000C, 17)
    SetChrSubChip(0x000C, 0)
    OP_4B(0x000C, 255)
    OP_1D(0x49)
    Sleep(500)

    FadeIn(1000, 0)
    OP_A2(0x1608)
    EventEnd(0x00)

    Return()

# id: 0x001A offset: 0x46D1
@scena.Code('func_1A_46D1')
def func_1A_46D1():
    OP_8E(0x000B, 4059, 5500, -3740, 8000, 0x00)
    def _loc_46E5(): pass

    label('loc_46E5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_4705',
    )

    OP_97(0x000B, 0x00000CBC, 0xFFFFF0E2, 0xFFFD40E0, 0x00001F40, 0x0001)
    Yield()

    Jump('loc_46E5')

    def _loc_4705(): pass

    label('loc_4705')

    OP_97(0x000B, 0x00000CBC, 0xFFFFF0E2, 0xFFFD40E0, 0x00001770, 0x0001)
    OP_97(0x000B, 0x00000CBC, 0xFFFFF0E2, 0xFFFD40E0, 0x00000FA0, 0x0001)
    OP_97(0x000B, 0x00000CBC, 0xFFFFF0E2, 0xFFFEEE90, 0x00000BB8, 0x0001)
    OP_97(0x000B, 0x00000CBC, 0xFFFFF0E2, 0xFFFF8AD0, 0x000007D0, 0x0001)
    OP_A2(0x0003)

    Return()

# id: 0x001B offset: 0x475D
@scena.Code('func_1B_475D')
def func_1B_475D():
    EventBegin(0x00)
    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    OP_6D(860, 5000, 20310, 0)
    OP_67(0, 7530, -10000, 0)
    OP_6B(5380, 0)
    OP_6C(188000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 2890, 5000, -4960, 90)
    SetChrChipByIndex(0x0101, 6)
    SetChrSubChip(0x0101, 0)
    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x0017, 0x0080)
    ClearChrFlags(0x0018, 0x0080)

    @scena.Lambda('lambda_47D6')
    def lambda_47D6():
        OP_6D(2520, 5000, -5080, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_47D6)

    @scena.Lambda('lambda_47EE')
    def lambda_47EE():
        OP_6C(236000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_47EE)

    @scena.Lambda('lambda_47FE')
    def lambda_47FE():
        OP_67(0, 6570, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_47FE)

    @scena.Lambda('lambda_4816')
    def lambda_4816():
        OP_6B(4380, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_4816)

    OP_C8(0x0200, 0x0046, 'C_PLAC07._CH', 0x01, 0x07D0)
    FadeIn(1000, 0)
    WaitForThreadExit(0x0101, 0x0000)
    Fade(1000)
    OP_6B(2860, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010280347V#1003F……呼……………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280348V#1007F…………哈……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(500, 0, -1)
    OP_0D()
    OP_AD(0x00240091, 0x0000, 0x0000, 0x000001F4)
    Sleep(1000)

    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010280349V#1007F（这个……\n',
            '  果然是约修亚吧……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280350V#1025F（还戴着围巾\n',
            '装～什么酷呢……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280351V（有没有……\n',
            '  好好吃饭呢……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AE(0x000001F4)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    SetMessageWindowPos(72, 320, 56, 3)
    OP_99(0x0101, 0x00, 0x02, 0x000003E8)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010280352V#1003F（约修亚果然\n',
            '  在利贝尔某处……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280353V（和空贼们合作\n',
            '  打算做些什么……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280354V#1026F（但是……既然这样的话……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280355V（为什么……\n',
            '  为什么不找我帮忙？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(500, 0, -1)
    OP_0D()
    OP_AD(0x00240111, 0x0000, 0x0000, 0x000001F4)
    Sleep(1000)

    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010280356V#1027F（约修亚这笨蛋……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280357V（竟然做出袭击军事基地\n',
            '  这么乱来的事……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280358V（这么冰冷……\n',
            '  和初遇时一样的眼神……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280359V（而且……而且……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetChrSubChip(0x0101, 0)
    OP_AE(0x000001F4)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0101,
        (
            '#0010280360V#1014F#3S为什么看起来\n',
            '跟那男人婆这么要好啊！？',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    CloseMessageWindow()
    OP_4A(0x000E, 255)
    SetChrPos(0x000E, 3160, 5000, 4910, 180)
    ClearChrFlags(0x000E, 0x0080)

    NpcTalk(
        0x000E,
        '女性的声音',
        (
            '#0030280361V#1P艾丝蒂尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010280362V#1004F呜哎！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x0101, 0x0002)
    SetChrChipByIndex(0x0101, 65535)
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x00)

    @scena.Lambda('lambda_4C69')
    def lambda_4C69():
        OP_6D(2650, 5000, -880, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4C69)

    @scena.Lambda('lambda_4C81')
    def lambda_4C81():
        OP_67(0, 8000, -10000, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4C81)

    @scena.Lambda('lambda_4C99')
    def lambda_4C99():
        OP_6E(262, 2500)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_4C99)

    @scena.Lambda('lambda_4CA9')
    def lambda_4CA9():
        OP_6C(315000, 2500)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_4CA9)

    OP_8C(0x0101, 0, 400)
    WaitForThreadExit(0x000E, 0x0002)
    OP_63(0x0101)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010280363V#1015F雪拉姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4CEF')
    def lambda_4CEF():
        OP_6D(2950, 5000, -4260, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4CEF)

    OP_8E(0x000E, 2900, 5000, -3950, 2500, 0x00)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x000E,
        (
            '#0030280364V#021F#2P原来你在这里啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030280365V#020F突然就不见了\n',
            '多让人担心啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030280366V怎么了？\n',
            '晕船了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280367V#1025F#6P啊，嗯……别担心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280368V我并不是不舒服。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0030280369V#020F#2P是吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000E, 90, 400)
    Sleep(500)

    ChrTalk(
        0x000E,
        (
            '#0030280370V#021F#5P呼，今天也是个好天气呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 90, 400)
    Sleep(500)

    ChrTalk(
        0x000E,
        (
            '#0030280371V#026F#5P这样平和的天空下\n',
            '却有人在\n',
            '图谋不轨……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030280372V#022F真是够蠢的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010221183V#1003F#5P嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0030280374V#524F#5P……还有，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030280375V你没有必要把事情一个人憋在心里哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000E, 400)

    ChrTalk(
        0x0101,
        (
            '#0010211879V#1004F#6P咦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0030280377V#524F#5P我倒不会问\n',
            '记者们说了什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030280378V不过现在的你\n',
            '还有很多值得依赖的好同伴。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030280379V当然，也包括我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280380V#1026F#6P………啊………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0030280381V#026F#5P当然，你要自己\n',
            '整理好心情也可以。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030280382V#020F只是，我想我们所有人\n',
            '都很愿意帮助你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030280383V这点千万不要忘记了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280384V#1003F#6P雪拉姐，我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000E, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x000E,
        (
            '#0030280385V#021F#2P呵呵，我要说的就是这些。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030280386V#020F到达柏斯之前\n',
            '虽然还有很多时间……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030280387V不过中途在洛连特着陆的时候\n',
            '可一定要回到座位哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280388V#1025F#6P嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000E, 0, 400)

    @scena.Lambda('lambda_51A0')
    def lambda_51A0():
        OP_6D(2910, 5000, 2500, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_51A0)

    OP_8E(0x000E, 2840, 5100, 6760, 2500, 0x00)
    OP_8C(0x000E, 270, 400)
    OP_72(0x0002, 0x0010)
    OP_72(0x0002, 0x0800)
    OP_6F(0x0002, 0)
    OP_70(0x0002, 0x0000003B)
    OP_22(0x0006, 0x00, 0x64)
    OP_73(0x0002)
    OP_8E(0x000E, 720, 5100, 7110, 2500, 0x00)
    SetChrFlags(0x000E, 0x0080)
    OP_6F(0x0002, 59)
    OP_70(0x0002, 0x00000000)
    OP_22(0x0007, 0x00, 0x64)

    @scena.Lambda('lambda_521F')
    def lambda_521F():
        OP_6D(2780, 5000, -4080, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_521F)

    OP_73(0x0002)
    OP_71(0x0002, 0x0010)
    OP_71(0x0002, 0x0800)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010280389V#1007F#5P依赖吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280390V#1015F是不是去和大家\n',
            '稍微谈谈好呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1806)
    EventEnd(0x00)
    SetMapFlags(0x02000000)
    OP_D6(0x01)

    Return()

# id: 0x001C offset: 0x52AD
@scena.Code('func_1C_52AD')
def func_1C_52AD():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_DB()
    OP_11(0xE6, 0xF0, 0xFF, 0x00000000, 0x0000F230, 0x00000000)
    OP_6D(-7500, -5100, -12260, 0)
    OP_67(0, 3000, -10000, 0)
    OP_6B(2000, 0)
    OP_6C(10000, 0)
    OP_6E(300, 0)
    SetChrPos(0x0101, -200, 5000, 3170, 86)
    SetChrFlags(0x0101, 0x0080)
    OP_C8(0x0200, 0x0046, 'C_PLAC07._CH', 0x01, 0x1388)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    @scena.Lambda('lambda_5347')
    def lambda_5347():
        OP_6D(-2580, 5500, -5200, 9000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_5347)

    @scena.Lambda('lambda_535F')
    def lambda_535F():
        OP_67(0, 7240, -10000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_535F)

    @scena.Lambda('lambda_5377')
    def lambda_5377():
        OP_6C(45000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_5377)

    @scena.Lambda('lambda_5387')
    def lambda_5387():
        OP_6E(505, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_5387)

    @scena.Lambda('lambda_5397')
    def lambda_5397():
        OP_6B(3200, 8000)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_5397)

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0101, 0x0003)
    WaitForThreadExit(0x0008, 0x0000)
    OP_DC()
    NewScene('ED6_DT21/E0011._SN', 113, 0, 0)
    IdleLoop()

    Return()

# id: 0x001D offset: 0x53C5
@scena.Code('func_1D_53C5')
def func_1D_53C5():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_DB()
    OP_11(0xE6, 0xF0, 0xFF, 0x00000000, 0x0000F230, 0x00000000)
    OP_6D(3710, 0, 27280, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3450, 0)
    UnlockAchievement(0x65, 0x01, 0x00, 0x00)
    OP_6C(206000, 0)
    OP_6E(525, 0)
    SetChrPos(0x0101, -200, 5000, 3170, 86)
    SetChrFlags(0x0101, 0x0080)

    @scena.Lambda('lambda_5440')
    def lambda_5440():
        OP_6D(650, 5000, -4910, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_5440)

    @scena.Lambda('lambda_5458')
    def lambda_5458():
        OP_67(0, 8600, -10000, 12000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5458)

    @scena.Lambda('lambda_5470')
    def lambda_5470():
        OP_6C(326000, 13000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_5470)

    @scena.Lambda('lambda_5480')
    def lambda_5480():
        OP_6B(3600, 13000)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_5480)

    OP_C8(0x0200, 0x0046, 'C_PLAC07._CH', 0x01, 0x07D0)
    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    OP_DC()
    NewScene('ED6_DT21/E0011._SN', 114, 0, 0)
    IdleLoop()

    Return()

# id: 0x001E offset: 0x54C3
@scena.Code('func_1E_54C3')
def func_1E_54C3():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_DB()
    OP_11(0xE6, 0xF0, 0xFF, 0x00000000, 0x0000F230, 0x00000000)
    OP_6D(-6810, 5000, 32110, 0)
    OP_67(0, 4910, -10000, 0)
    OP_6B(4680, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    OP_C8(0x0080, 0x0046, 'C_PLAC07._CH', 0x01, 0x03E8)
    FadeIn(1500, 0)

    @scena.Lambda('lambda_5541')
    def lambda_5541():
        OP_6D(1140, 5000, -29550, 9000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5541)

    Sleep(1500)

    Sleep(1500)

    Sleep(1500)

    Sleep(1500)

    FadeOut(1500, 0, -1)
    OP_0D()
    OP_DC()
    NewScene('ED6_DT21/E0011._SN', 113, 0, 0)
    IdleLoop()

    Return()

# id: 0x001F offset: 0x557D
@scena.Code('func_1F_557D')
def func_1F_557D():
    EventBegin(0x00)
    OP_4A(0x000E, 255)
    OP_20(0x000003E8)
    Fade(1000)
    OP_6D(2850, 5000, -4700, 0)
    OP_67(0, 6140, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(57000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 1870, 5000, -4700, 90)
    ChrTurnDirection(0x000E, 0x0101, 0)
    OP_0D()
    OP_21()
    OP_1D(0x53)
    Sleep(500)

    ChrTalk(
        0x000E,
        (
            '#0030300345V#020F#2P哎呀，艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300346V#1025F#6P雪拉姐，你在这里啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300347V#1015F唔……\n',
            '我是不是打扰你了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0030300348V#027F#2P呵呵，你客气什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300349V你想问我关于\n',
            '露茜奥拉姐姐的事对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300350V#1013F#6P啊，嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300351V#1007F以前好像见过，\n',
            '但是几乎完全不记得了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300352V她是怎样的人呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0030300353V#524F#2P这个嘛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300354V#026F『幻惑之铃』露茜奥拉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300355V她能藉由使用铃铛与扇子的『舞蹈』\n',
            '令观众产生幻觉……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300356V#020F在我以前待过的剧团里\n',
            '是被视为台柱的艺人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300357V#1015F#6P这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300358V那种幻觉，\n',
            '是使用导力器产生的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0030300359V#027F#2P不，似乎是自古流传下来的\n',
            '名为『幻术』的技术。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300360V因为姐姐她好像原本就\n',
            '出生于这样的家庭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300361V#1026F#6P原本……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0030300362V#524F#2P当旅行艺人的人\n',
            '大致上分为两种。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300363V由于某种原因背井离乡的人\n',
            '和无依无靠终生孤独的人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300364V#026F露茜奥拉姐姐是前者……\n',
            '而我……是后者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_24(0x0079, 0x3C)
    OP_24(0x01C3, 0x5A)
    Sleep(100)

    OP_24(0x0079, 0x32)
    OP_24(0x01C3, 0x50)
    Sleep(100)

    OP_24(0x0079, 0x28)
    OP_24(0x01C3, 0x46)
    Sleep(100)

    OP_24(0x0079, 0x1E)
    OP_24(0x01C3, 0x3C)
    Sleep(100)

    OP_24(0x0079, 0x14)
    OP_24(0x01C3, 0x32)
    Sleep(100)

    OP_24(0x0079, 0x0A)
    OP_24(0x01C3, 0x28)
    Sleep(100)

    OP_24(0x01C3, 0x1E)
    Sleep(100)

    OP_24(0x01C3, 0x14)
    Sleep(100)

    OP_23(0x0079)
    OP_23(0x01C3)
    OP_0D()
    Sleep(500)

    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('雪拉扎德')

    Talk(
        (
            (TxtCtl.SetColor, 0xC),
            '#0030300365V我被哈维剧团收养\n',
            '是在７岁左右的时候吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300366V那时的我，流落于城市的贫民窟\n',
            '终日过着颓废的生活。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300367V扒窃，掉包，顺手牵羊……\n',
            '真的没干过什么好事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AD(0x0024007F, 0x0000, 0x0000, 0x000001F4)
    Sleep(1500)

    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('雪拉扎德')

    Talk(
        (
            (TxtCtl.SetColor, 0xC),
            '#0030300368V向这样的我\n',
            '伸出援手的\n',
            '就是哈维团长和姐姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300369V他们教给无法相信他人的我\n',
            '何谓家庭的温暖……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300370V为了让我找到自己的容身之处\n',
            '他们教我各种各样的技艺和技术。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300371V舞蹈，驯兽，塔罗牌。\n',
            '全都是姐姐他们传授给我的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AE(0x000001F4)
    Sleep(1000)

    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('雪拉扎德')

    Talk(
        (
            (TxtCtl.SetColor, 0xC),
            '#0030300372V但是……八年前。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300373V在团长死于事故之后，\n',
            '剧团就变得七零八落了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AD(0x00240080, 0x0000, 0x0000, 0x000001F4)
    Sleep(1500)

    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('雪拉扎德')

    Talk(
        (
            (TxtCtl.SetColor, 0xC),
            '#0030300374V我本来打算\n',
            '跟随姐姐的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300375V但她却留下『我有要做的事』这句话后\n',
            '就消失了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300376V穷途末路的我\n',
            '只好去找除团长和姐姐之外\n',
            '唯一可以信赖的人商量。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300377V对──就是当时以游击士身份\n',
            '展开活跃的卡西乌斯老师。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AE(0x000000C8)
    FadeIn(2000, 0)
    Sleep(1000)

    OP_22(0x0079, 0x01, 0x0A)
    OP_22(0x01C3, 0x01, 0x14)
    Sleep(100)

    OP_24(0x01C3, 0x1E)
    Sleep(100)

    OP_24(0x01C3, 0x28)
    Sleep(100)

    OP_24(0x0079, 0x14)
    OP_24(0x01C3, 0x32)
    Sleep(100)

    OP_24(0x0079, 0x1E)
    OP_24(0x01C3, 0x3C)
    Sleep(100)

    OP_24(0x0079, 0x28)
    OP_24(0x01C3, 0x46)
    Sleep(100)

    OP_24(0x0079, 0x32)
    OP_24(0x01C3, 0x50)
    Sleep(100)

    OP_24(0x0079, 0x3C)
    OP_24(0x01C3, 0x5A)
    Sleep(100)

    OP_24(0x0079, 0x46)
    OP_24(0x01C3, 0x64)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010300378V#1026F#6P原来发生过这种事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0030300379V#026F#2P我会成为游击士，\n',
            '是为了尽可能地变强。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300380V在姐姐回来之前，\n',
            '一个人堂堂正正的活下去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300381V#524F但是……八年过去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300382V或许这是个好机会，\n',
            '该重新审视一下自己所走的道路了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300383V#1003F#6P雪拉姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0030300384V#021F#2P呵呵，别摆出那副表情啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300385V#020F就像金先生说的一样\n',
            '我并不打算话也不说就迎面开战。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300386V只是想和姐姐\n',
            '好好地谈一次。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300387V问问她为了什么理由\n',
            '才会与『结社』勾结。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300388V#1025F#6P嗯……说得也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300389V#1018F雪拉姐，加油！\n',
            '我也会尽力帮忙的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0030300390V#021F#2P呵呵，谢谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300391V#027F不过艾丝蒂尔……\n',
            '你真的长大了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300392V#1004F#6P什，什么啊，突然这么说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0030300393V#524F#2P虽说一直以来\n',
            '都觉得你不愧是老师的女儿……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300394V不过或许\n',
            '我还是看走眼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300395V#1015F#6P咦……什么意思？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0030300396V#020F#2P你的力量\n',
            '和老师的力量好像有些许不同。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300397V老师是拥有像海一般胸怀宽广\n',
            '而又气魄宏大的力量……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300398V#021F而你嘛……\n',
            '是拥有照耀自己的同时也照耀他人，\n',
            '像太阳一般的力量。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300399V#1004F#6P哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(500, 0, -1)
    OP_24(0x0079, 0x3C)
    OP_24(0x01C3, 0x50)
    Sleep(100)

    OP_24(0x0079, 0x32)
    OP_24(0x01C3, 0x3C)
    Sleep(100)

    OP_24(0x0079, 0x28)
    OP_24(0x01C3, 0x28)
    Sleep(100)

    OP_24(0x0079, 0x1E)
    OP_24(0x01C3, 0x1E)
    Sleep(100)

    OP_24(0x0079, 0x14)
    OP_24(0x01C3, 0x14)
    Sleep(100)

    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0020300400V我的艾丝蒂尔……\n',
            '如太阳般耀眼的你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(500, 0)
    OP_24(0x0079, 0x1E)
    OP_24(0x01C3, 0x1E)
    Sleep(100)

    OP_24(0x0079, 0x28)
    OP_24(0x01C3, 0x28)
    Sleep(100)

    OP_24(0x0079, 0x32)
    OP_24(0x01C3, 0x3C)
    Sleep(100)

    OP_24(0x0079, 0x3C)
    OP_24(0x01C3, 0x50)
    Sleep(100)

    OP_24(0x0079, 0x46)
    OP_24(0x01C3, 0x64)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010300401V#1025F#6P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0030300402V#026F#2P我想大家都是\n',
            '被你这一点所吸引的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300403V我也是……\n',
            '当然还有约修亚也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300404V#020F你没有必要\n',
            '因为老师而感到压力哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300405V#1012F#6P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300406V#1017F嘿嘿，雪拉姐\n',
            '果然是我的好姐姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300407V每次总是……\n',
            '谢谢你为我打气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0030300408V#027F#2P呵呵，别客气。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300409V#021F作为回报，\n',
            '下次陪我喝酒吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300410V既然当了正游击士\n',
            '酒量也要够强才行啊㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300411V#1019F#6P我倒觉得这点\n',
            '实在一点关系也没有……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_6D(1400, 5000, -4730, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 1400, 5000, -4730, 270)
    OP_8C(0x000E, 90, 0)
    OP_4B(0x000E, 255)
    Sleep(500)

    OP_A2(0x1A06)
    OP_21()
    OP_1D(0x01)
    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0020 offset: 0x6616
@scena.Code('func_20_6616')
def func_20_6616():
    OP_20(0x000003E8)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x49),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(1000)

    OP_21()
    OP_1D(0x49)

    Return()

# id: 0x0021 offset: 0x662D
@scena.Code('func_21_662D')
def func_21_662D():
    OP_20(0x000003E8)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(1000)

    OP_21()
    OP_1D(0x01)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

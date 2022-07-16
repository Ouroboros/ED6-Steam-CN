import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T1200_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1200   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '巴德斯'),
    TXT(0x02, '弗兰'),
    TXT(0x03, '鲁伊'),
    TXT(0x04, '罗亚'),
    TXT(0x05, '菲戈'),
    TXT(0x06, '贝斯卡'),
    TXT(0x07, '梅洛涅'),
    TXT(0x08, '库赖老人'),
    TXT(0x09, '艾丝蒂尔'),
    TXT(0x0A, '莱森村长'),
    TXT(0x0B, '鸡'),
    TXT(0x0C, '鸡'),
    TXT(0x0D, '鸡'),
    TXT(0x0E, '鸡'),
    TXT(0x0F, '拉文努山道方向'),
    TXT(0x10, '拉文努村废坑方向'),
    TXT(0x11, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1200.x'
    header.mapIndex       = 1
    header.bgm            = 15
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x530E
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0xFFFFF9C0,
            dword_04        = 0x00000000,
            dword_08        = 0x00002260,
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
        ('ED6_DT07/CH01060._CH', 'ED6_DT07/CH01060P._CP'),
        ('ED6_DT07/CH01070._CH', 'ED6_DT07/CH01070P._CP'),
        ('ED6_DT07/CH01470._CH', 'ED6_DT07/CH01470P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT07/CH00107._CH', 'ED6_DT07/CH00107P._CP'),
        ('ED6_DT07/CH01490._CH', 'ED6_DT07/CH01490P._CP'),
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH01720._CH', 'ED6_DT07/CH01720P._CP'),
    ]

# id: 0x10002 offset: 0x10A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 4720,
            z                   = 0,
            y                   = 28930,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = 2730,
            z                   = 0,
            y                   = 27400,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = 2610,
            z                   = 0,
            y                   = 28970,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = 25370,
            z                   = -4000,
            y                   = 9110,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            x                   = 14250,
            z                   = -4000,
            y                   = 21420,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            x                   = 20710,
            z                   = -4000,
            y                   = 9840,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            x                   = 18930,
            z                   = -4000,
            y                   = 15140,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 26300,
            z                   = -4000,
            y                   = 19500,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            x                   = 4000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
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
            x                   = 33000,
            z                   = 8000,
            y                   = 36660,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = -4000,
            y                   = 0,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0007,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = -4000,
            y                   = 0,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0007,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = -4000,
            y                   = 0,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0007,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = -4000,
            y                   = 0,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0007,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = -2080,
            z                   = 0,
            y                   = -80,
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
            x                   = 7170,
            z                   = 8000,
            y                   = 78890,
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

# id: 0x10003 offset: 0x30A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x30A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 3260,
            y           = 7000,
            z           = 66870,
            range       = 9230,
            dword_10    = 0x00002710,
            dword_14    = 0x00010C52,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000016,
        ),
        ScenaEventData(
            x           = 5000,
            y           = 0,
            z           = 34240,
            range       = 1500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000019,
        ),
        ScenaEventData(
            x           = 5150,
            y           = 4550,
            z           = 41780,
            range       = 1500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000019,
        ),
        ScenaEventData(
            x           = 5310,
            y           = 0,
            z           = 23020,
            range       = 1500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000001A,
        ),
        ScenaEventData(
            x           = 6000,
            y           = 4400,
            z           = 54640,
            range       = 1500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000001B,
        ),
    )

# id: 0x10005 offset: 0x3AA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -7280,
            triggerZ            = 4460,
            triggerY            = 54000,
            triggerRange        = 800,
            actorX              = -7280,
            actorZ              = 5460,
            actorY              = 54000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0015,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 33020,
            triggerZ            = 8000,
            triggerY            = 35080,
            triggerRange        = 1000,
            actorX              = 33020,
            actorZ              = 9200,
            actorY              = 35080,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0018,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x3F2
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_42E',
    )

    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000A, 0x0008)
    SetChrFlags(0x000F, 0x0080)
    SetChrFlags(0x000F, 0x0008)
    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000C, 0x0008)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000B, 0x0008)
    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000D, 0x0008)

    Jump('loc_51B')

    def _loc_42E(): pass

    label('loc_42E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_44C',
    )

    SetChrFlags(0x000F, 0x0080)
    SetChrFlags(0x000F, 0x0008)
    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000C, 0x0008)

    Jump('loc_51B')

    def _loc_44C(): pass

    label('loc_44C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_488',
    )

    SetChrFlags(0x000F, 0x0080)
    SetChrFlags(0x000F, 0x0008)
    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000D, 0x0008)
    SetChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000E, 0x0008)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000B, 0x0008)
    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000C, 0x0008)

    Jump('loc_51B')

    def _loc_488(): pass

    label('loc_488')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 5, 0x31D)),
            Expr.Return,
        ),
        'loc_49C',
    )

    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000C, 0x0008)

    Jump('loc_51B')

    def _loc_49C(): pass

    label('loc_49C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 4, 0x31C)),
            Expr.Return,
        ),
        'loc_4C1',
    )

    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000C, 0x0008)
    SetChrPos(0x000A, 35020, -3850, 8540, 180)

    Jump('loc_51B')

    def _loc_4C1(): pass

    label('loc_4C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_4EB',
    )

    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000C, 0x0008)
    SetChrPos(0x000A, 35020, -3850, 8540, 180)
    SetChrFlags(0x000A, 0x0010)

    Jump('loc_51B')

    def _loc_4EB(): pass

    label('loc_4EB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_51B',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x000E, 0x01, 0x1000)"),
            Expr.Return,
        ),
        'loc_505',
    )

    SetChrFlags(0x000C, 0x0080)

    Jump('loc_516')

    def _loc_505(): pass

    label('loc_505')

    SetChrPos(0x000C, 4840, 8000, 66800, 180)

    def _loc_516(): pass

    label('loc_516')

    SetChrFlags(0x000A, 0x0010)

    def _loc_51B(): pass

    label('loc_51B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 5, 0x31D)),
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 6, 0x31E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_52C',
    )

    ClearChrFlags(0x0011, 0x0080)

    def _loc_52C(): pass

    label('loc_52C')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x0000006C, 'loc_53C'),
        (0x0000006D, 'loc_565'),
        (-1, 'loc_586'),
    )

    def _loc_53C(): pass

    label('loc_53C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 2, 0x31A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_54E',
    )

    SetScenaFlags(ScenaFlag(0x0063, 2, 0x31A))
    Event(0, 0x0014)

    Jump('loc_562')

    def _loc_54E(): pass

    label('loc_54E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006D, 0, 0x368)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 2, 0x31A)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_562',
    )

    Event(0, 0x0013)

    def _loc_562(): pass

    label('loc_562')

    Jump('loc_586')

    def _loc_565(): pass

    label('loc_565')

    If(
        (
            (Expr.Eval, "OP_29(0x000E, 0x01, 0x0008)"),
            (Expr.Eval, "OP_29(0x000E, 0x01, 0x1000)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_583',
    )

    OP_28(0x000E, 0x01, 0x1000)
    Event(0, 0x0017)

    def _loc_583(): pass

    label('loc_583')

    Jump('loc_586')

    def _loc_586(): pass

    label('loc_586')

    Return()

# id: 0x0001 offset: 0x587
@scena.Code('Init')
def Init():
    OP_16(0x02, 4000, -109000, -92000, 196675)
    OP_72(0x0006, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 1, 0x319)),
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 4, 0x35C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5B2',
    )

    OP_72(0x000A, 0x0004)

    Jump('loc_5B7')

    def _loc_5B2(): pass

    label('loc_5B2')

    OP_71(0x000A, 0x0004)

    def _loc_5B7(): pass

    label('loc_5B7')

    Return()

# id: 0x0002 offset: 0x5B8
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
        'loc_5DD',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_71F')

    def _loc_5DD(): pass

    label('loc_5DD')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5F6',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_71F')

    def _loc_5F6(): pass

    label('loc_5F6')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_60F',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_71F')

    def _loc_60F(): pass

    label('loc_60F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_628',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_71F')

    def _loc_628(): pass

    label('loc_628')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_641',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_71F')

    def _loc_641(): pass

    label('loc_641')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_65A',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_71F')

    def _loc_65A(): pass

    label('loc_65A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_673',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_71F')

    def _loc_673(): pass

    label('loc_673')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_68C',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_71F')

    def _loc_68C(): pass

    label('loc_68C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6A5',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_71F')

    def _loc_6A5(): pass

    label('loc_6A5')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6BE',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_71F')

    def _loc_6BE(): pass

    label('loc_6BE')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6D7',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_71F')

    def _loc_6D7(): pass

    label('loc_6D7')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6F0',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_71F')

    def _loc_6F0(): pass

    label('loc_6F0')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_709',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_71F')

    def _loc_709(): pass

    label('loc_709')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_71F',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_71F(): pass

    label('loc_71F')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_734',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_71F')

    def _loc_734(): pass

    label('loc_734')

    Return()

# id: 0x0003 offset: 0x735
@scena.Code('func_03_735')
def func_03_735():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_781',
    )

    ChrWalkTo(0x00FE, 5060, 0, 28370, 2000, 0x00)
    SetChrDirection(0x00FE, 225, 500)
    Sleep(1000)

    ChrWalkTo(0x00FE, 3990, 0, 29380, 2000, 0x00)
    SetChrDirection(0x00FE, 225, 500)
    Sleep(1000)

    Jump('func_03_735')

    def _loc_781(): pass

    label('loc_781')

    Return()

# id: 0x0004 offset: 0x782
@scena.Code('func_04_782')
def func_04_782():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_816',
    )

    ChrWalkTo(0x00FE, 3520, 0, 28170, 2000, 0x00)
    SetChrDirection(0x00FE, 0, 500)
    Sleep(1000)

    ChrWalkTo(0x00FE, 4190, 0, 27460, 2000, 0x00)
    SetChrDirection(0x00FE, 45, 500)
    Sleep(1000)

    ChrWalkTo(0x00FE, 3760, 0, 26070, 2000, 0x00)
    ChrWalkTo(0x00FE, 3010, 0, 26480, 2000, 0x00)
    SetChrDirection(0x00FE, 45, 500)
    Sleep(1000)

    ChrWalkTo(0x00FE, 2730, 0, 27400, 2000, 0x00)

    Jump('func_04_782')

    def _loc_816(): pass

    label('loc_816')

    Return()

# id: 0x0005 offset: 0x817
@scena.Code('func_05_817')
def func_05_817():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_883',
    )

    ChrWalkTo(0x00FE, 25370, -4000, 11080, 2000, 0x00)
    SetChrDirection(0x00FE, 0, 400)
    Sleep(1000)

    ChrWalkTo(0x00FE, 29220, -4000, 8480, 2000, 0x00)
    SetChrDirection(0x00FE, 180, 400)
    Sleep(1000)

    ChrWalkTo(0x00FE, 22910, -4000, 5610, 2000, 0x00)
    SetChrDirection(0x00FE, 270, 400)
    Sleep(1000)

    Jump('func_05_817')

    def _loc_883(): pass

    label('loc_883')

    Return()

# id: 0x0006 offset: 0x884
@scena.Code('func_06_884')
def func_06_884():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_8D0',
    )

    ChrWalkTo(0x00FE, 16930, -4000, 16010, 2000, 0x00)
    SetChrDirection(0x00FE, 0, 500)
    Sleep(1000)

    ChrWalkTo(0x00FE, 21410, -4000, 13880, 2000, 0x00)
    SetChrDirection(0x00FE, 0, 500)
    Sleep(1000)

    Jump('func_06_884')

    def _loc_8D0(): pass

    label('loc_8D0')

    Return()

# id: 0x0007 offset: 0x8D1
@scena.Code('func_07_8D1')
def func_07_8D1():
    SetChrFlags(0x00FE, 0x0040)
    SetChrFlags(0x00FE, 0x0004)
    OP_8D(0x00FE, 12660, 3550, 26000, 18020, 0)

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

    def _loc_8FF(): pass

    label('loc_8FF')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_A22',
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
        'loc_9E7',
    )

    If(
        (
            (Expr.PushLong, 0x3174),
            (Expr.PushLong, 0x3E8),
            Expr.Add,
            (Expr.GetChrWork, 0xFE, 0x1),
            Expr.Lss,
            (Expr.PushLong, 0xDDE),
            (Expr.PushLong, 0x3E8),
            Expr.Add,
            (Expr.GetChrWork, 0xFE, 0x3),
            Expr.Lss,
            Expr.Nez64,
            (Expr.PushLong, 0x6590),
            (Expr.PushLong, 0x3E8),
            Expr.Sub,
            (Expr.GetChrWork, 0xFE, 0x1),
            Expr.Gtr,
            Expr.Nez64,
            (Expr.PushLong, 0x4664),
            (Expr.PushLong, 0x3E8),
            Expr.Sub,
            (Expr.GetChrWork, 0xFE, 0x3),
            Expr.Gtr,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_9BC',
    )

    SetChrFlags(0x00FE, 0x0020)
    ChrTurnDirection(0x00FE, 0x0000, 0)
    ClearChrFlags(0x00FE, 0x0020)

    @scena.Lambda('lambda_09A9')
    def lambda_09A9():
        OP_94(0x00, 0x00FE, 0x00B4, 0x0000012C, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_09A9)

    Jump('loc_9DF')

    def _loc_9BC(): pass

    label('loc_9BC')

    @scena.Lambda('lambda_09C2')
    def lambda_09C2():
        OP_8D(0x00FE, 12660, 3550, 26000, 18020, 6000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_09C2)

    Sleep(200)

    def _loc_9DF(): pass

    label('loc_9DF')

    Sleep(30)

    Jump('loc_A1F')

    def _loc_9E7(): pass

    label('loc_9E7')

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
        'loc_A1F',
    )

    TerminateThread(0x00FE, 0x02)

    @scena.Lambda('lambda_0A07')
    def lambda_0A07():
        OP_8D(0x00FE, 12660, 3550, 26000, 18020, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0A07)

    def _loc_A1F(): pass

    label('loc_A1F')

    Jump('loc_8FF')

    def _loc_A22(): pass

    label('loc_A22')

    Return()

# id: 0x0008 offset: 0xA23
@scena.Code('func_08_A23')
def func_08_A23():
    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AAD',
    )

    CreateThread(0x00FE, 0x02, 0x00, 0x0009)
    PlaySE(401, 0x00, 0x64)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Rand,
            (Expr.PushLong, 0xA),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_AAD',
    )

    If(
        (
            (Expr.Eval, "AddItem(0x038B, 1)"),
            Expr.Return,
        ),
        'loc_AAD',
    )

    TalkBegin(0x00FE)
    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    SetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '新鲜鸡蛋',
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

    def _loc_AAD(): pass

    label('loc_AAD')

    Return()

# id: 0x0009 offset: 0xAAE
@scena.Code('func_09_AAE')
def func_09_AAE():
    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x7),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_AC9',
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

    Jump('func_09_AAE')

    def _loc_AC9(): pass

    label('loc_AC9')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x000A offset: 0xAD4
@scena.Code('func_0A_AD4')
def func_0A_AD4():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_B74',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B40',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '啊～啊， \n',
            '我可是在柏斯出生的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为柏斯市\n',
            '没有果树园，\n',
            '我都帮不上什么忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B71')

    def _loc_B40(): pass

    label('loc_B40')

    ChrTalk(
        0x00FE,
        (
            '因为我在柏斯市出生，\n',
            '所以无法在果树园帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B71(): pass

    label('loc_B71')

    Jump('loc_E71')

    def _loc_B74(): pass

    label('loc_B74')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_BAD',
    )

    ChrTalk(
        0x00FE,
        (
            '大人也有\n',
            '大人要做的事情啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真头痛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E71')

    def _loc_BAD(): pass

    label('loc_BAD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_BF2',
    )

    ChrTalk(
        0x00FE,
        (
            '库赖爷爷和贝斯卡\n',
            '又在吵架了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近经常能听到呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E71')

    def _loc_BF2(): pass

    label('loc_BF2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 5, 0x31D)),
            Expr.Return,
        ),
        'loc_CF1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C9A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '我是从鲁伊那里听说的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '姐姐你们\n',
            '是游击士对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好厉害，\n',
            '女人也能够成为游击士啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我觉得如果不是像阿加特\n',
            '那样厉害是办不到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CEE')

    def _loc_C9A(): pass

    label('loc_C9A')

    ChrTalk(
        0x00FE,
        (
            '原来女人也能够\n',
            '成为游击士啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我觉得如果不是像阿加特\n',
            '那样厉害是办不到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CEE(): pass

    label('loc_CEE')

    Jump('loc_E71')

    def _loc_CF1(): pass

    label('loc_CF1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 4, 0x31C)),
            Expr.Return,
        ),
        'loc_DEC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D8B',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '鲁伊的话不可信，\n',
            '也有他自身的原因吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也有人说，\n',
            '说不定那怪影可能是龙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '龙是很久以前的生物吧？\n',
            '这种说法就更不可信了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DE9')

    def _loc_D8B(): pass

    label('loc_D8B')

    ChrTalk(
        0x00FE,
        (
            '鲁伊的话不可信，\n',
            '也有他自身的原因吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '龙是很久以前的生物吧？\n',
            '这种说法就更不可信了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DE9(): pass

    label('loc_DE9')

    Jump('loc_E71')

    def _loc_DEC(): pass

    label('loc_DEC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_E29',
    )

    ChrTalk(
        0x00FE,
        (
            '最近，\n',
            '鲁伊都没过来玩啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '发生什么事了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E71')

    def _loc_E29(): pass

    label('loc_E29')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_E71',
    )

    ChrTalk(
        0x00FE,
        (
            '你们说鲁伊啊，\n',
            '他应该是看错了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不会是星星看多了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E71(): pass

    label('loc_E71')

    TalkEnd(0x0008)

    Return()

# id: 0x000B offset: 0xE75
@scena.Code('func_0B_E75')
def func_0B_E75():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_F07',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_ED7',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '如果出生在商人之家，\n',
            '可能会更麻烦吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为巴德斯\n',
            '可不擅长学习。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F04')

    def _loc_ED7(): pass

    label('loc_ED7')

    ChrTalk(
        0x00FE,
        (
            '如果出生在商人之家，\n',
            '我想那一定更痛苦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F04(): pass

    label('loc_F04')

    Jump('loc_11FD')

    def _loc_F07(): pass

    label('loc_F07')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_F3E',
    )

    ChrTalk(
        0x00FE,
        (
            '既然住在同一个村里，\n',
            '大家应该和平友好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11FD')

    def _loc_F3E(): pass

    label('loc_F3E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_FA2',
    )

    ChrTalk(
        0x00FE,
        (
            '贝斯卡是前不久\n',
            '才来到这个村里的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他是个平时很温柔，\n',
            '认真起来也非常酷的大哥哥。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11FD')

    def _loc_FA2(): pass

    label('loc_FA2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 5, 0x31D)),
            Expr.Return,
        ),
        'loc_108F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1046',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '事到如今，\n',
            '巴德斯还在说什么啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从今以后\n',
            '将是女性的时代了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看罗亚家就知道，\n',
            '他夫人比他厉害多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还有，女王陛下也是女性。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_108C')

    def _loc_1046(): pass

    label('loc_1046')

    ChrTalk(
        0x00FE,
        (
            '事到如今，\n',
            '巴德斯还在说什么啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从今以后\n',
            '将是女性的时代了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_108C(): pass

    label('loc_108C')

    Jump('loc_11FD')

    def _loc_108F(): pass

    label('loc_108F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 4, 0x31C)),
            Expr.Return,
        ),
        'loc_1174',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_111D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '我觉得巴德斯\n',
            '说得一点都没错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听说爸爸们小的时候，\n',
            '那一带附近还有龙哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要一次就好，\n',
            '我也想见见龙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1171')

    def _loc_111D(): pass

    label('loc_111D')

    ChrTalk(
        0x00FE,
        (
            '听说爸爸们小的时候，\n',
            '那一带附近还有龙哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要一次就好，\n',
            '我也想见见龙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1171(): pass

    label('loc_1171')

    Jump('loc_11FD')

    def _loc_1174(): pass

    label('loc_1174')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_11CA',
    )

    ChrTalk(
        0x00FE,
        (
            '咦……\n',
            '大姐姐你们是客人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要找村长家的话，\n',
            '登上里面的坡道就是了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11FD')

    def _loc_11CA(): pass

    label('loc_11CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_11FD',
    )

    ChrTalk(
        0x00FE,
        (
            '大姐姐，你们是谁？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '柏斯的商人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11FD(): pass

    label('loc_11FD')

    TalkEnd(0x0009)

    Return()

# id: 0x000C offset: 0x1201
@scena.Code('func_0C_1201')
def func_0C_1201():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_1515',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0071, 6, 0x38E)),
            Expr.Return,
        ),
        'loc_12F1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_12AC',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '过去，\n',
            '这里曾经发生过一场大战。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '村里有好几个人\n',
            '在战争中死去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也想和\n',
            '帝国的人交朋友……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是……\n',
            '我讨厌悲伤的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12EE')

    def _loc_12AC(): pass

    label('loc_12AC')

    ChrTalk(
        0x00FE,
        (
            '我也想和\n',
            '帝国的人交朋友……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是……\n',
            '我讨厌悲伤的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12EE(): pass

    label('loc_12EE')

    Jump('loc_1512')

    def _loc_12F1(): pass

    label('loc_12F1')

    SetScenaFlags(ScenaFlag(0x0071, 6, 0x38E))
    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '啊，是姐姐啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#001F你好啊～鲁伊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那之后，\n',
            '军队就来把姐姐们带走了，\n',
            '把我吓死了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '姐姐们明明\n',
            '什么坏事也没有做啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没什么事吧？\n',
            '他们没有刁难你们吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#506F哎呀呀，\n',
            '让你为我们担心了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#006F没事啦，\n',
            '你看我现在不是很有活力吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，那就好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我所看到的那个，\n',
            '果然是飞艇啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '姐姐， \n',
            '谢谢你为我作证！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#505F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过最后反正会被\n',
            '王国军证明清楚，\n',
            '我的心里还真不是滋味啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '他们还把我们\n',
            '误认为空贼而抓走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F算了，\n',
            '这次虽然有些丢脸，\n',
            '不过我们还是守住了约定……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '这不是挺好吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1512(): pass

    label('loc_1512')

    Jump('loc_2543')

    def _loc_1515(): pass

    label('loc_1515')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_1771',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_174B',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    SetScenaFlags(ScenaFlag(0x0071, 6, 0x38E))
    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '啊，是姐姐啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#001F你好啊～鲁伊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那之后，\n',
            '军队就来把姐姐们带走了，\n',
            '把我吓死了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '姐姐们明明\n',
            '什么坏事也没有做啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没什么事吧？\n',
            '他们没有刁难你们吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#506F哎呀呀，\n',
            '让你为我们担心了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#006F没事啦，\n',
            '你看我现在不是很有活力吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，那就好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我所看到的那个，\n',
            '果然是飞艇啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '姐姐， \n',
            '谢谢你为我作证！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#505F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过最后反正会被\n',
            '王国军证明清楚，\n',
            '我的心里还真不是滋味啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '他们还把我们\n',
            '误认为空贼而抓走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F算了，\n',
            '这次虽然有些丢脸，\n',
            '不过我们还是守住了约定……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '这不是挺好吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_176E')

    def _loc_174B(): pass

    label('loc_174B')

    ChrTalk(
        0x00FE,
        (
            '姐姐，\n',
            '谢谢你们为我的话作证！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_176E(): pass

    label('loc_176E')

    Jump('loc_2543')

    def _loc_1771(): pass

    label('loc_1771')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 5, 0x31D)),
            Expr.Return,
        ),
        'loc_1896',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1879',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '是、是姐姐你们啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎样，找到什么线索了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#006F嗯～\n',
            '还不能说是很清楚的线索……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过，你所看到的东西\n',
            '真的不是什么梦境。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '真的！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#006F现在我们要开始仔细调查，\n',
            '你就等着好消息吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯！\n',
            '大姐姐你们要加油啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1893')

    def _loc_1879(): pass

    label('loc_1879')

    ChrTalk(
        0x00FE,
        (
            '大姐姐你们要加油啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1893(): pass

    label('loc_1893')

    Jump('loc_2543')

    def _loc_1896(): pass

    label('loc_1896')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 4, 0x31C)),
            Expr.Return,
        ),
        'loc_18FF',
    )

    ChrTalk(
        0x00FE,
        (
            '在空中飞翔的两个影子\n',
            '向北方飞去了，\n',
            '然后就那样看不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我敢说\n',
            '那个绝对不是在做梦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2543')

    def _loc_18FF(): pass

    label('loc_18FF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_251E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 4, 0x31C)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 3, 0x31B)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_24DF',
    )

    SetScenaFlags(ScenaFlag(0x0063, 4, 0x31C))
    OP_28(0x0036, 0x01, 0x0008)
    OP_28(0x0036, 0x01, 0x0010)
    EventBegin(0x00)
    Fade(1000)
    CameraMove(34870, -3850, 9830, 0)
    CameraSetDistance(2800, 0)
    OP_6C(135000, 0)
    SetChrPos(0x0101, 35122, -3850, 10423, 180)
    SetChrPos(0x0102, 35484, -3850, 11571, 180)
    SetChrPos(0x0103, 34518, -3850, 11700, 180)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    OP_0D()

    ChrTalk(
        0x00FE,
        (
            '#1190021610V哎～\n',
            '我没见过大姐姐你们呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1190021611V是来这里买水果的商人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021612V#006F呵呵，不是呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021613V不瞒你说，我们是游击士哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1190021614V游击士？\n',
            '和阿加特大哥哥一样吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1190021615V可是大姐姐，\n',
            '你看起来好像不是很强呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010021616V#007F呜～\n',
            '说得还真直接……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021617V#006F那么，让你见识一下我华丽的棒术吧，\n',
            '这样就肯定不会再说同样的话了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(1500)
    SetChrChipByIndex(0x0101, 10)
    OP_6C(0, 1500)
    Sleep(500)

    Fade(250)
    SetChrChipByIndex(0x0101, 8)
    PlaySE(126, 0x01, 0x64)

    @scena.Lambda('lambda_1B37')
    def lambda_1B37():
        OP_99(0x00FE, 0x00, 0x07, 3000)
        Yield()

        Jump('lambda_1B37')

    DispatchAsync2(0x0101, 0x0000, lambda_1B37)

    Sleep(2000)

    OP_62(0x00FE, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    ChrJumpToRelative(0x00FE, 0, 0, 0, 800, 8000)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '#1190021618V哇、哇哇！\n',
            '棍子耍得骨碌转，好厉害呀！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    TerminateThread(0x0101, 0xFF)
    OP_23(0x007E)
    OP_99(0x0101, 0x00, 0x0A, 2000)
    PlaySE(500, 0x00, 0x64)
    OP_99(0x0101, 0x0B, 0x13, 2000)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010021619V#502F哈哈，知道我的厉害了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)

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
    OP_6C(135000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010021620V#001F再给你看个更厉害的招式……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021621V#017F艾丝蒂尔，闹过头了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020021622V#010F对了……\n',
            '你就是鲁伊吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1190021623V啊，是呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1190021624V为什么哥哥会知道我的名字呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021625V#010F是从村长那里听说的。\n',
            '你看到了夜空中飞过的影子是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020021626V我们想听你说说当时的情景。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1190021627V哎，可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1190021628V士兵叔叔已经调查过了，\n',
            '什么也没找到……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021629V#010F嗯，那样也没关系的。\n',
            '给我们讲一遍那晚发生的事好吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020021630V越详细越好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1190021631V啊～嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1190021632V…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1190021633V那个那个……\n',
            '我非常喜欢看星星。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1190021634V所以，我经常半夜\n',
            '从家里跑出来到这里看星星……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1190021635V前几天的晚上，\n',
            '我看到有两个影子在夜空中飞过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021636V#004F哎，先停一下……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021637V夜空中飞过的影子有两个？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1190021638V是啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1190021639V啊，不过大小不一样哦。\n',
            '就好像是大人带着孩子似的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021640V#002F大小不同的两个影子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021641V#022F定期船和空贼飞艇……\n',
            '这么想的话就说得通了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021642V#012F确实，在森林里见过的空贼飞艇\n',
            '比定期船体形要小呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1190021643V然后，那两个影子\n',
            '就向着北边的方向飞去……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1190021644V接着就那样消失了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021645V#002F北边的方向……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021646V#020F从村子的后村口出去，\n',
            '会有一条通往北边的山道。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021647V山道尽头是一个七耀石矿山，\n',
            '不过据说那里很久之前就成了废坑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1190021648V士兵叔叔们虽然把北面的山道\n',
            '彻底地搜查了一遍，\n',
            '但是什么也没找到呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1190021649V所以呢，\n',
            '他们都说是我睡迷糊了梦见的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1190021650V而且……\n',
            '他们还把我当成傻瓜嘲笑了一番呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '说着说着，小男孩的眼眶已经湿润了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0101,
        (
            '#0010021651V#004F啊，怎么了……\n',
            '男孩子不能这么轻易地哭哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_92(0x0101, 0x00FE, 800, 3000, 0x00)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010021652V#006F我们和士兵们可不一样哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021653V你说的话绝对不是在做梦，\n',
            '我们一定会证明给你看的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '#1190021654V真、真的……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021655V#006F真的真的。\n',
            '就交给姐姐我们吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021656V所以呢，\n',
            '你可不能总是哭哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1190021657V啊～嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1190021658V姐姐，你真是个好人！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021659V#027F（呵呵，还是老样子，\n',
            '　到哪里都这么受小孩子欢迎。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021660V#019F（嗯……\n',
            '　这大概也是她的优点所在吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0101, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010021661V#501F嗯？怎么了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021662V#010F没有，没什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020021663V好了，我们下一步\n',
            '要做的事情应该很清楚了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021664V#006F嗯！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021665V赶快从后村口出发，\n',
            '到北面的山道调查一下吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Jump('loc_251B')

    def _loc_24DF(): pass

    label('loc_24DF')

    ChrTalk(
        0x00FE,
        (
            '呼哧，没有人愿意相信我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那明明不是在做梦呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_251B(): pass

    label('loc_251B')

    Jump('loc_2543')

    def _loc_251E(): pass

    label('loc_251E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_2543',
    )

    ChrTalk(
        0x00FE,
        (
            '我说了我真的看到过的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2543(): pass

    label('loc_2543')

    TalkEnd(0x000A)

    Return()

# id: 0x000D offset: 0x2547
@scena.Code('func_0D_2547')
def func_0D_2547():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_25D2',
    )

    ChrTalk(
        0x00FE,
        (
            '如果贝斯卡与库赖爷爷\n',
            '能够在这次的集会上\n',
            '达成和解就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果那两人合作的话，\n',
            '我想这个村子的果树园\n',
            '会越来越兴旺的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A38')

    def _loc_25D2(): pass

    label('loc_25D2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_266E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_262F',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '这两天，\n',
            '村长准备召开集会\n',
            '讨论栽培的方针。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果有进展就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_266B')

    def _loc_262F(): pass

    label('loc_262F')

    ChrTalk(
        0x00FE,
        (
            '波波那家伙现在怎么样了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他在柏斯过得好不好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_266B(): pass

    label('loc_266B')

    Jump('loc_2A38')

    def _loc_266E(): pass

    label('loc_266E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 5, 0x31D)),
            Expr.Return,
        ),
        'loc_2796',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2712',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '我也明白\n',
            '库赖爷爷说的话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，我觉得\n',
            '贝斯卡所说的话更加有道理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这件事对村里来说也很重要，\n',
            '应该找一个机会让大家好好谈谈才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2793')

    def _loc_2712(): pass

    label('loc_2712')

    ChrTalk(
        0x00FE,
        (
            '如果不解决这个问题，\n',
            '肯定是后患无穷，我也没有办法去柏斯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我还是试着\n',
            '向村长提议一下，\n',
            '就果树栽培的方针进行一次谈话吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2793(): pass

    label('loc_2793')

    Jump('loc_2A38')

    def _loc_2796(): pass

    label('loc_2796')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 4, 0x31C)),
            Expr.Return,
        ),
        'loc_28BE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_286D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '今天库赖爷爷\n',
            '又和贝斯卡吵架了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '库赖爷爷在\n',
            '开展果树栽培之前\n',
            '就在村里种植水果了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '矿山封闭之后，\n',
            '能够在村里重建果树园\n',
            '都是爷爷的功劳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就凭这个，\n',
            '爷爷他也有不肯让步的地方吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28BB')

    def _loc_286D(): pass

    label('loc_286D')

    ChrTalk(
        0x00FE,
        (
            '今天库赖爷爷\n',
            '又和贝斯卡吵架了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '库赖爷爷也有\n',
            '许多不肯让步的地方吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_28BB(): pass

    label('loc_28BB')

    Jump('loc_2A38')

    def _loc_28BE(): pass

    label('loc_28BE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_29F0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_298B',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '其实，我准备放弃果园的，\n',
            '打算在柏斯开家小店做生意了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，\n',
            '这个村里还有着各种各样的问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不把那些解决的话，\n',
            '我没办法放心离去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以我安排\n',
            '妻子和儿子先去柏斯了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29ED')

    def _loc_298B(): pass

    label('loc_298B')

    ChrTalk(
        0x00FE,
        (
            '其实，我准备放弃果园的，\n',
            '打算在柏斯开家小店做生意了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我安排妻子和儿子\n',
            '先去柏斯等着我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_29ED(): pass

    label('loc_29ED')

    Jump('loc_2A38')

    def _loc_29F0(): pass

    label('loc_29F0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_2A38',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，库赖爷爷也真是的，\n',
            '不管我怎么费尽口舌，他也听不进去……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A38(): pass

    label('loc_2A38')

    TalkEnd(0x000B)

    Return()

# id: 0x000E offset: 0x2A3C
@scena.Code('func_0E_2A3C')
def func_0E_2A3C():
    TalkBegin(0x000C)

    If(
        (
            (Expr.Eval, "OP_29(0x000E, 0x00, 0x04)"),
            Expr.Return,
        ),
        'loc_2E5A',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x000E, 0x01, 0x2000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2DD5',
    )

    OP_28(0x000E, 0x01, 0x2000)

    If(
        (
            (Expr.Eval, "OP_29(0x000E, 0x01, 0x4000)"),
            Expr.Return,
        ),
        'loc_2C13',
    )

    OP_28(0x000E, 0x01, 0x4000)

    ChrTalk(
        0x000C,
        (
            '#1410151439V非常抱歉，\n',
            '前方地带现在禁止进入。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1410151440V详细的情况\n',
            '请去询问村长吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010151441V#000F嗯，关于委托的事情，\n',
            '村长都告诉我们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x0101, 400)

    ChrTalk(
        0x000C,
        (
            '#1410151442V哎，委托……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1410151430V难道说，\n',
            '你们是游击士协会的人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030151431V#020F嗯，没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x0103, 400)

    ChrTalk(
        0x000C,
        (
            '#1410151445V那就太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1410151446V请赶快帮我们\n',
            '消灭那些魔兽吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1410151433V很快就要进入\n',
            '种植树苗的季节了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x0000, 400)

    ChrTalk(
        0x000C,
        (
            '#1410151448V……那么，请小心。\n',
            '拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2DD2')

    def _loc_2C13(): pass

    label('loc_2C13')

    OP_28(0x000E, 0x01, 0x4000)

    ChrTalk(
        0x000C,
        (
            '#1410151426V非常抱歉，\n',
            '前方地带现在禁止进入。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1410151427V不是我吓你们，\n',
            '这里面的山道上\n',
            '出现了非常凶暴的魔兽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010151428V#000F啊，我们正是\n',
            '接受了村长的委托而来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x0101, 400)

    ChrTalk(
        0x000C,
        (
            '#1410151429V啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1410151430V难道说，\n',
            '你们是游击士协会的人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030151431V#020F嗯，没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x0103, 400)

    ChrTalk(
        0x000C,
        (
            '#1410151432V那就太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1410151433V很快就要进入\n',
            '种植树苗的季节了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1410151434V在开始忙碌之前，\n',
            '请一定要帮我们消灭魔兽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x0000, 400)

    ChrTalk(
        0x000C,
        (
            '#1410151435V那么，\n',
            '请你们多加小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2DD2(): pass

    label('loc_2DD2')

    Jump('loc_2E57')

    def _loc_2DD5(): pass

    label('loc_2DD5')

    ChrTalk(
        0x00FE,
        (
            '#1410151436V很快就要\n',
            '进入种植树苗的季节了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1410151437V在开始忙碌之前，\n',
            '拜托你们消灭掉魔兽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1410151435V那么，\n',
            '请你们多加小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_2E57(): pass

    label('loc_2E57')

    Jump('loc_304D')

    def _loc_2E5A(): pass

    label('loc_2E5A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2FBF',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    OP_28(0x000E, 0x01, 0x4000)

    ChrTalk(
        0x000C,
        (
            '#1410151426V非常抱歉，\n',
            '前方地带现在禁止进入。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1410151427V不是我吓你们，\n',
            '这里面的山道上\n',
            '出现了非常凶暴的魔兽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x000E, 0x00, 0x02)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2F53',
    )

    ChrTalk(
        0x0101,
        (
            '#0010151451V#004F咦……？！\n',
            '有这样的传言吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x0101, 400)

    ChrTalk(
        0x000C,
        (
            '#1410151452V只是传言的话就好了，\n',
            '不过看起来应该是真的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2F53(): pass

    label('loc_2F53')

    ChrTurnDirection(0x000C, 0x0000, 400)

    ChrTalk(
        0x000C,
        (
            '#1410151453V详细的情况，\n',
            '请去询问村长吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1410151454V以防万一，\n',
            '我们委托了游击士协会来消灭魔兽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_304D')

    def _loc_2FBF(): pass

    label('loc_2FBF')

    ChrTalk(
        0x000C,
        (
            '#1410151455V前方地带现在禁止进入。\n',
            '详细的情况就请去问村长吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x000C, 180, 400)

    ChrTalk(
        0x000C,
        (
            '#1410151456V看，\n',
            '往那边不是能看到屋顶吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1410151457V那就是村长的家了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_304D(): pass

    label('loc_304D')

    TalkEnd(0x000C)

    Return()

# id: 0x000F offset: 0x3051
@scena.Code('func_0F_3051')
def func_0F_3051():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_3157',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_30F4',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '我想试着在村里的\n',
            '集会上提出我的想法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然到最后，\n',
            '我总是和库赖爷爷发生争吵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我觉得还是应该冷静下来，\n',
            '大家一起好好商量。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3154')

    def _loc_30F4(): pass

    label('loc_30F4')

    ChrTalk(
        0x00FE,
        (
            '虽然到最后，\n',
            '我总是和库赖爷爷发生争吵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我觉得还是应该冷静下来，\n',
            '大家一起好好商量。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3154(): pass

    label('loc_3154')

    Jump('loc_368B')

    def _loc_3157(): pass

    label('loc_3157')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_3296',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3268',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '总是使用\n',
            '古老的方法也不行吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '多考虑一下总体的效率，\n',
            '能够定期送货上市的独特想法\n',
            '也是很必要的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里已经结果的树\n',
            '都比大家的身高要高不少吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这也是我在集会上\n',
            '打算要提出的内容。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要减少高空的作业，\n',
            '也就不需要这么多人手了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3293')

    def _loc_3268(): pass

    label('loc_3268')

    ChrTalk(
        0x00FE,
        (
            '唉……\n',
            '为什么我的提议他不愿意接受呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3293(): pass

    label('loc_3293')

    Jump('loc_368B')

    def _loc_3296(): pass

    label('loc_3296')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 5, 0x31D)),
            Expr.Return,
        ),
        'loc_3401',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_33A8',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '我的意思可不是说\n',
            '无论如何也要实行机械化啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本来果树栽培的作业\n',
            '要实行机械化就非常困难。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算拥有导力机械，\n',
            '要依赖手工作业的部分仍然很多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，\n',
            '这个村里并没有十分充足的人手啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我觉得该交给机械做的事情，\n',
            '还是应该让机械来完成。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_33FE')

    def _loc_33A8(): pass

    label('loc_33A8')

    ChrTalk(
        0x00FE,
        (
            '我好几次都想和库赖爷爷\n',
            '好好谈一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你别误会哦，\n',
            '他只是有点钻牛角尖而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_33FE(): pass

    label('loc_33FE')

    Jump('loc_368B')

    def _loc_3401(): pass

    label('loc_3401')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 4, 0x31C)),
            Expr.Return,
        ),
        'loc_3508',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_34AB',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '库赖爷爷认为\n',
            '我是为了能够轻松地工作\n',
            '才依赖于机械作业的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那可是个很大的误会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我认为应该吸收各种果树栽培的技术，\n',
            '然后慢慢提高进步。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3505')

    def _loc_34AB(): pass

    label('loc_34AB')

    ChrTalk(
        0x00FE,
        (
            '库赖爷爷认为\n',
            '我是为了能够轻松地工作\n',
            '才依赖于机械作业的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那可是个很大的误会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3505(): pass

    label('loc_3505')

    Jump('loc_368B')

    def _loc_3508(): pass

    label('loc_3508')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_363D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_35C8',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '我想成为果树农学家。\n',
            '在数年前我来到了这个村庄。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '很早以前我就做了很多研究，\n',
            '买齐了最新式的导力农机器具。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了不输给其他人，\n',
            '我要种出更多的水果拿到外面出售。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_363A')

    def _loc_35C8(): pass

    label('loc_35C8')

    ChrTalk(
        0x00FE,
        (
            '我想成为果树农学家。\n',
            '在数年前我来到了这个村庄。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '很早以前我就做了很多研究，\n',
            '买齐了最新式的导力农机器具。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_363A(): pass

    label('loc_363A')

    Jump('loc_368B')

    def _loc_363D(): pass

    label('loc_363D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_368B',
    )

    ChrTalk(
        0x00FE,
        (
            '你好，来果树园参观吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '反正也不会少些什么，\n',
            '慢慢四处看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_368B(): pass

    label('loc_368B')

    TalkEnd(0x000D)

    Return()

# id: 0x0010 offset: 0x368F
@scena.Code('func_10_368F')
def func_10_368F():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_36EE',
    )

    ChrTalk(
        0x00FE,
        (
            '我丈夫去参加集会了，\n',
            '很晚才能回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果能和库赖爷爷\n',
            '好好谈谈就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_397A')

    def _loc_36EE(): pass

    label('loc_36EE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_3744',
    )

    ChrTalk(
        0x00FE,
        (
            '我是永远站在\n',
            '我丈夫这一边的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '夫妻之间要相互信赖\n',
            '才能够天长地久。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_397A')

    def _loc_3744(): pass

    label('loc_3744')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_379B',
    )

    ChrTalk(
        0x00FE,
        (
            '我很希望库赖爷爷\n',
            '也能够理解我丈夫的想法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一定会为村子带来好处的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_397A')

    def _loc_379B(): pass

    label('loc_379B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 5, 0x31D)),
            Expr.Return,
        ),
        'loc_384B',
    )

    ChrTalk(
        0x00FE,
        (
            '我也非常喜欢\n',
            '种植水果的生活，\n',
            '我觉得能跟着我丈夫来这里真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '花了不少时间，\n',
            '终于能和村里的人融洽相处了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过还是有例外的，\n',
            '那就是库赖爷爷了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_397A')

    def _loc_384B(): pass

    label('loc_384B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 4, 0x31C)),
            Expr.Return,
        ),
        'loc_38C6',
    )

    ChrTalk(
        0x00FE,
        (
            '丈夫说得对，\n',
            '库赖爷爷一定是\n',
            '误解我们的意思了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我想双方静下心来好好交谈的话，\n',
            '就一定能够达成一致的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_397A')

    def _loc_38C6(): pass

    label('loc_38C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_3936',
    )

    ChrTalk(
        0x00FE,
        (
            '我丈夫贝斯卡\n',
            '非常热衷于研究呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '白天就像这样在果园里工作，\n',
            '晚上就在研究各种各样的栽培方法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_397A')

    def _loc_3936(): pass

    label('loc_3936')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_397A',
    )

    ChrTalk(
        0x00FE,
        (
            '马上就要到午休的时间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要赶快把\n',
            '工作都给解决掉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_397A(): pass

    label('loc_397A')

    TalkEnd(0x000E)

    Return()

# id: 0x0011 offset: 0x397E
@scena.Code('func_11_397E')
def func_11_397E():
    TalkBegin(0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_39CD',
    )

    ChrTalk(
        0x00FE,
        (
            '在下次集会的时候，\n',
            '我要让村里的年轻人\n',
            '再注意一下做法才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3CA3')

    def _loc_39CD(): pass

    label('loc_39CD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_3A36',
    )

    ChrTalk(
        0x00FE,
        (
            '要尽量让果树\n',
            '保持自然生长，\n',
            '这才是最重要的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就是要肯花时间，\n',
            '才能种出美味的水果。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3CA3')

    def _loc_3A36(): pass

    label('loc_3A36')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 5, 0x31D)),
            Expr.Return,
        ),
        'loc_3B65',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3AEE',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '贝斯卡的做法\n',
            '太过依赖导力器这类的东西了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那家伙种出来的水果\n',
            '在口味方面肯定\n',
            '要比我的逊色许多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他那种东西\n',
            '是不可以作为\n',
            '拉文努村的水果对外销售的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3B62')

    def _loc_3AEE(): pass

    label('loc_3AEE')

    ChrTalk(
        0x00FE,
        (
            '那家伙种出来的水果\n',
            '在口味方面肯定\n',
            '要比我的逊色许多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他那种东西\n',
            '是不可以作为\n',
            '拉文努村的水果对外销售的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3B62(): pass

    label('loc_3B62')

    Jump('loc_3CA3')

    def _loc_3B65(): pass

    label('loc_3B65')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 4, 0x31C)),
            Expr.Return,
        ),
        'loc_3BE4',
    )

    ChrTalk(
        0x00FE,
        (
            '年轻人栽培果树\n',
            '真是大手大脚的啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不考虑产品的质量和口味， \n',
            '一味追求数量来进行作业。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是可悲啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3CA3')

    def _loc_3BE4(): pass

    label('loc_3BE4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_3C65',
    )

    ChrTalk(
        0x00FE,
        (
            '在这个村还是\n',
            '以矿山而繁荣的时候，\n',
            '我就开始在这里种植水果了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在完美培育水果方面，\n',
            '我可不会输给村里的任何人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3CA3')

    def _loc_3C65(): pass

    label('loc_3C65')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_3CA3',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，今年的气候也很好，\n',
            '所有的果实看上去都熟透了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3CA3(): pass

    label('loc_3CA3')

    TalkEnd(0x000F)

    Return()

# id: 0x0012 offset: 0x3CA7
@scena.Code('func_12_3CA7')
def func_12_3CA7():
    TalkBegin(0x0011)
    EventBegin(0x00)
    Fade(1000)
    CameraMove(31970, 8000, 37320, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2920, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 32990, 8000, 38280, 180)
    SetChrPos(0x0102, 33860, 8000, 39820, 180)
    SetChrPos(0x0103, 31890, 8000, 39180, 180)
    SetChrDirection(0x0011, 0, 400)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010021716V#000F村长，您在这里啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180021717V#1P哦，是刚才几位游击士啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021718V#020F……好宏伟的坟墓啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180021719V#1P这是为了悼念十年前\n',
            '战争中的牺牲者而建造的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180021720V#1P柏斯地区因为离帝国很近，\n',
            '所以也成了战争中最惨烈的地方……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180021721V#1P这村子也被战火无情地席卷了，\n',
            '不知多少人为此献出了自己的生命。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021722V#003F是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021723V#013F………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180021724V#1P哈哈，不好意思，\n',
            '让你们几位也触景生情了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180021725V#1P来这里打扫，\n',
            '已经是我每天的必做之事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180021726V#1P话说回来，发生什么事了？\n',
            '有什么我能帮忙的地方吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021727V#501F啊，是的。\n',
            '有件事想和您商量一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021728V啊，在这之前……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021729V#020F来到这里也算是缘分，\n',
            '能不能让我们先拜祭一下呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021730V#015F虽然没有鲜花……\n',
            '至少让我们向为了保卫祖国\n',
            '而献身的人们祈祷一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180021731V#1P哦，这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180021732V#1P当然没关系了。\n',
            '你们能这样做，他们也会高兴吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    FadeOut(2000, 0, -1)
    NewScene('ED6_DT01/T1210._SN', 100, 0, 0)
    IdleLoop()
    TalkEnd(0x0011)

    Return()

# id: 0x0013 offset: 0x40B3
@scena.Code('func_13_40B3')
def func_13_40B3():
    SetScenaFlags(ScenaFlag(0x006D, 0, 0x368))
    OP_28(0x0036, 0x01, 0x0002)
    EventBegin(0x00)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    SetChrPos(0x0101, 560, 0, 13490, 225)
    SetChrPos(0x0102, 510, 0, 11530, 0)
    SetChrPos(0x0103, -820, 0, 12480, 90)
    CameraMove(110, 0, 13180, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x0103,
        (
            '#0030021548V#020F接下来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021549V先试着调查一下\n',
            '这次事件的目击情报吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021550V#501F那样的话，\n',
            '先向村里的人都打听一下吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021551V#010F突然问村民的话会让人怀疑的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020021552V总之，还是先听听\n',
            '这里的村长是怎么说的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021553V#006F嗯，知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x0014 offset: 0x4225
@scena.Code('func_14_4225')
def func_14_4225():
    EventBegin(0x00)
    CameraSetDistance(3800, 0)
    OP_6C(90000, 0)
    CameraMove(23730, 0, 31170, 0)
    SetChrPos(0x0101, 560, 0, 13490, 0)
    SetChrPos(0x0102, 510, 0, 11530, 0)
    SetChrPos(0x0103, -820, 0, 12480, 0)
    OP_12(0x00009470, 0x00030D40, 0x00000000)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_4299')
    def lambda_4299():
        OP_6C(45000, 8000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_4299)

    CameraMove(820, 0, 19100, 8000)
    Fade(2000)
    CameraMove(110, 0, 13180, 0)
    CameraSetDistance(2800, 0)
    OP_12(0x00009470, 0x000186A0, 0x00001F40)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010021524V#000F这里就是拉文努村……\n',
            '真是个悠闲舒适的地方啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0101, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010021525V#000F啊，那边有个果树园。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0102, 90, 400)
    SetChrDirection(0x0103, 90, 400)

    ChrTalk(
        0x0103,
        (
            '#0030021526V#020F现在这里是以种植水果闻名，\n',
            '不过以前可是靠采矿业而兴旺的哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021527V据说村子北面有一个\n',
            '已经被废弃的七耀石矿山呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_43E4')
    def lambda_43E4():
        ChrTurnDirection(0x00FE, 0x0103, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_43E4)

    ChrTurnDirection(0x0102, 0x0103, 400)

    ChrTalk(
        0x0102,
        (
            '#0020021528V#010F了解得非常详细啊，\n',
            '雪拉姐姐以前来过这里吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021529V#020F嗯，为了成为正游击士，\n',
            '我在巡回修行的时候来过这村子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021530V那时候，我可是没有乘飞艇，\n',
            '而是徒步走遍了全国的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021531V#004F啊，为什么呢？\n',
            '坐飞艇多方便啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021532V#026F『飞艇的确很方便，\n',
            '　可以在五大城市间任意往来。』',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021533V『而这种方便一旦变成了习惯，\n',
            '　就会减少许多在各地修行时的阅历。』',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021534V『要守护一片土地，\n',
            '　首先就要自己脚踏实地去看一看……』',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021535V#020F——这些话\n',
            '是卡西乌斯老师的教导呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021536V#501F哎，是老爸他……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021537V#010F确实如此，如果发生了事件，\n',
            '而之前从没去过事发地点的话，\n',
            '很有可能会延误到达的时间。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020021538V而且在追击犯人的时候，\n',
            '熟悉地理环境才能处于有利的局面……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4707',
    )

    ChrTalk(
        0x0103,
        (
            '#0030021539V#021F呵呵，正是如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021540V你们如果有机会的话，\n',
            '最好也尝试一下哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4839')

    def _loc_4707(): pass

    label('loc_4707')

    SetScenaFlags(ScenaFlag(0x006D, 0, 0x368))
    OP_28(0x0036, 0x01, 0x0002)

    ChrTalk(
        0x0103,
        (
            '#0030021541V#021F呵呵，正是如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021542V#020F接下来，不管怎么说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021543V先试着调查一下\n',
            '这次事件的目击情报吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021544V#000F那样的话，\n',
            '先向村里的人都打听一下吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021545V#010F突然问村民的话会让人怀疑的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020021546V总之，还是先听听\n',
            '这里的村长是怎么说的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021547V#006F嗯，知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4839(): pass

    label('loc_4839')

    EventEnd(0x00)

    Return()

# id: 0x0015 offset: 0x483C
@scena.Code('func_15_483C')
def func_15_483C():
    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上着锁，无法打开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0016 offset: 0x488C
@scena.Code('func_16_488C')
def func_16_488C():
    If(
        (
            (Expr.Eval, "OP_29(0x000E, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x000E, 0x00, 0x40)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_489E',
    )

    Return()

    def _loc_489E(): pass

    label('loc_489E')

    If(
        (
            (Expr.Eval, "OP_29(0x000E, 0x00, 0x04)"),
            Expr.Return,
        ),
        'loc_4C3E',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x000E, 0x01, 0x2000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4C3B',
    )

    OP_28(0x000E, 0x01, 0x2000)
    TalkBegin(0x000C)
    EventBegin(0x02)

    If(
        (
            (Expr.Eval, "OP_29(0x000E, 0x01, 0x4000)"),
            Expr.Return,
        ),
        'loc_4A77',
    )

    OP_28(0x000E, 0x01, 0x4000)

    ChrTalk(
        0x000C,
        (
            '#1410151439V非常抱歉，\n',
            '前方地带现在禁止进入。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1410151482V我不是说过了吗？\n',
            '这里可能有凶暴的魔兽出没。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010151483V#000F嗯，\n',
            '村长先生已经委托我们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x0101, 400)

    ChrTalk(
        0x000C,
        (
            '#1410151429V啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1410151430V难道说，\n',
            '你们是游击士协会的人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030151431V#020F嗯，没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x0103, 400)

    ChrTalk(
        0x000C,
        (
            '#1410151445V那就太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1410151446V请赶快帮我们\n',
            '消灭那些魔兽吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1410151433V很快就要进入\n',
            '种植树苗的季节了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x0000, 400)

    ChrTalk(
        0x000C,
        (
            '#1410151448V……那么，请小心。\n',
            '拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4C36')

    def _loc_4A77(): pass

    label('loc_4A77')

    OP_28(0x000E, 0x01, 0x4000)

    ChrTalk(
        0x000C,
        (
            '#1410151426V非常抱歉，\n',
            '前方地带现在禁止进入。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1410151427V不是我吓你们，\n',
            '这里面的山道上\n',
            '出现了非常凶暴的魔兽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010151493V#000F啊，我们正是\n',
            '接受了村长的委托而来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x0101, 400)

    ChrTalk(
        0x000C,
        (
            '#1410151429V啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1410151430V难道说，\n',
            '你们是游击士协会的人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030151431V#020F嗯，没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x0103, 400)

    ChrTalk(
        0x000C,
        (
            '#1410151432V那就太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1410151433V很快就要进入\n',
            '种植树苗的季节了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1410151434V在开始忙碌之前，\n',
            '请一定要帮我们消灭魔兽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x0000, 400)

    ChrTalk(
        0x000C,
        (
            '#1410151435V那么，\n',
            '请你们多加小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4C36(): pass

    label('loc_4C36')

    EventEnd(0x03)
    TalkEnd(0x000C)

    def _loc_4C3B(): pass

    label('loc_4C3B')

    Jump('loc_4E54')

    def _loc_4C3E(): pass

    label('loc_4C3E')

    TalkBegin(0x000C)
    EventBegin(0x02)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4DA8',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    OP_28(0x000E, 0x01, 0x4000)

    ChrTalk(
        0x000C,
        (
            '#1410151426V非常抱歉，\n',
            '前方地带现在禁止进入。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1410151427V不是我吓你们，\n',
            '这里面的山道上\n',
            '出现了非常凶暴的魔兽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x000E, 0x00, 0x02)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4D3C',
    )

    ChrTalk(
        0x0101,
        (
            '#0010151451V#004F咦……？！\n',
            '有这样的传言吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x0101, 400)

    ChrTalk(
        0x000C,
        (
            '#1410151452V只是传言的话就好了，\n',
            '不过看起来应该是真的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4D3C(): pass

    label('loc_4D3C')

    ChrTurnDirection(0x000C, 0x0000, 400)

    ChrTalk(
        0x000C,
        (
            '#1410151453V详细的情况，\n',
            '请去询问村长吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1410151454V以防万一，\n',
            '我们委托了游击士协会来消灭魔兽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4E36')

    def _loc_4DA8(): pass

    label('loc_4DA8')

    ChrTalk(
        0x000C,
        (
            '#1410151455V前方地带现在禁止进入。\n',
            '详细的情况就请去问村长吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x000C, 180, 400)

    ChrTalk(
        0x000C,
        (
            '#1410151456V看，\n',
            '往那边不是能看到屋顶吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1410151457V那就是村长的家了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_4E36(): pass

    label('loc_4E36')

    ChrMoveToRelative(0x0000, 0, 0, -2000, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    TalkEnd(0x000C)
    def _loc_4E54(): pass

    label('loc_4E54')

    Return()

# id: 0x0017 offset: 0x4E55
@scena.Code('func_17_4E55')
def func_17_4E55():
    FadeIn(1000, 0)
    SetMapFlags(0x00400000)
    EventBegin(0x00)
    OP_6C(45000, 0)
    CameraMove(9600, 8000, 68460, 0)

    @scena.Lambda('lambda_4E85')
    def lambda_4E85():
        CameraMove(7080, 8000, 66150, 3000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_4E85)

    SetChrPos(0x000C, 5430, 8000, 66280, 180)
    SetChrPos(0x0101, 7080, 8000, 68150, 180)
    SetChrPos(0x0102, 7580, 8000, 69650, 180)
    SetChrPos(0x0103, 6530, 8000, 69110, 180)

    @scena.Lambda('lambda_4EE1')
    def lambda_4EE1():
        ChrMoveToRelative(0x0101, 0, 0, -2000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4EE1)

    Sleep(400)

    @scena.Lambda('lambda_4F01')
    def lambda_4F01():
        ChrMoveToRelative(0x0102, 0, 0, -2200, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_4F01)

    Sleep(400)

    @scena.Lambda('lambda_4F21')
    def lambda_4F21():
        ChrMoveToRelative(0x0103, 0, 0, -1800, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_4F21)

    OP_0D()
    WaitForThreadExit(0x0101, 0x0001)
    ChrTurnDirection(0x0101, 0x000C, 400)
    WaitForThreadExit(0x000C, 0x0001)
    OP_62(0x000C, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x000C, 0x0101, 400)
    OP_4A(0x000C, 255)

    ChrTalk(
        0x000C,
        (
            '#1410151468V啊……是你们！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0103, 0x0001)
    ChrTurnDirection(0x0103, 0x000C, 400)
    WaitForThreadExit(0x0102, 0x0001)
    ChrTurnDirection(0x0102, 0x000C, 400)

    ChrTalk(
        0x000C,
        (
            '#1410151469V刚、刚才那场地震……\n',
            '难道是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1410151470V魔兽果真出现了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010151471V#502F嘿嘿⊙\n',
            '已经被我们干掉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x000C,
        (
            '#1410151472V真、真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030151473V#020F嗯，已经把它消灭了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030151474V虽然是个很难缠的家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x0103, 400)

    ChrTalk(
        0x000C,
        (
            '#1410151475V呼，太好了。\n',
            '真是个振奋人心的好消息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1410151476V这样一来，\n',
            '就不用担心魔兽\n',
            '会在农忙期间来袭击了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1410151477V我现在就去把\n',
            '这个好消息告诉村长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x0101, 400)

    ChrTalk(
        0x000C,
        (
            '#1410151478V你们真是帮了大忙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1410151479V虽然没什么可招待各位的，\n',
            '还是请你们在这里好好休息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010151480V#001F嗯，谢谢⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x000C, 3720, 8000, 64470, 3000, 0x00)
    ChrWalkTo(0x000C, -2009, 6000, 63710, 3000, 0x00)

    @scena.Lambda('lambda_51E0')
    def lambda_51E0():
        OP_92(0x0102, 0x0101, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_51E0)

    OP_92(0x0103, 0x0101, 0, 3000, 0x00)
    SetChrFlags(0x000C, 0x0080)
    ClearMapFlags(0x00400000)
    EventEnd(0x00)

    Return()

# id: 0x0018 offset: 0x520A
@scena.Code('func_18_520A')
def func_18_520A():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '七耀历１１９２年\n',
            '在战火中丧生的\n',
            '六个善良的灵魂，在此长眠。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '雷夫、阿贝尔、尼高尔\n',
            '维姆、依蕾娜、米夏。\n',
            '在女神的座前，安息吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0019 offset: 0x52CA
@scena.Code('func_19_52CA')
def func_19_52CA():
    OP_13(0x002E)

    Return()

# id: 0x001A offset: 0x52CE
@scena.Code('func_1A_52CE')
def func_1A_52CE():
    OP_13(0x002D)

    Return()

# id: 0x001B offset: 0x52D2
@scena.Code('func_1B_52D2')
def func_1B_52D2():
    OP_13(0x002F)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

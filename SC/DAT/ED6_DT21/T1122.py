import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T1122_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1122   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '巴克'),
    TXT(0x02, '德拉多'),
    TXT(0x03, '普蕾沙'),
    TXT(0x04, '波波'),
    TXT(0x05, '思潘斯老人'),
    TXT(0x06, '卡特丽亚'),
    TXT(0x07, '芬尼尔'),
    TXT(0x08, '泊尔'),
    TXT(0x09, '米蕾婆婆'),
    TXT(0x0A, '里布罗'),
    TXT(0x0B, '艾米'),
    TXT(0x0C, '格蕾娅'),
    TXT(0x0D, '丽露露'),
    TXT(0x0E, '卡洛'),
    TXT(0x0F, '玛依森老人'),
    TXT(0x10, '刚茨'),
    TXT(0x11, '罗卡斯'),
    TXT(0x12, '科尔娜'),
    TXT(0x13, '西蒙'),
    TXT(0x14, '哈尔德'),
    TXT(0x15, '艾尔珂'),
    TXT(0x16, '马尔科'),
    TXT(0x17, '蒙提'),
    TXT(0x18, '罗亚'),
    TXT(0x19, '梅贝尔市长'),
    TXT(0x1A, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1122.x'
    header.mapIndex       = 1
    header.bgm            = 11
    header.flags          = 0x0000
    header.entryFunction  = 0x0025
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x67FB
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
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH01060._CH', 'ED6_DT07/CH01060P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT07/CH02490._CH', 'ED6_DT07/CH02490P._CP'),
        ('ED6_DT07/CH01220._CH', 'ED6_DT07/CH01220P._CP'),
        ('ED6_DT07/CH01010._CH', 'ED6_DT07/CH01010P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01070._CH', 'ED6_DT07/CH01070P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
        ('ED6_DT07/CH01270._CH', 'ED6_DT07/CH01270P._CP'),
        ('ED6_DT07/CH01180._CH', 'ED6_DT07/CH01180P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01480._CH', 'ED6_DT07/CH01480P._CP'),
        ('ED6_DT07/CH01100._CH', 'ED6_DT07/CH01100P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH02360._CH', 'ED6_DT07/CH02360P._CP'),
    ]

# id: 0x10002 offset: 0x14A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 1500,
            z                   = 0,
            y                   = -12700,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = 8500,
            z                   = 0,
            y                   = -8300,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = 4100,
            z                   = 0,
            y                   = 13650,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = 8250,
            z                   = 0,
            y                   = 13600,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            x                   = 9300,
            z                   = 0,
            y                   = 6900,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            x                   = -13400,
            z                   = 0,
            y                   = 2500,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 2830,
            z                   = 0,
            y                   = 9160,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            x                   = -16700,
            z                   = 0,
            y                   = -8600,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            x                   = -13600,
            z                   = 0,
            y                   = 10700,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            x                   = -11100,
            z                   = 0,
            y                   = 10300,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            x                   = 5250,
            z                   = 0,
            y                   = -4500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0016,
        ),
        ScenaNpcData(
            x                   = -3600,
            z                   = 0,
            y                   = 12500,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001A,
        ),
        ScenaNpcData(
            x                   = -2310,
            z                   = -1000,
            y                   = -10530,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0017,
        ),
        ScenaNpcData(
            x                   = 2350,
            z                   = 0,
            y                   = -8000,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0018,
        ),
        ScenaNpcData(
            x                   = 11500,
            z                   = 0,
            y                   = 12000,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0019,
        ),
        ScenaNpcData(
            x                   = -17180,
            z                   = 0,
            y                   = 5980,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001B,
        ),
        ScenaNpcData(
            x                   = -12620,
            z                   = 0,
            y                   = -8490,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001D,
        ),
        ScenaNpcData(
            x                   = -7300,
            z                   = -1000,
            y                   = 2510,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001E,
        ),
        ScenaNpcData(
            x                   = -12380,
            z                   = 0,
            y                   = 7420,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001F,
        ),
        ScenaNpcData(
            x                   = -16980,
            z                   = 0,
            y                   = -7310,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = -1200,
            z                   = -1000,
            y                   = 6040,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0021,
        ),
        ScenaNpcData(
            x                   = -1200,
            z                   = -1000,
            y                   = 5040,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0022,
        ),
        ScenaNpcData(
            x                   = 9730,
            z                   = -1000,
            y                   = 13220,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 1600,
            z                   = -1000,
            y                   = 150,
            direction           = 257,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0024,
        ),
    )

# id: 0x10003 offset: 0x46A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x46A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x46A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 6830,
            triggerZ            = 0,
            triggerY            = -8820,
            triggerRange        = 400,
            actorX              = 8360,
            actorZ              = 1500,
            actorY              = -8430,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 7540,
            triggerZ            = 0,
            triggerY            = 6450,
            triggerRange        = 400,
            actorX              = 9300,
            actorZ              = 1500,
            actorY              = 6900,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000E,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -15120,
            triggerZ            = 0,
            triggerY            = -8860,
            triggerRange        = 400,
            actorX              = -16700,
            actorZ              = 1500,
            actorY              = -8600,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0012,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x4D6
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_58B',
    )

    SetChrFlags(0x0019, 0x0080)
    SetChrFlags(0x001A, 0x0080)
    CreateThread(0x0012, 0x00, 0x06, 0x0002)
    SetChrPos(0x0012, 6320, 0, -5410, 90)
    CreateThread(0x0015, 0x00, 0x06, 0x0002)
    SetChrPos(0x0015, 6690, 0, -6830, 90)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_557',
    )

    CreateThread(0x0014, 0x00, 0x06, 0x0002)
    SetChrPos(0x0014, -7650, -1000, 270, 90)
    CreateThread(0x0016, 0x00, 0x00, 0x0008)
    SetChrPos(0x0016, 8210, 0, 11230, 90)
    SetChrFlags(0x0013, 0x0080)

    Jump('loc_588')

    def _loc_557(): pass

    label('loc_557')

    SetChrFlags(0x0008, 0x0010)
    SetChrPos(0x0014, -8720, -1000, -3130, 0)
    SetChrPos(0x0018, -10900, 0, -7320, 232)
    ClearChrFlags(0x0020, 0x0080)
    ClearChrFlags(0x001F, 0x0080)

    def _loc_588(): pass

    label('loc_588')

    Jump('loc_5E8')

    def _loc_58B(): pass

    label('loc_58B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_5E8',
    )

    ClearChrFlags(0x001B, 0x0080)
    ClearChrFlags(0x001C, 0x0080)
    ClearChrFlags(0x001D, 0x0080)
    ClearChrFlags(0x001E, 0x0080)
    ClearChrFlags(0x001F, 0x0080)
    SetChrFlags(0x0019, 0x0080)
    SetChrFlags(0x000B, 0x0010)
    SetChrPos(0x001A, 580, -1000, 5590, 270)
    SetChrPos(0x0018, -8790, 0, -11320, 270)
    SetChrPos(0x0014, -8720, -1000, -3130, 0)

    def _loc_5E8(): pass

    label('loc_5E8')

    Return()

# id: 0x0001 offset: 0x5E9
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_62F',
    )

    OP_72(0x0000, 0x0010)
    OP_6F(0x0000, 29)
    OP_72(0x0001, 0x0010)
    OP_6F(0x0001, 29)
    OP_75(0xFF, 0x0000000A, 0x07)
    OP_75(0xFF, 0x0000000C, 0x07)
    OP_75(0xFF, 0x0000000D, 0x07)
    OP_82(0x80, 0x00)
    OP_82(0x81, 0x00)
    OP_82(0x82, 0x00)
    OP_82(0x83, 0x00)
    OP_82(0x84, 0x00)

    Jump('loc_64B')

    def _loc_62F(): pass

    label('loc_62F')

    OP_25(0x01CB, 0xFFFFEF98, 0xFFFFFC18, 0x00000276, 0x000007D0, 0x000061A8, 0x64, 0x00000000)

    def _loc_64B(): pass

    label('loc_64B')

    Return()

# id: 0x0002 offset: 0x64C
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_698',
    )

    OP_8E(0x00FE, 6040, 0, 13600, 2000, 0x00)
    OP_8C(0x00FE, 0, 400)
    Sleep(3000)

    OP_8E(0x00FE, 8250, 0, 13600, 2000, 0x00)
    OP_8C(0x00FE, 0, 400)
    Sleep(3000)

    Jump('ReInit')

    def _loc_698(): pass

    label('loc_698')

    Return()

# id: 0x0003 offset: 0x699
@scena.Code('func_03_699')
def func_03_699():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_6C6',
    )

    def _loc_6A0(): pass

    label('loc_6A0')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_6C3',
    )

    OP_8D(0x00FE, -9760, 1870, -7910, -2550, 2000)

    Jump('loc_6A0')

    def _loc_6C3(): pass

    label('loc_6C3')

    Jump('loc_6E9')

    def _loc_6C6(): pass

    label('loc_6C6')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_6E9',
    )

    OP_8D(0x00FE, -1410, -8950, -3910, -12650, 2000)

    Jump('loc_6C6')

    def _loc_6E9(): pass

    label('loc_6E9')

    Return()

# id: 0x0004 offset: 0x6EA
@scena.Code('func_04_6EA')
def func_04_6EA():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_70D',
    )

    OP_8D(0x00FE, 5660, -10000, -300, -7600, 2000)

    Jump('func_04_6EA')

    def _loc_70D(): pass

    label('loc_70D')

    Return()

# id: 0x0005 offset: 0x70E
@scena.Code('func_05_70E')
def func_05_70E():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_731',
    )

    OP_8D(0x00FE, 200, 14800, -7900, 10300, 2000)

    Jump('func_05_70E')

    def _loc_731(): pass

    label('loc_731')

    Return()

# id: 0x0006 offset: 0x732
@scena.Code('func_06_732')
def func_06_732():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_755',
    )

    OP_8D(0x00FE, 7480, 600, 4800, -5000, 2000)

    Jump('func_06_732')

    def _loc_755(): pass

    label('loc_755')

    Return()

# id: 0x0007 offset: 0x756
@scena.Code('func_07_756')
def func_07_756():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_779',
    )

    OP_8D(0x00FE, -12100, 16600, -16600, 14400, 2000)

    Jump('func_07_756')

    def _loc_779(): pass

    label('loc_779')

    Return()

# id: 0x0008 offset: 0x77A
@scena.Code('func_08_77A')
def func_08_77A():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_79D',
    )

    OP_8D(0x00FE, 9580, 12630, 5520, 9820, 2000)

    Jump('func_08_77A')

    def _loc_79D(): pass

    label('loc_79D')

    Return()

# id: 0x0009 offset: 0x79E
@scena.Code('func_09_79E')
def func_09_79E():
    TalkBegin(0x0008)
    FadeOut(300, 0, 100)

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
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '买东西\n'),
            TXT(0x02, '离开\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_809',
    )

    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_801',
    )

    OP_A9(0x3E)

    Jump('loc_803')

    def _loc_801(): pass

    label('loc_801')

    OP_A9(0x60)

    def _loc_803(): pass

    label('loc_803')

    OP_56(0x00)
    TalkEnd(0x0008)

    Return()

    def _loc_809(): pass

    label('loc_809')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_81A',
    )

    TalkEnd(0x0008)

    Return()

    def _loc_81A(): pass

    label('loc_81A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_97C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8BE',
    )

    ChrTalk(
        0x0008,
        (
            '啊哟啊哟，稍微等等啦。\n',
            '支援的大酬宾哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '艰苦的时候更要互相帮助！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '为答谢各位平时经常光顾本店，\n',
            '我为大家准备了优惠的商品哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x0008, 0x0010)
    OP_A2(0x0000)

    Jump('loc_979')

    def _loc_8BE(): pass

    label('loc_8BE')

    ChrTalk(
        0x0008,
        (
            '前景虽然很严酷，\n',
            '但在小姐的帮助下，\n',
            '当前库存不足的情况总算得到了避免。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '这种时候更要靠大酬宾来\n',
            '使市场活跃起来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '这就是为了答谢顾客，\n',
            '在困难的时候更要加油呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0008, 0, 400)
    SetChrFlags(0x0008, 0x0010)
    OP_A3(0x0000)

    def _loc_979(): pass

    label('loc_979')

    Jump('loc_C30')

    def _loc_97C(): pass

    label('loc_97C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_A7B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A3B',
    )

    ChrTalk(
        0x0008,
        (
            '岂止是定期船，\n',
            '连货车和船都停开了。\n',
            '物流完全瘫痪了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '这样下去的话，\n',
            '很快就没有库存了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '尤其是像本店这样以货物新鲜为卖点的店铺。\n',
            '这可是生死攸关的问题啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_A78')

    def _loc_A3B(): pass

    label('loc_A3B')

    ChrTalk(
        0x0008,
        (
            '真头痛。\n',
            '物流完全瘫痪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '这可是生死攸关的问题啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A78(): pass

    label('loc_A78')

    Jump('loc_C30')

    def _loc_A7B(): pass

    label('loc_A7B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_B29',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_AC1',
    )

    ChrTalk(
        0x0008,
        (
            '好了，期待已久的\n',
            '恢复营业纪念大减价就要开始啰～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B26')

    def _loc_AC1(): pass

    label('loc_AC1')

    ChrTalk(
        0x0008,
        (
            '好了，期待已久的\n',
            '恢复营业纪念大减价就要开始啰～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '本日内可享受优惠的商品，\n',
            '您可别错过哟～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_B26(): pass

    label('loc_B26')

    Jump('loc_C30')

    def _loc_B29(): pass

    label('loc_B29')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_C30',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_B80',
    )

    ChrTalk(
        0x0008,
        (
            '拉文努村的水果\n',
            '大量到货啰～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '洛连特产的蔬菜也是\n',
            '最新鲜的哟～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C30')

    def _loc_B80(): pass

    label('loc_B80')

    ChrTalk(
        0x0008,
        (
            '来来，都来看一看啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '在拉文努村收获的水果\n',
            '大量到货啰～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '要是您正在为晚餐的菜单犹豫的话，\n',
            '本人向您推荐洛连特的蔬菜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '是刚刚从帕赛尔农场\n',
            '运送来的新鲜货哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_C30(): pass

    label('loc_C30')

    TalkEnd(0x0008)

    Return()

# id: 0x000A offset: 0xC34
@scena.Code('func_0A_C34')
def func_0A_C34():
    Call(0, 0x000B)

    Return()

# id: 0x000B offset: 0xC39
@scena.Code('func_0B_C39')
def func_0B_C39():
    TalkBegin(0x0009)
    FadeOut(300, 0, 100)

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
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '买东西\n'),
            TXT(0x02, '离开\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CA4',
    )

    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C9C',
    )

    OP_A9(0x3D)

    Jump('loc_C9E')

    def _loc_C9C(): pass

    label('loc_C9C')

    OP_A9(0x5F)

    def _loc_C9E(): pass

    label('loc_C9E')

    OP_56(0x00)
    TalkEnd(0x0009)

    Return()

    def _loc_CA4(): pass

    label('loc_CA4')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CB5',
    )

    TalkEnd(0x0009)

    Return()

    def _loc_CB5(): pass

    label('loc_CB5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_DBD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D60',
    )

    ChrTalk(
        0x0009,
        (
            '超市的所有店铺\n',
            '都在举办酬宾活动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '多亏了小姐，\n',
            '货源得到了保证，\n',
            '现在要尽全力使超市活跃起来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '柏斯的超市\n',
            '一直是站在平民百姓这一边的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    Jump('loc_DBA')

    def _loc_D60(): pass

    label('loc_D60')

    ChrTalk(
        0x0009,
        (
            '超市的所有店铺\n',
            '都在举办酬宾活动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '所有商品都是经济实惠的，\n',
            '请务必要来看一下啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DBA(): pass

    label('loc_DBA')

    Jump('loc_11B6')

    def _loc_DBD(): pass

    label('loc_DBD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_F52',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_EB3',
    )

    ChrTalk(
        0x0009,
        (
            '怎，怎么办。\n',
            '货物迟迟不来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '按道理的话，\n',
            '这样的状况是应该考虑涨价的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '以前我们曾经趁机涨过价，\n',
            '给大家添了不少麻烦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我想现在不能再随随便便\n',
            '涨价了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '必须得和巴克那家伙商量下，\n',
            '想出个办法来才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    Jump('loc_F4F')

    def _loc_EB3(): pass

    label('loc_EB3')

    ChrTalk(
        0x0009,
        (
            '物流仍然停止着，\n',
            '按道理的话，\n',
            '这样的状况是应该考虑涨价的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '以前我们曾经趁机涨过价，\n',
            '因为以前曾给大家添过麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '现在不能再随随便便\n',
            '涨价了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F4F(): pass

    label('loc_F4F')

    Jump('loc_11B6')

    def _loc_F52(): pass

    label('loc_F52')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_108D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_FC0',
    )

    ChrTalk(
        0x0009,
        (
            '现在正在举行恢复营业纪念大酬宾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '恢复营业是个不错的时机啊。\n',
            '得充分用来做生意才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_108A')

    def _loc_FC0(): pass

    label('loc_FC0')

    ChrTalk(
        0x0009,
        (
            '呀，欢迎。\n',
            '今日正举办恢复营业纪念大酬宾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '好不容易又重新开业的第一天嘛，\n',
            '不好好利用来做生意可不行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '摔倒了也不要白白站起来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这是米蕾婆婆的口头禅，\n',
            '那正是商人该秉持的精神啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_108A(): pass

    label('loc_108A')

    Jump('loc_11B6')

    def _loc_108D(): pass

    label('loc_108D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_11B6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1104',
    )

    ChrTalk(
        0x0009,
        (
            '有很多优惠的商品，\n',
            '请务必要来看一下啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '隔壁那个店铺是我伙伴开的，\n',
            '也请您顺便多关照一下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11B6')

    def _loc_1104(): pass

    label('loc_1104')

    ChrTalk(
        0x0009,
        (
            '柏斯最近很太平，\n',
            '商品的进货也很安定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '因此优惠商品比比皆是。\n',
            '请务必要来看一下啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '呵呵，隔壁的店铺是我伙伴巴克开的，\n',
            '所以也请多关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '那家伙是我的伙伴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_11B6(): pass

    label('loc_11B6')

    TalkEnd(0x0009)

    Return()

# id: 0x000C offset: 0x11BA
@scena.Code('func_0C_11BA')
def func_0C_11BA():
    TalkBegin(0x000A)
    FadeOut(300, 0, 100)

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
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '买东西\n'),
            TXT(0x02, '离开\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1225',
    )

    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_121D',
    )

    OP_A9(0x40)

    Jump('loc_121F')

    def _loc_121D(): pass

    label('loc_121D')

    OP_A9(0x5C)

    def _loc_121F(): pass

    label('loc_121F')

    OP_56(0x00)
    TalkEnd(0x000A)

    Return()

    def _loc_1225(): pass

    label('loc_1225')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1236',
    )

    TalkEnd(0x000A)

    Return()

    def _loc_1236(): pass

    label('loc_1236')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_134A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_12F3',
    )

    ChrTalk(
        0x000A,
        (
            '全店都在进行大酬宾，\n',
            '现在出售特殊的商品哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '虽然是水果店的老兄\n',
            '想出来的主意，\n',
            '但我觉得是个不错的点子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '就是这么回事，\n',
            '所以我们也不甘落后地开始叫卖了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    Jump('loc_1347')

    def _loc_12F3(): pass

    label('loc_12F3')

    ChrTalk(
        0x000A,
        (
            '全店都在进行大酬宾，\n',
            '现在出售特殊的商品哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我们也不甘落后地\n',
            '开始叫卖了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1347(): pass

    label('loc_1347')

    Jump('loc_14C0')

    def _loc_134A(): pass

    label('loc_134A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_13A8',
    )

    ChrTalk(
        0x000A,
        (
            '门以及喷水池停止的原因\n',
            '好像还没有查明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '这座商业城镇\n',
            '到底出了什么事儿呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14C0')

    def _loc_13A8(): pass

    label('loc_13A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_1423',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_13E3',
    )

    ChrTalk(
        0x000A,
        (
            '欢迎光临！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '日用的商品一大堆哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1420')

    def _loc_13E3(): pass

    label('loc_13E3')

    ChrTalk(
        0x000A,
        (
            '今天老公来店里\n',
            '帮忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '因此我也能\n',
            '专心经营了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_1420(): pass

    label('loc_1420')

    Jump('loc_14C0')

    def _loc_1423(): pass

    label('loc_1423')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_14C0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1463',
    )

    ChrTalk(
        0x000A,
        (
            '请随便看看吧。\n',
            '里面准备了各种便利的杂货。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14C0')

    def _loc_1463(): pass

    label('loc_1463')

    ChrTalk(
        0x000A,
        (
            '请随便看看吧。\n',
            '里面准备了各种便利的杂货。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '看看～\n',
            '推荐给各位顾客需要的小商品喔！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_14C0(): pass

    label('loc_14C0')

    TalkEnd(0x000A)

    Return()

# id: 0x000D offset: 0x14C4
@scena.Code('func_0D_14C4')
def func_0D_14C4():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_151D',
    )

    ChrTalk(
        0x000B,
        (
            '超市里的全部商人都在\n',
            '进行援助大酬宾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '妈妈好像也\n',
            '比平时更卖力了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17BB')

    def _loc_151D(): pass

    label('loc_151D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_15ED',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_15AB',
    )

    ChrTalk(
        0x000B,
        (
            '看来城里的导力器\n',
            '停止工作了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '我家店里的收款机\n',
            '不能用了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '现在我爸爸去工房了，\n',
            '委托别人来修理机器哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    Jump('loc_15EA')

    def _loc_15AB(): pass

    label('loc_15AB')

    ChrTalk(
        0x000B,
        (
            '看来城里的导力器\n',
            '停止工作了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '到底是怎么一回事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15EA(): pass

    label('loc_15EA')

    Jump('loc_17BB')

    def _loc_15ED(): pass

    label('loc_15ED')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_16E9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_166A',
    )

    ChrTalk(
        0x000B,
        (
            '能够帮上忙，\n',
            '我已经很高兴呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '但爸爸经常把商品\n',
            '摆放错位置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '不早点让他习惯这工作可不行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16E6')

    def _loc_166A(): pass

    label('loc_166A')

    OP_62(0x000B, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    ChrTurnDirection(0x000B, 0x001F, 400)

    ChrTalk(
        0x000B,
        (
            '啊，爸爸。\n',
            '这件商品不是放在那个架子上哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '爸爸你要多加油啊。\n',
            '刚才也搞错啰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)
    ClearChrFlags(0x000B, 0x0010)

    def _loc_16E6(): pass

    label('loc_16E6')

    Jump('loc_17BB')

    def _loc_16E9(): pass

    label('loc_16E9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_17BB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_174E',
    )

    ChrTalk(
        0x000B,
        (
            '我是这里的店员。\n',
            '是来帮妈妈工作的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '本店全是便利的商品，\n',
            '请务必来看一看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17BB')

    def _loc_174E(): pass

    label('loc_174E')

    ChrTalk(
        0x000B,
        (
            '啊，欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '我是这里的店员。\n',
            '我是来帮妈妈干活的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '本店全是便利的商品，\n',
            '请务必来看一看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_17BB(): pass

    label('loc_17BB')

    TalkEnd(0x000B)

    Return()

# id: 0x000E offset: 0x17BF
@scena.Code('func_0E_17BF')
def func_0E_17BF():
    Call(0, 0x000F)

    Return()

# id: 0x000F offset: 0x17C4
@scena.Code('func_0F_17C4')
def func_0F_17C4():
    TalkBegin(0x000C)
    FadeOut(300, 0, 100)

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
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '买东西\n'),
            TXT(0x02, '离开\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_182F',
    )

    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1827',
    )

    OP_A9(0x3C)

    Jump('loc_1829')

    def _loc_1827(): pass

    label('loc_1827')

    OP_A9(0x5A)

    def _loc_1829(): pass

    label('loc_1829')

    OP_56(0x00)
    TalkEnd(0x000C)

    Return()

    def _loc_182F(): pass

    label('loc_182F')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1840',
    )

    TalkEnd(0x000C)

    Return()

    def _loc_1840(): pass

    label('loc_1840')

    If(
        (
            (Expr.Eval, "OP_29(0x0011, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_184D',
    )

    OP_A2(0x0006)

    def _loc_184D(): pass

    label('loc_184D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_18C3',
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
        100,
        0,
        (
            TXT(0x00, '【◇前编QST017通关】\n'),
            TXT(0x01, '【◇前编QST017没有通关】\n'),
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
        (0x00000000, 'loc_18B7'),
        (0x00000001, 'loc_18BD'),
        (-1, 'loc_18C3'),
    )

    def _loc_18B7(): pass

    label('loc_18B7')

    OP_A2(0x0006)

    Jump('loc_18C3')

    def _loc_18BD(): pass

    label('loc_18BD')

    OP_A3(0x0006)

    Jump('loc_18C3')

    def _loc_18C3(): pass

    label('loc_18C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0348, 0, 0x1A40)),
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_1D9E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C68',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_1A21',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_19C1',
    )

    ChrTalk(
        0x000C,
        (
            '呵呵，\n',
            '在这种时候策划大酬宾……\n',
            '年轻人果然干劲十足呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '大酬宾的成功\n',
            '显然离不开梅贝尔市长的协助……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '而且柏斯商人那古老而优秀的品质，\n',
            '直到今天也依然健在呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '当然本店也将把秘蔵的商品\n',
            '摆放出来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    Jump('loc_1A1E')

    def _loc_19C1(): pass

    label('loc_19C1')

    ChrTalk(
        0x000C,
        (
            '呵呵，\n',
            '在这种时候策划大酬宾……\n',
            '年轻人果然干劲十足呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '本店当然也打算参加\n',
            '大酬宾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A1E(): pass

    label('loc_1A1E')

    Jump('loc_1C65')

    def _loc_1A21(): pass

    label('loc_1A21')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1B2B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1AD6',
    )

    ChrTalk(
        0x000C,
        (
            '王国内的流通渠道\n',
            '全都遇到了问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '目前虽然还有一点库存，\n',
            '但假如进货遇到困难的话，\n',
            '商品紧缺只是时间的问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '呼……\n',
            '真是面临基本生活失策的境况啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    Jump('loc_1B28')

    def _loc_1AD6(): pass

    label('loc_1AD6')

    ChrTalk(
        0x000C,
        (
            '王国内的流通渠道\n',
            '全都遇到了问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '呼……\n',
            '真是面临基本生活失策的境况啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B28(): pass

    label('loc_1B28')

    Jump('loc_1C65')

    def _loc_1B2B(): pass

    label('loc_1B2B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_1B9D',
    )

    ChrTalk(
        0x000C,
        (
            '托女王殿下的福，\n',
            '那条龙看来已经被赶走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '超市也顺利修复，\n',
            '又能集中精力投入到商品贸易中去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C65')

    def _loc_1B9D(): pass

    label('loc_1B9D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_1C65',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_1C06',
    )

    ChrTalk(
        0x000C,
        (
            '如果是需要药品的话，\n',
            '请来我的商店看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '七耀教会开发的\n',
            '新药已经投入使用啰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C65')

    def _loc_1C06(): pass

    label('loc_1C06')

    ChrTalk(
        0x000C,
        (
            '如果是需要药品的话，\n',
            '请来我的商店看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '从疗伤药到滋补品\n',
            '各个领域的药物都有啰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    def _loc_1C65(): pass

    label('loc_1C65')

    Jump('loc_1D9B')

    def _loc_1C68(): pass

    label('loc_1C68')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1CD6',
    )

    ChrTalk(
        0x000C,
        (
            '我们这里摆放的都是\n',
            '能在工作上提供方便的药物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '有需要的时候，\n',
            '思潘斯药店就请您多多关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D9B')

    def _loc_1CD6(): pass

    label('loc_1CD6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_1D32',
    )

    ChrTalk(
        0x000C,
        (
            '我们这里摆放的都是\n',
            '能为工作带来便利的药物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '有需要的时候，\n',
            '请多关照啰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D9B')

    def _loc_1D32(): pass

    label('loc_1D32')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_1D9B',
    )

    ChrTalk(
        0x000C,
        (
            '我们这里摆放的都是\n',
            '能为工作带来便利的药物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '有需要的时候，\n',
            '思潘斯药店就请您多多关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D9B(): pass

    label('loc_1D9B')

    Jump('loc_25B6')

    def _loc_1D9E(): pass

    label('loc_1D9E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_205E',
    )

    ChrTurnDirection(0x000C, 0x0101, 0)
    OP_62(0x000C, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTurnDirection(0x000C, 0x0101, 400)

    ChrTalk(
        0x000C,
        (
            '啊，各位是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '曾经帮我寻找药草的\n',
            '游击士们吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011F啊，说起来的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F哈哈……\n',
            '感觉好怀念呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '爷爷\n',
            '还是很健康啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x0102, 400)

    ChrTalk(
        0x000C,
        (
            '呵呵，也就是身体还行，\n',
            '这可是我的长项啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '说起来，那个时候\n',
            '真是多亏了你们的帮助。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '既然机会这么难得，作为谢礼，\n',
            '我送各位一件秘蔵的药品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['还魂粉']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['还魂粉'], 1)

    ChrTalk(
        0x000C,
        (
            '请不必客气，\n',
            '各位尽管收下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '这是我的\n',
            '一点心意啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1001F哇，谢谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '这样的话\n',
            '就不客气地接受啰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1041F对不起……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '此外也摆放着很多\n',
            '能在工作上提供方便的药物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '有需要的时候，\n',
            '请多关照啰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F嗯，知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '（不，不愧是生意人……\n',
            '  永远不忘记拉客。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25B0')

    def _loc_205E(): pass

    label('loc_205E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_2340',
    )

    ChrTurnDirection(0x000C, 0x0101, 0)
    OP_62(0x000C, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x000C,
        (
            '啊，各位是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '曾经帮我寻找药草的\n',
            '游击士们吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F好象…这么说\n',
            '是有这么回事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1000F好久不见了。\n',
            '这次好象还挺严重呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '哈哈哈。\n',
            '这不算什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '完全不能够和\n',
            '百日战役相比。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '这不谈这个了，\n',
            '难得你们能来我的店铺。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '我有一份谢礼\n',
            '要送给你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011F谢礼……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '哈哈哈，\n',
            '就当我给你们赶走龙后的谢礼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['还魂粉']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['还魂粉'], 1)

    ChrTalk(
        0x000C,
        (
            '这是效果很不错的药，\n',
            '我想肯定能帮到你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '请不必客气。\n',
            '各位尽管收下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1001F哇，谢谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '既然这样的话\n',
            '我们就不客气地收下啰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '此外还摆放着很多\n',
            '能在工作上提供方便的药物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '有需要的时候，\n',
            '请多关照啰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F嗯，知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '（不，不愧是生意人……\n',
            '  永远不忘记拉客。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25B0')

    def _loc_2340(): pass

    label('loc_2340')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_25B0',
    )

    ChrTurnDirection(0x000C, 0x0101, 0)
    OP_62(0x000C, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x000C,
        (
            '啊，各位是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '曾经帮我寻找药草的\n',
            '游击士们吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F好象…这么说\n',
            '是有这么回事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1000F好久不见。\n',
            '老爷爷您还好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '嗯嗯，还是老样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '不过那个时候\n',
            '真是多亏了你的帮助。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '既然机会这么难得，作为谢礼，\n',
            '我送各位一件秘蔵的药品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['还魂粉']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['还魂粉'], 1)

    ChrTalk(
        0x000C,
        (
            '请不必客气，\n',
            '各位尽管收下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '这是我的\n',
            '一点心意啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1001F哇，谢谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '这样的话\n',
            '就不客气地收下啰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '此外还摆放着很多\n',
            '能在工作上提供方便的药物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '有需要的时候，\n',
            '请多关照啰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F嗯，知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '（不，不愧是生意人……\n',
            '  永远不忘记拉客。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_25B0(): pass

    label('loc_25B0')

    OP_A2(0x1A40)
    OP_A2(0x0004)
    def _loc_25B6(): pass

    label('loc_25B6')

    TalkEnd(0x000C)

    Return()

# id: 0x0010 offset: 0x25BA
@scena.Code('func_10_25BA')
def func_10_25BA():
    TalkBegin(0x000D)
    FadeOut(300, 0, 100)

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
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '买东西\n'),
            TXT(0x02, '离开\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2625',
    )

    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_261D',
    )

    OP_A9(0x3F)

    Jump('loc_261F')

    def _loc_261D(): pass

    label('loc_261D')

    OP_A9(0x5E)

    def _loc_261F(): pass

    label('loc_261F')

    OP_56(0x00)
    TalkEnd(0x000D)

    Return()

    def _loc_2625(): pass

    label('loc_2625')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2636',
    )

    TalkEnd(0x000D)

    Return()

    def _loc_2636(): pass

    label('loc_2636')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_272D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_26B0',
    )

    ChrTalk(
        0x000D,
        (
            '欢迎光临！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '柏斯超市的招牌商品，\n',
            '美味可口，尝过之后必定难忘的蛋糕～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '来一块怎么样！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0007)

    Jump('loc_272A')

    def _loc_26B0(): pass

    label('loc_26B0')

    ChrTalk(
        0x000D,
        (
            '一心想让客人们\n',
            '打起精神来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '于是就跟大家伙一起\n',
            '举办了大酬宾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '至少在买东西的时候\n',
            '希望看到大家的笑脸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A3(0x0007)

    def _loc_272A(): pass

    label('loc_272A')

    Jump('loc_29CD')

    def _loc_272D(): pass

    label('loc_272D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2848',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_27D7',
    )

    ChrTalk(
        0x000D,
        (
            '对做蛋糕来说，\n',
            '新鲜的鸡蛋和牛奶是必不可少的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '今后如果一直无法进到材料的话，\n',
            '我的摊位将开不下去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '唉，真是的……\n',
            '到底该怎么办才好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0007)

    Jump('loc_2845')

    def _loc_27D7(): pass

    label('loc_27D7')

    ChrTalk(
        0x000D,
        (
            '对做蛋糕来说，\n',
            '新鲜的鸡蛋和牛奶是必不可少的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '今后如果一直无法进到材料的话，\n',
            '我的摊位将开不下去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2845(): pass

    label('loc_2845')

    Jump('loc_29CD')

    def _loc_2848(): pass

    label('loc_2848')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_2905',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_28B0',
    )

    ChrTalk(
        0x000D,
        (
            '柏斯超市的招牌产品，\n',
            '美味可口，尝过之后必定难忘的鸡蛋糕～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '来一块怎么样！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2902')

    def _loc_28B0(): pass

    label('loc_28B0')

    ChrTalk(
        0x000D,
        (
            '欢迎光临！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '柏斯超市的招牌商品，\n',
            '美味可口，尝过之后必定难忘的蛋糕～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0007)

    def _loc_2902(): pass

    label('loc_2902')

    Jump('loc_29CD')

    def _loc_2905(): pass

    label('loc_2905')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_29CD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_2965',
    )

    ChrTalk(
        0x000D,
        (
            '欢迎光临！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '柏斯超市的招牌商品，\n',
            '美味可口，尝过之后必定难忘的蛋糕～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29CD')

    def _loc_2965(): pass

    label('loc_2965')

    ChrTalk(
        0x000D,
        (
            '欢迎光临！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '柏斯超市的招牌商品，\n',
            '美味可口，尝过之后必定难忘的蛋糕～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '来一块怎么样！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0007)

    def _loc_29CD(): pass

    label('loc_29CD')

    TalkEnd(0x000D)

    Return()

# id: 0x0011 offset: 0x29D1
@scena.Code('func_11_29D1')
def func_11_29D1():
    TalkBegin(0x000E)
    FadeOut(300, 0, 100)

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
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '买东西\n'),
            TXT(0x02, '离开\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2A3C',
    )

    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2A34',
    )

    OP_A9(0x43)

    Jump('loc_2A36')

    def _loc_2A34(): pass

    label('loc_2A34')

    OP_A9(0x5B)

    def _loc_2A36(): pass

    label('loc_2A36')

    OP_56(0x00)
    TalkEnd(0x000E)

    Return()

    def _loc_2A3C(): pass

    label('loc_2A3C')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2A4D',
    )

    TalkEnd(0x000E)

    Return()

    def _loc_2A4D(): pass

    label('loc_2A4D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_2B8E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2B51',
    )

    ChrTalk(
        0x000E,
        (
            '全店大酬宾\n',
            '可真是个不错的计划。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '卡特丽亚那家伙也来了干劲，\n',
            '我们也参加了酬宾哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '总之，\n',
            '此事全靠梅贝尔市长的协助。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '市长说服了大商人，\n',
            '让他们不要不舍得把库存的商品拿出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '假如不这么做的话，\n',
            '现在物价肯定飞速上涨了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)

    Jump('loc_2B8B')

    def _loc_2B51(): pass

    label('loc_2B51')

    ChrTalk(
        0x000E,
        (
            '欢迎光临！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '在王都也很受欢迎的\n',
            '美味冰淇淋哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A3(0x0008)

    def _loc_2B8B(): pass

    label('loc_2B8B')

    Jump('loc_2D5A')

    def _loc_2B8E(): pass

    label('loc_2B8E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2C67',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2C18',
    )

    ChrTalk(
        0x000E,
        (
            '超市里也完全\n',
            '失去了活力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '大家果然对今后\n',
            '会怎样很不安呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '可恶，越是这种时候，\n',
            '就越想出一份力，但……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)

    Jump('loc_2C64')

    def _loc_2C18(): pass

    label('loc_2C18')

    ChrTalk(
        0x000E,
        (
            '连超市\n',
            '都消沉下来就全完了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '越是这种时候，\n',
            '就越想出一份力，但……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C64(): pass

    label('loc_2C64')

    Jump('loc_2D5A')

    def _loc_2C67(): pass

    label('loc_2C67')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_2CDF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_2CA8',
    )

    ChrTalk(
        0x000E,
        (
            '欢迎光临，欢迎光临！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '美味的冰淇淋哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2CDC')

    def _loc_2CA8(): pass

    label('loc_2CA8')

    ChrTalk(
        0x000E,
        (
            '欢迎光临！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '美味的冰淇淋也\n',
            '终于复活了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)

    def _loc_2CDC(): pass

    label('loc_2CDC')

    Jump('loc_2D5A')

    def _loc_2CDF(): pass

    label('loc_2CDF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_2D5A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_2D20',
    )

    ChrTalk(
        0x000E,
        (
            '欢迎光临，欢迎光临！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '美味的冰淇淋哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D5A')

    def _loc_2D20(): pass

    label('loc_2D20')

    ChrTalk(
        0x000E,
        (
            '欢迎光临！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '在王都也很受欢迎的\n',
            '美味冰淇淋哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)

    def _loc_2D5A(): pass

    label('loc_2D5A')

    TalkEnd(0x000E)

    Return()

# id: 0x0012 offset: 0x2D5E
@scena.Code('func_12_2D5E')
def func_12_2D5E():
    Call(0, 0x0013)

    Return()

# id: 0x0013 offset: 0x2D63
@scena.Code('func_13_2D63')
def func_13_2D63():
    TalkBegin(0x000F)
    FadeOut(300, 0, 100)

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
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '买东西\n'),
            TXT(0x02, '离开\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2DCE',
    )

    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2DC6',
    )

    OP_A9(0x41)

    Jump('loc_2DC8')

    def _loc_2DC6(): pass

    label('loc_2DC6')

    OP_A9(0x5D)

    def _loc_2DC8(): pass

    label('loc_2DC8')

    OP_56(0x00)
    TalkEnd(0x000F)

    Return()

    def _loc_2DCE(): pass

    label('loc_2DCE')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2DDF',
    )

    TalkEnd(0x000F)

    Return()

    def _loc_2DDF(): pass

    label('loc_2DDF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_2EAD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2E6D',
    )

    ChrTalk(
        0x000F,
        (
            '欢迎光临。\n',
            '不嫌弃的话请看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '哈哈，已经很久没有\n',
            '这么大声招呼客人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '因为这种经验方式\n',
            '不是我的风格嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    Jump('loc_2EAA')

    def _loc_2E6D(): pass

    label('loc_2E6D')

    ChrTalk(
        0x000F,
        (
            '欢迎光临。\n',
            '不嫌弃的话请看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '肯定能让你满意的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2EAA(): pass

    label('loc_2EAA')

    Jump('loc_336E')

    def _loc_2EAD(): pass

    label('loc_2EAD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2FF9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2F88',
    )

    ChrTalk(
        0x000F,
        (
            '导力器竟然无法使用……\n',
            '真是一点办法也没有了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '我家的照明灯也坏了，\n',
            '女儿为此大哭了一场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '对那个孩子来说，\n',
            '导力器是理所当然的日常用品啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '当知道无法使用后，\n',
            '对她或许是一大打击吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    Jump('loc_2FF6')

    def _loc_2F88(): pass

    label('loc_2F88')

    ChrTalk(
        0x000F,
        (
            '到了我女儿这一代，\n',
            '导力器已经成了理所当然的日用品了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '对孩子们的打击\n',
            '或许比我们大人更大也说不定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2FF6(): pass

    label('loc_2FF6')

    Jump('loc_336E')

    def _loc_2FF9(): pass

    label('loc_2FF9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_30F0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_305C',
    )

    ChrTalk(
        0x000F,
        (
            '一定要带女儿来\n',
            '恢复营业后的超市看看呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '要让她知道\n',
            '这座镇子已经安全了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_30ED')

    def _loc_305C(): pass

    label('loc_305C')

    ChrTalk(
        0x000F,
        (
            '我把女儿艾尔珂带来了，\n',
            '想让她看看\n',
            '超市恢复营业后的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '因为女儿她\n',
            '可是我们这里的招牌啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '『泊尔·艾尔珂』\n',
            '今后就请多关照了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    def _loc_30ED(): pass

    label('loc_30ED')

    Jump('loc_336E')

    def _loc_30F0(): pass

    label('loc_30F0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_336E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0348, 1, 0x1A41)),
            Expr.Return,
        ),
        'loc_3215',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_317A',
    )

    ChrTalk(
        0x000F,
        (
            '王都的商店和柏斯的果然各有千秋，\n',
            '真是不分伯仲啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '为了商店能够大张旗鼓地营业，\n',
            '我要更加专心致志才行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3212')

    def _loc_317A(): pass

    label('loc_317A')

    ChrTurnDirection(0x000F, 0x0101, 0)

    ChrTalk(
        0x000F,
        (
            '嗯，你的这件衣服……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '明明是出于以实用设计为目的，\n',
            '但却保留了少女那种楚楚动人的韵味……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '虽然不甘心，\n',
            '但不愧是王都一流的品牌啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    def _loc_3212(): pass

    label('loc_3212')

    Jump('loc_336E')

    def _loc_3215(): pass

    label('loc_3215')

    ChrTalk(
        0x000F,
        (
            '欢迎光临。\n',
            '今天想看些什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000F, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x000F, 0x0101, 400)
    Sleep(400)

    ChrTalk(
        0x000F,
        (
            '噢，这件衣服……\n',
            '是王都的牌子吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1004F嘿，真清楚呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_32C9',
    )

    ChrTalk(
        0x0103,
        (
            '#021F呵呵，不愧是行家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000F, 0x0103, 400)

    def _loc_32C9(): pass

    label('loc_32C9')

    ChrTalk(
        0x000F,
        (
            '哈哈，这个嘛，\n',
            '和以前所见过的品牌不同嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000F, 0x0101, 400)

    ChrTalk(
        0x000F,
        (
            '但是，一流品牌……\n',
            '这也是订做的吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '虽然很不甘心……\n',
            '但这设计实在太棒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '唉，我也要加油了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1A41)

    def _loc_336E(): pass

    label('loc_336E')

    TalkEnd(0x000F)

    Return()

# id: 0x0014 offset: 0x3372
@scena.Code('func_14_3372')
def func_14_3372():
    TalkBegin(0x0010)
    FadeOut(300, 0, 100)

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
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '买东西\n'),
            TXT(0x02, '离开\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_340B',
    )

    OP_0D()

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_33E6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_33E1',
    )

    OP_A9(0x4C)

    Jump('loc_33E3')

    def _loc_33E1(): pass

    label('loc_33E1')

    OP_A9(0x4D)

    def _loc_33E3(): pass

    label('loc_33E3')

    Jump('loc_3405')

    def _loc_33E6(): pass

    label('loc_33E6')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_33F7',
    )

    OP_A9(0x45)

    Jump('loc_3405')

    def _loc_33F7(): pass

    label('loc_33F7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_3403',
    )

    OP_A9(0x44)

    Jump('loc_3405')

    def _loc_3403(): pass

    label('loc_3403')

    OP_A9(0x42)

    def _loc_3405(): pass

    label('loc_3405')

    OP_56(0x00)
    TalkEnd(0x0010)

    Return()

    def _loc_340B(): pass

    label('loc_340B')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_341C',
    )

    TalkEnd(0x0010)

    Return()

    def _loc_341C(): pass

    label('loc_341C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_358E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0218, 2, 0x10C2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3545',
    )

    ChrTalk(
        0x0010,
        (
            '全店大酬宾\n',
            '这事和我无关啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '反正我的店铺\n',
            '每天都在营业嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '呵呵，本店也打算作为赞助商\n',
            '让售卖廉价商品的活动流行起来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '喂喂，那边的小姑娘，\n',
            '读读这本书打起精神来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['牌技师杰克 14卷']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    AddItem(ItemTable['牌技师杰克 14卷'], 1)
    OP_A2(0x10C2)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#1004F哇，谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_358B')

    def _loc_3545(): pass

    label('loc_3545')

    ChrTalk(
        0x0010,
        (
            '全店的大酬宾\n',
            '这事和我无关啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '反正我的店铺\n',
            '每天都在营业嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_358B(): pass

    label('loc_358B')

    Jump('loc_38BC')

    def _loc_358E(): pass

    label('loc_358E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_369D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3638',
    )

    ChrTalk(
        0x00FE,
        (
            '不管物流停滞与否，\n',
            '我店跟平时一样准时开门哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正是这种时候，\n',
            '才更要让大家鼓起勇气啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……这样的话，\n',
            '不如把秘藏的那本新刊拿出来卖吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000A)

    Jump('loc_369A')

    def _loc_3638(): pass

    label('loc_3638')

    ChrTalk(
        0x00FE,
        (
            '正是这种时候，\n',
            '才更要让大家鼓起勇气啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……这样的话，\n',
            '不如把秘藏的那本新刊拿出来卖吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_369A(): pass

    label('loc_369A')

    Jump('loc_38BC')

    def _loc_369D(): pass

    label('loc_369D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_37D0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_36F5',
    )

    ChrTalk(
        0x0010,
        (
            '共和国制最高級的绒毯～\n',
            '只要５００米拉！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '并且买一张送一张哟！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_37CD')

    def _loc_36F5(): pass

    label('loc_36F5')

    ChrTalk(
        0x0010,
        (
            '看一看。\n',
            '瞧一瞧！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '共和国制最高級的绒毯～\n',
            '只要５００米拉！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '只要５００米拉哟！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '除此之外！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '现在正值\n',
            '恢复营业的纪念活动期间……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '买一条绒毯\n',
            '#4S送一条绒毯！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '走过路过千万不要错过！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000A)

    def _loc_37CD(): pass

    label('loc_37CD')

    Jump('loc_38BC')

    def _loc_37D0(): pass

    label('loc_37D0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_38BC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_3845',
    )

    ChrTalk(
        0x0010,
        (
            '古书，纺织品，日用品，应有尽有！\n',
            '这就是米蕾婆婆的杂货店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '请来看一看。\n',
            '杂志的新刊也到啰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_38BC')

    def _loc_3845(): pass

    label('loc_3845')

    ChrTalk(
        0x0010,
        (
            '欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '古书，纺织品，日用品，应有尽有！\n',
            '这就是米蕾婆婆的杂货店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '请来看一看。\n',
            '杂志的新刊也到啰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000A)

    def _loc_38BC(): pass

    label('loc_38BC')

    TalkEnd(0x0010)

    Return()

# id: 0x0015 offset: 0x38C0
@scena.Code('func_15_38C0')
def func_15_38C0():
    TalkBegin(0x0011)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_39A0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3951',
    )

    ChrTalk(
        0x0011,
        (
            '不愧是大酬宾，\n',
            '超市很有活力了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '感觉很久以前的\n',
            '活力又回来了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '再加上小姐前来视察，\n',
            '大家格外的卖力呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000B)

    Jump('loc_399D')

    def _loc_3951(): pass

    label('loc_3951')

    ChrTalk(
        0x0011,
        (
            '不愧是大酬宾，\n',
            '超市很有活力了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '感觉很久以前的\n',
            '活力又回来了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_399D(): pass

    label('loc_399D')

    Jump('loc_3CC0')

    def _loc_39A0(): pass

    label('loc_39A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_3AAD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3A5A',
    )

    ChrTalk(
        0x0011,
        (
            '呀，欢迎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '虽然米蕾婆婆很有精神……\n',
            '但是超市其他的店铺气氛\n',
            '有点消沉呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '好不容易恢复了营业，\n',
            '谁知物流却突然瘫痪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '因此变得消沉也是没有办法的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000B)

    Jump('loc_3AAA')

    def _loc_3A5A(): pass

    label('loc_3A5A')

    ChrTalk(
        0x0011,
        (
            '米蕾婆婆\n',
            '跟平时一样精神啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '婆婆的生意人精神\n',
            '在柏斯里是首屈一指的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3AAA(): pass

    label('loc_3AAA')

    Jump('loc_3CC0')

    def _loc_3AAD(): pass

    label('loc_3AAD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_3B94',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_3B0C',
    )

    ChrTalk(
        0x0011,
        (
            '军队的戒严解除了，\n',
            '物流也恢复了正常。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '因此，\n',
            '新刊也差不多快送到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3B91')

    def _loc_3B0C(): pass

    label('loc_3B0C')

    ChrTalk(
        0x0011,
        (
            '呀，欢迎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '军队的戒严解除了，\n',
            '物流总算恢复正常了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '因此，\n',
            '我们这里新刊也开始陆续到货了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '不介意的话来看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000B)

    def _loc_3B91(): pass

    label('loc_3B91')

    Jump('loc_3CC0')

    def _loc_3B94(): pass

    label('loc_3B94')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_3CC0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_3C05',
    )

    ChrTalk(
        0x0011,
        (
            '别看我这样，\n',
            '其实我是这间店铺的店员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '因为我太喜欢书，\n',
            '所以被人招来这里，当起了店员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3CC0')

    def _loc_3C05(): pass

    label('loc_3C05')

    ChrTalk(
        0x0011,
        (
            '呀，欢迎。\n',
            '最新号的杂志已经到啰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '别看我这样，\n',
            '其实我是这间店铺的店员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '因为我太喜欢书，\n',
            '所以被人招来这里，当起了店员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '呵呵，\n',
            '没想到会在经常光顾的店里当起店员来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000B)

    def _loc_3CC0(): pass

    label('loc_3CC0')

    TalkEnd(0x0011)

    Return()

# id: 0x0016 offset: 0x3CC4
@scena.Code('func_16_3CC4')
def func_16_3CC4():
    TalkBegin(0x0012)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_3DC7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3D6D',
    )

    ChrTalk(
        0x00FE,
        (
            '呵呵呵，就是这个。\n',
            '我一直在等的就是这个！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '酬宾，特卖，大减价！！\n',
            '啊啊，多么动听的声音。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要听到这些词语，\n',
            '不管何时都会精神百倍！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000C)

    Jump('loc_3DC4')

    def _loc_3D6D(): pass

    label('loc_3D6D')

    ChrTalk(
        0x00FE,
        (
            '假如有特卖会的话，\n',
            '最佳位置是绝对不会让给别人的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哼哼，开始的同时发动攻击！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3DC4(): pass

    label('loc_3DC4')

    Jump('loc_4003')

    def _loc_3DC7(): pass

    label('loc_3DC7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_3E3B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3E38',
    )

    ChrTalk(
        0x00FE,
        (
            '定期船和货车都停开了，\n',
            '这的确是最严重的事态。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之，\n',
            '得趁物品尚未短缺之前大买特买才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3E38(): pass

    label('loc_3E38')

    Jump('loc_4003')

    def _loc_3E3B(): pass

    label('loc_3E3B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_3F30',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_3EB2',
    )

    ChrTalk(
        0x00FE,
        (
            '呵呵呵，\n',
            '今天有一场为纪念重新开业的大酬宾呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我特意早早赶来排队，\n',
            '就是为了确保最佳的位置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3F2D')

    def _loc_3EB2(): pass

    label('loc_3EB2')

    ChrTalk(
        0x00FE,
        (
            '呵呵呵，\n',
            '今天有一场为纪念重新开业的大酬宾呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊，久违的大减价啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最佳位置，\n',
            '是绝对不会让给别人的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000C)

    def _loc_3F2D(): pass

    label('loc_3F2D')

    Jump('loc_4003')

    def _loc_3F30(): pass

    label('loc_3F30')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_4003',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_3F87',
    )

    ChrTalk(
        0x00FE,
        (
            '上午的特卖会\n',
            '好像结束了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '下一个目标是\n',
            '傍晚的限时大甩卖。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4003')

    def _loc_3F87(): pass

    label('loc_3F87')

    ChrTalk(
        0x00FE,
        (
            '那么，上午的特卖\n',
            '好像结束了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，\n',
            '今天当然也把每家店铺都逛过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '收获就是……\n',
            '肉的最低价又被刷新了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000C)

    def _loc_4003(): pass

    label('loc_4003')

    TalkEnd(0x0012)

    Return()

# id: 0x0017 offset: 0x4007
@scena.Code('func_17_4007')
def func_17_4007():
    TalkBegin(0x0014)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_409A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_405E',
    )

    ChrTalk(
        0x00FE,
        (
            '酬宾就是……\n',
            '大型展销会吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样啊，丽露露也知道啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000D)

    Jump('loc_4097')

    def _loc_405E(): pass

    label('loc_405E')

    ChrTalk(
        0x00FE,
        (
            '在酬宾时买东西\n',
            '妈妈会很高兴的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好，要加油了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4097(): pass

    label('loc_4097')

    Jump('loc_42A9')

    def _loc_409A(): pass

    label('loc_409A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_40FC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_40DD',
    )

    ChrTalk(
        0x00FE,
        (
            '喷水池也没有精神呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎么回事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000D)

    Jump('loc_40F9')

    def _loc_40DD(): pass

    label('loc_40DD')

    ChrTalk(
        0x00FE,
        (
            '喷水池也没有精神呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_40F9(): pass

    label('loc_40F9')

    Jump('loc_42A9')

    def _loc_40FC(): pass

    label('loc_40FC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_41CE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_4147',
    )

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，\n',
            '今天吃蛋糕！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '蛋糕、蛋糕\n',
            '蛋糕、蛋～～糕⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_41CB')

    def _loc_4147(): pass

    label('loc_4147')

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，今天\n',
            '我可不是被人叫出来买东西的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那你是得到了零用钱，\n',
            '自己来买东西的了⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我要吃姐姐卖的那种\n',
            '软绵绵的蛋糕！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000D)

    def _loc_41CB(): pass

    label('loc_41CB')

    Jump('loc_42A9')

    def _loc_41CE(): pass

    label('loc_41CE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_42A9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_4229',
    )

    ChrTalk(
        0x00FE,
        (
            '奶酪加上苹果加上\n',
            '香喷喷的芋头⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '奶酪加上苹果加上\n',
            '香喷喷的芋头⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_42A9')

    def _loc_4229(): pass

    label('loc_4229')

    ChrTalk(
        0x00FE,
        (
            '已经可以一个人\n',
            '去买东西了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个，\n',
            '就是把买的东西编成歌记住了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '奶酪加上苹果加上\n',
            '香芋头⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，厉害吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000D)

    def _loc_42A9(): pass

    label('loc_42A9')

    TalkEnd(0x0014)

    Return()

# id: 0x0018 offset: 0x42AD
@scena.Code('func_18_42AD')
def func_18_42AD():
    TalkBegin(0x0015)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_439D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_434A',
    )

    ChrTalk(
        0x00FE,
        (
            '嘻嘻。\n',
            '在这种时候卖东西？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，岂止是一点点，\n',
            '这不是一件非常令人愉快的事吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不愧是柏斯超市。\n',
            '非常理解百姓的心情啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000E)

    Jump('loc_439A')

    def _loc_434A(): pass

    label('loc_434A')

    ChrTalk(
        0x00FE,
        (
            '这么难得的大减价，\n',
            '真想做一道丰盛的晚餐呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，\n',
            '今天要做什么菜呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_439A(): pass

    label('loc_439A')

    Jump('loc_4669')

    def _loc_439D(): pass

    label('loc_439D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_4409',
    )

    ChrTalk(
        0x00FE,
        (
            '由于导力器停止了工作，\n',
            '照明和暖房都无法使用了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '吃的东西买好了，\n',
            '接下来得去看看杂货了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4669')

    def _loc_4409(): pass

    label('loc_4409')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_45CB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Return,
        ),
        'loc_44D5',
    )

    ChrTalk(
        0x00FE,
        (
            '如果店铺能在卖菜的同时提供菜单就好了。\n',
            '那样就可以从中得到做菜的灵感也说不定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样的话就能\n',
            '帮主妇们分忧解难了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，细想一下这是理所当然的吧。\n',
            '得赶紧去和店里的人沟通一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_45C8')

    def _loc_44D5(): pass

    label('loc_44D5')

    ChrTalk(
        0x00FE,
        (
            '肉，蔬菜，鱼……\n',
            '唉，今天该怎么办呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '作为店铺，不能光是售卖做菜的材料。\n',
            '要是也能提供菜单给顾客就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……细想之下确实如此啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在买吸尘器的时候，\n',
            '店员不是也会教我们使用的方法吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '鱼和肉之类的\n',
            '为什么不能也这样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000E)

    def _loc_45C8(): pass

    label('loc_45C8')

    Jump('loc_4669')

    def _loc_45CB(): pass

    label('loc_45CB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_4669',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Return,
        ),
        'loc_4622',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，\n',
            '今天做什么菜呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '干脆去看看有什么特卖品\n',
            '配合着来做吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4669')

    def _loc_4622(): pass

    label('loc_4622')

    ChrTalk(
        0x00FE,
        (
            '今日的配菜\n',
            '做什么好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要在傍晚的特卖开始前\n',
            '决定好才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000E)

    def _loc_4669(): pass

    label('loc_4669')

    TalkEnd(0x0015)

    Return()

# id: 0x0019 offset: 0x466D
@scena.Code('func_19_466D')
def func_19_466D():
    TalkBegin(0x0016)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_4701',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_46E1',
    )

    ChrTalk(
        0x00FE,
        (
            '超市终于\n',
            '恢复往日的样子啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，看来今天能够集中精神\n',
            '进行古董鉴赏了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x00FE, 90, 0)
    SetChrFlags(0x00FE, 0x0010)
    OP_A2(0x000F)

    Jump('loc_46FE')

    def _loc_46E1(): pass

    label('loc_46E1')

    ChrTalk(
        0x00FE,
        (
            '嗯…\n',
            '这碟子相当高级啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_46FE(): pass

    label('loc_46FE')

    Jump('loc_497F')

    def _loc_4701(): pass

    label('loc_4701')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_47E9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_478C',
    )

    ChrTalk(
        0x00FE,
        (
            '导力器全都瘫痪了，\n',
            '连保卫国家都做不到……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '心里总觉得有点不安呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '帝国若是能\n',
            '遵守互不侵犯条约就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000F)

    Jump('loc_47E6')

    def _loc_478C(): pass

    label('loc_478C')

    ChrTalk(
        0x00FE,
        (
            '导力器全都瘫痪了，\n',
            '连保卫国家都做不到……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '帝国若是能\n',
            '遵守互不侵犯条约就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_47E6(): pass

    label('loc_47E6')

    Jump('loc_497F')

    def _loc_47E9(): pass

    label('loc_47E9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_48F5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Return,
        ),
        'loc_485C',
    )

    ChrTalk(
        0x00FE,
        (
            '前几天，\n',
            '我得到了去市长官邸参观古董的机会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '近距离观赏那些珍品，\n',
            '使我的眼光得到了磨练。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_48F2')

    def _loc_485C(): pass

    label('loc_485C')

    ChrTalk(
        0x00FE,
        (
            '前几天，\n',
            '机缘巧合下拜访了市长官邸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '参观了官邸内的\n',
            '很多古董。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呀，真品果然非同一般啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '拜那次机会所赐，\n',
            '我的眼光也得到了磨练。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000F)

    def _loc_48F2(): pass

    label('loc_48F2')

    Jump('loc_497F')

    def _loc_48F5(): pass

    label('loc_48F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_497F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Return,
        ),
        'loc_4927',
    )

    ChrTalk(
        0x00FE,
        (
            '呵呵，\n',
            '这件东西相当不错啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_497F')

    def _loc_4927(): pass

    label('loc_4927')

    ChrTalk(
        0x00FE,
        (
            '我对古董很感兴趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '像这样寻找出土的文物，\n',
            '就是我每天都要做的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000F)
    OP_8C(0x0016, 90, 0)
    SetChrFlags(0x0016, 0x0010)

    def _loc_497F(): pass

    label('loc_497F')

    TalkEnd(0x0016)

    Return()

# id: 0x001A offset: 0x4983
@scena.Code('func_1A_4983')
def func_1A_4983():
    TalkBegin(0x0013)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_4A59',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4A06',
    )

    ChrTalk(
        0x00FE,
        (
            '啊啊，\n',
            '超市果然是个好地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听着大家的声音，\n',
            '我也精神百倍了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，\n',
            '下定决心来了可真好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0010)

    Jump('loc_4A56')

    def _loc_4A06(): pass

    label('loc_4A06')

    ChrTalk(
        0x00FE,
        (
            '听着精神十足的声音，\n',
            '我也精神百倍了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，\n',
            '超市果然还是要这样才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4A56(): pass

    label('loc_4A56')

    Jump('loc_4BDB')

    def _loc_4A59(): pass

    label('loc_4A59')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_4AAB',
    )

    ChrTalk(
        0x00FE,
        (
            '大家的脸上\n',
            '又恢复了笑容了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '超市果然是\n',
            '这座柏斯市的象征啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4BDB')

    def _loc_4AAB(): pass

    label('loc_4AAB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_4BDB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Return,
        ),
        'loc_4B31',
    )

    ChrTalk(
        0x00FE,
        (
            '来到超市，\n',
            '让我感觉到了人们的活力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这是因为\n',
            '我从小就在这里长大。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我被这充满生机的世界\n',
            '深深的吸引了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4BDB')

    def _loc_4B31(): pass

    label('loc_4B31')

    ChrTalk(
        0x00FE,
        (
            '父母禁止我\n',
            '来超市……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我一直瞒着他们\n',
            '来这里玩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我非常喜欢这\n',
            '超市的气氛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然人来人往的，\n',
            '的确不是非常整洁的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但这里的人们\n',
            '充满了活力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0010)

    def _loc_4BDB(): pass

    label('loc_4BDB')

    TalkEnd(0x0013)

    Return()

# id: 0x001B offset: 0x4BDF
@scena.Code('func_1B_4BDF')
def func_1B_4BDF():
    TalkBegin(0x0017)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_4CFC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4CA3',
    )

    ChrTalk(
        0x00FE,
        (
            '蛋糕店的姐姐\n',
            '也恢复往常的笑容了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '或许是受到了\n',
            '开冰淇淋店的未婚夫的鼓励吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '假如真的是这样的话，\n',
            '我们就认同那个家伙吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今后也希望他能够\n',
            '保护那位姐姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0011)

    Jump('loc_4CF9')

    def _loc_4CA3(): pass

    label('loc_4CA3')

    ChrTalk(
        0x00FE,
        (
            '蛋糕店的姐姐\n',
            '也恢复往常的笑容了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '或许是受到了\n',
            '开冰淇淋店的未婚夫的鼓励吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4CF9(): pass

    label('loc_4CF9')

    Jump('loc_507B')

    def _loc_4CFC(): pass

    label('loc_4CFC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_4E4F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4DFA',
    )

    ChrTalk(
        0x00FE,
        (
            '蛋糕店的姐姐\n',
            '好像也无精打采的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，情况这么糟糕，\n',
            '不管换了是谁都会这样吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '她的未婚夫干什么去了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这种时候在身旁给予支持，\n',
            '不是身为伴侣的职责吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的……要不趁着买东西的时候\n',
            '好好教育那家伙一番吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0011)

    Jump('loc_4E4C')

    def _loc_4DFA(): pass

    label('loc_4DFA')

    ChrTalk(
        0x00FE,
        (
            '姐姐一点精神都没有，\n',
            '她的未婚夫跑去哪里了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还真想过去\n',
            '教训教训他一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4E4C(): pass

    label('loc_4E4C')

    Jump('loc_507B')

    def _loc_4E4F(): pass

    label('loc_4E4F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_4F02',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_4EAE',
    )

    ChrTalk(
        0x00FE,
        (
            '姐姐还是\n',
            '露出开朗笑容的时候最棒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明明肚子饱饱的\n',
            '却又想买蛋糕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4EFF')

    def _loc_4EAE(): pass

    label('loc_4EAE')

    ChrTalk(
        0x00FE,
        (
            '蛋糕店姐姐的笑容\n',
            '真是耀眼啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '全力帮忙施工来的，\n',
            '觉得十分有意义哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0011)

    def _loc_4EFF(): pass

    label('loc_4EFF')

    Jump('loc_507B')

    def _loc_4F02(): pass

    label('loc_4F02')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_507B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_4F96',
    )

    ChrTalk(
        0x00FE,
        (
            '那个卖蛋糕的未婚夫\n',
            '就在对面经营冰淇淋店呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '既然都订婚了，\n',
            '怎么不一起开店呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，作为姐姐的仰慕者\n',
            '其实这样倒好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_507B')

    def _loc_4F96(): pass

    label('loc_4F96')

    ChrTalk(
        0x00FE,
        (
            '啊啊，蛋糕店的\n',
            '姐姐笑起来真是漂亮。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，其实那位姐姐\n',
            '已经有约定将来的人了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那年轻人就在对面\n',
            '开冰淇淋店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像是个不服输的人，\n',
            '为了不输给姐姐的店\n',
            '自己也开了店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '既然都订婚了，\n',
            '一起开店不就好了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0011)

    def _loc_507B(): pass

    label('loc_507B')

    TalkEnd(0x0017)

    Return()

# id: 0x001C offset: 0x507F
@scena.Code('func_1C_507F')
def func_1C_507F():
    TalkBegin(0x0018)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_519A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 2, 0x12)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_513D',
    )

    ChrTalk(
        0x00FE,
        (
            '超市全店好像\n',
            '都开始打折了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这、这种时候\n',
            '竟然会打折…真是厉害啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不愧是柏斯超市。\n',
            '真有种顾客至上的感觉啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我、我再不振作精神\n',
            '可就跟不上了哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0012)

    Jump('loc_5197')

    def _loc_513D(): pass

    label('loc_513D')

    ChrTalk(
        0x00FE,
        (
            '这种时候竟然会打折，\n',
            '不愧是柏斯超市啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我、我也不该因为\n',
            '开店迟了就惶惶不安的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5197(): pass

    label('loc_5197')

    Jump('loc_5436')

    def _loc_519A(): pass

    label('loc_519A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_526B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 2, 0x12)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5224',
    )

    ChrTalk(
        0x00FE,
        (
            '由于出现了些问题，\n',
            '商品还没到达……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我的店开张营业\n',
            '也要大幅延期了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说现在这状况\n',
            '也顾不上这种事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0012)

    Jump('loc_5268')

    def _loc_5224(): pass

    label('loc_5224')

    ChrTalk(
        0x00FE,
        (
            '今天超市里也\n',
            '没什么活力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也是这样，\n',
            '大家都很不安呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5268(): pass

    label('loc_5268')

    Jump('loc_5436')

    def _loc_526B(): pass

    label('loc_526B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_5353',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 2, 0x12)),
            Expr.Return,
        ),
        'loc_52C4',
    )

    ChrTalk(
        0x00FE,
        (
            '看来古代龙\n',
            '也已经离开了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样我也可以放下心来\n',
            '准备开店了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5350')

    def _loc_52C4(): pass

    label('loc_52C4')

    ChrTalk(
        0x00FE,
        (
            '看来古代龙\n',
            '好像到别的地方去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样我也可以放下心来\n',
            '准备开店了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然估计离开张还要一段时间，\n',
            '不过，到时候还请多关照哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0012)

    def _loc_5350(): pass

    label('loc_5350')

    Jump('loc_5436')

    def _loc_5353(): pass

    label('loc_5353')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_5436',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 2, 0x12)),
            Expr.Return,
        ),
        'loc_53BE',
    )

    ChrTalk(
        0x00FE,
        (
            '提交给超市的开店申请\n',
            '终于被受理了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '店预计就开在这附近，\n',
            '小店开张时还请多关照！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5436')

    def _loc_53BE(): pass

    label('loc_53BE')

    ChrTalk(
        0x00FE,
        (
            '给超市的开店请求\n',
            '终于被受理了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这就是我作为\n',
            '商人的第一步。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要不输给任何竞争对手，\n',
            '开一个出色的店铺。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0012)

    def _loc_5436(): pass

    label('loc_5436')

    TalkEnd(0x0018)

    Return()

# id: 0x001D offset: 0x543A
@scena.Code('func_1D_543A')
def func_1D_543A():
    TalkBegin(0x0019)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_548C',
    )

    ChrTalk(
        0x00FE,
        (
            '唉，人太多，\n',
            '都不知道该问谁……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊，那女孩到底\n',
            '住在哪里呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_548C(): pass

    label('loc_548C')

    TalkEnd(0x0019)

    Return()

# id: 0x001E offset: 0x5490
@scena.Code('func_1E_5490')
def func_1E_5490():
    TalkBegin(0x001A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_5571',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 3, 0x13)),
            Expr.Return,
        ),
        'loc_54F4',
    )

    ChrTalk(
        0x00FE,
        (
            '正在为新客人\n',
            '做超市的向导。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '两人都是帝国的商人呢。\n',
            '是很大方的顾客哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_556E')

    def _loc_54F4(): pass

    label('loc_54F4')

    ChrTalk(
        0x00FE,
        (
            '正在为新客人\n',
            '做超市的向导。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '两人都是帝国的商人呢。\n',
            '是很大方的顾客哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今后和帝国的客人\n',
            '交流也会增加吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0013)

    def _loc_556E(): pass

    label('loc_556E')

    Jump('loc_5619')

    def _loc_5571(): pass

    label('loc_5571')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_5619',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 3, 0x13)),
            Expr.Return,
        ),
        'loc_55CA',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，要确认库存的\n',
            '不是衣料品吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '工、工作太多\n',
            '总是容易搞错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5619')

    def _loc_55CA(): pass

    label('loc_55CA')

    ChrTalk(
        0x00FE,
        (
            '嗯～接着是确认\n',
            '绒毯的库存啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '老样子…～\n',
            '米拉诺还是那么爱使唤人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0013)

    def _loc_5619(): pass

    label('loc_5619')

    TalkEnd(0x001A)

    Return()

# id: 0x001F offset: 0x561D
@scena.Code('func_1F_561D')
def func_1F_561D():
    TalkBegin(0x001B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_5700',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 4, 0x14)),
            Expr.Return,
        ),
        'loc_5672',
    )

    ChrTalk(
        0x001B,
        (
            '本来是来商谈的，\n',
            '结果正赶上开始大减价。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '只好暂时等一下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5700')

    def _loc_5672(): pass

    label('loc_5672')

    ChrTalk(
        0x001B,
        (
            '听说超市已经修复好了，\n',
            '就立刻赶来进行商谈……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '结果时机却不太好，\n',
            '正赶上开始大减价。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '一旦有便宜可以捡，婆婆就\n',
            '说什么也不肯回家的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0014)

    def _loc_5700(): pass

    label('loc_5700')

    TalkEnd(0x001B)

    Return()

# id: 0x0020 offset: 0x5704
@scena.Code('func_20_5704')
def func_20_5704():
    TalkBegin(0x001C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_5787',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 5, 0x15)),
            Expr.Return,
        ),
        'loc_5751',
    )

    ChrTalk(
        0x00FE,
        (
            '今天是来爸爸的店里\n',
            '帮忙的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，我会加油的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5787')

    def _loc_5751(): pass

    label('loc_5751')

    ChrTalk(
        0x00FE,
        (
            '欢迎光临！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天是来爸爸的店里\n',
            '帮忙的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0015)

    def _loc_5787(): pass

    label('loc_5787')

    TalkEnd(0x001C)

    Return()

# id: 0x0021 offset: 0x578B
@scena.Code('func_21_578B')
def func_21_578B():
    TalkBegin(0x001D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_5890',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 6, 0x16)),
            Expr.Return,
        ),
        'loc_57DD',
    )

    ChrTalk(
        0x00FE,
        (
            '最后终于\n',
            '找到了签约对象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀呀，总算\n',
            '保住了面子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5890')

    def _loc_57DD(): pass

    label('loc_57DD')

    ChrTalk(
        0x00FE,
        (
            '在快绝望的时候\n',
            '有位商人来找我谈合作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总算在最后关头\n',
            '找到了签约对象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，在这种不明朗的形势下\n',
            '还这么勇敢的推进交易……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '米拉诺这个商人。\n',
            '还真是镇定啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0016)

    def _loc_5890(): pass

    label('loc_5890')

    TalkEnd(0x001D)

    Return()

# id: 0x0022 offset: 0x5894
@scena.Code('func_22_5894')
def func_22_5894():
    TalkBegin(0x001E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_59B3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 7, 0x17)),
            Expr.Return,
        ),
        'loc_5904',
    )

    ChrTalk(
        0x00FE,
        (
            '呀，真是热闹啊。\n',
            '真难以想象这是小国的市场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来可以作为相当不错的\n',
            '出口地市场哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_59B3')

    def _loc_5904(): pass

    label('loc_5904')

    ChrTalk(
        0x00FE,
        (
            '唔～这就是\n',
            '柏斯超市啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呀，真是热闹啊。\n',
            '真难以想象这是小国的市场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们帝国的产品\n',
            '似乎也销售得很多啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔唔，孤陋寡闻了啊。\n',
            '看来作为出口地相当不错呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0017)

    def _loc_59B3(): pass

    label('loc_59B3')

    TalkEnd(0x001E)

    Return()

# id: 0x0023 offset: 0x59B7
@scena.Code('func_23_59B7')
def func_23_59B7():
    TalkBegin(0x001F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_5AA7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 0, 0x18)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5A56',
    )

    ChrTalk(
        0x00FE,
        (
            '为了修理收银机\n',
            '去了南街区的工房……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是据店主说\n',
            '这好像不是故障。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '似乎今天上门询问故障的客人太多，\n',
            '店主很疲劳的样子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0018)

    Jump('loc_5AA4')

    def _loc_5A56(): pass

    label('loc_5A56')

    ChrTalk(
        0x00FE,
        (
            '我们的收银机\n',
            '好像不是坏了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔～不能动的话，\n',
            '那和故障就没区别了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5AA4(): pass

    label('loc_5AA4')

    Jump('loc_5B71')

    def _loc_5AA7(): pass

    label('loc_5AA7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_5B71',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 0, 0x18)),
            Expr.Return,
        ),
        'loc_5AEF',
    )

    ChrTalk(
        0x00FE,
        (
            '暂时留在柏斯\n',
            '帮忙店里干活吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好、加油啰～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5B71')

    def _loc_5AEF(): pass

    label('loc_5AEF')

    ChrTalk(
        0x00FE,
        (
            '呀，欢迎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '暂时留在柏斯\n',
            '帮忙店里干活吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到现在为止一直\n',
            '给妻子和波波添麻烦嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '多少也要\n',
            '补偿他们一些才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0018)

    def _loc_5B71(): pass

    label('loc_5B71')

    TalkEnd(0x001F)

    Return()

# id: 0x0024 offset: 0x5B75
@scena.Code('func_24_5B75')
def func_24_5B75():
    TalkBegin(0x0020)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 0, 0x2090)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_60AD',
    )

    ChrTurnDirection(0x0020, 0x0101, 400)

    ChrTalk(
        0x0020,
        (
            '#0360350284V#613F呀、艾丝蒂尔，\n',
            '还有约修亚也来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350285V#1000F你好、梅贝尔市长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350286V#1040F……好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0020, 0x0102, 400)

    ChrTalk(
        0x0020,
        (
            '#0360350287V#611F呵呵，真的是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360350288V看起来还是\n',
            '那么忙碌呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350289V#1016F市长也\n',
            '很辛苦的样子嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010350290V我听卢格兰爷爷说了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350291V#1035F好象这里也有市民\n',
            '冲进来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#0360350292V#615F嗯嗯，一直说服到半夜\n',
            '才总算让他们回去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360350293V#612F不过，这样并不能\n',
            '消除市民的不安。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360350294V这个状况长久持续下去的话\n',
            '恐怕还会引起骚乱的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350295V#1043F的确是这样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020350296V因为结果还是\n',
            '什么也没能解决。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350297V#1006F不过，不管怎样\n',
            '只能做力所能及的事了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010350298V就算低头烦恼，\n',
            '导力器也不会动起来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5EC7',
    )

    ChrTalk(
        0x0106,
        (
            '#0050350299V#051F啊啊，说得对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050350300V不管结果怎样，\n',
            '我们都只能尽游击士的本分。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5FA4')

    def _loc_5EC7(): pass

    label('loc_5EC7')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5F36',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350301V#020F嗯嗯，说得对呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030350302V无论结果如何，\n',
            '我们都只能尽游击士的本分。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5FA4')

    def _loc_5F36(): pass

    label('loc_5F36')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5FA4',
    )

    ChrTalk(
        0x0108,
        (
            '#0080350303V#070F噢，你说得对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080350304V尽人事听天命……\n',
            '我们就尽游击士的本分就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5FA4(): pass

    label('loc_5FA4')

    ChrTurnDirection(0x0020, 0x0101, 400)

    ChrTalk(
        0x0020,
        (
            '#0360350305V#610F呵呵，我也有同感。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360350306V无论状况如何\n',
            '保护城市是市长的职责……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360350307V当然，我相信各位\n',
            '最后终能解决问题的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350308V#1008F啊，啊哈哈……\n',
            '这可是责任重大哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350309V#1049F我就当是\n',
            '鼓励的话记下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0019)
    OP_A2(0x2090)

    Jump('loc_61F7')

    def _loc_60AD(): pass

    label('loc_60AD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 1, 0x19)),
            Expr.Return,
        ),
        'loc_6131',
    )

    ChrTalk(
        0x0020,
        (
            '#0360350310V#610F现在只有各自\n',
            '尽力而为了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360350341V当这些努力积累在一起，\n',
            '我相信一定能够成为\n',
            '渡过危机的力量。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_61F7')

    def _loc_6131(): pass

    label('loc_6131')

    ChrTalk(
        0x0020,
        (
            '#0360350342V#610F超市似乎也\n',
            '恢复平静了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360350343V把物价安定下来\n',
            '果然还是很重要的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360350344V年轻的商人们\n',
            '也花了很多心思……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360350345V#611F呵呵，按现在状况的话\n',
            '应该可以稍微放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_61F7(): pass

    label('loc_61F7')

    TalkEnd(0x0020)

    Return()

# id: 0x0025 offset: 0x61FB
@scena.Code('func_25_61FB')
def func_25_61FB():
    If(
        (
            (Expr.PushValueByIndex, 0x13),
            (Expr.PushLong, 0x381),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6208',
    )

    Return()

    def _loc_6208(): pass

    label('loc_6208')

    If(
        (
            (Expr.Eval, "OP_29(0x0079, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0079, 0x00, 0x40)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_621A',
    )

    Return()

    def _loc_621A(): pass

    label('loc_621A')

    SetMapFlags(0x00000080)
    OP_C0(0x01, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    Sleep(30)

    If(
        (
            (Expr.Eval, "OP_CD(0x0010)"),
            Expr.Return,
        ),
        'loc_6255',
    )

    Call(0, 0x0026)

    Jump('loc_633B')

    def _loc_6255(): pass

    label('loc_6255')

    If(
        (
            (Expr.Eval, "OP_CD(0x000C)"),
            Expr.Return,
        ),
        'loc_6264',
    )

    Call(0, 0x0027)

    Jump('loc_633B')

    def _loc_6264(): pass

    label('loc_6264')

    If(
        (
            (Expr.Eval, "OP_CD(0x0009)"),
            Expr.Return,
        ),
        'loc_6273',
    )

    Call(0, 0x0028)

    Jump('loc_633B')

    def _loc_6273(): pass

    label('loc_6273')

    If(
        (
            (Expr.Eval, "OP_CD(0x0008)"),
            Expr.Return,
        ),
        'loc_6282',
    )

    Call(0, 0x0029)

    Jump('loc_633B')

    def _loc_6282(): pass

    label('loc_6282')

    If(
        (
            (Expr.Eval, "OP_CD(0x03E8)"),
            Expr.Return,
        ),
        'loc_6291',
    )

    Call(0, 0x0028)

    Jump('loc_633B')

    def _loc_6291(): pass

    label('loc_6291')

    If(
        (
            (Expr.Eval, "OP_CD(0x03E9)"),
            Expr.Return,
        ),
        'loc_62A0',
    )

    Call(0, 0x0027)

    Jump('loc_633B')

    def _loc_62A0(): pass

    label('loc_62A0')

    If(
        (
            (Expr.Eval, "OP_CD(0x00FF)"),
            (Expr.Eval, "OP_CD(0x04E7)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_62FD',
    )

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '试着出示了照片，\n',
            '但似乎没有见过的印象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    Jump('loc_633B')

    def _loc_62FD(): pass

    label('loc_62FD')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '附近没有人可以确认照片。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    def _loc_633B(): pass

    label('loc_633B')

    OP_0D()
    ClearMapFlags(0x00000080)

    Return()

# id: 0x0026 offset: 0x6342
@scena.Code('func_26_6342')
def func_26_6342():
    TalkBegin(0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_63B5',
    )

    ChrTalk(
        0x0010,
        (
            '#3790490564V你们要努力\n',
            '找到那个孩子啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#3790490565V因为战争而失散，\n',
            '可以说是最可怜的事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_648C')

    def _loc_63B5(): pass

    label('loc_63B5')

    ChrTalk(
        0x0010,
        (
            '#3790490559V怎么，找人吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#3790490560V……原来如此。\n',
            '１０年前的事了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#3790490561V很遗憾，我没印象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#3790490562V不过，要加油啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#3790490563V因为战争而失散，\n',
            '可以说是最可怜的事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000A)

    def _loc_648C(): pass

    label('loc_648C')

    TalkEnd(0x0010)

    Return()

# id: 0x0027 offset: 0x6490
@scena.Code('func_27_6490')
def func_27_6490():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_64E6',
    )

    ChrTalk(
        0x000C,
        (
            '#1360490570V很遗憾…\n',
            '我没有印象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1360490571V请去问问别人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_658E')

    def _loc_64E6(): pass

    label('loc_64E6')

    ChrTalk(
        0x000C,
        (
            '#1360490566V噢，找人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1360490567V嗯…\n',
            '原来如此原来如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1360490568V唔～很遗憾…\n',
            '我没印象呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1360490569V抱歉帮不上忙。\n',
            '请去问问别人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    def _loc_658E(): pass

    label('loc_658E')

    TalkEnd(0x000C)

    Return()

# id: 0x0028 offset: 0x6592
@scena.Code('func_28_6592')
def func_28_6592():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_65FB',
    )

    ChrTalk(
        0x0009,
        (
            '#1160490575V这照片里的女孩……\n',
            '感觉好像见过呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1160490576V嗯～不过到底\n',
            '是谁呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_668D')

    def _loc_65FB(): pass

    label('loc_65FB')

    ChrTalk(
        0x0009,
        (
            '#1160490572V咦、这照片里的女孩……\n',
            '感觉好像在哪儿见过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1160490573V嗯～不过可能只是有点像而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1160490574V抱歉，请别在意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_668D(): pass

    label('loc_668D')

    TalkEnd(0x0009)

    Return()

# id: 0x0029 offset: 0x6691
@scena.Code('func_29_6691')
def func_29_6691():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_670C',
    )

    ChrTalk(
        0x0008,
        (
            '#1150490578V绿色的眼睛\n',
            '那么清澈，真是漂亮呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1150490579V附近要是有这样的孩子\n',
            '我绝对不会放过的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_67A3')

    def _loc_670C(): pass

    label('loc_670C')

    ChrTalk(
        0x0008,
        (
            '#1150490577V哇，好可爱的女孩啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1150490578V绿色的眼睛\n',
            '那么清澈，真是漂亮呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1150490579V附近要是有这样的孩子\n',
            '我绝对不会放过的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_67A3(): pass

    label('loc_67A3')

    TalkEnd(0x0008)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

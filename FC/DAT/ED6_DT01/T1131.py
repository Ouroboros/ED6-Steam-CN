import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T1131_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1131   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '梅贝尔'),
    TXT(0x02, '维尔纳'),
    TXT(0x03, '普拉达'),
    TXT(0x04, '科梅尔斯'),
    TXT(0x05, '琉肯'),
    TXT(0x06, '西蒙'),
    TXT(0x07, '奈尔'),
    TXT(0x08, '雷克多主管'),
    TXT(0x09, '罗宋厨师长'),
    TXT(0x0A, '格露娜'),
    TXT(0x0B, '斯托隆'),
    TXT(0x0C, '莉诺'),
    TXT(0x0D, '玛丽安'),
    TXT(0x0E, '诺琪'),
    TXT(0x0F, '赫雷思老人'),
    TXT(0x10, '阿尔妲婆婆'),
    TXT(0x11, '卡洛塔'),
    TXT(0x12, '沙库'),
    TXT(0x13, '雷塔'),
    TXT(0x14, '法娜'),
    TXT(0x15, '甜点'),
    TXT(0x16, '甜点'),
    TXT(0x17, '汤碗'),
    TXT(0x18, '勺子'),
    TXT(0x19, '叉子'),
    TXT(0x1A, '叉子'),
    TXT(0x1B, '刀子'),
    TXT(0x1C, '刀子'),
    TXT(0x1D, '料理'),
    TXT(0x1E, '酒'),
    TXT(0x1F, '茶壶'),
    TXT(0x20, '茶壶'),
    TXT(0x21, '茶壶'),
    TXT(0x22, '瓶子'),
    TXT(0x23, '酒杯'),
    TXT(0x24, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1131.x'
    header.mapIndex       = 1
    header.bgm            = 11
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/T1131._SN', 'ED6_DT01/T1131_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x972A
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
        ('ED6_DT07/CH02363._CH', 'ED6_DT07/CH02363P._CP'),
        ('ED6_DT07/CH01270._CH', 'ED6_DT07/CH01270P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH01043._CH', 'ED6_DT07/CH01043P._CP'),
        ('ED6_DT07/CH01660._CH', 'ED6_DT07/CH01660P._CP'),
        ('ED6_DT07/CH01143._CH', 'ED6_DT07/CH01143P._CP'),
        ('ED6_DT06/CH20086._CH', 'ED6_DT06/CH20086P._CP'),
        ('ED6_DT07/CH01560._CH', 'ED6_DT07/CH01560P._CP'),
        ('ED6_DT07/CH01280._CH', 'ED6_DT07/CH01280P._CP'),
        ('ED6_DT07/CH02480._CH', 'ED6_DT07/CH02480P._CP'),
        ('ED6_DT07/CH01570._CH', 'ED6_DT07/CH01570P._CP'),
        ('ED6_DT07/CH02540._CH', 'ED6_DT07/CH02540P._CP'),
        ('ED6_DT07/CH01213._CH', 'ED6_DT07/CH01213P._CP'),
        ('ED6_DT07/CH01233._CH', 'ED6_DT07/CH01233P._CP'),
        ('ED6_DT07/CH01003._CH', 'ED6_DT07/CH01003P._CP'),
        ('ED6_DT07/CH01183._CH', 'ED6_DT07/CH01183P._CP'),
        ('ED6_DT07/CH01023._CH', 'ED6_DT07/CH01023P._CP'),
        ('ED6_DT07/CH01123._CH', 'ED6_DT07/CH01123P._CP'),
        ('ED6_DT07/CH01043._CH', 'ED6_DT07/CH01043P._CP'),
        ('ED6_DT07/CH01053._CH', 'ED6_DT07/CH01053P._CP'),
        ('ED6_DT07/CH00003._CH', 'ED6_DT07/CH00003P._CP'),
        ('ED6_DT07/CH00013._CH', 'ED6_DT07/CH00013P._CP'),
        ('ED6_DT07/CH00023._CH', 'ED6_DT07/CH00023P._CP'),
        ('ED6_DT07/CH02060._CH', 'ED6_DT07/CH02060P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
        ('ED6_DT06/CH20020._CH', 'ED6_DT06/CH20020P._CP'),
    ]

# id: 0x10002 offset: 0x17A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -620,
            z                   = -1000,
            y                   = -3500,
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
            x                   = 2970,
            z                   = 0,
            y                   = 3650,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = 1400,
            z                   = 0,
            y                   = 1500,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = -6030,
            z                   = 3350,
            y                   = 5100,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0155,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = 5480,
            z                   = 0,
            y                   = 1480,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = -1450,
            z                   = 3250,
            y                   = 3420,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = -7300,
            z                   = 1400,
            y                   = -4100,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 196614,
            chipIndex           = 6,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            x                   = -42600,
            z                   = 0,
            y                   = 1700,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            x                   = -35500,
            z                   = 0,
            y                   = 46700,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            x                   = -47450,
            z                   = 0,
            y                   = 44160,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = -38500,
            z                   = 1500,
            y                   = 14200,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            x                   = -53300,
            z                   = 1500,
            y                   = 200,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            x                   = -52950,
            z                   = 1600,
            y                   = 11400,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0154,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            x                   = -52950,
            z                   = 1600,
            y                   = 8600,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0154,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            x                   = -45600,
            z                   = 1600,
            y                   = 11000,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0154,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            x                   = -36400,
            z                   = 1600,
            y                   = -1000,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0154,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0016,
        ),
        ScenaNpcData(
            x                   = -39120,
            z                   = 1600,
            y                   = 7410,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0154,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0017,
        ),
        ScenaNpcData(
            x                   = -39130,
            z                   = 1600,
            y                   = 4590,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0154,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0018,
        ),
        ScenaNpcData(
            x                   = -42400,
            z                   = 1600,
            y                   = 11000,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0154,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0019,
        ),
        ScenaNpcData(
            x                   = -39600,
            z                   = 1600,
            y                   = 11000,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0154,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001A,
        ),
        ScenaNpcData(
            x                   = -52960,
            z                   = 2230,
            y                   = 9560,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 589849,
            chipIndex           = 25,
            npcIndex            = 0x0146,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -52940,
            z                   = 2230,
            y                   = 10400,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 589849,
            chipIndex           = 25,
            npcIndex            = 0x0146,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -35500,
            z                   = 2150,
            y                   = -1060,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 196633,
            chipIndex           = 25,
            npcIndex            = 0x0146,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -35750,
            z                   = 2150,
            y                   = -1000,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1114137,
            chipIndex           = 25,
            npcIndex            = 0x0146,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -35670,
            z                   = 2150,
            y                   = -950,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1376281,
            chipIndex           = 25,
            npcIndex            = 0x0146,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -35670,
            z                   = 2150,
            y                   = -830,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1376281,
            chipIndex           = 25,
            npcIndex            = 0x0146,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -35550,
            z                   = 2150,
            y                   = -1350,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1441817,
            chipIndex           = 25,
            npcIndex            = 0x0146,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -35550,
            z                   = 2150,
            y                   = -1490,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1441817,
            chipIndex           = 25,
            npcIndex            = 0x0146,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -46510,
            z                   = 2230,
            y                   = 10750,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 393241,
            chipIndex           = 25,
            npcIndex            = 0x0146,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -46750,
            z                   = 2230,
            y                   = 11300,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 327704,
            chipIndex           = 24,
            npcIndex            = 0x0146,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -39030,
            z                   = 2200,
            y                   = 6000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1703961,
            chipIndex           = 25,
            npcIndex            = 0x0146,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -39030,
            z                   = 2200,
            y                   = 6500,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1638425,
            chipIndex           = 25,
            npcIndex            = 0x0146,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -39030,
            z                   = 2200,
            y                   = 5300,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1638425,
            chipIndex           = 25,
            npcIndex            = 0x0146,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -6490,
            z                   = 2100,
            y                   = -3560,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1835033,
            chipIndex           = 25,
            npcIndex            = 0x01C6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -6360,
            z                   = 2100,
            y                   = -4420,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 65560,
            chipIndex           = 24,
            npcIndex            = 0x01C6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x5DA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x5DA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x5DA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 3050,
            triggerZ            = 0,
            triggerY            = 1520,
            triggerRange        = 400,
            actorX              = 2970,
            actorZ              = 1500,
            actorY              = 3650,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x5FE
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_60C',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x001B)

    def _loc_60C(): pass

    label('loc_60C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_62F',
    )

    SetChrFlags(0x001A, 0x0080)
    SetChrFlags(0x001A, 0x0008)
    SetChrFlags(0x001B, 0x0080)
    SetChrFlags(0x001B, 0x0008)
    SetChrFlags(0x000B, 0x0080)

    Jump('loc_6DA')

    def _loc_62F(): pass

    label('loc_62F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_64D',
    )

    SetChrFlags(0x001A, 0x0080)
    SetChrFlags(0x001A, 0x0008)
    SetChrFlags(0x001B, 0x0080)
    SetChrFlags(0x001B, 0x0008)

    Jump('loc_6DA')

    def _loc_64D(): pass

    label('loc_64D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_66B',
    )

    SetChrFlags(0x001A, 0x0080)
    SetChrFlags(0x001A, 0x0008)
    SetChrFlags(0x001B, 0x0080)
    SetChrFlags(0x001B, 0x0008)

    Jump('loc_6DA')

    def _loc_66B(): pass

    label('loc_66B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_675',
    )

    Jump('loc_6DA')

    def _loc_675(): pass

    label('loc_675')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 7, 0x317)),
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 5, 0x315)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_697',
    )

    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x0029, 0x0080)
    ClearChrFlags(0x002A, 0x0080)

    Jump('loc_6DA')

    def _loc_697(): pass

    label('loc_697')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 6, 0x316)),
            Expr.Return,
        ),
        'loc_6AB',
    )

    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)

    Jump('loc_6DA')

    def _loc_6AB(): pass

    label('loc_6AB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_6BA',
    )

    ClearChrFlags(0x000D, 0x0080)

    Jump('loc_6DA')

    def _loc_6BA(): pass

    label('loc_6BA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_6C9',
    )

    ClearChrFlags(0x000D, 0x0080)

    Jump('loc_6DA')

    def _loc_6C9(): pass

    label('loc_6C9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_6DA',
    )

    ClearChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000B, 0x0010)

    def _loc_6DA(): pass

    label('loc_6DA')

    Return()

# id: 0x0001 offset: 0x6DB
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0x6DC
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_6F1',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_6F1(): pass

    label('loc_6F1')

    Return()

# id: 0x0003 offset: 0x6F2
@scena.Code('func_03_6F2')
def func_03_6F2():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_715',
    )

    OP_8D(0x00FE, 1450, 3690, 4800, 3990, 1000)

    Jump('func_03_6F2')

    def _loc_715(): pass

    label('loc_715')

    Return()

# id: 0x0004 offset: 0x716
@scena.Code('func_04_716')
def func_04_716():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_855',
    )

    def _loc_721(): pass

    label('loc_721')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_852',
    )

    Sleep(2000)

    ChrWalkTo(0x00FE, -2100, 0, -1200, 2000, 0x00)
    ChrWalkTo(0x00FE, -4100, 1500, -1100, 1000, 0x00)
    ChrWalkTo(0x00FE, -6000, 1500, -2700, 2000, 0x00)
    SetChrDirection(0x00FE, 180, 200)
    Sleep(5000)

    ChrWalkTo(0x00FE, -7300, 1500, -100, 2000, 0x00)
    ChrWalkTo(0x00FE, -7300, 3250, 2100, 1000, 0x00)
    ChrWalkTo(0x00FE, -5000, 3250, 4100, 2000, 0x00)
    SetChrDirection(0x00FE, 0, 200)
    Sleep(5000)

    ChrWalkTo(0x00FE, -6600, 3250, 2200, 2000, 0x00)
    ChrWalkTo(0x00FE, -6600, 1500, 0, 1000, 0x00)
    ChrWalkTo(0x00FE, -6000, 1500, -2700, 2000, 0x00)
    SetChrDirection(0x00FE, 180, 200)
    Sleep(5000)

    ChrWalkTo(0x00FE, -4100, 1500, -1100, 2000, 0x00)
    ChrWalkTo(0x00FE, -2100, 0, -1200, 1000, 0x00)
    ChrWalkTo(0x00FE, 1400, 0, 1500, 2000, 0x00)
    SetChrDirection(0x00FE, 0, 200)
    Sleep(5000)

    Jump('loc_721')

    def _loc_852(): pass

    label('loc_852')

    Jump('loc_C52')

    def _loc_855(): pass

    label('loc_855')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 7, 0x317)),
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 5, 0x315)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_944',
    )

    def _loc_860(): pass

    label('loc_860')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_941',
    )

    Sleep(2000)

    ChrWalkTo(0x00FE, -1400, 0, 1200, 2000, 0x00)
    ChrWalkTo(0x00FE, -1400, 0, 3500, 2000, 0x00)
    ChrWalkTo(0x00FE, 350, 0, 4400, 2000, 0x00)
    SetChrDirection(0x00FE, 0, 200)
    Sleep(5000)

    ChrWalkTo(0x00FE, 1100, 0, 4400, 2000, 0x00)
    SetChrDirection(0x00FE, 45, 200)
    Sleep(5000)

    ChrWalkTo(0x00FE, -1100, 0, 4400, 2000, 0x00)
    SetChrDirection(0x00FE, 0, 200)
    Sleep(5000)

    ChrWalkTo(0x00FE, -1400, 0, 3500, 2000, 0x00)
    ChrWalkTo(0x00FE, -1400, 0, 1200, 2000, 0x00)
    ChrWalkTo(0x00FE, 1400, 0, 1500, 2000, 0x00)
    SetChrDirection(0x00FE, 0, 200)
    Sleep(5000)

    Jump('loc_860')

    def _loc_941(): pass

    label('loc_941')

    Jump('loc_C52')

    def _loc_944(): pass

    label('loc_944')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_A7F',
    )

    def _loc_94B(): pass

    label('loc_94B')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_A7C',
    )

    Sleep(2000)

    ChrWalkTo(0x00FE, -2100, 0, -1200, 2000, 0x00)
    ChrWalkTo(0x00FE, -4100, 1500, -1100, 1000, 0x00)
    ChrWalkTo(0x00FE, -6000, 1500, -2700, 2000, 0x00)
    SetChrDirection(0x00FE, 180, 200)
    Sleep(5000)

    ChrWalkTo(0x00FE, -7300, 1500, -100, 2000, 0x00)
    ChrWalkTo(0x00FE, -7300, 3250, 2100, 1000, 0x00)
    ChrWalkTo(0x00FE, -5000, 3250, 4100, 2000, 0x00)
    SetChrDirection(0x00FE, 0, 200)
    Sleep(5000)

    ChrWalkTo(0x00FE, -6600, 3250, 2200, 2000, 0x00)
    ChrWalkTo(0x00FE, -6600, 1500, 0, 1000, 0x00)
    ChrWalkTo(0x00FE, -6000, 1500, -2700, 2000, 0x00)
    SetChrDirection(0x00FE, 180, 200)
    Sleep(5000)

    ChrWalkTo(0x00FE, -4100, 1500, -1100, 2000, 0x00)
    ChrWalkTo(0x00FE, -2100, 0, -1200, 1000, 0x00)
    ChrWalkTo(0x00FE, 1400, 0, 1500, 2000, 0x00)
    SetChrDirection(0x00FE, 0, 200)
    Sleep(5000)

    Jump('loc_94B')

    def _loc_A7C(): pass

    label('loc_A7C')

    Jump('loc_C52')

    def _loc_A7F(): pass

    label('loc_A7F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_B6A',
    )

    def _loc_A86(): pass

    label('loc_A86')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_B67',
    )

    Sleep(2000)

    ChrWalkTo(0x00FE, -1400, 0, 1200, 2000, 0x00)
    ChrWalkTo(0x00FE, -1400, 0, 3500, 2000, 0x00)
    ChrWalkTo(0x00FE, 350, 0, 4400, 2000, 0x00)
    SetChrDirection(0x00FE, 0, 200)
    Sleep(5000)

    ChrWalkTo(0x00FE, 1100, 0, 4400, 2000, 0x00)
    SetChrDirection(0x00FE, 45, 200)
    Sleep(5000)

    ChrWalkTo(0x00FE, -1100, 0, 4400, 2000, 0x00)
    SetChrDirection(0x00FE, 0, 200)
    Sleep(5000)

    ChrWalkTo(0x00FE, -1400, 0, 3500, 2000, 0x00)
    ChrWalkTo(0x00FE, -1400, 0, 1200, 2000, 0x00)
    ChrWalkTo(0x00FE, 1400, 0, 1500, 2000, 0x00)
    SetChrDirection(0x00FE, 0, 200)
    Sleep(5000)

    Jump('loc_A86')

    def _loc_B67(): pass

    label('loc_B67')

    Jump('loc_C52')

    def _loc_B6A(): pass

    label('loc_B6A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_C52',
    )

    def _loc_B71(): pass

    label('loc_B71')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_C52',
    )

    Sleep(2000)

    ChrWalkTo(0x00FE, -1400, 0, 1200, 2000, 0x00)
    ChrWalkTo(0x00FE, -1400, 0, 3500, 2000, 0x00)
    ChrWalkTo(0x00FE, 350, 0, 4400, 2000, 0x00)
    SetChrDirection(0x00FE, 0, 200)
    Sleep(5000)

    ChrWalkTo(0x00FE, 1100, 0, 4400, 2000, 0x00)
    SetChrDirection(0x00FE, 45, 200)
    Sleep(5000)

    ChrWalkTo(0x00FE, -1100, 0, 4400, 2000, 0x00)
    SetChrDirection(0x00FE, 0, 200)
    Sleep(5000)

    ChrWalkTo(0x00FE, -1400, 0, 3500, 2000, 0x00)
    ChrWalkTo(0x00FE, -1400, 0, 1200, 2000, 0x00)
    ChrWalkTo(0x00FE, 1400, 0, 1500, 2000, 0x00)
    SetChrDirection(0x00FE, 0, 200)
    Sleep(5000)

    Jump('loc_B71')

    def _loc_C52(): pass

    label('loc_C52')

    Return()

# id: 0x0005 offset: 0xC53
@scena.Code('func_05_C53')
def func_05_C53():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_C76',
    )

    OP_8D(0x00FE, -48200, 42570, -46450, 46500, 1000)

    Jump('func_05_C53')

    def _loc_C76(): pass

    label('loc_C76')

    Return()

# id: 0x0006 offset: 0xC77
@scena.Code('func_06_C77')
def func_06_C77():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_EFB',
    )

    ChrWalkTo(0x00FE, -51700, 1500, 3300, 2000, 0x00)
    ChrWalkTo(0x00FE, -51700, 1500, 4000, 2000, 0x00)
    ChrWalkTo(0x00FE, -51700, 1500, 8700, 2000, 0x00)
    SetChrDirection(0x00FE, 315, 200)
    Sleep(5000)

    ChrWalkTo(0x00FE, -44200, 1500, 9600, 2000, 0x00)
    ChrWalkTo(0x00FE, -44200, 1500, 12000, 2000, 0x00)
    ChrWalkTo(0x00FE, -45800, 1500, 12000, 2000, 0x00)
    SetChrDirection(0x00FE, 225, 200)
    Sleep(5000)

    ChrWalkTo(0x00FE, -45700, 1500, 12700, 2000, 0x00)
    ChrWalkTo(0x00FE, -41000, 1500, 12700, 2000, 0x00)
    SetChrDirection(0x00FE, 180, 200)
    Sleep(5000)

    ChrWalkTo(0x00FE, -34900, 1500, 12500, 2000, 0x00)
    ChrWalkTo(0x00FE, -34900, 1500, 11900, 2000, 0x00)
    SetChrDirection(0x00FE, 180, 200)
    Sleep(5000)

    ChrWalkTo(0x00FE, -34900, 1500, 12500, 2000, 0x00)
    ChrWalkTo(0x00FE, -32600, 1500, 12500, 2000, 0x00)
    ChrWalkTo(0x00FE, -32600, 1500, 8000, 2000, 0x00)
    ChrWalkTo(0x00FE, -37200, 1500, 4000, 2000, 0x00)
    ChrWalkTo(0x00FE, -37400, 1500, -1200, 2000, 0x00)
    ChrWalkTo(0x00FE, -36800, 1500, -2400, 2000, 0x00)
    ChrWalkTo(0x00FE, -36100, 1500, -2400, 2000, 0x00)
    ChrWalkTo(0x00FE, -35700, 1500, -2100, 2000, 0x00)
    SetChrDirection(0x00FE, 45, 200)
    Sleep(5000)

    ChrWalkTo(0x00FE, -35800, 1500, -2400, 2000, 0x00)
    ChrWalkTo(0x00FE, -32299, 1500, -2400, 2000, 0x00)
    ChrWalkTo(0x00FE, -32299, 1500, 400, 2000, 0x00)
    ChrWalkTo(0x00FE, -35000, 1500, 400, 2000, 0x00)
    ChrWalkTo(0x00FE, -36800, 1500, 2400, 2000, 0x00)
    ChrWalkTo(0x00FE, -36800, 1500, 8600, 2000, 0x00)
    ChrWalkTo(0x00FE, -50800, 1500, 8600, 2000, 0x00)
    ChrWalkTo(0x00FE, -51700, 1500, 7400, 2000, 0x00)
    ChrWalkTo(0x00FE, -51700, 1500, 2500, 2000, 0x00)
    ChrWalkTo(0x00FE, -53300, 1500, 200, 2000, 0x00)
    SetChrDirection(0x00FE, 180, 200)
    Sleep(5000)

    Jump('func_06_C77')

    def _loc_EFB(): pass

    label('loc_EFB')

    Return()

# id: 0x0007 offset: 0xEFC
@scena.Code('func_07_EFC')
def func_07_EFC():
    Call(0, 0x0008)

    Return()

# id: 0x0008 offset: 0xF01
@scena.Code('func_08_F01')
def func_08_F01():
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
            TXT(0x02, '欢迎品尝「仰天奶酪肉汁烩饭」300米拉\n'),
            TXT(0x03, '离开\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F83',
    )

    FadeIn(300, 0)
    OP_0D()
    OP_A9(0x1D)
    OP_56(0x00)
    TalkEnd(0x0009)

    Return()

    def _loc_F83(): pass

    label('loc_F83')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10B5',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x12),
            (Expr.PushLong, 0x12C),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_1080',
    )

    SubMira(300)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    PlaySE(11, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x0),
            '尝了尝',
            (TxtCtl.SetColor, 0x2),
            '仰天奶酪肉汁烩饭',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrStatus(0x0000, 0xFC, 0)
    SetChrStatus(0x0001, 0xFC, 0)
    SetChrStatus(0x0002, 0xFC, 0)
    SetChrStatus(0x0003, 0xFC, 0)
    SetChrStatus(0x0004, 0xFC, 0)
    SetChrStatus(0x0005, 0xFC, 0)
    SetChrStatus(0x0006, 0xFC, 0)
    SetChrStatus(0x0007, 0xFC, 0)
    SetChrStatus(0x0000, 0xFD, 150)
    SetChrStatus(0x0001, 0xFD, 150)
    SetChrStatus(0x0002, 0xFD, 150)
    SetChrStatus(0x0003, 0xFD, 150)
    SetChrStatus(0x0004, 0xFD, 150)
    SetChrStatus(0x0005, 0xFD, 150)
    SetChrStatus(0x0006, 0xFD, 150)
    SetChrStatus(0x0007, 0xFD, 150)

    If(
        (
            (Expr.Eval, "OP_40(0x020D)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1072',
    )

    If(
        (
            (Expr.Eval, "OP_AC(0x0005)"),
            Expr.Return,
        ),
        'loc_1044',
    )

    Jump('loc_1072')

    def _loc_1044(): pass

    label('loc_1044')

    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x0),
            '学会了',
            (TxtCtl.SetColor, 0x2),
            '仰天奶酪肉汁烩饭',
            (TxtCtl.SetColor, 0x0),
            '的做法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1072(): pass

    label('loc_1072')

    OP_56(0x00)
    FadeIn(1000, 0)

    Jump('loc_10A6')

    def _loc_1080(): pass

    label('loc_1080')

    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '没有足够的米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeIn(300, 0)
    def _loc_10A6(): pass

    label('loc_10A6')

    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x0009)

    Return()

    def _loc_10B5(): pass

    label('loc_10B5')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_10CF',
    )

    FadeIn(300, 0)
    TalkEnd(0x0009)

    Return()

    def _loc_10CF(): pass

    label('loc_10CF')

    FadeIn(300, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_11D0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1175',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '强盗事件原来是\n',
            '空贼团所犯下的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '不过最后，\n',
            '摩尔根将军率领的王国军队\n',
            '把他们一网打尽了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '好久都没有\n',
            '感到这么轻松愉快了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11CD')

    def _loc_1175(): pass

    label('loc_1175')

    ChrTalk(
        0x0009,
        (
            '摩尔根将军率领的王国军队\n',
            '把空贼们一网打尽了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '好久都没有\n',
            '感到这么轻松愉快了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11CD(): pass

    label('loc_11CD')

    Jump('loc_156E')

    def _loc_11D0(): pass

    label('loc_11D0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_1232',
    )

    ChrTalk(
        0x0009,
        (
            '最近，\n',
            '总是发生一些让人不安的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我们做百姓的只是希望\n',
            '能过上些安稳的日子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_156E')

    def _loc_1232(): pass

    label('loc_1232')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_12A8',
    )

    ChrTalk(
        0x0009,
        (
            '南街区的商店街\n',
            '好像都被强盗搞得一团乱了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '柏斯是一个聚财的地方，\n',
            '自古以来这样的事件就没有断绝过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_156E')

    def _loc_12A8(): pass

    label('loc_12A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_130B',
    )

    ChrTalk(
        0x0009,
        (
            '我开这家店与其说是做生意，\n',
            '不如说是凭兴趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '如果能让客人感到更放松一点就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_156E')

    def _loc_130B(): pass

    label('loc_130B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_13C9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1387',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '安特洛丝餐厅\n',
            '不是能让人久坐的地方吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '相反我们的店子\n',
            '可以为各位食客营造\n',
            '一个放松舒适的环境。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13C6')

    def _loc_1387(): pass

    label('loc_1387')

    ChrTalk(
        0x0009,
        (
            '宾至如归的酒馆……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '嗯，\n',
            '就以这个作为关键词来努力吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13C6(): pass

    label('loc_13C6')

    Jump('loc_156E')

    def _loc_13C9(): pass

    label('loc_13C9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_152E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_14C9',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '经常有客人把本店\n',
            '和安特洛丝餐厅相比。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我们和他们本来就不是一回事，\n',
            '没有拿来比的必要吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '便宜又方便地享受快餐\n',
            '是我们的宗旨。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '而安特洛丝餐厅则只提供\n',
            '有格调的高档料理和服务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '面向的客户群不同，\n',
            '也不会互相竞争吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_152B')

    def _loc_14C9(): pass

    label('loc_14C9')

    ChrTalk(
        0x0009,
        (
            '经常有客人把本店\n',
            '和安特洛丝餐厅相比。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我们和他们本来就不是一回事，\n',
            '没有拿来比的必要吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_152B(): pass

    label('loc_152B')

    Jump('loc_156E')

    def _loc_152E(): pass

    label('loc_152E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_156E',
    )

    ChrTalk(
        0x0009,
        (
            '您好，欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '本酒馆的饭菜\n',
            '又便宜又好吃哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_156E(): pass

    label('loc_156E')

    TalkEnd(0x0009)

    Return()

# id: 0x0009 offset: 0x1572
@scena.Code('func_09_1572')
def func_09_1572():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_15B6',
    )

    ChrTalk(
        0x00FE,
        (
            '工作工作～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要赶快把麻烦的事情\n',
            '全部处理掉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AB1')

    def _loc_15B6(): pass

    label('loc_15B6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_1704',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1688',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '城里还是有案件接连发生，\n',
            '不过我们店里却风平浪静。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这大概正如店长所说的，\n',
            '我们店里的气氛\n',
            '能让人感到轻松自如吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然觉得有些无聊……\n',
            '不过没和案件扯上关系，\n',
            '也算是一件好事吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1701')

    def _loc_1688(): pass

    label('loc_1688')

    ChrTalk(
        0x00FE,
        (
            '城里还是有案件接连发生，\n',
            '不过我们店里却风平浪静。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这大概正如店长所说的，\n',
            '我们店里的气氛\n',
            '能让人感到轻松自如吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1701(): pass

    label('loc_1701')

    Jump('loc_1AB1')

    def _loc_1704(): pass

    label('loc_1704')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_185C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_17D9',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '强盗果然是\n',
            '懂得选择场所下手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '南街区有许多\n',
            '大商店和商人住宅，\n',
            '但是那里晚上却很少有行人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '即使他们袭击我们这家店，\n',
            '估计也只能抢走些食材吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '连这个也偷的话那和老鼠有啥区别。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1859')

    def _loc_17D9(): pass

    label('loc_17D9')

    ChrTalk(
        0x00FE,
        (
            '强盗果然是\n',
            '懂得选择场所下手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '即使他们袭击我们这家店，\n',
            '估计也只能抢走些食材吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '连这个也偷的话那和老鼠有啥区别。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1859(): pass

    label('loc_1859')

    Jump('loc_1AB1')

    def _loc_185C(): pass

    label('loc_185C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_1902',
    )

    ChrTalk(
        0x00FE,
        (
            '店长经常一本正经地说\n',
            '这家店是按照他的品位开的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，传说那家安特洛丝餐厅\n',
            '也是老板根据自己的品位而经营的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '品位的等级还真是相差得很远呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AB1')

    def _loc_1902(): pass

    label('loc_1902')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_19E8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_199B',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '我们店里的客人\n',
            '好像大多都喜欢一直坐在这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是不是谈生意的人比较多的缘故呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里是个休闲的地方，\n',
            '能让人们心情舒畅。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19E5')

    def _loc_199B(): pass

    label('loc_199B')

    ChrTalk(
        0x00FE,
        (
            '喝醉酒说胡话的客人，\n',
            '或者其他奇怪的客人有不少，\n',
            '这也是这里的特征吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19E5(): pass

    label('loc_19E5')

    Jump('loc_1AB1')

    def _loc_19E8(): pass

    label('loc_19E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_1A80',
    )

    ChrTalk(
        0x00FE,
        (
            '经常有客人把本店\n',
            '有些客人总喜欢拿我们和那家作比较。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总是说这些也没什么用吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那边是有钱人去的地方。\n',
            '而我们这里则面向工薪阶层。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AB1')

    def _loc_1A80(): pass

    label('loc_1A80')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_1AB1',
    )

    ChrTalk(
        0x00FE,
        (
            '欢迎光临～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请到空位上入座吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AB1(): pass

    label('loc_1AB1')

    TalkEnd(0x000A)

    Return()

# id: 0x000A offset: 0x1AB5
@scena.Code('func_0A_1AB5')
def func_0A_1AB5():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_1B64',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1B3C',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000B,
        (
            '尼冈德那家伙\n',
            '被带到哈肯门去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '那家伙好像\n',
            '做了相当坏的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '如果能找出\n',
            '他骗人的证据就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B61')

    def _loc_1B3C(): pass

    label('loc_1B3C')

    ChrTalk(
        0x000B,
        (
            '尼冈德那家伙\n',
            '被带到哈肯门去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B61(): pass

    label('loc_1B61')

    Jump('loc_208A')

    def _loc_1B64(): pass

    label('loc_1B64')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_1C50',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1BF7',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '刚才有军队上的人\n',
            '来我这里打听情况了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他们问我工房\n',
            '最近的经营状况怎么样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在我更奇怪了，到底发生了什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C4D')

    def _loc_1BF7(): pass

    label('loc_1BF7')

    ChrTalk(
        0x00FE,
        (
            '刚才有军队上的人\n',
            '来我这里打听情况了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他们问我工房\n',
            '最近的经营状况怎么样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C4D(): pass

    label('loc_1C4D')

    Jump('loc_208A')

    def _loc_1C50(): pass

    label('loc_1C50')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_1D30',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1CD5',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '我所经营的工房\n',
            '也被强盗袭击了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '尼冈德那家伙也就算了，\n',
            '我只担心雇来的工匠。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果没事就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D2D')

    def _loc_1CD5(): pass

    label('loc_1CD5')

    ChrTalk(
        0x00FE,
        (
            '我所经营的工房\n',
            '也被强盗袭击了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '尼冈德那家伙也就算了，\n',
            '我只担心雇来的工匠。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D2D(): pass

    label('loc_1D2D')

    Jump('loc_208A')

    def _loc_1D30(): pass

    label('loc_1D30')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_1E05',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1DB6',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '……就这样一直哭\n',
            '也无济于事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '工房被抢只能说明\n',
            '自己太缺乏经验。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好，在柏斯超市\n',
            '重新开始创业吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E02')

    def _loc_1DB6(): pass

    label('loc_1DB6')

    ChrTalk(
        0x00FE,
        (
            '工房被抢只能说明\n',
            '自己太缺乏经验。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好，在柏斯超市\n',
            '重新开始创业吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E02(): pass

    label('loc_1E02')

    Jump('loc_208A')

    def _loc_1E05(): pass

    label('loc_1E05')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_1EFF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1EE4',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '尼冈德那家伙真该死……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一直以来和我合作得好好的，\n',
            '竟然突然背叛我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本来工房借债就是\n',
            '他用强硬手段逼我签下的合同。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且现在他竟然\n',
            '成为了工房的店主。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到底是怎么回事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EFC')

    def _loc_1EE4(): pass

    label('loc_1EE4')

    ChrTalk(
        0x00FE,
        (
            '到底是怎么回事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1EFC(): pass

    label('loc_1EFC')

    Jump('loc_208A')

    def _loc_1EFF(): pass

    label('loc_1EFF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_2030',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1FD0',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '那间导力器工房\n',
            '一直以来是我经营的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有一次，\n',
            '借了他的钱却没办法还清……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他就以这个借口\n',
            '把我的店抢走了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本来还想着从超市独立出来\n',
            '经营自己的店的梦想终于实现了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_202D')

    def _loc_1FD0(): pass

    label('loc_1FD0')

    ChrTalk(
        0x00FE,
        (
            '本来还想着从超市独立出来\n',
            '经营自己的店的梦想终于实现了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊～未来一片黑暗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_202D(): pass

    label('loc_202D')

    Jump('loc_208A')

    def _loc_2030(): pass

    label('loc_2030')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_208A',
    )

    ChrTalk(
        0x00FE,
        (
            '啊啊……啊呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎么会这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我倾注了一生的\n',
            '那间工房……啊呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_208A(): pass

    label('loc_208A')

    TalkEnd(0x000B)

    Return()

# id: 0x000B offset: 0x208E
@scena.Code('func_0B_208E')
def func_0B_208E():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_218E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_213A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '这个地方果然保存着\n',
            '关于目击到古代龙的记载。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼呼呼，我的热情燃烧起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '它们为什么会突然失踪……\n',
            '这一谜题的答案说不定很快就能揭晓。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_218B')

    def _loc_213A(): pass

    label('loc_213A')

    ChrTalk(
        0x00FE,
        (
            '这个地方还保存着\n',
            '关于目击到古代龙的记载。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼呼呼，我的热情燃烧起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_218B(): pass

    label('loc_218B')

    Jump('loc_2996')

    def _loc_218E(): pass

    label('loc_218E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_226F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_221B',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '古代龙最后被目击的地点\n',
            '就是在这个柏斯地区。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以，\n',
            '我才会到这里来进行调查……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '首先要仔细收集当地的情报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_226C')

    def _loc_221B(): pass

    label('loc_221B')

    ChrTalk(
        0x00FE,
        (
            '古代龙最后被目击的地点\n',
            '就是在这个柏斯地区。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '首先要仔细收集当地的情报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_226C(): pass

    label('loc_226C')

    Jump('loc_2996')

    def _loc_226F(): pass

    label('loc_226F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_22DF',
    )

    ChrTalk(
        0x00FE,
        (
            '在『大崩坏』之前\n',
            '就已经存在的古代龙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '它们好像是按照自己的意志\n',
            '而选择在这个世界上消失的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2996')

    def _loc_22DF(): pass

    label('loc_22DF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_259E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2542',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '我的研究对象是在『大崩坏』以前的\n',
            '旧世界中生存的生物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '被称为比人类还要聪明，\n',
            '近似于神的存在……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对，就是指古代龙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，在主日学校学到过呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '但不是说，古代龙直到数十年前\n',
            '还在利贝尔王国生存的吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '可是，自从导力器发明出来之后，\n',
            '它们就消失无踪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#014F……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#501F怎么了，约修亚？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F没什么，\n',
            '只是觉得你能记得上课讲的东西，\n',
            '还真是难得啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#009F真是没礼貌啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#000F因为，\n',
            '体型那么大头脑又好的生物，\n',
            '听起来就很想亲眼看看呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#001F只是想想就觉得很兴奋。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x00FE, 400)
    ChrTurnDirection(0x0102, 0x00FE, 400)

    ChrTalk(
        0x00FE,
        (
            '哈哈，我也想亲眼看看呢。\n',
            '所以才在各地进行调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_259B')

    def _loc_2542(): pass

    label('loc_2542')

    ChrTalk(
        0x00FE,
        (
            '我的研究对象是在『大崩坏』以前的\n',
            '在旧世界生存的智慧生物……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对，就是指古代龙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_259B(): pass

    label('loc_259B')

    Jump('loc_2996')

    def _loc_259E(): pass

    label('loc_259E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_26C0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_265A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '在『大崩坏』之前，\n',
            '大陆上好像有比现在\n',
            '更加优秀的导力技术。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且现在也发现了\n',
            '在『大崩坏』之前的时代\n',
            '所使用过的导力装置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以『古代遗物』相称\n',
            '也毫不为过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26BD')

    def _loc_265A(): pass

    label('loc_265A')

    ChrTalk(
        0x00FE,
        (
            '现在也发现了\n',
            '在『大崩坏』之前的时代\n',
            '所使用过的导力装置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以『古代遗物』相称\n',
            '也毫不为过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_26BD(): pass

    label('loc_26BD')

    Jump('loc_2996')

    def _loc_26C0(): pass

    label('loc_26C0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_27FA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2773',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '你知道『大崩坏』吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '很久很久以前，在这块大陆上\n',
            '有高度发达的导力文明存在着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过后来因为一场被称为『大崩坏』的\n',
            '天地异变的破坏而全部消失掉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27F7')

    def _loc_2773(): pass

    label('loc_2773')

    ChrTalk(
        0x00FE,
        (
            '很久很久以前，在这块大陆上\n',
            '有高度发达的导力文明存在着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过后来因为一场被称为『大崩坏』的\n',
            '天地异变的破坏而全部消失掉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_27F7(): pass

    label('loc_27F7')

    Jump('loc_2996')

    def _loc_27FA(): pass

    label('loc_27FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_2996',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2902',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '我是一个\n',
            '研究古代生物的学者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '之前去进行地质调查的时候，\n',
            '无意间发现一只行动非常敏捷的魔兽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像就是在西柏斯街道上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那是种非常珍贵的魔兽，\n',
            '虽然我想抓住它，\n',
            '但是凭我的脚力是追不上的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来还是要多做点运动啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2996')

    def _loc_2902(): pass

    label('loc_2902')

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '之前去进行地质调查的时候，\n',
            '无意间发现一只行动非常敏捷的魔兽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那是种非常珍贵的魔兽，\n',
            '虽然我想抓住它，\n',
            '但是凭我的脚力是追不上的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2996(): pass

    label('loc_2996')

    TalkEnd(0x000C)

    Return()

# id: 0x000C offset: 0x299A
@scena.Code('func_0C_299A')
def func_0C_299A():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_2A94',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2A2F',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '特里诺家的米拉诺，\n',
            '现在可以称得上是\n',
            '实力仅次于市长的女强人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '博尔德家也非常有实力，\n',
            '但是如今，形势倾向于米拉诺啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A91')

    def _loc_2A2F(): pass

    label('loc_2A2F')

    ChrTalk(
        0x00FE,
        (
            '我自己将来\n',
            '该怎么生活下去才好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '协助米拉诺工作也不错，\n',
            '但是我还是想做自己喜欢的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A91(): pass

    label('loc_2A91')

    Jump('loc_2C28')

    def _loc_2A94(): pass

    label('loc_2A94')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_2BBA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2B61',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '米拉诺突然请了急假，\n',
            '到底是怎么回事……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '飞艇停止航行\n',
            '不是无法进行工作了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '她老是说忙的时候\n',
            '才会想做这样那样的事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在休息的时候\n',
            '反而会觉得什么事情就做不了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2BB7')

    def _loc_2B61(): pass

    label('loc_2B61')

    ChrTalk(
        0x00FE,
        (
            '米拉诺突然请了急假\n',
            '到底是怎么回事……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '飞艇停止航行\n',
            '不是无法进行工作了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2BB7(): pass

    label('loc_2BB7')

    Jump('loc_2C28')

    def _loc_2BBA(): pass

    label('loc_2BBA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_2C28',
    )

    ChrTalk(
        0x00FE,
        (
            '哈啊……\n',
            '陪着米拉诺还真累啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但正因为有那种干劲，\n',
            '所以才能称得上实力\n',
            '仅次于市长的女强人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C28(): pass

    label('loc_2C28')

    TalkEnd(0x000D)

    Return()

# id: 0x000D offset: 0x2C2C
@scena.Code('func_0D_2C2C')
def func_0D_2C2C():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 4, 0x314)),
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 7, 0x317)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_499D',
    )

    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0101, -7020, 1500, -2310, 180)
    SetChrPos(0x0102, -5070, 1500, -2700, 225)
    SetChrPos(0x0103, -6250, 1500, -1960, 180)
    CameraMove(-7050, 1500, -2350, 0)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x0063, 0, 0x318))
    OP_28(0x0036, 0x04, 0x02)
    OP_28(0x0036, 0x04, 0x04)
    OP_28(0x0036, 0x01, 0x0001)
    OP_28(0x000E, 0x04, 0x40)
    OP_28(0x0015, 0x04, 0x40)

    ChrTalk(
        0x000E,
        (
            '#0270021289V#145F呜……可恶……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270021290V真是的……别开玩笑了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270021291V……呜……嗝……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021292V#002F人是找到了，\n',
            '可是喝得烂醉的样子……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021293V只不过是被拒绝采访，\n',
            '受到的打击有那么大吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021294V#027F明明是个大男人，还真是没出息啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021295V酒是用来喝的，\n',
            '可不是用来灌的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0102, 270, 0)
    SetChrDirection(0x0101, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010021296V#007F一般人当然没法和\n',
            '无底洞一样的雪拉姐相提并论啦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021297V#020F说得真过分，\n',
            '无底洞用来形容爱娜还差不多。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021298V那个女人不管喝多少，\n',
            '都是面不改色、泰然自若呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021299V和我这种舒爽自然的醉酒方式\n',
            '根本不能混为一谈啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021300V#009F什么舒爽自然的醉酒方式啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021301V明明总是喝得酩酊大醉，\n',
            '只会一个劲儿地连累周围的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021302V#019F如果说雪拉姐姐是酒桶的话，\n',
            '那么爱娜姐姐给人的感觉就是酒缸。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020021303V两人的酒量都没有界限这一点，\n',
            '我倒是觉得没有什么不同……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021304V#022F哼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0270021305V#145F……唔…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2FF6')
    def lambda_2FF6():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2FF6)

    @scena.Lambda('lambda_3004')
    def lambda_3004():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3004)

    CameraMove(-7050, 1500, -2800, 1000)
    OP_62(0x000E, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(300)

    SetChrSubChip(0x000E, 0)
    Sleep(900)

    ChrTalk(
        0x000E,
        (
            '#0270021306V#142F呜～这里是……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021307V#010F好像醒过来了。\n',
            '酒喝得太多对身体可不好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0270021308V#145F呜……\n',
            '脑袋里像在打鼓一样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000E, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    SetChrSubChip(0x000E, 1)
    Sleep(500)

    ChrTalk(
        0x000E,
        (
            '#0270021309V#143F……怎么回事？\n',
            '这不是那两个游击士新人吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270021310V喂喂，\n',
            '为什么我还在洛连特啊！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270021311V明明已经来到柏斯了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021312V#006F你还没睡醒吧。\n',
            '是我们也到柏斯来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0270021313V#145F呼……\n',
            '真是吓了我一跳……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270021314V#141F哎哟，这次是和一位\n',
            '性感的姐姐一起来的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021315V#020F初次见面，记者先生。\n',
            '我是雪拉扎德·哈维。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021316V是这两个孩子的前辈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0270021317V#143F雪拉扎德……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270021318V难道说你就是\n',
            '那个『银闪雪拉扎德』？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021319V#021F哎呀，真荣幸。\n',
            '竟然知道我的名字呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0270021320V#141F啊啊，以前听过你的传闻。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270021321V『银闪』可是年轻一辈的\n',
            '游击士中数一数二的人物啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270021322V也就是说，\n',
            '你们几个是来调查这次事件的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021323V#027F啊，算是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021324V#000F你收集到什么情报了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021325V刚才在市长家门前看到你了，\n',
            '好像遇到什么困难的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0270021326V#145F可恶，被你们看见了啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270021327V#144F没错，就是这样！\n',
            '我正为没有材料可写而发愁啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021328V#008F啊，果然是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0270021329V#142F都是因为军队的什么情报管制，\n',
            '搞得我们连这件事到底是不是事故都不知道。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270021330V为了和摩尔根将军会面，\n',
            '我们去了哈肯大门，\n',
            '中途在检查站给拦了下来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270021331V我们想，那么至少采访一下\n',
            '那位传说中的美人市长吧，\n',
            '又被女佣给挡在门外……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270021332V再加上，那个傻丫头\n',
            '时不时地犯些愚蠢的错误……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270021333V#145F唉，女神啊！\n',
            '告诉我该怎么办呀！ ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021334V#501F好像被逼到绝境了呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021335V如果这么想得到情报的话，\n',
            '告诉你也不是不可以……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000E, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000E,
        (
            '#0270021336V#143F哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021337V#006F我们现在正在协助\n',
            '梅贝尔市长调查这次的事件。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021338V由于市长的介绍，\n',
            '我们也见到了摩尔根将军。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0270021339V#143F…………………真的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021340V#502F嗯，真的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000E, 0x0000012C, 1600, 0x36, 0x39, 0x000000FA, 0x00)
    Sleep(1000)

    ChrTalk(
        0x000E,
        (
            '#0270021341V#147F噢噢噢噢噢噢！\n',
            '这真是女神的相助！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x000E)
    Sleep(500)

    ChrTalk(
        0x000E,
        (
            '#0270021342V#144F无论如何也拜托了！\n',
            '把这件事的详情全告诉我吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021343V#015F告诉你倒是没什么关系……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020021344V#010F奈尔先生，\n',
            '你没有忘记这种情况下的规则吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0270021345V#143F#1P……哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021346V#027F呵呵……\n',
            '也就是说情报不是免费的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021347V需要付出一定的代价。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000E, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1200)

    ChrTalk(
        0x000E,
        (
            '#0270021348V#142F#1P难、难道是要钱？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270021349V不是我骗你们，\n',
            '我这次的取材费差不多快用完了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021350V#010F我们又不是情报站，\n',
            '所以不会要钱的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020021351V奈尔先生，你们是不是\n',
            '在事件发生之后就立刻来到柏斯了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020021352V之后一定听说了\n',
            '各种各样有趣的事吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0270021353V#145F#1P嘁，摆出一副大人的样子，\n',
            '真是个滑头的小鬼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270021354V话说在前面，\n',
            '我这里的消息可不是什么大情报哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021355V#010F只要是和事件相关，\n',
            '无论多么细微的情报都没有关系。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020021356V#019F不过……\n',
            '如果你舍不得说出来，那我们也不勉强你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0270021357V#144F#1P我知道了，我全说出来总行了吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270021358V我这里有两条消息。\n',
            '就用这些和你们交换吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021359V#011F那就这样定了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0101, 135, 400)

    ChrTalk(
        0x0101,
        (
            '#0010021360V#006F（约修亚真是能说会道啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021361V#021F（呵呵，看起来\n',
            '　讨价还价的本事相当不错嘛。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(3330, 0, -1410, 0)
    SetChrSubChip(0x000E, 0)
    SetChrFlags(0x0101, 0x0004)
    SetChrFlags(0x0102, 0x0004)
    SetChrFlags(0x0103, 0x0004)
    SetChrFlags(0x000E, 0x0004)
    SetChrPos(0x0101, 5100, 200, -1040, 270)
    SetChrPos(0x0102, 5100, 200, -2450, 270)
    SetChrPos(0x0103, 2950, 200, -2590, 90)
    SetChrPos(0x000E, 2950, 0, -1070, 90)
    SetChrChipByIndex(0x0101, 20)
    SetChrChipByIndex(0x0102, 21)
    SetChrChipByIndex(0x0103, 22)
    SetChrSubChip(0x0102, 2)
    SetChrSubChip(0x0103, 1)
    Sleep(500)

    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x000E,
        (
            '#0270021362V#140F#2P第一条消息，\n',
            '是在西边的拉文努村的目击情报。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270021363V是从正好来到柏斯市的\n',
            '村民那里打听来的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270021364V事件发生的当晚，\n',
            '有村民目击到夜空中有个巨大的影子飞过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021365V#004F夜空中有个巨大的影子飞过？\n',
            '那、那是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0270021366V#142F#2P嗯，不管谁听到\n',
            '都会认为是那艘定期船吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270021367V#145F之后，军方也派了部队去调查，\n',
            '但结果好像什么也没发现……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021368V#007F什么呀。\n',
            '害我白期待了半天。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021369V#020F那就是说，只是单纯的看错了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0270021370V#144F#2P所以我不是说了吗！\n',
            '不是什么大情报啦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270021371V即使像这种小消息，在情报管制下，\n',
            '收集起来也是相当辛苦的啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021372V#010F#3P您辛苦了。\n',
            '那么，另外一条消息是？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x000E, 2)
    Sleep(300)

    ChrTalk(
        0x000E,
        (
            '#0270021373V#142F#2P哼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270021374V……另一条是，\n',
            '军队的情报部好像开始有所行动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021375V#004F情报部？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021376V#020F我倒是听说过这方面的传闻。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021377V最近，王国军新设立了一个\n',
            '专门负责情报收集和分析的机构。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0270021378V#140F#2P对，据说是个\n',
            '与王室亲卫队并立的精英组织。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270021379V担任司令的是一位\n',
            '叫作理查德上校的人，\n',
            '据说是相当干练的军人呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270021380V人们都在议论，如果由他出马的话，\n',
            '这件事一定会顺利解决的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021381V#501F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021382V可是，这种消息对我们的调查\n',
            '好像没什么帮助呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x000E, 0)
    Sleep(300)

    ChrTalk(
        0x000E,
        (
            '#0270021383V#144F#2P那就抱歉了，没帮上什么忙！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270021384V不过，约定就是约定！\n',
            '你们自己也这么说的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021385V#019F#3P嗯，那个请不用担心。',
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
            '约修亚把在洛连特发生的事件和\n',
            '从摩尔根将军处听到的消息\n',
            '全部告诉了奈尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x000E,
        (
            '#0270021386V#143F#2P空贼团『卡普亚一家』……\n',
            '向王家和飞艇公社提出赎金要求……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270021387V#147F就是这个！\n',
            '这就是我死也要得到的\n',
            '所谓的决定性情报！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021388V#010F#3P现在满足了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x000E, 2)
    Sleep(300)

    ChrTalk(
        0x000E,
        (
            '#0270021389V#141F#2P当然啦！\n',
            '这样就能够写报道了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270021390V不能再耽搁了……\n',
            '得赶快找到朵洛希那家伙！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270021391V#144F就这样，再见啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x000E, 0, 0)
    SetChrChipByIndex(0x000E, 23)
    ChrJumpTo(0x000E, 2990, 0, -120, 600, 8000)
    CreateThread(0x0101, 0x02, 0x00, 0x001C)

    @scena.Lambda('lambda_4301')
    def lambda_4301():
        CameraMove(2130, 0, -2640, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_4301)

    ChrWalkTo(0x000E, 1490, 0, -370, 6000, 0x01)
    ChrWalkTo(0x000E, 110, 200, -5710, 6000, 0x01)

    @scena.Lambda('lambda_4341')
    def lambda_4341():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_4341)

    ChrWalkTo(0x000E, 50, 200, -8000, 3000, 0x00)
    SetChrFlags(0x000E, 0x0080)
    WaitForThreadExit(0x0101, 0x0003)
    OP_62(0x0101, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010021392V#004F好，好强的气势……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_43B1')
    def lambda_43B1():
        CameraMove(3330, 0, -1410, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_43B1)

    Sleep(500)

    SetChrSubChip(0x0102, 0)
    Sleep(100)

    SetChrSubChip(0x0102, 2)
    Sleep(100)

    SetChrSubChip(0x0103, 0)
    Sleep(300)

    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0102,
        (
            '#0020021393V#010F#3P最近老是为取材的事烦恼，\n',
            '快被逼到绝境了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020021394V能帮上忙真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021395V#006F#2P你还敢说呢。\n',
            '刚才还在一本正经地讨价还价。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021396V你呀，有时候还真是一肚子坏水……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021397V#019F#3P我并没有别的意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020021398V这只不过是\n',
            '以互惠互利为前提的商谈而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021399V#020F呵呵，说得很有道理。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021400V游击士所接触的\n',
            '可不光是善良的人啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021401V如果交涉对象并非通情达理之辈，\n',
            '强硬一点也是必要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1700, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010021402V#007F#2P唔～对于我来说，\n',
            '做到这一点可是很难啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021403V#006F……啊，不说这个了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021404V夜空中飞过的黑影……\n',
            '你们不觉得这说法很让人在意吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021405V#014F#3P是拉文努村的目击情报吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020021406V既然军队已经调查过，\n',
            '我认为实际是误报的可能性很高。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021407V#006F#2P可是可是，\n',
            '那个调查也许不是很全面啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021408V倒也不是针对摩尔根将军，\n',
            '不过那些军人好像都有点死脑筋，\n',
            '他们总会看漏了什么地方吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021409V#015F#3P确实如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020021410V#010F即使没用，也应该去调查一下。\n',
            '说不定会有什么收获呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 2, 0x31A)),
            Expr.Return,
        ),
        'loc_481C',
    )

    ChrTalk(
        0x0103,
        (
            '#0030021411V#021F呵呵，\n',
            '你们两个都成长了不少啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021412V#020F既然这样，\n',
            '我们就赶快去拉文努村看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_48E1')

    def _loc_481C(): pass

    label('loc_481C')

    ChrTalk(
        0x0103,
        (
            '#0030021413V#021F呵呵，\n',
            '你们两个都成长了不少啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021414V#020F拉文努村，是西边的一个\n',
            '以果树栽培而闻名的小村落。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021415V在西柏斯街道途中有一条向北的山道，\n',
            '村子就在那边哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021416V我们立刻出发吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_48E1(): pass

    label('loc_48E1')

    ChrTalk(
        0x0101,
        (
            '#0010021417V#006F#2P好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetChrStatus(0x0000, 0xFE, 0)
    SetChrStatus(0x0001, 0xFE, 0)
    SetChrStatus(0x0002, 0xFE, 0)
    SetChrStatus(0x0003, 0xFE, 0)
    SetChrStatus(0x0004, 0xFE, 0)
    SetChrStatus(0x0005, 0xFE, 0)
    SetChrStatus(0x0006, 0xFE, 0)
    SetChrStatus(0x0007, 0xFE, 0)
    ClearChrFlags(0x0101, 0x0004)
    ClearChrFlags(0x0102, 0x0004)
    ClearChrFlags(0x0103, 0x0004)
    ClearChrFlags(0x000E, 0x0004)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0103, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrPos(0x0101, 1150, 0, -2300, 180)
    SetChrPos(0x0103, 1150, 0, -2300, 180)
    SetChrPos(0x0102, 1150, 0, -2300, 180)
    OP_69(0x0101, 0)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Jump('loc_4BFA')

    def _loc_499D(): pass

    label('loc_499D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_4ABC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4A6D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x000E,
        (
            '#0270021418V#146F嗝……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021419V#000F喂，奈尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0270021420V#146F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270021421V既然这样，\n',
            '我只好再去追其它的新闻线索了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270021422V嗝……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021423V#017F这样不行啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4AB9')

    def _loc_4A6D(): pass

    label('loc_4A6D')

    ChrTalk(
        0x000E,
        (
            '#0270021424V#146F嗝……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270021425V既然这样，\n',
            '我只好再去追其它的新闻线索了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4AB9(): pass

    label('loc_4AB9')

    Jump('loc_4BFA')

    def _loc_4ABC(): pass

    label('loc_4ABC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_4BFA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4BA8',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x0102,
        (
            '#0020021426V#010F啊，奈尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0270021427V#146F呜～……嗝……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270021428V真是的，\n',
            '好不容易从洛连特走着来到这里……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270021429V咕噜咕噜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021430V#501F哎呀，喝得烂醉呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021431V#020F能醉成这个样子，真是差劲呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4BFA')

    def _loc_4BA8(): pass

    label('loc_4BA8')

    ChrTalk(
        0x000E,
        (
            '#0270021432V#146F呜～……嗝……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270021433V真是的，\n',
            '好不容易从洛连特走着来到这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4BFA(): pass

    label('loc_4BFA')

    TalkEnd(0x000E)

    Return()

# id: 0x000E offset: 0x4BFE
@scena.Code('func_0E_4BFE')
def func_0E_4BFE():
    TalkBegin(0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_4C68',
    )

    ChrTalk(
        0x00FE,
        (
            '多亏了这一连串事件得到解决，\n',
            '顾客们的脸色也都喜气洋洋的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '果然和平还是最美好的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_56D5')

    def _loc_4C68(): pass

    label('loc_4C68')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_4D47',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4CF9',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '最近，好像城里非常多事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本店是否也要\n',
            '配备几名警备比较好呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果万一有客人遭遇到什么不幸，\n',
            '那就糟糕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4D44')

    def _loc_4CF9(): pass

    label('loc_4CF9')

    ChrTalk(
        0x00FE,
        (
            '最近，好像城里非常多事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本店是否也要\n',
            '配备几名警备比较好呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4D44(): pass

    label('loc_4D44')

    Jump('loc_56D5')

    def _loc_4D47(): pass

    label('loc_4D47')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_5013',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0071, 5, 0x38D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4FBE',
    )

    SetScenaFlags(ScenaFlag(0x0071, 5, 0x38D))
    ChrTurnDirection(0x00FE, 0x0104, 0)
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrJumpToRelative(0x00FE, 0, 0, 0, 800, 12000)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '咦，你、你是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不，你是那个时候的……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#030F哟，主管先生。\n',
            '上次真是多谢您的款待了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊——！\n',
            '你、你不是已经被交给士兵了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这、这样的话，\n',
            '我是不是要再通报一次……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#035F呵呵，你就冷静一下嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#030F你们能请我来吃饭已经算十分荣幸的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000F, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0104,
        (
            '#035F能够理解我这位极富艺术修养的人才的人，\n',
            '也唯有你们餐厅的老板了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '而且，\n',
            '她还是一位如此闭月羞花的美丽女性。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#030F这家安特洛丝餐厅的将来，\n',
            '必定会如同沐浴在春日阳光下一般明艳动人。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#018F主管先生……\n',
            '我真的非常同情你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#007F嗯嗯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5010')

    def _loc_4FBE(): pass

    label('loc_4FBE')

    ChrTalk(
        0x00FE,
        (
            '这次的事情\n',
            '是作为主管的我失职引起的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉～……\n',
            '我真是对不起老板啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5010(): pass

    label('loc_5010')

    Jump('loc_56D5')

    def _loc_5013(): pass

    label('loc_5013')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_50D6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_50AC',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '欢、欢迎光临……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#002F（怎么了，\n',
            '　看起来样子相当没精神呢……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#014F（嗯，腰也直不起来了。\n',
            '　难道发生了什么事吗？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_50D3')

    def _loc_50AC(): pass

    label('loc_50AC')

    ChrTalk(
        0x00FE,
        (
            '唉，\n',
            '这件事该如何向老板交待呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_50D3(): pass

    label('loc_50D3')

    Jump('loc_56D5')

    def _loc_50D6(): pass

    label('loc_50D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_5295',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_51E6',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '现在，我们正在寻找一位\n',
            '能为本店弹琴的专属钢琴家……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是在国内好像\n',
            '没有什么非常出色的人才。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我已经跟老板商量过了，\n',
            '我们正在打算从帝国\n',
            '那里请一位钢琴家过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#023F哎～钢琴家啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#007F真、真不愧是一流的餐厅，\n',
            '规模就是不一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5292')

    def _loc_51E6(): pass

    label('loc_51E6')

    ChrTalk(
        0x00FE,
        (
            '现在，我们正在寻找一位\n',
            '能为本店弹琴的专属钢琴家……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是在国内好像\n',
            '没有什么非常出色的人才。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我已经跟老板商量过了，\n',
            '我们正在打算从帝国\n',
            '那里请一位钢琴家过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5292(): pass

    label('loc_5292')

    Jump('loc_56D5')

    def _loc_5295(): pass

    label('loc_5295')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_53FD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_53B0',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '感谢光临本店用餐。\n',
            '请慢走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们衷心希望\n',
            '客人能够再次光临本店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯～ \n',
            '刚才是市长请客吧，\n',
            '到底花了多少钱呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#009F凭我们自己的工资\n',
            '大概是消费不起的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F是呀……\n',
            '不过，味道的确很不错，\n',
            '物有所值呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '真是名不虚传。\n',
            '不愧是专家的手艺。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_53FA')

    def _loc_53B0(): pass

    label('loc_53B0')

    ChrTalk(
        0x00FE,
        (
            '感谢光临本店用餐。\n',
            '请慢走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们衷心希望\n',
            '客人能够再次光临本店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_53FA(): pass

    label('loc_53FA')

    Jump('loc_56D5')

    def _loc_53FD(): pass

    label('loc_53FD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_56D5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0071, 4, 0x38C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_565A',
    )

    SetScenaFlags(ScenaFlag(0x0071, 4, 0x38C))

    ChrTalk(
        0x00FE,
        (
            '欢迎光临。\n',
            '这里是安特洛丝餐厅。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请问客人预约了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊……没有。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '这里是饭店吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '您说得没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我是老板委任的主管，\n',
            '名叫雷克多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本店时时刻刻\n',
            '以最高级的食品和最优质的服务，\n',
            '来期待各位客人的光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我有自信能够为每位顾客\n',
            '提供满意的饭菜和服务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请一定要来本店体验一次。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F相当的自信呢。\n',
            '不过确实，从店的规模就能看出来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F他说让我们一定要体验一次呢。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '应该会很贵吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 0)

    ChrTalk(
        0x0103,
        (
            '#020F呵呵，那是肯定的了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '如果想享受一次正餐的话……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '至少要消灭三十只通缉魔兽\n',
            '得到的报酬才够吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 0)

    ChrTalk(
        0x0101,
        (
            '#007F唉，这里和我没有缘分呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_56D5')

    def _loc_565A(): pass

    label('loc_565A')

    ChrTalk(
        0x00FE,
        (
            '本店时时刻刻\n',
            '以最高级的食品和最优质的服务，\n',
            '来期待各位客人的光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我有自信能够为每位顾客\n',
            '提供满意的饭菜和服务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_56D5(): pass

    label('loc_56D5')

    TalkEnd(0x000F)

    Return()

# id: 0x000F offset: 0x56D9
@scena.Code('func_0F_56D9')
def func_0F_56D9():
    TalkBegin(0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_5738',
    )

    ChrTalk(
        0x00FE,
        (
            '终于把要采购的\n',
            '食物材料都买齐了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这下就可以试做\n',
            '考虑了很久的新菜式了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5B50')

    def _loc_5738(): pass

    label('loc_5738')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_57A9',
    )

    ChrTalk(
        0x00FE,
        (
            '格露娜那家伙很有前途……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说不定会在她身上发现\n',
            '与我不同的可能性。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '她给我的就是这种感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5B50')

    def _loc_57A9(): pass

    label('loc_57A9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_5876',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5832',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '刚才我好像听到主管的尖叫声……',
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

    ChrTalk(
        0x00FE,
        (
            '新的工作人员刚来的时候，\n',
            '我经常听到那个声音。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5873')

    def _loc_5832(): pass

    label('loc_5832')

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '刚才我好像听到主管的尖叫声……',
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

    def _loc_5873(): pass

    label('loc_5873')

    Jump('loc_5B50')

    def _loc_5876(): pass

    label('loc_5876')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_596E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_592C',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '之前的店主\n',
            '根本就听不进我的意见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，现在的老板\n',
            '却能热心地听取我的建议。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真的要感谢老板……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '老板和我素昧平生，\n',
            '但是却让我做上餐厅的主厨。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_596B')

    def _loc_592C(): pass

    label('loc_592C')

    ChrTalk(
        0x00FE,
        (
            '老板能够那么热心地\n',
            '听取我的建议。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我真的很感谢她……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_596B(): pass

    label('loc_596B')

    Jump('loc_5B50')

    def _loc_596E(): pass

    label('loc_596E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_59C1',
    )

    ChrTalk(
        0x00FE,
        (
            '烹饪是一种文化艺术。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因此独创性是必须的，\n',
            '而且绝对不允许妥协。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5B50')

    def _loc_59C1(): pass

    label('loc_59C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_59FF',
    )

    ChrTalk(
        0x00FE,
        (
            '……你们享受到料理的乐趣了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '欢迎再来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5B50')

    def _loc_59FF(): pass

    label('loc_59FF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_5B50',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5AF6',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '……作为一个厨师，\n',
            '在自己金盆洗手之前\n',
            '应该每天都在追求新的味道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '绝对不能自我满足。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果没有这样的心境，\n',
            '就没有资格当厨师长……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F总、总觉得他是个\n',
            '有一股恐怖压迫感的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F嗯，因为是专业人士嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5B50')

    def _loc_5AF6(): pass

    label('loc_5AF6')

    ChrTalk(
        0x00FE,
        (
            '作为一个厨师，\n',
            '在自己金盆洗手之前\n',
            '应该每天都在追求新的味道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '绝对不能自我满足。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5B50(): pass

    label('loc_5B50')

    TalkEnd(0x0010)

    Return()

# id: 0x0010 offset: 0x5B54
@scena.Code('func_10_5B54')
def func_10_5B54():
    TalkBegin(0x0011)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_5BA4',
    )

    ChrTalk(
        0x00FE,
        (
            '今天真是有劳了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请你们有空也到本店\n',
            '来享受料理的乐趣哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6150')

    def _loc_5BA4(): pass

    label('loc_5BA4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_5C4B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5C23',
    )

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '听我说听我说！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '厨师长吩咐我\n',
            '让我来做今天的汤。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我每晚都在练习做汤，\n',
            '这份辛苦终于有回报啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5C48')

    def _loc_5C23(): pass

    label('loc_5C23')

    ChrTalk(
        0x00FE,
        (
            '厨师长吩咐我\n',
            '让我来做今天的汤。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5C48(): pass

    label('loc_5C48')

    Jump('loc_6150')

    def _loc_5C4B(): pass

    label('loc_5C4B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_5D08',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5CE6',
    )

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '前几天，\n',
            '厨师长让我做了一锅汤。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这可是自从我来到这里以来的第一次。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然我不停地不停地重做，\n',
            '但是直到深夜他仍然陪着我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5D05')

    def _loc_5CE6(): pass

    label('loc_5CE6')

    ChrTalk(
        0x00FE,
        (
            '好！\n',
            '我要更加更加地努力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5D05(): pass

    label('loc_5D05')

    Jump('loc_6150')

    def _loc_5D08(): pass

    label('loc_5D08')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_5E86',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5E06',
    )

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '秘藏的『格兰·夏利拿』\n',
            '就这样被别人白喝了，\n',
            '老板竟然不把这当回事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明明年纪和我差不多，\n',
            '为什么能够如此心胸开阔呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '相对而言，\n',
            '主管就会面色苍白大发雷霆了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过那也是理所当然的。\n',
            '相对来说主管的境地还是比较可怜呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5E83')

    def _loc_5E06(): pass

    label('loc_5E06')

    ChrTalk(
        0x00FE,
        (
            '秘藏的『格兰·夏利拿』\n',
            '就这样被别人白喝了，\n',
            '老板竟然不把这当回事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明明年纪和我差不多，\n',
            '为什么能够如此心胸开阔呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5E83(): pass

    label('loc_5E83')

    Jump('loc_6150')

    def _loc_5E86(): pass

    label('loc_5E86')

    If(
        (
            (Expr.Eval, "OP_40(0x03A7)"),
            (Expr.PushLong, 0x5),
            Expr.Geq,
            (Expr.Eval, "OP_29(0x0012, 0x00, 0x02)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0012, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5EAA',
    )

    Call(1, 0x0000)

    Jump('loc_6150')

    def _loc_5EAA(): pass

    label('loc_5EAA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_5F5E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5F22',
    )

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '我本来是在\n',
            '卢安的酒店当厨师的，\n',
            '受老板的邀请来到这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像是因为她\n',
            '特别喜欢我做的点心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5F5B')

    def _loc_5F22(): pass

    label('loc_5F22')

    ChrTalk(
        0x00FE,
        (
            '虽然现在我还只是见习厨师，\n',
            '不过一定要坚持努力下去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5F5B(): pass

    label('loc_5F5B')

    Jump('loc_6150')

    def _loc_5F5E(): pass

    label('loc_5F5E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_6026',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5FE0',
    )

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '厨师长是一位非常严格的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，他不愧为\n',
            '利贝尔首屈一指的高级厨师。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '味感和技术都是超一流的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6023')

    def _loc_5FE0(): pass

    label('loc_5FE0')

    ChrTalk(
        0x00FE,
        (
            '厨师长是一位非常严格的人。\n',
            '但是，他的味感和技术都是超一流的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6023(): pass

    label('loc_6023')

    Jump('loc_6150')

    def _loc_6026(): pass

    label('loc_6026')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_60A8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6091',
    )

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '土豆削好了，\n',
            '接下来是洋葱……吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了不拖厨师长的后腿，\n',
            '我得加快速度才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_60A5')

    def _loc_6091(): pass

    label('loc_6091')

    ChrTalk(
        0x00FE,
        (
            '忙死了忙死了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_60A5(): pass

    label('loc_60A5')

    Jump('loc_6150')

    def _loc_60A8(): pass

    label('loc_60A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_6150',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_611F',
    )

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '厨师长对于味道的执念\n',
            '还真不是一般的厉害啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以前为了考虑新的汤点，\n',
            '曾经住在这个厨房里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6150')

    def _loc_611F(): pass

    label('loc_611F')

    ChrTalk(
        0x00FE,
        (
            '厨师长对于味道的执念\n',
            '还真不是一般的厉害啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6150(): pass

    label('loc_6150')

    TalkEnd(0x0011)

    Return()

# id: 0x0011 offset: 0x6154
@scena.Code('func_11_6154')
def func_11_6154():
    TalkBegin(0x0012)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_6213',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_61C4',
    )

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '以前订的红酒\n',
            '终于空运过来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '红酒的存货\n',
            '已经快见底了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是千钧一发啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6210')

    def _loc_61C4(): pass

    label('loc_61C4')

    ChrTalk(
        0x00FE,
        (
            '以前订的红酒\n',
            '终于空运过来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '库存已经快用完了，\n',
            '真是千钧一发啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6210(): pass

    label('loc_6210')

    Jump('loc_6669')

    def _loc_6213(): pass

    label('loc_6213')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_628C',
    )

    ChrTalk(
        0x00FE,
        (
            '飞艇重新开始起航了，\n',
            '终于能够订购到酒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明明订购单上有的，\n',
            '但是却偏偏这时候断货了，\n',
            '我好不甘心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6669')

    def _loc_628C(): pass

    label('loc_628C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_638E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_633B',
    )

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '麻烦了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在我休息的时候，\n',
            '那瓶『格兰·夏利拿』\n',
            '竟然被人白喝掉了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然老板没有怪我，\n',
            '还对我面带微笑，\n',
            '但我还是觉得自己要负一定的责任。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_638B')

    def _loc_633B(): pass

    label('loc_633B')

    ChrTalk(
        0x00FE,
        (
            '麻烦了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在我休息的时候，\n',
            '那瓶『格兰·夏利拿』\n',
            '竟然被人白喝掉了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_638B(): pass

    label('loc_638B')

    Jump('loc_6669')

    def _loc_638E(): pass

    label('loc_638E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_64E7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6488',
    )

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '我本来是帝国的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有一天，\n',
            '这里的老板到我工作的饭店用餐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '当时她特别喜欢\n',
            '我所调制的酒。\n',
            '后来就给我写信了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '问我愿不愿意到她的店工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一开始我只是想来利贝尔\n',
            '看看这家店的情况，\n',
            '没想到就一直工作到了现在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_64E4')

    def _loc_6488(): pass

    label('loc_6488')

    ChrTalk(
        0x00FE,
        (
            '老板邀请我来工作的时候\n',
            '我还苦恼了一阵子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '她确实有一种不可思议的魅力呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_64E4(): pass

    label('loc_64E4')

    Jump('loc_6669')

    def _loc_64E7(): pass

    label('loc_64E7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_65D2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6590',
    )

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '糟糕了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为定期船停航了，\n',
            '就不能向外面订购酒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过现在酒库里还有些存货，\n',
            '我想应该没什么问题……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '什么时候才能恢复原状呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_65CF')

    def _loc_6590(): pass

    label('loc_6590')

    ChrTalk(
        0x00FE,
        (
            '糟糕了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为定期船停航了，\n',
            '就不能向外面订购酒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_65CF(): pass

    label('loc_65CF')

    Jump('loc_6669')

    def _loc_65D2(): pass

    label('loc_65D2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_661D',
    )

    ChrTalk(
        0x00FE,
        (
            '谢谢光临本店用餐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们随时期待着\n',
            '各位客人的再次光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6669')

    def _loc_661D(): pass

    label('loc_661D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_6669',
    )

    ChrTalk(
        0x00FE,
        (
            '我是这家店的斟酒服务生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '凡是和酒有关的事情\n',
            '都可以来问我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6669(): pass

    label('loc_6669')

    TalkEnd(0x0012)

    Return()

# id: 0x0012 offset: 0x666D
@scena.Code('func_12_666D')
def func_12_666D():
    TalkBegin(0x0013)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_670A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_66CE',
    )

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    ChrTalk(
        0x00FE,
        (
            '欢迎光临～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果您要就餐的话，\n',
            '我会带您去一个环境比较好的位子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6707')

    def _loc_66CE(): pass

    label('loc_66CE')

    ChrTalk(
        0x00FE,
        (
            '如果您要就餐的话，\n',
            '我会带您去一个环境比较好的位子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6707(): pass

    label('loc_6707')

    Jump('loc_6A91')

    def _loc_670A(): pass

    label('loc_670A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_674D',
    )

    ChrTalk(
        0x00FE,
        (
            '厨师长拜托我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一会儿要去\n',
            '柏斯超市买点东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6A91')

    def _loc_674D(): pass

    label('loc_674D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_6822',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_67D9',
    )

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    ChrTalk(
        0x00FE,
        (
            '前不久，\n',
            '有一瓶非常珍贵的酒被客人喝掉了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我可是听到了主管\n',
            '久违了的尖叫声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那就像是\n',
            '女人的声音一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_681F')

    def _loc_67D9(): pass

    label('loc_67D9')

    ChrTalk(
        0x00FE,
        (
            '我可是听到了主管\n',
            '久违了的尖叫声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那就像是\n',
            '女人的声音一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_681F(): pass

    label('loc_681F')

    Jump('loc_6A91')

    def _loc_6822(): pass

    label('loc_6822')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_6935',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_68F3',
    )

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    ChrTalk(
        0x00FE,
        (
            '我本来在蔡斯的\n',
            '一家饭店当服务员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在的老板去蔡斯\n',
            '谈生意的时候看中了我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '她提出的工资很不错，\n',
            '而且分配的工作也很轻松。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且对我提出的要求\n',
            '也毫不犹豫地就答应了下来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6932')

    def _loc_68F3(): pass

    label('loc_68F3')

    ChrTalk(
        0x00FE,
        (
            '老板真是一个\n',
            '当机立断的人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和主管的性格正好相反。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6932(): pass

    label('loc_6932')

    Jump('loc_6A91')

    def _loc_6935(): pass

    label('loc_6935')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_6A05',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_69CF',
    )

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    ChrTalk(
        0x00FE,
        (
            '这家店自从被\n',
            '现在的老板买下之后，\n',
            '人气就越来越旺了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '几乎所有的工作人员\n',
            '都是老板自己带过来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过我是自己找过来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6A02')

    def _loc_69CF(): pass

    label('loc_69CF')

    ChrTalk(
        0x00FE,
        (
            '这里几乎所有的工作人员\n',
            '都是老板自己带过来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6A02(): pass

    label('loc_6A02')

    Jump('loc_6A91')

    def _loc_6A05(): pass

    label('loc_6A05')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_6A41',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，刚才的客人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有什么东西忘拿了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6A91')

    def _loc_6A41(): pass

    label('loc_6A41')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_6A91',
    )

    ChrTalk(
        0x00FE,
        (
            '欢迎光临～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果您要就餐的话，\n',
            '我会带您去一个环境比较好的位子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6A91(): pass

    label('loc_6A91')

    TalkEnd(0x0013)

    Return()

# id: 0x0013 offset: 0x6A95
@scena.Code('func_13_6A95')
def func_13_6A95():
    TalkBegin(0x0014)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_6B2A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6AF7',
    )

    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    ChrTalk(
        0x00FE,
        (
            '定期船恢复开航了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们在柏斯\n',
            '也玩得差不多了，\n',
            '该回王都了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6B27')

    def _loc_6AF7(): pass

    label('loc_6AF7')

    ChrTalk(
        0x00FE,
        (
            '我们在柏斯\n',
            '也玩得差不多了，\n',
            '该回王都了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6B27(): pass

    label('loc_6B27')

    Jump('loc_705C')

    def _loc_6B2A(): pass

    label('loc_6B2A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_6C49',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6BDE',
    )

    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    ChrTalk(
        0x00FE,
        (
            '我们从王都到这里来的时候，\n',
            '是坐船从瓦雷利亚湖上渡过来的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '湖的旁边\n',
            '有一家非常不错的旅馆呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们也去那里住了一晚。\n',
            '嗯，旅馆的名字叫什么呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6C46')

    def _loc_6BDE(): pass

    label('loc_6BDE')

    ChrTalk(
        0x00FE,
        (
            '我们从王都到这里来的时候，\n',
            '是坐船从瓦雷利亚湖上渡过来的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '湖的旁边\n',
            '有一家非常不错的旅馆呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6C46(): pass

    label('loc_6C46')

    Jump('loc_705C')

    def _loc_6C49(): pass

    label('loc_6C49')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_6D34',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6CEF',
    )

    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    ChrTalk(
        0x00FE,
        (
            '我对军队的人\n',
            '没有什么好感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不识风趣，又盛气凌人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为什么不能\n',
            '放下这个架子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '当然我也不是说\n',
            '所有的军人都是这个样子的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6D31')

    def _loc_6CEF(): pass

    label('loc_6CEF')

    ChrTalk(
        0x00FE,
        (
            '我对军队的人\n',
            '没有什么好感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为什么不能\n',
            '放下这个架子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6D31(): pass

    label('loc_6D31')

    Jump('loc_705C')

    def _loc_6D34(): pass

    label('loc_6D34')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_6E07',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6DBF',
    )

    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    ChrTalk(
        0x00FE,
        (
            '在这个城市的西北方\n',
            '有一个盛产美味水果的村子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是因为在山里，\n',
            '所以靠我们的脚力是去不了的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真遗憾……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6E04')

    def _loc_6DBF(): pass

    label('loc_6DBF')

    ChrTalk(
        0x00FE,
        (
            '对了，买水果的话，\n',
            '超市里不就有很多吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '待会儿过去看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6E04(): pass

    label('loc_6E04')

    Jump('loc_705C')

    def _loc_6E07(): pass

    label('loc_6E07')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_6F35',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6EE3',
    )

    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    ChrTalk(
        0x00FE,
        (
            '定期船的运营停止了，\n',
            '是真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过就这样\n',
            '在这个城市里多呆两天也不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为嘛，\n',
            '我自己都不知道该怎么做。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我想慢慢品尝美食，\n',
            '尽情到超市购物，\n',
            '敞开胸怀在这片土地上惬意地享受生活。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6F32')

    def _loc_6EE3(): pass

    label('loc_6EE3')

    ChrTalk(
        0x00FE,
        (
            '听说定期船停航了，是真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过就这样\n',
            '在这个城市里多呆两天也不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6F32(): pass

    label('loc_6F32')

    Jump('loc_705C')

    def _loc_6F35(): pass

    label('loc_6F35')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_6FF1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6FAB',
    )

    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    ChrTalk(
        0x00FE,
        (
            '这家餐厅在格兰赛尔\n',
            '口碑也相当不错呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我就是为了\n',
            '品尝这里的饭菜，\n',
            '才从王都专门过来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6FEE')

    def _loc_6FAB(): pass

    label('loc_6FAB')

    ChrTalk(
        0x00FE,
        (
            '真是名不虚传啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我还是第一次吃到\n',
            '如此美味的利贝尔料理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6FEE(): pass

    label('loc_6FEE')

    Jump('loc_705C')

    def _loc_6FF1(): pass

    label('loc_6FF1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_705C',
    )

    ChrTalk(
        0x00FE,
        (
            '我们是从王都\n',
            '到这里来购物和品尝美食的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然王都也很热闹，\n',
            '但是这个城市也丝毫不比王都差。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_705C(): pass

    label('loc_705C')

    TalkEnd(0x0014)

    Return()

# id: 0x0014 offset: 0x7060
@scena.Code('func_14_7060')
def func_14_7060():
    TalkBegin(0x0015)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_7178',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7111',
    )

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    ChrTalk(
        0x00FE,
        (
            '下一次，\n',
            '我想去埃雷波尼亚帝国旅行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '既是个有悠久历史的国家，\n',
            '值得去看的地方也不少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然一想到１０年前的事情，\n',
            '也会让人觉得有点恐怖……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7175')

    def _loc_7111(): pass

    label('loc_7111')

    ChrTalk(
        0x00FE,
        (
            '下一次，\n',
            '我想去埃雷波尼亚帝国旅行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然一想到１０年前的事情，\n',
            '也会让人觉得有点恐怖……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7175(): pass

    label('loc_7175')

    Jump('loc_7587')

    def _loc_7178(): pass

    label('loc_7178')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_71EE',
    )

    ChrTalk(
        0x00FE,
        (
            '没想到因为定期船失踪事件，\n',
            '我要长期滞留在这里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，正好趁此机会，\n',
            '可以放慢脚步，慢慢游玩了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7587')

    def _loc_71EE(): pass

    label('loc_71EE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_72B1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7269',
    )

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    ChrTalk(
        0x00FE,
        (
            '玛丽安所说的\n',
            '我也非常赞同。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '同样是军队，还是女王陛下的亲卫队\n',
            '礼仪更加端庄，举止更加优雅……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_72AE')

    def _loc_7269(): pass

    label('loc_7269')

    ChrTalk(
        0x00FE,
        (
            '同样是军队，还是女王陛下的亲卫队\n',
            '礼仪更加端庄，举止更加优雅……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_72AE(): pass

    label('loc_72AE')

    Jump('loc_7587')

    def _loc_72B1(): pass

    label('loc_72B1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_73BC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7353',
    )

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    ChrTalk(
        0x00FE,
        (
            '呵呵，\n',
            '玛丽安对美味的食物\n',
            '完全没有抵抗力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要听说有好吃的，\n',
            '就立刻会说\n',
            '『我们去尝尝吧』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为这样，\n',
            '我也没少跟着她饱口福。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_73B9')

    def _loc_7353(): pass

    label('loc_7353')

    ChrTalk(
        0x00FE,
        (
            '呵呵，\n',
            '玛丽安对美味的食物\n',
            '完全没有抵抗力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要听说有好吃的，\n',
            '就立刻会说\n',
            '『我们去尝尝吧』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_73B9(): pass

    label('loc_73B9')

    Jump('loc_7587')

    def _loc_73BC(): pass

    label('loc_73BC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_749E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7441',
    )

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    ChrTalk(
        0x00FE,
        (
            '这家店不仅是饭菜，\n',
            '工作人员的服务态度也非常好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你看看就知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '员工把老板的精神\n',
            '都传达到位了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_749B')

    def _loc_7441(): pass

    label('loc_7441')

    ChrTalk(
        0x00FE,
        (
            '这家店不仅是饭菜，\n',
            '工作人员的服务态度也非常好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '员工把老板的精神\n',
            '都传达到位了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_749B(): pass

    label('loc_749B')

    Jump('loc_7587')

    def _loc_749E(): pass

    label('loc_749E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_752C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_74F8',
    )

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    ChrTalk(
        0x00FE,
        (
            '真是太好吃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '格兰赛尔有没有\n',
            '能做出这样美味饭菜的店呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7529')

    def _loc_74F8(): pass

    label('loc_74F8')

    ChrTalk(
        0x00FE,
        (
            '格兰赛尔有没有\n',
            '能做出这样美味饭菜的店呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7529(): pass

    label('loc_7529')

    Jump('loc_7587')

    def _loc_752C(): pass

    label('loc_752C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_7587',
    )

    ChrTalk(
        0x00FE,
        (
            '我和玛丽安\n',
            '经常外出到各地去旅行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次，要我选择的话，\n',
            '我打算去超市购物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7587(): pass

    label('loc_7587')

    TalkEnd(0x0015)

    Return()

# id: 0x0015 offset: 0x758B
@scena.Code('func_15_758B')
def func_15_758B():
    TalkBegin(0x0016)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_7600',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_75DC',
    )

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))

    ChrTalk(
        0x00FE,
        (
            '我最喜欢的红酒\n',
            '终于进货了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我都等得不耐烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_75FD')

    def _loc_75DC(): pass

    label('loc_75DC')

    ChrTalk(
        0x00FE,
        (
            '我最喜欢的红酒\n',
            '终于进货了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_75FD(): pass

    label('loc_75FD')

    Jump('loc_7BFF')

    def _loc_7600(): pass

    label('loc_7600')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_76DB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7691',
    )

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))

    ChrTalk(
        0x00FE,
        (
            '只要去柏斯超市，\n',
            '就会想起以前的种种画面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在柏斯商人的血统\n',
            '仍然流淌在年轻人的身体里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我还是觉得很高兴的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_76D8')

    def _loc_7691(): pass

    label('loc_7691')

    ChrTalk(
        0x00FE,
        (
            '现在柏斯商人的血统\n',
            '仍然流淌在年轻人的身体里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我觉得很高兴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_76D8(): pass

    label('loc_76D8')

    Jump('loc_7BFF')

    def _loc_76DB(): pass

    label('loc_76DB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_7886',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7809',
    )

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))

    ChrTalk(
        0x00FE,
        (
            '百日战役时这座城市也成为了废墟，\n',
            '但它却是五大都市中\n',
            '最早复兴起来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '会这样也是有原因的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '商人们团结一心，集聚资金，\n',
            '使这个城市重新兴盛起来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '柏斯商人虽然崇尚自由，\n',
            '但是必要的时刻他们仍会团结一致……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我作为这座城市的商人，\n',
            '觉得能够生活在这里是一种骄傲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7883')

    def _loc_7809(): pass

    label('loc_7809')

    ChrTalk(
        0x00FE,
        (
            '柏斯商人虽然崇尚自由，\n',
            '但是必要的时刻他们仍会团结一致……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我作为这座城市的商人，\n',
            '觉得能够生活在这里是一种骄傲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7883(): pass

    label('loc_7883')

    Jump('loc_7BFF')

    def _loc_7886(): pass

    label('loc_7886')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_79E3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_797A',
    )

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))

    ChrTalk(
        0x00FE,
        (
            '超市变得正规和气派起来\n',
            '还是小姐的父亲当市长的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他推行了各种各样\n',
            '划时代的商业振兴政策。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且如今这些都被小姐\n',
            '继承和发展了下来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一开始觉得她太年轻，\n',
            '还有点看不起她。\n',
            '不过她的商业手段真是相当的厉害。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_79E0')

    def _loc_797A(): pass

    label('loc_797A')

    ChrTalk(
        0x00FE,
        (
            '超市变得正规和气派起来\n',
            '还是小姐的父亲当市长的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他推行了各种各样\n',
            '划时代的商业振兴政策。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_79E0(): pass

    label('loc_79E0')

    Jump('loc_7BFF')

    def _loc_79E3(): pass

    label('loc_79E3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_7B4E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7ADF',
    )

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))

    ChrTalk(
        0x00FE,
        (
            '在超市还没有建立起来的时候，\n',
            '那里有一个由空地上的小摊\n',
            '所组成的大型青空市场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那时商人的朝气和气派\n',
            '比现在还要高。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在有权势的商人如市长家，\n',
            '以及贸易商人特里诺家、博尔德家……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他们都是从那个青空市场\n',
            '开始起家的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7B4B')

    def _loc_7ADF(): pass

    label('loc_7ADF')

    ChrTalk(
        0x00FE,
        (
            '现在有权势的商人如市长家，\n',
            '以及贸易商人特里诺家、博尔德家……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他们都是从那个青空市场\n',
            '开始起家的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7B4B(): pass

    label('loc_7B4B')

    Jump('loc_7BFF')

    def _loc_7B4E(): pass

    label('loc_7B4E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_7B99',
    )

    ChrTalk(
        0x00FE,
        (
            '我年轻的时候\n',
            '也在柏斯超市做生意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在已经退休归隐啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7BFF')

    def _loc_7B99(): pass

    label('loc_7B99')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_7BFF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7BED',
    )

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))

    ChrTalk(
        0x00FE,
        (
            '呼～呼～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这烤鸭配上香菜，\n',
            '简直是太勾引人食欲了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7BFF')

    def _loc_7BED(): pass

    label('loc_7BED')

    ChrTalk(
        0x00FE,
        (
            '呼～呼～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7BFF(): pass

    label('loc_7BFF')

    TalkEnd(0x0016)

    Return()

# id: 0x0016 offset: 0x7C03
@scena.Code('func_16_7C03')
def func_16_7C03():
    TalkBegin(0x0017)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_7CE7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7C9E',
    )

    SetScenaFlags(ScenaFlag(0x0002, 0, 0x10))

    ChrTalk(
        0x00FE,
        (
            '啊呀，我觉得今天的汤\n',
            '和以前的味道不太一样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然有点粗糙，\n',
            '但是材料的风味都被活用了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '店里是不是\n',
            '来了新的厨师？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7CE4')

    def _loc_7C9E(): pass

    label('loc_7C9E')

    ChrTalk(
        0x00FE,
        (
            '今天的汤\n',
            '和以前的味道不太一样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '店里是不是\n',
            '来了新的厨师？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7CE4(): pass

    label('loc_7CE4')

    Jump('loc_808D')

    def _loc_7CE7(): pass

    label('loc_7CE7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_7D3D',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才，\n',
            '我在这里吃饭的时候……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总觉得桌子对面那个人\n',
            '在对着我微笑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_808D')

    def _loc_7D3D(): pass

    label('loc_7D3D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_7D96',
    )

    ChrTalk(
        0x00FE,
        (
            '只要一看到街上有穿着军服的人，\n',
            '我就会回忆起过去的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好痛苦啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_808D')

    def _loc_7D96(): pass

    label('loc_7D96')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_7E04',
    )

    ChrTalk(
        0x00FE,
        (
            '战争的时候，不只是这个城市，\n',
            '连拉文努村也受害了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和我怀有同样心情的人\n',
            '现在也会有很多吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_808D')

    def _loc_7E04(): pass

    label('loc_7E04')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_7F24',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7EC3',
    )

    SetScenaFlags(ScenaFlag(0x0002, 0, 0x10))

    ChrTalk(
        0x00FE,
        (
            '现在连帝国的人\n',
            '都可以来柏斯超市购物……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对我来说，这还真是让人百感交集的时代啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在那场战争中我最重要的亲人被夺去了性命，\n',
            '不管时代怎么变，历史是不会变的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7F21')

    def _loc_7EC3(): pass

    label('loc_7EC3')

    ChrTalk(
        0x00FE,
        (
            '现在这个年代，\n',
            '连帝国的人都可以\n',
            '来柏斯超市购物……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过对我来说，还真是百感交集啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7F21(): pass

    label('loc_7F21')

    Jump('loc_808D')

    def _loc_7F24(): pass

    label('loc_7F24')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_7F78',
    )

    ChrTalk(
        0x00FE,
        (
            '以前和老伴\n',
            '经常来这家饭店……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……是啊，\n',
            '那已经是十年前的事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_808D')

    def _loc_7F78(): pass

    label('loc_7F78')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_808D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8031',
    )

    SetScenaFlags(ScenaFlag(0x0002, 0, 0x10))

    ChrTalk(
        0x00FE,
        (
            '嗯，这里的饭菜\n',
            '还是和以前一样无可挑剔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然我听说几年前\n',
            '这里的老板换了，\n',
            '但是我还是很放心地来这里吃饭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我甚至觉得换了老板之后，\n',
            '饭菜的味道更好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_808D')

    def _loc_8031(): pass

    label('loc_8031')

    ChrTalk(
        0x00FE,
        (
            '嗯，这里的饭菜\n',
            '还是和以前一样无可挑剔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里换了老板之后，\n',
            '饭菜的味道更加美味了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_808D(): pass

    label('loc_808D')

    TalkEnd(0x0017)

    Return()

# id: 0x0017 offset: 0x8091
@scena.Code('func_17_8091')
def func_17_8091():
    TalkBegin(0x0018)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_80E4',
    )

    ChrTalk(
        0x00FE,
        (
            '哈啊……\n',
            '谈判又失败了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我好像真的不适合\n',
            '和别人谈生意呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_82D9')

    def _loc_80E4(): pass

    label('loc_80E4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_811D',
    )

    ChrTalk(
        0x00FE,
        (
            '也、也没有办法啊。\n',
            '那么您看这个价格如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_82D9')

    def _loc_811D(): pass

    label('loc_811D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_8162',
    )

    ChrTalk(
        0x00FE,
        (
            '哈啊……\n',
            '人际关系真的好难协调啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我真没用啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_82D9')

    def _loc_8162(): pass

    label('loc_8162')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_81D1',
    )

    ChrTalk(
        0x00FE,
        (
            '不不不，\n',
            '不管怎么样\n',
            '请接受这个价格吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我的上司\n',
            '是这么要求我的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请您一定要帮帮忙！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_82D9')

    def _loc_81D1(): pass

    label('loc_81D1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_8231',
    )

    ChrTalk(
        0x00FE,
        (
            '不不不，\n',
            '我非常明白你们的感受。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，作为我这一方，\n',
            '也要秉持商会的方针……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_82D9')

    def _loc_8231(): pass

    label('loc_8231')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_826E',
    )

    ChrTalk(
        0x00FE,
        (
            '不行，这已经突破底线了。\n',
            '这个价格我不能让步。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_82D9')

    def _loc_826E(): pass

    label('loc_826E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_82D9',
    )

    ChrTalk(
        0x00FE,
        (
            '由于军队的监控以及飞艇的停航，\n',
            '造成了范围很广的影响。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果不赶快重开\n',
            '这次交易谈判的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_82D9(): pass

    label('loc_82D9')

    TalkEnd(0x0018)

    Return()

# id: 0x0018 offset: 0x82DD
@scena.Code('func_18_82DD')
def func_18_82DD():
    TalkBegin(0x0019)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_8406',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 2, 0x12)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_83B1',
    )

    SetScenaFlags(ScenaFlag(0x0002, 2, 0x12))

    ChrTalk(
        0x00FE,
        (
            '虽然本来想跟您谈一下\n',
            '关于街道封锁时的流通问题……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过不知道什么时候\n',
            '所有的封锁都已经被解除了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '商人要敏锐地把握商机……\n',
            '这是我的座右铭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，\n',
            '一不小心就沉迷于谈判了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8403')

    def _loc_83B1(): pass

    label('loc_83B1')

    ChrTalk(
        0x00FE,
        (
            '商人要敏锐地把握商机……\n',
            '这是我的座右铭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，\n',
            '一不小心就沉迷于谈判了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8403(): pass

    label('loc_8403')

    Jump('loc_865A')

    def _loc_8406(): pass

    label('loc_8406')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_8436',
    )

    ChrTalk(
        0x00FE,
        (
            '呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然没有什么不好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_865A')

    def _loc_8436(): pass

    label('loc_8436')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_84A2',
    )

    ChrTalk(
        0x00FE,
        (
            '一味地逼迫对方，\n',
            '是不会在谈判中取得好结果的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '根据情况的不同\n',
            '来随机应变也是十分重要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_865A')

    def _loc_84A2(): pass

    label('loc_84A2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_8519',
    )

    ChrTalk(
        0x00FE,
        (
            '不不不，\n',
            '照你这么说的话，\n',
            '我这边的损失也可能扩大。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然这么说，\n',
            '不过采取更灵活的应对方式也很重要。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_865A')

    def _loc_8519(): pass

    label('loc_8519')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_8582',
    )

    ChrTalk(
        0x00FE,
        (
            '不不不，\n',
            '我们更重视\n',
            '长期的数值变化……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '应该把眼光放长远，\n',
            '考虑到飞艇复航之后的情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_865A')

    def _loc_8582(): pass

    label('loc_8582')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_85E8',
    )

    ChrTalk(
        0x00FE,
        (
            '不行不行，这个数字\n',
            '我们商会是无论如何也不接受的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对你来说，\n',
            '这也不是闹着玩的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_865A')

    def _loc_85E8(): pass

    label('loc_85E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_865A',
    )

    ChrTalk(
        0x00FE,
        (
            '柏斯能出售的商品\n',
            '变得越来越少了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '得想个办法才行，\n',
            '就算不能回避这种状况，\n',
            '至少能够做到缓和一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_865A(): pass

    label('loc_865A')

    TalkEnd(0x0019)

    Return()

# id: 0x0019 offset: 0x865E
@scena.Code('func_19_865E')
def func_19_865E():
    TalkBegin(0x001A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_86E4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 3, 0x13)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_86BA',
    )

    SetScenaFlags(ScenaFlag(0x0002, 3, 0x13))

    ChrTalk(
        0x00FE,
        (
            '因为太紧张了，\n',
            '都没有品尝出什么味道来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉～\n',
            '真是可惜啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_86E1')

    def _loc_86BA(): pass

    label('loc_86BA')

    ChrTalk(
        0x00FE,
        (
            '下次来的时候\n',
            '一定要仔细品味一番。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_86E1(): pass

    label('loc_86E1')

    Jump('loc_880D')

    def _loc_86E4(): pass

    label('loc_86E4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_8799',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 3, 0x13)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8759',
    )

    SetScenaFlags(ScenaFlag(0x0002, 3, 0x13))

    ChrTalk(
        0x00FE,
        (
            '我、我穿了最漂亮的衣服过来，\n',
            '但会不会感觉很奇怪？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我一定要小心\n',
            '不要让餐具掉在地上……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8796')

    def _loc_8759(): pass

    label('loc_8759')

    ChrTalk(
        0x00FE,
        (
            '哈啊，我这种在低下阶层的人\n',
            '穿这种服装还真是有点不搭配。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8796(): pass

    label('loc_8796')

    Jump('loc_880D')

    def _loc_8799(): pass

    label('loc_8799')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_87E8',
    )

    ChrTalk(
        0x00FE,
        (
            '其、其实我是第一次\n',
            '来这种高档的地方吃饭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是紧张死了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_880D')

    def _loc_87E8(): pass

    label('loc_87E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_880D',
    )

    ChrTalk(
        0x00FE,
        (
            '那、那么我们点些什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_880D(): pass

    label('loc_880D')

    TalkEnd(0x001A)

    Return()

# id: 0x001A offset: 0x8811
@scena.Code('func_1A_8811')
def func_1A_8811():
    TalkBegin(0x001B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_88F9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 4, 0x14)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_88AC',
    )

    SetScenaFlags(ScenaFlag(0x0002, 4, 0x14))

    ChrTalk(
        0x00FE,
        (
            '啊～真是太好吃了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不愧是被称为\n',
            '利贝尔首屈一指的饭店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '存钱来这里吃饭\n',
            '真是太值了㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '偶尔这样奢侈一次\n',
            '也不错嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_88F6')

    def _loc_88AC(): pass

    label('loc_88AC')

    ChrTalk(
        0x00FE,
        (
            '不愧是被称为\n',
            '利贝尔首屈一指的饭店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '存钱来这里吃饭\n',
            '真是太值了㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_88F6(): pass

    label('loc_88F6')

    Jump('loc_89F9')

    def _loc_88F9(): pass

    label('loc_88F9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_895F',
    )

    ChrTalk(
        0x00FE,
        (
            '我们在很久以前，\n',
            '就想来这里吃一顿饭……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '两个人拼命努力地打工赚钱\n',
            '才能来到这里的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_89F9')

    def _loc_895F(): pass

    label('loc_895F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_899A',
    )

    ChrTalk(
        0x00FE,
        (
            '我说，别低着头弓着腰啦。\n',
            '应该更放松一点嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_89F9')

    def _loc_899A(): pass

    label('loc_899A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_89F9',
    )

    ChrTalk(
        0x00FE,
        (
            '啊～果然如传闻一样，\n',
            '是一家很豪华的酒店啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '之前我都只敢\n',
            '在外面偷偷往里面看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_89F9(): pass

    label('loc_89F9')

    TalkEnd(0x001B)

    Return()

# id: 0x001B offset: 0x89FD
@scena.Code('func_1B_89FD')
def func_1B_89FD():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(-35680, 1500, 4059, 0)
    OP_67(0, 7500, -10000, 0)
    ClearChrFlags(0x0008, 0x0080)
    TerminateThread(0x0008, 0xFF)
    SetChrFlags(0x0101, 0x0004)
    SetChrFlags(0x0102, 0x0004)
    SetChrFlags(0x0103, 0x0004)
    SetChrFlags(0x0134, 0x0004)
    SetChrFlags(0x0008, 0x0004)
    SetChrPos(0x0101, -53630, 1700, 4200, 270)
    SetChrPos(0x0102, -54880, 1700, 2840, 0)
    SetChrPos(0x0103, -54970, 1700, 5580, 180)
    SetChrPos(0x0008, -56300, 1700, 4200, 90)
    SetChrPos(0x0134, -56990, 1500, 5470, 135)
    SetChrChipByIndex(0x0101, 20)
    SetChrChipByIndex(0x0102, 21)
    SetChrChipByIndex(0x0103, 22)
    FadeIn(2000, 0)
    CameraMove(-55280, 1700, 4240, 6000)

    ChrTalk(
        0x0101,
        (
            '#0010020579V#004F好、好豪华的饭店啊……\n',
            '就在这种地方商量吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360020580V#610F就在这里慢慢谈吧。\n',
            '这里菜色风味独特，味道也相当不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020581V#020F可是，虽然柏斯市长\n',
            '是位女性的事我早有耳闻……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020582V但没想到竟然如此年轻呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020583V#000F刚见面的时候，\n',
            '我觉得最多只和我相差四五岁的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360020584V#611F实际上也不过是初出茅庐的年轻人而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360020585V我只是一并继承了已亡故的父亲\n',
            '作为柏斯市长和柏斯超市业主的\n',
            '政治及商业地位而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020586V#010F怎么说呢……\n',
            '真是坦率的自我评价啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360020587V#610F毕竟是商人的女儿嘛，\n',
            '不擅长装腔作势那一套。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360020588V那么我们现在再确认一下\n',
            '委托的内容吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020589V#006F嗯，没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360020590V#612F不用说，我委托的正是\n',
            '调查和解决失踪定期船的事件。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360020591V我认为像这次这样的事件，\n',
            '游击士协会的各位会比起军方\n',
            '更能找出事件的真相。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360020592V因为不是要进行战争，\n',
            '而是要揭开事件的迷雾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020593V#027F啊，真荣幸。\n',
            '市长您太看得起我们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360020594V#611F所谓商人就是要有敏锐的眼光嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360020595V#615F实际上，失踪定期船的乘客中\n',
            '有一位在柏斯很有影响力的商人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360020596V如果持续目前的状况，\n',
            '王国军在柏斯上空继续实行飞行管制的话，\n',
            '这里的商业交易就没办法进行下去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360020597V在女王诞辰庆典之前，\n',
            '难得市场的景气好了起来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020598V#012F原来如此。\n',
            '是出于经济的考量吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360020599V#612F可以这样说吧，\n',
            '不能只让军队方面负责这件事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360020600V怎么样，愿意接受我的委托吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020601V#025F虽然我们这边也有\n',
            '要接受这个委托的理由……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020602V但是关于这个事件，\n',
            '军方已经把游击士协会排斥在外，\n',
            '所以我们现在也无法展开调查工作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020603V#020F您能不能以市长的立场\n',
            '给我们的工作一些支持呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360020604V#612F是摩尔根将军吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360020605V那位将军，\n',
            '从很早以前就非常讨厌游击士了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020606V#004F哎？\n',
            '市长姐姐也认识那个摩尔根将军？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360020607V#610F他是我去世父亲的朋友。\n',
            '所以曾经见过几次面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360020608V因此……\n',
            '说不定我能帮你们一些忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020609V#014F您的意思是……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0008, 1)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0360020610V#610F莉拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0134,
        (
            '#0370020611V#620F是，小姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0134, -56110, 1500, 4980, 2000, 0x00)
    ChrTurnDirection(0x0134, 0x0008, 400)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '莉拉从怀中拿出钢笔和信纸，\n',
            '递给了梅贝尔市长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetChrSubChip(0x0008, 0)
    Sleep(200)

    SetChrDirection(0x0134, 315, 400)
    ChrMoveTo(0x0134, -56990, 1500, 5470, 2000, 0x00)
    SetChrDirection(0x0134, 135, 400)

    ChrTalk(
        0x0008,
        (
            '#0360020612V#612F……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360020613V……………………………\n',
            '……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360020614V#615F……这样应该可以了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360020615V#610F那么，你们拿着吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    AddItem(0x032D, 1)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '梅贝尔市长的信',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#0010020616V#000F这封信，是做什么的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360020617V#610F是给摩尔根将军的委托信。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360020618V我以柏斯地区的负责人身份，\n',
            '向摩尔根将军申请\n',
            '获得这次事件的相关情报。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360020619V我想，从某种程度来说，\n',
            '你们应该可以获得军方掌握的情报吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020620V#002F原来是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020621V可是，那个讨厌游击士的将军\n',
            '会不会见我们呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360020622V#610F当然，各位只要隐瞒一下\n',
            '游击士的身份就没问题了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360020623V你们仅以市长使者的名义\n',
            '去拜见他就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020624V#003F唔，感觉有点不爽。\n',
            '好像我们是骗子似的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020625V#010F我们这么做可不是骗人啊。\n',
            '只是没把所有事都和盘托出而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020020626V因为我们必须争分夺秒，\n',
            '这次就暂时委屈一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020627V#007F嗯～说的也是呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020628V#000F话说回来，\n',
            '到哪里能找到摩尔根将军呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360020629V#610F柏斯北面，帝国方向的边境\n',
            '有座被称为『哈肯大门』的堡垒。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360020630V摩尔根将军就在那里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    FormationDelMember(0x33, 0xFF)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T1101._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x001C offset: 0x96BD
@scena.Code('func_1C_96BD')
def func_1C_96BD():
    Sleep(500)

    SetChrSubChip(0x0102, 0)
    Sleep(200)

    SetChrSubChip(0x0103, 0)
    Sleep(200)

    SetChrSubChip(0x0101, 1)
    Sleep(200)

    SetChrSubChip(0x0102, 1)
    Sleep(200)

    SetChrSubChip(0x0103, 2)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

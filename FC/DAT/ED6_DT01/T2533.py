import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2533_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2533   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '乔儿'),
    TXT(0x02, '汉斯'),
    TXT(0x03, '拉迪奥老师'),
    TXT(0x04, '碧欧拉老师'),
    TXT(0x05, '米丽亚老师'),
    TXT(0x06, '艾福托老师'),
    TXT(0x07, '罗迪'),
    TXT(0x08, '米克'),
    TXT(0x09, '米克'),
    TXT(0x0A, '雅莉丝'),
    TXT(0x0B, '帕布尔'),
    TXT(0x0C, '黛拉'),
    TXT(0x0D, '罗基克'),
    TXT(0x0E, '亚吉鲁'),
    TXT(0x0F, '罗伊斯'),
    TXT(0x10, '莫妮卡'),
    TXT(0x11, '塞尔玛'),
    TXT(0x12, '莉秋尔'),
    TXT(0x13, '巴托姆'),
    TXT(0x14, '基诺奇奥'),
    TXT(0x15, '德尼斯'),
    TXT(0x16, '妮吉塔'),
    TXT(0x17, '芙拉瑟'),
    TXT(0x18, '蕾娜'),
    TXT(0x19, '勤务员巴克斯'),
    TXT(0x1A, '侍女蕾妮'),
    TXT(0x1B, '侍女玲珐'),
    TXT(0x1C, '拉多公爵'),
    TXT(0x1D, '科洛多议长'),
    TXT(0x1E, '王都的主教'),
    TXT(0x1F, '暗杀者'),
    TXT(0x20, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2533.x'
    header.mapIndex       = 1
    header.bgm            = 14
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x38B0
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
        ('ED6_DT07/CH02390._CH', 'ED6_DT07/CH02390P._CP'),
        ('ED6_DT07/CH02550._CH', 'ED6_DT07/CH02550P._CP'),
        ('ED6_DT07/CH01660._CH', 'ED6_DT07/CH01660P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH01430._CH', 'ED6_DT07/CH01430P._CP'),
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
        ('ED6_DT07/CH01360._CH', 'ED6_DT07/CH01360P._CP'),
        ('ED6_DT07/CH01080._CH', 'ED6_DT07/CH01080P._CP'),
        ('ED6_DT07/CH01580._CH', 'ED6_DT07/CH01580P._CP'),
        ('ED6_DT07/CH01590._CH', 'ED6_DT07/CH01590P._CP'),
        ('ED6_DT07/CH01090._CH', 'ED6_DT07/CH01090P._CP'),
        ('ED6_DT07/CH01370._CH', 'ED6_DT07/CH01370P._CP'),
        ('ED6_DT07/CH01080._CH', 'ED6_DT07/CH01080P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH02260._CH', 'ED6_DT07/CH02260P._CP'),
        ('ED6_DT07/CH02270._CH', 'ED6_DT07/CH02270P._CP'),
        ('ED6_DT07/CH02280._CH', 'ED6_DT07/CH02280P._CP'),
        ('ED6_DT07/CH01350._CH', 'ED6_DT07/CH01350P._CP'),
        ('ED6_DT07/CH02540._CH', 'ED6_DT07/CH02540P._CP'),
        ('ED6_DT07/CH01220._CH', 'ED6_DT07/CH01220P._CP'),
        ('ED6_DT07/CH01570._CH', 'ED6_DT07/CH01570P._CP'),
        ('ED6_DT07/CH01670._CH', 'ED6_DT07/CH01670P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT06/CH20069._CH', 'ED6_DT06/CH20069P._CP'),
        ('ED6_DT06/CH20071._CH', 'ED6_DT06/CH20071P._CP'),
    ]

# id: 0x10002 offset: 0x172
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 59640,
            z                   = 1000,
            y                   = 13450,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0019,
        ),
        ScenaNpcData(
            x                   = 66040,
            z                   = 1000,
            y                   = 16210,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001A,
        ),
        ScenaNpcData(
            x                   = -500,
            z                   = 0,
            y                   = 9300,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            x                   = -6300,
            z                   = 0,
            y                   = 300,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 5900,
            z                   = 0,
            y                   = 3800,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = -4100,
            z                   = 0,
            y                   = -4200,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = -6300,
            z                   = 0,
            y                   = 6900,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = -4600,
            z                   = 0,
            y                   = 7500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = -3700,
            z                   = 0,
            y                   = 5900,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = -5700,
            z                   = 0,
            y                   = 4500,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = -2000,
            z                   = 0,
            y                   = 7200,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = -500,
            z                   = 0,
            y                   = 6700,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = -4000,
            z                   = 0,
            y                   = 2800,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            x                   = -1900,
            z                   = 0,
            y                   = -1700,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            x                   = -1000,
            z                   = 0,
            y                   = 1200,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            x                   = -2800,
            z                   = 0,
            y                   = 900,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = -5400,
            z                   = 0,
            y                   = -2300,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            x                   = -1500,
            z                   = 0,
            y                   = 2700,
            direction           = 270,
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
            x                   = 3400,
            z                   = 0,
            y                   = 3800,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            x                   = 4400,
            z                   = 0,
            y                   = 200,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            x                   = 3100,
            z                   = 0,
            y                   = 1700,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            x                   = 1900,
            z                   = 0,
            y                   = 200,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0016,
        ),
        ScenaNpcData(
            x                   = 2000,
            z                   = 0,
            y                   = 6000,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0017,
        ),
        ScenaNpcData(
            x                   = 4000,
            z                   = 0,
            y                   = 6000,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0018,
        ),
        ScenaNpcData(
            x                   = 1780,
            z                   = 0,
            y                   = -1860,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001B,
        ),
        ScenaNpcData(
            x                   = 61850,
            z                   = 1000,
            y                   = 17310,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 63320,
            z                   = 1000,
            y                   = 15250,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 57740,
            z                   = 1000,
            y                   = 16980,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 58590,
            z                   = 1000,
            y                   = 17010,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 59600,
            z                   = 1000,
            y                   = 16379,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 56830,
            z                   = 1000,
            y                   = 16500,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x552
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x552
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x552
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x552
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_55C',
    )

    Jump('loc_652')

    def _loc_55C(): pass

    label('loc_55C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_600',
    )

    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
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
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 320, 0, 4890, 0)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, -1040, 0, 4970, 0)

    Jump('loc_652')

    def _loc_600(): pass

    label('loc_600')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_60A',
    )

    Jump('loc_652')

    def _loc_60A(): pass

    label('loc_60A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_614',
    )

    Jump('loc_652')

    def _loc_614(): pass

    label('loc_614')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_61E',
    )

    Jump('loc_652')

    def _loc_61E(): pass

    label('loc_61E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_62D',
    )

    ClearChrFlags(0x0020, 0x0080)

    Jump('loc_652')

    def _loc_62D(): pass

    label('loc_62D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 6, 0x42E)),
            Expr.Return,
        ),
        'loc_637',
    )

    Jump('loc_652')

    def _loc_637(): pass

    label('loc_637')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_641',
    )

    Jump('loc_652')

    def _loc_641(): pass

    label('loc_641')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 6, 0x41E)),
            Expr.Return,
        ),
        'loc_64B',
    )

    Jump('loc_652')

    def _loc_64B(): pass

    label('loc_64B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_652',
    )

    def _loc_652(): pass

    label('loc_652')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_660',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x001C)

    def _loc_660(): pass

    label('loc_660')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_677',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, 0x001D)

    def _loc_677(): pass

    label('loc_677')

    Return()

# id: 0x0001 offset: 0x678
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Or,
            Expr.Return,
        ),
        'loc_699',
    )

    OP_B1('t2533_y')

    Jump('loc_6A2')

    def _loc_699(): pass

    label('loc_699')

    OP_B1('t2533_n')

    def _loc_6A2(): pass

    label('loc_6A2')

    Return()

# id: 0x0002 offset: 0x6A3
@scena.Code('ReInit')
def ReInit():
    ExecExpressionWithReg(
        0x0000,
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
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6C8',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_80A')

    def _loc_6C8(): pass

    label('loc_6C8')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6E1',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_80A')

    def _loc_6E1(): pass

    label('loc_6E1')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6FA',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_80A')

    def _loc_6FA(): pass

    label('loc_6FA')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_713',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_80A')

    def _loc_713(): pass

    label('loc_713')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_72C',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_80A')

    def _loc_72C(): pass

    label('loc_72C')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_745',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_80A')

    def _loc_745(): pass

    label('loc_745')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_75E',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_80A')

    def _loc_75E(): pass

    label('loc_75E')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_777',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_80A')

    def _loc_777(): pass

    label('loc_777')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_790',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_80A')

    def _loc_790(): pass

    label('loc_790')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7A9',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_80A')

    def _loc_7A9(): pass

    label('loc_7A9')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7C2',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_80A')

    def _loc_7C2(): pass

    label('loc_7C2')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7DB',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_80A')

    def _loc_7DB(): pass

    label('loc_7DB')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7F4',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_80A')

    def _loc_7F4(): pass

    label('loc_7F4')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_80A',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_80A(): pass

    label('loc_80A')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_81F',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_80A')

    def _loc_81F(): pass

    label('loc_81F')

    Return()

# id: 0x0003 offset: 0x820
@scena.Code('func_03_820')
def func_03_820():
    TalkBegin(0x000A)

    ChrTalk(
        0x00FE,
        (
            '各位老师和同学\n',
            '真的是辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次学园祭\n',
            '没有辜负王立学院的盛名。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000A)

    Return()

# id: 0x0004 offset: 0x873
@scena.Code('func_04_873')
def func_04_873():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8BF',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '呵呵，\n',
            '大家真是辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '每个人都尽全力努力了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8EC')

    def _loc_8BF(): pass

    label('loc_8BF')

    ChrTalk(
        0x00FE,
        (
            '这次结束后，\n',
            '就和米丽亚一起去城里玩吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8EC(): pass

    label('loc_8EC')

    TalkEnd(0x000B)

    Return()

# id: 0x0005 offset: 0x8F0
@scena.Code('func_05_8F0')
def func_05_8F0():
    TalkBegin(0x000C)

    ChrTalk(
        0x00FE,
        (
            '嗯，\n',
            '大家都干得很不错呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算他们合格了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000C)

    Return()

# id: 0x0006 offset: 0x92E
@scena.Code('func_06_92E')
def func_06_92E():
    TalkBegin(0x000D)

    ChrTalk(
        0x00FE,
        (
            '能顺利地完成真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明天开始大家\n',
            '还是要努力学习哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000D)

    Return()

# id: 0x0007 offset: 0x978
@scena.Code('func_07_978')
def func_07_978():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9BD',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '好，庆祝吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家痛快地玩吧，痛快地玩吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9F6')

    def _loc_9BD(): pass

    label('loc_9BD')

    ChrTalk(
        0x00FE,
        (
            '明天开始又要上课了，\n',
            '现实在等着我们呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9F6(): pass

    label('loc_9F6')

    TalkEnd(0x000E)

    Return()

# id: 0x0008 offset: 0x9FA
@scena.Code('func_08_9FA')
def func_08_9FA():
    TalkBegin(0x000F)

    ChrTalk(
        0x00FE,
        (
            '学园祭已经结束了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那干嘛还要特地\n',
            '聚在一起那么吵闹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我好想快点回去啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000F)

    Return()

# id: 0x0009 offset: 0xA5A
@scena.Code('func_09_A5A')
def func_09_A5A():
    TalkBegin(0x0010)

    ChrTalk(
        0x00FE,
        (
            '好像失去了什么的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，为学园祭做准备的\n',
            '那段时间是最快乐的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0010)

    Return()

# id: 0x000A offset: 0xAAE
@scena.Code('func_0A_AAE')
def func_0A_AAE():
    TalkBegin(0x0011)

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，\n',
            '庆祝胜利真是好开心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0011)

    Return()

# id: 0x000B offset: 0xAD8
@scena.Code('func_0B_AD8')
def func_0B_AD8():
    TalkBegin(0x0012)

    ChrTalk(
        0x00FE,
        (
            '准备花了那么多时间，\n',
            '今天却是一眨眼就过去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '客人们看起来很高兴啊。\n',
            '我自己也很高兴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0012)

    Return()

# id: 0x000C offset: 0xB46
@scena.Code('func_0C_B46')
def func_0C_B46():
    TalkBegin(0x0013)

    ChrTalk(
        0x00FE,
        (
            '这几天虽然很忙，\n',
            '但我很努力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还是很有成就感的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0013)

    Return()

# id: 0x000D offset: 0xB88
@scena.Code('func_0D_B88')
def func_0D_B88():
    TalkBegin(0x0014)

    ChrTalk(
        0x00FE,
        (
            '我家在卢安，\n',
            '好想提前回去呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过今天就趁着余兴一起庆祝吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0014)

    Return()

# id: 0x000E offset: 0xBD8
@scena.Code('func_0E_BD8')
def func_0E_BD8():
    TalkBegin(0x0015)

    ChrTalk(
        0x00FE,
        (
            '顺利地结束了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0015)

    Return()

# id: 0x000F offset: 0xBF7
@scena.Code('func_0F_BF7')
def func_0F_BF7():
    TalkBegin(0x0016)

    ChrTalk(
        0x00FE,
        (
            '击剑部的冰淇淋店\n',
            '反响十分好哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我很高兴，\n',
            '因为来学园祭的孩子们那么开心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0016)

    Return()

# id: 0x0010 offset: 0xC52
@scena.Code('func_10_C52')
def func_10_C52():
    TalkBegin(0x0017)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CF3',
    )

    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    ChrTalk(
        0x00FE,
        (
            '嘿嘿。\n',
            '啊，好开心啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，学园祭……\n',
            '因为一年只有一次，\n',
            '大家齐心协力做这件事才会十分开心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是每天都这样，\n',
            '大家一定会累死了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D0E')

    def _loc_CF3(): pass

    label('loc_CF3')

    ChrTalk(
        0x00FE,
        (
            '嘿嘿。\n',
            '啊，好开心啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D0E(): pass

    label('loc_D0E')

    TalkEnd(0x0017)

    Return()

# id: 0x0011 offset: 0xD12
@scena.Code('func_11_D12')
def func_11_D12():
    TalkBegin(0x0018)

    ChrTalk(
        0x00FE,
        (
            '呵呵，\n',
            '真是个不能不参加的活动呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家都尽力了，\n',
            '这就是最好的结局。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0018)

    Return()

# id: 0x0012 offset: 0xD67
@scena.Code('func_12_D67')
def func_12_D67():
    TalkBegin(0x0019)

    ChrTalk(
        0x00FE,
        (
            '啊，是前辈们呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不论舞台剧还是冰淇淋店都很成功。\n',
            '莉秋尔，非常开心呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0019)

    Return()

# id: 0x0013 offset: 0xDBF
@scena.Code('func_13_DBF')
def func_13_DBF():
    TalkBegin(0x001A)

    ChrTalk(
        0x00FE,
        (
            '哈哈，我也非常开心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '舞台剧也非常好哦。\n',
            '真是辛苦大家了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x001A)

    Return()

# id: 0x0014 offset: 0xE09
@scena.Code('func_14_E09')
def func_14_E09():
    TalkBegin(0x001B)

    ChrTalk(
        0x00FE,
        (
            '呼，好累呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '快点回家睡觉吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x001B)

    Return()

# id: 0x0015 offset: 0xE38
@scena.Code('func_15_E38')
def func_15_E38():
    TalkBegin(0x001C)

    ChrTalk(
        0x00FE,
        (
            '嗯，\n',
            '今天不看书也不要紧吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为我有\n',
            '平时的积累啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x001C)

    Return()

# id: 0x0016 offset: 0xE7D
@scena.Code('func_16_E7D')
def func_16_E7D():
    TalkBegin(0x001D)

    ChrTalk(
        0x00FE,
        (
            '真是的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '基诺奇奥\n',
            '就只会打哈欠……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x001D)

    Return()

# id: 0x0017 offset: 0xEB3
@scena.Code('func_17_EB3')
def func_17_EB3():
    TalkBegin(0x001E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 4, 0x14)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F55',
    )

    SetScenaFlags(ScenaFlag(0x0002, 4, 0x14))
    SetScenaFlags(ScenaFlag(0x0002, 5, 0x15))

    ChrTalk(
        0x001E,
        (
            '真是的，都怪你，\n',
            '让我忙得焦头烂额。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001E,
        (
            '老爷子也很\n',
            '感谢你们呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '呵呵，得到你的夸奖真是光荣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '我只是为了\n',
            '锻炼芙拉瑟你嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x001F, 0x0010)

    Jump('loc_FAE')

    def _loc_F55(): pass

    label('loc_F55')

    ChrTalk(
        0x001E,
        (
            '唉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '哎呀，你为什么叹气啊？\n',
            '有烦恼的话可以和我谈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001E,
        (
            '求你了，放过我吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FAE(): pass

    label('loc_FAE')

    TalkEnd(0x001E)

    Return()

# id: 0x0018 offset: 0xFB2
@scena.Code('func_18_FB2')
def func_18_FB2():
    TalkBegin(0x001F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 5, 0x15)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1054',
    )

    SetScenaFlags(ScenaFlag(0x0002, 4, 0x14))
    SetScenaFlags(ScenaFlag(0x0002, 5, 0x15))

    ChrTalk(
        0x001E,
        (
            '真是的，都怪你，\n',
            '让我忙得焦头烂额。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001E,
        (
            '老爷子也很\n',
            '感谢你们呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '呵呵，得到你的夸奖真是光荣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '我只是为了\n',
            '锻炼芙拉瑟你嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x001F, 0x0010)

    Jump('loc_1064')

    def _loc_1054(): pass

    label('loc_1054')

    ChrTalk(
        0x00FE,
        (
            '呵呵呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1064(): pass

    label('loc_1064')

    TalkEnd(0x001F)

    Return()

# id: 0x0019 offset: 0x1068
@scena.Code('func_19_1068')
def func_19_1068():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 6, 0x16)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_10EF',
    )

    SetScenaFlags(ScenaFlag(0x0002, 6, 0x16))

    ChrTalk(
        0x00FE,
        (
            '#0510060932V#640F哎？\n',
            '你们还在这里啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510060933V不赶快回到卢安没有关系吗？\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510060934V如果想参加庆祝会的话十分欢迎哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1145')

    def _loc_10EF(): pass

    label('loc_10EF')

    ChrTalk(
        0x00FE,
        (
            '#0510060935V#640F不赶快回到卢安\n',
            '没有关系吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510060936V如果想参加庆祝会的话十分欢迎哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1145(): pass

    label('loc_1145')

    TalkEnd(0x0008)

    Return()

# id: 0x001A offset: 0x1149
@scena.Code('func_1A_1149')
def func_1A_1149():
    TalkBegin(0x0009)

    ChrTalk(
        0x00FE,
        (
            '#0520060937V#730F哦，\n',
            '你们是不是舍不得庆祝会啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520060938V今天全部由老师们请客呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0009)

    Return()

# id: 0x001B offset: 0x11A2
@scena.Code('func_1B_11A2')
def func_1B_11A2():
    TalkBegin(0x0020)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_11FD',
    )

    ChrTalk(
        0x00FE,
        (
            '这里只能在下午使用时才开放。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我现在正照科林兹校长的吩咐\n',
            '进行安全检查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11FD(): pass

    label('loc_11FD')

    TalkEnd(0x0020)

    Return()

# id: 0x001C offset: 0x1201
@scena.Code('func_1C_1201')
def func_1C_1201():
    EventBegin(0x00)
    OP_4A(0x0008, 255)
    OP_4A(0x0009, 255)
    CameraMove(-410, 4000, -4600, 0)
    OP_67(0, 5000, -10000, 0)
    CameraSetDistance(3720, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0101, 850, 1000, 14010, 270)
    SetChrPos(0x0105, -960, 1000, 14000, 90)
    SetChrPos(0x0008, -80, 1000, 13250, 0)
    SetChrChipByIndex(0x0101, 14)
    SetChrChipByIndex(0x0105, 15)
    SetChrChipByIndex(0x0102, 16)
    FadeIn(1000, 0)
    OP_13(0x005F)
    CameraMove(910, 2000, 12490, 4000)
    Fade(500)
    CameraMove(60050, 2310, 14620, 0)
    OP_67(0, 2930, -10000, 0)
    CameraSetDistance(1400, 0)
    OP_6C(0, 0)
    OP_6E(673, 0)
    SetChrFlags(0x0009, 0x0040)
    SetChrPos(0x0101, 61000, 1000, 14250, 225)
    SetChrPos(0x0105, 59080, 1000, 14210, 135)
    SetChrPos(0x0008, 60000, 1000, 13140, 45)
    SetChrPos(0x0102, 67180, 1000, 16860, 270)
    SetChrPos(0x0009, 67180, 1000, 16860, 270)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010051149V#340F#2P嗯～这就是戏服啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051150V刚才说要演骑士，\n',
            '我还以为要穿铠甲什么的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#644F#3P因为穿甲胄的话，\n',
            '会妨碍到演员动作的流畅度。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051152V所以我们就照现在\n',
            '王室亲卫队的制服式样设计了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051153V#340F#2P哦，是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051154V#341F科洛丝是短发，\n',
            '感觉正适合这角色呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051155V#351F#1P呵呵，谢谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051156V艾丝蒂尔也很适合呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051157V#348F#2P嘿嘿，是吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051158V对了……\n',
            '为什么我们的衣服颜色不同？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051159V#350F#1P我演的是\n',
            '平民的『苍骑士奥斯卡』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051160V艾丝蒂尔演的是\n',
            '贵族的『红骑士尤利乌斯』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051161V这是双方势力的代表色。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051162V#340F#2P哦～原来是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051163V那么，约修亚是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3P牵挂着两名骑士的\n',
            '王家『白色公主塞茜莉亚』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520051165V好了公主，请到这边来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#3P再、再等一下。\n',
            '……我还没做好心理准备………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_66(0x0000)

    @scena.Lambda('lambda_1656')
    def lambda_1656():
        CameraMove(61500, 2310, 14620, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1656)

    @scena.Lambda('lambda_166E')
    def lambda_166E():
        CameraSetDistance(850, 2500)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_166E)

    @scena.Lambda('lambda_167E')
    def lambda_167E():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_167E')

    DispatchAsync2(0x0101, 0x0001, lambda_167E)

    @scena.Lambda('lambda_168F')
    def lambda_168F():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_168F')

    DispatchAsync2(0x0105, 0x0001, lambda_168F)

    @scena.Lambda('lambda_16A0')
    def lambda_16A0():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_16A0')

    DispatchAsync2(0x0008, 0x0001, lambda_16A0)

    @scena.Lambda('lambda_16B1')
    def lambda_16B1():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_16B1')

    DispatchAsync2(0x0009, 0x0001, lambda_16B1)

    @scena.Lambda('lambda_16C2')
    def lambda_16C2():
        ChrMoveTo(0x00FE, 62850, 1000, 15120, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_16C2)

    Sleep(800)

    @scena.Lambda('lambda_16E2')
    def lambda_16E2():
        ChrMoveTo(0x00FE, 63260, 1000, 15870, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_16E2)

    WaitForThreadExit(0x0102, 0x0001)
    SetChrDirection(0x0102, 225, 0)
    WaitForThreadExit(0x0009, 0x0002)
    Sleep(200)

    ChrMoveTo(0x0009, 63580, 1000, 14220, 2000, 0x00)
    TerminateThread(0x0009, 0xFF)
    SetChrDirection(0x0009, 315, 0)

    ChrTalk(
        0x0102,
        (
            '#0020051167V#363F#2P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051168V#344F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051169V#354F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510051170V#643F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020051171V#367F#2P拜托了，说点什么吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020051172V在这种沉默的气氛\n',
            '呆呆地站着实在是有点……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051173V#340F哎呀，怎么说呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051174V#341F完全没有不协调的感觉⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051175V#351F我也吃了一惊呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051176V#358F啊啊，真的好漂亮……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520051177V#731F嗯嗯，自信一点啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520051178V假如你真的是女孩子，\n',
            '我恐怕会忍不住上来挑逗你哦㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1200)

    ChrTalk(
        0x0102,
        (
            '#0020051179V#368F#2P多谢你们真诚的感想。\n',
            '不过我可一点都高兴不起来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510051180V#659F哦呵呵……\n',
            '这就是我要的效果……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051181V这样的人选安排\n',
            '一定会受到各方面的认同……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051182V#641F各位，大家要团结一致，\n',
            '打造最完美的舞台剧哦～！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#341F#1P#1K好～！',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x0105,
        (
            '#351F#1K是！',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x0009,
        (
            '#731F#1K喔！',
            TxtCtl.Enter,
        ),
    )

    Sleep(500)

    OP_56(0x01)

    ChrTalk(
        0x0102,
        (
            '#0020051186V#367F#2P咳咳……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    FadeOut(1500, 0, -1)
    OP_0D()
    OP_21()
    Sleep(500)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '由当晚开始，艾丝蒂尔和约修亚\n',
            '分别住进了学院的女生宿舍和男生宿舍。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_66(0x0001)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T2512._SN', 115, 0, 0)
    IdleLoop()

    Return()

# id: 0x001D offset: 0x1AEF
@scena.Code('func_1D_1AEF')
def func_1D_1AEF():
    EventBegin(0x00)
    FadeOut(0, 0, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '之后，学园祭的前一天——',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    CameraMove(60050, 2310, 14620, 0)
    OP_67(0, 2930, -10000, 0)
    CameraSetDistance(1400, 0)
    OP_6C(0, 0)
    OP_6E(673, 0)
    SetChrFlags(0x0008, 0x0080)
    SetChrPos(0x0009, 610, 0, -360, 0)
    SetChrPos(0x0102, -400, 0, 430, 0)
    SetChrFlags(0x0021, 0x0080)
    SetChrFlags(0x0022, 0x0080)
    SetChrFlags(0x0023, 0x0080)
    SetChrFlags(0x0024, 0x0080)
    SetChrFlags(0x0025, 0x0080)
    SetChrFlags(0x0026, 0x0080)
    SetChrChipByIndex(0x0101, 14)
    SetChrChipByIndex(0x0105, 15)
    SetChrSubChip(0x0101, 0)
    SetChrSubChip(0x0105, 0)
    SetChrPos(0x0101, 62000, 1000, 14000, 270)
    SetChrPos(0x0105, 58000, 1000, 14000, 90)
    OP_77(0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    FadeIn(2000, 0)
    PlayBGM(97)
    OP_0D()
    Sleep(1000)

    NpcTalk(
        0x0101,
        '红骑士尤利乌斯',
        (
            '#0010051273V#424F#2P挚友啊。\n',
            '事已至此你我别无选择……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051274V命中注定\n',
            '我们终要决一雌雄。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    PlaySE(505, 0x00, 0x64)
    SetChrChipByIndex(0x0101, 23)
    SetChrSubChip(0x0101, 5)
    OP_0D()
    Sleep(500)

    NpcTalk(
        0x0101,
        '红骑士尤利乌斯',
        (
            '#0010051275V#421F#2P拔剑！\n',
            '为了彼此所背负的责任！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051276V更为了你我心爱的公主！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(
        0x0105,
        '苍骑士奥斯卡',
        (
            '#0060051277V#359F#1P所谓命运，\n',
            '是凭自己的双手开拓的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051278V本应承担的立场与公主的微笑，\n',
            '此时此刻是那么的遥远……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(
        0x0101,
        '红骑士尤利乌斯',
        (
            '#0010051279V#422F#2P你怕了吗，奥斯卡！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(
        0x0105,
        '苍骑士奥斯卡',
        (
            '#0060051280V#357F#1P然而，此刻驱使着身体的，\n',
            '这近乎疯狂的热情究竟是什么？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051281V我似乎再次不可避免地\n',
            '在此与你一决高下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    Fade(250)
    PlaySE(505, 0x00, 0x64)
    SetChrChipByIndex(0x0105, 24)
    SetChrSubChip(0x0105, 5)
    OP_0D()
    Sleep(500)

    NpcTalk(
        0x0105,
        '苍骑士奥斯卡',
        (
            '#0060051282V#352F#1P在以革命之名的暴风雨\n',
            '将一切吞没之前……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051283V以手中的剑刃决定命运吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(
        0x0101,
        '红骑士尤利乌斯',
        (
            '#0010051284V#420F#2P啊啊……\n',
            '空之女神将见证你我二人的灵魂!',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051285V来吧，一决胜负！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(
        0x0105,
        '苍骑士奥斯卡',
        (
            '#0060051286V#356F#1P来吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0105, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    OP_63(0x0101)
    OP_63(0x0105)
    OP_21()

    ChrTalk(
        0x0101,
        (
            '#0010051287V#347F#2P哈～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051288V#357F#1P呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    PlaySE(213, 0x00, 0x64)
    SetChrChipByIndex(0x0101, 14)
    SetChrChipByIndex(0x0105, 15)
    SetChrSubChip(0x0101, 0)
    SetChrSubChip(0x0105, 0)
    OP_0D()
    PlayBGM(14)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010051289V#341F#2P成功了～㈱',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051290V终于准确无误地\n',
            '完成了这一幕呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051291V#351F#1P呵呵，你的演技真是逼真。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051292V#346F#2P嘿嘿，不过跟科洛丝相比，\n',
            '我的功夫还差的远呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051293V而且，\n',
            '你又从来不会念错过台词。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051294V#350F#1P那是因为我从很早之前\n',
            '就开始看剧本了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051295V现在我也总算能\n',
            '跟得上艾丝蒂尔的动作了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051296V#351F要你不厌其烦地指点我练剑，\n',
            '真是太谢谢你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051297V#340F#2P你太客气了，\n',
            '因为你基础本来就很好嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051298V只要你愿意，我想你随时\n',
            '都能取得游击士的资格的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051299V#355F#1P呵呵，你就别抬举我了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0105, 180, 400)
    Sleep(500)

    @scena.Lambda('lambda_2204')
    def lambda_2204():
        CameraMove(58730, 2850, 2760, 5000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2204)

    @scena.Lambda('lambda_221C')
    def lambda_221C():
        OP_6C(18000, 5000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_221C)

    @scena.Lambda('lambda_222C')
    def lambda_222C():
        OP_67(0, 2930, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_222C)

    Sleep(1000)

    @scena.Lambda('lambda_2249')
    def lambda_2249():
        ChrWalkTo(0x00FE, 59350, 1000, 11500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_2249)

    Sleep(500)

    SetChrDirection(0x0101, 225, 400)

    @scena.Lambda('lambda_2270')
    def lambda_2270():
        ChrWalkTo(0x00FE, 60580, 1000, 11500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2270)

    WaitForThreadExit(0x0105, 0x0001)
    SetChrDirection(0x0105, 180, 400)
    WaitForThreadExit(0x0101, 0x0001)
    SetChrDirection(0x0101, 180, 400)
    WaitForThreadExit(0x0008, 0x0001)

    ChrTalk(
        0x0105,
        (
            '#0060051300V#350F终于，明天就要正式演出了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051301V不知道特蕾莎老师和孩子们\n',
            '会不会喜欢呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0101, 225, 400)

    ChrTalk(
        0x0101,
        (
            '#0010051302V#340F#2P呵呵，你真的很关心\n',
            '特蕾莎院长他们呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051303V#341F简直就像一家人似的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051304V#353F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051305V#344F#2P啊，对不起。\n',
            '我说错什么话了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0105, 135, 400)

    ChrTalk(
        0x0105,
        (
            '#0060051306V#355F不……\n',
            '就像艾丝蒂尔所说的那样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051307V是老师他们让我知道\n',
            '家人才是世上最宝贵的东西……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051308V#350F因为我刚出生不久，\n',
            '父母就在一次意外中去世了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051309V#344F#2P哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    CameraMove(60080, 1000, 14330, 0)
    OP_67(0, 5210, -10000, 0)
    CameraSetDistance(1400, 0)
    OP_6C(0, 0)
    OP_6E(673, 0)
    OP_0D()

    ChrTalk(
        0x0105,
        (
            '#0060051310V#357F#1P虽然被富裕的亲戚收养，\n',
            '过着自由自在随心所欲的生活……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051311V但我却从来都不知道，\n',
            '所谓的家人究竟是什么样的存在。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051312V#358F直到１０年前……\n',
            '遇到老师他们的那一天开始。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051313V#344F#2P１０年前……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051314V#342F难道是『百日战役』的时候？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051315V#359F#1P是的，\n',
            '那时候我正好来到了卢安。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051316V不仅要逃避帝国军追杀，\n',
            '而且还和自己的亲戚走散了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051317V是特蕾莎老师和\n',
            '她丈夫约瑟夫先生保护了我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051318V#343F#2P是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051319V#358F#1P战争结束后，我就被亲戚接回去了。\n',
            '虽然只是短短的几个月……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051320V但是，特蕾莎老师和约瑟夫叔叔\n',
            '对我的关心和照顾却是无微不至的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051321V#357F那时候，我才第一次知道。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051322V拥有父亲和母亲，\n',
            '是一种什么样的感觉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051323V全家人能够生活在一起，\n',
            '又是一种何等温暖的幸福……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051324V#340F#2P科洛丝……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051325V#355F#1P对、对不起……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051326V情不自禁之下，\n',
            '说了那么一大堆无聊的话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051327V#346F#2P不，没这回事呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051328V#341F明天的舞台剧……\n',
            '我们一起加油，来场绝佳的演出吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051329V#358F#1P……好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051330V#346F#2P由我来说可能有点自卖自夸，\n',
            '不过，我想绝对会很精彩的！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051331V不单是我们，\n',
            '乔儿和汉斯也都很努力呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051332V#350F#1P呵呵，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051333V不过，功劳最大的\n',
            '应该还是非约修亚莫属吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051334V想不到他的演技居然那么好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051335V#340F#2P嗯、嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051336V明明那么不情愿，\n',
            '却还能把公主演得活灵活现呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051337V#350F#1P不论是发音还是时机的把握，\n',
            '真的丝毫也不比职业演员逊色呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051338V约修亚过去曾经演过戏吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051339V#343F#2P啊，嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051340V在我和他相遇之前，\n',
            '有关他的事我自己也不是很清楚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051341V我不知道他以前经历过什么，\n',
            '而且，他一直总不想和我说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051342V#353F#1P啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051343V对不起……\n',
            '问了不该问的问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051344V#340F#2P啊哈哈，没什么啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051345V#346F嗯～约修亚确实就是\n',
            '那种什么事都能做得很完美的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051346V真的总是优哉游哉从容不迫的，\n',
            '一点儿都不可爱……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051347V倒还是偶尔慌张的时候\n',
            '才显出他那比较可爱一面～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051348V#355F#1P呵呵……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051349V#357F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051350V#340F#2P怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051351V#359F#1P其实我们两个的角色\n',
            '换过来扮演或许会比较好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051352V#344F#2P哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051353V#353F#1P尤利乌斯和奥斯卡啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051354V我觉得奥斯卡还是\n',
            '由艾丝蒂尔来演比较好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051355V#340F#2P哎？为什么？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051356V不过我和\n',
            '贵族出身的尤利乌斯\n',
            '在身份上的确有点不大相称……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051357V#353F#1P不，我不是这个意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051358V#355F……就是，舞台剧的最后……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051359V#344F#2P哦、哦哦……\n',
            '是公主对奥斯卡做那个……是吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051360V#355F#1P是、是的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051361V#348F#2P真是便宜了约修亚啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051362V难道说科洛丝\n',
            '不想和约修亚演那个？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051363V#354F#1P我、我不是这个意思！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051364V#359F不过，总觉得有点\n',
            '对不起你们两个呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051365V#348F#2P讨、讨厌啦～\n',
            '别像乔儿那样说这种话嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051366V#343F反正约修亚也只是把我当作\n',
            '妹妹那样照顾而已……\n',
            '  ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051367V#353F#1P是……这样吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051368V#347F#2P他呀，总是站在老爸那边，\n',
            '把我当作小孩子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051369V真是气死我了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051370V#346F总之呢，我觉得你完全\n',
            '没必要为这种事和我介意！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051371V#354F#1P是、是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4A(0x0009, 255)
    SetChrPos(0x0009, 65530, 0, 570, 0)
    SetChrPos(0x0102, 64700, 0, 520, 0)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x0102, 0x0080)

    ChrTalk(
        0x0102,
        (
            '#0020051372V#1P……啊，你们在这里啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_30CE')
    def lambda_30CE():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_30CE')

    DispatchAsync2(0x0101, 0x0001, lambda_30CE)

    @scena.Lambda('lambda_30DF')
    def lambda_30DF():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_30DF')

    DispatchAsync2(0x0105, 0x0001, lambda_30DF)

    @scena.Lambda('lambda_30F0')
    def lambda_30F0():
        CameraMove(62650, 1000, 10120, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_30F0)

    @scena.Lambda('lambda_3108')
    def lambda_3108():
        OP_67(0, 4550, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_3108)

    @scena.Lambda('lambda_3120')
    def lambda_3120():
        ChrWalkTo(0x00FE, 65590, 0, 7320, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3120)

    Sleep(500)

    @scena.Lambda('lambda_3140')
    def lambda_3140():
        ChrWalkTo(0x00FE, 64690, 0, 6430, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3140)

    WaitForThreadExit(0x0009, 0x0001)
    SetChrDirection(0x0009, 315, 400)
    WaitForThreadExit(0x0102, 0x0001)
    SetChrDirection(0x0102, 315, 400)
    TerminateThread(0x0105, 0xFF)
    TerminateThread(0x0101, 0xFF)

    ChrTalk(
        0x0101,
        (
            '#0010051373V#344F约、约修亚！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051374V#354F汉斯也在……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520051375V#730F彩排都结束了，\n',
            '居然还在练习啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520051376V你们俩还真是卖力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020051377V#010F决斗那场戏，没问题了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051378V#346F当然，就交给我们吧！\n',
            '一定让你看到完美无缺的表演！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020051379V#019F是吗……\n',
            '嗯，那我就拭目以待了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051380V#350F说起来，\n',
            '你们两个怎么会来这里？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051381V难道是在找我们吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520051382V#730F是啊，今天是艾丝蒂尔和约修亚\n',
            '在学院里住的最后一天了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520051383V大家不如一起吃顿晚饭，\n',
            '也算是为了预祝明天的成功。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051384V#340F啊，是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051385V#341F好，我也赞成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051386V#351F也请让我一同参加哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020051387V#010F说起来……\n',
            '乔儿没和你们在一起吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051388V#350F你说乔儿啊，\n',
            '她刚才被校长叫走了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051389V我去找她吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051390V#340F啊，我也去！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051391V约修亚你们\n',
            '就先去食堂占位子吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020051392V#019F嗯，好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0009, 400)

    ChrTalk(
        0x0102,
        (
            '#0020051393V#010F那我们就先去食堂吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0102, 400)

    ChrTalk(
        0x0009,
        (
            '#0520051394V#731F#2P好！老大。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020051395V#018F谁是你的老大……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0102, 180, 400)

    @scena.Lambda('lambda_3531')
    def lambda_3531():
        ChrWalkTo(0x00FE, 64700, 0, 520, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3531)

    Sleep(200)

    SetChrDirection(0x0009, 180, 400)
    ChrWalkTo(0x0009, 65530, 0, 570, 3000, 0x00)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x0102, 0x0080)
    Fade(1000)
    CameraMove(60080, 1000, 14330, 0)
    OP_67(0, 5210, -10000, 0)
    CameraSetDistance(1400, 0)
    OP_6C(0, 0)
    OP_6E(673, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010051396V#346F#2P呵呵，看来他们两个\n',
            '也相处得不错啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051397V约修亚他有时候\n',
            '会有拒人于千里之外的一面，\n',
            '我本来还有点担心呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0105, 135, 400)

    ChrTalk(
        0x0105,
        (
            '#0060051398V#358F#1P呵呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0101, 225, 400)

    ChrTalk(
        0x0101,
        (
            '#0010051399V#344F#2P咦？怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051400V#351F#1P不不……\n',
            '也没什么啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051401V#340F#2P嗯～好了。\n',
            '我们先去换衣服吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051402V穿成这样招摇过市的话，\n',
            '实在是有点难为情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051403V#358F#1P呵呵，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(-34830, 1000, 10350, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FormationDelMember(0x01, 0xFF)
    SetChrPos(0x0105, -36520, 1000, 8430, 90)
    SetChrPos(0x0101, -35180, 1000, 8580, 270)
    SetChrChipByIndex(0x0105, 65535)
    SetChrChipByIndex(0x0101, 65535)
    Sleep(300)

    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010051404V#006F#2P……好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051405V那我们现在\n',
            '就去接乔儿回来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051406V#040F#3P好。\n',
            '去校长室吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrStatus(0x0000, 0xFE, 0)
    SetChrStatus(0x0001, 0xFE, 0)
    SetChrStatus(0x0002, 0xFE, 0)
    SetChrStatus(0x0003, 0xFE, 0)
    SetChrStatus(0x0004, 0xFE, 0)
    SetChrStatus(0x0005, 0xFE, 0)
    SetChrStatus(0x0006, 0xFE, 0)
    SetChrStatus(0x0007, 0xFE, 0)
    ClearMapFlags(0x10000000)

    @scena.Lambda('lambda_3855')
    def lambda_3855():
        OP_69(0x0000, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_3855)

    EventEnd(0x02)
    SetMapFlags(0x00000080)
    WaitForThreadExit(0x0000, 0x0001)
    ClearMapFlags(0x00000080)
    SetMapFlags(0x00000001)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

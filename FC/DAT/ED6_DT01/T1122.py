import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T1122_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1122   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '帕克'),
    TXT(0x02, '德拉多'),
    TXT(0x03, '普蕾沙'),
    TXT(0x04, '波波'),
    TXT(0x05, '思潘斯老人'),
    TXT(0x06, '卡特丽亚'),
    TXT(0x07, '泊尔'),
    TXT(0x08, '米蕾婆婆'),
    TXT(0x09, '丽露露'),
    TXT(0x0A, '卡洛'),
    TXT(0x0B, '里布罗'),
    TXT(0x0C, '刚茨'),
    TXT(0x0D, '格蕾娅'),
    TXT(0x0E, '玛依森老人'),
    TXT(0x0F, '艾米'),
    TXT(0x10, '西加罗'),
    TXT(0x11, '艾德尔'),
    TXT(0x12, '马尔科'),
    TXT(0x13, '西蒙'),
    TXT(0x14, '年轻女性'),
    TXT(0x15, '米拉诺'),
    TXT(0x16, '莉拉'),
    TXT(0x17, '萨拉'),
    TXT(0x18, '朵洛希'),
    TXT(0x19, '芬尼尔'),
    TXT(0x1A, '奥利维尔'),
    TXT(0x1B, ''),
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
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/T1122._SN', 'ED6_DT01/T1122_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x7C66
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
        ('ED6_DT07/CH01070._CH', 'ED6_DT07/CH01070P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01270._CH', 'ED6_DT07/CH01270P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH01043._CH', 'ED6_DT07/CH01043P._CP'),
        ('ED6_DT07/CH01100._CH', 'ED6_DT07/CH01100P._CP'),
        ('ED6_DT07/CH02360._CH', 'ED6_DT07/CH02360P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01230._CH', 'ED6_DT07/CH01230P._CP'),
        ('ED6_DT07/CH01350._CH', 'ED6_DT07/CH01350P._CP'),
        ('ED6_DT06/CH20063._CH', 'ED6_DT06/CH20063P._CP'),
        ('ED6_DT07/CH02370._CH', 'ED6_DT07/CH02370P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT06/CH20064._CH', 'ED6_DT06/CH20064P._CP'),
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
    ]

# id: 0x10002 offset: 0x18A
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
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
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
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
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
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
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
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
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
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
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
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
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
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0016,
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
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0017,
        ),
        ScenaNpcData(
            x                   = -9150,
            z                   = -1000,
            y                   = 340,
            direction           = 275,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0018,
        ),
        ScenaNpcData(
            x                   = 6000,
            z                   = 0,
            y                   = -5500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0019,
        ),
        ScenaNpcData(
            x                   = -11100,
            z                   = 0,
            y                   = 10300,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0111,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001A,
        ),
        ScenaNpcData(
            x                   = -18120,
            z                   = 0,
            y                   = 5130,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001B,
        ),
        ScenaNpcData(
            x                   = -3600,
            z                   = 0,
            y                   = 12500,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            x                   = 11500,
            z                   = 0,
            y                   = 12000,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001D,
        ),
        ScenaNpcData(
            x                   = 1000,
            z                   = -1000,
            y                   = 1000,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0007,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001E,
        ),
        ScenaNpcData(
            x                   = -7700,
            z                   = 0,
            y                   = 14700,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            x                   = -15200,
            z                   = 0,
            y                   = 15700,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0008,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001F,
        ),
        ScenaNpcData(
            x                   = 6610,
            z                   = 0,
            y                   = 2340,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0021,
        ),
        ScenaNpcData(
            x                   = 700,
            z                   = -1000,
            y                   = 4900,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0009,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0022,
        ),
        ScenaNpcData(
            x                   = -620,
            z                   = -1000,
            y                   = -3500,
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
            x                   = 350,
            z                   = -1000,
            y                   = 480,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0023,
        ),
        ScenaNpcData(
            x                   = 6400,
            z                   = 0,
            y                   = 7700,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 24,
            chipIndex           = 24,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0024,
        ),
        ScenaNpcData(
            x                   = 12300,
            z                   = 0,
            y                   = -8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0025,
        ),
        ScenaNpcData(
            x                   = 7180,
            z                   = 0,
            y                   = 540,
            direction           = 275,
            word_0E             = 0,
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0026,
        ),
        ScenaNpcData(
            x                   = -1430,
            z                   = 0,
            y                   = 9040,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 25,
            chipIndex           = 25,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0027,
        ),
        ScenaNpcData(
            x                   = -12050,
            z                   = 0,
            y                   = -2230,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 27,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0028,
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
    )

# id: 0x10005 offset: 0x4CA
@scena.ActorData('ActorData')
def ActorData():
    return (
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
            talkFunctionIndex   = 0x0010,
            word_22             = 0x0000,
        ),
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
            talkFunctionIndex   = 0x000C,
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
            talkFunctionIndex   = 0x0015,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x536
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_580',
    )

    SetChrPos(0x0010, 1100, 0, -7600, 0)
    ClearChrFlags(0x0012, 0x0010)
    SetChrPos(0x0013, -14500, 0, 4500, 90)
    SetChrFlags(0x0018, 0x0080)
    SetChrFlags(0x0018, 0x0008)
    SetChrFlags(0x0017, 0x0080)
    SetChrFlags(0x0017, 0x0008)
    ClearChrFlags(0x0020, 0x0080)

    Jump('loc_7A2')

    def _loc_580(): pass

    label('loc_580')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_5DB',
    )

    SetChrPos(0x0010, 1100, 0, -7600, 0)
    ClearChrFlags(0x0012, 0x0010)
    SetChrPos(0x0013, -14500, 0, 4500, 90)
    SetChrFlags(0x0018, 0x0080)
    SetChrFlags(0x0018, 0x0008)
    SetChrFlags(0x0017, 0x0080)
    SetChrFlags(0x0017, 0x0008)
    ClearChrFlags(0x0019, 0x0080)
    SetChrPos(0x0019, -19400, 0, 3600, 180)

    Jump('loc_7A2')

    def _loc_5DB(): pass

    label('loc_5DB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_64B',
    )

    SetChrPos(0x0012, -12200, 0, 14900, 225)
    SetChrPos(0x0016, 5000, 0, 4700, 315)
    SetChrPos(0x0013, -11680, 0, -2590, 315)
    SetChrPos(0x0017, -7400, -1000, -320, 90)
    SetChrPos(0x0018, -7400, 0, 900, 90)
    SetChrPos(0x0010, 1100, 0, -7600, 0)

    Jump('loc_7A2')

    def _loc_64B(): pass

    label('loc_64B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_6CD',
    )

    SetChrFlags(0x000F, 0x0010)
    SetChrPos(0x0010, 1100, 0, -7600, 0)
    SetChrPos(0x0016, -11800, 0, 7900, 315)
    SetChrPos(0x0012, -12200, 0, 14900, 225)
    SetChrFlags(0x0018, 0x0010)
    SetChrFlags(0x0017, 0x0010)
    SetChrPos(0x0018, -15400, 0, 8900, 45)
    SetChrPos(0x0017, -13100, 0, 5900, 315)
    ClearChrFlags(0x0019, 0x0080)
    SetChrFlags(0x0019, 0x0010)
    ClearChrFlags(0x001A, 0x0080)
    ClearChrFlags(0x001D, 0x0080)

    Jump('loc_7A2')

    def _loc_6CD(): pass

    label('loc_6CD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_72F',
    )

    SetChrPos(0x0010, 1100, 0, -7600, 0)
    SetChrPos(0x0016, 6500, 0, -7100, 90)
    SetChrFlags(0x0018, 0x0010)
    SetChrPos(0x0018, -14500, 0, -6300, 270)
    SetChrPos(0x0017, -11700, 0, -7190, 215)
    ClearChrFlags(0x001C, 0x0080)
    ClearChrFlags(0x001E, 0x0080)
    ClearChrFlags(0x0021, 0x0080)

    Jump('loc_7A2')

    def _loc_72F(): pass

    label('loc_72F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_77D',
    )

    ClearChrFlags(0x0012, 0x0010)
    SetChrChipByIndex(0x001F, 26)
    ClearChrFlags(0x001F, 0x0080)
    SetChrPos(0x001F, -11600, 0, -7100, 225)
    SetChrChipByIndex(0x0017, 17)
    TerminateThread(0x0017, 0xFF)
    SetChrFlags(0x0017, 0x0004)
    SetChrFlags(0x0017, 0x0010)
    SetChrPos(0x0017, -8600, 0, 8600, 0)

    Jump('loc_7A2')

    def _loc_77D(): pass

    label('loc_77D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_7A2',
    )

    SetChrFlags(0x0015, 0x0010)
    ClearChrFlags(0x001F, 0x0080)
    SetChrFlags(0x0018, 0x0080)
    SetChrFlags(0x0018, 0x0008)
    SetChrFlags(0x0017, 0x0080)
    SetChrFlags(0x0017, 0x0008)

    def _loc_7A2(): pass

    label('loc_7A2')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_7BA'),
        (0x00000065, 'loc_7BA'),
        (0x00000066, 'loc_7BA'),
        (0x00000067, 'loc_7BA'),
        (-1, 'loc_7D0'),
    )

    def _loc_7BA(): pass

    label('loc_7BA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 2, 0x30A)),
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7CD',
    )

    SetScenaFlags(ScenaFlag(0x0061, 3, 0x30B))
    Event(0, 0x0029)

    def _loc_7CD(): pass

    label('loc_7CD')

    Jump('loc_7D0')

    def _loc_7D0(): pass

    label('loc_7D0')

    Return()

# id: 0x0001 offset: 0x7D1
@scena.Code('Init')
def Init():
    OP_25(0x01CB, -4200, -1000, 630, 2000, 25000, 0x64, 0x00000000)

    Return()

# id: 0x0002 offset: 0x7EE
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_803',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_803(): pass

    label('loc_803')

    Return()

# id: 0x0003 offset: 0x804
@scena.Code('func_03_804')
def func_03_804():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_850',
    )

    ChrWalkTo(0x00FE, 6040, 0, 13600, 2000, 0x00)
    SetChrDirection(0x00FE, 0, 400)
    Sleep(3000)

    ChrWalkTo(0x00FE, 8250, 0, 13600, 2000, 0x00)
    SetChrDirection(0x00FE, 0, 400)
    Sleep(3000)

    Jump('func_03_804')

    def _loc_850(): pass

    label('loc_850')

    Return()

# id: 0x0004 offset: 0x851
@scena.Code('func_04_851')
def func_04_851():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_87E',
    )

    def _loc_858(): pass

    label('loc_858')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_87B',
    )

    OP_8D(0x00FE, -800, -7100, 4200, -8700, 2000)

    Jump('loc_858')

    def _loc_87B(): pass

    label('loc_87B')

    Jump('loc_8FB')

    def _loc_87E(): pass

    label('loc_87E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_8AB',
    )

    def _loc_885(): pass

    label('loc_885')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_8A8',
    )

    OP_8D(0x00FE, -800, -7100, 4200, -8700, 2000)

    Jump('loc_885')

    def _loc_8A8(): pass

    label('loc_8A8')

    Jump('loc_8FB')

    def _loc_8AB(): pass

    label('loc_8AB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_8D8',
    )

    def _loc_8B2(): pass

    label('loc_8B2')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_8D5',
    )

    OP_8D(0x00FE, -800, -7100, 4200, -8700, 2000)

    Jump('loc_8B2')

    def _loc_8D5(): pass

    label('loc_8D5')

    Jump('loc_8FB')

    def _loc_8D8(): pass

    label('loc_8D8')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_8FB',
    )

    OP_8D(0x00FE, -10160, 3020, -8050, -1770, 2000)

    Jump('loc_8D8')

    def _loc_8FB(): pass

    label('loc_8FB')

    Return()

# id: 0x0005 offset: 0x8FC
@scena.Code('func_05_8FC')
def func_05_8FC():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_91F',
    )

    OP_8D(0x00FE, 6800, -2300, 4700, -12100, 2000)

    Jump('func_05_8FC')

    def _loc_91F(): pass

    label('loc_91F')

    Return()

# id: 0x0006 offset: 0x920
@scena.Code('func_06_920')
def func_06_920():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_943',
    )

    OP_8D(0x00FE, 200, 14800, -7900, 10300, 2000)

    Jump('func_06_920')

    def _loc_943(): pass

    label('loc_943')

    Return()

# id: 0x0007 offset: 0x944
@scena.Code('func_07_944')
def func_07_944():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_971',
    )

    def _loc_94B(): pass

    label('loc_94B')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_96E',
    )

    OP_8D(0x00FE, 6700, 3600, 4600, -9900, 2000)

    Jump('loc_94B')

    def _loc_96E(): pass

    label('loc_96E')

    Jump('loc_9B3')

    def _loc_971(): pass

    label('loc_971')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_990',
    )

    def _loc_978(): pass

    label('loc_978')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_98D',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_978')

    def _loc_98D(): pass

    label('loc_98D')

    Jump('loc_9B3')

    def _loc_990(): pass

    label('loc_990')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_9B3',
    )

    OP_8D(0x00FE, 2100, 4700, -900, -5100, 2000)

    Jump('loc_990')

    def _loc_9B3(): pass

    label('loc_9B3')

    Return()

# id: 0x0008 offset: 0x9B4
@scena.Code('func_08_9B4')
def func_08_9B4():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_9D3',
    )

    def _loc_9BB(): pass

    label('loc_9BB')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_9D0',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_9BB')

    def _loc_9D0(): pass

    label('loc_9D0')

    Jump('loc_B18')

    def _loc_9D3(): pass

    label('loc_9D3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_AF5',
    )

    def _loc_9DA(): pass

    label('loc_9DA')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_AF2',
    )

    ChrWalkTo(0x00FE, -14500, 0, -4400, 2000, 0x00)
    SetChrDirection(0x00FE, 270, 200)
    Sleep(5000)

    ChrWalkTo(0x00FE, -14400, 0, -2800, 2000, 0x00)
    ChrWalkTo(0x00FE, -17000, 0, -2800, 2000, 0x00)
    ChrWalkTo(0x00FE, -18100, 0, -8400, 2000, 0x00)
    ChrWalkTo(0x00FE, -16400, 0, -11700, 2000, 0x00)
    SetChrDirection(0x00FE, 90, 200)
    Sleep(4000)

    ChrWalkTo(0x00FE, -16400, 0, -13200, 2000, 0x00)
    ChrWalkTo(0x00FE, -11600, 0, -12600, 2000, 0x00)
    SetChrDirection(0x00FE, 0, 200)
    Sleep(4000)

    ChrWalkTo(0x00FE, -8500, 0, -12600, 2000, 0x00)
    ChrWalkTo(0x00FE, -8500, 0, -9900, 2000, 0x00)
    ChrWalkTo(0x00FE, -13200, 0, -9100, 2000, 0x00)
    ChrWalkTo(0x00FE, -14500, 0, -6300, 2000, 0x00)
    SetChrDirection(0x00FE, 270, 200)
    Sleep(5000)

    Jump('loc_9DA')

    def _loc_AF2(): pass

    label('loc_AF2')

    Jump('loc_B18')

    def _loc_AF5(): pass

    label('loc_AF5')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_B18',
    )

    OP_8D(0x00FE, -12100, 16600, -16600, 14400, 2000)

    Jump('loc_AF5')

    def _loc_B18(): pass

    label('loc_B18')

    Return()

# id: 0x0009 offset: 0xB19
@scena.Code('func_09_B19')
def func_09_B19():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_B3C',
    )

    OP_8D(0x00FE, -100, 500, 2300, 6000, 2000)

    Jump('func_09_B19')

    def _loc_B3C(): pass

    label('loc_B3C')

    Return()

# id: 0x000A offset: 0xB3D
@scena.Code('func_0A_B3D')
def func_0A_B3D():
    Call(0, 0x000B)

    Return()

# id: 0x000B offset: 0xB42
@scena.Code('func_0B_B42')
def func_0B_B42():
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
        'loc_BA0',
    )

    OP_0D()
    OP_A9(0x11)
    OP_56(0x00)
    TalkEnd(0x0008)

    Return()

    def _loc_BA0(): pass

    label('loc_BA0')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BB1',
    )

    TalkEnd(0x0008)

    Return()

    def _loc_BB1(): pass

    label('loc_BB1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_C56',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C10',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '那些可恶的空贼\n',
            '终于被逮捕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '这么长时间\n',
            '一直让柏斯蒙受着损失。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C53')

    def _loc_C10(): pass

    label('loc_C10')

    ChrTalk(
        0x0008,
        (
            '空贼吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不管有什么理由，\n',
            '也不应该随便夺取别人的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C53(): pass

    label('loc_C53')

    Jump('loc_12A2')

    def _loc_C56(): pass

    label('loc_C56')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_CEF',
    )

    ChrTalk(
        0x0008,
        (
            '道路封锁也解除了，\n',
            '虽然只有往西航行的定期船，\n',
            '不过空运也总算恢复了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我的店的状况\n',
            '也有了非常大的好转。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '好～我要更加努力哦～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12A2')

    def _loc_CEF(): pass

    label('loc_CEF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_DE8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D75',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '往西航行的飞行船\n',
            '终于再次起航了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '这样我就能够\n',
            '去采购洛连特的蔬菜了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '好～多多采购，\n',
            '多多卖出～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DE5')

    def _loc_D75(): pass

    label('loc_D75')

    ChrTalk(
        0x0008,
        (
            '我现在对挑选蔬菜的眼力\n',
            '可是十分有信心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '特别是帕赛尔农场的蔬菜，可谓绝品。\n',
            '在这里的销售状况非常好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DE5(): pass

    label('loc_DE5')

    Jump('loc_12A2')

    def _loc_DE8(): pass

    label('loc_DE8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_E65',
    )

    ChrTalk(
        0x0008,
        (
            '这家店的所有水果\n',
            '都是从拉文努村采购的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '那个村子以前\n',
            '虽然是因为矿山而热闹起来的，\n',
            '但是现在却以果园闻名。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12A2')

    def _loc_E65(): pass

    label('loc_E65')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_F5F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F10',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '柏斯商人崇尚\n',
            '自由的商业风气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '以前这里曾经有一个\n',
            '人们各做各的生意、\n',
            '互不关心的时代。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '全靠前任市长和现任市长小姐\n',
            '把商人们都团结起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F5C')

    def _loc_F10(): pass

    label('loc_F10')

    ChrTalk(
        0x0008,
        (
            '钢壁之路的检查哨\n',
            '好像被撤掉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '这样的话，\n',
            '进货应该能够恢复了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F5C(): pass

    label('loc_F5C')

    Jump('loc_12A2')

    def _loc_F5F(): pass

    label('loc_F5F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_1122',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_10AA',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '我们刚开始做生意的时候\n',
            '受到了市政府的很多援助呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哇～\n',
            '柏斯真的是商业都市呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F是啊，\n',
            '从梅贝尔市长父亲在的那个时候起， \n',
            '政府就一直作为我们的后援呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我们能够拥有自己的店铺，\n',
            '也是多亏了大小姐\n',
            '和前任市长呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '正因如此，\n',
            '如果我们再让大小姐为难的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '就会给柏斯商人丢脸呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_111F')

    def _loc_10AA(): pass

    label('loc_10AA')

    ChrTalk(
        0x0008,
        (
            '这里刚开始做生意的时候\n',
            '受到了市政府的很多援助呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我们能够拥有自己的店铺，\n',
            '也是多亏了大小姐\n',
            '和前任市长呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_111F(): pass

    label('loc_111F')

    Jump('loc_12A2')

    def _loc_1122(): pass

    label('loc_1122')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_12A2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1238',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '真是的……\n',
            '都是军队制定各式各样的规则，\n',
            '让我四处碰壁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '考虑到进货时的成本，\n',
            '再这样下去，我的生意就完蛋了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#002F（总、总感到一股危险的气氛。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#012F（嗯，飞艇继续停航，\n',
            '　钢壁之路被封锁……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '（应该给做生意的商人\n',
            '　带来了许多影响啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12A2')

    def _loc_1238(): pass

    label('loc_1238')

    ChrTalk(
        0x0008,
        (
            '我这么辛苦，\n',
            '好不容易才使营业额上升……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '现在却变成这个样子，\n',
            '唯一的对策就只有将价格继续提高了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12A2(): pass

    label('loc_12A2')

    TalkEnd(0x0008)

    Return()

# id: 0x000C offset: 0x12A6
@scena.Code('func_0C_12A6')
def func_0C_12A6():
    Call(0, 0x000D)

    Return()

# id: 0x000D offset: 0x12AB
@scena.Code('func_0D_12AB')
def func_0D_12AB():
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
        'loc_1309',
    )

    OP_0D()
    OP_A9(0x10)
    OP_56(0x00)
    TalkEnd(0x0009)

    Return()

    def _loc_1309(): pass

    label('loc_1309')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_131A',
    )

    TalkEnd(0x0009)

    Return()

    def _loc_131A(): pass

    label('loc_131A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_13F7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_13A6',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '我想从卢安\n',
            '进一批鱼类产品过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '那里过去就以\n',
            '王国水产量第一而著称。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '不愧是被称为\n',
            '『海港都市』的地方啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13F4')

    def _loc_13A6(): pass

    label('loc_13A6')

    ChrTalk(
        0x0009,
        (
            '我想从卢安\n',
            '进一批鱼类产品过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '那里过去就以\n',
            '王国水产量第一而著称。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13F4(): pass

    label('loc_13F4')

    Jump('loc_196F')

    def _loc_13F7(): pass

    label('loc_13F7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_147F',
    )

    ChrTalk(
        0x0009,
        (
            '飞艇事件也好，强盗案件也好，\n',
            '最近让人不安的话题还真多……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '不过，这个城市有市长小姐坐镇。\n',
            '她一定会想出办法来解决的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_196F')

    def _loc_147F(): pass

    label('loc_147F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_14C8',
    )

    ChrTalk(
        0x0009,
        (
            '听说南街区出现了强盗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '那里有许多\n',
            '非常高档的商店啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_196F')

    def _loc_14C8(): pass

    label('loc_14C8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_1617',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_15B6',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '在这个柏斯市中，\n',
            '要说起实力仅次于市长的名商人，\n',
            '就是特里诺和博尔德了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '说到这个，最近特里诺的女儿\n',
            '表现得也越来越抢眼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '嗯嗯……\n',
            '她的名字好像叫米拉诺？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '总之，她是一个\n',
            '毫不逊色于她父亲的商业奇才。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1614')

    def _loc_15B6(): pass

    label('loc_15B6')

    ChrTalk(
        0x0009,
        (
            '父女一起上阵，\n',
            '精明能干的商人真令人羡慕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '对了对了，\n',
            '米拉诺和市长小姐的关系非常好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1614(): pass

    label('loc_1614')

    Jump('loc_196F')

    def _loc_1617(): pass

    label('loc_1617')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_178F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1721',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '我和帕克为了在柏斯\n',
            '能够独树一帜而努力工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '将来开一间超大型的\n',
            '综合食品店是我们的梦想。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '在我们的店里能够买到\n',
            '各种各样又便宜又新鲜的食品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '是不是梦幻般的店啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '多亏了有定期船，\n',
            '流通也变得方便了，\n',
            '我们的目标肯定能达成的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_178C')

    def _loc_1721(): pass

    label('loc_1721')

    ChrTalk(
        0x0009,
        (
            '我和帕克\n',
            '为了在柏斯能够独树一帜，\n',
            '每天都在努力工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '将来开一间超大型的\n',
            '综合食品店是我们的梦想。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_178C(): pass

    label('loc_178C')

    Jump('loc_196F')

    def _loc_178F(): pass

    label('loc_178F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_1874',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_181B',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '我们只看到了\n',
            '自己眼前的蝇头小利……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '小姐所说的\n',
            '确实很有道理啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我们差一点就在\n',
            '商人的道路上迷失方向了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1871')

    def _loc_181B(): pass

    label('loc_181B')

    ChrTalk(
        0x0009,
        (
            '我们只看到了\n',
            '自己眼前的蝇头小利……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我们差一点就在\n',
            '商人的道路上迷失方向了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1871(): pass

    label('loc_1871')

    Jump('loc_196F')

    def _loc_1874(): pass

    label('loc_1874')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_196F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1904',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '我的同伴帕克\n',
            '开始哄抬价格了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '考虑一下现在的状况，\n',
            '那样做也是迫不得已啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '不过，\n',
            '我觉得价格好像也太高了点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_196F')

    def _loc_1904(): pass

    label('loc_1904')

    ChrTalk(
        0x0009,
        (
            '我的同伴帕克\n',
            '开始哄抬价格了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '考虑一下现在的状况，\n',
            '那样做也是迫不得已啊。\n',
            '不过也不能太过分了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_196F(): pass

    label('loc_196F')

    TalkEnd(0x0009)

    Return()

# id: 0x000E offset: 0x1973
@scena.Code('func_0E_1973')
def func_0E_1973():
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
        'loc_19D1',
    )

    OP_0D()
    OP_A9(0x13)
    OP_56(0x00)
    TalkEnd(0x000A)

    Return()

    def _loc_19D1(): pass

    label('loc_19D1')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_19E2',
    )

    TalkEnd(0x000A)

    Return()

    def _loc_19E2(): pass

    label('loc_19E2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_1AE5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A80',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '真是的，\n',
            '那个人跟过去相比一点都没变……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明明是为了和家人一起\n',
            '在柏斯生活才开始做生意的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有什么问题的话\n',
            '说清楚不就好了嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AE2')

    def _loc_1A80(): pass

    label('loc_1A80')

    ChrTalk(
        0x00FE,
        (
            '真是的，\n',
            '那个人跟过去相比一点都没变……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明明是为了和家人一起\n',
            '在柏斯生活才开始做生意的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AE2(): pass

    label('loc_1AE2')

    Jump('loc_1F7D')

    def _loc_1AE5(): pass

    label('loc_1AE5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_1B55',
    )

    ChrTalk(
        0x00FE,
        (
            '真是的，偶尔也该担心一下这里，\n',
            '过来露个脸也好啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是薄情的丈夫。\n',
            '为什么我当初会选他呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F7D')

    def _loc_1B55(): pass

    label('loc_1B55')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_1C68',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C07',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '这家店本来\n',
            '是老公首先提出要开的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是店才刚开张，\n',
            '他就把店强推给我打理了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而他自己却\n',
            '马上回到村里种树去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他脑子里到底在想些什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C65')

    def _loc_1C07(): pass

    label('loc_1C07')

    ChrTalk(
        0x00FE,
        (
            '这家店本来\n',
            '是老公首先提出要开的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是他却把店强推给我打理，\n',
            '自己回到村里种树去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C65(): pass

    label('loc_1C65')

    Jump('loc_1F7D')

    def _loc_1C68(): pass

    label('loc_1C68')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_1D10',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1CD4',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '呼，再加一把劲儿吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……不知道留在村里的老公\n',
            '现在是不是在很有精神地干活呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D0D')

    def _loc_1CD4(): pass

    label('loc_1CD4')

    ChrTalk(
        0x00FE,
        (
            '不知道留在村里的老公\n',
            '现在是不是在很有精神地干活呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D0D(): pass

    label('loc_1D0D')

    Jump('loc_1F7D')

    def _loc_1D10(): pass

    label('loc_1D10')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_1D80',
    )

    ChrTalk(
        0x00FE,
        (
            '最近店面扩大了，\n',
            '事情也变多了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '波波能经常过来帮忙真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是个好孩子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F7D')

    def _loc_1D80(): pass

    label('loc_1D80')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_1DD5',
    )

    ChrTalk(
        0x00FE,
        (
            '我这店的商品都是一些\n',
            '融入了女性智慧的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可不会输给别人的哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F7D')

    def _loc_1DD5(): pass

    label('loc_1DD5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_1F7D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1F4A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '#4S您好，欢迎光临！#2S',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那里的小妹妹与小兄弟！\n',
            '我这里可是有很多好货哦！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(700)

    ChrTalk(
        0x0101,
        (
            '#004F吓、吓死我了～\n',
            '这里的声音还真响呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F和传闻一样，这里是个充满活力的地方啊。\n',
            '在这里转了一天带给我的就是这种感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F就是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '因为超市聚集了\n',
            '从利贝尔各地前来的\n',
            '想在商界有一番作为的人们啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '这份干劲与热情\n',
            '可不是假的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F7D')

    def _loc_1F4A(): pass

    label('loc_1F4A')

    ChrTalk(
        0x00FE,
        (
            '如果有您喜欢的物品，\n',
            '您可以放心地拿起来观赏。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F7D(): pass

    label('loc_1F7D')

    TalkEnd(0x000A)

    Return()

# id: 0x000F offset: 0x1F81
@scena.Code('func_0F_1F81')
def func_0F_1F81():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_1FBB',
    )

    ChrTalk(
        0x00FE,
        (
            '留在拉文努村的爸爸\n',
            '现在正在干什么呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2304')

    def _loc_1FBB(): pass

    label('loc_1FBB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_2023',
    )

    ChrTalk(
        0x00FE,
        (
            '我觉得爸爸回到村里，\n',
            '这其中肯定是有什么原因的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为，\n',
            '爸爸对于开店是最有兴趣的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2304')

    def _loc_2023(): pass

    label('loc_2023')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_2075',
    )

    ChrTalk(
        0x00FE,
        (
            '妈妈，\n',
            '是不是很想见爸爸呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '经常能看到她\n',
            '一脸寂寞的样子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2304')

    def _loc_2075(): pass

    label('loc_2075')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_2104',
    )

    ChrTalk(
        0x00FE,
        (
            '我的爸爸啊，\n',
            '是在村里种水果的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在这里出售的水果\n',
            '也有可能是我爸爸种出来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '其实他本应该和我们\n',
            '一起经营这家小店的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2304')

    def _loc_2104(): pass

    label('loc_2104')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_21D5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_218A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '妈妈真是的，\n',
            '拿餐具这么不小心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我光是看着\n',
            '就已经很紧张了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这么重要的商品\n',
            '应该轻拿轻放才对啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21D2')

    def _loc_218A(): pass

    label('loc_218A')

    ChrTalk(
        0x00FE,
        (
            '妈妈真是的，\n',
            '拿餐具这么不小心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我光是看着\n',
            '就已经很紧张了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_21D2(): pass

    label('loc_21D2')

    Jump('loc_2304')

    def _loc_21D5(): pass

    label('loc_21D5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_22AD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2289',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '刚才市长姐姐来了，\n',
            '给了我们很多的建议。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '关于商品的排列和招待客人的方式，\n',
            '就算对还是小孩子的我也很认真地传授着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '然后还在我们这儿\n',
            '买了一些餐具。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_22AA')

    def _loc_2289(): pass

    label('loc_2289')

    ChrTalk(
        0x00FE,
        (
            '市长姐姐\n',
            '经常在超市巡视呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_22AA(): pass

    label('loc_22AA')

    Jump('loc_2304')

    def _loc_22AD(): pass

    label('loc_22AD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_2304',
    )

    ChrTalk(
        0x00FE,
        (
            '我也算是这里的店员了。\n',
            '在帮我妈妈的忙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我可绝对不是\n',
            '在这里玩耍哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2304(): pass

    label('loc_2304')

    TalkEnd(0x000B)

    Return()

# id: 0x0010 offset: 0x2308
@scena.Code('func_10_2308')
def func_10_2308():
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
        'loc_2366',
    )

    OP_0D()
    TalkBegin(0x000C)
    OP_A9(0x0C)
    OP_56(0x00)
    TalkEnd(0x000C)

    Return()

    def _loc_2366(): pass

    label('loc_2366')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2377',
    )

    TalkEnd(0x000C)

    Return()

    def _loc_2377(): pass

    label('loc_2377')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))
    Call(0, 0x0011)
    SetChrDirection(0x000C, 270, 0)

    Return()

# id: 0x0011 offset: 0x2386
@scena.Code('func_11_2386')
def func_11_2386():
    If(
        (
            (Expr.Eval, "OP_29(0x0011, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_23EB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_23E4',
    )

    TalkBegin(0x000C)

    ChrTalk(
        0x000C,
        (
            '各位，真是谢谢你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '这下我就可以放心地\n',
            '进行新药的调配了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23E8')

    def _loc_23E4(): pass

    label('loc_23E4')

    Call(0, 0x0012)

    def _loc_23E8(): pass

    label('loc_23E8')

    Jump('loc_24CE')

    def _loc_23EB(): pass

    label('loc_23EB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            (Expr.Eval, "OP_29(0x000D, 0x01, 0x4000)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0011, 0x00, 0x02)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_24CA',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0011, 0x01, 0x0004)"),
            (Expr.Eval, "OP_29(0x0011, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2436',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0011, 0x00, 0x04)"),
            Expr.Return,
        ),
        'loc_242A',
    )

    Call(1, 0x0002)
    SetChrDirection(0x000C, 270, 0)

    Return()

    def _loc_242A(): pass

    label('loc_242A')

    Call(1, 0x0001)
    SetChrDirection(0x000C, 270, 0)

    Return()

    def _loc_2436(): pass

    label('loc_2436')

    If(
        (
            (Expr.Eval, "OP_29(0x0011, 0x01, 0x8000)"),
            (Expr.Eval, "OP_29(0x0011, 0x01, 0x0004)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0011, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_245E',
    )

    Call(1, 0x0001)
    SetChrDirection(0x000C, 270, 0)

    Return()

    def _loc_245E(): pass

    label('loc_245E')

    If(
        (
            (Expr.Eval, "OP_29(0x0011, 0x00, 0x04)"),
            Expr.Return,
        ),
        'loc_24BB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_24B4',
    )

    TalkBegin(0x000C)

    ChrTalk(
        0x000C,
        (
            '#1360151078V那么各位，\n',
            '就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1360151079V请小心行事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24B8')

    def _loc_24B4(): pass

    label('loc_24B4')

    Call(0, 0x0012)

    def _loc_24B8(): pass

    label('loc_24B8')

    Jump('loc_24C7')

    def _loc_24BB(): pass

    label('loc_24BB')

    Call(1, 0x0000)
    SetChrDirection(0x000C, 270, 0)

    Return()

    def _loc_24C7(): pass

    label('loc_24C7')

    Jump('loc_24CE')

    def _loc_24CA(): pass

    label('loc_24CA')

    Call(0, 0x0012)
    def _loc_24CE(): pass

    label('loc_24CE')

    TalkEnd(0x000C)
    SetChrDirection(0x000C, 270, 0)

    Return()

# id: 0x0012 offset: 0x24D9
@scena.Code('func_12_24D9')
def func_12_24D9():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_2569',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_253B',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x000C,
        (
            '扰乱柏斯治安的坏人\n',
            '终于被逮捕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '这下子又可以\n',
            '安心地做买卖了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2566')

    def _loc_253B(): pass

    label('loc_253B')

    ChrTalk(
        0x000C,
        (
            '坏人被逮捕了，\n',
            '又可以安心地做买卖了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2566(): pass

    label('loc_2566')

    Jump('loc_2AD6')

    def _loc_2569(): pass

    label('loc_2569')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_267B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2611',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x000C,
        (
            '最近我的店里\n',
            '也渐渐忙起来了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '我在考虑是不是要\n',
            '多请一个人过来帮忙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '可是我又想和顾客接触，\n',
            '亲自沟通一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '真是伤脑筋啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2678')

    def _loc_2611(): pass

    label('loc_2611')

    ChrTalk(
        0x000C,
        (
            '我在考虑是不是要\n',
            '多请一个人过来帮忙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '可是我又想和顾客接触，\n',
            '亲自沟通一下，\n',
            '真是伤脑筋啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2678(): pass

    label('loc_2678')

    Jump('loc_2AD6')

    def _loc_267B(): pass

    label('loc_267B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_26C2',
    )

    ChrTalk(
        0x000C,
        (
            '哎呀，\n',
            '王国军好像也来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '是不是发生什么事情了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2AD6')

    def _loc_26C2(): pass

    label('loc_26C2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_27A0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2743',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x000C,
        (
            '即使飞艇停航了，\n',
            '柏斯商人也不会这么简单屈服的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '因为我们总会\n',
            '想出办法来应付的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '呵·呵·呵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_279D')

    def _loc_2743(): pass

    label('loc_2743')

    ChrTalk(
        0x000C,
        (
            '即使飞艇停航了，\n',
            '柏斯商人也不会这么简单屈服的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '因为我们总会\n',
            '想出办法来应付的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_279D(): pass

    label('loc_279D')

    Jump('loc_2AD6')

    def _loc_27A0(): pass

    label('loc_27A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_286E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_281F',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x000C,
        (
            '我会针对病人各自的症状\n',
            '来调配药剂。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '最近我从东方\n',
            '订购了一些中药。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '买卖的手段也是很重要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_286B')

    def _loc_281F(): pass

    label('loc_281F')

    ChrTalk(
        0x000C,
        (
            '我会针对病人各自的症状\n',
            '来调配药剂。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '最近我从东方\n',
            '订购了一些中药。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_286B(): pass

    label('loc_286B')

    Jump('loc_2AD6')

    def _loc_286E(): pass

    label('loc_286E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_29D8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2979',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x000C,
        (
            '市长每月都会从超市的店铺中\n',
            '挑选出一家进行表彰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '上个月，\n',
            '本店就被评选为『信得过的好商店』。   ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '哎呀哎呀～\n',
            '真是充满了干劲啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F原来如此，\n',
            '市长真的是下了很大功夫呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F是啊，市长虽然年轻，\n',
            '但是深受市民的爱戴和支持。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29D5')

    def _loc_2979(): pass

    label('loc_2979')

    ChrTalk(
        0x000C,
        (
            '上个月，\n',
            '本店被评选为超市中\n',
            '『信得过的好商店』。   ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '哎呀哎呀～\n',
            '真是充满了干劲啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_29D5(): pass

    label('loc_29D5')

    Jump('loc_2AD6')

    def _loc_29D8(): pass

    label('loc_29D8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_2AD6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2AA3',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x000C,
        (
            '想买点什么东西吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '我店里的药都是很有效的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#004F啊～连药都有卖吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '在柏斯超市\n',
            '真是想买什么就能买到什么啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F嗯，的确……\n',
            '出售各式的商品才是这里的特点啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2AD6')

    def _loc_2AA3(): pass

    label('loc_2AA3')

    ChrTalk(
        0x000C,
        (
            '想买点什么东西吗？\n',
            '我店里的药都是很有效的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2AD6(): pass

    label('loc_2AD6')

    ClearScenaFlags(ScenaFlag(0x0000, 6, 0x6))
    TalkEnd(0x000C)
    SetChrDirection(0x000C, 270, 0)

    Return()

# id: 0x0013 offset: 0x2AE4
@scena.Code('func_13_2AE4')
def func_13_2AE4():
    Call(0, 0x0014)

    Return()

# id: 0x0014 offset: 0x2AE9
@scena.Code('func_14_2AE9')
def func_14_2AE9():
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
        'loc_2B47',
    )

    OP_0D()
    OP_A9(0x12)
    OP_56(0x00)
    TalkEnd(0x000D)

    Return()

    def _loc_2B47(): pass

    label('loc_2B47')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2B58',
    )

    TalkEnd(0x000D)

    Return()

    def _loc_2B58(): pass

    label('loc_2B58')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_2CE0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2C6D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x000D,
        (
            '空贼被逮捕了，\n',
            '我的未婚夫也回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '不过他却自己\n',
            '开了另一家店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '大概是因为自己不在的时候\n',
            '这家店的经营状况很好，\n',
            '有点不甘心吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '呵呵，还是老样子，\n',
            '又顽固又不会轻易认输呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '以后我们之间就要竞争了。\n',
            '为了不输给他，我还要加油才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2CDD')

    def _loc_2C6D(): pass

    label('loc_2C6D')

    ChrTalk(
        0x000D,
        (
            '呵呵，还是老样子，\n',
            '又顽固又不会轻易认输呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '以后我们之间就要竞争了。\n',
            '为了不输给他，我还要加油才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2CDD(): pass

    label('loc_2CDD')

    Jump('loc_33CC')

    def _loc_2CE0(): pass

    label('loc_2CE0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_2DAA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2D58',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x000D,
        (
            '嘿嘿，\n',
            '来这里的客人正在慢慢增加哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '他一定会很高兴的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '不知道他能不能早点回来呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2DA7')

    def _loc_2D58(): pass

    label('loc_2D58')

    ChrTalk(
        0x000D,
        (
            '……明明已经找到了定期船，\n',
            '为什么他还没有回来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '我……一定要加油。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2DA7(): pass

    label('loc_2DA7')

    Jump('loc_33CC')

    def _loc_2DAA(): pass

    label('loc_2DAA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_2E12',
    )

    ChrTalk(
        0x000D,
        (
            '听说军队找到\n',
            '失踪的定期船了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '那么他……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '不知道飞艇上的乘客们\n',
            '现在怎样了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_33CC')

    def _loc_2E12(): pass

    label('loc_2E12')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_3101',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_2E6F',
    )

    ChrTalk(
        0x000D,
        (
            '欢迎光临～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '柏斯超市的名产——\n',
            '软绵绵香蛋糕，\n',
            '客人要来一块吗～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_30FE')

    def _loc_2E6F(): pass

    label('loc_2E6F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_307D',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x000D,
        (
            '……这家店，\n',
            '其实是我的未婚夫开设的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '他乘坐了那艘\n',
            '如今已经成为话题的消失的定期船。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '但是，\n',
            '我一直坚信他一定会回来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '在他回来之前，\n',
            '我一定要守护好这家店……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#003F………………………………\n',
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 0)

    ChrTalk(
        0x0102,
        (
            '#012F艾丝蒂尔，你怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#002F……说的是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#014F啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#003F失踪的飞艇上\n',
            '不单有自己的亲人乘坐啊，\n',
            '还有其他的百姓的亲人也在里面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#009F那么，\n',
            '我就要更加努力才行呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '作为游击士协会的一员，\n',
            '也作为父亲的女儿！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F艾丝蒂尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '嗯，说得对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_30FE')

    def _loc_307D(): pass

    label('loc_307D')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x000D,
        (
            '………………………………\n',
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x000D,
        (
            '啊，对、对不起。\n',
            '欢迎光临！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_30FE(): pass

    label('loc_30FE')

    Jump('loc_33CC')

    def _loc_3101(): pass

    label('loc_3101')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_3173',
    )

    ChrTalk(
        0x000D,
        (
            '嘿嘿，\n',
            '刚开始稍微有点迷茫……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '不过现在终于开始\n',
            '能够顺利地卖出去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '总之带着微笑努力吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_33CC')

    def _loc_3173(): pass

    label('loc_3173')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_326A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_320A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x000D,
        (
            '我最近开始\n',
            '帮忙经营这家店，\n',
            '不过还是很不习惯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '招呼客人的时候\n',
            '也觉得非常害羞呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '唉～不行啊。\n',
            '再这样下去的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3267')

    def _loc_320A(): pass

    label('loc_320A')

    ChrTalk(
        0x000D,
        (
            '我最近开始\n',
            '帮忙经营这家店，\n',
            '不过还是很不习惯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '招呼客人的时候\n',
            '也觉得非常害羞呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3267(): pass

    label('loc_3267')

    Jump('loc_33CC')

    def _loc_326A(): pass

    label('loc_326A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_33CC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3382',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x000D,
        (
            '欢迎光临～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '柏斯超市的名产——\n',
            '软绵绵香蛋糕，\n',
            '客人要来一份吗～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#001F哇，看上去很好吃呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F真的……\n',
            '味道很香呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#001F约修亚，找到父亲之后，\n',
            '我们一起来这里吃蛋糕吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#011F……嗯，好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#001F真的？\n',
            '那就说定了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_33CC')

    def _loc_3382(): pass

    label('loc_3382')

    ChrTalk(
        0x000D,
        (
            '欢迎光临～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '柏斯超市的名产——\n',
            '软绵绵香蛋糕，\n',
            '客人要来一份吗～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_33CC(): pass

    label('loc_33CC')

    TalkEnd(0x000D)

    Return()

# id: 0x0015 offset: 0x33D0
@scena.Code('func_15_33D0')
def func_15_33D0():
    Call(0, 0x0016)

    Return()

# id: 0x0016 offset: 0x33D5
@scena.Code('func_16_33D5')
def func_16_33D5():
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
        'loc_3433',
    )

    OP_0D()
    OP_A9(0x19)
    OP_56(0x00)
    TalkEnd(0x000E)

    Return()

    def _loc_3433(): pass

    label('loc_3433')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3444',
    )

    TalkEnd(0x000E)

    Return()

    def _loc_3444(): pass

    label('loc_3444')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_3551',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_34EF',
    )

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x000E,
        (
            '因为飞艇停运，\n',
            '服装等商品还是很难进到货。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '不过相反的，\n',
            '本店自己设计的服装\n',
            '比预想中卖得还要好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '好～为了我的家人，\n',
            '一定要更加努力才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_354E')

    def _loc_34EF(): pass

    label('loc_34EF')

    ChrTalk(
        0x000E,
        (
            '作为试验的\n',
            '本店原创服装\n',
            '比预想中卖的还要好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '好～为了我的家人，\n',
            '一定要更加努力才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_354E(): pass

    label('loc_354E')

    Jump('loc_3B95')

    def _loc_3551(): pass

    label('loc_3551')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_360F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_35CB',
    )

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x000E,
        (
            '那件事有没有\n',
            '让她和女儿感到心有余悸呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '嗯～\n',
            '我觉得强盗还是会再来，\n',
            '担心得无法好好工作呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_360C')

    def _loc_35CB(): pass

    label('loc_35CB')

    ChrTalk(
        0x000E,
        (
            '……好，我决定了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '今天就不营业了，\n',
            '我还是早点回家吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_360C(): pass

    label('loc_360C')

    Jump('loc_3B95')

    def _loc_360F(): pass

    label('loc_360F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_374E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_36ED',
    )

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x000E,
        (
            '昨晚，\n',
            '有强盗擅自闯入我家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '正好那个时候，\n',
            '家里只有我妻子和女儿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '虽然两个人都没什么事，\n',
            '但是她们好像受到了不小的惊吓。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '今天早上，\n',
            '虽然妻子微笑着送我出门，\n',
            '但是我还是很担心家里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_374B')

    def _loc_36ED(): pass

    label('loc_36ED')

    ChrTalk(
        0x000E,
        (
            '昨晚有强盗擅自闯入我家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '今天早上，\n',
            '虽然妻子微笑着送我出门，\n',
            '但是我还是很担心家里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_374B(): pass

    label('loc_374B')

    Jump('loc_3B95')

    def _loc_374E(): pass

    label('loc_374E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_381E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_37B9',
    )

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x000E,
        (
            '自己设计并且自己缝制的衣服\n',
            '卖得也相当不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '好，\n',
            '我还要多设计几种样式才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_381B')

    def _loc_37B9(): pass

    label('loc_37B9')

    ChrTalk(
        0x000E,
        (
            '对于原创的衣服，\n',
            '来这里询问的女性顾客比较多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '下次我试着以女性服装\n',
            '为中心来设计看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_381B(): pass

    label('loc_381B')

    Jump('loc_3B95')

    def _loc_381E(): pass

    label('loc_381E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_391A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_38AE',
    )

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x000E,
        (
            '在王都发行的新款服装\n',
            '没办法进到货了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '而且店里的存货\n',
            '也渐渐少起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '这下子只能大幅增加\n',
            '原创服装的数量了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3917')

    def _loc_38AE(): pass

    label('loc_38AE')

    ChrTalk(
        0x000E,
        (
            '其实之前就曾经尝试过\n',
            '增加本店的原创服装数量，\n',
            '效果还不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '趁这个机会再试一下\n',
            '也不是什么坏事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3917(): pass

    label('loc_3917')

    Jump('loc_3B95')

    def _loc_391A(): pass

    label('loc_391A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_3A50',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_39F5',
    )

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x000E,
        (
            '我本来是\n',
            '王国军的一名军官。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '不过因为怎么也放不下梦想，\n',
            '所以就开了这样一家店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '不过妻子却很反对我这么做。\n',
            '为了得到她的理解，我要更加努力才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '自从我回来做生意，\n',
            '女儿也很高兴呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3A4D')

    def _loc_39F5(): pass

    label('loc_39F5')

    ChrTalk(
        0x000E,
        (
            '我本来是\n',
            '王国军的一名军官。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '不过因为怎么也放不下梦想，\n',
            '所以就开了这样一家店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3A4D(): pass

    label('loc_3A4D')

    Jump('loc_3B95')

    def _loc_3A50(): pass

    label('loc_3A50')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_3B95',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3B54',
    )

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x000E,
        (
            '欢迎光临。\n',
            '今天想要买些什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '本店能够订购到\n',
            '王都的品牌服饰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '可以的话，就多看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F这里好像是卖衣服的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F我很喜欢这套衣服啊。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000E, 0x0101, 0)

    ChrTalk(
        0x000E,
        (
            '有自己喜欢的款式的话，\n',
            '还可以专门给您订制。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '欢迎再来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3B95')

    def _loc_3B54(): pass

    label('loc_3B54')

    ChrTalk(
        0x000E,
        (
            '有自己喜欢的款式的话，\n',
            '还可以专门给您订制。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '欢迎再来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3B95(): pass

    label('loc_3B95')

    TalkEnd(0x000E)

    Return()

# id: 0x0017 offset: 0x3B99
@scena.Code('func_17_3B99')
def func_17_3B99():
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
        'loc_3C0F',
    )

    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 4, 0x35C)),
            Expr.Return,
        ),
        'loc_3BFB',
    )

    OP_A9(0x6E)

    Jump('loc_3C09')

    def _loc_3BFB(): pass

    label('loc_3BFB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_3C07',
    )

    OP_A9(0x1B)

    Jump('loc_3C09')

    def _loc_3C07(): pass

    label('loc_3C07')

    OP_A9(0x1A)

    def _loc_3C09(): pass

    label('loc_3C09')

    OP_56(0x00)
    TalkEnd(0x000F)

    Return()

    def _loc_3C0F(): pass

    label('loc_3C0F')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3C20',
    )

    TalkEnd(0x000F)

    Return()

    def _loc_3C20(): pass

    label('loc_3C20')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_3C70',
    )

    ChrTalk(
        0x00FE,
        (
            '顾客需要的商品\n',
            '经常会有变化。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '必须要摸清楚规律\n',
            '来进货才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_431D')

    def _loc_3C70(): pass

    label('loc_3C70')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_3D36',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3D06',
    )

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '商品的采购终于\n',
            '能够恢复原来的样子了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '趁这个机会\n',
            '再增加一些实用性商品吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我可是那种跌倒了\n',
            '也不会轻易认输的性格。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3D33')

    def _loc_3D06(): pass

    label('loc_3D06')

    ChrTalk(
        0x00FE,
        (
            '我可是那种跌倒了\n',
            '也不会轻易认输的性格。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3D33(): pass

    label('loc_3D33')

    Jump('loc_431D')

    def _loc_3D36(): pass

    label('loc_3D36')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_3DAF',
    )

    ChrTalk(
        0x00FE,
        (
            '听说城里被\n',
            '强盗洗劫了是吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '把别人的东西占为己有，\n',
            '真不像话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望有人能够快点\n',
            '把那些家伙抓住。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_431D')

    def _loc_3DAF(): pass

    label('loc_3DAF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_3EFD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3EB9',
    )

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '您好，欢迎光临！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '顺便过来看看吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就现在！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '什么！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '共和国产的高级绒毯\n',
            '只要５００米拉！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要５００米拉哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '平时要卖\n',
            '１５００米拉的商品\n',
            '现在只要５００米拉！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '先到先得哦！\n',
            '而且现在还赠送一条\n',
            '相同模样的挂毯哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3EFA')

    def _loc_3EB9(): pass

    label('loc_3EB9')

    ChrTalk(
        0x00FE,
        (
            '共和国产的高级绒毯\n',
            '只要５００米拉！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要５００米拉哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3EFA(): pass

    label('loc_3EFA')

    Jump('loc_431D')

    def _loc_3EFD(): pass

    label('loc_3EFD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_3FF9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3F8E',
    )

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '真是的，军队打算把道路\n',
            '和国际空港封锁到什么时候啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本应从帝国送过来的商品\n',
            '现在也到达不了了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是难办啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3FF6')

    def _loc_3F8E(): pass

    label('loc_3F8E')

    ChrTalk(
        0x00FE,
        (
            '真是的，军队打算把道路\n',
            '和国际空港封锁到什么时候啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本应从帝国送过来的商品\n',
            '现在也到达不了了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3FF6(): pass

    label('loc_3FF6')

    Jump('loc_431D')

    def _loc_3FF9(): pass

    label('loc_3FF9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_4178',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4113',
    )

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '我从青空市场时代开始\n',
            '就在这里开店了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '算是现在超市中最老的店铺吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哇，您的资历真老啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '多谢夸奖……\n',
            '不过这都是４０多年前的事情了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个时候，\n',
            '这里还没有这么漂亮的建筑物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '柏斯也起了翻天覆地的变化，\n',
            '不过人们的热情却一直没变。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4175')

    def _loc_4113(): pass

    label('loc_4113')

    ChrTalk(
        0x00FE,
        (
            '这个市场建起来之前，\n',
            '在那个青空市场时代\n',
            '我就在这里开店了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '算是现在超市中最老的店铺吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4175(): pass

    label('loc_4175')

    Jump('loc_431D')

    def _loc_4178(): pass

    label('loc_4178')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_431D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_42C2',
    )

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '您好，欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从古书到织品，还有日用品，\n',
            '米蕾婆婆的杂货店应有尽有哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哇哇，有好多东西呀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '同样是杂货店，\n',
            '比里农叔叔店里的\n',
            '东西要多得多呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F嗯，真不愧是超市里开的店，\n',
            '感觉就是不一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我这里可是有许多从\n',
            '帝国与共和国带来的舶来品哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我对自家店的商品还是很有信心的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_431D')

    def _loc_42C2(): pass

    label('loc_42C2')

    ChrTalk(
        0x00FE,
        (
            '我这里可是有许多从\n',
            '帝国与共和国带来的舶来品哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我对自家店的商品还是很有信心的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_431D(): pass

    label('loc_431D')

    TalkEnd(0x000F)

    Return()

# id: 0x0018 offset: 0x4321
@scena.Code('func_18_4321')
def func_18_4321():
    TalkBegin(0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_440F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_43CF',
    )

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '洋葱和胡萝卜\n',
            '还有还有……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '洋葱和胡萝卜\n',
            '还有还有……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，好像还有肉吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_440C')

    def _loc_43CF(): pass

    label('loc_43CF')

    ChrTalk(
        0x00FE,
        (
            '洋葱～胡萝卜～\n',
            '还·有·肉⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '编成歌就很容易记住了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_440C(): pass

    label('loc_440C')

    Jump('loc_4701')

    def _loc_440F(): pass

    label('loc_440F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_44BD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_449D',
    )

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '嘿嘿嘿，\n',
            '我终于能够独自一人出来买东西了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '很厉害吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，\n',
            '我只买过卷心菜，\n',
            '除此之外就没有试过其他的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_44BA')

    def _loc_449D(): pass

    label('loc_449D')

    ChrTalk(
        0x00FE,
        (
            '我要努力\n',
            '早点成为大人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_44BA(): pass

    label('loc_44BA')

    Jump('loc_4701')

    def _loc_44BD(): pass

    label('loc_44BD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_44FC',
    )

    ChrTalk(
        0x00FE,
        (
            '外面有很多\n',
            '好可怕的叔叔呀。',
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

    Jump('loc_4701')

    def _loc_44FC(): pass

    label('loc_44FC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_455E',
    )

    ChrTalk(
        0x00FE,
        (
            '这个蛋糕\n',
            '看起来好好吃啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '出来买东西的钱\n',
            '不能乱花呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4701')

    def _loc_455E(): pass

    label('loc_455E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_4647',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_45E6',
    )

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '卷心菜、卷心菜……\n',
            '是我妈妈让我买的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和不认识的人说话\n',
            '总觉得有点可怕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好不容易\n',
            '来到商店前面了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4644')

    def _loc_45E6(): pass

    label('loc_45E6')

    ChrTalk(
        0x00FE,
        (
            '对了，先练习一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请给我１棵卷心菜……\n',
            '请给我１棵卷心菜……\n',
            '请给我１棵卷心菜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4644(): pass

    label('loc_4644')

    Jump('loc_4701')

    def _loc_4647(): pass

    label('loc_4647')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_46A8',
    )

    ChrTalk(
        0x00FE,
        (
            '呜～\n',
            '忘记该买什么东西了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难得妈妈拜托我买东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还是回家问问吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4701')

    def _loc_46A8(): pass

    label('loc_46A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_4701',
    )

    ChrTalk(
        0x00FE,
        (
            '嘿嘿嘿，\n',
            '这可是我出生以来第一次自己出来办事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……嗯，\n',
            '我要买什么来着？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4701(): pass

    label('loc_4701')

    TalkEnd(0x0010)

    Return()

# id: 0x0019 offset: 0x4705
@scena.Code('func_19_4705')
def func_19_4705():
    TalkBegin(0x0011)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_47B5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_477B',
    )

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    ChrTalk(
        0x00FE,
        (
            '偶尔也奢侈一次，\n',
            '买点牛排尝尝吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果决定要大吃一顿的话，\n',
            '做什么菜也就容易考虑了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_47B2')

    def _loc_477B(): pass

    label('loc_477B')

    ChrTalk(
        0x00FE,
        (
            '如果决定要大吃一顿的话，\n',
            '做什么菜也就容易考虑了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_47B2(): pass

    label('loc_47B2')

    Jump('loc_4B6C')

    def _loc_47B5(): pass

    label('loc_47B5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_4877',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_483D',
    )

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    ChrTalk(
        0x00FE,
        (
            '啊啊～干脆让我们家的人\n',
            '轮流来考虑每天吃什么好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '或者，\n',
            '事先决定好一个星期的安排，\n',
            '然后不断重复怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4874')

    def _loc_483D(): pass

    label('loc_483D')

    ChrTalk(
        0x00FE,
        (
            '啊啊～干脆让我们家的人\n',
            '轮流来考虑每天吃什么好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4874(): pass

    label('loc_4874')

    Jump('loc_4B6C')

    def _loc_4877(): pass

    label('loc_4877')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_4977',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4932',
    )

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    ChrTalk(
        0x00FE,
        (
            '肉、蔬菜、鱼……\n',
            '嗯～今天做什么好呢。\n',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管是强盗来，\n',
            '还是王国军来，\n',
            '都要考虑做什么菜啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊～\n',
            '女王陛下能不能让我有一天\n',
            '可以不用为做什么菜而烦恼呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4974')

    def _loc_4932(): pass

    label('loc_4932')

    ChrTalk(
        0x00FE,
        (
            '啊啊～\n',
            '女王陛下能不能让我有一天\n',
            '可以不用为做什么菜而烦恼呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4974(): pass

    label('loc_4974')

    Jump('loc_4B6C')

    def _loc_4977(): pass

    label('loc_4977')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_49EF',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯～\n',
            '今天做什么菜比较好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是伤脑筋啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我本来想来店里之后再决定的，\n',
            '不过好像还是决定不了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4B6C')

    def _loc_49EF(): pass

    label('loc_49EF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_4A9C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4A7E',
    )

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    ChrTalk(
        0x00FE,
        (
            '今天轮到吃肉了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到底是做牛排呢，\n',
            '还是炖肉呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊～真伤脑筋……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '考虑每天的菜单\n',
            '真是一件痛苦的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4A99')

    def _loc_4A7E(): pass

    label('loc_4A7E')

    ChrTalk(
        0x00FE,
        (
            '唔……\n',
            '还是改做鱼吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4A99(): pass

    label('loc_4A99')

    Jump('loc_4B6C')

    def _loc_4A9C(): pass

    label('loc_4A9C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_4B21',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4B01',
    )

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    ChrTalk(
        0x00FE,
        (
            '好，决定了！\n',
            '今天就做鱼好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，到底是烧着吃呢，\n',
            '还是煮着吃呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4B1E')

    def _loc_4B01(): pass

    label('loc_4B01')

    ChrTalk(
        0x00FE,
        (
            '嗯，\n',
            '我想还是改做肉吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4B1E(): pass

    label('loc_4B1E')

    Jump('loc_4B6C')

    def _loc_4B21(): pass

    label('loc_4B21')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_4B6C',
    )

    ChrTalk(
        0x00FE,
        (
            '那～么，\n',
            '今天做些什么菜比较好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是烧肉呢，\n',
            '还是煮鱼呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4B6C(): pass

    label('loc_4B6C')

    TalkEnd(0x0011)

    Return()

# id: 0x001A offset: 0x4B70
@scena.Code('func_1A_4B70')
def func_1A_4B70():
    TalkBegin(0x0012)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_4C12',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4BE2',
    )

    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    ChrTalk(
        0x00FE,
        (
            '为了攒够买书的钱，\n',
            '我决定在这里打工了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过我倒是没想到会在\n',
            '经常光顾的店打工。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4C0F')

    def _loc_4BE2(): pass

    label('loc_4BE2')

    ChrTalk(
        0x00FE,
        (
            '不过我倒是没想到会在\n',
            '经常光顾的店打工。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4C0F(): pass

    label('loc_4C0F')

    Jump('loc_4F7F')

    def _loc_4C12(): pass

    label('loc_4C12')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_4DB6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0072, 4, 0x394)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4D56',
    )

    SetScenaFlags(ScenaFlag(0x0072, 4, 0x394))

    ChrTalk(
        0x00FE,
        (
            '我是想来买小说的续篇的，\n',
            '果然还是没有进货呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我对于一本已经读过一遍的书，\n',
            '基本上不会再去看第二遍。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这本书就送给你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    AddItem(0x0215, 1)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '红耀石　第４卷',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x00FE,
        (
            '刚才，\n',
            '店里的老婆婆问我\n',
            '是不是想在这里工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是不是因为我总是\n',
            '在询问商品的缘故呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4DB3')

    def _loc_4D56(): pass

    label('loc_4D56')

    ChrTalk(
        0x00FE,
        (
            '刚才，\n',
            '店里的老婆婆问我\n',
            '是不是想在这里工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是不是因为我总是\n',
            '在询问商品的缘故呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4DB3(): pass

    label('loc_4DB3')

    Jump('loc_4F7F')

    def _loc_4DB6(): pass

    label('loc_4DB6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_4E1B',
    )

    ChrTalk(
        0x00FE,
        (
            '老旧而又贵重的书籍\n',
            '还是要悉心地保管\n',
            '比较好啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我这就去向\n',
            '店里的老婆婆说一声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4F7F')

    def _loc_4E1B(): pass

    label('loc_4E1B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_4E6F',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯～\n',
            '里面的书都布满灰尘了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '问店里的人借个掸子，\n',
            '打扫一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4F7F')

    def _loc_4E6F(): pass

    label('loc_4E6F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_4ECB',
    )

    ChrTalk(
        0x00FE,
        (
            '最近外国的书\n',
            '都进不货呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是因为军队制订的那些\n',
            '各种各样的规章制度吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4F7F')

    def _loc_4ECB(): pass

    label('loc_4ECB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_4F42',
    )

    ChrTalk(
        0x00FE,
        (
            '每次路过这里，\n',
            '我都会过来看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为来得次数太多，\n',
            '对于这家店，\n',
            '我有自信比店里的人了解得更详细哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4F7F')

    def _loc_4F42(): pass

    label('loc_4F42')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_4F7F',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯～没有我看得中的书啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还是找找其他的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4F7F(): pass

    label('loc_4F7F')

    TalkEnd(0x0012)

    Return()

# id: 0x001B offset: 0x4F83
@scena.Code('func_1B_4F83')
def func_1B_4F83():
    TalkBegin(0x0013)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_5049',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5018',
    )

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    ChrTalk(
        0x00FE,
        (
            '啊啊～真可惜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '蛋糕店的大姐\n',
            '原来已经订婚了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然有点失望，\n',
            '不过作为大姐的忠实支持者\n',
            '我以后还会经常光顾的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5046')

    def _loc_5018(): pass

    label('loc_5018')

    ChrTalk(
        0x00FE,
        (
            '啊啊～……\n',
            '蛋糕店的大姐\n',
            '原来已经订婚了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5046(): pass

    label('loc_5046')

    Jump('loc_5345')

    def _loc_5049(): pass

    label('loc_5049')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_50A3',
    )

    ChrTalk(
        0x00FE,
        (
            '果然，\n',
            '这家店越来越受市民欢迎了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和我想的一样，\n',
            '大姐她也非常努力呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5345')

    def _loc_50A3(): pass

    label('loc_50A3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_512C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5101',
    )

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    ChrTalk(
        0x00FE,
        (
            '最近蛋糕店的大姐\n',
            '好像没什么精神……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是不是在为什么事情担心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5129')

    def _loc_5101(): pass

    label('loc_5101')

    ChrTalk(
        0x00FE,
        (
            '最近，总是发生一些令人不安的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5129(): pass

    label('loc_5129')

    Jump('loc_5345')

    def _loc_512C(): pass

    label('loc_512C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_5203',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_51BB',
    )

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    ChrTalk(
        0x00FE,
        (
            '那家蛋糕店啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '自从大姐开始接管以来，\n',
            '味道也变得非常好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然我每天都吃，\n',
            '不过它的味道可是一天比一天好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5200')

    def _loc_51BB(): pass

    label('loc_51BB')

    ChrTalk(
        0x00FE,
        (
            '那家蛋糕店啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '自从大姐开始接管以来，\n',
            '味道也变得非常好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5200(): pass

    label('loc_5200')

    Jump('loc_5345')

    def _loc_5203(): pass

    label('loc_5203')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_526E',
    )

    ChrTalk(
        0x00FE,
        (
            '自从大姐\n',
            '开始接手蛋糕店，\n',
            '蛋糕的销量也变好了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也是因为能看到\n',
            '大姐的微笑才去买的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5345')

    def _loc_526E(): pass

    label('loc_526E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_52DC',
    )

    ChrTalk(
        0x00FE,
        (
            '那家店的大姐\n',
            '健康的微笑真是迷人啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了能见到她的笑脸，\n',
            '要我一天之内买多少个蛋糕都可以。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5345')

    def _loc_52DC(): pass

    label('loc_52DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_5345',
    )

    ChrTalk(
        0x00FE,
        (
            '软绵绵香蛋糕的店里的\n',
            '服务员好像换成一位女性了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '之前明明是个男的，\n',
            '难道发生什么事了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5345(): pass

    label('loc_5345')

    TalkEnd(0x0013)

    Return()

# id: 0x001C offset: 0x5349
@scena.Code('func_1C_5349')
def func_1C_5349():
    TalkBegin(0x0014)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_542A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_53D3',
    )

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))

    ChrTalk(
        0x00FE,
        (
            '我非常喜欢\n',
            '这个超市给人的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算会惹父母生气，\n',
            '我也要偷偷到这里来玩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为总是呆在家里好无聊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5427')

    def _loc_53D3(): pass

    label('loc_53D3')

    ChrTalk(
        0x00FE,
        (
            '我非常喜欢\n',
            '这个超市给人的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算会惹父母生气，\n',
            '我也要偷偷到这里来玩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5427(): pass

    label('loc_5427')

    Jump('loc_5881')

    def _loc_542A(): pass

    label('loc_542A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_554A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_54C2',
    )

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))

    ChrTalk(
        0x00FE,
        (
            '虽然父母反对我来这里，\n',
            '但是我非常喜欢\n',
            '这个超市给人的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以，\n',
            '我还是偷偷到这里来玩了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为总是呆在家里好无聊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5547')

    def _loc_54C2(): pass

    label('loc_54C2')

    ChrTalk(
        0x00FE,
        (
            '在这里可以听到各种各样的话题，\n',
            '可以品尝各类食物，\n',
            '还可以见识到许多人和事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我觉得来这里体验生活\n',
            '对于自己来说是非常必要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5547(): pass

    label('loc_5547')

    Jump('loc_5881')

    def _loc_554A(): pass

    label('loc_554A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_559C',
    )

    ChrTalk(
        0x00FE,
        (
            '我去超市的事情\n',
            '被我妈妈发现了，\n',
            '然后被狠狠地骂了一顿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5881')

    def _loc_559C(): pass

    label('loc_559C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_56D5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5676',
    )

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))

    ChrTalk(
        0x00FE,
        (
            '刚才，\n',
            '我第一次尝试自己买东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就是在喷水池旁边卖的\n',
            '软绵绵的像点心那样的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家好像都在\n',
            '那个地方吃东西，\n',
            '我就模仿他们也吃了一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '非常好吃。\n',
            '这给了我一个非常珍贵的体验。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_56D2')

    def _loc_5676(): pass

    label('loc_5676')

    ChrTalk(
        0x00FE,
        (
            '虽然在屋外吃东西\n',
            '感觉有损形象……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，我觉得只有在这个地方\n',
            '才能品味出它的美味。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_56D2(): pass

    label('loc_56D2')

    Jump('loc_5881')

    def _loc_56D5(): pass

    label('loc_56D5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_5723',
    )

    ChrTalk(
        0x00FE,
        (
            '总像这样只是看着\n',
            '也不是办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就在这里\n',
            '试着买点什么吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5881')

    def _loc_5723(): pass

    label('loc_5723')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_578F',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然是偷偷跑过来玩的，\n',
            '不过看到了好多稀奇的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '原来大家都是在\n',
            '这种地方买东西的啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5881')

    def _loc_578F(): pass

    label('loc_578F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_5881',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5829',
    )

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))

    ChrTalk(
        0x00FE,
        (
            '虽然我一直住在柏斯，\n',
            '但这还是我第一次来到超市。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯～\n',
            '总觉得这里好像乱糟糟的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且……咳咳……\n',
            '怎么会有这么脏的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5881')

    def _loc_5829(): pass

    label('loc_5829')

    ChrTalk(
        0x00FE,
        (
            '虽然我一直住在柏斯，\n',
            '但这还是我第一次来到超市。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯～\n',
            '总觉得这里好像乱糟糟的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5881(): pass

    label('loc_5881')

    TalkEnd(0x0014)

    Return()

# id: 0x001D offset: 0x5885
@scena.Code('func_1D_5885')
def func_1D_5885():
    TalkBegin(0x0015)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_5907',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_58E1',
    )

    SetScenaFlags(ScenaFlag(0x0002, 0, 0x10))

    ChrTalk(
        0x00FE,
        (
            '呵呵，\n',
            '今天又进了一些餐具。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔唔……\n',
            '这才是东方的精品啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5904')

    def _loc_58E1(): pass

    label('loc_58E1')

    ChrTalk(
        0x00FE,
        (
            '唔唔……\n',
            '这才是东方的精品啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5904(): pass

    label('loc_5904')

    Jump('loc_5CCA')

    def _loc_5907(): pass

    label('loc_5907')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_5974',
    )

    ChrTalk(
        0x00FE,
        (
            '我听说，\n',
            '共和国东边有许多国家\n',
            '也制作各式各样的陶器。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我一直想找个时间\n',
            '进行探求陶器之旅。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5CCA')

    def _loc_5974(): pass

    label('loc_5974')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_59C7',
    )

    ChrTalk(
        0x00FE,
        (
            '不知道为什么\n',
            '有许多军人在城里出入……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '给人一种盛气凌人的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5CCA')

    def _loc_59C7(): pass

    label('loc_59C7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_5B13',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5AAA',
    )

    SetScenaFlags(ScenaFlag(0x0002, 0, 0x10))

    ChrTalk(
        0x00FE,
        (
            '帝国产的陶器拥有豪华绚烂的装饰，\n',
            '非常具有艺术性。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '相反，\n',
            '共和国的陶器颜色与装饰都非常朴素，\n',
            '但是会让人有种一直想用下去的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真的是各有特色啊。\n',
            '正因为如此，陶器这种东西才会让人觉得很有趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5B10')

    def _loc_5AAA(): pass

    label('loc_5AAA')

    ChrTalk(
        0x00FE,
        (
            '顺便提一下，\n',
            '利贝尔的陶器在外形和装饰上都非常简单，\n',
            '但是充满高雅气质。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……我是这么感觉的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5B10(): pass

    label('loc_5B10')

    Jump('loc_5CCA')

    def _loc_5B13(): pass

    label('loc_5B13')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_5C38',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5BDF',
    )

    SetScenaFlags(ScenaFlag(0x0002, 0, 0x10))

    ChrTalk(
        0x00FE,
        (
            '发现它潜在的价值，\n',
            '然后低价购进。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我现在越来越体会到\n',
            '买卖古董的最大乐趣了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说本来我还是一个门外汉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样一挑一选、一买一卖，\n',
            '呵呵，就可以将大半的破烂化成钱财。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5C35')

    def _loc_5BDF(): pass

    label('loc_5BDF')

    ChrTalk(
        0x00FE,
        (
            '发现它潜在的价值，\n',
            '然后低价购进。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我现在越来越体会到\n',
            '买卖古董的最大乐趣了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5C35(): pass

    label('loc_5C35')

    Jump('loc_5CCA')

    def _loc_5C38(): pass

    label('loc_5C38')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_5CA6',
    )

    ChrTalk(
        0x00FE,
        (
            '我喜欢去淘一些\n',
            '被挖掘出来的古董。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要看到品种各异的古董摆在面前，\n',
            '我整个人就会坐立不安。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5CCA')

    def _loc_5CA6(): pass

    label('loc_5CA6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_5CCA',
    )

    ChrTalk(
        0x00FE,
        (
            '唔……\n',
            '这个东西有点……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5CCA(): pass

    label('loc_5CCA')

    TalkEnd(0x0015)

    Return()

# id: 0x001E offset: 0x5CCE
@scena.Code('func_1E_5CCE')
def func_1E_5CCE():
    TalkBegin(0x0016)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_5D77',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5D4F',
    )

    SetScenaFlags(ScenaFlag(0x0002, 1, 0x11))

    ChrTalk(
        0x00FE,
        (
            '买不到新鲜的东西\n',
            '真是很痛苦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果在便宜的时候\n',
            '能够多买一些的话，\n',
            '就能改善家庭财政状况了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5D74')

    def _loc_5D4F(): pass

    label('loc_5D4F')

    ChrTalk(
        0x00FE,
        (
            '买不到新鲜的东西\n',
            '真是很痛苦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5D74(): pass

    label('loc_5D74')

    Jump('loc_60D7')

    def _loc_5D77(): pass

    label('loc_5D77')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_5E6D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5E20',
    )

    SetScenaFlags(ScenaFlag(0x0002, 1, 0x11))

    ChrTalk(
        0x00FE,
        (
            '嘿嘿嘿，\n',
            '我有今天的打折券哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '用什么手段\n',
            '才能买到便宜好货……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这已经成为\n',
            '我的生存价值之一了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，\n',
            '现在开始履行主妇的本分吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5E6A')

    def _loc_5E20(): pass

    label('loc_5E20')

    ChrTalk(
        0x00FE,
        (
            '用什么手段\n',
            '才能买到便宜好货……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这已经成为\n',
            '我的生存价值之一了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5E6A(): pass

    label('loc_5E6A')

    Jump('loc_60D7')

    def _loc_5E6D(): pass

    label('loc_5E6D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_5F17',
    )

    ChrTalk(
        0x00FE,
        (
            '今天没有哪家商店\n',
            '进行特价大甩卖呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，绝不能疏忽对情报的收集。\n',
            '为了我家明天的帐簿着想！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说不定明天\n',
            '就会有什么出乎意料的\n',
            '绝世珍宝被我发现呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_60D7')

    def _loc_5F17(): pass

    label('loc_5F17')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_5FE4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5F9D',
    )

    SetScenaFlags(ScenaFlag(0x0002, 1, 0x11))

    ChrTalk(
        0x00FE,
        (
            '哼，我不甘心！\n',
            '这算什么意思！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天，\n',
            '我已经身无分文了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我对这家店大甩卖的时机\n',
            '竟然预测失误……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5FE1')

    def _loc_5F9D(): pass

    label('loc_5F9D')

    ChrTalk(
        0x00FE,
        (
            '哼，我不甘心！\n',
            '这算什么意思！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天，\n',
            '我已经身无分文了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5FE1(): pass

    label('loc_5FE1')

    Jump('loc_60D7')

    def _loc_5FE4(): pass

    label('loc_5FE4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_603E',
    )

    ChrTalk(
        0x00FE,
        (
            '今天从三点开始\n',
            '一定会有减价肉卖的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '得赶快去商店前面\n',
            '占个好位置等着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_60D7')

    def _loc_603E(): pass

    label('loc_603E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_6099',
    )

    ChrTalk(
        0x00FE,
        (
            '如果想买到广告促销品，\n',
            '就一定要在超市开业前去排队。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这是基本中的基本。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_60D7')

    def _loc_6099(): pass

    label('loc_6099')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_60D7',
    )

    ChrTalk(
        0x00FE,
        (
            '那么～\n',
            '今天哪家店会有促销呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '赶快记下来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_60D7(): pass

    label('loc_60D7')

    TalkEnd(0x0016)

    Return()

# id: 0x001F offset: 0x60DB
@scena.Code('func_1F_60DB')
def func_1F_60DB():
    TalkBegin(0x0018)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_6149',
    )

    ChrTalk(
        0x00FE,
        (
            '多亏了飞艇停航，\n',
            '让我能够称心如意地\n',
            '在周围抢购一番了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我丈夫都被我吓傻了吧，\n',
            '嘿嘿嘿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_62AF')

    def _loc_6149(): pass

    label('loc_6149')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_61C1',
    )

    ChrTalk(
        0x00FE,
        (
            '好便宜啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是买了那个的话，\n',
            '就会成为我旅途的负担了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还是让他把东西送到\n',
            '我在王都的家里吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_62AF')

    def _loc_61C1(): pass

    label('loc_61C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_623C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 2, 0x12)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_621F',
    )

    SetScenaFlags(ScenaFlag(0x0002, 2, 0x12))

    ChrTalk(
        0x00FE,
        (
            '好～接下来去哪家呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就是为了今天，\n',
            '我才和丈夫一起出来巡礼的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6239')

    def _loc_621F(): pass

    label('loc_621F')

    ChrTalk(
        0x00FE,
        (
            '好～接下来去哪家呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6239(): pass

    label('loc_6239')

    Jump('loc_62AF')

    def _loc_623C(): pass

    label('loc_623C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_62AF',
    )

    ChrTalk(
        0x00FE,
        (
            '呵呵，虽然有点对不起丈夫，\n',
            '不过飞艇停航了还真是一件好事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样的话就可以\n',
            '慢慢享受购物的乐趣了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_62AF(): pass

    label('loc_62AF')

    TalkEnd(0x0018)

    Return()

# id: 0x0020 offset: 0x62B3
@scena.Code('func_20_62B3')
def func_20_62B3():
    TalkBegin(0x0017)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_63C1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 3, 0x13)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6364',
    )

    SetScenaFlags(ScenaFlag(0x0002, 3, 0x13))

    ChrTalk(
        0x00FE,
        (
            '定期船的航运\n',
            '终于恢复正常了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这下终于可以去卢安了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到时候一定要密切注意\n',
            '妻子的购物癖呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我觉得人嘛，\n',
            '还是要稍微勤俭节约一点的好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_63BE')

    def _loc_6364(): pass

    label('loc_6364')

    ChrTalk(
        0x00FE,
        (
            '到时候一定要密切注意\n',
            '妻子的购物癖呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我觉得人嘛，\n',
            '还是要稍微勤俭节约一点的好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_63BE(): pass

    label('loc_63BE')

    Jump('loc_66A9')

    def _loc_63C1(): pass

    label('loc_63C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_64A4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 3, 0x13)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_644F',
    )

    SetScenaFlags(ScenaFlag(0x0002, 3, 0x13))

    ChrTalk(
        0x00FE,
        (
            '啊啊，\n',
            '艾德尔那家伙又想去买东西啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉……\n',
            '她不是刚刚才来过这家店吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊～\n',
            '定期船的航运赶快恢复吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_64A1')

    def _loc_644F(): pass

    label('loc_644F')

    ChrTalk(
        0x00FE,
        (
            '啊啊，\n',
            '艾德尔那家伙又想去买东西啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉……\n',
            '她不是刚刚才来过这家店吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_64A1(): pass

    label('loc_64A1')

    Jump('loc_66A9')

    def _loc_64A4(): pass

    label('loc_64A4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_65AB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 3, 0x13)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6549',
    )

    SetScenaFlags(ScenaFlag(0x0002, 3, 0x13))

    ChrTalk(
        0x00FE,
        (
            '妻子买东西的气势\n',
            '真是强悍啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '自从来了这里之后，\n',
            '好像就在一直不停地购物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我觉得，\n',
            '就算再有钱也应该\n',
            '保持勤俭节约的习惯才行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_65A8')

    def _loc_6549(): pass

    label('loc_6549')

    ChrTalk(
        0x00FE,
        (
            '妻子买东西的气势\n',
            '真是强悍啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我觉得，\n',
            '就算再有钱也应该\n',
            '保持勤俭节约的习惯才行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_65A8(): pass

    label('loc_65A8')

    Jump('loc_66A9')

    def _loc_65AB(): pass

    label('loc_65AB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_66A9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 3, 0x13)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_664B',
    )

    SetScenaFlags(ScenaFlag(0x0002, 3, 0x13))

    ChrTalk(
        0x00FE,
        (
            '啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要步行到卢安去\n',
            '就必须要翻越山峰……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过妻子\n',
            '肯定会反对这样做的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是这样下去\n',
            '留在这里就会花掉更多的住宿费。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_66A9')

    def _loc_664B(): pass

    label('loc_664B')

    ChrTalk(
        0x00FE,
        (
            '嗯～又不能步行去卢安，\n',
            '到底该怎么办呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是这样下去\n',
            '留在这里就会花掉更多的住宿费。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_66A9(): pass

    label('loc_66A9')

    TalkEnd(0x0017)

    Return()

# id: 0x0021 offset: 0x66AD
@scena.Code('func_21_66AD')
def func_21_66AD():
    TalkBegin(0x0019)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_681E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 4, 0x14)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6796',
    )

    SetScenaFlags(ScenaFlag(0x0002, 4, 0x14))

    ChrTalk(
        0x00FE,
        (
            '在被袭击的工房\n',
            '恢复营业之前，\n',
            '我都会一直呆在柏斯的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '利贝尔的导力器\n',
            '十分吸引我啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是自从我来到利贝尔之后，\n',
            '就光是在等啊等……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，商人必须学会忍耐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在还是静下心来\n',
            '慢慢等着吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_681B')

    def _loc_6796(): pass

    label('loc_6796')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 5, 0x15)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_67E5',
    )

    SetScenaFlags(ScenaFlag(0x0002, 5, 0x15))

    ChrTalk(
        0x00FE,
        (
            '不过，商人必须学会忍耐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在还是静下心来\n',
            '慢慢等着吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_681B')

    def _loc_67E5(): pass

    label('loc_67E5')

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '那个工房的店主……\n',
            '好像有点坐立不安呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_681B(): pass

    label('loc_681B')

    Jump('loc_6922')

    def _loc_681E(): pass

    label('loc_681E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_6922',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 4, 0x14)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_68B9',
    )

    SetScenaFlags(ScenaFlag(0x0002, 4, 0x14))

    ChrTalk(
        0x00FE,
        (
            '嗯，\n',
            '这就是柏斯超市吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还真是出人意料啊……\n',
            '作为一个小国家的超市，\n',
            '居然这么热闹啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '趁谈判的空档，\n',
            '就顺便参观一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6922')

    def _loc_68B9(): pass

    label('loc_68B9')

    ChrTalk(
        0x00FE,
        (
            '还真是出人意料啊……\n',
            '作为一个小国家的超市，\n',
            '居然这么热闹啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '趁谈判的空档，\n',
            '就顺便参观一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6922(): pass

    label('loc_6922')

    TalkEnd(0x0019)

    Return()

# id: 0x0022 offset: 0x6926
@scena.Code('func_22_6926')
def func_22_6926():
    TalkBegin(0x001A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 6, 0x16)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_69C8',
    )

    SetScenaFlags(ScenaFlag(0x0002, 6, 0x16))

    ChrTalk(
        0x00FE,
        (
            '没想到特里诺先生\n',
            '连同飞艇一起行踪不明了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '米拉诺小姐代替父亲\n',
            '去处理了谈判工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真厉害呀……\n',
            '但是，我很担心这样会不会累垮小姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6A28')

    def _loc_69C8(): pass

    label('loc_69C8')

    ChrTalk(
        0x00FE,
        (
            '米拉诺小姐代替父亲\n',
            '去处理了谈判工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真厉害呀……\n',
            '但是，我很担心这样会不会累垮小姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6A28(): pass

    label('loc_6A28')

    TalkEnd(0x001A)

    Return()

# id: 0x0023 offset: 0x6A2C
@scena.Code('func_23_6A2C')
def func_23_6A2C():
    TalkBegin(0x001C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 7, 0x17)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6AD9',
    )

    SetScenaFlags(ScenaFlag(0x0002, 7, 0x17))

    ChrTalk(
        0x00FE,
        (
            '唉，\n',
            '本来想把父亲的工作委任给西蒙的，\n',
            '不过他还差得很远呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是被博尔德大叔\n',
            '占了上风就糟糕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，我必须得有一个助手。\n',
            '还是把他叫上吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6B28')

    def _loc_6AD9(): pass

    label('loc_6AD9')

    ChrTalk(
        0x00FE,
        (
            '……行商最重要就是信用第一。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算自己的业绩不好，\n',
            '也不能连累其他人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6B28(): pass

    label('loc_6B28')

    TalkEnd(0x001C)

    Return()

# id: 0x0024 offset: 0x6B2C
@scena.Code('func_24_6B2C')
def func_24_6B2C():
    TalkBegin(0x001D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 0, 0x18)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6BE4',
    )

    SetScenaFlags(ScenaFlag(0x0003, 0, 0x18))

    ChrTalk(
        0x00FE,
        (
            '#0370021451V#620F小姐就是那种自己越忙\n',
            '就越有干劲的类型。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370021452V#621F这可能是继承了前市长……\n',
            '她父亲血统的原因吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370021453V#620F可是，\n',
            '我却非常担心小姐的身体状况……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6C50')

    def _loc_6BE4(): pass

    label('loc_6BE4')

    ChrTalk(
        0x00FE,
        (
            '#0370021454V#620F小姐就是那种自己越忙\n',
            '就越有干劲的类型。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370021455V#620F可是，\n',
            '我却非常担心小姐的身体状况……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6C50(): pass

    label('loc_6C50')

    TalkEnd(0x001D)

    Return()

# id: 0x0025 offset: 0x6C54
@scena.Code('func_25_6C54')
def func_25_6C54():
    TalkBegin(0x001E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 1, 0x19)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6D09',
    )

    SetScenaFlags(ScenaFlag(0x0003, 1, 0x19))

    ChrTalk(
        0x00FE,
        (
            '别看我这样，\n',
            '我可是市长官邸的厨师呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然没办法做出\n',
            '像安特洛丝餐厅那样高级的料理，\n',
            '不过手艺也算可以啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '小姐最近十分繁忙，\n',
            '不知道营养能跟得上吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6D3A')

    def _loc_6D09(): pass

    label('loc_6D09')

    ChrTalk(
        0x00FE,
        (
            '小姐最近十分繁忙，\n',
            '不知道营养能跟得上吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6D3A(): pass

    label('loc_6D3A')

    TalkEnd(0x001E)

    Return()

# id: 0x0026 offset: 0x6D3E
@scena.Code('func_26_6D3E')
def func_26_6D3E():
    TalkBegin(0x001F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_6E8D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 2, 0x1A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6E3A',
    )

    SetScenaFlags(ScenaFlag(0x0003, 2, 0x1A))

    ChrTalk(
        0x0102,
        (
            '#0020020658V#010F啊，是朵洛希。\n',
            '在干什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x001F, 270, 100)
    SetChrDirection(0x001F, 180, 100)
    SetChrDirection(0x001F, 225, 100)

    ChrTalk(
        0x001F,
        (
            '#0280020659V#151F大家，要摆出最好的表情哦～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280020660V好～向这边微笑一下㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020661V#501F好像听不见我说话呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020662V#014F嗯，是啊……\n',
            '集中力还是那么厉害。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6E8A')

    def _loc_6E3A(): pass

    label('loc_6E3A')

    ChrTalk(
        0x001F,
        (
            '#0280020663V#150F那么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280020664V接下来照前辈的指示，\n',
            '去拍一些资料用的照片吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6E8A(): pass

    label('loc_6E8A')

    Jump('loc_7002')

    def _loc_6E8D(): pass

    label('loc_6E8D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_7002',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 2, 0x1A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6FA9',
    )

    SetScenaFlags(ScenaFlag(0x0003, 2, 0x1A))

    ChrTalk(
        0x0101,
        (
            '#0010020375V#004F哎……\n',
            '这不是朵洛希吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x001F, 90, 100)
    SetChrDirection(0x001F, 180, 100)
    SetChrDirection(0x001F, 270, 100)
    OP_62(0x001F, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(700)

    ChrTalk(
        0x001F,
        (
            '#0280020376V#151F哇～～\n',
            '真的是什么东西都有卖的啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280020377V东西太多了，\n',
            '我都看花眼了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020378V#014F好像沉浸在梦里一样，\n',
            '完全听不到别人说话呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020379V#007F啊哈哈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7002')

    def _loc_6FA9(): pass

    label('loc_6FA9')

    ChrTalk(
        0x001F,
        (
            '#0280020380V#151F哇～～\n',
            '真的是什么东西都有卖的啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280020381V东西太多了，\n',
            '我都看花眼了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7002(): pass

    label('loc_7002')

    TalkEnd(0x001F)

    Return()

# id: 0x0027 offset: 0x7006
@scena.Code('func_27_7006')
def func_27_7006():
    TalkBegin(0x0020)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_7121',
    )

    If(
        (
            (Expr.PushLong, 0x1B),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_70C5',
    )

    SetScenaFlags(ScenaFlag(0x0003, 3, 0x1B))

    ChrTalk(
        0x00FE,
        (
            '我被空贼抓起来这段时间，\n',
            '我的未婚妻卡特丽亚\n',
            '一直打理着小店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '她把小店经营得那么好，\n',
            '我真是没有脸面接手回来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我要做我自己，\n',
            '一切从零开始吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7121')

    def _loc_70C5(): pass

    label('loc_70C5')

    ChrTalk(
        0x00FE,
        (
            '她把小店经营得那么好，\n',
            '我真是没有脸面接手回来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我要做我自己，\n',
            '一切从零开始吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7121(): pass

    label('loc_7121')

    TalkEnd(0x0020)

    Return()

# id: 0x0028 offset: 0x7125
@scena.Code('func_28_7125')
def func_28_7125():
    TalkBegin(0x0021)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_719E',
    )

    ChrTalk(
        0x00FE,
        (
            '#0041050007V#030F那么，\n',
            '这就去传说中的安特洛丝餐厅看看吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0041050008V#035F一定得仔细品尝利贝尔料理的精髓。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_71EE')

    def _loc_719E(): pass

    label('loc_719E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_71EE',
    )

    ChrTalk(
        0x00FE,
        (
            '#0041050009V#030F哦～这里比想象中要繁华很多嘛。\n',
            '有很多地方值得参观一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_71EE(): pass

    label('loc_71EE')

    TalkEnd(0x0021)

    Return()

# id: 0x0029 offset: 0x71F2
@scena.Code('func_29_71F2')
def func_29_71F2():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    ChrSetRGBAMask(0x0101, 200, 255, 255, 255, 0)
    OP_67(0, 9500, -10000, 0)
    SetChrPos(0x0008, -84, -1000, -4656, 0)
    SetChrPos(0x0009, 1100, -1000, -3970, 270)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x001B, 0xFF)
    SetChrDirection(0x001B, 135, 0)
    ClearChrFlags(0x001B, 0x0080)
    SetChrFlags(0x0016, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000066, 'loc_726C'),
        (0x00000067, 'loc_72B3'),
        (0x00000065, 'loc_72FA'),
        (0x00000064, 'loc_7352'),
        (-1, 'loc_73AA'),
    )

    def _loc_726C(): pass

    label('loc_726C')

    SetChrPos(0x0134, -4819, 0, 15920, 180)
    SetChrPos(0x0101, -3723, 0, 16050, 180)
    SetChrPos(0x0102, -3383, 0, 17070, 180)
    SetChrPos(0x0103, -5216, 0, 17120, 180)

    Jump('loc_73AA')

    def _loc_72B3(): pass

    label('loc_72B3')

    SetChrPos(0x0134, 11560, 0, -630, 270)
    SetChrPos(0x0101, 11200, 0, 680, 270)
    SetChrPos(0x0102, 11974, 0, 1065, 270)
    SetChrPos(0x0103, 12448, 0, 181, 270)

    Jump('loc_73AA')

    def _loc_72FA(): pass

    label('loc_72FA')

    CameraMove(-17200, 0, 1000, 0)
    SetChrPos(0x0134, -19570, 0, 1459, 90)
    SetChrPos(0x0101, -19730, 0, 487, 90)
    SetChrPos(0x0102, -20300, 0, 1991, 90)
    SetChrPos(0x0103, -20600, 0, -237, 90)

    Jump('loc_73AA')

    def _loc_7352(): pass

    label('loc_7352')

    CameraMove(-3530, 0, -11850, 0)
    SetChrPos(0x0134, -2950, 0, -15160, 0)
    SetChrPos(0x0101, -4030, 0, -15400, 0)
    SetChrPos(0x0102, -4400, 0, -16490, 0)
    SetChrPos(0x0103, -3060, 0, -16480, 0)

    Jump('loc_73AA')

    def _loc_73AA(): pass

    label('loc_73AA')

    FadeIn(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010020546V#000F哇～地方好大啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020547V市长会在哪里呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0134,
        (
            '#0370020548V#620F那么引人注目的人物，\n',
            '应该很快就能找到的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0134, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0134,
        (
            '#0370020549V#623F……啊，果然如我所想。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_69(0x001B, 2000)

    NpcTalk(
        0x001B,
        '年轻女性',
        (
            '#0360020550V#612F我说你们，还知不知道什么叫做廉耻？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360020551V在这么紧张的时候，\n',
            '竟然囤积居奇、哄抬食品价格……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360020552V柏斯商人的名誉都让你们给败坏了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1150020553V可、可是，大小姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1160020554V我们只是为了提高柏斯超市的销售额，\n',
            '所以才……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x001B,
        '年轻女性',
        (
            '#0360020555V#614F给我闭嘴！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360020556V其它的商品也就不说了，\n',
            '连生活必需品都用来牟取暴利，\n',
            '会给我们的市场带来很坏的影响！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360020557V赶快给我恢复原来的价格！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1150020558V好、好的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1160020559V我明白了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x001B,
        '年轻女性',
        (
            '#0360020560V#615F……要知道，\n',
            '我从来没怀疑过\n',
            '你们对柏斯超市付出的热情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360020561V但是，我想让你们明白。\n',
            '所谓的买卖就是一种建立\n',
            '人与人之间信赖关系的过程。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360020562V#610F不要气馁，\n',
            '我相信你们一定能成为杰出的柏斯商人！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1150020563V大、大小姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1160020564V明白，我们一定努力！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0009, 0x01, 0x00, 0x002A)
    Sleep(300)

    CreateThread(0x0008, 0x01, 0x00, 0x002A)
    SetChrDirection(0x001B, 90, 300)
    Sleep(3000)

    NpcTalk(
        0x001B,
        '年轻女性',
        (
            '#0360020565V#610F呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0134,
        (
            '#0370020566V#620F小姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x001B, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000066, 'loc_77EE'),
        (0x00000067, 'loc_77EE'),
        (0x00000065, 'loc_78C2'),
        (0x00000064, 'loc_78C2'),
        (-1, 'loc_7996'),
    )

    def _loc_77EE(): pass

    label('loc_77EE')

    SetChrPos(0x0134, 4913, -250, 1250, 0)
    SetChrPos(0x0101, 4913, -250, 1250, 0)
    SetChrPos(0x0102, 4913, -250, 1250, 0)
    SetChrPos(0x0103, 4913, -250, 1250, 0)
    SetChrDirection(0x001B, 45, 400)

    @scena.Lambda('lambda_783F')
    def lambda_783F():
        CameraMove(920, -1000, -2130, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_783F)

    @scena.Lambda('lambda_7857')
    def lambda_7857():
        OP_92(0x00FE, 0x001B, 2000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0134, 0x0001, lambda_7857)

    Sleep(400)

    @scena.Lambda('lambda_7871')
    def lambda_7871():
        ChrWalkTo(0x00FE, 2180, -1000, -2150, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_7871)

    Sleep(400)

    @scena.Lambda('lambda_7891')
    def lambda_7891():
        ChrWalkTo(0x00FE, 1640, -1000, -1320, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_7891)

    Sleep(400)

    ChrWalkTo(0x0103, 2900, -1000, -1000, 3000, 0x00)

    Jump('loc_7996')

    def _loc_78C2(): pass

    label('loc_78C2')

    SetChrPos(0x0134, -6440, 0, -10600, 0)
    SetChrPos(0x0101, -6440, 0, -10600, 0)
    SetChrPos(0x0102, -6440, 0, -10600, 0)
    SetChrPos(0x0103, -6440, 0, -10600, 0)
    SetChrDirection(0x001B, 225, 400)

    @scena.Lambda('lambda_7913')
    def lambda_7913():
        CameraMove(-1270, -1000, -4770, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_7913)

    @scena.Lambda('lambda_792B')
    def lambda_792B():
        OP_92(0x00FE, 0x001B, 2000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0134, 0x0001, lambda_792B)

    Sleep(400)

    @scena.Lambda('lambda_7945')
    def lambda_7945():
        ChrWalkTo(0x00FE, -3010, -1000, -5580, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_7945)

    Sleep(400)

    @scena.Lambda('lambda_7965')
    def lambda_7965():
        ChrWalkTo(0x00FE, -2240, -1000, -6350, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_7965)

    Sleep(400)

    ChrWalkTo(0x0103, -3100, -1000, -6690, 3000, 0x00)

    Jump('loc_7996')

    def _loc_7996(): pass

    label('loc_7996')

    WaitForThreadExit(0x0134, 0x0001)

    NpcTalk(
        0x001B,
        '年轻女性',
        (
            '#0360020567V#610F莉拉……你来了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360020568V#617F又让你看到我丢脸的样子了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0134,
        (
            '#0370020569V#621F不……\n',
            '还是一如既往地表现出色啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370020570V不说这个了，小姐。\n',
            '这边几位客人有事想和您商谈。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370020571V请您赶快回官邸吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x001B,
        '年轻女性',
        (
            '#0360020572V#610F啊，那个徽章……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360020573V#610F难道你们就是\n',
            '游击士协会派来的人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020574V#000F嗯，正是。可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020575V#010F难道您就是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x001B,
        '年轻女性',
        (
            '#0360020576V#611F呵呵，请允许我先自我介绍一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360020577V我的名字叫梅贝尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360020578V是这座超市的拥有者，\n',
            '也是担任柏斯地区管理职务的市长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0035, 0x01, 0x0020)
    OP_28(0x0035, 0x01, 0x0040)
    OP_28(0x0035, 0x01, 0x0080)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T1131._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x002A offset: 0x7BC7
@scena.Code('func_2A_7BC7')
def func_2A_7BC7():
    SetChrDirection(0x00FE, 45, 400)
    ChrWalkTo(0x00FE, 1995, -1000, -1980, 3000, 0x00)
    ChrWalkTo(0x00FE, 5047, 0, 140, 3000, 0x00)
    ChrWalkTo(0x00FE, 9138, 0, -3300, 3000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

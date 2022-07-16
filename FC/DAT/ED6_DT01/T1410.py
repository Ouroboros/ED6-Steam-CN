import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T1410_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1410   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '诺朗'),
    TXT(0x02, '艾蕾米亚'),
    TXT(0x03, '马尔科'),
    TXT(0x04, '金发青年'),
    TXT(0x05, '卫兵'),
    TXT(0x06, '王国军士兵'),
    TXT(0x07, '王国军士兵'),
    TXT(0x08, '摩尔根将军'),
    TXT(0x09, '梅贝尔市长'),
    TXT(0x0A, '斯丁克'),
    TXT(0x0B, '王国军士兵'),
    TXT(0x0C, '王国军士兵'),
    TXT(0x0D, '王国军军官'),
    TXT(0x0E, '尼冈德'),
    TXT(0x0F, '塔罗牌'),
    TXT(0x10, '塔罗牌'),
    TXT(0x11, '咖啡'),
    TXT(0x12, '咖啡'),
    TXT(0x13, '咖啡'),
    TXT(0x14, '塔罗牌'),
    TXT(0x15, '王国军士兵'),
    TXT(0x16, '王国军宪兵'),
    TXT(0x17, '王国军宪兵'),
    TXT(0x18, '目标用摄像机'),
    TXT(0x19, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1410.x'
    header.mapIndex       = 1
    header.bgm            = 16
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x939B
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
        ('ED6_DT07/CH01270._CH', 'ED6_DT07/CH01270P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01100._CH', 'ED6_DT07/CH01100P._CP'),
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT07/CH02080._CH', 'ED6_DT07/CH02080P._CP'),
        ('ED6_DT07/CH02360._CH', 'ED6_DT07/CH02360P._CP'),
        ('ED6_DT07/CH01620._CH', 'ED6_DT07/CH01620P._CP'),
        ('ED6_DT07/CH01310._CH', 'ED6_DT07/CH01310P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH00033._CH', 'ED6_DT07/CH00033P._CP'),
        ('ED6_DT06/CH20020._CH', 'ED6_DT06/CH20020P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH01650._CH', 'ED6_DT07/CH01650P._CP'),
        ('ED6_DT07/CH00003._CH', 'ED6_DT07/CH00003P._CP'),
        ('ED6_DT07/CH00013._CH', 'ED6_DT07/CH00013P._CP'),
        ('ED6_DT07/CH00023._CH', 'ED6_DT07/CH00023P._CP'),
        ('ED6_DT06/CH20045._CH', 'ED6_DT06/CH20045P._CP'),
        ('ED6_DT07/CH02083._CH', 'ED6_DT07/CH02083P._CP'),
    ]

# id: 0x10002 offset: 0x14A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 18100,
            z                   = 0,
            y                   = 16400,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 15350,
            z                   = 0,
            y                   = 15480,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = 13100,
            z                   = -100,
            y                   = 17110,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x01D4,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = 18850,
            z                   = 200,
            y                   = 14150,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 131075,
            chipIndex           = 3,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = 19944,
            z                   = 0,
            y                   = 8440,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 203044,
            z                   = 0,
            y                   = 9046,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 203044,
            z                   = 0,
            y                   = 9046,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 209550,
            z                   = 200,
            y                   = 11820,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0154,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            x                   = -60835,
            z                   = 0,
            y                   = 38681,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 18300,
            z                   = 0,
            y                   = 14300,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = 201700,
            z                   = 0,
            y                   = 109600,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = 104300,
            z                   = 0,
            y                   = 107600,
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
            x                   = 204600,
            z                   = 0,
            y                   = 15300,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            x                   = 110330,
            z                   = 0,
            y                   = -74950,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            x                   = 18500,
            z                   = 750,
            y                   = 15400,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 524299,
            chipIndex           = 11,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 19100,
            z                   = 700,
            y                   = 15300,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 327692,
            chipIndex           = 12,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 14950,
            z                   = 700,
            y                   = 12390,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1572875,
            chipIndex           = 11,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 15000,
            z                   = 700,
            y                   = 11770,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1572875,
            chipIndex           = 11,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 13190,
            z                   = 700,
            y                   = 12340,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1572875,
            chipIndex           = 11,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 13240,
            z                   = 700,
            y                   = 11670,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1572875,
            chipIndex           = 11,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 103480,
            z                   = 0,
            y                   = -74820,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 110330,
            z                   = 0,
            y                   = -77770,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            x                   = 106850,
            z                   = 0,
            y                   = -77680,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
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
    )

# id: 0x10003 offset: 0x44A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x44A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x44A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 118930,
            triggerZ            = 0,
            triggerY            = 14070,
            triggerRange        = 800,
            actorX              = 118930,
            actorZ              = 800,
            actorY              = 14070,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0014,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 123890,
            triggerZ            = 0,
            triggerY            = 11990,
            triggerRange        = 800,
            actorX              = 123890,
            actorZ              = 800,
            actorY              = 11990,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0020,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 17690,
            triggerZ            = 0,
            triggerY            = 14350,
            triggerRange        = 800,
            actorX              = 18100,
            actorZ              = 1500,
            actorY              = 16400,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x4B6
@scena.Code('PreInit')
def PreInit():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000066, 'loc_4C2'),
        (-1, 'loc_4CF'),
    )

    def _loc_4C2(): pass

    label('loc_4C2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 6, 0x30E)),
            Expr.Return,
        ),
        'loc_4CC',
    )

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    def _loc_4CC(): pass

    label('loc_4CC')

    Jump('loc_4CF')

    def _loc_4CF(): pass

    label('loc_4CF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_503',
    )

    SetChrPos(0x0009, 16900, 0, 14300, 0)
    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x001C, 0x0080)
    ClearChrFlags(0x001D, 0x0080)
    ClearChrFlags(0x001E, 0x0080)
    ClearChrFlags(0x0015, 0x0080)

    Jump('loc_59C')

    def _loc_503(): pass

    label('loc_503')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_51E',
    )

    SetChrPos(0x0009, 16900, 0, 14300, 0)

    Jump('loc_59C')

    def _loc_51E(): pass

    label('loc_51E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_539',
    )

    SetChrPos(0x0009, 16900, 0, 14300, 0)

    Jump('loc_59C')

    def _loc_539(): pass

    label('loc_539')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_559',
    )

    SetChrPos(0x0009, 21600, 0, 11200, 180)
    ClearChrFlags(0x0011, 0x0080)

    Jump('loc_59C')

    def _loc_559(): pass

    label('loc_559')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 7, 0x317)),
            Expr.Return,
        ),
        'loc_563',
    )

    Jump('loc_59C')

    def _loc_563(): pass

    label('loc_563')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 3, 0x313)),
            Expr.Return,
        ),
        'loc_572',
    )

    ClearChrFlags(0x000A, 0x0080)

    Jump('loc_59C')

    def _loc_572(): pass

    label('loc_572')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_581',
    )

    ClearChrFlags(0x000A, 0x0080)

    Jump('loc_59C')

    def _loc_581(): pass

    label('loc_581')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 0, 0x310)),
            Expr.Return,
        ),
        'loc_590',
    )

    ClearChrFlags(0x000A, 0x0080)

    Jump('loc_59C')

    def _loc_590(): pass

    label('loc_590')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 4, 0x30C)),
            Expr.Return,
        ),
        'loc_59C',
    )

    ClearChrFlags(0x000A, 0x0080)

    def _loc_59C(): pass

    label('loc_59C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5DD',
    )

    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x0017, 0x0080)
    ClearChrFlags(0x0016, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 0, 0x310)),
            Expr.Return,
        ),
        'loc_5D8',
    )

    SetChrChipByIndex(0x000B, 10)
    SetChrPos(0x000B, 18850, 200, 14150, 225)
    SetChrSubChip(0x000B, 2)

    Jump('loc_5DD')

    def _loc_5D8(): pass

    label('loc_5D8')

    SetChrChipByIndex(0x000B, 10)

    def _loc_5DD(): pass

    label('loc_5DD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_5EB',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x001A)

    def _loc_5EB(): pass

    label('loc_5EB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_602',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, 0x001B)

    def _loc_602(): pass

    label('loc_602')

    Return()

# id: 0x0001 offset: 0x603
@scena.Code('Init')
def Init():
    OP_72(0x0003, 0x0010)
    OP_72(0x0004, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 2, 0x32A)),
            Expr.Return,
        ),
        'loc_617',
    )

    Jump('loc_623')

    def _loc_617(): pass

    label('loc_617')

    OP_6F(0x0002, 0)
    OP_72(0x0002, 0x0010)

    def _loc_623(): pass

    label('loc_623')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_62E',
    )

    OP_64(0x00, 0x0001)

    def _loc_62E(): pass

    label('loc_62E')

    Return()

# id: 0x0002 offset: 0x62F
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_644',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_644(): pass

    label('loc_644')

    Return()

# id: 0x0003 offset: 0x645
@scena.Code('func_03_645')
def func_03_645():
    ClearScenaFlags(ScenaFlag(0x0001, 2, 0xA))
    def _loc_648(): pass

    label('loc_648')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_661',
    )

    OP_99(0x00FE, 0x00, 0x07, 2000)

    Jump('loc_648')

    def _loc_661(): pass

    label('loc_661')

    Return()

# id: 0x0004 offset: 0x662
@scena.Code('func_04_662')
def func_04_662():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_6D6',
    )

    ChrWalkTo(0x00FE, 19170, 0, 12910, 1500, 0x00)
    ChrWalkTo(0x00FE, 22480, 0, 11400, 1500, 0x00)
    SetChrDirection(0x00FE, 180, 500)
    Sleep(1000)

    ChrWalkTo(0x00FE, 22480, 0, 11400, 1500, 0x00)
    ChrWalkTo(0x00FE, 16990, 0, 14340, 1500, 0x00)
    SetChrDirection(0x00FE, 0, 500)
    Sleep(1000)

    Jump('func_04_662')

    def _loc_6D6(): pass

    label('loc_6D6')

    Return()

# id: 0x0005 offset: 0x6D7
@scena.Code('func_05_6D7')
def func_05_6D7():
    Call(0, 0x0006)

    Return()

# id: 0x0006 offset: 0x6DC
@scena.Code('func_06_6DC')
def func_06_6DC():
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
            TXT(0x02, '休息\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_748',
    )

    FadeIn(300, 0)
    OP_0D()
    OP_A9(0x18)
    OP_56(0x00)
    TalkEnd(0x0008)

    Return()

    def _loc_748(): pass

    label('loc_748')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_75E',
    )

    OP_0D()
    OP_A9(0x17)
    OP_56(0x00)
    TalkEnd(0x0008)

    Return()

    def _loc_75E(): pass

    label('loc_75E')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_778',
    )

    FadeIn(300, 0)
    TalkEnd(0x0008)

    Return()

    def _loc_778(): pass

    label('loc_778')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_7DA',
    )

    ChrTalk(
        0x0008,
        (
            '那些空贼\n',
            '一个不留地都被抓住了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '国境守备队的士兵们\n',
            '终于可以好好休息一阵子了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D7B')

    def _loc_7DA(): pass

    label('loc_7DA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_8D8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_884',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '军人同志们都累得不行了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '虽然找到了失踪的飞艇，\n',
            '不过他们好像还没有抓到\n',
            '那些作案的犯人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '摩尔根将军彻夜不眠地\n',
            '指挥手下执行搜索任务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8D5')

    def _loc_884(): pass

    label('loc_884')

    ChrTalk(
        0x0008,
        (
            '军人同志们都累得不行了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '摩尔根将军彻夜不眠地\n',
            '指挥手下执行搜索任务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8D5(): pass

    label('loc_8D5')

    Jump('loc_D7B')

    def _loc_8D8(): pass

    label('loc_8D8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_9B8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_955',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '刚把吃霸王餐的犯人\n',
            '关进监牢里面……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '这次是不是又抓到了\n',
            '袭击定期船的家伙们？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '啊，搞错了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9B5')

    def _loc_955(): pass

    label('loc_955')

    ChrTalk(
        0x0008,
        (
            '空贼团那些家伙\n',
            '很难被抓获啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '他们是可以在天空飞翔的家伙。\n',
            '要抓到他们也不是件容易事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9B5(): pass

    label('loc_9B5')

    Jump('loc_D7B')

    def _loc_9B8(): pass

    label('loc_9B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_ADD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A66',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '国境守备队好像十分忙碌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '虽然出动了很多士兵来搜索，\n',
            '可还是没发现定期船的踪影。\n',
            '我看他们以后怎么摆架子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不过话说回来，\n',
            '士兵们也很辛苦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ADA')

    def _loc_A66(): pass

    label('loc_A66')

    ChrTalk(
        0x0008,
        (
            '国境守备队好像十分忙碌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '虽然出动了很多士兵来搜索，\n',
            '不过还是没发现定期船的踪影。\n',
            '我看他们以后怎么摆架子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_ADA(): pass

    label('loc_ADA')

    Jump('loc_D7B')

    def _loc_ADD(): pass

    label('loc_ADD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_BB3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B5A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '哈～哈～哈～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '哈肯大门的名产，\n',
            '就是将军阁下的雷声降下呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '士兵们也是人，\n',
            '犯错是难免的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BB0')

    def _loc_B5A(): pass

    label('loc_B5A')

    ChrTalk(
        0x0008,
        (
            '哈肯大门的名产，\n',
            '就是将军阁下的雷声降下呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '士兵们也是人，\n',
            '犯错是难免的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BB0(): pass

    label('loc_BB0')

    Jump('loc_D7B')

    def _loc_BB3(): pass

    label('loc_BB3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 0, 0x310)),
            Expr.Return,
        ),
        'loc_CB6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C52',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '王国军封锁了\n',
            '通往这里的钢壁之路。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '从帝国过来的人\n',
            '以及打算出国的人\n',
            '都只能滞留在这里啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '那边的金发小兄弟\n',
            '也是同样的情况吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CB3')

    def _loc_C52(): pass

    label('loc_C52')

    ChrTalk(
        0x0008,
        (
            '王国军封锁了\n',
            '通往这里的钢壁之路。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '从帝国过来的人\n',
            '以及打算出国的人\n',
            '都只能滞留在这里啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CB3(): pass

    label('loc_CB3')

    Jump('loc_D7B')

    def _loc_CB6(): pass

    label('loc_CB6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 4, 0x30C)),
            Expr.Return,
        ),
        'loc_D7B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D32',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '你好，欢迎来到关所酒场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '这里好歹也是个酒场，\n',
            '食物和饮料应有尽有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '虽然都是些粗茶淡饭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D7B')

    def _loc_D32(): pass

    label('loc_D32')

    ChrTalk(
        0x0008,
        (
            '这里好歹也是个酒场，\n',
            '食物和饮料应有尽有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '虽然都是些粗茶淡饭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D7B(): pass

    label('loc_D7B')

    TalkEnd(0x0008)

    Return()

# id: 0x0007 offset: 0xD7F
@scena.Code('func_07_D7F')
def func_07_D7F():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_DE1',
    )

    ChrTalk(
        0x00FE,
        (
            '前几天，\n',
            '军队的士兵抓到了一个古怪的男人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听说那个男人做了什么欺诈的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12F1')

    def _loc_DE1(): pass

    label('loc_DE1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_EF0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E8C',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '最近，即使一到睡觉的时间，\n',
            '军队的士兵还一直在进进出出的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '吵得我们也睡得不舒服……呼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '下次那些士兵来喝酒的话，\n',
            '要向他们发发牢骚才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EED')

    def _loc_E8C(): pass

    label('loc_E8C')

    ChrTalk(
        0x00FE,
        (
            '最近，即使一到睡觉的时间，\n',
            '军队的士兵还一直在进进出出的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '吵得我们也睡得不舒服……呼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EED(): pass

    label('loc_EED')

    Jump('loc_12F1')

    def _loc_EF0(): pass

    label('loc_EF0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_FBC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F90',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '传言中的精英上校\n',
            '来我们店里吃饭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他真是风度翩翩的绅士，\n',
            '和这里粗鲁的军人\n',
            '简直是天壤之别的对比啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不经意，我都迷上他了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FB9')

    def _loc_F90(): pass

    label('loc_F90')

    ChrTalk(
        0x00FE,
        (
            '这世上，\n',
            '还会有如此动人的男人在啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FB9(): pass

    label('loc_FB9')

    Jump('loc_12F1')

    def _loc_FBC(): pass

    label('loc_FBC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_1106',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_109D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '在此之前，我曾经\n',
            '从那些士兵听过上校的事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没想到那个超帅的精英上校\n',
            '会来关所这里视察。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呀，要是他向我打招呼的话，\n',
            '人家怎么应他才好呢㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我要穿一件漂亮的衣服\n',
            '来迎接上校的到来才行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1103')

    def _loc_109D(): pass

    label('loc_109D')

    ChrTalk(
        0x00FE,
        (
            '没想到那个超帅的精英上校\n',
            '会来关所这里视察。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呀，要是他向我打招呼的话，\n',
            '人家怎么应他才好呢㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1103(): pass

    label('loc_1103')

    Jump('loc_12F1')

    def _loc_1106(): pass

    label('loc_1106')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_1213',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_11A7',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '将军的怒吼声\n',
            '还是和以前一样震耳欲聋啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在这种小店\n',
            '也能听得这么清楚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一听到那个声音，\n',
            '新兵们一个一个都\n',
            '哭着跑到这里来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1210')

    def _loc_11A7(): pass

    label('loc_11A7')

    ChrTalk(
        0x00FE,
        (
            '将军的怒吼声\n',
            '还是和以前一样震耳欲聋啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一听到那个声音，\n',
            '新兵们一个一个都\n',
            '哭着跑到这里来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1210(): pass

    label('loc_1210')

    Jump('loc_12F1')

    def _loc_1213(): pass

    label('loc_1213')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 0, 0x310)),
            Expr.Return,
        ),
        'loc_128A',
    )

    ChrTalk(
        0x00FE,
        (
            '说起这里的客人，\n',
            '都是一些歇班的士兵\n',
            '和等待入境办理手续的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以说，\n',
            '大部分的客人都已经很脸熟啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12F1')

    def _loc_128A(): pass

    label('loc_128A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 4, 0x30C)),
            Expr.Return,
        ),
        'loc_12F1',
    )

    ChrTalk(
        0x00FE,
        (
            '那位金发的小兄弟，\n',
            '看上去样子还不错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过和他谈了两句之后，\n',
            '发现他真是个奇怪的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12F1(): pass

    label('loc_12F1')

    TalkEnd(0x0009)

    Return()

# id: 0x0008 offset: 0x12F5
@scena.Code('func_08_12F5')
def func_08_12F5():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_1358',
    )

    ChrTalk(
        0x00FE,
        (
            '呼……\n',
            '街道的封锁总算解除了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '入境许可证也办理好了，\n',
            '我终于可以到柏斯去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_152F')

    def _loc_1358(): pass

    label('loc_1358')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 0, 0x310)),
            Expr.Return,
        ),
        'loc_14EA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0072, 3, 0x393)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1489',
    )

    SetScenaFlags(ScenaFlag(0x0072, 3, 0x393))

    ChrTalk(
        0x00FE,
        (
            '由于定期船一直停航，\n',
            '我只能靠走路来到这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到底要让身为帝都商人的我\n',
            '等到什么时候才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呆在这里太清闲了，\n',
            '所以把带在身上的书给看完了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '带在身上觉得有点麻烦，\n',
            '不如把这本书送给你们算了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    AddItem(0x0214, 1)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '红耀石　第３卷',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    Jump('loc_14E7')

    def _loc_1489(): pass

    label('loc_1489')

    ChrTalk(
        0x00FE,
        (
            '到底要让身为帝都商人的我\n',
            '等到什么时候才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '小国所做的事情\n',
            '就是欠缺优雅的气派……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14E7(): pass

    label('loc_14E7')

    Jump('loc_152F')

    def _loc_14EA(): pass

    label('loc_14EA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 4, 0x30C)),
            Expr.Return,
        ),
        'loc_152F',
    )

    ChrTalk(
        0x00FE,
        (
            '我是埃雷波尼亚帝国的商人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在我正在去柏斯的途中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_152F(): pass

    label('loc_152F')

    TalkEnd(0x000A)

    Return()

# id: 0x0009 offset: 0x1533
@scena.Code('func_09_1533')
def func_09_1533():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 0, 0x310)),
            Expr.Return,
        ),
        'loc_1605',
    )

    ClearChrFlags(0x000B, 0x0010)
    ChrTurnDirection(0x000B, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0xC8),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_155F',
    )

    SetChrSubChip(0x000B, 1)

    Jump('loc_157A')

    def _loc_155F(): pass

    label('loc_155F')

    If(
        (
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0xFA),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1575',
    )

    SetChrSubChip(0x000B, 2)

    Jump('loc_157A')

    def _loc_1575(): pass

    label('loc_1575')

    SetChrSubChip(0x000B, 0)

    def _loc_157A(): pass

    label('loc_157A')

    SetChrDirection(0x000B, 225, 0)
    SetChrFlags(0x000B, 0x0010)

    ChrTalk(
        0x000B,
        (
            '#0040020794V#030F哎哟，\n',
            '难道说你们改变主意打算带我去了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020795V#009F怎么可能～你做梦吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0040020796V#034F小气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x000B, 2)

    Jump('loc_2384')

    def _loc_1605(): pass

    label('loc_1605')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 7, 0x30F)),
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 6, 0x30E)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 0, 0x310)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2084',
    )

    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x0062, 0, 0x310))
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0101, 17370, 0, 13720, 90)
    SetChrPos(0x0102, 17820, 0, 12390, 45)
    SetChrPos(0x0103, 19280, 0, 12690, 0)
    SetChrPos(0x000B, 18850, 200, 14150, 225)
    SetChrSubChip(0x000B, 0)
    OP_69(0x000B, 0)
    OP_67(0, 6740, -10000, 0)
    CameraSetDistance(1210, 0)
    OP_6C(45000, 0)
    OP_6E(660, 0)
    OP_0D()

    ChrTalk(
        0x000B,
        (
            '#0040020750V#030F呀，你们好啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040020751V你们看起来好像是利贝尔人，\n',
            '要到帝国旅行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020752V#000F不呢，\n',
            '我们是因为有事要办才到这里来的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020753V没打算去帝国。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020754V#010F你看起来\n',
            '好像是埃雷波尼亚人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020020755V是来利贝尔王国旅游的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0040020756V#035F呵呵，一半工作，一半游玩啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040020757V#035F你们是来办事的吗……\n',
            '那么本人可看出你们的真面目了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020758V#505F哎，真面目？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0040020759V#030F你们其实是游击士吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
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
            '#0010020760V#004F为、为什么……\n',
            '明明游击士徽章都摘下来了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020761V难道说，你是同行？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0040020762V#035F确实帝国也有游击士协会，\n',
            '可惜，本人并不是游击士。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040020763V#030F只是在游击士协会有熟人而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040020764V你们给我的感觉和他们很像，\n',
            '所以我就稍微猜测了一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020765V#015F真是敏锐的观察力呀……\n',
            '我想你不会是个普通人吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020020766V#012F真的只是来旅行的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0040020767V#035F呵呵，\n',
            '先不要用这幅表情瞪着我嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040020768V冰冷地闪烁着琥珀色光辉的眼眸……\n',
            '宛如极品白兰地的色泽。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040020769V#037F让人不禁想要\n',
            '紧紧拥抱一亲芳泽啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_62(0x0102, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_94(0x01, 0x0102, 0x00B4, 0x00000258, 0x00000BB8, 0x00)

    ChrTalk(
        0x0102,
        (
            '#0020020770V#018F什么……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020771V#023F真……敢说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020772V#005F慢、慢着！\n',
            '难道你是有那种嗜好的人！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0040020773V#031F嘻……\n',
            '本人只是迷恋美丽的东西罢了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040020774V玲珑有致的美女。\n',
            '沉静惊艳的少年。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040020775V天籁之音，洗涤心灵的风景。\n',
            '名匠之作，震撼魂魄的故事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040020776V再加之极品美酒与上等料理……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040020777V以上所说，\n',
            '皆是本人所好之物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020778V#509F只是单纯的没有节操罢了吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020779V#027F不可救药的享乐主义者呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0040020780V#034F哈～不管是哪个时代，\n',
            '天才果然都是孤独的啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040020781V本人像玻璃一样，\n',
            '脆弱易碎的纯洁心灵已经受到了伤害呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040020782V#030F黑发的少年……\n',
            '来抚慰一下我受伤的心灵好吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020783V#017F不好意思，我拒绝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4A(0x0008, 255)

    ChrTalk(
        0x0008,
        (
            '#1170020784V（尽说些奇怪的话……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x000C, 20020, 0, 8730, 0)
    PlaySE(6, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000C,
        (
            '#2420020785V#1P喂～你们几个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4A(0x000C, 255)
    ClearChrFlags(0x000C, 0x0080)
    ChrSetRGBAMask(0x000C, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_1DD8')
    def lambda_1DD8():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1DD8)

    ChrWalkTo(0x000C, 19920, 0, 9570, 2000, 0x00)
    OP_4B(0x0008, 255)
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0102, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0103, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1200)

    @scena.Lambda('lambda_1E3D')
    def lambda_1E3D():
        CameraMove(20620, 0, 12620, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1E3D)

    @scena.Lambda('lambda_1E55')
    def lambda_1E55():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1E55)

    @scena.Lambda('lambda_1E63')
    def lambda_1E63():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1E63)

    @scena.Lambda('lambda_1E71')
    def lambda_1E71():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_1E71)

    SetChrSubChip(0x000B, 1)
    ChrWalkTo(0x000C, 20500, 0, 11100, 3000, 0x00)
    SetChrDirection(0x000C, 270, 400)
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0103,
        (
            '#0030020786V#020F#5P啊，是刚才的那个士兵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2420020787V#2P就在刚才，\n',
            '将军已经回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2420020788V#2P我已经向将军禀报了你们的事，\n',
            '他可以马上接见你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020789V#501F#5P哎，是真的吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2420020790V#2P请赶快到营房来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x000C, 180, 400)
    ChrWalkTo(0x000C, 20010, 0, 10290, 3000, 0x00)

    @scena.Lambda('lambda_1F9D')
    def lambda_1F9D():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1F9D)

    ChrWalkTo(0x000C, 20010, 0, 8690, 2000, 0x00)
    WaitForThreadExit(0x000C, 0x0001)
    SetChrFlags(0x000C, 0x0080)
    CameraMove(18830, 0, 13990, 1200)
    ChrTurnDirection(0x0102, 0x0103, 400)

    ChrTalk(
        0x0102,
        (
            '#0020020791V#010F比预想中回来得要早啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0102, 400)

    ChrTalk(
        0x0103,
        (
            '#0030020792V#020F#2P是啊。\n',
            '终于要得到情报了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x000B, 0)
    Sleep(400)

    ChrTalk(
        0x000B,
        (
            '#0040020793V#035F呵呵……\n',
            '那我们马上去看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T1400._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_2384')

    def _loc_2084(): pass

    label('loc_2084')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 7, 0x30F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_22FA',
    )

    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x0061, 7, 0x30F))

    ChrTalk(
        0x000B,
        (
            '#0040020797V#035F呵呵，真令人惊讶……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040020798V#035F初次品尝正宗的利贝尔料理，\n',
            '想不到味道还真不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1170020799V哈哈，\n',
            '能听到你这么说我也很高兴啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1170020800V如果到了城市那边，\n',
            '你会找到更多富有利贝尔特色的饭店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1170020801V这也是旅行中的乐趣所在啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0040020802V#030F当然，本人就是如此打算的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040020803V#030F偏远地区的酒馆也能做出如此美味的料理，\n',
            '看来今后真是令人期待啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1170020804V嘿嘿，这里的确偏远，真过意不去啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1170020805V再喝点酒怎么样？\n',
            '虽然是便宜货，但是口感相当好哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0040020806V#035F呼，让我考虑一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020807V#000F（这个人，难道是……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020808V#010F（看上去好像是从帝国来的旅行者。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)

    Jump('loc_2384')

    def _loc_22FA(): pass

    label('loc_22FA')

    ChrTalk(
        0x000B,
        (
            '#0040020809V#030F嗯，这酒的确不错……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040020810V#030F没想到利贝尔的东西\n',
            '是如此的价廉物美。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040020811V#030F这也许是女王\n',
            '赐予民众的恩惠之一吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2384(): pass

    label('loc_2384')

    TalkEnd(0x000B)

    Return()

# id: 0x000A offset: 0x2388
@scena.Code('func_0A_2388')
def func_0A_2388():
    TalkBegin(0x0011)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 7, 0x35F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_261B',
    )

    SetScenaFlags(ScenaFlag(0x006B, 7, 0x35F))
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x0101,
        (
            '#006F（啊，这个人……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F（嗯，\n',
            '　好像和我们一样都是游击士呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#002F喂，打扰一下？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F你还是那样讨人厌呢，\n',
            '斯丁克。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0011, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x00FE, 0x0103, 400)

    ChrTalk(
        0x00FE,
        (
            '你是……\n',
            '以前的那个见习游击士啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F没错呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '托你的福，\n',
            '现在我已经是正游击士啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼……看起来的确成熟了不少。\n',
            '在柏斯支部有工作吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F嗯，现在就正在工作呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近发生了很多事情，\n',
            '游击士的人手远远不够呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……那就靠你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x00FE, 0, 0)

    ChrTalk(
        0x0101,
        (
            '#002F（是雪拉姐的熟人吧。\n',
            '　感觉有点恐怖的人呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F（但是那走路的动作……\n',
            '　看起来应该很厉害吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27FB')

    def _loc_261B(): pass

    label('loc_261B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_279D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x0103,
        (
            '#020F这不是斯丁克吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0103, 0)

    ChrTalk(
        0x00FE,
        (
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是雪拉扎德啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F柏斯支部的同行也都很忙吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我刚把一位\n',
            '帝国的旅行者送走……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '然后打算不回支部\n',
            '直接去办下一件事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F真的是很忙呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '怎么样，等我们都忙完了，\n',
            '一起去喝一杯吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '算了，我不会喝酒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F啊，是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x00FE, 0, 0)

    Jump('loc_27FB')

    def _loc_279D(): pass

    label('loc_279D')

    ChrTurnDirection(0x00FE, 0x0000, 0)

    ChrTalk(
        0x00FE,
        (
            '我刚把一位\n',
            '帝国的旅行者送走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '然后打算不回支部\n',
            '直接去办下一件事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x00FE, 0, 0)

    def _loc_27FB(): pass

    label('loc_27FB')

    TalkEnd(0x0011)

    Return()

# id: 0x000B offset: 0x27FF
@scena.Code('func_0B_27FF')
def func_0B_27FF():
    TalkBegin(0x0013)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_28E9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2894',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '空贼被抓获了，\n',
            '终于可以恢复正常的工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，这里毕竟是\n',
            '和埃雷波尼亚接壤的国境啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们可不能\n',
            '掉以轻心呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28E6')

    def _loc_2894(): pass

    label('loc_2894')

    ChrTalk(
        0x00FE,
        (
            '虽然恢复正常工作了，\n',
            '这里就是和埃雷波尼亚接壤的国境，\n',
            '我们可不能掉以轻心呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_28E6(): pass

    label('loc_28E6')

    Jump('loc_29EA')

    def _loc_28E9(): pass

    label('loc_28E9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_2938',
    )

    ChrTalk(
        0x00FE,
        (
            '明早要乘坐警备飞艇\n',
            '在山里面进行搜索。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天得早点睡才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29EA')

    def _loc_2938(): pass

    label('loc_2938')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_2991',
    )

    ChrTalk(
        0x00FE,
        (
            '啊啊，今天很累啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '比起吃饭和洗澡，\n',
            '现在最想做的还是好好睡一觉啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29EA')

    def _loc_2991(): pass

    label('loc_2991')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 0, 0x310)),
            Expr.Return,
        ),
        'loc_29EA',
    )

    ChrTalk(
        0x00FE,
        (
            '其实今天\n',
            '本来不是我当班的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为上面下达了\n',
            '让我们在要塞内待命的命令。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_29EA(): pass

    label('loc_29EA')

    TalkEnd(0x0013)

    Return()

# id: 0x000C offset: 0x29EE
@scena.Code('func_0C_29EE')
def func_0C_29EE():
    TalkBegin(0x0012)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_2A8D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2A74',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '即使那些空贼被抓住了，\n',
            '也并不代表我能得到休假。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我现在处于\n',
            '睡眠不足的状态啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔……想睡觉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A8A')

    def _loc_2A74(): pass

    label('loc_2A74')

    ChrTalk(
        0x00FE,
        (
            '唔……想睡觉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A8A(): pass

    label('loc_2A8A')

    Jump('loc_2B7A')

    def _loc_2A8D(): pass

    label('loc_2A8D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_2AE5',
    )

    ChrTalk(
        0x00FE,
        (
            '明天歇班的士兵\n',
            '也会被召集起来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可能会进行一场\n',
            '大规模的搜索行动啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B7A')

    def _loc_2AE5(): pass

    label('loc_2AE5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_2B2C',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯……睡觉是最舒服的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '趁现在去食堂\n',
            '弄点饭吃吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B7A')

    def _loc_2B2C(): pass

    label('loc_2B2C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 0, 0x310)),
            Expr.Return,
        ),
        'loc_2B7A',
    )

    ChrTalk(
        0x00FE,
        (
            '呼啊啊～～～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '昨天参加飞艇的搜查，\n',
            '很晚才回来，现在好困。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B7A(): pass

    label('loc_2B7A')

    TalkEnd(0x0012)

    Return()

# id: 0x000D offset: 0x2B7E
@scena.Code('func_0D_2B7E')
def func_0D_2B7E():
    TalkBegin(0x000F)
    ClearChrFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x5A),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2BA3',
    )

    SetChrSubChip(0x00FE, 2)

    Jump('loc_2BD4')

    def _loc_2BA3(): pass

    label('loc_2BA3')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2BB9',
    )

    SetChrSubChip(0x00FE, 1)

    Jump('loc_2BD4')

    def _loc_2BB9(): pass

    label('loc_2BB9')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2BCF',
    )

    SetChrSubChip(0x00FE, 0)

    Jump('loc_2BD4')

    def _loc_2BCF(): pass

    label('loc_2BCF')

    SetChrSubChip(0x00FE, 2)

    def _loc_2BD4(): pass

    label('loc_2BD4')

    SetChrDirection(0x00FE, 270, 0)
    SetChrFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_2CB9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2C81',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x000F,
        (
            '#0600021016V#160F唔，你们两个是卡西乌斯的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600021017V来干什么啊？\n',
            '这里已经没你们的事了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600021018V我现在有很多工作要处理，\n',
            '没空和你们瞎闹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2CB6')

    def _loc_2C81(): pass

    label('loc_2C81')

    ChrTalk(
        0x000F,
        (
            '#0600021019V#160F来干什么啊？\n',
            '这里已经没你们的事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2CB6(): pass

    label('loc_2CB6')

    Jump('loc_3156')

    def _loc_2CB9(): pass

    label('loc_2CB9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_2F69',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_2D15',
    )

    ChrTalk(
        0x000F,
        (
            '#0600021020V#163F这次连情报部的家伙也来了，\n',
            '我们非得要靠他们协助才行吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F66')

    def _loc_2D15(): pass

    label('loc_2D15')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006C, 1, 0x361)),
            Expr.Return,
        ),
        'loc_2E0B',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x000F,
        (
            '#0600021021V#163F唔～\n',
            '如果继续动员守备队的士兵的话，\n',
            '那岂不忽视了对帝国方面的监视。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600021022V明知我们的工作已经够忙的了，\n',
            '还要叫这些家伙过来耍派头，\n',
            '这叫什么上策啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600021023V这次连情报部的家伙也来了，\n',
            '我们非得要靠他们协助才行吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F66')

    def _loc_2E0B(): pass

    label('loc_2E0B')

    SetScenaFlags(ScenaFlag(0x006C, 1, 0x361))

    ChrTalk(
        0x000F,
        (
            '#0600021024V#160F怎么，是卡西乌斯的孩子吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600021025V别老在我面前走来走去的行不行……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600021026V我事先给你们一个忠告，\n',
            '这次的事件属于军队的管辖范围。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600021027V要是你们以后再有出格的行为，\n',
            '就别怪我不客气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021028V#002F（将军的脸色好像不太好呢。\n',
            '　看来工作累坏了吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021029V#012F（嗯，因为军队也在拼命地\n',
            '　到处搜索那些空贼的行踪。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2F66(): pass

    label('loc_2F66')

    Jump('loc_3156')

    def _loc_2F69(): pass

    label('loc_2F69')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_3156',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_30D9',
    )

    SetScenaFlags(ScenaFlag(0x006C, 1, 0x361))
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x000F,
        (
            '#0600021030V#160F怎么，是卡西乌斯的孩子吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600021031V别老在我面前走来走去的行不行……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600021032V我事先给你们一个忠告，\n',
            '这次的事件属于军队的管辖范围。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600021033V要是你们以后再有出格的行为，\n',
            '就别怪我不客气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021034V#002F（将军的脸色好像不太好呢。\n',
            '　看来工作累坏了吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021035V#012F（嗯，因为军队也在拼命地\n',
            '　到处搜索那些空贼的行踪。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3156')

    def _loc_30D9(): pass

    label('loc_30D9')

    ChrTalk(
        0x000F,
        (
            '#0600021036V#160F我事先给你们一个忠告，\n',
            '这次的事件属于军队的管辖范围。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600021037V要是你们以后再有出格的行为，\n',
            '就别怪我不客气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3156(): pass

    label('loc_3156')

    SetChrSubChip(0x00FE, 0)
    TalkEnd(0x000F)

    Return()

# id: 0x000E offset: 0x315F
@scena.Code('func_0E_315F')
def func_0E_315F():
    TalkBegin(0x0014)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_31C9',
    )

    ChrTalk(
        0x00FE,
        (
            '那些空贼已经被押送到\n',
            '蔡斯的雷斯顿要塞那里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不久之后，\n',
            '他们会受到军队的严厉审讯的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_31C9(): pass

    label('loc_31C9')

    TalkEnd(0x0014)

    Return()

# id: 0x000F offset: 0x31CD
@scena.Code('func_0F_31CD')
def func_0F_31CD():
    TalkBegin(0x0015)

    If(
        (
            (Expr.Eval, "OP_29(0x0014, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_3304',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_32AD',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '为、为什么我会\n',
            '鬼迷心窍做出这种事……\n',
            '只、只是一时的糊涂而已啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我、我以后再也不做坏事了。\n',
            '请原谅我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我、我很胆小的，\n',
            '而且身体很虚弱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果一直被关在监狱里，\n',
            '一定会生病的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3301')

    def _loc_32AD(): pass

    label('loc_32AD')

    ChrTalk(
        0x00FE,
        (
            '我、我很胆小的，\n',
            '而且身体很虚弱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我、我以后再也不做坏事了。\n',
            '请原谅我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3301(): pass

    label('loc_3301')

    Jump('loc_33C5')

    def _loc_3304(): pass

    label('loc_3304')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3382',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '所以啊，我说了好几遍啦，\n',
            '请拿出证据来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果还是怀疑我的话，\n',
            '就把证据拿出来再说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，哈哈哈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_33C5')

    def _loc_3382(): pass

    label('loc_3382')

    ChrTalk(
        0x00FE,
        (
            '如果还是怀疑我的话，\n',
            '就把证据拿出来再说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，哈哈哈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_33C5(): pass

    label('loc_33C5')

    TalkEnd(0x0015)

    Return()

# id: 0x0010 offset: 0x33C9
@scena.Code('func_10_33C9')
def func_10_33C9():
    TalkBegin(0x001C)

    If(
        (
            (Expr.Eval, "OP_29(0x0014, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_34B2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3461',
    )

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))

    ChrTalk(
        0x00FE,
        (
            '被关在监牢里的这个大叔\n',
            '看起来是个坏人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然以貌取人\n',
            '是不太礼貌的事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过像这样\n',
            '一目了然的情况也很多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_34AF')

    def _loc_3461(): pass

    label('loc_3461')

    ChrTalk(
        0x00FE,
        (
            '虽然以貌取人\n',
            '是不太礼貌的事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过像这样\n',
            '一目了然的情况也很多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_34AF(): pass

    label('loc_34AF')

    Jump('loc_36A1')

    def _loc_34B2(): pass

    label('loc_34B2')

    If(
        (
            (Expr.Eval, "OP_29(0x0014, 0x00, 0x40)"),
            Expr.Return,
        ),
        'loc_359C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_354B',
    )

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))

    ChrTalk(
        0x00FE,
        (
            '被关在监牢里的这个大叔\n',
            '看起来是个很坏的人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然以貌取人\n',
            '是不太礼貌的事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过像这样\n',
            '一目了然的情况也很多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3599')

    def _loc_354B(): pass

    label('loc_354B')

    ChrTalk(
        0x00FE,
        (
            '虽然以貌取人\n',
            '是不太礼貌的事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过像这样\n',
            '一目了然的情况也很多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3599(): pass

    label('loc_3599')

    Jump('loc_36A1')

    def _loc_359C(): pass

    label('loc_359C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3628',
    )

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))

    ChrTalk(
        0x00FE,
        (
            '被关在监牢里的这个大叔\n',
            '不管怎么看都是个坏蛋……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是只要没有找到证据，\n',
            '就不得不释放他了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是让人无法接受呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_36A1')

    def _loc_3628(): pass

    label('loc_3628')

    ChrTalk(
        0x00FE,
        (
            '只要没有找到被关在监牢里的\n',
            '这个大叔的犯罪证据，\n',
            '就不得不释放他了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '把这样的坏人释放出去，\n',
            '真是让人无法接受呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_36A1(): pass

    label('loc_36A1')

    TalkEnd(0x001C)

    Return()

# id: 0x0011 offset: 0x36A5
@scena.Code('func_11_36A5')
def func_11_36A5():
    TalkBegin(0x001D)

    If(
        (
            (Expr.Eval, "OP_29(0x0014, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_3713',
    )

    ChrTalk(
        0x00FE,
        (
            '那么，\n',
            '你怎么解释这本黑账簿？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '别着急，\n',
            '你可以想好了再说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '反正时间还非常充裕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_384D')

    def _loc_3713(): pass

    label('loc_3713')

    If(
        (
            (Expr.Eval, "OP_29(0x0014, 0x00, 0x40)"),
            Expr.Return,
        ),
        'loc_377E',
    )

    ChrTalk(
        0x00FE,
        (
            '那么，\n',
            '你怎么解释这本黑账簿？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '别着急，\n',
            '你可以想好了再说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '反正时间还非常充裕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_384D')

    def _loc_377E(): pass

    label('loc_377E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3806',
    )

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    ChrTalk(
        0x00FE,
        (
            '喂，你到底把那本帐簿上\n',
            '记载的钱弄到哪里去了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '早点交待清楚，对你是有好处的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '反正我们迟早\n',
            '也会找到证据的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_384D')

    def _loc_3806(): pass

    label('loc_3806')

    ChrTalk(
        0x00FE,
        (
            '早点交待清楚，对你是有好处的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '反正我们迟早\n',
            '也会找到证据的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_384D(): pass

    label('loc_384D')

    TalkEnd(0x001D)

    Return()

# id: 0x0012 offset: 0x3851
@scena.Code('func_12_3851')
def func_12_3851():
    If(
        (
            (Expr.Eval, "OP_29(0x0014, 0x00, 0x10)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0014, 0x01, 0x8000)"),
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x0338)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3870',
    )

    Call(0, 0x0013)

    Jump('loc_39FA')

    def _loc_3870(): pass

    label('loc_3870')

    TalkBegin(0x001E)

    If(
        (
            (Expr.Eval, "OP_29(0x0014, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_38C6',
    )

    ChrTalk(
        0x00FE,
        (
            '终于解决掉尼冈德这家伙的事情了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '很快就可以把他关押起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_39F7')

    def _loc_38C6(): pass

    label('loc_38C6')

    If(
        (
            (Expr.Eval, "OP_29(0x0014, 0x00, 0x40)"),
            Expr.Return,
        ),
        'loc_395C',
    )

    ChrTalk(
        0x00FE,
        (
            '在空贼团的据点里\n',
            '找到了尼冈德这家伙的黑账本。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '肯定是强盗来的时候\n',
            '把它一起抢走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '坏蛋帮了坏蛋的忙，\n',
            '还真是奇妙的偶然啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_39F7')

    def _loc_395C(): pass

    label('loc_395C')

    ChrTalk(
        0x00FE,
        (
            '我们怀疑这个男人\n',
            '侵占了工房的财产……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是在那家伙的店铺里面调查后，\n',
            '又没有发现任何有力的证据。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '拘留是有期限的，\n',
            '很快就要到释放他的时候了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_39F7(): pass

    label('loc_39F7')

    TalkEnd(0x001E)

    def _loc_39FA(): pass

    label('loc_39FA')

    Return()

# id: 0x0013 offset: 0x39FB
@scena.Code('func_13_39FB')
def func_13_39FB():
    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0101, 106320, 0, -76490, 180)
    SetChrPos(0x0102, 105450, 0, -77130, 135)
    ChrTurnDirection(0x0101, 0x001D, 0)
    ChrTurnDirection(0x0102, 0x001D, 0)
    CameraMove(109770, 0, -76050, 2000)
    OP_0D()
    OP_4A(0x0015, 0)
    OP_4A(0x001D, 0)

    ChrTalk(
        0x001D,
        (
            '#2520151357V喂，你到底把那本帐簿上\n',
            '记载的钱弄到哪里去了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001D,
        (
            '#2520151358V早点交待清楚，对你是有好处的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001D,
        (
            '#2520151359V反正我们迟早\n',
            '也会找到证据的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#1400151360V所以啊，我说了好几遍啦，\n',
            '请拿出证据来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#1400151361V如果还是怀疑我的话，\n',
            '就把证据拿出来再说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#1400151362V呵呵哈哈哈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x001D, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(800)

    OP_4B(0x0015, 0)
    OP_4B(0x001D, 0)
    CameraMove(106250, 0, -77490, 1500)
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(400)

    SetChrDirection(0x0101, 180, 400)
    SetChrDirection(0x0102, 135, 400)

    ChrTalk(
        0x0101,
        (
            '#0010151363V#000F请问，这里怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x001E, 0x0101, 400)
    OP_4A(0x001E, 0)

    ChrTalk(
        0x001E,
        (
            '#2530151364V嗯？是这样的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001E,
        (
            '#2530151365V我们怀疑这个男人\n',
            '侵占了工房的财产……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001E,
        (
            '#2530151366V但是在那家伙的店铺里面调查后，\n',
            '又没有发现任何有力的证据。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001E,
        (
            '#2530151367V拘留是有期限的，\n',
            '很快就要到释放他的时候了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010151368V#501F咦～要证据啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020151369V#013F…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020151370V……对了，艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010151371V#000F嗯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020151372V#010F说起来，我们不是在空贼的基地里\n',
            '发现了一个奇怪的东西吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010151373V#505F奇怪的东西？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010151374V#001F……啊，是那个。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010151375V是说在吸尘器里面藏着的笔记本吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x001E, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x001E,
        (
            '#2530151376V吸尘器里面的……笔记本？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001E,
        (
            '#2530151377V不好意思，\n',
            '你们说的东西，能让我看看吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3E60')
    def lambda_3E60():
        SetChrDirection(0x0101, 180, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_3E60)

    SetChrDirection(0x0102, 135, 400)

    ChrTalk(
        0x0101,
        (
            '#0010151378V#002F好的，说不定对你们有用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '黑色笔记本',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetChrDirection(0x001E, 45, 400)
    OP_62(0x001E, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)

    ChrTalk(
        0x001E,
        (
            '#2530151379V……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001E,
        (
            '#2530151379V……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001E,
        (
            '#2530151379V……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x001E)
    Sleep(800)

    OP_62(0x001E, 0x00000000, 2000, 0x22, 0x24, 0x000000FA, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x001E,
        (
            '#2530151382V…………就是它。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150156V#501F什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x001E, 0x0101, 400)

    ChrTalk(
        0x001E,
        (
            '#2530151384V就是它，没错了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001E,
        (
            '#2530151385V这就是那个家伙经营的工房的黑账簿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x001E, 0x0015, 400)

    ChrTalk(
        0x001E,
        (
            '#2530151386V喂，尼冈德！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x001F,
        0x01,
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.GetChrWork, 0x15, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001F,
        0x02,
        (
            (Expr.GetChrWork, 0x101, 0x2),
            (Expr.GetChrWork, 0x15, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001F,
        0x03,
        (
            (Expr.GetChrWork, 0x101, 0x3),
            (Expr.GetChrWork, 0x15, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_4060')
    def lambda_4060():
        OP_69(0x001F, 2000)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_4060)

    @scena.Lambda('lambda_406E')
    def lambda_406E():
        ChrTurnDirection(0x001D, 0x001E, 400)

        ExitThread()

    DispatchAsync(0x001D, 0x0001, lambda_406E)

    @scena.Lambda('lambda_407C')
    def lambda_407C():
        ChrTurnDirection(0x001C, 0x001E, 400)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_407C)

    @scena.Lambda('lambda_408A')
    def lambda_408A():
        ChrTurnDirection(0x0101, 0x0015, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_408A)

    @scena.Lambda('lambda_4098')
    def lambda_4098():
        ChrTurnDirection(0x0102, 0x0015, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_4098)

    OP_62(0x0015, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x0015, 0x001E, 400)
    OP_4A(0x0015, 0)
    OP_4A(0x001D, 0)
    OP_4A(0x001C, 0)
    WaitForThreadExit(0x001F, 0x0001)

    ChrTalk(
        0x001E,
        (
            '#2530151387V看清楚了。\n',
            '这个就是你犯罪的证据！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0015, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrJumpToRelative(0x0015, 0, 0, 0, 700, 6000)
    Sleep(400)

    ChrTalk(
        0x0015,
        (
            '#1400151388V这、这不可能！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#1400151389V它应该和吸尘器一起\n',
            '被强盗给抢走了的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4180')
    def lambda_4180():
        ChrTurnDirection(0x00FE, 0x001E, 400)
        Yield()

        Jump('lambda_4180')

    DispatchAsync2(0x0000, 0x0001, lambda_4180)

    @scena.Lambda('lambda_4191')
    def lambda_4191():
        ChrTurnDirection(0x00FE, 0x001E, 400)
        Yield()

        Jump('lambda_4191')

    DispatchAsync2(0x0001, 0x0001, lambda_4191)

    @scena.Lambda('lambda_41A2')
    def lambda_41A2():
        ChrTurnDirection(0x00FE, 0x001E, 400)
        Yield()

        Jump('lambda_41A2')

    DispatchAsync2(0x0015, 0x0001, lambda_41A2)

    OP_92(0x001E, 0x001D, 1000, 2000, 0x00)
    Sleep(2000)

    TerminateThread(0x0015, 0x01)
    SetChrDirection(0x001D, 0, 400)
    SetChrDirection(0x0015, 180, 400)

    @scena.Lambda('lambda_41D8')
    def lambda_41D8():
        CameraMove(106250, 0, -77490, 2000)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_41D8)

    ChrWalkTo(0x001E, 106850, 0, -77680, 2000, 0x00)
    ChrTurnDirection(0x001E, 0x0101, 400)
    TerminateThread(0x0000, 0x01)
    TerminateThread(0x0001, 0x01)

    @scena.Lambda('lambda_4213')
    def lambda_4213():
        SetChrDirection(0x0101, 180, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_4213)

    SetChrDirection(0x0102, 135, 400)
    WaitForThreadExit(0x001F, 0x0001)

    ChrTalk(
        0x001E,
        (
            '#2530151390V谢谢你们的帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001E,
        (
            '#2530151391V这种麻烦的事情，\n',
            '果然就要靠游击士呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001E,
        (
            '#2530151392V有了那个记事本，\n',
            '就肯定可以定那家伙的罪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001E,
        (
            '#2530151393V我一定会通过游击士协会，\n',
            '正式支付你们酬劳的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001E,
        (
            '#2530151394V再次感谢你们的协助。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【黑色笔记本】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    RemoveItem(0x0338, 1)
    OP_28(0x0014, 0x04, 0x02)
    OP_28(0x0014, 0x04, 0x04)
    OP_28(0x0014, 0x04, 0x10)
    OP_28(0x0014, 0x01, 0x0001)
    OP_28(0x0014, 0x01, 0x0002)
    OP_28(0x0014, 0x01, 0x0004)
    ClearScenaFlags(ScenaFlag(0x0001, 7, 0xF))
    ClearScenaFlags(ScenaFlag(0x0001, 0, 0x8))
    SetChrDirection(0x001E, 45, 0)
    SetChrDirection(0x001C, 270, 0)
    OP_4B(0x001E, 0)
    OP_4B(0x001D, 0)
    OP_4B(0x001C, 0)
    OP_4B(0x0015, 0)
    EventEnd(0x00)

    Return()

# id: 0x0014 offset: 0x43A0
@scena.Code('func_14_43A0')
def func_14_43A0():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5623',
    )

    EventBegin(0x00)

    ChrTalk(
        0x0102,
        (
            '#0020020830V#010F走廊尽头的左边……\n',
            '这一间就是将军的房间吧。',
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
            TXT(0x00, '【敲门试试】\n'),
            TXT(0x01, '【还是算了】\n'),
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
        (0x00000001, 'loc_4452'),
        (0x00000000, 'loc_4457'),
        (-1, 'loc_5623'),
    )

    def _loc_4452(): pass

    label('loc_4452')

    EventEnd(0x01)

    Jump('loc_5623')

    def _loc_4457(): pass

    label('loc_4457')

    Fade(1000)
    CameraMove(118940, 0, 12530, 0)
    SetChrPos(0x000F, 119060, 0, 14740, 0)
    SetChrPos(0x0101, 118650, 0, 13360, 0)
    SetChrPos(0x0102, 119650, 0, 12540, 315)
    SetChrPos(0x0103, 117980, 0, 11970, 0)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x0062, 2, 0x312))

    ChrTalk(
        0x0101,
        (
            '#0010020831V#002F先敲一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(113, 0x00, 0x64)
    Sleep(1000)

    NpcTalk(
        0x000F,
        '男性的声音',
        (
            '#0600020832V……是梅贝尔小姐的使者吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020833V#000F#4P啊，正是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000F,
        '男性的声音',
        (
            '#0600020834V嗯，进来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020835V#020F那么，打扰了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    CameraMove(206210, 0, 13220, 0)
    OP_4A(0x000F, 255)
    SetChrPos(0x000F, 209550, 200, 11820, 270)
    SetChrFlags(0x000F, 0x0004)
    OP_0D()
    Sleep(500)

    PlaySE(106, 0x00, 0x64)
    Sleep(500)

    @scena.Lambda('lambda_45BD')
    def lambda_45BD():
        CameraMove(209700, 0, 13260, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_45BD)

    SetChrFlags(0x0101, 0x0004)
    SetChrFlags(0x0102, 0x0004)
    SetChrFlags(0x0103, 0x0004)
    ClearChrFlags(0x0101, 0x0080)
    ClearChrFlags(0x0102, 0x0080)
    ClearChrFlags(0x0103, 0x0080)
    CreateThread(0x0101, 0x00, 0x00, 0x0015)
    CreateThread(0x0103, 0x00, 0x00, 0x0017)
    CreateThread(0x0102, 0x00, 0x00, 0x0016)
    WaitForThreadExit(0x0102, 0x0000)

    ChrTalk(
        0x000F,
        (
            '#0600020836V#160F#2P终于来了啊。\n',
            '我就是摩尔根。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600020837V艾莉茜雅女王任命的\n',
            '看守哈肯大门的负责人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020838V#020F#5P初次见面。\n',
            '我们是梅贝尔市长的使者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020839V#010F在您百忙之中前来打扰，非常抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0600020840V#163F#2P哪里，梅贝尔小姐尚年幼的时候\n',
            '我就认识她了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600020841V何况是以市长立场而传达的话，\n',
            '我就更是不能不听了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020842V#002F#6P嗯，那么，\n',
            '还是请您先读读这封信吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '梅贝尔市长的信',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    RemoveItem(0x032D, 1)

    ChrTalk(
        0x000F,
        (
            '#0600020843V#161F#2P………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600020844V#163F唔……\n',
            '果然是和那个事件有关。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600020845V这些事情本来不能向外人透漏的。\n',
            '但既然是那孩子的委托，就顺应她意思吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600020846V#160F我就把所掌握的情报告诉你们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020847V#001F#6P太好了，真走运☆',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0600020848V#161F#2P……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600020849V你为什么要这么兴奋？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010020850V#003F#6P（不妙……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020851V#015F梅贝尔市长她\n',
            '对这次的事件非常地担心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020020852V所以，我们也很希望能\n',
            '尽自己的全力来帮助市长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0600020853V#163F#2P原来如此，梅贝尔小姐\n',
            '有这么出色的协助者真是太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600020854V我马上向你们说明搜索情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020855V#022F#5P洗耳恭听。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0600020856V#160F#2P……定期船『林德号』\n',
            '是在柏斯国际空港起飞后，\n',
            '飞往洛连特方向的途中失踪的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600020857V现在，各方面的部队还在搜索中，\n',
            '但到目前为止还没有发现目标。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020858V#012F这么说来，被魔兽攻击或是发生事故的\n',
            '可能性就大大降低了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020020859V那么庞大的飞船，\n',
            '如果真的是坠机的话， \n',
            '在最初进行搜索时就一定能发现了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0600020860V#160F#2P正是如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600020861V实际上，柏斯和洛连特之间的航线\n',
            '是在视野比较开阔的平原上空。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600020862V坠落入瓦雷利亚湖，\n',
            '甚至海里的可能性应该也很小。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020863V#007F#6P啊～太好了。\n',
            '没有发生最糟糕的事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030020864V#022F#5P那样的话，由人为原因而导致\n',
            '定期船被劫持的可能性就很高了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020865V可以想到的原因，也只有抢夺货物，\n',
            '甚至是挟持人质来要求赎金……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020866V#012F也就是所谓的劫机事件吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020020867V#013F还有，从地理情况上考虑的话，\n',
            '是帝国军队所做的地下活动……\n',
            '这样的可能性也不能排除。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010020868V#505F#6P这、这么说的话，事情可就严重了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0600020869V#161F#2P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000F, 400)
    ChrTurnDirection(0x0103, 0x000F, 400)

    ChrTalk(
        0x0101,
        (
            '#0010020870V#004F#6P怎么了，将军？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0600020871V#163F#2P没什么，只是觉得以寻常百姓而言，\n',
            '你们的观点相当有见地。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600020872V我们军方也为了查明帝国军队\n',
            '是否有参与此事件的可能性，\n',
            '正在进行彻底的情报管制。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600020873V在国际问题上轻举妄动的话，\n',
            '很有可能会发展成大规模的战争。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020874V#003F#6P战争……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0600020875V#160F#2P但是，不幸中的万幸，\n',
            '今天早上这种可能性被排除了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600020876V某个组织已经\n',
            '向王家飞艇公社发表了犯罪声明，\n',
            '并且要求赎回乘客的赎金。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600020877V那个组织的名字叫『卡普亚一家』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010020878V#580F#6P『卡普亚一家』？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020879V那、那么，难道说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020880V#012F……看来这是毫无疑问的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0600020881V#160F#2P他们是一伙以兄妹三人为首的的空贼团，\n',
            '经常在柏斯地区流窜作案。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600020882V难道说，\n',
            '你们也听说过他们的事情？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020883V#009F#6P何止听说过，\n',
            '之前在洛连特还和他们交过手呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020884V那帮家伙，难道就是\n',
            '到目前为止这个大事件的始作俑者……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_517D')
    def lambda_517D():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_517D)

    ChrTalk(
        0x0102,
        (
            '#0020020885V#012F艾丝蒂尔……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010020886V#008F#6P啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0600020887V#161F#2P在洛连特交过手？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600020888V那些家伙在洛连特地区\n',
            '出没的事情我倒是听说过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600020889V…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020890V#007F#6P啊，完了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020891V#025F#5P哈啊～大笨蛋……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x000F, 400)
    Sleep(500)

    ChrTalk(
        0x000F,
        (
            '#0600020892V#163F#2P……原来如此啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600020893V作为普通市民能如此思维敏捷而且能说会道，\n',
            '我正觉得奇怪……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600020894V#160F不过还真是没想到，\n',
            '这样的小女孩儿竟也会是游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020895V#009F#6P什、什么呀，什么小女孩儿！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020896V#013F但是，我们受到梅贝尔市长委托\n',
            '这件事的确是事实……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000F, 0x00000000, 1700, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    CameraSetDistance(3070, 0)
    CameraSetDistance(3000, 80)

    @scena.Lambda('lambda_53F2')
    def lambda_53F2():
        ChrJumpToRelative(0x00FE, 0, 0, 0, 1000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_53F2)

    @scena.Lambda('lambda_5410')
    def lambda_5410():
        ChrJumpToRelative(0x00FE, 0, 0, 0, 1000, 8000)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_5410)

    @scena.Lambda('lambda_542E')
    def lambda_542E():
        ChrJumpToRelative(0x00FE, 0, 0, 0, 1000, 8000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_542E)

    ChrTalk(
        0x000F,
        (
            '#0600020897V#162F#3S#2P住口，难道要我姑息你们吗！？#2S',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x000F, 5)
    SetChrPos(0x000F, 209430, 0, 11990, 270)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x000F,
        (
            '#0600020898V#162F#3S#2P给我来人！！#2S',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020899V#004F#6P好，好大的嗓门……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020900V#023F#5P简直像狮吼一样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5519')
    def lambda_5519():
        CameraMove(206340, 0, 12850, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_5519)

    CreateThread(0x000D, 0x00, 0x00, 0x0018)
    CreateThread(0x000E, 0x00, 0x00, 0x0019)
    Sleep(500)

    @scena.Lambda('lambda_5544')
    def lambda_5544():
        ChrTurnDirection(0x00FE, 0x000E, 400)
        Yield()

        Jump('lambda_5544')

    DispatchAsync2(0x0101, 0x0002, lambda_5544)

    @scena.Lambda('lambda_5555')
    def lambda_5555():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_5555')

    DispatchAsync2(0x0103, 0x0002, lambda_5555)

    @scena.Lambda('lambda_5566')
    def lambda_5566():
        ChrTurnDirection(0x00FE, 0x000E, 400)
        Yield()

        Jump('lambda_5566')

    DispatchAsync2(0x0102, 0x0002, lambda_5566)

    Sleep(1000)

    ChrTalk(
        0x000D,
        (
            '#2440020901V将军，有什么吩咐！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2450020902V这些人怎么了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0600020903V#163F#3P各位游击士要回去了！#2P',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600020904V#3P立刻，请他们出去！！#2P',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0035, 0x01, 0x0200)
    OP_28(0x0035, 0x01, 0x0400)
    SetMapFlags(0x00400000)
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T1400._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_5623')

    def _loc_5623(): pass

    label('loc_5623')

    Return()

# id: 0x0015 offset: 0x5624
@scena.Code('func_15_5624')
def func_15_5624():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_5635')
    def lambda_5635():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_5635)

    SetChrPos(0x00FE, 202980, 0, 8390, 0)
    ChrWalkTo(0x00FE, 202920, 0, 11010, 3000, 0x00)
    ChrWalkTo(0x00FE, 207070, 0, 11000, 3000, 0x00)
    SetChrDirection(0x00FE, 90, 400)

    Return()

# id: 0x0016 offset: 0x5682
@scena.Code('func_16_5682')
def func_16_5682():
    Sleep(1600)

    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_5698')
    def lambda_5698():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_5698)

    SetChrPos(0x00FE, 202980, 0, 8390, 0)
    ChrWalkTo(0x00FE, 202920, 0, 11010, 3000, 0x00)
    ChrWalkTo(0x00FE, 205560, 0, 11550, 3000, 0x00)
    SetChrDirection(0x00FE, 90, 400)

    Return()

# id: 0x0017 offset: 0x56E5
@scena.Code('func_17_56E5')
def func_17_56E5():
    Sleep(800)

    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_56FB')
    def lambda_56FB():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_56FB)

    SetChrPos(0x00FE, 202980, 0, 8390, 0)
    ChrWalkTo(0x00FE, 202920, 0, 11010, 3000, 0x00)
    ChrWalkTo(0x00FE, 207110, 0, 12840, 3000, 0x00)
    SetChrDirection(0x00FE, 135, 400)

    Return()

# id: 0x0018 offset: 0x5748
@scena.Code('func_18_5748')
def func_18_5748():
    SetChrChipByIndex(0x00FE, 14)
    SetChrPos(0x00FE, 202630, 0, 7280, 0)
    SetChrFlags(0x00FE, 0x0004)
    ClearChrFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 202920, 0, 11010, 4000, 0x00)
    ChrWalkTo(0x00FE, 203560, 0, 12530, 4000, 0x00)
    SetChrDirection(0x00FE, 90, 400)

    Return()

# id: 0x0019 offset: 0x5798
@scena.Code('func_19_5798')
def func_19_5798():
    Sleep(500)

    SetChrChipByIndex(0x00FE, 14)
    SetChrPos(0x00FE, 202630, 0, 7280, 0)
    SetChrFlags(0x00FE, 0x0004)
    ClearChrFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 202920, 0, 11010, 4000, 0x00)
    SetChrDirection(0x00FE, 90, 400)

    Return()

# id: 0x001A offset: 0x57D9
@scena.Code('func_1A_57D9')
def func_1A_57D9():
    SetChrStatus(0x0003, 0x00, 13)
    OP_B5(0x0003, 0x00)
    OP_B5(0x0003, 0x01)
    OP_B5(0x0003, 0x02)
    OP_B5(0x0003, 0x03)
    OP_B5(0x0003, 0x04)
    EquipCmd(0x03, 0x005C)
    EquipCmd(0x03, 0x00F3)
    EquipCmd(0x03, 0x0111)
    EquipCmd(0x03, 0x025B, 0x00)
    EquipCmd(0x03, 0x026A, 0x01)
    EquipCmd(0x03, 0x025E, 0x02)
    AddCraft(0x0003, 0x00B4)
    AddSCraft(0x0003, 0x00F5)
    FormationAddMember(0x03, 0xFF)
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(14980, 200, 13030, 0)
    OP_67(0, 5040, -10000, 0)
    CameraSetDistance(1680, 0)
    OP_6C(45000, 0)
    OP_6E(484, 0)
    SetChrFlags(0x0016, 0x0080)
    SetChrFlags(0x0017, 0x0080)
    ClearChrFlags(0x0018, 0x0080)
    ClearChrFlags(0x0019, 0x0080)
    ClearChrFlags(0x001A, 0x0080)
    ClearChrFlags(0x001B, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x0101, 0x0004)
    SetChrFlags(0x0102, 0x0004)
    SetChrFlags(0x0103, 0x0004)
    SetChrFlags(0x0104, 0x0004)
    SetChrChipByIndex(0x0101, 15)
    SetChrChipByIndex(0x0102, 16)
    SetChrChipByIndex(0x0103, 17)
    SetChrChipByIndex(0x0104, 10)
    SetChrPos(0x0101, 13130, 200, 10750, 0)
    SetChrPos(0x0102, 14990, 200, 10750, 0)
    SetChrPos(0x0103, 13190, 200, 13350, 180)
    SetChrPos(0x0104, 14980, 200, 13350, 225)
    SetChrSubChip(0x0101, 2)
    SetChrSubChip(0x0102, 0)
    SetChrSubChip(0x0103, 1)
    SetChrSubChip(0x0104, 0)
    FadeIn(2000, 0)
    OP_0D()

    NpcTalk(
        0x0104,
        '金发青年',
        (
            '#0040020963V#030F#5P——重新做一下自我介绍。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040020964V本人名为奥利维尔·朗海姆。\n',
            '漂泊的诗人兼演奏家。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040020965V正如你们所知，从埃雷波尼亚来，\n',
            '到利贝尔王国进行巡回演出的旅行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020966V#001F#6P我叫艾丝蒂尔…… ',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020967V#005F喂、喂喂……\n',
            '凭什么一定要自我介绍啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020968V#010F呵呵，方法姑且不论，\n',
            '毕竟把那种场面和平解决了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020020969V啊，我的名字叫约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020970V#020F#3P我是雪拉扎德。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020971V刚才，我也是一时太冲动了，\n',
            '多亏你出手收拾局面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020972V不管怎样，在这里向你道谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0104, 2)
    Sleep(300)

    ChrTalk(
        0x0104,
        (
            '#0040020973V#035F#5P呵呵，不必道谢哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040020974V本人是爱与和平的热爱者，\n',
            '那样做是理所当然的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040020975V但是，如果你一定要感谢的话，\n',
            '那就请和本人约会一天吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020976V#027F#3P我拒绝。\n',
            '首先，没那个闲工夫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040020977V#034F#5P真是太遗憾了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0104, 0)
    Sleep(100)

    SetChrSubChip(0x0104, 1)
    Sleep(300)

    ChrTalk(
        0x0104,
        (
            '#0040020978V#030F#5P那么作为补偿，\n',
            '约修亚君你来怎么样啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020979V#017F怎么会到我头上呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020020980V请别开这种恶劣的玩笑了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040020981V#033F#5P真意外呢。\n',
            '我可不是在开玩笑哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020982V#018F感觉更差了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1500)

    OP_63(0x0101)

    ChrTalk(
        0x0101,
        (
            '#0010020983V#009F#6P你给我等一下。\n',
            '为什么就不邀请我呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0104, 0)
    Sleep(300)

    ChrTalk(
        0x0104,
        (
            '#0040020984V#033F#5P你？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040020985V嗯～问题是你不仅长得有些抱歉，\n',
            '而且也缺少女性魅力。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040020986V#035F最好还是稍稍向这两位学习一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1700, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1200)

    ChrTalk(
        0x0101,
        (
            '#0010020987V#005F#6P哼～～～！\n',
            '没有女性魅力可真是对不起呀！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020988V再说，约修亚是个男孩子，\n',
            '为什么要向他学习呢！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0102, 1)
    Sleep(300)

    ChrTalk(
        0x0102,
        (
            '#0020020989V#014F冷、冷静点。\n',
            '我一直都觉得艾丝蒂尔非常可爱。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020020990V#017F不过，确实是……\n',
            '缺少了点女性魅力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020991V#509F#6P你、你说什么～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020992V#026F#3P哎呀哎呀……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020993V#020F好了，正如刚才所说，\n',
            '我们现在有很多事情要办。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020994V虽然很抱歉无法向你表达更多的谢意，\n',
            '但是我们差不多该告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040020995V#030F#5P嗯～那样的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040020996V让本人也和你们一起去\n',
            '那个叫柏斯的城市吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040020997V不管怎么说，我也是初次来到王国。\n',
            '就拜托你们做向导了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020998V#020F#3P好吧，只是这种小事的话，\n',
            '我倒是没什么意见……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1200)

    SetChrSubChip(0x0101, 0)

    ChrTalk(
        0x0101,
        (
            '#0010020999V#009F#6P等等，雪拉姐！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0103, 0)
    Sleep(300)

    ChrTalk(
        0x0103,
        (
            '#0030021000V#020F#1P只是做向导的话还好啦。\n',
            '反正大家的目的地都一样嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021001V而且做向导也是\n',
            '游击士工作的一种哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021002V#007F#6P唉，没办法了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021003V#003F可是可是，\n',
            '万一那家伙向约修亚下毒手的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0102,
        (
            '#0020021004V#014F喂喂，艾丝蒂尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0101, 2)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010021005V#002F#6P约修亚，你别担心！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021006V就算发生了什么万一，\n',
            '我也一定会保护你的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021007V#018F我要担心什么呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040021008V#033F#5P真是的，把人家说得像禽兽似的。\n',
            '下次再这样说人家可不依哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040021009V#035F换个好听点的，\n',
            '就叫我『爱情猎人』吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040021010V『恋爱盗贼』也不错呢，嘻嘻……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0101, 2)
    SetChrSubChip(0x0102, 0)
    SetChrSubChip(0x0103, 1)
    OP_62(0x0101, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0103, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1200)

    ChrTalk(
        0x0101,
        (
            '#0010021011V#509F#6P你的脑子是不是进水了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040021012V#031F#5P那么，\n',
            '我们还是赶快向柏斯出发吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040021013V就拜托你们几位带路了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021014V#007F#6P又在旁若无人地自说自唱……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021015V#005F喂，说你呢！\n',
            '多少也要听听别人说的话呀！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(18700, 0, 12270, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0101, 18700, 0, 12267, 180)
    SetChrPos(0x0102, 18700, 0, 12267, 180)
    SetChrPos(0x0103, 18700, 0, 12267, 180)
    SetChrPos(0x0104, 18700, 0, 12267, 180)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0103, 65535)
    SetChrChipByIndex(0x0104, 65535)
    SetChrSubChip(0x0101, 0)
    SetChrSubChip(0x0102, 0)
    SetChrSubChip(0x0103, 0)
    SetChrSubChip(0x0104, 0)
    ClearChrFlags(0x0101, 0x0004)
    ClearChrFlags(0x0102, 0x0004)
    ClearChrFlags(0x0103, 0x0004)
    ClearChrFlags(0x0104, 0x0004)
    FadeIn(1000, 0)
    EventEnd(0x00)
    OP_0D()

    Return()

# id: 0x001B offset: 0x64F9
@scena.Code('func_1B_64F9')
def func_1B_64F9():
    OP_78(0x64, 0x78, 0x82)
    OP_72(0x0005, 0x0004)
    OP_72(0x0006, 0x0004)
    OP_72(0x0007, 0x0004)
    RemoveItem(0x032E, 1)
    SetScenaFlags(ScenaFlag(0x0065, 2, 0x32A))
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    SetChrStatus(0x0003, 0x00, 15)
    FormationAddMember(0x03, 0xFF)
    EquipCmd(0x03, 0x005C)
    EquipCmd(0x03, 0x00F3)
    EquipCmd(0x03, 0x0111)
    EquipCmd(0x03, 0x025B, 0x00)
    EquipCmd(0x03, 0x026A, 0x01)
    EquipCmd(0x03, 0x025E, 0x02)
    SetChrPos(0x0101, 109190, 0, -72940, 180)
    SetChrPos(0x0102, 110080, 0, -71930, 180)
    SetChrPos(0x0103, 108560, 0, -71890, 180)
    SetChrPos(0x0104, 113220, 0, -74620, 225)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    OP_4A(0x000D, 255)
    OP_4A(0x000E, 255)
    SetChrPos(0x000D, 108515, 0, -76468, 0)
    SetChrPos(0x000E, 109535, 0, -76968, 0)
    SetChrChipByIndex(0x000D, 13)
    SetChrChipByIndex(0x000E, 13)
    CameraMove(102920, 0, -73120, 0)
    OP_67(0, 10460, -10000, 0)
    CameraSetDistance(2240, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeIn(2000, 0)
    CameraMove(109920, 0, -73120, 3000)
    OP_0D()

    ChrTalk(
        0x000D,
        (
            '#2440030001V#5P明天早上，\n',
            '将军会亲自审问你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#2440030002V#5P如果你们确实无罪的话，\n',
            '那么两三天之内就会被释放。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2450030003V#2P今晚就先呆在这儿，\n',
            '让头脑稍微冷静一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x000D, 0x01, 0x00, 0x001C)
    Sleep(500)

    CreateThread(0x000E, 0x01, 0x00, 0x001C)
    Sleep(1000)

    @scena.Lambda('lambda_66DF')
    def lambda_66DF():
        OP_69(0x0102, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_66DF)

    Sleep(500)

    SetChrDirection(0x0102, 225, 400)
    SetChrDirection(0x0103, 135, 400)
    SetChrDirection(0x0101, 0, 400)
    WaitForThreadExit(0x0000, 0x0003)

    ChrTalk(
        0x0101,
        (
            '#0010030004V#007F#4P唉……这真是天大的笑话。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030005V竟然连一句解释也不听\n',
            '就把我们关在这种地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030006V#013F#2P如果王国军能早日抓到空贼团，\n',
            '我们的嫌疑就可以洗脱了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020030007V不过，要抓住他们也很难啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030008V#004F#4P啊，为什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030009V#012F#2P还记得在废坑一战里\n',
            '那个空贼头目说的话吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020030010V就是『消息有误』，\n',
            '还有『来得太早了吧』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030011V#505F#4P说起来，\n',
            '他们的确说过这些话。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030012V#580F难、难道他们……\n',
            '早就知道军队的行动！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030013V#012F#2P嗯，我想十有八九是这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020030014V况且这还意味着……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030015V#026F#1P王国军内部有间谍。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030016V或者有人专门向\n',
            '空贼提供军队的情报。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030017V#022F你想说的就是这个吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030018V#012F#2P是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030019V#009F#4P如、如果那是真的，\n',
            '怪不得很难抓到他们啦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030020V真是的，\n',
            '我们还费那么大的力气去追捕他们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030021V#522F#1P真是四处碰壁啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030022V这种时候，如果老师在的话，\n',
            '会怎么应付这样的局面呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0104,
        '青年的声音',
        (
            '#0040030023V呵呵呵……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030024V遇到什么麻烦了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    OP_62(0x0103, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010030025V#505F#4P咦……\n',
            '约修亚，你在说话吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030026V#014F#2P不，我什么也没说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030027V#023F#1P隔壁好像有人在说话。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030028V而且那声音，\n',
            '听起来有点耳熟……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0104,
        '青年的声音',
        (
            '#0040030029V讨厌啦，干嘛跟人家这么见外。\n',
            '下次再这样说人家可不依哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030030V不过，一听到如此成熟艳丽的声音，\n',
            '我就心领神会，知道是谁来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0103, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1500)

    ChrTurnDirection(0x0101, 0x0104, 400)

    ChrTalk(
        0x0101,
        (
            '#0010030031V#509F#4P这、这么没根据的自信……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0104, 400)

    ChrTalk(
        0x0102,
        (
            '#0020030032V#017F#2P还有这种自我陶醉的口吻……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030033V#023F#1P难道隔壁那个人是……奥利维尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(166, 0x00, 0x64)

    NpcTalk(
        0x0104,
        '青年的声音',
        (
            '#0040030034VＢｉｎｇｏ㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_6D59')
    def lambda_6D59():
        CameraMove(111710, 0, -72760, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_6D59)

    @scena.Lambda('lambda_6D71')
    def lambda_6D71():
        OP_6C(0, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_6D71)

    @scena.Lambda('lambda_6D81')
    def lambda_6D81():
        OP_67(0, 6000, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_6D81)

    @scena.Lambda('lambda_6D99')
    def lambda_6D99():
        CameraSetDistance(3000, 3000)

        ExitThread()

    DispatchAsync(0x0001, 0x0003, lambda_6D99)

    Sleep(1000)

    @scena.Lambda('lambda_6DAE')
    def lambda_6DAE():
        ChrWalkTo(0x00FE, 109820, 0, -74610, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6DAE)

    Sleep(500)

    @scena.Lambda('lambda_6DCE')
    def lambda_6DCE():
        ChrWalkTo(0x00FE, 109030, 0, -74180, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_6DCE)

    Sleep(500)

    @scena.Lambda('lambda_6DEE')
    def lambda_6DEE():
        ChrWalkTo(0x00FE, 110150, 0, -73640, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_6DEE)

    WaitForThreadExit(0x0101, 0x0001)
    SetChrDirection(0x0101, 135, 0)
    WaitForThreadExit(0x0103, 0x0001)
    SetChrDirection(0x0103, 135, 0)
    WaitForThreadExit(0x0102, 0x0001)
    SetChrDirection(0x0102, 135, 0)
    WaitForThreadExit(0x0000, 0x0002)

    ChrTalk(
        0x0104,
        (
            '#0040030035V#031F#2P啊啊，\n',
            '没想到我们会在这种地方邂逅……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030036V这就是空之女神的引导啊。\n',
            '我们的命运果然是紧紧相连的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030037V#005F你、你……\n',
            '你怎么会在这里？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030038V你明明应该在柏斯的啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030039V#023F而且还被别人\n',
            '关在这个牢房里面……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030040V究竟发生了什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040030041V#035F#2P呵～呵～\n',
            '你们别像审讯那样问人家嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030042V说起来，这可是一个\n',
            '比山还高、比海还深的故事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030043V#509F这样啊，那我们就不问了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030044V直觉告诉我，\n',
            '听你那所谓的故事肯定挺累人的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030045V#017F真巧啊，艾丝蒂尔。\n',
            '我也恰好有同样的预感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030046V#027F所以说\n',
            '你最好还是不要告诉我们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030047V也是为了我们的健康和美容着想。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040030048V#031F#2P哈·哈·哈。\n',
            '你们就别这么见外嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030049V#030F我这就向你们讲述……\n',
            '这件发生在我身上的悲剧事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030050V#007F（真的不想听啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040030051V#035F#2P和你们分手之后……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030052V我先到超市转了一圈，\n',
            '之后就进了『安特洛丝餐厅』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030053V在品尝了各种美食之后，\n',
            '我即兴弹起了钢琴。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030054V而餐厅负责人被我的表演所震撼，\n',
            '感动得赞不绝口。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030055V之后，他还打算聘请我\n',
            '做餐厅专门的钢琴演奏家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030056V#509F真的会聘请你吗……\n',
            '我记得，你好像是弹鲁特琴的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040030057V#035F#2P呵呵，真正的天才，\n',
            '是会将所有乐器视为自己的朋友。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030058V#030F先不谈这个……\n',
            '我可是提出了一个条件，\n',
            '才会接受他们的聘请要求的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030059V钱，我可以一分都不要，\n',
            '不过，料理和葡萄酒都可以任我享用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030060V#010F说这种话……\n',
            '还真是很像奥利维尔的风格。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020030061V可是，为什么\n',
            '你又会无缘无故地被关在这里呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040030062V#034F#2P啊啊，回想起来，\n',
            '这还真是个听者泣、闻者泪的故事呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030063V那天夜晚……\n',
            '主厨特意为我准备了奶油炒鸭肉，\n',
            '味道嘛，还算过得去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030064V还有特制的鸭血汤，\n',
            '汤味比较浓，不过也还算差强人意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030065V虽说有葡萄酒相伴，\n',
            '不过说到底毕竟只是普通级数的货色。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030066V#509F我越来越想痛揍\n',
            '这个不知足的家伙了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030067V然后呢，你又吃了些什么好东西？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040030068V#030F#2P然后我就打开了餐厅里的冰箱，\n',
            '拿了一瓶貌似极品的葡萄酒。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030069V『格兰·夏利拿』１１８３年的经典杰作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0103,
        (
            '#0030030070V#024F『格兰·夏利拿』……\n',
            '而且还是１１８３年的！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030071V那不是王都的拍卖品吗？\n',
            '被称为『幻之经典』的古典葡萄酒！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040030072V#033F#2P啊，看来雪拉小姐\n',
            '对葡萄酒也蛮了解的嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030073V#033F以前也只是听闻这酒非同一般而已，\n',
            '没想到竟有机会能品尝到这酒中极品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030074V#008F拍、拍卖品……\n',
            '这东西可以值多少钱啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030075V#022F据我所知……\n',
            '至少需要５０万米拉才能买下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010030076V#005F５、５０万米拉～！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030077V只是一瓶葡萄酒而已啊！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030078V#017F物以稀为贵的世界啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020030079V#018F奥利维尔，\n',
            '难道你把那瓶葡萄酒给……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040030080V#031F#2P呵呵，那还用说。\n',
            '实在是美妙得令人难以忘怀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030081V酒香入鼻、馥郁纯正。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030082V丝滑润喉、滋味芳醇。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030083V你们能理解吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030084V闪耀着动人蔷薇之色的时空中，\n',
            '的确是存在这样的东西啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030085V#007F……不想听了………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030086V#017F……果然听得很累………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030087V#025F……已经震惊得无语了………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040030088V#035F#2P话说回来，美味倒是美味，\n',
            '不过料理的分量始终还是太少了嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030089V当我正打算叫主厨\n',
            '再做点其他美味佳肴的时候，\n',
            '餐厅的负责人刚好回来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030090V你也知道我为人相当豪爽。\n',
            '本来打算叫他一起来品尝美酒佳肴，\n',
            '没想到我向他劝酒的时候……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030091V负责人竟然暴跳如雷。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030092V还在我不知所措的瞬间，\n',
            '叫了一大群士兵进来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, 100)

    ChrTalk(
        0x0104,
        (
            '#0040030093V#035F#2P……之后就……怎么说好呢………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -56)

    ChrTalk(
        0x0104,
        (
            '#0040030094V#035F#2P……就是这样了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    Sleep(2000)

    ChrTalk(
        0x0104,
        (
            '#0040030095V#030F#2P以上，就是我会来到这里的原因。\n',
            '一件充满血与泪的悲剧事件。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030096V#031F来吧！\n',
            '对我的不幸遭遇表示一下同情吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030097V#500F……呼…呼………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030098V#015F……嘶…嘶………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030099V#025F……呼唔…傻瓜……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040030100V#033F#2P……………哎哟？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030101V#033F#2P等一下嘛你们……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030102V那个『呼』、『嘶』，\n',
            '还有『呼唔，傻瓜』是什么意思嘛？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030103V#035F很好听吧？\n',
            '故事的高潮才刚刚开始呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030104V我被带到这里之后，\n',
            '等待我的是一场更加严酷的试炼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030105V#036F喂喂——？\n',
            '你们有没有听我说话？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)
    Sleep(2000)

    PlaySE(13, 0x00, 0x64)
    Sleep(5000)

    SetChrPos(0x0101, 109190, 0, -72940, 180)
    SetChrPos(0x0102, 110080, 0, -71930, 180)
    SetChrPos(0x0103, 108560, 0, -71890, 180)
    SetChrPos(0x0104, 113180, 0, -74620, 225)
    OP_4A(0x000D, 255)
    OP_4A(0x000E, 255)
    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x000E, 109535, 0, -76170, 0)
    SetChrChipByIndex(0x000D, 13)
    SetChrChipByIndex(0x000E, 13)
    CameraMove(109920, 0, -73120, 0)
    OP_67(0, 10460, -10000, 0)
    CameraSetDistance(2240, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)

    ChrTalk(
        0x000E,
        (
            '#2450030106V#4P喂！\n',
            '你们几个，快起来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030107V#007F#1P唔……呼哇哇……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030108V嗯……我还要睡～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030109V#017F#1P怎么了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030110V#025F#1P哎呀……\n',
            '一大早就来审问我们了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030111V能不能让我们再睡会儿啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2450030112V#4P不，正好相反。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#2450030113V#4P你们被释放了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030114V#004F#1P啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlayBGM(16)
    FadeIn(2000, 0)
    OP_0D()
    ChrWalkTo(0x000E, 106712, 0, -76140, 2000, 0x00)
    SetChrDirection(0x000E, 0, 400)
    Sleep(500)

    PlaySE(110, 0x00, 0x64)
    OP_72(0x0003, 0x0800)
    OP_70(0x0003, 80)
    OP_73(0x0003)
    ChrWalkTo(0x000E, 108300, 0, -76170, 2000, 0x00)
    SetChrDirection(0x000E, 271, 400)

    ChrTalk(
        0x0101,
        (
            '#0010030115V#004F为、为什么这么快就……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030116V#014F应该有什么理由吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4A(0x0010, 255)
    OP_4A(0x000F, 255)
    SetChrChipByIndex(0x000F, 5)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    SetChrPos(0x0010, 102150, 0, -78020, 0)
    SetChrPos(0x000F, 102150, 0, -76690, 0)
    SetChrFlags(0x000F, 0x0001)

    NpcTalk(
        0x0010,
        '女性的声音',
        (
            '#0360030117V#2P……就是因为有理由。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_803D')
    def lambda_803D():
        CameraMove(108420, 0, -75290, 1500)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_803D)

    SetChrDirection(0x0101, 225, 400)
    SetChrDirection(0x0102, 225, 400)
    SetChrDirection(0x0103, 225, 400)

    @scena.Lambda('lambda_806A')
    def lambda_806A():
        ChrWalkTo(0x00FE, 105100, 0, -78020, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0000, lambda_806A)

    Sleep(600)

    @scena.Lambda('lambda_808A')
    def lambda_808A():
        ChrWalkTo(0x00FE, 104460, 0, -76690, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0000, lambda_808A)

    WaitForThreadExit(0x0010, 0x0000)
    SetChrDirection(0x0010, 45, 400)
    WaitForThreadExit(0x000F, 0x0000)
    SetChrDirection(0x000F, 90, 400)
    WaitForThreadExit(0x0104, 0x0001)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1200)

    ChrTalk(
        0x0101,
        (
            '#0010030118V#004F市、市长姐姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030119V#023F哎呀呀。\n',
            '没想到在这种地方再见面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_815F')
    def lambda_815F():
        CameraMove(106510, 0, -76720, 1500)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_815F)

    CreateThread(0x0101, 0x01, 0x00, 0x001D)
    CreateThread(0x0102, 0x01, 0x00, 0x001E)
    CreateThread(0x0103, 0x01, 0x00, 0x001F)
    WaitForThreadExit(0x0104, 0x0001)
    WaitForThreadExit(0x0102, 0x0001)

    ChrTalk(
        0x0010,
        (
            '#0360030120V#611F#4P给大家添麻烦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360030121V不过请各位安心。\n',
            '将军已经知道你们是清白的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0600030122V#163F唔，不过这并不代表\n',
            '我认同你们的所作所为……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600030123V算了，既然是梅贝尔小姐亲自出面。\n',
            '你们要谢就谢她吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030124V#501F#5P嘿嘿，那样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030125V原来是市长姐姐\n',
            '救我们脱离了苦海。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0360030126V#610F#4P也没那么夸张。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360030127V我不过是将大家的实际情况\n',
            '向摩尔根将军解释清楚而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030128V#505F#5P我们的实际情况……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0600030129V#160F……你们两个。\n',
            '我有句话要问你们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600030130V你们真的是\n',
            '卡西乌斯·布莱特的孩子吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x000F, 400)
    ChrTurnDirection(0x0102, 0x000F, 400)
    ChrTurnDirection(0x0103, 0x000F, 400)

    ChrTalk(
        0x0101,
        (
            '#0010030131V#004F#5P啊……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030132V#015F是的，正如将军所言。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020030133V#010F她是艾丝蒂尔·布莱特……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020030134V而我是养子约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0600030135V#160F是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600030136V的确，小姑娘的样貌\n',
            '颇有几分莱娜小姐的影子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010030137V#004F#5P！！！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030138V您认识我的妈妈！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0600030139V#160F以前到你们家造访的时候，\n',
            '我可是吃过好几顿你母亲煮的菜哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600030140V#163F现在想想，\n',
            '那还是你刚出生时的事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030141V#580F#5P等、等一下……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030142V摩尔根将军\n',
            '也认识我的老爸吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030143V虽然我知道\n',
            '老爸以前是一名军人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0600030144V#160F哼……自从那家伙做起游击士，\n',
            '我就把他当作陌生人了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600030145V我认识的只有\n',
            '身为军人的卡西乌斯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600030146V被称为『稀世的战略家』的卡西乌斯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030147V#505F#5P战略家？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0600030148V#163F真是的，不知道那家伙脑子想什么，\n',
            '加入什么游击士协会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000F, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1200)

    ChrTalk(
        0x000F,
        (
            '#0600030149V#162F……啊啊！\n',
            '一想起这件事就满肚子火！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600030150V我先失陪了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x000F, 0xFF)

    @scena.Lambda('lambda_874E')
    def lambda_874E():
        ChrTurnDirection(0x00FE, 0x000F, 0)
        Yield()

        Jump('lambda_874E')

    DispatchAsync2(0x0010, 0x0001, lambda_874E)

    @scena.Lambda('lambda_875F')
    def lambda_875F():
        ChrTurnDirection(0x00FE, 0x000F, 0)
        Yield()

        Jump('lambda_875F')

    DispatchAsync2(0x0101, 0x0001, lambda_875F)

    @scena.Lambda('lambda_8770')
    def lambda_8770():
        ChrTurnDirection(0x00FE, 0x000F, 0)
        Yield()

        Jump('lambda_8770')

    DispatchAsync2(0x0102, 0x0001, lambda_8770)

    @scena.Lambda('lambda_8781')
    def lambda_8781():
        ChrTurnDirection(0x00FE, 0x000F, 0)
        Yield()

        Jump('lambda_8781')

    DispatchAsync2(0x0103, 0x0001, lambda_8781)

    CreateThread(0x000F, 0x01, 0x00, 0x001C)
    Sleep(500)

    ChrWalkTo(0x000E, 108060, 0, -77910, 3000, 0x00)
    CreateThread(0x000E, 0x01, 0x00, 0x001C)
    Sleep(2000)

    TerminateThread(0x0010, 0x01)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x0103, 0x01)

    ChrTalk(
        0x0101,
        (
            '#0010030151V#007F#5P又、又怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0010, 45, 400)

    ChrTalk(
        0x0010,
        (
            '#0360030152V#611F呵呵……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360030153V因为艾丝蒂尔的父亲\n',
            '是一位非常优秀的军人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360030154V我听说在他退伍的时候，\n',
            '摩尔根将军曾多次出面挽留他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0010, 400)
    ChrTurnDirection(0x0103, 0x0010, 0)
    ChrTurnDirection(0x0102, 0x0010, 0)

    ChrTalk(
        0x0101,
        (
            '#0010030155V#008F#5P有、有这么一回事啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030156V听起来还真有点不可思议。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030157V#020F不过，这可是事实啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030158V将军这么不喜欢游击士，\n',
            '也许就是因为这个原因吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030159V看着自己亲手栽培的部下退伍，\n',
            '对将军来说的确很不是滋味。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030160V#019F说的也是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030161V#509F#5P这么说，就是因为老爸得罪了别人，\n',
            '才害我们白吃了这么多苦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030162V#582F那、那个乱来的老爸～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0360030163V#611F呵呵……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360030164V#610F好了，事情总算解决了。\n',
            '我们马上回柏斯好吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360030165V既然定期船找到了，\n',
            '那么事态肯定会迎来新的局面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360030166V我还有很多事情想和你们商量一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030167V#501F#5P啊，嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030168V…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0360030169V#613F哎呀，怎么了艾丝蒂尔？',
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
            '#0010030170V#505F#5P我非常赞成现在回去，\n',
            '可是我们好像忘了些什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030171V#014F说起来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030172V#023F究竟是什么呢……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    Sleep(400)

    PlaySE(190, 0x00, 0x64)
    Sleep(3000)

    PlayBGM(73)

    NpcTalk(
        0x0104,
        '青年的声音',
        (
            '#0040030173V#3P啊啊……\n',
            '人类果然是无情的生物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1200)

    OP_1F(0x64, 0x00000190)
    SetChrChipByIndex(0x0104, 18)
    SetChrPos(0x0104, 113250, 0, -74620, 180)

    @scena.Lambda('lambda_8C7F')
    def lambda_8C7F():
        CameraMove(109470, 0, -72760, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_8C7F)

    @scena.Lambda('lambda_8C97')
    def lambda_8C97():
        OP_6C(0, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_8C97)

    @scena.Lambda('lambda_8CA7')
    def lambda_8CA7():
        OP_67(0, 6000, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_8CA7)

    @scena.Lambda('lambda_8CBF')
    def lambda_8CBF():
        CameraSetDistance(3000, 3000)

        ExitThread()

    DispatchAsync(0x0001, 0x0003, lambda_8CBF)

    @scena.Lambda('lambda_8CCF')
    def lambda_8CCF():
        ChrTurnDirection(0x00FE, 0x0104, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_8CCF)

    @scena.Lambda('lambda_8CDD')
    def lambda_8CDD():
        ChrTurnDirection(0x00FE, 0x0104, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_8CDD)

    @scena.Lambda('lambda_8CEB')
    def lambda_8CEB():
        ChrTurnDirection(0x00FE, 0x0104, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_8CEB)

    @scena.Lambda('lambda_8CF9')
    def lambda_8CF9():
        ChrTurnDirection(0x00FE, 0x0104, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_8CF9)

    Sleep(3000)

    ChrTalk(
        0x0104,
        (
            '#0040030174V#034F#5P如此轻易就将\n',
            '与自己共度一夜的伙伴忘记……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030175V无言的悲剧……\n',
            '悲哀的无奈啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030176V这样也好，就让我在这黑暗的炼狱里，\n',
            '独身一人走向腐朽的彼方吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0104, 0x00, 0x00, 0x0003)
    Sleep(2000)

    ChrTalk(
        0x0101,
        (
            '#0010030177V#509F#2P你想去就去吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030178V#021F#2P嗯……\n',
            '完全忘了有这么一个人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030179V#010F#2P虽说很同情他，\n',
            '不过怎么才能帮他呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0360030180V#612F#2P那位先生……\n',
            '难道就是传闻中的演奏家吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360030181V毫不客气地品尝了\n',
            '『格兰·夏利拿』的特别客人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))
    OP_20(0x000005DC)
    OP_21()
    PlayBGM(16)
    Sleep(500)

    Fade(250)
    SetChrChipByIndex(0x0104, 65535)
    OP_0D()
    Sleep(500)

    SetChrDirection(0x0104, 225, 400)

    ChrTalk(
        0x0104,
        (
            '#0040030182V#031F#5P呵呵，不敢当……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030183V话说回来，\n',
            '小姐可能有些误会了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030184V因为我已经预付了费用，\n',
            '华丽的钢琴演奏可不是随便就能欣赏到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0360030185V#611F#2P呵呵，听起来挺有趣的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360030186V算了，反正也是顺便的事情。\n',
            '我刚才已经和将军打了招呼，\n',
            '你也可以和他们一起离开这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040030187V#033F#5P哦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_9026')
    def lambda_9026():
        ChrTurnDirection(0x00FE, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_9026)

    Sleep(100)

    @scena.Lambda('lambda_9039')
    def lambda_9039():
        ChrTurnDirection(0x00FE, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_9039)

    Sleep(100)

    @scena.Lambda('lambda_904C')
    def lambda_904C():
        ChrTurnDirection(0x00FE, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_904C)

    WaitForThreadExit(0x0102, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010030188V#506F#2P连、连他也可以释放吗？\n',
            '这样会不会有点勉强……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030189V#023F#2P餐厅方面不用理会吗？\n',
            '如果餐厅对他进行起诉怎么办？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0360030190V#610F#2P呵呵……\n',
            '餐厅方面你们不用担心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360030191V因为餐厅的拥有者\n',
            '就是我梅贝尔本人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030192V#004F#2P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0360030193V#611F#2P那瓶『格兰·夏利拿』\n',
            '也是我之前竞投买下的东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360030194V这样的话你们可以放心了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeIn(1500, 0)
    OP_0D()
    SetChrStatus(0x0000, 0xFE, 0)
    SetChrStatus(0x0001, 0xFE, 0)
    SetChrStatus(0x0002, 0xFE, 0)
    SetChrStatus(0x0003, 0xFE, 0)
    SetChrStatus(0x0004, 0xFE, 0)
    SetChrStatus(0x0005, 0xFE, 0)
    SetChrStatus(0x0006, 0xFE, 0)
    SetChrStatus(0x0007, 0xFE, 0)
    ClearMapFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T1111._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x001C offset: 0x9207
@scena.Code('func_1C_9207')
def func_1C_9207():
    SetChrDirection(0x00FE, 270, 400)
    ChrWalkTo(0x00FE, 103075, 0, -76808, 3000, 0x00)
    ChrWalkTo(0x00FE, 102863, 0, -69973, 3000, 0x00)
    ChrWalkTo(0x00FE, 99072, 2000, -70167, 3000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x001D offset: 0x9250
@scena.Code('func_1D_9250')
def func_1D_9250():
    ChrWalkTo(0x00FE, 107030, 0, -73620, 3000, 0x00)
    ChrWalkTo(0x00FE, 106930, 0, -76150, 3000, 0x00)
    ChrWalkTo(0x00FE, 105910, 0, -76750, 3000, 0x00)
    SetChrDirection(0x00FE, 225, 400)

    Return()

# id: 0x001E offset: 0x9294
@scena.Code('func_1E_9294')
def func_1E_9294():
    Sleep(1000)

    ChrWalkTo(0x00FE, 107030, 0, -73620, 3000, 0x00)
    ChrWalkTo(0x00FE, 106930, 0, -76150, 3000, 0x00)
    SetChrDirection(0x00FE, 225, 400)

    Return()

# id: 0x001F offset: 0x92C9
@scena.Code('func_1F_92C9')
def func_1F_92C9():
    Sleep(500)

    ChrWalkTo(0x00FE, 107030, 0, -73620, 3000, 0x00)
    ChrWalkTo(0x00FE, 106930, 0, -76150, 3000, 0x00)
    ChrWalkTo(0x00FE, 107020, 0, -77050, 3000, 0x00)
    SetChrDirection(0x00FE, 225, 400)

    Return()

# id: 0x0020 offset: 0x9312
@scena.Code('func_20_9312')
def func_20_9312():
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
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2530_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2530   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2530.x'
    header.mapIndex       = 1
    header.bgm            = 14
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
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

# id: 0x10000 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH02600._CH', 'ED6_DT07/CH02600P._CP'),
        ('ED6_DT07/CH02390._CH', 'ED6_DT07/CH02390P._CP'),
        ('ED6_DT07/CH02490._CH', 'ED6_DT07/CH02490P._CP'),
        ('ED6_DT07/CH01660._CH', 'ED6_DT07/CH01660P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH01430._CH', 'ED6_DT07/CH01430P._CP'),
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
        ('ED6_DT07/CH01360._CH', 'ED6_DT07/CH01360P._CP'),
        ('ED6_DT07/CH01580._CH', 'ED6_DT07/CH01580P._CP'),
        ('ED6_DT07/CH01590._CH', 'ED6_DT07/CH01590P._CP'),
        ('ED6_DT07/CH01370._CH', 'ED6_DT07/CH01370P._CP'),
        ('ED6_DT07/CH01090._CH', 'ED6_DT07/CH01090P._CP'),
        ('ED6_DT07/CH01080._CH', 'ED6_DT07/CH01080P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
        ('ED6_DT07/CH01663._CH', 'ED6_DT07/CH01663P._CP'),
        ('ED6_DT07/CH01213._CH', 'ED6_DT07/CH01213P._CP'),
        ('ED6_DT07/CH01433._CH', 'ED6_DT07/CH01433P._CP'),
        ('ED6_DT07/CH01463._CH', 'ED6_DT07/CH01463P._CP'),
        ('ED6_DT07/CH02603._CH', 'ED6_DT07/CH02603P._CP'),
    ]

# id: 0x10001 offset: 0x142
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '科林兹校长',
            x                   = 116010,
            z                   = 200,
            y                   = 4800,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '乔儿',
            x                   = 30700,
            z                   = 0,
            y                   = 55110,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '珐奥娜',
            x                   = 41400,
            z                   = 0,
            y                   = 7500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '拉迪奥老师',
            x                   = 87700,
            z                   = 0,
            y                   = 1000,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '碧欧拉老师',
            x                   = 87700,
            z                   = 0,
            y                   = 2800,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '米丽亚老师',
            x                   = 84400,
            z                   = 0,
            y                   = 1000,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '艾福托老师',
            x                   = 84400,
            z                   = 0,
            y                   = 2800,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '罗迪',
            x                   = 0,
            z                   = 0,
            y                   = 3100,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '坎诺',
            x                   = -2800,
            z                   = 0,
            y                   = 4000,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '雅莉丝',
            x                   = -700,
            z                   = 0,
            y                   = 4000,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '黛拉',
            x                   = 3500,
            z                   = 0,
            y                   = 2000,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '帕布尔',
            x                   = -3100,
            z                   = 0,
            y                   = 5400,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '罗基克',
            x                   = -2900,
            z                   = 0,
            y                   = 30000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0105,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '罗伊斯',
            x                   = -2600,
            z                   = 0,
            y                   = 30800,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '塞尔玛',
            x                   = -6200,
            z                   = 0,
            y                   = 35300,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            name                = '巴托姆',
            x                   = 86000,
            z                   = 0,
            y                   = 30400,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            name                = '基诺奇奥',
            x                   = 86600,
            z                   = 0,
            y                   = 32700,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '妮吉塔',
            x                   = 84800,
            z                   = 0,
            y                   = 33200,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            name                = '戴尔蒙市长',
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
            name                = 'CH22000',
            x                   = 85590,
            z                   = 700,
            y                   = 3050,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1835021,
            chipIndex           = 13,
            npcIndex            = 0x0166,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x3C2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x3C2
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 51000,
            y           = 0,
            z           = 1400,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000021,
        ),
        ScenaEventData(
            x           = 59000,
            y           = 0,
            z           = 1400,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000022,
        ),
        ScenaEventData(
            x           = 33000,
            y           = 0,
            z           = 1400,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000023,
        ),
        ScenaEventData(
            x           = 58990,
            y           = 0,
            z           = 31330,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000024,
        ),
        ScenaEventData(
            x           = 33000,
            y           = 0,
            z           = 31400,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000025,
        ),
    )

# id: 0x10004 offset: 0x462
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 85590,
            triggerZ            = 700,
            triggerY            = 3400,
            triggerRange        = 1000,
            actorX              = 85590,
            actorZ              = 1000,
            actorY              = 3050,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0016,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 48200,
            triggerZ            = 0,
            triggerY            = 0,
            triggerRange        = 800,
            actorX              = 48200,
            actorZ              = 1000,
            actorY              = 0,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0017,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 31580,
            triggerZ            = 0,
            triggerY            = 1450,
            triggerRange        = 800,
            actorX              = 31580,
            actorZ              = 1000,
            actorY              = 1450,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0018,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 51020,
            triggerZ            = 0,
            triggerY            = 31860,
            triggerRange        = 800,
            actorX              = 51020,
            actorZ              = 1500,
            actorY              = 31860,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0019,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 57380,
            triggerZ            = 0,
            triggerY            = 31460,
            triggerRange        = 800,
            actorX              = 57380,
            actorZ              = 1000,
            actorY              = 31460,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 31630,
            triggerZ            = 0,
            triggerY            = 31460,
            triggerRange        = 800,
            actorX              = 31630,
            actorZ              = 1000,
            actorY              = 31460,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 3420,
            triggerZ            = 0,
            triggerY            = 0,
            triggerRange        = 800,
            actorX              = 3420,
            actorZ              = 1000,
            actorY              = 0,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001C,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 3570,
            triggerZ            = 0,
            triggerY            = 34450,
            triggerRange        = 800,
            actorX              = 3570,
            actorZ              = 1200,
            actorY              = 34450,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001D,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 790,
            triggerZ            = 0,
            triggerY            = 35530,
            triggerRange        = 800,
            actorX              = 790,
            actorZ              = 1200,
            actorY              = 35530,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001E,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -5010,
            triggerZ            = 0,
            triggerY            = 29180,
            triggerRange        = 800,
            actorX              = -5010,
            actorZ              = 1200,
            actorY              = 29180,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001F,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -1970,
            triggerZ            = 0,
            triggerY            = 30780,
            triggerRange        = 800,
            actorX              = -1970,
            actorZ              = 1200,
            actorY              = 30780,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0020,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 41160,
            triggerZ            = 0,
            triggerY            = 6230,
            triggerRange        = 400,
            actorX              = 41400,
            actorZ              = 1500,
            actorY              = 7500,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x612
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_668',
    )

    ChrSetPos(0x000B, 5320, 250, 2110, 270)
    ChrSetPos(0x000C, 5300, 250, 32080, 267)
    ChrSetFlags(0x000C, 0x0010)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetPos(0x000F, 400, 0, 0, 90)
    ChrSetFlags(0x000F, 0x0004)
    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0013, 0x0080)

    Jump('loc_9C1')

    def _loc_668(): pass

    label('loc_668')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_6AE',
    )

    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0014, 0x0080)
    ChrSetFlags(0x0015, 0x0080)
    ChrSetFlags(0x0016, 0x0080)

    Jump('loc_9C1')

    def _loc_6AE(): pass

    label('loc_6AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_740',
    )

    ChrSetPos(0x000B, 1710, 0, 4970, 180)
    ChrSetPos(0x000C, -6910, 0, 33220, 90)
    ChrSetPos(0x000D, 95370, 250, 34220, 225)
    ChrSetPos(0x0008, 43470, 0, 5280, 225)
    ChrSetPos(0x0010, -7060, 0, 1680, 90)
    ChrSetPos(0x0011, 920, 0, -1500, 0)
    ChrSetPos(0x0012, -1590, 0, 34700, 0)
    ChrSetPos(0x0014, 1300, 0, 28510, 90)

    Jump('loc_9C1')

    def _loc_740(): pass

    label('loc_740')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_7C4',
    )

    ChrSetPos(0x000B, 1710, 0, 4970, 180)
    ChrSetPos(0x000C, -6910, 0, 33220, 90)
    ChrSetPos(0x000D, 95370, 250, 34220, 225)
    ChrSetPos(0x0008, 42940, 0, 1070, 270)
    ChrSetFlags(0x0008, 0x0010)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetPos(0x0010, -7060, 0, 1680, 90)
    ChrSetPos(0x0011, 920, 0, -1500, 0)
    ChrSetFlags(0x0014, 0x0080)

    Jump('loc_9C1')

    def _loc_7C4(): pass

    label('loc_7C4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_887',
    )

    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetPos(0x0010, -5200, 0, 2050, 0)
    ChrSetPos(0x0011, 4500, 250, 4019, 270)
    ChrSetFlags(0x0014, 0x0080)
    ChrSetFlags(0x0014, 0x0008)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0018, 0x0080)
    ChrSetFlags(0x0018, 0x0010)
    ChrClearFlags(0x0019, 0x0080)
    ChrSetFlags(0x0019, 0x0010)
    ChrSetChipByIndex(0x000D, 16)
    ChrSetPos(0x000D, 84450, 250, 2790, 90)
    ChrSetFlags(0x000D, 0x0004)
    ChrSetFlags(0x000D, 0x0010)
    TerminateThread(0x000D, 0xFF)
    ChrSetChipByIndex(0x000B, 14)
    ChrSetPos(0x000B, 84450, 250, 1030, 90)
    ChrSetFlags(0x000B, 0x0004)
    ChrSetFlags(0x000B, 0x0010)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x0008, 0xFF)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetFlags(0x0008, 0x0010)
    ChrSetChipByIndex(0x0008, 18)

    Jump('loc_9C1')

    def _loc_887(): pass

    label('loc_887')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_8BB',
    )

    ChrSetPos(0x000C, 5300, 250, 32080, 267)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0015, 0x0080)

    Jump('loc_9C1')

    def _loc_8BB(): pass

    label('loc_8BB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 6, 0x42E)),
            Expr.Return,
        ),
        'loc_8F7',
    )

    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0014, 0x0080)
    ChrSetFlags(0x0015, 0x0080)

    Jump('loc_9C1')

    def _loc_8F7(): pass

    label('loc_8F7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_938',
    )

    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0014, 0x0080)
    ChrSetFlags(0x0015, 0x0080)

    Jump('loc_9C1')

    def _loc_938(): pass

    label('loc_938')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 6, 0x41E)),
            Expr.Return,
        ),
        'loc_97E',
    )

    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0014, 0x0080)
    ChrSetFlags(0x0015, 0x0080)

    Jump('loc_9C1')

    def _loc_97E(): pass

    label('loc_97E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_9C1',
    )

    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0014, 0x0080)
    ChrSetFlags(0x0015, 0x0080)

    def _loc_9C1(): pass

    label('loc_9C1')

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0080)"),
            Expr.Return,
        ),
        'loc_9D1',
    )

    ChrSetFlags(0x001B, 0x0080)

    def _loc_9D1(): pass

    label('loc_9D1')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000072, 'loc_9DD'),
        (-1, 'loc_9F0'),
    )

    def _loc_9DD(): pass

    label('loc_9DD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0089, 0, 0x448)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_9ED',
    )

    Event(0, func_15_36E3)

    def _loc_9ED(): pass

    label('loc_9ED')

    Jump('loc_9F0')

    def _loc_9F0(): pass

    label('loc_9F0')

    Return()

# id: 0x0001 offset: 0x9F1
@scena.Code('func_01_9F1')
def func_01_9F1():
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
        'loc_A12',
    )

    OP_B1('t2530_y')

    Jump('loc_A1B')

    def _loc_A12(): pass

    label('loc_A12')

    OP_B1('t2530_n')

    def _loc_A1B(): pass

    label('loc_A1B')

    OP_64(0x00, 0x0001)

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0020)"),
            Expr.Return,
        ),
        'loc_A2E',
    )

    OP_65(0x00, 0x0001)

    def _loc_A2E(): pass

    label('loc_A2E')

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0080)"),
            Expr.Return,
        ),
        'loc_A42',
    )

    OP_64(0x00, 0x0001)
    ChrSetFlags(0x001B, 0x0080)

    def _loc_A42(): pass

    label('loc_A42')

    Return()

# id: 0x0002 offset: 0xA43
@scena.Code('func_02_A43')
def func_02_A43():
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
        'loc_A68',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_BAA')

    def _loc_A68(): pass

    label('loc_A68')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A81',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_BAA')

    def _loc_A81(): pass

    label('loc_A81')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A9A',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_BAA')

    def _loc_A9A(): pass

    label('loc_A9A')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AB3',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_BAA')

    def _loc_AB3(): pass

    label('loc_AB3')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_ACC',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_BAA')

    def _loc_ACC(): pass

    label('loc_ACC')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AE5',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_BAA')

    def _loc_AE5(): pass

    label('loc_AE5')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AFE',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_BAA')

    def _loc_AFE(): pass

    label('loc_AFE')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B17',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_BAA')

    def _loc_B17(): pass

    label('loc_B17')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B30',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_BAA')

    def _loc_B30(): pass

    label('loc_B30')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B49',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_BAA')

    def _loc_B49(): pass

    label('loc_B49')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B62',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_BAA')

    def _loc_B62(): pass

    label('loc_B62')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B7B',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_BAA')

    def _loc_B7B(): pass

    label('loc_B7B')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B94',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_BAA')

    def _loc_B94(): pass

    label('loc_B94')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BAA',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_BAA(): pass

    label('loc_BAA')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_BBF',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_BAA')

    def _loc_BBF(): pass

    label('loc_BBF')

    Return()

# id: 0x0003 offset: 0xBC0
@scena.Code('func_03_BC0')
def func_03_BC0():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_CA7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C47',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '#780F是艾丝蒂尔和约修亚啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '犯人总算给逮捕归案了，\n',
            '实在是太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '等会儿我想听你们\n',
            '说明一下事情的经过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CA4')

    def _loc_C47(): pass

    label('loc_C47')

    ChrTalk(
        0x00FE,
        (
            '#780F抓到袭击孤儿院的犯人\n',
            '总算是让大家安心了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '你们等会儿可以把\n',
            '把事情的经过告诉我吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CA4(): pass

    label('loc_CA4')

    Jump('loc_1216')

    def _loc_CA7(): pass

    label('loc_CA7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 5, 0x435)),
            Expr.Return,
        ),
        'loc_D87',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D3A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '#780F艾丝蒂尔、约修亚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我听说特蕾莎院长的事情了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '怎么说呢……\n',
            '实在是很过分的事啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '这件事实在无法用语言表达……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D84')

    def _loc_D3A(): pass

    label('loc_D3A')

    ChrTalk(
        0x00FE,
        (
            '#780F我听说特蕾莎院长的事情了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '怎么说呢……\n',
            '实在是很过分的事啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D84(): pass

    label('loc_D84')

    Jump('loc_1216')

    def _loc_D87(): pass

    label('loc_D87')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_EA7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E49',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '#780F艾丝蒂尔、约修亚，\n',
            '这次真是麻烦你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '舞台剧的演出很成功。\n',
            '特别是约修亚饰演的塞茜莉亚公主，\n',
            '演技和扮相实在是太感人了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '下次有机会的话\n',
            '请务必再到我们学院来玩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EA4')

    def _loc_E49(): pass

    label('loc_E49')

    ChrTalk(
        0x00FE,
        (
            '#780F艾丝蒂尔、约修亚，\n',
            '这次真是麻烦你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '下次有机会的话\n',
            '请务必再到我们学院来玩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EA4(): pass

    label('loc_EA4')

    Jump('loc_1216')

    def _loc_EA7(): pass

    label('loc_EA7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_F7C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F35',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '#0530850025V#780F哦，是你们。\n',
            '这次真是史无前例的盛况啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530060102V大家都很期待舞台剧，\n',
            '请务必让学园祭圆满成功。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F79')

    def _loc_F35(): pass

    label('loc_F35')

    ChrTalk(
        0x00FE,
        (
            '#0530060103V#780F大家都很期待舞台剧。\n',
            '请务必让学园祭圆满成功。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F79(): pass

    label('loc_F79')

    Jump('loc_1216')

    def _loc_F7C(): pass

    label('loc_F7C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_10D2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_105F',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '#780F戴尔蒙市长，\n',
            '自从去年的王国会议之后我们也好久不见了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530060080V这段时间，你身体怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '#660F就像你看到的，结实着呢。\n',
            '科林兹校长也很精神嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490060082V今天我打算好好放松一下。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0008, 0x0010)

    Jump('loc_10CF')

    def _loc_105F(): pass

    label('loc_105F')

    ChrTalk(
        0x00FE,
        (
            '#780F我还要找时间和市长先生谈谈\n',
            '关于学院运营的事情呢。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '虽说是王立的教育机构，\n',
            '但也要重视地方上的建议。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10CF(): pass

    label('loc_10CF')

    Jump('loc_1216')

    def _loc_10D2(): pass

    label('loc_10D2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0089, 0, 0x448)),
            Expr.Return,
        ),
        'loc_119A',
    )

    ChrClearFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x87),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_10FB',
    )

    ChrSetSubChip(0x00FE, 1)

    Jump('loc_1116')

    def _loc_10FB(): pass

    label('loc_10FB')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1111',
    )

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_1116')

    def _loc_1111(): pass

    label('loc_1111')

    ChrSetSubChip(0x00FE, 2)

    def _loc_1116(): pass

    label('loc_1116')

    ChrSetDirection(0x00FE, 180, 0)
    ChrSetFlags(0x00FE, 0x0010)

    ChrTalk(
        0x0008,
        (
            '#0530060099V#780F呵呵，可别玩得太过火，\n',
            '影响到明天的活动就不好了哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530060100V那么，你们开心地去玩吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x00FE, 0)

    Jump('loc_1216')

    def _loc_119A(): pass

    label('loc_119A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_1216',
    )

    ChrTalk(
        0x00FE,
        (
            '#0530060085V#780F你们住宿的地方我们已经给安排好了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530060086V学院里也有食堂，\n',
            '你们就安心准备好舞台剧吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1216(): pass

    label('loc_1216')

    TalkEnd(0x0008)

    Return()

# id: 0x0004 offset: 0x121A
@scena.Code('func_04_121A')
def func_04_121A():
    Call(0, 0x0005)

    Return()

# id: 0x0005 offset: 0x121F
@scena.Code('func_05_121F')
def func_05_121F():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_12B6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1292',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x000A,
        (
            '啊，怎么了？\n',
            '你们要找人吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '现在正好是\n',
            '上课结束的时间。\n',
            '你们可以去和同学们见面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12B3')

    def _loc_1292(): pass

    label('loc_1292')

    ChrTalk(
        0x000A,
        (
            '啊，怎么了？\n',
            '你们要找人吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12B3(): pass

    label('loc_12B3')

    Jump('loc_18A8')

    def _loc_12B6(): pass

    label('loc_12B6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_1301',
    )

    ChrTalk(
        0x000A,
        (
            '呵呵，学园祭很成功呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '学生们正在\n',
            '礼堂那里庆祝胜利呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18A8')

    def _loc_1301(): pass

    label('loc_1301')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_13AE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_136A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x000A,
        (
            '说起来\n',
            '真是出乎意料的盛况啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '有很多带孩子来的家长，\n',
            '我担心会有孩子走失。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13AB')

    def _loc_136A(): pass

    label('loc_136A')

    ChrTalk(
        0x000A,
        (
            '请问您想找哪位呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我可以使用广播\n',
            '来帮您寻找想找的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13AB(): pass

    label('loc_13AB')

    Jump('loc_18A8')

    def _loc_13AE(): pass

    label('loc_13AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_1477',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_143C',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x000A,
        (
            '各种活动都在\n',
            '校园和主楼里进行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '下午礼堂那边\n',
            '预定要演出舞台剧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '食堂作为休息场所开放，\n',
            '你们可以好好利用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1474')

    def _loc_143C(): pass

    label('loc_143C')

    ChrTalk(
        0x000A,
        (
            '为了以防万一，\n',
            '学园祭举行的时候\n',
            '宿舍楼都是锁住的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1474(): pass

    label('loc_1474')

    Jump('loc_18A8')

    def _loc_1477(): pass

    label('loc_1477')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_14F3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_14C7',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x000A,
        (
            '准备完成了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '到了明天\n',
            '就会有许多客人来参观了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14F0')

    def _loc_14C7(): pass

    label('loc_14C7')

    ChrTalk(
        0x000A,
        (
            '准备完成了吗？\n',
            '明天就要正式表演了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14F0(): pass

    label('loc_14F0')

    Jump('loc_18A8')

    def _loc_14F3(): pass

    label('loc_14F3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_15AC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1574',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x000A,
        (
            '呵呵，一到下课时间，\n',
            '校园里就会变得热闹起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '学园祭就要开始了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '希望同学们\n',
            '都能加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15A9')

    def _loc_1574(): pass

    label('loc_1574')

    ChrTalk(
        0x000A,
        (
            '呵呵，一到下课时间，\n',
            '校园里就会变得热闹起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15A9(): pass

    label('loc_15A9')

    Jump('loc_18A8')

    def _loc_15AC(): pass

    label('loc_15AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 6, 0x42E)),
            Expr.Return,
        ),
        'loc_16C5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1680',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x000A,
        (
            '啊，科洛丝。\n',
            '你回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F对不起，\n',
            '我到现在才回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '呵呵，回来就好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '要找校长的话，\n',
            '他就在办公室里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '他也很担心\n',
            '科洛丝你呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F啊，是的。\n',
            '我们现在就过去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16C2')

    def _loc_1680(): pass

    label('loc_1680')

    ChrTalk(
        0x000A,
        (
            '要找校长的话，\n',
            '他就在办公室里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '他也很担心\n',
            '科洛丝你呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_16C2(): pass

    label('loc_16C2')

    Jump('loc_18A8')

    def _loc_16C5(): pass

    label('loc_16C5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_177E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1758',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x000A,
        (
            '啊，科洛丝。\n',
            '你们外出回来了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F啊，不是的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '对不起，\n',
            '我们还没有办完事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '是吗。\n',
            '外出时请务必要小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_177B')

    def _loc_1758(): pass

    label('loc_1758')

    ChrTalk(
        0x000A,
        (
            '科洛丝，\n',
            '外出时请务必要小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_177B(): pass

    label('loc_177B')

    Jump('loc_18A8')

    def _loc_177E(): pass

    label('loc_177E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 6, 0x41E)),
            Expr.Return,
        ),
        'loc_17D0',
    )

    ChrTalk(
        0x000A,
        (
            '啊，是想参观吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '很抱歉，\n',
            '现在学生们正在上课，\n',
            '不能带您参观。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18A8')

    def _loc_17D0(): pass

    label('loc_17D0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_18A8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1878',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x000A,
        (
            '啊，科洛丝。\n',
            '已经回来了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F不是，\n',
            '我正要带这两位朋友去卢安呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '是吗，难得的假日，\n',
            '就好好地放松一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F嗯，谢谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18A8')

    def _loc_1878(): pass

    label('loc_1878')

    ChrTalk(
        0x000A,
        (
            '科洛丝，\n',
            '难得的假日，\n',
            '就好好地放松一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18A8(): pass

    label('loc_18A8')

    TalkEnd(0x000A)

    Return()

# id: 0x0006 offset: 0x18AC
@scena.Code('func_06_18AC')
def func_06_18AC():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_18E8',
    )

    ChrTalk(
        0x00FE,
        (
            '课虽然上完了，\n',
            '但还有学生们的问题要回答。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B36')

    def _loc_18E8(): pass

    label('loc_18E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_193A',
    )

    ChrTalk(
        0x00FE,
        (
            '唔，\n',
            '我们班的同学干劲热火朝天啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家做布景\n',
            '也非常地努力嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B36')

    def _loc_193A(): pass

    label('loc_193A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_198A',
    )

    ChrTalk(
        0x00FE,
        (
            '学园祭的主角\n',
            '果然还是学生们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家都比平时\n',
            '要活跃许多呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B36')

    def _loc_198A(): pass

    label('loc_198A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_1ADB',
    )

    ChrClearFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_19B3',
    )

    ChrSetSubChip(0x00FE, 1)

    Jump('loc_19E4')

    def _loc_19B3(): pass

    label('loc_19B3')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x87),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_19C9',
    )

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_19E4')

    def _loc_19C9(): pass

    label('loc_19C9')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x10E),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_19DF',
    )

    ChrSetSubChip(0x00FE, 2)

    Jump('loc_19E4')

    def _loc_19DF(): pass

    label('loc_19DF')

    ChrSetSubChip(0x00FE, 1)

    def _loc_19E4(): pass

    label('loc_19E4')

    ChrSetDirection(0x00FE, 90, 0)
    ChrSetFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A87',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '你们好像是\n',
            '从洛连特来的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '其实我也是\n',
            '洛连特出身的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说起来我父母\n',
            '也要来参观学园祭呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……我要是能招待他们就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AD3')

    def _loc_1A87(): pass

    label('loc_1A87')

    ChrTalk(
        0x00FE,
        (
            '对了对了……\n',
            '舞台剧表演我也看了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是热闹啊。\n',
            '那天真是很开心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AD3(): pass

    label('loc_1AD3')

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_1B36')

    def _loc_1ADB(): pass

    label('loc_1ADB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_1B36',
    )

    ChrTalk(
        0x00FE,
        (
            '学园祭快到了，\n',
            '同学们就连上课\n',
            '都开始坐不安定了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，这也是没办法的呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B36(): pass

    label('loc_1B36')

    TalkEnd(0x000B)

    Return()

# id: 0x0007 offset: 0x1B3A
@scena.Code('func_07_1B3A')
def func_07_1B3A():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_1BCA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1BA0',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '唔唔，\n',
            '这个问题……',
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
            '怎么做好呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x000C, 0x0010)

    Jump('loc_1BC7')

    def _loc_1BA0(): pass

    label('loc_1BA0')

    ChrTalk(
        0x00FE,
        (
            '呼，这里的学生\n',
            '都很热心于学习呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1BC7(): pass

    label('loc_1BC7')

    Jump('loc_1DF4')

    def _loc_1BCA(): pass

    label('loc_1BCA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_1C2C',
    )

    ChrTalk(
        0x00FE,
        (
            '下午终于要上演\n',
            '万众瞩目的舞台剧了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '拜托你们二位了！\n',
            '我相信一定能取得成功的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DF4')

    def _loc_1C2C(): pass

    label('loc_1C2C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_1CDA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1CB6',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '嗯，\n',
            '我们班的同学相当认真呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然我觉得\n',
            '研究发表什么的太朴素了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过这样也好，\n',
            '有很多客人来看呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CD7')

    def _loc_1CB6(): pass

    label('loc_1CB6')

    ChrTalk(
        0x00FE,
        (
            '决不能输给\n',
            '米丽亚的班级……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1CD7(): pass

    label('loc_1CD7')

    Jump('loc_1DF4')

    def _loc_1CDA(): pass

    label('loc_1CDA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_1DF4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1DCD',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '啊，科洛丝。\n',
            '你回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F碧欧拉老师，\n',
            '我刚刚才回来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '对不起，\n',
            '我又没来上课。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，没关系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你不是有重要的事情吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有时间的话来一下办公室，\n',
            '我给你漏下的上课笔记。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F嗯，我过会儿就去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DF4')

    def _loc_1DCD(): pass

    label('loc_1DCD')

    ChrTalk(
        0x00FE,
        (
            '我还是趁现在\n',
            '批改一下考试卷子吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1DF4(): pass

    label('loc_1DF4')

    TalkEnd(0x000C)

    Return()

# id: 0x0008 offset: 0x1DF8
@scena.Code('func_08_1DF8')
def func_08_1DF8():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_1E4E',
    )

    ChrTalk(
        0x00FE,
        (
            '我是今年\n',
            '入学考试的出题老师。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我已经跃跃欲试了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2106')

    def _loc_1E4E(): pass

    label('loc_1E4E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_1EEB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1EBD',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '为什么我们班的同学\n',
            '尽办些游戏和占卜的活动……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '维奥拉的班级\n',
            '都是很正经的东西呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EE8')

    def _loc_1EBD(): pass

    label('loc_1EBD')

    ChrTalk(
        0x00FE,
        (
            '那个班的老师不行，\n',
            '学生们却都很优秀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1EE8(): pass

    label('loc_1EE8')

    Jump('loc_2106')

    def _loc_1EEB(): pass

    label('loc_1EEB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_1F1F',
    )

    ChrTalk(
        0x00FE,
        (
            '人还真是多呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家都很闲吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2106')

    def _loc_1F1F(): pass

    label('loc_1F1F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_2020',
    )

    ChrClearFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1F48',
    )

    ChrSetSubChip(0x00FE, 1)

    Jump('loc_1F79')

    def _loc_1F48(): pass

    label('loc_1F48')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x87),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1F5E',
    )

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_1F79')

    def _loc_1F5E(): pass

    label('loc_1F5E')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x10E),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1F74',
    )

    ChrSetSubChip(0x00FE, 2)

    Jump('loc_1F79')

    def _loc_1F74(): pass

    label('loc_1F74')

    ChrSetSubChip(0x00FE, 1)

    def _loc_1F79(): pass

    label('loc_1F79')

    ChrSetDirection(0x00FE, 90, 0)
    ChrSetFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1FE9',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '嗯，明天就能好好看到\n',
            '同学们努力的成果了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '无论怎样，\n',
            '那天我可不能再啰嗦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2018')

    def _loc_1FE9(): pass

    label('loc_1FE9')

    ChrTalk(
        0x00FE,
        (
            '嗯，明天就能好好看到\n',
            '同学们努力的成果了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2018(): pass

    label('loc_2018')

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_2106')

    def _loc_2020(): pass

    label('loc_2020')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_2106',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_20B0',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '在学园祭的准备期间，\n',
            '大家学习都提不起精神来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算在课上\n',
            '也开始不愿动脑筋了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要不要明天\n',
            '来次突击测验呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2106')

    def _loc_20B0(): pass

    label('loc_20B0')

    ChrTalk(
        0x00FE,
        (
            '在学园祭的准备期间，\n',
            '大家学习都提不起精神来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要不要明天\n',
            '来次突击测验呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2106(): pass

    label('loc_2106')

    TalkEnd(0x000D)

    Return()

# id: 0x0009 offset: 0x210A
@scena.Code('func_09_210A')
def func_09_210A():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_2158',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，差不多该去巡视了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我要看看\n',
            '有没有同学太过懒散了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23DE')

    def _loc_2158(): pass

    label('loc_2158')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_2248',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_21D6',
    )

    ChrTalk(
        0x00FE,
        (
            '哦，昨天真是辛苦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我真是个不称职的老师啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了防止再发生突发事件，\n',
            '我在这里待命。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2245')

    def _loc_21D6(): pass

    label('loc_21D6')

    ChrTalk(
        0x00FE,
        (
            '昨天，\n',
            '有学生说在旧校舍看到了魔兽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了慎重起见，\n',
            '我把旧校舍的门锁紧了。\n',
            '不过一会儿还是再去看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2245(): pass

    label('loc_2245')

    Jump('loc_23DE')

    def _loc_2248(): pass

    label('loc_2248')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 6, 0x42E)),
            Expr.Return,
        ),
        'loc_2351',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_22EA',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '这个学园一共设立了\n',
            '三个方向的专业。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我教的科目则是\n',
            '所有专业都必修的科目——体育。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在这个时候我没有课，\n',
            '就来整理一下教案了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_234E')

    def _loc_22EA(): pass

    label('loc_22EA')

    ChrTalk(
        0x00FE,
        (
            '我教的科目则是\n',
            '所有专业都必修的科目——体育。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在这个时候我没有课，\n',
            '就来整理一下教案了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_234E(): pass

    label('loc_234E')

    Jump('loc_23DE')

    def _loc_2351(): pass

    label('loc_2351')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_23DE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_23BD',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '唔，怎么，\n',
            '你们是哪个班的学生？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在正在上课哦。\n',
            '要有外出许可证\n',
            '才能出去哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23DE')

    def _loc_23BD(): pass

    label('loc_23BD')

    ChrTalk(
        0x00FE,
        (
            '要有外出许可证\n',
            '才能出去哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_23DE(): pass

    label('loc_23DE')

    TalkEnd(0x000E)

    Return()

# id: 0x000A offset: 0x23E2
@scena.Code('func_0A_23E2')
def func_0A_23E2():
    TalkBegin(0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_2456',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2436',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '呼～\n',
            '今天的课总算上完了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '下午的课\n',
            '一定会睡着的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2453')

    def _loc_2436(): pass

    label('loc_2436')

    ChrTalk(
        0x00FE,
        (
            '下午的课\n',
            '一定会睡着的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2453(): pass

    label('loc_2453')

    Jump('loc_2513')

    def _loc_2456(): pass

    label('loc_2456')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_2513',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_24CD',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '我一直在照顾\n',
            '我们社团的店面呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '班里的活动\n',
            '就没办法参加了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，感觉真是很充实呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2513')

    def _loc_24CD(): pass

    label('loc_24CD')

    ChrTalk(
        0x00FE,
        (
            '我一直在照顾\n',
            '我们社团的店面呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '班里的活动\n',
            '就没办法参加了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2513(): pass

    label('loc_2513')

    TalkEnd(0x000F)

    Return()

# id: 0x000B offset: 0x2517
@scena.Code('func_0B_2517')
def func_0B_2517():
    TalkBegin(0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_2563',
    )

    ChrTalk(
        0x00FE,
        (
            '那么，该去社团活动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天要把\n',
            '画到一半的绘画完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2762')

    def _loc_2563(): pass

    label('loc_2563')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_25A6',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，\n',
            '茶座还是要办成这样才对啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '辛苦也值得了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2762')

    def _loc_25A6(): pass

    label('loc_25A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_25FE',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，不管怎么说\n',
            '准备工作还是赶上了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为通宵工作，\n',
            '现在好困啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2762')

    def _loc_25FE(): pass

    label('loc_25FE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_26AF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2664',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))
    OP_62(0x0010, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '唔哇哇！\n',
            '怎么回事！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呆在这里\n',
            '会来不及准备的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26AC')

    def _loc_2664(): pass

    label('loc_2664')

    ChrTalk(
        0x00FE,
        (
            '……难道说\n',
            '这样下去要通宵赶工了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '做衣服花了太多时间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_26AC(): pass

    label('loc_26AC')

    Jump('loc_2762')

    def _loc_26AF(): pass

    label('loc_26AF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_2762',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2744',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '啦啦啦～～⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我正在做\n',
            '摆摊时穿的衣服。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔～就是要在这种时候集中精力！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为做这种东西\n',
            '是我最喜欢干的事情了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2762')

    def _loc_2744(): pass

    label('loc_2744')

    ChrTalk(
        0x00FE,
        (
            '接下来还要做房间的装饰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2762(): pass

    label('loc_2762')

    TalkEnd(0x0010)

    Return()

# id: 0x000C offset: 0x2766
@scena.Code('func_0C_2766')
def func_0C_2766():
    TalkBegin(0x0011)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_27AC',
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
            '如果需要的话，\n',
            '我可以帮你们找空位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28DC')

    def _loc_27AC(): pass

    label('loc_27AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_27F2',
    )

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，这件制服很可爱吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '坎诺还为我准备了好多呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28DC')

    def _loc_27F2(): pass

    label('loc_27F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_285C',
    )

    ChrTalk(
        0x00FE,
        (
            '一想时间还很充裕\n',
            '就不由自主地松懈了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过应该还来得及。\n',
            '努力把店面打扮得漂亮一些吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28DC')

    def _loc_285C(): pass

    label('loc_285C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_28DC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_28AD',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '坎诺君的手\n',
            '可巧啦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次他缝了个\n',
            '布娃娃给我呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28DC')

    def _loc_28AD(): pass

    label('loc_28AD')

    ChrTalk(
        0x00FE,
        (
            '就算是演出用的女佣服装\n',
            '也是他自己做的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_28DC(): pass

    label('loc_28DC')

    TalkEnd(0x0011)

    Return()

# id: 0x000D offset: 0x28E0
@scena.Code('func_0D_28E0')
def func_0D_28E0():
    TalkBegin(0x0012)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_299D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_296C',
    )

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '刚才讲的课，\n',
            '有一些地方不明白……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔～\n',
            '我还想问问老师呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '米丽亚老师\n',
            '才刚上完课\n',
            '就马上回办公室了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_299A')

    def _loc_296C(): pass

    label('loc_296C')

    ChrTalk(
        0x00FE,
        (
            '米丽亚老师\n',
            '才刚上完课\n',
            '就马上回办公室了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_299A(): pass

    label('loc_299A')

    Jump('loc_2A6E')

    def _loc_299D(): pass

    label('loc_299D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_2A6E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2A29',
    )

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '社会系各位的作品\n',
            '都是研究成果发表啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哇……真是厉害啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们系的同学\n',
            '只会办茶座或者\n',
            '鬼怪屋什么的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A6E')

    def _loc_2A29(): pass

    label('loc_2A29')

    ChrTalk(
        0x00FE,
        (
            '社会系各位的作品\n',
            '都是研究成果发表啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哇……真是厉害啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A6E(): pass

    label('loc_2A6E')

    TalkEnd(0x0012)

    Return()

# id: 0x000E offset: 0x2A72
@scena.Code('func_0E_2A72')
def func_0E_2A72():
    TalkBegin(0x0013)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_2AAC',
    )

    ChrTalk(
        0x00FE,
        (
            '欢迎光临。\n',
            '这里是我们的茶座『芳塔娜』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2AEF')

    def _loc_2AAC(): pass

    label('loc_2AAC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_2AEF',
    )

    ChrTalk(
        0x00FE,
        (
            '穿成这个样子\n',
            '虽然有点不好意思，\n',
            '但为了学园祭，忍了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2AEF(): pass

    label('loc_2AEF')

    TalkEnd(0x0013)

    Return()

# id: 0x000F offset: 0x2AF3
@scena.Code('func_0F_2AF3')
def func_0F_2AF3():
    TalkBegin(0x0014)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_2B27',
    )

    ChrTalk(
        0x00FE,
        (
            '唔，\n',
            '今天也是很有意义的一课啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_301C')

    def _loc_2B27(): pass

    label('loc_2B27')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_2C33',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2BE2',
    )

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '虽然办娱乐活动很有意思，\n',
            '不过让大家知道我们\n',
            '平日的研究成果也是很重要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '尤其是有很多前辈\n',
            '和市民们前来参观。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……虽说如此，\n',
            '考试也不会得到更高的分数。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C30')

    def _loc_2BE2(): pass

    label('loc_2BE2')

    ChrTalk(
        0x00FE,
        (
            '虽然办娱乐活动很有意思，\n',
            '不过让大家知道我们\n',
            '平日的研究成果也是很重要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C30(): pass

    label('loc_2C30')

    Jump('loc_301C')

    def _loc_2C33(): pass

    label('loc_2C33')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_2ECF',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x1000)"),
            Expr.Return,
        ),
        'loc_2D1E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2CF9',
    )

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '我们社会系发表了\n',
            '从各种产业的经济指标上\n',
            '进行经济动向的预测的研究。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且也收集了\n',
            '通俗易懂的关于卢安地区\n',
            '历史和发展的资料。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果有兴趣的话就请看一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D1B')

    def _loc_2CF9(): pass

    label('loc_2CF9')

    ChrTalk(
        0x00FE,
        (
            '如果有兴趣的话就请看一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2D1B(): pass

    label('loc_2D1B')

    Jump('loc_2ECC')

    def _loc_2D1E(): pass

    label('loc_2D1E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2E22',
    )

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '我们社会系发表了\n',
            '从各种产业的经济指标上\n',
            '进行经济动向的预测的研究。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且也收集了\n',
            '通俗易懂的关于卢安地区\n',
            '历史和发展的资料。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然有几份资料没到手，\n',
            '但在这么点时间里，\n',
            '能做成这么完善的内容也算不错了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果有兴趣的话就请看一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2ECC')

    def _loc_2E22(): pass

    label('loc_2E22')

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0020)"),
            Expr.Return,
        ),
        'loc_2EAA',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然没赶上这次发表，\n',
            '但是《卢安经济史》是很贵重的资料。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果你们看到那三本书的话，\n',
            '麻烦帮我放回资料室的书架上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2ECC')

    def _loc_2EAA(): pass

    label('loc_2EAA')

    ChrTalk(
        0x00FE,
        (
            '如果有兴趣的话就请看一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2ECC(): pass

    label('loc_2ECC')

    Jump('loc_301C')

    def _loc_2ECF(): pass

    label('loc_2ECF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_2ED9',
    )

    Jump('loc_301C')

    def _loc_2ED9(): pass

    label('loc_2ED9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_301C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2FFE',
    )

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '啊，科洛丝。\n',
            '你终于回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们班级的节目\n',
            '准备工作进展得很顺利啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们舞台剧方面怎么样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听说连主要演员\n',
            '都还没决定下来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F呵呵，罗基克，\n',
            '那件事已经解决了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '舞台剧方面我们不会输的。\n',
            '敬请期待哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哦，是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那我们互相加油吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_301C')

    def _loc_2FFE(): pass

    label('loc_2FFE')

    ChrTalk(
        0x00FE,
        (
            '科洛丝，我们互相加油吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_301C(): pass

    label('loc_301C')

    TalkEnd(0x0014)

    Return()

# id: 0x0010 offset: 0x3020
@scena.Code('func_10_3020')
def func_10_3020():
    TalkBegin(0x0015)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_3079',
    )

    ChrTalk(
        0x00FE,
        (
            '这次的女王诞辰庆典上\n',
            '要召开武术大会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们的击剑部\n',
            '也好想参加啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_32FC')

    def _loc_3079(): pass

    label('loc_3079')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_3138',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_30F5',
    )

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    ChrTalk(
        0x00FE,
        (
            '我太过忙于班里的活动，\n',
            '连社团开的店\n',
            '都没能去帮上忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '等到店员需要换班的时候\n',
            '我再过去看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3135')

    def _loc_30F5(): pass

    label('loc_30F5')

    ChrTalk(
        0x00FE,
        (
            '来这里参观的人\n',
            '真是多啊……\n',
            '还有热心人问了我们很多问题呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3135(): pass

    label('loc_3135')

    Jump('loc_32FC')

    def _loc_3138(): pass

    label('loc_3138')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_3228',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_31CB',
    )

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    ChrTalk(
        0x00FE,
        (
            '我是从卡尔瓦德共和国\n',
            '来这里进修的留学生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次我从研究发表的\n',
            '准备中也学到不少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我认为这是很有意义的一件事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3225')

    def _loc_31CB(): pass

    label('loc_31CB')

    ChrTalk(
        0x00FE,
        (
            '我是从卡尔瓦德共和国\n',
            '来这里进修的留学生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次我从研究发表的\n',
            '准备中也学到不少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3225(): pass

    label('loc_3225')

    Jump('loc_32FC')

    def _loc_3228(): pass

    label('loc_3228')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_32FC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_32A9',
    )

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))
    ChrTurnDirection(0x00FE, 0x0105, 0)

    ChrTalk(
        0x00FE,
        (
            '啊，科洛丝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们班的活动\n',
            '大致都准备好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过罗基克\n',
            '好像还有些不放心，\n',
            '去了资料室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_32FC')

    def _loc_32A9(): pass

    label('loc_32A9')

    ChrTalk(
        0x00FE,
        (
            '我们班的活动\n',
            '大致都准备好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过罗基克\n',
            '好像还有些不放心，\n',
            '去了资料室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_32FC(): pass

    label('loc_32FC')

    TalkEnd(0x0015)

    Return()

# id: 0x0011 offset: 0x3300
@scena.Code('func_11_3300')
def func_11_3300():
    TalkBegin(0x0016)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3357',
    )

    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '罗基克真是个完美主义者啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我觉得这样\n',
            '就已经足够了嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_337C')

    def _loc_3357(): pass

    label('loc_3357')

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '罗基克真是个完美主义者啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_337C(): pass

    label('loc_337C')

    TalkEnd(0x0016)

    Return()

# id: 0x0012 offset: 0x3380
@scena.Code('func_12_3380')
def func_12_3380():
    TalkBegin(0x0017)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_33E4',
    )

    ChrTalk(
        0x00FE,
        (
            '这两个人是青梅竹马，\n',
            '都是住在卢安市里的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈，关系总是那么好，\n',
            '真让人羡慕呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_33E4(): pass

    label('loc_33E4')

    TalkEnd(0x0017)

    Return()

# id: 0x0013 offset: 0x33E8
@scena.Code('func_13_33E8')
def func_13_33E8():
    TalkBegin(0x0018)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_355F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_353E',
    )

    TalkBegin(0x0019)
    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))
    SetScenaFlags(ScenaFlag(0x0002, 0, 0x10))

    ChrTalk(
        0x0018,
        (
            '……喂，妮吉塔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0019, 0x0018, 500)
    OP_62(0x0019, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0018,
        (
            '这样应该就可以了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '明天早上收尾，\n',
            '叫大家一起来帮忙吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '你怎么老是\n',
            '说那么天真的话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '其他同学\n',
            '还有他们要办的事情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '再说一般早上起来都会很忙，\n',
            '都不知道有没有空来帮忙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '哦，是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '好饿啊，肚子好饿啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0019, 0x0010)
    ChrClearFlags(0x0018, 0x0010)
    TalkEnd(0x0019)

    Jump('loc_355F')

    def _loc_353E(): pass

    label('loc_353E')

    ChrTalk(
        0x00FE,
        (
            '啊……\n',
            '好饿啊，肚子好饿啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_355F(): pass

    label('loc_355F')

    TalkEnd(0x0018)

    Return()

# id: 0x0014 offset: 0x3563
@scena.Code('func_14_3563')
def func_14_3563():
    TalkBegin(0x0019)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_36DF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_36BA',
    )

    TalkBegin(0x0018)
    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))
    SetScenaFlags(ScenaFlag(0x0002, 0, 0x10))

    ChrTalk(
        0x0018,
        (
            '喂，妮吉塔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0019, 0x0018, 500)
    OP_62(0x0019, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0018,
        (
            '这样应该就可以了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '明天早上收尾，\n',
            '叫大家一起来帮忙吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '你怎么老是\n',
            '说那么天真的话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '其他同学\n',
            '还有他们要办的事情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '再说一般早上起来\n',
            '大家都会很忙，\n',
            '都不知道有没有空来帮忙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '哦，是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '好饿啊，肚子好饿啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0019, 0x0010)
    ChrClearFlags(0x0018, 0x0010)
    TalkEnd(0x0018)

    Jump('loc_36DF')

    def _loc_36BA(): pass

    label('loc_36BA')

    ChrTalk(
        0x00FE,
        (
            '怎么办，\n',
            '这样下去会来不及的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_36DF(): pass

    label('loc_36DF')

    TalkEnd(0x0019)

    Return()

# id: 0x0015 offset: 0x36E3
@scena.Code('func_15_36E3')
def func_15_36E3():
    FormationAddMember(0x3A, 0xFF)
    EventBegin(0x00)
    MapClearFlags(0x00000001)
    CameraMove(116200, 0, 4240, 0)
    ChrSetPos(0x0101, 116870, 0, -3740, 0)
    ChrSetPos(0x0105, 116870, 0, -3740, 0)
    ChrSetRGBAMask(0x0101, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0105, 255, 255, 255, 0, 0)
    ChrClearFlags(0x0101, 0x0080)
    ChrClearFlags(0x0105, 0x0080)
    OP_4A(0x0008, 255)
    ChrSetPos(0x013B, 115990, 0, 2740, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x013B,
        (
            '#0510051433V#643F#4P原来如此……\n',
            '这主意的确一举两得！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051434V#641F不愧是校长，太英明了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0530051435V#781F哈哈哈……\n',
            '拍我马屁也不会给你奖励哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530051436V#780F这样的话，\n',
            '名单就交给你负责行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x013B,
        (
            '#0510051437V#644F#4P没问题，包在我身上！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(113, 0x00, 0x64)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010051438V#1P打扰了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(6, 0x00, 0x64)
    Sleep(500)

    @scena.Lambda('lambda_389D')
    def lambda_389D():
        CameraMove(117520, 0, 2870, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_389D)

    @scena.Lambda('lambda_38B5')
    def lambda_38B5():
        ChrWalkTo(0x00FE, 117490, 0, 1460, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_38B5)

    @scena.Lambda('lambda_38D0')
    def lambda_38D0():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_38D0)

    Sleep(700)

    @scena.Lambda('lambda_38E7')
    def lambda_38E7():
        ChrWalkTo(0x00FE, 116570, 0, 460, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_38E7)

    @scena.Lambda('lambda_3902')
    def lambda_3902():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0105, 0x0003, lambda_3902)

    ChrSetDirection(0x013B, 180, 400)
    WaitForThreadExit(0x0101, 0x0001)
    ChrSetDirection(0x0101, 315, 0)
    WaitForThreadExit(0x0105, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0105,
        (
            '#0060051439V#044F啊，对不起……\n',
            '没有打扰你们谈话吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0530051440V#781F不不。\n',
            '刚好谈完了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530051441V其实是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x013B, 0x0008, 400)

    ChrTalk(
        0x013B,
        (
            '#0510051442V#646F哎呀，校长！\n',
            '别这么快说出来啦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051443V让大家知道的话，\n',
            '明天就没有什么惊喜了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x013B, 400)

    ChrTalk(
        0x0101,
        (
            '#0010051444V#008F#2P是、是什么？\n',
            '好像神神秘秘的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051445V#045F乔儿真是的……\n',
            '又在打什么鬼主意了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x013B, 0x0105, 400)

    ChrTalk(
        0x013B,
        (
            '#0510051446V#649F呵、呵、呵……\n',
            '这就等着明天揭晓吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051447V#640F倒是你们来做什么？\n',
            '找我有事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051448V#040F嗯，其实是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '科洛丝告诉乔儿等会大家在食堂共进晚餐，\n',
            '同时预祝明天学园祭成功的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x013B,
        (
            '#0510051449V#640F啊，不错啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051450V#641F那么，为了预祝明天学园祭的成功，\n',
            '我们今晚就好好热闹一下吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051451V痛痛快快玩一场，痛痛快快地！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0530051452V#780F呵呵，可别玩得太过火，\n',
            '影响到明天的活动就不好了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051453V#040F是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051454V#501F#2P那么，乔儿。\n',
            '一起去食堂吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x013B,
        (
            '#0510051455V#644F嗯，走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0089, 0, 0x448))
    EventEnd(0x00)
    OP_4B(0x0008, 255)

    Return()

# id: 0x0016 offset: 0x3CE7
@scena.Code('func_16_3CE7')
def func_16_3CE7():
    PlaySE(17, 0x00, 0x64)
    ChrSetFlags(0x001B, 0x0080)
    OP_64(0x00, 0x0001)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '卢安经济史·中',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(0x033E, 1)
    OP_28(0x0027, 0x01, 0x0080)
    TalkEnd(0x00FF)

    Return()

# id: 0x0017 offset: 0x3D4D
@scena.Code('func_17_3D4D')
def func_17_3D4D():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　　　前面是校长室和办公室　　　　\n',
            '※谢绝外来人员进入。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0018 offset: 0x3DB7
@scena.Code('func_18_3DB7')
def func_18_3DB7():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '人文系模拟店铺\n',
            '茶座『芳塔娜』',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0019 offset: 0x3E07
@scena.Code('func_19_3E07')
def func_19_3E07():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　　走　\n',
            '　　廊　\n',
            '　　里　\n',
            '　　请　\n',
            '　　保　\n',
            '　学持　\n',
            '　生安　\n',
            '　指静　\n',
            '　导！　\n',
            '　部　　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x001A offset: 0x3E93
@scena.Code('func_1A_3E93')
def func_1A_3E93():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '自然系成果展示\n',
            '『结晶回路与导力技术』',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x001B offset: 0x3EEB
@scena.Code('func_1B_3EEB')
def func_1B_3EEB():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　　社会系成果展示\n',
            '『卢安地区的历史与经济』',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x001C offset: 0x3F49
@scena.Code('func_1C_3F49')
def func_1C_3F49():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '欢迎光临！\n',
            '这里是茶座『芳塔娜』！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x001D offset: 0x3F9D
@scena.Code('func_1D_3F9D')
def func_1D_3F9D():
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '这里分析了导力器产业的发展动向。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

# id: 0x001E offset: 0x3FF0
@scena.Code('func_1E_3FF0')
def func_1E_3FF0():
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '这里用图表展示了每年观光客数量的变化。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

# id: 0x001F offset: 0x4049
@scena.Code('func_1F_4049')
def func_1F_4049():
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '这里整理了国内主要产品的出口方向。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

# id: 0x0020 offset: 0x409E
@scena.Code('func_20_409E')
def func_20_409E():
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '这里归纳了人口移动的情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

# id: 0x0021 offset: 0x40EB
@scena.Code('func_21_40EB')
def func_21_40EB():
    OP_13(0x006F)

    Return()

# id: 0x0022 offset: 0x40EF
@scena.Code('func_22_40EF')
def func_22_40EF():
    OP_13(0x005E)

    Return()

# id: 0x0023 offset: 0x40F3
@scena.Code('func_23_40F3')
def func_23_40F3():
    OP_13(0x006E)

    Return()

# id: 0x0024 offset: 0x40F7
@scena.Code('func_24_40F7')
def func_24_40F7():
    OP_13(0x0074)

    Return()

# id: 0x0025 offset: 0x40FB
@scena.Code('func_25_40FB')
def func_25_40FB():
    OP_13(0x0073)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

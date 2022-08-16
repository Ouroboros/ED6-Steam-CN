import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5400_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5400   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5400.x'
    header.mapIndex       = 1
    header.bgm            = 28
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
        ('ED6_DT07/CH00010._CH', 'ED6_DT07/CH00010P._CP'),
        ('ED6_DT27/CH03001._CH', 'ED6_DT27/CH03001P._CP'),
        ('ED6_DT26/CH20380._CH', 'ED6_DT26/CH20380P._CP'),
        ('ED6_DT27/CH03005._CH', 'ED6_DT27/CH03005P._CP'),
        ('ED6_DT26/CH20235._CH', 'ED6_DT26/CH20235P._CP'),
        ('ED6_DT26/CH20376._CH', 'ED6_DT26/CH20376P._CP'),
        ('ED6_DT27/CH03510._CH', 'ED6_DT27/CH03510P._CP'),
        ('ED6_DT27/CH03000._CH', 'ED6_DT27/CH03000P._CP'),
        ('ED6_DT27/CH04620._CH', 'ED6_DT27/CH04620P._CP'),
        ('ED6_DT27/CH03003._CH', 'ED6_DT27/CH03003P._CP'),
        ('ED6_DT07/CH02040._CH', 'ED6_DT07/CH02040P._CP'),
        ('ED6_DT27/CH04621._CH', 'ED6_DT27/CH04621P._CP'),
        ('ED6_DT27/CH04622._CH', 'ED6_DT27/CH04622P._CP'),
        ('ED6_DT27/CH04623._CH', 'ED6_DT27/CH04623P._CP'),
        ('ED6_DT26/CH20384._CH', 'ED6_DT26/CH20384P._CP'),
        ('ED6_DT27/CH04624._CH', 'ED6_DT27/CH04624P._CP'),
        ('ED6_DT26/CH20237._CH', 'ED6_DT26/CH20237P._CP'),
        ('ED6_DT27/CH04001._CH', 'ED6_DT27/CH04001P._CP'),
        ('ED6_DT26/CH20501._CH', 'ED6_DT26/CH20501P._CP'),
        ('ED6_DT27/CH04002._CH', 'ED6_DT27/CH04002P._CP'),
        ('ED6_DT26/CH20381._CH', 'ED6_DT26/CH20381P._CP'),
        ('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT07/CH00343._CH', 'ED6_DT07/CH00343P._CP'),
        ('ED6_DT07/CH00341._CH', 'ED6_DT07/CH00341P._CP'),
        ('ED6_DT07/CH00344._CH', 'ED6_DT07/CH00344P._CP'),
        ('ED6_DT29/CH12570._CH', 'ED6_DT29/CH12570P._CP'),
        ('ED6_DT29/CH12571._CH', 'ED6_DT29/CH12571P._CP'),
        ('ED6_DT29/CH12350._CH', 'ED6_DT29/CH12350P._CP'),
        ('ED6_DT29/CH12351._CH', 'ED6_DT29/CH12351P._CP'),
        ('ED6_DT07/CH02110._CH', 'ED6_DT07/CH02110P._CP'),
        ('ED6_DT07/CH02120._CH', 'ED6_DT07/CH02120P._CP'),
        ('ED6_DT07/CH01380._CH', 'ED6_DT07/CH01380P._CP'),
        ('ED6_DT26/CH20208._CH', 'ED6_DT26/CH20208P._CP'),
    ]

# id: 0x10001 offset: 0x1B2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '约修亚',
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
            name                = '约修亚',
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
            name                = '约修亚',
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
            name                = '歼灭天使玲',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '强化猎兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 32,
            chipIndex           = 32,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '强化猎兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 32,
            chipIndex           = 32,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '剑帝莱维',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '多伦',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 29,
            chipIndex           = 29,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '吉尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 30,
            chipIndex           = 30,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '空贼雷古',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 31,
            chipIndex           = 31,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '空贼阿伦',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 31,
            chipIndex           = 31,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '空贼莱尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 31,
            chipIndex           = 31,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '空贼罗尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 31,
            chipIndex           = 31,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '空贼',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 31,
            chipIndex           = 31,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '空贼',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 31,
            chipIndex           = 31,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x392
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '哨兵570（蓝）',
            x           = -134110,
            z           = 0,
            y           = 45880,
            word_0C     = 0x0000,
            word_0E     = 0x0019,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0424,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '哨兵235（红）',
            x           = -135340,
            z           = 0,
            y           = -27900,
            word_0C     = 0x0000,
            word_0E     = 0x001B,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0427,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x3CA
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 2850,
            y           = 0,
            z           = 22850,
            range       = 5160,
            dword_10    = 0x000007D0,
            dword_14    = 0x00006112,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000F,
        ),
        ScenaEventData(
            x           = -52950,
            y           = 0,
            z           = -61000,
            range       = -51020,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFF1730,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000010,
        ),
        ScenaEventData(
            x           = -42980,
            y           = -1000,
            z           = 75190,
            range       = 3000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000037,
        ),
        ScenaEventData(
            x           = -36920,
            y           = -1000,
            z           = -67150,
            range       = 3000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000038,
        ),
        ScenaEventData(
            x           = 70070,
            y           = -1000,
            z           = -234030,
            range       = 3000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000039,
        ),
        ScenaEventData(
            x           = -90500,
            y           = 0,
            z           = -343710,
            range       = -85100,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFAC61C,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000001F,
        ),
    )

# id: 0x10004 offset: 0x48A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -131900,
            triggerZ            = 0,
            triggerY            = 10590,
            triggerRange        = 1000,
            actorX              = -131900,
            actorZ              = 0,
            actorY              = 11210,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -87000,
            triggerZ            = 0,
            triggerY            = -342900,
            triggerRange        = 1000,
            actorX              = -87000,
            actorZ              = 1000,
            actorY              = -343080,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0024,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -127350,
            triggerZ            = 0,
            triggerY            = -58920,
            triggerRange        = 1000,
            actorX              = -126610,
            actorZ              = 0,
            actorY              = -58850,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0025,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -37010,
            triggerZ            = 0,
            triggerY            = -67050,
            triggerRange        = 1000,
            actorX              = -37010,
            actorZ              = 1200,
            actorY              = -67050,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x002B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 61080,
            triggerZ            = 0,
            triggerY            = -184550,
            triggerRange        = 1000,
            actorX              = 61080,
            actorZ              = 1000,
            actorY              = -184550,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0012,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 61000,
            triggerZ            = 0,
            triggerY            = -27060,
            triggerRange        = 1000,
            actorX              = 61000,
            actorZ              = 1000,
            actorY              = -27060,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 52900,
            triggerZ            = 0,
            triggerY            = -53160,
            triggerRange        = 1000,
            actorX              = 52880,
            actorZ              = 1000,
            actorY              = -52540,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -79360,
            triggerZ            = 0,
            triggerY            = -318070,
            triggerRange        = 1000,
            actorX              = -78700,
            actorZ              = 0,
            actorY              = -318100,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -79400,
            triggerZ            = 0,
            triggerY            = -298090,
            triggerRange        = 1000,
            actorX              = -78740,
            actorZ              = 0,
            actorY              = -298130,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -37430,
            triggerZ            = 0,
            triggerY            = 73910,
            triggerRange        = 1000,
            actorX              = -37430,
            actorZ              = 1000,
            actorY              = 73910,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x003C,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -38100,
            triggerZ            = 0,
            triggerY            = -71790,
            triggerRange        = 1000,
            actorX              = -38100,
            actorZ              = 1000,
            actorY              = -71790,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x003D,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -83920,
            triggerZ            = 0,
            triggerY            = -346980,
            triggerRange        = 1000,
            actorX              = -83920,
            actorZ              = 1000,
            actorY              = -346980,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x003E,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x63A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_654',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_0D_152E)

    Jump('loc_6E6')

    def _loc_654(): pass

    label('loc_654')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_665',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    Event(0, func_0E_2290)

    Jump('loc_6E6')

    def _loc_665(): pass

    label('loc_665')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Return,
        ),
        'loc_67F',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x53),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    Event(0, func_14_321E)

    Jump('loc_6E6')

    def _loc_67F(): pass

    label('loc_67F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 3, 0x10F3)),
            Expr.Return,
        ),
        'loc_699',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x72),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    Event(0, func_16_5A6A)

    Jump('loc_6E6')

    def _loc_699(): pass

    label('loc_699')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 4, 0x10F4)),
            Expr.Return,
        ),
        'loc_6AA',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    Event(0, func_11_2C47)

    Jump('loc_6E6')

    def _loc_6AA(): pass

    label('loc_6AA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 5, 0x10F5)),
            Expr.Return,
        ),
        'loc_6C4',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x1C),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 5, 0x10F5))
    Event(0, func_17_61B7)

    Jump('loc_6E6')

    def _loc_6C4(): pass

    label('loc_6C4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0444, 4, 0x2224)),
            (Expr.TestScenaFlags, ScenaFlag(0x0456, 2, 0x22B2)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x7F),
            Expr.Equ,
            Expr.Nez64,
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6E6',
    )

    Event(0, func_26_95E6)

    def _loc_6E6(): pass

    label('loc_6E6')

    Return()

# id: 0x0001 offset: 0x6E7
@scena.Code('func_01_6E7')
def func_01_6E7():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_705',
    )

    ExecExpressionWithVar(
        0x3B,
        (
            (Expr.PushLong, 0x227),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x3C,
        (
            (Expr.PushLong, 0x10A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_705(): pass

    label('loc_705')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A6, 0, 0x1D30)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_717',
    )

    OP_6F(0x0025, 0)

    Jump('loc_71E')

    def _loc_717(): pass

    label('loc_717')

    OP_6F(0x0025, 60)

    def _loc_71E(): pass

    label('loc_71E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A6, 1, 0x1D31)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_730',
    )

    OP_6F(0x0026, 0)

    Jump('loc_737')

    def _loc_730(): pass

    label('loc_730')

    OP_6F(0x0026, 60)

    def _loc_737(): pass

    label('loc_737')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A7, 3, 0x1D3B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_749',
    )

    OP_6F(0x002B, 0)

    Jump('loc_750')

    def _loc_749(): pass

    label('loc_749')

    OP_6F(0x002B, 60)

    def _loc_750(): pass

    label('loc_750')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A7, 4, 0x1D3C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_762',
    )

    OP_6F(0x002C, 0)

    Jump('loc_769')

    def _loc_762(): pass

    label('loc_762')

    OP_6F(0x002C, 60)

    def _loc_769(): pass

    label('loc_769')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_783',
    )

    OP_64(0x02, 0x0001)
    OP_71(0x0025, 0x0000)
    OP_71(0x0025, 0x0004)

    def _loc_783(): pass

    label('loc_783')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A9, 2, 0x1D4A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_795',
    )

    OP_6F(0x002D, 0)

    Jump('loc_79C')

    def _loc_795(): pass

    label('loc_795')

    OP_6F(0x002D, 60)

    def _loc_79C(): pass

    label('loc_79C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A9, 3, 0x1D4B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7AE',
    )

    OP_6F(0x002E, 0)

    Jump('loc_7B5')

    def _loc_7AE(): pass

    label('loc_7AE')

    OP_6F(0x002E, 60)

    def _loc_7B5(): pass

    label('loc_7B5')

    OP_64(0x01, 0x0001)
    OP_64(0x02, 0x0001)
    OP_64(0x03, 0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0383, 3, 0x1C1B)),
            (Expr.TestScenaFlags, ScenaFlag(0x0383, 4, 0x1C1C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7E1',
    )

    ChrSetChipByIndex(0x0101, 6)
    ChrSetChipByIndex(0x012F, 7)
    ChrSetFlags(0x0101, 0x1000)
    ChrSetFlags(0x012F, 0x1000)

    def _loc_7E1(): pass

    label('loc_7E1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0383, 4, 0x1C1C)),
            (Expr.TestScenaFlags, ScenaFlag(0x0383, 5, 0x1C1D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_80F',
    )

    ChrSetPos(0x000B, 70380, 0, -234050, 270)
    ChrClearFlags(0x000B, 0x0080)
    CreateThread(0x000B, 0x00, 0x00, func_02_9CA)
    OP_72(0x001A, 0x0010)

    def _loc_80F(): pass

    label('loc_80F')

    Call(0, 0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0383, 5, 0x1C1D)),
            Expr.Return,
        ),
        'loc_823',
    )

    OP_65(0x03, 0x0001)
    OP_72(0x0017, 0x0010)

    def _loc_823(): pass

    label('loc_823')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0444, 2, 0x2222)),
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_931',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0444, 3, 0x2223)),
            Expr.Return,
        ),
        'loc_85B',
    )

    ChrSetPos(0x000F, -84180, 0, -335080, 270)
    ChrSetPos(0x0010, -84470, 0, -336340, 270)

    Jump('loc_87D')

    def _loc_85B(): pass

    label('loc_85B')

    ChrSetPos(0x000F, -81860, 0, -334130, 180)
    ChrSetPos(0x0010, -81190, 0, -335370, 0)

    def _loc_87D(): pass

    label('loc_87D')

    ChrSetPos(0x0011, -82890, 0, -331950, 45)
    ChrSetPos(0x0014, -81710, 0, -332430, 270)
    ChrSetPos(0x0015, -81980, 0, -331150, 180)
    ChrSetPos(0x0013, -81220, 0, -336530, 225)
    ChrSetPos(0x0012, -81780, 0, -338160, 0)
    ChrSetPos(0x0016, -82670, 0, -337380, 90)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    OP_65(0x01, 0x0001)
    OP_65(0x03, 0x0001)
    OP_72(0x0017, 0x0010)
    OP_72(0x0003, 0x0010)
    OP_72(0x0004, 0x0010)
    OP_72(0x0005, 0x0010)
    OP_72(0x0006, 0x0010)
    OP_72(0x0007, 0x0010)

    def _loc_931(): pass

    label('loc_931')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0444, 3, 0x2223)),
            Expr.Return,
        ),
        'loc_951',
    )

    OP_65(0x02, 0x0001)
    OP_6F(0x0025, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0444, 5, 0x2225)),
            Expr.Return,
        ),
        'loc_951',
    )

    OP_6F(0x0025, 60)

    def _loc_951(): pass

    label('loc_951')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Return,
        ),
        'loc_969',
    )

    OP_6F(0x0003, 50)
    OP_71(0x0023, 0x0004)
    OP_72(0x0024, 0x0004)

    def _loc_969(): pass

    label('loc_969')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 0, 0x2228)),
            Expr.Return,
        ),
        'loc_981',
    )

    OP_6F(0x0004, 50)
    OP_71(0x0023, 0x0004)
    OP_72(0x0024, 0x0004)

    def _loc_981(): pass

    label('loc_981')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 1, 0x2229)),
            Expr.Return,
        ),
        'loc_999',
    )

    OP_6F(0x0005, 50)
    OP_71(0x0023, 0x0004)
    OP_72(0x0024, 0x0004)

    def _loc_999(): pass

    label('loc_999')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 2, 0x222A)),
            Expr.Return,
        ),
        'loc_9B1',
    )

    OP_6F(0x0006, 50)
    OP_71(0x0023, 0x0004)
    OP_72(0x0024, 0x0004)

    def _loc_9B1(): pass

    label('loc_9B1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 3, 0x222B)),
            Expr.Return,
        ),
        'loc_9C9',
    )

    OP_6F(0x0007, 50)
    OP_71(0x0023, 0x0004)
    OP_72(0x0024, 0x0004)

    def _loc_9C9(): pass

    label('loc_9C9')

    Return()

# id: 0x0002 offset: 0x9CA
@scena.Code('func_02_9CA')
def func_02_9CA():
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
        'loc_9EF',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_B31')

    def _loc_9EF(): pass

    label('loc_9EF')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A08',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_B31')

    def _loc_A08(): pass

    label('loc_A08')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A21',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_B31')

    def _loc_A21(): pass

    label('loc_A21')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A3A',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_B31')

    def _loc_A3A(): pass

    label('loc_A3A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A53',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_B31')

    def _loc_A53(): pass

    label('loc_A53')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A6C',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_B31')

    def _loc_A6C(): pass

    label('loc_A6C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A85',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_B31')

    def _loc_A85(): pass

    label('loc_A85')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A9E',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_B31')

    def _loc_A9E(): pass

    label('loc_A9E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AB7',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_B31')

    def _loc_AB7(): pass

    label('loc_AB7')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AD0',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_B31')

    def _loc_AD0(): pass

    label('loc_AD0')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AE9',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_B31')

    def _loc_AE9(): pass

    label('loc_AE9')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B02',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_B31')

    def _loc_B02(): pass

    label('loc_B02')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B1B',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_B31')

    def _loc_B1B(): pass

    label('loc_B1B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B31',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_B31(): pass

    label('loc_B31')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_B46',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_B31')

    def _loc_B46(): pass

    label('loc_B46')

    Return()

# id: 0x0003 offset: 0xB47
@scena.Code('func_03_B47')
def func_03_B47():
    Call(0, 0x0013)

    Return()

# id: 0x0004 offset: 0xB4C
@scena.Code('func_04_B4C')
def func_04_B4C():
    TalkBegin(0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0444, 5, 0x2225)),
            Expr.Return,
        ),
        'loc_BAE',
    )

    ChrTalk(
        0x000F,
        (
            '#0300400493V#490F哦哦，找到卡了吗！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300400494V#191F那就好办了！\n',
            '赶快逃跑吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C17')

    def _loc_BAE(): pass

    label('loc_BAE')

    ChrTalk(
        0x000F,
        (
            '#0300400495V#197F前方区域的第二层……\n',
            '地方太大都不知道在哪里了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300400496V#199F总之小心前往吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C17(): pass

    label('loc_C17')

    TalkEnd(0x000F)

    Return()

# id: 0x0005 offset: 0xC1B
@scena.Code('func_05_C1B')
def func_05_C1B():
    TalkBegin(0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0444, 5, 0x2225)),
            Expr.Return,
        ),
        'loc_C86',
    )

    ChrTalk(
        0x0010,
        (
            '#0290400497V#204F……看来似乎\n',
            '平安返回了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290400498V#200F没时间了。\n',
            '赶快逃出去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CE3')

    def _loc_C86(): pass

    label('loc_C86')

    ChrTalk(
        0x0010,
        (
            '#0290400499V#204F……刚才有红衣士兵\n',
            '到这里来巡逻过。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290400500V#206F小心别被发现哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CE3(): pass

    label('loc_CE3')

    TalkEnd(0x0010)

    Return()

# id: 0x0006 offset: 0xCE7
@scena.Code('func_06_CE7')
def func_06_CE7():
    UnlockAchievement(0x02, 0x0153, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A6, 0, 0x1D30)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DC4',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0025, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['死之刃２'], 1)"),
            Expr.Return,
        ),
        'loc_D5B',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['死之刃２']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03A6, 0, 0x1D30))

    Jump('loc_DC1')

    def _loc_D5B(): pass

    label('loc_D5B')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['死之刃２']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['死之刃２']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0025, 60)
    OP_70(0x0025, 0)

    def _loc_DC1(): pass

    label('loc_DC1')

    Jump('loc_DF5')

    def _loc_DC4(): pass

    label('loc_DC4')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_DF5(): pass

    label('loc_DF5')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0xE03
@scena.Code('func_07_E03')
def func_07_E03():
    UnlockAchievement(0x02, 0x0154, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A6, 1, 0x1D31)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_EE0',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0026, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['大回复药'], 1)"),
            Expr.Return,
        ),
        'loc_E77',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['大回复药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03A6, 1, 0x1D31))

    Jump('loc_EDD')

    def _loc_E77(): pass

    label('loc_E77')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['大回复药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['大回复药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0026, 60)
    OP_70(0x0026, 0)

    def _loc_EDD(): pass

    label('loc_EDD')

    Jump('loc_F11')

    def _loc_EE0(): pass

    label('loc_EE0')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_F11(): pass

    label('loc_F11')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0xF1F
@scena.Code('func_08_F1F')
def func_08_F1F():
    UnlockAchievement(0x02, 0x0155, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A7, 3, 0x1D3B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_FFC',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x002B, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['昏厥肉丸子'], 1)"),
            Expr.Return,
        ),
        'loc_F93',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['昏厥肉丸子']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03A7, 3, 0x1D3B))

    Jump('loc_FF9')

    def _loc_F93(): pass

    label('loc_F93')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['昏厥肉丸子']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['昏厥肉丸子']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x002B, 60)
    OP_70(0x002B, 0)

    def _loc_FF9(): pass

    label('loc_FF9')

    Jump('loc_102D')

    def _loc_FFC(): pass

    label('loc_FFC')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_102D(): pass

    label('loc_102D')

    Sleep(30)

    If(
        (
            (Expr.Eval, "OP_40(0x020D, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1085',
    )

    If(
        (
            (Expr.Eval, "OP_AC(0x0044)"),
            Expr.Return,
        ),
        'loc_104C',
    )

    Jump('loc_1085')

    def _loc_104C(): pass

    label('loc_104C')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['昏厥肉丸子']),
            (TxtCtl.SetColor, 0x0),
            '的食谱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.Item, ItemTable['昏厥肉丸子']),
            (TxtCtl.SetColor, 0x0),
            '的做法已经学会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1085(): pass

    label('loc_1085')

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0009 offset: 0x108E
@scena.Code('func_09_108E')
def func_09_108E():
    UnlockAchievement(0x02, 0x0156, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A7, 4, 0x1D3C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_116B',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x002C, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅱ'], 1)"),
            Expr.Return,
        ),
        'loc_1102',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅱ']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03A7, 4, 0x1D3C))

    Jump('loc_1168')

    def _loc_1102(): pass

    label('loc_1102')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅱ']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅱ']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x002C, 60)
    OP_70(0x002C, 0)

    def _loc_1168(): pass

    label('loc_1168')

    Jump('loc_119C')

    def _loc_116B(): pass

    label('loc_116B')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_119C(): pass

    label('loc_119C')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x000A offset: 0x11AA
@scena.Code('func_0A_11AA')
def func_0A_11AA():
    UnlockAchievement(0x02, 0x0157, 0x00)
    MapSetFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A9, 2, 0x1D4A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_12D6',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x002D, 30)
    OP_73(0x002D)
    OP_6F(0x002D, 30)
    AddSepith(0x00, 300)
    AddSepith(0x01, 300)
    AddSepith(0x02, 300)
    AddSepith(0x03, 300)
    AddSepith(0x04, 300)
    AddSepith(0x05, 300)
    AddSepith(0x06, 300)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#56I地之耀晶片×３００\n',
            (TxtCtl.SetColor, 0x2),
            '#57I水之耀晶片×３００\n',
            (TxtCtl.SetColor, 0x2),
            '#58I火之耀晶片×３００\n',
            (TxtCtl.SetColor, 0x2),
            '#59I风之耀晶片×３００\n',
            (TxtCtl.SetColor, 0x2),
            '#62I时之耀晶片×３００\n',
            (TxtCtl.SetColor, 0x2),
            '#60I空之耀晶片×３００\n',
            (TxtCtl.SetColor, 0x2),
            '#61I幻之耀晶片×３００\n',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    SetScenaFlags(ScenaFlag(0x03A9, 2, 0x1D4A))

    Jump('loc_12F0')

    def _loc_12D6(): pass

    label('loc_12D6')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_12F0(): pass

    label('loc_12F0')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x000B offset: 0x1302
@scena.Code('func_0B_1302')
def func_0B_1302():
    UnlockAchievement(0x02, 0x0158, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A9, 3, 0x1D4B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_13DF',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x002E, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['机械靴'], 1)"),
            Expr.Return,
        ),
        'loc_1376',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['机械靴']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03A9, 3, 0x1D4B))

    Jump('loc_13DC')

    def _loc_1376(): pass

    label('loc_1376')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['机械靴']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['机械靴']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x002E, 60)
    OP_70(0x002E, 0)

    def _loc_13DC(): pass

    label('loc_13DC')

    Jump('loc_1410')

    def _loc_13DF(): pass

    label('loc_13DF')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_1410(): pass

    label('loc_1410')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x000C offset: 0x141E
@scena.Code('func_0C_141E')
def func_0C_141E():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1437',
    )

    OP_71(0x0001, 0x0004)
    OP_72(0x0000, 0x0004)

    Jump('loc_152D')

    def _loc_1437(): pass

    label('loc_1437')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0383, 5, 0x1C1D)),
            Expr.Return,
        ),
        'loc_14A6',
    )

    OP_64(0x04, 0x0001)
    ChrSetPos(0x000C, 54170, 0, 12070, 270)
    ChrSetPos(0x000D, 60700, 0, 7800, 270)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetFlags(0x000C, 0x0002)
    ChrSetFlags(0x000D, 0x0002)
    ChrSetChipByIndex(0x000C, 18)
    ChrSetChipByIndex(0x000D, 18)
    ChrSetSubChip(0x000C, 15)
    ChrSetSubChip(0x000D, 15)

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x6F),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_14A0',
    )

    PlaySE(451, 0x00, 0x64)

    Jump('loc_14A3')

    def _loc_14A0(): pass

    label('loc_14A0')

    OP_23(0x01C3)

    def _loc_14A3(): pass

    label('loc_14A3')

    Jump('loc_152D')

    def _loc_14A6(): pass

    label('loc_14A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0392, 3, 0x1C93)),
            Expr.Return,
        ),
        'loc_14BA',
    )

    OP_71(0x0001, 0x0004)
    OP_72(0x0000, 0x0004)

    Jump('loc_152D')

    def _loc_14BA(): pass

    label('loc_14BA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0391, 1, 0x1C89)),
            Expr.Return,
        ),
        'loc_14F2',
    )

    OP_64(0x04, 0x0001)
    OP_72(0x0002, 0x0020)
    OP_72(0x0002, 0x0010)
    OP_6F(0x0002, 270)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x48),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_1F(0x64, 0x00000000)
    OP_71(0x0001, 0x0004)
    OP_72(0x0000, 0x0004)

    Jump('loc_152D')

    def _loc_14F2(): pass

    label('loc_14F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0383, 4, 0x1C1C)),
            Expr.Return,
        ),
        'loc_1517',
    )

    OP_72(0x0002, 0x0020)
    OP_72(0x0002, 0x0010)
    OP_6F(0x0002, 0)
    OP_71(0x0001, 0x0004)
    OP_72(0x0000, 0x0004)

    Jump('loc_152D')

    def _loc_1517(): pass

    label('loc_1517')

    OP_72(0x0002, 0x0010)
    OP_6F(0x0002, 0)
    OP_71(0x0001, 0x0004)
    OP_72(0x0000, 0x0004)

    def _loc_152D(): pass

    label('loc_152D')

    Return()

# id: 0x000D offset: 0x152E
@scena.Code('func_0D_152E')
def func_0D_152E():
    EventBegin(0x00)
    OP_20(0x00000000)
    FadeOut(0, 0, -1)
    OP_0D()
    OP_D6(0x01)
    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    ChrSetStatus(0x00FF, 0xFE, 0)
    ChrSetPos(0x0101, 78890, 0, 5300, 270)
    ChrSetPos(0x0008, 84600, 0, 5600, 270)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    CameraMove(79330, 0, 5940, 0)
    OP_67(0, 8500, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(3000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            (TxtCtl.SetColor, 0x0),
            '#0010330001V#1003F#5P……这里……是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    SetMessageWindowPos(400, 50, -1, -1)
    TalkSetChrName('声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0020330002V#40W………艾丝蒂尔…………',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    PlayBGM(91)
    Sleep(500)

    @scena.Lambda('lambda_1678')
    def lambda_1678():
        CameraMove(82590, 0, 6280, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1678)

    @scena.Lambda('lambda_1690')
    def lambda_1690():
        OP_67(0, 6500, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1690)

    @scena.Lambda('lambda_16A8')
    def lambda_16A8():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_16A8)

    ChrTurnDirection(0x0101, 0x0008, 400)
    WaitForThreadExit(0x0008, 0x0000)
    WaitForThreadExit(0x0008, 0x0002)

    ChrTalk(
        0x0101,
        (
            (TxtCtl.SetColor, 0x0),
            '#0010330003V#1020F#6P约修亚！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_16F2')
    def lambda_16F2():
        OP_99(0x0101, 0x00, 0x07, 1000)
        Yield()

        Jump('lambda_16F2')

    DispatchAsync2(0x0101, 0x0001, lambda_16F2)

    Sleep(1500)

    ChrSetChipByIndex(0x0101, 1)

    @scena.Lambda('lambda_170F')
    def lambda_170F():
        OP_99(0x0101, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_170F')

    DispatchAsync2(0x0101, 0x0001, lambda_170F)

    Sleep(1500)

    OP_62(0x0101, 0x00000064, 1900, 0x28, 0x2B, 0x000000FA, 0x00)

    @scena.Lambda('lambda_1739')
    def lambda_1739():
        OP_99(0x0101, 0x00, 0x07, 2000)
        Yield()

        Jump('lambda_1739')

    DispatchAsync2(0x0101, 0x0001, lambda_1739)

    Sleep(3000)

    ChrTalk(
        0x0101,
        (
            (TxtCtl.SetColor, 0x0),
            '#0010330004V#1021F#6P为……为什么……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            (TxtCtl.SetColor, 0x5),
            '#0020330005V#2P#40W够了……\n',
            '……已经够了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrSetFlags(0x0008, 0x0002)
    ChrSetChipByIndex(0x0008, 2)
    ChrSetSubChip(0x0008, 0)
    Sleep(500)

    OP_99(0x0008, 0x00, 0x09, 1500)
    PlaySE(130, 0x00, 0x64)
    OP_99(0x0008, 0x0A, 0x0B, 1500)
    Sleep(500)

    TerminateThread(0x0101, 0x01)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0101, 65535)
    OP_63(0x0101)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            (TxtCtl.SetColor, 0x0),
            '#0010330006V#1020F#6P啊啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            (TxtCtl.SetColor, 0x5),
            '#0020330007V#2P#40W原本……\n',
            '#40W我就是个坏掉的人偶……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1885')
    def lambda_1885():
        OP_99(0x0008, 0x0C, 0x14, 1500)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1885)

    Sleep(500)

    PlaySE(130, 0x00, 0x64)
    WaitForThreadExit(0x0008, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            (TxtCtl.SetColor, 0x5),
            '#0020330008V#2P#40W无法恢复成人类……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_18D6')
    def lambda_18D6():
        CameraMove(83130, 0, 6760, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_18D6)

    OP_99(0x0008, 0x15, 0x18, 1500)

    @scena.Lambda('lambda_18F7')
    def lambda_18F7():
        OP_99(0x0008, 0x19, 0x25, 1500)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_18F7)

    PlaySE(177, 0x00, 0x64)
    Sleep(500)

    ChrSetFlags(0x0101, 0x0002)
    ChrSetFlags(0x0101, 0x0020)
    ChrSetChipByIndex(0x0101, 20)
    ChrSetSubChip(0x0101, 32)
    WaitForThreadExit(0x0008, 0x0000)
    WaitForThreadExit(0x0101, 0x0002)
    Sleep(500)

    ChrSetPos(0x0009, 82600, -800, 6180, 0)

    ChrTalk(
        0x0009,
        (
            (TxtCtl.SetColor, 0x5),
            '#0020330009V#5P#40W所以……\n',
            '#40W……已经够了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            (TxtCtl.SetColor, 0x0),
            '#0010330010V#1020F#6P……………啊………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrSetFlags(0x0101, 0x0800)
    ChrSetFlags(0x0101, 0x8000)

    @scena.Lambda('lambda_19C6')
    def lambda_19C6():
        OP_9E(0x00FE, 20, 0, 2500, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_19C6)

    @scena.Lambda('lambda_19E0')
    def lambda_19E0():
        OP_99(0x00FE, 0x20, 0x27, 1500)
        Yield()

        Jump('lambda_19E0')

    DispatchAsync2(0x0101, 0x0002, lambda_19E0)

    ChrMoveTo(0x0101, 80430, 0, 5710, 1000, 0x00)
    TerminateThread(0x0101, 0x02)
    ChrSetSubChip(0x0101, 32)
    Sleep(500)

    @scena.Lambda('lambda_1A15')
    def lambda_1A15():
        OP_9E(0x00FE, 20, 0, 2500, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1A15)

    @scena.Lambda('lambda_1A2F')
    def lambda_1A2F():
        OP_99(0x00FE, 0x20, 0x27, 1500)
        Yield()

        Jump('lambda_1A2F')

    DispatchAsync2(0x0101, 0x0002, lambda_1A2F)

    ChrMoveTo(0x0101, 82020, 0, 6210, 1000, 0x00)
    TerminateThread(0x0101, 0x02)
    ChrSetSubChip(0x0101, 0)
    WaitForThreadExit(0x0101, 0x0003)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(1000)

    OP_99(0x0101, 0x00, 0x05, 1500)
    Sleep(1500)

    Fade(500)

    @scena.Lambda('lambda_1A81')
    def lambda_1A81():
        CameraSetDistance(2200, 5000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1A81)

    ChrSetSubChip(0x0008, 38)
    ChrSetFlags(0x000A, 0x0040)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 82020, 0, 6210, 0)
    ChrSetFlags(0x000A, 0x0002)
    ChrSetChipByIndex(0x000A, 20)
    ChrSetSubChip(0x000A, 21)
    Sleep(200)

    ChrSetSubChip(0x0101, 6)
    ChrSetSubChip(0x000A, 22)
    Sleep(200)

    ChrSetSubChip(0x0101, 7)
    ChrSetSubChip(0x000A, 23)
    Sleep(1000)

    Sleep(500)

    ChrSetPos(0x0009, 81500, 0, 5500, 0)

    ChrTalk(
        0x0009,
        (
            (TxtCtl.SetColor, 0x5),
            '#0020330011V#2P#60W谢谢你……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330012V#80W再见了，艾丝蒂尔……',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrSetSubChip(0x000A, 24)
    Sleep(1500)

    WaitForThreadExit(0x0008, 0x0001)

    ChrTalk(
        0x0101,
        (
            (TxtCtl.SetColor, 0x0),
            '#0010330013V#1025F#5P不……不要……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    ChrSetSubChip(0x0101, 8)
    ChrSetSubChip(0x000A, 26)
    Sleep(100)

    ChrSetSubChip(0x0101, 10)
    ChrSetSubChip(0x000A, 27)
    Sleep(100)

    ChrSetSubChip(0x0101, 11)
    Sleep(1000)

    FadeOut(2000, 0, -1)

    @scena.Lambda('lambda_1BBC')
    def lambda_1BBC():
        CameraSetDistance(5000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1BBC)

    ChrTalk(
        0x0101,
        (
            (TxtCtl.SetColor, 0x0),
            '#0010330014V#1014F#4S#30A#5P不要啊啊啊啊啊！！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 100, 3000, 500)
    Sleep(3500)

    OP_0D()
    OP_20(0x000003E8)
    OP_21()
    ChrClearFlags(0x0101, 0x0800)
    ChrClearFlags(0x0101, 0x8000)
    TerminateThread(0x0101, 0x02)
    ChrSetChipByIndex(0x0101, 5)
    ChrSetSubChip(0x0101, 0)
    ChrSetFlags(0x0101, 0x0002)
    ChrSetFlags(0x0101, 0x0800)
    ChrSetFlags(0x0101, 0x0004)
    ChrClearFlags(0x0101, 0x0001)
    ChrSetPos(0x0101, 60300, 500, 15000, 270)
    ChrSetPos(0x000B, 60720, 0, 13200, 0)
    ChrClearFlags(0x000B, 0x0080)
    CameraMove(60440, 0, 15530, 0)
    OP_67(0, 8510, -10000, 0)
    CameraSetDistance(2200, 0)
    OP_6C(32000, 0)
    OP_6E(288, 0)
    FadeIn(1000, 0)
    Sleep(500)

    @scena.Lambda('lambda_1CBD')
    def lambda_1CBD():
        OP_99(0x0101, 0x00, 0x02, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1CBD)

    WaitForThreadExit(0x0101, 0x0001)
    Sleep(50)

    ChrSetSubChip(0x0101, 5)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010330015V#1020F#5P………啊…………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000B,
        (
            (TxtCtl.SetColor, 0x0),
            '#0220330016V#264F#4P吓死我了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220330017V艾丝蒂尔，不要紧吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    ChrSetSubChip(0x0101, 7)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010330018V#1026F#5P玲……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330019V#1025F太、太好了……\n',
            '……是梦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            (TxtCtl.SetColor, 0x0),
            '#0220330020V#260F#4P嘻嘻……\n',
            '做了恶梦吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    ChrSetSubChip(0x0101, 4)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010330021V#1007F嗯……最糟糕的梦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330022V都是碰上了那种人偶\n',
            '才会做这么奇怪的梦——',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    PlaySE(571, 0x00, 0x3C)

    @scena.Lambda('lambda_1E9B')
    def lambda_1E9B():
        ChrJumpTo(0x00FE, 59860, 700, 15320, 500, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1E9B)

    ChrClearFlags(0x0101, 0x0002)
    ChrClearFlags(0x0101, 0x0020)
    ChrSetFlags(0x0101, 0x0001)
    ChrSetDirection(0x0101, 180, 0)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0101, 3)
    WaitForThreadExit(0x0101, 0x0001)
    ChrClearFlags(0x0101, 0x0800)
    OP_62(0x0101, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010330023V#1020F#5P……慢、慢着！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330024V为什么玲\n',
            '会在这种地方啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            (TxtCtl.SetColor, 0x0),
            '#0220330025V#261F#4P呜呵呵……\n',
            '你吓一跳的节奏都晚半拍。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220330026V艾丝蒂尔真是的，\n',
            '还是那么没紧张感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330027V#1019F#5P我就是没紧张感，不好意思呀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330028V#1004F……那，这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0101, 65535)
    OP_0D()
    Sleep(500)

    ChrSetDirection(0x0101, 270, 400)
    Sleep(500)

    ChrSetDirection(0x0101, 90, 400)
    Sleep(500)

    ChrTalk(
        0x000B,
        (
            (TxtCtl.SetColor, 0x0),
            '#0220330029V#263F#4P玲在这里\n',
            '并不是什么奇怪的事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220330030V#269F因为这里是\n',
            '我们的新据点嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 180, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010330031V#1002F#5P新据点……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            (TxtCtl.SetColor, 0x0),
            '#0220330032V#1305F#4P嘻嘻……\n',
            '去看看那个窗口如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330033V#1002F#5P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    @scena.Lambda('lambda_214E')
    def lambda_214E():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_214E')

    DispatchAsync2(0x000B, 0x0002, lambda_214E)

    ChrMoveTo(0x0101, 59470, 700, 13890, 1500, 0x00)
    ChrJumpTo(0x0101, 59710, 0, 13590, 200, 3000)

    @scena.Lambda('lambda_218A')
    def lambda_218A():
        CameraMove(62950, 0, 12460, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_218A)

    @scena.Lambda('lambda_21A2')
    def lambda_21A2():
        OP_67(0, 4220, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_21A2)

    @scena.Lambda('lambda_21BA')
    def lambda_21BA():
        CameraSetDistance(2900, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_21BA)

    @scena.Lambda('lambda_21CA')
    def lambda_21CA():
        OP_6C(57000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_21CA)

    @scena.Lambda('lambda_21DA')
    def lambda_21DA():
        OP_6E(288, 3000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_21DA)

    ChrWalkTo(0x0101, 59900, 0, 11640, 2000, 0x00)

    @scena.Lambda('lambda_21FE')
    def lambda_21FE():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_21FE)

    ChrWalkTo(0x0101, 61490, 0, 11290, 2000, 0x00)
    Sleep(500)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1500)

    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0101,
        (
            '#0010330034V#1020F#4S什…什么…！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C5414._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000E offset: 0x2290
@scena.Code('func_0E_2290')
def func_0E_2290():
    EventBegin(0x00)
    ChrSetPos(0x0101, 61490, 0, 11290, 90)
    ChrSetPos(0x000B, 61300, 0, 12390, 90)
    ChrClearFlags(0x000B, 0x0080)
    CameraMove(62950, 0, 12460, 0)
    OP_67(0, 4220, -10000, 0)
    CameraSetDistance(2900, 0)
    OP_6C(57000, 0)
    OP_6E(288, 0)
    CameraMove(63980, 0, 13140, 0)
    OP_67(0, 4220, -10000, 0)
    CameraSetDistance(2900, 0)
    OP_6C(57000, 0)
    OP_6E(288, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010330035V#1020F#6P…………………（惊讶）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0220330036V#263F#6P『红色方舟』古罗力亚斯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220330037V光凭这一艘飞船，\n',
            '就可能超越一个国家的军队哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000B, 180, 400)
    Sleep(400)

    ChrTalk(
        0x000B,
        (
            '#0220330038V#1306F#5P嘻嘻，相当\n',
            '有趣的玩具对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 0, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010330039V#1020F#4P你、你们……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330040V拿出这样的东西想干什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(157, 0x00, 0x5A)
    Sleep(1000)

    SetMessageWindowPos(320, 60, -1, -1)
    TalkSetChrName('男性的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0150330041V呀，看来醒了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetDirection(0x0101, 270, 600)
    Sleep(500)

    ChrSetDirection(0x0101, 180, 600)
    Sleep(500)

    ChrSetDirection(0x0101, 270, 600)
    Sleep(500)

    TalkSetChrName('男性的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0150330042V欢迎，艾丝蒂尔。\n',
            '睡得还好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    TalkSetChrName('男性的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0150330043V被带到这种地方来，\n',
            '想必你内心相当混乱吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    TalkSetChrName('男性的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0150330044V不过，我们并不\n',
            '打算加害于你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    TalkSetChrName('男性的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0150330045V请你大可以放心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ChrTalk(
        0x0101,
        (
            '#0010330046V#1002F#5P…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkSetChrName('男性的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0150330047V如何，你不想\n',
            '好好地谈一次吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    TalkSetChrName('男性的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0150330048V关于结社的事、我们的目的，\n',
            '以及那位共同的朋友……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    TalkSetChrName('男性的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0150330049V你的种种的疑问\n',
            '应该都能得到解答哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ChrTalk(
        0x0101,
        (
            '#0010330050V#1022F#5P……好吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330051V就让我好好发问吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkSetChrName('男性的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0150330052V好，稍等。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    TalkSetChrName('男性的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0150330053V玲，给艾丝蒂尔\n',
            '带个路吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x000B,
        (
            '#0220330054V#261F#5P嘻嘻，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(157, 0x00, 0x5A)
    Sleep(1000)

    ChrSetDirection(0x000B, 225, 400)

    @scena.Lambda('lambda_27EB')
    def lambda_27EB():
        CameraMove(61750, 0, 11850, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_27EB)

    ChrWalkTo(0x000B, 59560, 0, 11060, 1500, 0x00)
    ChrSetDirection(0x000B, 90, 400)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    ChrTalk(
        0x000B,
        (
            '#0220330055V#260F#6P那么，艾丝蒂尔。\n',
            '去『圣堂』吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330056V#1002F#2P『圣堂』……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0220330057V#263F#6P是这艘战舰最上层的\n',
            '一个很棒的房间哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220330058V『教授』在那里等着你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330059V#1002F#2P…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330060V#1022F……明白了。\n',
            '你带路吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0220330061V#1305F#6P嘻嘻，不用\n',
            '那么紧张啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220330062V或许对艾丝蒂尔来说\n',
            '也一定不会是什么坏事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330063V#1015F#2P哦……什么意思？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0220330064V#261F#6P好戏在后头呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220330065V#265F好了，跟玲走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    FormationAddMember(ChrTable['玲'], 0xFF, 0xFF)
    ChrSetChipByIndex(0x0101, 6)
    ChrSetChipByIndex(0x012F, 7)
    ChrSetFlags(0x0101, 0x1000)
    ChrSetFlags(0x012F, 0x1000)
    ChrSetFlags(0x000B, 0x0080)
    CameraMove(59560, 0, 11060, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, 59560, 0, 11060, 270)
    ChrSetPos(0x0001, 59560, 0, 11060, 270)
    OP_69(0x0000, 0)
    SetScenaFlags(ScenaFlag(0x0383, 3, 0x1C1B))
    RemoveItem(ItemTable['红色密码卡'], 1)
    RemoveItem(ItemTable['绿色密码卡'], 1)
    RemoveItem(ItemTable['蓝色密码卡'], 1)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x000F offset: 0x2AD7
@scena.Code('func_0F_2AD7')
def func_0F_2AD7():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0383, 3, 0x1C1B)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0383, 4, 0x1C1C)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_2AE4',
    )

    Return()

    def _loc_2AE4(): pass

    label('loc_2AE4')

    EventBegin(0x01)
    ChrTurnDirection(0x0101, 0x012F, 400)

    NpcTalk(
        0x0101,
        '歼灭天使玲',
        (
            '#0220330066V#263F艾丝蒂尔。\n',
            '『圣堂』不是这边。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220330067V#260F要去走廊另一端\n',
            '搭乘升降梯哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0010 offset: 0x2B78
@scena.Code('func_10_2B78')
def func_10_2B78():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0383, 3, 0x1C1B)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0383, 4, 0x1C1C)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_2B85',
    )

    Return()

    def _loc_2B85(): pass

    label('loc_2B85')

    EventBegin(0x01)
    ChrTurnDirection(0x0101, 0x012F, 400)

    NpcTalk(
        0x0101,
        '歼灭天使玲',
        (
            '#0220330068V#265F艾丝蒂尔。\n',
            '『圣堂』不是这边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CameraMove(-38720, 0, -65209, 2000)

    NpcTalk(
        0x0101,
        '歼灭天使玲',
        (
            '#0220330069V#2P看，就在那里\n',
            '搭乘升降梯哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Fade(1000)
    OP_69(0x0101, 0)
    OP_0D()
    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0011 offset: 0x2C47
@scena.Code('func_11_2C47')
def func_11_2C47():
    EventBegin(0x00)
    ChrSetPos(0x0101, 73290, 0, -234130, 270)
    ChrSetPos(0x012F, 74790, 0, -234130, 270)
    CameraMove(72090, 0, -232990, 0)
    OP_67(0, 7540, -10000, 0)
    CameraSetDistance(2700, 0)
    OP_6C(45000, 0)
    OP_6E(285, 0)
    FadeIn(1000, 0)
    OP_0D()
    PlaySE(14, 0x00, 0x64)
    Sleep(1000)

    OP_72(0x001A, 0x0010)
    OP_72(0x001A, 0x0020)
    OP_6F(0x001A, 0)
    OP_70(0x001A, 15)
    OP_73(0x001A)

    @scena.Lambda('lambda_2CDD')
    def lambda_2CDD():
        CameraMove(67800, 0, -233840, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2CDD)

    @scena.Lambda('lambda_2CF5')
    def lambda_2CF5():
        ChrMoveToRelative(0x00FE, -7000, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2CF5)

    Sleep(100)

    @scena.Lambda('lambda_2D15')
    def lambda_2D15():
        ChrMoveToRelative(0x00FE, -7000, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x012F, 0x0001, lambda_2D15)

    WaitForThreadExit(0x012F, 0x0001)
    OP_6F(0x001A, 15)
    OP_70(0x001A, 0)
    ChrTurnDirection(0x0101, 0x012F, 400)
    Sleep(500)

    NpcTalk(
        0x0101,
        '歼灭天使玲',
        (
            '#0220330075V#263F#6P嘻嘻……\n',
            '这里就是教授所在的『圣堂』哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220330076V#260F这前面\n',
            '艾丝蒂尔一个人去就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x012F,
        '艾丝蒂尔',
        (
            '#0010330077V#1015F#2P……对了，玲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0101,
        '歼灭天使玲',
        (
            '#0220330078V#260F#6P什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x012F,
        '艾丝蒂尔',
        (
            '#0010330079V#1002F#2P在研究所，操纵约修亚的\n',
            '人偶的是玲对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0101,
        '歼灭天使玲',
        (
            '#0220330080V#265F#6P嗯嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220330081V#261F是『教授』拜托我做的，\n',
            '相当有趣对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x012F,
        '艾丝蒂尔',
        (
            '#0010330082V#1007F#2P唉……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330083V#1003F……看来你也是\n',
            '『结社』的受害者啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0101,
        '歼灭天使玲',
        (
            '#0220330084V#264F#6P咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x012F,
        '艾丝蒂尔',
        (
            '#0010330085V#1007F#2P……算了，现在先不管。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330086V#1006F那么我过去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0101,
        '玲',
        (
            '#0220330087V#261F#6P嘻嘻，慢走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(67790, 0, -234130, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FormationDelMember(0x2E, 0xFF)
    ChrSetPos(0x0101, 67790, 0, -234130, 270)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetPos(0x000B, 70380, 0, -234050, 270)
    ChrClearFlags(0x000B, 0x0080)
    CreateThread(0x000B, 0x00, 0x00, func_02_9CA)
    OP_69(0x0101, 0)
    OP_69(0x0000, 0)
    OP_72(0x001A, 0x0010)
    SetScenaFlags(ScenaFlag(0x0383, 4, 0x1C1C))
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0012 offset: 0x3092
@scena.Code('func_12_3092')
def func_12_3092():
    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, 61000, 0, -185610, 0)
    CameraMove(61240, 0, -185600, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_20(0x00000BB8)

    @scena.Lambda('lambda_30F3')
    def lambda_30F3():
        CameraMove(60980, 500, -184400, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_30F3)

    @scena.Lambda('lambda_310B')
    def lambda_310B():
        OP_67(0, 5000, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_310B)

    @scena.Lambda('lambda_3123')
    def lambda_3123():
        CameraSetDistance(3120, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3123)

    @scena.Lambda('lambda_3133')
    def lambda_3133():
        OP_6C(0, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3133)

    WaitForThreadExit(0x0101, 0x0000)
    OP_21()
    Sleep(300)

    OP_6F(0x0002, 0)
    OP_70(0x0002, 270)
    PlaySE(306, 0x00, 0x64)
    Sleep(500)

    PlayBGM(121)
    OP_1F(0x46, 0x00000064)
    OP_73(0x0002)

    @scena.Lambda('lambda_3171')
    def lambda_3171():
        ChrWalkTo(0x00FE, 60840, 0, -180500, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3171)

    Sleep(2000)

    FadeOut(1000, 0, -1)
    OP_0D()
    MapSetFlags(0x02000000)
    NewScene('ED6_DT21/C5401._SN', 125, 0, 0)
    IdleLoop()
    OP_64(0x04, 0x0001)
    SetScenaFlags(ScenaFlag(0x0391, 1, 0x1C89))
    Sleep(500)

    EventEnd(0x00)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x79),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0013 offset: 0x31BC
@scena.Code('func_13_31BC')
def func_13_31BC():
    TalkBegin(0x000B)

    ChrTalk(
        0x000B,
        (
            '#0220330088V#1306F沿着走廊前进，\n',
            '马上就到『圣堂』了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220330089V『教授』在等你哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000B)

    Return()

# id: 0x0014 offset: 0x321E
@scena.Code('func_14_321E')
def func_14_321E():
    EventBegin(0x00)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetPos(0x000C, 6240, 0, 4990, 270)
    ChrClearFlags(0x000C, 0x0080)
    CameraMove(6850, 0, 5420, 0)
    OP_67(0, 5820, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(56000, 0)
    OP_6E(262, 0)
    FadeIn(2000, 0)
    OP_0D()
    Sleep(1000)

    Fade(1000)
    ChrSetPos(0x0101, 55870, 200, 13910, 0)
    ChrClearFlags(0x0101, 0x0080)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetChipByIndex(0x0101, 9)
    CameraMove(57200, 0, 14960, 0)
    OP_67(0, 5140, -10000, 0)
    CameraSetDistance(3050, 0)
    OP_6C(56000, 0)
    OP_6E(296, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010330239V#1003F#6P（进入『结社』\n',
            '就能再见到约修亚……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330240V（这种可能性\n',
            ' 倒是的确相当的高……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330241V#1016F（而且，也不一定\n',
            '真的要加入吧……？）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330242V（假装成为同伴之后\n',
            '探听内情也是可以……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330243V#1025F（以我的演技来说虽然困难，\n',
            '但是总比被关在这里好……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330244V（………………………………）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    Fade(500)

    @scena.Lambda('lambda_3454')
    def lambda_3454():
        CameraMove(58030, 0, 14730, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3454)

    ChrSetChipByIndex(0x0101, 65535)
    ChrSetPos(0x0101, 56790, 0, 14000, 90)
    OP_0D()
    Sleep(1000)

    @scena.Lambda('lambda_3488')
    def lambda_3488():
        CameraMove(62030, 0, 11840, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3488)

    ChrWalkTo(0x0101, 57970, 0, 11220, 2000, 0x00)
    ChrWalkTo(0x0101, 61500, 0, 11060, 2000, 0x00)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010330245V#1010F#6P（可是……\n',
            '总觉得有点不太对……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330246V#1002F（这……\n',
            '并不是我的作风。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(300)

    PlaySE(113, 0x00, 0x64)
    Sleep(500)

    ChrSetRGBAMask(0x000E, 255, 255, 255, 0, 0)
    ChrSetPos(0x000E, 50890, 0, 10990, 90)
    ChrClearFlags(0x000E, 0x0080)

    NpcTalk(
        0x000E,
        '青年的声音',
        (
            '#0140330247V#2P……打扰了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_35B5')
    def lambda_35B5():
        CameraMove(59440, 0, 11670, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_35B5)

    PlaySE(109, 0x00, 0x64)
    ChrSetDirection(0x0101, 270, 400)
    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_35DE')
    def lambda_35DE():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_35DE)

    @scena.Lambda('lambda_35F0')
    def lambda_35F0():
        ChrWalkTo(0x00FE, 56830, 0, 10980, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_35F0)

    Sleep(500)

    @scena.Lambda('lambda_3610')
    def lambda_3610():
        CameraMove(60440, 0, 11670, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3610)

    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010330248V#1020F啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330249V#1002F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x000E, 0x0001)

    ChrTalk(
        0x000E,
        (
            '#0140330250V#123F#6P呵……不用那么戒备。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330251V只要不再做出刚才那种\n',
            '不经大脑思考的行为，\n',
            '我们就不会加害于你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330252V#1022F不好意思啊，我做事就是不经大脑。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330253V#1019F什么嘛，你们\n',
            '不是到外面去了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0140330254V#124F#6P我只是负责留守。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330255V出去的是教授\n',
            '和其它的『执行者』们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330256V#1002F……你到底想怎样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0140330257V#121F#6P想知道的话\n',
            '就接受教授的邀请如何？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330258V这样就能得知你想了解的一切吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330259V#1003F…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0140330260V#123F#6P呵呵……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330261V已经有了答案，\n',
            '却还在迷惘中吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330262V#1026F！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0140330263V#124F#6P以我个人的意见看来，\n',
            '你到底还是\n',
            '不太适合『结社』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330264V无论是能力，还是性格。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330265V#1019F呜……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330266V说得好直白，\n',
            '也太打击别人的自尊心了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0140330267V#121F#6P嗯，关于能力方面，\n',
            '倒是还潜藏着一些可能性吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330268V但是，说到性格……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330269V#124F以『结社』的标准来衡量，\n',
            '你的阴暗面实在太少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330270V#1026F阴暗面……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0140330271V#120F#6P从属于『结社』的人\n',
            '必定都背负着某种黑暗的过去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330272V我，教授，其他的执行者……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330273V#124F当然，还有约修亚也是。',
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
            '#0010330274V#1003F………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330275V#1010F对了，『剑帝』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330276V#1002F你和约修亚\n',
            '到底是什么关系？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0140330277V#121F#6P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330278V#1002F约修亚一直\n',
            '十分介意洛伦斯少尉的事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330279V虽然未曾谋面，\n',
            '却好像知道对方是谁……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330280V似乎在竭尽全力\n',
            '调查他的真实身份。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0140330281V#121F#6P呼……这也难怪。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330282V#124F他的一部分记忆\n',
            '被教授封印了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330283V从离开『结社』的一刹起\n',
            '就被暗示了，\n',
            '根本无法想起任何具体的情报。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330284V#120F就算记得自己在『结社』\n',
            '做了怎样的事情\n',
            '但也想不起来相关人员的名字……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330285V必须要面对这样的一种困境。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330286V#1020F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0140330287V#124F小时候的记忆也是一样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330288V就算他还记得卡琳，\n',
            '恐怕对我的记忆也变得模糊了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330289V#1003F是吗……所以才……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330290V#1015F对了，『卡琳』这个名字，\n',
            '我好像在哪里听过？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0140330291V#121F#6P…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    @scena.Lambda('lambda_3EDA')
    def lambda_3EDA():
        CameraMove(62560, 0, 12000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3EDA)

    @scena.Lambda('lambda_3EF2')
    def lambda_3EF2():
        ChrTurnDirection(0x0101, 0x000E, 400)
        Yield()

        Jump('lambda_3EF2')

    DispatchAsync2(0x0101, 0x0002, lambda_3EF2)

    ChrMoveTo(0x000E, 61560, 0, 12060, 2000, 0x00)
    WaitForThreadExit(0x0101, 0x0001)
    TerminateThread(0x0101, 0x02)
    Sleep(1000)

    ChrTalk(
        0x000E,
        (
            '#0140330292V#129F#5P──卡琳·阿斯特雷。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330293V我的青梅竹马，\n',
            '也就是约修亚的亲姐姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330294V１０年前死了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330295V#1020F#3S#4P！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0140330296V#122F#5P你拿的口琴\n',
            '原本是卡琳的东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330297V作为遗物，\n',
            '交给约修亚保管……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330298V#125F之后他又将它交给了你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330299V#1020F#4P约修亚……\n',
            '原来有姐姐啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330300V#1003F…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330301V那个……为什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330302V#1026F卡琳……\n',
            '约修亚的姐姐会死呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000E, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x000E,
        (
            '#0140330303V#123F#5P……如果告诉你的话，\n',
            '也许你会受到很大的刺激。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330304V而且也会了解到约修亚和我们\n',
            '所背负的黑暗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330305V你有这个心理准备吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330306V#1003F#4P……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330307V#1010F……嗯，请告诉我吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330308V#1025F虽然不知道是否\n',
            '真的做好了心理准备……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330309V可是我……\n',
            '无论如何都想知道\n',
            '约修亚曾经发生过的事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330310V这就是我目前的心境。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0140330311V#124F#5P……好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000003E8)
    ChrSetDirection(0x000E, 90, 300)
    WaitForThreadExit(0x0101, 0x0001)
    OP_21()
    Sleep(500)

    PlayBGM(114)
    Sleep(500)

    @scena.Lambda('lambda_42EA')
    def lambda_42EA():
        CameraSetDistance(2800, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_42EA)

    Sleep(1000)

    ChrTalk(
        0x000E,
        (
            '#0140330312V#129F#5P那是在１０年前……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330313V我们所居住的哈梅尔村\n',
            '还记载在地图上的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    Sleep(1000)

    OP_C4(0x00, 0x00000010)
    OP_AD('ED6_DT24/C_VIS108._CH', 0x0000, 0x0000, 0x00000064)
    Sleep(3000)

    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0xC),
            '#0140330314V哈梅尔是个小村子……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330315V小孩子也很少，\n',
            '所以我们常常在一起玩。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330316V我梦想有一天能成为游击士\n',
            '空闲的时候就会练剑……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330317V对此，卡琳和小约修亚\n',
            '每天都司空见惯了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AE(0x000000C8)
    Sleep(2000)

    OP_AD('ED6_DT24/C_VIS109._CH', 0x0000, 0x0000, 0x00000064)
    Sleep(3000)

    Talk(
        (
            (TxtCtl.SetColor, 0xC),
            '#0140330318V……练习结束之后，\n',
            '我和约修亚会倾听\n',
            '卡琳吹奏口琴的旋律。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330319V卡琳会吹很多首曲子，\n',
            '但我们最喜欢的还是\n',
            '曾经一度流行的『星之所在』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330320V我们一直深信着',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330321V这样的日子将会持续到永远……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AE(0x000000C8)
    Sleep(2000)

    Sleep(500)

    Talk(
        (
            (TxtCtl.SetColor, 0xC),
            '#0140330322V但是，有一天，一群手持王国制导力枪',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AD('ED6_DT24/C_VIS110._CH', 0x0000, 0x0000, 0x00000064)
    Sleep(3000)

    Talk(
        (
            (TxtCtl.SetColor, 0xC),
            '#0140330323V的黑衣人向村子发动了袭击……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330324V他们包围了村子之后，\n',
            '开始对村民们进行残酷的折磨、虐杀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330325V从老人到婴儿，没有一个人可以幸免。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330326V被直接杀死的人也许还算是幸运，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330327V……女人们的命运就更加悲惨。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AE(0x000000C8)
    Sleep(2000)

    OP_AD('ED6_DT24/C_VIS111._CH', 0x0000, 0x0000, 0x00000064)
    Sleep(3000)

    Talk(
        (
            (TxtCtl.SetColor, 0xC),
            '#0140330328V我们──就在那地狱中开始拼命逃跑。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330329V听着亲人和朋友们的临终哀嚎，\n',
            '在『快逃！』的声音的催促下，\n',
            '拼尽全力向村外逃去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330330V之后，终于逃到了村外，\n',
            '我为了吸引追兵的注意力留下断后，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330331V让卡琳和约修亚先走，\n',
            '并向他们保证随后就会追上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AE(0x000000C8)
    Sleep(2000)

    Sleep(500)

    Talk(
        (
            (TxtCtl.SetColor, 0xC),
            '#0140330332V但是……\n',
            '袭击者们的布局超乎想象的周全。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330333V竟特意留下了负责截杀逃跑村民的人在外待命。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_C5(0x00, 0, 0, 752, 612, 0, 0, 768, 512, 0, 0, 751, 611, 0x00FFFFFF, 0x00, 'C_VIS112._CH')
    OP_C5(0x01, 0, 0, 512, 512, -200, 0, 768, 512, 0, 0, 511, 511, 0x00FFFFFF, 0x00, 'C_VIS138._CH')
    OP_C5(0x02, 0, 0, 712, 612, 0, 0, 768, 512, 0, 0, 711, 611, 0x00FFFFFF, 0x01, 'C_VIS139._CH')
    OP_C6(0x02, 0x03, -1, 500, 0)
    Sleep(500)

    OP_C6(0x00, 0x03, -1, 500, 0)
    Sleep(500)

    OP_C6(0x00, 0x00, -100000, 0, 3000)
    Sleep(1000)

    OP_C6(0x01, 0x03, -1, 500, 0)
    OP_C6(0x01, 0x00, 100000, 0, 2000)
    Sleep(3000)

    FadeOut(3000, 16777215, -1)
    OP_C6(0x01, 0x03, 16777215, 2000, 0)
    OP_C6(0x00, 0x03, 16777215, 2000, 0)
    OP_C6(0x02, 0x03, 16777215, 2000, 0)
    Sleep(2000)

    OP_0D()
    OP_77(0x00, 0x00, 0x00, 0x00, 0x00000000)
    FadeIn(2000, 16777215)
    OP_0D()
    Sleep(1000)

    FadeOut(3000, 0, -1)
    OP_0D()
    OP_77(0xFF, 0xFF, 0xFF, 0x00, 0x00000000)

    Talk(
        (
            (TxtCtl.SetColor, 0xC),
            '#0140330334V当我赶上他们的时候，那里出奇地安静。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330335V一具喉咙被打穿的男人尸体……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330336V手中握着枪发呆的约修亚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330337V从肩膀到背后都被劈开，\n',
            '但仍然紧紧抱着约修亚的卡琳……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330338V卡琳……在我赶到时还有一口气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AD('ED6_DT24/C_VIS113._CH', 0x0000, 0x0000, 0x00000064)
    Sleep(3000)

    Talk(
        (
            (TxtCtl.SetColor, 0xC),
            '#0140330339V不知为何，卡琳她……\n',
            '脸上竟浮现出平静而满足的表情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330340V她将心爱的口琴托付给约修亚，\n',
            '并请求我照顾约修亚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330341V然后──静静地离开了人世。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AE(0x000000C8)
    Sleep(2000)

    OP_C6(0x00, 0x06, 0, 0, 0)
    OP_C6(0x01, 0x06, 0, 0, 0)
    OP_C6(0x02, 0x06, 0, 0, 0)
    OP_C4(0x01, 0x00000010)
    FadeIn(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010330342V#1020F#4P…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330343V……为……什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330344V为什么……会有这种事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0140330345V#129F#5P帝国军在这之后\n',
            '开始侵略利贝尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330346V手持王国制造的导力枪的\n',
            '袭击者在国境附近引起的\n',
            '惨剧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330347V这无疑是发动侵略战争\n',
            '的最佳借口。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330348V#1026F#4P……怎么会……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330349V真的是利贝尔的士兵……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0140330350V#128F#5P被军队保护的我们\n',
            '最初是这样被告知的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330351V#129F然而数月后……\n',
            '战争以帝国军的败退而结束时，\n',
            '我们却收到了截然相反的说明。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330352V袭击村子的人们\n',
            '是猎兵团的野盗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330353V并且威胁我们\n',
            '绝对不许说出袭击的事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330354V军队向外界宣布发生了山崩，\n',
            '将通往哈梅尔的道路完全封锁了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330355V#1020F#4P等、等一下！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330356V为什么要特意\n',
            '撒这种谎？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330357V那简直就是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0140330358V#125F#5P哼哼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330359V#122F这一切都是帝国内的主战派\n',
            '为了侵略利贝尔\n',
            '而精心策划的剧本。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330360V到战争末期，此事已经无法掩盖，\n',
            '帝国政府也开始惊慌失措了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330361V只得假惺惺地提出停战，\n',
            '并决定借着将主谋者们悉数处刑\n',
            '来抹消这个事件。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330362V#129F这就是──\n',
            '『哈梅尔的悲剧』的真相。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330363V#1020F#4P…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0140330364V#129F#5P在这些日子中……\n',
            '约修亚的心完全坏掉了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330365V姐姐的死，亲人的死，邻居的死，\n',
            '初次夺走他人的生命的冲击，\n',
            '还有这充满欺瞒的世界……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330366V这一切，足够让\n',
            '一个六岁孩子的心灵彻底崩溃。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330367V#1003F#4P…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0140330368V#128F#5P之后发生的事情，\n',
            '大概约修亚都已经告诉你了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330369V心灵破碎的约修亚，\n',
            '对除口琴以外的一切事情都失去了兴趣，\n',
            '日渐消瘦衰弱。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330370V就在此时，怀斯曼出现在了\n',
            '约修亚和我的面前……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330371V我把约修亚托付给他，\n',
            '自己投身加入了『噬身之蛇』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330372V#129F而两年后……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330373V被教授改造之后的约修亚也\n',
            '走上了与我同样的道路。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330374V#1027F#4P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000E, 180, 400)
    Sleep(500)

    ChrTalk(
        0x000E,
        (
            '#0140330375V#123F#5P──这就是黑暗。\n',
            '艾丝蒂尔·布莱特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330376V你和约修亚之间\n',
            '有着怎样的隔阂……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330377V现在终于可以理解了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330378V#1003F#4P………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330379V#1010F……嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330380V我觉得，终于明白\n',
            '约修亚失踪的真正理由了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0140330381V#126F#5P什么……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330382V#1006F#4P──我现在可以明确拒绝\n',
            '教授的邀请了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330383V我绝对不会\n',
            '进入『噬身之蛇』的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330384V不管是喜欢还是讨厌『结社』\n',
            '这都无所谓……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330385V只要我还在追寻约修亚\n',
            '就绝对不会加入。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0140330386V#120F#5P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330387V#1015F#4P虽然很对不起\n',
            '特地邀请我的玲……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330388V#1016F不过只要道歉，她应该会原谅我吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0140330389V#124F#5P哼……奇怪的小姑娘。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330390V#123F听了刚才的话\n',
            '反而打消了迷惘。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330391V看来，只把你当作是『剑圣』的女儿\n',
            '似乎有些小看你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330392V#1016F#4P是、是吗？\n',
            '虽然不是很了解……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330393V#1006F倒是你，\n',
            '并不只是约修亚\n',
            '从前的朋友那么简单吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330394V对他来说，你可以算是哥哥吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0140220037V#121F#5P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000E, 90, 400)
    Sleep(500)

    ChrTalk(
        0x000E,
        (
            '#0140330396V#125F#5P为了避免误会，我要先声明，\n',
            '我和那家伙的兄弟情份\n',
            '在１０年前就已经结束了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330397V对现在的我来说，那家伙\n',
            '不过是个应该排除的危险分子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330398V#1020F#4P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0140330399V#128F#5P教授似乎以\n',
            '放任约修亚为乐……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330400V但我的想法却与教授不同。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330401V#129F在不久的将来，\n',
            '我会亲手收拾他的。',
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
            '#0010330402V#1005F#4P慢、慢着！\n',
            '为什么要这样啊！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330403V卡琳……\n',
            '约修亚的姐姐\n',
            '不是把他托付给你吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0140330404V#129F#5P我有我自己选择的道路。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330405V谁阻我路，就是我的敌人，\n',
            '无论是谁，我也都会斩杀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330406V#128F即便是违背\n',
            '卡琳的遗愿，也在所不惜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330407V#1026F#4P怎么会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(1000)

    CreateThread(0x000E, 0x01, 0x00, func_15_5A55)
    Sleep(4000)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetDirection(0x0101, 90, 400)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010330408V#1020F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x000E, 0x0001)
    FadeOut(1000, 0, -1)
    OP_0D()
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/C5414._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0015 offset: 0x5A55
@scena.Code('func_15_5A55')
def func_15_5A55():
    PlaySE(307, 0x00, 0x2D)
    Sleep(4000)

    PlaySE(307, 0x00, 0x2D)
    Sleep(4000)

    Return()

# id: 0x0016 offset: 0x5A6A
@scena.Code('func_16_5A6A')
def func_16_5A6A():
    EventBegin(0x00)
    ChrSetPos(0x0101, 61500, 0, 11060, 90)
    ChrSetPos(0x000E, 61560, 0, 12060, 90)
    ChrClearFlags(0x000E, 0x0080)
    CameraMove(62560, 0, 12000, 0)
    OP_67(0, 5140, -10000, 0)
    CameraSetDistance(3050, 0)
    OP_6C(56000, 0)
    OP_6E(296, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010330409V#1020F#6P那个是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0140330410V#125F#5P是教授和其他的执行者。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330411V计划的第三阶段\n',
            '终于要实行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000E, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010330412V#1002F#4P第、第三阶段是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000E, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x000E,
        (
            '#0140330413V#123F#5P呼……\n',
            '你没有必要知道这些。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330414V#124F事成之后，你应该也\n',
            '可以回到父亲的身边吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330415V在那之前\n',
            '乖乖待在这里就好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000E, 270, 400)
    Sleep(500)

    @scena.Lambda('lambda_5C50')
    def lambda_5C50():
        CameraMove(60160, 0, 11740, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5C50)

    @scena.Lambda('lambda_5C68')
    def lambda_5C68():
        ChrMoveTo(0x00FE, 55890, 0, 11030, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_5C68)

    Sleep(200)

    ChrSetDirection(0x0101, 270, 400)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010330416V#1005F#2P慢、慢着！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x000E, 0x0001)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    ChrTalk(
        0x000E,
        (
            '#0140330417V#122F#8P话先说在前头……\n',
            '可别想逃跑哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140330418V#125F这里距离地面的高度是８０００亚矩。\n',
            '你根本没有任何逃跑的机会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5D53')
    def lambda_5D53():
        CameraMove(57590, 0, 11310, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5D53)

    ChrWalkTo(0x000E, 50860, 0, 11030, 2000, 0x00)

    @scena.Lambda('lambda_5D7F')
    def lambda_5D7F():
        ChrWalkTo(0x00FE, 49500, 0, 10950, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_5D7F)

    ChrSetRGBAMask(0x000E, 255, 255, 255, 0, 400)
    WaitForThreadExit(0x000E, 0x0001)
    ChrSetFlags(0x000E, 0x0080)
    WaitForThreadExit(0x0101, 0x0001)
    PlaySE(109, 0x00, 0x64)
    Sleep(1000)

    CameraMove(62560, 0, 12000, 2000)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010330419V#1002F#5P……………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330420V#1007F叫我别想逃跑吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330421V越是这么说就越想试试看，\n',
            '这应该算是人之常情吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330422V#1006F幸好教授和玲他们\n',
            '好像都出去了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330423V好……就这么决定了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_DB()

    @scena.Lambda('lambda_5EC4')
    def lambda_5EC4():
        CameraMove(58740, 0, 11420, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5EC4)

    ChrWalkTo(0x0101, 53350, 0, 10870, 3000, 0x00)
    Sleep(500)

    ChrSetDirection(0x0101, 0, 400)
    Sleep(500)

    ChrSetDirection(0x0101, 270, 400)
    ChrSetDirection(0x0101, 180, 400)
    Sleep(500)

    ChrSetDirection(0x0101, 270, 400)
    Sleep(1000)

    ChrSetDirection(0x0101, 45, 400)
    ChrWalkTo(0x0101, 57090, 0, 12790, 3000, 0x00)
    ChrWalkTo(0x0101, 57330, 0, 14200, 3000, 0x00)
    Sleep(500)

    ChrSetDirection(0x0101, 45, 400)
    Sleep(500)

    ChrSetDirection(0x0101, 270, 400)
    Sleep(500)

    ChrWalkTo(0x0101, 57220, 0, 10620, 3000, 0x00)
    ChrSetDirection(0x0101, 270, 400)
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrSetDirection(0x0101, 90, 600)
    Sleep(500)

    @scena.Lambda('lambda_5FAF')
    def lambda_5FAF():
        CameraMove(62560, 0, 12000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_5FAF)

    ChrWalkTo(0x0101, 61500, 0, 10910, 5000, 0x00)
    WaitForThreadExit(0x0101, 0x0002)
    Sleep(500)

    OP_DC()

    ChrTalk(
        0x0101,
        (
            '#0010330424V#1002F#6P……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330425V虽然…一旦掌握不好时机就会有性命危险，\n',
            '但如果能够抓住这次机会……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330426V#1015F为了让他们放松警惕，\n',
            '先老老实实地待上两个小时……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330427V#1006F……嗯！\n',
            '看来值得一试呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrSetDirection(0x0101, 270, 400)
    Sleep(500)

    @scena.Lambda('lambda_60E9')
    def lambda_60E9():
        CameraSetDistance(2800, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_60E9)

    Sleep(500)

    Fade(500)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0101, 4)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010330428V#1007F#5P……原来这是\n',
            '姐姐的珍贵遗物啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330429V#1027F#5P约修亚那笨蛋……\n',
            '这种东西怎么可以轻易交给别人呀！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    OP_20(0x00000BB8)
    OP_21()
    Sleep(1000)

    SetScenaFlags(ScenaFlag(0x021E, 5, 0x10F5))
    NewScene('ED6_DT21/C5400._SN', 111, 0, 0)
    IdleLoop()

    Return()

# id: 0x0017 offset: 0x61B7
@scena.Code('func_17_61B7')
def func_17_61B7():
    EventBegin(0x00)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetPos(0x000D, 6240, 0, 4990, 270)
    ChrSetPos(0x000C, 4270, 0, 26120, 315)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetChipByIndex(0x000D, 32)
    ChrSetChipByIndex(0x000C, 32)
    CameraMove(4660, 0, 23820, 0)
    OP_67(0, 5500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(44000, 0)
    OP_6E(265, 0)
    FadeIn(1000, 0)
    OP_0D()
    OP_72(0x0008, 0x0010)
    OP_72(0x0008, 0x0020)
    PlaySE(109, 0x00, 0x64)
    OP_6F(0x0008, 0)
    OP_70(0x0008, 15)
    OP_73(0x0008)
    Sleep(1000)

    ChrSetChipByIndex(0x000C, 32)

    @scena.Lambda('lambda_626B')
    def lambda_626B():
        ChrWalkTo(0x00FE, 3960, 0, 5780, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_626B)

    @scena.Lambda('lambda_6286')
    def lambda_6286():
        CameraMove(5620, 0, 5560, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6286)

    @scena.Lambda('lambda_629E')
    def lambda_629E():
        OP_6C(66000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_629E)

    Sleep(2000)

    OP_6F(0x0008, 15)
    OP_70(0x0008, 0)
    OP_71(0x0008, 0x0010)
    WaitForThreadExit(0x0000, 0x0001)
    ChrSetChipByIndex(0x000C, 32)
    ChrSetSubChip(0x000C, 0)
    Sleep(100)

    ChrSetDirection(0x000C, 90, 400)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    NpcTalk(
        0x000C,
        '强化猎兵',
        (
            '#4210330430V#6P换班的时间到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000C,
        '强化猎兵',
        (
            '#4210330431V#6P小丫头的情况怎样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000D,
        '强化猎兵',
        (
            '#4220330432V#5P哈哈，很安分呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000D,
        '强化猎兵',
        (
            '#4220330433V#5P就算是游击士，\n',
            '到底还是小孩子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000D,
        '强化猎兵',
        (
            '#4220330434V#5P恐怕正在床上发抖呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000C,
        '强化猎兵',
        (
            '#4210330435V#6P哼……\n',
            '居然要留下来看守这个小东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000C,
        '强化猎兵',
        (
            '#4210330436V#6P真是够无聊的。\n',
            '我也想参加启动作战啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000D,
        '强化猎兵',
        (
            '#4220330437V#5P别发牢骚啦。\n',
            '这是莱恩哈特大人的命令嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_1F(0x50, 0x000003E8)
    PlaySE(214, 0x01, 0x46)
    Sleep(500)

    OP_62(0x000D, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(50)

    OP_62(0x000C, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    NpcTalk(
        0x000D,
        '强化猎兵',
        (
            '#4220330438V#5P……嗯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000C,
        '强化猎兵',
        (
            '#4210330439V#6P什么，这声音是？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_6541')
    def lambda_6541():
        CameraMove(7090, 0, 5430, 1000)

        ExitThread()

    DispatchAsync(0x000D, 0x0003, lambda_6541)

    ChrSetDirection(0x000D, 90, 400)
    Sleep(500)

    PlaySE(114, 0x00, 0x64)
    Sleep(1500)

    NpcTalk(
        0x000D,
        '强化猎兵',
        (
            '#4220330440V#6P喂！\n',
            '你到底在干什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_23(0x00D6)
    PlaySE(308, 0x00, 0x64)
    Sleep(1000)

    OP_1F(0x64, 0x000003E8)
    OP_62(0x000D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    NpcTalk(
        0x000C,
        '强化猎兵',
        (
            '#4210330441V#6P喂，难不成……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000D,
        '强化猎兵',
        (
            '#4220330442V#6P逃走了吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(115, 0x00, 0x64)
    Sleep(500)

    OP_72(0x000A, 0x0010)
    OP_72(0x000A, 0x0020)
    PlaySE(109, 0x00, 0x64)
    OP_6F(0x000A, 0)
    OP_70(0x000A, 15)
    OP_73(0x000A)
    ChrSetChipByIndex(0x000D, 11)

    @scena.Lambda('lambda_6674')
    def lambda_6674():
        ChrWalkTo(0x00FE, 8500, 0, 5000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_6674)

    Sleep(100)

    ChrSetChipByIndex(0x000C, 11)

    @scena.Lambda('lambda_6699')
    def lambda_6699():
        ChrWalkTo(0x00FE, 8500, 0, 5000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_6699)

    WaitForThreadExit(0x000D, 0x0001)
    ChrSetFlags(0x000D, 0x0080)
    WaitForThreadExit(0x000C, 0x0001)
    ChrSetFlags(0x000C, 0x0080)
    Fade(1000)
    CameraMove(52360, 0, 12450, 0)
    OP_67(0, 5270, -10000, 0)
    CameraSetDistance(2980, 0)
    OP_6C(56000, 0)
    OP_6E(281, 0)
    LoadEffect(0x01, 'scraft\\\\sc000_11.eff')
    OP_71(0x000A, 0x0010)
    OP_71(0x0000, 0x0004)
    OP_72(0x0001, 0x0004)
    PlaySE(451, 0x00, 0x64)
    OP_0D()

    @scena.Lambda('lambda_6736')
    def lambda_6736():
        CameraMove(58180, 0, 12600, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_6736)

    CreateThread(0x000D, 0x01, 0x00, func_1D_79A2)
    Sleep(500)

    CreateThread(0x000C, 0x01, 0x00, func_1E_79F4)
    WaitForThreadExit(0x000C, 0x0001)
    OP_62(0x000D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    WaitForThreadExit(0x0101, 0x0000)

    NpcTalk(
        0x000C,
        '强化猎兵',
        (
            '#4210330443V#6P啊，糟糕……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000D,
        '强化猎兵',
        (
            '#4220330444V#6P怎、怎么会！？\n',
            '她以为这里是哪里啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000D,
        '强化猎兵',
        (
            '#4220330445V#6P那丫头，难道想自杀吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_6844')
    def lambda_6844():
        CameraMove(61920, 0, 11630, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6844)

    ChrSetChipByIndex(0x000D, 11)

    @scena.Lambda('lambda_6861')
    def lambda_6861():
        ChrWalkTo(0x00FE, 61490, 0, 10480, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_6861)

    Sleep(300)

    ChrSetChipByIndex(0x000C, 11)

    @scena.Lambda('lambda_6886')
    def lambda_6886():
        ChrWalkTo(0x00FE, 60490, 0, 11490, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_6886)

    WaitForThreadExit(0x000D, 0x0001)
    ChrSetChipByIndex(0x000D, 8)
    WaitForThreadExit(0x000C, 0x0001)
    ChrSetChipByIndex(0x000C, 8)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    NpcTalk(
        0x000D,
        '强化猎兵',
        (
            '#4220330446V#6P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000D,
        '强化猎兵',
        (
            '#4220330447V#6P不行，可能掉下去了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000C,
        '强化猎兵',
        (
            '#4210330448V#6P喂喂，饶了我吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000C,
        '强化猎兵',
        (
            '#4210330449V#6P该怎么对莱恩哈特大人\n',
            '交代才好？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000C,
        '强化猎兵',
        (
            '#4210330450V#6P那个臭小鬼……\n',
            '居然给我惹出这种麻烦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    OP_20(0x000003E8)
    OP_21()
    ChrSetPos(0x0101, 63690, 2000, 11810, 270)

    ChrTalk(
        0x0101,
        (
            '#0010330451V#6P你说谁～是臭小鬼？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(500)

    PlayBGM(113)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x71),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(500)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x0101, 0x0002)
    ChrSetChipByIndex(0x0101, 14)
    ChrSetSubChip(0x0101, 0)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetPos(0x0101, 63500, 500, 11810, 270)
    ChrClearFlags(0x0101, 0x0080)
    ChrSetFlags(0x0101, 0x0020)
    ChrSetFlags(0x0101, 0x0040)
    ChrSetFlags(0x0101, 0x1000)
    OP_99(0x0101, 0x00, 0x02, 2500)
    ChrSetFlags(0x0101, 0x0800)

    @scena.Lambda('lambda_6AAC')
    def lambda_6AAC():
        OP_99(0x00FE, 0x03, 0x04, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_6AAC)

    ChrMoveTo(0x0101, 61910, -200, 11810, 12000, 0x00)
    PlayEffect(0x01, 0x00, 0x000C, 0, 800, 500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(521, 0x00, 0x64)
    OP_7C(100, 0, 5000, 1000)
    CreateThread(0x000C, 0x00, 0x00, func_1C_7932)

    NpcTalk(
        0x000C,
        '强化猎兵',
        (
            '#4210330452V#15A#5P呜哇！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    @scena.Lambda('lambda_6B4A')
    def lambda_6B4A():
        CameraMove(59720, 0, 11940, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_6B4A)

    WaitForThreadExit(0x0101, 0x0002)

    @scena.Lambda('lambda_6B67')
    def lambda_6B67():
        ChrSetDirection(0x00FE, 270, 0)
        Yield()

        Jump('lambda_6B67')

    DispatchAsync2(0x0101, 0x0003, lambda_6B67)

    @scena.Lambda('lambda_6B78')
    def lambda_6B78():
        ChrJumpTo(0x00FE, 60930, 0, 11900, 2500, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6B78)

    Sleep(100)

    ChrClearFlags(0x0101, 0x0002)
    ChrClearFlags(0x0101, 0x0020)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)

    @scena.Lambda('lambda_6BAF')
    def lambda_6BAF():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_6BAF')

    DispatchAsync2(0x000D, 0x0003, lambda_6BAF)

    @scena.Lambda('lambda_6BC0')
    def lambda_6BC0():
        ChrJumpTo(0x00FE, 59390, 0, 7830, 500, 7000)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_6BC0)

    WaitForThreadExit(0x0101, 0x0001)
    PlaySE(164, 0x00, 0x64)
    ChrSetFlags(0x0101, 0x0002)
    ChrSetChipByIndex(0x0101, 14)

    @scena.Lambda('lambda_6BF2')
    def lambda_6BF2():
        OP_99(0x00FE, 0x05, 0x06, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_6BF2)

    WaitForThreadExit(0x0101, 0x0002)
    ChrClearFlags(0x0101, 0x0004)
    ChrClearFlags(0x0101, 0x0800)
    WaitForThreadExit(0x000D, 0x0002)
    Sleep(500)

    WaitForThreadExit(0x000C, 0x0000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_6C29')
    def lambda_6C29():
        CameraMove(59670, 0, 10950, 1000)

        ExitThread()

    DispatchAsync(0x000C, 0x0000, lambda_6C29)

    @scena.Lambda('lambda_6C41')
    def lambda_6C41():
        OP_6E(298, 1000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_6C41)

    OP_62(0x000D, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    LoadEffect(0x02, 'map\\\\mp003_00.eff')
    LoadEffect(0x03, 'monster\\\\msc0310.eff')
    WaitForThreadExit(0x000C, 0x0000)
    WaitForThreadExit(0x000C, 0x0001)
    TerminateThread(0x0101, 0x03)

    NpcTalk(
        0x000D,
        '强化猎兵',
        (
            '#4220330453V#4P你、你！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(213, 0x00, 0x64)
    ChrClearFlags(0x0101, 0x0002)
    ChrSetChipByIndex(0x0101, 21)
    ChrSetSubChip(0x0101, 0)
    ChrTurnDirection(0x0101, 0x000D, 500)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010330454V#1005F#5P太天真了，大叔！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CreateThread(0x000D, 0x00, 0x00, func_18_7503)
    CreateThread(0x000D, 0x01, 0x00, func_19_757B)

    @scena.Lambda('lambda_6D26')
    def lambda_6D26():
        CameraMove(58930, 0, 12880, 600)

        ExitThread()

    DispatchAsync(0x000C, 0x0000, lambda_6D26)

    PlaySE(163, 0x00, 0x64)
    ChrSetFlags(0x0101, 0x0004)

    @scena.Lambda('lambda_6D48')
    def lambda_6D48():
        ChrJumpTo(0x00FE, 59560, 500, 15180, 1500, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_6D48)

    WaitForThreadExit(0x0101, 0x0000)
    PlaySE(164, 0x00, 0x64)
    Sleep(300)

    @scena.Lambda('lambda_6D75')
    def lambda_6D75():
        CameraMove(55620, 0, 9400, 500)

        ExitThread()

    DispatchAsync(0x000C, 0x0000, lambda_6D75)

    PlaySE(163, 0x00, 0x64)

    @scena.Lambda('lambda_6D92')
    def lambda_6D92():
        ChrSetDirection(0x00FE, 180, 0)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6D92)

    @scena.Lambda('lambda_6DA0')
    def lambda_6DA0():
        ChrJumpTo(0x00FE, 56050, 200, 14010, 1000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_6DA0)

    Sleep(50)

    CreateThread(0x000D, 0x00, 0x00, func_1A_767D)
    CreateThread(0x000D, 0x01, 0x00, func_1B_7734)
    WaitForThreadExit(0x0101, 0x0000)
    PlaySE(164, 0x00, 0x64)
    Sleep(100)

    PlaySE(163, 0x00, 0x64)

    @scena.Lambda('lambda_6DE5')
    def lambda_6DE5():
        ChrSetDirection(0x00FE, 225, 0)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6DE5)

    @scena.Lambda('lambda_6DF3')
    def lambda_6DF3():
        ChrJumpTo(0x00FE, 53450, 0, 10330, 500, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_6DF3)

    WaitForThreadExit(0x0101, 0x0000)
    PlaySE(164, 0x00, 0x64)
    TerminateThread(0x000D, 0x03)
    ChrClearFlags(0x0101, 0x0004)
    ChrSetChipByIndex(0x0101, 17)

    @scena.Lambda('lambda_6E29')
    def lambda_6E29():
        CameraMove(59460, 0, 8740, 500)

        ExitThread()

    DispatchAsync(0x000C, 0x0000, lambda_6E29)

    OP_97(0x0101, 55260, 9420, -100000, 12000, 0x0001)

    @scena.Lambda('lambda_6E56')
    def lambda_6E56():
        ChrSetDirection(0x00FE, 90, 0)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6E56)

    @scena.Lambda('lambda_6E64')
    def lambda_6E64():
        ChrJumpTo(0x00FE, 57760, 0, 7840, 200, 12000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_6E64)

    Sleep(100)

    ChrSetChipByIndex(0x0101, 19)
    ChrSetSubChip(0x0101, 0)
    PlaySE(500, 0x00, 0x64)

    @scena.Lambda('lambda_6E96')
    def lambda_6E96():
        OP_99(0x0101, 0x01, 0x0C, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_6E96)

    TerminateThread(0x000D, 0x00)
    TerminateThread(0x000D, 0x01)
    Sleep(400)

    PlaySE(521, 0x00, 0x64)
    OP_7C(100, 0, 5000, 1000)
    PlayEffect(0x01, 0x00, 0x000D, 0, 700, 0, 0, 0, 0, 1200, 1200, 1200, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_6EFE')
    def lambda_6EFE():
        CameraMove(61000, 0, 8620, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_6EFE)

    @scena.Lambda('lambda_6F16')
    def lambda_6F16():
        CameraSetDistance(2810, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6F16)

    TerminateThread(0x000D, 0x03)
    ChrSetDirection(0x000D, 270, 0)
    ChrSetFlags(0x000D, 0x0020)
    ChrSetFlags(0x000D, 0x0002)
    ChrSetFlags(0x000D, 0x0800)
    ChrSetFlags(0x000D, 0x0004)
    ChrSetFlags(0x000D, 0x1000)

    @scena.Lambda('lambda_6F4A')
    def lambda_6F4A():
        ChrMoveTo(0x00FE, 61500, 1500, 7950, 24000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_6F4A)

    ChrSetChipByIndex(0x000D, 13)
    ChrSetSubChip(0x000D, 7)
    WaitForThreadExit(0x000D, 0x0001)
    OP_7C(100, 50, 5000, 1000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(1000)

    @scena.Lambda('lambda_6F93')
    def lambda_6F93():
        ChrMoveTo(0x000D, 61500, 0, 7950, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_6F93)

    Sleep(100)

    @scena.Lambda('lambda_6FB3')
    def lambda_6FB3():
        ChrMoveTo(0x000D, 61500, 0, 7950, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_6FB3)

    Sleep(100)

    @scena.Lambda('lambda_6FD3')
    def lambda_6FD3():
        ChrMoveTo(0x000D, 61500, 0, 7950, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_6FD3)

    WaitForThreadExit(0x000D, 0x0001)
    ChrClearFlags(0x000D, 0x0020)
    ChrClearFlags(0x000D, 0x0004)
    ChrClearFlags(0x000D, 0x0002)
    ChrSetChipByIndex(0x000D, 15)
    ChrSetSubChip(0x000D, 0)
    OP_99(0x000D, 0x00, 0x02, 1500)
    PlaySE(524, 0x00, 0x64)
    Sleep(500)

    NpcTalk(
        0x000D,
        '强化猎兵',
        (
            '#4220330455V#5P呜哇，呼呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrClearFlags(0x0101, 0x0020)
    ChrClearFlags(0x0101, 0x1000)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0101, 65535)
    Sleep(500)

    ChrWalkTo(0x0101, 59690, 0, 8039, 2000, 0x00)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010330456V#1028F#6P哼哼。\n',
            '可别小看游击士哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330457V而且你们太没礼貌了吧？\n',
            '竟然称呼少女为臭小鬼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000D,
        '强化猎兵',
        (
            '#4220330458V#5P真、真是看走眼了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000D,
        '强化猎兵',
        (
            '#4220330459V#5P我可没有那么说啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330460V#1004F#6P哦，是吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330461V#1006F算了，大叔你也是同罪。\n',
            '暂且做个替罪羊吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    PlaySE(216, 0x00, 0x64)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0101, 19)
    OP_0D()
    Sleep(300)

    ChrSetFlags(0x0101, 0x1000)
    ChrSetFlags(0x0101, 0x0020)

    @scena.Lambda('lambda_71E5')
    def lambda_71E5():
        OP_99(0x0101, 0x00, 0x0C, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_71E5)

    Sleep(500)

    PlaySE(521, 0x00, 0x64)
    OP_7C(0, 50, 5000, 1000)
    PlayEffect(0x01, 0x00, 0x000D, 0, 700, 300, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_7245')
    def lambda_7245():
        OP_9E(0x00FE, 0, 30, 300, 2000)

        ExitThread()

    DispatchAsync(0x000D, 0x0003, lambda_7245)

    WaitForThreadExit(0x0101, 0x0000)
    ChrSetChipByIndex(0x0101, 21)
    ChrSetSubChip(0x0101, 0)

    NpcTalk(
        0x000D,
        '强化猎兵',
        (
            '#4220330462V#5P……嗯～…………',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(1500)

    Fade(500)
    PlaySE(524, 0x00, 0x64)
    ChrSetPos(0x000D, 60700, 0, 7800, 270)
    ChrClearFlags(0x000D, 0x0001)
    ChrSetFlags(0x000D, 0x0002)
    ChrSetChipByIndex(0x000D, 18)
    ChrSetSubChip(0x000D, 15)
    OP_0D()
    ChrClearFlags(0x0101, 0x0040)
    ChrClearFlags(0x000C, 0x0040)
    ChrClearFlags(0x000D, 0x0040)
    Sleep(1500)

    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0101, 65535)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010330463V#1007F#6P那～么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 270, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010330464V#1006F#5P增援大概很快就会来了，\n',
            '还是赶快逃跑吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330465V必须想个脱逃的办法才行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    ChrSetChipByIndex(0x0101, 16)
    ChrSetSubChip(0x0101, 0)
    OP_0D()
    Sleep(500)

    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1500)

    OP_63(0x0101)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010330466V#1027F#5P（我不会放弃的……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330467V（一定要再次见到约修亚……\n',
            '  ……和那个笨蛋重逢……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010330468V#1005F#5P#3S（我绝对不会放弃！）',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    ChrClearFlags(0x0101, 0x1000)
    CameraMove(59690, 0, 8039, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x0383, 5, 0x1C1D))
    OP_28(0x0099, 0x04, 0x02)
    OP_28(0x0099, 0x04, 0x08)
    OP_28(0x0099, 0x01, 0x0001)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0018 offset: 0x7503
@scena.Code('func_18_7503')
def func_18_7503():
    PlayEffect(0x03, 0x01, 0x000D, 0, 800, 1000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    PlayEffect(0x03, 0x01, 0x000D, 0, 800, 1000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    StopEffect(0x01, 0x02)

    Return()

# id: 0x0019 offset: 0x757B
@scena.Code('func_19_757B')
def func_19_757B():
    Sleep(300)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x02, 0xFF, 0x00FF, 60520, 0, 10840, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x02, 0xFF, 0x00FF, 60910, 0, 12450, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x02, 0xFF, 0x00FF, 60540, 500, 14400, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x02, 0xFF, 0x00FF, 61770, 800, 15340, 90, 90, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    Return()

# id: 0x001A offset: 0x767D
@scena.Code('func_1A_767D')
def func_1A_767D():
    Sleep(100)

    PlayEffect(0x03, 0x01, 0x000D, 0, 800, 1000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    PlayEffect(0x03, 0x01, 0x000D, 0, 800, 1000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    PlayEffect(0x03, 0x01, 0x000D, 0, 800, 1000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    StopEffect(0x01, 0x02)

    Return()

# id: 0x001B offset: 0x7734
@scena.Code('func_1B_7734')
def func_1B_7734():
    Sleep(300)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x02, 0xFF, 0x00FF, 59540, 500, 15040, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x02, 0xFF, 0x00FF, 57490, 1000, 16020, 0, 90, 90, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x02, 0xFF, 0x00FF, 56080, 800, 15120, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x02, 0xFF, 0x00FF, 55920, 200, 13920, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x02, 0xFF, 0x00FF, 53370, 0, 12980, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x02, 0xFF, 0x00FF, 53800, 0, 10980, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x02, 0xFF, 0x00FF, 52880, 0, 8770, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlaySE(503, 0x00, 0x64)
    PlayEffect(0x02, 0xFF, 0x00FF, 52810, 0, 8230, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    Return()

# id: 0x001C offset: 0x7932
@scena.Code('func_1C_7932')
def func_1C_7932():
    ChrSetChipByIndex(0x000C, 13)
    ChrSetSubChip(0x000C, 0)

    @scena.Lambda('lambda_7942')
    def lambda_7942():
        ChrJumpTo(0x00FE, 57360, 0, 11840, 2000, 10000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_7942)

    WaitForThreadExit(0x000C, 0x0001)
    ChrSetFlags(0x000C, 0x0002)
    ChrClearFlags(0x000C, 0x0001)
    ChrSetChipByIndex(0x000C, 18)
    ChrSetSubChip(0x000C, 11)
    ChrJumpTo(0x000C, 55660, 0, 12080, 1000, 8000)
    ChrJumpTo(0x000C, 54170, 0, 12070, 300, 6000)

    Return()

# id: 0x001D offset: 0x79A2
@scena.Code('func_1D_79A2')
def func_1D_79A2():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, 49790, 0, 10830, 90)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_79C9')
    def lambda_79C9():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_79C9)

    ChrSetChipByIndex(0x00FE, 11)
    ChrWalkTo(0x00FE, 54760, 0, 10170, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 8)

    Return()

# id: 0x001E offset: 0x79F4
@scena.Code('func_1E_79F4')
def func_1E_79F4():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, 49790, 0, 10830, 90)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_7A1B')
    def lambda_7A1B():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_7A1B)

    ChrSetChipByIndex(0x00FE, 11)
    ChrWalkTo(0x00FE, 54760, 0, 11810, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 8)

    Return()

# id: 0x001F offset: 0x7A46
@scena.Code('func_1F_7A46')
def func_1F_7A46():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0444, 2, 0x2222)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0444, 3, 0x2223)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_7A53',
    )

    Return()

    def _loc_7A53(): pass

    label('loc_7A53')

    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7A78',
    )

    Call(0, 0x003A)
    Call(0, 0x003B)
    FadeIn(0, 0)
    Sleep(100)

    def _loc_7A78(): pass

    label('loc_7A78')

    Fade(1000)
    OP_4A(0x000F, 0)
    OP_4A(0x0010, 0)
    OP_4A(0x0011, 0)
    OP_4A(0x0014, 0)
    OP_4A(0x0015, 0)
    OP_4A(0x0012, 0)
    OP_4A(0x0013, 0)
    OP_4A(0x0016, 0)
    ChrSetPos(0x0015, -81520, 0, -331440, 225)
    CameraMove(-87930, 0, -344320, 0)
    OP_67(0, 7500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(57000, 0)
    OP_6E(343, 0)
    ChrSetPos(0x010B, -88230, 0, -342500, 0)
    ChrSetPos(0x0102, -87830, 0, -343500, 0)
    ChrSetPos(0x0101, -89410, 0, -343500, 0)
    ChrSetPos(0x00F9, -88810, 0, -344500, 0)
    Sleep(500)

    OP_62(0x010B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    CreateThread(0x010B, 0x01, 0x00, func_20_90E6)

    @scena.Lambda('lambda_7B5D')
    def lambda_7B5D():
        CameraMove(-82340, 0, -335690, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_7B5D)

    @scena.Lambda('lambda_7B75')
    def lambda_7B75():
        OP_67(0, 6000, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_7B75)

    @scena.Lambda('lambda_7B8D')
    def lambda_7B8D():
        CameraSetDistance(2800, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_7B8D)

    @scena.Lambda('lambda_7B9D')
    def lambda_7B9D():
        OP_6C(57000, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_7B9D)

    @scena.Lambda('lambda_7BAD')
    def lambda_7BAD():
        OP_6E(343, 2000)

        ExitThread()

    DispatchAsync(0x010B, 0x0002, lambda_7BAD)

    CreateThread(0x0101, 0x01, 0x00, func_22_911E)
    Sleep(400)

    CreateThread(0x0102, 0x01, 0x00, func_21_9102)
    Sleep(400)

    CreateThread(0x00F9, 0x01, 0x00, func_23_913A)
    WaitForThreadExit(0x010B, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x010B,
        (
            '#0090400235V#415F#4S#6P各位！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000F, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0010, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0011, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0014, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0015, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0012, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0013, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0016, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_7CD5')
    def lambda_7CD5():
        ChrTurnDirection(0x00FE, 0x010B, 500)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_7CD5)

    Sleep(50)

    @scena.Lambda('lambda_7CE8')
    def lambda_7CE8():
        ChrTurnDirection(0x00FE, 0x010B, 500)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_7CE8)

    Sleep(50)

    @scena.Lambda('lambda_7CFB')
    def lambda_7CFB():
        ChrTurnDirection(0x00FE, 0x010B, 500)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_7CFB)

    Sleep(50)

    @scena.Lambda('lambda_7D0E')
    def lambda_7D0E():
        ChrTurnDirection(0x00FE, 0x010B, 500)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_7D0E)

    Sleep(50)

    @scena.Lambda('lambda_7D21')
    def lambda_7D21():
        ChrTurnDirection(0x00FE, 0x010B, 500)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_7D21)

    Sleep(50)

    @scena.Lambda('lambda_7D34')
    def lambda_7D34():
        ChrTurnDirection(0x00FE, 0x010B, 500)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_7D34)

    Sleep(50)

    @scena.Lambda('lambda_7D47')
    def lambda_7D47():
        ChrTurnDirection(0x00FE, 0x010B, 500)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_7D47)

    Sleep(50)

    @scena.Lambda('lambda_7D5A')
    def lambda_7D5A():
        ChrTurnDirection(0x00FE, 0x010B, 500)

        ExitThread()

    DispatchAsync(0x0016, 0x0001, lambda_7D5A)

    WaitForThreadExit(0x0010, 0x0001)

    ChrTalk(
        0x0010,
        (
            '#0290400236V#201F#5P什…什么…！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0300400237V#192F#5P乔丝特……\n',
            '还有这小子！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_7DC6')
    def lambda_7DC6():
        OP_67(0, 5660, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_7DC6)

    @scena.Lambda('lambda_7DDE')
    def lambda_7DDE():
        CameraMove(-84260, 0, -335810, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_7DDE)

    @scena.Lambda('lambda_7DF6')
    def lambda_7DF6():
        ChrWalkTo(0x00FE, -84470, 0, -336340, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0000, lambda_7DF6)

    Sleep(500)

    @scena.Lambda('lambda_7E16')
    def lambda_7E16():
        ChrWalkTo(0x00FE, -84080, 0, -335080, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0000, lambda_7E16)

    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0011,
        (
            '#1040400238V#5P小、小姐！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#1250400239V怎、怎么会在这里！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090400240V#415F#6P太、太好了……\n',
            '大家都平安无事吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090400241V现在就来救你们，等等哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0010, 0x0000)
    WaitForThreadExit(0x000F, 0x0000)

    ChrTalk(
        0x0010,
        (
            '#0290400242V#203F#5P救、救我们……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290400243V#201F……喂，约修亚！\n',
            '到底怎么回事啊！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290400244V为什么连你们\n',
            '都来到这个浮游都市了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020400245V#1042F#6P嗯，其实……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '向空贼们简单地说明了之前的经过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x000F,
        (
            '#0300400246V#490F#5P原来如此……\n',
            '还有这种事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0290400247V#204F#5P我说啊，乔丝特……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290400248V#206F我们可是为了掩护你逃走\n',
            '才会被捕的，你难道不知道吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290400249V可你现在却又……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090400250V#214F#6P别、别自作主张了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090400251V我才不想抛下大家，\n',
            '自己一个人得救！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090400252V与其这样的话，\n',
            '我宁可和哥哥们一起被关在这里！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0290400253V#201F#5P笨蛋，你是女人吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290400254V总该稍微担心一下\n',
            '自己的人身安全啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090400255V#216F#6P这、这么说太狡猾了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090400256V#215F吉尔哥你\n',
            '总是在这种时候\n',
            '才把我当女人对待！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_825A',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    Jump('loc_8298')

    def _loc_825A(): pass

    label('loc_825A')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8281',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    Jump('loc_8298')

    def _loc_8281(): pass

    label('loc_8281')

    OP_62(0x00F9, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    def _loc_8298(): pass

    label('loc_8298')

    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010400257V#1016F#6P（这、这个……\n',
            '兄妹之间的感情真好啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8327',
    )

    ChrTalk(
        0x0107,
        (
            '#0070400258V#067F#6P（嘿嘿……\n',
            '稍微有点羡慕呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_84E3')

    def _loc_8327(): pass

    label('loc_8327')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8370',
    )

    ChrTalk(
        0x0105,
        (
            '#0060400259V#1168F#6P（呵呵……\n',
            '稍微有点羡慕啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_84E3')

    def _loc_8370(): pass

    label('loc_8370')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_83C3',
    )

    ChrTalk(
        0x0109,
        (
            '#0180400260V#1061F#6P（哈哈……\n',
            '真是令人莞尔的兄妹吵架啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_84E3')

    def _loc_83C3(): pass

    label('loc_83C3')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8415',
    )

    ChrTalk(
        0x0103,
        (
            '#0030400261V#027F#6P（呵呵……\n',
            '真是令人莞尔的兄妹吵架啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_84E3')

    def _loc_8415(): pass

    label('loc_8415')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8465',
    )

    ChrTalk(
        0x0104,
        (
            '#0040400262V#031F#6P（呼……\n',
            '真是感情深厚的一对兄妹啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_84E3')

    def _loc_8465(): pass

    label('loc_8465')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_84A2',
    )

    ChrTalk(
        0x0106,
        (
            '#0050400263V#556F#6P（嘿………是啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_84E3')

    def _loc_84A2(): pass

    label('loc_84A2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_84E3',
    )

    ChrTalk(
        0x0108,
        (
            '#0080400264V#071F#6P（哈哈……\n',
            '感情真好呀。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_84E3(): pass

    label('loc_84E3')

    ChrTalk(
        0x000F,
        (
            '#0300400265V#192F#5P喂喂，别在这种地方\n',
            '吵架啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300400266V#199F你们两个真是……\n',
            '都什么时候了还耍小孩子脾气！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090400267V#215F#6P多伦哥……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0290400268V#207F#2P可、可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0300400269V#198F#5P既然来了，那也没办法了。\n',
            '只能一起逃出去了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300400270V#199F那么，小子……\n',
            '你要怎样把我们从这里弄出去？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_862D')
    def lambda_862D():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_862D)

    Sleep(50)

    @scena.Lambda('lambda_8640')
    def lambda_8640():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x010B, 0x0001, lambda_8640)

    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020340794V#1035F#6P……这个嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400272V#1042F看来这个能量障壁\n',
            '已经完全被锁上了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400273V要解除保护，\n',
            '说实话，确实很难。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0290400274V#204F#5P……原来如此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090400275V#216F#5P怎，怎么会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010400276V#1015F#5P嗯～那么\n',
            '不能用暴力弄开吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010400277V比如使用炸弹之类的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0102, 0, 400)

    ChrTalk(
        0x0102,
        (
            '#0020400278V#1043F#4P不行，这个能量障壁\n',
            '不是普通炸弹能伤得了的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400279V就算可以炸开，强大的爆破力\n',
            '可能也会危及到吉尔他们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400280V#1042F现在也只能去\n',
            '找一张最新密码卡来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010400281V#1004F#5P密码卡？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090400282V#415F#5P用、用那个\n',
            '就能解除这个障壁吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_88AD')
    def lambda_88AD():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_88AD)

    Sleep(100)

    @scena.Lambda('lambda_88C0')
    def lambda_88C0():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_88C0)

    @scena.Lambda('lambda_88CE')
    def lambda_88CE():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x010B, 0x0001, lambda_88CE)

    CameraMove(-84260, 0, -340520, 2000)

    ChrTalk(
        0x0102,
        (
            '#0020400283V#1040F#5P只要有那张密码卡，应该\n',
            '就能通过终端解除障壁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_8935')
    def lambda_8935():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_8935)

    Sleep(100)

    @scena.Lambda('lambda_8948')
    def lambda_8948():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_8948)

    CameraMove(-84260, 0, -335810, 1500)

    ChrTalk(
        0x0102,
        (
            '#0020400284V#1042F#4P我以前潜入时用的那张\n',
            '大概已经无法再使用了，\n',
            '所以需要找到最新的卡。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090400285V#212F#5P原、原来如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010400286V#1015F#5P那么，最新的密码卡\n',
            '放在哪里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020400287V#1035F#4P──前方区域的第二层。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400288V#1042F应该被保管在以前\n',
            '囚禁你的房间周边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010400289V#1002F#5P是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8AED',
    )

    ChrTalk(
        0x0107,
        (
            '#0070400290V#062F#6P看来赶快去\n',
            '调查为好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8C80')

    def _loc_8AED(): pass

    label('loc_8AED')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8B30',
    )

    ChrTalk(
        0x0105,
        (
            '#0060400291V#1162F#6P看来赶快去\n',
            '调查为好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8C80')

    def _loc_8B30(): pass

    label('loc_8B30')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8B71',
    )

    ChrTalk(
        0x0109,
        (
            '#0180400292V#1060F#6P那么，赶快\n',
            '去调查吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8C80')

    def _loc_8B71(): pass

    label('loc_8B71')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8BB5',
    )

    ChrTalk(
        0x0103,
        (
            '#0030400293V#027F#6P既然如此\n',
            '就赶快去调查吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8C80')

    def _loc_8BB5(): pass

    label('loc_8BB5')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8BFB',
    )

    ChrTalk(
        0x0104,
        (
            '#0040400294V#035F#6P呼，那就需要\n',
            '赶快去调查了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8C80')

    def _loc_8BFB(): pass

    label('loc_8BFB')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8C3F',
    )

    ChrTalk(
        0x0106,
        (
            '#0050400295V#051F#6P既然如此\n',
            '就赶快去调查吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8C80')

    def _loc_8C3F(): pass

    label('loc_8C3F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8C80',
    )

    ChrTalk(
        0x0108,
        (
            '#0080400296V#070F#6P既然如此\n',
            '就赶快去调查吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8C80(): pass

    label('loc_8C80')

    @scena.Lambda('lambda_8C86')
    def lambda_8C86():
        ChrSetDirection(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x010B, 0x0001, lambda_8C86)

    Sleep(50)

    @scena.Lambda('lambda_8C99')
    def lambda_8C99():
        ChrSetDirection(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_8C99)

    Sleep(50)

    @scena.Lambda('lambda_8CAC')
    def lambda_8CAC():
        ChrSetDirection(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_8CAC)

    Sleep(50)

    @scena.Lambda('lambda_8CBF')
    def lambda_8CBF():
        ChrSetDirection(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_8CBF)

    WaitForThreadExit(0x010B, 0x0001)
    Sleep(500)

    ChrTalk(
        0x010B,
        (
            '#0090400297V#214F#6P吉尔哥！多伦哥！\n',
            '还有大家！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090400298V委屈你们\n',
            '再耐心等等吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090400299V我们会马上找到密码卡\n',
            '回来的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0290400300V#203F#5P唉……没办法了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0300400301V#198F#5P小子……\n',
            '还有游击士的小姑娘。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300400302V#490F麻烦你们了，\n',
            '可别让那个冒失鬼乱来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020400303V#1040F#6P啊啊，交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010400304V#1006F#6P嗯，我们会\n',
            '管好她的，放心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x010B, 0x0101, 400)
    Sleep(300)

    ChrTalk(
        0x010B,
        (
            '#0090400305V#210F#2P哼，哼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090400306V你明明比我还莽撞无脑很多，\n',
            '竟然还敢说那种话啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x010B, 400)

    ChrTalk(
        0x0101,
        (
            '#0010400307V#1019F#6P你，你说什么～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0102, 270, 400)

    ChrTalk(
        0x0102,
        (
            '#0020400308V#1052F#2P好了好了，适可而止。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400309V#1042F──那么，\n',
            '马上返回出口附近吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400310V要去前方区域第２层\n',
            '需要使用反方向\n',
            '的升降梯呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x010B, 0x0102, 400)

    ChrTalk(
        0x010B,
        (
            '#0090400311V#212F#5P知、知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010400312V#1006F#5P那么，去吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(-87640, 0, -336030, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, -87640, 0, -336030, 180)
    ChrSetPos(0x0001, -87640, 0, -336030, 180)
    ChrSetPos(0x0002, -87640, 0, -336030, 180)
    ChrSetPos(0x0003, -87640, 0, -336030, 180)
    ChrSetPos(0x000F, -84180, 0, -335080, 270)
    ChrSetDirection(0x000F, 270, 0)
    CreateThread(0x000F, 0x00, 0x00, func_02_9CA)
    CreateThread(0x0010, 0x00, 0x00, func_02_9CA)
    OP_4B(0x000F, 255)
    OP_4B(0x0010, 255)
    OP_4B(0x0011, 255)
    OP_4B(0x0014, 255)
    OP_4B(0x0015, 255)
    OP_4B(0x0012, 255)
    OP_4B(0x0013, 255)
    OP_4B(0x0016, 255)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x0444, 3, 0x2223))
    OP_28(0x009E, 0x01, 0x0020)
    OP_28(0x009E, 0x01, 0x0040)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0020 offset: 0x90E6
@scena.Code('func_20_90E6')
def func_20_90E6():
    ChrWalkTo(0x00FE, -85690, 0, -336620, 5000, 0x00)
    ChrSetDirection(0x00FE, 45, 400)

    Return()

# id: 0x0021 offset: 0x9102
@scena.Code('func_21_9102')
def func_21_9102():
    ChrWalkTo(0x00FE, -86080, 0, -337750, 3000, 0x00)
    ChrSetDirection(0x00FE, 45, 400)

    Return()

# id: 0x0022 offset: 0x911E
@scena.Code('func_22_911E')
def func_22_911E():
    ChrWalkTo(0x00FE, -86830, 0, -336420, 3000, 0x00)
    ChrSetDirection(0x00FE, 45, 400)

    Return()

# id: 0x0023 offset: 0x913A
@scena.Code('func_23_913A')
def func_23_913A():
    ChrWalkTo(0x00FE, -87770, 0, -337880, 3000, 0x00)
    ChrSetDirection(0x00FE, 45, 400)

    Return()

# id: 0x0024 offset: 0x9156
@scena.Code('func_24_9156')
def func_24_9156():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0444, 5, 0x2225)),
            Expr.Return,
        ),
        'loc_9164',
    )

    Call(0, 0x002D)

    Jump('loc_91AE')

    def _loc_9164(): pass

    label('loc_9164')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 0, 0x2228)),
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 1, 0x2229)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 2, 0x222A)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 3, 0x222B)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_917E',
    )

    Call(0, 0x002D)

    Jump('loc_91AE')

    def _loc_917E(): pass

    label('loc_917E')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '终端被锁定了。\n',
            '似乎需要密码卡。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    def _loc_91AE(): pass

    label('loc_91AE')

    TalkEnd(0x00FF)

    Return()

# id: 0x0025 offset: 0x91B2
@scena.Code('func_25_91B2')
def func_25_91B2():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0444, 5, 0x2225)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_95AC',
    )

    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_91DF',
    )

    Call(0, 0x003A)
    Call(0, 0x003B)
    FadeIn(0, 0)
    Sleep(100)

    def _loc_91DF(): pass

    label('loc_91DF')

    Fade(1000)
    CameraMove(-127570, 0, -60040, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0102, -127670, 0, -58950, 90)
    ChrSetPos(0x0101, -126930, 0, -59970, 0)
    ChrSetPos(0x010B, -128550, 0, -59930, 45)
    ChrSetPos(0x00F9, -127840, 0, -61020, 0)
    OP_0D()
    OP_6F(0x0025, 0)
    OP_70(0x0025, 60)
    PlaySE(43, 0x00, 0x64)
    OP_73(0x0025)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['安全卡片']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['安全卡片'], 1)
    UnlockAchievement(0x02, 0x020E, 0x00)

    ChrTalk(
        0x010B,
        (
            '#0090400320V#213F#6P难道那就是……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010400321V#1004F#4P刚刚说的\n',
            '最新的密码卡？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0102, 180, 400)
    Sleep(300)

    ChrTalk(
        0x0102,
        (
            '#0020400322V#1040F#5P嗯……没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400323V通过这个牢房中的终端\n',
            '就能解除障壁哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010271052V#1018F#4P太好了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090400325V#415F#6P太好了……这下就……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9421',
    )

    ChrTalk(
        0x0107,
        (
            '#0070400326V#067F嘿嘿……那么，\n',
            '赶快返回牢房吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_959E')

    def _loc_9421(): pass

    label('loc_9421')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9463',
    )

    ChrTalk(
        0x0105,
        (
            '#0060400327V#1168F呵呵……\n',
            '赶快返回牢房吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_959E')

    def _loc_9463(): pass

    label('loc_9463')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_94A3',
    )

    ChrTalk(
        0x0109,
        (
            '#0180400328V#1061F那么，马上\n',
            '返回牢房吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_959E')

    def _loc_94A3(): pass

    label('loc_94A3')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_94E4',
    )

    ChrTalk(
        0x0103,
        (
            '#0030400329V#021F呵呵……\n',
            '赶快返回牢房吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_959E')

    def _loc_94E4(): pass

    label('loc_94E4')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9525',
    )

    ChrTalk(
        0x0104,
        (
            '#0040400330V#031F呼，那么尽快\n',
            '返回牢房吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_959E')

    def _loc_9525(): pass

    label('loc_9525')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9562',
    )

    ChrTalk(
        0x0106,
        (
            '#0050400331V#051F好～马上\n',
            '返回牢房吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_959E')

    def _loc_9562(): pass

    label('loc_9562')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_959E',
    )

    ChrTalk(
        0x0108,
        (
            '#0080400332V#070F好……\n',
            '马上返回牢房吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_959E(): pass

    label('loc_959E')

    SetScenaFlags(ScenaFlag(0x0444, 5, 0x2225))
    OP_28(0x009E, 0x01, 0x0080)
    EventEnd(0x00)

    Jump('loc_95E5')

    def _loc_95AC(): pass

    label('loc_95AC')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱里什么也没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)
    def _loc_95E5(): pass

    label('loc_95E5')

    Return()

# id: 0x0026 offset: 0x95E6
@scena.Code('func_26_95E6')
def func_26_95E6():
    EventBegin(0x00)
    FadeIn(0, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_9606',
    )

    Call(0, 0x003A)
    Call(0, 0x003B)

    def _loc_9606(): pass

    label('loc_9606')

    CameraMove(-42070, 0, 75240, 0)
    OP_67(0, 7490, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, -42880, 0, 76490, 180)
    ChrSetPos(0x0102, -42880, 0, 76490, 180)
    ChrSetPos(0x010B, -42880, 0, 76490, 180)
    ChrSetPos(0x00F9, -42880, 0, 76490, 180)
    FadeIn(2000, 0)
    OP_0D()
    PlaySE(14, 0x00, 0x64)
    Sleep(1000)

    OP_72(0x0012, 0x0010)
    OP_72(0x0012, 0x0020)
    OP_6F(0x0012, 0)
    OP_70(0x0012, 15)
    OP_73(0x0012)
    Sleep(300)

    @scena.Lambda('lambda_96C1')
    def lambda_96C1():
        CameraMove(-42610, 0, 71440, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_96C1)

    @scena.Lambda('lambda_96D9')
    def lambda_96D9():
        OP_67(0, 6710, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_96D9)

    CreateThread(0x0101, 0x00, 0x00, func_27_98DF)
    Sleep(700)

    CreateThread(0x0102, 0x00, 0x00, func_28_9913)
    Sleep(600)

    CreateThread(0x010B, 0x00, 0x00, func_29_9943)
    Sleep(600)

    CreateThread(0x00F9, 0x00, 0x00, func_2A_9973)
    Sleep(1000)

    OP_71(0x0012, 0x0010)
    OP_6F(0x0012, 15)
    OP_70(0x0012, 0)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x00F9, 0x0000)
    ChrSetDirection(0x0101, 0, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010400313V#1015F#6P嗯，这一带的确是\n',
            '我当初被监禁的区域呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020400314V#1035F#5P嗯，是前方区域的第２层。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400315V#1040F也是用来向向猎兵们\n',
            '传达作战方案的会议室。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400316V最新的密码卡\n',
            '应该被保管在这附近。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x010B, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x010B,
        (
            '#0090400317V#212F#5P那、那么\n',
            '赶快调查看看吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x010B, 400)

    ChrTalk(
        0x0101,
        (
            '#0010400318V#1007F#6P好好，知道啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010400319V#1006F总之先把房间\n',
            '一个个都调查一遍吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0456, 2, 0x22B2))
    EventEnd(0x00)

    Return()

# id: 0x0027 offset: 0x98DF
@scena.Code('func_27_98DF')
def func_27_98DF():
    ChrWalkTo(0x00FE, -43170, 0, 69480, 2000, 0x00)
    ChrSetDirection(0x00FE, 135, 400)
    Sleep(500)

    ChrSetDirection(0x00FE, 225, 400)
    Sleep(500)

    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x0028 offset: 0x9913
@scena.Code('func_28_9913')
def func_28_9913():
    ChrWalkTo(0x00FE, -43200, 0, 73250, 2000, 0x00)
    ChrWalkTo(0x00FE, -44090, 0, 70670, 2000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x0029 offset: 0x9943
@scena.Code('func_29_9943')
def func_29_9943():
    ChrWalkTo(0x00FE, -43200, 0, 73250, 2000, 0x00)
    ChrWalkTo(0x00FE, -41900, 0, 70930, 2000, 0x00)
    ChrTurnDirection(0x00FE, 0x0101, 400)

    Return()

# id: 0x002A offset: 0x9973
@scena.Code('func_2A_9973')
def func_2A_9973():
    ChrWalkTo(0x00FE, -42920, 0, 71940, 2000, 0x00)

    Return()

# id: 0x002B offset: 0x9988
@scena.Code('func_2B_9988')
def func_2B_9988():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            (Expr.TestScenaFlags, ScenaFlag(0x0444, 6, 0x2226)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_A717',
    )

    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_99B9',
    )

    Call(0, 0x003A)
    Call(0, 0x003B)
    FadeIn(0, 0)
    Sleep(100)

    def _loc_99B9(): pass

    label('loc_99B9')

    Fade(1000)
    CameraMove(-37810, 0, -66450, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2820, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, -37980, 0, -67260, 90)
    ChrSetPos(0x0102, -38640, 0, -66330, 90)
    ChrSetPos(0x010B, -39140, 0, -67430, 90)
    ChrSetPos(0x00F9, -39800, 0, -66450, 90)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010400333V#1004F#6P咦，这个升降梯是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020400334V#1042F#5P是在『圣堂』和『引擎室』\n',
            '之间用来移动的升降梯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400335V由于要进行声纹模式的认证，\n',
            '所以只有『执行者』以上的人才能使用。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400336V#1035F看来只有放弃这里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010400337V#1007F#4P是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x010B, 0x0102, 400)
    Sleep(300)

    ChrTalk(
        0x010B,
        (
            '#0090400338V#213F#6P……对了，\n',
            '声纹模式是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x010B, 400)
    Sleep(300)

    ChrTalk(
        0x0102,
        (
            '#0020400339V#1040F#5P每个人的声音频率\n',
            '都是不同的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400340V由机械对声音进行识别，\n',
            '借此来判别是否有资格……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400341V似乎就是这样的装置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090400342V#414F#6P原、原来如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010400343V#1016F#4P好像懂了，\n',
            '又好像不懂……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9DF7',
    )

    ChrTalk(
        0x0107,
        (
            '#0070400344V#561F#6P不过，真是高超的技术啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070400345V#063F……对了，约修亚哥哥。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070400346V这艘飞船和人形兵器\n',
            '究竟都是谁制造的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020400347V#1035F#5P这个啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400348V#1042F听说是\n',
            '『蛇之使徒』之一的\n',
            '诺华提斯博士…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400349V结社使用的导力机械，\n',
            '全都是由那个博士所率领的\n',
            '『十三工房』开发出来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A5CD')

    def _loc_9DF7(): pass

    label('loc_9DF7')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9F47',
    )

    ChrTalk(
        0x0105,
        (
            '#0060400350V#1167F#6P真的是很高超的技术……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060400351V#1162F……对了，约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060400352V这艘飞船和人形兵器\n',
            '究竟都是谁制造的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020400347V#1035F#5P这个啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400348V#1042F听说是\n',
            '『蛇之使徒』之一的\n',
            '诺华提斯博士…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400349V结社使用的导力机械，\n',
            '全都是由那个博士所率领的\n',
            '『十三工房』开发出来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A5CD')

    def _loc_9F47(): pass

    label('loc_9F47')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A095',
    )

    ChrTalk(
        0x0109,
        (
            '#0180400356V#1068F#6P真是高超的技术啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180400357V#1063F……对了，约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180400358V这艘飞船和人形兵器\n',
            '究竟都是谁制造的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020400359V#1035F#5P这个啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400360V#1042F听说是\n',
            '『蛇之使徒』之一的\n',
            '诺华提斯博士…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400361V结社使用的导力机械，\n',
            '全都是由那个博士所率领的\n',
            '『十三工房』开发出来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A5CD')

    def _loc_A095(): pass

    label('loc_A095')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A1E1',
    )

    ChrTalk(
        0x0103,
        (
            '#0030400362V#025F#6P真是高超的技术啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030400363V#022F……对了，约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030400364V这艘飞船和人形兵器\n',
            '究竟都是谁制造的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020400359V#1035F#5P这个啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400360V#1042F听说是\n',
            '『蛇之使徒』之一的\n',
            '诺华提斯博士…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400361V结社使用的导力机械，\n',
            '全都是由那个博士所率领的\n',
            '『十三工房』开发出来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A5CD')

    def _loc_A1E1(): pass

    label('loc_A1E1')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A329',
    )

    ChrTalk(
        0x0104,
        (
            '#0040400368V#035F#6P真是高超的技术啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040400369V#030F……对了约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040400370V这艘飞船和人形兵器\n',
            '究竟都是谁制造的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020400359V#1035F#5P这个啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400360V#1042F听说是\n',
            '『蛇之使徒』之一的\n',
            '诺华提斯博士…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400361V结社使用的导力机械，\n',
            '全都是由那个博士所率领的\n',
            '『十三工房』开发出来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A5CD')

    def _loc_A329(): pass

    label('loc_A329')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A484',
    )

    ChrTalk(
        0x0106,
        (
            '#0050400374V#551F#6P真是的，到处都是一些\n',
            '古怪的小玩意……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050400375V#555F……喂，约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050400376V这艘飞船和人形兵器\n',
            '究竟都是谁制造的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020400359V#1035F#5P这个啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400360V#1042F听说是\n',
            '『蛇之使徒』之一的\n',
            '诺华提斯博士…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400361V结社使用的导力机械，\n',
            '全都是由那个博士所率领的\n',
            '『十三工房』开发出来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A5CD')

    def _loc_A484(): pass

    label('loc_A484')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A5CD',
    )

    ChrTalk(
        0x0108,
        (
            '#0080400380V#074F#6P相当了不起的技术呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080400381V#072F……对了，约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080400382V这艘飞船和人形兵器\n',
            '究竟都是谁制造的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020400359V#1035F#5P这个啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400360V#1042F听说是\n',
            '『蛇之使徒』之一的\n',
            '诺华提斯博士…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400361V结社使用的导力机械，\n',
            '全都是由那个博士所率领的\n',
            '『十三工房』开发出来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A5CD(): pass

    label('loc_A5CD')

    ChrTalk(
        0x010B,
        (
            '#0090400386V#212F#6P『十三工房』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010400387V#1007F#4P嗯……\n',
            '虽然不知道是个怎样的人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010400388V#1019F但感觉他好像比拉赛尔博士\n',
            '还要更加疯狂的样子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0102, 180, 400)
    Sleep(300)

    ChrTalk(
        0x0102,
        (
            '#0020400389V#1043F#5P疯狂吗……\n',
            '老实说，是个神秘莫测的人哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400390V#1035F……不过包括教授在内，\n',
            '『蛇之使徒』全体人员也都是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0444, 6, 0x2226))
    EventEnd(0x00)

    Jump('loc_A768')

    def _loc_A717(): pass

    label('loc_A717')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            (Expr.TestScenaFlags, ScenaFlag(0x0444, 6, 0x2226)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_A768',
    )

    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '升降机的门牢牢地关着',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    def _loc_A768(): pass

    label('loc_A768')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0383, 5, 0x1C1D)),
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_A7B3',
    )

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '升降机的门牢牢地关着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    def _loc_A7B3(): pass

    label('loc_A7B3')

    Return()

# id: 0x002C offset: 0xA7B4
@scena.Code('func_2C_A7B4')
def func_2C_A7B4():
    If(
        (
            (Expr.PushValueByIndex, 0x13),
            (Expr.PushLong, 0x410),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A7C1',
    )

    Return()

    def _loc_A7C1(): pass

    label('loc_A7C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 0, 0x2228)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 1, 0x2229)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 2, 0x222A)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 3, 0x222B)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_A83F',
    )

    If(
        (
            (Expr.GetChrWork, 0x0, 0x1),
            (Expr.PushLong, 0x151E4),
            Expr.Neg,
            Expr.Leq,
            (Expr.GetChrWork, 0x0, 0x1),
            (Expr.PushLong, 0x159B4),
            Expr.Neg,
            Expr.Geq,
            Expr.Nez64,
            (Expr.GetChrWork, 0x0, 0x3),
            (Expr.PushLong, 0x539E4),
            Expr.Neg,
            Expr.Leq,
            Expr.Nez64,
            (Expr.GetChrWork, 0x0, 0x3),
            (Expr.PushLong, 0x53FC0),
            Expr.Neg,
            Expr.Geq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_A83E',
    )

    MapSetFlags(0x00000080)
    OP_C0(0x01, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    Sleep(200)

    Call(0, 0x002D)

    Jump('loc_A83F')

    def _loc_A83E(): pass

    label('loc_A83E')

    Return()

    def _loc_A83F(): pass

    label('loc_A83F')

    Return()

# id: 0x002D offset: 0xA840
@scena.Code('func_2D_A840')
def func_2D_A840():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_A857',
    )

    Call(0, 0x003A)
    Call(0, 0x003B)

    def _loc_A857(): pass

    label('loc_A857')

    Fade(1000)
    CameraMove(-86740, 0, -342830, 0)
    OP_67(0, 7350, -10000, 0)
    CameraSetDistance(3040, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, -88010, 0, -343970, 90)
    ChrSetPos(0x0102, -87600, 0, -343010, 90)
    ChrSetPos(0x010B, -88360, 0, -342220, 90)
    ChrSetPos(0x00F9, -88850, 0, -343260, 90)
    OP_0D()
    Sleep(500)

    FadeIn(0, 0)
    Sleep(100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 0, 0x2228)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 1, 0x2229)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 2, 0x222A)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 3, 0x222B)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_A95E',
    )

    PlaySE(156, 0x00, 0x64)
    Sleep(500)

    PlaySE(157, 0x00, 0x64)
    OP_71(0x0023, 0x0004)
    Sleep(100)

    OP_72(0x0024, 0x0004)
    Sleep(1000)

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('合成音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#3700400501V──认证完毕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_A95E(): pass

    label('loc_A95E')

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('合成音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#3700400502V请选择想解除锁定的\n',
            '障壁号码。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
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

    SetMessageWindowPos(-1, 50, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            0x18,
            (TxtCtl.SetColor, 0x5),
            '输入想解除的障壁号码',
            TxtCtl.Enter,
        ),
    )

    Menu(
        0,
        -1,
        150,
        0,
        (
            TXT(0x00, '【１号】\n'),
            TXT(0x01, '【２号】\n'),
            TXT(0x02, '【３号】\n'),
            TXT(0x03, '【４号】\n'),
            TXT(0x04, '【５号】\n'),
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
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000001, 'loc_AA61'),
        (0x00000002, 'loc_AC18'),
        (0x00000003, 'loc_ADCF'),
        (0x00000004, 'loc_AF86'),
        (0x00000000, 'loc_B13D'),
        (-1, 'loc_B75F'),
    )

    def _loc_AA61(): pass

    label('loc_AA61')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 0, 0x2228)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AB44',
    )

    CameraMove(-83240, 0, -320400, 3000)
    PlaySE(170, 0x00, 0x64)
    Sleep(1000)

    OP_6F(0x0004, 0)
    OP_70(0x0004, 35)
    PlaySE(225, 0x00, 0x64)
    OP_73(0x0004)
    Sleep(500)

    OP_6F(0x0004, 35)
    OP_70(0x0004, 50)
    PlaySE(109, 0x00, 0x64)
    OP_73(0x0004)
    SetScenaFlags(ScenaFlag(0x0445, 0, 0x2228))
    Fade(500)
    CameraMove(-87600, 0, -342990, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, -87600, 0, -342990, 90)
    ChrSetPos(0x0001, -87600, 0, -342990, 90)
    ChrSetPos(0x0002, -87600, 0, -342990, 90)
    ChrSetPos(0x0003, -87600, 0, -342990, 90)
    OP_0D()
    EventEnd(0x00)

    Jump('loc_AC15')

    def _loc_AB44(): pass

    label('loc_AB44')

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('合成音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#3700400503V２号的锁定\n',
            '已经被解除。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Fade(500)
    CameraMove(-87600, 0, -342990, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, -87600, 0, -342990, 90)
    ChrSetPos(0x0001, -87600, 0, -342990, 90)
    ChrSetPos(0x0002, -87600, 0, -342990, 90)
    ChrSetPos(0x0003, -87600, 0, -342990, 90)
    OP_0D()
    EventEnd(0x00)
    TalkEnd(0x00FF)

    def _loc_AC15(): pass

    label('loc_AC15')

    Jump('loc_B75F')

    def _loc_AC18(): pass

    label('loc_AC18')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 1, 0x2229)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_ACFB',
    )

    CameraMove(-83240, 0, -309340, 3000)
    PlaySE(170, 0x00, 0x64)
    Sleep(1000)

    OP_6F(0x0005, 0)
    OP_70(0x0005, 35)
    PlaySE(225, 0x00, 0x64)
    OP_73(0x0005)
    Sleep(500)

    OP_6F(0x0005, 35)
    OP_70(0x0005, 50)
    PlaySE(109, 0x00, 0x64)
    OP_73(0x0005)
    SetScenaFlags(ScenaFlag(0x0445, 1, 0x2229))
    Fade(500)
    CameraMove(-87600, 0, -342990, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, -87600, 0, -342990, 90)
    ChrSetPos(0x0001, -87600, 0, -342990, 90)
    ChrSetPos(0x0002, -87600, 0, -342990, 90)
    ChrSetPos(0x0003, -87600, 0, -342990, 90)
    OP_0D()
    EventEnd(0x00)

    Jump('loc_ADCC')

    def _loc_ACFB(): pass

    label('loc_ACFB')

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('合成音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#3700400504V３号的锁定\n',
            '已经被解除。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Fade(500)
    CameraMove(-87600, 0, -342990, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, -87600, 0, -342990, 90)
    ChrSetPos(0x0001, -87600, 0, -342990, 90)
    ChrSetPos(0x0002, -87600, 0, -342990, 90)
    ChrSetPos(0x0003, -87600, 0, -342990, 90)
    OP_0D()
    EventEnd(0x00)
    TalkEnd(0x00FF)

    def _loc_ADCC(): pass

    label('loc_ADCC')

    Jump('loc_B75F')

    def _loc_ADCF(): pass

    label('loc_ADCF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 2, 0x222A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AEB2',
    )

    CameraMove(-83240, 0, -299470, 3000)
    PlaySE(170, 0x00, 0x64)
    Sleep(1000)

    OP_6F(0x0006, 0)
    OP_70(0x0006, 35)
    PlaySE(225, 0x00, 0x64)
    OP_73(0x0006)
    Sleep(500)

    OP_6F(0x0006, 35)
    OP_70(0x0006, 50)
    PlaySE(109, 0x00, 0x64)
    OP_73(0x0006)
    SetScenaFlags(ScenaFlag(0x0445, 2, 0x222A))
    Fade(500)
    CameraMove(-87600, 0, -342990, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, -87600, 0, -342990, 90)
    ChrSetPos(0x0001, -87600, 0, -342990, 90)
    ChrSetPos(0x0002, -87600, 0, -342990, 90)
    ChrSetPos(0x0003, -87600, 0, -342990, 90)
    OP_0D()
    EventEnd(0x00)

    Jump('loc_AF83')

    def _loc_AEB2(): pass

    label('loc_AEB2')

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('合成音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#3700400505V４号的锁定\n',
            '已经被解除。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Fade(500)
    CameraMove(-87600, 0, -342990, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, -87600, 0, -342990, 90)
    ChrSetPos(0x0001, -87600, 0, -342990, 90)
    ChrSetPos(0x0002, -87600, 0, -342990, 90)
    ChrSetPos(0x0003, -87600, 0, -342990, 90)
    OP_0D()
    EventEnd(0x00)
    TalkEnd(0x00FF)

    def _loc_AF83(): pass

    label('loc_AF83')

    Jump('loc_B75F')

    def _loc_AF86(): pass

    label('loc_AF86')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 3, 0x222B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B069',
    )

    SetScenaFlags(ScenaFlag(0x0445, 3, 0x222B))
    CameraMove(-83240, 0, -289000, 3000)
    PlaySE(170, 0x00, 0x64)
    Sleep(1000)

    OP_6F(0x0007, 0)
    OP_70(0x0007, 35)
    PlaySE(225, 0x00, 0x64)
    OP_73(0x0007)
    Sleep(500)

    OP_6F(0x0007, 35)
    OP_70(0x0007, 50)
    PlaySE(109, 0x00, 0x64)
    OP_73(0x0007)
    Fade(500)
    CameraMove(-87600, 0, -342990, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, -87600, 0, -342990, 90)
    ChrSetPos(0x0001, -87600, 0, -342990, 90)
    ChrSetPos(0x0002, -87600, 0, -342990, 90)
    ChrSetPos(0x0003, -87600, 0, -342990, 90)
    OP_0D()
    EventEnd(0x00)

    Jump('loc_B13A')

    def _loc_B069(): pass

    label('loc_B069')

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('合成音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#3700400506V５号的锁定\n',
            '已经被解除。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Fade(500)
    CameraMove(-87600, 0, -342990, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, -87600, 0, -342990, 90)
    ChrSetPos(0x0001, -87600, 0, -342990, 90)
    ChrSetPos(0x0002, -87600, 0, -342990, 90)
    ChrSetPos(0x0003, -87600, 0, -342990, 90)
    OP_0D()
    EventEnd(0x00)
    TalkEnd(0x00FF)

    def _loc_B13A(): pass

    label('loc_B13A')

    Jump('loc_B75F')

    def _loc_B13D(): pass

    label('loc_B13D')

    SetMessageWindowPos(-1, -1, -1, -1)
    CameraMove(-81410, 0, -332940, 2000)
    PlaySE(170, 0x00, 0x64)
    Sleep(1000)

    OP_6F(0x0003, 0)
    OP_70(0x0003, 35)
    PlaySE(225, 0x00, 0x64)
    OP_73(0x0003)
    Sleep(500)

    OP_6F(0x0003, 35)
    OP_70(0x0003, 50)
    PlaySE(109, 0x00, 0x64)
    OP_73(0x0003)
    OP_4A(0x000F, 0)

    @scena.Lambda('lambda_B19C')
    def lambda_B19C():
        ChrSetDirection(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_B19C)

    Sleep(20)

    OP_4A(0x0010, 0)

    @scena.Lambda('lambda_B1B3')
    def lambda_B1B3():
        ChrSetDirection(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_B1B3)

    Sleep(80)

    OP_4A(0x0011, 0)

    @scena.Lambda('lambda_B1CA')
    def lambda_B1CA():
        ChrSetDirection(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_B1CA)

    Sleep(10)

    OP_4A(0x0014, 0)

    @scena.Lambda('lambda_B1E1')
    def lambda_B1E1():
        ChrSetDirection(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_B1E1)

    Sleep(10)

    OP_4A(0x0015, 0)

    @scena.Lambda('lambda_B1F8')
    def lambda_B1F8():
        ChrSetDirection(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_B1F8)

    Sleep(70)

    OP_4A(0x0012, 0)

    @scena.Lambda('lambda_B20F')
    def lambda_B20F():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_B20F)

    Sleep(20)

    OP_4A(0x0013, 0)

    @scena.Lambda('lambda_B226')
    def lambda_B226():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_B226)

    Sleep(15)

    OP_4A(0x0016, 0)
    ChrSetDirection(0x0016, 270, 400)

    ChrTalk(
        0x0013,
        (
            '#0990400507V#2P哦哦……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#1270400508V#5P得、得救了……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_B288')
    def lambda_B288():
        CameraMove(-86260, 0, -337310, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_B288)

    @scena.Lambda('lambda_B2A0')
    def lambda_B2A0():
        OP_67(0, 4660, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_B2A0)

    @scena.Lambda('lambda_B2B8')
    def lambda_B2B8():
        CameraSetDistance(3450, 4000)

        ExitThread()

    DispatchAsync(0x010B, 0x0002, lambda_B2B8)

    @scena.Lambda('lambda_B2C8')
    def lambda_B2C8():
        OP_6C(45000, 4000)

        ExitThread()

    DispatchAsync(0x010B, 0x0003, lambda_B2C8)

    CreateThread(0x0010, 0x01, 0x00, func_30_B825)
    Sleep(500)

    CreateThread(0x000F, 0x01, 0x00, func_2F_B7E1)
    Sleep(600)

    CreateThread(0x0102, 0x02, 0x00, func_2E_B760)
    CreateThread(0x0016, 0x01, 0x00, func_31_B855)
    Sleep(700)

    CreateThread(0x0012, 0x01, 0x00, func_32_B899)
    Sleep(300)

    CreateThread(0x0013, 0x01, 0x00, func_33_B8DD)
    CreateThread(0x0014, 0x01, 0x00, func_34_B921)
    Sleep(400)

    CreateThread(0x0011, 0x01, 0x00, func_35_B951)
    Sleep(600)

    CreateThread(0x0015, 0x01, 0x00, func_36_B981)
    WaitForThreadExit(0x0102, 0x0002)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x010B,
        (
            '#0090400509V#415F#6P吉尔哥、多伦哥！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0290400510V#200F#5P乔丝特……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0300400511V#490F#5P嘿嘿……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300400512V看来也欠了你们一次\n',
            '很大的人情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020400513V#1040F#4P哪里，彼此彼此啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010400514V#1006F#4P是啊是啊，之前逃脱的时候\n',
            '可是多亏有你们的帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(172, 0x00, 0x64)
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B4B3',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_B4F1')

    def _loc_B4B3(): pass

    label('loc_B4B3')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B4DA',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_B4F1')

    def _loc_B4DA(): pass

    label('loc_B4DA')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_B4F1(): pass

    label('loc_B4F1')

    OP_62(0x010B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000F, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0010, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0012, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0013, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0016, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0011, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0014, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0015, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetDirection(0x010B, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010400515V#1005F糟糕……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020400516V#1035F#4P看来我们的动向\n',
            '完全都在他们的掌握之中……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020400517V#1042F各位，赶快逃跑吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090400518V#210F#5P嗯、嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0290400519V#201F#5P好……\n',
            '马上逃跑吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000F, 45, 400)
    ChrSetDirection(0x0014, 225, 400)

    ChrTalk(
        0x000F,
        (
            '#0300400520V#196F#6P小子们，别拖拉！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    SetMessageWindowPos(150, 80, -1, -1)
    TalkSetChrName('空贼们')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0990400521V#5S遵命！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeOut(1000, 0, -1)
    OP_0D()
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C5702._SN', 101, 0, 0)
    IdleLoop()

    Jump('loc_B75F')

    def _loc_B75F(): pass

    label('loc_B75F')

    Return()

# id: 0x002E offset: 0xB760
@scena.Code('func_2E_B760')
def func_2E_B760():
    @scena.Lambda('lambda_B766')
    def lambda_B766():
        ChrWalkTo(0x00FE, -87770, 0, -339660, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x010B, 0x0001, lambda_B766)

    Sleep(300)

    @scena.Lambda('lambda_B786')
    def lambda_B786():
        ChrWalkTo(0x00FE, -87310, 0, -341030, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_B786)

    Sleep(300)

    @scena.Lambda('lambda_B7A6')
    def lambda_B7A6():
        ChrWalkTo(0x00FE, -89090, 0, -341770, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_B7A6)

    Sleep(300)

    @scena.Lambda('lambda_B7C6')
    def lambda_B7C6():
        ChrWalkTo(0x00FE, -88050, 0, -342470, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_B7C6)

    WaitForThreadExit(0x010B, 0x0001)

    Return()

# id: 0x002F offset: 0xB7E1
@scena.Code('func_2F_B7E1')
def func_2F_B7E1():
    ChrWalkTo(0x00FE, -83810, 0, -336030, 3000, 0x00)
    ChrWalkTo(0x00FE, -85900, 0, -336030, 3000, 0x00)
    ChrWalkTo(0x00FE, -88400, 0, -338210, 3000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x0030 offset: 0xB825
@scena.Code('func_30_B825')
def func_30_B825():
    ChrWalkTo(0x00FE, -85900, 0, -336030, 3000, 0x00)
    ChrWalkTo(0x00FE, -86980, 0, -338370, 3000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x0031 offset: 0xB855
@scena.Code('func_31_B855')
def func_31_B855():
    ChrWalkTo(0x00FE, -83810, 0, -336030, 4000, 0x00)
    ChrWalkTo(0x00FE, -85900, 0, -336030, 4000, 0x00)
    ChrWalkTo(0x00FE, -88760, 0, -336860, 4000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x0032 offset: 0xB899
@scena.Code('func_32_B899')
def func_32_B899():
    ChrWalkTo(0x00FE, -83810, 0, -336030, 4000, 0x00)
    ChrWalkTo(0x00FE, -85900, 0, -336030, 4000, 0x00)
    ChrWalkTo(0x00FE, -88130, 0, -335480, 4000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x0033 offset: 0xB8DD
@scena.Code('func_33_B8DD')
def func_33_B8DD():
    ChrWalkTo(0x00FE, -83810, 0, -336030, 4000, 0x00)
    ChrWalkTo(0x00FE, -85900, 0, -336030, 4000, 0x00)
    ChrWalkTo(0x00FE, -87530, 0, -336550, 4000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x0034 offset: 0xB921
@scena.Code('func_34_B921')
def func_34_B921():
    ChrWalkTo(0x00FE, -83810, 0, -336030, 4000, 0x00)
    ChrWalkTo(0x00FE, -86500, 0, -337030, 4000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x0035 offset: 0xB951
@scena.Code('func_35_B951')
def func_35_B951():
    ChrWalkTo(0x00FE, -83690, 0, -334890, 4000, 0x00)
    ChrWalkTo(0x00FE, -85140, 0, -336360, 4000, 0x00)
    ChrSetDirection(0x00FE, 225, 400)

    Return()

# id: 0x0036 offset: 0xB981
@scena.Code('func_36_B981')
def func_36_B981():
    ChrWalkTo(0x00FE, -84350, 0, -334980, 4000, 0x00)
    ChrSetDirection(0x00FE, 225, 400)

    Return()

# id: 0x0037 offset: 0xB99D
@scena.Code('func_37_B99D')
def func_37_B99D():
    ClearScenaFlags(ScenaFlag(0x0390, 1, 0x1C81))
    SetScenaFlags(ScenaFlag(0x0390, 2, 0x1C82))
    ClearScenaFlags(ScenaFlag(0x0390, 3, 0x1C83))
    ClearScenaFlags(ScenaFlag(0x0390, 4, 0x1C84))
    ClearScenaFlags(ScenaFlag(0x0390, 5, 0x1C85))
    ClearScenaFlags(ScenaFlag(0x0390, 6, 0x1C86))
    ClearScenaFlags(ScenaFlag(0x0390, 7, 0x1C87))
    ClearScenaFlags(ScenaFlag(0x0391, 0, 0x1C88))

    Return()

# id: 0x0038 offset: 0xB9B6
@scena.Code('func_38_B9B6')
def func_38_B9B6():
    ClearScenaFlags(ScenaFlag(0x0390, 1, 0x1C81))
    ClearScenaFlags(ScenaFlag(0x0390, 2, 0x1C82))
    SetScenaFlags(ScenaFlag(0x0390, 3, 0x1C83))
    ClearScenaFlags(ScenaFlag(0x0390, 4, 0x1C84))
    ClearScenaFlags(ScenaFlag(0x0390, 5, 0x1C85))
    ClearScenaFlags(ScenaFlag(0x0390, 6, 0x1C86))
    ClearScenaFlags(ScenaFlag(0x0390, 7, 0x1C87))
    ClearScenaFlags(ScenaFlag(0x0391, 0, 0x1C88))

    Return()

# id: 0x0039 offset: 0xB9CF
@scena.Code('func_39_B9CF')
def func_39_B9CF():
    ClearScenaFlags(ScenaFlag(0x0390, 1, 0x1C81))
    ClearScenaFlags(ScenaFlag(0x0390, 2, 0x1C82))
    ClearScenaFlags(ScenaFlag(0x0390, 3, 0x1C83))
    SetScenaFlags(ScenaFlag(0x0390, 4, 0x1C84))
    ClearScenaFlags(ScenaFlag(0x0390, 5, 0x1C85))
    ClearScenaFlags(ScenaFlag(0x0390, 6, 0x1C86))
    ClearScenaFlags(ScenaFlag(0x0390, 7, 0x1C87))
    ClearScenaFlags(ScenaFlag(0x0391, 0, 0x1C88))

    Return()

# id: 0x003A offset: 0xB9E8
@scena.Code('func_3A_B9E8')
def func_3A_B9E8():
    FadeOut(0, 0, -1)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
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
        (0x00000000, 'loc_BA62'),
        (0x00000001, 'loc_BA68'),
        (-1, 'loc_BA6E'),
    )

    def _loc_BA62(): pass

    label('loc_BA62')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_BA6E')

    def _loc_BA68(): pass

    label('loc_BA68')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_BA6E')

    def _loc_BA6E(): pass

    label('loc_BA6E')

    Return()

# id: 0x003B offset: 0xBA6F
@scena.Code('func_3B_BA6F')
def func_3B_BA6F():
    FadeOut(0, 0, -1)
    CameraMove(-107890, 0, -346700, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            ChrTable['乔丝特'],
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['雪拉扎德'],
            ChrTable['科洛丝'],
            ChrTable['奥利维尔'],
            ChrTable['提妲'],
            ChrTable['金'],
            ChrTable['凯文神父'],
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0)

    Return()

# id: 0x003C offset: 0xBB00
@scena.Code('func_3C_BB00')
def func_3C_BB00():
    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_AD('ED6_DT24/C_VIS251._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(500)

    OP_56(0x03)
    OP_AE(0x000001F4)
    TalkEnd(0x00FF)

    Return()

# id: 0x003D offset: 0xBB26
@scena.Code('func_3D_BB26')
def func_3D_BB26():
    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_AD('ED6_DT24/C_VIS252._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(500)

    OP_56(0x03)
    OP_AE(0x000001F4)
    TalkEnd(0x00FF)

    Return()

# id: 0x003E offset: 0xBB4C
@scena.Code('func_3E_BB4C')
def func_3E_BB4C():
    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_AD('ED6_DT24/C_VIS258._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(500)

    OP_56(0x03)
    OP_AE(0x000001F4)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

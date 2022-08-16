import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4136_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4136   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4136.x'
    header.mapIndex       = 1
    header.bgm            = 18
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/T4136._SN', 'ED6_DT01/T4136_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
            word_3A         = 186,
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
        ('ED6_DT07/CH01240._CH', 'ED6_DT07/CH01240P._CP'),
        ('ED6_DT07/CH01630._CH', 'ED6_DT07/CH01630P._CP'),
        ('ED6_DT07/CH01260._CH', 'ED6_DT07/CH01260P._CP'),
        ('ED6_DT07/CH01620._CH', 'ED6_DT07/CH01620P._CP'),
        ('ED6_DT07/CH02510._CH', 'ED6_DT07/CH02510P._CP'),
        ('ED6_DT07/CH02520._CH', 'ED6_DT07/CH02520P._CP'),
        ('ED6_DT07/CH02530._CH', 'ED6_DT07/CH02530P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH01310._CH', 'ED6_DT07/CH01310P._CP'),
        ('ED6_DT07/CH01380._CH', 'ED6_DT07/CH01380P._CP'),
        ('ED6_DT07/CH02110._CH', 'ED6_DT07/CH02110P._CP'),
        ('ED6_DT07/CH02120._CH', 'ED6_DT07/CH02120P._CP'),
        ('ED6_DT07/CH02130._CH', 'ED6_DT07/CH02130P._CP'),
        ('ED6_DT07/CH02070._CH', 'ED6_DT07/CH02070P._CP'),
        ('ED6_DT07/CH02350._CH', 'ED6_DT07/CH02350P._CP'),
        ('ED6_DT07/CH02030._CH', 'ED6_DT07/CH02030P._CP'),
        ('ED6_DT07/CH02100._CH', 'ED6_DT07/CH02100P._CP'),
        ('ED6_DT07/CH02200._CH', 'ED6_DT07/CH02200P._CP'),
        ('ED6_DT07/CH01540._CH', 'ED6_DT07/CH01540P._CP'),
        ('ED6_DT07/CH00010._CH', 'ED6_DT07/CH00010P._CP'),
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP'),
        ('ED6_DT07/CH01290._CH', 'ED6_DT07/CH01290P._CP'),
        ('ED6_DT06/CH20142._CH', 'ED6_DT06/CH20142P._CP'),
    ]

# id: 0x10001 offset: 0x16A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '卡露娜',
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
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '亚妮拉丝',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '库拉茨',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '克鲁茨',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '迪恩',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '雷斯',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '洛克',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵艾扎克',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0002,
        ),
        ScenaNpcData(
            name                = '士兵赛恩',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '士兵塔里斯',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '士兵拜安',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '士兵密克里亚',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '士兵格古',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '莱尔中尉',
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
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '贝伦中尉',
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
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '迪鲁队长',
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
            name                = '莱尔',
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
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            name                = '多伦',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '吉尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '乔丝特',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '朵洛希',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '克劳斯市长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '理查德上校',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '凯诺娜上尉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '洛伦斯少尉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '斯妮亚',
            x                   = -1850,
            z                   = 0,
            y                   = 13450,
            direction           = 197,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '科娜克',
            x                   = 1440,
            z                   = 0,
            y                   = 13450,
            direction           = 197,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '约修亚',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '奥利维尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '金',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
    )

# id: 0x10002 offset: 0x54A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x54A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x54A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 87000,
            triggerZ            = 0,
            triggerY            = 42860,
            triggerRange        = 800,
            actorX              = 87000,
            actorZ              = 1000,
            actorY              = 42860,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x002E,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -87000,
            triggerZ            = 0,
            triggerY            = 42860,
            triggerRange        = 800,
            actorX              = -87000,
            actorZ              = 1000,
            actorY              = 42860,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x002E,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 84200,
            triggerZ            = 0,
            triggerY            = 33000,
            triggerRange        = 800,
            actorX              = 84200,
            actorZ              = 1000,
            actorY              = 33000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x002F,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -84200,
            triggerZ            = 0,
            triggerY            = 33000,
            triggerRange        = 800,
            actorX              = -84200,
            actorZ              = 1000,
            actorY              = 33000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x002F,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 84200,
            triggerZ            = 0,
            triggerY            = 33000,
            triggerRange        = 800,
            actorX              = 84200,
            actorZ              = 1000,
            actorY              = 33000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0015,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -1710,
            triggerZ            = 0,
            triggerY            = 11500,
            triggerRange        = 400,
            actorX              = -1850,
            actorZ              = 1500,
            actorY              = 13450,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000C,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 1580,
            triggerZ            = 0,
            triggerY            = 11500,
            triggerRange        = 400,
            actorX              = 1440,
            actorZ              = 1500,
            actorY              = 13450,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x646
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_654',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_12_1EE0)

    def _loc_654(): pass

    label('loc_654')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_662',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, func_16_41DB)

    def _loc_662(): pass

    label('loc_662')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 4, 0x3FC)),
            Expr.Return,
        ),
        'loc_670',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    Event(0, func_18_4668)

    def _loc_670(): pass

    label('loc_670')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 5, 0x3FD)),
            Expr.Return,
        ),
        'loc_67E',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 5, 0x3FD))
    Event(0, func_19_4A6D)

    def _loc_67E(): pass

    label('loc_67E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 6, 0x3FE)),
            Expr.Return,
        ),
        'loc_68C',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 6, 0x3FE))
    Event(0, func_1A_53A7)

    def _loc_68C(): pass

    label('loc_68C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 7, 0x3FF)),
            Expr.Return,
        ),
        'loc_69A',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 7, 0x3FF))
    Event(0, func_1C_5B35)

    def _loc_69A(): pass

    label('loc_69A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007E, 0, 0x3F0)),
            Expr.Return,
        ),
        'loc_6A8',
    )

    ClearScenaFlags(ScenaFlag(0x007E, 0, 0x3F0))
    Event(0, func_1D_5D85)

    def _loc_6A8(): pass

    label('loc_6A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007E, 1, 0x3F1)),
            Expr.Return,
        ),
        'loc_6B6',
    )

    ClearScenaFlags(ScenaFlag(0x007E, 1, 0x3F1))
    Event(0, func_1F_686D)

    def _loc_6B6(): pass

    label('loc_6B6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007E, 2, 0x3F2)),
            Expr.Return,
        ),
        'loc_6C4',
    )

    ClearScenaFlags(ScenaFlag(0x007E, 2, 0x3F2))
    Event(0, func_23_8AEF)

    def _loc_6C4(): pass

    label('loc_6C4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007E, 3, 0x3F3)),
            Expr.Return,
        ),
        'loc_6D2',
    )

    ClearScenaFlags(ScenaFlag(0x007E, 3, 0x3F3))
    Event(0, func_25_A34E)

    def _loc_6D2(): pass

    label('loc_6D2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007E, 4, 0x3F4)),
            Expr.Return,
        ),
        'loc_6E0',
    )

    ClearScenaFlags(ScenaFlag(0x007E, 4, 0x3F4))
    Event(0, func_26_AA30)

    def _loc_6E0(): pass

    label('loc_6E0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007E, 5, 0x3F5)),
            Expr.Return,
        ),
        'loc_6EE',
    )

    ClearScenaFlags(ScenaFlag(0x007E, 5, 0x3F5))
    Event(0, func_27_BAD5)

    def _loc_6EE(): pass

    label('loc_6EE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007E, 6, 0x3F6)),
            Expr.Return,
        ),
        'loc_6FC',
    )

    ClearScenaFlags(ScenaFlag(0x007E, 6, 0x3F6))
    Event(0, func_2A_DB73)

    def _loc_6FC(): pass

    label('loc_6FC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007E, 7, 0x3F7)),
            Expr.Return,
        ),
        'loc_70A',
    )

    ClearScenaFlags(ScenaFlag(0x007E, 7, 0x3F7))
    Event(0, func_2B_DF12)

    def _loc_70A(): pass

    label('loc_70A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 0, 0x3F8)),
            Expr.Return,
        ),
        'loc_718',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 0, 0x3F8))
    Event(0, func_2C_E084)

    def _loc_718(): pass

    label('loc_718')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000065, 'loc_730'),
        (0x00000066, 'loc_730'),
        (0x0000006A, 'loc_74E'),
        (0x0000006F, 'loc_764'),
        (-1, 'loc_78D'),
    )

    def _loc_730(): pass

    label('loc_730')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 5, 0x635)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 2, 0x632)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 3, 0x633)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 4, 0x634)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_74B',
    )

    SetScenaFlags(ScenaFlag(0x00C6, 5, 0x635))
    Event(0, func_28_C5B3)

    def _loc_74B(): pass

    label('loc_74B')

    Jump('loc_78D')

    def _loc_74E(): pass

    label('loc_74E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 7, 0x60F)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_761',
    )

    SetScenaFlags(ScenaFlag(0x00C2, 0, 0x610))
    Event(0, func_13_200F)

    def _loc_761(): pass

    label('loc_761')

    Jump('loc_78D')

    def _loc_764(): pass

    label('loc_764')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 6, 0x636)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 5, 0x635)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_777',
    )

    SetScenaFlags(ScenaFlag(0x00C6, 6, 0x636))
    Event(0, func_29_DB66)

    def _loc_777(): pass

    label('loc_777')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 5, 0x625)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 4, 0x624)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_78A',
    )

    SetScenaFlags(ScenaFlag(0x00C4, 5, 0x625))
    Event(0, func_22_8AE2)

    def _loc_78A(): pass

    label('loc_78A')

    Jump('loc_78D')

    def _loc_78D(): pass

    label('loc_78D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 4, 0x61C)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 5, 0x61D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_79C',
    )

    Jump('loc_800')

    def _loc_79C(): pass

    label('loc_79C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 5, 0x61D)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7AB',
    )

    Jump('loc_800')

    def _loc_7AB(): pass

    label('loc_7AB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 5, 0x625)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7BA',
    )

    Jump('loc_800')

    def _loc_7BA(): pass

    label('loc_7BA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 1, 0x631)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 6, 0x636)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_800',
    )

    ChrClearFlags(0x0025, 0x0080)
    ChrClearFlags(0x0026, 0x0080)
    ChrSetPos(0x0025, 80420, 0, -63670, 0)
    ChrSetPos(0x0026, 80420, 0, -62320, 180)
    CreateThread(0x0025, 0x00, 0x00, func_02_902)
    CreateThread(0x0026, 0x00, 0x00, func_02_902)

    def _loc_800(): pass

    label('loc_800')

    Return()

# id: 0x0001 offset: 0x801
@scena.Code('func_01_801')
def func_01_801():
    OP_1B(0x00, 0x00, 0x002D)
    OP_64(0x02, 0x0001)
    OP_64(0x03, 0x0001)
    OP_71(0x0006, 0x0002)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 3, 0x61B)),
            Expr.Return,
        ),
        'loc_822',
    )

    OP_1B(0x05, 0x00, 0x0032)

    Jump('loc_84A')

    def _loc_822(): pass

    label('loc_822')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 7, 0x60F)),
            Expr.Return,
        ),
        'loc_835',
    )

    OP_72(0x0003, 0x0010)
    OP_65(0x02, 0x0001)

    Jump('loc_84A')

    def _loc_835(): pass

    label('loc_835')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 5, 0x60D)),
            Expr.Return,
        ),
        'loc_84A',
    )

    OP_1B(0x05, 0x00, 0x0032)
    OP_72(0x0003, 0x0010)
    OP_65(0x02, 0x0001)

    def _loc_84A(): pass

    label('loc_84A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 4, 0x61C)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 5, 0x61D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_863',
    )

    OP_1B(0x0B, 0x00, 0x0030)
    OP_1B(0x0C, 0x00, 0x0031)

    Jump('loc_8B0')

    def _loc_863(): pass

    label('loc_863')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 5, 0x61D)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_877',
    )

    OP_1B(0x0B, 0x00, 0x0030)

    Jump('loc_8B0')

    def _loc_877(): pass

    label('loc_877')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 5, 0x625)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_88B',
    )

    OP_1B(0x0B, 0x00, 0x0030)

    Jump('loc_8B0')

    def _loc_88B(): pass

    label('loc_88B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 1, 0x631)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 6, 0x636)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_89F',
    )

    OP_1B(0x0C, 0x00, 0x0031)

    Jump('loc_8B0')

    def _loc_89F(): pass

    label('loc_89F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 6, 0x636)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_8B0',
    )

    OP_1B(0x0B, 0x00, 0x0030)

    def _loc_8B0(): pass

    label('loc_8B0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 4, 0x61C)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 3, 0x61B)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_8C4',
    )

    OP_72(0x0003, 0x0010)

    Jump('loc_8C8')

    def _loc_8C4(): pass

    label('loc_8C4')

    OP_64(0x04, 0x0001)

    def _loc_8C8(): pass

    label('loc_8C8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 4, 0x624)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 3, 0x623)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_8DE',
    )

    OP_1B(0x02, 0x00, 0x0020)
    OP_1B(0x01, 0x00, 0x0021)

    def _loc_8DE(): pass

    label('loc_8DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 7, 0x60F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8F5',
    )

    OP_10(0x04, 0x01)
    OP_10(0x09, 0x01)
    OP_10(0x0D, 0x00)
    OP_10(0x0E, 0x00)

    Jump('loc_901')

    def _loc_8F5(): pass

    label('loc_8F5')

    OP_10(0x04, 0x00)
    OP_10(0x09, 0x00)
    OP_10(0x0D, 0x01)
    OP_10(0x0E, 0x01)

    def _loc_901(): pass

    label('loc_901')

    Return()

# id: 0x0002 offset: 0x902
@scena.Code('func_02_902')
def func_02_902():
    ExecExpressionWithValue(
        0x00FE,
        0x28,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

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
        'loc_932',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_A74')

    def _loc_932(): pass

    label('loc_932')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_94B',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_A74')

    def _loc_94B(): pass

    label('loc_94B')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_964',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_A74')

    def _loc_964(): pass

    label('loc_964')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_97D',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_A74')

    def _loc_97D(): pass

    label('loc_97D')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_996',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_A74')

    def _loc_996(): pass

    label('loc_996')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9AF',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_A74')

    def _loc_9AF(): pass

    label('loc_9AF')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9C8',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_A74')

    def _loc_9C8(): pass

    label('loc_9C8')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9E1',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_A74')

    def _loc_9E1(): pass

    label('loc_9E1')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9FA',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_A74')

    def _loc_9FA(): pass

    label('loc_9FA')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A13',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_A74')

    def _loc_A13(): pass

    label('loc_A13')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A2C',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_A74')

    def _loc_A2C(): pass

    label('loc_A2C')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A45',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_A74')

    def _loc_A45(): pass

    label('loc_A45')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A5E',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_A74')

    def _loc_A5E(): pass

    label('loc_A5E')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A74',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_A74(): pass

    label('loc_A74')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_A89',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_A74')

    def _loc_A89(): pass

    label('loc_A89')

    Return()

# id: 0x0003 offset: 0xA8A
@scena.Code('func_03_A8A')
def func_03_A8A():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#0020110128V#010F如果平静不下来的话，\n',
            '不如去和其他组的选手谈谈话，\n',
            '这样就能稍微让心情轻松一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110129V今天还不会和这边的小组对战嘛。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))
    Call(0, 0x0017)
    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0xB2C
@scena.Code('func_04_B2C')
def func_04_B2C():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 1, 0x631)),
            Expr.Return,
        ),
        'loc_C05',
    )

    ChrTalk(
        0x00FE,
        (
            '#0040110136V#030F哟，已经回来了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040110137V离比赛开始还有一段时间呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040110138V你们两人再到其他地方转转，\n',
            '好好放松一下嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110139V#509F……难得你会说些正经的话，\n',
            '感觉有点怪怪的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C7D')

    def _loc_C05(): pass

    label('loc_C05')

    ChrTalk(
        0x00FE,
        (
            '#0040110134V#035F呼，这种高亢的感觉……\n',
            '就像是歌剧快要开始一样呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040110135V那么，就让我更加沉醉吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))
    Call(0, 0x0017)

    def _loc_C7D(): pass

    label('loc_C7D')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0xC81
@scena.Code('func_05_C81')
def func_05_C81():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 1, 0x631)),
            Expr.Return,
        ),
        'loc_D24',
    )

    ChrTalk(
        0x00FE,
        (
            '#0080110132V#070F那么，该如何与毫无破绽的\n',
            '特务部队那些家伙们作战呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080110133V无论进攻还是防守，\n',
            '他们肯定会以那个队长\n',
            '为核心展开战斗吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DA2')

    def _loc_D24(): pass

    label('loc_D24')

    ChrTalk(
        0x00FE,
        (
            '#0080110130V#070F这样看来，\n',
            '不管哪一组都是很强的队伍呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080110131V嘿嘿，这次特地来到利贝尔，\n',
            '真是不虚此行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0002, 0, 0x10))
    Call(0, 0x0017)

    def _loc_DA2(): pass

    label('loc_DA2')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0xDA6
@scena.Code('func_06_DA6')
def func_06_DA6():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 5, 0x61D)),
            Expr.Return,
        ),
        'loc_E36',
    )

    ChrTalk(
        0x00FE,
        (
            '#0120110169V#851F呼，出了很多汗呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120110170V回去之后，\n',
            '一定要吃冰淇淋才行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120110171V#816F两位新人，你们也要加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F59')

    def _loc_E36(): pass

    label('loc_E36')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_EA6',
    )

    ChrTalk(
        0x00FE,
        (
            '#0120110165V#816F你们是作为金先生小组的成员\n',
            '登记参加比赛的吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120110166V真期待你们的表现啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F59')

    def _loc_EA6(): pass

    label('loc_EA6')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '#0120110163V#850F啊，两位新人！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110164V#001F啊，亚妮拉丝姐姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0120110165V#816F你们是为了协助金先生\n',
            '而登记参加比赛的吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120110166V真期待你们的表现啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F59(): pass

    label('loc_F59')

    Call(0, 0x0017)
    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0xF61
@scena.Code('func_07_F61')
def func_07_F61():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 5, 0x61D)),
            Expr.Return,
        ),
        'loc_FB1',
    )

    ChrTalk(
        0x00FE,
        (
            '#0320110159V#830F终于轮到你们了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320110160V好好加油吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1103')

    def _loc_FB1(): pass

    label('loc_FB1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_101E',
    )

    ChrTalk(
        0x00FE,
        (
            '#0320110161V#835F你们也在这个休息室啊，\n',
            '也就是说\n',
            '我们的对战要推迟了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320110162V有点遗憾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1103')

    def _loc_101E(): pass

    label('loc_101E')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '#0320110154V#831F呀，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320110155V你们也在这个休息室啊，\n',
            '也就是说我们的对战要推迟了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320110156V#835F有点遗憾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110157V#001F嗯，期待的心情又要延长了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0320110158V#830F呵呵，你还真敢说啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1103(): pass

    label('loc_1103')

    Call(0, 0x0017)
    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x110B
@scena.Code('func_08_110B')
def func_08_110B():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 5, 0x61D)),
            Expr.Return,
        ),
        'loc_1157',
    )

    ChrTalk(
        0x00FE,
        (
            '#0310110178V#820F我支持你们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0310110179V一口气解决吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1269')

    def _loc_1157(): pass

    label('loc_1157')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_11B5',
    )

    ChrTalk(
        0x00FE,
        (
            '#0310110174V#820F就让我们好好见识一下\n',
            '你们的功夫吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0310110175V一起加油吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1269')

    def _loc_11B5(): pass

    label('loc_11B5')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '#0310110172V#821F哟！\n',
            '你们果然来参加大会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110173V#000F嗯，多亏了前辈你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0310110174V#820F就让我们好好见识一下\n',
            '你们的功夫吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0310110175V一起加油吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1269(): pass

    label('loc_1269')

    Call(0, 0x0017)
    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x1271
@scena.Code('func_09_1271')
def func_09_1271():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 5, 0x61D)),
            Expr.Return,
        ),
        'loc_12E7',
    )

    ChrTalk(
        0x00FE,
        (
            '#0330110152V#840F只要保持平常心，\n',
            '你们就一定没问题的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330110153V这场比赛会怎么样，\n',
            '真是期待呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1513')

    def _loc_12E7(): pass

    label('loc_12E7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1362',
    )

    ChrTalk(
        0x00FE,
        (
            '#0330110150V#840F紧张的时候，\n',
            '呼吸就会变得又浅又急。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330110151V试着慢慢地进行深呼吸，\n',
            '就能缓解紧张感了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1513')

    def _loc_1362(): pass

    label('loc_1362')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '#0330110140V#840F啊，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110141V#008F嘿嘿，\n',
            '稍微有点安不下心来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0330110142V#840F紧张的时候，\n',
            '呼吸就会变得又浅又急。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330110143V试着慢慢地进行深呼吸，\n',
            '就能缓解紧张感了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110144V#505F原来是这样啊，慢慢地深呼吸……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110145V#500F吸～……呼～……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110146V吸～……呼～……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110147V#006F嗯，确实有点安心了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110148V谢谢，克鲁茨先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0330110149V#841F哈哈，没什么啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1513(): pass

    label('loc_1513')

    Call(0, 0x0017)
    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x151B
@scena.Code('func_0A_151B')
def func_0A_151B():
    Call(0, 0x000B)

    Return()

# id: 0x000B offset: 0x1520
@scena.Code('func_0B_1520')
def func_0B_1520():
    TalkBegin(0x0023)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_152D',
    )

    Jump('loc_1743')

    def _loc_152D(): pass

    label('loc_152D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_1537',
    )

    Jump('loc_1743')

    def _loc_1537(): pass

    label('loc_1537')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_1541',
    )

    Jump('loc_1743')

    def _loc_1541(): pass

    label('loc_1541')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_154B',
    )

    Jump('loc_1743')

    def _loc_154B(): pass

    label('loc_154B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_15A0',
    )

    ChrTalk(
        0x0023,
        (
            '不愧是决赛日，\n',
            '今天一早就看见很多客人在门外等候进场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0023,
        (
            '要加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1743')

    def _loc_15A0(): pass

    label('loc_15A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_15AA',
    )

    Jump('loc_1743')

    def _loc_15AA(): pass

    label('loc_15AA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_15EF',
    )

    ChrTalk(
        0x0023,
        (
            '今天若是胜利的话，\n',
            '明天就是决赛了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0023,
        (
            '要加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1743')

    def _loc_15EF(): pass

    label('loc_15EF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_1622',
    )

    ChrTalk(
        0x0023,
        (
            '进入休息室之后，\n',
            '请静候广播的通知。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1743')

    def _loc_1622(): pass

    label('loc_1622')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_1655',
    )

    ChrTalk(
        0x0023,
        (
            '进入休息室之后，\n',
            '请静候广播的通知。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1743')

    def _loc_1655(): pass

    label('loc_1655')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_169A',
    )

    ChrTalk(
        0x0023,
        (
            '今天的比赛\n',
            '已经全部结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0023,
        (
            '期待各位的再次光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1743')

    def _loc_169A(): pass

    label('loc_169A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_1743',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 7, 0x60F)),
            Expr.Return,
        ),
        'loc_16ED',
    )

    ChrTalk(
        0x0023,
        (
            '今天的比赛\n',
            '已经全部结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0023,
        (
            '期待着明天\n',
            '各位客人的光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1743')

    def _loc_16ED(): pass

    label('loc_16ED')

    ChrTalk(
        0x0023,
        (
            '如果想要观看预选赛，\n',
            '就请抓紧时间进场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0023,
        (
            '现在去的话，\n',
            '还可以赶上第七场比赛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1743(): pass

    label('loc_1743')

    TalkEnd(0x0023)

    Return()

# id: 0x000C offset: 0x1747
@scena.Code('func_0C_1747')
def func_0C_1747():
    Call(0, 0x000D)

    Return()

# id: 0x000D offset: 0x174C
@scena.Code('func_0D_174C')
def func_0D_174C():
    TalkBegin(0x0022)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1759',
    )

    Jump('loc_19A6')

    def _loc_1759(): pass

    label('loc_1759')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_1763',
    )

    Jump('loc_19A6')

    def _loc_1763(): pass

    label('loc_1763')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_176D',
    )

    Jump('loc_19A6')

    def _loc_176D(): pass

    label('loc_176D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_1777',
    )

    Jump('loc_19A6')

    def _loc_1777(): pass

    label('loc_1777')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_183A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_17D3',
    )

    ChrTalk(
        0x0022,
        (
            '唔，金先生的小组……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0022,
        (
            '今天也一样，\n',
            '请进入右边『苍之组』的休息室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1837')

    def _loc_17D3(): pass

    label('loc_17D3')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0022,
        (
            '决赛就要开始了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0022,
        (
            '唔，金先生的小组……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0022,
        (
            '今天也一样，\n',
            '请进入右边『苍之组』的休息室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1837(): pass

    label('loc_1837')

    Jump('loc_19A6')

    def _loc_183A(): pass

    label('loc_183A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_1844',
    )

    Jump('loc_19A6')

    def _loc_1844(): pass

    label('loc_1844')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_188D',
    )

    ChrTalk(
        0x0022,
        (
            '唔，金先生的小组……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0022,
        (
            '请进入右边\n',
            '『苍之组』的休息室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19A6')

    def _loc_188D(): pass

    label('loc_188D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_1897',
    )

    Jump('loc_19A6')

    def _loc_1897(): pass

    label('loc_1897')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_1900',
    )

    ChrTalk(
        0x0022,
        (
            '你们是金选手一行人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0022,
        (
            '唔～你们的休息室\n',
            '是在右边的『苍之组』休息室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0022,
        (
            '要加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19A6')

    def _loc_1900(): pass

    label('loc_1900')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_190A',
    )

    Jump('loc_19A6')

    def _loc_190A(): pass

    label('loc_190A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_19A6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 7, 0x60F)),
            Expr.Return,
        ),
        'loc_1963',
    )

    ChrTalk(
        0x0022,
        (
            '游击士组的成员\n',
            '还没有离开竞技场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0022,
        (
            '他们应该在\n',
            '北边的休息室里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19A6')

    def _loc_1963(): pass

    label('loc_1963')

    ChrTalk(
        0x0022,
        (
            '欢迎来到格兰竞技场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0022,
        (
            '要到观众席去观战，\n',
            '请走里面的楼梯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19A6(): pass

    label('loc_19A6')

    TalkEnd(0x0022)

    Return()

# id: 0x000E offset: 0x19AA
@scena.Code('func_0E_19AA')
def func_0E_19AA():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_1A3D',
    )

    ChrTalk(
        0x00FE,
        (
            '#0300110783V#190F那些家伙，\n',
            '到底对我做了些啥……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300110784V哼，无论如何，\n',
            '不教训一下那群卑鄙的家伙的话，\n',
            '我就憋着一肚子的气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B3B')

    def _loc_1A3D(): pass

    label('loc_1A3D')

    SetScenaFlags(ScenaFlag(0x0002, 1, 0x11))

    ChrTalk(
        0x00FE,
        (
            '#0300110779V#197F在柏斯发生的那件事\n',
            '我现在也不太记得了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300110780V想要强行回忆的话，\n',
            '头就像要裂开似的疼痛异常。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300110781V那些家伙，\n',
            '到底对我做了些啥……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300110782V#190F哼，无论如何，\n',
            '不教训一下那群卑鄙的家伙的话，\n',
            '我就憋着一肚子的气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B3B(): pass

    label('loc_1B3B')

    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x1B3F
@scena.Code('func_0F_1B3F')
def func_0F_1B3F():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 2, 0x12)),
            Expr.Return,
        ),
        'loc_1BCD',
    )

    ChrTalk(
        0x00FE,
        (
            '#0290110785V#200F我现在没有闲心来理会你们。\n',
            '　\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290110789V之前和你们打起来，\n',
            '其实就是因为情报部的那些家伙从中作梗。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C96')

    def _loc_1BCD(): pass

    label('loc_1BCD')

    SetScenaFlags(ScenaFlag(0x0002, 2, 0x12))

    ChrTalk(
        0x00FE,
        (
            '#0290110785V#200F我现在没有闲心来理会你们。\n',
            '　\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290110786V之前和你们打起来，\n',
            '其实就是因为情报部的那些家伙从中作梗。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290110787V虽然我没想要与你们和好，\n',
            '不过也没必要和你们在这里打架。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C96(): pass

    label('loc_1C96')

    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x1C9A
@scena.Code('func_10_1C9A')
def func_10_1C9A():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1D2F',
    )

    ChrTalk(
        0x00FE,
        (
            '#0090110795V#216F啊…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090110796V#215F不要在我面前瞎转悠了，\n',
            '快点走开，走开。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090110797V我、我会尽全力给你们看的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E37')

    def _loc_1D2F(): pass

    label('loc_1D2F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 3, 0x13)),
            Expr.Return,
        ),
        'loc_1D91',
    )

    ChrTalk(
        0x00FE,
        (
            '#0090110793V#214F什、什么呀？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090110794V别在这里晃来晃去的了，\n',
            '快点走开，走开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E37')

    def _loc_1D91(): pass

    label('loc_1D91')

    SetScenaFlags(ScenaFlag(0x0002, 3, 0x13))

    ChrTalk(
        0x00FE,
        (
            '#0090110790V#213F什、什么呀？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090110791V#214F不要在我面前瞎转悠了，\n',
            '快点走开，走开。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090110792V不止是情报部，\n',
            '早晚有一天会让你们\n',
            '也领教到本小姐的厉害！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E37(): pass

    label('loc_1E37')

    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0x1E3B
@scena.Code('func_11_1E3B')
def func_11_1E3B():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 4, 0x14)),
            Expr.Return,
        ),
        'loc_1E81',
    )

    ChrTalk(
        0x00FE,
        (
            '为了还关在地牢里面的同伴，\n',
            '能多赢一个就要多赢一个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EDC')

    def _loc_1E81(): pass

    label('loc_1E81')

    SetScenaFlags(ScenaFlag(0x0002, 4, 0x14))

    ChrTalk(
        0x00FE,
        (
            '我也相当痛恨那群穿黑衣服的人，\n',
            '为了还关在地牢里面的同伴，\n',
            '能多赢一个就要多赢一个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1EDC(): pass

    label('loc_1EDC')

    TalkEnd(0x00FE)

    Return()

# id: 0x0012 offset: 0x1EE0
@scena.Code('func_12_1EE0')
def func_12_1EE0():
    EventBegin(0x00)
    CameraMove(-570, 0, 16630, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 540, 0, 2040, 0)
    ChrSetPos(0x0102, -550, 0, 1580, 0)
    FadeIn(1000, 0)
    CameraMove(-40, 0, 2550, 5000)

    ChrTalk(
        0x0101,
        (
            '#0010100894V#004F哇……\n',
            '又是这么豪华的房间啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100895V#010F这里是正门大厅吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100896V看起来，观众席应该在上面二层。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100897V#006F嗯，去看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x0013 offset: 0x200F
@scena.Code('func_13_200F')
def func_13_200F():
    EventBegin(0x00)
    FadeIn(2000, 0)
    CameraMove(-88340, 0, -60660, 0)
    ChrSetPos(0x0101, -89210, 0, -62630, 45)
    ChrSetPos(0x0102, -89130, 0, -63770, 45)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x0008, -87270, 0, -59540, 135)
    ChrSetPos(0x0009, -85710, 0, -59510, 180)
    ChrSetPos(0x000A, -86540, 0, -61600, 45)
    ChrSetPos(0x000B, -84960, 0, -60990, 315)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010100996V#001F#1P卡露娜姐姐，\n',
            '祝贺你们通过预选赛～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0009, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x000A, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x000B, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    @scena.Lambda('lambda_213B')
    def lambda_213B():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_213B)

    @scena.Lambda('lambda_2149')
    def lambda_2149():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2149)

    @scena.Lambda('lambda_2157')
    def lambda_2157():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_2157)

    @scena.Lambda('lambda_2165')
    def lambda_2165():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_2165)

    ChrTalk(
        0x0009,
        (
            '#0120100997V#850F#2P啊，是两位新人啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_219F')
    def lambda_219F():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_219F')

    DispatchAsync2(0x0008, 0x0001, lambda_219F)

    @scena.Lambda('lambda_21B0')
    def lambda_21B0():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_21B0')

    DispatchAsync2(0x0009, 0x0001, lambda_21B0)

    @scena.Lambda('lambda_21C1')
    def lambda_21C1():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_21C1')

    DispatchAsync2(0x000A, 0x0001, lambda_21C1)

    @scena.Lambda('lambda_21D2')
    def lambda_21D2():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_21D2')

    DispatchAsync2(0x000B, 0x0001, lambda_21D2)

    @scena.Lambda('lambda_21E3')
    def lambda_21E3():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_21E3')

    DispatchAsync2(0x0101, 0x0001, lambda_21E3)

    @scena.Lambda('lambda_21F4')
    def lambda_21F4():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_21F4')

    DispatchAsync2(0x0102, 0x0001, lambda_21F4)

    @scena.Lambda('lambda_2205')
    def lambda_2205():
        CameraMove(-87430, 0, -59810, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2205)

    @scena.Lambda('lambda_221D')
    def lambda_221D():
        ChrWalkTo(0x00FE, -88420, 0, -60220, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_221D)

    Sleep(500)

    @scena.Lambda('lambda_223D')
    def lambda_223D():
        ChrWalkTo(0x00FE, -88150, 0, -61430, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_223D)

    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0008,
        (
            '#0320100998V#831F哦，是你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0310100999V#821F#6P嘿嘿。\n',
            '难道你们是特地来看比赛的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101000V#010F#1P嗯，是的。\n',
            '正好看到了前辈你们的比赛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101001V比赛真是精彩啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0330101002V#841F谢谢，\n',
            '听到你们这么说真是高兴啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330101003V不过这次突然变成团体赛，\n',
            '正觉得奇怪呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0120101004V#819F#2P嗯嗯，\n',
            '真是紧张呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0320101005V#835F我们还算好啦。\n',
            '不管怎么说集齐了队友。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320101006V老实说，\n',
            '金大人的情况可真是不妙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101007V#501F啊～～\n',
            '卡露娜姐姐你们也认识金先生吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0320101008V#830F啊，不算认识，\n',
            '仅仅是知道名字而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320101009V他被称为『不动金』，\n',
            '是共和国著名的游击士呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0330101010V#840F好像是专门为参加武术大会\n',
            '而来到利贝尔王国的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330101011V就像刚才所说的，\n',
            '今年的武术大会突然从\n',
            '个人赛改成了团体赛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0310101012V#825F#6P这么大胆的主意大概是\n',
            '那个杜南公爵想出来的吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0310101013V#6P金大人没有办法，\n',
            '只能落到一个人出场的境地了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101014V#007F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101015V#009F真是的……\n',
            '那个公爵净爱搞一些无聊的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0330101016V#841F哈哈，没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330101017V#844F可是，这样他的实力没办法全部发挥，\n',
            '真是太替他可惜了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0310101018V#823F#6P不过，如果有实力不俗的人来协助他，\n',
            '就算那些人没有什么名气也好啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '#0310101019V#821F#6P……哦！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0320101020V#831F……哎呀…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    OP_63(0x000B)

    ChrTalk(
        0x000B,
        (
            '#0330101021V#841F…………嗯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#0120101022V#2P……或许能行…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101023V#505F？？？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101024V怎、怎么了？\n',
            '这样盯着我们看……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0330101025V#840F没什么，我们在想……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330101026V你们愿不愿意\n',
            '协助金先生参加正式赛呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101027V#002F哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    OP_63(0x0101)

    ChrTalk(
        0x0101,
        (
            '#0010101028V#004F#3S哎～～～～～～！？',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101029V#014F#1P从正式赛开始参加……\n',
            '这样也可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0320101030V#835F本来就是突然\n',
            '从个人赛变成团体赛的嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320101031V规矩也不是死的，\n',
            '应该能多少通融一下的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0310101032V#820F#6P而且金大人\n',
            '也曾经问过艾南有没有\n',
            '能够协助他的游击士呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0310101033V#6P不过雪拉扎德忙得脱不开身，\n',
            '阿加特那家伙也联系不上。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0310101034V#6P别的人也都是类似的情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0120101035V#856F#2P至于卡西乌斯先生，\n',
            '好像也不在国内呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120101036V#819F#2P不过，他和金先生组合的话，\n',
            '好像违反规定了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0330101037V#841F哈哈，如果这样的话，\n',
            '我们可是连一点胜算也没有了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330101038V#840F……就是这样，\n',
            '你们好好考虑一下吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330101039V今天和金先生达成一致意见的话，\n',
            '就能赶上明天的选手报名了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101040V#004F嗯，好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0320101041V#830F哎呀……\n',
            '聊天的时间太长了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320101042V我们还有很多的委托要做，\n',
            '抱歉，就先告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0120101043V#850F#2P拜拜了，两位新人！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0310101044V#821F#6P嘿嘿。\n',
            '期待能在比赛场上和你们交手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x000B, 0xFF)

    @scena.Lambda('lambda_2CE1')
    def lambda_2CE1():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_2CE1')

    DispatchAsync2(0x0101, 0x0001, lambda_2CE1)

    @scena.Lambda('lambda_2CF2')
    def lambda_2CF2():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_2CF2')

    DispatchAsync2(0x0102, 0x0001, lambda_2CF2)

    CreateThread(0x000A, 0x01, 0x00, func_14_33C3)
    Sleep(300)

    CreateThread(0x000B, 0x01, 0x00, func_14_33C3)
    Sleep(300)

    CreateThread(0x0009, 0x01, 0x00, func_14_33C3)
    Sleep(300)

    OP_72(0x0005, 0x0010)
    OP_6F(0x0005, 0)
    OP_70(0x0005, 29)
    Sleep(300)

    CreateThread(0x0008, 0x01, 0x00, func_14_33C3)
    Sleep(2000)

    WaitForThreadExit(0x0008, 0x0001)
    OP_72(0x0005, 0x0800)
    PlaySE(7, 0x00, 0x64)
    OP_70(0x0005, 29)
    OP_70(0x0005, 0)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    CameraMove(-89000, 0, -60260, 1000)
    OP_71(0x0005, 0x0800)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020101045V#010F……怎么办，艾丝蒂尔？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101046V本来是要谈和工作有关的事情，\n',
            '结果变成这个样子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0101, 15, 0, 300, 4000)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010101047V#008F#2P……嘿嘿…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0101, 15, 0, 400, 4000)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010101048V#502F#2P………哼哼……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020101049V#014F艾丝蒂尔，你、你没事吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0101, 0x0002)
    ChrSetChipByIndex(0x0101, 23)
    ChrSetSubChip(0x0101, 0)

    ChrTalk(
        0x0101,
        (
            '#0010101050V#582F#2P来了来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x0101)
    Sleep(400)

    ChrSetSubChip(0x0101, 1)

    ChrTalk(
        0x0101,
        (
            '#0010101051V#508F#2P#3S终于来了～～～！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    OP_62(0x0102, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    CloseMessageWindow()
    ChrClearFlags(0x0101, 0x0002)
    ChrSetChipByIndex(0x0101, 65535)
    ChrTurnDirection(0x0101, 0x0102, 400)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010101052V#006F#2P对了，就是这样！\n',
            '果然果然就是这样！！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101053V#502F啊啊，女神！\n',
            '感谢您的保佑！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101054V#014F………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101055V#013F艾、艾丝蒂尔疯了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101056V#580F#2P你想想看！\n',
            '我们可以参加武术大会了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101057V#582F可以帮助遇到困难的金先生……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101058V可以光明正大地进入王城……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101059V而且可以体验白热化的战斗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010101060V#508F#2P#3S这真是一石三鸟啊！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101061V#019F能、能做到这一步吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101062V#010F不过，\n',
            '虽然还不知道能不能获胜……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101063V有靠自己就能完成委托的可能性，\n',
            '这个主意还真非常不错呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101064V#001F#2P嗯嗯⊙\n',
            '不管怎么说，这是最重要的！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101065V#005F……就这么决定了，\n',
            '赶快去拜托金先生吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101066V#014F话说回来，\n',
            '你知道金先生在哪里吗？',
            TxtCtl.Enter,
        ),
    )

    @scena.Lambda('lambda_328C')
    def lambda_328C():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_328C')

    DispatchAsync2(0x0102, 0x0001, lambda_328C)

    @scena.Lambda('lambda_329D')
    def lambda_329D():
        ChrWalkTo(0x0101, -89630, 0, -62950, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_329D)

    Sleep(600)

    TerminateThread(0x0101, 0xFF)
    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1000)

    OP_63(0x0101)
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010101067V#505F#1P……这么说的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101068V#017F#2P真是的……\n',
            '稍微冷静一点嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101069V#010F总之先回协会\n',
            '向艾南先生报告一下吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101070V如果是他的话，\n',
            '肯定会知道金先生在哪儿的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T4121._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0014 offset: 0x33C3
@scena.Code('func_14_33C3')
def func_14_33C3():
    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, -87400, 0, -62970, 3000, 0x00)
    ChrWalkTo(0x00FE, -90080, 0, -62980, 3000, 0x00)

    @scena.Lambda('lambda_33F6')
    def lambda_33F6():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_33F6)

    ChrWalkTo(0x00FE, -91260, 0, -62700, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0015 offset: 0x341C
@scena.Code('func_15_341C')
def func_15_341C():
    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0104, 84960, 0, 33240, 270)
    ChrSetPos(0x0102, 84840, 0, 32159, 270)
    ChrSetPos(0x0101, 85910, 0, 32400, 270)
    ChrSetPos(0x0108, 86160, 0, 33600, 270)
    ChrSetPos(0x000C, 87840, 0, 24750, 0)
    ChrSetPos(0x000D, 86780, 0, 23680, 0)
    ChrSetPos(0x000E, 88160, 0, 23360, 0)
    CameraMove(84240, 0, 32960, 0)
    OP_0D()

    ChrTalk(
        0x0102,
        (
            '#0020110067V#010F右边的『苍之组』休息室，\n',
            '应该就是这里对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080110068V#070F嗯，没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040110069V#035F哈·哈·哈。\n',
            '在比赛之前就让我们悠闲地休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110070V#007F不管什么时候，\n',
            '你不都是一样地悠闲吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000C,
        '青年的声音',
        (
            '#0450110071V#2P嘿嘿……\n',
            '还真是一点也不紧张啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_35F6')
    def lambda_35F6():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_35F6)

    @scena.Lambda('lambda_3604')
    def lambda_3604():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3604)

    @scena.Lambda('lambda_3612')
    def lambda_3612():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_3612)

    @scena.Lambda('lambda_3620')
    def lambda_3620():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_3620)

    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    CameraMove(86060, 0, 28650, 2000)

    ChrTalk(
        0x0101,
        (
            '#0010110072V#004F你、你们是……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3675')
    def lambda_3675():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_3675')

    DispatchAsync2(0x0101, 0x0001, lambda_3675)

    @scena.Lambda('lambda_3686')
    def lambda_3686():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_3686')

    DispatchAsync2(0x0102, 0x0001, lambda_3686)

    @scena.Lambda('lambda_3697')
    def lambda_3697():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_3697')

    DispatchAsync2(0x0108, 0x0001, lambda_3697)

    @scena.Lambda('lambda_36A8')
    def lambda_36A8():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_36A8')

    DispatchAsync2(0x0104, 0x0001, lambda_36A8)

    @scena.Lambda('lambda_36B9')
    def lambda_36B9():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_36B9')

    DispatchAsync2(0x000C, 0x0001, lambda_36B9)

    @scena.Lambda('lambda_36CA')
    def lambda_36CA():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_36CA')

    DispatchAsync2(0x000D, 0x0001, lambda_36CA)

    @scena.Lambda('lambda_36DB')
    def lambda_36DB():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_36DB')

    DispatchAsync2(0x000E, 0x0001, lambda_36DB)

    @scena.Lambda('lambda_36EC')
    def lambda_36EC():
        CameraMove(84900, 0, 32229, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_36EC)

    @scena.Lambda('lambda_3704')
    def lambda_3704():
        ChrWalkTo(0x00FE, 86080, 0, 31150, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_3704)

    Sleep(200)

    @scena.Lambda('lambda_3724')
    def lambda_3724():
        ChrWalkTo(0x00FE, 87340, 0, 30470, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_3724)

    Sleep(200)

    @scena.Lambda('lambda_3744')
    def lambda_3744():
        ChrWalkTo(0x00FE, 86030, 0, 29770, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_3744)

    WaitForThreadExit(0x000E, 0x0002)

    ChrTalk(
        0x000E,
        (
            '#0460110073V哼……\n',
            '没想到在这种地方见面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0470110074V嘻哈哈。\n',
            '在这里遇见你们，还真是走运啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110075V#505F#2P……你们是谁啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000C, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x000D, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x000E, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1200)

    ChrTalk(
        0x000C,
        (
            '#0450110076V#1P我们可是卢安\n',
            '大名鼎鼎的『渡鸦帮』！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0460110077V不要说你已经忘了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110078V#001F#2P开玩笑，是开玩笑的啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110079V#006F昨天已经观看了你们同伴参加的预选赛，\n',
            '就知道你们几个肯定也来了王都。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110080V那么，这次你们来，\n',
            '又是想不知悔改地找我们麻烦对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0450110081V哼·哼·哼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0470110082V嘿·嘿·嘿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0460110083V呼·呼·呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110084V#009F#2P什、什么啊，真是恶心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110085V#014F难道说，你们也参加正式赛吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110086V#004F#2P哎……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0450110087V喂，干嘛露出那么吃惊的表情啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0470110088V我们可是在预选赛中取胜，\n',
            '才走到这一步的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0460110089V可不像半途参加的某些家伙那样，\n',
            '这么厚脸皮的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110090V#004F#2P哎～这不是很厉害嘛！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110091V#001F像你们这种业余的人也能胜出，\n',
            '干得不错嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110092V肯定进行了相当辛苦的特训吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0450110093V哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0460110094V说什么呢，这个小丫头……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110095V#006F#2P本来以为你们只是普通的小混混呢，\n',
            '没想到这么有毅力啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110096V#502F嗯嗯，要对你们刮目相看了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0470110097V没什么啦……嘿嘿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x000C, 0xFF)
    ChrTurnDirection(0x000C, 0x000D, 600)

    ChrTalk(
        0x000C,
        (
            '#0450110098V#2P别、别被迷惑了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0460110099V总、总之，\n',
            '之前被你们给捉弄了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0460110100V趁这个机会，\n',
            '一定要把这笔账算回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x0101, 600)

    ChrTalk(
        0x0101,
        (
            '#0010110101V#006F#2P哼哼，正合我意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110102V对了，\n',
            '你们也在这边的休息室？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0450110103V不，是另外一边……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110104V#006F#2P那么，我们很有可能\n',
            '会在今天的比赛中就碰面哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110105V#001F如果这样的话，\n',
            '我们就来堂堂正正地较量一番吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x000E, 0xFF)
    TerminateThread(0x000D, 0xFF)

    ChrTalk(
        0x000C,
        (
            '#0450110106V…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0460110107V…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0470110108V…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110109V#505F#2P哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000C, 180, 400)

    ChrTalk(
        0x000C,
        (
            '#0450110110V#2P喂，我们走吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0460110111V嗯……\n',
            '她好像有点不正常。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0470110112V比赛之前我们去吃点东西吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000D, 180, 400)

    @scena.Lambda('lambda_3F4C')
    def lambda_3F4C():
        ChrWalkTo(0x00FE, 86030, 0, 23300, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_3F4C)

    ChrSetDirection(0x000E, 180, 400)

    @scena.Lambda('lambda_3F6E')
    def lambda_3F6E():
        ChrWalkTo(0x00FE, 87340, 0, 23300, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_3F6E)

    Sleep(300)

    @scena.Lambda('lambda_3F8E')
    def lambda_3F8E():
        ChrWalkTo(0x00FE, 86080, 0, 23300, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_3F8E)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0108, 0xFF)
    TerminateThread(0x0104, 0xFF)
    CameraMove(84900, 0, 33240, 2000)

    ChrTalk(
        0x0101,
        (
            '#0010110113V#580F#2P什、什么呀……真是不给面子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010110114V#505F喂，我说了什么奇怪的话吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)
    ChrTurnDirection(0x0108, 0x0101, 0)
    ChrTurnDirection(0x0104, 0x0101, 0)

    ChrTalk(
        0x0102,
        (
            '#0020110115V#010F#1P不……没有啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110116V#019F你也真是厉害啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110117V#004F哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080110118V#071F#2P哈哈，算了，不要在意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040110119V#035F#5P对自己的优点毫不关心，\n',
            '这才是艾丝蒂尔君的本色嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110120V#509F怎么感觉像是被看猴戏了一样……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110121V#019F#1P没有这种事啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110122V#010F我们赶快进休息室，\n',
            '等待比赛开始吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x00C3, 4, 0x61C))
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T4104._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0016 offset: 0x41DB
@scena.Code('func_16_41DB')
def func_16_41DB():
    EventBegin(0x00)
    CameraMove(82890, 0, -58910, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 82240, 0, -59590, 90)
    ChrSetPos(0x0102, 83290, 0, -60620, 0)
    ChrSetPos(0x0108, 84060, 0, -58500, 180)
    ChrSetPos(0x0104, 84330, 0, -59900, 270)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrSetPos(0x0008, 80230, 0, -59410, 180)
    ChrSetPos(0x000A, 79030, 0, -59770, 90)
    ChrSetPos(0x000B, 81100, 0, -61130, 315)
    ChrSetPos(0x0009, 79590, 0, -60950, 0)
    ChrSetPos(0x0016, 77000, 0, -64940, 135)
    ChrSetPos(0x000F, 77450, 0, -66680, 352)
    ChrSetPos(0x0010, 78200, 0, -66090, 315)
    ChrSetPos(0x0011, 78970, 0, -65300, 247)
    ChrSetPos(0x0017, 82830, 0, -65010, 270)
    ChrSetPos(0x0013, 81290, 0, -65700, 90)
    ChrSetPos(0x0012, 83000, 0, -66520, 16)
    ChrSetPos(0x0014, 81230, 0, -64459, 98)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010110123V#503F好、好像快要开始了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110124V怎么办……\n',
            '心一直在扑通扑通地乱跳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110125V#010F要保持镇静啊，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110126V轮到我们的时候会有通知的，\n',
            '在那之前就安心等待吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110127V#007F嗯～就算这么说，\n',
            '我也平静不下来啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    FormationDelMember(0x01, 0xFF)
    FormationDelMember(0x07, 0xFF)
    FormationDelMember(0x03, 0xFF)
    ChrClearFlags(0x0024, 0x0080)
    ChrClearFlags(0x0025, 0x0080)
    ChrClearFlags(0x0026, 0x0080)
    ChrSetPos(0x0024, 83160, 0, -59400, 180)
    ChrSetPos(0x0026, 84060, 0, -58500, 180)
    ChrSetPos(0x0025, 85350, 0, -58540, 180)
    CameraMove(84180, 0, -61020, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 84180, 0, -61020, 0)
    CreateThread(0x0024, 0x00, 0x00, func_02_902)
    CreateThread(0x0025, 0x00, 0x00, func_02_902)
    CreateThread(0x0026, 0x00, 0x00, func_02_902)
    CreateThread(0x0008, 0x00, 0x00, func_02_902)
    CreateThread(0x000A, 0x00, 0x00, func_02_902)
    CreateThread(0x0009, 0x00, 0x00, func_02_902)
    CreateThread(0x000B, 0x00, 0x00, func_02_902)
    CreateThread(0x000F, 0x00, 0x00, func_02_902)
    CreateThread(0x0010, 0x00, 0x00, func_02_902)
    CreateThread(0x0011, 0x00, 0x00, func_02_902)
    CreateThread(0x0012, 0x00, 0x00, func_02_902)
    CreateThread(0x0013, 0x00, 0x00, func_02_902)
    CreateThread(0x0014, 0x00, 0x00, func_02_902)
    CreateThread(0x0016, 0x00, 0x00, func_02_902)
    CreateThread(0x0017, 0x00, 0x00, func_02_902)
    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0017 offset: 0x458A
@scena.Code('func_17_458A')
def func_17_458A():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4667',
    )

    FadeOut(1000, 0, -1)
    OP_0D()
    EventBegin(0x00)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('主持人的声音')

    Talk(
        (
            '#2200110180V',
            (TxtCtl.SetColor, 0x5),
            '各位……\n',
            '让你们久等了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200110181V',
            (TxtCtl.SetColor, 0x5),
            '我宣布，武术大会正式赛，现在开始！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    MapSetFlags(0x00100000)
    PlaySE(175, 0x00, 0x64)
    PlaySE(191, 0x00, 0x64)
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T4104._SN', 100, 0, 0)
    IdleLoop()

    def _loc_4667(): pass

    label('loc_4667')

    Return()

# id: 0x0018 offset: 0x4668
@scena.Code('func_18_4668')
def func_18_4668():
    EventBegin(0x00)
    CameraMove(79600, 0, -59790, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 82240, 0, -59590, 90)
    ChrSetPos(0x0102, 83290, 0, -60620, 0)
    ChrSetPos(0x0108, 84060, 0, -58500, 180)
    ChrSetPos(0x0104, 84330, 0, -59900, 270)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrSetPos(0x0008, 80230, 0, -59410, 180)
    ChrSetPos(0x000A, 79030, 0, -59770, 90)
    ChrSetPos(0x000B, 81100, 0, -61130, 315)
    ChrSetPos(0x0009, 79590, 0, -60950, 0)
    ChrSetPos(0x0016, 77000, 0, -64940, 135)
    ChrSetPos(0x000F, 77450, 0, -66680, 352)
    ChrSetPos(0x0010, 78200, 0, -66090, 315)
    ChrSetPos(0x0011, 78970, 0, -65300, 247)
    ChrSetPos(0x0017, 82830, 0, -65010, 270)
    ChrSetPos(0x0013, 81290, 0, -65700, 90)
    ChrSetPos(0x0012, 83000, 0, -66520, 16)
    ChrSetPos(0x0014, 81230, 0, -64459, 98)

    @scena.Lambda('lambda_47F9')
    def lambda_47F9():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_47F9')

    DispatchAsync2(0x0016, 0x0001, lambda_47F9)

    @scena.Lambda('lambda_480A')
    def lambda_480A():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_480A')

    DispatchAsync2(0x000F, 0x0001, lambda_480A)

    @scena.Lambda('lambda_481B')
    def lambda_481B():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_481B')

    DispatchAsync2(0x0010, 0x0001, lambda_481B)

    @scena.Lambda('lambda_482C')
    def lambda_482C():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_482C')

    DispatchAsync2(0x0011, 0x0001, lambda_482C)

    @scena.Lambda('lambda_483D')
    def lambda_483D():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_483D')

    DispatchAsync2(0x0017, 0x0001, lambda_483D)

    @scena.Lambda('lambda_484E')
    def lambda_484E():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_484E')

    DispatchAsync2(0x0012, 0x0001, lambda_484E)

    @scena.Lambda('lambda_485F')
    def lambda_485F():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_485F')

    DispatchAsync2(0x0013, 0x0001, lambda_485F)

    @scena.Lambda('lambda_4870')
    def lambda_4870():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_4870')

    DispatchAsync2(0x0014, 0x0001, lambda_4870)

    @scena.Lambda('lambda_4881')
    def lambda_4881():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_4881')

    DispatchAsync2(0x0101, 0x0001, lambda_4881)

    @scena.Lambda('lambda_4892')
    def lambda_4892():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_4892')

    DispatchAsync2(0x0102, 0x0001, lambda_4892)

    @scena.Lambda('lambda_48A3')
    def lambda_48A3():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_48A3')

    DispatchAsync2(0x0108, 0x0001, lambda_48A3)

    @scena.Lambda('lambda_48B4')
    def lambda_48B4():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_48B4')

    DispatchAsync2(0x0104, 0x0001, lambda_48B4)

    Sleep(1000)

    ChrTalk(
        0x000B,
        (
            '#0330110185V好……该出场了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0310110186V#820F被称为突击骑兵队的，\n',
            '肯定是相当勇猛的王国军将士。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0310110187V作为对手来说够格了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110188V#000F卡露娜姐姐，你们要加油哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#0320110189V#831F啊，看我们的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0009,
        (
            '#0120110190V#816F那么我们上吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_49E1')
    def lambda_49E1():
        ChrWalkTo(0x00FE, 73100, 0, -63210, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_49E1)

    Sleep(200)

    @scena.Lambda('lambda_4A01')
    def lambda_4A01():
        ChrWalkTo(0x00FE, 73100, 0, -63210, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_4A01)

    @scena.Lambda('lambda_4A1C')
    def lambda_4A1C():
        ChrWalkTo(0x00FE, 73100, 0, -63210, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_4A1C)

    Sleep(200)

    @scena.Lambda('lambda_4A3C')
    def lambda_4A3C():
        ChrWalkTo(0x00FE, 73100, 0, -63210, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_4A3C)

    FadeOut(2000, 0, -1)
    Sleep(1000)

    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/T4104._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0019 offset: 0x4A6D
@scena.Code('func_19_4A6D')
def func_19_4A6D():
    EventBegin(0x00)
    CameraMove(77930, 0, -60800, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 78520, 0, -61710, 270)
    ChrSetPos(0x0102, 79300, 0, -62840, 270)
    ChrSetPos(0x0108, 79800, 0, -61660, 270)
    ChrSetPos(0x0104, 79010, 0, -60670, 180)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrSetPos(0x0016, 77000, 0, -64940, 135)
    ChrSetPos(0x000F, 77450, 0, -66680, 352)
    ChrSetPos(0x0010, 78200, 0, -66090, 315)
    ChrSetPos(0x0011, 78970, 0, -65300, 247)
    ChrSetPos(0x0017, 82830, 0, -65010, 270)
    ChrSetPos(0x0013, 81290, 0, -65700, 90)
    ChrSetPos(0x0012, 83000, 0, -66520, 16)
    ChrSetPos(0x0014, 81230, 0, -64459, 98)
    ChrSetPos(0x0008, 72110, 0, -61480, 90)
    ChrSetPos(0x000A, 72060, 0, -62470, 90)
    ChrSetPos(0x000B, 71980, 0, -63590, 90)
    ChrSetPos(0x0009, 72090, 0, -64519, 90)

    @scena.Lambda('lambda_4BEA')
    def lambda_4BEA():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_4BEA')

    DispatchAsync2(0x0016, 0x0001, lambda_4BEA)

    @scena.Lambda('lambda_4BFB')
    def lambda_4BFB():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_4BFB')

    DispatchAsync2(0x000F, 0x0001, lambda_4BFB)

    @scena.Lambda('lambda_4C0C')
    def lambda_4C0C():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_4C0C')

    DispatchAsync2(0x0010, 0x0001, lambda_4C0C)

    @scena.Lambda('lambda_4C1D')
    def lambda_4C1D():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_4C1D')

    DispatchAsync2(0x0011, 0x0001, lambda_4C1D)

    @scena.Lambda('lambda_4C2E')
    def lambda_4C2E():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_4C2E')

    DispatchAsync2(0x0017, 0x0001, lambda_4C2E)

    @scena.Lambda('lambda_4C3F')
    def lambda_4C3F():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_4C3F')

    DispatchAsync2(0x0012, 0x0001, lambda_4C3F)

    @scena.Lambda('lambda_4C50')
    def lambda_4C50():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_4C50')

    DispatchAsync2(0x0013, 0x0001, lambda_4C50)

    @scena.Lambda('lambda_4C61')
    def lambda_4C61():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_4C61')

    DispatchAsync2(0x0014, 0x0001, lambda_4C61)

    @scena.Lambda('lambda_4C72')
    def lambda_4C72():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_4C72')

    DispatchAsync2(0x0101, 0x0001, lambda_4C72)

    @scena.Lambda('lambda_4C83')
    def lambda_4C83():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_4C83')

    DispatchAsync2(0x0102, 0x0001, lambda_4C83)

    @scena.Lambda('lambda_4C94')
    def lambda_4C94():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_4C94')

    DispatchAsync2(0x0108, 0x0001, lambda_4C94)

    @scena.Lambda('lambda_4CA5')
    def lambda_4CA5():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_4CA5')

    DispatchAsync2(0x0104, 0x0001, lambda_4CA5)

    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010110196V#001F#5P太好了！\n',
            '卡露娜姐姐他们赢了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080110197V#070F不愧是利贝尔的游击士啊。\n',
            '  ',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080110198V联手作战能厉害到如此程度。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040110199V#035F就算在人少的时候，\n',
            '各自也能做到以一敌百呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110200V#010F如果碰上他们，\n',
            '肯定要进行一番苦战了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x000A, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x000B, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0009, 255, 255, 255, 0, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetFlags(0x0008, 0x0040)
    ChrSetFlags(0x000A, 0x0040)
    ChrSetFlags(0x000B, 0x0040)
    ChrSetFlags(0x0009, 0x0040)

    @scena.Lambda('lambda_4E1E')
    def lambda_4E1E():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_4E1E)

    @scena.Lambda('lambda_4E30')
    def lambda_4E30():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_4E30')

    DispatchAsync2(0x0008, 0x0002, lambda_4E30)

    @scena.Lambda('lambda_4E41')
    def lambda_4E41():
        ChrWalkTo(0x00FE, 77020, 0, -60760, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_4E41)

    Sleep(100)

    @scena.Lambda('lambda_4E61')
    def lambda_4E61():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_4E61)

    @scena.Lambda('lambda_4E73')
    def lambda_4E73():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_4E73')

    DispatchAsync2(0x000A, 0x0002, lambda_4E73)

    @scena.Lambda('lambda_4E84')
    def lambda_4E84():
        ChrWalkTo(0x00FE, 76490, 0, -61830, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_4E84)

    Sleep(100)

    @scena.Lambda('lambda_4EA4')
    def lambda_4EA4():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_4EA4)

    @scena.Lambda('lambda_4EB6')
    def lambda_4EB6():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_4EB6')

    DispatchAsync2(0x000B, 0x0002, lambda_4EB6)

    @scena.Lambda('lambda_4EC7')
    def lambda_4EC7():
        ChrWalkTo(0x00FE, 77520, 0, -62340, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_4EC7)

    Sleep(100)

    @scena.Lambda('lambda_4EE7')
    def lambda_4EE7():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_4EE7)

    @scena.Lambda('lambda_4EF9')
    def lambda_4EF9():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_4EF9')

    DispatchAsync2(0x0009, 0x0002, lambda_4EF9)

    @scena.Lambda('lambda_4F0A')
    def lambda_4F0A():
        ChrWalkTo(0x00FE, 76260, 0, -59400, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_4F0A)

    WaitForThreadExit(0x0009, 0x0003)

    @scena.Lambda('lambda_4F2A')
    def lambda_4F2A():
        ChrWalkTo(0x00FE, 77690, 0, -59890, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_4F2A)

    ChrTalk(
        0x0101,
        (
            '#0010110201V#508F各位前辈，打得真漂亮！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080110202V#070F哟，真是精彩的比赛啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x000B, 0x0003)

    ChrTalk(
        0x000B,
        (
            '#0330110203V#841F哈哈，能被『不动金』这样称赞，\n',
            '真是光荣之至啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x000A, 0x0003)

    ChrTalk(
        0x000A,
        (
            '#0310110204V#825F果然和预选赛不一样，\n',
            '不能有丝毫懈怠呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('主持人的声音')

    Talk(
        (
            '#2200110205V',
            (TxtCtl.SetColor, 0x5),
            '下面宣布第二场比赛的\n',
            '对阵双方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200110206V',
            (TxtCtl.SetColor, 0x5),
            '南边，苍之组——\n',
            '来自卡尔瓦德共和国的武术家，\n',
            '金选手等四人组！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200110207V',
            (TxtCtl.SetColor, 0x5),
            '北边，红之组——\n',
            '『渡鸦帮』所属，\n',
            '迪恩选手等四人组！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0108, 0xFF)
    TerminateThread(0x0104, 0xFF)

    @scena.Lambda('lambda_5139')
    def lambda_5139():
        CameraMove(78520, 0, -60920, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5139)

    ChrTurnDirection(0x0101, 0x0102, 400)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010110208V#006F#5P轮到我们了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020110209V#015F而且对手是渡鸦帮那些人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040110210V#035F哼哼，虽然是有欠优雅的对手，\n',
            '不过会是场有趣的比赛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080110211V#076F好，我们出场吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0016, 0xFF)
    TerminateThread(0x000F, 0xFF)
    TerminateThread(0x0010, 0xFF)
    TerminateThread(0x0011, 0xFF)
    TerminateThread(0x0017, 0xFF)
    TerminateThread(0x0012, 0xFF)
    TerminateThread(0x0013, 0xFF)
    TerminateThread(0x0014, 0xFF)
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(77750, 0, -62490, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 77750, 0, -62490, 270)
    ChrSetPos(0x0102, 77750, 0, -62490, 270)
    ChrSetPos(0x0108, 77750, 0, -62490, 270)
    ChrSetPos(0x0104, 77750, 0, -62490, 270)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000B, 0xFF)
    ChrSetPos(0x0008, 76870, 0, -60150, 180)
    ChrSetPos(0x000A, 79050, 0, -59930, 180)
    ChrSetPos(0x0009, 77910, 0, -59730, 180)
    ChrSetPos(0x000B, 75670, 0, -60330, 180)
    CreateThread(0x0008, 0x00, 0x00, func_02_902)
    CreateThread(0x000A, 0x00, 0x00, func_02_902)
    CreateThread(0x0009, 0x00, 0x00, func_02_902)
    CreateThread(0x000B, 0x00, 0x00, func_02_902)
    CreateThread(0x000F, 0x00, 0x00, func_02_902)
    CreateThread(0x0010, 0x00, 0x00, func_02_902)
    CreateThread(0x0011, 0x00, 0x00, func_02_902)
    CreateThread(0x0012, 0x00, 0x00, func_02_902)
    CreateThread(0x0013, 0x00, 0x00, func_02_902)
    CreateThread(0x0014, 0x00, 0x00, func_02_902)
    CreateThread(0x0016, 0x00, 0x00, func_02_902)
    CreateThread(0x0017, 0x00, 0x00, func_02_902)
    SetScenaFlags(ScenaFlag(0x00C3, 5, 0x61D))
    OP_1B(0x0B, 0x00, 0x0030)
    OP_1B(0x0C, 0x00, 0xFFFF)
    ChrClearFlags(0x0008, 0x0040)
    ChrClearFlags(0x000A, 0x0040)
    ChrClearFlags(0x000B, 0x0040)
    ChrClearFlags(0x0009, 0x0040)
    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x001A offset: 0x53A7
@scena.Code('func_1A_53A7')
def func_1A_53A7():
    EventBegin(0x00)
    CameraMove(81050, 0, -59630, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 81880, 0, -59420, 225)
    ChrSetPos(0x0102, 82470, 0, -60720, 270)
    ChrSetPos(0x0108, 82960, 0, -59440, 225)
    ChrSetPos(0x0104, 82020, 0, -61450, 315)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrSetPos(0x0008, 80230, 0, -59410, 90)
    ChrSetPos(0x000A, 79030, 0, -59770, 90)
    ChrSetPos(0x000B, 80710, 0, -61590, 45)
    ChrSetPos(0x0009, 79590, 0, -60950, 90)
    ChrSetPos(0x0016, 77000, 0, -64940, 135)
    ChrSetPos(0x000F, 77450, 0, -66680, 352)
    ChrSetPos(0x0010, 78200, 0, -66090, 315)
    ChrSetPos(0x0011, 78970, 0, -65300, 247)
    ChrSetPos(0x0017, 82830, 0, -65010, 270)
    ChrSetPos(0x0013, 81290, 0, -65700, 90)
    ChrSetPos(0x0012, 83000, 0, -66520, 16)
    ChrSetPos(0x0014, 81230, 0, -64459, 98)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0320110238V#830F哈哈……\n',
            '那些小混混也能做到如此程度啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320110239V看来人真是可以改变的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0310110240V虽然胜负已分，\n',
            '不过真是精彩的比赛呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040110241V#031F哈·哈·哈，谢谢了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040110242V他们能洗心革面，\n',
            '全是拜我的仁德所赐哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0120110243V哎～是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0104, 400)

    ChrTalk(
        0x0101,
        (
            '#0010110244V#007F#2P一个完全不知情的人，\n',
            '又在别人面前信口开河起来了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110245V#509F说起来，\n',
            '你根本不认识那些流氓呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040110246V#035F坠入爱河只是一瞬间的事，\n',
            '但加速度可是无限大的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110247V#018F越来越听不懂了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('主持人的声音')

    Talk(
        (
            '#2200110248V',
            (TxtCtl.SetColor, 0x5),
            '下面宣布第三场比赛的\n',
            '对阵双方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200110249V',
            (TxtCtl.SetColor, 0x5),
            '南边，苍之组——',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200110250V',
            (TxtCtl.SetColor, 0x5),
            '王国军空降部队３连，\n',
            '莱尔中尉等四人组！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    @scena.Lambda('lambda_57F0')
    def lambda_57F0():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_57F0')

    DispatchAsync2(0x0008, 0x0001, lambda_57F0)

    @scena.Lambda('lambda_5801')
    def lambda_5801():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_5801')

    DispatchAsync2(0x000A, 0x0001, lambda_5801)

    @scena.Lambda('lambda_5812')
    def lambda_5812():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_5812')

    DispatchAsync2(0x000B, 0x0001, lambda_5812)

    @scena.Lambda('lambda_5823')
    def lambda_5823():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_5823')

    DispatchAsync2(0x0009, 0x0001, lambda_5823)

    @scena.Lambda('lambda_5834')
    def lambda_5834():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_5834')

    DispatchAsync2(0x0101, 0x0001, lambda_5834)

    @scena.Lambda('lambda_5845')
    def lambda_5845():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_5845')

    DispatchAsync2(0x0102, 0x0001, lambda_5845)

    @scena.Lambda('lambda_5856')
    def lambda_5856():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_5856')

    DispatchAsync2(0x0108, 0x0001, lambda_5856)

    @scena.Lambda('lambda_5867')
    def lambda_5867():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_5867')

    DispatchAsync2(0x0104, 0x0001, lambda_5867)

    @scena.Lambda('lambda_5878')
    def lambda_5878():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_5878')

    DispatchAsync2(0x0017, 0x0001, lambda_5878)

    @scena.Lambda('lambda_5889')
    def lambda_5889():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_5889')

    DispatchAsync2(0x0012, 0x0001, lambda_5889)

    @scena.Lambda('lambda_589A')
    def lambda_589A():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_589A')

    DispatchAsync2(0x0013, 0x0001, lambda_589A)

    @scena.Lambda('lambda_58AB')
    def lambda_58AB():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_58AB')

    DispatchAsync2(0x0014, 0x0001, lambda_58AB)

    CameraMove(78750, 0, -62500, 1500)

    ChrTalk(
        0x0016,
        (
            '#2240110251V#5P好……该我们出场了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#2240110252V#5P打起精神来上场吧，小子们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#2250110253V是的，长官！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0016, 0x01, 0x00, func_1B_5AF5)
    Sleep(300)

    CreateThread(0x000F, 0x01, 0x00, func_1B_5AF5)
    Sleep(300)

    CreateThread(0x0011, 0x01, 0x00, func_1B_5AF5)
    Sleep(600)

    CreateThread(0x0010, 0x01, 0x00, func_1B_5AF5)
    Sleep(1000)

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('主持人的声音')

    Talk(
        (
            '#2200110254V',
            (TxtCtl.SetColor, 0x5),
            '北边，红之组——',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200110255V',
            (TxtCtl.SetColor, 0x5),
            '空贼团『卡普亚一家』所属，\n',
            '多伦选手等四人组！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0108, 0xFF)
    TerminateThread(0x0104, 0xFF)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    CameraMove(82090, 0, -59990, 1000)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010110256V#580F#2P#3S哎！？',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110257V#014F『卡普亚一家』不是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040110258V#033F哎呀哎呀，\n',
            '好像在哪里听说过这名字呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x007F, 5, 0x3FD))
    NewScene('ED6_DT01/T4104._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x001B offset: 0x5AF5
@scena.Code('func_1B_5AF5')
def func_1B_5AF5():
    ChrWalkTo(0x00FE, 74370, 0, -62950, 3000, 0x00)

    @scena.Lambda('lambda_5B0F')
    def lambda_5B0F():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_5B0F)

    ChrWalkTo(0x00FE, 72250, 0, -62830, 3000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x001C offset: 0x5B35
@scena.Code('func_1C_5B35')
def func_1C_5B35():
    EventBegin(0x00)
    CameraMove(81050, 0, -59630, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 81880, 0, -59420, 270)
    ChrSetPos(0x0102, 82470, 0, -60720, 270)
    ChrSetPos(0x0108, 82960, 0, -59440, 270)
    ChrSetPos(0x0104, 82020, 0, -61450, 270)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrSetPos(0x0008, 80230, 0, -59410, 270)
    ChrSetPos(0x000A, 79030, 0, -59770, 270)
    ChrSetPos(0x000B, 80710, 0, -61590, 270)
    ChrSetPos(0x0009, 79590, 0, -60950, 270)
    ChrSetPos(0x0017, 82830, 0, -65010, 270)
    ChrSetPos(0x0013, 81290, 0, -65700, 270)
    ChrSetPos(0x0012, 83000, 0, -66520, 270)
    ChrSetPos(0x0014, 81230, 0, -64459, 270)
    Sleep(1000)

    ChrTalk(
        0x0108,
        (
            '#0080110266V#074F规则变为团体赛，\n',
            '又破例允许罪犯参加比赛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080110267V#070F真是什么事情都可能发生呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040110268V#031F哈·哈·哈。\n',
            '真是宽容的公爵大人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110269V#005F#2P不、不是笑的时候吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110270V#017F我也觉得不应该变成这样……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x007F, 6, 0x3FE))
    NewScene('ED6_DT01/T4104._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x001D offset: 0x5D85
@scena.Code('func_1D_5D85')
def func_1D_5D85():
    EventBegin(0x00)
    CameraMove(81050, 0, -59630, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 81880, 0, -59420, 270)
    ChrSetPos(0x0102, 82470, 0, -60720, 270)
    ChrSetPos(0x0108, 82960, 0, -59440, 270)
    ChrSetPos(0x0104, 82020, 0, -61450, 270)
    ChrSetPos(0x0008, 80230, 0, -59410, 270)
    ChrSetPos(0x000A, 79030, 0, -59770, 270)
    ChrSetPos(0x000B, 80710, 0, -61590, 270)
    ChrSetPos(0x0009, 79590, 0, -60950, 270)
    ChrSetPos(0x0016, 72110, 0, -61480, 90)
    ChrSetPos(0x000F, 72060, 0, -62470, 90)
    ChrSetPos(0x0010, 71980, 0, -63590, 90)
    ChrSetPos(0x0011, 72090, 0, -64519, 90)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrSetPos(0x0017, 82830, 0, -65010, 270)
    ChrSetPos(0x0013, 81290, 0, -65700, 270)
    ChrSetPos(0x0012, 83000, 0, -66520, 270)
    ChrSetPos(0x0014, 81790, 0, -63840, 270)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010110277V#505F#2P哈啊～……\n',
            '那些空贼真的赢了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110278V#010F按他们的实力来说，\n',
            '这也是合理的结果啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110279V#017F不过，万一他们获得冠军，\n',
            '那该怎么办才好呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040110280V#031F哈·哈·哈。\n',
            '招待空贼进城参加晚宴吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040110281V一定会是很有趣的情景呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110282V#005F#2P这种事在发生之前，\n',
            '一定会被我们阻止的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080110283V#070F不管怎么说，强敌又多了一组啊。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_6099')
    def lambda_6099():
        CameraMove(79710, 0, -62800, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_6099)

    ChrSetRGBAMask(0x0016, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x000F, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0010, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0011, 255, 255, 255, 0, 0)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)

    @scena.Lambda('lambda_60F1')
    def lambda_60F1():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0016, 0x0001, lambda_60F1)

    @scena.Lambda('lambda_6103')
    def lambda_6103():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_6103)

    @scena.Lambda('lambda_6115')
    def lambda_6115():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_6115)

    @scena.Lambda('lambda_6127')
    def lambda_6127():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_6127)

    @scena.Lambda('lambda_6139')
    def lambda_6139():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_6139')

    DispatchAsync2(0x0016, 0x0002, lambda_6139)

    @scena.Lambda('lambda_614A')
    def lambda_614A():
        ChrWalkTo(0x00FE, 78430, 0, -65650, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0016, 0x0003, lambda_614A)

    Sleep(300)

    @scena.Lambda('lambda_616A')
    def lambda_616A():
        ChrTurnDirection(0x00FE, 0x0016, 0)
        Yield()

        Jump('lambda_616A')

    DispatchAsync2(0x000F, 0x0002, lambda_616A)

    @scena.Lambda('lambda_617B')
    def lambda_617B():
        ChrWalkTo(0x00FE, 77210, 0, -65870, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0003, lambda_617B)

    Sleep(300)

    @scena.Lambda('lambda_619B')
    def lambda_619B():
        ChrTurnDirection(0x00FE, 0x0016, 0)
        Yield()

        Jump('lambda_619B')

    DispatchAsync2(0x0010, 0x0002, lambda_619B)

    @scena.Lambda('lambda_61AC')
    def lambda_61AC():
        ChrWalkTo(0x00FE, 77260, 0, -64709, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0003, lambda_61AC)

    Sleep(300)

    @scena.Lambda('lambda_61CC')
    def lambda_61CC():
        ChrTurnDirection(0x00FE, 0x0016, 0)
        Yield()

        Jump('lambda_61CC')

    DispatchAsync2(0x0011, 0x0002, lambda_61CC)

    ChrSetFlags(0x0011, 0x0040)

    @scena.Lambda('lambda_61E2')
    def lambda_61E2():
        ChrWalkTo(0x00FE, 78250, 0, -64160, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_61E2)

    @scena.Lambda('lambda_61FD')
    def lambda_61FD():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_61FD')

    DispatchAsync2(0x0008, 0x0001, lambda_61FD)

    @scena.Lambda('lambda_620E')
    def lambda_620E():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_620E')

    DispatchAsync2(0x000A, 0x0001, lambda_620E)

    @scena.Lambda('lambda_621F')
    def lambda_621F():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_621F')

    DispatchAsync2(0x000B, 0x0001, lambda_621F)

    @scena.Lambda('lambda_6230')
    def lambda_6230():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_6230')

    DispatchAsync2(0x0009, 0x0001, lambda_6230)

    @scena.Lambda('lambda_6241')
    def lambda_6241():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_6241')

    DispatchAsync2(0x0101, 0x0001, lambda_6241)

    @scena.Lambda('lambda_6252')
    def lambda_6252():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_6252')

    DispatchAsync2(0x0102, 0x0001, lambda_6252)

    @scena.Lambda('lambda_6263')
    def lambda_6263():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_6263')

    DispatchAsync2(0x0108, 0x0001, lambda_6263)

    @scena.Lambda('lambda_6274')
    def lambda_6274():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_6274')

    DispatchAsync2(0x0104, 0x0001, lambda_6274)

    @scena.Lambda('lambda_6285')
    def lambda_6285():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_6285')

    DispatchAsync2(0x0017, 0x0001, lambda_6285)

    @scena.Lambda('lambda_6296')
    def lambda_6296():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_6296')

    DispatchAsync2(0x0012, 0x0001, lambda_6296)

    @scena.Lambda('lambda_62A7')
    def lambda_62A7():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_62A7')

    DispatchAsync2(0x0013, 0x0001, lambda_62A7)

    @scena.Lambda('lambda_62B8')
    def lambda_62B8():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_62B8')

    DispatchAsync2(0x0014, 0x0001, lambda_62B8)

    WaitForThreadExit(0x0016, 0x0003)

    ChrTalk(
        0x0016,
        (
            '#2240110284V#5P可恶……\n',
            '竟然输给了罪犯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0017, 0xFF)
    ChrWalkTo(0x0017, 80400, 0, -64709, 2000, 0x00)

    ChrTalk(
        0x0017,
        (
            '#2260110285V#2P哎，别这么泄气了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#2260110286V#2P只是因为他们擅长小队作战罢了，\n',
            '在这点上我们还是有差距的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0016, 0xFF)
    TerminateThread(0x000F, 0xFF)
    TerminateThread(0x0010, 0xFF)
    TerminateThread(0x0011, 0xFF)

    @scena.Lambda('lambda_639B')
    def lambda_639B():
        ChrTurnDirection(0x00FE, 0x0017, 400)
        Yield()

        Jump('lambda_639B')

    DispatchAsync2(0x000F, 0x0001, lambda_639B)

    @scena.Lambda('lambda_63AC')
    def lambda_63AC():
        ChrTurnDirection(0x00FE, 0x0017, 400)
        Yield()

        Jump('lambda_63AC')

    DispatchAsync2(0x0010, 0x0001, lambda_63AC)

    @scena.Lambda('lambda_63BD')
    def lambda_63BD():
        ChrTurnDirection(0x00FE, 0x0017, 400)
        Yield()

        Jump('lambda_63BD')

    DispatchAsync2(0x0011, 0x0001, lambda_63BD)

    ChrSetDirection(0x0016, 90, 400)

    ChrTalk(
        0x0016,
        (
            '#2240110287V#5P不……\n',
            '问题在于我们的实力不够。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#2240110288V#5P回到部队之后，\n',
            '训练量要增加了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('主持人的声音')

    Talk(
        (
            '#2200110289V',
            (TxtCtl.SetColor, 0x5),
            '下面宣布第四场比赛的\n',
            '对阵双方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200110249V',
            (TxtCtl.SetColor, 0x5),
            '南边，苍之组——',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200110291V',
            (TxtCtl.SetColor, 0x5),
            '国境警卫队７连所属，\n',
            '贝伦中尉等四人组！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    @scena.Lambda('lambda_64E2')
    def lambda_64E2():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_64E2')

    DispatchAsync2(0x0008, 0x0001, lambda_64E2)

    @scena.Lambda('lambda_64F3')
    def lambda_64F3():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_64F3')

    DispatchAsync2(0x000A, 0x0001, lambda_64F3)

    @scena.Lambda('lambda_6504')
    def lambda_6504():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_6504')

    DispatchAsync2(0x000B, 0x0001, lambda_6504)

    @scena.Lambda('lambda_6515')
    def lambda_6515():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_6515')

    DispatchAsync2(0x0009, 0x0001, lambda_6515)

    @scena.Lambda('lambda_6526')
    def lambda_6526():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_6526')

    DispatchAsync2(0x0101, 0x0001, lambda_6526)

    @scena.Lambda('lambda_6537')
    def lambda_6537():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_6537')

    DispatchAsync2(0x0102, 0x0001, lambda_6537)

    @scena.Lambda('lambda_6548')
    def lambda_6548():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_6548')

    DispatchAsync2(0x0108, 0x0001, lambda_6548)

    @scena.Lambda('lambda_6559')
    def lambda_6559():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_6559')

    DispatchAsync2(0x0104, 0x0001, lambda_6559)

    ChrTalk(
        0x0016,
        (
            '#2240110292V#5P该你们出场了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#2240110293V#5P剩下的对手只有那些家伙了。\n',
            '一定不要输给他们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#2260110294V#2P知道了……\n',
            '就让他们看看我们正规军的军魂吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0017, 0xFF)
    TerminateThread(0x0012, 0xFF)
    TerminateThread(0x0013, 0xFF)
    TerminateThread(0x0014, 0xFF)
    ChrSetDirection(0x0017, 90, 400)

    ChrTalk(
        0x0017,
        (
            '#2260110295V#5P伙计们，上吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_664B')
    def lambda_664B():
        ChrTurnDirection(0x00FE, 0x0017, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_664B)

    @scena.Lambda('lambda_6659')
    def lambda_6659():
        ChrTurnDirection(0x00FE, 0x0017, 400)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_6659)

    ChrTurnDirection(0x0014, 0x0017, 400)

    ChrTalk(
        0x0012,
        (
            '#2290110298V#2P#1K是的，长官！',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x0013,
        (
            '#1P#1K是的，长官！',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x0014,
        (
            '#2P#1K是的，长官！',
            TxtCtl.Enter,
        ),
    )

    Sleep(500)

    OP_56(0x01)
    OP_59()

    @scena.Lambda('lambda_66C7')
    def lambda_66C7():
        ChrTurnDirection(0x00FE, 0x0017, 400)
        Yield()

        Jump('lambda_66C7')

    DispatchAsync2(0x0016, 0x0001, lambda_66C7)

    CreateThread(0x0017, 0x01, 0x00, func_1E_6819)
    Sleep(300)

    CreateThread(0x0014, 0x01, 0x00, func_1E_6819)
    Sleep(300)

    CreateThread(0x0013, 0x01, 0x00, func_1E_6819)
    CreateThread(0x0012, 0x01, 0x00, func_1E_6819)
    Sleep(1500)

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('主持人的声音')

    Talk(
        (
            '#2200110254V',
            (TxtCtl.SetColor, 0x5),
            '北边，红之组——',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200110300V',
            (TxtCtl.SetColor, 0x5),
            '王国军情报部特务部队所属，\n',
            '洛伦斯少尉等四人组！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0108, 0xFF)
    TerminateThread(0x0104, 0xFF)
    CameraMove(82090, 0, -59990, 1000)

    ChrTalk(
        0x0101,
        (
            '#0010110301V#005F#2P是他们……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110302V#012F洛伦斯少尉……\n',
            '难道是那个时候的……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x007F, 7, 0x3FF))
    NewScene('ED6_DT01/T4104._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x001E offset: 0x6819
@scena.Code('func_1E_6819')
def func_1E_6819():
    ChrWalkTo(0x00FE, 79260, 0, -62720, 3000, 0x00)
    ChrWalkTo(0x00FE, 74370, 0, -62950, 3000, 0x00)

    @scena.Lambda('lambda_6847')
    def lambda_6847():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_6847)

    ChrWalkTo(0x00FE, 72250, 0, -62830, 3000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x001F offset: 0x686D
@scena.Code('func_1F_686D')
def func_1F_686D():
    EventBegin(0x00)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    CameraMove(76690, 0, -61440, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0102, 76260, 0, -60960, 270)
    ChrSetPos(0x0108, 77340, 0, -60400, 270)
    ChrSetPos(0x0101, 76310, 0, -62260, 270)
    ChrSetPos(0x0104, 77550, 0, -61920, 270)
    ChrSetPos(0x0008, 80230, 0, -59410, 270)
    ChrSetPos(0x000A, 79030, 0, -59770, 270)
    ChrSetPos(0x000B, 80710, 0, -61590, 270)
    ChrSetPos(0x0009, 79590, 0, -60950, 270)
    ChrSetPos(0x0016, 77000, 0, -64940, 270)
    ChrSetPos(0x000F, 77630, 0, -66970, 270)
    ChrSetPos(0x0010, 78610, 0, -66490, 270)
    ChrSetPos(0x0011, 79150, 0, -65459, 270)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010110308V#005F#1P怎、怎么会……\n',
            '简直是压倒性的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080110309V#073F哦～真强啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080110310V那个小组，\n',
            '预选赛的时候是三个人参赛的。\n',
            '也曾想到他们会增加一个人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080110311V原来还准备了这样的王牌啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040110312V#032F与我和艾丝蒂尔君他们一样，\n',
            '是从正式赛才开始参赛的呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040110313V#035F呵呵……\n',
            '还有这样的隐藏人物啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110314V#514F……刚才的剑法……是………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_6B32')
    def lambda_6B32():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_6B32)

    @scena.Lambda('lambda_6B40')
    def lambda_6B40():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_6B40)

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010110315V#505F哎……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110316V约修亚，你怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110317V#013F难道………………\n',
            '………可是………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110318V#580F约修亚……………？\n',
            '……………约修亚！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0102, 15, 0, 300, 4000)
    Sleep(400)

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020110319V#014F啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110320V#019F没关系……什么事也没有。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110321V那个的剑法太漂亮了，\n',
            '所以看得有点入迷……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110322V#505F是、是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040110323V#035F呵，不愧是约修亚。\n',
            '感性还真是丰富啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('主持人的声音')

    Talk(
        (
            '#2200110324V',
            (TxtCtl.SetColor, 0x5),
            '经过刚才的激战，\n',
            '武术大会正式赛首日的比赛就全部结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200110325V',
            (TxtCtl.SetColor, 0x5),
            '晋级第二轮的队伍是——\n',
            '克鲁茨、多伦、\n',
            '金以及洛伦斯四个小组！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200110326V',
            (TxtCtl.SetColor, 0x5),
            '期待他们以后的精彩表现！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_20(0x000005DC)
    FadeOut(1500, 0, -1)
    OP_0D()
    Sleep(500)

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到奖金',
            (TxtCtl.SetColor, 0x4),
            '２００００',
            (TxtCtl.SetColor, 0x0),
            '米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(500)

    AddMira(20000)
    MapClearFlags(0x00100000)
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T4101._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0020 offset: 0x6E43
@scena.Code('func_20_6E43')
def func_20_6E43():
    EventBegin(0x00)
    ChrClearFlags(0x001D, 0x0080)
    ChrSetPos(0x001D, 320, 0, -470, 0)

    NpcTalk(
        0x001D,
        '女孩的声音',
        (
            '#0280110635V#2P啊，是小艾你们啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0104, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0108, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    Fade(500)
    CameraMove(560, 0, 3040, 0)
    ChrSetPos(0x0101, 9740, 0, 4610, 0)
    ChrSetPos(0x0102, 10040, 0, 5710, 0)
    ChrSetPos(0x0108, 10970, 0, 5750, 0)
    ChrSetPos(0x0104, 10990, 0, 4550, 0)
    ChrWalkTo(0x001D, 260, 0, 3010, 3000, 0x00)
    ChrTurnDirection(0x001D, 0x0101, 400)

    ChrTalk(
        0x0101,
        (
            '#0010110636V#501F#1P啊，这不是朵洛希嘛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_6F97')
    def lambda_6F97():
        ChrWalkTo(0x00FE, 1410, 0, 2520, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_6F97)

    Sleep(300)

    @scena.Lambda('lambda_6FB7')
    def lambda_6FB7():
        ChrWalkTo(0x00FE, 1360, 0, 3560, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_6FB7)

    Sleep(300)

    @scena.Lambda('lambda_6FD7')
    def lambda_6FD7():
        ChrWalkTo(0x00FE, 2680, 0, 2640, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0002, lambda_6FD7)

    Sleep(300)

    @scena.Lambda('lambda_6FF7')
    def lambda_6FF7():
        ChrWalkTo(0x00FE, 2630, 0, 3740, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_6FF7)

    WaitForThreadExit(0x0102, 0x0002)

    ChrTalk(
        0x0102,
        (
            '#0020110637V#010F好久不见了……\n',
            '其实也没有相隔多长时间吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110638V在蔡斯还碰见过呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001D,
        (
            '#0280110639V#151F是啊是啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280110640V还能够活着见到你们，\n',
            '真是做梦也没有想到呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280110641V因为你们好像乘坐工房的飞艇，\n',
            '到十分危险的地方去了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080110642V#073F危险的地方……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040110643V#030F哦～真是有趣嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110644V#580F哇哇，朵洛希！\n',
            '这件事以后再说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001D,
        (
            '#0280110645V#153F哎……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280110646V对了对了，\n',
            '这两位好像在哪里见过呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040110647V#031F呵呵……\n',
            '我们在柏斯市里见过一次面哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040110648V能再见面真是让人高兴呢。\n',
            '这位富有个性魅力的小姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080110649V#071F至于我，则是在温泉村附近\n',
            '曾和你擦肩而过的那个人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001D,
        (
            '#0280110650V#151F啊啊～我想起来了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280110651V喝霸王酒的客人先生，\n',
            '和东方装束的熊先生！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280110652V#150F小艾，你们就是\n',
            '和他们一起参加武术大会的吗～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110653V#006F嗯，没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110654V#010F我们是拜托过这位金先生，\n',
            '才从正式赛开始参加的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110655V对了，朵洛希小姐。\n',
            '今天你也是来取材的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001D,
        (
            '#0280110656V#150F嗯～直到昨天\n',
            '都在对别的事情进行取材呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280110657V今天早上碰到奈尔前辈，\n',
            '才听说小艾你们来参加武术大会的事～\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280110658V#151F不过，真是和前辈所说的一样，\n',
            '真是很强的小组呢！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280110659V这下说不定能拍出很棒的照片呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110660V#506F啊哈哈，那真是让人期待啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110661V#004F哎……说起来，\n',
            '奈尔没和你一起来吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001D,
        (
            '#0280110662V#154F嗯，奈尔前辈嘛～\n',
            '好像有非常重要的事情要调查呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280110663V昨天整个晚上好像\n',
            '都在和大堆大堆的资料作战呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280110664V今天又去找老朋友谈话去了～\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110665V#505F是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001D,
        (
            '#0280110666V#150F啊，对了对了，\n',
            '我带来了前辈给小艾你们的口信哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280110667V说是让你们今天傍晚的时候，\n',
            '到编辑部来一趟～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280110668V看起来，好像是很重要的事情吧～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110669V#006F嗯……我知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110670V#010F比赛结束之后就去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040110671V#037F很重要的事情……\n',
            '嘿嘿～～感觉有点可疑呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040110672V#031F真是让人在意啊。\n',
            '咕噜咕噜咕噜～喵喵～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrTurnDirection(0x0101, 0x0104, 600)

    ChrTalk(
        0x0101,
        (
            '#0010110673V#580F这、这可不行。\n',
            '这件事跟大赖皮蛋没有关系啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040110674V#034F真无情啊，艾丝蒂尔君！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040110675V昨天的比赛中，\n',
            '我们俩的感情明明那样激情地燃烧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040110676V用不到我的时候，\n',
            '就像扔垃圾一样把我抛弃掉！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110677V#582F我都说啦！\n',
            '不要用那种容易让人误解的说话方式！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001D,
        (
            '#0280110678V#153F哇哇，小艾，\n',
            '你什么时候和这位帅哥……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 270, 600)

    ChrTalk(
        0x0101,
        (
            '#0010110679V#509F这种鬼话你也相信！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001D,
        (
            '#0280110680V#151F啊，这样的话～\n',
            '为了能找到好的摄影位置，\n',
            '我现在就去观众席了～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280110681V我支持小艾你们，\n',
            '一定要加油啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x001D, 270, 400)

    @scena.Lambda('lambda_79BF')
    def lambda_79BF():
        CameraMove(-2000, 0, 3110, 2000)

        ExitThread()

    DispatchAsync(0x001D, 0x0003, lambda_79BF)

    @scena.Lambda('lambda_79D7')
    def lambda_79D7():
        ChrWalkTo(0x00FE, -11300, 0, 5910, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001D, 0x0002, lambda_79D7)

    WaitForThreadExit(0x001D, 0x0003)
    Sleep(1500)

    CameraMove(1820, 0, 2900, 1500)

    ChrTalk(
        0x0108,
        (
            '#0080110682V#073F怎么说呢……\n',
            '真是有个性的小姑娘啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_7A47')
    def lambda_7A47():
        ChrTurnDirection(0x00FE, 0x0104, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_7A47)

    ChrTurnDirection(0x0101, 0x0104, 400)

    ChrTalk(
        0x0101,
        (
            '#0010110683V#007F呼～……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110684V要同时对付奥利维尔和朵洛希，\n',
            '还真是够累人的啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040110685V#031F哈·哈·哈，这也是为了\n',
            '缓解一下比赛前的紧张气氛嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110686V#010F朵洛希小姐，\n',
            '作为摄影师可是相当的厉害哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110687V最近《利贝尔通讯》上的照片\n',
            '都是她亲手拍摄的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080110688V#073F哦，这还真是厉害啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080110689V#071F那么，我们就在照相机前\n',
            '好好地表现一番给他们看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110690V#006F嗯……没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110691V虽然还不知道会和谁相遇，\n',
            '不过不打起十分的精神来不行啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x00C4, 4, 0x624))
    OP_28(0x0048, 0x01, 0x0008)
    OP_1B(0x01, 0x00, 0xFFFF)
    OP_1B(0x02, 0x00, 0xFFFF)
    ChrSetFlags(0x001D, 0x0080)
    EventEnd(0x00)

    Return()

# id: 0x0021 offset: 0x7C6D
@scena.Code('func_21_7C6D')
def func_21_7C6D():
    EventBegin(0x00)
    ChrClearFlags(0x001D, 0x0080)
    ChrSetPos(0x001D, -320, 0, -470, 0)

    NpcTalk(
        0x001D,
        '女孩的声音',
        (
            '#0280110635V#1P啊，是小艾你们啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0104, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0108, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    Fade(500)
    CameraMove(-2000, 0, 3040, 0)
    ChrSetPos(0x0101, -9740, 0, 4610, 90)
    ChrSetPos(0x0102, -10040, 0, 5710, 90)
    ChrSetPos(0x0108, -10970, 0, 5750, 90)
    ChrSetPos(0x0104, -10990, 0, 4550, 90)
    ChrWalkTo(0x001D, -260, 0, 3010, 3000, 0x00)
    ChrTurnDirection(0x001D, 0x0101, 400)

    ChrTalk(
        0x0101,
        (
            '#0010110636V#501F#4P啊，这不是朵洛希嘛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_7DC1')
    def lambda_7DC1():
        ChrWalkTo(0x00FE, -1410, 0, 2520, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_7DC1)

    Sleep(300)

    @scena.Lambda('lambda_7DE1')
    def lambda_7DE1():
        ChrWalkTo(0x00FE, -1360, 0, 3560, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_7DE1)

    Sleep(300)

    @scena.Lambda('lambda_7E01')
    def lambda_7E01():
        ChrWalkTo(0x00FE, -2680, 0, 2640, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0002, lambda_7E01)

    Sleep(300)

    @scena.Lambda('lambda_7E21')
    def lambda_7E21():
        ChrWalkTo(0x00FE, -2630, 0, 3740, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_7E21)

    WaitForThreadExit(0x0102, 0x0002)

    ChrTalk(
        0x0102,
        (
            '#0020110637V#010F#5P好久不见了……\n',
            '其实也没有相隔多长时间吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110638V在蔡斯还碰见过呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001D,
        (
            '#0280110639V#151F#4P是啊是啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280110640V还能够活着见到你们，\n',
            '真是做梦也没有想到呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280110641V因为你们好像乘坐工房的飞艇，\n',
            '到十分危险的地方去了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080110642V#073F#5P危险的地方……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040110643V#030F#5P哦～真是有趣嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110644V#580F#5P哇哇，朵洛希！\n',
            '这件事以后再说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001D,
        (
            '#0280110645V#153F#4P哎……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280110646V对了对了，\n',
            '这两位好像在哪里见过呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040110647V#031F#5P呵呵……\n',
            '我们在柏斯市里见过一次面哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040110648V能再见面真是让人高兴呢。\n',
            '这位富有个性魅力的小姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080110649V#071F#5P至于我，则是在温泉村附近\n',
            '曾和你擦肩而过的那个人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001D,
        (
            '#0280110650V#151F#4P啊啊～我想起来了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280110651V喝霸王酒的客人先生，\n',
            '和东方装束的熊先生！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280110652V#150F小艾，你们就是\n',
            '和他们一起参加武术大会的吗～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110653V#006F#5P嗯，没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110654V#010F#5P我们是拜托过这位金先生，\n',
            '才从正式赛开始参加的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110655V对了，朵洛希小姐。\n',
            '今天你也是来取材的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001D,
        (
            '#0280110656V#150F#4P嗯～直到昨天\n',
            '都在对别的事情进行取材呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280110657V今天早上碰到奈尔前辈，\n',
            '才听说小艾你们来参加武术大会的事～\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280110658V#151F不过，真是和前辈所说的一样，\n',
            '真是很强的小组呢！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280110659V这下说不定能拍出很棒的照片呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110660V#506F#5P啊哈哈，那真是让人期待啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110661V#004F哎……说起来，\n',
            '奈尔没和你一起来吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001D,
        (
            '#0280110662V#154F#4P嗯，奈尔前辈嘛～\n',
            '好像有非常重要的事情要调查呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280110663V昨天整个晚上好像\n',
            '都在和大堆大堆的资料作战呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280110664V今天又去找老朋友谈话去了～\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110665V#505F#5P是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001D,
        (
            '#0280110666V#150F#4P啊，对了对了，\n',
            '我带来了前辈给小艾你们的口信哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280110667V说是让你们今天傍晚的时候，\n',
            '到编辑部来一趟～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280110668V看起来，好像是很重要的事情吧～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110669V#006F#5P嗯……我知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110670V#010F#5P比赛结束之后就去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040110671V#037F#5P很重要的事情……\n',
            '嘿嘿～～感觉有点可疑呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040110672V#031F真是让人在意啊。\n',
            '咕噜咕噜咕噜～喵喵～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrTurnDirection(0x0101, 0x0104, 600)

    ChrTalk(
        0x0101,
        (
            '#0010110673V#580F#6P这、这可不行。\n',
            '这件事跟大赖皮蛋没有关系啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040110674V#034F#5P真无情啊，艾丝蒂尔君！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040110675V昨天的比赛中，\n',
            '我们俩的感情明明那样激情地燃烧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040110676V用不到我的时候，\n',
            '就像扔垃圾一样把我抛弃掉！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110677V#582F#6P我都说啦！\n',
            '不要用那种容易让人误解的说话方式！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001D,
        (
            '#0280110678V#153F#4P哇哇，小艾，\n',
            '你什么时候和这位帅哥……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 90, 600)

    ChrTalk(
        0x0101,
        (
            '#0010110679V#509F#5P这种鬼话你也相信！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001D,
        (
            '#0280110680V#151F#4P啊，这样的话～\n',
            '为了能找到好的摄影位置，\n',
            '我现在就去观众席了～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280110681V我支持小艾你们，\n',
            '一定要加油啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x001D, 90, 400)

    @scena.Lambda('lambda_8834')
    def lambda_8834():
        CameraMove(2000, 0, 3110, 2000)

        ExitThread()

    DispatchAsync(0x001D, 0x0003, lambda_8834)

    @scena.Lambda('lambda_884C')
    def lambda_884C():
        ChrWalkTo(0x00FE, 11300, 0, 5910, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001D, 0x0002, lambda_884C)

    WaitForThreadExit(0x001D, 0x0003)
    Sleep(1500)

    CameraMove(-1920, 0, 3060, 1500)

    ChrTalk(
        0x0108,
        (
            '#0080110682V#073F怎么说呢……\n',
            '真是有个性的小姑娘啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_88BC')
    def lambda_88BC():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_88BC)

    ChrTurnDirection(0x0101, 0x0104, 400)

    ChrTalk(
        0x0101,
        (
            '#0010110683V#007F呼～……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110684V要同时对付奥利维尔和朵洛希，\n',
            '还真是够累人的啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040110685V#031F哈·哈·哈，这也是为了\n',
            '缓解一下比赛前的紧张气氛嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110686V#010F朵洛希小姐，\n',
            '作为摄影师可是相当的厉害哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110687V最近《利贝尔通讯》上的照片\n',
            '都是她亲手拍摄的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080110688V#073F哦，这还真是厉害啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080110689V#071F那么，我们就在照相机前\n',
            '好好地表现一番给他们看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110690V#006F嗯……没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110691V虽然还不知道会和谁相遇，\n',
            '不过不打起十分的精神来不行啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x00C4, 4, 0x624))
    OP_28(0x0048, 0x01, 0x0008)
    OP_1B(0x01, 0x00, 0xFFFF)
    OP_1B(0x02, 0x00, 0xFFFF)
    ChrSetFlags(0x001D, 0x0080)
    EventEnd(0x00)

    Return()

# id: 0x0022 offset: 0x8AE2
@scena.Code('func_22_8AE2')
def func_22_8AE2():
    SetScenaFlags(ScenaFlag(0x007E, 0, 0x3F0))
    NewScene('ED6_DT01/T4104._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0023 offset: 0x8AEF
@scena.Code('func_23_8AEF')
def func_23_8AEF():
    EventBegin(0x00)
    CameraMove(74460, 0, -62460, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x000F, 87610, 0, -63640, 270)
    ChrSetPos(0x0010, 87610, 0, -62310, 270)
    ChrSetPos(0x001A, 87610, 0, -63200, 270)
    ChrSetPos(0x001B, 87610, 0, -63200, 270)
    ChrSetPos(0x001C, 87610, 0, -63200, 270)
    ChrSetPos(0x0019, 87610, 0, -63200, 270)
    ChrSetFlags(0x000F, 0x0004)
    ChrSetFlags(0x0010, 0x0004)
    ChrSetFlags(0x001A, 0x0004)
    ChrSetFlags(0x001B, 0x0004)
    ChrSetFlags(0x001C, 0x0004)
    ChrSetFlags(0x0019, 0x0004)
    ChrSetFlags(0x000F, 0x0040)
    ChrSetFlags(0x0010, 0x0040)
    ChrSetFlags(0x001A, 0x0040)
    ChrSetFlags(0x001B, 0x0040)
    ChrSetFlags(0x001C, 0x0040)
    ChrSetFlags(0x0019, 0x0040)
    ChrSetPos(0x0101, 81280, 0, -63460, 270)
    ChrSetPos(0x0102, 81350, 0, -62190, 270)
    ChrSetPos(0x0108, 80030, 0, -62140, 135)
    ChrSetPos(0x0104, 79980, 0, -63500, 90)
    FadeIn(1000, 0)
    CameraMove(79710, 0, -62840, 2500)

    ChrTalk(
        0x0101,
        (
            '#0010110692V#505F嗯……动作真是慢啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110693V比赛马上就要开始了，\n',
            '另外一组的队员怎么还不来啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110694V#013F确实很奇怪。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110695V是因为有事情迟到了，\n',
            '还是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000F,
        '男人的声音',
        (
            '#2580110696V#1P喂，还不赶快走！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_8D1C')
    def lambda_8D1C():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_8D1C)

    @scena.Lambda('lambda_8D2A')
    def lambda_8D2A():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_8D2A)

    @scena.Lambda('lambda_8D38')
    def lambda_8D38():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_8D38)

    NpcTalk(
        0x001A,
        '粗鲁的声音',
        (
            '#0300110697V#1P真是啰嗦呀。\n',
            '也不用这么急吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x001B,
        '青年的声音',
        (
            '#0290110698V#1P啊啊……\n',
            '为什么会变成这个样子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x001C,
        '女孩的声音',
        (
            '#0090110699V#1P吉尔哥，打起精神来啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x001C,
        '女孩的声音',
        (
            '#0090110700V#1P遇到那些家伙的时候，\n',
            '你这个样子该怎么办啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(6, 0x00, 0x64)
    ChrSetRGBAMask(0x001A, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x001B, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x001C, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0019, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x000F, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0010, 255, 255, 255, 0, 0)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x001A, 0x0080)
    ChrClearFlags(0x001B, 0x0080)
    ChrClearFlags(0x001C, 0x0080)
    ChrClearFlags(0x0019, 0x0080)

    @scena.Lambda('lambda_8EAA')
    def lambda_8EAA():
        CameraMove(81720, 0, -62380, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_8EAA)

    @scena.Lambda('lambda_8EC2')
    def lambda_8EC2():
        ChrWalkTo(0x00FE, 82650, 0, -61790, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_8EC2)

    @scena.Lambda('lambda_8EDD')
    def lambda_8EDD():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x001A, 0x0002, lambda_8EDD)

    Sleep(300)

    @scena.Lambda('lambda_8EF4')
    def lambda_8EF4():
        ChrWalkTo(0x00FE, 83100, 0, -62910, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_8EF4)

    @scena.Lambda('lambda_8F0F')
    def lambda_8F0F():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x001B, 0x0002, lambda_8F0F)

    Sleep(300)

    @scena.Lambda('lambda_8F26')
    def lambda_8F26():
        ChrWalkTo(0x00FE, 82650, 0, -63910, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_8F26)

    @scena.Lambda('lambda_8F41')
    def lambda_8F41():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x001C, 0x0002, lambda_8F41)

    Sleep(300)

    @scena.Lambda('lambda_8F58')
    def lambda_8F58():
        ChrWalkTo(0x00FE, 83540, 0, -60870, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_8F58)

    @scena.Lambda('lambda_8F73')
    def lambda_8F73():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0019, 0x0002, lambda_8F73)

    Sleep(500)

    @scena.Lambda('lambda_8F8A')
    def lambda_8F8A():
        ChrWalkTo(0x00FE, 85520, 0, -63640, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_8F8A)

    @scena.Lambda('lambda_8FA5')
    def lambda_8FA5():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_8FA5)

    Sleep(300)

    @scena.Lambda('lambda_8FBC')
    def lambda_8FBC():
        ChrWalkTo(0x00FE, 85520, 0, -62310, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_8FBC)

    @scena.Lambda('lambda_8FD7')
    def lambda_8FD7():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_8FD7)

    WaitForThreadExit(0x0019, 0x0001)
    ChrTurnDirection(0x0019, 0x0108, 0)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010110701V#004F#5P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x001A, 0x0002)

    ChrTalk(
        0x001A,
        (
            '#0300110702V#192F#4P你们是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110703V#014F#5P是你们这一组啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040110704V#035F#5P呵呵，\n',
            '所以才会来得这么晚啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#0290110705V#200F#4P哼……\n',
            '今天的对手原来不是你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '#0090110706V#210F#4P哼……运气真不错啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090110707V本来还想如果碰上你们的话，\n',
            '一定要让那个没脑子的女人\n',
            '知道我们的厉害呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110708V#509F#5P你、你说什么～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000F,
        '警卫兵',
        (
            '#2580110709V喂！\n',
            '不要乱说话！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0010,
        '警卫兵',
        (
            '#2570110710V多亏了公爵大人的好意，\n',
            '你们才能来参加比赛，难道忘了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_9205')
    def lambda_9205():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_9205)

    @scena.Lambda('lambda_9213')
    def lambda_9213():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_9213)

    @scena.Lambda('lambda_9221')
    def lambda_9221():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_9221)

    ChrSetDirection(0x001A, 90, 400)

    ChrTalk(
        0x001A,
        (
            '#0300110711V#191F#5P哎呀哎呀，士兵小哥。\n',
            '不要这么生气嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300110712V自从被你们带到这里来，\n',
            '我们不是一直老老实实的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000F,
        '警卫兵',
        (
            '#2580110713V希望你们在回到牢房之前，\n',
            '最好给我保持这个态度。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000F,
        '警卫兵',
        (
            '#2580110714V你们也是，\n',
            '不要让这些家伙随便乱说话啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000F,
        '警卫兵',
        (
            '#2580110715V如果弄出麻烦的事情来就坏了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110716V#007F#5P本来就不是在弄麻烦的事情……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0010,
        '警卫兵',
        (
            '#2570110717V你们最好给我记住，\n',
            '竞技场可是有一个中队的兵力在警备着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0010,
        '警卫兵',
        (
            '#2570110718V别想打逃跑的主意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#0290110719V#202F#5P知道啦。\n',
            '我们不会做这种愚蠢的事情的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '#0090110720V#211F#5P哼～\n',
            '真是碍眼啊，还不赶快走？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000F,
        '警卫兵',
        (
            '#2580110721V你这个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x000F, 400)

    NpcTalk(
        0x0010,
        '警卫兵',
        (
            '#2570110722V不要中了小鬼的挑衅啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0010, 270, 400)

    NpcTalk(
        0x0010,
        '警卫兵',
        (
            '#2570110723V听好了，\n',
            '不要动奇怪的心思哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000F, 90, 400)

    @scena.Lambda('lambda_9538')
    def lambda_9538():
        ChrWalkTo(0x00FE, 87610, 0, -63640, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_9538)

    @scena.Lambda('lambda_9553')
    def lambda_9553():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_9553)

    ChrSetDirection(0x0010, 90, 400)

    @scena.Lambda('lambda_956C')
    def lambda_956C():
        ChrWalkTo(0x00FE, 87610, 0, -62310, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_956C)

    @scena.Lambda('lambda_9587')
    def lambda_9587():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_9587)

    Sleep(500)

    PlaySE(7, 0x00, 0x64)
    Sleep(500)

    CameraMove(80720, 0, -62380, 1000)

    ChrTalk(
        0x0101,
        (
            '#0010110724V#505F#5P喂……\n',
            '到底是怎么回事？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110725V为什么你们会来参加武术大会？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_9617')
    def lambda_9617():
        ChrSetDirection(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_9617)

    @scena.Lambda('lambda_9625')
    def lambda_9625():
        ChrSetDirection(0x00FE, 315, 400)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_9625)

    @scena.Lambda('lambda_9633')
    def lambda_9633():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_9633)

    @scena.Lambda('lambda_9641')
    def lambda_9641():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_9641)

    ChrTalk(
        0x0102,
        (
            '#0020110726V#012F#5P真的是杜南公爵让你们参加的吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#0290110727V#200F没错，让我们参加比赛的就是\n',
            '那个头发秀逗身材胖胖的什么公爵。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290110728V如果取得武术大会的优胜，\n',
            '我们就可以减刑了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110729V#509F#5P真、真是难以置信啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080110730V#074F嗯～没想到在这个法治国家，\n',
            '也有这样的独断专制啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040110731V#031F#5P哈·哈·哈，\n',
            '真是乱来的公爵大人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '#0300110732V#197F算了，好不容易得到的批准。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300110733V在判决执行，进棺材之前，\n',
            '至少能做些什么事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300110734V当然……\n',
            '不仅仅是为了这个理由。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110735V#004F#5P哎……怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '#0090110736V#214F真啰嗦，这和你们没有关系吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090110737V是对我们来说有着特殊意义的事情。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110738V#010F#5P不是为了和我们交战\n',
            '才来参加这次武术大会的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110739V是打算和特务兵的人交手吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x001C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x001A, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x001B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x001C,
        (
            '#0090110740V#213F为、为什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '#0300110741V#196F唔……你说得没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300110742V那些家伙装作我们的同伴，\n',
            '但却陷害我们，让我们落到这种田地。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300110743V为了扩大他们情报部的势力而利用我们，\n',
            '等我们没有利用价值之后就过河拆桥！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#0290110744V#203F虽然这次被骗，\n',
            '使我们可以称得上是白痴中的白痴……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290110745V不过，实在是令人不爽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110746V#007F#5P嗯～没错……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110747V这样想的话，\n',
            '你们也真是可怜啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '#0090110748V#214F所以～\n',
            '别用那么哀怜的眼神看着我们啦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090110749V你们还欠了我们人情呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110750V#004F#5P哎？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110751V欠了你们人情……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#0290110752V#200F哼哼，是说之前的事情啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290110753V如果我们把要塞里的事情告诉那些家伙，\n',
            '我看你们还能站在这里比赛吗？',
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
            '#0010110754V#580F#5P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '#0300110755V#191F就是因为痛恨那些家伙，\n',
            '所以才没有把你们的事情说出去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300110756V哇哈哈，感谢我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110757V#509F#5P呜～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110758V#015F#5P确实如此啊……\n',
            '十分感谢你们能对那件事保持沉默。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040110759V#031F#5P好像是很有趣的事情呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040110760V到底是什么好玩的事情，\n',
            '也快点和哥哥我说说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0104, 400)

    ChrTalk(
        0x0101,
        (
            '#0010110761V#582F#6P哼，什么事也没有！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0108, 0x00000000, 2300, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    @scena.Lambda('lambda_9E41')
    def lambda_9E41():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_9E41)

    CameraMove(79710, 0, -62380, 1000)

    ChrTalk(
        0x0108,
        (
            '#0080110762V#073F哦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080110763V那边开始嘈杂起来了，\n',
            '比赛应该马上就要开始了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_9EBA')
    def lambda_9EBA():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_9EBA)

    @scena.Lambda('lambda_9EC8')
    def lambda_9EC8():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_9EC8)

    @scena.Lambda('lambda_9ED6')
    def lambda_9ED6():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_9ED6)

    Sleep(1000)

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('主持人的声音')

    Talk(
        (
            '#2200110180V',
            (TxtCtl.SetColor, 0x5),
            '各位……\n',
            '让你们久等了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200110765V',
            (TxtCtl.SetColor, 0x5),
            '我宣布，武术大会正式赛，\n',
            '第二天的比赛现在开始！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('主持人的声音')

    Talk(
        (
            '#2200110766V',
            (TxtCtl.SetColor, 0x5),
            '那么，我们立刻公布\n',
            '参加第五场比赛的小组吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200110206V',
            (TxtCtl.SetColor, 0x5),
            '南边，苍之组——\n',
            '来自卡尔瓦德共和国的武术家，\n',
            '金选手等四人组！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200110768V',
            (TxtCtl.SetColor, 0x5),
            '北边，红之组——\n',
            '游击士协会格兰赛尔支部，\n',
            '克鲁茨选手等四人组！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ChrTalk(
        0x0101,
        (
            '#0010110769V#005F来了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110770V而且对手是卡露娜姐姐他们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110771V#012F……强敌啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110772V希望我们不会拖金先生的后腿就好了……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0108, 0x0101, 400)

    ChrTalk(
        0x0108,
        (
            '#0080110773V#070F不要想得那么多。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080110774V你们的实力，\n',
            '已经非常接近正游击士了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080110775V剩下的就是胜利的气势了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_A184')
    def lambda_A184():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_A184)

    @scena.Lambda('lambda_A192')
    def lambda_A192():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_A192)

    @scena.Lambda('lambda_A1A0')
    def lambda_A1A0():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_A1A0)

    ChrTalk(
        0x0101,
        (
            '#0010110776V#006F嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110777V#010F我们会努力的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040110778V#035F哈·哈·哈。\n',
            '那么我们向战场上进发吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    ChrClearFlags(0x001A, 0x0004)
    ChrClearFlags(0x001B, 0x0004)
    ChrClearFlags(0x001C, 0x0004)
    ChrClearFlags(0x0019, 0x0004)
    ChrClearFlags(0x001A, 0x0040)
    ChrClearFlags(0x001B, 0x0040)
    ChrClearFlags(0x001C, 0x0040)
    ChrClearFlags(0x0019, 0x0040)
    ChrSetDirection(0x001A, 270, 0)
    ChrSetDirection(0x001C, 270, 0)
    CreateThread(0x001A, 0x00, 0x00, func_02_902)
    CreateThread(0x001B, 0x00, 0x00, func_02_902)
    CreateThread(0x001C, 0x00, 0x00, func_02_902)
    CreateThread(0x0019, 0x00, 0x00, func_02_902)
    CameraMove(80480, 0, -62830, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 80480, 0, -62830, 270)
    ChrSetPos(0x0102, 80480, 0, -62830, 270)
    ChrSetPos(0x0108, 80480, 0, -62830, 270)
    ChrSetPos(0x0104, 80480, 0, -62830, 270)
    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0024 offset: 0xA30E
@scena.Code('func_24_A30E')
def func_24_A30E():
    ChrWalkTo(0x00FE, 85520, 0, -63140, 3000, 0x00)

    @scena.Lambda('lambda_A328')
    def lambda_A328():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_A328)

    ChrWalkTo(0x00FE, 87690, 0, -63010, 3000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0025 offset: 0xA34E
@scena.Code('func_25_A34E')
def func_25_A34E():
    EventBegin(0x00)
    CameraMove(80720, 0, -62380, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 81280, 0, -63460, 90)
    ChrSetPos(0x0102, 81350, 0, -62190, 90)
    ChrSetPos(0x0108, 80030, 0, -62140, 90)
    ChrSetPos(0x0104, 79980, 0, -63500, 90)
    ChrSetPos(0x001A, 82650, 0, -61790, 270)
    ChrSetPos(0x001B, 83100, 0, -62910, 270)
    ChrSetPos(0x001C, 82650, 0, -63910, 270)
    ChrSetPos(0x0019, 84010, 0, -62350, 270)
    ChrClearFlags(0x001A, 0x0080)
    ChrClearFlags(0x001B, 0x0080)
    ChrClearFlags(0x001C, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    FadeIn(1500, 0)
    OP_0D()

    ChrTalk(
        0x001A,
        (
            '#0300110830V#192F哦～干得不错嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#0290110831V#202F嗯嗯。\n',
            '光是看看就让我很兴奋了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '#0090110832V#212F哼……\n',
            '这场比赛打得还可以嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110833V#001F#5P啊哈哈，多谢⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110834V#004F哎，怎么了？\n',
            '你也会说称赞的话啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110835V难道是发烧了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '#0090110836V#214F我、我才不会\n',
            '称赞你这种黄毛丫头呢！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090110837V我只是不想看到把我们逼到绝境的家伙\n',
            '就这么随便地输掉而已！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110838V#509F#5P哼……\n',
            '还真是个嘴硬的丫头啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020110839V#010F#5P算了算了，艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x001C, 400)

    ChrTalk(
        0x0102,
        (
            '#0020110840V#019F#5P……谢谢你们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110841V不管怎么说，\n',
            '你们是在支持我们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x001C, 0x0102, 400)

    ChrTalk(
        0x001C,
        (
            '#0090110842V#414F……啊…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    OP_62(0x001C, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x001C,
        (
            '#0090110843V#216F我、我刚才不是说了吗！？\n',
            '不是在支持你们啦！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110844V#009F#5P（嗯……？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('主持人的声音')

    Talk(
        (
            '#2200110845V',
            (TxtCtl.SetColor, 0x5),
            '下面宣布第六场比赛的\n',
            '对阵双方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200110846V',
            (TxtCtl.SetColor, 0x5),
            '南边，苍之组——\n',
            '空贼团『卡普亚一家』所属，\n',
            '多伦选手等四人组！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200110847V',
            (TxtCtl.SetColor, 0x5),
            '北边，红之组——\n',
            '王国军情报部特务部队所属，\n',
            '洛伦斯少尉等四人组！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    ChrTurnDirection(0x001A, 0x001C, 400)

    ChrTalk(
        0x001A,
        (
            '#0300110848V#196F哦，终于来啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_A866')
    def lambda_A866():
        ChrTurnDirection(0x00FE, 0x001A, 400)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_A866)

    @scena.Lambda('lambda_A874')
    def lambda_A874():
        ChrTurnDirection(0x00FE, 0x001A, 400)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_A874)

    @scena.Lambda('lambda_A882')
    def lambda_A882():
        ChrTurnDirection(0x00FE, 0x001A, 400)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_A882)

    Sleep(400)

    ChrTalk(
        0x001B,
        (
            '#0290110849V#201F要让那些嚣张的黑小子\n',
            '好好见识一下我们的厉害！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110850V#006F#5P这也是一种缘分吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110851V我支持你们，一定要加油哦！\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_A930')
    def lambda_A930():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_A930)

    @scena.Lambda('lambda_A93E')
    def lambda_A93E():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_A93E)

    @scena.Lambda('lambda_A94C')
    def lambda_A94C():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_A94C)

    @scena.Lambda('lambda_A95A')
    def lambda_A95A():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_A95A)

    ChrTalk(
        0x0102,
        (
            '#0020110852V#012F#5P要小心对方的队长。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110853V只要能限制他的自由行动，\n',
            '就一定会有胜算了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '#0090110854V#414F嗯、嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090110855V#214F……不对！\n',
            '谁、谁要你关心了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007E, 1, 0x3F1))
    NewScene('ED6_DT01/T4104._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0026 offset: 0xAA30
@scena.Code('func_26_AA30')
def func_26_AA30():
    EventBegin(0x00)
    CameraMove(75020, 0, -60990, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 75990, 0, -61820, 270)
    ChrSetPos(0x0102, 75110, 0, -61050, 270)
    ChrSetPos(0x0108, 75980, 0, -60520, 270)
    ChrSetPos(0x0104, 77190, 0, -60900, 270)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010110877V#007F啊啊……还是输了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040110878V#033F比赛进行到一半之前，\n',
            '那些空贼的形势还是不错的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040110879V在那个红面具的队长出动之后，\n',
            '他们就开始溃败了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080110880V#072F嗯……不知道底细的对手啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080110881V而且他肯定没有尽全力，\n',
            '以免被别人知道他真正的实力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110882V#580F哎……\n',
            '刚才那不是他的全部实力吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110883V#012F……应该不是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110884V最后的剑技收招之后，\n',
            '集中的剑气也没有因此而衰弱。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110885V肯定还留有余力呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110886V#009F真、真是难以相信……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x001A, 0x0040)
    ChrSetFlags(0x001B, 0x0040)
    ChrSetFlags(0x001C, 0x0040)
    ChrSetFlags(0x0019, 0x0040)
    ChrSetRGBAMask(0x001A, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x001B, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x001C, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0019, 255, 255, 255, 0, 0)
    ChrSetPos(0x001A, 72050, 0, -63520, 90)
    ChrSetPos(0x001B, 72050, 0, -63520, 90)
    ChrSetPos(0x001C, 72050, 0, -63520, 90)
    ChrSetPos(0x0019, 72050, 0, -63520, 90)

    @scena.Lambda('lambda_AD4B')
    def lambda_AD4B():
        ChrTurnDirection(0x00FE, 0x001C, 400)
        Yield()

        Jump('lambda_AD4B')

    DispatchAsync2(0x0101, 0x0002, lambda_AD4B)

    @scena.Lambda('lambda_AD5C')
    def lambda_AD5C():
        ChrTurnDirection(0x00FE, 0x001C, 400)
        Yield()

        Jump('lambda_AD5C')

    DispatchAsync2(0x0102, 0x0002, lambda_AD5C)

    @scena.Lambda('lambda_AD6D')
    def lambda_AD6D():
        ChrTurnDirection(0x00FE, 0x001C, 400)
        Yield()

        Jump('lambda_AD6D')

    DispatchAsync2(0x0108, 0x0002, lambda_AD6D)

    @scena.Lambda('lambda_AD7E')
    def lambda_AD7E():
        ChrTurnDirection(0x00FE, 0x001C, 400)
        Yield()

        Jump('lambda_AD7E')

    DispatchAsync2(0x0104, 0x0002, lambda_AD7E)

    ChrClearFlags(0x001A, 0x0080)
    ChrClearFlags(0x001B, 0x0080)
    ChrClearFlags(0x001C, 0x0080)
    ChrClearFlags(0x0019, 0x0080)

    @scena.Lambda('lambda_ADA3')
    def lambda_ADA3():
        CameraMove(75100, 0, -62310, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_ADA3)

    @scena.Lambda('lambda_ADBB')
    def lambda_ADBB():
        CameraSetDistance(3000, 3000)

        ExitThread()

    DispatchAsync(0x001C, 0x0002, lambda_ADBB)

    @scena.Lambda('lambda_ADCB')
    def lambda_ADCB():
        ChrWalkTo(0x00FE, 77330, 0, -65099, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0003, lambda_ADCB)

    @scena.Lambda('lambda_ADE6')
    def lambda_ADE6():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_ADE6)

    Sleep(500)

    @scena.Lambda('lambda_ADFD')
    def lambda_ADFD():
        ChrWalkTo(0x00FE, 76630, 0, -63990, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001C, 0x0003, lambda_ADFD)

    @scena.Lambda('lambda_AE18')
    def lambda_AE18():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_AE18)

    Sleep(400)

    @scena.Lambda('lambda_AE2F')
    def lambda_AE2F():
        ChrWalkTo(0x00FE, 75560, 0, -64250, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0003, lambda_AE2F)

    @scena.Lambda('lambda_AE4A')
    def lambda_AE4A():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_AE4A)

    Sleep(800)

    @scena.Lambda('lambda_AE61')
    def lambda_AE61():
        ChrWalkTo(0x00FE, 76260, 0, -65370, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0003, lambda_AE61)

    @scena.Lambda('lambda_AE7C')
    def lambda_AE7C():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_AE7C)

    @scena.Lambda('lambda_AE8E')
    def lambda_AE8E():
        ChrSetDirection(0x00FE, 90, 0)
        Yield()

        Jump('lambda_AE8E')

    DispatchAsync2(0x0019, 0x0002, lambda_AE8E)

    WaitForThreadExit(0x001A, 0x0003)

    ChrTalk(
        0x001A,
        (
            '#0300110887V#197F#6P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x001B, 0x0003)

    ChrTalk(
        0x001B,
        (
            '#0290110888V#204F#5P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x001C, 0x0003)

    ChrTalk(
        0x001C,
        (
            '#0090110889V#215F#5P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110890V#505F#2P啊，那个……真是可惜呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '#0300110891V#197F#6P不要说安慰的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0300110892V我们彻底失败了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#0290110893V#205F#5P可恶……\n',
            '都是因为我的支援还太不成熟了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0019, 0xFF)
    ChrTurnDirection(0x001C, 0x001B, 400)

    ChrTalk(
        0x001C,
        (
            '#0090110894V#216F#2P不是吉尔哥的责任……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090110895V都是因为我没有阻止住\n',
            '那家伙的突击啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110896V#003F#2P…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110897V#007F哎，这也是没有办法的事。\n',
            '胜负有时候也要看运气的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110898V#006F你们三兄妹的仇，\n',
            '明天的比赛里我们一定会帮忙讨回来的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_B125')
    def lambda_B125():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x001A, 0x0002, lambda_B125)

    @scena.Lambda('lambda_B133')
    def lambda_B133():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x001B, 0x0002, lambda_B133)

    @scena.Lambda('lambda_B141')
    def lambda_B141():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x001C, 0x0002, lambda_B141)

    @scena.Lambda('lambda_B14F')
    def lambda_B14F():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0019, 0x0002, lambda_B14F)

    ChrTurnDirection(0x001A, 0x0101, 400)

    ChrTalk(
        0x001A,
        (
            '#0300110899V#192F#6P什么……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#0290110900V#201F#6P喂喂……\n',
            '不要说得这么轻巧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110901V#017F虽然我不认为\n',
            '他们是可以随便挑战的对手……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080110902V#071F不过，如果没有干劲的话，\n',
            '本来能赢也会赢不了的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040110903V#035F#2P呵呵，说些没来由的话\n',
            '还真是艾丝蒂尔君的性格啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x000F, 84120, 0, -64660, 270)
    ChrSetPos(0x0010, 84380, 0, -65750, 270)
    ChrSetPos(0x0011, 85120, 0, -64170, 270)
    ChrSetPos(0x0012, 85370, 0, -65269, 270)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)

    NpcTalk(
        0x000F,
        '警卫兵',
        (
            '#2580110904V#1P哼……\n',
            '终于结束了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_B319')
    def lambda_B319():
        ChrTurnDirection(0x00FE, 0x0012, 400)
        Yield()

        Jump('lambda_B319')

    DispatchAsync2(0x001A, 0x0002, lambda_B319)

    @scena.Lambda('lambda_B32A')
    def lambda_B32A():
        ChrTurnDirection(0x00FE, 0x000F, 400)
        Yield()

        Jump('lambda_B32A')

    DispatchAsync2(0x001B, 0x0002, lambda_B32A)

    @scena.Lambda('lambda_B33B')
    def lambda_B33B():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_B33B')

    DispatchAsync2(0x001C, 0x0002, lambda_B33B)

    @scena.Lambda('lambda_B34C')
    def lambda_B34C():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_B34C')

    DispatchAsync2(0x0019, 0x0002, lambda_B34C)

    @scena.Lambda('lambda_B35D')
    def lambda_B35D():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_B35D')

    DispatchAsync2(0x0101, 0x0002, lambda_B35D)

    @scena.Lambda('lambda_B36E')
    def lambda_B36E():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_B36E')

    DispatchAsync2(0x0102, 0x0002, lambda_B36E)

    @scena.Lambda('lambda_B37F')
    def lambda_B37F():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_B37F')

    DispatchAsync2(0x0108, 0x0002, lambda_B37F)

    @scena.Lambda('lambda_B390')
    def lambda_B390():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_B390')

    DispatchAsync2(0x0104, 0x0002, lambda_B390)

    CameraMove(79330, 0, -63550, 1000)

    @scena.Lambda('lambda_B3B2')
    def lambda_B3B2():
        ChrTurnDirection(0x00FE, 0x001B, 0)
        Yield()

        Jump('lambda_B3B2')

    DispatchAsync2(0x000F, 0x0001, lambda_B3B2)

    @scena.Lambda('lambda_B3C3')
    def lambda_B3C3():
        ChrTurnDirection(0x00FE, 0x001A, 0)
        Yield()

        Jump('lambda_B3C3')

    DispatchAsync2(0x0010, 0x0001, lambda_B3C3)

    @scena.Lambda('lambda_B3D4')
    def lambda_B3D4():
        ChrTurnDirection(0x00FE, 0x001A, 0)
        Yield()

        Jump('lambda_B3D4')

    DispatchAsync2(0x0011, 0x0001, lambda_B3D4)

    @scena.Lambda('lambda_B3E5')
    def lambda_B3E5():
        ChrTurnDirection(0x00FE, 0x001A, 0)
        Yield()

        Jump('lambda_B3E5')

    DispatchAsync2(0x0012, 0x0001, lambda_B3E5)

    @scena.Lambda('lambda_B3F6')
    def lambda_B3F6():
        ChrWalkTo(0x00FE, 76360, 0, -62810, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_B3F6)

    Sleep(300)

    @scena.Lambda('lambda_B416')
    def lambda_B416():
        ChrWalkTo(0x00FE, 76760, 0, -66540, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_B416)

    @scena.Lambda('lambda_B431')
    def lambda_B431():
        CameraMove(75030, 0, -62490, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_B431)

    Sleep(300)

    @scena.Lambda('lambda_B44E')
    def lambda_B44E():
        ChrWalkTo(0x00FE, 77690, 0, -63760, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_B44E)

    Sleep(100)

    @scena.Lambda('lambda_B46E')
    def lambda_B46E():
        ChrWalkTo(0x00FE, 78150, 0, -65780, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_B46E)

    WaitForThreadExit(0x000F, 0x0002)

    @scena.Lambda('lambda_B48E')
    def lambda_B48E():
        ChrWalkTo(0x00FE, 74780, 0, -63460, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_B48E)

    WaitForThreadExit(0x0010, 0x0002)

    @scena.Lambda('lambda_B4AE')
    def lambda_B4AE():
        ChrWalkTo(0x00FE, 74960, 0, -65250, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_B4AE)

    NpcTalk(
        0x0011,
        '警卫兵',
        (
            '#2560110905V好了，别磨磨蹭蹭的！\n',
            '赶快回港口去吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '#0300110906V#192F#5P喂喂，别开玩笑了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#0290110907V#202F刚刚比赛完，\n',
            '让我们稍微休息一会儿嘛～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000F,
        '警卫兵',
        (
            '#2580110908V#5P哼……\n',
            '罪犯还要求这么多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0012,
        '警卫兵',
        (
            '#2290110909V喂，赶快走！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '#0300110910V#197F#5P哼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#0290110911V#203F啊啊，好累啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '#0090110889V#215F#5P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x000F, 0xFF)
    TerminateThread(0x0010, 0xFF)
    TerminateThread(0x0011, 0xFF)
    TerminateThread(0x0012, 0xFF)
    TerminateThread(0x001A, 0xFF)
    TerminateThread(0x001B, 0xFF)
    TerminateThread(0x001C, 0xFF)
    TerminateThread(0x0019, 0xFF)

    @scena.Lambda('lambda_B65E')
    def lambda_B65E():
        ChrMoveToRelative(0x00FE, 7000, 0, 1760, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_B65E)

    @scena.Lambda('lambda_B679')
    def lambda_B679():
        ChrMoveToRelative(0x00FE, 7000, 0, 1760, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_B679)

    @scena.Lambda('lambda_B694')
    def lambda_B694():
        CameraMove(78790, 0, -61860, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_B694)

    Sleep(300)

    @scena.Lambda('lambda_B6B1')
    def lambda_B6B1():
        ChrMoveToRelative(0x00FE, 7000, 0, 1760, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_B6B1)

    @scena.Lambda('lambda_B6CC')
    def lambda_B6CC():
        ChrMoveToRelative(0x00FE, 6380, 0, 1760, 2200, 0x00)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_B6CC)

    Sleep(200)

    @scena.Lambda('lambda_B6EC')
    def lambda_B6EC():
        ChrMoveToRelative(0x00FE, 6000, 0, 1760, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_B6EC)

    @scena.Lambda('lambda_B707')
    def lambda_B707():
        ChrMoveToRelative(0x00FE, 6000, 0, 1760, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_B707)

    Sleep(200)

    @scena.Lambda('lambda_B727')
    def lambda_B727():
        ChrMoveToRelative(0x00FE, 6000, 0, 1760, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_B727)

    @scena.Lambda('lambda_B742')
    def lambda_B742():
        ChrMoveToRelative(0x00FE, 6000, 0, 1760, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_B742)

    WaitForThreadExit(0x001C, 0x0001)
    Sleep(600)

    ChrTalk(
        0x001C,
        (
            '#0090110913V#212F#1P喂，你们……',
            TxtCtl.Enter,
        ),
    )

    @scena.Lambda('lambda_B78C')
    def lambda_B78C():
        ChrTurnDirection(0x00FE, 0x001C, 400)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_B78C)

    @scena.Lambda('lambda_B79A')
    def lambda_B79A():
        ChrTurnDirection(0x00FE, 0x001C, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_B79A)

    @scena.Lambda('lambda_B7A8')
    def lambda_B7A8():
        ChrTurnDirection(0x00FE, 0x001C, 400)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_B7A8)

    @scena.Lambda('lambda_B7B6')
    def lambda_B7B6():
        ChrTurnDirection(0x00FE, 0x001C, 400)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_B7B6)

    @scena.Lambda('lambda_B7C4')
    def lambda_B7C4():
        ChrTurnDirection(0x00FE, 0x001C, 400)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_B7C4)

    @scena.Lambda('lambda_B7D2')
    def lambda_B7D2():
        ChrTurnDirection(0x00FE, 0x001C, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_B7D2)

    @scena.Lambda('lambda_B7E0')
    def lambda_B7E0():
        ChrTurnDirection(0x00FE, 0x001C, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_B7E0)

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110914V#004F#6P哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x001C, 0x0102, 400)

    ChrTalk(
        0x001C,
        (
            '#0090110915V#215F#2P虽然我们明天不能来这里看比赛了……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090110916V#214F但是你们，一定要赢哦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090110917V如果输给那些家伙，\n',
            '我可饶不了你们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110918V#501F#3P啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110919V#001F当然啦！就交给我们吧！\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110920V#010F绝对……会赢给你们看的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000F,
        '警卫兵',
        (
            '#2580110921V#5P……说完了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0010,
        '警卫兵',
        (
            '#2570110922V#5P走吧，不要浪费时间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)
    FadeOut(2000, 0, -1)

    @scena.Lambda('lambda_B997')
    def lambda_B997():
        ChrMoveToRelative(0x00FE, 7000, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_B997)

    @scena.Lambda('lambda_B9B2')
    def lambda_B9B2():
        ChrMoveToRelative(0x00FE, 7000, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_B9B2)

    Sleep(300)

    @scena.Lambda('lambda_B9D2')
    def lambda_B9D2():
        ChrMoveToRelative(0x00FE, 7000, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_B9D2)

    @scena.Lambda('lambda_B9ED')
    def lambda_B9ED():
        ChrMoveToRelative(0x00FE, 6380, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_B9ED)

    Sleep(300)

    @scena.Lambda('lambda_BA0D')
    def lambda_BA0D():
        ChrMoveToRelative(0x00FE, 6380, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_BA0D)

    @scena.Lambda('lambda_BA28')
    def lambda_BA28():
        ChrMoveToRelative(0x00FE, 6380, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_BA28)

    Sleep(300)

    @scena.Lambda('lambda_BA48')
    def lambda_BA48():
        ChrMoveToRelative(0x00FE, 6380, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_BA48)

    @scena.Lambda('lambda_BA63')
    def lambda_BA63():
        ChrMoveToRelative(0x00FE, 6380, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_BA63)

    OP_0D()
    Sleep(500)

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到奖金',
            (TxtCtl.SetColor, 0x4),
            '４００００',
            (TxtCtl.SetColor, 0x0),
            '米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(500)

    AddMira(40000)
    MapClearFlags(0x00100000)
    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/T4101._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0027 offset: 0xBAD5
@scena.Code('func_27_BAD5')
def func_27_BAD5():
    EventBegin(0x00)
    CameraMove(79580, 0, -62340, 0)
    OP_67(0, 6570, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(314000, 0)
    OP_6E(371, 0)
    ChrSetRGBAMask(0x0000, 255, 255, 255, 255, 0)
    ChrSetRGBAMask(0x0001, 255, 255, 255, 255, 0)
    ChrSetRGBAMask(0x0002, 255, 255, 255, 255, 0)
    ChrSetRGBAMask(0x0003, 255, 255, 255, 255, 0)
    ChrSetFlags(0x0025, 0x0080)
    ChrSetFlags(0x0026, 0x0080)
    ChrSetPos(0x0101, 81740, 0, -63700, 270)
    ChrSetPos(0x0102, 82090, 0, -62760, 270)
    ChrSetPos(0x0104, 80420, 0, -63500, 270)
    ChrSetPos(0x0108, 80850, 0, -62320, 270)
    FadeIn(1500, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010111531V#008F哈～现在这里只有我们，\n',
            '显得真是宽敞啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111532V#010F这里是为团体竞技、马戏表演等活动\n',
            '而建造的建筑设施啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111533V以前，好像还曾经举行过\n',
            '人和大型魔兽战斗的表演呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111534V#006F哎～是这样啊，\n',
            '所以才有这么大的休息室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040111535V#035F#5P虽然和帝都的歌剧院比起来，\n',
            '这里的设施还略显不足……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040111536V不过这里也有这里的特色，\n',
            '举办一场室外音乐会也不是不可以的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0104, 400)

    ChrTalk(
        0x0101,
        (
            '#0010111537V#509F这是什么话啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0108, 135, 400)

    ChrTalk(
        0x0108,
        (
            '#0080111538V#070F#2P话说回来，\n',
            '今天我们好像来得太早了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080111539V仔细想想，只剩一场比赛了，\n',
            '开始时间应该会晚一些。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_BDEC')
    def lambda_BDEC():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_BDEC)

    @scena.Lambda('lambda_BDFA')
    def lambda_BDFA():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_BDFA)

    ChrTurnDirection(0x0101, 0x0108, 400)

    ChrTalk(
        0x0101,
        (
            '#0010111540V#004F哎，是这样吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111541V#007F嗯……就这样只是等着比赛开始，\n',
            '我还是会有点紧张呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020111542V#010F那么在比赛开始之前，\n',
            '我们就在场内散散步吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010111543V#001F嗯，好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_BEED')
    def lambda_BEED():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_BEED)

    ChrTurnDirection(0x0101, 0x0108, 400)

    ChrTalk(
        0x0101,
        (
            '#0010111544V#006F金先生，奥利维尔。\n',
            '那我们就去散步了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080111545V#070F#2P好，到时间就赶快回来哦。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_BF73')
    def lambda_BF73():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_BF73')

    DispatchAsync2(0x0104, 0x0001, lambda_BF73)

    @scena.Lambda('lambda_BF84')
    def lambda_BF84():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_BF84')

    DispatchAsync2(0x0108, 0x0001, lambda_BF84)

    @scena.Lambda('lambda_BF95')
    def lambda_BF95():
        CameraMove(81340, 0, -62730, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_BF95)

    @scena.Lambda('lambda_BFAD')
    def lambda_BFAD():
        OP_6E(314, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_BFAD)

    ChrSetDirection(0x0101, 90, 400)

    @scena.Lambda('lambda_BFC4')
    def lambda_BFC4():
        ChrWalkTo(0x00FE, 85380, 0, -63500, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_BFC4)

    Sleep(400)

    ChrSetDirection(0x0102, 90, 400)

    @scena.Lambda('lambda_BFEB')
    def lambda_BFEB():
        ChrWalkTo(0x00FE, 85500, 0, -62300, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_BFEB)

    WaitForThreadExit(0x0101, 0x0001)
    PlaySE(6, 0x00, 0x64)
    Sleep(50)

    @scena.Lambda('lambda_C015')
    def lambda_C015():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_C015)

    @scena.Lambda('lambda_C027')
    def lambda_C027():
        ChrWalkTo(0x00FE, 87410, 0, -63500, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_C027)

    WaitForThreadExit(0x0102, 0x0001)

    @scena.Lambda('lambda_C047')
    def lambda_C047():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_C047)

    @scena.Lambda('lambda_C059')
    def lambda_C059():
        ChrWalkTo(0x00FE, 87510, 0, -62300, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_C059)

    WaitForThreadExit(0x0102, 0x0002)
    PlaySE(7, 0x00, 0x64)
    Sleep(500)

    ChrTalk(
        0x0104,
        (
            '#0040111546V#030F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_C0B0')
    def lambda_C0B0():
        CameraMove(80340, 0, -62730, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_C0B0)

    Sleep(400)

    TerminateThread(0x0108, 0xFF)
    ChrTurnDirection(0x0108, 0x0104, 400)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0108,
        (
            '#0080111547V#073F#2P哎。今天这是吹的什么风啊？\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080111548V我还以为你肯定会粘着他们一起去的。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0104, 0xFF)
    ChrTurnDirection(0x0104, 0x0108, 400)

    ChrTalk(
        0x0104,
        (
            '#0040111549V#035F#6P没什么，我只是觉得\n',
            '他们两个之间的气氛稍微有点改变。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040111550V好像有所进展呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080111551V#073F#2P哈哈，你很了解嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080111552V#070F确实，他们两个看起来在大会上\n',
            '承受着奇怪的压力……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080111553V不过今天从他们的表情看来，\n',
            '这种压力好像烟消云散了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080111554V#071F哎呀，真是羡慕年轻人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040111555V#031F#6P不过，他们两个嘛……\n',
            '需要加深感情的地方还有很多呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040111556V如果能有进一步发展的话，\n',
            '相信他们会享受到爱情甜蜜的喜悦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040111557V#037F呵呵……\n',
            '看来我善意的讥讽还是挺有效的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080111558V#075F#2P哎呀哎呀，真是恶趣味……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    CameraMove(84790, 0, 33020, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FormationDelMember(0x07, 0xFF)
    FormationDelMember(0x03, 0xFF)
    ChrSetPos(0x0101, 85160, 0, 32390, 90)
    ChrSetPos(0x0102, 85170, 0, 33380, 90)
    ChrClearFlags(0x0025, 0x0080)
    ChrClearFlags(0x0026, 0x0080)
    ChrSetPos(0x0025, 80420, 0, -63670, 0)
    ChrSetPos(0x0026, 80420, 0, -62320, 180)
    CreateThread(0x0025, 0x00, 0x00, func_02_902)
    CreateThread(0x0026, 0x00, 0x00, func_02_902)
    ChrSetRGBAMask(0x0000, 255, 255, 255, 255, 0)
    ChrSetRGBAMask(0x0001, 255, 255, 255, 255, 0)
    OP_0D()
    OP_9E(0x0101, 15, 0, 300, 4000)

    ChrTalk(
        0x0101,
        (
            '#0010111559V#009F……（哆嗦）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020111560V#014F怎么了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111561V是不是身体不舒服？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010111562V#509F没什么……\n',
            '只是感觉到有股邪恶的意念……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111563V老是把别人的隐私当作自己的乐趣，\n',
            '一想起他那副玩世不恭的模样我就……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111564V#017F……呵呵，\n',
            '我大概能想象得出是谁在作怪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0049, 0x01, 0x0008)
    EventEnd(0x00)

    Return()

# id: 0x0028 offset: 0xC5B3
@scena.Code('func_28_C5B3')
def func_28_C5B3():
    EventBegin(0x00)
    ChrClearFlags(0x001E, 0x0080)

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x66),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C60D',
    )

    ChrSetPos(0x0101, 11050, 0, 5180, 270)
    ChrSetPos(0x0102, 11120, 0, 6310, 270)
    ChrSetPos(0x001E, 1660, 0, 3830, 90)
    CameraMove(10420, 0, 6050, 0)

    Jump('loc_C651')

    def _loc_C60D(): pass

    label('loc_C60D')

    ChrSetPos(0x0101, -11040, 0, 5190, 90)
    ChrSetPos(0x0102, -10950, 0, 6290, 90)
    ChrSetPos(0x001E, -2060, 0, 5520, 270)
    CameraMove(-10910, 0, 5550, 0)

    def _loc_C651(): pass

    label('loc_C651')

    FadeIn(1000, 0)
    OP_0D()

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x66),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CFE2',
    )

    NpcTalk(
        0x001E,
        '老人的声音',
        (
            '#0340111638V#4P哦哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x001E,
        '老人的声音',
        (
            '#0340111639V#4P你们……\n',
            '这不是艾丝蒂尔和约修亚嘛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    CameraMove(6960, 0, 4810, 2000)

    ChrTalk(
        0x0101,
        (
            '#0010111640V#004F啊啊，是克劳斯市长！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111641V#014F为什么您会在这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_C774')
    def lambda_C774():
        ChrTurnDirection(0x00FE, 0x001E, 0)
        Yield()

        Jump('lambda_C774')

    DispatchAsync2(0x0101, 0x0001, lambda_C774)

    @scena.Lambda('lambda_C785')
    def lambda_C785():
        ChrTurnDirection(0x00FE, 0x001E, 0)
        Yield()

        Jump('lambda_C785')

    DispatchAsync2(0x0102, 0x0001, lambda_C785)

    @scena.Lambda('lambda_C796')
    def lambda_C796():
        ChrWalkTo(0x00FE, 6040, 0, 4750, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0002, lambda_C796)

    Sleep(300)

    @scena.Lambda('lambda_C7B6')
    def lambda_C7B6():
        ChrWalkTo(0x00FE, 7570, 0, 4470, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_C7B6)

    Sleep(300)

    @scena.Lambda('lambda_C7D6')
    def lambda_C7D6():
        ChrWalkTo(0x00FE, 7160, 0, 5630, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_C7D6)

    WaitForThreadExit(0x001E, 0x0002)
    ChrSetDirection(0x001E, 90, 400)

    ChrTalk(
        0x001E,
        (
            '#0340111642V#601F哎呀，真是好久不见了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340111643V我听雪拉扎德说了，\n',
            '你们为了成为正游击士\n',
            '在王国各地旅行的事情……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340111644V这么长时间不见，\n',
            '你们都成熟了不少嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111645V#019F哈哈……谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111646V#506F嗯～～\n',
            '我自己倒没有什么感觉……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111647V#501F市长爷爷还是这么有精神呢。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111648V这样我就放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001E,
        (
            '#0340111649V#601F哈哈，\n',
            '我可是还不会输给年轻人的哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340111650V对了，\n',
            '你们不是闯进决赛了嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340111651V所以我不顾这一把老骨头\n',
            '就赶来观看比赛了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111652V#004F哎，您是为了看比赛\n',
            '从洛连特过来的吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001E,
        (
            '#0340111653V#600F不，不是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340111654V其实，是突然收到了\n',
            '格兰赛尔城的晚宴的邀请信。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340111655V所以今天早上才乘定期船\n',
            '刚刚到达王都。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111656V#580F王城的晚宴！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111657V#015F原来如此……\n',
            '是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111658V#010F那个晚宴，\n',
            '是不是杜南公爵举办的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001E,
        (
            '#0340111659V#604F原来你知道啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340111660V#600F本来我们夫妇是要在\n',
            '诞辰庆典的仪式上出席的，\n',
            '所以最近肯定会来王都……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340111661V不过突然有一位军队的女性军官\n',
            '来邀请我们参加晚餐会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111662V#002F（那个女性军官……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111663V#012F（一定就是凯诺娜上尉了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001E,
        (
            '#0340111664V#603F不过，\n',
            '米蕾奴还没有做好旅行的准备。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340111665V所以没办法，\n',
            '我就一个人先来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111666V#007F是吗……\n',
            '米蕾奴婶婶没有来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111667V#010F对了，市长爷爷。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111668V其实，\n',
            '我们说不定也会出席晚宴呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001E,
        (
            '#0340111669V#604F哦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '约修亚向克劳斯市长说明了\n',
            '因公爵的提案，武术大会优胜者会被招待参加晚宴的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x001E,
        (
            '#0340111670V#604F原来如此……\n',
            '还有这样的事啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340111671V#600F本来在陛下身体欠佳的时候，\n',
            '不太想出席晚宴什么的……  ',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340111672V和你们一起的话，\n',
            '也就可以转换一下心情了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340111673V#601F这下子，\n',
            '你们就更必须得赢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111674V#001F啊哈哈……\n',
            '嗯，我知道了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111675V#010F我们一定会努力，不辜负您的期待的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001E,
        (
            '#0340111676V#600F那么，\n',
            '我就到观众席去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340111677V加油啊。\n',
            '艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x001E, 8039, 0, 2550, 3000, 0x00)
    ChrWalkTo(0x001E, 11630, 0, 5800, 3000, 0x00)

    @scena.Lambda('lambda_CFBA')
    def lambda_CFBA():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_CFBA)

    ChrWalkTo(0x001E, 13690, 0, 5800, 3000, 0x00)
    PlaySE(7, 0x00, 0x64)

    Jump('loc_D970')

    def _loc_CFE2(): pass

    label('loc_CFE2')

    NpcTalk(
        0x001E,
        '老人的声音',
        (
            '#0340111678V#1P哦哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x001E,
        '老人的声音',
        (
            '#0340111679V#1P你们……\n',
            '这不是艾丝蒂尔和约修亚嘛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    CameraMove(-6910, 0, 5920, 2000)

    ChrTalk(
        0x0101,
        (
            '#0010111640V#004F啊啊，是克劳斯市长！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111681V#014F为什么您会在这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_D0EF')
    def lambda_D0EF():
        ChrTurnDirection(0x00FE, 0x001E, 0)
        Yield()

        Jump('lambda_D0EF')

    DispatchAsync2(0x0101, 0x0001, lambda_D0EF)

    @scena.Lambda('lambda_D100')
    def lambda_D100():
        ChrTurnDirection(0x00FE, 0x001E, 0)
        Yield()

        Jump('lambda_D100')

    DispatchAsync2(0x0102, 0x0001, lambda_D100)

    @scena.Lambda('lambda_D111')
    def lambda_D111():
        ChrWalkTo(0x00FE, -5900, 0, 5760, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0002, lambda_D111)

    Sleep(300)

    @scena.Lambda('lambda_D131')
    def lambda_D131():
        ChrWalkTo(0x00FE, -7600, 0, 5320, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_D131)

    Sleep(300)

    @scena.Lambda('lambda_D151')
    def lambda_D151():
        ChrWalkTo(0x00FE, -7530, 0, 6580, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_D151)

    WaitForThreadExit(0x001E, 0x0002)

    ChrTalk(
        0x001E,
        (
            '#0340111642V#601F哎呀，真是好久不见了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340111643V我听雪拉扎德说了，\n',
            '你们为了成为正游击士\n',
            '在王国各地旅行的事情……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340111644V这么长时间不见，\n',
            '你们都成熟了不少嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111645V#019F哈哈……谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111646V#506F嗯～～\n',
            '我自己倒没有什么感觉……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111647V#501F市长爷爷还是这么有精神呢。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111648V这样我就放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001E,
        (
            '#0340111649V#601F哈哈，\n',
            '我可是还不会输给年轻人的哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340111650V对了，\n',
            '你们不是闯进决赛了嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340111651V所以我不顾这一把老骨头\n',
            '就赶来观看比赛了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111652V#004F哎，您是为了看比赛\n',
            '从洛连特过来的吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001E,
        (
            '#0340111653V#600F不，不是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340111654V其实，是突然收到了\n',
            '格兰赛尔城的晚宴的邀请信。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340111655V所以今天早上才乘定期船\n',
            '刚刚到达王都。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111656V#580F王城的晚宴！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111657V#015F原来如此……\n',
            '是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111658V#010F那个晚宴，\n',
            '是不是杜南公爵举办的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001E,
        (
            '#0340111659V#604F原来你知道啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340111660V#600F本来我们夫妇是要在\n',
            '诞辰庆典的仪式上出席的，\n',
            '所以最近肯定会来王都……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340111661V不过突然有一位军队的女性军官\n',
            '来邀请我们参加晚餐会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111662V#002F（那个女性军官……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111663V#012F（一定就是凯诺娜上尉了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001E,
        (
            '#0340111664V#603F不过，\n',
            '米蕾奴还没有做好旅行的准备。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340111665V所以没办法，\n',
            '我就一个人先来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111666V#007F是吗……\n',
            '米蕾奴婶婶没有来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111667V#010F对了，市长爷爷。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111668V其实，\n',
            '我们说不定也会出席晚宴呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001E,
        (
            '#0340111669V#604F哦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '约修亚向克劳斯市长说明了\n',
            '因公爵的提案，武术大会优胜者会被招待参加晚宴的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x001E,
        (
            '#0340111670V#604F原来如此……\n',
            '还有这样的事啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340111671V#600F本来在陛下身体欠佳的时候，\n',
            '不太想出席晚宴什么的……  ',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340111672V和你们一起的话，\n',
            '也就可以转换一下心情了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340111673V#601F这下子，\n',
            '你们就更必须得赢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111674V#001F啊哈哈……\n',
            '嗯，我知道了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111675V#010F我们一定会努力，不辜负您的期待的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001E,
        (
            '#0340111676V#600F那么，\n',
            '我就到观众席去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340111677V加油啊。\n',
            '艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x001E, -7360, 0, 4120, 3000, 0x00)
    ChrWalkTo(0x001E, -11330, 0, 5740, 3000, 0x00)
    ChrSetDirection(0x001E, 270, 400)
    OP_70(0x0001, 30)
    OP_73(0x0001)

    @scena.Lambda('lambda_D93F')
    def lambda_D93F():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_D93F)

    ChrWalkTo(0x001E, -13110, 0, 6020, 3000, 0x00)
    OP_72(0x0001, 0x0800)
    PlaySE(7, 0x00, 0x64)
    OP_70(0x0001, 0)

    def _loc_D970(): pass

    label('loc_D970')

    Sleep(500)

    OP_71(0x0001, 0x0800)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010111718V#505F没想到克劳斯市长\n',
            '也要出席晚宴啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111719V那么，梅贝尔市长她们\n',
            '是不是也被邀请了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020111720V#012F很有可能。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111721V把这些有权力的官员们集中在一起，\n',
            '是不是有什么重要的事情宣布啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111722V#007F嗯……算了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111723V#006F不管怎么说先把比赛赢下来，\n',
            '只要能参加晚宴，一切不就知道了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111724V#010F嗯，也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111725V我们也该回休息室了吧。\n',
            '快要到开场的时候了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111726V#006F嗯，知道了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0049, 0x01, 0x0010)
    EventEnd(0x00)

    Return()

# id: 0x0029 offset: 0xDB66
@scena.Code('func_29_DB66')
def func_29_DB66():
    SetScenaFlags(ScenaFlag(0x007E, 2, 0x3F2))
    NewScene('ED6_DT01/T4104._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x002A offset: 0xDB73
@scena.Code('func_2A_DB73')
def func_2A_DB73():
    EventBegin(0x00)
    CameraMove(75070, 0, -63440, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FormationAddMember(0x03, 0xFF)
    FormationAddMember(0x07, 0xFF)
    ChrSetPos(0x0101, 75600, 0, -63280, 270)
    ChrSetPos(0x0102, 76550, 0, -62310, 270)
    ChrSetPos(0x0104, 76600, 0, -64489, 270)
    ChrSetPos(0x0108, 77680, 0, -63300, 270)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010111729V#580F啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111730V今天理查德上校也和公爵一起来了啊！\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111731V#012F是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111732V是作为公爵的随行人员，\n',
            '顺道来看自己部下的比赛的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080111733V#070F哦，那就是街头巷尾很有人气的\n',
            '王国军情报部的首领啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080111734V仪表堂堂，又有风度，\n',
            '看起来是个相当厉害的人物呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111735V#007F嗯……\n',
            '这样说也没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040111736V#033F唔～那个男人……\n',
            '比在柏斯见到的时候更加风度翩翩了呢。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040111737V#035F哼，真没有办法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040111738V只好承认他为\n',
            '我奥利维尔·朗海姆的对手了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0104, 400)

    ChrTalk(
        0x0101,
        (
            '#0010111739V#509F#5P谁也没有要把你当成对手吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111740V#012F……好像要开始了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 270, 400)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('主持人的声音')

    Talk(
        (
            '#2200110180V',
            (TxtCtl.SetColor, 0x5),
            '各位……\n',
            '让你们久等了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#2200111742V',
            (TxtCtl.SetColor, 0x5),
            '我宣布，武术大会正式赛，\n',
            '最后的决赛现在开始！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(1000, 0)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007E, 3, 0x3F3))
    NewScene('ED6_DT01/T4104._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x002B offset: 0xDF12
@scena.Code('func_2B_DF12')
def func_2B_DF12():
    EventBegin(0x00)
    CameraMove(76480, 0, -63310, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 75600, 0, -63280, 90)
    ChrSetPos(0x0102, 76550, 0, -62310, 180)
    ChrSetPos(0x0104, 76600, 0, -64489, 0)
    ChrSetPos(0x0108, 77680, 0, -63300, 270)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010111749V#508F好，我们上场吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111750V#012F终于……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040111751V#035F哼～\n',
            '这次我就认真一回吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080111752V#074F不管结果是哭还是笑，\n',
            '这都是战斗的最后时刻了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080111753V#076F鼓足干劲上吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)
    OP_1B(0x0C, 0x00, 0xFFFF)
    OP_1B(0x0B, 0x00, 0x0030)

    Return()

# id: 0x002C offset: 0xE084
@scena.Code('func_2C_E084')
def func_2C_E084():
    EventBegin(0x00)
    OP_24(0x00AE, 0x50)
    CameraMove(-80090, 0, -63100, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrClearFlags(0x001F, 0x0080)
    ChrClearFlags(0x0020, 0x0080)
    ChrClearFlags(0x0021, 0x0080)
    ChrSetPos(0x001F, -82950, 0, -63110, 90)
    ChrSetPos(0x0020, -82500, 0, -64220, 90)
    ChrSetPos(0x0021, -82420, 0, -61920, 180)
    MapClearFlags(0x00100000)
    CameraMove(-82600, 0, -63080, 2000)

    ChrTalk(
        0x001F,
        (
            '#0130111808V#111F呵呵，那些有趣的家伙取得优胜了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0020, 0x0021, 400)

    ChrTalk(
        0x0020,
        (
            '#0610111809V#183F真是的……\n',
            '你也应该知道耻辱了吧，洛伦斯少尉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610111810V让那样初出茅庐的小孩子占了上风，\n',
            '实在是给上校的脸上抹黑……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610111811V平时那种狂妄自大的态度\n',
            '难道都是装出来的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0021,
        (
            '#0140111812V#281F……抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '#0130111813V#110F哈哈，凯诺娜。\n',
            '不要这么责怪洛伦斯嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130111814V其实是我拜托他不要使出全力的。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#0610111815V#184F哎……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '#0130111816V#115F情报部因为本身的性质，\n',
            '不能这么容易摆脱黑子的角色。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130111817V就这样让众星云集的小组获得优胜\n',
            '应该是众望所归的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#0610111818V#180F原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610111819V#181F看起来公爵大人对那个东方人\n',
            '比我们想象中的更感兴趣呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610111820V说不定想拿回王城当作玩具熊呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '#0130111821V#110F不过……\n',
            '今年的大会有点遗憾啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130111822V王室亲卫队队长的舒华兹中尉\n',
            '还有摩尔根将军如果能来参加的话，\n',
            '就会更加精彩纷呈了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#0610111823V#182F呵呵，请不要开玩笑……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610111824V如果这样的话，\n',
            '上校您亲自参加不是更好吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610111825V那个狂妄的尤莉亚什么的\n',
            '根本连您的一个脚趾头都比不上呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '#0130111826V#111F哈哈，我可不打算\n',
            '变成这样一个自信家啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130111827V如果洛伦斯使出全力的话，\n',
            '我也不一定能胜过呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0021,
        (
            '#0140111828V#281F……请不要开玩笑了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140111829V上校您实在是太抬举我了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140111830V我有幸徒得军人的名号，\n',
            '实际上不过是个所谓猎兵的草莽匹夫罢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '#0130111831V#110F就算你说得这么谦虚，\n',
            '我理查德也是绝对不会看错人的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130111832V真正能做你的对手也只有那个男人吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0021,
        (
            '#0140111833V#281F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#0610111834V#183F是指『他』吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610111835V这样下去的话，\n',
            '他的孩子就要进入格兰赛尔城了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610111836V要不要采取什么措施？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '#0130111837V#110F不用管了。\n',
            '这是杜南公爵定下的事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130111838V#115F现在就算游击士协会出面干涉，\n',
            '也不可能阻止我们计划的进行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#0610111839V#184F可、可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '#0130111840V#112F……洛伦斯。\n',
            '计划进展得如何了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0021,
        (
            '#0140111841V#280F现在已经超过９０％了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140111842V再过一两天应该就可以\n',
            '带上校到最后的地方去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '#0130111843V#110F好，太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_E8EC')
    def lambda_E8EC():
        CameraMove(-80600, 0, -63080, 1500)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_E8EC)

    @scena.Lambda('lambda_E904')
    def lambda_E904():
        ChrWalkTo(0x00FE, -80700, 0, -63110, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0002, lambda_E904)

    Sleep(400)

    @scena.Lambda('lambda_E924')
    def lambda_E924():
        ChrTurnDirection(0x00FE, 0x001F, 400)
        Yield()

        Jump('lambda_E924')

    DispatchAsync2(0x0021, 0x0001, lambda_E924)

    @scena.Lambda('lambda_E935')
    def lambda_E935():
        ChrSetDirection(0x00FE, 90, 200)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_E935)

    WaitForThreadExit(0x001F, 0x0001)
    WaitForThreadExit(0x001F, 0x0002)
    Sleep(400)

    ChrTalk(
        0x001F,
        (
            '#0130111844V#115F……王国的黎明就要来到了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130111845V#111F就算背负上逆贼的罪名，\n',
            '也一定要用我这双手开拓未来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    FadeOut(1500, 0, -1)
    OP_24(0x00AE, 0x5A)
    Sleep(100)

    OP_24(0x00AE, 0x50)
    Sleep(100)

    OP_24(0x00AE, 0x46)
    Sleep(100)

    OP_24(0x00AE, 0x3C)
    Sleep(100)

    OP_24(0x00AE, 0x28)
    Sleep(100)

    OP_23(0x00AE)
    OP_0D()
    Sleep(1000)

    SetScenaFlags(ScenaFlag(0x007F, 6, 0x3FE))
    NewScene('ED6_DT01/T4101._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x002D offset: 0xEA15
@scena.Code('func_2D_EA15')
def func_2D_EA15():
    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_EAD6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_EA9D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020111498V#014F艾丝蒂尔，这里是出口啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111499V#004F哎呀……\n',
            '现在这个时候不能走呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EAD3')

    def _loc_EA9D(): pass

    label('loc_EA9D')

    ChrTalk(
        0x0101,
        (
            '#0010111500V#002F好像一旦出去\n',
            '就不能再进来了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EAD3(): pass

    label('loc_EAD3')

    Jump('loc_EBC1')

    def _loc_EAD6(): pass

    label('loc_EAD6')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_EB28',
    )

    ChrTalk(
        0x0102,
        (
            '#0020111501V#010F这里是出口吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111502V现在还不能出去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EBC1')

    def _loc_EB28(): pass

    label('loc_EB28')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_EB98',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_EB69',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0108,
        (
            '#0080111503V#074F哦，这边是出口。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EB95')

    def _loc_EB69(): pass

    label('loc_EB69')

    ChrTalk(
        0x0108,
        (
            '#0080111504V#070F唔，\n',
            '现在还不能回去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EB95(): pass

    label('loc_EB95')

    Jump('loc_EBC1')

    def _loc_EB98(): pass

    label('loc_EB98')

    ChrTalk(
        0x0104,
        (
            '#0040111505V#030F唔，这边是出口呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EBC1(): pass

    label('loc_EBC1')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x002E offset: 0xEBDD
@scena.Code('func_2E_EBDD')
def func_2E_EBDD():
    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '贵宾席，无关人等禁止入内。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x002F offset: 0xEC33
@scena.Code('func_2F_EC33')
def func_2F_EC33():
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

# id: 0x0030 offset: 0xEC83
@scena.Code('func_30_EC83')
def func_30_EC83():
    EventBegin(0x02)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 5, 0x61D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_ECBD',
    )

    ChrTalk(
        0x0101,
        (
            '#0010111506V#501F啊，往这边去是走廊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EE94')

    def _loc_ECBD(): pass

    label('loc_ECBD')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_ED4E',
    )

    ChrTurnDirection(0x0108, 0x0000, 400)

    ChrTalk(
        0x0108,
        (
            '#0080111507V#070F喂，那里是走廊啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080111508V去比赛场地，\n',
            '要走对面那个出口才对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111509V#505F啊，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EE94')

    def _loc_ED4E(): pass

    label('loc_ED4E')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_EDBE',
    )

    ChrTurnDirection(0x0108, 0x0000, 400)

    ChrTalk(
        0x0108,
        (
            '#0080111507V#070F喂，那里是走廊啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080111508V去比赛场地，\n',
            '要走对面那个出口才对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EE94')

    def _loc_EDBE(): pass

    label('loc_EDBE')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_EDF4',
    )

    ChrTalk(
        0x0108,
        (
            '#0080111512V#070F哦，这边是走廊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EE94')

    def _loc_EDF4(): pass

    label('loc_EDF4')

    ChrTurnDirection(0x0108, 0x0000, 400)

    ChrTalk(
        0x0108,
        (
            '#0080111507V#070F喂，那里是走廊啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080111508V去比赛场地，\n',
            '要走对面那个出口才对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0104, 0x0108, 400)

    ChrTalk(
        0x0104,
        (
            '#0040111515V#035F呼，我当然知道。\n',
            '开个玩笑而已嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EE94(): pass

    label('loc_EE94')

    ChrMoveToRelative(0x0000, -1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0031 offset: 0xEEB0
@scena.Code('func_31_EEB0')
def func_31_EEB0():
    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 5, 0x61D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_EF28',
    )

    ChrTalk(
        0x0101,
        (
            '#0010111516V#002F这里就是比赛场的入口了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111517V#003F唔～冷静不下来啊。\n',
            '还没轮到我们出场吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F008')

    def _loc_EF28(): pass

    label('loc_EF28')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_EFA0',
    )

    ChrTalk(
        0x0101,
        (
            '#0010111518V#000F啊，\n',
            '就算进了比赛场也没用。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111519V还有一些时间，\n',
            '我们就在竞技场内散散步吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F008')

    def _loc_EFA0(): pass

    label('loc_EFA0')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F008',
    )

    ChrTalk(
        0x0102,
        (
            '#0020111520V#010F这边是场内……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111521V到比赛开始还有些时间，\n',
            '在这附近散散步吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F008(): pass

    label('loc_F008')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0032 offset: 0xF024
@scena.Code('func_32_F024')
def func_32_F024():
    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 3, 0x61B)),
            Expr.Return,
        ),
        'loc_F1C3',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F0CE',
    )

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020111522V#014F艾丝蒂尔，我们走错地方了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111523V我们的休息室\n',
            '是在另外一边的房间才对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111524V#505F啊，是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F1C0')

    def _loc_F0CE(): pass

    label('loc_F0CE')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F14B',
    )

    ChrTalk(
        0x0102,
        (
            '#0020111525V#010F这里是『红之组』的房间……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111526V我们的休息室应该是\n',
            '另外一边的『苍之组』的房间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F1C0')

    def _loc_F14B(): pass

    label('loc_F14B')

    ChrTurnDirection(0x0102, 0x0000, 400)

    ChrTalk(
        0x0102,
        (
            '#0020111527V#010F这里是『红之组』的休息室。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111528V我们的休息室应该是\n',
            '另外一边的『苍之组』的房间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F1C0(): pass

    label('loc_F1C0')

    Jump('loc_F233')

    def _loc_F1C3(): pass

    label('loc_F1C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 5, 0x60D)),
            Expr.Return,
        ),
        'loc_F233',
    )

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020111529V#010F这里应该就是选手休息室了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111530V不能打扰选手，\n',
            '我们还是别进去了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F233(): pass

    label('loc_F233')

    ChrMoveToRelative(0x0000, -1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4136_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4136   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '卡露娜'),
    TXT(0x02, '亚妮拉丝'),
    TXT(0x03, '库拉茨'),
    TXT(0x04, '克鲁茨'),
    TXT(0x05, '迪恩'),
    TXT(0x06, '雷斯'),
    TXT(0x07, '洛克'),
    TXT(0x08, '士兵艾扎克'),
    TXT(0x09, '士兵赛恩'),
    TXT(0x0A, '士兵塔里斯'),
    TXT(0x0B, '士兵拜安'),
    TXT(0x0C, '士兵密克里亚'),
    TXT(0x0D, '士兵格古'),
    TXT(0x0E, '士兵'),
    TXT(0x0F, '莱尔中尉'),
    TXT(0x10, '贝伦中尉'),
    TXT(0x11, '迪鲁队长'),
    TXT(0x12, '莱尔'),
    TXT(0x13, '多伦'),
    TXT(0x14, '吉尔'),
    TXT(0x15, '乔丝特'),
    TXT(0x16, '朵洛希'),
    TXT(0x17, '克劳斯市长'),
    TXT(0x18, '理查德上校'),
    TXT(0x19, '凯诺娜上尉'),
    TXT(0x1A, '洛伦斯少尉'),
    TXT(0x1B, '斯妮亚'),
    TXT(0x1C, '科娜克'),
    TXT(0x1D, '约修亚'),
    TXT(0x1E, '奥利维尔'),
    TXT(0x1F, '金'),
    TXT(0x20, ''),
]

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

# id: 0xFFFF offset: 0xE347
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
            word_3A         = 186,
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
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
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
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
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

# id: 0x10003 offset: 0x54A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x54A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x54A
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
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_654',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x0012)

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
    Event(0, 0x0016)

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
    Event(0, 0x0018)

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
    Event(0, 0x0019)

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
    Event(0, 0x001A)

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
    Event(0, 0x001C)

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
    Event(0, 0x001D)

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
    Event(0, 0x001F)

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
    Event(0, 0x0023)

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
    Event(0, 0x0025)

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
    Event(0, 0x0026)

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
    Event(0, 0x0027)

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
    Event(0, 0x002A)

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
    Event(0, 0x002B)

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
    Event(0, 0x002C)

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
    Event(0, 0x0028)

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
    Event(0, 0x0013)

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
    Event(0, 0x0029)

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
    Event(0, 0x0022)

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

    ClearChrFlags(0x0025, 0x0080)
    ClearChrFlags(0x0026, 0x0080)
    SetChrPos(0x0025, 80420, 0, -63670, 0)
    SetChrPos(0x0026, 80420, 0, -62320, 180)
    CreateThread(0x0025, 0x00, 0x00, 0x0002)
    CreateThread(0x0026, 0x00, 0x00, 0x0002)

    def _loc_800(): pass

    label('loc_800')

    Return()

# id: 0x0001 offset: 0x801
@scena.Code('Init')
def Init():
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
@scena.Code('ReInit')
def ReInit():
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

# id: 0x0004 offset: 0xB22
@scena.Code('func_04_B22')
def func_04_B22():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 1, 0x631)),
            Expr.Return,
        ),
        'loc_BE7',
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

    Jump('loc_C55')

    def _loc_BE7(): pass

    label('loc_BE7')

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

    def _loc_C55(): pass

    label('loc_C55')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0xC59
@scena.Code('func_05_C59')
def func_05_C59():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 1, 0x631)),
            Expr.Return,
        ),
        'loc_CF2',
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

    Jump('loc_D66')

    def _loc_CF2(): pass

    label('loc_CF2')

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

    def _loc_D66(): pass

    label('loc_D66')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0xD6A
@scena.Code('func_06_D6A')
def func_06_D6A():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 5, 0x61D)),
            Expr.Return,
        ),
        'loc_DEB',
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

    Jump('loc_EF0')

    def _loc_DEB(): pass

    label('loc_DEB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_E51',
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

    Jump('loc_EF0')

    def _loc_E51(): pass

    label('loc_E51')

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

    def _loc_EF0(): pass

    label('loc_EF0')

    Call(0, 0x0017)
    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0xEF8
@scena.Code('func_07_EF8')
def func_07_EF8():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 5, 0x61D)),
            Expr.Return,
        ),
        'loc_F3E',
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

    Jump('loc_106D')

    def _loc_F3E(): pass

    label('loc_F3E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_FA1',
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

    Jump('loc_106D')

    def _loc_FA1(): pass

    label('loc_FA1')

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

    def _loc_106D(): pass

    label('loc_106D')

    Call(0, 0x0017)
    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x1075
@scena.Code('func_08_1075')
def func_08_1075():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 5, 0x61D)),
            Expr.Return,
        ),
        'loc_10B7',
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

    Jump('loc_11AB')

    def _loc_10B7(): pass

    label('loc_10B7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_110B',
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

    Jump('loc_11AB')

    def _loc_110B(): pass

    label('loc_110B')

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

    def _loc_11AB(): pass

    label('loc_11AB')

    Call(0, 0x0017)
    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x11B3
@scena.Code('func_09_11B3')
def func_09_11B3():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 5, 0x61D)),
            Expr.Return,
        ),
        'loc_121F',
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

    Jump('loc_140F')

    def _loc_121F(): pass

    label('loc_121F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1290',
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

    Jump('loc_140F')

    def _loc_1290(): pass

    label('loc_1290')

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

    def _loc_140F(): pass

    label('loc_140F')

    Call(0, 0x0017)
    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x1417
@scena.Code('func_0A_1417')
def func_0A_1417():
    Call(0, 0x000B)

    Return()

# id: 0x000B offset: 0x141C
@scena.Code('func_0B_141C')
def func_0B_141C():
    TalkBegin(0x0023)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1429',
    )

    Jump('loc_163F')

    def _loc_1429(): pass

    label('loc_1429')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_1433',
    )

    Jump('loc_163F')

    def _loc_1433(): pass

    label('loc_1433')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_143D',
    )

    Jump('loc_163F')

    def _loc_143D(): pass

    label('loc_143D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_1447',
    )

    Jump('loc_163F')

    def _loc_1447(): pass

    label('loc_1447')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_149C',
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

    Jump('loc_163F')

    def _loc_149C(): pass

    label('loc_149C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_14A6',
    )

    Jump('loc_163F')

    def _loc_14A6(): pass

    label('loc_14A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_14EB',
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

    Jump('loc_163F')

    def _loc_14EB(): pass

    label('loc_14EB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_151E',
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

    Jump('loc_163F')

    def _loc_151E(): pass

    label('loc_151E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_1551',
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

    Jump('loc_163F')

    def _loc_1551(): pass

    label('loc_1551')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_1596',
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

    Jump('loc_163F')

    def _loc_1596(): pass

    label('loc_1596')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_163F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 7, 0x60F)),
            Expr.Return,
        ),
        'loc_15E9',
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

    Jump('loc_163F')

    def _loc_15E9(): pass

    label('loc_15E9')

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

    def _loc_163F(): pass

    label('loc_163F')

    TalkEnd(0x0023)

    Return()

# id: 0x000C offset: 0x1643
@scena.Code('func_0C_1643')
def func_0C_1643():
    Call(0, 0x000D)

    Return()

# id: 0x000D offset: 0x1648
@scena.Code('func_0D_1648')
def func_0D_1648():
    TalkBegin(0x0022)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1655',
    )

    Jump('loc_18A2')

    def _loc_1655(): pass

    label('loc_1655')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_165F',
    )

    Jump('loc_18A2')

    def _loc_165F(): pass

    label('loc_165F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_1669',
    )

    Jump('loc_18A2')

    def _loc_1669(): pass

    label('loc_1669')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_1673',
    )

    Jump('loc_18A2')

    def _loc_1673(): pass

    label('loc_1673')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1736',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_16CF',
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

    Jump('loc_1733')

    def _loc_16CF(): pass

    label('loc_16CF')

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

    def _loc_1733(): pass

    label('loc_1733')

    Jump('loc_18A2')

    def _loc_1736(): pass

    label('loc_1736')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_1740',
    )

    Jump('loc_18A2')

    def _loc_1740(): pass

    label('loc_1740')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_1789',
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

    Jump('loc_18A2')

    def _loc_1789(): pass

    label('loc_1789')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_1793',
    )

    Jump('loc_18A2')

    def _loc_1793(): pass

    label('loc_1793')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_17FC',
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

    Jump('loc_18A2')

    def _loc_17FC(): pass

    label('loc_17FC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_1806',
    )

    Jump('loc_18A2')

    def _loc_1806(): pass

    label('loc_1806')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_18A2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 7, 0x60F)),
            Expr.Return,
        ),
        'loc_185F',
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

    Jump('loc_18A2')

    def _loc_185F(): pass

    label('loc_185F')

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

    def _loc_18A2(): pass

    label('loc_18A2')

    TalkEnd(0x0022)

    Return()

# id: 0x000E offset: 0x18A6
@scena.Code('func_0E_18A6')
def func_0E_18A6():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_192F',
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

    Jump('loc_1A19')

    def _loc_192F(): pass

    label('loc_192F')

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

    def _loc_1A19(): pass

    label('loc_1A19')

    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x1A1D
@scena.Code('func_0F_1A1D')
def func_0F_1A1D():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 2, 0x12)),
            Expr.Return,
        ),
        'loc_1AA1',
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

    Jump('loc_1B5B')

    def _loc_1AA1(): pass

    label('loc_1AA1')

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

    def _loc_1B5B(): pass

    label('loc_1B5B')

    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x1B5F
@scena.Code('func_10_1B5F')
def func_10_1B5F():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1BE5',
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

    Jump('loc_1CD4')

    def _loc_1BE5(): pass

    label('loc_1BE5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 3, 0x13)),
            Expr.Return,
        ),
        'loc_1C3D',
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

    Jump('loc_1CD4')

    def _loc_1C3D(): pass

    label('loc_1C3D')

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

    def _loc_1CD4(): pass

    label('loc_1CD4')

    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0x1CD8
@scena.Code('func_11_1CD8')
def func_11_1CD8():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 4, 0x14)),
            Expr.Return,
        ),
        'loc_1D1E',
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

    Jump('loc_1D79')

    def _loc_1D1E(): pass

    label('loc_1D1E')

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

    def _loc_1D79(): pass

    label('loc_1D79')

    TalkEnd(0x00FE)

    Return()

# id: 0x0012 offset: 0x1D7D
@scena.Code('func_12_1D7D')
def func_12_1D7D():
    EventBegin(0x00)
    CameraMove(-570, 0, 16630, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 540, 0, 2040, 0)
    SetChrPos(0x0102, -550, 0, 1580, 0)
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

# id: 0x0013 offset: 0x1E98
@scena.Code('func_13_1E98')
def func_13_1E98():
    EventBegin(0x00)
    FadeIn(2000, 0)
    CameraMove(-88340, 0, -60660, 0)
    SetChrPos(0x0101, -89210, 0, -62630, 45)
    SetChrPos(0x0102, -89130, 0, -63770, 45)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x0008, -87270, 0, -59540, 135)
    SetChrPos(0x0009, -85710, 0, -59510, 180)
    SetChrPos(0x000A, -86540, 0, -61600, 45)
    SetChrPos(0x000B, -84960, 0, -60990, 315)
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

    @scena.Lambda('lambda_1FBF')
    def lambda_1FBF():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1FBF)

    @scena.Lambda('lambda_1FCD')
    def lambda_1FCD():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1FCD)

    @scena.Lambda('lambda_1FDB')
    def lambda_1FDB():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1FDB)

    @scena.Lambda('lambda_1FE9')
    def lambda_1FE9():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1FE9)

    ChrTalk(
        0x0009,
        (
            '#0120100997V#850F#2P啊，是两位新人啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_201E')
    def lambda_201E():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_201E')

    DispatchAsync2(0x0008, 0x0001, lambda_201E)

    @scena.Lambda('lambda_202F')
    def lambda_202F():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_202F')

    DispatchAsync2(0x0009, 0x0001, lambda_202F)

    @scena.Lambda('lambda_2040')
    def lambda_2040():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_2040')

    DispatchAsync2(0x000A, 0x0001, lambda_2040)

    @scena.Lambda('lambda_2051')
    def lambda_2051():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_2051')

    DispatchAsync2(0x000B, 0x0001, lambda_2051)

    @scena.Lambda('lambda_2062')
    def lambda_2062():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_2062')

    DispatchAsync2(0x0101, 0x0001, lambda_2062)

    @scena.Lambda('lambda_2073')
    def lambda_2073():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_2073')

    DispatchAsync2(0x0102, 0x0001, lambda_2073)

    @scena.Lambda('lambda_2084')
    def lambda_2084():
        CameraMove(-87430, 0, -59810, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2084)

    @scena.Lambda('lambda_209C')
    def lambda_209C():
        ChrWalkTo(0x00FE, -88420, 0, -60220, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_209C)

    Sleep(500)

    @scena.Lambda('lambda_20BC')
    def lambda_20BC():
        ChrWalkTo(0x00FE, -88150, 0, -61430, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_20BC)

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

    @scena.Lambda('lambda_2A75')
    def lambda_2A75():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_2A75')

    DispatchAsync2(0x0101, 0x0001, lambda_2A75)

    @scena.Lambda('lambda_2A86')
    def lambda_2A86():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_2A86')

    DispatchAsync2(0x0102, 0x0001, lambda_2A86)

    CreateThread(0x000A, 0x01, 0x00, 0x0014)
    Sleep(300)

    CreateThread(0x000B, 0x01, 0x00, 0x0014)
    Sleep(300)

    CreateThread(0x0009, 0x01, 0x00, 0x0014)
    Sleep(300)

    OP_72(0x0005, 0x0010)
    OP_6F(0x0005, 0)
    OP_70(0x0005, 29)
    Sleep(300)

    CreateThread(0x0008, 0x01, 0x00, 0x0014)
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
    SetChrFlags(0x0101, 0x0002)
    SetChrChipByIndex(0x0101, 23)
    SetChrSubChip(0x0101, 0)

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

    SetChrSubChip(0x0101, 1)

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
    ClearChrFlags(0x0101, 0x0002)
    SetChrChipByIndex(0x0101, 65535)
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

    @scena.Lambda('lambda_2FB2')
    def lambda_2FB2():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_2FB2')

    DispatchAsync2(0x0102, 0x0001, lambda_2FB2)

    @scena.Lambda('lambda_2FC3')
    def lambda_2FC3():
        ChrWalkTo(0x0101, -89630, 0, -62950, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2FC3)

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

# id: 0x0014 offset: 0x30D5
@scena.Code('func_14_30D5')
def func_14_30D5():
    SetChrFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, -87400, 0, -62970, 3000, 0x00)
    ChrWalkTo(0x00FE, -90080, 0, -62980, 3000, 0x00)

    @scena.Lambda('lambda_3108')
    def lambda_3108():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_3108)

    ChrWalkTo(0x00FE, -91260, 0, -62700, 2000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0015 offset: 0x312E
@scena.Code('func_15_312E')
def func_15_312E():
    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0104, 84960, 0, 33240, 270)
    SetChrPos(0x0102, 84840, 0, 32159, 270)
    SetChrPos(0x0101, 85910, 0, 32400, 270)
    SetChrPos(0x0108, 86160, 0, 33600, 270)
    SetChrPos(0x000C, 87840, 0, 24750, 0)
    SetChrPos(0x000D, 86780, 0, 23680, 0)
    SetChrPos(0x000E, 88160, 0, 23360, 0)
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

    @scena.Lambda('lambda_32EF')
    def lambda_32EF():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_32EF)

    @scena.Lambda('lambda_32FD')
    def lambda_32FD():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_32FD)

    @scena.Lambda('lambda_330B')
    def lambda_330B():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_330B)

    @scena.Lambda('lambda_3319')
    def lambda_3319():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_3319)

    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    CameraMove(86060, 0, 28650, 2000)

    ChrTalk(
        0x0101,
        (
            '#0010110072V#004F你、你们是……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3369')
    def lambda_3369():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_3369')

    DispatchAsync2(0x0101, 0x0001, lambda_3369)

    @scena.Lambda('lambda_337A')
    def lambda_337A():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_337A')

    DispatchAsync2(0x0102, 0x0001, lambda_337A)

    @scena.Lambda('lambda_338B')
    def lambda_338B():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_338B')

    DispatchAsync2(0x0108, 0x0001, lambda_338B)

    @scena.Lambda('lambda_339C')
    def lambda_339C():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_339C')

    DispatchAsync2(0x0104, 0x0001, lambda_339C)

    @scena.Lambda('lambda_33AD')
    def lambda_33AD():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_33AD')

    DispatchAsync2(0x000C, 0x0001, lambda_33AD)

    @scena.Lambda('lambda_33BE')
    def lambda_33BE():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_33BE')

    DispatchAsync2(0x000D, 0x0001, lambda_33BE)

    @scena.Lambda('lambda_33CF')
    def lambda_33CF():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_33CF')

    DispatchAsync2(0x000E, 0x0001, lambda_33CF)

    @scena.Lambda('lambda_33E0')
    def lambda_33E0():
        CameraMove(84900, 0, 32229, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_33E0)

    @scena.Lambda('lambda_33F8')
    def lambda_33F8():
        ChrWalkTo(0x00FE, 86080, 0, 31150, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_33F8)

    Sleep(200)

    @scena.Lambda('lambda_3418')
    def lambda_3418():
        ChrWalkTo(0x00FE, 87340, 0, 30470, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_3418)

    Sleep(200)

    @scena.Lambda('lambda_3438')
    def lambda_3438():
        ChrWalkTo(0x00FE, 86030, 0, 29770, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_3438)

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
    SetChrDirection(0x000C, 180, 400)

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
    SetChrDirection(0x000D, 180, 400)

    @scena.Lambda('lambda_3B78')
    def lambda_3B78():
        ChrWalkTo(0x00FE, 86030, 0, 23300, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_3B78)

    SetChrDirection(0x000E, 180, 400)

    @scena.Lambda('lambda_3B9A')
    def lambda_3B9A():
        ChrWalkTo(0x00FE, 87340, 0, 23300, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_3B9A)

    Sleep(300)

    @scena.Lambda('lambda_3BBA')
    def lambda_3BBA():
        ChrWalkTo(0x00FE, 86080, 0, 23300, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_3BBA)

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

# id: 0x0016 offset: 0x3DD5
@scena.Code('func_16_3DD5')
def func_16_3DD5():
    EventBegin(0x00)
    CameraMove(82890, 0, -58910, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 82240, 0, -59590, 90)
    SetChrPos(0x0102, 83290, 0, -60620, 0)
    SetChrPos(0x0108, 84060, 0, -58500, 180)
    SetChrPos(0x0104, 84330, 0, -59900, 270)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0017, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0014, 0x0080)
    SetChrPos(0x0008, 80230, 0, -59410, 180)
    SetChrPos(0x000A, 79030, 0, -59770, 90)
    SetChrPos(0x000B, 81100, 0, -61130, 315)
    SetChrPos(0x0009, 79590, 0, -60950, 0)
    SetChrPos(0x0016, 77000, 0, -64940, 135)
    SetChrPos(0x000F, 77450, 0, -66680, 352)
    SetChrPos(0x0010, 78200, 0, -66090, 315)
    SetChrPos(0x0011, 78970, 0, -65300, 247)
    SetChrPos(0x0017, 82830, 0, -65010, 270)
    SetChrPos(0x0013, 81290, 0, -65700, 90)
    SetChrPos(0x0012, 83000, 0, -66520, 16)
    SetChrPos(0x0014, 81230, 0, -64459, 98)
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
    ClearChrFlags(0x0024, 0x0080)
    ClearChrFlags(0x0025, 0x0080)
    ClearChrFlags(0x0026, 0x0080)
    SetChrPos(0x0024, 83160, 0, -59400, 180)
    SetChrPos(0x0026, 84060, 0, -58500, 180)
    SetChrPos(0x0025, 85350, 0, -58540, 180)
    CameraMove(84180, 0, -61020, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 84180, 0, -61020, 0)
    CreateThread(0x0024, 0x00, 0x00, 0x0002)
    CreateThread(0x0025, 0x00, 0x00, 0x0002)
    CreateThread(0x0026, 0x00, 0x00, 0x0002)
    CreateThread(0x0008, 0x00, 0x00, 0x0002)
    CreateThread(0x000A, 0x00, 0x00, 0x0002)
    CreateThread(0x0009, 0x00, 0x00, 0x0002)
    CreateThread(0x000B, 0x00, 0x00, 0x0002)
    CreateThread(0x000F, 0x00, 0x00, 0x0002)
    CreateThread(0x0010, 0x00, 0x00, 0x0002)
    CreateThread(0x0011, 0x00, 0x00, 0x0002)
    CreateThread(0x0012, 0x00, 0x00, 0x0002)
    CreateThread(0x0013, 0x00, 0x00, 0x0002)
    CreateThread(0x0014, 0x00, 0x00, 0x0002)
    CreateThread(0x0016, 0x00, 0x00, 0x0002)
    CreateThread(0x0017, 0x00, 0x00, 0x0002)
    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0017 offset: 0x416B
@scena.Code('func_17_416B')
def func_17_416B():
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
        'loc_423E',
    )

    FadeOut(1000, 0, -1)
    OP_0D()
    EventBegin(0x00)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('主持人的声音')

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
    SetMapFlags(0x00100000)
    PlaySE(175, 0x00, 0x64)
    PlaySE(191, 0x00, 0x64)
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T4104._SN', 100, 0, 0)
    IdleLoop()

    def _loc_423E(): pass

    label('loc_423E')

    Return()

# id: 0x0018 offset: 0x423F
@scena.Code('func_18_423F')
def func_18_423F():
    EventBegin(0x00)
    CameraMove(79600, 0, -59790, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 82240, 0, -59590, 90)
    SetChrPos(0x0102, 83290, 0, -60620, 0)
    SetChrPos(0x0108, 84060, 0, -58500, 180)
    SetChrPos(0x0104, 84330, 0, -59900, 270)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0017, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0014, 0x0080)
    SetChrPos(0x0008, 80230, 0, -59410, 180)
    SetChrPos(0x000A, 79030, 0, -59770, 90)
    SetChrPos(0x000B, 81100, 0, -61130, 315)
    SetChrPos(0x0009, 79590, 0, -60950, 0)
    SetChrPos(0x0016, 77000, 0, -64940, 135)
    SetChrPos(0x000F, 77450, 0, -66680, 352)
    SetChrPos(0x0010, 78200, 0, -66090, 315)
    SetChrPos(0x0011, 78970, 0, -65300, 247)
    SetChrPos(0x0017, 82830, 0, -65010, 270)
    SetChrPos(0x0013, 81290, 0, -65700, 90)
    SetChrPos(0x0012, 83000, 0, -66520, 16)
    SetChrPos(0x0014, 81230, 0, -64459, 98)

    @scena.Lambda('lambda_43D0')
    def lambda_43D0():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_43D0')

    DispatchAsync2(0x0016, 0x0001, lambda_43D0)

    @scena.Lambda('lambda_43E1')
    def lambda_43E1():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_43E1')

    DispatchAsync2(0x000F, 0x0001, lambda_43E1)

    @scena.Lambda('lambda_43F2')
    def lambda_43F2():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_43F2')

    DispatchAsync2(0x0010, 0x0001, lambda_43F2)

    @scena.Lambda('lambda_4403')
    def lambda_4403():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_4403')

    DispatchAsync2(0x0011, 0x0001, lambda_4403)

    @scena.Lambda('lambda_4414')
    def lambda_4414():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_4414')

    DispatchAsync2(0x0017, 0x0001, lambda_4414)

    @scena.Lambda('lambda_4425')
    def lambda_4425():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_4425')

    DispatchAsync2(0x0012, 0x0001, lambda_4425)

    @scena.Lambda('lambda_4436')
    def lambda_4436():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_4436')

    DispatchAsync2(0x0013, 0x0001, lambda_4436)

    @scena.Lambda('lambda_4447')
    def lambda_4447():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_4447')

    DispatchAsync2(0x0014, 0x0001, lambda_4447)

    @scena.Lambda('lambda_4458')
    def lambda_4458():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_4458')

    DispatchAsync2(0x0101, 0x0001, lambda_4458)

    @scena.Lambda('lambda_4469')
    def lambda_4469():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_4469')

    DispatchAsync2(0x0102, 0x0001, lambda_4469)

    @scena.Lambda('lambda_447A')
    def lambda_447A():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_447A')

    DispatchAsync2(0x0108, 0x0001, lambda_447A)

    @scena.Lambda('lambda_448B')
    def lambda_448B():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_448B')

    DispatchAsync2(0x0104, 0x0001, lambda_448B)

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

    @scena.Lambda('lambda_459A')
    def lambda_459A():
        ChrWalkTo(0x00FE, 73100, 0, -63210, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_459A)

    Sleep(200)

    @scena.Lambda('lambda_45BA')
    def lambda_45BA():
        ChrWalkTo(0x00FE, 73100, 0, -63210, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_45BA)

    @scena.Lambda('lambda_45D5')
    def lambda_45D5():
        ChrWalkTo(0x00FE, 73100, 0, -63210, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_45D5)

    Sleep(200)

    @scena.Lambda('lambda_45F5')
    def lambda_45F5():
        ChrWalkTo(0x00FE, 73100, 0, -63210, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_45F5)

    FadeOut(2000, 0, -1)
    Sleep(1000)

    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/T4104._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0019 offset: 0x4626
@scena.Code('func_19_4626')
def func_19_4626():
    EventBegin(0x00)
    CameraMove(77930, 0, -60800, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 78520, 0, -61710, 270)
    SetChrPos(0x0102, 79300, 0, -62840, 270)
    SetChrPos(0x0108, 79800, 0, -61660, 270)
    SetChrPos(0x0104, 79010, 0, -60670, 180)
    ClearChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0017, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0014, 0x0080)
    SetChrPos(0x0016, 77000, 0, -64940, 135)
    SetChrPos(0x000F, 77450, 0, -66680, 352)
    SetChrPos(0x0010, 78200, 0, -66090, 315)
    SetChrPos(0x0011, 78970, 0, -65300, 247)
    SetChrPos(0x0017, 82830, 0, -65010, 270)
    SetChrPos(0x0013, 81290, 0, -65700, 90)
    SetChrPos(0x0012, 83000, 0, -66520, 16)
    SetChrPos(0x0014, 81230, 0, -64459, 98)
    SetChrPos(0x0008, 72110, 0, -61480, 90)
    SetChrPos(0x000A, 72060, 0, -62470, 90)
    SetChrPos(0x000B, 71980, 0, -63590, 90)
    SetChrPos(0x0009, 72090, 0, -64519, 90)

    @scena.Lambda('lambda_47A3')
    def lambda_47A3():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_47A3')

    DispatchAsync2(0x0016, 0x0001, lambda_47A3)

    @scena.Lambda('lambda_47B4')
    def lambda_47B4():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_47B4')

    DispatchAsync2(0x000F, 0x0001, lambda_47B4)

    @scena.Lambda('lambda_47C5')
    def lambda_47C5():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_47C5')

    DispatchAsync2(0x0010, 0x0001, lambda_47C5)

    @scena.Lambda('lambda_47D6')
    def lambda_47D6():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_47D6')

    DispatchAsync2(0x0011, 0x0001, lambda_47D6)

    @scena.Lambda('lambda_47E7')
    def lambda_47E7():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_47E7')

    DispatchAsync2(0x0017, 0x0001, lambda_47E7)

    @scena.Lambda('lambda_47F8')
    def lambda_47F8():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_47F8')

    DispatchAsync2(0x0012, 0x0001, lambda_47F8)

    @scena.Lambda('lambda_4809')
    def lambda_4809():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_4809')

    DispatchAsync2(0x0013, 0x0001, lambda_4809)

    @scena.Lambda('lambda_481A')
    def lambda_481A():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_481A')

    DispatchAsync2(0x0014, 0x0001, lambda_481A)

    @scena.Lambda('lambda_482B')
    def lambda_482B():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_482B')

    DispatchAsync2(0x0101, 0x0001, lambda_482B)

    @scena.Lambda('lambda_483C')
    def lambda_483C():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_483C')

    DispatchAsync2(0x0102, 0x0001, lambda_483C)

    @scena.Lambda('lambda_484D')
    def lambda_484D():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_484D')

    DispatchAsync2(0x0108, 0x0001, lambda_484D)

    @scena.Lambda('lambda_485E')
    def lambda_485E():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_485E')

    DispatchAsync2(0x0104, 0x0001, lambda_485E)

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
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    SetChrFlags(0x0008, 0x0040)
    SetChrFlags(0x000A, 0x0040)
    SetChrFlags(0x000B, 0x0040)
    SetChrFlags(0x0009, 0x0040)

    @scena.Lambda('lambda_49BE')
    def lambda_49BE():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_49BE)

    @scena.Lambda('lambda_49D0')
    def lambda_49D0():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_49D0')

    DispatchAsync2(0x0008, 0x0002, lambda_49D0)

    @scena.Lambda('lambda_49E1')
    def lambda_49E1():
        ChrWalkTo(0x00FE, 77020, 0, -60760, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_49E1)

    Sleep(100)

    @scena.Lambda('lambda_4A01')
    def lambda_4A01():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_4A01)

    @scena.Lambda('lambda_4A13')
    def lambda_4A13():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_4A13')

    DispatchAsync2(0x000A, 0x0002, lambda_4A13)

    @scena.Lambda('lambda_4A24')
    def lambda_4A24():
        ChrWalkTo(0x00FE, 76490, 0, -61830, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_4A24)

    Sleep(100)

    @scena.Lambda('lambda_4A44')
    def lambda_4A44():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_4A44)

    @scena.Lambda('lambda_4A56')
    def lambda_4A56():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_4A56')

    DispatchAsync2(0x000B, 0x0002, lambda_4A56)

    @scena.Lambda('lambda_4A67')
    def lambda_4A67():
        ChrWalkTo(0x00FE, 77520, 0, -62340, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_4A67)

    Sleep(100)

    @scena.Lambda('lambda_4A87')
    def lambda_4A87():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_4A87)

    @scena.Lambda('lambda_4A99')
    def lambda_4A99():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_4A99')

    DispatchAsync2(0x0009, 0x0002, lambda_4A99)

    @scena.Lambda('lambda_4AAA')
    def lambda_4AAA():
        ChrWalkTo(0x00FE, 76260, 0, -59400, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_4AAA)

    WaitForThreadExit(0x0009, 0x0003)

    @scena.Lambda('lambda_4ACA')
    def lambda_4ACA():
        ChrWalkTo(0x00FE, 77690, 0, -59890, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_4ACA)

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
    SetChrName('主持人的声音')

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

    @scena.Lambda('lambda_4CB6')
    def lambda_4CB6():
        CameraMove(78520, 0, -60920, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4CB6)

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
    SetChrPos(0x0101, 77750, 0, -62490, 270)
    SetChrPos(0x0102, 77750, 0, -62490, 270)
    SetChrPos(0x0108, 77750, 0, -62490, 270)
    SetChrPos(0x0104, 77750, 0, -62490, 270)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000B, 0xFF)
    SetChrPos(0x0008, 76870, 0, -60150, 180)
    SetChrPos(0x000A, 79050, 0, -59930, 180)
    SetChrPos(0x0009, 77910, 0, -59730, 180)
    SetChrPos(0x000B, 75670, 0, -60330, 180)
    CreateThread(0x0008, 0x00, 0x00, 0x0002)
    CreateThread(0x000A, 0x00, 0x00, 0x0002)
    CreateThread(0x0009, 0x00, 0x00, 0x0002)
    CreateThread(0x000B, 0x00, 0x00, 0x0002)
    CreateThread(0x000F, 0x00, 0x00, 0x0002)
    CreateThread(0x0010, 0x00, 0x00, 0x0002)
    CreateThread(0x0011, 0x00, 0x00, 0x0002)
    CreateThread(0x0012, 0x00, 0x00, 0x0002)
    CreateThread(0x0013, 0x00, 0x00, 0x0002)
    CreateThread(0x0014, 0x00, 0x00, 0x0002)
    CreateThread(0x0016, 0x00, 0x00, 0x0002)
    CreateThread(0x0017, 0x00, 0x00, 0x0002)
    SetScenaFlags(ScenaFlag(0x00C3, 5, 0x61D))
    OP_1B(0x0B, 0x00, 0x0030)
    OP_1B(0x0C, 0x00, 0xFFFF)
    ClearChrFlags(0x0008, 0x0040)
    ClearChrFlags(0x000A, 0x0040)
    ClearChrFlags(0x000B, 0x0040)
    ClearChrFlags(0x0009, 0x0040)
    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x001A offset: 0x4F10
@scena.Code('func_1A_4F10')
def func_1A_4F10():
    EventBegin(0x00)
    CameraMove(81050, 0, -59630, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 81880, 0, -59420, 225)
    SetChrPos(0x0102, 82470, 0, -60720, 270)
    SetChrPos(0x0108, 82960, 0, -59440, 225)
    SetChrPos(0x0104, 82020, 0, -61450, 315)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0017, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0014, 0x0080)
    SetChrPos(0x0008, 80230, 0, -59410, 90)
    SetChrPos(0x000A, 79030, 0, -59770, 90)
    SetChrPos(0x000B, 80710, 0, -61590, 45)
    SetChrPos(0x0009, 79590, 0, -60950, 90)
    SetChrPos(0x0016, 77000, 0, -64940, 135)
    SetChrPos(0x000F, 77450, 0, -66680, 352)
    SetChrPos(0x0010, 78200, 0, -66090, 315)
    SetChrPos(0x0011, 78970, 0, -65300, 247)
    SetChrPos(0x0017, 82830, 0, -65010, 270)
    SetChrPos(0x0013, 81290, 0, -65700, 90)
    SetChrPos(0x0012, 83000, 0, -66520, 16)
    SetChrPos(0x0014, 81230, 0, -64459, 98)
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
    SetChrName('主持人的声音')

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

    @scena.Lambda('lambda_5318')
    def lambda_5318():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_5318')

    DispatchAsync2(0x0008, 0x0001, lambda_5318)

    @scena.Lambda('lambda_5329')
    def lambda_5329():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_5329')

    DispatchAsync2(0x000A, 0x0001, lambda_5329)

    @scena.Lambda('lambda_533A')
    def lambda_533A():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_533A')

    DispatchAsync2(0x000B, 0x0001, lambda_533A)

    @scena.Lambda('lambda_534B')
    def lambda_534B():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_534B')

    DispatchAsync2(0x0009, 0x0001, lambda_534B)

    @scena.Lambda('lambda_535C')
    def lambda_535C():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_535C')

    DispatchAsync2(0x0101, 0x0001, lambda_535C)

    @scena.Lambda('lambda_536D')
    def lambda_536D():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_536D')

    DispatchAsync2(0x0102, 0x0001, lambda_536D)

    @scena.Lambda('lambda_537E')
    def lambda_537E():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_537E')

    DispatchAsync2(0x0108, 0x0001, lambda_537E)

    @scena.Lambda('lambda_538F')
    def lambda_538F():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_538F')

    DispatchAsync2(0x0104, 0x0001, lambda_538F)

    @scena.Lambda('lambda_53A0')
    def lambda_53A0():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_53A0')

    DispatchAsync2(0x0017, 0x0001, lambda_53A0)

    @scena.Lambda('lambda_53B1')
    def lambda_53B1():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_53B1')

    DispatchAsync2(0x0012, 0x0001, lambda_53B1)

    @scena.Lambda('lambda_53C2')
    def lambda_53C2():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_53C2')

    DispatchAsync2(0x0013, 0x0001, lambda_53C2)

    @scena.Lambda('lambda_53D3')
    def lambda_53D3():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_53D3')

    DispatchAsync2(0x0014, 0x0001, lambda_53D3)

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
    CreateThread(0x0016, 0x01, 0x00, 0x001B)
    Sleep(300)

    CreateThread(0x000F, 0x01, 0x00, 0x001B)
    Sleep(300)

    CreateThread(0x0011, 0x01, 0x00, 0x001B)
    Sleep(600)

    CreateThread(0x0010, 0x01, 0x00, 0x001B)
    Sleep(1000)

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('主持人的声音')

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

# id: 0x001B offset: 0x55F5
@scena.Code('func_1B_55F5')
def func_1B_55F5():
    ChrWalkTo(0x00FE, 74370, 0, -62950, 3000, 0x00)

    @scena.Lambda('lambda_560F')
    def lambda_560F():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_560F)

    ChrWalkTo(0x00FE, 72250, 0, -62830, 3000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x001C offset: 0x5635
@scena.Code('func_1C_5635')
def func_1C_5635():
    EventBegin(0x00)
    CameraMove(81050, 0, -59630, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 81880, 0, -59420, 270)
    SetChrPos(0x0102, 82470, 0, -60720, 270)
    SetChrPos(0x0108, 82960, 0, -59440, 270)
    SetChrPos(0x0104, 82020, 0, -61450, 270)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x0017, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0014, 0x0080)
    SetChrPos(0x0008, 80230, 0, -59410, 270)
    SetChrPos(0x000A, 79030, 0, -59770, 270)
    SetChrPos(0x000B, 80710, 0, -61590, 270)
    SetChrPos(0x0009, 79590, 0, -60950, 270)
    SetChrPos(0x0017, 82830, 0, -65010, 270)
    SetChrPos(0x0013, 81290, 0, -65700, 270)
    SetChrPos(0x0012, 83000, 0, -66520, 270)
    SetChrPos(0x0014, 81230, 0, -64459, 270)
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

# id: 0x001D offset: 0x586C
@scena.Code('func_1D_586C')
def func_1D_586C():
    EventBegin(0x00)
    CameraMove(81050, 0, -59630, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 81880, 0, -59420, 270)
    SetChrPos(0x0102, 82470, 0, -60720, 270)
    SetChrPos(0x0108, 82960, 0, -59440, 270)
    SetChrPos(0x0104, 82020, 0, -61450, 270)
    SetChrPos(0x0008, 80230, 0, -59410, 270)
    SetChrPos(0x000A, 79030, 0, -59770, 270)
    SetChrPos(0x000B, 80710, 0, -61590, 270)
    SetChrPos(0x0009, 79590, 0, -60950, 270)
    SetChrPos(0x0016, 72110, 0, -61480, 90)
    SetChrPos(0x000F, 72060, 0, -62470, 90)
    SetChrPos(0x0010, 71980, 0, -63590, 90)
    SetChrPos(0x0011, 72090, 0, -64519, 90)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x0017, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0014, 0x0080)
    SetChrPos(0x0017, 82830, 0, -65010, 270)
    SetChrPos(0x0013, 81290, 0, -65700, 270)
    SetChrPos(0x0012, 83000, 0, -66520, 270)
    SetChrPos(0x0014, 81790, 0, -63840, 270)
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

    @scena.Lambda('lambda_5B5D')
    def lambda_5B5D():
        CameraMove(79710, 0, -62800, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_5B5D)

    ChrSetRGBAMask(0x0016, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x000F, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0010, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0011, 255, 255, 255, 0, 0)
    ClearChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x0011, 0x0080)

    @scena.Lambda('lambda_5BB5')
    def lambda_5BB5():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0016, 0x0001, lambda_5BB5)

    @scena.Lambda('lambda_5BC7')
    def lambda_5BC7():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_5BC7)

    @scena.Lambda('lambda_5BD9')
    def lambda_5BD9():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_5BD9)

    @scena.Lambda('lambda_5BEB')
    def lambda_5BEB():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_5BEB)

    @scena.Lambda('lambda_5BFD')
    def lambda_5BFD():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_5BFD')

    DispatchAsync2(0x0016, 0x0002, lambda_5BFD)

    @scena.Lambda('lambda_5C0E')
    def lambda_5C0E():
        ChrWalkTo(0x00FE, 78430, 0, -65650, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0016, 0x0003, lambda_5C0E)

    Sleep(300)

    @scena.Lambda('lambda_5C2E')
    def lambda_5C2E():
        ChrTurnDirection(0x00FE, 0x0016, 0)
        Yield()

        Jump('lambda_5C2E')

    DispatchAsync2(0x000F, 0x0002, lambda_5C2E)

    @scena.Lambda('lambda_5C3F')
    def lambda_5C3F():
        ChrWalkTo(0x00FE, 77210, 0, -65870, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0003, lambda_5C3F)

    Sleep(300)

    @scena.Lambda('lambda_5C5F')
    def lambda_5C5F():
        ChrTurnDirection(0x00FE, 0x0016, 0)
        Yield()

        Jump('lambda_5C5F')

    DispatchAsync2(0x0010, 0x0002, lambda_5C5F)

    @scena.Lambda('lambda_5C70')
    def lambda_5C70():
        ChrWalkTo(0x00FE, 77260, 0, -64709, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0003, lambda_5C70)

    Sleep(300)

    @scena.Lambda('lambda_5C90')
    def lambda_5C90():
        ChrTurnDirection(0x00FE, 0x0016, 0)
        Yield()

        Jump('lambda_5C90')

    DispatchAsync2(0x0011, 0x0002, lambda_5C90)

    SetChrFlags(0x0011, 0x0040)

    @scena.Lambda('lambda_5CA6')
    def lambda_5CA6():
        ChrWalkTo(0x00FE, 78250, 0, -64160, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_5CA6)

    @scena.Lambda('lambda_5CC1')
    def lambda_5CC1():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_5CC1')

    DispatchAsync2(0x0008, 0x0001, lambda_5CC1)

    @scena.Lambda('lambda_5CD2')
    def lambda_5CD2():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_5CD2')

    DispatchAsync2(0x000A, 0x0001, lambda_5CD2)

    @scena.Lambda('lambda_5CE3')
    def lambda_5CE3():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_5CE3')

    DispatchAsync2(0x000B, 0x0001, lambda_5CE3)

    @scena.Lambda('lambda_5CF4')
    def lambda_5CF4():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_5CF4')

    DispatchAsync2(0x0009, 0x0001, lambda_5CF4)

    @scena.Lambda('lambda_5D05')
    def lambda_5D05():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_5D05')

    DispatchAsync2(0x0101, 0x0001, lambda_5D05)

    @scena.Lambda('lambda_5D16')
    def lambda_5D16():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_5D16')

    DispatchAsync2(0x0102, 0x0001, lambda_5D16)

    @scena.Lambda('lambda_5D27')
    def lambda_5D27():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_5D27')

    DispatchAsync2(0x0108, 0x0001, lambda_5D27)

    @scena.Lambda('lambda_5D38')
    def lambda_5D38():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_5D38')

    DispatchAsync2(0x0104, 0x0001, lambda_5D38)

    @scena.Lambda('lambda_5D49')
    def lambda_5D49():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_5D49')

    DispatchAsync2(0x0017, 0x0001, lambda_5D49)

    @scena.Lambda('lambda_5D5A')
    def lambda_5D5A():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_5D5A')

    DispatchAsync2(0x0012, 0x0001, lambda_5D5A)

    @scena.Lambda('lambda_5D6B')
    def lambda_5D6B():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_5D6B')

    DispatchAsync2(0x0013, 0x0001, lambda_5D6B)

    @scena.Lambda('lambda_5D7C')
    def lambda_5D7C():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_5D7C')

    DispatchAsync2(0x0014, 0x0001, lambda_5D7C)

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

    @scena.Lambda('lambda_5E50')
    def lambda_5E50():
        ChrTurnDirection(0x00FE, 0x0017, 400)
        Yield()

        Jump('lambda_5E50')

    DispatchAsync2(0x000F, 0x0001, lambda_5E50)

    @scena.Lambda('lambda_5E61')
    def lambda_5E61():
        ChrTurnDirection(0x00FE, 0x0017, 400)
        Yield()

        Jump('lambda_5E61')

    DispatchAsync2(0x0010, 0x0001, lambda_5E61)

    @scena.Lambda('lambda_5E72')
    def lambda_5E72():
        ChrTurnDirection(0x00FE, 0x0017, 400)
        Yield()

        Jump('lambda_5E72')

    DispatchAsync2(0x0011, 0x0001, lambda_5E72)

    SetChrDirection(0x0016, 90, 400)

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
    SetChrName('主持人的声音')

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

    @scena.Lambda('lambda_5F7E')
    def lambda_5F7E():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_5F7E')

    DispatchAsync2(0x0008, 0x0001, lambda_5F7E)

    @scena.Lambda('lambda_5F8F')
    def lambda_5F8F():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_5F8F')

    DispatchAsync2(0x000A, 0x0001, lambda_5F8F)

    @scena.Lambda('lambda_5FA0')
    def lambda_5FA0():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_5FA0')

    DispatchAsync2(0x000B, 0x0001, lambda_5FA0)

    @scena.Lambda('lambda_5FB1')
    def lambda_5FB1():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_5FB1')

    DispatchAsync2(0x0009, 0x0001, lambda_5FB1)

    @scena.Lambda('lambda_5FC2')
    def lambda_5FC2():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_5FC2')

    DispatchAsync2(0x0101, 0x0001, lambda_5FC2)

    @scena.Lambda('lambda_5FD3')
    def lambda_5FD3():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_5FD3')

    DispatchAsync2(0x0102, 0x0001, lambda_5FD3)

    @scena.Lambda('lambda_5FE4')
    def lambda_5FE4():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_5FE4')

    DispatchAsync2(0x0108, 0x0001, lambda_5FE4)

    @scena.Lambda('lambda_5FF5')
    def lambda_5FF5():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_5FF5')

    DispatchAsync2(0x0104, 0x0001, lambda_5FF5)

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
    SetChrDirection(0x0017, 90, 400)

    ChrTalk(
        0x0017,
        (
            '#2260110295V#5P伙计们，上吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_60D3')
    def lambda_60D3():
        ChrTurnDirection(0x00FE, 0x0017, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_60D3)

    @scena.Lambda('lambda_60E1')
    def lambda_60E1():
        ChrTurnDirection(0x00FE, 0x0017, 400)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_60E1)

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

    @scena.Lambda('lambda_614A')
    def lambda_614A():
        ChrTurnDirection(0x00FE, 0x0017, 400)
        Yield()

        Jump('lambda_614A')

    DispatchAsync2(0x0016, 0x0001, lambda_614A)

    CreateThread(0x0017, 0x01, 0x00, 0x001E)
    Sleep(300)

    CreateThread(0x0014, 0x01, 0x00, 0x001E)
    Sleep(300)

    CreateThread(0x0013, 0x01, 0x00, 0x001E)
    CreateThread(0x0012, 0x01, 0x00, 0x001E)
    Sleep(1500)

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('主持人的声音')

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

# id: 0x001E offset: 0x6288
@scena.Code('func_1E_6288')
def func_1E_6288():
    ChrWalkTo(0x00FE, 79260, 0, -62720, 3000, 0x00)
    ChrWalkTo(0x00FE, 74370, 0, -62950, 3000, 0x00)

    @scena.Lambda('lambda_62B6')
    def lambda_62B6():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_62B6)

    ChrWalkTo(0x00FE, 72250, 0, -62830, 3000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x001F offset: 0x62DC
@scena.Code('func_1F_62DC')
def func_1F_62DC():
    EventBegin(0x00)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    CameraMove(76690, 0, -61440, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0102, 76260, 0, -60960, 270)
    SetChrPos(0x0108, 77340, 0, -60400, 270)
    SetChrPos(0x0101, 76310, 0, -62260, 270)
    SetChrPos(0x0104, 77550, 0, -61920, 270)
    SetChrPos(0x0008, 80230, 0, -59410, 270)
    SetChrPos(0x000A, 79030, 0, -59770, 270)
    SetChrPos(0x000B, 80710, 0, -61590, 270)
    SetChrPos(0x0009, 79590, 0, -60950, 270)
    SetChrPos(0x0016, 77000, 0, -64940, 270)
    SetChrPos(0x000F, 77630, 0, -66970, 270)
    SetChrPos(0x0010, 78610, 0, -66490, 270)
    SetChrPos(0x0011, 79150, 0, -65459, 270)
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

    @scena.Lambda('lambda_657E')
    def lambda_657E():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_657E)

    @scena.Lambda('lambda_658C')
    def lambda_658C():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_658C)

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
    SetChrName('主持人的声音')

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
    SetChrName('')
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
    ClearMapFlags(0x00100000)
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T4101._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0020 offset: 0x6853
@scena.Code('func_20_6853')
def func_20_6853():
    EventBegin(0x00)
    ClearChrFlags(0x001D, 0x0080)
    SetChrPos(0x001D, 320, 0, -470, 0)

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
    SetChrPos(0x0101, 9740, 0, 4610, 0)
    SetChrPos(0x0102, 10040, 0, 5710, 0)
    SetChrPos(0x0108, 10970, 0, 5750, 0)
    SetChrPos(0x0104, 10990, 0, 4550, 0)
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

    @scena.Lambda('lambda_699D')
    def lambda_699D():
        ChrWalkTo(0x00FE, 1410, 0, 2520, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_699D)

    Sleep(300)

    @scena.Lambda('lambda_69BD')
    def lambda_69BD():
        ChrWalkTo(0x00FE, 1360, 0, 3560, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_69BD)

    Sleep(300)

    @scena.Lambda('lambda_69DD')
    def lambda_69DD():
        ChrWalkTo(0x00FE, 2680, 0, 2640, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0002, lambda_69DD)

    Sleep(300)

    @scena.Lambda('lambda_69FD')
    def lambda_69FD():
        ChrWalkTo(0x00FE, 2630, 0, 3740, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_69FD)

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
    SetChrDirection(0x0101, 270, 600)

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
    SetChrDirection(0x001D, 270, 400)

    @scena.Lambda('lambda_72E4')
    def lambda_72E4():
        CameraMove(-2000, 0, 3110, 2000)

        ExitThread()

    DispatchAsync(0x001D, 0x0003, lambda_72E4)

    @scena.Lambda('lambda_72FC')
    def lambda_72FC():
        ChrWalkTo(0x00FE, -11300, 0, 5910, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001D, 0x0002, lambda_72FC)

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

    @scena.Lambda('lambda_7367')
    def lambda_7367():
        ChrTurnDirection(0x00FE, 0x0104, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_7367)

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
    SetChrFlags(0x001D, 0x0080)
    EventEnd(0x00)

    Return()

# id: 0x0021 offset: 0x7560
@scena.Code('func_21_7560')
def func_21_7560():
    EventBegin(0x00)
    ClearChrFlags(0x001D, 0x0080)
    SetChrPos(0x001D, -320, 0, -470, 0)

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
    SetChrPos(0x0101, -9740, 0, 4610, 90)
    SetChrPos(0x0102, -10040, 0, 5710, 90)
    SetChrPos(0x0108, -10970, 0, 5750, 90)
    SetChrPos(0x0104, -10990, 0, 4550, 90)
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

    @scena.Lambda('lambda_76AA')
    def lambda_76AA():
        ChrWalkTo(0x00FE, -1410, 0, 2520, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_76AA)

    Sleep(300)

    @scena.Lambda('lambda_76CA')
    def lambda_76CA():
        ChrWalkTo(0x00FE, -1360, 0, 3560, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_76CA)

    Sleep(300)

    @scena.Lambda('lambda_76EA')
    def lambda_76EA():
        ChrWalkTo(0x00FE, -2680, 0, 2640, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0002, lambda_76EA)

    Sleep(300)

    @scena.Lambda('lambda_770A')
    def lambda_770A():
        ChrWalkTo(0x00FE, -2630, 0, 3740, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_770A)

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
    SetChrDirection(0x0101, 90, 600)

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
    SetChrDirection(0x001D, 90, 400)

    @scena.Lambda('lambda_803C')
    def lambda_803C():
        CameraMove(2000, 0, 3110, 2000)

        ExitThread()

    DispatchAsync(0x001D, 0x0003, lambda_803C)

    @scena.Lambda('lambda_8054')
    def lambda_8054():
        ChrWalkTo(0x00FE, 11300, 0, 5910, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001D, 0x0002, lambda_8054)

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

    @scena.Lambda('lambda_80BF')
    def lambda_80BF():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_80BF)

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
    SetChrFlags(0x001D, 0x0080)
    EventEnd(0x00)

    Return()

# id: 0x0022 offset: 0x82B8
@scena.Code('func_22_82B8')
def func_22_82B8():
    SetScenaFlags(ScenaFlag(0x007E, 0, 0x3F0))
    NewScene('ED6_DT01/T4104._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0023 offset: 0x82C5
@scena.Code('func_23_82C5')
def func_23_82C5():
    EventBegin(0x00)
    CameraMove(74460, 0, -62460, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x000F, 87610, 0, -63640, 270)
    SetChrPos(0x0010, 87610, 0, -62310, 270)
    SetChrPos(0x001A, 87610, 0, -63200, 270)
    SetChrPos(0x001B, 87610, 0, -63200, 270)
    SetChrPos(0x001C, 87610, 0, -63200, 270)
    SetChrPos(0x0019, 87610, 0, -63200, 270)
    SetChrFlags(0x000F, 0x0004)
    SetChrFlags(0x0010, 0x0004)
    SetChrFlags(0x001A, 0x0004)
    SetChrFlags(0x001B, 0x0004)
    SetChrFlags(0x001C, 0x0004)
    SetChrFlags(0x0019, 0x0004)
    SetChrFlags(0x000F, 0x0040)
    SetChrFlags(0x0010, 0x0040)
    SetChrFlags(0x001A, 0x0040)
    SetChrFlags(0x001B, 0x0040)
    SetChrFlags(0x001C, 0x0040)
    SetChrFlags(0x0019, 0x0040)
    SetChrPos(0x0101, 81280, 0, -63460, 270)
    SetChrPos(0x0102, 81350, 0, -62190, 270)
    SetChrPos(0x0108, 80030, 0, -62140, 135)
    SetChrPos(0x0104, 79980, 0, -63500, 90)
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

    @scena.Lambda('lambda_84D9')
    def lambda_84D9():
        SetChrDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_84D9)

    @scena.Lambda('lambda_84E7')
    def lambda_84E7():
        SetChrDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_84E7)

    @scena.Lambda('lambda_84F5')
    def lambda_84F5():
        SetChrDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_84F5)

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
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x001A, 0x0080)
    ClearChrFlags(0x001B, 0x0080)
    ClearChrFlags(0x001C, 0x0080)
    ClearChrFlags(0x0019, 0x0080)

    @scena.Lambda('lambda_8653')
    def lambda_8653():
        CameraMove(81720, 0, -62380, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_8653)

    @scena.Lambda('lambda_866B')
    def lambda_866B():
        ChrWalkTo(0x00FE, 82650, 0, -61790, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_866B)

    @scena.Lambda('lambda_8686')
    def lambda_8686():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x001A, 0x0002, lambda_8686)

    Sleep(300)

    @scena.Lambda('lambda_869D')
    def lambda_869D():
        ChrWalkTo(0x00FE, 83100, 0, -62910, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_869D)

    @scena.Lambda('lambda_86B8')
    def lambda_86B8():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x001B, 0x0002, lambda_86B8)

    Sleep(300)

    @scena.Lambda('lambda_86CF')
    def lambda_86CF():
        ChrWalkTo(0x00FE, 82650, 0, -63910, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_86CF)

    @scena.Lambda('lambda_86EA')
    def lambda_86EA():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x001C, 0x0002, lambda_86EA)

    Sleep(300)

    @scena.Lambda('lambda_8701')
    def lambda_8701():
        ChrWalkTo(0x00FE, 83540, 0, -60870, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_8701)

    @scena.Lambda('lambda_871C')
    def lambda_871C():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0019, 0x0002, lambda_871C)

    Sleep(500)

    @scena.Lambda('lambda_8733')
    def lambda_8733():
        ChrWalkTo(0x00FE, 85520, 0, -63640, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_8733)

    @scena.Lambda('lambda_874E')
    def lambda_874E():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_874E)

    Sleep(300)

    @scena.Lambda('lambda_8765')
    def lambda_8765():
        ChrWalkTo(0x00FE, 85520, 0, -62310, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_8765)

    @scena.Lambda('lambda_8780')
    def lambda_8780():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_8780)

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

    @scena.Lambda('lambda_897C')
    def lambda_897C():
        SetChrDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_897C)

    @scena.Lambda('lambda_898A')
    def lambda_898A():
        SetChrDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_898A)

    @scena.Lambda('lambda_8998')
    def lambda_8998():
        SetChrDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_8998)

    SetChrDirection(0x001A, 90, 400)

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
    SetChrDirection(0x0010, 270, 400)

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
    SetChrDirection(0x000F, 90, 400)

    @scena.Lambda('lambda_8C6E')
    def lambda_8C6E():
        ChrWalkTo(0x00FE, 87610, 0, -63640, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_8C6E)

    @scena.Lambda('lambda_8C89')
    def lambda_8C89():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_8C89)

    SetChrDirection(0x0010, 90, 400)

    @scena.Lambda('lambda_8CA2')
    def lambda_8CA2():
        ChrWalkTo(0x00FE, 87610, 0, -62310, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_8CA2)

    @scena.Lambda('lambda_8CBD')
    def lambda_8CBD():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_8CBD)

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

    @scena.Lambda('lambda_8D43')
    def lambda_8D43():
        SetChrDirection(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_8D43)

    @scena.Lambda('lambda_8D51')
    def lambda_8D51():
        SetChrDirection(0x00FE, 315, 400)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_8D51)

    @scena.Lambda('lambda_8D5F')
    def lambda_8D5F():
        SetChrDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_8D5F)

    @scena.Lambda('lambda_8D6D')
    def lambda_8D6D():
        SetChrDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_8D6D)

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

    @scena.Lambda('lambda_94B9')
    def lambda_94B9():
        SetChrDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_94B9)

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

    @scena.Lambda('lambda_9528')
    def lambda_9528():
        SetChrDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_9528)

    @scena.Lambda('lambda_9536')
    def lambda_9536():
        SetChrDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_9536)

    @scena.Lambda('lambda_9544')
    def lambda_9544():
        SetChrDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_9544)

    Sleep(1000)

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('主持人的声音')

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
    SetChrName('主持人的声音')

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

    @scena.Lambda('lambda_97B6')
    def lambda_97B6():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_97B6)

    @scena.Lambda('lambda_97C4')
    def lambda_97C4():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_97C4)

    @scena.Lambda('lambda_97D2')
    def lambda_97D2():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_97D2)

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
    ClearChrFlags(0x001A, 0x0004)
    ClearChrFlags(0x001B, 0x0004)
    ClearChrFlags(0x001C, 0x0004)
    ClearChrFlags(0x0019, 0x0004)
    ClearChrFlags(0x001A, 0x0040)
    ClearChrFlags(0x001B, 0x0040)
    ClearChrFlags(0x001C, 0x0040)
    ClearChrFlags(0x0019, 0x0040)
    SetChrDirection(0x001A, 270, 0)
    SetChrDirection(0x001C, 270, 0)
    CreateThread(0x001A, 0x00, 0x00, 0x0002)
    CreateThread(0x001B, 0x00, 0x00, 0x0002)
    CreateThread(0x001C, 0x00, 0x00, 0x0002)
    CreateThread(0x0019, 0x00, 0x00, 0x0002)
    CameraMove(80480, 0, -62830, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 80480, 0, -62830, 270)
    SetChrPos(0x0102, 80480, 0, -62830, 270)
    SetChrPos(0x0108, 80480, 0, -62830, 270)
    SetChrPos(0x0104, 80480, 0, -62830, 270)
    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0024 offset: 0x9931
@scena.Code('func_24_9931')
def func_24_9931():
    ChrWalkTo(0x00FE, 85520, 0, -63140, 3000, 0x00)

    @scena.Lambda('lambda_994B')
    def lambda_994B():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_994B)

    ChrWalkTo(0x00FE, 87690, 0, -63010, 3000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0025 offset: 0x9971
@scena.Code('func_25_9971')
def func_25_9971():
    EventBegin(0x00)
    CameraMove(80720, 0, -62380, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 81280, 0, -63460, 90)
    SetChrPos(0x0102, 81350, 0, -62190, 90)
    SetChrPos(0x0108, 80030, 0, -62140, 90)
    SetChrPos(0x0104, 79980, 0, -63500, 90)
    SetChrPos(0x001A, 82650, 0, -61790, 270)
    SetChrPos(0x001B, 83100, 0, -62910, 270)
    SetChrPos(0x001C, 82650, 0, -63910, 270)
    SetChrPos(0x0019, 84010, 0, -62350, 270)
    ClearChrFlags(0x001A, 0x0080)
    ClearChrFlags(0x001B, 0x0080)
    ClearChrFlags(0x001C, 0x0080)
    ClearChrFlags(0x0019, 0x0080)
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
    SetChrName('主持人的声音')

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

    @scena.Lambda('lambda_9E2A')
    def lambda_9E2A():
        ChrTurnDirection(0x00FE, 0x001A, 400)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_9E2A)

    @scena.Lambda('lambda_9E38')
    def lambda_9E38():
        ChrTurnDirection(0x00FE, 0x001A, 400)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_9E38)

    @scena.Lambda('lambda_9E46')
    def lambda_9E46():
        ChrTurnDirection(0x00FE, 0x001A, 400)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_9E46)

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

    @scena.Lambda('lambda_9EE5')
    def lambda_9EE5():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_9EE5)

    @scena.Lambda('lambda_9EF3')
    def lambda_9EF3():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_9EF3)

    @scena.Lambda('lambda_9F01')
    def lambda_9F01():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_9F01)

    @scena.Lambda('lambda_9F0F')
    def lambda_9F0F():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_9F0F)

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

# id: 0x0026 offset: 0x9FD1
@scena.Code('func_26_9FD1')
def func_26_9FD1():
    EventBegin(0x00)
    CameraMove(75020, 0, -60990, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 75990, 0, -61820, 270)
    SetChrPos(0x0102, 75110, 0, -61050, 270)
    SetChrPos(0x0108, 75980, 0, -60520, 270)
    SetChrPos(0x0104, 77190, 0, -60900, 270)
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
    SetChrFlags(0x001A, 0x0040)
    SetChrFlags(0x001B, 0x0040)
    SetChrFlags(0x001C, 0x0040)
    SetChrFlags(0x0019, 0x0040)
    ChrSetRGBAMask(0x001A, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x001B, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x001C, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0019, 255, 255, 255, 0, 0)
    SetChrPos(0x001A, 72050, 0, -63520, 90)
    SetChrPos(0x001B, 72050, 0, -63520, 90)
    SetChrPos(0x001C, 72050, 0, -63520, 90)
    SetChrPos(0x0019, 72050, 0, -63520, 90)

    @scena.Lambda('lambda_A2BA')
    def lambda_A2BA():
        ChrTurnDirection(0x00FE, 0x001C, 400)
        Yield()

        Jump('lambda_A2BA')

    DispatchAsync2(0x0101, 0x0002, lambda_A2BA)

    @scena.Lambda('lambda_A2CB')
    def lambda_A2CB():
        ChrTurnDirection(0x00FE, 0x001C, 400)
        Yield()

        Jump('lambda_A2CB')

    DispatchAsync2(0x0102, 0x0002, lambda_A2CB)

    @scena.Lambda('lambda_A2DC')
    def lambda_A2DC():
        ChrTurnDirection(0x00FE, 0x001C, 400)
        Yield()

        Jump('lambda_A2DC')

    DispatchAsync2(0x0108, 0x0002, lambda_A2DC)

    @scena.Lambda('lambda_A2ED')
    def lambda_A2ED():
        ChrTurnDirection(0x00FE, 0x001C, 400)
        Yield()

        Jump('lambda_A2ED')

    DispatchAsync2(0x0104, 0x0002, lambda_A2ED)

    ClearChrFlags(0x001A, 0x0080)
    ClearChrFlags(0x001B, 0x0080)
    ClearChrFlags(0x001C, 0x0080)
    ClearChrFlags(0x0019, 0x0080)

    @scena.Lambda('lambda_A312')
    def lambda_A312():
        CameraMove(75100, 0, -62310, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_A312)

    @scena.Lambda('lambda_A32A')
    def lambda_A32A():
        CameraSetDistance(3000, 3000)

        ExitThread()

    DispatchAsync(0x001C, 0x0002, lambda_A32A)

    @scena.Lambda('lambda_A33A')
    def lambda_A33A():
        ChrWalkTo(0x00FE, 77330, 0, -65099, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0003, lambda_A33A)

    @scena.Lambda('lambda_A355')
    def lambda_A355():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_A355)

    Sleep(500)

    @scena.Lambda('lambda_A36C')
    def lambda_A36C():
        ChrWalkTo(0x00FE, 76630, 0, -63990, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001C, 0x0003, lambda_A36C)

    @scena.Lambda('lambda_A387')
    def lambda_A387():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_A387)

    Sleep(400)

    @scena.Lambda('lambda_A39E')
    def lambda_A39E():
        ChrWalkTo(0x00FE, 75560, 0, -64250, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0003, lambda_A39E)

    @scena.Lambda('lambda_A3B9')
    def lambda_A3B9():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_A3B9)

    Sleep(800)

    @scena.Lambda('lambda_A3D0')
    def lambda_A3D0():
        ChrWalkTo(0x00FE, 76260, 0, -65370, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0003, lambda_A3D0)

    @scena.Lambda('lambda_A3EB')
    def lambda_A3EB():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_A3EB)

    @scena.Lambda('lambda_A3FD')
    def lambda_A3FD():
        SetChrDirection(0x00FE, 90, 0)
        Yield()

        Jump('lambda_A3FD')

    DispatchAsync2(0x0019, 0x0002, lambda_A3FD)

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

    @scena.Lambda('lambda_A658')
    def lambda_A658():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x001A, 0x0002, lambda_A658)

    @scena.Lambda('lambda_A666')
    def lambda_A666():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x001B, 0x0002, lambda_A666)

    @scena.Lambda('lambda_A674')
    def lambda_A674():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x001C, 0x0002, lambda_A674)

    @scena.Lambda('lambda_A682')
    def lambda_A682():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0019, 0x0002, lambda_A682)

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
    SetChrPos(0x000F, 84120, 0, -64660, 270)
    SetChrPos(0x0010, 84380, 0, -65750, 270)
    SetChrPos(0x0011, 85120, 0, -64170, 270)
    SetChrPos(0x0012, 85370, 0, -65269, 270)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0012, 0x0080)

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

    @scena.Lambda('lambda_A82E')
    def lambda_A82E():
        ChrTurnDirection(0x00FE, 0x0012, 400)
        Yield()

        Jump('lambda_A82E')

    DispatchAsync2(0x001A, 0x0002, lambda_A82E)

    @scena.Lambda('lambda_A83F')
    def lambda_A83F():
        ChrTurnDirection(0x00FE, 0x000F, 400)
        Yield()

        Jump('lambda_A83F')

    DispatchAsync2(0x001B, 0x0002, lambda_A83F)

    @scena.Lambda('lambda_A850')
    def lambda_A850():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_A850')

    DispatchAsync2(0x001C, 0x0002, lambda_A850)

    @scena.Lambda('lambda_A861')
    def lambda_A861():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_A861')

    DispatchAsync2(0x0019, 0x0002, lambda_A861)

    @scena.Lambda('lambda_A872')
    def lambda_A872():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_A872')

    DispatchAsync2(0x0101, 0x0002, lambda_A872)

    @scena.Lambda('lambda_A883')
    def lambda_A883():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_A883')

    DispatchAsync2(0x0102, 0x0002, lambda_A883)

    @scena.Lambda('lambda_A894')
    def lambda_A894():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_A894')

    DispatchAsync2(0x0108, 0x0002, lambda_A894)

    @scena.Lambda('lambda_A8A5')
    def lambda_A8A5():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_A8A5')

    DispatchAsync2(0x0104, 0x0002, lambda_A8A5)

    CameraMove(79330, 0, -63550, 1000)

    @scena.Lambda('lambda_A8C7')
    def lambda_A8C7():
        ChrTurnDirection(0x00FE, 0x001B, 0)
        Yield()

        Jump('lambda_A8C7')

    DispatchAsync2(0x000F, 0x0001, lambda_A8C7)

    @scena.Lambda('lambda_A8D8')
    def lambda_A8D8():
        ChrTurnDirection(0x00FE, 0x001A, 0)
        Yield()

        Jump('lambda_A8D8')

    DispatchAsync2(0x0010, 0x0001, lambda_A8D8)

    @scena.Lambda('lambda_A8E9')
    def lambda_A8E9():
        ChrTurnDirection(0x00FE, 0x001A, 0)
        Yield()

        Jump('lambda_A8E9')

    DispatchAsync2(0x0011, 0x0001, lambda_A8E9)

    @scena.Lambda('lambda_A8FA')
    def lambda_A8FA():
        ChrTurnDirection(0x00FE, 0x001A, 0)
        Yield()

        Jump('lambda_A8FA')

    DispatchAsync2(0x0012, 0x0001, lambda_A8FA)

    @scena.Lambda('lambda_A90B')
    def lambda_A90B():
        ChrWalkTo(0x00FE, 76360, 0, -62810, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_A90B)

    Sleep(300)

    @scena.Lambda('lambda_A92B')
    def lambda_A92B():
        ChrWalkTo(0x00FE, 76760, 0, -66540, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_A92B)

    @scena.Lambda('lambda_A946')
    def lambda_A946():
        CameraMove(75030, 0, -62490, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_A946)

    Sleep(300)

    @scena.Lambda('lambda_A963')
    def lambda_A963():
        ChrWalkTo(0x00FE, 77690, 0, -63760, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_A963)

    Sleep(100)

    @scena.Lambda('lambda_A983')
    def lambda_A983():
        ChrWalkTo(0x00FE, 78150, 0, -65780, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_A983)

    WaitForThreadExit(0x000F, 0x0002)

    @scena.Lambda('lambda_A9A3')
    def lambda_A9A3():
        ChrWalkTo(0x00FE, 74780, 0, -63460, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_A9A3)

    WaitForThreadExit(0x0010, 0x0002)

    @scena.Lambda('lambda_A9C3')
    def lambda_A9C3():
        ChrWalkTo(0x00FE, 74960, 0, -65250, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_A9C3)

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

    @scena.Lambda('lambda_AB4B')
    def lambda_AB4B():
        ChrMoveToRelative(0x00FE, 7000, 0, 1760, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_AB4B)

    @scena.Lambda('lambda_AB66')
    def lambda_AB66():
        ChrMoveToRelative(0x00FE, 7000, 0, 1760, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_AB66)

    @scena.Lambda('lambda_AB81')
    def lambda_AB81():
        CameraMove(78790, 0, -61860, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_AB81)

    Sleep(300)

    @scena.Lambda('lambda_AB9E')
    def lambda_AB9E():
        ChrMoveToRelative(0x00FE, 7000, 0, 1760, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_AB9E)

    @scena.Lambda('lambda_ABB9')
    def lambda_ABB9():
        ChrMoveToRelative(0x00FE, 6380, 0, 1760, 2200, 0x00)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_ABB9)

    Sleep(200)

    @scena.Lambda('lambda_ABD9')
    def lambda_ABD9():
        ChrMoveToRelative(0x00FE, 6000, 0, 1760, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_ABD9)

    @scena.Lambda('lambda_ABF4')
    def lambda_ABF4():
        ChrMoveToRelative(0x00FE, 6000, 0, 1760, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_ABF4)

    Sleep(200)

    @scena.Lambda('lambda_AC14')
    def lambda_AC14():
        ChrMoveToRelative(0x00FE, 6000, 0, 1760, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_AC14)

    @scena.Lambda('lambda_AC2F')
    def lambda_AC2F():
        ChrMoveToRelative(0x00FE, 6000, 0, 1760, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_AC2F)

    WaitForThreadExit(0x001C, 0x0001)
    Sleep(600)

    ChrTalk(
        0x001C,
        (
            '#0090110913V#212F#1P喂，你们……',
            TxtCtl.Enter,
        ),
    )

    @scena.Lambda('lambda_AC74')
    def lambda_AC74():
        ChrTurnDirection(0x00FE, 0x001C, 400)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_AC74)

    @scena.Lambda('lambda_AC82')
    def lambda_AC82():
        ChrTurnDirection(0x00FE, 0x001C, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_AC82)

    @scena.Lambda('lambda_AC90')
    def lambda_AC90():
        ChrTurnDirection(0x00FE, 0x001C, 400)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_AC90)

    @scena.Lambda('lambda_AC9E')
    def lambda_AC9E():
        ChrTurnDirection(0x00FE, 0x001C, 400)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_AC9E)

    @scena.Lambda('lambda_ACAC')
    def lambda_ACAC():
        ChrTurnDirection(0x00FE, 0x001C, 400)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_ACAC)

    @scena.Lambda('lambda_ACBA')
    def lambda_ACBA():
        ChrTurnDirection(0x00FE, 0x001C, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_ACBA)

    @scena.Lambda('lambda_ACC8')
    def lambda_ACC8():
        ChrTurnDirection(0x00FE, 0x001C, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_ACC8)

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

    @scena.Lambda('lambda_AE52')
    def lambda_AE52():
        ChrMoveToRelative(0x00FE, 7000, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_AE52)

    @scena.Lambda('lambda_AE6D')
    def lambda_AE6D():
        ChrMoveToRelative(0x00FE, 7000, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_AE6D)

    Sleep(300)

    @scena.Lambda('lambda_AE8D')
    def lambda_AE8D():
        ChrMoveToRelative(0x00FE, 7000, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_AE8D)

    @scena.Lambda('lambda_AEA8')
    def lambda_AEA8():
        ChrMoveToRelative(0x00FE, 6380, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_AEA8)

    Sleep(300)

    @scena.Lambda('lambda_AEC8')
    def lambda_AEC8():
        ChrMoveToRelative(0x00FE, 6380, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_AEC8)

    @scena.Lambda('lambda_AEE3')
    def lambda_AEE3():
        ChrMoveToRelative(0x00FE, 6380, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_AEE3)

    Sleep(300)

    @scena.Lambda('lambda_AF03')
    def lambda_AF03():
        ChrMoveToRelative(0x00FE, 6380, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_AF03)

    @scena.Lambda('lambda_AF1E')
    def lambda_AF1E():
        ChrMoveToRelative(0x00FE, 6380, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_AF1E)

    OP_0D()
    Sleep(500)

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
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
    ClearMapFlags(0x00100000)
    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/T4101._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0027 offset: 0xAF90
@scena.Code('func_27_AF90')
def func_27_AF90():
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
    SetChrFlags(0x0025, 0x0080)
    SetChrFlags(0x0026, 0x0080)
    SetChrPos(0x0101, 81740, 0, -63700, 270)
    SetChrPos(0x0102, 82090, 0, -62760, 270)
    SetChrPos(0x0104, 80420, 0, -63500, 270)
    SetChrPos(0x0108, 80850, 0, -62320, 270)
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
    SetChrDirection(0x0108, 135, 400)

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

    @scena.Lambda('lambda_B27A')
    def lambda_B27A():
        SetChrDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_B27A)

    @scena.Lambda('lambda_B288')
    def lambda_B288():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_B288)

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

    @scena.Lambda('lambda_B367')
    def lambda_B367():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_B367)

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

    @scena.Lambda('lambda_B3E3')
    def lambda_B3E3():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_B3E3')

    DispatchAsync2(0x0104, 0x0001, lambda_B3E3)

    @scena.Lambda('lambda_B3F4')
    def lambda_B3F4():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_B3F4')

    DispatchAsync2(0x0108, 0x0001, lambda_B3F4)

    @scena.Lambda('lambda_B405')
    def lambda_B405():
        CameraMove(81340, 0, -62730, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_B405)

    @scena.Lambda('lambda_B41D')
    def lambda_B41D():
        OP_6E(314, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_B41D)

    SetChrDirection(0x0101, 90, 400)

    @scena.Lambda('lambda_B434')
    def lambda_B434():
        ChrWalkTo(0x00FE, 85380, 0, -63500, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_B434)

    Sleep(400)

    SetChrDirection(0x0102, 90, 400)

    @scena.Lambda('lambda_B45B')
    def lambda_B45B():
        ChrWalkTo(0x00FE, 85500, 0, -62300, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_B45B)

    WaitForThreadExit(0x0101, 0x0001)
    PlaySE(6, 0x00, 0x64)
    Sleep(50)

    @scena.Lambda('lambda_B485')
    def lambda_B485():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_B485)

    @scena.Lambda('lambda_B497')
    def lambda_B497():
        ChrWalkTo(0x00FE, 87410, 0, -63500, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_B497)

    WaitForThreadExit(0x0102, 0x0001)

    @scena.Lambda('lambda_B4B7')
    def lambda_B4B7():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_B4B7)

    @scena.Lambda('lambda_B4C9')
    def lambda_B4C9():
        ChrWalkTo(0x00FE, 87510, 0, -62300, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_B4C9)

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

    @scena.Lambda('lambda_B51B')
    def lambda_B51B():
        CameraMove(80340, 0, -62730, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_B51B)

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
    SetChrPos(0x0101, 85160, 0, 32390, 90)
    SetChrPos(0x0102, 85170, 0, 33380, 90)
    ClearChrFlags(0x0025, 0x0080)
    ClearChrFlags(0x0026, 0x0080)
    SetChrPos(0x0025, 80420, 0, -63670, 0)
    SetChrPos(0x0026, 80420, 0, -62320, 180)
    CreateThread(0x0025, 0x00, 0x00, 0x0002)
    CreateThread(0x0026, 0x00, 0x00, 0x0002)
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

# id: 0x0028 offset: 0xB9C4
@scena.Code('func_28_B9C4')
def func_28_B9C4():
    EventBegin(0x00)
    ClearChrFlags(0x001E, 0x0080)

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x66),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BA1E',
    )

    SetChrPos(0x0101, 11050, 0, 5180, 270)
    SetChrPos(0x0102, 11120, 0, 6310, 270)
    SetChrPos(0x001E, 1660, 0, 3830, 90)
    CameraMove(10420, 0, 6050, 0)

    Jump('loc_BA62')

    def _loc_BA1E(): pass

    label('loc_BA1E')

    SetChrPos(0x0101, -11040, 0, 5190, 90)
    SetChrPos(0x0102, -10950, 0, 6290, 90)
    SetChrPos(0x001E, -2060, 0, 5520, 270)
    CameraMove(-10910, 0, 5550, 0)

    def _loc_BA62(): pass

    label('loc_BA62')

    FadeIn(1000, 0)
    OP_0D()

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x66),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C32B',
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

    @scena.Lambda('lambda_BB71')
    def lambda_BB71():
        ChrTurnDirection(0x00FE, 0x001E, 0)
        Yield()

        Jump('lambda_BB71')

    DispatchAsync2(0x0101, 0x0001, lambda_BB71)

    @scena.Lambda('lambda_BB82')
    def lambda_BB82():
        ChrTurnDirection(0x00FE, 0x001E, 0)
        Yield()

        Jump('lambda_BB82')

    DispatchAsync2(0x0102, 0x0001, lambda_BB82)

    @scena.Lambda('lambda_BB93')
    def lambda_BB93():
        ChrWalkTo(0x00FE, 6040, 0, 4750, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0002, lambda_BB93)

    Sleep(300)

    @scena.Lambda('lambda_BBB3')
    def lambda_BBB3():
        ChrWalkTo(0x00FE, 7570, 0, 4470, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_BBB3)

    Sleep(300)

    @scena.Lambda('lambda_BBD3')
    def lambda_BBD3():
        ChrWalkTo(0x00FE, 7160, 0, 5630, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_BBD3)

    WaitForThreadExit(0x001E, 0x0002)
    SetChrDirection(0x001E, 90, 400)

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
    SetChrName('')

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

    @scena.Lambda('lambda_C303')
    def lambda_C303():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_C303)

    ChrWalkTo(0x001E, 13690, 0, 5800, 3000, 0x00)
    PlaySE(7, 0x00, 0x64)

    Jump('loc_CBF1')

    def _loc_C32B(): pass

    label('loc_C32B')

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

    @scena.Lambda('lambda_C424')
    def lambda_C424():
        ChrTurnDirection(0x00FE, 0x001E, 0)
        Yield()

        Jump('lambda_C424')

    DispatchAsync2(0x0101, 0x0001, lambda_C424)

    @scena.Lambda('lambda_C435')
    def lambda_C435():
        ChrTurnDirection(0x00FE, 0x001E, 0)
        Yield()

        Jump('lambda_C435')

    DispatchAsync2(0x0102, 0x0001, lambda_C435)

    @scena.Lambda('lambda_C446')
    def lambda_C446():
        ChrWalkTo(0x00FE, -5900, 0, 5760, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0002, lambda_C446)

    Sleep(300)

    @scena.Lambda('lambda_C466')
    def lambda_C466():
        ChrWalkTo(0x00FE, -7600, 0, 5320, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_C466)

    Sleep(300)

    @scena.Lambda('lambda_C486')
    def lambda_C486():
        ChrWalkTo(0x00FE, -7530, 0, 6580, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_C486)

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
    SetChrName('')

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
    SetChrDirection(0x001E, 270, 400)
    OP_70(0x0001, 30)
    OP_73(0x0001)

    @scena.Lambda('lambda_CBC0')
    def lambda_CBC0():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_CBC0)

    ChrWalkTo(0x001E, -13110, 0, 6020, 3000, 0x00)
    OP_72(0x0001, 0x0800)
    PlaySE(7, 0x00, 0x64)
    OP_70(0x0001, 0)

    def _loc_CBF1(): pass

    label('loc_CBF1')

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

# id: 0x0029 offset: 0xCDBA
@scena.Code('func_29_CDBA')
def func_29_CDBA():
    SetScenaFlags(ScenaFlag(0x007E, 2, 0x3F2))
    NewScene('ED6_DT01/T4104._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x002A offset: 0xCDC7
@scena.Code('func_2A_CDC7')
def func_2A_CDC7():
    EventBegin(0x00)
    CameraMove(75070, 0, -63440, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FormationAddMember(0x03, 0xFF)
    FormationAddMember(0x07, 0xFF)
    SetChrPos(0x0101, 75600, 0, -63280, 270)
    SetChrPos(0x0102, 76550, 0, -62310, 270)
    SetChrPos(0x0104, 76600, 0, -64489, 270)
    SetChrPos(0x0108, 77680, 0, -63300, 270)
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
    SetChrDirection(0x0101, 270, 400)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('主持人的声音')

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

# id: 0x002B offset: 0xD120
@scena.Code('func_2B_D120')
def func_2B_D120():
    EventBegin(0x00)
    CameraMove(76480, 0, -63310, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 75600, 0, -63280, 90)
    SetChrPos(0x0102, 76550, 0, -62310, 180)
    SetChrPos(0x0104, 76600, 0, -64489, 0)
    SetChrPos(0x0108, 77680, 0, -63300, 270)
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

# id: 0x002C offset: 0xD279
@scena.Code('func_2C_D279')
def func_2C_D279():
    EventBegin(0x00)
    OP_24(0x00AE, 0x50)
    CameraMove(-80090, 0, -63100, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x001F, 0x0080)
    ClearChrFlags(0x0020, 0x0080)
    ClearChrFlags(0x0021, 0x0080)
    SetChrPos(0x001F, -82950, 0, -63110, 90)
    SetChrPos(0x0020, -82500, 0, -64220, 90)
    SetChrPos(0x0021, -82420, 0, -61920, 180)
    ClearMapFlags(0x00100000)
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

    @scena.Lambda('lambda_DA2D')
    def lambda_DA2D():
        CameraMove(-80600, 0, -63080, 1500)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_DA2D)

    @scena.Lambda('lambda_DA45')
    def lambda_DA45():
        ChrWalkTo(0x00FE, -80700, 0, -63110, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0002, lambda_DA45)

    Sleep(400)

    @scena.Lambda('lambda_DA65')
    def lambda_DA65():
        ChrTurnDirection(0x00FE, 0x001F, 400)
        Yield()

        Jump('lambda_DA65')

    DispatchAsync2(0x0021, 0x0001, lambda_DA65)

    @scena.Lambda('lambda_DA76')
    def lambda_DA76():
        SetChrDirection(0x00FE, 90, 200)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_DA76)

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

# id: 0x002D offset: 0xDB4C
@scena.Code('func_2D_DB4C')
def func_2D_DB4C():
    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_DBFE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DBCA',
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

    Jump('loc_DBFB')

    def _loc_DBCA(): pass

    label('loc_DBCA')

    ChrTalk(
        0x0101,
        (
            '#0010111500V#002F好像一旦出去\n',
            '就不能再进来了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DBFB(): pass

    label('loc_DBFB')

    Jump('loc_DCD0')

    def _loc_DBFE(): pass

    label('loc_DBFE')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_DC46',
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

    Jump('loc_DCD0')

    def _loc_DC46(): pass

    label('loc_DC46')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_DCAC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DC82',
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

    Jump('loc_DCA9')

    def _loc_DC82(): pass

    label('loc_DC82')

    ChrTalk(
        0x0108,
        (
            '#0080111504V#070F唔，\n',
            '现在还不能回去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DCA9(): pass

    label('loc_DCA9')

    Jump('loc_DCD0')

    def _loc_DCAC(): pass

    label('loc_DCAC')

    ChrTalk(
        0x0104,
        (
            '#0040111505V#030F唔，这边是出口呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DCD0(): pass

    label('loc_DCD0')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x002E offset: 0xDCEC
@scena.Code('func_2E_DCEC')
def func_2E_DCEC():
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

# id: 0x002F offset: 0xDD42
@scena.Code('func_2F_DD42')
def func_2F_DD42():
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

# id: 0x0030 offset: 0xDD92
@scena.Code('func_30_DD92')
def func_30_DD92():
    EventBegin(0x02)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 5, 0x61D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DDC7',
    )

    ChrTalk(
        0x0101,
        (
            '#0010111506V#501F啊，往这边去是走廊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DF71')

    def _loc_DDC7(): pass

    label('loc_DDC7')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_DE49',
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

    Jump('loc_DF71')

    def _loc_DE49(): pass

    label('loc_DE49')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_DEAF',
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

    Jump('loc_DF71')

    def _loc_DEAF(): pass

    label('loc_DEAF')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_DEE0',
    )

    ChrTalk(
        0x0108,
        (
            '#0080111512V#070F哦，这边是走廊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DF71')

    def _loc_DEE0(): pass

    label('loc_DEE0')

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

    def _loc_DF71(): pass

    label('loc_DF71')

    ChrMoveToRelative(0x0000, -1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0031 offset: 0xDF8D
@scena.Code('func_31_DF8D')
def func_31_DF8D():
    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 5, 0x61D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DFFB',
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

    Jump('loc_E0C7')

    def _loc_DFFB(): pass

    label('loc_DFFB')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E069',
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

    Jump('loc_E0C7')

    def _loc_E069(): pass

    label('loc_E069')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E0C7',
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

    def _loc_E0C7(): pass

    label('loc_E0C7')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0032 offset: 0xE0E3
@scena.Code('func_32_E0E3')
def func_32_E0E3():
    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 3, 0x61B)),
            Expr.Return,
        ),
        'loc_E25F',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E17E',
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

    Jump('loc_E25C')

    def _loc_E17E(): pass

    label('loc_E17E')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E1F1',
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

    Jump('loc_E25C')

    def _loc_E1F1(): pass

    label('loc_E1F1')

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

    def _loc_E25C(): pass

    label('loc_E25C')

    Jump('loc_E2C5')

    def _loc_E25F(): pass

    label('loc_E25F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 5, 0x60D)),
            Expr.Return,
        ),
        'loc_E2C5',
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

    def _loc_E2C5(): pass

    label('loc_E2C5')

    ChrMoveToRelative(0x0000, -1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

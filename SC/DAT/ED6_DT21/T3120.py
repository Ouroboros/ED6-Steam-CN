import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T3120_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3120   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3120.x'
    header.mapIndex       = 1
    header.bgm            = 13
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT21/T3120._SN', 'ED6_DT21/T3120_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
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
        ('ED6_DT07/CH02610._CH', 'ED6_DT07/CH02610P._CP'),
        ('ED6_DT07/CH02020._CH', 'ED6_DT07/CH02020P._CP'),
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT06/CH20020._CH', 'ED6_DT06/CH20020P._CP'),
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT07/CH00040._CH', 'ED6_DT07/CH00040P._CP'),
        ('ED6_DT07/CH00033._CH', 'ED6_DT07/CH00033P._CP'),
        ('ED6_DT07/CH00043._CH', 'ED6_DT07/CH00043P._CP'),
        ('ED6_DT07/CH02620._CH', 'ED6_DT07/CH02620P._CP'),
        ('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01160._CH', 'ED6_DT07/CH01160P._CP'),
        ('ED6_DT07/CH01760._CH', 'ED6_DT07/CH01760P._CP'),
        ('ED6_DT07/CH00023._CH', 'ED6_DT07/CH00023P._CP'),
        ('ED6_DT07/CH00053._CH', 'ED6_DT07/CH00053P._CP'),
        ('ED6_DT07/CH00063._CH', 'ED6_DT07/CH00063P._CP'),
        ('ED6_DT07/CH00073._CH', 'ED6_DT07/CH00073P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH02490._CH', 'ED6_DT07/CH02490P._CP'),
    ]

# id: 0x10001 offset: 0x152
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '雾香',
            x                   = 3500,
            z                   = 0,
            y                   = 1200,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '拉赛尔博士',
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '提妲',
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
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0002,
        ),
        ScenaNpcData(
            name                = '测量仪',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '测量仪',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '测量仪',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '奥利维尔',
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
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0000,
        ),
        ScenaNpcData(
            name                = '科洛丝',
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
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0001,
        ),
        ScenaNpcData(
            name                = '玛多克工房长',
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
            name                = '金',
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
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '埃尔文',
            x                   = 1780,
            z                   = 1000,
            y                   = 53000,
            direction           = 183,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '耶鲁克',
            x                   = 52970,
            z                   = 0,
            y                   = 2400,
            direction           = 172,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '艾妲',
            x                   = 52390,
            z                   = 0,
            y                   = 53790,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '呆呆',
            x                   = 55570,
            z                   = 0,
            y                   = 51740,
            direction           = 63,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '王',
            x                   = 25480,
            z                   = 0,
            y                   = -3020,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '雪拉扎德',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '阿加特',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '吉米',
            x                   = 3500,
            z                   = 0,
            y                   = -3440,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '莫妮卡',
            x                   = 40,
            z                   = 1000,
            y                   = 50980,
            direction           = 359,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '临时',
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
    )

# id: 0x10002 offset: 0x3D2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x3D2
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -50,
            y           = 0,
            z           = -7200,
            range       = 3010,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFFE98A,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000014,
        ),
    )

# id: 0x10004 offset: 0x3F2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 3480,
            triggerZ            = 0,
            triggerY            = -710,
            triggerRange        = 400,
            actorX              = 3500,
            actorZ              = 1500,
            actorY              = 1200,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 1830,
            triggerZ            = 1000,
            triggerY            = 51000,
            triggerRange        = 400,
            actorX              = 1780,
            actorZ              = 2500,
            actorY              = 53000,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 53210,
            triggerZ            = 0,
            triggerY            = 520,
            triggerRange        = 400,
            actorX              = 52970,
            actorZ              = 1500,
            actorY              = 2400,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -1320,
            triggerZ            = 0,
            triggerY            = -4700,
            triggerRange        = 1400,
            actorX              = -1320,
            actorZ              = 2000,
            actorY              = -4700,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x482
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 7, 0x1417)),
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Or,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5AD',
    )

    ClearScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_4D6',
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4D6',
    )

    ChrSetFlags(0x0011, 0x0004)
    ChrSetPos(0x0011, 23530, 200, -2100, 0)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetChipByIndex(0x0011, 18)
    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    def _loc_4D6(): pass

    label('loc_4D6')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_529',
    )

    ChrSetFlags(0x000E, 0x0004)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_508',
    )

    ChrSetPos(0x000E, 23530, 200, -2100, 0)
    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    Jump('loc_51C')

    def _loc_508(): pass

    label('loc_508')

    ChrSetPos(0x000E, 23530, 200, 400, 180)
    ClearScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    def _loc_51C(): pass

    label('loc_51C')

    ChrClearFlags(0x000E, 0x0080)
    ChrSetChipByIndex(0x000E, 6)
    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    def _loc_529(): pass

    label('loc_529')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_57C',
    )

    ChrSetFlags(0x000F, 0x0004)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_55B',
    )

    ChrSetPos(0x000F, 23530, 200, -2100, 0)
    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    Jump('loc_56F')

    def _loc_55B(): pass

    label('loc_55B')

    ChrSetPos(0x000F, 23530, 200, 400, 180)
    ClearScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    def _loc_56F(): pass

    label('loc_56F')

    ChrClearFlags(0x000F, 0x0080)
    ChrSetChipByIndex(0x000F, 7)
    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    def _loc_57C(): pass

    label('loc_57C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5AD',
    )

    ChrSetFlags(0x000A, 0x0004)
    ChrSetPos(0x000A, 23530, 200, 400, 180)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetChipByIndex(0x000A, 17)
    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    def _loc_5AD(): pass

    label('loc_5AD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_5C1',
    )

    ChrClearFlags(0x001A, 0x0080)
    ChrSetFlags(0x0016, 0x0080)

    Jump('loc_601')

    def _loc_5C1(): pass

    label('loc_5C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_5DC',
    )

    ChrSetPos(0x0016, 61080, 2000, 2170, 0)

    Jump('loc_601')

    def _loc_5DC(): pass

    label('loc_5DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_5F0',
    )

    ChrSetFlags(0x0014, 0x0080)
    ChrSetFlags(0x0016, 0x0080)

    Jump('loc_601')

    def _loc_5F0(): pass

    label('loc_5F0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_601',
    )

    ChrSetFlags(0x0014, 0x0080)
    ChrSetFlags(0x0016, 0x0080)

    def _loc_601(): pass

    label('loc_601')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6CA',
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_643',
    )

    ChrClearFlags(0x0017, 0x0080)
    ChrSetFlags(0x0017, 0x0004)
    ChrSetChipByIndex(0x0017, 15)
    ChrSetPos(0x0017, 23550, 200, 420, 180)

    def _loc_643(): pass

    label('loc_643')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_670',
    )

    ChrClearFlags(0x0018, 0x0080)
    ChrSetFlags(0x0018, 0x0004)
    ChrSetChipByIndex(0x0018, 16)
    ChrSetPos(0x0018, 26270, 200, -480, 90)

    def _loc_670(): pass

    label('loc_670')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_69D',
    )

    ChrClearFlags(0x000A, 0x0080)
    ChrSetFlags(0x000A, 0x0004)
    ChrSetChipByIndex(0x000A, 17)
    ChrSetPos(0x000A, 28530, 200, -570, 270)

    def _loc_69D(): pass

    label('loc_69D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_6CA',
    )

    ChrClearFlags(0x0011, 0x0080)
    ChrSetFlags(0x0011, 0x0004)
    ChrSetChipByIndex(0x0011, 18)
    ChrSetPos(0x0011, 23550, 200, -2170, 0)

    def _loc_6CA(): pass

    label('loc_6CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_6E0',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    Event(1, 0x0010)

    Jump('loc_770')

    def _loc_6E0(): pass

    label('loc_6E0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_6FF',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    MapSetFlags(0x10000000)
    Event(0, func_0D_4BFF)

    Jump('loc_770')

    def _loc_6FF(): pass

    label('loc_6FF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Return,
        ),
        'loc_71E',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x74),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    MapSetFlags(0x10000000)
    Event(0, func_0E_7943)

    Jump('loc_770')

    def _loc_71E(): pass

    label('loc_71E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 3, 0x10F3)),
            Expr.Return,
        ),
        'loc_734',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    MapSetFlags(0x10000000)
    Event(1, 0x000D)

    Jump('loc_770')

    def _loc_734(): pass

    label('loc_734')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_740'),
        (-1, 'loc_770'),
    )

    def _loc_740(): pass

    label('loc_740')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 5, 0x2005)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_758',
    )

    MapSetFlags(0x10000000)
    Event(0, func_0F_7C4C)

    Jump('loc_76D')

    def _loc_758(): pass

    label('loc_758')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 7, 0x1417)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_76D',
    )

    MapSetFlags(0x10000000)
    Event(1, 0x0016)

    def _loc_76D(): pass

    label('loc_76D')

    Jump('loc_770')

    def _loc_770(): pass

    label('loc_770')

    Return()

# id: 0x0001 offset: 0x771
@scena.Code('func_01_771')
def func_01_771():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0290, 4, 0x1484)),
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_78A',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_78A(): pass

    label('loc_78A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 3, 0x13)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7B9',
    )

    TerminateThread(0x0015, 0x00)
    ChrSetFlags(0x0015, 0x0010)

    ExecExpressionWithValue(
        0x0015,
        0x01,
        (
            (Expr.PushReg, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0015,
        0x03,
        (
            (Expr.PushReg, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0015,
        0x04,
        (
            (Expr.PushReg, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_7B9(): pass

    label('loc_7B9')

    Return()

# id: 0x0002 offset: 0x7BA
@scena.Code('func_02_7BA')
def func_02_7BA():
    ExecExpressionWithReg(
        0x0001,
        (
            Expr.Rand,
            (Expr.PushLong, 0x8),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Switch(
        (
            (Expr.PushReg, 0x1),
            Expr.Return,
        ),
        (0x00000000, 'loc_7EB'),
        (0x00000001, 'loc_7F7'),
        (0x00000002, 'loc_803'),
        (0x00000003, 'loc_80F'),
        (0x00000004, 'loc_81B'),
        (0x00000005, 'loc_827'),
        (0x00000006, 'loc_833'),
        (-1, 'loc_83F'),
    )

    def _loc_7EB(): pass

    label('loc_7EB')

    OP_99(0x00FE, 0x00, 0x07, 1450)

    Jump('loc_84B')

    def _loc_7F7(): pass

    label('loc_7F7')

    OP_99(0x00FE, 0x00, 0x07, 1550)

    Jump('loc_84B')

    def _loc_803(): pass

    label('loc_803')

    OP_99(0x00FE, 0x00, 0x07, 1600)

    Jump('loc_84B')

    def _loc_80F(): pass

    label('loc_80F')

    OP_99(0x00FE, 0x00, 0x07, 1400)

    Jump('loc_84B')

    def _loc_81B(): pass

    label('loc_81B')

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_84B')

    def _loc_827(): pass

    label('loc_827')

    OP_99(0x00FE, 0x00, 0x07, 1350)

    Jump('loc_84B')

    def _loc_833(): pass

    label('loc_833')

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_84B')

    def _loc_83F(): pass

    label('loc_83F')

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_84B')

    def _loc_84B(): pass

    label('loc_84B')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_860',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_84B')

    def _loc_860(): pass

    label('loc_860')

    Return()

# id: 0x0003 offset: 0x861
@scena.Code('func_03_861')
def func_03_861():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_88E',
    )

    def _loc_868(): pass

    label('loc_868')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_88B',
    )

    OP_8D(0x00FE, 58120, 52460, 56040, 51120, 3000)

    Jump('loc_868')

    def _loc_88B(): pass

    label('loc_88B')

    Jump('loc_8B1')

    def _loc_88E(): pass

    label('loc_88E')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_8B1',
    )

    OP_8D(0x00FE, 52620, 51160, 59990, 53120, 3000)

    Jump('loc_88E')

    def _loc_8B1(): pass

    label('loc_8B1')

    Return()

# id: 0x0004 offset: 0x8B2
@scena.Code('func_04_8B2')
def func_04_8B2():
    Call(0, 0x0005)

    Return()

# id: 0x0005 offset: 0x8B7
@scena.Code('func_05_8B7')
def func_05_8B7():
    TalkBegin(0x0012)
    Call(6, 0x0004)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8E2',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8DC',
    )

    OP_A9(0x9E)

    Jump('loc_8DE')

    def _loc_8DC(): pass

    label('loc_8DC')

    OP_A9(0x98)

    def _loc_8DE(): pass

    label('loc_8DE')

    TalkEnd(0x0012)

    Return()

    def _loc_8E2(): pass

    label('loc_8E2')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8F3',
    )

    TalkEnd(0x0012)

    Return()

    def _loc_8F3(): pass

    label('loc_8F3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_A67',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9E6',
    )

    ChrTalk(
        0x0012,
        (
            '不久前中央工房的人\n',
            '来买油灯的灯油呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '那里原本装设的全是导力灯，\n',
            '这下可就麻烦了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '多亏他们制造了夜视眼镜，\n',
            '戴上之后就可以通过漆黑的卡鲁迪亚隧道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '拐弯抹角的话就不多说了，\n',
            '总之我就是在推销而已啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_A64')

    def _loc_9E6(): pass

    label('loc_9E6')

    ChrTalk(
        0x0012,
        (
            '卡鲁迪亚隧道现在一团漆黑，\n',
            '想走那里的话一定要买夜视眼镜才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '这是中央工房的特制产品，\n',
            '戴上之后可以在黑暗中看东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A64(): pass

    label('loc_A64')

    Jump('loc_FB9')

    def _loc_A67(): pass

    label('loc_A67')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_BF4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B48',
    )

    ChrTalk(
        0x0012,
        (
            '呀，欢迎。\n',
            '欢迎光临贝尔杂货店～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '大家好像遇到了麻烦吧，\n',
            '从早上开始客人就一直不断。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '听说卡鲁迪亚隧道现在漆黑一团，\n',
            '不过只要戴上这眼镜就ＯＫ了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '要是想去卢安的话\n',
            '这个东西是一定要买的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_BF1')

    def _loc_B48(): pass

    label('loc_B48')

    ChrTalk(
        0x0012,
        (
            '大家好像遇到了什么麻烦，\n',
            '从早上开始客人就一直不断。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '听说卡鲁迪亚隧道现在漆黑一团，\n',
            '不过只要戴上这眼镜就ＯＫ了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '要是想去卢安的话\n',
            '这个东西是一定要买的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BF1(): pass

    label('loc_BF1')

    Jump('loc_FB9')

    def _loc_BF4(): pass

    label('loc_BF4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_CAF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_C47',
    )

    ChrTalk(
        0x0012,
        (
            '听说地震不会再来了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '中央工房发表的声明是不会骗人的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CAC')

    def _loc_C47(): pass

    label('loc_C47')

    ChrTalk(
        0x0012,
        (
            '啊，你好。\n',
            '欢迎光临贝尔杂货店～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '听说已经不会再有地震了，\n',
            '这样的话就可以放心去买东西了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_CAC(): pass

    label('loc_CAC')

    Jump('loc_FB9')

    def _loc_CAF(): pass

    label('loc_CAF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_DEF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_D3B',
    )

    ChrTalk(
        0x0012,
        (
            '我老婆去礼拜堂\n',
            '找药去了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '不过今天怎么回来这么晚啊。\n',
            '难道还有其他别的事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '每次去都是很快\n',
            '就回来了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DEC')

    def _loc_D3B(): pass

    label('loc_D3B')

    ChrTalk(
        0x0012,
        (
            '我老婆\n',
            '经常去礼拜堂呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '她一直有肩酸的毛病，\n',
            '所以要去找教区长领取药品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '不过，说起来的话……\n',
            '今天回来得好像比平时晚不少啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '每次去都是很快\n',
            '就回来了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_DEC(): pass

    label('loc_DEC')

    Jump('loc_FB9')

    def _loc_DEF(): pass

    label('loc_DEF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_F00',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_E65',
    )

    ChrTalk(
        0x0012,
        (
            '工房遭遇袭击的事件\n',
            '到现在我仿佛还历历在目呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '那次的事件\n',
            '在当时可是改变了我们\n',
            '的想法呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EFD')

    def _loc_E65(): pass

    label('loc_E65')

    ChrTalk(
        0x0012,
        (
            '以前我和妻子经常会因为经营方针的不和\n',
            '而产生冲突矛盾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '但工房遭到袭击后\n',
            '我们就再也没吵过架。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '我们今后的目标是要经营\n',
            '两个人共同的店铺。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_EFD(): pass

    label('loc_EFD')

    Jump('loc_FB9')

    def _loc_F00(): pass

    label('loc_F00')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 0, 0x1408)),
            Expr.Return,
        ),
        'loc_FB9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_F64',
    )

    ChrTalk(
        0x0012,
        (
            '我们这里的东西可以说是应有尽有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '不管食材还是日用品，\n',
            '你想找的都能找到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FB9')

    def _loc_F64(): pass

    label('loc_F64')

    ChrTalk(
        0x0012,
        (
            '呀，欢迎。\n',
            '欢迎光临贝尔杂货店～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '我是不会输给地震的，\n',
            '今天也要照常营业！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_FB9(): pass

    label('loc_FB9')

    TalkEnd(0x0012)

    Return()

# id: 0x0006 offset: 0xFBD
@scena.Code('func_06_FBD')
def func_06_FBD():
    TalkBegin(0x0014)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_10BD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1062',
    )

    ChrTalk(
        0x00FE,
        (
            '导力器无法运转了，\n',
            '家务事也变得很麻烦呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是再不去拿治疗肩膀的药\n',
            '可就快撑不下去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，真想去亚尔摩温泉\n',
            '好好泡个热水澡啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_10BA')

    def _loc_1062(): pass

    label('loc_1062')

    ChrTalk(
        0x00FE,
        (
            '家务活真是累人，\n',
            '肩膀都快疼死了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '再不早点去礼拜堂拿药的话\n',
            '可就要撑不下去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10BA(): pass

    label('loc_10BA')

    Jump('loc_1361')

    def _loc_10BD(): pass

    label('loc_10BD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_11F5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1196',
    )

    ChrTalk(
        0x00FE,
        (
            '很多平时不常用的东西最近卖得很好，\n',
            '让我赚了不少……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，那也就意味着\n',
            '大家遇到了什么困难吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是一直这样下去的话\n',
            '我这里也就不是杂货店了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望中央工房的人\n',
            '能早点解决危机。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_11F2')

    def _loc_1196(): pass

    label('loc_1196')

    ChrTalk(
        0x00FE,
        (
            '要是一直这样下去的话\n',
            '我这里也就不是杂货店了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望中央工房的人\n',
            '能早点解决危机。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11F2(): pass

    label('loc_11F2')

    Jump('loc_1361')

    def _loc_11F5(): pass

    label('loc_11F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_128D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1247',
    )

    ChrTalk(
        0x00FE,
        (
            '听说地震已经不会再来了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '果然在礼拜堂祈祷\n',
            '是有用的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_128A')

    def _loc_1247(): pass

    label('loc_1247')

    ChrTalk(
        0x00FE,
        (
            '听说地震已经不会再来了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵呵，祈祷也是有用的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_128A(): pass

    label('loc_128A')

    Jump('loc_1361')

    def _loc_128D(): pass

    label('loc_128D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 0, 0x1408)),
            Expr.Return,
        ),
        'loc_1361',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_12FA',
    )

    ChrTalk(
        0x00FE,
        (
            '接下来还要去找教区长\n',
            '拿治疗肩膀的药。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望地震别再来了，\n',
            '我今天也有虔诚地祈祷呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1361')

    def _loc_12FA(): pass

    label('loc_12FA')

    ChrTalk(
        0x00FE,
        (
            '希望地震别再来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总觉得地震还会再来，\n',
            '实在安心不下来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天还是继续\n',
            '祈祷比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_1361(): pass

    label('loc_1361')

    TalkEnd(0x0014)

    Return()

# id: 0x0007 offset: 0x1365
@scena.Code('func_07_1365')
def func_07_1365():
    TalkBegin(0x0015)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1652',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0418, 1, 0x20C1)),
            Expr.Ez,
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_14CA',
    )

    ChrTurnDirection(0x00FE, 0x0107, 0)

    ChrTalk(
        0x00FE,
        (
            '嘿～提妲姐姐～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在的情况\n',
            '怎么样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#063F嗯～抱歉…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '姐姐我们\n',
            '现在还在调查中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎～是吗…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F嗯，所以请再\n',
            '稍等一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '姐姐我们一定\n',
            '会让一切都恢复原样的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯～～我明白了。\n',
            '一言为定哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那好吧～\n',
            '到时还要一起\n',
            '玩上次的游戏啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#067F嗯、嗯，没问题。\n',
            '（到、到底是什么游戏呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0418, 1, 0x20C1))

    Jump('loc_164F')

    def _loc_14CA(): pass

    label('loc_14CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1517',
    )

    ChrTalk(
        0x00FE,
        (
            '那、下次还要\n',
            '一起玩以前的',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '游戏哦，\n',
            '提妲姐姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_164F')

    def _loc_1517(): pass

    label('loc_1517')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_1557',
    )

    ChrTalk(
        0x00FE,
        (
            '妈妈的肩膀\n',
            '又开始疼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是因为太\n',
            '劳累了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_164F')

    def _loc_1557(): pass

    label('loc_1557')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_15FA',
    )

    ChrTalk(
        0x00FE,
        (
            '哎～看啊看啊～\n',
            '是新游戏呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我想出来的、\n',
            '嘿～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00FE, 0, 400)
    Sleep(500)

    ChrTalk(
        0x00FE,
        (
            '冲啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '砰………………………！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x00FE, 0x00)
    ChrSetFlags(0x00FE, 0x0010)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.GetChrWork, 0x15, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.GetChrWork, 0x15, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.GetChrWork, 0x15, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetScenaFlags(ScenaFlag(0x0002, 3, 0x13))
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_164F')

    def _loc_15FA(): pass

    label('loc_15FA')

    ChrTalk(
        0x00FE,
        (
            '……………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……………………………………\n',
            '（在干什么啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_164F(): pass

    label('loc_164F')

    Jump('loc_1903')

    def _loc_1652(): pass

    label('loc_1652')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_16E1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_16AD',
    )

    ChrTalk(
        0x00FE,
        (
            '啊～可是这样的话\n',
            '会让哥哥生气的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……嗯、果然还是\n',
            '不应该来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16DE')

    def _loc_16AD(): pass

    label('loc_16AD')

    ChrTalk(
        0x00FE,
        (
            '哎？还是没有地震吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我还很期待呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_16DE(): pass

    label('loc_16DE')

    Jump('loc_1903')

    def _loc_16E1(): pass

    label('loc_16E1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_1777',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1731',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯～今天\n',
            '妈妈回来得好晚啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '平时这时候都已经回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1774')

    def _loc_1731(): pass

    label('loc_1731')

    ChrTalk(
        0x00FE,
        (
            '嗯～今天\n',
            '妈妈回来得好晚啊，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为什么到\n',
            '现在还不回来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_1774(): pass

    label('loc_1774')

    Jump('loc_1903')

    def _loc_1777(): pass

    label('loc_1777')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 7, 0x1417)),
            Expr.Return,
        ),
        'loc_1893',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_17D1',
    )

    ChrTalk(
        0x00FE,
        (
            '啊～地震快点\n',
            '来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_17A4')
    def lambda_17A4():
        OP_9E(0x00FE, 30, 0, 0, 3000)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_17A4)

    ChrTalk(
        0x00FE,
        (
            '哇～～来了来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_188C')

    def _loc_17D1(): pass

    label('loc_17D1')

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x00FE, 0x0107, 0)

    ChrTalk(
        0x00FE,
        (
            '啊～提妲姐姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '地震来了～地震来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#064F地震来了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '是在假装地震吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是呀～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1853')
    def lambda_1853():
        OP_9E(0x00FE, 30, 0, 0, 3000)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_1853)

    ChrTalk(
        0x00FE,
        (
            '轰隆隆隆～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哇～是地震！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_188C(): pass

    label('loc_188C')

    TerminateThread(0x00FE, 0x01)

    Jump('loc_1903')

    def _loc_1893(): pass

    label('loc_1893')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_18D1',
    )

    ChrTalk(
        0x00FE,
        (
            '妈妈\n',
            '去礼拜堂了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像是去找教区长\n',
            '拿药。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1903')

    def _loc_18D1(): pass

    label('loc_18D1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 0, 0x1408)),
            Expr.Return,
        ),
        'loc_1903',
    )

    ChrTalk(
        0x00FE,
        (
            '我在玩地震\n',
            '的游戏。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要一起玩吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1903(): pass

    label('loc_1903')

    TalkEnd(0x0015)

    Return()

# id: 0x0008 offset: 0x1907
@scena.Code('func_08_1907')
def func_08_1907():
    Call(0, 0x0009)

    Return()

# id: 0x0009 offset: 0x190C
@scena.Code('func_09_190C')
def func_09_190C():
    TalkBegin(0x0013)
    Call(6, 0x0004)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1937',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_1931',
    )

    OP_A9(0xA9)

    Jump('loc_1933')

    def _loc_1931(): pass

    label('loc_1931')

    OP_A9(0x97)

    def _loc_1933(): pass

    label('loc_1933')

    TalkEnd(0x0013)

    Return()

    def _loc_1937(): pass

    label('loc_1937')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1948',
    )

    TalkEnd(0x0013)

    Return()

    def _loc_1948(): pass

    label('loc_1948')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_1A43',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_19E0',
    )

    ChrTalk(
        0x0013,
        (
            '我的店本来是以贩卖枪类武器\n',
            '为主的，不过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '这次也进了不少\n',
            '近战型的武器。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '虽然不想这样……\n',
            '但现在这种情况也没办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_1A40')

    def _loc_19E0(): pass

    label('loc_19E0')

    ChrTalk(
        0x0013,
        (
            '枪炮类的武器无法使用，\n',
            '只能进些近战武器了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '虽然不想这样……\n',
            '但现在这种情况也没办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A40(): pass

    label('loc_1A40')

    Jump('loc_2109')

    def _loc_1A43(): pass

    label('loc_1A43')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1B99',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1B2C',
    )

    ChrTalk(
        0x0013,
        (
            '真没办法啊……\n',
            '本来我们是主营业导力炮的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '因为最近的这一系列异变\n',
            '销售量直线下降，已经严重赤字了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '中央工房的那些家伙\n',
            '到底在做什么啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '我们的生活已经严重受影响了，\n',
            '研究者们还是危机意识不足啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_1B96')

    def _loc_1B2C(): pass

    label('loc_1B2C')

    ChrTalk(
        0x0013,
        (
            '中央工房的那些家伙\n',
            '到底在做什么啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '理论研究等东西都无所谓，\n',
            '现在最关键的是要调查出异变的原因。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B96(): pass

    label('loc_1B96')

    Jump('loc_2109')

    def _loc_1B99(): pass

    label('loc_1B99')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_1D40',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1C6C',
    )

    ChrTalk(
        0x0013,
        (
            '帝国莱恩福尔特社和\n',
            '共和国的乌尔努社……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '这两家是目前最大的\n',
            '导力枪制造商。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '当然了！我们蔡斯中央工房\n',
            '的技术力也是不会输给他们的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '总有一天会让ＺＣＦ的标志\n',
            '变成世界最强的象征。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D3D')

    def _loc_1C6C(): pass

    label('loc_1C6C')

    ChrTalk(
        0x0013,
        (
            '说起来的话，再过不久\n',
            '就是互不侵犯条约的签字仪式了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '我们和帝国的枪械制造社\n',
            '也都有往来的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '哟，帝国的莱恩福尔特社，\n',
            '你们应该也听说过吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '嗯，那里并不只是生产枪械，\n',
            '连战车也都有制造。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_1D3D(): pass

    label('loc_1D3D')

    Jump('loc_2109')

    def _loc_1D40(): pass

    label('loc_1D40')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_1E8D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1DC1',
    )

    ChrTalk(
        0x0013,
        (
            '虽然还在开发中，但斯坦因先生\n',
            '可是很重视的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '如果遇到技术高超的专业人士，\n',
            '一定可以学到有用的枪械知识。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E8A')

    def _loc_1DC1(): pass

    label('loc_1DC1')

    ChrTalk(
        0x0013,
        (
            '不久前斯坦因先生给我看了\n',
            '开发中的新型枪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '那种型号很罕见，\n',
            '我非常喜欢呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '经过足够的测试之后\n',
            '相信一定很快就能流行起来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '斯坦因先生对它也是赞美有加。\n',
            '一定可以学到有用的枪械知识。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_1E8A(): pass

    label('loc_1E8A')

    Jump('loc_2109')

    def _loc_1E8D(): pass

    label('loc_1E8D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_1F82',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1EE5',
    )

    ChrTalk(
        0x0013,
        (
            '斯坦因先生虽然技术高超\n',
            '但却不太好相处。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '真是苦了技术员们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F7F')

    def _loc_1EE5(): pass

    label('loc_1EE5')

    ChrTalk(
        0x0013,
        (
            '这家店的主人\n',
            '就是斯坦因先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '虽然他有些倔强，\n',
            '但对武器的见解还是很强的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '总之是个技术高超\n',
            '却不太好相处的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '真是苦了技术员们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_1F7F(): pass

    label('loc_1F7F')

    Jump('loc_2109')

    def _loc_1F82(): pass

    label('loc_1F82')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 0, 0x1408)),
            Expr.Return,
        ),
        'loc_2109',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_203E',
    )

    ChrTalk(
        0x0013,
        (
            '虽然被地震吓了一跳，\n',
            '但是我并不在意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '所谓的地震，本来就是周期性的\n',
            '普通自然现象而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '我们作为受过良好教育的工房都市居民，\n',
            '遇到这种情况时自然应该保持冷静。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2109')

    def _loc_203E(): pass

    label('loc_203E')

    ChrTalk(
        0x0013,
        (
            '哟，欢迎光临。\n',
            '欢迎光临斯坦因武器店，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '虽然被地震吓了一跳，\n',
            '但是我并不在意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '那只是再普通不过的\n',
            '自然现象而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '我们作为受过良好教育的工房都市居民，\n',
            '遇到这种情况时自然应该保持冷静。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_2109(): pass

    label('loc_2109')

    TalkEnd(0x0013)

    Return()

# id: 0x000A offset: 0x210D
@scena.Code('func_0A_210D')
def func_0A_210D():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            (Expr.TestScenaFlags, ScenaFlag(0x0418, 7, 0x20C7)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_29FB',
    )

    EventBegin(0x00)
    Fade(1000)
    CameraMove(2920, 0, 700, 0)
    OP_67(0, 5850, -10000, 0)
    CameraSetDistance(2320, 0)
    OP_6C(315000, 0)
    OP_6E(332, 0)
    ChrSetPos(0x0101, 4360, 0, -720, 0)
    ChrSetPos(0x0102, 3220, 0, -700, 0)
    ChrSetPos(0x00F8, 4600, 0, -1800, 0)
    ChrSetPos(0x00F9, 3230, 0, -1800, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0401, 4, 0x200C)),
            Expr.Return,
        ),
        'loc_2332',
    )

    ChrTalk(
        0x0008,
        (
            '#0580370709V#790F你们还是和以前一样忙，\n',
            '整天到处跑啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370710V啊，温泉的水泵\n',
            '已经修好了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370711V#1001F#4P嗯、已经修好了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010370712V#1015F……嗯、总之先来\n',
            '做个正式的报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370713V#1040F#1P那么，先做个报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '将亚尔摩温泉的水泵\n',
            '已经修理好的情况做了说明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#0580370714V#790F呵呵，看来比想象中的\n',
            '还麻烦呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2492')

    def _loc_2332(): pass

    label('loc_2332')

    ChrTalk(
        0x0008,
        (
            '#0580370715V#790F听工房长说过了，\n',
            '好像很忙的样子呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370716V发生什么事情了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370717V#1011F#4P啊，是啊是啊。\n',
            '要报告一下才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370718V#1035F#1P嗯嗯，其实……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '将亚尔摩温泉的水泵\n',
            '已经修理好的情况做了说明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#0580370719V#790F呼呼～原来如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370720V果然是游击士\n',
            '要做的工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2492(): pass

    label('loc_2492')

    ChrTalk(
        0x0101,
        (
            '#0010370721V#1015F#4P嗯，在这种非常时期\n',
            '似乎有点过于悠闲了呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010370722V#1002F不过，遇到有困难的人\n',
            '总没有办法坐视不管。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2580',
    )

    ChrTalk(
        0x0108,
        (
            '#0080370723V#070F啊啊，那也正是\n',
            '游击士的精神啊，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080370724V我认为这是正确的判断。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2650')

    def _loc_2580(): pass

    label('loc_2580')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_25EB',
    )

    ChrTalk(
        0x0106,
        (
            '#0050370725V#051F啊啊～那也正是\n',
            '游击士的精神啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050370726V我认为这是正确的判断。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2650')

    def _loc_25EB(): pass

    label('loc_25EB')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2650',
    )

    ChrTalk(
        0x0103,
        (
            '#0030370727V#020F嗯，那也正是游击士的精神啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030370728V我认为这是正确的判断。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2650(): pass

    label('loc_2650')

    ChrTalk(
        0x0008,
        (
            '#0580370729V#792F协会规章第二项……\n',
            '以保护市民为原则。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370730V以那种精神来判定的话，\n',
            '你们的决断自然是正确的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370731V#791F你们做的很好，\n',
            '很值得自豪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370732V#1008F#4P嘿嘿嘿，谢谢啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010370733V被雾香小姐这么一说，\n',
            '一下子就有自信了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370734V#1040F#1P……报告就这么多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x00C2, 0x00, 0x20)"),
            Expr.Return,
        ),
        'loc_2794',
    )

    SetScenaFlags(ScenaFlag(0x0002, 0, 0x10))

    Jump('loc_2797')

    def _loc_2794(): pass

    label('loc_2794')

    ClearScenaFlags(ScenaFlag(0x0002, 0, 0x10))

    def _loc_2797(): pass

    label('loc_2797')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2851',
    )

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
        0,
        (
            TXT(0x00, '【◇地方任务未报告（QF_REPORT不成立）】\n'),
            TXT(0x01, '【◇在其他支部报告完毕（QF_REPORT成立）】\n'),
            TXT(0x02, '【◇不变更】\n'),
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
        (0x00000000, 'loc_2845'),
        (0x00000001, 'loc_284B'),
        (-1, 'loc_2851'),
    )

    def _loc_2845(): pass

    label('loc_2845')

    ClearScenaFlags(ScenaFlag(0x0002, 0, 0x10))

    Jump('loc_2851')

    def _loc_284B(): pass

    label('loc_284B')

    SetScenaFlags(ScenaFlag(0x0002, 0, 0x10))

    Jump('loc_2851')

    def _loc_2851(): pass

    label('loc_2851')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2930',
    )

    ChrTalk(
        0x0008,
        (
            '#0580370735V#790F那么，接下来我们\n',
            '马上就会去核查。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370736V要想收取报酬的话，\n',
            '请重新选择『报告』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370737V#1011F#4P在领取报酬的时候\n',
            '再来报告就可以了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580370738V#790F嗯，那就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29F2')

    def _loc_2930(): pass

    label('loc_2930')

    ChrTalk(
        0x0008,
        (
            '#0580370739V#790F核查已经结束了，\n',
            '这件事也算是告一段落。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370740V那么，各位今后\n',
            '也要小心行事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370741V#1006F#4P嗯，了解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370742V#1040F#1P是的……\n',
            '那就先失礼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_29F2(): pass

    label('loc_29F2')

    SetScenaFlags(ScenaFlag(0x0418, 7, 0x20C7))
    EventEnd(0x00)
    TalkEnd(0x0008)

    Return()

    def _loc_29FB(): pass

    label('loc_29FB')

    If(
        (
            (Expr.Eval, "OP_29(0x006C, 0x00, 0x02)"),
            (Expr.Eval, "OP_29(0x006C, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x006C, 0x01, 0x0004)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2A67',
    )

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
            TXT(0x01, '报告\n'),
            TXT(0x02, '有关招牌板\n'),
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

    Jump('loc_2B76')

    def _loc_2A67(): pass

    label('loc_2A67')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B72',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0401, 3, 0x200B)),
            (Expr.TestScenaFlags, ScenaFlag(0x0401, 4, 0x200C)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0401, 6, 0x200E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2B10',
    )

    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2AD2',
    )

    Menu(
        0,
        10,
        100,
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '报告\n'),
            TXT(0x02, '呼叫同伴\n'),
            TXT(0x03, '向要塞询问\n'),
            TXT(0x04, '离开\n'),
        ),
    )

    Jump('loc_2AF5')

    def _loc_2AD2(): pass

    label('loc_2AD2')

    Menu(
        0,
        10,
        100,
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '报告\n'),
            TXT(0x02, '向要塞询问\n'),
            TXT(0x03, '离开\n'),
        ),
    )

    def _loc_2AF5(): pass

    label('loc_2AF5')

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

    Jump('loc_2B6F')

    def _loc_2B10(): pass

    label('loc_2B10')

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2B6B',
    )

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
            TXT(0x01, '报告\n'),
            TXT(0x02, '呼叫同伴\n'),
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

    Jump('loc_2B6F')

    def _loc_2B6B(): pass

    label('loc_2B6B')

    Call(6, 0x0005)

    def _loc_2B6F(): pass

    label('loc_2B6F')

    Jump('loc_2B76')

    def _loc_2B72(): pass

    label('loc_2B72')

    Call(6, 0x0005)

    def _loc_2B76(): pass

    label('loc_2B76')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2DC2',
    )

    OP_0D()
    Sleep(200)

    If(
        (
            (Expr.Eval, "OP_29(0x0085, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0085, 0x00, 0x20)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2C69',
    )

    ChrTalk(
        0x0008,
        (
            '#0580370743V#790F辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370744V之前一系列调查的报酬\n',
            '已经给你们准备好了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_AF(0x9A, 0x0085)
    Sleep(100)

    OP_28(0x0086, 0x04, 0x20)
    OP_28(0x0087, 0x04, 0x20)

    ChrTalk(
        0x0008,
        (
            '#0580370745V#790F去亚尔摩村之前\n',
            '最好先好好整备一下装备。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370746V总之，请小心行事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2DBC')

    def _loc_2C69(): pass

    label('loc_2C69')

    If(
        (
            (Expr.Eval, "OP_29(0x00C0, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x00C0, 0x00, 0x20)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2CE8',
    )

    OP_28(0x00C3, 0x04, 0x20)
    OP_A9(0x9A)

    ChrTalk(
        0x0008,
        (
            '#0580370747V#790F辛苦了。\n',
            '看来顺利达成目的了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370748V完成了什么任务的话\n',
            '再来报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2DBC')

    def _loc_2CE8(): pass

    label('loc_2CE8')

    If(
        (
            (Expr.Eval, "OP_A9(0x9A)"),
            Expr.Return,
        ),
        'loc_2D55',
    )

    ChrTalk(
        0x0008,
        (
            '#0580370749V#790F辛苦了。\n',
            '看来顺利达成目的了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370750V完成了什么任务的话\n',
            '再来报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2DBC')

    def _loc_2D55(): pass

    label('loc_2D55')

    ChrTalk(
        0x0008,
        (
            '#0580370751V#790F啊，现在\n',
            '好像没有可以报告的工作吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370752V完成了什么任务的话\n',
            '再来报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2DBC(): pass

    label('loc_2DBC')

    OP_56(0x00)
    TalkEnd(0x0008)

    Return()

    def _loc_2DC2(): pass

    label('loc_2DC2')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2F0B',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x006C, 0x00, 0x02)"),
            (Expr.Eval, "OP_29(0x006C, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x006C, 0x01, 0x0004)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2E18',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x006C, 0x00, 0x04)"),
            Expr.Return,
        ),
        'loc_2DFB',
    )

    Call(1, 0x000C)

    Jump('loc_2E12')

    def _loc_2DFB(): pass

    label('loc_2DFB')

    If(
        (
            (Expr.Eval, "OP_29(0x006C, 0x01, 0x8000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2E0E',
    )

    Call(1, 0x0009)

    Jump('loc_2E12')

    def _loc_2E0E(): pass

    label('loc_2E0E')

    Call(1, 0x000A)

    def _loc_2E12(): pass

    label('loc_2E12')

    TalkEnd(0x0008)

    Jump('loc_2F0A')

    def _loc_2E18(): pass

    label('loc_2E18')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2EDA',
    )

    ChrTalk(
        0x0008,
        (
            '#0580370753V#790F要呼叫同伴吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370754V了解。\n',
            '马上就和他们进行联络。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '联络各支部，\n',
            '集合了待命人员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeIn(1000, 0)
    OP_0D()
    TalkEnd(0x0008)

    Jump('loc_2F0A')

    def _loc_2EDA(): pass

    label('loc_2EDA')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2F07',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0401, 3, 0x200B)),
            (Expr.TestScenaFlags, ScenaFlag(0x0401, 4, 0x200C)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0401, 6, 0x200E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2F01',
    )

    Call(0, 0x001A)
    TalkEnd(0x0008)

    Jump('loc_2F04')

    def _loc_2F01(): pass

    label('loc_2F01')

    TalkEnd(0x0008)

    def _loc_2F04(): pass

    label('loc_2F04')

    Jump('loc_2F0A')

    def _loc_2F07(): pass

    label('loc_2F07')

    TalkEnd(0x0008)

    def _loc_2F0A(): pass

    label('loc_2F0A')

    Return()

    def _loc_2F0B(): pass

    label('loc_2F0B')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2F3E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0401, 3, 0x200B)),
            (Expr.TestScenaFlags, ScenaFlag(0x0401, 4, 0x200C)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0401, 6, 0x200E)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2F3A',
    )

    Call(0, 0x001A)
    TalkEnd(0x0008)

    Return()

    def _loc_2F3A(): pass

    label('loc_2F3A')

    TalkEnd(0x0008)

    Return()

    def _loc_2F3E(): pass

    label('loc_2F3E')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2F4F',
    )

    TalkEnd(0x0008)

    Return()

    def _loc_2F4F(): pass

    label('loc_2F4F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_3012',
    )

    ChrTalk(
        0x0008,
        (
            '#0580370755V#790F水泵的修理辛苦你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370756V虽然是平凡的小事，\n',
            '但对游击士来说却也是重要的任务哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370757V用心解决市民的每个困难，\n',
            '身为游击士，应该把这句话牢记在心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4214')

    def _loc_3012(): pass

    label('loc_3012')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_355F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0401, 7, 0x200F)),
            (Expr.TestScenaFlags, ScenaFlag(0x0401, 4, 0x200C)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_32BE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_324A',
    )

    ChrTalk(
        0x0008,
        (
            '#0580370758V#790F内燃引擎已经拿到了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370759V#1006F嗯，总算是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370760V#1040F顺利借到了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020370761V警备艇上的各位士兵\n',
            '好像也没有受伤。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580370762V#790F是吗，那可是好消息。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370763V要塞那边就由我来\n',
            '通知就可以了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370764V你们就继续去忙\n',
            '自己的工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370765V#1040F明白。',
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
        'loc_31B8',
    )

    ChrTalk(
        0x0107,
        (
            '#0070370766V#560F是、是的！\n',
            '那么～我们走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_321F')

    def _loc_31B8(): pass

    label('loc_31B8')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_31EC',
    )

    ChrTalk(
        0x0106,
        (
            '#0050370767V#051F嗯，我们走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_321F')

    def _loc_31EC(): pass

    label('loc_31EC')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_321F',
    )

    ChrTalk(
        0x0108,
        (
            '#0080370768V#070F嗯，那就走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_321F(): pass

    label('loc_321F')

    ChrTalk(
        0x0008,
        (
            '#0580370769V#790F一定要小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Jump('loc_32BB')

    def _loc_324A(): pass

    label('loc_324A')

    ChrTalk(
        0x0008,
        (
            '#0580370770V#790F警备艇的事情\n',
            '让我来报告给他们就可以了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370771V你们就继续去忙\n',
            '你们继续忙自己的事吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_32BB(): pass

    label('loc_32BB')

    Jump('loc_355C')

    def _loc_32BE(): pass

    label('loc_32BE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0401, 4, 0x200C)),
            Expr.Return,
        ),
        'loc_3359',
    )

    ChrTalk(
        0x0008,
        (
            '#0580370772V#790F听说内燃引擎被装载在迫降在\n',
            '托兰特平原的警备艇上。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370773V你们也只有去托兰特平原搜索一下，\n',
            '和他们的负责人交涉一下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_355C')

    def _loc_3359(): pass

    label('loc_3359')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 5, 0x2005)),
            Expr.Return,
        ),
        'loc_355C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 6, 0x2006)),
            Expr.Return,
        ),
        'loc_33E7',
    )

    ChrTalk(
        0x0008,
        (
            '#0580370774V#790F从刚才的联络来看，\n',
            '似乎不用马上就出发。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370775V如果你们以后正好路过王都的话\n',
            '顺便去看看就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_355C')

    def _loc_33E7(): pass

    label('loc_33E7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_34C8',
    )

    ChrTalk(
        0x0008,
        (
            '#0580370776V#790F因为在雷斯顿要塞附近，\n',
            '所以治安方面应该不成问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370777V就检查一下告示板，\n',
            '之后确认一下中央工房和\n',
            '亚尔摩温泉的状况就可以了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370778V现在联系困难，\n',
            '也许会遇到什么麻烦也说不定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Jump('loc_355C')

    def _loc_34C8(): pass

    label('loc_34C8')

    ChrTalk(
        0x0008,
        (
            '#0580370779V#790F就检查一下告示板，\n',
            '之后确认一下中央工房和\n',
            '亚尔摩温泉的状况就可以了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370778V现在联系困难，\n',
            '也许会遇到什么麻烦也说不定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_355C(): pass

    label('loc_355C')

    Jump('loc_4214')

    def _loc_355F(): pass

    label('loc_355F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_3B5D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_35E1',
    )

    ChrTalk(
        0x0008,
        (
            '#0580240136V#790F有关古代遗物，\n',
            '目前还有很多未解之处。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580240137V希望从这次的发现中\n',
            '可以找到什么线索……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3B5A')

    def _loc_35E1(): pass

    label('loc_35E1')

    If(
        (
            (Expr.Eval, "OP_29(0x006C, 0x01, 0x4000)"),
            (Expr.Eval, "OP_29(0x006C, 0x00, 0x04)"),
            (Expr.Eval, "OP_29(0x006C, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x006C, 0x00, 0x40)"),
            Expr.Nez64,
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_36FE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_3698',
    )

    ChrTalk(
        0x0008,
        (
            '#0580240138V#790F今后他们很有可能\n',
            '会再次出现，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580240139V即使到了王都也要小心行动啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580231329V愿女神保佑诸位。\n',
            '请一路小心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_36FB')

    def _loc_3698(): pass

    label('loc_3698')

    ChrTalk(
        0x0008,
        (
            '#0580240141V#790F王都的艾南先生\n',
            '就由我来联络吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580231329V愿女神保佑诸位。\n',
            '请一路小心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_36FB(): pass

    label('loc_36FB')

    Jump('loc_3B5A')

    def _loc_36FE(): pass

    label('loc_36FE')

    ChrTalk(
        0x0008,
        (
            '#0580240143V#792F说起来的话，已经注意到了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580240144V协会的招牌板……\n',
            '已经顺利找回了呢。',
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
            '#0010240145V#1004F那块招牌板已经找到了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#0580240146V#790F是中央工房的菲小姐\n',
            '帮忙找到的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580240147V不知是怎么回事，\n',
            '竟然被人运送到了地下仓库',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240148V#1020F地、地下仓库～！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240149V#1007F为什么会在那里……\n',
            '这、有什么缘由吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_38F7',
    )

    ChrTalk(
        0x0106,
        (
            '#0050240150V#551F大概是那家伙干的吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050240151V虽然不知道他是怎么做到的，\n',
            '但手段真是很厉害啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_394F')

    def _loc_38F7(): pass

    label('loc_38F7')

    ChrTalk(
        0x0103,
        (
            '#0030240152V#025F嗯嗯，肯定是那个人\n',
            '干的好事吧，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030240153V真是个不得了的家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_394F(): pass

    label('loc_394F')

    ChrTalk(
        0x0008,
        (
            '#0580240154V#792F事情就是这样，\n',
            '所以那个委托也就撤消了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580240155V没有凭自己的实力夺回来，\n',
            '总觉得有些遗憾呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580240138V#790F今后他们很有可能\n',
            '会再次出现，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580240157V即使到了王都也要小心行动啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3A5C',
    )

    ChrTalk(
        0x0104,
        (
            '#0040240158V#030F呼，这样也不错啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3AB4')

    def _loc_3A5C(): pass

    label('loc_3A5C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3A8E',
    )

    ChrTalk(
        0x0107,
        (
            '#0070240159V#062F是、是的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3AB4')

    def _loc_3A8E(): pass

    label('loc_3A8E')

    ChrTalk(
        0x0101,
        (
            '#0010240160V#1002F嗯……明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3AB4(): pass

    label('loc_3AB4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3AE5',
    )

    ChrTalk(
        0x0106,
        (
            '#0050240161V#050F啊啊，会小心的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3B08')

    def _loc_3AE5(): pass

    label('loc_3AE5')

    ChrTalk(
        0x0103,
        (
            '#0030240162V#020F嗯，了解啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3B08(): pass

    label('loc_3B08')

    ChrTalk(
        0x0008,
        (
            '#0580240163V#790F那么，愿女神守护诸位。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580240164V请一路小心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    OP_28(0x006C, 0x01, 0x4000)

    def _loc_3B5A(): pass

    label('loc_3B5A')

    Jump('loc_4214')

    def _loc_3B5D(): pass

    label('loc_3B5D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_3BF6',
    )

    ChrTalk(
        0x0008,
        (
            '#0580231359V#790F那么，招牌板的搜查工作\n',
            '也就一起交给你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580231360V并不是什么太紧急的任务，和地震的调查\n',
            '相比起来就显得无关紧要了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4214')

    def _loc_3BF6(): pass

    label('loc_3BF6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_3E19',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_3C6F',
    )

    ChrTalk(
        0x0008,
        (
            '#0580231348V#790F竟然敢对雷斯顿要塞下手，\n',
            '看来对手不是等闲之辈。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580231349V你们一定不能大意啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E16')

    def _loc_3C6F(): pass

    label('loc_3C6F')

    ChrTalk(
        0x0008,
        (
            '#0580231343V#790F我听说了，\n',
            '你们要去亚尔摩村对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010231344V#1016F啊，消息还是那么灵通～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580231345V#790F海泽尔和我联系过了哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580231346V竟然敢对雷斯顿要塞下手，\n',
            '看来对手不是等闲之辈。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580231347V……一定不要大意啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3D8E',
    )

    ChrTalk(
        0x0106,
        (
            '#0050231350V#050F哈，那当然。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3DB3')

    def _loc_3D8E(): pass

    label('loc_3D8E')

    ChrTalk(
        0x0103,
        (
            '#0030231351V#022F嗯嗯～明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3DB3(): pass

    label('loc_3DB3')

    ChrTalk(
        0x0008,
        (
            '#0580231352V#790F嗯，那就不用多说了。\n',
            '好了，快去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010231353V#1002F嗯，我们走了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_3E16(): pass

    label('loc_3E16')

    Jump('loc_4214')

    def _loc_3E19(): pass

    label('loc_3E19')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 1, 0x1419)),
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 3, 0x141B)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 7, 0x141F)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3E9E',
    )

    ChrTalk(
        0x0008,
        (
            '#0580231363V#790F测量仪已经设置完毕的话，\n',
            '接下来就请去中央工房吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580231364V我想博士应该在５层的\n',
            '演算室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4214')

    def _loc_3E9E(): pass

    label('loc_3E9E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_3F3E',
    )

    ChrTalk(
        0x0008,
        (
            '#0580231361V#790F测量仪的设置场所是\n',
            '隧道中部、平原北部外围、\n',
            '雷斯顿要塞前三个地方。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580231362V必要的联络已经做过了，\n',
            '请你们直接去现场调查吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4214')

    def _loc_3F3E(): pass

    label('loc_3F3E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_408F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_3FC4',
    )

    ChrTalk(
        0x0008,
        (
            '#0580231354V#790F地震的调查\n',
            '并不是紧急性的工作哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580231355V一边完成告示板上的委托\n',
            '一边抽空进行调查就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_408C')

    def _loc_3FC4(): pass

    label('loc_3FC4')

    ChrTalk(
        0x0008,
        (
            '#0580231337V#790F你们先去沃尔费堡垒\n',
            '进行调查吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580231338V蔡斯市内的情报收集工作\n',
            '已经拜托过工房长先生了。\n',
            '即使不去管也没关系。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580231355V一边完成告示板上的委托\n',
            '一边抽空进行调查就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_408C(): pass

    label('loc_408C')

    Jump('loc_4214')

    def _loc_408F(): pass

    label('loc_408F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 0, 0x1408)),
            Expr.Return,
        ),
        'loc_4214',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_411B',
    )

    ChrTalk(
        0x0008,
        (
            '#0580231341V#790F地震的调查工作并不是很急，\n',
            '慢慢进行也没关系的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580231340V先去拉赛尔工房\n',
            '和博士他们打个招呼如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4214')

    def _loc_411B(): pass

    label('loc_411B')

    ChrTalk(
        0x0008,
        (
            '#0580231337V#790F你们先去沃尔费堡垒\n',
            '进行调查吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580231338V蔡斯市内的情报收集工作\n',
            '已经拜托过工房长先生了。\n',
            '即使不去管也没关系。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580231339V一边完成告示板上的委托\n',
            '慢慢进行也没关系哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580231340V先去拉赛尔工房\n',
            '和博士他们打个招呼如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_4214(): pass

    label('loc_4214')

    TalkEnd(0x0008)

    Return()

# id: 0x000B offset: 0x4218
@scena.Code('func_0B_4218')
def func_0B_4218():
    TalkBegin(0x0016)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AF, 4, 0x57C)),
            Expr.Return,
        ),
        'loc_4225',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    def _loc_4225(): pass

    label('loc_4225')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_429B',
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
            TXT(0x00, '【◇在前作中与王相识】\n'),
            TXT(0x01, '【◇在前作中不认识王】\n'),
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
        (0x00000000, 'loc_428F'),
        (0x00000001, 'loc_4295'),
        (-1, 'loc_429B'),
    )

    def _loc_428F(): pass

    label('loc_428F')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    Jump('loc_429B')

    def _loc_4295(): pass

    label('loc_4295')

    ClearScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    Jump('loc_429B')

    def _loc_429B(): pass

    label('loc_429B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 7, 0x1427)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_44FD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_44B8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_438D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_4311',
    )

    ChrTalk(
        0x00FE,
        (
            '冈多夫好像\n',
            '马上就要回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这种人手不足的情况\n',
            '究竟要持续到什么时候呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_438A')

    def _loc_4311(): pass

    label('loc_4311')

    ChrTalk(
        0x00FE,
        (
            '前去王都的冈多夫\n',
            '马上就要回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '终于快要卸下担子了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过这里的人手不足问题\n',
            '究竟要持续到什么时候呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    def _loc_438A(): pass

    label('loc_438A')

    Jump('loc_44B5')

    def _loc_438D(): pass

    label('loc_438D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_4448',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_43EE',
    )

    ChrTalk(
        0x00FE,
        (
            '等修好之后\n',
            '还要继续进行护卫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '导力器的输出工作\n',
            '还是和以前一样顺利啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4445')

    def _loc_43EE(): pass

    label('loc_43EE')

    ChrTalk(
        0x00FE,
        (
            '等修好之后\n',
            '还要继续进行护卫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近出现了很多危险的魔兽，\n',
            '也真是伤脑筋呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    def _loc_4445(): pass

    label('loc_4445')

    Jump('loc_44B5')

    def _loc_4448(): pass

    label('loc_4448')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 0, 0x1408)),
            Expr.Return,
        ),
        'loc_44B5',
    )

    ChrTalk(
        0x00FE,
        (
            '可能的话，我也想\n',
            '自己挑选工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以后你们要是接到什么重要调查的话\n',
            '也分配一些简单任务给我吧，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_44B5(): pass

    label('loc_44B5')

    Jump('loc_44FA')

    def _loc_44B8(): pass

    label('loc_44B8')

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '不好意思，\n',
            '很想帮到你们一些忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家一起加油吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_44FA(): pass

    label('loc_44FA')

    Jump('loc_4A4C')

    def _loc_44FD(): pass

    label('loc_44FD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_46BC',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4609',
    )

    ChrTalk(
        0x00FE,
        (
            '呀，好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还记得我吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1001F当然记得啦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '你不是蔡斯支部\n',
            '的王吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈，谢谢，竟然还记得我。\n',
            '能再次相遇真是高兴啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你终于顺利晋升为\n',
            '正游击士了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '恭喜！\n',
            '凭你的实力，这也是理所当然的结果。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_46B9')

    def _loc_4609(): pass

    label('loc_4609')

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '啊，这不是艾丝蒂尔吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1004F咦……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1018F啊，我还说是谁，\n',
            '这不是王吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你终于顺利晋升为\n',
            '正游击士了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '恭喜！\n',
            '凭你的实力，这也是理所当然的结果。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_46B9(): pass

    label('loc_46B9')

    Jump('loc_4804')

    def _loc_46BC(): pass

    label('loc_46BC')

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '…………哎呀？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你不就是…\n',
            '最近才转正的艾丝蒂尔吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1004F哎哎，是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，失礼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我是王。\n',
            '蔡斯地区的游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F啊～是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我是艾丝蒂尔·布莱特。\n',
            '麻烦您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊，请多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们的事情\n',
            '我也早有耳闻了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是立了大功啊，\n',
            '升为正游击士也是理所当然的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_4804(): pass

    label('loc_4804')

    ChrTalk(
        0x0101,
        (
            '#1008F嘿嘿，谢谢夸奖。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我们也还差得远呢，\n',
            '还需要不断努力进步。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯…保持上进心，永不懈怠吗…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这种谦虚的态度\n',
            '我也要多多学习。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对了，冈多夫\n',
            '出去办事了，你们知道吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011F啊，嗯。\n',
            '从嘉恩那里听说了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我们就是为了增援\n',
            '才特意来蔡斯的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是这样吗。\n',
            '谢啦，真是帮了大忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是不好意思，\n',
            '很想帮到你们一些忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_49B8',
    )

    ChrTurnDirection(0x00FE, 0x0106, 400)

    ChrTalk(
        0x00FE,
        (
            '阿加特前辈也一样……\n',
            '就请你们多多关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#051F哪里，也请你们多关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4A0F')

    def _loc_49B8(): pass

    label('loc_49B8')

    ChrTurnDirection(0x00FE, 0x0103, 400)

    ChrTalk(
        0x00FE,
        (
            '雪拉扎德前辈也一样，\n',
            '就请你们多多关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F哪里的话，互相关照吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4A0F(): pass

    label('loc_4A0F')

    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '我也竭尽全力哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，大家都加油吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0284, 7, 0x1427))
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))
    def _loc_4A4C(): pass

    label('loc_4A4C')

    TalkEnd(0x0016)

    Return()

# id: 0x000C offset: 0x4A50
@scena.Code('func_0C_4A50')
def func_0C_4A50():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_4B12',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4ACC',
    )

    ChrTalk(
        0x00FE,
        (
            '好久没看见这个了，\n',
            '油灯其实也不错啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然亮度不能和\n',
            '导力灯相比……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是却很温暖呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    Jump('loc_4B0F')

    def _loc_4ACC(): pass

    label('loc_4ACC')

    ChrTalk(
        0x00FE,
        (
            '好久没看见这个了，\n',
            '油灯其实也不错啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '让人感觉很温暖呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4B0F(): pass

    label('loc_4B0F')

    Jump('loc_4BFB')

    def _loc_4B12(): pass

    label('loc_4B12')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_4BFB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4BB3',
    )

    ChrTalk(
        0x00FE,
        (
            '今天是为了购买油灯\n',
            '不过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '买这种东西果然\n',
            '简单多了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '买水果和面包的时候\n',
            '总是给我提『买看起来好吃的』\n',
            '这种含糊不清的要求。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    Jump('loc_4BFB')

    def _loc_4BB3(): pass

    label('loc_4BB3')

    ChrTalk(
        0x00FE,
        (
            '今天是为了购买油灯\n',
            '而过来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '果然还是买工业制品\n',
            '简单多了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4BFB(): pass

    label('loc_4BFB')

    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x4BFF
@scena.Code('func_0D_4BFF')
def func_0D_4BFF():
    EventBegin(0x00)
    MapClearFlags(0x02000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4C1B',
    )

    Call(0, 0x001B)
    Call(0, 0x001C)

    def _loc_4C1B(): pass

    label('loc_4C1B')

    OP_4A(0x0008, 255)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4C33',
    )

    FormationAddMember(ChrTable['科洛丝'], 0xFA, 0xFF)

    Jump('loc_4C37')

    def _loc_4C33(): pass

    label('loc_4C33')

    FormationAddMember(ChrTable['奥利维尔'], 0xFA, 0xFF)

    def _loc_4C37(): pass

    label('loc_4C37')

    CameraMove(2340, 0, -5820, 0)
    OP_67(0, 9000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, 3120, 0, -700, 0)
    ChrSetPos(0x0101, 4170, 0, -700, 315)
    ChrSetPos(0x0104, 2450, 0, -1620, 0)
    ChrSetPos(0x00F7, 3600, 0, -1920, 0)
    ChrSetPos(0x0105, 4720, 0, -1960, 0)
    ChrSetPos(0x0107, 4190, 0, -3140, 0)
    ChrSetPos(0x0009, 3140, 0, -2970, 0)
    ChrSetPos(0x0010, 2029, 0, -2710, 0)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_4D1A')
    def lambda_4D1A():
        CameraMove(2660, 0, -300, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4D1A)

    @scena.Lambda('lambda_4D32')
    def lambda_4D32():
        OP_67(0, 8000, -10000, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4D32)

    OP_0D()
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0580231146V#792F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580231147V那个戴墨镜的男人\n',
            '果然就是瓦鲁特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0080231148V#073F#6P啊啊──哎？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080231149V难道你早就\n',
            '已经猜到了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580231150V#791F嗯，听过服装和体型的描述后\n',
            '我就基本确定是他了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580231151V#792F你这次还是太大意了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580231152V怎么可以就这样任由他\n',
            '把『福音』带走？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0080231153V#075F#6P没办法……\n',
            '我也没想到那东西\n',
            '会这么重要啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080231154V#072F而且连事情经过都不说\n',
            '就直接催我快去亚尔摩村\n',
            '的人不正是你吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580231155V#791F嗯，这也算是我的判断失误。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580231156V本以为这种状况就算不做说明\n',
            '你自己也能判断清楚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0080231157V#075F#6P呼……你还是这么不可爱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580231158V#792F不管怎么说，\n',
            '地震的调查总算是解决了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580231159V#790F把调查的报酬\n',
            '给你们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0085, 0x00, 0x20)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5052',
    )

    OP_AF(0x9A, 0x0085)
    Sleep(100)

    OP_28(0x0086, 0x04, 0x10)
    OP_28(0x0086, 0x04, 0x20)
    OP_28(0x0087, 0x04, 0x10)
    OP_28(0x0087, 0x04, 0x20)

    def _loc_5052(): pass

    label('loc_5052')

    OP_28(0x0088, 0x04, 0x10)
    OP_AF(0x9A, 0x0088)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ChrTalk(
        0x0101,
        (
            '#0010231160V#1006F#6P谢谢雾香姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010231161V#1015F不过…你们和那个墨镜男\n',
            '在以前就认识的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0011, 0x0101, 400)

    ChrTalk(
        0x0011,
        (
            '#0080231162V#074F#5P嗯，这个啊…\n',
            '要怎么说才好呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580231163V#791F简单的说，\n',
            '我和金，还有瓦鲁特…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580231164V曾经都是同门修行的弟子……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580231165V其中他最年长，\n',
            '也就是大师兄。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_51E1',
    )

    ChrTalk(
        0x0106,
        (
            '#0050231166V#052F#6P同门师兄弟啊……\n',
            '也就是武术上的前辈吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5224')

    def _loc_51E1(): pass

    label('loc_51E1')

    ChrTalk(
        0x0103,
        (
            '#0030231167V#023F#6P同门师兄弟……\n',
            '那也就是武术上的前辈了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5224(): pass

    label('loc_5224')

    ChrSetDirection(0x0011, 135, 400)

    ChrTalk(
        0x0011,
        (
            '#0080231168V#070F#5P嗯，正确的说，\n',
            '雾香她并不是弟子，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080231169V而是龙牙师傅的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580231170V#792F我的事情就没必要提了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580231171V#790F总之那个男人曾经是\n',
            '『泰斗流』门下的弟子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580231172V在6年前离开道场后\n',
            '就被『噬身之蛇』看中。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580231173V#792F之后就加入了那个组织。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0080231174V#572F#5P雾香……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_541C',
    )

    ChrTalk(
        0x0106,
        (
            '#0050231175V#053F#6P说到这里我就完全明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050231176V#552F话说回来，他使用的武术好像是\n',
            '和你们一样的『泰斗流』功夫啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050231177V强得简直像个妖怪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_54BC')

    def _loc_541C(): pass

    label('loc_541C')

    ChrTalk(
        0x0103,
        (
            '#0030231178V#026F#6P说到这里我就完全明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030231179V#020F话说回来，他好像和你们一样，\n',
            '用的也是『泰斗流』的武术……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030231180V真是好厉害的功夫啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_54BC(): pass

    label('loc_54BC')

    ChrTalk(
        0x0011,
        (
            '#0080231181V#074F#5P他的身手比在道场时\n',
            '又精进了很多。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080231182V#072F可以说是达人级别的武者了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580231183V#792F确实是个非常危险的男人啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580231184V#791F不过现在看来，再发生地震\n',
            '的可能性应该已经很低了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580231185V稍微放松一下警备也无所谓了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0550231186V#801F#6P啊啊，说的对。\n',
            '我这就去通知市民和职员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0540231187V#104F#6P不过，他们再次使用了\n',
            '『福音』啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540231188V而且还连同让七耀脉活性化的\n',
            '装置一起使用……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_567E')
    def lambda_567E():
        CameraMove(2660, 0, -1300, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_567E)

    @scena.Lambda('lambda_5696')
    def lambda_5696():
        ChrSetDirection(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_5696)

    @scena.Lambda('lambda_56A4')
    def lambda_56A4():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_56A4)

    Sleep(50)

    @scena.Lambda('lambda_56B7')
    def lambda_56B7():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_56B7)

    @scena.Lambda('lambda_56C5')
    def lambda_56C5():
        ChrSetDirection(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_56C5)

    Sleep(50)

    @scena.Lambda('lambda_56D8')
    def lambda_56D8():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_56D8)

    @scena.Lambda('lambda_56E6')
    def lambda_56E6():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_56E6)

    Sleep(50)

    @scena.Lambda('lambda_56F9')
    def lambda_56F9():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_56F9)

    Sleep(300)

    WaitForThreadExit(0x0101, 0x0002)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_58B5',
    )

    ChrTalk(
        0x0104,
        (
            '#0040231189V#030F#5P联系学院地下的投影\n',
            '装置一起分析的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040231190V看来他们已经得到了可以大幅度提高\n',
            '导力器性能的技术了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0540231191V#102F#6P嗯……确实如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540231192V空间投影装置也好，\n',
            '七耀脉的活性化装置也好，\n',
            '都不是绝对无法实现的技术。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540231193V但加上『福音』的影响后就可以产生\n',
            '以当今的导力技术无法解释的现象。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540231194V不仅是我，其他任何一家\n',
            '技术工房恐怕也都不能解释这些现象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5A4F')

    def _loc_58B5(): pass

    label('loc_58B5')

    ChrTalk(
        0x0105,
        (
            '#0060231195V#042F#2P连同学院地下的投影装置\n',
            '一起分析的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060231196V看来他们已经得到了可以大幅度提高\n',
            '导力器性能的技术了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0540231197V#102F#6P嗯……应该没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540231192V空间投影装置也好，\n',
            '七耀脉的活性化装置也好，\n',
            '都不是绝对无法实现的技术。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540231193V但加上『福音』的影响后就可以产生\n',
            '以当今的导力技术无法解释的现象。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540231200V不仅是我，其它任何一家\n',
            '技术工房恐怕也都不能解释这些现象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5A4F(): pass

    label('loc_5A4F')

    ChrTalk(
        0x0010,
        (
            '#0550231201V#803F#5P是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550231202V共和国的乌尔努社，\n',
            '帝国的莱恩福尔特社……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550231203V#800F甚至是研发了战术导力器的\n',
            '爱普斯泰恩财团也都无法做到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010231204V#1002F#2P这么说的话…结社的\n',
            '技术力实在是太惊人了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0540231205V#100F#6P嗯，大概他们之中\n',
            '有个这方面的天才吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540231206V#101F嗯嗯……\n',
            '我也不能输给他们啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070231207V#065F#6P爷、爷爷……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0550231208V#803F#5P呼，真没办法……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550231209V#800F新型引擎总算\n',
            '也完工了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550231210V中央工房今后就将解析『福音』\n',
            '作为最优先的工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0540231211V#101F#6P哇哈哈，那当然。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010231212V#1006F#2P确实，如果能参透『福音』\n',
            '的奥秘的话就帮大忙了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010231213V不知道他们今后还会以怎样的\n',
            '方式来使用『福音』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_5D95',
    )

    ChrTalk(
        0x0106,
        (
            '#0050231214V#053F#5P而且那些家伙都在说\n',
            '什么『实验』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050231215V#050F既然有２次的话，再出现第３次也不奇怪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5E03')

    def _loc_5D95(): pass

    label('loc_5D95')

    ChrTalk(
        0x0103,
        (
            '#0030231216V#026F#5P而且那些家伙都在说\n',
            '什么『实验』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030231217V#022F有２次的话，就难保不会有第３次。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5E03(): pass

    label('loc_5E03')

    ChrTalk(
        0x0008,
        (
            '#0580231218V#792F『福音』的分析工作\n',
            '就拜托博士他们了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580231219V#790F而你们也差不多该\n',
            '向下一个地方进发了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5E81')
    def lambda_5E81():
        CameraMove(2660, 0, -300, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_5E81)

    @scena.Lambda('lambda_5E99')
    def lambda_5E99():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_5E99)

    @scena.Lambda('lambda_5EA7')
    def lambda_5EA7():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5EA7)

    Sleep(50)

    @scena.Lambda('lambda_5EBA')
    def lambda_5EBA():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_5EBA)

    @scena.Lambda('lambda_5EC8')
    def lambda_5EC8():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_5EC8)

    Sleep(50)

    @scena.Lambda('lambda_5EDB')
    def lambda_5EDB():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_5EDB)

    @scena.Lambda('lambda_5EE9')
    def lambda_5EE9():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_5EE9)

    Sleep(50)

    @scena.Lambda('lambda_5EFC')
    def lambda_5EFC():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_5EFC)

    Sleep(500)

    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010231220V#1006F#6P嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010231221V虽然没有抓到犯人，\n',
            '但总算把地震的事情解决了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010231222V接下来我们要去哪里好呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580231223V#791F王都支部正好刚发来了\n',
            '支援请求。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580231224V王国军\n',
            '好像有什么正式的委托啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010231225V#1004F#6P王国军……\n',
            '难道是老爸的委托吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580231226V#791F详情我也不清楚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580231227V不过那边还特意指名\n',
            '让你们去，\n',
            '大概是和结社有关的事情吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010231228V#1015F#6P确实如此啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_6104',
    )

    ChrTalk(
        0x0106,
        (
            '#0050231229V#051F#6P嘿……\n',
            '那就过去看看好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_613F')

    def _loc_6104(): pass

    label('loc_6104')

    ChrTalk(
        0x0103,
        (
            '#0030231230V#027F#6P呵呵……\n',
            '那就只有先过去看看了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_613F(): pass

    label('loc_613F')

    ChrSetDirection(0x0011, 135, 400)

    ChrTalk(
        0x0011,
        (
            '#0080231231V#071F#5P好，那就这么决定了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080231232V把蔡斯的事情全做完以后\n',
            '就乘坐定期船去王都吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010231233V#1001F ＯＫ……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010231234V#1004F啊，难道\n',
            '金先生也要和我们一起行动吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0080231235V#070F#5P喂～那是当然的啊，不然你以为\n',
            '我是为了什么才会特意赶回来的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080231236V瓦鲁特的事情我不能坐视不管，\n',
            '而且你不是还在寻找约修亚吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080231237V我当然要尽力帮忙的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010231238V#1017F金先生……谢谢你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_6450',
    )

    ChrTalk(
        0x0106,
        (
            '#0050231239V#053F#6P说心里话，你能\n',
            '帮忙实在是太好了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050231240V#050F我这次算是彻底\n',
            '惨败给那个戴墨镜的混蛋了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050231241V可以的话请你指点我几招吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0080231242V#071F#5P哈哈，你这么说话未免\n',
            '太谦虚了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080231243V#070F原来的豪气跑到哪里去了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050231244V#552F#6P哼，我早已不是连你的\n',
            '实力都不清楚的呆小子了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6598')

    def _loc_6450(): pass

    label('loc_6450')

    ChrTalk(
        0x0103,
        (
            '#0030231245V#021F#6P呵呵，金先生一个人\n',
            '可是比一百个人还要可靠的强援啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030231246V#027F我这次算是彻底\n',
            '被那个戴墨镜的男人打败了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030231247V可以的话请你来指教我一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0080231248V#070F#5P嗯，这个没问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080231249V那家伙的招式比较特殊，\n',
            '到时我把应对方法告诉你吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030231250V#021F#6P嗯，那就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6598(): pass

    label('loc_6598')

    OP_62(0x0107, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1000)

    OP_63(0x0107)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_6862',
    )

    ChrTalk(
        0x0107,
        (
            '#0070231251V#062F#6P姐姐，阿加特哥哥。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070231252V我也……\n',
            '我也和你们一起去可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x00F7, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_664D')
    def lambda_664D():
        CameraMove(2660, 0, -1300, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_664D)

    @scena.Lambda('lambda_6665')
    def lambda_6665():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_6665)

    @scena.Lambda('lambda_6673')
    def lambda_6673():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6673)

    Sleep(50)

    @scena.Lambda('lambda_6686')
    def lambda_6686():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_6686)

    @scena.Lambda('lambda_6694')
    def lambda_6694():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_6694)

    Sleep(50)

    @scena.Lambda('lambda_66A7')
    def lambda_66A7():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_66A7)

    @scena.Lambda('lambda_66B5')
    def lambda_66B5():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_66B5)

    Sleep(50)

    @scena.Lambda('lambda_66C8')
    def lambda_66C8():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_66C8)

    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010231253V#1004F#2P哎……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050231254V#055F#5P什、什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070231255V#561F#6P嗯…我想他们以后也许还会\n',
            '继续使用『福音』之类的\n',
            '奇怪装置。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070231256V到了那个时候…\n',
            '我应该可以帮上一点忙……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070231257V#062F所以…请你们带上我吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010231258V#1003F#2P可、可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050231259V#053F#5P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0106, 180, 400)
    Sleep(300)

    ChrTalk(
        0x0106,
        (
            '#0050231260V#050F#5P老爷子的意见如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6AFC')

    def _loc_6862(): pass

    label('loc_6862')

    ChrTalk(
        0x0107,
        (
            '#0070231261V#062F#6P艾丝蒂尔姐姐、雪拉姐姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070231252V我也……\n',
            '我也和你们一起去可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x00F7, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_68FC')
    def lambda_68FC():
        CameraMove(2660, 0, -1300, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_68FC)

    @scena.Lambda('lambda_6914')
    def lambda_6914():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_6914)

    @scena.Lambda('lambda_6922')
    def lambda_6922():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6922)

    Sleep(50)

    @scena.Lambda('lambda_6935')
    def lambda_6935():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_6935)

    @scena.Lambda('lambda_6943')
    def lambda_6943():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_6943)

    Sleep(50)

    @scena.Lambda('lambda_6956')
    def lambda_6956():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_6956)

    @scena.Lambda('lambda_6964')
    def lambda_6964():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_6964)

    Sleep(50)

    @scena.Lambda('lambda_6977')
    def lambda_6977():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_6977)

    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010231253V#1004F#2P哎……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030190499V#023F#5P哎呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070231255V#561F#6P嗯…我想他们以后也许还会\n',
            '继续使用『福音』之类的\n',
            '奇怪装置。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070231256V到了那个时候…\n',
            '我应该可以帮上一点忙……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070231257V#062F所以…请你们带上我吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010231258V#1003F#2P可、可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030231269V#026F#5P嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0103, 180, 400)
    Sleep(300)

    ChrTalk(
        0x0103,
        (
            '#0030231270V#020F#5P博士的意见如何呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6AFC(): pass

    label('loc_6AFC')

    ChrTalk(
        0x0009,
        (
            '#0540231271V#104F#6P嗯…作为爷爷\n',
            '我自然是不愿意孙女去犯险……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540231272V#100F不过提妲这孩子也很顽固，\n',
            '还是尽量顺从她的心意比较好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540231273V所以呢，我就不反对了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0107, 270, 400)

    ChrTalk(
        0x0107,
        (
            '#0070231274V#560F#6P爷爷……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0540231275V#100F#6P结社拥有着超乎我们\n',
            '想象的技术力。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540231276V所以在今后的调查中\n',
            '提妲一定可以派得上用场，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540231277V#101F你们收下她肯定是不吃亏的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0550231278V#805F#5P真是的…这口气怎么像是\n',
            '在兜售新产品一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010231279V#1007F#2P嗯，有提妲的帮忙\n',
            '虽然很好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010231280V#1003F但如果以后再出现墨镜男子\n',
            '那样危险的家伙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_725B',
    )

    ChrTalk(
        0x0106,
        (
            '#0050231281V#552F#5P……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050231282V#053F不……这样也好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050231283V您的孙女，\n',
            '就先交给我照顾吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0107, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetDirection(0x0107, 315, 400)

    ChrTalk(
        0x0107,
        (
            '#0070231284V#064F#6P哎哎！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0540231285V#103F#6P喔哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010231286V#1004F#2P这、这到底是什么了！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010231287V本以为你一定会\n',
            '坚决反对的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050231288V#053F#5P单从地震事件就可以看出，\n',
            '『结社』的行为完全没有顾及到\n',
            '民间人士的生命安全。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050231289V这就意味着，不管在什么地方\n',
            '也都不能保证绝对的安全。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050231290V#051F所以还不如遵照她本人的意愿，\n',
            '顺便也还能帮我们一点忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070231291V#560F#6P阿加特哥哥……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0540231292V#100F#6P原来如此……\n',
            '这种想法倒也没有错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040231293V#035F#5P嘿嘿嘿～你是希望把她留在身边\n',
            '保护，不然放不下心吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040231294V#037F原来是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0106, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_62(0x0106, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrSetDirection(0x0106, 270, 600)

    ChrTalk(
        0x0106,
        (
            '#0050231295V#055F#4P什、什么啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010231296V#1006F#2P啊，好像脸红了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070231297V#560F#6P那个那个……\n',
            '那个…真的是这样吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0106, 135, 400)

    ChrTalk(
        0x0106,
        (
            '#0050231298V#551F#5P这种话你还要当真啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050231299V#555F事先听好！保护好自己\n',
            '是最基本的原则。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050231300V不要再一看到机械就不顾\n',
            '周围的情况了，明白了没有？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070231301V#067F#6P嘿嘿……我一定会小心的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0080231302V#071F#5P哈哈……\n',
            '能达成共识就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060231303V#048F哈哈，看来\n',
            '大家的意见统一了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_75AA')

    def _loc_725B(): pass

    label('loc_725B')

    ChrSetDirection(0x0105, 270, 400)
    Sleep(300)

    ChrTalk(
        0x0105,
        (
            '#0060231304V#043F#4P啊啊，话虽如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060231305V但从地震事件来看的话，\n',
            '『结社』的行为已经严重\n',
            '威胁到了民众的安全。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060231306V因此即使留在这里\n',
            '也未必可以保证完全没有危险。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010231307V#1004F#2P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0103, 90, 400)
    ChrSetDirection(0x0107, 0, 400)

    ChrTalk(
        0x0103,
        (
            '#0030231308V#027F#5P也许和我们一起行动\n',
            '反而会更安全一点……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030231309V那么说的话也没错啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060231310V#542F#4P是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070231311V#064F#6P科洛丝姐姐…雪拉姐姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010231312V#1007F#2P啊啊！！好了啦，我知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010231313V#1005F其实我不是也……\n',
            '不想和提妲分别吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070231314V#560F#6P艾丝蒂尔姐姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010231315V#1013F哎#2P、嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010231316V#1016F就是那样啦，\n',
            '以后多多关照啊，提妲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070231317V#067F#6P嗯！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0080231302V#071F#5P哈哈……\n',
            '能达成共识就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040231319V#031F#5P呵呵，看来大家\n',
            '已经统一意见了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_758A')
    def lambda_758A():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_758A)

    Sleep(50)

    @scena.Lambda('lambda_759D')
    def lambda_759D():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_759D)

    Sleep(50)

    def _loc_75AA(): pass

    label('loc_75AA')

    ChrSetDirection(0x0107, 270, 400)
    ChrSetDirection(0x0009, 90, 400)

    ChrTalk(
        0x0009,
        (
            '#0540231320V#100F#5P提妲啊，\n',
            '旅途中一定要多加小心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540231321V#101F在你努力的时候\n',
            '爷爷也会把『福音』之谜\n',
            '解明给你看的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070231322V#061F#6P嗯……那就等着您的好消息了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0550231323V#801F#5P博士就放心交给我吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550231324V我会好好监视他，\n',
            '避免引起什么事故的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070231325V#067F#6P嘿嘿……\n',
            '那就拜托您啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0540231326V#104F#5P真是的……\n',
            '不管到哪里都这么失礼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580231327V#792F呵呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_7760')
    def lambda_7760():
        CameraMove(2660, 0, -300, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_7760)

    @scena.Lambda('lambda_7778')
    def lambda_7778():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_7778)

    @scena.Lambda('lambda_7786')
    def lambda_7786():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_7786)

    Sleep(50)

    @scena.Lambda('lambda_7799')
    def lambda_7799():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_7799)

    @scena.Lambda('lambda_77A7')
    def lambda_77A7():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_77A7)

    Sleep(50)

    @scena.Lambda('lambda_77BA')
    def lambda_77BA():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_77BA)

    @scena.Lambda('lambda_77C8')
    def lambda_77C8():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_77C8)

    Sleep(50)

    @scena.Lambda('lambda_77DB')
    def lambda_77DB():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_77DB)

    @scena.Lambda('lambda_77E9')
    def lambda_77E9():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_77E9)

    Sleep(200)

    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0008,
        (
            '#0580231328V#791F王都的艾南那里\n',
            '就由我来联络吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580231329V愿女神保佑诸位。\n',
            '请一路小心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    RemoveItem(ItemTable['后山的钥匙'], 1)
    FadeOut(2000, 0, -1)
    OP_0D()

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7881',
    )

    FormationDelMember(0x04, 0xFF)

    Jump('loc_7884')

    def _loc_7881(): pass

    label('loc_7881')

    FormationDelMember(0x03, 0xFF)

    def _loc_7884(): pass

    label('loc_7884')

    Sleep(1000)

    OP_AD('ED6_DT24/C_VIS152._CH', 0x0000, 0x0000, 0x00000064)
    Sleep(4000)

    OP_56(0x02)
    SetScenaFlags(ScenaFlag(0x0290, 4, 0x1484))

    ExecExpressionWithVar(
        0x31,
        (
            (Expr.PushLong, 0x124),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(100000, -100000, 100000, 0)
    FadeIn(0, 0)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    UnlockAchievement(0x0F, 0x0000, 0x00)

    Menu(
        0,
        240,
        180,
        0,
        (
            TXT(0x00, '【保存进度】\n'),
            TXT(0x01, '【进入下一章】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_790A',
    )

    ShowSaveMenu()

    def _loc_790A(): pass

    label('loc_790A')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_AE(0x000000C8)
    OP_20(0x00000BB8)
    Sleep(2000)

    OP_21()
    ClearScenaFlags(ScenaFlag(0x0290, 4, 0x1484))

    ExecExpressionWithVar(
        0x04,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    NewScene('ED6_DT21/C3108._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000E offset: 0x7943
@scena.Code('func_0E_7943')
def func_0E_7943():
    EventBegin(0x00)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    CameraMove(4430, 0, 3750, 0)
    OP_67(0, 4980, -10000, 0)
    CameraSetDistance(2920, 0)
    OP_6C(327000, 0)
    OP_6E(272, 0)
    ChrSetPos(0x0008, 5380, 0, 2500, 270)
    OP_4A(0x0008, 255)
    LoadEffect(0x00, 'map\\\\mp001_01.eff')
    PlayEffect(0x00, 0x00, 0x00FF, 4840, 2000, 2560, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0580340962V#792F……原来如此。\n',
            '大致状况我已经明白了',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580340963V#791F军队的守备队\n',
            '之前也已经开始行动了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580340964V现在的战况已经基本稳定，\n',
            '不需要协会的援助了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580340965V#790F…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580340966V#792F……是吗，接下来\n',
            '要去的是『红莲之塔』吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580340967V#791F明白了……祝大家好运。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    PlaySE(131, 0x00, 0x64)
    StopEffect(0x00, 0x00)
    Sleep(1000)

    OP_62(0x0008, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1500)

    OP_63(0x0008)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0580340968V#792F……还是和以前一样\n',
            '什么事都憋不住，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580340969V#791F真的是一点也没变啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 180, 400)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0580340970V#790F#5P好了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580340971V这样的话\n',
            '接下来我也有的忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    OP_20(0x000007D0)
    OP_21()
    SetScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/E0810._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000F offset: 0x7C4C
@scena.Code('func_0F_7C4C')
def func_0F_7C4C():
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
        'loc_7C63',
    )

    Call(0, 0x001B)
    Call(0, 0x001D)

    def _loc_7C63(): pass

    label('loc_7C63')

    ChrSetPos(0x0101, 770, 0, -6100, 0)
    ChrSetPos(0x0102, 770, 0, -6100, 0)
    ChrSetPos(0x00F8, 770, 0, -6100, 0)
    ChrSetPos(0x00F9, 770, 0, -6100, 0)
    OP_4A(0x0008, 255)
    ChrSetPos(0x0008, 3380, 0, 2350, 0)
    CameraMove(2880, 0, 2070, 0)
    OP_67(0, 5770, -10000, 0)
    CameraSetDistance(2400, 0)
    OP_6C(315000, 0)
    OP_6E(310, 0)
    FadeIn(1000, 0)
    OP_0D()
    PlaySE(6, 0x00, 0x64)
    Sleep(500)

    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 3, 0x2003)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 1, 0x2001)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7D6D',
    )

    ChrTalk(
        0x0008,
        (
            '#0580370114V#792F#5P哎呀……\n',
            '比我预想中来得要早啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7DE9')

    def _loc_7D6D(): pass

    label('loc_7D6D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 3, 0x2003)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 1, 0x2001)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7DB2',
    )

    ChrTalk(
        0x0008,
        (
            '#0580370116V#792F#5P呵……\n',
            '比我预想的慢了好多啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7DE9')

    def _loc_7DB2(): pass

    label('loc_7DB2')

    ChrTalk(
        0x0008,
        (
            '#0580370115V#792F#5P呵呵……\n',
            '你们来的正是时候啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7DE9(): pass

    label('loc_7DE9')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_802A',
    )

    ChrTalk(
        0x0108,
        (
            '#0080370117V#2P喔～你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    ChrSetPos(0x0101, 1770, 0, -6100, 0)
    ChrSetPos(0x0102, 1770, 0, -6100, 0)
    ChrSetPos(0x00F8, 1770, 0, -6100, 0)
    ChrSetPos(0x00F9, 1770, 0, -6100, 0)

    @scena.Lambda('lambda_7E65')
    def lambda_7E65():
        CameraMove(2800, 0, 750, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_7E65)

    @scena.Lambda('lambda_7E7D')
    def lambda_7E7D():
        OP_67(0, 6190, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_7E7D)

    @scena.Lambda('lambda_7E95')
    def lambda_7E95():
        CameraSetDistance(2500, 4000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_7E95)

    @scena.Lambda('lambda_7EA5')
    def lambda_7EA5():
        OP_6E(311, 4000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_7EA5)

    CreateThread(0x0101, 0x01, 0x00, func_10_9CD1)
    ChrSetDirection(0x0008, 180, 400)
    CreateThread(0x0102, 0x01, 0x00, func_11_9D01)

    @scena.Lambda('lambda_7ECA')
    def lambda_7ECA():
        ChrWalkTo(0x00FE, 3500, 0, 1200, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_7ECA)

    Sleep(500)

    CreateThread(0x00F8, 0x01, 0x00, func_12_9D31)
    Sleep(500)

    CreateThread(0x00F9, 0x01, 0x00, func_13_9D61)
    WaitForThreadExit(0x0108, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0108,
        (
            '#0080370118V#075F#6P为什么你知道\n',
            '我们会来？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580370119V#791F这次导力停止现象\n',
            '的原因就是那座浮游都市吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370120V如今一切导力设施都已经瘫痪，\n',
            '你们要想确认各地情况的话当然\n',
            '也就只能徒步巡视各地了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080370121V#072F#6P嗯嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370122V#1016F#6P啊哈哈，确实是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_826C')

    def _loc_802A(): pass

    label('loc_802A')

    ChrTalk(
        0x0101,
        (
            '#0010370123V#2P呵呵，不愧是雾香姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    ChrSetPos(0x0101, 1590, 0, -8119, 0)
    ChrSetPos(0x0102, 1590, 0, -8119, 0)
    ChrSetPos(0x00F8, 1590, 0, -8119, 0)
    ChrSetPos(0x00F9, 1590, 0, -8119, 0)

    @scena.Lambda('lambda_80A4')
    def lambda_80A4():
        CameraMove(2800, 0, 750, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_80A4)

    @scena.Lambda('lambda_80BC')
    def lambda_80BC():
        OP_67(0, 6190, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_80BC)

    @scena.Lambda('lambda_80D4')
    def lambda_80D4():
        CameraSetDistance(2500, 4000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_80D4)

    @scena.Lambda('lambda_80E4')
    def lambda_80E4():
        OP_6E(311, 4000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_80E4)

    CreateThread(0x0101, 0x01, 0x00, func_10_9CD1)
    ChrSetDirection(0x0008, 180, 400)
    CreateThread(0x0102, 0x01, 0x00, func_11_9D01)

    @scena.Lambda('lambda_8109')
    def lambda_8109():
        ChrWalkTo(0x00FE, 3500, 0, 1200, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_8109)

    Sleep(500)

    CreateThread(0x00F8, 0x01, 0x00, func_12_9D31)
    Sleep(500)

    CreateThread(0x00F9, 0x01, 0x00, func_13_9D61)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010370124V#1008F#6P你已经猜想到\n',
            '我们会来了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580370119V#791F这次导力停止现象\n',
            '的原因就是那座浮游都市吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370120V如今一切导力设施都已经瘫痪，\n',
            '你们要想确认各地情况的话当然\n',
            '也就只能徒步巡视各地了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370127V#1016F#6P原、原来如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370128V#1040F#6P确实是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_826C(): pass

    label('loc_826C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_82B0',
    )

    ChrTalk(
        0x0107,
        (
            '#0070370129V#067F#6P嘿嘿……\n',
            '不愧是雾香姐啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_833F')

    def _loc_82B0(): pass

    label('loc_82B0')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_82FA',
    )

    ChrTalk(
        0x0106,
        (
            '#0050370130V#051F#6P嘿……\n',
            '真是位可靠的女中豪杰啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_833F')

    def _loc_82FA(): pass

    label('loc_82FA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_833F',
    )

    ChrTalk(
        0x0103,
        (
            '#0030370131V#021F#6P呵呵……\n',
            '真是个可以靠的人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_833F(): pass

    label('loc_833F')

    ChrTalk(
        0x0008,
        (
            '#0580370132V#792F嗯，这里的情况\n',
            '正如你们想象中的一样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370133V#790F作为利贝尔王国\n',
            '最先进的导力都市，\n',
            '这里的混乱情况也是倍加严重。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370134V虽然玛多克工房长努力\n',
            '做了各种补救对策，\n',
            '但仍然无法平息市民们的不安。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370135V#1015F#6P这样啊……\n',
            '工房长现在怎么样了。',
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
        'loc_84A0',
    )

    ChrTalk(
        0x0107,
        (
            '#0070370136V#063F#6P要是我们可以\n',
            '帮的上他的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_84E2')

    def _loc_84A0(): pass

    label('loc_84A0')

    ChrTalk(
        0x0102,
        (
            '#0020370137V#1043F#6P要是有什么需要的话，\n',
            '我们可以去帮他……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_84E2(): pass

    label('loc_84E2')

    ChrTalk(
        0x0008,
        (
            '#0580370138V#792F嗯，有空的话就去\n',
            '顺便看看也好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370139V#790F另外……\n',
            '还有一个问题就是卡鲁迪亚隧道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370140V由于照明系统的消失，\n',
            '现在想从那里通行就变得十分困难。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_86AB',
    )

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
        0,
        (
            TXT(0x00, '【◇通过卡鲁迪亚隧道而来到蔡斯】\n'),
            TXT(0x01, '【◇曾进入过卡鲁迪亚隧道的艾尔·雷登一侧】\n'),
            TXT(0x02, '【◇曾进入过卡鲁迪亚隧道的蔡斯一侧】\n'),
            TXT(0x03, '【◇没有进入卡鲁迪亚隧道】\n'),
            TXT(0x04, '【◇不变更】\n'),
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
        (0x00000000, 'loc_8687'),
        (0x00000001, 'loc_8690'),
        (0x00000002, 'loc_8699'),
        (0x00000003, 'loc_86A2'),
        (-1, 'loc_86AB'),
    )

    def _loc_8687(): pass

    label('loc_8687')

    SetScenaFlags(ScenaFlag(0x0410, 1, 0x2081))
    SetScenaFlags(ScenaFlag(0x0410, 2, 0x2082))

    Jump('loc_86AB')

    def _loc_8690(): pass

    label('loc_8690')

    SetScenaFlags(ScenaFlag(0x0410, 1, 0x2081))
    ClearScenaFlags(ScenaFlag(0x0410, 2, 0x2082))

    Jump('loc_86AB')

    def _loc_8699(): pass

    label('loc_8699')

    ClearScenaFlags(ScenaFlag(0x0410, 1, 0x2081))
    SetScenaFlags(ScenaFlag(0x0410, 2, 0x2082))

    Jump('loc_86AB')

    def _loc_86A2(): pass

    label('loc_86A2')

    ClearScenaFlags(ScenaFlag(0x0410, 1, 0x2081))
    ClearScenaFlags(ScenaFlag(0x0410, 2, 0x2082))

    Jump('loc_86AB')

    def _loc_86AB(): pass

    label('loc_86AB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 1, 0x2081)),
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 2, 0x2082)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_8749',
    )

    ChrTalk(
        0x0101,
        (
            '#0010370141V#1007F#6P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010370142V我们就是通过那里\n',
            '来到蔡斯的，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370143V#1042F#6P那里的可视范围十分狭小，\n',
            '确实非常危险呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_884F')

    def _loc_8749(): pass

    label('loc_8749')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 1, 0x2081)),
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 2, 0x2082)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_87D5',
    )

    ChrTalk(
        0x0101,
        (
            '#0010370144V#1007F#6P嗯……\n',
            '我们也去那里看过了，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370145V#1042F#6P那里的可视范围十分狭小，\n',
            '状况确实非常危险呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_884F')

    def _loc_87D5(): pass

    label('loc_87D5')

    ChrTalk(
        0x0101,
        (
            '#0010370146V#1007F#6P那个地方确实不能\n',
            '没有照明系统啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370147V#1042F#6P如果失去了照明系统\n',
            '那就太危险了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_884F(): pass

    label('loc_884F')

    ChrTalk(
        0x0008,
        (
            '#0580370148V#792F还有啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370149V#790F听说亚尔摩村的水泵装置坏掉了，\n',
            '现在温泉已经不能使用了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301155V#1015F#6P这样啊……',
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
        'loc_891B',
    )

    ChrTalk(
        0x0107,
        (
            '#0070370151V#561F#6P那麻绪婆婆一定会\n',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_894F')

    def _loc_891B(): pass

    label('loc_891B')

    ChrTalk(
        0x0102,
        (
            '#0020370152V#1043F#6P那麻绪婆婆肯定\n',
            '很沮丧吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_894F(): pass

    label('loc_894F')

    ChrTalk(
        0x0008,
        (
            '#0580370153V#792F……大概吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370154V#790F那么也把你们的事情\n',
            '说给我听听吧，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370155V在『红莲之塔』分别以后\n',
            '到底发生了什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8A16',
    )

    ChrTalk(
        0x0108,
        (
            '#0080370156V#072F#6P啊啊，其实……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8A3F')

    def _loc_8A16(): pass

    label('loc_8A16')

    ChrTalk(
        0x0101,
        (
            '#0010370157V#1002F#6P嗯，其实呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8A3F(): pass

    label('loc_8A3F')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔告诉雾香\n',
            '『浮游都市』出现了的缘由以及\n',
            '说明了关于『零力场发生器』的情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#0580370158V#792F原来是这样。\n',
            '那个果然就是『辉之环』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370159V#790F在『四轮之塔』被他们占据时，\n',
            '这种事态就注定要发生了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8B7C',
    )

    ChrTalk(
        0x0108,
        (
            '#0080370160V#074F#6P啊啊……确实是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8BAB')

    def _loc_8B7C(): pass

    label('loc_8B7C')

    ChrTalk(
        0x0102,
        (
            '#0020370161V#1035F#6P是啊……确实是那样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8BAB(): pass

    label('loc_8BAB')

    ChrTalk(
        0x0101,
        (
            '#0010370162V#1003F#6P那么说的话\n',
            '我们费那么大力气到那四座塔里战斗\n',
            '根本就是毫无意义的嘛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010370163V#1007F真是气死人了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580370164V#792F已经过去的事情，\n',
            '再后悔也没有意义啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370165V#791F而且你们在塔内\n',
            '新发现的一些事情\n',
            '似乎也很有意义。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370166V现在最重要的是从中找出有用的信息\n',
            '留至以后活用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370167V#1025F#6P雾香姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580370168V#791F……那么你们就尽快\n',
            '把通讯器修好可以吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370169V这也是为了迎来光明的未来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8DD5',
    )

    ChrTalk(
        0x0108,
        (
            '#0080370170V#075F#6P啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080370171V#072F光顾着聊天，\n',
            '把正事都给忘了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8DD5(): pass

    label('loc_8DD5')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8F76',
    )

    ChrTalk(
        0x0101,
        (
            '#0010370172V#1016F#6P啊哈哈……明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0107, 400)

    ChrTalk(
        0x0101,
        (
            '#0010370173V#1006F#2P那么，提妲。\n',
            '这里就拜托你了哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0101, 400)

    ChrTalk(
        0x0107,
        (
            '#0070370174V#061F#6P嗯，交给我吧⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Call(1, 0x001B)
    ChrSetPos(0x0107, 5350, 0, 2490, 270)
    ChrSetDirection(0x0008, 90, 0)
    ChrSetDirection(0x0101, 0, 0)
    CameraMove(3430, 0, 2620, 0)
    OP_67(0, 6490, -10000, 0)
    CameraSetDistance(2300, 0)
    OP_6C(315000, 0)
    OP_6E(317, 0)
    Sleep(1000)

    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0107,
        (
            '#0070370175V#560F……嗯，这样就完成了。',
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
            '提妲打开了通讯器的开关。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    Jump('loc_90CE')

    def _loc_8F76(): pass

    label('loc_8F76')

    ChrTalk(
        0x0101,
        (
            '#0010370172V#1016F#6P啊哈哈……明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370177V#1040F#6P那我马上就开始\n',
            '设置『零力场发生器』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Call(1, 0x001B)
    ChrSetPos(0x0102, 5350, 0, 2490, 270)
    ChrSetDirection(0x0008, 90, 0)
    CameraMove(3430, 0, 2620, 0)
    OP_67(0, 6490, -10000, 0)
    CameraSetDistance(2300, 0)
    OP_6C(315000, 0)
    OP_6E(317, 0)
    Sleep(1000)

    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020370178V#1035F……这样就可以了。',
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
            '约修亚打开了通讯器的开关。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    def _loc_90CE(): pass

    label('loc_90CE')

    Sleep(500)

    PlaySE(157, 0x00, 0x64)
    Sleep(1000)

    PlaySE(131, 0x00, 0x64)
    LoadEffect(0x01, 'map\\\\mp001_01.eff')
    PlayEffect(0x01, 0x01, 0x00FF, 4840, 2000, 2560, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0580370179V#791F#5P……真不愧是拉赛尔博士。\n',
            '能发明出这么好的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(300)

    PlaySE(131, 0x00, 0x64)
    StopEffect(0x01, 0x00)
    Sleep(1000)

    @scena.Lambda('lambda_9191')
    def lambda_9191():
        CameraMove(2850, 0, 1670, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_9191)

    @scena.Lambda('lambda_91A9')
    def lambda_91A9():
        OP_67(0, 6270, -10000, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_91A9)

    @scena.Lambda('lambda_91C1')
    def lambda_91C1():
        OP_6E(325, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_91C1)

    @scena.Lambda('lambda_91D1')
    def lambda_91D1():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_91D1)

    Sleep(400)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_91F6',
    )

    ChrSetDirection(0x0107, 180, 400)

    Jump('loc_91FD')

    def _loc_91F6(): pass

    label('loc_91F6')

    ChrSetDirection(0x0102, 180, 400)

    def _loc_91FD(): pass

    label('loc_91FD')

    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0008,
        (
            '#0580370180V#791F#2P你们大家也辛苦了，\n',
            '这下真是帮了大忙了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_92E3',
    )

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
        0,
        (
            TXT(0x00, '【◇恢复全部的通讯器】\n'),
            TXT(0x01, '【◇只恢复这里的通讯器】\n'),
            TXT(0x02, '【◇不变更】\n'),
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
        (0x00000000, 'loc_92D1'),
        (0x00000001, 'loc_92DA'),
        (-1, 'loc_92E3'),
    )

    def _loc_92D1(): pass

    label('loc_92D1')

    SetScenaFlags(ScenaFlag(0x0400, 1, 0x2001))
    SetScenaFlags(ScenaFlag(0x0400, 3, 0x2003))

    Jump('loc_92E3')

    def _loc_92DA(): pass

    label('loc_92DA')

    ClearScenaFlags(ScenaFlag(0x0400, 1, 0x2001))
    ClearScenaFlags(ScenaFlag(0x0400, 3, 0x2003))

    Jump('loc_92E3')

    def _loc_92E3(): pass

    label('loc_92E3')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_95E1',
    )

    ChrTalk(
        0x0101,
        (
            '#0010370181V#1016F#6P嘿嘿，不用客气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080370182V#071F#6P哈哈，怎么了。\n',
            '你以前可没这么直白啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580370183V#792F#2P这真是遗憾啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370184V#791F我倒是觉得应该没有\n',
            '比我更直白的人了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 1, 0x2001)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 3, 0x2003)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_952C',
    )

    ChrTalk(
        0x0108,
        (
            '#0080370185V#075F#6P与其说是直白，\n',
            '倒不如说是毫不客气。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080370186V#070F好了，这样一来，\n',
            '所有支部的通信器就都修好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080370187V确认各地的状况\n',
            '进行执行任务的报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x009B, 0x04, 0x10)
    OP_AF(0x67, 0x009B)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    OP_28(0x009B, 0x01, 0x0100)

    ChrTalk(
        0x0008,
        (
            '#0580370188V#791F#2P真是辛苦大家了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370189V如此一来，\n',
            '我们就可以迅速作出各种应对策略了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080370190V#070F还有其他事情要帮忙吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_95DE')

    def _loc_952C(): pass

    label('loc_952C')

    ChrTalk(
        0x0108,
        (
            '#0080370185V#075F#6P用不着\n',
            '那么客气啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080370192V#070F嗯，接下来准备照这个样子，\n',
            '把其他几个协会的通讯器也\n',
            '给修理好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080370193V不过，这里没有其他需要帮忙的事情吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_95DE(): pass

    label('loc_95DE')

    Jump('loc_9A1B')

    def _loc_95E1(): pass

    label('loc_95E1')

    ChrTalk(
        0x0101,
        (
            '#0010370181V#1016F#6P嘿嘿，不用客气。',
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
        'loc_9648',
    )

    ChrTalk(
        0x0102,
        (
            '#0020370195V#1040F#6P能帮上忙就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9679')

    def _loc_9648(): pass

    label('loc_9648')

    ChrTalk(
        0x0102,
        (
            '#0020370195V#1040F#2P能帮上忙就比什么都好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9679(): pass

    label('loc_9679')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 1, 0x2001)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 3, 0x2003)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_9894',
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_970C',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350450V#020F好了，这下子\n',
            '地方支部所有的通讯器都修好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030370197V那么现在就将各地的任务\n',
            '做个总结报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9795')

    def _loc_970C(): pass

    label('loc_970C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9795',
    )

    ChrTalk(
        0x0106,
        (
            '#0050350452V#051F好了，这下子\n',
            '地方支部所有的通讯器都修好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050350453V那么，结合各地的状况\n',
            '那就进行任务的汇报吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9795(): pass

    label('loc_9795')

    OP_59()
    OP_28(0x009B, 0x04, 0x10)
    OP_AF(0x67, 0x009B)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    OP_28(0x009B, 0x01, 0x0100)

    ChrTalk(
        0x0008,
        (
            '#0580370188V#791F#2P真是辛苦大家了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370189V这样一来\n',
            '这样我们就可以迅速作出各种应对策略了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9858',
    )

    ChrTalk(
        0x0103,
        (
            '#0030370198V#020F还有其他事情要帮忙吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9891')

    def _loc_9858(): pass

    label('loc_9858')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9891',
    )

    ChrTalk(
        0x0106,
        (
            '#0050350460V#051F还有什么要帮忙的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9891(): pass

    label('loc_9891')

    Jump('loc_9A1B')

    def _loc_9894(): pass

    label('loc_9894')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9917',
    )

    ChrTalk(
        0x0103,
        (
            '#0030370199V#020F#6P嗯，准备继续\n',
            '把其他协会的通讯器\n',
            '也修好…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030370200V不过，这里没有其他事情要帮忙了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9A1B')

    def _loc_9917(): pass

    label('loc_9917')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_999A',
    )

    ChrTalk(
        0x0106,
        (
            '#0050350463V#051F#6P嗯，准备继续\n',
            '把其他协会的通讯器\n',
            '也修好…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050370208V不过，这里没有其他事情要帮忙了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9A1B')

    def _loc_999A(): pass

    label('loc_999A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9A1B',
    )

    ChrTalk(
        0x0107,
        (
            '#0070370209V#560F这个嘛，准备继续\n',
            '把其他协会的通讯器\n',
            '也修好…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070370210V不过，这里没有其他事情要帮忙了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9A1B(): pass

    label('loc_9A1B')

    ChrTalk(
        0x0008,
        (
            '#0580370211V#791F#2P雷斯顿要塞就在附近，\n',
            '治安方面应该没什么问题，不过…\n',
            '你们还是看看告示板上的委托吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370212V如果有时间的话\n',
            '去中央工房和亚尔摩温泉看看吧，\n',
            '确认一下那里的状况就可以了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370213V那里好像有什么麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370214V#1006F#6P嗯，知道啦！',
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
        'loc_9B5C',
    )

    ChrTalk(
        0x0102,
        (
            '#0020370215V#1040F#6P明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9B7F')

    def _loc_9B5C(): pass

    label('loc_9B5C')

    ChrTalk(
        0x0102,
        (
            '#0020370215V#1040F#2P明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9B7F(): pass

    label('loc_9B7F')

    FadeOut(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※因为通讯器已经修好了，可以呼叫在其他支部待命的同伴，\n',
            '  将他们召集来蔡斯支部。\n',
            '　想呼叫的时候请在接待处选择『呼叫同伴』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_59()
    OP_4B(0x0008, 255)
    SetScenaFlags(ScenaFlag(0x0400, 5, 0x2005))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 1, 0x2001)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 3, 0x2003)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_9C2E',
    )

    SetScenaFlags(ScenaFlag(0x0412, 1, 0x2091))

    Jump('loc_9C31')

    def _loc_9C2E(): pass

    label('loc_9C2E')

    ClearScenaFlags(ScenaFlag(0x0412, 1, 0x2091))

    def _loc_9C31(): pass

    label('loc_9C31')

    OP_28(0x009B, 0x02, 0x0010)
    OP_28(0x009B, 0x01, 0x0020)
    CameraMove(2510, 0, -2680, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, 2510, 0, -2680, 180)
    ChrSetPos(0x0001, 2510, 0, -2680, 180)
    ChrSetPos(0x0002, 2510, 0, -2680, 180)
    ChrSetPos(0x0003, 2510, 0, -2680, 180)
    OP_69(0x0000, 0)
    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0010 offset: 0x9CD1
@scena.Code('func_10_9CD1')
def func_10_9CD1():
    ChrWalkTo(0x00FE, 3900, 0, -3480, 2500, 0x00)
    ChrWalkTo(0x00FE, 4330, 0, -700, 2500, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0011 offset: 0x9D01
@scena.Code('func_11_9D01')
def func_11_9D01():
    ChrWalkTo(0x00FE, 2650, 0, -3190, 2500, 0x00)
    ChrWalkTo(0x00FE, 3330, 0, -700, 2500, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0012 offset: 0x9D31
@scena.Code('func_12_9D31')
def func_12_9D31():
    ChrWalkTo(0x00FE, 3900, 0, -3480, 2500, 0x00)
    ChrWalkTo(0x00FE, 4330, 0, -1800, 2500, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0013 offset: 0x9D61
@scena.Code('func_13_9D61')
def func_13_9D61():
    ChrWalkTo(0x00FE, 2650, 0, -3190, 2500, 0x00)
    ChrWalkTo(0x00FE, 3330, 0, -1800, 2500, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0014 offset: 0x9D91
@scena.Code('func_14_9D91')
def func_14_9D91():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 1, 0x2001)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 3, 0x2003)),
            Expr.Ez,
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 2, 0x2002)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 4, 0x2004)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 6, 0x2006)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_9DAB',
    )

    Return()

    def _loc_9DAB(): pass

    label('loc_9DAB')

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
        'loc_9DCB',
    )

    Call(0, 0x001B)
    Call(0, 0x001D)
    FadeIn(0, 0)

    def _loc_9DCB(): pass

    label('loc_9DCB')

    PlaySE(195, 0x01, 0x64)
    LoadEffect(0x00, 'map\\\\mp001_00.eff')
    LoadEffect(0x01, 'map\\\\mp001_01.eff')
    PlayEffect(0x00, 0x00, 0x00FF, 4840, 2000, 2560, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_4A(0x0008, 255)

    ChrTalk(
        0x0101,
        (
            '#0010260612V#1004F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_9E55')
    def lambda_9E55():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_9E55)

    @scena.Lambda('lambda_9E63')
    def lambda_9E63():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_9E63)

    Sleep(100)

    @scena.Lambda('lambda_9E76')
    def lambda_9E76():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_9E76)

    ChrSetDirection(0x0003, 0, 400)

    ChrTalk(
        0x0008,
        (
            '#0580370218V#791F#3P这么快就有联络了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    CameraMove(3970, 0, 2180, 0)
    OP_67(0, 6980, -10000, 0)
    CameraSetDistance(2500, 0)
    OP_6C(315000, 0)
    OP_6E(268, 0)
    ChrSetPos(0x0101, 1770, 0, -6100, 0)
    ChrSetPos(0x0102, 1770, 0, -6100, 0)
    ChrSetPos(0x00F8, 1770, 0, -6100, 0)
    ChrSetPos(0x00F9, 1770, 0, -6100, 0)
    ChrWalkTo(0x0008, 5350, 0, 1200, 2000, 0x00)
    ChrWalkTo(0x0008, 5350, 0, 2490, 2000, 0x00)
    ChrSetDirection(0x0008, 270, 400)
    Sleep(700)

    OP_23(0x00C3)
    PlaySE(131, 0x00, 0x64)
    StopEffect(0x00, 0x00)
    PlayEffect(0x01, 0x01, 0x00FF, 4840, 2000, 2560, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    WaitForThreadExit(0x0101, 0x0001)
    CreateThread(0x0101, 0x00, 0x00, func_15_A7FC)

    ChrTalk(
        0x0008,
        (
            '#0580370219V#792F这里是游击士协会\n',
            '蔡斯支部……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370220V#791F……啊啊，是你吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370221V这边的通讯也是刚刚才修复好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370222V……嗯嗯，是啊。\n',
            '他们正好就在这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x00F9, 0x0001)

    @scena.Lambda('lambda_A082')
    def lambda_A082():
        CameraMove(3720, 0, 1230, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_A082)

    @scena.Lambda('lambda_A09A')
    def lambda_A09A():
        OP_67(0, 6580, -10000, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_A09A)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010370223V#1004F#6P（找我们的……？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370224V#1044F#6P（好像有话要说。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580370225V#792F……嗯……嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370226V………………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370227V#791F……明白了。\n',
            '我会转告给他们的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370228V关于这边的状况\n',
            '以后有机会再联络吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370229V#792F……是啊。\n',
            '只有互相加油了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    PlaySE(131, 0x00, 0x64)
    StopEffect(0x01, 0x00)
    Sleep(1000)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A27C',
    )

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A24D',
    )

    ChrTalk(
        0x0108,
        (
            '#0080370230V#073F#6P雾香，\n',
            '是哪里的联络？',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_A278')

    def _loc_A24D(): pass

    label('loc_A24D')

    ChrTalk(
        0x0108,
        (
            '#0080370231V#073F雾香，\n',
            '是哪里的联络？',
            TxtCtl.Enter,
        ),
    )

    def _loc_A278(): pass

    label('loc_A278')

    CloseMessageWindow()

    Jump('loc_A2B2')

    def _loc_A27C(): pass

    label('loc_A27C')

    ChrTalk(
        0x0101,
        (
            '#0010370232V#1015F#6P雾香姐姐，\n',
            '是哪里来的联络？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_A2B2(): pass

    label('loc_A2B2')

    @scena.Lambda('lambda_A2B8')
    def lambda_A2B8():
        CameraMove(3080, 0, 500, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_A2B8)

    ChrWalkTo(0x0008, 5300, 0, 1200, 2000, 0x00)
    ChrWalkTo(0x0008, 3500, 0, 1200, 2000, 0x00)
    ChrSetDirection(0x0008, 180, 400)
    Sleep(700)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#0580370233V#791F是王都支部的艾南先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370234V好像是艾莉茜娅女王\n',
            '有事情要和你们说，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370235V如果到格兰赛尔附近来的话，\n',
            '希望你们去王城一趟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370236V#1004F#6P女王陛下！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A413',
    )

    ChrTalk(
        0x0103,
        (
            '#0030370237V#023F#6P这真让人惊讶……\n',
            '到底是什么事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A4F2')

    def _loc_A413(): pass

    label('loc_A413')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A460',
    )

    ChrTalk(
        0x0106,
        (
            '#0050350505V#052F#6P真是让人吃惊啊……\n',
            '到底有什么事呢?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A4F2')

    def _loc_A460(): pass

    label('loc_A460')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A4F2',
    )

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A4B9',
    )

    ChrTalk(
        0x0108,
        (
            '#0080370239V#073F#6P那真是让人吃惊啊。\n',
            '到底有什么事呢?',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_A4F1')

    def _loc_A4B9(): pass

    label('loc_A4B9')

    ChrTalk(
        0x0108,
        (
            '#0080370240V#073F那真是让人吃惊啊。\n',
            '到底有什么事呢?',
            TxtCtl.Enter,
        ),
    )

    def _loc_A4F1(): pass

    label('loc_A4F1')

    CloseMessageWindow()

    def _loc_A4F2(): pass

    label('loc_A4F2')

    ChrTalk(
        0x0008,
        (
            '#0580370241V#792F我没有具体问。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370242V#790F不过似乎是在通信器中\n',
            '难以说清楚的事哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370243V#1015F#6P通信中无法说清楚的事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010350513V#1026F是吗，导力通讯\n',
            '存在被人监听的危险……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370245V#1042F#6P看来是\n',
            '比较机密的话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580370246V#792F不过倒是没要求你们马上就去，\n',
            '看样子并不是什么急事，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370247V#791F路过王都的时候顺便去看看就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370248V#1006F#6P这样的啊……知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A714',
    )

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A6E6',
    )

    ChrTalk(
        0x0108,
        (
            '#0080370249V#070F#6P嗯，那就过去一趟吧。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_A710')

    def _loc_A6E6(): pass

    label('loc_A6E6')

    ChrTalk(
        0x0108,
        (
            '#0080370250V#070F嗯，那就过去一趟吧。',
            TxtCtl.Enter,
        ),
    )

    def _loc_A710(): pass

    label('loc_A710')

    CloseMessageWindow()

    Jump('loc_A73F')

    def _loc_A714(): pass

    label('loc_A714')

    ChrTalk(
        0x0102,
        (
            '#0020370251V#1040F#6P赶快过去看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_A73F(): pass

    label('loc_A73F')

    SetScenaFlags(ScenaFlag(0x0400, 6, 0x2006))
    OP_28(0x009B, 0x01, 0x0100)
    OP_28(0x009B, 0x01, 0x0200)
    OP_28(0x009B, 0x01, 0x0400)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_4B(0x0008, 255)
    CameraMove(2510, 0, -2680, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, 2510, 0, -2680, 180)
    ChrSetPos(0x0001, 2510, 0, -2680, 180)
    ChrSetPos(0x0002, 2510, 0, -2680, 180)
    ChrSetPos(0x0003, 2510, 0, -2680, 180)
    OP_69(0x0000, 0)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0015 offset: 0xA7FC
@scena.Code('func_15_A7FC')
def func_15_A7FC():
    CreateThread(0x0101, 0x01, 0x00, func_10_9CD1)
    Sleep(500)

    CreateThread(0x0102, 0x01, 0x00, func_11_9D01)
    Sleep(600)

    CreateThread(0x00F8, 0x01, 0x00, func_12_9D31)
    Sleep(300)

    CreateThread(0x00F9, 0x01, 0x00, func_13_9D61)
    WaitForThreadExit(0x00F9, 0x0001)

    Return()

# id: 0x0016 offset: 0xA82D
@scena.Code('func_16_A82D')
def func_16_A82D():
    ChrWalkTo(0x00FE, 1590, 0, -4400, 2000, 0x00)
    ChrWalkTo(0x00FE, 3090, 0, -700, 2000, 0x00)

    @scena.Lambda('lambda_A85B')
    def lambda_A85B():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_A85B')

    DispatchAsync2(0x00FE, 0x0002, lambda_A85B)

    Return()

# id: 0x0017 offset: 0xA867
@scena.Code('func_17_A867')
def func_17_A867():
    ChrWalkTo(0x00FE, 2530, 0, -4570, 2000, 0x00)
    ChrWalkTo(0x00FE, 3850, 0, -700, 2000, 0x00)

    @scena.Lambda('lambda_A895')
    def lambda_A895():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_A895')

    DispatchAsync2(0x00FE, 0x0002, lambda_A895)

    Return()

# id: 0x0018 offset: 0xA8A1
@scena.Code('func_18_A8A1')
def func_18_A8A1():
    ChrWalkTo(0x00FE, 1590, 0, -4400, 2000, 0x00)
    ChrWalkTo(0x00FE, 2330, 0, -1320, 2000, 0x00)

    @scena.Lambda('lambda_A8CF')
    def lambda_A8CF():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_A8CF')

    DispatchAsync2(0x00FE, 0x0002, lambda_A8CF)

    Return()

# id: 0x0019 offset: 0xA8DB
@scena.Code('func_19_A8DB')
def func_19_A8DB():
    ChrWalkTo(0x00FE, 2530, 0, -4570, 2000, 0x00)
    ChrWalkTo(0x00FE, 4650, 0, -920, 2000, 0x00)

    @scena.Lambda('lambda_A909')
    def lambda_A909():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_A909')

    DispatchAsync2(0x00FE, 0x0002, lambda_A909)

    Return()

# id: 0x001A offset: 0xA915
@scena.Code('func_1A_A915')
def func_1A_A915():
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
        'loc_A935',
    )

    Call(0, 0x001B)
    Call(0, 0x001D)
    FadeIn(0, 0)

    def _loc_A935(): pass

    label('loc_A935')

    Fade(1000)
    CameraMove(2920, 0, 700, 0)
    OP_67(0, 5850, -10000, 0)
    CameraSetDistance(2320, 0)
    OP_6C(315000, 0)
    OP_6E(332, 0)
    ChrSetPos(0x0101, 4360, 0, -720, 0)
    ChrSetPos(0x0102, 3220, 0, -700, 0)
    ChrSetPos(0x00F8, 4600, 0, -1800, 0)
    ChrSetPos(0x00F9, 3230, 0, -1800, 0)
    ChrSetDirection(0x0008, 180, 0)
    LoadEffect(0x01, 'map\\\\mp001_01.eff')
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0580370420V#790F#2P啊……\n',
            '发生什么事了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370157V#1002F#6P嗯，其实呢……',
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
            '将内燃引擎的事情告诉了雾香，\n',
            '并拜托雾香帮忙和雷斯顿要塞\n',
            '进行联络。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#0580370422V#791F#2P呵呵，这也是我们\n',
            '游击士应该做的工作啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370423V要塞的通信器应该也已经恢复了，\n',
            '现在就和他们联络看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_AB25')
    def lambda_AB25():
        CameraMove(3670, 0, 1500, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_AB25)

    ChrWalkTo(0x0008, 5350, 0, 1200, 2000, 0x00)
    ChrWalkTo(0x0008, 5350, 0, 2490, 2000, 0x00)
    ChrSetDirection(0x0008, 270, 400)
    Sleep(700)

    WaitForThreadExit(0x0101, 0x0001)
    PlaySE(131, 0x00, 0x64)
    PlayEffect(0x01, 0x01, 0x00FF, 4840, 2000, 2560, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1500)

    ChrTalk(
        0x0008,
        (
            '#0580370424V#792F……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370425V#790F您好，这里是游击士协会\n',
            '的蔡斯支部──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    Sleep(2000)

    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0580370426V#792F──是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370427V#791F我知道了，\n',
            '这就转告他们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(131, 0x00, 0x64)
    StopEffect(0x01, 0x00)
    Sleep(1000)

    @scena.Lambda('lambda_AC92')
    def lambda_AC92():
        CameraMove(2920, 0, 700, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_AC92)

    ChrWalkTo(0x0008, 5300, 0, 1200, 2000, 0x00)
    ChrWalkTo(0x0008, 3500, 0, 1200, 2000, 0x00)
    ChrSetDirection(0x0008, 180, 400)
    Sleep(700)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#0580370428V#792F#2P──现在要塞里\n',
            '也没有『内燃引擎』了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370429V#1020F#6P咦咦！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370430V#1044F#6P这是怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0580370431V#790F#2P他们准备将它那东西返还给中央工房，\n',
            '就使用一艘警备艇进行运送。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370432V但那艘警备艇却因为导力停止现象\n',
            '而紧急迫降在托兰特平原道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370433V#1004F#6P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AE6E',
    )

    ChrTalk(
        0x0108,
        (
            '#0080370434V#070F#6P原来如此，事情是那样吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AEF1')

    def _loc_AE6E(): pass

    label('loc_AE6E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AEB1',
    )

    ChrTalk(
        0x0103,
        (
            '#0030370435V#027F#6P原来如此，事情是那样呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AEF1')

    def _loc_AEB1(): pass

    label('loc_AEB1')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AEF1',
    )

    ChrTalk(
        0x0106,
        (
            '#0050370436V#051F#6P原来如此，事情是那样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AEF1(): pass

    label('loc_AEF1')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AF4F',
    )

    ChrTalk(
        0x0107,
        (
            '#0070370437V#560F#6P那么说的话，只要去找\n',
            '那艘警备艇上的士兵就可以了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AF95')

    def _loc_AF4F(): pass

    label('loc_AF4F')

    ChrTalk(
        0x0102,
        (
            '#0020370438V#1040F#6P这样的话，去拜托\n',
            '警备艇的负责人不就行了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AF95(): pass

    label('loc_AF95')

    ChrTalk(
        0x0008,
        (
            '#0580370439V#792F#2P嗯，没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580370440V#791F警备艇应该降落在\n',
            '托兰特平原道一带了，\n',
            '你们去找找看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0401, 4, 0x200C))
    OP_28(0x00C2, 0x01, 0x0010)
    OP_28(0x00C2, 0x01, 0x0040)
    EventEnd(0x00)

    Return()

# id: 0x001B offset: 0xB014
@scena.Code('func_1B_B014')
def func_1B_B014():
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
        (0x00000000, 'loc_B08E'),
        (0x00000001, 'loc_B094'),
        (-1, 'loc_B09A'),
    )

    def _loc_B08E(): pass

    label('loc_B08E')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_B09A')

    def _loc_B094(): pass

    label('loc_B094')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_B09A')

    def _loc_B09A(): pass

    label('loc_B09A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_B0A8',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_B0AC')

    def _loc_B0A8(): pass

    label('loc_B0A8')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_B0AC(): pass

    label('loc_B0AC')

    Return()

# id: 0x001C offset: 0xB0AD
@scena.Code('func_1C_B0AD')
def func_1C_B0AD():
    MapClearFlags(0x00000001)
    CameraMove(0, 0, 0, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_B0E7',
    )

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['雪拉扎德'],
            ChrTable['提妲'],
            0x00FF,
        ),
        (
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            0xFFFF,
        ),
    )

    Jump('loc_B101')

    def _loc_B0E7(): pass

    label('loc_B0E7')

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['阿加特'],
            ChrTable['提妲'],
            0x00FF,
        ),
        (
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            0xFFFF,
        ),
    )

    def _loc_B101(): pass

    label('loc_B101')

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0)

    Return()

# id: 0x001D offset: 0xB113
@scena.Code('func_1D_B113')
def func_1D_B113():
    MapClearFlags(0x00000001)
    CameraMove(106730, -1920, 53920, 0)
    Sleep(100)

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['雪拉扎德'],
            ChrTable['提妲'],
            ChrTable['金'],
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

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0)
    Sleep(1000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4135_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4135   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4135.x'
    header.mapIndex       = 1
    header.bgm            = 14
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T4135_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
        ('ED6_DT07/CH01540._CH', 'ED6_DT07/CH01540P._CP'),
        ('ED6_DT27/CH03510._CH', 'ED6_DT27/CH03510P._CP'),
        ('ED6_DT07/CH01490._CH', 'ED6_DT07/CH01490P._CP'),
        ('ED6_DT07/CH01660._CH', 'ED6_DT07/CH01660P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT27/CH03060._CH', 'ED6_DT27/CH03060P._CP'),
        ('ED6_DT07/CH01230._CH', 'ED6_DT07/CH01230P._CP'),
        ('ED6_DT07/CH01170._CH', 'ED6_DT07/CH01170P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
    ]

# id: 0x10001 offset: 0x102
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '莉西娅',
            x                   = 4400,
            z                   = 0,
            y                   = -5910,
            direction           = 255,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '馆长',
            x                   = -69160,
            z                   = 0,
            y                   = 57560,
            direction           = 90,
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
            name                = '森特',
            x                   = -69000,
            z                   = 0,
            y                   = -1470,
            direction           = 90,
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
            name                = '吉米',
            x                   = -2380,
            z                   = 0,
            y                   = -5360,
            direction           = 0,
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
            name                = '王都市民',
            x                   = 72040,
            z                   = 0,
            y                   = 2820,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '王都市民',
            x                   = 72050,
            z                   = 0,
            y                   = 1820,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '王都市民',
            x                   = 7500,
            z                   = 4000,
            y                   = -990,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '王都市民',
            x                   = -1050,
            z                   = 0,
            y                   = 66030,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '王都市民',
            x                   = 3870,
            z                   = 0,
            y                   = 2930,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '玲',
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
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '提妲',
            x                   = -1050,
            z                   = 0,
            y                   = 66290,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
    )

# id: 0x10002 offset: 0x262
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x262
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x262
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 2580,
            triggerZ            = 0,
            triggerY            = -5970,
            triggerRange        = 800,
            actorX              = 4400,
            actorZ              = 1700,
            actorY              = -5910,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 5090,
            triggerZ            = 0,
            triggerY            = 2190,
            triggerRange        = 800,
            actorX              = 5090,
            actorZ              = 800,
            actorY              = 2190,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001D,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 7840,
            triggerZ            = 4000,
            triggerY            = 6700,
            triggerRange        = 800,
            actorX              = 7840,
            actorZ              = 5700,
            actorY              = 6700,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001E,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 75860,
            triggerZ            = 0,
            triggerY            = -2000,
            triggerRange        = 800,
            actorX              = 75860,
            actorZ              = 1500,
            actorY              = -2000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001F,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 73200,
            triggerZ            = 0,
            triggerY            = 710,
            triggerRange        = 800,
            actorX              = 73200,
            actorZ              = 800,
            actorY              = 710,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0020,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 68740,
            triggerZ            = 0,
            triggerY            = 7310,
            triggerRange        = 800,
            actorX              = 68740,
            actorZ              = 800,
            actorY              = 7310,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0021,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 73480,
            triggerZ            = 0,
            triggerY            = 6420,
            triggerRange        = 800,
            actorX              = 73480,
            actorZ              = 800,
            actorY              = 6420,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0022,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 75820,
            triggerZ            = 4000,
            triggerY            = 8010,
            triggerRange        = 800,
            actorX              = 75820,
            actorZ              = 5700,
            actorY              = 8010,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0023,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 71960,
            triggerZ            = 4000,
            triggerY            = 9290,
            triggerRange        = 800,
            actorX              = 71960,
            actorZ              = 4800,
            actorY              = 9290,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0024,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -20,
            triggerZ            = 0,
            triggerY            = 77880,
            triggerRange        = 800,
            actorX              = -20,
            actorZ              = 1700,
            actorY              = 77880,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0025,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -770,
            triggerZ            = 0,
            triggerY            = 72650,
            triggerRange        = 800,
            actorX              = -770,
            actorZ              = 800,
            actorY              = 72650,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0026,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 7000,
            triggerZ            = 0,
            triggerY            = 66550,
            triggerRange        = 1200,
            actorX              = 7000,
            actorZ              = 800,
            actorY              = 66550,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0027,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 1770,
            triggerZ            = 0,
            triggerY            = 66890,
            triggerRange        = 800,
            actorX              = 1770,
            actorZ              = 800,
            actorY              = 66890,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0028,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -3790,
            triggerZ            = 0,
            triggerY            = 64959,
            triggerRange        = 800,
            actorX              = -3790,
            actorZ              = 800,
            actorY              = 64959,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0029,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x45A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_48E',
    )

    ChrSetPos(0x000B, -950, 0, 74090, 90)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)

    Jump('loc_5B1')

    def _loc_48E(): pass

    label('loc_48E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_4BA',
    )

    ChrSetPos(0x0009, -69470, 0, 57290, 273)
    ChrSetPos(0x000B, -71620, 0, 57130, 86)

    Jump('loc_5B1')

    def _loc_4BA(): pass

    label('loc_4BA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_4D5',
    )

    ChrSetPos(0x000B, -950, 0, 74090, 90)

    Jump('loc_5B1')

    def _loc_4D5(): pass

    label('loc_4D5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_520',
    )

    ChrSetPos(0x000B, 69710, 0, 7140, 0)

    If(
        (
            (Expr.Eval, "OP_29(0x00C4, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_51D',
    )

    ChrSetPos(0x0009, 7000, 4000, -3740, 90)

    If(
        (
            (Expr.Eval, "OP_29(0x00C4, 0x00, 0x02)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_51D',
    )

    ChrSetFlags(0x0009, 0x0010)

    def _loc_51D(): pass

    label('loc_51D')

    Jump('loc_5B1')

    def _loc_520(): pass

    label('loc_520')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_594',
    )

    ChrSetPos(0x000B, 4170, 0, 2620, 45)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 5, 0x161D)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_565',
    )

    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, -2990, 0, 67900, 165)
    CreateThread(0x0011, 0x00, 0x00, func_02_67D)

    def _loc_565(): pass

    label('loc_565')

    If(
        (
            (Expr.Eval, "OP_29(0x00C4, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_591',
    )

    ChrSetPos(0x0009, 7000, 4000, -3740, 90)

    If(
        (
            (Expr.Eval, "OP_29(0x00C4, 0x00, 0x02)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_591',
    )

    ChrSetFlags(0x0009, 0x0010)

    def _loc_591(): pass

    label('loc_591')

    Jump('loc_5B1')

    def _loc_594(): pass

    label('loc_594')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_5B1',
    )

    ChrSetPos(0x0009, -930, 0, 71060, 90)
    ChrSetFlags(0x000B, 0x0080)

    def _loc_5B1(): pass

    label('loc_5B1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_5C7',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    MapSetFlags(0x10000000)
    Event(1, 0x0003)

    Jump('loc_628')

    def _loc_5C7(): pass

    label('loc_5C7')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_5DB'),
        (0x00000067, 'loc_610'),
        (0x00000068, 'loc_610'),
        (-1, 'loc_628'),
    )

    def _loc_5DB(): pass

    label('loc_5DB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 6, 0x162E)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 0, 0x1630)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5F3',
    )

    MapSetFlags(0x10000000)
    Event(0, func_10_297B)

    Jump('loc_60D')

    def _loc_5F3(): pass

    label('loc_5F3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 6, 0x162E)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 7, 0x162F)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_60D',
    )

    MapSetFlags(0x10000000)
    Event(0, func_0F_2577)

    def _loc_60D(): pass

    label('loc_60D')

    Jump('loc_628')

    def _loc_610(): pass

    label('loc_610')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 0, 0x1630)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 1, 0x1631)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_625',
    )

    MapSetFlags(0x10000000)
    Event(0, func_15_30F4)

    def _loc_625(): pass

    label('loc_625')

    Jump('loc_628')

    def _loc_628(): pass

    label('loc_628')

    Return()

# id: 0x0001 offset: 0x629
@scena.Code('func_01_629')
def func_01_629():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_645',
    )

    OP_B1('t4135_y')

    Jump('loc_64E')

    def _loc_645(): pass

    label('loc_645')

    OP_B1('t4135_n')

    def _loc_64E(): pass

    label('loc_64E')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_67C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_67C',
    )

    OP_71(0x0001, 0x0004)

    If(
        (
            (Expr.Eval, "OP_29(0x00C4, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x00C4, 0x00, 0x40)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_67C',
    )

    OP_72(0x0001, 0x0004)

    def _loc_67C(): pass

    label('loc_67C')

    Return()

# id: 0x0002 offset: 0x67D
@scena.Code('func_02_67D')
def func_02_67D():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_692',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_67D')

    def _loc_692(): pass

    label('loc_692')

    Return()

# id: 0x0003 offset: 0x693
@scena.Code('func_03_693')
def func_03_693():
    Call(0, 0x0004)

    Return()

# id: 0x0004 offset: 0x698
@scena.Code('func_04_698')
def func_04_698():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_704',
    )

    ChrTalk(
        0x0008,
        (
            '欢迎光临，\n',
            '历史资料馆免费开放中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '为了让市民朋友\n',
            '能有所放松，\n',
            '女王陛下作了这一决定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A39')

    def _loc_704(): pass

    label('loc_704')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_872',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C8, 7, 0x1647)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_814',
    )

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '那、那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '后来有没有找到\n',
            '和你们同行的那位小姐？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F嗯，嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '没事了，\n',
            '我们已经找到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '是吗？太好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '听到昨夜发生的事件，\n',
            '我就有点担心\n',
            '那位小姐了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '听说已经找到了，\n',
            '我总算放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x02C8, 7, 0x1647))

    Jump('loc_86F')

    def _loc_814(): pass

    label('loc_814')

    ChrTalk(
        0x0008,
        (
            '听到昨夜发生的事件，\n',
            '我就有点担心\n',
            '那位小姐了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '听说已经找到了，\n',
            '我总算放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_86F(): pass

    label('loc_86F')

    Jump('loc_A39')

    def _loc_872(): pass

    label('loc_872')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_98F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 1, 0x1631)),
            Expr.Return,
        ),
        'loc_8EC',
    )

    ChrTalk(
        0x0008,
        (
            '线索就是『你知道哪儿有\n',
            '没有颜色的鱼吗？』',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '和你们一起的那位小姐用\n',
            '一种很恶作剧的表情\n',
            '这么说道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_98C')

    def _loc_8EC(): pass

    label('loc_8EC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 0, 0x1630)),
            Expr.Return,
        ),
        'loc_934',
    )

    ChrTalk(
        0x0008,
        (
            '和你们一起的那位\n',
            '小姐来过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我想她应该\n',
            '还在馆内。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_98C')

    def _loc_934(): pass

    label('loc_934')

    ChrTalk(
        0x0008,
        (
            '我如果看见你们要找的\n',
            '那位小姐我会联系协会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '入口仅此一处，\n',
            '应该不会漏看的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_98C(): pass

    label('loc_98C')

    Jump('loc_A39')

    def _loc_98F(): pass

    label('loc_98F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_9C8',
    )

    ChrTalk(
        0x0008,
        (
            '本馆很快就要关门了。\n',
            '欢迎您下次光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A39')

    def _loc_9C8(): pass

    label('loc_9C8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_A0D',
    )

    ChrTalk(
        0x0008,
        (
            '最近，馆长和研究员\n',
            '都很忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '希望他们保重身体……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A39')

    def _loc_A0D(): pass

    label('loc_A0D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_A39',
    )

    ChrTalk(
        0x0008,
        (
            '欢迎光临，\n',
            '欢迎光临历史资料馆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A39(): pass

    label('loc_A39')

    TalkEnd(0x0008)

    Return()

# id: 0x0005 offset: 0xA3D
@scena.Code('func_05_A3D')
def func_05_A3D():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AE3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_AE0',
    )

    ChrTalk(
        0x00FE,
        (
            '历史资料馆这边没什么\n',
            '具体的损失。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过人民生活受到冲击的\n',
            '事实仍然无法改变。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '通过这次的事件终于知道\n',
            '我们平时是多么依赖导力了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AE0(): pass

    label('loc_AE0')

    Jump('loc_1427')

    def _loc_AE3(): pass

    label('loc_AE3')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1427',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_B51',
    )

    ChrTalk(
        0x00FE,
        (
            '这次事件从管理的角度来看\n',
            '也算是积累了好的经验。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '必须防范类似事件的\n',
            '再度发生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1427')

    def _loc_B51(): pass

    label('loc_B51')

    If(
        (
            (Expr.Eval, "OP_29(0x00C4, 0x00, 0x04)"),
            (Expr.Eval, "OP_29(0x00C4, 0x00, 0x40)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x00C4, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x00C4, 0x01, 0x4000)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_CEE',
    )

    ChrTalk(
        0x00FE,
        (
            '哟，是你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '埃尔赛尤的照片\n',
            '后来顺利找到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1004F这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1007F非常抱歉。\n',
            '没能帮上忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哪里哪里，\n',
            '别介意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '既然顺利找回来了，\n',
            '也就没事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1008F很感激您能这么说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1015F那么……\n',
            '是在哪儿找到的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '令人不可思议的是\n',
            '居然是在关闭中的竞技场\n',
            '找到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像是做定期检查的\n',
            '警卫员找到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1007F唔～想不到\n',
            '是在那种地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x00C4, 0x01, 0x4000)
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_1427')

    def _loc_CEE(): pass

    label('loc_CEE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            (Expr.Eval, "OP_29(0x00C4, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x00C4, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_F21',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x00C4, 0x00, 0x04)"),
            Expr.Return,
        ),
        'loc_EC4',
    )

    ChrTalk(
        0x00FE,
        (
            '要不要再\n',
            '看一次卡片？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
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
            TXT(0x00, '【是】\n'),
            TXT(0x01, '【否】\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_EA3',
    )

    FadeOut(300, 0, 100)
    OP_AD('ED6_DT24/C_VIS124._CH', 0x00BE, 0x0064, 0x000001F4)
    Sleep(1000)

    SetMessageWindowPos(-1, 300, -1, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　　美丽的公主及其随从啊。　　\n',
            '　　 高尚的白鹰剪影画\n',
            '　　    飘落在我手中。　　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '　　  如果就想要寻求它\n',
            '　　  就要回应我的挑战。 　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '　  第一把钥匙在老将之居。　　\n',
            '　 探索『时间的旁观者』吧。　　',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_AE(0x000001F4)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '那我就等着你们的好消息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EC1')

    def _loc_EA3(): pass

    label('loc_EA3')

    ChrTalk(
        0x00FE,
        (
            '那我就等着你们的好消息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EC1(): pass

    label('loc_EC1')

    Jump('loc_F1E')

    def _loc_EC4(): pass

    label('loc_EC4')

    If(
        (
            (Expr.Eval, "OP_29(0x00C4, 0x00, 0x02)"),
            Expr.Return,
        ),
        'loc_EE7',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x00C4, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_EE0',
    )

    Call(1, 0x0001)

    Jump('loc_EE4')

    def _loc_EE0(): pass

    label('loc_EE0')

    Call(1, 0x0000)

    def _loc_EE4(): pass

    label('loc_EE4')

    Jump('loc_F1E')

    def _loc_EE7(): pass

    label('loc_EE7')

    ChrTalk(
        0x00FE,
        (
            '嗯嗯……\n',
            '真让人头痛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '究竟是谁会这么做呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_F1E(): pass

    label('loc_F1E')

    Jump('loc_1427')

    def _loc_F21(): pass

    label('loc_F21')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1059',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1013',
    )

    ChrTalk(
        0x00FE,
        (
            '吉米申请要当\n',
            '研究员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他虽然毫无经验，\n',
            '不过经历很独特，\n',
            '而且观点也很有趣。　　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然要花点时间，\n',
            '不过因为他有潜力，我们还是决定录用他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '各塔的装置和古代遗物……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有很多事要调查，\n',
            '希望他能多多活跃。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_1056')

    def _loc_1013(): pass

    label('loc_1013')

    ChrTalk(
        0x00FE,
        (
            '他似乎对财宝的传言和传说\n',
            '相当地了解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是个很有趣的人才。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1056(): pass

    label('loc_1056')

    Jump('loc_1427')

    def _loc_1059(): pass

    label('loc_1059')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_10E8',
    )

    ChrTalk(
        0x00FE,
        (
            '塔的调查、研究和送来的\n',
            '古代遗物的解析……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有很多事要做，\n',
            '人手实在不足啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还好预算充裕，\n',
            '要商量一下增加研究员的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1427')

    def _loc_10E8(): pass

    label('loc_10E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_120E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_11B3',
    )

    ChrTalk(
        0x00FE,
        (
            '我让卡兰大主教看了，\n',
            '他说被送来的古代遗物\n',
            '留在资料馆也没关系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '古代遗物很可能和古代\n',
            '塞姆里亚文明有关……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '能够把它作为研究对象\n',
            '我也很期待啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这也要感谢吉米。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_120B')

    def _loc_11B3(): pass

    label('loc_11B3')

    ChrTalk(
        0x00FE,
        (
            '古代遗物很可能和古代\n',
            '塞姆里亚文明有关……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '能够把它作为研究对象\n',
            '我也很期待啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_120B(): pass

    label('loc_120B')

    Jump('loc_1427')

    def _loc_120E(): pass

    label('loc_120E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_129B',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然还有能量的古代遗物\n',
            '必须交给七耀教会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过这次送来的\n',
            '已经完全丧失了功能。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之先跟七耀教会\n',
            '打声招呼再收藏吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1427')

    def _loc_129B(): pass

    label('loc_129B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_1427',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_13C2',
    )

    ChrTalk(
        0x00FE,
        (
            '以前暂居此地的\n',
            '亚鲁瓦教授真了不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '知识自不必说，\n',
            '他那关于『七至宝』的\n',
            '假说也非常有魅力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真想听听他对\n',
            '古代遗迹之塔上\n',
            '启动的神秘装置的见解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为他好像遍游过\n',
            '那４座塔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F（………………亚鲁瓦教授？）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1003F（咦……那是谁……\n',
            ' 好像听说过……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_1427')

    def _loc_13C2(): pass

    label('loc_13C2')

    ChrTalk(
        0x00FE,
        (
            '以前暂居此地的\n',
            '亚鲁瓦教授真了不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '关于古代遗迹之塔上\n',
            '启动的神秘装置，\n',
            '真想听听他的见解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1427(): pass

    label('loc_1427')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x142B
@scena.Code('func_06_142B')
def func_06_142B():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_14E9',
    )

    ChrTalk(
        0x00FE,
        (
            '我们正在研究的各地的\n',
            '塔似乎发生了奇怪的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '塔顶被黑色的东西包着，\n',
            '不过不久又恢复原样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那到底是什么呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对了，导力停止是发生在\n',
            '塔的异变完全结束之后啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AE8')

    def _loc_14E9(): pass

    label('loc_14E9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1566',
    )

    ChrTalk(
        0x00FE,
        (
            '在塞姆里亚时期\n',
            '还有龙生存着呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对了，以前我读过以前\n',
            '研究龙的人的报告。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '应该是一个住在\n',
            '柏斯的人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AE8')

    def _loc_1566(): pass

    label('loc_1566')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_1648',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 0, 0x1630)),
            Expr.Return,
        ),
        'loc_15C4',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才有个穿白色礼服的\n',
            '女孩子一个人在参观……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……不知是不是迷路了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1645')

    def _loc_15C4(): pass

    label('loc_15C4')

    ChrTalk(
        0x00FE,
        (
            '那个持有古代遗物的\n',
            '青年挺有意思的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不愧是找寻过宝藏的人，\n',
            '拥有考古和挖掘的潜质。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然他偶尔会说些\n',
            '不知所云的话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1645(): pass

    label('loc_1645')

    Jump('loc_1AE8')

    def _loc_1648(): pass

    label('loc_1648')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_16C7',
    )

    ChrTalk(
        0x00FE,
        (
            '唔……\n',
            '研究停滞不前了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样下去的话，\n',
            '赶不上结果发表了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是亚鲁瓦教授在，\n',
            '就能和他谈谈了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AE8')

    def _loc_16C7(): pass

    label('loc_16C7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_1725',
    )

    ChrTalk(
        0x00FE,
        (
            '成为塞姆里亚文明消亡\n',
            '契机的『大崩坏』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说不定和塔的装置\n',
            '有某种联系……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AE8')

    def _loc_1725(): pass

    label('loc_1725')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_1AE8',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0066, 0x00, 0x10)"),
            (Expr.TestScenaFlags, ScenaFlag(0x02C9, 0, 0x1648)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_196C',
    )

    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '哎呀……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1004F好、好象见过你……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1008F……你是谁？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x00FE,
        (
            '唉！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈……我是在卢安委托\n',
            '你们上塔拍照的森特啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1008F哦，对对。\n',
            '我没忘记你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1000F后来怎么样了？\n',
            '有没有了解到什么关于塔的装置的情况？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不……惭愧，\n',
            '还没什么重要发现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之不管从什么角度来看，\n',
            '不明的地方还是太多了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只知道塔本身是在\n',
            '塞姆里亚时期建造的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只能先从这点上\n',
            '来解析资料了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F呼，考古学的结论也\n',
            '不是那么容易就做的出呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1011F我只能为你\n',
            '加油了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，这是探索遗失的古代睿智的\n',
            '第一步，我会努力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x02C9, 0, 0x1648))

    Jump('loc_1AE8')

    def _loc_196C(): pass

    label('loc_196C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A63',
    )

    ChrTalk(
        0x00FE,
        (
            '在古代遗迹之塔启动的神秘装置……\n',
            '我的工作就是调查这个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '装置被安在遗迹塔的塔顶，\n',
            '作用完全不明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '研究还在进行，\n',
            '不过还没什么重要的发现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只知道塔本身是在\n',
            '塞姆里亚时期建造的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只能先好好从这点上\n',
            '来解析资料了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_1AE8')

    def _loc_1A63(): pass

    label('loc_1A63')

    ChrTalk(
        0x00FE,
        (
            '只知道塔本身是在\n',
            '塞姆里亚时期建造的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只能先好好从这点上\n',
            '来解析资料了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这是探索遗失的古代睿智的\n',
            '第一步，我会努力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AE8(): pass

    label('loc_1AE8')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x1AEC
@scena.Code('func_07_1AEC')
def func_07_1AEC():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1BA9',
    )

    ChrTalk(
        0x00FE,
        (
            '就算不能用导力器，\n',
            '也可以看着古代遗迹想象一下啊，\n',
            '这样就可以使得思想插上翅膀了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '考古学在任何困境中\n',
            '都能继续。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哇～这才是男人的浪漫！\n',
            '我不会这么容易就被击倒的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21A6')

    def _loc_1BA9(): pass

    label('loc_1BA9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1C1E',
    )

    ChrTalk(
        0x00FE,
        (
            '哇～我被这座历史资料馆\n',
            '雇用了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对我来说就像是拿着工资\n',
            '来寻找宝藏。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我真是开心得\n',
            '要发狂了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21A6')

    def _loc_1C1E(): pass

    label('loc_1C1E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_1D8C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 0, 0x1630)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 1, 0x1631)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1D14',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1C7B',
    )

    ChrTalk(
        0x00FE,
        (
            '穿白色礼服的女孩子？\n',
            '刚才还在这里的，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '应该还没\n',
            '走远。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D11')

    def _loc_1C7B(): pass

    label('loc_1C7B')

    ChrTalk(
        0x00FE,
        (
            '……穿白衣服的女孩子？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00FE, 180, 400)

    ChrTalk(
        0x00FE,
        (
            '她应该是在那……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '哇～？ 不见了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x00F6, 400)

    ChrTalk(
        0x00FE,
        (
            '不过刚才确实在的，\n',
            '应该还没走远。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_1D11(): pass

    label('loc_1D11')

    Jump('loc_1D89')

    def _loc_1D14(): pass

    label('loc_1D14')

    ChrTalk(
        0x00FE,
        (
            '哇～钱也没了，\n',
            '得回卢安了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过我在这儿找到了\n',
            '男人的新浪漫——考古学……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '感觉就这样回去\n',
            '有点浪费了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1D89(): pass

    label('loc_1D89')

    Jump('loc_21A6')

    def _loc_1D8C(): pass

    label('loc_1D8C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1E1A',
    )

    ChrTalk(
        0x00FE,
        (
            '哇～这儿真了不起！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '想不到古代还有这种东西……\n',
            '完全可以称为人类的宝藏。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……莫非考古学是更\n',
            '胜于寻宝的男人的浪漫？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21A6')

    def _loc_1E1A(): pass

    label('loc_1E1A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_1E7D',
    )

    ChrTalk(
        0x00FE,
        (
            '那东西我已经交给馆长了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他们在研究是不是能由资料馆收藏，\n',
            '我在一边参观一边等。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21A6')

    def _loc_1E7D(): pass

    label('loc_1E7D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_21A6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C9, 1, 0x1649)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_215D',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0071, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_2058',
    )

    ChrTalk(
        0x00FE,
        (
            '历史资料馆……\n',
            '嗯，应该就是这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F咦？这不是吉米先生吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊？　对了，你是\n',
            '在蔡斯救过我的游击士吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F你在这里干什么啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '哦，对了……你是来\n',
            '那个古代遗物的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是啊，就算失去了力量，不过\n',
            '还是不知道这东西会引起什么事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我打算放在这里委托他们调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F是吗，很好很好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '如果你能顺便放弃寻宝而\n',
            '认真工作的话就更了不起了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哇，你嘴好厉害……\n',
            '不过那是没的商量的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '除非我能找到比\n',
            '寻宝更浪漫的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2157')

    def _loc_2058(): pass

    label('loc_2058')

    ChrTalk(
        0x00FE,
        (
            '历史资料馆……\n',
            '嗯，应该没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里一定能保管\n',
            '东西应该会留下来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F古代遗物！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那如果是真东西的话\n',
            '得送去七耀教会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哇～是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过这已经\n',
            '失去了力量。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之希望他们查一下，\n',
            '调查，就过来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F哦，原来如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2157(): pass

    label('loc_2157')

    SetScenaFlags(ScenaFlag(0x02C9, 1, 0x1649))

    Jump('loc_21A6')

    def _loc_215D(): pass

    label('loc_215D')

    ChrTalk(
        0x00FE,
        (
            '准备让他们帮我\n',
            '调查失去了力量的古代遗物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '首先得去见负责人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_21A6(): pass

    label('loc_21A6')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x21AA
@scena.Code('func_08_21AA')
def func_08_21AA():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_2222',
    )

    ChrTalk(
        0x00FE,
        (
            '#0070250430V#060F能发明接近这种原理的\n',
            '东西的人真了不起。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070250431V我也想有一天\n',
            '能发明这样的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2322')

    def _loc_2222(): pass

    label('loc_2222')

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '#0070250432V#560F啊，姐姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070250433V#060F纺车虽然结构很简单，\n',
            '不过却浓缩着很多发明在里面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070250434V能发明接近这种原理的\n',
            '东西的人真了不起。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070250435V#061F我也想有一天\n',
            '能发明这样的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250436V#1016F（又开始了啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    def _loc_2322(): pass

    label('loc_2322')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x2326
@scena.Code('func_09_2326')
def func_09_2326():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_2389',
    )

    ChrTalk(
        0x00FE,
        (
            '#0220250437V#267F提妲一见到机器\n',
            '就会立即忘乎所以。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220250438V一直是这样的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2422')

    def _loc_2389(): pass

    label('loc_2389')

    ChrTalk(
        0x00FE,
        (
            '#0220250439V#266F提妲一见到机器\n',
            '就会立即忘乎所以。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220250440V#267F一直是这样的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250441V#1016F对、对不起。\n',
            '她可能一直是这样的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_2422(): pass

    label('loc_2422')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x2426
@scena.Code('func_0A_2426')
def func_0A_2426():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '女王陛下让这里\n',
            '免费开放了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '小孩子也稍微\n',
            '恢复了一些活力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x2473
@scena.Code('func_0B_2473')
def func_0B_2473():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '这东西就算没导力\n',
            '也能使用吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x249D
@scena.Code('func_0C_249D')
def func_0C_249D():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '哈哈，这设计\n',
            '真独特……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x24C1
@scena.Code('func_0D_24C1')
def func_0D_24C1():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '哟，以前是用\n',
            '这样的东西的啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果导力就一直不恢复的话\n',
            '就要回到使用这个的时代了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x252A
@scena.Code('func_0E_252A')
def func_0E_252A():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '我是为了调节心情\n',
            '才来的这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望一切都能\n',
            '快点恢复原状……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x2577
@scena.Code('func_0F_2577')
def func_0F_2577():
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
        'loc_258E',
    )

    Call(0, 0x001B)
    Call(0, 0x001C)

    def _loc_258E(): pass

    label('loc_258E')

    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x00F7, 0x0080)
    ChrSetFlags(0x0107, 0x0080)
    ChrSetFlags(0x00F9, 0x0080)
    CameraMove(1000, 4000, 8000, 0)
    OP_67(0, 5500, -10000, 0)
    CameraSetDistance(1900, 0)
    OP_6C(45000, 0)
    OP_6E(502, 0)

    @scena.Lambda('lambda_25E5')
    def lambda_25E5():
        CameraMove(1000, 4000, -2000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_25E5)

    FadeIn(2000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0000)
    Fade(1000)
    CameraMove(550, 0, -5250, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    CreateThread(0x0101, 0x01, 0x00, func_11_2FD4)
    Sleep(500)

    CreateThread(0x0107, 0x01, 0x00, func_12_301C)
    Sleep(500)

    CreateThread(0x00F7, 0x01, 0x00, func_13_3064)
    Sleep(500)

    CreateThread(0x00F9, 0x01, 0x00, func_14_30AC)
    WaitForThreadExit(0x00F9, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010260601V#1015F#5P我记得你说昨天\n',
            '也路过这里的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070260602V#067F#1P嗯，只是眺望了\n',
            '一下而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4A(0x0008, 255)

    ChrTalk(
        0x0008,
        (
            '#3200260603V#3P欢迎。\n',
            '您是游客吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2717')
    def lambda_2717():
        CameraMove(2500, 0, -5250, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2717)

    @scena.Lambda('lambda_272F')
    def lambda_272F():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_272F)

    Sleep(100)

    @scena.Lambda('lambda_2742')
    def lambda_2742():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_2742)

    Sleep(100)

    @scena.Lambda('lambda_2755')
    def lambda_2755():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_2755)

    Sleep(100)

    @scena.Lambda('lambda_2768')
    def lambda_2768():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_2768)

    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010260604V#1016F#1P嗯，我们在\n',
            '找人……',
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
            '向接待处的女性说明了玲的外貌特征。',
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
            '#3200260605V啊，就是昨天\n',
            '那边的这位小姐在一起的\n',
            '穿白色礼服的小姐吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070260606V#560F#1P啊，应该是的\n',
            '你还记得吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3200260607V呵呵，因为两位小姐\n',
            '很惹人注目。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3200260608V很遗憾，今天\n',
            '她没来过这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260609V#1015F#1P这样啊……\n',
            '可能在别的地方。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260610V#1006F如果那孩子来了的话\n',
            '能不能请你传口信\n',
            '让她回协会？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3200260611V好的，我明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x0008, 255)
    SetScenaFlags(ScenaFlag(0x02C5, 7, 0x162F))
    OP_28(0x008C, 0x01, 0x0002)
    EventEnd(0x00)

    Return()

# id: 0x0010 offset: 0x297B
@scena.Code('func_10_297B')
def func_10_297B():
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
        'loc_2992',
    )

    Call(0, 0x001B)
    Call(0, 0x001C)

    def _loc_2992(): pass

    label('loc_2992')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2A47',
    )

    FadeOut(0, 0, -1)

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
            TXT(0x00, '【◇没看到『在历史资料馆听玲说话１』】\n'),
            TXT(0x01, '【◇已看到『在历史资料馆听玲说话１』】\n'),
            TXT(0x02, '【◇什么也没有变更】\n'),
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
        (0x00000000, 'loc_2A3B'),
        (0x00000001, 'loc_2A41'),
        (-1, 'loc_2A47'),
    )

    def _loc_2A3B(): pass

    label('loc_2A3B')

    ClearScenaFlags(ScenaFlag(0x02C5, 7, 0x162F))

    Jump('loc_2A47')

    def _loc_2A41(): pass

    label('loc_2A41')

    SetScenaFlags(ScenaFlag(0x02C5, 7, 0x162F))

    Jump('loc_2A47')

    def _loc_2A47(): pass

    label('loc_2A47')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 7, 0x162F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2DC1',
    )

    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x00F7, 0x0080)
    ChrSetFlags(0x0107, 0x0080)
    ChrSetFlags(0x00F9, 0x0080)
    CameraMove(1000, 4000, 8000, 0)
    OP_67(0, 5500, -10000, 0)
    CameraSetDistance(1900, 0)
    OP_6C(45000, 0)
    OP_6E(502, 0)

    @scena.Lambda('lambda_2AA6')
    def lambda_2AA6():
        CameraMove(1000, 4000, -2000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2AA6)

    FadeIn(2000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0000)
    Fade(1000)
    CameraMove(550, 0, -5250, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    CreateThread(0x0101, 0x01, 0x00, func_11_2FD4)
    Sleep(500)

    CreateThread(0x0107, 0x01, 0x00, func_12_301C)
    Sleep(500)

    CreateThread(0x00F7, 0x01, 0x00, func_13_3064)
    Sleep(500)

    CreateThread(0x00F9, 0x01, 0x00, func_14_30AC)
    WaitForThreadExit(0x00F9, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010260601V#1015F#5P我记得你说昨天\n',
            '也路过这里的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070260602V#067F#1P嗯，只是眺望了\n',
            '一下而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4A(0x0008, 255)

    ChrTalk(
        0x0008,
        (
            '#3200260603V#3P你好。\n',
            '您是游客吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2BD9')
    def lambda_2BD9():
        CameraMove(2500, 0, -5250, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2BD9)

    @scena.Lambda('lambda_2BF1')
    def lambda_2BF1():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2BF1)

    Sleep(100)

    @scena.Lambda('lambda_2C04')
    def lambda_2C04():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_2C04)

    Sleep(100)

    @scena.Lambda('lambda_2C17')
    def lambda_2C17():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_2C17)

    Sleep(100)

    @scena.Lambda('lambda_2C2A')
    def lambda_2C2A():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_2C2A)

    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010260627V#1006F#1P嗯，我们在\n',
            '找人……',
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
            '向接待处的女性说明了玲的外貌特征。',
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
            '#3200260605V啊，就是昨天\n',
            '那边的这位小姐在一起的\n',
            '穿白色礼服的小姐吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070260606V#560F#1P啊，应该是的\n',
            '你还记得吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3200260607V呵呵，因为两位小姐\n',
            '很惹人注目。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3200260631V如果说的是那位小姐\n',
            '刚才已经来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3200260632V我想她应该\n',
            '还在馆内。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F3B')

    def _loc_2DC1(): pass

    label('loc_2DC1')

    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x00F7, 0x0080)
    ChrSetFlags(0x0107, 0x0080)
    ChrSetFlags(0x00F9, 0x0080)
    CameraMove(550, 0, -5250, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(2000, 0)
    Sleep(1000)

    CreateThread(0x0101, 0x01, 0x00, func_11_2FD4)
    Sleep(500)

    CreateThread(0x0107, 0x01, 0x00, func_12_301C)
    Sleep(500)

    CreateThread(0x00F7, 0x01, 0x00, func_13_3064)
    Sleep(500)

    OP_4A(0x0008, 255)
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    CreateThread(0x00F9, 0x01, 0x00, func_14_30AC)
    WaitForThreadExit(0x00F9, 0x0001)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#3200260633V啊，尊敬的顾客。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2E8F')
    def lambda_2E8F():
        CameraMove(2500, 0, -5250, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2E8F)

    @scena.Lambda('lambda_2EA7')
    def lambda_2EA7():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2EA7)

    Sleep(100)

    @scena.Lambda('lambda_2EBA')
    def lambda_2EBA():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_2EBA)

    Sleep(100)

    @scena.Lambda('lambda_2ECD')
    def lambda_2ECD():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_2ECD)

    Sleep(100)

    @scena.Lambda('lambda_2EE0')
    def lambda_2EE0():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_2EE0)

    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0008,
        (
            '#3200260634V那位小姐\n',
            '小姐来过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3200260632V我想她应该\n',
            '还在馆内。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2F3B(): pass

    label('loc_2F3B')

    ChrTalk(
        0x0101,
        (
            '#0010260636V#1006F#1P哦，这样啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2F97',
    )

    ChrTalk(
        0x0106,
        (
            '#0050260637V#051F#6P好。\n',
            '赶紧抓住她。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2FC4')

    def _loc_2F97(): pass

    label('loc_2F97')

    ChrTalk(
        0x0103,
        (
            '#0030260638V#021F#6P呵呵，终于\n',
            '逮到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2FC4(): pass

    label('loc_2FC4')

    OP_4B(0x0008, 255)
    SetScenaFlags(ScenaFlag(0x02C6, 0, 0x1630))
    OP_28(0x008C, 0x01, 0x0008)
    EventEnd(0x00)

    Return()

# id: 0x0011 offset: 0x2FD4
@scena.Code('func_11_2FD4')
def func_11_2FD4():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, 0, -250, -9500, 0)

    @scena.Lambda('lambda_2FFB')
    def lambda_2FFB():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2FFB)

    ChrWalkTo(0x00FE, 350, 0, -5050, 2000, 0x00)

    Return()

# id: 0x0012 offset: 0x301C
@scena.Code('func_12_301C')
def func_12_301C():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, 0, -250, -9500, 0)

    @scena.Lambda('lambda_3043')
    def lambda_3043():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3043)

    ChrWalkTo(0x00FE, -680, 0, -5140, 2000, 0x00)

    Return()

# id: 0x0013 offset: 0x3064
@scena.Code('func_13_3064')
def func_13_3064():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, 0, -250, -9500, 0)

    @scena.Lambda('lambda_308B')
    def lambda_308B():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_308B)

    ChrWalkTo(0x00FE, 230, 0, -6560, 2000, 0x00)

    Return()

# id: 0x0014 offset: 0x30AC
@scena.Code('func_14_30AC')
def func_14_30AC():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, 0, -250, -9500, 0)

    @scena.Lambda('lambda_30D3')
    def lambda_30D3():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_30D3)

    ChrWalkTo(0x00FE, -840, 0, -6560, 2000, 0x00)

    Return()

# id: 0x0015 offset: 0x30F4
@scena.Code('func_15_30F4')
def func_15_30F4():
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
        'loc_310B',
    )

    Call(0, 0x001B)
    Call(0, 0x001C)

    def _loc_310B(): pass

    label('loc_310B')

    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x00F7, 0x0080)
    ChrSetFlags(0x0107, 0x0080)
    ChrSetFlags(0x00F9, 0x0080)
    OP_4A(0x0008, 255)

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000067, 'loc_3133'),
        (0x00000068, 'loc_3173'),
        (-1, 'loc_31B3'),
    )

    def _loc_3133(): pass

    label('loc_3133')

    CameraMove(-5980, 4000, 5800, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    Jump('loc_31B3')

    def _loc_3173(): pass

    label('loc_3173')

    CameraMove(5990, 4000, 5800, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    Jump('loc_31B3')

    def _loc_31B3(): pass

    label('loc_31B3')

    FadeIn(2000, 0)
    CreateThread(0x0101, 0x01, 0x00, func_16_353F)
    Sleep(400)

    CreateThread(0x0107, 0x01, 0x00, func_17_35AE)
    Sleep(500)

    CreateThread(0x00F7, 0x01, 0x00, func_18_361D)
    Sleep(300)

    CreateThread(0x00F9, 0x01, 0x00, func_19_368C)
    WaitForThreadExit(0x00F9, 0x0001)
    OP_0D()
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, 2600, 0, -5900, 90)

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000067, 'loc_3213'),
        (0x00000068, 'loc_3222'),
        (-1, 'loc_3225'),
    )

    def _loc_3213(): pass

    label('loc_3213')

    ChrTurnDirection(0x0101, 0x0011, 400)
    Sleep(500)

    Jump('loc_3225')

    def _loc_3222(): pass

    label('loc_3222')

    Jump('loc_3225')

    def _loc_3225(): pass

    label('loc_3225')

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010260639V#1004F#6P咦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CameraMove(2500, 0, -5250, 2000)

    ChrTalk(
        0x0011,
        (
            '#0220260640V#1306F#6P我说，姐姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220260641V你知道哪儿有\n',
            '没有颜色的鱼吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3200260642V咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0220260643V#263F#6P呵呵，再见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0011, 0x01, 0x00, func_1A_36FB)
    Sleep(500)

    @scena.Lambda('lambda_3313')
    def lambda_3313():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_3313')

    DispatchAsync2(0x0008, 0x0001, lambda_3313)

    ChrTalk(
        0x0008,
        (
            '#3200260644V啊……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(2000)

    ChrTalk(
        0x0008,
        (
            '#3200260645V#5P喂，小姐！\n',
            '有你认识的人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0011, 0x0001)
    Sleep(1000)

    ChrSetPos(0x0101, -840, 1270, 3460, 0)
    ChrSetPos(0x0107, 230, 1270, 3460, 0)
    ChrSetPos(0x00F7, -680, 1270, 3460, 0)
    ChrSetPos(0x00F9, 350, 1270, 3460, 0)

    @scena.Lambda('lambda_33BF')
    def lambda_33BF():
        ChrWalkTo(0x00FE, -840, 0, -5250, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_33BF)

    Sleep(100)

    @scena.Lambda('lambda_33DF')
    def lambda_33DF():
        ChrWalkTo(0x00FE, 230, 0, -5560, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_33DF)

    Sleep(500)

    @scena.Lambda('lambda_33FF')
    def lambda_33FF():
        ChrWalkTo(0x00FE, -680, 0, -4050, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_33FF)

    Sleep(100)

    @scena.Lambda('lambda_341F')
    def lambda_341F():
        ChrWalkTo(0x00FE, 350, 0, -4050, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_341F)

    WaitForThreadExit(0x00F9, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010260646V#1020F#5P等、等等，玲！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070260647V#065F#5P小玲，等等！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)

    @scena.Lambda('lambda_3498')
    def lambda_3498():
        ChrWalkTo(0x00FE, 0, -250, -9500, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3498)

    Sleep(300)

    @scena.Lambda('lambda_34B8')
    def lambda_34B8():
        ChrWalkTo(0x00FE, 0, -250, -9500, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_34B8)

    Sleep(300)

    @scena.Lambda('lambda_34D8')
    def lambda_34D8():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_34D8)

    @scena.Lambda('lambda_34EA')
    def lambda_34EA():
        ChrWalkTo(0x00FE, 0, -250, -9500, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_34EA)

    Sleep(300)

    @scena.Lambda('lambda_350A')
    def lambda_350A():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0002, lambda_350A)

    @scena.Lambda('lambda_351C')
    def lambda_351C():
        ChrWalkTo(0x00FE, 0, -250, -9500, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_351C)

    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/T4101._SN', 102, 0, 0)
    IdleLoop()

    Return()

# id: 0x0016 offset: 0x353F
@scena.Code('func_16_353F')
def func_16_353F():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrClearFlags(0x00FE, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000067, 'loc_355F'),
        (0x00000068, 'loc_3573'),
        (-1, 'loc_3587'),
    )

    def _loc_355F(): pass

    label('loc_355F')

    ChrSetPos(0x00FE, -5150, 6550, 10500, 180)

    Jump('loc_3587')

    def _loc_3573(): pass

    label('loc_3573')

    ChrSetPos(0x00FE, 5340, 6550, 10500, 180)

    Jump('loc_3587')

    def _loc_3587(): pass

    label('loc_3587')

    @scena.Lambda('lambda_358D')
    def lambda_358D():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_358D)

    ChrMoveToRelative(0x00FE, 0, 0, -4000, 2000, 0x00)

    Return()

# id: 0x0017 offset: 0x35AE
@scena.Code('func_17_35AE')
def func_17_35AE():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrClearFlags(0x00FE, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000067, 'loc_35CE'),
        (0x00000068, 'loc_35E2'),
        (-1, 'loc_35F6'),
    )

    def _loc_35CE(): pass

    label('loc_35CE')

    ChrSetPos(0x00FE, -6400, 6540, 10480, 180)

    Jump('loc_35F6')

    def _loc_35E2(): pass

    label('loc_35E2')

    ChrSetPos(0x00FE, 6600, 6550, 10500, 180)

    Jump('loc_35F6')

    def _loc_35F6(): pass

    label('loc_35F6')

    @scena.Lambda('lambda_35FC')
    def lambda_35FC():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_35FC)

    ChrMoveToRelative(0x00FE, 0, 0, -3900, 2000, 0x00)

    Return()

# id: 0x0018 offset: 0x361D
@scena.Code('func_18_361D')
def func_18_361D():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrClearFlags(0x00FE, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000067, 'loc_363D'),
        (0x00000068, 'loc_3651'),
        (-1, 'loc_3665'),
    )

    def _loc_363D(): pass

    label('loc_363D')

    ChrSetPos(0x00FE, -5150, 6550, 10500, 180)

    Jump('loc_3665')

    def _loc_3651(): pass

    label('loc_3651')

    ChrSetPos(0x00FE, 5340, 6550, 10500, 180)

    Jump('loc_3665')

    def _loc_3665(): pass

    label('loc_3665')

    @scena.Lambda('lambda_366B')
    def lambda_366B():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_366B)

    ChrMoveToRelative(0x00FE, 0, 0, -2500, 2000, 0x00)

    Return()

# id: 0x0019 offset: 0x368C
@scena.Code('func_19_368C')
def func_19_368C():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrClearFlags(0x00FE, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000067, 'loc_36AC'),
        (0x00000068, 'loc_36C0'),
        (-1, 'loc_36D4'),
    )

    def _loc_36AC(): pass

    label('loc_36AC')

    ChrSetPos(0x00FE, -6400, 6540, 10480, 180)

    Jump('loc_36D4')

    def _loc_36C0(): pass

    label('loc_36C0')

    ChrSetPos(0x00FE, 6600, 6550, 10500, 180)

    Jump('loc_36D4')

    def _loc_36D4(): pass

    label('loc_36D4')

    @scena.Lambda('lambda_36DA')
    def lambda_36DA():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_36DA)

    ChrMoveToRelative(0x00FE, 0, 0, -2400, 2000, 0x00)

    Return()

# id: 0x001A offset: 0x36FB
@scena.Code('func_1A_36FB')
def func_1A_36FB():
    ChrSetDirection(0x00FE, 225, 400)
    ChrWalkTo(0x00FE, 0, 0, -7500, 2000, 0x00)
    ChrWalkTo(0x00FE, 0, 0, -8390, 2000, 0x00)

    @scena.Lambda('lambda_3730')
    def lambda_3730():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3730)

    ChrWalkTo(0x00FE, 0, -250, -9500, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x001B offset: 0x3756
@scena.Code('func_1B_3756')
def func_1B_3756():
    FadeOut(0, 0, -1)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x09, 0xFF)

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
        (0x00000000, 'loc_37D3'),
        (0x00000001, 'loc_37D9'),
        (-1, 'loc_37DF'),
    )

    def _loc_37D3(): pass

    label('loc_37D3')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_37DF')

    def _loc_37D9(): pass

    label('loc_37D9')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_37DF')

    def _loc_37DF(): pass

    label('loc_37DF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_37ED',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_37F1')

    def _loc_37ED(): pass

    label('loc_37ED')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_37F1(): pass

    label('loc_37F1')

    Return()

# id: 0x001C offset: 0x37F2
@scena.Code('func_1C_37F2')
def func_1C_37F2():
    MapClearFlags(0x00000001)
    CameraMove(106730, -1920, 53920, 0)
    Sleep(100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_3831',
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
            ChrTable['科洛丝'],
            ChrTable['金'],
            0xFFFF,
        ),
    )

    Jump('loc_384B')

    def _loc_3831(): pass

    label('loc_3831')

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
            ChrTable['科洛丝'],
            ChrTable['金'],
            0xFFFF,
        ),
    )

    def _loc_384B(): pass

    label('loc_384B')

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

# id: 0x001D offset: 0x386B
@scena.Code('func_1D_386B')
def func_1D_386B():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '【『四轮之塔』的外壁】\n',
            '　　　　　　　　　　　年代：七耀历以前？\n',
            '　　这块朴素的石壁，是从『大崩坏』后所建\n',
            '的『四轮之塔』上作为研究资料切割出来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '其上所绘制的纹样是同时代建筑物中的典型，\n',
            '据说描述的是持杖的祭司、以及展翅的神祗的\n',
            '身姿。关于其与七耀教会成立之后的代表神格\n',
            '『空之女神』的关系，各方面的研究仍在进行\n',
            '中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x001E offset: 0x39DD
@scena.Code('func_1E_39DD')
def func_1E_39DD():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '【七耀历１１５０～１２００年\n',
            '　　　　　　　～导力革命以后的世界～】\n',
            '　　Ｃ·爱普斯泰恩博士发明导力器后仅仅五\n',
            '十年。世界以惊人的速度进步着，接连不断地\n',
            '开拓岀导力技术新的应用领域。堪称其象征的\n',
            '就是飞船。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　　利贝尔王国定期飞船的运航已经成为国民\n',
            '们习以为常的交通方式，近年来埃雷波尼亚帝\n',
            '国等其他国家也开始正式引进飞船制造业，使\n',
            '得飞船级的船体逐步实用化。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x001F offset: 0x3B74
@scena.Code('func_1F_3B74')
def func_1F_3B74():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '【七耀历以前\n',
            '　　　　　～古代塞姆里亚文明～】\n',
            '　　距今约１２００年前，当时繁荣绝顶的塞\n',
            '姆里亚文明突然迎来了终结，失去了文明的人\n',
            '们开始度过漫长的暗黑时代。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　　第一层的展示物据考证是『大崩坏』之后\n',
            '所制造的遗物。虽然据判断并非古代文明的直\n',
            '接遗物，但因受到其深刻影响，学术方面的价\n',
            '值极高。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0020 offset: 0x3CCA
@scena.Code('func_20_3CCA')
def func_20_3CCA():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '【古代的照明器具】\n',
            '　　　　　　　　　　　年代：七耀历以前？\n',
            '　　专用于焚烧篝火的容器。在塔之类被认为\n',
            '与祭祀仪式有关联的建筑物中频繁被使用，其\n',
            '具体用途不仅仅是照明，在宗教上可能也拥有\n',
            '某种程度的意义。当然这点目前还只是推测罢\n',
            '了。  ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0021 offset: 0x3DE3
@scena.Code('func_21_3DE3')
def func_21_3DE3():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '【浮雕石柱】\n',
            '　　　　　　　　　　　年代：七耀历以前？\n',
            '　　刻有优美雕刻的石柱。在瓦雷利亚湖的湖\n',
            '底被打捞上来，可以看出与『四轮之塔』的壁\n',
            '画类似的纹样在其上也被反复使用。\n',
            '　　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0022 offset: 0x3EC3
@scena.Code('func_22_3EC3')
def func_22_3EC3():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '【瓷工艺的地板】\n',
            '　　　　　　　　　　　年代：七耀历以前？\n',
            '　　遗迹内部彩色镶嵌的瓷工艺地板。将破碎\n',
            '的天然石块巧妙拼接，作出朴素而美妙的花纹\n',
            '样式。\n',
            '　　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0023 offset: 0x3F8D
@scena.Code('func_23_3F8D')
def func_23_3F8D():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '【七耀历１～５００年左右\n',
            '　　　　　　　　～暗黑时代的到来～】\n',
            '　　由于『大崩坏』而导致文明尽失，世界陷\n',
            '入了长期的混乱时代。\n',
            '　　大小各异的国家、势力使得无尽的战争持\n',
            '续了约５００年间，后世称此时代为『暗黑时\n',
            '代』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0024 offset: 0x4094
@scena.Code('func_24_4094')
def func_24_4094():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '【骑士们的武具】\n',
            '　　　　　　　　年代：七耀历５００年左右\n',
            '　　日夜征战的时代中，战士们的集团拥有社\n',
            '会性的强大影响力，最终成长为特权的骑士阶\n',
            '级。\n',
            '　　他们佩戴着如展品所示的武具投身沙场，\n',
            '获得战利品和领土，势力不断扩大。\n',
            '　　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0025 offset: 0x41A6
@scena.Code('func_25_41A6')
def func_25_41A6():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '【七耀历５００～１１００年左右\n',
            '　　　　　　～七耀教会带来的安定期～】\n',
            '　　七耀教会登上历史舞台，正值暗黑时代末\n',
            '期，七耀历５００年左右。\n',
            '　　以『空之女神』为中心所整理的教义，通\n',
            '过教会救济民众的社会活动，瞬间深入人心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　　它的权威很快成长到连贵族、骑士阶级也\n',
            '无法忽视的地步，其后以教会为中心的新秩序\n',
            '便逐步形成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0026 offset: 0x4318
@scena.Code('func_26_4318')
def func_26_4318():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '【古代文明的遗物——\n',
            '　　　　　　　　『古代遗产』】\n',
            '　　　　　　　　　　　　　　　年代：不明\n',
            '　　『古代遗产』是从各地发现的古代遗迹中\n',
            '出土的诸如器物、杖等形态各异、不可思议的\n',
            '遗物。\n',
            '　　在七耀教会的教义中，作为与女神赐予的\n',
            '『七至宝』相关的物品，其回收成为教会必须\n',
            '履行的义务之一。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '展品的『古代遗产』也是教\n',
            '会所回收的物品。\n',
            '　　许多传闻称其拥有超常的力量，但此展品\n',
            '已经失去能力，无法启动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0027 offset: 0x44D4
@scena.Code('func_27_44D4')
def func_27_44D4():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '【七耀教会的祭具】\n',
            '　　　　　　　　年代：七耀历９００年左右\n',
            '　　七耀教会创造岀种种的宗教艺术，由此开\n',
            '始教会开拓出一个稳定的时代。据考证，『空\n',
            '之女神』的圣像也是由此时起被塑造为现今的\n',
            '姿态。此外，现在所使用的祭祀道具多数也是\n',
            '在这个时代被定型的。\n',
            '　　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0028 offset: 0x4600
@scena.Code('func_28_4600')
def func_28_4600():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '【七耀教会圣典的抄本】\n',
            '　　　　　　　　年代：七耀历５００年左右\n',
            '　　暗黑时代末期的原始七耀教会所使用的圣\n',
            '典抄本。中世纪没有印刷技术，因此这本书是\n',
            '由人手工抄写在兽皮制的纸张上的。\n',
            '　　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0029 offset: 0x46EA
@scena.Code('func_29_46EA')
def func_29_46EA():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '【中世纪的纺纱机】\n',
            '　　　　　　　　年代：七耀历９００年左右\n',
            '　　纺纱用的手工机械。到了稳定的中世纪，\n',
            '农民的生活逐渐富裕，作为商品作物的棉花栽\n',
            '培日渐繁盛。为了收入货币，这个时代的手工\n',
            '业也开始发展。\n',
            '　　C37259',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

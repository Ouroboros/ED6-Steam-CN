import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3200_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3200   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3200.x'
    header.mapIndex       = 1
    header.bgm            = 15
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
        ('ED6_DT07/CH02430._CH', 'ED6_DT07/CH02430P._CP'),
        ('ED6_DT07/CH02070._CH', 'ED6_DT07/CH02070P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
        ('ED6_DT07/CH01270._CH', 'ED6_DT07/CH01270P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH01160._CH', 'ED6_DT07/CH01160P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01060._CH', 'ED6_DT07/CH01060P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH01153._CH', 'ED6_DT07/CH01153P._CP'),
        ('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP'),
    ]

# id: 0x10001 offset: 0x12A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '毛婆婆',
            x                   = 2590,
            z                   = 250,
            y                   = 5360,
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
            name                = '朵洛希',
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
            name                = '加雷利',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '拜舍尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '艾德',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '林',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '莉西亚',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '希利尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '艾缇',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '拉克',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '希玛',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '库安',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '西加罗',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '艾德尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '东方打扮的男人',
            x                   = 13610,
            z                   = 2500,
            y                   = 16860,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '托兰特平原道方向',
            x                   = -30790,
            z                   = -2000,
            y                   = 15330,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x32A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x32A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 4000,
            y           = 0,
            z           = 18870,
            range       = 7100,
            dword_10    = 0x000007D0,
            dword_14    = 0x00002D82,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000013,
        ),
        ScenaEventData(
            x           = -13210,
            y           = -3000,
            z           = 9240,
            range       = -19510,
            dword_10    = 0x000003E8,
            dword_14    = 0x00005BAE,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000015,
        ),
        ScenaEventData(
            x           = 28950,
            y           = 1000,
            z           = 4030,
            range       = 2500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000001B,
        ),
        ScenaEventData(
            x           = 980,
            y           = -250,
            z           = 18420,
            range       = 1250,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000001C,
        ),
        ScenaEventData(
            x           = 42330,
            y           = 5750,
            z           = 36020,
            range       = 1250,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000001D,
        ),
    )

# id: 0x10004 offset: 0x3CA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 43290,
            triggerZ            = 6250,
            triggerY            = 35890,
            triggerRange        = 800,
            actorX              = 43290,
            actorZ              = 6500,
            actorY              = 35890,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0012,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 40000,
            triggerZ            = 6000,
            triggerY            = 49730,
            triggerRange        = 800,
            actorX              = 40000,
            actorZ              = 7000,
            actorY              = 49730,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0016,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 42130,
            triggerZ            = 0,
            triggerY            = -860,
            triggerRange        = 1250,
            actorX              = 44880,
            actorZ              = 3000,
            actorY              = 1020,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001A,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x436
@scena.Code('Init')
def Init():
    SetScenaFlags(ScenaFlag(0x00BA, 2, 0x5D2))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_447',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_14_263F)

    def _loc_447(): pass

    label('loc_447')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_453'),
        (-1, 'loc_469'),
    )

    def _loc_453(): pass

    label('loc_453')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 4, 0x51C)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 3, 0x51B)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_466',
    )

    SetScenaFlags(ScenaFlag(0x00A3, 4, 0x51C))
    Event(0, func_11_1B5F)

    def _loc_466(): pass

    label('loc_466')

    Jump('loc_469')

    def _loc_469(): pass

    label('loc_469')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_473',
    )

    Jump('loc_4BE')

    def _loc_473(): pass

    label('loc_473')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_49A',
    )

    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, -450, 0, 12380, 180)
    CreateThread(0x000A, 0x00, 0x00, func_03_968)

    Jump('loc_4BE')

    def _loc_49A(): pass

    label('loc_49A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_4BE',
    )

    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, -450, 0, 12380, 180)
    CreateThread(0x000A, 0x00, 0x00, func_03_968)

    def _loc_4BE(): pass

    label('loc_4BE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_519',
    )

    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, 30590, 4500, 35260, 249)
    ChrSetFlags(0x000E, 0x0010)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, 28630, 4000, 36530, 176)
    ChrSetFlags(0x0011, 0x0010)
    ChrClearFlags(0x0013, 0x0080)
    ChrSetPos(0x0013, 28800, 4000, 33220, 0)
    ChrSetFlags(0x0013, 0x0010)

    Jump('loc_71C')

    def _loc_519(): pass

    label('loc_519')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_565',
    )

    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, 11420, 2000, 14520, 273)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, 9750, 2000, 15450, 181)
    ChrClearFlags(0x0013, 0x0080)
    ChrSetPos(0x0013, 9820, 2000, 13580, 351)

    Jump('loc_71C')

    def _loc_565(): pass

    label('loc_565')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_5B6',
    )

    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, 39080, 6000, 47390, 7)
    ChrClearFlags(0x0013, 0x0080)
    ChrSetPos(0x0013, 40560, 6000, 47840, 342)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, 39640, 6000, 44670, 353)
    ChrSetFlags(0x000E, 0x0010)

    Jump('loc_71C')

    def _loc_5B6(): pass

    label('loc_5B6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 2, 0x52A)),
            Expr.Return,
        ),
        'loc_5C5',
    )

    ChrClearFlags(0x0016, 0x0080)

    Jump('loc_71C')

    def _loc_5C5(): pass

    label('loc_5C5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_5CF',
    )

    Jump('loc_71C')

    def _loc_5CF(): pass

    label('loc_5CF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_5EF',
    )

    ChrClearFlags(0x0015, 0x0080)
    ChrSetPos(0x0015, 49070, 2500, -2340, 12)

    Jump('loc_71C')

    def _loc_5EF(): pass

    label('loc_5EF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_625',
    )

    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 17100, 2500, 20360, 180)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, 39080, 6000, 47390, 7)

    Jump('loc_71C')

    def _loc_625(): pass

    label('loc_625')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Return,
        ),
        'loc_671',
    )

    ChrClearFlags(0x0014, 0x0080)
    ChrSetPos(0x0014, 13770, 2500, 18660, 90)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, 17040, 2500, 13580, 0)
    ChrClearFlags(0x0013, 0x0080)
    ChrSetPos(0x0013, 15970, 2500, 13580, 45)

    Jump('loc_71C')

    def _loc_671(): pass

    label('loc_671')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_6D3',
    )

    ChrClearFlags(0x0014, 0x0080)
    ChrSetPos(0x0014, 14240, 2500, 16170, 90)
    ChrClearFlags(0x0015, 0x0080)
    ChrSetPos(0x0015, 14200, 2500, 17020, 90)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, 15630, 2500, 13690, 45)
    ChrClearFlags(0x0013, 0x0080)
    ChrSetPos(0x0013, 17390, 2500, 13750, 0)

    Jump('loc_71C')

    def _loc_6D3(): pass

    label('loc_6D3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_71C',
    )

    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, 12180, 2000, 15020, 270)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, 9850, 2000, 13940, 45)
    ChrClearFlags(0x0013, 0x0080)
    ChrSetPos(0x0013, 10210, 2000, 16010, 135)

    def _loc_71C(): pass

    label('loc_71C')

    Return()

# id: 0x0001 offset: 0x71D
@scena.Code('func_01_71D')
def func_01_71D():
    OP_16(0x02, 4000, -98000, -107000, 196692)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_747',
    )

    OP_B1('t3200_y')

    Jump('loc_750')

    def _loc_747(): pass

    label('loc_747')

    OP_B1('t3200_n')

    def _loc_750(): pass

    label('loc_750')

    OP_72(0x000B, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 6, 0x51E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_765',
    )

    OP_72(0x0003, 0x0010)

    Jump('loc_769')

    def _loc_765(): pass

    label('loc_765')

    OP_64(0x00, 0x0001)

    def _loc_769(): pass

    label('loc_769')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_773',
    )

    Jump('loc_7A7')

    def _loc_773(): pass

    label('loc_773')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_782',
    )

    OP_1B(0x00, 0x00, 0x0019)

    Jump('loc_7A7')

    def _loc_782(): pass

    label('loc_782')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 0, 0x520)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_796',
    )

    OP_1B(0x00, 0x00, 0x0018)

    Jump('loc_7A7')

    def _loc_796(): pass

    label('loc_796')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 5, 0x51D)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7A7',
    )

    OP_1B(0x00, 0x00, 0x0017)

    def _loc_7A7(): pass

    label('loc_7A7')

    If(
        (
            (Expr.GetChrWork, 0x101, 0x1E),
            (Expr.PushLong, 0x11C),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7BB',
    )

    OP_28(0x002A, 0x01, 0x0800)

    def _loc_7BB(): pass

    label('loc_7BB')

    OP_64(0x02, 0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x002E, 0x00, 0x04)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x002E, 0x01, 0x0010)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7DB',
    )

    OP_65(0x02, 0x0001)

    def _loc_7DB(): pass

    label('loc_7DB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7EA',
    )

    StopEffect(0x8D, 0x00)

    def _loc_7EA(): pass

    label('loc_7EA')

    Return()

# id: 0x0002 offset: 0x7EB
@scena.Code('func_02_7EB')
def func_02_7EB():
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
        'loc_810',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_952')

    def _loc_810(): pass

    label('loc_810')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_829',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_952')

    def _loc_829(): pass

    label('loc_829')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_842',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_952')

    def _loc_842(): pass

    label('loc_842')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_85B',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_952')

    def _loc_85B(): pass

    label('loc_85B')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_874',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_952')

    def _loc_874(): pass

    label('loc_874')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_88D',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_952')

    def _loc_88D(): pass

    label('loc_88D')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8A6',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_952')

    def _loc_8A6(): pass

    label('loc_8A6')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8BF',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_952')

    def _loc_8BF(): pass

    label('loc_8BF')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8D8',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_952')

    def _loc_8D8(): pass

    label('loc_8D8')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8F1',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_952')

    def _loc_8F1(): pass

    label('loc_8F1')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_90A',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_952')

    def _loc_90A(): pass

    label('loc_90A')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_923',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_952')

    def _loc_923(): pass

    label('loc_923')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_93C',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_952')

    def _loc_93C(): pass

    label('loc_93C')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_952',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_952(): pass

    label('loc_952')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_967',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_952')

    def _loc_967(): pass

    label('loc_967')

    Return()

# id: 0x0003 offset: 0x968
@scena.Code('func_03_968')
def func_03_968():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_98B',
    )

    OP_8D(0x00FE, 2630, 16300, -3360, 10300, 3000)

    Jump('func_03_968')

    def _loc_98B(): pass

    label('loc_98B')

    Return()

# id: 0x0004 offset: 0x98C
@scena.Code('func_04_98C')
def func_04_98C():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_999',
    )

    Jump('loc_BEA')

    def _loc_999(): pass

    label('loc_999')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_9A3',
    )

    Jump('loc_BEA')

    def _loc_9A3(): pass

    label('loc_9A3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_9AD',
    )

    Jump('loc_BEA')

    def _loc_9AD(): pass

    label('loc_9AD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_9B7',
    )

    Jump('loc_BEA')

    def _loc_9B7(): pass

    label('loc_9B7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_A07',
    )

    ChrTalk(
        0x00FE,
        (
            '月光映照下的\n',
            '东方风格的庭园……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，\n',
            '简直就像梦幻一样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BEA')

    def _loc_A07(): pass

    label('loc_A07')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_AB3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_A5F',
    )

    ChrTalk(
        0x00FE,
        (
            '唔～我想去后山看看啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '村子里都已经\n',
            '没有可以去探险的地方了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AB0')

    def _loc_A5F(): pass

    label('loc_A5F')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '这里面的后山\n',
            '好像有温泉的源头。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我很想去看看，\n',
            '但是村民不允许进去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AB0(): pass

    label('loc_AB0')

    Jump('loc_BEA')

    def _loc_AB3(): pass

    label('loc_AB3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Return,
        ),
        'loc_ABD',
    )

    Jump('loc_BEA')

    def _loc_ABD(): pass

    label('loc_ABD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_BE3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_B3C',
    )

    ChrTalk(
        0x00FE,
        (
            '虽说好不容易来到这里，\n',
            '想好好调养一路疲劳的身体……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过我更想去买些特产，\n',
            '好好地品尝一下东方料理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BE0')

    def _loc_B3C(): pass

    label('loc_B3C')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '我丈夫把这当成是女神的试炼，\n',
            '我才不这么想呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说好不容易来到这里，\n',
            '想好好调养一路疲劳的身体……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过我更想去买些特产，\n',
            '好好地品尝一下东方料理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BE0(): pass

    label('loc_BE0')

    Jump('loc_BEA')

    def _loc_BE3(): pass

    label('loc_BE3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_BEA',
    )

    def _loc_BEA(): pass

    label('loc_BEA')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0xBEE
@scena.Code('func_05_BEE')
def func_05_BEE():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_BFB',
    )

    Jump('loc_D4E')

    def _loc_BFB(): pass

    label('loc_BFB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_C05',
    )

    Jump('loc_D4E')

    def _loc_C05(): pass

    label('loc_C05')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_C0F',
    )

    Jump('loc_D4E')

    def _loc_C0F(): pass

    label('loc_C0F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_C19',
    )

    Jump('loc_D4E')

    def _loc_C19(): pass

    label('loc_C19')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_C23',
    )

    Jump('loc_D4E')

    def _loc_C23(): pass

    label('loc_C23')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_C2D',
    )

    Jump('loc_D4E')

    def _loc_C2D(): pass

    label('loc_C2D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Return,
        ),
        'loc_C68',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '艾德尔那家伙\n',
            '到哪里去了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D4E')

    def _loc_C68(): pass

    label('loc_C68')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_D47',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_CD5',
    )

    ChrTalk(
        0x00FE,
        (
            '水泵出故障了， \n',
            '热水就抽不上来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然很遗憾， \n',
            '但这说不定是女神给我们的试炼呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D44')

    def _loc_CD5(): pass

    label('loc_CD5')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '唔，完全冷掉了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '泵坏掉了， \n',
            '热水就抽不上来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然很遗憾， \n',
            '但这也是女神给我们的试炼呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D44(): pass

    label('loc_D44')

    Jump('loc_D4E')

    def _loc_D47(): pass

    label('loc_D47')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_D4E',
    )

    def _loc_D4E(): pass

    label('loc_D4E')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0xD52
@scena.Code('func_06_D52')
def func_06_D52():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_D5F',
    )

    Jump('loc_E96')

    def _loc_D5F(): pass

    label('loc_D5F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_D69',
    )

    Jump('loc_E96')

    def _loc_D69(): pass

    label('loc_D69')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_D73',
    )

    Jump('loc_E96')

    def _loc_D73(): pass

    label('loc_D73')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_D7D',
    )

    Jump('loc_E96')

    def _loc_D7D(): pass

    label('loc_D7D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_D87',
    )

    Jump('loc_E96')

    def _loc_D87(): pass

    label('loc_D87')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_E7B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_DE9',
    )

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
            '…………嗯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这口井……\n',
            '大小正好适合做钓鱼池啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E78')

    def _loc_DE9(): pass

    label('loc_DE9')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '哎呀～太舒服了！\n',
            '温泉最棒了！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '连身为钓公师团成员的我\n',
            '都要把钓鱼的事情给忘掉了。\n',
            '心情真好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '简直感觉\n',
            '像心灵被清洗了一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E78(): pass

    label('loc_E78')

    Jump('loc_E96')

    def _loc_E7B(): pass

    label('loc_E7B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Return,
        ),
        'loc_E85',
    )

    Jump('loc_E96')

    def _loc_E85(): pass

    label('loc_E85')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_E8F',
    )

    Jump('loc_E96')

    def _loc_E8F(): pass

    label('loc_E8F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_E96',
    )

    def _loc_E96(): pass

    label('loc_E96')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0xE9A
@scena.Code('func_07_E9A')
def func_07_E9A():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0xEA1
@scena.Code('func_08_EA1')
def func_08_EA1():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0xEA8
@scena.Code('func_09_EA8')
def func_09_EA8():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_F87',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_F25',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，喂，库安。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你在刚才的战斗中\n',
            '一直在用导力魔法，\n',
            '那可不行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '使用魔法\n',
            '需要待机时间啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F84')

    def _loc_F25(): pass

    label('loc_F25')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '还在玩武术大会游戏……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且是在大马路上，\n',
            '不觉得害羞吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是个小鬼头。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F84(): pass

    label('loc_F84')

    Jump('loc_1238')

    def _loc_F87(): pass

    label('loc_F87')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_106D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_FF7',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，\n',
            '在蔡斯发生大事的同时，\n',
            '这边的水泵也出了故障。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不愧是解乏又温暖的\n',
            '亚尔摩温泉啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_106A')

    def _loc_FF7(): pass

    label('loc_FF7')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '嗯，不愧是蔡斯啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '恐怖事件……\n',
            '真是了不得的大新闻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '《利贝尔通讯》中\n',
            '也会登载这个爆炸性新闻吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_106A(): pass

    label('loc_106A')

    Jump('loc_1238')

    def _loc_106D(): pass

    label('loc_106D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_110E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_10C4',
    )

    ChrTalk(
        0x00FE,
        (
            '好啦，拉克。\n',
            '不能去栅栏那边啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要不然我又要\n',
            '被毛婆婆骂了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_110B')

    def _loc_10C4(): pass

    label('loc_10C4')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '只是去后山而已，\n',
            '有什么了不起的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们啊，\n',
            '真是一群小鬼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_110B(): pass

    label('loc_110B')

    Jump('loc_1238')

    def _loc_110E(): pass

    label('loc_110E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_1118',
    )

    Jump('loc_1238')

    def _loc_1118(): pass

    label('loc_1118')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_1122',
    )

    Jump('loc_1238')

    def _loc_1122(): pass

    label('loc_1122')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_112C',
    )

    Jump('loc_1238')

    def _loc_112C(): pass

    label('loc_112C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Return,
        ),
        'loc_1136',
    )

    Jump('loc_1238')

    def _loc_1136(): pass

    label('loc_1136')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_1140',
    )

    Jump('loc_1238')

    def _loc_1140(): pass

    label('loc_1140')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_1238',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_11A8',
    )

    ChrTurnDirection(0x00FE, 0x0102, 0)

    ChrTalk(
        0x00FE,
        (
            '嗯～\n',
            '蔡斯的人果然都很酷啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '该怎么说呢，\n',
            '就像这样给人以干练的感觉呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1238')

    def _loc_11A8(): pass

    label('loc_11A8')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11D0',
    )

    ChrTalk(
        0x00FE,
        (
            '哇，哥哥真帅呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11FA')

    def _loc_11D0(): pass

    label('loc_11D0')

    ChrTurnDirection(0x00FE, 0x0102, 0)

    ChrTalk(
        0x00FE,
        (
            '哇，\n',
            '那边的哥哥看起来真帅呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11FA(): pass

    label('loc_11FA')

    ChrTalk(
        0x00FE,
        (
            '喂，喂？\n',
            '你们是从蔡斯来的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在那边\n',
            '正流行什么啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1238(): pass

    label('loc_1238')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x123C
@scena.Code('func_0A_123C')
def func_0A_123C():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x1243
@scena.Code('func_0B_1243')
def func_0B_1243():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x124A
@scena.Code('func_0C_124A')
def func_0C_124A():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_12DA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_128D',
    )

    ChrTalk(
        0x00FE,
        (
            '上啊～！\n',
            '看我的导力魔法！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '咚～～啪！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12D7')

    def _loc_128D(): pass

    label('loc_128D')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '喂，莉西亚姐姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x000E, 400)

    ChrTalk(
        0x00FE,
        (
            '你是裁判，\n',
            '要好好看着才行哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00FE, 180, 0)

    def _loc_12D7(): pass

    label('loc_12D7')

    Jump('loc_15BD')

    def _loc_12DA(): pass

    label('loc_12DA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_1368',
    )

    ChrTalk(
        0x00FE,
        (
            '嘿，你知道吗？\n',
            '蔡斯出事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像是不得了的大事件。\n',
            '这个村子里\n',
            '也有游击士来调查了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊～\n',
            '好想看看真正的游击士呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15BD')

    def _loc_1368(): pass

    label('loc_1368')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_1426',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_13B9',
    )

    ChrTalk(
        0x00FE,
        (
            '啊啊～\n',
            '真想去后山探险一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '村子里面\n',
            '我都已经玩够了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1423')

    def _loc_13B9(): pass

    label('loc_13B9')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '温泉的源头\n',
            '一定非常大吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '温泉水从那里\n',
            '涌出了几十年，\n',
            '也没有见它干涸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊～真想去看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1423(): pass

    label('loc_1423')

    Jump('loc_15BD')

    def _loc_1426(): pass

    label('loc_1426')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_1430',
    )

    Jump('loc_15BD')

    def _loc_1430(): pass

    label('loc_1430')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_143A',
    )

    Jump('loc_15BD')

    def _loc_143A(): pass

    label('loc_143A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_14E6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_1492',
    )

    ChrTalk(
        0x00FE,
        (
            '唔～我想去后山看看啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '村子里都已经\n',
            '没有可以去探险的地方了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14E3')

    def _loc_1492(): pass

    label('loc_1492')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '这里面的后山\n',
            '好像有温泉的源头。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我很想去看看，\n',
            '但是村民不允许进去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14E3(): pass

    label('loc_14E3')

    Jump('loc_15BD')

    def _loc_14E6(): pass

    label('loc_14E6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_153B',
    )

    ChrTalk(
        0x00FE,
        (
            '我正在想温泉\n',
            '为什么越来越凉了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在热水已经完全没有了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15BD')

    def _loc_153B(): pass

    label('loc_153B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_15BD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_1583',
    )

    ChrTalk(
        0x00FE,
        (
            '这么年轻\n',
            '就来泡温泉啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '肯定是相当累了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15BD')

    def _loc_1583(): pass

    label('loc_1583')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '啊，有客人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎～真少见啊。\n',
            '这么年轻的客人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15BD(): pass

    label('loc_15BD')

    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x15C1
@scena.Code('func_0D_15C1')
def func_0D_15C1():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x15C8
@scena.Code('func_0E_15C8')
def func_0E_15C8():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_1656',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_1617',
    )

    ChrTalk(
        0x00FE,
        (
            '可恶！不能认输！\n',
            '我也发动魔法！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿呀呀呀呀～～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1653')

    def _loc_1617(): pass

    label('loc_1617')

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '嘿嘿嘿～说起诞辰庆典，\n',
            '果然还是武术大会最吸引人吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1653(): pass

    label('loc_1653')

    Jump('loc_18BC')

    def _loc_1656(): pass

    label('loc_1656')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_16D8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_16A2',
    )

    ChrTalk(
        0x00FE,
        (
            '真是件大事啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然好像和我们村子\n',
            '没什么关系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16D5')

    def _loc_16A2(): pass

    label('loc_16A2')

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '蔡斯出了大事吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '城市里果然可怕啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_16D5(): pass

    label('loc_16D5')

    Jump('loc_18BC')

    def _loc_16D8(): pass

    label('loc_16D8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_17E1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_175A',
    )

    ChrTalk(
        0x00FE,
        (
            '……但是，\n',
            '莉西亚姐姐也真是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们都已经是大人了，\n',
            '不要管我们那么多嘛。\n',
            '有这时间倒不如去旅馆帮帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17DE')

    def _loc_175A(): pass

    label('loc_175A')

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '后山的温泉源头吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然我经常听说，\n',
            '但是从来没有亲眼见过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，\n',
            '虽说不能越过这个栅栏，\n',
            '但我还是很想去看看啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17DE(): pass

    label('loc_17DE')

    Jump('loc_18BC')

    def _loc_17E1(): pass

    label('loc_17E1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_17EB',
    )

    Jump('loc_18BC')

    def _loc_17EB(): pass

    label('loc_17EB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_17F5',
    )

    Jump('loc_18BC')

    def _loc_17F5(): pass

    label('loc_17F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_17FF',
    )

    Jump('loc_18BC')

    def _loc_17FF(): pass

    label('loc_17FF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1836',
    )

    ChrTalk(
        0x00FE,
        (
            '不冒热气的温泉\n',
            '总觉得有点不习惯啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18BC')

    def _loc_1836(): pass

    label('loc_1836')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_18BC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_188C',
    )

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，拉克真是小鬼啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说到情侣，\n',
            '果然要一起去温泉才浪漫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18BC')

    def _loc_188C(): pass

    label('loc_188C')

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '嘿嘿嘿，很浪漫啊。\n',
            '情侣一起到温泉旅游。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18BC(): pass

    label('loc_18BC')

    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x18C0
@scena.Code('func_0F_18C0')
def func_0F_18C0():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_19BA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1933',
    )

    ChrTalk(
        0x00FE,
        (
            '唔～\n',
            '我还是很想亲眼看看\n',
            '真正的东方文化啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来要委托游击士\n',
            '护卫我到沃尔费堡垒了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19B7')

    def _loc_1933(): pass

    label('loc_1933')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '唔～\n',
            '蔡斯好像发生了不得了的大事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '其实我想过\n',
            '要不要去共和国旅游。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是发生了那种事件之后，\n',
            '总觉得旅行不太安全。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19B7(): pass

    label('loc_19B7')

    Jump('loc_1AFC')

    def _loc_19BA(): pass

    label('loc_19BA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_1AFC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1A62',
    )

    ChrTalk(
        0x00FE,
        (
            '这么说来，\n',
            '在这里的途中……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我迷了路，\n',
            '结果被一种身手敏捷的魔兽追赶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我还想着死定了呢，\n',
            '但它们只是不停地在闪光。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到底是什么呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AFC')

    def _loc_1A62(): pass

    label('loc_1A62')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '喔喔～很厉害的热气啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '建物的风格也很有意思……\n',
            '嗯，呆在这里真是享受。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '原来如此。\n',
            '这就是东方风格吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我越来越想\n',
            '去东方看看了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AFC(): pass

    label('loc_1AFC')

    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x1B00
@scena.Code('func_10_1B00')
def func_10_1B00():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#0080080668V#070F哦，真不错……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080080669V赶快去泡个澡，\n',
            '驱除一下旅途的劳累吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0x1B5F
@scena.Code('func_11_1B5F')
def func_11_1B5F():
    EventBegin(0x00)
    CameraMove(17070, 6660, 16820, 0)
    OP_67(0, 3960, -10000, 0)
    CameraSetDistance(4370, 0)
    OP_6C(39000, 0)
    ChrSetPos(0x0101, -17420, -2000, 15200, 90)
    ChrSetPos(0x0102, -18340, -2000, 16000, 90)
    ChrSetPos(0x0107, -18340, -2000, 14400, 90)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_1BD7')
    def lambda_1BD7():
        OP_6C(90000, 8500)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_1BD7)

    Sleep(4000)

    @scena.Lambda('lambda_1BEC')
    def lambda_1BEC():
        CameraMove(-16149, -2000, 14900, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1BEC)

    @scena.Lambda('lambda_1C04')
    def lambda_1C04():
        OP_67(0, 9500, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1C04)

    @scena.Lambda('lambda_1C1C')
    def lambda_1C1C():
        CameraSetDistance(2800, 4000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1C1C)

    Sleep(4500)

    ChrTalk(
        0x0101,
        (
            '#0010080001V#501F#5P哎～这里就是亚尔摩村啊。\n',
            '环境真的很不错呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080002V#505F不过……好像有什么怪味……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080003V#560F啊～～\n',
            '这是温泉里硫磺散发出来的气味。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080004V#010F有温泉涌出来的地方，\n',
            '似乎大多都有这种气味吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0107, 400)
    ChrTurnDirection(0x0101, 0x0107, 400)

    ChrTalk(
        0x0101,
        (
            '#0010080005V#004F#5P哦～\n',
            '好像烧糊的鸡蛋气味呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080006V#006F嗯，不过也不是特别难闻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080007V#067F嘿嘿……那就好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080008V#064F啊～不过不过，\n',
            '今天的气味好像比平时淡了点……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080009V好像是热气没放出来的感觉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080010V#010F我想大概就是因为\n',
            '水泵发生了故障的缘故。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080011V我们现在就去修理吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0102, 400)

    ChrTalk(
        0x0107,
        (
            '#0070080012V#060F嗯，好啊。\n',
            '不过水泵小屋的钥匙\n',
            '在旅馆的毛婆婆那里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080013V得先去借钥匙才行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080014V#006F#5PＯＫ！\n',
            '那就先去旅馆吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0040, 0x01, 0x0002)
    EventEnd(0x00)

    Return()

# id: 0x0012 offset: 0x1F28
@scena.Code('func_12_1F28')
def func_12_1F28():
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

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 5, 0x51D)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 6, 0x51E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_208E',
    )

    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x00A3, 6, 0x51E))
    OP_28(0x0040, 0x01, 0x0008)

    ChrTalk(
        0x0101,
        (
            '#0010080052V#501F啊，这里就是水泵小屋啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080053V#060F嗯，是呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080054V这里可以把深山里的温泉\n',
            '运送到旅馆和广场的井里哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080055V#010F那么，\n',
            '用刚才的钥匙开门吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(115, 0x00, 0x64)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '使用水泵小屋的钥匙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_71(0x0003, 0x0010)
    OP_64(0x00, 0x0001)
    EventEnd(0x01)

    Jump('loc_2091')

    def _loc_208E(): pass

    label('loc_208E')

    TalkEnd(0x00FF)

    def _loc_2091(): pass

    label('loc_2091')

    Return()

# id: 0x0013 offset: 0x2092
@scena.Code('func_13_2092')
def func_13_2092():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 3, 0x523)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_263E',
    )

    SetScenaFlags(ScenaFlag(0x00A4, 3, 0x523))
    OP_28(0x0040, 0x01, 0x0200)
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    ChrSetDirection(0x0101, 90, 400)
    ChrSetDirection(0x0102, 90, 400)
    ChrSetDirection(0x0110, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010080210V#501F啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080211V快看，温泉涌出来了呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0110,
        (
            '#0280080212V#153F哇～真的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_212B')
    def lambda_212B():
        CameraMove(15680, 2830, 16620, 2600)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_212B)

    @scena.Lambda('lambda_2143')
    def lambda_2143():
        OP_6C(56000, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_2143)

    Sleep(2500)

    ChrSetPos(0x0101, 8210, 2000, 16740, 90)
    ChrSetPos(0x0102, 7680, 2000, 15580, 90)
    ChrSetPos(0x0110, 6840, 2000, 16430, 90)

    @scena.Lambda('lambda_218B')
    def lambda_218B():
        ChrWalkTo(0x00FE, 13600, 2500, 16970, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_218B)

    Sleep(300)

    @scena.Lambda('lambda_21AB')
    def lambda_21AB():
        ChrWalkTo(0x00FE, 12880, 2500, 15970, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_21AB)

    Sleep(300)

    @scena.Lambda('lambda_21CB')
    def lambda_21CB():
        ChrMoveTo(0x00FE, 12530, 2250, 17630, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0110, 0x0001, lambda_21CB)

    WaitForThreadExit(0x0110, 0x0001)

    ChrTalk(
        0x0102,
        (
            '#0020080213V#010F看来提妲那孩子\n',
            '已经将导力泵顺利修好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0110,
        (
            '#0280080214V#151F好棒～\n',
            '这下总算可以泡温泉了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280080215V死而无憾了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0110, 400)

    ChrTalk(
        0x0101,
        (
            '#0010080216V#506F#2P没那么夸张吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0110, 400)

    ChrTalk(
        0x0102,
        (
            '#0020080217V#010F#2P朵洛希小姐你\n',
            '那么喜欢泡温泉吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0110, 0x0102, 400)

    ChrTalk(
        0x0110,
        (
            '#0280080218V#150F嘿嘿，那当然啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280080219V没有什么比泡好温泉后\n',
            '喝杯水果牛奶更棒的事了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280080220V#151F那么～～\n',
            '我就先去泡温泉了～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2381')
    def lambda_2381():
        CameraMove(16100, 2000, 12100, 3600)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2381)

    @scena.Lambda('lambda_2399')
    def lambda_2399():
        OP_6C(135000, 3600)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2399)

    @scena.Lambda('lambda_23A9')
    def lambda_23A9():
        ChrTurnDirection(0x00FE, 0x0110, 0)
        Yield()

        Jump('lambda_23A9')

    DispatchAsync2(0x0101, 0x0003, lambda_23A9)

    @scena.Lambda('lambda_23BA')
    def lambda_23BA():
        ChrTurnDirection(0x00FE, 0x0110, 0)
        Yield()

        Jump('lambda_23BA')

    DispatchAsync2(0x0102, 0x0003, lambda_23BA)

    ChrWalkTo(0x0110, 10940, 2000, 15830, 3000, 0x00)
    ChrWalkTo(0x0110, 11280, 2000, 12300, 3000, 0x00)
    ChrWalkTo(0x0110, 17020, 2000, 10790, 3000, 0x00)
    OP_62(0x0110, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTalk(
        0x0110,
        (
            '#0280080221V#153F#2P啊，对了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0110, 0x0101, 400)

    ChrTalk(
        0x0110,
        (
            '#0280080222V#151F#2P小艾、小约。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280080223V刚才真是谢谢了～！\n',
            '在危难之中救了我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_24A2')
    def lambda_24A2():
        CameraMove(14030, 2500, 16360, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_24A2)

    @scena.Lambda('lambda_24BA')
    def lambda_24BA():
        OP_6C(90000, 2500)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_24BA)

    ChrSetDirection(0x0110, 90, 400)
    ChrWalkTo(0x0110, 23120, 2000, 4090, 3000, 0x00)
    ChrSetFlags(0x0110, 0x0080)
    ChrSetPos(0x0110, 13600, 2500, 16970, 0)
    TerminateThread(0x0101, 0x03)
    TerminateThread(0x0102, 0x03)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010080224V#007F#1P这个朵洛希……\n',
            '现在才想起说这种客气话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080225V#008F真受不了她，\n',
            '做什么事都少根筋似的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020080226V#019F哈哈，这就是朵洛希的风格。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080227V#010F那么，\n',
            '我们去水泵小屋看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010080228V#006F#1P啊，对呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080229V提妲那孩子\n',
            '可能还留在那里呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)
    FormationDelMember(0x0F, 0xFF)

    def _loc_263E(): pass

    label('loc_263E')

    Return()

# id: 0x0014 offset: 0x263F
@scena.Code('func_14_263F')
def func_14_263F():
    EventBegin(0x00)
    CameraMove(26330, 2000, 4950, 0)
    OP_6C(44000, 0)
    ChrSetPos(0x0101, 23790, 2000, 4370, 90)
    ChrSetPos(0x0102, 23900, 2000, 3160, 90)
    ChrSetPos(0x0107, 25060, 2000, 3830, 90)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, 27590, 2000, 3840, 270)
    RemoveItem(0x0369, 1)
    FadeIn(1500, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010080578V#006F那么再见了，毛婆婆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080579V#010F承蒙您的多方照顾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570080580V#681F不用这么客气，\n',
            '你们能玩得高兴我就很开心了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080581V哈哈，\n',
            '提妲也很高兴的样子嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080582V#067F嘿嘿……是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570080583V#680F看来昨天有开心的事情是吧。\n',
            '我觉得你们三个已经像是兄妹那样了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080584V#683F说起来……\n',
            '怎么没看到那个带眼镜的姑娘呢。\n',
            '那个傻丫头怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080585V#505F嗯……\n',
            '她好像还在睡呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080586V怎么叫都叫不醒，\n',
            '所以我们就没再去打扰她了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080587V#010F朵洛希小姐起来的话，\n',
            '请代我们向她问候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570080588V#680F好，知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080589V提妲，\n',
            '也麻烦你代为问候拉赛尔那家伙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080590V叫他不要整天只顾着研究，\n',
            '要多注意一下生活规律才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080591V#060F呵呵，我会转告的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080592V#061F婆婆您也要保重。\n',
            '以后我还会再来玩的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570080593V#681F啊啊，我等着你过来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080594V#680F你们俩也是，\n',
            '有空的话记得多来这里玩哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080595V总之，想泡温泉的话就过来，\n',
            '反正这里随时为你们准备着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080596V#508F嗯！\n',
            '一定会再来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080597V#019F而且料理也很美味，\n',
            '我们下次一定会再来品尝的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 90, 400)
    ChrWalkTo(0x0008, 29620, 2500, 4130, 2000, 0x00)
    OP_70(0x0004, 29)
    OP_73(0x0004)
    ChrSetFlags(0x0008, 0x0004)
    ChrWalkTo(0x0008, 31880, 2500, 4030, 2000, 0x00)
    OP_72(0x0004, 0x0800)
    PlaySE(7, 0x00, 0x64)
    OP_6F(0x0004, 29)
    OP_70(0x0004, 0)
    OP_73(0x0004)
    OP_71(0x0004, 0x0800)

    @scena.Lambda('lambda_2B55')
    def lambda_2B55():
        CameraMove(24380, 2000, 3780, 1500)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_2B55)

    ChrSetDirection(0x0107, 270, 400)
    WaitForThreadExit(0x0107, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010080598V#001F这次任务可说是最轻松的了，\n',
            '我呢，感觉整个人更加有干劲呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080599V#019F没错。\n',
            '这也是托修理水泵的福啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080600V真要多谢提妲了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080601V#067F哪、哪儿的话，\n',
            '其实我也没做什么啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080602V#066F倒是艾丝蒂尔姐姐你们辛苦了。\n',
            '昨天特地护送我过来，真是谢谢呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080603V我……过得非常开心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080604V#008F嘿嘿～\n',
            '能帮上忙我也很开心啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080605V#001F算是彼此彼此啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080606V#061F嗯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020080607V#010F那么接下来，\n',
            '我们差不多该回蔡斯了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080608V说不定我们回到工房的时候，\n',
            '『黑色导力器』的解体也已经完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010080609V#004F啊，对了……\n',
            '还有那么一回事呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080610V#506F哎呀～完全忘记了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080611V#018F唉……\n',
            '就知道你会这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080612V#067F呵呵～\n',
            '艾丝蒂尔姐姐真是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetStatus(0x0000, 0xFE, 0)
    ChrSetStatus(0x0001, 0xFE, 0)
    ChrSetStatus(0x0002, 0xFE, 0)
    ChrSetStatus(0x0003, 0xFE, 0)
    ChrSetStatus(0x0004, 0xFE, 0)
    ChrSetStatus(0x0005, 0xFE, 0)
    ChrSetStatus(0x0006, 0xFE, 0)
    ChrSetStatus(0x0007, 0xFE, 0)
    TerminateThread(0x0101, 0xFF)
    MapClearFlags(0x10000000)
    EventEnd(0x00)

    Return()

# id: 0x0015 offset: 0x2EBB
@scena.Code('func_15_2EBB')
def func_15_2EBB():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 1, 0x529)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3312',
    )

    SetScenaFlags(ScenaFlag(0x00A5, 1, 0x529))
    EventBegin(0x00)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, 5790, 1000, 14450, 0)

    ChrTalk(
        0x0009,
        (
            '#0280080613V等一下～～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)

    @scena.Lambda('lambda_2F10')
    def lambda_2F10():
        OP_6C(45000, 0)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_2F10)

    ChrSetFlags(0x000A, 0x0080)
    CameraMove(-11320, -2000, 15580, 0)
    ChrSetPos(0x0009, -2260, 0, 14820, 270)
    ChrSetPos(0x0101, -11140, -2000, 15290, 90)
    ChrSetPos(0x0102, -12050, -2000, 16190, 90)
    ChrSetPos(0x0107, -12260, -2000, 14680, 90)
    OP_0D()

    @scena.Lambda('lambda_2F7B')
    def lambda_2F7B():
        ChrWalkTo(0x00FE, -9830, -2000, 15440, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2F7B)

    WaitForThreadExit(0x0009, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010080614V#501F啊，朵洛希。\n',
            '你总算起床了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0280080615V#152F哈啊哈啊哈啊……\n',
            '大、大家好过分呢～！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280080616V竟然丢下我一个人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080617V#004F咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080618V#014F朵洛希小姐，\n',
            '你不是说要拍报道用的照片，\n',
            '所以还要留在村子里一段时间吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0280080619V#153F咦，我有说过吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280080620V#151F这个不重要啦～\n',
            '你们不要把我排除在外嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280080621V小提也同意吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080622V#065F小提……\n',
            '是、是在叫我吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080623V#509F你、你还叫得真随便啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0280080624V#154F哎呀～\n',
            '因为『小提妲』叫起来太拗口了嘛～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280080625V不行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080626V#067F不会啊，挺好的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0280080627V#151F谢谢，小提⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080628V#007F唉……\n',
            '真不愧是我行我素的类型。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080629V#006F好了，闲话少说。\n',
            '你就跟我们一起回蔡斯吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0280080630V#150F嘿嘿，这样才对嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080631V#010F那么，\n',
            '我们一起出发吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0009, 0x0040)

    @scena.Lambda('lambda_32EF')
    def lambda_32EF():
        OP_92(0x00FE, 0x0000, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_32EF)

    EventEnd(0x00)
    ChrSetFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    MapClearFlags(0x10000000)
    FormationAddMember(0x0F, 0xFF)

    def _loc_3312(): pass

    label('loc_3312')

    Return()

# id: 0x0016 offset: 0x3313
@scena.Code('func_16_3313')
def func_16_3313():
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

# id: 0x0017 offset: 0x3363
@scena.Code('func_17_3363')
def func_17_3363():
    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_33B0',
    )

    ChrTalk(
        0x0107,
        (
            '#0070080048V#060F（这边是村口。\n',
            '　赶快去水泵小屋吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_345B')

    def _loc_33B0(): pass

    label('loc_33B0')

    ChrTurnDirection(0x0107, 0x0000, 400)

    ChrTalk(
        0x0107,
        (
            '#0070080049V#060F啊，那个……\n',
            '再往前走就到平原上去了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080050V水泵小屋在村子的另外一边哦。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3429')
    def lambda_3429():
        ChrTurnDirection(0x0102, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3429)

    ChrTurnDirection(0x0101, 0x0107, 400)

    ChrTalk(
        0x0101,
        (
            '#0010080051V#000F嗯，明白了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_345B(): pass

    label('loc_345B')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0018 offset: 0x3477
@scena.Code('func_18_3477')
def func_18_3477():
    EventBegin(0x02)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020080076V#010F在修理好之前，\n',
            '我们就在旅馆等着吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080077V那种情况，\n',
            '我们也帮不上什么忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010080078V#000F是啊，\n',
            '偶尔清闲一下也不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0019 offset: 0x353C
@scena.Code('func_19_353C')
def func_19_353C():
    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3589',
    )

    ChrTalk(
        0x0102,
        (
            '#0020080311V#010F太阳快下山了……\n',
            '村子外面会很危险的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_35EE')

    def _loc_3589(): pass

    label('loc_3589')

    ChrTurnDirection(0x0102, 0x0000, 400)

    ChrTalk(
        0x0102,
        (
            '#0020080312V#014F太阳就快下山了，\n',
            '村子外面会很危险的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080313V我们还是不要出去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_35EE(): pass

    label('loc_35EE')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x001A offset: 0x360A
@scena.Code('func_1A_360A')
def func_1A_360A():
    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '发现了一个油纸包。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '里面放着',
            (TxtCtl.SetColor, 0x2),
            '艾尔贝啄木鸟的生态',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(0x0343, 1)
    OP_64(0x02, 0x0001)
    OP_28(0x002E, 0x01, 0x0010)
    TalkEnd(0x00FF)

    Return()

# id: 0x001B offset: 0x368B
@scena.Code('func_1B_368B')
def func_1B_368B():
    OP_13(0x0088)

    Return()

# id: 0x001C offset: 0x368F
@scena.Code('func_1C_368F')
def func_1C_368F():
    OP_13(0x0087)

    Return()

# id: 0x001D offset: 0x3693
@scena.Code('func_1D_3693')
def func_1D_3693():
    OP_13(0x0089)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

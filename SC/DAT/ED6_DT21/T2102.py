import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T2102_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2102   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2102.x'
    header.mapIndex       = 1
    header.bgm            = 12
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
        ('ED6_DT07/CH01100._CH', 'ED6_DT07/CH01100P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01160._CH', 'ED6_DT07/CH01160P._CP'),
        ('ED6_DT07/CH01660._CH', 'ED6_DT07/CH01660P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01290._CH', 'ED6_DT07/CH01290P._CP'),
        ('ED6_DT07/CH02590._CH', 'ED6_DT07/CH02590P._CP'),
        ('ED6_DT07/CH02500._CH', 'ED6_DT07/CH02500P._CP'),
        ('ED6_DT07/CH02630._CH', 'ED6_DT07/CH02630P._CP'),
        ('ED6_DT07/CH02640._CH', 'ED6_DT07/CH02640P._CP'),
        ('ED6_DT07/CH02390._CH', 'ED6_DT07/CH02390P._CP'),
        ('ED6_DT07/CH02550._CH', 'ED6_DT07/CH02550P._CP'),
        ('ED6_DT07/CH02570._CH', 'ED6_DT07/CH02570P._CP'),
        ('ED6_DT07/CH02600._CH', 'ED6_DT07/CH02600P._CP'),
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
        ('ED6_DT07/CH01470._CH', 'ED6_DT07/CH01470P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01660._CH', 'ED6_DT07/CH01660P._CP'),
        ('ED6_DT07/CH01470._CH', 'ED6_DT07/CH01470P._CP'),
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
        ('ED6_DT07/CH01180._CH', 'ED6_DT07/CH01180P._CP'),
    ]

# id: 0x10001 offset: 0x16A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '城中老年男子',
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '城中中年妇女',
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
            name                = '城中小男孩',
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '森特',
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '贵族中年男子',
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
            name                = '贵族女孩',
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
            name                = '哈尔德',
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '林德号',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0184,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '林德号影子',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0184,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '爱德望',
            x                   = 101700,
            z                   = 0,
            y                   = 83800,
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
            name                = '克拉姆',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '波利',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '玛丽',
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
            name                = '达尼艾尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '乔儿',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '汉斯',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '特蕾莎院长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '科林兹校长',
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '库莱泽',
            x                   = 111220,
            z                   = 6150,
            y                   = 101150,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '萨马里奥',
            x                   = 112530,
            z                   = 6150,
            y                   = 102340,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '豆豆',
            x                   = 129990,
            z                   = 8150,
            y                   = 92560,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '哈尔德',
            x                   = 111500,
            z                   = 4150,
            y                   = 85650,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '森特',
            x                   = 108620,
            z                   = 6150,
            y                   = 95510,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '孩子',
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '贵族女子',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '贵族男子',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '卢安市·北街区',
            x                   = 71170,
            z                   = 0,
            y                   = 80860,
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

# id: 0x10002 offset: 0x4CA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x4CA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x4CA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 100400,
            triggerZ            = 0,
            triggerY            = 83700,
            triggerRange        = 1000,
            actorX              = 101700,
            actorZ              = 1500,
            actorY              = 83800,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 108610,
            triggerZ            = 6150,
            triggerY            = 96910,
            triggerRange        = 800,
            actorX              = 108610,
            actorZ              = 8350,
            actorY              = 96910,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0029,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 127080,
            triggerZ            = 6150,
            triggerY            = 100740,
            triggerRange        = 800,
            actorX              = 127080,
            actorZ              = 8350,
            actorY              = 100740,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x002A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 122620,
            triggerZ            = 400,
            triggerY            = 100640,
            triggerRange        = 800,
            actorX              = 122620,
            actorZ              = 1600,
            actorY              = 100640,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x002B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 140870,
            triggerZ            = 1000,
            triggerY            = 108000,
            triggerRange        = 800,
            actorX              = 140870,
            actorZ              = 2000,
            actorY              = 108000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 149330,
            triggerZ            = 1000,
            triggerY            = 108000,
            triggerRange        = 800,
            actorX              = 149330,
            actorZ              = 2000,
            actorY              = 108000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 103030,
            triggerZ            = 1000,
            triggerY            = 108000,
            triggerRange        = 800,
            actorX              = 103030,
            actorZ              = 2000,
            actorY              = 108000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 96980,
            triggerZ            = 1000,
            triggerY            = 108000,
            triggerRange        = 800,
            actorX              = 96980,
            actorZ              = 2000,
            actorY              = 108000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x5EA
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_659',
    )

    ChrSetFlags(0x001A, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_634',
    )

    ChrSetPos(0x0011, 108580, 6150, 96500, 0)
    ChrSetPos(0x001B, 136340, 8150, 95080, 270)
    ChrSetPos(0x001C, 135340, 8150, 95080, 90)

    Jump('loc_656')

    def _loc_634(): pass

    label('loc_634')

    ChrSetPos(0x0011, 111500, 4150, 80040, 100)
    ChrSetPos(0x001B, 134010, 8150, 92800, 270)

    def _loc_656(): pass

    label('loc_656')

    Jump('loc_715')

    def _loc_659(): pass

    label('loc_659')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_68F',
    )

    ChrSetPos(0x001A, 139320, 6150, 99610, 180)
    ChrSetPos(0x001B, 130460, 8150, 98040, 180)
    ChrSetFlags(0x001C, 0x0010)
    ChrClearFlags(0x001D, 0x0080)

    Jump('loc_715')

    def _loc_68F(): pass

    label('loc_68F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_6CF',
    )

    ChrSetPos(0x001A, 139320, 6150, 99610, 180)
    ChrSetPos(0x001B, 129990, 8150, 92560, 90)
    ChrSetFlags(0x001C, 0x0080)

    If(
        (
            (Expr.Eval, "OP_29(0x0066, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_6CC',
    )

    ChrClearFlags(0x001E, 0x0080)

    def _loc_6CC(): pass

    label('loc_6CC')

    Jump('loc_715')

    def _loc_6CF(): pass

    label('loc_6CF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_6FF',
    )

    ChrSetPos(0x001A, 111460, 4150, 79470, 90)
    ChrSetPos(0x001B, 141100, 6150, 100100, 39)

    Jump('loc_715')

    def _loc_6FF(): pass

    label('loc_6FF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_715',
    )

    ChrSetFlags(0x001A, 0x0010)
    ChrSetFlags(0x001B, 0x0010)
    ChrSetFlags(0x001C, 0x0010)

    def _loc_715(): pass

    label('loc_715')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_72B',
    )

    MapClearFlags(0x00000010)
    MapSetFlags(0x10000000)
    Event(0, func_0C_1908)

    def _loc_72B(): pass

    label('loc_72B')

    Return()

# id: 0x0001 offset: 0x72C
@scena.Code('func_01_72C')
def func_01_72C():
    OP_16(0x02, 4000, 20000, -40000, 2293833)
    PlaySE(453, 0x01, 0x64)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_74E',
    )

    OP_64(0x00, 0x0001)

    def _loc_74E(): pass

    label('loc_74E')

    Return()

# id: 0x0002 offset: 0x74F
@scena.Code('func_02_74F')
def func_02_74F():
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
        'loc_774',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_8B6')

    def _loc_774(): pass

    label('loc_774')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_78D',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_8B6')

    def _loc_78D(): pass

    label('loc_78D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7A6',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_8B6')

    def _loc_7A6(): pass

    label('loc_7A6')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7BF',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_8B6')

    def _loc_7BF(): pass

    label('loc_7BF')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7D8',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_8B6')

    def _loc_7D8(): pass

    label('loc_7D8')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7F1',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_8B6')

    def _loc_7F1(): pass

    label('loc_7F1')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_80A',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_8B6')

    def _loc_80A(): pass

    label('loc_80A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_823',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_8B6')

    def _loc_823(): pass

    label('loc_823')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_83C',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_8B6')

    def _loc_83C(): pass

    label('loc_83C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_855',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_8B6')

    def _loc_855(): pass

    label('loc_855')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_86E',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_8B6')

    def _loc_86E(): pass

    label('loc_86E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_887',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_8B6')

    def _loc_887(): pass

    label('loc_887')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8A0',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_8B6')

    def _loc_8A0(): pass

    label('loc_8A0')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8B6',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_8B6(): pass

    label('loc_8B6')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_8CB',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_8B6')

    def _loc_8CB(): pass

    label('loc_8CB')

    Return()

# id: 0x0003 offset: 0x8CC
@scena.Code('func_03_8CC')
def func_03_8CC():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_91B',
    )

    ChrTalk(
        0x00FE,
        (
            '定期船来之前\n',
            '还有相当长的时间呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要不要先\n',
            '去吃饭呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_953')

    def _loc_91B(): pass

    label('loc_91B')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '～前往王都的船是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，还有空闲呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x00FE, 0x0010)

    def _loc_953(): pass

    label('loc_953')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x957
@scena.Code('func_04_957')
def func_04_957():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_9A9',
    )

    ChrTalk(
        0x001D,
        (
            '前往王都的船就快到了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '最近都没有误点过，\n',
            '还是定期船方便啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A0F')

    def _loc_9A9(): pass

    label('loc_9A9')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x001D,
        (
            '这次的视察\n',
            '成果丰厚啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '旅游向导指出的\n',
            '景点也不少。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那么，接着是去王都\n',
            '跟飞船公社的谈判了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A0F(): pass

    label('loc_A0F')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0xA13
@scena.Code('func_05_A13')
def func_05_A13():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_B22',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AC9',
    )

    ChrTalk(
        0x00FE,
        (
            '检查了几十次\n',
            '却没有任何异常。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '尽管如此，却怎么也\n',
            '动不了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，要是这就放弃\n',
            '我作为维修员就失职了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没发现原因之前\n',
            '几百次都要检查下去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_B1F')

    def _loc_AC9(): pass

    label('loc_AC9')

    ChrTalk(
        0x00FE,
        (
            '维修的基本就是检查，\n',
            '哥哥就是这么说的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没发现原因之前\n',
            '几百次都要检查下去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B1F(): pass

    label('loc_B1F')

    Jump('loc_DAB')

    def _loc_B22(): pass

    label('loc_B22')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_BFD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BAF',
    )

    ChrTalk(
        0x00FE,
        (
            '库莱泽哥哥\n',
            '都乘上『埃尔赛尤』了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为哥哥很优秀，\n',
            '现在一定在修理导力器。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以我、我们也不能输，要努力！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_BFA')

    def _loc_BAF(): pass

    label('loc_BAF')

    ChrTalk(
        0x00FE,
        (
            '库莱泽哥哥\n',
            '现在一定在修理导力器。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以我、我们也不能输，要努力！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BFA(): pass

    label('loc_BFA')

    Jump('loc_DAB')

    def _loc_BFD(): pass

    label('loc_BFD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_CA5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_C5E',
    )

    ChrTalk(
        0x00FE,
        (
            '我的工作\n',
            '也渐渐增多了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要更加更加熟练，\n',
            '以后成为独当一面的维修士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CA2')

    def _loc_C5E(): pass

    label('loc_C5E')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '舷梯的导力机构ＯＫ……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好，这样靠岸准备就完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x00FE, 0x0010)

    def _loc_CA2(): pass

    label('loc_CA2')

    Jump('loc_DAB')

    def _loc_CA5(): pass

    label('loc_CA5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_D46',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_CFA',
    )

    ChrTalk(
        0x00FE,
        (
            '我要努力\n',
            '早日独当一面！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为此还有很多事\n',
            '要学习才行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D43')

    def _loc_CFA(): pass

    label('loc_CFA')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '库莱泽哥哥\n',
            '一定也是想认真做研究的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我要努力\n',
            '早日独当一面！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D43(): pass

    label('loc_D43')

    Jump('loc_DAB')

    def _loc_D46(): pass

    label('loc_D46')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_DAB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_D6F',
    )

    ChrTalk(
        0x00FE,
        (
            '我是见习的维修员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DAB')

    def _loc_D6F(): pass

    label('loc_D6F')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '导力机构锁定确认完毕！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，没有任何问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x00FE, 0x0010)

    def _loc_DAB(): pass

    label('loc_DAB')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0xDAF
@scena.Code('func_06_DAF')
def func_06_DAF():
    ChrTalk(
        0x001A,
        (
            '萨马里奥\n',
            '去确认诱导灯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '豆豆那小家伙去哪了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '豆豆去检查\n',
            '靠岸装置了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '是吗，那就交给他了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '时间不多，要慎重。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x001B, 0x0010)

    Return()

# id: 0x0007 offset: 0xE3B
@scena.Code('func_07_E3B')
def func_07_E3B():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_F22',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_EA0',
    )

    ChrTalk(
        0x00FE,
        (
            '那么… \n',
            '接着即将到达的是『赛希莉亚号』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果要乘坐\n',
            '最好赶快办手续哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F1F')

    def _loc_EA0(): pass

    label('loc_EA0')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '那么… \n',
            '接着即将到达的是『赛希莉亚号』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正准备到达卢安，\n',
            '并发来了准点的联络。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果要乘坐\n',
            '最好赶快办手续哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F1F(): pass

    label('loc_F1F')

    Jump('loc_10D3')

    def _loc_F22(): pass

    label('loc_F22')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_FB1',
    )

    ChrTalk(
        0x00FE,
        (
            '最近的豆豆\n',
            '变得像个维修员的样子了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '即使不作细节的指示，\n',
            '一般的工作也能处理了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈，偶尔不在\n',
            '就能体会到他的成长了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10D3')

    def _loc_FB1(): pass

    label('loc_FB1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1076',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1010',
    )

    ChrTalk(
        0x00FE,
        (
            '中央工房的新型引擎\n',
            '据说终于完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '作为技术人员\n',
            '真想看一次啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1073')

    def _loc_1010(): pass

    label('loc_1010')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '中央工房的新型引擎\n',
            '据说终于完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样的话，『埃尔赛尤』\n',
            '应该也能发挥本来的性能了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1073(): pass

    label('loc_1073')

    Jump('loc_10D3')

    def _loc_1076(): pass

    label('loc_1076')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_10D3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_10C1',
    )

    OP_4A(0x001B, 255)

    ChrTalk(
        0x00FE,
        (
            '时间不多，要慎重。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '很快就会再有船来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x001B, 255)

    Jump('loc_10D3')

    def _loc_10C1(): pass

    label('loc_10C1')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    OP_4A(0x001B, 255)
    Call(0, 0x0006)
    OP_4B(0x001B, 255)

    def _loc_10D3(): pass

    label('loc_10D3')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x10D7
@scena.Code('func_08_10D7')
def func_08_10D7():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_11B5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1172',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，结晶回路还有效，\n',
            '导力器实体也没有异常……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，重要的装置\n',
            '为什么不能动呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这可能有什么\n',
            '根本性的问题也不一定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_11B2')

    def _loc_1172(): pass

    label('loc_1172')

    ChrTalk(
        0x00FE,
        (
            '所有导力器\n',
            '都找不到异常。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过……\n',
            '装置就是不能动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11B2(): pass

    label('loc_11B2')

    Jump('loc_1568')

    def _loc_11B5(): pass

    label('loc_11B5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_12CA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1272',
    )

    ChrTalk(
        0x00FE,
        (
            '导力器停止的原因\n',
            '我们维修员也不明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果库莱泽在\n',
            '说不定能知道些什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他现在肯定作为『埃尔赛尤』的乘员\n',
            '在那边努力吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们也只能\n',
            '尽自己所能了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_12C7')

    def _loc_1272(): pass

    label('loc_1272')

    ChrTalk(
        0x00FE,
        (
            '导力器停止的原因\n',
            '还完全不明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '库莱泽也一定\n',
            '在『埃尔赛尤』舰上\n',
            '努力着吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12C7(): pass

    label('loc_12C7')

    Jump('loc_1568')

    def _loc_12CA(): pass

    label('loc_12CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_1362',
    )

    ChrTalk(
        0x00FE,
        (
            '豆豆作为维修员\n',
            '离能够独当一面的时候\n',
            '也不远了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样库莱泽就能\n',
            '安心投入研究工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '工作变得更忙了…\n',
            '不过，为了伙伴要加油啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1568')

    def _loc_1362(): pass

    label('loc_1362')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_13B8',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，下一艘船的接纳准备\n',
            '只能靠我们来做了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为豆豆\n',
            '去了主日学校。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1568')

    def _loc_13B8(): pass

    label('loc_13B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1522',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1437',
    )

    ChrTalk(
        0x00FE,
        (
            '为了让哥哥库莱泽放心，\n',
            '豆豆比别的孩子更加努力呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '再过一阵子，那孩子\n',
            '一定能成为出色的维修员的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_151F')

    def _loc_1437(): pass

    label('loc_1437')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '库莱泽身为研究者\n',
            '也受到了极高评价。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '中央工房都来邀请他\n',
            '参加新型引擎的开发计划。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是他为了照料豆豆\n',
            '就拒绝了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就是因为这个吧，\n',
            '豆豆比别的孩子更加努力呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '再过一阵子，那孩子\n',
            '一定能成为独当一面的维修员哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_151F(): pass

    label('loc_151F')

    Jump('loc_1568')

    def _loc_1522(): pass

    label('loc_1522')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_1568',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1556',
    )

    ChrTalk(
        0x00FE,
        (
            '不好意思，\n',
            '我们正在商量工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1568')

    def _loc_1556(): pass

    label('loc_1556')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    OP_4A(0x001A, 255)
    Call(0, 0x0006)
    OP_4B(0x001A, 255)

    def _loc_1568(): pass

    label('loc_1568')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x156C
@scena.Code('func_09_156C')
def func_09_156C():
    Call(0, 0x000A)

    Return()

# id: 0x000A offset: 0x1571
@scena.Code('func_0A_1571')
def func_0A_1571():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_158C',
    )

    OP_4A(0x0011, 255)
    Call(0, 0x0011)
    OP_4B(0x0011, 255)

    Jump('loc_18C1')

    def _loc_158C(): pass

    label('loc_158C')

    TalkBegin(0x0011)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_1612',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_15EC',
    )

    ChrTalk(
        0x0011,
        (
            '飞船公社\n',
            '也没有发来什么联络。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '导力通讯不能使用，\n',
            '这也难怪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_160F')

    def _loc_15EC(): pass

    label('loc_15EC')

    ChrTalk(
        0x0011,
        (
            '飞船公社\n',
            '也没有发来什么联络。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_160F(): pass

    label('loc_160F')

    Jump('loc_18BE')

    def _loc_1612(): pass

    label('loc_1612')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_16D4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1683',
    )

    ChrTalk(
        0x0011,
        (
            '咦，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '抱歉，定期船\n',
            '还没有恢复的迹象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '现在，时刻表上面\n',
            '都贴着那张纸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_16D1')

    def _loc_1683(): pass

    label('loc_1683')

    ChrTalk(
        0x0011,
        (
            '定期船好像都停在\n',
            '各地的飞船坪呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '不过，没有出现坠落\n',
            '就算是万幸了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_16D1(): pass

    label('loc_16D1')

    Jump('loc_18BE')

    def _loc_16D4(): pass

    label('loc_16D4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_1776',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1716',
    )

    ChrTalk(
        0x0011,
        (
            '哼，可惜已经结束了。\n',
            '明明马上就要去帮忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1773')

    def _loc_1716(): pass

    label('loc_1716')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0011,
        (
            '噢，好像两阵营之间\n',
            '有发生争执嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '哼，可惜已经结束了。\n',
            '明明马上就要赶去帮忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1773(): pass

    label('loc_1773')

    Jump('loc_18BE')

    def _loc_1776(): pass

    label('loc_1776')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1843',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_17ED',
    )

    ChrTalk(
        0x0011,
        (
            '当然我是支持旅游推进派\n',
            '的诺曼先生啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '海运业的复活是不可能的啦。\n',
            '港口已经落后于时代啦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1840')

    def _loc_17ED(): pass

    label('loc_17ED')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0011,
        (
            '这次的选举对这个飞船坪\n',
            '也有很大影响啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '候选人说的话\n',
            '我一直有注意的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1840(): pass

    label('loc_1840')

    Jump('loc_18BE')

    def _loc_1843(): pass

    label('loc_1843')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_18BE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1879',
    )

    ChrTalk(
        0x0011,
        (
            '选举中也有选举中的\n',
            '精彩之处啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18BE')

    def _loc_1879(): pass

    label('loc_1879')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0011,
        (
            '呼哈啊～\n',
            '最近有点闲呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '因为在选举，\n',
            '游客好像都不来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18BE(): pass

    label('loc_18BE')

    TalkEnd(0x0011)

    def _loc_18C1(): pass

    label('loc_18C1')

    Return()

# id: 0x000B offset: 0x18C2
@scena.Code('func_0B_18C2')
def func_0B_18C2():
    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上着锁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x000C offset: 0x1908
@scena.Code('func_0C_1908')
def func_0C_1908():
    FadeOut(0, 0, -1)
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_1922',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_1926')

    def _loc_1922(): pass

    label('loc_1922')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_1926(): pass

    label('loc_1926')

    OP_DB()
    ChrSetFlags(0x0101, 0x0008)
    ChrSetFlags(0x00F7, 0x0008)
    CameraMove(132050, 8360, 87990, 0)
    OP_67(0, 9030, -10000, 0)
    CameraSetDistance(7800, 0)
    OP_6C(102000, 0)
    OP_6E(262, 0)
    PlaySE(121, 0x00, 0x64)
    OP_71(0x000A, 0x0004)
    OP_6F(0x0007, 100)
    OP_72(0x000A, 0x0004)
    ChrSetPos(0x000F, 136000, 7500, 82500, 90)
    ChrSetPos(0x0010, 136000, 5500, 82500, 90)
    ChrSetFlags(0x000F, 0x0004)
    ChrClearFlags(0x000F, 0x0040)
    OP_A1(0x000F, 0x0008)
    OP_72(0x0008, 0x0004)
    OP_72(0x0008, 0x0020)
    OP_72(0x0008, 0x0002)
    OP_71(0x0008, 0x0400)
    OP_71(0x0008, 0x0040)
    OP_A1(0x0010, 0x0009)
    OP_72(0x0009, 0x0004)
    ChrSetFlags(0x0010, 0x0004)
    ChrSetPos(0x001A, 134820, 8150, 93440, 180)
    ChrSetPos(0x001B, 132030, 8150, 94310, 180)
    ChrSetPos(0x001C, 134350, 8150, 92500, 180)
    OP_C8(0x0200, 0x0046, 'C_PLAC04._CH', 0x01, 0x07D0)
    ShowPlaceName('卢安')
    FadeIn(2000, 0)

    @scena.Lambda('lambda_1A3A')
    def lambda_1A3A():
        CameraMove(131670, 8360, 81790, 8000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_1A3A)

    @scena.Lambda('lambda_1A52')
    def lambda_1A52():
        OP_67(0, 8000, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_1A52)

    @scena.Lambda('lambda_1A6A')
    def lambda_1A6A():
        CameraSetDistance(3500, 8000)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_1A6A)

    @scena.Lambda('lambda_1A7A')
    def lambda_1A7A():
        OP_6C(134000, 8000)

        ExitThread()

    DispatchAsync(0x0001, 0x0003, lambda_1A7A)

    @scena.Lambda('lambda_1A8A')
    def lambda_1A8A():
        ChrMoveTo(0x00FE, 136000, 2500, 82500, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_1A8A)

    @scena.Lambda('lambda_1AA5')
    def lambda_1AA5():
        ChrMoveTo(0x00FE, 136000, 2000, 82500, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_1AA5)

    WaitForThreadExit(0x000F, 0x0002)
    WaitForThreadExit(0x0010, 0x0002)

    @scena.Lambda('lambda_1ACA')
    def lambda_1ACA():
        ChrMoveTo(0x00FE, 136000, 1000, 82500, 500, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0003, lambda_1ACA)

    @scena.Lambda('lambda_1AE5')
    def lambda_1AE5():
        ChrMoveTo(0x00FE, 136000, 1000, 82500, 500, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0003, lambda_1AE5)

    WaitForThreadExit(0x000F, 0x0003)
    WaitForThreadExit(0x0010, 0x0003)
    WaitForThreadExit(0x0000, 0x0000)
    WaitForThreadExit(0x0000, 0x0001)
    WaitForThreadExit(0x0000, 0x0002)
    WaitForThreadExit(0x0000, 0x0003)
    OP_23(0x0079)
    PlaySE(200, 0x00, 0x64)
    OP_7C(0, 100, 3000, 100)
    OP_B0(0x0008, 0x32)
    OP_B0(0x0009, 0x32)
    OP_6F(0x0008, 100)
    OP_70(0x0008, 1)
    OP_6F(0x0009, 100)
    OP_70(0x0009, 1)
    PlaySE(118, 0x00, 0x64)
    OP_73(0x0008)
    OP_73(0x0009)
    Sleep(400)

    OP_B0(0x0007, 0x2D)
    OP_6F(0x0007, 100)
    OP_70(0x0007, 0)
    OP_71(0x000A, 0x0004)
    PlaySE(120, 0x00, 0x64)
    OP_73(0x0007)
    Sleep(1000)

    OP_6F(0x0008, 410)
    OP_70(0x0008, 460)
    PlaySE(6, 0x00, 0x64)
    Sleep(800)

    PlaySE(6, 0x00, 0x64)
    OP_73(0x0008)
    ChrClearFlags(0x0101, 0x0008)
    ChrClearFlags(0x00F7, 0x0008)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetFlags(0x0101, 0x0040)
    ChrSetFlags(0x00F7, 0x0040)
    ChrSetFlags(0x0008, 0x0040)
    ChrSetFlags(0x0009, 0x0040)
    ChrSetFlags(0x000A, 0x0040)
    ChrSetFlags(0x000B, 0x0040)
    ChrSetFlags(0x000C, 0x0040)
    ChrSetFlags(0x000D, 0x0040)
    ChrSetFlags(0x000E, 0x0040)
    ChrSetBattleFlags(0x0101, 0x0020)
    ChrSetBattleFlags(0x00F7, 0x0020)
    ChrSetBattleFlags(0x0008, 0x0020)
    ChrSetBattleFlags(0x0009, 0x0020)
    ChrSetBattleFlags(0x000A, 0x0020)
    ChrSetBattleFlags(0x000B, 0x0020)
    ChrSetBattleFlags(0x000C, 0x0020)
    ChrSetBattleFlags(0x000D, 0x0020)
    ChrSetBattleFlags(0x000E, 0x0020)
    Yield()
    OP_89(0x0101, 137100, 8200, 82210, 90)
    OP_89(0x00F7, 137100, 8200, 82210, 90)
    OP_89(0x0008, 137100, 8200, 82210, 90)
    OP_89(0x0009, 137100, 8200, 82210, 90)
    OP_89(0x000A, 137100, 8200, 82210, 90)
    OP_89(0x000B, 137100, 8200, 82210, 90)
    OP_89(0x000C, 142970, 8300, 85160, 272)
    OP_89(0x000D, 137100, 8200, 82210, 90)
    OP_89(0x000E, 142970, 8300, 85160, 272)
    CreateThread(0x000A, 0x01, 0x00, func_0E_1DA2)
    Sleep(1000)

    CreateThread(0x0009, 0x01, 0x00, func_0E_1DA2)
    Sleep(500)

    CreateThread(0x0008, 0x01, 0x00, func_0D_1D60)
    Sleep(1000)

    CreateThread(0x000B, 0x01, 0x00, func_0D_1D60)
    Sleep(1200)

    CreateThread(0x000C, 0x01, 0x00, func_10_1E21)
    CreateThread(0x0101, 0x01, 0x00, func_0F_1DE4)
    Sleep(1000)

    CreateThread(0x00F7, 0x01, 0x00, func_0F_1DE4)
    Sleep(200)

    CreateThread(0x000E, 0x01, 0x00, func_10_1E21)
    Sleep(1200)

    CreateThread(0x000D, 0x01, 0x00, func_0D_1D60)
    FadeOut(2000, 0, -1)
    OP_0D()
    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x0010, 0x0080)
    OP_71(0x0007, 0x0004)
    OP_71(0x0008, 0x0004)
    OP_71(0x0009, 0x0004)
    OP_72(0x000A, 0x0004)
    OP_DC()
    NewScene('ED6_DT21/T2120._SN', 105, 0, 0)
    IdleLoop()

    Return()

# id: 0x000D offset: 0x1D60
@scena.Code('func_0D_1D60')
def func_0D_1D60():
    ChrWalkTo(0x00FE, 133850, 8200, 82580, 2000, 0x00)
    ChrWalkTo(0x00FE, 131700, 8200, 85050, 2000, 0x00)
    ChrWalkTo(0x00FE, 131870, 8090, 96720, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x000E offset: 0x1DA2
@scena.Code('func_0E_1DA2')
def func_0E_1DA2():
    ChrWalkTo(0x00FE, 133420, 8200, 82530, 5000, 0x00)
    ChrWalkTo(0x00FE, 131700, 8200, 85050, 5000, 0x00)
    ChrWalkTo(0x00FE, 131870, 8090, 96720, 5000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x000F offset: 0x1DE4
@scena.Code('func_0F_1DE4')
def func_0F_1DE4():
    ChrWalkTo(0x00FE, 133850, 8200, 82580, 2000, 0x00)
    ChrWalkTo(0x00FE, 131700, 8200, 85050, 2000, 0x00)
    ChrWalkTo(0x00FE, 131870, 8090, 96720, 2000, 0x00)

    Return()

# id: 0x0010 offset: 0x1E21
@scena.Code('func_10_1E21')
def func_10_1E21():
    ChrWalkTo(0x00FE, 131860, 8200, 85690, 2000, 0x00)
    ChrWalkTo(0x00FE, 131870, 8090, 96720, 2000, 0x00)

    Return()

# id: 0x0011 offset: 0x1E4A
@scena.Code('func_11_1E4A')
def func_11_1E4A():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1E64',
    )

    Call(0, 0x0028)
    FadeIn(0, 0)

    def _loc_1E64(): pass

    label('loc_1E64')

    EventBegin(0x00)
    Fade(1000)
    CameraMove(100140, 0, 83780, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3180, 0)
    OP_6C(134000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 99550, 0, 84460, 90)
    ChrSetPos(0x00F7, 99470, 0, 83460, 90)
    ChrSetPos(0x0105, 98390, 0, 84500, 90)
    ChrSetPos(0x0104, 98500, 0, 83270, 90)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 2, 0x1402)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2134',
    )

    SetScenaFlags(ScenaFlag(0x0280, 2, 0x1402))

    ChrTalk(
        0x0011,
        (
            '#3010220145V#5P噢，欢迎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3010220146V#5P去蔡斯的\n',
            '游击士一行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220147V#1011F啊，嗯，是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3010220148V#5P我收到嘉恩的联络了。\n',
            '据说船票费用协会包了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3010220149V#5P赶快办乘船手续吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00F7, 0x0101, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_203E',
    )

    ChrTalk(
        0x0106,
        (
            '#0050220150V#050F办好手续，就在这里\n',
            '等船来就行了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220151V在卢安地区\n',
            '还有事情吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_209B')

    def _loc_203E(): pass

    label('loc_203E')

    ChrTalk(
        0x0103,
        (
            '#0030220152V#020F办好手续，就在这里\n',
            '等船来就行了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220153V在卢安地区\n',
            '还有事情吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_209B(): pass

    label('loc_209B')

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
            TXT(0x00, '【还有事情】\n'),
            TXT(0x01, '【办理乘船手续】\n'),
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
        'loc_2131',
    )

    ChrTalk(
        0x0011,
        (
            '#3010220154V#5P那么，事情办完\n',
            '再来找我好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

    def _loc_2131(): pass

    label('loc_2131')

    Jump('loc_21FC')

    def _loc_2134(): pass

    label('loc_2134')

    ChrTalk(
        0x0011,
        (
            '#3010220155V#5P快快，怎样。\n',
            '办理乘船手续吗？',
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
            TXT(0x00, '【还有事情】\n'),
            TXT(0x01, '【办理乘船手续】\n'),
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
        'loc_21FC',
    )

    ChrTalk(
        0x0011,
        (
            '#3010220154V#5P那么，事情办完\n',
            '再来找我好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

    def _loc_21FC(): pass

    label('loc_21FC')

    ChrSetDirection(0x00F7, 90, 400)

    ChrTalk(
        0x0011,
        (
            '#3010220157V#5P好的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3010220158V#5P那么所有人\n',
            '都在纸上签字。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201318V#1006F嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔等人办完了乘船手续。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0011,
        (
            '#3010220160V#5P所有人都没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3010220161V#5P那么定期船到来之前\n',
            '就在飞船坪等等吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220162V#1001F好～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    OP_C0(0x15, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    Call(0, 0x0012)

    Return()

# id: 0x0012 offset: 0x2368
@scena.Code('func_12_2368')
def func_12_2368():
    MapClearFlags(0x00000001)
    CameraMove(132370, 8150, 95580, 0)
    OP_67(0, 8500, -10000, 0)
    CameraSetDistance(3050, 0)
    OP_6C(146000, 0)
    OP_6E(302, 0)
    ChrSetPos(0x000F, 136000, 1000, 82200, 90)
    ChrSetPos(0x0010, 136000, 1000, 82200, 90)
    ChrSetFlags(0x000F, 0x0004)
    ChrClearFlags(0x000F, 0x0040)
    ChrSetFlags(0x0010, 0x0004)
    ChrSetFlags(0x0010, 0x0040)
    OP_A1(0x000F, 0x000B)
    OP_A1(0x0010, 0x0009)
    OP_71(0x0008, 0x0004)
    OP_72(0x0009, 0x0004)
    OP_72(0x000B, 0x0004)
    ChrSetPos(0x0021, 132100, 8150, 96320, 185)
    ChrSetPos(0x001F, 132680, 8150, 94880, 197)
    ChrSetPos(0x000C, 131790, 8150, 94810, 185)
    ChrSetPos(0x000B, 130490, 8150, 95130, 175)
    ChrSetPos(0x0020, 131360, 8150, 96150, 177)
    ChrSetPos(0x000E, 130240, 8150, 96640, 185)
    ChrSetFlags(0x001A, 0x0080)
    ChrSetFlags(0x001B, 0x0080)
    ChrSetFlags(0x001C, 0x0080)
    OP_71(0x000A, 0x0004)
    ChrClearFlags(0x0021, 0x0080)
    ChrClearFlags(0x001F, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x0020, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetBattleFlags(0x0021, 0x0020)
    ChrSetBattleFlags(0x001F, 0x0020)
    ChrSetBattleFlags(0x000C, 0x0020)
    ChrSetBattleFlags(0x000B, 0x0020)
    ChrSetBattleFlags(0x0020, 0x0020)
    ChrSetBattleFlags(0x000E, 0x0020)
    Yield()
    ChrSetFlags(0x0021, 0x0040)
    ChrSetFlags(0x001F, 0x0040)
    ChrSetFlags(0x000C, 0x0040)
    ChrSetFlags(0x000B, 0x0040)
    ChrSetFlags(0x0020, 0x0040)
    ChrSetFlags(0x000E, 0x0040)
    ChrSetPos(0x0101, 132260, 8150, 97290, 184)
    ChrSetPos(0x00F7, 131250, 8150, 97380, 184)
    ChrSetPos(0x0104, 131250, 8150, 98500, 184)
    ChrSetPos(0x0105, 132310, 8150, 98400, 184)
    Sleep(2000)

    PlaySE(226, 0x00, 0x64)
    PlaySE(117, 0x00, 0x64)
    Sleep(2000)

    PlaySE(200, 0x00, 0x64)
    Sleep(500)

    PlaySE(118, 0x00, 0x64)
    PlaySE(120, 0x00, 0x64)
    Sleep(2000)

    OP_6F(0x000B, 1)
    OP_6F(0x0007, 0)
    FadeIn(1500, 0)
    OP_0D()
    OP_62(0x001F, 0x00000000, 1700, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    CreateThread(0x001F, 0x01, 0x00, func_15_4003)
    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    CreateThread(0x000C, 0x01, 0x00, func_16_4031)
    Sleep(300)

    CreateThread(0x000B, 0x01, 0x00, func_17_4074)
    Sleep(500)

    CreateThread(0x0021, 0x01, 0x00, func_17_4074)
    Sleep(1300)

    CreateThread(0x0020, 0x01, 0x00, func_17_4074)
    Sleep(200)

    CreateThread(0x000E, 0x01, 0x00, func_17_4074)
    Sleep(2000)

    CameraMove(131700, 8150, 97100, 1000)

    ChrTalk(
        0x0101,
        (
            '#0010220163V#1006F#5P那么……\n',
            '我们也上去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060220164V#542F#6P嗯，是啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2641')
    def lambda_2641():
        ChrWalkTo(0x00FE, 132260, 8150, 95410, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2641)

    Sleep(50)

    @scena.Lambda('lambda_2661')
    def lambda_2661():
        ChrWalkTo(0x00FE, 131250, 8150, 95660, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0000, lambda_2661)

    Sleep(50)

    @scena.Lambda('lambda_2681')
    def lambda_2681():
        ChrWalkTo(0x00FE, 132250, 8150, 96850, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0000, lambda_2681)

    Sleep(50)

    @scena.Lambda('lambda_26A1')
    def lambda_26A1():
        ChrWalkTo(0x00FE, 131120, 8150, 97090, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0000, lambda_26A1)

    Sleep(300)

    ChrSetPos(0x0012, 122550, 6150, 101030, 90)

    NpcTalk(
        0x0012,
        '男孩子的声音',
        (
            '#0400220165V#1P啊～找到了找到了！',
            TxtCtl.Enter,
        ),
    )

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x00F7, 0x0000)
    WaitForThreadExit(0x0105, 0x0000)
    WaitForThreadExit(0x0104, 0x0000)
    CloseMessageWindow()
    OP_20(0x000003E8)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0104, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x00F7, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_2785')
    def lambda_2785():
        ChrSetDirection(0x00FE, 334, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2785)

    @scena.Lambda('lambda_2793')
    def lambda_2793():
        ChrSetDirection(0x00FE, 334, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_2793)

    Sleep(100)

    @scena.Lambda('lambda_27A6')
    def lambda_27A6():
        ChrSetDirection(0x00FE, 334, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_27A6)

    @scena.Lambda('lambda_27B4')
    def lambda_27B4():
        ChrSetDirection(0x00FE, 334, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_27B4)

    OP_21()
    PlayBGM(88)
    Sleep(500)

    @scena.Lambda('lambda_27CA')
    def lambda_27CA():
        CameraMove(124110, 8150, 100440, 2000)

        ExitThread()

    DispatchAsync(0x0012, 0x0003, lambda_27CA)

    @scena.Lambda('lambda_27E2')
    def lambda_27E2():
        OP_67(0, 8000, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0012, 0x0003, lambda_27E2)

    ChrSetPos(0x0012, 122550, 6150, 101430, 90)
    ChrSetPos(0x0014, 121550, 6150, 101430, 90)
    ChrSetPos(0x0013, 120550, 6150, 101430, 90)
    ChrSetPos(0x0015, 119550, 6150, 101430, 90)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrSetFlags(0x0012, 0x0040)
    ChrSetFlags(0x0013, 0x0040)
    ChrSetFlags(0x0014, 0x0040)
    ChrSetFlags(0x0015, 0x0040)
    CreateThread(0x0012, 0x01, 0x00, func_18_40A2)
    Sleep(100)

    CreateThread(0x0014, 0x01, 0x00, func_19_40E6)
    Sleep(50)

    CreateThread(0x0013, 0x01, 0x00, func_1A_412A)
    Sleep(100)

    CreateThread(0x0015, 0x01, 0x00, func_1B_416E)
    Sleep(3000)

    @scena.Lambda('lambda_2896')
    def lambda_2896():
        CameraMove(133070, 8150, 96500, 2000)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_2896)

    @scena.Lambda('lambda_28AE')
    def lambda_28AE():
        OP_67(0, 8000, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0001, 0x0003, lambda_28AE)

    @scena.Lambda('lambda_28C6')
    def lambda_28C6():
        ChrWalkTo(0x00FE, 132620, 8150, 97510, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0000, lambda_28C6)

    Sleep(100)

    @scena.Lambda('lambda_28E6')
    def lambda_28E6():
        ChrWalkTo(0x00FE, 132710, 8150, 96340, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_28E6)

    Sleep(200)

    @scena.Lambda('lambda_2906')
    def lambda_2906():
        ChrWalkTo(0x00FE, 131490, 8150, 96340, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0000, lambda_2906)

    Sleep(100)

    @scena.Lambda('lambda_2926')
    def lambda_2926():
        ChrWalkTo(0x00FE, 131240, 8150, 97750, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0000, lambda_2926)

    WaitForThreadExit(0x0101, 0x0000)

    @scena.Lambda('lambda_2946')
    def lambda_2946():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2946)

    WaitForThreadExit(0x0105, 0x0000)

    @scena.Lambda('lambda_2959')
    def lambda_2959():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_2959)

    WaitForThreadExit(0x00F7, 0x0000)

    @scena.Lambda('lambda_296C')
    def lambda_296C():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_296C)

    WaitForThreadExit(0x0104, 0x0000)

    @scena.Lambda('lambda_297F')
    def lambda_297F():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_297F)

    WaitForThreadExit(0x0001, 0x0002)
    WaitForThreadExit(0x0001, 0x0003)

    ChrTalk(
        0x0101,
        (
            '#0010220166V#1004F#2P你、你们！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060220167V#044F大家，怎么了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0430220168V#1732F#5P来送你们了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0400220169V#772F#5P真是的，你们俩\n',
            '也太薄情啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400220170V居然瞒着我们\n',
            '就出发了～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0410220171V#1712F#5P真是，生气了哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#0420220172V#1722F#6P科洛丝姐姐。\n',
            '真的要走吗～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0015, 400)

    ChrTalk(
        0x0105,
        (
            '#0060220173V#542F#5P嗯……对不起。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060220174V本来想打个招呼的，\n',
            '但听说你们不在家……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220175V#1016F#2P原来都跑到卢安来了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220176V#1004F啊，那么\n',
            '难道特蕾莎院长也……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0018, 0x0040)
    ChrSetFlags(0x0016, 0x0040)
    ChrSetFlags(0x0017, 0x0040)
    ChrSetFlags(0x0019, 0x0040)
    ChrSetPos(0x0018, 125500, 6400, 101150, 90)
    ChrClearFlags(0x0018, 0x0080)
    ChrSetPos(0x0016, 125500, 6400, 101150, 90)
    ChrClearFlags(0x0016, 0x0080)
    ChrSetPos(0x0017, 125500, 6400, 101150, 90)
    ChrClearFlags(0x0017, 0x0080)
    ChrSetPos(0x0019, 125500, 6400, 101150, 90)
    ChrClearFlags(0x0019, 0x0080)

    NpcTalk(
        0x0018,
        '女性的声音',
        (
            '#0390220177V#5P呜呼呼。\n',
            '看来赶上了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    CreateThread(0x0018, 0x03, 0x00, func_25_43E1)
    CreateThread(0x0018, 0x01, 0x00, func_1C_41B2)
    Sleep(500)

    CreateThread(0x0016, 0x01, 0x00, func_1D_41F6)

    @scena.Lambda('lambda_2C7F')
    def lambda_2C7F():
        ChrTurnDirection(0x00FE, 0x0018, 400)
        Yield()

        Jump('lambda_2C7F')

    DispatchAsync2(0x0101, 0x0001, lambda_2C7F)

    @scena.Lambda('lambda_2C90')
    def lambda_2C90():
        ChrTurnDirection(0x00FE, 0x0018, 400)
        Yield()

        Jump('lambda_2C90')

    DispatchAsync2(0x00F7, 0x0001, lambda_2C90)

    CreateThread(0x0104, 0x00, 0x00, func_27_441A)
    CreateThread(0x0105, 0x00, 0x00, func_26_4401)
    Sleep(500)

    @scena.Lambda('lambda_2CB4')
    def lambda_2CB4():
        CameraMove(133670, 8150, 96500, 2000)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_2CB4)

    @scena.Lambda('lambda_2CCC')
    def lambda_2CCC():
        OP_67(0, 8000, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0001, 0x0003, lambda_2CCC)

    CreateThread(0x0017, 0x01, 0x00, func_1E_423A)
    CreateThread(0x0019, 0x01, 0x00, func_1F_427E)
    WaitForThreadExit(0x0018, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010220178V#1008F#2P院长老师！\n',
            '还有乔儿你们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#0510220179V#641F#5P啊哈哈！\n',
            '感觉真是刚刚好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#0520220180V#734F哈，突然想\n',
            '给你们个惊喜，\n',
            '于是就这样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#0510220181V#648F#5P嗯，结果是万事大吉啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#0390220182V#751F#5P其实是乔儿他们\n',
            '告诉我\n',
            '你们要出发的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390220183V所以，机会难得\n',
            '就大家一起来送行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0019, 0x0001)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x00F7, 0x01)
    TerminateThread(0x0104, 0x01)
    TerminateThread(0x0105, 0x01)

    ChrTalk(
        0x0019,
        (
            '#0530220184V#781F#5P呵呵，既然顺路\n',
            '我也陪着来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060220185V#542F#6P是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0400220186V#775F#5P……对了，艾丝蒂尔姐姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400220187V约修亚哥哥……\n',
            '离家出走了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200778V#1026F#2P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0410220189V#1713F#5P我们听老师\n',
            '说了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220190V#1007F#2P是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220191V#1003F抱歉哦，瞒着大家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0410220192V#1710F#5P不，没关系的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0410220193V#1718F#5P那个，我们\n',
            '会每天向女神祈祷的！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0410220194V#5P希望约修亚哥哥\n',
            '能早日回来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#0420220195V#1721F#6P我也会祈祷的～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0430220196V#1732F#5P一定会实现的～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220197V#1025F#2P大家……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060220198V#048F#6P呵呵，谢谢你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#0510220199V#644F#5P还有我们\n',
            '也会向女神祈祷的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510220200V#648F艾丝蒂尔、科洛丝。\n',
            '你们也要多加小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#0520220201V#730F你们虽然要加油，\n',
            '但可别太勉强而招致危险哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520220202V如果发生危险，那家伙\n',
            '绝对无法原谅自己的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060220203V#542F#6P乔儿、汉斯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220204V#1017F#2P嗯……\n',
            '我会铭记于心的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#0390220205V#750F#5P艾丝蒂尔，科洛丝\n',
            '就请你们多多关照了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390220206V虽然看起来坚强，\n',
            '其实她也是有脆弱一面的女孩子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0105, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(500)

    ChrTalk(
        0x0105,
        (
            '#0060220207V#540F#6P老，老师……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220208V#1008F#2P嘿嘿，交给我吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220209V#1016F话虽这么说，其实是她经常\n',
            '帮助我才对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#0390220210V#751F#5P呵呵……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390220211V#750F科洛丝，要趁此机会\n',
            '好好看清楚自己。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390220212V自己应该做什么\n',
            '慢慢找到答案就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060220213V#048F#6P是……我明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '#0530220214V#783F#5P游击士和学生……\n',
            '两者都有自己的目标。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530220215V#780F两人应该都在之前的日子里\n',
            '充分成长了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530220216V不要过于相信自己的力量，\n',
            '能运用自如就好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530220217V#781F这样的话就一定\n',
            '能渡过重重难关。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F#2P#1K是！',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x0105,
        (
            '#0060220219V#041F#6P#1K是！',
            TxtCtl.Enter,
        ),
    )

    OP_56(0x01)
    OP_59()
    Sleep(500)

    PlaySE(166, 0x00, 0x64)
    Sleep(500)

    TalkSetChrName('女性的声音')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0880220220V前往蔡斯方向的定期船，\n',
            '『赛希莉亚号』即将升空。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0880220221V需要乘坐的旅客请立即登船。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0101,
        (
            '#0010220222V#1004F#2P啊，不好……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    @scena.Lambda('lambda_35C5')
    def lambda_35C5():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_35C5')

    DispatchAsync2(0x0012, 0x0001, lambda_35C5)

    @scena.Lambda('lambda_35D6')
    def lambda_35D6():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_35D6')

    DispatchAsync2(0x0014, 0x0001, lambda_35D6)

    Sleep(100)

    @scena.Lambda('lambda_35EC')
    def lambda_35EC():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_35EC')

    DispatchAsync2(0x0013, 0x0001, lambda_35EC)

    @scena.Lambda('lambda_35FD')
    def lambda_35FD():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_35FD')

    DispatchAsync2(0x0015, 0x0001, lambda_35FD)

    Sleep(100)

    @scena.Lambda('lambda_3613')
    def lambda_3613():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_3613')

    DispatchAsync2(0x0018, 0x0001, lambda_3613)

    @scena.Lambda('lambda_3624')
    def lambda_3624():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_3624')

    DispatchAsync2(0x0016, 0x0001, lambda_3624)

    @scena.Lambda('lambda_3635')
    def lambda_3635():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_3635')

    DispatchAsync2(0x0017, 0x0001, lambda_3635)

    @scena.Lambda('lambda_3646')
    def lambda_3646():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_3646')

    DispatchAsync2(0x0019, 0x0001, lambda_3646)

    CreateThread(0x0101, 0x01, 0x00, func_20_42C2)
    Sleep(800)

    CreateThread(0x00F7, 0x01, 0x00, func_20_42C2)
    Sleep(300)

    CreateThread(0x0105, 0x01, 0x00, func_20_42C2)
    Sleep(500)

    CreateThread(0x0104, 0x01, 0x00, func_20_42C2)
    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x00F7, 0x01)
    TerminateThread(0x0105, 0x01)
    TerminateThread(0x0104, 0x01)
    TerminateThread(0x0012, 0x01)
    TerminateThread(0x0014, 0x01)
    TerminateThread(0x0013, 0x01)
    TerminateThread(0x0015, 0x01)
    TerminateThread(0x0018, 0x01)
    TerminateThread(0x0016, 0x01)
    TerminateThread(0x0017, 0x01)
    TerminateThread(0x0019, 0x01)
    ChrSetPos(0x0012, 133000, 8090, 94500, 180)
    ChrSetPos(0x0014, 132610, 8090, 95000, 180)
    ChrSetPos(0x0013, 131710, 8090, 94500, 180)
    ChrSetPos(0x0015, 131100, 8090, 94800, 180)
    ChrSetPos(0x0018, 133310, 8090, 95600, 180)
    ChrSetPos(0x0016, 132610, 8090, 96200, 180)
    ChrSetPos(0x0017, 131610, 8090, 96200, 180)
    ChrSetPos(0x0019, 132300, 8150, 97250, 180)
    ChrSetFlags(0x0000, 0x0020)
    ChrSetFlags(0x0001, 0x0020)
    ChrSetFlags(0x0002, 0x0020)
    ChrSetFlags(0x0003, 0x0020)
    Yield()
    ChrSetPos(0x00F7, 133390, 8200, 84310, 0)
    ChrSetPos(0x0101, 132420, 8200, 84780, 0)
    ChrSetPos(0x0105, 131400, 8200, 84690, 0)
    ChrSetPos(0x0104, 132250, 8200, 83530, 0)
    ChrSetSubChip(0x00F7, 0)
    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x0105, 0)
    ChrSetSubChip(0x0104, 0)
    CameraMove(132310, 8090, 90270, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3690, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    Sleep(500)

    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010220223V#1018F#2P那么，再见了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060220224V#048F#5P大家……多保重。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0400220225V#771F#7P姐姐你们也多保重啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#0510220226V#641F#6P期待你们的旅行见闻\n',
            '和约修亚哟！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    OP_DB()
    Fade(1000)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x00F7, 0x0080)
    ChrSetFlags(0x0105, 0x0080)
    ChrSetFlags(0x0104, 0x0080)
    MapClearFlags(0x00000010)
    CameraMove(132160, 8200, 85340, 0)
    OP_67(0, 11210, -10000, 0)
    CameraSetDistance(4730, 0)
    OP_6C(45000, 0)
    OP_6E(302, 0)
    OP_0D()
    PlaySE(226, 0x00, 0x64)
    PlaySE(120, 0x00, 0x64)
    OP_6F(0x0007, 0)
    OP_70(0x0007, 100)
    OP_73(0x0007)
    PlaySE(118, 0x00, 0x64)
    OP_6F(0x000B, 1)
    OP_70(0x000B, 60)
    OP_73(0x000B)
    Sleep(500)

    ChrSetFlags(0x0000, 0x0020)
    ChrSetFlags(0x0001, 0x0020)
    ChrSetFlags(0x0002, 0x0020)
    ChrSetFlags(0x0003, 0x0020)
    OP_23(0x0075)
    PlaySE(119, 0x00, 0x64)
    CreateThread(0x000F, 0x02, 0x00, func_13_3F97)

    @scena.Lambda('lambda_3978')
    def lambda_3978():
        CameraMove(160160, 8200, 85340, 12000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3978)

    @scena.Lambda('lambda_3990')
    def lambda_3990():
        ChrTurnDirection(0x00FE, 0x0013, 400)
        Yield()

        Jump('lambda_3990')

    DispatchAsync2(0x0101, 0x0002, lambda_3990)

    @scena.Lambda('lambda_39A1')
    def lambda_39A1():
        ChrTurnDirection(0x00FE, 0x0012, 400)
        Yield()

        Jump('lambda_39A1')

    DispatchAsync2(0x00F7, 0x0002, lambda_39A1)

    @scena.Lambda('lambda_39B2')
    def lambda_39B2():
        ChrTurnDirection(0x00FE, 0x0014, 400)
        Yield()

        Jump('lambda_39B2')

    DispatchAsync2(0x0105, 0x0002, lambda_39B2)

    @scena.Lambda('lambda_39C3')
    def lambda_39C3():
        ChrTurnDirection(0x00FE, 0x0015, 400)
        Yield()

        Jump('lambda_39C3')

    DispatchAsync2(0x0104, 0x0002, lambda_39C3)

    @scena.Lambda('lambda_39D4')
    def lambda_39D4():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_39D4')

    DispatchAsync2(0x0013, 0x0002, lambda_39D4)

    @scena.Lambda('lambda_39E5')
    def lambda_39E5():
        ChrTurnDirection(0x00FE, 0x00F7, 400)
        Yield()

        Jump('lambda_39E5')

    DispatchAsync2(0x0012, 0x0002, lambda_39E5)

    @scena.Lambda('lambda_39F6')
    def lambda_39F6():
        ChrTurnDirection(0x00FE, 0x0105, 400)
        Yield()

        Jump('lambda_39F6')

    DispatchAsync2(0x0014, 0x0002, lambda_39F6)

    @scena.Lambda('lambda_3A07')
    def lambda_3A07():
        ChrTurnDirection(0x00FE, 0x0104, 400)
        Yield()

        Jump('lambda_3A07')

    DispatchAsync2(0x0015, 0x0002, lambda_3A07)

    @scena.Lambda('lambda_3A18')
    def lambda_3A18():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_3A18')

    DispatchAsync2(0x0016, 0x0002, lambda_3A18)

    @scena.Lambda('lambda_3A29')
    def lambda_3A29():
        ChrTurnDirection(0x00FE, 0x00F7, 400)
        Yield()

        Jump('lambda_3A29')

    DispatchAsync2(0x0018, 0x0002, lambda_3A29)

    @scena.Lambda('lambda_3A3A')
    def lambda_3A3A():
        ChrTurnDirection(0x00FE, 0x0105, 400)
        Yield()

        Jump('lambda_3A3A')

    DispatchAsync2(0x0017, 0x0002, lambda_3A3A)

    @scena.Lambda('lambda_3A4B')
    def lambda_3A4B():
        ChrTurnDirection(0x00FE, 0x0104, 400)
        Yield()

        Jump('lambda_3A4B')

    DispatchAsync2(0x0019, 0x0002, lambda_3A4B)

    @scena.Lambda('lambda_3A5C')
    def lambda_3A5C():
        ChrMoveTo(0x00FE, 160000, 3550, 82000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_3A5C)

    @scena.Lambda('lambda_3A77')
    def lambda_3A77():
        ChrMoveTo(0x00FE, 160000, 1200, 82000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_3A77)

    @scena.Lambda('lambda_3A92')
    def lambda_3A92():
        ChrMoveToRelativeAsync(0x00FE, 24000, 2650, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_3A92)

    @scena.Lambda('lambda_3AAD')
    def lambda_3AAD():
        ChrMoveToRelativeAsync(0x00FE, 24000, 2650, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_3AAD)

    @scena.Lambda('lambda_3AC8')
    def lambda_3AC8():
        ChrMoveToRelativeAsync(0x00FE, 24000, 2650, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_3AC8)

    @scena.Lambda('lambda_3AE3')
    def lambda_3AE3():
        ChrMoveToRelativeAsync(0x00FE, 24000, 2650, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_3AE3)

    Sleep(600)

    @scena.Lambda('lambda_3B03')
    def lambda_3B03():
        ChrMoveTo(0x00FE, 160000, 4550, 82000, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_3B03)

    @scena.Lambda('lambda_3B1E')
    def lambda_3B1E():
        ChrMoveTo(0x00FE, 160000, 1200, 82000, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_3B1E)

    @scena.Lambda('lambda_3B39')
    def lambda_3B39():
        ChrMoveToRelativeAsync(0x00FE, 24000, 2650, 0, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_3B39)

    @scena.Lambda('lambda_3B54')
    def lambda_3B54():
        ChrMoveToRelativeAsync(0x00FE, 24000, 2650, 0, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_3B54)

    @scena.Lambda('lambda_3B6F')
    def lambda_3B6F():
        ChrMoveToRelativeAsync(0x00FE, 24000, 2650, 0, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_3B6F)

    @scena.Lambda('lambda_3B8A')
    def lambda_3B8A():
        ChrMoveToRelativeAsync(0x00FE, 24000, 2650, 0, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_3B8A)

    Sleep(700)

    @scena.Lambda('lambda_3BAA')
    def lambda_3BAA():
        ChrMoveTo(0x00FE, 160000, 5550, 82000, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_3BAA)

    @scena.Lambda('lambda_3BC5')
    def lambda_3BC5():
        ChrMoveTo(0x00FE, 160000, 1200, 82000, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_3BC5)

    @scena.Lambda('lambda_3BE0')
    def lambda_3BE0():
        ChrMoveToRelativeAsync(0x00FE, 24000, 2650, 0, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_3BE0)

    @scena.Lambda('lambda_3BFB')
    def lambda_3BFB():
        ChrMoveToRelativeAsync(0x00FE, 24000, 2650, 0, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_3BFB)

    @scena.Lambda('lambda_3C16')
    def lambda_3C16():
        ChrMoveToRelativeAsync(0x00FE, 24000, 2650, 0, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_3C16)

    @scena.Lambda('lambda_3C31')
    def lambda_3C31():
        ChrMoveToRelativeAsync(0x00FE, 24000, 2650, 0, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_3C31)

    Sleep(800)

    CreateThread(0x0012, 0x00, 0x00, func_21_42F2)
    CreateThread(0x0014, 0x00, 0x00, func_22_432A)
    CreateThread(0x0013, 0x00, 0x00, func_23_4367)
    CreateThread(0x0015, 0x00, 0x00, func_24_43A4)

    @scena.Lambda('lambda_3C6D')
    def lambda_3C6D():
        ChrMoveTo(0x00FE, 160000, 6550, 82000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_3C6D)

    @scena.Lambda('lambda_3C88')
    def lambda_3C88():
        ChrMoveTo(0x00FE, 160000, 1200, 82000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_3C88)

    @scena.Lambda('lambda_3CA3')
    def lambda_3CA3():
        ChrMoveToRelativeAsync(0x00FE, 24000, 2650, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_3CA3)

    @scena.Lambda('lambda_3CBE')
    def lambda_3CBE():
        ChrMoveToRelativeAsync(0x00FE, 24000, 2650, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_3CBE)

    @scena.Lambda('lambda_3CD9')
    def lambda_3CD9():
        ChrMoveToRelativeAsync(0x00FE, 24000, 2650, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_3CD9)

    @scena.Lambda('lambda_3CF4')
    def lambda_3CF4():
        ChrMoveToRelativeAsync(0x00FE, 24000, 2650, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_3CF4)

    Sleep(900)

    @scena.Lambda('lambda_3D14')
    def lambda_3D14():
        ChrMoveTo(0x00FE, 160000, 7550, 82000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_3D14)

    @scena.Lambda('lambda_3D2F')
    def lambda_3D2F():
        ChrMoveTo(0x00FE, 160000, 1200, 82000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_3D2F)

    @scena.Lambda('lambda_3D4A')
    def lambda_3D4A():
        ChrMoveToRelativeAsync(0x00FE, 24000, 2650, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_3D4A)

    @scena.Lambda('lambda_3D65')
    def lambda_3D65():
        ChrMoveToRelativeAsync(0x00FE, 24000, 2650, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_3D65)

    @scena.Lambda('lambda_3D80')
    def lambda_3D80():
        ChrMoveToRelativeAsync(0x00FE, 24000, 2650, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_3D80)

    @scena.Lambda('lambda_3D9B')
    def lambda_3D9B():
        ChrMoveToRelativeAsync(0x00FE, 24000, 2650, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_3D9B)

    Sleep(1500)

    @scena.Lambda('lambda_3DBB')
    def lambda_3DBB():
        ChrMoveTo(0x00FE, 160000, 8550, 82000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_3DBB)

    @scena.Lambda('lambda_3DD6')
    def lambda_3DD6():
        ChrMoveTo(0x00FE, 160000, 1200, 82000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_3DD6)

    @scena.Lambda('lambda_3DF1')
    def lambda_3DF1():
        ChrMoveToRelativeAsync(0x00FE, 24000, 2650, 0, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_3DF1)

    @scena.Lambda('lambda_3E0C')
    def lambda_3E0C():
        ChrMoveToRelativeAsync(0x00FE, 24000, 2650, 0, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_3E0C)

    @scena.Lambda('lambda_3E27')
    def lambda_3E27():
        ChrMoveToRelativeAsync(0x00FE, 24000, 2650, 0, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_3E27)

    @scena.Lambda('lambda_3E42')
    def lambda_3E42():
        ChrMoveToRelativeAsync(0x00FE, 24000, 2650, 0, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_3E42)

    Sleep(1500)

    OP_20(0x00000FA0)
    FadeOut(2000, 0, -1)
    Sleep(1000)

    CreateThread(0x000F, 0x03, 0x00, func_14_3FC0)

    @scena.Lambda('lambda_3E7D')
    def lambda_3E7D():
        ChrMoveTo(0x00FE, 160000, 9550, 82000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_3E7D)

    @scena.Lambda('lambda_3E98')
    def lambda_3E98():
        ChrMoveTo(0x00FE, 160000, 1200, 82000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_3E98)

    @scena.Lambda('lambda_3EB3')
    def lambda_3EB3():
        ChrMoveToRelativeAsync(0x00FE, 24000, 2650, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_3EB3)

    @scena.Lambda('lambda_3ECE')
    def lambda_3ECE():
        ChrMoveToRelativeAsync(0x00FE, 24000, 2650, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_3ECE)

    @scena.Lambda('lambda_3EE9')
    def lambda_3EE9():
        ChrMoveToRelativeAsync(0x00FE, 24000, 2650, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_3EE9)

    @scena.Lambda('lambda_3F04')
    def lambda_3F04():
        ChrMoveToRelativeAsync(0x00FE, 24000, 2650, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_3F04)

    OP_0D()
    ChrClearFlags(0x0000, 0x0004)
    ChrClearFlags(0x0001, 0x0004)
    ChrClearFlags(0x0002, 0x0004)
    ChrClearFlags(0x0003, 0x0004)
    ChrClearFlags(0x0000, 0x0020)
    ChrClearFlags(0x0001, 0x0020)
    ChrClearFlags(0x0002, 0x0020)
    ChrClearFlags(0x0003, 0x0020)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x03, 0xFF)
    SetScenaFlags(ScenaFlag(0x0280, 3, 0x1403))
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    OP_28(0x0065, 0x04, 0x40)
    OP_28(0x0066, 0x04, 0x40)
    OP_28(0x0067, 0x04, 0x40)
    OP_28(0x0068, 0x04, 0x40)
    OP_28(0x0069, 0x04, 0x40)
    OP_28(0x006B, 0x04, 0x40)
    OP_28(0x00A1, 0x04, 0x40)
    OP_28(0x00A2, 0x04, 0x40)
    OP_28(0x00A3, 0x04, 0x40)
    OP_28(0x00A4, 0x04, 0x40)
    OP_21()
    Sleep(1000)

    OP_DC()
    NewScene('ED6_DT21/E0001._SN', 104, 0, 0)
    IdleLoop()

    Return()

# id: 0x0013 offset: 0x3F97
@scena.Code('func_13_3F97')
def func_13_3F97():
    OP_B0(0x000B, 0x32)
    OP_6F(0x000B, 61)
    OP_70(0x000B, 160)
    OP_73(0x000B)
    OP_71(0x000B, 0x0020)
    OP_6F(0x000B, 161)
    OP_70(0x000B, 260)

    Return()

# id: 0x0014 offset: 0x3FC0
@scena.Code('func_14_3FC0')
def func_14_3FC0():
    OP_24(0x0077, 0x5A)
    Sleep(300)

    OP_24(0x0077, 0x50)
    Sleep(300)

    OP_24(0x0077, 0x46)
    Sleep(300)

    OP_24(0x0077, 0x3C)
    Sleep(300)

    OP_24(0x0077, 0x32)
    Sleep(300)

    OP_24(0x0077, 0x28)
    Sleep(300)

    OP_24(0x0077, 0x1E)
    Sleep(300)

    OP_23(0x0077)

    Return()

# id: 0x0015 offset: 0x4003
@scena.Code('func_15_4003')
def func_15_4003():
    ChrWalkTo(0x00FE, 131920, 8300, 93820, 6000, 0x00)
    ChrWalkTo(0x00FE, 131930, 8150, 81870, 6000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0016 offset: 0x4031
@scena.Code('func_16_4031')
def func_16_4031():
    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x00)
    ChrWalkTo(0x00FE, 131920, 8300, 93820, 4000, 0x00)
    ChrWalkTo(0x00FE, 131930, 8150, 81870, 4000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)
    OP_63(0x00FE)

    Return()

# id: 0x0017 offset: 0x4074
@scena.Code('func_17_4074')
def func_17_4074():
    ChrWalkTo(0x00FE, 131920, 8300, 93820, 2000, 0x00)
    ChrWalkTo(0x00FE, 131930, 8150, 81870, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0018 offset: 0x40A2
@scena.Code('func_18_40A2')
def func_18_40A2():
    ChrWalkTo(0x00FE, 134840, 8150, 100700, 4000, 0x00)
    ChrWalkTo(0x00FE, 134730, 8150, 98370, 4000, 0x00)
    ChrWalkTo(0x00FE, 133730, 8150, 95150, 4000, 0x00)
    ChrTurnDirection(0x00FE, 0x0101, 400)

    Return()

# id: 0x0019 offset: 0x40E6
@scena.Code('func_19_40E6')
def func_19_40E6():
    ChrWalkTo(0x00FE, 134840, 8150, 100700, 4000, 0x00)
    ChrWalkTo(0x00FE, 135110, 8150, 98880, 4000, 0x00)
    ChrWalkTo(0x00FE, 133880, 8150, 96110, 4000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)

    Return()

# id: 0x001A offset: 0x412A
@scena.Code('func_1A_412A')
def func_1A_412A():
    ChrWalkTo(0x00FE, 134840, 8150, 100700, 4000, 0x00)
    ChrWalkTo(0x00FE, 134890, 8150, 98910, 4000, 0x00)
    ChrWalkTo(0x00FE, 133580, 8150, 97160, 4000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)

    Return()

# id: 0x001B offset: 0x416E
@scena.Code('func_1B_416E')
def func_1B_416E():
    ChrWalkTo(0x00FE, 134840, 8150, 100700, 4000, 0x00)
    ChrWalkTo(0x00FE, 134980, 8150, 98850, 4000, 0x00)
    ChrWalkTo(0x00FE, 133050, 8150, 98180, 4000, 0x00)
    ChrTurnDirection(0x00FE, 0x0105, 400)

    Return()

# id: 0x001C offset: 0x41B2
@scena.Code('func_1C_41B2')
def func_1C_41B2():
    ChrWalkTo(0x00FE, 129250, 6150, 101380, 3000, 0x00)
    ChrWalkTo(0x00FE, 134840, 8150, 100700, 3000, 0x00)
    ChrWalkTo(0x00FE, 134710, 8150, 96490, 3000, 0x00)
    ChrTurnDirection(0x00FE, 0x0101, 400)

    Return()

# id: 0x001D offset: 0x41F6
@scena.Code('func_1D_41F6')
def func_1D_41F6():
    ChrWalkTo(0x00FE, 129250, 6150, 101380, 3000, 0x00)
    ChrWalkTo(0x00FE, 134840, 8150, 100700, 3000, 0x00)
    ChrWalkTo(0x00FE, 134450, 8150, 97590, 3000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)

    Return()

# id: 0x001E offset: 0x423A
@scena.Code('func_1E_423A')
def func_1E_423A():
    ChrWalkTo(0x00FE, 129250, 6150, 101380, 3000, 0x00)
    ChrWalkTo(0x00FE, 134840, 8150, 100700, 3000, 0x00)
    ChrWalkTo(0x00FE, 135420, 8150, 97250, 3000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)

    Return()

# id: 0x001F offset: 0x427E
@scena.Code('func_1F_427E')
def func_1F_427E():
    ChrWalkTo(0x00FE, 129250, 6150, 101380, 2000, 0x00)
    ChrWalkTo(0x00FE, 134840, 8150, 100700, 2000, 0x00)
    ChrWalkTo(0x00FE, 135140, 8150, 98460, 2000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)

    Return()

# id: 0x0020 offset: 0x42C2
@scena.Code('func_20_42C2')
def func_20_42C2():
    ChrSetDirection(0x00FE, 180, 400)
    ChrWalkTo(0x00FE, 131960, 8150, 94450, 2000, 0x00)
    ChrWalkTo(0x00FE, 132130, 8090, 87220, 2000, 0x00)

    Return()

# id: 0x0021 offset: 0x42F2
@scena.Code('func_21_42F2')
def func_21_42F2():
    TerminateThread(0x00FE, 0x02)
    ChrSetDirection(0x00FE, 90, 600)
    ChrWalkTo(0x00FE, 140500, 8150, 94000, 4000, 0x00)
    ChrSetDirection(0x00FE, 185, 400)

    @scena.Lambda('lambda_431E')
    def lambda_431E():
        ChrTurnDirection(0x00FE, 0x00F7, 400)
        Yield()

        Jump('lambda_431E')

    DispatchAsync2(0x0012, 0x0002, lambda_431E)

    Return()

# id: 0x0022 offset: 0x432A
@scena.Code('func_22_432A')
def func_22_432A():
    Sleep(300)

    TerminateThread(0x00FE, 0x02)
    ChrSetDirection(0x00FE, 90, 600)
    ChrWalkTo(0x00FE, 140000, 8150, 94670, 4000, 0x00)
    ChrSetDirection(0x00FE, 185, 400)

    @scena.Lambda('lambda_435B')
    def lambda_435B():
        ChrTurnDirection(0x00FE, 0x0105, 400)
        Yield()

        Jump('lambda_435B')

    DispatchAsync2(0x0014, 0x0002, lambda_435B)

    Return()

# id: 0x0023 offset: 0x4367
@scena.Code('func_23_4367')
def func_23_4367():
    Sleep(500)

    TerminateThread(0x00FE, 0x02)
    ChrSetDirection(0x00FE, 90, 600)
    ChrWalkTo(0x00FE, 138910, 8150, 94150, 4000, 0x00)
    ChrSetDirection(0x00FE, 185, 400)

    @scena.Lambda('lambda_4398')
    def lambda_4398():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_4398')

    DispatchAsync2(0x0013, 0x0002, lambda_4398)

    Return()

# id: 0x0024 offset: 0x43A4
@scena.Code('func_24_43A4')
def func_24_43A4():
    Sleep(800)

    TerminateThread(0x00FE, 0x02)
    ChrSetDirection(0x00FE, 90, 600)
    ChrWalkTo(0x00FE, 138310, 8150, 94750, 4000, 0x00)
    ChrSetDirection(0x00FE, 185, 400)

    @scena.Lambda('lambda_43D5')
    def lambda_43D5():
        ChrTurnDirection(0x00FE, 0x0104, 400)
        Yield()

        Jump('lambda_43D5')

    DispatchAsync2(0x0015, 0x0002, lambda_43D5)

    Return()

# id: 0x0025 offset: 0x43E1
@scena.Code('func_25_43E1')
def func_25_43E1():
    ChrSetDirection(0x0101, 354, 400)
    Sleep(500)

    ChrSetDirection(0x00F7, 354, 400)
    Sleep(500)

    ChrSetDirection(0x0104, 354, 400)

    Return()

# id: 0x0026 offset: 0x4401
@scena.Code('func_26_4401')
def func_26_4401():
    ChrSetDirection(0x00FE, 315, 400)

    @scena.Lambda('lambda_440E')
    def lambda_440E():
        ChrTurnDirection(0x00FE, 0x0018, 400)
        Yield()

        Jump('lambda_440E')

    DispatchAsync2(0x0105, 0x0001, lambda_440E)

    Return()

# id: 0x0027 offset: 0x441A
@scena.Code('func_27_441A')
def func_27_441A():
    ChrSetDirection(0x00FE, 315, 400)
    Sleep(500)

    ChrSetDirection(0x00FE, 0, 400)
    Sleep(500)

    @scena.Lambda('lambda_4438')
    def lambda_4438():
        ChrTurnDirection(0x00FE, 0x0018, 400)
        Yield()

        Jump('lambda_4438')

    DispatchAsync2(0x0104, 0x0001, lambda_4438)

    Return()

# id: 0x0028 offset: 0x4444
@scena.Code('func_28_4444')
def func_28_4444():
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
        (0x00000000, 'loc_44BE'),
        (0x00000001, 'loc_44C4'),
        (-1, 'loc_44CA'),
    )

    def _loc_44BE(): pass

    label('loc_44BE')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_44CA')

    def _loc_44C4(): pass

    label('loc_44C4')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_44CA')

    def _loc_44CA(): pass

    label('loc_44CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_44D8',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_44DC')

    def _loc_44D8(): pass

    label('loc_44D8')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_44DC(): pass

    label('loc_44DC')

    Return()

# id: 0x0029 offset: 0x44DD
@scena.Code('func_29_44DD')
def func_29_44DD():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_4544',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '定期船起降坪\n',
            '※所有航班暂时停开。\n',
            '　　　　　　　　　飞船坪接待处',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_4576')

    def _loc_4544(): pass

    label('loc_4544')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '定期船起降坪\n',
            '≡　开往柏斯市\n',
            '≡　前往蔡斯市',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_4576(): pass

    label('loc_4576')

    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x002A offset: 0x458C
@scena.Code('func_2A_458C')
def func_2A_458C():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※请勿携带易燃物和危险品\n',
            '　　　　『利贝尔飞船公社』',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x002B offset: 0x45F2
@scena.Code('func_2B_45F2')
def func_2B_45F2():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　　　飞船坪塔台　　　　\n',
            '　※无关人员禁止入内　　\n',
            '   『利贝尔飞船公社』　',
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

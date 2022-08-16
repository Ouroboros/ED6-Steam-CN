import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3102_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3102   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3102.x'
    header.mapIndex       = 1
    header.bgm            = 13
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
        ('ED6_DT07/CH01290._CH', 'ED6_DT07/CH01290P._CP'),
        ('ED6_DT07/CH02440._CH', 'ED6_DT07/CH02440P._CP'),
        ('ED6_DT07/CH02620._CH', 'ED6_DT07/CH02620P._CP'),
        ('ED6_DT07/CH02070._CH', 'ED6_DT07/CH02070P._CP'),
        ('ED6_DT07/CH01700._CH', 'ED6_DT07/CH01700P._CP'),
        ('ED6_DT07/CH02100._CH', 'ED6_DT07/CH02100P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
    ]

# id: 0x10001 offset: 0xFA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '格斯塔夫维修长',
            x                   = -37000,
            z                   = -3800,
            y                   = 145500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '吉拉尔',
            x                   = -20110,
            z                   = 8000,
            y                   = 121830,
            direction           = 177,
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
            name                = '玛多克工房长',
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
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '朵洛希',
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
            name                = '安东尼',
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
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '凯诺娜上尉',
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
            name                = '鲁特尔',
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
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '多杰',
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
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '巴拉特',
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
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '船',
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
            name                = '船影',
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
            name                = '士兵',
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '蔡斯市·工房区',
            x                   = -18770,
            z                   = 8000,
            y                   = 89560,
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

# id: 0x10002 offset: 0x2DA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x2DA
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -43700,
            y           = -4000,
            z           = 146000,
            range       = -41600,
            dword_10    = 0xFFFFF830,
            dword_14    = 0x00022A4C,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000F,
        ),
        ScenaEventData(
            x           = -43200,
            y           = -5000,
            z           = 145000,
            range       = -48600,
            dword_10    = 0xFFFFF830,
            dword_14    = 0x00022B78,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000013,
        ),
        ScenaEventData(
            x           = -15210,
            y           = 7000,
            z           = 100600,
            range       = -22980,
            dword_10    = 0x00002710,
            dword_14    = 0x0001938E,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000001A,
        ),
    )

# id: 0x10004 offset: 0x33A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -19980,
            triggerZ            = 8000,
            triggerY            = 119710,
            triggerRange        = 400,
            actorX              = -20110,
            actorZ              = 9500,
            actorY              = 121830,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000E,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -41010,
            triggerZ            = 8000,
            triggerY            = 122500,
            triggerRange        = 800,
            actorX              = -41010,
            actorZ              = 10200,
            actorY              = 122500,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0018,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -38900,
            triggerZ            = 8400,
            triggerY            = 122040,
            triggerRange        = 800,
            actorX              = -38900,
            actorZ              = 9900,
            actorY              = 122040,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0019,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x3A6
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_3BD',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_10_5CB7)
    OP_B1('T3102_1')

    def _loc_3BD(): pass

    label('loc_3BD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AC, 1, 0x561)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3DF',
    )

    ChrSetPos(0x000A, -44860, -4000, 141600, 270)
    ChrClearFlags(0x000A, 0x0080)

    def _loc_3DF(): pass

    label('loc_3DF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 3, 0x603)),
            Expr.Return,
        ),
        'loc_41C',
    )

    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, -40990, 8000, 129460, 12)
    CreateThread(0x000E, 0x00, 0x00, func_02_872)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, -44660, 8000, 129500, 5)

    Jump('loc_660')

    def _loc_41C(): pass

    label('loc_41C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_459',
    )

    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, -40990, 8000, 129460, 12)
    CreateThread(0x000E, 0x00, 0x00, func_02_872)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, -44660, 8000, 129500, 5)

    Jump('loc_660')

    def _loc_459(): pass

    label('loc_459')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_479',
    )

    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, -40990, 8000, 122890, 180)

    Jump('loc_660')

    def _loc_479(): pass

    label('loc_479')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_4E2',
    )

    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, -47500, -4000, 151780, 261)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, -47500, -4000, 152840, 261)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, -40130, 8000, 125930, 237)
    CreateThread(0x000C, 0x00, 0x00, func_04_A13)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, -44750, -4000, 146070, 81)

    Jump('loc_660')

    def _loc_4E2(): pass

    label('loc_4E2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_522',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, -44530, -4000, 142000, 176)
    ChrSetFlags(0x0008, 0x0010)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, -44510, -4000, 140610, 21)
    ChrSetFlags(0x0010, 0x0010)

    Jump('loc_660')

    def _loc_522(): pass

    label('loc_522')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_55F',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, -58040, 4000, 125930, 187)
    CreateThread(0x0008, 0x00, 0x00, func_06_A5B)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, -44750, -4000, 146070, 81)

    Jump('loc_660')

    def _loc_55F(): pass

    label('loc_55F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_569',
    )

    Jump('loc_660')

    def _loc_569(): pass

    label('loc_569')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_5A6',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, -49800, 8000, 117400, 3)
    CreateThread(0x0008, 0x00, 0x00, func_05_A37)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, -44750, -4000, 146070, 81)

    Jump('loc_660')

    def _loc_5A6(): pass

    label('loc_5A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 6, 0x516)),
            Expr.Return,
        ),
        'loc_5C6',
    )

    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, -44440, -4000, 153380, 90)

    Jump('loc_660')

    def _loc_5C6(): pass

    label('loc_5C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_5E6',
    )

    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, -44750, -4000, 146070, 81)

    Jump('loc_660')

    def _loc_5E6(): pass

    label('loc_5E6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_606',
    )

    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, -44750, -4000, 146070, 81)

    Jump('loc_660')

    def _loc_606(): pass

    label('loc_606')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_626',
    )

    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, -44750, -4000, 146070, 81)

    Jump('loc_660')

    def _loc_626(): pass

    label('loc_626')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_660',
    )

    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, -40130, 8000, 125930, 237)
    CreateThread(0x000C, 0x00, 0x00, func_04_A13)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, -44750, -4000, 146070, 81)

    def _loc_660(): pass

    label('loc_660')

    Return()

# id: 0x0001 offset: 0x661
@scena.Code('func_01_661')
def func_01_661():
    OP_16(0x02, 4000, -172000, 20000, 196691)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 4, 0x604)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6A3',
    )

    OP_B1('T3102_3')
    OP_6F(0x0000, 1001)
    OP_71(0x0004, 0x0004)
    OP_71(0x0005, 0x0004)
    OP_6F(0x0003, 100)

    Jump('loc_871')

    def _loc_6A3(): pass

    label('loc_6A3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AE, 2, 0x572)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AC, 1, 0x561)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_70C',
    )

    OP_B1('T3102_2')
    OP_6F(0x0004, 1)
    OP_6F(0x0003, 200)
    OP_71(0x0006, 0x0004)
    OP_6F(0x0000, 1001)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetPos(0x0008, -43100, -3800, 144030, 270)
    OP_25(0x0075, -34230, -4000, 144000, 10000, 40000, 0x64, 0x00000000)

    Jump('loc_871')

    def _loc_70C(): pass

    label('loc_70C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AC, 1, 0x561)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_73C',
    )

    OP_B1('T3102_2')
    OP_6F(0x0000, 250)
    OP_71(0x0004, 0x0004)
    OP_71(0x0005, 0x0004)
    OP_6F(0x0003, 100)

    Jump('loc_871')

    def _loc_73C(): pass

    label('loc_73C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_767',
    )

    OP_B1('T3102_2')
    OP_6F(0x0000, 250)
    OP_71(0x0004, 0x0004)
    OP_71(0x0005, 0x0004)
    OP_6F(0x0003, 100)

    Jump('loc_871')

    def _loc_767(): pass

    label('loc_767')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 6, 0x516)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_827',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 0, 0x518)),
            Expr.Return,
        ),
        'loc_7BB',
    )

    OP_B1('T3102_2')
    OP_6F(0x0004, 1)
    OP_6F(0x0003, 200)
    OP_71(0x0006, 0x0004)
    OP_6F(0x0000, 1001)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetPos(0x0008, -42710, -3800, 144020, 270)

    Jump('loc_824')

    def _loc_7BB(): pass

    label('loc_7BB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 7, 0x517)),
            Expr.Return,
        ),
        'loc_803',
    )

    OP_B1('T3102_2')
    OP_6F(0x0004, 1)
    OP_6F(0x0003, 200)
    OP_71(0x0006, 0x0004)
    OP_6F(0x0000, 1001)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetPos(0x0008, -36900, -3800, 140550, 90)

    Jump('loc_824')

    def _loc_803(): pass

    label('loc_803')

    OP_B1('T3102_2')
    OP_6F(0x0000, 1001)
    OP_71(0x0004, 0x0004)
    OP_71(0x0005, 0x0004)
    OP_6F(0x0003, 100)

    def _loc_824(): pass

    label('loc_824')

    Jump('loc_871')

    def _loc_827(): pass

    label('loc_827')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_850',
    )

    OP_B1('T3102_1')
    OP_6F(0x0004, 1)
    OP_6F(0x0003, 200)
    OP_6F(0x0000, 1001)

    Jump('loc_871')

    def _loc_850(): pass

    label('loc_850')

    OP_B1('T3102_2')
    OP_6F(0x0000, 1001)
    OP_71(0x0004, 0x0004)
    OP_71(0x0005, 0x0004)
    OP_6F(0x0003, 100)

    def _loc_871(): pass

    label('loc_871')

    Return()

# id: 0x0002 offset: 0x872
@scena.Code('func_02_872')
def func_02_872():
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
        'loc_897',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_9D9')

    def _loc_897(): pass

    label('loc_897')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8B0',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_9D9')

    def _loc_8B0(): pass

    label('loc_8B0')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8C9',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_9D9')

    def _loc_8C9(): pass

    label('loc_8C9')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8E2',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_9D9')

    def _loc_8E2(): pass

    label('loc_8E2')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8FB',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_9D9')

    def _loc_8FB(): pass

    label('loc_8FB')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_914',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_9D9')

    def _loc_914(): pass

    label('loc_914')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_92D',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_9D9')

    def _loc_92D(): pass

    label('loc_92D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_946',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_9D9')

    def _loc_946(): pass

    label('loc_946')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_95F',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_9D9')

    def _loc_95F(): pass

    label('loc_95F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_978',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_9D9')

    def _loc_978(): pass

    label('loc_978')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_991',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_9D9')

    def _loc_991(): pass

    label('loc_991')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9AA',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_9D9')

    def _loc_9AA(): pass

    label('loc_9AA')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9C3',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_9D9')

    def _loc_9C3(): pass

    label('loc_9C3')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9D9',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_9D9(): pass

    label('loc_9D9')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_9EE',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_9D9')

    def _loc_9EE(): pass

    label('loc_9EE')

    Return()

# id: 0x0003 offset: 0x9EF
@scena.Code('func_03_9EF')
def func_03_9EF():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_A12',
    )

    OP_8D(0x00FE, -19390, 119560, -16690, 116060, 3000)

    Jump('func_03_9EF')

    def _loc_A12(): pass

    label('loc_A12')

    Return()

# id: 0x0004 offset: 0xA13
@scena.Code('func_04_A13')
def func_04_A13():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_A36',
    )

    OP_8D(0x00FE, -35820, 123780, -43940, 129220, 3000)

    Jump('func_04_A13')

    def _loc_A36(): pass

    label('loc_A36')

    Return()

# id: 0x0005 offset: 0xA37
@scena.Code('func_05_A37')
def func_05_A37():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_A5A',
    )

    OP_8D(0x00FE, -45240, 117320, -51970, 121500, 2000)

    Jump('func_05_A37')

    def _loc_A5A(): pass

    label('loc_A5A')

    Return()

# id: 0x0006 offset: 0xA5B
@scena.Code('func_06_A5B')
def func_06_A5B():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_A7E',
    )

    OP_8D(0x00FE, -56420, 122640, -59470, 129340, 2000)

    Jump('func_06_A5B')

    def _loc_A7E(): pass

    label('loc_A7E')

    Return()

# id: 0x0007 offset: 0xA7F
@scena.Code('func_07_A7F')
def func_07_A7F():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 3, 0x603)),
            Expr.Return,
        ),
        'loc_AD0',
    )

    ChrTalk(
        0x00FE,
        (
            '呼……\n',
            '都不通知一下就检查，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '王国军真是的，\n',
            '实在太乱来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_109B')

    def _loc_AD0(): pass

    label('loc_AD0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_B2A',
    )

    ChrTalk(
        0x00FE,
        (
            '一会儿『赛希莉亚号』\n',
            '就要开过来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '必须马上开始\n',
            '确认下拢岸的状况了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_109B')

    def _loc_B2A(): pass

    label('loc_B2A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_B9E',
    )

    ChrTalk(
        0x00FE,
        (
            '工房船现在\n',
            '马上就要出航了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '却比预定去要塞的时间提前了很多……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那边发生了什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_109B')

    def _loc_B9E(): pass

    label('loc_B9E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_BF6',
    )

    ChrTalk(
        0x00FE,
        (
            '好了，\n',
            '这样飞船起航就告一段落了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之，\n',
            '趁这段时间整理一下货物吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_109B')

    def _loc_BF6(): pass

    label('loc_BF6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_CC0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_C7A',
    )

    ChrTalk(
        0x00FE,
        (
            '话说回来，这种时候\n',
            '真是羡慕雷曼那家伙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那家伙兼任驾驶员，\n',
            '飞行前为了调整身体状态，\n',
            '早早地就回家去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CBD')

    def _loc_C7A(): pass

    label('loc_C7A')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '呼，明天还是要去要塞啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近的工作\n',
            '好像很多啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x00FE, 0x0010)

    def _loc_CBD(): pass

    label('loc_CBD')

    Jump('loc_109B')

    def _loc_CC0(): pass

    label('loc_CC0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_D3D',
    )

    ChrTalk(
        0x00FE,
        (
            '中央工房的事件\n',
            '应该解决了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎？\n',
            '犯人到现在都还没抓到？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那还真是糟糕啊。\n',
            '下次不会来袭击工房船吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_109B')

    def _loc_D3D(): pass

    label('loc_D3D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_ED5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_DF8',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，都是因为那个公爵大人，\n',
            '搞得大家都对王家的印象变差了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哼，很久以前\n',
            '那种快乐纯粹的女王诞辰庆典\n',
            '是很难再出现了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '该死，那个混账公爵。\n',
            '还我的诞辰庆典来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ED2')

    def _loc_DF8(): pass

    label('loc_DF8')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '之前的休假\n',
            '我去参观了\n',
            '艾尔·雷登瀑布……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '竟遇到那个叫杜什么的公爵，\n',
            '那个王家的人微服出行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且那个人\n',
            '还蛮横任性得要命。\n',
            '真是倒了大霉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔，大家都没想到\n',
            '王家的人竟会是那个样子。\n',
            '真是失望透了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_ED2(): pass

    label('loc_ED2')

    Jump('loc_109B')

    def _loc_ED5(): pass

    label('loc_ED5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_F58',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 7, 0x517)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F0C',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯……\n',
            '差不多该到返航的时候了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F55')

    def _loc_F0C(): pass

    label('loc_F0C')

    ChrTalk(
        0x00FE,
        (
            '怎么样？很漂亮吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这可是中央工房引以为傲的\n',
            '『莱普尼兹号』啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F55(): pass

    label('loc_F55')

    Jump('loc_109B')

    def _loc_F58(): pass

    label('loc_F58')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_104D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_FC3',
    )

    ChrTalk(
        0x00FE,
        (
            '工房好像还没找出\n',
            '昨天那种现象的原因所在吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管怎样，\n',
            '希望不要再发生这种事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_104A')

    def _loc_FC3(): pass

    label('loc_FC3')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '昨天晚上，导力供应停止了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过还好不是在白天发生，\n',
            '真是万幸呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果在飞艇上出现这种情况，\n',
            '真不知道会发生什么事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_104A(): pass

    label('loc_104A')

    Jump('loc_109B')

    def _loc_104D(): pass

    label('loc_104D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_109B',
    )

    ChrTalk(
        0x00FE,
        (
            '好的，拢岸准备好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '接下来，\n',
            '要快点进行出发前的检查了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_109B(): pass

    label('loc_109B')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x109F
@scena.Code('func_08_109F')
def func_08_109F():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AE, 2, 0x572)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AC, 1, 0x561)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_131E',
    )

    EventBegin(0x00)

    ChrTalk(
        0x0008,
        (
            '#0560090605V这就出发去雷斯顿要塞吗？',
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
            TXT(0x00, '【出发】\n'),
            TXT(0x01, '【整理装备】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1141'),
        (0x00000001, 'loc_12D8'),
        (-1, 'loc_131B'),
    )

    def _loc_1141(): pass

    label('loc_1141')

    OP_4A(0x000A, 255)
    ChrSetDirection(0x000A, 315, 400)

    ChrTalk(
        0x0008,
        (
            '#0560090606V#693F好！\n',
            '那么快上去吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560090607V工房船『莱普尼兹号』，\n',
            '向目的地雷斯顿要塞进发！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0550090608V#803F#2P各位游击士……\n',
            '博士的事就拜托你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550090609V#800F还有的是……\n',
            '麻烦你们好好保护提妲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_122E')
    def lambda_122E():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_122E)

    @scena.Lambda('lambda_123C')
    def lambda_123C():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_123C)

    @scena.Lambda('lambda_124A')
    def lambda_124A():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_124A)

    ChrTurnDirection(0x0107, 0x000A, 400)

    ChrTalk(
        0x0107,
        (
            '#0070090610V#560F工房长……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090611V#006F嗯，都包在我们身上吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090612V#010F那么我们走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Call(0, 0x0011)

    Jump('loc_131B')

    def _loc_12D8(): pass

    label('loc_12D8')

    SetScenaFlags(ScenaFlag(0x00AE, 2, 0x572))

    ChrTalk(
        0x0008,
        (
            '#0560090613V#691F明白了。\n',
            '准备好了就说一声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 270, 400)
    OP_4B(0x0008, 255)
    EventEnd(0x01)

    Return()

    def _loc_131B(): pass

    label('loc_131B')

    Jump('loc_198F')

    def _loc_131E(): pass

    label('loc_131E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_13DE',
    )

    ChrTalk(
        0x00FE,
        (
            '#0560090614V#690F哦，稍微晚了些真是不好意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560090615V要塞那边又来要求我们出动了。\n',
            '我想今天之内\n',
            '就可以做好准备了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560090616V嗯，希望和平时一样\n',
            '不要发生什么意外就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_198F')

    def _loc_13DE(): pass

    label('loc_13DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 0, 0x538)),
            Expr.Return,
        ),
        'loc_149A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_142D',
    )

    ChrTalk(
        0x00FE,
        (
            '#0560090630V#690F骚乱中没有人员伤亡\n',
            '就是不幸中的大幸了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1497')

    def _loc_142D(): pass

    label('loc_142D')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '#0560090631V#690F不过，\n',
            '事情真是糟糕啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560090632V唔，骚乱中没有人员伤亡\n',
            '就是不幸中的大幸了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1497(): pass

    label('loc_1497')

    Jump('loc_198F')

    def _loc_149A(): pass

    label('loc_149A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_1677',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_14E9',
    )

    ChrTalk(
        0x00FE,
        (
            '#0560090633V#690F骚乱中没有人员伤亡\n',
            '就是不幸中的大幸了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1674')

    def _loc_14E9(): pass

    label('loc_14E9')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    ChrTurnDirection(0x0008, 0x0107, 400)

    ChrTalk(
        0x00FE,
        (
            '#0560090634V#690F哦，是提妲丫头。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560090635V事情真是糟糕啊。\n',
            '没有受伤吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090636V#063F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090637V#064F啊……是、是的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '#0560090638V#692F……发生什么事了？\n',
            '你一直在发呆啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090639V#066F嗯、嗯。\n',
            '没事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0560090640V#691F是吗，没受伤的话，\n',
            '那比什么都好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090641V#063F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1674(): pass

    label('loc_1674')

    Jump('loc_198F')

    def _loc_1677(): pass

    label('loc_1677')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_18D9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_16BC',
    )

    ChrTalk(
        0x00FE,
        (
            '#0560090629V#690F哦，是提妲丫头。\n',
            '多多保重哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18D6')

    def _loc_16BC(): pass

    label('loc_16BC')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '#0560090617V#690F哦，是提妲丫头。\n',
            '又成了拉赛尔老爷子的差使吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090618V#060F啊，是呢。\n',
            '要到亚尔摩村去一趟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0560090619V#692F亚尔摩村？\n',
            '喂喂，没问题吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560090620V之前在卡鲁迪亚隧道\n',
            '不是受到袭击了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090621V#061F嘿嘿，\n',
            '这次有两个游击士做我的护卫啊，\n',
            '所以怎么说都不要紧的啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0560090622V#692F你们好像是上次\n',
            '来拿内燃引擎设备的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560090623V#691F哎，你也是游击士啊。\n',
            '我还以为只是个盛气凌人的丫头呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560090624V那么就没什么问题了。\n',
            '路上小心点啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090625V#560F嗯，\n',
            '那么我们就出发了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18D6(): pass

    label('loc_18D6')

    Jump('loc_198F')

    def _loc_18D9(): pass

    label('loc_18D9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 0, 0x518)),
            Expr.Return,
        ),
        'loc_198F',
    )

    ChrTalk(
        0x0008,
        (
            '#0560090626V#691F话说回来， \n',
            '这也真是个有趣的巧合啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560090627V那东西刚被军方还回来，\n',
            '马上就又被老爷子借走了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560090628V那可是一般仓库都没有的\n',
            '十分稀有的物件啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_198F(): pass

    label('loc_198F')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x1993
@scena.Code('func_09_1993')
def func_09_1993():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_19B3',
    )

    PlaySE(402, 0x00, 0x64)

    ChrTalk(
        0x00FE,
        (
            '喵－噢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19CD')

    def _loc_19B3(): pass

    label('loc_19B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_19CD',
    )

    PlaySE(402, 0x00, 0x64)

    ChrTalk(
        0x00FE,
        (
            '喵～噢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19CD(): pass

    label('loc_19CD')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x19D1
@scena.Code('func_0A_19D1')
def func_0A_19D1():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 3, 0x603)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 4, 0x604)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_26BD',
    )

    SetScenaFlags(ScenaFlag(0x00C0, 4, 0x604))
    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, -20510, 8000, 119230, 0)
    ChrSetPos(0x0102, -18980, 8000, 119430, 0)

    @scena.Lambda('lambda_1A12')
    def lambda_1A12():
        OP_6C(0, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1A12)

    @scena.Lambda('lambda_1A22')
    def lambda_1A22():
        CameraSetDistance(2750, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_1A22)

    CameraMove(-20140, 8000, 120700, 2000)

    ChrTalk(
        0x0009,
        (
            '#1970100284V啊，是你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970100285V就像刚才我说的，\n',
            '飞艇什么时候能来还不知道呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970100286V实在抱歉，\n',
            '你们在游击士协会等一会儿吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100287V#506F嗯～其实……\n',
            '我们稍微改变了一下计划。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100288V#010F非常抱歉。\n',
            '请问搭乘手续能取消吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970100289V这样啊……\n',
            '唉，也是没办法的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970100290V在定期船到来之前，\n',
            '是不需要支付取消手续费的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970100291V把刚才的船票\n',
            '还给我就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100292V#000F嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '把两张',
            (TxtCtl.SetColor, 0x2),
            '船票',
            (TxtCtl.SetColor, 0x0),
            '还了回去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    RemoveItem(0x0370, 2)
    Sleep(500)

    PlaySE(226, 0x00, 0x64)
    OP_20(0x000003E8)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    PlayBGM(86)

    ChrTalk(
        0x0009,
        (
            '#1970100293V哎呀……\n',
            '好像是军用警备飞艇来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970100294V来得还真早啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100295V#004F那、那么我们赶快……！\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 180, 600)

    @scena.Lambda('lambda_1D30')
    def lambda_1D30():
        ChrWalkTo(0x00FE, -20180, 8000, 103080, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1D30)

    ChrTalk(
        0x0102,
        (
            '#0020100296V#010F麻烦您了。\n',
            '真是非常不好意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0102, 180, 600)

    @scena.Lambda('lambda_1D86')
    def lambda_1D86():
        ChrWalkTo(0x00FE, -18440, 8000, 103080, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1D86)

    ChrTalk(
        0x0009,
        (
            '#1970100297V没什么。\n',
            '欢迎两位下次再来乘坐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    OP_6F(0x0000, 1001)
    OP_A1(0x0011, 0x0004)
    OP_72(0x0004, 0x0004)
    OP_72(0x0004, 0x0020)
    ChrSetPos(0x0011, -34000, 17000, 180000, 0)
    ChrSetFlags(0x0011, 0x0004)
    OP_A1(0x0012, 0x0005)
    OP_72(0x0005, 0x0004)
    OP_72(0x000A, 0x0004)
    ChrSetPos(0x0012, -34000, -10000, 180000, 0)
    ChrSetFlags(0x0012, 0x0004)
    OP_6F(0x0003, 100)
    OP_B0(0x0004, 0x1E)
    CameraMove(-34000, 17000, 170000, 0)
    OP_67(0, 26070, -10000, 0)
    CameraSetDistance(3500, 0)
    OP_6C(156000, 0)
    OP_6E(239, 0)
    OP_12(0x000186A0, 0x0003D090, 0x00000000)
    OP_6F(0x0004, 470)
    OP_70(0x0004, 590)

    @scena.Lambda('lambda_1E90')
    def lambda_1E90():
        ChrMoveTo(0x00FE, -34000, 17000, 170000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_1E90)

    @scena.Lambda('lambda_1EAB')
    def lambda_1EAB():
        ChrMoveTo(0x00FE, -34000, -10000, 170000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_1EAB)

    PlaySE(121, 0x01, 0x28)
    Sleep(100)

    OP_24(0x0079, 0x3C)
    Sleep(100)

    OP_24(0x0079, 0x41)
    Sleep(100)

    OP_24(0x0079, 0x46)
    Sleep(100)

    OP_24(0x0079, 0x4B)
    Sleep(100)

    OP_24(0x0079, 0x50)
    Sleep(100)

    OP_24(0x0079, 0x55)
    Sleep(100)

    OP_24(0x0079, 0x5A)
    Sleep(100)

    OP_24(0x0079, 0x5F)
    Sleep(100)

    OP_24(0x0079, 0x64)
    WaitForThreadExit(0x0011, 0x0001)
    OP_66(0x0000)
    OP_6A(0x0011)

    @scena.Lambda('lambda_1F27')
    def lambda_1F27():
        ChrSetDirection(0x00FE, 180, 5)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_1F27)

    @scena.Lambda('lambda_1F35')
    def lambda_1F35():
        ChrSetDirection(0x00FE, 180, 5)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_1F35)

    @scena.Lambda('lambda_1F43')
    def lambda_1F43():
        ChrMoveTo(0x00FE, -34000, 17000, 157000, 7500, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_1F43)

    @scena.Lambda('lambda_1F5E')
    def lambda_1F5E():
        ChrMoveTo(0x00FE, -34000, -10000, 157000, 7500, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_1F5E)

    Sleep(200)

    @scena.Lambda('lambda_1F7E')
    def lambda_1F7E():
        ChrSetDirection(0x00FE, 180, 10)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_1F7E)

    @scena.Lambda('lambda_1F8C')
    def lambda_1F8C():
        ChrSetDirection(0x00FE, 180, 10)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_1F8C)

    @scena.Lambda('lambda_1F9A')
    def lambda_1F9A():
        ChrMoveTo(0x00FE, -34000, 17000, 157000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_1F9A)

    @scena.Lambda('lambda_1FB5')
    def lambda_1FB5():
        ChrMoveTo(0x00FE, -34000, -10000, 157000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_1FB5)

    Sleep(200)

    @scena.Lambda('lambda_1FD5')
    def lambda_1FD5():
        ChrSetDirection(0x00FE, 180, 30)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_1FD5)

    @scena.Lambda('lambda_1FE3')
    def lambda_1FE3():
        ChrSetDirection(0x00FE, 180, 30)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_1FE3)

    @scena.Lambda('lambda_1FF1')
    def lambda_1FF1():
        ChrMoveTo(0x00FE, -34000, 17000, 157000, 6500, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_1FF1)

    @scena.Lambda('lambda_200C')
    def lambda_200C():
        ChrMoveTo(0x00FE, -34000, -10000, 157000, 6500, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_200C)

    Sleep(200)

    @scena.Lambda('lambda_202C')
    def lambda_202C():
        ChrSetDirection(0x00FE, 180, 50)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_202C)

    @scena.Lambda('lambda_203A')
    def lambda_203A():
        ChrSetDirection(0x00FE, 180, 50)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_203A)

    @scena.Lambda('lambda_2048')
    def lambda_2048():
        ChrMoveTo(0x00FE, -34000, 17000, 157000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_2048)

    @scena.Lambda('lambda_2063')
    def lambda_2063():
        ChrMoveTo(0x00FE, -34000, -10000, 157000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_2063)

    Sleep(200)

    @scena.Lambda('lambda_2083')
    def lambda_2083():
        ChrSetDirection(0x00FE, 180, 60)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_2083)

    @scena.Lambda('lambda_2091')
    def lambda_2091():
        ChrSetDirection(0x00FE, 180, 60)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_2091)

    @scena.Lambda('lambda_209F')
    def lambda_209F():
        ChrMoveTo(0x00FE, -34000, 17000, 157000, 5500, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_209F)

    @scena.Lambda('lambda_20BA')
    def lambda_20BA():
        ChrMoveTo(0x00FE, -34000, -10000, 157000, 5500, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_20BA)

    Sleep(200)

    @scena.Lambda('lambda_20DA')
    def lambda_20DA():
        ChrMoveTo(0x00FE, -34000, 17000, 157000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_20DA)

    @scena.Lambda('lambda_20F5')
    def lambda_20F5():
        ChrMoveTo(0x00FE, -34000, -10000, 157000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_20F5)

    Sleep(200)

    @scena.Lambda('lambda_2115')
    def lambda_2115():
        ChrMoveTo(0x00FE, -34000, 17000, 157000, 4500, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_2115)

    @scena.Lambda('lambda_2130')
    def lambda_2130():
        ChrMoveTo(0x00FE, -34000, -10000, 157000, 4500, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_2130)

    Sleep(200)

    @scena.Lambda('lambda_2150')
    def lambda_2150():
        ChrMoveTo(0x00FE, -34000, 17000, 157000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_2150)

    @scena.Lambda('lambda_216B')
    def lambda_216B():
        ChrMoveTo(0x00FE, -34000, -10000, 157000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_216B)

    Sleep(200)

    @scena.Lambda('lambda_218B')
    def lambda_218B():
        ChrMoveTo(0x00FE, -34000, 17000, 157000, 3500, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_218B)

    @scena.Lambda('lambda_21A6')
    def lambda_21A6():
        ChrMoveTo(0x00FE, -34000, -10000, 157000, 3500, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_21A6)

    Sleep(200)

    @scena.Lambda('lambda_21C6')
    def lambda_21C6():
        ChrMoveTo(0x00FE, -34000, 17000, 157000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_21C6)

    @scena.Lambda('lambda_21E1')
    def lambda_21E1():
        ChrMoveTo(0x00FE, -34000, -10000, 157000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_21E1)

    Sleep(200)

    @scena.Lambda('lambda_2201')
    def lambda_2201():
        ChrMoveTo(0x00FE, -34000, 17000, 157000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_2201)

    @scena.Lambda('lambda_221C')
    def lambda_221C():
        ChrMoveTo(0x00FE, -34000, -10000, 157000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_221C)

    Sleep(800)

    @scena.Lambda('lambda_223C')
    def lambda_223C():
        ChrSetDirection(0x00FE, 180, 50)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_223C)

    @scena.Lambda('lambda_224A')
    def lambda_224A():
        ChrSetDirection(0x00FE, 180, 50)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_224A)

    Sleep(100)

    @scena.Lambda('lambda_225D')
    def lambda_225D():
        ChrSetDirection(0x00FE, 180, 40)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_225D)

    @scena.Lambda('lambda_226B')
    def lambda_226B():
        ChrSetDirection(0x00FE, 180, 40)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_226B)

    Sleep(100)

    @scena.Lambda('lambda_227E')
    def lambda_227E():
        ChrSetDirection(0x00FE, 180, 30)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_227E)

    @scena.Lambda('lambda_228C')
    def lambda_228C():
        ChrSetDirection(0x00FE, 180, 30)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_228C)

    Sleep(100)

    @scena.Lambda('lambda_229F')
    def lambda_229F():
        ChrSetDirection(0x00FE, 180, 20)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_229F)

    @scena.Lambda('lambda_22AD')
    def lambda_22AD():
        ChrSetDirection(0x00FE, 180, 20)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_22AD)

    Sleep(100)

    @scena.Lambda('lambda_22C0')
    def lambda_22C0():
        ChrSetDirection(0x00FE, 180, 10)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_22C0)

    @scena.Lambda('lambda_22CE')
    def lambda_22CE():
        ChrSetDirection(0x00FE, 180, 10)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_22CE)

    PlaySE(204, 0x00, 0x64)
    OP_6F(0x0004, 590)
    OP_70(0x0004, 690)
    WaitForThreadExit(0x0011, 0x0001)

    @scena.Lambda('lambda_22F4')
    def lambda_22F4():
        ChrMoveTo(0x00FE, -33620, -11000, 144000, 1300, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_22F4)

    @scena.Lambda('lambda_230F')
    def lambda_230F():
        ChrMoveTo(0x00FE, -33620, -10000, 144000, 666, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_230F)

    Sleep(100)

    @scena.Lambda('lambda_232F')
    def lambda_232F():
        ChrMoveTo(0x00FE, -33620, -11000, 144000, 1560, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_232F)

    @scena.Lambda('lambda_234A')
    def lambda_234A():
        ChrMoveTo(0x00FE, -33620, -10000, 144000, 800, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_234A)

    Sleep(100)

    OP_6A(0x0000)
    MapClearFlags(0x00000001)

    @scena.Lambda('lambda_2372')
    def lambda_2372():
        OP_67(-48240, 40960, 201970, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2372)

    @scena.Lambda('lambda_238A')
    def lambda_238A():
        OP_6E(262, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_238A)

    @scena.Lambda('lambda_239A')
    def lambda_239A():
        CameraMove(-32150, -6000, 142270, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_239A)

    @scena.Lambda('lambda_23B2')
    def lambda_23B2():
        ChrMoveTo(0x00FE, -33620, -11000, 144000, 1950, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_23B2)

    @scena.Lambda('lambda_23CD')
    def lambda_23CD():
        ChrMoveTo(0x00FE, -33620, -10000, 144000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_23CD)

    Sleep(100)

    @scena.Lambda('lambda_23ED')
    def lambda_23ED():
        ChrMoveTo(0x00FE, -33620, -11000, 144000, 2600, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_23ED)

    @scena.Lambda('lambda_2408')
    def lambda_2408():
        ChrMoveTo(0x00FE, -33620, -10000, 144000, 1333, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_2408)

    Sleep(100)

    @scena.Lambda('lambda_2428')
    def lambda_2428():
        ChrMoveTo(0x00FE, -33620, -11000, 144000, 3900, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_2428)

    @scena.Lambda('lambda_2443')
    def lambda_2443():
        ChrMoveTo(0x00FE, -33620, -10000, 144000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_2443)

    Sleep(100)

    @scena.Lambda('lambda_2463')
    def lambda_2463():
        ChrMoveTo(0x00FE, -33620, -11000, 144000, 5200, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_2463)

    @scena.Lambda('lambda_247E')
    def lambda_247E():
        ChrMoveTo(0x00FE, -33620, -10000, 144000, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_247E)

    Sleep(100)

    WaitForThreadExit(0x0011, 0x0001)
    OP_23(0x0079)
    PlaySE(200, 0x00, 0x64)
    OP_7C(0, 200, 3000, 100)
    Sleep(600)

    PlaySE(109, 0x00, 0x64)
    OP_6F(0x0004, 1)
    OP_70(0x0004, 15)
    Sleep(300)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_66(0x0001)
    TerminateThread(0x0101, 0xFF)
    CameraMove(-44580, -3800, 144110, 0)
    OP_67(0, 7580, -10000, 0)
    CameraSetDistance(3330, 0)
    OP_6C(134000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0011, -33620, -11600, 144000, 180)
    ChrSetPos(0x0012, -33620, -10000, 144000, 180)

    ExecExpressionWithValue(
        0x0015,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0014,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0013,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    CreateThread(0x0015, 0x01, 0x00, func_17_8190)
    CreateThread(0x0014, 0x01, 0x00, func_16_816D)
    CreateThread(0x0013, 0x01, 0x00, func_15_814A)
    CreateThread(0x000D, 0x01, 0x00, func_14_8127)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_25B3')
    def lambda_25B3():
        CameraMove(-34960, -3480, 144150, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_25B3)

    @scena.Lambda('lambda_25CB')
    def lambda_25CB():
        CameraSetDistance(3330, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_25CB)

    OP_6F(0x0003, 100)
    OP_70(0x0003, 196)
    Sleep(500)

    PlaySE(120, 0x00, 0x64)
    Sleep(3000)

    Sleep(1000)

    ChrTalk(
        0x000D,
        (
            '#0610100298V#180F哼哼……\n',
            '这段时间还真是忙啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610100299V第一件事……\n',
            '就是去拜会一下玛多克工房长。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610100300V#188F不过，不愧是上校……\n',
            '连这样的方法也能想得出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T3101._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_3EBB')

    def _loc_26BD(): pass

    label('loc_26BD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 2, 0x602)),
            Expr.Return,
        ),
        'loc_2723',
    )

    ChrTalk(
        0x0009,
        (
            '再等一会儿\n',
            '『赛希莉亚号』就会来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '定期船到了之后，\n',
            '把这个出示给乘务员就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3EBB')

    def _loc_2723(): pass

    label('loc_2723')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 2, 0x602)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_292D',
    )

    SetScenaFlags(ScenaFlag(0x00C0, 2, 0x602))
    OP_28(0x0054, 0x01, 0x0002)
    EventBegin(0x00)
    OP_69(0x0009, 1000)

    ChrTalk(
        0x0009,
        (
            '#1970100192V啊，你们好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970100193V我已经从雾香那里听说了。\n',
            '现在就办理搭乘手续吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100194V#006F嗯，麻烦您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970100195V那么，请你们在这张单子上\n',
            '填写姓名和联络方式吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100196V#010F好的。',
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
            '艾丝蒂尔和约修亚办理了搭乘手续。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0009,
        (
            '#1970100197V好了，\n',
            '这就是你们的船票。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970100198V定期船到了之后，\n',
            '向乘务员出示船票就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到两张',
            (TxtCtl.SetColor, 0x2),
            '船票',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    AddItem(0x0370, 2)
    EventEnd(0x01)

    Jump('loc_3EBB')

    def _loc_292D(): pass

    label('loc_292D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 6, 0x516)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 7, 0x517)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_38E4',
    )

    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x00A2, 7, 0x517))
    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, -19410, 8000, 119800, 0)
    ChrSetPos(0x0102, -20670, 8000, 119780, 0)

    @scena.Lambda('lambda_296D')
    def lambda_296D():
        OP_6C(315000, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_296D)

    @scena.Lambda('lambda_297D')
    def lambda_297D():
        CameraSetDistance(3000, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_297D)

    OP_69(0x0009, 2000)

    ChrTalk(
        0x0009,
        (
            '#1970071359V#2P哟！客人是来乘坐定期船的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970071360V#2P很不巧，\n',
            '上一班定期船刚刚开走……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071361V#006F唔，不是呢。\n',
            '我们不是来坐定期船的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010071362V我们是有事来找\n',
            '那位叫格斯塔夫的维修长的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970071363V#2P怎么，要找大叔啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970071364V#2P不过很遗憾，\n',
            '大叔他现在不在这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071365V#004F哎，出去了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970071366V#2P嗯，没错。\n',
            '这两三天他去了雷斯顿要塞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970071367V#2P好像是突然接到了\n',
            '那边军用飞艇的维修委托。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071368V#505F说到雷斯顿要塞……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071369V#010F是位于瓦雷利亚湖畔的\n',
            '王国军最大的军事基地。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020071370V就在蔡斯地区的北面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071371V#007F唔～这样的话，\n',
            '看来维修长可没有那么快回来啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010071372V那博士要的东西该怎么办啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970071373V#2P虽然不知道你们有什么事，\n',
            '不过我想他差不多也该回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970071374V#2P刚刚有连络通信过来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(226, 0x00, 0x64)
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010071375V#004F咦……\n',
            '下一班定期船已经来了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0009, 0, 400)

    ChrTalk(
        0x0009,
        (
            '#1970071376V啊，就是这个传说中的飞艇。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A1(0x0011, 0x0004)
    OP_72(0x0004, 0x0004)
    OP_72(0x0004, 0x0020)
    ChrSetPos(0x0011, -34000, 9000, 177000, 180)
    ChrSetFlags(0x0011, 0x0004)
    OP_A1(0x0012, 0x0005)
    OP_72(0x0005, 0x0004)
    OP_72(0x000A, 0x0004)
    ChrSetPos(0x0012, -34000, -11150, 177000, 180)
    ChrSetFlags(0x0012, 0x0004)
    OP_66(0x0000)

    @scena.Lambda('lambda_2DC7')
    def lambda_2DC7():
        OP_67(2310, 43070, 99410, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2DC7)

    @scena.Lambda('lambda_2DDF')
    def lambda_2DDF():
        CameraMove(-32150, 15520, 142270, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2DDF)

    @scena.Lambda('lambda_2DF7')
    def lambda_2DF7():
        CameraSetDistance(900, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2DF7)

    Sleep(2000)

    OP_71(0x0004, 0x0020)
    OP_6F(0x0004, 161)
    OP_70(0x0004, 260)

    @scena.Lambda('lambda_2E1F')
    def lambda_2E1F():
        ChrMoveTo(0x00FE, -34000, 9000, 157000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_2E1F)

    @scena.Lambda('lambda_2E3A')
    def lambda_2E3A():
        ChrMoveTo(0x00FE, -34000, -11150, 157000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_2E3A)

    PlaySE(121, 0x01, 0x28)
    Sleep(100)

    OP_24(0x0079, 0x3C)
    Sleep(100)

    OP_24(0x0079, 0x41)
    Sleep(100)

    OP_24(0x0079, 0x46)
    Sleep(100)

    OP_24(0x0079, 0x4B)
    Sleep(100)

    OP_24(0x0079, 0x50)
    Sleep(100)

    OP_24(0x0079, 0x55)
    Sleep(100)

    OP_24(0x0079, 0x5A)
    Sleep(100)

    OP_24(0x0079, 0x5F)
    Sleep(100)

    OP_24(0x0079, 0x64)
    Sleep(100)

    Sleep(2000)

    Sleep(100)

    @scena.Lambda('lambda_2EBA')
    def lambda_2EBA():
        OP_67(2310, 60560, 99410, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2EBA)

    @scena.Lambda('lambda_2ED2')
    def lambda_2ED2():
        ChrSetDirection(0x00FE, 0, 5)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_2ED2)

    @scena.Lambda('lambda_2EE0')
    def lambda_2EE0():
        ChrSetDirection(0x00FE, 0, 5)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_2EE0)

    Sleep(100)

    @scena.Lambda('lambda_2EF3')
    def lambda_2EF3():
        ChrSetDirection(0x00FE, 0, 8)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_2EF3)

    @scena.Lambda('lambda_2F01')
    def lambda_2F01():
        ChrSetDirection(0x00FE, 0, 8)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_2F01)

    Sleep(100)

    @scena.Lambda('lambda_2F14')
    def lambda_2F14():
        ChrSetDirection(0x00FE, 0, 10)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_2F14)

    @scena.Lambda('lambda_2F22')
    def lambda_2F22():
        ChrSetDirection(0x00FE, 0, 10)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_2F22)

    Sleep(100)

    @scena.Lambda('lambda_2F35')
    def lambda_2F35():
        ChrSetDirection(0x00FE, 0, 13)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_2F35)

    @scena.Lambda('lambda_2F43')
    def lambda_2F43():
        ChrSetDirection(0x00FE, 0, 13)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_2F43)

    Sleep(100)

    @scena.Lambda('lambda_2F56')
    def lambda_2F56():
        ChrSetDirection(0x00FE, 0, 15)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_2F56)

    @scena.Lambda('lambda_2F64')
    def lambda_2F64():
        ChrSetDirection(0x00FE, 0, 15)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_2F64)

    Sleep(100)

    @scena.Lambda('lambda_2F77')
    def lambda_2F77():
        ChrSetDirection(0x00FE, 0, 18)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_2F77)

    @scena.Lambda('lambda_2F85')
    def lambda_2F85():
        ChrSetDirection(0x00FE, 0, 18)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_2F85)

    @scena.Lambda('lambda_2F93')
    def lambda_2F93():
        ChrMoveTo(0x00FE, -34000, 9000, 157000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_2F93)

    Sleep(85)

    @scena.Lambda('lambda_2FB3')
    def lambda_2FB3():
        ChrSetDirection(0x00FE, 0, 20)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_2FB3)

    @scena.Lambda('lambda_2FC1')
    def lambda_2FC1():
        ChrSetDirection(0x00FE, 0, 20)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_2FC1)

    Sleep(85)

    @scena.Lambda('lambda_2FD4')
    def lambda_2FD4():
        ChrSetDirection(0x00FE, 0, 23)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_2FD4)

    @scena.Lambda('lambda_2FE2')
    def lambda_2FE2():
        ChrSetDirection(0x00FE, 0, 23)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_2FE2)

    @scena.Lambda('lambda_2FF0')
    def lambda_2FF0():
        ChrMoveTo(0x00FE, -34000, 9000, 157000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_2FF0)

    Sleep(85)

    @scena.Lambda('lambda_3010')
    def lambda_3010():
        ChrSetDirection(0x00FE, 0, 25)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_3010)

    @scena.Lambda('lambda_301E')
    def lambda_301E():
        ChrSetDirection(0x00FE, 0, 25)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_301E)

    Sleep(85)

    @scena.Lambda('lambda_3031')
    def lambda_3031():
        ChrMoveTo(0x00FE, -34000, 9000, 157000, 4500, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_3031)

    @scena.Lambda('lambda_304C')
    def lambda_304C():
        ChrSetDirection(0x00FE, 0, 28)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_304C)

    @scena.Lambda('lambda_305A')
    def lambda_305A():
        ChrSetDirection(0x00FE, 0, 28)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_305A)

    Sleep(85)

    @scena.Lambda('lambda_306D')
    def lambda_306D():
        ChrSetDirection(0x00FE, 0, 30)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_306D)

    @scena.Lambda('lambda_307B')
    def lambda_307B():
        ChrSetDirection(0x00FE, 0, 30)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_307B)

    Sleep(85)

    @scena.Lambda('lambda_308E')
    def lambda_308E():
        ChrSetDirection(0x00FE, 0, 33)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_308E)

    @scena.Lambda('lambda_309C')
    def lambda_309C():
        ChrSetDirection(0x00FE, 0, 33)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_309C)

    @scena.Lambda('lambda_30AA')
    def lambda_30AA():
        ChrMoveTo(0x00FE, -34000, 9000, 157000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_30AA)

    Sleep(85)

    Sleep(85)

    @scena.Lambda('lambda_30CF')
    def lambda_30CF():
        ChrMoveTo(0x00FE, -34000, 9000, 157000, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_30CF)

    Sleep(170)

    @scena.Lambda('lambda_30EF')
    def lambda_30EF():
        ChrMoveTo(0x00FE, -34000, 9000, 157000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_30EF)

    Sleep(170)

    @scena.Lambda('lambda_310F')
    def lambda_310F():
        ChrMoveTo(0x00FE, -34000, 9000, 157000, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_310F)

    Sleep(170)

    @scena.Lambda('lambda_312F')
    def lambda_312F():
        ChrMoveTo(0x00FE, -34000, 9000, 157000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_312F)

    Sleep(170)

    @scena.Lambda('lambda_314F')
    def lambda_314F():
        ChrMoveTo(0x00FE, -34000, 9000, 157000, 500, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_314F)

    Sleep(170)

    WaitForThreadExit(0x0011, 0x0001)
    Sleep(1900)

    Sleep(200)

    @scena.Lambda('lambda_317E')
    def lambda_317E():
        ChrSetDirection(0x00FE, 0, 25)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_317E)

    @scena.Lambda('lambda_318C')
    def lambda_318C():
        ChrSetDirection(0x00FE, 0, 25)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_318C)

    Sleep(200)

    @scena.Lambda('lambda_319F')
    def lambda_319F():
        ChrSetDirection(0x00FE, 0, 20)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_319F)

    @scena.Lambda('lambda_31AD')
    def lambda_31AD():
        ChrSetDirection(0x00FE, 0, 20)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_31AD)

    Sleep(200)

    @scena.Lambda('lambda_31C0')
    def lambda_31C0():
        ChrSetDirection(0x00FE, 0, 15)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_31C0)

    @scena.Lambda('lambda_31CE')
    def lambda_31CE():
        ChrSetDirection(0x00FE, 0, 15)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_31CE)

    Sleep(200)

    @scena.Lambda('lambda_31E1')
    def lambda_31E1():
        ChrSetDirection(0x00FE, 0, 10)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_31E1)

    @scena.Lambda('lambda_31EF')
    def lambda_31EF():
        ChrSetDirection(0x00FE, 0, 10)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_31EF)

    Sleep(200)

    @scena.Lambda('lambda_3202')
    def lambda_3202():
        ChrSetDirection(0x00FE, 0, 7)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_3202)

    @scena.Lambda('lambda_3210')
    def lambda_3210():
        ChrSetDirection(0x00FE, 0, 7)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_3210)

    WaitForThreadExit(0x0011, 0x0002)
    OP_72(0x0004, 0x0020)
    OP_6F(0x0004, 261)
    OP_70(0x0004, 410)

    @scena.Lambda('lambda_3236')
    def lambda_3236():
        ChrMoveTo(0x00FE, -34000, -11150, 148000, 500, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_3236)

    @scena.Lambda('lambda_3251')
    def lambda_3251():
        ChrMoveTo(0x00FE, -34000, -11150, 148000, 100, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_3251)

    Sleep(100)

    @scena.Lambda('lambda_3271')
    def lambda_3271():
        ChrMoveTo(0x00FE, -34000, -11150, 148000, 200, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_3271)

    Sleep(100)

    @scena.Lambda('lambda_3291')
    def lambda_3291():
        ChrMoveTo(0x00FE, -34000, -11150, 148000, 300, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_3291)

    Sleep(100)

    @scena.Lambda('lambda_32B1')
    def lambda_32B1():
        ChrMoveTo(0x00FE, -34000, -11150, 148000, 500, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_32B1)

    @scena.Lambda('lambda_32CC')
    def lambda_32CC():
        CameraMove(-32150, 3000, 135270, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_32CC)

    Sleep(100)

    @scena.Lambda('lambda_32E9')
    def lambda_32E9():
        ChrMoveTo(0x00FE, -34000, -11150, 148000, 700, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_32E9)

    Sleep(100)

    @scena.Lambda('lambda_3309')
    def lambda_3309():
        ChrMoveTo(0x00FE, -34000, -11150, 148000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_3309)

    Sleep(100)

    @scena.Lambda('lambda_3329')
    def lambda_3329():
        ChrMoveTo(0x00FE, -34000, -11150, 148000, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_3329)

    Sleep(100)

    @scena.Lambda('lambda_3349')
    def lambda_3349():
        ChrMoveTo(0x00FE, -34000, -11150, 148000, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_3349)

    Sleep(100)

    @scena.Lambda('lambda_3369')
    def lambda_3369():
        ChrMoveTo(0x00FE, -34000, -11150, 148000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_3369)

    Sleep(100)

    @scena.Lambda('lambda_3389')
    def lambda_3389():
        ChrMoveTo(0x00FE, -34000, -11150, 148000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_3389)

    Sleep(100)

    @scena.Lambda('lambda_33A9')
    def lambda_33A9():
        ChrMoveTo(0x00FE, -34000, -11150, 148000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_33A9)

    Sleep(100)

    @scena.Lambda('lambda_33C9')
    def lambda_33C9():
        ChrMoveTo(0x00FE, -34000, -11150, 148000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_33C9)

    Sleep(4500)

    Sleep(100)

    @scena.Lambda('lambda_33EE')
    def lambda_33EE():
        ChrMoveTo(0x00FE, -34000, -11150, 148000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_33EE)

    Sleep(100)

    @scena.Lambda('lambda_340E')
    def lambda_340E():
        ChrMoveTo(0x00FE, -34000, -11150, 148000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_340E)

    Sleep(100)

    @scena.Lambda('lambda_342E')
    def lambda_342E():
        ChrMoveTo(0x00FE, -34000, -11150, 148000, 2200, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_342E)

    Sleep(100)

    @scena.Lambda('lambda_344E')
    def lambda_344E():
        ChrMoveTo(0x00FE, -34000, -11150, 148000, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_344E)

    Sleep(100)

    @scena.Lambda('lambda_346E')
    def lambda_346E():
        ChrMoveTo(0x00FE, -34000, -11150, 148000, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_346E)

    Sleep(100)

    @scena.Lambda('lambda_348E')
    def lambda_348E():
        ChrMoveTo(0x00FE, -34000, -11150, 148000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_348E)

    Sleep(100)

    @scena.Lambda('lambda_34AE')
    def lambda_34AE():
        ChrMoveTo(0x00FE, -34000, -11150, 148000, 700, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_34AE)

    Sleep(100)

    @scena.Lambda('lambda_34CE')
    def lambda_34CE():
        ChrMoveTo(0x00FE, -34000, -11150, 148000, 600, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_34CE)

    Sleep(100)

    @scena.Lambda('lambda_34EE')
    def lambda_34EE():
        ChrMoveTo(0x00FE, -34000, -11150, 148000, 500, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_34EE)

    Sleep(100)

    @scena.Lambda('lambda_350E')
    def lambda_350E():
        ChrMoveTo(0x00FE, -34000, -11150, 148000, 400, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_350E)

    TerminateThread(0x0011, 0x01)
    OP_23(0x0079)
    PlaySE(200, 0x00, 0x64)
    OP_7C(0, 100, 3000, 100)
    ChrSetPos(0x0011, -34000, -11150, 148000, 0)
    Sleep(1000)

    PlaySE(118, 0x00, 0x46)
    OP_72(0x0004, 0x0020)
    OP_6F(0x0004, 60)
    OP_70(0x0004, 1)
    Sleep(1100)

    OP_6F(0x0003, 100)
    OP_70(0x0003, 200)
    Sleep(2500)

    TerminateThread(0x0101, 0x01)
    Fade(1000)
    TerminateThread(0x0008, 0xFF)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetPos(0x0008, -36900, -3800, 140550, 90)
    OP_66(0x0001)
    ChrSetPos(0x0101, -24600, 8000, 121410, 0)
    ChrSetPos(0x0102, -23560, 8000, 121480, 0)
    ChrTurnDirection(0x0009, 0x0101, 0)
    TerminateThread(0x0101, 0xFF)
    CameraMove(-23460, 8000, 121550, 0)
    OP_67(0, 9450, -10000, 0)
    CameraSetDistance(2880, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_71(0x0006, 0x0004)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010071377V#004F橙色的定期船……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010071378V咦咦。\n',
            '有那样的定期船吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071379V#010F不……\n',
            '好像不是定期船。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020071380V很多地方的形状都和定期船不同，\n',
            '而且还带有作业用的扶手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071381V#505F啊，的确……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970071382V#2P这是中央工房所属的工房船\n',
            '『莱普尼兹号』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970071383V#2P虽然和定期船是相同型号，\n',
            '但追加了各种设备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970071384V#2P主要是用于\n',
            '大型设备的维护和制品的搬运。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071385V#001F嘿嘿～！\n',
            '是在天上飞的工房啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010071386V#006F工房船回来了，\n',
            '那么维修长应该在飞艇里面吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970071387V#2P是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970071388V#2P你们不是有事吗？\n',
            '快点去找他吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0009, 400)

    ChrTalk(
        0x0101,
        (
            '#0010071389V#006F嗯，好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0009, 400)

    ChrTalk(
        0x0102,
        (
            '#0020071390V#010F那么我们先告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)
    CreateThread(0x0008, 0x00, 0x00, func_02_872)

    Jump('loc_3EBB')

    def _loc_38E4(): pass

    label('loc_38E4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_395A',
    )

    ChrTalk(
        0x0009,
        (
            '#1970100201V嗯？怎么了？\n',
            '手续已经办好了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970100202V定期船到了之后，\n',
            '凭刚才的票就可以乘坐了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3EBB')

    def _loc_395A(): pass

    label('loc_395A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_39BA',
    )

    ChrTalk(
        0x0009,
        (
            '哟，你们也很忙呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '好像工房船\n',
            '有很紧急的任务要执行。\n',
            '这边也已经乱成一团了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3EBB')

    def _loc_39BA(): pass

    label('loc_39BA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_3A2E',
    )

    ChrTalk(
        0x0009,
        (
            '『赛希莉亚号』\n',
            '已经按预定的时间出航了………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '唔，就趁现在难得的空闲\n',
            '集中精神看《利贝尔通讯》吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3EBB')

    def _loc_3A2E(): pass

    label('loc_3A2E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_3B79',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_3AD5',
    )

    ChrTalk(
        0x0009,
        (
            '嗯嗯，对了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '说到封面……\n',
            '最近《利贝尔通讯》上面的照片\n',
            '都变得好漂亮啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '嗯，一想到这个，\n',
            '就很期待下期的封面啊。\n',
            '……偷偷告诉你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3B76')

    def _loc_3AD5(): pass

    label('loc_3AD5')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0009,
        (
            '中央工房的骚动\n',
            '好像是起严重的事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '竟然敢袭击中央工房，\n',
            '世上还有这样无法无天的家伙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '唉，这样一来\n',
            '下期《利贝尔通讯》的封面\n',
            '就会是蔡斯了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3B76(): pass

    label('loc_3B76')

    Jump('loc_3EBB')

    def _loc_3B79(): pass

    label('loc_3B79')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_3C3E',
    )

    ChrTalk(
        0x0009,
        (
            '那个，你们看过\n',
            '《利贝尔通讯》最新一期了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '听说卢安的市长\n',
            '是个无法无天的坏家伙，\n',
            '已经被逮捕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '不过，空贼事件也好，\n',
            '这个叫戴尔蒙的家伙也好……\n',
            '最近这个世界真是不太平啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3EBB')

    def _loc_3C3E(): pass

    label('loc_3C3E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_3D17',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 6, 0x516)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3CAA',
    )

    ChrTalk(
        0x0009,
        (
            '现在西向航线的定期船\n',
            '正按预定时间出发。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '希望定期船今天也能够\n',
            '太平顺畅地运行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3D14')

    def _loc_3CAA(): pass

    label('loc_3CAA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 7, 0x517)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 0, 0x518)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3CFA',
    )

    ChrTalk(
        0x0009,
        (
            '我们老大应该就在\n',
            '『莱普尼兹号』里面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '赶快去问问他吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3D14')

    def _loc_3CFA(): pass

    label('loc_3CFA')

    ChrTalk(
        0x0009,
        (
            '你们见到维修长了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3D14(): pass

    label('loc_3D14')

    Jump('loc_3EBB')

    def _loc_3D17(): pass

    label('loc_3D17')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_3E48',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_3D9A',
    )

    ChrTalk(
        0x0009,
        (
            '听说，最后好像是游击士\n',
            '解决了这次空贼事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '真是的，明明发生了这么严重的事情，\n',
            '王国军却什么事也做不了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E45')

    def _loc_3D9A(): pass

    label('loc_3D9A')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0009,
        (
            '我读过利贝尔通讯了，\n',
            '前段时间柏斯的空贼骚动\n',
            '好像闹得很大啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '定期船停航了，\n',
            '对我们接待员来说可真是噩梦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '要把事情向客人解释清楚，\n',
            '可是一件很难的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3E45(): pass

    label('loc_3E45')

    Jump('loc_3EBB')

    def _loc_3E48(): pass

    label('loc_3E48')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_3EBB',
    )

    ChrTalk(
        0x0009,
        (
            '目前，西向航线的『赛希莉亚号』\n',
            '正停靠在飞艇坪中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '去往格兰赛尔的旅客，\n',
            '请前往入口处准备登船。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3EBB(): pass

    label('loc_3EBB')

    TalkEnd(0x0009)

    Return()

# id: 0x000B offset: 0x3EBF
@scena.Code('func_0B_3EBF')
def func_0B_3EBF():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AE, 2, 0x572)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AC, 1, 0x561)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3F64',
    )

    TalkBegin(0x000A)

    ChrTalk(
        0x000A,
        (
            '#0550090603V#800F今天乘务员们都很忙，\n',
            '一会儿在飞船里是不能\n',
            '对导力器进行修理维护的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550090604V你们最好趁现在到街上\n',
            '把自己的装备整理好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000A)

    Jump('loc_4F3D')

    def _loc_3F64(): pass

    label('loc_3F64')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AC, 0, 0x560)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AC, 1, 0x561)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4DB0',
    )

    EventBegin(0x00)
    Fade(1000)
    OP_4A(0x000A, 255)
    OP_4A(0x0008, 255)
    ChrSetPos(0x0101, -46160, -4000, 141480, 90)
    ChrSetPos(0x0106, -44780, -4000, 140260, 0)
    ChrSetPos(0x0107, -45700, -4000, 140390, 45)
    ChrSetPos(0x0102, -45780, -4000, 142250, 135)
    ChrTurnDirection(0x000A, 0x0107, 0)

    @scena.Lambda('lambda_3FD0')
    def lambda_3FD0():
        OP_6C(45000, 0)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3FD0)

    CameraMove(-45150, -4000, 141460, 0)
    CameraSetDistance(3000, 0)
    OP_0D()

    ChrTalk(
        0x000A,
        (
            '#0550090555V#800F哦哦，正等着你们呢。\n',
            '大家都准备好了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050090556V#051F啊啊，随时都能出发。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090557V#560F『莱普尼兹号』的准备也完成了吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0550090558V#801F啊，我们这次运气真好，\n',
            '刚好要塞那边急着要我们发货。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550090559V正好准备前往雷斯顿要塞。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550090560V随时都可以出发哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 135, 400)
    Sleep(200)

    ChrSetDirection(0x0101, 0, 400)
    Sleep(200)

    ChrTurnDirection(0x0101, 0x000A, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010090561V#505F随时……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090562V可是没看到那艘橙色的飞艇啊……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0102, 315, 400)
    Sleep(500)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrWalkTo(0x0102, -47490, -4000, 143600, 2000, 0x00)

    ChrTalk(
        0x0102,
        (
            '#0020090563V#010F艾丝蒂尔，看下面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    @scena.Lambda('lambda_420F')
    def lambda_420F():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_420F')

    DispatchAsync2(0x000A, 0x0002, lambda_420F)

    @scena.Lambda('lambda_4220')
    def lambda_4220():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_4220')

    DispatchAsync2(0x0107, 0x0002, lambda_4220)

    @scena.Lambda('lambda_4231')
    def lambda_4231():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_4231')

    DispatchAsync2(0x0106, 0x0002, lambda_4231)

    @scena.Lambda('lambda_4242')
    def lambda_4242():
        CameraMove(-48810, -4000, 144860, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_4242)

    @scena.Lambda('lambda_425A')
    def lambda_425A():
        OP_6C(314000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_425A)

    @scena.Lambda('lambda_426A')
    def lambda_426A():
        CameraSetDistance(3500, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_426A)

    Sleep(3000)

    @scena.Lambda('lambda_427F')
    def lambda_427F():
        ChrWalkTo(0x0101, -47480, -4000, 142560, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_427F)

    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010090564V#501F#1P啊，在那里啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090565V那我们也要到下面去吧？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090566V#061F#1P呵呵，姐姐。\n',
            '我们不用下去啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0107, 400)

    ChrTalk(
        0x0101,
        (
            '#0010090567V#004F#1P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(167, 0x01, 0x55)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetDirection(0x0101, 315, 400)

    ChrTalk(
        0x0101,
        (
            '#0010090568V#004F#1P什、什么……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090569V#014F#2P飞艇的轨道……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050090570V#051F#2P怎么，你们连这都不知道吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090571V这个城镇的飞艇坪是\n',
            '用超乎常识的方法来建造的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090572V#509F#1P超、超乎常识？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_24(0x00A7, 0x64)
    OP_B0(0x0000, 0x0F)
    OP_6F(0x0000, 250)
    OP_70(0x0000, 600)

    @scena.Lambda('lambda_4477')
    def lambda_4477():
        OP_6C(339000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4477)

    CameraMove(-55390, -4000, 147110, 3000)
    OP_12(0x0000C350, 0x0003D090, 0x00000FA0)
    Sleep(100)

    PlaySE(154, 0x00, 0x64)

    @scena.Lambda('lambda_44AF')
    def lambda_44AF():
        CameraSetDistance(2200, 3500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_44AF)

    OP_67(0, 21600, -10000, 3500)
    PlaySE(154, 0x00, 0x64)
    OP_7C(0, 400, 3000, 100)
    Sleep(500)

    @scena.Lambda('lambda_44EB')
    def lambda_44EB():
        CameraSetDistance(3500, 6200)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_44EB)

    @scena.Lambda('lambda_44FB')
    def lambda_44FB():
        OP_6C(27000, 6100)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_44FB)

    CameraMove(-36640, -4000, 148800, 6100)
    PlaySE(154, 0x00, 0x64)
    OP_7C(0, 400, 3000, 100)
    Sleep(100)

    @scena.Lambda('lambda_4537')
    def lambda_4537():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_4537')

    DispatchAsync2(0x0102, 0x0000, lambda_4537)

    @scena.Lambda('lambda_4548')
    def lambda_4548():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_4548')

    DispatchAsync2(0x0101, 0x0000, lambda_4548)

    @scena.Lambda('lambda_4559')
    def lambda_4559():
        ChrWalkTo(0x00FE, -46240, -4000, 141000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_4559)

    @scena.Lambda('lambda_4574')
    def lambda_4574():
        ChrWalkTo(0x00FE, -46280, -4000, 142120, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_4574)

    @scena.Lambda('lambda_458F')
    def lambda_458F():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_458F)

    @scena.Lambda('lambda_459D')
    def lambda_459D():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0002, lambda_459D)

    @scena.Lambda('lambda_45AB')
    def lambda_45AB():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0106, 0x0002, lambda_45AB)

    @scena.Lambda('lambda_45B9')
    def lambda_45B9():
        CameraSetDistance(5500, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_45B9)

    @scena.Lambda('lambda_45C9')
    def lambda_45C9():
        OP_67(0, 4000, -10000, 11800)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_45C9)

    OP_6C(90000, 9800)
    OP_73(0x0000)
    TerminateThread(0x0101, 0x01)
    OP_23(0x00A7)
    PlaySE(154, 0x00, 0x64)
    OP_7C(0, 200, 3000, 100)
    Sleep(1000)

    Fade(1000)
    OP_25(0x0075, -34230, -4000, 144000, 10000, 40000, 0x64, 0x00000000)
    OP_71(0x0006, 0x0004)
    OP_A1(0x0011, 0x0004)
    OP_72(0x0004, 0x0004)
    OP_6F(0x0004, 60)
    ChrSetPos(0x0011, -34000, -11150, 148000, 0)
    ChrSetFlags(0x0011, 0x0004)
    CameraSetDistance(3500, 0)
    OP_67(0, 11000, -10000, 0)
    OP_12(0x0000C350, 0x0001FBD0, 0x00000000)
    CameraMove(-45210, -4000, 142090, 0)
    OP_6F(0x0000, 1001)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010090573V#509F怎么说呢……\n',
            '我还以为已经对这种玩意习惯了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090574V#019F哈哈，就是啊。\n',
            '没想到还有这么厉害的设施啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0550090575V#803F顺带说一下，\n',
            '这个飞艇坪的构建理念也是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090576V#007F知道啦。\n',
            '又是拉赛尔博士的杰作对吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090577V#008F提妲啊，\n',
            '你的爷爷还真是无所不能呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090578V#067F#2P嘿嘿……\n',
            '我也有同感呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0008, 0x0004)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, -36460, -4000, 144380, 270)
    PlaySE(118, 0x00, 0x64)
    OP_6F(0x0004, 60)
    OP_70(0x0004, 1)
    Sleep(1100)

    PlaySE(120, 0x00, 0x64)
    OP_6F(0x0003, 100)
    OP_70(0x0003, 200)
    OP_73(0x0003)

    ChrTalk(
        0x0008,
        (
            '#0560090579V#6P哟，久等了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CameraMove(-40270, -4000, 143040, 1000)

    ChrTalk(
        0x0107,
        (
            '#0070090580V#560F啊，维修长叔叔！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_48B2')
    def lambda_48B2():
        ChrWalkTo(0x00FE, -43100, -3800, 144030, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_48B2)

    @scena.Lambda('lambda_48CD')
    def lambda_48CD():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_48CD')

    DispatchAsync2(0x000A, 0x0002, lambda_48CD)

    @scena.Lambda('lambda_48DE')
    def lambda_48DE():
        CameraMove(-44110, -3800, 143890, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_48DE)

    Sleep(100)

    @scena.Lambda('lambda_48FB')
    def lambda_48FB():
        ChrWalkTo(0x00FE, -46070, -4000, 145500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_48FB)

    Sleep(100)

    @scena.Lambda('lambda_491B')
    def lambda_491B():
        ChrWalkTo(0x00FE, -46450, -4000, 144410, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_491B)

    Sleep(100)

    @scena.Lambda('lambda_493B')
    def lambda_493B():
        ChrWalkTo(0x00FE, -46340, -4000, 143490, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0003, lambda_493B)

    Sleep(100)

    @scena.Lambda('lambda_495B')
    def lambda_495B():
        ChrWalkTo(0x00FE, -46250, -4000, 142590, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0003, lambda_495B)

    WaitForThreadExit(0x0102, 0x0003)

    @scena.Lambda('lambda_497B')
    def lambda_497B():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_497B')

    DispatchAsync2(0x0102, 0x0002, lambda_497B)

    WaitForThreadExit(0x0101, 0x0003)

    @scena.Lambda('lambda_4991')
    def lambda_4991():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_4991')

    DispatchAsync2(0x0101, 0x0002, lambda_4991)

    WaitForThreadExit(0x0107, 0x0003)

    @scena.Lambda('lambda_49A7')
    def lambda_49A7():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_49A7')

    DispatchAsync2(0x0107, 0x0002, lambda_49A7)

    WaitForThreadExit(0x0106, 0x0003)

    @scena.Lambda('lambda_49BD')
    def lambda_49BD():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_49BD')

    DispatchAsync2(0x0106, 0x0002, lambda_49BD)

    WaitForThreadExit(0x0008, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#0560090581V#690F提妲啊，\n',
            '详细情况我已经听工房长说了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560090582V没想到老爷子会遇到那样的事。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560090583V#691F能帮上忙的话，\n',
            '我们全体维修员随时乐意效劳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090584V#061F谢、谢谢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050090585V#051F抱歉，麻烦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0560090586V#691F不要客气。\n',
            '因为老爷子也是我的恩人啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560090587V好了。\n',
            '这边准备ＯＫ了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560090588V这就出发去雷斯顿要塞吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0107, 0xFF)
    TerminateThread(0x0106, 0xFF)
    TerminateThread(0x000A, 0xFF)
    ChrSetDirection(0x000A, 315, 400)
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
            TXT(0x00, '【出发】\n'),
            TXT(0x01, '【整理装备】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_4BC7'),
        (0x00000001, 'loc_4D66'),
        (-1, 'loc_4DAD'),
    )

    def _loc_4BC7(): pass

    label('loc_4BC7')

    SetScenaFlags(ScenaFlag(0x00AC, 1, 0x561))
    OP_28(0x0043, 0x01, 0x0400)
    OP_28(0x0044, 0x04, 0x02)
    OP_28(0x0044, 0x04, 0x04)

    ChrTalk(
        0x0008,
        (
            '#0560090589V#693F好！\n',
            '那么快上去吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560090590V工房船『莱普尼兹号』，\n',
            '向目的地雷斯顿要塞进发！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0550090591V#803F#2P各位游击士……\n',
            '博士的事就拜托你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550090592V#800F还有的是……\n',
            '麻烦你们好好保护提妲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4CBC')
    def lambda_4CBC():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4CBC)

    @scena.Lambda('lambda_4CCA')
    def lambda_4CCA():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_4CCA)

    @scena.Lambda('lambda_4CD8')
    def lambda_4CD8():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_4CD8)

    ChrTurnDirection(0x0107, 0x000A, 400)

    ChrTalk(
        0x0107,
        (
            '#0070090593V#560F工房长……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090594V#006F嗯，都包在我们身上吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090595V#010F那么我们走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Call(0, 0x0011)

    Jump('loc_4DAD')

    def _loc_4D66(): pass

    label('loc_4D66')

    SetScenaFlags(ScenaFlag(0x00AE, 2, 0x572))

    ChrTalk(
        0x0008,
        (
            '#0560090596V#691F明白了。\n',
            '准备好了就说一声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x000A, 255)
    OP_4B(0x0008, 255)
    CreateThread(0x000A, 0x00, 0x00, func_02_872)
    EventEnd(0x00)

    Return()

    def _loc_4DAD(): pass

    label('loc_4DAD')

    Jump('loc_4F3D')

    def _loc_4DB0(): pass

    label('loc_4DB0')

    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_4E41',
    )

    ChrTalk(
        0x000A,
        (
            '#0550090597V#800F现在这边也正由格斯塔夫维修长\n',
            '指挥进行起飞前的准备呢。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550090598V如果你们准备好了，\n',
            '就再到这儿来找我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4F3A')

    def _loc_4E41(): pass

    label('loc_4E41')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000A,
        (
            '#0550090599V#800F哦哦，是你们啊。\n',
            '已经准备好了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090600V#010F非常抱歉，\n',
            '可能还要再费些时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0550090601V#800F是吗。\n',
            '现在这边也正由格斯塔夫维修长\n',
            '指挥进行起飞前的准备呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550090602V如果你们准备好了，\n',
            '就再到这儿来找我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4F3A(): pass

    label('loc_4F3A')

    TalkEnd(0x000A)

    def _loc_4F3D(): pass

    label('loc_4F3D')

    Return()

# id: 0x000C offset: 0x4F3E
@scena.Code('func_0C_4F3E')
def func_0C_4F3E():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 3, 0x603)),
            Expr.Return,
        ),
        'loc_4FF0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_4F9C',
    )

    ChrTalk(
        0x00FE,
        (
            '看起来定期船\n',
            '好像会晚点很长时间啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我还是先回家\n',
            '再做打算吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4FED')

    def _loc_4F9C(): pass

    label('loc_4F9C')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '看起来定期船\n',
            '好像会晚点很长时间啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听说军队要盘检，\n',
            '真是麻烦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4FED(): pass

    label('loc_4FED')

    Jump('loc_51C6')

    def _loc_4FF0(): pass

    label('loc_4FF0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_50A9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_5022',
    )

    ChrTalk(
        0x00FE,
        (
            '说起来\n',
            '我是不是来得太早了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_50A6')

    def _loc_5022(): pass

    label('loc_5022')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '哦～早上好啊。\n',
            '你们也是要去王都吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我呀，\n',
            '是要去飞艇公社办些事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且还想赶快把工作搞定，\n',
            '顺便参观诞辰庆典……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_50A6(): pass

    label('loc_50A6')

    Jump('loc_51C6')

    def _loc_50A9(): pass

    label('loc_50A9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_51C6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_5111',
    )

    ChrTalk(
        0x00FE,
        (
            '飞艇的技术\n',
            '真是越来越进步了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '乘坐定期船\n',
            '到多杰的故乡\n',
            '也不再是遥远的梦想了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_51C6')

    def _loc_5111(): pass

    label('loc_5111')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '今天早上，\n',
            '偶然遇到了来自共和国的\n',
            '导力器商人多杰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为他要在飞艇坪参观，\n',
            '我就热情地为他介绍了一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000E, 270, 400)

    ChrTalk(
        0x00FE,
        (
            '看，多杰。\n',
            '那是器材的搬入口，\n',
            '造船设施就在那个地下哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_51C6(): pass

    label('loc_51C6')

    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x51CA
@scena.Code('func_0D_51CA')
def func_0D_51CA():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_526A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_522E',
    )

    ChrTalk(
        0x00FE,
        (
            '我将来也要\n',
            '把飞艇作为商品……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但在那之前，\n',
            '我的城镇得有个飞艇坪才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_526A')

    def _loc_522E(): pass

    label('loc_522E')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '现在只能感叹眼前的景象了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '实在是太棒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_526A(): pass

    label('loc_526A')

    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x526E
@scena.Code('func_0E_526E')
def func_0E_526E():
    Call(0, 0x000A)

    Return()

# id: 0x000F offset: 0x5273
@scena.Code('func_0F_5273')
def func_0F_5273():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 7, 0x517)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 0, 0x518)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5CB6',
    )

    SetScenaFlags(ScenaFlag(0x00A3, 0, 0x518))
    OP_28(0x003F, 0x01, 0x0800)

    If(
        (
            (Expr.Eval, "OP_29(0x003F, 0x01, 0x1000)"),
            Expr.Return,
        ),
        'loc_5299',
    )

    OP_28(0x003F, 0x01, 0x2000)

    def _loc_5299(): pass

    label('loc_5299')

    MapClearFlags(0x00000001)
    EventBegin(0x00)
    ChrSetFlags(0x0008, 0x0004)
    ChrClearFlags(0x0008, 0x0080)
    OP_4A(0x0008, 255)
    ChrTurnDirection(0x0008, 0x0000, 400)

    NpcTalk(
        0x0008,
        '年长的维修员',
        (
            '#0560071427V#690F唔……\n',
            '哎哟，小姑娘你们是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(1000)
    ChrSetPos(0x0000, -44000, -3800, 144340, 135)
    ChrSetPos(0x0001, -44420, -3800, 143430, 90)
    CameraMove(-40020, -3800, 143530, 0)
    OP_67(0, 6510, -10000, 0)
    CameraSetDistance(3620, 0)
    OP_6C(124000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010071428V#004F#6P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '年长的维修员',
        (
            '#0560071429V#690F这个『莱普尼兹号』上\n',
            '堆积着像山一样的各种器材。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560071430V随便靠近可是很危险的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071431V#505F#6P啊，其实我们想找人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071432V#010F#6P我们有点事情，\n',
            '请问格斯塔夫维修长在里面吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '年长的维修员',
        (
            '#0560071433V#692F怎么，找我有事啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071434V#501F#6P哎呀……\n',
            '原来大叔就是维修长啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔他们向格斯塔夫维修长\n',
            '说明了拉赛尔博士委托借用内燃引擎一事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#0560071435V#691F怎么。\n',
            '原来是拉赛尔老爷子啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560071436V要内燃引擎设备吗？\n',
            '你们来得还真是时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071437V#004F#6P哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0560071438V#690F稍等一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_55E8')
    def lambda_55E8():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_55E8')

    DispatchAsync2(0x0101, 0x0000, lambda_55E8)

    @scena.Lambda('lambda_55F9')
    def lambda_55F9():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_55F9')

    DispatchAsync2(0x0102, 0x0000, lambda_55F9)

    @scena.Lambda('lambda_560A')
    def lambda_560A():
        CameraMove(-37020, -3800, 144870, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_560A)

    ChrWalkTo(0x0008, -37260, -3800, 143510, 3000, 0x00)
    ChrWalkTo(0x0008, -31250, -3800, 148530, 3000, 0x00)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010071439V#501F#1P难道就放在工房船上？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071440V#010F#1P嗯，好像是这样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0008, -35640, -3800, 145300, 3000, 0x00)

    @scena.Lambda('lambda_56C0')
    def lambda_56C0():
        CameraMove(-42590, -3800, 143930, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_56C0)

    ChrWalkTo(0x0008, -42710, -3800, 144020, 3000, 0x00)
    WaitForThreadExit(0x0101, 0x0001)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)

    ChrTalk(
        0x0008,
        (
            '#0560071441V#691F来。\n',
            '很重的，小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_92(0x0008, 0x0000, 700, 2000, 0x00)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '内燃引擎设备',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    AddItem(0x0368, 1)
    ChrMoveTo(0x0008, -42710, -3800, 144020, 3000, 0x00)
    ChrSetDirection(0x0008, 270, 400)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5887',
    )

    ChrTalk(
        0x0101,
        (
            '#0010071442V#004F哇哇……\n',
            '的确是沉甸甸的啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010071443V#006F但也不是重到拿不动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0560071444V#692F嘿嘿，\n',
            '想不到小姑娘还挺能干的嘛！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560071445V#693F我很中意你哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071446V#506F嘿嘿，过奖啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5956')

    def _loc_5887(): pass

    label('loc_5887')

    ChrTalk(
        0x0102,
        (
            '#0020071447V#010F确实是很重……\n',
            '不过也不至于重到拿不动就是了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0560071448V#692F哦……\n',
            '小伙子好样的。\n',
            '现在的年轻人还是挺能干的嘛！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560071449V#693F我挺中意你哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071450V#019F您过奖了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5956(): pass

    label('loc_5956')

    ChrTalk(
        0x0008,
        (
            '#0560071451V#691F话说回来，\n',
            '这也真是个有趣的巧合啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560071452V这东西刚从军方那里还回来，\n',
            '马上就被老爷子借走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071453V#004F哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071454V#014F从军方那里还回来？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0560071455V#690F啊，没错啊。\n',
            '那个货样被王国军借走了一阵子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560071456V说是什么研究要用。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560071457V一直用到今天，\n',
            '总算是还给我们工房了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071458V#501F这样啊～\n',
            '的确是有趣的巧合呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071459V#013F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010071460V#004F约修亚，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 1, 0x519)),
            Expr.Return,
        ),
        'loc_5BB1',
    )

    ChrTalk(
        0x0102,
        (
            '#0020071461V#015F不……没什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020071462V#010F需要的东西都已经拿到了，\n',
            '我们快点回博士那里吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5C1C')

    def _loc_5BB1(): pass

    label('loc_5BB1')

    ChrTalk(
        0x0102,
        (
            '#0020071463V#015F不……没什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020071464V#010F……剩下的就是汽油了。\n',
            '马上去中央工房的地下工场吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5C1C(): pass

    label('loc_5C1C')

    ChrTalk(
        0x0101,
        (
            '#0010071465V#006F嗯，知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0008, 400)
    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010071466V#001F维修长大叔，谢谢您！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0560071467V#691F别客气。\n',
            '顺便帮我向老爷子问好哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x0008, 255)
    EventEnd(0x00)

    def _loc_5CB6(): pass

    label('loc_5CB6')

    Return()

# id: 0x0010 offset: 0x5CB7
@scena.Code('func_10_5CB7')
def func_10_5CB7():
    EventBegin(0x00)
    FormationAddMember(0x06, 0xFF)
    ChrSetPos(0x0108, -45670, -4000, 146000, 0)
    ChrSetPos(0x0101, -46540, -4000, 147540, 0)
    ChrSetPos(0x0102, -47220, -4000, 146840, 0)
    ChrSetPos(0x0107, -47150, -4000, 145610, 0)
    ChrTurnDirection(0x0101, 0x0108, 0)
    ChrTurnDirection(0x0102, 0x0108, 0)
    ChrTurnDirection(0x0107, 0x0108, 0)
    ChrTurnDirection(0x0108, 0x0102, 0)
    CameraMove(-45760, -4000, 146000, 0)
    OP_67(0, 9090, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(111000, 0)
    OP_6E(262, 0)
    OP_6F(0x0004, 1)
    OP_6F(0x0003, 0)
    OP_71(0x0006, 0x0004)
    OP_6F(0x0000, 1001)
    OP_72(0x0004, 0x0004)
    OP_72(0x0005, 0x0004)
    OP_25(0x0075, -34230, -4000, 144000, 10000, 40000, 0x64, 0x00000000)
    SetScenaFlags(ScenaFlag(0x00AB, 1, 0x559))
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0010, 0x0080)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0108,
        (
            '#0080090001V#070F……真是抱歉，\n',
            '要你们特地来为我送行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090002V#006F这是当然的啦。\n',
            '昨天真是受到你诸多关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090003V#010F金先生，\n',
            '这就乘定期船直接去王都吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080090004V#072F啊啊……\n',
            '我还有要事必须去办。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080090005V要不是有事在身的话，\n',
            '我一定会留在这里帮你们\n',
            '调查绑架事件的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0108, 0x0107, 400)
    Sleep(400)

    ChrTalk(
        0x0108,
        (
            '#0080090006V#075F抱歉了，小姑娘。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090007V#560F哪、哪儿的话呢。\n',
            '您已经帮了我们很多忙了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090008V金大哥哥，\n',
            '真的非常感谢您呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080090009V#070F哈哈……\n',
            '你能这么说真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(166, 0x00, 0x64)
    Sleep(500)

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('女性的声音')

    Talk(
        (
            '#0880090010V',
            (TxtCtl.SetColor, 0x5),
            '开往王都的定期船\n',
            '『赛希莉亚号』马上就要起飞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0880090011V',
            (TxtCtl.SetColor, 0x5),
            '请尚未登机的乘客尽快登机。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Sleep(500)

    ChrTalk(
        0x0108,
        (
            '#0080090012V#070F哎呀……\n',
            '差不多要出发了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x0108,
        0x28,
        (
            (Expr.PushLong, 0x10),
            (Expr.PushLong, 0x8),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_6096')
    def lambda_6096():
        CameraMove(-40990, -4000, 146200, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_6096)

    @scena.Lambda('lambda_60AE')
    def lambda_60AE():
        CameraSetDistance(3360, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_60AE)

    @scena.Lambda('lambda_60BE')
    def lambda_60BE():
        OP_6C(32000, 4000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_60BE)

    ChrWalkTo(0x0108, -46180, -4000, 144020, 3000, 0x00)
    ChrWalkTo(0x0108, -43180, -3800, 144010, 3000, 0x00)
    ChrSetFlags(0x0108, 0x0004)

    @scena.Lambda('lambda_60FB')
    def lambda_60FB():
        ChrWalkTo(0x00FE, -44880, -4000, 146000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_60FB)

    @scena.Lambda('lambda_6116')
    def lambda_6116():
        ChrWalkTo(0x00FE, -46120, -4000, 145560, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_6116)

    @scena.Lambda('lambda_6131')
    def lambda_6131():
        ChrWalkTo(0x00FE, -46090, -4000, 144690, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_6131)

    ChrWalkTo(0x0108, -36960, -3800, 144020, 3000, 0x00)
    ChrTurnDirection(0x0108, 0x0107, 400)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0108,
        (
            '#0080090013V#070F那再见了。\n',
            '有机会我们再聚吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090014V#501F啊，嗯！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090015V想问一下，\n',
            '金先生会在王国呆多久呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080090016V#073F明确时间还不知道……\n',
            '我想会呆到女王诞辰庆典吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090017V#001F啊，那样的话，\n',
            '说不定我们还会再见面哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090018V#010F到时就请多关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080090019V#071F哈哈，彼此彼此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    PlaySE(120, 0x00, 0x64)
    OP_6F(0x0003, 0)
    OP_70(0x0003, 100)
    OP_73(0x0003)
    Fade(2000)
    CameraMove(-33750, -7050, 155120, 0)
    OP_67(0, -600, -10000, 0)
    CameraSetDistance(3170, 0)
    OP_6C(163000, 0)
    OP_6E(536, 0)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x0107, 0x0080)
    ChrSetFlags(0x0108, 0x0080)
    Sleep(1000)

    OP_A1(0x0011, 0x0004)
    OP_72(0x0004, 0x0004)
    OP_72(0x0004, 0x0020)
    ChrSetPos(0x0011, -34000, -11150, 148000, 0)
    ChrSetFlags(0x0011, 0x0004)
    OP_A1(0x0012, 0x0005)
    OP_72(0x0005, 0x0004)
    OP_72(0x000A, 0x0004)
    ChrSetPos(0x0012, -34000, -11150, 148000, 0)
    ChrSetFlags(0x0012, 0x0004)
    PlaySE(118, 0x00, 0x46)
    OP_6F(0x0004, 0)
    OP_70(0x0004, 60)
    OP_73(0x0004)
    Sleep(1000)

    PlaySE(119, 0x01, 0x64)
    OP_6F(0x0004, 61)
    OP_70(0x0004, 160)
    OP_73(0x0004)
    OP_71(0x0004, 0x0020)
    OP_6F(0x0004, 161)
    OP_70(0x0004, 260)

    @scena.Lambda('lambda_63C8')
    def lambda_63C8():
        CameraMove(-33750, -5050, 155120, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_63C8)

    @scena.Lambda('lambda_63E0')
    def lambda_63E0():
        OP_67(0, 1800, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_63E0)

    ChrMoveToRelativeAsync(0x0011, 0, 300, 0, 300, 0x00)
    ChrMoveToRelativeAsync(0x0011, 0, 800, 0, 500, 0x00)
    Sleep(2000)

    @scena.Lambda('lambda_6425')
    def lambda_6425():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_6425)

    OP_94(0x01, 0x0011, 0x0000, 0x000003E8, 0x000003E8, 0x00)

    @scena.Lambda('lambda_644A')
    def lambda_644A():
        OP_94(0x01, 0x00FE, 0x0000, 0x000004B0, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_644A)

    OP_94(0x01, 0x0011, 0x0000, 0x000004B0, 0x000007D0, 0x00)

    @scena.Lambda('lambda_646F')
    def lambda_646F():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000578, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_646F)

    OP_94(0x01, 0x0011, 0x0000, 0x00000578, 0x00000BB8, 0x00)

    @scena.Lambda('lambda_6494')
    def lambda_6494():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000640, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_6494)

    OP_94(0x01, 0x0011, 0x0000, 0x00000640, 0x00000FA0, 0x00)

    @scena.Lambda('lambda_64B9')
    def lambda_64B9():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000708, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_64B9)

    FadeOut(2000, 0, -1)
    OP_94(0x01, 0x0011, 0x0000, 0x00000708, 0x00001388, 0x00)

    @scena.Lambda('lambda_64E8')
    def lambda_64E8():
        OP_94(0x01, 0x00FE, 0x0000, 0x000007D0, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_64E8)

    OP_94(0x01, 0x0011, 0x0000, 0x000007D0, 0x00001770, 0x00)

    @scena.Lambda('lambda_650D')
    def lambda_650D():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000898, 0x00001B58, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_650D)

    OP_94(0x01, 0x0011, 0x0000, 0x00000898, 0x00001B58, 0x00)

    @scena.Lambda('lambda_6532')
    def lambda_6532():
        OP_94(0x01, 0x00FE, 0x0000, 0x0000C350, 0x00001F40, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_6532)

    @scena.Lambda('lambda_6548')
    def lambda_6548():
        OP_94(0x01, 0x00FE, 0x0000, 0x0000C350, 0x00001F40, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_6548)

    OP_25(0x0075, -34230, -4000, 144000, 10000, 40000, 0x5A, 0x00000000)
    OP_24(0x0077, 0x5A)
    Sleep(100)

    OP_25(0x0075, -34230, -4000, 144000, 10000, 40000, 0x50, 0x00000000)
    OP_24(0x0077, 0x50)
    Sleep(100)

    OP_25(0x0075, -34230, -4000, 144000, 10000, 40000, 0x46, 0x00000000)
    OP_24(0x0077, 0x46)
    Sleep(100)

    OP_25(0x0075, -34230, -4000, 144000, 10000, 40000, 0x3C, 0x00000000)
    OP_24(0x0077, 0x3C)
    Sleep(100)

    OP_25(0x0075, -34230, -4000, 144000, 10000, 40000, 0x32, 0x00000000)
    OP_24(0x0077, 0x32)
    Sleep(100)

    OP_25(0x0075, -34230, -4000, 144000, 10000, 40000, 0x28, 0x00000000)
    OP_24(0x0077, 0x28)
    Sleep(100)

    OP_25(0x0075, -34230, -4000, 144000, 10000, 40000, 0x1E, 0x00000000)
    OP_24(0x0077, 0x1E)
    Sleep(100)

    OP_25(0x0075, -34230, -4000, 144000, 10000, 40000, 0x14, 0x00000000)
    OP_24(0x0077, 0x14)
    Sleep(100)

    OP_25(0x0075, -34230, -4000, 144000, 10000, 40000, 0x0A, 0x00000000)
    OP_24(0x0077, 0x0A)
    Sleep(100)

    OP_25(0x0075, -34230, -4000, 144000, 10000, 40000, 0x01, 0x00000000)
    OP_23(0x0077)
    OP_0D()
    OP_B8(0x07)
    FormationDelMember(0x07, 0xFF)
    ChrSetStatus(0x0000, 0xFE, 0)
    ChrSetStatus(0x0001, 0xFE, 0)
    ChrSetStatus(0x0002, 0xFE, 0)
    ChrSetStatus(0x0003, 0xFE, 0)
    ChrSetStatus(0x0004, 0xFE, 0)
    ChrSetStatus(0x0005, 0xFE, 0)
    ChrSetStatus(0x0006, 0xFE, 0)
    ChrSetStatus(0x0007, 0xFE, 0)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T3101._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0011 offset: 0x66FF
@scena.Code('func_11_66FF')
def func_11_66FF():
    Sleep(100)

    OP_20(0x000003E8)
    Fade(1000)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x0107, 0x0080)
    ChrSetFlags(0x0106, 0x0080)
    ChrSetFlags(0x0008, 0x0080)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0107, 0xFF)
    TerminateThread(0x0106, 0xFF)
    TerminateThread(0x000A, 0xFF)
    ChrSetDirection(0x000A, 45, 0)
    ChrSetPos(0x000B, -45980, 0, 129680, 0)
    ChrClearFlags(0x000B, 0x0080)
    OP_23(0x0075)
    PlaySE(117, 0x01, 0x64)
    CameraMove(-36160, -4000, 150300, 0)
    OP_67(0, 11000, -10000, 0)
    CameraSetDistance(3500, 0)
    OP_6C(112000, 0)
    OP_6E(415, 0)
    OP_0D()
    PlayBGM(87)
    PlaySE(120, 0x00, 0x64)
    OP_6F(0x0003, 0)
    OP_70(0x0003, 100)
    OP_73(0x0003)
    OP_72(0x0004, 0x0004)
    OP_A1(0x0011, 0x0004)
    OP_72(0x0009, 0x0004)
    OP_72(0x0009, 0x0020)
    ChrSetPos(0x0011, -34000, -11150, 148000, 0)
    ChrSetFlags(0x0011, 0x0004)
    OP_A1(0x0012, 0x0005)
    OP_72(0x0005, 0x0004)
    OP_72(0x000A, 0x0004)
    ChrSetPos(0x0012, -34000, -11150, 148000, 0)
    ChrSetFlags(0x0012, 0x0004)

    @scena.Lambda('lambda_680B')
    def lambda_680B():
        OP_67(0, 7880, -10000, 12000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_680B)

    PlaySE(118, 0x00, 0x64)
    OP_6F(0x0004, 1)
    OP_70(0x0004, 60)
    OP_73(0x0004)
    PlaySE(119, 0x01, 0x64)
    OP_6F(0x0004, 61)
    OP_70(0x0004, 160)
    OP_73(0x0004)
    OP_71(0x0004, 0x0020)
    OP_6F(0x0004, 161)
    OP_70(0x0004, 260)

    @scena.Lambda('lambda_6862')
    def lambda_6862():
        OP_6E(465, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_6862)

    @scena.Lambda('lambda_6872')
    def lambda_6872():
        OP_6C(90000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_6872)

    ChrMoveToRelativeAsync(0x0011, 0, 500, 0, 300, 0x00)
    ChrMoveToRelativeAsync(0x0011, 0, 1000, 0, 600, 0x00)
    Sleep(500)

    @scena.Lambda('lambda_68AF')
    def lambda_68AF():
        OP_94(0x01, 0x00FE, 0x0000, 0x000001F4, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_68AF)

    OP_94(0x01, 0x0011, 0x0000, 0x000001F4, 0x000003E8, 0x00)

    @scena.Lambda('lambda_68D4')
    def lambda_68D4():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000258, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_68D4)

    OP_94(0x01, 0x0011, 0x0000, 0x00000258, 0x000007D0, 0x00)

    @scena.Lambda('lambda_68F9')
    def lambda_68F9():
        OP_94(0x01, 0x00FE, 0x0000, 0x000002BC, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_68F9)

    OP_94(0x01, 0x0011, 0x0000, 0x000002BC, 0x00000BB8, 0x00)

    @scena.Lambda('lambda_691E')
    def lambda_691E():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000320, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_691E)

    OP_94(0x01, 0x0011, 0x0000, 0x00000320, 0x00000FA0, 0x00)

    @scena.Lambda('lambda_6943')
    def lambda_6943():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000384, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_6943)

    OP_94(0x01, 0x0011, 0x0000, 0x00000384, 0x00001388, 0x00)

    @scena.Lambda('lambda_6968')
    def lambda_6968():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_6968)

    OP_94(0x01, 0x0011, 0x0000, 0x000003E8, 0x00001770, 0x00)

    @scena.Lambda('lambda_698D')
    def lambda_698D():
        OP_94(0x01, 0x00FE, 0x0000, 0x0000044C, 0x00001B58, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_698D)

    OP_94(0x01, 0x0011, 0x0000, 0x0000044C, 0x00001B58, 0x00)

    @scena.Lambda('lambda_69B2')
    def lambda_69B2():
        OP_94(0x01, 0x00FE, 0x0000, 0x0000C350, 0x00001F40, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_69B2)

    @scena.Lambda('lambda_69C8')
    def lambda_69C8():
        OP_94(0x01, 0x00FE, 0x0000, 0x0000C350, 0x00001F40, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_69C8)

    CreateThread(0x0011, 0x03, 0x00, func_12_6D9A)
    ChrSetDirection(0x000A, 0, 400)

    ChrTalk(
        0x000A,
        (
            '#0550090642V#800F#5P拜托你们了，各位游击士……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0280090643V#1P等、等一下～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_6A43')
    def lambda_6A43():
        CameraMove(-44410, -4000, 143480, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6A43)

    @scena.Lambda('lambda_6A5B')
    def lambda_6A5B():
        OP_6E(273, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_6A5B)

    @scena.Lambda('lambda_6A6B')
    def lambda_6A6B():
        ChrTurnDirection(0x00FE, 0x000B, 400)
        Yield()

        Jump('lambda_6A6B')

    DispatchAsync2(0x000A, 0x0001, lambda_6A6B)

    ChrWalkTo(0x000B, -46510, -4000, 144200, 5000, 0x00)

    ChrTalk(
        0x000B,
        (
            '#0280090644V#152F#1P哈啊哈啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280090645V啊啊～走掉了～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0550090646V#802F#2P啊……\n',
            '这不是朵洛希吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x000A, 0xFF)
    ChrWalkTo(0x000A, -46550, -4000, 142020, 2000, 0x00)
    ChrTurnDirection(0x000A, 0x000B, 0)
    ChrTurnDirection(0x000B, 0x000A, 400)

    ChrTalk(
        0x000B,
        (
            '#0280090647V#152F#1P啊，工房长先生！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280090648V刚才飞走的那艘飞艇，\n',
            '是小艾和小约他们坐的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0550090649V#802F#2P是啊……\n',
            '你怎么知道的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0280090650V#152F#1P我刚刚去了协会，\n',
            '是那里的负责人告诉我的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280090651V刚才我和编辑部联络的时候，\n',
            '知道了一件非常非常不得了的大事，\n',
            '不告诉他们不行啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0550090652V#805F#2P不得了的大事……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550090653V#806F唔……以现在的状况，\n',
            '实在想不出还有什么更不得了的事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0280090654V#154F#1P这个嘛……\n',
            '虽然是非公开发表的～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280090655V女王陛下的王室亲卫队\n',
            '好像以谋反的罪名被逮捕了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0550090656V#804F#2P#3S什、什么！？',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/E0002._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0012 offset: 0x6D9A
@scena.Code('func_12_6D9A')
def func_12_6D9A():
    Sleep(1000)

    OP_24(0x0077, 0x5F)
    OP_24(0x0075, 0x5F)
    Sleep(200)

    OP_24(0x0077, 0x5A)
    OP_24(0x0075, 0x5A)
    Sleep(200)

    OP_24(0x0077, 0x55)
    OP_24(0x0075, 0x55)
    Sleep(200)

    OP_24(0x0077, 0x50)
    OP_24(0x0075, 0x50)
    Sleep(200)

    OP_24(0x0077, 0x4B)
    OP_24(0x0075, 0x4B)
    Sleep(200)

    OP_24(0x0077, 0x46)
    OP_24(0x0075, 0x46)
    Sleep(200)

    OP_24(0x0077, 0x41)
    OP_24(0x0075, 0x41)
    Sleep(200)

    OP_24(0x0077, 0x3C)
    OP_24(0x0075, 0x3C)
    Sleep(200)

    OP_24(0x0077, 0x32)
    OP_24(0x0075, 0x32)
    Sleep(200)

    OP_23(0x0077)
    OP_23(0x0075)

    Return()

# id: 0x0013 offset: 0x6E1B
@scena.Code('func_13_6E1B')
def func_13_6E1B():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 2, 0x602)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 3, 0x603)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_8126',
    )

    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x00C0, 3, 0x603))
    OP_28(0x0054, 0x01, 0x0004)
    OP_28(0x0054, 0x01, 0x0008)
    ChrSetPos(0x000C, -46060, 0, 127820, 0)
    ChrClearFlags(0x000C, 0x0080)
    PlaySE(402, 0x00, 0x64)

    ChrTalk(
        0x000C,
        (
            '#2030100203V喵～呵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0102, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    @scena.Lambda('lambda_6E9C')
    def lambda_6E9C():
        ChrTurnDirection(0x00FE, 0x000C, 400)
        Yield()

        Jump('lambda_6E9C')

    DispatchAsync2(0x0101, 0x0003, lambda_6E9C)

    @scena.Lambda('lambda_6EAD')
    def lambda_6EAD():
        ChrTurnDirection(0x00FE, 0x000C, 400)
        Yield()

        Jump('lambda_6EAD')

    DispatchAsync2(0x0102, 0x0003, lambda_6EAD)

    @scena.Lambda('lambda_6EBE')
    def lambda_6EBE():
        CameraMove(-46010, -1000, 131740, 2500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_6EBE)

    @scena.Lambda('lambda_6ED6')
    def lambda_6ED6():
        OP_67(0, 7390, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_6ED6)

    @scena.Lambda('lambda_6EEE')
    def lambda_6EEE():
        CameraSetDistance(3700, 4000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_6EEE)

    @scena.Lambda('lambda_6EFE')
    def lambda_6EFE():
        OP_6C(158000, 4000)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_6EFE)

    Sleep(3000)

    ChrSetPos(0x0101, -45400, -4000, 140210, 0)
    ChrSetPos(0x0102, -46640, -4000, 140440, 0)

    @scena.Lambda('lambda_6F35')
    def lambda_6F35():
        ChrWalkTo(0x00FE, -45660, -4000, 138540, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_6F35)

    @scena.Lambda('lambda_6F50')
    def lambda_6F50():
        CameraMove(-45610, -4000, 139000, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_6F50)

    Sleep(3000)

    If(
        (
            (Expr.Eval, "OP_29(0x002C, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_7136',
    )

    ChrTalk(
        0x0101,
        (
            '#0010100269V#004F啊，安东尼！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100270V#010F哟，昨天辛苦你了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(402, 0x00, 0x64)

    ChrTalk(
        0x000C,
        (
            '#2030100207V喵呜～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100272V#509F真是的，都是因为你，\n',
            '昨天害我吓了一大跳呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100210V你是不是该反省一下呢，嗯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(402, 0x00, 0x64)

    ChrTalk(
        0x000C,
        (
            '#2030100274V咪呜？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100212V#007F都不听我说话啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100213V#019F哈哈，说不定它是在装傻呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100277V#006F唉，算了。\n',
            '总之承蒙你的关照啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100278V多谢了，安东尼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(402, 0x00, 0x64)

    ChrTalk(
        0x000C,
        (
            '#2030100279V咪～呜嗯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_72E4')

    def _loc_7136(): pass

    label('loc_7136')

    ChrTalk(
        0x0101,
        (
            '#0010100204V#004F啊，那只猫是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100205V#010F就是那个时候\n',
            '钻进集装箱里的那只猫吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100206V我记得，\n',
            '好像是叫做安东尼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(402, 0x00, 0x64)

    ChrTalk(
        0x000C,
        (
            '#2030100207V喵呜～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100208V#001F啊哈哈～真可爱。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100209V#006F真是的，都是因为你，\n',
            '昨天害我吓了一大跳呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100210V你是不是该反省一下呢，嗯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(402, 0x00, 0x64)

    ChrTalk(
        0x000C,
        (
            '#2030100211V咪呜？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100212V#007F都不听我说话啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100213V#019F哈哈，说不定它是在装傻呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_72E4(): pass

    label('loc_72E4')

    ChrSetPos(0x0008, -47160, 0, 129750, 0)
    ChrClearFlags(0x0008, 0x0080)

    ChrTalk(
        0x0008,
        (
            '#0560100214V#3P哦，是你们啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4A(0x0008, 255)
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0102, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    @scena.Lambda('lambda_7350')
    def lambda_7350():
        CameraMove(-46010, -4000, 137720, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_7350)

    @scena.Lambda('lambda_7368')
    def lambda_7368():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_7368')

    DispatchAsync2(0x0101, 0x0003, lambda_7368)

    @scena.Lambda('lambda_7379')
    def lambda_7379():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_7379')

    DispatchAsync2(0x0102, 0x0003, lambda_7379)

    @scena.Lambda('lambda_738A')
    def lambda_738A():
        ChrWalkTo(0x00FE, -46190, -4000, 138820, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_738A)

    Sleep(1000)

    @scena.Lambda('lambda_73AA')
    def lambda_73AA():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_73AA')

    DispatchAsync2(0x0101, 0x0003, lambda_73AA)

    @scena.Lambda('lambda_73BB')
    def lambda_73BB():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_73BB')

    DispatchAsync2(0x0102, 0x0003, lambda_73BB)

    ChrSetDirection(0x000C, 192, 800)

    @scena.Lambda('lambda_73D3')
    def lambda_73D3():
        ChrMoveTo(0x00FE, -45660, 0, 128289, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_73D3)

    WaitForThreadExit(0x0008, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010100215V#501F啊，维修长先生！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0560100216V#691F#2P工房长都告诉我了。\n',
            '博士救出作战干得真是漂亮啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560100217V博士对我们这些技术人员来说，\n',
            '算是师傅一样的人物了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560100218V我也要好好感谢你们呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)

    ChrTalk(
        0x0101,
        (
            '#0010100219V#008F嘿嘿……\n',
            '这也多亏了维修长你们的帮忙啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100220V不过我真是被那孩子吓坏了呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100221V#010F那个安东尼，\n',
            '果然是您故意放进去的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0560100222V#693F#2P啊哈哈，要想欺骗敌人，\n',
            '首先要瞒过伙伴才行啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560100223V#691F话说回来，\n',
            '你们来飞艇坪有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100224V#006F嗯，受博士的委托，\n',
            '我们现在要赶往王都。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100225V#010F要乘坐１１点的定期船，\n',
            '看来好像来得早了点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0560100226V#692F#2P啊啊……\n',
            '好像要稍微晚到一会儿。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560100227V#691F因为还要花点时间卸货，\n',
            '你们到街上再转一会也没关系啦。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100228V#505F嗯，这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0009, -45980, 0, 128889, 0)
    OP_4A(0x0009, 255)

    ChrTalk(
        0x0009,
        (
            '#1970100229V#3P喂，你们两位！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0102, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    @scena.Lambda('lambda_7790')
    def lambda_7790():
        ChrWalkTo(0x0009, -45170, -4000, 138180, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_7790)

    @scena.Lambda('lambda_77AB')
    def lambda_77AB():
        CameraMove(-46700, -2500, 134910, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_77AB)

    @scena.Lambda('lambda_77C3')
    def lambda_77C3():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_77C3')

    DispatchAsync2(0x0101, 0x0002, lambda_77C3)

    @scena.Lambda('lambda_77D4')
    def lambda_77D4():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_77D4')

    DispatchAsync2(0x0102, 0x0002, lambda_77D4)

    @scena.Lambda('lambda_77E5')
    def lambda_77E5():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_77E5')

    DispatchAsync2(0x0008, 0x0002, lambda_77E5)

    Sleep(1500)

    @scena.Lambda('lambda_77FB')
    def lambda_77FB():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_77FB')

    DispatchAsync2(0x0101, 0x0002, lambda_77FB)

    @scena.Lambda('lambda_780C')
    def lambda_780C():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_780C')

    DispatchAsync2(0x0102, 0x0002, lambda_780C)

    @scena.Lambda('lambda_781D')
    def lambda_781D():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_781D')

    DispatchAsync2(0x0008, 0x0002, lambda_781D)

    @scena.Lambda('lambda_782E')
    def lambda_782E():
        CameraMove(-46010, -4000, 137720, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_782E)

    WaitForThreadExit(0x0009, 0x0001)
    ChrTurnDirection(0x0009, 0x0102, 0)

    ChrTalk(
        0x0008,
        (
            '#0560100230V#692F#2P什么啊，这不是吉拉尔吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560100231V怎么，发生了什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0008, 400)

    ChrTalk(
        0x0009,
        (
            '#1970100232V正好，\n',
            '大叔您也在啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970100233V实际上，事情变得麻烦起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0560100234V#692F#2P你说什么，麻烦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970100235V嗯，是啊……\n',
            '飞艇公社发来的联络说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970100236V定期船可能要\n',
            '晚几个小时才能到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100237V#004F哎……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100238V#012F#6P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0560100239V#692F#2P喂喂……\n',
            '到底是怎么回事啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560100240V又有空贼作乱吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970100241V啊，说起来也差不多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970100242V据说，有一伙打算妨碍\n',
            '女王陛下的诞辰庆典的恐怖分子\n',
            '可能在王国的某个地方潜伏着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970100243V为了调查这件事，\n',
            '所有的飞艇坪都被军队设下了哨卡。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100244V#002F（那、那个是……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100245V#015F#6P（大概是为了搜寻博士他们吧……）\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970100246V所以，开往王都的定期船\n',
            '现在还滞留在卢安那里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970100247V取而代之的好像是\n',
            '雷斯顿要塞的军用警备飞艇。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0560100248V#691F#2P原来如此，是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560100249V不过这样一来，\n',
            '你不是就要很忙了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0008, 400)

    ChrTalk(
        0x0009,
        (
            '#1970100250V是啊……\n',
            '不把这件事告诉旅客们不行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0009,
        (
            '#1970100251V就因为这样，\n',
            '你们也得再等一段时间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1970100252V对了……\n',
            '如果你们愿意在游击士协会等的话，\n',
            '我去帮你们联系一下吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100253V#505F嗯，好的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100254V#010F#6P真是麻烦您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0009, 190, 400)
    ChrMoveTo(0x0009, -46020, 0, 129410, 3000, 0x00)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0008, 0xFF)
    ChrSetPos(0x0009, -20110, 8000, 121830, 177)
    OP_4B(0x0009, 255)
    TerminateThread(0x0008, 0xFF)
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#0560100255V#690F#2P……真是可疑啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560100256V如果军队那帮家伙这样干的话，\n',
            '莱普尼兹号肯定也会被检查的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560100257V我这就去和工房长说这件事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_7E39')
    def lambda_7E39():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_7E39')

    DispatchAsync2(0x0101, 0x0002, lambda_7E39)

    @scena.Lambda('lambda_7E4A')
    def lambda_7E4A():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_7E4A')

    DispatchAsync2(0x0102, 0x0002, lambda_7E4A)

    ChrTalk(
        0x0101,
        (
            '#0010100258V#002F对啊，要是查起昨天那件事的话，\n',
            '那中央工房就不好办了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100259V#012F请一定要小心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0560100260V#691F#2P哈哈，我还没有不中用到\n',
            '让你们这些小孩子担心的份儿上呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0560100261V#693F那么告辞了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 190, 600)
    ChrMoveTo(0x0008, -46190, 0, 129250, 4000, 0x00)
    ChrSetFlags(0x0008, 0x0080)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)

    @scena.Lambda('lambda_7F68')
    def lambda_7F68():
        CameraMove(-45920, -4000, 139870, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_7F68)

    ChrTurnDirection(0x0101, 0x0102, 400)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010100262V#002F约修亚……\n',
            '这样不就很麻烦了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020100263V#013F嗯……\n',
            '这样的话乘定期船就有点危险了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100264V#012F虽然要花点时间，\n',
            '不过还是走街道比较好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100265V#509F唔，还以为好不容易\n',
            '可以坐上久违的飞艇了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100266V我跟你没完，理查德上校！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100267V#019F算了算了，\n',
            '当成是继续修行不也很好吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100268V#010F那么，我们赶快去接待处那里\n',
            '把搭乘手续取消吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x000C, 0x0080)
    EventEnd(0x00)

    def _loc_8126(): pass

    label('loc_8126')

    Return()

# id: 0x0014 offset: 0x8127
@scena.Code('func_14_8127')
def func_14_8127():
    ChrSetFlags(0x00FE, 0x0004)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -34090, -4000, 144010, 270)
    ChrSetDirection(0x00FE, 270, 400)

    Return()

# id: 0x0015 offset: 0x814A
@scena.Code('func_15_814A')
def func_15_814A():
    ChrSetFlags(0x00FE, 0x0004)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -35750, -4000, 143010, 90)
    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x0016 offset: 0x816D
@scena.Code('func_16_816D')
def func_16_816D():
    ChrSetFlags(0x00FE, 0x0004)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -35770, -4000, 144120, 90)
    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x0017 offset: 0x8190
@scena.Code('func_17_8190')
def func_17_8190():
    ChrSetFlags(0x00FE, 0x0004)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetPos(0x00FE, -36170, -4000, 145050, 90)
    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x0018 offset: 0x81B3
@scena.Code('func_18_81B3')
def func_18_81B3():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '定期船起降坪\n',
            '≡　开往王都格兰赛尔\n',
            '≡　开往卢安市',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※请勿携带易燃物和危险品\n',
            '　　　　　利贝尔飞艇公社',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0019 offset: 0x824D
@scena.Code('func_19_824D')
def func_19_824D():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　　　飞艇坪塔台　　　　\n',
            '　※无关人员禁止入内　　\n',
            '『利贝尔飞艇公社』　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x001A offset: 0x82C6
@scena.Code('func_1A_82C6')
def func_1A_82C6():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 3, 0x603)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 4, 0x604)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_8355',
    )

    EventBegin(0x02)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020100282V#010F首先去取消搭乘手续，\n',
            '把票退掉吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100281V然后，    \n',
            '我们就出发吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_8355(): pass

    label('loc_8355')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

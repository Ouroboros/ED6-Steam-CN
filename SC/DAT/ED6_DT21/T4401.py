import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4401_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4401   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4401.x'
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
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
        ('ED6_DT07/CH01530._CH', 'ED6_DT07/CH01530P._CP'),
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
        ('ED6_DT07/CH01530._CH', 'ED6_DT07/CH01530P._CP'),
        ('ED6_DT07/CH01500._CH', 'ED6_DT07/CH01500P._CP'),
        ('ED6_DT07/CH01500._CH', 'ED6_DT07/CH01500P._CP'),
        ('ED6_DT07/CH01500._CH', 'ED6_DT07/CH01500P._CP'),
        ('ED6_DT07/CH01530._CH', 'ED6_DT07/CH01530P._CP'),
        ('ED6_DT07/CH01550._CH', 'ED6_DT07/CH01550P._CP'),
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
        ('ED6_DT07/CH01690._CH', 'ED6_DT07/CH01690P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01170._CH', 'ED6_DT07/CH01170P._CP'),
    ]

# id: 0x10001 offset: 0x13A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '丹克',
            x                   = 4280,
            z                   = 1500,
            y                   = 93750,
            direction           = 45,
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
            name                = '歌德',
            x                   = 14220,
            z                   = 0,
            y                   = 57490,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '罗布',
            x                   = 14850,
            z                   = 0,
            y                   = 104990,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '工人',
            x                   = -3760,
            z                   = 0,
            y                   = 30260,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '工人',
            x                   = 45200,
            z                   = 0,
            y                   = 48610,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '工人',
            x                   = -5140,
            z                   = 0,
            y                   = 76620,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '工人',
            x                   = -6530,
            z                   = 0,
            y                   = 109060,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '工人',
            x                   = 2760,
            z                   = 5500,
            y                   = 110270,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '工人',
            x                   = 3210,
            z                   = 1500,
            y                   = 106100,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '围观者',
            x                   = -14940,
            z                   = 0,
            y                   = 109290,
            direction           = 331,
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
            name                = '围观者',
            x                   = -16290,
            z                   = 0,
            y                   = 109480,
            direction           = 315,
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
            name                = '围观者',
            x                   = 13900,
            z                   = 0,
            y                   = 123350,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '围观者',
            x                   = 17930,
            z                   = 0,
            y                   = 122800,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '围观者',
            x                   = 22520,
            z                   = 0,
            y                   = 123430,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            name                = '围观者',
            x                   = -19490,
            z                   = 0,
            y                   = 106510,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            name                = '围观者',
            x                   = -13780,
            z                   = 0,
            y                   = 109360,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '围观者',
            x                   = -12350,
            z                   = 0,
            y                   = 109360,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            name                = '围观者',
            x                   = 23190,
            z                   = 0,
            y                   = 120570,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            name                = '王都格兰赛尔·码头南',
            x                   = -880,
            z                   = 0,
            y                   = -32689,
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

# id: 0x10002 offset: 0x39A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x39A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x39A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 40210,
            triggerZ            = 800,
            triggerY            = 54960,
            triggerRange        = 800,
            actorX              = 40410,
            actorZ              = 2200,
            actorY              = 54960,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0018,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 3110,
            triggerZ            = 2450,
            triggerY            = 121430,
            triggerRange        = 1000,
            actorX              = 3230,
            actorZ              = -1500,
            actorY              = 127300,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0019,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -19490,
            triggerZ            = 0,
            triggerY            = 109370,
            triggerRange        = 1700,
            actorX              = -19490,
            actorZ              = 0,
            actorY              = 109370,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001A,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x406
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_464',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_461',
    )

    ChrSetPos(0x000A, 18510, 0, 111750, 320)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    ChrSetFlags(0x0017, 0x0010)
    ChrSetFlags(0x0018, 0x0010)

    def _loc_461(): pass

    label('loc_461')

    Jump('loc_668')

    def _loc_464(): pass

    label('loc_464')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_668',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_47A',
    )

    Jump('loc_668')

    def _loc_47A(): pass

    label('loc_47A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_4DC',
    )

    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrSetPos(0x0011, 13720, 0, 54670, 18)
    ChrSetPos(0x0012, 9200, 0, 81310, 348)
    ChrSetPos(0x0013, 23080, 0, 91150, 85)
    ChrSetPos(0x0014, 12070, 0, 38910, 281)

    Jump('loc_668')

    def _loc_4DC(): pass

    label('loc_4DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_567',
    )

    ChrSetFlags(0x000A, 0x0010)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    ChrSetPos(0x0015, -22340, 0, 78050, 271)
    ChrSetPos(0x0016, 19180, 0, 114150, 252)
    ChrSetPos(0x0017, 18930, 0, 113030, 217)
    ChrSetPos(0x0018, -29540, 0, 75460, 360)
    ChrSetPos(0x0019, -29540, 0, 76300, 180)
    ChrSetFlags(0x0018, 0x0010)
    ChrSetFlags(0x0019, 0x0010)

    Jump('loc_668')

    def _loc_567(): pass

    label('loc_567')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_5E9',
    )

    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    ChrSetPos(0x0015, -12470, 0, 82840, 332)
    ChrSetPos(0x0016, 19180, 0, 114150, 252)
    ChrSetPos(0x0017, 18930, 0, 113030, 217)
    ChrSetPos(0x0018, 26840, 0, 72510, 179)
    ChrSetPos(0x0019, 27510, 0, 60850, 12)
    ChrSetFlags(0x0018, 0x0010)
    ChrSetFlags(0x0019, 0x0010)

    Jump('loc_668')

    def _loc_5E9(): pass

    label('loc_5E9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_668',
    )

    ChrSetFlags(0x000A, 0x0010)
    ChrSetFlags(0x000C, 0x0010)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    ChrSetPos(0x0015, -12470, 0, 82840, 332)
    ChrSetPos(0x0016, 19180, 0, 114150, 252)
    ChrSetPos(0x0017, 18930, 0, 113030, 217)
    ChrSetPos(0x0018, 26170, 0, 60420, 37)
    ChrSetPos(0x0019, -1210, 0, 67700, 180)

    def _loc_668(): pass

    label('loc_668')

    Return()

# id: 0x0001 offset: 0x669
@scena.Code('func_01_669')
def func_01_669():
    OP_16(0x02, 4000, -122000, -73000, 2293870)
    PlaySE(453, 0x00, 0x64)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 5, 0x1625)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 6, 0x1626)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 4, 0x162C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6A0',
    )

    OP_B1('t4401_y')

    Jump('loc_6A9')

    def _loc_6A0(): pass

    label('loc_6A0')

    OP_B1('t4401_n')

    def _loc_6A9(): pass

    label('loc_6A9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6B5',
    )

    OP_64(0x02, 0x0001)

    def _loc_6B5(): pass

    label('loc_6B5')

    Return()

# id: 0x0002 offset: 0x6B6
@scena.Code('func_02_6B6')
def func_02_6B6():
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
        'loc_6DB',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_81D')

    def _loc_6DB(): pass

    label('loc_6DB')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6F4',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_81D')

    def _loc_6F4(): pass

    label('loc_6F4')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_70D',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_81D')

    def _loc_70D(): pass

    label('loc_70D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_726',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_81D')

    def _loc_726(): pass

    label('loc_726')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_73F',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_81D')

    def _loc_73F(): pass

    label('loc_73F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_758',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_81D')

    def _loc_758(): pass

    label('loc_758')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_771',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_81D')

    def _loc_771(): pass

    label('loc_771')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_78A',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_81D')

    def _loc_78A(): pass

    label('loc_78A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7A3',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_81D')

    def _loc_7A3(): pass

    label('loc_7A3')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7BC',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_81D')

    def _loc_7BC(): pass

    label('loc_7BC')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7D5',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_81D')

    def _loc_7D5(): pass

    label('loc_7D5')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7EE',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_81D')

    def _loc_7EE(): pass

    label('loc_7EE')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_807',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_81D')

    def _loc_807(): pass

    label('loc_807')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_81D',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_81D(): pass

    label('loc_81D')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_832',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_81D')

    def _loc_832(): pass

    label('loc_832')

    Return()

# id: 0x0003 offset: 0x833
@scena.Code('func_03_833')
def func_03_833():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_856',
    )

    OP_8D(0x00FE, 21480, 122570, 23470, 120150, 2000)

    Jump('func_03_833')

    def _loc_856(): pass

    label('loc_856')

    Return()

# id: 0x0004 offset: 0x857
@scena.Code('func_04_857')
def func_04_857():
    TalkBegin(0x0008)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_963',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_960',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_8BF',
    )

    ChrTalk(
        0x00FE,
        (
            '导力停止之后，\n',
            '船不来也没法工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这下坦白说\n',
            '真是束手无策啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_960')

    def _loc_8BF(): pass

    label('loc_8BF')

    ChrTalk(
        0x00FE,
        (
            '来参观那个螺一样的物体\n',
            '的人越来越多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是平时会阻碍工作\n',
            '会把他们赶走……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '导力停止之后，\n',
            '船不来也没法工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这下坦白说\n',
            '真是束手无策啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_960(): pass

    label('loc_960')

    Jump('loc_E91')

    def _loc_963(): pass

    label('loc_963')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E91',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_A96',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02CA, 3, 0x1653)),
            Expr.Return,
        ),
        'loc_9DE',
    )

    ChrTalk(
        0x00FE,
        (
            '偷走引擎的家伙们，\n',
            '企图做什么不得了的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果你们没来，\n',
            '现在还不知道会变成怎样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A93')

    def _loc_9DE(): pass

    label('loc_9DE')

    ChrTalk(
        0x00FE,
        (
            '哦，你们不是\n',
            '那天晚上的游击士吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '偷走引擎的家伙们，\n',
            '企图做什么不得了的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果你们没来，\n',
            '现在还不知道会变成怎样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管怎样，谢谢你们了。\n',
            '让我再次道谢吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x02CA, 3, 0x1653))

    def _loc_A93(): pass

    label('loc_A93')

    Jump('loc_E91')

    def _loc_A96(): pass

    label('loc_A96')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_BB2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_AF3',
    )

    ChrTalk(
        0x00FE,
        (
            '诺曼新市长\n',
            '也不会对港口使坏的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '致力于旅游事业\n',
            '我想是很不错的啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BAF')

    def _loc_AF3(): pass

    label('loc_AF3')

    ChrTalk(
        0x00FE,
        (
            '看来卢安的市长\n',
            '决定是诺曼氏了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们是觉得，参与港湾事业\n',
            '的波尔多斯氏当选\n',
            '会有更多利益……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过诺曼氏也不会\n',
            '完全不考虑港口的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，暂时用温和的目光\n',
            '观察一下情况吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_BAF(): pass

    label('loc_BAF')

    Jump('loc_E91')

    def _loc_BB2(): pass

    label('loc_BB2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_CB9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_C0F',
    )

    ChrTalk(
        0x00FE,
        (
            '对了对了，卢安\n',
            '正在举行市长选举呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '卢安市民到底\n',
            '会选哪边呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CB6')

    def _loc_C0F(): pass

    label('loc_C0F')

    ChrTalk(
        0x00FE,
        (
            '对了对了，卢安\n',
            '正在举行市长选举呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '卢安市民到底\n',
            '会选哪边呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为同样在港口工作\n',
            '很想支援波尔多斯氏……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过候选人诺曼氏\n',
            '说的话也很有说服力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_CB6(): pass

    label('loc_CB6')

    Jump('loc_E91')

    def _loc_CB9(): pass

    label('loc_CB9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_DAF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_D23',
    )

    ChrTalk(
        0x00FE,
        (
            '解决了１个问题\n',
            '后面的问题又紧接而来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '工作就是这样反复不断,\n',
            '总是无法随人愿啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DAC')

    def _loc_D23(): pass

    label('loc_D23')

    ChrTalk(
        0x00FE,
        (
            '解决了１个问题\n',
            '后面的问题又紧接而来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '工作就是这样反复不断,\n',
            '总是无法随人愿啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正因如此，有费心的价值\n',
            '才有趣也说不定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_DAC(): pass

    label('loc_DAC')

    Jump('loc_E91')

    def _loc_DAF(): pass

    label('loc_DAF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_E91',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_E0A',
    )

    ChrTalk(
        0x00FE,
        (
            '因为卢安市长不在\n',
            '船的通过审查推迟了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '害得我们的工作\n',
            '好难计划。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E91')

    def _loc_E0A(): pass

    label('loc_E0A')

    ChrTalk(
        0x00FE,
        (
            '王都进港的船全部\n',
            '都要通过卢安的卢比诺川\n',
            '才能过来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为卢安市长不在\n',
            '船的通过审查推迟了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '害得我们的工作\n',
            '好难计划。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_E91(): pass

    label('loc_E91')

    TalkEnd(0x0008)

    Return()

# id: 0x0005 offset: 0xE95
@scena.Code('func_05_E95')
def func_05_E95():
    TalkBegin(0x0009)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F83',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_F80',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_F03',
    )

    ChrTalk(
        0x00FE,
        (
            '自从导力船被导入后\n',
            '也没造过帆船之类的了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈……\n',
            '不能想点办法吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F80')

    def _loc_F03(): pass

    label('loc_F03')

    ChrTalk(
        0x00FE,
        (
            '我们的工作\n',
            '要是没有船\n',
            '就根本没办法了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '自从导力船被导入后\n',
            '也没造过帆船之类的了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈……\n',
            '不能想点办法吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_F80(): pass

    label('loc_F80')

    Jump('loc_139A')

    def _loc_F83(): pass

    label('loc_F83')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_139A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1068',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_FF1',
    )

    ChrTalk(
        0x00FE,
        (
            '被破坏的仓库门\n',
            '和港口设施似乎会有补偿金。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '国家的对应够快真是帮大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1065')

    def _loc_FF1(): pass

    label('loc_FF1')

    ChrTalk(
        0x00FE,
        (
            '仓库的借主好像\n',
            '是情报部的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难道保管了\n',
            '开发中的导力战车之类的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大吃一惊眼珠子\n',
            '都差点跳出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_1065(): pass

    label('loc_1065')

    Jump('loc_139A')

    def _loc_1068(): pass

    label('loc_1068')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_113B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_10BF',
    )

    ChrTalk(
        0x00FE,
        (
            '和借仓库的人\n',
            '联络不上啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '差不多该进行\n',
            '更新合同的手续了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1138')

    def _loc_10BF(): pass

    label('loc_10BF')

    ChrTalk(
        0x00FE,
        (
            '半年前开始\n',
            '就有人借了\n',
            '里头的仓库。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '使用费是预付的\n',
            '倒是没有问题……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不知为何，这数个月间，\n',
            '联络不上啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_1138(): pass

    label('loc_1138')

    Jump('loc_139A')

    def _loc_113B(): pass

    label('loc_113B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_11AB',
    )

    ChrTalk(
        0x00FE,
        (
            '……已经完全到傍晚了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '埋头工作总让人感觉\n',
            '时间过得真快啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我就这样\n',
            '慢慢老了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_139A')

    def _loc_11AB(): pass

    label('loc_11AB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_12C4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_120C',
    )

    ChrTalk(
        0x00FE,
        (
            '仓库空着\n',
            '就只是浪费维修费而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以大家商量着\n',
            '开始了借出仓库的业务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12C1')

    def _loc_120C(): pass

    label('loc_120C')

    ChrTalk(
        0x00FE,
        (
            '最近物资的搬运\n',
            '也用飞船进行了,\n',
            '空空的仓库很受欢迎啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '仓库空着\n',
            '就只是浪费维修费而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以大家商量着\n',
            '开始了借出仓库的业务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不用说普通人，连王国军\n',
            '也来借了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_12C1(): pass

    label('loc_12C1')

    Jump('loc_139A')

    def _loc_12C4(): pass

    label('loc_12C4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_139A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_131B',
    )

    ChrTalk(
        0x00FE,
        (
            '港口营运重开之后\n',
            '那个忙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真正安定下来，\n',
            '还是这几天以后。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_139A')

    def _loc_131B(): pass

    label('loc_131B')

    ChrTalk(
        0x00FE,
        (
            '政变的时候，这个港口\n',
            '被情报部封锁了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '结果为了卸货\n',
            '进港的船\n',
            '要在湖上等好几天……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '港口营运重开之后\n',
            '那个忙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_139A(): pass

    label('loc_139A')

    TalkEnd(0x0009)

    Return()

# id: 0x0006 offset: 0x139E
@scena.Code('func_06_139E')
def func_06_139E():
    TalkBegin(0x000A)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_143E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_143B',
    )

    ChrTalk(
        0x00FE,
        (
            '港口跃出的黑色巨人，\n',
            '出现在柏斯的古代龙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算再出来什么\n',
            '我都不会再惊讶了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '什么啊，那是……\n',
            '出来那么奇怪的东西啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_143B(): pass

    label('loc_143B')

    Jump('loc_1895')

    def _loc_143E(): pass

    label('loc_143E')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1895',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1536',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_14B1',
    )

    ChrTalk(
        0x00FE,
        (
            '那天夜晚，港口飞起的\n',
            '巨大黑影我确实看到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像是人的样子，\n',
            '到底那是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1533')

    def _loc_14B1(): pass

    label('loc_14B1')

    ChrTalk(
        0x00FE,
        (
            '那天夜晚，港口飞起的\n',
            '巨大黑影我确实看到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像是人的样子，\n',
            '到底那是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还以为是看错了，\n',
            '但军队也骚动不断。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_1533(): pass

    label('loc_1533')

    Jump('loc_1895')

    def _loc_1536(): pass

    label('loc_1536')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_1655',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_15A6',
    )

    ChrTalk(
        0x00FE,
        (
            '因为晕船\n',
            '有些人说不喜欢船……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要我说的话，\n',
            '不知何时会落下的\n',
            '浮在空中的东西更加讨厌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1652')

    def _loc_15A6(): pass

    label('loc_15A6')

    ChrTalk(
        0x00FE,
        (
            '因为晕船\n',
            '有些人说不喜欢船……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要我说的话，\n',
            '不知何时会落下的\n',
            '浮在空中的东西更加讨厌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '船又不会坠落\n',
            '比飞船安全多了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……嗯，虽然也有\n',
            '沉没的可能性。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_1652(): pass

    label('loc_1652')

    Jump('loc_1895')

    def _loc_1655(): pass

    label('loc_1655')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_172F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_16BF',
    )

    ChrTalk(
        0x00FE,
        (
            '要说船和飞船，\n',
            '我还是会毫不犹豫地选船。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要问为什么，我是属于大海的男人嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_172C')

    def _loc_16BF(): pass

    label('loc_16BF')

    ChrTalk(
        0x00FE,
        (
            '浮在夕照海面的船……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还有那前面\n',
            '毅然伫立的我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎样，属于大海的男人\n',
            '那种哀愁感受得到吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_172C(): pass

    label('loc_172C')

    Jump('loc_1895')

    def _loc_172F(): pass

    label('loc_172F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_1845',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_17AB',
    )

    ChrTalk(
        0x00FE,
        (
            '飞船确实很便利，\n',
            '不过以现在的性能\n',
            '能堆积的货物也很有限。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是大型货物的搬运\n',
            '现在船也是很重要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1842')

    def _loc_17AB(): pass

    label('loc_17AB')

    ChrTalk(
        0x00FE,
        (
            '船的优点怎么说\n',
            '都是货物的装载量嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '飞船确实很便利，\n',
            '不过以现在的性能\n',
            '能堆积的货物也很有限。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是大型货物的搬运\n',
            '现在船也是很重要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_1842(): pass

    label('loc_1842')

    Jump('loc_1895')

    def _loc_1845(): pass

    label('loc_1845')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_1895',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯～还是船好～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在大海上驰骋的浪漫\n',
            '只有属于海的男人才能品味啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1895(): pass

    label('loc_1895')

    TalkEnd(0x000A)

    Return()

# id: 0x0007 offset: 0x1899
@scena.Code('func_07_1899')
def func_07_1899():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_18FA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_18F7',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯啊？　对了，你们也是\n',
            '来参观那个的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '去到码头\n',
            '就能看到啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18F7(): pass

    label('loc_18F7')

    Jump('loc_1A22')

    def _loc_18FA(): pass

    label('loc_18FA')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A22',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1910',
    )

    Jump('loc_1A22')

    def _loc_1910(): pass

    label('loc_1910')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_195B',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯啊？　白衣服的女孩子？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不，那样的孩子\n',
            '没来过这里哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A22')

    def _loc_195B(): pass

    label('loc_195B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_19B9',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯啊？　这种时候\n',
            '到底怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '差不多工作也快结束了。\n',
            '赶快回家回家！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A22')

    def _loc_19B9(): pass

    label('loc_19B9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_19DE',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯……\n',
            '今天真是累啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A22')

    def _loc_19DE(): pass

    label('loc_19DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_1A22',
    )

    ChrTalk(
        0x00FE,
        (
            '啊？有事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是出租仓库的合同\n',
            '得先通过事务所哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A22(): pass

    label('loc_1A22')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x1A26
@scena.Code('func_08_1A26')
def func_08_1A26():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A8D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1A8A',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，到底怎么回事。\n',
            '那是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '反正也不能工作，\n',
            '就在这里平静一下心情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A8A(): pass

    label('loc_1A8A')

    Jump('loc_1C58')

    def _loc_1A8D(): pass

    label('loc_1A8D')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1C58',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1AA3',
    )

    Jump('loc_1C58')

    def _loc_1AA3(): pass

    label('loc_1AA3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_1ACD',
    )

    ChrTalk(
        0x00FE,
        (
            '好，差不多该回去工作了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C58')

    def _loc_1ACD(): pass

    label('loc_1ACD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1B0C',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，出汗了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真想就这样\n',
            '跳进湖里啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C58')

    def _loc_1B0C(): pass

    label('loc_1B0C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_1B57',
    )

    ChrTalk(
        0x00FE,
        (
            '不开心的时候\n',
            '来到这里就镇定了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你也有这样的地方吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C58')

    def _loc_1B57(): pass

    label('loc_1B57')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_1C58',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1BA7',
    )

    ChrTalk(
        0x00FE,
        (
            '不、不是偷懒哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是为了防范可疑的人\n',
            '而在、在巡逻啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C58')

    def _loc_1BA7(): pass

    label('loc_1BA7')

    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x00FE, 0x0000, 300)
    ChrJumpToRelative(0x00FE, 0, 0, 0, 600, 5000)
    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x00FE,
        (
            '你、你们，是什么人！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不、不是偷懒哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是为了防范可疑的人\n',
            '而在、在巡逻啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x00FE, 0x0010)
    ChrSetDirection(0x00FE, 180, 0)
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_1C58(): pass

    label('loc_1C58')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x1C5C
@scena.Code('func_09_1C5C')
def func_09_1C5C():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1CC3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1CC0',
    )

    ChrTalk(
        0x00FE,
        (
            '港口营运终于上了轨道\n',
            '却在这时出这麻烦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '空之女神\n',
            '弃我们不顾了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1CC0(): pass

    label('loc_1CC0')

    Jump('loc_1DC3')

    def _loc_1CC3(): pass

    label('loc_1CC3')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1DC3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1CD9',
    )

    Jump('loc_1DC3')

    def _loc_1CD9(): pass

    label('loc_1CD9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_1CFF',
    )

    ChrTalk(
        0x00FE,
        (
            '今天的便当吃什么呢～⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DC3')

    def _loc_1CFF(): pass

    label('loc_1CFF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1D34',
    )

    ChrTalk(
        0x00FE,
        (
            '好，还有一点\n',
            '今天的工作也完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DC3')

    def _loc_1D34(): pass

    label('loc_1D34')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_1D75',
    )

    ChrTalk(
        0x00FE,
        (
            '呜呜……肚子好涨………\n',
            '中午的便当吃１个就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DC3')

    def _loc_1D75(): pass

    label('loc_1D75')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_1DC3',
    )

    ChrTalk(
        0x00FE,
        (
            '难道是来港口参观的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到处转转看看是可以，\n',
            '可别妨碍工作哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1DC3(): pass

    label('loc_1DC3')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x1DC7
@scena.Code('func_0A_1DC7')
def func_0A_1DC7():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1E25',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1E22',
    )

    ChrTalk(
        0x00FE,
        (
            '搬运车也不能用，\n',
            '重要的船也动不了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到底我们做错了什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E22(): pass

    label('loc_1E22')

    Jump('loc_1F26')

    def _loc_1E25(): pass

    label('loc_1E25')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1F26',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1E3B',
    )

    Jump('loc_1F26')

    def _loc_1E3B(): pass

    label('loc_1E3B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_1E78',
    )

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，今天也是个令人陶醉\n',
            '适合工作的好天气啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F26')

    def _loc_1E78(): pass

    label('loc_1E78')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1EA4',
    )

    ChrTalk(
        0x00FE,
        (
            '呼～今天也出了一身汗啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F26')

    def _loc_1EA4(): pass

    label('loc_1EA4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_1EF0',
    )

    ChrTalk(
        0x00FE,
        (
            '我们的工作\n',
            '全年都得站着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没有结实的腰腿\n',
            '可没法胜任哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F26')

    def _loc_1EF0(): pass

    label('loc_1EF0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_1F26',
    )

    ChrTalk(
        0x00FE,
        (
            '竟然来到这么深处的地方。\n',
            '来看我们工作吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F26(): pass

    label('loc_1F26')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x1F2A
@scena.Code('func_0B_1F2A')
def func_0B_1F2A():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1F67',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1F64',
    )

    ChrTalk(
        0x00FE,
        (
            '这个状况要持续到什么时候啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F64(): pass

    label('loc_1F64')

    Jump('loc_206E')

    def _loc_1F67(): pass

    label('loc_1F67')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_206E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1F7D',
    )

    Jump('loc_206E')

    def _loc_1F7D(): pass

    label('loc_1F7D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_1FA8',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯～湖上\n',
            '吹来好凉爽的风啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_206E')

    def _loc_1FA8(): pass

    label('loc_1FA8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1FDB',
    )

    ChrTalk(
        0x00FE,
        (
            '真想向着那夕阳\n',
            '让船飞驰而去……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_206E')

    def _loc_1FDB(): pass

    label('loc_1FDB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_202C',
    )

    ChrTalk(
        0x00FE,
        (
            '我可喜欢这个工作岗位了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为全年都能\n',
            '看到这个瓦雷利亚湖啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_206E')

    def _loc_202C(): pass

    label('loc_202C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_206E',
    )

    ChrTalk(
        0x00FE,
        (
            '这蓝天多么赏心悦目。\n',
            '今天也能清楚地看到古罗尼峰峦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_206E(): pass

    label('loc_206E')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x2072
@scena.Code('func_0C_2072')
def func_0C_2072():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_20C4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_20C1',
    )

    ChrTalk(
        0x00FE,
        (
            '没想到导力器\n',
            '都动不了了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……唉，真担心未来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_20C1(): pass

    label('loc_20C1')

    Jump('loc_21DB')

    def _loc_20C4(): pass

    label('loc_20C4')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_21DB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_20DA',
    )

    Jump('loc_21DB')

    def _loc_20DA(): pass

    label('loc_20DA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_2109',
    )

    ChrTalk(
        0x00FE,
        (
            '哈哈哈，今天\n',
            '船的情形也非常好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21DB')

    def _loc_2109(): pass

    label('loc_2109')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_214C',
    )

    ChrTalk(
        0x00FE,
        (
            '黄昏之时真不可思议……\n',
            '不知为何心情会变得难过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21DB')

    def _loc_214C(): pass

    label('loc_214C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_219D',
    )

    ChrTalk(
        0x00FE,
        (
            '这艘船何时都非常精神哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为是我倾注深情\n',
            '整备出来的东西嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21DB')

    def _loc_219D(): pass

    label('loc_219D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_21DB',
    )

    ChrTalk(
        0x00FE,
        (
            '是来参观导力船的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，好啊。\n',
            '尽情地看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_21DB(): pass

    label('loc_21DB')

    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x21DF
@scena.Code('func_0D_21DF')
def func_0D_21DF():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_220F',
    )

    ChrTalk(
        0x00FE,
        (
            '唔唔，越看越觉得\n',
            '不可思议啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2227')

    def _loc_220F(): pass

    label('loc_220F')

    ChrTalk(
        0x00FE,
        (
            '哦哦，好多货物啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2227(): pass

    label('loc_2227')

    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x222B
@scena.Code('func_0E_222B')
def func_0E_222B():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_227D',
    )

    ChrTalk(
        0x00FE,
        (
            '想想真是不可思议啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '导力又不能使用\n',
            '那个到底怎么浮起来？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_22B2')

    def _loc_227D(): pass

    label('loc_227D')

    ChrTalk(
        0x00FE,
        (
            '导力船也相当有震撼力呢。\n',
            '要是带了照相机就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_22B2(): pass

    label('loc_22B2')

    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x22B6
@scena.Code('func_0F_22B6')
def func_0F_22B6():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2345',
    )

    ChrTalk(
        0x00FE,
        (
            '我活了这么久，\n',
            '看过各种各样的东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那样不可思议的东西\n',
            '还是第一次见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '由于那个而\n',
            '不能使用导力器\n',
            '的传闻是真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_236A')

    def _loc_2345(): pass

    label('loc_2345')

    ChrTalk(
        0x00FE,
        (
            '哎呀，王都的美丽\n',
            '可喻为珍珠呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_236A(): pass

    label('loc_236A')

    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x236E
@scena.Code('func_10_236E')
def func_10_236E():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_23FA',
    )

    ChrTalk(
        0x00FE,
        (
            '那个物体出现之后\n',
            '导力器就一齐停了哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '亲卫队不能用『埃尔赛尤』\n',
            '把它击落吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔，『埃尔赛尤』\n',
            '一定也动不了了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2421')

    def _loc_23FA(): pass

    label('loc_23FA')

    ChrTalk(
        0x00FE,
        (
            '哦……确实是\n',
            '气氛不错的仓库街呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2421(): pass

    label('loc_2421')

    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0x2425
@scena.Code('func_11_2425')
def func_11_2425():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_247B',
    )

    ChrTalk(
        0x00FE,
        (
            '我，我什么都看不见！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那样奇怪又令人毛骨悚然\n',
            '的东西我才不相信！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2579')

    def _loc_247B(): pass

    label('loc_247B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_2485',
    )

    Jump('loc_2579')

    def _loc_2485(): pass

    label('loc_2485')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_24E1',
    )

    ChrTalk(
        0x00FE,
        (
            '哦哦，那对亲子\n',
            '不觉得是很棒的画面吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不知道为什么，\n',
            '都快流眼泪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2579')

    def _loc_24E1(): pass

    label('loc_24E1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_253A',
    )

    ChrTalk(
        0x00FE,
        (
            '只是这样待在这里\n',
            '就能感觉到成为属于海的男人的心情哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎样，有效吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2579')

    def _loc_253A(): pass

    label('loc_253A')

    ChrTalk(
        0x00FE,
        (
            '港口气氛真好啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果要向她告白\n',
            '真希望能在这种地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2579(): pass

    label('loc_2579')

    TalkEnd(0x00FE)

    Return()

# id: 0x0012 offset: 0x257D
@scena.Code('func_12_257D')
def func_12_257D():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_25A7',
    )

    ChrTalk(
        0x00FE,
        (
            '今天更加\n',
            '看得清楚了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2631')

    def _loc_25A7(): pass

    label('loc_25A7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_25B1',
    )

    Jump('loc_2631')

    def _loc_25B1(): pass

    label('loc_25B1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_25DB',
    )

    ChrTalk(
        0x00FE,
        (
            '哇啊，好漂亮的景色啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2631')

    def _loc_25DB(): pass

    label('loc_25DB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_2612',
    )

    ChrTalk(
        0x00FE,
        (
            '飞船也不错，\n',
            '但船也相当令人心情舒畅呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2631')

    def _loc_2612(): pass

    label('loc_2612')

    ChrTalk(
        0x00FE,
        (
            '船上能装\n',
            '这么多货物啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2631(): pass

    label('loc_2631')

    TalkEnd(0x00FE)

    Return()

# id: 0x0013 offset: 0x2635
@scena.Code('func_13_2635')
def func_13_2635():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2676',
    )

    ChrTalk(
        0x00FE,
        (
            '别、别说这么可怕的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你、你说谁在乘！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2722')

    def _loc_2676(): pass

    label('loc_2676')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_2680',
    )

    Jump('loc_2722')

    def _loc_2680(): pass

    label('loc_2680')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_26AC',
    )

    ChrTalk(
        0x00FE,
        (
            '嗬，这真是漂亮的晚霞啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2722')

    def _loc_26AC(): pass

    label('loc_26AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_26E9',
    )

    ChrTalk(
        0x00FE,
        (
            '话说回来拂过瓦雷利亚湖\n',
            '的风真令人心情舒畅啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2722')

    def _loc_26E9(): pass

    label('loc_26E9')

    ChrTalk(
        0x00FE,
        (
            '嗬，导力船吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是惭愧，\n',
            '我还是第一次看到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2722(): pass

    label('loc_2722')

    TalkEnd(0x00FE)

    Return()

# id: 0x0014 offset: 0x2726
@scena.Code('func_14_2726')
def func_14_2726():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_274E',
    )

    ChrTalk(
        0x00FE,
        (
            '那里面\n',
            '是谁在乘坐呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2896')

    def _loc_274E(): pass

    label('loc_274E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_2758',
    )

    Jump('loc_2896')

    def _loc_2758(): pass

    label('loc_2758')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2796',
    )

    ChrTalk(
        0x00FE,
        (
            '啊啊，总算碰到你了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '再也不分开了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2896')

    def _loc_2796(): pass

    label('loc_2796')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_27F7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_27C8',
    )

    ChrTalk(
        0x00FE,
        (
            '为什么港口会有\n',
            '这种装置……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27F4')

    def _loc_27C8(): pass

    label('loc_27C8')

    ChrTalk(
        0x00FE,
        (
            '我现在就去那边\n',
            '待在那里别动──哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    def _loc_27F4(): pass

    label('loc_27F4')

    Jump('loc_2896')

    def _loc_27F7(): pass

    label('loc_27F7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_2819',
    )

    ChrTalk(
        0x00FE,
        (
            '我、我女儿去哪里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2896')

    def _loc_2819(): pass

    label('loc_2819')

    ChrTalk(
        0x00FE,
        (
            '这个砖瓦仓库\n',
            '气氛真好啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '哎呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '我、我女儿去哪里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    def _loc_2896(): pass

    label('loc_2896')

    TalkEnd(0x00FE)

    Return()

# id: 0x0015 offset: 0x289A
@scena.Code('func_15_289A')
def func_15_289A():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_28C2',
    )

    ChrTalk(
        0x00FE,
        (
            '好大的贝壳在飞～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Jump('loc_2930')

    def _loc_28C2(): pass

    label('loc_28C2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_28CC',
    )

    Jump('loc_2930')

    def _loc_28CC(): pass

    label('loc_28CC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_28EE',
    )

    ChrTalk(
        0x00FE,
        (
            '呜哇～妈妈～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2930')

    def _loc_28EE(): pass

    label('loc_28EE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_2916',
    )

    ChrTalk(
        0x00FE,
        (
            '妈妈～！我在这里哦～！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2930')

    def _loc_2916(): pass

    label('loc_2916')

    ChrTalk(
        0x00FE,
        (
            '妈妈～！你在哪里～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2930(): pass

    label('loc_2930')

    TalkEnd(0x00FE)

    Return()

# id: 0x0016 offset: 0x2934
@scena.Code('func_16_2934')
def func_16_2934():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '消息未作成 给根田确认',
            TxtCtl.Enter,
        ),
    )

    TalkEnd(0x00FE)

    Return()

# id: 0x0017 offset: 0x2955
@scena.Code('func_17_2955')
def func_17_2955():
    TalkBegin(0x00FF)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_296C',
    )

    OP_6F(0x0004, 0)
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_29CF')

    def _loc_296C(): pass

    label('loc_296C')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    LoadEffect(0x00, 'map\\\\snddst1.eff')
    PlayEffect(0x00, 0xFF, 0x00FF, 15080, 0, 56290, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0004, 0)
    OP_70(0x0004, 30)
    OP_CA(0x04, 0x01, 0x000001F4)
    OP_73(0x0004)

    def _loc_29CF(): pass

    label('loc_29CF')

    TalkEnd(0x00FF)

    Return()

# id: 0x0018 offset: 0x29D3
@scena.Code('func_18_29D3')
def func_18_29D3():
    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门紧紧地关着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0019 offset: 0x2A1D
@scena.Code('func_19_2A1D')
def func_19_2A1D():
    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0011860001V#1001F这里好像可以钓上什么来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2A55')
    def lambda_2A55():
        CameraMove(3250, 0, 123500, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_2A55)

    @scena.Lambda('lambda_2A6D')
    def lambda_2A6D():
        CameraSetDistance(3200, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_2A6D)

    @scena.Lambda('lambda_2A7D')
    def lambda_2A7D():
        OP_6C(45000, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_2A7D)

    Sleep(1000)

    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '钓鱼吗？',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
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
        32,
        1,
        (
            TXT(0x00, '钓鱼\n'),
            TXT(0x01, '离开\n'),
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
    WaitForThreadExit(0x0000, 0x0001)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B04',
    )

    OP_C0(0x0E, 0x0000002C, 0x00000C6C, 0x00000992, 0x0001DA88, 0x00000000, 0x00000C9E, 0xFFFFF8F8, 0x0001F144)
    OP_0D()
    EventEnd(0x01)

    Jump('loc_2B13')

    def _loc_2B04(): pass

    label('loc_2B04')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2B13',
    )

    EventEnd(0x01)

    def _loc_2B13(): pass

    label('loc_2B13')

    Return()

# id: 0x001A offset: 0x2B14
@scena.Code('func_1A_2B14')
def func_1A_2B14():
    ChrSetDirection(0x0000, 315, 0)
    ChrSetDirection(0x0001, 315, 0)
    ChrSetDirection(0x0002, 315, 0)
    ChrSetDirection(0x0003, 315, 0)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_AD('ED6_DT24/C_VIS183._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(500)

    OP_56(0x03)
    OP_AE(0x000001F4)
    Sleep(500)

    SetScenaFlags(ScenaFlag(0x041D, 2, 0x20EA))
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

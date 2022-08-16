import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T3400_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3400   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3400.x'
    header.mapIndex       = 1
    header.bgm            = 16
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
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT07/CH01350._CH', 'ED6_DT07/CH01350P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01750._CH', 'ED6_DT07/CH01750P._CP'),
    ]

# id: 0x10001 offset: 0xDA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '士兵切斯利',
            x                   = 20790,
            z                   = 11750,
            y                   = 6470,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '黛米',
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
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '士兵儒勒',
            x                   = 10500,
            z                   = 0,
            y                   = -3140,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '士兵埃克托尔',
            x                   = 10500,
            z                   = 0,
            y                   = 3140,
            direction           = 270,
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
            name                = '安敦',
            x                   = 14160,
            z                   = 13400,
            y                   = 1650,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0195,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            name                = '利库斯',
            x                   = 16520,
            z                   = 11750,
            y                   = -540,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            name                = '士兵沃普',
            x                   = 5730,
            z                   = 0,
            y                   = 4940,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0008,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '士兵欧鲁尼斯',
            x                   = 35310,
            z                   = 0,
            y                   = 3610,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            name                = '冈多夫',
            x                   = 40970,
            z                   = 0,
            y                   = 10,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0009,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            name                = '利塔街道方向',
            x                   = -37360,
            z                   = 0,
            y                   = 960,
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
        ScenaNpcData(
            name                = '庭园大道方向',
            x                   = 83520,
            z                   = 0,
            y                   = 630,
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

# id: 0x10002 offset: 0x29A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x29A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -25540,
            y           = -1000,
            z           = -4310,
            range       = -27840,
            dword_10    = 0x00001388,
            dword_14    = 0x00001F90,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000019,
        ),
    )

# id: 0x10004 offset: 0x2BA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 15150,
            triggerZ            = 11750,
            triggerY            = 1650,
            triggerRange        = 400,
            actorX              = 14160,
            actorZ              = 14750,
            actorY              = 1650,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0010,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2DE
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_314',
    )

    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrSetPos(0x0008, 20790, 11750, 6470, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_311',
    )

    ChrClearFlags(0x0013, 0x0080)

    def _loc_311(): pass

    label('loc_311')

    Jump('loc_450')

    def _loc_314(): pass

    label('loc_314')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_347',
    )

    CreateThread(0x0008, 0x00, 0x00, func_07_64E)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, 35300, 0, -3600, 90)
    CreateThread(0x0011, 0x00, 0x00, func_02_517)
    ChrClearFlags(0x0012, 0x0080)

    Jump('loc_450')

    def _loc_347(): pass

    label('loc_347')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_35D',
    )

    ChrClearFlags(0x000E, 0x0080)
    CreateThread(0x0008, 0x00, 0x00, func_07_64E)

    Jump('loc_450')

    def _loc_35D(): pass

    label('loc_35D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_36E',
    )

    CreateThread(0x0008, 0x00, 0x00, func_07_64E)

    Jump('loc_450')

    def _loc_36E(): pass

    label('loc_36E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_37F',
    )

    CreateThread(0x0008, 0x00, 0x00, func_07_64E)

    Jump('loc_450')

    def _loc_37F(): pass

    label('loc_37F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            Expr.Return,
        ),
        'loc_429',
    )

    ChrSetPos(0x0008, 18300, 11750, -10110, 225)
    CreateThread(0x0008, 0x00, 0x00, func_03_5BE)
    ChrSetPos(0x000A, 17700, 11750, 12950, 270)
    ChrClearFlags(0x000A, 0x0080)
    CreateThread(0x000A, 0x00, 0x00, func_04_5E2)
    ChrSetPos(0x000B, 17070, 11750, -190, 270)
    ChrClearFlags(0x000B, 0x0080)
    CreateThread(0x000B, 0x00, 0x00, func_05_606)
    ChrSetPos(0x000C, 29080, 11750, -1550, 90)
    ChrClearFlags(0x000C, 0x0080)
    CreateThread(0x000C, 0x00, 0x00, func_06_62A)
    ChrSetPos(0x000F, 16120, 11750, 5980, 270)
    ChrSetPos(0x0010, 16120, 11750, 4840, 0)
    ChrClearFlags(0x000F, 0x0004)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)

    Jump('loc_450')

    def _loc_429(): pass

    label('loc_429')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_450',
    )

    ChrClearFlags(0x000E, 0x0080)

    ExecExpressionWithValue(
        0x000F,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x10),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)

    def _loc_450(): pass

    label('loc_450')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_45E',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    Event(0, func_16_2527)

    def _loc_45E(): pass

    label('loc_45E')

    Return()

# id: 0x0001 offset: 0x45F
@scena.Code('func_01_45F')
def func_01_45F():
    OP_16(0x02, 4000, -105000, -128000, 2293846)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4A4',
    )

    OP_72(0x0002, 0x0010)
    OP_6F(0x0002, 100)
    OP_72(0x0003, 0x0010)
    OP_6F(0x0003, 100)
    OP_72(0x0004, 0x0010)
    OP_6F(0x0004, 100)

    Jump('loc_4B3')

    def _loc_4A4(): pass

    label('loc_4A4')

    OP_1C(0x02, 0x00, 0x001A)
    OP_1C(0x03, 0x00, 0x001A)
    OP_1C(0x04, 0x00, 0x001A)

    def _loc_4B3(): pass

    label('loc_4B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_4C1',
    )

    OP_64(0x00, 0x0001)

    Jump('loc_4E4')

    def _loc_4C1(): pass

    label('loc_4C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_4CB',
    )

    Jump('loc_4E4')

    def _loc_4CB(): pass

    label('loc_4CB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_4D9',
    )

    OP_64(0x00, 0x0001)

    Jump('loc_4E4')

    def _loc_4D9(): pass

    label('loc_4D9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            Expr.Return,
        ),
        'loc_4E4',
    )

    OP_64(0x00, 0x0001)

    def _loc_4E4(): pass

    label('loc_4E4')

    OP_6F(0x0000, 160)
    OP_6F(0x0001, 160)
    OP_72(0x0000, 0x0010)
    OP_72(0x0001, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 2, 0x1412)),
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_516',
    )

    MapSetFlags(0x02000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x22),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_516(): pass

    label('loc_516')

    Return()

# id: 0x0002 offset: 0x517
@scena.Code('func_02_517')
def func_02_517():
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
        (0x00000000, 'loc_548'),
        (0x00000001, 'loc_554'),
        (0x00000002, 'loc_560'),
        (0x00000003, 'loc_56C'),
        (0x00000004, 'loc_578'),
        (0x00000005, 'loc_584'),
        (0x00000006, 'loc_590'),
        (-1, 'loc_59C'),
    )

    def _loc_548(): pass

    label('loc_548')

    OP_99(0x00FE, 0x00, 0x07, 1450)

    Jump('loc_5A8')

    def _loc_554(): pass

    label('loc_554')

    OP_99(0x00FE, 0x00, 0x07, 1550)

    Jump('loc_5A8')

    def _loc_560(): pass

    label('loc_560')

    OP_99(0x00FE, 0x00, 0x07, 1600)

    Jump('loc_5A8')

    def _loc_56C(): pass

    label('loc_56C')

    OP_99(0x00FE, 0x00, 0x07, 1400)

    Jump('loc_5A8')

    def _loc_578(): pass

    label('loc_578')

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_5A8')

    def _loc_584(): pass

    label('loc_584')

    OP_99(0x00FE, 0x00, 0x07, 1350)

    Jump('loc_5A8')

    def _loc_590(): pass

    label('loc_590')

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_5A8')

    def _loc_59C(): pass

    label('loc_59C')

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_5A8')

    def _loc_5A8(): pass

    label('loc_5A8')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5BD',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_5A8')

    def _loc_5BD(): pass

    label('loc_5BD')

    Return()

# id: 0x0003 offset: 0x5BE
@scena.Code('func_03_5BE')
def func_03_5BE():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5E1',
    )

    OP_8D(0x00FE, 20420, -7160, 16050, -13610, 2000)

    Jump('func_03_5BE')

    def _loc_5E1(): pass

    label('loc_5E1')

    Return()

# id: 0x0004 offset: 0x5E2
@scena.Code('func_04_5E2')
def func_04_5E2():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_605',
    )

    OP_8D(0x00FE, 15300, 14530, 19530, 9890, 2000)

    Jump('func_04_5E2')

    def _loc_605(): pass

    label('loc_605')

    Return()

# id: 0x0005 offset: 0x606
@scena.Code('func_05_606')
def func_05_606():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_629',
    )

    OP_8D(0x00FE, 15160, 2490, 19190, -2240, 2000)

    Jump('func_05_606')

    def _loc_629(): pass

    label('loc_629')

    Return()

# id: 0x0006 offset: 0x62A
@scena.Code('func_06_62A')
def func_06_62A():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_64D',
    )

    OP_8D(0x00FE, 30170, 1730, 27910, -3560, 2000)

    Jump('func_06_62A')

    def _loc_64D(): pass

    label('loc_64D')

    Return()

# id: 0x0007 offset: 0x64E
@scena.Code('func_07_64E')
def func_07_64E():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_671',
    )

    OP_8D(0x00FE, 23750, 7410, 18380, -2820, 2000)

    Jump('func_07_64E')

    def _loc_671(): pass

    label('loc_671')

    Return()

# id: 0x0008 offset: 0x672
@scena.Code('func_08_672')
def func_08_672():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_695',
    )

    OP_8D(0x00FE, 9410, 9240, 790, -7190, 2000)

    Jump('func_08_672')

    def _loc_695(): pass

    label('loc_695')

    Return()

# id: 0x0009 offset: 0x696
@scena.Code('func_09_696')
def func_09_696():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_6B9',
    )

    OP_8D(0x00FE, 38690, -4550, 43980, 4290, 2000)

    Jump('func_09_696')

    def _loc_6B9(): pass

    label('loc_6B9')

    Return()

# id: 0x000A offset: 0x6BA
@scena.Code('func_0A_6BA')
def func_0A_6BA():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_7D3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_780',
    )

    ChrTalk(
        0x00FE,
        (
            '今天浮游岛也\n',
            '悠哉游哉地浮在空中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然那座岛出现之后\n',
            '导力器都停止了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过感觉它\n',
            '自身并不坏。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可能是我胡思乱想……\n',
            '可我能感觉到这东西散发着崇高的气息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_7D0')

    def _loc_780(): pass

    label('loc_780')

    ChrTalk(
        0x00FE,
        (
            '那座浮游岛\n',
            '给人一种神圣的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我觉得它本身应该\n',
            '不是什么不好的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7D0(): pass

    label('loc_7D0')

    Jump('loc_EF0')

    def _loc_7D3(): pass

    label('loc_7D3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_8D7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_886',
    )

    ChrTalk(
        0x00FE,
        (
            '从这里可以模模糊糊地\n',
            '看见那座浮游岛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以我总是趁闲暇时\n',
            '观察着它……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '偶尔能看见岛上面\n',
            '有东西哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看上去像是建筑物，\n',
            '不过到底是什么呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_8D4')

    def _loc_886(): pass

    label('loc_886')

    ChrTalk(
        0x00FE,
        (
            '在那座浮游岛上能\n',
            '看到像建筑物一样的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个\n',
            '不过到底是什么呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8D4(): pass

    label('loc_8D4')

    Jump('loc_EF0')

    def _loc_8D7(): pass

    label('loc_8D7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_945',
    )

    ChrTalk(
        0x00FE,
        (
            '听说在艾尔贝离宫那边\n',
            '也出现了情报部的家伙们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '包括王都的成员一起，\n',
            '好像全员都被抓起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EF0')

    def _loc_945(): pass

    label('loc_945')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Return,
        ),
        'loc_9D8',
    )

    ChrTalk(
        0x00FE,
        (
            '互不侵犯条约缔结后\n',
            '真正的和平能到来就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可现实是什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '比如我实在无法想象\n',
            '帝国和共和国的边境问题\n',
            '能通过谈判解决。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EF0')

    def _loc_9D8(): pass

    label('loc_9D8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_A3C',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，还是警戒和巡逻这样的\n',
            '任务能让人平静下来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算是王国军也\n',
            '没办法防止地震啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EF0')

    def _loc_A3C(): pass

    label('loc_A3C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_AC7',
    )

    ChrTalk(
        0x00FE,
        (
            '现在艾尔贝离宫\n',
            '对普通市民也开放哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然有传言说很快这里\n',
            '就要设置警备本部了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看样子要去离宫游览\n',
            '也只能趁现在了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EF0')

    def _loc_AC7(): pass

    label('loc_AC7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_C15',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_B4D',
    )

    ChrTalk(
        0x00FE,
        (
            '希德中校给人的\n',
            '印象更像是文官，\n',
            '不过实际上战斗力也十分了得哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '特别是在魔法方面\n',
            '可是王国军中少数精锐之一。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C12')

    def _loc_B4D(): pass

    label('loc_B4D')

    ChrTalk(
        0x00FE,
        (
            '对签字仪式进行警戒的\n',
            '好像是雷斯顿要塞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且又是希德中校指挥，\n',
            '可以说是万无一失了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '印象更像是文官，\n',
            '中校的战斗力也十分了得哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '特别是在魔法方面\n',
            '可是王国军中少数精锐之一。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_C12(): pass

    label('loc_C12')

    Jump('loc_EF0')

    def _loc_C15(): pass

    label('loc_C15')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_D2E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_CA3',
    )

    ChrTalk(
        0x00FE,
        (
            '塔顶开始闪光是在\n',
            '诞辰庆典之后的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不知何时起开始向天\n',
            '升起柱子一样的光线来了',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '后来就一直能看到\n',
            '塔顶上有光亮。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D2B')

    def _loc_CA3(): pass

    label('loc_CA3')

    ChrTalk(
        0x00FE,
        (
            '从这里能看到托兰特\n',
            '平原的『红莲之塔』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近一直能看到\n',
            '塔顶有光亮。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我向队长也报告过了，\n',
            '不过还是很在意那是什么光。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_D2B(): pass

    label('loc_D2B')

    Jump('loc_EF0')

    def _loc_D2E(): pass

    label('loc_D2E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_D92',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，真没办法……\n',
            '好不容易搞定了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然地震很罕见，\n',
            '不过还是希望不要有第二次了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EF0')

    def _loc_D92(): pass

    label('loc_D92')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 5, 0x1415)),
            Expr.Return,
        ),
        'loc_DEA',
    )

    ChrTalk(
        0x00FE,
        (
            '叫黛米的女孩子\n',
            '听说见过那个怪家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '她在食堂工作，\n',
            '要不你们去问问？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EF0')

    def _loc_DEA(): pass

    label('loc_DEA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            Expr.Return,
        ),
        'loc_E2D',
    )

    ChrTalk(
        0x00FE,
        (
            '你们看看这副样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望能在晚饭之前\n',
            '整理好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EF0')

    def _loc_E2D(): pass

    label('loc_E2D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_EF0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_E7D',
    )

    ChrTalk(
        0x0008,
        (
            '爬城墙可是很危险的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '得好好提醒一下\n',
            '那个年轻人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EF0')

    def _loc_E7D(): pass

    label('loc_E7D')

    ChrTalk(
        0x0008,
        (
            '爬城墙可不正常。\n',
            '真是的，要是掉下来怎么办。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '咦！？　难、难道说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '你、你没在想什么\n',
            '搞怪的事吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_EF0(): pass

    label('loc_EF0')

    TalkEnd(0x0008)

    Return()

# id: 0x000B offset: 0xEF4
@scena.Code('func_0B_EF4')
def func_0B_EF4():
    TalkBegin(0x000A)

    ChrTalk(
        0x000A,
        (
            '◆没有台词。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000A)

    Return()

# id: 0x000C offset: 0xF0D
@scena.Code('func_0C_F0D')
def func_0C_F0D():
    TalkBegin(0x000B)

    ChrTalk(
        0x000B,
        (
            '◆没有台词。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000B)

    Return()

# id: 0x000D offset: 0xF26
@scena.Code('func_0D_F26')
def func_0D_F26():
    TalkBegin(0x000C)

    ChrTalk(
        0x000C,
        (
            '◆没有台词。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000C)

    Return()

# id: 0x000E offset: 0xF3F
@scena.Code('func_0E_F3F')
def func_0E_F3F():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_1057',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1000',
    )

    ChrTalk(
        0x00FE,
        (
            '飞船要是不能飞了\n',
            '我们的责任就更大了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '航空路线既然已经断绝，\n',
            '能侵入王都的就只有东西两侧的哨所了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就是说，只要我们的警戒万无一失，\n',
            '就能够保证王都的安全。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_1054')

    def _loc_1000(): pass

    label('loc_1000')

    ChrTalk(
        0x00FE,
        (
            '大门倒是个问题，\n',
            '不过说了也没用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '问题是在这种状况下\n',
            '如何对哨所进行警戒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1054(): pass

    label('loc_1054')

    Jump('loc_136E')

    def _loc_1057(): pass

    label('loc_1057')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1132',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_10E5',
    )

    ChrTalk(
        0x00FE,
        (
            '呀，欢迎来到\n',
            '圣海姆门……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……虽然想这么说，\n',
            '不过现在不是说这种话的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哨所里的人现在也\n',
            '都如坐针毡呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_112F')

    def _loc_10E5(): pass

    label('loc_10E5')

    ChrTalk(
        0x00FE,
        (
            '本来是想欢迎你们的，\n',
            '不过现在情况特殊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '旅游的话\n',
            '请以后再来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_112F(): pass

    label('loc_112F')

    Jump('loc_136E')

    def _loc_1132(): pass

    label('loc_1132')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_1167',
    )

    ChrTalk(
        0x00FE,
        (
            '欢迎来到圣海姆门。\n',
            '有事的话请进来说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_136E')

    def _loc_1167(): pass

    label('loc_1167')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_1214',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_11B3',
    )

    ChrTalk(
        0x00FE,
        (
            '埃克托尔去帮忙以后\n',
            '就没回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是不是先吃饭了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1211')

    def _loc_11B3(): pass

    label('loc_11B3')

    ChrTalk(
        0x00FE,
        (
            '地震的善后\n',
            '总算是结束了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过埃克托尔那家伙还没回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是不是先吃饭了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_1211(): pass

    label('loc_1211')

    Jump('loc_136E')

    def _loc_1214(): pass

    label('loc_1214')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            Expr.Return,
        ),
        'loc_12AC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_126F',
    )

    ChrTalk(
        0x00FE,
        (
            '门内的大家\n',
            '都在努力收拾残局。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我的搭档埃克托尔\n',
            '也急忙去帮忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12A9')

    def _loc_126F(): pass

    label('loc_126F')

    ChrTalk(
        0x00FE,
        (
            '刚才摇得挺厉害。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好久没像这样\n',
            '感觉到危险了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_12A9(): pass

    label('loc_12A9')

    Jump('loc_136E')

    def _loc_12AC(): pass

    label('loc_12AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_136E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_12E8',
    )

    ChrTalk(
        0x000D,
        (
            '欢迎来到圣海姆门！\n',
            '也欢迎你们来旅游。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_136E')

    def _loc_12E8(): pass

    label('loc_12E8')

    ChrTalk(
        0x000D,
        (
            '欢迎来到圣海姆门！\n',
            '也欢迎你们来旅游。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '这里是名叫『亚宁堡』的\n',
            '古代长城的一部分。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '作为旅游名胜，\n',
            '来参观的人也很多哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_136E(): pass

    label('loc_136E')

    TalkEnd(0x000D)

    Return()

# id: 0x000F offset: 0x1372
@scena.Code('func_0F_1372')
def func_0F_1372():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_145A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1409',
    )

    ChrTalk(
        0x00FE,
        (
            '就因为导力枪不能使用\n',
            '而发牢骚的那些人真没用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '反正一进入混战，\n',
            '枪就没用了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '既然如此，\n',
            '一开始就用刺刀作战好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_1457')

    def _loc_1409(): pass

    label('loc_1409')

    ChrTalk(
        0x00FE,
        (
            '我从以前起\n',
            '就更喜欢剑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为用那个才能感觉到\n',
            '是凭自己的力量在战斗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1457(): pass

    label('loc_1457')

    Jump('loc_1669')

    def _loc_145A(): pass

    label('loc_145A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1547',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_14F6',
    )

    ChrTalk(
        0x00FE,
        (
            '导力式的门\n',
            '怎么也放不下来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为这里是王都防卫的中枢，\n',
            '所以这个问题挺严重的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过就算有人入侵\n',
            '我们也会把他们挡下的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_1544')

    def _loc_14F6(): pass

    label('loc_14F6')

    ChrTalk(
        0x00FE,
        (
            '门关不起来这种事\n',
            '可是闻所未闻啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过即便如此，\n',
            '这里还是要死守的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1544(): pass

    label('loc_1544')

    Jump('loc_1669')

    def _loc_1547(): pass

    label('loc_1547')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_15EC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_15A8',
    )

    ChrTalk(
        0x00FE,
        (
            '说起来很快就有\n',
            '条约的签字仪式了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，队长又要在那儿\n',
            '嚷嚷强化警戒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15E9')

    def _loc_15A8(): pass

    label('loc_15A8')

    ChrTalk(
        0x00FE,
        (
            '地震好像也\n',
            '平息下来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '旅客和我们都总算\n',
            '能放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_15E9(): pass

    label('loc_15E9')

    Jump('loc_1669')

    def _loc_15EC(): pass

    label('loc_15EC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_1669',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_162B',
    )

    ChrTalk(
        0x000E,
        (
            '没事情也没关系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '你们可以随意出入。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1669')

    def _loc_162B(): pass

    label('loc_162B')

    ChrTalk(
        0x000E,
        (
            '哟，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '如果有什么事情\n',
            '就和里面的队长说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_1669(): pass

    label('loc_1669')

    TalkEnd(0x000E)

    Return()

# id: 0x0010 offset: 0x166D
@scena.Code('func_10_166D')
def func_10_166D():
    Call(0, 0x0011)

    Return()

# id: 0x0011 offset: 0x1672
@scena.Code('func_11_1672')
def func_11_1672():
    UnlockAchievement(0x01, 0x000A, 0x00)
    TalkSetChrName('安敦')
    TalkBegin(0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            Expr.Return,
        ),
        'loc_1700',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_16C0',
    )

    ChrTalk(
        0x00FE,
        (
            '差、差点就\n',
            '掉下去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊～真吓人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16FD')

    def _loc_16C0(): pass

    label('loc_16C0')

    ChrTalk(
        0x00FE,
        (
            '呼～呼……\n',
            '啊～真吓人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '差、差点就\n',
            '掉下去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_16FD(): pass

    label('loc_16FD')

    Jump('loc_1819')

    def _loc_1700(): pass

    label('loc_1700')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_1819',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1778',
    )

    ChrSetSubChip(0x000F, 0)

    @scena.Lambda('lambda_1719')
    def lambda_1719():
        OP_9E(0x000F, 15, 0, 300, 4000)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_1719)

    ChrTalk(
        0x000F,
        (
            '#3S再见了──！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1748')
    def lambda_1748():
        OP_9E(0x000F, 15, 0, 300, 4000)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_1748)

    ChrTalk(
        0x000F,
        (
            '#3S我的青春──！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1819')

    def _loc_1778(): pass

    label('loc_1778')

    ChrSetSubChip(0x000F, 0)

    @scena.Lambda('lambda_1783')
    def lambda_1783():
        OP_9E(0x000F, 15, 0, 300, 4000)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_1783)

    ChrTalk(
        0x000F,
        (
            '#3S诞辰庆典──！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_17B4')
    def lambda_17B4():
        OP_9E(0x000F, 15, 0, 300, 4000)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_17B4)

    ChrTalk(
        0x000F,
        (
            '#3S我最讨厌了───！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_17EB')
    def lambda_17EB():
        OP_9E(0x000F, 15, 0, 300, 4000)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_17EB)

    ChrTalk(
        0x000F,
        (
            '#3S啊啊啊──！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_1819(): pass

    label('loc_1819')

    TalkEnd(0x000F)

    Return()

# id: 0x0012 offset: 0x181D
@scena.Code('func_12_181D')
def func_12_181D():
    TalkSetChrName('利库斯')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1834',
    )

    ChrClearFlags(0x0010, 0x0010)

    Jump('loc_1839')

    def _loc_1834(): pass

    label('loc_1834')

    ChrSetFlags(0x0010, 0x0010)

    def _loc_1839(): pass

    label('loc_1839')

    TalkBegin(0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            Expr.Return,
        ),
        'loc_1903',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1897',
    )

    ChrTalk(
        0x00FE,
        (
            '这家伙地震的时候\n',
            '正好在爬城墙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '被震感吓着了，\n',
            '差点就掉下去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1900')

    def _loc_1897(): pass

    label('loc_1897')

    ChrTalk(
        0x00FE,
        (
            '如果地震再稍微大一点，\n',
            '说不定真的就掉下去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从这一点上来说，安敦，\n',
            '可以说你算是走运的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_1900(): pass

    label('loc_1900')

    Jump('loc_1A02')

    def _loc_1903(): pass

    label('loc_1903')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_1A02',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_19AF',
    )

    ChrTalk(
        0x0010,
        (
            '我的搭档安敦在诞辰庆典的时候\n',
            '向仰慕的女性告白了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '不过残酷的现实是他被\n',
            '彻底地拒绝了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '再次来到这里也算\n',
            '他好像为了断却这个念想就去爬城墙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A02')

    def _loc_19AF(): pass

    label('loc_19AF')

    ChrTalk(
        0x0010,
        (
            '安敦…\n',
            '那边是蔡斯的方向啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '如果你恨诞辰庆典的话\n',
            '至少要面向王都吼吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_1A02(): pass

    label('loc_1A02')

    TalkEnd(0x0010)

    Return()

# id: 0x0013 offset: 0x1A06
@scena.Code('func_13_1A06')
def func_13_1A06():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_1AF1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1AB3',
    )

    ChrTalk(
        0x00FE,
        (
            '虽、虽然前辈们\n',
            '都泰然自若……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过我还是感到不安啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为要在不能使用枪的状态下\n',
            '把守这样的平地地形。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '能不能至少\n',
            '安排一点路障啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    Jump('loc_1AEE')

    def _loc_1AB3(): pass

    label('loc_1AB3')

    ChrTalk(
        0x00FE,
        (
            '虽、虽然前辈们\n',
            '都泰然自若……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我感到还是不安啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AEE(): pass

    label('loc_1AEE')

    Jump('loc_1E27')

    def _loc_1AF1(): pass

    label('loc_1AF1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1C18',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1BC6',
    )

    ChrTalk(
        0x00FE,
        (
            '我是王都那边的门卫，\n',
            '不过现在过来这边支援。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是为了强化外侧的\n',
            '蔡斯这边的警戒……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '能和儒勒前辈以及埃克托尔前辈\n',
            '一起站岗真是荣幸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他们两人都是传闻要光荣\n',
            '调往亲卫队的人物哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    Jump('loc_1C15')

    def _loc_1BC6(): pass

    label('loc_1BC6')

    ChrTalk(
        0x00FE,
        (
            '今天我是来支援蔡斯这边的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，能和我崇拜的前辈们\n',
            '一起站岗真是荣幸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C15(): pass

    label('loc_1C15')

    Jump('loc_1E27')

    def _loc_1C18(): pass

    label('loc_1C18')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1CC4',
    )

    ChrTalk(
        0x00FE,
        (
            '王都空中出现会飞的\n',
            '巨大人形兵器是真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果真的有那种东西的话，\n',
            '连哈肯大门和雷斯顿要塞\n',
            '都危险了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '通知里说到的『结社』，\n',
            '到底是些什么人呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E27')

    def _loc_1CC4(): pass

    label('loc_1CC4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Return,
        ),
        'loc_1D3D',
    )

    ChrTalk(
        0x00FE,
        (
            '你们是游击士吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听说这次的警戒工作是由希德中校的\n',
            '部队和游击士协会联合进行的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之请多关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E27')

    def _loc_1D3D(): pass

    label('loc_1D3D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_1DB0',
    )

    ChrTalk(
        0x00FE,
        (
            '这里的迪尔队长的\n',
            '严格是出了名的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然军队本身应该是\n',
            '严格的，不过太顽固的话\n',
            '就让人感到为难了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E27')

    def _loc_1DB0(): pass

    label('loc_1DB0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_1E27',
    )

    ChrTalk(
        0x00FE,
        (
            '诞辰庆典前被配属到这个部队\n',
            '之后已经过了好几个月了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然还有很多问题，\n',
            '不过总算习惯现在的工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E27(): pass

    label('loc_1E27')

    TalkEnd(0x00FE)

    Return()

# id: 0x0014 offset: 0x1E2B
@scena.Code('func_14_1E2B')
def func_14_1E2B():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_1F64',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1F05',
    )

    ChrTalk(
        0x00FE,
        (
            '导力器不能用的话\n',
            '夜晚的警戒还是让人担心啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没有照明的话\n',
            '敌人接近了也注意不到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '蔡斯\n',
            '听说有卖在黑暗中\n',
            '也能看见东西的眼镜的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真希望我们的部队也\n',
            '能讨论是不是能引进这东西呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F61')

    def _loc_1F05(): pass

    label('loc_1F05')

    ChrTalk(
        0x00FE,
        (
            '导力灯也没有，\n',
            '夜晚的警戒还是让人担心啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听说有卖在黑暗中\n',
            '真希望早点装备那个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F61(): pass

    label('loc_1F61')

    Jump('loc_2207')

    def _loc_1F64(): pass

    label('loc_1F64')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2061',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_200E',
    )

    ChrTalk(
        0x00FE,
        (
            '一起做门卫的沃普\n',
            '现在现在去蔡斯那边了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像因为那边是外围，\n',
            '所以要强化警戒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然我觉得这是理所当然的判断，\n',
            '不过我也因此变得寂寞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    Jump('loc_205E')

    def _loc_200E(): pass

    label('loc_200E')

    ChrTalk(
        0x00FE,
        (
            '一个人做门卫\n',
            '已经是很久之前的事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有、有什么事的话\n',
            '得马上去叫增援。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_205E(): pass

    label('loc_205E')

    Jump('loc_2207')

    def _loc_2061(): pass

    label('loc_2061')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_20AF',
    )

    ChrTalk(
        0x00FE,
        (
            '附近可能还潜伏着\n',
            '出现在王都的\n',
            '特务兵的余党。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请充分注意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2207')

    def _loc_20AF(): pass

    label('loc_20AF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Return,
        ),
        'loc_213C',
    )

    ChrTalk(
        0x00FE,
        (
            '从今天开始王都的\n',
            '警戒和巡逻好像开始了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '艾尔贝离宫好像也\n',
            '设置了警备本部……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有一种签字仪式马上\n',
            '就要开始了的紧张感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2207')

    def _loc_213C(): pass

    label('loc_213C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_218D',
    )

    ChrTalk(
        0x00FE,
        (
            '今天天气不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样的日子真想和孩子\n',
            '拿着盒饭去离宫那边游玩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2207')

    def _loc_218D(): pass

    label('loc_218D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_2207',
    )

    ChrTalk(
        0x00FE,
        (
            '蔡斯的地震事件\n',
            '好像好不容易才解决了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '格兰赛尔现在\n',
            '很和平。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '政变以来就\n',
            '就没发生过什么可疑的事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2207(): pass

    label('loc_2207')

    TalkEnd(0x00FE)

    Return()

# id: 0x0015 offset: 0x220B
@scena.Code('func_15_220B')
def func_15_220B():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_2523',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041A, 1, 0x20D1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_240B',
    )

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '哟，艾丝蒂尔你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011F啊，冈多夫先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_22B1',
    )

    ChrTalk(
        0x0106,
        (
            '#050F在巡逻吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0106, 400)

    Jump('loc_230E')

    def _loc_22B1(): pass

    label('loc_22B1')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_22E2',
    )

    ChrTalk(
        0x0103,
        (
            '#020F是在巡逻中吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0103, 400)

    Jump('loc_230E')

    def _loc_22E2(): pass

    label('loc_22E2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_230E',
    )

    ChrTalk(
        0x0107,
        (
            '#064F是在巡逻吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0107, 400)

    def _loc_230E(): pass

    label('loc_230E')

    ChrTalk(
        0x00FE,
        (
            '啊，正是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管怎么说，警戒工作\n',
            '可是不能松懈的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈，你们就集中精力\n',
            '完成自己的任务吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '维持治安之类的事情\n',
            '交给我们就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1002F嗯……明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F……那可太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那么，请当心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '喔，真周到啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))
    SetScenaFlags(ScenaFlag(0x041A, 1, 0x20D1))

    Jump('loc_2523')

    def _loc_240B(): pass

    label('loc_240B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_2471',
    )

    ChrTalk(
        0x00FE,
        (
            '在现在这种形势下，\n',
            '不管再发生什么我也不会惊奇了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我只要做好自己的\n',
            '警戒就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2523')

    def _loc_2471(): pass

    label('loc_2471')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_24DB',
    )

    ChrTalk(
        0x00FE,
        (
            '哟，是你们啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像工作\n',
            '很忙的样子嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之努力是好，\n',
            '可别太埋头于工作中哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    Jump('loc_2523')

    def _loc_24DB(): pass

    label('loc_24DB')

    ChrTalk(
        0x00FE,
        (
            '好像工作\n',
            '很忙的样子嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之努力是好，\n',
            '可别太埋头于工作中哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2523(): pass

    label('loc_2523')

    TalkEnd(0x00FE)

    Return()

# id: 0x0016 offset: 0x2527
@scena.Code('func_16_2527')
def func_16_2527():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2538',
    )

    Call(0, 0x0018)

    def _loc_2538(): pass

    label('loc_2538')

    EventBegin(0x00)
    FadeOut(0, 0, -1)
    PlaySE(198, 0x00, 0x64)
    OP_6F(0x0004, 100)
    OP_72(0x0004, 0x0010)
    ChrSetPos(0x0009, 22890, 7250, -24590, 180)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0101, 23390, 7250, -23090, 180)
    ChrSetPos(0x00F7, 22390, 7250, -23090, 180)
    ChrSetPos(0x0104, 23390, 7250, -22090, 180)
    ChrSetPos(0x0105, 22390, 7250, -22090, 180)
    CameraMove(22650, 7250, -20770, 0)
    OP_67(0, 8020, -10000, 0)
    CameraSetDistance(1910, 0)
    OP_6C(315000, 0)
    OP_6E(427, 0)
    OP_69(0x0101, 0)
    OP_6A(0x0101)
    Sleep(2500)

    @scena.Lambda('lambda_2601')
    def lambda_2601():
        ChrMoveToRelative(0x00FE, 0, 0, -18000, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2601)

    Sleep(80)

    @scena.Lambda('lambda_2621')
    def lambda_2621():
        ChrMoveToRelative(0x00FE, 0, 0, -18000, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2621)

    Sleep(120)

    @scena.Lambda('lambda_2641')
    def lambda_2641():
        ChrMoveToRelative(0x00FE, 0, 0, -18000, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_2641)

    Sleep(80)

    @scena.Lambda('lambda_2661')
    def lambda_2661():
        ChrMoveToRelative(0x00FE, 0, 0, -17500, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_2661)

    Sleep(120)

    @scena.Lambda('lambda_2681')
    def lambda_2681():
        ChrMoveToRelative(0x00FE, 0, 0, -17500, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_2681)

    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x0104, 0x0001)
    OP_6A(0x00FF)
    Fade(1000)
    CameraMove(22860, 7250, -41960, 0)
    OP_67(0, 8020, -10000, 0)
    CameraSetDistance(1910, 0)
    OP_6C(220000, 0)
    OP_6E(427, 0)
    OP_0D()

    ChrTalk(
        0x0009,
        (
            '#3100221158V#5P等我到外面看看的时候\n',
            '他已经不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0009, 0, 400)

    ChrTalk(
        0x0009,
        (
            '#3100221159V#5P就是说，是在\n',
            '这里跟丢的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010221160V#1020F#6P跟、跟丢了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060221161V#043F#4P可这里是死路吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3100221162V#5P嗯，无法想象他能\n',
            '从这么高的地方跳下去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3100221163V#5P大概觉得他朝这边来了\n',
            '是我的错觉吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3100221164V#5P最后，我找了其他的地方\n',
            '也没发现他的踪影。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3100221165V#5P有一点忧郁呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040221166V#035F#6P呵呵，可怜的小猫咪。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040221167V#037F只要你愿意，就让我\n',
            '来帮你忘却那种男人吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010221168V#1019F#5P停！不许浑水摸鱼！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2992',
    )

    ChrTalk(
        0x0106,
        (
            '#0050221169V#053F#2P原来如此……\n',
            '大致情况我们了解了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050221170V#051F谢谢，你可帮了我们大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29FA')

    def _loc_2992(): pass

    label('loc_2992')

    ChrTalk(
        0x0103,
        (
            '#0030221171V#026F#2P原来如此……\n',
            '大致情况我们了解了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030221172V#526F谢谢，你可帮了我们大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_29FA(): pass

    label('loc_29FA')

    ChrSetDirection(0x0101, 180, 400)

    ChrTalk(
        0x0009,
        (
            '#3100221173V#5P呵呵，不用客气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3100221174V#5P不过那个人……\n',
            '果然是个逃犯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3100221175V#5P是个被游击士协会\n',
            '追踪的冷血杀人狂？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010221176V#1016F#6P这、这还不能确定……\n',
            '不过肯定是应该注意的人物。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010221177V#1002F如果你看到他\n',
            '也还是不要靠近的为好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3100221178V#5P嗯～\n',
            '虽然帅，不过也没办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3100221179V#5P我还有工作，就先\n',
            '告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3100221180V#5P加油啊，游击士们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0009, 0x00, 0x00, func_17_304C)

    @scena.Lambda('lambda_2BA3')
    def lambda_2BA3():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_2BA3')

    DispatchAsync2(0x0101, 0x0001, lambda_2BA3)

    @scena.Lambda('lambda_2BB4')
    def lambda_2BB4():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_2BB4')

    DispatchAsync2(0x00F7, 0x0001, lambda_2BB4)

    @scena.Lambda('lambda_2BC5')
    def lambda_2BC5():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_2BC5')

    DispatchAsync2(0x0105, 0x0001, lambda_2BC5)

    @scena.Lambda('lambda_2BD6')
    def lambda_2BD6():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_2BD6')

    DispatchAsync2(0x0104, 0x0001, lambda_2BD6)

    Sleep(1000)

    @scena.Lambda('lambda_2BEC')
    def lambda_2BEC():
        CameraMove(23080, 7250, -38000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2BEC)

    WaitForThreadExit(0x0009, 0x0000)
    ChrSetFlags(0x0009, 0x0080)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x00F7, 0x01)
    TerminateThread(0x0105, 0x01)
    TerminateThread(0x0104, 0x01)
    WaitForThreadExit(0x0101, 0x0003)
    Sleep(500)

    @scena.Lambda('lambda_2C28')
    def lambda_2C28():
        CameraMove(23080, 7250, -40700, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2C28)

    ChrSetDirection(0x0104, 225, 400)
    ChrSetDirection(0x00F7, 45, 400)
    ChrSetDirection(0x0105, 180, 400)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0105,
        (
            '#0060221181V#047F『无法想象他能\n',
            '从这么高的地方跳下去』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060221182V#042F……艾丝蒂尔。\n',
            '你有没有想到什么人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010221183V#1003F#5P嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_AD('ED6_DT24/C_VIS175._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(2000)

    Sleep(1000)

    OP_AE(0x000001F4)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010221184V#1002F#5P从女王宫跳下去的\n',
            '银发男人──洛伦斯少尉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010221185V确实，要是和那家伙水准相当的话\n',
            '从这里跳下去也没问题……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2DF8',
    )

    ChrTalk(
        0x0106,
        (
            '#0050221186V#057F#2P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050221187V这样一来太阳眼镜小子的\n',
            '原形应该可以确定了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E57')

    def _loc_2DF8(): pass

    label('loc_2DF8')

    ChrTalk(
        0x0103,
        (
            '#0030221188V#022F#2P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030221189V这样一来戴太阳眼镜的男人的\n',
            '原形应该可以确定了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2E57(): pass

    label('loc_2E57')

    ChrTalk(
        0x0104,
        (
            '#0040221190V#035F#6P是怪盗之后的第二个『执行者』──',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040221191V#030F可以这么说吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2F1A',
    )

    ChrTalk(
        0x0106,
        (
            '#0050221192V#053F#2P看来没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050221193V#050F这里的调查都结束了。\n',
            '我们回协会报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F78')

    def _loc_2F1A(): pass

    label('loc_2F1A')

    ChrTalk(
        0x0103,
        (
            '#0030221194V#026F#2P看来没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030221195V#020F这里的调查都结束了。\n',
            '我们回协会报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2F78(): pass

    label('loc_2F78')

    OP_20(0x000007D0)
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(23030, 7250, -40170, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3250, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, 23060, 7250, -40220, 16)
    ChrSetPos(0x0001, 23060, 7250, -40220, 16)
    ChrSetPos(0x0002, 23060, 7250, -40220, 16)
    ChrSetPos(0x0003, 23060, 7250, -40220, 16)
    OP_69(0x0000, 0)
    OP_0D()
    OP_6F(0x0004, 0)
    OP_71(0x0004, 0x0010)
    SetScenaFlags(ScenaFlag(0x0282, 6, 0x1416))
    OP_28(0x0086, 0x01, 0x0020)
    OP_28(0x0086, 0x01, 0x0040)
    OP_28(0x0086, 0x01, 0x0080)
    OP_28(0x0086, 0x01, 0x0100)
    Sleep(1000)

    OP_21()
    PlayBGM(16)
    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0017 offset: 0x304C
@scena.Code('func_17_304C')
def func_17_304C():
    @scena.Lambda('lambda_3052')
    def lambda_3052():
        ChrWalkTo(0x00FE, 24400, 7250, -41700, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3052)

    WaitForThreadExit(0x0009, 0x0001)

    @scena.Lambda('lambda_3072')
    def lambda_3072():
        ChrWalkTo(0x00FE, 24300, 7250, -29000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3072)

    WaitForThreadExit(0x0009, 0x0001)

    Return()

# id: 0x0018 offset: 0x308D
@scena.Code('func_18_308D')
def func_18_308D():
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
        (0x00000000, 'loc_3107'),
        (0x00000001, 'loc_310D'),
        (-1, 'loc_3113'),
    )

    def _loc_3107(): pass

    label('loc_3107')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_3113')

    def _loc_310D(): pass

    label('loc_310D')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_3113')

    def _loc_3113(): pass

    label('loc_3113')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_3121',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_3125')

    def _loc_3121(): pass

    label('loc_3121')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_3125(): pass

    label('loc_3125')

    Return()

# id: 0x0019 offset: 0x3126
@scena.Code('func_19_3126')
def func_19_3126():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 3, 0x1413)),
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3298',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3199',
    )

    ChrTalk(
        0x0101,
        (
            '#0010221014V#1002F……这里的调查\n',
            '还没结束。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010221015V我们赶快\n',
            '去打听情况吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_327D')

    def _loc_3199(): pass

    label('loc_3199')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3210',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_31B6',
    )

    ChrTurnDirection(0x0106, 0x0001, 400)

    Jump('loc_31BD')

    def _loc_31B6(): pass

    label('loc_31B6')

    ChrTurnDirection(0x0106, 0x0000, 400)

    def _loc_31BD(): pass

    label('loc_31BD')

    ChrTalk(
        0x0106,
        (
            '#0050221016V#050F这里的调查\n',
            '还没结束。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050221017V我们赶快去打听情况吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_327D')

    def _loc_3210(): pass

    label('loc_3210')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3226',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_322D')

    def _loc_3226(): pass

    label('loc_3226')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_322D(): pass

    label('loc_322D')

    ChrTalk(
        0x0103,
        (
            '#0030221018V#020F这里的调查\n',
            '还没结束。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030221019V我们赶快去打听情况吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_327D(): pass

    label('loc_327D')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_3298(): pass

    label('loc_3298')

    Return()

# id: 0x001A offset: 0x3299
@scena.Code('func_1A_3299')
def func_1A_3299():
    TalkBegin(0x00FF)
    Sleep(400)

    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

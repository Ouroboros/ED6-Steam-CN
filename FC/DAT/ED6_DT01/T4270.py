import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4270_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4270   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4270.x'
    header.mapIndex       = 1
    header.bgm            = 17
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
        ('ED6_DT07/CH02460._CH', 'ED6_DT07/CH02460P._CP'),
        ('ED6_DT07/CH02230._CH', 'ED6_DT07/CH02230P._CP'),
        ('ED6_DT07/CH02240._CH', 'ED6_DT07/CH02240P._CP'),
        ('ED6_DT07/CH00000._CH', 'ED6_DT07/CH00000P._CP'),
        ('ED6_DT07/CH00010._CH', 'ED6_DT07/CH00010P._CP'),
        ('ED6_DT07/CH02010._CH', 'ED6_DT07/CH02010P._CP'),
        ('ED6_DT07/CH02140._CH', 'ED6_DT07/CH02140P._CP'),
        ('ED6_DT07/CH02470._CH', 'ED6_DT07/CH02470P._CP'),
        ('ED6_DT07/CH01330._CH', 'ED6_DT07/CH01330P._CP'),
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00101._CH', 'ED6_DT07/CH00101P._CP'),
        ('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP'),
        ('ED6_DT07/CH00121._CH', 'ED6_DT07/CH00121P._CP'),
        ('ED6_DT07/CH00140._CH', 'ED6_DT07/CH00140P._CP'),
        ('ED6_DT07/CH00141._CH', 'ED6_DT07/CH00141P._CP'),
        ('ED6_DT07/CH02540._CH', 'ED6_DT07/CH02540P._CP'),
        ('ED6_DT07/CH00003._CH', 'ED6_DT07/CH00003P._CP'),
        ('ED6_DT07/CH00013._CH', 'ED6_DT07/CH00013P._CP'),
        ('ED6_DT07/CH02013._CH', 'ED6_DT07/CH02013P._CP'),
        ('ED6_DT06/CH20020._CH', 'ED6_DT06/CH20020P._CP'),
        ('ED6_DT07/CH00043._CH', 'ED6_DT07/CH00043P._CP'),
        ('ED6_DT07/CH02093._CH', 'ED6_DT07/CH02093P._CP'),
        ('ED6_DT07/CH02463._CH', 'ED6_DT07/CH02463P._CP'),
    ]

# id: 0x10001 offset: 0x162
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '艾莉茜雅女王',
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
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '杜南公爵',
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
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '管家菲利普',
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
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '特务兵',
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
            name                = '特务兵',
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
            name                = '特务兵',
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
            name                = '特务兵',
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
            name                = '茜亚',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1638419,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1638419,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1638419,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1638419,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '\u3000',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1703955,
            chipIndex           = 19,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '科洛丝',
            x                   = -103870,
            z                   = 200,
            y                   = 8990,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '尤莉亚中尉',
            x                   = -105240,
            z                   = 200,
            y                   = 7690,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '希尔丹夫人',
            x                   = -106560,
            z                   = 200,
            y                   = 8960,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
    )

# id: 0x10002 offset: 0x362
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x362
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 1980,
            y           = -1000,
            z           = -1550,
            range       = -2230,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFFF056,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000D,
        ),
    )

# id: 0x10004 offset: 0x382
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -1040,
            triggerZ            = 8000,
            triggerY            = 35960,
            triggerRange        = 800,
            actorX              = -1040,
            actorZ              = 9000,
            actorY              = 35960,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
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
        'loc_3B4',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_0A_FB0)

    def _loc_3B4(): pass

    label('loc_3B4')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_3C0'),
        (-1, 'loc_3D6'),
    )

    def _loc_3C0(): pass

    label('loc_3C0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 5, 0x665)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 4, 0x664)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3D3',
    )

    SetScenaFlags(ScenaFlag(0x00CC, 5, 0x665))
    Event(0, func_0C_4E95)

    def _loc_3D3(): pass

    label('loc_3D3')

    Jump('loc_3D6')

    def _loc_3D6(): pass

    label('loc_3D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_419',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 4, 0x644)),
            Expr.Return,
        ),
        'loc_3FB',
    )

    ChrSetChipByIndex(0x0000, 0)
    ChrSetChipByIndex(0x0001, 1)
    ChrSetChipByIndex(0x0138, 2)

    Jump('loc_40A')

    def _loc_3FB(): pass

    label('loc_3FB')

    ChrSetChipByIndex(0x0000, 0)
    ChrSetChipByIndex(0x0001, 3)
    ChrSetChipByIndex(0x0138, 4)

    def _loc_40A(): pass

    label('loc_40A')

    ChrSetFlags(0x0000, 0x1000)
    ChrSetFlags(0x0001, 0x1000)
    ChrSetFlags(0x0138, 0x1000)

    def _loc_419(): pass

    label('loc_419')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_4D6',
    )

    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetChipByIndex(0x0008, 18)
    ChrSetPos(0x0008, -105250, 200, 10500, 180)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrSetPos(0x0011, -104620, 640, 8950, 0)
    ChrSetPos(0x0012, -105280, 640, 8300, 0)
    ChrSetPos(0x0010, -105350, 640, 9620, 0)
    ChrSetPos(0x0013, -105990, 640, 8950, 0)
    ChrSetPos(0x0014, -105280, 700, 9050, 0)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, -107640, 0, 7110, 90)

    Jump('loc_522')

    def _loc_4D6(): pass

    label('loc_4D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_4FD',
    )

    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, -53080, 0, 12340, 3)
    CreateThread(0x000F, 0x00, 0x00, func_02_624)

    Jump('loc_522')

    def _loc_4FD(): pass

    label('loc_4FD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_507',
    )

    Jump('loc_522')

    def _loc_507(): pass

    label('loc_507')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_511',
    )

    Jump('loc_522')

    def _loc_511(): pass

    label('loc_511')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_51B',
    )

    Jump('loc_522')

    def _loc_51B(): pass

    label('loc_51B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_522',
    )

    def _loc_522(): pass

    label('loc_522')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_52C',
    )

    Jump('loc_5B9')

    def _loc_52C(): pass

    label('loc_52C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_562',
    )

    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x0009, -52830, 0, 7650, 179)
    ChrSetPos(0x000A, -53810, 0, 7520, 79)

    Jump('loc_5B9')

    def _loc_562(): pass

    label('loc_562')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_56C',
    )

    Jump('loc_5B9')

    def _loc_56C(): pass

    label('loc_56C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_576',
    )

    Jump('loc_5B9')

    def _loc_576(): pass

    label('loc_576')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_580',
    )

    Jump('loc_5B9')

    def _loc_580(): pass

    label('loc_580')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_58A',
    )

    Jump('loc_5B9')

    def _loc_58A(): pass

    label('loc_58A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_594',
    )

    Jump('loc_5B9')

    def _loc_594(): pass

    label('loc_594')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_59E',
    )

    Jump('loc_5B9')

    def _loc_59E(): pass

    label('loc_59E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_5A8',
    )

    Jump('loc_5B9')

    def _loc_5A8(): pass

    label('loc_5A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_5B2',
    )

    Jump('loc_5B9')

    def _loc_5B2(): pass

    label('loc_5B2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_5B9',
    )

    def _loc_5B9(): pass

    label('loc_5B9')

    Return()

# id: 0x0001 offset: 0x5BA
@scena.Code('func_01_5BA')
def func_01_5BA():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 4, 0x644)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5DE',
    )

    OP_72(0x0022, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 3, 0x643)),
            Expr.Return,
        ),
        'loc_5DB',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_5DB(): pass

    label('loc_5DB')

    Jump('loc_5EE')

    def _loc_5DE(): pass

    label('loc_5DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 4, 0x644)),
            Expr.Return,
        ),
        'loc_5EE',
    )

    OP_71(0x0022, 0x0010)
    OP_64(0x00, 0x0001)

    def _loc_5EE(): pass

    label('loc_5EE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CE, 0, 0x670)),
            Expr.Return,
        ),
        'loc_60A',
    )

    MapSetFlags(0x02000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x4A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_0E_6411)

    Jump('loc_61A')

    def _loc_60A(): pass

    label('loc_60A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 4, 0x644)),
            Expr.Return,
        ),
        'loc_61A',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_61A(): pass

    label('loc_61A')

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0002 offset: 0x624
@scena.Code('func_02_624')
def func_02_624():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_639',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_624')

    def _loc_639(): pass

    label('loc_639')

    Return()

# id: 0x0003 offset: 0x63A
@scena.Code('func_03_63A')
def func_03_63A():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '杜南公爵晕过去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x659
@scena.Code('func_04_659')
def func_04_659():
    TalkBegin(0x00FE)

    ChrTalk(
        0x000A,
        (
            '#0660131281V#720F公主殿下，还有各位，\n',
            '十分感谢你们的宽宏大量。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660131282V我代表殿下向你们谢罪，\n',
            '对于此恩此德，没齿难忘。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x6E1
@scena.Code('func_05_6E1')
def func_05_6E1():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_7CC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_761',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x000F,
        (
            '刚才我给公主殿下帮忙，\n',
            '制做了一些点心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '公主做的点心真是非常美味，\n',
            '如果有兴趣请一定要来品尝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7C9')

    def _loc_761(): pass

    label('loc_761')

    ChrTalk(
        0x000F,
        (
            '刚才我给公主殿下帮忙，\n',
            '制做了一些点心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '公主做的点心真是非常美味，\n',
            '如果有兴趣请一定要来品尝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7C9(): pass

    label('loc_7C9')

    Jump('loc_8D7')

    def _loc_7CC(): pass

    label('loc_7CC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_8B2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_82B',
    )

    ChrTalk(
        0x00FE,
        (
            '公主殿下她\n',
            '刚才悄悄地到街上去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '据说是因为\n',
            '她的同学也到王都来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8AF')

    def _loc_82B(): pass

    label('loc_82B')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '因为公主殿下回来了，\n',
            '我要把这个房间打扫一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '公主殿下她\n',
            '刚才悄悄地到街上去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '据说是因为\n',
            '她的同学也到王都来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8AF(): pass

    label('loc_8AF')

    Jump('loc_8D7')

    def _loc_8B2(): pass

    label('loc_8B2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_8BC',
    )

    Jump('loc_8D7')

    def _loc_8BC(): pass

    label('loc_8BC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_8C6',
    )

    Jump('loc_8D7')

    def _loc_8C6(): pass

    label('loc_8C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_8D0',
    )

    Jump('loc_8D7')

    def _loc_8D0(): pass

    label('loc_8D0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_8D7',
    )

    def _loc_8D7(): pass

    label('loc_8D7')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x8DB
@scena.Code('func_06_8DB')
def func_06_8DB():
    TalkBegin(0x0008)
    ChrClearFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x87),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_900',
    )

    ChrSetSubChip(0x00FE, 1)

    Jump('loc_91B')

    def _loc_900(): pass

    label('loc_900')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_916',
    )

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_91B')

    def _loc_916(): pass

    label('loc_916')

    ChrSetSubChip(0x00FE, 2)

    def _loc_91B(): pass

    label('loc_91B')

    ChrSetDirection(0x00FE, 180, 0)
    ChrSetFlags(0x00FE, 0x0010)

    ChrTalk(
        0x0008,
        (
            '#0630141307V#090F嗯，\n',
            '已经休养了很长的一段时间。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630141308V从明天开始要抓紧时间，\n',
            '还有很多的事情要处理呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630141309V#094F又要和科洛蒂娅\n',
            '暂时分别一些日子了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0008)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x0007 offset: 0x9DB
@scena.Code('func_07_9DB')
def func_07_9DB():
    TalkBegin(0x0015)
    ChrClearFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x5A),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_A00',
    )

    ChrSetSubChip(0x00FE, 2)

    Jump('loc_A31')

    def _loc_A00(): pass

    label('loc_A00')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_A16',
    )

    ChrSetSubChip(0x00FE, 1)

    Jump('loc_A31')

    def _loc_A16(): pass

    label('loc_A16')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_A2C',
    )

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_A31')

    def _loc_A2C(): pass

    label('loc_A2C')

    ChrSetSubChip(0x00FE, 2)

    def _loc_A31(): pass

    label('loc_A31')

    ChrSetDirection(0x00FE, 270, 0)
    ChrSetFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_AA5',
    )

    ChrTalk(
        0x0015,
        (
            '#0060141317V#040F等没事了，\n',
            '就和约修亚一起过来坐坐吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060141318V大家一起喝茶聊聊天。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BF2')

    def _loc_AA5(): pass

    label('loc_AA5')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x0015,
        (
            '#0060141310V#040F艾丝蒂尔，\n',
            '一起来喝杯茶吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060141311V还想让你尝尝我新学来的点心呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141312V#506F不好意思，科洛丝。\n',
            '我正在找约修亚呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#0060141313V#044F……约修亚？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060141314V#041F那好，\n',
            '等你们没事了就一起过来吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060141315V我们会在这等着的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010141316V#008F啊，嗯……谢谢。\n',
            '让你们费心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BF2(): pass

    label('loc_BF2')

    ChrSetSubChip(0x00FE, 0)
    TalkEnd(0x0015)

    Return()

# id: 0x0008 offset: 0xBFB
@scena.Code('func_08_BFB')
def func_08_BFB():
    TalkBegin(0x0016)
    ChrClearFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x87),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_C20',
    )

    ChrSetSubChip(0x00FE, 2)

    Jump('loc_C3B')

    def _loc_C20(): pass

    label('loc_C20')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_C36',
    )

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_C3B')

    def _loc_C36(): pass

    label('loc_C36')

    ChrSetSubChip(0x00FE, 1)

    def _loc_C3B(): pass

    label('loc_C3B')

    ChrSetDirection(0x00FE, 0, 0)
    ChrSetFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_CF2',
    )

    ChrTalk(
        0x0016,
        (
            '#0100141322V#170F以后决不能让理查德上校叛变\n',
            '这种事件再次发生了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100141321V#176F亲卫队会和摩尔根将军\n',
            '以及卡西乌斯上校齐心协力，\n',
            '为王国军的再建拼尽全力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DCB')

    def _loc_CF2(): pass

    label('loc_CF2')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x0016,
        (
            '#0100141319V#170F诞辰庆典平安无事地结束，\n',
            '实在太好了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100141320V以后决不能让理查德上校叛变\n',
            '这种事件再次发生了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100141321V#176F亲卫队会和摩尔根将军\n',
            '以及卡西乌斯上校齐心协力，\n',
            '为王国军的再建拼尽全力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DCB(): pass

    label('loc_DCB')

    ChrSetSubChip(0x00FE, 0)
    TalkEnd(0x0016)

    Return()

# id: 0x0009 offset: 0xDD4
@scena.Code('func_09_DD4')
def func_09_DD4():
    TalkBegin(0x0017)
    ChrClearFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x5A),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_DF9',
    )

    ChrSetSubChip(0x00FE, 1)

    Jump('loc_E2A')

    def _loc_DF9(): pass

    label('loc_DF9')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_E0F',
    )

    ChrSetSubChip(0x00FE, 2)

    Jump('loc_E2A')

    def _loc_E0F(): pass

    label('loc_E0F')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_E25',
    )

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_E2A')

    def _loc_E25(): pass

    label('loc_E25')

    ChrSetSubChip(0x00FE, 1)

    def _loc_E2A(): pass

    label('loc_E2A')

    ChrSetDirection(0x00FE, 90, 0)
    ChrSetFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_EF2',
    )

    ChrTalk(
        0x0017,
        (
            '#0650141324V#711F这样看着陛下和公主殿下\n',
            '开心快乐地在一起，\n',
            '我深切体会到和平的日子又回来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650141325V这全靠艾丝蒂尔和各位的努力换来的啊。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650141326V真是千恩万谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FA7')

    def _loc_EF2(): pass

    label('loc_EF2')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x0017,
        (
            '#0650141324V#711F这样看着陛下和公主殿下\n',
            '开心快乐地在一起，\n',
            '我深切体会到和平的日子又回来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650141325V这全靠艾丝蒂尔和各位的努力换来的啊。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650141326V真是千恩万谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FA7(): pass

    label('loc_FA7')

    ChrSetSubChip(0x00FE, 0)
    TalkEnd(0x0017)

    Return()

# id: 0x000A offset: 0xFB0
@scena.Code('func_0A_FB0')
def func_0A_FB0():
    EventBegin(0x00)
    CameraMove(-460, 0, 2620, 0)
    ChrSetChipByIndex(0x0101, 1)
    ChrSetChipByIndex(0x0102, 2)
    ChrSetChipByIndex(0x0138, 0)
    ChrSetRGBAMask(0x0101, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0102, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0138, 255, 255, 255, 0, 0)
    ChrSetPos(0x0101, 10, 0, -5370, 225)
    ChrSetPos(0x0102, 10, 0, -5370, 225)
    ChrSetPos(0x0138, 10, 0, -5370, 225)

    @scena.Lambda('lambda_102C')
    def lambda_102C():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0138, 0x0002, lambda_102C)

    @scena.Lambda('lambda_103E')
    def lambda_103E():
        ChrWalkTo(0x00FE, -90, 0, 1380, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0138, 0x0001, lambda_103E)

    Sleep(500)

    @scena.Lambda('lambda_105E')
    def lambda_105E():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_105E)

    @scena.Lambda('lambda_1070')
    def lambda_1070():
        ChrWalkTo(0x00FE, -1040, 0, -420, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1070)

    Sleep(500)

    @scena.Lambda('lambda_1090')
    def lambda_1090():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_1090)

    @scena.Lambda('lambda_10A2')
    def lambda_10A2():
        ChrWalkTo(0x00FE, 750, 0, -420, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_10A2)

    WaitForThreadExit(0x0138, 0x0001)
    ChrSetDirection(0x0138, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010121073V#327F呼～刚才好紧张。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121074V#328F谢谢您，希尔丹夫人，\n',
            '多亏您的及时相助。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121075V#331F很高明的手腕呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0138,
        (
            '#0650121076V#713F#5P多谢你们的夸奖。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121077V#711F那么……怎么样，\n',
            '在和陛下见面之前先换衣服吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121078V不用特别在意的，\n',
            '我先带你们去换吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121079V#471F没关系，就这个样子可以了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121080V#333F#3S请务必要带我去换衣服。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)
    FadeOut(2000, 0, -1)

    @scena.Lambda('lambda_1260')
    def lambda_1260():
        CameraMove(7620, 0, 14990, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1260)

    OP_0D()
    TerminateThread(0x0101, 0x01)
    MapSetFlags(0x00000800)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlayBGM(84)
    CameraMove(-52690, 0, 7170, 0)
    OP_67(0, 7500, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetPos(0x0101, -51850, 0, 7470, 270)
    ChrSetPos(0x0102, -53280, 0, 7850, 180)
    ChrSetPos(0x0138, -52990, 0, 5970, 0)
    Sleep(500)

    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010121081V#507F你还真是的，那么害羞干嘛。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121082V刚才那样不就很好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121083V#017F这可关系到我的名誉啊，\n',
            '刚才那个样子是绝对不行的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121084V#010F对了，希尔丹夫人，\n',
            '这个房间莫非是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0138,
        (
            '#0650121085V#713F嗯……\n',
            '就是科洛蒂亚公主的房间。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121086V不过她一般不在王城里面居住，\n',
            '所以就没有怎么用过……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0138, 400)

    ChrTalk(
        0x0101,
        (
            '#0010121087V#501F咦～是这样的啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121088V#505F可是……\n',
            '不是说公主殿下在照顾着陛下的吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0138,
        (
            '#0650121089V#715F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121090V#012F那果然也是假消息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0138,
        (
            '#0650121091V#713F详细情况你们就直接询问陛下吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121092V#710F女王宫的二楼就是\n',
            '艾莉茜雅女王的房间。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121093V我们这就去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x00C8, 3, 0x643))

    ExecExpressionWithVar(
        0x31,
        (
            (Expr.PushLong, 0xC8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    EventEnd(0x00)
    ChrSetChipByIndex(0x0000, 0)
    ChrSetChipByIndex(0x0001, 3)
    ChrSetChipByIndex(0x0138, 4)

    Return()

# id: 0x000B offset: 0x15CA
@scena.Code('func_0B_15CA')
def func_0B_15CA():
    EventBegin(0x00)
    Fade(1000)
    SetScenaFlags(ScenaFlag(0x00C8, 4, 0x644))
    OP_28(0x004A, 0x01, 0x0100)
    OP_28(0x004A, 0x01, 0x0200)
    ChrSetChipByIndex(0x0138, 0)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetPos(0x0138, -1000, 8000, 35250, 0)
    ChrSetPos(0x0101, -1500, 8000, 34000, 0)
    ChrSetPos(0x0102, -500, 8000, 34000, 0)
    ChrSetPos(0x0008, -980, 8000, 38840, 0)
    CameraMove(-1080, 8000, 35400, 0)
    OP_67(0, 7500, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(27000, 0)
    OP_6E(280, 0)
    OP_0D()
    PlaySE(113, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0138,
        (
            '#0650121095V#713F陛下，打扰了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121096V我照之前所说，\n',
            '把艾丝蒂尔和约修亚带来了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '老妇人的声音',
        (
            '#0630121097V#4P……辛苦你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '老妇人的声音',
        (
            '#0630121098V#4P请进来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0138,
        (
            '#0650121099V#711F我明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0138, 270, 400)
    ChrWalkTo(0x0138, -2170, 8000, 35250, 2000, 0x00)
    ChrSetDirection(0x0138, 180, 400)

    ChrTalk(
        0x0138,
        (
            '#0650121100V#711F#1P我就在这里等着。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121101V那么你们俩就进去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121102V#006F好、好的……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121103V#015F打扰了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(-100970, 0, 4310, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, -96900, 0, 15200, 0)
    ChrSetPos(0x0101, -101650, 0, 3300, 0)
    ChrSetPos(0x0102, -100450, 0, 3300, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010121104V#004F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_188C')
    def lambda_188C():
        CameraMove(-97420, 0, 14400, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_188C)

    @scena.Lambda('lambda_18A4')
    def lambda_18A4():
        OP_6C(18000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_18A4)

    @scena.Lambda('lambda_18B4')
    def lambda_18B4():
        OP_67(0, 4200, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_18B4)

    @scena.Lambda('lambda_18CC')
    def lambda_18CC():
        OP_6E(317, 4000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_18CC)

    Sleep(4000)

    ChrSetDirection(0x0008, 180, 300)

    ChrTalk(
        0x0008,
        (
            '#0630121105V#091F#5P呵呵……\n',
            '欢迎你们两位的到来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121106V#090F我的名字叫做\n',
            '艾莉茜雅·冯·奥赛雷丝。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121107V利贝尔王国第２６代国王。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_197D')
    def lambda_197D():
        CameraMove(-97420, 0, 14400, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_197D)

    @scena.Lambda('lambda_1995')
    def lambda_1995():
        ChrWalkTo(0x00FE, -98510, 0, 12640, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1995)

    Sleep(300)

    @scena.Lambda('lambda_19B5')
    def lambda_19B5():
        ChrWalkTo(0x00FE, -97260, 0, 12110, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_19B5)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010121108V#008F我、我是……\n',
            '艾丝蒂尔·布莱特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121109V游击士协会的准游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121110V#015F同为游击士协会的准游击士，\n',
            '我的名字是约修亚·布莱特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121111V初次见面，陛下您好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630121112V#090F#5P艾丝蒂尔和约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121113V我真的很高兴能和你们两位见面。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121114V没有什么好东西可以款待你们，\n',
            '就以一些茶水微表谢意吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121115V#091F请吧，我们到那边去慢慢谈。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(-105030, 0, 9180, 0)
    OP_67(0, 6300, -10000, 0)
    CameraSetDistance(1990, 0)
    OP_6C(44000, 0)
    OP_6E(368, 0)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetFlags(0x0102, 0x0004)
    ChrSetChipByIndex(0x0101, 16)
    ChrSetChipByIndex(0x0102, 17)
    ChrSetChipByIndex(0x0008, 18)
    ChrSetPos(0x0008, -105250, 200, 10500, 180)
    ChrSetPos(0x0101, -103870, 200, 8990, 270)
    ChrSetPos(0x0102, -105250, 200, 7600, 0)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrSetPos(0x0011, -104620, 640, 8950, 0)
    ChrSetPos(0x0012, -105280, 640, 8300, 0)
    ChrSetPos(0x0010, -105350, 640, 9620, 0)
    ChrSetPos(0x0014, -105280, 700, 9050, 0)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0630121116V#093F这样啊……\n',
            '拉赛尔博士竟会卷入这样的事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121117V#094F将一切导力停止的黑色导力器……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121118V那样的物品竟然落入了上校手中……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121119V#012F博士说女王陛下也许会知道\n',
            '理查德上校使用这个黑色导力器的目的。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121120V请问……有什么线索吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630121121V#094F……………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121122V#093F只有一个线索。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121123V不过……\n',
            '我想上校应该不会知道那一点。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121124V希望那只是我多余的担心就好了……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121125V#505F请问……\n',
            '那个线索是什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630121126V#094F……把这些事情告诉你们也没什么关系。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121127V#092F——数十年前，在这个王都的地下\n',
            '检测出了巨大的导力反应。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121128V当时做这项导力调查研究的就是\n',
            '中央工房的拉赛尔博士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121129V#004F巨大的导力反应……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121130V#012F所谓王都的地下……\n',
            '就是指地下水路的周边吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630121131V#092F不是，是从比地下水路\n',
            '还要深很多的地方检测出来的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121132V博士认为那是古文明宝藏之地，\n',
            '埋藏着至今仍未失去机能的古代文明遗物。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0101, 1)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010121133V#004F古代文明的遗物……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0102, 2)
    Sleep(400)

    ChrTalk(
        0x0102,
        (
            '#0020121134V#012F就是被称为『古代遗物』的古代导力器。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121135V其中大部分都像四轮之塔塔顶的装置\n',
            '那样失去了机能……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121136V而小部分就像戴尔蒙市长的传家宝那样，\n',
            '还继续保持着机能。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121137V#505F那样的东西在王都地下……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121138V#580F啊，这么说那个『福音』就是……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0101, 0)
    Sleep(100)

    ChrSetSubChip(0x0102, 0)
    Sleep(400)

    ChrTalk(
        0x0102,
        (
            '#0020121139V#012F是用作将古代遗物的机能\n',
            '停止下来的特殊导力器……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121140V这种可能性是有的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630121141V#093F是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121142V可是，那个遗物究竟是什么\n',
            '以及为何会埋藏在那里这些问题至今仍未查明。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121143V拉赛尔博士的调查\n',
            '本身也是在非正式的进行当中……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121144V如果说上校从某个地方得知了其存在，\n',
            '我认为这也并不是不可能的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121145V#013F是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121146V不管怎样说，\n',
            '所有的事件有可能是因此而引起的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121147V#007F真是的，稍微想开一点，\n',
            '不要把事情想的那么严峻嘛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121148V#002F总之，只要人们陷入了困境，\n',
            '代表爱与正义的游击士就会立刻出现！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121149V无论如何也会阻止上校的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630121150V#090F呵呵……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121151V真不愧是……\n',
            '卡西乌斯上校的孩子啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121152V#004F！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121153V#014F陛下和父亲以前曾经认识吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630121154V#090F他是我去世的孩子的朋友，\n',
            '也是拯救王国的英雄呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121155V他退役之后，当了游击士还常帮我办事，\n',
            '真是……无论何时都承蒙他的关照啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121156V#004F还、还有这回事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121157V#015F这我们以前并不知道呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630121158V#090F呵呵，以他的性格来看，\n',
            '你们两个不知道也是比较正常的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121159V假如十年前的战争中，\n',
            '没有他在战场上的奋力拼搏……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121160V这个地方还会存在吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121161V#007F其实呢，女王陛下……\n',
            '这件事的详细情况我确实不太清楚呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630121162V#094F那么，告诉你们真相的角色，\n',
            '说不定是留给了身为女王的本人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121163V#090F艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121164V你们两个愿意稍微听一听\n',
            '我这个上了年纪的人讲的故事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121165V#006F啊……好的，那当然啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121166V#010F洗耳恭听。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000003E8)
    Sleep(1000)

    FadeOut(2000, 0, -1)
    PlayBGM(83)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('艾莉茜雅女王')

    Talk(
        (
            '#0630121167V',
            (TxtCtl.SetColor, 0xC),
            '这是在十年前的春天发生的事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0630121168V埃雷波尼亚帝国的南部\n',
            '发生了一起十分沉痛的事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0630121169V因为至今整个事件的起因仍未查明，\n',
            '所以与事件有关的说明就省略了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0630121170V以这起事件为开端，\n',
            '埃雷波尼亚帝国向利贝尔王国宣战。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0630121171V之后，『百日战役』的苦难岁月\n',
            '就是从那个时候开始的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AD('ED6_DT04/C_VIS008._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(2000)

    TalkSetChrName('艾莉茜雅女王')

    Talk(
        (
            '#0630121172V就在帝国向王国宣战的同时，\n',
            '帝国军集中大量兵力攻陷了哈肯大门……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0630121173V除了有长城守护的王都格兰赛尔以外，\n',
            '利贝尔整片土地转瞬之间被全部占领了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0630121174V而且入侵的帝国军的兵力是\n',
            '我们王国军的三倍以上……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0630121175V即使卡尔瓦德要派来援军也来不及……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0630121176V王都被占领也只是时间上的问题。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AE(0x000001F4)
    Sleep(1000)

    OP_AD('ED6_DT04/C_VIS009._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(2000)

    TalkSetChrName('艾莉茜雅女王')

    Talk(
        (
            '#0630121177V可是开战的两个月之后……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0630121178V处于被动的战局发生了巨大的逆转。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0630121179V利用当时才开发完毕的警备飞艇，\n',
            '王国军将连接各地的关所一一夺回，\n',
            '并且切断了帝国军的联络。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0630121180V接着，以雷斯顿要塞为先发部队，\n',
            '王国军总兵力乘坐水上飞艇出击，\n',
            '将各个地区顺利夺了回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0630121181V蔡斯、卢安、柏斯、洛连特……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0630121182V帝国军的补给线被切断了之后，\n',
            '王国军将占领各地的帝国军师团逐个击破。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AE(0x000001F4)
    Sleep(1000)

    OP_AD('ED6_DT04/C_VIS010._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(2000)

    TalkSetChrName('艾莉茜雅女王')

    Talk(
        (
            '#0630121183V制定这次反攻作战计划的就是\n',
            '卡西乌斯·布莱特上校——',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0630121184V摩尔根将军的得力助手、\n',
            '理查德上校的顶头上司，\n',
            '同时也是你们两个孩子的父亲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0630121185V此后不久，\n',
            '在游击士协会以及七耀教会的仲裁之下，\n',
            '长达百日的战争也就此宣告结束。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0630121186V可是就在那个时候……\n',
            '卡西乌斯上校失去了他的最爱最重要的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AE(0x000001F4)
    Sleep(1000)

    OP_AD('ED6_DT04/C_VIS011._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(2000)

    TalkSetChrName('艾莉茜雅女王')

    Talk(
        (
            '#0630121187V她就是莱娜·布莱特女士……\n',
            '也是艾丝蒂尔你的母亲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0630121188V在反攻作战即将胜利的时刻，\n',
            '走投无路的帝国军师团为了报复王国军，\n',
            '炮击破坏了作为洛连特象征的钟楼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0630121189V于是……\n',
            '后面的事情你们都知道了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0630121190V卡西乌斯上校，\n',
            '甚至连夫人最后一面都没有见到……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AE(0x00000064)
    FadeIn(2000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010121191V#003F……怎么会……………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121192V怎么会这样……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630121193V#094F……无奈自己制定的作战计划\n',
            '却是导致了夫人死去的原因。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121194V因此而深深自责的卡西乌斯上校决定退役，\n',
            '走上了游击士的道路……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121195V守护在战争中幸存下来的你的身边……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121196V他这样做，外人虽然非常不解，\n',
            '但也是为了用自己双手来保护最亲的人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121197V#003F笨蛋……爸爸……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121198V因为爸爸的过失而导致妈妈的离去什么的……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121199V明明不是这样的啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121200V#013F艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630121201V#093F嗯，是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121202V这一切一切的悲剧……都是我这个\n',
            '没有好好保护自己子民的女王的过错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121203V#094F对不起，艾丝蒂尔。\n',
            '我没能保护好你的妈妈……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121204V对于此事……\n',
            '请接受我深深的歉意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121205V#002F没、没有必要道歉呢！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121206V#500F女王陛下一直守护着这来之不易的和平……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121207V而爸爸他们也在拼死守护着这个国家……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121208V妈妈以生命为代价守护了我……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121209V#008F这样，我就已经满足了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630121210V#090F艾丝蒂尔……\n',
            '谢谢，你的确是个优秀的孩子……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121211V#094F能够见到你真是太好了……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121212V这是我发自心底的感慨。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121213V#008F女王陛下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630121214V#094F不过，正因为如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121215V#090F正因为如此，\n',
            '我不希望你们遇到任何危险。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121216V无论结局是怎样都好，\n',
            '我都不想让你们再卷入这次的事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121217V#580F啊……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121218V可、可是我们俩是受尤莉亚中尉委托\n',
            '来协助女王陛下您的啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630121219V#090F谢谢。\n',
            '你们的好意我心领了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121220V在卡西乌斯上校外出的时候，\n',
            '你们两个孩子万一出了什么事情，\n',
            '身为女王的我只会无法向他交待……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121221V因此，请你们回到洛连特的家中，\n',
            '等待你们的父亲回来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121222V#580F可、可是……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121223V#015F可是，女王陛下……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121224V由父亲取回的、陛下您一直守护着的和平，\n',
            '现在正在经受着严峻的考验。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630121225V#093F约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121226V#012F因为『福音』引起的所有事件……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121227V就这样下去的话……\n',
            '上校一旦达成让公爵成为国王的目的，\n',
            '现在的和平会变成如何的样子呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121228V请陛下您务必要考虑一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630121229V#093F…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121230V#003F对、对不起，女王陛下……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121231V我们两个自从成为游击士以来，\n',
            '就作为爸爸的代理人来完成任务。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121232V从那个时候的空贼事件开始，\n',
            '收到了老爸的信、来历不明的包裹，\n',
            '然后就沿着这样的轨迹在各地修行……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121233V感觉就好像是老爸在\n',
            '引导着我们来这里和女王陛下见面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121234V#500F所以……我也有必须守护的东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121235V这和平的、幸福的每一天……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121236V以及这一路上所认识的，\n',
            '关心我、喜欢我的各位朋友……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121237V#002F我会用自己的方法来守护着的！\n',
            '就像女王陛下您和妈妈那样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630121238V#093F艾丝蒂尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121121V#094F……………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121240V的确……\n',
            '和那个孩子所说的一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121241V#004F咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630121242V#090F我也终于明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121243V我想通过艾丝蒂尔你们\n',
            '向游击士协会委托一些需要解决的事情。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121244V#501F女王陛下……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121245V#010F陛下……\n',
            '请您尽管吩咐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630121246V#092F委托的内容就是——\n',
            '救出被情报部囚禁的人质。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121247V其中还包括我的孙女科洛蒂娅。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121248V#002F啊，公主殿下果然\n',
            '被那些家伙抓到某个地方去了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630121249V#094F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121250V现在回想起来……\n',
            '这次的政变是因为我要推选那个孩子\n',
            '为下一任国王而开始的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121251V#012F果然不是杜南公爵呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630121252V#093F嗯，虽说杜南是我的外甥，\n',
            '但这个人是个问题诸多的败家子。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121253V相比之下，我的孙女虽说不算很成熟，\n',
            '但在很多方面都要出色很多。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121254V在考虑了王国的未来之后……\n',
            '我做出的决定就是选择科洛蒂娅公主。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121255V#506F嗯……\n',
            '公主的事情我不是很了解……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121256V不过不管怎么说，\n',
            '做出这样的决定肯定是正确的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630121257V#094F可是无论何时……\n',
            '这个世界总是倾向于对女性当权\n',
            '持反对甚至是敌对的态度。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121258V而且，当年被侵略的历史依旧历历在目，\n',
            '所以这种态度也越来越强硬……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121259V#092F国家连续两代都由女性来统治，\n',
            '结果只会导致国力的衰弱……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121260V会出现持有这种观点的人物，\n',
            '也不是什么不可思议的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121261V#015F原来如此……\n',
            '那样的人物就是理查德上校吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630121262V#092F是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121263V我打算推选科洛蒂娅为下一任国王的想法\n',
            '不知何时被他得知了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121264V于是他就把这件事告诉了杜南公爵，\n',
            '然后发动了这次政变。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121265V实际上，他暗中操纵杜南公爵，\n',
            '是为了要把利贝尔打造成一个\n',
            '能与周边大国抗衡的强大军事国家……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121266V#012F原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121267V终于明白整件事情的全貌了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0101, 1)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010121268V#505F打造成强大的军事国家……\n',
            '具体来说他要怎么做呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0102, 2)
    Sleep(400)

    ChrTalk(
        0x0102,
        (
            '#0020121269V#012F会有各种各样的做法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121270V例如提高税率、增加军费开支……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121271V开发大量具有破坏性的导力兵器……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121272V采取大规模的征兵制……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121273V甚至能和利贝尔不承认的组织『猎兵团』\n',
            '签订所谓的合法契约……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121274V#580F怎、怎么会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630121275V#094F的确，与之类似的要求，\n',
            '理查德上校也曾向我提出过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0101, 0)
    Sleep(100)

    ChrSetSubChip(0x0102, 0)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#0630121276V#093F虽说我知道这也是\n',
            '出自纯粹的爱国心而说的一番话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121277V但是无论怎样，\n',
            '我也不认为这种作法是正确的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121278V要守护一个国家，\n',
            '仅靠强大的军事力量是不行的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121279V只要和周边诸国协调好关系，\n',
            '多做一些善意的互利的外交政策……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121280V加强国家之间的技术和经济交流，\n',
            '这样就可以让全国各地更加繁荣，\n',
            '也就可以牢固地守护着国家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121281V#015F……陛下所言的确才是真正的道理。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121282V#006F嗯嗯！我也觉得是！\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630121283V#092F但是，上校一口断定这是\n',
            '我自己带有妇人之见的理想论。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121284V而且没想到的是……\n',
            '他以科洛蒂娅的安全来要挟我退位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121285V#005F！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630121286V#094F大部分掌权者的亲属都被扣押为人质，\n',
            '所以他们都不敢违抗上校的意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121287V可我是利贝尔的女王。\n',
            '不能因为骨肉之情而出卖国家的未来。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121288V#093F话虽然这么说……\n',
            '但那孩子毕竟是我唯一的孙女……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121289V我不能见死不救啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121290V#006F女王陛下……\n',
            '这件事就请您放心吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121291V#010F您委托的旨意，我们已经清楚地了解了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121292V我们一定会将包括公主殿下在内的\n',
            '所有人质解救出来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630121293V#090F非常感谢……\n',
            '艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121294V这样一来，\n',
            '我就有和上校相抗衡的保证。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121295V#002F请、请问，\n',
            '就没有其他的委托了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121296V还有『福音』那件事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121297V如果现在要帮助女王陛下您逃离这里，\n',
            '我认为也不是不可能的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630121298V#090F谢谢你，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121299V不过，即使我离开这里，\n',
            '也不能改变国家如今的局势。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121300V#094F这件事究竟与『福音』有着怎样的关联，\n',
            '对此我真的非常在意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121301V所以，我要向上校问清楚\n',
            '他做这些事情的真实意图所在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)
    FadeOut(1500, 0, -1)
    OP_0D()
    OP_21()
    CameraMove(-52350, 0, 6280, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrClearFlags(0x0101, 0x0004)
    ChrClearFlags(0x0102, 0x0004)
    ChrSetChipByIndex(0x0101, 1)
    ChrSetChipByIndex(0x0102, 2)
    ChrSetChipByIndex(0x0138, 0)
    ChrSetPos(0x0101, -53000, 0, 6160, 90)
    ChrSetPos(0x0102, -51450, 0, 6000, 270)
    PlayBGM(84)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010121302V#328F哈……女王陛下真是一位\n',
            '充满魅力和优雅感的女性啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121303V不但待人和蔼可亲，\n',
            '而且内心又坚强，性格又坚毅……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121304V#321F等我到了那个年纪时，\n',
            '也要成为那样有魅力的老奶奶呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121305V#337F有魅力……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121306V#338F不过的确是一位很有\n',
            '一国之主风范的女性呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121307V#323F唔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121308V真想这就阻止政变，\n',
            '把女王陛下和公主他们救出来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121309V#330F唔……其实这并不属于\n',
            '游击士协会所管辖的范围……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121310V不过无论如何，\n',
            '我们也要尽力去完成委托。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121311V#326F嗯……没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121312V#327F而且，能从女王那里听说到老爸的事迹，\n',
            '简直就像是在做梦一样……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010121313V还会不会有我不知道的事情冒出来呢？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(113, 0x00, 0x64)
    Sleep(500)

    ChrSetRGBAMask(0x0138, 255, 255, 255, 0, 0)
    ChrSetPos(0x0138, -51030, 0, 420, 225)
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0102, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    @scena.Lambda('lambda_4BFD')
    def lambda_4BFD():
        ChrTurnDirection(0x00FE, 0x0138, 400)
        Yield()

        Jump('lambda_4BFD')

    DispatchAsync2(0x0101, 0x0001, lambda_4BFD)

    @scena.Lambda('lambda_4C0E')
    def lambda_4C0E():
        ChrTurnDirection(0x00FE, 0x0138, 400)
        Yield()

        Jump('lambda_4C0E')

    DispatchAsync2(0x0102, 0x0001, lambda_4C0E)

    ChrTalk(
        0x0138,
        (
            '#0650121314V#1P艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121315V你们准备好了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4C64')
    def lambda_4C64():
        ChrTurnDirection(0x00FE, 0x0138, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4C64)

    ChrTurnDirection(0x0101, 0x0138, 400)

    ChrTalk(
        0x0101,
        (
            '#0010121316V#471F啊，好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(6, 0x00, 0x64)
    Sleep(300)

    @scena.Lambda('lambda_4CA4')
    def lambda_4CA4():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0138, 0x0002, lambda_4CA4)

    @scena.Lambda('lambda_4CB6')
    def lambda_4CB6():
        ChrWalkTo(0x00FE, -52060, 0, 3990, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0138, 0x0001, lambda_4CB6)

    CameraMove(-52330, 0, 5310, 2000)
    WaitForThreadExit(0x0138, 0x0001)

    ChrTalk(
        0x0138,
        (
            '#0650121317V#710F那我们就立刻回休息室去吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121318V已经过１１点了……\n',
            '再过一会儿就是新的一天了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121319V#324F哇啊，已经这么晚了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121320V#330F我们和陛下聊天用了很长时间呢。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121321V如果再这么呆下去的话，\n',
            '看守的那些士兵就会怀疑了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    ChrSetPos(0x0101, -52650, 0, 5460, 180)
    ChrSetPos(0x0102, -52650, 0, 5460, 180)
    ChrSetPos(0x0138, -52650, 0, 5460, 180)
    ChrSetChipByIndex(0x0000, 0)
    ChrSetChipByIndex(0x0001, 1)
    ChrSetChipByIndex(0x0138, 2)
    OP_1B(0x02, 0x00, 0xFFFF)
    CameraMove(-52650, 0, 5460, 0)
    OP_67(0, 7500, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x000C offset: 0x4E95
@scena.Code('func_0C_4E95')
def func_0C_4E95():
    OP_28(0x004E, 0x01, 0x0004)
    EventBegin(0x00)
    CameraMove(170, 0, 5170, 0)
    OP_67(0, 7500, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(44000, 0)
    OP_6E(280, 0)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x0009, 0, 0, 9760, 180)
    ChrSetPos(0x000B, -1480, 0, 9280, 180)
    ChrSetPos(0x000C, -660, 0, 8290, 180)
    ChrSetPos(0x000D, 700, 0, 8420, 180)
    ChrSetPos(0x000E, 1400, 0, 9310, 180)
    ChrSetPos(0x0101, -90, 0, 920, 0)
    ChrSetPos(0x0105, -1330, 0, 430, 0)
    ChrSetPos(0x0103, 930, 0, 430, 0)
    ChrSetChipByIndex(0x0101, 9)
    ChrSetChipByIndex(0x0103, 11)
    ChrSetChipByIndex(0x0105, 13)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0009,
        (
            '#220F叛、叛逆者！\n',
            '居然恬不知耻的跑到这儿来了！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640131196V明知我是将要继承王位的人，\n',
            '你们还要动粗吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F别说笑了，你那发型已经够搞笑了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010131198V你现在已经\n',
            '再也不可能成为国王了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#220F什、什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030840019V#020F您是杜南公爵阁下吧。\n',
            '我们是游击士协会派来的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030840020V科洛蒂娅殿下委托我们\n',
            '来救出女王陛下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030840021V如果您能通融一下，\n',
            '我们也会给您好处的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#220F科、科洛蒂娅！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640131204V那个小姑娘……\n',
            '简直是多此一举！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060940013V#040F杜南王叔……\n',
            '请您不要再执迷不悟了好吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060131206V王叔，您是被理查德\n',
            '上校给利用了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#220F你、你在胡说什么啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640131208V………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#0641110005V#220F你、你、你、\n',
            '你不是科洛蒂娅吗！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那样的发型和装扮，像个什么样子！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F终于发觉了啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010131213V原来这就是你在卢安\n',
            '没能注意到的原因啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F虽然之前不是很了解，\n',
            '不过的确是个很迟钝的人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F对不起，一直瞒着您\n',
            '这件事，是我不好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#220F根、根本就是把我\n',
            '当傻瓜来耍！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640131217V这就是为何女人这种生物\n',
            '不可信任的原因啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0641110006V狡猾、小气，为一些不值得\n',
            '的小事情故意找碴儿……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640131219V怎么能把王冠交给\n',
            '这样无聊的家伙呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x000B, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x000C, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x000D, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x000E, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#220F……嗯……不过………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '大、大人……\n',
            '情况不妙啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '还、还是投降吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哈哈……无聊的手下啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F哎呀呀，看来我得对你另眼相看了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030131228V在这样的时代中，\n',
            '还敢做出这么有胆识的发言。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F对、对不起了王叔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060940014V这回有点儿……\n',
            '我也不好帮您求情了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_562F')
    def lambda_562F():
        ChrWalkTo(0x00FE, 290, 0, 22950, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_562F)

    @scena.Lambda('lambda_564A')
    def lambda_564A():
        ChrWalkTo(0x00FE, 290, 0, 22950, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_564A)

    @scena.Lambda('lambda_5665')
    def lambda_5665():
        ChrWalkTo(0x00FE, 290, 0, 22950, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_5665)

    CameraMove(420, 0, 10250, 500)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0103, 0xFF)
    TerminateThread(0x0105, 0xFF)
    Battle(0x000003AA, 0x00000000, 0x00, 0x0002, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_56B0'),
        (-1, 'loc_56B3'),
    )

    def _loc_56B0(): pass

    label('loc_56B0')

    OP_B4(0x00)

    Return()

    def _loc_56B3(): pass

    label('loc_56B3')

    EventBegin(0x00)
    ChrSetPos(0x000B, -1890, 0, 12000, 315)
    ChrSetPos(0x000C, 280, 0, 13640, 135)
    ChrSetPos(0x000D, 3410, 0, 11230, 315)
    ChrSetPos(0x000E, 1760, 0, 8900, 177)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000003, 'loc_5705'),
        (-1, 'loc_5E39'),
    )

    def _loc_5705(): pass

    label('loc_5705')

    CameraMove(-2350, 0, 8189, 0)
    ChrSetPos(0x0009, -4620, 0, 7950, 90)
    ChrSetPos(0x0101, -1690, 0, 9010, 22)
    ChrSetPos(0x0105, -390, 0, 8010, 90)
    ChrSetPos(0x0103, -1510, 0, 6870, 90)
    OP_2B(0x004D, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#000F好的，解决了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '接下来，应该\n',
            '轮到公爵您了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_579D')
    def lambda_579D():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_579D)

    @scena.Lambda('lambda_57AB')
    def lambda_57AB():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_57AB)

    @scena.Lambda('lambda_57B9')
    def lambda_57B9():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_57B9)

    ChrMoveTo(0x0009, -5440, 0, 7860, 2000, 0x00)

    ChrTalk(
        0x0103,
        (
            '#020F由女人手中挥出的鞭子，\n',
            '想不想品尝一下是什么滋味呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveTo(0x0009, -6430, 0, 7860, 2000, 0x00)

    ChrTalk(
        0x0009,
        (
            '#220F哇、哇呀呀呀呀呀……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640131235V不要过来，不要靠近我呀啊啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F对、对不起……\n',
            '请您原谅我们吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_58A2')
    def lambda_58A2():
        CameraMove(-4750, 0, 8080, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_58A2)

    ChrTalk(
        0x0009,
        (
            '#220F可恶，这样的话，\n',
            '我就只好拿陛下当盾牌……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '……嘿～哈～喝！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5900')
    def lambda_5900():
        ChrSetDirection(0x00FE, 275, 800)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_5900)

    ChrMoveTo(0x0009, -8240, 0, 7810, 7000, 0x00)
    OP_62(0x0009, 0x00000000, 1900, 0x30, 0x32, 0x00000096, 0x00)
    PlaySE(48, 0x00, 0x64)

    @scena.Lambda('lambda_5939')
    def lambda_5939():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_5939)

    ChrMoveTo(0x0009, -7900, 0, 7810, 3000, 0x00)
    WaitForThreadExit(0x0009, 0x0001)

    @scena.Lambda('lambda_5960')
    def lambda_5960():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_5960)

    ChrTalk(
        0x0009,
        (
            '#220F呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哎呀……\n',
            '好像惊吓过度了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030840022V#020F不过他确实阻碍我们了呢，\n',
            '这不是个很好的教训吗?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F是……\n',
            '真是不幸的事件啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '可是，难道就让\n',
            '王叔这么昏迷在这儿吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, -50, 0, 340, 315)

    ChrTalk(
        0x000A,
        (
            '……公、公爵大人！？　　　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0103, 65535)
    ChrSetChipByIndex(0x0105, 65535)

    @scena.Lambda('lambda_5A7A')
    def lambda_5A7A():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5A7A)

    @scena.Lambda('lambda_5A88')
    def lambda_5A88():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_5A88)

    @scena.Lambda('lambda_5A96')
    def lambda_5A96():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_5A96)

    CameraMove(-2009, 0, 6520, 1000)

    @scena.Lambda('lambda_5AB5')
    def lambda_5AB5():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_5AB5')

    DispatchAsync2(0x0101, 0x0001, lambda_5AB5)

    @scena.Lambda('lambda_5AC6')
    def lambda_5AC6():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_5AC6')

    DispatchAsync2(0x0103, 0x0001, lambda_5AC6)

    @scena.Lambda('lambda_5AD7')
    def lambda_5AD7():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_5AD7')

    DispatchAsync2(0x0105, 0x0001, lambda_5AD7)

    @scena.Lambda('lambda_5AE8')
    def lambda_5AE8():
        CameraMove(-4750, 0, 8080, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_5AE8)

    OP_92(0x000A, 0x0009, 600, 5000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#000F啊，是菲利普先生！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0101, 400)

    ChrTalk(
        0x000A,
        (
            '#0660850002V#720F艾丝蒂尔小姐……\n',
            '还有科洛蒂娅公主！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660131247V对于这次我家主人\n',
            '的执迷不悟，我感到非常的抱歉！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660131248V这一切都是因为我没有\n',
            '好好教导大人而导致的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '因此，如果你们要惩罚的话，\n',
            '就请惩罚在下吧！　　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '菲利普深深的低下了头。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#000F惩、惩罚……\n',
            '只是晕过去了而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F菲利普先生……\n',
            '请您先抬起头来吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060131252V我们一行人，是为了救祖母……\n',
            '营救陛下而赶来的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060131253V原本就和王叔\n',
            '是没有任何牵连的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060131254V因此，请把王叔送到\n',
            '我的房间养伤吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#720F公、公主殿下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030131256V#020F事实上他没有受到什么伤害哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030131257V就只是因为突然受惊\n',
            '而昏厥，没事儿的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#720F大、大家……\n',
            '真是太感谢了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660131259V你们的大恩大德，我决对不会忘记的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    OP_63(0x0009)
    FadeIn(2000, 0)
    OP_0D()
    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x0001, 0xFF)
    TerminateThread(0x0002, 0xFF)
    EventEnd(0x00)

    Return()

    def _loc_5E39(): pass

    label('loc_5E39')

    CameraMove(370, 0, 8590, 0)
    ChrSetPos(0x0009, 1620, 0, 8100, 112)
    ChrSetPos(0x0101, -1690, 0, 9010, 22)
    ChrSetPos(0x0105, -390, 0, 8010, 90)
    ChrSetPos(0x0103, -1510, 0, 6870, 90)
    ChrTurnDirection(0x0101, 0x0009, 0)
    ChrTurnDirection(0x0105, 0x0009, 0)
    ChrTurnDirection(0x0103, 0x0009, 0)

    ChrTalk(
        0x0101,
        (
            '#000F呼，想不到连公爵\n',
            '也一起打晕了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030131261V#020F如果可以办到的话，\n',
            '倒是只需要打倒特务兵就行了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030840023V不过他确实阻碍我们了呢，\n',
            '这不是个很好的教训吗?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F是……\n',
            '真是不幸的事件啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '可是，难道就让\n',
            '王叔这么昏迷在这儿吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, -120, 0, -820, 315)

    ChrTalk(
        0x000A,
        (
            '……公、公爵大人！？　　　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0103, 65535)
    ChrSetChipByIndex(0x0105, 65535)

    @scena.Lambda('lambda_5FEB')
    def lambda_5FEB():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5FEB)

    @scena.Lambda('lambda_5FF9')
    def lambda_5FF9():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_5FF9)

    @scena.Lambda('lambda_6007')
    def lambda_6007():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_6007)

    CameraMove(510, 0, 4400, 1000)

    @scena.Lambda('lambda_6026')
    def lambda_6026():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_6026')

    DispatchAsync2(0x0101, 0x0001, lambda_6026)

    @scena.Lambda('lambda_6037')
    def lambda_6037():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_6037')

    DispatchAsync2(0x0103, 0x0001, lambda_6037)

    @scena.Lambda('lambda_6048')
    def lambda_6048():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_6048')

    DispatchAsync2(0x0105, 0x0001, lambda_6048)

    @scena.Lambda('lambda_6059')
    def lambda_6059():
        CameraMove(370, 0, 8590, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_6059)

    OP_92(0x000A, 0x0009, 600, 5000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#000F啊，是菲利普先生！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0101, 400)

    ChrTalk(
        0x000A,
        (
            '#0660850003V#720F艾丝蒂尔小姐……\n',
            '还有科洛蒂娅公主！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660131247V对于这次我家主人\n',
            '的执迷不悟，我感到非常的抱歉！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660131248V这一切都是因为我没有\n',
            '好好教导大人而导致的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '因此，如果你们要惩罚的话，\n',
            '就请惩罚在下吧！　　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '菲利普深深的低下了头。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#000F等、等一下！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F菲利普先生……\n',
            '请您先抬起头来吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060131252V我们一行人，是为了救祖母……\n',
            '营救陛下而赶来的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060131253V原本就和王叔\n',
            '是没有任何牵连的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060131254V因此，请把王叔送到\n',
            '我的房间养伤吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#720F公、公主殿下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030131256V#020F事实上他没有受到什么伤害哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030131278V就只是因为受了点打击\n',
            '而昏厥，没事儿的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#720F大、大家……\n',
            '真是太感谢了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660131259V你们的大恩大德，我决对不会忘记的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    OP_63(0x0009)
    FadeIn(2000, 0)
    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x0001, 0xFF)
    TerminateThread(0x0002, 0xFF)
    OP_0D()
    EventEnd(0x00)

    Return()

# id: 0x000D offset: 0x6399
@scena.Code('func_0D_6399')
def func_0D_6399():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 4, 0x644)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6410',
    )

    EventBegin(0x01)
    ChrTurnDirection(0x0000, 0x0001, 400)

    NpcTalk(
        0x0000,
        '希尔丹夫人',
        (
            '#0650121094V#710F女王陛下的房间就在\n',
            '这个女王宫的二楼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_6410(): pass

    label('loc_6410')

    Return()

# id: 0x000E offset: 0x6411
@scena.Code('func_0E_6411')
def func_0E_6411():
    OP_1F(0x50, 0x000000C8)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

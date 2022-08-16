import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4111_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4111   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4111.x'
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
        ('ED6_DT07/CH01220._CH', 'ED6_DT07/CH01220P._CP'),
        ('ED6_DT07/CH01230._CH', 'ED6_DT07/CH01230P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH02490._CH', 'ED6_DT07/CH02490P._CP'),
        ('ED6_DT07/CH01180._CH', 'ED6_DT07/CH01180P._CP'),
        ('ED6_DT07/CH01350._CH', 'ED6_DT07/CH01350P._CP'),
        ('ED6_DT07/CH01480._CH', 'ED6_DT07/CH01480P._CP'),
        ('ED6_DT07/CH01023._CH', 'ED6_DT07/CH01023P._CP'),
    ]

# id: 0x10001 offset: 0xF2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '赫穆特',
            x                   = 60450,
            z                   = 0,
            y                   = 62340,
            direction           = 10,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            name                = '诺琪',
            x                   = 60030,
            z                   = 0,
            y                   = 1650,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '马丁',
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
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '玛丽安',
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
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '海伦娜',
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
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '卡特莉娜夫人',
            x                   = 6600,
            z                   = 0,
            y                   = -55590,
            direction           = 83,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '达丽娅',
            x                   = -4760,
            z                   = 0,
            y                   = 1910,
            direction           = 150,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0008,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '莉安妮',
            x                   = -2300,
            z                   = 0,
            y                   = 61070,
            direction           = 87,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0009,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
    )

# id: 0x10002 offset: 0x1F2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x1F2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x1F2
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x1F2
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_223',
    )

    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, 60480, 0, 62200, 17)
    ChrSetPos(0x000D, -3010, 0, -54540, 0)

    Jump('loc_70B')

    def _loc_223(): pass

    label('loc_223')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_2D2',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, 59640, 0, 2040, 163)
    CreateThread(0x0008, 0x00, 0x00, func_03_76F)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, 60480, 0, 62200, 17)
    ChrSetChipByIndex(0x000A, 8)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 122730, 250, 64200, 278)
    ChrSetFlags(0x000A, 0x0010)
    ChrSetFlags(0x000A, 0x0004)
    TerminateThread(0x000A, 0xFF)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 123540, 0, 68800, 3)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, 113680, 0, -55940, 266)
    CreateThread(0x000C, 0x00, 0x00, func_07_7FF)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetPos(0x000D, -3010, 0, -54540, 0)

    Jump('loc_70B')

    def _loc_2D2(): pass

    label('loc_2D2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_347',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 115780, 0, 61020, 228)
    CreateThread(0x000A, 0x00, 0x00, func_05_7B7)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 123540, 0, 68800, 3)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, 113680, 0, -55940, 266)
    CreateThread(0x000C, 0x00, 0x00, func_07_7FF)
    ChrSetPos(0x000D, -3010, 0, -54540, 0)
    ChrSetFlags(0x000F, 0x0080)

    Jump('loc_70B')

    def _loc_347(): pass

    label('loc_347')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_3C6',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 115920, 0, 69500, 343)
    ChrSetFlags(0x000A, 0x0010)
    ChrTurnDirection(0x000B, 0x000A, 0)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 123540, 0, 68800, 3)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, 113680, 0, -55940, 266)
    CreateThread(0x000C, 0x00, 0x00, func_07_7FF)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetPos(0x000D, -3010, 0, -54540, 0)

    Jump('loc_70B')

    def _loc_3C6(): pass

    label('loc_3C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_44F',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, 58250, 0, 60130, 270)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 115780, 0, 61020, 228)
    CreateThread(0x000A, 0x00, 0x00, func_06_7DB)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 126360, 0, 1830, 270)
    ChrSetFlags(0x000B, 0x0010)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetFlags(0x000C, 0x0010)
    ChrSetPos(0x000C, 126360, 0, 740, 270)
    ChrSetPos(0x000D, -3010, 0, -54540, 0)
    ChrSetFlags(0x000F, 0x0080)

    Jump('loc_70B')

    def _loc_44F(): pass

    label('loc_44F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_4BF',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 115780, 0, 61020, 228)
    CreateThread(0x000A, 0x00, 0x00, func_05_7B7)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 121030, 0, -58010, 90)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, 116840, 0, -55210, 90)
    CreateThread(0x000C, 0x00, 0x00, func_07_7FF)
    ChrSetPos(0x000D, -3010, 0, -54540, 0)

    Jump('loc_70B')

    def _loc_4BF(): pass

    label('loc_4BF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_537',
    )

    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 123980, 0, 1080, 90)
    CreateThread(0x000A, 0x00, 0x00, func_02_759)
    ChrSetFlags(0x000A, 0x0010)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 126360, 0, 1830, 270)
    ChrSetFlags(0x000B, 0x0010)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetFlags(0x000C, 0x0010)
    ChrSetPos(0x000C, 126360, 0, 740, 270)
    ChrSetPos(0x000D, -960, 0, -55790, 0)

    Jump('loc_70B')

    def _loc_537(): pass

    label('loc_537')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_59B',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 115780, 0, 61020, 228)
    CreateThread(0x000A, 0x00, 0x00, func_05_7B7)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 123540, 0, 68800, 3)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, 113680, 0, -55940, 266)
    CreateThread(0x000C, 0x00, 0x00, func_07_7FF)

    Jump('loc_70B')

    def _loc_59B(): pass

    label('loc_59B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_613',
    )

    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 123980, 0, 1080, 90)
    CreateThread(0x000A, 0x00, 0x00, func_02_759)
    ChrSetFlags(0x000A, 0x0010)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 126360, 0, 1830, 270)
    ChrSetFlags(0x000B, 0x0010)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetFlags(0x000C, 0x0010)
    ChrSetPos(0x000C, 126360, 0, 740, 270)
    ChrSetPos(0x000D, 2380, 0, -55230, 0)

    Jump('loc_70B')

    def _loc_613(): pass

    label('loc_613')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_699',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetChipByIndex(0x000A, 8)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 122730, 250, 64200, 278)
    ChrSetFlags(0x000A, 0x0010)
    ChrSetFlags(0x000A, 0x0004)
    TerminateThread(0x000A, 0xFF)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 113680, 0, -55940, 266)
    CreateThread(0x000B, 0x00, 0x00, func_07_7FF)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetFlags(0x000C, 0x0010)
    ChrSetPos(0x000C, 115850, 0, 60880, 45)
    ChrSetPos(0x000D, -960, 0, -55790, 0)

    Jump('loc_70B')

    def _loc_699(): pass

    label('loc_699')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_70B',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 115780, 0, 61020, 228)
    CreateThread(0x000A, 0x00, 0x00, func_05_7B7)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 123540, 0, 68800, 3)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, 113680, 0, -55940, 266)
    CreateThread(0x000C, 0x00, 0x00, func_07_7FF)
    ChrSetPos(0x000D, 6320, 0, -55580, 91)

    def _loc_70B(): pass

    label('loc_70B')

    Return()

# id: 0x0001 offset: 0x70C
@scena.Code('func_01_70C')
def func_01_70C():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 1, 0x631)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 3, 0x623)),
            Expr.Or,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 3, 0x61B)),
            Expr.Or,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 6, 0x616)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_73F',
    )

    OP_B1('t4111_y')

    Jump('loc_748')

    def _loc_73F(): pass

    label('loc_73F')

    OP_B1('t4111_n')

    def _loc_748(): pass

    label('loc_748')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 2, 0x66A)),
            Expr.Return,
        ),
        'loc_758',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x4B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_758(): pass

    label('loc_758')

    Return()

# id: 0x0002 offset: 0x759
@scena.Code('func_02_759')
def func_02_759():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_76E',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_759')

    def _loc_76E(): pass

    label('loc_76E')

    Return()

# id: 0x0003 offset: 0x76F
@scena.Code('func_03_76F')
def func_03_76F():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_792',
    )

    OP_8D(0x00FE, 59200, 2620, 64319, 1410, 2500)

    Jump('func_03_76F')

    def _loc_792(): pass

    label('loc_792')

    Return()

# id: 0x0004 offset: 0x793
@scena.Code('func_04_793')
def func_04_793():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_7B6',
    )

    OP_8D(0x00FE, 56200, 3180, 64330, 1570, 2500)

    Jump('func_04_793')

    def _loc_7B6(): pass

    label('loc_7B6')

    Return()

# id: 0x0005 offset: 0x7B7
@scena.Code('func_05_7B7')
def func_05_7B7():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_7DA',
    )

    OP_8D(0x00FE, 113710, 62230, 117600, 58990, 3000)

    Jump('func_05_7B7')

    def _loc_7DA(): pass

    label('loc_7DA')

    Return()

# id: 0x0006 offset: 0x7DB
@scena.Code('func_06_7DB')
def func_06_7DB():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_7FE',
    )

    OP_8D(0x00FE, 113710, 62230, 117600, 58990, 6000)

    Jump('func_06_7DB')

    def _loc_7FE(): pass

    label('loc_7FE')

    Return()

# id: 0x0007 offset: 0x7FF
@scena.Code('func_07_7FF')
def func_07_7FF():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_822',
    )

    OP_8D(0x00FE, 113410, -55340, 116360, -56940, 3000)

    Jump('func_07_7FF')

    def _loc_822(): pass

    label('loc_822')

    Return()

# id: 0x0008 offset: 0x823
@scena.Code('func_08_823')
def func_08_823():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_846',
    )

    OP_8D(0x00FE, -6280, 2250, 4250, -530, 3000)

    Jump('func_08_823')

    def _loc_846(): pass

    label('loc_846')

    Return()

# id: 0x0009 offset: 0x847
@scena.Code('func_09_847')
def func_09_847():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_86A',
    )

    OP_8D(0x00FE, -4570, 58630, -30, 63950, 3000)

    Jump('func_09_847')

    def _loc_86A(): pass

    label('loc_86A')

    Return()

# id: 0x000A offset: 0x86B
@scena.Code('func_0A_86B')
def func_0A_86B():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_8BC',
    )

    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '啊，\n',
            '游击士艾丝蒂尔姐姐！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次一定要陪莉安妮玩嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B8D')

    def _loc_8BC(): pass

    label('loc_8BC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_8C6',
    )

    Jump('loc_B8D')

    def _loc_8C6(): pass

    label('loc_8C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_8D0',
    )

    Jump('loc_B8D')

    def _loc_8D0(): pass

    label('loc_8D0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_8DA',
    )

    Jump('loc_B8D')

    def _loc_8DA(): pass

    label('loc_8DA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_926',
    )

    ChrTalk(
        0x00FE,
        (
            '今年爷爷他\n',
            '没有参加比赛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是无聊，\n',
            '还是去外面玩吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B8D')

    def _loc_926(): pass

    label('loc_926')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_963',
    )

    ChrTalk(
        0x00FE,
        (
            '奶奶好像\n',
            '没有什么精神呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '她不要紧吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B8D')

    def _loc_963(): pass

    label('loc_963')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_9BB',
    )

    ChrTalk(
        0x00FE,
        (
            '庆典开始了的话，\n',
            '就能见到大家了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '想见见爷爷，\n',
            '还有公主殿下呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B8D')

    def _loc_9BB(): pass

    label('loc_9BB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_A78',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_A18',
    )

    ChrTalk(
        0x00FE,
        (
            '好久没有这样\n',
            '和奶奶一起去王城里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '还是没能见到公主殿下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A75')

    def _loc_A18(): pass

    label('loc_A18')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '好久没有这样\n',
            '和奶奶一起去王城里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '还是没能见到公主殿下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呜呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A75(): pass

    label('loc_A75')

    Jump('loc_B8D')

    def _loc_A78(): pass

    label('loc_A78')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_AB9',
    )

    ChrTalk(
        0x00FE,
        (
            '我莉安妮啊，\n',
            '和公主可是好朋友哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是真的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B8D')

    def _loc_AB9(): pass

    label('loc_AB9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_AF7',
    )

    ChrTalk(
        0x00FE,
        (
            '呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '爷爷他\n',
            '不知什么时候\n',
            '才能回来啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B8D')

    def _loc_AF7(): pass

    label('loc_AF7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_B8D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_B3B',
    )

    ChrTalk(
        0x00FE,
        (
            '哇～\n',
            '爷爷很快就要回来了呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '快点回来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B8D')

    def _loc_B3B(): pass

    label('loc_B3B')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '哇～\n',
            '爷爷很快就要回来了呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000F, 0x00000000, 1700, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '快点回来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B8D(): pass

    label('loc_B8D')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0xB91
@scena.Code('func_0B_B91')
def func_0B_B91():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_BF5',
    )

    ChrTalk(
        0x00FE,
        (
            '理查德先生\n',
            '曾经几次到这里来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '连我家老爷都\n',
            '称赞过他，\n',
            '真是个了不起的人呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_104A')

    def _loc_BF5(): pass

    label('loc_BF5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_C34',
    )

    ChrTalk(
        0x00FE,
        (
            '莉安妮小姐\n',
            '好像已经被找到了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '太好了～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_104A')

    def _loc_C34(): pass

    label('loc_C34')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_C8E',
    )

    ChrTalk(
        0x00FE,
        (
            '夫人已经委托\n',
            '王国军去搜寻\n',
            '莉安妮小姐的下落了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但还没有什么消息呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_104A')

    def _loc_C8E(): pass

    label('loc_C8E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_C98',
    )

    Jump('loc_104A')

    def _loc_C98(): pass

    label('loc_C98')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_CEF',
    )

    ChrTalk(
        0x00FE,
        (
            '老爷怎么不和我们联络呢，\n',
            '真有点奇怪啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望没出什么事就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_104A')

    def _loc_CEF(): pass

    label('loc_CEF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_D7A',
    )

    ChrTalk(
        0x00FE,
        (
            '夫人还有莉安妮小姐\n',
            '都很期待诞辰庆典的到来，\n',
            '因为只有那个时候老爷才会回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要能够回来，\n',
            '哪怕只是呆上一会儿也好啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_104A')

    def _loc_D7A(): pass

    label('loc_D7A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_DEF',
    )

    ChrTalk(
        0x00FE,
        (
            '每年诞辰庆典\n',
            '老爷他都会受到女王陛下的招待。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '自从战争结束之后，\n',
            '每年的这个时候\n',
            '他都一定会回来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_104A')

    def _loc_DEF(): pass

    label('loc_DEF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_EB2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_E38',
    )

    ChrTalk(
        0x00FE,
        (
            '我在这悄悄告诉你，\n',
            '就算是老爷也\n',
            '不敢惹夫人生气呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EAF')

    def _loc_E38(): pass

    label('loc_E38')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '老爷他发起脾气\n',
            '是很可怕的呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，我在这里悄悄告诉你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算是这样的老爷，\n',
            '也不敢惹夫人呢，呵呵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EAF(): pass

    label('loc_EAF')

    Jump('loc_104A')

    def _loc_EB2(): pass

    label('loc_EB2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_FB5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_F20',
    )

    ChrTalk(
        0x00FE,
        (
            '我在百日战役时\n',
            '失去了双亲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '当时，老爷和夫人\n',
            '收养了无依无靠的我，\n',
            '让我在这里生活。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FB2')

    def _loc_F20(): pass

    label('loc_F20')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '我在百日战役时\n',
            '失去了双亲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '当时，老爷和夫人\n',
            '收养了无依无靠的我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在还让我\n',
            '在这个家里当保姆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我真是太感谢他们两位了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FB2(): pass

    label('loc_FB2')

    Jump('loc_104A')

    def _loc_FB5(): pass

    label('loc_FB5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_101C',
    )

    ChrTalk(
        0x00FE,
        (
            '诞辰庆典就要到了，\n',
            '我本以为老爷肯定\n',
            '就要回来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难道最近工作就\n',
            '那么的繁忙吗～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_104A')

    def _loc_101C(): pass

    label('loc_101C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_104A',
    )

    ChrTalk(
        0x00FE,
        (
            '在老爷回来之前\n',
            '得进行大扫除才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_104A(): pass

    label('loc_104A')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x104E
@scena.Code('func_0C_104E')
def func_0C_104E():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1175',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_10CA',
    )

    ChrTalk(
        0x00FE,
        (
            '他曾经是真心为利贝尔着想的\n',
            '军人之一啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一定是因为这种想法太强烈，\n',
            '才导致采取了这次行动的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1172')

    def _loc_10CA(): pass

    label('loc_10CA')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '那位理查德先生\n',
            '竟然发起了政变……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他曾经是真心为利贝尔着想的\n',
            '军人之一啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一定是因为这种想法太强烈，\n',
            '才导致采取了这次行动的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我是这么认为的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1172(): pass

    label('loc_1172')

    Jump('loc_17AC')

    def _loc_1175(): pass

    label('loc_1175')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_12AC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_11F9',
    )

    ChrTalk(
        0x00FE,
        (
            '就在刚才，\n',
            '收到了游击士协会\n',
            '一位叫艾南的先生的联络。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他说在艾贝尔离宫\n',
            '找到了莉安妮。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是太好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12A9')

    def _loc_11F9(): pass

    label('loc_11F9')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '就在刚才，\n',
            '收到了游击士协会\n',
            '一位叫艾南的先生的联络。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他说在艾贝尔离宫\n',
            '找到了莉安妮。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是太好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果有什么意外的话，\n',
            '我真是无颜面对\n',
            '那孩子的父母……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12A9(): pass

    label('loc_12A9')

    Jump('loc_17AC')

    def _loc_12AC(): pass

    label('loc_12AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_13C3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_12F3',
    )

    ChrTalk(
        0x00FE,
        (
            '身为他的妻子，\n',
            '又是莉安妮的祖母，\n',
            '我必须坚强……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13C0')

    def _loc_12F3(): pass

    label('loc_12F3')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '……我孙女莉安妮\n',
            '昨天傍晚出去以后一直未归。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且和我丈夫\n',
            '也一直联系不上……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我该怎么办啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

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
            '不过，身为他的妻子，\n',
            '又是莉安妮的祖母，\n',
            '我必须坚强……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13C0(): pass

    label('loc_13C0')

    Jump('loc_17AC')

    def _loc_13C3(): pass

    label('loc_13C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_13F0',
    )

    ChrTalk(
        0x00FE,
        (
            '唉，\n',
            '莉安妮跑到哪里去玩了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17AC')

    def _loc_13F0(): pass

    label('loc_13F0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1450',
    )

    ChrTalk(
        0x00FE,
        (
            '女王陛下卧病在床也好，\n',
            '丈夫失去音信也好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎么总是发生\n',
            '这些不好的事情啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17AC')

    def _loc_1450(): pass

    label('loc_1450')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_153A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_14AD',
    )

    ChrTalk(
        0x00FE,
        (
            '我和驻扎在哈肯大门的\n',
            '丈夫怎么也联络不上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到底是\n',
            '发生了什么事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1537')

    def _loc_14AD(): pass

    label('loc_14AD')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '我和驻扎在柏斯哈肯大门的\n',
            '丈夫怎么也联络不上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这种事情自从战争结束后，\n',
            '还从来没有发生过呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到底是\n',
            '发生了什么事啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1537(): pass

    label('loc_1537')

    Jump('loc_17AC')

    def _loc_153A(): pass

    label('loc_153A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_15A7',
    )

    ChrTalk(
        0x00FE,
        (
            '不要说武术大会，\n',
            '丈夫他连诞辰庆典\n',
            '好像都不能回来参加……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天再联系一下他，\n',
            '问问情况吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17AC')

    def _loc_15A7(): pass

    label('loc_15A7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_16C4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_160A',
    )

    ChrTalk(
        0x00FE,
        (
            '以前去看望陛下的时候\n',
            '从来没有被拒绝过啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好担心啊……\n',
            '恐怕病得很重吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16C1')

    def _loc_160A(): pass

    label('loc_160A')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '今天本想去看望女王陛下的，\n',
            '可是到了那里，\n',
            '却被拒绝进城。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然女王陛下\n',
            '以前也曾经\n',
            '生过几次病……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但还从来没有\n',
            '不让人去探望的情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好担心啊……\n',
            '恐怕病得很重吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_16C1(): pass

    label('loc_16C1')

    Jump('loc_17AC')

    def _loc_16C4(): pass

    label('loc_16C4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_1717',
    )

    ChrTalk(
        0x00FE,
        (
            '我今天打算到王城里面\n',
            '去看望女王陛下，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '早点把其他的事情办完吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17AC')

    def _loc_1717(): pass

    label('loc_1717')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_176E',
    )

    ChrTalk(
        0x00FE,
        (
            '他今年\n',
            '没有参加武术大会，\n',
            '是怎么回事呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '会不会是\n',
            '出什么事了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17AC')

    def _loc_176E(): pass

    label('loc_176E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_17AC',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀呀，欢迎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我现在正在为\n',
            '孙女炖牛肉汤呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17AC(): pass

    label('loc_17AC')

    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x17B0
@scena.Code('func_0D_17B0')
def func_0D_17B0():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_17BD',
    )

    Jump('loc_1D15')

    def _loc_17BD(): pass

    label('loc_17BD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_17D7',
    )

    ChrTalk(
        0x00FE,
        (
            '唉…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D15')

    def _loc_17D7(): pass

    label('loc_17D7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_1847',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，这样下去的话，\n',
            '诞辰庆典到底会怎么样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这可是难得遇到的盛大活动，\n',
            '一定要举办才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D15')

    def _loc_1847(): pass

    label('loc_1847')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_18C2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_187B',
    )

    ChrTalk(
        0x00FE,
        (
            '哈～哈～哈，\n',
            '夕阳无限好啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18BF')

    def _loc_187B(): pass

    label('loc_187B')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈～哈～哈，\n',
            '夕阳无限好啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18BF(): pass

    label('loc_18BF')

    Jump('loc_1D15')

    def _loc_18C2(): pass

    label('loc_18C2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1974',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1910',
    )

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '为什么没有一个人叫我起床呢！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是过分。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1971')

    def _loc_1910(): pass

    label('loc_1910')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '这是怎么回事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '今天是武术大会的决赛日，\n',
            '我怎么会睡过头了啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1971(): pass

    label('loc_1971')

    Jump('loc_1D15')

    def _loc_1974(): pass

    label('loc_1974')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_1A8C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_19D5',
    )

    ChrTalk(
        0x00FE,
        (
            '我猜想十有八九\n',
            '特务部队会取得优胜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈～哈～哈，\n',
            '很期待明天的比赛啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A89')

    def _loc_19D5(): pass

    label('loc_19D5')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '哈～哈～哈，\n',
            '明天终于到决赛了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我猜想十有八九\n',
            '特务部队会取得优胜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#009F（哼……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明天要鼓足干劲，\n',
            '九点准时在门口集合。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈～哈～哈，\n',
            '这就去通知她们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A89(): pass

    label('loc_1A89')

    Jump('loc_1D15')

    def _loc_1A8C(): pass

    label('loc_1A8C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_1AD7',
    )

    ChrTalk(
        0x00FE,
        (
            '哈～哈～哈，\n',
            '全员都到齐了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，现在开始点名了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D15')

    def _loc_1AD7(): pass

    label('loc_1AD7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_1B54',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，\n',
            '我可是为比赛捏了一把汗啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明天早晨十点\n',
            '全员依旧要在门口集合。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈～哈～哈，\n',
            '这就去通知她们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D15')

    def _loc_1B54(): pass

    label('loc_1B54')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_1BA1',
    )

    ChrTalk(
        0x00FE,
        (
            '好～的，全员集合了吗～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，\n',
            '现在说明一下今天的任务～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D15')

    def _loc_1BA1(): pass

    label('loc_1BA1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_1CA5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1BEE',
    )

    ChrTalk(
        0x00FE,
        (
            '早晨１０点\n',
            '在门口集合。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '接着大家散步\n',
            '到竞技场去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CA2')

    def _loc_1BEE(): pass

    label('loc_1BEE')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '唔～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '早晨１０点\n',
            '在门口集合。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '然后到咖啡馆\n',
            '去吃点东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '接着大家散步\n',
            '到竞技场去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '好，明天全体家族成员\n',
            '外出观看武术大会～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1CA2(): pass

    label('loc_1CA2')

    Jump('loc_1D15')

    def _loc_1CA5(): pass

    label('loc_1CA5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_1D15',
    )

    ChrTalk(
        0x00FE,
        (
            '哈～哈～哈，\n',
            '武术大会终于要开始了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '毫无疑问，\n',
            '像这种盛大的活动，\n',
            '一定要家族全员全部参与才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D15(): pass

    label('loc_1D15')

    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x1D19
@scena.Code('func_0E_1D19')
def func_0E_1D19():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1D26',
    )

    Jump('loc_20D1')

    def _loc_1D26(): pass

    label('loc_1D26')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_1D79',
    )

    ChrTalk(
        0x00FE,
        (
            '街上的气氛很怪异。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '平常的那些士兵不见了，\n',
            '黑衣士兵却增加了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20D1')

    def _loc_1D79(): pass

    label('loc_1D79')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_1DC0',
    )

    ChrTalk(
        0x00FE,
        (
            '我那老公啊，为了这次诞辰庆典，\n',
            '简直急得上气不接下气了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20D1')

    def _loc_1DC0(): pass

    label('loc_1DC0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_1E00',
    )

    ChrTalk(
        0x00FE,
        (
            '我丈夫在比赛后\n',
            '就连饭也不吃了，\n',
            '一直那个样子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20D1')

    def _loc_1E00(): pass

    label('loc_1E00')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1E57',
    )

    ChrTalk(
        0x00FE,
        (
            '总是那么慌慌张张的，\n',
            '就不能稍稍冷静一点吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '冷静一下又不会惹到谁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20D1')

    def _loc_1E57(): pass

    label('loc_1E57')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_1EDC',
    )

    ChrTalk(
        0x00FE,
        (
            '他那么旺盛的精力\n',
            '到底是从哪里来的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从我们认识开始\n',
            '他就一直是那个样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本来以为年纪大了\n',
            '他能够安分点呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20D1')

    def _loc_1EDC(): pass

    label('loc_1EDC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_1F18',
    )

    ChrTalk(
        0x00FE,
        (
            '最难办的是，\n',
            '越是在这种时候\n',
            '老公的干劲越足。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20D1')

    def _loc_1F18(): pass

    label('loc_1F18')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_1F50',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，\n',
            '今天女儿也很累了，\n',
            '我去帮她做晚饭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20D1')

    def _loc_1F50(): pass

    label('loc_1F50')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_1F93',
    )

    ChrTalk(
        0x00FE,
        (
            '我那老公啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一旦起床了，\n',
            '就要开始搞活动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20D1')

    def _loc_1F93(): pass

    label('loc_1F93')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_206E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1FF8',
    )

    ChrTalk(
        0x00FE,
        (
            '诺琪和她丈夫\n',
            '现在关系处得怎么样呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在柏斯旅行时常常\n',
            '可以听到她的感叹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_206B')

    def _loc_1FF8(): pass

    label('loc_1FF8')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '诺琪和她丈夫\n',
            '现在关系处得怎么样呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在柏斯旅行时常常\n',
            '可以听到她的感叹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像是考虑了许多事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_206B(): pass

    label('loc_206B')

    Jump('loc_20D1')

    def _loc_206E(): pass

    label('loc_206E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_20D1',
    )

    ChrTalk(
        0x00FE,
        (
            '我那老公啊，\n',
            '就是喜欢搞些活动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '武术大会和诞辰庆典就要到了，\n',
            '肯定又要热闹过头的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_20D1(): pass

    label('loc_20D1')

    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x20D5
@scena.Code('func_0F_20D5')
def func_0F_20D5():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_20E2',
    )

    Jump('loc_24F8')

    def _loc_20E2(): pass

    label('loc_20E2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_2176',
    )

    ChrTalk(
        0x00FE,
        (
            '如果诞辰庆典不能举行，\n',
            '那爸爸的情绪就会一直低落下去的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就这么一言不发，\n',
            '会让人很担心的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为我也是这种容易受挫的性格。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24F8')

    def _loc_2176(): pass

    label('loc_2176')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_21A3',
    )

    ChrTalk(
        0x00FE,
        (
            '我家也总算能够\n',
            '消停一阵子了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24F8')

    def _loc_21A3(): pass

    label('loc_21A3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_2220',
    )

    ChrTalk(
        0x00FE,
        (
            '决胜赛时爸爸\n',
            '支持的队伍输了，\n',
            '所以我要做点好吃的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了安慰爸爸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……真是的，\n',
            '总是给人家添些麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24F8')

    def _loc_2220(): pass

    label('loc_2220')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_227E',
    )

    ChrTalk(
        0x00FE,
        (
            '原本我偷偷地\n',
            '把爸爸的闹钟里的\n',
            '导力器取出来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，结果他还是起来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24F8')

    def _loc_227E(): pass

    label('loc_227E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_22E6',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，连续三天\n',
            '陪老爸看武术大会，累死人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '武术大会什么的\n',
            '只要知道个结果不就行了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24F8')

    def _loc_22E6(): pass

    label('loc_22E6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_2347',
    )

    ChrTalk(
        0x00FE,
        (
            '明明是１０点集合，\n',
            '９点前就在大门口\n',
            '转来转去的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '爸爸为什么\n',
            '总是那么紧张呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24F8')

    def _loc_2347(): pass

    label('loc_2347')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_23AD',
    )

    ChrTalk(
        0x00FE,
        (
            '唉～我的爸爸呀，\n',
            '如果我和妈妈说不去的话，\n',
            '就会立刻发脾气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '作女儿的也真是辛苦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24F8')

    def _loc_23AD(): pass

    label('loc_23AD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_247F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_240C',
    )

    ChrTalk(
        0x00FE,
        (
            '我的爸爸呀，\n',
            '总是容易兴奋过头。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那样高度紧张，\n',
            '会导致心脏病爆发的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_247C')

    def _loc_240C(): pass

    label('loc_240C')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '全员……\n',
            '不是只有三人吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我的爸爸呀，\n',
            '总是容易兴奋过头。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那样高度紧张，\n',
            '会导致心脏病爆发的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_247C(): pass

    label('loc_247C')

    Jump('loc_24F8')

    def _loc_247F(): pass

    label('loc_247F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_24AA',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '今年又到这个时期了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24F8')

    def _loc_24AA(): pass

    label('loc_24AA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_24F8',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯～这么多东西啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '家里做饭的工作\n',
            '是由我和妈妈轮流担当的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_24F8(): pass

    label('loc_24F8')

    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x24FC
@scena.Code('func_10_24FC')
def func_10_24FC():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_2624',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_258C',
    )

    ChrTalk(
        0x00FE,
        (
            '我这次终于\n',
            '顺利地通过『钓公师团』的\n',
            '入团测试了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我丈夫又开始上班了，\n',
            '我可以趁这段时间\n',
            '努力缩小和他技术上的差距。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2621')

    def _loc_258C(): pass

    label('loc_258C')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '哦～呵呵呵呵呵！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我这次终于\n',
            '顺利地通过『钓公师团』的\n',
            '入团测试了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我丈夫又开始上班了，\n',
            '我可以趁这段时间\n',
            '努力缩小和他技术上的差距。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2621(): pass

    label('loc_2621')

    Jump('loc_29BC')

    def _loc_2624(): pass

    label('loc_2624')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_272C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_2684',
    )

    ChrTalk(
        0x00FE,
        (
            '现在我也把对家的热情\n',
            '转移到钓鱼上面了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样一来，就会感到快乐了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2729')

    def _loc_2684(): pass

    label('loc_2684')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '哦～呵呵呵呵呵！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '老公只对钓鱼感兴趣，\n',
            '所以现在我也把对家的热情\n',
            '转移到钓鱼上面了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样一来，\n',
            '就会感到快乐了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不知不觉就可以\n',
            '让时间流过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2729(): pass

    label('loc_2729')

    Jump('loc_29BC')

    def _loc_272C(): pass

    label('loc_272C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_2736',
    )

    Jump('loc_29BC')

    def _loc_2736(): pass

    label('loc_2736')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_2740',
    )

    Jump('loc_29BC')

    def _loc_2740(): pass

    label('loc_2740')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_274A',
    )

    Jump('loc_29BC')

    def _loc_274A(): pass

    label('loc_274A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_2754',
    )

    Jump('loc_29BC')

    def _loc_2754(): pass

    label('loc_2754')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_281C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_279E',
    )

    ChrTalk(
        0x00FE,
        (
            '真让人恼火啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '既然这样，\n',
            '我也要想想办法了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2819')

    def _loc_279E(): pass

    label('loc_279E')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '我丈夫一大早\n',
            '又出去钓鱼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '……真让人恼火啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '既然这样，\n',
            '我也要想想办法了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2819(): pass

    label('loc_2819')

    Jump('loc_29BC')

    def _loc_281C(): pass

    label('loc_281C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_286A',
    )

    ChrTalk(
        0x00FE,
        (
            '呼…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我那老公啊，\n',
            '最近就算回到家里\n',
            '也不打声招呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29BC')

    def _loc_286A(): pass

    label('loc_286A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_28CC',
    )

    ChrTalk(
        0x00FE,
        (
            '老公又连招呼都不打\n',
            '就从家里出去了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说什么他也不听，\n',
            '我究竟该怎么办才好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29BC')

    def _loc_28CC(): pass

    label('loc_28CC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_294F',
    )

    ChrTalk(
        0x00FE,
        (
            '我老公因为忙于工作和爱好，\n',
            '不怎么回家来，\n',
            '所以我最近也出去旅行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '前些日子和附近的玛丽安\n',
            '一起到柏斯去玩了玩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29BC')

    def _loc_294F(): pass

    label('loc_294F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_29BC',
    )

    ChrTalk(
        0x00FE,
        (
            '老公难得在家一次，\n',
            '却总是只顾做自己喜欢的事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样真是不知道\n',
            '我们是为了什么生活在一起的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_29BC(): pass

    label('loc_29BC')

    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0x29C0
@scena.Code('func_11_29C0')
def func_11_29C0():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_29CD',
    )

    Jump('loc_2F93')

    def _loc_29CD(): pass

    label('loc_29CD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_2AD8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_2A34',
    )

    ChrTalk(
        0x00FE,
        (
            '唔～虽然心情有点复杂，\n',
            '不过反过来想想平日自己的所作所为，\n',
            '就没办法再抱怨什么了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2AD5')

    def _loc_2A34(): pass

    label('loc_2A34')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '听我说！\n',
            '行踪不明的妻子竟然回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且还有啊，\n',
            '这几天她一直都在练习钓鱼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '虽说刚刚才开始起步，\n',
            '但已经比我技术还好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2AD5(): pass

    label('loc_2AD5')

    Jump('loc_2F93')

    def _loc_2AD8(): pass

    label('loc_2AD8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_2B26',
    )

    ChrTalk(
        0x00FE,
        (
            '哈啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我可以放弃最喜欢的钓鱼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要你能回来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F93')

    def _loc_2B26(): pass

    label('loc_2B26')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_2C14',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_2B94',
    )

    ChrTalk(
        0x00FE,
        (
            '我委托了游击士协会\n',
            '寻找我妻子的行踪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '他们叫我不用担心，\n',
            '说她自己会回家的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C11')

    def _loc_2B94(): pass

    label('loc_2B94')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '我委托游击士协会\n',
            '寻找我妻子的行踪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '他们叫我不用担心，\n',
            '说她自己会回家的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他们会帮我\n',
            '好好寻找吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C11(): pass

    label('loc_2C11')

    Jump('loc_2F93')

    def _loc_2C14(): pass

    label('loc_2C14')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_2C90',
    )

    ChrTalk(
        0x00FE,
        (
            '不、不好了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '妻子昨天下午出门之后，\n',
            '就再也没有回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要、要是被那些\n',
            '恐怖分子给抓走的话怎么办……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F93')

    def _loc_2C90(): pass

    label('loc_2C90')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_2DBA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_2D13',
    )

    ChrTalk(
        0x00FE,
        (
            '唉，\n',
            '我在『钓公师团』的入团测试中落选了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……说起来一大早\n',
            '我就见不到妻子的踪影了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到哪里去了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2DB7')

    def _loc_2D13(): pass

    label('loc_2D13')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '唉，\n',
            '我在『钓公师团』的入团测试中落选了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样的话只有重新磨练技术\n',
            '以后再次挑战了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……说起来一大早\n',
            '我就见不到妻子的踪影了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到哪里去了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2DB7(): pass

    label('loc_2DB7')

    Jump('loc_2F93')

    def _loc_2DBA(): pass

    label('loc_2DBA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_2DC4',
    )

    Jump('loc_2F93')

    def _loc_2DC4(): pass

    label('loc_2DC4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_2E0D',
    )

    ChrTalk(
        0x00FE,
        (
            '据说『钓公师团』\n',
            '正要进行入团测试。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要赶快去试试看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F93')

    def _loc_2E0D(): pass

    label('loc_2E0D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_2E17',
    )

    Jump('loc_2F93')

    def _loc_2E17(): pass

    label('loc_2E17')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_2F32',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_2E9E',
    )

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '市内好像有个名为\n',
            '『钓公师团』的钓鱼爱好者组织呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这是个好机会，\n',
            '趁这次休假的时候\n',
            '到那里去看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F2F')

    def _loc_2E9E(): pass

    label('loc_2E9E')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '市内好像有个名为\n',
            '『钓公师团』的钓鱼爱好者组织呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔，好像很有趣……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这是个好机会，\n',
            '趁这次休假的时候\n',
            '到那里去看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2F2F(): pass

    label('loc_2F2F')

    Jump('loc_2F93')

    def _loc_2F32(): pass

    label('loc_2F32')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_2F93',
    )

    ChrTalk(
        0x00FE,
        (
            '我本来是在王城里工作的，\n',
            '公爵突然就让我休假。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没办法，\n',
            '只有用钓鱼来消磨时间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2F93(): pass

    label('loc_2F93')

    TalkEnd(0x00FE)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

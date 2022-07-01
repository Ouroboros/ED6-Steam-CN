import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import R3102_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R3102   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '大食人花'),
    TXT(0x02, '蔡斯方向'),
    TXT(0x03, '沃尔费堡垒方向'),
    TXT(0x04, '红莲之塔方向'),
    TXT(0x05, ''),
    TXT(0x06, ''),
    TXT(0x07, ''),
    TXT(0x08, ''),
    TXT(0x09, ''),
    TXT(0x0A, ''),
    TXT(0x0B, ''),
    TXT(0x0C, ''),
    TXT(0x0D, ''),
    TXT(0x0E, ''),
    TXT(0x0F, ''),
    TXT(0x10, ''),
    TXT(0x11, ''),
    TXT(0x12, ''),
    TXT(0x13, ''),
    TXT(0x14, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'R3102.x'
    header.mapIndex       = 144
    header.bgm            = 29
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x993
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
            word_3A         = 0,
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
        ('ED6_DT09/CH10610._CH', 'ED6_DT09/CH10610P._CP'),
        ('ED6_DT09/CH10611._CH', 'ED6_DT09/CH10611P._CP'),
        ('ED6_DT09/CH10080._CH', 'ED6_DT09/CH10080P._CP'),
        ('ED6_DT09/CH10081._CH', 'ED6_DT09/CH10081P._CP'),
        ('ED6_DT09/CH10120._CH', 'ED6_DT09/CH10120P._CP'),
        ('ED6_DT09/CH10121._CH', 'ED6_DT09/CH10121P._CP'),
        ('ED6_DT09/CH10140._CH', 'ED6_DT09/CH10140P._CP'),
        ('ED6_DT09/CH10141._CH', 'ED6_DT09/CH10141P._CP'),
        ('ED6_DT09/CH10620._CH', 'ED6_DT09/CH10620P._CP'),
        ('ED6_DT09/CH10621._CH', 'ED6_DT09/CH10621P._CP'),
        ('ED6_DT09/CH10600._CH', 'ED6_DT09/CH10600P._CP'),
        ('ED6_DT09/CH10601._CH', 'ED6_DT09/CH10601P._CP'),
        ('ED6_DT09/CH10400._CH', 'ED6_DT09/CH10400P._CP'),
        ('ED6_DT09/CH10401._CH', 'ED6_DT09/CH10401P._CP'),
        ('ED6_DT09/CH11210._CH', 'ED6_DT09/CH11210P._CP'),
        ('ED6_DT09/CH11211._CH', 'ED6_DT09/CH11211P._CP'),
        ('ED6_DT09/CH11250._CH', 'ED6_DT09/CH11250P._CP'),
        ('ED6_DT09/CH11251._CH', 'ED6_DT09/CH11251P._CP'),
        ('ED6_DT29/CH12090._CH', 'ED6_DT29/CH12090P._CP'),
        ('ED6_DT29/CH12091._CH', 'ED6_DT29/CH12091P._CP'),
    ]

# id: 0x10002 offset: 0x14A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 48380,
            z                   = -90,
            y                   = -10430,
            direction           = 277,
            word_0E             = 18,
            dword_10            = 1179648,
            chipIndex           = 0,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -74130,
            z                   = 0,
            y                   = 3100,
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
            x                   = 64319,
            z                   = 10,
            y                   = -52920,
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
            x                   = 10040,
            z                   = -130,
            y                   = 67800,
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

# id: 0x10003 offset: 0x1CA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -36940,
            z           = -10,
            y           = 10890,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -28070,
            z           = 80,
            y           = 10280,
            word_0C     = 0x00B4,
            word_0E     = 0x000C,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -17490,
            z           = 0,
            y           = -1540,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 4150,
            z           = -60,
            y           = 15540,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 26070,
            z           = -30,
            y           = 28060,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 26690,
            z           = 50,
            y           = 5570,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 13500,
            z           = -20,
            y           = -4890,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 34620,
            z           = -50,
            y           = -10530,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 37440,
            z           = -50,
            y           = -24530,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 15930,
            z           = 0,
            y           = -38970,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -35920,
            z           = -20,
            y           = -35400,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -29740,
            z           = -110,
            y           = -7150,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -19490,
            z           = 0,
            y           = -17710,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 12390,
            z           = 50,
            y           = -16010,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -5230,
            z           = 0,
            y           = -27150,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x36E
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 48380,
            y           = -2000,
            z           = -10430,
            range       = 3000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000003,
        ),
    )

# id: 0x10005 offset: 0x38E
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -3130,
            triggerZ            = 30,
            triggerY            = -11320,
            triggerRange        = 1000,
            actorX              = -3130,
            actorZ              = 30,
            actorY              = -10750,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 13630,
            triggerZ            = 0,
            triggerY            = 35620,
            triggerRange        = 1500,
            actorX              = 13630,
            actorZ              = 1200,
            actorY              = 35620,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 36850,
            triggerZ            = 80,
            triggerY            = 17250,
            triggerRange        = 1000,
            actorX              = 33720,
            actorZ              = -1000,
            actorY              = 13980,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x3FA
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x3FB
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFE0048, 0xFFFE13D0, 0x0023002F)

    ExecExpressionWithVar(
        0x3A,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_71(0x0000, 0x0004)

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            (Expr.Eval, "OP_29(0x006E, 0x00, 0x08)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x006E, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x006E, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4CA',
    )

    If(
        (
            (Expr.GetChrWork, 0x104, 0x1C),
            (Expr.PushLong, 0x5B),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4CA',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4CA',
    )

    OP_CE(
        0x00,
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0xA),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_479',
    )

    OP_28(0x006E, 0x01, 0x0040)

    Jump('loc_4CA')

    def _loc_479(): pass

    label('loc_479')

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_48E',
    )

    OP_28(0x006E, 0x01, 0x0020)

    Jump('loc_4CA')

    def _loc_48E(): pass

    label('loc_48E')

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4A3',
    )

    OP_28(0x006E, 0x01, 0x0010)

    Jump('loc_4CA')

    def _loc_4A3(): pass

    label('loc_4A3')

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4B8',
    )

    OP_28(0x006E, 0x01, 0x0008)

    Jump('loc_4CA')

    def _loc_4B8(): pass

    label('loc_4B8')

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4CA',
    )

    OP_28(0x006E, 0x01, 0x0004)

    def _loc_4CA(): pass

    label('loc_4CA')

    ExecExpressionWithValue(
        0x0008,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 0, 0x1408)),
            Expr.Ez,
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_4F3',
    )

    SetChrFlags(0x0008, 0x0080)
    OP_B2(0x00, 0x00, 0x0080)

    Jump('loc_505')

    def _loc_4F3(): pass

    label('loc_4F3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x029F, 3, 0x14FB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_505',
    )

    ClearChrFlags(0x0008, 0x0080)
    OP_B2(0x01, 0x00, 0x0080)

    def _loc_505(): pass

    label('loc_505')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A0, 6, 0x1506)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_517',
    )

    OP_6F(0x0001, 0)

    Jump('loc_51E')

    def _loc_517(): pass

    label('loc_517')

    OP_6F(0x0001, 60)

    def _loc_51E(): pass

    label('loc_51E')

    Return()

# id: 0x0002 offset: 0x51F
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_534',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('ReInit')

    def _loc_534(): pass

    label('loc_534')

    Return()

# id: 0x0003 offset: 0x535
@scena.Code('func_03_535')
def func_03_535():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x029F, 3, 0x14FB)),
            Expr.Return,
        ),
        'loc_53D',
    )

    Return()

    def _loc_53D(): pass

    label('loc_53D')

    EventBegin(0x01)

    ExecExpressionWithValue(
        0x0000,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0001,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0002,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0003,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0004,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0005,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0006,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0007,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrSubChip(0x0000, 0)
    SetChrSubChip(0x0001, 0)
    SetChrSubChip(0x0002, 0)
    SetChrSubChip(0x0003, 0)
    SetChrSubChip(0x0004, 0)
    SetChrSubChip(0x0005, 0)
    SetChrSubChip(0x0006, 0)
    SetChrSubChip(0x0007, 0)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '大型魔兽正在四处游荡中。',
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
        0,
        (
            TXT(0x00, '【消灭它】\n'),
            TXT(0x01, '【放弃】\n'),
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
        (0x00000001, 'loc_622'),
        (-1, 'loc_645'),
    )

    def _loc_622(): pass

    label('loc_622')

    Fade(500)
    OP_89(0x0000, 41860, -30, -10460, 95)
    OP_69(0x0000, 0x00000000)
    OP_30(0x01)
    OP_0D()
    EventEnd(0x00)

    Return()

    def _loc_645(): pass

    label('loc_645')

    Battle(0x00000EE2, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x01)
    OP_89(0x0000, 41860, -30, -10460, 95)
    OP_69(0x0000, 0x00000000)
    OP_30(0x01)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000002, 'loc_67E'),
        (0x00000001, 'loc_681'),
        (-1, 'loc_684'),
    )

    def _loc_67E(): pass

    label('loc_67E')

    EventEnd(0x00)

    Return()

    def _loc_681(): pass

    label('loc_681')

    OP_B4(0x00)

    Return()

    def _loc_684(): pass

    label('loc_684')

    EventBegin(0x01)
    SetChrFlags(0x0008, 0x0080)
    OP_B2(0x00, 0x00, 0x0080)
    OP_0D()
    Sleep(400)

    OP_22(0x0017, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '消灭了通缉魔兽！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_A2(0x14FB)
    OP_28(0x00A6, 0x04, 0x10)
    OP_28(0x00A6, 0x04, 0x02)
    OP_28(0x00A6, 0x01, 0x0001)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0x6F0
@scena.Code('func_04_6F0')
def func_04_6F0():
    UnlockAchievement(0x02, 0xEF, 0x01, 0x00)
    SetMapFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A0, 6, 0x1506)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_80E',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0001, 0x0000001E)
    OP_73(0x0001)
    OP_6F(0x0001, 30)
    AddSepith(0x00, 0x000A)
    AddSepith(0x01, 0x000A)
    AddSepith(0x02, 0x000A)
    AddSepith(0x03, 0x000A)
    AddSepith(0x04, 0x000A)
    AddSepith(0x05, 0x000A)
    AddSepith(0x06, 0x000A)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#56I地之耀晶片×１０\n',
            (TxtCtl.SetColor, 0x2),
            '#57I水之耀晶片×１０\n',
            (TxtCtl.SetColor, 0x2),
            '#58I火之耀晶片×１０\n',
            (TxtCtl.SetColor, 0x2),
            '#59I风之耀晶片×１０\n',
            (TxtCtl.SetColor, 0x2),
            '#62I时之耀晶片×１０\n',
            (TxtCtl.SetColor, 0x2),
            '#60I空之耀晶片×１０\n',
            (TxtCtl.SetColor, 0x2),
            '#61I幻之耀晶片×１０\n',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1506)

    Jump('loc_828')

    def _loc_80E(): pass

    label('loc_80E')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_828(): pass

    label('loc_828')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x83A
@scena.Code('func_05_83A')
def func_05_83A():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '北　红莲之塔\n',
            '※魔兽较多，请注意！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0006 offset: 0x88E
@scena.Code('func_06_88E')
def func_06_88E():
    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0011860001V#1001F这里好像可以钓上什么来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_08C6')
    def lambda_08C6():
        OP_6D(34900, 70, 15500, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_08C6)

    @scena.Lambda('lambda_08DE')
    def lambda_08DE():
        OP_6B(3250, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_08DE)

    @scena.Lambda('lambda_08EE')
    def lambda_08EE():
        OP_6C(270000, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_08EE)

    Sleep(1000)

    SetChrName('')

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
        'loc_975',
    )

    OP_C0(0x0E, 0x00000023, 0x00008FF2, 0x00000050, 0x00004362, 0x000000E1, 0x000083B8, 0xFFFFFC18, 0x0000369C)
    OP_0D()
    EventEnd(0x01)

    Jump('loc_984')

    def _loc_975(): pass

    label('loc_975')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_984',
    )

    EventEnd(0x01)

    def _loc_984(): pass

    label('loc_984')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import R0102_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R0102   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '亡命守护者'),
    TXT(0x02, '呼啸母兽'),
    TXT(0x03, '洛连特方向'),
    TXT(0x04, '格鲁纳门方向'),
    TXT(0x05, '神秘森林方向'),
    TXT(0x06, '莱诺+赤茶'),
    TXT(0x07, '莱诺+玛兹'),
    TXT(0x08, '帕因+玛兹'),
    TXT(0x09, '莱诺+赤茶'),
    TXT(0x0A, '莱诺+玛兹'),
    TXT(0x0B, '帕因+红茶'),
    TXT(0x0C, '帕因+玛兹'),
    TXT(0x0D, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'R0102.x'
    header.mapIndex       = 23
    header.bgm            = 29
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xC09
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
            word_3A         = 23,
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
        ('ED6_DT09/CH10240._CH', 'ED6_DT09/CH10240P._CP'),
        ('ED6_DT09/CH10241._CH', 'ED6_DT09/CH10241P._CP'),
        ('ED6_DT09/CH10230._CH', 'ED6_DT09/CH10230P._CP'),
        ('ED6_DT09/CH10231._CH', 'ED6_DT09/CH10231P._CP'),
        ('ED6_DT29/CH12320._CH', 'ED6_DT29/CH12320P._CP'),
        ('ED6_DT29/CH12321._CH', 'ED6_DT29/CH12321P._CP'),
        ('ED6_DT09/CH10870._CH', 'ED6_DT09/CH10870P._CP'),
        ('ED6_DT09/CH10871._CH', 'ED6_DT09/CH10871P._CP'),
    ]

# id: 0x10002 offset: 0xEA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -125440,
            z                   = 1000,
            y                   = 20910,
            direction           = 45,
            word_0E             = 4,
            dword_10            = 262144,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -177120,
            z                   = 1000,
            y                   = -18990,
            direction           = 90,
            word_0E             = 6,
            dword_10            = 393216,
            chipIndex           = 0,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -101100,
            z                   = 1000,
            y                   = 83200,
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
            x                   = -205500,
            z                   = 1000,
            y                   = -19070,
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
            x                   = -65750,
            z                   = 1000,
            y                   = 51180,
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

# id: 0x10003 offset: 0x18A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -107000,
            z           = 1000,
            y           = 43000,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0014,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -125000,
            z           = 2000,
            y           = 34000,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0015,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -91000,
            z           = 1000,
            y           = 28000,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0017,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -150000,
            z           = 1000,
            y           = -6000,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0014,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -160000,
            z           = 1000,
            y           = -22000,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0015,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -151000,
            z           = 2000,
            y           = 8000,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0016,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -138000,
            z           = 2000,
            y           = 4000,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0017,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x24E
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -128100,
            y           = -500,
            z           = 18300,
            range       = -122400,
            dword_10    = 0x00000DAC,
            dword_14    = 0x00005BCC,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000004,
        ),
        ScenaEventData(
            x           = -177120,
            y           = 0,
            z           = -18990,
            range       = 2000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000003,
        ),
    )

# id: 0x10005 offset: 0x28E
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -128400,
            triggerZ            = 2020,
            triggerY            = 37060,
            triggerRange        = 1000,
            actorX              = -128970,
            actorZ              = 2070,
            actorY              = 37440,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -132050,
            triggerZ            = 1010,
            triggerY            = 7280,
            triggerRange        = 1000,
            actorX              = -131520,
            actorZ              = 1010,
            actorY              = 6750,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -115130,
            triggerZ            = 970,
            triggerY            = 25940,
            triggerRange        = 1500,
            actorX              = -115130,
            actorZ              = 2700,
            actorY              = 25940,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -163860,
            triggerZ            = 970,
            triggerY            = -7310,
            triggerRange        = 1500,
            actorX              = -163860,
            actorZ              = 2500,
            actorY              = -7310,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x31E
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x31F
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFC1FD0, 0xFFFE5A20, 0x0023000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0322, 2, 0x1912)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_343',
    )

    OP_6F(0x0000, 0)

    Jump('loc_34A')

    def _loc_343(): pass

    label('loc_343')

    OP_6F(0x0000, 60)

    def _loc_34A(): pass

    label('loc_34A')

    OP_64(0x01, 0x0001)
    OP_71(0x0001, 0x0000)
    OP_71(0x0001, 0x0004)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_386',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_386',
    )

    SetMapFlags(0x00000010)
    OP_11(0xE6, 0xF0, 0xFF, 0x00000000, 0x0000EA60, 0x00000000)
    OP_C4(0x00, 0x00000004)

    def _loc_386(): pass

    label('loc_386')

    ExecExpressionWithValue(
        0x0008,
        0x24,
        (
            (Expr.PushLong, 0xE7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Ez,
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_3AF',
    )

    SetChrFlags(0x0009, 0x0080)
    OP_B2(0x00, 0x01, 0x0080)

    Jump('loc_3C1')

    def _loc_3AF(): pass

    label('loc_3AF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x031F, 3, 0x18FB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3C1',
    )

    ClearChrFlags(0x0009, 0x0080)
    OP_B2(0x01, 0x01, 0x0080)

    def _loc_3C1(): pass

    label('loc_3C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_3F0',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x66),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3DB',
    )

    OP_8C(0x0008, 225, 0)

    def _loc_3DB(): pass

    label('loc_3DB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041F, 0, 0x20F8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3ED',
    )

    ClearChrFlags(0x0008, 0x0080)
    OP_B2(0x01, 0x00, 0x0080)

    def _loc_3ED(): pass

    label('loc_3ED')

    Jump('loc_3FA')

    def _loc_3F0(): pass

    label('loc_3F0')

    SetChrFlags(0x0008, 0x0080)
    OP_B2(0x00, 0x00, 0x0080)
    def _loc_3FA(): pass

    label('loc_3FA')

    Return()

# id: 0x0002 offset: 0x3FB
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_410',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('ReInit')

    def _loc_410(): pass

    label('loc_410')

    Return()

# id: 0x0003 offset: 0x411
@scena.Code('func_03_411')
def func_03_411():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x031F, 3, 0x18FB)),
            Expr.Return,
        ),
        'loc_419',
    )

    Return()

    def _loc_419(): pass

    label('loc_419')

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
        (0x00000001, 'loc_4FE'),
        (-1, 'loc_521'),
    )

    def _loc_4FE(): pass

    label('loc_4FE')

    Fade(500)
    OP_89(0x0000, -171270, 1000, -18910, 270)
    OP_69(0x0000, 0x00000000)
    OP_30(0x01)
    OP_0D()
    EventEnd(0x00)

    Return()

    def _loc_521(): pass

    label('loc_521')

    Battle(0x00000EE9, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x01)
    OP_89(0x0000, -171270, 1000, -18910, 270)
    OP_69(0x0000, 0x00000000)
    OP_30(0x01)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000002, 'loc_55A'),
        (0x00000001, 'loc_55D'),
        (-1, 'loc_560'),
    )

    def _loc_55A(): pass

    label('loc_55A')

    EventEnd(0x00)

    Return()

    def _loc_55D(): pass

    label('loc_55D')

    OP_B4(0x00)

    Return()

    def _loc_560(): pass

    label('loc_560')

    EventBegin(0x01)
    SetChrFlags(0x0009, 0x0080)
    OP_B2(0x00, 0x01, 0x0080)
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
    OP_A2(0x18FB)
    OP_28(0x00AD, 0x04, 0x10)
    OP_28(0x00AD, 0x04, 0x02)
    OP_28(0x00AD, 0x01, 0x0001)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0x5CC
@scena.Code('func_04_5CC')
def func_04_5CC():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_5E0'),
        (0x00000065, 'loc_5E0'),
        (0x00000066, 'loc_732'),
        (-1, 'loc_884'),
    )

    def _loc_5E0(): pass

    label('loc_5E0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041F, 0, 0x20F8)),
            Expr.Return,
        ),
        'loc_5E8',
    )

    Return()

    def _loc_5E8(): pass

    label('loc_5E8')

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
        (0x00000001, 'loc_6CD'),
        (-1, 'loc_6F0'),
    )

    def _loc_6CD(): pass

    label('loc_6CD')

    Fade(500)
    OP_89(0x0000, -121320, 1000, 25970, 219)
    OP_69(0x0000, 0x00000000)
    OP_30(0x01)
    OP_0D()
    EventEnd(0x00)

    Return()

    def _loc_6F0(): pass

    label('loc_6F0')

    Battle(0x00000EEF, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x01)
    OP_89(0x0000, -121320, 1000, 25970, 219)
    OP_69(0x0000, 0x00000000)
    OP_30(0x01)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000002, 'loc_729'),
        (0x00000001, 'loc_72C'),
        (-1, 'loc_72F'),
    )

    def _loc_729(): pass

    label('loc_729')

    EventEnd(0x00)

    Return()

    def _loc_72C(): pass

    label('loc_72C')

    OP_B4(0x00)

    Return()

    def _loc_72F(): pass

    label('loc_72F')

    Jump('loc_884')

    def _loc_732(): pass

    label('loc_732')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041F, 0, 0x20F8)),
            Expr.Return,
        ),
        'loc_73A',
    )

    Return()

    def _loc_73A(): pass

    label('loc_73A')

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
        (0x00000001, 'loc_81F'),
        (-1, 'loc_842'),
    )

    def _loc_81F(): pass

    label('loc_81F')

    Fade(500)
    OP_89(0x0000, -129910, 1020, 17100, 49)
    OP_69(0x0000, 0x00000000)
    OP_30(0x01)
    OP_0D()
    EventEnd(0x00)

    Return()

    def _loc_842(): pass

    label('loc_842')

    Battle(0x00000EF8, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x01)
    OP_89(0x0000, -129910, 1020, 17100, 49)
    OP_69(0x0000, 0x00000000)
    OP_30(0x01)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000002, 'loc_87B'),
        (0x00000001, 'loc_87E'),
        (-1, 'loc_881'),
    )

    def _loc_87B(): pass

    label('loc_87B')

    EventEnd(0x00)

    Return()

    def _loc_87E(): pass

    label('loc_87E')

    OP_B4(0x00)

    Return()

    def _loc_881(): pass

    label('loc_881')

    Jump('loc_884')

    def _loc_884(): pass

    label('loc_884')

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
    OP_A2(0x20F8)
    OP_28(0x00B7, 0x04, 0x10)
    OP_28(0x00B7, 0x04, 0x02)
    OP_28(0x00B7, 0x01, 0x0001)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x00)

    Return()

# id: 0x0005 offset: 0x8F0
@scena.Code('func_05_8F0')
def func_05_8F0():
    UnlockAchievement(0x02, 0xBF, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0322, 2, 0x1912)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9CD',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0000, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['棕榈之药'], 1)"),
            Expr.Return,
        ),
        'loc_964',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['棕榈之药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1912)

    Jump('loc_9CA')

    def _loc_964(): pass

    label('loc_964')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['棕榈之药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['棕榈之药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0x00000000)

    def _loc_9CA(): pass

    label('loc_9CA')

    Jump('loc_9FE')

    def _loc_9CD(): pass

    label('loc_9CD')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_9FE(): pass

    label('loc_9FE')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0xA0C
@scena.Code('func_06_A0C')
def func_06_A0C():
    UnlockAchievement(0x02, 0xC0, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0322, 3, 0x1913)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AE9',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0001, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['绝缘胶带'], 1)"),
            Expr.Return,
        ),
        'loc_A80',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['绝缘胶带']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1913)

    Jump('loc_AE6')

    def _loc_A80(): pass

    label('loc_A80')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['绝缘胶带']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['绝缘胶带']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0x00000000)

    def _loc_AE6(): pass

    label('loc_AE6')

    Jump('loc_B1A')

    def _loc_AE9(): pass

    label('loc_AE9')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_B1A(): pass

    label('loc_B1A')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0xB28
@scena.Code('func_07_B28')
def func_07_B28():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '东　神秘森林\n',
            '※魔兽很多，危险！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0008 offset: 0xB7A
@scena.Code('func_08_B7A')
def func_08_B7A():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '北　洛连特市　　　３０８塞尔矩\n',
            '西　王都格兰赛尔　１９３塞尔矩\n',
            '　　格鲁纳门',
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

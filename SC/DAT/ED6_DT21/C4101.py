import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C4101_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C4101   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'C4101.x'
    header.mapIndex       = 1
    header.bgm            = 21
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
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
        ('ED6_DT09/CH10780._CH', 'ED6_DT09/CH10780P._CP'),
        ('ED6_DT09/CH10781._CH', 'ED6_DT09/CH10781P._CP'),
        ('ED6_DT09/CH10790._CH', 'ED6_DT09/CH10790P._CP'),
        ('ED6_DT09/CH10791._CH', 'ED6_DT09/CH10791P._CP'),
        ('ED6_DT09/CH10050._CH', 'ED6_DT09/CH10050P._CP'),
        ('ED6_DT09/CH10051._CH', 'ED6_DT09/CH10051P._CP'),
        ('ED6_DT09/CH10800._CH', 'ED6_DT09/CH10800P._CP'),
        ('ED6_DT09/CH10801._CH', 'ED6_DT09/CH10801P._CP'),
        ('ED6_DT09/CH10810._CH', 'ED6_DT09/CH10810P._CP'),
        ('ED6_DT09/CH10811._CH', 'ED6_DT09/CH10811P._CP'),
        ('ED6_DT09/CH10820._CH', 'ED6_DT09/CH10820P._CP'),
        ('ED6_DT09/CH10821._CH', 'ED6_DT09/CH10821P._CP'),
        ('ED6_DT09/CH11220._CH', 'ED6_DT09/CH11220P._CP'),
        ('ED6_DT09/CH11221._CH', 'ED6_DT09/CH11221P._CP'),
        ('ED6_DT09/CH11230._CH', 'ED6_DT09/CH11230P._CP'),
        ('ED6_DT09/CH11231._CH', 'ED6_DT09/CH11231P._CP'),
        ('ED6_DT29/CH12470._CH', 'ED6_DT29/CH12470P._CP'),
        ('ED6_DT29/CH12471._CH', 'ED6_DT29/CH12471P._CP'),
        ('ED6_DT09/CH10610._CH', 'ED6_DT09/CH10610P._CP'),
        ('ED6_DT09/CH10611._CH', 'ED6_DT09/CH10611P._CP'),
    ]

# id: 0x10001 offset: 0x14A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '大仙人掌',
            x                   = -25480,
            z                   = 0,
            y                   = -5450,
            direction           = 180,
            word_0E             = 16,
            dword_10            = 1048576,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '金甲犀牛',
            x                   = -59440,
            z                   = 0,
            y                   = -18470,
            direction           = 270,
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
            name                = '金甲犀牛',
            x                   = 4320,
            z                   = 0,
            y                   = -16850,
            direction           = 90,
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
            name                = '庭园大道方向',
            x                   = 62880,
            z                   = 0,
            y                   = 55500,
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
            name                = '艾尔贝离宫方向',
            x                   = -25910,
            z                   = 0,
            y                   = 25290,
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
            x                   = -107380,
            z                   = 0,
            y                   = -10960,
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

# id: 0x10002 offset: 0x20A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '凶暴巨鳄',
            x           = 54960,
            z           = 20,
            y           = 1810,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x025C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '沼泽剑齿吸血魔',
            x           = 39700,
            z           = 70,
            y           = -19490,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x025B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '鳄鱼',
            x           = 18160,
            z           = 10,
            y           = -7650,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x025D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '地狱火爆麻雀',
            x           = -32450,
            z           = 20,
            y           = -19130,
            word_0C     = 0x00B4,
            word_0E     = 0x000C,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x025F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '迅猛小鹫',
            x           = -30720,
            z           = -20,
            y           = -16340,
            word_0C     = 0x00B4,
            word_0E     = 0x000E,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0260,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '丘陵毒蜂',
            x           = 14990,
            z           = 0,
            y           = -58900,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0259,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '丘陵毒蜂',
            x           = 4590,
            z           = 0,
            y           = -60490,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0259,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '丘陵毒蜂',
            x           = 6970,
            z           = 0,
            y           = -47290,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0259,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x2EA
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -25480,
            y           = -500,
            z           = -5450,
            range       = 2000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000005,
        ),
        ScenaEventData(
            x           = -62000,
            y           = 0,
            z           = -25360,
            range       = -58270,
            dword_10    = 0x00000BB8,
            dword_14    = 0xFFFFD99A,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000003,
        ),
        ScenaEventData(
            x           = 2500,
            y           = 0,
            z           = -24310,
            range       = 7000,
            dword_10    = 0x00000BB8,
            dword_14    = 0xFFFFE462,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000004,
        ),
    )

# id: 0x10004 offset: 0x34A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -18470,
            triggerZ            = 0,
            triggerY            = -5070,
            triggerRange        = 1500,
            actorX              = -18470,
            actorZ              = 1700,
            actorY              = -5070,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 9670,
            triggerZ            = 500,
            triggerY            = -54320,
            triggerRange        = 1500,
            actorX              = 9670,
            actorZ              = 4000,
            actorY              = -54320,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x392
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3CA',
    )

    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0014, 0x0080)
    ChrSetFlags(0x0015, 0x0080)

    def _loc_3CA(): pass

    label('loc_3CA')

    Return()

# id: 0x0001 offset: 0x3CB
@scena.Code('func_01_3CB')
def func_01_3CB():
    OP_16(0x02, 4000, -140000, -140000, 2293860)

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
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 5, 0x1625)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_41C',
    )

    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0014, 0x0080)
    ChrSetFlags(0x0015, 0x0080)

    def _loc_41C(): pass

    label('loc_41C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Ez,
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_444',
    )

    ChrSetFlags(0x0009, 0x0080)
    OP_B2(0x00, 0x01, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    OP_B2(0x00, 0x01, 0x0080)

    Jump('loc_468')

    def _loc_444(): pass

    label('loc_444')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02DF, 4, 0x16FC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_456',
    )

    ChrClearFlags(0x0009, 0x0080)
    OP_B2(0x01, 0x01, 0x0080)

    def _loc_456(): pass

    label('loc_456')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02DF, 4, 0x16FC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_468',
    )

    ChrClearFlags(0x000A, 0x0080)
    OP_B2(0x01, 0x01, 0x0080)

    def _loc_468(): pass

    label('loc_468')

    OP_B2(0x00, 0x00, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            (Expr.TestScenaFlags, ScenaFlag(0x041F, 7, 0x20FF)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_483',
    )

    ChrClearFlags(0x0008, 0x0080)
    OP_B2(0x01, 0x00, 0x0080)

    def _loc_483(): pass

    label('loc_483')

    Return()

# id: 0x0002 offset: 0x484
@scena.Code('func_02_484')
def func_02_484():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_499',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_484')

    def _loc_499(): pass

    label('loc_499')

    Return()

# id: 0x0003 offset: 0x49A
@scena.Code('func_03_49A')
def func_03_49A():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            (Expr.TestScenaFlags, ScenaFlag(0x02DF, 4, 0x16FC)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_665',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02DF, 4, 0x16FC)),
            Expr.Return,
        ),
        'loc_4AE',
    )

    Return()

    def _loc_4AE(): pass

    label('loc_4AE')

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

    ChrSetSubChip(0x0000, 0)
    ChrSetSubChip(0x0001, 0)
    ChrSetSubChip(0x0002, 0)
    ChrSetSubChip(0x0003, 0)
    ChrSetSubChip(0x0004, 0)
    ChrSetSubChip(0x0005, 0)
    ChrSetSubChip(0x0006, 0)
    ChrSetSubChip(0x0007, 0)
    TalkSetChrName('')

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
        (0x00000001, 'loc_593'),
        (-1, 'loc_5B6'),
    )

    def _loc_593(): pass

    label('loc_593')

    Fade(500)
    OP_89(0x0000, -64379, 0, -18250, 90)
    OP_69(0x0000, 0)
    OP_30(0x01)
    OP_0D()
    EventEnd(0x00)

    Return()

    def _loc_5B6(): pass

    label('loc_5B6')

    Battle(0x00000EE6, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x01)
    OP_89(0x0000, -64379, 0, -18250, 90)
    OP_69(0x0000, 0)
    OP_30(0x01)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000002, 'loc_5EF'),
        (0x00000001, 'loc_5F2'),
        (-1, 'loc_5F5'),
    )

    def _loc_5EF(): pass

    label('loc_5EF')

    EventEnd(0x00)

    Return()

    def _loc_5F2(): pass

    label('loc_5F2')

    OP_B4(0x00)

    Return()

    def _loc_5F5(): pass

    label('loc_5F5')

    EventBegin(0x01)
    ChrSetFlags(0x0009, 0x0080)
    OP_B2(0x00, 0x01, 0x0080)
    OP_0D()
    Sleep(400)

    PlaySE(23, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '消灭了通缉魔兽！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetScenaFlags(ScenaFlag(0x02DF, 4, 0x16FC))
    OP_28(0x00AA, 0x04, 0x10)
    OP_28(0x00AA, 0x04, 0x02)
    OP_28(0x00AA, 0x01, 0x0001)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x00)
    ChrSetFlags(0x000A, 0x0080)

    def _loc_665(): pass

    label('loc_665')

    Return()

# id: 0x0004 offset: 0x666
@scena.Code('func_04_666')
def func_04_666():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            (Expr.TestScenaFlags, ScenaFlag(0x02DF, 4, 0x16FC)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_831',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02DF, 4, 0x16FC)),
            Expr.Return,
        ),
        'loc_67A',
    )

    Return()

    def _loc_67A(): pass

    label('loc_67A')

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

    ChrSetSubChip(0x0000, 0)
    ChrSetSubChip(0x0001, 0)
    ChrSetSubChip(0x0002, 0)
    ChrSetSubChip(0x0003, 0)
    ChrSetSubChip(0x0004, 0)
    ChrSetSubChip(0x0005, 0)
    ChrSetSubChip(0x0006, 0)
    ChrSetSubChip(0x0007, 0)
    TalkSetChrName('')

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
        (0x00000001, 'loc_75F'),
        (-1, 'loc_782'),
    )

    def _loc_75F(): pass

    label('loc_75F')

    Fade(500)
    OP_89(0x0000, 9120, 0, -16700, 270)
    OP_69(0x0000, 0)
    OP_30(0x01)
    OP_0D()
    EventEnd(0x00)

    Return()

    def _loc_782(): pass

    label('loc_782')

    Battle(0x00000EDC, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x01)
    OP_89(0x0000, 9120, 0, -16700, 270)
    OP_69(0x0000, 0)
    OP_30(0x01)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000002, 'loc_7BB'),
        (0x00000001, 'loc_7BE'),
        (-1, 'loc_7C1'),
    )

    def _loc_7BB(): pass

    label('loc_7BB')

    EventEnd(0x00)

    Return()

    def _loc_7BE(): pass

    label('loc_7BE')

    OP_B4(0x00)

    Return()

    def _loc_7C1(): pass

    label('loc_7C1')

    EventBegin(0x01)
    ChrSetFlags(0x000A, 0x0080)
    OP_B2(0x00, 0x01, 0x0080)
    OP_0D()
    Sleep(400)

    PlaySE(23, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '消灭了通缉魔兽！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetScenaFlags(ScenaFlag(0x02DF, 4, 0x16FC))
    OP_28(0x00AA, 0x04, 0x10)
    OP_28(0x00AA, 0x04, 0x02)
    OP_28(0x00AA, 0x01, 0x0001)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x00)
    ChrSetFlags(0x0009, 0x0080)

    def _loc_831(): pass

    label('loc_831')

    Return()

# id: 0x0005 offset: 0x832
@scena.Code('func_05_832')
def func_05_832():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041F, 7, 0x20FF)),
            Expr.Return,
        ),
        'loc_83A',
    )

    Return()

    def _loc_83A(): pass

    label('loc_83A')

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

    ChrSetSubChip(0x0000, 0)
    ChrSetSubChip(0x0001, 0)
    ChrSetSubChip(0x0002, 0)
    ChrSetSubChip(0x0003, 0)
    ChrSetSubChip(0x0004, 0)
    ChrSetSubChip(0x0005, 0)
    ChrSetSubChip(0x0006, 0)
    ChrSetSubChip(0x0007, 0)
    TalkSetChrName('')

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
        (0x00000001, 'loc_91F'),
        (-1, 'loc_942'),
    )

    def _loc_91F(): pass

    label('loc_91F')

    Fade(500)
    OP_89(0x0000, -25500, 0, -11130, 357)
    OP_69(0x0000, 0)
    OP_30(0x01)
    OP_0D()
    EventEnd(0x00)

    Return()

    def _loc_942(): pass

    label('loc_942')

    Battle(0x00000EF6, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x01)
    OP_89(0x0000, -25500, 0, -11130, 357)
    OP_69(0x0000, 0)
    OP_30(0x01)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000002, 'loc_97B'),
        (0x00000001, 'loc_97E'),
        (-1, 'loc_981'),
    )

    def _loc_97B(): pass

    label('loc_97B')

    EventEnd(0x00)

    Return()

    def _loc_97E(): pass

    label('loc_97E')

    OP_B4(0x00)

    Return()

    def _loc_981(): pass

    label('loc_981')

    EventBegin(0x01)
    ChrSetFlags(0x0008, 0x0080)
    OP_B2(0x00, 0x00, 0x0080)
    OP_0D()
    Sleep(400)

    PlaySE(23, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '消灭了通缉魔兽！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetScenaFlags(ScenaFlag(0x041F, 7, 0x20FF))
    OP_28(0x00BE, 0x04, 0x10)
    OP_28(0x00BE, 0x04, 0x02)
    OP_28(0x00BE, 0x01, 0x0001)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x00)

    Return()

# id: 0x0006 offset: 0x9ED
@scena.Code('func_06_9ED')
def func_06_9ED():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '北　艾尔贝离宫\n',
            '西　圣海姆门　　２２４塞尔矩\n',
            '东　格鲁纳门　　２５６塞尔矩',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0007 offset: 0xA68
@scena.Code('func_07_A68')
def func_07_A68():
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '竖立着古老的琥耀石石碑。',
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

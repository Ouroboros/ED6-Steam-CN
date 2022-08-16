import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import R2201_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R2201   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'R2201.x'
    header.mapIndex       = 101
    header.bgm            = 29
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
        ('ED6_DT09/CH10160._CH', 'ED6_DT09/CH10160P._CP'),
        ('ED6_DT09/CH10161._CH', 'ED6_DT09/CH10161P._CP'),
        ('ED6_DT09/CH10450._CH', 'ED6_DT09/CH10450P._CP'),
        ('ED6_DT09/CH10451._CH', 'ED6_DT09/CH10451P._CP'),
        ('ED6_DT09/CH10220._CH', 'ED6_DT09/CH10220P._CP'),
        ('ED6_DT09/CH10221._CH', 'ED6_DT09/CH10221P._CP'),
        ('ED6_DT09/CH10470._CH', 'ED6_DT09/CH10470P._CP'),
        ('ED6_DT09/CH10471._CH', 'ED6_DT09/CH10471P._CP'),
        ('ED6_DT09/CH10480._CH', 'ED6_DT09/CH10480P._CP'),
        ('ED6_DT09/CH10481._CH', 'ED6_DT09/CH10481P._CP'),
        ('ED6_DT09/CH10160._CH', 'ED6_DT09/CH10160P._CP'),
        ('ED6_DT09/CH10161._CH', 'ED6_DT09/CH10160P._CP'),
        ('ED6_DT09/CH10460._CH', 'ED6_DT09/CH10460P._CP'),
        ('ED6_DT09/CH10461._CH', 'ED6_DT09/CH10461P._CP'),
        ('ED6_DT27/CH03100._CH', 'ED6_DT27/CH03100P._CP'),
        ('ED6_DT07/CH02120._CH', 'ED6_DT07/CH02120P._CP'),
        ('ED6_DT07/CH02110._CH', 'ED6_DT07/CH02110P._CP'),
        ('ED6_DT26/CH20390._CH', 'ED6_DT26/CH20390P._CP'),
        ('ED6_DT26/CH20389._CH', 'ED6_DT26/CH20389P._CP'),
        ('ED6_DT26/CH20388._CH', 'ED6_DT26/CH20388P._CP'),
        ('ED6_DT26/CH20391._CH', 'ED6_DT26/CH20391P._CP'),
        ('ED6_DT26/CH20407._CH', 'ED6_DT26/CH20407P._CP'),
        ('ED6_DT09/CH11030._CH', 'ED6_DT09/CH11030P._CP'),
        ('ED6_DT09/CH11031._CH', 'ED6_DT09/CH11031P._CP'),
    ]

# id: 0x10001 offset: 0x16A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '飞球',
            x                   = 73200,
            z                   = -6020,
            y                   = -15060,
            direction           = 147,
            word_0E             = 22,
            dword_10            = 1441792,
            chipIndex           = 0,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '飞船',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '飞船',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '乔丝特',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '吉尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '多伦',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '玛诺利亚村方向',
            x                   = -5600,
            z                   = -2000,
            y                   = 30080,
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
            name                = '卢安方向',
            x                   = 117910,
            z                   = -2020,
            y                   = -87790,
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

# id: 0x10002 offset: 0x26A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = 36840,
            z           = -2000,
            y           = 16600,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x017D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 41480,
            z           = -6090,
            y           = 11430,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0187,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 83840,
            z           = -2000,
            y           = -19430,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x017F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 103150,
            z           = -6030,
            y           = -53480,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0188,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 73280,
            z           = -5940,
            y           = -40040,
            word_0C     = 0x00B4,
            word_0E     = 0x000C,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x018D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x2F6
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 73200,
            y           = -7000,
            z           = -15060,
            range       = 2000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000003,
        ),
    )

# id: 0x10004 offset: 0x316
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 79840,
            triggerZ            = -6030,
            triggerY            = -14200,
            triggerRange        = 1000,
            actorX              = 80360,
            actorZ              = -6040,
            actorY              = -13800,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 112050,
            triggerZ            = -6010,
            triggerY            = -68270,
            triggerRange        = 1000,
            actorX              = 112550,
            actorZ              = -5940,
            actorY              = -68770,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 66590,
            triggerZ            = -6050,
            triggerY            = -4800,
            triggerRange        = 1000,
            actorX              = 65960,
            actorZ              = -5100,
            actorY              = -4960,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 55480,
            triggerZ            = -6680,
            triggerY            = -65900,
            triggerRange        = 5000,
            actorX              = 55480,
            actorZ              = -6680,
            actorY              = -65900,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0013,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x3A6
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_3C2',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    OP_B5(0x00)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x5B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_07_A0E)

    Jump('loc_3F7')

    def _loc_3C2(): pass

    label('loc_3C2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Return,
        ),
        'loc_3DE',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    OP_B5(0x00)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x75),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_08_2F8A)

    Jump('loc_3F7')

    def _loc_3DE(): pass

    label('loc_3DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_3F7',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    OP_B5(0x00)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x75),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_12_3F56)

    def _loc_3F7(): pass

    label('loc_3F7')

    Return()

# id: 0x0001 offset: 0x3F8
@scena.Code('func_01_3F8')
def func_01_3F8():
    OP_16(0x02, 4000, -67000, -155000, 2293799)

    ExecExpressionWithVar(
        0x2A,
        (
            (Expr.PushLong, 0x186A),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlaySE(456, 0x01, 0x64)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x6),
            Expr.Neq,
            (Expr.TestScenaFlags, ScenaFlag(0x0385, 0, 0x1C28)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_436',
    )

    OP_B1('R2201_1')

    Jump('loc_43F')

    def _loc_436(): pass

    label('loc_436')

    OP_B1('R2201_2')

    def _loc_43F(): pass

    label('loc_43F')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_451',
    )

    OP_10(0x00, 0x00)
    OP_10(0x02, 0x01)

    def _loc_451(): pass

    label('loc_451')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0260, 4, 0x1304)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_463',
    )

    OP_6F(0x0000, 0)

    Jump('loc_46A')

    def _loc_463(): pass

    label('loc_463')

    OP_6F(0x0000, 60)

    def _loc_46A(): pass

    label('loc_46A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0260, 5, 0x1305)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_47C',
    )

    OP_6F(0x0001, 0)

    Jump('loc_483')

    def _loc_47C(): pass

    label('loc_47C')

    OP_6F(0x0001, 60)

    def _loc_483(): pass

    label('loc_483')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0260, 6, 0x1306)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_495',
    )

    OP_6F(0x0002, 0)

    Jump('loc_49C')

    def _loc_495(): pass

    label('loc_495')

    OP_6F(0x0002, 60)

    def _loc_49C(): pass

    label('loc_49C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Ez,
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_4BA',
    )

    ChrSetFlags(0x0008, 0x0080)
    OP_B2(0x00, 0x00, 0x0080)

    Jump('loc_4CC')

    def _loc_4BA(): pass

    label('loc_4BA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x025F, 4, 0x12FC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4CC',
    )

    ChrClearFlags(0x0008, 0x0080)
    OP_B2(0x01, 0x00, 0x0080)

    def _loc_4CC(): pass

    label('loc_4CC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0395, 1, 0x1CA9)),
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4E8',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_23(0x01C8)

    def _loc_4E8(): pass

    label('loc_4E8')

    Return()

# id: 0x0002 offset: 0x4E9
@scena.Code('func_02_4E9')
def func_02_4E9():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4FE',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_4E9')

    def _loc_4FE(): pass

    label('loc_4FE')

    Return()

# id: 0x0003 offset: 0x4FF
@scena.Code('func_03_4FF')
def func_03_4FF():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x025F, 4, 0x12FC)),
            Expr.Return,
        ),
        'loc_507',
    )

    Return()

    def _loc_507(): pass

    label('loc_507')

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
        (0x00000001, 'loc_5EC'),
        (-1, 'loc_60F'),
    )

    def _loc_5EC(): pass

    label('loc_5EC')

    Fade(500)
    OP_89(0x0000, 76640, -6000, -19790, 319)
    OP_69(0x0000, 0)
    OP_30(0x01)
    OP_0D()
    EventEnd(0x00)

    Return()

    def _loc_60F(): pass

    label('loc_60F')

    Battle(0x00000EDF, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x01)
    OP_89(0x0000, 76640, -6000, -19790, 319)
    OP_69(0x0000, 0)
    OP_30(0x01)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000002, 'loc_648'),
        (0x00000001, 'loc_64B'),
        (-1, 'loc_64E'),
    )

    def _loc_648(): pass

    label('loc_648')

    EventEnd(0x00)

    Return()

    def _loc_64B(): pass

    label('loc_64B')

    OP_B4(0x00)

    Return()

    def _loc_64E(): pass

    label('loc_64E')

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
    SetScenaFlags(ScenaFlag(0x025F, 4, 0x12FC))
    OP_28(0x00A3, 0x04, 0x10)
    OP_28(0x00A3, 0x04, 0x02)
    OP_28(0x00A3, 0x01, 0x0001)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0x6BA
@scena.Code('func_04_6BA')
def func_04_6BA():
    UnlockAchievement(0x02, 0x01E2, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0260, 4, 0x1304)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_797',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['绝缘胶带'], 1)"),
            Expr.Return,
        ),
        'loc_72E',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

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
    SetScenaFlags(ScenaFlag(0x0260, 4, 0x1304))

    Jump('loc_794')

    def _loc_72E(): pass

    label('loc_72E')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

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
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0)

    def _loc_794(): pass

    label('loc_794')

    Jump('loc_7C8')

    def _loc_797(): pass

    label('loc_797')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

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
    def _loc_7C8(): pass

    label('loc_7C8')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x7D6
@scena.Code('func_05_7D6')
def func_05_7D6():
    UnlockAchievement(0x02, 0x01E3, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0260, 5, 0x1305)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8B3',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['海参'], 1)"),
            Expr.Return,
        ),
        'loc_84A',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['海参']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0260, 5, 0x1305))

    Jump('loc_8B0')

    def _loc_84A(): pass

    label('loc_84A')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['海参']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['海参']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0)

    def _loc_8B0(): pass

    label('loc_8B0')

    Jump('loc_8E4')

    def _loc_8B3(): pass

    label('loc_8B3')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

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
    def _loc_8E4(): pass

    label('loc_8E4')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x8F2
@scena.Code('func_06_8F2')
def func_06_8F2():
    UnlockAchievement(0x02, 0x01E4, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0260, 6, 0x1306)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9CF',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['薄底船鞋'], 1)"),
            Expr.Return,
        ),
        'loc_966',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['薄底船鞋']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0260, 6, 0x1306))

    Jump('loc_9CC')

    def _loc_966(): pass

    label('loc_966')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['薄底船鞋']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['薄底船鞋']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0)

    def _loc_9CC(): pass

    label('loc_9CC')

    Jump('loc_A00')

    def _loc_9CF(): pass

    label('loc_9CF')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

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
    def _loc_A00(): pass

    label('loc_A00')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0xA0E
@scena.Code('func_07_A0E')
def func_07_A0E():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_DB()
    StopEffect(0x80, 0x00)
    CameraMove(13200, 10570, 10650, 0)
    OP_67(0, 13040, -10000, 0)
    CameraSetDistance(2480, 0)
    OP_6C(68000, 0)
    OP_6E(665, 0)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    OP_72(0x0003, 0x0004)
    OP_A1(0x0009, 0x0003)
    ChrSetFlags(0x0009, 0x0004)
    ChrSetFlags(0x0009, 0x0040)
    ChrSetPos(0x0009, 51850, -7500, -42660, 265)
    OP_72(0x0003, 0x0020)
    OP_6F(0x0003, 1140)
    LoadEffect(0x00, 'map\\\\mp021_00.eff')

    @scena.Lambda('lambda_0AB0')
    def lambda_0AB0():
        CameraMove(42720, 10570, -45970, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0AB0)

    OP_C8(0x0200, 0x0046, 'C_PLAC18._CH', 0x01, 0x07D0)
    ShowPlaceName('梅威海道')
    FadeIn(2000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0000)
    Fade(500)
    CameraMove(52300, -4200, -42780, 0)
    OP_67(0, 10000, -10000, 0)
    CameraSetDistance(3250, 0)
    OP_6C(224000, 0)
    OP_6E(589, 0)
    Sleep(1300)

    PlaySE(253, 0x00, 0x64)
    OP_B0(0x0003, 0x32)
    OP_6F(0x0003, 1140)
    OP_70(0x0003, 1200)
    OP_73(0x0003)

    @scena.Lambda('lambda_0B57')
    def lambda_0B57():
        CameraMove(65000, -5990, -39540, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0B57)

    @scena.Lambda('lambda_0B6F')
    def lambda_0B6F():
        OP_67(0, 8800, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0B6F)

    @scena.Lambda('lambda_0B87')
    def lambda_0B87():
        OP_6C(232000, 8000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0B87)

    @scena.Lambda('lambda_0B97')
    def lambda_0B97():
        OP_6E(287, 8000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_0B97)

    CreateThread(0x0102, 0x01, 0x00, func_0A_3D46)
    Sleep(1500)

    CreateThread(0x0101, 0x01, 0x00, func_0B_3D85)
    Sleep(7500)

    WaitForThreadExit(0x0101, 0x0002)
    Fade(500)
    OP_C4(0x00, 0x00000002)
    CameraMove(69820, -5950, -38750, 0)
    OP_67(0, 5400, -10000, 0)
    CameraSetDistance(2500, 0)
    OP_6C(45000, 0)
    OP_6E(397, 0)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    Sleep(1000)

    OP_DC()

    ChrTalk(
        0x0102,
        (
            '#0020330935V#1033F#5P……别了，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330936V请不要再\n',
            '继续追寻我了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330937V#1026F#6P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020330938V#1035F#5P能和你再度相会\n',
            '虽然非常开心……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330939V但我们两人始终\n',
            '不该在一起。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330940V#1033F有我这样的人在\n',
            '只会害了你……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330941V说实话，你跟着我\n',
            '也只是累赘而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330942V所以……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330943V#1007F#6P……你说谎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)

    ChrTalk(
        0x0102,
        (
            '#0020330944V#1034F#5P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)
    OP_21()
    PlayBGM(120)
    Sleep(500)

    @scena.Lambda('lambda_0DD8')
    def lambda_0DD8():
        CameraSetDistance(2200, 20000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0DD8)

    Sleep(1500)

    ChrTalk(
        0x0101,
        (
            '#0010330945V#1025F#6P嗯…约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330946V我呢，听说了许多东西，\n',
            '然后终于明白了一件事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330947V#1012F为什么约修亚\n',
            '会从我面前消失……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330948V或许，连约修亚自己\n',
            '都没察觉到真正的理由。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020330949V#1034F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330950V#1019F#6P因为心灵崩溃了，\n',
            '和我在一起就觉得痛苦？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330951V就算和我在一起也只觉得\n',
            '好像是别人的事情一样？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330952V#1007F约修亚在身边\n',
            '会害了我？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330953V我跟着你\n',
            '也只是累赘？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330954V#1006F这些全部，都是谎言吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020330955V#1032F怎么会是谎……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330956V#1012F#6P好了，你听我说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330957V#1025F要我说……\n',
            '约修亚只是在害怕而已哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020330958V#1034F咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330959V#1025F#6P深信自己\n',
            '害死了姐姐……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330960V因此无法忍受\n',
            '同样的事发生在我身上……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330961V所以，在那个夜晚，约修亚\n',
            '才会从我的面前消失。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330962V#1016F其它的理由只不过是强加上去的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020330963V#1034F………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330964V#1035F哈哈，你说什么呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330965V#1045F自从被教授调整以后\n',
            '我就从未感到过恐惧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330966V似乎是为了避免在执行任务中产生恐惧\n',
            '而被调整为这样子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330967V你的指责……完全偏离了重点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330968V#1007F#6P不，我要说的不是\n',
            '那么表面化的东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330969V#1015F……我问你，约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330970V为什么你会觉得\n',
            '姐姐死去的事情\n',
            '就像是别人的事一样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330971V你明白真正的理由吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020330972V#1033F那是因为……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330973V我的心……已经坏掉了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330974V#1002F#6P不，不是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330975V#1007F约修亚……\n',
            '只是不愿意回想起\n',
            '姐姐死去时所受的打击。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330976V所以在潜意识中强制自己\n',
            '将其认定为别人的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020330977V#1050F#3S！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330978V#1025F#6P这和刚才救我的事情\n',
            '是一样的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330979V为了潜入战舰\n',
            '你一定费了很大功夫吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330980V但你却毫不犹豫地\n',
            '现身救我……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330981V那是因为你强烈盼望我能\n',
            '早一刻脱离险境啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020330982V#1033F…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330983V#1012F#6P约修亚的心并没有坏掉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330984V只是因为恐惧……\n',
            '所以在欺骗自己而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330985V#1006F现在的我\n',
            '可以很有把握地肯定这一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020330986V#1050F怎么会……但是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020330987V………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0102, 90, 300)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020330988V#1033F#5P#40W为什么你……#1000W\n',
            '#40W……连这种事都……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330989V#1006F#6P以前我不是就说过嘛～\n',
            '我可是最擅长观察约修亚的人呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330990V何况现在又知道了约修亚过去的身世，\n',
            '已经没人会比我更了解约修亚了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330991V#1018F即便是教授和莱维\n',
            '我也绝对不会输给他们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020330992V#1033F#5P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010330993V#1025F#6P胆怯又勇敢的约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330994V喜欢说谎，本性却又这么诚实的约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330995V#1012F我……最喜欢的约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330996V#1017F终于……\n',
            '回到我的身边了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0x01)
    ChrSetFlags(0x0101, 0x0040)
    ChrSetFlags(0x0102, 0x0040)

    @scena.Lambda('lambda_1840')
    def lambda_1840():
        OP_92(0x0101, 0x0102, 400, 800, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1840)

    Sleep(600)

    Fade(500)
    CameraMove(68080, -6690, -40950, 0)
    OP_67(0, 5530, -10000, 0)
    CameraSetDistance(2500, 0)
    OP_6C(225000, 0)
    OP_6E(379, 0)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(500)

    Fade(500)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetChipByIndex(0x0102, 18)
    ChrSetSubChip(0x0102, 0)
    ChrSetFlags(0x0102, 0x0002)
    OP_99(0x0102, 0x00, 0x03, 1500)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020330997V#1050F#6P……！………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_18F4')
    def lambda_18F4():
        CameraSetDistance(2200, 20000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_18F4)

    OP_99(0x0102, 0x03, 0x06, 1000)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010330998V#1003F#2P但是我……\n',
            '并不是仅仅需要你的保护。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010330999V因为我知道，作为一名游击士，\n',
            '时刻都伴随着危险。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010331000V#1025F无论有没有约修亚，\n',
            '这都是无法改变的事实。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010331001V这是我自己\n',
            '选择的道路。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020331002V#1033F#6P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0102, 0x07, 0x09, 1500)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010331003V#1025F#2P所以……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010331004V所以约修亚，答应我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0102, 0x09, 0x0C, 1500)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020331005V#1034F#6P……什么…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0102, 0x0D, 0x0F, 1000)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010331006V#1012F#2P让我们彼此守护，\n',
            '一起向前吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010331007V我已经变强了，\n',
            '足以保护约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010331008V只要有约修亚在身边，\n',
            '我的力量就会增大好几倍呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010331009V就算是『结社』想要加害，\n',
            '也绝对不会死的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010331010V所以呢……\n',
            '你已经不需要再害怕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020331011V#1051F#6P……艾丝……蒂尔………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020331012V#1039F…………啊…………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0102, 0x0F, 0x12, 1000)
    Sleep(500)

    OP_99(0x0102, 0x13, 0x15, 1000)
    ChrSetSubChip(0x0102, 21)
    Sleep(100)

    @scena.Lambda('lambda_1C44')
    def lambda_1C44():
        OP_99(0x00FE, 0x24, 0x27, 1000)
        Yield()

        Jump('lambda_1C44')

    DispatchAsync2(0x0102, 0x0002, lambda_1C44)

    Sleep(1500)

    ChrTalk(
        0x0102,
        (
            '#0020331013V#1039F#6P#40W为什……么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020331014V#40W……眼泪会……\n',
            '姐姐死后……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020331015V#40W即使是在演戏时……\n',
            '也从来……都没流过的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0102, 0x02)
    ChrSetSubChip(0x0102, 36)
    Sleep(200)

    ChrSetSubChip(0x0102, 22)
    Sleep(200)

    ChrSetSubChip(0x0102, 23)
    Sleep(200)

    ChrSetSubChip(0x0102, 24)
    Sleep(200)

    OP_99(0x0102, 0x28, 0x2B, 1500)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010331016V#1008F#2P#30W嘿嘿……是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0102, 43)
    Sleep(100)

    ChrSetSubChip(0x0102, 25)
    Sleep(100)

    ChrSetSubChip(0x0102, 26)
    Sleep(100)

    ChrSetSubChip(0x0102, 27)
    FadeOut(2000, 0, -1)
    OP_0D()
    Sleep(500)

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0010331017V#30W我什么都没有看到哦……\n',
            '你就尽情哭吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010331018V#40W我会一直这样……\n',
            '……抱紧你的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_DB()
    OP_20(0x00001388)
    OP_21()
    Sleep(2000)

    CameraMove(75980, -5890, -51970, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2810, 0)
    OP_6C(225000, 0)
    OP_6E(317, 0)
    StopEffect(0x80, 0x00)
    ChrSetSubChip(0x0102, 6)
    PlayBGM(117)
    FadeIn(2000, 0)
    OP_0D()
    Sleep(1000)

    CameraMove(69420, -5960, -39640, 6000)
    Fade(1000)
    CameraMove(69420, -5960, -39640, 0)
    OP_67(0, 6950, -10000, 0)
    CameraSetDistance(2500, 0)
    OP_6C(201000, 0)
    OP_6E(317, 0)
    OP_0D()
    Sleep(1000)

    OP_99(0x0102, 0x06, 0x09, 1000)
    Sleep(500)

    OP_99(0x0102, 0x09, 0x0C, 1000)
    Sleep(500)

    Fade(500)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetSubChip(0x0102, 0)
    ChrClearFlags(0x0102, 0x0002)
    ChrClearFlags(0x0101, 0x0080)
    ChrSetDirection(0x0102, 225, 0)
    ChrSetDirection(0x0101, 45, 0)

    @scena.Lambda('lambda_1F1B')
    def lambda_1F1B():
        CameraMove(69190, -5930, -39970, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1F1B)

    ChrMoveTo(0x0101, 68920, -5940, -39630, 1000, 0x00)
    Sleep(500)

    ChrTurnDirection(0x0102, 0x0101, 400)
    Sleep(500)

    OP_DC()

    ChrTalk(
        0x0101,
        (
            '#0010331019V#1008F#2P嘿嘿……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010331020V#1016F好、好难为情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020331021V#1053F#6P嗯……是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010331022V#1004F#2P啊……对了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010331023V#1006F这个，还给你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0101, 19)
    ChrSetSubChip(0x0101, 8)
    ChrSetFlags(0x0101, 0x0002)

    @scena.Lambda('lambda_201D')
    def lambda_201D():
        OP_99(0x00FE, 0x08, 0x0F, 1000)
        Yield()

        Jump('lambda_201D')

    DispatchAsync2(0x0101, 0x0001, lambda_201D)

    ChrMoveTo(0x0101, 69350, -5970, -39550, 500, 0x00)
    TerminateThread(0x0101, 0x01)
    Fade(500)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    ChrSetFlags(0x0102, 0x0002)
    ChrSetChipByIndex(0x0102, 17)
    ChrSetSubChip(0x0102, 0)
    OP_99(0x0102, 0x01, 0x02, 1000)
    Sleep(500)

    OP_99(0x0102, 0x03, 0x04, 1000)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020331024V#1044F#6P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0102, 0x05, 0x06, 1000)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010331025V#1007F#2P真是的……\n',
            '这可是姐姐的遗物吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010331026V#1019F怎么能随便给别人呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020331027V#1043F#6P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020331028V#1040F确实太随便了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0102, 0x07, 0x08, 1000)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010331029V#1025F#2P你的姐姐……\n',
            '是个怎么样的人呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020331030V#1053F#6P嗯……这个嘛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020331031V#1040F气质优雅又温柔，\n',
            '但又有凛然的威严……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020331032V和莱维很相配，\n',
            '小时候我还有点嫉妒呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010331033V#1015F#2P气质优雅又温柔，\n',
            '威严凛然的类型……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010331034V#1004F那不就是……\n',
            '像科洛丝那种感觉吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020331035V#1054F#6P哈哈……是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020331036V#1053F虽然长相完全不同，\n',
            '但性格上也许很相近。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010331037V#1015F#2P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020331038V#1044F#6P……艾丝蒂尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010331039V#1013F#2P没、没什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010331040V#1019F……话说在前，\n',
            '科洛丝，还有大家\n',
            '也都非常担心你呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010331041V回去之后要好好向他们道歉哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020331042V#1043F#6P艾丝蒂尔……我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010331043V#1002F#2P我可不想听你说什么\n',
            '没有资格回去之类的话。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010331044V就算是做了教授的工具，\n',
            '那也不是有意去做的啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010331045V#1007F空贼艇的抢夺事件\n',
            '也只是为了潜入调查。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010331046V#1006F只要你把『结社』的情报\n',
            '告诉老爸，不就功过相抵了嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010331047V这就是所谓的公平交易吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020331048V#1052F#6P这好像是不一样的吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010331049V#1006F#2P而且，你的计划已经暴露，\n',
            '也没办法再潜回那艘船了吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010331050V这样的话，就只有和我们\n',
            '一起行动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020331051V#1048F#6P……要不是你来捣乱，\n',
            '我早就可以按照原定计划\n',
            '把『古罗力亚斯号』炸毁了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010331052V#1007F#2P唔……抱歉哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010331053V#1020F喂！别再说爆破之类\n',
            '的话吓唬人啦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010331054V就算是对抗『结社』，\n',
            '也没必要用上这种极端手段吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020331055V#1043F#6P……不这么做\n',
            '是无法打倒教授和莱维的啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020331056V#1035F不过，就算爆破成功，\n',
            '能杀死他们的可能性也很低……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010331057V#1007F#2P唉，真是的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010331058V#1019F幸好我被\n',
            '抓住了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010331059V不然约修亚就会\n',
            '做出无可挽回的事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020331060V#1053F#6P呵呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010331061V#1009F#2P啊～你刚才觉得我\n',
            '『又在说这么天真的话』\n',
            '没有错吧！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020331062V#1041F#6P不，一阵子没见，\n',
            '你好像成熟了不少……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020331063V不过艾丝蒂尔还是\n',
            '原来的艾丝蒂尔呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020331064V#1049F真让人开心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010331065V#1020F#2P唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    ChrSetSubChip(0x0102, 0)
    ChrClearFlags(0x0101, 0x0002)
    ChrTurnDirection(0x0101, 0x0102, 0)
    ChrClearFlags(0x0101, 0x0080)
    ChrSetSubChip(0x0102, 9)
    OP_0D()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrSetDirection(0x0101, 225, 600)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010331066V#1013F#5P（我、我这是怎么了！）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010331067V(为什么到现在，看到约修亚的笑容\n',
            '  还会心跳不已啊～！)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010331068V#1007F（啊啊，也许是好久不见了，\n',
            '  有些控制不住了吧……)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010331069V(………………………………)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020331070V#1044F#6P？艾丝蒂尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010331071V#1013F#5P对了、对了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010331072V约修亚和那个男人婆\n',
            '关系相当好了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020331073V#1044F#6P男人婆……\n',
            '啊啊，你是说乔丝特吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020331074V#1053F是啊，虽然一开始\n',
            '她好像十分讨厌我的样子……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020331075V不过到后来，很意外地\n',
            '融洽相处了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010331076V#1013F#5P融洽相处……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010331077V………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010331078V……那是不是，接过吻了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020331079V#1044F#6P啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010331080V#1019F#5P不要支支吾吾，快回答！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020331081V#1048F#6P啊，啊啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020331082V当然没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010331083V#1013F#5P那、那么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 300)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010331084V#1017F#2P在这里……\n',
            '那天晚上的要求…\n',
            '重来一次可以吗……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020331085V#1043F#6P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010331086V#1013F#2P因、因为第一次\n',
            '对于女孩子来说很重要嘛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010331087V都、都怪约修亚，\n',
            '竟然给搞成那个样子……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010331088V你要……负责任哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020331089V#1044F#6P艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0101, 0x0080)
    OP_99(0x0102, 0x0A, 0x0D, 1000)
    Sleep(500)

    OP_99(0x0102, 0x0D, 0x10, 1000)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010331090V#2P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020331091V#1056F#6P（……艾丝蒂尔……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020331092V#1054F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0102, 0x10, 0x12, 1000)
    Sleep(500)

    OP_99(0x0102, 0x12, 0x15, 1000)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010331093V#2P（……啊………）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0102, 0x15, 0x19, 1000)
    Sleep(100)

    Sleep(200)

    SetMessageWindowPos(50, 100, -1, -1)
    TalkSetChrName('女孩的声音')

    Talk(
        (
            '#0090331094V#3S喂，约修亚！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_99(0x0102, 0x1B, 0x1E, 1500)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x0394, 5, 0x1CA5))
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021F, 5, 0x10FD))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/E0810._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0008 offset: 0x2F8A
@scena.Code('func_08_2F8A')
def func_08_2F8A():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_DB()
    StopEffect(0x80, 0x00)
    ChrSetPos(0x0101, 68830, -5930, -39840, 135)
    ChrSetPos(0x0102, 70100, -5950, -39240, 135)
    OP_72(0x0003, 0x0004)
    OP_A1(0x0009, 0x0003)
    ChrSetFlags(0x0009, 0x0004)
    ChrSetFlags(0x0009, 0x0040)
    ChrSetPos(0x0009, 51850, -7500, -42660, 265)
    OP_72(0x0003, 0x0020)
    OP_6F(0x0003, 1200)
    OP_B0(0x0003, 0x0A)
    ChrClearFlags(0x0102, 0x0080)
    ChrClearFlags(0x0101, 0x0002)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    CameraMove(79640, -6290, -56570, 0)
    OP_67(0, 9360, -10000, 0)
    CameraSetDistance(4070, 0)
    OP_6C(155000, 0)
    OP_6E(551, 0)
    OP_A1(0x000A, 0x0004)
    ChrSetPos(0x000A, 74070, 6000, -51400, 45)
    OP_72(0x0004, 0x0004)
    PlaySE(121, 0x00, 0x64)
    OP_71(0x0004, 0x0020)
    OP_6F(0x0004, 360)
    OP_70(0x0004, 460)

    @scena.Lambda('lambda_307B')
    def lambda_307B():
        CameraMove(76120, -6250, -54260, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_307B)

    @scena.Lambda('lambda_3093')
    def lambda_3093():
        OP_67(0, 10670, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3093)

    @scena.Lambda('lambda_30AB')
    def lambda_30AB():
        CameraSetDistance(3500, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_30AB)

    @scena.Lambda('lambda_30BB')
    def lambda_30BB():
        OP_6C(180000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_30BB)

    @scena.Lambda('lambda_30CB')
    def lambda_30CB():
        OP_6E(398, 6000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_30CB)

    LoadEffect(0x00, 'map\\\\mp021_00.eff')
    FadeIn(2000, 0)
    OP_C4(0x00, 0x00000002)

    @scena.Lambda('lambda_30FE')
    def lambda_30FE():
        ChrMoveTo(0x00FE, 74070, -6000, -51400, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_30FE)

    Sleep(2000)

    @scena.Lambda('lambda_311E')
    def lambda_311E():
        ChrMoveTo(0x00FE, 74070, -6000, -51400, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_311E)

    PlayEffect(0x00, 0x00, 0x000A, 0, -2000, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(204, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_3178')
    def lambda_3178():
        ChrMoveTo(0x00FE, 74070, -6000, -51400, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_3178)

    OP_72(0x0004, 0x0020)
    OP_73(0x0004)
    StopEffect(0x00, 0x02)
    OP_6F(0x0004, 460)
    OP_70(0x0004, 650)
    OP_73(0x0004)
    OP_23(0x0079)
    OP_23(0x00CC)
    PlaySE(200, 0x00, 0x64)
    OP_7C(0, 200, 3000, 100)
    Sleep(500)

    PlaySE(106, 0x00, 0x64)
    OP_6F(0x0004, 1)
    OP_70(0x0004, 60)
    OP_73(0x0004)
    Sleep(500)

    @scena.Lambda('lambda_31EB')
    def lambda_31EB():
        CameraMove(71790, -6370, -56090, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_31EB)

    @scena.Lambda('lambda_3203')
    def lambda_3203():
        OP_67(0, 6280, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3203)

    @scena.Lambda('lambda_321B')
    def lambda_321B():
        CameraSetDistance(3000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_321B)

    @scena.Lambda('lambda_322B')
    def lambda_322B():
        OP_6C(191000, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_322B)

    @scena.Lambda('lambda_323B')
    def lambda_323B():
        OP_6E(455, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_323B)

    ChrSetPos(0x000B, 73580, -450, -50830, 315)
    ChrSetBattleFlags(0x000B, 0x0020)
    ChrClearFlags(0x000B, 0x0001)
    ChrSetFlags(0x000B, 0x0040)
    ChrClearFlags(0x000B, 0x0080)
    CreateThread(0x000B, 0x00, 0x00, func_0C_3DC4)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x000B, 0x0000)
    OP_DC()

    ChrTalk(
        0x0101,
        (
            '#0010331095V#1005F#5P男、男人婆！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0090331096V#213F#5P怎么，你也\n',
            '一起逃出来了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090331097V#210F真是的……\n',
            '继续被关着不是挺好嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010331098V#1019F#1P你、你说什么～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x000C, 73100, -450, -51090, 315)
    ChrSetPos(0x000D, 73100, -450, -51090, 315)

    ChrTalk(
        0x000C,
        (
            '#0290331099V#4P好啦，乔丝特。\n',
            '别再没事挑衅啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3397')
    def lambda_3397():
        CameraMove(71160, -6550, -57510, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3397)

    Sleep(200)

    CreateThread(0x000C, 0x01, 0x00, func_0D_3DF4)
    Sleep(1500)

    CreateThread(0x000D, 0x01, 0x00, func_0E_3E38)
    WaitForThreadExit(0x000D, 0x0001)
    Sleep(500)

    ChrTalk(
        0x000D,
        (
            '#0300331100V#490F#5P游击士小姑娘，\n',
            '你们暂且休战一下吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010331101V#1007F#5P嗯，唔……\n',
            '刚才承蒙你们相救，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010331102V#1006F再次感谢。\n',
            '真是帮了大忙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0300331103V#191F#5P哈哈哈，这种小事不值一提啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0090331104V#210F#5P哼，我才没打算\n',
            '救你呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090331105V不用谢我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010331106V#1019F#5P哼……你这男人婆，\n',
            '真想把你抓起来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0290331107V#200F#5P对了，约修亚。\n',
            '之后你要怎么办？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010331108V#1026F#5P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    CameraMove(68910, -5930, -41190, 0)
    OP_67(0, 7010, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(202000, 0)
    OP_6E(262, 0)
    ChrSetSubChip(0x0101, 2)
    ChrSetChipByIndex(0x0101, 21)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000C,
        (
            '#0290331109V#204F#7P我们本是来\n',
            '邀请你和我们一起走的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290331110V#200F不过，看这种样子…\n',
            '这句话也没必要问了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020331111V#1035F#6P嗯……抱歉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020331112V#1040F今后的事情会变成怎样，\n',
            '我还无法确定……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020331113V但我现在想\n',
            '和艾丝蒂尔一起回去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010331114V#1025F#2P约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0300331115V#490F#7P嘿，是吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0090331116V#215F#7P……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090331117V#413F唉，也好。\n',
            '反正还有机会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010331118V#1019F#2P哼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0101, 0x02, 0x01, 2000)
    Sleep(100)

    Fade(500)
    CameraMove(71160, -6550, -57510, 0)
    OP_67(0, 6280, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(191000, 0)
    OP_6E(455, 0)
    ChrClearFlags(0x0101, 0x0002)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0101, 65535)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000B,
        (
            '#0090331119V#211F#5P约修亚，记住！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090331120V要是以后厌烦了这个无脑女，\n',
            '随时都可以回到我们这里哦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090331121V#415F我们会热烈欢迎你的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010331122V#1005F#5P谁、谁是无脑女呀！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020331123V#1049F#1P哈哈……\n',
            '多谢了，乔丝特！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020331124V#1041F多伦兄、吉尔兄！\n',
            '感谢你们多日来的关照！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0300331125V#490F#5P嘿，彼此彼此啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0290331126V#202F#5P那，再见啦！\n',
            '后会有期！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_DB()
    CreateThread(0x000D, 0x01, 0x00, func_11_3F16)
    Sleep(1000)

    CreateThread(0x000C, 0x01, 0x00, func_10_3EC9)
    Sleep(1000)

    CreateThread(0x000B, 0x01, 0x00, func_0F_3E68)
    WaitForThreadExit(0x000B, 0x0001)
    OP_6F(0x0004, 60)
    OP_70(0x0004, 1)
    PlaySE(230, 0x00, 0x64)
    OP_73(0x0004)
    Sleep(1000)

    Fade(1000)
    CameraMove(71340, -6240, -49430, 0)
    OP_67(0, 9140, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(179000, 0)
    OP_6E(664, 0)
    OP_0D()

    @scena.Lambda('lambda_3A26')
    def lambda_3A26():
        CameraMove(71340, -4000, -49430, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3A26)

    @scena.Lambda('lambda_3A3E')
    def lambda_3A3E():
        OP_67(0, 14800, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3A3E)

    @scena.Lambda('lambda_3A56')
    def lambda_3A56():
        ChrMoveTo(0x00FE, 74070, 0, -51400, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_3A56)

    CreateThread(0x000A, 0x02, 0x00, func_09_3C9A)
    PlayEffect(0x00, 0x00, 0x000A, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(204, 0x00, 0x64)
    PlaySE(121, 0x01, 0x64)
    Sleep(1500)

    OP_B0(0x0004, 0x0A)
    OP_6F(0x0004, 160)
    OP_70(0x0004, 240)
    OP_73(0x0004)
    OP_71(0x0004, 0x0020)
    OP_6F(0x0004, 240)
    OP_70(0x0004, 340)
    WaitForThreadExit(0x000A, 0x0001)
    WaitForThreadExit(0x000A, 0x0002)
    WaitForThreadExit(0x0101, 0x0001)
    StopEffect(0x00, 0x02)
    OP_23(0x00CC)
    Fade(500)
    CameraMove(74870, -2760, -45440, 0)
    OP_67(0, 9140, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(34000, 0)
    OP_6E(664, 0)
    ChrTurnDirection(0x0101, 0x000A, 0)
    ChrTurnDirection(0x0102, 0x000A, 0)
    OP_0D()

    @scena.Lambda('lambda_3B4A')
    def lambda_3B4A():
        CameraMove(68970, -2760, -60770, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3B4A)

    @scena.Lambda('lambda_3B62')
    def lambda_3B62():
        ChrMoveTo(0x00FE, 50620, 3000, -110430, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_3B62)

    Sleep(200)

    @scena.Lambda('lambda_3B82')
    def lambda_3B82():
        ChrMoveTo(0x00FE, 50620, 3000, -110430, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_3B82)

    Sleep(200)

    @scena.Lambda('lambda_3BA2')
    def lambda_3BA2():
        ChrMoveTo(0x00FE, 50620, 3000, -110430, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_3BA2)

    Sleep(100)

    @scena.Lambda('lambda_3BC2')
    def lambda_3BC2():
        ChrMoveTo(0x00FE, 50620, 3000, -110430, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_3BC2)

    Sleep(100)

    @scena.Lambda('lambda_3BE2')
    def lambda_3BE2():
        ChrMoveTo(0x00FE, 50620, 3000, -110430, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_3BE2)

    Sleep(100)

    @scena.Lambda('lambda_3C02')
    def lambda_3C02():
        ChrMoveTo(0x00FE, 50620, 3000, -110430, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_3C02)

    Sleep(100)

    @scena.Lambda('lambda_3C22')
    def lambda_3C22():
        ChrMoveTo(0x00FE, 50620, 3000, -110430, 16000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_3C22)

    Sleep(100)

    @scena.Lambda('lambda_3C42')
    def lambda_3C42():
        ChrMoveTo(0x00FE, 50620, 3000, -110430, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_3C42)

    Sleep(100)

    @scena.Lambda('lambda_3C62')
    def lambda_3C62():
        ChrMoveTo(0x00FE, 50620, 3000, -110430, 26000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_3C62)

    WaitForThreadExit(0x000A, 0x0001)
    MapSetFlags(0x02000000)
    OP_DC()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021F, 4, 0x10FC))
    NewScene('ED6_DT21/E0810._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0009 offset: 0x3C9A
@scena.Code('func_09_3C9A')
def func_09_3C9A():
    @scena.Lambda('lambda_3CA0')
    def lambda_3CA0():
        ChrSetDirection(0x00FE, 202, 5)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_3CA0)

    Sleep(400)

    @scena.Lambda('lambda_3CB3')
    def lambda_3CB3():
        ChrSetDirection(0x00FE, 202, 10)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_3CB3)

    Sleep(400)

    @scena.Lambda('lambda_3CC6')
    def lambda_3CC6():
        ChrSetDirection(0x00FE, 202, 15)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_3CC6)

    Sleep(400)

    @scena.Lambda('lambda_3CD9')
    def lambda_3CD9():
        ChrSetDirection(0x00FE, 202, 20)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_3CD9)

    Sleep(400)

    @scena.Lambda('lambda_3CEC')
    def lambda_3CEC():
        ChrSetDirection(0x00FE, 202, 30)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_3CEC)

    Sleep(3500)

    @scena.Lambda('lambda_3CFF')
    def lambda_3CFF():
        ChrSetDirection(0x00FE, 202, 20)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_3CFF)

    Sleep(700)

    @scena.Lambda('lambda_3D12')
    def lambda_3D12():
        ChrSetDirection(0x00FE, 202, 15)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_3D12)

    Sleep(600)

    @scena.Lambda('lambda_3D25')
    def lambda_3D25():
        ChrSetDirection(0x00FE, 202, 10)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_3D25)

    Sleep(500)

    @scena.Lambda('lambda_3D38')
    def lambda_3D38():
        ChrSetDirection(0x00FE, 202, 5)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_3D38)

    WaitForThreadExit(0x000A, 0x0003)

    Return()

# id: 0x000A offset: 0x3D46
@scena.Code('func_0A_3D46')
def func_0A_3D46():
    ChrClearFlags(0x0102, 0x0080)
    ChrSetPos(0x0102, 51690, -4200, -43010, 90)
    ChrWalkTo(0x0102, 61100, -6530, -41380, 2000, 0x00)
    ChrMoveTo(0x0102, 70100, -5950, -39240, 2000, 0x00)

    Return()

# id: 0x000B offset: 0x3D85
@scena.Code('func_0B_3D85')
def func_0B_3D85():
    ChrClearFlags(0x0101, 0x0080)
    ChrSetPos(0x0101, 51690, -4200, -43010, 90)
    ChrWalkTo(0x0101, 61100, -6530, -41380, 2000, 0x00)
    ChrMoveTo(0x0101, 68140, -5940, -39340, 2000, 0x00)

    Return()

# id: 0x000C offset: 0x3DC4
@scena.Code('func_0C_3DC4')
def func_0C_3DC4():
    ChrWalkTo(0x00FE, 72740, -450, -49500, 3000, 0x00)
    ChrWalkTo(0x00FE, 74400, -170, -46560, 3000, 0x00)
    ChrSetDirection(0x00FE, 315, 400)

    Return()

# id: 0x000D offset: 0x3DF4
@scena.Code('func_0D_3DF4')
def func_0D_3DF4():
    ChrSetBattleFlags(0x000C, 0x0020)
    ChrClearFlags(0x000C, 0x0001)
    ChrSetFlags(0x000C, 0x0040)
    ChrClearFlags(0x000C, 0x0080)
    ChrWalkTo(0x000C, 72520, -450, -49470, 2000, 0x00)
    ChrWalkTo(0x000C, 73880, 20, -47830, 2000, 0x00)
    ChrSetDirection(0x000C, 315, 400)

    Return()

# id: 0x000E offset: 0x3E38
@scena.Code('func_0E_3E38')
def func_0E_3E38():
    ChrSetBattleFlags(0x000D, 0x0020)
    ChrClearFlags(0x000D, 0x0001)
    ChrSetFlags(0x000D, 0x0040)
    ChrClearFlags(0x000D, 0x0080)
    ChrWalkTo(0x000D, 72520, -450, -49470, 2000, 0x00)
    ChrSetDirection(0x000D, 315, 400)

    Return()

# id: 0x000F offset: 0x3E68
@scena.Code('func_0F_3E68')
def func_0F_3E68():
    ChrWalkTo(0x00FE, 74070, 40, -47860, 2000, 0x00)
    ChrWalkTo(0x00FE, 72720, -450, -49410, 2000, 0x00)
    ChrWalkTo(0x00FE, 73100, -450, -51090, 2000, 0x00)
    ChrWalkTo(0x00FE, 73860, -450, -51580, 2000, 0x00)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 400)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0010 offset: 0x3EC9
@scena.Code('func_10_3EC9')
def func_10_3EC9():
    ChrWalkTo(0x00FE, 72320, -450, -49620, 2000, 0x00)
    ChrWalkTo(0x00FE, 73100, -450, -51090, 2000, 0x00)
    ChrWalkTo(0x00FE, 73860, -450, -51580, 2000, 0x00)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 400)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0011 offset: 0x3F16
@scena.Code('func_11_3F16')
def func_11_3F16():
    ChrSetDirection(0x000D, 135, 400)
    ChrWalkTo(0x00FE, 73100, -450, -51090, 2000, 0x00)
    ChrWalkTo(0x00FE, 73860, -450, -51580, 2000, 0x00)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 400)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0012 offset: 0x3F56
@scena.Code('func_12_3F56')
def func_12_3F56():
    EventBegin(0x00)
    ChrSetChipByIndex(0x0101, 21)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0102, 20)
    ChrSetSubChip(0x0102, 0)
    StopEffect(0x80, 0x00)
    OP_C4(0x00, 0x00000002)
    OP_72(0x0003, 0x0004)
    OP_A1(0x0009, 0x0003)
    ChrSetFlags(0x0009, 0x0004)
    ChrSetFlags(0x0009, 0x0040)
    ChrSetPos(0x0009, 51850, -7500, -42660, 265)
    OP_72(0x0003, 0x0020)
    OP_6F(0x0003, 1200)
    CameraMove(76830, -6040, -37090, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3080, 0)
    OP_6C(215000, 0)
    OP_6E(624, 0)
    ChrSetPos(0x0101, 70130, -5950, -39180, 180)
    ChrSetPos(0x0102, 71460, -5970, -39040, 180)

    @scena.Lambda('lambda_400B')
    def lambda_400B():
        CameraMove(71660, -5970, -39280, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_400B)

    @scena.Lambda('lambda_4023')
    def lambda_4023():
        OP_67(0, 5600, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4023)

    FadeIn(2000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0001)
    Fade(1000)
    CameraMove(70470, -5960, -39980, 0)
    OP_67(0, 4240, -10000, 0)
    CameraSetDistance(3300, 0)
    OP_6C(225000, 0)
    OP_6E(281, 0)
    OP_0D()
    Sleep(500)

    OP_99(0x0102, 0x00, 0x02, 1500)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020331127V#1043F#6P……对了，艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0101, 0x00, 0x02, 1500)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010331128V#1017F#2P什么……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020331129V#1035F……敌人实在太过强大了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020331130V我想，教授抓走艾丝蒂尔的用意\n',
            '也是为了把我引诱出来吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020331131V#1042F这样才能保证在自己离开时，\n',
            '『古罗力亚斯号』不被攻破。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010331132V#1020F#2P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020331133V#1043F#6P莱维也是，\n',
            '当时他完全可以在解决我们之后\n',
            '再去阻止引擎的失控。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020331134V他之所以没这样做……\n',
            '应该就是因为觉得我太没用，\n',
            '所以手下留情吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010331135V#1026F#2P…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020331136V#1042F其他执行者也是一样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020331137V单论战斗力\n',
            '都是在我之上的高手。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020331138V说实话，今后还会面对无数的苦战。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0101, 0x02, 0x04, 1500)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010331139V#1003F#2P嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0102, 0x02, 0x04, 1500)
    Sleep(300)

    ChrTalk(
        0x0102,
        (
            '#0020331140V#1053F#6P但是……我答应你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020331141V#1040F绝不会再一次……\n',
            '逃避现实了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020331142V我会和你一起……\n',
            '走到最后。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0101, 0x04, 0x02, 1500)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010331143V#1008F#2P约修亚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010331144V#1017F嗯……我也发誓！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    OP_C4(0x01, 0x00000002)
    RemoveItem(ItemTable['约修亚的口琴'], 1)
    OP_AD('ED6_DT24/C_VIS156._CH', 0x0000, 0x0000, 0x00000064)
    Sleep(4000)

    OP_56(0x02)
    SetScenaFlags(ScenaFlag(0x0395, 1, 0x1CA9))

    ExecExpressionWithVar(
        0x31,
        (
            (Expr.PushLong, 0x128),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(100000, -100000, 100000, 0)
    FadeIn(0, 0)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    UnlockAchievement(0x13, 0x0000, 0x00)

    Menu(
        0,
        240,
        180,
        0,
        (
            TXT(0x00, '【保存进度】\n'),
            TXT(0x01, '【进入下一章】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_44EE',
    )

    ShowSaveMenu()

    def _loc_44EE(): pass

    label('loc_44EE')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_AE(0x000000C8)
    Sleep(2000)

    MapClearFlags(0x02000000)
    ClearScenaFlags(ScenaFlag(0x0395, 1, 0x1CA9))

    ExecExpressionWithVar(
        0x04,
        (
            (Expr.PushLong, 0x7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/C0705._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0013 offset: 0x4529
@scena.Code('func_13_4529')
def func_13_4529():
    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0011860001V#1001F这里好像可以钓上什么来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4561')
    def lambda_4561():
        CameraMove(57640, -6680, -64840, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_4561)

    @scena.Lambda('lambda_4579')
    def lambda_4579():
        CameraSetDistance(3200, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_4579)

    @scena.Lambda('lambda_4589')
    def lambda_4589():
        OP_6C(20000, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_4589)

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
        'loc_4610',
    )

    OP_C0(0x0E, 0x00000016, 0x0000E9AC, 0xFFFFE5CA, 0xFFFF05F6, 0x000000FA, 0x0000D8B8, 0xFFFFE9D0, 0xFFFEFE94)
    OP_0D()
    EventEnd(0x01)

    Jump('loc_461F')

    def _loc_4610(): pass

    label('loc_4610')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_461F',
    )

    EventEnd(0x01)

    def _loc_461F(): pass

    label('loc_461F')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

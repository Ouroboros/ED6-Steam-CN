import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C4201_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C4201   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'C4201.x'
    header.mapIndex       = 1
    header.bgm            = 31
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
        ('ED6_DT09/CH10490._CH', 'ED6_DT09/CH10490P._CP'),
        ('ED6_DT09/CH10491._CH', 'ED6_DT09/CH10491P._CP'),
        ('ED6_DT09/CH10500._CH', 'ED6_DT09/CH10500P._CP'),
        ('ED6_DT09/CH10501._CH', 'ED6_DT09/CH10501P._CP'),
        ('ED6_DT09/CH10510._CH', 'ED6_DT09/CH10510P._CP'),
        ('ED6_DT09/CH10511._CH', 'ED6_DT09/CH10511P._CP'),
        ('ED6_DT09/CH11110._CH', 'ED6_DT09/CH11110P._CP'),
        ('ED6_DT09/CH11111._CH', 'ED6_DT09/CH11111P._CP'),
        ('ED6_DT09/CH11120._CH', 'ED6_DT09/CH11120P._CP'),
        ('ED6_DT09/CH11121._CH', 'ED6_DT09/CH11121P._CP'),
        ('ED6_DT09/CH11130._CH', 'ED6_DT09/CH11130P._CP'),
        ('ED6_DT09/CH11131._CH', 'ED6_DT09/CH11131P._CP'),
        ('ED6_DT09/CH11140._CH', 'ED6_DT09/CH11140P._CP'),
        ('ED6_DT09/CH11141._CH', 'ED6_DT09/CH11141P._CP'),
        ('ED6_DT09/CH11150._CH', 'ED6_DT09/CH11150P._CP'),
        ('ED6_DT09/CH11151._CH', 'ED6_DT09/CH11151P._CP'),
    ]

# id: 0x10001 offset: 0x12A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '',
            x                   = 119050,
            z                   = 0,
            y                   = 5990,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '',
            x                   = 140780,
            z                   = 1000,
            y                   = -151350,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x1AA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = 139310,
            z           = 0,
            y           = 6070,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x027E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 104120,
            z           = 0,
            y           = 13980,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x027B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x1E2
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 119050,
            y           = -1000,
            z           = 5990,
            range       = 2000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000004,
        ),
        ScenaEventData(
            x           = 140780,
            y           = 0,
            z           = -151350,
            range       = 2000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000005,
        ),
    )

# id: 0x10004 offset: 0x222
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 128250,
            triggerZ            = 0,
            triggerY            = -152730,
            triggerRange        = 1000,
            actorX              = 127270,
            actorZ              = 1500,
            actorY              = -152920,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 118070,
            triggerZ            = 0,
            triggerY            = 19130,
            triggerRange        = 1000,
            actorX              = 118680,
            actorZ              = 1500,
            actorY              = 19250,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 123780,
            triggerZ            = 0,
            triggerY            = 19220,
            triggerRange        = 1000,
            actorX              = 122910,
            actorZ              = 1500,
            actorY              = 19200,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 103870,
            triggerZ            = 0,
            triggerY            = 24400,
            triggerRange        = 1000,
            actorX              = 103830,
            actorZ              = 1500,
            actorY              = 24960,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 136410,
            triggerZ            = 0,
            triggerY            = -112150,
            triggerRange        = 1000,
            actorX              = 137180,
            actorZ              = 1500,
            actorY              = -112180,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2D6
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x2D7
@scena.Code('func_01_2D7')
def func_01_2D7():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D0, 1, 0x681)),
            Expr.Return,
        ),
        'loc_2EC',
    )

    OP_6F(0x0000, 240)
    OP_6F(0x0003, 120)

    def _loc_2EC(): pass

    label('loc_2EC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DA, 2, 0x6D2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2FE',
    )

    OP_6F(0x0001, 0)

    Jump('loc_305')

    def _loc_2FE(): pass

    label('loc_2FE')

    OP_6F(0x0001, 60)

    def _loc_305(): pass

    label('loc_305')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DA, 4, 0x6D4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_317',
    )

    OP_6F(0x0002, 0)

    Jump('loc_31E')

    def _loc_317(): pass

    label('loc_317')

    OP_6F(0x0002, 60)

    def _loc_31E(): pass

    label('loc_31E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DA, 6, 0x6D6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_330',
    )

    OP_6F(0x0004, 0)

    Jump('loc_337')

    def _loc_330(): pass

    label('loc_330')

    OP_6F(0x0004, 60)

    def _loc_337(): pass

    label('loc_337')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DA, 7, 0x6D7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_349',
    )

    OP_6F(0x0005, 0)

    Jump('loc_350')

    def _loc_349(): pass

    label('loc_349')

    OP_6F(0x0005, 60)

    def _loc_350(): pass

    label('loc_350')

    OP_B2(0x00, 0x00, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DC, 5, 0x6E5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_367',
    )

    ChrClearFlags(0x000A, 0x0080)
    OP_B2(0x01, 0x00, 0x0080)

    def _loc_367(): pass

    label('loc_367')

    OP_B2(0x00, 0x01, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DC, 6, 0x6E6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_37E',
    )

    ChrClearFlags(0x000B, 0x0080)
    OP_B2(0x01, 0x01, 0x0080)

    def _loc_37E(): pass

    label('loc_37E')

    PlaySE(461, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x384
@scena.Code('func_02_384')
def func_02_384():
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

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3A9',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_43C')

    def _loc_3A9(): pass

    label('loc_3A9')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3C2',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_43C')

    def _loc_3C2(): pass

    label('loc_3C2')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3DB',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_43C')

    def _loc_3DB(): pass

    label('loc_3DB')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3F4',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_43C')

    def _loc_3F4(): pass

    label('loc_3F4')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_40D',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_43C')

    def _loc_40D(): pass

    label('loc_40D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_426',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_43C')

    def _loc_426(): pass

    label('loc_426')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_43C',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    def _loc_43C(): pass

    label('loc_43C')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_451',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_43C')

    def _loc_451(): pass

    label('loc_451')

    Return()

# id: 0x0003 offset: 0x452
@scena.Code('func_03_452')
def func_03_452():
    MapSetFlags(0x00000080)
    Sleep(30)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00D0, 1, 0x681)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4B7',
    )

    EventBegin(0x00)
    PlaySE(100, 0x00, 0x64)
    OP_6F(0x0003, 65)
    OP_70(0x0003, 120)
    OP_73(0x0003)
    OP_6F(0x0003, 120)
    Sleep(500)

    CameraMove(128919, 0, -146150, 2000)
    PlaySE(208, 0x00, 0x64)
    OP_70(0x0000, 240)
    OP_73(0x0000)
    OP_6F(0x0000, 240)
    SetScenaFlags(ScenaFlag(0x00D0, 1, 0x681))
    EventEnd(0x01)

    Jump('loc_4D1')

    def _loc_4B7(): pass

    label('loc_4B7')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '控制杆纹丝不动。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_4D1(): pass

    label('loc_4D1')

    OP_73(0x0003)
    MapClearFlags(0x00000080)

    Return()

# id: 0x0004 offset: 0x4DA
@scena.Code('func_04_4DA')
def func_04_4DA():
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
            '成群凶暴的魔兽正在四处游荡中。',
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
        (0x00000001, 'loc_5C5'),
        (-1, 'loc_65F'),
    )

    def _loc_5C5(): pass

    label('loc_5C5')

    Fade(1000)
    ChrSetPos(0x0000, 112770, 0, 5750, 90)
    ChrSetPos(0x0001, 112770, 0, 5750, 90)
    ChrSetPos(0x0002, 112770, 0, 5750, 90)
    ChrSetPos(0x0003, 112770, 0, 5750, 90)
    ChrSetPos(0x0004, 112770, 0, 5750, 90)
    ChrSetPos(0x0005, 112770, 0, 5750, 90)
    ChrSetPos(0x0006, 112770, 0, 5750, 90)
    ChrSetPos(0x0007, 112770, 0, 5750, 90)
    OP_69(0x0000, 0)
    OP_30(0x00)
    OP_0D()
    EventEnd(0x00)

    Return()

    def _loc_65F(): pass

    label('loc_65F')

    Battle(0x00000401, 0x00000000, 0x00, 0x0000, 0xFF)
    ChrSetPos(0x0000, 112770, 0, 5750, 90)
    ChrSetPos(0x0001, 112770, 0, 5750, 90)
    ChrSetPos(0x0002, 112770, 0, 5750, 90)
    ChrSetPos(0x0003, 112770, 0, 5750, 90)
    ChrSetPos(0x0004, 112770, 0, 5750, 90)
    ChrSetPos(0x0005, 112770, 0, 5750, 90)
    ChrSetPos(0x0006, 112770, 0, 5750, 90)
    ChrSetPos(0x0007, 112770, 0, 5750, 90)
    OP_69(0x0000, 0)
    OP_30(0x00)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000002, 'loc_70D'),
        (0x00000001, 'loc_710'),
        (-1, 'loc_713'),
    )

    def _loc_70D(): pass

    label('loc_70D')

    EventEnd(0x00)

    Return()

    def _loc_710(): pass

    label('loc_710')

    OP_B4(0x00)

    Return()

    def _loc_713(): pass

    label('loc_713')

    EventBegin(0x01)
    ChrSetFlags(0x000A, 0x0080)
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
            '成功消灭了地下水路·西部区域中被通缉的魔兽！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetScenaFlags(ScenaFlag(0x00DC, 5, 0x6E5))
    OP_28(0x0050, 0x04, 0x10)
    OP_28(0x0050, 0x01, 0x0001)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x00)

    Return()

# id: 0x0005 offset: 0x796
@scena.Code('func_05_796')
def func_05_796():
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
        (0x00000001, 'loc_87B'),
        (-1, 'loc_915'),
    )

    def _loc_87B(): pass

    label('loc_87B')

    Fade(1000)
    ChrSetPos(0x0000, 140780, 0, -157740, 0)
    ChrSetPos(0x0001, 140780, 0, -157740, 0)
    ChrSetPos(0x0002, 140780, 0, -157740, 0)
    ChrSetPos(0x0003, 140780, 0, -157740, 0)
    ChrSetPos(0x0004, 140780, 0, -157740, 0)
    ChrSetPos(0x0005, 140780, 0, -157740, 0)
    ChrSetPos(0x0006, 140780, 0, -157740, 0)
    ChrSetPos(0x0007, 140780, 0, -157740, 0)
    OP_69(0x0000, 0)
    OP_30(0x00)
    OP_0D()
    EventEnd(0x00)

    Return()

    def _loc_915(): pass

    label('loc_915')

    Battle(0x00000402, 0x00000000, 0x00, 0x0000, 0xFF)
    ChrSetPos(0x0000, 140780, 0, -157740, 0)
    ChrSetPos(0x0001, 140780, 0, -157740, 0)
    ChrSetPos(0x0002, 140780, 0, -157740, 0)
    ChrSetPos(0x0003, 140780, 0, -157740, 0)
    ChrSetPos(0x0004, 140780, 0, -157740, 0)
    ChrSetPos(0x0005, 140780, 0, -157740, 0)
    ChrSetPos(0x0006, 140780, 0, -157740, 0)
    ChrSetPos(0x0007, 140780, 0, -157740, 0)
    OP_69(0x0000, 0)
    OP_30(0x00)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000002, 'loc_9C3'),
        (0x00000001, 'loc_9C6'),
        (-1, 'loc_9C9'),
    )

    def _loc_9C3(): pass

    label('loc_9C3')

    EventEnd(0x00)

    Return()

    def _loc_9C6(): pass

    label('loc_9C6')

    OP_B4(0x00)

    Return()

    def _loc_9C9(): pass

    label('loc_9C9')

    EventBegin(0x01)
    ChrSetFlags(0x000B, 0x0080)
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
            '成功消灭了地下水路·东部区域中被通缉的魔兽！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetScenaFlags(ScenaFlag(0x00DC, 6, 0x6E6))
    OP_28(0x0051, 0x04, 0x10)
    OP_28(0x0051, 0x01, 0x0001)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x00)

    Return()

# id: 0x0006 offset: 0xA4C
@scena.Code('func_06_A4C')
def func_06_A4C():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DA, 2, 0x6D2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BF6',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DA, 3, 0x6D3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B28',
    )

    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    ChrSetPos(0x0008, 118680, 3000, 19250, 320)
    ChrTurnDirection(0x0008, 0x0000, 0)

    @scena.Lambda('lambda_0A9B')
    def lambda_0A9B():
        ChrMoveTo(0x00FE, 118680, 1500, 19250, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0A9B)

    @scena.Lambda('lambda_0AB6')
    def lambda_0AB6():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1200)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0AB6)

    ChrClearFlags(0x0008, 0x0080)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '魔兽出现了！',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Battle(0x00000270, 0x00000000, 0x00, 0x0000, 0xFF)
    ChrSetFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_B03'),
        (0x00000002, 'loc_B15'),
        (0x00000001, 'loc_B25'),
        (-1, 'loc_B28'),
    )

    def _loc_B03(): pass

    label('loc_B03')

    SetScenaFlags(ScenaFlag(0x00DA, 3, 0x6D3))
    OP_6F(0x0001, 60)
    Sleep(500)

    Jump('loc_B28')

    def _loc_B15(): pass

    label('loc_B15')

    OP_6F(0x0001, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

    def _loc_B25(): pass

    label('loc_B25')

    OP_B4(0x00)

    Return()

    def _loc_B28(): pass

    label('loc_B28')

    If(
        (
            (Expr.Eval, "AddItem(0x00FB, 1)"),
            Expr.Return,
        ),
        'loc_B7E',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '反射大衣',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00DA, 2, 0x6D2))

    Jump('loc_BF3')

    def _loc_B7E(): pass

    label('loc_B7E')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '反射大衣',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '反射大衣',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0)

    def _loc_BF3(): pass

    label('loc_BF3')

    Jump('loc_C2C')

    def _loc_BF6(): pass

    label('loc_BF6')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱里什么东西都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    WaitEffect(0x0F, 0x43)
    def _loc_C2C(): pass

    label('loc_C2C')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0xC3A
@scena.Code('func_07_C3A')
def func_07_C3A():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DA, 4, 0x6D4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DEA',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DA, 5, 0x6D5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D16',
    )

    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    ChrSetPos(0x0008, 122910, 3000, 19200, 320)
    ChrTurnDirection(0x0008, 0x0000, 0)

    @scena.Lambda('lambda_0C89')
    def lambda_0C89():
        ChrMoveTo(0x00FE, 122910, 1500, 19200, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0C89)

    @scena.Lambda('lambda_0CA4')
    def lambda_0CA4():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1200)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0CA4)

    ChrClearFlags(0x0008, 0x0080)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '魔兽出现了！',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Battle(0x00000279, 0x00000000, 0x00, 0x0000, 0xFF)
    ChrSetFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_CF1'),
        (0x00000002, 'loc_D03'),
        (0x00000001, 'loc_D13'),
        (-1, 'loc_D16'),
    )

    def _loc_CF1(): pass

    label('loc_CF1')

    SetScenaFlags(ScenaFlag(0x00DA, 5, 0x6D5))
    OP_6F(0x0002, 60)
    Sleep(500)

    Jump('loc_D16')

    def _loc_D03(): pass

    label('loc_D03')

    OP_6F(0x0002, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

    def _loc_D13(): pass

    label('loc_D13')

    OP_B4(0x00)

    Return()

    def _loc_D16(): pass

    label('loc_D16')

    If(
        (
            (Expr.Eval, "AddItem(0x00D5, 1)"),
            Expr.Return,
        ),
        'loc_D6E',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '拳斗士手套',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00DA, 4, 0x6D4))

    Jump('loc_DE7')

    def _loc_D6E(): pass

    label('loc_D6E')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '拳斗士手套',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '拳斗士手套',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0)

    def _loc_DE7(): pass

    label('loc_DE7')

    Jump('loc_E20')

    def _loc_DEA(): pass

    label('loc_DEA')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱里什么东西都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    WaitEffect(0x0F, 0x44)
    def _loc_E20(): pass

    label('loc_E20')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0xE2E
@scena.Code('func_08_E2E')
def func_08_E2E():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DA, 6, 0x6D6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F1E',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0004, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01F6, 1)"),
            Expr.Return,
        ),
        'loc_EA4',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '大回复药',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00DA, 6, 0x6D6))

    Jump('loc_F1B')

    def _loc_EA4(): pass

    label('loc_EA4')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '大回复药',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '大回复药',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0004, 60)
    OP_70(0x0004, 0)

    def _loc_F1B(): pass

    label('loc_F1B')

    Jump('loc_F54')

    def _loc_F1E(): pass

    label('loc_F1E')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱里什么东西都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    WaitEffect(0x0F, 0x45)
    def _loc_F54(): pass

    label('loc_F54')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0009 offset: 0xF62
@scena.Code('func_09_F62')
def func_09_F62():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DA, 7, 0x6D7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1052',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0005, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01F6, 1)"),
            Expr.Return,
        ),
        'loc_FD8',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '大回复药',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00DA, 7, 0x6D7))

    Jump('loc_104F')

    def _loc_FD8(): pass

    label('loc_FD8')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '大回复药',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '大回复药',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0005, 60)
    OP_70(0x0005, 0)

    def _loc_104F(): pass

    label('loc_104F')

    Jump('loc_1088')

    def _loc_1052(): pass

    label('loc_1052')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱里什么东西都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    WaitEffect(0x0F, 0x46)
    def _loc_1088(): pass

    label('loc_1088')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T0310_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0310   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0310.x'
    header.mapIndex       = 15
    header.bgm            = 88
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
            dword_08        = 0x00000000,
            word_0C         = 0x0004,
            word_0E         = 0x010E,
            dword_10        = 0,
            dword_14        = 8000,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2600,
            dword_2C        = 262,
            word_30         = 45,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 15,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
        ScenaEntryPoint(
            dword_00        = 0x00010554,
            dword_04        = 0x00000320,
            dword_08        = 0x00008AAC,
            word_0C         = 0x0004,
            word_0E         = 0x00B4,
            dword_10        = 0,
            dword_14        = 8000,
            dword_18        = -10000,
            dword_1C        = -32600,
            dword_20        = 0,
            dword_24        = -41000,
            dword_28        = 2600,
            dword_2C        = 262,
            word_30         = 45,
            word_32         = 45,
            word_34         = 45,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 15,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
        ScenaEntryPoint(
            dword_00        = 0x00010554,
            dword_04        = 0x00000320,
            dword_08        = 0x00008AAC,
            word_0C         = 0x0004,
            word_0E         = 0x00B4,
            dword_10        = 0,
            dword_14        = 6000,
            dword_18        = -10000,
            dword_1C        = -1040,
            dword_20        = 0,
            dword_24        = -3230,
            dword_28        = 3000,
            dword_2C        = 280,
            word_30         = 45,
            word_32         = 45,
            word_34         = 45,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 15,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10000 offset: 0x130
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH02000._CH', 'ED6_DT07/CH02000P._CP'),
        ('ED6_DT07/CH00010._CH', 'ED6_DT07/CH00010P._CP'),
        ('ED6_DT06/CH20008._CH', 'ED6_DT06/CH20008P._CP'),
        ('ED6_DT06/CH20005._CH', 'ED6_DT06/CH20005P._CP'),
        ('ED6_DT06/CH20006._CH', 'ED6_DT06/CH20006P._CP'),
        ('ED6_DT07/CH02210._CH', 'ED6_DT07/CH02210P._CP'),
        ('ED6_DT07/CH02220._CH', 'ED6_DT07/CH02220P._CP'),
        ('ED6_DT06/CH20011._CH', 'ED6_DT06/CH20011P._CP'),
        ('ED6_DT07/CH00003._CH', 'ED6_DT07/CH00003P._CP'),
        ('ED6_DT07/CH00013._CH', 'ED6_DT07/CH00013P._CP'),
        ('ED6_DT07/CH02003._CH', 'ED6_DT07/CH02003P._CP'),
        ('ED6_DT07/CH00023._CH', 'ED6_DT07/CH00023P._CP'),
        ('ED6_DT06/CH20020._CH', 'ED6_DT06/CH20020P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
    ]

# id: 0x10001 offset: 0x1A2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '卡西乌斯',
            x                   = -1600,
            z                   = 0,
            y                   = 3011,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0141,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '约修亚',
            x                   = 11500,
            z                   = 0,
            y                   = -3400,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '艾丝蒂尔',
            x                   = 148000,
            z                   = 520,
            y                   = 145400,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x01C4,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '艾丝蒂尔',
            x                   = -8230,
            z                   = 200,
            y                   = -520,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x01C0,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '男孩',
            x                   = -9550,
            z                   = 200,
            y                   = -520,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x01C4,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '卡西乌斯',
            x                   = -8100,
            z                   = 200,
            y                   = 2200,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x01C4,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '器皿',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 65548,
            chipIndex           = 12,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '器皿',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 65548,
            chipIndex           = 12,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '器皿',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 65548,
            chipIndex           = 12,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '咖啡',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1572876,
            chipIndex           = 12,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '咖啡',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1572876,
            chipIndex           = 12,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '咖啡',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1572876,
            chipIndex           = 12,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '法式面包',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 720908,
            chipIndex           = 12,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '炸面包',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2031628,
            chipIndex           = 12,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
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
    )

# id: 0x10004 offset: 0x362
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 146290,
            triggerZ            = 0,
            triggerY            = 144760,
            triggerRange        = 800,
            actorX              = 147910,
            actorZ              = 1500,
            actorY              = 144780,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0010,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 72010,
            triggerZ            = 0,
            triggerY            = 71390,
            triggerRange        = 800,
            actorX              = 72570,
            actorZ              = 1500,
            actorY              = 72600,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0010,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x3AA
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_3B9',
    )

    ChrSetFlags(0x0008, 0x0080)

    Jump('loc_4B1')

    def _loc_3B9(): pass

    label('loc_3B9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_3D9',
    )

    ChrSetFlags(0x0008, 0x0004)
    ChrSetPos(0x0008, 3554, 0, 71683, 161)

    Jump('loc_4B1')

    def _loc_3D9(): pass

    label('loc_3D9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 2, 0x202)),
            Expr.Return,
        ),
        'loc_49D',
    )

    ChrSetPos(0x0008, -8100, 200, 2200, 180)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetFlags(0x0008, 0x0010)
    ChrSetChipByIndex(0x0008, 10)
    ChrSetPos(0x000E, -8360, 700, 300, 0)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x0011, -7860, 700, 200, 0)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x000F, -9620, 700, 300, 0)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x0012, -9120, 700, 200, 0)
    ChrClearFlags(0x0012, 0x0080)
    ChrSetPos(0x0010, -8260, 700, 1100, 0)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0013, -8860, 700, 1200, 0)
    ChrClearFlags(0x0013, 0x0080)
    ChrSetPos(0x0014, -9520, 700, 1100, 0)
    ChrClearFlags(0x0014, 0x0080)

    Jump('loc_4B1')

    def _loc_49D(): pass

    label('loc_49D')

    ChrClearFlags(0x000A, 0x0008)
    ChrClearFlags(0x0009, 0x0008)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x0009, 0x0080)

    def _loc_4B1(): pass

    label('loc_4B1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_4C8',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x30),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_0E_382E)

    def _loc_4C8(): pass

    label('loc_4C8')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000001, 'loc_4E4'),
        (0x00000002, 'loc_587'),
        (0x00000003, 'loc_69D'),
        (0x00000066, 'loc_6A4'),
        (0x00000067, 'loc_70F'),
        (-1, 'loc_77A'),
    )

    def _loc_4E4(): pass

    label('loc_4E4')

    MapClearFlags(0x00000001)
    CameraMove(-6600, 0, 1400, 0)
    ChrSetSubChip(0x000E, 10)
    ChrSetSubChip(0x000F, 10)
    ChrSetSubChip(0x0010, 1)
    ChrSetPos(0x000E, -8360, 700, 300, 0)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000F, -9620, 700, 300, 0)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x0010, -8260, 700, 1100, 0)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0014, -9520, 700, 1100, 0)
    ChrClearFlags(0x0014, 0x0080)
    ChrSetPos(0x0015, -640, 800, 2960, 0)
    ChrClearFlags(0x0015, 0x0080)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_04_990)

    Jump('loc_77A')

    def _loc_587(): pass

    label('loc_587')

    MapClearFlags(0x00000001)
    CameraMove(-3500, 0, 1700, 0)
    ChrSetPos(0x000A, -8230, 200, -520, 0)
    ChrSetPos(0x0009, -9550, 200, -520, 0)
    ChrSetPos(0x0008, -8100, 200, 2200, 180)
    ChrSetFlags(0x0101, 0x0008)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetFlags(0x000A, 0x0004)
    ChrSetFlags(0x0009, 0x0004)
    ChrSetChipByIndex(0x000A, 8)
    ChrSetChipByIndex(0x0009, 9)
    ChrSetChipByIndex(0x0008, 10)
    ChrSetPos(0x000E, -8360, 700, 300, 0)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x0011, -7860, 700, 200, 0)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x000F, -9620, 700, 300, 0)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x0012, -9120, 700, 200, 0)
    ChrClearFlags(0x0012, 0x0080)
    ChrSetPos(0x0010, -8260, 700, 1100, 0)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0013, -8860, 700, 1200, 0)
    ChrClearFlags(0x0013, 0x0080)
    ChrSetPos(0x0014, -9520, 700, 1100, 0)
    ChrClearFlags(0x0014, 0x0080)
    FadeIn(1000, 0)
    Event(0, func_05_C86)

    Jump('loc_77A')

    def _loc_69D(): pass

    label('loc_69D')

    Event(0, func_05_C86)

    Jump('loc_77A')

    def _loc_6A4(): pass

    label('loc_6A4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_6AE',
    )

    Jump('loc_70C')

    def _loc_6AE(): pass

    label('loc_6AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_70C',
    )

    MapClearFlags(0x00000001)
    CameraMove(6187, 0, 71060, 0)
    ChrSetPos(0x0101, 3012, 0, 67051, 0)
    ChrSetPos(0x0102, 3891, 0, 66840, 0)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetPos(0x0008, 3060, 200, 71360, 180)
    ChrSetChipByIndex(0x0008, 10)
    Event(0, func_08_1B88)

    def _loc_70C(): pass

    label('loc_70C')

    Jump('loc_77A')

    def _loc_70F(): pass

    label('loc_70F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_719',
    )

    Jump('loc_777')

    def _loc_719(): pass

    label('loc_719')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_777',
    )

    MapClearFlags(0x00000001)
    CameraMove(6187, 0, 71060, 0)
    ChrSetPos(0x0101, 8324, 0, 71386, 270)
    ChrSetPos(0x0102, 8138, 0, 70528, 270)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetPos(0x0008, 3060, 200, 71360, 180)
    ChrSetChipByIndex(0x0008, 10)
    Event(0, func_08_1B88)

    def _loc_777(): pass

    label('loc_777')

    Jump('loc_77A')

    def _loc_77A(): pass

    label('loc_77A')

    Return()

# id: 0x0001 offset: 0x77B
@scena.Code('func_01_77B')
def func_01_77B():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_793',
    )

    OP_B1('t0310_y')

    Jump('loc_79C')

    def _loc_793(): pass

    label('loc_793')

    OP_B1('t0310_n')

    def _loc_79C(): pass

    label('loc_79C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_7B2',
    )

    StopEffect(0x80, 0x00)
    StopEffect(0x81, 0x00)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0xF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_7B2(): pass

    label('loc_7B2')

    Return()

# id: 0x0002 offset: 0x7B3
@scena.Code('func_02_7B3')
def func_02_7B3():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_7C8',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_7B3')

    def _loc_7C8(): pass

    label('loc_7C8')

    Return()

# id: 0x0003 offset: 0x7C9
@scena.Code('func_03_7C9')
def func_03_7C9():
    TalkBegin(0x00FE)
    ChrClearFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x87),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_7EE',
    )

    ChrSetSubChip(0x00FE, 1)

    Jump('loc_809')

    def _loc_7EE(): pass

    label('loc_7EE')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_804',
    )

    ChrSetSubChip(0x00FE, 2)

    Jump('loc_809')

    def _loc_804(): pass

    label('loc_804')

    ChrSetSubChip(0x00FE, 0)

    def _loc_809(): pass

    label('loc_809')

    ChrSetDirection(0x00FE, 180, 0)
    ChrSetFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_93D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x0101,
        (
            '#0010000212V#004F对了，老爸。\n',
            '你今天不去游击士协会吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000213V这几天你还是抽空去一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160000214V#080F我还有一些堆积的文件要处理。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160000215V#080F呵呵，不用为我担心，\n',
            '等到要被解雇的时候我自然会回去工作的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000216V#505F（老爸真是一点也不可靠啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_987')

    def _loc_93D(): pass

    label('loc_93D')

    ChrTalk(
        0x0008,
        (
            '#0160000217V#080F你们还不去协会那里？\n',
            '雪拉扎德不是在等着你们过去吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_987(): pass

    label('loc_987')

    ChrSetSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x990
@scena.Code('func_04_990')
def func_04_990():
    OP_24(0x01C2, 0x46)
    OP_72(0x0000, 0x0020)
    OP_6F(0x0000, 5)
    EventBegin(0x00)
    MapClearFlags(0x00000001)
    ChrSetFlags(0x0101, 0x0008)
    PlaySE(202, 0x00, 0x64)
    CameraMove(-1590, 0, 1830, 4000)
    Sleep(1000)

    OP_0D()
    Fade(1000)
    ChrClearFlags(0x0008, 0x0020)
    ChrClearFlags(0x0008, 0x0010)
    CameraMove(148000, 540, 145400, 0)
    OP_67(0, 5940, -10000, 0)
    CameraSetDistance(3120, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_62(0x0101, 0x00000258, 1200, 0x1C, 0x21, 0x000000FA, 0x00)
    Sleep(2000)

    OP_63(0x0101)
    ChrSetDirection(0x000A, 45, 0)
    ChrSetFlags(0x000A, 0x0020)
    ChrSetFlags(0x000A, 0x0002)
    OP_99(0x000A, 0x0F, 0x10, 1000)
    OP_24(0x01C2, 0x41)
    Sleep(1000)

    OP_23(0x01C2)
    OP_61(0x0101)

    ChrTalk(
        0x000A,
        (
            '#0010000110V#459F……呜～……好刺眼呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0A8D')
    def lambda_0A8D():
        OP_99(0x00FE, 0x00, 0x07, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0A8D)

    Sleep(200)

    OP_6F(0x0000, 5)
    OP_70(0x0000, 20)
    Sleep(1500)

    @scena.Lambda('lambda_0AB5')
    def lambda_0AB5():
        OP_99(0x00FE, 0x08, 0x0C, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0AB5)

    ChrTalk(
        0x000A,
        (
            '#0010000111V#458F#3S#15A……呼哇啊啊啊啊啊啊～……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    OP_9E(0x000A, 15, 0, 2000, 4000)

    @scena.Lambda('lambda_0B10')
    def lambda_0B10():
        OP_99(0x00FE, 0x0C, 0x0E, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0B10)

    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '#0010000112V#455F嗯～～睡得真舒服～～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Sleep(1000)

    OP_99(0x000A, 0x11, 0x12, 1000)
    Sleep(400)

    ChrTalk(
        0x000A,
        (
            '#0010000113V#457F……对了………\n',
            '今天早上轮到老爸做饭。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000114V那么……\n',
            '也就是说约修亚还在睡觉吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_20(0x000005DC)
    OP_21()
    PlayBGM(70)
    OP_1F(0x50, 0x000000C8)
    Sleep(2000)

    OP_62(0x000A, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_99(0x000A, 0x13, 0x15, 1000)

    ChrTalk(
        0x000A,
        (
            '#0010000115V#450F啊哈，好像已经起来了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(1000)

    OP_99(0x000A, 0x16, 0x17, 1000)

    ChrTalk(
        0x000A,
        (
            '#0010000116V#454F好的……\n',
            '我也赶快起床吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    MapSetFlags(0x02000000)
    NewScene('ED6_DT01/T0300._SN', 1, 0, 0)
    IdleLoop()

    Return()

# id: 0x0005 offset: 0xC86
@scena.Code('func_05_C86')
def func_05_C86():
    EventBegin(0x00)
    CameraMove(-3500, 0, 1700, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FormationAddMember(0x01, 0xFF)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetPos(0x0102, -4460, 0, 230, 0)
    MapClearFlags(0x00000001)
    CreateThread(0x0101, 0x00, 0x00, func_06_1A95)
    CreateThread(0x0009, 0x00, 0x00, func_07_1B1E)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_67(0, 7000, -11000, 3000)
    OP_A5(0x0000)

    ChrTalk(
        0x000A,
        (
            '#0010000156V#001F我吃饱啦～！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000157V#001F嗯……\n',
            '肚子已经鼓鼓的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0009, 2)
    Sleep(300)

    ChrTalk(
        0x0009,
        (
            '#0020000158V#010F#6P一大早你就吃这么多……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x000A, 1)
    Sleep(300)

    ChrTalk(
        0x000A,
        (
            '#0010000159V#502F不行吗？\n',
            '能吃能睡的孩子才健康嘛⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160000160V#080F说的也是，\n',
            '吃饱了才有精神去做事哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160000161V#080F对了，\n',
            '你们今天不是要去协会做最后的研修吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0009, 0)
    ChrSetSubChip(0x000A, 0)
    Sleep(300)

    ChrTalk(
        0x0009,
        (
            '#0020000162V#010F#6P嗯。\n',
            '就是复习至今为止学到的知识。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0010000163V#006F最重要的是，过了研修之后呢，\n',
            '我们就和老爸一样是『游击士』啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000164V以后再也不会被当成小孩子啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160000165V#080F哼哼，你们还太嫩了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160000166V开始的时候也不过是『准游击士』，\n',
            '也就是见习而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160000167V要想独当一面的话，\n',
            '就得早日成为『正游击士』才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0010000168V#009F呵呵，这正合我意呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000169V等着瞧吧～\n',
            '我一定会做出很多成绩来的，\n',
            '然后超越老爸！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160000170V#081F哈哈哈。\n',
            '做得到的话就试试看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0009, 2)
    Sleep(300)

    ChrTalk(
        0x0009,
        (
            '#0020000171V#017F#6P这有什么好争的啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000172V#010F艾丝蒂尔，绝对不能小看今天的复习。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000173V#010F复习研修之后，\n',
            '还有一场考试等着我们呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x000A, 1)
    Sleep(300)

    ChrTalk(
        0x000A,
        (
            '#0010000174V#004F啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000175V……………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000176V#501F考试……有这回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#0020000177V#018F#6P难，难道说……\n',
            '你已经把这件事忘掉了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000178V那可是考察我们有没有\n',
            '在研修里学到东西的测验啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000179V要是不合格的话就要重新补习，\n',
            '雪拉姐姐之前不是说过吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '#0010000180V#505F糟了～……\n',
            '忘得一干二净了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000181V听你这么一说，\n',
            '我也觉得雪拉姐好像是说过这件事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000182V#001F不怕不怕，车到山前必有路☆',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0020000183V#017F#6P唉，你啊……\n',
            '该说你是天性乐观呢，还是思想单纯呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160000184V#083F真拿你没办法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160000185V这种乐天的性格，\n',
            '到底像谁呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x000A, 0)
    Sleep(300)

    ChrTalk(
        0x000A,
        (
            '#0010000186V#009F真、真讨厌～\n',
            '比起老爸你来我还算好的呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0020000187V#017F#6P简直就是一个模子里刻出来的父女。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000188V#010F好了好了。\n',
            '艾丝蒂尔，差不多该去城里了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000189V#010F雪拉姐姐还在协会等着呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x000A, 1)
    Sleep(300)

    ChrTalk(
        0x000A,
        (
            '#0010000190V#006F嗯，知道了。\n',
            '让雪拉姐等太久可就惨了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Sleep(200)

    Fade(1000)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    Sleep(200)

    CameraMove(-5050, 0, -70, 4000)
    OP_A5(0x0000)

    ChrTalk(
        0x0101,
        (
            '#0010000191V#006F啊～对了老爸。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000192V今天晚上轮到我做饭哦，\n',
            '想吃点什么呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000193V别客气，想吃什么尽管说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160000194V#085F嗯，想吃的东西嘛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160000195V#085F………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160000196V#080F我想吃点卢安风味的……\n',
            '就来个香醋烤鱼怎样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000197V#004F那、那是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0020000198V#019F对艾丝蒂尔来说，\n',
            '要做那个也许太难了点吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160000199V#081F算了，只是随便说说而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160000200V和平常一样，\n',
            '做点炸鱼和煎蛋什么的就行了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160000201V不用太过勉强，\n',
            '做出来能吃进肚子就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000202V#509F谁说我不会做的啊……\n',
            '你、你就不能少说点吗，讨厌……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160000203V#080F对了，还要拜托你一件事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160000204V到了城里，帮我到杂货铺\n',
            '买本叫《利贝尔通讯》的杂志。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160000205V最新一期今天应该到货了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000206V#006F明白了。\n',
            '《利贝尔通讯》对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_182C')
    def lambda_182C():
        CameraMove(-5870, 0, 1160, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_182C)

    ChrWalkTo(0x0101, -6680, 0, 2158, 2000, 0x00)
    ChrTurnDirection(0x0101, 0x0008, 500)
    ChrSetSubChip(0x0008, 1)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x4),
            '５００',
            (TxtCtl.SetColor, 0x0),
            '米拉。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    AddMira(500)
    AddItem(0x035F, 1)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0008,
        (
            '#0160000207V#080F剩下的就给你们当零花钱吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160000208V#080F不过可别乱花哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010000209V#001F太好了，谢谢老爸！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1951')
    def lambda_1951():
        CameraMove(-4460, 0, 230, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1951)

    ChrWalkTo(0x0101, -4460, 0, 230, 2000, 0x00)
    ChrSetSubChip(0x0008, 0)
    ChrTurnDirection(0x0101, 0x0008, 500)

    ChrTalk(
        0x0009,
        (
            '#0020000210V#010F那么爸爸，我们走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160000211V#080F哦，好好干。\n',
            '代我向雪拉扎德问好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeOut(1000, 0, -1)
    OP_0D()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x0008, 0xFF)
    ChrClearFlags(0x0101, 0x0004)
    ChrClearFlags(0x0009, 0x0004)
    ChrSetFlags(0x0008, 0x0010)
    SetScenaFlags(ScenaFlag(0x0040, 2, 0x202))
    ChrClearFlags(0x0102, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x0009, 0x0008)
    MapClearFlags(0x02000000)
    CameraMove(-2770, 0, -440, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ChrSetPos(0x0101, -2770, 0, -440, 180)
    ChrSetPos(0x0102, -2770, 0, -440, 180)
    FadeIn(1000, 0)
    MapClearFlags(0x00400000)
    EventEnd(0x00)

    Return()

# id: 0x0006 offset: 0x1A95
@scena.Code('func_06_1A95')
def func_06_1A95():
    OP_A6(0x0000)
    CameraMove(-8500, 0, 1700, 3000)
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_A6(0x0000)
    ChrClearFlags(0x00FE, 0x0008)
    ChrSetFlags(0x000A, 0x0008)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetPos(0x00FE, -8810, 0, -1170, 180)
    Sleep(200)

    ChrWalkTo(0x00FE, -8550, 0, -2200, 2000, 0x00)
    ChrWalkTo(0x00FE, -4460, 0, 230, 2000, 0x00)
    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(1000)

    ChrTurnDirection(0x00FE, 0x0008, 500)
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Return()

# id: 0x0007 offset: 0x1B1E
@scena.Code('func_07_1B1E')
def func_07_1B1E():
    OP_A6(0x0001)
    ChrSetChipByIndex(0x00FE, 1)
    ChrSetPos(0x00FE, -10410, 0, -800, 180)
    Sleep(200)

    ChrWalkTo(0x00FE, -10370, 0, -1920, 2000, 0x00)
    ChrWalkTo(0x00FE, -7230, 0, -1920, 2000, 0x00)
    ChrWalkTo(0x00FE, -3550, 0, -1010, 2000, 0x00)
    Sleep(300)

    ChrTurnDirection(0x00FE, 0x0008, 500)
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x0008 offset: 0x1B88
@scena.Code('func_08_1B88')
def func_08_1B88():
    EventBegin(0x00)
    CreateThread(0x0101, 0x00, 0x00, func_09_2540)
    CreateThread(0x0102, 0x00, 0x00, func_0A_2601)
    CreateThread(0x0008, 0x00, 0x00, func_0B_26A5)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010001106V#501F我们回来了～老爸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    OP_A5(0x0001)
    OP_A5(0x0000)

    ChrTalk(
        0x0101,
        (
            '#0010001107V#006F#2P工作报告也已经完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0008, 1)
    Sleep(100)

    ChrTalk(
        0x0008,
        (
            '#0160001108V#080F#5P嗯，辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001109V#080F报告内容会在各支部进行评测，\n',
            '报酬和升级之类的也会受其影响。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001110V#080F这点你们要记住才行哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001111V#006F#2P知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001112V#501F对了老爸。\n',
            '《利贝尔通讯》买回来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001113V#501F而且还有协会要我转交的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_A5(0x0000)
    ChrSetDirection(0x0101, 270, 400)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '利贝尔通讯',
            (TxtCtl.SetColor, 0x0),
            '和',
            (TxtCtl.SetColor, 0x2),
            '致卡西乌斯的信',
            (TxtCtl.SetColor, 0x0),
            '。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(0x0347, 1)
    RemoveItem(0x0336, 1)

    ChrTalk(
        0x0008,
        (
            '#0160001114V#084F#5P唔，是信啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001115V#000F#2P好了，\n',
            '我还要去准备晚饭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_A5(0x0000)

    ChrTalk(
        0x0101,
        (
            '#0010001116V#004F#5P啊，对了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)
    ChrSetDirection(0x0101, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010001117V#008F#2P……今天谢谢老爸你了。\n',
            '在危急的时候救了我们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160001118V#084F#5P呵呵，今天真是一反常态，这么乖啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001119V你终于理解为父的伟大了，\n',
            '真是件令人高兴的事情。 ',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001120V#081F来吧女儿，不必客气。\n',
            '飞扑到爸爸怀里来尽情撒娇吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010001121V#582F#2P不要得意忘形！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001122V#509F真是的，\n',
            '为什么这家里的男人都只会耍嘴皮子啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1FD7')
    def lambda_1FD7():
        CameraMove(6187, 0, 70000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1FD7)

    MapSetFlags(0x00400000)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    Sleep(300)

    ChrSetSubChip(0x0008, 0)
    OP_A5(0x0000)
    OP_A5(0x0001)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0160001123V#080F#5P看起来并没有我想象得那么沮丧嘛……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001124V约修亚，是因为你吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0008, 400)

    ChrTalk(
        0x0102,
        (
            '#0020001125V#010F#2P其实我也没做什么。\n',
            '只是稍微鼓励了她一下吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001126V她本来就很坚强的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160001127V#085F#5P哼，还太嫩了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001128V做游击士这种工作，\n',
            '感到迷茫肯定是经常会有的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001129V#082F要独当一面就得跨过这些门槛才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001130V#019F#2P呵呵，您就是那么为女儿着想。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    PlaySE(151, 0x00, 0x64)
    Sleep(1500)

    NpcTalk(
        0x0101,
        '艾丝蒂尔的声音',
        (
            '#0010001131V#1P惨了～……\n',
            '还得再重来一遍啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    NpcTalk(
        0x0101,
        '艾丝蒂尔的声音',
        (
            '#0010001132V#1P突然挑战这个菜式，\n',
            '对我来说真的那么难吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0101,
        '艾丝蒂尔的声音',
        (
            '#0010001133V#1P不对，做料理要靠气势！\n',
            '无论失败多少次都要继续挑战！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0008, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0160001134V#083F#5P真是的……\n',
            '我这个沉不住气的女儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0008, 400)

    ChrTalk(
        0x0102,
        (
            '#0020001135V#010F#2P我去帮她一下吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001136V#010F这样下去，\n',
            '都不知道什么时候才能吃饭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    OP_A5(0x0001)

    ChrTalk(
        0x0008,
        (
            '#0160001137V#080F#5P呵呵……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001138V#085F……好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CameraMove(5500, 0, 72500, 1500)
    Sleep(500)

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '卡西乌斯把信封打开。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    Sleep(1000)

    OP_20(0x00000BB8)

    ChrTalk(
        0x0008,
        (
            '#0160001139V#080F#5P嗯……\n',
            '是帝国那边寄来的联络信啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001140V#080F………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001141V#082F………………………………\n',
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_21()

    ChrTalk(
        0x0008,
        (
            '#0160001142V#086F#5P#3S……什么……！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    FadeOut(500, 0, -1)
    OP_0D()
    Sleep(500)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0008, 0xFF)
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T0311._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0009 offset: 0x2540
@scena.Code('func_09_2540')
def func_09_2540():
    OP_A6(0x0000)
    ChrWalkTo(0x00FE, 5522, 0, 70452, 3000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_A6(0x0000)
    ChrWalkTo(0x00FE, 4226, 0, 71132, 2000, 0x00)
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_A6(0x0000)
    ChrWalkTo(0x00FE, 5522, 0, 70452, 2000, 0x00)
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_A6(0x0000)
    ChrWalkTo(0x00FE, 3451, 0, 67219, 4000, 0x01)
    ChrWalkTo(0x00FE, 2980, 0, 66310, 4000, 0x01)

    @scena.Lambda('lambda_25C6')
    def lambda_25C6():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_25C6)

    ChrWalkTo(0x00FE, 2980, 0, 64220, 2000, 0x01)
    ChrSetFlags(0x00FE, 0x0080)
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    ClearScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_A6(0x0000)
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_A6(0x0000)
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Return()

# id: 0x000A offset: 0x2601
@scena.Code('func_0A_2601')
def func_0A_2601():
    OP_A6(0x0001)
    Sleep(500)

    ChrWalkTo(0x00FE, 5703, 0, 69197, 3000, 0x00)
    ChrTurnDirection(0x00FE, 0x0008, 400)
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    OP_A6(0x0001)
    def _loc_262A(): pass

    label('loc_262A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_263C',
    )

    ChrTurnDirection(0x00FE, 0x0101, 0)
    Yield()

    Jump('loc_262A')

    def _loc_263C(): pass

    label('loc_263C')

    OP_A6(0x0001)
    ChrWalkTo(0x00FE, 3451, 0, 67219, 3000, 0x01)
    ChrWalkTo(0x00FE, 2980, 0, 66310, 3000, 0x01)

    @scena.Lambda('lambda_266D')
    def lambda_266D():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_266D)

    ChrWalkTo(0x00FE, 2980, 0, 64220, 2000, 0x01)
    ChrSetFlags(0x00FE, 0x0080)
    ClearScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    OP_A6(0x0001)
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    OP_A6(0x0001)
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x000B offset: 0x26A5
@scena.Code('func_0B_26A5')
def func_0B_26A5():
    OP_A6(0x0002)
    def _loc_26A8(): pass

    label('loc_26A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_26BA',
    )

    ChrTurnDirection(0x00FE, 0x0101, 0)
    Yield()

    Jump('loc_26A8')

    def _loc_26BA(): pass

    label('loc_26BA')

    OP_A6(0x0002)
    def _loc_26BD(): pass

    label('loc_26BD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_26CF',
    )

    ChrTurnDirection(0x00FE, 0x0102, 0)
    Yield()

    Jump('loc_26BD')

    def _loc_26CF(): pass

    label('loc_26CF')

    OP_A6(0x0002)
    ClearScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    OP_A6(0x0002)
    ClearScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Return()

# id: 0x000C offset: 0x26DC
@scena.Code('func_0C_26DC')
def func_0C_26DC():
    CameraMove(-7500, 0, 1700, 0)
    ChrSetPos(0x0101, -7950, 0, -500, 0)
    ChrSetPos(0x0102, -9310, 0, -300, 0)
    ChrSetPos(0x000A, -8230, 200, -520, 0)
    ChrSetPos(0x0009, -9550, 200, -520, 0)
    ChrSetPos(0x0008, -8100, 200, 2200, 180)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x0101, 0x0008)
    ChrSetFlags(0x0102, 0x0008)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetFlags(0x000A, 0x0004)
    ChrSetFlags(0x0009, 0x0004)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0008)
    ChrClearFlags(0x0009, 0x0008)
    ChrSetChipByIndex(0x000A, 8)
    ChrSetChipByIndex(0x0009, 9)
    ChrSetSubChip(0x000E, 0)
    ChrSetSubChip(0x000F, 0)
    ChrSetSubChip(0x0010, 0)
    ChrSetSubChip(0x0014, 8)
    ChrSetPos(0x000E, -8360, 700, 300, 0)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x0011, -7860, 700, 200, 0)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x000F, -9620, 700, 300, 0)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x0012, -9120, 700, 200, 0)
    ChrClearFlags(0x0012, 0x0080)
    ChrSetPos(0x0010, -8260, 700, 1100, 0)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0013, -8860, 700, 1200, 0)
    ChrClearFlags(0x0013, 0x0080)
    ChrSetPos(0x0014, -9520, 700, 1100, 0)
    ChrClearFlags(0x0014, 0x0080)
    FadeIn(1000, 0)
    PlayBGM(84)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0160001143V#084F哦，真是不可思议啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1700, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#502F怎么样，这可是艾丝蒂尔特制的\n',
            '香滑美味的鸡肉蛋包饭！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#502F请用心品味哦⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0009, 2)
    Sleep(300)

    ChrTalk(
        0x0102,
        (
            '#019F#6P嗯。\n',
            '味道真的很好啊，这个。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001147V#019F做得不错嘛，艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x000A, 1)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#001F哼哼，这就是我的真正实力哦㈱',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#001F啊～虽然发生了很多事，\n',
            '不过今天还真是很棒的一天啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#001F得到了游击士的资格，\n',
            '完成了自己的第一份任务……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001151V#001F蛋包饭也成功了⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#081F嗯……\n',
            '第一次做的竟然还能入口。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001153V#081F本来已经做好心理准备了，有点意外啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x000A, 0)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#009F好讨厌啊～\n',
            '直接说好吃不就行了嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160001155V#080F嗯，\n',
            '真没想到能在出发前吃到这么好的东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001156V#080F做得很不错，艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140734V#001F嘿嘿……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#001F……………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001159V#501F……出发前？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0009, 0)
    Sleep(300)

    ChrTalk(
        0x0102,
        (
            '#014F#6P爸爸，难道您……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160001161V#080F嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#080F突然接到了紧急任务。\n',
            '我又要暂时离家外出了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#004F等、等一下！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#004F那……什么时候出发？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160001165V#080F明天就走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001166V#005F什么～！？\n',
            '再怎么说这也太急了吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#012F#6P是因为今天那封信吧……\n',
            '难道出了什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#080F没什么……单纯的调查而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#080F要到很多地方去看看，\n',
            '大概要花一个月左右的时间吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001170V#080F就是这样，又要拜托你们看家了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1700, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#005F什么『就是这样』啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#003F老爸真是的，\n',
            '每次都自作主张……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#015F#6P没办法啊，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#015F接到任务就要立刻行动，\n',
            '因为工作报告也是游击士应履行的职责。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#002F这我知道啊……\n',
            '可是洛连特支部的工作该怎么办呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#002F很多工作……应该也还没做完吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160001177V#080F嗯，大概有五、六件吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001178V#080F我也考虑过这个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001179V#080F不然你们代替我，\n',
            '去试着完成这其中几个任务吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001180V#004F啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001181V#004F就是说让我们来做\n',
            '本该由老爸去做的工作？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160001182V#080F嗯，\n',
            '给你们几个新手也可以应付得来的任务。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001183V#080F其余那些难度高点的工作\n',
            '我就交给雪拉扎德帮忙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001184V#080F怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

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
            TXT(0x00, '『我一定会做好的！』\n'),
            TXT(0x01, '『虽然想试试看……』\n'),
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
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_303E'),
        (0x00000001, 'loc_3376'),
        (-1, 'loc_3668'),
    )

    def _loc_303E(): pass

    label('loc_303E')

    ChrTalk(
        0x0101,
        (
            '#0010001185V#001F我一定会做好的！\n',
            '而且一定会比之前做得更好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x000A, 1)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010001186V#501F对不对？约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0009, 2)
    Sleep(300)

    ChrTalk(
        0x0102,
        (
            '#010F#6P嗯。\n',
            '而且我觉得这是难得的锻炼机会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160001188V#080F就这么定了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001189V#080F明天出发前，\n',
            '我会亲自向协会说明一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0009, 0)
    ChrSetSubChip(0x000A, 0)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010001190V#006F嗯。\n',
            '我觉得现在充满了干劲呢！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001191V#006F我们可不能让老爸丢脸，\n',
            '一定全力以赴把几个任务做好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160001192V#084F啊啊，艾丝蒂尔……\n',
            '你这一番话太让我感动了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001193V#085F在天国的孩子她妈，你看到了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#085F我们的女儿终于长大了，\n',
            '是一个又懂事又听话的好孩子呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001195V#007F我说老爸你年纪也不小了，\n',
            '怎么老是把我当成小孩子看待啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#007F帮助父亲去完成工作是女儿应该做的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160001197V#086F我今年才不过是４５而已！\n',
            '而且还是协会里现役的游击士！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#017F#6P啊……这对父女又在对唱了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Jump('loc_3668')

    def _loc_3376(): pass

    label('loc_3376')

    ChrTalk(
        0x0101,
        (
            '#003F虽然想试试看……\n',
            '不过一想到万一失败的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#003F真的是我们这种新人\n',
            '也可以应付得来的工作吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160001203V#080F相对来说都是比较简单的，\n',
            '不过其中也会有性命攸关的工作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001204V#080F我不强求你们。\n',
            '可以再好好考虑一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#002F……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x000A, 1)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010001206V#002F约修亚你觉得怎样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0009, 2)
    Sleep(300)

    ChrTalk(
        0x0102,
        (
            '#010F#6P我赞成。\n',
            '而且这是一次难得的锻炼机会。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#010F确实我们的能力都有所不足，\n',
            '不过我想一起行动的话应该没问题的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#010F我们两个人齐心协力的话，\n',
            '应该可以取长补短。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001210V#501F齐心协力取长补短……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001211V#006F嗯，说得对啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x000A, 0)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#001F老爸！\n',
            '我也要试试看！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001213V#001F老实说是跃跃欲试啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160001214V#080F就这么定了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001215V#080F明天出发前，\n',
            '我会亲自向协会说明一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0009, 0)
    Sleep(300)

    Jump('loc_3668')

    def _loc_3668(): pass

    label('loc_3668')

    ChrTalk(
        0x0102,
        (
            '#010F#6P对了爸爸。\n',
            '你明天要坐哪艘定期船啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001217V#010F去王都的？\n',
            '还是去柏斯的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160001218V#080F去王都的。\n',
            '明早１０点出发。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#001F这样啊……\n',
            '那明天要早点起来才行呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001220V#001F我还是先调好闹钟吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(500)

    OP_21()
    ChrClearFlags(0x0101, 0x0080)
    ChrClearFlags(0x0102, 0x0080)
    ChrClearFlags(0x0101, 0x0008)
    ChrClearFlags(0x0102, 0x0008)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0008, 0xFF)
    Call(0, 0x000D)

    Return()

# id: 0x000D offset: 0x3787
@scena.Code('func_0D_3787')
def func_0D_3787():
    PlayBGM(84)
    ChrSetFlags(0x0101, 0x0004)
    ChrClearFlags(0x0101, 0x0080)
    ChrSetFlags(0x0101, 0x0008)
    ChrSetPos(0x0101, 67000, 300, 35500, 225)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x0008, 0x0080)
    OP_77(0x07, 0x45, 0x91, 0x00, 0x00000000)
    ChrSetPos(0x000A, 148000, 520, 145400, 315)
    ChrSetChipByIndex(0x000A, 2)
    ChrSetSubChip(0x000A, 0)
    ChrClearFlags(0x000A, 0x0008)
    ChrClearFlags(0x000A, 0x0080)
    OP_69(0x000A, 0)
    Sleep(1000)

    FadeIn(2000, 0)
    OP_0D()
    Sleep(1000)

    OP_62(0x000A, 0x00000000, 1700, 0x1C, 0x21, 0x000000FA, 0x00)
    Sleep(3000)

    MapSetFlags(0x02000000)
    NewScene('ED6_DT01/T0300._SN', 2, 0, 0)
    IdleLoop()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0008, 0xFF)

    Return()

# id: 0x000E offset: 0x382E
@scena.Code('func_0E_382E')
def func_0E_382E():
    OP_77(0x5A, 0x5A, 0x7D, 0x00, 0x00000000)
    FormationAddMember(0x00, 0xFF)
    FormationAddMember(0x01, 0xFF)
    FormationAddMember(0x02, 0xFF)
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    MapSetFlags(0x00400000)
    ChrSetFlags(0x0103, 0x0080)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x0101, 0x0040)
    ChrSetFlags(0x0102, 0x0040)
    ChrSetFlags(0x0103, 0x0040)
    ChrSetPos(0x000B, -7995, 0, 2276, 180)
    OP_69(0x000B, 0)
    CameraSetDistance(3300, 0)
    FadeIn(2000, 0)
    Sleep(2000)

    @scena.Lambda('lambda_389F')
    def lambda_389F():
        CameraSetDistance(2500, 7000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_389F)

    Sleep(2000)

    Fade(5000)
    ChrClearFlags(0x000B, 0x0080)
    OP_77(0xFF, 0xC8, 0x96, 0x00, 0x00000000)
    OP_0D()
    WaitForThreadExit(0x0000, 0x0001)
    OP_66(0x0000)
    Sleep(1000)

    ChrTalk(
        0x000B,
        (
            '#290F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000002V爸爸怎么还没回来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000003V协会捎来的口信\n',
            '明明说他今天会回家的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(400)
    Sleep(1000)

    @scena.Lambda('lambda_3947')
    def lambda_3947():
        CameraMove(-7866, 1000, 5490, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_3947)

    ChrSetDirection(0x000B, 90, 0)
    ChrJumpToRelative(0x000B, 1000, 0, 0, 600, 6000)
    Sleep(500)

    ChrWalkTo(0x000B, -6615, 0, 2910, 3000, 0x00)
    ChrWalkTo(0x000B, -7866, 0, 5490, 3000, 0x00)
    Sleep(1500)

    ChrTalk(
        0x000B,
        (
            '#290F雪拉姐也还在\n',
            '周游王国的修行旅途中……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '唉～真无聊。\n',
            '再练习一下棒术吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(15, 0x00, 0x64)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, -1550, 0, -3450, 0)
    Sleep(500)

    NpcTalk(
        0x0008,
        '男性的声音',
        (
            '#0160000006V哟，我回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetDirection(0x000B, 180, 400)

    ChrTalk(
        0x000B,
        (
            '#291F爸爸！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3A7F')
    def lambda_3A7F():
        CameraMove(-1110, 0, -1690, 2500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_3A7F)

    ChrWalkTo(0x000B, -2190, 0, -1390, 4000, 0x00)
    ChrSetDirection(0x000B, 180, 400)

    ChrTalk(
        0x0008,
        (
            '#0160000008V#080F#4P我回来了，艾丝蒂尔。\n',
            '让你等急了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160000009V有没有乖乖地看家啊，我的乖女儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#290F#1P哼哼，当然有啦☆',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000011V#290F爸爸你也没什么事吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000012V和魔兽战斗没受伤吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160000013V#080F#4P当然啦，你瞧，我不是精神得很吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160000014V对了，艾丝蒂尔。\n',
            '我这次给你带回一样礼物哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#291F#1P啊，真的！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000016V钓鱼竿？还是运动鞋？\n',
            '要不然就是棒术用具！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160000017V#083F#4P…………………………\n',
            '唉，我是不是真的教女无方呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160000018V你啊，一个女孩子家，\n',
            '难道不想要衣服或者首饰之类的东西吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#290F#1P我当然喜欢漂亮的衣服呀，\n',
            '不过，再漂亮的衣服一会儿就弄脏了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000020V首饰也是一样哦，\n',
            '活动的时候很容易就会坏掉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000021V对了，爸爸。\n',
            '你抱着这么大的毛毯做什么呀……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000022V难道说……那就是给我的礼物？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160000023V#080F#4P呵呵，你眼睛真尖……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160000024V#080F嘿嘿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '卡西乌斯将抱在手里的毛毯掀开。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    @scena.Lambda('lambda_3E4E')
    def lambda_3E4E():
        CameraMove(-400, 0, -2200, 1200)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_3E4E)

    Sleep(2000)

    NpcTalk(
        0x0008,
        '男孩',
        (
            '#305F#2P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#293F#1P…………啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000027V……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160000028V#081F#4P看，就是这个了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160000029V很帅的小伙子吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#293F#1P什、什、什……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#294F#4S什么呀，这男孩！？#2S',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160000032V#080F#4P别这么大声，\n',
            '不然会把他吵醒的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#292F#1P吵醒……\n',
            '这孩子还活着吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000034V看起来很虚弱的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160000035V#080F#4P我已经给他包扎好伤口了，\n',
            '这小子应该不会有生命危险的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160000036V不过，总而言之……\n',
            '还是先让他好好休息一下才行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160000037V我把他抱到床上去，\n',
            '艾丝蒂尔你赶快去烧些开水。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#291F#1P嗯，知道了～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    OP_66(0x0001)
    ChrSetFlags(0x000B, 0x0040)
    CameraMove(8550, 0, 69460, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(44000, 0)
    OP_6E(280, 0)
    ChrSetPos(0x000B, 8900, 0, 68600, 180)
    ChrSetPos(0x0008, 8550, 0, 69460, 180)
    ChrSetPos(0x000C, 9300, 0, 67150, 270)
    ChrClearFlags(0x000C, 0x0080)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x000B,
        (
            '#290F#2P睡得真香啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000040V这男孩……\n',
            '和我差不多大吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000041V这么乌黑的头发，\n',
            '我还是头一次见呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160000042V#080F确实是很漂亮的黑发啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160000043V而且眼睛还是琥珀色的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#290F#2P嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000B, 0, 400)

    ChrTalk(
        0x000B,
        (
            '#292F#2P先不说这个……\n',
            '现在该把事情交代清楚了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160000046V#084F噢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#292F#2P这小男孩到底是谁？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000048V为什么他会受伤？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000049V还有，\n',
            '为什么爸爸你要把他带回家来？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000050V难道是私生子？\n',
            '难道你背叛了妈妈！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160000051V#083F唉……\n',
            '我说你到底是从哪学来这些话的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160000052V#080F一定是那个雪拉扎德教的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#291F#2P嗯，没错！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160000054V#080F那个不知天高地厚的女人也真是的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160000055V#080F其实爸爸我也是\n',
            '因为工作关系才认识这孩子的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160000056V我连他的名字都还不知道呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#290F#2P工作？是指游击士的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160000058V#080F是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160000059V哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#293F#2P啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160000061V#080F好像醒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x000C, 400)
    CameraMove(8900, 0, 68600, 2000)

    ChrTalk(
        0x000C,
        (
            '#0020000062V#306F嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0010000063V#293F哇，真的是琥珀色哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0020000064V#301F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#301F…………这里是…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160000066V#080F小子，你醒了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160000067V这里是我家。\n',
            '总之你放心就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#300F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#300F……你这是什么意思？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0010000070V#293F哈？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#300F简直无法理解……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#300F为什么这样做……\n',
            '你其实可以丢下我不管呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160000073V#084F你问为什么啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160000074V#081F也许是所谓的理所当然吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0020000075V#302F别、别开玩笑了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000076V#302F卡西乌斯·布莱特！\n',
            '你知道自己在做什么吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0010000077V#294F喂！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x000B, 0x0004)
    ChrJumpToRelative(0x000B, 0, 700, -1200, 1200, 6000)
    OP_7C(0, 100, 3000, 100)
    PlaySE(18, 0x00, 0x64)
    ChrJumpToRelative(0x000B, 0, -700, 1200, 200, 6000)

    ChrTalk(
        0x000B,
        (
            '#0010000078V#294F你一个受伤的小男孩\n',
            '别这么大声叫嚷好不好！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000079V你不知道这样会弄痛伤口的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0020000080V#304F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000081V#304F………………你是谁？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0010000082V#294F我叫艾丝蒂尔！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000083V艾丝蒂尔·布莱特！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160000084V#080F这是我的女儿。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160000085V之前不是和你说过吗。\n',
            '我有一个和你差不多大的女儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#304F好像提起过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000087V#302F现、现在是说这种事情的时候吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrJumpToRelative(0x000B, 0, 700, -1200, 1200, 6000)
    OP_7C(0, 100, 3000, 100)
    PlaySE(18, 0x00, 0x64)
    ChrJumpToRelative(0x000B, 0, -700, 1200, 200, 6000)
    ChrJumpToRelative(0x000B, 0, 700, -1200, 1500, 6000)
    OP_7C(0, 200, 3000, 100)
    PlaySE(18, 0x00, 0x64)
    ChrJumpToRelative(0x000B, 0, -700, 1200, 500, 6000)

    ChrTalk(
        0x000C,
        (
            '#0020000088V#303F疼啊☆',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0010000089V#294F不要那么大声！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0020000090V#300F知、知道了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000091V#300F但是你这么做……\n',
            '不是反而会让我伤口更痛吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0010000092V#292F你说什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0020000093V#300F我是说会伤上加伤……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#292F你·刚·才·说·什·么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0020000095V#304F没、没什么了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160000096V#081F呵呵，在这个家里\n',
            '千万不要和艾丝蒂尔作对哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160000097V她要是真的发起脾气来，\n',
            '连我也对付不了的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0020000098V#304F看得出来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0010000099V#292F对了，我说你。\n',
            '是不是忘了一件事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0020000100V#304F啊……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0010000101V#291F名字啊，你的名字。\n',
            '我刚才不是说了我的吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000102V你知道我的，我却不知道你的。\n',
            '这不公平！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0020000103V#304F……啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000104V#301F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160000105V#080F嗯，有道理。\n',
            '事到如今也没必要再隐瞒了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160000106V不知道名字也不方便，能告诉我们吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0020000107V#301F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#301F我……知道了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#301F我……我的名字是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(3000)
    OP_77(0x00, 0x00, 0x00, 0x00, 0x00000BB8)
    CameraSetDistance(3100, 3000)
    FadeOut(0, 0, -1)
    Sleep(2000)

    OP_77(0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ChrClearFlags(0x0101, 0x0080)
    ChrClearFlags(0x0102, 0x0080)
    ChrClearFlags(0x0103, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x0008, 0x0080)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    CameraMove(78732, 0, -740, 0)
    ChrSetPos(0x0102, 78554, 0, -1046, 0)
    ChrSetPos(0x0101, 78930, 0, 1500, 0)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0102,
        (
            '#0020020001V#013F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    PlaySE(16, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020020002V#010F艾丝蒂尔，你还好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020003V……约修亚？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020004V#010F晚饭已经准备好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020020005V顺便告诉你一声，\n',
            '今天晚上的菜是香酱烤鸡肉，\n',
            '还有你最喜欢的洋葱奶汁烤菜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020006V……听起来很丰盛呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020007V嗯，我一会儿就去，\n',
            '你们两个先吃吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020008V#010F这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020020009V我知道了。\n',
            '可别等菜都凉了才下来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(2000)
    ChrSetFlags(0x0101, 0x0040)
    ChrSetFlags(0x0102, 0x0040)
    ChrSetFlags(0x0103, 0x0040)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetFlags(0x0102, 0x0004)
    ChrSetFlags(0x0103, 0x0004)
    ChrSetChipByIndex(0x0103, 11)
    ChrSetPos(0x0102, 3066, 0, -2366, 0)
    ChrSetPos(0x0101, 3066, 0, -2366, 0)
    ChrSetPos(0x0103, -9810, 250, 2050, 200)
    CameraSetDistance(3000, 0)
    OP_69(0x0103, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x0103,
        (
            '#0030020010V#026F『命运之轮』……\n',
            '又是这张牌啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020011V看来，有什么事情正在发生，\n',
            '已经是无可置疑的事实了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020012V不过，现在还不知道是怎样的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0103, 0x00000000, 1700, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(1000)

    ChrSetSubChip(0x0103, 1)

    @scena.Lambda('lambda_5110')
    def lambda_5110():
        CameraMove(-7800, 1150, 1700, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_5110)

    ChrWalkTo(0x0102, -4630, 0, 250, 3000, 0x00)

    ChrTalk(
        0x0103,
        (
            '#0030020013V#023F啊，艾丝蒂尔怎样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#013F#2P刚才我叫她下来吃饭……\n',
            '不过她好像没什么食欲的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#022F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030840001V就算是平时多么活泼的女孩，\n',
            '遇到这种事情也承受不了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#013F#2P……这也是没办法的事啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020020018V不管怎么说，\n',
            '他们父女俩的感情那么好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020019V#026F是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020020V……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5296')
    def lambda_5296():
        CameraMove(-8020, 0, 1120, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5296)

    ChrWalkTo(0x0102, -7660, 0, -1790, 3000, 0x00)
    ChrWalkTo(0x0102, -10330, 0, -1440, 3000, 0x00)
    ChrSetSubChip(0x0103, 0)
    ChrWalkTo(0x0102, -10390, 0, -590, 3000, 0x00)
    Fade(1000)
    ChrSetFlags(0x0102, 0x0004)
    ChrSetChipByIndex(0x0102, 9)
    ChrSetPos(0x0102, -9550, 200, -520, 20)
    Sleep(1000)

    OP_62(0x0102, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    OP_63(0x0102)

    ChrTalk(
        0x0102,
        (
            '#012F#4P雪拉姐姐你是怎么想的？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020020022V这次的事件是单纯的事故，\n',
            '还是人为的案件……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#026F#1P……说实话，我也不能断定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030840002V老师是一流的游击士。\n',
            '对于任何突发的危机\n',
            '都有着十分果断的应付能力。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020025V不管是意外还是案件，\n',
            '只要有老师在场的话，\n',
            '都应该能够立刻解决掉的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '可是实际情况却是，\n',
            '定期船和老师都失踪了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#013F#4P不可能发生的事情却出现了……\n',
            '你是这个意思吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F#1P呵呵，不要这么沮丧嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020029V你应该更加振作起来，\n',
            '因为你现在是艾丝蒂尔唯一支柱啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020030V明天，我也要开始行动了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)

    ChrTalk(
        0x0101,
        (
            '#0010020031V#3P哈啊～真香啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020032V已经饿得受不了了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0103, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_21()
    PlayBGM(15)

    @scena.Lambda('lambda_55C8')
    def lambda_55C8():
        CameraMove(-5000, 0, 1000, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_55C8)

    ChrSetSubChip(0x0103, 1)
    Sleep(500)

    ChrSetSubChip(0x0102, 2)
    ChrWalkTo(0x0101, -4630, 0, 250, 3000, 0x00)

    ChrTalk(
        0x0102,
        (
            '#0020020033V#014F哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#023F#2P艾丝蒂尔……\n',
            '你没事了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020035V#007F不行啦不行啦。\n',
            '肚子已经快要饿扁了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020036V#501F哇～看上去好好吃呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_56AA')
    def lambda_56AA():
        CameraMove(-8590, 200, 780, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_56AA)

    ChrWalkTo(0x0101, -7480, 0, -530, 3000, 0x00)
    Fade(1000)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetChipByIndex(0x0101, 8)
    ChrSetPos(0x0101, -8230, 200, -520, 0)
    ChrSetSubChip(0x0103, 0)
    OP_0D()
    Sleep(500)

    OP_62(0x0101, 0x00000000, 1700, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#001F#2P我不客气啦～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0103, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0102, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    OP_63(0x0103)
    OP_63(0x0102)
    ChrSetSubChip(0x0101, 1)

    ChrTalk(
        0x0101,
        (
            '#501F#2P哎，你们怎么不吃啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '奶汁烤菜很好吃呢。\n',
            '洋葱的甜味也特别爽口。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020040V#001F不愧是约修亚。\n',
            '做得真不错⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#014F#3P过、过奖了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F#2P哎呀哎呀。\n',
            '雪拉姐也别客气了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '啊，老爸藏起来的\n',
            '白兰地你要不要喝点？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我记得好像是\n',
            '２０年陈酿的『圣蔷薇』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0103, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0103,
        (
            '#024F圣、圣蔷薇？\n',
            '而且还是２０年陈酿！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0102, 0)

    ChrTalk(
        0x0102,
        (
            '#017F#3P我说啊，雪拉姐姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#023F…………啊。\n',
            '咳咳，这个等会再说吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020048V#020F话说回来，你这是怎么了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020049V刚才约修亚去叫你，\n',
            '你不是不肯下来吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F#2P嗯？\n',
            '啊啊，我正在找替换用的内衣呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020051V因为一直忙着在里面找东西，\n',
            '所以没有注意啦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0102, 2)

    ChrTalk(
        0x0102,
        (
            '#018F#3P内、内衣？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#006F#2P而且还有套装旅行用具。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020054V虽然不知道能不能派上用场，\n',
            '不过不是有句话叫『有备无患』嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#014F#3P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#022F你难道要……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020057V为了确认老师的消息\n',
            '而打算去趟柏斯吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#006F#2P那当然啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020059V虽然觉得那个霉运超强的老爸\n',
            '不会发生什么事情……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020060V不过就这样干等着实在不是我的性格，\n',
            '所以想亲自去确认一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#011F#3P哈哈……\n',
            '你这孩子真是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020020062V#011F不知道该说是乐观呢，\n',
            '还是粗神经呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#006F#2P什么呀～真没礼貌。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '反正约修亚你\n',
            '一定会和我一起去吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F#3P那是当然的了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020020066V但是要知道，\n',
            '定期船在军队的搜索行动结束之前\n',
            '是不会恢复航运的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020020067V所以，我们要到柏斯去的话，\n',
            '也只能从街道上走过去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F#2P步行到柏斯……\n',
            '要花多长时间呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030840003V#026F按照游击士的脚力，\n',
            '快的话半天左右就能到了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#026F不过也真是的……\n',
            '这些话你应该早点说嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#020F我也正打算这么做呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#004F#2P哎……\n',
            '雪拉姐也要一起去吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020073V可是，工作不是很忙吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020074V#020F我可是卡西乌斯老师的徒弟哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020075V听说老师出了事，\n',
            '我怎么能够安心在这里留守呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020076V协会的工作，\n',
            '我已经拜托爱娜让其它的成员去做了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F#2P雪拉姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0102, 0)

    ChrTalk(
        0x0102,
        (
            '#010F#3P雪拉姐姐，谢谢你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030840004V#027F不用感谢我啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020080V这种事件交给新人去调查，\n',
            '我也放心不下啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#007F#2P呜～真不甘心……\n',
            '不过这样说好像也没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#000F算了，反正有雪拉姐一起，\n',
            '我们也更加放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F#3P那就请多关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F呵呵，彼此彼此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020085V#020F总之，\n',
            '明早出发前去一趟协会吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020086V必须向爱娜说明一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_21()
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '第一章『消失的定期船』',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T0121._SN', 103, 0, 0)
    IdleLoop()

    Return()

# id: 0x000F offset: 0x6037
@scena.Code('func_0F_6037')
def func_0F_6037():
    EventBegin(0x00)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrSetPos(0x0010, -8260, 700, 1100, 0)
    ChrSetPos(0x0014, -9520, 700, 1100, 0)
    ChrSetPos(0x0010, -8360, 800, 300, 0)
    ChrSetPos(0x0014, -9620, 800, 300, 0)
    ChrSetChipByIndex(0x0010, 13)
    ChrSetChipByIndex(0x0014, 12)
    ChrSetSubChip(0x0010, 0)
    ChrSetSubChip(0x0014, 0)

    ChrTalk(
        0x0000,
        (
            '0',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0010, 1)
    ChrSetSubChip(0x0014, 1)

    ChrTalk(
        0x0000,
        (
            '1',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0010, 2)
    ChrSetSubChip(0x0014, 2)

    ChrTalk(
        0x0000,
        (
            '2',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0010, 3)
    ChrSetSubChip(0x0014, 3)

    ChrTalk(
        0x0000,
        (
            '3',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0010, 4)
    ChrSetSubChip(0x0014, 4)

    ChrTalk(
        0x0000,
        (
            '4',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0010, 5)
    ChrSetSubChip(0x0014, 5)

    ChrTalk(
        0x0000,
        (
            '5',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0010, 6)
    ChrSetSubChip(0x0014, 6)

    ChrTalk(
        0x0000,
        (
            '6',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0010, 7)
    ChrSetSubChip(0x0014, 7)

    ChrTalk(
        0x0000,
        (
            '7',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0010, 8)
    ChrSetSubChip(0x0014, 8)

    ChrTalk(
        0x0000,
        (
            '8',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0010, 9)
    ChrSetSubChip(0x0014, 9)

    ChrTalk(
        0x0000,
        (
            '9',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0010, 10)
    ChrSetSubChip(0x0014, 10)

    ChrTalk(
        0x0000,
        (
            '10',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0010, 11)
    ChrSetSubChip(0x0014, 11)

    ChrTalk(
        0x0000,
        (
            '11',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0010, 12)
    ChrSetSubChip(0x0014, 12)

    ChrTalk(
        0x0000,
        (
            '12',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0010, 13)
    ChrSetSubChip(0x0014, 13)

    ChrTalk(
        0x0000,
        (
            '13',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0010, 14)
    ChrSetSubChip(0x0014, 14)

    ChrTalk(
        0x0000,
        (
            '14',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0010, 15)
    ChrSetSubChip(0x0014, 15)

    ChrTalk(
        0x0000,
        (
            '15',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0010, 16)
    ChrSetSubChip(0x0014, 16)

    ChrTalk(
        0x0000,
        (
            '16',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0010, 17)
    ChrSetSubChip(0x0014, 17)

    ChrTalk(
        0x0000,
        (
            '17',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0010, 18)
    ChrSetSubChip(0x0014, 18)

    ChrTalk(
        0x0000,
        (
            '18',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0010, 19)
    ChrSetSubChip(0x0014, 19)

    ChrTalk(
        0x0000,
        (
            '19',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0010, 20)
    ChrSetSubChip(0x0014, 20)

    ChrTalk(
        0x0000,
        (
            '20',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0010, 21)
    ChrSetSubChip(0x0014, 21)

    ChrTalk(
        0x0000,
        (
            '21',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0010, 22)
    ChrSetSubChip(0x0014, 22)

    ChrTalk(
        0x0000,
        (
            '22',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0010, 23)
    ChrSetSubChip(0x0014, 23)

    ChrTalk(
        0x0000,
        (
            '23',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0010, 24)
    ChrSetSubChip(0x0014, 24)

    ChrTalk(
        0x0000,
        (
            '24',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0010, 25)
    ChrSetSubChip(0x0014, 25)

    ChrTalk(
        0x0000,
        (
            '25',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0010, 26)
    ChrSetSubChip(0x0014, 26)

    ChrTalk(
        0x0000,
        (
            '26',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0010, 27)
    ChrSetSubChip(0x0014, 27)

    ChrTalk(
        0x0000,
        (
            '27',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0010, 28)
    ChrSetSubChip(0x0014, 28)

    ChrTalk(
        0x0000,
        (
            '28',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0010, 29)
    ChrSetSubChip(0x0014, 29)

    ChrTalk(
        0x0000,
        (
            '29',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0010, 30)
    ChrSetSubChip(0x0014, 30)

    ChrTalk(
        0x0000,
        (
            '30',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0010, 31)
    ChrSetSubChip(0x0014, 31)

    ChrTalk(
        0x0000,
        (
            '31',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x0014, 0x0080)
    EventEnd(0x00)

    Return()

# id: 0x0010 offset: 0x62D4
@scena.Code('func_10_62D4')
def func_10_62D4():
    FadeOut(300, 0, 100)

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
        1,
        (
            TXT(0x00, '休息\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_636D',
    )

    OP_20(0x00000BB8)
    FadeOut(1000, 0, -1)
    Sleep(700)

    PlaySE(13, 0x00, 0x64)
    OP_0D()
    ChrSetStatus(0x0000, 0xFE, 0)
    ChrSetStatus(0x0001, 0xFE, 0)
    ChrSetStatus(0x0002, 0xFE, 0)
    ChrSetStatus(0x0003, 0xFE, 0)
    ChrSetStatus(0x0004, 0xFE, 0)
    ChrSetStatus(0x0005, 0xFE, 0)
    ChrSetStatus(0x0006, 0xFE, 0)
    ChrSetStatus(0x0007, 0xFE, 0)
    Sleep(3500)

    OP_1E()
    FadeIn(1000, 0)
    OP_56(0x00)
    TalkEnd(0x00FF)

    Return()

    def _loc_636D(): pass

    label('loc_636D')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6387',
    )

    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

    def _loc_6387(): pass

    label('loc_6387')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

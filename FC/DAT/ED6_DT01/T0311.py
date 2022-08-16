import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T0311_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0311   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0311.x'
    header.mapIndex       = 15
    header.bgm            = 15
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

# id: 0x10000 offset: 0x174
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
        ('ED6_DT06/CH20056._CH', 'ED6_DT06/CH20056P._CP'),
        ('ED6_DT06/CH20033._CH', 'ED6_DT06/CH20033P._CP'),
        ('ED6_DT06/CH20133._CH', 'ED6_DT06/CH20133P._CP'),
    ]

# id: 0x10001 offset: 0x1FE
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
            npcIndex            = 0x01C1,
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
            npcIndex            = 0x01C6,
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
        ScenaNpcData(
            name                = '床',
            x                   = 8470,
            z                   = 0,
            y                   = 67140,
            direction           = 90,
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

# id: 0x10002 offset: 0x3DE
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x3DE
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x3DE
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
            talkFunctionIndex   = 0x0011,
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
            talkFunctionIndex   = 0x0011,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x426
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_435',
    )

    ChrSetFlags(0x0008, 0x0080)

    Jump('loc_52D')

    def _loc_435(): pass

    label('loc_435')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_455',
    )

    ChrSetFlags(0x0008, 0x0004)
    ChrSetPos(0x0008, 3554, 0, 71683, 161)

    Jump('loc_52D')

    def _loc_455(): pass

    label('loc_455')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 2, 0x202)),
            Expr.Return,
        ),
        'loc_519',
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

    Jump('loc_52D')

    def _loc_519(): pass

    label('loc_519')

    ChrClearFlags(0x000A, 0x0008)
    ChrClearFlags(0x0009, 0x0008)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x0009, 0x0080)

    def _loc_52D(): pass

    label('loc_52D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_544',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_0F_5122)

    def _loc_544(): pass

    label('loc_544')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_55B',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0xF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_0C_244A)

    def _loc_55B(): pass

    label('loc_55B')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000001, 'loc_577'),
        (0x00000002, 'loc_61A'),
        (0x00000003, 'loc_730'),
        (0x00000066, 'loc_746'),
        (0x00000067, 'loc_7B1'),
        (-1, 'loc_81C'),
    )

    def _loc_577(): pass

    label('loc_577')

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

    Event(0, func_04_98E)

    Jump('loc_81C')

    def _loc_61A(): pass

    label('loc_61A')

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
    Event(0, func_05_BEB)

    Jump('loc_81C')

    def _loc_730(): pass

    label('loc_730')

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x30),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_26(125)
    Event(0, func_0E_37CA)

    Jump('loc_81C')

    def _loc_746(): pass

    label('loc_746')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_750',
    )

    Jump('loc_7AE')

    def _loc_750(): pass

    label('loc_750')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_7AE',
    )

    MapClearFlags(0x00000001)
    CameraMove(6187, 0, 71060, 0)
    ChrSetPos(0x0101, 3012, 0, 67051, 0)
    ChrSetPos(0x0102, 3891, 0, 66840, 0)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetPos(0x0008, 3060, 200, 71360, 180)
    ChrSetChipByIndex(0x0008, 10)
    Event(0, func_08_19D8)

    def _loc_7AE(): pass

    label('loc_7AE')

    Jump('loc_81C')

    def _loc_7B1(): pass

    label('loc_7B1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_7BB',
    )

    Jump('loc_819')

    def _loc_7BB(): pass

    label('loc_7BB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_819',
    )

    MapClearFlags(0x00000001)
    CameraMove(6187, 0, 71060, 0)
    ChrSetPos(0x0101, 8324, 0, 71386, 270)
    ChrSetPos(0x0102, 8138, 0, 70528, 270)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetPos(0x0008, 3060, 200, 71360, 180)
    ChrSetChipByIndex(0x0008, 10)
    Event(0, func_08_19D8)

    def _loc_819(): pass

    label('loc_819')

    Jump('loc_81C')

    def _loc_81C(): pass

    label('loc_81C')

    Return()

# id: 0x0001 offset: 0x81D
@scena.Code('func_01_81D')
def func_01_81D():
    Return()

# id: 0x0002 offset: 0x81E
@scena.Code('func_02_81E')
def func_02_81E():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_833',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_81E')

    def _loc_833(): pass

    label('loc_833')

    Return()

# id: 0x0003 offset: 0x834
@scena.Code('func_03_834')
def func_03_834():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_940',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x0101,
        (
            '#000F对了，老爸。\n',
            '你今天不去游击士协会吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#000F这几天你还是抽空去一下吧。',
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
            '#007F（老爸真是一点也不可靠啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_98A')

    def _loc_940(): pass

    label('loc_940')

    ChrTalk(
        0x0008,
        (
            '#0160000217V#080F你们还不去协会那里？\n',
            '雪拉扎德不是在等着你们过去吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_98A(): pass

    label('loc_98A')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x98E
@scena.Code('func_04_98E')
def func_04_98E():
    OP_72(0x0000, 0x0020)
    OP_6F(0x0000, 5)
    EventBegin(0x00)
    MapClearFlags(0x00000001)
    ChrSetFlags(0x0101, 0x0008)
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
    Sleep(2000)

    ChrSetDirection(0x000A, 45, 0)
    ChrSetFlags(0x000A, 0x0020)
    ChrSetFlags(0x000A, 0x0002)
    OP_99(0x000A, 0x0F, 0x10, 1000)
    Sleep(1000)

    OP_61(0x0101)

    ChrTalk(
        0x000A,
        (
            '#377F……呜～……好刺眼呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0A5A')
    def lambda_0A5A():
        OP_99(0x00FE, 0x00, 0x07, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0A5A)

    Sleep(200)

    OP_6F(0x0000, 5)
    OP_70(0x0000, 20)
    Sleep(1500)

    @scena.Lambda('lambda_0A82')
    def lambda_0A82():
        OP_99(0x00FE, 0x08, 0x0E, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0A82)

    ChrTalk(
        0x000A,
        (
            '#375F呼哇啊啊啊啊啊啊～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '#440F嗯～～睡得真舒服～～！',
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
            '#370F……对了………\n',
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
    OP_1F(0x4B, 0x000000C8)
    Sleep(2000)

    OP_62(0x000A, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_99(0x000A, 0x13, 0x15, 1000)

    ChrTalk(
        0x000A,
        (
            '#371F啊哈，好像已经起来了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(1000)

    OP_99(0x000A, 0x16, 0x17, 1000)

    ChrTalk(
        0x000A,
        (
            '#376F好的……\n',
            '我也赶快起床吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    EventBegin(0x00)
    MapSetFlags(0x02000000)
    NewScene('ED6_DT01/T0300._SN', 1, 0, 0)
    IdleLoop()

    Return()

# id: 0x0005 offset: 0xBEB
@scena.Code('func_05_BEB')
def func_05_BEB():
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
    CreateThread(0x0101, 0x00, 0x00, func_06_18E5)
    CreateThread(0x0009, 0x00, 0x00, func_07_196E)
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
            '#010F#3P一大早你就吃这么多……',
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
            '#010F#3P嗯。\n',
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
            '#017F#3P这有什么好争的啊……',
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
            '#501F啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000175V……………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '考试……有这回事？',
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
            '#018F#3P难，难道说……\n',
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
            '#002F糟了～……\n',
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
            '#017F#3P唉，你啊……\n',
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
            '#017F#3P简直就是一个模子里刻出来的父女。',
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
            '#501F啊～对了老爸。',
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
            '不用太过勉强，\n',
            '做出来能吃进肚子就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#009F谁说我不会做的啊……\n',
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
            '#000F知道了。\n',
            '《利贝尔通讯》对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_16F0')
    def lambda_16F0():
        CameraMove(-5870, 0, 1160, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_16F0)

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
            '#001F太好了，谢谢老爸！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1804')
    def lambda_1804():
        CameraMove(-4460, 0, 230, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1804)

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
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x0008, 0xFF)
    ChrClearFlags(0x0101, 0x0004)
    ChrClearFlags(0x0009, 0x0004)
    ChrSetFlags(0x0008, 0x0010)
    SetScenaFlags(ScenaFlag(0x0040, 2, 0x202))

    @scena.Lambda('lambda_18BF')
    def lambda_18BF():
        OP_92(0x00FE, 0x0000, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_18BF)

    EventEnd(0x00)
    ChrClearFlags(0x0102, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x0009, 0x0008)
    MapClearFlags(0x02000000)

    Return()

# id: 0x0006 offset: 0x18E5
@scena.Code('func_06_18E5')
def func_06_18E5():
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

# id: 0x0007 offset: 0x196E
@scena.Code('func_07_196E')
def func_07_196E():
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

# id: 0x0008 offset: 0x19D8
@scena.Code('func_08_19D8')
def func_08_19D8():
    EventBegin(0x00)
    CreateThread(0x0101, 0x00, 0x00, func_09_22FA)
    CreateThread(0x0102, 0x00, 0x00, func_0A_2395)
    CreateThread(0x0008, 0x00, 0x00, func_0B_2413)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010001106V#000F我们回来了～老爸。',
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
            '#0010001107V#000F工作报告也已经完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0008, 1)
    Sleep(100)

    ChrTalk(
        0x0008,
        (
            '#0160001108V#080F#2P嗯，辛苦了。',
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
            '#0010001111V#501F知道了。',
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
            (TxtCtl.SetColor, 0x5),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '利贝尔通讯',
            (TxtCtl.SetColor, 0x5),
            '和',
            (TxtCtl.SetColor, 0x2),
            '致卡西乌斯的信',
            (TxtCtl.SetColor, 0x5),
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
            '#0160001114V#084F#2P唔，是信啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001115V#000F好了，\n',
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
            '#0010001116V#501F啊，对了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)
    ChrSetDirection(0x0101, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010001117V#008F……今天谢谢老爸你了。\n',
            '在危急的时候救了我们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160001118V#080F#2P呵呵，今天真是一反常态，这么乖啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001119V#080F你终于理解为父的伟大了，\n',
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
            '#0010001121V#009F不要得意忘形！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001122V#009F真是的，\n',
            '为什么这家里的男人都只会耍嘴皮子啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
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
            '#0160001123V#080F#2P看起来并没有我想象得那么沮丧嘛……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001124V#080F约修亚，是因为你吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0008, 400)

    ChrTalk(
        0x0102,
        (
            '#0020001125V#010F其实我也没做什么。\n',
            '只是稍微鼓励了她一下吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001126V#010F她本来就很坚强的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160001127V#085F#2P哼，还太嫩了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001128V#085F做游击士这种工作，\n',
            '感到迷茫肯定是经常会有的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001129V#085F要独当一面就得跨过这些门槛才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001130V#019F呵呵，您就是那么为女儿着想。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001131V惨了～……\n',
            '还得再重来一遍啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0101,
        (
            '#0010001132V突然挑战这个菜式，\n',
            '对我来说真的那么难吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001133V不对，做料理要靠气势！\n',
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
            '#0160001134V#083F#2P真是的……\n',
            '我这个沉不住气的女儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0008, 400)

    ChrTalk(
        0x0102,
        (
            '#0020001135V#010F我去帮她一下吧。',
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
            '#0160001137V#080F#2P呵呵……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001138V#085F……好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
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
            '#0160001139V#080F#2P嗯……\n',
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
    Sleep(2000)

    OP_21()

    ChrTalk(
        0x0008,
        (
            '#0160001142V#086F#2P……什么……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(500, 0, -1)
    OP_0D()
    Sleep(500)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0008, 0xFF)
    Call(0, 0x000C)

    Return()

# id: 0x0009 offset: 0x22FA
@scena.Code('func_09_22FA')
def func_09_22FA():
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
    ChrWalkTo(0x00FE, 3451, 0, 67219, 4000, 0x00)
    ChrWalkTo(0x00FE, 3043, 0, 64584, 4000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    ClearScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_A6(0x0000)
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_A6(0x0000)
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Return()

# id: 0x000A offset: 0x2395
@scena.Code('func_0A_2395')
def func_0A_2395():
    OP_A6(0x0001)
    Sleep(500)

    ChrWalkTo(0x00FE, 5703, 0, 69197, 3000, 0x00)
    ChrTurnDirection(0x00FE, 0x0008, 400)
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    OP_A6(0x0001)
    def _loc_23BE(): pass

    label('loc_23BE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_23D0',
    )

    ChrTurnDirection(0x00FE, 0x0101, 0)
    Yield()

    Jump('loc_23BE')

    def _loc_23D0(): pass

    label('loc_23D0')

    OP_A6(0x0001)
    ChrWalkTo(0x00FE, 3451, 0, 67219, 3000, 0x00)
    ChrWalkTo(0x00FE, 3043, 0, 64584, 3000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)
    ClearScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    OP_A6(0x0001)
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    OP_A6(0x0001)
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x000B offset: 0x2413
@scena.Code('func_0B_2413')
def func_0B_2413():
    OP_A6(0x0002)
    def _loc_2416(): pass

    label('loc_2416')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_2428',
    )

    ChrTurnDirection(0x00FE, 0x0101, 0)
    Yield()

    Jump('loc_2416')

    def _loc_2428(): pass

    label('loc_2428')

    OP_A6(0x0002)
    def _loc_242B(): pass

    label('loc_242B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_243D',
    )

    ChrTurnDirection(0x00FE, 0x0102, 0)
    Yield()

    Jump('loc_242B')

    def _loc_243D(): pass

    label('loc_243D')

    OP_A6(0x0002)
    ClearScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    OP_A6(0x0002)
    ClearScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Return()

# id: 0x000C offset: 0x244A
@scena.Code('func_0C_244A')
def func_0C_244A():
    EventBegin(0x00)
    CameraMove(-2500, 0, 1700, 0)
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
    ChrSetChipByIndex(0x0008, 10)
    ChrSetSubChip(0x000E, 0)
    ChrSetSubChip(0x000F, 0)
    ChrSetSubChip(0x0010, 0)
    ChrSetSubChip(0x0014, 7)
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
    FadeOut(0, 0, -1)
    Sleep(1000)

    FadeIn(2000, 0)
    CameraMove(-7500, 0, 1700, 3500)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0160001143V#084F#5P哦，真是不可思议啊……',
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
            '#0010001144V#508F怎么样，这可是艾丝蒂尔特制的\n',
            '香滑美味的鸡肉蛋包饭！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001145V请用心品味哦⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0009, 2)
    Sleep(300)

    ChrTalk(
        0x0102,
        (
            '#0020001146V#010F#6P嗯。\n',
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
            '#0010001148V#502F哼哼，这就是我的真正实力哦㈱',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001149V#006F啊～虽然发生了很多事，\n',
            '不过今天还真是很棒的一天啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001150V得到了游击士的资格，\n',
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
            '#0160001152V#080F#5P嗯……\n',
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
            '#0010001154V#509F好讨厌啊～\n',
            '直接说好吃不就行了嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160001155V#080F#5P嗯，\n',
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
            '#0010001157V#506F嘿嘿……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001158V#506F……………',
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
            '#0020001160V#014F#6P爸爸，难道您……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160001161V#080F#5P嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001162V突然接到了紧急任务。\n',
            '我又要暂时离家外出了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0101,
        (
            '#0010001163V#580F等、等一下！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001164V那……什么时候出发？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160001165V#080F#5P明天就走。',
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
            '#0020001167V#012F#6P是因为今天那封信吧……\n',
            '难道出了什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160001168V#085F没什么……单纯的调查而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001169V要到很多地方去看看，\n',
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
            '#0010001171V#005F#3S什么『就是这样』啊！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001172V#007F老爸真是的，\n',
            '每次都自作主张……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001173V#010F#6P没办法啊，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001174V接到任务就要立刻行动，\n',
            '这就是游击士的本职工作啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001175V#505F这我知道啊……\n',
            '可是洛连特支部的工作该怎么办呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001176V很多工作……应该也还没做完吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160001177V#080F#5P嗯，大概有五、六个吧。',
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
            '#0160001182V#080F#5P嗯，\n',
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
        (0x00000000, 'loc_2EED'),
        (0x00000001, 'loc_32B6'),
        (-1, 'loc_3654'),
    )

    def _loc_2EED(): pass

    label('loc_2EED')

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
            '#0020001187V#019F#6P嗯。\n',
            '而且我觉得这是难得的锻炼机会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160001188V#080F#5P就这么定了。',
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
            '#0160001192V#084F#5P啊啊，艾丝蒂尔……\n',
            '你这一番话太让我感动了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001193V#085F在天国的孩子她妈，你看到了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001194V我们的女儿终于长大了，\n',
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
            '#0010001196V#507F帮助父亲去完成工作是女儿应该做的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160001197V#086F#5P我今年才不过是４５而已！\n',
            '而且还是协会里现役的游击士！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001198V#017F#6P啊……这对父女又在对唱了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001199V#010F对了爸爸。\n',
            '你明天要坐哪艘定期船啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001200V#010F去王都的？\n',
            '还是去柏斯的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3654')

    def _loc_32B6(): pass

    label('loc_32B6')

    ChrTalk(
        0x0101,
        (
            '#0010001201V#007F虽然想试试看……\n',
            '不过一想到万一失败的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001202V#505F真的是我们这种新人\n',
            '也可以应付得来的工作吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160001203V#080F#5P相对来说都是比较简单的，\n',
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
            '#0010001205V#003F……………………',
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
            '#0020001207V#010F#6P我赞成。\n',
            '而且这是一次难得的锻炼机会。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001208V确实我们的能力都有所不足，\n',
            '不过我想一起行动的话应该没问题的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001209V两人齐心协力的话，\n',
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
            '#0010001212V#508F老爸！\n',
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
            '#0160001214V#080F#5P就这么定了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001215V明天出发前\n',
            '我会亲自向协会说明一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0009, 0)
    Sleep(300)

    ChrTalk(
        0x0102,
        (
            '#0020001216V#010F#6P对了爸爸。\n',
            '你明天要坐哪艘定期船啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001217V#010F去王都的？\n',
            '还是去柏斯的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3654')

    def _loc_3654(): pass

    label('loc_3654')

    ChrTalk(
        0x0008,
        (
            '#0160001218V#080F#5P去王都的。\n',
            '明早１０点出发。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001219V#006F这样啊……\n',
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

# id: 0x000D offset: 0x3720
@scena.Code('func_0D_3720')
def func_0D_3720():
    PlayBGM(84)
    ChrSetFlags(0x0101, 0x0004)
    ChrClearFlags(0x0101, 0x0080)
    ChrSetFlags(0x0101, 0x0008)
    ChrSetPos(0x0101, 67000, 300, 35500, 225)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x0008, 0x0080)
    OP_72(0x0000, 0x0020)
    OP_6F(0x0000, 5)
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

    OP_62(0x000A, 0xFFFFFE0C, 1200, 0x1C, 0x21, 0x000000FA, 0x00)
    Sleep(3000)

    MapSetFlags(0x02000000)
    NewScene('ED6_DT01/T0301._SN', 2, 0, 0)
    IdleLoop()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0008, 0xFF)

    Return()

# id: 0x000E offset: 0x37CA
@scena.Code('func_0E_37CA')
def func_0E_37CA():
    OP_77(0x5A, 0x5A, 0x7D, 0x00, 0x00000000)
    ChrSetFlags(0x0008, 0x0080)
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

    @scena.Lambda('lambda_3840')
    def lambda_3840():
        CameraSetDistance(2500, 7000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_3840)

    Sleep(2000)

    Fade(5000)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetSubChip(0x000E, 3)
    ChrSetSubChip(0x0010, 3)
    ChrSetSubChip(0x000F, 7)
    ChrSetSubChip(0x0014, 11)
    ChrSetPos(0x000E, -8360, 700, 300, 0)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x0010, -8260, 700, 1100, 0)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x000F, -9200, 750, 1000, 0)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x0014, -9000, 750, 400, 0)
    ChrClearFlags(0x0014, 0x0080)
    OP_77(0xFF, 0xC8, 0x96, 0x00, 0x00000000)
    OP_0D()
    WaitForThreadExit(0x0000, 0x0001)
    OP_66(0x0000)
    Sleep(1000)

    ChrTalk(
        0x000B,
        (
            '#0010000001V#295F嗯……',
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

    @scena.Lambda('lambda_3960')
    def lambda_3960():
        CameraMove(-7866, 1000, 5490, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_3960)

    ChrSetDirection(0x000B, 90, 0)
    ChrJumpToRelative(0x000B, 1000, 0, 0, 600, 6000)
    Sleep(500)

    ChrWalkTo(0x000B, -6615, 0, 2910, 3000, 0x00)
    ChrWalkTo(0x000B, -7866, 0, 5490, 3000, 0x00)
    Sleep(1500)

    ChrTalk(
        0x000B,
        (
            '#0010000004V#295F#5P雪拉姐也还在\n',
            '周游王国的修行旅途中……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000005V唉～真无聊。\n',
            '吃饭前还是再练习一下棒术吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(6, 0x00, 0x64)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, -1550, 0, -3450, 0)
    ChrSetChipByIndex(0x0008, 14)
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

    ChrSetDirection(0x000B, 180, 800)

    ChrTalk(
        0x000B,
        (
            '#0010000007V#291F#5P爸爸！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3AD4')
    def lambda_3AD4():
        CameraMove(-1110, 0, -1690, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_3AD4)

    ChrWalkTo(0x000B, -2190, 0, -1390, 5000, 0x00)
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
            '#0010000010V#290F#1P哼哼，当然有啦☆',
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
            '#0010000015V#291F#1P啊，真的！？',
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
            '#0010000019V#290F#1P我当然喜欢漂亮的衣服呀，\n',
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

    @scena.Lambda('lambda_3E81')
    def lambda_3E81():
        CameraMove(-400, 0, -2200, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_3E81)

    Fade(1500)
    ChrSetDirection(0x0008, 315, 0)
    OP_0D()
    Sleep(500)

    NpcTalk(
        0x0008,
        '男孩',
        (
            '#0160000025V#305F#5P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0010000026V#293F#1P…………啊？',
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
            '#0010000030V#293F#1P什、什、什……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x000B,
        (
            '#0010000031V#294F#3S#1P什么呀，这男孩！？',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
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
            '#0010000033V#292F#1P吵醒……\n',
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
            '#0010000038V#291F#1P嗯，知道了～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    OP_66(0x0001)
    ChrSetFlags(0x000B, 0x0040)
    ChrSetPos(0x000B, 8900, 0, 68600, 180)
    ChrSetPos(0x0008, 8550, 0, 69460, 180)
    ChrSetPos(0x000C, 8550, 500, 67500, 270)
    ChrSetChipByIndex(0x0008, 0)
    ChrSetChipByIndex(0x000C, 15)
    ChrSetSubChip(0x000C, 0)
    ChrClearFlags(0x000C, 0x0080)
    OP_72(0x0005, 0x0004)
    OP_72(0x0005, 0x0020)
    OP_6F(0x0005, 0)
    CameraMove(8550, 0, 69460, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(44000, 0)
    OP_6E(280, 0)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x000B,
        (
            '#0010000039V#290F#2P睡得真香啊……',
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
            '#0010000044V#290F#2P嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000B, 0, 400)

    ChrTalk(
        0x000B,
        (
            '#0010000045V#292F#2P先不说这个……\n',
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
            '#0010000047V#292F#2P这小男孩到底是谁？',
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
            '#0010000053V#291F#2P嗯，没错！',
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
            '#0010000057V#290F#2P工作？是指游击士的？',
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
            '#0010000060V#293F#2P啊？',
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
    ChrSetDirection(0x000B, 180, 400)

    @scena.Lambda('lambda_45E7')
    def lambda_45E7():
        CameraMove(8900, 0, 68600, 2000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_45E7)

    Sleep(2000)

    OP_99(0x000C, 0x00, 0x01, 1000)
    Sleep(500)

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
            '#0020000064V#307F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000065V#307F…………这里是…………',
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
            '#0020000068V#301F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000069V#301F……你这是什么意思？',
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
            '#0020000071V#307F简直无法理解……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000072V#307F为什么这样做……\n',
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
    OP_99(0x000C, 0x01, 0x02, 1500)
    Sleep(400)

    @scena.Lambda('lambda_4832')
    def lambda_4832():
        OP_7C(0, 200, 3000, 100)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_4832)

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
    ChrJumpToRelative(0x000B, -200, 800, -1200, 1200, 6000)
    OP_7C(0, 100, 3000, 100)
    OP_A1(0x0016, 0x0005)

    @scena.Lambda('lambda_48FC')
    def lambda_48FC():
        OP_99(0x000C, 0x00, 0x02, 1000)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_48FC)

    @scena.Lambda('lambda_490C')
    def lambda_490C():
        ChrJumpToRelative(0x000C, 0, 0, 0, 200, 4000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_490C)

    @scena.Lambda('lambda_492A')
    def lambda_492A():
        ChrJumpToRelative(0x0016, 0, 0, 0, 100, 2000)

        ExitThread()

    DispatchAsync(0x0016, 0x0001, lambda_492A)

    PlaySE(125, 0x00, 0x64)
    ChrJumpToRelative(0x000B, 200, -800, 1200, 200, 6000)
    Sleep(400)

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
            '#0020000086V#307F好像提起过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000087V#302F现、现在是说这种事情的时候吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrJumpToRelative(0x000B, -200, 800, -1200, 1200, 6000)
    OP_7C(0, 100, 3000, 100)
    PlaySE(125, 0x00, 0x64)

    @scena.Lambda('lambda_4B51')
    def lambda_4B51():
        OP_99(0x000C, 0x00, 0x02, 1000)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_4B51)

    @scena.Lambda('lambda_4B61')
    def lambda_4B61():
        ChrJumpToRelative(0x000C, 0, 0, 0, 200, 4000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_4B61)

    @scena.Lambda('lambda_4B7F')
    def lambda_4B7F():
        ChrJumpToRelative(0x0016, 0, 0, 0, 100, 2000)

        ExitThread()

    DispatchAsync(0x0016, 0x0001, lambda_4B7F)

    ChrJumpToRelative(0x000B, 200, -800, 1200, 200, 6000)
    ChrJumpToRelative(0x000B, -200, 800, -1200, 1500, 6000)
    OP_7C(0, 200, 3000, 100)
    PlaySE(125, 0x00, 0x64)

    @scena.Lambda('lambda_4BE1')
    def lambda_4BE1():
        OP_99(0x000C, 0x00, 0x02, 1000)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_4BE1)

    @scena.Lambda('lambda_4BF1')
    def lambda_4BF1():
        ChrJumpToRelative(0x000C, 0, 0, 0, 250, 4000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_4BF1)

    @scena.Lambda('lambda_4C0F')
    def lambda_4C0F():
        ChrJumpToRelative(0x0016, 0, 0, 0, 100, 1500)

        ExitThread()

    DispatchAsync(0x0016, 0x0001, lambda_4C0F)

    ChrJumpToRelative(0x000B, 200, -800, 1200, 500, 6000)
    Sleep(400)

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
            '#0010000094V#291F#3S你·刚·才·说·什·么？',
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
            '#0160000096V#081F呵呵，\n',
            '在这个家里千万不要和艾丝蒂尔作对哦。',
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
    OP_99(0x000C, 0x02, 0x01, 1500)
    Sleep(500)

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
            '#0020000108V#307F#40W我……知道了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000109V#307F#40W我……#400W　\n',
            '#80W我的名字是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 3, 0x203)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_50EE',
    )

    Fade(3000)
    FormationDelMember(0x01, 0xFF)
    FormationDelMember(0x02, 0xFF)
    OP_77(0x00, 0x00, 0x00, 0x00, 0x00000BB8)
    CameraSetDistance(3100, 3000)
    OP_20(0x000005DC)
    OP_21()
    CameraMove(-9880, 0, -44600, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    PlayMovie(0x00, 'ed6_op.avi')
    def _loc_50C0(): pass

    label('loc_50C0')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_50EE',
    )

    Sleep(10)

    If(
        (
            (Expr.PushValueByIndex, 0x2D),
            Expr.Return,
        ),
        'loc_50EB',
    )

    FadeOut(2000, 0, -1)
    OP_0D()
    PlayMovie(0x01, '')
    NewScene('ED6_DT01/T0300._SN', 3, 0, 0)
    IdleLoop()

    def _loc_50EB(): pass

    label('loc_50EB')

    Jump('loc_50C0')

    def _loc_50EE(): pass

    label('loc_50EE')

    Fade(3000)
    OP_77(0x00, 0x00, 0x00, 0x00, 0x00000BB8)
    CameraSetDistance(3100, 3000)
    FadeOut(0, 0, -1)
    Sleep(2000)

    OP_77(0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    Call(1, 0x000F)

    Return()

# id: 0x000F offset: 0x5122
@scena.Code('func_0F_5122')
def func_0F_5122():
    EventBegin(0x00)
    FormationAddMember(0x00, 0xFF)
    FormationAddMember(0x01, 0xFF)
    FormationAddMember(0x02, 0xFF)
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

    PlaySE(113, 0x00, 0x64)
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
    ChrSetFlags(0x0103, 0x0002)
    ChrSetChipByIndex(0x0103, 16)
    ChrSetSubChip(0x0103, 11)
    ChrSetPos(0x0102, 3066, 0, -2366, 0)
    ChrSetPos(0x0101, 3066, 0, -2366, 0)
    ChrSetPos(0x0103, -9810, 250, 2050, 200)
    ChrSetSubChip(0x0014, 2)
    ChrSetSubChip(0x000E, 8)
    ChrSetSubChip(0x000F, 8)
    ChrSetSubChip(0x0010, 8)
    ChrSetPos(0x0014, -8500, 750, 1000, 0)
    ChrClearFlags(0x0014, 0x0080)
    ChrSetPos(0x000E, -8060, 750, 300, 0)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000F, -9320, 750, 300, 0)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x0010, -9520, 750, 1100, 0)
    ChrClearFlags(0x0010, 0x0080)
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
    OP_99(0x0103, 0x0B, 0x09, 1000)
    ChrClearFlags(0x0103, 0x0002)
    ChrSetChipByIndex(0x0103, 11)
    ChrSetSubChip(0x0103, 0)
    OP_62(0x0103, 0x00000000, 1700, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(1000)

    ChrSetSubChip(0x0103, 1)

    @scena.Lambda('lambda_5530')
    def lambda_5530():
        CameraMove(-7800, 1150, 1700, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_5530)

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
            '#0020020014V#013F#2P刚才我叫她下来吃饭……\n',
            '不过她好像没什么食欲的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020015V#522F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020016V就算是平时多么活泼的女孩，\n',
            '遇到这种事情也承受不了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020017V#013F#2P……这也是没办法的事啊。',
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

    @scena.Lambda('lambda_56DA')
    def lambda_56DA():
        CameraMove(-8020, 0, 1120, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_56DA)

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
            '#0020020021V#012F#4P雪拉姐姐你是怎么想的？',
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
            '#0030020023V#522F#1P……说实话，我也不能断定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020024V老师是一流的游击士。\n',
            '对于任何突发的危机\n',
            '都有着十分果断的应付能力。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020025V不管是意外还是案件，\n',
            '只要有老师在场的话，\n',
            '都应该能够立刻解决掉的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020026V#026F可是实际情况却是，\n',
            '定期船和老师都失踪了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020027V#013F#4P不可能发生的事情却出现了……\n',
            '你是这个意思吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020028V#020F#1P呵呵，不要这么沮丧嘛。',
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

    @scena.Lambda('lambda_5A4D')
    def lambda_5A4D():
        CameraMove(-5000, 0, 1000, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_5A4D)

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
            '#0030020034V#023F#5P艾丝蒂尔……\n',
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

    @scena.Lambda('lambda_5B3B')
    def lambda_5B3B():
        CameraMove(-8590, 200, 780, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_5B3B)

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
            '#0010020037V#001F#2P我不客气啦～！',
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
            '#0010020038V#501F#2P哎，你们怎么不吃啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020039V奶汁烤菜很好吃呢。\n',
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
            '#0020020041V#014F#6P过、过奖了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020042V#000F#2P哎呀哎呀。\n',
            '雪拉姐也别客气了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020043V#004F啊，老爸藏起来的\n',
            '白兰地你要不要喝点？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020044V#505F我记得好像是\n',
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
            '#0030020045V#024F#5P圣、圣蔷薇？\n',
            '而且还是２０年陈酿！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0102, 0)

    ChrTalk(
        0x0102,
        (
            '#0020020046V#017F#6P我说啊，雪拉姐姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020047V#023F#5P…………啊。\n',
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
            '#0010020050V#501F#2P嗯？\n',
            '啊啊，我正在找替换用的睡衣呢。',
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
            '#0020020052V#018F#6P睡、睡衣？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020053V#006F#2P而且还有套装旅行用具。',
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
            '#0020020055V#014F#6P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020056V#023F#5P你难道要……',
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
            '#0010020058V#006F#2P那当然啦。',
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
            '#0020020061V#011F#6P哈哈……\n',
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
            '#0010020063V#007F#2P什么呀～真没礼貌。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020064V#006F反正约修亚你\n',
            '一定会和我一起去吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020065V#010F#6P那是当然的了。',
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
            '#0010020068V#505F#2P步行到柏斯……\n',
            '要花多长时间呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020069V#026F#5P按照游击士的脚力，\n',
            '快的话半天左右就能到了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020070V#020F不过也真是的……\n',
            '这些话你应该早点说嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020071V我也正打算这么做呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020072V#004F#2P哎……\n',
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
            '#0030020074V#020F#5P我可是卡西乌斯老师的徒弟哦。',
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
            '#0010020077V#501F#2P雪拉姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0102, 0)

    ChrTalk(
        0x0102,
        (
            '#0020020078V#010F#6P雪拉姐姐，谢谢你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020079V#027F#5P不用感谢我啦。',
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
            '#0010020081V#509F#2P呜～真不甘心……\n',
            '不过这样说好像也没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020082V#007F算了，反正有雪拉姐一起，\n',
            '我们也更加放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020083V#019F#6P那就请多关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020084V#021F#5P呵呵，彼此彼此。',
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
    OP_20(0x000009C4)
    FadeOut(2000, 0, -1)
    OP_0D()
    OP_21()
    Sleep(1000)

    OP_AD('ED6_DT04/C_VIS041._CH', 0x0000, 0x0000, 0x00000064)
    Sleep(4000)

    OP_56(0x02)
    OP_AE(0x000000C8)
    Sleep(2000)

    MapClearFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T0121._SN', 103, 0, 0)
    IdleLoop()

    Return()

# id: 0x0010 offset: 0x664C
@scena.Code('func_10_664C')
def func_10_664C():
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

# id: 0x0011 offset: 0x68E9
@scena.Code('func_11_68E9')
def func_11_68E9():
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
        'loc_697D',
    )

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

    def _loc_697D(): pass

    label('loc_697D')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6997',
    )

    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

    def _loc_6997(): pass

    label('loc_6997')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

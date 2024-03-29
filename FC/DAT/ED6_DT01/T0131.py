import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T0131_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0131   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0131.x'
    header.mapIndex       = 7
    header.bgm            = 10
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
            dword_00        = 0x0000A410,
            dword_04        = 0x00000000,
            dword_08        = 0x00011170,
            word_0C         = 0x010E,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 8000,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2600,
            dword_2C        = 262,
            word_30         = 315,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 7,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
        ScenaEntryPoint(
            dword_00        = 0x00009C40,
            dword_04        = 0x00000000,
            dword_08        = 0x0000FA00,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 8000,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2600,
            dword_2C        = 262,
            word_30         = 315,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 7,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
        ScenaEntryPoint(
            dword_00        = 0x0000AFC8,
            dword_04        = 0x00000000,
            dword_08        = 0x00011170,
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
            word_30         = 315,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 7,
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
        ('ED6_DT07/CH01280._CH', 'ED6_DT07/CH01280P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH02490._CH', 'ED6_DT07/CH02490P._CP'),
        ('ED6_DT07/CH01270._CH', 'ED6_DT07/CH01270P._CP'),
        ('ED6_DT07/CH01503._CH', 'ED6_DT07/CH01503P._CP'),
        ('ED6_DT07/CH01233._CH', 'ED6_DT07/CH01233P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01003._CH', 'ED6_DT07/CH01003P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01250._CH', 'ED6_DT07/CH01250P._CP'),
        ('ED6_DT07/CH01760._CH', 'ED6_DT07/CH01760P._CP'),
        ('ED6_DT07/CH02060._CH', 'ED6_DT07/CH02060P._CP'),
        ('ED6_DT06/CH20015._CH', 'ED6_DT06/CH20015P._CP'),
    ]

# id: 0x10001 offset: 0x19A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '德瑟鲁',
            x                   = 36450,
            z                   = 0,
            y                   = 126300,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '托露塔',
            x                   = 82238,
            z                   = 0,
            y                   = 79895,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '伊莉莎',
            x                   = 40200,
            z                   = 1500,
            y                   = 78700,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '福克纳',
            x                   = 34500,
            z                   = 0,
            y                   = 75200,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '提恩特',
            x                   = 39320,
            z                   = 220,
            y                   = 70940,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0155,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '米拉诺',
            x                   = 39570,
            z                   = 0,
            y                   = 66410,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '西蒙',
            x                   = 41450,
            z                   = 0,
            y                   = 67420,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0111,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '拉欧老人',
            x                   = 39480,
            z                   = 1650,
            y                   = 76950,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0195,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '奈尔',
            x                   = 36600,
            z                   = 0,
            y                   = 75170,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '潘杜爷爷',
            x                   = 36500,
            z                   = 0,
            y                   = 72960,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '利吉',
            x                   = 36500,
            z                   = 0,
            y                   = 72960,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '目标用摄像机',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0180,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x31A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x31A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x31A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 35580,
            triggerZ            = 0,
            triggerY            = 74990,
            triggerRange        = 800,
            actorX              = 34500,
            actorZ              = 1500,
            actorY              = 75200,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x33E
@scena.Code('Init')
def Init():
    ChrSetFlags(0x000D, 0x0010)
    ChrSetFlags(0x000E, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_357',
    )

    ChrClearFlags(0x000F, 0x0080)

    Jump('loc_36D')

    def _loc_357(): pass

    label('loc_357')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_361',
    )

    Jump('loc_36D')

    def _loc_361(): pass

    label('loc_361')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_36D',
    )

    ChrClearFlags(0x000F, 0x0080)

    def _loc_36D(): pass

    label('loc_36D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 1, 0x251)),
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 2, 0x252)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_383',
    )

    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0010, 0x0008)

    def _loc_383(): pass

    label('loc_383')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 6, 0x24E)),
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 1, 0x251)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3AA',
    )

    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0010, 0x0008)
    ChrSetPos(0x0010, 37320, 0, 75500, 0)

    def _loc_3AA(): pass

    label('loc_3AA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3C0',
    )

    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000C, 0x0008)

    def _loc_3C0(): pass

    label('loc_3C0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_3DB',
    )

    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000D, 0x0008)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000E, 0x0008)

    def _loc_3DB(): pass

    label('loc_3DB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_3EF',
    )

    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0011, 0x0008)

    Jump('loc_405')

    def _loc_3EF(): pass

    label('loc_3EF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_405',
    )

    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0011, 0x0008)

    def _loc_405(): pass

    label('loc_405')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_41E',
    )

    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0012, 0x0008)

    Jump('loc_434')

    def _loc_41E(): pass

    label('loc_41E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_434',
    )

    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0012, 0x0008)

    def _loc_434(): pass

    label('loc_434')

    Return()

# id: 0x0001 offset: 0x435
@scena.Code('func_01_435')
def func_01_435():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_44D',
    )

    OP_B1('t0131_y')

    Jump('loc_456')

    def _loc_44D(): pass

    label('loc_44D')

    OP_B1('t0131_n')

    def _loc_456(): pass

    label('loc_456')

    Return()

# id: 0x0002 offset: 0x457
@scena.Code('func_02_457')
def func_02_457():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_46C',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_457')

    def _loc_46C(): pass

    label('loc_46C')

    Return()

# id: 0x0003 offset: 0x46D
@scena.Code('func_03_46D')
def func_03_46D():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_61C',
    )

    Sleep(3000)

    ChrWalkTo(0x00FE, 43100, 1500, 78900, 2500, 0x00)
    ChrTurnDirectionByPos(0x00FE, 100000, 78900, 500)
    Sleep(3000)

    ChrWalkTo(0x00FE, 42935, 1500, 77000, 2000, 0x00)
    ChrWalkTo(0x00FE, 42907, 1500, 76200, 2000, 0x00)
    ChrWalkTo(0x00FE, 42901, 0, 74390, 1000, 0x00)
    ChrWalkTo(0x00FE, 41200, 0, 72000, 2500, 0x00)
    ChrTurnDirectionByPos(0x00FE, 0, 72000, 500)
    Sleep(3000)

    ChrWalkTo(0x00FE, 42800, 0, 65500, 2000, 0x00)
    ChrTurnDirectionByPos(0x00FE, 100000, 65500, 500)
    Sleep(3000)

    ChrWalkTo(0x00FE, 34900, 0, 63860, 2500, 0x00)
    ChrTurnDirectionByPos(0x00FE, 0, 63800, 500)
    Sleep(3000)

    ChrTurnDirectionByPos(0x00FE, 100000, 63800, 500)
    ChrWalkTo(0x00FE, 37100, 0, 64500, 2000, 0x00)
    ChrWalkTo(0x00FE, 37700, 0, 67200, 2500, 0x00)
    ChrTurnDirectionByPos(0x00FE, 100000, 67200, 500)
    Sleep(3000)

    ChrWalkTo(0x00FE, 33200, 0, 69000, 2000, 0x00)
    ChrWalkTo(0x00FE, 33200, 0, 74200, 2500, 0x00)
    ChrTurnDirectionByPos(0x00FE, 0, 74200, 500)
    Sleep(3000)

    ChrWalkTo(0x00FE, 35120, 0, 78350, 2000, 0x00)
    ChrWalkTo(0x00FE, 36400, 0, 78810, 2000, 0x00)
    ChrWalkTo(0x00FE, 40200, 1500, 78700, 2500, 0x00)
    ChrTurnDirectionByPos(0x00FE, 40200, 0, 500)

    Jump('func_03_46D')

    def _loc_61C(): pass

    label('loc_61C')

    Return()

# id: 0x0004 offset: 0x61D
@scena.Code('func_04_61D')
def func_04_61D():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_717',
    )

    Sleep(3000)

    ChrWalkTo(0x00FE, 36450, 0, 123500, 2000, 0x00)
    ChrTurnDirectionByPos(0x00FE, 0, 123500, 500)
    Sleep(3000)

    ChrWalkTo(0x00FE, 37640, 0, 121500, 2000, 0x00)
    ChrTurnDirectionByPos(0x00FE, 37640, 0, 500)
    Sleep(3000)

    ChrTurnDirectionByPos(0x00FE, 0, 121500, 500)
    ChrWalkTo(0x00FE, 36660, 0, 123500, 2500, 0x00)
    ChrWalkTo(0x00FE, 36660, 0, 126300, 2500, 0x00)
    ChrWalkTo(0x00FE, 38000, 0, 127300, 2500, 0x00)
    ChrWalkTo(0x00FE, 39600, 0, 127700, 2500, 0x00)
    ChrTurnDirectionByPos(0x00FE, 39600, 200000, 500)
    Sleep(3000)

    ChrTurnDirectionByPos(0x00FE, 0, 127700, 500)
    ChrWalkTo(0x00FE, 36450, 0, 126300, 2000, 0x00)
    ChrTurnDirectionByPos(0x00FE, 0, 126300, 500)

    Jump('func_04_61D')

    def _loc_717(): pass

    label('loc_717')

    Return()

# id: 0x0005 offset: 0x718
@scena.Code('func_05_718')
def func_05_718():
    TalkBegin(0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 1, 0x251)),
            Expr.Return,
        ),
        'loc_165A',
    )

    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, 36520, 0, 73960, 0)
    ChrSetPos(0x0102, 37840, 0, 73590, 315)
    ChrSetDirection(0x0010, 180, 0)
    MapClearFlags(0x00000001)

    ExecExpressionWithValue(
        0x0013,
        0x01,
        (
            (Expr.GetChrWork, 0x10, 0x1),
            (Expr.GetChrWork, 0x101, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0013,
        0x02,
        (
            (Expr.GetChrWork, 0x10, 0x2),
            (Expr.GetChrWork, 0x101, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0013,
        0x03,
        (
            (Expr.GetChrWork, 0x10, 0x3),
            (Expr.GetChrWork, 0x101, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x0013, 1000)
    SetScenaFlags(ScenaFlag(0x004A, 2, 0x252))
    OP_28(0x0019, 0x01, 0x0008)
    OP_28(0x0019, 0x01, 0x0010)
    OP_28(0x0019, 0x01, 0x0020)
    OP_28(0x0008, 0x04, 0x40)
    OP_28(0x000B, 0x04, 0x40)

    ExecExpressionWithVar(
        0x17,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x0010, 0x0040)

    NpcTalk(
        0x0010,
        '满脸胡渣的男人',
        (
            '#0270010456V#142F喂，你们是什么人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010457V#000F你是不是……\n',
            '《利贝尔通讯》的记者啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0010,
        '满脸胡渣的男人',
        (
            '#0270010458V#142F没错……\n',
            '你怎么会知道？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010459V#142F虽然我喜欢采访别人，\n',
            '不过可不喜欢别人对我刨根问底。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010460V#142F到底有什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010461V#010F#4P我们是游击士协会派来的。\n',
            '请问您是不是委托了护卫的工作？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0010,
        '满脸胡渣的男人',
        (
            '#0270010462V#147F哦哦，终于来了啊！\n',
            '我都等得不耐烦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010463V#141F那么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0010, 45, 400)
    ChrSetDirection(0x0010, 180, 400)
    ChrTurnDirection(0x0010, 0x0101, 400)

    NpcTalk(
        0x0010,
        '满脸胡渣的男人',
        (
            '#0270010464V#143F卡西乌斯·布莱特在哪里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010465V#007F那个嘛……\n',
            '他本人要负责其他的工作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010466V#007F而且已经离开了洛连特……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0010,
        '满脸胡渣的男人',
        (
            '#0270010467V#142F你、你说什么！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010468V#142F好不容易来这一趟，\n',
            '还以为可以顺便采访这位传说中的游击士……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010469V#145F可恶……\n',
            '这下子我的专访计划全都落空了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010470V#001F虽然不知道是怎么回事……\n',
            '不过，也不用那么悲观嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010471V#001F因为有我们在，\n',
            '一定会好好替他完成任务的⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0010,
        '满脸胡渣的男人',
        (
            '#0270010472V#145F嘁，没办法……\n',
            '这次也只能这么办了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010473V#145F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010474V#142F……刚才你说什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010010475V#501F『也不用那么悲观嘛』？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0010,
        '满脸胡渣的男人',
        (
            '#0270010476V#144F不是那句！\n',
            '是『替他完成任务』！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010477V#144F那是怎么回事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010478V#000F你还不明白吗？\n',
            '我们是代替他工作的游击士啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010479V#000F看看，这封是介绍信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '游击士协会的介绍信',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(0x0324, 1)

    NpcTalk(
        0x0010,
        '满脸胡渣的男人',
        (
            '#0270010480V#142F喂喂，玩笑开过头了吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010481V#142F像你们这样的小鬼，\n',
            '也敢说自己是游击士？',
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
            '#0010010482V#009F小、小鬼？\n',
            '你怎么能对妙龄少女说这种话呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0010,
        '满脸胡渣的男人',
        (
            '#0270010483V#141F什～么少女呀。\n',
            '一身毫无品味的打扮。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010484V#141F不甘心的话，\n',
            '就换回裙子做一个像样的女孩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010485V#005F这是棒术用的服装！\n',
            '没看到我穿的就是裙子吗！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010486V#005F真是的，没礼貌的大叔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0010, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    NpcTalk(
        0x0010,
        '满脸胡渣的男人',
        (
            '#0270010487V#144F我，我才二十几岁！\n',
            '别叫我大叔！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010488V#017F#4P……总之，记者先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020010489V#017F我们确实是游击士，\n',
            '是协会派来协助你取材的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020010490V#010F换成其他人也不是不行。\n',
            '但是最近人手紧缺，不知要等到何时。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0102, 400)

    NpcTalk(
        0x0010,
        '满脸胡渣的男人',
        (
            '#0270010491V#145F唔，那也是……\n',
            '截稿时间也不能再拖了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010492V#145F没办法，实在是走投无路了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010493V#141F就当我拜托你们了，这样总可以了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010494V#009F自以为是的大叔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010495V#010F#4P好了好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020010496V#010F……我叫约修亚。\n',
            '这个女孩叫艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020010497V#010F能告诉我们您的名字吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0010,
        '满脸胡渣的男人',
        (
            '#0270010498V#141F奈尔·班兹。\n',
            '《利贝尔通讯》最能干的记者。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010499V#141F虽说不会相处很久，不过还是多关照啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010500V#009F哼哼，这句话是我说才对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010501V#007F对了……你要我们带你去哪里呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010502V#007F我记得是要去危险的地方取材，\n',
            '需要有身手不凡的向导对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0270010503V#140F是被称做『翡翠之塔』的遗迹。\n',
            '你们至少也应该听过这名字吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010504V#006F什～么呀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010505V#006F何止听说过，\n',
            '之前还进去过执行任务呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0270010506V#141F哦，那不是正好嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010507V#141F具体来说，\n',
            '只要护送我们到塔顶就可以了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010508V#141F我们要拍一些登在杂志上的照片。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010509V#000F嗯～听起来好像很有趣嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010510V#010F#4P你说『我们』……\n',
            '难道还有其他人一起去吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0270010511V#140F还有和我搭档的摄影师。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010512V#140F因为照相机出了点问题，\n',
            '刚才去了工房那里……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010513V#142F真是的，怎么这么慢啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010514V#000F要是你着急的话，\n',
            '我们就去工房接你的搭档吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010515V#000F反正等一下也要一起出去的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0270010516V#140F这样说也对……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270010517V#140F好，去工房叫上那家伙，\n',
            '然后直接出城去塔那边吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_92(0x0010, 0x0000, 0, 3000, 0x00)
    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x0010, 0x0008)
    OP_92(0x0001, 0x0000, 0, 3000, 0x00)
    FormationAddMember(0x0E, 0xFF)
    EventEnd(0x00)
    MapSetFlags(0x00000001)

    Jump('loc_1696')

    def _loc_165A(): pass

    label('loc_165A')

    NpcTalk(
        0x0010,
        '满脸胡渣的男人',
        (
            '#0270010455V#145F啊～肚子饿死了，肚子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1696(): pass

    label('loc_1696')

    TalkEnd(0x0010)

    Return()

# id: 0x0006 offset: 0x169A
@scena.Code('func_06_169A')
def func_06_169A():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_17A6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_173B',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '新的菜式\n',
            '受到了广泛的好评。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '特别是伊莉莎想出的\n',
            '那个菜式最受大家欢迎啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不如别叫她当服务生了，\n',
            '来帮我打理厨房可能更合适。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17A3')

    def _loc_173B(): pass

    label('loc_173B')

    ChrTalk(
        0x00FE,
        (
            '特别是伊莉莎想出的\n',
            '那个菜式最受大家欢迎啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不如别叫她当服务生了，\n',
            '来帮我打理厨房可能更合适。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17A3(): pass

    label('loc_17A3')

    Jump('loc_1EAE')

    def _loc_17A6(): pass

    label('loc_17A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            Expr.Return,
        ),
        'loc_1893',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_184E',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    ChrTurnDirection(0x00FE, 0x0103, 0)

    ChrTalk(
        0x00FE,
        (
            '哟，雪拉扎德！\n',
            '你又来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我进了几瓶\n',
            '你最喜欢喝的酒哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一定要来喝啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F哎呀，真开心。\n',
            '等工作告一段落了我就过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1890')

    def _loc_184E(): pass

    label('loc_184E')

    ChrTurnDirection(0x00FE, 0x0103, 0)

    ChrTalk(
        0x00FE,
        (
            '我进了雪拉扎德你\n',
            '最喜欢喝的酒哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一定要来喝啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1890(): pass

    label('loc_1890')

    Jump('loc_1EAE')

    def _loc_1893(): pass

    label('loc_1893')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_1972',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_192D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '差不多该考虑\n',
            '换换新的菜式了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以往遇到这种情况，\n',
            '都是由全体员工一起\n',
            '出主意定制新菜单的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……让伊莉莎也帮忙想想吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_196F')

    def _loc_192D(): pass

    label('loc_192D')

    ChrTalk(
        0x00FE,
        (
            '以往遇到这种情况，\n',
            '都是由全体员工一起\n',
            '出主意定制新菜单的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_196F(): pass

    label('loc_196F')

    Jump('loc_1EAE')

    def _loc_1972(): pass

    label('loc_1972')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_1AEF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A8C',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '说起来，艾丝蒂尔会做饭吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F啊哈哈，\n',
            '我家做饭是轮班制的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#007F……所以嘛，好歹算是会一点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是水平不行的话\n',
            '就从简单的东西做起好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要备齐了材料和炊具，\n',
            '剩下的就只要放手一试就行了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '学会做饭的话\n',
            '真的百利而无一害啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AEC')

    def _loc_1A8C(): pass

    label('loc_1A8C')

    ChrTalk(
        0x00FE,
        (
            '只要备齐了材料和炊具，\n',
            '剩下的就只要放手一试就行了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '学会做饭的话\n',
            '真的百利而无一害啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AEC(): pass

    label('loc_1AEC')

    Jump('loc_1EAE')

    def _loc_1AEF(): pass

    label('loc_1AEF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_1BDD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1B99',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '刚才帕赛尔农场\n',
            '发来联络通知我们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说是再过一小阵\n',
            '就能恢复蔬菜供应了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在虽然从其它地方进着货，\n',
            '但毕竟还是帕赛尔农场的东西最好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BDA')

    def _loc_1B99(): pass

    label('loc_1B99')

    ChrTalk(
        0x00FE,
        (
            '现在虽然从其它地方进着货，\n',
            '毕竟还是帕赛尔农场的蔬菜最好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1BDA(): pass

    label('loc_1BDA')

    Jump('loc_1EAE')

    def _loc_1BDD(): pass

    label('loc_1BDD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_1C28',
    )

    ChrTalk(
        0x00FE,
        (
            '帕赛尔农场\n',
            '没有按预定送来蔬菜呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是不是出什么事了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EAE')

    def _loc_1C28(): pass

    label('loc_1C28')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_1C92',
    )

    ChrTalk(
        0x0008,
        (
            '呼，忙死了。\n',
            '现在正是最忙的时候啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '储备的食材已经用完了，\n',
            '明天还得去采购一些才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EAE')

    def _loc_1C92(): pass

    label('loc_1C92')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_1D9B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D48',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '在我看来，\n',
            '料理有两大乐趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '那就是吃的乐趣\n',
            '以及做菜的乐趣！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '呵呵，\n',
            '我做每一款料理时\n',
            '都燃烧着无穷的热情啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '当然，\n',
            '吃美味的料理时也很开心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D98')

    def _loc_1D48(): pass

    label('loc_1D48')

    ChrTalk(
        0x0008,
        (
            '吃是乐趣做也是乐趣……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '呵呵，\n',
            '我做每一款料理时\n',
            '都燃烧着无穷的热情啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D98(): pass

    label('loc_1D98')

    Jump('loc_1EAE')

    def _loc_1D9B(): pass

    label('loc_1D9B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0055, 2, 0x2AA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1E74',
    )

    SetScenaFlags(ScenaFlag(0x0055, 2, 0x2AA))

    ChrTalk(
        0x0008,
        (
            '哟，艾丝蒂尔和约修亚啊，\n',
            '今天怎么这么早呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F早上好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F早上好，\n',
            '德瑟鲁厨师。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '要想满足食客们的要求，\n',
            '就得从早餐做起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '今日的主打菜式是一口气薏粉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '嗯，非常的可口啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EAE')

    def _loc_1E74(): pass

    label('loc_1E74')

    ChrTalk(
        0x0008,
        (
            '今日的主打菜式是一口气薏粉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '嗯，非常的可口啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1EAE(): pass

    label('loc_1EAE')

    TalkEnd(0x0008)

    Return()

# id: 0x0007 offset: 0x1EB2
@scena.Code('func_07_1EB2')
def func_07_1EB2():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_1F19',
    )

    ChrTalk(
        0x00FE,
        (
            '新菜单受到好评，\n',
            '材料都已经用完了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是供不应求呢。\n',
            '看来要进多一点的货才行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24DE')

    def _loc_1F19(): pass

    label('loc_1F19')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            Expr.Return,
        ),
        'loc_1F57',
    )

    ChrTurnDirection(0x00FE, 0x0103, 0)

    ChrTalk(
        0x00FE,
        (
            '哎呀，雪拉小姐。\n',
            '欢迎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请随便坐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24DE')

    def _loc_1F57(): pass

    label('loc_1F57')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_2050',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1FEE',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '我们店是在我和老公\n',
            '结婚之前开张的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以寄托了\n',
            '我们很多的思念哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看见女儿伊莉莎\n',
            '在店里帮忙，\n',
            '真是有点感慨万千啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_204D')

    def _loc_1FEE(): pass

    label('loc_1FEE')

    ChrTalk(
        0x00FE,
        (
            '我们店是在我和老公\n',
            '结婚之前开张的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看见女儿伊莉莎\n',
            '在店里帮忙，\n',
            '真是有点感慨万千啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_204D(): pass

    label('loc_204D')

    Jump('loc_24DE')

    def _loc_2050(): pass

    label('loc_2050')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_214A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_20FE',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '最近有一对十分活跃的\n',
            '新人游击士拍档……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难不成\n',
            '就是指艾丝蒂尔你们吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大名鼎鼎的游击士居然是我女儿的朋友，\n',
            '我可以在朋友面前吹嘘一番了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2147')

    def _loc_20FE(): pass

    label('loc_20FE')

    ChrTalk(
        0x00FE,
        (
            '大名鼎鼎的游击士居然是我女儿的朋友，\n',
            '我可以在朋友面前吹嘘一番了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2147(): pass

    label('loc_2147')

    Jump('loc_24DE')

    def _loc_214A(): pass

    label('loc_214A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_21B5',
    )

    ChrTalk(
        0x00FE,
        (
            '听说帕赛尔农场\n',
            '很快就能恢复供货了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像是田里\n',
            '出现了一些魔兽，\n',
            '后来请了游击士摆平了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24DE')

    def _loc_21B5(): pass

    label('loc_21B5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_227F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2240',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '帕赛尔农场\n',
            '通知我们说暂时不能给\n',
            '我们供应足够的蔬菜了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '出什么事了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '得尽快去其它农场那里想办法啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_227C')

    def _loc_2240(): pass

    label('loc_2240')

    ChrTalk(
        0x00FE,
        (
            '帕赛尔农场\n',
            '通知我们说暂时不能给\n',
            '我们供应足够的蔬菜了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_227C(): pass

    label('loc_227C')

    Jump('loc_24DE')

    def _loc_227F(): pass

    label('loc_227F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_22CD',
    )

    ChrTalk(
        0x0009,
        (
            '好，\n',
            '先把经理的工作放在一边……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '该着手进行\n',
            '做饭的准备了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24DE')

    def _loc_22CD(): pass

    label('loc_22CD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_2413',
    )

    ChrTurnDirection(0x0009, 0x0101, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_23BE',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '哎呀，艾丝蒂尔，\n',
            '好久没有看到你了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '自从你们从\n',
            '主日学校毕业之后，\n',
            '不知不觉已经过去了很久呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '你是来找伊莉莎的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '就在刚才，\n',
            '她还在店里帮忙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '需要的话我把她叫出来。\n',
            '她也肯定想见你呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2410')

    def _loc_23BE(): pass

    label('loc_23BE')

    ChrTalk(
        0x0009,
        (
            '艾丝蒂尔，\n',
            '你是来找伊莉莎的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '她在店里帮忙呢，\n',
            '需要的话我把她叫出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2410(): pass

    label('loc_2410')

    Jump('loc_24DE')

    def _loc_2413(): pass

    label('loc_2413')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2497',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0009,
        (
            '唔，昨天的销售额有所增长……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '嗯，\n',
            '客人对于早餐的评价十分高。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我们偶尔也要想想这些\n',
            '令人有干劲的事情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24DE')

    def _loc_2497(): pass

    label('loc_2497')

    ChrTalk(
        0x0009,
        (
            '唔，昨天的销售额有所增长……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '嗯，\n',
            '客人对于早餐的评价十分高。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_24DE(): pass

    label('loc_24DE')

    TalkEnd(0x0009)

    Return()

# id: 0x0008 offset: 0x24E2
@scena.Code('func_08_24E2')
def func_08_24E2():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_2690',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2630',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '这不是艾丝蒂尔和约修亚嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎么了～？\n',
            '拿着旅行包。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F唔，其实呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔告诉伊莉莎她和约修亚将要去柏斯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x00FE,
        (
            '这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我有点担心呢。\n',
            '不过你们还是早点出发比较好哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在这里等着的确\n',
            '不像是艾丝蒂尔的作风。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#001F啊哈哈……\n',
            '嗯，那我们出发了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_268D')

    def _loc_2630(): pass

    label('loc_2630')

    ChrTalk(
        0x00FE,
        (
            '这可是非同一般的\n',
            '旅行冒险啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 0)

    ChrTalk(
        0x00FE,
        (
            '约修亚、艾丝蒂尔，\n',
            '我一定会在这里支持你们的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_268D(): pass

    label('loc_268D')

    Jump('loc_3805')

    def _loc_2690(): pass

    label('loc_2690')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            Expr.Return,
        ),
        'loc_27C5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2787',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '啊，艾丝蒂尔和约修亚啊。\n',
            '欢迎光临……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F你好，小伊莉莎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0103, 400)

    ChrTalk(
        0x00FE,
        (
            '呀，连雪拉扎德姐姐也来了啊……\n',
            '今天也是来喝酒的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是不是又来\n',
            '欺负福克纳先生了啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#021F哎呀，\n',
            '我才没有欺负他呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#027F我那是疼他㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27C2')

    def _loc_2787(): pass

    label('loc_2787')

    ChrTurnDirection(0x00FE, 0x0103, 0)

    ChrTalk(
        0x00FE,
        (
            '雪拉扎德姐姐，\n',
            '是不是又来\n',
            '欺负福克纳先生了啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_27C2(): pass

    label('loc_27C2')

    Jump('loc_3805')

    def _loc_27C5(): pass

    label('loc_27C5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_28A8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2874',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '艾丝蒂尔，听我说听我说～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '前一阵里农的妈妈\n',
            '忽然来我家， \n',
            '问我要不要嫁到他们家去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '吓了我一跳呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过， \n',
            '我还是想自己挑老公。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28A5')

    def _loc_2874(): pass

    label('loc_2874')

    ChrTalk(
        0x00FE,
        (
            '里农先生年纪也不小了。\n',
            '也难怪她妈妈会担心～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_28A5(): pass

    label('loc_28A5')

    Jump('loc_3805')

    def _loc_28A8(): pass

    label('loc_28A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_2965',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2923',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '之前雪拉扎德姐姐\n',
            '来店里喝酒了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就像艾丝蒂尔说的那样，\n',
            '真是不得了呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '简直难以言表。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2962')

    def _loc_2923(): pass

    label('loc_2923')

    ChrTalk(
        0x00FE,
        (
            '之前雪拉扎德姐姐\n',
            '来店里喝酒了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之真是不得了呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2962(): pass

    label('loc_2962')

    Jump('loc_3805')

    def _loc_2965(): pass

    label('loc_2965')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_29C0',
    )

    ChrTalk(
        0x00FE,
        (
            '艾丝蒂尔、约修亚。\n',
            '怎么样？工作还顺利吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '偶尔也来我们这里休息休息啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3805')

    def _loc_29C0(): pass

    label('loc_29C0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_2B25',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2AE3',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '你们俩也终于踏出了\n',
            '成为游击士的第一步了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '客人之间已经\n',
            '在议论纷纷了呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#008F是、是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '洛连特虽说是乡下地方，\n',
            '但也有卡西乌斯先生和雪拉姐姐\n',
            '这样了不起的人物在啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家都说你们也会\n',
            '加入他们的行列呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#007F唔唔，伊莉莎，\n',
            '别给我太大压力嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B22')

    def _loc_2AE3(): pass

    label('loc_2AE3')

    ChrTalk(
        0x00FE,
        (
            '你们俩也终于踏出了\n',
            '成为游击士的第一步了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '加油哦★',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B22(): pass

    label('loc_2B22')

    Jump('loc_3805')

    def _loc_2B25(): pass

    label('loc_2B25')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_2EEF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 0, 0x210)),
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 1, 0x211)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_2BC9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2BA1',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000A,
        (
            '啊，欢迎光临～★',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '难得你们俩\n',
            '到这里来吃饭呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '爸爸和妈妈\n',
            '要我好好款待你们哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2BC6')

    def _loc_2BA1(): pass

    label('loc_2BA1')

    ChrTalk(
        0x000A,
        (
            '叫全家人都来\n',
            '好好吃一顿如何呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2BC6(): pass

    label('loc_2BC6')

    Jump('loc_2EEC')

    def _loc_2BC9(): pass

    label('loc_2BC9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0055, 1, 0x2A9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2EBF',
    )

    SetScenaFlags(ScenaFlag(0x0055, 1, 0x2A9))

    ChrTalk(
        0x000A,
        (
            '欢迎光临～☆',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '哦？艾丝蒂尔和约修亚？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F好久不见了，伊莉莎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '你们今天在一起做什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x22, 0x24, 0x000000FA, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '啊～难道说你们是在约会～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#008F哈哈哈……\n',
            '这当然不是啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '说起来，你们俩正在\n',
            '为当上游击士而努力着吧～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '做得怎么样呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，其实我们呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            '艾丝蒂尔将胸前的徽章拿给伊莉莎看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x000A,
        (
            '哇～合格了吗～？\n',
            '恭喜啊！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '这可是艾丝蒂尔\n',
            '从小就向往的职业呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哈哈，是啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '对了，为了庆祝你们俩，\n',
            '今天就到我家吃饭好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '爸爸和妈妈\n',
            '要我好好款待你们哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#001F啊，真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#018F不行呢，艾丝蒂尔。\n',
            '父亲还在家里等着我们回去呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#007F啊，对啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#501F不好意思呢，伊莉莎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '啊，唔。\n',
            '没关系呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不过你们下次\n',
            '一定要来我家吃饭哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2EEC')

    def _loc_2EBF(): pass

    label('loc_2EBF')

    ChrTalk(
        0x000A,
        (
            '艾丝蒂尔，你们下次\n',
            '一定要来我家吃饭哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2EEC(): pass

    label('loc_2EEC')

    Jump('loc_3805')

    def _loc_2EEF(): pass

    label('loc_2EEF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_3578',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 0, 0x210)),
            Expr.Return,
        ),
        'loc_31F5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0055, 0, 0x2A8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_317F',
    )

    SetScenaFlags(ScenaFlag(0x0055, 0, 0x2A8))

    ChrTalk(
        0x000A,
        (
            '咦，\n',
            '研修已经结束了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#001F是啊！\n',
            '太好了，伊莉莎！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#001F告诉你，\n',
            '我终于成为游击士了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '真的啊？\n',
            '恭喜恭喜～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '这可是艾丝蒂尔\n',
            '从小就向往的职业呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不过作为游击士，\n',
            '危险的工作也会不少的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F这个，可能会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '约修亚，你要看着艾丝蒂尔，\n',
            '不要让她蛮横乱来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '因为艾丝蒂尔\n',
            '就像一只小野猪一样，\n',
            '今后鲁莽的时候肯定不少呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F我很明白这一点，伊莉莎。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#015F不过如果她本人不太明白的话，\n',
            '还是一件比较麻烦的事情呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#009F哼，你们两个说的\n',
            '怎么全部都是我的坏话呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我和约修亚只是为你\n',
            '感到有些不放心呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '总之如果不小心的话，\n',
            '就很有可能会受伤的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#007F呼，知道了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_31F2')

    def _loc_317F(): pass

    label('loc_317F')

    ChrTalk(
        0x000A,
        (
            '约修亚，你要看着艾丝蒂尔，\n',
            '不要让她蛮横乱来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '艾丝蒂尔\n',
            '就像一只小野猪一样，\n',
            '今后鲁莽的时候肯定不少呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_31F2(): pass

    label('loc_31F2')

    Jump('loc_3575')

    def _loc_31F5(): pass

    label('loc_31F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 1, 0x211)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3502',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    SetScenaFlags(ScenaFlag(0x0042, 1, 0x211))

    ChrTalk(
        0x000A,
        (
            '欢迎光临～☆',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '哦？艾丝蒂尔和约修亚？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F好久不见了，伊莉莎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '你们今天在一起做什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x22, 0x24, 0x000000FA, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '啊～难道说你们是在约会～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F不是啦。\n',
            '听我说，伊莉莎！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#001F告诉你，\n',
            '我终于成为游击士了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '真的啊？\n',
            '恭喜恭喜～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '这可是艾丝蒂尔\n',
            '从小就向往的职业呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不过作为游击士，\n',
            '危险的工作也会不少的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F这个，可能会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '约修亚，你要看着艾丝蒂尔，\n',
            '不要让她蛮横乱来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '艾丝蒂尔\n',
            '就像一只小野猪一样，\n',
            '今后鲁莽的时候肯定不少呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F我很明白这一点，伊莉莎。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#015F不过如果她本人不太明白的话，\n',
            '还是一件比较麻烦的事情呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#009F哼，你们两个说的\n',
            '怎么全部都是我的坏话呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我和约修亚只是为你\n',
            '感到有些不放心呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '总之如果不小心的话，\n',
            '就很有可能会受伤的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#007F呼，知道了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3575')

    def _loc_3502(): pass

    label('loc_3502')

    ChrTalk(
        0x000A,
        (
            '约修亚，你要看着艾丝蒂尔，\n',
            '不要让她蛮横乱来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '艾丝蒂尔\n',
            '就像一只小野猪一样，\n',
            '今后鲁莽的时候肯定不少呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3575(): pass

    label('loc_3575')

    Jump('loc_3805')

    def _loc_3578(): pass

    label('loc_3578')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0054, 7, 0x2A7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_37A9',
    )

    SetScenaFlags(ScenaFlag(0x0054, 7, 0x2A7))
    SetScenaFlags(ScenaFlag(0x0042, 0, 0x210))

    ChrTalk(
        0x000A,
        (
            '欢迎光临～☆',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '哦？艾丝蒂尔和约修亚？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F好久不见了，伊莉莎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '你们今天在一起做什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x22, 0x24, 0x000000FA, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '啊～难道说你们是在约会～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F不是啦。\n',
            '今天就要进行游击士训练了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '这样啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '当年在主日学校\n',
            '上课的同学们都沿着\n',
            '各自的理想拼命努力了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '……不愧是艾丝蒂尔，\n',
            '选择走这样一条路。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#006F什么呀～这样不好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '嗯，没有啦，我反倒觉得\n',
            '这样才符合艾丝蒂尔你的风格哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '哦，对啦。\n',
            '缇欧已经在帮家里做农活了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '上次还叫大家\n',
            '一起去她家玩呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#004F咦……是缇欧啊。\n',
            '有这样的事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3805')

    def _loc_37A9(): pass

    label('loc_37A9')

    ChrTalk(
        0x000A,
        (
            '当年在主日学校\n',
            '上课的同学们都沿着\n',
            '各自的理想拼命努力了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '艾丝蒂尔也要好好加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3805(): pass

    label('loc_3805')

    TalkEnd(0x000A)

    Return()

# id: 0x0009 offset: 0x3809
@scena.Code('func_09_3809')
def func_09_3809():
    Call(0, 0x000A)

    Return()

# id: 0x000A offset: 0x380E
@scena.Code('func_0A_380E')
def func_0A_380E():
    TalkBegin(0x000B)
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
            TXT(0x00, '对话\n'),
            TXT(0x01, '买东西\n'),
            TXT(0x02, '欢迎品尝「一口气薏粉」100米拉\n'),
            TXT(0x03, '离开\n'),
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
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3896',
    )

    FadeIn(300, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_388E',
    )

    OP_A9(0x75)

    Jump('loc_3890')

    def _loc_388E(): pass

    label('loc_388E')

    OP_A9(0x05)

    def _loc_3890(): pass

    label('loc_3890')

    OP_56(0x00)
    TalkEnd(0x000B)

    Return()

    def _loc_3896(): pass

    label('loc_3896')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3994',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x12),
            (Expr.PushLong, 0x64),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_395F',
    )

    RemoveMira(100)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    PlaySE(11, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x0),
            '尝了尝',
            (TxtCtl.SetColor, 0x2),
            '一口气薏粉',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetStatus(0x0000, 0xFD, 180)
    ChrSetStatus(0x0001, 0xFD, 180)
    ChrSetStatus(0x0002, 0xFD, 180)
    ChrSetStatus(0x0003, 0xFD, 180)
    ChrSetStatus(0x0004, 0xFD, 180)
    ChrSetStatus(0x0005, 0xFD, 180)
    ChrSetStatus(0x0006, 0xFD, 180)
    ChrSetStatus(0x0007, 0xFD, 180)

    If(
        (
            (Expr.Eval, "OP_40(0x020D)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3951',
    )

    If(
        (
            (Expr.Eval, "OP_AC(0x0003)"),
            Expr.Return,
        ),
        'loc_3929',
    )

    Jump('loc_3951')

    def _loc_3929(): pass

    label('loc_3929')

    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x0),
            '学会了',
            (TxtCtl.SetColor, 0x2),
            '一口气薏粉',
            (TxtCtl.SetColor, 0x0),
            '的做法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3951(): pass

    label('loc_3951')

    OP_56(0x00)
    FadeIn(1000, 0)

    Jump('loc_3985')

    def _loc_395F(): pass

    label('loc_395F')

    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '没有足够的米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeIn(300, 0)
    def _loc_3985(): pass

    label('loc_3985')

    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x000B)

    Return()

    def _loc_3994(): pass

    label('loc_3994')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_39AE',
    )

    FadeIn(300, 0)
    TalkEnd(0x000B)

    Return()

    def _loc_39AE(): pass

    label('loc_39AE')

    FadeIn(300, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_3AC4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3A5D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000B,
        (
            '说起来之前市长官邸\n',
            '好像被强盗洗劫了一番哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '偏偏是选择市长官邸下手，\n',
            '看来犯人也挺猖狂的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '啊啊，总之没有人受伤\n',
            '就已经让人安心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3AC1')

    def _loc_3A5D(): pass

    label('loc_3A5D')

    ChrTalk(
        0x000B,
        (
            '说起来之前市长官邸\n',
            '好像被强盗洗劫了一番哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '偏偏是选择市长官邸下手，\n',
            '看来犯人也挺猖狂的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3AC1(): pass

    label('loc_3AC1')

    Jump('loc_44E4')

    def _loc_3AC4(): pass

    label('loc_3AC4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            Expr.Return,
        ),
        'loc_3C6E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3C4D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x0103,
        (
            '#020F你好啊，福克纳㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x0103, 400)
    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000B,
        (
            '啊，雪、雪拉扎德小姐！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '欢、欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#027F什么嘛，你慌什么呀。\n',
            '不用担心，我现在在工作呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '那、那太好了。\n',
            '不不，您辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#027F呵呵，工作结束之后\n',
            '我会再来这里喝一杯的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#027F到时还请多关照啊㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '哈、哈哈……恭候光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#007F（唉，被吓到了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#017F（还被吓得不轻呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3C6B')

    def _loc_3C4D(): pass

    label('loc_3C4D')

    ChrTalk(
        0x000B,
        (
            '……我今天要不要早退呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3C6B(): pass

    label('loc_3C6B')

    Jump('loc_44E4')

    def _loc_3C6E(): pass

    label('loc_3C6E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_3EAB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3E33',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000B,
        (
            '游击士协会的人\n',
            '酒量都很好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '雪拉扎德小姐就不用说了，\n',
            '卡西乌斯先生也挺能喝的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '不过，爱娜小姐真是叫人意外。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F我们听雪拉姐姐说过，\n',
            '爱娜小姐的酒量也是挺厉害的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '是啊，她可是\n',
            '和雪拉扎德小姐同一个级别的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '而且喝完之后脸色都一点没变，\n',
            '一直都那么悠悠然的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#506F哈哈，只要不像雪拉姐那样\n',
            '胡搅蛮缠就已经很好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '看起来，\n',
            '游击士协会真是恐怖的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '……啊，\n',
            '只有利吉先生倒是不大能喝呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3EA8')

    def _loc_3E33(): pass

    label('loc_3E33')

    ChrTalk(
        0x000B,
        (
            '竟然有人能和\n',
            '雪拉扎德小姐是一个级别的，\n',
            '真是叫人吃惊了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '而这个人居然是爱娜小姐，\n',
            '这就更叫人惊上加惊了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3EA8(): pass

    label('loc_3EA8')

    Jump('loc_44E4')

    def _loc_3EAB(): pass

    label('loc_3EAB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_4046',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3FF3',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000B,
        (
            '之前雪拉扎德小姐\n',
            '来光顾我们店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '我一直陪她到打烊，\n',
            '真是惨不堪言呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '她连喝了五瓶\n',
            '我们这里最烈的酒，\n',
            '而且还一点醉意都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F是啊，\n',
            '雪拉姐喝醉这种事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F闻所未闻见所未见呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '伊莉莎自己躲起来了，\n',
            '厨师长也先回去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '结果第二天我整个人软绵绵的，\n',
            '根本都没法工作呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4043')

    def _loc_3FF3(): pass

    label('loc_3FF3')

    ChrTalk(
        0x000B,
        (
            '之前雪拉扎德小姐\n',
            '来光顾我们店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '我一直陪她到打烊，\n',
            '真是惨不堪言呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4043(): pass

    label('loc_4043')

    Jump('loc_44E4')

    def _loc_4046(): pass

    label('loc_4046')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_41E6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4168',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000B,
        (
            '洛连特支部里有个\n',
            '叫雪拉扎德的\n',
            '外国游击士对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '长得又漂亮，\n',
            '又经常光顾本店，\n',
            '我们是很欢迎她来的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '不过喝了酒之后可真是不得了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '要说怎么个不得了法嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F哈哈，这我知道……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#015F深有体会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '唉，平时倒真是个\n',
            '爽朗又漂亮的大姐姐啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_41E3')

    def _loc_4168(): pass

    label('loc_4168')

    ChrTalk(
        0x000B,
        (
            '之前雪拉扎德小姐\n',
            '一个人来的时候实在是有点恐怖。\n',
            '因为要陪她喝酒的那个人是我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '平时倒真是个\n',
            '爽朗又漂亮的大姐姐啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_41E3(): pass

    label('loc_41E3')

    Jump('loc_44E4')

    def _loc_41E6(): pass

    label('loc_41E6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_422F',
    )

    ChrTalk(
        0x000B,
        (
            '厨师长忽然要我们\n',
            '改换进货商……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '是不是出什么事了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_44E4')

    def _loc_422F(): pass

    label('loc_422F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_434D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_42D5',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000B,
        (
            '我们这儿的厨师可以\n',
            '灵活地运用食材让乡村的\n',
            '风味得以完全地展现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '洛连特周围有很多农场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '我向你们极力推荐那道\n',
            '用野菜制成的主打菜品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_434A')

    def _loc_42D5(): pass

    label('loc_42D5')

    ChrTalk(
        0x000B,
        (
            '我们这儿的厨师可以\n',
            '灵活地运用食材让乡村的\n',
            '风味得以完全地展现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '我向你们极力推荐那道\n',
            '用野菜制成的主打菜品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_434A(): pass

    label('loc_434A')

    Jump('loc_44E4')

    def _loc_434D(): pass

    label('loc_434D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_4472',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4408',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000B,
        (
            '在那边坐的那位女商人\n',
            '好像是从柏斯来的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '头脑又聪明，\n',
            '人又长得漂亮。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '像我这种人\n',
            '根本就配不上她啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '……可是，她说话的口音\n',
            '总让人感觉有些怪怪的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_446F')

    def _loc_4408(): pass

    label('loc_4408')

    ChrTalk(
        0x000B,
        (
            '在那边的那位女商人\n',
            '头脑又聪明，\n',
            '人又长得漂亮。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '……可是，她说话的口音\n',
            '总让人感觉有些怪怪的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_446F(): pass

    label('loc_446F')

    Jump('loc_44E4')

    def _loc_4472(): pass

    label('loc_4472')

    ChrTalk(
        0x000B,
        (
            '酒吧刚开的时候，\n',
            '我是作为一个\n',
            '服务生来这里工作的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '自从店里开始\n',
            '提供早餐和午餐，\n',
            '我就成为了一个酒保了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_44E4(): pass

    label('loc_44E4')

    TalkEnd(0x000B)

    Return()

# id: 0x000B offset: 0x44E8
@scena.Code('func_0B_44E8')
def func_0B_44E8():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_45F8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_45BA',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '香香香香……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不错不错不错不错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好吃好吃好吃好吃……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '…………打嗝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '刚才好像在街上看到了老大。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '反正小心不要让他发现\n',
            '我翘班来这里吃东西就行了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_45F5')

    def _loc_45BA(): pass

    label('loc_45BA')

    ChrTalk(
        0x00FE,
        (
            '香香香香……\n',
            '不错不错好吃好吃……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '…………打嗝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_45F5(): pass

    label('loc_45F5')

    Jump('loc_4977')

    def _loc_45F8(): pass

    label('loc_45F8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_46E3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_46B9',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '香香香香……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不错不错不错不错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好吃好吃好吃好吃……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '…………打嗝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '玛鲁加矿山的魔兽事件\n',
            '也总算平静下来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总算可以\n',
            '悠悠闲闲地吃饭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_46E0')

    def _loc_46B9(): pass

    label('loc_46B9')

    ChrTalk(
        0x00FE,
        (
            '香香香香……\n',
            '不错不错好吃好吃……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_46E0(): pass

    label('loc_46E0')

    Jump('loc_4977')

    def _loc_46E3(): pass

    label('loc_46E3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_47B9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_477B',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x000C,
        (
            '香香香香……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '不错不错不错不错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '好吃好吃好吃好吃……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '…………打嗝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '再来一杯，\n',
            '再来一杯我就回去工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_47B6')

    def _loc_477B(): pass

    label('loc_477B')

    ChrTalk(
        0x000C,
        (
            '香香香香……\n',
            '不错不错好吃好吃……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '…………打嗝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_47B6(): pass

    label('loc_47B6')

    Jump('loc_4977')

    def _loc_47B9(): pass

    label('loc_47B9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_48A5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4867',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x000C,
        (
            '香香香香……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '不错不错不错不错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '好吃好吃好吃好吃……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '…………打嗝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '如果不快点吃完回矿山的话，\n',
            '我旷工的事情就会被老大发现的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_48A2')

    def _loc_4867(): pass

    label('loc_4867')

    ChrTalk(
        0x000C,
        (
            '香香香香……\n',
            '不错不错好吃好吃……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '…………打嗝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_48A2(): pass

    label('loc_48A2')

    Jump('loc_4977')

    def _loc_48A5(): pass

    label('loc_48A5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_493C',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x000C,
        (
            '香香香香……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '不错不错不错不错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '好吃好吃好吃好吃……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '…………打嗝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '因为在矿山工作的缘故，\n',
            '很容易变得饿起来～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4977')

    def _loc_493C(): pass

    label('loc_493C')

    ChrTalk(
        0x000C,
        (
            '香香香香……\n',
            '不错不错好吃好吃……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '…………打嗝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4977(): pass

    label('loc_4977')

    TalkEnd(0x000C)

    Return()

# id: 0x000C offset: 0x497B
@scena.Code('func_0C_497B')
def func_0C_497B():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_4A53',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4A06',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '啊啊，玛鲁加矿山\n',
            '开采出来的那颗翠耀石，\n',
            '我真想以个人的身份买下来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到底是什么人\n',
            '抢在我之前买走了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4A50')

    def _loc_4A06(): pass

    label('loc_4A06')

    ChrTalk(
        0x00FE,
        (
            '啊啊，玛鲁加矿山\n',
            '开采出来的那颗翠耀石，\n',
            '我真想以个人的身份买下来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4A50(): pass

    label('loc_4A50')

    Jump('loc_4F8C')

    def _loc_4A53(): pass

    label('loc_4A53')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_4B8A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4B29',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '我听说洛连特的\n',
            '游击士中有很多\n',
            '很厉害的人物在哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听说最近还新加入两个\n',
            '很有前途的年轻人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个城镇不仅资源丰富，\n',
            '人才也很多呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是能网罗到有前途的新人，\n',
            '小姐也会开心的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4B87')

    def _loc_4B29(): pass

    label('loc_4B29')

    ChrTalk(
        0x00FE,
        (
            '这个城镇不仅资源丰富，\n',
            '人才也很多呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是能网罗到有前途的新人，\n',
            '小姐也会开心的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4B87(): pass

    label('loc_4B87')

    Jump('loc_4F8C')

    def _loc_4B8A(): pass

    label('loc_4B8A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_4C88',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4C43',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '哎呀，\n',
            '这次可真走运。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '想不到正在谈判的时候\n',
            '矿山竟然发现了新矿脉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听到这种消息，\n',
            '比看在父亲的份上去听\n',
            '帝国商人啰里啰嗦要好得多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对吧，西蒙？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4C85')

    def _loc_4C43(): pass

    label('loc_4C43')

    ChrTalk(
        0x00FE,
        (
            '虽然很多人认为\n',
            '洛连特是乡下地方，\n',
            '但其实却是个资源的宝库啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4C85(): pass

    label('loc_4C85')

    Jump('loc_4F8C')

    def _loc_4C88(): pass

    label('loc_4C88')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_4D89',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4D30',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x000D,
        (
            '呵呵，西蒙！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '这次我特意来做这笔生意，\n',
            '真是来对了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '预订的七耀石\n',
            '已经全部收购完毕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '过不了多久这些东西\n',
            '就会产生更多的价值了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4D86')

    def _loc_4D30(): pass

    label('loc_4D30')

    ChrTalk(
        0x000D,
        (
            '预订的七耀石\n',
            '已经全部收购完毕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '过不了多久这些东西\n',
            '就会产生更多的价值了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4D86(): pass

    label('loc_4D86')

    Jump('loc_4F8C')

    def _loc_4D89(): pass

    label('loc_4D89')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_4E86',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4E27',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x000D,
        (
            '木材方面\n',
            '无论如何都要确保足够的购入量。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '我说西蒙，\n',
            '七耀石的收购没问题吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '我特地来到洛连特做这笔交易，\n',
            '怎么能让它失败呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4E83')

    def _loc_4E27(): pass

    label('loc_4E27')

    ChrTalk(
        0x000D,
        (
            '我说西蒙，\n',
            '七耀石的收购没问题吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '我特地来到洛连特做这笔交易，\n',
            '怎么能让它失败呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4E83(): pass

    label('loc_4E83')

    Jump('loc_4F8C')

    def _loc_4E86(): pass

    label('loc_4E86')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4F12',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x000D,
        (
            '西蒙，你听好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '现在是应该收购洛连特的\n',
            '木材和七耀石的时候了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '无论风险有多大，\n',
            '只要预算允许就尽量多购入一些。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4F8C')

    def _loc_4F12(): pass

    label('loc_4F12')

    ChrTalk(
        0x000D,
        (
            '目标就是女王诞辰庆典，\n',
            '到了那个时候价格就会上扬了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '趁现在还是便宜的时候买入，\n',
            '到了那个时候就可以好好赚一笔了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4F8C(): pass

    label('loc_4F8C')

    TalkEnd(0x000D)

    Return()

# id: 0x000D offset: 0x4F90
@scena.Code('func_0D_4F90')
def func_0D_4F90():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_5007',
    )

    ChrTalk(
        0x00FE,
        (
            '米拉诺小姐，下次的谈判就要开始了，\n',
            '差不多该回柏斯去了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '小姐也一定对这次的报告\n',
            '迫不及待了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_51F9')

    def _loc_5007(): pass

    label('loc_5007')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_505C',
    )

    ChrTalk(
        0x00FE,
        (
            '米拉诺小姐，那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我、我想我们实在是\n',
            '没什么时间去招募人才了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_51F9')

    def _loc_505C(): pass

    label('loc_505C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_509F',
    )

    ChrTalk(
        0x00FE,
        (
            '米拉诺小姐伶牙俐齿，\n',
            '真是说不过她啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉唉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_51F9')

    def _loc_509F(): pass

    label('loc_509F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_50F2',
    )

    ChrTalk(
        0x000E,
        (
            '说起来最近在玛鲁加矿山\n',
            '好像发现了新的矿脉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '或许很值得期待哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_51F9')

    def _loc_50F2(): pass

    label('loc_50F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_515C',
    )

    ChrTalk(
        0x000E,
        (
            '嗯，这个嘛，\n',
            '我已经和玛鲁加矿山的人取得了联系，\n',
            '商谈也正在进行中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '再耐心等待一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_51F9')

    def _loc_515C(): pass

    label('loc_515C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_51B9',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x000E,
        (
            '好、好的，木材方面\n',
            '事情都已经安排好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '七耀石那边也开始着手进行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_51F9')

    def _loc_51B9(): pass

    label('loc_51B9')

    ChrTalk(
        0x000E,
        (
            '木材方面\n',
            '事情都已经安排好了。\n',
            '七耀石那边也开始着手进行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_51F9(): pass

    label('loc_51F9')

    TalkEnd(0x000E)

    Return()

# id: 0x000E offset: 0x51FD
@scena.Code('func_0E_51FD')
def func_0E_51FD():
    TalkBegin(0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_5307',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_52BF',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '我也是个男人。\n',
            '所以我下定决心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '绝对信任女儿选择的男人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那家伙一定能\n',
            '成为独当一面的人，\n',
            '给我的女儿带来幸福。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也要尽我所能，\n',
            '在工作上好好协助他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5304')

    def _loc_52BF(): pass

    label('loc_52BF')

    ChrTalk(
        0x00FE,
        (
            '我也是个男人。\n',
            '所以我下定决心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '绝对信任女儿选择的男人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5304(): pass

    label('loc_5304')

    Jump('loc_53C1')

    def _loc_5307(): pass

    label('loc_5307')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_538A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x000F,
        (
            '哼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '太嫩了，\n',
            '那家伙也不过是个半吊子而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '想在两三年内\n',
            '在林业上做出好成绩来，\n',
            '这种想法也太天真了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_53C1')

    def _loc_538A(): pass

    label('loc_538A')

    ChrTalk(
        0x000F,
        (
            '哼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '太嫩了，\n',
            '那家伙也不过是个半吊子而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_53C1(): pass

    label('loc_53C1')

    TalkEnd(0x000F)

    Return()

# id: 0x000F offset: 0x53C5
@scena.Code('func_0F_53C5')
def func_0F_53C5():
    TalkBegin(0x0011)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_54DD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5476',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '昨天，我看到南面\n',
            '好像有什么东西在空中盘旋着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果是鸟的话也太大了吧。\n',
            '究竟是什么东西呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '年纪老了眼睛也不中用了，\n',
            '看什么东西都不清楚了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_54DA')

    def _loc_5476(): pass

    label('loc_5476')

    ChrTalk(
        0x00FE,
        (
            '昨天，我看到南面\n',
            '好像有什么东西在空中盘旋着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果是鸟的话也太大了吧。\n',
            '究竟是什么东西呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_54DA(): pass

    label('loc_54DA')

    Jump('loc_5611')

    def _loc_54DD(): pass

    label('loc_54DD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_55C1',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '１０年前，突破了国境线的帝国军\n',
            '曾经将洛连特重重包围。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '然后为了迫使市民投降\n',
            '竟然炮轰了那座钟楼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#003F…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔……对不起。\n',
            '又让你想起那件事了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F不不，没事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#014F……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5611')

    def _loc_55C1(): pass

    label('loc_55C1')

    ChrTalk(
        0x00FE,
        (
            '如今城市和钟楼\n',
            '都已经恢复如初了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但还是留下了许多\n',
            '看不见的伤痕啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5611(): pass

    label('loc_5611')

    TalkEnd(0x0011)

    Return()

# id: 0x0010 offset: 0x5615
@scena.Code('func_10_5615')
def func_10_5615():
    TalkBegin(0x0012)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_573A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_56CF',
    )

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x0012,
        (
            '呀，是艾丝蒂尔和约修亚啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '前一阵我在米尔西街道见到了一种\n',
            '四处乱蹿异常敏捷的魔兽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '闪着光冲过来，\n',
            '一眨眼功夫就又逃走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '到底是什么东西呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5737')

    def _loc_56CF(): pass

    label('loc_56CF')

    ChrTalk(
        0x0012,
        (
            '前一阵我在米尔西街道见到了一种\n',
            '四处乱蹿异常敏捷的魔兽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '闪着光冲过来，\n',
            '一眨眼功夫就又逃走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5737(): pass

    label('loc_5737')

    Jump('loc_584C')

    def _loc_573A(): pass

    label('loc_573A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_584C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_57E9',
    )

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x0012,
        (
            '呀，是艾丝蒂尔和约修亚啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F利吉哥哥……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '你们第一天当上游击士\n',
            '就发生了大事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '听说连卡西乌斯先生\n',
            '都出动来帮你们了，\n',
            '应该没事吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_584C')

    def _loc_57E9(): pass

    label('loc_57E9')

    ChrTalk(
        0x0012,
        (
            '你们第一天当上游击士\n',
            '就发生了大事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '听说连卡西乌斯先生\n',
            '都出动来帮你们了，\n',
            '应该没事吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_584C(): pass

    label('loc_584C')

    TalkEnd(0x0012)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

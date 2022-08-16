import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T1111_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1111   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1111.x'
    header.mapIndex       = 1
    header.bgm            = 11
    header.flags          = 0x0001
    header.entryFunction  = 0x0000
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T1111_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
        ('ED6_DT07/CH02360._CH', 'ED6_DT07/CH02360P._CP'),
        ('ED6_DT07/CH02370._CH', 'ED6_DT07/CH02370P._CP'),
        ('ED6_DT07/CH01410._CH', 'ED6_DT07/CH01410P._CP'),
        ('ED6_DT07/CH01350._CH', 'ED6_DT07/CH01350P._CP'),
        ('ED6_DT07/CH02363._CH', 'ED6_DT07/CH02363P._CP'),
        ('ED6_DT07/CH01560._CH', 'ED6_DT07/CH01560P._CP'),
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
        ('ED6_DT07/CH01123._CH', 'ED6_DT07/CH01123P._CP'),
        ('ED6_DT26/CH20361._CH', 'ED6_DT26/CH20361P._CP'),
    ]

# id: 0x10001 offset: 0xF2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '梅贝尔市长',
            x                   = -120710,
            z                   = 200,
            y                   = 68600,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '莉拉',
            x                   = -121000,
            z                   = 0,
            y                   = -1300,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '修女萝萨',
            x                   = -117100,
            z                   = 0,
            y                   = -2170,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '萨拉',
            x                   = -64200,
            z                   = -3000,
            y                   = 66350,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '管家门特斯',
            x                   = 4000,
            z                   = 500,
            y                   = -870,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '玛依森老人',
            x                   = -1860,
            z                   = 500,
            y                   = -3840,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '哈尔德',
            x                   = 6790,
            z                   = 700,
            y                   = 1130,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0195,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
    )

# id: 0x10002 offset: 0x1D2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x1D2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x1D2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -117140,
            triggerZ            = 0,
            triggerY            = -1120,
            triggerRange        = 400,
            actorX              = -114920,
            actorZ              = 1500,
            actorY              = -1340,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1F6
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_209',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    Event(0, func_0D_391F)

    def _loc_209(): pass

    label('loc_209')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_269',
    )

    ChrSetPos(0x000C, -760, 500, -1050, 135)
    ChrSetPos(0x0009, -6170, 4500, 2730, 280)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_244',
    )

    CreateThread(0x0009, 0x00, 0x00, func_02_4A3)

    Jump('loc_266')

    def _loc_244(): pass

    label('loc_244')

    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetPos(0x000B, -117020, 0, 66660, 90)
    CreateThread(0x000B, 0x00, 0x00, func_03_620)

    def _loc_266(): pass

    label('loc_266')

    Jump('loc_40C')

    def _loc_269(): pass

    label('loc_269')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_27A',
    )

    CreateThread(0x0009, 0x00, 0x00, func_02_4A3)

    Jump('loc_40C')

    def _loc_27A(): pass

    label('loc_27A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_2F6',
    )

    ChrSetPos(0x0009, -115400, 0, -1540, 180)
    ChrSetPos(0x000C, 4160, 500, -950, 180)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, -121500, 0, -4140, 270)
    OP_4A(0x0009, 255)
    ChrSetFlags(0x0009, 0x0004)
    ChrSetFlags(0x0009, 0x0010)
    ChrSetChipByIndex(0x0009, 8)
    ChrSetSubChip(0x0009, 1)
    ChrSetChipByIndex(0x0008, 0)
    ChrClearFlags(0x0008, 0x0010)
    ChrSetPos(0x0008, -116800, 0, -2420, 45)
    CreateThread(0x0008, 0x00, 0x00, func_02_4A3)

    Jump('loc_40C')

    def _loc_2F6(): pass

    label('loc_2F6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_37A',
    )

    ChrSetPos(0x0009, -115400, 0, -1540, 180)
    ChrSetPos(0x000C, -210, 500, -880, 270)
    ChrSetFlags(0x000C, 0x0010)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, -1550, 500, -880, 90)
    ChrSetFlags(0x000D, 0x0010)
    OP_4A(0x0009, 255)
    ChrSetFlags(0x0009, 0x0004)
    ChrSetFlags(0x0009, 0x0010)
    ChrSetChipByIndex(0x0009, 8)
    ChrSetSubChip(0x0009, 0)
    ChrSetPos(0x000A, -116810, 0, -1060, 90)

    Jump('loc_40C')

    def _loc_37A(): pass

    label('loc_37A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_3FE',
    )

    ChrSetChipByIndex(0x0008, 4)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetPos(0x0008, -120760, 200, 68570, 180)
    ChrSetPos(0x0009, -115400, 0, -1540, 180)
    ChrSetPos(0x000B, -117050, 0, -1280, 90)
    ChrSetFlags(0x000B, 0x0010)
    ChrSetPos(0x000C, 570, 500, 1500, 180)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    OP_4A(0x0009, 255)
    ChrSetFlags(0x0009, 0x0004)
    ChrSetFlags(0x0009, 0x0010)
    ChrSetChipByIndex(0x0009, 8)
    ChrSetSubChip(0x0009, 0)

    Jump('loc_40C')

    def _loc_3FE(): pass

    label('loc_3FE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_40C',
    )

    CreateThread(0x0009, 0x00, 0x00, func_02_4A3)

    def _loc_40C(): pass

    label('loc_40C')

    Return()

# id: 0x0001 offset: 0x40D
@scena.Code('func_01_40D')
def func_01_40D():
    OP_64(0x00, 0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_41B',
    )

    Jump('loc_473')

    def _loc_41B(): pass

    label('loc_41B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_436',
    )

    OP_10(0x00, 0x00)
    OP_10(0x0B, 0x01)
    OP_6F(0x000D, 15)
    OP_65(0x00, 0x0001)

    Jump('loc_473')

    def _loc_436(): pass

    label('loc_436')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_451',
    )

    OP_6F(0x000D, 15)
    OP_10(0x00, 0x00)
    OP_10(0x0B, 0x01)
    OP_65(0x00, 0x0001)

    Jump('loc_473')

    def _loc_451(): pass

    label('loc_451')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_46C',
    )

    OP_6F(0x000D, 15)
    OP_10(0x00, 0x00)
    OP_10(0x0B, 0x01)
    OP_65(0x00, 0x0001)

    Jump('loc_473')

    def _loc_46C(): pass

    label('loc_46C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_473',
    )

    def _loc_473(): pass

    label('loc_473')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4A2',
    )

    OP_71(0x0004, 0x0004)
    OP_71(0x0005, 0x0004)
    OP_71(0x0006, 0x0004)
    OP_71(0x0007, 0x0004)
    OP_71(0x0008, 0x0004)
    OP_71(0x0009, 0x0004)
    OP_71(0x000A, 0x0004)

    def _loc_4A2(): pass

    label('loc_4A2')

    Return()

# id: 0x0002 offset: 0x4A3
@scena.Code('func_02_4A3')
def func_02_4A3():
    ExecExpressionWithReg(
        0x0001,
        (
            Expr.Rand,
            (Expr.PushLong, 0xE),
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
        'loc_4C8',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_60A')

    def _loc_4C8(): pass

    label('loc_4C8')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4E1',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_60A')

    def _loc_4E1(): pass

    label('loc_4E1')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4FA',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_60A')

    def _loc_4FA(): pass

    label('loc_4FA')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_513',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_60A')

    def _loc_513(): pass

    label('loc_513')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_52C',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_60A')

    def _loc_52C(): pass

    label('loc_52C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_545',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_60A')

    def _loc_545(): pass

    label('loc_545')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_55E',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_60A')

    def _loc_55E(): pass

    label('loc_55E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_577',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_60A')

    def _loc_577(): pass

    label('loc_577')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_590',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_60A')

    def _loc_590(): pass

    label('loc_590')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5A9',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_60A')

    def _loc_5A9(): pass

    label('loc_5A9')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5C2',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_60A')

    def _loc_5C2(): pass

    label('loc_5C2')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5DB',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_60A')

    def _loc_5DB(): pass

    label('loc_5DB')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5F4',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_60A')

    def _loc_5F4(): pass

    label('loc_5F4')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_60A',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_60A(): pass

    label('loc_60A')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_61F',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_60A')

    def _loc_61F(): pass

    label('loc_61F')

    Return()

# id: 0x0003 offset: 0x620
@scena.Code('func_03_620')
def func_03_620():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_643',
    )

    OP_8D(0x00FE, -118390, 67890, -115780, 64680, 1500)

    Jump('func_03_620')

    def _loc_643(): pass

    label('loc_643')

    Return()

# id: 0x0004 offset: 0x644
@scena.Code('func_04_644')
def func_04_644():
    If(
        (
            (Expr.Eval, "OP_29(0x0079, 0x01, 0x0004)"),
            (Expr.Eval, "OP_29(0x0079, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0079, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_664',
    )

    Call(1, 0x0001)

    Return()

    def _loc_664(): pass

    label('loc_664')

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0x8, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x05,
        (
            (Expr.GetChrWork, 0x8, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x0008)
    ChrClearFlags(0x0008, 0x0010)
    ChrTurnDirection(0x0008, 0x0000, 0)

    ExecExpressionWithValue(
        0x0008,
        0x04,
        (
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x04,
        (
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0x8, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x05,
        (
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_6F4',
    )

    Jump('loc_736')

    def _loc_6F4(): pass

    label('loc_6F4')

    If(
        (
            (Expr.GetChrWork, 0x8, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_710',
    )

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_736')

    def _loc_710(): pass

    label('loc_710')

    If(
        (
            (Expr.GetChrWork, 0x8, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_72C',
    )

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_736')

    def _loc_72C(): pass

    label('loc_72C')

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.GetChrWork, 0x8, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_736(): pass

    label('loc_736')

    ExecExpressionWithValue(
        0x0008,
        0x04,
        (
            (Expr.GetChrWork, 0x0, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x0008, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_D74',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 0, 0x2090)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C83',
    )

    ChrTalk(
        0x0008,
        (
            '#0360350284V#613F呀、艾丝蒂尔，\n',
            '还有约修亚也来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350285V#1000F你好、梅贝尔市长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350286V#1040F……好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360350287V#611F呵呵，真的是呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360350288V看起来还是\n',
            '那么忙碌呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350289V#1016F市长也\n',
            '很辛苦的样子嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010350290V我听卢格兰爷爷说了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350291V#1035F好象这里也有市民\n',
            '冲进来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360350292V#615F嗯嗯，一直说服到半夜\n',
            '才总算让他们回去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360350293V#612F不过，这样并不能\n',
            '消除市民的不安。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360350294V这个状况长久持续下去的话\n',
            '恐怕还会引起骚乱的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350295V#1043F的确是这样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020350296V因为结果还是\n',
            '什么也没能解决。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350297V#1006F不过，不管怎样\n',
            '只能做力所能及的事了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010350298V就算低头烦恼，\n',
            '导力器也不会动起来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AA5',
    )

    ChrTalk(
        0x0106,
        (
            '#0050350299V#051F啊啊，说得对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050350300V不管结果怎样，\n',
            '我们都只能尽游击士的本分。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B82')

    def _loc_AA5(): pass

    label('loc_AA5')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B14',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350301V#020F嗯嗯，说得对呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030350302V无论结果如何，\n',
            '我们都只能尽游击士的本分。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B82')

    def _loc_B14(): pass

    label('loc_B14')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B82',
    )

    ChrTalk(
        0x0108,
        (
            '#0080350303V#070F唔，你说得对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080350304V尽人事听天命……\n',
            '我们就尽游击士的本分就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B82(): pass

    label('loc_B82')

    ChrTalk(
        0x0008,
        (
            '#0360350305V#610F呵呵，我也有同感。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360350306V无论状况如何，\n',
            '保护城市是市长的职责……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360350307V当然，我相信各位\n',
            '最后终能解决问题的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010350308V#1008F啊，啊哈哈……\n',
            '这可是责任重大哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350309V#1049F我就当是\n',
            '鼓励的话记下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0412, 0, 0x2090))

    Jump('loc_D71')

    def _loc_C83(): pass

    label('loc_C83')

    ChrTalk(
        0x0008,
        (
            '#0360350310V#610F现在只有各自\n',
            '尽力而为了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360350311V这些努力积累在一起，\n',
            '我相信一定能成为\n',
            '渡过危机的力量。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360350312V我也打算先和有实力的商人\n',
            '谈谈看。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360350313V这种状况下一定要保持物价安定，\n',
            '所以他们的协助是不可或缺的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_D71(): pass

    label('loc_D71')

    Jump('loc_1BD6')

    def _loc_D74(): pass

    label('loc_D74')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_1638',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0079, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_1343',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0079, 0x01, 0x2000)"),
            Expr.Return,
        ),
        'loc_DEB',
    )

    ChrTalk(
        0x0008,
        (
            '#0360320285V#610F虽然时间短暂，\n',
            '还请尽情放松。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360320286V休息也是为工作做准备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1340')

    def _loc_DEB(): pass

    label('loc_DEB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034A, 2, 0x1A52)),
            Expr.Return,
        ),
        'loc_10A0',
    )

    ChrTalk(
        0x0008,
        (
            '#0360320287V#610F啊，各位……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360320288V刚才莉拉的事…\n',
            '十分感谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360320289V#617F很令人吃惊吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320290V#1016F嗯、嗯……\n',
            '真是吓了一跳。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320291V#1000F不过，最后也妥善解决了，\n',
            '能帮上忙真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360320292V#610F嗯嗯，真是帮了大忙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360320293V这次又是到了最后的最后\n',
            '麻烦你们帮忙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360320294V去了瓦雷利亚湖畔\n',
            '请务必好好休息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320295V#1001F嘿嘿，我们会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_FCB',
    )

    ChrTalk(
        0x0103,
        (
            '#0030320296V#020F难得的休假，\n',
            '就恭敬不如从命了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_104E')

    def _loc_FCB(): pass

    label('loc_FCB')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1010',
    )

    ChrTalk(
        0x0106,
        (
            '#0050320297V#051F是啊，正打算\n',
            '好好修养一下呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_104E')

    def _loc_1010(): pass

    label('loc_1010')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_104E',
    )

    ChrTalk(
        0x0104,
        (
            '#0040320298V#031F呼，不用说\n',
            '我也会放松的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_104E(): pass

    label('loc_104E')

    ChrTalk(
        0x0008,
        (
            '#0360320299V#611F嗯嗯，请尽情享用。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360320300V那么，祝各位休假愉快……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_133A')

    def _loc_10A0(): pass

    label('loc_10A0')

    ChrTalk(
        0x0008,
        (
            '#0360320287V#610F啊，各位……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360320288V刚才莉拉的事…\n',
            '十分感谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360320303V还有那个金耀石结晶……\n',
            '我会小心使用的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360320304V对了，关于票的事情\n',
            '已经听说了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320305V#1018F啊，嗯。\n',
            '就在刚才。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320306V难得市长一番好意，\n',
            '我们就打算恭敬不如从命了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360320307V#610F嗯嗯，请务必要去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360320308V虽然时间短暂，\n',
            '但请好好休息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1244',
    )

    ChrTalk(
        0x0103,
        (
            '#0030320309V#020F嗯嗯，就轻松一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12AD')

    def _loc_1244(): pass

    label('loc_1244')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1278',
    )

    ChrTalk(
        0x0106,
        (
            '#0050320310V#051F啊啊，会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12AD')

    def _loc_1278(): pass

    label('loc_1278')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_12AD',
    )

    ChrTalk(
        0x0104,
        (
            '#0040320311V#031F呼，就这样定了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12AD(): pass

    label('loc_12AD')

    ChrTalk(
        0x0101,
        (
            '#0010320312V#1000F嗯，趁此机会\n',
            '好好休息一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360320313V#611F休息也是为了更好地工作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360320314V那么各位。\n',
            '祝你们休假愉快……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_133A(): pass

    label('loc_133A')

    OP_28(0x0079, 0x01, 0x2000)

    def _loc_1340(): pass

    label('loc_1340')

    Jump('loc_1635')

    def _loc_1343(): pass

    label('loc_1343')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034A, 2, 0x1A52)),
            Expr.Return,
        ),
        'loc_13A5',
    )

    ChrTalk(
        0x0008,
        (
            '#0360320285V#610F虽然时间短暂，\n',
            '请尽情放松。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360320286V休息也是为了更好地工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1635')

    def _loc_13A5(): pass

    label('loc_13A5')

    ChrTalk(
        0x0008,
        (
            '#0360320317V#610F哎呀，各位。\n',
            '这次真是辛苦了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360320318V那个金耀石结晶……\n',
            '我会小心使用的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360320319V#613F对了，关于票的事情\n',
            '已经听说了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320305V#1018F啊，嗯。\n',
            '就在刚才。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320306V难得市长一番好意，\n',
            '我们就打算恭敬不如从命了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360320322V#611F嗯嗯，请务必要去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360320308V虽然时间短暂，\n',
            '但请好好休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_153C',
    )

    ChrTalk(
        0x0103,
        (
            '#0030320324V#021F嗯嗯，就轻松一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15A5')

    def _loc_153C(): pass

    label('loc_153C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1570',
    )

    ChrTalk(
        0x0106,
        (
            '#0050320310V#051F啊啊，会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15A5')

    def _loc_1570(): pass

    label('loc_1570')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_15A5',
    )

    ChrTalk(
        0x0104,
        (
            '#0040320311V#031F呼，就这样定了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15A5(): pass

    label('loc_15A5')

    ChrTalk(
        0x0101,
        (
            '#0010320327V#1001F嗯，趁此机会\n',
            '好好休息一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360320328V#610F休息也是为了更好地工作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360320314V那么各位。\n',
            '祝你们休假愉快……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x034A, 2, 0x1A52))

    def _loc_1635(): pass

    label('loc_1635')

    Jump('loc_1BD6')

    def _loc_1638(): pass

    label('loc_1638')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_1703',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_16A1',
    )

    ChrTurnDirection(0x0008, 0x0000, 0)

    ChrTalk(
        0x0008,
        (
            '#0360310764V#611F多亏了各位\n',
            '把莉拉救出来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360310765V我衷心感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 45, 0)

    Jump('loc_1700')

    def _loc_16A1(): pass

    label('loc_16A1')

    ChrTurnDirection(0x0008, 0x0000, 0)

    ChrTalk(
        0x0008,
        (
            '#0360310766V#611F艾丝蒂尔，\n',
            '莉拉醒来了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360310767V太好了……真的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 45, 0)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_1700(): pass

    label('loc_1700')

    Jump('loc_1BD6')

    def _loc_1703(): pass

    label('loc_1703')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_18E7',
    )

    ChrSetSubChip(0x0008, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_176B',
    )

    ChrTalk(
        0x0008,
        (
            '#0360310768V#618F不得不做的\n',
            '工作堆积如山……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360310769V现在可不能泄气啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18E4')

    def _loc_176B(): pass

    label('loc_176B')

    ChrTalk(
        0x0008,
        (
            '#0360310770V#615F给避难目的地各店铺的邀请\n',
            '总算发完了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360310771V接下来是超市的受害调查\n',
            '和修复工程的计划还有材料的定购……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360310772V#618F还有送往拉文努村的\n',
            '物资也必须进行准备……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360310773V…………………………………\n',
            '…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#0360310774V#616F梅贝尔，振作点！\n',
            '工作还堆积如山呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360310775V身为市长的我\n',
            '要是泄气了城市可怎么办？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_18E4(): pass

    label('loc_18E4')

    Jump('loc_1BD6')

    def _loc_18E7(): pass

    label('loc_18E7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_1BD6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1961',
    )

    ChrTalk(
        0x0008,
        (
            '#0360310776V#610F交通安全的确保\n',
            '也是商业都市的重要工作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360310777V通缉魔兽的剿灭……\n',
            '就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BD6')

    def _loc_1961(): pass

    label('loc_1961')

    ChrTalk(
        0x0008,
        (
            '#0360310778V#610F哎呀，各位……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360310779V开门见山吧，有什么要事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310780V#1000F不，只是来\n',
            '报告一下状况。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310781V#1015F首先从通缉魔兽的剿灭任务开始，\n',
            '做帮忙的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050310782V#050F嗯，总之先做这个吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360310783V#617F哪里，这也是帮大忙了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360310784V最近实在很多，\n',
            '一直是让人头痛的原因之一呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310785V#1016F啊，果然\n',
            '市长也很困扰啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360310786V#615F嗯嗯，安全交通路线的确保\n',
            '对商业都市来说是生死存亡的问题……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360310787V#610F虽然或许这工作并不难，\n',
            '但解决了这些可是有很大益处的哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360310788V通缉魔兽的剿灭……\n',
            '就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310789V#1006F嗯，交给我们吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_1BD6(): pass

    label('loc_1BD6')

    ChrSetSubChip(0x0008, 0)
    TalkEnd(0x0008)

    Return()

# id: 0x0005 offset: 0x1BDF
@scena.Code('func_05_1BDF')
def func_05_1BDF():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1BEF',
    )

    Call(0, 0x0006)

    def _loc_1BEF(): pass

    label('loc_1BEF')

    Return()

# id: 0x0006 offset: 0x1BF0
@scena.Code('func_06_1BF0')
def func_06_1BF0():
    If(
        (
            (Expr.Eval, "OP_29(0x0079, 0x01, 0x0008)"),
            (Expr.Eval, "OP_29(0x0079, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0079, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1C10',
    )

    Call(1, 0x0002)

    Return()

    def _loc_1C10(): pass

    label('loc_1C10')

    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1CFB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1CBE',
    )

    ChrTalk(
        0x0009,
        (
            '#0370320388V#620F各位……\n',
            '前几天给你们添麻烦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370320389V现在梅贝尔小姐\n',
            '似乎忙得不可开交……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370320390V能帮助小姐的\n',
            '就只有你们了，拜托。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_1CF8')

    def _loc_1CBE(): pass

    label('loc_1CBE')

    ChrTalk(
        0x0009,
        (
            '#0370320391V#620F能帮助小姐的，\n',
            '就只有你们了，拜托。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1CF8(): pass

    label('loc_1CF8')

    Jump('loc_286A')

    def _loc_1CFB(): pass

    label('loc_1CFB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_237F',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0079, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_2119',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0079, 0x01, 0x4000)"),
            Expr.Return,
        ),
        'loc_1D73',
    )

    ChrTalk(
        0x0009,
        (
            '#0370320392V#620F各位现在\n',
            '要去湖畔的旅馆吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370320393V那么就请你们\n',
            '好好静养吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2116')

    def _loc_1D73(): pass

    label('loc_1D73')

    ChrTalk(
        0x0009,
        (
            '#0370320330V#620F哎呀，各位……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370320331V各位为我做这么多事\n',
            '真是给你们添麻烦了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320332V#1017F没什么麻烦的啦。\n',
            '能帮上忙真是太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320333V因为，就算没有血缘关系\n',
            '亲人就是亲人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320334V只要能确定这个，\n',
            '我就感觉受到了鼓舞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1EA8',
    )

    ChrTalk(
        0x0103,
        (
            '#0030320335V#020F艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F09')

    def _loc_1EA8(): pass

    label('loc_1EA8')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1ED8',
    )

    ChrTalk(
        0x0107,
        (
            '#0070320336V#060F姐姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F09')

    def _loc_1ED8(): pass

    label('loc_1ED8')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1F09',
    )

    ChrTalk(
        0x0105,
        (
            '#0060320337V#040F艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F09(): pass

    label('loc_1F09')

    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0009,
        (
            '#0370320338V#621F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370320339V你能这么说\n',
            '我也安心不少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320340V#1000F对了，莉拉\n',
            '打算几时回家乡？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0370320341V#620F日程还没定……\n',
            '要看小姐的计划了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370320342V因为小姐\n',
            '会一起去嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320343V#1018F啊，不错的主意嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0370320344V#623F嗯嗯，但是\n',
            '大概也不太可能吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370320345V小姐还是这么忙碌……\n',
            '时间估计空不出来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320346V#1016F啊，啊哈哈……的确是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0370320347V#620F嗯，虽然现在没办法\n',
            '但总有一天一定会回去的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370320348V在此之前慢慢\n',
            '等待机会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0079, 0x01, 0x4000)

    def _loc_2116(): pass

    label('loc_2116')

    Jump('loc_237C')

    def _loc_2119(): pass

    label('loc_2119')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_2194',
    )

    ChrTalk(
        0x0009,
        (
            '#0370320349V#620F这次你们又帮了小姐不少忙，\n',
            '实在是感激不尽。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370320350V那么，请在湖畔的旅店\n',
            '好好静养吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_237C')

    def _loc_2194(): pass

    label('loc_2194')

    ChrTalk(
        0x0009,
        (
            '#0370320351V#620F哎呀，各位是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370320352V这次你们又帮了小姐不少忙，\n',
            '实在是感激不尽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320353V#1007F嗯、嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320354V觉得这次莉拉\n',
            '才是最为辛苦的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320355V#1002F……身体没事了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0370320356V#620F请不必\n',
            '为莉拉担心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370320357V对了，听说各位现在\n',
            '要去湖畔的旅店……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370320358V从龙的骚动事件开始，\n',
            '这次似乎又有很多事情要忙呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370320359V#621F请趁此机会\n',
            '好好静养吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320360V#1016F唔、嗯，谢谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320361V不用客气好好享受哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_237C(): pass

    label('loc_237C')

    Jump('loc_286A')

    def _loc_237F(): pass

    label('loc_237F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_271C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034E, 5, 0x1A75)),
            Expr.Return,
        ),
        'loc_23E6',
    )

    ChrTalk(
        0x0009,
        (
            '#0370320362V#621F也给金先生和奥利维尔先生\n',
            '添麻烦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370320363V真是非常感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2719')

    def _loc_23E6(): pass

    label('loc_23E6')

    ChrTalk(
        0x0009,
        (
            '#0370320364V#627F艾丝蒂尔小姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320365V#1004F莉拉，没事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0370320366V#620F是……让各位\n',
            '担心了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370320367V#627F……真是抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320368V#1001F说什么呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320369V莉拉拼命\n',
            '保护了梅贝尔市长。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320370V#1009F错的都是\n',
            '那头龙和银发男子啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2534',
    )

    ChrTalk(
        0x0108,
        (
            '#0080320371V#070F呼，无需自责。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25AD')

    def _loc_2534(): pass

    label('loc_2534')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2575',
    )

    ChrTalk(
        0x0104,
        (
            '#0040320372V#030F呼，小姐没必要\n',
            '责怪自己。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25AD')

    def _loc_2575(): pass

    label('loc_2575')

    ChrTalk(
        0x0106,
        (
            '#0050320373V#053F艾丝蒂尔说得对。\n',
            '没必要责怪自己。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_25AD(): pass

    label('loc_25AD')

    ChrTalk(
        0x0009,
        (
            '#0370320374V#621F……我听小姐说了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370320375V也给金先生和奥利维尔先生\n',
            '添麻烦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370320363V真是非常感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2692',
    )

    ChrTalk(
        0x0108,
        (
            '#0080320377V#070F哪里，区区小事不值得道谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080320378V反倒是我们\n',
            '被你的行为所感动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2716')

    def _loc_2692(): pass

    label('loc_2692')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_26E1',
    )

    ChrTalk(
        0x0104,
        (
            '#0040320379V#031F哪里，能救到小姐，\n',
            '可以说是我的荣幸呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2716')

    def _loc_26E1(): pass

    label('loc_26E1')

    ChrTalk(
        0x0101,
        (
            '#0010320380V#1001F嗯，我一定会\n',
            '传达给他们俩的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2716(): pass

    label('loc_2716')

    SetScenaFlags(ScenaFlag(0x034E, 5, 0x1A75))

    def _loc_2719(): pass

    label('loc_2719')

    Jump('loc_286A')

    def _loc_271C(): pass

    label('loc_271C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_2751',
    )

    ChrTalk(
        0x0009,
        (
            '#0370320381V#620F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_286A')

    def _loc_2751(): pass

    label('loc_2751')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_2786',
    )

    ChrTalk(
        0x0009,
        (
            '#0370320382V#620F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_286A')

    def _loc_2786(): pass

    label('loc_2786')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_286A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_27EC',
    )

    ChrTalk(
        0x0009,
        (
            '#0370320383V#620F小姐正在２楼的书房\n',
            '办公。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370320384V有事的话请去那找她吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CloseMessageWindow()

    Jump('loc_286A')

    def _loc_27EC(): pass

    label('loc_27EC')

    ChrTalk(
        0x0009,
        (
            '#0370320385V#620F哎呀，各位游击士。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370320386V小姐在２楼的书房\n',
            '办公。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370320387V有什么事情的话\n',
            '请到那去找她吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_286A(): pass

    label('loc_286A')

    TalkEnd(0x0009)

    Return()

# id: 0x0007 offset: 0x286E
@scena.Code('func_07_286E')
def func_07_286E():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_290D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_28D2',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，欢迎各位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '小姐和莉拉\n',
            '出门去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我想一定是\n',
            '去做礼拜了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_290A')

    def _loc_28D2(): pass

    label('loc_28D2')

    ChrTalk(
        0x00FE,
        (
            '小姐和莉拉\n',
            '出门去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我想一定是\n',
            '去做礼拜了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_290A(): pass

    label('loc_290A')

    Jump('loc_2D41')

    def _loc_290D(): pass

    label('loc_290D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2A06',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_29CE',
    )

    ChrTalk(
        0x00FE,
        (
            '晚上的骚乱真恐怖～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好多人\n',
            '涌来屋子这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在还觉得好像会有人要冲进来似的，\n',
            '每个人都一脸怒气冲冲的凶像呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，能把这些人\n',
            '都说服，\n',
            '真不愧是小姐呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_2A03')

    def _loc_29CE(): pass

    label('loc_29CE')

    ChrTalk(
        0x00FE,
        (
            '骚乱的时候好恐怖呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好多人\n',
            '涌来屋子这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A03(): pass

    label('loc_2A03')

    Jump('loc_2D41')

    def _loc_2A06(): pass

    label('loc_2A06')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_2AFE',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0079, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_2ABA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_2A5D',
    )

    ChrTalk(
        0x00FE,
        (
            '莉拉的话\n',
            '不可能有人说坏话的～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯～真有点\n',
            '在意呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2AB7')

    def _loc_2A5D(): pass

    label('loc_2A5D')

    ChrTalk(
        0x00FE,
        (
            '刚才找莉拉\n',
            '有什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '莉拉的话\n',
            '不可能有人说坏话的～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯～真有点\n',
            '在意呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_2AB7(): pass

    label('loc_2AB7')

    Jump('loc_2AFB')

    def _loc_2ABA(): pass

    label('loc_2ABA')

    ChrTalk(
        0x00FE,
        (
            '超市也重新开门了，\n',
            '小姐还有得忙呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，市长可真辛苦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_2AFB(): pass

    label('loc_2AFB')

    Jump('loc_2D41')

    def _loc_2AFE(): pass

    label('loc_2AFE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_2BD6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_2B49',
    )

    ChrTalk(
        0x00FE,
        (
            '莉拉终于\n',
            '醒过来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼～太好了。\n',
            '这下就放心了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2BD3')

    def _loc_2B49(): pass

    label('loc_2B49')

    ChrTalk(
        0x00FE,
        (
            '啊，各位！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '莉拉终于\n',
            '醒过来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '莉拉刚醒来就开始工作，\n',
            '惹得修女都生气了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过还真是莉拉的风格。\n',
            '感觉就是工作狂～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_2BD3(): pass

    label('loc_2BD3')

    Jump('loc_2D41')

    def _loc_2BD6(): pass

    label('loc_2BD6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_2C69',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_2C16',
    )

    ChrTalk(
        0x00FE,
        (
            '没，没有莉拉、\n',
            '连晚饭的菜单也定不下来啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C66')

    def _loc_2C16(): pass

    label('loc_2C16')

    ChrTalk(
        0x00FE,
        (
            '没，没有莉拉、\n',
            '连晚饭的菜单也定不下来啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '拜，拜托你一定要醒过来～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_2C66(): pass

    label('loc_2C66')

    Jump('loc_2D41')

    def _loc_2C69(): pass

    label('loc_2C69')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_2D41',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_2CB8',
    )

    ChrTalk(
        0x00FE,
        (
            '好了，差不多该\n',
            '准备茶点了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '小姐不休息一下\n',
            '可不行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D41')

    def _loc_2CB8(): pass

    label('loc_2CB8')

    ChrTalk(
        0x00FE,
        (
            '好了，差不多该\n',
            '准备茶点了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '小姐不休息一下\n',
            '可不行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '小姐经常会\n',
            '工作到废寝忘食～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以要送些茶点，\n',
            '逼着她休息一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_2D41(): pass

    label('loc_2D41')

    TalkEnd(0x000B)

    Return()

# id: 0x0008 offset: 0x2D45
@scena.Code('func_08_2D45')
def func_08_2D45():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_2DD8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_2D8B',
    )

    ChrTalk(
        0x00FE,
        (
            '莉拉才刚刚\n',
            '醒过来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还不方便\n',
            '行动呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2DD5')

    def _loc_2D8B(): pass

    label('loc_2D8B')

    ChrTalk(
        0x00FE,
        (
            '莉拉才刚刚\n',
            '醒过来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就开始\n',
            '工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还不方便\n',
            '行动呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_2DD5(): pass

    label('loc_2DD5')

    Jump('loc_2EFD')

    def _loc_2DD8(): pass

    label('loc_2DD8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_2EAA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_2E35',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然状态是稳定了……\n',
            '但意识还没恢复。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '教区长给的药\n',
            '还没有效果……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2EA7')

    def _loc_2E35(): pass

    label('loc_2E35')

    ChrTalk(
        0x00FE,
        (
            '虽然状态是稳定了……\n',
            '但意识还没恢复。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '教区长给的药\n',
            '还没有效果……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……接下来只有\n',
            '向女神祈祷了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_2EA7(): pass

    label('loc_2EA7')

    Jump('loc_2EFD')

    def _loc_2EAA(): pass

    label('loc_2EAA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_2EFD',
    )

    ChrTalk(
        0x00FE,
        (
            '莉拉的意识\n',
            '还没有回复……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然性命保住了，\n',
            '但也只能再继续观察了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2EFD(): pass

    label('loc_2EFD')

    TalkEnd(0x000A)

    Return()

# id: 0x0009 offset: 0x2F01
@scena.Code('func_09_2F01')
def func_09_2F01():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_2F0D',
    )

    Call(1, 0x0004)

    Return()

    def _loc_2F0D(): pass

    label('loc_2F0D')

    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_2FE9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2F9C',
    )

    ChrTalk(
        0x00FE,
        (
            '超市也恢复\n',
            '往日的热闹了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '之后要是导力器能复原\n',
            '就万事大吉了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从各方的说法看来，\n',
            '这才是最大的难题呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Jump('loc_2FE6')

    def _loc_2F9C(): pass

    label('loc_2F9C')

    ChrTalk(
        0x00FE,
        (
            '城市里也恢复\n',
            '往日的热闹了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '小姐连日连夜的努力\n',
            '终于也有了回报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2FE6(): pass

    label('loc_2FE6')

    Jump('loc_34E8')

    def _loc_2FE9(): pass

    label('loc_2FE9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_30AE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3065',
    )

    ChrTalk(
        0x00FE,
        (
            '噢，这不是\n',
            '各位游击士吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在，柏斯正在遭遇\n',
            '不得了的危机。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了小姐\n',
            '请务必伸出援手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Jump('loc_30AB')

    def _loc_3065(): pass

    label('loc_3065')

    ChrTalk(
        0x00FE,
        (
            '现在，柏斯正在遭遇\n',
            '不得了的危机。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了小姐\n',
            '请务必伸出援手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_30AB(): pass

    label('loc_30AB')

    Jump('loc_34E8')

    def _loc_30AE(): pass

    label('loc_30AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_318C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_311B',
    )

    ChrTalk(
        0x00FE,
        (
            '多亏各位的帮忙\n',
            '终于恢复了和平。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是，小姐\n',
            '还是忙得不可开交。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这也是天性吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3189')

    def _loc_311B(): pass

    label('loc_311B')

    ChrTalk(
        0x00FE,
        (
            '多亏各位的帮忙\n',
            '终于恢复了和平。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要说还有什么担心的，\n',
            '也就是小姐的身体了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我会妥善\n',
            '管理的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_3189(): pass

    label('loc_3189')

    Jump('loc_34E8')

    def _loc_318C(): pass

    label('loc_318C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_326B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_3200',
    )

    ChrTalk(
        0x00FE,
        (
            '女佣莉拉\n',
            '终于恢复意识了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '忙于公务的小姐\n',
            '也很担心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呀，主从二人\n',
            '心情都变开朗了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3268')

    def _loc_3200(): pass

    label('loc_3200')

    ChrTalk(
        0x00FE,
        (
            '女佣莉拉\n',
            '终于恢复意识了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '万一无法恢复……\n',
            '虽然这样担心过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呀，总算\n',
            '心情都变开朗了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_3268(): pass

    label('loc_3268')

    Jump('loc_34E8')

    def _loc_326B(): pass

    label('loc_326B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_32E3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_32DC',
    )

    ChrTalk(
        0x00FE,
        (
            '那盏吊灯\n',
            '也是逃过战火的东西之一。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不知道是不是因为这样的过去，\n',
            '前市长也经常注视着它。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_32E0')

    def _loc_32DC(): pass

    label('loc_32DC')

    Call(0, 0x000B)

    def _loc_32E0(): pass

    label('loc_32E0')

    Jump('loc_34E8')

    def _loc_32E3(): pass

    label('loc_32E3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_340E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_3332',
    )

    ChrTalk(
        0x00FE,
        (
            '避难而来的人\n',
            '也是我家的客人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好好招待\n',
            '是当然的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_340B')

    def _loc_3332(): pass

    label('loc_3332')

    ChrTalk(
        0x00FE,
        (
            '避难而来的人\n',
            '也是我家的客人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好好招待\n',
            '是当然的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '１０年前的战役中，\n',
            '好象也给避难的市民\n',
            '分发了茶点哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '无论是怎样的非常时刻\n',
            '都不能丧失平常的从容。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正因为这样的心态\n',
            '才引导了柏斯的复兴吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_340B(): pass

    label('loc_340B')

    Jump('loc_34E8')

    def _loc_340E(): pass

    label('loc_340E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_34E8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_3467',
    )

    ChrTalk(
        0x00FE,
        (
            '市长现在在２楼\n',
            '办公。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在小姐也正如往常一样\n',
            '忙着处理公务呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_34E8')

    def _loc_3467(): pass

    label('loc_3467')

    ChrTalk(
        0x00FE,
        (
            '各位不是……\n',
            '欢迎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '前阵子\n',
            '真是承蒙照顾了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '市长现在在２楼\n',
            '办公。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在小姐也如往常一样\n',
            '正忙着处理公务呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_34E8(): pass

    label('loc_34E8')

    TalkEnd(0x000C)

    Return()

# id: 0x000A offset: 0x34EC
@scena.Code('func_0A_34EC')
def func_0A_34EC():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_359F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_3537',
    )

    ChrTalk(
        0x00FE,
        (
            '那盏吊灯\n',
            '一定相当有名。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不愧是柏斯的名家啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_359C')

    def _loc_3537(): pass

    label('loc_3537')

    ChrTalk(
        0x00FE,
        (
            '昨天瞄了一眼，\n',
            '觉得有点在意……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔唔，那盏吊灯\n',
            '一定相当有名。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不愧是柏斯的名家啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_359C(): pass

    label('loc_359C')

    Jump('loc_371F')

    def _loc_359F(): pass

    label('loc_359F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_3623',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_361C',
    )

    ChrTalk(
        0x00FE,
        (
            '唔，原来如此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '果然出色的文物，\n',
            '必然有很深的渊源啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '解开这些谜团\n',
            '也可说是古董的乐趣所在呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3620')

    def _loc_361C(): pass

    label('loc_361C')

    Call(0, 0x000B)

    def _loc_3620(): pass

    label('loc_3620')

    Jump('loc_371F')

    def _loc_3623(): pass

    label('loc_3623')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_371F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_3686',
    )

    ChrTalk(
        0x00FE,
        (
            '我们没礼貌的闯进来，\n',
            '竟然还招待茶点……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这种时候\n',
            '温暖的人情真令人感动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_371F')

    def _loc_3686(): pass

    label('loc_3686')

    ChrTalk(
        0x00FE,
        (
            '虽然贸然\n',
            '逃进这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们没礼貌的闯进来，\n',
            '管家还拿出茶点来招待我们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这茶杯\n',
            '也是精美的古董啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '太感动了……\n',
            '都忍不住热泪盈眶了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_371F(): pass

    label('loc_371F')

    TalkEnd(0x000D)

    Return()

# id: 0x000B offset: 0x3723
@scena.Code('func_0B_3723')
def func_0B_3723():
    OP_4A(0x000D, 255)
    OP_4A(0x000C, 255)

    ChrTalk(
        0x000D,
        (
            '唔，原来如此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '原本是帝国制的\n',
            '吊灯吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '之后才装入导力器\n',
            '的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '是的，正是如此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '算是上代市长\n',
            '留下来的上等品之一吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x000D, 255)
    OP_4B(0x000C, 255)
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    ChrClearFlags(0x000D, 0x0010)
    ChrClearFlags(0x000C, 0x0010)

    Return()

# id: 0x000C offset: 0x37D1
@scena.Code('func_0C_37D1')
def func_0C_37D1():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_391B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_3870',
    )

    ChrTalk(
        0x000E,
        (
            '胡乱冲进去的地方\n',
            '没想到竟是市长的宅邸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '不过，真不愧是市长官邸。\n',
            '好气派的房子啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '可以的话真希望\n',
            '能在和平的时候来拜访啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_391B')

    def _loc_3870(): pass

    label('loc_3870')

    ChrTalk(
        0x000E,
        (
            '唉，总算\n',
            '逃过一劫……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '话虽如此……\n',
            '胡乱冲进去的地方 \n',
            '竟是市长的宅邸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '真不愧是市长官邸。\n',
            '好气派的房子啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '可以的话真希望\n',
            '能在和平的时候来拜访啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    def _loc_391B(): pass

    label('loc_391B')

    TalkEnd(0x000E)

    Return()

# id: 0x000D offset: 0x391F
@scena.Code('func_0D_391F')
def func_0D_391F():
    EventBegin(0x00)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    ChrSetFlags(0x0004, 0x0080)
    ChrSetFlags(0x0005, 0x0080)
    ChrSetFlags(0x0006, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    CameraMove(-120360, 0, -6050, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    ChrSetPos(0x0008, -117150, 0, -1280, 90)
    ChrSetPos(0x0009, -115400, 0, -1540, 180)
    ChrSetPos(0x000A, -117100, 0, -2170, 90)
    ChrSetChipByIndex(0x0008, 0)
    CreateThread(0x0008, 0x00, 0x00, func_02_4A3)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    OP_4A(0x0009, 255)
    ChrSetFlags(0x0009, 0x0004)
    ChrSetChipByIndex(0x0009, 8)
    ChrSetSubChip(0x0009, 0)
    OP_6F(0x000D, 15)

    @scena.Lambda('lambda_39F4')
    def lambda_39F4():
        CameraMove(-116590, 0, -790, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_39F4)

    FadeIn(2000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    FadeOut(1500, 0, -1)
    OP_0D()
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    NewScene('ED6_DT21/T1121._SN', 100, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

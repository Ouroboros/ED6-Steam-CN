import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2512_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2512   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2512.x'
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
        ('ED6_DT07/CH02390._CH', 'ED6_DT07/CH02390P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
        ('ED6_DT07/CH01590._CH', 'ED6_DT07/CH01590P._CP'),
        ('ED6_DT07/CH01090._CH', 'ED6_DT07/CH01090P._CP'),
        ('ED6_DT07/CH01580._CH', 'ED6_DT07/CH01580P._CP'),
        ('ED6_DT07/CH01360._CH', 'ED6_DT07/CH01360P._CP'),
        ('ED6_DT07/CH01370._CH', 'ED6_DT07/CH01370P._CP'),
        ('ED6_DT06/CH20100._CH', 'ED6_DT06/CH20100P._CP'),
        ('ED6_DT06/CH20109._CH', 'ED6_DT06/CH20109P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
    ]

# id: 0x10001 offset: 0x102
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '乔儿',
            x                   = 59640,
            z                   = 1000,
            y                   = 13450,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '碧欧拉老师',
            x                   = 87700,
            z                   = 0,
            y                   = 2800,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '艾福托老师',
            x                   = 84400,
            z                   = 0,
            y                   = 2800,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '雅莉丝',
            x                   = -60350,
            z                   = 0,
            y                   = 30800,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '帕布尔',
            x                   = -60450,
            z                   = 0,
            y                   = 30850,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '亚吉鲁',
            x                   = -28710,
            z                   = 0,
            y                   = 25280,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '德尼斯',
            x                   = -31400,
            z                   = 0,
            y                   = -800,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '芙拉瑟',
            x                   = -63000,
            z                   = 0,
            y                   = -3700,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '蕾娜',
            x                   = -61500,
            z                   = 0,
            y                   = -3700,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = 'CH22000',
            x                   = -28640,
            z                   = 700,
            y                   = 31090,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1835018,
            chipIndex           = 10,
            npcIndex            = 0x0166,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x242
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x242
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x242
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -28640,
            triggerZ            = 700,
            triggerY            = 31090,
            triggerRange        = 1000,
            actorX              = -28640,
            actorZ              = 1000,
            actorY              = 31090,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000D,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x266
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_2AB',
    )

    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, -58560, 0, -1150, 90)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, -60740, 0, 750, 180)

    Jump('loc_380')

    def _loc_2AB(): pass

    label('loc_2AB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_2B5',
    )

    Jump('loc_380')

    def _loc_2B5(): pass

    label('loc_2B5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_2BF',
    )

    Jump('loc_380')

    def _loc_2BF(): pass

    label('loc_2BF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_2C9',
    )

    Jump('loc_380')

    def _loc_2C9(): pass

    label('loc_2C9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_322',
    )

    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, -119550, 0, 30420, 0)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 29320, 0, 27850, 270)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetFlags(0x000F, 0x0010)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetFlags(0x0010, 0x0010)

    Jump('loc_380')

    def _loc_322(): pass

    label('loc_322')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_351',
    )

    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 29790, 0, 30750, 0)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)

    Jump('loc_380')

    def _loc_351(): pass

    label('loc_351')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 6, 0x42E)),
            Expr.Return,
        ),
        'loc_35B',
    )

    Jump('loc_380')

    def _loc_35B(): pass

    label('loc_35B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_365',
    )

    Jump('loc_380')

    def _loc_365(): pass

    label('loc_365')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 6, 0x41E)),
            Expr.Return,
        ),
        'loc_374',
    )

    ChrClearFlags(0x000C, 0x0080)

    Jump('loc_380')

    def _loc_374(): pass

    label('loc_374')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_380',
    )

    ChrClearFlags(0x000C, 0x0080)

    def _loc_380(): pass

    label('loc_380')

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0100)"),
            Expr.Return,
        ),
        'loc_390',
    )

    ChrSetFlags(0x0011, 0x0080)

    def _loc_390(): pass

    label('loc_390')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_3B0',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_0B_12D6)
    OP_B1('T2512_k')

    def _loc_3B0(): pass

    label('loc_3B0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_3D5',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0xE),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x10000000)
    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, func_0C_24E9)
    OP_B1('t2512_n')

    def _loc_3D5(): pass

    label('loc_3D5')

    Return()

# id: 0x0001 offset: 0x3D6
@scena.Code('func_01_3D6')
def func_01_3D6():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Or,
            Expr.Return,
        ),
        'loc_3F7',
    )

    OP_B1('t2512_y')

    Jump('loc_400')

    def _loc_3F7(): pass

    label('loc_3F7')

    OP_B1('t2512_n')

    def _loc_400(): pass

    label('loc_400')

    OP_64(0x00, 0x0001)

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0020)"),
            Expr.Return,
        ),
        'loc_413',
    )

    OP_65(0x00, 0x0001)

    def _loc_413(): pass

    label('loc_413')

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0100)"),
            Expr.Return,
        ),
        'loc_422',
    )

    OP_64(0x00, 0x0001)

    def _loc_422(): pass

    label('loc_422')

    Return()

# id: 0x0002 offset: 0x423
@scena.Code('func_02_423')
def func_02_423():
    ExecExpressionWithReg(
        0x0000,
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
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_448',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_58A')

    def _loc_448(): pass

    label('loc_448')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_461',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_58A')

    def _loc_461(): pass

    label('loc_461')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_47A',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_58A')

    def _loc_47A(): pass

    label('loc_47A')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_493',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_58A')

    def _loc_493(): pass

    label('loc_493')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4AC',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_58A')

    def _loc_4AC(): pass

    label('loc_4AC')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4C5',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_58A')

    def _loc_4C5(): pass

    label('loc_4C5')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4DE',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_58A')

    def _loc_4DE(): pass

    label('loc_4DE')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4F7',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_58A')

    def _loc_4F7(): pass

    label('loc_4F7')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_510',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_58A')

    def _loc_510(): pass

    label('loc_510')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_529',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_58A')

    def _loc_529(): pass

    label('loc_529')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_542',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_58A')

    def _loc_542(): pass

    label('loc_542')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_55B',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_58A')

    def _loc_55B(): pass

    label('loc_55B')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_574',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_58A')

    def _loc_574(): pass

    label('loc_574')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_58A',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_58A(): pass

    label('loc_58A')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_59F',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_58A')

    def _loc_59F(): pass

    label('loc_59F')

    Return()

# id: 0x0003 offset: 0x5A0
@scena.Code('func_03_5A0')
def func_03_5A0():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_601',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '哎呀，\n',
            '难道大家都还在练习吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '差不多该回房间休息，\n',
            '为明天做准备了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_64E')

    def _loc_601(): pass

    label('loc_601')

    ChrTalk(
        0x00FE,
        (
            '难道他们\n',
            '还留在校园里吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '还有一些同学\n',
            '没回宿舍去呢………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_64E(): pass

    label('loc_64E')

    TalkEnd(0x0009)

    Return()

# id: 0x0004 offset: 0x652
@scena.Code('func_04_652')
def func_04_652():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_7B0',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_707',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6B8',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '哦，刚才辛苦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在事态扩大之前解决了，\n',
            '实在太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_704')

    def _loc_6B8(): pass

    label('loc_6B8')

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '真拿米克那家伙没办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，在下次体育课上\n',
            '我要好好锻炼他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_704(): pass

    label('loc_704')

    Jump('loc_7AD')

    def _loc_707(): pass

    label('loc_707')

    ChrTalk(
        0x00FE,
        (
            '刚才有个学生\n',
            '说要找大道具的材料，\n',
            '来借走了旧校舍的钥匙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '已经有段时间了，\n',
            '怎么还没回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没回房间的住宿生还有很多，\n',
            '在宿舍关门之前还是去巡视一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_7AD(): pass

    label('loc_7AD')

    Jump('loc_803')

    def _loc_7B0(): pass

    label('loc_7B0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_803',
    )

    ChrTalk(
        0x00FE,
        (
            '学院的宿舍\n',
            '都是由老师担当宿管的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '咳咳！\n',
            '男生宿舍的宿管就是我了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_803(): pass

    label('loc_803')

    TalkEnd(0x000A)

    Return()

# id: 0x0005 offset: 0x807
@scena.Code('func_05_807')
def func_05_807():
    TalkBegin(0x000B)

    ChrTalk(
        0x00FE,
        (
            '呼～\n',
            '今天一天又要结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '接下来做什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000B)

    Return()

# id: 0x0006 offset: 0x843
@scena.Code('func_06_843')
def func_06_843():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_8DB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8A5',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '啊，科洛丝前辈，还有艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明天的舞台剧，你们要好好加油啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8D8')

    def _loc_8A5(): pass

    label('loc_8A5')

    ChrTalk(
        0x00FE,
        (
            '我很喜欢历史，\n',
            '而且对戏剧的背景设定很有兴趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8D8(): pass

    label('loc_8D8')

    Jump('loc_93A')

    def _loc_8DB(): pass

    label('loc_8DB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_93A',
    )

    ChrTalk(
        0x00FE,
        (
            '今天刚买的小说，\n',
            '一定要好好读一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我的理想是做个小说家，\n',
            '所以选择了人文系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_93A(): pass

    label('loc_93A')

    TalkEnd(0x000C)

    Return()

# id: 0x0007 offset: 0x93E
@scena.Code('func_07_93E')
def func_07_93E():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_A12',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9F2',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '呼呼，\n',
            '快点到晚上吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我偏好安静，\n',
            '所以特别喜欢黑暗的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '洗澡时我也喜欢\n',
            '漆黑一片的浴室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为让我感到很安静。\n',
            '有机会你们也试试吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A0F')

    def _loc_9F2(): pass

    label('loc_9F2')

    ChrTalk(
        0x00FE,
        (
            '呼呼，\n',
            '快点到晚上吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A0F(): pass

    label('loc_A0F')

    Jump('loc_B9F')

    def _loc_A12(): pass

    label('loc_A12')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_B5D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B12',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '呼呼呼……\n',
            '天马上就要黑了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们知道吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从这里向北走\n',
            '有一间学院的旧校舍。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '旧校舍是用以前的要塞改建的，\n',
            '原来好像是个战场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……你不觉得\n',
            '那里也许会出现鬼怪吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#506F………是吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B5A')

    def _loc_B12(): pass

    label('loc_B12')

    ChrTalk(
        0x00FE,
        (
            '旧校舍是用\n',
            '以前的要塞改建的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你不觉得\n',
            '那里也许会出现鬼怪吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B5A(): pass

    label('loc_B5A')

    Jump('loc_B9F')

    def _loc_B5D(): pass

    label('loc_B5D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_B9F',
    )

    ChrTalk(
        0x00FE,
        (
            '学园祭快要到了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '必须要开始准备\n',
            '社团的摊位了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B9F(): pass

    label('loc_B9F')

    TalkEnd(0x000D)

    Return()

# id: 0x0008 offset: 0xBA3
@scena.Code('func_08_BA3')
def func_08_BA3():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_C0A',
    )

    ChrTalk(
        0x00FE,
        (
            '照我的经验来看，\n',
            '复习比预习更有效果。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '复习三小时，\n',
            '预习两小时是我每天的必修课。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CCB')

    def _loc_C0A(): pass

    label('loc_C0A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_C68',
    )

    ChrTalk(
        0x00FE,
        (
            '好了，\n',
            '我差不多该去休息了哦㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '糟、糟了……\n',
            '不知不觉就用上演戏的语气了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CCB')

    def _loc_C68(): pass

    label('loc_C68')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_CCB',
    )

    ChrTalk(
        0x00FE,
        (
            '我一直专心于学习，\n',
            '舞台剧方面都没怎么排练。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼～而且我还是演员，\n',
            '不会出洋相吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CCB(): pass

    label('loc_CCB')

    TalkEnd(0x000E)

    Return()

# id: 0x0009 offset: 0xCCF
@scena.Code('func_09_CCF')
def func_09_CCF():
    TalkBegin(0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_D7A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D40',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '现在开始是美术部的活动时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我正要回宿舍\n',
            '去拿道具。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……这可不能忘了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D77')

    def _loc_D40(): pass

    label('loc_D40')

    ChrTalk(
        0x00FE,
        (
            '我正要回宿舍\n',
            '去拿道具。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……这可不能忘了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D77(): pass

    label('loc_D77')

    Jump('loc_FB4')

    def _loc_D7A(): pass

    label('loc_D7A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_FB4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F8D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))
    OP_4A(0x0010, 255)

    ChrTalk(
        0x000F,
        (
            '呼，\n',
            '果然是激动人心的一周啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '戏剧的练习，美术社团的摊位准备，\n',
            '还有帮忙班级展示………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '全部都处理完了呀，\n',
            '哇，好棒，很厉害嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000F, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000F,
        (
            '……这还不都是\n',
            '被你逼着做的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '舞台剧方面\n',
            '我本来还想拒绝的呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '可是，\n',
            '是你自己抢下主教这个角色的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000F, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000F,
        (
            '这是当然的啦！\n',
            '难道让我演一般平民？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '要干就要好好干。\n',
            '可惜主角已经有人选了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '哇哇，真是伟大。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000F, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000F,
        (
            '……真是的，\n',
            '蕾娜老是这样为难我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x000F, 0x0010)
    ChrClearFlags(0x0010, 0x0010)
    OP_4B(0x0010, 255)

    Jump('loc_FB4')

    def _loc_F8D(): pass

    label('loc_F8D')

    ChrTalk(
        0x00FE,
        (
            '……真是的，\n',
            '蕾娜老是这样为难我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FB4(): pass

    label('loc_FB4')

    TalkEnd(0x000F)

    Return()

# id: 0x000A offset: 0xFB8
@scena.Code('func_0A_FB8')
def func_0A_FB8():
    TalkBegin(0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_1092',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_106C',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))
    OP_4A(0x000F, 255)

    ChrTalk(
        0x0010,
        (
            '嗯，只要是人，\n',
            '总会有忘记的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000F, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_101A')
    def lambda_101A():
        ChrTurnDirection(0x000F, 0x0010, 1500)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_101A)

    ChrTalk(
        0x000F,
        (
            '哎呀！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x000F, 500)

    ChrTalk(
        0x0010,
        (
            '呼，不快点的话\n',
            '活动时间就要结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4A(0x000F, 255)
    ChrSetDirection(0x000F, 90, 6000)

    Jump('loc_108F')

    def _loc_106C(): pass

    label('loc_106C')

    ChrTalk(
        0x00FE,
        (
            '只要是人，\n',
            '总会有忘记的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_108F(): pass

    label('loc_108F')

    Jump('loc_12D2')

    def _loc_1092(): pass

    label('loc_1092')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_12D2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_12AB',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))
    OP_4A(0x000F, 255)

    ChrTalk(
        0x000F,
        (
            '呼，\n',
            '果然是激动人心的一周啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '戏剧的练习，美术社团的摊位准备，\n',
            '还有帮忙班级展示………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '全部都处理完了呀，\n',
            '哇，好棒，很厉害嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000F, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000F,
        (
            '……这还不都是\n',
            '被你逼着做的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '舞台剧方面\n',
            '我本来还想拒绝的呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '演出不是更好吗，\n',
            '你自己抢下主教这个角色的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000F, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000F,
        (
            '这是当然的啦！\n',
            '难道让我演一般平民？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '要干就要好好干。\n',
            '可惜主角已经有人选了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '哇哇，不错不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000F, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000F,
        (
            '……真是的，\n',
            '蕾娜老是这样为难我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x000F, 255)
    ChrClearFlags(0x000F, 0x0010)
    ChrClearFlags(0x0010, 0x0010)

    Jump('loc_12D2')

    def _loc_12AB(): pass

    label('loc_12AB')

    ChrTalk(
        0x00FE,
        (
            '看着芙拉瑟的成长\n',
            '是我的一种乐趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12D2(): pass

    label('loc_12D2')

    TalkEnd(0x0010)

    Return()

# id: 0x000B offset: 0x12D6
@scena.Code('func_0B_12D6')
def func_0B_12D6():
    EventBegin(0x00)
    MapClearFlags(0x00000001)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    CameraMove(-120390, 0, -2060, 0)
    OP_67(0, 5400, -10000, 0)
    CameraSetDistance(3040, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, -121640, 0, -4360, 0)
    ChrSetPos(0x0105, -122120, 0, -3050, 180)
    ChrSetPos(0x0008, -121110, 0, -2820, 180)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0105,
        (
            '#0060051188V#040F#3P……那么，艾丝蒂尔。\n',
            '这段时间你就睡这张床吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051189V#001F谢啦⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051190V#501F不过，原来科洛丝和\n',
            '乔儿会长是住同一房间的啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051191V难怪关系这么好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051192V#041F#3P呵呵……\n',
            '自从来了学院之后，我们就是朋友了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510051193V#641F#1P不过呢，作为室友来说，\n',
            '我们恐怕算是一对冤家哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051194V#644F对了，艾丝蒂尔。\n',
            '我这里有一个提议……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051195V#004F什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510051196V#648F#1P你呢，以后直接\n',
            '叫我乔儿就可以了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051197V加上『会长』的话，\n',
            '听起来总觉得好见外～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051198V我也直接叫你艾丝蒂尔，\n',
            '以后大家就是好朋友哦㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051199V#001F啊哈哈……\n',
            '嗯，那我们以后就是好朋友啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051200V#040F#3P我觉得这提议也不错，\n',
            '大家以后就互相直呼名字吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051201V那样感觉比较自然……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051202V#006F是吗，那我就不客气了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051203V#001F乔儿，科洛丝。\n',
            '这段时间就请你们多多关照啦⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051204V#048F#3P嗯，也请你多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510051205V#641F#1P反正这里全是女生，\n',
            '我们就过得随意一点行了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051206V只要是在这幢楼里，\n',
            '就不用担心会被男生看到哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0008, 400)

    ChrTalk(
        0x0105,
        (
            '#0060051207V#045F虽然话是这么说，\n',
            '不过太随意的话也不太好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0105, 400)

    ChrTalk(
        0x0008,
        (
            '#0510051208V#645F#1P哎～所以我就说，\n',
            '好孩子是最麻烦的了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051209V成天在装正经。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051210V#042F啊，你好过分呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051211V会说这种话的孩子，\n',
            '我就算做了糕点也不会分给她。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510051212V#643F#1P啊，不要啊不要啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051213V科洛丝大人。\n',
            '请饶恕在下刚才的无礼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051214V#041F不～行，要好好反省。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051215V#501F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060051216V#044F#3P哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#0510051217V#640F#1P怎么了，艾丝蒂尔？\n',
            '这样呆呆地盯着我们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051218V#008F啊哈哈，没什么～……\n',
            '其实我挺羡慕你们呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510051219V#643F#1P羡慕？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051220V#000F我在洛连特\n',
            '虽然也有很要好的朋友……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051221V不过顶多也就是\n',
            '到对方的家里过过夜罢了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051222V#001F像你们这样，可以和\n',
            '意气相投的朋友一起生活真好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0105, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    OP_63(0x0008)
    OP_63(0x0105)

    ChrTalk(
        0x0008,
        (
            '#0510051223V#642F#1P……科洛丝，你怎么想？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051224V#045F#3P要我该怎么说好呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051225V被艾丝蒂尔羡慕，\n',
            '我觉得有点不能理解啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051226V#501F哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510051227V#646F#1P啊，果然是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051228V你知道自己在说什么吗。\n',
            '我都不明白你要羡慕些什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051229V#004F为、为什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510051230V#645F#1P我说你啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051231V你知道自己\n',
            '是在跟谁一起旅行吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051232V在家里的时候，\n',
            '是在跟谁住在同一屋檐下？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051233V#004F哎？……这个。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051234V难道是在说约修亚？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051235V#045F#3P用不着难道你也知道啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510051236V#644F#1P和那样棒的帅哥形影不离，\n',
            '却还要来羡慕女生宿舍，\n',
            '艾丝蒂尔你也真是的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051237V不觉得太暴殄天物了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051238V#007F真是的～你们说什么呀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051239V#006F其实我和约修亚\n',
            '纯粹是情同姐弟的关系。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051240V这么多年来，\n',
            '我们都是像家人一样生活在一起的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510051241V#649F#1P嘿嘿，像家人一样吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051242V就算你这么认为，\n',
            '那约修亚又是怎么想的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051243V#501F哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510051244V#659F#1P像他这种年纪的男孩，\n',
            '太过压抑自己的感情可是不好哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051245V更何况身边有一个\n',
            '又健康又漂亮的女孩子，\n',
            '我想他一定忍得很辛苦吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051246V#004F………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0008, 400)

    ChrTalk(
        0x0105,
        (
            '#0060051247V#043F说够了没有，乔儿！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060051248V#045F#3P不好意思，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051249V她一得意起来就会拿别人开玩笑,\n',
            '这是她的坏习惯，你要多多包涵哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0105, 400)

    ChrTalk(
        0x0008,
        (
            '#0510051250V#646F#1P哼～哼～\n',
            '那什么才不叫坏习惯啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0008, 400)

    ChrTalk(
        0x0105,
        (
            '#0060051251V#042F你有意见吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510051252V#641F#1P哎呀，一点都没有呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051253V#008F啊、啊哈哈……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051254V真是的～别吓我嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051255V#503F这种事，怎么可能嘛。\n',
            '居然说约修亚他会对我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#0510051256V#649F#1P意识到了、意识到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051257V#047F乔儿！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0008,
        (
            '#0510051258V#643F#1P啊，我忘记了。\n',
            '睡前得把当日报告交给老师。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510051259V#648F那么，晚安。\n',
            '你们两个先睡好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2240')
    def lambda_2240():
        CameraMove(-121140, 0, -5760, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2240)

    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    ChrSetFlags(0x0008, 0x0004)

    @scena.Lambda('lambda_226F')
    def lambda_226F():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_226F')

    DispatchAsync2(0x0101, 0x0002, lambda_226F)

    @scena.Lambda('lambda_2280')
    def lambda_2280():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_2280')

    DispatchAsync2(0x0105, 0x0002, lambda_2280)

    ChrWalkTo(0x0008, -120900, 0, -3700, 3000, 0x00)
    ChrWalkTo(0x0008, -120570, 0, -8500, 3000, 0x00)
    PlaySE(6, 0x00, 0x64)

    @scena.Lambda('lambda_22BE')
    def lambda_22BE():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_22BE)

    ChrWalkTo(0x0008, -120580, 0, -9820, 3000, 0x00)
    Sleep(200)

    PlaySE(7, 0x00, 0x64)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0105, 0xFF)

    ChrTalk(
        0x0105,
        (
            '#0060051260V#043F真是的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CameraMove(-120390, 0, -2060, 1500)

    ChrTalk(
        0x0105,
        (
            '#0060051261V#045F#1P对了，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051262V如果不介意的话，\n',
            '你这段时间就穿我的睡衣吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x0101)

    ChrTalk(
        0x0101,
        (
            '#0010051263V#503F……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051264V#044F#1P艾丝蒂尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051265V#004F哎！？',
            TxtCtl.Enter,
        ),
    )

    OP_9E(0x0101, 50, 0, 300, 6000)
    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrSetDirection(0x0101, 350, 400)

    ChrTalk(
        0x0101,
        (
            '#0010051266V#008F啊、啊啊，睡衣是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010051267V嗯，就随便借一件给我行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    FadeOut(1500, 0, -1)
    OP_0D()
    OP_21()
    Sleep(500)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '就这样，艾丝蒂尔和约修亚的校园生活\n',
            '以一种意想不到的形式展开了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_77(0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    MapSetFlags(0x10000000)
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T2512._SN', 115, 0, 1)
    IdleLoop()

    Return()

# id: 0x000C offset: 0x24E9
@scena.Code('func_0C_24E9')
def func_0C_24E9():
    EventBegin(0x00)
    ChrSetFlags(0x0102, 0x0080)
    OP_77(0xFF, 0xC8, 0x96, 0x00, 0x00000000)
    OP_72(0x0008, 0x0020)
    OP_6F(0x0008, 15)
    OP_72(0x000A, 0x0020)
    OP_6F(0x000A, 15)
    CameraMove(-118900, 0, -2700, 0)
    ChrClearFlags(0x0008, 0x0080)
    OP_62(0x0101, 0x00000258, 1200, 0x1C, 0x21, 0x000000FA, 0x00)
    OP_62(0x0008, 0x0000012C, 1750, 0x1C, 0x21, 0x000000FA, 0x00)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetPos(0x0105, -118840, 0, -3930, 180)
    ChrSetPos(0x0101, -118500, 500, -5400, 0)
    ChrSetPos(0x0008, -118550, 100, 300, 0)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetFlags(0x0101, 0x0002)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetFlags(0x0008, 0x0002)
    ChrSetChipByIndex(0x0101, 9)
    ChrSetChipByIndex(0x0008, 8)
    FadeIn(2000, 0)
    OP_0D()
    OP_62(0x0105, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(1000)

    OP_63(0x0101)
    ChrSetSubChip(0x0101, 15)
    Sleep(50)

    ChrSetSubChip(0x0101, 16)
    Sleep(1000)

    @scena.Lambda('lambda_25DF')
    def lambda_25DF():
        OP_99(0x00FE, 0x00, 0x07, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_25DF)

    Sleep(50)

    OP_6F(0x000A, 15)
    OP_70(0x000A, 20)
    Sleep(1000)

    OP_62(0x0101, 0x00000064, 1500, 0x18, 0x1B, 0x000000FA, 0x00)
    ChrSetDirection(0x0105, 270, 400)

    @scena.Lambda('lambda_2620')
    def lambda_2620():
        CameraMove(-118800, 0, -930, 2000)

        ExitThread()

    DispatchAsync(0x0105, 0x0002, lambda_2620)

    ChrWalkTo(0x0105, -120450, 0, -4000, 3000, 0x00)
    ChrWalkTo(0x0105, -120410, 0, -1040, 3000, 0x00)
    ChrWalkTo(0x0105, -118850, 0, -1010, 3000, 0x00)
    ChrSetDirection(0x0105, 0, 400)
    OP_62(0x0105, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(1000)

    OP_63(0x0101)
    Sleep(1000)

    @scena.Lambda('lambda_269A')
    def lambda_269A():
        OP_99(0x00FE, 0x07, 0x00, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_269A)

    Sleep(100)

    OP_6F(0x000A, 20)
    OP_70(0x000A, 15)
    WaitForThreadExit(0x0101, 0x0001)
    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    Sleep(1000)

    OP_62(0x0101, 0x00000258, 1200, 0x1C, 0x21, 0x000000FA, 0x00)
    ChrTurnDirection(0x0105, 0x0101, 400)
    OP_62(0x0105, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    Sleep(1200)

    OP_62(0x0105, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrSetDirection(0x0105, 270, 400)
    FadeOut(2000, 0, -1)

    @scena.Lambda('lambda_272C')
    def lambda_272C():
        CameraMove(-118900, 0, -2700, 1500)

        ExitThread()

    DispatchAsync(0x0105, 0x0002, lambda_272C)

    ChrWalkTo(0x0105, -120410, 0, -1040, 3500, 0x00)
    ChrWalkTo(0x0105, -120450, 0, -4000, 3500, 0x00)
    ChrWalkTo(0x0105, -118840, 0, -3930, 3500, 0x00)
    ChrSetDirection(0x0105, 180, 400)
    OP_0D()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '早上，他们和学院的同辈伙伴们\n',
            '一起起床，然后一起上学……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T2510._SN', 123, 0, 0)
    IdleLoop()

    Return()

# id: 0x000D offset: 0x27CE
@scena.Code('func_0D_27CE')
def func_0D_27CE():
    PlaySE(17, 0x00, 0x64)
    ChrSetFlags(0x0011, 0x0080)
    OP_64(0x00, 0x0001)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '卢安经济史·下',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(0x033F, 1)
    OP_28(0x0027, 0x01, 0x0100)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

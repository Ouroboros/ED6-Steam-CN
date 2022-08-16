import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import E0313_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('E0313   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Event'
    header.mapModel       = 'E0313.x'
    header.mapIndex       = 1
    header.bgm            = 116
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
        ('ED6_DT07/CH01550._CH', 'ED6_DT07/CH01550P._CP'),
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
        ('ED6_DT07/CH01320._CH', 'ED6_DT07/CH01320P._CP'),
    ]

# id: 0x10001 offset: 0xC2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '菲',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '修理员佩顿',
            x                   = 2270,
            z                   = 0,
            y                   = 5880,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '亲卫队队员',
            x                   = 2820,
            z                   = 0,
            y                   = -90,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '亲卫队队员',
            x                   = 2280,
            z                   = 0,
            y                   = 6070,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
    )

# id: 0x10002 offset: 0x142
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x142
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 700,
            y           = -2000,
            z           = -10500,
            range       = 3200,
            dword_10    = 0x00000DAC,
            dword_14    = 0xFFFFE2B4,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000016,
        ),
        ScenaEventData(
            x           = -30,
            y           = -1000,
            z           = -7340,
            range       = 3700,
            dword_10    = 0x000003E8,
            dword_14    = 0xFFFFDC88,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000001B,
        ),
    )

# id: 0x10004 offset: 0x182
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x182
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_1D2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 1, 0x2219)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_199',
    )

    ChrClearFlags(0x000A, 0x0080)

    Jump('loc_1CF')

    def _loc_199(): pass

    label('loc_199')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A4',
    )

    Jump('loc_1CF')

    def _loc_1A4(): pass

    label('loc_1A4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1B4',
    )

    ChrClearFlags(0x000A, 0x0080)

    Jump('loc_1CF')

    def _loc_1B4(): pass

    label('loc_1B4')

    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 3690, 0, -4710, 90)

    def _loc_1CF(): pass

    label('loc_1CF')

    Jump('loc_203')

    def _loc_1D2(): pass

    label('loc_1D2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            Expr.Return,
        ),
        'loc_1F2',
    )

    ChrSetPos(0x0008, 3690, 0, -4710, 90)
    ChrClearFlags(0x0008, 0x0080)

    Jump('loc_203')

    def _loc_1F2(): pass

    label('loc_1F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 6, 0x1A1E)),
            Expr.Return,
        ),
        'loc_203',
    )

    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)

    def _loc_203(): pass

    label('loc_203')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_216',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    Event(0, func_08_1FBA)

    def _loc_216(): pass

    label('loc_216')

    Return()

# id: 0x0001 offset: 0x217
@scena.Code('func_01_217')
def func_01_217():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_235',
    )

    ExecExpressionWithVar(
        0x3B,
        (
            (Expr.PushLong, 0x227),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x3C,
        (
            (Expr.PushLong, 0x10A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_235(): pass

    label('loc_235')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_271',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Return,
        ),
        'loc_265',
    )

    OP_B1('E0313_1')
    OP_72(0x0005, 0x0020)
    OP_72(0x0005, 0x0008)
    OP_6F(0x0005, 0)

    Jump('loc_26E')

    def _loc_265(): pass

    label('loc_265')

    OP_B1('E0313_2')

    def _loc_26E(): pass

    label('loc_26E')

    Jump('loc_2A3')

    def _loc_271(): pass

    label('loc_271')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_289',
    )

    OP_B1('E0313_2')

    Jump('loc_2A3')

    def _loc_289(): pass

    label('loc_289')

    OP_B1('E0313_1')
    OP_72(0x0005, 0x0020)
    OP_72(0x0005, 0x0008)
    OP_6F(0x0005, 0)

    def _loc_2A3(): pass

    label('loc_2A3')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2D9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 3, 0x1A23)),
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2CC',
    )

    MapSetFlags(0x02000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x21),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2D9')

    def _loc_2CC(): pass

    label('loc_2CC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 3, 0x1A23)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2D9',
    )

    PlaySE(122, 0x01, 0x46)

    def _loc_2D9(): pass

    label('loc_2D9')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_304',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_304',
    )

    MapSetFlags(0x02000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x21),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlaySE(122, 0x01, 0x46)

    def _loc_304(): pass

    label('loc_304')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_325',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_325',
    )

    MapSetFlags(0x02000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x3E),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_325(): pass

    label('loc_325')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            Expr.Return,
        ),
        'loc_32C',
    )

    def _loc_32C(): pass

    label('loc_32C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 6, 0x1E1E)),
            Expr.Return,
        ),
        'loc_34A',
    )

    OP_71(0x0006, 0x0004)
    OP_72(0x0007, 0x0004)
    OP_71(0x0008, 0x0004)
    OP_71(0x0009, 0x0004)

    Jump('loc_3A1')

    def _loc_34A(): pass

    label('loc_34A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 1, 0x1E11)),
            Expr.Return,
        ),
        'loc_368',
    )

    OP_71(0x0006, 0x0004)
    OP_71(0x0007, 0x0004)
    OP_72(0x0008, 0x0004)
    OP_71(0x0009, 0x0004)

    Jump('loc_3A1')

    def _loc_368(): pass

    label('loc_368')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 2, 0x1E0A)),
            Expr.Return,
        ),
        'loc_386',
    )

    OP_71(0x0006, 0x0004)
    OP_71(0x0007, 0x0004)
    OP_71(0x0008, 0x0004)
    OP_72(0x0009, 0x0004)

    Jump('loc_3A1')

    def _loc_386(): pass

    label('loc_386')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            Expr.Return,
        ),
        'loc_3A1',
    )

    OP_72(0x0006, 0x0004)
    OP_71(0x0007, 0x0004)
    OP_71(0x0008, 0x0004)
    OP_71(0x0009, 0x0004)

    def _loc_3A1(): pass

    label('loc_3A1')

    Return()

# id: 0x0002 offset: 0x3A2
@scena.Code('func_02_3A2')
def func_02_3A2():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3B7',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_3A2')

    def _loc_3B7(): pass

    label('loc_3B7')

    Return()

# id: 0x0003 offset: 0x3B8
@scena.Code('func_03_3B8')
def func_03_3B8():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_3D7',
    )

    ChrTalk(
        0x00FE,
        (
            '◆没有台词。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BF7')

    def _loc_3D7(): pass

    label('loc_3D7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 6, 0x1E1E)),
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 7, 0x1E1F)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3EA',
    )

    Call(0, 0x000E)

    Jump('loc_BF7')

    def _loc_3EA(): pass

    label('loc_3EA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 1, 0x1E11)),
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 2, 0x1E12)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3FD',
    )

    Call(0, 0x000C)

    Jump('loc_BF7')

    def _loc_3FD(): pass

    label('loc_3FD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 2, 0x1E0A)),
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 4, 0x1E0C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_410',
    )

    Call(0, 0x000A)

    Jump('loc_BF7')

    def _loc_410(): pass

    label('loc_410')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 3, 0x1E03)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_41F',
    )

    Call(0, 0x0007)

    Jump('loc_BF7')

    def _loc_41F(): pass

    label('loc_41F')

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
        0,
        (
            TXT(0x00, '【说话】\n'),
            TXT(0x01, '【搭乘升降机】\n'),
            TXT(0x02, '【放弃】\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_553',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么请立刻\n',
            '站到升降机上吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 6, 0x1E1E)),
            Expr.Return,
        ),
        'loc_4E6',
    )

    Call(0, 0x0010)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    NewScene('ED6_DT21/E0301._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_552')

    def _loc_4E6(): pass

    label('loc_4E6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 1, 0x1E11)),
            Expr.Return,
        ),
        'loc_50B',
    )

    Call(0, 0x0010)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    NewScene('ED6_DT21/E0301._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_552')

    def _loc_50B(): pass

    label('loc_50B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 2, 0x1E0A)),
            Expr.Return,
        ),
        'loc_530',
    )

    Call(0, 0x0010)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/E0301._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_552')

    def _loc_530(): pass

    label('loc_530')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            Expr.Return,
        ),
        'loc_552',
    )

    Call(0, 0x0010)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/E0301._SN', 100, 0, 0)
    IdleLoop()

    def _loc_552(): pass

    label('loc_552')

    Return()

    def _loc_553(): pass

    label('loc_553')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_564',
    )

    TalkEnd(0x00FE)

    Return()

    def _loc_564(): pass

    label('loc_564')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 6, 0x1E1E)),
            Expr.Return,
        ),
        'loc_687',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_61A',
    )

    ChrTalk(
        0x00FE,
        (
            '博士正在研究的『装置』\n',
            '试制终于有了头绪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '用升降机将你们送下去之后，\n',
            '我要马上去帮忙进行原型的制作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，它的功能大概要等到\n',
            '组装完毕后才会知道呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_684')

    def _loc_61A(): pass

    label('loc_61A')

    ChrTalk(
        0x00FE,
        (
            '『装置』有了试作的头绪，\n',
            '我也打算过去帮一下忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，至于有些什么功能，\n',
            '这就是组装完毕后的事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_684(): pass

    label('loc_684')

    Jump('loc_BF7')

    def _loc_687(): pass

    label('loc_687')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 1, 0x1E11)),
            Expr.Return,
        ),
        'loc_7A6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_73F',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才中央工房的雷伊\n',
            '一边散步一边发着牢骚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他一直都很沉着冷静，\n',
            '从来就不是那种埋首研究的类型……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过他居然变成那样，\n',
            '看来这次的研究似乎相当困难呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_7A3')

    def _loc_73F(): pass

    label('loc_73F')

    ChrTalk(
        0x00FE,
        (
            '刚才中央工房的雷伊\n',
            '一边散步一边发着牢骚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他居然变成那样，\n',
            '看来这次的研究似乎相当困难呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7A3(): pass

    label('loc_7A3')

    Jump('loc_BF7')

    def _loc_7A6(): pass

    label('loc_7A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 2, 0x1E0A)),
            Expr.Return,
        ),
        'loc_8E7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_872',
    )

    ChrTalk(
        0x00FE,
        (
            '拉赛尔老爷子所研究的东西\n',
            '好像是极特殊的导力器。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我看过设计图，但是里面有一大堆\n',
            '功能不明的结晶回路，真令人头疼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '乍看很像是导力波的增幅器……\n',
            '到底是用来做什么的装置呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_8E4')

    def _loc_872(): pass

    label('loc_872')

    ChrTalk(
        0x00FE,
        (
            '拉赛尔老爷子所研究的东西\n',
            '好像是极特殊的导力器。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '乍看很像是导力波的增幅器……\n',
            '到底是用来做什么的装置呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8E4(): pass

    label('loc_8E4')

    Jump('loc_BF7')

    def _loc_8E7(): pass

    label('loc_8E7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            Expr.Return,
        ),
        'loc_BF7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B95',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然我不太清楚详情，\n',
            '不过好像是老爷子正在研究新发明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以，因为人手不够\n',
            '急急忙忙叫我们来凑数是吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0031, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0031, 0x01, 0x0020)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_979',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_979(): pass

    label('loc_979')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9F1',
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
        100,
        0,
        (
            TXT(0x00, '【◇前作『爱的使者』高评价完成】\n'),
            TXT(0x01, '【◇没有完成】\n'),
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
        (0x00000000, 'loc_9E5'),
        (0x00000001, 'loc_9EB'),
        (-1, 'loc_9F1'),
    )

    def _loc_9E5(): pass

    label('loc_9E5')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_9F1')

    def _loc_9EB(): pass

    label('loc_9EB')

    ClearScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_9F1')

    def _loc_9F1(): pass

    label('loc_9F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_A2E',
    )

    ChrTalk(
        0x00FE,
        (
            '呼～，本来这个时候\n',
            '应该正在和布拉姆旅行呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A5F')

    def _loc_A2E(): pass

    label('loc_A2E')

    ChrTalk(
        0x00FE,
        (
            '呼～，本来这个时候\n',
            '应该正在和鲁迪旅行呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A5F(): pass

    label('loc_A5F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_ABE',
    )

    ChrTalk(
        0x0107,
        (
            '#562F啊……\n',
            '菲小姐，真的很抱歉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '一直以来都是\n',
            '因为爷爷的缘故……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0107, 400)

    Jump('loc_AF6')

    def _loc_ABE(): pass

    label('loc_ABE')

    ChrTalk(
        0x0101,
        (
            '#1016F啊、啊哈哈……\n',
            '让人不禁有点同情你呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    def _loc_AF6(): pass

    label('loc_AF6')

    ChrTalk(
        0x00FE,
        (
            '不过，在这种时候受人之托\n',
            '心里还是很高兴的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且这项工作也十分有意义，\n',
            '我可不会对那些小事耿耿于怀哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有什么难处要告诉我啊。\n',
            '我会帮忙的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_BF7')

    def _loc_B95(): pass

    label('loc_B95')

    ChrTalk(
        0x00FE,
        (
            '拉赛尔老爷子\n',
            '好像在研究什么新发明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '光是分析塔的现象就够忙了，\n',
            '居然还在插手其它的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BF7(): pass

    label('loc_BF7')

    TalkEnd(0x0008)

    Return()

# id: 0x0004 offset: 0xBFB
@scena.Code('func_04_BFB')
def func_04_BFB():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 6, 0x1A1E)),
            Expr.Return,
        ),
        'loc_1128',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034E, 3, 0x1A73)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_109B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C87',
    )

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
        0,
        (
            TXT(0x00, '【决定做在◇3章中没遇到的事】\n'),
            TXT(0x01, '【决定做在◇3章中见到过的事】\n'),
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
    FadeIn(300, 0)

    def _loc_C87(): pass

    label('loc_C87')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_DEF',
    )

    ChrTalk(
        0x00FE,
        (
            '呀，艾丝蒂尔。\n',
            '好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F啊，你是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '咦，不记得我了吗？\n',
            '我是维修员佩顿啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '理查德上校事件发生时\n',
            '我曾经参加了作战啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1008F对、对不起。\n',
            '终于想起来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '就是那个时候为我们\n',
            '准备了特务艇的人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊哈哈，谢谢。\n',
            '你能想起我是我的光荣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，我听别人说\n',
            '有游击士要登舰……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过没想到\n',
            '是艾丝蒂尔你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ED8')

    def _loc_DEF(): pass

    label('loc_DEF')

    ChrTalk(
        0x00FE,
        (
            '哎呀，艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1004F啊，佩顿先生。\n',
            '你怎么会在这里呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1016F……不过仔细想想\n',
            '也是理所当然的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊哈哈，因为我可是\n',
            '这艘军舰的专职维修员啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，我听别人说\n',
            '有游击士要登舰……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过没想到\n',
            '是艾丝蒂尔你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_ED8(): pass

    label('loc_ED8')

    ChrTalk(
        0x0101,
        (
            '#1006F我也没想到\n',
            '『埃尔赛尤』会来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '看来王国军对于这次作战\n',
            '投入了相当多的力量呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是啊，听说是继『百日战役』之后，\n',
            '最大的作战行动呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还有，根据传言\n',
            '目标是传说中的古代龙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以新型引擎的处女秀来说，\n',
            '算是个完美的对手呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011F嘿，这么有信心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '当然，为了这一天的到来\n',
            '我不断地进行了各种的调整呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '中央工房的设计者预定\n',
            '今天也要来记录数据。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难得有个这么盛大的舞台。\n',
            '就让『埃尔赛尤』\n',
            '尽情地发挥它的力量吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x034E, 3, 0x1A73))

    Jump('loc_1128')

    def _loc_109B(): pass

    label('loc_109B')

    ChrTalk(
        0x00FE,
        (
            '此次的作战目标\n',
            '是捕获古代龙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以新型引擎的处女秀来说，\n',
            '算得上是个完美的对手呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '『埃尔赛尤』应该也能\n',
            '尽情地发挥它的力量吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1128(): pass

    label('loc_1128')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x112C
@scena.Code('func_05_112C')
def func_05_112C():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11B8',
    )

    ChrTalk(
        0x00FE,
        (
            '脱落的舷外支架啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '居然决定要用榴弹炮\n',
            '进行牵引回收了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '据说是穆拉少校的提议，\n',
            '的确很像陆军国家的想法呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_137A')

    def _loc_11B8(): pass

    label('loc_11B8')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0xF),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_12AF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_125D',
    )

    ChrTalk(
        0x00FE,
        (
            '<FIXME>あ、これから\n',
            '少佐の案を試してみるところですよ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '居然决定要用榴弹炮\n',
            '牵引回收脱落的舷外支架……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这点子我们可想不出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_12AC')

    def _loc_125D(): pass

    label('loc_125D')

    ChrTalk(
        0x00FE,
        (
            '居然决定要用榴弹炮\n',
            '牵引回收脱落的舷外支架……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这点子我们可想不出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12AC(): pass

    label('loc_12AC')

    Jump('loc_137A')

    def _loc_12AF(): pass

    label('loc_12AF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1337',
    )

    ChrTalk(
        0x00FE,
        (
            '脱落的舷外支架啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '居然决定要用榴弹炮\n',
            '进行牵引回收了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像是穆拉少校的提议，\n',
            '的确很像陆军国家的想法呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_137A')

    def _loc_1337(): pass

    label('loc_1337')

    ChrTalk(
        0x00FE,
        (
            '居然将宝贵的榴弹炮\n',
            '当成拖拉机用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这点子我们可想不出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_137A(): pass

    label('loc_137A')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x137E
@scena.Code('func_06_137E')
def func_06_137E():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Return,
        ),
        'loc_168D',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_141F',
    )

    ChrTalk(
        0x00FE,
        (
            '据说要在脱落的左舷部系上锁链\n',
            '然后再用榴弹炮进行牵引拖曳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是粗暴的做法，\n',
            '不过也没有其他办法了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '无论如何要尝试一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_168A')

    def _loc_141F(): pass

    label('loc_141F')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0xF),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1557',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_14E4',
    )

    ChrTalk(
        0x00FE,
        (
            '据说要在脱落的左舷部系上锁链\n',
            '然后用榴弹炮牵引拖曳……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是粗暴的做法，\n',
            '不过确实只有这样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '结社那些家伙的动向也很让人在意，\n',
            '所以必须要尽快完成修复才行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_1554')

    def _loc_14E4(): pass

    label('loc_14E4')

    ChrTalk(
        0x00FE,
        (
            '结社那些家伙的动向也很让人在意，\n',
            '所以必须要尽快完成修复才行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是粗暴的做法，\n',
            '不过确实只有这样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1554(): pass

    label('loc_1554')

    Jump('loc_168A')

    def _loc_1557(): pass

    label('loc_1557')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1610',
    )

    ChrTalk(
        0x00FE,
        (
            '据说要在脱落的左舷部系上锁链\n',
            '然后用榴弹炮牵引拖曳……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是粗暴的做法，\n',
            '不过确实只有这样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '结社那些家伙的动向也很让人在意，\n',
            '所以必须要尽快完成修复才行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_168A')

    def _loc_1610(): pass

    label('loc_1610')

    ChrTalk(
        0x00FE,
        (
            '结社那些家伙的动向也很让人在意，\n',
            '所以必须要尽快完成修复才行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是粗暴的做法，\n',
            '但只要是有效的手段就必须尝试。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_168A(): pass

    label('loc_168A')

    Jump('loc_18E2')

    def _loc_168D(): pass

    label('loc_168D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Return,
        ),
        'loc_16F5',
    )

    ChrTalk(
        0x00FE,
        (
            '多亏有了作业专用的通道，\n',
            '工作进展容易多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我想今后修复工程\n',
            '也会因此而更为迅速哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18E2')

    def _loc_16F5(): pass

    label('loc_16F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_17D8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1785',
    )

    ChrTalk(
        0x00FE,
        (
            '听说要在舰外开辟\n',
            '作业专用的通道呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们正在寻找\n',
            '有没有什么合适的材料。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '拆掉集装箱\n',
            '拿铁板来用也是一个办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_17D5')

    def _loc_1785(): pass

    label('loc_1785')

    ChrTalk(
        0x00FE,
        (
            '我在为作业专用的通道\n',
            '寻找材料。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，万不得已时\n',
            '就只能拆掉集装箱了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17D5(): pass

    label('loc_17D5')

    Jump('loc_18E2')

    def _loc_17D8(): pass

    label('loc_17D8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 6, 0x1A1E)),
            Expr.Return,
        ),
        'loc_18E2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1882',
    )

    ChrTalk(
        0x00FE,
        (
            '在王都政变二次起义中\n',
            '这里的导力炮也受到袭击。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然全部损坏了，\n',
            '但幸好马上进行了补充。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果没有这个东西，\n',
            '我们降落之后就等于手无寸铁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_18E2')

    def _loc_1882(): pass

    label('loc_1882')

    ChrTalk(
        0x00FE,
        (
            '在王都政变二次起义中\n',
            '这里的导力炮也受到袭击。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然全部损坏了，\n',
            '但幸好马上进行了补充。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18E2(): pass

    label('loc_18E2')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x18E6
@scena.Code('func_07_18E6')
def func_07_18E6():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_190B',
    )

    Call(0, 0x0017)
    Call(0, 0x0018)
    FadeIn(0, 0)
    Sleep(100)

    def _loc_190B(): pass

    label('loc_190B')

    Fade(1000)
    CameraMove(3010, 0, -4350, 0)
    OP_67(0, 5650, -10000, 0)
    CameraSetDistance(3150, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 2200, 0, -5260, 90)
    ChrSetPos(0x0102, 2200, 0, -4400, 90)
    ChrSetPos(0x00F8, 900, 0, -5260, 90)
    ChrSetPos(0x00F9, 900, 0, -4400, 90)
    ChrSetDirection(0x0008, 270, 0)
    OP_4A(0x0008, 255)
    OP_0D()
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 2, 0x1E02)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1CD4',
    )

    SetScenaFlags(ScenaFlag(0x03C0, 2, 0x1E02))

    ChrTalk(
        0x0008,
        (
            '#1980340650V呀，来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B86',
    )

    ChrTalk(
        0x0101,
        (
            '#0010340651V#1004F#6P啊，菲小姐？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070340652V#560F#6P您怎么会\n',
            '在埃尔赛尤号上啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1980340653V我是和拉赛尔老爷子\n',
            '一起搭上这艘船的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1980340654V听说维修人员的人手\n',
            '似乎不太够的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070340655V#064F#6P不过，我记得这里\n',
            '应该有常驻的维修员吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1980340656V不，好像是为了\n',
            '舰艇维修以外的事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1980340657V我想该不会是来帮忙完成\n',
            '老爷子的新发明吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070340658V#067F#6P嗯。\n',
            '是有这个可能呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C6D')

    def _loc_1B86(): pass

    label('loc_1B86')

    ChrTalk(
        0x0101,
        (
            '#0010340659V#1004F#6P啊，菲小姐？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010340660V你怎么会在\n',
            '埃尔赛尤号上啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1980340653V我是和拉赛尔老爷子\n',
            '一起搭上这艘船的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1980340654V听说维修人员的人手\n',
            '似乎不太够的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340663V#1015F#6P哦～是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C6D(): pass

    label('loc_1C6D')

    ChrTalk(
        0x0008,
        (
            '#1980340664V嗯，反正现在有空\n',
            '就到船上来帮忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1980340665V那么……\n',
            '要马上搭乘升降机吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D22')

    def _loc_1CD4(): pass

    label('loc_1CD4')

    ChrTalk(
        0x00FE,
        (
            '#1980340666V呀，辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980340667V要下降到『翡翠之塔』的前方吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1D22(): pass

    label('loc_1D22')

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
        0,
        (
            TXT(0x00, '【搭乘升降机】\n'),
            TXT(0x01, '【还有点事】\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1DC1',
    )

    ChrTalk(
        0x00FE,
        (
            '#1980340668V明白了。\n',
            '需要时叫我一声哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 90, 400)
    OP_4B(0x0008, 255)
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

    def _loc_1DC1(): pass

    label('loc_1DC1')

    ChrTalk(
        0x0008,
        (
            '#1980340669V嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1980340670V那么请立刻\n',
            '站到升降机上吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240717V#1006F#6P好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(2029, 0, -710, 0)
    OP_67(0, 6620, -10000, 0)
    CameraSetDistance(3340, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, -600, -100, -600, 180)
    ChrSetPos(0x0102, 600, -100, -600, 180)
    ChrSetPos(0x00F8, -600, -100, 600, 180)
    ChrSetPos(0x00F9, 600, -100, 600, 180)
    Sleep(500)

    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x00FE,
        (
            '#1980340672V#2P现在要将你们放下去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980340673V#2P虽然这个应该很平稳\n',
            '不过你们还是要小心，不要掉下去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 90, 400)
    Sleep(1000)

    OP_6F(0x0005, 0)
    OP_70(0x0005, 10)
    PlaySE(247, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010340674V#1004F#5P哇……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    MapSetFlags(0x00100000)
    PlaySE(104, 0x00, 0x64)
    OP_6F(0x0005, 10)
    OP_70(0x0005, 60)
    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/E0301._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0008 offset: 0x1FBA
@scena.Code('func_08_1FBA')
def func_08_1FBA():
    EventBegin(0x00)
    CameraMove(0, -250, 0, 0)
    OP_67(0, 7500, -10000, 0)
    CameraSetDistance(4000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, -620, -4000, -820, 180)
    ChrSetPos(0x0102, 750, -4000, -780, 180)
    ChrSetPos(0x00F8, -700, -4000, 280, 180)
    ChrSetPos(0x00F9, 600, -4000, 290, 180)
    MapClearFlags(0x00100000)
    OP_6F(0x0005, 60)
    OP_70(0x0005, 0)
    FadeIn(1000, 0)
    OP_0D()
    OP_73(0x0005)
    OP_23(0x0068)
    PlaySE(247, 0x00, 0x64)
    Sleep(1000)

    Fade(500)
    CameraMove(70, 0, -3620, 0)
    OP_67(0, 7500, -10000, 0)
    CameraSetDistance(4000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, 70, 0, -3620, 180)
    ChrSetPos(0x0001, 70, 0, -3620, 180)
    ChrSetPos(0x0002, 70, 0, -3620, 180)
    ChrSetPos(0x0003, 70, 0, -3620, 180)
    OP_0D()
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

# id: 0x0009 offset: 0x20F9
@scena.Code('func_09_20F9')
def func_09_20F9():
    EventBegin(0x00)
    Fade(1000)
    CameraMove(3010, 0, -4350, 0)
    OP_67(0, 5650, -10000, 0)
    CameraSetDistance(3150, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 2200, 0, -5260, 90)
    ChrSetPos(0x0102, 2200, 0, -4400, 90)
    ChrSetPos(0x00F8, 900, 0, -5260, 90)
    ChrSetPos(0x00F9, 900, 0, -4400, 90)
    ChrSetDirection(0x0008, 270, 0)
    OP_4A(0x0008, 255)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x0008,
        (
            '#1980340666V呀，辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1980340667V要下降到『翡翠之塔』的前方吗？',
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
        100,
        0,
        (
            TXT(0x00, '【搭乘升降机】\n'),
            TXT(0x01, '【还有点事】\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_227F',
    )

    ChrTalk(
        0x0008,
        (
            '#1980340668V明白了。\n',
            '需要时叫我一声哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 90, 400)
    OP_4B(0x0008, 255)
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

    def _loc_227F(): pass

    label('loc_227F')

    ChrTalk(
        0x0008,
        (
            '#1980340669V嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1980340670V那么请立刻\n',
            '站到升降机上吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0010)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/R0303._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000A offset: 0x22E6
@scena.Code('func_0A_22E6')
def func_0A_22E6():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_230B',
    )

    Call(0, 0x0017)
    Call(0, 0x0019)
    FadeIn(0, 0)
    Sleep(100)

    def _loc_230B(): pass

    label('loc_230B')

    Fade(1000)
    CameraMove(3010, 0, -4350, 0)
    OP_67(0, 5650, -10000, 0)
    CameraSetDistance(3150, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 2200, 0, -5260, 90)
    ChrSetPos(0x0102, 2200, 0, -4400, 90)
    ChrSetPos(0x00F9, 900, 0, -5260, 90)
    ChrSetPos(0x00F8, 900, 0, -4400, 90)
    ChrSetDirection(0x0008, 270, 0)
    OP_4A(0x0008, 255)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x00FE,
        (
            '#1980340666V呀，辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980341023V要下降到『红莲之塔』的前方吗？',
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
        100,
        0,
        (
            TXT(0x00, '【搭乘升降机】\n'),
            TXT(0x01, '【还有点事】\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_248F',
    )

    ChrTalk(
        0x00FE,
        (
            '#1980340668V明白了。\n',
            '需要时叫我一声哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 90, 400)
    OP_4B(0x0008, 255)
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

    def _loc_248F(): pass

    label('loc_248F')

    ChrTalk(
        0x00FE,
        (
            '#1980340669V嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980340670V那么请立刻\n',
            '站到升降机上吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0010)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/E0301._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000B offset: 0x24F6
@scena.Code('func_0B_24F6')
def func_0B_24F6():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_251B',
    )

    Call(0, 0x0017)
    Call(0, 0x0019)
    FadeIn(0, 0)
    Sleep(100)

    def _loc_251B(): pass

    label('loc_251B')

    Fade(1000)
    CameraMove(3010, 0, -4350, 0)
    OP_67(0, 5650, -10000, 0)
    CameraSetDistance(3150, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 2200, 0, -5260, 90)
    ChrSetPos(0x0102, 2200, 0, -4400, 90)
    ChrSetPos(0x00F9, 900, 0, -5260, 90)
    ChrSetPos(0x00F8, 900, 0, -4400, 90)
    ChrSetDirection(0x0008, 270, 0)
    OP_4A(0x0008, 255)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x00FE,
        (
            '#1980340666V呀，辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980341023V要下降到『红莲之塔』的前方吗？',
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
        100,
        0,
        (
            TXT(0x00, '【搭乘升降机】\n'),
            TXT(0x01, '【还有点事】\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_269F',
    )

    ChrTalk(
        0x00FE,
        (
            '#1980340668V明白了。\n',
            '需要时叫我一声哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 90, 400)
    OP_4B(0x0008, 255)
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

    def _loc_269F(): pass

    label('loc_269F')

    ChrTalk(
        0x00FE,
        (
            '#1980340669V嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980340670V那么请立刻\n',
            '站到升降机上吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0010)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/R3104._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000C offset: 0x2706
@scena.Code('func_0C_2706')
def func_0C_2706():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_272B',
    )

    Call(0, 0x0017)
    Call(0, 0x001A)
    FadeIn(0, 0)
    Sleep(100)

    def _loc_272B(): pass

    label('loc_272B')

    Fade(1000)
    CameraMove(3010, 0, -4350, 0)
    OP_67(0, 5650, -10000, 0)
    CameraSetDistance(3150, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 2200, 0, -5260, 90)
    ChrSetPos(0x0102, 2200, 0, -4400, 90)
    ChrSetPos(0x00F9, 900, 0, -5260, 90)
    ChrSetPos(0x00F8, 900, 0, -4400, 90)
    ChrSetDirection(0x0008, 270, 0)
    OP_4A(0x0008, 255)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x0008,
        (
            '#1980340666V呀，辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1980341287V要下降到『绀碧之塔』的前方吗？',
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
        100,
        0,
        (
            TXT(0x00, '【搭乘升降机】\n'),
            TXT(0x01, '【还有点事】\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_28AF',
    )

    ChrTalk(
        0x00FE,
        (
            '#1980340668V明白了。\n',
            '需要时叫我一声哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 90, 400)
    OP_4B(0x0008, 255)
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

    def _loc_28AF(): pass

    label('loc_28AF')

    ChrTalk(
        0x00FE,
        (
            '#1980340669V嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980340670V那么请立刻\n',
            '站到升降机上吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0010)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    NewScene('ED6_DT21/E0301._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000D offset: 0x2916
@scena.Code('func_0D_2916')
def func_0D_2916():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_293B',
    )

    Call(0, 0x0017)
    Call(0, 0x001A)
    FadeIn(0, 0)
    Sleep(100)

    def _loc_293B(): pass

    label('loc_293B')

    Fade(1000)
    CameraMove(3010, 0, -4350, 0)
    OP_67(0, 5650, -10000, 0)
    CameraSetDistance(3150, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 2200, 0, -5260, 90)
    ChrSetPos(0x0102, 2200, 0, -4400, 90)
    ChrSetPos(0x00F9, 900, 0, -5260, 90)
    ChrSetPos(0x00F8, 900, 0, -4400, 90)
    ChrSetDirection(0x0008, 270, 0)
    OP_4A(0x0008, 255)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x0008,
        (
            '#1980340666V呀，辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1980341287V要下降到『绀碧之塔』的前方吗？',
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
        100,
        0,
        (
            TXT(0x00, '【搭乘升降机】\n'),
            TXT(0x01, '【还有点事】\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2ABF',
    )

    ChrTalk(
        0x00FE,
        (
            '#1980340668V明白了。\n',
            '需要时叫我一声哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 90, 400)
    OP_4B(0x0008, 255)
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

    def _loc_2ABF(): pass

    label('loc_2ABF')

    ChrTalk(
        0x00FE,
        (
            '#1980340669V嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980340670V那么请立刻\n',
            '站到升降机上吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0010)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/R2401._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000E offset: 0x2B26
@scena.Code('func_0E_2B26')
def func_0E_2B26():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2B4B',
    )

    Call(0, 0x0017)
    Call(0, 0x0018)
    FadeIn(0, 0)
    Sleep(100)

    def _loc_2B4B(): pass

    label('loc_2B4B')

    Fade(1000)
    CameraMove(3010, 0, -4350, 0)
    OP_67(0, 5650, -10000, 0)
    CameraSetDistance(3150, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 2200, 0, -5260, 90)
    ChrSetPos(0x0102, 2200, 0, -4400, 90)
    ChrSetPos(0x00F9, 900, 0, -5260, 90)
    ChrSetPos(0x00F8, 900, 0, -4400, 90)
    ChrSetDirection(0x0008, 270, 0)
    OP_4A(0x0008, 255)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x0008,
        (
            '#1980341526V终于到最后的塔了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1980341527V要下降到『琥珀之塔』的前方吗？',
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
        100,
        0,
        (
            TXT(0x00, '【搭乘升降机】\n'),
            TXT(0x01, '【还有点事】\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2CD5',
    )

    ChrTalk(
        0x00FE,
        (
            '#1980340668V明白了。\n',
            '需要时叫我一声哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 90, 400)
    OP_4B(0x0008, 255)
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

    def _loc_2CD5(): pass

    label('loc_2CD5')

    ChrTalk(
        0x00FE,
        (
            '#1980340669V嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980340670V那么请立刻\n',
            '站到升降机上吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0010)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    NewScene('ED6_DT21/E0301._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000F offset: 0x2D3C
@scena.Code('func_0F_2D3C')
def func_0F_2D3C():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2D61',
    )

    Call(0, 0x0017)
    Call(0, 0x0018)
    FadeIn(0, 0)
    Sleep(100)

    def _loc_2D61(): pass

    label('loc_2D61')

    Fade(1000)
    CameraMove(3010, 0, -4350, 0)
    OP_67(0, 5650, -10000, 0)
    CameraSetDistance(3150, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 2200, 0, -5260, 90)
    ChrSetPos(0x0102, 2200, 0, -4400, 90)
    ChrSetPos(0x00F9, 900, 0, -5260, 90)
    ChrSetPos(0x00F8, 900, 0, -4400, 90)
    ChrSetDirection(0x0008, 270, 0)
    OP_4A(0x0008, 255)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x0008,
        (
            '#1980341526V终于到最后的塔了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1980341527V要下降到『琥珀之塔』的前方吗？',
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
        100,
        0,
        (
            TXT(0x00, '【搭乘升降机】\n'),
            TXT(0x01, '【还有点事】\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2EEB',
    )

    ChrTalk(
        0x00FE,
        (
            '#1980340668V明白了。\n',
            '需要时叫我一声哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 90, 400)
    OP_4B(0x0008, 255)
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

    def _loc_2EEB(): pass

    label('loc_2EEB')

    ChrTalk(
        0x00FE,
        (
            '#1980340669V嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1980340670V那么请立刻\n',
            '站到升降机上吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0010)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/R1402._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0010 offset: 0x2F52
@scena.Code('func_10_2F52')
def func_10_2F52():
    Sleep(300)

    Fade(500)
    CameraMove(2029, 0, -710, 0)
    OP_67(0, 6620, -10000, 0)
    CameraSetDistance(3340, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, -600, -100, -600, 180)
    ChrSetPos(0x0102, 600, -100, -600, 180)
    ChrSetPos(0x00F8, -600, -100, 600, 180)
    ChrSetPos(0x00F9, 600, -100, 600, 180)
    OP_0D()
    Sleep(300)

    ChrSetDirection(0x0008, 90, 400)
    Sleep(1000)

    OP_6F(0x0005, 0)
    OP_70(0x0005, 10)
    PlaySE(247, 0x00, 0x64)
    Sleep(1000)

    MapSetFlags(0x00100000)
    PlaySE(104, 0x00, 0x64)
    OP_6F(0x0005, 10)
    OP_70(0x0005, 60)
    Sleep(1000)

    Return()

# id: 0x0011 offset: 0x3025
@scena.Code('func_11_3025')
def func_11_3025():
    ChrWalkTo(0x00FE, -550, -250, -550, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0012 offset: 0x3041
@scena.Code('func_12_3041')
def func_12_3041():
    ChrWalkTo(0x00FE, -550, -250, 550, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0013 offset: 0x305D
@scena.Code('func_13_305D')
def func_13_305D():
    ChrWalkTo(0x00FE, 550, -250, -550, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0014 offset: 0x3079
@scena.Code('func_14_3079')
def func_14_3079():
    ChrWalkTo(0x00FE, 550, 0, 4530, 2000, 0x00)
    ChrWalkTo(0x00FE, 550, -250, 550, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0015 offset: 0x30A9
@scena.Code('func_15_30A9')
def func_15_30A9():
    ChrWalkTo(0x00FE, 2230, 0, 6360, 2000, 0x00)
    ChrTurnDirection(0x00FE, 0x0101, 400)

    Return()

# id: 0x0016 offset: 0x30C5
@scena.Code('func_16_30C5')
def func_16_30C5():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_30FD',
    )

    EventBegin(0x02)
    FadeOut(500, 0, -1)
    ChrSetDirection(0x0000, 180, 0)
    ChrMoveToRelativeAsync(0x0000, 0, 0, -1000, 1000, 0x00)
    OP_0D()
    NewScene('ED6_DT21/C5900._SN', 102, 0, 0)
    IdleLoop()

    def _loc_30FD(): pass

    label('loc_30FD')

    Return()

# id: 0x0017 offset: 0x30FE
@scena.Code('func_17_30FE')
def func_17_30FE():
    FadeOut(0, 0, -1)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)

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
        0,
        (
            TXT(0x00, '【◇选择雪拉扎德为队友】\n'),
            TXT(0x01, '【◇选择阿加特为队友】\n'),
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
        (0x00000000, 'loc_3178'),
        (0x00000001, 'loc_317E'),
        (-1, 'loc_3184'),
    )

    def _loc_3178(): pass

    label('loc_3178')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_3184')

    def _loc_317E(): pass

    label('loc_317E')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_3184')

    def _loc_3184(): pass

    label('loc_3184')

    Return()

# id: 0x0018 offset: 0x3185
@scena.Code('func_18_3185')
def func_18_3185():
    FadeOut(0, 0, -1)
    CameraMove(-18870, 0, -1650, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['雪拉扎德'],
            ChrTable['提妲'],
            ChrTable['科洛丝'],
            ChrTable['金'],
            ChrTable['凯文神父'],
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0)

    Return()

# id: 0x0019 offset: 0x3214
@scena.Code('func_19_3214')
def func_19_3214():
    FadeOut(0, 0, -1)
    CameraMove(-18870, 0, -1650, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            ChrTable['金'],
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['雪拉扎德'],
            ChrTable['提妲'],
            ChrTable['科洛丝'],
            ChrTable['凯文神父'],
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0)

    Return()

# id: 0x001A offset: 0x32A1
@scena.Code('func_1A_32A1')
def func_1A_32A1():
    FadeOut(0, 0, -1)
    CameraMove(-18870, 0, -1650, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            ChrTable['雪拉扎德'],
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['提妲'],
            ChrTable['科洛丝'],
            ChrTable['凯文神父'],
            ChrTable['金'],
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0)

    Return()

# id: 0x001B offset: 0x332E
@scena.Code('func_1B_332E')
def func_1B_332E():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3395',
    )

    EventBegin(0x01)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门紧紧地关着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    MapSetFlags(0x02000000)

    def _loc_3395(): pass

    label('loc_3395')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

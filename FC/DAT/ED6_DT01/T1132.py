import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T1132_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1132   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1132.x'
    header.mapIndex       = 1
    header.bgm            = 11
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/T1132._SN', 'ED6_DT01/T1132_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
        ('ED6_DT07/CH01560._CH', 'ED6_DT07/CH01560P._CP'),
        ('ED6_DT07/CH01350._CH', 'ED6_DT07/CH01350P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
    ]

# id: 0x10001 offset: 0xC2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '巴雷里奥',
            x                   = 4500,
            z                   = 0,
            y                   = 190600,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '蒂娜',
            x                   = -130180,
            z                   = 0,
            y                   = 130460,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '哈尔德',
            x                   = -86950,
            z                   = 0,
            y                   = 119700,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0000,
        ),
    )

# id: 0x10002 offset: 0x122
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x122
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x122
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 6598,
            triggerZ            = 0,
            triggerY            = 190158,
            triggerRange        = 700,
            actorX              = 4500,
            actorZ              = 1500,
            actorY              = 190662,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 3130,
            triggerZ            = 0,
            triggerY            = 192000,
            triggerRange        = 800,
            actorX              = 3130,
            actorZ              = 1000,
            actorY              = 192000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x16A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_185',
    )

    ChrSetPos(0x0009, -49700, 0, 119900, 0)

    Jump('loc_209')

    def _loc_185(): pass

    label('loc_185')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_1A0',
    )

    ChrSetPos(0x0009, -128400, 0, 139800, 0)

    Jump('loc_209')

    def _loc_1A0(): pass

    label('loc_1A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_1CC',
    )

    ChrSetPos(0x0009, -84700, 0, 152800, 0)

    If(
        (
            (Expr.Eval, "OP_29(0x0010, 0x01, 0x0002)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C9',
    )

    ChrClearFlags(0x000A, 0x0080)

    def _loc_1C9(): pass

    label('loc_1C9')

    Jump('loc_209')

    def _loc_1CC(): pass

    label('loc_1CC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_1E7',
    )

    ChrSetPos(0x0009, -84300, 0, 119900, 0)

    Jump('loc_209')

    def _loc_1E7(): pass

    label('loc_1E7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_202',
    )

    ChrSetPos(0x0009, -124300, 0, 179000, 0)

    Jump('loc_209')

    def _loc_202(): pass

    label('loc_202')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_209',
    )

    def _loc_209(): pass

    label('loc_209')

    Return()

# id: 0x0001 offset: 0x20A
@scena.Code('func_01_20A')
def func_01_20A():
    Return()

# id: 0x0002 offset: 0x20B
@scena.Code('func_02_20B')
def func_02_20B():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_220',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_20B')

    def _loc_220(): pass

    label('loc_220')

    Return()

# id: 0x0003 offset: 0x221
@scena.Code('func_03_221')
def func_03_221():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_24E',
    )

    def _loc_228(): pass

    label('loc_228')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_24B',
    )

    OP_8D(0x00FE, -51500, 121100, -47400, 118400, 2000)

    Jump('loc_228')

    def _loc_24B(): pass

    label('loc_24B')

    Jump('loc_32C')

    def _loc_24E(): pass

    label('loc_24E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_27B',
    )

    def _loc_255(): pass

    label('loc_255')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_278',
    )

    OP_8D(0x00FE, -130100, 142200, -127100, 126500, 2000)

    Jump('loc_255')

    def _loc_278(): pass

    label('loc_278')

    Jump('loc_32C')

    def _loc_27B(): pass

    label('loc_27B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_2A8',
    )

    def _loc_282(): pass

    label('loc_282')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2A5',
    )

    OP_8D(0x00FE, -86300, 154100, -82400, 151500, 2000)

    Jump('loc_282')

    def _loc_2A5(): pass

    label('loc_2A5')

    Jump('loc_32C')

    def _loc_2A8(): pass

    label('loc_2A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_2D5',
    )

    def _loc_2AF(): pass

    label('loc_2AF')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2D2',
    )

    OP_8D(0x00FE, -86000, 121200, -81700, 118700, 2000)

    Jump('loc_2AF')

    def _loc_2D2(): pass

    label('loc_2D2')

    Jump('loc_32C')

    def _loc_2D5(): pass

    label('loc_2D5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_302',
    )

    def _loc_2DC(): pass

    label('loc_2DC')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2FF',
    )

    OP_8D(0x00FE, -126000, 180700, -122800, 177900, 2000)

    Jump('loc_2DC')

    def _loc_2FF(): pass

    label('loc_2FF')

    Jump('loc_32C')

    def _loc_302(): pass

    label('loc_302')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_32C',
    )

    def _loc_309(): pass

    label('loc_309')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_32C',
    )

    OP_8D(0x00FE, -130120, 126680, -127550, 142940, 2000)

    Jump('loc_309')

    def _loc_32C(): pass

    label('loc_32C')

    Return()

# id: 0x0004 offset: 0x32D
@scena.Code('func_04_32D')
def func_04_32D():
    TalkBegin(0x0008)
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
            TXT(0x01, '休息\n'),
            TXT(0x02, '离开\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_389',
    )

    OP_0D()
    OP_A9(0x0D)
    OP_56(0x00)
    TalkEnd(0x0008)

    Return()

    def _loc_389(): pass

    label('loc_389')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_39A',
    )

    TalkEnd(0x0008)

    Return()

    def _loc_39A(): pass

    label('loc_39A')

    Call(0, 0x0005)
    ChrSetDirection(0x0008, 90, 0)

    Return()

# id: 0x0005 offset: 0x3A6
@scena.Code('func_05_3A6')
def func_05_3A6():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_4A5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_454',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '在时代的洪流中\n',
            '顽固地保持着传统……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我明白这是\n',
            '非常困难的一件事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '看来，\n',
            '我也不能被陈旧的习惯所束缚，\n',
            '要与时俱进地改善服务质量才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4A2')

    def _loc_454(): pass

    label('loc_454')

    ChrTalk(
        0x0008,
        (
            '在时代的洪流中\n',
            '顽固地保持着传统……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我明白这是\n',
            '非常困难的一件事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4A2(): pass

    label('loc_4A2')

    Jump('loc_986')

    def _loc_4A5(): pass

    label('loc_4A5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_545',
    )

    ChrTalk(
        0x0008,
        (
            '虽然我明白\n',
            '那些年轻员工所说的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '但是我自己\n',
            '已经是个落伍的人了，\n',
            '绝对不能接受他们所说的话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '哈哈……\n',
            '这个时代变得有些不可理喻了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_986')

    def _loc_545(): pass

    label('loc_545')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_65A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5F1',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '以前的员工都是团结一心\n',
            '为了满足顾客而共同努力的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '最近年轻人的思考方式\n',
            '也改变了许多啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '有很多事情\n',
            '都无法顺利开展了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_657')

    def _loc_5F1(): pass

    label('loc_5F1')

    ChrTalk(
        0x0008,
        (
            '以前的员工都是团结一心\n',
            '为了满足顾客而共同努力的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '最近年轻人的思考方式\n',
            '也改变了许多啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_657(): pass

    label('loc_657')

    Jump('loc_986')

    def _loc_65A(): pass

    label('loc_65A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_789',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_716',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '本酒店自创立以来，\n',
            '一直在国内保有非常高的人气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '虽然经常会忙不过来，\n',
            '不过，这家酒店就是我的生存价值……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '将这种勤劳肯干的传统\n',
            '传给下一任主管是我的职责。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_786')

    def _loc_716(): pass

    label('loc_716')

    ChrTalk(
        0x0008,
        (
            '本酒店自创立以来，\n',
            '一直在国内保有非常高的人气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '虽然经常会忙不过来，\n',
            '不过，这家酒店就是我的生存价值。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_786(): pass

    label('loc_786')

    Jump('loc_986')

    def _loc_789(): pass

    label('loc_789')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_886',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_829',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '迎接客人的时候\n',
            '必须要遵守严格的纪律……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '而且要把时时刻刻\n',
            '保持微笑作为行为准则。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '要向着提供更优质的服务\n',
            '这一目标努力再努力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_883')

    def _loc_829(): pass

    label('loc_829')

    ChrTalk(
        0x0008,
        (
            '迎接客人的时候\n',
            '必须要遵守严格的纪律……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '而且要把时时刻刻\n',
            '保持微笑作为行为准则。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_883(): pass

    label('loc_883')

    Jump('loc_986')

    def _loc_886(): pass

    label('loc_886')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_92C',
    )

    ChrTalk(
        0x0008,
        (
            '欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '本酒店自创业以来已经１２０年了。\n',
            '在柏斯也算是拥有悠久历史的酒店了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '请您务必要好好享受一下\n',
            '拥有悠久传统的本酒店所独有的高级服务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_986')

    def _loc_92C(): pass

    label('loc_92C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_986',
    )

    ChrTalk(
        0x0008,
        (
            '欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '请您务必要好好享受一下\n',
            '拥有悠久传统的本酒店所独有的高级服务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_986(): pass

    label('loc_986')

    TalkEnd(0x0008)

    Return()

# id: 0x0006 offset: 0x98A
@scena.Code('func_06_98A')
def func_06_98A():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_9BE',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，真是的！\n',
            '今天也忙得要命！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D8F')

    def _loc_9BE(): pass

    label('loc_9BE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_B0F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AA5',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '我是为了自己\n',
            '才来干这份工作的，\n',
            '而不是为了这个酒店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然主管说过\n',
            '做什么都要以酒店利益为前提，\n',
            '然后再行动……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以酒店利益为前提，\n',
            '是主管的工作吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我可不是\n',
            '来这里当佣人的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我说错了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B0C')

    def _loc_AA5(): pass

    label('loc_AA5')

    ChrTalk(
        0x00FE,
        (
            '虽然主管说过\n',
            '做什么都要以酒店利益为前提，\n',
            '然后再行动……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以酒店利益为前提，\n',
            '是主管的工作吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B0C(): pass

    label('loc_B0C')

    Jump('loc_D8F')

    def _loc_B0F(): pass

    label('loc_B0F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_B72',
    )

    ChrTalk(
        0x00FE,
        (
            '今天不管主管说什么，\n',
            '我都要依我自己的安排去逛街购物！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要将上次的郁闷一扫而光！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D8F')

    def _loc_B72(): pass

    label('loc_B72')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_C0E',
    )

    ChrTalk(
        0x00FE,
        (
            '你听我说！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明明是休息时间，\n',
            '主管却突然叫我来工作！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '好不容易订到了安特洛丝餐厅的位子，\n',
            '现在却去不成了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D8F')

    def _loc_C0E(): pass

    label('loc_C0E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_CA3',
    )

    ChrTalk(
        0x00FE,
        (
            '今天不管怎么样也要\n',
            '订到安特洛丝餐厅的座位！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了这一天\n',
            '我已经存了很长时间的钱了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊，我的心情好激动。\n',
            '要赶快把工作搞定！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D8F')

    def _loc_CA3(): pass

    label('loc_CA3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_D3D',
    )

    ChrTalk(
        0x00FE,
        (
            '工作完成之后，\n',
            '先去吃饭，\n',
            '然后到超市去看看衣服……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近那家店的评价挺不错。\n',
            '衣服的设计也很可爱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我要去看看\n',
            '有没有新的款式出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D8F')

    def _loc_D3D(): pass

    label('loc_D3D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_D8F',
    )

    ChrTalk(
        0x00FE,
        (
            '哈～忙死了忙死了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好想把讨厌的工作赶快解决掉，\n',
            '然后马上出去玩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D8F(): pass

    label('loc_D8F')

    TalkEnd(0x0009)

    Return()

# id: 0x0007 offset: 0xD93
@scena.Code('func_07_D93')
def func_07_D93():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　　　　　　　洗衣房　　　　　　　\n',
            '※工作人员以外禁止进入。',
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

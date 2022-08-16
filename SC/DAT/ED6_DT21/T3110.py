import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T3110_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3110   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3110.x'
    header.mapIndex       = 1
    header.bgm            = 13
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
        ('ED6_DT07/CH01430._CH', 'ED6_DT07/CH01430P._CP'),
        ('ED6_DT07/CH01070._CH', 'ED6_DT07/CH01070P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
    ]

# id: 0x10001 offset: 0xDA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '露依赛',
            x                   = -190,
            z                   = 0,
            y                   = 23730,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '乌缇',
            x                   = -1840,
            z                   = 4000,
            y                   = 23380,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '鲁特尔',
            x                   = 24940,
            z                   = 0,
            y                   = 530,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '索黛丽娅',
            x                   = -4040,
            z                   = 0,
            y                   = 3790,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '斯坦因',
            x                   = 48200,
            z                   = 0,
            y                   = 23060,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '阿利瑟',
            x                   = 27890,
            z                   = 0,
            y                   = 22500,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
    )

# id: 0x10002 offset: 0x19A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x19A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x19A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x19A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1B3',
    )

    ChrSetFlags(0x000A, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetFlags(0x000C, 0x0080)

    Jump('loc_218')

    def _loc_1B3(): pass

    label('loc_1B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_1C2',
    )

    ChrSetFlags(0x000A, 0x0080)

    Jump('loc_218')

    def _loc_1C2(): pass

    label('loc_1C2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_1DD',
    )

    ChrSetPos(0x0009, 940, 0, 23830, 319)

    Jump('loc_218')

    def _loc_1DD(): pass

    label('loc_1DD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 7, 0x1417)),
            Expr.Return,
        ),
        'loc_1F8',
    )

    ChrSetPos(0x0009, 940, 0, 23830, 319)

    Jump('loc_218')

    def _loc_1F8(): pass

    label('loc_1F8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_202',
    )

    Jump('loc_218')

    def _loc_202(): pass

    label('loc_202')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 0, 0x1408)),
            Expr.Return,
        ),
        'loc_218',
    )

    ChrSetFlags(0x000C, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0010)

    def _loc_218(): pass

    label('loc_218')

    Return()

# id: 0x0001 offset: 0x219
@scena.Code('func_01_219')
def func_01_219():
    Return()

# id: 0x0002 offset: 0x21A
@scena.Code('func_02_21A')
def func_02_21A():
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
        'loc_23F',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_381')

    def _loc_23F(): pass

    label('loc_23F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_258',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_381')

    def _loc_258(): pass

    label('loc_258')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_271',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_381')

    def _loc_271(): pass

    label('loc_271')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_28A',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_381')

    def _loc_28A(): pass

    label('loc_28A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2A3',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_381')

    def _loc_2A3(): pass

    label('loc_2A3')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2BC',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_381')

    def _loc_2BC(): pass

    label('loc_2BC')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2D5',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_381')

    def _loc_2D5(): pass

    label('loc_2D5')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2EE',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_381')

    def _loc_2EE(): pass

    label('loc_2EE')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_307',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_381')

    def _loc_307(): pass

    label('loc_307')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_320',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_381')

    def _loc_320(): pass

    label('loc_320')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_339',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_381')

    def _loc_339(): pass

    label('loc_339')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_352',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_381')

    def _loc_352(): pass

    label('loc_352')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_36B',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_381')

    def _loc_36B(): pass

    label('loc_36B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_381',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_381(): pass

    label('loc_381')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_396',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_381')

    def _loc_396(): pass

    label('loc_396')

    Return()

# id: 0x0003 offset: 0x397
@scena.Code('func_03_397')
def func_03_397():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3BA',
    )

    OP_8D(0x00FE, 25620, 1830, 23470, -690, 1000)

    Jump('func_03_397')

    def _loc_3BA(): pass

    label('loc_3BA')

    Return()

# id: 0x0004 offset: 0x3BB
@scena.Code('func_04_3BB')
def func_04_3BB():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3DE',
    )

    OP_8D(0x00FE, 48200, 23060, 51000, 22330, 1000)

    Jump('func_04_3BB')

    def _loc_3DE(): pass

    label('loc_3DE')

    Return()

# id: 0x0005 offset: 0x3DF
@scena.Code('func_05_3DF')
def func_05_3DF():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 0, 0x1408)),
            Expr.Return,
        ),
        'loc_4AC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_453',
    )

    ChrTalk(
        0x00FE,
        (
            '如果是那种程度的摇晃，\n',
            '中央工房应该还不要紧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊～晚了晚了～\n',
            '再不赶快出勤可不行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4AC')

    def _loc_453(): pass

    label('loc_453')

    ChrTalk(
        0x00FE,
        (
            '呀～地震\n',
            '真是很久没遇到过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一开始我还以为是拉赛尔博士\n',
            '又在搞什么试验了，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_4AC(): pass

    label('loc_4AC')

    TalkEnd(0x0008)

    Return()

# id: 0x0006 offset: 0x4B0
@scena.Code('func_06_4B0')
def func_06_4B0():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_5C6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_55A',
    )

    ChrTalk(
        0x00FE,
        (
            '导力器不能用了，\n',
            '大家都很困扰…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但我和姐姐\n',
            '却一点也不在乎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为我们基本上\n',
            '都不会使用厨房。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '倒是姐姐的男朋友\n',
            '乌尔斯偶尔会用，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_5C3')

    def _loc_55A(): pass

    label('loc_55A')

    ChrTalk(
        0x00FE,
        (
            '乌尔斯再过一会\n',
            '应该就会过来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '姐姐忙的时候他总是\n',
            '会把午餐送来，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且还会帮忙\n',
            '做扫除呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5C3(): pass

    label('loc_5C3')

    Jump('loc_C38')

    def _loc_5C6(): pass

    label('loc_5C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_8BB',
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_798',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0417, 3, 0x20BB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_714',
    )

    OP_62(0x00FE, 0x00000000, 1700, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x00FE, 0x0107, 0)

    ChrTalk(
        0x00FE,
        (
            '啊～提妲，\n',
            '真是好久不见了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难道你们\n',
            '今天也在帮博士的忙吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#560F啊、嗯～\n',
            '是呀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '乌缇你\n',
            '又在看家吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯～是呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '露依赛姐姐总是\n',
            '对什么事都充满兴趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '能乘坐上『埃尔赛尤』\n',
            '她好像特别兴奋呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是像个小孩子一样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#067F啊、啊哈哈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0417, 3, 0x20BB))

    Jump('loc_795')

    def _loc_714(): pass

    label('loc_714')

    ChrTalk(
        0x00FE,
        (
            '我姐姐虽然头脑聪明，\n',
            '但完全是小孩子脾气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算把房间收拾好了，\n',
            '马上又会恢复原样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '倒是提妲给人的感觉\n',
            '像个大人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_795(): pass

    label('loc_795')

    Jump('loc_8B8')

    def _loc_798(): pass

    label('loc_798')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_845',
    )

    ChrTalk(
        0x00FE,
        (
            '露依赛姐姐最近\n',
            '好像非常兴奋呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '能乘坐上『埃尔赛尤』\n',
            '她好像特别兴奋呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天也说要研究什么异变，\n',
            '一大早就离开家了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是像个小孩子一样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_8B8')

    def _loc_845(): pass

    label('loc_845')

    ChrTalk(
        0x00FE,
        (
            '姐姐虽然头脑聪明，\n',
            '但其实完全是小孩子脾气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '比起探明异变的原因，\n',
            '我倒是更想知道为什么\n',
            '家里总是一团乱糟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8B8(): pass

    label('loc_8B8')

    Jump('loc_C38')

    def _loc_8BB(): pass

    label('loc_8BB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_9A7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_918',
    )

    ChrTalk(
        0x00FE,
        (
            '啊啊～～真希望我姐姐\n',
            '早点嫁出去啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不然房间永远都\n',
            '不能恢复整洁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9A4')

    def _loc_918(): pass

    label('loc_918')

    ChrTalk(
        0x00FE,
        (
            '我姐姐因为工作上的事情\n',
            '到要塞去了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也就是说，如果现在把房间收拾好，\n',
            '就可以保持干净一阵子了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，有干劲了，\n',
            '加油做扫除！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_9A4(): pass

    label('loc_9A4')

    Jump('loc_C38')

    def _loc_9A7(): pass

    label('loc_9A7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_A0B',
    )

    ChrTalk(
        0x00FE,
        (
            '姐姐因为工作上的事情\n',
            '到要塞那边去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，真希望她能在出发前\n',
            '把房间收拾一下啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C38')

    def _loc_A0B(): pass

    label('loc_A0B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 7, 0x1417)),
            Expr.Return,
        ),
        'loc_B32',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0286, 3, 0x1433)),
            Expr.Return,
        ),
        'loc_A7D',
    )

    ChrTurnDirection(0x00FE, 0x0107, 0)

    ChrTalk(
        0x00FE,
        (
            '帮博士的忙…\n',
            '真的好厉害啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果是我姐姐的话就肯定不行～\n',
            '我可以１２０％的确定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B2F')

    def _loc_A7D(): pass

    label('loc_A7D')

    ChrTurnDirection(0x00FE, 0x0107, 0)

    ChrTalk(
        0x00FE,
        (
            '啊～提妲。\n',
            '今天也在帮博士的忙吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F啊、嗯～是呀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我们要去设置\n',
            '最新开发的观测装置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是吗～其实也只能如此呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可以帮到博士的人\n',
            '大概只有提妲了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0286, 3, 0x1433))

    def _loc_B2F(): pass

    label('loc_B2F')

    Jump('loc_C38')

    def _loc_B32(): pass

    label('loc_B32')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_B8C',
    )

    ChrTalk(
        0x00FE,
        (
            '在露依赛姐姐回来之前\n',
            '书就这样扔着就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次一定要让她\n',
            '自己整理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C38')

    def _loc_B8C(): pass

    label('loc_B8C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 0, 0x1408)),
            Expr.Return,
        ),
        'loc_C38',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_BEF',
    )

    ChrTalk(
        0x00FE,
        (
            '真是的～姐姐从来都\n',
            '不会整理房间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '她的男朋友乌尔斯先生\n',
            '为此也很辛苦呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C38')

    def _loc_BEF(): pass

    label('loc_BEF')

    ChrTalk(
        0x00FE,
        (
            '真讨厌～刚才的地震\n',
            '把书震落了一地～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '姐姐又不把它们\n',
            '收拾好～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_C38(): pass

    label('loc_C38')

    TalkEnd(0x0009)

    Return()

# id: 0x0007 offset: 0xC3C
@scena.Code('func_07_C3C')
def func_07_C3C():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_D2C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_CBC',
    )

    ChrTalk(
        0x00FE,
        (
            '不久后又要去王都\n',
            '和共和国的人商谈了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果输出工作这样发展下去的话，\n',
            '飞船产业的未来倒是很光明呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D29')

    def _loc_CBC(): pass

    label('loc_CBC')

    ChrTalk(
        0x00FE,
        (
            '最近利用飞船的\n',
            '合作越来越多，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是发展商业渠道的好机会。\n',
            '我也高兴得很啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '高兴得都想大喊了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_D29(): pass

    label('loc_D29')

    Jump('loc_EDA')

    def _loc_D2C(): pass

    label('loc_D2C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_DE9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_D91',
    )

    ChrTalk(
        0x00FE,
        (
            '等工作告一段落之后\n',
            '我准备去中央工房拜访。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那孩子一定\n',
            '给大家添了不少麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DE6')

    def _loc_D91(): pass

    label('loc_D91')

    ChrTalk(
        0x00FE,
        (
            '我的女儿进入中央工房\n',
            '工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然她的动机不正…\n',
            '但还是希望她能加油干。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_DE6(): pass

    label('loc_DE6')

    Jump('loc_EDA')

    def _loc_DE9(): pass

    label('loc_DE9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 0, 0x1408)),
            Expr.Return,
        ),
        'loc_EDA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_E44',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才我也忍不住\n',
            '大声惊叫了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '身为飞船商人，\n',
            '真是有些不好意思啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EDA')

    def _loc_E44(): pass

    label('loc_E44')

    ChrTalk(
        0x00FE,
        (
            '啊～在飞船坪的时候\n',
            '真是吓了一跳呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然脑子里明白不会有什么危险，\n',
            '但还是不由自主地大叫了起来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '身为飞船商人，\n',
            '真是有些不好意思啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_EDA(): pass

    label('loc_EDA')

    TalkEnd(0x000A)

    Return()

# id: 0x0008 offset: 0xEDE
@scena.Code('func_08_EDE')
def func_08_EDE():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_FCE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F79',
    )

    ChrTalk(
        0x00FE,
        (
            '为了重新展开研究工作，\n',
            '中央工房好像非常忙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '去做事务见习工作，\n',
            '对我女儿米优也有好处。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个孩子没有\n',
            '什么工作经验，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_FCB')

    def _loc_F79(): pass

    label('loc_F79')

    ChrTalk(
        0x00FE,
        (
            '为了重新展开研究工作，\n',
            '中央工房好像非常忙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '能长点见识\n',
            '对她也有好处。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FCB(): pass

    label('loc_FCB')

    Jump('loc_15A2')

    def _loc_FCE(): pass

    label('loc_FCE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_10F3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_107E',
    )

    ChrTalk(
        0x00FE,
        (
            '导力器瘫痪之后，\n',
            '城里发生了很大的骚乱呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一群人都围到了中央工房，\n',
            '工房长也被吓得很惨。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次的情况和上一次很像，\n',
            '大概又是同一伙犯人做的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_10F0')

    def _loc_107E(): pass

    label('loc_107E')

    ChrTalk(
        0x00FE,
        (
            '虽然搞破坏的那些家伙难逃其罪，\n',
            '但我们自己其实也有责任。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '做实验引起不良异变的事情\n',
            '也有过不止一次两次了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10F0(): pass

    label('loc_10F0')

    Jump('loc_15A2')

    def _loc_10F3(): pass

    label('loc_10F3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_1204',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_115C',
    )

    ChrTalk(
        0x00FE,
        (
            '呼～今天总算把\n',
            '丈夫和女儿平安送走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样在爷爷回来之前\n',
            '可以好好休息一下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1201')

    def _loc_115C(): pass

    label('loc_115C')

    ChrTalk(
        0x00FE,
        (
            '呼～今天总算把\n',
            '丈夫和女儿平安送走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样在爷爷回来之前\n',
            '可以好好休息一下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我家的爷爷在白天\n',
            '总是泡在酒馆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但他却并不喝酒，\n',
            '真是个怪人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_1201(): pass

    label('loc_1201')

    Jump('loc_15A2')

    def _loc_1204(): pass

    label('loc_1204')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_12EB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_126D',
    )

    ChrTalk(
        0x00FE,
        (
            '听我老公说，最近和帝国那边\n',
            '的商谈好像增多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难道是和帝国的关系\n',
            '有了好转吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12E8')

    def _loc_126D(): pass

    label('loc_126D')

    ChrTalk(
        0x00FE,
        (
            '我老公的职业是飞船交易\n',
            '的中介商人，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近不知为什么总是出差。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不久前才刚从柏斯回来，\n',
            '这次马上又要去王都。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_12E8(): pass

    label('loc_12E8')

    Jump('loc_15A2')

    def _loc_12EB(): pass

    label('loc_12EB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 7, 0x1417)),
            Expr.Return,
        ),
        'loc_1407',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_134E',
    )

    ChrTalk(
        0x00FE,
        (
            '那个孩子能认真工作\n',
            '真是让我意外。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也许是隐藏的工作欲望\n',
            '终于被激发了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1404')

    def _loc_134E(): pass

    label('loc_134E')

    ChrTurnDirection(0x00FE, 0x0107, 0)

    ChrTalk(
        0x00FE,
        (
            '啊～提妲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我女儿有没有\n',
            '认真工作呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#560F啊～米优一直\n',
            '很努力工作呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '总是东奔西走忙个不停。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿～？那可真是有点意外啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我还以为她会\n',
            '经常偷懒呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_1404(): pass

    label('loc_1404')

    Jump('loc_15A2')

    def _loc_1407(): pass

    label('loc_1407')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_14DD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_146A',
    )

    ChrTalk(
        0x00FE,
        (
            '我女儿米优\n',
            '去中央工房帮忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '动机暂且不说，总之\n',
            '对工作有兴趣就是好事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14DA')

    def _loc_146A(): pass

    label('loc_146A')

    ChrTalk(
        0x00FE,
        (
            '我女儿米优\n',
            '去中央工房帮忙了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '她似乎本想当\n',
            '接待处的小姐的…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '算了，也是个接触社会\n',
            '的好机会…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_14DA(): pass

    label('loc_14DA')

    Jump('loc_15A2')

    def _loc_14DD(): pass

    label('loc_14DD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 0, 0x1408)),
            Expr.Return,
        ),
        'loc_15A2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_153B',
    )

    ChrTalk(
        0x00FE,
        (
            '话说回来，地震真是好久没遇到了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '已经都快把那种东西\n',
            '给忘掉了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15A2')

    def _loc_153B(): pass

    label('loc_153B')

    ChrTalk(
        0x00FE,
        (
            '我很讨厌地震呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '脚下摇晃个不停，\n',
            '真是让人不舒服。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，而且连飞船\n',
            '也都无法乘坐了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_15A2(): pass

    label('loc_15A2')

    TalkEnd(0x000B)

    Return()

# id: 0x0009 offset: 0x15A6
@scena.Code('func_09_15A6')
def func_09_15A6():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_16B9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_160E',
    )

    ChrTalk(
        0x00FE,
        (
            '地震倒是无所谓，\n',
            '还是互不侵犯条约比较重要。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '毕竟是关系到王国未来\n',
            '的问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16B6')

    def _loc_160E(): pass

    label('loc_160E')

    ChrTalk(
        0x00FE,
        (
            '嗯，再过不久就是\n',
            '互不侵犯条约的签字仪式了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那次的战争已经过去十年了…\n',
            '也是该和帝国清算一下历史问题的时候了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果能顺利签署条约\n',
            '自然是最好不过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_16B6(): pass

    label('loc_16B6')

    Jump('loc_19F8')

    def _loc_16B9(): pass

    label('loc_16B9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_17D9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1730',
    )

    ChrTalk(
        0x00FE,
        (
            '店长耶鲁克\n',
            '购进了新型枪……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们可以去看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果能找到优秀的射手\n',
            '帮忙测试一下就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17D6')

    def _loc_1730(): pass

    label('loc_1730')

    ChrTalk(
        0x00FE,
        (
            '前几天中央工房的加鲁诺\n',
            '给我看了新型的导力枪呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然细微部分还有点粗糙，\n',
            '但驱动部分却有着革命性的改进。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果好好测试一下，\n',
            '以后很可能会成为热销品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_17D6(): pass

    label('loc_17D6')

    Jump('loc_19F8')

    def _loc_17D9(): pass

    label('loc_17D9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_1922',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_188B',
    )

    ChrTalk(
        0x00FE,
        (
            '我经营的武器店一向\n',
            '不贩卖最新型的武器产品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以前我们一直遵循这个方针，\n',
            '也遭到了很多年轻人的不解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，他们现在也理解了，\n',
            '并且也认同了我的想法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_191F')

    def _loc_188B(): pass

    label('loc_188B')

    ChrTalk(
        0x00FE,
        (
            '我经营的武器店一向\n',
            '不贩卖最新型的武器产品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '新型的武器，其性能\n',
            '再怎么说也不是很稳定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只有经过一段时间的测试\n',
            '才能明白其中的缺陷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_191F(): pass

    label('loc_191F')

    Jump('loc_19F8')

    def _loc_1922(): pass

    label('loc_1922')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 0, 0x1408)),
            Expr.Return,
        ),
        'loc_19F8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_198B',
    )

    ChrTalk(
        0x00FE,
        (
            '我在蔡斯市内\n',
            '经营武器店，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就是游击士协会对面的那家店，\n',
            '有机会的话多来光顾吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19F8')

    def _loc_198B(): pass

    label('loc_198B')

    ChrTalk(
        0x00FE,
        (
            '嗯，好像没有余震了，\n',
            '店应该不要紧吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过真奇怪，竟然会有地震。\n',
            '利贝尔可是很少发生地震的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_19F8(): pass

    label('loc_19F8')

    TalkEnd(0x000C)

    Return()

# id: 0x000A offset: 0x19FC
@scena.Code('func_0A_19FC')
def func_0A_19FC():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_1AFC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A9B',
    )

    ChrTalk(
        0x00FE,
        (
            '导力器不能用了，\n',
            '我就买来了固形燃料。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '『贝尔杂货店』\n',
            '卖的东西真是齐全啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有这么商品齐全的店在附近，\n',
            '实在是让人很安心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    Jump('loc_1AF9')

    def _loc_1A9B(): pass

    label('loc_1A9B')

    ChrTalk(
        0x00FE,
        (
            '导力器不能用了，\n',
            '我就买来了固形燃料。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然火力有些弱，\n',
            '但也可以好好练习一下烹饪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AF9(): pass

    label('loc_1AF9')

    Jump('loc_1B78')

    def _loc_1AFC(): pass

    label('loc_1AFC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1B78',
    )

    ChrTalk(
        0x00FE,
        (
            '老公带着温丝\n',
            '去中央工房了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说是要去顶楼\n',
            '观察传闻中的浮游物体…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么可怕的东西\n',
            '确实让人无法不在意吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B78(): pass

    label('loc_1B78')

    TalkEnd(0x00FE)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

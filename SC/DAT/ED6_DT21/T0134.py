import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0134_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0134   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0134.x'
    header.mapIndex       = 3
    header.bgm            = 84
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T0134_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
        ('ED6_DT07/CH01400._CH', 'ED6_DT07/CH01400P._CP'),
        ('ED6_DT07/CH02350._CH', 'ED6_DT07/CH02350P._CP'),
        ('ED6_DT07/CH01410._CH', 'ED6_DT07/CH01410P._CP'),
        ('ED6_DT07/CH01500._CH', 'ED6_DT07/CH01500P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
    ]

# id: 0x10001 offset: 0xDA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '迪拜恩教区长',
            x                   = -14740,
            z                   = 0,
            y                   = 43530,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '克劳斯市长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '修女梅',
            x                   = -16830,
            z                   = 0,
            y                   = 42890,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0111,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '矿工皮尔姆',
            x                   = 55350,
            z                   = 0,
            y                   = 46550,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0111,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '矿工海涅',
            x                   = 56050,
            z                   = 0,
            y                   = 40700,
            direction           = 358,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '阿鲁姆',
            x                   = 64000,
            z                   = 0,
            y                   = 47270,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0111,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '艾娅莉',
            x                   = 64000,
            z                   = 0,
            y                   = 48170,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0111,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '目标用照相机',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0080,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x1DA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x1DA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x1DA
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x1DA
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.Eval, "OP_29(0x0072, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x0072, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0072, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x0234, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_20D',
    )

    ChrClearFlags(0x000E, 0x0010)
    ChrClearFlags(0x000D, 0x0010)

    Jump('loc_21C')

    def _loc_20D(): pass

    label('loc_20D')

    If(
        (
            (Expr.Eval, "OP_29(0x0072, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_21C',
    )

    ChrClearFlags(0x000E, 0x0010)

    def _loc_21C(): pass

    label('loc_21C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_233',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x51),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    Event(0, func_09_A1F)

    def _loc_233(): pass

    label('loc_233')

    Return()

# id: 0x0001 offset: 0x234
@scena.Code('func_01_234')
def func_01_234():
    Return()

# id: 0x0002 offset: 0x235
@scena.Code('func_02_235')
def func_02_235():
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
        'loc_25A',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_39C')

    def _loc_25A(): pass

    label('loc_25A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_273',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_39C')

    def _loc_273(): pass

    label('loc_273')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_28C',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_39C')

    def _loc_28C(): pass

    label('loc_28C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2A5',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_39C')

    def _loc_2A5(): pass

    label('loc_2A5')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2BE',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_39C')

    def _loc_2BE(): pass

    label('loc_2BE')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2D7',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_39C')

    def _loc_2D7(): pass

    label('loc_2D7')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2F0',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_39C')

    def _loc_2F0(): pass

    label('loc_2F0')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_309',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_39C')

    def _loc_309(): pass

    label('loc_309')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_322',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_39C')

    def _loc_322(): pass

    label('loc_322')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_33B',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_39C')

    def _loc_33B(): pass

    label('loc_33B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_354',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_39C')

    def _loc_354(): pass

    label('loc_354')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_36D',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_39C')

    def _loc_36D(): pass

    label('loc_36D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_386',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_39C')

    def _loc_386(): pass

    label('loc_386')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_39C',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_39C(): pass

    label('loc_39C')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3B1',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_39C')

    def _loc_3B1(): pass

    label('loc_3B1')

    Return()

# id: 0x0003 offset: 0x3B2
@scena.Code('func_03_3B2')
def func_03_3B2():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            Expr.Return,
        ),
        'loc_536',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_43F',
    )

    ChrTalk(
        0x0008,
        (
            '我也想尽快联络\n',
            '王都的大圣堂。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '那边文献也很丰富，\n',
            '也有了解各地地方病的神父。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '说不定能找到\n',
            '什么治疗的线索。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_536')

    def _loc_43F(): pass

    label('loc_43F')

    ChrTalk(
        0x0008,
        (
            '教会秘传的苏醒法\n',
            '都没用……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '说明此次的昏睡事件不是\n',
            '由药物和疾病引起的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '总之我准备先再查阅一遍\n',
            '手头的医学书，\n',
            '老实说我也不是很期待有什么结果。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '呼，看来还是尽快\n',
            '联络王都的大圣堂比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '等归纳好病例的报告\n',
            '就赶紧准备吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_536(): pass

    label('loc_536')

    TalkEnd(0x0008)

    Return()

# id: 0x0004 offset: 0x53A
@scena.Code('func_04_53A')
def func_04_53A():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            Expr.Return,
        ),
        'loc_583',
    )

    ChrTalk(
        0x00FE,
        (
            '空之女神啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望被睡眠迷住了的大家\n',
            '能够赶快醒来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_583(): pass

    label('loc_583')

    TalkEnd(0x000A)

    Return()

# id: 0x0005 offset: 0x587
@scena.Code('func_05_587')
def func_05_587():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            Expr.Return,
        ),
        'loc_61F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_5D0',
    )

    ChrTalk(
        0x00FE,
        (
            '深深感谢女神保佑我\n',
            '今天的工作也安全地完成了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_61F')

    def _loc_5D0(): pass

    label('loc_5D0')

    ChrTalk(
        0x00FE,
        (
            '多亏了女神，\n',
            '今天的工作也安全地完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请您明天也能\n',
            '保佑我们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_61F(): pass

    label('loc_61F')

    TalkEnd(0x000B)

    Return()

# id: 0x0006 offset: 0x623
@scena.Code('func_06_623')
def func_06_623():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            Expr.Return,
        ),
        'loc_71C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_685',
    )

    ChrTalk(
        0x00FE,
        (
            '皮尔姆那家伙……\n',
            '要祈祷到什么时候？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他怎么不想想\n',
            '我还在旁边等着呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_71C')

    def _loc_685(): pass

    label('loc_685')

    ChrTalk(
        0x00FE,
        (
            '皮尔姆那家伙……\n',
            '要祈祷到什么时候？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他怎么不想想\n',
            '我还在旁边等着呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊～太晚的话\n',
            '酒馆要关门了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……真是的，我一个人\n',
            '去吃算了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_71C(): pass

    label('loc_71C')

    TalkEnd(0x000C)

    Return()

# id: 0x0007 offset: 0x720
@scena.Code('func_07_720')
def func_07_720():
    TalkBegin(0x000D)

    If(
        (
            (Expr.Eval, "OP_29(0x0072, 0x00, 0x02)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0072, 0x00, 0x10)"),
            Expr.Or,
            (Expr.Eval, "OP_29(0x0072, 0x00, 0x40)"),
            Expr.Or,
            (Expr.Eval, "OP_29(0x0072, 0x00, 0x08)"),
            (Expr.Eval, "OP_40(0x0234, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Nez64,
            Expr.Or,
            Expr.Return,
        ),
        'loc_942',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_76D',
    )

    ChrTalk(
        0x00FE,
        (
            '啊啊～艾娅莉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_93F')

    def _loc_76D(): pass

    label('loc_76D')

    If(
        (
            (Expr.Eval, "OP_29(0x0072, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x0072, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0072, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_8C8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_7D5',
    )

    ChrTalk(
        0x00FE,
        (
            '那么，游击士。\n',
            '戒指的事拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是有什么情况\n',
            '请再来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8C5')

    def _loc_7D5(): pass

    label('loc_7D5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_823',
    )

    ChrTalk(
        0x00FE,
        (
            '那么，游击士。\n',
            '戒指的事拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是有什么情况\n',
            '请再来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8C5')

    def _loc_823(): pass

    label('loc_823')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '啊，游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎、怎么样了？\n',
            '调查进行得如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F嗯，还在继续啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '也许再等一会\n',
            '就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那、那样啊…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，明白了。\n',
            '我会一直等的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8C5(): pass

    label('loc_8C5')

    Jump('loc_93F')

    def _loc_8C8(): pass

    label('loc_8C8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            Expr.Return,
        ),
        'loc_93F',
    )

    ChrTalk(
        0x00FE,
        (
            '今天也看不见星星……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过只要有你在，\n',
            '我就一点儿也不寂寞。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为我所寻找的星星\n',
            '就是你啊，艾娅莉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_93F(): pass

    label('loc_93F')

    Jump('loc_96A')

    def _loc_942(): pass

    label('loc_942')

    If(
        (
            (Expr.Eval, "OP_29(0x0072, 0x00, 0x08)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_966',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0072, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_95F',
    )

    Call(1, 0x0001)

    Jump('loc_963')

    def _loc_95F(): pass

    label('loc_95F')

    Call(1, 0x0000)

    def _loc_963(): pass

    label('loc_963')

    Jump('loc_96A')

    def _loc_966(): pass

    label('loc_966')

    Call(1, 0x0003)
    def _loc_96A(): pass

    label('loc_96A')

    TalkEnd(0x000D)

    Return()

# id: 0x0008 offset: 0x96E
@scena.Code('func_08_96E')
def func_08_96E():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_98B',
    )

    ChrTalk(
        0x00FE,
        (
            '阿鲁姆……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A1B')

    def _loc_98B(): pass

    label('loc_98B')

    If(
        (
            (Expr.Eval, "OP_29(0x0072, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x0072, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0072, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_9ED',
    )

    ChrTalk(
        0x00FE,
        (
            '我们在这里等着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然是很艰难的委托，\n',
            '但请努力坚持一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A1B')

    def _loc_9ED(): pass

    label('loc_9ED')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            Expr.Return,
        ),
        'loc_A1B',
    )

    ChrTalk(
        0x00FE,
        (
            '呵呵，阿鲁姆\n',
            '你真是个浪漫主义者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A1B(): pass

    label('loc_A1B')

    TalkEnd(0x000E)

    Return()

# id: 0x0009 offset: 0xA1F
@scena.Code('func_09_A1F')
def func_09_A1F():
    EventBegin(0x00)
    OP_DB()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_A40',
    )

    Call(0, 0x000A)
    FadeIn(0, 0)
    Call(0, 0x000B)

    def _loc_A40(): pass

    label('loc_A40')

    TerminateThread(0x0008, 0x00)
    ChrSetPos(0x0008, -17390, 0, 42890, 90)
    ChrSetPos(0x0101, -15830, 0, 42280, 270)
    ChrSetPos(0x0103, -15950, 0, 43470, 270)
    ChrSetFlags(0x000A, 0x0080)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_ABF',
    )

    ChrSetPos(0x0009, -15850, 0, 45570, 180)
    ChrSetPos(0x00F8, -14610, 0, 43470, 270)
    ChrSetPos(0x00F9, -14600, 0, 42200, 270)

    Jump('loc_AF2')

    def _loc_ABF(): pass

    label('loc_ABF')

    ChrSetPos(0x0009, -16020, 0, 45150, 180)
    ChrSetPos(0x00F8, -14600, 0, 42200, 270)
    ChrSetPos(0x00F9, -14610, 0, 43470, 270)

    def _loc_AF2(): pass

    label('loc_AF2')

    ChrTurnDirection(0x00F8, 0x0008, 0)
    ChrTurnDirection(0x00F9, 0x0008, 0)
    ChrClearFlags(0x0009, 0x0080)
    CameraMove(-16630, 3000, 43560, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    FadeIn(1000, 0)
    CameraMove(-16630, 0, 43560, 2000)
    OP_0D()
    Sleep(500)

    OP_DC()

    ChrTalk(
        0x0008,
        (
            '#1080281379V#5P各位病人的家里都去看了一遍，\n',
            '果然所有人的症状都一致……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080281380V#5P呼吸也很稳定，\n',
            '瞳孔也没有异常。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080281381V#5P几乎就像是睡着了一样，\n',
            '所以应该不会立即恶化吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0340281382V#603F是、是吗……\n',
            '可以说是不幸中的万幸了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080281383V#5P可是这么一直沉睡下去的话\n',
            '体力肯定会不支的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080281384V#5P得赶紧想出\n',
            '对策来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0340281385V#602F嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281386V#1003F#6P…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0D25')
    def lambda_0D25():
        ChrTurnDirection(0x00F8, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_0D25)

    Sleep(100)

    @scena.Lambda('lambda_0D38')
    def lambda_0D38():
        ChrTurnDirection(0x00F9, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_0D38)

    Sleep(100)

    ChrTurnDirection(0x0103, 0x0101, 400)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_DAC',
    )

    ChrTalk(
        0x0107,
        (
            '#0070281387V#065F#4P姐、姐姐，你没事吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070281388V你的脸色好像很差……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F0D')

    def _loc_DAC(): pass

    label('loc_DAC')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E00',
    )

    ChrTalk(
        0x0106,
        (
            '#0050281389V#552F#4P喂……你没事吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050281390V脸色这么差？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F0D')

    def _loc_E00(): pass

    label('loc_E00')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E5D',
    )

    ChrTalk(
        0x0104,
        (
            '#0040281391V#032F#4P咦？你没事吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040281392V脸色好像相当\n',
            '不好呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F0D')

    def _loc_E5D(): pass

    label('loc_E5D')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_EBE',
    )

    ChrTalk(
        0x0105,
        (
            '#0060281393V#043F#4P艾丝蒂尔……\n',
            '那个，你没事吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060281394V你脸色很差。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F0D')

    def _loc_EBE(): pass

    label('loc_EBE')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F0D',
    )

    ChrTalk(
        0x0108,
        (
            '#0080281395V#572F#4P喂，你没事吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080281396V脸色很差啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F0D(): pass

    label('loc_F0D')

    ChrTurnDirection(0x0101, 0x00F8, 400)

    ChrTalk(
        0x0101,
        (
            '#0010281397V#1026F#5P啊，嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281398V#1007F想不到连伊莉莎的妈妈和\n',
            '鲁克也会倒下来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281399V……所以感到有点吃惊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030281400V#524F#2P艾丝蒂尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281401V如果觉得不舒服\n',
            '你也可以返回协会？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281402V还是说回家歇着？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010281403V#1025F#6P不……\n',
            '不能泄气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 400)

    @scena.Lambda('lambda_1054')
    def lambda_1054():
        ChrTurnDirection(0x0103, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_1054)

    @scena.Lambda('lambda_1062')
    def lambda_1062():
        ChrTurnDirection(0x00F9, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_1062)

    ChrTurnDirection(0x00F8, 0x0008, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010281404V#1002F#6P那么，教区长先生，\n',
            '昏睡的原因知道了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080281405V#5P很遗憾，现在还不能确定……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080281406V#5P不过，连教会秘传的苏醒法\n',
            '也没起作用，\n',
            '应该不是毒和疾病造成的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080281407V#5P如果一定要说的话，\n',
            '好像是灵魂被某种东西囚禁了……\n',
            '给人的印象就是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281408V#1002F#6P灵魂被某种东西囚禁……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030281409V#522F#4P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x0103,
        (
            '#0030281410V#022F#2P总之还是先走访一下\n',
            '昏睡者的家比较好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281411V他们究竟是在\n',
            '何种情况下进入昏睡状态的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281412V通过询问家属这方面的情况，\n',
            '说不定能发现些什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0009, 400)

    ChrTalk(
        0x0101,
        (
            '#0010200077V#1004F#6P啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281414V#1002F嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0340281415V#603F艾丝蒂尔、雪拉扎德。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_132E')
    def lambda_132E():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_132E)

    Sleep(100)

    @scena.Lambda('lambda_1341')
    def lambda_1341():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_1341)

    Sleep(100)

    ChrSetDirection(0x00F9, 0, 400)

    ChrTalk(
        0x0009,
        (
            '#0340281416V#602F洛连特市政府正式委托\n',
            '协会调查此次的事件。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340281417V希望你们能查出原因，\n',
            '消除大家的不安。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281418V#1006F#6P嗯……请放心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030281419V#020F#6P我们会尽一份薄力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_21()
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/T0101._SN', 117, 0, 0)
    IdleLoop()

    Return()

# id: 0x000A offset: 0x143D
@scena.Code('func_0A_143D')
def func_0A_143D():
    FadeOut(0, 0, -1)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x09, 0xFF)

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
        (0x00000000, 'loc_14BA'),
        (0x00000001, 'loc_14C0'),
        (-1, 'loc_14C6'),
    )

    def _loc_14BA(): pass

    label('loc_14BA')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_14C6')

    def _loc_14C0(): pass

    label('loc_14C0')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_14C6')

    def _loc_14C6(): pass

    label('loc_14C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_14D4',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_14D8')

    def _loc_14D4(): pass

    label('loc_14D4')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_14D8(): pass

    label('loc_14D8')

    Return()

# id: 0x000B offset: 0x14D9
@scena.Code('func_0B_14D9')
def func_0B_14D9():
    MapClearFlags(0x00000001)
    CameraMove(106730, -1920, 53920, 0)
    Sleep(100)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['雪拉扎德'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            ChrTable['提妲'],
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

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0)
    Sleep(1000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

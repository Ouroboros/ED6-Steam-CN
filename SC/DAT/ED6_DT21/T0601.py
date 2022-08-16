import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0601_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0601   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0601.x'
    header.mapIndex       = 17
    header.bgm            = 16
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
            word_3A         = 17,
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
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT27/CH03080._CH', 'ED6_DT27/CH03080P._CP'),
        ('ED6_DT29/CH12581._CH', 'ED6_DT29/CH12581P._CP'),
        ('ED6_DT07/CH01310._CH', 'ED6_DT07/CH01310P._CP'),
        ('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP'),
    ]

# id: 0x10001 offset: 0xDA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '士兵塞维安',
            x                   = -940,
            z                   = 7250,
            y                   = -94770,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '古利乌副队长',
            x                   = -5540,
            z                   = 7250,
            y                   = -68220,
            direction           = 266,
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
            name                = '凯文神父',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '目标探索者',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '目标探索者',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '古利乌副队长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
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
        ScenaEventData(
            x           = -5700,
            y           = -2000,
            z           = -21100,
            range       = 3800,
            dword_10    = 0x00002328,
            dword_14    = 0xFFFFBA14,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000006,
        ),
    )

# id: 0x10004 offset: 0x1BA
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x1BA
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1DC',
    )

    ChrSetPos(0x0008, -2980, 7250, -67430, 335)
    CreateThread(0x0008, 0x00, 0x00, func_02_286)

    Jump('loc_201')

    def _loc_1DC(): pass

    label('loc_1DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1E6',
    )

    Jump('loc_201')

    def _loc_1E6(): pass

    label('loc_1E6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 0, 0x1638)),
            Expr.Return,
        ),
        'loc_1F5',
    )

    ChrClearFlags(0x0009, 0x0080)

    Jump('loc_201')

    def _loc_1F5(): pass

    label('loc_1F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 6, 0x1636)),
            Expr.Return,
        ),
        'loc_201',
    )

    ChrSetFlags(0x0008, 0x0080)

    def _loc_201(): pass

    label('loc_201')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_21D',
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
    MapSetFlags(0x10000000)
    Event(0, func_07_E47)

    def _loc_21D(): pass

    label('loc_21D')

    ExecExpressionWithValue(
        0x000B,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0001 offset: 0x240
@scena.Code('func_01_240')
def func_01_240():
    OP_16(0x02, 4000, -129000, -166000, 2293778)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 7, 0x1637)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_27C',
    )

    OP_B1('t0601_y')
    OP_C4(0x00, 0x00000002)
    OP_7E(-1000, 500, 1000, 150, 0)

    Jump('loc_285')

    def _loc_27C(): pass

    label('loc_27C')

    OP_B1('t0601_n')

    def _loc_285(): pass

    label('loc_285')

    Return()

# id: 0x0002 offset: 0x286
@scena.Code('func_02_286')
def func_02_286():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_29B',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_286')

    def _loc_29B(): pass

    label('loc_29B')

    Return()

# id: 0x0003 offset: 0x29C
@scena.Code('func_03_29C')
def func_03_29C():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2BF',
    )

    OP_8D(0x00FE, -3140, -97580, 1480, -73120, 3000)

    Jump('func_03_29C')

    def _loc_2BF(): pass

    label('loc_2BF')

    Return()

# id: 0x0004 offset: 0x2C0
@scena.Code('func_04_2C0')
def func_04_2C0():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_3D9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_388',
    )

    ChrTalk(
        0x00FE,
        (
            '那个浮游岛好像是悬浮在\n',
            '相当高的地方……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这么说来，帝国军肯定\n',
            '也在监视它吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '出现在王国领空的\n',
            '谜样巨大飞行物体……吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不，不要有什么\n',
            '不切实际的误解就好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_3D6')

    def _loc_388(): pass

    label('loc_388')

    ChrTalk(
        0x00FE,
        (
            '帝国军应该也在\n',
            '监视那座岛吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不，不要有什么\n',
            '不切实际的误解就好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3D6(): pass

    label('loc_3D6')

    Jump('loc_CB5')

    def _loc_3D9(): pass

    label('loc_3D9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_53E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4D3',
    )

    ChrTalk(
        0x00FE,
        (
            '那天晚上我看见了哦。\n',
            '浮游岛出现的瞬间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像太阳升起一般，\n',
            '一下子照亮天空……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '等清醒过来那座岛\n',
            '就在天空正中挂着了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然难以置信，\n',
            '但真的是从什么都没有的地方突然出现的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像很久以前\n',
            '就已经在那里似的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_53B')

    def _loc_4D3(): pass

    label('loc_4D3')

    ChrTalk(
        0x00FE,
        (
            '那座浮游岛，\n',
            '真的是从什么都没有的地方突然出现的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '直到亲眼看习惯之前，\n',
            '一直都觉得难以置信呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_53B(): pass

    label('loc_53B')

    Jump('loc_CB5')

    def _loc_53E(): pass

    label('loc_53E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_620',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_59F',
    )

    ChrTalk(
        0x00FE,
        (
            '晴空万里的蓝天\n',
            '和浩瀚无边的大森林……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这种对比\n',
            '正是洛连特景色的魅力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_61D')

    def _loc_59F(): pass

    label('loc_59F')

    ChrTalk(
        0x00FE,
        (
            '晴空万里的蓝天\n',
            '和浩瀚无边的大森林……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，洛连特\n',
            '就是要这样才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '天空与大地的对比\n',
            '正是这里景色的亮点嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_61D(): pass

    label('loc_61D')

    Jump('loc_CB5')

    def _loc_620(): pass

    label('loc_620')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_708',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_679',
    )

    ChrTalk(
        0x00FE,
        (
            '要是有那个雾，\n',
            '周围都看不清了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们要是出城\n',
            '也要多加注意哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_705')

    def _loc_679(): pass

    label('loc_679')

    ChrTalk(
        0x00FE,
        (
            '今天也没什么异常……\n',
            '呼，虽然跟队长报告过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '洛连特那边白茫茫的一片，\n',
            '巡逻也没什么意义呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们要是出城\n',
            '也要多加注意哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_705(): pass

    label('loc_705')

    Jump('loc_CB5')

    def _loc_708(): pass

    label('loc_708')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_7E8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_769',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯～雾好像\n',
            '比昨天更浓了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我在这里工作也很久了，\n',
            '这还是头一次遇到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7E5')

    def _loc_769(): pass

    label('loc_769')

    ChrTalk(
        0x00FE,
        (
            '嗯～雾好像\n',
            '比昨天更浓了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '格兰赛尔那边的空气\n',
            '今天也很清新……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我在这里工作也很久了，\n',
            '这还是头一次遇到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_7E5(): pass

    label('loc_7E5')

    Jump('loc_CB5')

    def _loc_7E8(): pass

    label('loc_7E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_8D6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_84F',
    )

    ChrTalk(
        0x00FE,
        (
            '今天洛连特这边的景色\n',
            '都笼罩在白色中了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '平时森林鲜艳的绿色\n',
            '可是很耀眼的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8D3')

    def _loc_84F(): pass

    label('loc_84F')

    ChrTalk(
        0x00FE,
        (
            '王都那边是大晴天，\n',
            '虽然风景优美……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但另一方面，洛连特这边\n',
            '却笼罩在白色之中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '平时森林鲜艳的绿色\n',
            '可是很耀眼的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_8D3(): pass

    label('loc_8D3')

    Jump('loc_CB5')

    def _loc_8D6(): pass

    label('loc_8D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_946',
    )

    ChrTalk(
        0x00FE,
        (
            '结果，『结社』和特务兵\n',
            '那些家伙之后都没出现呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '王都有亲卫队\n',
            '和游击士守护嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '谢谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CB5')

    def _loc_946(): pass

    label('loc_946')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 0, 0x1638)),
            Expr.Return,
        ),
        'loc_99E',
    )

    ChrTalk(
        0x00FE,
        (
            '『结社』的事情我们\n',
            '也才刚刚听说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之要赶快吧？\n',
            '这里就交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CB5')

    def _loc_99E(): pass

    label('loc_99E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Return,
        ),
        'loc_A0B',
    )

    ChrTalk(
        0x00FE,
        (
            '情报部的特务兵吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然现在被追捕，\n',
            '但以前可是精英部队啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要打起精神好好警戒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CB5')

    def _loc_A0B(): pass

    label('loc_A0B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_C5C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02CA, 2, 0x1652)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C05',
    )

    ChrTalk(
        0x00FE,
        (
            '呀，欢迎来到格鲁纳门。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x012F, 0x0008, 400)

    ChrTalk(
        0x012F,
        (
            '#264F呼呼，记得在王都南边\n',
            '也有相似的建筑物啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x012F, 400)

    ChrTalk(
        0x00FE,
        (
            '哈哈，这个建筑物呢，\n',
            '是包围这个地区整体的长城、\n',
            '亚宁堡的一部分。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '小妹妹看到的长城\n',
            '是南边的圣海姆门吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#260F啊……明白啦，\n',
            '是这么回事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x012F, 0x0101, 400)

    ChrTalk(
        0x0101,
        (
            '#1007F呼～啊，景色又好，\n',
            '森林吹来的风也好舒服…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1006F我好像\n',
            '挺喜欢这个地方的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#261F呼嘿嘿，姐姐真是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#265F不过，真是巧呢……\n',
            '玲也非常喜欢这个地方呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈，和圣海姆门不一样，\n',
            '来的人很少、\n',
            '是个很安静的地方呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x02CA, 2, 0x1652))

    Jump('loc_C59')

    def _loc_C05(): pass

    label('loc_C05')

    ChrTalk(
        0x00FE,
        (
            '这个格鲁纳门\n',
            '和圣海姆门不一样，\n',
            '来的人很少吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以应该是个安静的地方呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C59(): pass

    label('loc_C59')

    Jump('loc_CB5')

    def _loc_C5C(): pass

    label('loc_C5C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_CB5',
    )

    ChrTalk(
        0x00FE,
        (
            '这里还是那么大，\n',
            '警备起来很辛苦呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好风景和清爽的风\n',
            '多少也算是补偿了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CB5(): pass

    label('loc_CB5')

    TalkEnd(0x0008)

    Return()

# id: 0x0005 offset: 0xCB9
@scena.Code('func_05_CB9')
def func_05_CB9():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 0, 0x1638)),
            Expr.Return,
        ),
        'loc_D4B',
    )

    ChrTalk(
        0x00FE,
        (
            '袭击你们的机械\n',
            '说不定是那『结社』的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不只是周游道，\n',
            '这一带也出现了的话，\n',
            '就必须加强警戒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们赶快\n',
            '回王都协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D4B(): pass

    label('loc_D4B')

    TalkEnd(0x0009)

    Return()

# id: 0x0006 offset: 0xD4F
@scena.Code('func_06_D4F')
def func_06_D4F():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 7, 0x1637)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 0, 0x1638)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_D5C',
    )

    Return()

    def _loc_D5C(): pass

    label('loc_D5C')

    EventBegin(0x00)
    Fade(1000)
    FormationAddMember(ChrTable['凯文神父'], 0xF7, 0xFF)
    ChrSetPos(0x0109, 3570, 7250, -68040, 90)
    ChrSetPos(0x0101, -780, 7250, -45000, 180)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3250, 0)
    OP_6C(145000, 0)
    OP_6E(262, 0)
    OP_69(0x0101, 0)
    OP_6A(0x0101)
    Sleep(100)

    ChrWalkTo(0x0101, -600, 7250, -54970, 3000, 0x00)
    OP_6A(0x00FF)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    CameraMove(-1190, 7250, -61210, 2000)

    ChrTalk(
        0x0101,
        (
            '#0010260974V#1025F#5P……啊………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T4103._SN', 104, 0, 0)
    IdleLoop()

    Return()

# id: 0x0007 offset: 0xE47
@scena.Code('func_07_E47')
def func_07_E47():
    EventBegin(0x00)
    FormationAddMember(ChrTable['凯文神父'], 0xF7, 0xFF)
    ChrSetStatus(ChrTable['凯文神父'], 0x00, 55)
    ChrSetStatus(ChrTable['凯文神父'], 0xFE, 0)
    ChrSetStatus(ChrTable['凯文神父'], 0x05, 90)
    EquipCmd(ChrTable['凯文神父'], ItemTable['气弓'], 0xFF)
    EquipCmd(ChrTable['凯文神父'], ItemTable['强化夹克'], 0xFF)
    EquipCmd(ChrTable['凯文神父'], ItemTable['纤维靴'], 0xFF)
    EquipCmd(ChrTable['凯文神父'], ItemTable['行动力１'], 0x00)
    EquipCmd(ChrTable['凯文神父'], ItemTable['ＥＰ２'], 0x01)
    EquipCmd(ChrTable['凯文神父'], ItemTable['ＨＰ２'], 0x02)
    EquipCmd(ChrTable['凯文神父'], ItemTable['精神２'], 0x03)
    EquipCmd(ChrTable['凯文神父'], ItemTable['防御２'], 0x04)
    AddCraft(ChrTable['凯文神父'], 0x0000)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetPos(0x0109, 3570, 7250, -68040, 90)
    ChrSetPos(0x0101, -600, 7250, -54970, 180)
    CameraMove(-1190, 7250, -61210, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3250, 0)
    OP_6C(145000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010260998V#1018F#5P约，约修──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0F23')
    def lambda_0F23():
        ChrWalkTo(0x0101, -140, 7250, -59980, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0F23)

    @scena.Lambda('lambda_0F3E')
    def lambda_0F3E():
        CameraMove(500, 7250, -63380, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0F3E)

    WaitForThreadExit(0x0101, 0x0000)
    TerminateThread(0x0101, 0x01)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0101, 65535)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010210750V#1004F#6P啊……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CameraMove(1140, 7250, -65340, 1200)
    OP_62(0x0109, 0x00000000, 2300, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    @scena.Lambda('lambda_0FD0')
    def lambda_0FD0():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_0FD0')

    DispatchAsync2(0x0109, 0x0000, lambda_0FD0)

    Sleep(400)

    ChrTalk(
        0x0109,
        (
            '#0180261000V#1064F#6P咦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180261001V艾丝蒂尔吗……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010261002V#1020F#5P凯文先生……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190373V为…为什么会在这里…？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 180, 400)
    Sleep(500)

    @scena.Lambda('lambda_107C')
    def lambda_107C():
        ChrWalkTo(0x00FE, -1040, 7250, -67840, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_107C)

    @scena.Lambda('lambda_1097')
    def lambda_1097():
        CameraMove(160, 7250, -67940, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1097)

    @scena.Lambda('lambda_10AF')
    def lambda_10AF():
        OP_67(0, 8210, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_10AF)

    @scena.Lambda('lambda_10C7')
    def lambda_10C7():
        CameraSetDistance(2570, 3000)

        ExitThread()

    DispatchAsync(0x0109, 0x0002, lambda_10C7)

    @scena.Lambda('lambda_10D7')
    def lambda_10D7():
        OP_6E(334, 3000)

        ExitThread()

    DispatchAsync(0x0109, 0x0003, lambda_10D7)

    OP_6C(134000, 3000)
    WaitForThreadExit(0x0101, 0x0001)
    ChrSetDirection(0x0101, 270, 400)
    Sleep(500)

    ChrSetDirection(0x0101, 90, 400)
    Sleep(500)

    ChrSetDirection(0x0101, 180, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010261004V#1026F#6P不，不在这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0109, 0x00)
    ChrWalkTo(0x0109, 580, 7250, -67770, 2000, 0x00)

    ChrTalk(
        0x0109,
        (
            '#0180261005V#1062F#5P呀～好久不见啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180261006V#1061F不过竟能在这种地方重逢，\n',
            '我们果然有缘──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0109, 600)

    ChrTalk(
        0x0101,
        (
            '#0010261007V#1002F#4P对了，凯文先生！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010261008V你在这里\n',
            '碰到过什么其它人吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180261009V#1064F#5P咦……什么人啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180261010V难道艾丝蒂尔\n',
            '也是在这里等人吗～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010261011V#1026F#4P啊，嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010261012V#1015F……那，凯文先生也是？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180261013V#1063F#5P啊啊……\n',
            '收到一封信、要我来这里的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010261014V#1011F#4P我，我也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010261015V#1016F嘿嘿。\n',
            '居然有这么有趣的巧合啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180261016V#1061F#5P哈哈，是呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180261017V#1069F──唔？\n',
            '会有这种巧合吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010261018V#1015F#4P难，难道说？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010261019V凯文先生\n',
            '也是被约修亚叫来的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180261020V#1064F#5P约修亚？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180261021V就是……\n',
            '你那个男朋友？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010261022V#1026F#4P嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180261023V#1067F#5P我，我不知道……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180261024V约修亚其实\n',
            '是个上了年纪的大叔吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180261025V#1068F当然，如果有爱、\n',
            '年龄差距倒也不是问题……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180261026V既然如此\n',
            '我也还是很有机会的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010261027V#1007F#4P那个～\n',
            '我觉得话题好像\n',
            '微妙的错开了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010261028V#1015F凯文先生是被谁的\n',
            '信叫出来的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180261029V#1060F#5P啊啊，格兰赛尔大圣堂\n',
            '收到了给我的信。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180261030V送来信的人好像是个体面的\n',
            '中年男子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010261031V#1019F#4P约，约修亚\n',
            '和我同年的啦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010261032V不可能是大叔吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180261033V#1064F#5P啊，果然？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180261034V#1061F呀～我也正觉得\n',
            '有点奇怪呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010261035V#1007F#4P说的没错……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010261036V#1002F不过，那\n',
            '到底是怎么回事呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010261037V难、难道说……',
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
            TXT(0x00, '【真的只是巧合？】\n'),
            TXT(0x01, '【为了解决两人设下的陷阱】\n'),
            TXT(0x02, '【中年男子是约修亚的变装】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_17C2'),
        (0x00000001, 'loc_1815'),
        (0x00000002, 'loc_185E'),
        (-1, 'loc_1902'),
    )

    def _loc_17C2(): pass

    label('loc_17C2')

    ChrTalk(
        0x0109,
        (
            '#0180261038V#1067F#5P嗯，虽然可能性\n',
            '不是零……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0109, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    Jump('loc_1902')

    def _loc_1815(): pass

    label('loc_1815')

    OP_2B(0x008E, 0x0003)

    ChrTalk(
        0x0109,
        (
            '#0180261039V#1063F#5P什么……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0109, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    Jump('loc_1902')

    def _loc_185E(): pass

    label('loc_185E')

    OP_2B(0x008E, 0x0001)

    ChrTalk(
        0x0109,
        (
            '#0180261040V#1064F#5P哈～想到\n',
            '奇怪的事了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180261041V#1063F约修亚\n',
            '很会变装吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010261042V#1015F#4P嗯～很难说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0109, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    Jump('loc_1902')

    def _loc_1902(): pass

    label('loc_1902')

    OP_20(0x000003E8)

    @scena.Lambda('lambda_190D')
    def lambda_190D():
        CameraSetDistance(2850, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_190D)

    ExecExpressionWithValue(
        0x000B,
        0x28,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x28,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetFlags(0x000B, 0x0004)
    ChrSetFlags(0x000C, 0x0004)
    ChrSetPos(0x000B, 11930, 10500, -73000, 90)
    ChrSetPos(0x000C, -11930, 10500, -62000, 270)
    PlaySE(207, 0x01, 0x0A)
    CreateThread(0x000B, 0x03, 0x00, func_02_286)
    CreateThread(0x000C, 0x03, 0x00, func_02_286)

    @scena.Lambda('lambda_197C')
    def lambda_197C():
        ChrWalkTo(0x00FE, -1130, 8500, -73000, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_197C)

    @scena.Lambda('lambda_1997')
    def lambda_1997():
        ChrWalkTo(0x00FE, -550, 8500, -62000, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1997)

    Sleep(100)

    OP_24(0x00CF, 0x1E)
    Sleep(100)

    OP_24(0x00CF, 0x32)
    Sleep(100)

    OP_24(0x00CF, 0x3C)
    Sleep(100)

    OP_24(0x00CF, 0x46)
    Sleep(100)

    OP_24(0x00CF, 0x50)
    Sleep(100)

    OP_24(0x00CF, 0x5A)
    Sleep(100)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_24(0x00CF, 0x64)
    WaitForThreadExit(0x000C, 0x0001)

    @scena.Lambda('lambda_1A0D')
    def lambda_1A0D():
        OP_97(0x00FE, -1040, -67840, 360000, 11000, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0000, lambda_1A0D)

    WaitForThreadExit(0x000B, 0x0001)

    @scena.Lambda('lambda_1A2E')
    def lambda_1A2E():
        OP_97(0x00FE, -1040, -67840, 360000, 11000, 0x0001)

        ExitThread()

    DispatchAsync(0x000B, 0x0000, lambda_1A2E)

    PlayBGM(53)
    ChrSetDirection(0x0101, 0, 600)
    ChrSetDirection(0x0109, 180, 600)

    ChrTalk(
        0x0101,
        (
            '#0010261043V#1020F#6P#12A什…么',
            TxtCtl.Enter,
        ),
    )

    Sleep(1200)

    ChrTalk(
        0x0109,
        (
            '#0180261044V#1063F#5P#12A真的假的……',
            TxtCtl.Enter,
        ),
    )

    Sleep(1200)

    @scena.Lambda('lambda_1AB2')
    def lambda_1AB2():
        ChrJumpToRelative(0x00FE, 0, 0, 500, 250, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1AB2)

    ChrSetChipByIndex(0x0101, 4)
    ChrSetSubChip(0x0101, 0)
    PlaySE(213, 0x00, 0x64)
    Sleep(100)

    @scena.Lambda('lambda_1AE4')
    def lambda_1AE4():
        ChrJumpToRelative(0x00FE, 0, 0, -500, 250, 6000)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_1AE4)

    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0109, 5)
    ChrSetSubChip(0x0109, 0)
    WaitForThreadExit(0x000B, 0x0000)
    ChrSetDirection(0x000B, 0, 400)
    WaitForThreadExit(0x000C, 0x0000)
    ChrSetDirection(0x000C, 180, 400)

    @scena.Lambda('lambda_1B29')
    def lambda_1B29():
        ChrMoveToRelativeAsync(0x00FE, 0, -1500, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1B29)

    @scena.Lambda('lambda_1B44')
    def lambda_1B44():
        ChrMoveToRelativeAsync(0x00FE, 0, -1500, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1B44)

    Sleep(500)

    @scena.Lambda('lambda_1B64')
    def lambda_1B64():
        ChrMoveToRelativeAsync(0x00FE, 0, -500, 0, 500, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1B64)

    @scena.Lambda('lambda_1B7F')
    def lambda_1B7F():
        ChrMoveToRelativeAsync(0x00FE, 0, -500, 0, 500, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1B7F)

    Sleep(1000)

    ChrTalk(
        0x0109,
        (
            '#0180261045V#1067F#5P哼，好像也不是\n',
            '认错人的感觉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010261046V#1005F#6P嗯……来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1C00')
    def lambda_1C00():
        CameraSetDistance(2100, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1C00)

    @scena.Lambda('lambda_1C10')
    def lambda_1C10():
        ChrWalkTo(0x00FE, -600, 7250, -69000, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1C10)

    @scena.Lambda('lambda_1C2B')
    def lambda_1C2B():
        ChrWalkTo(0x00FE, -400, 7250, -66060, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1C2B)

    WaitForThreadExit(0x000B, 0x0001)
    OP_23(0x00CF)
    Battle(0x0000045A, 0x00000000, 0x01, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_1C61'),
        (-1, 'loc_1C66'),
    )

    def _loc_1C61(): pass

    label('loc_1C61')

    OP_B4(0x00)

    Jump('loc_1C66')

    def _loc_1C66(): pass

    label('loc_1C66')

    Call(0, 0x0008)

    Return()

# id: 0x0008 offset: 0x1C6B
@scena.Code('func_08_1C6B')
def func_08_1C6B():
    EventBegin(0x00)
    OP_7E(-900, 500, 900, 150, 0)
    FadeOut(0, 0, -1)
    PlayBGM(81)
    Sleep(500)

    CameraMove(-430, 7250, -70700, 0)
    OP_67(0, 8210, -10000, 0)
    CameraSetDistance(2580, 0)
    OP_6C(134000, 0)
    OP_6E(334, 0)

    ExecExpressionWithValue(
        0x000B,
        0x28,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x28,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x0008, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetFlags(0x000B, 0x0004)
    ChrSetFlags(0x000C, 0x0004)
    ChrSetPos(0x0101, -2170, 7250, -68100, 180)
    ChrSetPos(0x0109, -180, 7250, -67940, 180)
    ChrSetPos(0x000B, -2080, 8500, -72570, 0)
    ChrSetPos(0x000C, 800, 8500, -72820, 0)
    CreateThread(0x000B, 0x03, 0x00, func_02_286)
    CreateThread(0x000C, 0x03, 0x00, func_02_286)
    PlaySE(207, 0x01, 0x64)
    OP_24(0x00CF, 0x64)
    ChrSetChipByIndex(0x0101, 4)
    ChrSetChipByIndex(0x0109, 5)
    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x0109, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010261047V#1005F#6P这，这些家伙……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180261048V#1063F！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000B, 270, 400)
    ChrSetDirection(0x000C, 270, 400)

    @scena.Lambda('lambda_1DCE')
    def lambda_1DCE():
        CameraMove(-6930, 7250, -69700, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1DCE)

    @scena.Lambda('lambda_1DE6')
    def lambda_1DE6():
        ChrWalkTo(0x00FE, -17970, 10250, -71460, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1DE6)

    Sleep(200)

    @scena.Lambda('lambda_1E06')
    def lambda_1E06():
        ChrWalkTo(0x00FE, -17970, 10250, -71460, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1E06)

    @scena.Lambda('lambda_1E21')
    def lambda_1E21():
        ChrTurnDirection(0x00FE, 0x000C, 400)
        Yield()

        Jump('lambda_1E21')

    DispatchAsync2(0x0101, 0x0002, lambda_1E21)

    @scena.Lambda('lambda_1E32')
    def lambda_1E32():
        ChrTurnDirection(0x00FE, 0x000C, 400)
        Yield()

        Jump('lambda_1E32')

    DispatchAsync2(0x0109, 0x0002, lambda_1E32)

    OP_24(0x00CF, 0x5A)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(200)

    OP_24(0x00CF, 0x5A)
    Sleep(150)

    OP_24(0x00CF, 0x50)
    Sleep(150)

    OP_24(0x00CF, 0x46)
    Sleep(100)

    OP_24(0x00CF, 0x3C)
    Sleep(100)

    OP_24(0x00CF, 0x32)
    Sleep(100)

    OP_24(0x00CF, 0x28)
    Sleep(100)

    OP_24(0x00CF, 0x1E)
    Sleep(100)

    OP_24(0x00CF, 0x14)
    Sleep(100)

    OP_24(0x00CF, 0x0A)
    Sleep(100)

    OP_23(0x00CF)

    ChrTalk(
        0x0101,
        (
            '#0010261049V#1004F#6P啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0x02)
    TerminateThread(0x0109, 0x02)
    ChrSetChipByIndex(0x0101, 65535)

    @scena.Lambda('lambda_1EE9')
    def lambda_1EE9():
        ChrWalkTo(0x00FE, -4430, 7250, -68210, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1EE9)

    Sleep(200)

    ChrSetChipByIndex(0x0109, 65535)

    @scena.Lambda('lambda_1F0E')
    def lambda_1F0E():
        ChrWalkTo(0x00FE, -4630, 7250, -69530, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_1F0E)

    WaitForThreadExit(0x0109, 0x0001)
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0109, 0x00000000, 2300, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1000)

    CameraMove(-4350, 7250, -69080, 1500)
    OP_63(0x0101)
    OP_63(0x0109)

    ChrTalk(
        0x0101,
        (
            '#0010261050V#1020F#6P什，什么啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010261051V这些机械……\n',
            '与其说是魔兽……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180261052V#1063F#5P啊啊，似乎和城中封印区域里的\n',
            '人形兵器一样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180261053V#1065F不过和那不同的是、\n',
            '好像是最近制造的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0109, 400)

    ChrTalk(
        0x0101,
        (
            '#0010261054V#1015F#6P这是怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0109, 0x0101, 400)

    ChrTalk(
        0x0109,
        (
            '#0180261055V#1060F封印区域的人形兵器\n',
            '如果说是一种古代遗物……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180261056V那刚才机械的就是导力驱动的\n',
            '现代人形兵器。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180261057V而且性能\n',
            '似乎毫不逊色。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010261058V#1007F#6P原，原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010261059V……………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010261060V#1019F为什么凯文先生\n',
            '知道封印区域的事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180261061V#1064F……（惊讶）。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4A(0x0008, 255)
    ChrSetPos(0x000D, -1180, 7250, -58700, 180)
    ChrSetPos(0x0008, -570, 7250, -57570, 180)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x0008, 0x0080)

    NpcTalk(
        0x0008,
        '男人的声音',
        (
            '#3220261062V#2P喂，在干什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(100)

    OP_62(0x0109, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_225F')
    def lambda_225F():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_225F')

    DispatchAsync2(0x0101, 0x0002, lambda_225F)

    @scena.Lambda('lambda_2270')
    def lambda_2270():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_2270')

    DispatchAsync2(0x0109, 0x0002, lambda_2270)

    Fade(1000)
    CameraMove(-2190, 7250, -67000, 0)
    OP_67(0, 7650, -10000, 0)
    CameraSetDistance(2420, 0)
    OP_6C(89000, 0)
    OP_6E(334, 0)
    OP_6E(334, 0)

    @scena.Lambda('lambda_22CC')
    def lambda_22CC():
        ChrWalkTo(0x00FE, -1370, 7250, -64739, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_22CC)

    Sleep(300)

    @scena.Lambda('lambda_22EC')
    def lambda_22EC():
        ChrWalkTo(0x00FE, -540, 7250, -63980, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_22EC)

    WaitForThreadExit(0x000D, 0x0001)
    ChrSetDirection(0x000D, 225, 400)
    WaitForThreadExit(0x0008, 0x0001)
    ChrSetDirection(0x0008, 225, 400)
    TerminateThread(0x0101, 0x02)
    TerminateThread(0x0109, 0x02)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010261063V#1004F#6P啊，士兵先生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3220261064V#5P就觉得有什么骚动……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3220261065V#5P你们在这里\n',
            '干什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010261066V#1020F#6P等、等一下！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010261067V我们只是在这里被奇怪的\n',
            '机械袭击……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3220261068V#5P奇怪的机械……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180261069V#1062F啊啊，惊动你们\n',
            '实在是不好意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180261070V其实她是协会\n',
            '所属的游击士。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180261071V为追捕某些人，\n',
            '正在调查中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010261072V#1004F#6P啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3220261073V#5P游击士……真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180261074V#1060F那，艾丝蒂尔。\n',
            '把游击士手册给他们看吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010261075V#1015F#6P啊，嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔急忙展示了游击士手册。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x000D,
        (
            '#3220261076V#5P……原来如此，好像是真的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3220261077V#5P某些人\n',
            '到底是什么人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180261078V#1065F是称为『结社』\n',
            '身份不明的家伙们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180261079V似乎在各地进行\n',
            '各种各样奇怪的实验。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180261080V#1063F我们追寻他们的线索\n',
            '来到这里，\n',
            '却被奇怪的机械袭击了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010261081V#1026F#6P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3220261082V#5P这么说来司令部\n',
            '发来了关于『结社』那些家伙的\n',
            '注意事项……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3220261083V#5P那么说周游道出现的\n',
            '就是那个『结社』的人吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010261084V#1020F#6P啊，等一下！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010261085V周游道出现了……？\n',
            '到底发生什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3220261086V#5P啊啊，之前艾尔贝离宫的\n',
            '警备本部发来了联络。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3220261087V#5P似乎是有某个不明武装集团\n',
            '袭击了离宫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010261088V#1005F#6P你、你说什么～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3220261089V#5P幸好有希德中校在，\n',
            '似乎轻松击退了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3220261090V#5P现在、周游道已被封锁，\n',
            '正在追捕那个集团。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180261091V#1068F呼啦～\n',
            '发生了大事啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180261092V那我们也暂时\n',
            '返回协会比较好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010261093V#1026F#6P呼，啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3220261094V#5P啊啊，说不定\n',
            '就是你们\n',
            '在追捕的人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3220261095V#5P好啦，附近的警戒\n',
            '就这样交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#3220261096V#5P你们赶快\n',
            '回王都协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180261097V#1061F谢谢！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180261098V#1062F那艾丝蒂尔。\n',
            '赶快回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2A6E')
    def lambda_2A6E():
        ChrTurnDirection(0x00FE, 0x0109, 400)
        Yield()

        Jump('lambda_2A6E')

    DispatchAsync2(0x0101, 0x0002, lambda_2A6E)

    ChrTalk(
        0x0101,
        (
            '#0010261099V#1020F#6P等、等等……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2AA6')
    def lambda_2AA6():
        ChrTurnDirection(0x00FE, 0x0109, 400)
        Yield()

        Jump('lambda_2AA6')

    DispatchAsync2(0x000D, 0x0002, lambda_2AA6)

    @scena.Lambda('lambda_2AB7')
    def lambda_2AB7():
        ChrTurnDirection(0x00FE, 0x0109, 400)
        Yield()

        Jump('lambda_2AB7')

    DispatchAsync2(0x0008, 0x0002, lambda_2AB7)

    CreateThread(0x0109, 0x00, 0x00, func_0A_2B2B)
    Sleep(1500)

    TerminateThread(0x0101, 0x02)
    CreateThread(0x0101, 0x00, 0x00, func_0B_2B54)
    CameraMove(-2110, 7250, -63810, 3000)
    FadeOut(1000, 0, -1)
    OP_0D()
    TerminateThread(0x0109, 0x01)
    TerminateThread(0x0101, 0x01)
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T0610._SN', 107, 0, 0)
    IdleLoop()

    Return()

# id: 0x0009 offset: 0x2B0F
@scena.Code('func_09_2B0F')
def func_09_2B0F():
    ChrWalkTo(0x00FE, -710, 7250, -67100, 2000, 0x00)
    ChrTurnDirection(0x00FE, 0x0101, 400)

    Return()

# id: 0x000A offset: 0x2B2B
@scena.Code('func_0A_2B2B')
def func_0A_2B2B():
    ChrWalkTo(0x00FE, -2790, 7250, -67510, 3000, 0x00)
    ChrWalkTo(0x00FE, -1800, 7250, -53040, 3000, 0x00)

    Return()

# id: 0x000B offset: 0x2B54
@scena.Code('func_0B_2B54')
def func_0B_2B54():
    ChrWalkTo(0x00FE, -2890, 7250, -66430, 3000, 0x00)
    ChrWalkTo(0x00FE, -1800, 7250, -53040, 3000, 0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

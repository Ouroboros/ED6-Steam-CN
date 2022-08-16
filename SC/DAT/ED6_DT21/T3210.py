import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T3210_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3210   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3210.x'
    header.mapIndex       = 1
    header.bgm            = 15
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
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
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
    ]

# id: 0x10001 offset: 0xBA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '林',
            x                   = 28010,
            z                   = 0,
            y                   = 4920,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0002,
        ),
        ScenaNpcData(
            name                = '希利尔',
            x                   = 3350,
            z                   = 250,
            y                   = 3380,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
    )

# id: 0x10002 offset: 0xFA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xFA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0xFA
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xFA
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_104',
    )

    Jump('loc_13A')

    def _loc_104(): pass

    label('loc_104')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_10E',
    )

    Jump('loc_13A')

    def _loc_10E(): pass

    label('loc_10E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_118',
    )

    Jump('loc_13A')

    def _loc_118(): pass

    label('loc_118')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_133',
    )

    ChrSetPos(0x0008, 27000, 0, 3050, 270)

    Jump('loc_13A')

    def _loc_133(): pass

    label('loc_133')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_13A',
    )

    def _loc_13A(): pass

    label('loc_13A')

    Return()

# id: 0x0001 offset: 0x13B
@scena.Code('func_01_13B')
def func_01_13B():
    Return()

# id: 0x0002 offset: 0x13C
@scena.Code('func_02_13C')
def func_02_13C():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_203',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C1',
    )

    ChrTalk(
        0x00FE,
        (
            '我从来巡逻的士兵\n',
            '那里听说了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在整个利贝尔\n',
            '好像都不能使用导力器。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那、那不是\n',
            '挺麻烦的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_200')

    def _loc_1C1(): pass

    label('loc_1C1')

    ChrTalk(
        0x00FE,
        (
            '全国的导力器\n',
            '竟然都停下来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……真令人无法相信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_200(): pass

    label('loc_200')

    Jump('loc_58B')

    def _loc_203(): pass

    label('loc_203')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_255',
    )

    ChrTalk(
        0x00FE,
        (
            '好～像温泉又\n',
            '发生什么事了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '导力灯也打不开，\n',
            '是怎么回事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_58B')

    def _loc_255(): pass

    label('loc_255')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_344',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_2AE',
    )

    ChrTalk(
        0x0008,
        (
            '总算水的温度也\n',
            '好像恢复正常了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '『红叶亭』的澡堂\n',
            '看来能用了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_341')

    def _loc_2AE(): pass

    label('loc_2AE')

    ChrTalk(
        0x0008,
        (
            '总算水的温度也\n',
            '好像恢复正常了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '『红叶亭』的澡堂\n',
            '看来能用了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '说起来最近\n',
            '好像发生了地震……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '这次的温泉的事也跟\n',
            '那个有关系？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_341(): pass

    label('loc_341')

    Jump('loc_58B')

    def _loc_344(): pass

    label('loc_344')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_422',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_3A4',
    )

    ChrTalk(
        0x0008,
        (
            '可我们村的温泉\n',
            '是直接从后山取的水啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '难道是在源泉那边发生了什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_41F')

    def _loc_3A4(): pass

    label('loc_3A4')

    ChrTalk(
        0x0008,
        (
            '我想外面怎么这么吵，\n',
            '原来是温泉的水沸腾了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '对主妇来说不用花时间\n',
            '烧开水可是件好事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不过问题不在这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_41F(): pass

    label('loc_41F')

    Jump('loc_58B')

    def _loc_422(): pass

    label('loc_422')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_4D3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_46F',
    )

    ChrTalk(
        0x0008,
        (
            '最近我女儿也在\n',
            '旅馆打工。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '在认真地做\n',
            '就很好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4D0')

    def _loc_46F(): pass

    label('loc_46F')

    ChrTalk(
        0x0008,
        (
            '我女儿终于\n',
            '也开始工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不过也只是\n',
            '旅馆的帮工而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '但只要不是闲在家里就好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_4D0(): pass

    label('loc_4D0')

    Jump('loc_58B')

    def _loc_4D3(): pass

    label('loc_4D3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_58B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_53C',
    )

    ChrTalk(
        0x0008,
        (
            '我丈夫是在『红叶亭』\n',
            '做东方料理的厨师哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '评价好像还不错，\n',
            '经常有杂志来采访。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_58B')

    def _loc_53C(): pass

    label('loc_53C')

    ChrTalk(
        0x0008,
        (
            '哎呀，莫非你们\n',
            '在找旅馆？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '『红叶亭』就在\n',
            '外面的大街走到底的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_58B(): pass

    label('loc_58B')

    TalkEnd(0x0008)

    Return()

# id: 0x0003 offset: 0x58F
@scena.Code('func_03_58F')
def func_03_58F():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_686',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_641',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，泵能够修好\n',
            '真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '旅馆的营业当然\n',
            '也一样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最重要的是\n',
            '省去烧开水的工夫了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在如今这种不能使用导力器的\n',
            '时候就更是如此了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_683')

    def _loc_641(): pass

    label('loc_641')

    ChrTalk(
        0x00FE,
        (
            '泵能够修好\n',
            '真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最重要的是\n',
            '省去烧开水的工夫了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_683(): pass

    label('loc_683')

    Jump('loc_B44')

    def _loc_686(): pass

    label('loc_686')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_785',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_726',
    )

    ChrTalk(
        0x00FE,
        (
            '导力器不能用了，\n',
            '温泉的泵也停止运转了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '温泉可是我们村子招揽\n',
            '疗养客人的法宝啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不快点修好的话，\n',
            '我们的生活可就不好过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_782')

    def _loc_726(): pass

    label('loc_726')

    ChrTalk(
        0x00FE,
        (
            '导力器不能用了，\n',
            '温泉的泵也停止运转了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不快点修好的话，\n',
            '我们的生活可就不好过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_782(): pass

    label('loc_782')

    Jump('loc_B44')

    def _loc_785(): pass

    label('loc_785')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_7F2',
    )

    ChrTalk(
        0x0009,
        (
            '温泉的水温\n',
            '也好象恢复正常了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '尽管如此\n',
            '这真是件怪事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '可能还是因为地震\n',
            '的影响吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B44')

    def _loc_7F2(): pass

    label('loc_7F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_8B3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_84D',
    )

    ChrTalk(
        0x0009,
        (
            '说不定是地壳\n',
            '产生变化了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '而且还发生了地震，\n',
            '完全有那个可能性。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8B0')

    def _loc_84D(): pass

    label('loc_84D')

    ChrTalk(
        0x0009,
        (
            '呼，真令人感到为难。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '温泉不能用的话\n',
            '旅馆也不能营业了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '说不定是地壳\n',
            '产生变化了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_8B0(): pass

    label('loc_8B0')

    Jump('loc_B44')

    def _loc_8B3(): pass

    label('loc_8B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_A70',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0070, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_937',
    )

    ChrTalk(
        0x0009,
        (
            '我、我刚才看见我家后面\n',
            '有什么东西飞快地\n',
            '跑过去了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '那、那到底\n',
            '是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '看、看上去\n',
            '像是魔兽……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A6D')

    def _loc_937(): pass

    label('loc_937')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_9AF',
    )

    ChrTalk(
        0x0009,
        (
            '听说露天浴场好像\n',
            '有偷窥犯出没，要小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '实在无法相信这个\n',
            '村里会有那种人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '一定是客人的错觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A6D')

    def _loc_9AF(): pass

    label('loc_9AF')

    ChrTalk(
        0x0009,
        (
            '我从在旅馆工作的\n',
            '老婆那里听说了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '听说露天浴场好像\n',
            '有偷窥犯出没，要小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '实在无法相信这个\n',
            '村里会有那种人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '麻绪婆婆为慎重起见\n',
            '好像联系协会了，\n',
            '一定是客人的错觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_A6D(): pass

    label('loc_A6D')

    Jump('loc_B44')

    def _loc_A70(): pass

    label('loc_A70')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_B44',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_AD1',
    )

    ChrTalk(
        0x0009,
        (
            '呀，欢迎。\n',
            '欢迎来到亚尔摩村。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这里自古以来就是温泉地区。\n',
            '常客也很多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B44')

    def _loc_AD1(): pass

    label('loc_AD1')

    ChrTalk(
        0x0009,
        (
            '呀，欢迎。\n',
            '欢迎来到亚尔摩村。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '你们也是来做温泉疗养的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这里自古以来就是温泉地区。\n',
            '常客也很多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_B44(): pass

    label('loc_B44')

    TalkEnd(0x0009)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T3231_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3231   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3231.x'
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
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
    ]

# id: 0x10001 offset: 0xBA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '莉西亚',
            x                   = -100,
            z                   = 0,
            y                   = 120,
            direction           = 180,
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
            name                = '阿尔宾',
            x                   = -580,
            z                   = 0,
            y                   = -5020,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
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
        ScenaActorData(
            triggerX            = -1900,
            triggerZ            = 0,
            triggerY            = 5070,
            triggerRange        = 800,
            actorX              = -1900,
            actorZ              = 1000,
            actorY              = 5070,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -1890,
            triggerZ            = 0,
            triggerY            = -4990,
            triggerRange        = 800,
            actorX              = -1890,
            actorZ              = 1000,
            actorY              = -4990,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x142
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_16E',
    )

    ChrSetFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_16B',
    )

    ChrSetPos(0x0009, -1110, 0, -3330, 90)

    def _loc_16B(): pass

    label('loc_16B')

    Jump('loc_189')

    def _loc_16E(): pass

    label('loc_16E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_17D',
    )

    ChrClearFlags(0x0008, 0x0080)

    Jump('loc_189')

    def _loc_17D(): pass

    label('loc_17D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_189',
    )

    ChrClearFlags(0x0008, 0x0080)

    def _loc_189(): pass

    label('loc_189')

    Return()

# id: 0x0001 offset: 0x18A
@scena.Code('func_01_18A')
def func_01_18A():
    OP_72(0x0008, 0x0010)
    OP_72(0x0009, 0x0010)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1D0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D0',
    )

    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    StopEffect(0x80, 0x00)
    StopEffect(0x81, 0x00)
    StopEffect(0x82, 0x00)
    StopEffect(0x83, 0x00)
    StopEffect(0x84, 0x00)

    def _loc_1D0(): pass

    label('loc_1D0')

    Return()

# id: 0x0002 offset: 0x1D1
@scena.Code('func_02_1D1')
def func_02_1D1():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1F4',
    )

    OP_8D(0x00FE, -1080, -1680, 1450, 3260, 2000)

    Jump('func_02_1D1')

    def _loc_1F4(): pass

    label('loc_1F4')

    Return()

# id: 0x0003 offset: 0x1F5
@scena.Code('func_03_1F5')
def func_03_1F5():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0286, 0, 0x1430)),
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_421',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_370',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_2B1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_268',
    )

    ChrTalk(
        0x0008,
        (
            '我只是在打扫的时候\n',
            '顺便确认了一下水温哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我、我可没偷懒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2AE')

    def _loc_268(): pass

    label('loc_268')

    ChrTalk(
        0x0008,
        (
            '哇～这水不错。\n',
            '看来温泉已经没问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '好，得继续打扫了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_2AE(): pass

    label('loc_2AE')

    Jump('loc_36D')

    def _loc_2B1(): pass

    label('loc_2B1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_36D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_30B',
    )

    ChrTalk(
        0x0008,
        (
            '我来室内浴场打扫了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不过这里水蒸气太厉害，\n',
            '什么也看不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_36D')

    def _loc_30B(): pass

    label('loc_30B')

    ChrTalk(
        0x0008,
        (
            '我来室内浴场打扫了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不过这里水蒸气太厉害，\n',
            '什么也看不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '这是怎么回事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_36D(): pass

    label('loc_36D')

    Jump('loc_41E')

    def _loc_370(): pass

    label('loc_370')

    ChrTurnDirection(0x00FE, 0x0104, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3DE',
    )

    ChrTalk(
        0x0008,
        (
            '对不起，奥利维尔大人～\n',
            '您难得来却不能泡温泉～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不知道为什么，\n',
            '澡堂的水沸腾起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_41E')

    def _loc_3DE(): pass

    label('loc_3DE')

    ChrTalk(
        0x0008,
        (
            '啊～还是\n',
            '奥利维尔大人优秀～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '哎呀～请把我\n',
            '拐去帝都吧～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_41E(): pass

    label('loc_41E')

    Jump('loc_740')

    def _loc_421(): pass

    label('loc_421')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_483',
    )

    ChrTalk(
        0x0008,
        (
            '我来室内浴场打扫了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '进了更衣室就会因为有很厉害的\n',
            '水蒸气而什么都看不见……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4E5')

    def _loc_483(): pass

    label('loc_483')

    ChrTalk(
        0x0008,
        (
            '反正也是闲着，就开始\n',
            '打工了，打扫卫生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不过都是一些上了年纪的客人，\n',
            '不太有干劲啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4E5(): pass

    label('loc_4E5')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5B8',
    )

    ChrTalk(
        0x0008,
        (
            '……咦？啊、啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(1000)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '呀～！？　这不是奥利维尔大人么！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我真高兴～！\n',
            '您又来啦！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1004F（奥、奥利维尔大人～？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#031F呵呵，好久不见。\n',
            '还乖吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_691')

    def _loc_5B8(): pass

    label('loc_5B8')

    ChrTurnDirection(0x0008, 0x0104, 500)

    ChrTalk(
        0x0008,
        (
            '……咦？啊、啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '那、那边是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#031F呵呵，好久不见。\n',
            '还乖吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '呀～！？\n',
            '果然是奥利维尔大人！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我真高兴～！\n',
            '您又来啦！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1004F（奥、奥利维尔大人～？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_691(): pass

    label('loc_691')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6F4',
    )

    ChrTalk(
        0x0008,
        (
            '对不起，奥利维尔大人～\n',
            '现在还不能洗澡～。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不知道为什么，\n',
            '澡堂的水沸腾起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_73A')

    def _loc_6F4(): pass

    label('loc_6F4')

    ChrTalk(
        0x0008,
        (
            '奥利维尔先生～\n',
            '这次要再唱歌给我听哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '您弹琴的样子\n',
            '最帅了㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_73A(): pass

    label('loc_73A')

    SetScenaFlags(ScenaFlag(0x0286, 0, 0x1430))
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    def _loc_740(): pass

    label('loc_740')

    TalkEnd(0x0008)

    Return()

# id: 0x0004 offset: 0x744
@scena.Code('func_04_744')
def func_04_744():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_7F9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7A8',
    )

    ChrTalk(
        0x00FE,
        (
            '呀～～结婚仪式\n',
            '头把澡是特别的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈，也不枉我在这里\n',
            '苦苦等待了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_7F6')

    def _loc_7A8(): pass

    label('loc_7A8')

    ChrTalk(
        0x00FE,
        (
            '呀～～结婚仪式\n',
            '头把澡是特别的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好了，先休息一下\n',
            '然后再泡个回头澡！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7F6(): pass

    label('loc_7F6')

    Jump('loc_8ED')

    def _loc_7F9(): pass

    label('loc_7F9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_8ED',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_89F',
    )

    ChrTalk(
        0x00FE,
        (
            '泵出了故障，\n',
            '澡堂好像不能用了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过都到了这里，\n',
            '我怎么能不泡温泉呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我会一直在这里\n',
            '等到能用为止。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……阻止我也是没用的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_8ED')

    def _loc_89F(): pass

    label('loc_89F')

    ChrTalk(
        0x00FE,
        (
            '都到了亚尔摩了，\n',
            '我怎么能不泡温泉呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我会一直在这里\n',
            '等到能用为止。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8ED(): pass

    label('loc_8ED')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x8F1
@scena.Code('func_05_8F1')
def func_05_8F1():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_8FF',
    )

    Call(0, 0x0007)

    Jump('loc_B1F')

    def _loc_8FF(): pass

    label('loc_8FF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_970',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '发现门上有块牌子。\n',
            '『因为泵装置出现故障，\n',
            '　温泉暂停开放』',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    Jump('loc_B1F')

    def _loc_970(): pass

    label('loc_970')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_AB6',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '发现门上有块牌子。\n',
            '『因为温泉处于沸腾状态，\n',
            '　暂时禁止进入』',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_A51',
    )

    ChrTalk(
        0x0103,
        (
            '#0030230921V#020F要泡温泉就得\n',
            '想办法解决洗澡水的沸腾问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030230922V赶快去后面的栅门吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AB3')

    def _loc_A51(): pass

    label('loc_A51')

    ChrTalk(
        0x0106,
        (
            '#0050230923V#050F要泡温泉就得\n',
            '想办法解决洗澡水的沸腾问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050230924V赶快去后面的栅门吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AB3(): pass

    label('loc_AB3')

    Jump('loc_B1F')

    def _loc_AB6(): pass

    label('loc_AB6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0290, 2, 0x1482)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_AC8',
    )

    Call(0, 0x0007)

    Jump('loc_B1F')

    def _loc_AC8(): pass

    label('loc_AC8')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '『女澡堂』\n',
            '　需要使用时\n',
            '　请到服务台申请。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    def _loc_B1F(): pass

    label('loc_B1F')

    TalkEnd(0x00FF)

    Return()

# id: 0x0006 offset: 0xB23
@scena.Code('func_06_B23')
def func_06_B23():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_B34',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    Call(0, 0x0007)

    Jump('loc_D57')

    def _loc_B34(): pass

    label('loc_B34')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_BA5',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '发现门上有块牌子。\n',
            '『因为泵装置出现故障，\n',
            '　温泉暂停开放』',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    Jump('loc_D57')

    def _loc_BA5(): pass

    label('loc_BA5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_CEB',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '发现门上有块牌子。\n',
            '『因为温泉处于沸腾状态，\n',
            '　暂时禁止进入』',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_C86',
    )

    ChrTalk(
        0x0103,
        (
            '#0030230921V#020F要泡温泉就得\n',
            '想办法解决洗澡水的沸腾问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030230922V赶快去后面的栅门吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CE8')

    def _loc_C86(): pass

    label('loc_C86')

    ChrTalk(
        0x0106,
        (
            '#0050230923V#050F要泡温泉就得\n',
            '想办法解决洗澡水的沸腾问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050230924V赶快去后面的栅门吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CE8(): pass

    label('loc_CE8')

    Jump('loc_D57')

    def _loc_CEB(): pass

    label('loc_CEB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0290, 2, 0x1482)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_D00',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    Call(0, 0x0007)

    Jump('loc_D57')

    def _loc_D00(): pass

    label('loc_D00')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '『男澡堂』\n',
            '　需要使用时\n',
            '　请到服务台申请。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    def _loc_D57(): pass

    label('loc_D57')

    TalkEnd(0x00FF)

    Return()

# id: 0x0007 offset: 0xD5B
@scena.Code('func_07_D5B')
def func_07_D5B():
    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
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
        10,
        1,
        (
            TXT(0x00, '洗澡\n'),
            TXT(0x01, '离开\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_DB6'),
        (0x00000001, 'loc_FE0'),
        (-1, 'loc_FE3'),
    )

    def _loc_DB6(): pass

    label('loc_DB6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_DD3',
    )

    OP_6F(0x0009, 0)
    OP_70(0x0009, 29)
    Sleep(200)

    Jump('loc_DE6')

    def _loc_DD3(): pass

    label('loc_DD3')

    OP_6F(0x0008, 0)
    OP_70(0x0008, 29)
    Sleep(200)

    def _loc_DE6(): pass

    label('loc_DE6')

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_6F(0x0008, 0)
    OP_6F(0x0009, 0)
    Sleep(600)

    PlaySE(162, 0x00, 0x64)
    Sleep(1500)

    PlaySE(11, 0x00, 0x64)
    Sleep(800)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_EAA',
    )

    ChrSetPos(0x0000, -1000, 0, -5090, 90)
    ChrSetPos(0x0001, -1000, 0, -5090, 90)
    ChrSetPos(0x0002, -1000, 0, -5090, 90)
    ChrSetPos(0x0003, -1000, 0, -5090, 90)
    ChrSetPos(0x0004, -1000, 0, -5090, 90)
    ChrSetPos(0x0005, -1000, 0, -5090, 90)
    ChrSetPos(0x0006, -1000, 0, -5090, 90)
    ChrSetPos(0x0007, -1000, 0, -5090, 90)

    Jump('loc_F32')

    def _loc_EAA(): pass

    label('loc_EAA')

    ChrSetPos(0x0000, -1000, 0, 4900, 90)
    ChrSetPos(0x0001, -1000, 0, 4900, 90)
    ChrSetPos(0x0002, -1000, 0, 4900, 90)
    ChrSetPos(0x0003, -1000, 0, 4900, 90)
    ChrSetPos(0x0004, -1000, 0, 4900, 90)
    ChrSetPos(0x0005, -1000, 0, 4900, 90)
    ChrSetPos(0x0006, -1000, 0, 4900, 90)
    ChrSetPos(0x0007, -1000, 0, 4900, 90)

    def _loc_F32(): pass

    label('loc_F32')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['艾丝蒂尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F45',
    )

    ChrSetStatus(ChrTable['艾丝蒂尔'], 0xFB, 0)

    def _loc_F45(): pass

    label('loc_F45')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['约修亚'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F58',
    )

    ChrSetStatus(ChrTable['约修亚'], 0xFB, 0)

    def _loc_F58(): pass

    label('loc_F58')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F6B',
    )

    ChrSetStatus(ChrTable['雪拉扎德'], 0xFB, 0)

    def _loc_F6B(): pass

    label('loc_F6B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F7E',
    )

    ChrSetStatus(ChrTable['奥利维尔'], 0xFB, 0)

    def _loc_F7E(): pass

    label('loc_F7E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F91',
    )

    ChrSetStatus(ChrTable['阿加特'], 0xFB, 0)

    def _loc_F91(): pass

    label('loc_F91')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_FA4',
    )

    ChrSetStatus(ChrTable['科洛丝'], 0xFB, 0)

    def _loc_FA4(): pass

    label('loc_FA4')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_FB7',
    )

    ChrSetStatus(ChrTable['提妲'], 0xFB, 0)

    def _loc_FB7(): pass

    label('loc_FB7')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_FCA',
    )

    ChrSetStatus(ChrTable['金'], 0xFB, 0)

    def _loc_FCA(): pass

    label('loc_FCA')

    OP_69(0x0000, 0)
    OP_30(0x00)
    FadeIn(1000, 0)
    OP_0D()

    Jump('loc_FE6')

    def _loc_FE0(): pass

    label('loc_FE0')

    Jump('loc_FE6')

    def _loc_FE3(): pass

    label('loc_FE3')

    Jump('loc_FE6')

    def _loc_FE6(): pass

    label('loc_FE6')

    ClearScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

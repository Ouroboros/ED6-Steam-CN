import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T1121_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1121   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '卢格兰老人'),
    TXT(0x02, '斯丁克'),
    TXT(0x03, '亚妮拉丝'),
    TXT(0x04, '梅贝尔'),
    TXT(0x05, '莉拉'),
    TXT(0x06, '售票员泰德'),
    TXT(0x07, '小包'),
    TXT(0x08, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1121.x'
    header.mapIndex       = 1
    header.bgm            = 11
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/T1121._SN', 'ED6_DT01/T1121_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x62C8
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
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

# id: 0x10001 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH02380._CH', 'ED6_DT07/CH02380P._CP'),
        ('ED6_DT07/CH01620._CH', 'ED6_DT07/CH01620P._CP'),
        ('ED6_DT07/CH01630._CH', 'ED6_DT07/CH01630P._CP'),
        ('ED6_DT07/CH02360._CH', 'ED6_DT07/CH02360P._CP'),
        ('ED6_DT07/CH02370._CH', 'ED6_DT07/CH02370P._CP'),
        ('ED6_DT07/CH01290._CH', 'ED6_DT07/CH01290P._CP'),
        ('ED6_DT07/CH00003._CH', 'ED6_DT07/CH00003P._CP'),
        ('ED6_DT07/CH00013._CH', 'ED6_DT07/CH00013P._CP'),
        ('ED6_DT07/CH00023._CH', 'ED6_DT07/CH00023P._CP'),
        ('ED6_DT07/CH00033._CH', 'ED6_DT07/CH00033P._CP'),
        ('ED6_DT06/CH20020._CH', 'ED6_DT06/CH20020P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
    ]

# id: 0x10002 offset: 0x10A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 186,
            z                   = 0,
            y                   = 4400,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0114,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = 34900,
            z                   = 0,
            y                   = -2300,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 25010,
            z                   = 0,
            y                   = 630,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = -60835,
            z                   = 0,
            y                   = 38681,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -35500,
            z                   = 0,
            y                   = -2500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 46050,
            z                   = 0,
            y                   = 19400,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 25390,
            z                   = 750,
            y                   = -3760,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 983051,
            chipIndex           = 11,
            npcIndex            = 0x01E7,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x1EA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x1EA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x1EA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 130,
            triggerZ            = 0,
            triggerY            = 3000,
            triggerRange        = 600,
            actorX              = 186,
            actorZ              = 1500,
            actorY              = 4400,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -4470,
            triggerZ            = 0,
            triggerY            = -2690,
            triggerRange        = 1400,
            actorX              = -4470,
            actorZ              = 2000,
            actorY              = -2690,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0000,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 3520,
            triggerZ            = 0,
            triggerY            = -780,
            triggerRange        = 1400,
            actorX              = 3520,
            actorZ              = 2000,
            actorY              = -780,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0000,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x256
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_26F',
    )

    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x0009, 0x0010)

    Jump('loc_29E')

    def _loc_26F(): pass

    label('loc_26F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_279',
    )

    Jump('loc_29E')

    def _loc_279(): pass

    label('loc_279')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_288',
    )

    ClearChrFlags(0x000A, 0x0080)

    Jump('loc_29E')

    def _loc_288(): pass

    label('loc_288')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_292',
    )

    Jump('loc_29E')

    def _loc_292(): pass

    label('loc_292')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_29E',
    )

    ClearChrFlags(0x0009, 0x0080)

    def _loc_29E(): pass

    label('loc_29E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_2AC',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x0009)

    def _loc_2AC(): pass

    label('loc_2AC')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_2B8'),
        (-1, 'loc_2CA'),
    )

    def _loc_2B8(): pass

    label('loc_2B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 0, 0x308)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2C7',
    )

    SetScenaFlags(ScenaFlag(0x0061, 0, 0x308))
    Event(0, 0x0008)

    def _loc_2C7(): pass

    label('loc_2C7')

    Jump('loc_2CA')

    def _loc_2CA(): pass

    label('loc_2CA')

    Return()

# id: 0x0001 offset: 0x2CB
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0x2CC
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2E1',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_2E1(): pass

    label('loc_2E1')

    Return()

# id: 0x0003 offset: 0x2E2
@scena.Code('func_03_2E2')
def func_03_2E2():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_305',
    )

    OP_8D(0x00FE, 24030, 2670, 26360, -1350, 1500)

    Jump('func_03_2E2')

    def _loc_305(): pass

    label('loc_305')

    Return()

# id: 0x0004 offset: 0x306
@scena.Code('func_04_306')
def func_04_306():
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
            TXT(0x01, '报告\n'),
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
        'loc_4E6',
    )

    OP_0D()

    If(
        (
            (Expr.Eval, "OP_29(0x0035, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0035, 0x00, 0x20)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3F7',
    )

    ChrTalk(
        0x0008,
        (
            '#0380031976V#630F之前调查的报酬\n',
            '梅贝尔市长已经支付过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    OP_AF(0x1C, 0x0035)
    Sleep(100)

    OP_28(0x0036, 0x04, 0x10)
    OP_28(0x0036, 0x04, 0x20)

    ChrTalk(
        0x0008,
        (
            '#0380031977V#630F唔，\n',
            '接下来你们也要认真地进行调查哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4E0')

    def _loc_3F7(): pass

    label('loc_3F7')

    If(
        (
            (Expr.Eval, "OP_A9(0x1C)"),
            Expr.Return,
        ),
        'loc_472',
    )

    ChrTalk(
        0x0008,
        (
            '#0380031978V#630F嗯，辛苦了。\n',
            '看起来很顺利地完成工作了嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380031979V如果完成其他任务的话，\n',
            '可以随时再来向我报告。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4E0')

    def _loc_472(): pass

    label('loc_472')

    Sleep(200)

    ChrTalk(
        0x0008,
        (
            '#0380031980V#630F唔，\n',
            '现在好像没有可以报告的工作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380031981V如果完成其他任务的话，\n',
            '可以随时再来向我报告。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4E0(): pass

    label('loc_4E0')

    OP_56(0x00)
    TalkEnd(0x0008)

    Return()

    def _loc_4E6(): pass

    label('loc_4E6')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4F7',
    )

    TalkEnd(0x0008)

    Return()

    def _loc_4F7(): pass

    label('loc_4F7')

    Call(0, 0x0005)

    Return()

# id: 0x0005 offset: 0x4FC
@scena.Code('func_05_4FC')
def func_05_4FC():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_6C2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_66F',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '#0380040078V#630F哦，你们要去卢安吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040079V#000F嗯，卢格兰爷爷，\n',
            '谢谢您最近一段时间的照顾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040080V#010F真是麻烦您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380040081V#630F没什么没什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380040082V你们走了之后\n',
            '还真是有点寂寞呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380040083V如果再来到柏斯的话\n',
            '一定要来这里看看啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380040084V#631F无论你们什么时候来，\n',
            '我都十分欢迎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040085V#001F嗯，我知道啦。\n',
            '您也要保重哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6BF')

    def _loc_66F(): pass

    label('loc_66F')

    ChrTalk(
        0x0008,
        (
            '#0380040086V#630F去卢安的话，\n',
            '会经过比较难走的山道。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380040087V赶路的时候要小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6BF(): pass

    label('loc_6BF')

    Jump('loc_15E9')

    def _loc_6C2(): pass

    label('loc_6C2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_7F7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_794',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '#0380030565V#630F是吗，要去湖边的旅馆吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380030566V从柏斯市的南门出去，\n',
            '沿着安塞尔新街一直走下去就到了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380030567V就是瓦雷利亚湖边的建筑物，\n',
            '你们一到就应该看到了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380030568V你们路上要小心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7F4')

    def _loc_794(): pass

    label('loc_794')

    ChrTalk(
        0x0008,
        (
            '#0380030569V#630F是吗，要去湖边的旅馆吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380030570V从柏斯市的南门出去，\n',
            '沿着安塞尔新街向南走哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7F4(): pass

    label('loc_7F4')

    Jump('loc_15E9')

    def _loc_7F7(): pass

    label('loc_7F7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_B47',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006D, 5, 0x36D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AB9',
    )

    SetScenaFlags(ScenaFlag(0x006D, 5, 0x36D))

    ChrTalk(
        0x0008,
        (
            '#0380030273V#630F哦哦，是雪拉扎德啊。\n',
            '你们终于回来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380030274V之前吓了我一跳哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380030275V游击士在调查中竟被军队逮捕，\n',
            '这还真是闻所未闻的事情啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380030276V摩尔根将军也真是干得出来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030277V#022F真是非常抱歉。\n',
            '让你们这么担心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380030278V#630F没事没事，\n',
            '不管怎么说能够平安回来比什么都好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380030279V本来我们打算\n',
            '以柏斯支部的名义\n',
            '来向王都提出抗议的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380030280V就在那个时候，\n',
            '梅贝尔市长亲自出面调停了这件事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030281V#004F原、原来\n',
            '这件事引起这么多风波啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030282V#020F这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030283V不过利贝尔王国既然承认了\n',
            '游击士拥有特别的搜查权。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030284V那么将军的行动就与\n',
            '王国所作的规定相违背了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380030285V#630F嗯，不过这件事已经平息，\n',
            '也算是解决了问题，\n',
            '大家就安心继续工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B44')

    def _loc_AB9(): pass

    label('loc_AB9')

    ChrTalk(
        0x0008,
        (
            '#0380030286V#630F不管怎样，\n',
            '你们现在还是专注于\n',
            '调查强盗案件比较好一些。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380030287V你们还会和军队那些人碰面的，\n',
            '以后行动就多多小心一点哦。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B44(): pass

    label('loc_B44')

    Jump('loc_15E9')

    def _loc_B47(): pass

    label('loc_B47')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_CAB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C3F',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '#0380021434V#630F哦哦……\n',
            '你们要去拉文努村调查吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380021435V沿着西柏斯街道走，\n',
            '途中会有一个山道的入口。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380021436V你们沿着那条山道走，\n',
            '就能到那里了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380021437V#632F拉文努村……\n',
            '如果那家伙在这个支部的话，\n',
            '也许如今的情况会好转些吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CA8')

    def _loc_C3F(): pass

    label('loc_C3F')

    ChrTalk(
        0x0008,
        (
            '#0380021438V#630F拉文努村的话，\n',
            '沿着途中会有一个山道的入口。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380021439V你们沿着那条山道走，\n',
            '就能到那里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CA8(): pass

    label('loc_CA8')

    Jump('loc_15E9')

    def _loc_CAB(): pass

    label('loc_CAB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 4, 0x314)),
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 7, 0x317)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_DDC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 5, 0x315)),
            Expr.Return,
        ),
        'loc_D79',
    )

    ChrTalk(
        0x0008,
        (
            '#0380021101V#630F空贼团『卡普亚一家』吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380021102V没想到他们竟然策划\n',
            '如此大胆无耻的犯罪行为。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380021103V要想弄清楚现状\n',
            '还需要更多的线索啊。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380021104V总之现在去收集一下情报怎么样？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DD9')

    def _loc_D79(): pass

    label('loc_D79')

    ChrTalk(
        0x0008,
        (
            '#0380021105V#630F空贼团『卡普亚一家』吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380021106V没想到他们竟然策划\n',
            '如此大胆无耻的犯罪行为。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DD9(): pass

    label('loc_DD9')

    Jump('loc_15E9')

    def _loc_DDC(): pass

    label('loc_DDC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 4, 0x314)),
            Expr.Return,
        ),
        'loc_E72',
    )

    ChrTalk(
        0x0008,
        (
            '#0380021098V#630F空贼团『卡普亚一家』吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380021099V没想到他们竟然策划\n',
            '如此大胆无耻的犯罪行为。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380021100V要赶紧向梅贝尔市长\n',
            '报告情况才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15E9')

    def _loc_E72(): pass

    label('loc_E72')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 3, 0x313)),
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 4, 0x314)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_13A9',
    )

    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x0062, 4, 0x314))
    ClearMapFlags(0x00000001)
    Fade(1000)
    SetChrPos(0x0101, 940, 0, 2160, 0)
    SetChrPos(0x0102, 240, 0, 790, 0)
    SetChrPos(0x0103, -540, 0, 1860, 0)
    CameraMove(640, 0, 2790, 1000)

    ChrTalk(
        0x0008,
        (
            '#0380021078V#633F哦哦，你们几个回来了啊。\n',
            '搞清楚到底发生什么事件了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021079V#001F嘿嘿……\n',
            '得到了重要的情报哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '众人把从将军那里得到的情报\n',
            '向卢格兰老人进行了详细的说明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#0380021080V#631F空贼团『卡普亚一家』……\n',
            '这确实是重大的情报啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380021081V这样一来，\n',
            '协会的行动方针也可以决定了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380021082V#632F可是，摩尔根将军好像\n',
            '比传说中还要讨厌游击士啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021083V#007F嗯，吓死我了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021084V因为在洛连特\n',
            '游击士是个很受大家欢迎的职业，\n',
            '这次竟然会被别人批了一番……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380021085V#630F算了，摩尔根将军是个例外吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380021086V一般情况下，\n',
            '王国军和协会都还能维持着合作关系。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380021087V#634F话说回来，\n',
            '这次好像害你们多费了不少功夫，\n',
            '真是不好意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021088V#020F没什么，我们也希望能\n',
            '做些自己力所能及的事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021089V对了，最近一段时间的盗窃案件\n',
            '好像也是空贼团的所为。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380021090V#632F嗯，结合洛连特的案件来分析，\n',
            '应该错不了的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380021091V说是盗窃案件，\n',
            '其实大部分都只是些琐碎的案子……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380021092V不过，真没想到的是，\n',
            '他们竟还能做出如此胆大包天的案件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021093V#002F确实像您所说的那样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021094V他们在洛连特犯下的\n',
            '也是十分明目张胆的强盗事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021095V#013F这次竟然劫持了定期船，\n',
            '向王家要求赎金……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020021096V我总觉得这风险太过高了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021097V#026F嗯，以这个疑点为基础进行调查，\n',
            '说不定能找到什么线索。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Jump('loc_15E9')

    def _loc_13A9(): pass

    label('loc_13A9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_156B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_14F9',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '#0380020642V#630F是吗，\n',
            '你们要去哈肯门会见摩尔根将军啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380020643V说实话，\n',
            '你们能接受市长的委托，\n',
            '真的是帮了大忙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380020644V最近这段时间\n',
            '接连发生了不少事故\n',
            '和与魔兽相关的事件。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380020645V虽然都不是什么大事，\n',
            '但是这里所属的游击士\n',
            '都已经派出去工作了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380020646V本来我还想着\n',
            '如果实在忙不过来，\n',
            '就去联络其他支部要求支援呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1568')

    def _loc_14F9(): pass

    label('loc_14F9')

    ChrTalk(
        0x0008,
        (
            '#0380020647V#630F是吗，\n',
            '你们要去哈肯门会见摩尔根将军啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380020648V你们从东柏斯街道出去\n',
            '沿着钢壁之路走就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1568(): pass

    label('loc_1568')

    Jump('loc_15E9')

    def _loc_156B(): pass

    label('loc_156B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_15E9',
    )

    ChrTalk(
        0x0008,
        (
            '#0380020640V#630F这样一来，\n',
            '市长的委托就可以交托给你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380020641V市长官邸坐落在城西门附近。\n',
            '你们就去打听一下消息吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15E9(): pass

    label('loc_15E9')

    TalkEnd(0x0008)

    Return()

# id: 0x0006 offset: 0x15ED
@scena.Code('func_06_15ED')
def func_06_15ED():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_167E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 7, 0x35F)),
            Expr.Return,
        ),
        'loc_1640',
    )

    ChrTalk(
        0x00FE,
        (
            '……要走了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我期待着你们能\n',
            '早日成为正游击士哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_167B')

    def _loc_1640(): pass

    label('loc_1640')

    ChrTalk(
        0x00FE,
        (
            '你们是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……和雪拉扎德\n',
            '一起行动的准游击士吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_167B(): pass

    label('loc_167B')

    Jump('loc_1A6E')

    def _loc_167E(): pass

    label('loc_167E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 7, 0x35F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_190A',
    )

    SetScenaFlags(ScenaFlag(0x006B, 7, 0x35F))
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0101,
        (
            '#006F（啊，这个人……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F（嗯，\n',
            '　好像和我们一样都是游击士呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#002F喂，打扰一下？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F还是那样冷淡呢，\n',
            '斯丁克。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x00FE, 0x0103, 400)

    ChrTalk(
        0x00FE,
        (
            '你是……\n',
            '以前的那个见习游击士啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F没错呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '托你的福，\n',
            '现在我已经是正游击士啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼……看起来的确成熟了不少。\n',
            '在柏斯支部有工作吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F嗯，现在就正在工作呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近发生了很多事情，\n',
            '游击士的人手远远不够呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……那就靠你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x00FE, 90, 0)

    ChrTalk(
        0x0101,
        (
            '#002F（是雪拉姐的熟人吧。\n',
            '　感觉有点恐怖的人呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F（但是那走路的动作……\n',
            '　看起来应该很厉害吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A6E')

    def _loc_190A(): pass

    label('loc_190A')

    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A1A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是你们啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难得来到这里，\n',
            '本来想开个欢迎会的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过现在库拉茨和亚妮拉丝\n',
            '都因为工作出去了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F（……其实他人挺好的吧？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 0)

    ChrTalk(
        0x0103,
        (
            '#020F（呵呵，别看他那个样子，\n',
            '　其实很会关心人的。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x00FE, 90, 0)

    Jump('loc_1A6E')

    def _loc_1A1A(): pass

    label('loc_1A1A')

    ChrTalk(
        0x00FE,
        (
            '最近发生了很多事情，\n',
            '游击士的人手远远不够呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……那就靠你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x00FE, 90, 0)

    def _loc_1A6E(): pass

    label('loc_1A6E')

    TalkEnd(0x0009)

    Return()

# id: 0x0007 offset: 0x1A72
@scena.Code('func_07_1A72')
def func_07_1A72():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_1C10',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1BCB',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006C, 0, 0x360)),
            Expr.Return,
        ),
        'loc_1B2F',
    )

    ChrTalk(
        0x00FE,
        (
            '#0120040088V#814F啊，你们要走了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120040089V#818F真是遗憾啊……\n',
            '本来还想和你们一起工作的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120040090V#810F今后还会有很多事情等着你们，\n',
            '一定不要泄气，加油干哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BC8')

    def _loc_1B2F(): pass

    label('loc_1B2F')

    ChrTalk(
        0x00FE,
        (
            '#0120040091V#814F啊，难道你们就是\n',
            '和雪拉前辈一起很活跃的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120040092V#810F嗯～真是年轻啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120040093V今后还会有很多事情等着你们，\n',
            '一定不要泄气，加油干哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1BC8(): pass

    label('loc_1BC8')

    Jump('loc_1C0D')

    def _loc_1BCB(): pass

    label('loc_1BCB')

    ChrTalk(
        0x00FE,
        (
            '#0120040094V今后还会有很多事情等着你们，\n',
            '一定不要泄气，加油干哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1C0D(): pass

    label('loc_1C0D')

    Jump('loc_247F')

    def _loc_1C10(): pass

    label('loc_1C10')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006C, 0, 0x360)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1FF5',
    )

    ChrTurnDirection(0x00FE, 0x0103, 0)
    SetScenaFlags(ScenaFlag(0x006C, 0, 0x360))
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    ChrTurnDirection(0x00FE, 0x0103, 0)

    ChrTalk(
        0x00FE,
        (
            '#0120030288V#850F很久不见了，雪拉扎德前辈。\n',
            '自从您去修行之后就再没见面了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030289V#020F这不是亚妮拉丝吗。\n',
            '真的是很久没见了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030290V对了，\n',
            '你已经找到所谓的剑之道了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0120030291V#819F呵呵，请别问了。\n',
            '我还处在修行阶段呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120030292V#817F在没有确凿证据的情况下，\n',
            '王国军居然把游击士抓进监狱……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120030293V#818F那个胡子将军也真是的，\n',
            '他到底在想些什么呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030294V#025F算了，\n',
            '反正那也是一场误会罢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0120030295V#810F呵呵，\n',
            '总之大家没事就好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120030296V有件事我想问问……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#0120030297V听说前辈您带的两个新人\n',
            '好像是卡西乌斯先生的孩子，\n',
            '是不是呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030298V#006F啊，是的。\n',
            '我叫艾丝蒂尔·布莱特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0102, 400)

    ChrTalk(
        0x0102,
        (
            '#0020030299V#010F我叫约修亚。\n',
            '我其实是卡西乌斯先生收养的儿子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#0120030300V#818F啊，原来如此……\n',
            '就是你们两个啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120030301V本来我以为你们年纪太小，\n',
            '是不会成为什么厉害的游击士的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120030302V#811F这次亲眼看到你们，\n',
            '才感到你们的未来\n',
            '真是无可限量呀～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030303V#000F（……这个人\n',
            '　果然也知道老爸的事情。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030304V#010F（嗯，应该是这样。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_247F')

    def _loc_1FF5(): pass

    label('loc_1FF5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_23CE',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    ChrTurnDirection(0x00FE, 0x0103, 0)

    ChrTalk(
        0x00FE,
        (
            '#0120030305V#810F雪拉扎德前辈，真是一场灾难啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120030306V#817F在没有确凿证据的情况下，\n',
            '王国军居然把游击士抓进监狱……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120030307V#818F那个胡子将军也真是的，\n',
            '他到底在想些什么呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030308V#025F算了，\n',
            '反正那也是一场误会罢了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030309V#020F说起来，\n',
            '听说是你去通知的市长……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0120030310V#810F啊，对，是我。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120030311V正好那时我有任务在身，\n',
            '碰巧就在那村子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030312V#021F哈哈，给你添麻烦了，\n',
            '真是不好意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0120030313V#810F呵呵，前辈您就别这么客气啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120030314V有件事我想问问……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#0120030315V听说前辈您带的两个新人\n',
            '是卡西乌斯先生的孩子，\n',
            '有没有这回事呢……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030316V#006F啊，是的。\n',
            '我叫艾丝蒂尔·布莱特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0102, 400)

    ChrTalk(
        0x0102,
        (
            '#0020030317V#010F我叫约修亚。\n',
            '我其实是卡西乌斯先生的养子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#0120030318V#818F啊，原来如此……\n',
            '就是你们两个啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120030319V本来我以为你们年纪太小，\n',
            '是不会成为什么厉害的游击士的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120030320V#811F这次亲眼看到你们，\n',
            '才感到你们的未来\n',
            '真是无可限量呀～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030321V#000F（……这个人\n',
            '　果然也知道老爸的事情。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030322V#010F（嗯，应该是这样。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_247F')

    def _loc_23CE(): pass

    label('loc_23CE')

    ChrTurnDirection(0x000A, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '#0120030323V#810F你们是卡西乌斯先生的孩子吧。\n',
            '本来我以为你们年纪太小，\n',
            '是不会成为什么厉害的游击士的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120030324V#811F这次亲眼看到你们，\n',
            '才感到你们的未来\n',
            '真是无可限量呀～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_247F(): pass

    label('loc_247F')

    TalkEnd(0x000A)

    Return()

# id: 0x0008 offset: 0x2483
@scena.Code('func_08_2483')
def func_08_2483():
    EventBegin(0x00)
    SetChrPos(0x0101, -1120, 0, -4740, 0)
    SetChrPos(0x0102, 22, 0, -4880, 0)
    SetChrPos(0x0103, -57, 0, -3932, 0)

    @scena.Lambda('lambda_24BE')
    def lambda_24BE():
        CameraMove(0, 0, 2800, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_24BE)

    Sleep(2000)

    OP_4A(0x0008, 0)
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0380020385V#633F噢，雪拉扎德。\n',
            '你比我预想中来得要早啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380020386V特地从洛连特走路过来，\n',
            '真是辛苦你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_255D')
    def lambda_255D():
        ChrWalkTo(0x0103, -470, 0, 1910, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_255D)

    Sleep(500)

    @scena.Lambda('lambda_257D')
    def lambda_257D():
        ChrWalkTo(0x0101, -1120, 0, 710, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_257D)

    Sleep(500)

    @scena.Lambda('lambda_259D')
    def lambda_259D():
        ChrWalkTo(0x0102, 22, 0, 710, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_259D)

    WaitForThreadExit(0x0103, 0x0001)

    ChrTalk(
        0x0103,
        (
            '#0030020387V#020F#2P卢格兰爷爷，好久不见了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020388V难道说您已经\n',
            '收到我们要来的通知了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380020389V#630F嗯，早些时候爱娜通知我了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380020390V那么，那边的小姑娘和小兄弟\n',
            '就是卡西乌斯的孩子吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020391V#020F#2P是的，正如您所说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020392V#000F#3P嗯，初次见面。\n',
            '我是艾丝蒂尔·布莱特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020393V#010F我是约修亚·布莱特。\n',
            '请您多多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380020394V#631F我是柏斯支部的负责人，\n',
            '叫做卢格兰的老头子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380020395V其实我和你们的父亲\n',
            '也算是交情颇深哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380020396V你们就叫我卢格兰爷爷吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020397V#501F#3P嗯，卢格兰爷爷。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020398V#002F那么……\n',
            '请您赶快告诉我们那个事件\n',
            '到底是怎么一回事吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380020399V#632F嗯，事情是这样的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380020400V国王军对失踪定期船的搜索行动\n',
            '目前还在进行当中。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380020401V#634F但是由于军队实行情报控制，\n',
            '至今没有半点儿消息传出来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380020402V一般的市民也就算了，\n',
            '连游击士协会也得不到任何消息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020403V#004F#3P哎～！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020404V怎么回事啊，\n',
            '军队不是和游击士协会有合作关系吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020405V#022F#2P唉，那只不过是表面的政策而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020406V事实上，在很多情况下，\n',
            '还是双方对立的局面比较多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020407V#012F也就是说，在互相争夺势力范围吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380020408V#632F虽然很遗憾，但事实如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380020409V而且更麻烦的是，\n',
            '这次事件是由摩尔根将军来负责的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0103,
        (
            '#0030020410V#023F#2P啊，摩尔根将军……\n',
            '这下子事情可不好办了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020411V#004F#3P什么，那个摩尔根将军是谁啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020020412V#010F他可是十年前击退帝国军的功臣，\n',
            '是个赫赫有名的人物。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020020413V在历史书里不是也出现过吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010020414V#007F#3P唔……\n',
            '好像完全没有印象呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020415V#002F不过，那位将军究竟有什么问题呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030020416V#025F#2P据说那位将军……\n',
            '非常地讨厌游击士。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020417V而且他一直在主张\n',
            '游击士协会没有存在的必要。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010020418V#009F#3P真、真是个不讲道理的大叔～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020419V那么说，就是那个将军\n',
            '害我们一点情报都得不到吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380020420V#634F……也不能那么说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 400)
    ChrTurnDirection(0x0102, 0x0008, 400)
    ChrTurnDirection(0x0103, 0x0008, 400)

    ChrTalk(
        0x0008,
        (
            '#0380020421V#632F因为军队进行调查的地方\n',
            '是不能让无关人员进入的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380020422V所以说，\n',
            '就算是其它工作也没办法顺利进行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020423V#009F#3P怎，怎么这样……\n',
            '好不容易才从洛连特来到这里……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020424V既然这样，我要和那个将军一决胜负，\n',
            '决定到底由谁来调查这个事件！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020425V#017F你千万不要乱来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380020426V#630F好了，不用那么心急。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380020427V其实，关于这个事件，\n',
            '支部收到了来自柏斯市长的委托。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380020428V市长希望在军队搜索定期船的同时，\n',
            '游击士协会也能够参与调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020429V#020F#2P真的？这下我就放心了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020430V有了柏斯市长的正式委托书，\n',
            '我们的行动就有正当的理由了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020431V#006F#3P真的吗，这还真是场及时雨啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020432V卢格兰爷爷。\n',
            '我们能接受那个委托吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380020433V#634F嗯，当然可以。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380020434V#630F不过在那之前……\n',
            '你们已经是准游击士了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020435V#000F#3P嗯，有什么问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380020436V#630F作为准游击士，\n',
            '必须在各个支部进行实习。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380020437V也就是说，\n',
            '是受所属支部监督的身份。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380020438V你们现在还是\n',
            '隶属于洛连特支部的游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020439V#004F#3P这么说的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020440V#010F是不是想接受这个委托，\n',
            '就必须变更所属的支部才行呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380020441V#630F正是如此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0008, 1449, 0, 4210, 2000, 0x00)
    SetChrDirection(0x0008, 180, 400)

    ChrTalk(
        0x0008,
        (
            '#0380020442V#630F来，你们两个。\n',
            '在这份转属手续的文件上签字吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020443V#501F#3P哦，好的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3158')
    def lambda_3158():
        ChrWalkTo(0x00FE, 1710, 0, 2320, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3158)

    Sleep(500)

    @scena.Lambda('lambda_3178')
    def lambda_3178():
        CameraMove(2210, 0, 3140, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_3178)

    ChrWalkTo(0x0101, -460, 0, 890, 3000, 0x00)
    ChrWalkTo(0x0101, 870, 0, 2300, 3000, 0x00)

    @scena.Lambda('lambda_31B8')
    def lambda_31B8():
        ChrTurnDirection(0x0103, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_31B8)

    SetChrDirection(0x0101, 0, 400)
    SetChrDirection(0x0102, 0, 400)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020020444V#010F#4P在这里填入名字就可以了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔和约修亚\n',
            '在转属手续的文书上签了字。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#0380020445V#630F嗯，这就行了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380020446V游击士艾丝蒂尔，以及约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380020447V以上两人于本日１５：２０\n',
            '正式成为柏斯支部所属的游击士。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380020448V#631F……这样一来，\n',
            '你们就是柏斯支部的游击士了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020449V#021F顺便说一下，一旦成为正游击士，\n',
            '即使没有隶属关系也可以接受工作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020450V当然相应的责任和义务也就增多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)
    ChrTurnDirection(0x0102, 0x0103, 400)

    ChrTalk(
        0x0102,
        (
            '#0020020451V#010F#4P原来如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020452V#007F#4P我们还是矮人一截啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_33EB')
    def lambda_33EB():
        CameraMove(490, 0, 3220, 1000)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_33EB)

    ChrWalkTo(0x0008, 186, 0, 4400, 2000, 0x00)
    SetChrDirection(0x0008, 180, 400)

    ChrTalk(
        0x0008,
        (
            '#0380020453V#630F这样一来，\n',
            '市长的委托就可以交托给你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380020454V市长官邸坐落在西面入口附近。\n',
            '你们就去打听一下消息吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 400)
    ChrTurnDirection(0x0102, 0x0008, 400)
    ChrTurnDirection(0x0103, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010020455V#006F嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020456V#010F明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0052, 0x03, 0x02)
    OP_28(0x0052, 0x03, 0x04)
    OP_28(0x0035, 0x04, 0x02)
    OP_28(0x0035, 0x04, 0x04)
    OP_28(0x0035, 0x01, 0x0001)
    OP_28(0x0035, 0x01, 0x0002)
    OP_28(0x0035, 0x01, 0x0004)
    OP_4B(0x0008, 0)
    EventEnd(0x00)

    Return()

# id: 0x0009 offset: 0x3503
@scena.Code('func_09_3503')
def func_09_3503():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x000B, -710, 0, -80, 45)
    SetChrPos(0x000C, -1790, 0, -290, 45)
    SetChrPos(0x0101, 500, 0, 2000, 225)
    SetChrPos(0x0102, -910, 0, 2000, 180)
    SetChrPos(0x0103, 1580, 0, 1390, 225)
    SetChrPos(0x0104, 1700, 0, 190, 270)
    CameraMove(830, 0, 5070, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(261, 0)
    OP_4A(0x000B, 255)
    OP_4A(0x000C, 255)
    OP_4A(0x000D, 255)
    OP_4A(0x0008, 255)
    FadeIn(2000, 0)
    CameraMove(830, 0, 2120, 2000)
    OP_0D()

    ChrTalk(
        0x000B,
        (
            '#0360031775V#611F#4P——真是辛苦你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360031776V我就相信自己不会看错人。\n',
            '你们真不愧为一流的游击士。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360031777V由你们来出马的话，\n',
            '一定可以把问题妥善解决。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031778V#007F#5P可是可是，\n',
            '最后好处都被军队给占光了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031779V根本不算是我们解决的呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0360031780V#610F#4P才不是那回事呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360031781V假如没有大家的帮忙，\n',
            '军队也不会那么顺利地突入。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360031782V而且，搞不好会让\n',
            '那些反抗的空贼伤害人质。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380031783V#631F嗯，你们的潜入的确为\n',
            '压制空贼基地起了很大作用。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380031784V你们应该引以为傲啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031785V#008F#5P是吗……嘿嘿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030031786V#025F的确顺利解救了人质，\n',
            '也逮捕了空贼团一伙人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031787V遗憾的是，\n',
            '还有几个遗留下来的谜团没有解开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031788V#012F#1P是在湖畔出现的男人，\n',
            '还有空贼首领奇怪的态度吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031789V这起事件，\n',
            '似乎还隐藏着一些不为人知的内幕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380031790V#632F也是啊……\n',
            '不过那些问题也只能交给王国军处理了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380031791V那些空贼已经被关押起来了，\n',
            '所以我们也无法做深入的调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0360031792V#610F#4P总之，所有人质平安获救，\n',
            '这已经是万幸的事情了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360031793V多亏了逮捕空贼的新闻，\n',
            '现在城市又重新恢复活力了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360031794V我代表柏斯市民由衷感谢你们，\n',
            '请接受我们小小的谢礼吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031795V#501F#5P咦，这样好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0360031796V#611F#4P呵呵，当然可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    SetChrDirection(0x000B, 90, 200)

    ChrTalk(
        0x000B,
        (
            '#0360031797V#610F#4P还有奥利维尔先生……\n',
            '真是太感谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040031798V#031F#2P呵呵……\n',
            '这就作为我不小心喝掉\n',
            '『格兰·夏利拿』的补偿好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0360031799V#611F#4P是啊，还有找零呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    SetChrDirection(0x000B, 45, 200)

    ChrTalk(
        0x000B,
        (
            '#0360031800V#611F#4P那么各位，请保重了。\n',
            '再有什么事的话还请多多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0370031801V#621F#6P……我们告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3B91')
    def lambda_3B91():
        ChrTurnDirection(0x00FE, 0x000B, 400)
        Yield()

        Jump('lambda_3B91')

    DispatchAsync2(0x0101, 0x0001, lambda_3B91)

    @scena.Lambda('lambda_3BA2')
    def lambda_3BA2():
        ChrTurnDirection(0x00FE, 0x000B, 400)
        Yield()

        Jump('lambda_3BA2')

    DispatchAsync2(0x0102, 0x0001, lambda_3BA2)

    @scena.Lambda('lambda_3BB3')
    def lambda_3BB3():
        ChrTurnDirection(0x00FE, 0x000B, 400)
        Yield()

        Jump('lambda_3BB3')

    DispatchAsync2(0x0103, 0x0001, lambda_3BB3)

    @scena.Lambda('lambda_3BC4')
    def lambda_3BC4():
        ChrTurnDirection(0x00FE, 0x000B, 400)
        Yield()

        Jump('lambda_3BC4')

    DispatchAsync2(0x0104, 0x0001, lambda_3BC4)

    SetChrDirection(0x000B, 180, 400)

    @scena.Lambda('lambda_3BDC')
    def lambda_3BDC():
        ChrWalkTo(0x00FE, -800, 0, -8480, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_3BDC)

    Sleep(300)

    SetChrDirection(0x000C, 180, 400)

    @scena.Lambda('lambda_3C03')
    def lambda_3C03():
        ChrWalkTo(0x00FE, -800, 0, -8480, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_3C03)

    WaitForThreadExit(0x000B, 0x0001)
    SetChrFlags(0x000B, 0x0080)
    PlaySE(6, 0x00, 0x64)
    WaitForThreadExit(0x000C, 0x0001)
    SetChrFlags(0x000C, 0x0080)
    Sleep(300)

    PlaySE(7, 0x00, 0x64)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0103, 0xFF)
    TerminateThread(0x0104, 0xFF)

    ChrTalk(
        0x0101,
        (
            '#0010031802V#008F#5P啊～感觉就像是\n',
            '一场隆重的表彰仪式呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0102, 90, 400)

    ChrTalk(
        0x0102,
        (
            '#0020031803V#010F#1P如果事件迟迟得不到解决，\n',
            '贸易流通必定变得更加混乱。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031804V市长这么高兴也是理所当然的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0101, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010031805V#001F#5P嘿嘿，我也觉得非常开心呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031806V靠我们的努力能\n',
            '帮到大家的忙、让大家开心，\n',
            '也算是尽到了游击士的职责呢⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3D86')
    def lambda_3D86():
        SetChrDirection(0x00FE, 315, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_3D86)

    SetChrDirection(0x0103, 270, 400)

    ChrTalk(
        0x0103,
        (
            '#0030031807V#027F呵呵，还太嫩了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031808V不过呢，\n',
            '你们已经不算是什么新人了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031809V坦白说，你们这次的表现很惊人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010031810V#008F#5P嘿嘿，真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380031811V#630F总而言之，\n',
            '先接受这次事件的评定和报酬吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3E75')
    def lambda_3E75():
        CameraMove(770, 0, 3160, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3E75)

    @scena.Lambda('lambda_3E8D')
    def lambda_3E8D():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3E8D)

    @scena.Lambda('lambda_3E9B')
    def lambda_3E9B():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_3E9B)

    @scena.Lambda('lambda_3EA9')
    def lambda_3EA9():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_3EA9)

    ChrTurnDirection(0x0101, 0x0008, 400)
    WaitForThreadExit(0x0101, 0x0003)
    Sleep(100)

    If(
        (
            (Expr.Eval, "OP_29(0x0035, 0x00, 0x20)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3EE0',
    )

    OP_AF(0x1C, 0x0035)
    Sleep(100)

    OP_28(0x0036, 0x04, 0x10)
    OP_28(0x0036, 0x04, 0x20)

    def _loc_3EE0(): pass

    label('loc_3EE0')

    OP_AF(0x1C, 0x0037)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    OP_28(0x0038, 0x04, 0x10)
    OP_28(0x0038, 0x04, 0x20)
    OP_28(0x0039, 0x04, 0x10)
    OP_28(0x0039, 0x04, 0x20)
    OP_28(0x0039, 0x01, 0x0400)

    ChrTalk(
        0x0008,
        (
            '#0380031812V#630F市长也说过了，\n',
            '这次要付给你们很多的酬劳。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380031813V#630F还有这个……\n',
            '是我代表支部给你们的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '正游击士资格的推荐信',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    AddItem(0x0333, 1)

    ChrTalk(
        0x0101,
        (
            '#0010031814V#004F#4P这个是……\n',
            '柏斯支部的推荐信！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031815V#014F#6P这样可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380031816V#631F那还用说。\n',
            '光是凭解决这起事件的功劳，\n',
            '已经足够让我们支部来推荐你们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380031817V总之你们接受吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031818V#001F#4P谢谢，卢格兰爷爷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031819V#010F#6P为了不愧对这封推荐信，\n',
            '我们以后也会继续努力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0103, 270, 400)

    ChrTalk(
        0x0103,
        (
            '#0030031820V#021F#2P呵呵，真是太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031821V如果让卡西乌斯老师听到了，\n',
            '他也一定会很高兴的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0101, 135, 400)

    ChrTalk(
        0x0101,
        (
            '#0010031822V#003F……唔…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0102, 135, 400)

    ChrTalk(
        0x0102,
        (
            '#0020031823V#013F……是啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380031824V#634F卡西乌斯……\n',
            '他现在到底在哪里呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380031825V协会就先不说了，\n',
            '没想到连家人也不联系一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030031826V#522F#2P是啊……真不像老师的作风。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031827V在柏斯突然下机后，\n',
            '老师到底去了哪里呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(6, 0x00, 0x64)
    Sleep(500)

    SetChrPos(0x000D, -800, 0, -8480, 0)

    NpcTalk(
        0x000D,
        '青年的声音',
        (
            '#1330031828V#1P打扰了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_42B5')
    def lambda_42B5():
        CameraMove(830, 0, 2120, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_42B5)

    @scena.Lambda('lambda_42CD')
    def lambda_42CD():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_42CD')

    DispatchAsync2(0x0101, 0x0001, lambda_42CD)

    @scena.Lambda('lambda_42DE')
    def lambda_42DE():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_42DE')

    DispatchAsync2(0x0102, 0x0001, lambda_42DE)

    @scena.Lambda('lambda_42EF')
    def lambda_42EF():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_42EF')

    DispatchAsync2(0x0103, 0x0001, lambda_42EF)

    @scena.Lambda('lambda_4300')
    def lambda_4300():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_4300')

    DispatchAsync2(0x0104, 0x0001, lambda_4300)

    ClearChrFlags(0x000D, 0x0080)
    ChrWalkTo(0x000D, -520, 0, -1060, 3000, 0x00)

    ChrTalk(
        0x0008,
        (
            '#0380031829V#633F空港的接待员……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380031830V怎么了，有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#1330031831V是这样的，\n',
            '被空贼抢走的定期船货物都拿回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#1330031832V其中有一份是给游击士\n',
            '协会的邮件和包裹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#1330031833V请签收一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0380031834V#631F那真是辛苦你了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380031835V#632F啊，慢着……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380031836V从柏斯出发的定期船里\n',
            '怎么会有给我们支部的东西？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#1330031837V哎呀，不是呢。\n',
            '是寄往洛连特支部的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#1330031838V对了，请问一下\n',
            '卡西乌斯·布莱特的家属\n',
            '现在在这里吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010031839V#004F#5P哎哎！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020031840V#014F#1P我们就是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#1330031841V啊，那真是太巧了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#1330031842V刚才联络洛连特支部的时候，\n',
            '他们说你们很早就已经来了柏斯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#1330031843V那么，请你们签收吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_92(0x000D, 0x0101, 800, 3000, 0x00)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0103, 0xFF)
    TerminateThread(0x0104, 0xFF)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '得到了信件和包裹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    ChrMoveTo(0x000D, 80, 0, 430, 2000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010031844V#501F#5P这封信……\n',
            '嗯，是老爸的字呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031845V收信人是洛连特支部的\n',
            '我和约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031846V#010F#1P看来应该是\n',
            '在下机之前写好的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031847V#019F原来如此……\n',
            '其实父亲也正打算和我们联络的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031848V#008F#5P是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030031849V#021F呵呵，真是太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031850V#020F那个包裹也是\n',
            '老师送来的东西吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031851V#000F#5P唔……\n',
            '好像是别人送给老爸的东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031852V#004F…………………………\n',
            '……咦，好奇怪啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031853V#012F#1P……嗯，\n',
            '上面没有写寄件人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#1330031854V你们把邮件收好吧，我告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x000D, 180, 400)

    @scena.Lambda('lambda_4844')
    def lambda_4844():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_4844')

    DispatchAsync2(0x0101, 0x0001, lambda_4844)

    @scena.Lambda('lambda_4855')
    def lambda_4855():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_4855')

    DispatchAsync2(0x0102, 0x0001, lambda_4855)

    @scena.Lambda('lambda_4866')
    def lambda_4866():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_4866')

    DispatchAsync2(0x0103, 0x0001, lambda_4866)

    @scena.Lambda('lambda_4877')
    def lambda_4877():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_4877')

    DispatchAsync2(0x0104, 0x0001, lambda_4877)

    ChrWalkTo(0x000D, -420, 0, -1060, 2000, 0x00)
    OP_62(0x000D, 0x00000000, 2300, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    SetChrDirection(0x000D, 0, 400)

    ChrTalk(
        0x000D,
        (
            '#1330031855V啊啊，还有的是，\n',
            '逮捕空贼那件事真是辛苦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#1330031856V真不愧是游击士啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x000D, 180, 400)
    ChrWalkTo(0x000D, -800, 0, -8480, 3000, 0x00)
    PlaySE(7, 0x00, 0x64)
    SetChrFlags(0x000D, 0x0080)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0103, 0xFF)
    TerminateThread(0x0104, 0xFF)

    @scena.Lambda('lambda_494A')
    def lambda_494A():
        CameraMove(770, 0, 3160, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_494A)

    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0008,
        (
            '#0380031857V#630F真没想到定期船的货物里\n',
            '会有卡西乌斯的线索。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0380031858V大家如果要看信的话，\n',
            '就到二楼的休息所吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_49D6')
    def lambda_49D6():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_49D6)

    @scena.Lambda('lambda_49E4')
    def lambda_49E4():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_49E4)

    @scena.Lambda('lambda_49F2')
    def lambda_49F2():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_49F2)

    ChrTurnDirection(0x0101, 0x0008, 400)
    Sleep(200)

    ChrTalk(
        0x0101,
        (
            '#0010031859V#501F谢谢，卢格兰爷爷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040031860V#035F哈·哈·哈，\n',
            '那么我们赶快看看这里面的东西吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Call(0, 0x000A)

    Return()

# id: 0x000A offset: 0x4A79
@scena.Code('func_0A_4A79')
def func_0A_4A79():
    EventBegin(0x00)
    SetChrFlags(0x0101, 0x0004)
    SetChrFlags(0x0102, 0x0004)
    SetChrFlags(0x0103, 0x0004)
    SetChrFlags(0x0104, 0x0004)
    SetChrPos(0x0101, 26780, 200, -3520, 270)
    SetChrPos(0x0102, 26780, 200, -4800, 270)
    SetChrPos(0x0103, 24180, 200, -3500, 90)
    SetChrPos(0x0104, 24180, 200, -4700, 90)
    SetChrChipByIndex(0x0101, 6)
    SetChrChipByIndex(0x0102, 7)
    SetChrChipByIndex(0x0103, 8)
    SetChrChipByIndex(0x0104, 9)
    SetChrSubChip(0x0101, 1)
    CameraMove(26360, 200, -3250, 0)
    OP_67(0, 5820, -10000, 0)
    CameraSetDistance(1730, 0)
    OP_6C(45000, 0)
    OP_6E(459, 0)
    ClearChrFlags(0x000E, 0x0080)
    Sleep(500)

    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010031861V#007F#5P……真是的，\n',
            '为什么你也要跟着过来啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040031862V#030F#6P哎呀，纯粹是感兴趣嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040031863V比如你们的父亲\n',
            '为什么会在出发前下机……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040031864V又为什么要送这东西过来，\n',
            '我简直好奇得连觉也睡不着呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031865V#505F#5P就、就算你说这种话也……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040031866V#034F#6P啊啊，你怎么能对一个曾经\n',
            '出生入死的同伴如此薄情寡意……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040031867V能成功潜入基地\n',
            '到底是多亏了谁～～呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031868V#509F#5P唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030031869V#027F真是个爱记旧帐的坏男人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031870V#015F真没办法……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031871V#012F不过，看过内容后，\n',
            '请你谨记不能说出去哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040031872V#031F#6P呵呵，这是当然的啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031873V#007F#5P哈啊，先做一下深呼吸……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔先把信封打开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Sleep(500)

    OP_1F(0x50, 0x0000012C)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '#0160031874V',
            (TxtCtl.SetColor, 0x5),
            '致艾丝蒂尔、约修亚：',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0160031875V',
            (TxtCtl.SetColor, 0x5),
            '交给你们的工作\n',
            '也差不多快完成了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0160031876V',
            (TxtCtl.SetColor, 0x5),
            '起初可能忽略工作上的细节，\n',
            '但只要一步一步地积累经验，\n',
            '我想你们一定能够做得更好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0160031877V',
            (TxtCtl.SetColor, 0x5),
            '我这里的工作\n',
            '稍微遇到了一些麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0160031878V',
            (TxtCtl.SetColor, 0x5),
            '总之短时间内\n',
            '大概是不能回家了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0160031879V',
            (TxtCtl.SetColor, 0x5),
            '对了……\n',
            '我想起码要到女王的\n',
            '诞辰庆典结束之后才能回来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0160031880V',
            (TxtCtl.SetColor, 0x5),
            '在这里先说声抱歉了。\n',
            '不过你们也要知道自己\n',
            '已经到了不用爸爸带着的年龄了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0160031881V',
            (TxtCtl.SetColor, 0x5),
            '——在我回来之前，\n',
            '你们要过怎样的生活，\n',
            '就由自己来决定吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0160031882V',
            (TxtCtl.SetColor, 0x5),
            '可以继续留在洛连特工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0160031883V',
            (TxtCtl.SetColor, 0x5),
            '也可以为了得到\n',
            '正游击士的资格环游王国旅行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0160031884V',
            (TxtCtl.SetColor, 0x5),
            '１６岁是收获的季节啊，\n',
            '希望你们能过得充实有意义。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0160031885V',
            (TxtCtl.SetColor, 0x5),
            '好了，先写到这吧。\n',
            '记得帮我向雪拉扎德\n',
            '还有爱娜问好哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0160031886V',
            (TxtCtl.SetColor, 0x5),
            '卡西乌斯·布莱特',
            (TxtCtl.SetColor, 0x5),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_1F(0x64, 0x0000012C)
    Sleep(500)

    ChrTalk(
        0x0103,
        (
            '#0030031887V#020F……是老师的文笔呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031888V虽然看上去轻松随意，\n',
            '但却充满了对我们的思念啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031889V#008F#5P嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031890V#010F是啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040031891V#030F#6P哦，女王诞辰庆典啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040031892V听这番话的口气，\n',
            '好像还有一段时间吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030031893V#020F大概两三个月吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031894V这段时间，\n',
            '即使出去旅行都够了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031895V究竟老师他在哪里，\n',
            '现在又在做些什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031896V#003F#5P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031897V#013F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040031898V#030F#6P先不说这个……\n',
            '那个包裹装着什么东西呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040031899V没有写寄件人，\n',
            '的确是太耐人寻味了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031900V#506F#5P哈哈，的确很让人在意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031901V不过随便乱动\n',
            '老爸的东西会不会有点……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040031902V#035F#6P但是你仔细想想嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040031903V在父亲失踪的同时，\n',
            '收到一个寄件人不明的包裹。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040031904V这之间或许有什么关联哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031905V#505F#5P这、这倒是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030031906V#025F喂喂，奥利维尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031907V你怎么能为了自己的好奇心\n',
            '而找诸多的借口怂恿别人呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031908V#012F不，我觉得奥利维尔说的\n',
            '确实也有他的道理。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031909V就这样一直放到\n',
            '父亲回来才打开的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031910V我觉得还是先打开看看比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031911V#505F#5P………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031912V#006F明白了，打开看看吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0101, 0)
    Sleep(100)

    SetChrSubChip(0x0102, 2)
    Sleep(500)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔打开寄件人不明的包裹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_20(0x000005DC)
    Fade(1000)
    SetChrPos(0x000E, 25190, 750, -3960, 0)
    SetChrSubChip(0x000E, 16)
    OP_0D()
    OP_AD('ED6_DT04/C_VIS012._CH', 0x00BE, 0x0064, 0x000001F4)
    Sleep(1000)

    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '包裹里装着一个\n',
            '闪着漆黑色光泽的半球体状的装置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '同时还附有一张纸条。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_AE(0x000001F4)
    PlayBGM(33)
    Sleep(1000)

    AddItem(0x035B, 1)

    ChrTalk(
        0x0101,
        (
            '#0010031913V#004F#5P这、这个是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031914V#012F是导力器。\n',
            '虽然用途还不清楚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031915V有张纸条……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '#0330031916V',
            (TxtCtl.SetColor, 0x5),
            '这是那个集团运来的物品，\n',
            '麻烦暂时保管一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0330031917V',
            (TxtCtl.SetColor, 0x5),
            '找到机会的话，\n',
            '希望能送给Ｒ博士进行解析。　　Ｋ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#0010031918V#580F#5P就、就这些？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031919V#013F嗯……\n',
            '没写其他的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031920V#012F雪拉姐姐。\n',
            '这里所写的Ｋ和Ｒ博士，\n',
            '你觉得这两个是什么人呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030031921V#025F唔……\n',
            '很遗憾我并不清楚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031922V老师的人面非常广，\n',
            '这两个人有可能是外国人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031923V#007F#5P暗示只有这么一点，\n',
            '的确让人摸不着头脑。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031924V#505F这个黑色的\n',
            '导力器到底是什么东西呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030031925V#022F从形状来判断的话，\n',
            '不像是一般的导力器。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031926V感觉有点像\n',
            '战术导力器一类的东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040031927V#032F#6P不，应该不是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040031928V一般的战术导力器都会有\n',
            '用来镶嵌结晶回路的结晶孔……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040031929V但是，这个什么也没有。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040031930V这个难道是……\n',
            '传说中的『古代遗物』？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031931V#004F#5P古代遗物？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040031932V#035F#6P就是我们现在\n',
            '所用的导力器的原型。\n',
            '换句话说，是古代文明的导力器。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040031933V从遗迹发掘出的古代遗物极为珍稀，\n',
            '而且大多数是由七耀教会保管的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040031934V通俗点说，也就是古董了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030031935V#022F不过这个看上去\n',
            '并不像十分古老的东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031936V反而比较像最近才制造的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040031937V#030F#6P确实是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040031938V不过……\n',
            '可以肯定的是这不是什么简单的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1700, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1500)

    ChrTalk(
        0x0101,
        (
            '#0010031939V#582F#5P#3S啊～真受不了！\n',
            '那个乱来的老爸！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010031940V#582F#5P#3S真是的！\n',
            '总是让我们操心！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031941V#014F艾、艾丝蒂尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031942V#003F#5P竟然送来这种\n',
            '寄件人不明的奇怪东西……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031943V老爸到底卷入了\n',
            '什么样的事件里呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030031944V#522F艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031945V#015F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    OP_21()

    ChrTalk(
        0x0102,
        (
            '#0020031946V#010F我说，艾丝蒂尔。\n',
            '我有一个提议……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031947V我们就这样继续旅行下去吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    SetChrSubChip(0x0101, 1)

    ChrTalk(
        0x0101,
        (
            '#0010031948V#004F#5P……哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030031949V#023F约修亚？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlayBGM(88)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020031950V#010F父亲的信不是\n',
            '已经写得很清楚了吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031951V『也可以为了得到\n',
            '正游击士的资格环游王国旅行』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031952V#505F#5P嗯、嗯……\n',
            '的确是这样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031953V#010F我们已经得到了\n',
            '洛连特和柏斯的推荐信了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031954V剩下的有卢安、蔡斯和王都格兰赛尔\n',
            '这三个地方。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031955V一边做协会的工作，\n',
            '一边在这些地方旅行的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031956V说不定……\n',
            '能找到父亲的行踪呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031957V#501F#5P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031958V#015F想到父亲的实力，\n',
            '就觉得担心都是多余的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031959V而且他有可能\n',
            '去了外国执行任务……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031960V#010F与其在这里等待，\n',
            '我觉得还不如做点实际的事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031961V而且……\n',
            '我们也许还能找到那个叫Ｒ博士的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031962V#003F#5P……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031963V……喂……约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031964V#010F什么?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0101, 65535)
    SetChrPos(0x0101, 26826, 0, -3385, 180)
    SetChrSubChip(0x0101, 0)
    ChrJumpTo(0x0101, 26710, 0, -4150, 700, 4000)
    SetChrSubChip(0x0101, 2)
    OP_7C(0, 200, 3000, 100)
    PlaySE(125, 0x00, 0x64)

    ChrTalk(
        0x0101,
        (
            '#0010031965V#001F#5P#5S约修亚真是个天才！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0102,
        (
            '#0020031966V#014F艾、艾丝蒂尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031967V#006F#5P这真是一石二鸟的想法，\n',
            '不不，简直是十鸟呢～！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031968V啊～我已经不烦恼了，\n',
            '而且头脑也清醒多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031969V#010F那么……\n',
            '你是赞成的了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031970V#001F#5P赞成，赞成，非常赞成！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031971V#001F一边做游击士的修行，\n',
            '一边环游利贝尔王国……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031972V顺便还要调查一下\n',
            '那个不良中年到底在干什么！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031973V#018F那个……\n',
            '好像有点偏离目标了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030031974V#021F呵呵……\n',
            '好像完全恢复精神了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040031975V#031F#6P呵呵，总算解决了一件事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1500, 0, -1)
    OP_0D()
    SetMapFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T1102._SN', 100, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

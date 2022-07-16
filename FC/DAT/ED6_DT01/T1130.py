import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T1130_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1130   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '豪尔斯教区长'),
    TXT(0x02, '修女萝萨'),
    TXT(0x03, '西加罗'),
    TXT(0x04, '艾德尔'),
    TXT(0x05, '莉拉'),
    TXT(0x06, '萨拉'),
    TXT(0x07, '目标用摄像机'),
    TXT(0x08, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1130.x'
    header.mapIndex       = 1
    header.bgm            = 11
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/T0130._SN', 'ED6_DT01/T1130_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x15A8
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
        ('ED6_DT07/CH01400._CH', 'ED6_DT07/CH01400P._CP'),
        ('ED6_DT07/CH01410._CH', 'ED6_DT07/CH01410P._CP'),
        ('ED6_DT07/CH01043._CH', 'ED6_DT07/CH01043P._CP'),
        ('ED6_DT07/CH01213._CH', 'ED6_DT07/CH01213P._CP'),
        ('ED6_DT07/CH01350._CH', 'ED6_DT07/CH01350P._CP'),
        ('ED6_DT07/CH02370._CH', 'ED6_DT07/CH02370P._CP'),
    ]

# id: 0x10002 offset: 0xDA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 59100,
            z                   = 1000,
            y                   = 52100,
            direction           = 180,
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
            x                   = 15690,
            z                   = 4000,
            y                   = 43180,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = 63600,
            z                   = 90,
            y                   = 46000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x01D4,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 62600,
            z                   = 90,
            y                   = 46000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x01D4,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = 58950,
            z                   = 0,
            y                   = 48260,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = 58920,
            z                   = 0,
            y                   = 48170,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
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

# id: 0x10003 offset: 0x1BA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x1BA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x1BA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 58950,
            triggerZ            = 1000,
            triggerY            = 50250,
            triggerRange        = 400,
            actorX              = 59100,
            actorZ              = 2500,
            actorY              = 52100,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1DE
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_1E8',
    )

    Jump('loc_235')

    def _loc_1E8(): pass

    label('loc_1E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_1F7',
    )

    ClearChrFlags(0x000C, 0x0080)

    Jump('loc_235')

    def _loc_1F7(): pass

    label('loc_1F7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_206',
    )

    ClearChrFlags(0x000D, 0x0080)

    Jump('loc_235')

    def _loc_206(): pass

    label('loc_206')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_210',
    )

    Jump('loc_235')

    def _loc_210(): pass

    label('loc_210')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_21A',
    )

    Jump('loc_235')

    def _loc_21A(): pass

    label('loc_21A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_224',
    )

    Jump('loc_235')

    def _loc_224(): pass

    label('loc_224')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_235',
    )

    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)

    def _loc_235(): pass

    label('loc_235')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 1, 0x309)),
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 2, 0x30A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_246',
    )

    ClearChrFlags(0x000C, 0x0080)

    def _loc_246(): pass

    label('loc_246')

    Return()

# id: 0x0001 offset: 0x247
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0x248
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_25D',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_25D(): pass

    label('loc_25D')

    Return()

# id: 0x0003 offset: 0x25E
@scena.Code('func_03_25E')
def func_03_25E():
    If(
        (
            (Expr.Eval, "OP_29(0x000D, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x000D, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_277',
    )

    Call(1, 0x0000)

    Jump('loc_27B')

    def _loc_277(): pass

    label('loc_277')

    Call(0, 0x0004)

    def _loc_27B(): pass

    label('loc_27B')

    Return()

# id: 0x0004 offset: 0x27C
@scena.Code('func_04_27C')
def func_04_27C():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_2F9',
    )

    ChrTalk(
        0x0008,
        (
            '你们从洛连特一路赶来，\n',
            '真是辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '空之女神爱德丝啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '请赐予他们护佑……\n',
            '并且给予他们指引……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_950')

    def _loc_2F9(): pass

    label('loc_2F9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_3E7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3A4',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '虽然发生了很多事情，\n',
            '不过现在城市似乎已经\n',
            '恢复了往常的平静。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '呵呵，\n',
            '就算发生了意外也不会失去活力，\n',
            '这就是柏斯市民的优点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '呵·呵·呵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E4')

    def _loc_3A4(): pass

    label('loc_3A4')

    ChrTalk(
        0x0008,
        (
            '就算发生了什么意外\n',
            '也不会失去活力，\n',
            '这就是柏斯市民的优点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3E4(): pass

    label('loc_3E4')

    Jump('loc_950')

    def _loc_3E7(): pass

    label('loc_3E7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_4F2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_49B',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '不知为何，\n',
            '最近总是接连发生许多案件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '为了这里的市民，\n',
            '我们来对天祈祷吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '空之女神爱德丝啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '请保佑这里的每个人……\n',
            '并且给予他们指引……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4EF')

    def _loc_49B(): pass

    label('loc_49B')

    ChrTalk(
        0x0008,
        (
            '不知为何，\n',
            '最近总是接连发生许多案件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '为了这里的市民，\n',
            '我们来对天祈祷吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4EF(): pass

    label('loc_4EF')

    Jump('loc_950')

    def _loc_4F2(): pass

    label('loc_4F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_530',
    )

    ChrTalk(
        0x0008,
        (
            '不知为何外面这么吵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '发生什么事情了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_950')

    def _loc_530(): pass

    label('loc_530')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_67A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5EA',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '出城往西走，有一个叫拉文努的小村。\n',
            '那里是王国富有盛名的果树栽培园地。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '那个小村没有教会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '其实，\n',
            '我很想让那里的孩子们\n',
            '也到这个教会的主日学校来上课啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_677')

    def _loc_5EA(): pass

    label('loc_5EA')

    ChrTalk(
        0x0008,
        (
            '出城往西走，有一个叫拉文努的小村。\n',
            '那里是王国富有盛名的果树栽培园地。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '其实，\n',
            '我很想让那里的孩子们\n',
            '也到这个教会的主日学校来上课啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_677(): pass

    label('loc_677')

    Jump('loc_950')

    def _loc_67A(): pass

    label('loc_67A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_793',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_752',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '修女萝萨\n',
            '非常认真而且优秀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '呵呵，\n',
            '如果她能少付出一点多余的关心就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '柏斯的人民\n',
            '非常崇尚自由的风气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '虽然教义和戒律也很重要，\n',
            '但是教会也要根据\n',
            '当地的实际情况而进行活动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_790')

    def _loc_752(): pass

    label('loc_752')

    ChrTalk(
        0x0008,
        (
            '呵呵，每个人的身高不同，\n',
            '思考的角度也不同，\n',
            '不能强求……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_790(): pass

    label('loc_790')

    Jump('loc_950')

    def _loc_793(): pass

    label('loc_793')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_826',
    )

    ChrTalk(
        0x0008,
        (
            '现在的市长梅贝尔小姐\n',
            '是前任市长的女儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '虽然她还年轻，\n',
            '有时候做事有点欠考虑……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不过也能看到她有很多\n',
            '不逊色于父亲的优点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_950')

    def _loc_826(): pass

    label('loc_826')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_950',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8DE',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '柏斯的大部分街道\n',
            '在１０年前的战争中一度成为瓦砾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '战后，商人们都把自己的财产\n',
            '捐出来作为复兴城市的资金。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '原本各自为政的商人们\n',
            '也因为这样而团结起来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_950')

    def _loc_8DE(): pass

    label('loc_8DE')

    ChrTalk(
        0x0008,
        (
            '柏斯的大部分街道\n',
            '在１０年前的战争中一度成为瓦砾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '战后，商人们都把自己的财产\n',
            '捐出来作为复兴城市的资金。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_950(): pass

    label('loc_950')

    TalkEnd(0x0008)

    Return()

# id: 0x0005 offset: 0x954
@scena.Code('func_05_954')
def func_05_954():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_A56',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A20',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '扫除做完了，\n',
            '衣物也都洗完了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '讲话稿也写好了，\n',
            '弥撒也准备好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对了对了，\n',
            '主日学校下一次的课程该怎么办呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不把以后要做的事情决定下来，\n',
            '我是不会放心的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A53')

    def _loc_A20(): pass

    label('loc_A20')

    ChrTalk(
        0x00FE,
        (
            '不把以后要做的事情决定下来，\n',
            '我是不会放心的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A53(): pass

    label('loc_A53')

    Jump('loc_E62')

    def _loc_A56(): pass

    label('loc_A56')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_B4C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B00',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '没想到竟然连普通的民居\n',
            '也受到了强盗的洗劫……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '………………………………\n',
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……等会儿我要去\n',
            '探访一下受害的居民。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B49')

    def _loc_B00(): pass

    label('loc_B00')

    ChrTalk(
        0x00FE,
        (
            '商业街也受到了强盗的洗劫……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '等会儿我要去\n',
            '探访一下受害的居民。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B49(): pass

    label('loc_B49')

    Jump('loc_E62')

    def _loc_B4C(): pass

    label('loc_B4C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_BAE',
    )

    ChrTalk(
        0x00FE,
        (
            '现在正在做礼拜，\n',
            '外面还真是吵得很啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个城市也真是的，\n',
            '总是那么吵吵嚷嚷的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E62')

    def _loc_BAE(): pass

    label('loc_BAE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_CAD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C4E',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '经常来教会做礼拜的人\n',
            '都是来祈求生意兴隆的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '爱德丝是创造女神，\n',
            '而不是发财女神！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的……\n',
            '是不是该在入口处贴一张告示呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CAA')

    def _loc_C4E(): pass

    label('loc_C4E')

    ChrTalk(
        0x00FE,
        (
            '经常来教会做礼拜的人\n',
            '都是来祈求生意兴隆的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '爱德丝是创造女神，\n',
            '而不是发财女神！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CAA(): pass

    label('loc_CAA')

    Jump('loc_E62')

    def _loc_CAD(): pass

    label('loc_CAD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_D17',
    )

    ChrTalk(
        0x00FE,
        (
            '教区长非常通情达理，\n',
            '也获得了很多人的支持……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过有时候有点自作主张\n',
            '也算是个缺点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E62')

    def _loc_D17(): pass

    label('loc_D17')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_E16',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DB3',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '市长把礼拜交给女佣来做\n',
            '真是前所未闻的事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '教区长也不怎么介意，\n',
            '真是可叹啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '作为市长，\n',
            '应该为大家树立榜样才对啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E13')

    def _loc_DB3(): pass

    label('loc_DB3')

    ChrTalk(
        0x00FE,
        (
            '市长把礼拜交给女佣来做\n',
            '真是前所未闻的事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '作为市长，\n',
            '应该为大家树立榜样才对啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E13(): pass

    label('loc_E13')

    Jump('loc_E62')

    def _loc_E16(): pass

    label('loc_E16')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_E62',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，欢迎来到七耀教会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要做礼拜吗？\n',
            '这么年轻值得表扬啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E62(): pass

    label('loc_E62')

    TalkEnd(0x0009)

    Return()

# id: 0x0006 offset: 0xE66
@scena.Code('func_06_E66')
def func_06_E66():
    TalkBegin(0x000A)

    ChrTalk(
        0x00FE,
        (
            '我一到达柏斯，\n',
            '定期船就开始停航了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我还在巡礼的途中啊，\n',
            '这下伤脑筋了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000A)

    Return()

# id: 0x0007 offset: 0xEC1
@scena.Code('func_07_EC1')
def func_07_EC1():
    TalkBegin(0x000B)

    ChrTalk(
        0x00FE,
        (
            '嘿嘿嘿，终于来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这一天终于到来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '等礼拜结束之后，\n',
            '就向柏斯超市进发！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000B)

    Return()

# id: 0x0008 offset: 0xF25
@scena.Code('func_08_F25')
def func_08_F25():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F7A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '为什么士兵\n',
            '都是那么傲慢呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还是游击士比较友善，\n',
            '我喜欢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FA5')

    def _loc_F7A(): pass

    label('loc_F7A')

    ChrTalk(
        0x00FE,
        (
            '今天我会连大小姐的那份\n',
            '也一起祈祷呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FA5(): pass

    label('loc_FA5')

    TalkEnd(0x000D)

    Return()

# id: 0x0009 offset: 0xFA9
@scena.Code('func_09_FA9')
def func_09_FA9():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_1038',
    )

    ChrTalk(
        0x00FE,
        (
            '#0370020527V#620F小姐连续好几天\n',
            '彻夜不眠地加班加点，\n',
            '来想办法如何处理强盗事件。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370020528V如果我无法好好照顾\n',
            '小姐的身体状况的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1590')

    def _loc_1038(): pass

    label('loc_1038')

    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x0061, 2, 0x30A))
    Fade(1000)
    SetChrPos(0x0101, 58910, 0, 46930, 0)
    SetChrPos(0x0102, 58250, 0, 46000, 0)
    SetChrPos(0x0103, 59540, 0, 46030, 0)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    OP_69(0x000C, 1000)

    ChrTalk(
        0x0101,
        (
            '#0010020503V#001F是女佣小姐，找到了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000C, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000C,
        (
            '#0370020504V#620F诸位是……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020505V#017F艾丝蒂尔，这么冒失太失礼了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020020506V#010F非常抱歉，我们是游击士协会的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020020507V为了确认委托的内容，\n',
            '特地前来拜访你们的市长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0370020508V#621F啊，是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370020509V请允许我先自我介绍一下。\n',
            '我是女佣莉拉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370020510V打理市长的日常生活\n',
            '是我的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020511V#000F打理日常生活……\n',
            '真是活在不同的世界啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020512V那么市长在哪里呢？\n',
            '不是说来这里做礼拜吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0370020513V#623F……逃掉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020514V#008F哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0370020515V#620F我想现在大概\n',
            '正在超市里面视察吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370020516V刚才市长吩咐我，\n',
            '让我代替做礼拜，\n',
            '然后自己就出去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0103, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020020517V#019F该怎么说呢……\n',
            '真是一位独特的人物啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020518V#027F呵呵，市长还真有趣。\n',
            '暂且不说是不是专注于职务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0370020519V#620F市长确实是位十分有能力的人。\n',
            '只是有时候的行动让人无法捉摸。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370020520V……我差不多\n',
            '该去接市长回官邸了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370020521V十分抱歉，能不能先请\n',
            '诸位到市长官邸稍稍等候一下？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370020522V我陪同市长随后就到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020523V#000F嗯～都到这里来了，\n',
            '要是空着手回去也不太好嘛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020524V可以的话，我们和你一起去好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0370020525V#622F一起去迎接市长吗？\n',
            '我倒是没什么意见……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370020526V#621F那么我们立刻前往\n',
            '坐落在市中央的柏斯超市吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0035, 0x01, 0x0010)
    SetChrFlags(0x000C, 0x0040)
    OP_92(0x000C, 0x0000, 0, 3000, 0x00)
    SetChrFlags(0x000C, 0x0080)
    EventEnd(0x00)
    FormationAddMember(0x33, 0xFF)
    SetMapFlags(0x00000001)

    def _loc_1590(): pass

    label('loc_1590')

    TalkEnd(0x000C)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

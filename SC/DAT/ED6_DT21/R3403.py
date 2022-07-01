import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import R3403_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R3403   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '鲁迪'),
    TXT(0x02, '王'),
    TXT(0x03, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'R3403.x'
    header.mapIndex       = 1
    header.bgm            = 30
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x18F3
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
        ('ED6_DT07/CH01500._CH', 'ED6_DT07/CH01500P._CP'),
        ('ED6_DT07/CH01760._CH', 'ED6_DT07/CH01760P._CP'),
    ]

# id: 0x10002 offset: 0xBA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 613590,
            z                   = 20,
            y                   = -52010,
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
            x                   = 604750,
            z                   = 0,
            y                   = -52330,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
    )

# id: 0x10003 offset: 0xFA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0xFA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0xFA
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xFA
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_109',
    )

    SetChrFlags(0x0008, 0x0080)

    Jump('loc_140')

    def _loc_109(): pass

    label('loc_109')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_118',
    )

    SetChrFlags(0x0008, 0x0080)

    Jump('loc_140')

    def _loc_118(): pass

    label('loc_118')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_133',
    )

    SetChrPos(0x0008, 609020, -20, -62710, 135)

    Jump('loc_140')

    def _loc_133(): pass

    label('loc_133')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0290, 0, 0x1480)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_140',
    )

    SetChrFlags(0x0008, 0x0010)

    def _loc_140(): pass

    label('loc_140')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_178',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 2, 0x2082)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_178',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 1, 0x2081)),
            Expr.Return,
        ),
        'loc_161',
    )

    OP_A2(0x2082)

    Jump('loc_178')

    def _loc_161(): pass

    label('loc_161')

    If(
        (
            (Expr.Eval, "OP_40(0x0150, 0x02)"),
            Expr.Return,
        ),
        'loc_171',
    )

    Event(0, 0x0005)

    Jump('loc_175')

    def _loc_171(): pass

    label('loc_171')

    Event(0, 0x0004)

    def _loc_175(): pass

    label('loc_175')

    OP_A2(0x2082)

    def _loc_178(): pass

    label('loc_178')

    Return()

# id: 0x0001 offset: 0x179
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1BD',
    )

    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    OP_71(0x0005, 0x0004)
    OP_71(0x0006, 0x0004)
    OP_79(0xFF, 0x0002)
    OP_7A(0x08, 0x0002)
    OP_C4(0x00, 0x00000001)
    OP_78(0x00, 0x00, 0x00)

    Jump('loc_1BD')

    def _loc_1BD(): pass

    label('loc_1BD')

    OP_16(0x02, 0x00000FA0, 0x00076E58, 0xFFFD40E0, 0x0023003A)

    Return()

# id: 0x0002 offset: 0x1D0
@scena.Code('ReInit')
def ReInit():
    TalkBegin(0x0008)

    If(
        (
            (Expr.Eval, "OP_29(0x0031, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0031, 0x01, 0x0020)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1E8',
    )

    OP_A2(0x0001)

    def _loc_1E8(): pass

    label('loc_1E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_26E',
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
            TXT(0x00, '【◇【爱的使者】高评价完成】\n'),
            TXT(0x01, '【◇【爱的使者】没有高评价完成】\n'),
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
        (0x00000000, 'loc_262'),
        (0x00000001, 'loc_268'),
        (-1, 'loc_26E'),
    )

    def _loc_262(): pass

    label('loc_262')

    OP_A2(0x0001)

    Jump('loc_26E')

    def _loc_268(): pass

    label('loc_268')

    OP_A3(0x0001)

    Jump('loc_26E')

    def _loc_26E(): pass

    label('loc_26E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_469',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_356',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_2E8',
    )

    ChrTalk(
        0x00FE,
        (
            '菲前辈乘坐工房的飞船\n',
            '出发前往雷斯顿要塞了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听说是为了在那里更换\n',
            '『埃尔赛尤』的引擎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_353')

    def _loc_2E8(): pass

    label('loc_2E8')

    ChrTalk(
        0x00FE,
        (
            '那么～前辈不在的时候，\n',
            '我就先一个人努力工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在新的邂逅来临之前，\n',
            '每天的工作就是我的恋人！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_353(): pass

    label('loc_353')

    Jump('loc_466')

    def _loc_356(): pass

    label('loc_356')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_3FB',
    )

    ChrTalk(
        0x00FE,
        (
            '为了装配『埃尔赛尤』的引擎，\n',
            '似乎要到要塞那边更换。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈，我正准备向前辈提出\n',
            '正式交往的请求呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可恶的『埃尔赛尤』……\n',
            '竟敢把我和前辈拆散～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_466')

    def _loc_3FB(): pass

    label('loc_3FB')

    ChrTalk(
        0x00FE,
        (
            '菲前辈乘坐工房的飞船\n',
            '出发前往雷斯顿要塞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我、我今天原本打算向前辈\n',
            '提出正式交往的请求呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_466(): pass

    label('loc_466')

    Jump('loc_1297')

    def _loc_469(): pass

    label('loc_469')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_673',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_597',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_510',
    )

    ChrTalk(
        0x00FE,
        (
            '唉，但是我\n',
            '绝对不能够消沉下去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之要专注在工作上，\n',
            '努力忘掉前辈的事才行！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……不过，尽管话是这么说…\n',
            '想彻底忘记又谈何容易啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_594')

    def _loc_510(): pass

    label('loc_510')

    ChrTalk(
        0x00FE,
        (
            '唉～前辈最近……\n',
            '好像很幸福的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看样子果然是和\n',
            '以前的男友重修旧好了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呜呜……\n',
            '这就是所谓的『破镜重圆』吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_594(): pass

    label('loc_594')

    Jump('loc_670')

    def _loc_597(): pass

    label('loc_597')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_609',
    )

    ChrTalk(
        0x00FE,
        (
            '不行！今天一定要向前辈\n',
            '坦白我的心意才行！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼、呼啊～光是想象一下，\n',
            '心脏就噗通噗通地跳个不停。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_670')

    def _loc_609(): pass

    label('loc_609')

    ChrTalk(
        0x00FE,
        (
            '决、决定了！今天我就要向\n',
            '菲前辈做出正式的表白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '毕竟我也是个男人，\n',
            '不能老是这么优柔寡断。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_670(): pass

    label('loc_670')

    Jump('loc_1297')

    def _loc_673(): pass

    label('loc_673')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 3, 0x141B)),
            Expr.Return,
        ),
        'loc_7C4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_6F0',
    )

    ChrTalk(
        0x00FE,
        (
            '前辈虽然平时看起来很可爱，\n',
            '工作起来却不输给男人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯～太棒了。\n',
            '这种美妙的错差感真令人受不了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7C1')

    def _loc_6F0(): pass

    label('loc_6F0')

    ChrTalk(
        0x00FE,
        (
            '刚才经过这里的那两个人\n',
            '是你们的游击士同伴吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那、那个绑发带的女孩\n',
            '实在是太可爱了啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，穿着那么可爱的服装…\n',
            '真的可以去和魔兽战斗吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯～太棒了。\n',
            '这种美妙的错差感真令人受不了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_7C1(): pass

    label('loc_7C1')

    Jump('loc_1297')

    def _loc_7C4(): pass

    label('loc_7C4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_9C4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_8EA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_86E',
    )

    ChrTalk(
        0x00FE,
        (
            '难道说菲前辈……\n',
            '和以前的恋人重归于好了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呜啊啊啊～我真是个笨蛋。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '早知如此的话，在事态发展到这种地步之前\n',
            '就应该展开攻势才对啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8E7')

    def _loc_86E(): pass

    label('loc_86E')

    ChrTalk(
        0x00FE,
        (
            '为、为什么在诞辰庆典之后，\n',
            '菲前辈的脸上就一直洋溢着幸福的微笑！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难、难道说她和前男友\n',
            '已经重修旧好了吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_8E7(): pass

    label('loc_8E7')

    Jump('loc_9C1')

    def _loc_8EA(): pass

    label('loc_8EA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_944',
    )

    ChrTalk(
        0x00FE,
        (
            '可是，菲前辈和我\n',
            '毕竟还没有正式交往。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '原、原本打算\n',
            '在最近向她表白的…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9C1')

    def _loc_944(): pass

    label('loc_944')

    ChrTalk(
        0x00FE,
        (
            '呵呵～和菲前辈一起参加的\n',
            '诞辰庆典实在是太完美了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们两个人静静地\n',
            '眺望着『埃尔赛尤』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是太浪漫了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_9C1(): pass

    label('loc_9C1')

    Jump('loc_1297')

    def _loc_9C4(): pass

    label('loc_9C4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_1297',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0290, 0, 0x1480)),
            Expr.Return,
        ),
        'loc_A8F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A3F',
    )

    ChrTalk(
        0x00FE,
        (
            '不管是地震也好，\n',
            '那个黑衣服的怪家伙也罢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总有种不祥的预感啊。\n',
            '但愿别发生什么事才好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A8C')

    def _loc_A3F(): pass

    label('loc_A3F')

    ChrTalk(
        0x00FE,
        (
            '虽然我不是很清楚，\n',
            '但能帮上你们就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，我也要继续工作了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A8C(): pass

    label('loc_A8C')

    Jump('loc_1297')

    def _loc_A8F(): pass

    label('loc_A8F')

    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0101, 614200, 20, -53200, 0)
    SetChrPos(0x00F7, 613000, 0, -53200, 0)
    SetChrPos(0x0105, 614200, 0, -54440, 0)
    SetChrPos(0x0104, 613000, 0, -54440, 0)
    OP_6B(2715, 0)
    OP_6D(613510, 10, -52620, 0)
    OP_0D()
    Sleep(600)

    ChrTalk(
        0x00FE,
        (
            '#2090220786V呼，真是的……\n',
            '希望地震不要再来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2090220787V嗯，还有之前遇到的\n',
            '那个怪家伙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2090220788V……总让人有种不祥的预感啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220789V#1002F怪家伙……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220790V……有那样的人出现吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    OP_8C(0x00FE, 180, 400)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '#2090220791V啊，啊啊……\n',
            '我昨天看见了一个奇怪的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2090220792V是我从来没见过的生面孔，\n',
            '一言不发地就站在这个地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2090220793V因为这里平时不太有人走动，\n',
            '所以让人感觉有点毛骨悚然。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_D2D',
    )

    ChrTalk(
        0x0106,
        (
            '#0050220794V#052F确实值得注意啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220795V#050F能不能把那个人的\n',
            '外貌特征详细地告诉我们？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D91')

    def _loc_D2D(): pass

    label('loc_D2D')

    ChrTalk(
        0x0103,
        (
            '#0030220796V#022F确实很值得注意啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220797V能不能把那个怪人的\n',
            '外貌特征详细地告诉我们？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D91(): pass

    label('loc_D91')

    ChrTurnDirection(0x00FE, 0x00F7, 400)

    ChrTalk(
        0x00FE,
        (
            '#2090220798V啊，那当然没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2090220799V总之是一名个子很高的家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2090220800V除了身穿黑色大衣之外，\n',
            '还戴着同样颜色的黑手套……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2090220801V其中最引人注目的\n',
            '就是他脸上那一副墨镜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220802V#1011F墨镜……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220803V#1015F…………那是什么东西啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#2090220804V那是一种可以遮挡阳光的特殊眼镜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2090220805V你看到的话马上就会明白了。\n',
            '因为整个镜片都是漆黑的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220806V#1004F那、那样的话\n',
            '岂不是看不见前边了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2090220807V哈哈，不会的。\n',
            '还是可以看见前方的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2090220808V只不过，这附近似乎\n',
            '从没见过有人戴着那种东西呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1037',
    )

    ChrTalk(
        0x0106,
        (
            '#0050220809V#050F嗯嗯，是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220810V这可是相当有价值\n',
            '的情报啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1086')

    def _loc_1037(): pass

    label('loc_1037')

    ChrTalk(
        0x0103,
        (
            '#0030220811V#026F嗯，是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220812V#022F这可是相当有用\n',
            '的情报啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1086(): pass

    label('loc_1086')

    ChrTalk(
        0x0101,
        (
            '#0010220813V#1019F黑大衣、黑手套，\n',
            '连眼镜也是黑色的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220814V#1007F不管怎么想也是个\n',
            '可疑的怪家伙啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220815V这件事情最好也向\n',
            '雾香小姐报告一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_118B',
    )

    ChrTalk(
        0x0106,
        (
            '#0050220816V#050F嗯，说的对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220817V等堡垒的调查结束之后\n',
            '再一起去报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11DF')

    def _loc_118B(): pass

    label('loc_118B')

    ChrTalk(
        0x0103,
        (
            '#0030220818V#020F嗯，没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220819V等堡垒的调查结束之后\n',
            '再一起去报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11DF(): pass

    label('loc_11DF')

    OP_8C(0x00FE, 180, 400)

    ChrTalk(
        0x00FE,
        (
            '#2090220820V虽然不知道发生了什么事，\n',
            '不过好像对你们有些用处？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220821V#1006F嗯，当然。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220822V真是谢谢了。\n',
            '这些情报对我们非常有用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1480)
    OP_A2(0x0000)
    OP_28(0x0085, 0x01, 0x0008)
    OP_28(0x0085, 0x01, 0x0010)
    ClearChrFlags(0x0008, 0x0010)
    EventEnd(0x00)

    def _loc_1297(): pass

    label('loc_1297')

    TalkEnd(0x0008)

    Return()

# id: 0x0003 offset: 0x129B
@scena.Code('func_03_129B')
def func_03_129B():
    Return()

# id: 0x0004 offset: 0x129C
@scena.Code('func_04_129C')
def func_04_129C():
    EventBegin(0x00)
    OP_6D(619280, 500, -53640, 0)
    OP_67(0, 8500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 622820, 1000, -55100, 270)
    SetChrPos(0x0102, 623820, 1000, -55100, 270)
    SetChrPos(0x00F8, 624820, 1000, -55100, 270)
    SetChrPos(0x00F9, 625820, 1000, -55100, 270)
    FadeIn(1500, 0)
    CreateThread(0x0101, 0x01, 0x00, 0x0006)
    Sleep(200)

    CreateThread(0x0102, 0x01, 0x00, 0x0007)
    Sleep(100)

    CreateThread(0x00F8, 0x01, 0x00, 0x0008)
    Sleep(200)

    CreateThread(0x00F9, 0x01, 0x00, 0x0009)
    WaitForThreadExit(0x00F8, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010370001V#1020F这、这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x00F9, 0x0001)

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_13C6',
    )

    ChrTalk(
        0x0108,
        (
            '#0080370002V#072F不行啊……\n',
            '眼前完全一片漆黑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_144C')

    def _loc_13C6(): pass

    label('loc_13C6')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_140B',
    )

    ChrTalk(
        0x0106,
        (
            '#0050370003V#055F喂喂……\n',
            '根本什么都看不见啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_144C')

    def _loc_140B(): pass

    label('loc_140B')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_144C',
    )

    ChrTalk(
        0x0103,
        (
            '#0030370004V#022F没办法了……完全漆黑一团呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_144C(): pass

    label('loc_144C')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_149F',
    )

    ChrTalk(
        0x0107,
        (
            '#0070370005V#065F没、没有了导力灯，\n',
            '这里竟然会变得这么暗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_153E')

    def _loc_149F(): pass

    label('loc_149F')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_14F2',
    )

    ChrTalk(
        0x0103,
        (
            '#0030370006V#025F……没有了导力灯，\n',
            '这里居然会变得这么暗啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_153E')

    def _loc_14F2(): pass

    label('loc_14F2')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_153E',
    )

    ChrTalk(
        0x0106,
        (
            '#0050370007V#057F没有了导力灯，\n',
            '这里竟然会变得这么暗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_153E(): pass

    label('loc_153E')

    ChrTalk(
        0x0102,
        (
            '#0020370008V#1043F#5P如果不戴上『夜视眼镜』的话，\n',
            '想通过这里实在太困难了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020370009V#1042F若是身上没有的话，\n',
            '就回城镇上的道具店找找看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370010V#1007F嗯，明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010370011V#1002F看来，在通过这里时\n',
            '最好要事先准备齐全呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x0005 offset: 0x1637
@scena.Code('func_05_1637')
def func_05_1637():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_6D(619280, 500, -53640, 0)
    OP_67(0, 8500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 622820, 1000, -55100, 270)
    SetChrPos(0x0102, 623820, 1000, -55100, 270)
    SetChrPos(0x00F8, 624820, 1000, -55100, 270)
    SetChrPos(0x00F9, 625820, 1000, -55100, 270)
    CreateThread(0x0101, 0x01, 0x00, 0x0006)
    Sleep(200)

    CreateThread(0x0102, 0x01, 0x00, 0x0007)
    Sleep(100)

    CreateThread(0x00F8, 0x01, 0x00, 0x0008)
    Sleep(200)

    CreateThread(0x00F9, 0x01, 0x00, 0x0009)
    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x00F9, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010370012V#1019F还好有夜视眼镜，\n',
            '总算可以看见路了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010370013V但如果把它摘下来的话\n',
            '就会又什么都看不见了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370014V#1035F#5P嗯，完全一片漆黑啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020370015V#1042F如果不想迷路的话，\n',
            '在通过这个地方时\n',
            '就一定要戴着夜视眼镜啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370016V#1002F嗯，了解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x0006 offset: 0x181F
@scena.Code('func_06_181F')
def func_06_181F():
    OP_8E(0x00FE, 622250, 1000, -55050, 2000, 0x00)
    OP_8E(0x00FE, 620140, 1000, -55560, 2000, 0x00)
    OP_8C(0x00FE, 270, 400)

    Return()

# id: 0x0007 offset: 0x184F
@scena.Code('func_07_184F')
def func_07_184F():
    OP_8E(0x00FE, 622250, 1000, -55050, 2000, 0x00)
    OP_8E(0x00FE, 620160, 1000, -54720, 2000, 0x00)
    OP_8C(0x00FE, 270, 400)

    Return()

# id: 0x0008 offset: 0x187F
@scena.Code('func_08_187F')
def func_08_187F():
    OP_8E(0x00FE, 621690, 1000, -55220, 2000, 0x00)
    OP_8E(0x00FE, 621030, 1000, -55700, 2000, 0x00)
    OP_8C(0x00FE, 270, 400)

    Return()

# id: 0x0009 offset: 0x18AF
@scena.Code('func_09_18AF')
def func_09_18AF():
    OP_8E(0x00FE, 622250, 1000, -55050, 2000, 0x00)
    OP_8E(0x00FE, 620990, 1000, -54860, 2000, 0x00)
    OP_8C(0x00FE, 270, 400)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

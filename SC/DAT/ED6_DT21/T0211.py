import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0211_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0211   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '米蕾奴夫人'),
    TXT(0x02, '玲达'),
    TXT(0x03, '克劳斯市长'),
    TXT(0x04, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0211.x'
    header.mapIndex       = 12
    header.bgm            = 84
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1956
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
        ('ED6_DT07/CH01180._CH', 'ED6_DT07/CH01180P._CP'),
        ('ED6_DT26/CH20330._CH', 'ED6_DT26/CH20330P._CP'),
        ('ED6_DT07/CH02350._CH', 'ED6_DT07/CH02350P._CP'),
    ]

# id: 0x10002 offset: 0xC2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 200400,
            z                   = 0,
            y                   = 48360,
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
            x                   = 201800,
            z                   = 0,
            y                   = 48800,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 77760,
            z                   = 0,
            y                   = 3410,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
    )

# id: 0x10003 offset: 0x122
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x122
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x122
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x122
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            Expr.Return,
        ),
        'loc_159',
    )

    ClearChrFlags(0x0009, 0x0002)
    SetChrSubChip(0x0009, 0)
    SetChrPos(0x0009, 201800, 0, 49000, 270)
    SetChrPos(0x0008, 200400, 0, 48360, 90)
    OP_4A(0x0009, 255)

    def _loc_159(): pass

    label('loc_159')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_170',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x51),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10F0)
    Event(0, 0x0005)

    def _loc_170(): pass

    label('loc_170')

    Return()

# id: 0x0001 offset: 0x171
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            Expr.Return,
        ),
        'loc_17F',
    )

    OP_6F(0x0005, 10)

    def _loc_17F(): pass

    label('loc_17F')

    Return()

# id: 0x0002 offset: 0x180
@scena.Code('ReInit')
def ReInit():
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
        'loc_1A5',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_2E7')

    def _loc_1A5(): pass

    label('loc_1A5')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1BE',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000640)

    Jump('loc_2E7')

    def _loc_1BE(): pass

    label('loc_1BE')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1D7',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x0000060E)

    Jump('loc_2E7')

    def _loc_1D7(): pass

    label('loc_1D7')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1F0',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005DC)

    Jump('loc_2E7')

    def _loc_1F0(): pass

    label('loc_1F0')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_209',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AA)

    Jump('loc_2E7')

    def _loc_209(): pass

    label('loc_209')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_222',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x00000578)

    Jump('loc_2E7')

    def _loc_222(): pass

    label('loc_222')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_23B',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x00000546)

    Jump('loc_2E7')

    def _loc_23B(): pass

    label('loc_23B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_254',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000677)

    Jump('loc_2E7')

    def _loc_254(): pass

    label('loc_254')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_26D',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000645)

    Jump('loc_2E7')

    def _loc_26D(): pass

    label('loc_26D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_286',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x00000613)

    Jump('loc_2E7')

    def _loc_286(): pass

    label('loc_286')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_29F',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005E1)

    Jump('loc_2E7')

    def _loc_29F(): pass

    label('loc_29F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B8',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AF)

    Jump('loc_2E7')

    def _loc_2B8(): pass

    label('loc_2B8')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2D1',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x0000057D)

    Jump('loc_2E7')

    def _loc_2D1(): pass

    label('loc_2D1')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2E7',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x0000054B)

    def _loc_2E7(): pass

    label('loc_2E7')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2FC',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_2E7')

    def _loc_2FC(): pass

    label('loc_2FC')

    Return()

# id: 0x0003 offset: 0x2FD
@scena.Code('func_03_2FD')
def func_03_2FD():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 3, 0x1813)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_30C',
    )

    Call(0, 0x0006)

    Jump('loc_3AD')

    def _loc_30C(): pass

    label('loc_30C')

    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_367',
    )

    ChrTalk(
        0x00FE,
        (
            '如果有事\n',
            '我会马上联系协会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，这座城市\n',
            '现在到底在发生着什么啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3AA')

    def _loc_367(): pass

    label('loc_367')

    ChrTalk(
        0x00FE,
        (
            '如果有事\n',
            '我会马上联系协会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们也……\n',
            '一定要小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_3AA(): pass

    label('loc_3AA')

    TalkEnd(0x0008)

    def _loc_3AD(): pass

    label('loc_3AD')

    Return()

# id: 0x0004 offset: 0x3AE
@scena.Code('func_04_3AE')
def func_04_3AE():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            Expr.Return,
        ),
        'loc_DF3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0313, 3, 0x189B)),
            Expr.Return,
        ),
        'loc_4F7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_430',
    )

    ChrTalk(
        0x000A,
        (
            '#0340281453V#602F玲达\n',
            '在对面的房间里休息。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340281454V米蕾奴在陪着她，\n',
            '详细情况你们可以去问她。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4F4')

    def _loc_430(): pass

    label('loc_430')

    ChrTalk(
        0x000A,
        (
            '#0340281455V#602F调查的事我已经\n',
            '传达给爱娜了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340281456V艾丝蒂尔你们就\n',
            '专心地调查吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340281457V……玲达\n',
            '在对面的房间里休息。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340281454V米蕾奴在陪着她，\n',
            '详细情况你们可以去问她。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_4F4(): pass

    label('loc_4F4')

    Jump('loc_DF3')

    def _loc_4F7(): pass

    label('loc_4F7')

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    Sleep(400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0310, 1, 0x1881)),
            Expr.Return,
        ),
        'loc_7F5',
    )

    ChrTalk(
        0x000A,
        (
            '#0340281459V#604F哦，是艾丝蒂尔你们啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340281460V#603F真想不到会\n',
            '变成这样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340281461V本来我只是推迟去王都，\n',
            '现在看来只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281462V#1004F啊……！？\n',
            '您、您不去了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030281463V#023F就是说要缺席签字仪式？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0340281464V#603F嗯，虽然对女王陛下感到抱歉，\n',
            '不过现在也只能这么做了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340281465V虽然参加仪式也是\n',
            '市长的工作……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340281466V#602F可是不管有什么样的理由，\n',
            '我现在都不能离开这座城市。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340281467V……就算那是\n',
            '陛下的命令。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281468V#1020F市长爷爷……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x000A,
        (
            '#0340281455V#602F调查的事我已经\n',
            '传达给爱娜了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340281470V艾丝蒂尔你们请\n',
            '马上开始调查。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340281471V即便是为了防止\n',
            '受害者的增加。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281472V#1002F嗯！明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030281473V#022F嗯，我们会尽全力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DF0')

    def _loc_7F5(): pass

    label('loc_7F5')

    ChrTalk(
        0x000A,
        (
            '#0340281459V#604F哦，是艾丝蒂尔你们啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340281460V#603F真想不到会\n',
            '变成这样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340281476V呼，看来我放弃去\n',
            '王都是正确的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280918V#1015F啊？在王都也有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030280919V#023F去王都，难道是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030280920V互不侵犯条约的签字仪式吗？！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010281480V#1004F啊！签字仪式！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0340281481V#602F嗯，你说得没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340281482V虽然对不起女王陛下，\n',
            '不过我还是得缺席了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281483V#1020F缺、缺席……！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281484V真、真的打算\n',
            '不去了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x000A,
        (
            '#0340281485V#603F当然，参加仪式也是\n',
            '市长的工作……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340281486V可是不管有什么样的理由，\n',
            '我现在都不能离开这座城市。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340281487V#602F……就算那是\n',
            '女王陛下的命令。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281488V#1026F市长爷爷……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B2E',
    )

    ChrTalk(
        0x0105,
        (
            '#0060281489V#047F……我觉得这是一个英明的抉择。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060281490V#042F祖母大人\n',
            '也一定会理解您的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B2E(): pass

    label('loc_B2E')

    ChrTalk(
        0x000A,
        (
            '#0340281491V#602F如果接下来再发生什么问题，\n',
            '我打算与协会合作应对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340281492V不好意思，这段时间\n',
            '我要借助各位的力量。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281493V#1002F嗯，当然没问题！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C34',
    )

    ChrTalk(
        0x0106,
        (
            '#0050280932V#050F啊，那是应该的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050280933V再次来到这里也算\n',
            '是缘分吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D35')

    def _loc_C34(): pass

    label('loc_C34')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C9F',
    )

    ChrTalk(
        0x0108,
        (
            '#0080281496V#072F嗯，我们会配合的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080280935V再次来到这里…\n',
            '这一定是女神的召唤。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D35')

    def _loc_C9F(): pass

    label('loc_C9F')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D06',
    )

    ChrTalk(
        0x0104,
        (
            '#0040280936V#030F呼，交给我们好啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040280937V再次来到这里\n',
            '也算是一种缘分啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D35')

    def _loc_D06(): pass

    label('loc_D06')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D35',
    )

    ChrTalk(
        0x0107,
        (
            '#0070240159V#062F是、是的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D35(): pass

    label('loc_D35')

    ChrTalk(
        0x000A,
        (
            '#0340280940V#603F那就先谢谢你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030281502V#022F那如果有什么事的话\n',
            '请随时和协会联络。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030280942V爱娜会马上\n',
            '联络到我们的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0103, 400)

    ChrTalk(
        0x000A,
        (
            '#0340281504V#602F嗯，我们会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1881)

    def _loc_DF0(): pass

    label('loc_DF0')

    OP_A2(0x189B)

    def _loc_DF3(): pass

    label('loc_DF3')

    TalkEnd(0x000A)

    Return()

# id: 0x0005 offset: 0xDF7
@scena.Code('func_05_DF7')
def func_05_DF7():
    EventBegin(0x00)
    OP_DB()
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    OP_6F(0x0005, 10)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x0009, 0x0002)
    SetChrSubChip(0x0009, 0)
    SetChrPos(0x0009, 201800, 0, 49000, 270)
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 200400, 0, 48360, 90)
    OP_4A(0x0009, 255)
    OP_6D(200500, 0, 45550, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    OP_6D(201840, 0, 49170, 3000)
    OP_0D()
    FadeOut(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x0000, 0x0080)
    ClearChrFlags(0x0001, 0x0080)
    ClearChrFlags(0x0002, 0x0080)
    ClearChrFlags(0x0003, 0x0080)
    OP_DC()
    OP_A2(0x10F0)
    NewScene('ED6_DT21/T0135._SN', 106, 0, 0)
    IdleLoop()

    Return()

# id: 0x0006 offset: 0xED4
@scena.Code('func_06_ED4')
def func_06_ED4():
    EventBegin(0x00)
    OP_4A(0x0008, 255)
    Fade(1000)
    SetChrPos(0x0101, 199890, 0, 46520, 0)
    SetChrPos(0x0103, 200990, 0, 46580, 0)
    SetChrPos(0x00F8, 199780, 0, 45200, 0)
    SetChrPos(0x00F9, 200960, 0, 45200, 0)
    OP_6D(200720, 0, 47460, 0)
    OP_67(0, 6690, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(288, 0)
    OP_8C(0x0008, 180, 0)
    OP_0D()
    Sleep(200)

    ChrTalk(
        0x00FE,
        (
            '#1020281505V#5P哎呀，艾丝蒂尔……\n',
            '和雪拉扎德吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281506V#1002F晚上好。\n',
            '米蕾奴阿姨。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281507V市长先生跟您说过了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1020281508V#5P嗯，你们要调查\n',
            '这次的事件吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1020281509V#5P有什么问题\n',
            '尽管问我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030281510V#026F#4P那真是太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281511V#022F那么首先……\n',
            '玲达小姐的情况怎样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1020281512V#5P嗯……\n',
            '一点也没有要醒的迹象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1020281513V#5P如果明天早上能\n',
            '自然地醒过来就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1020281514V#5P现在只能继续观察了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281515V#1007F是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030281516V#022F#4P玲达小姐是于何时昏倒的？\n',
            '当时是什么样的情况？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1020281517V#5P让我想想……\n',
            '大概是傍晚的５点前吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1020281518V#5P我从楼下的厨房出来后，\n',
            '就看到玲达倒在门口。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1020281519V#5P我就赶紧到书房去叫我先生，\n',
            '然后把她扶到了床上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1020281520V#5P不过，真没想到还有其他的人\n',
            '也遇上了同样的事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281521V#1015F倒在门口……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281522V那时大门锁着吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1020281523V#5P我记得……\n',
            '应该是没有锁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1020281524V#5P因为有很多人来跟我先生\n',
            '商量大雾的对策。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281525V#1007F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281526V#1002F阿姨您准备饭菜大概\n',
            '用了多久？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1020281527V#5P让我想想……\n',
            '３０分钟左右。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030281528V#026F#4P是这样啊……\n',
            '大致情况我们了解了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281529V#022F最后一个问题……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281530V在玲达小姐昏睡的前后……\n',
            '有发生过什么怪事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1020281531V#5P怪事……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030281532V#020F#4P比如有陌生人来访\n',
            '或者异常的响动之类的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281533V只要能想到的什么都行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1020281534V#5P让我想想……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1020281535V#5P有一件与其说是怪事倒不如\n',
            '说是令人印象深刻的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1020281536V#5P我在厨房准备饭菜的时候，\n',
            '听见了微弱的铃声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1675',
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
            TXT(0x00, '【◇没在其他地方听说过铃的事(没从亚尔丽&胡里奥哪里听说)】\n'),
            TXT(0x01, '【◇已在其他地方听说过铃的事(已从亚尔丽&胡里奥哪里听说)】\n'),
            TXT(0x02, '【◇不变更】\n'),
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
        (0x00000000, 'loc_1669'),
        (0x00000001, 'loc_166F'),
        (-1, 'loc_1675'),
    )

    def _loc_1669(): pass

    label('loc_1669')

    OP_A3(0x1815)

    Jump('loc_1675')

    def _loc_166F(): pass

    label('loc_166F')

    OP_A2(0x1815)

    Jump('loc_1675')

    def _loc_1675(): pass

    label('loc_1675')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 5, 0x1815)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1748',
    )

    ChrTalk(
        0x0103,
        (
            '#0030281537V#023F#4P铃声……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281538V#1004F那是……\n',
            '我们也听到过的那个？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1020281539V#5P音色很美，\n',
            '我还以为是玲达\n',
            '在摇呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1020281540V#5P说起来真让人想不出\n',
            '是从哪里传来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1813')

    def _loc_1748(): pass

    label('loc_1748')

    ChrTalk(
        0x0103,
        (
            '#0030281541V#022F#4P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281542V#1002F这里也提到了铃声……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1020281539V#5P音色很美，\n',
            '我还以为是玲达\n',
            '在摇呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1020281540V#5P说起来真让人想不出\n',
            '是从哪里传来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1813(): pass

    label('loc_1813')

    ChrTalk(
        0x0103,
        (
            '#0030281545V#026F#4P……您给了我们很好的参考。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281546V#020F如果再发现什么事\n',
            '请联系协会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1020281547V#5P嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1020281548V#5P你们也……\n',
            '请一定要小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281549V#1025F嗯，我们会的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281550V谢谢。\n',
            '米蕾奴阿姨。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0008, 90, 0)
    OP_4B(0x0008, 255)
    OP_A2(0x1813)
    OP_28(0x0090, 0x02, 0x0002)
    OP_28(0x0090, 0x01, 0x0004)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 3, 0x1813)),
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 4, 0x1814)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 5, 0x1815)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 6, 0x1816)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1945',
    )

    OP_28(0x0090, 0x01, 0x0200)

    Jump('loc_1945')

    def _loc_1945(): pass

    label('loc_1945')

    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

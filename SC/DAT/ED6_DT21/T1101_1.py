import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T1101_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1101_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0403.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T1101_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x20DD
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
    ]

# id: 0x10002 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0xA8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0xA8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0xA8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xA8
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.PushValueByIndex, 0x13),
            (Expr.PushLong, 0x381),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B5',
    )

    Return()

    def _loc_B5(): pass

    label('loc_B5')

    If(
        (
            (Expr.Eval, "OP_29(0x0079, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0079, 0x00, 0x40)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_C7',
    )

    Return()

    def _loc_C7(): pass

    label('loc_C7')

    SetMapFlags(0x00000080)
    OP_C0(0x01, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    Sleep(30)

    If(
        (
            (Expr.Eval, "OP_CD(0x000A)"),
            Expr.Return,
        ),
        'loc_102',
    )

    Call(1, 0x0001)

    Jump('loc_1A7')

    def _loc_102(): pass

    label('loc_102')

    If(
        (
            (Expr.Eval, "OP_CD(0x0011)"),
            Expr.Return,
        ),
        'loc_111',
    )

    Call(1, 0x0002)

    Jump('loc_1A7')

    def _loc_111(): pass

    label('loc_111')

    If(
        (
            (Expr.Eval, "OP_CD(0x00FF)"),
            Expr.Return,
        ),
        'loc_169',
    )

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '试着出示了照片，\n',
            '但似乎没有见过的印象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    Jump('loc_1A7')

    def _loc_169(): pass

    label('loc_169')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '附近没有人可以确认照片。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    def _loc_1A7(): pass

    label('loc_1A7')

    OP_0D()
    ClearMapFlags(0x00000080)

    Return()

# id: 0x0001 offset: 0x1AE
@scena.Code('Init')
def Init():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_218',
    )

    ChrTalk(
        0x000A,
        (
            '#3510490609V嗯，照片上的小女孩\n',
            '确实有见过的印象……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3510490610V哎呀，是谁来着呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B4')

    def _loc_218(): pass

    label('loc_218')

    ChrTalk(
        0x000A,
        (
            '#3510490605V啊，那个照片……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010490606V#1004F认识这女孩吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0101, 400)

    ChrTalk(
        0x000A,
        (
            '#3510490607V嗯，有见过的印象……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3510490608V哎呀，是谁来着呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_2B4(): pass

    label('loc_2B4')

    TalkEnd(0x000A)

    Return()

# id: 0x0002 offset: 0x2B8
@scena.Code('ReInit')
def ReInit():
    TalkBegin(0x0011)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034A, 3, 0x1A53)),
            Expr.Return,
        ),
        'loc_43C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_356',
    )

    ChrTalk(
        0x0011,
        (
            '#3830490613V这个情况……\n',
            '线索是头发的颜色……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3830490614V表情伴随着成长\n',
            '有了很大的变化……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3830490615V……不能先入为主。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_439')

    def _loc_356(): pass

    label('loc_356')

    ChrTalk(
        0x0011,
        (
            '#3830490611V……行踪调查正在进行啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3830490612V………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3830490613V这个情况……\n',
            '线索是头发的颜色……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3830490614V表情伴随着成长\n',
            '有了很大的变化……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3830490615V……不能先入为主。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000B)

    def _loc_439(): pass

    label('loc_439')

    Jump('loc_440')

    def _loc_43C(): pass

    label('loc_43C')

    Call(0, 0x000C)
    def _loc_440(): pass

    label('loc_440')

    TalkEnd(0x0011)

    Return()

# id: 0x0003 offset: 0x444
@scena.Code('func_03_444')
def func_03_444():
    EventBegin(0x00)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0008, 33010, 0, 74070, 180)
    SetChrPos(0x0009, 33850, 0, 74840, 180)
    OP_4A(0x000E, 255)
    SetChrFlags(0x0000, 0x0008)
    SetChrFlags(0x0001, 0x0008)
    SetChrFlags(0x0002, 0x0008)
    SetChrFlags(0x0003, 0x0008)
    OP_6D(48680, 0, 82940, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3470, 0)
    OP_6C(46000, 0)
    OP_6E(262, 0)

    @scena.Lambda('lambda_04CD')
    def lambda_04CD():
        OP_67(0, 7520, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_04CD)

    @scena.Lambda('lambda_04E5')
    def lambda_04E5():
        OP_6B(2800, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_04E5)

    @scena.Lambda('lambda_04F5')
    def lambda_04F5():
        OP_6C(359000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_04F5)

    @scena.Lambda('lambda_0505')
    def lambda_0505():
        OP_8E(0x0008, 33010, 0, 66360, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0505)

    Sleep(150)

    @scena.Lambda('lambda_0525')
    def lambda_0525():
        OP_8E(0x0009, 33850, 0, 67130, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0525)

    OP_6D(33430, 0, 67300, 6000)
    WaitForThreadExit(0x0008, 0x0001)
    WaitForThreadExit(0x0101, 0x0003)
    Sleep(400)

    ChrTurnDirection(0x0008, 0x0009, 400)

    ChrTalk(
        0x0008,
        (
            '#0360490928V#610F对了，莉拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0008, 400)

    ChrTalk(
        0x0009,
        (
            '#0370490929V#620F是，小姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360490930V#610F关于刚才的事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490931V你定在什么时候？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0370490932V#620F回乡的日期吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370490933V嗯，当然\n',
            '还没决定……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360490934V#610F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490935V决定了的话，\n',
            '就尽快告诉我。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490936V我也得调整\n',
            '日程表才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0370490937V#622F小姐您吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360490938V#610F嗯，我也打算\n',
            '一起去呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490939V你的故乡是怎样的地方，\n',
            '我很想亲眼看看呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490940V而且……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0370490941V#624F而且……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360490942V#610F还想听听各种\n',
            '莉拉小时候的事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490943V你不也听我父亲\n',
            '说了许多我的事吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490944V要是我不掌握点你的弱点\n',
            '交易就不公平了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0370490945V#621F原来如此，目的是这个啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370490946V#620F不过，恐怕会让您失望，\n',
            '我小时候可是绝对的品行端正。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370490947V跟任性妄为的小姐不同，\n',
            '我可没什么把柄怕能让您知道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360490948V#611F哎呀，这可难说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490949V最好还是别小看\n',
            '我的交涉手腕哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0370490950V#621F呵呵，那就期待您的表现了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370490951V那么，回乡的日期\n',
            '随后就会告知给您。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360490952V#610F嗯，拜托了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490953V好了，今天的预定行程\n',
            '是怎么安排的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0370490954V#620F是、午茶时间以前\n',
            '需要回市长官邸办公……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370490955V此后，还有超市的\n',
            '新成员加入审查会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0360490956V#613F呀、审查会\n',
            '是今天！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490957V不，不得了，\n',
            '得先看一遍文件才行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360490958V#614F莉拉，要赶快了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0ACC')
    def lambda_0ACC():
        ChrTurnDirection(0x0009, 0x0008, 400)
        Yield()

        Jump('lambda_0ACC')

    DispatchAsync2(0x0009, 0x0001, lambda_0ACC)

    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_8E(0x0008, 33010, 0, 59000, 5000, 0x00)

    ChrTalk(
        0x0009,
        (
            '#0370490959V#623F呼，真是的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370490960V照这个情形，休假什么的\n',
            '根本就是遥不可及嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0009, 0x01)

    @scena.Lambda('lambda_0B65')
    def lambda_0B65():
        OP_8E(0x0009, 33850, 0, 59000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0B65)

    Sleep(1000)

    FadeOut(2000, 0, -1)
    OP_0D()
    ClearChrFlags(0x0000, 0x0008)
    ClearChrFlags(0x0001, 0x0008)
    ClearChrFlags(0x0002, 0x0008)
    ClearChrFlags(0x0003, 0x0008)
    OP_6D(36200, 400, 79200, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    Sleep(1000)

    EventEnd(0x00)
    FadeIn(2000, 0)
    OP_0D()
    OP_4B(0x000A, 255)
    OP_4B(0x000E, 255)

    Return()

# id: 0x0004 offset: 0xBFF
@scena.Code('func_04_BFF')
def func_04_BFF():
    TalkBegin(0x000D)

    If(
        (
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C15',
    )

    ChrTurnDirection(0x0004, 0x000D, 0)

    def _loc_C15(): pass

    label('loc_C15')

    Fade(1000)
    EventBegin(0x00)
    OP_6D(47700, 0, 47800, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x00F6, 48200, 0, 48120, 90)
    SetChrPos(0x00F7, 48100, 0, 47360, 90)
    SetChrPos(0x00F8, 47200, 0, 48130, 90)
    SetChrPos(0x00F9, 47100, 0, 47320, 90)

    If(
        (
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CBA',
    )

    SetChrPos(0x0004, 46150, 0, 47720, 90)

    def _loc_CBA(): pass

    label('loc_CBA')

    OP_0D()
    OP_62(0x000D, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    OP_63(0x000D)
    ChrTurnDirection(0x000D, 0x0101, 400)

    If(
        (
            (Expr.Eval, "OP_29(0x007B, 0x01, 0x2000)"),
            Expr.Return,
        ),
        'loc_DE1',
    )

    ChrTalk(
        0x000D,
        (
            '#1070480671V哦，是你啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480672V#1007F前阵子真不好意思。\n',
            '招呼才打了一半就走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#1070480673V哪里，不用在意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#1070480674V游击士的工作\n',
            '好象很忙嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480675V#1006F托你的福吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480676V叔叔现在\n',
            '在柏斯做生意？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_117C')

    def _loc_DE1(): pass

    label('loc_DE1')

    ChrTalk(
        0x000D,
        (
            '#1070480642V啊，你是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0065, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_E74',
    )

    ChrTalk(
        0x0101,
        (
            '#0010480669V#1004F啊……\n',
            '这不是玛利诺亚的商人吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480670V#1000F好久不见了。\n',
            '在柏斯做生意吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_117C')

    def _loc_E74(): pass

    label('loc_E74')

    ChrTalk(
        0x0101,
        (
            '#0010480654V#1004F啊，我还在想是谁呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480732V#1001F真的是\n',
            '好久不见了呀。',
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
        'loc_F02',
    )

    ChrTalk(
        0x0106,
        (
            '#0050480656V#052F熟人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0106, 400)

    Jump('loc_FB2')

    def _loc_F02(): pass

    label('loc_F02')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F41',
    )

    ChrTalk(
        0x0103,
        (
            '#0030480657V#023F哎呀，是熟人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    Jump('loc_FB2')

    def _loc_F41(): pass

    label('loc_F41')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F7C',
    )

    ChrTalk(
        0x0108,
        (
            '#0080480658V#070F呼，熟人啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0108, 400)

    Jump('loc_FB2')

    def _loc_F7C(): pass

    label('loc_F7C')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_FB2',
    )

    ChrTalk(
        0x0104,
        (
            '#0040480659V#030F是熟人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0104, 400)

    def _loc_FB2(): pass

    label('loc_FB2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_10E9',
    )

    ChrTalk(
        0x0101,
        (
            '#0010480660V#1000F嗯，这个人\n',
            '是做食材生意的商人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480661V#1007F……现在可不是悠闲\n',
            '让大家自我介绍的时候。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480646V得抓紧时间赶去拉文努村。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#1070480647V看来你们很忙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#1070480664V那么，有机会再见吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000D, 400)

    ChrTalk(
        0x0101,
        (
            '#0010480665V#1002F啊，嗯。\n',
            '那么失陪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x007B, 0x01, 0x2000)
    OP_8C(0x000D, 0, 0)
    EventEnd(0x00)
    TalkEnd(0x000D)

    Return()

    def _loc_10E9(): pass

    label('loc_10E9')

    ChrTalk(
        0x0101,
        (
            '#0010480666V#1000F嗯，这个人\n',
            '是做食材生意的商人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480667V很早以前\n',
            '接受过他的委托。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000D, 400)

    ChrTalk(
        0x0101,
        (
            '#0010480668V#1011F现在到柏斯来做生意吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_117C(): pass

    label('loc_117C')

    ChrTalk(
        0x000D,
        (
            '#1070480677V嗯嗯，为了拓展业务而来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#1070480678V跟『安特洛丝餐厅』谈成生意\n',
            '是此次柏斯之行的最终目标……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1070480748V不过首先还是脚踏实地\n',
            '到超市兜售一下食材吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    OP_22(0x0026, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010480681V#1015F以『安特洛丝餐厅』为目的，\n',
            '为什么却要去超市兜售呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480682V听起来有些不太明白呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#1070480683V嗯，当然我也是很想\n',
            '直接联系那里的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1070480684V但听说那里如果没有介绍人，\n',
            '好象连话也不会听你说一句。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1070480685V嘿，谁让它那么大的名气呢，\n',
            '这也是理所当然的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480686V#1004F啊～不愧是『安特洛丝餐厅』。\n',
            '门坎还真不是一般的高哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#1070480687V话说回来，你们\n',
            '也在这城里做事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480688V#1015F唔，一言难尽……吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480689V#1011F啊，对了\n',
            '说到工作……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480690V那个『安特洛丝餐厅』\n',
            '委托给我们一个任务呢。',
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
        'loc_14BB',
    )

    ChrTalk(
        0x0106,
        (
            '#0050480691V#050F啊啊，是收集\n',
            '珍贵食材的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_158D')

    def _loc_14BB(): pass

    label('loc_14BB')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_14FE',
    )

    ChrTalk(
        0x0103,
        (
            '#0030480692V#020F委托内容是\n',
            '收集珍贵食材呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_158D')

    def _loc_14FE(): pass

    label('loc_14FE')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_154D',
    )

    ChrTalk(
        0x0108,
        (
            '#0080480693V#070F啊啊，我记得委托内容\n',
            '是收集珍贵食材吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_158D')

    def _loc_154D(): pass

    label('loc_154D')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_158D',
    )

    ChrTalk(
        0x0104,
        (
            '#0040480694V#030F嗯，是收集\n',
            '珍贵食材的事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_158D(): pass

    label('loc_158D')

    OP_62(0x000D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000D,
        (
            '#1070480695V什，什么？\n',
            '食、食材的收集……！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1070480696V而且还是，那个\n',
            '『安特洛丝餐厅』委托的！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480697V#1007F这可是相当\n',
            '麻烦的工作哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480698V必须收集的食材中\n',
            '有相当珍贵的东西呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#1070480699V嗯～唔，这可真有趣。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1070480700V那，需要怎样的食材？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480701V#1015F嗯～稍等一下。\n',
            '我先看看手册……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '给奥维德看安特洛丝\n',
            '订的食材清单。',
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
            '#1070480702V哈哈哈，这也，不过如此嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1070480703V要是这些食材的话，\n',
            '我这里随时都有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480772V#1004F啊啊！？真的！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_182F',
    )

    ChrTalk(
        0x0109,
        (
            '#0180480705V#1060F哈～这简直就是\n',
            '女神的指引嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180480706V希望您\n',
            '能助我们一臂之力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19C0')

    def _loc_182F(): pass

    label('loc_182F')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1896',
    )

    ChrTalk(
        0x0104,
        (
            '#0040480707V#030F呵，这真是太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040480708V诸位，这下就正好\n',
            '请他帮个忙吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19C0')

    def _loc_1896(): pass

    label('loc_1896')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_18FB',
    )

    ChrTalk(
        0x0108,
        (
            '#0080480709V#070F噢哟，这可真是太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080480710V希望您\n',
            '能助我们一臂之力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19C0')

    def _loc_18FB(): pass

    label('loc_18FB')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1960',
    )

    ChrTalk(
        0x0103,
        (
            '#0030480711V#020F哎呀，这可真是太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030480712V希望您\n',
            '能助我们一臂之力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19C0')

    def _loc_1960(): pass

    label('loc_1960')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_19C0',
    )

    ChrTalk(
        0x0106,
        (
            '#0050480713V#051F呼，这可真是太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050480714V希望您\n',
            '能助我们一臂之力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19C0(): pass

    label('loc_19C0')

    ChrTalk(
        0x000D,
        (
            '#1070480715V啊啊，我也想拜托你们。\n',
            '这可是绝好的机会啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1070480716V食材我会免费提供，\n',
            '请务必帮我做个介绍。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480717V#1017F是，是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480718V嗯，这样的话\n',
            '就麻烦你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#1070480719V嗯，请多关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F2)
    NewScene('ED6_DT21/T1131._SN', 103, 0, 0)
    IdleLoop()
    EventEnd(0x00)
    TalkEnd(0x000D)

    Return()

# id: 0x0005 offset: 0x1AC0
@scena.Code('func_05_1AC0')
def func_05_1AC0():
    EventBegin(0x00)
    Fade(1000)
    OP_4A(0x0012, 255)
    SetChrPos(0x0012, 19300, 0, 48720, 135)
    SetChrPos(0x0101, 20510, 0, 47110, 320)
    SetChrPos(0x00F7, 21430, 0, 47400, 315)
    SetChrPos(0x00F8, 21520, 0, 46030, 315)
    SetChrPos(0x00F9, 22470, 0, 46390, 315)
    OP_6D(20450, 0, 47700, 0)
    OP_67(0, 8520, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(359000, 0)
    OP_6E(262, 0)
    OP_0D()

    If(
        (
            (Expr.Eval, "OP_29(0x007C, 0x01, 0x4000)"),
            Expr.Return,
        ),
        'loc_1BCE',
    )

    ChrTalk(
        0x0012,
        (
            '#3710490065V已经准备好了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010490066V#1006F嗯，久等了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490067V那么，出发吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F2C')

    def _loc_1BCE(): pass

    label('loc_1BCE')

    ChrTalk(
        0x0012,
        (
            '#3710490068V喔，我可等好久了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#3710490069V赶快出发吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010490070V#1006F嗯，走吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490071V目的地拉文努村吧。',
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
        'loc_1CD2',
    )

    ChrTalk(
        0x0106,
        (
            '#0050490072V#050F啊啊，虽然是走惯了的路\n',
            '但可别忘了有人同行啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050490073V途中的魔兽\n',
            '要尽可能的避开哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E55')

    def _loc_1CD2(): pass

    label('loc_1CD2')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1D50',
    )

    ChrTalk(
        0x0103,
        (
            '#0030490074V#020F嗯，虽然是走惯了的路\n',
            '但可别忘了有人同行哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030490075V途中的魔兽\n',
            '要尽可能的避开哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E55')

    def _loc_1D50(): pass

    label('loc_1D50')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1DD6',
    )

    ChrTalk(
        0x0108,
        (
            '#0080490076V#070F啊啊，虽然怎么走应该都知道，\n',
            '但可别忘了有人同行哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080490077V途中的魔兽\n',
            '要尽可能的避开哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E55')

    def _loc_1DD6(): pass

    label('loc_1DD6')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1E55',
    )

    ChrTalk(
        0x0104,
        (
            '#0040490078V#030F呼，走什么路都知道的吧。\n',
            '不过这次有人同行哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040490079V途中的魔兽\n',
            '要尽可能的避开它们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E55(): pass

    label('loc_1E55')

    ChrTalk(
        0x0012,
        (
            '#3710490080V是呀，没有意义的战斗…\n',
            '而是尽量避开为好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#3710490081V根据工作的质量好坏，\n',
            '奖金也会增加哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010490082V#1006F那我好好努力一下，\n',
            '争取不辜负大家的期望。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490083V#1018F那么，出发前进！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F2C(): pass

    label('loc_1F2C')

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_28(0x007C, 0x01, 0x0004)
    OP_28(0x007C, 0x04, 0x08)

    OP_CE(
        0x00,
        (
            (Expr.PushValueByIndex, 0x15),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FormationAddMember(ChrTable['米拉诺'], 0xFF, 0xFF)
    NewScene('ED6_DT21/R1200._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0006 offset: 0x1F56
@scena.Code('func_06_1F56')
def func_06_1F56():
    EventBegin(0x00)
    FormationDelMember(0x46, 0xFF)
    SetChrPos(0x0012, 19300, 0, 48720, 135)
    OP_4A(0x0012, 255)
    SetChrPos(0x0101, 20510, 0, 47110, 320)
    SetChrPos(0x00F7, 21430, 0, 47400, 315)
    SetChrPos(0x00F8, 21520, 0, 46030, 315)
    SetChrPos(0x00F9, 22470, 0, 46390, 315)
    OP_6D(20450, 0, 47700, 0)
    OP_67(0, 8520, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(359000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x0012,
        (
            '#3710490084V怎么了？\n',
            '城里还有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010490085V#1006F嗯，要回去一趟，\n',
            '需要准备一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010490086V马上回来，\n',
            '还在这里集合吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#3710490087V麻烦快点咯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x007C, 0x01, 0x4000)
    OP_28(0x007C, 0x03, 0x08)

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushValueByIndex, 0x15),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_20B7',
    )

    OP_28(0x007C, 0x01, 0x2000)

    def _loc_20B7(): pass

    label('loc_20B7')

    OP_4B(0x0012, 255)
    SetChrPos(0x0012, 19300, 0, 48720, 180)
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

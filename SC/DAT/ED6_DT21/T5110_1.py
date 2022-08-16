import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T5110_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T5110_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'T5110.x'
    header.mapIndex       = 1
    header.bgm            = 25
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT21/T5110._SN', 'ED6_DT21/T5110_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
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
    ]

# id: 0x10001 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10002 offset: 0xA8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xA8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0xA8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xA8
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0xA9
@scena.Code('func_01_A9')
def func_01_A9():
    Return()

# id: 0x0002 offset: 0xAA
@scena.Code('func_02_AA')
def func_02_AA():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 5, 0x1005)),
            Expr.Return,
        ),
        'loc_270',
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0x9, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x05,
        (
            (Expr.GetChrWork, 0x9, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x0009)
    ChrClearFlags(0x0009, 0x0010)
    ChrTurnDirection(0x0009, 0x0000, 0)

    ExecExpressionWithValue(
        0x0009,
        0x04,
        (
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x04,
        (
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0x9, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x05,
        (
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_141',
    )

    Jump('loc_183')

    def _loc_141(): pass

    label('loc_141')

    If(
        (
            (Expr.GetChrWork, 0x9, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_15D',
    )

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_183')

    def _loc_15D(): pass

    label('loc_15D')

    If(
        (
            (Expr.GetChrWork, 0x9, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_179',
    )

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_183')

    def _loc_179(): pass

    label('loc_179')

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.GetChrWork, 0x9, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_183(): pass

    label('loc_183')

    ExecExpressionWithValue(
        0x0009,
        0x04,
        (
            (Expr.GetChrWork, 0x0, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x0009, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_225',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0009,
        (
            '#0330190671V#843F来了吗，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190672V#840F那就马上开始说明演习内容吧。\n',
            '请坐到对面的位子上吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_265')

    def _loc_225(): pass

    label('loc_225')

    ChrTalk(
        0x0009,
        (
            '#0330190673V#840F赶快，演习要开始了。\n',
            '请坐到对面的位子上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_265(): pass

    label('loc_265')

    ChrSetSubChip(0x0009, 0)
    TalkEnd(0x0009)

    Jump('loc_36C')

    def _loc_270(): pass

    label('loc_270')

    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_308',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0009,
        (
            '#0330190674V#840F啊，是艾丝蒂尔吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190675V请马上整理好装备\n',
            '然后到一楼去吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190676V距离演习开始\n',
            '已经没有多少时间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_369')

    def _loc_308(): pass

    label('loc_308')

    ChrTalk(
        0x0009,
        (
            '#0330190677V#840F先去自己的房间\n',
            '整理好装备吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330190676V离演习开始的时间\n',
            '已经没多久了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_369(): pass

    label('loc_369')

    TalkEnd(0x0009)
    def _loc_36C(): pass

    label('loc_36C')

    Return()

# id: 0x0003 offset: 0x36D
@scena.Code('func_03_36D')
def func_03_36D():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 5, 0x1005)),
            Expr.Return,
        ),
        'loc_4A8',
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0x8, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x05,
        (
            (Expr.GetChrWork, 0x8, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x0008)
    ChrClearFlags(0x0008, 0x0010)
    ChrTurnDirection(0x0008, 0x0000, 0)

    ExecExpressionWithValue(
        0x0008,
        0x04,
        (
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x04,
        (
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0x8, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x05,
        (
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_404',
    )

    Jump('loc_446')

    def _loc_404(): pass

    label('loc_404')

    If(
        (
            (Expr.GetChrWork, 0x8, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_420',
    )

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_446')

    def _loc_420(): pass

    label('loc_420')

    If(
        (
            (Expr.GetChrWork, 0x8, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_43C',
    )

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_446')

    def _loc_43C(): pass

    label('loc_43C')

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.GetChrWork, 0x8, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_446(): pass

    label('loc_446')

    ExecExpressionWithValue(
        0x0008,
        0x04,
        (
            (Expr.GetChrWork, 0x0, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x0008, 0x0010)

    ChrTalk(
        0x0008,
        (
            '#0120190679V#810F艾丝蒂尔，\n',
            '快坐到我旁边来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0008, 0)
    TalkEnd(0x0008)

    Jump('loc_615')

    def _loc_4A8(): pass

    label('loc_4A8')

    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0206, 7, 0x1037)),
            Expr.Return,
        ),
        'loc_526',
    )

    ChrTalk(
        0x0008,
        (
            '#0120190680V#810F赶快准备好，\n',
            '然后到一楼集合吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190681V克鲁茨前辈很讲究守时，\n',
            '如果迟到一定会被骂的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_612')

    def _loc_526(): pass

    label('loc_526')

    SetScenaFlags(ScenaFlag(0x0206, 7, 0x1037))

    ChrTalk(
        0x0008,
        (
            '#0120190682V#814F啊，艾丝蒂尔。\n',
            '已经准备好了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190683V#1000F啊……还要再回去整备一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0120190684V#810F是吗……\n',
            '好，那就快点吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120190685V那么，艾丝蒂尔。\n',
            '待会儿见啰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190686V#1006F嗯，待会儿见！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_612(): pass

    label('loc_612')

    TalkEnd(0x0008)
    def _loc_615(): pass

    label('loc_615')

    Return()

# id: 0x0004 offset: 0x616
@scena.Code('func_04_616')
def func_04_616():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 6, 0x1006)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_802',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 5, 0x1005)),
            Expr.Return,
        ),
        'loc_68D',
    )

    ChrTalk(
        0x000A,
        (
            '#2760190693V先听听克鲁茨前辈\n',
            '要说些什么吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760190694V他好像有什么东西\n',
            '想交给你们哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7FB')

    def _loc_68D(): pass

    label('loc_68D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 7, 0x1007)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_78D',
    )

    ChrTalk(
        0x000A,
        (
            '#2760190687V呀，早上好啊，艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760190688V早上的锻炼也很辛苦啊，\n',
            '在这里都听得到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760190689V导力工房暂时还无法使用，\n',
            '不过在你们出发前就可以恢复正常。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760190690V想调整导力器或购买结晶回路的话\n',
            '等一会儿再来就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7FB')

    def _loc_78D(): pass

    label('loc_78D')

    ChrTalk(
        0x000A,
        (
            '#2760190691V导力工房现在还在\n',
            '进行开店准备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760190692V不过在你们出发之前肯定\n',
            '可以开张，放心好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7FB(): pass

    label('loc_7FB')

    SetScenaFlags(ScenaFlag(0x0200, 7, 0x1007))
    TalkEnd(0x000A)

    Return()

    def _loc_802(): pass

    label('loc_802')

    If(
        (
            (Expr.Eval, "OP_29(0x00C5, 0x01, 0x0008)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_816',
    )

    Call(1, 0x0007)
    TalkEnd(0x000A)

    Return()

    def _loc_816(): pass

    label('loc_816')

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
            TXT(0x01, '改造·换钱\n'),
            TXT(0x02, '买东西\n'),
            TXT(0x03, '离开\n'),
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
        'loc_888',
    )

    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0201, 1, 0x1009)),
            Expr.Return,
        ),
        'loc_880',
    )

    OP_A9(0xFA)

    Jump('loc_882')

    def _loc_880(): pass

    label('loc_880')

    OP_A9(0xFD)

    def _loc_882(): pass

    label('loc_882')

    OP_56(0x00)
    TalkEnd(0x000A)

    Return()

    def _loc_888(): pass

    label('loc_888')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8AA',
    )

    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0201, 1, 0x1009)),
            Expr.Return,
        ),
        'loc_8A2',
    )

    OP_A9(0xFB)

    Jump('loc_8A4')

    def _loc_8A2(): pass

    label('loc_8A2')

    OP_A9(0xFE)

    def _loc_8A4(): pass

    label('loc_8A4')

    OP_56(0x00)
    TalkEnd(0x000A)

    Return()

    def _loc_8AA(): pass

    label('loc_8AA')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8BB',
    )

    TalkEnd(0x000A)

    Return()

    def _loc_8BB(): pass

    label('loc_8BB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0201, 1, 0x1009)),
            Expr.Return,
        ),
        'loc_914',
    )

    ChrTalk(
        0x000A,
        (
            '#2760190695V演习怎么样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760190696V需要整备的时候\n',
            '就回这里来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CAB')

    def _loc_914(): pass

    label('loc_914')

    If(
        (
            (Expr.Eval, "OP_B9(0x00, 0x006E)"),
            (Expr.Eval, "OP_B9(0x09, 0x006E)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_98A',
    )

    ChrTalk(
        0x000A,
        (
            '#2760190705V嗯，你们已经可以使用\n',
            '回复魔法了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760190706V那么，你们俩\n',
            '小心一些出发吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CAB')

    def _loc_98A(): pass

    label('loc_98A')

    If(
        (
            (Expr.Eval, "OP_40(0x0258, 0x00)"),
            Expr.Return,
        ),
        'loc_B04',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_A0D',
    )

    ChrTalk(
        0x000A,
        (
            '#2760190707V把『ＨＰ１』的结晶回路装备上\n',
            '就可以使用回复魔法了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760190708V有了它的话\n',
            '就万无一失了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B01')

    def _loc_A0D(): pass

    label('loc_A0D')

    ChrTalk(
        0x000A,
        (
            '#2760190709V噢，看来你们已经顺利\n',
            '合成了结晶回路啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760190710V把它镶嵌到导力器中\n',
            '就可以使用回复魔法了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760190711V那样的话就算是准备万全了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760190697V好了，克鲁茨前辈还在外边等着呢。\n',
            '赶快把结晶回路镶嵌好就出发吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    def _loc_B01(): pass

    label('loc_B01')

    Jump('loc_CAB')

    def _loc_B04(): pass

    label('loc_B04')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_BD8',
    )

    ChrTalk(
        0x000A,
        (
            '#2760190698V啊，难道不知道该怎么做吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760190699V真是拿你没办法……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760190700V只要合成结晶回路『ＨＰ１』\n',
            '就可以了啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760190701V把它镶嵌到导力器中\n',
            '有了它就可以施展回复魔法了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CAB')

    def _loc_BD8(): pass

    label('loc_BD8')

    ChrTalk(
        0x000A,
        (
            '#2760190702V回复魔法的名字是『回复术』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760190703V查看游击士手册中的『魔法表』\n',
            '就可以知道它所需要的回路属性值了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760190704V想合成结晶回路的时候，\n',
            '在[改造·换钱]中选择[结晶回路]就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_CAB(): pass

    label('loc_CAB')

    TalkEnd(0x000A)

    Return()

# id: 0x0005 offset: 0xCAF
@scena.Code('func_05_CAF')
def func_05_CAF():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 5, 0x1005)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E54',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0206, 5, 0x1035)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DFF',
    )

    SetScenaFlags(ScenaFlag(0x0206, 5, 0x1035))

    ChrTalk(
        0x000B,
        (
            '#2750190712V哎呀，艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2750190713V怎么样？吃饱了没有？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190714V#1008F嘿嘿嘿，已经吃撑了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190715V实在太好吃了，\n',
            '不知不觉就吃好多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2750190716V呵呵，那就好㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2750190717V今天的训练\n',
            '好像是很重要的演习呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2750190718V拿出干劲\n',
            '努力上吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190719V#1006F嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E50')

    def _loc_DFF(): pass

    label('loc_DFF')

    ChrTalk(
        0x000B,
        (
            '#2750190720V训练要加油啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2750190721V我会准备好美味的晚餐\n',
            '等你们的㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E50(): pass

    label('loc_E50')

    TalkEnd(0x000B)

    Return()

    def _loc_E54(): pass

    label('loc_E54')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 5, 0x1005)),
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 6, 0x1006)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_EBB',
    )

    ChrTalk(
        0x000B,
        (
            '#2750190722V啊，快点过去坐吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2750190723V克鲁茨先生和亚妮拉丝\n',
            '一直在等你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000B)

    Return()

    def _loc_EBB(): pass

    label('loc_EBB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 6, 0x1006)),
            (Expr.Eval, "OP_29(0x00C5, 0x01, 0x0004)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_ED3',
    )

    Call(1, 0x0006)
    TalkEnd(0x000B)

    Return()

    def _loc_ED3(): pass

    label('loc_ED3')

    Call(6, 0x0004)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_EF8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0201, 1, 0x1009)),
            Expr.Return,
        ),
        'loc_EF0',
    )

    OP_A9(0xFC)

    Jump('loc_EF2')

    def _loc_EF0(): pass

    label('loc_EF0')

    OP_A9(0xFF)

    def _loc_EF2(): pass

    label('loc_EF2')

    OP_56(0x00)
    TalkEnd(0x000B)

    Return()

    def _loc_EF8(): pass

    label('loc_EF8')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F09',
    )

    TalkEnd(0x000B)

    Return()

    def _loc_F09(): pass

    label('loc_F09')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0201, 1, 0x1009)),
            Expr.Return,
        ),
        'loc_1010',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_FB2',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x000B,
        (
            '#2750190724V哎呀，你们两人辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2750190725V有什么需要的东西\n',
            '赶快回宿舍休息吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2750190726V我和罗伯特先生\n',
            '会一直在这里等着你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_100D')

    def _loc_FB2(): pass

    label('loc_FB2')

    ChrTalk(
        0x000B,
        (
            '#2750190725V有什么需要的东西\n',
            '赶快回宿舍休息吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2750190728V那么，演习时加油吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_100D(): pass

    label('loc_100D')

    Jump('loc_1100')

    def _loc_1010(): pass

    label('loc_1010')

    If(
        (
            (Expr.Eval, "OP_29(0x00C5, 0x01, 0x0004)"),
            Expr.Return,
        ),
        'loc_1096',
    )

    ChrTalk(
        0x000B,
        (
            '#2750190729V在情况危险的时候\n',
            '别忘了吃些料理，然后休息一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2750190730V有干劲虽然很好，\n',
            '但一定不要太勉强啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1100')

    def _loc_1096(): pass

    label('loc_1096')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 5, 0x1005)),
            Expr.Return,
        ),
        'loc_1100',
    )

    ChrTalk(
        0x000B,
        (
            '#2750190731V快点快点，克鲁茨先生已经在等着了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2750190732V快点去听他说明演习内容吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1100')

    def _loc_1100(): pass

    label('loc_1100')

    TalkEnd(0x000B)

    Return()

# id: 0x0006 offset: 0x1104
@scena.Code('func_06_1104')
def func_06_1104():
    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, 22220, 0, 12120, 90)
    ChrSetPos(0x010A, 21720, 0, 12890, 90)
    ChrSetDirection(0x000B, 270, 0)
    CameraMove(23050, 0, 12920, 0)
    OP_0D()

    ChrTalk(
        0x000B,
        (
            '#2750190733V今天的演习\n',
            '好像要比平时更严酷呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2750190734V我现在把这个简单料理\n',
            '的配方教给你吧㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['料理手册']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    AddItem(ItemTable['料理手册'], 1)

    If(
        (
            (Expr.Eval, "OP_40(0x020D, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1229',
    )

    If(
        (
            (Expr.Eval, "OP_AC(0x001E)"),
            Expr.Return,
        ),
        'loc_11FB',
    )

    Jump('loc_1229')

    def _loc_11FB(): pass

    label('loc_11FB')

    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x2),
            '大自然恩惠之水',
            (TxtCtl.SetColor, 0x0),
            '的做法已经学会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1229(): pass

    label('loc_1229')

    OP_56(0x00)
    FadeIn(300, 0)
    OP_0D()

    ChrTalk(
        0x000B,
        (
            '#2750190735V对了，食材也别忘记了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#20I食材的组合',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_0D()
    AddItem(ItemTable['枫糖'], 10)
    AddItem(ItemTable['清新香草'], 10)
    AddItem(ItemTable['皇家香叶'], 10)
    AddItem(ItemTable['爽口洋葱'], 10)
    AddItem(ItemTable['鲜味马铃薯'], 10)
    AddItem(ItemTable['新磨小麦粉'], 10)
    AddItem(ItemTable['魔兽明胶'], 2)

    ChrTalk(
        0x010A,
        (
            '#0120190736V#0814F现在就用手里的食材\n',
            '试着制作料理如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2750190737V嗯，普通料理所需的食材\n',
            '都很容易买到……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2750190738V不过有些料理所需的食材…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2750190739V需要打倒魔兽后才能得到，\n',
            '光是收集就很辛苦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190740V#1016F确、确实……\n',
            '有很多食材是非常稀少的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120190741V#0817F嗯～原来如此。\n',
            '天上是不会掉馅饼的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2750190742V有关料理的详细说明\n',
            '在游击士手册中就有记载，\n',
            '有时间的话仔细读读吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2750190743V那么，你们两个～\n',
            '演习时要加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190744V#1006F嗯，谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120190745V#1310F制作料理…马上来试试吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※品尝餐厅、酒馆的『推荐菜式』，\n',
            '　或是使用道具中的『携带料理』后，\n',
            '　都会在料理手册中自动添加新料理配方。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '※有了食材和配方后，只要食材足够的话，\n',
            '　就可以随时制作料理了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '※料理手册的打开方法∶在主菜单的［Items］\n',
            '  项中的[书籍]类别中选择『料理手册』。\n',
            '  另外点击画面右下方的图标(红)也可以打开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x00C5, 0x01, 0x0004)
    FadeIn(300, 0)
    OP_0D()
    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0x1654
@scena.Code('func_07_1654')
def func_07_1654():
    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, 24620, 0, 4960, 90)
    ChrSetPos(0x010A, 24060, 0, 5730, 90)
    ChrSetDirection(0x000A, 270, 0)
    CameraMove(24720, 0, 5730, 0)
    OP_0D()

    ChrTalk(
        0x000A,
        (
            '#2760190746V哟，看来你们两个都已经\n',
            '装备上新型导力器了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760190747V手册中记载的新型结晶回路\n',
            '和魔法目录\n',
            '已经读过了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760190748V基本使用方法和原来的导力器\n',
            '没什么不同，但具体性能还是有区别的，\n',
            '最好仔细熟悉一下啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760190749V在正式使用导力器之前\n',
            '先来复习一下相关的知识吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760190750V有关导力器的知识，\n',
            '如果有什么内容忘记了可以问我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    def _loc_1804(): pass

    label('loc_1804')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2087',
    )

    SetMessageWindowPos(-1, 50, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            0x18,
            (TxtCtl.SetColor, 0x5),
            '想询问什么内容呢？',
            TxtCtl.Enter,
        ),
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
        -1,
        155,
        0,
        (
            TXT(0x00, '【导力器】\n'),
            TXT(0x01, '【导力魔法】\n'),
            TXT(0x02, '【结晶回路】\n'),
            TXT(0x03, '【耀晶片】\n'),
            TXT(0x04, '【结晶孔强化】\n'),
            TXT(0x05, '【放弃】\n'),
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
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_18DC'),
        (0x00000001, 'loc_1A7B'),
        (0x00000002, 'loc_1C5B'),
        (0x00000003, 'loc_1DDD'),
        (0x00000004, 'loc_1F0D'),
        (0x00000005, 'loc_2072'),
        (-1, 'loc_2082'),
    )

    def _loc_18DC(): pass

    label('loc_18DC')

    ChrTalk(
        0x000A,
        (
            '#2760190751V所谓的导力器，\n',
            '即是可以通过镶嵌的结晶回路\n',
            '而发挥出各种效能的机械。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760190752V这里所说的导力器是一种\n',
            '可以提高身体能力，并可以施展出魔法\n',
            '的『战术导力器』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760190753V战术导力器都是根据使用者量身定做，\n',
            '因为每个人的战术导力器\n',
            '具体构造都是不同的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760190754V说具体一点，就是结晶孔属性\n',
            '和结晶链都各不相同。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760190755V要想发挥出导力器的最大效力\n',
            '就必须熟悉自己导力器的特性。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2082')

    def _loc_1A7B(): pass

    label('loc_1A7B')

    ChrTalk(
        0x000A,
        (
            '#2760190756V所谓的导力魔法，\n',
            '就是需要通过『战术导力器』\n',
            '而施展的魔法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760190757V因为『导力魔法』这个名字比较拗口，\n',
            '因此大家一般都简称它为『魔法』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760190758V要想使用魔法的话\n',
            '就必须先到工房合成结晶回路。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760190759V把合成好的结晶回路镶嵌到导力器中\n',
            '就可以施展出各种各样的魔法了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760190760V所以，可以使用的魔法种类\n',
            '会因导力器镶嵌结晶回路的属性不同\n',
            '而发生改变。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760190761V如果想使用水属性的魔法，\n',
            '在导力器中镶嵌水属性的\n',
            '结晶回路就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2082')

    def _loc_1C5B(): pass

    label('loc_1C5B')

    ChrTalk(
        0x000A,
        (
            '#2760190762V所谓的结晶回路，\n',
            '就是用耀晶片合成的回路。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760190763V结晶回路不仅能决定\n',
            '可以使用的魔法，还会提高\n',
            '装备者的自身能力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760190764V结晶回路要镶嵌到导力器的结晶孔\n',
            '之后才能发挥效果，不过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760190765V有些结晶孔只能镶嵌特定属性的结晶\n',
            '回路，其他属性的回路无法镶嵌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760190766V另外，有些高级的结晶回路\n',
            '只能镶嵌在强化后的结晶孔里，\n',
            '这一点也请注意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2082')

    def _loc_1DDD(): pass

    label('loc_1DDD')

    ChrTalk(
        0x000A,
        (
            '#2760190767V所谓的耀晶片就是魔兽掉落的\n',
            '七耀石的碎片。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760190768V因颜色的不同，分为#56I地·#57I水·#58I火·#59I风·\n',
            '#62I时·#60I空·#61I幻……这７个种类。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760190769V耀晶片在很多地方都可以\n',
            '直接换钱，不过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760190770V最好还是到工房利用它们\n',
            '来合成强力的结晶回路\n',
            '或强化导力孔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2082')

    def _loc_1F0D(): pass

    label('loc_1F0D')

    ChrTalk(
        0x000A,
        (
            '#2760190771V新型导力器的特征之一\n',
            '就是结晶孔的强化程度。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760190772V新型导力器可以镶嵌\n',
            '很多种性能超群的\n',
            '结晶回路，不过…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760190773V要想镶嵌那些强力结晶回路的话\n',
            '首先要将结晶孔进行强化。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760190774V另外，在强化结晶孔的同时，\n',
            '自身的ＥＰ最大值也会增加。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760190775V虽然这么做需要消费不少耀晶片，\n',
            '但如果数量足够的话一定要试试看！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2082')

    def _loc_2072(): pass

    label('loc_2072')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)

    Jump('loc_2082')

    def _loc_2082(): pass

    label('loc_2082')

    OP_56(0x00)

    Jump('loc_1804')

    def _loc_2087(): pass

    label('loc_2087')

    ChrTalk(
        0x000A,
        (
            '#2760190776V那么，说明就到此为止，\n',
            '接下来赶快去做演习的准备吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760190777V在战斗前最好先准备好\n',
            '回复类的魔法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760190778V你们应该已经知道使用\n',
            '回复魔法需要哪种结晶回路了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#2760190779V如果不知道的话就查看一下手册中\n',
            '的说明，尽快合成出来吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x00C5, 0x01, 0x0008)
    OP_28(0x00C5, 0x01, 0x0010)
    OP_28(0x00C5, 0x01, 0x0020)
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

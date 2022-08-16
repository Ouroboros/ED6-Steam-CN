import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T1103_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1103_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1103.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT21/T1103._SN', 'ED6_DT21/T1103_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
    TalkBegin(0x0035)

    If(
        (
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BF',
    )

    ChrTurnDirection(0x0004, 0x0035, 0)

    def _loc_BF(): pass

    label('loc_BF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_122',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x007B, 0x01, 0x2000)"),
            Expr.Return,
        ),
        'loc_122',
    )

    ChrTurnDirection(0x0035, 0x0101, 400)

    ChrTalk(
        0x0035,
        (
            '#1070480720V怎么了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0035,
        (
            '#1070480721V不是很着急吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0035, 0, 0)
    TalkEnd(0x0035)

    Return()

    def _loc_122(): pass

    label('loc_122')

    Fade(1000)
    EventBegin(0x00)
    CameraMove(47700, 0, 47800, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2700, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x00F6, 48200, 0, 48120, 90)
    ChrSetPos(0x00F7, 48100, 0, 47360, 90)
    ChrSetPos(0x00F8, 47200, 0, 48130, 90)
    ChrSetPos(0x00F9, 47100, 0, 47320, 90)

    If(
        (
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1C7',
    )

    ChrSetPos(0x0004, 46150, 0, 47720, 90)

    def _loc_1C7(): pass

    label('loc_1C7')

    OP_0D()
    OP_62(0x0035, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    OP_63(0x0035)
    ChrTurnDirection(0x0035, 0x0101, 400)

    If(
        (
            (Expr.Eval, "OP_29(0x007B, 0x01, 0x2000)"),
            Expr.Return,
        ),
        'loc_2EE',
    )

    ChrTalk(
        0x0035,
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
        0x0035,
        (
            '#1070480673V哪里，不用在意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0035,
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

    Jump('loc_86C')

    def _loc_2EE(): pass

    label('loc_2EE')

    ChrTalk(
        0x0035,
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
        'loc_56C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_501',
    )

    ChrTalk(
        0x0101,
        (
            '#0010480643V#1000F啊，好久不见。\n',
            '这不是在卢安的商人吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480644V在柏斯做生意吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480645V#1007F……现在可不是悠闲\n',
            '让大家自我介绍的时候。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480646V得抓紧时间赶去拉文努村。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0035,
        (
            '#1070480647V看来你们很忙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0035,
        (
            '#1070480648V看起来\n',
            '你们正在调查事件？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480649V#1002F嗯……\n',
            '正是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0035,
        (
            '#1070480650V是吗……\n',
            '路上要小心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0035,
        (
            '#1070480651V等下次有机会\n',
            '再聊聊近况吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480652V#1002F叔叔也要小心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480653V那么，失陪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x007B, 0x01, 0x2000)
    ChrSetDirection(0x0035, 0, 0)
    EventEnd(0x00)
    TalkEnd(0x0035)

    Return()

    def _loc_501(): pass

    label('loc_501')

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

    Jump('loc_86C')

    def _loc_56C(): pass

    label('loc_56C')

    ChrTalk(
        0x0101,
        (
            '#0010480654V#1004F啊，我还在想是谁呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480655V真是\n',
            '好久不见了呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5F2',
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

    Jump('loc_6A2')

    def _loc_5F2(): pass

    label('loc_5F2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_631',
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

    Jump('loc_6A2')

    def _loc_631(): pass

    label('loc_631')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_66C',
    )

    ChrTalk(
        0x0108,
        (
            '#0080480658V#070F噢，熟人啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0108, 400)

    Jump('loc_6A2')

    def _loc_66C(): pass

    label('loc_66C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6A2',
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

    def _loc_6A2(): pass

    label('loc_6A2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7DB',
    )

    ChrTalk(
        0x0101,
        (
            '#0010480660V#1000F嗯，这个人\n',
            '是做食材生意的商人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480661V#1007F……现在好象不是悠闲\n',
            '让大家自我介绍的时候。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480646V得抓紧时间赶去拉文努村。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0035,
        (
            '#1070480647V看来你们很忙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0035,
        (
            '#1070480664V那么，有机会再见吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0035, 400)

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
    ChrSetDirection(0x0035, 0, 0)
    EventEnd(0x00)
    TalkEnd(0x0035)

    Return()

    def _loc_7DB(): pass

    label('loc_7DB')

    ChrTalk(
        0x0101,
        (
            '#0010480666V#1000F嗯，这个人\n',
            '做食材生意的商人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480667V很早以前\n',
            '接受过他的委托。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0035, 400)

    ChrTalk(
        0x0101,
        (
            '#0010480668V#1011F现在到柏斯来做生意吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_86C(): pass

    label('loc_86C')

    ChrTalk(
        0x0035,
        (
            '#1070480677V嗯嗯，为了拓展业务而来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0035,
        (
            '#1070480678V跟『安特洛丝餐厅』谈成生意\n',
            '是此次柏斯之行的最终目标……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1070480679V在这之前本来打算\n',
            '先到超市兜售寻找买家。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1070480680V不过，很遗憾……\n',
            '在那之前出事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010480681V#1015F以『安特洛丝餐厅』为目的\n',
            '为什么却要去超市兜售呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480682V听起来有些不太明白呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0035,
        (
            '#1070480683V嗯，当然我也是很想\n',
            '直接联系那里的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1070480684V但听说那里如果没有介绍人，\n',
            '好象连话也不会听你说一句。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1070480685V嘿，谁让它那么大名气，\n',
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
        0x0035,
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
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BD0',
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

    Jump('loc_CA2')

    def _loc_BD0(): pass

    label('loc_BD0')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C13',
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

    Jump('loc_CA2')

    def _loc_C13(): pass

    label('loc_C13')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C62',
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

    Jump('loc_CA2')

    def _loc_C62(): pass

    label('loc_C62')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CA2',
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

    def _loc_CA2(): pass

    label('loc_CA2')

    OP_62(0x0035, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0035,
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
        0x0035,
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
    TalkSetChrName('')

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
        0x0035,
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
            '#0010480704V#1004F啊啊！？真的！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F42',
    )

    ChrTalk(
        0x0109,
        (
            '#0180480705V#1060F哈～这简直就是\n',
            '女神的指引嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180480706V希望\n',
            '能助我们一臂之力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10D3')

    def _loc_F42(): pass

    label('loc_F42')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_FA9',
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

    Jump('loc_10D3')

    def _loc_FA9(): pass

    label('loc_FA9')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_100E',
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

    Jump('loc_10D3')

    def _loc_100E(): pass

    label('loc_100E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1073',
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

    Jump('loc_10D3')

    def _loc_1073(): pass

    label('loc_1073')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_10D3',
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

    def _loc_10D3(): pass

    label('loc_10D3')

    ChrTalk(
        0x0035,
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
        0x0035,
        (
            '#1070480719V嗯，请多关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    NewScene('ED6_DT21/T1131._SN', 103, 0, 0)
    IdleLoop()
    EventEnd(0x00)
    TalkEnd(0x0035)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

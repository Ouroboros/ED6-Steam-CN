import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T1131_2_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1131_2 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1131.x'
    header.mapIndex       = 1
    header.bgm            = 11
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
    EventBegin(0x00)
    Fade(1000)
    OP_4A(0x000A, 255)
    ChrSetPos(0x000A, -47710, 0, 44840, 270)
    ChrSetPos(0x0101, -46020, 0, 44370, 270)
    ChrSetPos(0x00F7, -45610, 0, 45370, 270)
    ChrSetPos(0x00F8, -44250, 0, 45330, 270)
    ChrSetPos(0x00F9, -44580, 0, 44110, 270)

    If(
        (
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_125',
    )

    ChrSetPos(0x0004, -43430, 0, 44650, 270)

    def _loc_125(): pass

    label('loc_125')

    If(
        (
            (Expr.Eval, "OP_29(0x007B, 0x01, 0x1000)"),
            Expr.Return,
        ),
        'loc_137',
    )

    ChrSetDirection(0x000A, 90, 0)

    def _loc_137(): pass

    label('loc_137')

    CameraMove(-46490, 0, 45440, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1E5',
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
            TXT(0x00, '【◇QST018完成】\n'),
            TXT(0x01, '【◇QST018未完成】\n'),
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
        (0x00000000, 'loc_1D5'),
        (0x00000001, 'loc_1DD'),
        (-1, 'loc_1E5'),
    )

    def _loc_1D5(): pass

    label('loc_1D5')

    OP_28(0x0012, 0x04, 0x10)

    Jump('loc_1E5')

    def _loc_1DD(): pass

    label('loc_1DD')

    OP_28(0x0012, 0x03, 0x10)

    Jump('loc_1E5')

    def _loc_1E5(): pass

    label('loc_1E5')

    If(
        (
            (Expr.Eval, "OP_29(0x007B, 0x01, 0x1000)"),
            Expr.Return,
        ),
        'loc_2BB',
    )

    ChrTalk(
        0x000A,
        (
            '#1350480587V哎呀，游击士们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480570V委托你们工作\n',
            '没问题了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2B8',
    )

    ChrTalk(
        0x0101,
        (
            '#0010480571V#1007F抱歉，还不行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480572V#1002F我们还会再来的，\n',
            '那时再说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x007B, 0x01, 0x1000)
    EventEnd(0x00)
    OP_4B(0x000A, 255)
    TerminateThread(0x000A, 0x00)
    CreateThread(0x000A, 0x00, 0x00, 0x0002)

    Return()

    def _loc_2B8(): pass

    label('loc_2B8')

    Jump('loc_631')

    def _loc_2BB(): pass

    label('loc_2BB')

    ChrClearFlags(0x000A, 0x0010)
    ChrSetDirection(0x000A, 90, 400)

    ChrTalk(
        0x000A,
        (
            '#1350480547V是，什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0012, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_409',
    )

    ChrTalk(
        0x0101,
        (
            '#0010480548V#1000F嗯，我们是看了\n',
            '公告板来的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480549V你是格露娜小姐吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480550V嗯嗯，是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480551V哎呀？你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480552V不是之前\n',
            '帮我收集食材的人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480553V#1017F嘿嘿，好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480554V啊哈哈，看来\n',
            '好象很有缘呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4AF')

    def _loc_409(): pass

    label('loc_409')

    ChrTalk(
        0x0101,
        (
            '#0010480548V#1000F嗯，我们是看了\n',
            '公告板来的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480556V你是格露娜小姐？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480557V嗯嗯，我就是格露娜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480558V是游击士们吧。\n',
            '正等你们呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4AF(): pass

    label('loc_4AF')

    ChrTalk(
        0x000A,
        (
            '#1350480559V事不宜迟，\n',
            '可以帮忙工作了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_631',
    )

    ChrTalk(
        0x0101,
        (
            '#0010480560V#1006F嗯，当然。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480561V#1007F……虽然想马上开始，\n',
            '但其实还有些急事要做。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480562V是吗……\n',
            '因为那个龙的骚乱事件吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480563V那样就没办法了。\n',
            '有空了请再来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480564V也不是什么紧急的工作，\n',
            '不用着急的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480565V#1002F抱歉。\n',
            '那，我们会再来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x007B, 0x01, 0x1000)
    EventEnd(0x00)
    OP_4B(0x000A, 255)
    TerminateThread(0x000A, 0x00)
    CreateThread(0x000A, 0x00, 0x00, 0x0002)

    Return()

    def _loc_631(): pass

    label('loc_631')

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
            TXT(0x00, '【是】\n'),
            TXT(0x01, '【否】\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7AC',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x007B, 0x01, 0x1000)"),
            Expr.Return,
        ),
        'loc_6DF',
    )

    ChrTalk(
        0x0101,
        (
            '#0010480571V#1007F抱歉，还不行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480574V我们会再来的，\n',
            '那时再说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_794')

    def _loc_6DF(): pass

    label('loc_6DF')

    ChrTalk(
        0x0101,
        (
            '#0010480566V#1015F嗯……抱歉。\n',
            '现在有点不方便。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480567V哎呀呀，这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480568V嗯，明白了。\n',
            '有空了请再来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480569V#1007F抱歉。\n',
            '那就先这样吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_794(): pass

    label('loc_794')

    OP_28(0x007B, 0x01, 0x1000)
    EventEnd(0x00)
    OP_4B(0x000A, 255)
    TerminateThread(0x000A, 0x00)
    CreateThread(0x000A, 0x00, 0x00, 0x0002)

    Return()

    def _loc_7AC(): pass

    label('loc_7AC')

    ChrTalk(
        0x0101,
        (
            '#0010480575V#1006F嗯，没问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480576V#1015F公告板上面写着\n',
            '收集食材的工作吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480577V嗯，是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480578V为了研究新菜单，\n',
            '我需要稀有的食材。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480579V而且，还想顺便\n',
            '麻烦收集其他的食材。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_8F5',
    )

    ChrTalk(
        0x000A,
        (
            '#1350480585V倒不是很紧急的工作，\n',
            '但时间也不多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480586V所以请各位\n',
            '尽快解决吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A1F')

    def _loc_8F5(): pass

    label('loc_8F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Return,
        ),
        'loc_969',
    )

    ChrTalk(
        0x000A,
        (
            '#1350480580V由于龙的骚乱事件\n',
            '大家都很忙吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480581V不是什么紧急的工作，\n',
            '有空的时候再来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A1F')

    def _loc_969(): pass

    label('loc_969')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_9E1',
    )

    ChrTalk(
        0x000A,
        (
            '#1350480582V似乎发生了什么事件，\n',
            '大家都很忙吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480581V不是什么紧急的工作，\n',
            '有空的时候再来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A1F')

    def _loc_9E1(): pass

    label('loc_9E1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_A1F',
    )

    ChrTalk(
        0x000A,
        (
            '#1350480584V也不是紧急的工作，\n',
            '有空的时候再来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A1F(): pass

    label('loc_A1F')

    ChrTalk(
        0x0101,
        (
            '#0010480588V#1006F原来如此，明白了。',
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
        'loc_AC7',
    )

    ChrTalk(
        0x0106,
        (
            '#0050480589V#050F那么，说明一下\n',
            '寻找食材的方法吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050480590V因为必要的食材清单里\n',
            '也有很稀有的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C42')

    def _loc_AC7(): pass

    label('loc_AC7')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B47',
    )

    ChrTalk(
        0x0103,
        (
            '#0030480591V#020F那么，能说明一下\n',
            '寻找食材的方法吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030480592V因为必要的食材清单里\n',
            '也有很稀有的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C42')

    def _loc_B47(): pass

    label('loc_B47')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BC5',
    )

    ChrTalk(
        0x0108,
        (
            '#0080480593V#070F那么，说明一下\n',
            '寻找食材的方法吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080480594V因为必要的食材清单里\n',
            '也有很稀有的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C42')

    def _loc_BC5(): pass

    label('loc_BC5')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C42',
    )

    ChrTalk(
        0x0104,
        (
            '#0040480595V#030F那么，不说明一下\n',
            '寻找食材的方法吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040480596V因为必要的食材清单里\n',
            '也有很稀有的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C42(): pass

    label('loc_C42')

    ChrTalk(
        0x0101,
        (
            '#0010480597V#1011F啊，这个得确认一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480598V#1015F例如『魔兽之骨』什么的，\n',
            '好象还挺难弄到的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480599V难得到的有\n',
            '『魔兽之骨』和『魔兽之角』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480600V其它特别该举出来的，\n',
            '就是『魔兽之牙』什么的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480601V#1002F这些全部\n',
            '都能在柏斯地区弄到吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480602V嗯嗯，应该是的。\n',
            '大致的魔兽身上都有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480603V首先，『魔兽之骨』\n',
            '应该能在迷雾峡谷找到哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480604V而『魔兽之角』\n',
            '在北边的拉文努山道……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480605V最后的『魔兽之牙』也\n',
            '能在古罗尼山顶弄到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480606V#1007F地、地方都散落各处呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480607V这搞不好挺麻烦的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480608V呼呼，那是当然的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480609V正因为麻烦，\n',
            '才这样委托各位嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480610V#1008F啊……说得也是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480611V如果食材全部集齐了，\n',
            '就请拿来这里吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480612V麻烦请集齐了再来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480613V分别拿来也不会接受的，\n',
            '这点请注意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480614V#1006F一个不少的集齐了\n',
            '交来这里就行了吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480615V的确，这样我们\n',
            '也少费点工夫。',
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
        'loc_108C',
    )

    ChrTalk(
        0x0109,
        (
            '#0180480616V#1066F嗯，只要不自己偷吃掉\n',
            '就没问题了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180480617V还有，做饭的时候\n',
            '要注意所使用的食材哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1265')

    def _loc_108C(): pass

    label('loc_108C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1102',
    )

    ChrTalk(
        0x0104,
        (
            '#0040480618V#035F呼，这么说\n',
            '就是严禁我们先偷吃吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040480619V做饭的时候\n',
            '要注意所使用的食材。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1265')

    def _loc_1102(): pass

    label('loc_1102')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1176',
    )

    ChrTalk(
        0x0108,
        (
            '#0080480620V#070F哈哈，这么一来\n',
            '就严禁偷吃了哟。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080480621V做饭的时候\n',
            '要注意所使用的食材。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1265')

    def _loc_1176(): pass

    label('loc_1176')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_11EE',
    )

    ChrTalk(
        0x0103,
        (
            '#0030480622V#027F嗯嗯，只要某人\n',
            '不先偷吃就行了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030480623V做料理的时候\n',
            '要注意所使用的食材啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1265')

    def _loc_11EE(): pass

    label('loc_11EE')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1265',
    )

    ChrTalk(
        0x0106,
        (
            '#0050480624V#053F啊啊，只要某人\n',
            '不先偷吃就行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050480625V在外边做饭的时候\n',
            '要注意所使用的食材哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1265(): pass

    label('loc_1265')

    ChrTalk(
        0x0101,
        (
            '#0010480626V#1016F啊哈哈，这个确实……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480627V没有别的问题了？\n',
            '没有的话我就回去工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480628V#1015F嗯，取得食材的地方\n',
            '和交付方法都问了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480629V#1006F嗯，我想没问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480630V那就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480631V我就在这里等吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x007B, 0x01, 0x0001)
    OP_28(0x007B, 0x01, 0x0002)
    OP_28(0x007B, 0x01, 0x0004)
    OP_28(0x007B, 0x04, 0x04)
    OP_28(0x007B, 0x04, 0x08)
    EventEnd(0x00)
    OP_4B(0x000A, 255)
    TerminateThread(0x000A, 0x00)
    CreateThread(0x000A, 0x00, 0x00, 0x0002)

    Return()

# id: 0x0001 offset: 0x13A3
@scena.Code('func_01_13A3')
def func_01_13A3():
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
            TXT(0x00, '【说话】\n'),
            TXT(0x01, '【展示食材】\n'),
            TXT(0x02, '【离开】\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_140A',
    )

    Call(0, 0x0009)

    Return()

    def _loc_140A(): pass

    label('loc_140A')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_141C',
    )

    Call(2, 0x0002)

    Return()

    def _loc_141C(): pass

    label('loc_141C')

    Return()

# id: 0x0002 offset: 0x141D
@scena.Code('func_02_141D')
def func_02_141D():
    EventBegin(0x00)
    Fade(1000)
    OP_4A(0x000A, 255)
    ChrSetPos(0x000A, -47710, 0, 44840, 90)
    ChrSetPos(0x0101, -46020, 0, 44370, 270)
    ChrSetPos(0x00F7, -45610, 0, 45370, 270)
    ChrSetPos(0x00F8, -44250, 0, 45330, 270)
    ChrSetPos(0x00F9, -44580, 0, 44110, 270)

    If(
        (
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_149A',
    )

    ChrSetPos(0x0004, -43430, 0, 44650, 270)

    def _loc_149A(): pass

    label('loc_149A')

    CameraMove(-46490, 0, 45440, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(
        0x000A,
        (
            '#1350480632V哎呀，把食材\n',
            '拿来了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1538',
    )

    ChrTalk(
        0x0101,
        (
            '#0010480633V#1002F嗯，你确认一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1560')

    def _loc_1538(): pass

    label('loc_1538')

    ChrTalk(
        0x0101,
        (
            '#0010480634V#1006F嗯，你确认一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1560(): pass

    label('loc_1560')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '向格露娜展示了食材。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    If(
        (
            (Expr.Eval, "OP_29(0x007B, 0x01, 0x0008)"),
            Expr.Return,
        ),
        'loc_15D4',
    )

    If(
        (
            (Expr.Eval, "OP_40(0x03A7, 0x00)"),
            (Expr.PushLong, 0xA),
            Expr.Geq,
            (Expr.Eval, "OP_40(0x03A9, 0x00)"),
            (Expr.PushLong, 0xA),
            Expr.Geq,
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x03A2, 0x00)"),
            (Expr.PushLong, 0xA),
            Expr.Geq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_15D1',
    )

    Call(2, 0x0003)

    Return()

    def _loc_15D1(): pass

    label('loc_15D1')

    Jump('loc_1624')

    def _loc_15D4(): pass

    label('loc_15D4')

    If(
        (
            (Expr.Eval, "OP_40(0x03A7, 0x00)"),
            (Expr.PushLong, 0xA),
            Expr.Geq,
            (Expr.Eval, "OP_40(0x03A9, 0x00)"),
            (Expr.PushLong, 0xA),
            Expr.Geq,
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x03A2, 0x00)"),
            (Expr.PushLong, 0xA),
            Expr.Geq,
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x039E, 0x00)"),
            (Expr.PushLong, 0x5),
            Expr.Geq,
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x03A3, 0x00)"),
            (Expr.PushLong, 0x5),
            Expr.Geq,
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x03A1, 0x00)"),
            (Expr.PushLong, 0x5),
            Expr.Geq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1624',
    )

    Call(2, 0x0003)

    Return()

    def _loc_1624(): pass

    label('loc_1624')

    ChrTalk(
        0x000A,
        (
            '#1350480635V嗯～很抱歉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480636V食材好象没齐呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480637V#1004F啊，是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480638V嗯嗯，没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480639V再确认一次\n',
            '需要的食材吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480640V#1015F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480641V那下次再来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)
    OP_4B(0x000A, 255)
    TerminateThread(0x000A, 0x00)
    CreateThread(0x000A, 0x00, 0x00, 0x0002)

    Return()

# id: 0x0003 offset: 0x171F
@scena.Code('func_03_171F')
def func_03_171F():
    ChrTalk(
        0x000A,
        (
            '#1350480808V嗯……\n',
            '全部集齐了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480809V那么，\n',
            '我就收下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x007B, 0x01, 0x0008)"),
            Expr.Return,
        ),
        'loc_1809',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.Item, ItemTable['魔兽鸟肉']),
            (TxtCtl.SetColor, 0x0),
            '交付了１０个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.Item, ItemTable['魔兽眼珠']),
            (TxtCtl.SetColor, 0x0),
            '交付了１０个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.Item, ItemTable['魔兽鸟蛋']),
            (TxtCtl.SetColor, 0x0),
            '交付了１０个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(ItemTable['魔兽鸟肉'], 10)
    RemoveItem(ItemTable['魔兽眼珠'], 10)
    RemoveItem(ItemTable['魔兽鸟蛋'], 10)

    Jump('loc_18FC')

    def _loc_1809(): pass

    label('loc_1809')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.Item, ItemTable['魔兽之角']),
            (TxtCtl.SetColor, 0x0),
            '交付了５个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.Item, ItemTable['魔兽之牙']),
            (TxtCtl.SetColor, 0x0),
            '交付了５个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.Item, ItemTable['魔兽之骨']),
            (TxtCtl.SetColor, 0x0),
            '交付了５个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.Item, ItemTable['魔兽鸟肉']),
            (TxtCtl.SetColor, 0x0),
            '交付了１０个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.Item, ItemTable['魔兽眼珠']),
            (TxtCtl.SetColor, 0x0),
            '交付了１０个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.Item, ItemTable['魔兽鸟蛋']),
            (TxtCtl.SetColor, 0x0),
            '交付了１０个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(ItemTable['魔兽之角'], 5)
    RemoveItem(ItemTable['魔兽之牙'], 5)
    RemoveItem(ItemTable['魔兽之骨'], 5)
    RemoveItem(ItemTable['魔兽鸟肉'], 10)
    RemoveItem(ItemTable['魔兽眼珠'], 10)
    RemoveItem(ItemTable['魔兽鸟蛋'], 10)

    def _loc_18FC(): pass

    label('loc_18FC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1A93',
    )

    ChrTalk(
        0x0101,
        (
            '#0010480810V#1002F好，这样委托就完成了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480811V那，格露娜……\n',
            '不好意思，我们这就告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480812V看来好像很急呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480813V难道你们\n',
            '因为刚才那龙的事……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480814V#1002F嗯，有紧急的事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480815V是吗……\n',
            '那就不留你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480816V今天谢谢你们帮忙了。\n',
            '你们也要多加小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480817V#1006F谢谢了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480818V格露娜也加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C96')

    def _loc_1A93(): pass

    label('loc_1A93')

    ChrTalk(
        0x0101,
        (
            '#0010480819V#1007F呼～这样就完成委托了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480820V呵呵，辛苦辛苦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480821V百忙之中真是谢谢你们了。\n',
            '多亏你们帮了大忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x007B, 0x01, 0x0008)"),
            Expr.Return,
        ),
        'loc_1B64',
    )

    ChrTalk(
        0x000A,
        (
            '#1350480822V还连商人\n',
            '也顺便介绍过来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_2B(0x007B, 0x0002)
    OP_2C(0x007B, 0x05DC)

    def _loc_1B64(): pass

    label('loc_1B64')

    ChrTalk(
        0x0101,
        (
            '#0010480823V#1001F嘿嘿，别介意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480824V能帮上忙就再好不过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480825V如果有空\n',
            '请务必来我家做客。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480826V那，今后\n',
            '也请努力工作哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010480827V#1006F嗯，谢谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480818V格露娜也加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(23, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【美味的调制】',
            (TxtCtl.SetColor, 0x0),
            '完成了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    def _loc_1C96(): pass

    label('loc_1C96')

    OP_28(0x007B, 0x01, 0x0020)
    OP_28(0x007B, 0x04, 0x10)
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))
    EventEnd(0x00)
    OP_4B(0x000A, 255)
    TerminateThread(0x000A, 0x00)
    CreateThread(0x000A, 0x00, 0x00, 0x0002)

    Return()

# id: 0x0004 offset: 0x1CB9
@scena.Code('func_04_1CB9')
def func_04_1CB9():
    EventBegin(0x00)
    ChrClearFlags(0x0011, 0x0080)
    OP_4A(0x000A, 255)
    OP_4A(0x0011, 255)
    ChrSetPos(0x000A, -47710, 0, 44840, 90)
    ChrSetPos(0x0011, -46020, 0, 44840, 270)
    ChrSetPos(0x0101, -44910, 0, 44600, 270)
    ChrSetPos(0x00F7, -44680, 0, 45560, 270)
    ChrSetPos(0x00F8, -43250, 0, 45520, 270)
    ChrSetPos(0x00F9, -43450, 0, 44560, 270)

    If(
        (
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1D4B',
    )

    ChrSetPos(0x0004, -42250, 0, 45000, 270)

    def _loc_1D4B(): pass

    label('loc_1D4B')

    CameraMove(-46490, 0, 45440, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(
        0x000A,
        (
            '#1350480788V──嗯，品质也没有问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480789V那么，这里的食材\n',
            '我就先收下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '『魔兽之骨』，『魔兽之角』，\n',
            '『魔兽之牙』都交给了格露娜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#0010480790V#1000F呼，得救了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010480791V这下很麻烦的食材\n',
            '就全部收齐了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480792V嗯嗯，是呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480793V拜托你们找\n',
            '剩下的食材吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190892V#1006F嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480795V话虽如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480796V这么珍稀的食材\n',
            '竟然有库存呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#1070480797V哈哈哈，那当然啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1070480798V怎么说本商会可是\n',
            '专业出售高级食材的嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1070480799V跟那些普通的小食品店\n',
            '进的货品可不一样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1070480800V需要什么的时候，\n',
            '请再联络本商会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480801V一定会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480802V本来还想介绍给厨师长，\n',
            '但现在他比较忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480803V十分抱歉，\n',
            '能在这里稍等片刻吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#1070480804V好说好说，多长时间\n',
            '我都等。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1070480805V……那么，一会儿见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrWalkTo(0x0011, -46070, 0, 46360, 2000, 0x00)

    @scena.Lambda('lambda_2103')
    def lambda_2103():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_2103')

    DispatchAsync2(0x00F6, 0x0001, lambda_2103)

    @scena.Lambda('lambda_2114')
    def lambda_2114():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_2114')

    DispatchAsync2(0x00F7, 0x0001, lambda_2114)

    @scena.Lambda('lambda_2125')
    def lambda_2125():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_2125')

    DispatchAsync2(0x00F8, 0x0001, lambda_2125)

    @scena.Lambda('lambda_2136')
    def lambda_2136():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_2136')

    DispatchAsync2(0x00F9, 0x0001, lambda_2136)

    If(
        (
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_215E',
    )

    @scena.Lambda('lambda_2153')
    def lambda_2153():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_2153')

    DispatchAsync2(0x0004, 0x0001, lambda_2153)

    def _loc_215E(): pass

    label('loc_215E')

    ChrWalkTo(0x0011, -42330, 0, 46360, 2000, 0x00)
    ChrWalkTo(0x0011, -41230, 0, 45250, 2000, 0x00)
    ChrWalkTo(0x0011, -36660, 0, 44840, 2000, 0x00)
    TerminateThread(0x00F6, 0x01)
    TerminateThread(0x00F7, 0x01)
    TerminateThread(0x00F8, 0x01)
    TerminateThread(0x00F9, 0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_21BA',
    )

    TerminateThread(0x0004, 0x01)

    def _loc_21BA(): pass

    label('loc_21BA')

    ChrSetPos(0x0011, -33640, 0, 42550, 0)

    @scena.Lambda('lambda_21D1')
    def lambda_21D1():
        ChrSetDirection(0x00F6, 270, 400)

        ExitThread()

    DispatchAsync(0x00F6, 0x0001, lambda_21D1)

    @scena.Lambda('lambda_21DF')
    def lambda_21DF():
        ChrSetDirection(0x00F7, 270, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_21DF)

    Sleep(100)

    @scena.Lambda('lambda_21F2')
    def lambda_21F2():
        ChrSetDirection(0x00F8, 270, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_21F2)

    If(
        (
            (Expr.PushValueByIndex, 0xE),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2214',
    )

    @scena.Lambda('lambda_220C')
    def lambda_220C():
        ChrSetDirection(0x0004, 270, 400)

        ExitThread()

    DispatchAsync(0x0004, 0x0001, lambda_220C)

    def _loc_2214(): pass

    label('loc_2214')

    ChrSetDirection(0x00F9, 270, 400)

    ChrTalk(
        0x000A,
        (
            '#1350480806V好了，剩下的食材\n',
            '大多是简单的东西了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1350480807V那么各位，\n',
            '还需要再麻烦你们一下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x007B, 0x01, 0x0008)
    OP_28(0x007B, 0x01, 0x0010)
    EventEnd(0x00)
    OP_4B(0x000A, 255)
    TerminateThread(0x000A, 0x00)
    CreateThread(0x000A, 0x00, 0x00, 0x0002)
    OP_4B(0x0011, 255)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0110_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0110_1 ._SN')

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
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T0110_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '#3410470126V哎呀，是游击士们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3410470127V我家的鲁克\n',
            '终于醒来了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3410470128V已经完全恢复了呢。\n',
            '现在已经出去玩了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034D, 0, 0x1A68)),
            Expr.Return,
        ),
        'loc_1D4',
    )

    ChrTalk(
        0x0101,
        (
            '#0010470129V#1017F啊，嗯。\n',
            '已经见过他了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470130V真的比之前\n',
            '有精神多了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3410470131V现在反倒更担心\n',
            '会不会得意忘形反而受伤呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_281')

    def _loc_1D4(): pass

    label('loc_1D4')

    ChrTalk(
        0x0101,
        (
            '#0010470132V#1001F嘿嘿，太好了。\n',
            '这样就放心了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470133V待会儿我们\n',
            '也去看看他吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3410470134V啊啊，就这么办吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3410470135V那个孩子\n',
            '好像很喜欢你似的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_281(): pass

    label('loc_281')

    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#3410470136V话说回来，是不是\n',
            '有什么事才来的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470137V#1008F啊，您看出来了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470138V其实是\n',
            '向您询问一些事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3410470139V哎呀，是什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '诉说了在寻找拉欧老人\n',
            '所说的炖煮材理食谱的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x00FE,
        (
            '#3410470140V放了胡椒的炖煮料理啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3410470141V我确实吃过，\n',
            '不过没有做过哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3410470142V以前帮着父母做过，\n',
            '都是些简单的事嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470143V#1007F哎呀呀，是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0075, 0x01, 0x0800)"),
            Expr.Return,
        ),
        'loc_4AF',
    )

    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030470144V#020F总之\n',
            '先去报告那个食谱吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010470145V#1015F嗯，只有先这样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5A0')

    def _loc_4AF(): pass

    label('loc_4AF')

    If(
        (
            (Expr.Eval, "OP_29(0x0075, 0x01, 0x0400)"),
            Expr.Return,
        ),
        'loc_52F',
    )

    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030470146V#020F老老实实调查一下\n',
            '雷特拉先生家不好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010470147V#1015F嗯……或许是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5A0')

    def _loc_52F(): pass

    label('loc_52F')

    ChrTalk(
        0x0103,
        (
            '#0030470148V#020F……问问其他人\n',
            '可能比较好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0103, 400)

    ChrTalk(
        0x00FE,
        (
            '#3410470149V啊啊，不好意思…但也只能这么办了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5A0(): pass

    label('loc_5A0')

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))
    OP_28(0x0075, 0x01, 0x0010)

    Return()

# id: 0x0001 offset: 0x5AA
@scena.Code('func_01_5AA')
def func_01_5AA():
    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, 91960, 0, 162870, 90)
    ChrSetPos(0x00F7, 91150, 0, 162270, 90)
    ChrSetPos(0x00F8, 90480, 0, 163570, 90)
    ChrSetPos(0x00F9, 91330, 0, 164280, 135)
    ChrSetDirection(0x00FE, 270, 0)
    CameraMove(91870, 0, 163740, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_4A(0x00FE, 255)
    OP_0D()

    ChrTalk(
        0x00FE,
        (
            '#3580470331V啊，有什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470332V#1000F不，没什么\n',
            '特别重要的事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470333V……雷特拉先生\n',
            '好像有很多书吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3580470334V哼哼，这可是\n',
            '我自豪的收藏啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3580470335V对以收集古书为兴趣的我来说，\n',
            '这里就像是我的城堡一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470336V#1015F以收集古书为兴趣……吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470337V嗯～慎重起见，\n',
            '问问看吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030470338V#027F#1P嗯，我看\n',
            '有确认一下的价值哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3580470339V？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3580470340V你们说什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '传达了协会的工作，要寻找\n',
            '布露姆老奶奶的食谱册的事。',
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
            '#0010470341V#1011F──就是这么回事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470342V那个食谱册，\n',
            '雷特拉先生有吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3580470343V听说是老奶奶的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3580470344V啊啊，记得以前，\n',
            '她的确是送给我了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010470345V#1004F咦、真、真的吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3580470346V啊啊，因为是传统料理的食谱，\n',
            '所以她说想设法保存下来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3580470347V于是我就拜托老奶奶\n',
            '转手给我了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470348V#1011F原来是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A17',
    )

    ChrTalk(
        0x0107,
        (
            '#0070470349V#060F没错了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AEE')

    def _loc_A17(): pass

    label('loc_A17')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A4B',
    )

    ChrTalk(
        0x0105,
        (
            '#0060470350V#040F好像没错了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AEE')

    def _loc_A4B(): pass

    label('loc_A4B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A83',
    )

    ChrTalk(
        0x0108,
        (
            '#0080470351V#070F嗯，看来没错了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AEE')

    def _loc_A83(): pass

    label('loc_A83')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_ABB',
    )

    ChrTalk(
        0x0104,
        (
            '#0040470352V#030F呵，好像没错了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AEE')

    def _loc_ABB(): pass

    label('loc_ABB')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AEE',
    )

    ChrTalk(
        0x0106,
        (
            '#0050470353V#051F好像没错了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AEE(): pass

    label('loc_AEE')

    ChrTalk(
        0x0103,
        (
            '#0030470354V#021F#1P呵呵，看来\n',
            '终于找到目标了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030470355V那么，麻烦立刻\n',
            '拿给我们看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470356V#1000F……就是这样、\n',
            '麻烦您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3580470357V啊啊，小事一桩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3580470358V……话虽如此，\n',
            '其实放在哪里\n',
            '我也记不清了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3580470359V不好意思，\n',
            '你们自己去找找看吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3580470360V一定在这个房间里，\n',
            '我确定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470361V#1006F啊，嗯，明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470362V既然同意给我们看，\n',
            '这点小事当然自己做啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0075, 0x01, 0x0400)
    OP_65(0x00, 0x0001)
    EventEnd(0x00)

    Return()

# id: 0x0002 offset: 0xCA9
@scena.Code('func_02_CA9')
def func_02_CA9():
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '书架上有『布露姆老奶奶的食谱册』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
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
        10,
        1,
        (
            TXT(0x00, '【读书】\n'),
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
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E77',
    )

    OP_B8(0x0236, 0x0000)

    If(
        (
            (Expr.Eval, "OP_29(0x0075, 0x01, 0x0800)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E74',
    )

    Sleep(400)

    AddItem(ItemTable['料理抄本'], 1)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['料理抄本']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0101,
        (
            '#0010470363V#1028F好……\n',
            '做好笔记了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470364V#1007F说实话，完全不懂什么意思……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030470365V#020F算了，解读就交给专业人士吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030470366V必要的食材也知道了，\n',
            '赶快准备回去报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0075, 0x01, 0x0800)

    def _loc_E74(): pass

    label('loc_E74')

    Jump('loc_E77')

    def _loc_E77(): pass

    label('loc_E77')

    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

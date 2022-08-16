import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0200_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0200_1 ._SN')

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
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T0200_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
    ChrSetPos(0x0101, 7870, 0, -15950, 0)
    ChrSetPos(0x00F7, 6710, 0, -16560, 0)
    ChrSetPos(0x00F8, 7910, 0, -17100, 0)
    ChrSetPos(0x00F9, 8940, 0, -16500, 0)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_122',
    )

    ChrSetPos(0x00F9, 7910, 0, -17100, 0)
    ChrSetPos(0x00F8, 8940, 0, -16500, 0)

    def _loc_122(): pass

    label('loc_122')

    CameraMove(8740, 0, -14620, 0)
    OP_67(0, 8360, -10000, 0)
    CameraSetDistance(3250, 0)
    OP_6C(45000, 0)
    OP_6E(230, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010471153V#1002F#5P嗯，这些木箱的排列方式……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010471154V和卡片上的记号\n',
            '不是一模一样吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030471155V#020F#3P是啊，箱子的数量\n',
            '也正好是五个。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030471156V还是调查一下比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010471157V#1006F#5P嗯，那么马上……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0101, 7870, 0, -14600, 2000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010471158V#1028F#5P那么～到底\n',
            '是·在·哪·里·呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    ChrMoveTo(0x0101, 6860, 0, -14600, 2000, 0x00)
    Sleep(1500)

    ChrMoveTo(0x0101, 8530, 0, -14600, 2000, 0x00)
    Sleep(500)

    ChrMoveTo(0x0101, 7870, 0, -14600, 2000, 0x00)
    Sleep(1500)

    OP_63(0x0101)
    Sleep(500)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_63(0x0101)

    ChrTalk(
        0x0101,
        (
            '#0010471159V#1018F#5P有，有了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0348')
    def lambda_0348():
        ChrTurnDirection(0x00F7, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_0348)

    @scena.Lambda('lambda_0356')
    def lambda_0356():
        ChrTurnDirection(0x00F8, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_0356)

    @scena.Lambda('lambda_0364')
    def lambda_0364():
        ChrTurnDirection(0x00F9, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_0364)

    ChrSetDirection(0x0101, 180, 400)
    Fade(1000)
    ChrSetChipByIndex(0x0101, 6)
    OP_0D()
    Sleep(1000)

    FadeOut(300, 0, 100)
    OP_AD('ED6_DT24/C_VIS124._CH', 0x00BE, 0x0064, 0x000001F4)
    Sleep(1000)

    SetMessageWindowPos(-1, 300, -1, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0170471160V　\n',
            '　　第三把钥匙在市内。　　\n',
            '  在『八眼铁兽』的腹部寻找。\n',
            '　',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_AE(0x000001F4)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010471161V#1015F#5P──是这么\n',
            '写着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030471162V#022F#3P『八眼铁兽』啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030471163V好象是在洛连特市内，\n',
            '不过到底是什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_52D',
    )

    ChrTalk(
        0x0104,
        (
            '#0040471164V#034F呼，看来还是只有\n',
            '四处走动走动继续调查了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040471165V不管怎样都得早点找到钥匙，\n',
            '那样才能放松下来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6B4')

    def _loc_52D(): pass

    label('loc_52D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5AF',
    )

    ChrTalk(
        0x0108,
        (
            '#0080471168V#070F就和以前一样，只好\n',
            '四处走动走动继续调查了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080471169V虽然是麻烦，\n',
            '但这时候更要加油啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6B4')

    def _loc_5AF(): pass

    label('loc_5AF')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_627',
    )

    ChrTalk(
        0x0106,
        (
            '#0050471171V#050F就和以前一样，只好\n',
            '四处走动走动继续调查了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050471172V别磨磨蹭蹭了\n',
            '赶快去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6B4')

    def _loc_627(): pass

    label('loc_627')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6B4',
    )

    ChrTalk(
        0x0105,
        (
            '#0060471174V#040F看来还是只能和以前一样\n',
            '四处走动走动继续调查了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060471175V一定就差最后一口气了，\n',
            '就努力再坚持一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6B4(): pass

    label('loc_6B4')

    Sleep(500)

    Fade(1000)
    ChrSetChipByIndex(0x0101, 65535)
    OP_0D()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_72A',
    )

    ChrTalk(
        0x0101,
        (
            '#0010471166V#1016F#5P啊哈哈，我也是这么想的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010471167V#1006F那么就走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7DC')

    def _loc_72A(): pass

    label('loc_72A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_76D',
    )

    ChrTalk(
        0x0101,
        (
            '#0010471170V#1006F#5P嗯，明白。\n',
            '那么就走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7DC')

    def _loc_76D(): pass

    label('loc_76D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7A3',
    )

    ChrTalk(
        0x0101,
        (
            '#0010471173V#1006F#5P嗯，走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7DC')

    def _loc_7A3(): pass

    label('loc_7A3')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7DC',
    )

    ChrTalk(
        0x0101,
        (
            '#0010471176V#1006F#5P嗯，那么出发吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7DC(): pass

    label('loc_7DC')

    OP_28(0x0077, 0x01, 0x0020)
    OP_64(0x00, 0x0001)
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T0121_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0121_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0121.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
    )

# id: 0x10000 offset: 0x64
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
    ]

# id: 0x10001 offset: 0x64
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10002 offset: 0x64
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x64
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x64
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x64
@scena.Code('Init')
def Init():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D9',
    )

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '真是的，开什么玩笑。\n',
            '什么商品都缺货！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可恶，在下次谈判之前\n',
            '必须发掘些超热门产品才行啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10C')

    def _loc_D9(): pass

    label('loc_D9')

    ChrTalk(
        0x00FE,
        (
            '在下次谈判之前\n',
            '必须发掘些超热门产品才行啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10C(): pass

    label('loc_10C')

    TalkEnd(0x000E)

    Return()

# id: 0x0001 offset: 0x110
@scena.Code('func_01_110')
def func_01_110():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_12F',
    )

    OP_2A(0x0004, 0x0005, 0x0006, 0x0007, 0x0008, 0x0009, 0x000B, 0x000C, 0x000D, 0xFFFF)

    Jump('loc_24F')

    def _loc_12F(): pass

    label('loc_12F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_14C',
    )

    OP_2A(0x0004, 0x0005, 0x0006, 0x0007, 0x0008, 0x0009, 0x000B, 0x000C, 0xFFFF)

    Jump('loc_24F')

    def _loc_14C(): pass

    label('loc_14C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 2, 0x252)),
            Expr.Return,
        ),
        'loc_169',
    )

    OP_2A(0x0004, 0x0005, 0x0006, 0x0007, 0x0008, 0x0009, 0x000B, 0x000C, 0xFFFF)

    Jump('loc_24F')

    def _loc_169(): pass

    label('loc_169')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_186',
    )

    OP_2A(0x0004, 0x0005, 0x0006, 0x0007, 0x0008, 0x0009, 0x000B, 0x000C, 0xFFFF)

    Jump('loc_24F')

    def _loc_186(): pass

    label('loc_186')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 2, 0x23A)),
            Expr.Return,
        ),
        'loc_19F',
    )

    OP_2A(0x0004, 0x0005, 0x0006, 0x0007, 0x0008, 0x000B, 0xFFFF)

    Jump('loc_24F')

    def _loc_19F(): pass

    label('loc_19F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_1B8',
    )

    OP_2A(0x0004, 0x0005, 0x0006, 0x0007, 0x0008, 0x000B, 0xFFFF)

    Jump('loc_24F')

    def _loc_1B8(): pass

    label('loc_1B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_1C9',
    )

    OP_2A(0x0004, 0x000B, 0xFFFF)

    Jump('loc_24F')

    def _loc_1C9(): pass

    label('loc_1C9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0041, 4, 0x20C)),
            Expr.Return,
        ),
        'loc_211',
    )

    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '现在没有什么特别的委托。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    Jump('loc_24F')

    def _loc_211(): pass

    label('loc_211')

    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '现在没有什么特别的委托。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    def _loc_24F(): pass

    label('loc_24F')

    TalkEnd(0x00FF)

    Return()

# id: 0x0002 offset: 0x253
@scena.Code('func_02_253')
def func_02_253():
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0045, 7, 0x22F)),
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_658',
    )

    Sleep(100)

    OP_AF(0x04, 0x000A)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    EventBegin(0x00)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0350000634V#741F辛苦了。\n',
            '看来你们很顺利地完成了任务呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350000635V#741F有时工作中的具体表现\n',
            '也会影响到最后所得的报酬，\n',
            '这点你们俩一定要注意哦。 ',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350000636V#740F报告之后，不仅会得到米拉，\n',
            '而且会为自己加算一种叫做ＢＰ的点数。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350000637VＢＰ是游击士点数的缩写，\n',
            '是用来衡量游击士实绩的数据。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350000638V这个点数达到一定值数的话，\n',
            '你们的游击士等级就能提升，\n',
            '同时也会得到协会奖励的特别物品。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350000639V准游击士一共分为９个等级，\n',
            '９级是初始等级，１级是最高等级。\n',
            '为了达到１级，你们俩要好好加油哦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350000640V#740F工作中实际获得的米拉和ＢＰ\n',
            '在游击士手册中都有记录，\n',
            '完成任务之后可以确认一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030000641V#020F这样的话，\n',
            '剩下的就是例行的仪式了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000642V你们两个，\n',
            '先跟我回到二楼再说吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030000643V回头见，爱娜。\n',
            '这么忙还要麻烦你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350000644V#741F呵呵，没关系。\n',
            '这是为了培养新生的战斗力嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350000645V以后还要靠他们\n',
            '上刀山、下火海呢，呵呵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000646V#008F上、上刀山……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000647V#019F……还是先做好心里准备吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(500, 0, -1)
    OP_0D()
    Call(0, 0x0017)

    Jump('loc_764')

    def _loc_658(): pass

    label('loc_658')

    If(
        (
            (Expr.Eval, "OP_A9(0x04)"),
            Expr.Return,
        ),
        'loc_6E2',
    )

    Sleep(200)

    ChrTalk(
        0x0008,
        (
            '#0350000648V#740F辛苦了。\n',
            '看来你们很顺利地完成了任务呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350000649V如果完成其他任务的话，\n',
            '别忘记回协会报告一下哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_764')

    def _loc_6E2(): pass

    label('loc_6E2')

    Sleep(200)

    ChrTalk(
        0x0008,
        (
            '#0350000650V#740F哎呀，\n',
            '现在好像没有需要报告的工作任务呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350000651V如果完成其他任务的话，\n',
            '别忘记回协会报告一下哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_764(): pass

    label('loc_764')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import R2202_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R2202_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'R2202.x'
    header.mapIndex       = 101
    header.bgm            = 20
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
    EventBegin(0x00)
    OP_64(0x00, 0x0001)
    Fade(1000)
    OP_6C(90000, 0)
    OP_69(0x0101, 0)
    OP_0D()
    Sleep(800)

    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '骷髅刀',
            (TxtCtl.SetColor, 0x0),
            '和',
            (TxtCtl.SetColor, 0x2),
            '古海图的残片',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(0x0335, 1)
    AddItem(0x002D, 1)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010160911V#501F咦～好酷的短剑啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020160912V#010F看上去是相当古老的东西呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020160913V从使用的材质来看，\n',
            '也许是导力革命以前的东西呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010160914V#000F对了，\n',
            '那个像是碎纸片的东西是什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020160915V#010F好像是航海图的碎片。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x001E, 0x00, 0x04)"),
            Expr.Return,
        ),
        'loc_401',
    )

    OP_28(0x001E, 0x01, 0x0010)
    OP_62(0x0101, 0x00000000, 2000, 0x22, 0x24, 0x000000FA, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010160916V#004F等一下…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160917V吉米先生所说的财宝\n',
            '难道就是指这个？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020160918V#010F很遗憾，\n',
            '两者恐怕毫无联系。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020160919V#010F这些应该都是从什么地方\n',
            '飘流过来的东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020160920V可能是遇难船只上面的货物吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_38F',
    )

    ChrTurnDirection(0x0105, 0x0102, 400)

    ChrTalk(
        0x0105,
        (
            '#0060160921V#040F嗯，我想也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060160922V听说以前这类的\n',
            '海上事故很多呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    Jump('loc_3FE')

    def _loc_38F(): pass

    label('loc_38F')

    If(
        (
            (Expr.Eval, "OP_42(0x0035)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_3FE',
    )

    ChrTurnDirection(0x0136, 0x0102, 400)

    ChrTalk(
        0x0136,
        (
            '#0060160921V#040F嗯，我想也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060160922V听说以前这类的\n',
            '海上事故很多呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0136, 400)

    def _loc_3FE(): pass

    label('loc_3FE')

    Jump('loc_407')

    def _loc_401(): pass

    label('loc_401')

    OP_28(0x001E, 0x01, 0x4000)
    def _loc_407(): pass

    label('loc_407')

    ChrTalk(
        0x0101,
        (
            '#0010160925V#505F对啊，在还没有飞艇的时候，\n',
            '大家都是用船运东西的呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160926V这里的海岸过去\n',
            '也是货船途径的通道吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)

    Return()

# id: 0x0001 offset: 0x487
@scena.Code('func_01_487')
def func_01_487():
    If(
        (
            (Expr.Eval, "OP_29(0x001D, 0x00, 0x08)"),
            (Expr.Eval, "OP_40(0x0326)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_60D',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_551',
    )

    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060160513V#040F往这边走就到王立学院了……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060160514V你们的工作不要紧吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010160515V#000F啊，对了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010160516V要赶快把工作先做完。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5EF')

    def _loc_551(): pass

    label('loc_551')

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020160517V#010F这边是通往王立学院的街景林道吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020160518V在去学院之前\n',
            '还是先把手头的工作做完吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010160519V#000F啊，没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5EF(): pass

    label('loc_5EF')

    ChrMoveToRelative(0x0000, -1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_6C1')

    def _loc_60D(): pass

    label('loc_60D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            (Expr.TestScenaFlags, ScenaFlag(0x0088, 2, 0x442)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6C1',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_631',
    )

    ChrTurnDirection(0x0102, 0x0001, 400)

    Jump('loc_638')

    def _loc_631(): pass

    label('loc_631')

    ChrTurnDirection(0x0102, 0x0000, 400)

    def _loc_638(): pass

    label('loc_638')

    ChrTalk(
        0x0102,
        (
            '#0020160520V#012F这边是王立学院。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020160521V我们要赶快去市长官邸…………\n',
            '在王国军来之前尽量拖延时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, -1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_6C1(): pass

    label('loc_6C1')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

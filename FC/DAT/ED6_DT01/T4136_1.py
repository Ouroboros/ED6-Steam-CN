import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4136_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4136_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4136.x'
    header.mapIndex       = 1
    header.bgm            = 18
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
    Return()

# id: 0x0001 offset: 0x65
@scena.Code('func_01_65')
def func_01_65():
    Return()

# id: 0x0002 offset: 0x66
@scena.Code('func_02_66')
def func_02_66():
    TalkBegin(0x00FE)
    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 5, 0x61D)),
            Expr.Return,
        ),
        'loc_A5',
    )

    ChrTalk(
        0x00FE,
        (
            '突击骑兵队被打败了吗。\n',
            '游击士干得不错嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CE')

    def _loc_A5(): pass

    label('loc_A5')

    ChrTalk(
        0x00FE,
        (
            '不管对手是谁，\n',
            '我一定会全力战斗的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CE(): pass

    label('loc_CE')

    Call(0, 0x0017)
    TalkEnd(0x00FE)

    Return()

# id: 0x0003 offset: 0xD6
@scena.Code('func_03_D6')
def func_03_D6():
    TalkBegin(0x00FE)
    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 5, 0x61D)),
            Expr.Return,
        ),
        'loc_127',
    )

    ChrTalk(
        0x00FE,
        (
            '今年游击士的小组\n',
            '还剩下两组。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管怎么样，互相加油吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_172')

    def _loc_127(): pass

    label('loc_127')

    ChrTalk(
        0x00FE,
        (
            '一会儿就轮到我们出场了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正好趁这个机会\n',
            '检验一下平时训练的成果。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_172(): pass

    label('loc_172')

    Call(0, 0x0017)
    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x17A
@scena.Code('func_04_17A')
def func_04_17A():
    TalkBegin(0x00FE)
    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 5, 0x61D)),
            Expr.Return,
        ),
        'loc_1EA',
    )

    ChrTalk(
        0x00FE,
        (
            '『渡鸦帮』那些家伙们\n',
            '打得不错啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '游击士以外的平民小组\n',
            '在正式比赛中出场还真是少见呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_204')

    def _loc_1EA(): pass

    label('loc_1EA')

    ChrTalk(
        0x00FE,
        (
            '还没轮到我们出场吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_204(): pass

    label('loc_204')

    Call(0, 0x0017)
    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x20C
@scena.Code('func_05_20C')
def func_05_20C():
    TalkBegin(0x00FE)
    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 5, 0x61D)),
            Expr.Return,
        ),
        'loc_272',
    )

    ChrTalk(
        0x00FE,
        (
            '你们的战斗在王国军中\n',
            '得到了很高的评价呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天也要仔细地\n',
            '观摩你们的比赛啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2AD')

    def _loc_272(): pass

    label('loc_272')

    ChrTalk(
        0x00FE,
        (
            '摩尔根将军不能参赛，\n',
            '我们一定要连他的那份一起加油啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2AD(): pass

    label('loc_2AD')

    Call(0, 0x0017)
    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x2B5
@scena.Code('func_06_2B5')
def func_06_2B5():
    TalkBegin(0x00FE)
    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 5, 0x61D)),
            Expr.Return,
        ),
        'loc_2EE',
    )

    ChrTalk(
        0x00FE,
        (
            '唔，我们的对手\n',
            '说不定是那些家伙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_339')

    def _loc_2EE(): pass

    label('loc_2EE')

    ChrTalk(
        0x00FE,
        (
            '我们国境守卫队是精锐部队。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管对手是谁，\n',
            '也绝对不能轻易地输掉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_339(): pass

    label('loc_339')

    Call(0, 0x0017)
    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x341
@scena.Code('func_07_341')
def func_07_341():
    TalkBegin(0x00FE)
    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 5, 0x61D)),
            Expr.Return,
        ),
        'loc_37C',
    )

    ChrTalk(
        0x00FE,
        (
            '接下来轮到你们了呢。\n',
            '祝你们取得胜利。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E5')

    def _loc_37C(): pass

    label('loc_37C')

    ChrTalk(
        0x00FE,
        (
            '通过这次武术大会，\n',
            '就能了解到其他的部队\n',
            '和你们游击士的水平了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对我们来说\n',
            '也有很好的促进作用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3E5(): pass

    label('loc_3E5')

    Call(0, 0x0017)
    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x3ED
@scena.Code('func_08_3ED')
def func_08_3ED():
    TalkBegin(0x00FE)
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 5, 0x61D)),
            Expr.Return,
        ),
        'loc_42E',
    )

    ChrTalk(
        0x00FE,
        (
            '身体状态非常不错，\n',
            '今年应该能取得好成绩吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_455')

    def _loc_42E(): pass

    label('loc_42E')

    ChrTalk(
        0x00FE,
        (
            '请不要打扰。\n',
            '我现在正在集中精神。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_455(): pass

    label('loc_455')

    Call(0, 0x0017)
    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x45D
@scena.Code('func_09_45D')
def func_09_45D():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 5, 0x61D)),
            Expr.Return,
        ),
        'loc_499',
    )

    ChrTalk(
        0x00FE,
        (
            '为了不留下遗憾，\n',
            '一定要尽全力战斗到最后。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_542')

    def _loc_499(): pass

    label('loc_499')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_4E6',
    )

    ChrTalk(
        0x00FE,
        (
            '唔，虽然年轻，\n',
            '但是看起来很厉害的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天一起奋战吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_542')

    def _loc_4E6(): pass

    label('loc_4E6')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '你们是游击士吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔，虽然年轻，\n',
            '但是看起来很厉害的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天一起奋战吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_542(): pass

    label('loc_542')

    Call(0, 0x0017)
    TalkEnd(0x00FE)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

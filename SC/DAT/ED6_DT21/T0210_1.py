import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0210_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0210_1 ._SN')

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
    header.importTable    = ['ED6_DT21/T0210._SN', 'ED6_DT21/T0210_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x5BA
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
    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x0101,
        (
            '#0010470215V#1011F啊、米蕾奴阿姨。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470216V我能问你一件事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1020470217V哎呀，什么事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '诉说了在寻找拉欧老人\n',
            '所说的炖煮料理食谱的事。',
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
            '#1020470218V哦，是炖煮料理……呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030470219V#020F难不成您\n',
            '知道那个食谱？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0103, 400)

    ChrTalk(
        0x00FE,
        (
            '#1020470220V真不凑巧。\n',
            '我并不是那么精通料理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1020470221V应该是吃过，\n',
            '但是做法就完全不知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470222V#1007F呼～还是不行吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0075, 0x01, 0x0800)"),
            Expr.Return,
        ),
        'loc_2D1',
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

    Jump('loc_5AE')

    def _loc_2D1(): pass

    label('loc_2D1')

    If(
        (
            (Expr.Eval, "OP_29(0x0075, 0x01, 0x0400)"),
            Expr.Return,
        ),
        'loc_34D',
    )

    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030470146V#020F看来还是得\n',
            '调查雷特拉先生家了吧？',
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

    Jump('loc_5AE')

    def _loc_34D(): pass

    label('loc_34D')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_38E',
    )

    ChrTalk(
        0x0107,
        (
            '#0070470227V#063F嗯～怎么也\n',
            '找不到线索呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_442')

    def _loc_38E(): pass

    label('loc_38E')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3C9',
    )

    ChrTalk(
        0x0105,
        (
            '#0060470228V#043F好难找到\n',
            '线索呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_442')

    def _loc_3C9(): pass

    label('loc_3C9')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_406',
    )

    ChrTalk(
        0x0104,
        (
            '#0040470229V#032F唔，很难\n',
            '找到线索呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_442')

    def _loc_406(): pass

    label('loc_406')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_442',
    )

    ChrTalk(
        0x0108,
        (
            '#0080470230V#075F唔，调查\n',
            '没什么进展啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_442(): pass

    label('loc_442')

    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030470231V#020F唉，着急也不是办法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030470232V还是得坚持下去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470233V#1006F嗯……\n',
            '放弃就前功尽弃了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470234V阿姨，也谢谢您帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1020470235V哪里，别客气了。\n',
            '我也没帮上什么嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1020470236V你们一直工作真是很辛苦，\n',
            '要好好努力哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190634V#1006F嗯，明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x00FE, 400)

    ChrTalk(
        0x0103,
        (
            '#0030470238V#020F那么，我们告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5AE(): pass

    label('loc_5AE')

    OP_A2(0x0006)
    OP_28(0x0075, 0x01, 0x0040)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0120_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0120_1 ._SN')

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
    header.importTable    = ['ED6_DT21/T0120._SN', 'ED6_DT21/T0120_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x502
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
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_130',
    )

    ChrTalk(
        0x0101,
        (
            '#0010470150V#1011F啊，对了阿姨。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470151V其实是有点事…\n',
            '想向你询问一些事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#3690470152V咦？想问的事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C3')

    def _loc_130(): pass

    label('loc_130')

    ChrTalk(
        0x0101,
        (
            '#0010470153V#1011F啊、斯蒂娜阿姨。\n',
            '问您件事行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#3690470154V哎呀，怎么了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470155V#1000F嗯，其实想向您打听\n',
            '一些事情…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C3(): pass

    label('loc_1C3')

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
        0x0103,
        (
            '#0030470156V#020F──大概就是这样的，\n',
            '这个料理有印象吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0103, 400)

    ChrTalk(
        0x00FE,
        (
            '#3690470157V嗯～小的时候\n',
            '的确吃过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3690470158V很可惜，详细的食谱\n',
            '我也没听说过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470159V#1020F咦～怎么会……\n',
            '连阿姨也不知道吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#3690470160V一般的食谱我是知道的，\n',
            '但不知道那个料理哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3690470161V说不定是只在\n',
            '洛连特流传的乡土料理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470162V#1007F呼，是吗～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0075, 0x01, 0x0800)"),
            Expr.Return,
        ),
        'loc_39F',
    )

    Jump('loc_3DA')

    def _loc_39F(): pass

    label('loc_39F')

    If(
        (
            (Expr.Eval, "OP_29(0x0075, 0x01, 0x0400)"),
            Expr.Return,
        ),
        'loc_3AD',
    )

    Jump('loc_3DA')

    def _loc_3AD(): pass

    label('loc_3AD')

    ChrTalk(
        0x0103,
        (
            '#0030470163V#025F……比想象的更麻烦呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3DA(): pass

    label('loc_3DA')

    ChrTalk(
        0x00FE,
        (
            '#3690470164V抱歉，帮不上忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3690470165V但是，艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3690470166V别老是顾着工作，\n',
            '不好好休息可不行哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470167V#1016F啊哈哈……我会注意的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0103, 400)

    ChrTalk(
        0x00FE,
        (
            '#3690470168V雪拉也是，\n',
            '要多注意点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030470169V#021F嗯嗯，我知道的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030470170V那么，失陪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)
    OP_28(0x0075, 0x01, 0x0020)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

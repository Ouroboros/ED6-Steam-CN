import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0122_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0122_1 ._SN')

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
    header.importTable    = ['ED6_DT21/T0122._SN', 'ED6_DT21/T0122_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
    ChrSetDirection(0x00FE, 180, 0)
    Fade(1000)
    ChrSetPos(0x0101, -40360, 0, -4070, 270)
    ChrSetPos(0x0103, -39740, 0, -4770, 270)
    ChrSetPos(0x00F8, -38890, 0, -3380, 270)
    ChrSetPos(0x00F9, -38350, 0, -4310, 270)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_129',
    )

    ChrSetPos(0x00F9, -38890, 0, -3380, 270)
    ChrSetPos(0x00F8, -38350, 0, -4310, 270)

    def _loc_129(): pass

    label('loc_129')

    CameraMove(-39690, 0, -3410, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(
        0x00FE,
        (
            '#3330461112V哼哼哼哼～⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3330461113V嘿嘿，偶尔好好\n',
            '买些东西也不坏啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010461114V#1000F#1P对不起，我能问个问题吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010461115V你是定期船的操舵手\n',
            '库因特先生吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#3330461116V咦？\n',
            '嗯，是的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3330461117V……有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010461118V#1002F#1P嗯，有点事想要问你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '向他说明了正在寻找\n',
            '褐色猫的事。',
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
            '#3330461119V哟，你们在找迷路猫啊？\n',
            '在雾起得这么厉害的夜晚，真不容易。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3330461120V不过很遗憾……\n',
            '我没看见过那只猫。',
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
            '#0010461121V#1004F#1P啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030461122V#023F#4P……你没看见？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3330461123V嗯，我向空之女神发誓\n',
            '我没看见过猫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3330461124V我只是从别人\n',
            '那里听说的。',
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
        'loc_457',
    )

    ChrTalk(
        0x0106,
        (
            '#0050461125V#052F是从谁那里听说的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_513')

    def _loc_457(): pass

    label('loc_457')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_495',
    )

    ChrTalk(
        0x0108,
        (
            '#0080461126V#073F哦？是从谁那里听说的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_513')

    def _loc_495(): pass

    label('loc_495')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4D3',
    )

    ChrTalk(
        0x0104,
        (
            '#0040461127V#033F哦？是从谁那里听说的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_513')

    def _loc_4D3(): pass

    label('loc_4D3')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_513',
    )

    ChrTalk(
        0x0105,
        (
            '#0060461128V#040F那个……\n',
            '是从谁那里听说的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_513(): pass

    label('loc_513')

    ChrTalk(
        0x00FE,
        (
            '#3330461129V是一同乘船的索斯摩夫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3330461130V记得他说是在\n',
            '飞船坪工作时看到的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3330461131V详细情况你们去问他本人吧。\n',
            '他应该还在飞船坪工作着呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010461132V#1015F#1P飞船坪的索斯摩夫先生吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010461133V#1007F哈哈……\n',
            '结果又绕回去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030461134V#025F反正就在附近。\n',
            '与其发牢骚还不如赶快去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030461135V#020F好了，我们回飞船坪吧。',
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
        'loc_6B0',
    )

    ChrTalk(
        0x0107,
        (
            '#0070461136V#060F嗯，走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_757')

    def _loc_6B0(): pass

    label('loc_6B0')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6EA',
    )

    ChrTalk(
        0x0105,
        (
            '#0060461137V#040F嗯，那我们就走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_757')

    def _loc_6EA(): pass

    label('loc_6EA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_720',
    )

    ChrTalk(
        0x0104,
        (
            '#0040461138V#030F呼，那就走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_757')

    def _loc_720(): pass

    label('loc_720')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_757',
    )

    ChrTalk(
        0x0108,
        (
            '#0080461139V#070F好，那我们就走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_757(): pass

    label('loc_757')

    OP_28(0x0074, 0x01, 0x0040)
    OP_28(0x0074, 0x01, 0x0080)
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T3118_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3118_1 ._SN')

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
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T3118_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
    If(
        (
            (Expr.PushValueByIndex, 0x13),
            (Expr.PushLong, 0x382),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B5',
    )

    Return()

    def _loc_B5(): pass

    label('loc_B5')

    ExecExpressionWithReg(
        0x0006,
        (
            (Expr.PushLong, 0xE4E5A8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0007,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "OP_29(0x006F, 0x01, 0x0400)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_146',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.GetChrWork, 0x9, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0004,
        (
            (Expr.PushReg, 0x3),
            (Expr.PushReg, 0x2),
            Expr.Sub,
            (Expr.PushReg, 0x3),
            (Expr.PushReg, 0x2),
            Expr.Sub,
            Expr.Mul,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.GetChrWork, 0x9, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0005,
        (
            (Expr.PushReg, 0x3),
            (Expr.PushReg, 0x2),
            Expr.Sub,
            (Expr.PushReg, 0x3),
            (Expr.PushReg, 0x2),
            Expr.Sub,
            Expr.Mul,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushReg, 0x4),
            (Expr.PushReg, 0x5),
            Expr.Add,
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_146',
    )

    ExecExpressionWithReg(
        0x0006,
        (
            (Expr.PushReg, 0x4),
            (Expr.PushReg, 0x5),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0007,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_146(): pass

    label('loc_146')

    MapSetFlags(0x00000080)
    OP_C0(0x01, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    Sleep(30)

    LoadEffect(0x00, 'map\\\\mp108_00.eff')
    PlayEffect(0x00, 0x00, 0x0000, 0, 0, 0, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    Sleep(600)

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0xF4240),
            Expr.Leq,
            (Expr.PushReg, 0x7),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_22B',
    )

    EventBegin(0x01)
    OP_4A(0x0009, 1)
    ChrTurnDirection(0x0000, 0x0009, 400)
    OP_62(0x0000, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    OP_63(0x0000)
    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_63(0x0000)
    Call(1, 0x0002)
    EventEnd(0x01)

    Jump('loc_301')

    def _loc_22B(): pass

    label('loc_22B')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x4C4B40),
            Expr.Leq,
            Expr.Return,
        ),
        'loc_27B',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '这附近有反应！',
            TxtCtl.Enter,
        ),
    )

    PlaySE(170, 0x00, 0x64)
    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    Jump('loc_301')

    def _loc_27B(): pass

    label('loc_27B')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x989680),
            Expr.Leq,
            Expr.Return,
        ),
        'loc_2C7',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '附近有反应',
            TxtCtl.Enter,
        ),
    )

    PlaySE(170, 0x00, 0x64)
    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    Jump('loc_301')

    def _loc_2C7(): pass

    label('loc_2C7')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '没有反应',
            TxtCtl.Enter,
        ),
    )

    PlaySE(171, 0x00, 0x64)
    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    def _loc_301(): pass

    label('loc_301')

    OP_0D()
    MapClearFlags(0x00000080)

    Return()

# id: 0x0001 offset: 0x308
@scena.Code('func_01_308')
def func_01_308():
    Call(1, 0x0002)

    Return()

# id: 0x0002 offset: 0x30D
@scena.Code('func_02_30D')
def func_02_30D():
    EventBegin(0x00)
    OP_4A(0x000A, 255)
    Fade(1000)
    TerminateThread(0x0009, 0x00)
    ChrSetPos(0x0009, -5510, 0, -3140, 45)
    ChrSetPos(0x0101, -4640, 0, -2300, 225)
    ChrSetPos(0x00F7, -5400, 0, -1160, 180)
    ChrSetPos(0x00F8, -4170, 0, -1020, 225)
    ChrSetPos(0x00F9, -3520, 0, -2690, 270)
    CameraMove(-5020, 0, -2650, 0)
    OP_67(0, 5050, -10000, 0)
    CameraSetDistance(2870, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()
    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['导力器零件']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['导力器零件'], 1)
    OP_28(0x006F, 0x01, 0x0400)
    OP_64(0x00, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010450366V#1007F#5P真、真是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450367V没想到安东尼\n',
            '居然拿着零件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_47F',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450368V#051F#1P差点就放过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4A9')

    def _loc_47F(): pass

    label('loc_47F')

    ChrTalk(
        0x0103,
        (
            '#0030450369V#020F#1P差点就放过了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4A9(): pass

    label('loc_4A9')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_53A',
    )

    ChrTalk(
        0x0107,
        (
            '#0070450370V#560F#1P这么说来，埃里克先生\n',
            '他说过和它一起玩过呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070450371V它一定是那时候发现了零件\n',
            '然后拿到这里来了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_63B')

    def _loc_53A(): pass

    label('loc_53A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5B8',
    )

    ChrTalk(
        0x0104,
        (
            '#0040450372V#030F这么说来，委托人也\n',
            '说和它一起玩过吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040450373V是那时候发现了零件\n',
            '拿到这里来的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_63B')

    def _loc_5B8(): pass

    label('loc_5B8')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_63B',
    )

    ChrTalk(
        0x0105,
        (
            '#0060450374V#040F这么说来，埃里克先生也\n',
            '说和它一起玩过吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060450375V是那时候发现了零件\n',
            '然后拿到这里来了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_63B(): pass

    label('loc_63B')

    ChrTalk(
        0x0101,
        (
            '#0010450376V#1015F我想是吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450377V#1016F不过，没想到\n',
            '会拿过来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(402, 0x00, 0x64)

    ChrTalk(
        0x000A,
        (
            '#2030450378V喵呜？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_70C',
    )

    ChrTalk(
        0x0108,
        (
            '#0080450379V#071F哈哈，抱歉抱歉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080450380V把你的玩具拿走\n',
            '你也很为难吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7D5')

    def _loc_70C(): pass

    label('loc_70C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_76D',
    )

    ChrTalk(
        0x0105,
        (
            '#0060450381V#041F呵呵，对不起哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060450382V难得有了件玩具\n',
            '也被拿走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7D5')

    def _loc_76D(): pass

    label('loc_76D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7D5',
    )

    ChrTalk(
        0x0104,
        (
            '#0040450383V#031F呼，对不起啊小猫咪。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040450384V虽然是你的玩具\n',
            '就暂且借用一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7D5(): pass

    label('loc_7D5')

    ChrTalk(
        0x0101,
        (
            '#0010450385V#1006F嗯，这个补偿\n',
            '就让埃里克先生来做吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450386V那再见哦，安东尼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(402, 0x00, 0x64)

    ChrTalk(
        0x000A,
        (
            '#2030450387V喵～呜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)
    CreateThread(0x0009, 0x00, 0x00, 0x0002)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

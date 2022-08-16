import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import E0002_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('E0002   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'event'
    header.mapModel       = 'E0002.x'
    header.mapIndex       = 232
    header.bgm            = 1
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
            dword_04        = 0x00000FA0,
            dword_08        = 0xFFFFEE6C,
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
            word_3A         = 232,
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
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_B6',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_02_105)

    def _loc_B6(): pass

    label('loc_B6')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000068, 'loc_CA'),
        (0x00000067, 'loc_CA'),
        (0x00000066, 'loc_CA'),
        (-1, 'loc_DD'),
    )

    def _loc_CA(): pass

    label('loc_CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AC, 2, 0x562)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00B9, 4, 0x5CC)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_DA',
    )

    Event(0, func_04_231)

    def _loc_DA(): pass

    label('loc_DA')

    Jump('loc_DD')

    def _loc_DD(): pass

    label('loc_DD')

    Return()

# id: 0x0001 offset: 0xDE
@scena.Code('func_01_DE')
def func_01_DE():
    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x64),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_EF',
    )

    PlaySE(121, 0x01, 0x64)

    def _loc_EF(): pass

    label('loc_EF')

    PlaySE(451, 0x01, 0x64)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AC, 2, 0x562)),
            Expr.Return,
        ),
        'loc_104',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x57),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_104(): pass

    label('loc_104')

    Return()

# id: 0x0002 offset: 0x105
@scena.Code('func_02_105')
def func_02_105():
    PlaySE(121, 0x01, 0x14)
    EventBegin(0x00)
    CameraMove(4490, 5000, 36760, 0)
    OP_67(0, 5400, -10000, 0)
    CameraSetDistance(5000, 0)
    OP_6C(189000, 0)
    OP_6E(262, 0)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    CreateThread(0x0102, 0x00, 0x00, func_03_1DF)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_0173')
    def lambda_0173():
        CameraMove(970, 5000, -15390, 11000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0173)

    @scena.Lambda('lambda_018B')
    def lambda_018B():
        OP_67(0, 8000, -10000, 11000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_018B)

    Sleep(2000)

    @scena.Lambda('lambda_01A8')
    def lambda_01A8():
        CameraSetDistance(5000, 9000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_01A8)

    @scena.Lambda('lambda_01B8')
    def lambda_01B8():
        OP_6C(156000, 9000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_01B8)

    Sleep(5000)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/E0012._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x1DF
@scena.Code('func_03_1DF')
def func_03_1DF():
    Sleep(300)

    OP_24(0x0079, 0x14)
    Sleep(300)

    OP_24(0x0079, 0x1E)
    Sleep(300)

    OP_24(0x0079, 0x28)
    Sleep(300)

    OP_24(0x0079, 0x32)
    Sleep(300)

    OP_24(0x0079, 0x3C)
    Sleep(300)

    OP_24(0x0079, 0x46)
    Sleep(300)

    OP_24(0x0079, 0x50)
    Sleep(300)

    OP_24(0x0079, 0x5A)
    Sleep(300)

    OP_24(0x0079, 0x64)

    Return()

# id: 0x0004 offset: 0x231
@scena.Code('func_04_231')
def func_04_231():
    EventBegin(0x00)
    FadeIn(2000, 0)
    CameraMove(8370, -18350, -3430, 0)
    OP_67(0, 4240, -10000, 0)
    CameraSetDistance(3360, 0)
    OP_6C(90000, 0)
    OP_6E(378, 0)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetPos(0x0101, 3150, 5000, -2260, 90)
    ChrSetPos(0x0102, 3160, 5000, -3660, 90)

    @scena.Lambda('lambda_02AA')
    def lambda_02AA():
        CameraMove(5750, 5000, -1990, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_02AA)

    @scena.Lambda('lambda_02C2')
    def lambda_02C2():
        OP_67(0, 6400, -10000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_02C2)

    Sleep(2000)

    @scena.Lambda('lambda_02DF')
    def lambda_02DF():
        OP_6C(45000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_02DF)

    @scena.Lambda('lambda_02EF')
    def lambda_02EF():
        OP_6E(262, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_02EF)

    Sleep(8000)

    ChrTalk(
        0x0101,
        (
            '#0010090680V#001F哇～～好高啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090681V我们好像很久没坐过飞艇了吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090682V#010F是啊……\n',
            '上次潜入空贼飞艇的时候\n',
            '连看风景的机会和余闲也没有。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090683V#013F虽说现在和那时很相似，\n',
            '但我觉得这次的状况更为危险……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090684V不能掉以轻心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090685V#007F嗯……知道啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090686V#003F不过，一向和平的利贝尔\n',
            '竟然会发生那样的事情……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090687V我总觉得好像有什么大事\n',
            '开始蠢蠢欲动似的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020090688V#012F#4P是啊……我也这么想。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090689V空贼和卢安市长所做的坏事\n',
            '都是由那些黑衣人在背后操纵。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090690V#015F因此，如果能知道他们的真面目，\n',
            '一定可以掌握到重要的线索。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090691V#010F说不定……\n',
            '这也是父亲外出调查的原因。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010090692V#501F#5P是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090693V#006F好，救出博士之后，\n',
            '我们最好也在附近查查看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/E0012._SN', 100, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

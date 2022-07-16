import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2102_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2102_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T2102.x'
    header.mapIndex       = 1
    header.bgm            = 12
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x6AD
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
    )

# id: 0x10001 offset: 0x64
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
    ]

# id: 0x10002 offset: 0x64
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0x64
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x64
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x64
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x64
@scena.Code('PreInit')
def PreInit():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    OP_28(0x0020, 0x01, 0x0010)
    Fade(1000)
    SetChrPos(0x0102, 113500, 0, 102600, 90)
    SetChrPos(0x0101, 112500, 0, 102300, 90)
    SetChrPos(0x0105, 111200, 0, 103100, 90)

    ExecExpressionWithValue(
        0x000E,
        0x01,
        (
            (Expr.GetChrWork, 0x102, 0x1),
            (Expr.GetChrWork, 0x105, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x02,
        (
            (Expr.GetChrWork, 0x102, 0x2),
            (Expr.GetChrWork, 0x105, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x03,
        (
            (Expr.GetChrWork, 0x102, 0x3),
            (Expr.GetChrWork, 0x105, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6C(135000, 0)

    @scena.Lambda('lambda_00F7')
    def lambda_00F7():
        OP_6C(155000, 3000)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_00F7)

    @scena.Lambda('lambda_0107')
    def lambda_0107():
        OP_69(0x000E, 3000)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_0107)

    CameraSetDistance(2800, 3000)
    WaitForThreadExit(0x000E, 0x0001)
    WaitForThreadExit(0x000E, 0x0002)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020170162V#011F#1P原来如此，\n',
            '『独眼狮子』啊…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170163V照谜语上所写的，\n',
            '这看起来不就是一只狮子吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170164V#006F#2P这里也正是『陆地之港』吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170165V绝对没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020170166V#010F#1P是啊，那就调查一下吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x000E,
        0x01,
        (
            (Expr.PushLong, 0x1C32C),
            (Expr.PushLong, 0x1BB5C),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x02,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x03,
        (
            (Expr.PushLong, 0x19000),
            (Expr.PushLong, 0x190C8),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_0247')
    def lambda_0247():
        OP_6C(180000, 3000)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0247)

    @scena.Lambda('lambda_0257')
    def lambda_0257():
        OP_69(0x000E, 3000)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_0257)

    SetChrFlags(0x0102, 0x0040)
    SetChrDirection(0x0102, 0, 400)

    @scena.Lambda('lambda_0271')
    def lambda_0271():
        ChrWalkTo(0x0101, 113500, 0, 102600, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0271)

    @scena.Lambda('lambda_028C')
    def lambda_028C():
        ChrWalkTo(0x0105, 112600, 0, 103200, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_028C)

    ChrWalkTo(0x0102, 113500, 0, 104100, 2000, 0x00)
    ChrWalkTo(0x0102, 115110, 0, 104100, 2000, 0x00)
    ChrWalkTo(0x0102, 115500, 0, 102400, 2000, 0x00)
    SetChrDirection(0x0102, 225, 400)
    ClearChrFlags(0x0102, 0x0040)
    Sleep(600)

    OP_62(0x0102, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x0102,
        (
            '#0020170167V#012F#1P嗯，有一张卡片。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170168V立刻确认内容。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170169V#006F嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '#0170170170V',
            (TxtCtl.SetColor, 0x0),
            '『啊，探寻者们。\n',
            '　如女神一般直视真实，\n',
            '　抛弃虚伪的人啊。\n',
            '　\n',
            TxtCtl.Enter,
            '#0170170171V　前往开合桥的对面，\n',
            '　安身于钢铁之鹤旁的\n',
            '　木桶所在之处吧。\n',
            '　如是，探寻者们，\n',
            '　汝等将至苍之光所在。\n',
            '　　　　　　　　　　　　　　　怪盗Ｂ』',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010170172V#509F#2P哼，怎么还是这种东西。\n',
            '这回又是『钢铁之鹤』了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170173V#505F所谓『开合桥的对面』\n',
            '就是港湾的方向吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170174V呼，我们究竟要被这种东西\n',
            '捉弄到什么时候啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060170175V#041F#4P呵呵，\n',
            '只要再坚持一下就好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060170176V再加把劲吧，\n',
            '艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020170177V#018F#1P艾丝蒂尔…………\n',
            '你不是一向都很干劲十足的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010170178V#008F#2P啊…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170179V人、人家只是\n',
            '觉得找了这么久有点累嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170180V好、好了，\n',
            '我们鼓足干劲出发吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020170181V#017F#1P真拿你没办法……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_64(0x00, 0x0001)

    @scena.Lambda('lambda_0676')
    def lambda_0676():
        CameraSetDistance(3500, 2000)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0676)

    ChrWalkTo(0x0102, 115110, 0, 104100, 2000, 0x00)
    ChrWalkTo(0x0102, 113500, 0, 104100, 2000, 0x00)
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

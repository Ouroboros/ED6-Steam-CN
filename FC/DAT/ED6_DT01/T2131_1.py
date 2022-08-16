import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2131_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2131_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T2131.x'
    header.mapIndex       = 1
    header.bgm            = 12
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
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    OP_28(0x0020, 0x01, 0x0008)
    Fade(1000)
    ChrSetPos(0x0102, 25900, 0, 26500, 315)
    ChrSetPos(0x0101, 27000, 0, 26500, 315)
    ChrSetPos(0x0105, 27500, 0, 27100, 270)

    ExecExpressionWithValue(
        0x0009,
        0x01,
        (
            (Expr.GetChrWork, 0x105, 0x1),
            (Expr.PushLong, 0x6158),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x02,
        (
            (Expr.GetChrWork, 0x105, 0x2),
            (Expr.PushLong, 0x3E8),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x03,
        (
            (Expr.GetChrWork, 0x105, 0x3),
            (Expr.PushLong, 0x6DC4),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x0009, 2000)

    ChrTalk(
        0x0101,
        (
            '#0010170144V#006F红与黑的圆舞曲…………对吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170145V嗯，除了这个轮盘，\n',
            '应该找不到其他更合适的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020170146V#010F的确如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170147V那么我们就调查一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4A(0x0008, 255)
    ChrTurnDirection(0x0008, 0x0102, 400)

    ChrTalk(
        0x0008,
        (
            '#1780170148V哦，是客人啊…………\n',
            '在找什么东西吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_01F4')
    def lambda_01F4():
        ChrTurnDirection(0x0101, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_01F4)

    ChrTurnDirection(0x0102, 0x0008, 400)

    ChrTalk(
        0x0102,
        (
            '#0020170149V#010F非常抱歉，\n',
            '我们马上就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_023B')
    def lambda_023B():
        ChrTurnDirection(0x0101, 0x0102, 0)
        Yield()

        Jump('lambda_023B')

    DispatchAsync2(0x0101, 0x0001, lambda_023B)

    @scena.Lambda('lambda_024C')
    def lambda_024C():
        ChrTurnDirection(0x0105, 0x0102, 0)
        Yield()

        Jump('lambda_024C')

    DispatchAsync2(0x0105, 0x0001, lambda_024C)

    @scena.Lambda('lambda_025D')
    def lambda_025D():
        ChrTurnDirection(0x0008, 0x0102, 0)
        Yield()

        Jump('lambda_025D')

    DispatchAsync2(0x0008, 0x0001, lambda_025D)

    ChrSetFlags(0x0102, 0x0040)
    ChrWalkTo(0x0102, 25970, 0, 27210, 2000, 0x00)
    ChrSetDirection(0x0102, 315, 400)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0105, 0x01)
    TerminateThread(0x0008, 0x01)
    Sleep(600)

    OP_62(0x0102, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x0102,
        (
            '#0020170150V#012F……果然这里也有。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170151V横着贴上了一张卡片。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060170152V#040F那么…………\n',
            '下一条提示\n',
            '写的又是什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0105, 400)

    ChrTalk(
        0x0102,
        (
            '#0020170153V#010F嗯，看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '#0170170154V',
            (TxtCtl.SetColor, 0x0),
            '『啊，探寻者们。\n',
            '　如女神一般直视真实，\n',
            '　抛弃虚伪的人啊。\n',
            '　\n',
            '　前往栖身于陆地之港的\n',
            '　独眼狮子所在之处吧。\n',
            '　如是，探寻者们，\n',
            '　汝等将至苍之光所在。\n',
            '　　　　　　　　　　　怪盗Ｂ』',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)

    @scena.Lambda('lambda_0463')
    def lambda_0463():
        ChrTurnDirection(0x0105, 0x0102, 0)
        Yield()

        Jump('lambda_0463')

    DispatchAsync2(0x0105, 0x0001, lambda_0463)

    @scena.Lambda('lambda_0474')
    def lambda_0474():
        ChrTurnDirection(0x0008, 0x0102, 0)
        Yield()

        Jump('lambda_0474')

    DispatchAsync2(0x0008, 0x0001, lambda_0474)

    ChrWalkTo(0x0102, 25900, 0, 26500, 2000, 0x00)

    @scena.Lambda('lambda_0499')
    def lambda_0499():
        ChrTurnDirection(0x0102, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0499)

    ChrTurnDirection(0x0101, 0x0102, 400)
    TerminateThread(0x0105, 0x01)
    TerminateThread(0x0008, 0x01)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010170155V#006F好的，已经记录下来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170156V重要的部分就是『陆地之港』\n',
            '和『独眼狮子』这两点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060170157V#043F这次变成『独眼』了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020170158V#010F根据至今为止的经验，\n',
            '我认为只要找到相应的地方后\n',
            '再仔细调查一下就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010170159V#006F嗯，\n',
            '那我们这就展开行动吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    ChrTurnDirection(0x0008, 0x0102, 400)

    ChrTalk(
        0x0008,
        (
            '#1780170160V？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0626')
    def lambda_0626():
        ChrTurnDirection(0x0101, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0626)

    @scena.Lambda('lambda_0634')
    def lambda_0634():
        ChrTurnDirection(0x0105, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_0634)

    ChrTurnDirection(0x0102, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010170161V#001F打扰您了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(1000)
    ChrSetDirection(0x0008, 0, 0)
    OP_4B(0x0008, 255)
    OP_64(0x00, 0x0001)

    ExecExpressionWithValue(
        0x0001,
        0x01,
        (
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0001,
        0x02,
        (
            (Expr.GetChrWork, 0x0, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0001,
        0x03,
        (
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0002,
        0x01,
        (
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0002,
        0x02,
        (
            (Expr.GetChrWork, 0x0, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0002,
        0x03,
        (
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x0102, 0x0040)
    EventEnd(0x00)

    Return()

# id: 0x0001 offset: 0x6BC
@scena.Code('func_01_6BC')
def func_01_6BC():
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '钓鱼工具并排摆在架子上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_718',
    )

    OP_28(0x0021, 0x01, 0x1000)

    Jump('loc_8AC')

    def _loc_718(): pass

    label('loc_718')

    If(
        (
            (Expr.Eval, "OP_40(0x0332)"),
            Expr.Return,
        ),
        'loc_764',
    )

    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010170482V#000F钓鱼竿用完之后，\n',
            '要还给这家店的人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8AC')

    def _loc_764(): pass

    label('loc_764')

    If(
        (
            (Expr.Eval, "OP_29(0x0021, 0x01, 0x0010)"),
            Expr.Return,
        ),
        'loc_7AD',
    )

    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010170483V#007F呼，\n',
            '本来我还想好好钓一次鱼的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8AC')

    def _loc_7AD(): pass

    label('loc_7AD')

    If(
        (
            (Expr.Eval, "OP_29(0x0021, 0x00, 0x40)"),
            Expr.Return,
        ),
        'loc_7BA',
    )

    Jump('loc_8AC')

    def _loc_7BA(): pass

    label('loc_7BA')

    If(
        (
            (Expr.Eval, "OP_29(0x0021, 0x01, 0x0004)"),
            Expr.Return,
        ),
        'loc_877',
    )

    Sleep(400)

    OP_28(0x0021, 0x01, 0x1000)

    ChrTalk(
        0x0101,
        (
            '#0010170477V#501F…………这里的东西\n',
            '可不可以借走呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020170478V#010F问问店里的人吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170479V这家店的老板在一楼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170480V#000F嗯，好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8AC')

    def _loc_877(): pass

    label('loc_877')

    Sleep(400)

    OP_28(0x0021, 0x01, 0x1000)

    ChrTalk(
        0x0101,
        (
            '#501F这里果然也可以租借钓鱼竿啊。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8AC(): pass

    label('loc_8AC')

    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

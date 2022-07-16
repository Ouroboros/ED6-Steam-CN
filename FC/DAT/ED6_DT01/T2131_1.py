import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2131_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2131_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

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

# id: 0xFFFF offset: 0x83C
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
    OP_28(0x0020, 0x01, 0x0008)
    Fade(1000)
    SetChrPos(0x0102, 25900, 0, 26500, 315)
    SetChrPos(0x0101, 27000, 0, 26500, 315)
    SetChrPos(0x0105, 27500, 0, 27100, 270)

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

    @scena.Lambda('lambda_01DB')
    def lambda_01DB():
        ChrTurnDirection(0x0101, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_01DB)

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

    @scena.Lambda('lambda_021D')
    def lambda_021D():
        ChrTurnDirection(0x0101, 0x0102, 0)
        Yield()

        Jump('lambda_021D')

    DispatchAsync2(0x0101, 0x0001, lambda_021D)

    @scena.Lambda('lambda_022E')
    def lambda_022E():
        ChrTurnDirection(0x0105, 0x0102, 0)
        Yield()

        Jump('lambda_022E')

    DispatchAsync2(0x0105, 0x0001, lambda_022E)

    @scena.Lambda('lambda_023F')
    def lambda_023F():
        ChrTurnDirection(0x0008, 0x0102, 0)
        Yield()

        Jump('lambda_023F')

    DispatchAsync2(0x0008, 0x0001, lambda_023F)

    SetChrFlags(0x0102, 0x0040)
    ChrWalkTo(0x0102, 25970, 0, 27210, 2000, 0x00)
    SetChrDirection(0x0102, 315, 400)
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
    SetChrName('')
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

    @scena.Lambda('lambda_042C')
    def lambda_042C():
        ChrTurnDirection(0x0105, 0x0102, 0)
        Yield()

        Jump('lambda_042C')

    DispatchAsync2(0x0105, 0x0001, lambda_042C)

    @scena.Lambda('lambda_043D')
    def lambda_043D():
        ChrTurnDirection(0x0008, 0x0102, 0)
        Yield()

        Jump('lambda_043D')

    DispatchAsync2(0x0008, 0x0001, lambda_043D)

    ChrWalkTo(0x0102, 25900, 0, 26500, 2000, 0x00)

    @scena.Lambda('lambda_0462')
    def lambda_0462():
        ChrTurnDirection(0x0102, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0462)

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

    @scena.Lambda('lambda_05D1')
    def lambda_05D1():
        ChrTurnDirection(0x0101, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_05D1)

    @scena.Lambda('lambda_05DF')
    def lambda_05DF():
        ChrTurnDirection(0x0105, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_05DF)

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
    SetChrDirection(0x0008, 0, 0)
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

    ClearChrFlags(0x0102, 0x0040)
    EventEnd(0x00)

    Return()

# id: 0x0001 offset: 0x662
@scena.Code('Init')
def Init():
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

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
        'loc_6BE',
    )

    OP_28(0x0021, 0x01, 0x1000)

    Jump('loc_834')

    def _loc_6BE(): pass

    label('loc_6BE')

    If(
        (
            (Expr.Eval, "OP_40(0x0332)"),
            Expr.Return,
        ),
        'loc_705',
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

    Jump('loc_834')

    def _loc_705(): pass

    label('loc_705')

    If(
        (
            (Expr.Eval, "OP_29(0x0021, 0x01, 0x0010)"),
            Expr.Return,
        ),
        'loc_749',
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

    Jump('loc_834')

    def _loc_749(): pass

    label('loc_749')

    If(
        (
            (Expr.Eval, "OP_29(0x0021, 0x00, 0x40)"),
            Expr.Return,
        ),
        'loc_756',
    )

    Jump('loc_834')

    def _loc_756(): pass

    label('loc_756')

    If(
        (
            (Expr.Eval, "OP_29(0x0021, 0x01, 0x0004)"),
            Expr.Return,
        ),
        'loc_7FF',
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

    Jump('loc_834')

    def _loc_7FF(): pass

    label('loc_7FF')

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

    def _loc_834(): pass

    label('loc_834')

    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

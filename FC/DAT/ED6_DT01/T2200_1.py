import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2200_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2200_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T2200.x'
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
    EventBegin(0x00)
    OP_69(0x0101, 0)
    MapSetFlags(0x00400000)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x0105, 0x0080)
    ChrSetPos(0x0101, 113000, 2000, 22300, 270)
    ChrSetPos(0x0102, 114500, 2000, 21500, 270)
    ChrSetPos(0x0105, 115000, 2000, 22600, 270)

    ExecExpressionWithValue(
        0x000A,
        0x01,
        (
            (Expr.GetChrWork, 0x102, 0x1),
            (Expr.GetChrWork, 0x101, 0x1),
            Expr.Add,
            (Expr.GetChrWork, 0x105, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x3),
            Expr.Div,
            (Expr.PushLong, 0x1770),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x02,
        (
            (Expr.GetChrWork, 0x102, 0x2),
            (Expr.GetChrWork, 0x101, 0x2),
            Expr.Add,
            (Expr.GetChrWork, 0x105, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x3),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x03,
        (
            (Expr.GetChrWork, 0x102, 0x3),
            (Expr.GetChrWork, 0x101, 0x3),
            Expr.Add,
            (Expr.GetChrWork, 0x105, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x3),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6F(0x0000, 30)
    ChrClearFlags(0x0101, 0x0080)
    ChrClearFlags(0x0102, 0x0080)
    ChrClearFlags(0x0105, 0x0080)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_012D')
    def lambda_012D():
        OP_94(0x01, 0x0101, 0x0000, 0x000015E0, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_012D)

    Sleep(200)

    @scena.Lambda('lambda_0148')
    def lambda_0148():
        OP_94(0x01, 0x0102, 0x0000, 0x00001770, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0148)

    Sleep(200)

    @scena.Lambda('lambda_0163')
    def lambda_0163():
        OP_94(0x01, 0x0105, 0x0000, 0x00001900, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_0163)

    @scena.Lambda('lambda_0179')
    def lambda_0179():
        OP_69(0x000A, 3000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0179)

    OP_0D()
    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_018D')
    def lambda_018D():
        ChrTurnDirection(0x0101, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_018D)

    OP_72(0x0000, 0x0800)
    PlaySE(7, 0x00, 0x64)
    OP_6F(0x0000, 30)
    OP_70(0x0000, 0)
    OP_73(0x0000)
    OP_71(0x0000, 0x0800)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010170365V#007F呼～～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170366V总算是勉强完成了任务，\n',
            '不过总感觉不够彻底啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060170367V#043F嗯，是啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020170368V#013F……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x0101, 0x0102, 400)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010170369V#002F啊，约修亚你怎么了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170370V一个人在那里想些什么呢？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0102, 400)
    OP_62(0x0102, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020170371V#010F啊…………？\n',
            '……嗯，没什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170372V只是在想……\n',
            '犯人偷烛台的动机究竟是什么呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170373V#004F啊，对啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170374V最后我们还是不明白这一点呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0102, 400)

    ChrTalk(
        0x0105,
        (
            '#0060170375V#042F最后一张卡片的内容\n',
            '应该隐含着更深层的含义。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060170376V从那种行文的语气来看，\n',
            '好像对于艾丝蒂尔你们\n',
            '抱有什么期待一样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170377V#003F唔……\n',
            '我还是非常在意呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170378V#002F不如……\n',
            '我们继续进行调查吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170379V先判断一下犯人\n',
            '大概会隐藏在什么地方。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170380V等今晚时机一到，\n',
            '我们就去对应的房屋里面调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0102,
        (
            '#0020170381V#018F那我们不就和小偷\n',
            '没什么两样了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170382V#009F可是，我不甘心啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020170383V#017F这也是没有办法的事，\n',
            '委托人并不希望这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170384V#010F我们就忍住吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010170385V#505F唔…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020170386V#010F好了，我们走吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170387V市长说的话很对，\n',
            '还要许多需要我们去做的事情呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170388V#505F……嗯，明白了。\n',
            '只有忍住了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170389V#006F那好，\n',
            '我们就调整心情继续努力吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060170390V#041F嗯，就应该这样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【烛台失窃事件】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)

    MapClearFlags(0x00400000)
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

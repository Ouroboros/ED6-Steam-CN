import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2700_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2700_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T2700.x'
    header.mapIndex       = 1
    header.bgm            = 16
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
    FadeIn(2000, 0)
    MapSetFlags(0x00400000)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    TerminateThread(0x0008, 0xFF)
    CameraMove(10100, 15000, 8500, 0)

    ExecExpressionWithValue(
        0x000C,
        0x01,
        (
            (Expr.GetChrWork, 0x8, 0x1),
            (Expr.GetChrWork, 0x9, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x02,
        (
            (Expr.GetChrWork, 0x8, 0x2),
            (Expr.GetChrWork, 0x9, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x03,
        (
            (Expr.GetChrWork, 0x8, 0x3),
            (Expr.GetChrWork, 0x9, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_00E7')
    def lambda_00E7():
        OP_69(0x000C, 6000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_00E7)

    CameraSetDistance(2800, 6000)
    OP_0D()
    WaitForThreadExit(0x000C, 0x0001)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#1860170602V那么…………\n',
            '大人的心情现在怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0660170603V#720F大人是那种话一旦说出口，\n',
            '就固执得谁也劝不动的类型……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660170604V无论我们如何劝说，\n',
            '都改变不了他的主意，\n',
            '就是想要在这里留宿啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1860170605V唔，这样啊…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1860170606V没办法，\n',
            '在游击士来之前，\n',
            '就只能先稳定他的情绪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0660170607V#720F是的，真是过意不去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660170608V那我就先告辞了………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1860170609V…………嗯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0009, 1400, 5000, 2000, 2000, 0x00)

    @scena.Lambda('lambda_02BD')
    def lambda_02BD():
        ChrWalkTo(0x0009, -4700, 5000, 2000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_02BD)

    ChrSetDirection(0x0008, 0, 400)
    ChrSetPos(0x0101, -3600, 5000, 0, 90)
    ChrSetPos(0x0102, -4600, 5000, -1000, 90)
    ChrSetPos(0x0105, -5600, 5000, 400, 90)
    ChrClearFlags(0x0000, 0x0080)
    ChrClearFlags(0x0001, 0x0080)
    ChrClearFlags(0x0002, 0x0080)

    @scena.Lambda('lambda_0321')
    def lambda_0321():
        OP_94(0x01, 0x0101, 0x0000, 0x00001964, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0321)

    Sleep(200)

    @scena.Lambda('lambda_033C')
    def lambda_033C():
        OP_94(0x01, 0x0102, 0x0000, 0x00001B58, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_033C)

    Sleep(200)

    @scena.Lambda('lambda_0357')
    def lambda_0357():
        OP_94(0x01, 0x0105, 0x0000, 0x00001B58, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_0357)

    WaitForThreadExit(0x0101, 0x0001)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(400)

    ChrSetDirection(0x0101, 315, 400)
    ChrSetDirection(0x0101, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010170610V#004F…………咦？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170611V刚才那个人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0009, 0x0080)
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x0008, 0x0101, 400)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#1860170612V哦哦，你们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1860170613V是游击士，对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x000C,
        0x01,
        (
            (Expr.GetChrWork, 0x8, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Sub,
            (Expr.GetChrWork, 0x101, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x02,
        (
            (Expr.GetChrWork, 0x8, 0x2),
            (Expr.GetChrWork, 0x101, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x03,
        (
            (Expr.GetChrWork, 0x8, 0x3),
            (Expr.GetChrWork, 0x101, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_0483')
    def lambda_0483():
        OP_69(0x000C, 1000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0483)

    @scena.Lambda('lambda_0491')
    def lambda_0491():
        OP_94(0x01, 0x0008, 0x0000, 0x000003E8, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0491)

    @scena.Lambda('lambda_04A7')
    def lambda_04A7():
        ChrTurnDirection(0x0101, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_04A7)

    @scena.Lambda('lambda_04B5')
    def lambda_04B5():
        ChrTurnDirection(0x0102, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_04B5)

    ChrTurnDirection(0x0105, 0x0008, 400)
    WaitForThreadExit(0x0008, 0x0001)

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x02)"),
            Expr.Return,
        ),
        'loc_5C8',
    )

    ChrTalk(
        0x0008,
        (
            '#1860170614V终于来了啊。\n',
            '我是守备队队长哈恩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170615V#508F啊，初次见面。\n',
            '我是准游击士艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020170616V#010F我是准游击士约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170617V我们从公告板上了解到\n',
            '关所来了一个麻烦的旅行者，\n',
            '所以来看看能帮上什么忙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_613')

    def _loc_5C8(): pass

    label('loc_5C8')

    ChrTalk(
        0x0101,
        (
            '#0010170618V#501F嗯，然后呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020170619V#014F有什么问题吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_613(): pass

    label('loc_613')

    OP_28(0x0023, 0x04, 0x04)
    OP_28(0x0023, 0x04, 0x02)
    ChrTurnDirection(0x0102, 0x0008, 400)

    ChrTalk(
        0x0008,
        (
            '#1860170620V嗯，是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1860170621V实际上有一个非常麻烦的旅行者……\n',
            '想要处理妥当十分困难。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1860170622V如果可以的话，\n',
            '能请你们帮帮忙吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        10,
        0,
        (
            TXT(0x00, '【是】\n'),
            TXT(0x01, '【否】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_71B'),
        (0x00000001, 'loc_7BF'),
        (-1, 'loc_900'),
    )

    def _loc_71B(): pass

    label('loc_71B')

    OP_28(0x0023, 0x04, 0x08)

    ChrTalk(
        0x0101,
        (
            '#0010150127V#000F嗯，好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1860170624V谢谢了，真是帮大忙了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1860170625V那么就先到楼下去，\n',
            '我把详细的情况告诉你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    NewScene('ED6_DT01/T2710._SN', 101, 0, 0)
    IdleLoop()

    Jump('loc_900')

    def _loc_7BF(): pass

    label('loc_7BF')

    OP_28(0x0023, 0x01, 0x4000)

    ChrTalk(
        0x0101,
        (
            '#0010170626V#003F抱歉，\n',
            '现在大概不行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1860170627V是吗，\n',
            '不过我这边也的确很麻烦啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1860170628V那我们唯有\n',
            '先靠自己去说服他吧，\n',
            '虽然知道自己对这种事不是很擅长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1860170629V你们一旦有空，\n',
            '就请尽快过来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020170630V#010F嗯，明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1860170631V唔，拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(1000)
    CameraSetDistance(3500, 0)
    ChrSetDirection(0x0008, 270, 0)

    Jump('loc_900')

    def _loc_900(): pass

    label('loc_900')

    OP_85(0x0008)
    MapClearFlags(0x00400000)
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

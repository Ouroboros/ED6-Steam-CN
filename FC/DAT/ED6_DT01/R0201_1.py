import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import R0201_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R0201_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0131.x'
    header.mapIndex       = 22
    header.bgm            = 20
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
    MapClearFlags(0x00000001)
    MapSetFlags(0x08000000)
    Fade(1000)
    OP_6C(260000, 0)

    @scena.Lambda('lambda_0084')
    def lambda_0084():
        CameraSetDistance(2500, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0084)

    ChrSetPos(0x0101, -205210, 0, -19200, 135)
    ChrSetPos(0x0102, -206190, 20, -20420, 135)
    CameraMove(-205750, 20, -20780, 3000)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010150454V#000F根据佛莱迪叔叔所说的，\n',
            '我想大概就是这个路灯吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150455V#010F我也是这么想的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150456V#010F外面的面板上\n',
            '也写着『６号路灯』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150457V#006F啊，果然。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150458V好～的，\n',
            '我们赶快把它弄好收工吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrSetDirection(0x0102, 180, 400)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020150459V#012F……很可惜，\n',
            '好像不会那么顺利。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010150460V#004F……哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0008, -202100, 0, -35820, 0)
    ChrSetPos(0x0009, -199870, 1000, -36700, 0)
    ChrSetPos(0x000A, -197980, 0, -35450, 0)
    ChrSetPos(0x000B, -196350, 0, -33810, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)

    @scena.Lambda('lambda_0297')
    def lambda_0297():
        ChrMoveToRelative(0x0008, -1000, 0, 5000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0297)

    Sleep(150)

    @scena.Lambda('lambda_02B7')
    def lambda_02B7():
        ChrMoveToRelative(0x0009, -1000, 0, 5000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_02B7)

    Sleep(100)

    @scena.Lambda('lambda_02D7')
    def lambda_02D7():
        ChrMoveToRelative(0x000A, -1000, 0, 5000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_02D7)

    Sleep(120)

    @scena.Lambda('lambda_02F7')
    def lambda_02F7():
        ChrMoveToRelative(0x000B, -1000, 0, 5000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_02F7)

    @scena.Lambda('lambda_0312')
    def lambda_0312():
        OP_6C(225000, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0312)

    @scena.Lambda('lambda_0322')
    def lambda_0322():
        CameraMove(-202310, 0, -28900, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_0322)

    WaitForThreadExit(0x0008, 0x0001)
    ChrSetChipByIndex(0x0008, 8)
    CreateThread(0x0008, 0x00, 0x00, 0x0002)

    @scena.Lambda('lambda_034B')
    def lambda_034B():
        ChrTurnDirection(0x0008, 0x0101, 0)
        Yield()

        Jump('lambda_034B')

    DispatchAsync2(0x0008, 0x0001, lambda_034B)

    WaitForThreadExit(0x0009, 0x0001)
    ChrSetChipByIndex(0x0009, 8)
    CreateThread(0x0009, 0x00, 0x00, 0x0002)

    @scena.Lambda('lambda_036D')
    def lambda_036D():
        ChrTurnDirection(0x0009, 0x0101, 0)
        Yield()

        Jump('lambda_036D')

    DispatchAsync2(0x0009, 0x0001, lambda_036D)

    WaitForThreadExit(0x000A, 0x0001)
    ChrSetChipByIndex(0x000A, 8)
    CreateThread(0x000A, 0x00, 0x00, 0x0002)

    @scena.Lambda('lambda_038F')
    def lambda_038F():
        ChrTurnDirection(0x000A, 0x0101, 0)
        Yield()

        Jump('lambda_038F')

    DispatchAsync2(0x000A, 0x0001, lambda_038F)

    WaitForThreadExit(0x000B, 0x0001)
    ChrSetChipByIndex(0x000B, 8)
    CreateThread(0x000B, 0x00, 0x00, 0x0002)

    @scena.Lambda('lambda_03B1')
    def lambda_03B1():
        ChrTurnDirection(0x000B, 0x0101, 0)
        Yield()

        Jump('lambda_03B1')

    DispatchAsync2(0x000B, 0x0001, lambda_03B1)

    WaitForThreadExit(0x0000, 0x0001)
    ChrClearFlags(0x000C, 0x0008)
    ChrClearFlags(0x000D, 0x0008)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetFlags(0x0101, 0x0008)
    ChrSetFlags(0x0102, 0x0008)
    ChrSetPos(0x000C, -206450, 50, -21160, 141)
    ChrSetPos(0x000D, -206450, 50, -21160, 141)
    ChrSetFlags(0x000D, 0x1000)
    ChrSetFlags(0x000C, 0x1000)
    ChrSetFlags(0x000D, 0x0040)
    ChrSetFlags(0x000C, 0x0040)
    ChrSetChipByIndex(0x000D, 5)
    ChrSetChipByIndex(0x000C, 4)

    @scena.Lambda('lambda_0425')
    def lambda_0425():
        ChrWalkTo(0x000D, -204690, -70, -24890, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_0425)

    ChrWalkTo(0x000C, -203610, -30, -24480, 5000, 0x00)
    WaitForThreadExit(0x000D, 0x0001)
    ChrSetDirection(0x000D, 180, 0)
    ChrSetDirection(0x000C, 180, 0)
    ChrSetChipByIndex(0x000D, 7)
    ChrSetChipByIndex(0x000C, 6)
    CameraMove(-202010, 10, -26160, 1000)

    ChrTalk(
        0x000C,
        (
            '#0010150461V#002F怎、怎么会有这么多魔兽！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0020150462V#012F应该是由于\n',
            '导力灯的故障而被引来的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150463V#012F总而言之，如果不击退它们，\n',
            '是没法安心更换导力灯的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0010150464V#002F嗯，对，没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150465V那么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_568(): pass

    label('loc_568')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_619',
    )

    FadeOut(300, 0, 100)

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
        100,
        0,
        (
            TXT(0x00, '【魔兽就交给我来解决！】\n'),
            TXT(0x01, '【魔兽就交给约修亚你了！】\n'),
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
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_5EE'),
        (0x00000001, 'loc_602'),
        (-1, 'loc_616'),
    )

    def _loc_5EE(): pass

    label('loc_5EE')

    Call(1, 0x0001)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)

    Jump('loc_616')

    def _loc_602(): pass

    label('loc_602')

    Call(1, 0x0002)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)

    Jump('loc_616')

    def _loc_616(): pass

    label('loc_616')

    Jump('loc_568')

    def _loc_619(): pass

    label('loc_619')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_64(0x00, 0x0001)
    OP_28(0x0006, 0x01, 0x0008)
    ChrClearFlags(0x0102, 0x0040)
    ChrClearFlags(0x0101, 0x0040)
    EventEnd(0x00)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0001 offset: 0x63F
@scena.Code('func_01_63F')
def func_01_63F():
    FormationDelMember(0x01, 0x00)

    ChrTalk(
        0x000C,
        (
            '#0010150466V#002F魔兽就交给我来解决！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0020150467V#012F明白。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150468V我去打开控电盘的时候，\n',
            '其他的就拜托你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0010150469V#005F嗯！交给我吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x000D, 18)
    ChrSetChipByIndex(0x000C, 4)
    ChrSetChipByIndex(0x0008, 9)
    ChrSetChipByIndex(0x0009, 9)
    ChrSetChipByIndex(0x000A, 9)
    ChrSetChipByIndex(0x000B, 9)

    @scena.Lambda('lambda_070A')
    def lambda_070A():
        OP_92(0x0008, 0x0101, 4600, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_070A)

    @scena.Lambda('lambda_071F')
    def lambda_071F():
        OP_92(0x0009, 0x0101, 4600, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_071F)

    @scena.Lambda('lambda_0734')
    def lambda_0734():
        OP_92(0x000A, 0x0101, 4600, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0734)

    @scena.Lambda('lambda_0749')
    def lambda_0749():
        OP_92(0x000B, 0x0101, 4600, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0749)

    @scena.Lambda('lambda_075E')
    def lambda_075E():
        ChrWalkTo(0x000D, -205980, 60, -21600, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_075E)

    ChrWalkTo(0x000C, -202710, 0, -26520, 6000, 0x00)
    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x000D, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Battle(0x000003EB, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_7C1'),
        (-1, 'loc_7C6'),
    )

    def _loc_7C1(): pass

    label('loc_7C1')

    OP_B4(0x00)

    Jump('loc_7C6')

    def _loc_7C6(): pass

    label('loc_7C6')

    EventBegin(0x00)
    PlayBGM(20)
    FormationAddMember(0x01, 0x01)
    CameraMove(-203550, -30, -24610, 0)
    ChrClearFlags(0x0102, 0x0008)
    ChrClearFlags(0x0101, 0x0008)
    ChrSetChipByIndex(0x0101, 6)
    ChrSetPos(0x0101, -202010, 10, -26160, 180)
    ChrSetPos(0x0102, -204100, 0, -20750, 180)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010150470V#002F哼，知道我的厉害了吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150471V#014F（……很厉害啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    ChrSetChipByIndex(0x0101, 65535)
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010150472V#002F约修亚！\n',
            '你那边的情况如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150473V#010F现在正在输入解锁密码。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150474V嗯……\n',
            '５·４·４·８·１·８……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150475V#002F我这边没问题了，\n',
            '放心去弄吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    PlaySE(131, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0102,
        (
            '#0020150476V#012F……好的，打开了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150477V接下来是更换导力器……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    RemoveItem(0x0327, 1)

    ChrTalk(
        0x0101,
        (
            '#0010150478V#502F嘿嘿嘿嘿，\n',
            '我的斗志正在燃烧～～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0101, 6)
    ChrSetDirection(0x0101, 0, 400)
    ChrSetDirection(0x0101, 45, 400)
    OP_62(0x0101, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    PlaySE(126, 0x01, 0x64)
    ChrSetChipByIndex(0x0101, 16)

    @scena.Lambda('lambda_0A2F')
    def lambda_0A2F():
        OP_99(0x00FE, 0x00, 0x07, 3000)
        Yield()

        Jump('lambda_0A2F')

    DispatchAsync2(0x0101, 0x0000, lambda_0A2F)

    @scena.Lambda('lambda_0A42')
    def lambda_0A42():
        CameraMove(-202010, 10, -26160, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0A42)

    ChrSetFlags(0x0102, 0x0040)

    @scena.Lambda('lambda_0A5F')
    def lambda_0A5F():
        ChrWalkTo(0x0102, -203190, -10, -20690, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0A5F)

    WaitForThreadExit(0x0102, 0x0001)

    @scena.Lambda('lambda_0A7F')
    def lambda_0A7F():
        ChrWalkTo(0x0102, -201660, -30, -22540, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0A7F)

    WaitForThreadExit(0x0102, 0x0001)

    @scena.Lambda('lambda_0A9F')
    def lambda_0A9F():
        OP_92(0x0102, 0x0101, 1500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0A9F)

    OP_23(0x007E)
    TerminateThread(0x0101, 0x00)
    ChrSetChipByIndex(0x0101, 6)
    ChrSetDirection(0x0101, 180, 400)
    WaitForThreadExit(0x0102, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010150479V#005F出来吧！你们这些魔兽！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0102, 0x0001)

    ChrTalk(
        0x0102,
        (
            '#0020150480V#010F久等了，艾丝蒂尔。\n',
            '已经完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(800)

    Sleep(400)

    ChrSetChipByIndex(0x0101, 65535)
    ChrTurnDirection(0x0101, 0x0102, 400)
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010150481V#000F……啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150482V#004F咦？已经完成了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150483V难道连导力器\n',
            '也已经更换好了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150484V#010F嗯，这样就不会再有魔兽来袭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 45, 400)
    OP_62(0x0101, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010150485V#007F唉，这样就结束了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1000)

    OP_63(0x0102)

    ChrTalk(
        0x0102,
        (
            '#0020150486V#018F……………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150487V怎么觉得你好像\n',
            '有点意犹未尽的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010150488V#506F哈、哈哈哈☆',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150489V错、错觉啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150490V#017F真是的，艾丝蒂尔你啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_2B(0x0006, 0x0001)
    Sleep(400)

    Return()

# id: 0x0002 offset: 0xD5B
@scena.Code('func_02_D5B')
def func_02_D5B():
    FormationDelMember(0x00, 0x00)

    ChrTalk(
        0x000C,
        (
            '#0010150491V#002F魔兽就交给约修亚你了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x000D,
        (
            '#0020150492V#014F艾丝蒂尔，这样没问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0010150493V#009F真是的～别担心那么多啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150494V更换导力器这种小事，\n',
            '对我来说简直是轻而易举啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0020150495V#012F明白。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150496V那么，路灯就拜托你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0010150469V#005F嗯！交给我吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x000D, 5)
    ChrSetChipByIndex(0x000C, 17)
    ChrSetChipByIndex(0x0008, 9)
    ChrSetChipByIndex(0x0009, 9)
    ChrSetChipByIndex(0x000A, 9)
    ChrSetChipByIndex(0x000B, 9)

    @scena.Lambda('lambda_0ECC')
    def lambda_0ECC():
        OP_92(0x0008, 0x0101, 4600, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0ECC)

    @scena.Lambda('lambda_0EE1')
    def lambda_0EE1():
        OP_92(0x0009, 0x0101, 4600, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0EE1)

    @scena.Lambda('lambda_0EF6')
    def lambda_0EF6():
        OP_92(0x000A, 0x0101, 4600, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0EF6)

    @scena.Lambda('lambda_0F0B')
    def lambda_0F0B():
        OP_92(0x000B, 0x0101, 4600, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0F0B)

    @scena.Lambda('lambda_0F20')
    def lambda_0F20():
        ChrWalkTo(0x000C, -205980, 60, -21600, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0F20)

    ChrWalkTo(0x000D, -202710, 0, -26520, 6000, 0x00)
    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x000D, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Battle(0x000003EB, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_F83'),
        (-1, 'loc_F88'),
    )

    def _loc_F83(): pass

    label('loc_F83')

    OP_B4(0x00)

    Jump('loc_F88')

    def _loc_F88(): pass

    label('loc_F88')

    EventBegin(0x00)
    PlayBGM(20)
    FormationAddMember(0x00, 0x00)
    CameraMove(-203550, -30, -24610, 0)
    ChrClearFlags(0x0102, 0x0008)
    ChrClearFlags(0x0101, 0x0008)
    ChrSetChipByIndex(0x0102, 7)
    ChrSetPos(0x0102, -202010, 10, -26160, 180)
    ChrSetPos(0x0101, -204100, 0, -20750, 180)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020150498V#012F……这样就算解决了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrSetChipByIndex(0x0102, 65535)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020150499V#012F艾丝蒂尔，\n',
            '你那边的情况如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150500V#002F正在开始输入控电盘的解锁密码。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150501V#505F嗯～～\n',
            '正确的密码是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_10C9(): pass

    label('loc_10C9')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_117D',
    )

    FadeOut(300, 0, 100)

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
        100,
        0,
        (
            TXT(0x00, '【５４５８１８】\n'),
            TXT(0x01, '【５５４８１８】\n'),
            TXT(0x02, '【５４４８１８】\n'),
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
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1152'),
        (0x00000001, 'loc_115C'),
        (0x00000002, 'loc_1166'),
        (-1, 'loc_117A'),
    )

    def _loc_1152(): pass

    label('loc_1152')

    Call(1, 0x0003)
    OP_5F(0x0000)

    Jump('loc_117A')

    def _loc_115C(): pass

    label('loc_115C')

    Call(1, 0x0003)
    OP_5F(0x0000)

    Jump('loc_117A')

    def _loc_1166(): pass

    label('loc_1166')

    Call(1, 0x0004)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)

    Jump('loc_117A')

    def _loc_117A(): pass

    label('loc_117A')

    Jump('loc_10C9')

    def _loc_117D(): pass

    label('loc_117D')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(400)

    Return()

# id: 0x0003 offset: 0x118D
@scena.Code('func_03_118D')
def func_03_118D():
    OP_28(0x0006, 0x01, 0x0004)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_124C',
    )

    ChrTalk(
        0x0101,
        (
            '#0010150502V#002F５·４·５·８·１·８……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150503V……………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150504V#509F……………………咦？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150505V怎么回事～\n',
            '怎么没打开呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12F5')

    def _loc_124C(): pass

    label('loc_124C')

    ChrTalk(
        0x0101,
        (
            '#0010150506V#002F５·５·４·８·１·８……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150503V……………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150504V#509F……………………咦？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150505V怎么回事～\n',
            '怎么没打开呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12F5(): pass

    label('loc_12F5')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0102,
        (
            '#0020150510V#017F（果然。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrSetChipByIndex(0x0102, 7)
    ChrSetDirection(0x0102, 180, 400)
    Sleep(400)

    ChrSetPos(0x0008, -202100, 0, -35820, 0)
    ChrSetPos(0x000A, -197980, 0, -35450, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x000A, 0x0080)

    @scena.Lambda('lambda_1396')
    def lambda_1396():
        CameraMove(-202310, 0, -28900, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_1396)

    @scena.Lambda('lambda_13AE')
    def lambda_13AE():
        ChrMoveToRelative(0x0008, -1000, 0, 5000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_13AE)

    Sleep(150)

    @scena.Lambda('lambda_13CE')
    def lambda_13CE():
        ChrMoveToRelative(0x000A, -1000, 0, 5000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_13CE)

    WaitForThreadExit(0x0008, 0x0001)
    ChrSetChipByIndex(0x0008, 8)
    CreateThread(0x0008, 0x00, 0x00, 0x0002)

    @scena.Lambda('lambda_13FA')
    def lambda_13FA():
        ChrTurnDirection(0x0008, 0x0102, 0)
        Yield()

        Jump('lambda_13FA')

    DispatchAsync2(0x0008, 0x0001, lambda_13FA)

    WaitForThreadExit(0x000A, 0x0001)
    ChrSetChipByIndex(0x000A, 8)
    CreateThread(0x000A, 0x00, 0x00, 0x0002)

    @scena.Lambda('lambda_141C')
    def lambda_141C():
        ChrTurnDirection(0x000A, 0x0102, 0)
        Yield()

        Jump('lambda_141C')

    DispatchAsync2(0x000A, 0x0001, lambda_141C)

    WaitForThreadExit(0x0000, 0x0002)

    ChrTalk(
        0x0102,
        (
            '#0020150511V#013F唉，又来了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x000D, -202010, 10, -26160, 180)
    ChrSetChipByIndex(0x000D, 7)
    ChrClearFlags(0x000D, 0x0008)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetFlags(0x0102, 0x0008)
    ChrSetChipByIndex(0x0008, 9)
    ChrSetChipByIndex(0x000A, 9)

    @scena.Lambda('lambda_1488')
    def lambda_1488():
        OP_92(0x0008, 0x000D, 3600, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1488)

    @scena.Lambda('lambda_149D')
    def lambda_149D():
        OP_92(0x000A, 0x000D, 3600, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_149D)

    WaitForThreadExit(0x000A, 0x0001)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x000A, 0xFF)
    FormationDelMember(0x00, 0x00)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Battle(0x000003EC, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_14DE'),
        (-1, 'loc_14E3'),
    )

    def _loc_14DE(): pass

    label('loc_14DE')

    OP_B4(0x00)

    Jump('loc_14E3')

    def _loc_14E3(): pass

    label('loc_14E3')

    EventBegin(0x00)
    PlayBGM(20)
    FormationAddMember(0x00, 0x00)
    CameraMove(-203550, -30, -24610, 0)
    ChrSetChipByIndex(0x0102, 7)
    ChrSetPos(0x0102, -202010, 10, -26160, 180)
    ChrSetPos(0x0101, -204100, 0, -20750, 180)
    CameraMove(-203320, -20, -24970, 0)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrClearFlags(0x0102, 0x0008)
    ChrClearFlags(0x0102, 0x0080)
    OP_0D()
    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010150512V#009F啊～\n',
            '为什么还是没打开！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150513V气死我了，我要采取一些行动了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 225, 2000)
    ChrSetDirection(0x0101, 45, 2000)
    ChrSetDirection(0x0101, 180, 2000)
    ChrSetChipByIndex(0x0101, 6)

    ChrTalk(
        0x0101,
        (
            '#0010150514V#005F就让我用实力把它……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0102, 65535)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020150515V#012F艾丝蒂尔，等一下！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150516V解锁密码是『５４４８１８』！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010150517V#501F…………嗯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetDirection(0x0101, 135, 400)

    ChrTalk(
        0x0101,
        (
            '#0010150518V#004F等、等一下，\n',
            '再说一次！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150519V#017F５·４·４…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010150520V#002F嗯～５·４·４……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150521V#017F…………８·１·８。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150522V#002F……８·１·８。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    PlaySE(131, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010150523V#004F……啊，打开了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150524V#502F呵呵㈱\n',
            '这样就等于完全成功了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150525V#018F（她还真是自得其乐啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010150526V#006F接下来，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150527V把导力器更换……好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150528V#001F好了，完成～～⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150529V呼～～～\n',
            '这回可真是累人啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_18EC')
    def lambda_18EC():
        CameraMove(-203230, -10, -20760, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_18EC)

    ChrWalkTo(0x0102, -202460, -10, -20750, 2000, 0x00)
    ChrTurnDirection(0x0102, 0x0101, 400)
    RemoveItem(0x0327, 1)

    ChrTalk(
        0x0102,
        (
            '#0020150530V#010F辛苦了，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150531V好像也不会有魔兽再过来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 800)

    ChrTalk(
        0x0101,
        (
            '#0010150532V#007F约修亚，对不起啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150533V是我把事情变得麻烦了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150534V#010F我倒是没关系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0102, 225, 400)

    ChrTalk(
        0x0102,
        (
            '#0020150535V#017F反正最后街道的路灯也完好无损。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150536V刚刚艾丝蒂尔摆出挥棍姿势的时候\n',
            '真是吓死我了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010150537V#008F那、那只是\n',
            '为了让精神集中而摆出的架势啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150538V我做什么事都是以华丽为宗旨的……\n',
            '怎么会做出那种野蛮的事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020150539V#018F真的吗？\n',
            '我怎么觉得你现在还想打它呢。',
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
            '#0010150540V#009F哼。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150541V不、不管怎样已经完成了委托，\n',
            '这样也就可以了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150542V#508F完成就好了，\n',
            '至于其他的小事就不用管了☆',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150543V#010F嗯，说得也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150544V那现在我们就回城里去吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150545V要向佛莱迪叔叔\n',
            '报告一下情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150546V#001F嗯⊙　走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Return()

# id: 0x0004 offset: 0x1C8D
@scena.Code('func_04_1C8D')
def func_04_1C8D():
    OP_2B(0x0006, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010150547V#002F５·４·４·８·１·８……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    PlaySE(131, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010150548V#000F……好了，打开了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150549V#502F嘿嘿嘿㈱\n',
            '我果然是聪明伶俐！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020150550V#010F艾丝蒂尔，\n',
            '我这边已经没问题了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150551V#010F慢慢来，要沉着冷静。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150552V#000F嗯，明～白。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150553V接下来是更换导力器……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010150554V#001F好了，完成～～⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1E20')
    def lambda_1E20():
        CameraMove(-203230, -10, -20760, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1E20)

    ChrWalkTo(0x0102, -202460, -10, -20750, 2000, 0x00)
    ChrTurnDirection(0x0102, 0x0101, 400)
    RemoveItem(0x0327, 1)

    ChrTalk(
        0x0102,
        (
            '#0020150530V#010F辛苦了，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150531V好像也不会有魔兽再过来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010150557V#007F呼～～～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150558V这次还真有一点紧张呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150559V#010F因为面临的是这样的状况嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150560V不过出乎我意料的是，\n',
            '艾丝蒂尔居然记得密码。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010150561V#001F呵呵呵⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150562V其实我只是凭印象随便输入的，\n',
            '没想到居然对了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0102,
        (
            '#0020150563V#017F果然。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150564V真是的，艾丝蒂尔你啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150565V#006F总之已经完成了委托，\n',
            '这样也就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150566V#010F呵呵，说的也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150567V#010F那现在我们就回城里去吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150568V#010F要向佛莱迪先生报告一下情况。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150546V#001F嗯⊙　走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Return()

# id: 0x0005 offset: 0x2113
@scena.Code('func_05_2113')
def func_05_2113():
    OP_6C(270000, 2000)

    Return()

# id: 0x0006 offset: 0x211D
@scena.Code('func_06_211D')
def func_06_211D():
    OP_A6(0x0000)
    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, -203000, 0, -34500, 3000, 0x00)
    ChrSetDirection(0x00FE, 0, 0)
    CreateThread(0x0008, 0x02, 0x00, 0x0002)
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_A6(0x0000)
    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, -203400, 0, -30900, 7000, 0x00)
    ChrSetDirection(0x00FE, 0, 0)
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Return()

# id: 0x0007 offset: 0x2171
@scena.Code('func_07_2171')
def func_07_2171():
    OP_A6(0x0001)
    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, -200300, 0, -33700, 3000, 0x00)
    ChrSetDirection(0x00FE, 0, 0)
    CreateThread(0x0009, 0x02, 0x00, 0x0002)
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    OP_A6(0x0001)
    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, -201100, 0, -30500, 7000, 0x00)
    ChrSetDirection(0x00FE, 315, 0)
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x0008 offset: 0x21C5
@scena.Code('func_08_21C5')
def func_08_21C5():
    OP_A6(0x0002)
    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, -200000, 0, -35500, 3000, 0x00)
    ChrSetDirection(0x00FE, 0, 0)
    CreateThread(0x000A, 0x02, 0x00, 0x0002)
    ClearScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    OP_A6(0x0002)
    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, -202000, 0, -31500, 7000, 0x00)
    ChrSetDirection(0x00FE, 0, 0)
    ClearScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Return()

# id: 0x0009 offset: 0x2219
@scena.Code('func_09_2219')
def func_09_2219():
    OP_A6(0x0003)
    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, -197300, 0, -34700, 3000, 0x00)
    ChrSetDirection(0x00FE, 0, 0)
    CreateThread(0x000B, 0x02, 0x00, 0x0002)
    ClearScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    OP_A6(0x0003)
    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, -200300, 0, -31700, 7000, 0x00)
    ChrSetDirection(0x00FE, 315, 0)
    ClearScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Return()

# id: 0x000A offset: 0x226D
@scena.Code('func_0A_226D')
def func_0A_226D():
    OP_A6(0x0004)
    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, -203900, 0, -26200, 3000, 0x00)
    ChrSetDirection(0x00FE, 180, 0)
    ClearScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Return()

# id: 0x000B offset: 0x2294
@scena.Code('func_0B_2294')
def func_0B_2294():
    OP_A6(0x0005)
    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, -202100, 0, -25900, 3000, 0x00)
    ChrSetDirection(0x00FE, 180, 0)
    ClearScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    Return()

# id: 0x000C offset: 0x22BB
@scena.Code('func_0C_22BB')
def func_0C_22BB():
    OP_A6(0x0004)
    ChrSetChipByIndex(0x000C, 4)
    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, -202800, 0, -29700, 6000, 0x00)
    ClearScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    ClearScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    Return()

# id: 0x000D offset: 0x22E3
@scena.Code('func_0D_22E3')
def func_0D_22E3():
    OP_A6(0x0005)
    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, -203250, 0, -22270, 6000, 0x00)
    ChrSetDirection(0x00FE, 315, 0)

    Return()

# id: 0x000E offset: 0x2307
@scena.Code('func_0E_2307')
def func_0E_2307():
    OP_A6(0x0004)
    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, -203250, 0, -22270, 6000, 0x00)
    ChrSetDirection(0x00FE, 315, 0)

    Return()

# id: 0x000F offset: 0x232B
@scena.Code('func_0F_232B')
def func_0F_232B():
    OP_A6(0x0005)
    ChrSetChipByIndex(0x000D, 5)
    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, -202800, 0, -29700, 6000, 0x00)
    ClearScenaFlags(ScenaFlag(0x0000, 5, 0x5))
    ClearScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Return()

# id: 0x0010 offset: 0x2353
@scena.Code('func_10_2353')
def func_10_2353():
    OP_A6(0x0005)
    ChrSetFlags(0x00FE, 0x0040)
    OP_92(0x0102, 0x000E, 1000, 3000, 0x00)
    ChrTurnDirection(0x0102, 0x000E, 0)
    ClearScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    Return()

# id: 0x0011 offset: 0x2374
@scena.Code('func_11_2374')
def func_11_2374():
    OP_A6(0x0005)
    ChrSetFlags(0x00FE, 0x0040)
    OP_92(0x0102, 0x0101, 1000, 3000, 0x00)
    ChrTurnDirection(0x0102, 0x0101, 0)
    ClearScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

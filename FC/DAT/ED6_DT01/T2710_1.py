import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2710_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2710_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T2710.x'
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
    OP_4A(0x000B, 255)
    OP_4A(0x000C, 255)
    OP_4A(0x000D, 255)
    ChrSetPos(0x000B, 1596, 0, 12441, 90)
    ChrSetPos(0x000C, 1513, 0, 13617, 90)
    ChrSetPos(0x000D, 909, 0, 13169, 90)

    ExecExpressionWithValue(
        0x000F,
        0x01,
        (
            (Expr.GetChrWork, 0xB, 0x1),
            (Expr.GetChrWork, 0xD, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x02,
        (
            (Expr.GetChrWork, 0xB, 0x2),
            (Expr.GetChrWork, 0xD, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x03,
        (
            (Expr.GetChrWork, 0xB, 0x3),
            (Expr.GetChrWork, 0xD, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x000F, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x000B,
        (
            '#1830170588V唔………\n',
            '完全不听别人的劝告啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1840170589V真是的，\n',
            '到底想要怎么样嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#1850170590V王国军原来都是些\n',
            '畏惧强权的家伙啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(1000)

    OP_4B(0x000B, 255)
    Sleep(50)

    OP_4B(0x000C, 255)
    Sleep(70)

    OP_4B(0x000D, 255)
    ChrSetPos(0x0101, -550, 0, 3400, 0)
    ChrSetPos(0x0102, -1460, 0, 2620, 0)
    ChrSetPos(0x0105, -1000, 0, 1420, 0)
    ChrClearFlags(0x0000, 0x0080)
    ChrClearFlags(0x0001, 0x0080)
    ChrClearFlags(0x0002, 0x0080)

    @scena.Lambda('lambda_020B')
    def lambda_020B():
        OP_94(0x01, 0x0000, 0x0000, 0x00000FA0, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_020B)

    @scena.Lambda('lambda_0221')
    def lambda_0221():
        OP_94(0x01, 0x0001, 0x0000, 0x00000FA0, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0221)

    @scena.Lambda('lambda_0237')
    def lambda_0237():
        OP_94(0x01, 0x0002, 0x0000, 0x00000FA0, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_0237)

    CameraMove(-550, 0, 8300, 3000)
    WaitForThreadExit(0x0101, 0x0001)
    ChrTurnDirection(0x0101, 0x000B, 400)
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010170591V#501F…………？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170592V那群人在那里围着看什么呢？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x000B, 400)
    ChrTurnDirection(0x0105, 0x000B, 400)

    ChrTalk(
        0x0102,
        (
            '#0020170593V#010F看起来好像只是一般的旅行者……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170594V而且…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010170595V#000F……而且什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020170596V#013F守备队的人一个都不在啊。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0102, 400)

    ChrTalk(
        0x0105,
        (
            '#0060170597V#044F啊，果然…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170598V#002F发生了什么事件吗…………？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020170599V#010F现在还不清楚呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170600V总之还是先找一个\n',
            '守备队的人来问问比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170601V#000F嗯，好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    MapClearFlags(0x00400000)
    EventEnd(0x00)

    Return()

# id: 0x0001 offset: 0x479
@scena.Code('func_01_479')
def func_01_479():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    FadeIn(2000, 0)
    MapSetFlags(0x00400000)
    FormationDelMember(0x01, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationAddMember(0x04, 0xFF)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    OP_4A(0x0008, 255)
    OP_4A(0x000E, 255)
    OP_69(0x0101, 0)
    ChrSetPos(0x0008, -4000, 0, 4000, 90)
    ChrSetPos(0x0101, -7000, 1000, 3800, 90)
    ChrSetPos(0x000E, -7000, 1000, 4900, 90)
    ChrSetPos(0x0105, -8500, 1000, 5200, 180)
    ChrSetPos(0x000B, 1596, 0, 12441, 90)
    ChrSetPos(0x000C, 1513, 0, 13617, 90)
    ChrSetPos(0x000D, 909, 0, 13169, 90)
    CreateThread(0x0008, 0x01, 0x01, 0x0002)
    CreateThread(0x0101, 0x01, 0x01, 0x0003)
    CreateThread(0x000E, 0x01, 0x01, 0x0004)
    CreateThread(0x0105, 0x01, 0x01, 0x0005)
    CameraMove(-1000, 0, 8700, 4000)
    WaitForThreadExit(0x0105, 0x0001)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#1860170643V唔…………\n',
            '好像没有什么进展啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x000F,
        0x01,
        (
            (Expr.GetChrWork, 0x8, 0x1),
            (Expr.GetChrWork, 0x101, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
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
        0x000F,
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

    OP_69(0x000F, 800)

    ChrTalk(
        0x0101,
        (
            '#0010170644V#000F那里围着的一群人\n',
            '和这件事有什么关系吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_061A')
    def lambda_061A():
        ChrTurnDirection(0x000E, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_061A)

    @scena.Lambda('lambda_0628')
    def lambda_0628():
        ChrTurnDirection(0x0105, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_0628)

    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#1860170645V他们都是被这次事件\n',
            '牵连的受害者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1860170646V麻烦的旅行者\n',
            '现在正在食堂里面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170647V#501F食堂…………？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1860170648V是啊，\n',
            '无论如何也要说服他才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1860170649V我的部下们\n',
            '正在努力劝说他呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170650V#505F说服…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170651V#002F对了，那个麻烦的旅客\n',
            '究竟是个什么样的人呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1860170652V唔，实际上他是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x000B, 0x0008, 400)
    Sleep(400)

    ChrTalk(
        0x000B,
        (
            '#1830170653V喂！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000E, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000C, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x000D, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)

    @scena.Lambda('lambda_0861')
    def lambda_0861():
        ChrTurnDirection(0x000D, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_0861)

    ChrTurnDirection(0x000C, 0x0008, 400)

    @scena.Lambda('lambda_0876')
    def lambda_0876():
        ChrTurnDirection(0x0008, 0x000B, 0)
        Yield()

        Jump('lambda_0876')

    DispatchAsync2(0x0008, 0x0001, lambda_0876)

    @scena.Lambda('lambda_0887')
    def lambda_0887():
        ChrTurnDirection(0x0101, 0x000B, 0)
        Yield()

        Jump('lambda_0887')

    DispatchAsync2(0x0101, 0x0001, lambda_0887)

    @scena.Lambda('lambda_0898')
    def lambda_0898():
        ChrTurnDirection(0x000E, 0x000B, 0)
        Yield()

        Jump('lambda_0898')

    DispatchAsync2(0x000E, 0x0001, lambda_0898)

    @scena.Lambda('lambda_08A9')
    def lambda_08A9():
        ChrTurnDirection(0x0105, 0x000B, 0)
        Yield()

        Jump('lambda_08A9')

    DispatchAsync2(0x0105, 0x0001, lambda_08A9)

    @scena.Lambda('lambda_08BA')
    def lambda_08BA():
        OP_69(0x0008, 2000)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_08BA)

    Sleep(400)

    CreateThread(0x000C, 0x01, 0x01, 0x0006)
    CreateThread(0x000D, 0x01, 0x01, 0x0007)
    ChrWalkTo(0x000B, 0, 0, 7230, 3000, 0x00)
    TerminateThread(0x0008, 0x01)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x000E, 0x01)
    TerminateThread(0x0105, 0x01)
    ChrTurnDirection(0x000B, 0x0008, 400)
    TerminateThread(0x000B, 0xFF)

    ChrTalk(
        0x000B,
        (
            '#1830170654V你是这里的负责人吧！\n',
            '快点想想办法啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x000D, 0x0001)

    ChrTalk(
        0x000D,
        (
            '#1850170655V就这样任他无理取闹吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x000C, 0x0001)

    ChrTalk(
        0x000C,
        (
            '#1840170656V王国军不是市民的朋友吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#1840170657V好歹也要做些什么吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0008,
        (
            '#1860170658V大家……大家……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x000E, -680, 0, 6220, 3000, 0x00)
    ChrSetDirection(0x000E, 0, 400)

    ChrTalk(
        0x000E,
        (
            '#0020170659V#012F大家先冷静下来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000B, 180, 0)
    ChrSetDirection(0x000C, 180, 0)
    ChrSetDirection(0x000D, 180, 0)

    @scena.Lambda('lambda_0A50')
    def lambda_0A50():
        CameraMove(-840, 0, 3830, 1000)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_0A50)

    @scena.Lambda('lambda_0A68')
    def lambda_0A68():
        OP_94(0x01, 0x000B, 0x0000, 0x000003E8, 0x00001B58, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0A68)

    @scena.Lambda('lambda_0A7E')
    def lambda_0A7E():
        OP_94(0x01, 0x000C, 0x0000, 0x000003E8, 0x00001B58, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0A7E)

    @scena.Lambda('lambda_0A94')
    def lambda_0A94():
        OP_94(0x01, 0x000D, 0x0000, 0x000003E8, 0x00001B58, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_0A94)

    OP_62(0x000E, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_0ACE')
    def lambda_0ACE():
        OP_94(0x01, 0x000E, 0x00B4, 0x000003E8, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0ACE)

    @scena.Lambda('lambda_0AE4')
    def lambda_0AE4():
        OP_94(0x01, 0x0008, 0x00B4, 0x000003E8, 0x00001B58, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0AE4)

    Sleep(200)

    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_0B11')
    def lambda_0B11():
        OP_94(0x01, 0x0101, 0x00B4, 0x000003E8, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0B11)

    ChrTalk(
        0x000B,
        (
            '#1830170660V你叫我们怎么冷静！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x000B, 0x01, 0x01, 0x0008)
    CreateThread(0x000C, 0x01, 0x01, 0x0009)
    CreateThread(0x000D, 0x01, 0x01, 0x000A)

    ChrTalk(
        0x000E,
        (
            '#0020170661V#014F我、我明白你们的心情，\n',
            '能不能不要这么靠近…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170662V#004F约、约修亚，没事吧！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000E, 0x0101, 400)

    ChrTalk(
        0x000E,
        (
            '#0020170663V#012F这、这边还行……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170664V总之，艾丝蒂尔你们\n',
            '快到食堂里看看情况吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000E, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010170665V#002F嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010170666V#002F好了，我们走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060170667V#043F……嗯、嗯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x000E, 255)
    OP_4B(0x0008, 255)
    CreateThread(0x000B, 0x00, 0x00, 0x0002)
    CreateThread(0x000C, 0x00, 0x00, 0x0002)
    CreateThread(0x000D, 0x00, 0x00, 0x0002)
    CreateThread(0x000B, 0x01, 0x01, 0x0008)
    CreateThread(0x000C, 0x01, 0x01, 0x0009)
    CreateThread(0x000D, 0x01, 0x01, 0x000A)
    ChrSetFlags(0x0008, 0x0010)
    OP_28(0x0023, 0x01, 0x1000)
    MapClearFlags(0x00400000)
    EventEnd(0x00)

    Return()

# id: 0x0002 offset: 0xCF9
@scena.Code('func_02_CF9')
def func_02_CF9():
    ChrWalkTo(0x00FE, 0, 0, 6250, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0003 offset: 0xD15
@scena.Code('func_03_D15')
def func_03_D15():
    ChrWalkTo(0x00FE, -2800, 0, 4000, 2000, 0x00)
    ChrWalkTo(0x00FE, -600, 0, 4800, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0004 offset: 0xD45
@scena.Code('func_04_D45')
def func_04_D45():
    ChrWalkTo(0x00FE, -3150, 0, 5100, 2000, 0x00)
    ChrWalkTo(0x00FE, -1800, 0, 6000, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0005 offset: 0xD75
@scena.Code('func_05_D75')
def func_05_D75():
    ChrWalkTo(0x00FE, -6950, 1000, 4300, 2000, 0x00)
    ChrWalkTo(0x00FE, -2430, 0, 4300, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0006 offset: 0xDA5
@scena.Code('func_06_DA5')
def func_06_DA5():
    Sleep(800)

    ChrWalkTo(0x000C, 670, 0, 6960, 3000, 0x00)
    ChrTurnDirection(0x000C, 0x0008, 400)
    TerminateThread(0x000C, 0xFF)

    Return()

# id: 0x0007 offset: 0xDCA
@scena.Code('func_07_DCA')
def func_07_DCA():
    Sleep(600)

    ChrWalkTo(0x000D, -800, 0, 10580, 3000, 0x00)
    ChrWalkTo(0x000D, -800, 0, 6880, 3000, 0x00)
    ChrTurnDirection(0x000D, 0x0008, 400)
    TerminateThread(0x000D, 0xFF)

    Return()

# id: 0x0008 offset: 0xE03
@scena.Code('func_08_E03')
def func_08_E03():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_E4B',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(1400)

    ChrTurnDirection(0x00FE, 0x0008, 400)
    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(1800)

    ChrTurnDirection(0x00FE, 0x000E, 400)

    Jump('func_08_E03')

    def _loc_E4B(): pass

    label('loc_E4B')

    Return()

# id: 0x0009 offset: 0xE4C
@scena.Code('func_09_E4C')
def func_09_E4C():
    Sleep(400)

    def _loc_E51(): pass

    label('loc_E51')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_E99',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(1400)

    ChrTurnDirection(0x00FE, 0x0008, 400)
    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(2000)

    ChrTurnDirection(0x00FE, 0x000E, 400)

    Jump('loc_E51')

    def _loc_E99(): pass

    label('loc_E99')

    Return()

# id: 0x000A offset: 0xE9A
@scena.Code('func_0A_E9A')
def func_0A_E9A():
    Sleep(200)

    def _loc_E9F(): pass

    label('loc_E9F')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_EE7',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(2000)

    ChrTurnDirection(0x00FE, 0x0008, 400)
    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(1400)

    ChrTurnDirection(0x00FE, 0x000E, 400)

    Jump('loc_E9F')

    def _loc_EE7(): pass

    label('loc_EE7')

    Return()

# id: 0x000B offset: 0xEE8
@scena.Code('func_0B_EE8')
def func_0B_EE8():
    MapSetFlags(0x00400000)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0105, 0x0080)
    EventBegin(0x00)
    MapClearFlags(0x00000001)
    FadeIn(2000, 0)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0009, 92630, 0, 12500, 90)
    ChrSetPos(0x0101, 90630, 0, 10900, 90)
    ChrSetPos(0x0105, 89630, 0, 10900, 90)
    ChrSetPos(0x0010, 95380, 0, 12000, 90)
    ChrSetPos(0x0012, 96610, 0, 12000, 270)
    ChrSetPos(0x0011, 94280, 0, 11200, 90)
    OP_4A(0x0012, 255)
    OP_4A(0x0009, 255)
    OP_4A(0x000A, 255)

    ExecExpressionWithValue(
        0x000F,
        0x01,
        (
            (Expr.GetChrWork, 0x10, 0x1),
            (Expr.GetChrWork, 0x12, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x02,
        (
            (Expr.GetChrWork, 0x10, 0x2),
            (Expr.GetChrWork, 0x12, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x03,
        (
            (Expr.GetChrWork, 0x10, 0x3),
            (Expr.GetChrWork, 0x12, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x000F, 0)
    OP_0D()
    OP_28(0x0023, 0x01, 0x0002)
    OP_28(0x0023, 0x01, 0x0004)

    ChrTalk(
        0x0012,
        (
            '#1880170672V…………所以说啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#1880170673V您把招待所和食堂\n',
            '全都包下来，\n',
            '难道就没有为别的客人想想吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#1880170674V为什么连这种事\n',
            '您也不能做一下让步呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0011, 0x0010, 400)

    ChrTalk(
        0x0011,
        (
            '#0660170675V#722F殿下，他说的也有道理。\n',
            '请您稍微考虑一下吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660170676V就按照预定的安排，\n',
            '我们现在回去卢安好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0011, 400)

    ChrTalk(
        0x0010,
        (
            '#0640170677V#222F给我闭嘴，菲利普！\n',
            '我在这里呆定了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640170678V#220F只有在这种地方才能和\n',
            '艾尔·雷登的瀑布做最亲密的接触呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0012, 400)
    ChrSetDirection(0x0011, 90, 0)
    OP_62(0x0012, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0012,
        (
            '#1880170679V我说你啊…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0012, 0x01, 0x01, 0x000C)
    CreateThread(0x0010, 0x01, 0x01, 0x000D)
    ChrClearFlags(0x0101, 0x0080)
    ChrClearFlags(0x0105, 0x0080)
    ChrSetFlags(0x0101, 0x0040)
    ChrSetFlags(0x0105, 0x0040)
    ChrSetFlags(0x0010, 0x0040)
    ChrSetFlags(0x0011, 0x0040)
    OP_6F(0x0001, 0)
    OP_70(0x0001, 30)
    OP_73(0x0001)

    @scena.Lambda('lambda_1219')
    def lambda_1219():
        CameraMove(92630, 0, 11500, 2000)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_1219)

    @scena.Lambda('lambda_1231')
    def lambda_1231():
        OP_94(0x01, 0x0105, 0x0000, 0x00000BB8, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_1231)

    OP_94(0x01, 0x0101, 0x0000, 0x000007D0, 0x000007D0, 0x00)

    @scena.Lambda('lambda_1256')
    def lambda_1256():
        ChrWalkTo(0x0101, 92630, 0, 11500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1256)

    WaitForThreadExit(0x0105, 0x0001)
    ChrWalkTo(0x0105, 92630, 0, 10500, 2000, 0x00)
    ChrTurnDirection(0x0101, 0x0010, 400)
    ChrSetDirection(0x0105, 90, 400)
    OP_72(0x0001, 0x0800)
    PlaySE(7, 0x00, 0x64)
    OP_6F(0x0001, 30)
    OP_70(0x0001, 0)
    OP_73(0x0001)
    OP_71(0x0001, 0x0800)
    Sleep(400)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010170680V#004F…………咦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170681V我说是谁呢，\n',
            '这不是任性公爵吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0009,
        (
            '#1870170682V…………嗯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1870170683V哦…………\n',
            '是游击士啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_138E')
    def lambda_138E():
        ChrTurnDirection(0x0105, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_138E)

    ChrTurnDirection(0x0101, 0x0009, 400)

    ChrTalk(
        0x0009,
        (
            '#1870170684V等你们很久了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170685V#509F超级麻烦的旅行者……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170686V难道就是他？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1870170687V除了他还有谁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_142A')
    def lambda_142A():
        ChrSetDirection(0x0105, 90, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_142A)

    ChrTurnDirection(0x0101, 0x0010, 400)
    OP_62(0x0101, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010170688V#007F呼，伤脑筋啊…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170689V其实刚才看到\n',
            '和队长谈话的那个人，\n',
            '就应该想到是他……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0010, 400)

    ChrTalk(
        0x0009,
        (
            '#1870170690V那个公爵\n',
            '说他要在这里留宿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1870170691V还放出话来说要把\n',
            '这里的招待所和食堂全部包下来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170692V#509F简直就是肆无忌惮嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060170693V#047F呼，真是的……\n',
            '好一个麻烦的人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0009,
        (
            '#1870170694V难道就因为王族的客人要留宿，\n',
            '就把一般的旅行者全都赶到外面\n',
            '去风餐露宿吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1870170695V…………事情就是这样的，\n',
            '希望你们能够主持公道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1870170696V无论怎样也要\n',
            '说服公爵回卢安去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_168C')
    def lambda_168C():
        ChrTurnDirection(0x0105, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_168C)

    ChrTurnDirection(0x0101, 0x0009, 400)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010170697V#004F要、要我去说服！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1870170698V和别人交涉\n',
            '不也属于游击士的工作之一吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1870170699V而我们这些士兵\n',
            '只受过剑和枪的训练。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170700V#004F我、我也没有\n',
            '受过与交涉相关的训练啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170701V#503F如果他之前\n',
            '稍微教我一些秘诀之类的，\n',
            '也许我还能胜任这种事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170702V（这种事情平常\n',
            '　都是交给约修亚的啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060170703V#043F可是艾丝蒂尔。\n',
            '我们不能这样放任不管啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010170704V#505F唔………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1870170705V那就拜托了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)

    ChrTalk(
        0x0101,
        (
            '#0010170706V#007F唉…………\n',
            '没得选择了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170707V呼，只有硬着头皮上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1870170708V哦，听你这么说\n',
            '我就有信心了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170709V#509F管他呢，乱说一气吧，\n',
            '我可是完全没有自信啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170710V…………最好不要对我抱有希望。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060170711V#040F艾丝蒂尔，你一定能行的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010170712V#002F嗯、嗯，谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 90, 400)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010170713V#582F好的，不管成功与否，\n',
            '我尽全力就是了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    @scena.Lambda('lambda_1A3B')
    def lambda_1A3B():
        ChrTurnDirection(0x0009, 0x0101, 0)
        Yield()

        Jump('lambda_1A3B')

    DispatchAsync2(0x0009, 0x0001, lambda_1A3B)

    @scena.Lambda('lambda_1A4C')
    def lambda_1A4C():
        ChrTurnDirection(0x0105, 0x0101, 0)
        Yield()

        Jump('lambda_1A4C')

    DispatchAsync2(0x0105, 0x0001, lambda_1A4C)

    @scena.Lambda('lambda_1A5D')
    def lambda_1A5D():
        ChrTurnDirection(0x000A, 0x0101, 0)
        Yield()

        Jump('lambda_1A5D')

    DispatchAsync2(0x000A, 0x0001, lambda_1A5D)

    ExecExpressionWithValue(
        0x000F,
        0x01,
        (
            (Expr.GetChrWork, 0x10, 0x1),
            (Expr.PushLong, 0x17494),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x02,
        (
            (Expr.GetChrWork, 0x10, 0x2),
            (Expr.PushLong, 0x0),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x03,
        (
            (Expr.GetChrWork, 0x10, 0x3),
            (Expr.PushLong, 0x32C8),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_1AB0')
    def lambda_1AB0():
        OP_69(0x000F, 2000)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_1AB0)

    ChrWalkTo(0x0101, 93400, 0, 12300, 2000, 0x00)
    ChrWalkTo(0x0101, 95380, 0, 13000, 2000, 0x00)
    ChrTurnDirection(0x0101, 0x0010, 400)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x0105, 0xFF)
    TerminateThread(0x000A, 0xFF)
    OP_62(0x0011, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x0011, 0x0101, 400)

    ChrTalk(
        0x0011,
        (
            '#0660170714V#721F哦？你好像之前的那位……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0011, 400)

    ChrTalk(
        0x0101,
        (
            '#0010170715V#506F嗯，好久不见了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170716V不过一见面又有大麻烦了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0010, 0xFF)
    TerminateThread(0x0012, 0xFF)
    MapClearFlags(0x00400000)
    OP_62(0x0010, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0012, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)

    @scena.Lambda('lambda_1BC8')
    def lambda_1BC8():
        ChrTurnDirection(0x0012, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_1BC8)

    ChrTurnDirection(0x0010, 0x0011, 400)

    ChrTalk(
        0x0010,
        (
            '#0640170717V#220F嗯？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640170718V菲利普，你在和谁说话？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0010, 400)

    ChrTalk(
        0x0101,
        (
            '#0010170719V#002F（总、总之开始是很关键的。）',
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
            TXT(0x00, '【嗨嗨～公爵大人！】\n'),
            TXT(0x01, '【公爵大人，我来恭迎您的大驾。】\n'),
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
        (0x00000000, 'loc_1CD7'),
        (0x00000001, 'loc_23A6'),
        (-1, 'loc_2DA1'),
    )

    def _loc_1CD7(): pass

    label('loc_1CD7')

    OP_28(0x0023, 0x01, 0x2000)

    ChrTalk(
        0x0101,
        (
            '#0010170720V#508F嗨嗨～公爵大人！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0101, 400)

    ChrTalk(
        0x0010,
        (
            '#0640170721V#222F…………哼。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640170722V竟然用那样的口气\n',
            '来称呼即将成为国王的我……\n',
            '真是个无知至极的家伙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640170723V#220F哼，算了……\n',
            '…………有什么事情吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170724V#000F嗯，\n',
            '我是来迎接公爵您的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0640170725V#223F迎接我？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640170726V我不记得\n',
            '下过这样的命令啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640170727V究竟是从哪里来迎接的呢？\n',
            '　',
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
            TXT(0x00, '【市长官邸啊。】\n'),
            TXT(0x01, '【布朗西酒店啊。】\n'),
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
        (0x00000000, 'loc_1ECA'),
        (0x00000001, 'loc_1F23'),
        (-1, 'loc_1F7C'),
    )

    def _loc_1ECA(): pass

    label('loc_1ECA')

    ChrTalk(
        0x0101,
        (
            '#0010170728V#000F市长官邸啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170729V戴尔蒙市长委托我，\n',
            '让我来迎接您回去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F7C')

    def _loc_1F23(): pass

    label('loc_1F23')

    ChrTalk(
        0x0101,
        (
            '#0010170730V#000F布朗西酒店啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170731V酒店老板委托我，\n',
            '让我来迎接您回去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F7C')

    def _loc_1F7C(): pass

    label('loc_1F7C')

    ChrTalk(
        0x0010,
        (
            '#0640170732V#220F哼，是这样啊。\n',
            '辛苦你了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640170733V不过，今晚我不准备回卢安。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640170734V我决定在艾尔·雷登留宿一晚。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170735V#000F可是今晚市长官邸\n',
            '会举办一场豪华晚宴哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170736V如果身为未来国王的您能参加，\n',
            '大家一定会很高兴的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0640170737V#220F啊啊，\n',
            '晚宴什么时候举行都可以啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640170738V我对晚宴之类的活动已经有些厌倦了。\n',
            '今晚是绝对不会去的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640170739V#225F在这个关所住下来，\n',
            '然后悠然自得地远眺瀑布，\n',
            '更是一件有趣开心的事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640170740V哈哈哈…………\n',
            '我的情操真是高尚啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010170741V#004F但、但是…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170742V未来的国王要在这种简陋的地方留宿，\n',
            '是不是有些太～委屈了呢？\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170743V而且也没有\n',
            '豪华的料理来招待您…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0640170744V#223F哦，这也有道理。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640170745V#220F虽然你的好心让我有一些动摇……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640170746V…………菲利普！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_22C1')
    def lambda_22C1():
        ChrTurnDirection(0x0012, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_22C1)

    ChrTurnDirection(0x0011, 0x0010, 400)

    ChrTalk(
        0x0011,
        (
            '#0660170747V#720F是、是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0011, 400)

    ChrTalk(
        0x0010,
        (
            '#0640170748V#220F马上做好留宿的准备。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640170749V和卢安的酒店联系，\n',
            '叫他们把床给我送来这里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640170750V还有，不要忘记了。\n',
            '叫他们把一流的厨师和料理也一起送来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(1, 0x000F)

    Jump('loc_2DA1')

    def _loc_23A6(): pass

    label('loc_23A6')

    ChrTalk(
        0x0101,
        (
            '#0010170751V#500F公爵大人，我来恭迎您的大驾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0101, 400)

    ChrTalk(
        0x0010,
        (
            '#0640170725V#223F迎接我？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640170726V我不记得\n',
            '下过这样的命令啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640170727V究竟是从哪里来迎接的呢？\n',
            '　',
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
            TXT(0x00, '【是市长官邸。】\n'),
            TXT(0x01, '【是布朗西酒店。】\n'),
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
        (0x00000000, 'loc_24C6'),
        (0x00000001, 'loc_251F'),
        (-1, 'loc_2578'),
    )

    def _loc_24C6(): pass

    label('loc_24C6')

    ChrTalk(
        0x0101,
        (
            '#0010170755V#000F市长官邸啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170756V戴尔蒙市长委托我，\n',
            '让我来迎接您回去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2578')

    def _loc_251F(): pass

    label('loc_251F')

    ChrTalk(
        0x0101,
        (
            '#0010170757V#000F布朗西酒店啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170758V酒店老板委托我，\n',
            '让我来迎接您回去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2578')

    def _loc_2578(): pass

    label('loc_2578')

    ChrTalk(
        0x0010,
        (
            '#0640170759V#220F哦，是吗。\n',
            '办事很细心，值得称赞。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640170733V不过，今晚我不准备回卢安。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640170734V我决定在艾尔·雷登留宿一晚。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170762V#002F（……关键的时刻到了。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170763V（趁这个时候\n',
            '　顺着他的话劝服他……）',
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
            TXT(0x00, '【啊！在这样简陋的地方……】\n'),
            TXT(0x01, '【今晚市长官邸会有豪华晚宴……】\n'),
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
        (0x00000000, 'loc_26F6'),
        (0x00000001, 'loc_2A05'),
        (-1, 'loc_2D9E'),
    )

    def _loc_26F6(): pass

    label('loc_26F6')

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010170764V#004F……啊！\n',
            '难道公爵您要在这样简陋的地方留宿？\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170765V这个地方怎么看，\n',
            '都和贵为未来国王的您极不相称啊……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0640170766V#225F哼，\n',
            '这种事不用你说我也很清楚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640170767V我本来就不觉得\n',
            '这个地方与我相称。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640170768V只是觉得偶尔体验一下\n',
            '庶民生活也是很有趣的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170769V#003F既然您觉得可以，那就算了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170770V不过，留在这里就没有\n',
            '豪华的料理可以款待您了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170771V而且很明显…………\n',
            '这里不太卫生啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0012, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0012,
        (
            '#1880170772V（……怒。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0640170773V#223F……是、是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0010, 180, 400)

    ChrTalk(
        0x0010,
        (
            '#0640170774V#222F唔、唔，经你这么一说，\n',
            '好像这里到处都不太干净啊…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640170775V唔…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640170776V果然不能在这种地方留宿。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170777V#002F（好，就差最后一步了！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(1, 0x000E)

    Jump('loc_2D9E')

    def _loc_2A05(): pass

    label('loc_2A05')

    ChrTalk(
        0x0101,
        (
            '#0010170778V#000F今晚市长官邸会举办一场豪华晚宴哦。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170779V如果身为未来国王的您能参加，\n',
            '大家一定会很高兴的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0640170737V#220F啊啊，\n',
            '晚宴什么时候举行都可以啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640170738V我对晚宴之类的活动已经有些厌倦了。\n',
            '今晚是绝对不会去的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640170739V#225F在这个关所住下来，\n',
            '然后悠然自得地远眺瀑布，\n',
            '更是一件有趣开心的事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640170783V呵呵呵……\n',
            '我的情操真是高尚啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010170784V#004F哎～可、可是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170785V这个地方怎么看，\n',
            '都和贵为未来国王的您极不相称啊……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170786V而且庶民吃的饭菜\n',
            '也肯定不合您的口味啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0640170744V#223F哦，这也有道理。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640170745V#220F虽然你的好心让我有一些动摇……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640170746V…………菲利普！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2CB9')
    def lambda_2CB9():
        ChrTurnDirection(0x0012, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_2CB9)

    ChrTurnDirection(0x0011, 0x0010, 400)

    ChrTalk(
        0x0011,
        (
            '#0660170747V#720F是、是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0011, 400)

    ChrTalk(
        0x0010,
        (
            '#0640170748V#220F马上做好留宿的准备。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640170749V和卢安的酒店联系，\n',
            '叫他们把床给我送来这里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640170750V还有，不要忘记了。\n',
            '叫他们把一流的厨师和料理也一起送来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(1, 0x000F)

    Jump('loc_2D9E')

    def _loc_2D9E(): pass

    label('loc_2D9E')

    Jump('loc_2DA1')

    def _loc_2DA1(): pass

    label('loc_2DA1')

    MapClearFlags(0x00400000)
    EventEnd(0x00)
    MapSetFlags(0x00000001)

    Return()

# id: 0x000C offset: 0x2DAE
@scena.Code('func_0C_2DAE')
def func_0C_2DAE():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2DD1',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(4000)

    Jump('func_0C_2DAE')

    def _loc_2DD1(): pass

    label('loc_2DD1')

    Return()

# id: 0x000D offset: 0x2DD2
@scena.Code('func_0D_2DD2')
def func_0D_2DD2():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2DFA',
    )

    Sleep(2000)

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(2000)

    Jump('func_0D_2DD2')

    def _loc_2DFA(): pass

    label('loc_2DFA')

    Return()

# id: 0x000E offset: 0x2DFB
@scena.Code('func_0E_2DFB')
def func_0E_2DFB():
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
            TXT(0x00, '【那我们就回卢安吧。】\n'),
            TXT(0x01, '【啊，大人的脚下是……】\n'),
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
        (0x00000000, 'loc_2E7C'),
        (0x00000001, 'loc_30C8'),
        (-1, 'loc_35B9'),
    )

    def _loc_2E7C(): pass

    label('loc_2E7C')

    ChrTalk(
        0x0101,
        (
            '#0010170829V#006F那我们就回卢安吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170830V趁现在天色还早，快点回去吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0101, 400)

    ChrTalk(
        0x0010,
        (
            '#0640170831V#223F嗯？你说什么啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640170832V谁说过要回卢安啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170833V#004F…………啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170834V可、可是刚才\n',
            '您不是说这种地方不能留宿的吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0640170835V#220F哼，那只是看你那么费心，\n',
            '而随便说说罢了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640170746V…………菲利普！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2FE3')
    def lambda_2FE3():
        ChrTurnDirection(0x0012, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_2FE3)

    ChrTurnDirection(0x0011, 0x0010, 400)

    ChrTalk(
        0x0011,
        (
            '#0660170747V#720F是、是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0011, 400)

    ChrTalk(
        0x0010,
        (
            '#0640170748V#220F马上做好留宿的准备。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640170749V和卢安的酒店联系，\n',
            '叫他们把床给我送来这里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640170750V还有，不要忘记了。\n',
            '叫他们把一流的厨师和料理也一起送来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(1, 0x000F)

    Jump('loc_35B9')

    def _loc_30C8(): pass

    label('loc_30C8')

    OP_28(0x0023, 0x01, 0x0008)

    ChrTalk(
        0x0101,
        (
            '#0010170841V#004F啊，大人的脚下是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0010, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    ChrTurnDirection(0x0010, 0x0101, 400)

    ChrTalk(
        0x0010,
        (
            '#0640170842V#223F嗯？我的脚下怎么了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170843V#509F……有一只蟑螂。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0010, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrJumpToRelative(0x0010, 0, 0, 0, 800, 12000)

    @scena.Lambda('lambda_319F')
    def lambda_319F():
        ChrTurnDirection(0x0009, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_319F)

    @scena.Lambda('lambda_31AD')
    def lambda_31AD():
        ChrTurnDirection(0x0105, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_31AD)

    ChrTurnDirection(0x0012, 0x0010, 400)

    ChrTalk(
        0x0010,
        (
            '#0640170844V#226F啊、啊呀呀呀！\n',
            '菲、菲利～普！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0660170845V#723F是、是的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0010, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrSetDirection(0x0010, 225, 800)
    ChrSetDirection(0x0010, 315, 800)
    ChrSetDirection(0x0010, 135, 800)

    ChrTalk(
        0x0010,
        (
            '#0640170846V#226F呜，虫子在哪里！\n',
            '究竟在哪里啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640170847V快、快给我杀死它们～～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170848V#507F哎～呀，\n',
            '庶民的食堂果然不卫生啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170849V说不定哪里还会\n',
            '冒出一只大魔兽来哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0010, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrJumpToRelative(0x0010, 0, 0, 0, 800, 12000)

    ChrTalk(
        0x0010,
        (
            '#0640170850V#228F啊、啊呀呀！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0011, 0)

    ChrTalk(
        0x0010,
        (
            '#0640170851V#226F不、不能这样！\n',
            '菲利普，我们回去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0011, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0011,
        (
            '#0660170852V#723F是、是的！\n',
            '这就最好不过了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_33E2')
    def lambda_33E2():
        ChrTurnDirection(0x0012, 0x0010, 0)
        Yield()

        Jump('lambda_33E2')

    DispatchAsync2(0x0012, 0x0001, lambda_33E2)

    @scena.Lambda('lambda_33F3')
    def lambda_33F3():
        ChrTurnDirection(0x0009, 0x0010, 0)
        Yield()

        Jump('lambda_33F3')

    DispatchAsync2(0x0009, 0x0001, lambda_33F3)

    @scena.Lambda('lambda_3404')
    def lambda_3404():
        ChrTurnDirection(0x0101, 0x0010, 0)
        Yield()

        Jump('lambda_3404')

    DispatchAsync2(0x0101, 0x0001, lambda_3404)

    @scena.Lambda('lambda_3415')
    def lambda_3415():
        ChrTurnDirection(0x0011, 0x0010, 0)
        Yield()

        Jump('lambda_3415')

    DispatchAsync2(0x0011, 0x0001, lambda_3415)

    @scena.Lambda('lambda_3426')
    def lambda_3426():
        ChrTurnDirection(0x000A, 0x0010, 0)
        Yield()

        Jump('lambda_3426')

    DispatchAsync2(0x000A, 0x0001, lambda_3426)

    ChrWalkTo(0x0010, 93700, 0, 12000, 5000, 0x00)
    OP_6F(0x0001, 0)
    OP_70(0x0001, 30)
    CreateThread(0x0105, 0x01, 0x01, 0x0014)
    CreateThread(0x0011, 0x01, 0x01, 0x0015)
    OP_62(0x000A, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_3479')
    def lambda_3479():
        ChrWalkTo(0x000A, 92580, 0, 8700, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_3479)

    ChrWalkTo(0x0010, 90700, 0, 10500, 5000, 0x00)
    ChrSetFlags(0x0010, 0x0080)
    WaitForThreadExit(0x0011, 0x0001)
    ChrTurnDirection(0x0011, 0x0101, 400)

    ChrTalk(
        0x0011,
        (
            '#0660170819V#720F……给你们添麻烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_73(0x0001)
    TerminateThread(0x0012, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0105, 0xFF)
    TerminateThread(0x000A, 0xFF)

    @scena.Lambda('lambda_34FB')
    def lambda_34FB():
        ChrTurnDirection(0x0012, 0x0011, 0)
        Yield()

        Jump('lambda_34FB')

    DispatchAsync2(0x0012, 0x0001, lambda_34FB)

    @scena.Lambda('lambda_350C')
    def lambda_350C():
        ChrTurnDirection(0x0009, 0x0011, 0)
        Yield()

        Jump('lambda_350C')

    DispatchAsync2(0x0009, 0x0001, lambda_350C)

    @scena.Lambda('lambda_351D')
    def lambda_351D():
        ChrTurnDirection(0x0101, 0x0011, 0)
        Yield()

        Jump('lambda_351D')

    DispatchAsync2(0x0101, 0x0001, lambda_351D)

    @scena.Lambda('lambda_352E')
    def lambda_352E():
        ChrTurnDirection(0x0105, 0x0011, 0)
        Yield()

        Jump('lambda_352E')

    DispatchAsync2(0x0105, 0x0001, lambda_352E)

    @scena.Lambda('lambda_353F')
    def lambda_353F():
        ChrTurnDirection(0x000A, 0x0011, 0)
        Yield()

        Jump('lambda_353F')

    DispatchAsync2(0x000A, 0x0001, lambda_353F)

    ChrTalk(
        0x0101,
        (
            '#0010170854V#001F嗯，这就可以放心了⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0011, 90700, 0, 10500, 5000, 0x00)
    ChrSetFlags(0x0011, 0x0080)
    FadeOut(2000, 0, -1)
    OP_0D()
    TerminateThread(0x0012, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0105, 0xFF)
    TerminateThread(0x000A, 0xFF)
    NewScene('ED6_DT01/T2710._SN', 102, 0, 0)
    IdleLoop()

    Jump('loc_35B9')

    def _loc_35B9(): pass

    label('loc_35B9')

    Return()

# id: 0x000F offset: 0x35BA
@scena.Code('func_0F_35BA')
def func_0F_35BA():
    OP_28(0x0023, 0x01, 0x0010)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010170794V#004F啊，什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0640170795V#220F从现在开始，让士兵到这里集中，\n',
            '做食堂的大扫除。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0660170796V#722F大人，这是不是有点……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0640170797V#224F给我闭嘴，菲利普！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640170798V作为未来国王的我要在这里留宿！\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640170799V做准备是理所当然的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010170800V#002F请您不要太过分了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0101, 400)

    ChrTalk(
        0x0010,
        (
            '#0640170801V#222F唔……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170802V#009F你可不要敬酒不吃吃罚酒……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170803V没有菲利普先生在，\n',
            '你根本就什么也做不了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x01, 0x2000)"),
            Expr.Return,
        ),
        'loc_384A',
    )

    OP_62(0x0105, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0105,
        (
            '#0060170804V#045F（哎呀，艾丝蒂尔发怒了……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060170805V（都说出这种话来了……）\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_388D')

    def _loc_384A(): pass

    label('loc_384A')

    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0105,
        (
            '#0060170806V#044F艾、艾丝蒂尔！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_388D(): pass

    label('loc_388D')

    ChrTalk(
        0x0010,
        (
            '#0640170807V#222F可恶……\n',
            '你、你不知道就不要乱说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0009, 400)

    ChrTalk(
        0x0010,
        (
            '#0640170808V#224F喂、喂，那边的士兵！\n',
            '给我行动起来！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640170809V快把这个家伙给我赶出去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170810V#582F要赶出去的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 45, 1000)
    ChrSetDirection(0x0101, 315, 1000)
    ChrSetDirection(0x0101, 180, 1000)
    ChrSetChipByIndex(0x0101, 9)

    ChrTalk(
        0x0101,
        (
            '#0010170811V#005F是你啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3990')
    def lambda_3990():
        ChrTurnDirection(0x0012, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_3990)

    ChrTurnDirection(0x0010, 0x0101, 0)
    OP_62(0x0010, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(100)

    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0011, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0012, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrJumpToRelative(0x0010, 0, 0, 0, 800, 12000)
    Sleep(400)

    OP_62(0x0010, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_3A62')
    def lambda_3A62():
        OP_94(0x01, 0x0010, 0x00B4, 0x00000578, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_3A62)

    WaitForThreadExit(0x0010, 0x0001)

    ChrTalk(
        0x0010,
        (
            '#0640170812V#226F啊啊，好可怕啊！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060170813V#043F啊，艾丝蒂尔！不行！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170814V#005F喝啊～～～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x000A, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_3B18')
    def lambda_3B18():
        ChrTurnDirection(0x0009, 0x0101, 0)
        Yield()

        Jump('lambda_3B18')

    DispatchAsync2(0x0009, 0x0001, lambda_3B18)

    @scena.Lambda('lambda_3B29')
    def lambda_3B29():
        ChrTurnDirection(0x000A, 0x0101, 0)
        Yield()

        Jump('lambda_3B29')

    DispatchAsync2(0x000A, 0x0001, lambda_3B29)

    CreateThread(0x0010, 0x01, 0x01, 0x0010)
    CreateThread(0x0011, 0x02, 0x01, 0x0011)
    CreateThread(0x0101, 0x01, 0x01, 0x0012)
    CreateThread(0x0105, 0x01, 0x01, 0x0013)

    @scena.Lambda('lambda_3B56')
    def lambda_3B56():
        ChrTurnDirection(0x0012, 0x0010, 0)
        Yield()

        Jump('lambda_3B56')

    DispatchAsync2(0x0012, 0x0001, lambda_3B56)

    @scena.Lambda('lambda_3B67')
    def lambda_3B67():
        ChrTurnDirection(0x0011, 0x0010, 0)
        Yield()

        Jump('lambda_3B67')

    DispatchAsync2(0x0011, 0x0001, lambda_3B67)

    FadeOut(2000, 0, -1)
    OP_0D()
    TerminateThread(0x0012, 0xFF)
    TerminateThread(0x0011, 0xFF)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0105, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    ChrSetChipByIndex(0x0101, 65535)
    ChrClearFlags(0x000E, 0x0080)
    Sleep(1000)

    FadeIn(2000, 0)
    ChrSetPos(0x0010, 95380, 0, 12000, 90)
    ChrSetPos(0x0011, 94280, 0, 11200, 90)
    ChrSetPos(0x0101, 92630, 0, 13400, 135)
    ChrSetPos(0x000A, 93400, 0, 13300, 315)
    ChrSetPos(0x0009, 92710, 0, 12520, 0)
    ChrSetPos(0x0012, 93420, 0, 12620, 315)
    ChrSetPos(0x000E, 96610, 0, 12500, 270)
    ChrSetPos(0x0105, 96610, 0, 11500, 270)
    TerminateThread(0x000E, 0xFF)
    CreateThread(0x0101, 0x01, 0x01, 0x0016)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x0010,
        (
            '#0640170815V#220F……呼，如果是这样，\n',
            '那就没办法了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640170816V呵哈哈，\n',
            '想怎么做就怎么做，怎么做都行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640170817V菲利普，\n',
            '我们回卢安吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0660170818V#720F好、好的！\n',
            '这就最好不过了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3D14')
    def lambda_3D14():
        ChrTurnDirection(0x0101, 0x0010, 0)
        Yield()

        Jump('lambda_3D14')

    DispatchAsync2(0x0101, 0x0003, lambda_3D14)

    ChrSetFlags(0x0010, 0x0040)
    ChrSetFlags(0x0011, 0x0040)
    ChrWalkTo(0x0010, 93700, 0, 12000, 3000, 0x00)
    ChrWalkTo(0x0010, 92600, 0, 10900, 3000, 0x00)
    CreateThread(0x0011, 0x01, 0x01, 0x0015)
    OP_6F(0x0001, 0)
    OP_70(0x0001, 30)
    OP_73(0x0001)
    ChrWalkTo(0x0010, 90700, 0, 10900, 3000, 0x00)
    ChrSetFlags(0x0010, 0x0008)
    ChrTurnDirection(0x0011, 0x000E, 400)

    ChrTalk(
        0x0011,
        (
            '#0660170819V#720F……给你们添麻烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000E, 0x0011, 400)

    ChrTalk(
        0x000E,
        (
            '#0020170820V#015F这话该我们说才是，\n',
            '刚才非常抱歉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170821V还好公爵没有受伤。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0011, 0x0105, 400)

    ChrTalk(
        0x0011,
        (
            '#0660170822V#720F多亏了这位小姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660170823V差一点就闹到不可收拾了，\n',
            '幸好她及时阻止住了大人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0640170824V菲利普！\n',
            '你还在做什么！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0660170825V#720F那我就告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0011, 90700, 0, 10900, 5000, 0x00)
    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0010, 0x0080)
    OP_72(0x0001, 0x0800)
    PlaySE(7, 0x00, 0x64)
    OP_6F(0x0001, 30)
    OP_70(0x0001, 0)
    OP_73(0x0001)
    OP_71(0x0001, 0x0800)

    ChrTalk(
        0x000E,
        (
            '#0020170826V#017F……………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170827V呼……终于……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060170828V#045F哈…………\n',
            '已经回去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x0012, 0xFF)
    TerminateThread(0x000A, 0xFF)
    ChrSetFlags(0x000E, 0x0080)
    NewScene('ED6_DT01/T2710._SN', 102, 0, 0)
    IdleLoop()

    Return()

# id: 0x0010 offset: 0x3FA9
@scena.Code('func_10_3FA9')
def func_10_3FA9():
    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrWalkTo(0x00FE, 94900, 0, 8100, 2000, 0x00)
    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrTurnDirection(0x00FE, 0x0101, 400)

    Return()

# id: 0x0011 offset: 0x3FE9
@scena.Code('func_11_3FE9')
def func_11_3FE9():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_400C',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    Jump('func_11_3FE9')

    def _loc_400C(): pass

    label('loc_400C')

    Return()

# id: 0x0012 offset: 0x400D
@scena.Code('func_12_400D')
def func_12_400D():
    ChrSetChipByIndex(0x0101, 10)
    ChrWalkTo(0x00FE, 94900, 0, 9500, 2000, 0x00)

    Return()

# id: 0x0013 offset: 0x4027
@scena.Code('func_13_4027')
def func_13_4027():
    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrWalkTo(0x00FE, 94100, 0, 10280, 3000, 0x00)
    ChrWalkTo(0x00FE, 95000, 0, 8880, 3000, 0x00)
    ChrTurnDirection(0x00FE, 0x0101, 400)

    Return()

# id: 0x0014 offset: 0x4069
@scena.Code('func_14_4069')
def func_14_4069():
    ChrSetDirection(0x00FE, 0, 400)
    OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x000007D0, 0x00)

    @scena.Lambda('lambda_4085')
    def lambda_4085():
        ChrTurnDirection(0x0105, 0x0010, 0)
        Yield()

        Jump('lambda_4085')

    DispatchAsync2(0x0105, 0x0002, lambda_4085)

    Return()

# id: 0x0015 offset: 0x4091
@scena.Code('func_15_4091')
def func_15_4091():
    ChrSetDirection(0x00FE, 270, 400)
    OP_94(0x01, 0x00FE, 0x0000, 0x00000064, 0x000007D0, 0x00)
    Sleep(1000)

    Return()

# id: 0x0016 offset: 0x40AD
@scena.Code('func_16_40AD')
def func_16_40AD():
    CreateThread(0x00FE, 0x00, 0x00, 0x0002)
    OP_4B(0x0009, 255)
    OP_4B(0x0012, 255)
    OP_4B(0x000A, 255)
    def _loc_40C0(): pass

    label('loc_40C0')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4225',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0012, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x000A, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_4117')
    def lambda_4117():
        OP_94(0x01, 0x00FE, 0x0000, 0x0000012C, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_4117)

    Sleep(200)

    @scena.Lambda('lambda_4132')
    def lambda_4132():
        OP_94(0x01, 0x00FE, 0x00B4, 0x0000012C, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_4132)

    @scena.Lambda('lambda_4148')
    def lambda_4148():
        OP_94(0x01, 0x00FE, 0x00B4, 0x0000012C, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_4148)

    Sleep(200)

    @scena.Lambda('lambda_4163')
    def lambda_4163():
        OP_94(0x01, 0x0012, 0x00B4, 0x0000012C, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_4163)

    Sleep(2000)

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0012, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x000A, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_41C6')
    def lambda_41C6():
        OP_94(0x01, 0x00FE, 0x00B4, 0xFFFFFED4, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_41C6)

    @scena.Lambda('lambda_41DC')
    def lambda_41DC():
        OP_94(0x01, 0x00FE, 0x00B4, 0xFFFFFED4, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_41DC)

    @scena.Lambda('lambda_41F2')
    def lambda_41F2():
        OP_94(0x01, 0x0012, 0x00B4, 0xFFFFFED4, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_41F2)

    Sleep(200)

    @scena.Lambda('lambda_420D')
    def lambda_420D():
        OP_94(0x01, 0x00FE, 0x0000, 0xFFFFFED4, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_420D)

    Sleep(2000)

    Jump('loc_40C0')

    def _loc_4225(): pass

    label('loc_4225')

    Return()

# id: 0x0017 offset: 0x4226
@scena.Code('func_17_4226')
def func_17_4226():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    FadeIn(2000, 0)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetPos(0x000B, -770, 0, 21500, 0)
    ChrSetPos(0x000C, -770, 0, 22500, 0)
    ChrSetPos(0x000D, -770, 0, 23500, 0)
    ChrSetPos(0x0101, -1000, 0, 9300, 180)
    ChrSetPos(0x0105, 0, 0, 9300, 180)
    ChrSetPos(0x0102, -1800, 0, 7800, 90)
    ChrSetPos(0x0008, 0, 0, 6500, 0)
    ChrSetPos(0x0009, -1000, 0, 5500, 0)
    ChrSetPos(0x0012, -2000, 0, 6500, 90)
    ChrSetPos(0x000A, -4800, 0, 7900, 90)

    ExecExpressionWithValue(
        0x000F,
        0x01,
        (
            (Expr.GetChrWork, 0x102, 0x1),
            (Expr.GetChrWork, 0x101, 0x1),
            Expr.Add,
            (Expr.GetChrWork, 0x8, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x3),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x02,
        (
            (Expr.GetChrWork, 0x102, 0x2),
            (Expr.GetChrWork, 0x101, 0x2),
            Expr.Add,
            (Expr.GetChrWork, 0x8, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x3),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x03,
        (
            (Expr.GetChrWork, 0x102, 0x3),
            (Expr.GetChrWork, 0x101, 0x3),
            Expr.Add,
            (Expr.GetChrWork, 0x8, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x3),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x000F, 0)
    OP_4A(0x0008, 255)
    OP_4A(0x0009, 255)
    OP_4A(0x0012, 255)
    OP_4A(0x000A, 255)
    OP_0D()

    ChrTalk(
        0x0009,
        (
            '#1870170855V……就是这样，\n',
            '这位小姑娘一句话就把他摆平了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1870170856V说那家伙的脚下\n',
            '有一只蟑螂。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1870170857V一听到这句话，\n',
            '那家伙的脸色都吓白了……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1870170858V呀～\n',
            '好久都没有这么痛快过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#1860170859V唔，是这样啊。\n',
            '听到你们所说的我就放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1860170860V我开始还有些担心\n',
            '你们会用强制性的手段呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1860170861V从基恩茨的话来看，\n',
            '你们处理得非常好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0012, 0x0101, 400)

    ChrTalk(
        0x0012,
        (
            '#1880170862V刚才我听你说了些食堂的坏话，\n',
            '确实还很生气呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170863V#506F啊、啊哈哈，真是不好意思呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170864V为了让公爵动摇，\n',
            '只有说些谎话了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020170865V#011F不过很让我意外哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170866V艾丝蒂尔竟然可以处理得那么恰当。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010170867V#502F嘿嘿，我可是在关键时刻\n',
            '就能发挥出真正的实力。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170868V嗯，说实话，\n',
            '刚才我是以约修亚的方式\n',
            '来劝说公爵的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060170869V#040F呵呵，原来是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010170870V#001F嗯，是呀，\n',
            '我才不会像那样说谎吓人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)

    ChrTalk(
        0x0102,
        (
            '#0020170871V#018F……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x0102)

    ChrTalk(
        0x0009,
        (
            '#1870170872V哈哈哈，\n',
            '谎话也是分很多种的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1870170873V如果是为了帮助大家，\n',
            '相信女神也是会允许的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1860170874V嗯，今天多谢你们的帮助。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1860170875V以后的工作\n',
            '也多多加油吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_47E7')
    def lambda_47E7():
        ChrTurnDirection(0x0105, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_47E7)

    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010170876V#006F嗯，那么就再见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0008, 400)

    ChrTalk(
        0x0102,
        (
            '#0020170877V#010F告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_2B(0x0023, 0x0002)
    Sleep(400)

    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【说服旅行者】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeOut(2000, 0, -1)
    OP_0D()
    OP_4B(0x0008, 255)
    OP_4B(0x0009, 255)
    OP_4B(0x0012, 255)
    OP_4B(0x000A, 255)
    ChrClearFlags(0x0101, 0x0040)
    ChrClearFlags(0x0105, 0x0040)
    ChrClearFlags(0x0010, 0x0040)
    ChrClearFlags(0x0011, 0x0040)
    NewScene('ED6_DT01/T2700._SN', 101, 0, 0)
    IdleLoop()
    MapSetFlags(0x00000001)
    EventEnd(0x00)

    Return()

# id: 0x0018 offset: 0x48DD
@scena.Code('func_18_48DD')
def func_18_48DD():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    FadeIn(2000, 0)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetPos(0x000B, -770, 0, 21500, 0)
    ChrSetPos(0x000C, -770, 0, 22500, 0)
    ChrSetPos(0x000D, -770, 0, 23500, 0)
    ChrSetPos(0x0101, -1000, 0, 9300, 180)
    ChrSetPos(0x0105, 0, 0, 9300, 180)
    ChrSetPos(0x0102, -1800, 0, 7800, 90)
    ChrSetPos(0x0008, 0, 0, 6500, 0)
    ChrSetPos(0x0009, -1000, 0, 5500, 0)
    ChrSetPos(0x0012, -2000, 0, 6500, 90)
    ChrSetPos(0x000A, -4800, 0, 7900, 90)

    ExecExpressionWithValue(
        0x000F,
        0x01,
        (
            (Expr.GetChrWork, 0x102, 0x1),
            (Expr.GetChrWork, 0x101, 0x1),
            Expr.Add,
            (Expr.GetChrWork, 0x8, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x3),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x02,
        (
            (Expr.GetChrWork, 0x102, 0x2),
            (Expr.GetChrWork, 0x101, 0x2),
            Expr.Add,
            (Expr.GetChrWork, 0x8, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x3),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x03,
        (
            (Expr.GetChrWork, 0x102, 0x3),
            (Expr.GetChrWork, 0x101, 0x3),
            Expr.Add,
            (Expr.GetChrWork, 0x8, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x3),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x000F, 0)
    OP_4A(0x0008, 255)
    OP_4A(0x0009, 255)
    OP_4A(0x0012, 255)
    OP_4A(0x000A, 255)
    OP_0D()

    ChrTalk(
        0x0009,
        (
            '#1870170878V……就是这样，\n',
            '这位小姑娘的确很干脆啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1870170879V那家伙不讲道理的时候，\n',
            '就把棒子向他挥去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1870170880V一看到这种情况，\n',
            '那家伙的脸色都吓白了……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1870170881V结果呢，靠小姑娘一个人\n',
            '就成功地赶走了那家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1860170882V唔，是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1860170883V我刚才听到打架的声音\n',
            '还担心了半天……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1860170884V喂，\n',
            '真的没有把他打伤吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0012, 0x0008, 400)

    ChrTalk(
        0x0012,
        (
            '#1880170885V嗯，一点事也没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010170886V#007F唉，我真丢脸……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0008, 400)

    ChrTalk(
        0x0102,
        (
            '#0020170887V#017F真是不好意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0102, 400)

    ChrTalk(
        0x0008,
        (
            '#1860170888V哪里，\n',
            '这件事的起因是\n',
            '公爵大人的任性胡为。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1860170889V你们没有必要\n',
            '为此道歉或负责。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4C86')
    def lambda_4C86():
        ChrTurnDirection(0x0012, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_4C86)

    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#1860170890V不过，今后不到万不得已，\n',
            '还是不要动手为好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170891V#007F嗯……\n',
            '我会牢记在心的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010170892V#003F谢谢队长。\n',
            '还有科洛丝，你们及时阻止了我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060170893V#040F没事的，不要那么介意嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060170894V虽然使用暴力的确不太好……\n',
            '不过这也和公爵大人的态度有关。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1860170895V方法虽然有些问题，\n',
            '不过最后还是帮助了那些普通的旅行者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1860170896V我代表他们\n',
            '向你们表达感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010170897V#000F……嗯，谢谢您。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170898V#001F嘿嘿，太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010170899V听了你们的话，\n',
            '我觉得又精神起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020170900V#018F真是的，\n',
            '转变得可真快啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020170901V#017F算了，\n',
            '这也算是艾丝蒂尔的一个优点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060170902V#041F嘻嘻…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1860170903V不管怎么说，\n',
            '今天真是辛苦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1860170875V以后的工作\n',
            '也多多加油吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170876V#006F嗯，那么就再见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4FF4')
    def lambda_4FF4():
        ChrTurnDirection(0x0105, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_4FF4)

    ChrTurnDirection(0x0102, 0x0008, 400)

    ChrTalk(
        0x0102,
        (
            '#0020170877V#010F告辞了。',
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
            '任务【说服旅行者】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeOut(2000, 0, -1)
    OP_0D()
    OP_4B(0x0008, 255)
    OP_4B(0x0009, 255)
    OP_4B(0x0012, 255)
    OP_4B(0x000A, 255)
    ChrClearFlags(0x0101, 0x0040)
    ChrClearFlags(0x0105, 0x0040)
    ChrClearFlags(0x0010, 0x0040)
    ChrClearFlags(0x0011, 0x0040)
    NewScene('ED6_DT01/T2700._SN', 101, 0, 0)
    IdleLoop()
    MapSetFlags(0x00000001)
    EventEnd(0x00)

    Return()

# id: 0x0019 offset: 0x50B5
@scena.Code('func_19_50B5')
def func_19_50B5():
    If(
        (
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x0023, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5132',
    )

    EventBegin(0x01)
    OP_4A(0x000E, 255)
    ChrTurnDirection(0x000E, 0x0101, 0)

    ChrTalk(
        0x000E,
        (
            '#0020170668V#012F艾丝蒂尔，\n',
            '赶快去食堂看看情况吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    ChrSetDirection(0x000E, 0, 0)
    OP_4B(0x000E, 255)
    Sleep(50)

    EventEnd(0x04)

    def _loc_5132(): pass

    label('loc_5132')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

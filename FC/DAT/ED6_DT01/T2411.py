import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2411_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2411   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2411.x'
    header.mapIndex       = 1
    header.bgm            = 15
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
        ('ED6_DT07/CH02590._CH', 'ED6_DT07/CH02590P._CP'),
        ('ED6_DT07/CH02640._CH', 'ED6_DT07/CH02640P._CP'),
        ('ED6_DT07/CH02630._CH', 'ED6_DT07/CH02630P._CP'),
        ('ED6_DT07/CH02570._CH', 'ED6_DT07/CH02570P._CP'),
        ('ED6_DT07/CH02500._CH', 'ED6_DT07/CH02500P._CP'),
        ('ED6_DT06/CH20094._CH', 'ED6_DT06/CH20094P._CP'),
        ('ED6_DT06/CH20095._CH', 'ED6_DT06/CH20095P._CP'),
        ('ED6_DT06/CH20096._CH', 'ED6_DT06/CH20096P._CP'),
        ('ED6_DT06/CH20097._CH', 'ED6_DT06/CH20097P._CP'),
        ('ED6_DT07/CH02573._CH', 'ED6_DT07/CH02573P._CP'),
    ]

# id: 0x10001 offset: 0xFA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '特蕾莎院长',
            x                   = 34340,
            z                   = 0,
            y                   = -31330,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '达尼艾尔',
            x                   = 37220,
            z                   = 0,
            y                   = -33090,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0104,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '玛丽',
            x                   = 37310,
            z                   = 1500,
            y                   = -33090,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0104,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '波利',
            x                   = 37220,
            z                   = 0,
            y                   = -36830,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0104,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '克拉姆',
            x                   = 37220,
            z                   = 1500,
            y                   = -36830,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0104,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x19A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x19A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x19A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x19A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_1B1',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x56),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_03_53F)

    def _loc_1B1(): pass

    label('loc_1B1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_1C8',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, func_02_252)

    def _loc_1C8(): pass

    label('loc_1C8')

    Return()

# id: 0x0001 offset: 0x1C9
@scena.Code('func_01_1C9')
def func_01_1C9():
    OP_6F(0x0003, 10)
    OP_6F(0x0004, 15)
    OP_6F(0x0005, 20)
    OP_6F(0x0006, 15)
    ChrSetFlags(0x000C, 0x0002)
    ChrSetFlags(0x0009, 0x0002)
    ChrSetFlags(0x000A, 0x0002)
    ChrSetFlags(0x000B, 0x0002)
    ChrSetFlags(0x000C, 0x0004)
    ChrSetFlags(0x0009, 0x0004)
    ChrSetFlags(0x000A, 0x0004)
    ChrSetFlags(0x000B, 0x0004)
    ChrSetPos(0x000C, 37940, 1500, -36940, 225)
    ChrSetPos(0x0009, 37940, 200, -36940, 225)
    ChrSetPos(0x000A, 37960, 1500, -32830, 225)
    ChrSetPos(0x000B, 37960, 200, -32830, 225)

    Return()

# id: 0x0002 offset: 0x252
@scena.Code('func_02_252')
def func_02_252():
    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x0083, 4, 0x41C))
    ChrSetFlags(0x0008, 0x0004)
    ChrSetPos(0x0008, 36300, 200, 42360, 270)
    OP_4A(0x0009, 255)
    OP_4A(0x000A, 255)
    OP_4A(0x000B, 255)
    OP_4A(0x000C, 255)
    OP_4A(0x0008, 255)
    ChrSetChipByIndex(0x0008, 9)
    ChrSetSubChip(0x0008, 0)
    OP_6F(0x0003, 50)
    CameraMove(35210, 3800, -34580, 0)
    OP_67(0, 3030, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(37000, 0)
    OP_6E(280, 0)
    FadeIn(500, 0)
    CameraMove(35210, 2500, -34580, 3000)
    Sleep(1000)

    Fade(1000)
    CameraMove(36570, 0, 42820, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0390050001V#750F呵呵，要修补的东西还真多，\n',
            '这也说明孩子们的精力都很旺盛吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050002V好了，差不多该休息了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    ChrSetChipByIndex(0x0008, 3)
    ChrSetPos(0x0008, 35780, 0, 42330, 270)
    OP_0D()
    Sleep(500)

    @scena.Lambda('lambda_03DA')
    def lambda_03DA():
        CameraMove(35930, 0, 43280, 1500)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_03DA)

    ChrWalkTo(0x0008, 34780, 0, 42310, 1000, 0x00)
    ChrWalkTo(0x0008, 34380, 0, 43600, 1000, 0x00)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0390050003V#754F女神啊， \n',
            '请赐予这些孩子健康的明天吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(134, 0x00, 0x64)
    Sleep(1000)

    OP_62(0x0008, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0390050004V#753F这是什么声音？\n',
            '好像是柴火的声音……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050005V#753F……还有这气味是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetDirection(0x0008, 180, 500)

    ChrTalk(
        0x0008,
        (
            '#0390050006V#755F………………难道！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/T2403._SN', 0, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x53F
@scena.Code('func_03_53F')
def func_03_53F():
    EventBegin(0x00)
    PlaySE(135, 0x01, 0x46)
    ChrSetPos(0x0101, 40390, 0, -29880, 0)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x0008, 0x0040)
    ChrSetFlags(0x000C, 0x0040)
    ChrSetFlags(0x000A, 0x0040)
    ChrSetFlags(0x000B, 0x0040)
    ChrSetFlags(0x0009, 0x0040)
    MapClearFlags(0x00000001)
    CameraMove(35210, 2050, -34580, 0)
    OP_67(0, 3210, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(37000, 0)
    OP_6E(280, 0)
    OP_0D()
    OP_72(0x0001, 0x0010)
    OP_70(0x0001, 20)
    OP_73(0x0001)
    ChrWalkTo(0x0008, 34080, 0, -33810, 4000, 0x00)

    ChrTalk(
        0x0008,
        (
            '#0390050007V#755F孩子们，快起来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x000C, 1)
    ChrSetSubChip(0x000A, 1)
    OP_62(0x000C, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_70(0x0005, 60)
    Sleep(1000)

    ChrClearFlags(0x000C, 0x0002)
    ChrSetChipByIndex(0x000C, 0)

    @scena.Lambda('lambda_063F')
    def lambda_063F():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_063F)

    ChrJumpToRelative(0x000C, 0, 300, 0, 600, 4000)

    ChrTalk(
        0x000C,
        (
            '#0400050008V#774F#2P哇哇哇……\n',
            '对不起，我不会再这样了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400050009V#772F…………………哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x000A, 2)
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0410050010V#1P克拉姆……\n',
            '你又睡昏头了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0700')
    def lambda_0700():
        CameraMove(36380, 1500, -34730, 1000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0700)

    ChrWalkTo(0x0008, 35540, 0, -34870, 3000, 0x00)
    ChrSetDirection(0x0008, 90, 400)

    ChrTalk(
        0x0008,
        (
            '#0390050011V#755F波利，达尼艾尔！\n',
            '快起来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x000B, 1)
    ChrSetSubChip(0x0009, 1)

    ChrTalk(
        0x000B,
        (
            '#0430050012V#4P呜唔～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0420050013V#3P怎么了啊……\n',
            '老师你的样子好吓人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0390050014V#752F……着火了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0400050015V#774F#2P哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0410050016V#1P真、真的！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0390050017V#755F快下一楼去！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050018V都别慌！\n',
            '快点跟老师走就是了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(-1280, 0, -1260, 0)
    OP_67(0, 7800, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    PlaySE(135, 0x01, 0x64)
    ChrClearFlags(0x000A, 0x0002)
    ChrClearFlags(0x000C, 0x0002)
    ChrClearFlags(0x0009, 0x0002)
    ChrClearFlags(0x000B, 0x0002)
    ChrSetFlags(0x000A, 0x0001)
    ChrSetFlags(0x000C, 0x0001)
    ChrSetFlags(0x0009, 0x0001)
    ChrSetFlags(0x000B, 0x0001)
    ChrClearFlags(0x000A, 0x0004)
    ChrClearFlags(0x000C, 0x0004)
    ChrClearFlags(0x0009, 0x0004)
    ChrClearFlags(0x000B, 0x0004)
    ChrSetPos(0x0008, 870, 1250, 12330, 0)
    ChrSetPos(0x000A, 560, 1750, 12770, 0)
    ChrSetPos(0x000C, 1240, 1750, 12770, 0)
    ChrSetPos(0x0009, 1220, 2000, 13840, 0)
    ChrSetPos(0x000B, 520, 2000, 13840, 0)
    ChrClearFlags(0x000A, 0x0004)
    ChrClearFlags(0x000A, 0x0002)
    ChrSetChipByIndex(0x000A, 2)
    ChrSetChipByIndex(0x0009, 1)
    ChrSetChipByIndex(0x000B, 4)
    Sleep(500)

    FadeIn(1000, 0)

    @scena.Lambda('lambda_0979')
    def lambda_0979():
        CameraMove(530, 0, 10090, 2700)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0979)

    Sleep(1000)

    @scena.Lambda('lambda_0996')
    def lambda_0996():
        ChrWalkTo(0x00FE, 290, 0, 8250, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0996)

    Sleep(100)

    @scena.Lambda('lambda_09B6')
    def lambda_09B6():
        ChrWalkTo(0x00FE, 1330, 0, 8560, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_09B6)

    @scena.Lambda('lambda_09D1')
    def lambda_09D1():
        ChrWalkTo(0x00FE, 500, 0, 10000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_09D1)

    Sleep(100)

    @scena.Lambda('lambda_09F1')
    def lambda_09F1():
        ChrWalkTo(0x00FE, 1310, 0, 9980, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_09F1)

    @scena.Lambda('lambda_0A0C')
    def lambda_0A0C():
        ChrWalkTo(0x00FE, 500, 0, 10000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0A0C)

    WaitForThreadExit(0x000A, 0x0001)

    @scena.Lambda('lambda_0A2C')
    def lambda_0A2C():
        ChrWalkTo(0x00FE, -400, 0, 8860, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0A2C)

    WaitForThreadExit(0x0008, 0x0002)

    ChrTalk(
        0x000C,
        (
            '#0400050019V#774F#2P哇哇，怎么会这样！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0410050020V咳咳，好呛～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0420050021V我、我怕～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0430050022V呜唔～……\n',
            '我还想睡～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_70(0x0000, 100)
    ChrWalkTo(0x0008, -1320, 0, 8280, 3000, 0x00)

    @scena.Lambda('lambda_0AFA')
    def lambda_0AFA():
        ChrTurnDirection(0x00FE, 0x000C, 400)
        Yield()

        Jump('lambda_0AFA')

    DispatchAsync2(0x0008, 0x0001, lambda_0AFA)

    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#0390050023V#755F快，大家快从门口出去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0008, 0xFF)
    OP_6F(0x0000, 100)
    OP_70(0x0000, 280)

    @scena.Lambda('lambda_0B4F')
    def lambda_0B4F():
        CameraMove(-580, 0, 4990, 1500)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0B4F)

    @scena.Lambda('lambda_0B67')
    def lambda_0B67():
        ChrWalkTo(0x00FE, -1200, 0, 1490, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0B67)

    Sleep(100)

    @scena.Lambda('lambda_0B87')
    def lambda_0B87():
        ChrWalkTo(0x00FE, -1200, 0, 1490, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0B87)

    Sleep(100)

    @scena.Lambda('lambda_0BA7')
    def lambda_0BA7():
        ChrWalkTo(0x00FE, -1200, 0, 1490, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0BA7)

    Sleep(100)

    @scena.Lambda('lambda_0BC7')
    def lambda_0BC7():
        ChrWalkTo(0x00FE, -1200, 0, 1490, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0BC7)

    Sleep(500)

    @scena.Lambda('lambda_0BE7')
    def lambda_0BE7():
        ChrWalkTo(0x00FE, -1200, 0, 1490, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0BE7)

    PlaySE(136, 0x00, 0x64)
    Sleep(200)

    OP_62(0x000C, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x000A, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0009, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x000B, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_0C54')
    def lambda_0C54():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000001F4, 0x00001B58, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0C54)

    @scena.Lambda('lambda_0C6A')
    def lambda_0C6A():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000001F4, 0x00001B58, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0C6A)

    Sleep(200)

    @scena.Lambda('lambda_0C85')
    def lambda_0C85():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000064, 0x00001B58, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0C85)

    @scena.Lambda('lambda_0C9B')
    def lambda_0C9B():
        OP_94(0x01, 0x00FE, 0x00B4, 0x0000012C, 0x00001B58, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0C9B)

    @scena.Lambda('lambda_0CB1')
    def lambda_0CB1():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000001F4, 0x00001B58, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0CB1)

    ChrTalk(
        0x000C,
        (
            '#0400050024V#775F哇啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0410050025V啊啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0390050026V#756F怎，怎么会这样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390050027V啊啊，女神啊！\n',
            '无论如何，请救救这些孩子吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0D62')
    def lambda_0D62():
        CameraSetDistance(3000, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0D62)

    OP_77(0xFF, 0x00, 0x00, 0x00, 0x000001F4)
    Sleep(500)

    OP_20(0x000005DC)
    FadeOut(1000, 16777215, -1)
    OP_24(0x0087, 0x5A)
    Sleep(300)

    OP_24(0x0087, 0x50)
    Sleep(300)

    OP_24(0x0087, 0x46)
    Sleep(300)

    OP_24(0x0087, 0x3C)
    Sleep(300)

    OP_24(0x0087, 0x32)
    Sleep(300)

    OP_24(0x0087, 0x28)
    Sleep(300)

    OP_24(0x0087, 0x1E)
    Sleep(300)

    OP_23(0x0087)
    OP_0D()
    CameraMove(16750, 0, -54030, 0)
    OP_77(0x00, 0x00, 0x00, 0x00, 0x00000000)
    FadeIn(1000, 16777215)
    OP_21()
    OP_0D()
    MapSetFlags(0x10000000)
    SetScenaFlags(ScenaFlag(0x007F, 5, 0x3FD))
    NewScene('ED6_DT01/T2100._SN', 100, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

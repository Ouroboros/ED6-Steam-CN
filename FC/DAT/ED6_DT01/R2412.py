import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import R2412_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R2412   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'R2412.x'
    header.mapIndex       = 103
    header.bgm            = 86
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
            word_3A         = 103,
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
        ('ED6_DT07/CH00341._CH', 'ED6_DT07/CH00341P._CP'),
        ('ED6_DT07/CH00151._CH', 'ED6_DT07/CH00151P._CP'),
        ('ED6_DT07/CH00152._CH', 'ED6_DT07/CH00152P._CP'),
        ('ED6_DT07/CH00260._CH', 'ED6_DT07/CH00260P._CP'),
        ('ED6_DT07/CH00340._CH', 'ED6_DT07/CH00340P._CP'),
        ('ED6_DT07/CH00341._CH', 'ED6_DT07/CH00341P._CP'),
        ('ED6_DT07/CH00342._CH', 'ED6_DT07/CH00342P._CP'),
        ('ED6_DT07/CH00344._CH', 'ED6_DT07/CH00344P._CP'),
        ('ED6_DT07/CH00260._CH', 'ED6_DT07/CH00260P._CP'),
        ('ED6_DT07/CH00261._CH', 'ED6_DT07/CH00261P._CP'),
        ('ED6_DT07/CH00262._CH', 'ED6_DT07/CH00262P._CP'),
        ('ED6_DT07/CH00264._CH', 'ED6_DT07/CH00264P._CP'),
        ('ED6_DT07/CH00265._CH', 'ED6_DT07/CH00265P._CP'),
        ('ED6_DT07/CH02200._CH', 'ED6_DT07/CH02200P._CP'),
        ('ED6_DT06/CH20137._CH', 'ED6_DT06/CH20137P._CP'),
        ('ED6_DT06/CH20138._CH', 'ED6_DT06/CH20138P._CP'),
    ]

# id: 0x10001 offset: 0x12A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '黑衣男子',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '黑衣男子',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '阿加特',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '蒙面队长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '目标用摄像机',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0080,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x1CA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x1CA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x1CA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -2060,
            triggerZ            = 0,
            triggerY            = 120820,
            triggerRange        = 1500,
            actorX              = -2060,
            actorZ              = 1500,
            actorY              = 120820,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1EE
@scena.Code('Init')
def Init():
    Event(0, func_02_206)

    Return()

# id: 0x0001 offset: 0x1F3
@scena.Code('func_01_1F3')
def func_01_1F3():
    OP_16(0x02, 4000, -136000, -52000, 196645)

    Return()

# id: 0x0002 offset: 0x206
@scena.Code('func_02_206')
def func_02_206():
    FadeIn(2000, 0)
    LoadEffect(0x00, 'craft\\\\cr201_00.eff')
    LoadEffect(0x01, 'craft\\\\cr201_01.eff')
    LoadEffect(0x02, 'craft\\\\cr201_02.eff')
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(-4600, 3000, 117500, 0)
    CameraSetDistance(3400, 0)
    OP_67(0, 3300, -10000, 0)
    OP_6C(52000, 0)
    ChrSetPos(0x0008, -4900, 0, 125700, 0)
    ChrSetPos(0x0009, -3900, 0, 125000, 0)
    ChrSetPos(0x000A, 5300, 0, 139100, 0)

    @scena.Lambda('lambda_02C5')
    def lambda_02C5():
        OP_6C(45000, 5000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_02C5)

    CameraMove(-4600, 0, 117500, 5000)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)

    @scena.Lambda('lambda_02F5')
    def lambda_02F5():
        ChrWalkTo(0x00FE, -5700, 0, 115900, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_02F5)

    @scena.Lambda('lambda_0310')
    def lambda_0310():
        ChrWalkTo(0x00FE, -4600, 0, 117500, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0310)

    WaitForThreadExit(0x0009, 0x0001)

    @scena.Lambda('lambda_0330')
    def lambda_0330():
        ChrSetDirection(0x0009, 0, 800)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0330)

    WaitForThreadExit(0x0008, 0x0001)

    @scena.Lambda('lambda_0343')
    def lambda_0343():
        ChrSetDirection(0x0008, 0, 800)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0343)

    ChrTalk(
        0x0008,
        (
            '#2620070001V哈啊哈啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2630070002V#2P好、好缠人的家伙！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050070003V#10A#4P哦喔喔喔喔！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(1300)

    @scena.Lambda('lambda_03C0')
    def lambda_03C0():
        OP_6C(21000, 3000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_03C0)

    CreateThread(0x000A, 0x01, 0x00, func_05_262C)

    ChrTalk(
        0x0009,
        (
            '#2630070004V#25A#6P背着这么一把巨剑，\n',
            '竟然还能追得上来！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(200)

    CreateThread(0x0008, 0x01, 0x00, func_03_24A5)
    Sleep(200)

    CreateThread(0x0009, 0x01, 0x00, func_04_258B)
    OP_6A(0x0009)
    Sleep(2800)

    ChrTalk(
        0x000A,
        (
            '#0050070005V#25A#1P哼，别把我和你们这些三脚猫混为一谈。',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(2700)

    ChrTalk(
        0x000A,
        (
            '#0050070006V#12A#5S#5P喝啊啊啊啊啊！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    WaitForThreadExit(0x000A, 0x0001)

    @scena.Lambda('lambda_04A6')
    def lambda_04A6():
        OP_6C(348000, 4000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_04A6)

    Sleep(500)

    ChrJumpTo(0x000A, -8000, 0, 58200, 500, 6000)
    PlaySE(164, 0x00, 0x64)
    OP_99(0x000A, 0x07, 0x00, 2000)
    ChrClearFlags(0x000A, 0x0800)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#2620070007V#6P呜……\n',
            '还是甩不掉吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0516')
    def lambda_0516():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_0516')

    DispatchAsync2(0x0008, 0x0000, lambda_0516)

    @scena.Lambda('lambda_0527')
    def lambda_0527():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_0527')

    DispatchAsync2(0x0009, 0x0000, lambda_0527)

    @scena.Lambda('lambda_0538')
    def lambda_0538():
        ChrJumpTo(0x0008, -4890, 30, 52030, 800, 5000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0538)

    WaitForThreadExit(0x0008, 0x0001)
    ChrSetChipByIndex(0x0008, 4)
    ChrSetSubChip(0x0008, 0)
    Sleep(100)

    @scena.Lambda('lambda_056A')
    def lambda_056A():
        ChrJumpTo(0x0009, -7220, 20, 50760, 800, 5000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_056A)

    WaitForThreadExit(0x0009, 0x0001)
    ChrSetChipByIndex(0x0009, 4)
    ChrSetSubChip(0x0009, 0)
    WaitForThreadExit(0x000A, 0x0001)

    ChrTalk(
        0x0009,
        (
            '#2630070008V没办法了，迎击吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050070009V#051F好极了。\n',
            '终于打算动手了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050070010V和你们这些杂碎捉迷藏，\n',
            '我可早就玩腻了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620070011V你要是识趣不追上来的话，\n',
            '或许还能保住自己的小命……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2630070012V愚蠢的家伙……\n',
            '一对二你还想赢吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050070013V#051F哈哈，\n',
            '我当然会赢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620070014V什么……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050070015V#054F打架也要打得有气势。\n',
            '连气势也输掉的话那就别想赢了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050070016V你们从夹着尾巴开溜那一刻起，\n',
            '就已注定成为丧家之犬了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620070017V一、一派胡言！\n',
            '你这只协会的走狗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2630070018V看我们两个\n',
            '怎么好好收拾你！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_07D6')
    def lambda_07D6():
        OP_6E(243, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_07D6)

    @scena.Lambda('lambda_07E6')
    def lambda_07E6():
        CameraMove(-7660, 0, 57680, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_07E6)

    PlayEffect(0x01, 0x01, 0x000A, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_0833')
    def lambda_0833():
        OP_99(0x00FE, 0x00, 0x04, 2600)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0833)

    ChrSetChipByIndex(0x0008, 5)
    ChrSetChipByIndex(0x0009, 5)
    ChrTurnDirection(0x0008, 0x000A, 0)
    ChrTurnDirection(0x0009, 0x000A, 0)

    @scena.Lambda('lambda_085B')
    def lambda_085B():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000005DC, 0x000005DC, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_085B)

    @scena.Lambda('lambda_0871')
    def lambda_0871():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000005DC, 0x000005DC, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_0871)

    Sleep(500)

    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    Sleep(100)

    @scena.Lambda('lambda_0899')
    def lambda_0899():
        OP_94(0x01, 0x00FE, 0x0000, 0x00002328, 0x00002710, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0899)

    Sleep(50)

    @scena.Lambda('lambda_08B4')
    def lambda_08B4():
        OP_94(0x01, 0x00FE, 0x0000, 0x00002328, 0x00002710, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_08B4)

    Sleep(400)

    StopEffect(0x01, 0x02)
    PlayEffect(0x00, 0xFF, 0x000A, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_0907')
    def lambda_0907():
        OP_99(0x00FE, 0x04, 0x07, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0907)

    Sleep(200)

    PlayEffect(0x02, 0xFF, 0x0008, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0008, 7)
    ChrSetFlags(0x0008, 0x0020)

    @scena.Lambda('lambda_0966')
    def lambda_0966():
        OP_94(0x01, 0x00FE, 0x00B4, 0x00000FA0, 0x00004E20, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0966)

    Sleep(50)

    PlayEffect(0x02, 0xFF, 0x0009, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0009, 7)
    ChrSetFlags(0x0009, 0x0020)

    @scena.Lambda('lambda_09CB')
    def lambda_09CB():
        OP_94(0x01, 0x00FE, 0x00B4, 0x00000FA0, 0x00003A98, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_09CB)

    @scena.Lambda('lambda_09E1')
    def lambda_09E1():
        OP_94(0x01, 0x00FE, 0x00B4, 0x00000FA0, 0x00004E20, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_09E1)

    Sleep(50)

    @scena.Lambda('lambda_09FC')
    def lambda_09FC():
        OP_94(0x01, 0x00FE, 0x00B4, 0x00000FA0, 0x00002710, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_09FC)

    @scena.Lambda('lambda_0A12')
    def lambda_0A12():
        OP_94(0x01, 0x00FE, 0x00B4, 0x00000FA0, 0x00003A98, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_0A12)

    Sleep(50)

    @scena.Lambda('lambda_0A2D')
    def lambda_0A2D():
        OP_94(0x01, 0x00FE, 0x00B4, 0x00000FA0, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0A2D)

    @scena.Lambda('lambda_0A43')
    def lambda_0A43():
        OP_94(0x01, 0x00FE, 0x00B4, 0x00000FA0, 0x00002710, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_0A43)

    Sleep(50)

    @scena.Lambda('lambda_0A5E')
    def lambda_0A5E():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0A5E)

    @scena.Lambda('lambda_0A74')
    def lambda_0A74():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_0A74)

    Sleep(50)

    @scena.Lambda('lambda_0A8F')
    def lambda_0A8F():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_0A8F)

    Sleep(450)

    Fade(1000)
    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    CameraMove(-7670, 0, 56050, 0)
    CameraSetDistance(3000, 0)
    OP_67(0, 8200, -10000, 0)
    OP_6C(45000, 0)
    ChrSetPos(0x0008, -8400, 0, 54200, 0)
    ChrSetPos(0x0009, -9800, 0, 54800, 0)
    ChrSetPos(0x000B, -6700, 0, 58700, 180)
    ChrTurnDirection(0x000A, 0x0008, 0)
    ChrTurnDirection(0x0008, 0x000A, 0)
    ChrTurnDirection(0x0009, 0x000A, 0)
    PlayEffect(0x02, 0xFF, 0x0008, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x02, 0xFF, 0x0009, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#2620070019V#4P呜啊啊啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2630070020V呜……\n',
            '怎么能在这种地方被抓住………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0BFE')
    def lambda_0BFE():
        ChrSetDirection(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0BFE)

    @scena.Lambda('lambda_0C0C')
    def lambda_0C0C():
        OP_99(0x00FE, 0x05, 0x00, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0C0C)

    ChrJumpTo(0x000A, -7300, 0, 56400, 700, 4000)
    TerminateThread(0x000A, 0x02)
    ChrSetChipByIndex(0x000A, 14)
    ChrSetSubChip(0x000A, 0)
    Sleep(300)

    ChrTalk(
        0x000A,
        (
            '#0050070021V#050F#5P哼，还不赶快投降。\n',
            '给我老老实实地坦白一切！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050070022V你们是什么人？\n',
            '干那么多坏事有什么企图……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000003E8)
    ChrSetPos(0x000B, -4010, 0, 61460, 270)
    ChrSetRGBAMask(0x000B, 255, 255, 255, 0, 0)

    NpcTalk(
        0x000B,
        '青年的声音',
        (
            '#0140070023V#4P——这可真让人为难啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_21()
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(800)

    ChrSetChipByIndex(0x000A, 14)
    ChrSetSubChip(0x000A, 0)
    ChrSetDirection(0x000A, 43, 600)

    ChrTalk(
        0x000A,
        (
            '#0050070024V#052F#4P什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlayBGM(81)
    ChrSetChipByIndex(0x000B, 13)
    ChrClearFlags(0x000B, 0x0080)

    @scena.Lambda('lambda_0D75')
    def lambda_0D75():
        CameraMove(-6790, 0, 56980, 1500)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_0D75)

    @scena.Lambda('lambda_0D8D')
    def lambda_0D8D():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1500)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_0D8D)

    @scena.Lambda('lambda_0D9F')
    def lambda_0D9F():
        ChrWalkTo(0x00FE, -6700, 0, 58700, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0D9F)

    ChrSetChipByIndex(0x000A, 2)
    ChrSetSubChip(0x000A, 7)

    @scena.Lambda('lambda_0DC4')
    def lambda_0DC4():
        ChrSetDirection(0x00FE, 0, 800)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0DC4)

    ChrJumpTo(0x000A, -6000, 0, 55000, 700, 4000)
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0050070025V#055F#4P什、什么时候……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0E18')
    def lambda_0E18():
        OP_99(0x0008, 0x03, 0x00, 1000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0E18)

    ChrTalk(
        0x0008,
        (
            '#2620070026V队、队长！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0E44')
    def lambda_0E44():
        OP_99(0x0009, 0x03, 0x00, 1000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0E44)

    ChrTalk(
        0x0009,
        (
            '#2630070027V您来救我们了吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0140070028V#281F真拿你们没办法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140070029V不仅没按时进行联络，\n',
            '还在这种地方玩起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620070030V实、实在抱歉！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2630070031V一路上遇到重重阻挠……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050070032V#050F#4P原来如此啊……\n',
            '这么说你就是他们的老大吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x000A, 400)
    Sleep(400)

    ChrTalk(
        0x000B,
        (
            '#0140070033V#280F呵呵……\n',
            '我只不过是现场负责人而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140070034V我为部下的失礼表示歉意，\n',
            '能不能在此放他们一马呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050070035V#055F#4P啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050070036V你刚才……说什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0140070037V#280F我说能不能放他们一马。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140070038V说到底，\n',
            '我们也没打算和游击士协会为敌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050070039V#054F#4P白、白痴啊你！\n',
            '世上哪有这么便宜的好事！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0140070040V#281F哎呀哎呀……\n',
            '我可是觉得这提议不错啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x0009, 400)
    Sleep(400)

    ChrTalk(
        0x000B,
        (
            '#0140070041V#281F……你们两个。\n',
            '这里由我来挡着。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140070042V你们快去会合地点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)

    ChrTalk(
        0x0008,
        (
            '#2620070043V是、是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0008, 5)
    ChrClearFlags(0x0008, 0x0020)

    @scena.Lambda('lambda_1193')
    def lambda_1193():
        ChrWalkTo(0x00FE, -8900, 0, 43900, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1193)

    ChrTalk(
        0x0009,
        (
            '#2630070044V多谢队长！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0009, 5)
    ChrClearFlags(0x0008, 0x0020)

    @scena.Lambda('lambda_11D4')
    def lambda_11D4():
        ChrWalkTo(0x00FE, -8900, 0, 43900, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_11D4)

    ChrSetChipByIndex(0x000A, 14)
    ChrSetSubChip(0x000A, 0)

    @scena.Lambda('lambda_11F9')
    def lambda_11F9():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_11F9')

    DispatchAsync2(0x000A, 0x0001, lambda_11F9)

    Sleep(300)

    TerminateThread(0x000A, 0xFF)

    ChrTalk(
        0x000A,
        (
            '#0050070045V#054F又想逃吗？喂！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x000B, 9)
    ChrWalkTo(0x000B, -7400, 0, 57000, 7000, 0x00)

    @scena.Lambda('lambda_1253')
    def lambda_1253():
        OP_6C(0, 2000)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_1253)

    @scena.Lambda('lambda_1263')
    def lambda_1263():
        CameraMove(-9340, 0, 52260, 1000)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_1263)

    @scena.Lambda('lambda_127B')
    def lambda_127B():
        OP_97(0x00FE, -5100, 53300, -75000, 14000, 0x0001)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_127B)

    ChrSetChipByIndex(0x000A, 1)
    ChrWalkTo(0x000A, -8300, 0, 53000, 7000, 0x00)
    ChrTurnDirection(0x000A, 0x000B, 0)

    @scena.Lambda('lambda_12B7')
    def lambda_12B7():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_12B7')

    DispatchAsync2(0x000B, 0x0000, lambda_12B7)

    ChrSetChipByIndex(0x000A, 14)

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x000B, 8)

    @scena.Lambda('lambda_12E8')
    def lambda_12E8():
        ChrJumpTo(0x00FE, -7900, -50, 53420, 400, 3000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_12E8)

    PlaySE(501, 0x00, 0x64)
    ChrTurnDirection(0x000A, 0x000B, 0)
    ChrTurnDirection(0x000B, 0x000A, 800)
    ChrMoveTo(0x000B, -10400, 0, 51000, 4000, 0x00)
    Sleep(500)

    WaitForThreadExit(0x000B, 0x0003)

    ChrTalk(
        0x000B,
        (
            '#0140070046V#280F………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050070047V#057F#2P混帐……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050070048V#053F哼，算了。\n',
            '不过是换了个猎物罢了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050070049V看来你知道的东西\n',
            '比那两个杂碎的更有价值……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0140070050V#280F呵呵……\n',
            '你以为这么简单就能抓住我吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_142B')
    def lambda_142B():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_142B')

    DispatchAsync2(0x000A, 0x0000, lambda_142B)

    ChrTalk(
        0x000A,
        (
            '#0050070051V#054F#2P正是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000003E8)
    OP_21()
    PlayBGM(43)
    ChrSetFlags(0x000B, 0x0004)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)

    @scena.Lambda('lambda_1473')
    def lambda_1473():
        OP_6C(315000, 1000)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_1473)

    ChrClearFlags(0x000A, 0x0020)
    ChrSetChipByIndex(0x000A, 1)
    OP_94(0x01, 0x000A, 0x00B4, 0x000001F4, 0x000003E8, 0x00)

    ExecExpressionWithValue(
        0x000C,
        0x01,
        (
            (Expr.GetChrWork, 0xB, 0x1),
            (Expr.GetChrWork, 0xA, 0x1),
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
            (Expr.GetChrWork, 0xB, 0x2),
            (Expr.GetChrWork, 0xA, 0x2),
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
            (Expr.GetChrWork, 0xB, 0x3),
            (Expr.GetChrWork, 0xA, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x000C, 1000)
    OP_6A(0x000C)
    CreateThread(0x0008, 0x01, 0x00, func_06_2804)
    OP_93(0x000A, 0x000B, 1600, 12000, 0x00)
    ChrSetFlags(0x000A, 0x0020)
    ChrSetChipByIndex(0x000B, 12)
    ChrSetSubChip(0x000B, 0)
    ChrSetChipByIndex(0x000A, 15)
    ChrSetSubChip(0x000A, 0)
    PlaySE(505, 0x00, 0x64)

    @scena.Lambda('lambda_1518')
    def lambda_1518():
        OP_94(0x01, 0x00FE, 0x0000, 0x000000C8, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1518)

    @scena.Lambda('lambda_152E')
    def lambda_152E():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000000C8, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_152E)

    OP_9E(0x000B, 30, 0, 300, 5000)
    WaitForThreadExit(0x000B, 0x0001)

    @scena.Lambda('lambda_155C')
    def lambda_155C():
        OP_94(0x01, 0x00FE, 0x0000, 0x000005DC, 0x00001B58, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_155C)

    ChrSetChipByIndex(0x000B, 8)
    ChrSetSubChip(0x000B, 0)
    PlaySE(163, 0x00, 0x64)
    ChrSetChipByIndex(0x000A, 2)
    ChrSetSubChip(0x000A, 7)
    ChrJumpTo(0x000B, -12300, 1300, 50300, 1400, 15000)
    Sleep(100)

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x000B, 10)
    TerminateThread(0x000B, 0xFF)

    @scena.Lambda('lambda_15BB')
    def lambda_15BB():
        ChrJumpTo(0x00FE, -10200, 1300, 50800, 1000, 10000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_15BB)

    @scena.Lambda('lambda_15D9')
    def lambda_15D9():
        OP_99(0x00FE, 0x00, 0x07, 2000)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_15D9)

    Sleep(200)

    PlaySE(501, 0x00, 0x64)

    @scena.Lambda('lambda_15F3')
    def lambda_15F3():
        ChrJumpTo(0x00FE, -9200, 0, 53000, 1000, 10000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_15F3)

    @scena.Lambda('lambda_1611')
    def lambda_1611():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_1611')

    DispatchAsync2(0x000B, 0x0000, lambda_1611)

    ChrSetChipByIndex(0x000A, 1)
    WaitForThreadExit(0x000B, 0x0001)
    PlaySE(164, 0x00, 0x64)
    ChrJumpTo(0x000B, -9500, 0, 47800, 1000, 10000)
    PlaySE(164, 0x00, 0x64)

    @scena.Lambda('lambda_164D')
    def lambda_164D():
        OP_99(0x00FE, 0x07, 0x0B, 1500)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_164D)

    CameraSetDistance(2900, 1000)
    ChrSetChipByIndex(0x000B, 9)

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrJumpTo(0x000B, -8300, 0, 49200, 500, 3000)
    PlaySE(164, 0x00, 0x64)

    @scena.Lambda('lambda_1692')
    def lambda_1692():
        CameraSetDistance(2500, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1692)

    ChrJumpTo(0x000B, -9900, 0, 50100, 500, 7000)
    PlaySE(164, 0x00, 0x64)

    @scena.Lambda('lambda_16BE')
    def lambda_16BE():
        ChrSetDirection(0x000A, 30, 500)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_16BE)

    ChrJumpTo(0x000B, -7800, 0, 51800, 500, 10000)
    PlaySE(164, 0x00, 0x64)

    @scena.Lambda('lambda_16E8')
    def lambda_16E8():
        ChrJumpTo(0x000B, -9000, 0, 52000, 500, 10000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_16E8)

    TerminateThread(0x000A, 0xFF)
    PlaySE(505, 0x00, 0x64)
    ChrSetDirection(0x000A, 315, 1300)

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x000B, 8)

    @scena.Lambda('lambda_1726')
    def lambda_1726():
        ChrJumpTo(0x00FE, -9500, 500, 51900, 1000, 7000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1726)

    ChrSetDirection(0x000A, 135, 1600)
    Sleep(350)

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x000B, 10)

    @scena.Lambda('lambda_1760')
    def lambda_1760():
        OP_99(0x00FE, 0x00, 0x02, 3000)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_1760)

    ChrSetDirection(0x000A, 225, 0)
    ChrSetChipByIndex(0x000A, 2)
    OP_99(0x000A, 0x06, 0x07, 1500)

    @scena.Lambda('lambda_1785')
    def lambda_1785():
        OP_99(0x000A, 0x05, 0x00, 3000)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_1785)

    PlaySE(163, 0x00, 0x64)

    @scena.Lambda('lambda_179A')
    def lambda_179A():
        OP_99(0x00FE, 0x02, 0x00, 3000)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_179A)

    @scena.Lambda('lambda_17AA')
    def lambda_17AA():
        ChrJumpTo(0x000B, -8900, 0, 56800, 4000, 7000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_17AA)

    Sleep(200)

    @scena.Lambda('lambda_17CD')
    def lambda_17CD():
        ChrSetDirection(0x000A, 0, 500)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_17CD)

    Sleep(300)

    @scena.Lambda('lambda_17E0')
    def lambda_17E0():
        OP_99(0x00FE, 0x00, 0x07, 3000)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_17E0)

    PlaySE(164, 0x00, 0x64)
    PlaySE(163, 0x00, 0x64)

    @scena.Lambda('lambda_17FA')
    def lambda_17FA():
        ChrJumpTo(0x000A, -8900, 0, 55900, 2000, 10000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_17FA)

    @scena.Lambda('lambda_1818')
    def lambda_1818():
        OP_99(0x000A, 0x00, 0x07, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_1818)

    Sleep(200)

    PlaySE(505, 0x00, 0x64)
    Sleep(200)

    @scena.Lambda('lambda_1837')
    def lambda_1837():
        OP_99(0x00FE, 0x07, 0x0B, 1500)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_1837)

    ChrMoveTo(0x000B, -7350, 0, 56800, 15000, 0x00)
    WaitForThreadExit(0x000A, 0x0001)
    PlaySE(164, 0x00, 0x64)
    PlaySE(85, 0x00, 0x5A)
    PlayEffect(0x12, 0xFF, 0x00FF, -8610, -1000, 56740, 0, 0, 0, 3000, 3000, 3000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0, 500, 3000, 100)
    ChrJumpTo(0x000B, -5000, 0, 56700, 1300, 5000)
    PlaySE(164, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_18D1')
    def lambda_18D1():
        OP_99(0x000A, 0x07, 0x00, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_18D1)

    @scena.Lambda('lambda_18E1')
    def lambda_18E1():
        ChrTurnDirection(0x000A, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_18E1)

    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0050070052V#051F哼，有一手嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0140070053V#281F怀着无法抑制的激情\n',
            '来挥舞着沉重的铁块……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140070054V你……\n',
            '和我倒是有点像嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050070055V#052F………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050070056V……什么……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0140070057V#280F曾因自己的软弱无力\n',
            '而被绝望束缚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140070058V你的眼神是这么说的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050070059V#052F………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050070060V#053F哼哼哼，不错嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050070061V虽然不知道你是什么人，\n',
            '不过说话倒是相当讨人喜欢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0140070062V#280F我也一样，\n',
            '并不讨厌你这种直性子的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140070063V继续打斗下去也没意义，\n',
            '我们干脆就此握手言和吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050070064V#057F#5S#5P玩笑开够了吧！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    LoadEffect(0x00, 'battle\\\\mgaria0.eff')

    @scena.Lambda('lambda_1B79')
    def lambda_1B79():
        OP_9E(0x00FE, 30, 0, 1000, 5000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1B79)

    PlayEffect(0x00, 0x00, 0x000A, 0, 200, 0, 0, 0, 0, 900, 900, 900, 0x00FF, 0, 0, 0, 0)
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0050070065V#057F#5P我不出声，\n',
            '你就乱弹琴地鬼扯个没完！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050070066V看我怎么打烂你那张胡言乱语的臭嘴！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0008, 0xFF)

    ChrTalk(
        0x000B,
        (
            '#0140070067V#280F呵呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x000B, 12)

    @scena.Lambda('lambda_1C6D')
    def lambda_1C6D():
        OP_9E(0x00FE, 30, 0, 1000, 5000)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_1C6D)

    PlayEffect(0x00, 0x01, 0x000B, 0, 200, 0, 0, 0, 0, 900, 900, 900, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_1CBC')
    def lambda_1CBC():
        OP_9E(0x00FE, 30, 0, 1000, 5000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1CBC)

    Sleep(1000)

    @scena.Lambda('lambda_1CDB')
    def lambda_1CDB():
        OP_6C(0, 6000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_1CDB)

    @scena.Lambda('lambda_1CEB')
    def lambda_1CEB():
        OP_9E(0x00FE, 30, 0, 1000, 5000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1CEB)

    ChrTalk(
        0x000A,
        (
            '#0050070068V#15A#054F哦哦哦哦哦哦哦！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(3000)

    @scena.Lambda('lambda_1D35')
    def lambda_1D35():
        OP_9E(0x00FE, 30, 0, 1000, 5000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1D35)

    ChrTalk(
        0x000B,
        (
            '#0140070069V#15A#282F喝啊啊啊啊啊啊！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(3000)

    Sleep(500)

    TerminateThread(0x000B, 0xFF)
    ChrSetFlags(0x000B, 0x0040)
    ChrSetFlags(0x000A, 0x0040)
    OP_99(0x000A, 0x00, 0x03, 2000)

    @scena.Lambda('lambda_1D9B')
    def lambda_1D9B():
        OP_99(0x000A, 0x03, 0x07, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_1D9B)

    @scena.Lambda('lambda_1DAB')
    def lambda_1DAB():
        ChrTurnDirection(0x000A, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_1DAB)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x000B, 10)

    @scena.Lambda('lambda_1DD2')
    def lambda_1DD2():
        OP_99(0x00FE, 0x00, 0x03, 3000)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_1DD2)

    @scena.Lambda('lambda_1DE2')
    def lambda_1DE2():
        ChrWalkTo(0x00FE, -8900, 0, 55900, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1DE2)

    @scena.Lambda('lambda_1DFD')
    def lambda_1DFD():
        ChrWalkTo(0x00FE, -5000, 0, 56700, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1DFD)

    Sleep(100)

    OP_20(0x00000000)
    PlaySE(155, 0x00, 0x64)
    FadeOut(1, 16777215, -1)
    OP_0D()
    StopEffect(0x00, 0x00)
    StopEffect(0x01, 0x00)
    FadeIn(200, 16777215)
    LoadEffect(0x00, 'map\\\\mp009_00.eff')
    PlayEffect(0x00, 0x00, 0x000C, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_0D()
    PlayEffect(0x00, 0x01, 0x000C, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1500)

    @scena.Lambda('lambda_1EC5')
    def lambda_1EC5():
        OP_99(0x00FE, 0x03, 0x07, 1000)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_1EC5)

    ChrTalk(
        0x000B,
        (
            '#0140070070V#281F哼……',
            TxtCtl.Enter,
        ),
    )

    OP_9E(0x000B, 50, 0, 500, 5000)
    CloseMessageWindow()
    WaitForThreadExit(0x000B, 0x0003)
    ChrSetChipByIndex(0x000B, 11)
    OP_99(0x000B, 0x01, 0x03, 1200)
    Sleep(1000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_1F26')
    def lambda_1F26():
        OP_99(0x000A, 0x07, 0x00, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_1F26)

    ChrSetDirection(0x000A, 225, 400)
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0050070071V#051F嘿……\n',
            '看来你就只有嘴上功夫还算厉害。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050070072V现在就把你带回协会\n',
            '彻彻底底地审问一番吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlaySE(153, 0x00, 0x64)
    CreateThread(0x000B, 0x01, 0x00, func_07_2851)
    Sleep(1000)

    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrSetChipByIndex(0x000A, 14)
    ChrSetSubChip(0x000A, 0)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '#0050070073V#052F什、什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x000B, 0x01, 0x00, func_08_287E)
    Sleep(1000)

    TerminateThread(0x000B, 0x01)
    ChrSetRGBAMask(0x000B, 255, 255, 255, 200, 0)
    ChrSetRGBAMask(0x000B, 255, 255, 255, 0, 2000)
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0050070074V#055F这、这是……\n',
            '分身的战技！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '在昏暗树丛的空隙中隐隐约约地漂浮着人影。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlayBGM(83)
    Sleep(1000)

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('青年的声音')
    SetMessageWindowPos(75, 250, -1, -1)

    Talk(
        (
            '#0140070075V',
            (TxtCtl.SetColor, 0x5),
            '#50W呵呵呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    TalkSetChrName('青年的声音')

    Talk(
        (
            '#0140070076V#50W不错的一击，\n',
            '只是似乎还带有些迷惘啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkSetChrName('青年的声音')

    Talk(
        (
            '#0140070077V#50W这份迷惘会令刀法产生破绽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ChrTalk(
        0x000A,
        (
            '#0050070078V#057F什、什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkSetChrName('青年的声音')

    Talk(
        (
            '#0140070079V#50W想要化身修罗，\n',
            '就必须有舍弃一切的觉悟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0140070080V#50W想在这个世上生存下去……\n',
            '就必须忘却一切愤怒和悲伤。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0140070081V#100W那么，后会有期……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Sleep(1000)

    SetMessageWindowPos(72, 320, 56, 3)
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '树丛空隙间隐隐约约漂浮着的人影\n',
            '一瞬间隐入黑暗中消失了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapClearFlags(0x00000001)

    @scena.Lambda('lambda_22EA')
    def lambda_22EA():
        CameraMove(-5100, 1400, 56900, 1600)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_22EA)

    WaitForThreadExit(0x000A, 0x0002)
    ChrSetChipByIndex(0x000A, 15)
    ChrSetSubChip(0x000A, 0)
    OP_9E(0x000A, 20, 0, 1000, 5000)

    ChrTalk(
        0x000A,
        (
            '#0050070082V#056F#50W#5P…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050070083V#50W……说什么忘却……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050070084V#50W这种事……\n',
            '……我怎么可能做得出……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_23AF')
    def lambda_23AF():
        CameraSetDistance(2400, 2000)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_23AF)

    @scena.Lambda('lambda_23BF')
    def lambda_23BF():
        OP_67(0, 6000, -10000, 2300)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_23BF)

    @scena.Lambda('lambda_23D7')
    def lambda_23D7():
        OP_6C(54000, 2000)

        ExitThread()

    DispatchAsync(0x000B, 0x0000, lambda_23D7)

    Sleep(1000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_23F5')
    def lambda_23F5():
        CameraSetDistance(5000, 3000)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_23F5)

    @scena.Lambda('lambda_2405')
    def lambda_2405():
        OP_9E(0x00FE, 30, 0, 2000, 5000)
        Yield()

        Jump('lambda_2405')

    DispatchAsync2(0x000A, 0x0000, lambda_2405)

    ChrSetSubChip(0x000A, 1)

    ChrTalk(
        0x000A,
        (
            '#0050070085V#550F#5P#22A#5S呜哦哦哦哦哦哦哦哦！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    FadeOut(3000, 0, -1)
    OP_0D()

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(1000)

    OP_20(0x000007D0)
    OP_21()
    Sleep(1000)

    OP_AD('ED6_DT04/C_VIS043._CH', 0x0000, 0x0000, 0x00000064)
    Sleep(4000)

    OP_56(0x02)
    OP_AE(0x000000C8)
    Sleep(2000)

    SetScenaFlags(ScenaFlag(0x007F, 7, 0x3FF))
    NewScene('ED6_DT01/T2100._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x24A5
@scena.Code('func_03_24A5')
def func_03_24A5():
    ChrSetFlags(0x00FE, 0x0040)
    OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x00000BB8, 0x00)
    ChrWalkTo(0x00FE, -8400, 0, 100000, 10000, 0x00)
    ChrWalkTo(0x00FE, -10700, 0, 86400, 10000, 0x00)

    @scena.Lambda('lambda_24E7')
    def lambda_24E7():
        OP_6C(324000, 3000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_24E7)

    @scena.Lambda('lambda_24F7')
    def lambda_24F7():
        OP_67(0, 5200, -10000, 3000)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_24F7)

    @scena.Lambda('lambda_250F')
    def lambda_250F():
        CameraMove(-8000, 1300, 66400, 2700)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_250F)

    MapClearFlags(0x00000001)
    ChrWalkTo(0x00FE, -8000, 0, 72200, 12000, 0x00)
    ChrWalkTo(0x00FE, -6200, 0, 68800, 12000, 0x00)
    ChrWalkTo(0x00FE, -5100, 0, 64500, 13000, 0x00)
    ChrWalkTo(0x00FE, -6200, 0, 58700, 13000, 0x00)
    ChrWalkTo(0x00FE, -9600, 0, 48500, 13000, 0x00)

    Return()

# id: 0x0004 offset: 0x258B
@scena.Code('func_04_258B')
def func_04_258B():
    ChrSetFlags(0x00FE, 0x0040)
    OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x00000BB8, 0x00)
    ChrWalkTo(0x00FE, -8400, 0, 100000, 10000, 0x00)
    ChrWalkTo(0x00FE, -10700, 0, 86400, 11000, 0x00)
    ChrWalkTo(0x00FE, -8000, 0, 72200, 12000, 0x00)
    ChrWalkTo(0x00FE, -6200, 0, 68800, 12000, 0x00)
    ChrWalkTo(0x00FE, -5100, 0, 64500, 12000, 0x00)
    ChrWalkTo(0x00FE, -6200, 0, 58700, 12000, 0x00)
    ChrWalkTo(0x00FE, -8400, 0, 50800, 12000, 0x00)

    Return()

# id: 0x0005 offset: 0x262C
@scena.Code('func_05_262C')
def func_05_262C():
    ChrWalkTo(0x00FE, 0, 0, 133200, 12000, 0x00)
    ChrWalkTo(0x00FE, -8400, 0, 100000, 13000, 0x00)
    ChrWalkTo(0x00FE, -10700, 0, 86400, 14000, 0x00)
    ChrWalkTo(0x00FE, -8000, 0, 72200, 15000, 0x00)
    TerminateThread(0x0008, 0x02)
    TerminateThread(0x0008, 0x03)
    ChrSetFlags(0x00FE, 0x0004)
    PlaySE(164, 0x00, 0x64)
    ChrJumpTo(0x00FE, -8000, 1500, 66400, 2000, 8000)

    @scena.Lambda('lambda_26AB')
    def lambda_26AB():
        CameraMove(-7300, 0, 56400, 600)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_26AB)

    ChrSetFlags(0x000A, 0x0020)
    ChrSetChipByIndex(0x000A, 2)

    @scena.Lambda('lambda_26CD')
    def lambda_26CD():
        OP_99(0x000A, 0x00, 0x03, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_26CD)

    @scena.Lambda('lambda_26DD')
    def lambda_26DD():
        OP_6C(24000, 800)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_26DD)

    PlaySE(163, 0x00, 0x64)

    @scena.Lambda('lambda_26F2')
    def lambda_26F2():
        ChrJumpTo(0x00FE, -7300, 0, 56400, 2000, 8000)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_26F2)

    WaitForThreadExit(0x000A, 0x0000)

    @scena.Lambda('lambda_2715')
    def lambda_2715():
        OP_99(0x000A, 0x03, 0x07, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_2715)

    PlaySE(505, 0x00, 0x64)
    WaitForThreadExit(0x000A, 0x0003)
    PlaySE(85, 0x00, 0x5A)
    PlayEffect(0x12, 0xFF, 0x00FF, -6800, -2500, 55400, 0, 0, 0, 5000, 5000, 5000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0, 500, 3000, 100)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    ChrTurnDirection(0x0008, 0x000A, 0)
    ChrTurnDirection(0x0009, 0x000A, 0)

    @scena.Lambda('lambda_2790')
    def lambda_2790():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x00002710, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2790)

    @scena.Lambda('lambda_27A6')
    def lambda_27A6():
        ChrJumpTo(0x00FE, -5500, 0, 54700, 500, 6000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_27A6)

    WaitForThreadExit(0x0009, 0x0001)
    ChrTurnDirection(0x0009, 0x000A, 400)

    @scena.Lambda('lambda_27D0')
    def lambda_27D0():
        OP_94(0x01, 0x00FE, 0x00B4, 0x0000012C, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_27D0)

    WaitForThreadExit(0x0008, 0x0001)

    @scena.Lambda('lambda_27EB')
    def lambda_27EB():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000001F4, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_27EB)

    OP_6A(0x0000)
    MapClearFlags(0x00000001)

    Return()

# id: 0x0006 offset: 0x2804
@scena.Code('func_06_2804')
def func_06_2804():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2850',
    )

    ExecExpressionWithValue(
        0x000C,
        0x01,
        (
            (Expr.GetChrWork, 0xB, 0x1),
            (Expr.GetChrWork, 0xA, 0x1),
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
            (Expr.GetChrWork, 0xB, 0x2),
            (Expr.GetChrWork, 0xA, 0x2),
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
            (Expr.GetChrWork, 0xB, 0x3),
            (Expr.GetChrWork, 0xA, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Yield()

    Jump('func_06_2804')

    def _loc_2850(): pass

    label('loc_2850')

    Return()

# id: 0x0007 offset: 0x2851
@scena.Code('func_07_2851')
def func_07_2851():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_287D',
    )

    Sleep(100)

    ChrSetRGBAMask(0x00FE, 255, 255, 255, 100, 0)
    Sleep(100)

    ChrSetRGBAMask(0x000B, 255, 255, 255, 200, 0)

    Jump('func_07_2851')

    def _loc_287D(): pass

    label('loc_287D')

    Return()

# id: 0x0008 offset: 0x287E
@scena.Code('func_08_287E')
def func_08_287E():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_28AA',
    )

    Sleep(50)

    ChrSetRGBAMask(0x00FE, 255, 255, 255, 100, 0)
    Sleep(50)

    ChrSetRGBAMask(0x000B, 255, 255, 255, 200, 0)

    Jump('func_08_287E')

    def _loc_28AA(): pass

    label('loc_28AA')

    Return()

# id: 0x0009 offset: 0x28AB
@scena.Code('func_09_28AB')
def func_09_28AB():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '北　卢安市\n',
            '南　艾尔·雷登　１７５塞尔矩',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

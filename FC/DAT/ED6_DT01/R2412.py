import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import R2412_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R2412   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '黑衣男子'),
    TXT(0x02, '黑衣男子'),
    TXT(0x03, '阿加特'),
    TXT(0x04, '蒙面队长'),
    TXT(0x05, '目标用摄像机'),
    TXT(0x06, ''),
]

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

# id: 0xFFFF offset: 0x2770
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
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

# id: 0x10001 offset: 0xA8
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

# id: 0x10002 offset: 0x12A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
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

# id: 0x10003 offset: 0x1CA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x1CA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x1CA
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
@scena.Code('PreInit')
def PreInit():
    Event(0, 0x0002)

    Return()

# id: 0x0001 offset: 0x1F3
@scena.Code('Init')
def Init():
    OP_16(0x02, 4000, -136000, -52000, 196645)

    Return()

# id: 0x0002 offset: 0x206
@scena.Code('ReInit')
def ReInit():
    FadeIn(2000, 0)
    LoadEffect(0x00, 'craft\\\\cr201_00.eff')
    LoadEffect(0x01, 'craft\\\\cr201_01.eff')
    LoadEffect(0x02, 'craft\\\\cr201_02.eff')
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(-4600, 3000, 117500, 0)
    CameraSetDistance(3400, 0)
    OP_67(0, 3300, -10000, 0)
    OP_6C(52000, 0)
    SetChrPos(0x0008, -4900, 0, 125700, 0)
    SetChrPos(0x0009, -3900, 0, 125000, 0)
    SetChrPos(0x000A, 5300, 0, 139100, 0)

    @scena.Lambda('lambda_02C5')
    def lambda_02C5():
        OP_6C(45000, 5000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_02C5)

    CameraMove(-4600, 0, 117500, 5000)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)

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
        SetChrDirection(0x0009, 0, 800)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0330)

    WaitForThreadExit(0x0008, 0x0001)

    @scena.Lambda('lambda_0343')
    def lambda_0343():
        SetChrDirection(0x0008, 0, 800)

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

    @scena.Lambda('lambda_03B1')
    def lambda_03B1():
        OP_6C(21000, 3000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_03B1)

    CreateThread(0x000A, 0x01, 0x00, 0x0005)

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

    CreateThread(0x0008, 0x01, 0x00, 0x0003)
    Sleep(200)

    CreateThread(0x0009, 0x01, 0x00, 0x0004)
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

    @scena.Lambda('lambda_0488')
    def lambda_0488():
        OP_6C(348000, 4000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0488)

    Sleep(500)

    ChrJumpTo(0x000A, -8000, 0, 58200, 500, 6000)
    PlaySE(164, 0x00, 0x64)
    OP_99(0x000A, 0x07, 0x00, 2000)
    ClearChrFlags(0x000A, 0x0800)
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

    @scena.Lambda('lambda_04F3')
    def lambda_04F3():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_04F3')

    DispatchAsync2(0x0008, 0x0000, lambda_04F3)

    @scena.Lambda('lambda_0504')
    def lambda_0504():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_0504')

    DispatchAsync2(0x0009, 0x0000, lambda_0504)

    @scena.Lambda('lambda_0515')
    def lambda_0515():
        ChrJumpTo(0x0008, -4890, 30, 52030, 800, 5000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0515)

    WaitForThreadExit(0x0008, 0x0001)
    SetChrChipByIndex(0x0008, 4)
    SetChrSubChip(0x0008, 0)
    Sleep(100)

    @scena.Lambda('lambda_0547')
    def lambda_0547():
        ChrJumpTo(0x0009, -7220, 20, 50760, 800, 5000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0547)

    WaitForThreadExit(0x0009, 0x0001)
    SetChrChipByIndex(0x0009, 4)
    SetChrSubChip(0x0009, 0)
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

    @scena.Lambda('lambda_077C')
    def lambda_077C():
        OP_6E(243, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_077C)

    @scena.Lambda('lambda_078C')
    def lambda_078C():
        CameraMove(-7660, 0, 57680, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_078C)

    PlayEffect(0x01, 0x01, 0x000A, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_07D9')
    def lambda_07D9():
        OP_99(0x00FE, 0x00, 0x04, 2600)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_07D9)

    SetChrChipByIndex(0x0008, 5)
    SetChrChipByIndex(0x0009, 5)
    ChrTurnDirection(0x0008, 0x000A, 0)
    ChrTurnDirection(0x0009, 0x000A, 0)

    @scena.Lambda('lambda_0801')
    def lambda_0801():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000005DC, 0x000005DC, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0801)

    @scena.Lambda('lambda_0817')
    def lambda_0817():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000005DC, 0x000005DC, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_0817)

    Sleep(500)

    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    Sleep(100)

    @scena.Lambda('lambda_083F')
    def lambda_083F():
        OP_94(0x01, 0x00FE, 0x0000, 0x00002328, 0x00002710, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_083F)

    Sleep(50)

    @scena.Lambda('lambda_085A')
    def lambda_085A():
        OP_94(0x01, 0x00FE, 0x0000, 0x00002328, 0x00002710, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_085A)

    Sleep(400)

    StopEffect(0x01, 0x02)
    PlayEffect(0x00, 0xFF, 0x000A, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_08AD')
    def lambda_08AD():
        OP_99(0x00FE, 0x04, 0x07, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_08AD)

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

    SetChrChipByIndex(0x0008, 7)
    SetChrFlags(0x0008, 0x0020)

    @scena.Lambda('lambda_090C')
    def lambda_090C():
        OP_94(0x01, 0x00FE, 0x00B4, 0x00000FA0, 0x00004E20, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_090C)

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

    SetChrChipByIndex(0x0009, 7)
    SetChrFlags(0x0009, 0x0020)

    @scena.Lambda('lambda_0971')
    def lambda_0971():
        OP_94(0x01, 0x00FE, 0x00B4, 0x00000FA0, 0x00003A98, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0971)

    @scena.Lambda('lambda_0987')
    def lambda_0987():
        OP_94(0x01, 0x00FE, 0x00B4, 0x00000FA0, 0x00004E20, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_0987)

    Sleep(50)

    @scena.Lambda('lambda_09A2')
    def lambda_09A2():
        OP_94(0x01, 0x00FE, 0x00B4, 0x00000FA0, 0x00002710, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_09A2)

    @scena.Lambda('lambda_09B8')
    def lambda_09B8():
        OP_94(0x01, 0x00FE, 0x00B4, 0x00000FA0, 0x00003A98, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_09B8)

    Sleep(50)

    @scena.Lambda('lambda_09D3')
    def lambda_09D3():
        OP_94(0x01, 0x00FE, 0x00B4, 0x00000FA0, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_09D3)

    @scena.Lambda('lambda_09E9')
    def lambda_09E9():
        OP_94(0x01, 0x00FE, 0x00B4, 0x00000FA0, 0x00002710, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_09E9)

    Sleep(50)

    @scena.Lambda('lambda_0A04')
    def lambda_0A04():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0A04)

    @scena.Lambda('lambda_0A1A')
    def lambda_0A1A():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_0A1A)

    Sleep(50)

    @scena.Lambda('lambda_0A35')
    def lambda_0A35():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_0A35)

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
    SetChrPos(0x0008, -8400, 0, 54200, 0)
    SetChrPos(0x0009, -9800, 0, 54800, 0)
    SetChrPos(0x000B, -6700, 0, 58700, 180)
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

    @scena.Lambda('lambda_0B9A')
    def lambda_0B9A():
        SetChrDirection(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0B9A)

    @scena.Lambda('lambda_0BA8')
    def lambda_0BA8():
        OP_99(0x00FE, 0x05, 0x00, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0BA8)

    ChrJumpTo(0x000A, -7300, 0, 56400, 700, 4000)
    TerminateThread(0x000A, 0x02)
    SetChrChipByIndex(0x000A, 14)
    SetChrSubChip(0x000A, 0)
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
    SetChrPos(0x000B, -4010, 0, 61460, 270)
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

    SetChrChipByIndex(0x000A, 14)
    SetChrSubChip(0x000A, 0)
    SetChrDirection(0x000A, 43, 600)

    ChrTalk(
        0x000A,
        (
            '#0050070024V#052F#4P什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlayBGM(81)
    SetChrChipByIndex(0x000B, 13)
    ClearChrFlags(0x000B, 0x0080)

    @scena.Lambda('lambda_0CFD')
    def lambda_0CFD():
        CameraMove(-6790, 0, 56980, 1500)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_0CFD)

    @scena.Lambda('lambda_0D15')
    def lambda_0D15():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1500)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_0D15)

    @scena.Lambda('lambda_0D27')
    def lambda_0D27():
        ChrWalkTo(0x00FE, -6700, 0, 58700, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0D27)

    SetChrChipByIndex(0x000A, 2)
    SetChrSubChip(0x000A, 7)

    @scena.Lambda('lambda_0D4C')
    def lambda_0D4C():
        SetChrDirection(0x00FE, 0, 800)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0D4C)

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

    @scena.Lambda('lambda_0D9B')
    def lambda_0D9B():
        OP_99(0x0008, 0x03, 0x00, 1000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0D9B)

    ChrTalk(
        0x0008,
        (
            '#2620070026V队、队长！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0DC2')
    def lambda_0DC2():
        OP_99(0x0009, 0x03, 0x00, 1000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0DC2)

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
    SetChrChipByIndex(0x0008, 5)
    ClearChrFlags(0x0008, 0x0020)

    @scena.Lambda('lambda_10BC')
    def lambda_10BC():
        ChrWalkTo(0x00FE, -8900, 0, 43900, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_10BC)

    ChrTalk(
        0x0009,
        (
            '#2630070044V多谢队长！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0009, 5)
    ClearChrFlags(0x0008, 0x0020)

    @scena.Lambda('lambda_10F8')
    def lambda_10F8():
        ChrWalkTo(0x00FE, -8900, 0, 43900, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_10F8)

    SetChrChipByIndex(0x000A, 14)
    SetChrSubChip(0x000A, 0)

    @scena.Lambda('lambda_111D')
    def lambda_111D():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_111D')

    DispatchAsync2(0x000A, 0x0001, lambda_111D)

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
    SetChrChipByIndex(0x000B, 9)
    ChrWalkTo(0x000B, -7400, 0, 57000, 7000, 0x00)

    @scena.Lambda('lambda_1172')
    def lambda_1172():
        OP_6C(0, 2000)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_1172)

    @scena.Lambda('lambda_1182')
    def lambda_1182():
        CameraMove(-9340, 0, 52260, 1000)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_1182)

    @scena.Lambda('lambda_119A')
    def lambda_119A():
        OP_97(0x00FE, -5100, 53300, -75000, 14000, 0x0001)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_119A)

    SetChrChipByIndex(0x000A, 1)
    ChrWalkTo(0x000A, -8300, 0, 53000, 7000, 0x00)
    ChrTurnDirection(0x000A, 0x000B, 0)

    @scena.Lambda('lambda_11D6')
    def lambda_11D6():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_11D6')

    DispatchAsync2(0x000B, 0x0000, lambda_11D6)

    SetChrChipByIndex(0x000A, 14)

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

    SetChrChipByIndex(0x000B, 8)

    @scena.Lambda('lambda_1207')
    def lambda_1207():
        ChrJumpTo(0x00FE, -7900, -50, 53420, 400, 3000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_1207)

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

    @scena.Lambda('lambda_1331')
    def lambda_1331():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_1331')

    DispatchAsync2(0x000A, 0x0000, lambda_1331)

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
    SetChrFlags(0x000B, 0x0004)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)

    @scena.Lambda('lambda_1374')
    def lambda_1374():
        OP_6C(315000, 1000)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_1374)

    ClearChrFlags(0x000A, 0x0020)
    SetChrChipByIndex(0x000A, 1)
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
    CreateThread(0x0008, 0x01, 0x00, 0x0006)
    OP_93(0x000A, 0x000B, 1600, 12000, 0x00)
    SetChrFlags(0x000A, 0x0020)
    SetChrChipByIndex(0x000B, 12)
    SetChrSubChip(0x000B, 0)
    SetChrChipByIndex(0x000A, 15)
    SetChrSubChip(0x000A, 0)
    PlaySE(505, 0x00, 0x64)

    @scena.Lambda('lambda_1419')
    def lambda_1419():
        OP_94(0x01, 0x00FE, 0x0000, 0x000000C8, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1419)

    @scena.Lambda('lambda_142F')
    def lambda_142F():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000000C8, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_142F)

    OP_9E(0x000B, 30, 0, 300, 5000)
    WaitForThreadExit(0x000B, 0x0001)

    @scena.Lambda('lambda_145D')
    def lambda_145D():
        OP_94(0x01, 0x00FE, 0x0000, 0x000005DC, 0x00001B58, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_145D)

    SetChrChipByIndex(0x000B, 8)
    SetChrSubChip(0x000B, 0)
    PlaySE(163, 0x00, 0x64)
    SetChrChipByIndex(0x000A, 2)
    SetChrSubChip(0x000A, 7)
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

    SetChrChipByIndex(0x000B, 10)
    TerminateThread(0x000B, 0xFF)

    @scena.Lambda('lambda_14BC')
    def lambda_14BC():
        ChrJumpTo(0x00FE, -10200, 1300, 50800, 1000, 10000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_14BC)

    @scena.Lambda('lambda_14DA')
    def lambda_14DA():
        OP_99(0x00FE, 0x00, 0x07, 2000)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_14DA)

    Sleep(200)

    PlaySE(501, 0x00, 0x64)

    @scena.Lambda('lambda_14F4')
    def lambda_14F4():
        ChrJumpTo(0x00FE, -9200, 0, 53000, 1000, 10000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_14F4)

    @scena.Lambda('lambda_1512')
    def lambda_1512():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_1512')

    DispatchAsync2(0x000B, 0x0000, lambda_1512)

    SetChrChipByIndex(0x000A, 1)
    WaitForThreadExit(0x000B, 0x0001)
    PlaySE(164, 0x00, 0x64)
    ChrJumpTo(0x000B, -9500, 0, 47800, 1000, 10000)
    PlaySE(164, 0x00, 0x64)

    @scena.Lambda('lambda_154E')
    def lambda_154E():
        OP_99(0x00FE, 0x07, 0x0B, 1500)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_154E)

    CameraSetDistance(2900, 1000)
    SetChrChipByIndex(0x000B, 9)

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

    @scena.Lambda('lambda_1593')
    def lambda_1593():
        CameraSetDistance(2500, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1593)

    ChrJumpTo(0x000B, -9900, 0, 50100, 500, 7000)
    PlaySE(164, 0x00, 0x64)

    @scena.Lambda('lambda_15BF')
    def lambda_15BF():
        SetChrDirection(0x000A, 30, 500)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_15BF)

    ChrJumpTo(0x000B, -7800, 0, 51800, 500, 10000)
    PlaySE(164, 0x00, 0x64)

    @scena.Lambda('lambda_15E9')
    def lambda_15E9():
        ChrJumpTo(0x000B, -9000, 0, 52000, 500, 10000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_15E9)

    TerminateThread(0x000A, 0xFF)
    PlaySE(505, 0x00, 0x64)
    SetChrDirection(0x000A, 315, 1300)

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x000B, 8)

    @scena.Lambda('lambda_1627')
    def lambda_1627():
        ChrJumpTo(0x00FE, -9500, 500, 51900, 1000, 7000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1627)

    SetChrDirection(0x000A, 135, 1600)
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

    SetChrChipByIndex(0x000B, 10)

    @scena.Lambda('lambda_1661')
    def lambda_1661():
        OP_99(0x00FE, 0x00, 0x02, 3000)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_1661)

    SetChrDirection(0x000A, 225, 0)
    SetChrChipByIndex(0x000A, 2)
    OP_99(0x000A, 0x06, 0x07, 1500)

    @scena.Lambda('lambda_1686')
    def lambda_1686():
        OP_99(0x000A, 0x05, 0x00, 3000)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_1686)

    PlaySE(163, 0x00, 0x64)

    @scena.Lambda('lambda_169B')
    def lambda_169B():
        OP_99(0x00FE, 0x02, 0x00, 3000)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_169B)

    @scena.Lambda('lambda_16AB')
    def lambda_16AB():
        ChrJumpTo(0x000B, -8900, 0, 56800, 4000, 7000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_16AB)

    Sleep(200)

    @scena.Lambda('lambda_16CE')
    def lambda_16CE():
        SetChrDirection(0x000A, 0, 500)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_16CE)

    Sleep(300)

    @scena.Lambda('lambda_16E1')
    def lambda_16E1():
        OP_99(0x00FE, 0x00, 0x07, 3000)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_16E1)

    PlaySE(164, 0x00, 0x64)
    PlaySE(163, 0x00, 0x64)

    @scena.Lambda('lambda_16FB')
    def lambda_16FB():
        ChrJumpTo(0x000A, -8900, 0, 55900, 2000, 10000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_16FB)

    @scena.Lambda('lambda_1719')
    def lambda_1719():
        OP_99(0x000A, 0x00, 0x07, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_1719)

    Sleep(200)

    PlaySE(505, 0x00, 0x64)
    Sleep(200)

    @scena.Lambda('lambda_1738')
    def lambda_1738():
        OP_99(0x00FE, 0x07, 0x0B, 1500)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_1738)

    ChrMoveTo(0x000B, -7350, 0, 56800, 15000, 0x00)
    WaitForThreadExit(0x000A, 0x0001)
    PlaySE(164, 0x00, 0x64)
    PlaySE(85, 0x00, 0x5A)
    PlayEffect(0x12, 0xFF, 0x00FF, -8610, -1000, 56740, 0, 0, 0, 3000, 3000, 3000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0, 500, 3000, 100)
    ChrJumpTo(0x000B, -5000, 0, 56700, 1300, 5000)
    PlaySE(164, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_17D2')
    def lambda_17D2():
        OP_99(0x000A, 0x07, 0x00, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_17D2)

    @scena.Lambda('lambda_17E2')
    def lambda_17E2():
        ChrTurnDirection(0x000A, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_17E2)

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

    @scena.Lambda('lambda_1A39')
    def lambda_1A39():
        OP_9E(0x00FE, 30, 0, 1000, 5000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1A39)

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

    SetChrChipByIndex(0x000B, 12)

    @scena.Lambda('lambda_1B1E')
    def lambda_1B1E():
        OP_9E(0x00FE, 30, 0, 1000, 5000)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_1B1E)

    PlayEffect(0x00, 0x01, 0x000B, 0, 200, 0, 0, 0, 0, 900, 900, 900, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_1B6D')
    def lambda_1B6D():
        OP_9E(0x00FE, 30, 0, 1000, 5000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1B6D)

    Sleep(1000)

    @scena.Lambda('lambda_1B8C')
    def lambda_1B8C():
        OP_6C(0, 6000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_1B8C)

    @scena.Lambda('lambda_1B9C')
    def lambda_1B9C():
        OP_9E(0x00FE, 30, 0, 1000, 5000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1B9C)

    ChrTalk(
        0x000A,
        (
            '#0050070068V#15A#054F哦哦哦哦哦哦哦！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(3000)

    @scena.Lambda('lambda_1BE1')
    def lambda_1BE1():
        OP_9E(0x00FE, 30, 0, 1000, 5000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1BE1)

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
    SetChrFlags(0x000B, 0x0040)
    SetChrFlags(0x000A, 0x0040)
    OP_99(0x000A, 0x00, 0x03, 2000)

    @scena.Lambda('lambda_1C42')
    def lambda_1C42():
        OP_99(0x000A, 0x03, 0x07, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_1C42)

    @scena.Lambda('lambda_1C52')
    def lambda_1C52():
        ChrTurnDirection(0x000A, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_1C52)

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

    SetChrChipByIndex(0x000B, 10)

    @scena.Lambda('lambda_1C79')
    def lambda_1C79():
        OP_99(0x00FE, 0x00, 0x03, 3000)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_1C79)

    @scena.Lambda('lambda_1C89')
    def lambda_1C89():
        ChrWalkTo(0x00FE, -8900, 0, 55900, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1C89)

    @scena.Lambda('lambda_1CA4')
    def lambda_1CA4():
        ChrWalkTo(0x00FE, -5000, 0, 56700, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1CA4)

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

    @scena.Lambda('lambda_1D6C')
    def lambda_1D6C():
        OP_99(0x00FE, 0x03, 0x07, 1000)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_1D6C)

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
    SetChrChipByIndex(0x000B, 11)
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

    @scena.Lambda('lambda_1DC8')
    def lambda_1DC8():
        OP_99(0x000A, 0x07, 0x00, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_1DC8)

    SetChrDirection(0x000A, 225, 400)
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
    CreateThread(0x000B, 0x01, 0x00, 0x0007)
    Sleep(1000)

    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    SetChrChipByIndex(0x000A, 14)
    SetChrSubChip(0x000A, 0)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '#0050070073V#052F什、什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x000B, 0x01, 0x00, 0x0008)
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
    SetChrName('')

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
    SetChrName('青年的声音')
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

    SetChrName('青年的声音')

    Talk(
        (
            '#0140070076V#50W不错的一击，\n',
            '只是似乎还带有些迷惘啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrName('青年的声音')

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
    SetChrName('青年的声音')

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
    SetChrName('')

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

    ClearMapFlags(0x00000001)

    @scena.Lambda('lambda_2155')
    def lambda_2155():
        CameraMove(-5100, 1400, 56900, 1600)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_2155)

    WaitForThreadExit(0x000A, 0x0002)
    SetChrChipByIndex(0x000A, 15)
    SetChrSubChip(0x000A, 0)
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

    @scena.Lambda('lambda_220B')
    def lambda_220B():
        CameraSetDistance(2400, 2000)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_220B)

    @scena.Lambda('lambda_221B')
    def lambda_221B():
        OP_67(0, 6000, -10000, 2300)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_221B)

    @scena.Lambda('lambda_2233')
    def lambda_2233():
        OP_6C(54000, 2000)

        ExitThread()

    DispatchAsync(0x000B, 0x0000, lambda_2233)

    Sleep(1000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_2251')
    def lambda_2251():
        CameraSetDistance(5000, 3000)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_2251)

    @scena.Lambda('lambda_2261')
    def lambda_2261():
        OP_9E(0x00FE, 30, 0, 2000, 5000)
        Yield()

        Jump('lambda_2261')

    DispatchAsync2(0x000A, 0x0000, lambda_2261)

    SetChrSubChip(0x000A, 1)

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

# id: 0x0003 offset: 0x22FC
@scena.Code('func_03_22FC')
def func_03_22FC():
    SetChrFlags(0x00FE, 0x0040)
    OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x00000BB8, 0x00)
    ChrWalkTo(0x00FE, -8400, 0, 100000, 10000, 0x00)
    ChrWalkTo(0x00FE, -10700, 0, 86400, 10000, 0x00)

    @scena.Lambda('lambda_233E')
    def lambda_233E():
        OP_6C(324000, 3000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_233E)

    @scena.Lambda('lambda_234E')
    def lambda_234E():
        OP_67(0, 5200, -10000, 3000)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_234E)

    @scena.Lambda('lambda_2366')
    def lambda_2366():
        CameraMove(-8000, 1300, 66400, 2700)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_2366)

    ClearMapFlags(0x00000001)
    ChrWalkTo(0x00FE, -8000, 0, 72200, 12000, 0x00)
    ChrWalkTo(0x00FE, -6200, 0, 68800, 12000, 0x00)
    ChrWalkTo(0x00FE, -5100, 0, 64500, 13000, 0x00)
    ChrWalkTo(0x00FE, -6200, 0, 58700, 13000, 0x00)
    ChrWalkTo(0x00FE, -9600, 0, 48500, 13000, 0x00)

    Return()

# id: 0x0004 offset: 0x23E2
@scena.Code('func_04_23E2')
def func_04_23E2():
    SetChrFlags(0x00FE, 0x0040)
    OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x00000BB8, 0x00)
    ChrWalkTo(0x00FE, -8400, 0, 100000, 10000, 0x00)
    ChrWalkTo(0x00FE, -10700, 0, 86400, 11000, 0x00)
    ChrWalkTo(0x00FE, -8000, 0, 72200, 12000, 0x00)
    ChrWalkTo(0x00FE, -6200, 0, 68800, 12000, 0x00)
    ChrWalkTo(0x00FE, -5100, 0, 64500, 12000, 0x00)
    ChrWalkTo(0x00FE, -6200, 0, 58700, 12000, 0x00)
    ChrWalkTo(0x00FE, -8400, 0, 50800, 12000, 0x00)

    Return()

# id: 0x0005 offset: 0x2483
@scena.Code('func_05_2483')
def func_05_2483():
    ChrWalkTo(0x00FE, 0, 0, 133200, 12000, 0x00)
    ChrWalkTo(0x00FE, -8400, 0, 100000, 13000, 0x00)
    ChrWalkTo(0x00FE, -10700, 0, 86400, 14000, 0x00)
    ChrWalkTo(0x00FE, -8000, 0, 72200, 15000, 0x00)
    TerminateThread(0x0008, 0x02)
    TerminateThread(0x0008, 0x03)
    SetChrFlags(0x00FE, 0x0004)
    PlaySE(164, 0x00, 0x64)
    ChrJumpTo(0x00FE, -8000, 1500, 66400, 2000, 8000)

    @scena.Lambda('lambda_2502')
    def lambda_2502():
        CameraMove(-7300, 0, 56400, 600)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_2502)

    SetChrFlags(0x000A, 0x0020)
    SetChrChipByIndex(0x000A, 2)

    @scena.Lambda('lambda_2524')
    def lambda_2524():
        OP_99(0x000A, 0x00, 0x03, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_2524)

    @scena.Lambda('lambda_2534')
    def lambda_2534():
        OP_6C(24000, 800)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_2534)

    PlaySE(163, 0x00, 0x64)

    @scena.Lambda('lambda_2549')
    def lambda_2549():
        ChrJumpTo(0x00FE, -7300, 0, 56400, 2000, 8000)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_2549)

    WaitForThreadExit(0x000A, 0x0000)

    @scena.Lambda('lambda_256C')
    def lambda_256C():
        OP_99(0x000A, 0x03, 0x07, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_256C)

    PlaySE(505, 0x00, 0x64)
    WaitForThreadExit(0x000A, 0x0003)
    PlaySE(85, 0x00, 0x5A)
    PlayEffect(0x12, 0xFF, 0x00FF, -6800, -2500, 55400, 0, 0, 0, 5000, 5000, 5000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0, 500, 3000, 100)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    ChrTurnDirection(0x0008, 0x000A, 0)
    ChrTurnDirection(0x0009, 0x000A, 0)

    @scena.Lambda('lambda_25E7')
    def lambda_25E7():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x00002710, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_25E7)

    @scena.Lambda('lambda_25FD')
    def lambda_25FD():
        ChrJumpTo(0x00FE, -5500, 0, 54700, 500, 6000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_25FD)

    WaitForThreadExit(0x0009, 0x0001)
    ChrTurnDirection(0x0009, 0x000A, 400)

    @scena.Lambda('lambda_2627')
    def lambda_2627():
        OP_94(0x01, 0x00FE, 0x00B4, 0x0000012C, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2627)

    WaitForThreadExit(0x0008, 0x0001)

    @scena.Lambda('lambda_2642')
    def lambda_2642():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000001F4, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2642)

    OP_6A(0x0000)
    ClearMapFlags(0x00000001)

    Return()

# id: 0x0006 offset: 0x265B
@scena.Code('func_06_265B')
def func_06_265B():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_26A7',
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

    Jump('func_06_265B')

    def _loc_26A7(): pass

    label('loc_26A7')

    Return()

# id: 0x0007 offset: 0x26A8
@scena.Code('func_07_26A8')
def func_07_26A8():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_26D4',
    )

    Sleep(100)

    ChrSetRGBAMask(0x00FE, 255, 255, 255, 100, 0)
    Sleep(100)

    ChrSetRGBAMask(0x000B, 255, 255, 255, 200, 0)

    Jump('func_07_26A8')

    def _loc_26D4(): pass

    label('loc_26D4')

    Return()

# id: 0x0008 offset: 0x26D5
@scena.Code('func_08_26D5')
def func_08_26D5():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2701',
    )

    Sleep(50)

    ChrSetRGBAMask(0x00FE, 255, 255, 255, 100, 0)
    Sleep(50)

    ChrSetRGBAMask(0x000B, 255, 255, 255, 200, 0)

    Jump('func_08_26D5')

    def _loc_2701(): pass

    label('loc_2701')

    Return()

# id: 0x0009 offset: 0x2702
@scena.Code('func_09_2702')
def func_09_2702():
    FadeOut(300, 0, 100)
    SetChrName('')
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

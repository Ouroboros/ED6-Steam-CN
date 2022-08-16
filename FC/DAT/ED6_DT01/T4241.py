import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4241_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4241   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4241.x'
    header.mapIndex       = 1
    header.bgm            = 17
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
        ('ED6_DT07/CH02010._CH', 'ED6_DT07/CH02010P._CP'),
        ('ED6_DT07/CH02090._CH', 'ED6_DT07/CH02090P._CP'),
        ('ED6_DT07/CH00010._CH', 'ED6_DT07/CH00010P._CP'),
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP'),
        ('ED6_DT06/CH20053._CH', 'ED6_DT06/CH20053P._CP'),
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT07/CH02020._CH', 'ED6_DT07/CH02020P._CP'),
        ('ED6_DT07/CH01320._CH', 'ED6_DT07/CH01320P._CP'),
        ('ED6_DT06/CH20141._CH', 'ED6_DT06/CH20141P._CP'),
        ('ED6_DT07/CH00061._CH', 'ED6_DT07/CH00061P._CP'),
    ]

# id: 0x10001 offset: 0x102
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '艾莉茜雅女王',
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
            name                = '尤莉亚中尉',
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
            name                = '约修亚',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '奥利维尔',
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
            name                = '金',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
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
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '提妲',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '拉赛尔博士',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '亲卫队员',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '导力梯',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x242
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x242
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x242
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x242
@scena.Code('Init')
def Init():
    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x21),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_02_278)

    Return()

# id: 0x0001 offset: 0x253
@scena.Code('func_01_253')
def func_01_253():
    OP_A1(0x0011, 0x0002)
    ChrSetPos(0x0011, 0, 0, 0, 0)
    ChrSetFlags(0x0011, 0x0004)

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0002 offset: 0x278
@scena.Code('func_02_278')
def func_02_278():
    EventBegin(0x00)
    CameraMove(-10, 0, -72410, 0)
    OP_67(0, 7490, -10000, 0)
    CameraSetDistance(1830, 0)
    OP_6C(45000, 0)
    OP_6E(536, 0)
    ChrSetPos(0x0101, -1190, 0, -72040, 0)
    ChrSetPos(0x0105, -1330, 0, -73970, 0)
    ChrSetPos(0x0103, -30, 0, -72830, 0)
    ChrSetFlags(0x0008, 0x0040)
    ChrSetFlags(0x0009, 0x0040)
    ChrSetFlags(0x000A, 0x0040)
    ChrSetFlags(0x000B, 0x0040)
    ChrSetFlags(0x000C, 0x0040)
    ChrSetFlags(0x0101, 0x0040)
    ChrSetFlags(0x0105, 0x0040)
    ChrSetFlags(0x0103, 0x0040)
    ChrSetPos(0x0008, 80, 0, -70380, 0)
    ChrSetPos(0x0009, 890, 0, -71230, 0)
    ChrSetPos(0x000A, -2230, 0, -70590, 0)
    ChrSetPos(0x000B, 640, 0, -73900, 0)
    ChrSetPos(0x000C, 2070, 0, -73010, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)

    @scena.Lambda('lambda_0386')
    def lambda_0386():
        ChrWalkTo(0x00FE, -1500, 0, -68350, 1100, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0386)

    @scena.Lambda('lambda_03A1')
    def lambda_03A1():
        ChrWalkTo(0x00FE, -1070, 0, -69740, 1300, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_03A1)

    @scena.Lambda('lambda_03BC')
    def lambda_03BC():
        ChrWalkTo(0x00FE, 420, 0, -68720, 1300, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_03BC)

    @scena.Lambda('lambda_03D7')
    def lambda_03D7():
        ChrWalkTo(0x00FE, 80, 0, -67380, 1400, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_03D7)

    @scena.Lambda('lambda_03F2')
    def lambda_03F2():
        ChrWalkTo(0x00FE, 1160, 0, -67680, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_03F2)

    @scena.Lambda('lambda_040D')
    def lambda_040D():
        ChrWalkTo(0x00FE, -2230, 0, -67590, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_040D)

    @scena.Lambda('lambda_0428')
    def lambda_0428():
        ChrWalkTo(0x00FE, 640, 0, -69890, 1100, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0428)

    @scena.Lambda('lambda_0443')
    def lambda_0443():
        ChrWalkTo(0x00FE, 2070, 0, -69160, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0443)

    @scena.Lambda('lambda_045E')
    def lambda_045E():
        CameraMove(110, 0, -66230, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_045E)

    FadeIn(1000, 0)
    WaitForThreadExit(0x0000, 0x0002)
    Fade(500)
    CameraMove(110, 0, -66230, 0)
    OP_67(0, 7490, -10000, 0)
    CameraSetDistance(1470, 0)
    OP_6C(45000, 0)
    OP_6E(536, 0)
    OP_0D()

    ChrTalk(
        0x0009,
        (
            '#0100131459V#173F#2P这种地方居然有一部导力梯……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100131460V#177F以前是绝对没有的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0080131461V#072F这东西是上校特意建造的吧……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080131462V如此说来，乘坐这个导力梯应该就可以\n',
            '降落到封印『辉之环』的地方吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630121141V#093F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630131464V#094F也许，这正是理查德上校\n',
            '发动这次政变背后所隐藏的真正原因。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630131465V也只有控制了王城之后，\n',
            '才能达到他们建造出这东西的目的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010131466V#580F竟然、竟然会是这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0040131467V#035F呵呵，可能就是如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040131468V#030F无论是什么国家，\n',
            '由王权守护的圣域都是不可侵犯的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040131469V如果想要打破这一点，\n',
            '就必须下决心使出强硬的手段才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0020131470V#012F不管怎样，想要降落到地下，\n',
            '就必须要使用这个导力梯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020131471V先把它启动了再说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_07A7')
    def lambda_07A7():
        CameraMove(-40, 0, -62650, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_07A7)

    ChrWalkTo(0x000A, -920, 0, -66390, 3000, 0x00)
    ChrWalkTo(0x000A, -550, 60, -65970, 3000, 0x00)
    ChrWalkTo(0x000A, 10, 100, -61260, 3000, 0x00)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '约修亚开始调查导力梯的控电盘。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0105, 0xFF)
    TerminateThread(0x0103, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000C, 0xFF)
    OP_62(0x000A, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(2000)

    OP_63(0x000A)

    ChrTalk(
        0x000A,
        (
            '#0020131472V#014F#5P#4S！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010131473V#004F怎么了啊，约修亚？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_08CC')
    def lambda_08CC():
        CameraMove(110, 0, -66230, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_08CC)

    ChrTurnDirection(0x000A, 0x0101, 400)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x000A,
        (
            '#0020131474V#012F这个东西……\n',
            '用导力的加密方式锁住了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020131475V没有由特殊结晶回路组成的钥匙，\n',
            '是不能将导力梯启动的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_096F')
    def lambda_096F():
        ChrWalkTo(0x00FE, -160, 0, -65050, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_096F)

    ChrTalk(
        0x0101,
        (
            '#0010131476V#005F岂、岂有此理～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060131477V#043F怎么会这样，都到了这里了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0008, 400)

    ChrTalk(
        0x0009,
        (
            '#0100131478V#177F#2P把拘捕到的特务兵绑过来问话！\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100131479V钥匙一定是藏在某个地方了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630131480V#093F嗯……\n',
            '看来只有这个办法了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x000D, 0x0040)
    ChrSetFlags(0x000E, 0x0040)
    ChrSetFlags(0x000F, 0x0040)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetRGBAMask(0x000D, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x000E, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x000F, 255, 255, 255, 0, 0)
    ChrSetPos(0x000D, 20, 0, -77690, 0)
    ChrSetPos(0x000E, 20, 0, -77690, 0)
    ChrSetPos(0x000F, -1020, 0, -74230, 0)

    @scena.Lambda('lambda_0AF2')
    def lambda_0AF2():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_0AF2)

    NpcTalk(
        0x000F,
        '老人的声音',
        (
            '#0540131481V#1P不，还没有到那种地步。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0B3A')
    def lambda_0B3A():
        CameraMove(-550, 0, -69950, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_0B3A)

    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_0B80')
    def lambda_0B80():
        ChrTurnDirection(0x00FE, 0x000F, 400)
        Yield()

        Jump('lambda_0B80')

    DispatchAsync2(0x0101, 0x0001, lambda_0B80)

    Sleep(50)

    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_0BC4')
    def lambda_0BC4():
        ChrTurnDirection(0x00FE, 0x000F, 400)
        Yield()

        Jump('lambda_0BC4')

    DispatchAsync2(0x0105, 0x0001, lambda_0BC4)

    @scena.Lambda('lambda_0BD5')
    def lambda_0BD5():
        ChrTurnDirection(0x00FE, 0x000F, 400)
        Yield()

        Jump('lambda_0BD5')

    DispatchAsync2(0x0103, 0x0001, lambda_0BD5)

    Sleep(50)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_0C19')
    def lambda_0C19():
        ChrTurnDirection(0x00FE, 0x000F, 400)
        Yield()

        Jump('lambda_0C19')

    DispatchAsync2(0x0008, 0x0001, lambda_0C19)

    @scena.Lambda('lambda_0C2A')
    def lambda_0C2A():
        ChrTurnDirection(0x00FE, 0x000F, 400)
        Yield()

        Jump('lambda_0C2A')

    DispatchAsync2(0x0009, 0x0001, lambda_0C2A)

    Sleep(50)

    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_0C6E')
    def lambda_0C6E():
        ChrTurnDirection(0x00FE, 0x000F, 400)
        Yield()

        Jump('lambda_0C6E')

    DispatchAsync2(0x000B, 0x0001, lambda_0C6E)

    @scena.Lambda('lambda_0C7F')
    def lambda_0C7F():
        ChrTurnDirection(0x00FE, 0x000F, 400)
        Yield()

        Jump('lambda_0C7F')

    DispatchAsync2(0x000C, 0x0001, lambda_0C7F)

    WaitForThreadExit(0x0000, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010130371V#004F咦……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0020131483V#014F难道是……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630131484V#097F哦……是拉赛尔博士！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0D04')
    def lambda_0D04():
        CameraMove(-400, 0, -68560, 2500)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_0D04)

    @scena.Lambda('lambda_0D1C')
    def lambda_0D1C():
        ChrWalkTo(0x00FE, -690, 0, -71190, 1600, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_0D1C)

    Sleep(200)

    ChrSetFlags(0x000A, 0x0004)

    @scena.Lambda('lambda_0D41')
    def lambda_0D41():
        ChrWalkTo(0x00FE, -2940, 0, -68350, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0D41)

    @scena.Lambda('lambda_0D5C')
    def lambda_0D5C():
        ChrTurnDirection(0x00FE, 0x000F, 0)
        Yield()

        Jump('lambda_0D5C')

    DispatchAsync2(0x000A, 0x0001, lambda_0D5C)

    WaitForThreadExit(0x0000, 0x0002)

    ChrTalk(
        0x000F,
        (
            '#0540131485V#101F艾莉茜雅。久疏问候了啊。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540131486V哈哈……一阵子没见，\n',
            '艾丝蒂尔和约修亚看来也很精神嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010131487V#004F#5P等、等一下……\n',
            '为什么博士会在这里？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010131488V不是在被情报部追捕中吗。\n',
            '应该还没有逃出蔡斯地区才对啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0E6B')
    def lambda_0E6B():
        ChrTurnDirection(0x00FE, 0x000E, 400)
        Yield()

        Jump('lambda_0E6B')

    DispatchAsync2(0x000A, 0x0001, lambda_0E6B)

    ChrTalk(
        0x000A,
        (
            '#0020131489V#014F#5P能平安无事已经是最好了，\n',
            '不过，既然博士都到这里来的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x000E, -900, 0, -77820, 0)

    NpcTalk(
        0x000E,
        '小姑娘的声音',
        (
            '#0070131490V#1P爷爷、爷爷啊。\n',
            '您跑到哪里去了呢！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0F25')
    def lambda_0F25():
        CameraMove(-20, 0, -71810, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0F25)

    TerminateThread(0x000A, 0xFF)
    ChrSetDirection(0x000A, 180, 400)
    Sleep(100)

    @scena.Lambda('lambda_0F4D')
    def lambda_0F4D():
        ChrTurnDirection(0x00FE, 0x000E, 400)
        Yield()

        Jump('lambda_0F4D')

    DispatchAsync2(0x0101, 0x0001, lambda_0F4D)

    Sleep(50)

    @scena.Lambda('lambda_0F63')
    def lambda_0F63():
        ChrTurnDirection(0x00FE, 0x000E, 400)
        Yield()

        Jump('lambda_0F63')

    DispatchAsync2(0x0105, 0x0001, lambda_0F63)

    @scena.Lambda('lambda_0F74')
    def lambda_0F74():
        ChrTurnDirection(0x00FE, 0x000E, 400)
        Yield()

        Jump('lambda_0F74')

    DispatchAsync2(0x0103, 0x0001, lambda_0F74)

    Sleep(50)

    @scena.Lambda('lambda_0F8A')
    def lambda_0F8A():
        ChrTurnDirection(0x00FE, 0x000E, 400)
        Yield()

        Jump('lambda_0F8A')

    DispatchAsync2(0x0008, 0x0001, lambda_0F8A)

    @scena.Lambda('lambda_0F9B')
    def lambda_0F9B():
        ChrTurnDirection(0x00FE, 0x000E, 400)
        Yield()

        Jump('lambda_0F9B')

    DispatchAsync2(0x0009, 0x0001, lambda_0F9B)

    Sleep(50)

    @scena.Lambda('lambda_0FB1')
    def lambda_0FB1():
        ChrTurnDirection(0x00FE, 0x000E, 400)
        Yield()

        Jump('lambda_0FB1')

    DispatchAsync2(0x000B, 0x0001, lambda_0FB1)

    @scena.Lambda('lambda_0FC2')
    def lambda_0FC2():
        ChrTurnDirection(0x00FE, 0x000E, 400)
        Yield()

        Jump('lambda_0FC2')

    DispatchAsync2(0x000C, 0x0001, lambda_0FC2)

    @scena.Lambda('lambda_0FD3')
    def lambda_0FD3():
        ChrTurnDirection(0x00FE, 0x000E, 400)
        Yield()

        Jump('lambda_0FD3')

    DispatchAsync2(0x000F, 0x0001, lambda_0FD3)

    WaitForThreadExit(0x0101, 0x0002)
    ChrSetPos(0x000D, 360, 0, -77890, 0)

    NpcTalk(
        0x000D,
        '青年的声音',
        (
            '#0050131491V#1P喂，我说你这个小不点，\n',
            '别老在我面前窜来窜去好不好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000D,
        '青年的声音',
        (
            '#0050131492V#1P真是的，和老爷子是同种性格，\n',
            '都属于静不下来的类型。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000E,
        '小姑娘的声音',
        (
            '#0070131493V#1P可、可是阿加特大哥哥……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_10DA')
    def lambda_10DA():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_10DA)

    @scena.Lambda('lambda_10EC')
    def lambda_10EC():
        ChrWalkTo(0x00FE, -1120, 0, -74730, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_10EC)

    Sleep(600)

    @scena.Lambda('lambda_110C')
    def lambda_110C():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_110C)

    @scena.Lambda('lambda_111E')
    def lambda_111E():
        ChrWalkTo(0x00FE, 230, 0, -74960, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_111E)

    ChrSetStatus(0x0005, 0x00, 34)
    OP_B5(0x0005, 0x00)
    OP_B5(0x0005, 0x01)
    OP_B5(0x0005, 0x02)
    OP_B5(0x0005, 0x03)
    OP_B5(0x0005, 0x05)
    OP_B5(0x0005, 0x04)
    EquipCmd(0x05, 0x009A)
    EquipCmd(0x05, 0x00F6)
    EquipCmd(0x05, 0x0114)
    EquipCmd(0x05, 0x0260, 0x00)
    EquipCmd(0x05, 0x0259, 0x01)
    EquipCmd(0x05, 0x0262, 0x02)
    EquipCmd(0x05, 0x026E, 0x03)
    EquipCmd(0x05, 0x0283, 0x05)
    AddCraft(0x0005, 0x00C8)
    AddCraft(0x0005, 0x00C9)
    AddCraft(0x0005, 0x00CA)
    AddCraft(0x0005, 0x00CB)
    AddSCraft(0x0005, 0x00FF)
    AddSCraft(0x0005, 0x0100)
    ChrSetStatus(0x0006, 0x00, 32)
    OP_B5(0x0006, 0x00)
    OP_B5(0x0006, 0x01)
    OP_B5(0x0006, 0x05)
    OP_B5(0x0006, 0x04)
    OP_B5(0x0006, 0x03)
    OP_B5(0x0006, 0x02)
    EquipCmd(0x06, 0x00B8)
    EquipCmd(0x06, 0x00F6)
    EquipCmd(0x06, 0x0114)
    EquipCmd(0x06, 0x02C9, 0x00)
    EquipCmd(0x06, 0x0281, 0x01)
    EquipCmd(0x06, 0x025F, 0x05)
    EquipCmd(0x06, 0x026C, 0x04)
    EquipCmd(0x06, 0x0271, 0x03)
    EquipCmd(0x06, 0x0259, 0x02)
    AddCraft(0x0006, 0x00D2)
    AddCraft(0x0006, 0x00D3)
    AddSCraft(0x0006, 0x0104)
    WaitForThreadExit(0x000E, 0x0002)

    ChrTalk(
        0x000E,
        (
            '#0070131494V#064F啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)

    ChrTalk(
        0x0101,
        (
            '#0010131495V#004F提妲！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0020131496V#010F果然……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0070131497V#067F艾丝蒂尔姐姐！\n',
            '还有约修亚哥哥！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x000E, 10)

    @scena.Lambda('lambda_1287')
    def lambda_1287():
        ChrWalkTo(0x00FE, -2150, 0, -70350, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_1287)

    @scena.Lambda('lambda_12A2')
    def lambda_12A2():
        ChrSetDirection(0x00FE, 0, 0)
        Yield()

        Jump('lambda_12A2')

    DispatchAsync2(0x000E, 0x0001, lambda_12A2)

    @scena.Lambda('lambda_12B3')
    def lambda_12B3():
        ChrWalkTo(0x00FE, -1920, 0, -71250, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_12B3)

    @scena.Lambda('lambda_12CE')
    def lambda_12CE():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_12CE')

    DispatchAsync2(0x000D, 0x0001, lambda_12CE)

    @scena.Lambda('lambda_12DF')
    def lambda_12DF():
        CameraMove(-460, 0, -68660, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_12DF)

    @scena.Lambda('lambda_12F7')
    def lambda_12F7():
        ChrWalkTo(0x00FE, -2310, 0, -69900, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_12F7)

    @scena.Lambda('lambda_1312')
    def lambda_1312():
        ChrSetDirection(0x00FE, 180, 0)
        Yield()

        Jump('lambda_1312')

    DispatchAsync2(0x0101, 0x0001, lambda_1312)

    WaitForThreadExit(0x000E, 0x0002)
    ChrSetChipByIndex(0x000E, 9)
    ChrSetSubChip(0x000E, 0)
    ChrSetFlags(0x000E, 0x0020)

    @scena.Lambda('lambda_1337')
    def lambda_1337():
        OP_94(0x01, 0x00FE, 0x0000, 0x000001F4, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_1337)

    OP_94(0x01, 0x0101, 0x00B4, 0x000001F4, 0x000007D0, 0x00)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0105, 0xFF)
    TerminateThread(0x0103, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000C, 0xFF)

    ChrTalk(
        0x0101,
        (
            '#0010131498V#506F#5P哇哇，提妲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0070131499V#562F#6P实、实在太好啦。\n',
            '又见到你们了～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070131500V又见到姐姐你们了～\n',
            '我们从游击士协会听说了\n',
            '姐姐你们在城里战斗的事情……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070131501V#069F呜呜，你们平安真是太好了～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010131502V#008F#5P提妲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0020131503V#019F#5P谢谢你……\n',
            '让你为我们担心了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020131504V#010F阿加特兄……也平安无事呢。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020131505V您为什么也到王都来呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1509')
    def lambda_1509():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_1509)

    @scena.Lambda('lambda_1517')
    def lambda_1517():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_1517)

    @scena.Lambda('lambda_1525')
    def lambda_1525():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1525)

    @scena.Lambda('lambda_1533')
    def lambda_1533():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1533)

    @scena.Lambda('lambda_1541')
    def lambda_1541():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1541)

    @scena.Lambda('lambda_154F')
    def lambda_154F():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_154F)

    @scena.Lambda('lambda_155D')
    def lambda_155D():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_155D)

    ChrTalk(
        0x000D,
        (
            '#0050131506V#051F其实是在逃亡的途中，\n',
            '偶然找到了一艘开往王都的货船。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050131507V我们暗中乘着货船潜入这里，\n',
            '不过，来到之后却发现到处都是一团糟。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050131508V在向艾南打听了事情的经过之后，\n',
            '就特地赶来王城看一看情况。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050131509V对了，他叫我带了些东西给你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x004B, 0x00, 0x20)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_169B',
    )

    Sleep(100)

    OP_AF(0x63, 0x004B)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    OP_28(0x004C, 0x04, 0x10)
    OP_28(0x004C, 0x04, 0x20)

    def _loc_169B(): pass

    label('loc_169B')

    OP_28(0x004D, 0x04, 0x10)
    OP_28(0x004D, 0x01, 0x0100)
    Sleep(100)

    OP_AF(0x63, 0x004D)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    OP_28(0x004E, 0x04, 0x10)
    OP_28(0x004E, 0x04, 0x20)

    ChrTalk(
        0x0101,
        (
            '#0010131510V#004F#5P这样可以吗……\n',
            '还没有去协会做详细的报告呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0050131511V#053F我已经从亲卫队的队员那里\n',
            '了解到大概的情况了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050131512V#050F可是……\n',
            '这么多人聚在这里做什么呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050131513V是在商量怎么把\n',
            '残余的特务兵彻底打垮吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2300, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    TerminateThread(0x000D, 0xFF)
    ChrTurnDirection(0x000D, 0x0105, 400)

    ChrTalk(
        0x000D,
        (
            '#0050131514V#052F嗯，你是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x000D, 400)

    @scena.Lambda('lambda_180D')
    def lambda_180D():
        ChrTurnDirection(0x00FE, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_180D)

    @scena.Lambda('lambda_181B')
    def lambda_181B():
        ChrTurnDirection(0x00FE, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_181B)

    @scena.Lambda('lambda_1829')
    def lambda_1829():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_1829)

    ChrSetChipByIndex(0x000E, 6)
    ChrSetSubChip(0x000E, 0)
    ChrClearFlags(0x000E, 0x0020)
    OP_94(0x01, 0x000E, 0x00B4, 0x000000C8, 0x000003E8, 0x00)

    @scena.Lambda('lambda_1855')
    def lambda_1855():
        ChrTurnDirection(0x00FE, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1855)

    ChrTalk(
        0x0105,
        (
            '#0060131515V#041F#5P好久不见了，阿加特先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060131516V灯塔的事情多谢您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0050131517V#052F我记得你是叫科洛丝对吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050131518V可是，为什么你一个学生\n',
            '会跑到这种地方来啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630131519V#090F#5P看来我孙女承蒙过你的关照啊。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630131520V我也在此向你表示谢意。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x0008, 400)

    ChrTalk(
        0x000D,
        (
            '#0050131521V#051F哈哈，不用放在心上。\n',
            '对我来说只是单纯的任务罢了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050131522V对了，老太太。\n',
            '你是这个王城的什么人啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#0100131523V#177F#2P无、无礼之徒！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100131524V#177F你可知道这位夫人是谁！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100131525V她是利贝尔王国的一国之主\n',
            '艾莉茜雅女王陛下！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    @scena.Lambda('lambda_1ABC')
    def lambda_1ABC():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1ABC)

    ChrTalk(
        0x000D,
        (
            '#0050131526V#055F哎呀……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050131527V我就说好像感觉在哪见过……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0540131528V#104F#2P哎呀呀，你这个小子，\n',
            '很多方面还是不成熟啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x000F, 400)

    ChrTalk(
        0x000D,
        (
            '#0050131529V#054F#6P你说什么！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1B84')
    def lambda_1B84():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1B84)

    OP_62(0x000E, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    ChrTurnDirection(0x000E, 0x0105, 400)

    ChrTalk(
        0x000E,
        (
            '#0070131530V#065F#6P女、女王陛下！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070131531V这、这么说……\n',
            '那位姐姐不就是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x000E, 400)

    ChrTalk(
        0x000A,
        (
            '#0020131532V#010F#6P女王陛下的孙女科洛蒂娅公主。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020131533V我们都叫她科洛丝哦。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010131534V#001F#6P科洛丝。\n',
            '这个小姑娘是博士的孙女提妲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010131535V就像我们的妹妹一样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060131536V#048F#2P是这样啊……\n',
            '初次见面，提妲小妹妹。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060131537V#041F叫我科洛丝就可以了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0070131538V#067F#6P好、好的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070131539V科、科洛丝姐姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0103, -440, 0, -68460, 2000, 0x00)
    ChrTurnDirection(0x0103, 0x000E, 400)

    ChrTalk(
        0x0103,
        (
            '#0030131540V#023F哎哟哟。\n',
            '这个孩子好～可爱呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030131541V#021F我叫雪拉扎德，\n',
            '是艾丝蒂尔和约修亚的前辈哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030131542V叫我雪拉就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000E, 0x0103, 400)

    ChrTalk(
        0x000E,
        (
            '#0070131543V#066F#6P好、好的，雪拉姐姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0040131544V#031F嘻嘻……那么我就是\n',
            '『奥利维尔小哥哥』了哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010131545V#509F#6P别、别管那家伙，不要理他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000F, 0x000A, 400)

    ChrTalk(
        0x000F,
        (
            '#0540131546V#102F其他的姑且不论……\n',
            '你们应该不只是因为这个\n',
            '导力梯不能启动而烦恼吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540131547V到底是发生了什么事情？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1F57')
    def lambda_1F57():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1F57)

    @scena.Lambda('lambda_1F65')
    def lambda_1F65():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1F65)

    @scena.Lambda('lambda_1F73')
    def lambda_1F73():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1F73)

    ChrSetDirection(0x000A, 180, 400)

    ChrTalk(
        0x000A,
        (
            '#0020131548V#013F#5P事实上……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '约修亚向拉赛尔博士等人说明了\n',
            '上校的企图和与『辉之环』有关的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x000D,
        (
            '#0050131549V#057F喂喂，没有搞错吧……\n',
            '可别开这样的玩笑啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0070131550V#065F#6P那样的东西竟然埋在这地下……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0540131551V#104F呼……\n',
            '果然和我所担心的一样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540131552V#102F如果能够使用这个导力梯的话，\n',
            '就可以降落到那里去了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0020131553V#012F#5P嗯……\n',
            '可是它被特殊的钥匙给锁住了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020131554V似乎是使用了结晶回路……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000F, 0, 400)

    ChrTalk(
        0x000F,
        (
            '#0540131555V#103F呵呵，是这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540131556V让我来看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    CameraMove(-470, 100, -63150, 0)
    OP_67(0, 6860, -10000, 0)
    CameraSetDistance(1470, 0)
    OP_6C(32000, 0)
    OP_6E(536, 0)
    ChrSetPos(0x000F, -230, 100, -61280, 0)
    ChrSetPos(0x000E, 630, 100, -61490, 327)
    ChrSetPos(0x0101, -20, 100, -62860, 0)
    ChrSetPos(0x000A, -1040, 100, -62820, 33)
    ChrSetPos(0x0008, -80, 0, -65250, 0)
    ChrSetPos(0x0009, 760, 0, -66280, 346)
    ChrSetPos(0x000D, 1100, 100, -63990, 334)
    ChrSetPos(0x0105, -840, 0, -67210, 339)
    ChrSetPos(0x000C, -2050, 0, -66600, 39)
    ChrSetPos(0x0103, -3290, 0, -67250, 44)
    ChrSetPos(0x000B, -1860, 0, -67840, 10)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000F,
        (
            '#0540131557V#100F#6P这东西是用到了我开发的磁卡钥匙。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540131558V将拥有相同的结晶回路的磁卡\n',
            '插进去就可以解锁了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '拉赛尔博士取出了一个小型装置，\n',
            '然后将导力缆插入卡槽之中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x000F,
        (
            '#0540131559V#102F#6P哦，这个是早期的型号，\n',
            '所以没有采用保护技术。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540131560V这样，调整导力压，\n',
            '让特定的负荷进入回路……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(183, 0x00, 0x64)
    OP_71(0x0001, 0x0004)
    Sleep(1500)

    ChrTalk(
        0x0101,
        (
            '#0010131561V#001F#6P太棒了，不愧是博士啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0020131562V#010F#6P……名不虚传。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630131563V#091F呵呵……好厉害。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630131564V#090F那么我们就立刻前往地下去吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetRGBAMask(0x0010, 255, 255, 255, 0, 0)
    ChrSetPos(0x0010, 20, 0, -77690, 315)

    NpcTalk(
        0x0010,
        '青年的声音',
        (
            '#2690131565V不、不得了了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_253E')
    def lambda_253E():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_253E')

    DispatchAsync2(0x000A, 0x0001, lambda_253E)

    @scena.Lambda('lambda_254F')
    def lambda_254F():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_254F')

    DispatchAsync2(0x0101, 0x0001, lambda_254F)

    @scena.Lambda('lambda_2560')
    def lambda_2560():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_2560')

    DispatchAsync2(0x0105, 0x0001, lambda_2560)

    @scena.Lambda('lambda_2571')
    def lambda_2571():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_2571')

    DispatchAsync2(0x0103, 0x0001, lambda_2571)

    @scena.Lambda('lambda_2582')
    def lambda_2582():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_2582')

    DispatchAsync2(0x0008, 0x0001, lambda_2582)

    @scena.Lambda('lambda_2593')
    def lambda_2593():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_2593')

    DispatchAsync2(0x0009, 0x0001, lambda_2593)

    @scena.Lambda('lambda_25A4')
    def lambda_25A4():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_25A4')

    DispatchAsync2(0x000B, 0x0001, lambda_25A4)

    @scena.Lambda('lambda_25B5')
    def lambda_25B5():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_25B5')

    DispatchAsync2(0x000C, 0x0001, lambda_25B5)

    @scena.Lambda('lambda_25C6')
    def lambda_25C6():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_25C6')

    DispatchAsync2(0x000F, 0x0001, lambda_25C6)

    @scena.Lambda('lambda_25D7')
    def lambda_25D7():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_25D7')

    DispatchAsync2(0x000E, 0x0001, lambda_25D7)

    @scena.Lambda('lambda_25E8')
    def lambda_25E8():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_25E8')

    DispatchAsync2(0x000D, 0x0001, lambda_25E8)

    @scena.Lambda('lambda_25F9')
    def lambda_25F9():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_25F9)

    @scena.Lambda('lambda_260B')
    def lambda_260B():
        ChrWalkTo(0x00FE, 470, 0, -67960, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_260B)

    CameraMove(-170, 0, -65530, 1500)

    ChrTalk(
        0x0009,
        (
            '#0100131566V#173F怎么，怎么了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2690131567V一个师的正规军\n',
            '到达了王都的正门！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2690131568V是由一个看起来是\n',
            '情报部的军官模样的人率领的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0100131569V#178F什么，竟然这么快就到了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2690131570V更严重的是还有三艘\n',
            '军用警备飞艇正从湖面上接近！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2690131571V究、究竟应该怎么办！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0100131572V#177F唉，在这紧要关头！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630131573V#094F……还是由我出面去劝说他们吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0105, 0xFF)
    TerminateThread(0x0103, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000E, 0xFF)
    TerminateThread(0x000F, 0xFF)
    TerminateThread(0x000D, 0xFF)
    TerminateThread(0x000C, 0xFF)

    @scena.Lambda('lambda_27F3')
    def lambda_27F3():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_27F3)

    @scena.Lambda('lambda_2801')
    def lambda_2801():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2801)

    @scena.Lambda('lambda_280F')
    def lambda_280F():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_280F)

    @scena.Lambda('lambda_281D')
    def lambda_281D():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_281D)

    @scena.Lambda('lambda_282B')
    def lambda_282B():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_282B)

    @scena.Lambda('lambda_2839')
    def lambda_2839():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_2839)

    @scena.Lambda('lambda_2847')
    def lambda_2847():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_2847)

    @scena.Lambda('lambda_2855')
    def lambda_2855():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_2855)

    ChrTalk(
        0x0105,
        (
            '#0060131574V#043F祖、祖母大人……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630131575V#092F我要到屋顶的露台上去，\n',
            '让前来的部队听到我的解释。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630131576V尤莉亚中尉，帮我准备一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0100131577V#173F可、可是……\n',
            '万一他们展开攻击可就糟了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630131578V#094F我相信他们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630131579V虽然他们对事情有一些误解，\n',
            '但他们还是利贝尔的子民……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630131580V#090F如果看到了我，听到我的声音，\n',
            '还有什么理由会展开攻击呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0100131581V#175F……陛下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2A0F')
    def lambda_2A0F():
        CameraMove(-470, 100, -63150, 1200)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2A0F)

    ChrTurnDirection(0x0008, 0x0101, 400)
    WaitForThreadExit(0x0008, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#0630131582V#093F艾丝蒂尔，还有大家……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630131583V把这件事情委托给你们，\n',
            '我真是非常地过意不去……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010131584V#006F#5P女王陛下……\n',
            '请您不要这么说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010131585V我们一定不会让理查德上校得逞的。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0020131586V#010F#5P请放心地交给我们去办吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    CameraMove(140, 100, -61920, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2980, 0)
    OP_6C(45000, 0)
    OP_6E(259, 0)
    OP_A1(0x0011, 0x0000)
    ChrSetPos(0x0011, 0, 0, -62000, 0)
    ChrSetFlags(0x0011, 0x0004)
    ChrSetFlags(0x0011, 0x0040)
    ChrSetBattleFlags(0x0101, 0x0020)
    ChrSetBattleFlags(0x000A, 0x0020)
    ChrSetBattleFlags(0x0105, 0x0020)
    ChrSetBattleFlags(0x0103, 0x0020)
    ChrSetBattleFlags(0x000B, 0x0020)
    ChrSetBattleFlags(0x000E, 0x0020)
    ChrSetBattleFlags(0x000D, 0x0020)
    ChrSetBattleFlags(0x000C, 0x0020)
    ChrSetBattleFlags(0x000F, 0x0020)
    OP_89(0x0101, -1370, 10000, -61730, 180)
    OP_89(0x000A, -1470, 10000, -60920, 180)
    OP_89(0x0105, -390, 10000, -62450, 180)
    OP_89(0x0103, -1660, 10000, -63180, 180)
    OP_89(0x000B, -850, 10000, -64019, 180)
    OP_89(0x000E, 950, 10000, -61560, 180)
    OP_89(0x000C, 1300, 10000, -63220, 180)
    OP_89(0x000D, 420, 10000, -64010, 180)
    OP_89(0x000F, -70, 10000, -61150, 0)
    OP_0D()
    Sleep(500)

    PlaySE(247, 0x00, 0x64)
    PlaySE(104, 0x01, 0x64)

    @scena.Lambda('lambda_2C74')
    def lambda_2C74():
        ChrMoveTo(0x00FE, 0, -40000, -60000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_2C74)

    Sleep(300)

    @scena.Lambda('lambda_2C94')
    def lambda_2C94():
        ChrMoveTo(0x00FE, 0, -40000, -60000, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_2C94)

    Sleep(500)

    @scena.Lambda('lambda_2CB4')
    def lambda_2CB4():
        ChrMoveTo(0x00FE, 0, -40000, -60000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_2CB4)

    Sleep(800)

    @scena.Lambda('lambda_2CD4')
    def lambda_2CD4():
        ChrMoveTo(0x00FE, 0, -40000, -60000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_2CD4)

    Sleep(1000)

    @scena.Lambda('lambda_2CF4')
    def lambda_2CF4():
        ChrMoveTo(0x00FE, 0, -40000, -60000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_2CF4)

    FadeOut(2000, 0, -1)
    OP_0D()
    TerminateThread(0x0011, 0xFF)
    OP_A1(0x0011, 0x0002)
    ChrSetPos(0x0011, 0, 170000, 0, 0)
    ChrSetFlags(0x0011, 0x0004)
    OP_11(0x00, 0x00, 0x00, 30000, 40000, 0)
    MapSetFlags(0x00000010)
    Yield()
    OP_69(0x0011, 0)
    OP_6A(0x0011)
    OP_67(0, 4000, -10000, 0)
    CameraSetDistance(2070, 0)
    OP_6C(65000, 0)
    OP_6E(554, 0)
    OP_67(0, 3080, -10000, 0)
    CameraSetDistance(2180, 0)
    OP_6C(35000, 0)
    OP_6E(450, 0)

    @scena.Lambda('lambda_2DB1')
    def lambda_2DB1():
        OP_67(0, 11400, -10000, 20000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2DB1)

    @scena.Lambda('lambda_2DC9')
    def lambda_2DC9():
        CameraSetDistance(1310, 20000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2DC9)

    @scena.Lambda('lambda_2DD9')
    def lambda_2DD9():
        OP_6C(55000, 20000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2DD9)

    @scena.Lambda('lambda_2DE9')
    def lambda_2DE9():
        OP_6E(776, 20000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2DE9)

    ChrSetPos(0x0101, 0, 0, 0, 0)
    ChrClearFlags(0x000A, 0x0004)
    OP_89(0x0101, -1370, 190100, 270, 270)
    OP_89(0x000A, -1470, 190100, 1080, 270)
    OP_89(0x0105, -390, 190100, -450, 270)
    OP_89(0x0103, -1660, 190100, -1180, 270)
    OP_89(0x000B, -850, 190100, -2020, 270)
    OP_89(0x000E, 950, 190100, 440, 270)
    OP_89(0x000C, 1300, 190100, -1220, 270)
    OP_89(0x000D, 420, 190100, -2009, 270)
    OP_89(0x000F, -70, 190100, 750, 270)
    FadeIn(2000, 0)
    ChrMoveTo(0x0011, 0, 60000, 0, 8000, 0x00)
    FadeOut(2000, 0, -1)

    @scena.Lambda('lambda_2ECF')
    def lambda_2ECF():
        ChrMoveTo(0x00FE, 0, 0, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0000, lambda_2ECF)

    OP_24(0x0068, 0x5A)
    Sleep(400)

    OP_24(0x0068, 0x55)
    Sleep(400)

    OP_24(0x0068, 0x50)
    Sleep(400)

    OP_24(0x0068, 0x4B)
    Sleep(400)

    OP_24(0x0068, 0x46)
    Sleep(400)

    OP_24(0x0068, 0x41)
    Sleep(400)

    OP_24(0x0068, 0x3C)
    Sleep(400)

    OP_23(0x0068)
    OP_0D()
    MapClearFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/C4300._SN', 100, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

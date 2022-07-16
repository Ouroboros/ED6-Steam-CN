import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4281_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4281   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '艾莉茜雅女王'),
    TXT(0x02, '尤莉亚中尉'),
    TXT(0x03, '约修亚'),
    TXT(0x04, '奥利维尔'),
    TXT(0x05, '金'),
    TXT(0x06, '阿加特'),
    TXT(0x07, '提妲'),
    TXT(0x08, '拉赛尔博士'),
    TXT(0x09, '亲卫队员'),
    TXT(0x0A, '导力梯'),
    TXT(0x0B, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4281.x'
    header.mapIndex       = 1
    header.bgm            = 35
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x2200
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
            word_3A         = 0,
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
        ('ED6_DT07/CH02010._CH', 'ED6_DT07/CH02010P._CP'),
        ('ED6_DT07/CH02090._CH', 'ED6_DT07/CH02090P._CP'),
        ('ED6_DT07/CH00010._CH', 'ED6_DT07/CH00010P._CP'),
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP'),
        ('ED6_DT07/CH00050._CH', 'ED6_DT07/CH00050P._CP'),
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT07/CH02020._CH', 'ED6_DT07/CH02020P._CP'),
        ('ED6_DT07/CH01320._CH', 'ED6_DT07/CH01320P._CP'),
    ]

# id: 0x10002 offset: 0xF2
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
            dword_10            = 2,
            chipIndex           = 2,
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

# id: 0x10003 offset: 0x232
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x232
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x232
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x232
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_240',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x0002)

    def _loc_240(): pass

    label('loc_240')

    Return()

# id: 0x0001 offset: 0x241
@scena.Code('Init')
def Init():
    OP_A1(0x0011, 0x0002)
    SetChrPos(0x0011, 0, 0, 0, 0)
    SetChrFlags(0x0011, 0x0004)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 4, 0x644)),
            Expr.Return,
        ),
        'loc_26C',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_26C(): pass

    label('loc_26C')

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0002 offset: 0x276
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x00)
    CameraMove(-40, 100, -60120, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -1190, 0, -72040, 0)
    SetChrPos(0x0105, -1330, 0, -73970, 0)
    SetChrPos(0x0103, -30, 0, -72830, 0)
    SetChrFlags(0x0008, 0x0040)
    SetChrFlags(0x0009, 0x0040)
    SetChrFlags(0x000A, 0x0040)
    SetChrFlags(0x000B, 0x0040)
    SetChrFlags(0x000C, 0x0040)
    SetChrFlags(0x0101, 0x0040)
    SetChrFlags(0x0105, 0x0040)
    SetChrFlags(0x0103, 0x0040)
    SetChrPos(0x0008, 80, 0, -70380, 0)
    SetChrPos(0x0009, 890, 0, -71230, 0)
    SetChrPos(0x000A, -2230, 0, -70590, 0)
    SetChrPos(0x000B, 640, 0, -72930, 0)
    SetChrPos(0x000C, 2070, 0, -73010, 0)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)

    @scena.Lambda('lambda_0384')
    def lambda_0384():
        ChrWalkTo(0x00FE, -1500, 0, -68350, 1100, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0384)

    @scena.Lambda('lambda_039F')
    def lambda_039F():
        ChrWalkTo(0x00FE, -1070, 0, -69740, 1300, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_039F)

    @scena.Lambda('lambda_03BA')
    def lambda_03BA():
        ChrWalkTo(0x00FE, 420, 0, -68720, 1300, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_03BA)

    @scena.Lambda('lambda_03D5')
    def lambda_03D5():
        ChrWalkTo(0x00FE, 80, 0, -67380, 1400, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_03D5)

    @scena.Lambda('lambda_03F0')
    def lambda_03F0():
        ChrWalkTo(0x00FE, 1160, 0, -67680, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_03F0)

    @scena.Lambda('lambda_040B')
    def lambda_040B():
        ChrWalkTo(0x00FE, -2230, 0, -67590, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_040B)

    @scena.Lambda('lambda_0426')
    def lambda_0426():
        ChrWalkTo(0x00FE, 640, 0, -69890, 1100, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0426)

    @scena.Lambda('lambda_0441')
    def lambda_0441():
        ChrWalkTo(0x00FE, 2070, 0, -69160, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0441)

    @scena.Lambda('lambda_045C')
    def lambda_045C():
        CameraMove(-80, 0, -64650, 5000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_045C)

    FadeIn(1000, 0)
    WaitForThreadExit(0x0000, 0x0002)

    ChrTalk(
        0x0009,
        (
            '#170F在这种地方\n',
            '居然还有导力梯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '这以前是绝对没有过的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#070F这东西是上校\n',
            '特意建造的吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080131462V如此说来，这个导力梯\n',
            '应该就可以下降到\n',
            '封印『辉之环』的地方了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#090F是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '或许，这正是他们\n',
            '发动这次政变的背后\n',
            '所隐藏的真实目的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0631160024V只要不占领王城，\n',
            '就不能建造出这样的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F竟然、竟然会是这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0041050027V#030F呵呵，可能就是如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0041050028V想要打开由王权守护的圣域\n',
            '就必须采取一些强硬的手段……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#010F不管怎么样，想要下降到地下\n',
            '就必须要使用这个东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020131471V先把它启动了再说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x000A, -920, 0, -66390, 3000, 0x00)
    ChrWalkTo(0x000A, -550, 60, -65970, 3000, 0x00)
    ChrWalkTo(0x000A, 10, 100, -61260, 3000, 0x00)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '约修亚开始调查\n',
            '导力梯的控电盘。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '表情渐渐地焦急起来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
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
            '#0010131473V#000F怎么了，约修亚？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0101, 400)

    ChrTalk(
        0x000A,
        (
            '#010F这是……\n',
            '用导力的方式锁住了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '没有特殊结晶回路组成的钥匙\n',
            '是不能将其启动的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_07B6')
    def lambda_07B6():
        ChrWalkTo(0x00FE, -160, 0, -65050, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_07B6)

    ChrTalk(
        0x0101,
        (
            '#000F什、什么～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F怎么会这样，都到了这里了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0008, 400)

    ChrTalk(
        0x0009,
        (
            '#170F把拘捕到的特务兵\n',
            '绑过来问话！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100131479V钥匙一定存在于某个地方的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '嗯……\n',
            '看来只有这个办法了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x000D, 0x0040)
    SetChrFlags(0x000E, 0x0040)
    SetChrFlags(0x000F, 0x0040)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ChrSetRGBAMask(0x000D, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x000E, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x000F, 255, 255, 255, 0, 0)
    SetChrPos(0x000D, 20, 0, -77690, 0)
    SetChrPos(0x000E, 20, 0, -77690, 0)
    SetChrPos(0x000F, -1020, 0, -74230, 0)

    @scena.Lambda('lambda_08F6')
    def lambda_08F6():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_08F6)

    ChrTalk(
        0x000F,
        (
            '不，还没有到那种地步。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0924')
    def lambda_0924():
        CameraMove(-550, 0, -69950, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_0924)

    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_096A')
    def lambda_096A():
        ChrTurnDirection(0x00FE, 0x000F, 400)
        Yield()

        Jump('lambda_096A')

    DispatchAsync2(0x0101, 0x0001, lambda_096A)

    Sleep(50)

    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_09AE')
    def lambda_09AE():
        ChrTurnDirection(0x00FE, 0x000F, 400)
        Yield()

        Jump('lambda_09AE')

    DispatchAsync2(0x0105, 0x0001, lambda_09AE)

    @scena.Lambda('lambda_09BF')
    def lambda_09BF():
        ChrTurnDirection(0x00FE, 0x000F, 400)
        Yield()

        Jump('lambda_09BF')

    DispatchAsync2(0x0103, 0x0001, lambda_09BF)

    Sleep(50)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_0A03')
    def lambda_0A03():
        ChrTurnDirection(0x00FE, 0x000F, 400)
        Yield()

        Jump('lambda_0A03')

    DispatchAsync2(0x0008, 0x0001, lambda_0A03)

    @scena.Lambda('lambda_0A14')
    def lambda_0A14():
        ChrTurnDirection(0x00FE, 0x000F, 400)
        Yield()

        Jump('lambda_0A14')

    DispatchAsync2(0x0009, 0x0001, lambda_0A14)

    Sleep(50)

    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_0A58')
    def lambda_0A58():
        ChrTurnDirection(0x00FE, 0x000F, 400)
        Yield()

        Jump('lambda_0A58')

    DispatchAsync2(0x000B, 0x0001, lambda_0A58)

    @scena.Lambda('lambda_0A69')
    def lambda_0A69():
        ChrTurnDirection(0x00FE, 0x000F, 400)
        Yield()

        Jump('lambda_0A69')

    DispatchAsync2(0x000C, 0x0001, lambda_0A69)

    WaitForThreadExit(0x0000, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#000F哎……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#010F难道是……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#090F哦……是拉赛尔博士！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0ACA')
    def lambda_0ACA():
        CameraMove(-400, 0, -68560, 2500)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_0ACA)

    @scena.Lambda('lambda_0AE2')
    def lambda_0AE2():
        ChrWalkTo(0x00FE, -690, 0, -71190, 1600, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_0AE2)

    Sleep(200)

    SetChrFlags(0x000A, 0x0004)

    @scena.Lambda('lambda_0B07')
    def lambda_0B07():
        ChrWalkTo(0x00FE, -2940, 0, -68350, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0B07)

    @scena.Lambda('lambda_0B22')
    def lambda_0B22():
        ChrTurnDirection(0x00FE, 0x000F, 0)
        Yield()

        Jump('lambda_0B22')

    DispatchAsync2(0x000A, 0x0001, lambda_0B22)

    WaitForThreadExit(0x0000, 0x0002)

    ChrTalk(
        0x000F,
        (
            '#100F艾莉茜雅。\n',
            '久疏问候了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#100F艾丝蒂尔、约修亚，\n',
            '看来也很精神啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F等、等一下……\n',
            '为什么博士会在这里！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010131488V不是在蔡斯被情报部\n',
            '追击而逃离了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0BE2')
    def lambda_0BE2():
        ChrTurnDirection(0x00FE, 0x000E, 400)
        Yield()

        Jump('lambda_0BE2')

    DispatchAsync2(0x000A, 0x0001, lambda_0BE2)

    ChrTalk(
        0x000A,
        (
            '#010F而且，既然博士\n',
            '都到这里来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0C1D')
    def lambda_0C1D():
        CameraMove(-20, 0, -71810, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_0C1D)

    Sleep(100)

    @scena.Lambda('lambda_0C3A')
    def lambda_0C3A():
        ChrTurnDirection(0x00FE, 0x000E, 400)
        Yield()

        Jump('lambda_0C3A')

    DispatchAsync2(0x0101, 0x0001, lambda_0C3A)

    Sleep(50)

    @scena.Lambda('lambda_0C50')
    def lambda_0C50():
        ChrTurnDirection(0x00FE, 0x000E, 400)
        Yield()

        Jump('lambda_0C50')

    DispatchAsync2(0x0105, 0x0001, lambda_0C50)

    @scena.Lambda('lambda_0C61')
    def lambda_0C61():
        ChrTurnDirection(0x00FE, 0x000E, 400)
        Yield()

        Jump('lambda_0C61')

    DispatchAsync2(0x0103, 0x0001, lambda_0C61)

    Sleep(50)

    @scena.Lambda('lambda_0C77')
    def lambda_0C77():
        ChrTurnDirection(0x00FE, 0x000E, 400)
        Yield()

        Jump('lambda_0C77')

    DispatchAsync2(0x0008, 0x0001, lambda_0C77)

    @scena.Lambda('lambda_0C88')
    def lambda_0C88():
        ChrTurnDirection(0x00FE, 0x000E, 400)
        Yield()

        Jump('lambda_0C88')

    DispatchAsync2(0x0009, 0x0001, lambda_0C88)

    Sleep(50)

    @scena.Lambda('lambda_0C9E')
    def lambda_0C9E():
        ChrTurnDirection(0x00FE, 0x000E, 400)
        Yield()

        Jump('lambda_0C9E')

    DispatchAsync2(0x000B, 0x0001, lambda_0C9E)

    @scena.Lambda('lambda_0CAF')
    def lambda_0CAF():
        ChrTurnDirection(0x00FE, 0x000E, 400)
        Yield()

        Jump('lambda_0CAF')

    DispatchAsync2(0x000C, 0x0001, lambda_0CAF)

    @scena.Lambda('lambda_0CC0')
    def lambda_0CC0():
        ChrTurnDirection(0x00FE, 0x000E, 400)
        Yield()

        Jump('lambda_0CC0')

    DispatchAsync2(0x000F, 0x0001, lambda_0CC0)

    ChrTalk(
        0x000E,
        (
            '爷爷、爷爷啊。\n',
            '你跑到哪里去了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '喂，你不要在我\n',
            '面前窜来窜去好不好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '和老爷子果然是一家人，\n',
            '都属于静不下来的类型。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '可、可是阿加特大哥哥……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0D72')
    def lambda_0D72():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0D72)

    @scena.Lambda('lambda_0D84')
    def lambda_0D84():
        ChrWalkTo(0x00FE, -1120, 0, -74960, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_0D84)

    Sleep(600)

    @scena.Lambda('lambda_0DA4')
    def lambda_0DA4():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_0DA4)

    @scena.Lambda('lambda_0DB6')
    def lambda_0DB6():
        ChrWalkTo(0x00FE, 230, 0, -74730, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_0DB6)

    ChrTalk(
        0x000E,
        (
            '#060F啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)

    ChrTalk(
        0x0101,
        (
            '#000F提妲！？',
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
            '#060F艾丝蒂尔姐姐！\n',
            '还有约修亚哥哥！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0E3F')
    def lambda_0E3F():
        ChrWalkTo(0x00FE, -2410, 0, -69730, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_0E3F)

    @scena.Lambda('lambda_0E5A')
    def lambda_0E5A():
        SetChrDirection(0x00FE, 0, 0)
        Yield()

        Jump('lambda_0E5A')

    DispatchAsync2(0x000E, 0x0001, lambda_0E5A)

    @scena.Lambda('lambda_0E6B')
    def lambda_0E6B():
        ChrWalkTo(0x00FE, -1920, 0, -71390, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_0E6B)

    @scena.Lambda('lambda_0E86')
    def lambda_0E86():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_0E86')

    DispatchAsync2(0x000D, 0x0001, lambda_0E86)

    CameraMove(-460, 0, -68660, 2000)
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
            '#000F哇哇，提妲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#060F实、实在太好啦。\n',
            '又见到你们了～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070131500V从游击士协会听说了\n',
            '姐姐你们在城里\n',
            '战斗的事情……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '呜呜，你们平安真是太好了～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F提妲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0F71')
    def lambda_0F71():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0F71)

    ChrTalk(
        0x000A,
        (
            '#010F谢谢……\n',
            '让你为我们担心了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '阿加特兄……\n',
            '也平安无事呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020131505V为什么会到王都来呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0FDF')
    def lambda_0FDF():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0FDF)

    @scena.Lambda('lambda_0FED')
    def lambda_0FED():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_0FED)

    @scena.Lambda('lambda_0FFB')
    def lambda_0FFB():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_0FFB)

    @scena.Lambda('lambda_1009')
    def lambda_1009():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1009)

    @scena.Lambda('lambda_1017')
    def lambda_1017():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1017)

    @scena.Lambda('lambda_1025')
    def lambda_1025():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1025)

    @scena.Lambda('lambda_1033')
    def lambda_1033():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1033)

    @scena.Lambda('lambda_1041')
    def lambda_1041():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_1041)

    ChrTalk(
        0x000D,
        (
            '#050F其实是偶然的找到了\n',
            '一艘开往王都的货船。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050131507V乘着它暗中潜入这里，\n',
            ' ',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '就特地赶来王城这边看一看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F是、是这样吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0050131512V#050F可是这么多人聚\n',
            '在这里是在做什么呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '准是在商量怎么把\n',
            '残余的特务兵彻底打垮吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x000D, 0xFF)
    ChrTurnDirection(0x000D, 0x0105, 400)

    ChrTalk(
        0x000D,
        (
            '#050F……嗯，你是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x000D, 400)

    @scena.Lambda('lambda_1164')
    def lambda_1164():
        ChrTurnDirection(0x00FE, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1164)

    @scena.Lambda('lambda_1172')
    def lambda_1172():
        ChrTurnDirection(0x00FE, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1172)

    @scena.Lambda('lambda_1180')
    def lambda_1180():
        ChrTurnDirection(0x00FE, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1180)

    @scena.Lambda('lambda_118E')
    def lambda_118E():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_118E)

    ChrTalk(
        0x0105,
        (
            '#040F好久不见了，阿加特大哥。',
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
            '#050F我记得你是叫科洛丝对吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050131518V可是为何你一个学生\n',
            '会跑到这里来呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#090F看来我孙女承蒙过\n',
            '你的照顾啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630131520V我在这儿也向你\n',
            '表示谢意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x0008, 400)

    ChrTalk(
        0x000D,
        (
            '#050F哈哈，不用放在心上。\n',
            '对我来说只是单纯的任务罢了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050131522V对了，老太太，\n',
            '你是这个城的什么人呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0101060014V#170F无、无礼之徒！\n',
            '你可知道这位夫人是谁！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100131525V她是利贝尔的一国之主，\n',
            '艾莉茜雅女王陛下！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_134F')
    def lambda_134F():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_134F)

    ChrTalk(
        0x000D,
        (
            '#050F呼～～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我是说好像感觉\n',
            '好像在哪里见过的样子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#100F哎呀呀。\n',
            ' ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x000F, 400)

    ChrTalk(
        0x000D,
        (
            '#050F你说什么！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_13C8')
    def lambda_13C8():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_13C8)

    ChrTurnDirection(0x000E, 0x0105, 400)

    ChrTalk(
        0x000E,
        (
            '#060F女、女王陛下！？',
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
            '#010F女王陛下的孙女，\n',
            '科洛蒂娅公主。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020131533V我们都\n',
            '叫她科洛丝哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F科洛丝。\n',
            '这个小姑娘是博士的孙女提妲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010131535V她就像我们的妹妹一样哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F是这样啊……\n',
            '初次见面，提妲小妹妹。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '叫我科洛丝\n',
            '就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#060F好、好的呢……',
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
            '#020F哎哟哟。\n',
            '这个孩子好可爱呀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我叫雪拉扎德，\n',
            '是艾丝蒂尔和约修亚的前辈哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030131542V叫我雪拉就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#060F好、好的，雪拉姐姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#030F那么我就是\n',
            '『奥利维尔小哥哥』了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F别管那家伙，不要理他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000F, 0x000A, 400)

    ChrTalk(
        0x000F,
        (
            '#100F其他的姑且不论……\n',
            '不过应该不只是因为\n',
            '这个导力梯不能启动而烦恼吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540131547V到底是发生了什么事情？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_16A5')
    def lambda_16A5():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_16A5)

    @scena.Lambda('lambda_16B3')
    def lambda_16B3():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_16B3)

    ChrTalk(
        0x000A,
        (
            '#010F那是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '约修亚说明了上校的企图\n',
            '和与『辉之环』有关的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x000D,
        (
            '#050F喂喂，没有搞错吧……\n',
            '可别开这样的玩笑啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#060F那样的东西\n',
            '竟然埋在这儿地下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#100F呼……果然和我所\n',
            '担忧的一样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '如果能够使用这个导力梯的话，\n',
            '就可以下降到那里去了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#010F嗯，可是它被\n',
            '特殊的钥匙给锁住了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020131554V似乎是使用了结晶回路……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x000F, 0, 400)

    ChrTalk(
        0x000F,
        (
            '#100F呵呵，是这样。',
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
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(32000, 0)
    OP_6E(262, 0)
    SetChrPos(0x000F, -230, 100, -61280, 0)
    SetChrPos(0x000E, 630, 100, -61490, 327)
    SetChrPos(0x0101, -20, 100, -62860, 0)
    SetChrPos(0x000A, -1040, 100, -62820, 33)
    SetChrPos(0x0008, -80, 0, -65250, 9)
    SetChrPos(0x0009, 760, 0, -66280, 346)
    SetChrPos(0x000D, 1100, 100, -63990, 334)
    SetChrPos(0x0105, -840, 0, -67210, 339)
    SetChrPos(0x000C, -2050, 0, -66600, 39)
    SetChrPos(0x0103, -3290, 0, -67250, 44)
    SetChrPos(0x000B, -1860, 0, -67840, 10)
    OP_0D()

    ChrTalk(
        0x000F,
        (
            '#100F这东西是用到了我\n',
            '开发的磁卡钥匙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540131558V将拥有相同的结晶回路的\n',
            '磁卡插入进去就可以解锁了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '博士取出了一个小型装置，\n',
            '然后将伸出来的线缆\n',
            '插入导力梯的卡槽之中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x000F,
        (
            '#100F哦，这个是早期的型号，\n',
            '所以没有采用保护技术。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540131560V这样，调整导力压，\n',
            '让特定的负荷进入回路……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F太棒了，不愧是博士啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#010F……名不虚传。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#090F呵呵……好厉害。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那么我们就立刻\n',
            '降到地下去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    ChrSetRGBAMask(0x0010, 255, 255, 255, 0, 0)
    SetChrPos(0x0010, 20, 0, -77690, 315)

    ChrTalk(
        0x0010,
        (
            '#2690131565V不、不得了了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1B4F')
    def lambda_1B4F():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_1B4F')

    DispatchAsync2(0x0101, 0x0001, lambda_1B4F)

    @scena.Lambda('lambda_1B60')
    def lambda_1B60():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_1B60')

    DispatchAsync2(0x0105, 0x0001, lambda_1B60)

    @scena.Lambda('lambda_1B71')
    def lambda_1B71():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_1B71')

    DispatchAsync2(0x0103, 0x0001, lambda_1B71)

    @scena.Lambda('lambda_1B82')
    def lambda_1B82():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_1B82')

    DispatchAsync2(0x0008, 0x0001, lambda_1B82)

    @scena.Lambda('lambda_1B93')
    def lambda_1B93():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_1B93')

    DispatchAsync2(0x0009, 0x0001, lambda_1B93)

    @scena.Lambda('lambda_1BA4')
    def lambda_1BA4():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_1BA4')

    DispatchAsync2(0x000B, 0x0001, lambda_1BA4)

    @scena.Lambda('lambda_1BB5')
    def lambda_1BB5():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_1BB5')

    DispatchAsync2(0x000C, 0x0001, lambda_1BB5)

    @scena.Lambda('lambda_1BC6')
    def lambda_1BC6():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_1BC6')

    DispatchAsync2(0x000F, 0x0001, lambda_1BC6)

    @scena.Lambda('lambda_1BD7')
    def lambda_1BD7():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_1BD7')

    DispatchAsync2(0x000E, 0x0001, lambda_1BD7)

    @scena.Lambda('lambda_1BE8')
    def lambda_1BE8():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_1BE8')

    DispatchAsync2(0x000D, 0x0001, lambda_1BE8)

    @scena.Lambda('lambda_1BF9')
    def lambda_1BF9():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_1BF9)

    @scena.Lambda('lambda_1C0B')
    def lambda_1C0B():
        ChrWalkTo(0x00FE, 470, 0, -67960, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_1C0B)

    CameraMove(-170, 0, -65530, 3000)

    ChrTalk(
        0x0009,
        (
            '#170F怎么，怎么了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '一个师的正规军\n',
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
            '#0101060015V#170F什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '更严重的是还有三艘\n',
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
            '#170F唉，在这紧要关头！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#090F……还是由我出面\n',
            '去劝说他们吧。',
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

    @scena.Lambda('lambda_1D94')
    def lambda_1D94():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1D94)

    @scena.Lambda('lambda_1DA2')
    def lambda_1DA2():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_1DA2)

    @scena.Lambda('lambda_1DB0')
    def lambda_1DB0():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_1DB0)

    @scena.Lambda('lambda_1DBE')
    def lambda_1DBE():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1DBE)

    @scena.Lambda('lambda_1DCC')
    def lambda_1DCC():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1DCC)

    @scena.Lambda('lambda_1DDA')
    def lambda_1DDA():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1DDA)

    @scena.Lambda('lambda_1DE8')
    def lambda_1DE8():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_1DE8)

    ChrTalk(
        0x0105,
        (
            '#040F祖、祖母大人……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#090F我到屋顶的阳台上去\n',
            '让前来的部队听到我的声音。',
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
            '#170F可、可是……\n',
            '万一他们展开攻击可就糟了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#090F我相信他们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630131579V虽然有一些误解，\n',
            '但他们还是利贝尔的子民……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '如果看到了我，听到我的声音，\n',
            '还有什么理由会展开攻击呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#170F……陛下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#090F艾丝蒂尔，还有大家……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630131583V把这件事情委托给你们，\n',
            '我心理很是过意不去啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F女王陛下……\n',
            '请您不要这么说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010131585V理查德上校的野心，\n',
            '我们一定会阻止的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A1(0x0011, 0x0002)
    SetChrPos(0x0011, 0, 170000, 0, 0)
    SetChrFlags(0x0011, 0x0004)

    ChrTalk(
        0x000A,
        (
            '请放心的交给我们去办吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    OP_11(0x00, 0x00, 0x00, 30000, 40000, 0)
    SetMapFlags(0x00000010)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x0011, 0)
    OP_6A(0x0011)
    OP_67(0, 4000, -10000, 0)
    CameraSetDistance(2070, 0)
    OP_6C(65000, 0)
    OP_6E(554, 0)

    @scena.Lambda('lambda_208B')
    def lambda_208B():
        OP_67(0, 15000, -10000, 20000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_208B)

    @scena.Lambda('lambda_20A3')
    def lambda_20A3():
        CameraSetDistance(1280, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_20A3)

    @scena.Lambda('lambda_20B3')
    def lambda_20B3():
        OP_6C(600000, 20000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_20B3)

    @scena.Lambda('lambda_20C3')
    def lambda_20C3():
        OP_6E(900, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_20C3)

    SetChrPos(0x0101, 0, 0, 0, 0)
    ClearChrFlags(0x000A, 0x0004)
    SetChrBattleFlags(0x0101, 0x0020)
    SetChrBattleFlags(0x000A, 0x0020)
    SetChrBattleFlags(0x0105, 0x0020)
    SetChrBattleFlags(0x0103, 0x0020)
    SetChrBattleFlags(0x000B, 0x0020)
    SetChrBattleFlags(0x000E, 0x0020)
    SetChrBattleFlags(0x000D, 0x0020)
    SetChrBattleFlags(0x000C, 0x0020)
    SetChrBattleFlags(0x000F, 0x0020)
    OP_89(0x0101, -1370, 190100, 270, 258)
    OP_89(0x000A, -1470, 190100, 1080, 286)
    OP_89(0x0105, -390, 190100, -450, 9)
    OP_89(0x0103, -1660, 190100, -1180, 246)
    OP_89(0x000B, -850, 190100, -2020, 246)
    OP_89(0x000E, 950, 190100, 440, 319)
    OP_89(0x000D, 1300, 190100, -1220, 265)
    OP_89(0x000C, 420, 190100, -2009, 155)
    OP_89(0x000F, -70, 190100, 750, 9)
    FadeIn(2000, 0)
    ChrMoveTo(0x0011, 0, 40000, 0, 10000, 0x00)
    FadeOut(2000, 0, -1)
    ChrMoveTo(0x0011, 0, 0, 0, 10000, 0x00)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/C4300._SN', 100, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

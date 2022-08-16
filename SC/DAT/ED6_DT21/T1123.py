import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T1123_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1123   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1123.x'
    header.mapIndex       = 1
    header.bgm            = 11
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
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT07/CH00040._CH', 'ED6_DT07/CH00040P._CP'),
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP'),
        ('ED6_DT07/CH02360._CH', 'ED6_DT07/CH02360P._CP'),
        ('ED6_DT26/CH20360._CH', 'ED6_DT26/CH20360P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT26/CH20342._CH', 'ED6_DT26/CH20342P._CP'),
        ('ED6_DT07/CH01220._CH', 'ED6_DT07/CH01220P._CP'),
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH01680._CH', 'ED6_DT07/CH01680P._CP'),
        ('ED6_DT07/CH01690._CH', 'ED6_DT07/CH01690P._CP'),
        ('ED6_DT06/CH20118._CH', 'ED6_DT06/CH20118P._CP'),
        ('ED6_DT07/CH00021._CH', 'ED6_DT07/CH00021P._CP'),
        ('ED6_DT07/CH00031._CH', 'ED6_DT07/CH00031P._CP'),
        ('ED6_DT07/CH00041._CH', 'ED6_DT07/CH00041P._CP'),
        ('ED6_DT07/CH00061._CH', 'ED6_DT07/CH00061P._CP'),
        ('ED6_DT07/CH00071._CH', 'ED6_DT07/CH00071P._CP'),
    ]

# id: 0x10001 offset: 0x152
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '雪拉扎德',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '奥利维尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '科洛丝',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '提妲',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            direction           = 0,
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
            name                = '梅贝尔市长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '莉拉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '巴克',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '德拉多',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '市民',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '市民',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '市民',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '市民',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '市民',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '市民',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x332
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x332
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x332
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x332
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_34E',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2E),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_02_374)

    def _loc_34E(): pass

    label('loc_34E')

    Return()

# id: 0x0001 offset: 0x34F
@scena.Code('func_01_34F')
def func_01_34F():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_373',
    )

    OP_72(0x0000, 0x0010)
    OP_72(0x0001, 0x0010)
    OP_6F(0x0000, 29)
    OP_6F(0x0001, 29)

    def _loc_373(): pass

    label('loc_373')

    Return()

# id: 0x0002 offset: 0x374
@scena.Code('func_02_374')
def func_02_374():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0004)
    ChrSetPos(0x000D, -1910, -1000, -5900, 90)
    ChrSetPos(0x000E, 160, -1400, -5250, 90)
    ChrSetPos(0x000F, -720, -1000, -3310, 135)
    ChrSetPos(0x0010, -1340, -1000, -4540, 90)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetFlags(0x0010, 0x0004)
    ChrSetFlags(0x000E, 0x0004)
    ChrSetFlags(0x000E, 0x0002)
    ChrSetChipByIndex(0x000E, 6)
    ChrSetSubChip(0x000E, 10)
    ChrSetPos(0x0011, -20430, 0, 440, 270)
    ChrSetPos(0x0012, -20190, 0, 1910, 270)
    ChrSetPos(0x0013, -18990, 0, 1800, 270)
    ChrSetPos(0x0014, -17990, 0, 1380, 270)
    ChrSetPos(0x0015, -17170, 0, -470, 270)
    ChrSetPos(0x0016, -17100, 0, 200, 270)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    CreateThread(0x0011, 0x01, 0x00, func_09_163F)
    CreateThread(0x0013, 0x01, 0x00, func_0A_1674)
    CreateThread(0x0015, 0x01, 0x00, func_0B_169D)
    CameraMove(-13970, 0, 14660, 0)
    OP_67(0, 11740, -10000, 0)
    CameraSetDistance(1780, 0)
    OP_6C(56000, 0)
    OP_6E(367, 0)
    FadeIn(1500, 0)

    @scena.Lambda('lambda_04F9')
    def lambda_04F9():
        CameraMove(-17870, 0, 1730, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_04F9)

    @scena.Lambda('lambda_0511')
    def lambda_0511():
        OP_67(0, 9280, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0511)

    @scena.Lambda('lambda_0529')
    def lambda_0529():
        CameraSetDistance(1940, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0529)

    @scena.Lambda('lambda_0539')
    def lambda_0539():
        OP_6C(68000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0539)

    OP_62(0x0011, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x00)
    Sleep(100)

    OP_62(0x0012, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x00)
    Sleep(100)

    OP_62(0x0013, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x00)
    Sleep(100)

    OP_62(0x0014, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x00)
    Sleep(100)

    OP_62(0x0015, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x00)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(1000)

    Fade(500)
    CameraMove(9600, 0, 14190, 0)
    OP_67(0, 10090, -10000, 0)
    CameraSetDistance(1940, 0)
    OP_6C(30000, 0)
    OP_6E(367, 0)

    @scena.Lambda('lambda_0603')
    def lambda_0603():
        CameraMove(-400, 0, -5770, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0603)

    @scena.Lambda('lambda_061B')
    def lambda_061B():
        OP_6C(33000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_061B)

    Sleep(2500)

    OP_62(0x000F, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x00)
    Sleep(50)

    OP_62(0x0010, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x00)
    Sleep(50)

    OP_62(0x000D, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x00)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(1000)

    OP_63(0x000F)
    OP_63(0x0010)
    OP_63(0x000D)
    ChrSetPos(0x0101, -3100, 0, 12790, 180)
    ChrSetPos(0x0008, -4530, 0, 12880, 180)
    ChrSetPos(0x000A, -4370, 0, 14000, 180)
    ChrSetPos(0x000B, -5270, 0, 13810, 180)
    ChrSetPos(0x0009, -3500, 0, 14100, 180)
    ChrSetPos(0x000C, -2550, 0, 14100, 180)
    ChrClearFlags(0x0101, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    Fade(500)
    CameraMove(-3240, 0, 14240, 0)
    OP_67(0, 8200, -10000, 0)
    CameraSetDistance(1940, 0)
    OP_6C(33000, 0)
    OP_6E(367, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010300888V#1020F#5P好、好过分……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
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
        32,
        0,
        (
            TXT(0x00, '【总之先进行救助】\n'),
            TXT(0x01, '【首先决定任务分配】\n'),
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
        (0x00000000, 'loc_7E1'),
        (0x00000001, 'loc_B8F'),
        (-1, 'loc_EA2'),
    )

    def _loc_7E1(): pass

    label('loc_7E1')

    ChrTalk(
        0x0101,
        (
            '#0010300889V#1005F#5P总、总之得做点什么！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 180, 600)

    @scena.Lambda('lambda_081D')
    def lambda_081D():
        ChrWalkTo(0x00FE, -3100, 0, 11800, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_081D)

    Sleep(100)

    ChrTalk(
        0x0009,
        (
            '#0040300890V#530F#5P等一等、艾丝蒂尔！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040300891V这种时候不能急，\n',
            '要先决定任务分配！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0101, 0x0001)
    ChrTurnDirection(0x0101, 0x0009, 500)

    ChrTalk(
        0x0101,
        (
            '#0010300892V#1026F#4P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0040300893V#030F#5P看起来需要帮助的市民\n',
            '分在两个地方。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040300894V最好是分头处理吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300895V#1002F#4P嗯、嗯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 0, 500)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#0030300896V#022F#6P公主殿下、提妲。\n',
            '请跟我来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300897V去西出口引导\n',
            '还没来得及逃走的人们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_09B9')
    def lambda_09B9():
        ChrSetDirection(0x000C, 225, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_09B9)

    @scena.Lambda('lambda_09C7')
    def lambda_09C7():
        ChrSetDirection(0x0009, 225, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_09C7)

    ChrSetDirection(0x0101, 270, 400)

    ChrTalk(
        0x000A,
        (
            '#0060300898V#042F#5P是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0070300899V#062F#5P明、明白了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0A20')
    def lambda_0A20():
        CameraMove(-4420, 0, 13210, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0A20)

    CreateThread(0x0008, 0x01, 0x00, func_06_1588)
    Sleep(500)

    CreateThread(0x000B, 0x01, 0x00, func_07_15C5)
    Sleep(300)

    CreateThread(0x000A, 0x01, 0x00, func_08_1602)
    TerminateThread(0x0101, 0x02)
    TerminateThread(0x0009, 0x02)
    TerminateThread(0x000C, 0x02)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(1500)

    @scena.Lambda('lambda_0A6D')
    def lambda_0A6D():
        CameraMove(-2290, 0, 14010, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0A6D)

    Sleep(500)

    ChrSetDirection(0x000C, 180, 500)
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x000C,
        (
            '#0080300900V#076F#5P好，那我们\n',
            '就去帮忙搬开那边的瓦砾！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080300901V似乎有人\n',
            '被压在底下了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0AF8')
    def lambda_0AF8():
        ChrSetDirection(0x00FE, 0, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0AF8)

    Sleep(50)

    @scena.Lambda('lambda_0B0B')
    def lambda_0B0B():
        ChrSetDirection(0x00FE, 180, 500)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0B0B)

    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010300902V#1005F#4P嗯……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0040300903V#035F#5P呼，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 180, 600)
    CreateThread(0x0101, 0x01, 0x00, func_03_152B)
    Sleep(500)

    CreateThread(0x0009, 0x01, 0x00, func_04_1540)
    Sleep(300)

    CreateThread(0x000C, 0x01, 0x00, func_05_1564)
    Sleep(1000)

    Jump('loc_EA2')

    def _loc_B8F(): pass

    label('loc_B8F')

    OP_2B(0x0094, 0x0003)

    ChrTalk(
        0x0101,
        (
            '#0010300904V#1002F#5P……首先\n',
            '得决定任务分配！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 500)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010300905V#1005F#2P雪拉姐！\n',
            '你跟科洛丝和提妲一起\n',
            '去引导还没来得及逃走的人们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0C2F')
    def lambda_0C2F():
        ChrTurnDirection(0x00FE, 0x0101, 500)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0C2F)

    @scena.Lambda('lambda_0C3D')
    def lambda_0C3D():
        ChrTurnDirection(0x00FE, 0x0101, 500)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0C3D)

    ChrTurnDirection(0x000B, 0x0101, 500)

    ChrTalk(
        0x0008,
        (
            '#0030300906V#022F#6P嗯嗯，明白了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 0, 500)

    ChrTalk(
        0x0008,
        (
            '#0030300907V#024F#6P公主殿下，提妲。\n',
            '我们去西出口那边！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0CBE')
    def lambda_0CBE():
        ChrSetDirection(0x00FE, 180, 500)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0CBE)

    Sleep(50)

    @scena.Lambda('lambda_0CD1')
    def lambda_0CD1():
        ChrSetDirection(0x00FE, 180, 500)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0CD1)

    Sleep(300)

    ChrTalk(
        0x000A,
        (
            '#0060300898V#042F#5P是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0070300899V#062F#5P明、明白了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0D28')
    def lambda_0D28():
        ChrSetDirection(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0D28)

    Sleep(100)

    ChrSetDirection(0x0009, 225, 400)

    @scena.Lambda('lambda_0D42')
    def lambda_0D42():
        CameraMove(-4420, 0, 13210, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0D42)

    CreateThread(0x0008, 0x01, 0x00, func_06_1588)
    Sleep(500)

    CreateThread(0x000B, 0x01, 0x00, func_07_15C5)
    Sleep(300)

    CreateThread(0x000A, 0x01, 0x00, func_08_1602)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(1500)

    TerminateThread(0x0101, 0x02)
    TerminateThread(0x0009, 0x02)
    TerminateThread(0x000C, 0x02)

    @scena.Lambda('lambda_0D8F')
    def lambda_0D8F():
        CameraMove(-2290, 0, 14010, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0D8F)

    Sleep(500)

    ChrSetDirection(0x0101, 0, 500)
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0101,
        (
            '#0010300910V#1005F#6P金先生、奥利维尔！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300911V我们就先\n',
            '去帮忙搬开瓦砾吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0E0E')
    def lambda_0E0E():
        ChrSetDirection(0x00FE, 180, 500)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0E0E)

    Sleep(50)

    @scena.Lambda('lambda_0E21')
    def lambda_0E21():
        ChrSetDirection(0x00FE, 180, 500)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0E21)

    Sleep(400)

    ChrTalk(
        0x000C,
        (
            '#0080300912V#076F#5P喔喔！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0040300913V#035F#5P呼，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 180, 600)
    CreateThread(0x0101, 0x01, 0x00, func_03_152B)
    Sleep(500)

    CreateThread(0x0009, 0x01, 0x00, func_04_1540)
    Sleep(300)

    CreateThread(0x000C, 0x01, 0x00, func_05_1564)
    Sleep(1000)

    Jump('loc_EA2')

    def _loc_EA2(): pass

    label('loc_EA2')

    Fade(500)
    CameraMove(110, -1000, -4550, 0)
    OP_67(0, 7830, -10000, 0)
    CameraSetDistance(2900, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000D,
        (
            '#0360300914V#616F#6P拜托！\n',
            '请回答！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000F, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(100)

    OP_62(0x0010, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x000F,
        (
            '#1150300915V#5P唔……不行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#1160300916V#6P我们的力量……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0101, 0x01, 0x00, func_0C_16C2)

    @scena.Lambda('lambda_0F94')
    def lambda_0F94():
        CameraMove(910, -1000, -2920, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0F94)

    Sleep(300)

    CreateThread(0x0009, 0x01, 0x00, func_0D_16F7)
    Sleep(300)

    CreateThread(0x000C, 0x01, 0x00, func_0E_1740)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010300917V#1005F#5P梅贝尔市长！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0010, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000F, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_1044')
    def lambda_1044():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1044)

    @scena.Lambda('lambda_1052')
    def lambda_1052():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_1052)

    @scena.Lambda('lambda_1060')
    def lambda_1060():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_1060)

    Sleep(400)

    ChrTalk(
        0x0010,
        (
            '#1160300918V#6P你、你们是……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0360300919V#619F#6P艾、艾丝蒂尔！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300920V#1005F#5P我们来帮忙了！\n',
            '有人在底下吧！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0360300921V#618F#6P莉、莉拉她……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360300922V#616F莉拉为了保护我\n',
            '被压在这瓦砾下面……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_115A')
    def lambda_115A():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_115A)

    Sleep(50)

    @scena.Lambda('lambda_116D')
    def lambda_116D():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_116D)

    Sleep(50)

    ChrSetDirection(0x000C, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010300923V#1002F#5P！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0080300924V#072F#5P这程度\n',
            '我一个人就能举起。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080300925V你们稍微让开一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#1150300926V#3P啊，啊啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#1160300927V#3P拜、拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_123D')
    def lambda_123D():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_123D')

    DispatchAsync2(0x000F, 0x0002, lambda_123D)

    @scena.Lambda('lambda_124E')
    def lambda_124E():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_124E')

    DispatchAsync2(0x0010, 0x0002, lambda_124E)

    @scena.Lambda('lambda_125F')
    def lambda_125F():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_125F')

    DispatchAsync2(0x000D, 0x0001, lambda_125F)

    ChrSetFlags(0x000C, 0x0004)

    @scena.Lambda('lambda_1275')
    def lambda_1275():
        ChrWalkTo(0x00FE, 1550, -1000, -4100, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1275)

    @scena.Lambda('lambda_1290')
    def lambda_1290():
        CameraMove(870, -1000, -3760, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1290)

    Sleep(300)

    @scena.Lambda('lambda_12AD')
    def lambda_12AD():
        ChrMoveTo(0x00FE, -1370, -1000, -3120, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_12AD)

    Sleep(100)

    @scena.Lambda('lambda_12CD')
    def lambda_12CD():
        ChrMoveTo(0x00FE, -1920, -1000, -4230, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_12CD)

    WaitForThreadExit(0x000C, 0x0001)
    ChrSetDirection(0x000C, 225, 400)
    Sleep(500)

    Fade(500)

    @scena.Lambda('lambda_12FE')
    def lambda_12FE():
        CameraSetDistance(2700, 0)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_12FE)

    ChrSetFlags(0x000C, 0x0002)
    ChrSetChipByIndex(0x000C, 9)
    ChrSetSubChip(0x000C, 0)
    OP_0D()

    @scena.Lambda('lambda_131E')
    def lambda_131E():
        OP_99(0x00FE, 0x00, 0x02, 1000)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_131E)

    Sleep(500)

    ChrTalk(
        0x000C,
        (
            '#0080300928V#077F#5P……唔！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)

    @scena.Lambda('lambda_135A')
    def lambda_135A():
        CameraSetDistance(2900, 500)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_135A)

    OP_B0(0x0002, 0xFA)
    OP_6F(0x0002, 0)
    OP_70(0x0002, 170)
    Sleep(150)

    @scena.Lambda('lambda_1381')
    def lambda_1381():
        OP_99(0x00FE, 0x04, 0x09, 1400)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_1381)

    PlaySE(291, 0x00, 0x64)
    ChrSetSubChip(0x000E, 2)
    TerminateThread(0x000D, 0x01)

    @scena.Lambda('lambda_139F')
    def lambda_139F():
        ChrSetDirection(0x000D, 90, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_139F)

    OP_73(0x0002)
    WaitForThreadExit(0x000C, 0x0002)
    Sleep(1000)

    ChrTalk(
        0x000D,
        (
            '#0360300929V#619F#6P莉拉！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0370300930V#5P#625F#80W呜……啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370300931V#626F#80W……小……小姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0010, 0x02)
    TerminateThread(0x000F, 0x02)
    ChrSetDirection(0x000F, 135, 400)
    ChrSetDirection(0x0010, 135, 400)

    ChrTalk(
        0x000F,
        (
            '#1150300932V#6P啊，还活着呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x000D, 0x01)

    ChrTalk(
        0x000D,
        (
            '#0360300933V#616F#6P啊啊，莉拉！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 270, 500)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010300934V#1005F#2P奥利维尔……\n',
            '帮忙把莉拉小姐抱走！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0040300935V#035F#5P哈哈，交给我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)
    FadeOut(1500, 0, -1)
    OP_0D()
    OP_21()
    Sleep(1000)

    SetScenaFlags(ScenaFlag(0x0342, 3, 0x1A13))
    MapClearFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T1111._SN', 109, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x152B
@scena.Code('func_03_152B')
def func_03_152B():
    ChrWalkTo(0x00FE, -3510, -1000, 5990, 5000, 0x00)

    Return()

# id: 0x0004 offset: 0x1540
@scena.Code('func_04_1540')
def func_04_1540():
    ChrSetFlags(0x00FE, 0x1000)
    ChrSetChipByIndex(0x00FE, 17)
    ChrWalkTo(0x00FE, -3510, -1000, 5990, 5000, 0x00)
    ChrClearFlags(0x00FE, 0x1000)

    Return()

# id: 0x0005 offset: 0x1564
@scena.Code('func_05_1564')
def func_05_1564():
    ChrSetFlags(0x00FE, 0x1000)
    ChrSetChipByIndex(0x00FE, 20)
    ChrWalkTo(0x00FE, -3510, -1000, 5990, 4500, 0x00)
    ChrClearFlags(0x00FE, 0x1000)

    Return()

# id: 0x0006 offset: 0x1588
@scena.Code('func_06_1588')
def func_06_1588():
    ChrSetFlags(0x00FE, 0x1000)
    ChrSetChipByIndex(0x00FE, 16)
    ChrWalkTo(0x00FE, -8119, 0, 9780, 5000, 0x00)
    ChrWalkTo(0x00FE, -13790, 0, 8730, 5000, 0x00)
    ChrClearFlags(0x00FE, 0x1000)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0007 offset: 0x15C5
@scena.Code('func_07_15C5')
def func_07_15C5():
    ChrSetFlags(0x00FE, 0x1000)
    ChrSetChipByIndex(0x00FE, 19)
    ChrWalkTo(0x00FE, -7510, 0, 10030, 5000, 0x00)
    ChrWalkTo(0x00FE, -13260, 0, 8650, 5000, 0x00)
    ChrClearFlags(0x00FE, 0x1000)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0008 offset: 0x1602
@scena.Code('func_08_1602')
def func_08_1602():
    ChrSetFlags(0x00FE, 0x1000)
    ChrSetChipByIndex(0x00FE, 18)
    ChrWalkTo(0x00FE, -7510, 0, 10030, 5000, 0x00)
    ChrWalkTo(0x00FE, -13260, 0, 8650, 5000, 0x00)
    ChrClearFlags(0x00FE, 0x1000)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0009 offset: 0x163F
@scena.Code('func_09_163F')
def func_09_163F():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1673',
    )

    ChrMoveToRelative(0x00FE, 0, 0, -1000, 2500, 0x00)
    ChrMoveToRelative(0x00FE, 0, 0, 1000, 2500, 0x00)

    Jump('func_09_163F')

    def _loc_1673(): pass

    label('loc_1673')

    Return()

# id: 0x000A offset: 0x1674
@scena.Code('func_0A_1674')
def func_0A_1674():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_169C',
    )

    ChrSetDirection(0x00FE, 90, 200)
    ChrSetDirection(0x00FE, 0, 200)
    ChrSetDirection(0x00FE, 270, 200)
    ChrSetDirection(0x00FE, 180, 200)

    Jump('func_0A_1674')

    def _loc_169C(): pass

    label('loc_169C')

    Return()

# id: 0x000B offset: 0x169D
@scena.Code('func_0B_169D')
def func_0B_169D():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_16C1',
    )

    ChrSetDirection(0x00FE, 45, 300)
    Sleep(1000)

    ChrSetDirection(0x00FE, 315, 300)
    Sleep(1000)

    Jump('func_0B_169D')

    def _loc_16C1(): pass

    label('loc_16C1')

    Return()

# id: 0x000C offset: 0x16C2
@scena.Code('func_0C_16C2')
def func_0C_16C2():
    ChrWalkTo(0x00FE, 710, -1000, 2580, 5000, 0x00)
    ChrWalkTo(0x00FE, 650, -1000, -1790, 5000, 0x00)
    ChrSetSubChip(0x00FE, 0)
    ChrSetDirection(0x00FE, 225, 400)

    Return()

# id: 0x000D offset: 0x16F7
@scena.Code('func_0D_16F7')
def func_0D_16F7():
    ChrSetFlags(0x00FE, 0x1000)
    ChrSetChipByIndex(0x00FE, 17)
    ChrWalkTo(0x00FE, 710, -1000, 2580, 5000, 0x00)
    ChrWalkTo(0x00FE, -160, -1000, -920, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 1)
    ChrSetSubChip(0x00FE, 0)
    ChrClearFlags(0x00FE, 0x1000)
    ChrSetDirection(0x00FE, 225, 400)

    Return()

# id: 0x000E offset: 0x1740
@scena.Code('func_0E_1740')
def func_0E_1740():
    ChrSetFlags(0x00FE, 0x1000)
    ChrSetChipByIndex(0x00FE, 20)
    ChrWalkTo(0x00FE, 710, -1000, 2580, 4500, 0x00)
    ChrWalkTo(0x00FE, 1970, -1000, -1140, 4500, 0x00)
    ChrSetChipByIndex(0x00FE, 4)
    ChrSetSubChip(0x00FE, 0)
    ChrClearFlags(0x00FE, 0x1000)
    ChrSetDirection(0x00FE, 225, 400)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

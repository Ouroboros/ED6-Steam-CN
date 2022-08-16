import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import R3401_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R3401   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'R3401.x'
    header.mapIndex       = 1
    header.bgm            = 30
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
        ('ED6_DT09/CH10130._CH', 'ED6_DT09/CH10130P._CP'),
        ('ED6_DT09/CH10131._CH', 'ED6_DT09/CH10131P._CP'),
        ('ED6_DT09/CH10750._CH', 'ED6_DT09/CH10750P._CP'),
        ('ED6_DT09/CH10751._CH', 'ED6_DT09/CH10751P._CP'),
        ('ED6_DT09/CH10760._CH', 'ED6_DT09/CH10760P._CP'),
        ('ED6_DT09/CH10761._CH', 'ED6_DT09/CH10761P._CP'),
        ('ED6_DT09/CH10770._CH', 'ED6_DT09/CH10770P._CP'),
        ('ED6_DT09/CH10771._CH', 'ED6_DT09/CH10771P._CP'),
        ('ED6_DT29/CH12410._CH', 'ED6_DT29/CH12410P._CP'),
        ('ED6_DT29/CH12411._CH', 'ED6_DT29/CH12411P._CP'),
        ('ED6_DT06/CH20020._CH', 'ED6_DT06/CH20020P._CP'),
        ('ED6_DT07/CH00065._CH', 'ED6_DT07/CH00065P._CP'),
        ('ED6_DT27/CH03090._CH', 'ED6_DT27/CH03090P._CP'),
        ('ED6_DT06/CH20053._CH', 'ED6_DT06/CH20053P._CP'),
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT27/CH03091._CH', 'ED6_DT27/CH03091P._CP'),
        ('ED6_DT26/CH20284._CH', 'ED6_DT26/CH20284P._CP'),
    ]

# id: 0x10001 offset: 0x132
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '测量仪',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '亚妮拉丝',
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
            name                = '阿加特',
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
            name                = '雪拉扎德',
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
            name                = '艾尔·雷登关所方向',
            x                   = 169300,
            z                   = 0,
            y                   = -27030,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '蔡斯方向',
            x                   = 330710,
            z                   = 0,
            y                   = -37560,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x1F2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = 257600,
            z           = 70,
            y           = -24310,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01D0,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 286240,
            z           = 20,
            y           = -35830,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01CE,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 215540,
            z           = 0,
            y           = -31930,
            word_0C     = 0x005A,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01CE,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x246
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 275760,
            y           = -2000,
            z           = -27140,
            range       = 280150,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFF7482,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000002,
        ),
    )

# id: 0x10004 offset: 0x266
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 257600,
            triggerZ            = -70,
            triggerY            = -24310,
            triggerRange        = 3000,
            actorX              = 257600,
            actorZ              = -70,
            actorY              = -24310,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 284880,
            triggerZ            = 50,
            triggerY            = -26870,
            triggerRange        = 1000,
            actorX              = 284880,
            actorZ              = 1050,
            actorY              = -26870,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 267860,
            triggerZ            = 0,
            triggerY            = -29500,
            triggerRange        = 1000,
            actorX              = 268340,
            actorZ              = 0,
            actorY              = -25650,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2D2
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x2D3
@scena.Code('func_01_2D3')
def func_01_2D3():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_34C',
    )

    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    OP_71(0x0005, 0x0004)
    OP_71(0x0006, 0x0004)
    OP_71(0x0007, 0x0004)
    OP_71(0x0008, 0x0004)
    OP_71(0x0009, 0x0004)
    OP_71(0x000A, 0x0004)
    OP_71(0x000B, 0x0004)
    OP_71(0x000C, 0x0004)
    OP_71(0x000D, 0x0004)
    OP_71(0x000E, 0x0004)
    OP_71(0x000F, 0x0004)
    OP_71(0x0010, 0x0004)
    OP_79(0xFF, 0x0002)
    OP_64(0x02, 0x0001)
    StopEffect(0x80, 0x00)
    OP_C4(0x00, 0x00000001)
    OP_78(0x00, 0x00, 0x00)

    Jump('loc_34C')

    def _loc_34C(): pass

    label('loc_34C')

    OP_16(0x02, 4000, 127000, -157000, 2293816)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 2, 0x141A)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 3, 0x141B)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_371',
    )

    OP_64(0x00, 0x0001)

    Jump('loc_375')

    def _loc_371(): pass

    label('loc_371')

    OP_65(0x00, 0x0001)

    def _loc_375(): pass

    label('loc_375')

    ChrSetFlags(0x000E, 0x0080)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 3, 0x141B)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3A7',
    )

    OP_72(0x0012, 0x0004)
    OP_72(0x0013, 0x0004)
    OP_72(0x0014, 0x0004)
    OP_72(0x0015, 0x0004)
    PlaySE(158, 0x01, 0x64)
    OP_24(0x009E, 0x50)

    def _loc_3A7(): pass

    label('loc_3A7')

    ExecExpressionWithValue(
        0x0010,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_407',
    )

    LoadEffect(0x02, 'map\\\\mp027_00.eff')
    PlayEffect(0x02, 0x02, 0x00FF, 284880, 1050, -26870, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)

    def _loc_407(): pass

    label('loc_407')

    Return()

# id: 0x0002 offset: 0x408
@scena.Code('func_02_408')
def func_02_408():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 2, 0x141A)),
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 7, 0x1417)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_415',
    )

    Return()

    def _loc_415(): pass

    label('loc_415')

    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x0283, 2, 0x141A))
    Fade(1000)
    CameraMove(279460, 150, -31510, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetPos(0x0101, 279920, 150, -32780, 0)
    ChrSetPos(0x00F7, 278990, 150, -31880, 42)
    ChrSetPos(0x0107, 279800, 150, -30480, 188)
    ChrSetPos(0x00F9, 281010, 0, -31850, 321)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010230107V#1011F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230108V卡鲁迪亚隧道的第一座桥\n',
            '应该就是这里了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070230109V#061F嗯，让我想想设置在\n',
            '桥的哪一边比较好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230110V#064F嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0107, 270, 400)
    Sleep(500)

    ChrSetDirection(0x0107, 90, 400)
    ChrSetDirection(0x0107, 45, 400)
    Sleep(500)

    ChrSetDirection(0x0101, 50, 400)
    ChrSetDirection(0x00F7, 50, 400)
    ChrSetDirection(0x00F9, 50, 400)

    ChrTalk(
        0x0107,
        (
            '#0070230111V#060F这里有回复装置，\n',
            '还是不要放在这里了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230112V这样的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0107, 270, 400)
    Sleep(500)

    @scena.Lambda('lambda_05EC')
    def lambda_05EC():
        ChrTurnDirection(0x00FE, 0x0107, 400)
        Yield()

        Jump('lambda_05EC')

    DispatchAsync2(0x0101, 0x0001, lambda_05EC)

    @scena.Lambda('lambda_05FD')
    def lambda_05FD():
        ChrTurnDirection(0x00FE, 0x0107, 400)
        Yield()

        Jump('lambda_05FD')

    DispatchAsync2(0x00F7, 0x0001, lambda_05FD)

    @scena.Lambda('lambda_060E')
    def lambda_060E():
        ChrTurnDirection(0x00FE, 0x0107, 400)
        Yield()

        Jump('lambda_060E')

    DispatchAsync2(0x00F9, 0x0001, lambda_060E)

    @scena.Lambda('lambda_061F')
    def lambda_061F():
        ChrWalkTo(0x00FE, 260180, 0, -30550, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_061F)

    @scena.Lambda('lambda_063A')
    def lambda_063A():
        CameraMove(271840, 150, -30100, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_063A)

    @scena.Lambda('lambda_0652')
    def lambda_0652():
        OP_67(0, 8330, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0652)

    Sleep(3500)

    TerminateThread(0x0101, 0x02)
    TerminateThread(0x0101, 0x03)

    @scena.Lambda('lambda_0677')
    def lambda_0677():
        ChrWalkTo(0x00FE, 260490, -10, -30240, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_0677)

    Fade(1000)
    CameraMove(259010, 20, -28410, 0)
    OP_67(0, 8330, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(89000, 0)
    OP_6E(262, 0)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x00F7, 0x01)
    TerminateThread(0x00F9, 0x01)
    Sleep(1000)

    CreateThread(0x0101, 0x00, 0x00, func_04_BCC)
    Sleep(200)

    CreateThread(0x00F7, 0x00, 0x00, func_05_C05)
    Sleep(200)

    CreateThread(0x00F9, 0x00, 0x00, func_06_C3E)
    WaitForThreadExit(0x0107, 0x0001)

    @scena.Lambda('lambda_0709')
    def lambda_0709():
        ChrWalkTo(0x00FE, 257910, 50, -25930, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_0709)

    WaitForThreadExit(0x0107, 0x0001)
    ChrSetDirection(0x0107, 90, 400)
    Sleep(500)

    ChrSetDirection(0x0107, 297, 400)
    Sleep(500)

    ChrTalk(
        0x0107,
        (
            '#0070230113V#064F#5P哎…让天线对着\n',
            '蔡斯的方向……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230114V#060F嗯……这里就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x00F7, 0x0000)
    WaitForThreadExit(0x00F9, 0x0000)
    ChrSetDirection(0x0107, 140, 400)

    ChrTalk(
        0x0107,
        (
            '#0070230115V#061F姐姐。\n',
            '我想这里应该可以哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230116V现在就开始设置测量仪吗？',
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
        100,
        0,
        (
            TXT(0x00, '【设置测量仪】\n'),
            TXT(0x01, '【先不设置】\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8B9',
    )

    ChrTalk(
        0x0107,
        (
            '#0070230032V#061F那么我就开始\n',
            '进行设置工作了哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230028V请稍等一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9E4')

    def _loc_8B9(): pass

    label('loc_8B9')

    ChrTalk(
        0x0107,
        (
            '#0070230034V#064F哎……先不设置吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230030V#060F那就等准备好以后\n',
            '再来这个地方调查吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230031V到时再进行设置工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(261190, -20, -31590, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, 259760, 0, -30960, 270)
    ChrSetPos(0x0001, 259760, 0, -30960, 270)
    ChrSetPos(0x0002, 259760, 0, -30960, 270)
    ChrSetPos(0x0003, 259760, 0, -30960, 270)
    OP_69(0x0000, 0)
    OP_65(0x00, 0x0001)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

    def _loc_9E4(): pass

    label('loc_9E4')

    FadeOut(1000, 0, -1)
    OP_0D()
    Call(0, 0x0007)

    Return()

# id: 0x0003 offset: 0x9F4
@scena.Code('func_03_9F4')
def func_03_9F4():
    EventBegin(0x00)
    Fade(1000)
    CameraMove(257060, 50, -25420, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 256130, 30, -26520, 45)
    ChrSetPos(0x00F7, 257709, 50, -25940, 315)
    ChrSetPos(0x0107, 256660, 40, -25120, 45)
    ChrSetPos(0x00F9, 255050, 0, -25780, 47)
    OP_0D()
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
            TXT(0x00, '【设置测量仪】\n'),
            TXT(0x01, '【先不设置】\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B2C',
    )

    ChrTalk(
        0x0107,
        (
            '#0070230032V#061F#5P那么，\n',
            '进行设置工作了哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230028V请稍等一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BBC')

    def _loc_B2C(): pass

    label('loc_B2C')

    ChrSetDirection(0x0107, 225, 400)

    ChrTalk(
        0x0107,
        (
            '#0070230034V#064F#5P哎……先不设置吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230030V#060F那就等准备好以后\n',
            '再来这个地方调查吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230031V到时再进行设置工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

    def _loc_BBC(): pass

    label('loc_BBC')

    FadeOut(1000, 0, -1)
    OP_0D()
    Call(0, 0x0007)

    Return()

# id: 0x0004 offset: 0xBCC
@scena.Code('func_04_BCC')
def func_04_BCC():
    ChrSetPos(0x0101, 270570, 0, -31410, 265)

    @scena.Lambda('lambda_0BE3')
    def lambda_0BE3():
        ChrWalkTo(0x00FE, 259760, 0, -30960, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0BE3)

    WaitForThreadExit(0x0101, 0x0001)
    ChrSetDirection(0x0101, 323, 400)

    Return()

# id: 0x0005 offset: 0xC05
@scena.Code('func_05_C05')
def func_05_C05():
    ChrSetPos(0x00F7, 271930, 0, -30560, 268)

    @scena.Lambda('lambda_0C1C')
    def lambda_0C1C():
        ChrWalkTo(0x00FE, 261029, -30, -30130, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_0C1C)

    WaitForThreadExit(0x00F7, 0x0001)
    ChrSetDirection(0x00F7, 323, 400)

    Return()

# id: 0x0006 offset: 0xC3E
@scena.Code('func_06_C3E')
def func_06_C3E():
    ChrSetPos(0x00F9, 272280, 0, -32150, 272)

    @scena.Lambda('lambda_0C55')
    def lambda_0C55():
        ChrWalkTo(0x00FE, 261200, -20, -31790, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_0C55)

    WaitForThreadExit(0x00F9, 0x0001)
    ChrSetDirection(0x00F9, 323, 400)

    Return()

# id: 0x0007 offset: 0xC77
@scena.Code('func_07_C77')
def func_07_C77():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    CameraMove(257060, 50, -25420, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(80000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 256130, 30, -26520, 45)
    ChrSetPos(0x00F7, 257709, 50, -25940, 315)
    ChrSetPos(0x0107, 256660, 40, -25120, 45)
    ChrSetPos(0x00F9, 255050, 0, -25780, 47)
    OP_72(0x0012, 0x0004)
    OP_72(0x0013, 0x0004)
    Sleep(2000)

    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0107,
        (
            '#0070230037V#061F#5P嗯，这样就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E5B',
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
            TXT(0x00, '【◇第一次设置测量仪】\n'),
            TXT(0x01, '【◇设置了托兰特平原的测量仪】\n'),
            TXT(0x02, '【◇设置了雷斯顿要塞的测量仪】\n'),
            TXT(0x03, '【◇设置了托兰特平原和雷斯顿要塞的测量仪】\n'),
            TXT(0x04, '【◇不变更】\n'),
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
        (0x00000000, 'loc_E2B'),
        (0x00000001, 'loc_E37'),
        (0x00000002, 'loc_E43'),
        (0x00000003, 'loc_E4F'),
        (-1, 'loc_E5B'),
    )

    def _loc_E2B(): pass

    label('loc_E2B')

    ClearScenaFlags(ScenaFlag(0x0283, 1, 0x1419))
    ClearScenaFlags(ScenaFlag(0x0283, 3, 0x141B))
    ClearScenaFlags(ScenaFlag(0x0283, 7, 0x141F))

    Jump('loc_E5B')

    def _loc_E37(): pass

    label('loc_E37')

    SetScenaFlags(ScenaFlag(0x0283, 1, 0x1419))
    ClearScenaFlags(ScenaFlag(0x0283, 3, 0x141B))
    ClearScenaFlags(ScenaFlag(0x0283, 7, 0x141F))

    Jump('loc_E5B')

    def _loc_E43(): pass

    label('loc_E43')

    ClearScenaFlags(ScenaFlag(0x0283, 1, 0x1419))
    ClearScenaFlags(ScenaFlag(0x0283, 3, 0x141B))
    SetScenaFlags(ScenaFlag(0x0283, 7, 0x141F))

    Jump('loc_E5B')

    def _loc_E4F(): pass

    label('loc_E4F')

    SetScenaFlags(ScenaFlag(0x0283, 1, 0x1419))
    ClearScenaFlags(ScenaFlag(0x0283, 3, 0x141B))
    SetScenaFlags(ScenaFlag(0x0283, 7, 0x141F))

    Jump('loc_E5B')

    def _loc_E5B(): pass

    label('loc_E5B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 1, 0x1419)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 7, 0x141F)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_13DF',
    )

    ChrTalk(
        0x0101,
        (
            '#0010230128V#1004F哎～装好之后\n',
            '原来是这样的啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230039V#1015F不过……\n',
            '这个像盘子一样的东西是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0107, 225, 400)

    ChrTalk(
        0x0107,
        (
            '#0070230040V#060F#5P这个叫做抛物面天线\n',
            '是一种可以集中导力波的天线。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230041V通过它可以把强力的导力波\n',
            '传送到很远的地方……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230042V即使在卡鲁迪亚隧道这种地方\n',
            '也都一样可以传送到呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_113D',
    )

    ChrSetDirection(0x0104, 90, 400)

    ChrTalk(
        0x0104,
        (
            '#0040230133V#033F#6P嗯……\n',
            '那可是很厉害的东西啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040230044V#030F那么…\n',
            '在市场中也能买到这东西吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0107, 270, 400)

    ChrTalk(
        0x0107,
        (
            '#0070230135V#560F#5P啊，我也不是\n',
            '很清楚呢，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230046V不过爷爷的发明一般在问世半年后\n',
            '就会在市面贩卖了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040230137V#031F#6P呼，那可太令人期待了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_113A',
    )

    ChrSetDirection(0x0103, 270, 400)

    ChrTalk(
        0x0103,
        (
            '#0030230048V#027F#5P哎呀……想用在『工作联络』中吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040230139V#035F#6P哈～你在说什么嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_113A(): pass

    label('loc_113A')

    Jump('loc_12F3')

    def _loc_113D(): pass

    label('loc_113D')

    ChrSetDirection(0x0105, 90, 400)

    ChrTalk(
        0x0105,
        (
            '#0060230140V#044F#6P那个…提妲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060230051V我以前听说过，导力波遇到障碍物\n',
            '就会减弱，不过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060230052V这个装置为什么在洞窟\n',
            '这样的地方也可以使用呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0107, 270, 400)

    ChrTalk(
        0x0107,
        (
            '#0070230143V#560F#5P嗯，这种天线\n',
            '会赋予导力波指向性，\n',
            '所以可以顺利进行传送。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230054V即使是像洞窟这种地方，\n',
            '导力波似乎也能藉由墙壁反射\n',
            '一路传送到出口。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060230145V#040F#6P原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060230056V#041F不愧是拉赛尔博士啊，\n',
            '天才的称号果然名不虚传。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_12F3(): pass

    label('loc_12F3')

    ChrTalk(
        0x0101,
        (
            '#0010230147V#1007F嗯…看起来只是个\n',
            '不起眼的东西，竟然……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230058V#1006F不过这样一来就可以\n',
            '把地震情报传送出去了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0107, 225, 400)

    ChrTalk(
        0x0107,
        (
            '#0070230059V#560F#5P啊、嗯。\n',
            '不过现在还没有启动，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230060V那我现在就按下开关了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0107, 45, 400)

    Jump('loc_143C')

    def _loc_13DF(): pass

    label('loc_13DF')

    ChrTalk(
        0x0101,
        (
            '#0010230151V#1006F那么只剩下\n',
            '打开开关了对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070230062V#560F#5P嗯，请等一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_143C(): pass

    label('loc_143C')

    Fade(500)
    ChrSetSubChip(0x0107, 0)
    ChrSetChipByIndex(0x0107, 11)
    OP_0D()
    ChrSetDirection(0x00F7, 315, 400)
    ChrSetDirection(0x00F9, 45, 400)
    Sleep(500)

    PlaySE(156, 0x00, 0x64)
    Sleep(1000)

    OP_72(0x0014, 0x0004)
    OP_72(0x0015, 0x0004)
    PlaySE(158, 0x01, 0x64)
    OP_24(0x009E, 0x50)
    Sleep(2000)

    Fade(500)
    ChrSetSubChip(0x0107, 0)
    ChrSetChipByIndex(0x0107, 65535)
    OP_0D()
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 1, 0x1419)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 7, 0x141F)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_15F1',
    )

    ChrSetDirection(0x0107, 225, 400)

    ChrTalk(
        0x0107,
        (
            '#0070230153V#061F#5P呼，已经启动完毕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230154V#1006F辛苦啦，提妲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230155V#1015F不过…放在这种地方，\n',
            '难道不会被魔兽破坏吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230156V这种装置应该脆弱易损吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070230157V#560F#5P啊，这个不用担心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230090V因为装置具备了\n',
            '类似路灯的驱赶魔兽功能。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230159V#1011F是吗，那就放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1678')

    def _loc_15F1(): pass

    label('loc_15F1')

    ChrSetDirection(0x0107, 225, 400)

    ChrTalk(
        0x0107,
        (
            '#0070230153V#061F#5P呼，已经启动完毕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1653',
    )

    ChrTalk(
        0x0106,
        (
            '#0050230161V#051F喔，辛苦啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1678')

    def _loc_1653(): pass

    label('loc_1653')

    ChrTalk(
        0x0103,
        (
            '#0030230162V#021F呵呵，辛苦啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1678(): pass

    label('loc_1678')

    ChrSetPos(0x0009, 269420, 0, -30490, 0)
    ChrClearFlags(0x0009, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_16AE',
    )

    ChrSetPos(0x000B, 269390, 0, -31690, 0)
    ChrClearFlags(0x000B, 0x0080)

    Jump('loc_16C4')

    def _loc_16AE(): pass

    label('loc_16AE')

    ChrSetPos(0x000A, 269390, 0, -31690, 0)
    ChrClearFlags(0x000A, 0x0080)

    def _loc_16C4(): pass

    label('loc_16C4')

    NpcTalk(
        0x0009,
        '女孩的声音',
        (
            '#0120230163V#3P啊！\n',
            '艾丝蒂尔！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetDirection(0x0101, 135, 400)

    ChrTalk(
        0x0101,
        (
            '#0010230164V#1004F#6P哎……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1743')
    def lambda_1743():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_1743')

    DispatchAsync2(0x00F7, 0x0001, lambda_1743)

    @scena.Lambda('lambda_1754')
    def lambda_1754():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_1754')

    DispatchAsync2(0x0107, 0x0001, lambda_1754)

    @scena.Lambda('lambda_1765')
    def lambda_1765():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_1765')

    DispatchAsync2(0x00F9, 0x0001, lambda_1765)

    @scena.Lambda('lambda_1776')
    def lambda_1776():
        CameraMove(258339, 30, -28020, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1776)

    @scena.Lambda('lambda_178E')
    def lambda_178E():
        OP_67(0, 8300, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_178E)

    @scena.Lambda('lambda_17A6')
    def lambda_17A6():
        OP_6C(90000, 3000)

        ExitThread()

    DispatchAsync(0x00F7, 0x0003, lambda_17A6)

    @scena.Lambda('lambda_17B6')
    def lambda_17B6():
        ChrWalkTo(0x0009, 260649, -10, -30490, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_17B6)

    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_17F5',
    )

    @scena.Lambda('lambda_17DD')
    def lambda_17DD():
        ChrWalkTo(0x000B, 260670, 30, -31690, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_17DD)

    Jump('loc_1810')

    def _loc_17F5(): pass

    label('loc_17F5')

    @scena.Lambda('lambda_17FB')
    def lambda_17FB():
        ChrWalkTo(0x000A, 260670, 30, -31690, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_17FB)

    def _loc_1810(): pass

    label('loc_1810')

    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0009, 0x0001)

    @scena.Lambda('lambda_1820')
    def lambda_1820():
        ChrTurnDirection(0x0009, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1820)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1877',
    )

    ChrTalk(
        0x0101,
        (
            '#0010230165V#1004F#6P亚妮拉丝！\n',
            '还有雪拉姐！',
            TxtCtl.Enter,
        ),
    )

    WaitForThreadExit(0x000B, 0x0002)

    @scena.Lambda('lambda_186B')
    def lambda_186B():
        ChrTurnDirection(0x000B, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_186B)

    CloseMessageWindow()

    Jump('loc_18E6')

    def _loc_1877(): pass

    label('loc_1877')

    ChrTalk(
        0x0101,
        (
            '#0010230271V#1004F#6P亚妮拉丝！\n',
            '还有阿加特也……',
            TxtCtl.Enter,
        ),
    )

    WaitForThreadExit(0x000A, 0x0002)

    @scena.Lambda('lambda_18B7')
    def lambda_18B7():
        ChrTurnDirection(0x000A, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_18B7)

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070230272V#064F#5P啊啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18E6(): pass

    label('loc_18E6')

    TerminateThread(0x0107, 0x01)
    TerminateThread(0x00F7, 0x01)
    TerminateThread(0x00F9, 0x01)

    @scena.Lambda('lambda_18F8')
    def lambda_18F8():
        ChrWalkTo(0x00FE, 259380, 20, -28730, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_18F8)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_19FA',
    )

    Sleep(50)

    @scena.Lambda('lambda_191F')
    def lambda_191F():
        ChrWalkTo(0x00FE, 256959, 20, -28170, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_191F)

    Sleep(50)

    @scena.Lambda('lambda_193F')
    def lambda_193F():
        ChrWalkTo(0x00FE, 258209, 0, -29510, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0000, lambda_193F)

    Sleep(200)

    @scena.Lambda('lambda_195F')
    def lambda_195F():
        ChrWalkTo(0x00FE, 258769, 0, -27160, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0000, lambda_195F)

    Sleep(100)

    @scena.Lambda('lambda_197F')
    def lambda_197F():
        ChrWalkTo(0x00FE, 257000, 20, -26950, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0000, lambda_197F)

    Sleep(100)

    @scena.Lambda('lambda_199F')
    def lambda_199F():
        ChrWalkTo(0x00FE, 255500, 20, -27580, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0000, lambda_199F)

    WaitForThreadExit(0x0009, 0x0000)

    @scena.Lambda('lambda_19BF')
    def lambda_19BF():
        ChrTurnDirection(0x0009, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_19BF)

    WaitForThreadExit(0x0101, 0x0000)
    ChrSetDirection(0x0101, 135, 400)
    WaitForThreadExit(0x00F7, 0x0000)
    ChrSetDirection(0x00F7, 225, 400)
    WaitForThreadExit(0x0107, 0x0000)
    ChrSetDirection(0x0107, 135, 400)
    WaitForThreadExit(0x00F9, 0x0000)
    ChrSetDirection(0x00F9, 135, 400)

    Jump('loc_1B01')

    def _loc_19FA(): pass

    label('loc_19FA')

    Sleep(50)

    @scena.Lambda('lambda_1A05')
    def lambda_1A05():
        ChrWalkTo(0x00FE, 256959, 20, -28170, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1A05)

    Sleep(50)

    @scena.Lambda('lambda_1A25')
    def lambda_1A25():
        ChrWalkTo(0x00FE, 258209, 0, -29510, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_1A25)

    Sleep(200)

    @scena.Lambda('lambda_1A45')
    def lambda_1A45():
        ChrWalkTo(0x00FE, 258769, 0, -27160, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0000, lambda_1A45)

    Sleep(100)

    @scena.Lambda('lambda_1A65')
    def lambda_1A65():
        ChrWalkTo(0x00FE, 257000, 20, -26950, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0000, lambda_1A65)

    Sleep(100)

    @scena.Lambda('lambda_1A85')
    def lambda_1A85():
        ChrWalkTo(0x00FE, 255500, 20, -27580, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0000, lambda_1A85)

    WaitForThreadExit(0x0101, 0x0000)
    ChrSetDirection(0x0101, 135, 400)
    WaitForThreadExit(0x0009, 0x0000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1AC3',
    )

    @scena.Lambda('lambda_1AB8')
    def lambda_1AB8():
        ChrTurnDirection(0x0009, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_1AB8)

    Jump('loc_1AD1')

    def _loc_1AC3(): pass

    label('loc_1AC3')

    @scena.Lambda('lambda_1AC9')
    def lambda_1AC9():
        ChrTurnDirection(0x0009, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_1AC9)

    def _loc_1AD1(): pass

    label('loc_1AD1')

    WaitForThreadExit(0x0101, 0x0000)
    ChrSetDirection(0x0101, 135, 400)
    WaitForThreadExit(0x00F7, 0x0000)
    ChrSetDirection(0x00F7, 225, 400)
    WaitForThreadExit(0x0107, 0x0000)
    ChrSetDirection(0x0107, 135, 400)
    WaitForThreadExit(0x00F9, 0x0000)
    ChrSetDirection(0x00F9, 135, 400)

    def _loc_1B01(): pass

    label('loc_1B01')

    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3413',
    )

    ChrTalk(
        0x0009,
        (
            '#0120230166V#811F#5P嘿嘿，好久不见了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120230167V真没想到竟然能在这种地方\n',
            '再次相遇。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1CC7',
    )

    ChrTalk(
        0x000B,
        (
            '#0030230168V#021F不过…那边的那个男人\n',
            '好像在哪里见过嘛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030230169V#020F你现在不是应该还在\n',
            '亚尔摩的温泉逗留吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040230170V#035F#6P呵，这件事\n',
            '可就说来话长了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0030230171V#027F知道啦，我只是好奇而已嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230172V#1016F嗯，看来似乎是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0104, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0104,
        (
            '#0040230173V#036F#6P你们两个好过分啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DF9')

    def _loc_1CC7(): pass

    label('loc_1CC7')

    ChrTalk(
        0x000B,
        (
            '#0030230174V#021F呵呵，真是偶然的相遇啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030230175V#023F呀……\n',
            '那边的不是公主殿下吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060230176V#041F#6P好久不见了。\n',
            '雪拉扎德小姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060230177V#542F我现在正在协助艾丝蒂尔\n',
            '一起调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0030230178V#027F是吗，那可谢谢你啦。\n',
            '请多帮助艾丝蒂尔吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060220664V#048F#6P呵呵，不用客气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1DF9(): pass

    label('loc_1DF9')

    ChrTalk(
        0x0107,
        (
            '#0070230180V#560F#6P那个那个……\n',
            '好久不见了，雪拉姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0120230181V#814F#5P哈……',
            TxtCtl.Enter,
        ),
    )

    OP_9E(0x0009, 20, 0, 500, 4000)
    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0107, 600)

    ChrTalk(
        0x000B,
        (
            '#0030230182V#023F哎呀呀。\n',
            '提妲也在一起啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030230183V#021F对了，我记得雾香小姐说\n',
            '拉赛尔博士向协会提出了\n',
            '协助调查地震的请求。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030230184V所以你们就来帮忙了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070230185V#067F#6P嘿嘿，正是那样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0120230186V#1317F#5P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010230187V#1015F亚妮拉丝？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230188V怎么了？\n',
            '为什么突然发呆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0120230189V#1316F#5P……不行……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120230190V#812F我已经无法忍耐了！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230191V#1004F哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0009, 0x0040)

    @scena.Lambda('lambda_204C')
    def lambda_204C():
        CameraMove(257339, 30, -27020, 1000)

        ExitThread()

    DispatchAsync(0x0107, 0x0002, lambda_204C)

    @scena.Lambda('lambda_2064')
    def lambda_2064():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_2064')

    DispatchAsync2(0x0101, 0x0001, lambda_2064)

    @scena.Lambda('lambda_2075')
    def lambda_2075():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_2075')

    DispatchAsync2(0x00F7, 0x0001, lambda_2075)

    @scena.Lambda('lambda_2086')
    def lambda_2086():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_2086')

    DispatchAsync2(0x00F9, 0x0001, lambda_2086)

    ChrSetChipByIndex(0x0009, 15)
    OP_92(0x0009, 0x0107, 400, 5000, 0x00)

    @scena.Lambda('lambda_20AA')
    def lambda_20AA():
        OP_94(0x01, 0x0009, 0x0000, 0x000000C8, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_20AA)

    Yield()
    ChrSetDirection(0x0009, 315, 0)
    ChrSetFlags(0x0009, 0x0020)
    ChrSetChipByIndex(0x0009, 16)
    ChrSetSubChip(0x0009, 0)
    ChrTurnDirection(0x0107, 0x0009, 0)
    OP_94(0x01, 0x0107, 0x00B4, 0x000000C8, 0x000007D0, 0x00)
    WaitForThreadExit(0x0009, 0x0003)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x00F7, 0x01)
    TerminateThread(0x00F9, 0x01)
    OP_62(0x0009, 0x00000000, 2000, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(200)

    OP_62(0x0107, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    Fade(250)
    ChrSetSubChip(0x0009, 1)
    OP_0D()

    ChrTalk(
        0x0009,
        (
            '#0120230192V#1311F#5P啊啊啊～好可爱～！！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120230193V这么可爱的孩子\n',
            '实在让人忍不住想要抱抱啊～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0107,
        (
            '#0070230194V#064F#6P哇哇！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230195V#1016F（对、对了……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230196V（亚妮拉丝她…一看到\n',
            '可爱的东西就会失控…）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    ChrSetSubChip(0x0009, 0)
    OP_0D()

    ChrTalk(
        0x0009,
        (
            '#0120230197V#811F#5P你是叫提妲对吧？\n',
            '我是亚妮拉丝·艾尔菲德！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120230198V叫我亚妮拉丝姐姐就好啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070230199V#065F#6P呜、呜哎哎哎～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    Fade(250)
    ChrSetSubChip(0x0009, 1)
    OP_0D()

    ChrTalk(
        0x0009,
        (
            '#0120230200V#819F#5P啊啊啊啊！\n',
            '现在的表情也好可爱～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    ChrClearFlags(0x0009, 0x0020)
    ChrSetChipByIndex(0x0009, 12)
    ChrSetSubChip(0x0009, 0)
    ChrSetPos(0x0009, 257260, 20, -27260, 315)
    OP_0D()
    ChrSetDirection(0x0009, 135, 400)
    ChrSetDirection(0x0101, 45, 400)

    ChrTalk(
        0x0009,
        (
            '#0120230201V#812F#6P雪拉前辈！\n',
            '我可以把她带回家吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0030230202V#027F我明白你的心情，但还是克制一下吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030230203V那位老兄可是很可怕的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00F7, 225, 400)

    ChrTalk(
        0x0106,
        (
            '#0050230204V#552F#5P……为什么要扯上我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 135, 400)
    ChrSetDirection(0x00F9, 135, 400)

    ChrTalk(
        0x0101,
        (
            '#0010230205V#1011F#6P对了，雪拉姐\n',
            '你们为什么会在这里？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230206V难道\n',
            '是来找我们的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0030230207V#020F不，只是偶然遇到而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030230208V我们正在追捕\n',
            '空贼团和特务兵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010230209V#1020F#6P哎！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230210V空贼和特务兵……\n',
            '是逃亡中的余党吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050230211V#052F#5P的确，王国军也没有\n',
            '把他们全部抓捕归案呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050230212V你们现在有什么线索了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_25E4')
    def lambda_25E4():
        CameraMove(258339, 30, -28020, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_25E4)

    ChrWalkTo(0x0009, 259380, 20, -28730, 2500, 0x00)
    ChrTurnDirection(0x0009, 0x0107, 400)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0009,
        (
            '#0120230213V#810F协会那里倒是接到了\n',
            '几份目击情报，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120230214V但可信程度都不太高。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0030230215V#020F不过我们还是从中\n',
            '挑出了一些比较可疑的情报，\n',
            '目前正在各地展开调查。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030230216V#022F而且……我听说了，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030230217V『噬身之蛇』的爪牙似乎\n',
            '已经在卢安地区现身了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230218V#1007F嗯，嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230219V#1019F是个自称『怪盗绅士』，\n',
            '戴着假面具的奇怪家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050230220V#555F#5P虽然装束和性格比较怪异，\n',
            '但实力可是相当了得。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050230221V如果真的和他展开正面较量的话，\n',
            '恐怕会相当危险啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0120230222V#812F嗯嗯，连阿加特前辈\n',
            '都那么说的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120230223V看来『噬身之蛇』──\n',
            '确实是个非常危险的组织呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0030230224V#026F与其说危险，\n',
            '倒不如说他们的身份来历\n',
            '都无从得知比较正确呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030230225V#020F如果以后需要我们帮忙的话\n',
            '请别客气，尽管开口就是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030230226V通过协会的话\n',
            '马上就可以联络到我们的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230227V#1006F嗯，我们会的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230228V雪拉姐也是！如果需要我们帮忙的话\n',
            '就随时联系哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230229V我们马上就会赶到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0030230230V#021F呵呵，到时就拜托你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030230231V#027F虽然是难得的再会，\n',
            '不过这种地方也不适合聊天……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030230232V我们就\n',
            '先失陪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230233V#1017F啊、嗯……\n',
            '虽然很遗憾，但也没有办法呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2C54',
    )

    ChrTalk(
        0x0104,
        (
            '#0040230234V#036F#6P啊啊～太残忍了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040230235V面对着久别重逢的恋人，\n',
            '竟然会如此冷淡薄情？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0030230236V#021F啊，既然你这样说的话，\n',
            '不如就和我们一起走吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030230237V今天晚上一起去喝酒，好好庆祝一下\n',
            '美妙的重逢，这样总行了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0120230238V#811F啊，这主意不错⊙\n',
            '毕竟我也算是个酒豪呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040230239V#034F#6P……两位\n',
            '一路上请多加小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230240V#1019F真是的……\n',
            '一说到喝酒就原形毕露了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C54(): pass

    label('loc_2C54')

    ChrTalk(
        0x0106,
        (
            '#0050230241V#050F#5P我并不是故意轻视你们，\n',
            '不过你们毕竟是两个女人结伴同行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050230242V遇到什么事的话还是不要太乱来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0120230243V#814F哇～阿加特前辈\n',
            '竟然会这么关心我…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120230244V究竟在想什么呢？难道说…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0106, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0106,
        (
            '#0050230245V#552F#5P可恶，你是皮痒了吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0120230246V#1315F嘿嘿嘿……\n',
            '开个玩笑而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0030230247V#027F呵呵，说得也是。\n',
            '我们会牢记你的忠告。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0120230248V#1310F阿加特前辈，多保重哦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120230249V#811F艾丝蒂尔、提妲。\n',
            '下次再见面时要一起去玩哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230250V#1006F嗯！非常期待！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070230251V#560F#6P嗯嗯～再见啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2EA6')
    def lambda_2EA6():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_2EA6')

    DispatchAsync2(0x0101, 0x0001, lambda_2EA6)

    @scena.Lambda('lambda_2EB7')
    def lambda_2EB7():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_2EB7')

    DispatchAsync2(0x00F7, 0x0001, lambda_2EB7)

    @scena.Lambda('lambda_2EC8')
    def lambda_2EC8():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_2EC8')

    DispatchAsync2(0x0107, 0x0001, lambda_2EC8)

    @scena.Lambda('lambda_2ED9')
    def lambda_2ED9():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_2ED9')

    DispatchAsync2(0x00F9, 0x0001, lambda_2ED9)

    @scena.Lambda('lambda_2EEA')
    def lambda_2EEA():
        ChrWalkTo(0x00FE, 243410, 0, -25540, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_2EEA)

    Sleep(200)

    @scena.Lambda('lambda_2F0A')
    def lambda_2F0A():
        ChrWalkTo(0x00FE, 256170, 10, -29190, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2F0A)

    WaitForThreadExit(0x0009, 0x0001)

    @scena.Lambda('lambda_2F2A')
    def lambda_2F2A():
        CameraMove(255210, 20, -27320, 3000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_2F2A)

    @scena.Lambda('lambda_2F42')
    def lambda_2F42():
        ChrWalkTo(0x00FE, 243410, 0, -25540, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2F42)

    WaitForThreadExit(0x000B, 0x0001)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    Fade(500)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x00F7, 0x01)
    TerminateThread(0x0107, 0x01)
    TerminateThread(0x00F9, 0x01)
    CameraMove(257070, 20, -26960, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2860, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x00F7, 257800, 30, -27320, 270)
    OP_0D()
    ChrSetDirection(0x0101, 0, 400)
    ChrSetDirection(0x0107, 180, 400)
    ChrSetDirection(0x00F9, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010230252V#1017F#6P哈～在这种地方\n',
            '竟然能遇到雪拉姐她们，\n',
            '真是完全没想到啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230253V#1004F提妲，你没关系吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230254V亚妮拉丝突然就\n',
            '那么抱住你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070230255V#067F嘿嘿，我没事的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230256V……虽然说…\n',
            '吓了一大跳……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230257V#1016F#6P嗯～她并没有恶意的，\n',
            '你就原谅她好啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230258V#1015F话说回来，\n',
            '空贼和特务兵的余党……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050230259V#051F都是和『结社』一样，\n',
            '只会在暗中鬼祟行动的家伙啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050230260V他们两个继续追查下去的话，\n',
            '说不定能获得什么重要的线索。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 45, 400)
    ChrSetDirection(0x0107, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010230261V#1006F#6P那么我们也要加油了，\n',
            '绝对不可以输给他们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230262V#1011F总之……\n',
            '这里就已经ＯＫ了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 1, 0x1419)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 7, 0x141F)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_32D1',
    )

    ChrTalk(
        0x0106,
        (
            '#0050230263V#051F好！就保持这样的干劲，\n',
            '把剩下的测量仪也设置好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230096V#1006F#6P了解！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3410')

    def _loc_32D1(): pass

    label('loc_32D1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 1, 0x1419)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 7, 0x141F)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_3355',
    )

    ChrTalk(
        0x0106,
        (
            '#0050230265V#051F啊啊～这是第２个了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050230098V去把最后一个也搞定吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230101V#1006F#6P  ＯＫ～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3410')

    def _loc_3355(): pass

    label('loc_3355')

    ChrTalk(
        0x0106,
        (
            '#0050230268V#051F啊啊，这样就把\n',
            '全部测量仪设置完毕了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050230103V老爷子还在等着我们，\n',
            '赶快去中央工房的演算室吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230270V#1006F#6P  ＯＫ～！\n',
            '就在中央工房的５楼吧。',
            TxtCtl.Enter,
        ),
    )

    OP_28(0x0087, 0x01, 0x0200)
    CloseMessageWindow()

    def _loc_3410(): pass

    label('loc_3410')

    Jump('loc_4D1F')

    def _loc_3413(): pass

    label('loc_3413')

    ChrTalk(
        0x0009,
        (
            '#0120230273V#811F#5P好久不见了！\n',
            '雪拉前辈！艾丝蒂尔！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030230274V#021F#5P呵呵，好久不见了呢。\n',
            '你还是一样，这么有精神啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050230275V#051F怎么回事，竟然\n',
            '这么多人一起行动啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050230276V#052F噢。\n',
            '提妲也在一起吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050230277V#051F好久不见了啊，小家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0107,
        (
            '#0070230278V#062F#6P呜……\n',
            '谁是小家伙啊，真过分。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230279V#560F不过，真的是好久不见了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#0120230280V#814F哇！！真可爱！！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120230281V#1310F这孩子是谁呀！？\n',
            '艾丝蒂尔的妹妹吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230282V#1016F嘿嘿，可以算是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230283V#1006F她叫提妲，\n',
            '拉赛尔博士的孙女。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0120230284V#810F嗯，是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120230285V#811F我叫亚妮拉丝！\n',
            '亚妮拉丝·艾尔菲德！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120230286V请多多指教哦！提妲！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070230287V#560F#6P是、是的……\n',
            '请多多指教。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3913',
    )

    ChrTalk(
        0x000A,
        (
            '#0050230288V#555F怎么回事，在那边站着的\n',
            '不是埃雷波尼亚帝国的演奏家吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050230289V为什么连你也在一起啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040230290V#035F#6P呵，如此浅显易见\n',
            '的事情何必再问。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040230291V#037F帮助我可爱的小猫咪们\n',
            '难道还需要什么理由吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050230292V#552F该说什么才好……\n',
            '看来你们也很辛苦啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030230293V#027F#5P呵呵，是有一点呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230294V#1007F是非～常～辛苦啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230295V#1011F话说回来，阿加特你们\n',
            '为什么会出现在这里呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230206V难不成是\n',
            '来找我们的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3A6D')

    def _loc_3913(): pass

    label('loc_3913')

    ChrTalk(
        0x000A,
        (
            '#0050230297V#052F什么啊，站在那边的\n',
            '不就是公主吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050230298V怎么连你也在一起的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060230299V#041F#6P好久不见了，阿加特先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060230300V#542F其实我现在正在\n',
            '协助艾丝蒂尔进行调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050230301V#051F哈哈，公主还是\n',
            '这么热心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230302V#1011F对了，阿加特你们\n',
            '为什么会出现在这里呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230206V难不成是\n',
            '来找我们的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3A6D(): pass

    label('loc_3A6D')

    ChrTalk(
        0x000A,
        (
            '#0050230304V#051F不，只是偶然相遇而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050230305V我们正在追捕\n',
            '空贼团和特务兵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010230306V#1020F哎！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230307V空贼和特务兵……\n',
            '那些家伙的余党吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030230308V#023F#5P的确连王国军也没有\n',
            '把他们全部抓捕归案呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030230309V你们有什么线索了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0120230213V#810F协会那里倒是接到了\n',
            '几份目击情报…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120230214V但可信程度都不太高。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050230312V#551F但谨慎起见，还是要在各地巡视，\n',
            '调查一些可疑的场所。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050230313V#050F而且……我也听说了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050230314V『噬身之蛇』的爪牙似乎\n',
            '已经在卢安地区现身了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230218V#1007F嗯，嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230219V#1019F嗯，是个叫做『怪盗绅士』，\n',
            '戴着假面具的奇怪家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030230317V#022F#5P虽然打扮和性格比较怪异，\n',
            '但实力却是非常厉害的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030230318V如果真的和他展开正面较量的话，\n',
            '恐怕胜算不高呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0120230319V#812F嗯嗯…连雪拉前辈\n',
            '都那么说的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120230223V看来『噬身之蛇』──\n',
            '确实是个非常危险的组织呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050230321V#552F与其说危险\n',
            '倒不如说他们的身份来历\n',
            '都无从得知比较正确啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050230322V#050F如果以后需要我们帮忙的话，\n',
            '不要客气，尽管开口就是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050230323V通过协会的话，\n',
            '应该可以马上联络到我们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230227V#1006F嗯，我们会的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230325V阿加特你们也是，需要帮忙的话\n',
            '就随时联络我们哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230229V我们马上就会赶到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050230327V#053F哦！应该没那个必要，\n',
            '不过万一有需要的话我会去找你们的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050230328V#051F好了，这里也不是\n',
            '适合聊天的地方。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050230329V我们差不多也该走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230233V#1017F啊、嗯……\n',
            '虽然很遗憾，但也没有办法呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    OP_63(0x0107)

    ChrTalk(
        0x0107,
        (
            '#0070230331V#063F#6P啊……\n',
            '那个…阿加特哥哥。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050230332V#052F喔？怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0107,
        (
            '#0070230333V#560F#6P嗯、那个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230334V……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230335V#562F对不起……\n',
            '没什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050230336V#555F什么嘛，奇怪的家伙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050230337V#051F算了，替我向拉赛尔老爷子\n',
            '问声好吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050230338V还有啊，你也不要整天\n',
            '都琢磨那些机械了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050230339V小孩子就应该有小孩子的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070230340V#067F#6P嘿嘿……我知道啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230341V#560F不过，阿加特哥哥\n',
            '也不能太莽撞哦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230342V你总是喜欢意气用事，\n',
            '那样是很危险的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050230343V#055F哦……?\n',
            '竟然变得这么能言善道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070230344V#067F#6P嘿嘿，那是当然的啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230345V#066F我又不会……\n',
            '永远都是个小孩子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0120230346V#811F呵呵～对手是提妲的话，\n',
            '阿加特前辈也只能乖乖服输了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120230347V#1310F那我们这就走了，大家都要保重啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120230348V艾丝蒂尔，提妲。\n',
            '下次再见面时要一起去玩哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230250V#1006F嗯！非常期待！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070230350V#560F#6P是、是的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4421')
    def lambda_4421():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_4421')

    DispatchAsync2(0x0107, 0x0001, lambda_4421)

    @scena.Lambda('lambda_4432')
    def lambda_4432():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_4432')

    DispatchAsync2(0x00F7, 0x0001, lambda_4432)

    @scena.Lambda('lambda_4443')
    def lambda_4443():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_4443')

    DispatchAsync2(0x0101, 0x0001, lambda_4443)

    @scena.Lambda('lambda_4454')
    def lambda_4454():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_4454')

    DispatchAsync2(0x00F9, 0x0001, lambda_4454)

    @scena.Lambda('lambda_4465')
    def lambda_4465():
        ChrWalkTo(0x00FE, 243410, 0, -25540, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_4465)

    Sleep(200)

    @scena.Lambda('lambda_4485')
    def lambda_4485():
        ChrWalkTo(0x00FE, 256170, 10, -29190, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_4485)

    WaitForThreadExit(0x0009, 0x0001)

    @scena.Lambda('lambda_44A5')
    def lambda_44A5():
        CameraMove(255210, 20, -27320, 3000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_44A5)

    @scena.Lambda('lambda_44BD')
    def lambda_44BD():
        ChrWalkTo(0x00FE, 243410, 0, -25540, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_44BD)

    WaitForThreadExit(0x000A, 0x0001)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    Fade(1000)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x00F7, 0x01)
    TerminateThread(0x0107, 0x01)
    TerminateThread(0x00F9, 0x01)
    CameraMove(257070, 20, -26960, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2860, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x00F7, 257800, 30, -27320, 270)
    OP_0D()
    ChrSetDirection(0x0101, 45, 400)
    ChrSetDirection(0x00F9, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010230351V#1017F#6P哈～在这种地方\n',
            '竟然会遇到阿加特他们，\n',
            '真是完全没想到啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230352V#1016F阿加特和亚妮拉丝都还是老样子啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230353V实在没有办法想象他们两人\n',
            '在旅行时是如何相处的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030230354V#027F亚妮拉丝的性格\n',
            '那么地率直活泼。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030230355V就算是和阿加特这种别扭的家伙相处\n',
            '应该也不是什么困难的事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070230356V#063F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrSetDirection(0x0101, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010230357V#1004F#6P提妲？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0107,
        (
            '#0070230358V#065F哎……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(500)

    ChrSetDirection(0x0107, 180, 600)

    ChrTalk(
        0x0107,
        (
            '#0070230359V#067F怎、怎么了！？\n',
            '艾丝蒂尔姐姐！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230360V#1015F#6P你怎么啦？\n',
            '为什么一副若有所思的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070230361V#560F没、没有啦！！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230362V只是……\n',
            '稍微有些吃惊而已……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230363V#1004F#6P吃惊……为什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070230364V#065F哎……那个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230365V#067F阿加特哥哥……\n',
            '竟然已经有恋人了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230366V#1004F#6P恋人？？是指亚妮拉丝吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230367V#1016F啊哈哈，你搞错了啦，\n',
            '他们只是工作上的搭档。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070230368V#064F哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030230369V#027F呵呵，只是为了调查『结社』\n',
            '而联手行动而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030230370V完全不是你想的那样啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070230371V#560F是、是这样吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230372V#067F原来如此……嘿嘿嘿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230373V#1016F#6P（原来……是这样吗。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 45, 400)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010230374V#1015F#6P话说回来，\n',
            '空贼和特务兵的余党啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0103, 225, 400)

    ChrTalk(
        0x0103,
        (
            '#0030230375V#020F都是和『结社』一样\n',
            '藏身在暗地里行动的家伙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030230376V阿加特他们继续追查下去的话，\n',
            '应该能获得什么重要的线索才对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230261V#1006F#6P那么我们也要加油了，\n',
            '绝对不能输给她们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230262V#1011F总之……\n',
            '这里就已经ＯＫ了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 1, 0x1419)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 7, 0x141F)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4BD5',
    )

    ChrTalk(
        0x0103,
        (
            '#0030230379V#027F嗯，继续\n',
            '把剩下的测量仪设置好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230096V#1006F#6P了解！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4D1F')

    def _loc_4BD5(): pass

    label('loc_4BD5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 1, 0x1419)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0283, 7, 0x141F)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_4C57',
    )

    ChrTalk(
        0x0103,
        (
            '#0030230381V#526F嗯，这是第２个了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030230100V马上去设置最后一个吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230101V#1006F#6P  ＯＫ～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4D1F')

    def _loc_4C57(): pass

    label('loc_4C57')

    ChrTalk(
        0x0103,
        (
            '#0030230384V#026F嗯，这样一来，\n',
            '全部测量仪都设置完毕了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030230105V#020F拉赛尔博士还在等着我们，\n',
            '现在就回中央工房的演算室吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230270V#1006F#6P  ＯＫ～！\n',
            '就在中央工房的５楼吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0087, 0x01, 0x0200)

    def _loc_4D1F(): pass

    label('loc_4D1F')

    OP_64(0x00, 0x0001)
    SetScenaFlags(ScenaFlag(0x0283, 3, 0x141B))
    OP_28(0x0087, 0x01, 0x0020)
    EventEnd(0x00)

    Return()

# id: 0x0008 offset: 0x4D2F
@scena.Code('func_08_4D2F')
def func_08_4D2F():
    FadeOut(0, 0, -1)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)

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
            TXT(0x00, '【◇选择雪拉扎德为队友】\n'),
            TXT(0x01, '【◇选择阿加特为队友】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_4DA9'),
        (0x00000001, 'loc_4DAF'),
        (-1, 'loc_4DB5'),
    )

    def _loc_4DA9(): pass

    label('loc_4DA9')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_4DB5')

    def _loc_4DAF(): pass

    label('loc_4DAF')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_4DB5')

    def _loc_4DB5(): pass

    label('loc_4DB5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_4DC3',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_4DC7')

    def _loc_4DC3(): pass

    label('loc_4DC3')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_4DC7(): pass

    label('loc_4DC7')

    Return()

# id: 0x0009 offset: 0x4DC8
@scena.Code('func_09_4DC8')
def func_09_4DC8():
    MapClearFlags(0x00000001)
    CameraMove(0, 0, 0, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_4E02',
    )

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['雪拉扎德'],
            ChrTable['提妲'],
            0x00FF,
        ),
        (
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            0xFFFF,
        ),
    )

    Jump('loc_4E1C')

    def _loc_4E02(): pass

    label('loc_4E02')

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['阿加特'],
            ChrTable['提妲'],
            0x00FF,
        ),
        (
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            0xFFFF,
        ),
    )

    def _loc_4E1C(): pass

    label('loc_4E1C')

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0)

    Return()

# id: 0x000A offset: 0x4E2E
@scena.Code('func_0A_4E2E')
def func_0A_4E2E():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4EA5',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    If(
        (
            (Expr.Eval, "OP_40(0x0150, 0x02)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4E75',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '黑漆漆的，看不清楚。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_4E8A')

    def _loc_4E75(): pass

    label('loc_4E75')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '导力好像停止了。',
            TxtCtl.Enter,
        ),
    )

    def _loc_4E8A(): pass

    label('loc_4E8A')

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Jump('loc_5060')

    def _loc_4EA5(): pass

    label('loc_4EA5')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '这是一台可供旅行者回复体力的导力器装置。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
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
        32,
        1,
        (
            TXT(0x00, '在这里休息\n'),
            TXT(0x01, '离开\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5045',
    )

    FadeIn(100, 0)
    Sleep(500)

    OP_26(13)
    StopEffect(0x02, 0x02)
    PlayEffect(0x02, 0x02, 0x00FF, 284880, 1050, -26870, 0, 0, 0, 700, 700, 700, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0011, 0)
    OP_70(0x0011, 50)
    OP_73(0x0011)
    OP_20(0x00000BB8)
    PlaySE(12, 0x00, 0x64)
    StopEffect(0x02, 0x02)
    LoadEffect(0x01, 'map\\\\mp027_01.eff')
    PlayEffect(0x01, 0x01, 0x00FF, 284880, 1050, -26870, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    FadeOut(1000, 0, -1)
    Sleep(700)

    PlaySE(13, 0x00, 0x64)
    OP_0D()
    ChrSetStatus(0x00FF, 0xFE, 0)
    OP_69(0x0000, 0)
    OP_30(0x01)
    Sleep(3500)

    StopEffect(0x01, 0x02)
    PlayEffect(0x02, 0x02, 0x00FF, 284880, 1050, -26870, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0011, 0)
    OP_1E()
    FadeIn(1000, 0)
    OP_56(0x00)
    TalkEnd(0x00FF)

    Return()

    def _loc_5045(): pass

    label('loc_5045')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_505F',
    )

    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

    def _loc_505F(): pass

    label('loc_505F')

    Return()

    def _loc_5060(): pass

    label('loc_5060')

    Return()

# id: 0x000B offset: 0x5061
@scena.Code('func_0B_5061')
def func_0B_5061():
    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0011860001V#1001F这里好像可以钓上什么来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5099')
    def lambda_5099():
        CameraMove(268050, -1000, -27370, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_5099)

    @scena.Lambda('lambda_50B1')
    def lambda_50B1():
        CameraSetDistance(3200, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_50B1)

    @scena.Lambda('lambda_50C1')
    def lambda_50C1():
        OP_6C(45000, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_50C1)

    Sleep(1000)

    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '钓鱼吗？',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
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
        32,
        1,
        (
            TXT(0x00, '钓鱼\n'),
            TXT(0x01, '离开\n'),
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
    WaitForThreadExit(0x0000, 0x0001)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5166',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.GetChrWork, 0x101, 0x28),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0101,
        0x28,
        (
            (Expr.PushLong, 0x1),
            Expr.Not,
            Expr.And2,
            Expr.Return,
        ),
    )

    OP_C0(0x0E, 0x0000001E, 0x0004160E, 0x00000000, 0xFFFF8CC4, 0x00000000, 0x00041834, 0xFFFFFAEC, 0xFFFF9BCE)

    ExecExpressionWithValue(
        0x0101,
        0x28,
        (
            (Expr.PushReg, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_0D()
    EventEnd(0x01)

    Jump('loc_5175')

    def _loc_5166(): pass

    label('loc_5166')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5175',
    )

    EventEnd(0x01)

    def _loc_5175(): pass

    label('loc_5175')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

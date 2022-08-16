import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T1301_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1301   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1301.x'
    header.mapIndex       = 1
    header.bgm            = 84
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
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT09/CH10060._CH', 'ED6_DT09/CH10060P._CP'),
        ('ED6_DT09/CH10061._CH', 'ED6_DT09/CH10061P._CP'),
        ('ED6_DT09/CH10062._CH', 'ED6_DT09/CH10062P._CP'),
        ('ED6_DT09/CH10064._CH', 'ED6_DT09/CH10064P._CP'),
        ('ED6_DT09/CH10063._CH', 'ED6_DT09/CH10063P._CP'),
        ('ED6_DT07/CH01310._CH', 'ED6_DT07/CH01310P._CP'),
        ('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP'),
        ('ED6_DT07/CH00151._CH', 'ED6_DT07/CH00151P._CP'),
        ('ED6_DT07/CH00152._CH', 'ED6_DT07/CH00152P._CP'),
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00101._CH', 'ED6_DT07/CH00101P._CP'),
        ('ED6_DT07/CH00110._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT07/CH00111._CH', 'ED6_DT07/CH00111P._CP'),
        ('ED6_DT07/CH01650._CH', 'ED6_DT07/CH01650P._CP'),
        ('ED6_DT06/CH20053._CH', 'ED6_DT06/CH20053P._CP'),
        ('ED6_DT06/CH20053._CH', 'ED6_DT06/CH20053P._CP'),
        ('ED6_DT07/CH00330._CH', 'ED6_DT07/CH00330P._CP'),
        ('ED6_DT07/CH00331._CH', 'ED6_DT07/CH00331P._CP'),
        ('ED6_DT07/CH00332._CH', 'ED6_DT07/CH00332P._CP'),
        ('ED6_DT07/CH00320._CH', 'ED6_DT07/CH00320P._CP'),
        ('ED6_DT07/CH00321._CH', 'ED6_DT07/CH00321P._CP'),
        ('ED6_DT07/CH00322._CH', 'ED6_DT07/CH00322P._CP'),
        ('ED6_DT07/CH00324._CH', 'ED6_DT07/CH00324P._CP'),
    ]

# id: 0x10001 offset: 0x16A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '士兵卡多尔斯',
            x                   = -52000,
            z                   = -50,
            y                   = 12200,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵阿萨',
            x                   = -52000,
            z                   = -50,
            y                   = 12200,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '魔兽',
            x                   = -52000,
            z                   = -50,
            y                   = 12200,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '魔兽',
            x                   = -52000,
            z                   = -50,
            y                   = 12200,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '魔兽',
            x                   = -52000,
            z                   = -50,
            y                   = 12200,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '魔兽',
            x                   = -52000,
            z                   = -50,
            y                   = 12200,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '魔兽',
            x                   = -52000,
            z                   = -50,
            y                   = 12200,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '魔兽',
            x                   = -52000,
            z                   = -50,
            y                   = 12200,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '魔兽',
            x                   = -52000,
            z                   = -50,
            y                   = 12200,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '赛尔斯特队长',
            x                   = -52000,
            z                   = -50,
            y                   = 12200,
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
            name                = '赛罗斯副长',
            x                   = -52000,
            z                   = -50,
            y                   = 12200,
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
            name                = '士兵迈奇',
            x                   = -46890,
            z                   = -50,
            y                   = -15230,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 196631,
            chipIndex           = 23,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x2EA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x2EA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x2EA
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x2EA
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_2FD',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    MapSetFlags(0x10000000)
    Event(0, func_03_348)

    def _loc_2FD(): pass

    label('loc_2FD')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000066, 'loc_309'),
        (-1, 'loc_31E'),
    )

    def _loc_309(): pass

    label('loc_309')

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x52),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x10000000)
    Event(0, func_04_B8E)

    Jump('loc_31E')

    def _loc_31E(): pass

    label('loc_31E')

    Return()

# id: 0x0001 offset: 0x31F
@scena.Code('func_01_31F')
def func_01_31F():
    OP_16(0x02, 4000, -178000, -125000, 196676)

    Return()

# id: 0x0002 offset: 0x332
@scena.Code('func_02_332')
def func_02_332():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_347',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_332')

    def _loc_347(): pass

    label('loc_347')

    Return()

# id: 0x0003 offset: 0x348
@scena.Code('func_03_348')
def func_03_348():
    OP_4A(0x000A, 255)
    OP_4A(0x000B, 255)
    OP_4A(0x000C, 255)
    OP_4A(0x000D, 255)
    OP_4A(0x000E, 255)
    OP_4A(0x000F, 255)
    ChrSetPos(0x0008, -50060, 0, 12640, 0)
    ChrSetPos(0x0009, -50070, 450, 8800, 0)
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(-50200, 0, 9940, 0)
    CameraSetDistance(3000, 0)
    OP_6C(225000, 0)
    FadeIn(2000, 0)
    OP_0D()
    Sleep(1000)

    OP_70(0x0006, 100)
    OP_73(0x0006)
    ChrSetFlags(0x0009, 0x0004)
    ChrWalkTo(0x0009, -49991, 450, 11235, 2000, 0x00)
    ChrClearFlags(0x0009, 0x0004)
    OP_4A(0x0008, 255)

    ChrTalk(
        0x0009,
        (
            '#1450040227V#1P久等了。\n',
            '已经到交班时间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0009, 400)

    ChrTalk(
        0x0008,
        (
            '#1420040228V啊，已经这么晚了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1420040229V不过我说，既然没有人通行，\n',
            '那就没必要一直在这里站岗吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1420040230V其实我们可以整夜关着门，\n',
            '这样不就更省事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1450040231V#1P这是上头的决定，我们只能照办。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1450040232V#1P之前的空贼事件就不说了，\n',
            '最近还经常感觉到附近有骚动……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrSetDirection(0x0009, 270, 400)
    Sleep(200)

    ChrSetDirection(0x0009, 0, 400)
    ChrSetDirection(0x0009, 90, 400)
    Sleep(500)

    OP_62(0x0009, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#1420040233V怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1450040234V#1P你没听到有声音吗？\n',
            '听！沙沙沙的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1420040235V是风吹的声音吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x000A, -46050, -600, 23150, 225)
    ChrSetPos(0x000B, -43720, -300, 22970, 225)
    ChrSetPos(0x000C, -45010, -400, 25300, 225)
    ChrSetPos(0x000D, -44180, -500, 24380, 225)
    ChrSetPos(0x000E, -43420, -500, 25190, 225)
    ChrSetPos(0x000F, -42140, -600, 25680, 225)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    OP_20(0x000005DC)
    OP_21()
    PlaySE(403, 0x00, 0x64)

    NpcTalk(
        0x000F,
        '低吟声',
        (
            '#1P咕噜噜噜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetDirection(0x0009, 45, 400)
    ChrSetDirection(0x0008, 45, 400)
    PlayBGM(82)
    ChrSetFlags(0x000A, 0x0040)
    ChrSetFlags(0x000B, 0x0040)
    ChrSetFlags(0x000C, 0x0040)
    ChrSetFlags(0x000D, 0x0040)
    ChrSetFlags(0x000E, 0x0040)
    ChrSetFlags(0x000F, 0x0040)

    @scena.Lambda('lambda_0721')
    def lambda_0721():
        CameraSetDistance(3000, 2500)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0721)

    @scena.Lambda('lambda_0731')
    def lambda_0731():
        CameraMove(-47350, 0, 17130, 1700)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0731)

    Sleep(500)

    @scena.Lambda('lambda_074E')
    def lambda_074E():
        ChrWalkTo(0x00FE, -55460, 0, 16110, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_074E)

    @scena.Lambda('lambda_0769')
    def lambda_0769():
        ChrWalkTo(0x00FE, -59640, 0, 16410, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0769)

    @scena.Lambda('lambda_0784')
    def lambda_0784():
        ChrWalkTo(0x00FE, -56470, 0, 16880, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_0784)

    @scena.Lambda('lambda_079F')
    def lambda_079F():
        ChrWalkTo(0x00FE, -58070, 0, 17220, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_079F)

    Sleep(100)

    @scena.Lambda('lambda_07BF')
    def lambda_07BF():
        ChrWalkTo(0x00FE, -59260, 0, 18260, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_07BF)

    Sleep(100)

    @scena.Lambda('lambda_07DF')
    def lambda_07DF():
        ChrWalkTo(0x00FE, -56460, 0, 18480, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_07DF)

    Sleep(1000)

    @scena.Lambda('lambda_07FF')
    def lambda_07FF():
        CameraMove(-49494, 0, 13760, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_07FF)

    @scena.Lambda('lambda_0817')
    def lambda_0817():
        ChrWalkTo(0x00FE, -46460, 0, 16110, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0817)

    Sleep(150)

    @scena.Lambda('lambda_0837')
    def lambda_0837():
        ChrWalkTo(0x00FE, -50640, 0, 16410, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0837)

    Sleep(150)

    @scena.Lambda('lambda_0857')
    def lambda_0857():
        ChrWalkTo(0x00FE, -48050, 0, 17200, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_0857)

    Sleep(150)

    @scena.Lambda('lambda_0877')
    def lambda_0877():
        ChrWalkTo(0x00FE, -49070, 0, 17220, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0877)

    Sleep(150)

    @scena.Lambda('lambda_0897')
    def lambda_0897():
        ChrWalkTo(0x00FE, -50140, 0, 18000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0897)

    Sleep(150)

    @scena.Lambda('lambda_08B7')
    def lambda_08B7():
        ChrWalkTo(0x00FE, -46960, 0, 18000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_08B7)

    WaitForThreadExit(0x000B, 0x0001)
    ChrSetChipByIndex(0x000B, 1)
    CreateThread(0x000B, 0x01, 0x00, func_02_332)
    PlayEffect(0x12, 0xFF, 0x000B, 0, 100, 0, 0, 0, 0, 900, 900, 900, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_0918')
    def lambda_0918():
        OP_94(0x01, 0x00FE, 0x0000, 0x000002BC, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_0918)

    WaitForThreadExit(0x000A, 0x0001)
    ChrSetChipByIndex(0x000A, 1)
    CreateThread(0x000A, 0x01, 0x00, func_02_332)
    PlayEffect(0x12, 0xFF, 0x000A, 0, 100, 0, 0, 0, 0, 900, 900, 900, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_0974')
    def lambda_0974():
        OP_94(0x01, 0x00FE, 0x0000, 0x000002BC, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0974)

    WaitForThreadExit(0x000D, 0x0001)
    ChrSetChipByIndex(0x000D, 1)
    CreateThread(0x000D, 0x01, 0x00, func_02_332)
    PlayEffect(0x12, 0xFF, 0x000D, 0, 100, 0, 0, 0, 0, 900, 900, 900, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_09D0')
    def lambda_09D0():
        OP_94(0x01, 0x00FE, 0x0000, 0x000002BC, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_09D0)

    WaitForThreadExit(0x000C, 0x0001)
    ChrSetChipByIndex(0x000C, 1)
    CreateThread(0x000C, 0x01, 0x00, func_02_332)
    PlayEffect(0x12, 0xFF, 0x000C, 0, 100, 0, 0, 0, 0, 900, 900, 900, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_0A2C')
    def lambda_0A2C():
        OP_94(0x01, 0x00FE, 0x0000, 0x000002BC, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_0A2C)

    WaitForThreadExit(0x000E, 0x0001)
    ChrSetChipByIndex(0x000E, 1)
    CreateThread(0x000E, 0x01, 0x00, func_02_332)
    PlayEffect(0x12, 0xFF, 0x000E, 0, 100, 0, 0, 0, 0, 900, 900, 900, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_0A88')
    def lambda_0A88():
        OP_94(0x01, 0x00FE, 0x0000, 0x000002BC, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_0A88)

    WaitForThreadExit(0x000F, 0x0001)
    ChrSetChipByIndex(0x000F, 1)
    CreateThread(0x000F, 0x01, 0x00, func_02_332)
    PlayEffect(0x12, 0xFF, 0x000F, 0, 100, 0, 0, 0, 0, 900, 900, 900, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_0AE4')
    def lambda_0AE4():
        OP_94(0x01, 0x00FE, 0x0000, 0x000002BC, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_0AE4)

    WaitForThreadExit(0x000E, 0x0002)
    ChrTurnDirection(0x000E, 0x0008, 0)
    WaitForThreadExit(0x0101, 0x0001)
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_94(0x01, 0x0008, 0x00B4, 0x000001F4, 0x000003E8, 0x00)

    ChrTalk(
        0x0008,
        (
            '#1420040237V狼、狼群！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1450040238V喂喂，不是做梦吧！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    MapSetFlags(0x02000000)
    NewScene('ED6_DT01/T1311._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0xB8E
@scena.Code('func_04_B8E')
def func_04_B8E():
    FormationAddMember(0x05, 0xFF)
    MapClearFlags(0x00000010)
    ChrSetStatus(0x0005, 0x00, 22)
    OP_B5(0x0005, 0x00)
    OP_B5(0x0005, 0x01)
    OP_B5(0x0005, 0x02)
    EquipCmd(0x05, 0x0097)
    EquipCmd(0x05, 0x00F2)
    EquipCmd(0x05, 0x0110)
    EquipCmd(0x05, 0x025E, 0x00)
    EquipCmd(0x05, 0x0258, 0x01)
    EquipCmd(0x05, 0x0261, 0x02)
    AddCraft(0x0005, 0x00C8)
    AddCraft(0x0005, 0x00C9)
    AddSCraft(0x0005, 0x00FF)
    ChrSetStatus(0x0005, 0x05, 100)
    EventBegin(0x00)
    OP_6F(0x0006, 120)
    OP_72(0x0006, 0x0010)
    OP_6F(0x0007, 120)
    OP_72(0x0007, 0x0010)
    CameraMove(-49790, 450, 10030, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(4080, 0)
    OP_6C(201000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0106, -49160, 450, 11070, 20)
    ChrSetPos(0x0101, -50770, 450, 11200, 20)
    ChrSetPos(0x0102, -50340, 450, 10410, 20)
    ChrSetPos(0x0008, -52080, 0, 15480, 315)
    ChrSetPos(0x0009, -47500, 0, 13630, 90)
    ChrSetPos(0x0012, -49730, 0, 15340, 0)
    ChrSetPos(0x0011, -48130, 0, 14880, 45)
    ChrSetChipByIndex(0x0008, 20)
    ChrSetChipByIndex(0x0009, 20)
    ChrSetChipByIndex(0x0012, 20)
    ChrSetChipByIndex(0x0011, 17)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    OP_4A(0x000A, 255)
    OP_4A(0x000B, 255)
    OP_4A(0x000C, 255)
    OP_4A(0x000D, 255)
    OP_4A(0x000E, 255)
    OP_4A(0x000F, 255)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000A, -45600, 0, 14320, 270)
    ChrSetPos(0x000B, -47500, 0, 15620, 225)
    ChrSetPos(0x000F, -44730, 0, 19520, 225)
    ChrSetPos(0x000D, -47980, 0, 18190, 180)
    ChrSetPos(0x000C, -50380, 0, 18680, 135)
    ChrSetPos(0x000E, -51820, 0, 17000, 135)
    ChrTurnDirection(0x000A, 0x0009, 0)
    ChrTurnDirection(0x000B, 0x0011, 0)
    ChrTurnDirection(0x000F, 0x0011, 0)
    ChrTurnDirection(0x000D, 0x0012, 0)
    ChrTurnDirection(0x000C, 0x0012, 0)
    ChrTurnDirection(0x000E, 0x0008, 0)
    ChrTurnDirection(0x0012, 0x000D, 0)
    ChrSetChipByIndex(0x000A, 1)
    ChrSetChipByIndex(0x000B, 1)
    ChrSetChipByIndex(0x000C, 1)
    ChrSetChipByIndex(0x000D, 1)
    ChrSetChipByIndex(0x000E, 1)
    ChrSetChipByIndex(0x000F, 1)
    CreateThread(0x000A, 0x01, 0x00, func_02_332)
    CreateThread(0x000C, 0x01, 0x00, func_02_332)
    CreateThread(0x000D, 0x01, 0x00, func_02_332)
    CreateThread(0x000E, 0x01, 0x00, func_02_332)
    CreateThread(0x000F, 0x01, 0x00, func_02_332)
    ChrSetFlags(0x0101, 0x1000)
    ChrSetFlags(0x0102, 0x1000)
    ChrSetChipByIndex(0x0106, 15)
    CreateThread(0x0011, 0x01, 0x00, func_06_2A67)
    CreateThread(0x0009, 0x01, 0x00, func_05_281D)
    CreateThread(0x0012, 0x01, 0x00, func_07_2D7C)
    CameraMove(-49360, 450, 13230, 2000)

    ChrTalk(
        0x0102,
        (
            '#0020040245V#012F#2P狼群……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040246V#004F#2P不、不好了！\n',
            '我们快点去帮忙吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050040247V#053F#1P……给我回去，这里不用你们管。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0106, 400)

    ChrTalk(
        0x0101,
        (
            '#0010040248V#005F#2P什、什么不用我们管！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040249V你说这种话还算是个游击士吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050040250V#050F#1P你们别理解错了。\n',
            '守护关所是军队的使命。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050040251V而且这些士兵都受过严格训练，\n',
            '他们很快就会把这群狼消灭掉的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050040252V你们过去帮忙也只是多余罢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040253V#002F#2P虽、虽然这样说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A6(0x0000)
    TerminateThread(0x000F, 0x02)
    TerminateThread(0x000B, 0x02)
    OP_4A(0x0011, 1)
    TerminateThread(0x0011, 0xFF)
    ChrSetFlags(0x0011, 0x0020)

    ExecExpressionWithValue(
        0x0011,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0011, 19)
    PlaySE(132, 0x00, 0x64)

    @scena.Lambda('lambda_1017')
    def lambda_1017():
        OP_99(0x0011, 0x00, 0x03, 2000)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_1017)

    OP_93(0x0011, 0x000B, 600, 7000, 0x00)

    @scena.Lambda('lambda_1035')
    def lambda_1035():
        OP_99(0x0011, 0x03, 0x07, 2000)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_1035)

    ChrSetChipByIndex(0x000B, 5)
    TerminateThread(0x000B, 0xFF)
    ChrTurnDirection(0x000B, 0x0011, 0)

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x000B, 0x0020)
    PlayEffect(0x09, 0xFF, 0x00FF, -47540, 1000, 15460, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_109A')
    def lambda_109A():
        OP_94(0x01, 0x000B, 0x00B4, 0x000007D0, 0x00002AF8, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_109A)

    ChrSetRGBAMask(0x000B, 255, 255, 255, 0, 1000)

    ExecExpressionWithValue(
        0x0011,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0011, 17)
    ChrJumpTo(0x0011, -48130, 0, 14880, 1000, 5000)
    ChrSetFlags(0x000B, 0x0040)

    ChrTalk(
        0x0011,
        (
            '#1430040254V他说得没错！\n',
            '守护关所是我们军人的本分！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#1440040255V小姑娘，这里不用你们操心！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0011, 400)

    ChrTalk(
        0x0101,
        (
            '#0010040256V#003F#2P但、但是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1179')
    def lambda_1179():
        ChrWalkTo(0x00FE, -47730, 0, 15510, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_1179)

    ExecExpressionWithValue(
        0x0011,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0011, 19)
    PlaySE(194, 0x00, 0x64)
    OP_62(0x0106, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(70)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(70)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_11FD')
    def lambda_11FD():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_11FD)

    Sleep(300)

    @scena.Lambda('lambda_1210')
    def lambda_1210():
        ChrSetDirection(0x00FE, 160, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1210)

    @scena.Lambda('lambda_121E')
    def lambda_121E():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_121E)

    CameraMove(-49790, 450, 10030, 1000)

    ChrTalk(
        0x0106,
        (
            '#0050040257V#057F#1P……嘁！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0106, 0x0004)
    ChrWalkTo(0x0106, -50070, 290, 9000, 7000, 0x00)
    ChrWalkTo(0x0106, -50310, 450, 6810, 7000, 0x00)
    ChrClearFlags(0x0106, 0x0004)
    ChrSetFlags(0x0106, 0x0080)

    ChrTalk(
        0x0101,
        (
            '#0010040258V#004F#1P又怎么了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020040259V#016F#1P艾丝蒂尔，是对面！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040260V通往卢安那面的出口\n',
            '好像也受到了魔兽袭击。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040261V#005F#1P你说什么～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    CameraMove(-49110, -500, -18460, 0)
    OP_6C(315000, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    TerminateThread(0x0011, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x0012, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x000D, 0xFF)
    TerminateThread(0x000E, 0xFF)
    TerminateThread(0x000F, 0xFF)
    TerminateThread(0x0010, 0xFF)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetRGBAMask(0x000B, 255, 255, 255, 255, 0)
    ChrClearFlags(0x000A, 0x0020)
    ChrClearFlags(0x000B, 0x0020)
    ChrClearFlags(0x000C, 0x0020)
    ChrClearFlags(0x000D, 0x0020)
    ChrClearFlags(0x000E, 0x0020)
    ChrClearFlags(0x000F, 0x0020)
    ChrClearFlags(0x0010, 0x0020)
    ChrSetChipByIndex(0x000A, 1)
    ChrSetChipByIndex(0x000B, 1)
    ChrSetChipByIndex(0x000C, 1)
    ChrSetChipByIndex(0x000D, 1)
    ChrSetChipByIndex(0x000E, 1)
    ChrSetChipByIndex(0x000F, 2)
    ChrSetChipByIndex(0x0010, 1)
    ChrSetPos(0x000A, -45460, -500, -20310, 315)
    ChrSetPos(0x000B, -51540, -300, -17880, 90)
    ChrSetPos(0x000D, -51890, -500, -20520, 45)
    ChrSetPos(0x000C, -50260, -500, -20200, 45)
    ChrSetPos(0x000E, -48980, -500, -20950, 0)
    ChrSetPos(0x000F, -44270, -300, -18680, 270)
    ChrSetPos(0x0010, -44460, 0, -17870, 225)
    CreateThread(0x000A, 0x01, 0x00, func_02_332)
    CreateThread(0x000B, 0x01, 0x00, func_02_332)
    CreateThread(0x000C, 0x01, 0x00, func_02_332)
    CreateThread(0x000D, 0x01, 0x00, func_02_332)
    CreateThread(0x000E, 0x01, 0x00, func_02_332)
    CreateThread(0x000F, 0x01, 0x00, func_02_332)
    CreateThread(0x0010, 0x01, 0x00, func_02_332)
    ChrSetPos(0x0013, -49160, -600, -17710, 180)
    ChrSetFlags(0x000F, 0x0040)
    ChrClearFlags(0x0106, 0x0080)
    ChrSetPos(0x0106, -50596, 300, -9470, 0)
    ChrSetPos(0x0101, -50644, 0, -9440, 180)
    ChrSetPos(0x0102, -49430, 0, -9440, 180)
    ChrSetFlags(0x0106, 0x1000)
    ChrSetChipByIndex(0x0106, 8)

    @scena.Lambda('lambda_150A')
    def lambda_150A():
        OP_92(0x000F, 0x0013, 2300, 1300, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_150A)

    OP_0D()
    ChrWalkTo(0x0106, -49276, -500, -16530, 6000, 0x00)
    ChrSetChipByIndex(0x0106, 9)
    PlaySE(163, 0x00, 0x64)
    ChrSetFlags(0x0106, 0x0020)

    @scena.Lambda('lambda_1543')
    def lambda_1543():
        OP_99(0x0106, 0x00, 0x04, 2000)

        ExitThread()

    DispatchAsync(0x0106, 0x0002, lambda_1543)

    @scena.Lambda('lambda_1553')
    def lambda_1553():
        ChrJumpTo(0x0106, -47714, -500, -19390, 1800, 4000)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_1553)

    @scena.Lambda('lambda_1571')
    def lambda_1571():
        ChrJumpTo(0x000F, -49110, -500, -18460, 2000, 7000)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_1571)

    @scena.Lambda('lambda_158F')
    def lambda_158F():
        CameraSetDistance(2600, 1500)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_158F)

    ExecExpressionWithValue(
        0x000F,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x000F, 0x0020)
    Sleep(350)

    ChrSetFlags(0x000F, 0x0004)
    TerminateThread(0x000F, 0xFF)
    OP_4A(0x0106, 1)
    Sleep(100)

    OP_4B(0x0106, 1)
    PlayEffect(0x09, 0xFF, 0x00FF, -47725, 3000, -19196, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(505, 0x00, 0x64)

    @scena.Lambda('lambda_1604')
    def lambda_1604():
        OP_99(0x0106, 0x04, 0x07, 2000)

        ExitThread()

    DispatchAsync(0x0106, 0x0002, lambda_1604)

    ChrSetChipByIndex(0x000F, 5)
    TerminateThread(0x000F, 0xFF)
    ChrTurnDirection(0x000F, 0x0106, 0)

    ExecExpressionWithValue(
        0x000F,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x000F, 0x0020)
    ChrMoveTo(0x000F, -46630, -500, -21070, 20000, 0x00)
    ChrSetChipByIndex(0x000E, 2)
    ChrSetChipByIndex(0x0010, 2)
    ChrSetChipByIndex(0x000A, 2)

    @scena.Lambda('lambda_1657')
    def lambda_1657():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1657)

    @scena.Lambda('lambda_166D')
    def lambda_166D():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_166D)

    @scena.Lambda('lambda_1683')
    def lambda_1683():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1683)

    PlayEffect(0x12, 0xFF, 0x00FF, -46630, -500, -21070, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    ChrClearFlags(0x000F, 0x0004)

    @scena.Lambda('lambda_16D3')
    def lambda_16D3():
        ChrJumpTo(0x000F, -46040, -500, -22170, 2000, 10000)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_16D3)

    ChrSetRGBAMask(0x000F, 255, 255, 255, 0, 600)
    Sleep(50)

    ChrSetChipByIndex(0x000B, 2)

    @scena.Lambda('lambda_1706')
    def lambda_1706():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1706)

    Sleep(100)

    ChrSetChipByIndex(0x000D, 2)

    @scena.Lambda('lambda_1726')
    def lambda_1726():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1726)

    Sleep(100)

    ChrSetChipByIndex(0x000C, 2)

    @scena.Lambda('lambda_1746')
    def lambda_1746():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1746)

    OP_99(0x0106, 0x00, 0x03, 2000)
    ChrJumpTo(0x0106, -49320, -500, -18950, 1000, 4000)
    ChrSetChipByIndex(0x0106, 7)
    ChrClearFlags(0x0106, 0x0020)

    @scena.Lambda('lambda_1786')
    def lambda_1786():
        OP_6C(340000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1786)

    CameraMove(-50734, 0, -10950, 2000)

    ChrTalk(
        0x0101,
        (
            '#0010040262V#004F#1P好、好厉害……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040263V#012F看来他比传说中还要厉害呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(1000)
    CameraMove(-49960, -600, -18520, 0)

    @scena.Lambda('lambda_1818')
    def lambda_1818():
        CameraMove(-49070, -600, -19300, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1818)

    ChrSetPos(0x0013, -46890, -50, -15230, 180)
    OP_0D()

    @scena.Lambda('lambda_1842')
    def lambda_1842():
        ChrTurnDirection(0x00FE, 0x0106, 0)
        Yield()

        Jump('lambda_1842')

    DispatchAsync2(0x000A, 0x0002, lambda_1842)

    @scena.Lambda('lambda_1853')
    def lambda_1853():
        ChrTurnDirection(0x00FE, 0x0106, 0)
        Yield()

        Jump('lambda_1853')

    DispatchAsync2(0x000B, 0x0002, lambda_1853)

    @scena.Lambda('lambda_1864')
    def lambda_1864():
        ChrTurnDirection(0x00FE, 0x0106, 0)
        Yield()

        Jump('lambda_1864')

    DispatchAsync2(0x000C, 0x0002, lambda_1864)

    @scena.Lambda('lambda_1875')
    def lambda_1875():
        ChrTurnDirection(0x00FE, 0x0106, 0)
        Yield()

        Jump('lambda_1875')

    DispatchAsync2(0x000D, 0x0002, lambda_1875)

    @scena.Lambda('lambda_1886')
    def lambda_1886():
        ChrTurnDirection(0x00FE, 0x0106, 0)
        Yield()

        Jump('lambda_1886')

    DispatchAsync2(0x000E, 0x0002, lambda_1886)

    @scena.Lambda('lambda_1897')
    def lambda_1897():
        ChrTurnDirection(0x00FE, 0x0106, 0)
        Yield()

        Jump('lambda_1897')

    DispatchAsync2(0x0010, 0x0002, lambda_1897)

    ChrSetFlags(0x0106, 0x0040)
    ChrSetChipByIndex(0x0106, 8)

    @scena.Lambda('lambda_18B2')
    def lambda_18B2():
        ChrWalkTo(0x00FE, -50300, -500, -20250, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_18B2)

    @scena.Lambda('lambda_18CD')
    def lambda_18CD():
        ChrJumpTo(0x00FE, -52760, -500, -19870, 1000, 4000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_18CD)

    Sleep(100)

    @scena.Lambda('lambda_18F0')
    def lambda_18F0():
        ChrMoveTo(0x00FE, -51850, -500, -21970, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_18F0)

    @scena.Lambda('lambda_190B')
    def lambda_190B():
        ChrJumpTo(0x00FE, -51500, 0, -15800, 1000, 4000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_190B)

    Sleep(100)

    @scena.Lambda('lambda_192E')
    def lambda_192E():
        ChrJumpTo(0x00FE, -48860, -500, -22500, 1000, 4000)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_192E)

    @scena.Lambda('lambda_194C')
    def lambda_194C():
        ChrJumpTo(0x00FE, -47440, -500, -19540, 1000, 4000)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_194C)

    @scena.Lambda('lambda_196A')
    def lambda_196A():
        ChrMoveTo(0x00FE, -47610, -500, -20760, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_196A)

    WaitForThreadExit(0x0106, 0x0001)
    ChrSetChipByIndex(0x0106, 7)
    CreateThread(0x0106, 0x01, 0x00, func_02_332)
    WaitForThreadExit(0x000C, 0x0001)
    WaitForThreadExit(0x000D, 0x0001)
    WaitForThreadExit(0x000E, 0x0001)
    WaitForThreadExit(0x0010, 0x0001)
    ChrTurnDirection(0x0106, 0x0010, 600)
    ChrSetFlags(0x0106, 0x0040)
    ChrSetChipByIndex(0x0106, 8)

    @scena.Lambda('lambda_19BB')
    def lambda_19BB():
        ChrJumpTo(0x00FE, -48380, -600, -20050, 1000, 5000)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_19BB)

    @scena.Lambda('lambda_19D9')
    def lambda_19D9():
        ChrJumpTo(0x00FE, -46260, -500, -19390, 1000, 4000)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_19D9)

    Sleep(100)

    @scena.Lambda('lambda_19FC')
    def lambda_19FC():
        ChrMoveTo(0x00FE, -45460, -500, -21200, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_19FC)

    @scena.Lambda('lambda_1A17')
    def lambda_1A17():
        ChrJumpTo(0x00FE, -51590, -300, -18340, 1000, 7000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1A17)

    @scena.Lambda('lambda_1A35')
    def lambda_1A35():
        ChrMoveTo(0x00FE, -50600, -500, -20790, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1A35)

    WaitForThreadExit(0x0106, 0x0001)
    ChrSetChipByIndex(0x0106, 7)
    WaitForThreadExit(0x000C, 0x0001)
    WaitForThreadExit(0x000D, 0x0001)
    WaitForThreadExit(0x000E, 0x0001)
    WaitForThreadExit(0x0010, 0x0001)

    @scena.Lambda('lambda_1A6E')
    def lambda_1A6E():
        OP_92(0x00FE, 0x0106, 3000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1A6E)

    @scena.Lambda('lambda_1A83')
    def lambda_1A83():
        OP_92(0x00FE, 0x0106, 3000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1A83)

    @scena.Lambda('lambda_1A98')
    def lambda_1A98():
        ChrJumpTo(0x00FE, -49020, -300, -16110, 1000, 7000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1A98)

    Sleep(150)

    @scena.Lambda('lambda_1ABB')
    def lambda_1ABB():
        OP_92(0x00FE, 0x0106, 3500, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1ABB)

    Sleep(150)

    @scena.Lambda('lambda_1AD5')
    def lambda_1AD5():
        OP_92(0x00FE, 0x0106, 3500, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1AD5)

    Sleep(150)

    @scena.Lambda('lambda_1AEF')
    def lambda_1AEF():
        OP_92(0x00FE, 0x0106, 3000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_1AEF)

    WaitForThreadExit(0x000A, 0x0001)
    WaitForThreadExit(0x000B, 0x0001)
    WaitForThreadExit(0x000C, 0x0001)
    WaitForThreadExit(0x000D, 0x0001)
    WaitForThreadExit(0x000E, 0x0001)
    WaitForThreadExit(0x0010, 0x0001)

    @scena.Lambda('lambda_1B22')
    def lambda_1B22():
        OP_94(0x01, 0x00FE, 0x0064, 0x000001F4, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1B22)

    Sleep(200)

    @scena.Lambda('lambda_1B3D')
    def lambda_1B3D():
        OP_94(0x01, 0x00FE, 0x0064, 0x000001F4, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1B3D)

    Sleep(100)

    @scena.Lambda('lambda_1B58')
    def lambda_1B58():
        OP_94(0x01, 0x00FE, 0x0064, 0x000001F4, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1B58)

    @scena.Lambda('lambda_1B6E')
    def lambda_1B6E():
        OP_94(0x01, 0x00FE, 0x0064, 0x000001F4, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1B6E)

    Sleep(100)

    @scena.Lambda('lambda_1B89')
    def lambda_1B89():
        OP_94(0x01, 0x00FE, 0x0064, 0x000001F4, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1B89)

    Sleep(200)

    @scena.Lambda('lambda_1BA4')
    def lambda_1BA4():
        OP_94(0x01, 0x00FE, 0x0064, 0x000001F4, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_1BA4)

    Sleep(100)

    @scena.Lambda('lambda_1BBF')
    def lambda_1BBF():
        OP_94(0x01, 0x00FE, 0x005A, 0x000001F4, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1BBF)

    @scena.Lambda('lambda_1BD5')
    def lambda_1BD5():
        OP_94(0x01, 0x00FE, 0x005A, 0x000001F4, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1BD5)

    Sleep(100)

    @scena.Lambda('lambda_1BF0')
    def lambda_1BF0():
        OP_94(0x01, 0x00FE, 0x005A, 0x000001F4, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1BF0)

    Sleep(200)

    @scena.Lambda('lambda_1C0B')
    def lambda_1C0B():
        OP_94(0x01, 0x00FE, 0x005A, 0x000001F4, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1C0B)

    Sleep(100)

    @scena.Lambda('lambda_1C26')
    def lambda_1C26():
        OP_94(0x01, 0x00FE, 0x005A, 0x000001F4, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1C26)

    Sleep(200)

    @scena.Lambda('lambda_1C41')
    def lambda_1C41():
        OP_94(0x01, 0x00FE, 0x005A, 0x000001F4, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_1C41)

    ChrSetDirection(0x0106, 135, 400)

    ChrTalk(
        0x0106,
        (
            '#0050040264V#051F哈～想夹击我吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050040265V一群光使蛮劲的野狗，\n',
            '偶尔也会动动脑筋嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040266V……我们来帮忙了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0101, 10)
    ChrSetChipByIndex(0x0102, 12)
    ChrClearFlags(0x0101, 0x1000)
    ChrClearFlags(0x0102, 0x1000)

    @scena.Lambda('lambda_1CF4')
    def lambda_1CF4():
        ChrWalkTo(0x0101, -48090, -300, -16590, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1CF4)

    Sleep(300)

    @scena.Lambda('lambda_1D14')
    def lambda_1D14():
        ChrWalkTo(0x0102, -48090, -300, -16590, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1D14)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_1D34')
    def lambda_1D34():
        ChrJumpTo(0x0101, -49250, -640, -19500, 1000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1D34)

    WaitForThreadExit(0x0102, 0x0001)

    @scena.Lambda('lambda_1D57')
    def lambda_1D57():
        ChrJumpTo(0x0102, -48270, -500, -18950, 1000, 10000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1D57)

    @scena.Lambda('lambda_1D75')
    def lambda_1D75():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1D75)

    Sleep(100)

    @scena.Lambda('lambda_1D90')
    def lambda_1D90():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1D90)

    @scena.Lambda('lambda_1DA6')
    def lambda_1DA6():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1DA6)

    WaitForThreadExit(0x0101, 0x0001)
    PlaySE(164, 0x00, 0x64)

    @scena.Lambda('lambda_1DC6')
    def lambda_1DC6():
        ChrSetDirection(0x00FE, 315, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1DC6)

    Sleep(50)

    @scena.Lambda('lambda_1DD9')
    def lambda_1DD9():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1DD9)

    @scena.Lambda('lambda_1DEF')
    def lambda_1DEF():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1DEF)

    Sleep(100)

    @scena.Lambda('lambda_1E0A')
    def lambda_1E0A():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_1E0A)

    WaitForThreadExit(0x0102, 0x0001)
    PlaySE(164, 0x00, 0x64)

    @scena.Lambda('lambda_1E2A')
    def lambda_1E2A():
        ChrSetDirection(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_1E2A)

    OP_62(0x0106, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0106,
        (
            '#0050040267V#054F喂！谁叫你们过来的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040268V#006F嘿嘿～～\n',
            '我们想过来就过来的啦☆',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040269V#012F我们不会给你添麻烦的，\n',
            '让我们和你一起并肩作战吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050040270V#053F哼，随你们吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050040271V#054F不过你们要注意了，\n',
            '我的『重剑』可是不长眼的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1F64')
    def lambda_1F64():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000BB8, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1F64)

    @scena.Lambda('lambda_1F7A')
    def lambda_1F7A():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000BB8, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1F7A)

    Sleep(100)

    @scena.Lambda('lambda_1F95')
    def lambda_1F95():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000BB8, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1F95)

    Sleep(50)

    @scena.Lambda('lambda_1FB0')
    def lambda_1FB0():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000BB8, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1FB0)

    @scena.Lambda('lambda_1FC6')
    def lambda_1FC6():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000BB8, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1FC6)

    Sleep(100)

    @scena.Lambda('lambda_1FE1')
    def lambda_1FE1():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000BB8, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_1FE1)

    Sleep(200)

    Battle(0x00000396, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_200F'),
        (-1, 'loc_2012'),
    )

    def _loc_200F(): pass

    label('loc_200F')

    OP_B4(0x00)

    Return()

    def _loc_2012(): pass

    label('loc_2012')

    EventBegin(0x00)
    FadeIn(1000, 0)
    ChrSetStatus(0x0005, 0x00, 24)
    EquipCmd(0x05, 0x00F3)
    EquipCmd(0x05, 0x0111)
    CameraSetDistance(3000, 0)
    ChrSetPos(0x0101, -49970, -650, -18800, 315)
    ChrSetPos(0x0102, -47880, -430, -19000, 45)
    ChrSetPos(0x0106, -48850, -540, -20000, 180)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0106, 0xFF)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x0106, 15)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x0010, 0x0080)

    ChrTalk(
        0x0101,
        (
            '#0010040272V#501F呼……\n',
            '终于击败它们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040273V#012F嗯，它们数目众多，\n',
            '而且都是很难缠的魔兽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050040274V#050F……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050040275V#053F哼……\n',
            '看来你们也没有想象中那么没用。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050040276V毕竟是继承了大叔的真传，\n',
            '这点水平还是应该有的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_21BF')
    def lambda_21BF():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_21BF)

    ChrTurnDirection(0x0101, 0x0106, 400)

    ChrTalk(
        0x0101,
        (
            '#0010040277V#004F啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0106, 0, 400)

    ChrTalk(
        0x0106,
        (
            '#0050040278V#050F别搞错了。\n',
            '你们始终还是新人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050040279V离正游击士还差得远啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0011, 6)
    ChrSetChipByIndex(0x0012, 14)
    ChrSetPos(0x0011, -50620, 450, -7940, 0)
    ChrSetPos(0x0012, -49390, 450, -8010, 0)
    ChrClearFlags(0x0011, 0x0020)
    ChrClearFlags(0x0012, 0x0020)

    ChrTalk(
        0x0011,
        (
            '#1430040280V喂——！\n',
            '你们那边没事吧！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_22B1')
    def lambda_22B1():
        CameraMove(-49756, -300, -16490, 2000)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_22B1)

    @scena.Lambda('lambda_22C9')
    def lambda_22C9():
        ChrWalkTo(0x00FE, -50310, 0, -14800, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_22C9)

    Sleep(500)

    @scena.Lambda('lambda_22E9')
    def lambda_22E9():
        ChrWalkTo(0x00FE, -49250, 0, -14300, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_22E9)

    @scena.Lambda('lambda_2304')
    def lambda_2304():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2304)

    @scena.Lambda('lambda_2312')
    def lambda_2312():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2312)

    @scena.Lambda('lambda_2320')
    def lambda_2320():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_2320)

    WaitForThreadExit(0x0011, 0x0001)

    ChrTalk(
        0x0106,
        (
            '#0050040281V#050F#3P啊，没问题。\n',
            '把它们杀个片甲不留了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050040282V刚才那个晕倒的士兵怎样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#1430040283V还好没什么大碍。\n',
            '这次幸好有你在这里帮了大忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#1440040284V真不愧是『重剑阿加特』啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050040285V#053F#3P也没什么大不了的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050040286V#053F而且……\n',
            '这两个小鬼也帮了我不少忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#1440040287V是这样啊……\n',
            '小姑娘，太谢谢你们啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040288V#004F啊，嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#1430040289V为了安全起见，\n',
            '我们还要继续在这周围巡逻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#1430040290V你们大概都有点累了，\n',
            '回到休息室好好睡一觉吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050040291V#051F啊啊，你们也小心点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0011, 45, 400)

    @scena.Lambda('lambda_2567')
    def lambda_2567():
        ChrWalkTo(0x00FE, -50080, 450, -7500, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_2567)

    Sleep(500)

    ChrSetDirection(0x0012, 45, 400)

    @scena.Lambda('lambda_258E')
    def lambda_258E():
        ChrWalkTo(0x00FE, -50080, 450, -7500, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_258E)

    WaitForThreadExit(0x0011, 0x0001)
    ChrSetFlags(0x0011, 0x0080)
    WaitForThreadExit(0x0012, 0x0001)
    ChrSetFlags(0x0012, 0x0080)

    @scena.Lambda('lambda_25BD')
    def lambda_25BD():
        ChrTurnDirection(0x00FE, 0x0106, 400)
        Yield()

        Jump('lambda_25BD')

    DispatchAsync2(0x0101, 0x0001, lambda_25BD)

    @scena.Lambda('lambda_25CE')
    def lambda_25CE():
        ChrTurnDirection(0x00FE, 0x0106, 400)
        Yield()

        Jump('lambda_25CE')

    DispatchAsync2(0x0102, 0x0001, lambda_25CE)

    CameraMove(-49340, -600, -17500, 1000)

    ChrTalk(
        0x0106,
        (
            '#0050040292V#050F我要回去接着睡了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050040293V危险已经排除了，\n',
            '你们也快点回去睡觉吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0102, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    ChrWalkTo(0x0106, -50080, 450, -7500, 3000, 0x00)
    ChrSetFlags(0x0106, 0x0080)
    OP_63(0x0101)
    OP_63(0x0102)
    TerminateThread(0x0101, 0x01)
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010040294V#004F怎、怎么回事？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040295V那个刀子嘴\n',
            '这次竟然表扬我们呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0102, 0x01)
    ChrTurnDirection(0x0102, 0x0101, 300)

    ChrTalk(
        0x0102,
        (
            '#0020040296V#010F也许，他或多或少\n',
            '开始承认我们两个的能力了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040297V其实他也不是那种不近人情的人，\n',
            '只不过是性格比较直率而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040298V#007F呼……\n',
            '其实是率直过头了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040299V#006F……不过话说回来，\n',
            '那家伙也有相当可爱的一面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)
    FadeOut(1500, 0, -1)
    OP_0D()
    OP_21()
    PlaySE(13, 0x00, 0x64)
    MapSetFlags(0x00100000)
    Sleep(3000)

    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T1310._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0005 offset: 0x281D
@scena.Code('func_05_281D')
def func_05_281D():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2A66',
    )

    OP_93(0x0009, 0x000A, 600, 5000, 0x00)
    OP_94(0x01, 0x000A, 0x00B4, 0x000003E8, 0x00001388, 0x00)

    @scena.Lambda('lambda_2849')
    def lambda_2849():
        ChrMoveTo(0x00FE, -45600, 0, 14320, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_2849)

    @scena.Lambda('lambda_2864')
    def lambda_2864():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_2864)

    PlaySE(163, 0x00, 0x64)
    ChrJumpTo(0x000A, -47500, 0, 13630, 2000, 6000)
    ChrTurnDirection(0x000A, 0x0009, 0)
    ChrTurnDirection(0x0009, 0x000A, 800)
    Sleep(1000)

    @scena.Lambda('lambda_28A1')
    def lambda_28A1():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_28A1)

    @scena.Lambda('lambda_28B7')
    def lambda_28B7():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x000005DC, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_28B7)

    WaitForThreadExit(0x0009, 0x0002)
    WaitForThreadExit(0x000A, 0x0002)
    Sleep(700)

    ChrSetChipByIndex(0x000A, 2)

    @scena.Lambda('lambda_28E1')
    def lambda_28E1():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000640, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_28E1)

    @scena.Lambda('lambda_28F7')
    def lambda_28F7():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000640, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_28F7)

    WaitForThreadExit(0x0009, 0x0002)
    WaitForThreadExit(0x000A, 0x0002)
    PlaySE(555, 0x00, 0x64)
    ChrSetChipByIndex(0x000A, 1)

    @scena.Lambda('lambda_2921')
    def lambda_2921():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x0000012C, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_2921)

    @scena.Lambda('lambda_2937')
    def lambda_2937():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x0000012C, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_2937)

    Sleep(600)

    @scena.Lambda('lambda_2952')
    def lambda_2952():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x0000012C, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_2952)

    @scena.Lambda('lambda_2968')
    def lambda_2968():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x0000012C, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_2968)

    Sleep(200)

    @scena.Lambda('lambda_2983')
    def lambda_2983():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x0000012C, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_2983)

    @scena.Lambda('lambda_2999')
    def lambda_2999():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x0000012C, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_2999)

    Sleep(200)

    @scena.Lambda('lambda_29B4')
    def lambda_29B4():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x0000012C, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_29B4)

    @scena.Lambda('lambda_29CA')
    def lambda_29CA():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x0000012C, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_29CA)

    Sleep(200)

    @scena.Lambda('lambda_29E5')
    def lambda_29E5():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x0000012C, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_29E5)

    @scena.Lambda('lambda_29FB')
    def lambda_29FB():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x0000012C, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_29FB)

    Sleep(200)

    @scena.Lambda('lambda_2A16')
    def lambda_2A16():
        ChrMoveTo(0x00FE, -47500, 0, 13630, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_2A16)

    @scena.Lambda('lambda_2A31')
    def lambda_2A31():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_2A31)

    PlaySE(163, 0x00, 0x64)
    ChrJumpTo(0x000A, -45600, 0, 14320, 2000, 6000)
    ChrTurnDirection(0x000A, 0x0009, 0)
    ChrTurnDirection(0x0009, 0x000A, 800)

    Jump('func_05_281D')

    def _loc_2A66(): pass

    label('loc_2A66')

    Return()

# id: 0x0006 offset: 0x2A67
@scena.Code('func_06_2A67')
def func_06_2A67():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2D7B',
    )

    ChrSetFlags(0x0011, 0x0020)

    ExecExpressionWithValue(
        0x0011,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0011, 19)

    @scena.Lambda('lambda_2A8B')
    def lambda_2A8B():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x0000012C, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_2A8B)

    @scena.Lambda('lambda_2AA1')
    def lambda_2AA1():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x0000012C, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_2AA1)

    Sleep(200)

    @scena.Lambda('lambda_2ABC')
    def lambda_2ABC():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_2ABC)

    @scena.Lambda('lambda_2AD2')
    def lambda_2AD2():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_2AD2)

    Sleep(200)

    @scena.Lambda('lambda_2AED')
    def lambda_2AED():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x0000012C, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_2AED)

    @scena.Lambda('lambda_2B03')
    def lambda_2B03():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x0000012C, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_2B03)

    Sleep(200)

    @scena.Lambda('lambda_2B1E')
    def lambda_2B1E():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x0000012C, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_2B1E)

    @scena.Lambda('lambda_2B34')
    def lambda_2B34():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x0000012C, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_2B34)

    Sleep(200)

    @scena.Lambda('lambda_2B4F')
    def lambda_2B4F():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x00000190, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_2B4F)

    @scena.Lambda('lambda_2B65')
    def lambda_2B65():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x00000190, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_2B65)

    Sleep(200)

    @scena.Lambda('lambda_2B80')
    def lambda_2B80():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x000000C8, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_2B80)

    @scena.Lambda('lambda_2B96')
    def lambda_2B96():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x000000C8, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_2B96)

    Sleep(200)

    @scena.Lambda('lambda_2BB1')
    def lambda_2BB1():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_2BB1)

    @scena.Lambda('lambda_2BC7')
    def lambda_2BC7():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_2BC7)

    Sleep(500)

    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    ChrSetChipByIndex(0x000F, 2)

    @scena.Lambda('lambda_2BEA')
    def lambda_2BEA():
        OP_94(0x01, 0x00FE, 0x0000, 0x000005DC, 0x000009C4, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_2BEA)

    Sleep(500)

    WaitForThreadExit(0x000F, 0x0002)

    @scena.Lambda('lambda_2C0A')
    def lambda_2C0A():
        ChrJumpTo(0x00FE, -45180, 0, 17190, 1000, 6000)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_2C0A)

    TerminateThread(0x000F, 0x01)
    TerminateThread(0x000B, 0x01)
    OP_99(0x0011, 0x01, 0x03, 3000)
    ChrSetChipByIndex(0x000B, 5)

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x000B, 0x0020)
    PlaySE(501, 0x00, 0x64)

    @scena.Lambda('lambda_2C53')
    def lambda_2C53():
        OP_99(0x0011, 0x03, 0x07, 3000)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_2C53)

    @scena.Lambda('lambda_2C63')
    def lambda_2C63():
        ChrMoveTo(0x00FE, -48130, 0, 14880, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_2C63)

    @scena.Lambda('lambda_2C7E')
    def lambda_2C7E():
        ChrMoveTo(0x00FE, -44730, 0, 19520, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_2C7E)

    WaitForThreadExit(0x000F, 0x0002)

    @scena.Lambda('lambda_2C9E')
    def lambda_2C9E():
        ChrJumpTo(0x00FE, -47500, 0, 15620, 1000, 6000)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_2C9E)

    WaitForThreadExit(0x000B, 0x0002)
    ChrSetChipByIndex(0x000B, 1)
    WaitForThreadExit(0x000F, 0x0002)
    ChrSetChipByIndex(0x000F, 1)
    ChrSetPos(0x000B, -47500, 0, 15620, 225)
    ChrSetPos(0x000F, -44730, 0, 19520, 225)

    @scena.Lambda('lambda_2CF2')
    def lambda_2CF2():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000001F4, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_2CF2)

    ExecExpressionWithValue(
        0x0011,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0011, 19)
    OP_94(0x01, 0x0011, 0x00B4, 0x000001F4, 0x00001770, 0x00)

    ExecExpressionWithValue(
        0x0011,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0011, 17)
    CreateThread(0x000B, 0x01, 0x00, func_02_332)
    CreateThread(0x000F, 0x01, 0x00, func_02_332)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    CreateThread(0x0011, 0x02, 0x00, func_02_332)
    Sleep(500)

    Sleep(1000)

    @scena.Lambda('lambda_2D59')
    def lambda_2D59():
        OP_94(0x01, 0x00FE, 0x0000, 0x000001F4, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_2D59)

    OP_94(0x01, 0x0011, 0x0000, 0x000001F4, 0x00000FA0, 0x00)

    Jump('func_06_2A67')

    def _loc_2D7B(): pass

    label('loc_2D7B')

    Return()

# id: 0x0007 offset: 0x2D7C
@scena.Code('func_07_2D7C')
def func_07_2D7C():
    ChrSetFlags(0x000C, 0x0040)
    ChrSetFlags(0x000D, 0x0040)
    ChrSetFlags(0x000E, 0x0040)
    ChrSetFlags(0x0012, 0x0040)

    @scena.Lambda('lambda_2D96')
    def lambda_2D96():
        ChrTurnDirection(0x00FE, 0x000E, 0)
        Yield()

        Jump('lambda_2D96')

    DispatchAsync2(0x0008, 0x0000, lambda_2D96)

    @scena.Lambda('lambda_2DA7')
    def lambda_2DA7():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_2DA7')

    DispatchAsync2(0x000E, 0x0000, lambda_2DA7)

    def _loc_2DB2(): pass

    label('loc_2DB2')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3129',
    )

    PlaySE(551, 0x00, 0x64)

    @scena.Lambda('lambda_2DC6')
    def lambda_2DC6():
        OP_93(0x00FE, 0x0008, 600, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_2DC6)

    @scena.Lambda('lambda_2DDB')
    def lambda_2DDB():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_2DDB)

    ChrSetChipByIndex(0x000D, 2)
    OP_93(0x000D, 0x0012, 600, 6000, 0x00)
    ChrSetChipByIndex(0x000D, 1)
    OP_94(0x01, 0x0012, 0x00B4, 0x000001F4, 0x00001388, 0x00)
    Sleep(200)

    OP_94(0x01, 0x0012, 0x0000, 0x000001F4, 0x00001388, 0x00)

    @scena.Lambda('lambda_2E2C')
    def lambda_2E2C():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x0000012C, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2E2C)

    @scena.Lambda('lambda_2E42')
    def lambda_2E42():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x0000012C, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_2E42)

    @scena.Lambda('lambda_2E58')
    def lambda_2E58():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_2E58)

    @scena.Lambda('lambda_2E6E')
    def lambda_2E6E():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_2E6E)

    Sleep(500)

    @scena.Lambda('lambda_2E89')
    def lambda_2E89():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_2E89)

    @scena.Lambda('lambda_2E9F')
    def lambda_2E9F():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_2E9F)

    Sleep(500)

    @scena.Lambda('lambda_2EBA')
    def lambda_2EBA():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_2EBA)

    @scena.Lambda('lambda_2ED0')
    def lambda_2ED0():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_2ED0)

    Sleep(500)

    TerminateThread(0x0008, 0x02)

    @scena.Lambda('lambda_2EEF')
    def lambda_2EEF():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_2EEF)

    PlaySE(203, 0x00, 0x64)
    ChrJumpTo(0x0008, -50400, 0, 16600, 600, 6000)
    WaitForThreadExit(0x000C, 0x0002)

    @scena.Lambda('lambda_2F26')
    def lambda_2F26():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000007D0, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_2F26)

    @scena.Lambda('lambda_2F3C')
    def lambda_2F3C():
        OP_92(0x00FE, 0x0008, 300, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_2F3C)

    Sleep(150)

    ChrJumpTo(0x0008, -52100, 0, 16950, 1000, 6000)
    PlaySE(203, 0x00, 0x64)

    @scena.Lambda('lambda_2F72')
    def lambda_2F72():
        ChrTurnDirection(0x00FE, 0x000E, 800)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2F72)

    ChrTurnDirection(0x000E, 0x0008, 800)
    OP_92(0x0008, 0x000E, 600, 5000, 0x00)
    PlaySE(551, 0x00, 0x64)
    OP_94(0x01, 0x000E, 0x00B4, 0x000003E8, 0x00001388, 0x00)
    WaitForThreadExit(0x0008, 0x0002)
    WaitForThreadExit(0x000E, 0x0002)

    @scena.Lambda('lambda_2FB3')
    def lambda_2FB3():
        ChrMoveTo(0x00FE, -52080, 0, 15480, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2FB3)

    @scena.Lambda('lambda_2FCE')
    def lambda_2FCE():
        ChrWalkTo(0x00FE, -51450, 0, 17000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_2FCE)

    @scena.Lambda('lambda_2FE9')
    def lambda_2FE9():
        OP_93(0x00FE, 0x0012, 2500, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_2FE9)

    ChrSetChipByIndex(0x000C, 2)
    Sleep(1700)

    @scena.Lambda('lambda_3008')
    def lambda_3008():
        OP_93(0x00FE, 0x0012, 600, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_3008)

    PlaySE(554, 0x00, 0x64)
    TerminateThread(0x000D, 0x01)
    ChrSetChipByIndex(0x000D, 5)

    ExecExpressionWithValue(
        0x000D,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x000D, 0x0020)

    @scena.Lambda('lambda_303B')
    def lambda_303B():
        ChrMoveTo(0x00FE, -47980, 0, 18190, 13000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_303B)

    @scena.Lambda('lambda_3056')
    def lambda_3056():
        OP_94(0x01, 0x00FE, 0x0000, 0x000001F4, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_3056)

    @scena.Lambda('lambda_306C')
    def lambda_306C():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x0000012C, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_306C)

    @scena.Lambda('lambda_3082')
    def lambda_3082():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x0000012C, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_3082)

    WaitForThreadExit(0x000D, 0x0002)
    ChrSetChipByIndex(0x000D, 1)
    ChrClearFlags(0x000D, 0x0020)
    CreateThread(0x000D, 0x01, 0x00, func_02_332)
    WaitForThreadExit(0x000C, 0x0002)
    PlaySE(555, 0x00, 0x64)
    TerminateThread(0x000C, 0x01)
    ChrSetChipByIndex(0x000C, 5)

    ExecExpressionWithValue(
        0x000C,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x000C, 0x0020)

    @scena.Lambda('lambda_30D1')
    def lambda_30D1():
        ChrMoveTo(0x00FE, -50380, 0, 18680, 13000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_30D1)

    @scena.Lambda('lambda_30EC')
    def lambda_30EC():
        ChrMoveTo(0x00FE, -49730, 0, 15340, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_30EC)

    WaitForThreadExit(0x000C, 0x0002)
    ChrSetChipByIndex(0x000C, 1)
    ChrClearFlags(0x000C, 0x0020)
    CreateThread(0x000C, 0x01, 0x00, func_02_332)
    WaitForThreadExit(0x0012, 0x0002)
    WaitForThreadExit(0x000C, 0x0002)
    WaitForThreadExit(0x000D, 0x0002)

    Jump('loc_2DB2')

    def _loc_3129(): pass

    label('loc_3129')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T1301_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1301   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '士兵卡多尔斯'),
    TXT(0x02, '士兵阿萨'),
    TXT(0x03, '魔兽'),
    TXT(0x04, '魔兽'),
    TXT(0x05, '魔兽'),
    TXT(0x06, '魔兽'),
    TXT(0x07, '魔兽'),
    TXT(0x08, '魔兽'),
    TXT(0x09, '魔兽'),
    TXT(0x0A, '赛尔斯特队长'),
    TXT(0x0B, '赛罗斯副长'),
    TXT(0x0C, '士兵迈奇'),
    TXT(0x0D, ''),
]

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

# id: 0xFFFF offset: 0x2FF0
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

# id: 0x10002 offset: 0x16A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
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

# id: 0x10003 offset: 0x2EA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x2EA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x2EA
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x2EA
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_2FD',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    SetMapFlags(0x10000000)
    Event(0, 0x0003)

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

    SetMapFlags(0x10000000)
    Event(0, 0x0004)

    Jump('loc_31E')

    def _loc_31E(): pass

    label('loc_31E')

    Return()

# id: 0x0001 offset: 0x31F
@scena.Code('Init')
def Init():
    OP_16(0x02, 4000, -178000, -125000, 196676)

    Return()

# id: 0x0002 offset: 0x332
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_347',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

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
    SetChrPos(0x0008, -50060, 0, 12640, 0)
    SetChrPos(0x0009, -50070, 450, 8800, 0)
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(-50200, 0, 9940, 0)
    CameraSetDistance(3000, 0)
    OP_6C(225000, 0)
    FadeIn(2000, 0)
    OP_0D()
    Sleep(1000)

    OP_70(0x0006, 100)
    OP_73(0x0006)
    SetChrFlags(0x0009, 0x0004)
    ChrWalkTo(0x0009, -49991, 450, 11235, 2000, 0x00)
    ClearChrFlags(0x0009, 0x0004)
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

    SetChrDirection(0x0009, 270, 400)
    Sleep(200)

    SetChrDirection(0x0009, 0, 400)
    SetChrDirection(0x0009, 90, 400)
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
    SetChrPos(0x000A, -46050, -600, 23150, 225)
    SetChrPos(0x000B, -43720, -300, 22970, 225)
    SetChrPos(0x000C, -45010, -400, 25300, 225)
    SetChrPos(0x000D, -44180, -500, 24380, 225)
    SetChrPos(0x000E, -43420, -500, 25190, 225)
    SetChrPos(0x000F, -42140, -600, 25680, 225)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
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

    SetChrDirection(0x0009, 45, 400)
    SetChrDirection(0x0008, 45, 400)
    PlayBGM(82)
    SetChrFlags(0x000A, 0x0040)
    SetChrFlags(0x000B, 0x0040)
    SetChrFlags(0x000C, 0x0040)
    SetChrFlags(0x000D, 0x0040)
    SetChrFlags(0x000E, 0x0040)
    SetChrFlags(0x000F, 0x0040)

    @scena.Lambda('lambda_06F4')
    def lambda_06F4():
        CameraSetDistance(3000, 2500)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_06F4)

    @scena.Lambda('lambda_0704')
    def lambda_0704():
        CameraMove(-47350, 0, 17130, 1700)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0704)

    Sleep(500)

    @scena.Lambda('lambda_0721')
    def lambda_0721():
        ChrWalkTo(0x00FE, -55460, 0, 16110, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0721)

    @scena.Lambda('lambda_073C')
    def lambda_073C():
        ChrWalkTo(0x00FE, -59640, 0, 16410, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_073C)

    @scena.Lambda('lambda_0757')
    def lambda_0757():
        ChrWalkTo(0x00FE, -56470, 0, 16880, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_0757)

    @scena.Lambda('lambda_0772')
    def lambda_0772():
        ChrWalkTo(0x00FE, -58070, 0, 17220, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0772)

    Sleep(100)

    @scena.Lambda('lambda_0792')
    def lambda_0792():
        ChrWalkTo(0x00FE, -59260, 0, 18260, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0792)

    Sleep(100)

    @scena.Lambda('lambda_07B2')
    def lambda_07B2():
        ChrWalkTo(0x00FE, -56460, 0, 18480, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_07B2)

    Sleep(1000)

    @scena.Lambda('lambda_07D2')
    def lambda_07D2():
        CameraMove(-49494, 0, 13760, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_07D2)

    @scena.Lambda('lambda_07EA')
    def lambda_07EA():
        ChrWalkTo(0x00FE, -46460, 0, 16110, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_07EA)

    Sleep(150)

    @scena.Lambda('lambda_080A')
    def lambda_080A():
        ChrWalkTo(0x00FE, -50640, 0, 16410, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_080A)

    Sleep(150)

    @scena.Lambda('lambda_082A')
    def lambda_082A():
        ChrWalkTo(0x00FE, -48050, 0, 17200, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_082A)

    Sleep(150)

    @scena.Lambda('lambda_084A')
    def lambda_084A():
        ChrWalkTo(0x00FE, -49070, 0, 17220, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_084A)

    Sleep(150)

    @scena.Lambda('lambda_086A')
    def lambda_086A():
        ChrWalkTo(0x00FE, -50140, 0, 18000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_086A)

    Sleep(150)

    @scena.Lambda('lambda_088A')
    def lambda_088A():
        ChrWalkTo(0x00FE, -46960, 0, 18000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_088A)

    WaitForThreadExit(0x000B, 0x0001)
    SetChrChipByIndex(0x000B, 1)
    CreateThread(0x000B, 0x01, 0x00, 0x0002)
    PlayEffect(0x12, 0xFF, 0x000B, 0, 100, 0, 0, 0, 0, 900, 900, 900, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_08EB')
    def lambda_08EB():
        OP_94(0x01, 0x00FE, 0x0000, 0x000002BC, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_08EB)

    WaitForThreadExit(0x000A, 0x0001)
    SetChrChipByIndex(0x000A, 1)
    CreateThread(0x000A, 0x01, 0x00, 0x0002)
    PlayEffect(0x12, 0xFF, 0x000A, 0, 100, 0, 0, 0, 0, 900, 900, 900, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_0947')
    def lambda_0947():
        OP_94(0x01, 0x00FE, 0x0000, 0x000002BC, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0947)

    WaitForThreadExit(0x000D, 0x0001)
    SetChrChipByIndex(0x000D, 1)
    CreateThread(0x000D, 0x01, 0x00, 0x0002)
    PlayEffect(0x12, 0xFF, 0x000D, 0, 100, 0, 0, 0, 0, 900, 900, 900, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_09A3')
    def lambda_09A3():
        OP_94(0x01, 0x00FE, 0x0000, 0x000002BC, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_09A3)

    WaitForThreadExit(0x000C, 0x0001)
    SetChrChipByIndex(0x000C, 1)
    CreateThread(0x000C, 0x01, 0x00, 0x0002)
    PlayEffect(0x12, 0xFF, 0x000C, 0, 100, 0, 0, 0, 0, 900, 900, 900, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_09FF')
    def lambda_09FF():
        OP_94(0x01, 0x00FE, 0x0000, 0x000002BC, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_09FF)

    WaitForThreadExit(0x000E, 0x0001)
    SetChrChipByIndex(0x000E, 1)
    CreateThread(0x000E, 0x01, 0x00, 0x0002)
    PlayEffect(0x12, 0xFF, 0x000E, 0, 100, 0, 0, 0, 0, 900, 900, 900, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_0A5B')
    def lambda_0A5B():
        OP_94(0x01, 0x00FE, 0x0000, 0x000002BC, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_0A5B)

    WaitForThreadExit(0x000F, 0x0001)
    SetChrChipByIndex(0x000F, 1)
    CreateThread(0x000F, 0x01, 0x00, 0x0002)
    PlayEffect(0x12, 0xFF, 0x000F, 0, 100, 0, 0, 0, 0, 900, 900, 900, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_0AB7')
    def lambda_0AB7():
        OP_94(0x01, 0x00FE, 0x0000, 0x000002BC, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_0AB7)

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
    SetMapFlags(0x02000000)
    NewScene('ED6_DT01/T1311._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0xB57
@scena.Code('func_04_B57')
def func_04_B57():
    FormationAddMember(0x05, 0xFF)
    ClearMapFlags(0x00000010)
    SetChrStatus(0x0005, 0x00, 22)
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
    SetChrStatus(0x0005, 0x05, 100)
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
    SetChrPos(0x0106, -49160, 450, 11070, 20)
    SetChrPos(0x0101, -50770, 450, 11200, 20)
    SetChrPos(0x0102, -50340, 450, 10410, 20)
    SetChrPos(0x0008, -52080, 0, 15480, 315)
    SetChrPos(0x0009, -47500, 0, 13630, 90)
    SetChrPos(0x0012, -49730, 0, 15340, 0)
    SetChrPos(0x0011, -48130, 0, 14880, 45)
    SetChrChipByIndex(0x0008, 20)
    SetChrChipByIndex(0x0009, 20)
    SetChrChipByIndex(0x0012, 20)
    SetChrChipByIndex(0x0011, 17)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    OP_4A(0x000A, 255)
    OP_4A(0x000B, 255)
    OP_4A(0x000C, 255)
    OP_4A(0x000D, 255)
    OP_4A(0x000E, 255)
    OP_4A(0x000F, 255)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    SetChrPos(0x000A, -45600, 0, 14320, 270)
    SetChrPos(0x000B, -47500, 0, 15620, 225)
    SetChrPos(0x000F, -44730, 0, 19520, 225)
    SetChrPos(0x000D, -47980, 0, 18190, 180)
    SetChrPos(0x000C, -50380, 0, 18680, 135)
    SetChrPos(0x000E, -51820, 0, 17000, 135)
    ChrTurnDirection(0x000A, 0x0009, 0)
    ChrTurnDirection(0x000B, 0x0011, 0)
    ChrTurnDirection(0x000F, 0x0011, 0)
    ChrTurnDirection(0x000D, 0x0012, 0)
    ChrTurnDirection(0x000C, 0x0012, 0)
    ChrTurnDirection(0x000E, 0x0008, 0)
    ChrTurnDirection(0x0012, 0x000D, 0)
    SetChrChipByIndex(0x000A, 1)
    SetChrChipByIndex(0x000B, 1)
    SetChrChipByIndex(0x000C, 1)
    SetChrChipByIndex(0x000D, 1)
    SetChrChipByIndex(0x000E, 1)
    SetChrChipByIndex(0x000F, 1)
    CreateThread(0x000A, 0x01, 0x00, 0x0002)
    CreateThread(0x000C, 0x01, 0x00, 0x0002)
    CreateThread(0x000D, 0x01, 0x00, 0x0002)
    CreateThread(0x000E, 0x01, 0x00, 0x0002)
    CreateThread(0x000F, 0x01, 0x00, 0x0002)
    SetChrFlags(0x0101, 0x1000)
    SetChrFlags(0x0102, 0x1000)
    SetChrChipByIndex(0x0106, 15)
    CreateThread(0x0011, 0x01, 0x00, 0x0006)
    CreateThread(0x0009, 0x01, 0x00, 0x0005)
    CreateThread(0x0012, 0x01, 0x00, 0x0007)
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
    SetChrFlags(0x0011, 0x0020)

    ExecExpressionWithValue(
        0x0011,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0011, 19)
    PlaySE(132, 0x00, 0x64)

    @scena.Lambda('lambda_0FB3')
    def lambda_0FB3():
        OP_99(0x0011, 0x00, 0x03, 2000)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_0FB3)

    OP_93(0x0011, 0x000B, 600, 7000, 0x00)

    @scena.Lambda('lambda_0FD1')
    def lambda_0FD1():
        OP_99(0x0011, 0x03, 0x07, 2000)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_0FD1)

    SetChrChipByIndex(0x000B, 5)
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

    SetChrFlags(0x000B, 0x0020)
    PlayEffect(0x09, 0xFF, 0x00FF, -47540, 1000, 15460, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_1036')
    def lambda_1036():
        OP_94(0x01, 0x000B, 0x00B4, 0x000007D0, 0x00002AF8, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1036)

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

    SetChrChipByIndex(0x0011, 17)
    ChrJumpTo(0x0011, -48130, 0, 14880, 1000, 5000)
    SetChrFlags(0x000B, 0x0040)

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

    @scena.Lambda('lambda_1106')
    def lambda_1106():
        ChrWalkTo(0x00FE, -47730, 0, 15510, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_1106)

    ExecExpressionWithValue(
        0x0011,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0011, 19)
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

    @scena.Lambda('lambda_118A')
    def lambda_118A():
        SetChrDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_118A)

    Sleep(300)

    @scena.Lambda('lambda_119D')
    def lambda_119D():
        SetChrDirection(0x00FE, 160, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_119D)

    @scena.Lambda('lambda_11AB')
    def lambda_11AB():
        SetChrDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_11AB)

    CameraMove(-49790, 450, 10030, 1000)

    ChrTalk(
        0x0106,
        (
            '#0050040257V#057F#1P……嘁！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x0106, 0x0004)
    ChrWalkTo(0x0106, -50070, 290, 9000, 7000, 0x00)
    ChrWalkTo(0x0106, -50310, 450, 6810, 7000, 0x00)
    ClearChrFlags(0x0106, 0x0004)
    SetChrFlags(0x0106, 0x0080)

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
    ClearChrFlags(0x0010, 0x0080)
    ChrSetRGBAMask(0x000B, 255, 255, 255, 255, 0)
    ClearChrFlags(0x000A, 0x0020)
    ClearChrFlags(0x000B, 0x0020)
    ClearChrFlags(0x000C, 0x0020)
    ClearChrFlags(0x000D, 0x0020)
    ClearChrFlags(0x000E, 0x0020)
    ClearChrFlags(0x000F, 0x0020)
    ClearChrFlags(0x0010, 0x0020)
    SetChrChipByIndex(0x000A, 1)
    SetChrChipByIndex(0x000B, 1)
    SetChrChipByIndex(0x000C, 1)
    SetChrChipByIndex(0x000D, 1)
    SetChrChipByIndex(0x000E, 1)
    SetChrChipByIndex(0x000F, 2)
    SetChrChipByIndex(0x0010, 1)
    SetChrPos(0x000A, -45460, -500, -20310, 315)
    SetChrPos(0x000B, -51540, -300, -17880, 90)
    SetChrPos(0x000D, -51890, -500, -20520, 45)
    SetChrPos(0x000C, -50260, -500, -20200, 45)
    SetChrPos(0x000E, -48980, -500, -20950, 0)
    SetChrPos(0x000F, -44270, -300, -18680, 270)
    SetChrPos(0x0010, -44460, 0, -17870, 225)
    CreateThread(0x000A, 0x01, 0x00, 0x0002)
    CreateThread(0x000B, 0x01, 0x00, 0x0002)
    CreateThread(0x000C, 0x01, 0x00, 0x0002)
    CreateThread(0x000D, 0x01, 0x00, 0x0002)
    CreateThread(0x000E, 0x01, 0x00, 0x0002)
    CreateThread(0x000F, 0x01, 0x00, 0x0002)
    CreateThread(0x0010, 0x01, 0x00, 0x0002)
    SetChrPos(0x0013, -49160, -600, -17710, 180)
    SetChrFlags(0x000F, 0x0040)
    ClearChrFlags(0x0106, 0x0080)
    SetChrPos(0x0106, -50596, 300, -9470, 0)
    SetChrPos(0x0101, -50644, 0, -9440, 180)
    SetChrPos(0x0102, -49430, 0, -9440, 180)
    SetChrFlags(0x0106, 0x1000)
    SetChrChipByIndex(0x0106, 8)

    @scena.Lambda('lambda_147E')
    def lambda_147E():
        OP_92(0x000F, 0x0013, 2300, 1300, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_147E)

    OP_0D()
    ChrWalkTo(0x0106, -49276, -500, -16530, 6000, 0x00)
    SetChrChipByIndex(0x0106, 9)
    PlaySE(163, 0x00, 0x64)
    SetChrFlags(0x0106, 0x0020)

    @scena.Lambda('lambda_14B7')
    def lambda_14B7():
        OP_99(0x0106, 0x00, 0x04, 2000)

        ExitThread()

    DispatchAsync(0x0106, 0x0002, lambda_14B7)

    @scena.Lambda('lambda_14C7')
    def lambda_14C7():
        ChrJumpTo(0x0106, -47714, -500, -19390, 1800, 4000)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_14C7)

    @scena.Lambda('lambda_14E5')
    def lambda_14E5():
        ChrJumpTo(0x000F, -49110, -500, -18460, 2000, 7000)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_14E5)

    @scena.Lambda('lambda_1503')
    def lambda_1503():
        CameraSetDistance(2600, 1500)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1503)

    ExecExpressionWithValue(
        0x000F,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrFlags(0x000F, 0x0020)
    Sleep(350)

    SetChrFlags(0x000F, 0x0004)
    TerminateThread(0x000F, 0xFF)
    OP_4A(0x0106, 1)
    Sleep(100)

    OP_4B(0x0106, 1)
    PlayEffect(0x09, 0xFF, 0x00FF, -47725, 3000, -19196, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(505, 0x00, 0x64)

    @scena.Lambda('lambda_1578')
    def lambda_1578():
        OP_99(0x0106, 0x04, 0x07, 2000)

        ExitThread()

    DispatchAsync(0x0106, 0x0002, lambda_1578)

    SetChrChipByIndex(0x000F, 5)
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

    SetChrFlags(0x000F, 0x0020)
    ChrMoveTo(0x000F, -46630, -500, -21070, 20000, 0x00)
    SetChrChipByIndex(0x000E, 2)
    SetChrChipByIndex(0x0010, 2)
    SetChrChipByIndex(0x000A, 2)

    @scena.Lambda('lambda_15CB')
    def lambda_15CB():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_15CB)

    @scena.Lambda('lambda_15E1')
    def lambda_15E1():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_15E1)

    @scena.Lambda('lambda_15F7')
    def lambda_15F7():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_15F7)

    PlayEffect(0x12, 0xFF, 0x00FF, -46630, -500, -21070, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    ClearChrFlags(0x000F, 0x0004)

    @scena.Lambda('lambda_1647')
    def lambda_1647():
        ChrJumpTo(0x000F, -46040, -500, -22170, 2000, 10000)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_1647)

    ChrSetRGBAMask(0x000F, 255, 255, 255, 0, 600)
    Sleep(50)

    SetChrChipByIndex(0x000B, 2)

    @scena.Lambda('lambda_167A')
    def lambda_167A():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_167A)

    Sleep(100)

    SetChrChipByIndex(0x000D, 2)

    @scena.Lambda('lambda_169A')
    def lambda_169A():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_169A)

    Sleep(100)

    SetChrChipByIndex(0x000C, 2)

    @scena.Lambda('lambda_16BA')
    def lambda_16BA():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_16BA)

    OP_99(0x0106, 0x00, 0x03, 2000)
    ChrJumpTo(0x0106, -49320, -500, -18950, 1000, 4000)
    SetChrChipByIndex(0x0106, 7)
    ClearChrFlags(0x0106, 0x0020)

    @scena.Lambda('lambda_16FA')
    def lambda_16FA():
        OP_6C(340000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_16FA)

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

    @scena.Lambda('lambda_1782')
    def lambda_1782():
        CameraMove(-49070, -600, -19300, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1782)

    SetChrPos(0x0013, -46890, -50, -15230, 180)
    OP_0D()

    @scena.Lambda('lambda_17AC')
    def lambda_17AC():
        ChrTurnDirection(0x00FE, 0x0106, 0)
        Yield()

        Jump('lambda_17AC')

    DispatchAsync2(0x000A, 0x0002, lambda_17AC)

    @scena.Lambda('lambda_17BD')
    def lambda_17BD():
        ChrTurnDirection(0x00FE, 0x0106, 0)
        Yield()

        Jump('lambda_17BD')

    DispatchAsync2(0x000B, 0x0002, lambda_17BD)

    @scena.Lambda('lambda_17CE')
    def lambda_17CE():
        ChrTurnDirection(0x00FE, 0x0106, 0)
        Yield()

        Jump('lambda_17CE')

    DispatchAsync2(0x000C, 0x0002, lambda_17CE)

    @scena.Lambda('lambda_17DF')
    def lambda_17DF():
        ChrTurnDirection(0x00FE, 0x0106, 0)
        Yield()

        Jump('lambda_17DF')

    DispatchAsync2(0x000D, 0x0002, lambda_17DF)

    @scena.Lambda('lambda_17F0')
    def lambda_17F0():
        ChrTurnDirection(0x00FE, 0x0106, 0)
        Yield()

        Jump('lambda_17F0')

    DispatchAsync2(0x000E, 0x0002, lambda_17F0)

    @scena.Lambda('lambda_1801')
    def lambda_1801():
        ChrTurnDirection(0x00FE, 0x0106, 0)
        Yield()

        Jump('lambda_1801')

    DispatchAsync2(0x0010, 0x0002, lambda_1801)

    SetChrFlags(0x0106, 0x0040)
    SetChrChipByIndex(0x0106, 8)

    @scena.Lambda('lambda_181C')
    def lambda_181C():
        ChrWalkTo(0x00FE, -50300, -500, -20250, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_181C)

    @scena.Lambda('lambda_1837')
    def lambda_1837():
        ChrJumpTo(0x00FE, -52760, -500, -19870, 1000, 4000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1837)

    Sleep(100)

    @scena.Lambda('lambda_185A')
    def lambda_185A():
        ChrMoveTo(0x00FE, -51850, -500, -21970, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_185A)

    @scena.Lambda('lambda_1875')
    def lambda_1875():
        ChrJumpTo(0x00FE, -51500, 0, -15800, 1000, 4000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1875)

    Sleep(100)

    @scena.Lambda('lambda_1898')
    def lambda_1898():
        ChrJumpTo(0x00FE, -48860, -500, -22500, 1000, 4000)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1898)

    @scena.Lambda('lambda_18B6')
    def lambda_18B6():
        ChrJumpTo(0x00FE, -47440, -500, -19540, 1000, 4000)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_18B6)

    @scena.Lambda('lambda_18D4')
    def lambda_18D4():
        ChrMoveTo(0x00FE, -47610, -500, -20760, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_18D4)

    WaitForThreadExit(0x0106, 0x0001)
    SetChrChipByIndex(0x0106, 7)
    CreateThread(0x0106, 0x01, 0x00, 0x0002)
    WaitForThreadExit(0x000C, 0x0001)
    WaitForThreadExit(0x000D, 0x0001)
    WaitForThreadExit(0x000E, 0x0001)
    WaitForThreadExit(0x0010, 0x0001)
    ChrTurnDirection(0x0106, 0x0010, 600)
    SetChrFlags(0x0106, 0x0040)
    SetChrChipByIndex(0x0106, 8)

    @scena.Lambda('lambda_1925')
    def lambda_1925():
        ChrJumpTo(0x00FE, -48380, -600, -20050, 1000, 5000)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_1925)

    @scena.Lambda('lambda_1943')
    def lambda_1943():
        ChrJumpTo(0x00FE, -46260, -500, -19390, 1000, 4000)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_1943)

    Sleep(100)

    @scena.Lambda('lambda_1966')
    def lambda_1966():
        ChrMoveTo(0x00FE, -45460, -500, -21200, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1966)

    @scena.Lambda('lambda_1981')
    def lambda_1981():
        ChrJumpTo(0x00FE, -51590, -300, -18340, 1000, 7000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1981)

    @scena.Lambda('lambda_199F')
    def lambda_199F():
        ChrMoveTo(0x00FE, -50600, -500, -20790, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_199F)

    WaitForThreadExit(0x0106, 0x0001)
    SetChrChipByIndex(0x0106, 7)
    WaitForThreadExit(0x000C, 0x0001)
    WaitForThreadExit(0x000D, 0x0001)
    WaitForThreadExit(0x000E, 0x0001)
    WaitForThreadExit(0x0010, 0x0001)

    @scena.Lambda('lambda_19D8')
    def lambda_19D8():
        OP_92(0x00FE, 0x0106, 3000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_19D8)

    @scena.Lambda('lambda_19ED')
    def lambda_19ED():
        OP_92(0x00FE, 0x0106, 3000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_19ED)

    @scena.Lambda('lambda_1A02')
    def lambda_1A02():
        ChrJumpTo(0x00FE, -49020, -300, -16110, 1000, 7000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1A02)

    Sleep(150)

    @scena.Lambda('lambda_1A25')
    def lambda_1A25():
        OP_92(0x00FE, 0x0106, 3500, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1A25)

    Sleep(150)

    @scena.Lambda('lambda_1A3F')
    def lambda_1A3F():
        OP_92(0x00FE, 0x0106, 3500, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1A3F)

    Sleep(150)

    @scena.Lambda('lambda_1A59')
    def lambda_1A59():
        OP_92(0x00FE, 0x0106, 3000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_1A59)

    WaitForThreadExit(0x000A, 0x0001)
    WaitForThreadExit(0x000B, 0x0001)
    WaitForThreadExit(0x000C, 0x0001)
    WaitForThreadExit(0x000D, 0x0001)
    WaitForThreadExit(0x000E, 0x0001)
    WaitForThreadExit(0x0010, 0x0001)

    @scena.Lambda('lambda_1A8C')
    def lambda_1A8C():
        OP_94(0x01, 0x00FE, 0x0064, 0x000001F4, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1A8C)

    Sleep(200)

    @scena.Lambda('lambda_1AA7')
    def lambda_1AA7():
        OP_94(0x01, 0x00FE, 0x0064, 0x000001F4, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1AA7)

    Sleep(100)

    @scena.Lambda('lambda_1AC2')
    def lambda_1AC2():
        OP_94(0x01, 0x00FE, 0x0064, 0x000001F4, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1AC2)

    @scena.Lambda('lambda_1AD8')
    def lambda_1AD8():
        OP_94(0x01, 0x00FE, 0x0064, 0x000001F4, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1AD8)

    Sleep(100)

    @scena.Lambda('lambda_1AF3')
    def lambda_1AF3():
        OP_94(0x01, 0x00FE, 0x0064, 0x000001F4, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1AF3)

    Sleep(200)

    @scena.Lambda('lambda_1B0E')
    def lambda_1B0E():
        OP_94(0x01, 0x00FE, 0x0064, 0x000001F4, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_1B0E)

    Sleep(100)

    @scena.Lambda('lambda_1B29')
    def lambda_1B29():
        OP_94(0x01, 0x00FE, 0x005A, 0x000001F4, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1B29)

    @scena.Lambda('lambda_1B3F')
    def lambda_1B3F():
        OP_94(0x01, 0x00FE, 0x005A, 0x000001F4, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1B3F)

    Sleep(100)

    @scena.Lambda('lambda_1B5A')
    def lambda_1B5A():
        OP_94(0x01, 0x00FE, 0x005A, 0x000001F4, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1B5A)

    Sleep(200)

    @scena.Lambda('lambda_1B75')
    def lambda_1B75():
        OP_94(0x01, 0x00FE, 0x005A, 0x000001F4, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1B75)

    Sleep(100)

    @scena.Lambda('lambda_1B90')
    def lambda_1B90():
        OP_94(0x01, 0x00FE, 0x005A, 0x000001F4, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1B90)

    Sleep(200)

    @scena.Lambda('lambda_1BAB')
    def lambda_1BAB():
        OP_94(0x01, 0x00FE, 0x005A, 0x000001F4, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_1BAB)

    SetChrDirection(0x0106, 135, 400)

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
    SetChrChipByIndex(0x0101, 10)
    SetChrChipByIndex(0x0102, 12)
    ClearChrFlags(0x0101, 0x1000)
    ClearChrFlags(0x0102, 0x1000)

    @scena.Lambda('lambda_1C4F')
    def lambda_1C4F():
        ChrWalkTo(0x0101, -48090, -300, -16590, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1C4F)

    Sleep(300)

    @scena.Lambda('lambda_1C6F')
    def lambda_1C6F():
        ChrWalkTo(0x0102, -48090, -300, -16590, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1C6F)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_1C8F')
    def lambda_1C8F():
        ChrJumpTo(0x0101, -49250, -640, -19500, 1000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1C8F)

    WaitForThreadExit(0x0102, 0x0001)

    @scena.Lambda('lambda_1CB2')
    def lambda_1CB2():
        ChrJumpTo(0x0102, -48270, -500, -18950, 1000, 10000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1CB2)

    @scena.Lambda('lambda_1CD0')
    def lambda_1CD0():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1CD0)

    Sleep(100)

    @scena.Lambda('lambda_1CEB')
    def lambda_1CEB():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1CEB)

    @scena.Lambda('lambda_1D01')
    def lambda_1D01():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1D01)

    WaitForThreadExit(0x0101, 0x0001)
    PlaySE(164, 0x00, 0x64)

    @scena.Lambda('lambda_1D21')
    def lambda_1D21():
        SetChrDirection(0x00FE, 315, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1D21)

    Sleep(50)

    @scena.Lambda('lambda_1D34')
    def lambda_1D34():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1D34)

    @scena.Lambda('lambda_1D4A')
    def lambda_1D4A():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1D4A)

    Sleep(100)

    @scena.Lambda('lambda_1D65')
    def lambda_1D65():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_1D65)

    WaitForThreadExit(0x0102, 0x0001)
    PlaySE(164, 0x00, 0x64)

    @scena.Lambda('lambda_1D85')
    def lambda_1D85():
        SetChrDirection(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_1D85)

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

    @scena.Lambda('lambda_1EA6')
    def lambda_1EA6():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000BB8, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1EA6)

    @scena.Lambda('lambda_1EBC')
    def lambda_1EBC():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000BB8, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1EBC)

    Sleep(100)

    @scena.Lambda('lambda_1ED7')
    def lambda_1ED7():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000BB8, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1ED7)

    Sleep(50)

    @scena.Lambda('lambda_1EF2')
    def lambda_1EF2():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000BB8, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1EF2)

    @scena.Lambda('lambda_1F08')
    def lambda_1F08():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000BB8, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1F08)

    Sleep(100)

    @scena.Lambda('lambda_1F23')
    def lambda_1F23():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000BB8, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_1F23)

    Sleep(200)

    Battle(0x00000396, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_1F51'),
        (-1, 'loc_1F54'),
    )

    def _loc_1F51(): pass

    label('loc_1F51')

    OP_B4(0x00)

    Return()

    def _loc_1F54(): pass

    label('loc_1F54')

    EventBegin(0x00)
    FadeIn(1000, 0)
    SetChrStatus(0x0005, 0x00, 24)
    EquipCmd(0x05, 0x00F3)
    EquipCmd(0x05, 0x0111)
    CameraSetDistance(3000, 0)
    SetChrPos(0x0101, -49970, -650, -18800, 315)
    SetChrPos(0x0102, -47880, -430, -19000, 45)
    SetChrPos(0x0106, -48850, -540, -20000, 180)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0106, 0xFF)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0106, 15)
    SetChrFlags(0x0013, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000F, 0x0080)
    SetChrFlags(0x0010, 0x0080)

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

    @scena.Lambda('lambda_20E8')
    def lambda_20E8():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_20E8)

    ChrTurnDirection(0x0101, 0x0106, 400)

    ChrTalk(
        0x0101,
        (
            '#0010040277V#004F啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0106, 0, 400)

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
    SetChrChipByIndex(0x0011, 6)
    SetChrChipByIndex(0x0012, 14)
    SetChrPos(0x0011, -50620, 450, -7940, 0)
    SetChrPos(0x0012, -49390, 450, -8010, 0)
    ClearChrFlags(0x0011, 0x0020)
    ClearChrFlags(0x0012, 0x0020)

    ChrTalk(
        0x0011,
        (
            '#1430040280V喂——！\n',
            '你们那边没事吧！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_21C6')
    def lambda_21C6():
        CameraMove(-49756, -300, -16490, 2000)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_21C6)

    @scena.Lambda('lambda_21DE')
    def lambda_21DE():
        ChrWalkTo(0x00FE, -50310, 0, -14800, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_21DE)

    Sleep(500)

    @scena.Lambda('lambda_21FE')
    def lambda_21FE():
        ChrWalkTo(0x00FE, -49250, 0, -14300, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_21FE)

    @scena.Lambda('lambda_2219')
    def lambda_2219():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2219)

    @scena.Lambda('lambda_2227')
    def lambda_2227():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2227)

    @scena.Lambda('lambda_2235')
    def lambda_2235():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_2235)

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
    SetChrDirection(0x0011, 45, 400)

    @scena.Lambda('lambda_2445')
    def lambda_2445():
        ChrWalkTo(0x00FE, -50080, 450, -7500, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_2445)

    Sleep(500)

    SetChrDirection(0x0012, 45, 400)

    @scena.Lambda('lambda_246C')
    def lambda_246C():
        ChrWalkTo(0x00FE, -50080, 450, -7500, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_246C)

    WaitForThreadExit(0x0011, 0x0001)
    SetChrFlags(0x0011, 0x0080)
    WaitForThreadExit(0x0012, 0x0001)
    SetChrFlags(0x0012, 0x0080)

    @scena.Lambda('lambda_249B')
    def lambda_249B():
        ChrTurnDirection(0x00FE, 0x0106, 400)
        Yield()

        Jump('lambda_249B')

    DispatchAsync2(0x0101, 0x0001, lambda_249B)

    @scena.Lambda('lambda_24AC')
    def lambda_24AC():
        ChrTurnDirection(0x00FE, 0x0106, 400)
        Yield()

        Jump('lambda_24AC')

    DispatchAsync2(0x0102, 0x0001, lambda_24AC)

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
    SetChrFlags(0x0106, 0x0080)
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
    SetMapFlags(0x00100000)
    Sleep(3000)

    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T1310._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0005 offset: 0x26D3
@scena.Code('func_05_26D3')
def func_05_26D3():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_291C',
    )

    OP_93(0x0009, 0x000A, 600, 5000, 0x00)
    OP_94(0x01, 0x000A, 0x00B4, 0x000003E8, 0x00001388, 0x00)

    @scena.Lambda('lambda_26FF')
    def lambda_26FF():
        ChrMoveTo(0x00FE, -45600, 0, 14320, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_26FF)

    @scena.Lambda('lambda_271A')
    def lambda_271A():
        SetChrDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_271A)

    PlaySE(163, 0x00, 0x64)
    ChrJumpTo(0x000A, -47500, 0, 13630, 2000, 6000)
    ChrTurnDirection(0x000A, 0x0009, 0)
    ChrTurnDirection(0x0009, 0x000A, 800)
    Sleep(1000)

    @scena.Lambda('lambda_2757')
    def lambda_2757():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_2757)

    @scena.Lambda('lambda_276D')
    def lambda_276D():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x000005DC, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_276D)

    WaitForThreadExit(0x0009, 0x0002)
    WaitForThreadExit(0x000A, 0x0002)
    Sleep(700)

    SetChrChipByIndex(0x000A, 2)

    @scena.Lambda('lambda_2797')
    def lambda_2797():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000640, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_2797)

    @scena.Lambda('lambda_27AD')
    def lambda_27AD():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000640, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_27AD)

    WaitForThreadExit(0x0009, 0x0002)
    WaitForThreadExit(0x000A, 0x0002)
    PlaySE(555, 0x00, 0x64)
    SetChrChipByIndex(0x000A, 1)

    @scena.Lambda('lambda_27D7')
    def lambda_27D7():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x0000012C, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_27D7)

    @scena.Lambda('lambda_27ED')
    def lambda_27ED():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x0000012C, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_27ED)

    Sleep(600)

    @scena.Lambda('lambda_2808')
    def lambda_2808():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x0000012C, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_2808)

    @scena.Lambda('lambda_281E')
    def lambda_281E():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x0000012C, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_281E)

    Sleep(200)

    @scena.Lambda('lambda_2839')
    def lambda_2839():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x0000012C, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_2839)

    @scena.Lambda('lambda_284F')
    def lambda_284F():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x0000012C, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_284F)

    Sleep(200)

    @scena.Lambda('lambda_286A')
    def lambda_286A():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x0000012C, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_286A)

    @scena.Lambda('lambda_2880')
    def lambda_2880():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x0000012C, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_2880)

    Sleep(200)

    @scena.Lambda('lambda_289B')
    def lambda_289B():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x0000012C, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_289B)

    @scena.Lambda('lambda_28B1')
    def lambda_28B1():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x0000012C, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_28B1)

    Sleep(200)

    @scena.Lambda('lambda_28CC')
    def lambda_28CC():
        ChrMoveTo(0x00FE, -47500, 0, 13630, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_28CC)

    @scena.Lambda('lambda_28E7')
    def lambda_28E7():
        SetChrDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_28E7)

    PlaySE(163, 0x00, 0x64)
    ChrJumpTo(0x000A, -45600, 0, 14320, 2000, 6000)
    ChrTurnDirection(0x000A, 0x0009, 0)
    ChrTurnDirection(0x0009, 0x000A, 800)

    Jump('func_05_26D3')

    def _loc_291C(): pass

    label('loc_291C')

    Return()

# id: 0x0006 offset: 0x291D
@scena.Code('func_06_291D')
def func_06_291D():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2C31',
    )

    SetChrFlags(0x0011, 0x0020)

    ExecExpressionWithValue(
        0x0011,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0011, 19)

    @scena.Lambda('lambda_2941')
    def lambda_2941():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x0000012C, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_2941)

    @scena.Lambda('lambda_2957')
    def lambda_2957():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x0000012C, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_2957)

    Sleep(200)

    @scena.Lambda('lambda_2972')
    def lambda_2972():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_2972)

    @scena.Lambda('lambda_2988')
    def lambda_2988():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_2988)

    Sleep(200)

    @scena.Lambda('lambda_29A3')
    def lambda_29A3():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x0000012C, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_29A3)

    @scena.Lambda('lambda_29B9')
    def lambda_29B9():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x0000012C, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_29B9)

    Sleep(200)

    @scena.Lambda('lambda_29D4')
    def lambda_29D4():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x0000012C, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_29D4)

    @scena.Lambda('lambda_29EA')
    def lambda_29EA():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x0000012C, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_29EA)

    Sleep(200)

    @scena.Lambda('lambda_2A05')
    def lambda_2A05():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x00000190, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_2A05)

    @scena.Lambda('lambda_2A1B')
    def lambda_2A1B():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x00000190, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_2A1B)

    Sleep(200)

    @scena.Lambda('lambda_2A36')
    def lambda_2A36():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x000000C8, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_2A36)

    @scena.Lambda('lambda_2A4C')
    def lambda_2A4C():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x000000C8, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_2A4C)

    Sleep(200)

    @scena.Lambda('lambda_2A67')
    def lambda_2A67():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_2A67)

    @scena.Lambda('lambda_2A7D')
    def lambda_2A7D():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_2A7D)

    Sleep(500)

    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    SetChrChipByIndex(0x000F, 2)

    @scena.Lambda('lambda_2AA0')
    def lambda_2AA0():
        OP_94(0x01, 0x00FE, 0x0000, 0x000005DC, 0x000009C4, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_2AA0)

    Sleep(500)

    WaitForThreadExit(0x000F, 0x0002)

    @scena.Lambda('lambda_2AC0')
    def lambda_2AC0():
        ChrJumpTo(0x00FE, -45180, 0, 17190, 1000, 6000)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_2AC0)

    TerminateThread(0x000F, 0x01)
    TerminateThread(0x000B, 0x01)
    OP_99(0x0011, 0x01, 0x03, 3000)
    SetChrChipByIndex(0x000B, 5)

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrFlags(0x000B, 0x0020)
    PlaySE(501, 0x00, 0x64)

    @scena.Lambda('lambda_2B09')
    def lambda_2B09():
        OP_99(0x0011, 0x03, 0x07, 3000)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_2B09)

    @scena.Lambda('lambda_2B19')
    def lambda_2B19():
        ChrMoveTo(0x00FE, -48130, 0, 14880, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_2B19)

    @scena.Lambda('lambda_2B34')
    def lambda_2B34():
        ChrMoveTo(0x00FE, -44730, 0, 19520, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_2B34)

    WaitForThreadExit(0x000F, 0x0002)

    @scena.Lambda('lambda_2B54')
    def lambda_2B54():
        ChrJumpTo(0x00FE, -47500, 0, 15620, 1000, 6000)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_2B54)

    WaitForThreadExit(0x000B, 0x0002)
    SetChrChipByIndex(0x000B, 1)
    WaitForThreadExit(0x000F, 0x0002)
    SetChrChipByIndex(0x000F, 1)
    SetChrPos(0x000B, -47500, 0, 15620, 225)
    SetChrPos(0x000F, -44730, 0, 19520, 225)

    @scena.Lambda('lambda_2BA8')
    def lambda_2BA8():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000001F4, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_2BA8)

    ExecExpressionWithValue(
        0x0011,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0011, 19)
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

    SetChrChipByIndex(0x0011, 17)
    CreateThread(0x000B, 0x01, 0x00, 0x0002)
    CreateThread(0x000F, 0x01, 0x00, 0x0002)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    CreateThread(0x0011, 0x02, 0x00, 0x0002)
    Sleep(500)

    Sleep(1000)

    @scena.Lambda('lambda_2C0F')
    def lambda_2C0F():
        OP_94(0x01, 0x00FE, 0x0000, 0x000001F4, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_2C0F)

    OP_94(0x01, 0x0011, 0x0000, 0x000001F4, 0x00000FA0, 0x00)

    Jump('func_06_291D')

    def _loc_2C31(): pass

    label('loc_2C31')

    Return()

# id: 0x0007 offset: 0x2C32
@scena.Code('func_07_2C32')
def func_07_2C32():
    SetChrFlags(0x000C, 0x0040)
    SetChrFlags(0x000D, 0x0040)
    SetChrFlags(0x000E, 0x0040)
    SetChrFlags(0x0012, 0x0040)

    @scena.Lambda('lambda_2C4C')
    def lambda_2C4C():
        ChrTurnDirection(0x00FE, 0x000E, 0)
        Yield()

        Jump('lambda_2C4C')

    DispatchAsync2(0x0008, 0x0000, lambda_2C4C)

    @scena.Lambda('lambda_2C5D')
    def lambda_2C5D():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_2C5D')

    DispatchAsync2(0x000E, 0x0000, lambda_2C5D)

    def _loc_2C68(): pass

    label('loc_2C68')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2FDF',
    )

    PlaySE(551, 0x00, 0x64)

    @scena.Lambda('lambda_2C7C')
    def lambda_2C7C():
        OP_93(0x00FE, 0x0008, 600, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_2C7C)

    @scena.Lambda('lambda_2C91')
    def lambda_2C91():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_2C91)

    SetChrChipByIndex(0x000D, 2)
    OP_93(0x000D, 0x0012, 600, 6000, 0x00)
    SetChrChipByIndex(0x000D, 1)
    OP_94(0x01, 0x0012, 0x00B4, 0x000001F4, 0x00001388, 0x00)
    Sleep(200)

    OP_94(0x01, 0x0012, 0x0000, 0x000001F4, 0x00001388, 0x00)

    @scena.Lambda('lambda_2CE2')
    def lambda_2CE2():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x0000012C, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2CE2)

    @scena.Lambda('lambda_2CF8')
    def lambda_2CF8():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x0000012C, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_2CF8)

    @scena.Lambda('lambda_2D0E')
    def lambda_2D0E():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_2D0E)

    @scena.Lambda('lambda_2D24')
    def lambda_2D24():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_2D24)

    Sleep(500)

    @scena.Lambda('lambda_2D3F')
    def lambda_2D3F():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_2D3F)

    @scena.Lambda('lambda_2D55')
    def lambda_2D55():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_2D55)

    Sleep(500)

    @scena.Lambda('lambda_2D70')
    def lambda_2D70():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_2D70)

    @scena.Lambda('lambda_2D86')
    def lambda_2D86():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_2D86)

    Sleep(500)

    TerminateThread(0x0008, 0x02)

    @scena.Lambda('lambda_2DA5')
    def lambda_2DA5():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_2DA5)

    PlaySE(203, 0x00, 0x64)
    ChrJumpTo(0x0008, -50400, 0, 16600, 600, 6000)
    WaitForThreadExit(0x000C, 0x0002)

    @scena.Lambda('lambda_2DDC')
    def lambda_2DDC():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000007D0, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_2DDC)

    @scena.Lambda('lambda_2DF2')
    def lambda_2DF2():
        OP_92(0x00FE, 0x0008, 300, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_2DF2)

    Sleep(150)

    ChrJumpTo(0x0008, -52100, 0, 16950, 1000, 6000)
    PlaySE(203, 0x00, 0x64)

    @scena.Lambda('lambda_2E28')
    def lambda_2E28():
        ChrTurnDirection(0x00FE, 0x000E, 800)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2E28)

    ChrTurnDirection(0x000E, 0x0008, 800)
    OP_92(0x0008, 0x000E, 600, 5000, 0x00)
    PlaySE(551, 0x00, 0x64)
    OP_94(0x01, 0x000E, 0x00B4, 0x000003E8, 0x00001388, 0x00)
    WaitForThreadExit(0x0008, 0x0002)
    WaitForThreadExit(0x000E, 0x0002)

    @scena.Lambda('lambda_2E69')
    def lambda_2E69():
        ChrMoveTo(0x00FE, -52080, 0, 15480, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2E69)

    @scena.Lambda('lambda_2E84')
    def lambda_2E84():
        ChrWalkTo(0x00FE, -51450, 0, 17000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_2E84)

    @scena.Lambda('lambda_2E9F')
    def lambda_2E9F():
        OP_93(0x00FE, 0x0012, 2500, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_2E9F)

    SetChrChipByIndex(0x000C, 2)
    Sleep(1700)

    @scena.Lambda('lambda_2EBE')
    def lambda_2EBE():
        OP_93(0x00FE, 0x0012, 600, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_2EBE)

    PlaySE(554, 0x00, 0x64)
    TerminateThread(0x000D, 0x01)
    SetChrChipByIndex(0x000D, 5)

    ExecExpressionWithValue(
        0x000D,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrFlags(0x000D, 0x0020)

    @scena.Lambda('lambda_2EF1')
    def lambda_2EF1():
        ChrMoveTo(0x00FE, -47980, 0, 18190, 13000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_2EF1)

    @scena.Lambda('lambda_2F0C')
    def lambda_2F0C():
        OP_94(0x01, 0x00FE, 0x0000, 0x000001F4, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_2F0C)

    @scena.Lambda('lambda_2F22')
    def lambda_2F22():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x0000012C, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2F22)

    @scena.Lambda('lambda_2F38')
    def lambda_2F38():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x0000012C, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_2F38)

    WaitForThreadExit(0x000D, 0x0002)
    SetChrChipByIndex(0x000D, 1)
    ClearChrFlags(0x000D, 0x0020)
    CreateThread(0x000D, 0x01, 0x00, 0x0002)
    WaitForThreadExit(0x000C, 0x0002)
    PlaySE(555, 0x00, 0x64)
    TerminateThread(0x000C, 0x01)
    SetChrChipByIndex(0x000C, 5)

    ExecExpressionWithValue(
        0x000C,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrFlags(0x000C, 0x0020)

    @scena.Lambda('lambda_2F87')
    def lambda_2F87():
        ChrMoveTo(0x00FE, -50380, 0, 18680, 13000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_2F87)

    @scena.Lambda('lambda_2FA2')
    def lambda_2FA2():
        ChrMoveTo(0x00FE, -49730, 0, 15340, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_2FA2)

    WaitForThreadExit(0x000C, 0x0002)
    SetChrChipByIndex(0x000C, 1)
    ClearChrFlags(0x000C, 0x0020)
    CreateThread(0x000C, 0x01, 0x00, 0x0002)
    WaitForThreadExit(0x0012, 0x0002)
    WaitForThreadExit(0x000C, 0x0002)
    WaitForThreadExit(0x000D, 0x0002)

    Jump('loc_2C68')

    def _loc_2FDF(): pass

    label('loc_2FDF')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

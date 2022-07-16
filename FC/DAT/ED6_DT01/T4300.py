import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4300_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4300   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '中队长'),
    TXT(0x02, '特务兵'),
    TXT(0x03, '特务兵'),
    TXT(0x04, '特务兵'),
    TXT(0x05, '特务兵'),
    TXT(0x06, '特务兵'),
    TXT(0x07, '特务兵'),
    TXT(0x08, '特务兵'),
    TXT(0x09, '特务兵'),
    TXT(0x0A, '特务兵'),
    TXT(0x0B, '特务兵'),
    TXT(0x0C, '军用犬'),
    TXT(0x0D, '军用犬'),
    TXT(0x0E, '军用犬'),
    TXT(0x0F, '军用犬'),
    TXT(0x10, '军用犬'),
    TXT(0x11, '亲卫队员'),
    TXT(0x12, '亲卫队员'),
    TXT(0x13, '亲卫队员'),
    TXT(0x14, '亲卫队员'),
    TXT(0x15, '科洛丝'),
    TXT(0x16, '雪拉'),
    TXT(0x17, '奥利维尔'),
    TXT(0x18, '奈尔'),
    TXT(0x19, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4300.x'
    header.mapIndex       = 1
    header.bgm            = 89
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1AF5
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
        ('ED6_DT07/CH01610._CH', 'ED6_DT07/CH01610P._CP'),
        ('ED6_DT07/CH01800._CH', 'ED6_DT07/CH01800P._CP'),
        ('ED6_DT09/CH10060._CH', 'ED6_DT09/CH10060P._CP'),
        ('ED6_DT07/CH01320._CH', 'ED6_DT07/CH01320P._CP'),
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00101._CH', 'ED6_DT07/CH00101P._CP'),
        ('ED6_DT07/CH00110._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT07/CH00111._CH', 'ED6_DT07/CH00111P._CP'),
        ('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP'),
        ('ED6_DT07/CH00171._CH', 'ED6_DT07/CH00171P._CP'),
        ('ED6_DT07/CH00340._CH', 'ED6_DT07/CH00340P._CP'),
        ('ED6_DT07/CH00341._CH', 'ED6_DT07/CH00341P._CP'),
        ('ED6_DT07/CH00342._CH', 'ED6_DT07/CH00342P._CP'),
        ('ED6_DT07/CH00040._CH', 'ED6_DT07/CH00040P._CP'),
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT07/CH02060._CH', 'ED6_DT07/CH02060P._CP'),
        ('ED6_DT06/CH20116._CH', 'ED6_DT06/CH20116P._CP'),
        ('ED6_DT06/CH20117._CH', 'ED6_DT06/CH20117P._CP'),
    ]

# id: 0x10002 offset: 0x142
@scena.NpcData('NpcData')
def NpcData():
    return (
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
            dword_10            = 17,
            chipIndex           = 17,
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
            dword_10            = 17,
            chipIndex           = 17,
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
            dword_10            = 17,
            chipIndex           = 17,
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
            dword_10            = 17,
            chipIndex           = 17,
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
            dword_10            = 13,
            chipIndex           = 13,
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
            dword_10            = 14,
            chipIndex           = 14,
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
            dword_10            = 15,
            chipIndex           = 15,
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
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x442
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x442
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x442
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x442
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_453',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x0002)

    Jump('loc_4B6')

    def _loc_453(): pass

    label('loc_453')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_472',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    SetMapFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, 0x0005)

    Jump('loc_4B6')

    def _loc_472(): pass

    label('loc_472')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 4, 0x3FC)),
            Expr.Return,
        ),
        'loc_483',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    Event(0, 0x0006)

    Jump('loc_4B6')

    def _loc_483(): pass

    label('loc_483')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 5, 0x3FD)),
            Expr.Return,
        ),
        'loc_494',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 5, 0x3FD))
    Event(0, 0x0007)

    Jump('loc_4B6')

    def _loc_494(): pass

    label('loc_494')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_4A0'),
        (-1, 'loc_4B6'),
    )

    def _loc_4A0(): pass

    label('loc_4A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 2, 0x652)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 1, 0x651)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4B3',
    )

    SetScenaFlags(ScenaFlag(0x00CA, 2, 0x652))
    Event(0, 0x0003)

    def _loc_4B3(): pass

    label('loc_4B3')

    Jump('loc_4B6')

    def _loc_4B6(): pass

    label('loc_4B6')

    Return()

# id: 0x0001 offset: 0x4B7
@scena.Code('Init')
def Init():
    OP_16(0x02, 4000, -128000, -96000, 196705)

    Return()

# id: 0x0002 offset: 0x4CA
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x00)
    CameraMove(-70, 0, 20900, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(0, 0)
    OP_6E(408, 0)

    @scena.Lambda('lambda_050F')
    def lambda_050F():
        CameraMove(-1300, 0, 47880, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_050F)

    @scena.Lambda('lambda_0527')
    def lambda_0527():
        OP_6C(314000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0527)

    @scena.Lambda('lambda_0537')
    def lambda_0537():
        OP_6E(262, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0537)

    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0012, 0x0080)

    @scena.Lambda('lambda_057E')
    def lambda_057E():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_057E')

    DispatchAsync2(0x0013, 0x0000, lambda_057E)

    @scena.Lambda('lambda_0591')
    def lambda_0591():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_0591')

    DispatchAsync2(0x0014, 0x0000, lambda_0591)

    @scena.Lambda('lambda_05A4')
    def lambda_05A4():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_05A4')

    DispatchAsync2(0x0015, 0x0000, lambda_05A4)

    @scena.Lambda('lambda_05B7')
    def lambda_05B7():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_05B7')

    DispatchAsync2(0x0016, 0x0000, lambda_05B7)

    @scena.Lambda('lambda_05CA')
    def lambda_05CA():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_05CA')

    DispatchAsync2(0x0017, 0x0000, lambda_05CA)

    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x0017, 0x0080)
    SetChrPos(0x0008, -70, 1000, 50380, 180)
    SetChrPos(0x0009, 730, 0, 46530, 0)
    SetChrPos(0x000A, 2350, 0, 46770, 315)
    SetChrPos(0x000B, 2090, 0, 45430, 332)
    SetChrPos(0x000C, 1380, 0, 44350, 351)
    SetChrPos(0x000D, 470, 0, 43290, 7)
    SetChrPos(0x000E, -920, 0, 43360, 353)
    SetChrPos(0x000F, -2230, 0, 44390, 7)
    SetChrPos(0x0010, -1210, 0, 45310, 16)
    SetChrPos(0x0011, -2029, 0, 46530, 25)
    SetChrPos(0x0012, -690, 0, 46650, 7)
    SetChrPos(0x0013, -3190, 0, 43920, 33)
    SetChrPos(0x0014, -3130, 250, 47070, 62)
    SetChrPos(0x0015, 3260, 0, 45110, 307)
    SetChrPos(0x0016, 80, 0, 44910, 349)
    SetChrPos(0x0017, 1250, 0, 42490, 5)
    Sleep(5000)

    ChrTalk(
        0x0008,
        (
            '#2680130567V听着！\n',
            '从特务飞艇传来消息！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2680130568V亲卫队的残党\n',
            '竟然恬不知耻的出现了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2680130569V立刻前往现场，\n',
            '借此机会将他们全部剿灭！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    SetMessageWindowPos(70, 80, -1, -1)
    SetChrName('特务兵们')

    Talk(
        (
            '#2620130570V',
            (TxtCtl.SetColor, 0x0),
            '#5S是！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    OP_56(0x00)
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/C4113._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x7DD
@scena.Code('func_03_7DD')
def func_03_7DD():
    EventBegin(0x00)
    OP_6F(0x000D, 120)
    OP_72(0x000D, 0x0010)
    ClearChrFlags(0x0018, 0x0080)
    ClearChrFlags(0x0019, 0x0080)
    ClearChrFlags(0x001A, 0x0080)
    ClearChrFlags(0x001B, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    SetChrChipByIndex(0x0009, 12)
    SetChrChipByIndex(0x000A, 10)
    SetChrChipByIndex(0x000B, 10)
    SetChrChipByIndex(0x000C, 10)
    SetChrChipByIndex(0x000D, 10)
    SetChrChipByIndex(0x000E, 10)
    SetChrChipByIndex(0x0101, 4)
    SetChrChipByIndex(0x0102, 6)
    SetChrChipByIndex(0x0108, 8)
    SetChrPos(0x0108, 70, 0, 26850, 356)
    SetChrPos(0x0101, -640, 0, 26250, 315)
    SetChrPos(0x0102, 1000, 0, 26220, 45)
    SetChrFlags(0x0108, 0x0080)
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x0102, 0x0080)
    SetChrPos(0x0018, 9480, 250, 32070, 180)
    SetChrPos(0x0009, 9490, 250, 31050, 0)
    SetChrPos(0x0019, 8250, 130, 44870, 46)
    SetChrPos(0x000A, 7080, 0, 41450, 14)
    SetChrPos(0x000B, 17790, 0, 47220, 260)
    SetChrPos(0x001A, -18980, 0, 51590, 180)
    SetChrPos(0x000C, -19080, 0, 48030, 0)
    SetChrPos(0x001B, -9790, 210, 47380, 56)
    SetChrPos(0x000D, -19320, 0, 41420, 44)
    SetChrPos(0x000E, -17850, 20, 41630, 80)
    FadeIn(2000, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(278000, 0)
    OP_6E(288, 0)
    Fade(1000)
    CameraMove(9140, 250, 31570, 0)

    @scena.Lambda('lambda_0987')
    def lambda_0987():
        OP_6C(314000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0987)

    SetChrChipByIndex(0x0018, 18)
    SetChrSubChip(0x0018, 1)
    PlaySE(501, 0x00, 0x64)
    SetChrFlags(0x0009, 0x0020)

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_09B6')
    def lambda_09B6():
        OP_9E(0x00FE, 30, 0, 1000, 3000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_09B6)

    @scena.Lambda('lambda_09D0')
    def lambda_09D0():
        OP_9E(0x00FE, 30, 0, 1000, 3000)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_09D0)

    Sleep(1000)

    @scena.Lambda('lambda_09EF')
    def lambda_09EF():
        OP_99(0x0009, 0x02, 0x07, 2500)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_09EF)

    Sleep(100)

    SetChrChipByIndex(0x0018, 17)
    ChrJumpTo(0x0018, 9490, 250, 32990, 1000, 8000)
    PlaySE(164, 0x00, 0x64)
    SetChrFlags(0x0018, 0x0020)

    @scena.Lambda('lambda_0A2A')
    def lambda_0A2A():
        ChrWalkTo(0x0018, 9470, 250, 31940, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_0A2A)

    Sleep(50)

    SetChrChipByIndex(0x0018, 18)
    PlaySE(501, 0x00, 0x64)
    SetChrSubChip(0x0018, 0)
    Sleep(50)

    SetChrSubChip(0x0018, 1)
    Sleep(50)

    SetChrSubChip(0x0018, 2)
    ChrJumpTo(0x0009, 9460, 250, 29930, 1000, 8000)
    PlaySE(164, 0x00, 0x64)

    @scena.Lambda('lambda_0A89')
    def lambda_0A89():
        OP_99(0x0009, 0x00, 0x02, 2000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0A89)

    ChrWalkTo(0x0009, 9470, 250, 31130, 7000, 0x00)
    SetChrSubChip(0x0018, 1)
    PlaySE(501, 0x00, 0x64)

    @scena.Lambda('lambda_0AB7')
    def lambda_0AB7():
        OP_9E(0x00FE, 30, 0, 1000, 3000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0AB7)

    @scena.Lambda('lambda_0AD1')
    def lambda_0AD1():
        OP_9E(0x00FE, 30, 0, 1000, 3000)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_0AD1)

    Sleep(500)

    Fade(1000)
    CameraMove(7760, 0, 43410, 0)
    OP_6E(330, 0)

    @scena.Lambda('lambda_0B0F')
    def lambda_0B0F():
        OP_6E(262, 5000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_0B0F)

    @scena.Lambda('lambda_0B1F')
    def lambda_0B1F():
        CameraMove(11360, 0, 49140, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0B1F)

    @scena.Lambda('lambda_0B37')
    def lambda_0B37():
        ChrTurnDirection(0x00FE, 0x0019, 0)
        Yield()

        Jump('lambda_0B37')

    DispatchAsync2(0x000A, 0x0002, lambda_0B37)

    SetChrFlags(0x0019, 0x0040)
    SetChrFlags(0x000B, 0x0040)
    SetChrFlags(0x000B, 0x0040)
    SetChrChipByIndex(0x000A, 11)
    SetChrChipByIndex(0x000B, 11)

    @scena.Lambda('lambda_0B61')
    def lambda_0B61():
        ChrWalkTo(0x00FE, 15330, 250, 47290, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0B61)

    @scena.Lambda('lambda_0B7C')
    def lambda_0B7C():
        ChrWalkTo(0x00FE, 8890, 230, 46350, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0B7C)

    @scena.Lambda('lambda_0B97')
    def lambda_0B97():
        ChrWalkTo(0x00FE, 10020, 250, 47350, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_0B97)

    WaitForThreadExit(0x0019, 0x0001)

    @scena.Lambda('lambda_0BB7')
    def lambda_0BB7():
        ChrWalkTo(0x00FE, 11360, 0, 49430, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_0BB7)

    WaitForThreadExit(0x0019, 0x0001)
    SetChrChipByIndex(0x0019, 18)
    SetChrSubChip(0x0019, 2)
    SetChrFlags(0x0019, 0x0020)
    ChrTurnDirection(0x0019, 0x000A, 800)
    Sleep(200)

    @scena.Lambda('lambda_0BF2')
    def lambda_0BF2():
        OP_92(0x00FE, 0x0019, 1000, 400, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0BF2)

    @scena.Lambda('lambda_0C07')
    def lambda_0C07():
        OP_92(0x00FE, 0x0019, 1000, 800, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0C07)

    Sleep(300)

    ChrTurnDirection(0x0019, 0x000B, 800)
    SetChrFlags(0x000B, 0x0020)

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_99(0x000B, 0x00, 0x02, 2000)

    @scena.Lambda('lambda_0C41')
    def lambda_0C41():
        OP_99(0x00FE, 0x03, 0x07, 1000)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_0C41)

    @scena.Lambda('lambda_0C51')
    def lambda_0C51():
        ChrWalkTo(0x00FE, 12240, 0, 48490, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0C51)

    Sleep(100)

    @scena.Lambda('lambda_0C71')
    def lambda_0C71():
        ChrWalkTo(0x00FE, 10290, 40, 47930, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0C71)

    Sleep(200)

    SetChrFlags(0x0019, 0x0004)
    SetChrSubChip(0x0019, 1)

    @scena.Lambda('lambda_0C9B')
    def lambda_0C9B():
        OP_97(0x00FE, 11990, 49260, 230000, 9400, 0x0001)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_0C9B)

    Sleep(250)

    PlaySE(553, 0x00, 0x64)

    @scena.Lambda('lambda_0CC1')
    def lambda_0CC1():
        ChrMoveTo(0x00FE, 11020, 250, 46930, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0CC1)

    Sleep(100)

    @scena.Lambda('lambda_0CE1')
    def lambda_0CE1():
        ChrJumpTo(0x00FE, 9200, 0, 47750, 600, 7000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0CE1)

    ClearChrFlags(0x0019, 0x0020)
    ClearChrFlags(0x0019, 0x0004)
    SetChrChipByIndex(0x0019, 17)

    @scena.Lambda('lambda_0D0E')
    def lambda_0D0E():
        ChrWalkTo(0x00FE, 20480, 0, 46180, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_0D0E)

    Sleep(500)

    @scena.Lambda('lambda_0D2E')
    def lambda_0D2E():
        OP_92(0x00FE, 0x0019, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0D2E)

    Sleep(500)

    @scena.Lambda('lambda_0D48')
    def lambda_0D48():
        OP_92(0x00FE, 0x0019, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0D48)

    Sleep(100)

    ClearChrFlags(0x000B, 0x0020)
    ChrWalkTo(0x000B, 11130, 0, 48250, 5000, 0x00)

    @scena.Lambda('lambda_0D7B')
    def lambda_0D7B():
        OP_92(0x00FE, 0x0019, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0D7B)

    @scena.Lambda('lambda_0D90')
    def lambda_0D90():
        OP_92(0x00FE, 0x0019, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0D90)

    Sleep(500)

    Fade(1000)
    CameraMove(-19190, 0, 50360, 0)
    SetChrChipByIndex(0x000C, 11)

    @scena.Lambda('lambda_0DC5')
    def lambda_0DC5():
        CameraMove(-19700, 0, 53190, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0DC5)

    OP_92(0x000C, 0x001A, 600, 6000, 0x00)

    @scena.Lambda('lambda_0DEB')
    def lambda_0DEB():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 2000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0DEB)

    ChrMoveToRelativeAsync(0x001A, 0, 0, 2000, 2000, 0x00)
    SetChrFlags(0x001A, 0x0020)
    SetChrChipByIndex(0x001A, 18)
    SetChrSubChip(0x001A, 1)

    @scena.Lambda('lambda_0E29')
    def lambda_0E29():
        OP_9E(0x00FE, 30, 0, 700, 3000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0E29)

    @scena.Lambda('lambda_0E43')
    def lambda_0E43():
        OP_9E(0x00FE, 30, 0, 700, 3000)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_0E43)

    Sleep(700)

    @scena.Lambda('lambda_0E62')
    def lambda_0E62():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_0E62')

    DispatchAsync2(0x001A, 0x0001, lambda_0E62)

    @scena.Lambda('lambda_0E73')
    def lambda_0E73():
        ChrMoveTo(0x00FE, -19520, 0, 53650, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0002, lambda_0E73)

    SetChrFlags(0x000C, 0x0004)
    SetChrFlags(0x000C, 0x0040)
    ChrMoveToRelativeAsync(0x000C, 0, 0, 400, 5000, 0x00)
    SetChrChipByIndex(0x001A, 17)
    PlaySE(520, 0x00, 0x64)
    OP_97(0x000C, -19520, 53650, -100000, 9000, 0x0002)
    SetChrChipByIndex(0x001A, 18)
    SetChrSubChip(0x001A, 2)
    ChrJumpTo(0x000C, -20930, -4000, 56530, 200, 10000)
    PlaySE(179, 0x00, 0x64)
    TerminateThread(0x001A, 0xFF)
    SetChrChipByIndex(0x000D, 11)

    @scena.Lambda('lambda_0EFA')
    def lambda_0EFA():
        ChrWalkTo(0x00FE, -19640, 0, 48710, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_0EFA)

    Sleep(500)

    @scena.Lambda('lambda_0F1A')
    def lambda_0F1A():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_0F1A)

    @scena.Lambda('lambda_0F28')
    def lambda_0F28():
        CameraMove(-19190, 0, 50360, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0F28)

    @scena.Lambda('lambda_0F40')
    def lambda_0F40():
        OP_6E(305, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0F40)

    SetChrChipByIndex(0x000E, 11)

    @scena.Lambda('lambda_0F55')
    def lambda_0F55():
        ChrWalkTo(0x00FE, -18180, 0, 48630, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0F55)

    Sleep(1500)

    @scena.Lambda('lambda_0F75')
    def lambda_0F75():
        ChrTurnDirection(0x00FE, 0x000E, 0)
        Yield()

        Jump('lambda_0F75')

    DispatchAsync2(0x001A, 0x0001, lambda_0F75)

    @scena.Lambda('lambda_0F86')
    def lambda_0F86():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 4000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_0F86)

    Sleep(200)

    @scena.Lambda('lambda_0FA6')
    def lambda_0FA6():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 4000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0FA6)

    Sleep(300)

    @scena.Lambda('lambda_0FC6')
    def lambda_0FC6():
        ChrWalkTo(0x00FE, -17510, 0, 48700, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_0FC6)

    Sleep(500)

    @scena.Lambda('lambda_0FE6')
    def lambda_0FE6():
        ChrTurnDirection(0x00FE, 0x001B, 800)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0FE6)

    @scena.Lambda('lambda_0FF4')
    def lambda_0FF4():
        ChrTurnDirection(0x00FE, 0x001B, 800)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_0FF4)

    Sleep(200)

    @scena.Lambda('lambda_1007')
    def lambda_1007():
        ChrJumpTo(0x00FE, -17510, 0, 48700, 2000, 5000)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_1007)

    SetChrFlags(0x001B, 0x0020)
    SetChrChipByIndex(0x001B, 18)
    SetChrSubChip(0x001B, 0)
    Sleep(300)

    PlaySE(501, 0x00, 0x64)
    SetChrSubChip(0x001B, 1)
    Sleep(50)

    SetChrSubChip(0x001B, 2)
    ChrJumpTo(0x000E, -18870, 0, 47400, 1000, 6000)
    PlaySE(164, 0x00, 0x64)
    Sleep(100)

    @scena.Lambda('lambda_106E')
    def lambda_106E():
        ChrMoveTo(0x00FE, -19580, 0, 46820, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_106E)

    @scena.Lambda('lambda_1089')
    def lambda_1089():
        ChrMoveTo(0x00FE, -20250, 0, 49620, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1089)

    SetChrChipByIndex(0x001A, 17)
    ClearChrFlags(0x001A, 0x0020)
    SetChrFlags(0x001A, 0x0004)
    ChrMoveTo(0x001A, -18520, 0, 51440, 4000, 0x00)
    ChrJumpTo(0x001A, -16410, 0, 49120, 1000, 7000)
    PlaySE(164, 0x00, 0x64)
    ChrMoveTo(0x001A, -17150, 0, 47680, 2000, 0x00)
    SetChrChipByIndex(0x001A, 18)
    SetChrSubChip(0x001A, 2)
    Fade(1000)
    ClearChrFlags(0x0108, 0x0080)
    ClearChrFlags(0x0101, 0x0080)
    ClearChrFlags(0x0102, 0x0080)
    CameraMove(110, 0, 26870, 0)
    OP_6C(326000, 0)
    OP_0D()

    ChrTalk(
        0x0108,
        (
            '#0080130588V#070F#5P好呀好呀……正在交战呢。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130589V我们趁机冲进这座宫殿里去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130590V#006F#3PＯＫ！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130591V#012F明白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_11B6')
    def lambda_11B6():
        CameraMove(-60, 1000, 57500, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_11B6)

    @scena.Lambda('lambda_11CE')
    def lambda_11CE():
        OP_67(0, 5710, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_11CE)

    @scena.Lambda('lambda_11E6')
    def lambda_11E6():
        CameraSetDistance(1780, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_11E6)

    @scena.Lambda('lambda_11F6')
    def lambda_11F6():
        OP_6C(44000, 6000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_11F6)

    @scena.Lambda('lambda_1206')
    def lambda_1206():
        OP_6E(545, 3000)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_1206)

    @scena.Lambda('lambda_1216')
    def lambda_1216():
        ChrWalkTo(0x00FE, -90, 1000, 57450, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_1216)

    Sleep(300)

    @scena.Lambda('lambda_1236')
    def lambda_1236():
        ChrWalkTo(0x00FE, -580, 1000, 56160, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1236)

    Sleep(100)

    @scena.Lambda('lambda_1256')
    def lambda_1256():
        ChrWalkTo(0x00FE, 800, 1000, 55850, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1256)

    WaitForThreadExit(0x0108, 0x0001)
    OP_70(0x0000, 30)
    OP_73(0x0000)
    CreateThread(0x0108, 0x01, 0x00, 0x0004)
    Sleep(400)

    CreateThread(0x0101, 0x01, 0x00, 0x0004)
    Sleep(400)

    CreateThread(0x0102, 0x01, 0x00, 0x0004)
    OP_28(0x004C, 0x01, 0x0001)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T4310._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0x12AC
@scena.Code('func_04_12AC')
def func_04_12AC():
    ChrWalkTo(0x00FE, -90, 1000, 57450, 4500, 0x00)

    @scena.Lambda('lambda_12C6')
    def lambda_12C6():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_12C6)

    ChrWalkTo(0x00FE, -50, 1000, 59720, 4500, 0x00)

    Return()

# id: 0x0005 offset: 0x12E7
@scena.Code('func_05_12E7')
def func_05_12E7():
    ClearMapFlags(0x10000000)
    EventBegin(0x00)
    ClearChrFlags(0x0018, 0x0080)
    ClearChrFlags(0x0019, 0x0080)
    SetChrPos(0x0018, -1440, 1000, 57280, 180)
    SetChrPos(0x0019, 1590, 1000, 57280, 180)
    SetChrChipByIndex(0x0018, 18)
    SetChrChipByIndex(0x0019, 18)
    SetChrSubChip(0x0018, 2)
    SetChrSubChip(0x0019, 2)
    CameraMove(-110, 1000, 51060, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(538, 0)

    @scena.Lambda('lambda_1371')
    def lambda_1371():
        CameraMove(80, 1000, 58940, 8000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1371)

    @scena.Lambda('lambda_1389')
    def lambda_1389():
        OP_6C(0, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1389)

    @scena.Lambda('lambda_1399')
    def lambda_1399():
        OP_6E(346, 9000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1399)

    @scena.Lambda('lambda_13A9')
    def lambda_13A9():
        OP_67(0, 6150, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_13A9)

    Sleep(9000)

    SetMapFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T4311._SN', 106, 0, 0)
    IdleLoop()

    Return()

# id: 0x0006 offset: 0x13D2
@scena.Code('func_06_13D2')
def func_06_13D2():
    EventBegin(0x00)
    SetChrChipByIndex(0x0018, 18)
    SetChrChipByIndex(0x0019, 18)
    SetChrSubChip(0x0018, 2)
    SetChrSubChip(0x0019, 2)
    ClearChrFlags(0x0018, 0x0080)
    ClearChrFlags(0x0019, 0x0080)
    SetChrPos(0x0018, -1440, 1000, 57280, 180)
    SetChrPos(0x0019, 1590, 1000, 57280, 180)
    CameraMove(750, 0, 24130, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(480, 0)

    @scena.Lambda('lambda_1457')
    def lambda_1457():
        OP_6C(333000, 10000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_1457)

    Sleep(1000)

    @scena.Lambda('lambda_146C')
    def lambda_146C():
        CameraMove(-440, 0, 54170, 9000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_146C)

    @scena.Lambda('lambda_1484')
    def lambda_1484():
        OP_67(0, 4770, -10000, 9000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1484)

    @scena.Lambda('lambda_149C')
    def lambda_149C():
        OP_6E(480, 9000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_149C)

    Sleep(9000)

    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T4310._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0007 offset: 0x14B8
@scena.Code('func_07_14B8')
def func_07_14B8():
    EventBegin(0x00)
    SetChrStatus(0x0000, 0xFE, 0)
    SetChrStatus(0x0001, 0xFE, 0)
    SetChrStatus(0x0002, 0xFE, 0)
    SetChrStatus(0x0003, 0xFE, 0)
    SetChrStatus(0x0004, 0xFE, 0)
    SetChrStatus(0x0005, 0xFE, 0)
    SetChrStatus(0x0006, 0xFE, 0)
    SetChrStatus(0x0007, 0xFE, 0)
    CameraMove(260, 1000, 50040, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x001C, 0x0080)
    ClearChrFlags(0x001D, 0x0080)
    ClearChrFlags(0x001F, 0x0080)
    ClearChrFlags(0x001E, 0x0080)
    SetChrPos(0x0101, 130, 1000, 50320, 180)
    SetChrPos(0x0102, 170, 750, 49180, 337)
    SetChrPos(0x0101, 130, 1000, 50320, 180)
    SetChrPos(0x001C, 1300, 1000, 50640, 233)
    SetChrPos(0x001D, -1050, 1000, 51180, 189)
    SetChrPos(0x001F, -2540, 1000, 50100, 137)
    SetChrPos(0x001E, -1560, 500, 48490, 27)
    SetChrPos(0x0108, 1400, 250, 47380, 6)

    ChrTalk(
        0x0101,
        (
            '#000F……约修亚，你要小心哟。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130971V做不到的事情\n',
            '可不能勉强哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130972V#010F嗯，我会小心的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130973V你也要多思考，\n',
            '然后再行动哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130974V不要对自己的能力太自信，\n',
            '要和雪拉姐姐他们齐心协力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯……我知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130976V无论怎样，\n',
            '还是和往常相同的约定！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '平平安安的\n',
            '在格兰赛尔城相会吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F嗯……一定！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '#0060130979V#040F约修亚君。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060130980V现在还不知道在隐藏的水路里\n',
            '会有什么样的魔兽出现。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060130981V因此请你们一定要小心行事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020130982V#010F我知道了。\n',
            '我们会小心谨慎的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x001D,
        (
            '#020F现在已经不用为艾丝蒂尔担心了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030130984V她在经过了这么久的旅行之后\n',
            '已经成长了许多了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030840024V而且不仅是作为游击士，\n',
            '作为一个女人，也是如此哦㈱　　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x001D, 400)

    ChrTalk(
        0x0101,
        (
            '#000F雪、雪拉姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_187E')
    def lambda_187E():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_187E')

    DispatchAsync2(0x001F, 0x0001, lambda_187E)

    ChrTalk(
        0x0102,
        (
            '#010F？？？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130988V怎么啦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#000F不、不知道他们在说什么啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0081040026V#070F呵呵，那么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0081040027V我们这就开始行动吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_191A')
    def lambda_191A():
        ChrWalkTo(0x00FE, 140, 0, 22040, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_191A)

    ChrTalk(
        0x001E,
        (
            '#0041050029V#030F再会吧，小猫咪们㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1959')
    def lambda_1959():
        ChrWalkTo(0x00FE, 140, 0, 22040, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_1959)

    ChrTalk(
        0x0102,
        (
            '#0020130994V#010F愿女神保佑你们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1996')
    def lambda_1996():
        ChrWalkTo(0x00FE, 140, 0, 22040, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1996)

    Sleep(2000)

    ChrTalk(
        0x0101,
        (
            '#000F………约修亚……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x001D, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    ChrMoveTo(0x001D, 700, 1000, 51090, 1000, 0x00)
    OP_63(0x001D)

    ChrTalk(
        0x001D,
        (
            '#020F（公主殿下，您瞧您瞧……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030130997V（那两个孩子在旅途中\n',
            '是不是产生了……呢？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '#0060940015V#040F（……也许是这样的吧。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060130999V（他们两人可以每天\n',
            '这么愉快地在一起……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '（……让我都有那么一点儿羡慕了呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x00CB, 2, 0x65A))
    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/T4100._SN', 100, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

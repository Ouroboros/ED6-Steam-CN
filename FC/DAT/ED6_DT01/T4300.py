import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4300_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4300   ._SN')

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

# id: 0x10001 offset: 0x142
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '中队长',
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
            name                = '特务兵',
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
            name                = '特务兵',
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
            name                = '特务兵',
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
            name                = '特务兵',
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
            name                = '特务兵',
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
            name                = '特务兵',
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
            name                = '特务兵',
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
            name                = '特务兵',
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
            name                = '特务兵',
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
            name                = '特务兵',
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
            name                = '军用犬',
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
            name                = '军用犬',
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
            name                = '军用犬',
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
            name                = '军用犬',
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
            name                = '军用犬',
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
            name                = '亲卫队员',
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
            name                = '亲卫队员',
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
            name                = '亲卫队员',
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
            name                = '亲卫队员',
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
            name                = '科洛丝',
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
            name                = '雪拉',
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
            name                = '奥利维尔',
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
            name                = '奈尔',
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

# id: 0x10002 offset: 0x442
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x442
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x442
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x442
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_453',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_02_4CA)

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
    MapSetFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_05_130F)

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
    Event(0, func_06_13FA)

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
    Event(0, func_07_14E0)

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
    Event(0, func_03_7F1)

    def _loc_4B3(): pass

    label('loc_4B3')

    Jump('loc_4B6')

    def _loc_4B6(): pass

    label('loc_4B6')

    Return()

# id: 0x0001 offset: 0x4B7
@scena.Code('func_01_4B7')
def func_01_4B7():
    OP_16(0x02, 4000, -128000, -96000, 196705)

    Return()

# id: 0x0002 offset: 0x4CA
@scena.Code('func_02_4CA')
def func_02_4CA():
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

    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)

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

    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrSetPos(0x0008, -70, 1000, 50380, 180)
    ChrSetPos(0x0009, 730, 0, 46530, 0)
    ChrSetPos(0x000A, 2350, 0, 46770, 315)
    ChrSetPos(0x000B, 2090, 0, 45430, 332)
    ChrSetPos(0x000C, 1380, 0, 44350, 351)
    ChrSetPos(0x000D, 470, 0, 43290, 7)
    ChrSetPos(0x000E, -920, 0, 43360, 353)
    ChrSetPos(0x000F, -2230, 0, 44390, 7)
    ChrSetPos(0x0010, -1210, 0, 45310, 16)
    ChrSetPos(0x0011, -2029, 0, 46530, 25)
    ChrSetPos(0x0012, -690, 0, 46650, 7)
    ChrSetPos(0x0013, -3190, 0, 43920, 33)
    ChrSetPos(0x0014, -3130, 250, 47070, 62)
    ChrSetPos(0x0015, 3260, 0, 45110, 307)
    ChrSetPos(0x0016, 80, 0, 44910, 349)
    ChrSetPos(0x0017, 1250, 0, 42490, 5)
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
    TalkSetChrName('特务兵们')

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

# id: 0x0003 offset: 0x7F1
@scena.Code('func_03_7F1')
def func_03_7F1():
    EventBegin(0x00)
    OP_6F(0x000D, 120)
    OP_72(0x000D, 0x0010)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    ChrClearFlags(0x001A, 0x0080)
    ChrClearFlags(0x001B, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetChipByIndex(0x0009, 12)
    ChrSetChipByIndex(0x000A, 10)
    ChrSetChipByIndex(0x000B, 10)
    ChrSetChipByIndex(0x000C, 10)
    ChrSetChipByIndex(0x000D, 10)
    ChrSetChipByIndex(0x000E, 10)
    ChrSetChipByIndex(0x0101, 4)
    ChrSetChipByIndex(0x0102, 6)
    ChrSetChipByIndex(0x0108, 8)
    ChrSetPos(0x0108, 70, 0, 26850, 356)
    ChrSetPos(0x0101, -640, 0, 26250, 315)
    ChrSetPos(0x0102, 1000, 0, 26220, 45)
    ChrSetFlags(0x0108, 0x0080)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetPos(0x0018, 9480, 250, 32070, 180)
    ChrSetPos(0x0009, 9490, 250, 31050, 0)
    ChrSetPos(0x0019, 8250, 130, 44870, 46)
    ChrSetPos(0x000A, 7080, 0, 41450, 14)
    ChrSetPos(0x000B, 17790, 0, 47220, 260)
    ChrSetPos(0x001A, -18980, 0, 51590, 180)
    ChrSetPos(0x000C, -19080, 0, 48030, 0)
    ChrSetPos(0x001B, -9790, 210, 47380, 56)
    ChrSetPos(0x000D, -19320, 0, 41420, 44)
    ChrSetPos(0x000E, -17850, 20, 41630, 80)
    FadeIn(2000, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(278000, 0)
    OP_6E(288, 0)
    Fade(1000)
    CameraMove(9140, 250, 31570, 0)

    @scena.Lambda('lambda_099B')
    def lambda_099B():
        OP_6C(314000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_099B)

    ChrSetChipByIndex(0x0018, 18)
    ChrSetSubChip(0x0018, 1)
    PlaySE(501, 0x00, 0x64)
    ChrSetFlags(0x0009, 0x0020)

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_09CA')
    def lambda_09CA():
        OP_9E(0x00FE, 30, 0, 1000, 3000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_09CA)

    @scena.Lambda('lambda_09E4')
    def lambda_09E4():
        OP_9E(0x00FE, 30, 0, 1000, 3000)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_09E4)

    Sleep(1000)

    @scena.Lambda('lambda_0A03')
    def lambda_0A03():
        OP_99(0x0009, 0x02, 0x07, 2500)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0A03)

    Sleep(100)

    ChrSetChipByIndex(0x0018, 17)
    ChrJumpTo(0x0018, 9490, 250, 32990, 1000, 8000)
    PlaySE(164, 0x00, 0x64)
    ChrSetFlags(0x0018, 0x0020)

    @scena.Lambda('lambda_0A3E')
    def lambda_0A3E():
        ChrWalkTo(0x0018, 9470, 250, 31940, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_0A3E)

    Sleep(50)

    ChrSetChipByIndex(0x0018, 18)
    PlaySE(501, 0x00, 0x64)
    ChrSetSubChip(0x0018, 0)
    Sleep(50)

    ChrSetSubChip(0x0018, 1)
    Sleep(50)

    ChrSetSubChip(0x0018, 2)
    ChrJumpTo(0x0009, 9460, 250, 29930, 1000, 8000)
    PlaySE(164, 0x00, 0x64)

    @scena.Lambda('lambda_0A9D')
    def lambda_0A9D():
        OP_99(0x0009, 0x00, 0x02, 2000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0A9D)

    ChrWalkTo(0x0009, 9470, 250, 31130, 7000, 0x00)
    ChrSetSubChip(0x0018, 1)
    PlaySE(501, 0x00, 0x64)

    @scena.Lambda('lambda_0ACB')
    def lambda_0ACB():
        OP_9E(0x00FE, 30, 0, 1000, 3000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0ACB)

    @scena.Lambda('lambda_0AE5')
    def lambda_0AE5():
        OP_9E(0x00FE, 30, 0, 1000, 3000)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_0AE5)

    Sleep(500)

    Fade(1000)
    CameraMove(7760, 0, 43410, 0)
    OP_6E(330, 0)

    @scena.Lambda('lambda_0B23')
    def lambda_0B23():
        OP_6E(262, 5000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_0B23)

    @scena.Lambda('lambda_0B33')
    def lambda_0B33():
        CameraMove(11360, 0, 49140, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0B33)

    @scena.Lambda('lambda_0B4B')
    def lambda_0B4B():
        ChrTurnDirection(0x00FE, 0x0019, 0)
        Yield()

        Jump('lambda_0B4B')

    DispatchAsync2(0x000A, 0x0002, lambda_0B4B)

    ChrSetFlags(0x0019, 0x0040)
    ChrSetFlags(0x000B, 0x0040)
    ChrSetFlags(0x000B, 0x0040)
    ChrSetChipByIndex(0x000A, 11)
    ChrSetChipByIndex(0x000B, 11)

    @scena.Lambda('lambda_0B75')
    def lambda_0B75():
        ChrWalkTo(0x00FE, 15330, 250, 47290, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0B75)

    @scena.Lambda('lambda_0B90')
    def lambda_0B90():
        ChrWalkTo(0x00FE, 8890, 230, 46350, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0B90)

    @scena.Lambda('lambda_0BAB')
    def lambda_0BAB():
        ChrWalkTo(0x00FE, 10020, 250, 47350, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_0BAB)

    WaitForThreadExit(0x0019, 0x0001)

    @scena.Lambda('lambda_0BCB')
    def lambda_0BCB():
        ChrWalkTo(0x00FE, 11360, 0, 49430, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_0BCB)

    WaitForThreadExit(0x0019, 0x0001)
    ChrSetChipByIndex(0x0019, 18)
    ChrSetSubChip(0x0019, 2)
    ChrSetFlags(0x0019, 0x0020)
    ChrTurnDirection(0x0019, 0x000A, 800)
    Sleep(200)

    @scena.Lambda('lambda_0C06')
    def lambda_0C06():
        OP_92(0x00FE, 0x0019, 1000, 400, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0C06)

    @scena.Lambda('lambda_0C1B')
    def lambda_0C1B():
        OP_92(0x00FE, 0x0019, 1000, 800, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0C1B)

    Sleep(300)

    ChrTurnDirection(0x0019, 0x000B, 800)
    ChrSetFlags(0x000B, 0x0020)

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

    @scena.Lambda('lambda_0C55')
    def lambda_0C55():
        OP_99(0x00FE, 0x03, 0x07, 1000)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_0C55)

    @scena.Lambda('lambda_0C65')
    def lambda_0C65():
        ChrWalkTo(0x00FE, 12240, 0, 48490, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0C65)

    Sleep(100)

    @scena.Lambda('lambda_0C85')
    def lambda_0C85():
        ChrWalkTo(0x00FE, 10290, 40, 47930, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0C85)

    Sleep(200)

    ChrSetFlags(0x0019, 0x0004)
    ChrSetSubChip(0x0019, 1)

    @scena.Lambda('lambda_0CAF')
    def lambda_0CAF():
        OP_97(0x00FE, 11990, 49260, 230000, 9400, 0x0001)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_0CAF)

    Sleep(250)

    PlaySE(553, 0x00, 0x64)

    @scena.Lambda('lambda_0CD5')
    def lambda_0CD5():
        ChrMoveTo(0x00FE, 11020, 250, 46930, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0CD5)

    Sleep(100)

    @scena.Lambda('lambda_0CF5')
    def lambda_0CF5():
        ChrJumpTo(0x00FE, 9200, 0, 47750, 600, 7000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0CF5)

    ChrClearFlags(0x0019, 0x0020)
    ChrClearFlags(0x0019, 0x0004)
    ChrSetChipByIndex(0x0019, 17)

    @scena.Lambda('lambda_0D22')
    def lambda_0D22():
        ChrWalkTo(0x00FE, 20480, 0, 46180, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_0D22)

    Sleep(500)

    @scena.Lambda('lambda_0D42')
    def lambda_0D42():
        OP_92(0x00FE, 0x0019, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0D42)

    Sleep(500)

    @scena.Lambda('lambda_0D5C')
    def lambda_0D5C():
        OP_92(0x00FE, 0x0019, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0D5C)

    Sleep(100)

    ChrClearFlags(0x000B, 0x0020)
    ChrWalkTo(0x000B, 11130, 0, 48250, 5000, 0x00)

    @scena.Lambda('lambda_0D8F')
    def lambda_0D8F():
        OP_92(0x00FE, 0x0019, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0D8F)

    @scena.Lambda('lambda_0DA4')
    def lambda_0DA4():
        OP_92(0x00FE, 0x0019, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0DA4)

    Sleep(500)

    Fade(1000)
    CameraMove(-19190, 0, 50360, 0)
    ChrSetChipByIndex(0x000C, 11)

    @scena.Lambda('lambda_0DD9')
    def lambda_0DD9():
        CameraMove(-19700, 0, 53190, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0DD9)

    OP_92(0x000C, 0x001A, 600, 6000, 0x00)

    @scena.Lambda('lambda_0DFF')
    def lambda_0DFF():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 2000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0DFF)

    ChrMoveToRelativeAsync(0x001A, 0, 0, 2000, 2000, 0x00)
    ChrSetFlags(0x001A, 0x0020)
    ChrSetChipByIndex(0x001A, 18)
    ChrSetSubChip(0x001A, 1)

    @scena.Lambda('lambda_0E3D')
    def lambda_0E3D():
        OP_9E(0x00FE, 30, 0, 700, 3000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0E3D)

    @scena.Lambda('lambda_0E57')
    def lambda_0E57():
        OP_9E(0x00FE, 30, 0, 700, 3000)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_0E57)

    Sleep(700)

    @scena.Lambda('lambda_0E76')
    def lambda_0E76():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_0E76')

    DispatchAsync2(0x001A, 0x0001, lambda_0E76)

    @scena.Lambda('lambda_0E87')
    def lambda_0E87():
        ChrMoveTo(0x00FE, -19520, 0, 53650, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0002, lambda_0E87)

    ChrSetFlags(0x000C, 0x0004)
    ChrSetFlags(0x000C, 0x0040)
    ChrMoveToRelativeAsync(0x000C, 0, 0, 400, 5000, 0x00)
    ChrSetChipByIndex(0x001A, 17)
    PlaySE(520, 0x00, 0x64)
    OP_97(0x000C, -19520, 53650, -100000, 9000, 0x0002)
    ChrSetChipByIndex(0x001A, 18)
    ChrSetSubChip(0x001A, 2)
    ChrJumpTo(0x000C, -20930, -4000, 56530, 200, 10000)
    PlaySE(179, 0x00, 0x64)
    TerminateThread(0x001A, 0xFF)
    ChrSetChipByIndex(0x000D, 11)

    @scena.Lambda('lambda_0F0E')
    def lambda_0F0E():
        ChrWalkTo(0x00FE, -19640, 0, 48710, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_0F0E)

    Sleep(500)

    @scena.Lambda('lambda_0F2E')
    def lambda_0F2E():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_0F2E)

    @scena.Lambda('lambda_0F3C')
    def lambda_0F3C():
        CameraMove(-19190, 0, 50360, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0F3C)

    @scena.Lambda('lambda_0F54')
    def lambda_0F54():
        OP_6E(305, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0F54)

    ChrSetChipByIndex(0x000E, 11)

    @scena.Lambda('lambda_0F69')
    def lambda_0F69():
        ChrWalkTo(0x00FE, -18180, 0, 48630, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0F69)

    Sleep(1500)

    @scena.Lambda('lambda_0F89')
    def lambda_0F89():
        ChrTurnDirection(0x00FE, 0x000E, 0)
        Yield()

        Jump('lambda_0F89')

    DispatchAsync2(0x001A, 0x0001, lambda_0F89)

    @scena.Lambda('lambda_0F9A')
    def lambda_0F9A():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 4000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_0F9A)

    Sleep(200)

    @scena.Lambda('lambda_0FBA')
    def lambda_0FBA():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 4000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0FBA)

    Sleep(300)

    @scena.Lambda('lambda_0FDA')
    def lambda_0FDA():
        ChrWalkTo(0x00FE, -17510, 0, 48700, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_0FDA)

    Sleep(500)

    @scena.Lambda('lambda_0FFA')
    def lambda_0FFA():
        ChrTurnDirection(0x00FE, 0x001B, 800)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0FFA)

    @scena.Lambda('lambda_1008')
    def lambda_1008():
        ChrTurnDirection(0x00FE, 0x001B, 800)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1008)

    Sleep(200)

    @scena.Lambda('lambda_101B')
    def lambda_101B():
        ChrJumpTo(0x00FE, -17510, 0, 48700, 2000, 5000)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_101B)

    ChrSetFlags(0x001B, 0x0020)
    ChrSetChipByIndex(0x001B, 18)
    ChrSetSubChip(0x001B, 0)
    Sleep(300)

    PlaySE(501, 0x00, 0x64)
    ChrSetSubChip(0x001B, 1)
    Sleep(50)

    ChrSetSubChip(0x001B, 2)
    ChrJumpTo(0x000E, -18870, 0, 47400, 1000, 6000)
    PlaySE(164, 0x00, 0x64)
    Sleep(100)

    @scena.Lambda('lambda_1082')
    def lambda_1082():
        ChrMoveTo(0x00FE, -19580, 0, 46820, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1082)

    @scena.Lambda('lambda_109D')
    def lambda_109D():
        ChrMoveTo(0x00FE, -20250, 0, 49620, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_109D)

    ChrSetChipByIndex(0x001A, 17)
    ChrClearFlags(0x001A, 0x0020)
    ChrSetFlags(0x001A, 0x0004)
    ChrMoveTo(0x001A, -18520, 0, 51440, 4000, 0x00)
    ChrJumpTo(0x001A, -16410, 0, 49120, 1000, 7000)
    PlaySE(164, 0x00, 0x64)
    ChrMoveTo(0x001A, -17150, 0, 47680, 2000, 0x00)
    ChrSetChipByIndex(0x001A, 18)
    ChrSetSubChip(0x001A, 2)
    Fade(1000)
    ChrClearFlags(0x0108, 0x0080)
    ChrClearFlags(0x0101, 0x0080)
    ChrClearFlags(0x0102, 0x0080)
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

    @scena.Lambda('lambda_11DE')
    def lambda_11DE():
        CameraMove(-60, 1000, 57500, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_11DE)

    @scena.Lambda('lambda_11F6')
    def lambda_11F6():
        OP_67(0, 5710, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_11F6)

    @scena.Lambda('lambda_120E')
    def lambda_120E():
        CameraSetDistance(1780, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_120E)

    @scena.Lambda('lambda_121E')
    def lambda_121E():
        OP_6C(44000, 6000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_121E)

    @scena.Lambda('lambda_122E')
    def lambda_122E():
        OP_6E(545, 3000)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_122E)

    @scena.Lambda('lambda_123E')
    def lambda_123E():
        ChrWalkTo(0x00FE, -90, 1000, 57450, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_123E)

    Sleep(300)

    @scena.Lambda('lambda_125E')
    def lambda_125E():
        ChrWalkTo(0x00FE, -580, 1000, 56160, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_125E)

    Sleep(100)

    @scena.Lambda('lambda_127E')
    def lambda_127E():
        ChrWalkTo(0x00FE, 800, 1000, 55850, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_127E)

    WaitForThreadExit(0x0108, 0x0001)
    OP_70(0x0000, 30)
    OP_73(0x0000)
    CreateThread(0x0108, 0x01, 0x00, func_04_12D4)
    Sleep(400)

    CreateThread(0x0101, 0x01, 0x00, func_04_12D4)
    Sleep(400)

    CreateThread(0x0102, 0x01, 0x00, func_04_12D4)
    OP_28(0x004C, 0x01, 0x0001)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T4310._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0x12D4
@scena.Code('func_04_12D4')
def func_04_12D4():
    ChrWalkTo(0x00FE, -90, 1000, 57450, 4500, 0x00)

    @scena.Lambda('lambda_12EE')
    def lambda_12EE():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_12EE)

    ChrWalkTo(0x00FE, -50, 1000, 59720, 4500, 0x00)

    Return()

# id: 0x0005 offset: 0x130F
@scena.Code('func_05_130F')
def func_05_130F():
    MapClearFlags(0x10000000)
    EventBegin(0x00)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    ChrSetPos(0x0018, -1440, 1000, 57280, 180)
    ChrSetPos(0x0019, 1590, 1000, 57280, 180)
    ChrSetChipByIndex(0x0018, 18)
    ChrSetChipByIndex(0x0019, 18)
    ChrSetSubChip(0x0018, 2)
    ChrSetSubChip(0x0019, 2)
    CameraMove(-110, 1000, 51060, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(538, 0)

    @scena.Lambda('lambda_1399')
    def lambda_1399():
        CameraMove(80, 1000, 58940, 8000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1399)

    @scena.Lambda('lambda_13B1')
    def lambda_13B1():
        OP_6C(0, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_13B1)

    @scena.Lambda('lambda_13C1')
    def lambda_13C1():
        OP_6E(346, 9000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_13C1)

    @scena.Lambda('lambda_13D1')
    def lambda_13D1():
        OP_67(0, 6150, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_13D1)

    Sleep(9000)

    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T4311._SN', 106, 0, 0)
    IdleLoop()

    Return()

# id: 0x0006 offset: 0x13FA
@scena.Code('func_06_13FA')
def func_06_13FA():
    EventBegin(0x00)
    ChrSetChipByIndex(0x0018, 18)
    ChrSetChipByIndex(0x0019, 18)
    ChrSetSubChip(0x0018, 2)
    ChrSetSubChip(0x0019, 2)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    ChrSetPos(0x0018, -1440, 1000, 57280, 180)
    ChrSetPos(0x0019, 1590, 1000, 57280, 180)
    CameraMove(750, 0, 24130, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(480, 0)

    @scena.Lambda('lambda_147F')
    def lambda_147F():
        OP_6C(333000, 10000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_147F)

    Sleep(1000)

    @scena.Lambda('lambda_1494')
    def lambda_1494():
        CameraMove(-440, 0, 54170, 9000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1494)

    @scena.Lambda('lambda_14AC')
    def lambda_14AC():
        OP_67(0, 4770, -10000, 9000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_14AC)

    @scena.Lambda('lambda_14C4')
    def lambda_14C4():
        OP_6E(480, 9000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_14C4)

    Sleep(9000)

    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T4310._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0007 offset: 0x14E0
@scena.Code('func_07_14E0')
def func_07_14E0():
    EventBegin(0x00)
    ChrSetStatus(0x0000, 0xFE, 0)
    ChrSetStatus(0x0001, 0xFE, 0)
    ChrSetStatus(0x0002, 0xFE, 0)
    ChrSetStatus(0x0003, 0xFE, 0)
    ChrSetStatus(0x0004, 0xFE, 0)
    ChrSetStatus(0x0005, 0xFE, 0)
    ChrSetStatus(0x0006, 0xFE, 0)
    ChrSetStatus(0x0007, 0xFE, 0)
    CameraMove(260, 1000, 50040, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    ChrClearFlags(0x001C, 0x0080)
    ChrClearFlags(0x001D, 0x0080)
    ChrClearFlags(0x001F, 0x0080)
    ChrClearFlags(0x001E, 0x0080)
    ChrSetPos(0x0101, 130, 1000, 50320, 180)
    ChrSetPos(0x0102, 170, 750, 49180, 337)
    ChrSetPos(0x0101, 130, 1000, 50320, 180)
    ChrSetPos(0x001C, 1300, 1000, 50640, 233)
    ChrSetPos(0x001D, -1050, 1000, 51180, 189)
    ChrSetPos(0x001F, -2540, 1000, 50100, 137)
    ChrSetPos(0x001E, -1560, 500, 48490, 27)
    ChrSetPos(0x0108, 1400, 250, 47380, 6)

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

    @scena.Lambda('lambda_18DD')
    def lambda_18DD():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_18DD')

    DispatchAsync2(0x001F, 0x0001, lambda_18DD)

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

    @scena.Lambda('lambda_1988')
    def lambda_1988():
        ChrWalkTo(0x00FE, 140, 0, 22040, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_1988)

    ChrTalk(
        0x001E,
        (
            '#0041050029V#030F再会吧，小猫咪们㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_19CC')
    def lambda_19CC():
        ChrWalkTo(0x00FE, 140, 0, 22040, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_19CC)

    ChrTalk(
        0x0102,
        (
            '#0020130994V#010F愿女神保佑你们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1A0E')
    def lambda_1A0E():
        ChrWalkTo(0x00FE, 140, 0, 22040, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1A0E)

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

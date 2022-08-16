import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4302_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4302   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4302.x'
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
        ('ED6_DT07/CH01330._CH', 'ED6_DT07/CH01330P._CP'),
        ('ED6_DT07/CH01610._CH', 'ED6_DT07/CH01610P._CP'),
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
            dword_10            = 3,
            chipIndex           = 3,
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
            dword_10            = 3,
            chipIndex           = 3,
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
            dword_10            = 3,
            chipIndex           = 3,
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
            dword_10            = 3,
            chipIndex           = 3,
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
            name                = '雪拉扎德',
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
        ScenaActorData(
            triggerX            = 0,
            triggerZ            = 1000,
            triggerY            = 20390,
            triggerRange        = 1000,
            actorX              = 0,
            actorZ              = 1000,
            actorY              = 20390,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x466
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_477',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_02_4F7)

    Jump('loc_4E3')

    def _loc_477(): pass

    label('loc_477')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_488',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, func_05_1137)

    Jump('loc_4E3')

    def _loc_488(): pass

    label('loc_488')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 4, 0x3FC)),
            Expr.Return,
        ),
        'loc_4A2',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x65),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    Event(0, func_06_1218)

    Jump('loc_4E3')

    def _loc_4A2(): pass

    label('loc_4A2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 5, 0x3FD)),
            Expr.Return,
        ),
        'loc_4C1',
    )

    MapSetFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x65),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007F, 5, 0x3FD))
    Event(0, func_07_1312)

    Jump('loc_4E3')

    def _loc_4C1(): pass

    label('loc_4C1')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_4CD'),
        (-1, 'loc_4E3'),
    )

    def _loc_4CD(): pass

    label('loc_4CD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 2, 0x652)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 1, 0x651)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4E0',
    )

    SetScenaFlags(ScenaFlag(0x00CA, 2, 0x652))
    Event(0, func_03_779)

    def _loc_4E0(): pass

    label('loc_4E0')

    Jump('loc_4E3')

    def _loc_4E3(): pass

    label('loc_4E3')

    Return()

# id: 0x0001 offset: 0x4E4
@scena.Code('func_01_4E4')
def func_01_4E4():
    OP_16(0x02, 4000, -128000, -96000, 196705)

    Return()

# id: 0x0002 offset: 0x4F7
@scena.Code('func_02_4F7')
def func_02_4F7():
    EventBegin(0x00)
    CameraMove(-70, 0, 20900, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(0, 0)
    OP_6E(408, 0)

    @scena.Lambda('lambda_053C')
    def lambda_053C():
        CameraMove(-700, 0, 46980, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_053C)

    @scena.Lambda('lambda_0554')
    def lambda_0554():
        OP_6C(314000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0554)

    @scena.Lambda('lambda_0564')
    def lambda_0564():
        OP_6E(262, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0564)

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
            '立刻前往现场，\n',
            '借此机会将他们全部剿灭！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/C4103._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x779
@scena.Code('func_03_779')
def func_03_779():
    EventBegin(0x00)
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

    @scena.Lambda('lambda_0908')
    def lambda_0908():
        OP_6C(314000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0908)

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

    @scena.Lambda('lambda_0928')
    def lambda_0928():
        OP_9E(0x00FE, 30, 0, 1000, 3000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0928)

    @scena.Lambda('lambda_0942')
    def lambda_0942():
        OP_9E(0x00FE, 30, 0, 1000, 3000)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_0942)

    Sleep(1000)

    @scena.Lambda('lambda_0961')
    def lambda_0961():
        OP_99(0x0009, 0x02, 0x07, 2500)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0961)

    Sleep(100)

    ChrJumpTo(0x0018, 9490, 250, 32990, 1000, 8000)
    ChrWalkTo(0x0018, 9470, 250, 31940, 7000, 0x00)
    ChrJumpTo(0x0009, 9460, 250, 29930, 1000, 8000)

    @scena.Lambda('lambda_09B8')
    def lambda_09B8():
        OP_99(0x0009, 0x00, 0x02, 2000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_09B8)

    ChrWalkTo(0x0009, 9470, 250, 31130, 7000, 0x00)

    @scena.Lambda('lambda_09DC')
    def lambda_09DC():
        OP_9E(0x00FE, 30, 0, 1000, 3000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_09DC)

    @scena.Lambda('lambda_09F6')
    def lambda_09F6():
        OP_9E(0x00FE, 30, 0, 1000, 3000)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_09F6)

    Sleep(500)

    Fade(1000)
    CameraMove(7760, 0, 43410, 0)
    OP_6E(330, 0)

    @scena.Lambda('lambda_0A34')
    def lambda_0A34():
        OP_6E(262, 5000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_0A34)

    @scena.Lambda('lambda_0A44')
    def lambda_0A44():
        CameraMove(11360, 0, 49140, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0A44)

    @scena.Lambda('lambda_0A5C')
    def lambda_0A5C():
        ChrTurnDirection(0x00FE, 0x0019, 0)
        Yield()

        Jump('lambda_0A5C')

    DispatchAsync2(0x000A, 0x0002, lambda_0A5C)

    ChrSetFlags(0x0019, 0x0040)
    ChrSetFlags(0x000B, 0x0040)
    ChrSetFlags(0x000B, 0x0040)
    ChrSetChipByIndex(0x000A, 11)
    ChrSetChipByIndex(0x000B, 11)

    @scena.Lambda('lambda_0A86')
    def lambda_0A86():
        ChrWalkTo(0x00FE, 15330, 250, 47290, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0A86)

    @scena.Lambda('lambda_0AA1')
    def lambda_0AA1():
        ChrWalkTo(0x00FE, 8890, 230, 46350, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0AA1)

    @scena.Lambda('lambda_0ABC')
    def lambda_0ABC():
        ChrWalkTo(0x00FE, 10020, 250, 47350, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_0ABC)

    WaitForThreadExit(0x0019, 0x0001)

    @scena.Lambda('lambda_0ADC')
    def lambda_0ADC():
        ChrWalkTo(0x00FE, 11360, 0, 49430, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_0ADC)

    WaitForThreadExit(0x0019, 0x0001)
    ChrTurnDirection(0x0019, 0x000A, 800)
    Sleep(200)

    @scena.Lambda('lambda_0B08')
    def lambda_0B08():
        OP_92(0x00FE, 0x0019, 1000, 400, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0B08)

    @scena.Lambda('lambda_0B1D')
    def lambda_0B1D():
        OP_92(0x00FE, 0x0019, 1000, 800, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0B1D)

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

    @scena.Lambda('lambda_0B57')
    def lambda_0B57():
        OP_99(0x00FE, 0x03, 0x07, 1000)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_0B57)

    @scena.Lambda('lambda_0B67')
    def lambda_0B67():
        ChrWalkTo(0x00FE, 12240, 0, 48490, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0B67)

    Sleep(100)

    @scena.Lambda('lambda_0B87')
    def lambda_0B87():
        ChrWalkTo(0x00FE, 10290, 40, 47930, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0B87)

    Sleep(200)

    ChrSetFlags(0x0019, 0x0004)

    @scena.Lambda('lambda_0BAC')
    def lambda_0BAC():
        OP_97(0x00FE, 11990, 49260, 230000, 9400, 0x0001)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_0BAC)

    Sleep(250)

    @scena.Lambda('lambda_0BCD')
    def lambda_0BCD():
        ChrMoveTo(0x00FE, 11020, 250, 46930, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0BCD)

    Sleep(100)

    @scena.Lambda('lambda_0BED')
    def lambda_0BED():
        ChrJumpTo(0x00FE, 9200, 0, 47750, 600, 7000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0BED)

    ChrClearFlags(0x0019, 0x0004)

    @scena.Lambda('lambda_0C10')
    def lambda_0C10():
        ChrWalkTo(0x00FE, 20480, 0, 46180, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_0C10)

    Sleep(500)

    @scena.Lambda('lambda_0C30')
    def lambda_0C30():
        OP_92(0x00FE, 0x0019, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0C30)

    Sleep(500)

    @scena.Lambda('lambda_0C4A')
    def lambda_0C4A():
        OP_92(0x00FE, 0x0019, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0C4A)

    Sleep(100)

    ChrClearFlags(0x000B, 0x0020)
    ChrWalkTo(0x000B, 11130, 0, 48250, 5000, 0x00)

    @scena.Lambda('lambda_0C7D')
    def lambda_0C7D():
        OP_92(0x00FE, 0x0019, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0C7D)

    @scena.Lambda('lambda_0C92')
    def lambda_0C92():
        OP_92(0x00FE, 0x0019, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0C92)

    Sleep(500)

    Fade(1000)
    CameraMove(-19190, 0, 50360, 0)
    ChrSetChipByIndex(0x000C, 11)

    @scena.Lambda('lambda_0CC7')
    def lambda_0CC7():
        CameraMove(-19700, 0, 53190, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0CC7)

    OP_92(0x000C, 0x001A, 600, 6000, 0x00)

    @scena.Lambda('lambda_0CED')
    def lambda_0CED():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 2000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0CED)

    ChrMoveToRelativeAsync(0x001A, 0, 0, 2000, 2000, 0x00)

    @scena.Lambda('lambda_0D1C')
    def lambda_0D1C():
        OP_9E(0x00FE, 30, 0, 700, 3000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0D1C)

    @scena.Lambda('lambda_0D36')
    def lambda_0D36():
        OP_9E(0x00FE, 30, 0, 700, 3000)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_0D36)

    Sleep(700)

    @scena.Lambda('lambda_0D55')
    def lambda_0D55():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_0D55')

    DispatchAsync2(0x001A, 0x0001, lambda_0D55)

    @scena.Lambda('lambda_0D66')
    def lambda_0D66():
        ChrMoveTo(0x00FE, -19520, 0, 53650, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0002, lambda_0D66)

    ChrSetFlags(0x000C, 0x0004)
    ChrSetFlags(0x000C, 0x0040)
    ChrMoveToRelativeAsync(0x000C, 0, 0, 400, 5000, 0x00)
    OP_97(0x000C, -19520, 53650, -100000, 9000, 0x0002)
    ChrJumpTo(0x000C, -20930, -4000, 56530, 200, 10000)
    TerminateThread(0x001A, 0xFF)
    ChrSetChipByIndex(0x000D, 11)

    @scena.Lambda('lambda_0DD4')
    def lambda_0DD4():
        ChrWalkTo(0x00FE, -19640, 0, 48710, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_0DD4)

    Sleep(500)

    @scena.Lambda('lambda_0DF4')
    def lambda_0DF4():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_0DF4)

    @scena.Lambda('lambda_0E02')
    def lambda_0E02():
        CameraMove(-19190, 0, 50360, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0E02)

    @scena.Lambda('lambda_0E1A')
    def lambda_0E1A():
        OP_6E(305, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0E1A)

    ChrSetChipByIndex(0x000E, 11)

    @scena.Lambda('lambda_0E2F')
    def lambda_0E2F():
        ChrWalkTo(0x00FE, -18180, 0, 48630, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0E2F)

    Sleep(1500)

    @scena.Lambda('lambda_0E4F')
    def lambda_0E4F():
        ChrTurnDirection(0x00FE, 0x000E, 0)
        Yield()

        Jump('lambda_0E4F')

    DispatchAsync2(0x001A, 0x0001, lambda_0E4F)

    @scena.Lambda('lambda_0E60')
    def lambda_0E60():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 4000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_0E60)

    Sleep(200)

    @scena.Lambda('lambda_0E80')
    def lambda_0E80():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 4000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0E80)

    Sleep(300)

    @scena.Lambda('lambda_0EA0')
    def lambda_0EA0():
        ChrWalkTo(0x00FE, -17510, 0, 48700, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_0EA0)

    Sleep(500)

    @scena.Lambda('lambda_0EC0')
    def lambda_0EC0():
        ChrTurnDirection(0x00FE, 0x001B, 800)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0EC0)

    @scena.Lambda('lambda_0ECE')
    def lambda_0ECE():
        ChrTurnDirection(0x00FE, 0x001B, 800)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_0ECE)

    Sleep(400)

    ChrJumpTo(0x000E, -18870, 0, 47400, 1000, 6000)
    Sleep(100)

    @scena.Lambda('lambda_0EFD')
    def lambda_0EFD():
        ChrMoveTo(0x00FE, -19580, 0, 46820, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0EFD)

    @scena.Lambda('lambda_0F18')
    def lambda_0F18():
        ChrMoveTo(0x00FE, -20250, 0, 49620, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_0F18)

    ChrSetFlags(0x001A, 0x0004)
    ChrMoveTo(0x001A, -18520, 0, 51440, 4000, 0x00)
    ChrJumpTo(0x001A, -16410, 0, 49120, 1000, 7000)
    ChrMoveTo(0x001A, -17150, 0, 47680, 2000, 0x00)
    Fade(1000)
    CameraMove(110, 0, 26870, 0)
    OP_6C(326000, 0)

    ChrTalk(
        0x0108,
        (
            '#070F好呀好呀……正在交战呢。\n',
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
            '#000FＯＫ！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F明白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1006')
    def lambda_1006():
        CameraMove(-60, 1000, 57500, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1006)

    @scena.Lambda('lambda_101E')
    def lambda_101E():
        OP_67(0, 5710, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_101E)

    @scena.Lambda('lambda_1036')
    def lambda_1036():
        CameraSetDistance(1780, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_1036)

    @scena.Lambda('lambda_1046')
    def lambda_1046():
        OP_6C(44000, 6000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_1046)

    @scena.Lambda('lambda_1056')
    def lambda_1056():
        OP_6E(545, 3000)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_1056)

    @scena.Lambda('lambda_1066')
    def lambda_1066():
        ChrWalkTo(0x00FE, -90, 1000, 57450, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_1066)

    Sleep(300)

    @scena.Lambda('lambda_1086')
    def lambda_1086():
        ChrWalkTo(0x00FE, -580, 1000, 56160, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1086)

    Sleep(100)

    @scena.Lambda('lambda_10A6')
    def lambda_10A6():
        ChrWalkTo(0x00FE, 800, 1000, 55850, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_10A6)

    WaitForThreadExit(0x0108, 0x0001)
    OP_70(0x0000, 30)
    OP_73(0x0000)
    CreateThread(0x0108, 0x01, 0x00, func_04_10FC)
    Sleep(400)

    CreateThread(0x0101, 0x01, 0x00, func_04_10FC)
    Sleep(400)

    CreateThread(0x0102, 0x01, 0x00, func_04_10FC)
    OP_28(0x004C, 0x01, 0x0001)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T4310._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0x10FC
@scena.Code('func_04_10FC')
def func_04_10FC():
    ChrWalkTo(0x00FE, -90, 1000, 57450, 4500, 0x00)

    @scena.Lambda('lambda_1116')
    def lambda_1116():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1116)

    ChrWalkTo(0x00FE, -50, 1000, 59720, 4500, 0x00)

    Return()

# id: 0x0005 offset: 0x1137
@scena.Code('func_05_1137')
def func_05_1137():
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

    @scena.Lambda('lambda_11BC')
    def lambda_11BC():
        CameraMove(80, 1000, 58940, 8000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_11BC)

    @scena.Lambda('lambda_11D4')
    def lambda_11D4():
        OP_6C(0, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_11D4)

    @scena.Lambda('lambda_11E4')
    def lambda_11E4():
        OP_6E(346, 9000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_11E4)

    @scena.Lambda('lambda_11F4')
    def lambda_11F4():
        OP_67(0, 6150, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_11F4)

    Sleep(9000)

    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T4313._SN', 106, 0, 0)
    IdleLoop()

    Return()

# id: 0x0006 offset: 0x1218
@scena.Code('func_06_1218')
def func_06_1218():
    EventBegin(0x00)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x0108, 0x0080)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    ChrSetPos(0x0018, -1440, 1000, 57280, 180)
    ChrSetPos(0x0019, 1590, 1000, 57280, 180)
    ChrSetChipByIndex(0x0018, 18)
    ChrSetChipByIndex(0x0019, 18)
    ChrSetSubChip(0x0018, 2)
    ChrSetSubChip(0x0019, 2)
    CameraMove(750, 0, 24130, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(480, 0)

    @scena.Lambda('lambda_12AC')
    def lambda_12AC():
        OP_6C(333000, 10000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_12AC)

    Sleep(1000)

    @scena.Lambda('lambda_12C1')
    def lambda_12C1():
        CameraMove(-440, 0, 54170, 9000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_12C1)

    @scena.Lambda('lambda_12D9')
    def lambda_12D9():
        OP_67(0, 4770, -10000, 9000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_12D9)

    @scena.Lambda('lambda_12F1')
    def lambda_12F1():
        OP_6E(480, 9000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_12F1)

    Sleep(9000)

    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T4312._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0007 offset: 0x1312
@scena.Code('func_07_1312')
def func_07_1312():
    MapClearFlags(0x10000000)
    MapClearFlags(0x02000000)
    EventBegin(0x00)
    CameraMove(260, 1000, 50040, 0)
    OP_67(0, 6530, -10000, 0)
    CameraSetDistance(1570, 0)
    OP_6C(44000, 0)
    OP_6E(510, 0)
    ChrSetStatus(0x0000, 0xFE, 0)
    ChrSetStatus(0x0001, 0xFE, 0)
    ChrSetStatus(0x0002, 0xFE, 0)
    ChrSetStatus(0x0003, 0xFE, 0)
    ChrSetStatus(0x0004, 0xFE, 0)
    ChrSetStatus(0x0005, 0xFE, 0)
    ChrSetStatus(0x0006, 0xFE, 0)
    ChrSetStatus(0x0007, 0xFE, 0)
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
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010130970V#505F#5P……约修亚，你要小心哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130971V做不到的事情可不能勉强哦。\n',
            '　',
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
            '#0020130973V你也要谨慎行事哦。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130974V不要对自己的能力太自信，\n',
            '要和雪拉姐姐她们齐心协力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130975V#006F嗯……我知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130976V不管怎么说，\n',
            '我们还有上次的约定呢！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130977V#001F平平安安地在格兰赛尔城相会吧！\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130978V#019F嗯……一定！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '#0060130979V#040F约修亚。',
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
            '#0020130982V#010F好的。\n',
            '我们会小心谨慎的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x001D,
        (
            '#0030130983V#021F现在已经不用为艾丝蒂尔担心了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030130984V她在经过了这么久的修炼旅行之后\n',
            '已经成长了许多。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030130985V#027F而且不仅是作为一名游击士，\n',
            '作为一个女性，也是如此哦㈱　　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrTurnDirection(0x0101, 0x001D, 400)

    ChrTalk(
        0x0101,
        (
            '#0010130986V#503F雪、雪拉姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1786')
    def lambda_1786():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_1786')

    DispatchAsync2(0x001F, 0x0001, lambda_1786)

    ChrTalk(
        0x0102,
        (
            '#0020101326V#014F？？？',
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
            '#0010130989V#008F不、不知道她在说什么啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '#0270130990V#141F呵呵，在这种非常事态下，\n',
            '靠这群年轻人肯定会有所作为的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130991V#071F哈哈哈，的确如此啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130992V#070F那么……\n',
            '我们这就开始行动吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001E,
        (
            '#0040130993V#031F再会吧，亲爱的小猫咪㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130994V#010F愿女神保佑你们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0108, 180, 400)

    @scena.Lambda('lambda_1904')
    def lambda_1904():
        CameraMove(260, 1000, 49040, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1904)

    @scena.Lambda('lambda_191C')
    def lambda_191C():
        ChrWalkTo(0x00FE, 140, 0, 22040, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_191C)

    ChrSetDirection(0x001E, 180, 400)

    @scena.Lambda('lambda_193E')
    def lambda_193E():
        ChrWalkTo(0x00FE, 140, 0, 22040, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_193E)

    ChrSetDirection(0x0102, 180, 400)

    @scena.Lambda('lambda_1960')
    def lambda_1960():
        ChrWalkTo(0x00FE, 140, 0, 22040, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1960)

    Sleep(500)

    ChrWalkTo(0x0101, 170, 750, 49180, 1000, 0x00)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010130995V#000F#5P………约修亚……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x001D, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    OP_63(0x001D)
    ChrMoveTo(0x001D, 700, 1000, 51090, 2000, 0x00)

    ChrTalk(
        0x001D,
        (
            '#0030130996V#027F（我说我说，公主殿下……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030130997V（那两个孩子在旅途中\n',
            '　是不是发展成为那个……呢？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '#0060130998V#045F#5P（……也许是这样的吧。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060130999V（他们两人可以每天\n',
            '　这么愉快温馨地在一起……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060131000V#542F（……让我都觉得有点羡慕了呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x00CB, 2, 0x65A))
    OP_20(0x000007D0)
    FadeOut(1500, 0, -1)
    OP_0D()
    OP_21()
    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/T4100._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0008 offset: 0x1B26
@scena.Code('func_08_1B26')
def func_08_1B26():
    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上着锁，无法打开。',
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

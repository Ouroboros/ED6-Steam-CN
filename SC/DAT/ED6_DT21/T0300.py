import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0300_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0300   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0300.x'
    header.mapIndex       = 15
    header.bgm            = 15
    header.flags          = 0x0000
    header.entryFunction  = 0x0018
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
        ('ED6_DT06/CH20161._CH', 'ED6_DT06/CH20161P._CP'),
        ('ED6_DT07/CH02000._CH', 'ED6_DT07/CH02000P._CP'),
        ('ED6_DT27/CH03740._CH', 'ED6_DT27/CH03740P._CP'),
        ('ED6_DT26/CH20316._CH', 'ED6_DT26/CH20316P._CP'),
        ('ED6_DT26/CH20339._CH', 'ED6_DT26/CH20339P._CP'),
        ('ED6_DT26/CH20325._CH', 'ED6_DT26/CH20325P._CP'),
        ('ED6_DT26/CH20317._CH', 'ED6_DT26/CH20317P._CP'),
        ('ED6_DT26/CH20334._CH', 'ED6_DT26/CH20334P._CP'),
        ('ED6_DT26/CH20319._CH', 'ED6_DT26/CH20319P._CP'),
        ('ED6_DT26/CH20322._CH', 'ED6_DT26/CH20322P._CP'),
        ('ED6_DT27/CH03780._CH', 'ED6_DT27/CH03780P._CP'),
        ('ED6_DT07/CH02000._CH', 'ED6_DT07/CH02000P._CP'),
        ('ED6_DT26/CH20239._CH', 'ED6_DT26/CH20239P._CP'),
        ('ED6_DT27/CH03080._CH', 'ED6_DT27/CH03080P._CP'),
        ('ED6_DT26/CH20240._CH', 'ED6_DT26/CH20240P._CP'),
    ]

# id: 0x10001 offset: 0x122
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '卡西乌斯',
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
            name                = '莱娜',
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
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '雪拉扎德',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '凯文神父',
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
            name                = '艾利兹街道方向',
            x                   = 4110,
            z                   = -1000,
            y                   = -46140,
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

# id: 0x10002 offset: 0x1C2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x1C2
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -270,
            y           = 0,
            z           = -16990,
            range       = 4310,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFFC0CC,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000E,
        ),
    )

# id: 0x10004 offset: 0x1E2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -11800,
            triggerZ            = 0,
            triggerY            = 6720,
            triggerRange        = 1000,
            actorX              = -14930,
            actorZ              = -2000,
            actorY              = 9650,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001B,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x206
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0306, 6, 0x1836)),
            (Expr.TestScenaFlags, ScenaFlag(0x0307, 0, 0x1838)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_240',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0306, 7, 0x1837)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_21F',
    )

    ChrSetFlags(0x0009, 0x0010)

    def _loc_21F(): pass

    label('loc_21F')

    ChrSetPos(0x0009, -7530, 0, 2690, 90)
    ChrClearFlags(0x0009, 0x0080)
    OP_E5(0x09, 0x00, 0x00)
    CreateThread(0x0009, 0x00, 0x00, func_02_3B3)

    def _loc_240(): pass

    label('loc_240')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_251',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    Event(0, func_06_12E9)

    Jump('loc_2FD')

    def _loc_251(): pass

    label('loc_251')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_262',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    Event(0, func_07_13D6)

    Jump('loc_2FD')

    def _loc_262(): pass

    label('loc_262')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Return,
        ),
        'loc_281',
    )

    MapSetFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    Event(0, func_0C_17E1)

    Jump('loc_2FD')

    def _loc_281(): pass

    label('loc_281')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 3, 0x10F3)),
            Expr.Return,
        ),
        'loc_2A0',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x75),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x10000000)
    ClearScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    Event(0, func_10_2E7E)

    Jump('loc_2FD')

    def _loc_2A0(): pass

    label('loc_2A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 4, 0x10F4)),
            Expr.Return,
        ),
        'loc_2BF',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x75),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x10000000)
    ClearScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    Event(0, func_16_378E)

    Jump('loc_2FD')

    def _loc_2BF(): pass

    label('loc_2BF')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2DF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 5, 0x180D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2DC',
    )

    MapSetFlags(0x10000000)
    Event(0, func_05_9A2)

    def _loc_2DC(): pass

    label('loc_2DC')

    Jump('loc_2FD')

    def _loc_2DF(): pass

    label('loc_2DF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 3, 0x1003)),
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 4, 0x1004)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2FD',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x58),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x10000000)
    Event(0, func_04_535)

    def _loc_2FD(): pass

    label('loc_2FD')

    Return()

# id: 0x0001 offset: 0x2FE
@scena.Code('func_01_2FE')
def func_01_2FE():
    OP_16(0x02, 4000, -125000, -133000, 2293763)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_378',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0305, 0, 0x1828)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_358',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 7, 0x1817)),
            Expr.Return,
        ),
        'loc_343',
    )

    MapSetFlags(0x00000010)
    OP_11(0xE6, 0xF0, 0xFF, 0, 60000, 0)

    Jump('loc_358')

    def _loc_343(): pass

    label('loc_343')

    MapSetFlags(0x00000010)
    OP_11(0xE6, 0xF0, 0xFF, 0, 80000, 0)

    def _loc_358(): pass

    label('loc_358')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0306, 3, 0x1833)),
            Expr.Return,
        ),
        'loc_378',
    )

    OP_64(0x00, 0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0306, 4, 0x1834)),
            Expr.Return,
        ),
        'loc_378',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x75),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x02000000)

    def _loc_378(): pass

    label('loc_378')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_386',
    )

    CreateThread(0x0101, 0x03, 0x00, func_0D_19DC)

    def _loc_386(): pass

    label('loc_386')

    OP_71(0x0003, 0x0004)
    OP_71(0x0006, 0x0004)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 5, 0x180D)),
            Expr.Return,
        ),
        'loc_39E',
    )

    OP_6F(0x0007, 30)

    def _loc_39E(): pass

    label('loc_39E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0306, 3, 0x1833)),
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3B2',
    )

    OP_1B(0x00, 0x00, 0x001E)
    StopEffect(0x80, 0x02)

    def _loc_3B2(): pass

    label('loc_3B2')

    Return()

# id: 0x0002 offset: 0x3B3
@scena.Code('func_02_3B3')
def func_02_3B3():
    ExecExpressionWithReg(
        0x0001,
        (
            Expr.Rand,
            (Expr.PushLong, 0xE),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3D8',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_51A')

    def _loc_3D8(): pass

    label('loc_3D8')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3F1',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_51A')

    def _loc_3F1(): pass

    label('loc_3F1')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_40A',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_51A')

    def _loc_40A(): pass

    label('loc_40A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_423',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_51A')

    def _loc_423(): pass

    label('loc_423')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_43C',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_51A')

    def _loc_43C(): pass

    label('loc_43C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_455',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_51A')

    def _loc_455(): pass

    label('loc_455')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_46E',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_51A')

    def _loc_46E(): pass

    label('loc_46E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_487',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_51A')

    def _loc_487(): pass

    label('loc_487')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4A0',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_51A')

    def _loc_4A0(): pass

    label('loc_4A0')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4B9',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_51A')

    def _loc_4B9(): pass

    label('loc_4B9')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4D2',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_51A')

    def _loc_4D2(): pass

    label('loc_4D2')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4EB',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_51A')

    def _loc_4EB(): pass

    label('loc_4EB')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_504',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_51A')

    def _loc_504(): pass

    label('loc_504')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_51A',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_51A(): pass

    label('loc_51A')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_52F',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_51A')

    def _loc_52F(): pass

    label('loc_52F')

    Return()

# id: 0x0003 offset: 0x530
@scena.Code('func_03_530')
def func_03_530():
    Call(0, 0x0017)

    Return()

# id: 0x0004 offset: 0x535
@scena.Code('func_04_535')
def func_04_535():
    EventBegin(0x00)
    MapClearFlags(0x00000001)
    ChrSetPos(0x0101, 1890, -1000, -18670, 0)
    ChrSetPos(0x0142, 3040, -1000, -20140, 0)
    CameraMove(1760, 6700, 2360, 0)
    OP_67(0, 9860, -10000, 0)
    CameraSetDistance(3530, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    OP_C8(0x0200, 0x0046, 'C_PLAC01._CH', 0x00, 0x07D0)
    ShowPlaceName('布莱特家')
    FadeIn(2000, 0)

    @scena.Lambda('lambda_05C9')
    def lambda_05C9():
        CameraMove(990, 6700, -11410, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_05C9)

    @scena.Lambda('lambda_05E1')
    def lambda_05E1():
        OP_67(0, 9860, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_05E1)

    @scena.Lambda('lambda_05F9')
    def lambda_05F9():
        ChrWalkTo(0x0101, 1980, 0, -8680, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0142, 0x0000, lambda_05F9)

    @scena.Lambda('lambda_0614')
    def lambda_0614():
        ChrWalkTo(0x0142, 2430, 0, -9950, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0142, 0x0001, lambda_0614)

    Sleep(5000)

    TerminateThread(0x0101, 0x00)
    TerminateThread(0x0101, 0x01)
    Fade(1000)
    CameraMove(2550, 0, -8780, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    WaitForThreadExit(0x0142, 0x0000)
    WaitForThreadExit(0x0142, 0x0001)
    Sleep(1000)

    ChrTalk(
        0x0142,
        (
            '#0180190298V#1062F#4P嘿～\n',
            '这里就是艾丝蒂尔的家吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190299V好漂亮的房子，而且\n',
            '感觉真是温馨啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190300V#008F#5P嘿嘿，真的吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190301V我和爸爸、妈妈……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190302V还有约修亚的回忆\n',
            '都留存在这间屋子中呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0142,
        (
            '#0180190303V#1060F#4P是这样啊～～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190304V嗯，那么约修亚应该\n',
            '已经回来了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190305V#5P#006F嗯，肯定没错的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190306V快进来吧！我来介绍你们俩认识！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_081F')
    def lambda_081F():
        ChrWalkTo(0x0101, 2009, 450, -3930, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0142, 0x0000, lambda_081F)

    @scena.Lambda('lambda_083A')
    def lambda_083A():
        CameraMove(1750, 450, -4240, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_083A)

    @scena.Lambda('lambda_0852')
    def lambda_0852():
        OP_67(0, 9500, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0852)

    OP_62(0x0142, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    WaitForThreadExit(0x0142, 0x0000)
    OP_72(0x0000, 0x0010)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 59)
    OP_73(0x0000)

    @scena.Lambda('lambda_0897')
    def lambda_0897():
        ChrWalkTo(0x0101, 2270, 450, -1510, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0142, 0x0000, lambda_0897)

    Sleep(1200)

    @scena.Lambda('lambda_08B7')
    def lambda_08B7():
        CameraMove(1980, 0, -8680, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_08B7)

    @scena.Lambda('lambda_08CF')
    def lambda_08CF():
        OP_67(0, 9500, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_08CF)

    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0101, 0x0003)
    OP_63(0x0142)
    Sleep(500)

    ChrTalk(
        0x0142,
        (
            '#0180190307V#1067F#4P虽然不知道他是个怎样的笨蛋… \n',
            '但做出这么残酷的事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190308V#1065F呼……真是过分。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_096C')
    def lambda_096C():
        ChrWalkTo(0x0142, 2050, 450, -3760, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0142, 0x0001, lambda_096C)

    FadeOut(1000, 0, -1)
    OP_0D()
    TerminateThread(0x0142, 0x01)
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T0310._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0005 offset: 0x9A2
@scena.Code('func_05_9A2')
def func_05_9A2():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_9C2',
    )

    Call(0, 0x001C)
    FadeIn(0, 0)
    Call(0, 0x001D)

    def _loc_9C2(): pass

    label('loc_9C2')

    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    ChrSetPos(0x0101, 1800, -1000, -27820, 0)
    ChrSetPos(0x0103, 2900, -1000, -27820, 0)
    ChrSetPos(0x00F8, 1700, -1000, -28820, 0)
    ChrSetPos(0x00F9, 2800, -1000, -28820, 0)
    CameraMove(5010, 0, 6710, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2980, 0)
    OP_6C(48000, 0)
    OP_6E(358, 0)

    @scena.Lambda('lambda_0A5D')
    def lambda_0A5D():
        CameraMove(2660, 0, -15230, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0A5D)

    @scena.Lambda('lambda_0A75')
    def lambda_0A75():
        OP_67(0, 9500, -10000, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0A75)

    @scena.Lambda('lambda_0A8D')
    def lambda_0A8D():
        CameraSetDistance(1990, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0A8D)

    @scena.Lambda('lambda_0A9D')
    def lambda_0A9D():
        OP_6C(45000, 7000)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_0A9D)

    OP_C8(0x0200, 0x0046, 'C_PLAC01._CH', 0x00, 0x07D0)
    ShowPlaceName('布莱特家')
    FadeIn(2000, 0)
    ChrClearFlags(0x0000, 0x0080)
    ChrClearFlags(0x0001, 0x0080)
    ChrClearFlags(0x0002, 0x0080)
    ChrClearFlags(0x0003, 0x0080)

    @scena.Lambda('lambda_0AE9')
    def lambda_0AE9():
        ChrMoveToRelative(0x00FE, 0, 0, 12600, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0AE9)

    Sleep(200)

    @scena.Lambda('lambda_0B09')
    def lambda_0B09():
        ChrMoveToRelative(0x00FE, 0, 0, 12600, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0000, lambda_0B09)

    Sleep(200)

    @scena.Lambda('lambda_0B29')
    def lambda_0B29():
        ChrMoveToRelative(0x00FE, 0, 0, 12500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0000, lambda_0B29)

    Sleep(200)

    @scena.Lambda('lambda_0B49')
    def lambda_0B49():
        ChrMoveToRelative(0x00FE, 0, 0, 12500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0000, lambda_0B49)

    WaitForThreadExit(0x0101, 0x0000)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010280948V#1015F#6P嗯……\n',
            '这里的雾也很厉害啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_C22',
    )

    ChrTalk(
        0x0107,
        (
            '#0070280949V#560F哇……\n',
            '这里就是姐姐的家吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050280950V#051F那个大叔，还真会\n',
            '挑选好住处啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1109')

    def _loc_C22(): pass

    label('loc_C22')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_CAA',
    )

    ChrTalk(
        0x0104,
        (
            '#0040280951V#033F这……\n',
            '这里就是艾丝蒂尔的家吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050280950V#051F那个大叔，还真会\n',
            '挑选好住处啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1109')

    def _loc_CAA(): pass

    label('loc_CAA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_D32',
    )

    ChrTalk(
        0x0105,
        (
            '#0060280953V#048F啊……\n',
            '这里就是艾丝蒂尔的家啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050280950V#051F那个大叔，还真会\n',
            '挑选好住处啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1109')

    def _loc_D32(): pass

    label('loc_D32')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_DC4',
    )

    ChrTalk(
        0x0106,
        (
            '#0050280955V#051F呵……\n',
            '这里就是大叔的家吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080280956V#071F哈哈，和想象中的差不多，\n',
            '感觉很温馨的房子啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1109')

    def _loc_DC4(): pass

    label('loc_DC4')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_E48',
    )

    ChrTalk(
        0x0107,
        (
            '#0070280949V#560F哇……\n',
            '这里就是姐姐的家吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040280958V#031F呼～一看就是个很有\n',
            '情趣的家呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1109')

    def _loc_E48(): pass

    label('loc_E48')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_EC6',
    )

    ChrTalk(
        0x0107,
        (
            '#0070280949V#560F哇……\n',
            '这里就是姐姐的家吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060280960V#041F呵呵……\n',
            '看起来真不错呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1109')

    def _loc_EC6(): pass

    label('loc_EC6')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_F58',
    )

    ChrTalk(
        0x0107,
        (
            '#0070280961V#560F哇……\n',
            '这里就是姐姐的家啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080280956V#071F哈哈，和想象中的差不多，\n',
            '感觉很温馨的房子啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1109')

    def _loc_F58(): pass

    label('loc_F58')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_FE0',
    )

    ChrTalk(
        0x0105,
        (
            '#0060280953V#048F啊……\n',
            '这里就是艾丝蒂尔的家啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040280958V#031F呼～一看就是个很有\n',
            '情趣的家呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1109')

    def _loc_FE0(): pass

    label('loc_FE0')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1076',
    )

    ChrTalk(
        0x0104,
        (
            '#0040280951V#033F这……\n',
            '这里就是艾丝蒂尔的家吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080280956V#071F哈哈，和想象中的差不多，\n',
            '感觉很温馨的房子啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1109')

    def _loc_1076(): pass

    label('loc_1076')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1109',
    )

    ChrTalk(
        0x0105,
        (
            '#0060280953V#048F啊……\n',
            '这里就是艾丝蒂尔的家啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080280956V#071F哈哈，和想象中的差不多，\n',
            '感觉很温馨的房子啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1109(): pass

    label('loc_1109')

    ChrSetDirection(0x0101, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010280969V#1016F#5P嗯……\n',
            '就是那样啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280970V#1011F好啦，我去泡茶给大家喝，\n',
            '快点进来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030280971V#026F#2P茶就由我来泡吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030280972V#027F你还是先去二楼阳台\n',
            '看看比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010280973V#1004F#6P啊……为什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030280974V#524F#2P看啊，都已经那样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1237')
    def lambda_1237():
        CameraMove(2070, 0, 8140, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1237)

    @scena.Lambda('lambda_124F')
    def lambda_124F():
        OP_6C(9000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_124F)

    @scena.Lambda('lambda_125F')
    def lambda_125F():
        CameraSetDistance(2530, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_125F)

    ChrSetDirection(0x0101, 0, 400)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010280975V#1004F#1P啊……是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280976V#1007F这么大的雾确实\n',
            '会把房子都弄潮的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    NewScene('ED6_DT21/T0310._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0006 offset: 0x12E9
@scena.Code('func_06_12E9')
def func_06_12E9():
    EventBegin(0x00)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0103, 0x0080)
    ChrSetFlags(0x00F8, 0x0080)
    ChrSetFlags(0x00F9, 0x0080)
    CameraMove(490, 6660, 350, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 420, 6700, 2930, 180)
    ChrClearFlags(0x0101, 0x0080)
    FadeIn(1000, 0)
    Sleep(500)

    ChrWalkTo(0x0101, 420, 6700, -60, 2000, 0x00)
    ChrSetDirection(0x0101, 225, 400)
    Sleep(500)

    OP_6F(0x0007, 0)
    OP_70(0x0007, 30)
    OP_23(0x0006)

    @scena.Lambda('lambda_1397')
    def lambda_1397():
        ChrMoveTo(0x00FE, 610, 6700, 520, 500, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1397)

    Sleep(500)

    PlaySE(7, 0x00, 0x64)
    OP_73(0x0007)
    Sleep(500)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    NewScene('ED6_DT21/T0310._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0007 offset: 0x13D6
@scena.Code('func_07_13D6')
def func_07_13D6():
    EventBegin(0x00)
    PlaySE(450, 0x00, 0x64)
    OP_BB(0x00, 0x01, 0x00000000)
    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)
    FormationAddMember(ChrTable['提妲'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['科洛丝'], 0xF9, 0xFF)
    CameraMove(2280, 450, -2180, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(38000, 0)
    OP_6E(280, 0)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0103, 0x0080)
    ChrSetFlags(0x0107, 0x0080)
    ChrSetFlags(0x0105, 0x0080)
    ChrSetPos(0x0101, 2110, 450, -1890, 180)
    ChrSetPos(0x0103, 2110, 450, -1890, 180)
    ChrSetPos(0x0107, 2110, 450, -1890, 180)
    ChrSetPos(0x0105, 2110, 450, -1890, 180)
    ChrSetStatus(ChrTable['艾丝蒂尔'], 0xFE, 0)
    ChrSetStatus(ChrTable['雪拉扎德'], 0xFE, 0)
    ChrSetStatus(ChrTable['奥利维尔'], 0xFE, 0)
    ChrSetStatus(ChrTable['科洛丝'], 0xFE, 0)
    ChrSetStatus(ChrTable['阿加特'], 0xFE, 0)
    ChrSetStatus(ChrTable['提妲'], 0xFE, 0)
    ChrSetStatus(ChrTable['金'], 0xFE, 0)
    OP_C0(0x15, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    OP_6F(0x0000, 0)
    OP_70(0x0000, 59)
    OP_73(0x0000)
    Sleep(1000)

    CreateThread(0x0101, 0x01, 0x00, func_08_16F9)
    Sleep(500)

    CreateThread(0x0103, 0x01, 0x00, func_09_1713)
    Sleep(500)

    CreateThread(0x0107, 0x01, 0x00, func_0A_1748)
    Sleep(500)

    CreateThread(0x0105, 0x01, 0x00, func_0B_177D)

    @scena.Lambda('lambda_1520')
    def lambda_1520():
        CameraMove(2060, 450, -5010, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1520)

    WaitForThreadExit(0x0105, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    OP_23(0x01C2)

    ChrTalk(
        0x0101,
        (
            '#0010290306V#1004F#7P哇……\n',
            '好像比昨天更厉害了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060290307V#043F#5P嗯……\n',
            '雾确实更浓了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070290308V#065F#5P不知道阿加特哥哥他们\n',
            '是否还好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290309V#1015F#7P嗯……是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290310V虽然只是巡视，\n',
            '不过还是有点担心呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0107, 400)

    ChrTalk(
        0x0103,
        (
            '#0030290311V#020F#6P这样的话，\n',
            '我们赶快去协会看看吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290312V去问问昨夜\n',
            '的情况吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_16A6')
    def lambda_16A6():
        ChrTurnDirection(0x00FE, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_16A6)

    Sleep(50)

    @scena.Lambda('lambda_16B9')
    def lambda_16B9():
        ChrTurnDirection(0x00FE, 0x0103, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_16B9)

    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010290313V#1006F嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0303, 4, 0x181C))
    OP_28(0x0090, 0x01, 0x0800)
    OP_28(0x0074, 0x04, 0x40)
    EventEnd(0x00)

    Return()

# id: 0x0008 offset: 0x16F9
@scena.Code('func_08_16F9')
def func_08_16F9():
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 2020, 450, -5990, 2000, 0x00)

    Return()

# id: 0x0009 offset: 0x1713
@scena.Code('func_09_1713')
def func_09_1713():
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 2080, 450, -3790, 2000, 0x00)
    ChrWalkTo(0x00FE, 1180, 450, -5000, 2000, 0x00)
    ChrSetDirection(0x00FE, 226, 400)

    Return()

# id: 0x000A offset: 0x1748
@scena.Code('func_0A_1748')
def func_0A_1748():
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 2080, 450, -3790, 2000, 0x00)
    ChrWalkTo(0x00FE, 2860, 450, -5000, 2000, 0x00)
    ChrSetDirection(0x00FE, 136, 400)

    Return()

# id: 0x000B offset: 0x177D
@scena.Code('func_0B_177D')
def func_0B_177D():
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 2050, 450, -3490, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)
    Sleep(200)

    OP_72(0x0000, 0x0800)
    OP_6F(0x0000, 59)
    OP_70(0x0000, 0)
    OP_23(0x0006)
    PlaySE(7, 0x00, 0x64)
    OP_73(0x0000)
    OP_71(0x0000, 0x0800)
    ChrSetDirection(0x00FE, 180, 400)
    ChrWalkTo(0x00FE, 2029, 450, -4000, 2000, 0x00)

    Return()

# id: 0x000C offset: 0x17E1
@scena.Code('func_0C_17E1')
def func_0C_17E1():
    EventBegin(0x00)
    OP_D6(0x00)
    CameraMove(3370, -1000, -30420, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 2990, -1000, -35620, 0)

    @scena.Lambda('lambda_1839')
    def lambda_1839():
        ChrWalkTo(0x00FE, 3260, -1000, -31810, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1839)

    FadeIn(4000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010290944V#1004F#6P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1889')
    def lambda_1889():
        CameraMove(3360, -1000, -18490, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1889)

    @scena.Lambda('lambda_18A1')
    def lambda_18A1():
        OP_67(0, 8000, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_18A1)

    WaitForThreadExit(0x0101, 0x0001)
    Sleep(1000)

    Sleep(100)

    Fade(1000)
    CameraMove(3370, -1000, -30420, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010290945V#1004F#6P这里是……我的家？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 90, 500)
    Sleep(500)

    ChrSetDirection(0x0101, 270, 500)
    Sleep(500)

    ChrSetDirection(0x0101, 0, 400)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010290946V#1015F#6P我……\n',
            '应该在神秘森林才对…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290947V而且……\n',
            '雾是什么时候散去的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0306, 3, 0x1833))
    EventEnd(0x00)
    PlayBGM(15)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0xF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    CreateThread(0x0101, 0x03, 0x00, func_0D_19DC)
    OP_1B(0x00, 0x00, 0x001E)

    Return()

# id: 0x000D offset: 0x19DC
@scena.Code('func_0D_19DC')
def func_0D_19DC():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1A20',
    )

    Sleep(2000)

    PlaySE(282, 0x00, 0x46)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1A20',
    )

    def _loc_19F4(): pass

    label('loc_19F4')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1A20',
    )

    Sleep(4000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A0D',
    )

    Jump('loc_1A20')

    def _loc_1A0D(): pass

    label('loc_1A0D')

    PlaySE(282, 0x00, 0x46)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A1D',
    )

    Jump('loc_1A20')

    def _loc_1A1D(): pass

    label('loc_1A1D')

    Jump('loc_19F4')

    def _loc_1A20(): pass

    label('loc_1A20')

    Return()

# id: 0x000E offset: 0x1A21
@scena.Code('func_0E_1A21')
def func_0E_1A21():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0306, 3, 0x1833)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0306, 4, 0x1834)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1A2E',
    )

    Return()

    def _loc_1A2E(): pass

    label('loc_1A2E')

    EventBegin(0x00)
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    Fade(1000)
    ChrSetPos(0x0101, 1960, 0, -16680, 0)
    CameraMove(1440, 0, -16329, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_71(0x0004, 0x0004)
    OP_72(0x0003, 0x0004)
    OP_72(0x0003, 0x0020)
    OP_6F(0x0003, 0)
    OP_70(0x0003, 0)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetChipByIndex(0x0008, 3)
    ChrSetSubChip(0x0008, 2)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetFlags(0x0008, 0x0040)
    ChrSetFlags(0x0008, 0x0800)
    ChrSetPos(0x0008, -8500, 0, -7490, 90)

    @scena.Lambda('lambda_1AF0')
    def lambda_1AF0():
        CameraMove(-8590, 0, -7270, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1AF0)

    @scena.Lambda('lambda_1B08')
    def lambda_1B08():
        OP_67(0, 5180, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1B08)

    @scena.Lambda('lambda_1B20')
    def lambda_1B20():
        OP_6C(315000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1B20)

    ChrSetDirection(0x0101, 315, 400)
    WaitForThreadExit(0x0101, 0x0000)
    OP_99(0x0008, 0x02, 0x00, 1500)

    @scena.Lambda('lambda_1B45')
    def lambda_1B45():
        OP_99(0x0008, 0x00, 0x03, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_1B45)

    Sleep(200)

    OP_6F(0x0003, 0)
    OP_70(0x0003, 60)
    PlaySE(282, 0x00, 0x64)
    Sleep(300)

    WaitForThreadExit(0x0008, 0x0000)
    OP_99(0x0008, 0x04, 0x08, 1000)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0160290948V#085F#5P呼……真累啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0101, -1170, 0, -14210, 323)

    ChrTalk(
        0x0101,
        (
            '#0010290949V#5P老、老爸……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrSetSubChip(0x0008, 9)

    @scena.Lambda('lambda_1BFD')
    def lambda_1BFD():
        ChrWalkTo(0x00FE, -5030, 0, -11020, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1BFD)

    @scena.Lambda('lambda_1C18')
    def lambda_1C18():
        CameraMove(-8160, 0, -7840, 2200)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1C18)

    @scena.Lambda('lambda_1C30')
    def lambda_1C30():
        CameraSetDistance(3050, 2200)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1C30)

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    TerminateThread(0x0101, 0x03)

    ChrTalk(
        0x0008,
        (
            '#0160290950V#080F噢噢、艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160290951V怎么了？\n',
            '竟然这么早就起床了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250042V#1004F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160290953V#081F哈哈哈，我明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160290954V因为爸爸好久没回家了，\n',
            '想和爸爸撒撒娇对不对？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160290955V好啊！就像平时一样——\n',
            '赶快扑到爸爸怀里来吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290956V#1019F别、别像哄小孩一样！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290957V#1007F平时总说什么忙不过来，\n',
            '怎么忽然又放假了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290958V#1009F要是早点告诉我\n',
            '我也能多做点准备啊──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_72(0x0000, 0x0010)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 59)
    OP_73(0x0000)
    Sleep(500)

    ChrSetPos(0x0009, 2020, 450, -3650, 225)
    ChrSetFlags(0x0009, 0x0040)
    ChrClearFlags(0x0009, 0x0080)

    NpcTalk(
        0x0009,
        '女性的声音',
        (
            '#0700290959V#1P哎呀哎呀。\n',
            '一大清早就这么热闹啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_20(0x00000BB8)

    @scena.Lambda('lambda_1E9E')
    def lambda_1E9E():
        CameraMove(-3190, 450, -4810, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1E9E)

    @scena.Lambda('lambda_1EB6')
    def lambda_1EB6():
        OP_67(0, 4520, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1EB6)

    @scena.Lambda('lambda_1ECE')
    def lambda_1ECE():
        CameraSetDistance(3470, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1ECE)

    @scena.Lambda('lambda_1EDE')
    def lambda_1EDE():
        OP_6C(0, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1EDE)

    ChrTurnDirection(0x0101, 0x0009, 400)
    ChrSetSubChip(0x0008, 8)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010290960V#1004F#5P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160290961V#084F#5P喔喔，是莱娜啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160290962V#081F我正在砍柴，\n',
            '艾丝蒂尔也醒了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160290963V我们父女两个正在\n',
            '亲密地联络感情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0009,
        '女性',
        (
            '#0700290964V#866F#8P呵呵呵，是真的吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700290965V可是我看艾丝蒂尔\n',
            '好像一点都不情愿哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700290966V#861F你要总这么乱来的话，\n',
            '可是会被讨厌的哟……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0008,
        (
            '#0160290967V#086F#5P什、什么……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(300)

    @scena.Lambda('lambda_20BD')
    def lambda_20BD():
        CameraMove(-5460, 0, -9250, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_20BD)

    @scena.Lambda('lambda_20D5')
    def lambda_20D5():
        OP_6C(319000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_20D5)

    Fade(250)
    ChrSetChipByIndex(0x0008, 1)
    ChrSetSubChip(0x0008, 0)
    OP_72(0x0004, 0x0004)
    OP_0D()
    ChrClearFlags(0x0008, 0x0800)
    ChrSetFlags(0x0008, 0x0004)
    ChrWalkTo(0x0008, -8109, 0, -9660, 2500, 0x00)
    ChrSetDirection(0x0008, 90, 0)
    ChrMoveTo(0x0008, -6380, 0, -10850, 2500, 0x00)
    ChrClearFlags(0x0008, 0x0004)
    ChrTurnDirection(0x0008, 0x0101, 400)
    CreateThread(0x0009, 0x00, 0x00, func_0F_2E4E)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#0160290968V#084F#5P喂、喂喂、艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0008,
        (
            '#0160290969V#084F#5P你不会真的讨厌\n',
            '爸爸了吧！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160290970V#083F那个、虽然我经常因为工作\n',
            '太忙回不了家……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160290971V#082F爸爸可是这个世界上最疼爱\n',
            '艾丝蒂尔的人啊！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290972V#1026F#6P等、等一下啦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0009, 0x0000)

    NpcTalk(
        0x0009,
        '女性',
        (
            '#0700290973V#861F#4P呵呵呵……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700290974V#866F这孩子只是因为好久没看到你，\n',
            '有点不好意思了而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700290975V对吧，艾丝蒂尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0009, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010290976V#1026F#5P那、那个……\n',
            '难、难道你是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290977V…………………………\n',
            '………妈妈………？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0009,
        '女性',
        (
            '#0700290978V#866F#4P哎呀呀，真是个奇怪的孩子，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700290979V难道把妈妈都忘掉了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290980V#1025F#5P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    PlayBGM(83)
    Sleep(300)

    @scena.Lambda('lambda_23F1')
    def lambda_23F1():
        CameraSetDistance(3190, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_23F1)

    Fade(1000)
    OP_BB(0x00, 0x01, 0x00000044)
    OP_BD()
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010290981V#297F#5P妈——妈妈……\n',
            '真的是妈妈……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290982V呜呜呜呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0700290983V#864F#4P哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010290984V#298F#5P#4S妈妈———！！！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    @scena.Lambda('lambda_24CA')
    def lambda_24CA():
        CameraMove(-4460, 0, -9250, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_24CA)

    ChrWalkTo(0x0101, -3300, 0, -10700, 5000, 0x00)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0009, 0x0002)
    ChrSetFlags(0x0009, 0x0020)
    ChrSetChipByIndex(0x0009, 6)
    ChrSetSubChip(0x0009, 0)

    @scena.Lambda('lambda_250F')
    def lambda_250F():
        OP_99(0x0009, 0x00, 0x02, 2000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_250F)

    ChrMoveTo(0x0009, -2900, 0, -10750, 3000, 0x00)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0700290985V#866F#4P哎呀呀……\n',
            '怎么了？艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700290986V难道是做了恶梦了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290987V#298F#5P呜……呜呜……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290988V虽、虽然已经\n',
            '记不太清了，可是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290989V#297F我……做了好可怕的梦，\n',
            '梦见妈妈……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290990V不知去了哪里……\n',
            '……再也……没有回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0700290991V#863F#4P是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700290992V#866F呵呵，已经没事了。\n',
            '妈妈就在这里，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700290993V哪里都不会去的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700290994V别再害怕啦，乖孩子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290995V#299F#5P嗯……嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0160290996V#083F#5P那个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160290997V爸爸一个人…\n',
            '好寂寞啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0700290998V#864F#4P啊，亲爱的，你还在这里啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160290999V#082F#5P莱娜，你太过分了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0700291000V#861F#4P呵呵，开个玩笑而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291001V#866F……来，接住，亲爱的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160291002V#085F#5P嗯、嗯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0009, 0x02, 0x00, 1500)
    ChrSetPos(0x0101, -3400, 0, -10700, 90)
    ChrClearFlags(0x0101, 0x0080)
    ChrClearFlags(0x0009, 0x0002)
    ChrSetChipByIndex(0x0009, 2)
    ChrSetSubChip(0x0009, 0)
    ChrMoveTo(0x0101, -3700, 0, -10700, 1000, 0x00)
    ChrWalkTo(0x0008, -5350, 0, -10540, 1000, 0x00)
    ChrTurnDirection(0x0101, 0x0008, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010291003V#299F#6P嘿……嘿嘿嘿。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291004V#291F早上好～爸爸！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_28FF')
    def lambda_28FF():
        CameraMove(-5460, 0, -9250, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_28FF)

    ChrWalkTo(0x0101, -4820, 0, -10600, 5000, 0x00)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0008, 0x0002)
    ChrSetFlags(0x0008, 0x0020)
    ChrSetChipByIndex(0x0008, 8)
    ChrSetSubChip(0x0008, 0)
    ChrMoveTo(0x0008, -5450, 0, -10540, 3000, 0x00)

    @scena.Lambda('lambda_2958')
    def lambda_2958():
        OP_99(0x0008, 0x00, 0x02, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2958)

    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0160291005V#081F#5P噢！传得漂亮。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160291006V好！爸爸今天要\n',
            '陪艾丝蒂尔玩个够！\n',
            '随便你要玩什么都可以～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291007V#293F#6P真的吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160291008V#080F#5P那当然！男子汉卡西乌斯·布莱特\n',
            '说过的话什么时候不算数了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160680001V就算是扮家家酒\n',
            '爸爸也会陪你玩！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0008, 0x02, 0x00, 1500)
    ChrSetPos(0x0101, -4920, 0, -10600, 270)
    ChrClearFlags(0x0101, 0x0080)
    ChrClearFlags(0x0008, 0x0002)
    ChrSetChipByIndex(0x0008, 1)
    ChrSetSubChip(0x0008, 0)
    ChrMoveTo(0x0101, -4600, 0, -10540, 1000, 0x00)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010291009V#290F#6P嗯……那么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291010V#291F我就要……\n',
            '去钓鱼！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160291011V#081F#5P哦！不愧是我的女儿。\n',
            '连爱好都这么棒。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160291012V#084F……嗯，等一下，\n',
            '钓鱼好像是男孩子玩的…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160291013V还是玩扮家家酒比较好吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291014V#294F#6P不要！人家就要去钓鱼！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160291015V#083F#5P嗯……那好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0700291016V#861F#4P呵呵，只要她喜欢\n',
            '就随她的意吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291017V#866F不过，不管去玩什么……\n',
            '还是先吃过早餐后\n',
            '再去比较好吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160291018V#084F#5P哦，说的对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0009, 400)

    ChrTalk(
        0x0101,
        (
            '#0010291019V#293F#5P早餐吗！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291020V#291F妈妈～～！\n',
            '我的肚子都饿得在叫了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291021V我也来帮你一起做吧！\n',
            '这样可以快点吃到！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160291022V#080F#5P嗯，那我就去\n',
            '泡咖啡吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0700291023V#861F#4P呵呵，那可谢谢你们啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291024V#866F不过在那之前……\n',
            '请先去把手洗干净吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_20(0x00000FA0)
    OP_0D()
    OP_21()
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0010291025V──幸福的日子一天天过着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    PlayBGM(117)
    Sleep(500)

    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    NewScene('ED6_DT21/T0310._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000F offset: 0x2E4E
@scena.Code('func_0F_2E4E')
def func_0F_2E4E():
    ChrWalkTo(0x00FE, 1880, 0, -9170, 2000, 0x00)
    ChrWalkTo(0x00FE, -3010, 0, -10770, 2000, 0x00)
    ChrSetDirection(0x00FE, 270, 0)

    Return()

# id: 0x0010 offset: 0x2E7E
@scena.Code('func_10_2E7E')
def func_10_2E7E():
    EventBegin(0x00)
    OP_DB()
    LoadEffect(0x00, 'map\\\\mp071_01.eff')
    LoadEffect(0x01, 'map\\\\mp071_02.eff')
    LoadEffect(0x02, 'map\\\\mp071_03.eff')
    ChrSetFlags(0x0101, 0x0004)
    ChrSetFlags(0x0101, 0x0002)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetPos(0x0101, -12380, -200, 7130, 304)
    ChrSetPos(0x0008, -13750, -200, 4230, 333)
    ChrSetChipByIndex(0x0101, 4)
    ChrSetChipByIndex(0x0008, 5)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0009, -9360, -200, -1530, 314)
    ChrSetChipByIndex(0x0009, 2)
    ChrClearFlags(0x0009, 0x0080)
    CameraMove(-12910, -200, 5270, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(152000, 0)
    OP_6E(262, 0)

    @scena.Lambda('lambda_2F5B')
    def lambda_2F5B():
        OP_99(0x0101, 0x00, 0x03, 1500)
        Yield()

        Jump('lambda_2F5B')

    DispatchAsync2(0x0101, 0x0002, lambda_2F5B)

    @scena.Lambda('lambda_2F6E')
    def lambda_2F6E():
        OP_99(0x0008, 0x00, 0x03, 1500)
        Yield()

        Jump('lambda_2F6E')

    DispatchAsync2(0x0008, 0x0002, lambda_2F6E)

    FadeIn(1000, 0)
    OP_0D()
    Sleep(1500)

    PlayEffect(0x00, 0x01, 0x00FF, -13700, -1800, 7500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(500)

    OP_9E(0x0101, 0, 50, 300, 1000)
    OP_62(0x0101, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_2FF4')
    def lambda_2FF4():
        OP_99(0x0101, 0x04, 0x05, 1000)
        Yield()

        Jump('lambda_2FF4')

    DispatchAsync2(0x0101, 0x0002, lambda_2FF4)

    CreateThread(0x0101, 0x03, 0x00, func_11_3261)
    Sleep(500)

    @scena.Lambda('lambda_3013')
    def lambda_3013():
        OP_99(0x0008, 0x08, 0x0B, 1500)
        Yield()

        Jump('lambda_3013')

    DispatchAsync2(0x0008, 0x0002, lambda_3013)

    OP_62(0x0008, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    TerminateThread(0x0008, 0x02)
    Fade(500)

    @scena.Lambda('lambda_304B')
    def lambda_304B():
        ChrJumpTo(0x00FE, -13070, 0, 4130, 500, 4000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_304B)

    ChrClearFlags(0x0008, 0x0004)
    Sleep(10)

    ChrSetChipByIndex(0x0008, 1)
    ChrSetSubChip(0x0008, 0)
    WaitForThreadExit(0x0008, 0x0001)
    ChrWalkTo(0x0008, -11860, -200, 5110, 2000, 0x00)
    ChrWalkTo(0x0008, -12190, -200, 6380, 2000, 0x00)
    ChrSetDirection(0x0008, 293, 400)
    Sleep(500)

    TerminateThread(0x0101, 0x02)
    Sleep(1000)

    @scena.Lambda('lambda_30BF')
    def lambda_30BF():
        OP_99(0x00FE, 0x06, 0x0E, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_30BF)

    PlaySE(24, 0x00, 0x64)
    TerminateThread(0x0101, 0x03)
    StopEffect(0x01, 0x00)
    PlayEffect(0x02, 0x02, 0x00FF, -13700, -1800, 7500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    WaitForThreadExit(0x0101, 0x0001)
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(100)

    OP_62(0x0101, 0x00000000, 1700, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(1000)

    @scena.Lambda('lambda_3143')
    def lambda_3143():
        CameraMove(-11880, -200, 4500, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3143)

    @scena.Lambda('lambda_315B')
    def lambda_315B():
        OP_67(0, 8080, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_315B)

    @scena.Lambda('lambda_3173')
    def lambda_3173():
        OP_6C(140000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3173)

    ChrWalkTo(0x0009, -11890, -200, 3140, 1500, 0x00)
    ChrTurnDirection(0x0009, 0x0101, 400)
    Sleep(500)

    ChrTurnDirection(0x0008, 0x0009, 400)
    Sleep(200)

    OP_99(0x0101, 0x0E, 0x11, 1000)
    Sleep(100)

    OP_62(0x0101, 0x00000000, 1700, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    OP_62(0x0009, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(2000)

    OP_DC()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0010291027V在父母的注视和陪伴下\n',
            '在大自然中尽情嬉戏……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    FadeOut(1000, 0, -1)
    OP_0D()
    Call(0, 0x0013)

    Return()

# id: 0x0011 offset: 0x3261
@scena.Code('func_11_3261')
def func_11_3261():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_33C9',
    )

    PlayEffect(0x01, 0x01, 0x00FF, -13700, -1700, 7500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    PlayEffect(0x01, 0x01, 0x00FF, -13700, -1700, 7500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(400)

    PlayEffect(0x01, 0x01, 0x00FF, -13700, -1700, 7500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(350)

    PlayEffect(0x01, 0x01, 0x00FF, -13700, -1700, 7500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(500)

    PlayEffect(0x01, 0x01, 0x00FF, -13700, -1700, 7500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(450)

    PlayEffect(0x01, 0x01, 0x00FF, -13700, -1700, 7500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(250)

    Jump('func_11_3261')

    def _loc_33C9(): pass

    label('loc_33C9')

    Return()

# id: 0x0012 offset: 0x33CA
@scena.Code('func_12_33CA')
def func_12_33CA():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_344E',
    )

    ChrSetDirection(0x0101, 338, 0)
    Sleep(200)

    ChrSetDirection(0x0101, 293, 0)
    Sleep(200)

    ChrSetDirection(0x0101, 248, 0)
    Sleep(200)

    ChrSetDirection(0x0101, 293, 0)
    Sleep(500)

    ChrSetDirection(0x0101, 248, 0)
    Sleep(200)

    ChrSetDirection(0x0101, 293, 0)
    Sleep(200)

    ChrSetDirection(0x0101, 338, 0)
    Sleep(200)

    ChrSetDirection(0x0101, 293, 0)
    Sleep(500)

    ChrSetDirection(0x0101, 338, 0)
    Sleep(200)

    ChrSetDirection(0x0101, 293, 0)
    Sleep(500)

    Jump('func_12_33CA')

    def _loc_344E(): pass

    label('loc_344E')

    Return()

# id: 0x0013 offset: 0x344F
@scena.Code('func_13_344F')
def func_13_344F():
    OP_DB()
    CameraMove(21780, 0, 200, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(60000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0009, 20640, 0, -1190, 90)
    ChrClearFlags(0x0009, 0x0080)
    OP_72(0x0006, 0x0020)
    OP_72(0x0006, 0x0004)
    OP_6F(0x0006, 1)
    OP_70(0x0006, 1)
    FadeIn(1000, 0)
    OP_0D()
    OP_6F(0x0006, 1)
    OP_70(0x0006, 2)
    OP_73(0x0006)
    ChrSetChipByIndex(0x0009, 7)
    Sleep(500)

    ChrSetChipByIndex(0x0009, 2)
    Sleep(500)

    ChrMoveTo(0x0009, 20640, 0, -570, 2000, 0x00)
    OP_6F(0x0006, 2)
    OP_70(0x0006, 3)
    OP_73(0x0006)
    ChrSetChipByIndex(0x0009, 7)
    Sleep(500)

    ChrSetChipByIndex(0x0009, 2)
    Sleep(500)

    ChrSetDirection(0x0009, 45, 400)
    ChrWalkTo(0x0009, 20640, 0, 800, 1000, 0x00)
    CreateThread(0x0101, 0x00, 0x00, func_14_36A4)
    ChrSetDirection(0x0009, 90, 400)

    @scena.Lambda('lambda_3552')
    def lambda_3552():
        CameraMove(19970, 0, 490, 4000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_3552)

    @scena.Lambda('lambda_356A')
    def lambda_356A():
        OP_6C(50000, 4000)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_356A)

    Sleep(400)

    CreateThread(0x0008, 0x00, 0x00, func_15_3722)
    Sleep(1000)

    @scena.Lambda('lambda_358B')
    def lambda_358B():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_358B')

    DispatchAsync2(0x0009, 0x0001, lambda_358B)

    WaitForThreadExit(0x0101, 0x0000)
    TerminateThread(0x0009, 0x01)
    OP_99(0x0101, 0x10, 0x12, 1000)
    Sleep(200)

    ChrSetDirection(0x0009, 90, 400)
    OP_6F(0x0006, 3)
    OP_70(0x0006, 4)
    OP_73(0x0006)
    ChrSetChipByIndex(0x0009, 7)
    Sleep(500)

    ChrSetChipByIndex(0x0009, 2)
    Sleep(500)

    ChrMoveTo(0x0009, 20640, 0, 1480, 2000, 0x00)
    OP_6F(0x0006, 4)
    OP_70(0x0006, 5)
    OP_73(0x0006)
    ChrSetChipByIndex(0x0009, 7)
    Sleep(500)

    ChrSetChipByIndex(0x0009, 2)
    Sleep(300)

    ChrSetDirection(0x0009, 180, 400)
    OP_62(0x0009, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(2000)

    OP_DC()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0010291028V有时也会帮忙做家务……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    FadeOut(1000, 0, -1)
    OP_0D()
    ChrSetChipByIndex(0x0101, 65535)
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/T0311._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0014 offset: 0x36A4
@scena.Code('func_14_36A4')
def func_14_36A4():
    ChrSetChipByIndex(0x0101, 9)
    ChrSetSubChip(0x0101, 0)
    ChrClearFlags(0x0101, 0x0004)
    ChrSetFlags(0x0101, 0x0020)
    ChrSetFlags(0x0101, 0x0002)
    ChrSetPos(0x0101, 12520, 0, 350, 90)

    @scena.Lambda('lambda_36D4')
    def lambda_36D4():
        ChrWalkTo(0x00FE, 20250, 0, -60, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_36D4)

    @scena.Lambda('lambda_36EF')
    def lambda_36EF():
        OP_99(0x00FE, 0x01, 0x07, 1500)
        Yield()

        Jump('lambda_36EF')

    DispatchAsync2(0x0101, 0x0002, lambda_36EF)

    Sleep(1300)

    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    WaitForThreadExit(0x0101, 0x0001)
    TerminateThread(0x0101, 0x02)
    ChrSetSubChip(0x0101, 0)

    Return()

# id: 0x0015 offset: 0x3722
@scena.Code('func_15_3722')
def func_15_3722():
    ChrSetChipByIndex(0x0008, 9)
    ChrSetSubChip(0x0008, 8)
    ChrClearFlags(0x0008, 0x0004)
    ChrSetFlags(0x0008, 0x0020)
    ChrSetFlags(0x0008, 0x0002)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, 12350, 0, 1350, 90)

    @scena.Lambda('lambda_3757')
    def lambda_3757():
        ChrWalkTo(0x00FE, 18500, 0, 940, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_3757)

    @scena.Lambda('lambda_3772')
    def lambda_3772():
        OP_99(0x00FE, 0x09, 0x0F, 1500)
        Yield()

        Jump('lambda_3772')

    DispatchAsync2(0x0008, 0x0002, lambda_3772)

    WaitForThreadExit(0x0008, 0x0001)
    TerminateThread(0x0008, 0x02)
    ChrSetSubChip(0x0008, 8)

    Return()

# id: 0x0016 offset: 0x378E
@scena.Code('func_16_378E')
def func_16_378E():
    EventBegin(0x00)
    CameraMove(3070, 0, -13180, 0)
    OP_67(0, 7710, -10000, 0)
    CameraSetDistance(2710, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 2590, 0, -13750, 180)
    ChrSetPos(0x000A, 2450, 0, -15050, 0)
    ChrSetPos(0x0009, 3100, 0, -12520, 180)
    ChrSetPos(0x0008, 1980, 0, -12580, 180)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetChipByIndex(0x000A, 10)
    ChrSetSubChip(0x000A, 0)
    FadeIn(1500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0030291032V#870F……那…\n',
            '我这就回去啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030291033V艾丝蒂尔。\n',
            '等春天我再来找你玩哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291034V#295F#5P呜……等一下嘛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291035V难得才来一次，\n',
            '为什么这么快就要走……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291036V再多住一两天\n',
            '好不好嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030291037V#872F嗯～我当然也想\n',
            '那样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030291038V可是戏班的各位都在等我回去呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291039V#295F#5P喔——真是没意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0700291040V#861F#5P好啦～别耍小孩子脾气了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291041V#866F雪拉，真是谢谢你了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291042V为了陪艾丝蒂尔玩，\n',
            '总是大老远特意跑来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030291043V#871F哪里～\n',
            '我也很开心的啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030291044V#875F而且莱娜阿姨做的料理，\n',
            '美味得让我不想走呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0700291045V#861F#5P哎呀，还真会说话，\n',
            '能让你喜欢，我也很高兴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160291046V#080F#5P以后一定要再来玩啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160291047V#081F下次我会把珍藏的白兰地\n',
            '拿出来和你一起喝！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030291048V#875F哇～！真的吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0008, 400)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0700291049V#863F#3S#2P亲～爱～的～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrTurnDirection(0x0008, 0x0009, 400)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0160291050V#083F#6P玩、玩笑而已啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0009, 180, 400)
    ChrSetDirection(0x0008, 180, 400)

    ChrTalk(
        0x0009,
        (
            '#0700291051V#862F#5P雪拉你也不许酗酒哦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291052V不管你酒量有多好，\n',
            '毕竟现在才１２岁而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291053V等长大一点后\n',
            '再喝就没问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030291054V#873F唉～可是～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0700291055V#861F#3S#5P雪～拉～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0030291056V#874F明明明、我明白了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030291057V不、不过我肯定\n',
            '也喝不了酒的啦～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030291058V团长自然是不用说，\n',
            '姐姐管我也管得很严呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0700291059V#866F#5P呵呵，那样最好啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291060V#861F雪拉，\n',
            '代我向戏班的各位问好哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160291061V#080F#5P下次把大家都\n',
            '带来玩吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160291062V这个院子很大，\n',
            '办个野餐会都没问题的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030291063V#875F是！我会转告给大家的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030291064V#872F好了，就这样。艾丝蒂尔。\n',
            '……你也要做个听话的好孩子哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291065V#291F#5P嗯！！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291066V雪拉姐，拜拜啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000A, 180, 400)

    @scena.Lambda('lambda_3F01')
    def lambda_3F01():
        CameraMove(3430, -1000, -25690, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3F01)

    @scena.Lambda('lambda_3F19')
    def lambda_3F19():
        ChrWalkTo(0x00FE, 3380, -1000, -34370, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_3F19)

    WaitForThreadExit(0x000A, 0x0001)
    ChrSetFlags(0x000A, 0x0080)
    Fade(1000)
    CameraMove(2730, 0, -12880, 0)
    OP_62(0x0101, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0700291067V#866F#5P呵呵……\n',
            '以后可要寂寞了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160291068V#080F#5P好啦，她不是说了吗，\n',
            '到了春天还会再来玩的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160291069V正好我也休假在家，\n',
            '不如办个大型联欢会吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0700291070V#861F呵呵，那当然好啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x0101)
    ChrSetDirection(0x0101, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010291071V#290F爸爸～！妈妈～～！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291072V#291F我……\n',
            '我想要个弟弟！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(80)

    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0160291073V#084F#5P什、什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0700291074V#864F#5P哎呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291075V#295F雪拉姐只是偶尔\n',
            '才能来找我玩……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291076V我想有个随时都可以\n',
            '一起玩的弟弟！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160291077V#083F#5P你、你这孩子啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160291078V那种事可不是想要\n',
            '就马上能有的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0700291079V#861F#5P呵呵呵……\n',
            '艾丝蒂尔想要个弟弟吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291080V#860F可是呢～这个愿望我们也\n',
            '不能向你保证会实现哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291081V因为这要看女神的安排了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291082V#293F是那样吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0700291083V#866F#5P嗯，女神会在宁静的傍晚\n',
            '悄悄地把小宝宝放在菜园里……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291084V然后爸爸和妈妈就可以\n',
            '发现那个孩子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291085V#290F是、是那样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291086V#291F我就要……\n',
            '那我要向女神祈愿！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0700291087V#861F#5P呵呵，这样当然好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291088V#866F只要艾丝蒂尔做个听话的好孩子，\n',
            '女神说不定就会把小宝宝作为奖励\n',
            '赐给我们呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291089V#294F啊！那我一定要做个好孩子！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0009, 400)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0160291090V#080F#6P呼……\n',
            '你还是那么会哄小孩啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0008, 400)

    ChrTalk(
        0x0009,
        (
            '#0700291091V#866F#2P呵呵，不要说得好像是\n',
            '别人的事情一样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291092V#861F你自己也要努力\n',
            '才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0160291093V#081F#6P嗯、嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160291094V好～～～那我们现在\n',
            '就赶快回房间努力吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0700291095V#863F#2P我是说在常识的范围内努力！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291096V#860F好了！我现在要去\n',
            '准备晚饭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0160291097V#083F#6P……是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291098V#293F？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0700291099V#861F#2P呵呵呵，\n',
            '那我这就要去厨房了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291100V#866F你们现在\n',
            '要做什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160291101V#080F#6P说的也是啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 180, 400)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0160291102V#081F#5P艾丝蒂尔，要和爸爸\n',
            '一起去钓鱼吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0009, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010291103V#290F呜……今天就算了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291104V我想自己玩一会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160291105V#084F#5P#3S（受打击——）#2S',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160291106V#083F真是没办法……\n',
            '那我只能回书房看书去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0700291107V#861F#5P呵呵，\n',
            '被女儿抛弃了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291108V#865F艾丝蒂尔，\n',
            '玩的时候要注意安全哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160291109V#080F#5P一个人玩的时候\n',
            '一定不要靠近水池。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291110V#291F是——',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    ChrSetDirection(0x0008, 0, 400)

    @scena.Lambda('lambda_486A')
    def lambda_486A():
        CameraMove(2040, 0, -9450, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_486A)

    @scena.Lambda('lambda_4882')
    def lambda_4882():
        ChrWalkTo(0x00FE, 1920, 450, -3600, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_4882)

    Sleep(200)

    ChrSetDirection(0x0009, 315, 400)

    @scena.Lambda('lambda_48A9')
    def lambda_48A9():
        ChrWalkTo(0x00FE, 1900, 0, -9990, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_48A9)

    WaitForThreadExit(0x0009, 0x0001)

    @scena.Lambda('lambda_48C9')
    def lambda_48C9():
        ChrWalkTo(0x00FE, 1900, 450, -4950, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_48C9)

    WaitForThreadExit(0x0008, 0x0001)
    OP_72(0x0000, 0x0010)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 59)
    OP_73(0x0000)

    @scena.Lambda('lambda_48FF')
    def lambda_48FF():
        ChrWalkTo(0x00FE, 2210, 450, -1460, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_48FF)

    WaitForThreadExit(0x0009, 0x0001)
    Sleep(300)

    @scena.Lambda('lambda_4924')
    def lambda_4924():
        ChrWalkTo(0x00FE, 2210, 450, -1460, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_4924)

    WaitForThreadExit(0x0008, 0x0001)
    ChrSetFlags(0x0008, 0x0080)
    WaitForThreadExit(0x0009, 0x0001)
    ChrSetFlags(0x0009, 0x0080)
    OP_72(0x0000, 0x0800)
    OP_6F(0x0000, 59)
    OP_70(0x0000, 0)
    OP_23(0x0006)
    PlaySE(7, 0x00, 0x64)
    OP_73(0x0000)
    OP_71(0x0000, 0x0800)
    OP_71(0x0000, 0x0010)
    OP_62(0x0101, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)
    CameraMove(2590, 0, -13750, 2000)
    OP_63(0x0101)
    Sleep(600)

    ChrTalk(
        0x0101,
        (
            '#0010291111V#290F#5P……弟弟吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291112V#293F……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291113V#295F为什么……\n',
            '我的胸口会隐隐作痛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291114V好像忘掉了……\n',
            '什么…非常重要的东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 90, 500)
    Sleep(500)

    ChrSetDirection(0x0101, 270, 500)
    Sleep(500)

    ChrSetDirection(0x0101, 180, 500)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010291115V#292F#5P……不把它找出来的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0306, 4, 0x1834))
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

# id: 0x0017 offset: 0x4ABB
@scena.Code('func_17_4ABB')
def func_17_4ABB():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0306, 6, 0x1836)),
            (Expr.TestScenaFlags, ScenaFlag(0x0307, 0, 0x1838)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4EE6',
    )

    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0306, 7, 0x1837)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4E7E',
    )

    EventBegin(0x00)
    Fade(1000)
    CameraMove(-7910, 0, 2760, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, -8650, 0, 2630, 90)
    OP_0D()
    Sleep(200)

    ChrTalk(
        0x0009,
        (
            '#0700291206V#864F#5P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291207V剩下的洋葱… \n',
            '我记得确实是放在这里啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291208V#291F#6P妈妈！\n',
            '你在这里啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0009,
        (
            '#0700291209V#861F#2P啊～艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291210V#866F呵呵呵，怎么了？\n',
            '是不是已经饿坏了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291211V#290F#6P啊，不是。\n',
            '肚子还不算太饿……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291212V只是想问妈妈\n',
            '一点事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0700291213V#864F#2P？',
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
            '把寻找二楼储物室钥匙的事情告诉了妈妈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0009,
        (
            '#0700291214V#864F#2P哎呀哎呀……\n',
            '想去储物室探险吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291215V#863F嗯，那里面都是灰尘，\n',
            '会把衣服弄脏的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291216V#295F#6P唔……不能去吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0700291217V#860F#2P………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291218V#861F算啦，想去就去吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291219V#865F妈妈和爸爸的床边上\n',
            '不是有个小柜子吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291220V钥匙就放在\n',
            '最上边的抽屉里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291221V#291F#6P哇～谢谢妈妈！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0009, 90, 400)
    ChrClearFlags(0x0009, 0x0010)
    SetScenaFlags(ScenaFlag(0x0306, 7, 0x1837))
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Jump('loc_4EE3')

    def _loc_4E7E(): pass

    label('loc_4E7E')

    ChrTalk(
        0x0009,
        (
            '#0700291219V#865F妈妈和爸爸的床边上\n',
            '不是有个小柜子吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291220V钥匙就放在\n',
            '最上边的抽屉里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4EE3(): pass

    label('loc_4EE3')

    TalkEnd(0x0009)

    def _loc_4EE6(): pass

    label('loc_4EE6')

    Return()

# id: 0x0018 offset: 0x4EE7
@scena.Code('func_18_4EE7')
def func_18_4EE7():
    If(
        (
            (Expr.PushValueByIndex, 0x13),
            (Expr.PushLong, 0x3F9),
            Expr.Neq,
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Neq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_4EFD',
    )

    Return()

    def _loc_4EFD(): pass

    label('loc_4EFD')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x68),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4F0E',
    )

    Call(0, 0x0019)

    Return()

    def _loc_4F0E(): pass

    label('loc_4F0E')

    MapSetFlags(0x00000080)
    OP_C2()
    Yield()
    EventBegin(0x00)
    Fade(500)
    ChrSetChipByIndex(0x0101, 12)
    ChrSetSubChip(0x0101, 0)
    OP_0D()
    OP_20(0x000005DC)
    OP_21()
    OP_DB()
    PlaySE(283, 0x00, 0x64)

    @scena.Lambda('lambda_4F39')
    def lambda_4F39():
        OP_99(0x0101, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_4F39')

    DispatchAsync2(0x0101, 0x0002, lambda_4F39)

    Sleep(10000)

    Sleep(2000)

    Sleep(1500)

    Sleep(1500)

    TerminateThread(0x0101, 0x02)
    PlayBGM(117)
    Fade(500)
    ChrSetSubChip(0x0101, 8)
    OP_0D()
    Sleep(500)

    OP_DC()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5023',
    )

    ChrTalk(
        0x0101,
        (
            '#0010291234V#290F声音很好听呢，不过……\n',
            '似乎有些难吹啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291235V#296F可是，真奇怪啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291236V这个声音……\n',
            '总觉得以前在哪里听过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_508D')

    def _loc_5023(): pass

    label('loc_5023')

    ChrTalk(
        0x0101,
        (
            '#0010291237V#296F这声音……\n',
            '以前在哪里听到过呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291238V就去那个地方吹吹看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    OP_0D()

    def _loc_508D(): pass

    label('loc_508D')

    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

# id: 0x0019 offset: 0x5095
@scena.Code('func_19_5095')
def func_19_5095():
    MapSetFlags(0x00000080)
    OP_C2()
    Yield()
    EventBegin(0x00)
    OP_20(0x000005DC)
    Fade(1000)
    ChrSetPos(0x0101, -5540, 3450, 2200, 270)
    CameraMove(-5540, 3450, 2200, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    @scena.Lambda('lambda_50FD')
    def lambda_50FD():
        ChrWalkTo(0x00FE, -6490, 3450, 2230, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_50FD)

    @scena.Lambda('lambda_5118')
    def lambda_5118():
        CameraMove(-6490, 3450, 2230, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_5118)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    Sleep(500)

    Fade(500)
    ChrSetChipByIndex(0x0101, 12)
    ChrSetSubChip(0x0101, 0)
    OP_0D()
    OP_20(0x000005DC)
    OP_21()
    PlaySE(283, 0x00, 0x64)

    @scena.Lambda('lambda_515A')
    def lambda_515A():
        OP_99(0x0101, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_515A')

    DispatchAsync2(0x0101, 0x0002, lambda_515A)

    Sleep(10000)

    Sleep(2000)

    Sleep(1500)

    Sleep(1500)

    TerminateThread(0x0101, 0x02)
    Fade(500)
    ChrSetSubChip(0x0101, 8)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010291239V#295F嗯……\n',
            '还是吹不好啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291240V#292F这只口琴还\n',
            '真是气人啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291241V看起来很好吹，\n',
            '但真吹起来却这么难。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(500, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0020291242V比起你擅长的棒术，\n',
            '我倒觉得这个简单多了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '#0020291243V关键是集中力的问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010291244V#293F啊……？！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    FadeOut(500, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '#0010291245V不过，真是首节奏很好的曲子。\n',
            '旋律明快，却又有点悲伤的意境……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '#0010291246V虽然其它的曲子也都不错，\n',
            '不过我最喜欢的还是这首了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '#0010291247V对了……叫什么名字来的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(1500, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010291248V#292F……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291249V啊……确实就是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    ChrSetChipByIndex(0x0101, 12)
    ChrSetSubChip(0x0101, 0)
    OP_0D()
    OP_DB()
    PlaySE(284, 0x00, 0x64)

    @scena.Lambda('lambda_542D')
    def lambda_542D():
        OP_99(0x0101, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_542D')

    DispatchAsync2(0x0101, 0x0002, lambda_542D)

    Sleep(20000)

    TerminateThread(0x0101, 0x02)
    Fade(500)
    ChrSetSubChip(0x0101, 9)
    OP_0D()
    Sleep(500)

    OP_DC()

    ChrTalk(
        0x0101,
        (
            '#0010291250V#295F嗯嗯……不是那样的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291251V#290F对了……\n',
            '就是这种感觉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_DB()
    Fade(500)
    ChrSetChipByIndex(0x0101, 12)
    ChrSetSubChip(0x0101, 0)
    OP_0D()

    @scena.Lambda('lambda_54C4')
    def lambda_54C4():
        CameraSetDistance(2600, 15000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_54C4)

    @scena.Lambda('lambda_54D4')
    def lambda_54D4():
        OP_99(0x0101, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_54D4')

    DispatchAsync2(0x0101, 0x0002, lambda_54D4)

    PlayBGM(70)
    OP_1F(0x50, 0x000000C8)
    Sleep(10000)

    Fade(5000)
    CameraMove(-18140, 3450, 51220, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, -18140, 3450, 51220, 264)
    OP_0D()
    LoadEffect(0x00, 'map\\\\mp058_00.eff')
    Fade(2500)
    ChrSetRGBAMask(0x0101, 0, 0, 0, 150, 0)
    ChrSetChipByIndex(0x0101, 14)
    ChrSetRGBAMask(0x0101, 255, 255, 255, 255, 2500)
    OP_0D()
    OP_21()
    TerminateThread(0x0101, 0x02)
    Sleep(1000)

    OP_99(0x0101, 0x08, 0x09, 800)
    Sleep(500)

    Fade(500)
    ChrSetSubChip(0x0101, 10)
    OP_0D()
    Sleep(500)

    OP_DC()

    ChrTalk(
        0x0101,
        (
            '#0010291252V#1012F听到了吗……约修亚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291253V『星之所在』……\n',
            '我终于会吹了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0009, -14330, 3450, 50770, 270)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetRGBAMask(0x0009, 255, 255, 255, 0, 0)
    SetMessageWindowPos(300, 50, -1, -1)
    TalkSetChrName('女性的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0700291254V呵呵，很好听的曲子啊。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    PlayBGM(80)
    OP_BB(0x00, 0x01, 0x00000000)
    OP_BD()
    ChrSetChipByIndex(0x0101, 65535)

    @scena.Lambda('lambda_5699')
    def lambda_5699():
        CameraMove(-15800, 3450, 51080, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5699)

    @scena.Lambda('lambda_56B1')
    def lambda_56B1():
        OP_67(0, 8300, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_56B1)

    @scena.Lambda('lambda_56C9')
    def lambda_56C9():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 3000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_56C9)

    ChrSetDirection(0x0101, 90, 300)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0009, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010291255V#1025F#6P……妈妈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            (TxtCtl.SetColor, 0x5),
            '#0700291256V#866F正确的说……\n',
            '我并不是你的妈妈。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291257V而是由你的回忆所构建\n',
            '出的一个虚拟存在体。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291258V到现在为止发生的全部事情\n',
            '都只是你的一场梦。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291259V#1016F#6P是吗…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291260V#1025F可是、就算是在梦中，\n',
            '妈妈也还是妈妈啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291261V和妈妈在一起的每一天……\n',
            '我都非常幸福快乐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            (TxtCtl.SetColor, 0x5),
            '#0700291262V#861F呵呵……我也是呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291263V#860F不过……\n',
            '你还是要回去对吧？',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291264V#1012F#6P……嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291265V#1017F现在的我、已经想起了\n',
            '应该回去的地方……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            (TxtCtl.SetColor, 0x5),
            '#0700291266V#863F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291267V#866F他是叫约修亚吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291268V呵呵呵～很帅气的\n',
            '男孩子呢。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010291269V#1013F#6P妈、妈妈你真是的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            (TxtCtl.SetColor, 0x5),
            '#0700291270V#861F哎呀～\n',
            '小脸竟然变得通红。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291271V#866F呵呵……真是不可思议啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291272V我虽然不是真正的莱娜，\n',
            '但现在却感到非常欣慰……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291273V我的小艾丝蒂尔现在已经\n',
            '是一个可靠的大人了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291274V而且还那么认真地在恋爱……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291275V#861F身为母亲……\n',
            '没有比这个更值得高兴的了。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291276V#1026F#6P……妈妈……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290640V#1027F我……我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            (TxtCtl.SetColor, 0x5),
            '#0700291278V#866F好了啦！\n',
            '那种表情可是不行的哦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291279V你不是都已经想起应该\n',
            '回去的地方了吗？',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0009, 0x0002)
    ChrSetSubChip(0x0009, 7)

    @scena.Lambda('lambda_5BB7')
    def lambda_5BB7():
        CameraMove(-13040, 3450, 52280, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5BB7)

    @scena.Lambda('lambda_5BCF')
    def lambda_5BCF():
        OP_67(0, 3380, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_5BCF)

    @scena.Lambda('lambda_5BE7')
    def lambda_5BE7():
        OP_6C(71000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_5BE7)

    @scena.Lambda('lambda_5BF7')
    def lambda_5BF7():
        OP_6E(500, 4000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_5BF7)

    @scena.Lambda('lambda_5C07')
    def lambda_5C07():
        CameraSetDistance(1870, 4000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_5C07)

    Sleep(1000)

    PlayEffect(0x00, 0x00, 0x00FF, -8090, 4000, 54040, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(285, 0x01, 0x46)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    ChrClearFlags(0x0009, 0x0002)
    ChrSetSubChip(0x0009, 0)
    ChrSetDirection(0x0009, 306, 0)

    ChrTalk(
        0x0009,
        (
            (TxtCtl.SetColor, 0x5),
            '#0700291280V#863F#2P这场梦已经结束了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291281V那里就是通往现实世界\n',
            '的出口。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291282V#866F好孩子……\n',
            '挺起你的胸，向前去吧。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291283V#1025F#6P嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 102, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010291284V#1016F#6P嘿嘿嘿，其实…我还想再吃一次\n',
            '妈妈做的煎蛋卷呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            (TxtCtl.SetColor, 0x5),
            '#0700291285V#864F#2P哎呀呀……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291286V#860F傻孩子，要是想吃的话\n',
            '可以自己试着去做啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291287V你做出来的味道，\n',
            '肯定会和我做的一样。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291288V#1004F#6P啊……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            (TxtCtl.SetColor, 0x5),
            '#0700291289V#861F#2P家的味道…\n',
            '孩子是可以从妈妈身上继承的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291290V就算是没有亲身教导过，\n',
            '但一样也可以完全继承下来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291291V#866F我想你早就已经…\n',
            '将那种味道继承下来了。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291292V#1025F#6P是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190126V……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291294V#1012F嗯，听妈妈这么一说，\n',
            '我总算是放心了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291295V#1017F那么、妈妈……\n',
            '我，这就要走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            (TxtCtl.SetColor, 0x5),
            '#0700291296V#861F#2P嗯，别忘了替我向你爸爸\n',
            '和约修亚问好。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291297V#1017F#6P嗯！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291298V#1018F再见了……妈妈！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 70, 400)
    Sleep(500)

    @scena.Lambda('lambda_6036')
    def lambda_6036():
        CameraMove(-9890, 3450, 53440, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_6036)

    CreateThread(0x0101, 0x01, 0x00, func_1A_613F)
    Sleep(500)

    @scena.Lambda('lambda_605A')
    def lambda_605A():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_605A')

    DispatchAsync2(0x0009, 0x0003, lambda_605A)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    Sleep(500)

    StopEffect(0x00, 0x02)
    OP_24(0x011D, 0x3C)
    Sleep(300)

    OP_24(0x011D, 0x32)
    Sleep(300)

    OP_24(0x011D, 0x28)
    Sleep(300)

    OP_24(0x011D, 0x1E)
    Sleep(300)

    OP_24(0x011D, 0x14)
    Sleep(300)

    OP_24(0x011D, 0x0A)
    Sleep(300)

    OP_23(0x011D)

    @scena.Lambda('lambda_60B6')
    def lambda_60B6():
        CameraMove(-11020, 3450, 52690, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_60B6)

    WaitForThreadExit(0x0101, 0x0002)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            (TxtCtl.SetColor, 0x5),
            '#0700291299V#866F#6P再见……',
            TxtCtl.Enter,
            '\n',
            '#861F我可爱的艾丝蒂尔。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(3000, 0, -1)
    OP_0D()
    OP_20(0x00000BB8)
    OP_21()
    Sleep(1000)

    TerminateThread(0x0101, 0x01)
    MapClearFlags(0x02000000)
    OP_D6(0x01)
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/C0303._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x001A offset: 0x613F
@scena.Code('func_1A_613F')
def func_1A_613F():
    ChrWalkTo(0x00FE, -10500, 3450, 53350, 5000, 0x00)

    @scena.Lambda('lambda_6159')
    def lambda_6159():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_6159)

    ChrWalkTo(0x00FE, -8090, 3450, 54040, 5000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x001B offset: 0x617F
@scena.Code('func_1B_617F')
def func_1B_617F():
    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0011860001V#1001F这里好像可以钓上什么来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_61B7')
    def lambda_61B7():
        CameraMove(-12120, 0, 6790, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_61B7)

    @scena.Lambda('lambda_61CF')
    def lambda_61CF():
        CameraSetDistance(2800, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_61CF)

    @scena.Lambda('lambda_61DF')
    def lambda_61DF():
        OP_6C(0, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_61DF)

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
        'loc_630C',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.Eval, "OP_C0(0x0E, 0x00000005, 0xFFFFD008, 0x00000000, 0x000019DC, 0x0000013B, 0xFFFFC478, 0xFFFFF95C, 0x00002184)"),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_6306',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0073, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x0073, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0073, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6300',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0073, 0x01, 0x0020)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_62FD',
    )

    OP_28(0x0073, 0x01, 0x0002)
    OP_28(0x0073, 0x01, 0x0020)
    Sleep(400)

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '将在布莱特家发现钓鱼场的事情\n',
            '记录在游击士手册上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    def _loc_62FD(): pass

    label('loc_62FD')

    Jump('loc_6306')

    def _loc_6300(): pass

    label('loc_6300')

    OP_28(0x0073, 0x01, 0x2000)

    def _loc_6306(): pass

    label('loc_6306')

    OP_0D()
    EventEnd(0x01)

    Jump('loc_631B')

    def _loc_630C(): pass

    label('loc_630C')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_631B',
    )

    EventEnd(0x01)

    def _loc_631B(): pass

    label('loc_631B')

    Return()

# id: 0x001C offset: 0x631C
@scena.Code('func_1C_631C')
def func_1C_631C():
    FadeOut(0, 0, -1)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x09, 0xFF)

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
        (0x00000000, 'loc_6399'),
        (0x00000001, 'loc_639F'),
        (-1, 'loc_63A5'),
    )

    def _loc_6399(): pass

    label('loc_6399')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_63A5')

    def _loc_639F(): pass

    label('loc_639F')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_63A5')

    def _loc_63A5(): pass

    label('loc_63A5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_63B3',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_63B7')

    def _loc_63B3(): pass

    label('loc_63B3')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_63B7(): pass

    label('loc_63B7')

    Return()

# id: 0x001D offset: 0x63B8
@scena.Code('func_1D_63B8')
def func_1D_63B8():
    MapClearFlags(0x00000001)
    CameraMove(106730, -1920, 53920, 0)
    Sleep(100)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['雪拉扎德'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            ChrTable['提妲'],
            ChrTable['金'],
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0)
    Sleep(1000)

    Return()

# id: 0x001E offset: 0x640A
@scena.Code('func_1E_640A')
def func_1E_640A():
    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0306, 4, 0x1834)),
            Expr.Return,
        ),
        'loc_6475',
    )

    ChrTalk(
        0x0101,
        (
            '#0010291116V#290F一个人跑到外面\n',
            '是不行的哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291117V趁还没有被责备之前\n',
            '赶快回家吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_64BC')

    def _loc_6475(): pass

    label('loc_6475')

    ChrTalk(
        0x0101,
        (
            '#0010291118V#1011F……从家的方向\n',
            '传来什么声响。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '去确认一下看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_64BC(): pass

    label('loc_64BC')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    MapSetFlags(0x02000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

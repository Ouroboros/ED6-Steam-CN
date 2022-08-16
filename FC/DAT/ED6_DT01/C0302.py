import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C0302_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C0302   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0302.x'
    header.mapIndex       = 19
    header.bgm            = 21
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
            dword_00        = 0x000088B8,
            dword_04        = 0x00000000,
            dword_08        = 0x00003E80,
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
            word_3A         = 19,
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
        ('ED6_DT07/CH00310._CH', 'ED6_DT07/CH00310P._CP'),
        ('ED6_DT07/CH00311._CH', 'ED6_DT07/CH00311P._CP'),
        ('ED6_DT07/CH00314._CH', 'ED6_DT07/CH00314P._CP'),
        ('ED6_DT07/CH00360._CH', 'ED6_DT07/CH00360P._CP'),
        ('ED6_DT07/CH00361._CH', 'ED6_DT07/CH00361P._CP'),
        ('ED6_DT07/CH00364._CH', 'ED6_DT07/CH00364P._CP'),
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00101._CH', 'ED6_DT07/CH00101P._CP'),
        ('ED6_DT07/CH00110._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT07/CH00111._CH', 'ED6_DT07/CH00111P._CP'),
        ('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP'),
        ('ED6_DT07/CH00121._CH', 'ED6_DT07/CH00121P._CP'),
        ('ED6_DT07/CH00122._CH', 'ED6_DT07/CH00122P._CP'),
        ('ED6_DT07/CH02130._CH', 'ED6_DT07/CH02130P._CP'),
        ('ED6_DT07/CH02330._CH', 'ED6_DT07/CH02330P._CP'),
        ('ED6_DT07/CH02120._CH', 'ED6_DT07/CH02120P._CP'),
        ('ED6_DT07/CH01380._CH', 'ED6_DT07/CH01380P._CP'),
        ('ED6_DT09/CH10010._CH', 'ED6_DT09/CH10010P._CP'),
        ('ED6_DT09/CH10011._CH', 'ED6_DT09/CH10011P._CP'),
        ('ED6_DT09/CH10280._CH', 'ED6_DT09/CH10280P._CP'),
        ('ED6_DT09/CH10281._CH', 'ED6_DT09/CH10281P._CP'),
        ('ED6_DT09/CH10230._CH', 'ED6_DT09/CH10230P._CP'),
        ('ED6_DT09/CH10231._CH', 'ED6_DT09/CH10231P._CP'),
        ('ED6_DT09/CH10240._CH', 'ED6_DT09/CH10240P._CP'),
        ('ED6_DT09/CH10241._CH', 'ED6_DT09/CH10241P._CP'),
    ]

# id: 0x10001 offset: 0x172
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '乔丝特',
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
            name                = '雷古',
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
        ScenaNpcData(
            name                = '蒂诺',
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
        ScenaNpcData(
            name                = '莱尔',
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
        ScenaNpcData(
            name                = '吉尔',
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
            name                = '空贼艇',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0080,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '空贼艇（影）',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0080,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '目标用摄像机',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0080,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x272
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = 52120,
            z           = 240,
            y           = -16250,
            word_0C     = 0x005D,
            word_0E     = 0x0015,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x004D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 61090,
            z           = -350,
            y           = 5020,
            word_0C     = 0x00ED,
            word_0E     = 0x0017,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0047,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 73730,
            z           = -80,
            y           = -3560,
            word_0C     = 0x00D0,
            word_0E     = 0x0017,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0047,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 53060,
            z           = -210,
            y           = 8160,
            word_0C     = 0x003D,
            word_0E     = 0x0013,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0042,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x2E2
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -74120,
            y           = -1000,
            z           = -14700,
            range       = -71420,
            dword_10    = 0x000003E8,
            dword_14    = 0xFFFFA92A,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000002,
        ),
    )

# id: 0x10004 offset: 0x302
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 72710,
            triggerZ            = 0,
            triggerY            = 10290,
            triggerRange        = 1500,
            actorX              = 72710,
            actorZ              = 1500,
            actorY              = 10290,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 45900,
            triggerZ            = -60,
            triggerY            = 4140,
            triggerRange        = 1000,
            actorX              = 45300,
            actorZ              = 1440,
            actorY              = 3640,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x34A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0050, 6, 0x286)),
            Expr.Return,
        ),
        'loc_35F',
    )

    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_64(0x00, 0x0001)

    def _loc_35F(): pass

    label('loc_35F')

    Return()

# id: 0x0001 offset: 0x360
@scena.Code('func_01_360')
def func_01_360():
    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x385),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_37E',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x57),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_26(119)
    OP_26(121)
    OP_26(502)

    def _loc_37E(): pass

    label('loc_37E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0052, 3, 0x293)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_390',
    )

    OP_6F(0x0004, 0)

    Jump('loc_397')

    def _loc_390(): pass

    label('loc_390')

    OP_6F(0x0004, 60)

    def _loc_397(): pass

    label('loc_397')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0050, 6, 0x286)),
            Expr.Return,
        ),
        'loc_3AC',
    )

    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_64(0x00, 0x0001)

    def _loc_3AC(): pass

    label('loc_3AC')

    OP_10(0x01, 0x01)

    Return()

# id: 0x0002 offset: 0x3B0
@scena.Code('func_02_3B0')
def func_02_3B0():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 6, 0x266)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 4, 0x264)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2B40',
    )

    MapClearFlags(0x00000001)
    EventBegin(0x00)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0008, 0)
    ChrTurnDirection(0x0102, 0x0008, 0)
    ChrTurnDirection(0x0103, 0x0008, 0)
    ChrSetPos(0x0008, -60860, -320, 5360, 135)
    ChrSetPos(0x0009, -60550, -150, 2920, 341)
    ChrSetPos(0x000A, -59230, -300, 3520, 317)
    ChrSetPos(0x000B, -58760, -350, 5070, 270)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0008, 0x0008)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x0009, 0x0008)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000A, 0x0008)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000B, 0x0008)
    OP_20(0x00000FA0)

    @scena.Lambda('lambda_0499')
    def lambda_0499():
        OP_67(0, 6280, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_0499)

    @scena.Lambda('lambda_04B1')
    def lambda_04B1():
        OP_6C(0, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_04B1)

    CameraMove(-59790, -340, 4800, 4000)
    ChrSetPos(0x0101, -57980, 130, -9190, 356)
    ChrSetPos(0x0102, -56650, 110, -9280, 356)
    ChrSetPos(0x0103, -57400, -130, -10020, 356)
    PlaySE(128, 0x00, 0x64)
    LoadEffect(0x00, 'map\\\\evsepith.eff')
    PlayEffect(0x00, 0x00, 0x0008, 0, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayBGM(87)

    ChrTalk(
        0x0008,
        (
            '#0090011226V#219F哼哼哼……\n',
            '真是简单透顶了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090011227V#219F本小姐只不过略施小计，\n',
            '就能拿到这么棒的东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090011228V#219F这下可以向大哥他们炫耀一下啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#1040011229V#6P是啊是啊，大小姐真是厉害呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1040011230V#6P普通人就算穿上校服，\n',
            '也不见得有那么一流的演技啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1050011231V真不愧是原贵族大小姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0090011232V#219F哼……\n',
            '过去的事就别提了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090011233V#219F不过，这种装扮也能被骗倒，\n',
            '那些家伙还真是有眼光啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090011234V#219F不管是那个喜欢做老好人的市长，\n',
            '还是那个没大脑的女游击士……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090011235V#410F啊哈哈，他们真是太好骗了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x000A, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0009, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x000B, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(1000)

    @scena.Lambda('lambda_080D')
    def lambda_080D():
        CameraMove(-58480, 30, -5380, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_080D)

    @scena.Lambda('lambda_0825')
    def lambda_0825():
        OP_6C(0, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0825)

    Sleep(1500)

    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010011236V#005F（说、说什么～！？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020011237V#012F（冷静点……\n',
            ' 再听听他们还会说些什么。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
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
        10,
        0,
        (
            TXT(0x00, '（这叫我怎么冷～静！）\n'),
            TXT(0x01, '（唔……只好忍一下。）\n'),
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
        'loc_BCC',
    )

    ChrSetChipByIndex(0x0101, 6)

    ChrTalk(
        0x0101,
        (
            '#0010011238V#005F（这叫我怎么冷～静！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_096D')
    def lambda_096D():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_096D)

    @scena.Lambda('lambda_097B')
    def lambda_097B():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_097B)

    ChrWalkTo(0x0101, -59020, 20, -9230, 6000, 0x00)

    @scena.Lambda('lambda_099D')
    def lambda_099D():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_099D')

    DispatchAsync2(0x0102, 0x0001, lambda_099D)

    @scena.Lambda('lambda_09AE')
    def lambda_09AE():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_09AE')

    DispatchAsync2(0x0103, 0x0001, lambda_09AE)

    ChrWalkTo(0x0101, -60410, 0, -8140, 6000, 0x00)

    @scena.Lambda('lambda_09D3')
    def lambda_09D3():
        ChrWalkTo(0x00FE, -60620, 30, -2490, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_09D3)

    ChrTalk(
        0x0102,
        (
            '#0020011239V#014F（啊啊！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030011240V#025F（又冲动了啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010011241V#005F#6P哼～！\n',
            '你们这些坏蛋，一个都别想逃！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0102, 8)
    ChrSetChipByIndex(0x0103, 10)

    @scena.Lambda('lambda_0A7F')
    def lambda_0A7F():
        OP_6C(45000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0A7F)

    @scena.Lambda('lambda_0A8F')
    def lambda_0A8F():
        CameraMove(-60120, -80, 1150, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0A8F)

    @scena.Lambda('lambda_0AA7')
    def lambda_0AA7():
        ChrWalkTo(0x00FE, -60670, 20, -8860, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0AA7)

    Sleep(600)

    @scena.Lambda('lambda_0AC7')
    def lambda_0AC7():
        ChrWalkTo(0x00FE, -60670, 20, -8860, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_0AC7)

    WaitForThreadExit(0x0102, 0x0001)

    @scena.Lambda('lambda_0AE7')
    def lambda_0AE7():
        ChrWalkTo(0x00FE, -61520, -140, -3820, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0AE7)

    WaitForThreadExit(0x0103, 0x0001)

    @scena.Lambda('lambda_0B07')
    def lambda_0B07():
        ChrWalkTo(0x00FE, -59700, 10, -3820, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_0B07)

    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_0B8D')
    def lambda_0B8D():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0B8D)

    @scena.Lambda('lambda_0B9B')
    def lambda_0B9B():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0B9B)

    @scena.Lambda('lambda_0BA9')
    def lambda_0BA9():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0BA9)

    @scena.Lambda('lambda_0BB7')
    def lambda_0BB7():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0BB7)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)

    Jump('loc_1027')

    def _loc_BCC(): pass

    label('loc_BCC')

    OP_2B(0x001A, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010011242V#509F（唔……只好忍一下。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CameraMove(-59850, -340, 4500, 1500)

    ChrTalk(
        0x000B,
        (
            '#0990011243V可是我听说，\n',
            '那些小鬼好像还蛮强的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0990011244V矿山里出现的魔兽\n',
            '一下子就被他们收拾掉了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090011245V#219F矿山？\n',
            '啊啊，是说你行动失败的那件事吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090011246V#219F要是成功了，\n',
            '我就不必特意去演那出猴戏啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0990011247V对、对不起，大小姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090011248V#219F结局好就万事ＯＫ啦。\n',
            '话说回来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090011249V#219F那个……\n',
            '那种水平也能当上游击士，\n',
            '真是笑死本小姐了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090011250V#219F特别是那个没大脑的笨女人！\n',
            '对本小姐毫无戒心，\n',
            '还说什么『好不容易认识到一个朋友』！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090011251V#410F啊哈哈哈哈！\n',
            '我都忍不住要笑死了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3P#1K哇哈哈哈哈！',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x000B,
        (
            '#2P#1K嘎哈哈哈哈！',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x000A,
        (
            '#1050011254V#4P#1K呀哈哈哈哈！',
            TxtCtl.Enter,
        ),
    )

    Sleep(500)

    OP_56(0x01)
    OP_59()
    ChrSetChipByIndex(0x0101, 6)
    ChrSetChipByIndex(0x0102, 8)
    ChrSetChipByIndex(0x0103, 10)
    ChrSetPos(0x0101, -60670, 20, -8860, 270)
    ChrSetPos(0x0102, -60670, 20, -8860, 270)
    ChrSetPos(0x0103, -60670, 20, -8860, 270)

    ChrTalk(
        0x0101,
        (
            '#0010011255V#5P……真的那么好笑吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_0F79')
    def lambda_0F79():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0F79)

    @scena.Lambda('lambda_0F87')
    def lambda_0F87():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0F87)

    @scena.Lambda('lambda_0F95')
    def lambda_0F95():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0F95)

    @scena.Lambda('lambda_0FA3')
    def lambda_0FA3():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0FA3)

    @scena.Lambda('lambda_0FB1')
    def lambda_0FB1():
        ChrWalkTo(0x00FE, -60610, 30, -2480, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0FB1)

    Sleep(300)

    @scena.Lambda('lambda_0FD1')
    def lambda_0FD1():
        ChrWalkTo(0x00FE, -61520, -140, -3820, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0FD1)

    Sleep(300)

    @scena.Lambda('lambda_0FF1')
    def lambda_0FF1():
        ChrWalkTo(0x00FE, -59700, 10, -3820, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_0FF1)

    @scena.Lambda('lambda_100C')
    def lambda_100C():
        OP_6C(45000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_100C)

    CameraMove(-60120, -80, 1150, 1500)

    def _loc_1027(): pass

    label('loc_1027')

    WaitForThreadExit(0x0008, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#0090011256V#411F你、你们是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010011257V#582F一直忍着不出声，\n',
            '结果就没大脑啦笨女人啦之类的，\n',
            '越说越来劲，越说越放肆……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    ChrTalk(
        0x0101,
        (
            '#0010011258V#005F#3S准备好受死了吧！！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x000B, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrSetChipByIndex(0x0009, 3)
    ChrSetChipByIndex(0x000B, 3)
    ChrSetChipByIndex(0x000A, 3)

    ChrTalk(
        0x000B,
        (
            '#0990011259V是游击士！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1040011260V为什么会发现这儿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030011261V#027F从市长家偷走七耀石的手段\n',
            '的确相当高明……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030011262V#027F呵呵，不过最后还是被我们逮个正着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020011263V#012F现根据游击士协会的规定，\n',
            '你们涉嫌私闯民宅，破坏财物和盗窃，\n',
            '我们要代表游击士协会将你们逮捕。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020011264V请你们马上放下武器，不要做多余的抵抗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#1050011265V哇哇……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0990011266V大、大小姐，该怎么办！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090011267V#412F有什么好怕的！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090011268V就算是游击士，\n',
            '也只不过是女人和小孩罢了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090011269V要让他们尝尝\n',
            '我们『卡普亚一家』的厉害！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010011270V#005F什么女人和小孩啊！\n',
            '不要说得自己有多伟大！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010011271V#005F啊～真是快要气炸啦！\n',
            '我一定要让你们输得心服口服！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090011272V#219F那正是我要说的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_141F')
    def lambda_141F():
        CameraSetDistance(3000, 1000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_141F)

    @scena.Lambda('lambda_142F')
    def lambda_142F():
        CameraMove(-60120, -80, 3200, 1000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_142F)

    Sleep(500)

    StopEffect(0x00, 0x00)
    PlaySE(203, 0x00, 0x64)
    ChrSetDirection(0x0008, 32, 800)
    ChrSetChipByIndex(0x0008, 0)
    ChrSetDirection(0x0008, 330, 800)
    ChrSetDirection(0x0008, 180, 800)
    Sleep(500)

    WaitForThreadExit(0x0008, 0x0002)

    ChrTalk(
        0x0008,
        (
            '#0090011273V#210F你们，给我上！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#1P#1K收到！',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x000A,
        (
            '#2P#1K收到！',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x0009,
        (
            '#1040011276V#4P#1K收到！',
            TxtCtl.Enter,
        ),
    )

    Sleep(500)

    OP_56(0x01)
    OP_59()

    @scena.Lambda('lambda_14E4')
    def lambda_14E4():
        CameraMove(-60120, -80, 1150, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_14E4)

    ChrSetChipByIndex(0x000A, 4)

    @scena.Lambda('lambda_1501')
    def lambda_1501():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1501)

    ChrSetChipByIndex(0x0009, 4)

    @scena.Lambda('lambda_151B')
    def lambda_151B():
        OP_92(0x00FE, 0x0102, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_151B)

    ChrSetChipByIndex(0x000B, 4)

    @scena.Lambda('lambda_1535')
    def lambda_1535():
        OP_92(0x00FE, 0x0103, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1535)

    ChrSetChipByIndex(0x0008, 1)

    @scena.Lambda('lambda_154F')
    def lambda_154F():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_154F)

    Sleep(400)

    Battle(0x00000385, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_157C'),
        (-1, 'loc_1581'),
    )

    def _loc_157C(): pass

    label('loc_157C')

    OP_B4(0x00)

    Jump('loc_1581')

    def _loc_1581(): pass

    label('loc_1581')

    EventBegin(0x00)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x0009, 0xFF)
    CameraMove(-56340, -330, 2350, 0)
    OP_67(0, 6280, -10000, 0)
    CameraSetDistance(2900, 0)
    OP_6C(68000, 0)
    OP_6E(291, 0)
    ChrSetPos(0x0103, -59720, -110, 320, 26)
    ChrSetPos(0x0102, -57190, -230, -570, 20)
    ChrSetPos(0x0101, -57720, -260, 480, 4)

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0102,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0103,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x0103, 65535)

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0008, 2)
    ChrSetChipByIndex(0x0009, 5)
    ChrSetChipByIndex(0x000B, 5)
    ChrSetChipByIndex(0x000A, 5)
    ChrSetPos(0x0008, -55850, -280, 3840, 206)
    ChrSetPos(0x0009, -56410, -160, 5250, 213)
    ChrSetPos(0x000A, -54320, -160, 4210, 216)
    ChrSetPos(0x000B, -54160, -50, 5560, 270)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0090011277V#216F怎、怎么可能……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010011278V#502F嘿嘿，小菜一碟⊙\n',
            '这就是小看游击士的后果哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010011279V#507F我说你，快点把那东西还给我们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_92(0x0101, 0x0008, 800, 3000, 0x00)
    Sleep(300)

    LoadEffect(0x00, 'map\\\\evsepith.eff')
    PlayEffect(0x00, 0x00, 0x0101, 0, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    PlaySE(128, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '取回了',
            (TxtCtl.SetColor, 0x2),
            '七耀石的结晶',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#0090011280V#216F啊啊……本小姐的七耀石……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveTo(0x0101, -56760, -320, 2120, 2000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010011281V#582F不是你的，\n',
            '是洛连特全体市民的！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010011282V#009F真是的，脸皮这么厚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    StopEffect(0x00, 0x00)

    @scena.Lambda('lambda_18BE')
    def lambda_18BE():
        ChrMoveTo(0x00FE, -57150, -280, 730, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_18BE)

    ChrWalkTo(0x0103, -58680, -250, 1100, 3000, 0x00)
    ChrWalkTo(0x0103, -57590, -300, 1700, 3000, 0x00)
    ChrTurnDirection(0x0103, 0x0008, 400)

    ChrTalk(
        0x0103,
        (
            '#0030011283V#021F是啊，既然结晶已经取回来了，\n',
            '是不是到了该坦白交待的时间了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030011284V#020F之前你说了很有趣的名字呢。\n',
            '好像是『卡普亚一家』什么的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0090011285V#216F唔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090011286V#211F不、不知道啊，你在说什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0103, 10)

    ExecExpressionWithValue(
        0x0103,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x0103,
        (
            '#0030011287V#027F呵呵，真是嘴硬啊。\n',
            '不过我就是喜欢这样的孩子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0103, 12)
    PlaySE(502, 0x00, 0x64)
    OP_99(0x0103, 0x00, 0x04, 2000)

    @scena.Lambda('lambda_1A77')
    def lambda_1A77():
        OP_99(0x0103, 0x07, 0x09, 2000)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_1A77)

    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrJumpTo(0x0008, -55670, -220, 4250, 500, 5000)
    ChrSetChipByIndex(0x0008, 13)

    ChrTalk(
        0x0008,
        (
            '#0090011288V#213F呀！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090011289V#214F这、这样多危险啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030011290V#021F如果你不肯开口，\n',
            '就只好问问你的身体了，不是吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030011291V#021F没关系的，姐姐我会很温柔的哦㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x0103,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0103, 65535)
    ChrWalkTo(0x0103, -56760, -320, 2120, 2000, 0x00)
    ChrTurnDirection(0x0103, 0x0008, 400)

    ExecExpressionWithValue(
        0x0103,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0103, 10)

    @scena.Lambda('lambda_1BA7')
    def lambda_1BA7():
        OP_99(0x00FE, 0x00, 0x07, 1000)
        Yield()

        Jump('lambda_1BA7')

    DispatchAsync2(0x0103, 0x0001, lambda_1BA7)

    OP_62(0x0008, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    OP_9E(0x0008, 15, 0, 300, 4000)
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0008,
        (
            '#0090011292V#216F唔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090011293V#216F不、不要过来，离远点！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0102, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    OP_63(0x0101)
    OP_63(0x0102)

    ChrTalk(
        0x0101,
        (
            '#0010011294V#509F（雪拉姐绝对是在享受呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020011295V#019F（不招惹瘟神也就不会有报应了吧……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(121, 0x01, 0x5A)
    Sleep(200)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0102, 0x0103, 0)
    ChrSetPos(0x000D, -37060, 300, -13200, 291)
    ChrTurnDirection(0x0102, 0x000D, 800)
    ChrSetChipByIndex(0x0102, 8)

    @scena.Lambda('lambda_1D26')
    def lambda_1D26():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1D26)

    ChrTalk(
        0x0102,
        (
            '#0020011296V#016F雪拉姐姐，危险！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1D5B')
    def lambda_1D5B():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1D5B)

    TerminateThread(0x0103, 0xFF)
    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x0103, 0x000D, 800)
    ChrJumpTo(0x0103, -58870, -200, 260, 1000, 6000)
    LoadEffect(0x00, 'map\\\\mp003_00.eff')
    PlayEffect(0x00, 0xFF, 0x00FF, -53890, -320, 1090, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(503, 0x00, 0x64)
    OP_7C(0, 200, 3000, 100)
    Sleep(100)

    PlayEffect(0x00, 0xFF, 0x00FF, -54980, -320, 1650, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(503, 0x00, 0x64)
    OP_7C(0, 200, 3000, 100)
    Sleep(100)

    PlayEffect(0x00, 0xFF, 0x00FF, -56310, -330, 2190, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(503, 0x00, 0x64)
    OP_7C(0, 200, 3000, 100)
    Sleep(100)

    PlayEffect(0x00, 0xFF, 0x00FF, -57630, -300, 2760, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(503, 0x00, 0x64)
    OP_7C(0, 200, 3000, 100)
    Sleep(100)

    PlayEffect(0x00, 0xFF, 0x00FF, -58980, -300, 3360, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(503, 0x00, 0x64)
    OP_7C(0, 200, 3000, 100)
    Sleep(500)

    ChrTalk(
        0x0103,
        (
            '#0030011297V#023F导力炮！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010011298V#004F雪拉姐，没事吧！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030011299V#024F没事！\n',
            '注意头顶！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0101, 6)

    @scena.Lambda('lambda_1FC4')
    def lambda_1FC4():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1FC4)

    @scena.Lambda('lambda_1FD2')
    def lambda_1FD2():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1FD2)

    @scena.Lambda('lambda_1FE0')
    def lambda_1FE0():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_1FE0)

    @scena.Lambda('lambda_1FEE')
    def lambda_1FEE():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1FEE)

    OP_72(0x0002, 0x0004)
    OP_72(0x0003, 0x0004)
    ChrSetFlags(0x000D, 0x0004)
    ChrSetFlags(0x000D, 0x0040)
    ChrSetFlags(0x000E, 0x0004)
    ChrSetFlags(0x000E, 0x0040)
    OP_A1(0x000D, 0x0002)
    OP_A1(0x000E, 0x0003)
    CreateThread(0x000D, 0x01, 0x00, func_05_2BC7)
    CreateThread(0x000E, 0x01, 0x00, func_06_2F02)
    OP_B0(0x0002, 0x1E)

    @scena.Lambda('lambda_2036')
    def lambda_2036():
        OP_6E(511, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2036)

    OP_24(0x0079, 0x5A)
    Sleep(500)

    OP_24(0x0079, 0x64)
    Sleep(2500)

    @scena.Lambda('lambda_2058')
    def lambda_2058():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_2058')

    DispatchAsync2(0x0008, 0x0001, lambda_2058)

    @scena.Lambda('lambda_2069')
    def lambda_2069():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_2069')

    DispatchAsync2(0x0101, 0x0001, lambda_2069)

    @scena.Lambda('lambda_207A')
    def lambda_207A():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_207A')

    DispatchAsync2(0x0103, 0x0001, lambda_207A)

    @scena.Lambda('lambda_208B')
    def lambda_208B():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_208B')

    DispatchAsync2(0x0102, 0x0001, lambda_208B)

    @scena.Lambda('lambda_209C')
    def lambda_209C():
        CameraMove(-61600, 3050, 5140, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_209C)

    @scena.Lambda('lambda_20B4')
    def lambda_20B4():
        OP_6C(33000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_20B4)

    Sleep(5000)

    CreateThread(0x0009, 0x01, 0x00, func_07_31CC)
    CreateThread(0x000B, 0x01, 0x00, func_07_31CC)
    CreateThread(0x000A, 0x01, 0x00, func_07_31CC)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010011300V#580F飞、飞艇？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090011301V#211F啊哈哈，形势逆转了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_212F')
    def lambda_212F():
        ChrWalkTo(0x00FE, -60900, -320, 4560, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_212F)

    Sleep(200)

    ChrSetChipByIndex(0x0009, 4)

    @scena.Lambda('lambda_2154')
    def lambda_2154():
        ChrWalkTo(0x00FE, -59470, -370, 5530, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2154)

    Sleep(200)

    ChrSetChipByIndex(0x000B, 4)

    @scena.Lambda('lambda_2179')
    def lambda_2179():
        ChrWalkTo(0x00FE, -59800, -320, 4160, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_2179)

    Sleep(100)

    ChrSetChipByIndex(0x000A, 4)

    @scena.Lambda('lambda_219E')
    def lambda_219E():
        ChrWalkTo(0x00FE, -61020, -180, 3130, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_219E)

    WaitForThreadExit(0x0008, 0x0001)
    ChrSetPos(0x000C, -67370, 8500, 6060, 123)
    ChrTurnDirection(0x0008, 0x000C, 0)
    WaitForThreadExit(0x0009, 0x0001)
    ChrSetChipByIndex(0x0009, 3)
    WaitForThreadExit(0x000B, 0x0001)
    ChrSetChipByIndex(0x000B, 3)
    WaitForThreadExit(0x000A, 0x0001)
    ChrSetChipByIndex(0x000A, 3)
    WaitForThreadExit(0x0101, 0x0002)

    @scena.Lambda('lambda_21F9')
    def lambda_21F9():
        CameraMove(-62640, 4570, 5610, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_21F9)

    @scena.Lambda('lambda_2211')
    def lambda_2211():
        OP_6E(363, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2211)

    @scena.Lambda('lambda_2221')
    def lambda_2221():
        OP_67(0, 10510, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2221)

    Sleep(1000)

    PlaySE(106, 0x00, 0x64)
    OP_6F(0x0002, 60)
    OP_70(0x0002, 95)
    OP_73(0x0002)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetFlags(0x000C, 0x0004)
    ChrMoveTo(0x000C, -67370, 9400, 6060, 3000, 0x00)
    Sleep(500)

    ChrTalk(
        0x000C,
        (
            '#0290011302V#201F乔丝特，没事吧！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090011303V#214F吉尔哥！\n',
            '你来得太慢啦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090011304V#210F算了，赶快来帮我教训他们吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0290011305V#201F不，我们要马上离开洛连特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290011306V你不在的时候，\n',
            '柏斯发生了点麻烦事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090011307V#213F麻、麻烦事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0290011308V#201F好了，赶快上来！\n',
            '再磨蹭的话就不管你了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveTo(0x000C, -67370, 8000, 6060, 3000, 0x00)
    ChrSetFlags(0x000C, 0x0080)
    PlaySE(206, 0x00, 0x64)
    OP_6F(0x0002, 95)
    OP_70(0x0002, 160)

    ChrTalk(
        0x0008,
        (
            '#0090011309V#215F唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0008, 0x0004)
    ChrSetFlags(0x0009, 0x0004)
    ChrSetFlags(0x000B, 0x0004)
    ChrSetFlags(0x000A, 0x0004)

    @scena.Lambda('lambda_241D')
    def lambda_241D():
        ChrWalkTo(0x00FE, -65269, -200, 5050, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_241D)

    Sleep(200)

    @scena.Lambda('lambda_243D')
    def lambda_243D():
        CameraMove(-61640, -300, 5890, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_243D)

    @scena.Lambda('lambda_2455')
    def lambda_2455():
        OP_67(0, 9430, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2455)

    @scena.Lambda('lambda_246D')
    def lambda_246D():
        OP_6C(9000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_246D)

    ChrSetChipByIndex(0x0009, 4)

    @scena.Lambda('lambda_2482')
    def lambda_2482():
        ChrWalkTo(0x00FE, -83020, -330, 26640, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2482)

    Sleep(200)

    ChrSetChipByIndex(0x000B, 4)

    @scena.Lambda('lambda_24A7')
    def lambda_24A7():
        ChrWalkTo(0x00FE, -83020, -330, 26640, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_24A7)

    Sleep(100)

    ChrSetChipByIndex(0x000A, 4)

    @scena.Lambda('lambda_24CC')
    def lambda_24CC():
        ChrWalkTo(0x00FE, -83020, -330, 26640, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_24CC)

    @scena.Lambda('lambda_24E7')
    def lambda_24E7():
        ChrWalkTo(0x00FE, -58890, -280, 2009, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_24E7)

    @scena.Lambda('lambda_2502')
    def lambda_2502():
        ChrWalkTo(0x00FE, -60400, 20, -1210, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_2502)

    WaitForThreadExit(0x0008, 0x0001)
    ChrClearFlags(0x0008, 0x0004)
    ChrSetBattleFlags(0x0008, 0x0020)
    ChrJumpTo(0x0008, -66120, 550, 4700, 1000, 8000)
    ChrSetDirection(0x0008, 160, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010011310V#005F给、给我慢着！喂！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090011311V#214F#5P你们给我记住！\n',
            '别以为这样就算赢了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090011312V#214F总有一天要一决胜负！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_25DC')
    def lambda_25DC():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_25DC')

    DispatchAsync2(0x0101, 0x0000, lambda_25DC)

    @scena.Lambda('lambda_25ED')
    def lambda_25ED():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_25ED')

    DispatchAsync2(0x0103, 0x0000, lambda_25ED)

    @scena.Lambda('lambda_25FE')
    def lambda_25FE():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_25FE')

    DispatchAsync2(0x0102, 0x0000, lambda_25FE)

    PlaySE(205, 0x00, 0x64)
    CreateThread(0x000D, 0x01, 0x00, func_08_31F3)
    CreateThread(0x000E, 0x01, 0x00, func_09_33F4)
    CreateThread(0x0008, 0x03, 0x00, func_04_2B61)

    @scena.Lambda('lambda_2629')
    def lambda_2629():
        CameraMove(-68070, 1230, 7050, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2629)

    @scena.Lambda('lambda_2641')
    def lambda_2641():
        OP_6C(69000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2641)

    @scena.Lambda('lambda_2651')
    def lambda_2651():
        CameraSetDistance(4000, 6000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_2651)

    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    Sleep(3000)

    @scena.Lambda('lambda_2675')
    def lambda_2675():
        CameraMove(-60410, -60, 750, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2675)

    @scena.Lambda('lambda_268D')
    def lambda_268D():
        OP_67(0, 9000, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_268D)

    Sleep(3000)

    StopEffect(0x02, 0x00)
    OP_20(0x000007D0)
    FadeOut(1500, 0, -1)
    OP_0D()
    OP_21()
    CameraMove(-60200, -110, 1680, 0)
    OP_67(0, 9000, -10000, 0)
    CameraSetDistance(2009, 0)
    OP_6C(90000, 0)
    OP_6E(363, 0)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetPos(0x0101, -60700, -40, 950, 225)
    ChrSetPos(0x0102, -60790, -80, 2280, 225)
    ChrSetPos(0x0103, -59390, -210, 1740, 225)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x0103, 65535)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0103, 0xFF)
    OP_24(0x0079, 0x5F)
    OP_24(0x00CD, 0x5F)
    Sleep(100)

    OP_24(0x0079, 0x5A)
    OP_24(0x00CD, 0x5A)
    Sleep(100)

    OP_24(0x0079, 0x55)
    OP_24(0x00CD, 0x55)
    Sleep(100)

    OP_24(0x0079, 0x50)
    OP_24(0x00CD, 0x50)
    Sleep(50)

    OP_24(0x0079, 0x46)
    OP_24(0x00CD, 0x46)
    Sleep(50)

    OP_24(0x0079, 0x3C)
    OP_24(0x00CD, 0x3C)
    Sleep(50)

    OP_24(0x0079, 0x32)
    OP_24(0x00CD, 0x32)
    Sleep(50)

    OP_23(0x0079)
    OP_23(0x00CD)
    Sleep(500)

    PlayBGM(21)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010011313V#002F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030011314V#522F伤脑筋了。\n',
            '没想到连那种东西都出来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030011315V#021F啊哈哈，被她略占上风了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010011316V#007F现在不是笑的时候吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010011317V#003F唔～真不甘心啊～！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0102, 135, 400)

    ChrTalk(
        0x0102,
        (
            '#0020011318V#019F算了吧。\n',
            '反正七耀石也已经取回来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020011319V#012F那个……\n',
            '那些人应该就是空贼吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0103, 270, 400)

    ChrTalk(
        0x0103,
        (
            '#0030011320V#026F嗯，应该没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030011321V看起来，他们就是那群\n',
            '盘踞在柏斯地区的犯罪团伙……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030011322V#022F没想到会到洛连特\n',
            '这种乡下地方来作案。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010011323V#509F管他是空贼还是山贼，\n',
            '反正通通都不是好家伙啦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010011324V下次再让我遇到那个嚣张的男人婆，\n',
            '一定要打她个稀里哗啦噼里啪啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020011325V#019F稀里哗啦噼里啪啦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(500)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '经过众人的调查和森林一战后，\n',
            '市长家被抢走的七耀石结晶终于顺利地取回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '把七耀石还给市长之后，\n',
            '艾丝蒂尔等人为了报告事情的经过而回到协会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetScenaFlags(ScenaFlag(0x004C, 6, 0x266))
    OP_28(0x001B, 0x01, 0x0080)
    OP_28(0x001B, 0x01, 0x0100)
    Sleep(1000)

    NewScene('ED6_DT01/T0121._SN', 103, 0, 0)
    IdleLoop()

    def _loc_2B40(): pass

    label('loc_2B40')

    Return()

# id: 0x0003 offset: 0x2B41
@scena.Code('func_03_2B41')
def func_03_2B41():
    OP_24(0x0079, 0x46)
    Sleep(500)

    OP_24(0x0079, 0x50)
    Sleep(500)

    OP_24(0x0079, 0x5A)
    Sleep(500)

    OP_24(0x0079, 0x64)

    Return()

# id: 0x0004 offset: 0x2B61
@scena.Code('func_04_2B61')
def func_04_2B61():
    Sleep(6000)

    OP_24(0x0079, 0x64)
    Sleep(200)

    OP_24(0x0079, 0x5A)
    Sleep(200)

    OP_24(0x0079, 0x50)
    Sleep(200)

    OP_24(0x0079, 0x46)
    Sleep(200)

    OP_24(0x0079, 0x3C)
    Sleep(200)

    OP_24(0x0079, 0x32)
    Sleep(200)

    OP_24(0x0079, 0x28)
    Sleep(200)

    OP_24(0x0079, 0x1E)
    Sleep(200)

    OP_24(0x0079, 0x14)
    Sleep(200)

    OP_24(0x0079, 0x0A)
    Sleep(200)

    OP_23(0x0077)
    OP_23(0x0079)

    Return()

# id: 0x0005 offset: 0x2BC7
@scena.Code('func_05_2BC7')
def func_05_2BC7():
    ChrSetPos(0x00FE, -37060, 17100, -13200, 291)
    LoadEffect(0x01, 'map\\\\mp021_00.eff')

    @scena.Lambda('lambda_2BF2')
    def lambda_2BF2():
        ChrWalkTo(0x00FE, -68840, 10300, 9400, 6200, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2BF2)

    Sleep(3000)

    @scena.Lambda('lambda_2C12')
    def lambda_2C12():
        ChrMoveTo(0x00FE, -68840, 9300, 9400, 5500, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2C12)

    Sleep(500)

    @scena.Lambda('lambda_2C32')
    def lambda_2C32():
        ChrMoveTo(0x00FE, -68840, 9300, 9400, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2C32)

    @scena.Lambda('lambda_2C4D')
    def lambda_2C4D():
        ChrSetDirection(0x00FE, 155, 6)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2C4D)

    Sleep(100)

    @scena.Lambda('lambda_2C60')
    def lambda_2C60():
        ChrSetDirection(0x00FE, 155, 8)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2C60)

    Sleep(100)

    @scena.Lambda('lambda_2C73')
    def lambda_2C73():
        ChrSetDirection(0x00FE, 155, 10)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2C73)

    Sleep(100)

    @scena.Lambda('lambda_2C86')
    def lambda_2C86():
        ChrSetDirection(0x00FE, 155, 12)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2C86)

    Sleep(100)

    @scena.Lambda('lambda_2C99')
    def lambda_2C99():
        ChrSetDirection(0x00FE, 155, 14)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2C99)

    Sleep(100)

    @scena.Lambda('lambda_2CAC')
    def lambda_2CAC():
        ChrSetDirection(0x00FE, 155, 16)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2CAC)

    Sleep(100)

    @scena.Lambda('lambda_2CBF')
    def lambda_2CBF():
        ChrSetDirection(0x00FE, 155, 18)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2CBF)

    Sleep(100)

    @scena.Lambda('lambda_2CD2')
    def lambda_2CD2():
        ChrSetDirection(0x00FE, 155, 20)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2CD2)

    Sleep(100)

    @scena.Lambda('lambda_2CE5')
    def lambda_2CE5():
        ChrSetDirection(0x00FE, 155, 22)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2CE5)

    Sleep(100)

    @scena.Lambda('lambda_2CF8')
    def lambda_2CF8():
        ChrSetDirection(0x00FE, 155, 25)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2CF8)

    @scena.Lambda('lambda_2D06')
    def lambda_2D06():
        ChrMoveTo(0x00FE, -68840, 7300, 9400, 4500, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2D06)

    Sleep(500)

    @scena.Lambda('lambda_2D26')
    def lambda_2D26():
        ChrMoveTo(0x00FE, -68840, 7300, 9400, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2D26)

    Sleep(100)

    @scena.Lambda('lambda_2D46')
    def lambda_2D46():
        ChrSetDirection(0x00FE, 155, 28)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2D46)

    Sleep(100)

    @scena.Lambda('lambda_2D59')
    def lambda_2D59():
        ChrSetDirection(0x00FE, 155, 30)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2D59)

    Sleep(100)

    @scena.Lambda('lambda_2D6C')
    def lambda_2D6C():
        ChrSetDirection(0x00FE, 155, 32)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2D6C)

    Sleep(100)

    PlayEffect(0x01, 0x02, 0x000E, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlaySE(204, 0x00, 0x64)

    @scena.Lambda('lambda_2DB9')
    def lambda_2DB9():
        ChrMoveTo(0x00FE, -68840, 7300, 9400, 3500, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2DB9)

    Sleep(100)

    @scena.Lambda('lambda_2DD9')
    def lambda_2DD9():
        ChrSetDirection(0x00FE, 155, 30)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2DD9)

    Sleep(100)

    @scena.Lambda('lambda_2DEC')
    def lambda_2DEC():
        ChrSetDirection(0x00FE, 155, 28)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2DEC)

    Sleep(100)

    Sleep(100)

    @scena.Lambda('lambda_2E04')
    def lambda_2E04():
        ChrMoveTo(0x00FE, -68840, 3300, 9400, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2E04)

    Sleep(300)

    @scena.Lambda('lambda_2E24')
    def lambda_2E24():
        ChrSetDirection(0x00FE, 155, 25)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2E24)

    Sleep(100)

    @scena.Lambda('lambda_2E37')
    def lambda_2E37():
        ChrSetDirection(0x00FE, 155, 22)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2E37)

    Sleep(100)

    @scena.Lambda('lambda_2E4A')
    def lambda_2E4A():
        ChrSetDirection(0x00FE, 155, 20)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2E4A)

    @scena.Lambda('lambda_2E58')
    def lambda_2E58():
        ChrMoveTo(0x00FE, -68840, 300, 9400, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2E58)

    Sleep(500)

    Sleep(300)

    @scena.Lambda('lambda_2E7D')
    def lambda_2E7D():
        ChrSetDirection(0x00FE, 155, 18)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2E7D)

    Sleep(100)

    @scena.Lambda('lambda_2E90')
    def lambda_2E90():
        ChrSetDirection(0x00FE, 155, 16)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2E90)

    Sleep(100)

    @scena.Lambda('lambda_2EA3')
    def lambda_2EA3():
        ChrSetDirection(0x00FE, 155, 15)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2EA3)

    Sleep(100)

    @scena.Lambda('lambda_2EB6')
    def lambda_2EB6():
        ChrSetDirection(0x00FE, 155, 12)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2EB6)

    Sleep(1000)

    @scena.Lambda('lambda_2EC9')
    def lambda_2EC9():
        ChrMoveTo(0x00FE, -68840, 300, 9400, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2EC9)

    Sleep(2000)

    StopEffect(0x02, 0x02)
    WaitForThreadExit(0x00FE, 0x0002)
    PlaySE(200, 0x00, 0x64)
    OP_7C(0, 200, 3000, 100)

    Return()

# id: 0x0006 offset: 0x2F02
@scena.Code('func_06_2F02')
def func_06_2F02():
    ChrSetPos(0x00FE, -37060, 300, -13200, 291)

    @scena.Lambda('lambda_2F19')
    def lambda_2F19():
        ChrWalkTo(0x00FE, -68840, 300, 9400, 6200, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2F19)

    Sleep(3000)

    @scena.Lambda('lambda_2F39')
    def lambda_2F39():
        ChrMoveTo(0x00FE, -68840, 300, 9400, 5500, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2F39)

    Sleep(500)

    @scena.Lambda('lambda_2F59')
    def lambda_2F59():
        ChrMoveTo(0x00FE, -68840, 300, 9400, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2F59)

    @scena.Lambda('lambda_2F74')
    def lambda_2F74():
        ChrSetDirection(0x00FE, 155, 6)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2F74)

    Sleep(100)

    @scena.Lambda('lambda_2F87')
    def lambda_2F87():
        ChrSetDirection(0x00FE, 155, 8)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2F87)

    Sleep(100)

    @scena.Lambda('lambda_2F9A')
    def lambda_2F9A():
        ChrSetDirection(0x00FE, 155, 10)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2F9A)

    Sleep(100)

    @scena.Lambda('lambda_2FAD')
    def lambda_2FAD():
        ChrSetDirection(0x00FE, 155, 12)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2FAD)

    Sleep(100)

    @scena.Lambda('lambda_2FC0')
    def lambda_2FC0():
        ChrSetDirection(0x00FE, 155, 14)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2FC0)

    Sleep(100)

    @scena.Lambda('lambda_2FD3')
    def lambda_2FD3():
        ChrSetDirection(0x00FE, 155, 16)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2FD3)

    Sleep(100)

    @scena.Lambda('lambda_2FE6')
    def lambda_2FE6():
        ChrSetDirection(0x00FE, 155, 18)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2FE6)

    Sleep(100)

    @scena.Lambda('lambda_2FF9')
    def lambda_2FF9():
        ChrSetDirection(0x00FE, 155, 20)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2FF9)

    Sleep(100)

    @scena.Lambda('lambda_300C')
    def lambda_300C():
        ChrSetDirection(0x00FE, 155, 22)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_300C)

    Sleep(100)

    @scena.Lambda('lambda_301F')
    def lambda_301F():
        ChrSetDirection(0x00FE, 155, 25)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_301F)

    @scena.Lambda('lambda_302D')
    def lambda_302D():
        ChrMoveTo(0x00FE, -68840, 300, 9400, 4500, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_302D)

    Sleep(500)

    @scena.Lambda('lambda_304D')
    def lambda_304D():
        ChrMoveTo(0x00FE, -68840, 300, 9400, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_304D)

    Sleep(100)

    @scena.Lambda('lambda_306D')
    def lambda_306D():
        ChrSetDirection(0x00FE, 155, 28)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_306D)

    Sleep(100)

    @scena.Lambda('lambda_3080')
    def lambda_3080():
        ChrSetDirection(0x00FE, 155, 30)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_3080)

    Sleep(100)

    @scena.Lambda('lambda_3093')
    def lambda_3093():
        ChrSetDirection(0x00FE, 155, 32)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_3093)

    Sleep(100)

    @scena.Lambda('lambda_30A6')
    def lambda_30A6():
        ChrMoveTo(0x00FE, -68840, 300, 9400, 3500, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_30A6)

    Sleep(100)

    @scena.Lambda('lambda_30C6')
    def lambda_30C6():
        ChrSetDirection(0x00FE, 155, 30)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_30C6)

    Sleep(100)

    @scena.Lambda('lambda_30D9')
    def lambda_30D9():
        ChrSetDirection(0x00FE, 155, 28)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_30D9)

    Sleep(100)

    Sleep(100)

    @scena.Lambda('lambda_30F1')
    def lambda_30F1():
        ChrMoveTo(0x00FE, -68840, 300, 9400, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_30F1)

    Sleep(300)

    @scena.Lambda('lambda_3111')
    def lambda_3111():
        ChrSetDirection(0x00FE, 155, 25)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_3111)

    Sleep(100)

    @scena.Lambda('lambda_3124')
    def lambda_3124():
        ChrSetDirection(0x00FE, 155, 22)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_3124)

    Sleep(100)

    @scena.Lambda('lambda_3137')
    def lambda_3137():
        ChrSetDirection(0x00FE, 155, 20)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_3137)

    @scena.Lambda('lambda_3145')
    def lambda_3145():
        ChrMoveTo(0x00FE, -68840, 300, 9400, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3145)

    Sleep(500)

    Sleep(300)

    @scena.Lambda('lambda_316A')
    def lambda_316A():
        ChrSetDirection(0x00FE, 155, 18)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_316A)

    Sleep(100)

    @scena.Lambda('lambda_317D')
    def lambda_317D():
        ChrSetDirection(0x00FE, 155, 16)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_317D)

    Sleep(100)

    @scena.Lambda('lambda_3190')
    def lambda_3190():
        ChrSetDirection(0x00FE, 155, 15)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_3190)

    Sleep(100)

    @scena.Lambda('lambda_31A3')
    def lambda_31A3():
        ChrSetDirection(0x00FE, 155, 12)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_31A3)

    Sleep(1000)

    @scena.Lambda('lambda_31B6')
    def lambda_31B6():
        ChrMoveTo(0x00FE, -68840, 300, 9400, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_31B6)

    Return()

# id: 0x0007 offset: 0x31CC
@scena.Code('func_07_31CC')
def func_07_31CC():
    OP_99(0x00FE, 0x03, 0x00, 1000)
    ChrSetChipByIndex(0x00FE, 3)
    ChrTurnDirection(0x00FE, 0x000D, 200)

    @scena.Lambda('lambda_31E7')
    def lambda_31E7():
        ChrTurnDirection(0x00FE, 0x000D, 0)
        Yield()

        Jump('lambda_31E7')

    DispatchAsync2(0x00FE, 0x0002, lambda_31E7)

    Return()

# id: 0x0008 offset: 0x31F3
@scena.Code('func_08_31F3')
def func_08_31F3():
    LoadEffect(0x01, 'map\\\\mp021_00.eff')
    PlayEffect(0x01, 0x02, 0x000E, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlaySE(204, 0x00, 0x64)
    OP_6F(0x0002, 160)
    OP_70(0x0002, 240)

    @scena.Lambda('lambda_3255')
    def lambda_3255():
        ChrMoveTo(0x00FE, -68840, 10000, 9400, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3255)

    @scena.Lambda('lambda_3270')
    def lambda_3270():
        ChrSetDirection(0x00FE, 243, 12)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_3270)

    Sleep(100)

    @scena.Lambda('lambda_3283')
    def lambda_3283():
        ChrSetDirection(0x00FE, 243, 15)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_3283)

    Sleep(100)

    @scena.Lambda('lambda_3296')
    def lambda_3296():
        ChrSetDirection(0x00FE, 243, 17)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_3296)

    Sleep(500)

    Sleep(300)

    @scena.Lambda('lambda_32AE')
    def lambda_32AE():
        ChrSetDirection(0x00FE, 243, 15)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_32AE)

    Sleep(100)

    @scena.Lambda('lambda_32C1')
    def lambda_32C1():
        ChrSetDirection(0x00FE, 243, 12)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_32C1)

    Sleep(100)

    Sleep(1000)

    @scena.Lambda('lambda_32D9')
    def lambda_32D9():
        ChrMoveTo(0x00FE, -89950, 25000, -19340, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_32D9)

    Sleep(500)

    @scena.Lambda('lambda_32F9')
    def lambda_32F9():
        ChrMoveTo(0x00FE, -89950, 25000, -19340, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_32F9)

    Sleep(500)

    @scena.Lambda('lambda_3319')
    def lambda_3319():
        ChrMoveTo(0x00FE, -89950, 25000, -19340, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3319)

    Sleep(500)

    @scena.Lambda('lambda_3339')
    def lambda_3339():
        ChrMoveTo(0x00FE, -89950, 25000, -19340, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3339)

    Sleep(500)

    @scena.Lambda('lambda_3359')
    def lambda_3359():
        ChrMoveTo(0x00FE, -89950, 25000, -19340, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3359)

    Sleep(500)

    @scena.Lambda('lambda_3379')
    def lambda_3379():
        ChrMoveTo(0x00FE, -89950, 25000, -19340, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3379)

    Sleep(500)

    @scena.Lambda('lambda_3399')
    def lambda_3399():
        ChrMoveTo(0x00FE, -89950, 25000, -19340, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3399)

    Sleep(500)

    @scena.Lambda('lambda_33B9')
    def lambda_33B9():
        ChrMoveTo(0x00FE, -89950, 25000, -19340, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_33B9)

    Sleep(500)

    @scena.Lambda('lambda_33D9')
    def lambda_33D9():
        ChrMoveTo(0x00FE, -89950, 25000, -19340, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_33D9)

    Sleep(500)

    Return()

# id: 0x0009 offset: 0x33F4
@scena.Code('func_09_33F4')
def func_09_33F4():
    @scena.Lambda('lambda_33FA')
    def lambda_33FA():
        ChrMoveTo(0x00FE, -68840, 300, 9400, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_33FA)

    @scena.Lambda('lambda_3415')
    def lambda_3415():
        ChrSetDirection(0x00FE, 243, 12)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_3415)

    Sleep(100)

    @scena.Lambda('lambda_3428')
    def lambda_3428():
        ChrSetDirection(0x00FE, 243, 15)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_3428)

    Sleep(100)

    @scena.Lambda('lambda_343B')
    def lambda_343B():
        ChrSetDirection(0x00FE, 243, 17)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_343B)

    Sleep(500)

    Sleep(300)

    @scena.Lambda('lambda_3453')
    def lambda_3453():
        ChrSetDirection(0x00FE, 243, 15)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_3453)

    Sleep(100)

    @scena.Lambda('lambda_3466')
    def lambda_3466():
        ChrSetDirection(0x00FE, 243, 12)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_3466)

    Sleep(100)

    Sleep(2000)

    @scena.Lambda('lambda_347E')
    def lambda_347E():
        ChrMoveTo(0x00FE, -89950, 300, -19340, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_347E)

    Sleep(500)

    @scena.Lambda('lambda_349E')
    def lambda_349E():
        ChrMoveTo(0x00FE, -89950, 300, -19340, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_349E)

    Sleep(500)

    @scena.Lambda('lambda_34BE')
    def lambda_34BE():
        ChrMoveTo(0x00FE, -89950, 300, -19340, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_34BE)

    Sleep(500)

    @scena.Lambda('lambda_34DE')
    def lambda_34DE():
        ChrMoveTo(0x00FE, -89950, 300, -19340, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_34DE)

    Sleep(500)

    @scena.Lambda('lambda_34FE')
    def lambda_34FE():
        ChrMoveTo(0x00FE, -89950, 300, -19340, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_34FE)

    Sleep(500)

    @scena.Lambda('lambda_351E')
    def lambda_351E():
        ChrMoveTo(0x00FE, -89950, 300, -19340, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_351E)

    Sleep(500)

    @scena.Lambda('lambda_353E')
    def lambda_353E():
        ChrMoveTo(0x00FE, -89950, 300, -19340, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_353E)

    Sleep(500)

    @scena.Lambda('lambda_355E')
    def lambda_355E():
        ChrMoveTo(0x00FE, -89950, 300, -19340, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_355E)

    Sleep(500)

    @scena.Lambda('lambda_357E')
    def lambda_357E():
        ChrMoveTo(0x00FE, -89950, 300, -19340, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_357E)

    Return()

# id: 0x000A offset: 0x3594
@scena.Code('func_0A_3594')
def func_0A_3594():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0050, 6, 0x286)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3655',
    )

    If(
        (
            (Expr.Eval, "AddItem(0x0386, 1)"),
            Expr.Return,
        ),
        'loc_3603',
    )

    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '熊刺草',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_64(0x00, 0x0001)
    SetScenaFlags(ScenaFlag(0x0050, 6, 0x286))

    Jump('loc_3655')

    def _loc_3603(): pass

    label('loc_3603')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '熊刺草',
            (TxtCtl.SetColor, 0x0),
            '发现了，\n',
            (TxtCtl.SetColor, 0x0),
            '不过现有的数量太多，不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    def _loc_3655(): pass

    label('loc_3655')

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x000B offset: 0x365E
@scena.Code('func_0B_365E')
def func_0B_365E():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0052, 3, 0x293)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_374E',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0004, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x00F7, 1)"),
            Expr.Return,
        ),
        'loc_36D4',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '兽皮制服',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0052, 3, 0x293))

    Jump('loc_374B')

    def _loc_36D4(): pass

    label('loc_36D4')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '兽皮制服',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '兽皮制服',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0004, 60)
    OP_70(0x0004, 0)

    def _loc_374B(): pass

    label('loc_374B')

    Jump('loc_3786')

    def _loc_374E(): pass

    label('loc_374E')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱里什么东西都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    WaitEffect(0x0F, 0x02)
    def _loc_3786(): pass

    label('loc_3786')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C0302_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C0302   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '乔丝特'),
    TXT(0x02, '雷古'),
    TXT(0x03, '蒂诺'),
    TXT(0x04, '莱尔'),
    TXT(0x05, '吉尔'),
    TXT(0x06, '空贼艇'),
    TXT(0x07, '空贼艇（影）'),
    TXT(0x08, '目标用摄像机'),
    TXT(0x09, ''),
]

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

# id: 0xFFFF offset: 0x35CC
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
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

# id: 0x10001 offset: 0xA8
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

# id: 0x10002 offset: 0x172
@scena.NpcData('NpcData')
def NpcData():
    return (
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
            dword_10            = 16,
            chipIndex           = 16,
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
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0080,
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
            npcIndex            = 0x0080,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
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

# id: 0x10003 offset: 0x272
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
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

# id: 0x10004 offset: 0x2E2
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

# id: 0x10005 offset: 0x302
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
@scena.Code('PreInit')
def PreInit():
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
@scena.Code('Init')
def Init():
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
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 6, 0x266)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 4, 0x264)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2960',
    )

    ClearMapFlags(0x00000001)
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
    SetChrPos(0x0008, -60860, -320, 5360, 135)
    SetChrPos(0x0009, -60550, -150, 2920, 341)
    SetChrPos(0x000A, -59230, -300, 3520, 317)
    SetChrPos(0x000B, -58760, -350, 5070, 270)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0008, 0x0008)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x0009, 0x0008)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000A, 0x0008)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000B, 0x0008)
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
    SetChrPos(0x0101, -57980, 130, -9190, 356)
    SetChrPos(0x0102, -56650, 110, -9280, 356)
    SetChrPos(0x0103, -57400, -130, -10020, 356)
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

    @scena.Lambda('lambda_07DB')
    def lambda_07DB():
        CameraMove(-58480, 30, -5380, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_07DB)

    @scena.Lambda('lambda_07F3')
    def lambda_07F3():
        OP_6C(0, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_07F3)

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
        'loc_B7C',
    )

    SetChrChipByIndex(0x0101, 6)

    ChrTalk(
        0x0101,
        (
            '#0010011238V#005F（这叫我怎么冷～静！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_092C')
    def lambda_092C():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_092C)

    @scena.Lambda('lambda_093A')
    def lambda_093A():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_093A)

    ChrWalkTo(0x0101, -59020, 20, -9230, 6000, 0x00)

    @scena.Lambda('lambda_095C')
    def lambda_095C():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_095C')

    DispatchAsync2(0x0102, 0x0001, lambda_095C)

    @scena.Lambda('lambda_096D')
    def lambda_096D():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_096D')

    DispatchAsync2(0x0103, 0x0001, lambda_096D)

    ChrWalkTo(0x0101, -60410, 0, -8140, 6000, 0x00)

    @scena.Lambda('lambda_0992')
    def lambda_0992():
        ChrWalkTo(0x00FE, -60620, 30, -2490, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0992)

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
    SetChrChipByIndex(0x0102, 8)
    SetChrChipByIndex(0x0103, 10)

    @scena.Lambda('lambda_0A2F')
    def lambda_0A2F():
        OP_6C(45000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0A2F)

    @scena.Lambda('lambda_0A3F')
    def lambda_0A3F():
        CameraMove(-60120, -80, 1150, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0A3F)

    @scena.Lambda('lambda_0A57')
    def lambda_0A57():
        ChrWalkTo(0x00FE, -60670, 20, -8860, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0A57)

    Sleep(600)

    @scena.Lambda('lambda_0A77')
    def lambda_0A77():
        ChrWalkTo(0x00FE, -60670, 20, -8860, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_0A77)

    WaitForThreadExit(0x0102, 0x0001)

    @scena.Lambda('lambda_0A97')
    def lambda_0A97():
        ChrWalkTo(0x00FE, -61520, -140, -3820, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0A97)

    WaitForThreadExit(0x0103, 0x0001)

    @scena.Lambda('lambda_0AB7')
    def lambda_0AB7():
        ChrWalkTo(0x00FE, -59700, 10, -3820, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_0AB7)

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

    @scena.Lambda('lambda_0B3D')
    def lambda_0B3D():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0B3D)

    @scena.Lambda('lambda_0B4B')
    def lambda_0B4B():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0B4B)

    @scena.Lambda('lambda_0B59')
    def lambda_0B59():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0B59)

    @scena.Lambda('lambda_0B67')
    def lambda_0B67():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0B67)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)

    Jump('loc_F9B')

    def _loc_B7C(): pass

    label('loc_B7C')

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
    SetChrChipByIndex(0x0101, 6)
    SetChrChipByIndex(0x0102, 8)
    SetChrChipByIndex(0x0103, 10)
    SetChrPos(0x0101, -60670, 20, -8860, 270)
    SetChrPos(0x0102, -60670, 20, -8860, 270)
    SetChrPos(0x0103, -60670, 20, -8860, 270)

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

    @scena.Lambda('lambda_0EED')
    def lambda_0EED():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0EED)

    @scena.Lambda('lambda_0EFB')
    def lambda_0EFB():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0EFB)

    @scena.Lambda('lambda_0F09')
    def lambda_0F09():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0F09)

    @scena.Lambda('lambda_0F17')
    def lambda_0F17():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0F17)

    @scena.Lambda('lambda_0F25')
    def lambda_0F25():
        ChrWalkTo(0x00FE, -60610, 30, -2480, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0F25)

    Sleep(300)

    @scena.Lambda('lambda_0F45')
    def lambda_0F45():
        ChrWalkTo(0x00FE, -61520, -140, -3820, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0F45)

    Sleep(300)

    @scena.Lambda('lambda_0F65')
    def lambda_0F65():
        ChrWalkTo(0x00FE, -59700, 10, -3820, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_0F65)

    @scena.Lambda('lambda_0F80')
    def lambda_0F80():
        OP_6C(45000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0F80)

    CameraMove(-60120, -80, 1150, 1500)

    def _loc_F9B(): pass

    label('loc_F9B')

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
    SetChrChipByIndex(0x0009, 3)
    SetChrChipByIndex(0x000B, 3)
    SetChrChipByIndex(0x000A, 3)

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

    @scena.Lambda('lambda_133E')
    def lambda_133E():
        CameraSetDistance(3000, 1000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_133E)

    @scena.Lambda('lambda_134E')
    def lambda_134E():
        CameraMove(-60120, -80, 3200, 1000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_134E)

    Sleep(500)

    StopEffect(0x00, 0x00)
    PlaySE(203, 0x00, 0x64)
    SetChrDirection(0x0008, 32, 800)
    SetChrChipByIndex(0x0008, 0)
    SetChrDirection(0x0008, 330, 800)
    SetChrDirection(0x0008, 180, 800)
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

    @scena.Lambda('lambda_13F9')
    def lambda_13F9():
        CameraMove(-60120, -80, 1150, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_13F9)

    SetChrChipByIndex(0x000A, 4)

    @scena.Lambda('lambda_1416')
    def lambda_1416():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1416)

    SetChrChipByIndex(0x0009, 4)

    @scena.Lambda('lambda_1430')
    def lambda_1430():
        OP_92(0x00FE, 0x0102, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1430)

    SetChrChipByIndex(0x000B, 4)

    @scena.Lambda('lambda_144A')
    def lambda_144A():
        OP_92(0x00FE, 0x0103, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_144A)

    SetChrChipByIndex(0x0008, 1)

    @scena.Lambda('lambda_1464')
    def lambda_1464():
        OP_92(0x00FE, 0x0101, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1464)

    Sleep(400)

    Battle(0x00000385, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_1491'),
        (-1, 'loc_1496'),
    )

    def _loc_1491(): pass

    label('loc_1491')

    OP_B4(0x00)

    Jump('loc_1496')

    def _loc_1496(): pass

    label('loc_1496')

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
    SetChrPos(0x0103, -59720, -110, 320, 26)
    SetChrPos(0x0102, -57190, -230, -570, 20)
    SetChrPos(0x0101, -57720, -260, 480, 4)

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

    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0103, 65535)

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

    SetChrChipByIndex(0x0008, 2)
    SetChrChipByIndex(0x0009, 5)
    SetChrChipByIndex(0x000B, 5)
    SetChrChipByIndex(0x000A, 5)
    SetChrPos(0x0008, -55850, -280, 3840, 206)
    SetChrPos(0x0009, -56410, -160, 5250, 213)
    SetChrPos(0x000A, -54320, -160, 4210, 216)
    SetChrPos(0x000B, -54160, -50, 5560, 270)
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
    SetChrName('')
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

    @scena.Lambda('lambda_17B5')
    def lambda_17B5():
        ChrMoveTo(0x00FE, -57150, -280, 730, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_17B5)

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
    SetChrChipByIndex(0x0103, 10)

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
    SetChrChipByIndex(0x0103, 12)
    PlaySE(502, 0x00, 0x64)
    OP_99(0x0103, 0x00, 0x04, 2000)

    @scena.Lambda('lambda_1955')
    def lambda_1955():
        OP_99(0x0103, 0x07, 0x09, 2000)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_1955)

    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrJumpTo(0x0008, -55670, -220, 4250, 500, 5000)
    SetChrChipByIndex(0x0008, 13)

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

    SetChrChipByIndex(0x0103, 65535)
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

    SetChrChipByIndex(0x0103, 10)

    @scena.Lambda('lambda_1A71')
    def lambda_1A71():
        OP_99(0x00FE, 0x00, 0x07, 1000)
        Yield()

        Jump('lambda_1A71')

    DispatchAsync2(0x0103, 0x0001, lambda_1A71)

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
    SetChrPos(0x000D, -37060, 300, -13200, 291)
    ChrTurnDirection(0x0102, 0x000D, 800)
    SetChrChipByIndex(0x0102, 8)

    @scena.Lambda('lambda_1BDC')
    def lambda_1BDC():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1BDC)

    ChrTalk(
        0x0102,
        (
            '#0020011296V#016F雪拉姐姐，危险！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1C0C')
    def lambda_1C0C():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1C0C)

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
    SetChrChipByIndex(0x0101, 6)

    @scena.Lambda('lambda_1E66')
    def lambda_1E66():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1E66)

    @scena.Lambda('lambda_1E74')
    def lambda_1E74():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1E74)

    @scena.Lambda('lambda_1E82')
    def lambda_1E82():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_1E82)

    @scena.Lambda('lambda_1E90')
    def lambda_1E90():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1E90)

    OP_72(0x0002, 0x0004)
    OP_72(0x0003, 0x0004)
    SetChrFlags(0x000D, 0x0004)
    SetChrFlags(0x000D, 0x0040)
    SetChrFlags(0x000E, 0x0004)
    SetChrFlags(0x000E, 0x0040)
    OP_A1(0x000D, 0x0002)
    OP_A1(0x000E, 0x0003)
    CreateThread(0x000D, 0x01, 0x00, 0x0005)
    CreateThread(0x000E, 0x01, 0x00, 0x0006)
    OP_B0(0x0002, 0x1E)

    @scena.Lambda('lambda_1ED8')
    def lambda_1ED8():
        OP_6E(511, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1ED8)

    OP_24(0x0079, 0x5A)
    Sleep(500)

    OP_24(0x0079, 0x64)
    Sleep(2500)

    @scena.Lambda('lambda_1EFA')
    def lambda_1EFA():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_1EFA')

    DispatchAsync2(0x0008, 0x0001, lambda_1EFA)

    @scena.Lambda('lambda_1F0B')
    def lambda_1F0B():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_1F0B')

    DispatchAsync2(0x0101, 0x0001, lambda_1F0B)

    @scena.Lambda('lambda_1F1C')
    def lambda_1F1C():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_1F1C')

    DispatchAsync2(0x0103, 0x0001, lambda_1F1C)

    @scena.Lambda('lambda_1F2D')
    def lambda_1F2D():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_1F2D')

    DispatchAsync2(0x0102, 0x0001, lambda_1F2D)

    @scena.Lambda('lambda_1F3E')
    def lambda_1F3E():
        CameraMove(-61600, 3050, 5140, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1F3E)

    @scena.Lambda('lambda_1F56')
    def lambda_1F56():
        OP_6C(33000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1F56)

    Sleep(5000)

    CreateThread(0x0009, 0x01, 0x00, 0x0007)
    CreateThread(0x000B, 0x01, 0x00, 0x0007)
    CreateThread(0x000A, 0x01, 0x00, 0x0007)
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

    @scena.Lambda('lambda_1FC7')
    def lambda_1FC7():
        ChrWalkTo(0x00FE, -60900, -320, 4560, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1FC7)

    Sleep(200)

    SetChrChipByIndex(0x0009, 4)

    @scena.Lambda('lambda_1FEC')
    def lambda_1FEC():
        ChrWalkTo(0x00FE, -59470, -370, 5530, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1FEC)

    Sleep(200)

    SetChrChipByIndex(0x000B, 4)

    @scena.Lambda('lambda_2011')
    def lambda_2011():
        ChrWalkTo(0x00FE, -59800, -320, 4160, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_2011)

    Sleep(100)

    SetChrChipByIndex(0x000A, 4)

    @scena.Lambda('lambda_2036')
    def lambda_2036():
        ChrWalkTo(0x00FE, -61020, -180, 3130, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_2036)

    WaitForThreadExit(0x0008, 0x0001)
    SetChrPos(0x000C, -67370, 8500, 6060, 123)
    ChrTurnDirection(0x0008, 0x000C, 0)
    WaitForThreadExit(0x0009, 0x0001)
    SetChrChipByIndex(0x0009, 3)
    WaitForThreadExit(0x000B, 0x0001)
    SetChrChipByIndex(0x000B, 3)
    WaitForThreadExit(0x000A, 0x0001)
    SetChrChipByIndex(0x000A, 3)
    WaitForThreadExit(0x0101, 0x0002)

    @scena.Lambda('lambda_2091')
    def lambda_2091():
        CameraMove(-62640, 4570, 5610, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2091)

    @scena.Lambda('lambda_20A9')
    def lambda_20A9():
        OP_6E(363, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_20A9)

    @scena.Lambda('lambda_20B9')
    def lambda_20B9():
        OP_67(0, 10510, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_20B9)

    Sleep(1000)

    PlaySE(106, 0x00, 0x64)
    OP_6F(0x0002, 60)
    OP_70(0x0002, 95)
    OP_73(0x0002)
    ClearChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000C, 0x0004)
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
    SetChrFlags(0x000C, 0x0080)
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
    SetChrFlags(0x0008, 0x0004)
    SetChrFlags(0x0009, 0x0004)
    SetChrFlags(0x000B, 0x0004)
    SetChrFlags(0x000A, 0x0004)

    @scena.Lambda('lambda_228D')
    def lambda_228D():
        ChrWalkTo(0x00FE, -65269, -200, 5050, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_228D)

    Sleep(200)

    @scena.Lambda('lambda_22AD')
    def lambda_22AD():
        CameraMove(-61640, -300, 5890, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_22AD)

    @scena.Lambda('lambda_22C5')
    def lambda_22C5():
        OP_67(0, 9430, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_22C5)

    @scena.Lambda('lambda_22DD')
    def lambda_22DD():
        OP_6C(9000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_22DD)

    SetChrChipByIndex(0x0009, 4)

    @scena.Lambda('lambda_22F2')
    def lambda_22F2():
        ChrWalkTo(0x00FE, -83020, -330, 26640, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_22F2)

    Sleep(200)

    SetChrChipByIndex(0x000B, 4)

    @scena.Lambda('lambda_2317')
    def lambda_2317():
        ChrWalkTo(0x00FE, -83020, -330, 26640, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_2317)

    Sleep(100)

    SetChrChipByIndex(0x000A, 4)

    @scena.Lambda('lambda_233C')
    def lambda_233C():
        ChrWalkTo(0x00FE, -83020, -330, 26640, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_233C)

    @scena.Lambda('lambda_2357')
    def lambda_2357():
        ChrWalkTo(0x00FE, -58890, -280, 2009, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2357)

    @scena.Lambda('lambda_2372')
    def lambda_2372():
        ChrWalkTo(0x00FE, -60400, 20, -1210, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_2372)

    WaitForThreadExit(0x0008, 0x0001)
    ClearChrFlags(0x0008, 0x0004)
    SetChrBattleFlags(0x0008, 0x0020)
    ChrJumpTo(0x0008, -66120, 550, 4700, 1000, 8000)
    SetChrDirection(0x0008, 160, 400)
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

    @scena.Lambda('lambda_243D')
    def lambda_243D():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_243D')

    DispatchAsync2(0x0101, 0x0000, lambda_243D)

    @scena.Lambda('lambda_244E')
    def lambda_244E():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_244E')

    DispatchAsync2(0x0103, 0x0000, lambda_244E)

    @scena.Lambda('lambda_245F')
    def lambda_245F():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_245F')

    DispatchAsync2(0x0102, 0x0000, lambda_245F)

    PlaySE(205, 0x00, 0x64)
    CreateThread(0x000D, 0x01, 0x00, 0x0008)
    CreateThread(0x000E, 0x01, 0x00, 0x0009)
    CreateThread(0x0008, 0x03, 0x00, 0x0004)

    @scena.Lambda('lambda_248A')
    def lambda_248A():
        CameraMove(-68070, 1230, 7050, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_248A)

    @scena.Lambda('lambda_24A2')
    def lambda_24A2():
        OP_6C(69000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_24A2)

    @scena.Lambda('lambda_24B2')
    def lambda_24B2():
        CameraSetDistance(4000, 6000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_24B2)

    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    Sleep(3000)

    @scena.Lambda('lambda_24D6')
    def lambda_24D6():
        CameraMove(-60410, -60, 750, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_24D6)

    @scena.Lambda('lambda_24EE')
    def lambda_24EE():
        OP_67(0, 9000, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_24EE)

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
    SetChrFlags(0x0008, 0x0080)
    SetChrPos(0x0101, -60700, -40, 950, 225)
    SetChrPos(0x0102, -60790, -80, 2280, 225)
    SetChrPos(0x0103, -59390, -210, 1740, 225)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0103, 65535)
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
    SetChrDirection(0x0102, 135, 400)

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
    SetChrDirection(0x0103, 270, 400)

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

    def _loc_2960(): pass

    label('loc_2960')

    Return()

# id: 0x0003 offset: 0x2961
@scena.Code('func_03_2961')
def func_03_2961():
    OP_24(0x0079, 0x46)
    Sleep(500)

    OP_24(0x0079, 0x50)
    Sleep(500)

    OP_24(0x0079, 0x5A)
    Sleep(500)

    OP_24(0x0079, 0x64)

    Return()

# id: 0x0004 offset: 0x2981
@scena.Code('func_04_2981')
def func_04_2981():
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

# id: 0x0005 offset: 0x29E7
@scena.Code('func_05_29E7')
def func_05_29E7():
    SetChrPos(0x00FE, -37060, 17100, -13200, 291)
    LoadEffect(0x01, 'map\\\\mp021_00.eff')

    @scena.Lambda('lambda_2A12')
    def lambda_2A12():
        ChrWalkTo(0x00FE, -68840, 10300, 9400, 6200, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2A12)

    Sleep(3000)

    @scena.Lambda('lambda_2A32')
    def lambda_2A32():
        ChrMoveTo(0x00FE, -68840, 9300, 9400, 5500, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2A32)

    Sleep(500)

    @scena.Lambda('lambda_2A52')
    def lambda_2A52():
        ChrMoveTo(0x00FE, -68840, 9300, 9400, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2A52)

    @scena.Lambda('lambda_2A6D')
    def lambda_2A6D():
        SetChrDirection(0x00FE, 155, 6)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2A6D)

    Sleep(100)

    @scena.Lambda('lambda_2A80')
    def lambda_2A80():
        SetChrDirection(0x00FE, 155, 8)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2A80)

    Sleep(100)

    @scena.Lambda('lambda_2A93')
    def lambda_2A93():
        SetChrDirection(0x00FE, 155, 10)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2A93)

    Sleep(100)

    @scena.Lambda('lambda_2AA6')
    def lambda_2AA6():
        SetChrDirection(0x00FE, 155, 12)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2AA6)

    Sleep(100)

    @scena.Lambda('lambda_2AB9')
    def lambda_2AB9():
        SetChrDirection(0x00FE, 155, 14)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2AB9)

    Sleep(100)

    @scena.Lambda('lambda_2ACC')
    def lambda_2ACC():
        SetChrDirection(0x00FE, 155, 16)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2ACC)

    Sleep(100)

    @scena.Lambda('lambda_2ADF')
    def lambda_2ADF():
        SetChrDirection(0x00FE, 155, 18)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2ADF)

    Sleep(100)

    @scena.Lambda('lambda_2AF2')
    def lambda_2AF2():
        SetChrDirection(0x00FE, 155, 20)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2AF2)

    Sleep(100)

    @scena.Lambda('lambda_2B05')
    def lambda_2B05():
        SetChrDirection(0x00FE, 155, 22)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2B05)

    Sleep(100)

    @scena.Lambda('lambda_2B18')
    def lambda_2B18():
        SetChrDirection(0x00FE, 155, 25)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2B18)

    @scena.Lambda('lambda_2B26')
    def lambda_2B26():
        ChrMoveTo(0x00FE, -68840, 7300, 9400, 4500, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2B26)

    Sleep(500)

    @scena.Lambda('lambda_2B46')
    def lambda_2B46():
        ChrMoveTo(0x00FE, -68840, 7300, 9400, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2B46)

    Sleep(100)

    @scena.Lambda('lambda_2B66')
    def lambda_2B66():
        SetChrDirection(0x00FE, 155, 28)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2B66)

    Sleep(100)

    @scena.Lambda('lambda_2B79')
    def lambda_2B79():
        SetChrDirection(0x00FE, 155, 30)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2B79)

    Sleep(100)

    @scena.Lambda('lambda_2B8C')
    def lambda_2B8C():
        SetChrDirection(0x00FE, 155, 32)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2B8C)

    Sleep(100)

    PlayEffect(0x01, 0x02, 0x000E, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlaySE(204, 0x00, 0x64)

    @scena.Lambda('lambda_2BD9')
    def lambda_2BD9():
        ChrMoveTo(0x00FE, -68840, 7300, 9400, 3500, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2BD9)

    Sleep(100)

    @scena.Lambda('lambda_2BF9')
    def lambda_2BF9():
        SetChrDirection(0x00FE, 155, 30)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2BF9)

    Sleep(100)

    @scena.Lambda('lambda_2C0C')
    def lambda_2C0C():
        SetChrDirection(0x00FE, 155, 28)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2C0C)

    Sleep(100)

    Sleep(100)

    @scena.Lambda('lambda_2C24')
    def lambda_2C24():
        ChrMoveTo(0x00FE, -68840, 3300, 9400, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2C24)

    Sleep(300)

    @scena.Lambda('lambda_2C44')
    def lambda_2C44():
        SetChrDirection(0x00FE, 155, 25)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2C44)

    Sleep(100)

    @scena.Lambda('lambda_2C57')
    def lambda_2C57():
        SetChrDirection(0x00FE, 155, 22)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2C57)

    Sleep(100)

    @scena.Lambda('lambda_2C6A')
    def lambda_2C6A():
        SetChrDirection(0x00FE, 155, 20)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2C6A)

    @scena.Lambda('lambda_2C78')
    def lambda_2C78():
        ChrMoveTo(0x00FE, -68840, 300, 9400, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2C78)

    Sleep(500)

    Sleep(300)

    @scena.Lambda('lambda_2C9D')
    def lambda_2C9D():
        SetChrDirection(0x00FE, 155, 18)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2C9D)

    Sleep(100)

    @scena.Lambda('lambda_2CB0')
    def lambda_2CB0():
        SetChrDirection(0x00FE, 155, 16)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2CB0)

    Sleep(100)

    @scena.Lambda('lambda_2CC3')
    def lambda_2CC3():
        SetChrDirection(0x00FE, 155, 15)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2CC3)

    Sleep(100)

    @scena.Lambda('lambda_2CD6')
    def lambda_2CD6():
        SetChrDirection(0x00FE, 155, 12)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2CD6)

    Sleep(1000)

    @scena.Lambda('lambda_2CE9')
    def lambda_2CE9():
        ChrMoveTo(0x00FE, -68840, 300, 9400, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2CE9)

    Sleep(2000)

    StopEffect(0x02, 0x02)
    WaitForThreadExit(0x00FE, 0x0002)
    PlaySE(200, 0x00, 0x64)
    OP_7C(0, 200, 3000, 100)

    Return()

# id: 0x0006 offset: 0x2D22
@scena.Code('func_06_2D22')
def func_06_2D22():
    SetChrPos(0x00FE, -37060, 300, -13200, 291)

    @scena.Lambda('lambda_2D39')
    def lambda_2D39():
        ChrWalkTo(0x00FE, -68840, 300, 9400, 6200, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2D39)

    Sleep(3000)

    @scena.Lambda('lambda_2D59')
    def lambda_2D59():
        ChrMoveTo(0x00FE, -68840, 300, 9400, 5500, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2D59)

    Sleep(500)

    @scena.Lambda('lambda_2D79')
    def lambda_2D79():
        ChrMoveTo(0x00FE, -68840, 300, 9400, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2D79)

    @scena.Lambda('lambda_2D94')
    def lambda_2D94():
        SetChrDirection(0x00FE, 155, 6)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2D94)

    Sleep(100)

    @scena.Lambda('lambda_2DA7')
    def lambda_2DA7():
        SetChrDirection(0x00FE, 155, 8)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2DA7)

    Sleep(100)

    @scena.Lambda('lambda_2DBA')
    def lambda_2DBA():
        SetChrDirection(0x00FE, 155, 10)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2DBA)

    Sleep(100)

    @scena.Lambda('lambda_2DCD')
    def lambda_2DCD():
        SetChrDirection(0x00FE, 155, 12)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2DCD)

    Sleep(100)

    @scena.Lambda('lambda_2DE0')
    def lambda_2DE0():
        SetChrDirection(0x00FE, 155, 14)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2DE0)

    Sleep(100)

    @scena.Lambda('lambda_2DF3')
    def lambda_2DF3():
        SetChrDirection(0x00FE, 155, 16)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2DF3)

    Sleep(100)

    @scena.Lambda('lambda_2E06')
    def lambda_2E06():
        SetChrDirection(0x00FE, 155, 18)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2E06)

    Sleep(100)

    @scena.Lambda('lambda_2E19')
    def lambda_2E19():
        SetChrDirection(0x00FE, 155, 20)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2E19)

    Sleep(100)

    @scena.Lambda('lambda_2E2C')
    def lambda_2E2C():
        SetChrDirection(0x00FE, 155, 22)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2E2C)

    Sleep(100)

    @scena.Lambda('lambda_2E3F')
    def lambda_2E3F():
        SetChrDirection(0x00FE, 155, 25)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2E3F)

    @scena.Lambda('lambda_2E4D')
    def lambda_2E4D():
        ChrMoveTo(0x00FE, -68840, 300, 9400, 4500, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2E4D)

    Sleep(500)

    @scena.Lambda('lambda_2E6D')
    def lambda_2E6D():
        ChrMoveTo(0x00FE, -68840, 300, 9400, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2E6D)

    Sleep(100)

    @scena.Lambda('lambda_2E8D')
    def lambda_2E8D():
        SetChrDirection(0x00FE, 155, 28)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2E8D)

    Sleep(100)

    @scena.Lambda('lambda_2EA0')
    def lambda_2EA0():
        SetChrDirection(0x00FE, 155, 30)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2EA0)

    Sleep(100)

    @scena.Lambda('lambda_2EB3')
    def lambda_2EB3():
        SetChrDirection(0x00FE, 155, 32)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2EB3)

    Sleep(100)

    @scena.Lambda('lambda_2EC6')
    def lambda_2EC6():
        ChrMoveTo(0x00FE, -68840, 300, 9400, 3500, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2EC6)

    Sleep(100)

    @scena.Lambda('lambda_2EE6')
    def lambda_2EE6():
        SetChrDirection(0x00FE, 155, 30)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2EE6)

    Sleep(100)

    @scena.Lambda('lambda_2EF9')
    def lambda_2EF9():
        SetChrDirection(0x00FE, 155, 28)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2EF9)

    Sleep(100)

    Sleep(100)

    @scena.Lambda('lambda_2F11')
    def lambda_2F11():
        ChrMoveTo(0x00FE, -68840, 300, 9400, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2F11)

    Sleep(300)

    @scena.Lambda('lambda_2F31')
    def lambda_2F31():
        SetChrDirection(0x00FE, 155, 25)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2F31)

    Sleep(100)

    @scena.Lambda('lambda_2F44')
    def lambda_2F44():
        SetChrDirection(0x00FE, 155, 22)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2F44)

    Sleep(100)

    @scena.Lambda('lambda_2F57')
    def lambda_2F57():
        SetChrDirection(0x00FE, 155, 20)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2F57)

    @scena.Lambda('lambda_2F65')
    def lambda_2F65():
        ChrMoveTo(0x00FE, -68840, 300, 9400, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2F65)

    Sleep(500)

    Sleep(300)

    @scena.Lambda('lambda_2F8A')
    def lambda_2F8A():
        SetChrDirection(0x00FE, 155, 18)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2F8A)

    Sleep(100)

    @scena.Lambda('lambda_2F9D')
    def lambda_2F9D():
        SetChrDirection(0x00FE, 155, 16)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2F9D)

    Sleep(100)

    @scena.Lambda('lambda_2FB0')
    def lambda_2FB0():
        SetChrDirection(0x00FE, 155, 15)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2FB0)

    Sleep(100)

    @scena.Lambda('lambda_2FC3')
    def lambda_2FC3():
        SetChrDirection(0x00FE, 155, 12)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2FC3)

    Sleep(1000)

    @scena.Lambda('lambda_2FD6')
    def lambda_2FD6():
        ChrMoveTo(0x00FE, -68840, 300, 9400, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2FD6)

    Return()

# id: 0x0007 offset: 0x2FEC
@scena.Code('func_07_2FEC')
def func_07_2FEC():
    OP_99(0x00FE, 0x03, 0x00, 1000)
    SetChrChipByIndex(0x00FE, 3)
    ChrTurnDirection(0x00FE, 0x000D, 200)

    @scena.Lambda('lambda_3007')
    def lambda_3007():
        ChrTurnDirection(0x00FE, 0x000D, 0)
        Yield()

        Jump('lambda_3007')

    DispatchAsync2(0x00FE, 0x0002, lambda_3007)

    Return()

# id: 0x0008 offset: 0x3013
@scena.Code('func_08_3013')
def func_08_3013():
    LoadEffect(0x01, 'map\\\\mp021_00.eff')
    PlayEffect(0x01, 0x02, 0x000E, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlaySE(204, 0x00, 0x64)
    OP_6F(0x0002, 160)
    OP_70(0x0002, 240)

    @scena.Lambda('lambda_3075')
    def lambda_3075():
        ChrMoveTo(0x00FE, -68840, 10000, 9400, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3075)

    @scena.Lambda('lambda_3090')
    def lambda_3090():
        SetChrDirection(0x00FE, 243, 12)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_3090)

    Sleep(100)

    @scena.Lambda('lambda_30A3')
    def lambda_30A3():
        SetChrDirection(0x00FE, 243, 15)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_30A3)

    Sleep(100)

    @scena.Lambda('lambda_30B6')
    def lambda_30B6():
        SetChrDirection(0x00FE, 243, 17)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_30B6)

    Sleep(500)

    Sleep(300)

    @scena.Lambda('lambda_30CE')
    def lambda_30CE():
        SetChrDirection(0x00FE, 243, 15)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_30CE)

    Sleep(100)

    @scena.Lambda('lambda_30E1')
    def lambda_30E1():
        SetChrDirection(0x00FE, 243, 12)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_30E1)

    Sleep(100)

    Sleep(1000)

    @scena.Lambda('lambda_30F9')
    def lambda_30F9():
        ChrMoveTo(0x00FE, -89950, 25000, -19340, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_30F9)

    Sleep(500)

    @scena.Lambda('lambda_3119')
    def lambda_3119():
        ChrMoveTo(0x00FE, -89950, 25000, -19340, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3119)

    Sleep(500)

    @scena.Lambda('lambda_3139')
    def lambda_3139():
        ChrMoveTo(0x00FE, -89950, 25000, -19340, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3139)

    Sleep(500)

    @scena.Lambda('lambda_3159')
    def lambda_3159():
        ChrMoveTo(0x00FE, -89950, 25000, -19340, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3159)

    Sleep(500)

    @scena.Lambda('lambda_3179')
    def lambda_3179():
        ChrMoveTo(0x00FE, -89950, 25000, -19340, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3179)

    Sleep(500)

    @scena.Lambda('lambda_3199')
    def lambda_3199():
        ChrMoveTo(0x00FE, -89950, 25000, -19340, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3199)

    Sleep(500)

    @scena.Lambda('lambda_31B9')
    def lambda_31B9():
        ChrMoveTo(0x00FE, -89950, 25000, -19340, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_31B9)

    Sleep(500)

    @scena.Lambda('lambda_31D9')
    def lambda_31D9():
        ChrMoveTo(0x00FE, -89950, 25000, -19340, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_31D9)

    Sleep(500)

    @scena.Lambda('lambda_31F9')
    def lambda_31F9():
        ChrMoveTo(0x00FE, -89950, 25000, -19340, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_31F9)

    Sleep(500)

    Return()

# id: 0x0009 offset: 0x3214
@scena.Code('func_09_3214')
def func_09_3214():
    @scena.Lambda('lambda_321A')
    def lambda_321A():
        ChrMoveTo(0x00FE, -68840, 300, 9400, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_321A)

    @scena.Lambda('lambda_3235')
    def lambda_3235():
        SetChrDirection(0x00FE, 243, 12)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_3235)

    Sleep(100)

    @scena.Lambda('lambda_3248')
    def lambda_3248():
        SetChrDirection(0x00FE, 243, 15)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_3248)

    Sleep(100)

    @scena.Lambda('lambda_325B')
    def lambda_325B():
        SetChrDirection(0x00FE, 243, 17)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_325B)

    Sleep(500)

    Sleep(300)

    @scena.Lambda('lambda_3273')
    def lambda_3273():
        SetChrDirection(0x00FE, 243, 15)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_3273)

    Sleep(100)

    @scena.Lambda('lambda_3286')
    def lambda_3286():
        SetChrDirection(0x00FE, 243, 12)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_3286)

    Sleep(100)

    Sleep(2000)

    @scena.Lambda('lambda_329E')
    def lambda_329E():
        ChrMoveTo(0x00FE, -89950, 300, -19340, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_329E)

    Sleep(500)

    @scena.Lambda('lambda_32BE')
    def lambda_32BE():
        ChrMoveTo(0x00FE, -89950, 300, -19340, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_32BE)

    Sleep(500)

    @scena.Lambda('lambda_32DE')
    def lambda_32DE():
        ChrMoveTo(0x00FE, -89950, 300, -19340, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_32DE)

    Sleep(500)

    @scena.Lambda('lambda_32FE')
    def lambda_32FE():
        ChrMoveTo(0x00FE, -89950, 300, -19340, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_32FE)

    Sleep(500)

    @scena.Lambda('lambda_331E')
    def lambda_331E():
        ChrMoveTo(0x00FE, -89950, 300, -19340, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_331E)

    Sleep(500)

    @scena.Lambda('lambda_333E')
    def lambda_333E():
        ChrMoveTo(0x00FE, -89950, 300, -19340, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_333E)

    Sleep(500)

    @scena.Lambda('lambda_335E')
    def lambda_335E():
        ChrMoveTo(0x00FE, -89950, 300, -19340, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_335E)

    Sleep(500)

    @scena.Lambda('lambda_337E')
    def lambda_337E():
        ChrMoveTo(0x00FE, -89950, 300, -19340, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_337E)

    Sleep(500)

    @scena.Lambda('lambda_339E')
    def lambda_339E():
        ChrMoveTo(0x00FE, -89950, 300, -19340, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_339E)

    Return()

# id: 0x000A offset: 0x33B4
@scena.Code('func_0A_33B4')
def func_0A_33B4():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0050, 6, 0x286)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3475',
    )

    If(
        (
            (Expr.Eval, "AddItem(0x0386, 1)"),
            Expr.Return,
        ),
        'loc_3423',
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

    Jump('loc_3475')

    def _loc_3423(): pass

    label('loc_3423')

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

    def _loc_3475(): pass

    label('loc_3475')

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x000B offset: 0x347E
@scena.Code('func_0B_347E')
def func_0B_347E():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0052, 3, 0x293)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_356E',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0004, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x00F7, 1)"),
            Expr.Return,
        ),
        'loc_34F4',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

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

    Jump('loc_356B')

    def _loc_34F4(): pass

    label('loc_34F4')

    FadeOut(300, 0, 100)
    SetChrName('')

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

    def _loc_356B(): pass

    label('loc_356B')

    Jump('loc_35A6')

    def _loc_356E(): pass

    label('loc_356E')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    def _loc_35A6(): pass

    label('loc_35A6')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

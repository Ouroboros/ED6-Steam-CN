import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4250_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4250   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4250.x'
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
        ('ED6_DT07/CH02100._CH', 'ED6_DT07/CH02100P._CP'),
        ('ED6_DT07/CH02540._CH', 'ED6_DT07/CH02540P._CP'),
        ('ED6_DT07/CH02030._CH', 'ED6_DT07/CH02030P._CP'),
        ('ED6_DT07/CH02460._CH', 'ED6_DT07/CH02460P._CP'),
        ('ED6_DT07/CH02230._CH', 'ED6_DT07/CH02230P._CP'),
        ('ED6_DT07/CH02240._CH', 'ED6_DT07/CH02240P._CP'),
        ('ED6_DT07/CH01610._CH', 'ED6_DT07/CH01610P._CP'),
        ('ED6_DT07/CH00177._CH', 'ED6_DT07/CH00177P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
    ]

# id: 0x10001 offset: 0xF2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '凯诺娜上尉',
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
            name                = '茜亚',
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
            name                = '理查德上校',
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
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '特务兵',
            x                   = 21430,
            z                   = 750,
            y                   = -3970,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 2750,
            z                   = 0,
            y                   = -26300,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = -2980,
            z                   = 0,
            y                   = -26300,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 2750,
            z                   = 0,
            y                   = -26300,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = -2980,
            z                   = 0,
            y                   = -26300,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 9000,
            y                   = 29350,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
    )

# id: 0x10002 offset: 0x252
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x252
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 4010,
            y           = 10000,
            z           = 16219,
            range       = -4330,
            dword_10    = 0x00001F40,
            dword_14    = 0x00002D78,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000008,
        ),
        ScenaEventData(
            x           = 21060,
            y           = -1000,
            z           = -1860,
            range       = 19780,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFFE854,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000A,
        ),
        ScenaEventData(
            x           = 4290,
            y           = -1000,
            z           = -25590,
            range       = -4690,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFFA33A,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000B,
        ),
        ScenaEventData(
            x           = 0,
            y           = 8000,
            z           = 30350,
            range       = 3000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x0000000C,
        ),
    )

# id: 0x10004 offset: 0x2D2
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x2D2
@scena.Code('Init')
def Init():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_2E2'),
        (0x0000006C, 'loc_2F8'),
        (-1, 'loc_30B'),
    )

    def _loc_2E2(): pass

    label('loc_2E2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 0, 0x638)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2F5',
    )

    SetScenaFlags(ScenaFlag(0x00C7, 1, 0x639))
    Event(0, func_03_458)

    def _loc_2F5(): pass

    label('loc_2F5')

    Jump('loc_30B')

    def _loc_2F8(): pass

    label('loc_2F8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 1, 0x641)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_308',
    )

    Event(0, func_06_1AED)

    def _loc_308(): pass

    label('loc_308')

    Jump('loc_30B')

    def _loc_30B(): pass

    label('loc_30B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_335',
    )

    ChrSetChipByIndex(0x0000, 3)
    ChrSetChipByIndex(0x0001, 4)
    ChrSetChipByIndex(0x0138, 5)
    ChrSetFlags(0x0000, 0x1000)
    ChrSetFlags(0x0001, 0x1000)
    ChrSetFlags(0x0138, 0x1000)

    def _loc_335(): pass

    label('loc_335')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 0, 0x660)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_359',
    )

    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0010, 0x0080)

    def _loc_359(): pass

    label('loc_359')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 1, 0x641)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_36A',
    )

    ChrClearFlags(0x0012, 0x0080)

    def _loc_36A(): pass

    label('loc_36A')

    Return()

# id: 0x0001 offset: 0x36B
@scena.Code('func_01_36B')
def func_01_36B():
    OP_71(0x000C, 0x0002)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 4, 0x644)),
            Expr.Return,
        ),
        'loc_380',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_380(): pass

    label('loc_380')

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0002 offset: 0x38A
@scena.Code('func_02_38A')
def func_02_38A():
    ExecExpressionWithReg(
        0x0001,
        (
            Expr.Rand,
            (Expr.PushLong, 0x8),
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
        'loc_3AF',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_442')

    def _loc_3AF(): pass

    label('loc_3AF')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3C8',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_442')

    def _loc_3C8(): pass

    label('loc_3C8')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3E1',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_442')

    def _loc_3E1(): pass

    label('loc_3E1')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3FA',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_442')

    def _loc_3FA(): pass

    label('loc_3FA')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_413',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_442')

    def _loc_413(): pass

    label('loc_413')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_42C',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_442')

    def _loc_42C(): pass

    label('loc_42C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_442',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    def _loc_442(): pass

    label('loc_442')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_457',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_442')

    def _loc_457(): pass

    label('loc_457')

    Return()

# id: 0x0003 offset: 0x458
@scena.Code('func_03_458')
def func_03_458():
    EventBegin(0x00)
    ChrSetPos(0x0102, 520, 0, -22530, 0)
    ChrSetPos(0x0101, -1610, 0, -22470, 0)
    ChrSetPos(0x0108, -290, 0, -21870, 0)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    CameraMove(-70, 14350, 22560, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3920, 0)
    OP_6C(12000, 0)
    OP_6E(280, 0)

    @scena.Lambda('lambda_04DA')
    def lambda_04DA():
        CameraMove(-8920, 10250, -21440, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_04DA)

    @scena.Lambda('lambda_04F2')
    def lambda_04F2():
        OP_67(0, 8000, -10000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_04F2)

    @scena.Lambda('lambda_050A')
    def lambda_050A():
        CameraSetDistance(3920, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_050A)

    @scena.Lambda('lambda_051A')
    def lambda_051A():
        OP_6C(44000, 10000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_051A)

    @scena.Lambda('lambda_052A')
    def lambda_052A():
        OP_6E(280, 10000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_052A)

    FadeIn(2000, 0)
    Sleep(10000)

    Fade(1000)
    CameraMove(30, 0, -22200, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010120051V#004F哇～～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120052V#010F虽然知道王城是个很华丽的地方……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120053V但是，这比至今为止见过的房间\n',
            '都要豪华不知道多少倍呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080120054V#074F不只是豪华，\n',
            '还蕴含着历史的传统和壮丽。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120055V#070F到处都充满着浓厚的\n',
            '古代王国的传统风格呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0008, 770, 0, -9870, 180)
    ChrSetPos(0x0009, -280, 0, -9260, 180)

    NpcTalk(
        0x0008,
        '女人的声音',
        (
            '#0610120056V欢迎来到格兰赛尔城。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '女人的声音',
        (
            '#0610120057V请问你们就是\n',
            '金先生一行人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_0768')
    def lambda_0768():
        ChrWalkTo(0x00FE, -80, 0, -19430, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0768)

    @scena.Lambda('lambda_0783')
    def lambda_0783():
        ChrWalkTo(0x00FE, -850, 0, -18600, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0783)

    CameraMove(130, 0, -20310, 3000)

    ChrTalk(
        0x0101,
        (
            '#0010120058V#509F（哎哎……是凯诺娜上尉……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120059V#012F（虽然也不是没有预料到……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080120060V#070F啊，没错。\n',
            '我们受了公爵大人的邀请。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120061V请问……你是？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0008, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#0610120062V#182F呵呵，忘了自我介绍。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610120063V我是担任格兰赛尔城警卫工作的\n',
            '情报部的凯诺娜上尉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610120064V恭喜金先生你们获得武术大会的优胜。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610120065V我看了你们的比赛，\n',
            '真是威风凛凛，令人叹为观止啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080120066V#071F哎呀～真是过奖了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120067V我倒觉得，如此年轻美丽的女性\n',
            '能当上军队的上尉才是让人吃惊呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120068V一定是非常优秀才能做到这样吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0610120069V#184F哎呀……金先生您真会说话。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610120070V#180F哦，这两位不是年轻的游击士嘛。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120071V#002F……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120072V#012F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0610120073V#180F艾丝蒂尔·布莱特，\n',
            '以及约修亚·布莱特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610120074V蔡斯事件之后我们就没见过面吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120075V#006F……嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120076V#010F确实很久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0610120077V#181F虽然很遗憾，\n',
            '不过博士的事件还没有完全解决。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610120078V博士和他的孙女儿\n',
            '好像被一伙不知名的暴徒绑架了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610120079V#188F艾丝蒂尔你们\n',
            '有没有这方面的线索呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120080V#505F那、那个。\n',
            '一点也不知道呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120081V#015F那个事情交给了正游击士去处理，\n',
            '然后我们就来王都了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120082V之后的事情就没再听说了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0610120083V#188F是吗……呵呵。\n',
            '那真是遗憾呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610120084V不过，只要借助情报部的力量，\n',
            '逮捕绑架犯也只是时间上的问题了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610120085V就请你们瞧着吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120086V#009F（这、这只母狐狸～……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120087V#019F我知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120088V博士和他的孙女是我们的好朋友，\n',
            '所以请你们一定要把他们救出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0610120089V#181F那是当然的了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610120090V#182F好了，晚宴快开始了。\n',
            '这就把你们安排到各自的房间去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0009, 400)

    ChrTalk(
        0x0008,
        (
            '#0610120091V#182F#2P茜亚小姐……\n',
            '接下来就交给你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0008, 400)

    ChrTalk(
        0x0009,
        (
            '#2300120092V#5P是……\n',
            '我会好好照顾客人的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0610120093V#180F#2P还有，麻烦你记住一点……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610120094V不要对这些客人没有礼貌，\n',
            '说些不该说的话。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610120095V记住了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2300120096V#5P是、是的……\n',
            '我明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0610120097V#188F#2P哼哼，这样就好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0102, 400)
    ChrTurnDirection(0x0008, 0x0108, 400)

    ChrTalk(
        0x0008,
        (
            '#0610120098V#182F那么各位，\n',
            '希望你们今晚过得愉快。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610120099V我就此告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1007')
    def lambda_1007():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_1007')

    DispatchAsync2(0x0108, 0x0001, lambda_1007)

    @scena.Lambda('lambda_1018')
    def lambda_1018():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_1018')

    DispatchAsync2(0x0101, 0x0001, lambda_1018)

    @scena.Lambda('lambda_1029')
    def lambda_1029():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_1029')

    DispatchAsync2(0x0102, 0x0001, lambda_1029)

    ChrSetDirection(0x0008, 45, 400)
    ChrWalkTo(0x0008, 1840, 0, -15630, 2000, 0x00)

    @scena.Lambda('lambda_1055')
    def lambda_1055():
        ChrWalkTo(0x00FE, 7360, 0, -10100, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1055)

    Sleep(1500)

    ChrTalk(
        0x0108,
        (
            '#0080120100V#070F唔～感觉这个女人还不错嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0108, 0xFF)
    OP_62(0x0101, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0108, 400)

    ChrTalk(
        0x0101,
        (
            '#0010120101V#509F金先生，你的兴趣真是奇怪啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120102V那个母狐狸，有什么地方好啊？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0108, 400)

    ChrTalk(
        0x0102,
        (
            '#0020120103V#014F那样的人，是金先生喜欢的类型吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0108, 0x0101, 400)

    ChrTalk(
        0x0108,
        (
            '#0080120104V#071F#5P哈哈，只是外表那样而已，\n',
            '但其实本质上还是很纯情的哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120105V就是这一点最吸引人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120106V#007F不行了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120107V#006F不管怎么样都好啦。\n',
            '金先生，你真像个大叔呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080120108V#072F#5P#5S……（受到打击）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_127E')
    def lambda_127E():
        CameraMove(-240, 0, -20830, 1000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_127E)

    ChrWalkTo(0x0009, -260, 0, -20090, 1500, 0x00)
    ChrTurnDirection(0x0009, 0x0108, 400)

    ChrTalk(
        0x0009,
        (
            '#2300120109V#5P我、我说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_12D2')
    def lambda_12D2():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_12D2)

    @scena.Lambda('lambda_12E0')
    def lambda_12E0():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_12E0)

    ChrTurnDirection(0x0101, 0x0009, 400)

    ChrTalk(
        0x0101,
        (
            '#0010120110V#506F啊，不好意思～～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120111V现在可以带我们去看看房间吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2300120112V#5P好的……\n',
            '我来带路吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2300120113V#5P还没做自我介绍，\n',
            '我是这里的侍女，名叫茜亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2300120114V#5P从晚宴开始到明天，\n',
            '由我来照顾你们的起居生活。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2300120115V#5P如果各位客人有什么需要，\n',
            '随时告诉我就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080120116V#070F啊啊，拜托你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120117V#010F那么，现在带我们去房间吧？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2300120118V#5P啊，好的。\n',
            '各位的房间在二楼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0009, 315, 400)
    CreateThread(0x0009, 0x01, 0x00, func_04_1908)
    Sleep(50)

    ChrWalkTo(0x0108, -240, 0, -20830, 3000, 0x00)
    OP_6A(0x0108)
    CreateThread(0x0108, 0x01, 0x00, func_04_1908)
    Sleep(150)

    CreateThread(0x0101, 0x01, 0x00, func_04_1908)
    Sleep(400)

    CreateThread(0x0102, 0x01, 0x00, func_04_1908)
    Sleep(12000)

    OP_66(0x0000)
    WaitForThreadExit(0x0009, 0x0001)

    @scena.Lambda('lambda_151A')
    def lambda_151A():
        OP_6E(196, 3000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_151A)

    @scena.Lambda('lambda_152A')
    def lambda_152A():
        ChrWalkTo(0x00FE, 50, 9000, 23150, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_152A)

    WaitForThreadExit(0x0108, 0x0001)

    @scena.Lambda('lambda_154A')
    def lambda_154A():
        ChrWalkTo(0x00FE, 1040, 9000, 22000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_154A)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_156A')
    def lambda_156A():
        ChrWalkTo(0x00FE, -1130, 9000, 21070, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_156A)

    WaitForThreadExit(0x0102, 0x0001)

    @scena.Lambda('lambda_158A')
    def lambda_158A():
        ChrWalkTo(0x00FE, -110, 9000, 20410, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_158A)

    MapClearFlags(0x00000001)
    CameraMove(4840, 9000, 32350, 3000)

    ChrTalk(
        0x0101,
        (
            '#0010120119V#004F#5S哇～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120120V#001F那个巨大的吊灯，真是豪华绚丽呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120121V#017F艾丝蒂尔，不要大声喧哗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120122V#010F对了，那边是……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1669')
    def lambda_1669():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1669)

    @scena.Lambda('lambda_1677')
    def lambda_1677():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_1677)

    @scena.Lambda('lambda_1685')
    def lambda_1685():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_1685)

    ChrSetDirection(0x0009, 180, 400)

    ChrTalk(
        0x0009,
        (
            '#2300120123V#5P是『谒见室』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2300120124V#5P艾莉茜雅女王陛下\n',
            '就是在这里会见客人的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2300120125V#5P不过最近一直没有用过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1726')
    def lambda_1726():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1726)

    @scena.Lambda('lambda_1734')
    def lambda_1734():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_1734)

    ChrTurnDirection(0x0102, 0x0009, 400)

    ChrTalk(
        0x0102,
        (
            '#0020120126V#012F……是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_69(0x0009, 1500)
    OP_6A(0x0009)

    ChrTalk(
        0x0108,
        (
            '#0080120127V#073F#2P说起来，\n',
            '女王陛下的病情有那么严重吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120128V不是就要举行诞辰庆典了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrTurnDirection(0x0009, 0x0108, 400)

    ChrTalk(
        0x0009,
        (
            '#2300120129V#5P不、不是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2300120130V#5P最近照顾陛下的，\n',
            '是这里的女官长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2300120131V#5P所以……\n',
            '我不太清楚具体的情况……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0102, 0)

    ChrTalk(
        0x0009,
        (
            '#2300120132V#5P真、真是不好意思……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_66(0x0001)
    ChrSetDirection(0x0009, 270, 400)
    CreateThread(0x0009, 0x01, 0x00, func_05_1A85)
    Sleep(420)

    CreateThread(0x0101, 0x01, 0x00, func_05_1A85)
    Sleep(150)

    CreateThread(0x0102, 0x01, 0x00, func_05_1A85)
    Sleep(400)

    CreateThread(0x0108, 0x01, 0x00, func_05_1A85)
    Sleep(3000)

    OP_28(0x0049, 0x01, 0x0080)
    OP_28(0x0049, 0x01, 0x0100)
    OP_28(0x0049, 0x01, 0x0200)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T4262._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0x1908
@scena.Code('func_04_1908')
def func_04_1908():
    ChrWalkTo(0x00FE, -1210, 0, -15560, 3000, 0x01)
    ChrWalkTo(0x00FE, -1860, 0, -14700, 3000, 0x01)
    ChrWalkTo(0x00FE, -3820, 0, -12520, 3000, 0x01)
    ChrWalkTo(0x00FE, -8080, 0, -10300, 3000, 0x01)
    ChrWalkTo(0x00FE, -8080, 0, -10300, 3000, 0x01)
    ChrWalkTo(0x00FE, -12960, 0, -9190, 3000, 0x01)
    ChrWalkTo(0x00FE, -15420, 0, -7110, 3000, 0x01)
    ChrWalkTo(0x00FE, -17480, 0, -520, 3000, 0x01)
    ChrWalkTo(0x00FE, -17190, 1250, 3150, 3000, 0x01)
    ChrWalkTo(0x00FE, -16219, 2500, 5730, 3000, 0x01)
    ChrWalkTo(0x00FE, -15090, 3500, 7960, 3000, 0x01)
    ChrWalkTo(0x00FE, -13020, 5000, 10640, 3000, 0x01)
    ChrWalkTo(0x00FE, -10430, 6250, 12400, 3000, 0x01)
    ChrWalkTo(0x00FE, -8180, 7250, 13350, 3000, 0x01)
    ChrWalkTo(0x00FE, -5780, 8250, 13950, 3000, 0x01)
    ChrWalkTo(0x00FE, -2210, 9000, 14440, 3000, 0x01)
    ChrWalkTo(0x00FE, -1160, 9000, 14880, 3000, 0x01)
    ChrWalkTo(0x00FE, -430, 9000, 15810, 3000, 0x01)
    ChrWalkTo(0x00FE, 20, 9000, 17590, 3000, 0x01)

    Return()

# id: 0x0005 offset: 0x1A85
@scena.Code('func_05_1A85')
def func_05_1A85():
    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, -3610, 9000, 24020, 3000, 0x01)
    ChrWalkTo(0x00FE, -7960, 9000, 25860, 3000, 0x01)
    ChrWalkTo(0x00FE, -9570, 9000, 26050, 3000, 0x01)

    @scena.Lambda('lambda_1ACC')
    def lambda_1ACC():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1ACC)

    ChrWalkTo(0x00FE, -12900, 9000, 26050, 3000, 0x01)

    Return()

# id: 0x0006 offset: 0x1AED
@scena.Code('func_06_1AED')
def func_06_1AED():
    EventBegin(0x00)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x000A, -6640, 8000, 13770, 80)
    ChrSetPos(0x0008, -7900, 7500, 13100, 62)
    ChrSetPos(0x0101, -7920, 9000, 24630, 90)
    ChrSetPos(0x0102, -7520, 9000, 25920, 90)
    CameraMove(-7580, 9000, 25280, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    Sleep(1000)

    NpcTalk(
        0x000A,
        '男性的声音',
        (
            '#0130120810V#1P哦，是你们两个啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120811V#580F啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1BD8')
    def lambda_1BD8():
        CameraMove(-3860, 9000, 20630, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1BD8)

    @scena.Lambda('lambda_1BF0')
    def lambda_1BF0():
        ChrSetDirection(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1BF0)

    @scena.Lambda('lambda_1BFE')
    def lambda_1BFE():
        ChrSetDirection(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1BFE)

    Sleep(1000)

    @scena.Lambda('lambda_1C11')
    def lambda_1C11():
        ChrWalkTo(0x00FE, -2029, 9000, 14880, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1C11)

    @scena.Lambda('lambda_1C2C')
    def lambda_1C2C():
        ChrWalkTo(0x00FE, -2260, 9000, 13770, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1C2C)

    WaitForThreadExit(0x000A, 0x0001)

    @scena.Lambda('lambda_1C4C')
    def lambda_1C4C():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1C4C)

    WaitForThreadExit(0x0008, 0x0001)

    @scena.Lambda('lambda_1C5F')
    def lambda_1C5F():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1C5F)

    @scena.Lambda('lambda_1C6D')
    def lambda_1C6D():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_1C6D')

    DispatchAsync2(0x0101, 0x0001, lambda_1C6D)

    @scena.Lambda('lambda_1C7E')
    def lambda_1C7E():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_1C7E')

    DispatchAsync2(0x0102, 0x0001, lambda_1C7E)

    ChrTalk(
        0x0102,
        (
            '#0020120812V#012F理查德上校……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1CB4')
    def lambda_1CB4():
        CameraMove(-4040, 9000, 25340, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1CB4)

    CreateThread(0x000A, 0x01, 0x00, func_07_259A)
    Sleep(300)

    CreateThread(0x0008, 0x01, 0x00, func_07_259A)
    Sleep(2000)

    @scena.Lambda('lambda_1CE4')
    def lambda_1CE4():
        ChrWalkTo(0x00FE, -5300, 9000, 24610, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1CE4)

    Sleep(300)

    @scena.Lambda('lambda_1D04')
    def lambda_1D04():
        ChrWalkTo(0x00FE, -5380, 9000, 25710, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1D04)

    WaitForThreadExit(0x000A, 0x0001)

    @scena.Lambda('lambda_1D24')
    def lambda_1D24():
        ChrSetDirection(0x00FE, 270, 0)
        Yield()

        Jump('lambda_1D24')

    DispatchAsync2(0x000A, 0x0001, lambda_1D24)

    @scena.Lambda('lambda_1D35')
    def lambda_1D35():
        ChrWalkTo(0x00FE, -3690, 9000, 25330, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_1D35)

    WaitForThreadExit(0x0008, 0x0001)

    @scena.Lambda('lambda_1D55')
    def lambda_1D55():
        ChrSetDirection(0x00FE, 270, 0)
        Yield()

        Jump('lambda_1D55')

    DispatchAsync2(0x0008, 0x0001, lambda_1D55)

    WaitForThreadExit(0x000A, 0x0002)

    ChrTalk(
        0x000A,
        (
            '#0130120813V#111F#2P呵呵……\n',
            '艾丝蒂尔和约修亚啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120814V我们像这样面对面地对话\n',
            '已经不是第一次了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120815V#004F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120816V#010F我们最后一次对话\n',
            '是在戴尔蒙市长被捕之后。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120817V不过没有想到上校您还能记得我们。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0130120818V#110F#2P虽然见面的机会很少，\n',
            '不过你们给我留下了很深的印象。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120819V因此我调查了一下，结果让我大吃一惊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120820V没有想到你们竟然是\n',
            '卡西乌斯上校的孩子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010120821V#580F这、这件事也知道……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0130120822V#111F#2P哈哈，\n',
            '情报部可不是浪得虚名的哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120823V#115F……卡西乌斯上校当年在军中时\n',
            '曾给予我多方的照料。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120824V正因如此……\n',
            '我实在难以用言语表达我的谢意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120825V#002F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0130120826V#110F#2P怎么样，我们去稍微谈谈如何呢？\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120827V我之前就一直想和你们私下聊聊了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120828V#580F哎哎！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101434V#012F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x000A, 400)

    ChrTalk(
        0x0008,
        (
            '#0610120830V#184F对、对不起，上校……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610120831V不是要去和公爵大人商量相关事宜吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0130120832V#115F#2P稍微迟一会儿也没关系的吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120833V#110F对了，我们谈话的话，\n',
            '就借里面的谈话室一用吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120834V我请你们喝不带酒精的鸡尾酒。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0610120835V#187F只、只是这样的话，\n',
            '那就让我准备吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0008, 400)

    ChrTalk(
        0x000A,
        (
            '#0130120836V#112F不，这与你无关。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120837V你到公爵那里去，\n',
            '把我要迟一会儿的口信转告给他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0610120838V#183F明、明白了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_22E3')
    def lambda_22E3():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_22E3')

    DispatchAsync2(0x000A, 0x0001, lambda_22E3)

    @scena.Lambda('lambda_22F4')
    def lambda_22F4():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_22F4')

    DispatchAsync2(0x0101, 0x0001, lambda_22F4)

    @scena.Lambda('lambda_2305')
    def lambda_2305():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_2305')

    DispatchAsync2(0x0102, 0x0001, lambda_2305)

    ChrTurnDirection(0x0008, 0x0101, 400)
    OP_62(0x0008, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0610120839V#186F……………………（怒视）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010120840V#509F……（我好怕怕）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0610120841V#181F……那么我就先告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 45, 400)
    ChrWalkTo(0x0008, -150, 9000, 28360, 3000, 0x00)

    @scena.Lambda('lambda_23D7')
    def lambda_23D7():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_23D7)

    ChrWalkTo(0x0008, -70, 9000, 33280, 3000, 0x00)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    ChrSetDirection(0x000A, 270, 400)

    @scena.Lambda('lambda_2410')
    def lambda_2410():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_2410')

    DispatchAsync2(0x0101, 0x0001, lambda_2410)

    @scena.Lambda('lambda_2421')
    def lambda_2421():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_2421')

    DispatchAsync2(0x0102, 0x0001, lambda_2421)

    ChrTalk(
        0x000A,
        (
            '#0130120842V#110F#2P我们这就到谈话室去吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120843V请跟我来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000A, 90, 400)

    @scena.Lambda('lambda_2484')
    def lambda_2484():
        ChrWalkTo(0x00FE, 9130, 9000, 25780, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_2484)

    @scena.Lambda('lambda_249F')
    def lambda_249F():
        CameraMove(-3040, 9000, 25340, 1500)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_249F)

    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010111729V#580F啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120845V#003F（我说约修亚啊，怎么办好呢？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120846V#012F（只有先奉陪一下了……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120847V（虽说会有些迟，\n',
            '　但只有稍后才去夫人那里了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x004A, 0x01, 0x0008)
    OP_28(0x004A, 0x01, 0x0010)
    OP_20(0x000005DC)
    FadeOut(1500, 0, -1)
    OP_0D()
    OP_21()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T4261._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0007 offset: 0x259A
@scena.Code('func_07_259A')
def func_07_259A():
    ChrWalkTo(0x00FE, -1800, 9000, 20840, 3000, 0x00)
    ChrWalkTo(0x00FE, -2710, 9000, 24430, 3000, 0x00)

    Return()

# id: 0x0008 offset: 0x25C3
@scena.Code('func_08_25C3')
def func_08_25C3():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 7, 0x647)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_25D0',
    )

    Return()

    def _loc_25D0(): pass

    label('loc_25D0')

    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x00C8, 7, 0x647))
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x0008, -70, 9000, 27870, 180)
    ChrSetPos(0x000B, -800, 9000, 28970, 180)
    ChrSetPos(0x000C, 530, 9000, 28970, 180)

    NpcTalk(
        0x0008,
        '女性的声音',
        (
            '#0610121479V#4P……都这种时候了，\n',
            '你们还在这里做什么啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(200)

    @scena.Lambda('lambda_2699')
    def lambda_2699():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2699)

    @scena.Lambda('lambda_26A7')
    def lambda_26A7():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_26A7)

    CameraMove(10, 9000, 27580, 2000)

    ChrTalk(
        0x0101,
        (
            '#0010121480V#580F#1P啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    FormationAddMember(0x07, 0xFF)
    ChrSetPos(0x0101, -550, 9000, 16309, 0)
    ChrSetPos(0x0102, 670, 9000, 16190, 0)
    ChrSetFlags(0x0108, 0x0080)

    @scena.Lambda('lambda_2717')
    def lambda_2717():
        ChrWalkTo(0x00FE, 140, 9000, 19940, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2717)

    Sleep(200)

    @scena.Lambda('lambda_2737')
    def lambda_2737():
        ChrWalkTo(0x00FE, -580, 9000, 21140, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_2737)

    Sleep(100)

    @scena.Lambda('lambda_2757')
    def lambda_2757():
        ChrWalkTo(0x00FE, 830, 9000, 21150, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_2757)

    CameraMove(100, 9000, 18910, 3000)

    ChrTalk(
        0x0102,
        (
            '#0020121481V#012F凯诺娜上尉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0008, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#0610121482V#182F哼哼哼，晚上好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610121483V怎么说你们也是贵宾，\n',
            '我还是对你们比较客气的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610121484V可要说是孩子晚上出去散步\n',
            '不觉得未免太迟了一些吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121485V#015F很抱歉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121486V因为看见城里有许多新奇的东西，\n',
            '所以稍微迟了一些……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0610121487V#182F哎呀，这没什么啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610121488V那么你们３０分钟之前\n',
            '在哪里参观呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610121489V能不能告诉我，　\n',
            '让我做个参考呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121490V#505F嗯……',
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
            TXT(0x00, '【厨房】\n'),
            TXT(0x01, '【侍女休息室】\n'),
            TXT(0x02, '【行政区域】\n'),
            TXT(0x03, '【亲卫队值勤室】\n'),
            TXT(0x04, '【地下仓库】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_29EE'),
        (0x00000001, 'loc_2B46'),
        (0x00000002, 'loc_2C45'),
        (0x00000003, 'loc_2DA8'),
        (0x00000004, 'loc_2F24'),
        (-1, 'loc_3075'),
    )

    def _loc_29EE(): pass

    label('loc_29EE')

    ChrTalk(
        0x0008,
        (
            '#0610121491V#180F哎呀，很可疑呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610121492V刚才我去巡视的时候\n',
            '怎么没有看见你们呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121493V#009F那是、那是因为……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0610121494V#181F算了算了。\n',
            '我不准备再和你们兜圈子了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610121495V#188F事实上我已经收到了报告，\n',
            '发现你们两个曾屡次在侍女休息室进出。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610121496V到那样的地方去参观，\n',
            '难道不是十分可疑的行为吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3075')

    def _loc_2B46(): pass

    label('loc_2B46')

    ChrTalk(
        0x0008,
        (
            '#0610121497V#180F呵呵……\n',
            '真是老实的孩子呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610121494V#181F算了算了。\n',
            '我不准备再和你们兜圈子了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610121495V#188F事实上我已经收到了报告，\n',
            '发现你们两个曾屡次在侍女休息室进出。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610121496V到那样的地方去参观，\n',
            '难道不是十分可疑的行为吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3075')

    def _loc_2C45(): pass

    label('loc_2C45')

    ChrTalk(
        0x0008,
        (
            '#0610121501V#180F行政区域的值班人\n',
            '早就已经回去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610121502V你们在那种地方，\n',
            '到底干了些什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121493V#009F那是、那是因为……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0610121494V#181F算了算了。\n',
            '我不准备再和你们兜圈子了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610121495V#188F事实上我已经收到了报告，\n',
            '发现你们两个曾屡次在侍女休息室进出。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610121496V到那样的地方去参观，\n',
            '难道不是十分可疑的行为吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3075')

    def _loc_2DA8(): pass

    label('loc_2DA8')

    ChrTalk(
        0x0008,
        (
            '#0610121507V那真是奇怪了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610121508V那里现在正作为我们\n',
            '情报部的办公室使用……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610121509V是不可能让你们进去参观的。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121493V#009F那是、那是因为……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0610121494V#181F算了算了。\n',
            '我不准备再和你们兜圈子了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610121495V#188F事实上我已经收到了报告，\n',
            '发现你们两个曾屡次在侍女休息室进出。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610121496V到那样的地方去参观，\n',
            '难道不是十分可疑的行为吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3075')

    def _loc_2F24(): pass

    label('loc_2F24')

    ChrTalk(
        0x0008,
        (
            '#0610121514V#183F什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610121515V你们去那种地方\n',
            '到底干了些什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121516V#009F没、没有干什么事情啊……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0610121494V#181F算了算了。\n',
            '我不准备再和你们兜圈子了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610121495V#188F事实上我已经收到了报告，\n',
            '发现你们两个曾屡次在侍女休息室进出。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610121496V到那样的地方去参观，\n',
            '难道不是十分可疑的行为吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3075')

    def _loc_3075(): pass

    label('loc_3075')

    ChrTalk(
        0x0101,
        (
            '#0010121520V#005F什么……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121521V#012F你明知故问，\n',
            '人品也太差了一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0610121522V#188F哼哼哼……\n',
            '不错的赞美之词嘛，我先收下了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610121523V刚才只是调和一下气氛而已。\n',
            '说吧，去侍女休息室到底做什么？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610121524V老老实实回答对你们有好处哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121525V#013F那是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0108, 7350, 9000, 25020, 225)

    NpcTalk(
        0x0108,
        '男性的声音',
        (
            '#0080121526V#3P喂～～～～～！\n',
            '艾丝蒂尔、约修亚！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0108,
        '男性的声音',
        (
            '#0080121527V#3P原来你们还呆在那里啊～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0108, 0x0080)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_32B3')
    def lambda_32B3():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_32B3)

    @scena.Lambda('lambda_32C1')
    def lambda_32C1():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_32C1)

    @scena.Lambda('lambda_32CF')
    def lambda_32CF():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_32CF)

    @scena.Lambda('lambda_32DD')
    def lambda_32DD():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_32DD)

    @scena.Lambda('lambda_32EB')
    def lambda_32EB():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_32EB)

    CameraMove(3730, 9000, 21420, 2000)

    @scena.Lambda('lambda_330A')
    def lambda_330A():
        ChrTurnDirection(0x00FE, 0x0108, 0)
        Yield()

        Jump('lambda_330A')

    DispatchAsync2(0x0101, 0x0001, lambda_330A)

    @scena.Lambda('lambda_331B')
    def lambda_331B():
        ChrTurnDirection(0x00FE, 0x0108, 0)
        Yield()

        Jump('lambda_331B')

    DispatchAsync2(0x0102, 0x0001, lambda_331B)

    @scena.Lambda('lambda_332C')
    def lambda_332C():
        ChrTurnDirection(0x00FE, 0x0108, 0)
        Yield()

        Jump('lambda_332C')

    DispatchAsync2(0x0008, 0x0001, lambda_332C)

    @scena.Lambda('lambda_333D')
    def lambda_333D():
        ChrTurnDirection(0x00FE, 0x0108, 0)
        Yield()

        Jump('lambda_333D')

    DispatchAsync2(0x000B, 0x0001, lambda_333D)

    @scena.Lambda('lambda_334E')
    def lambda_334E():
        ChrTurnDirection(0x00FE, 0x0108, 0)
        Yield()

        Jump('lambda_334E')

    DispatchAsync2(0x000C, 0x0001, lambda_334E)

    ChrTalk(
        0x0102,
        (
            '#0020121528V#014F金先生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3380')
    def lambda_3380():
        CameraMove(900, 9000, 19490, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3380)

    @scena.Lambda('lambda_3398')
    def lambda_3398():
        OP_6E(256, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3398)

    @scena.Lambda('lambda_33A8')
    def lambda_33A8():
        OP_9E(0x00FE, 60, 0, 3000, 700)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_33A8)

    ChrWalkTo(0x0108, 1880, 9000, 19250, 2000, 0x00)
    Sleep(400)

    ChrSetChipByIndex(0x0108, 7)
    PlaySE(178, 0x00, 0x64)
    ChrSetSubChip(0x0108, 0)
    Sleep(150)

    ChrSetSubChip(0x0108, 1)
    Sleep(150)

    ChrSetSubChip(0x0108, 2)
    Sleep(150)

    ChrSetSubChip(0x0108, 0)
    Sleep(150)

    ChrSetSubChip(0x0108, 1)
    Sleep(150)

    ChrSetSubChip(0x0108, 2)
    Sleep(150)

    ChrSetSubChip(0x0108, 0)
    Sleep(180)

    ChrSetSubChip(0x0108, 1)
    Sleep(180)

    ChrSetSubChip(0x0108, 2)
    Sleep(200)

    ChrSetSubChip(0x0108, 3)
    Sleep(100)

    ChrSetSubChip(0x0108, 4)
    Sleep(170)

    ChrTalk(
        0x0108,
        (
            '#0080121529V#079F哇～流到身上了！',
            TxtCtl.Enter,
        ),
    )

    ChrSetSubChip(0x0108, 5)
    Sleep(70)

    ChrSetSubChip(0x0108, 6)
    Sleep(70)

    ChrSetSubChip(0x0108, 7)
    Sleep(350)

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121530V#509F哇，喝得酩酊大醉的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)

    ExecExpressionWithValue(
        0x0108,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0108, 65535)
    OP_0D()
    ChrTurnDirection(0x0108, 0x0008, 0)
    Sleep(400)

    ChrTalk(
        0x0108,
        (
            '#0080121531V#570F哦，抱歉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080121532V我说你们是和谁在这里呢，\n',
            '原来是和美女军官在一起啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080121533V#079F哎呀啊～\n',
            '怎么说都是美妙的邂逅啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0610121534V#184F是、是啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080121535V#078F怎么了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080121536V我那两个不成器的徒弟\n',
            '给您添了不少麻烦吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121537V#004F徒、徒弟……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0610121538V#183F没有，不过刚才他们竟然\n',
            '屡次出入侍女休息室……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610121539V出于保卫王城安全的理由，\n',
            '我想问问他们在里面做了些什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080121540V#079F哦，原来是这么回事啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080121541V下酒的菜都没有了，\n',
            '所以我叫他们去取一些来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0108, 225, 0)
    Sleep(400)

    ChrTalk(
        0x0108,
        (
            '#0080121542V#078F喂，约修亚，\n',
            '还有什么可以吃的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121543V#010F没有了，\n',
            '厨师他们好像已经回去休息了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121544V我又问了侍女她们，\n',
            '虽然她们去找了一下，\n',
            '但下酒菜是的确没有了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080121545V#571F呼，没办法啦。\n',
            '没有下酒菜就只有忍了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0108, 0x00000000, 2300, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTalk(
        0x0108,
        (
            '#0080121546V#570F对了……\n',
            '我想到了一个好办法！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0108, 0x0008, 0)
    Sleep(400)

    @scena.Lambda('lambda_386B')
    def lambda_386B():
        OP_9E(0x00FE, 100, 0, 1000, 300)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_386B)

    OP_92(0x0108, 0x0008, 800, 1000, 0x00)

    ChrTalk(
        0x0108,
        (
            '#0080121547V#079F#2P如果您不介意的话，\n',
            '赏面陪我喝喝酒谈谈心如何呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080121548V哇哈哈～～～\n',
            '美人的笑脸是最好的下酒佳肴啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_94(0x01, 0x0008, 0x00B4, 0x000001F4, 0x00000BB8, 0x00)

    ChrTalk(
        0x0008,
        (
            '#0610121549V#187F我、我还有任务在身，\n',
            '恕我无法奉陪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0008, 0xFF)
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#0610121550V#183F#1P刚才的那件事姑且不问……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610121551V你们现在就回房间去，\n',
            '今晚不准再出来乱走。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610121552V如果再发现你们有可疑的行动，\n',
            '我会保留调查的权利哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000C, 0xFF)

    @scena.Lambda('lambda_3A3E')
    def lambda_3A3E():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_3A3E')

    DispatchAsync2(0x0101, 0x0001, lambda_3A3E)

    @scena.Lambda('lambda_3A4F')
    def lambda_3A4F():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_3A4F')

    DispatchAsync2(0x0102, 0x0001, lambda_3A4F)

    @scena.Lambda('lambda_3A60')
    def lambda_3A60():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_3A60')

    DispatchAsync2(0x0108, 0x0001, lambda_3A60)

    ChrTalk(
        0x0101,
        (
            '#0010121553V#009F知、知道了还不行嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121554V#015F已经很晚了，\n',
            '我们也该休息了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0610121555V#180F#1P哼哼，老实点好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610121556V#181F那么……\n',
            '我们这就告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0008, 0x01, 0x00, func_09_3C61)
    Sleep(500)

    CreateThread(0x000B, 0x01, 0x00, func_09_3C61)
    Sleep(500)

    CreateThread(0x000C, 0x01, 0x00, func_09_3C61)

    @scena.Lambda('lambda_3B45')
    def lambda_3B45():
        CameraMove(710, 9000, 17230, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_3B45)

    Sleep(1500)

    TerminateThread(0x0108, 0xFF)
    ChrSetDirection(0x0108, 180, 0)
    WaitForThreadExit(0x0008, 0x0002)
    Sleep(2000)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0108, 0xFF)
    CameraMove(710, 9000, 18930, 1000)
    Sleep(400)

    ChrTalk(
        0x0108,
        (
            '#0080121557V#570F哎呀，这就走掉了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080121558V#571F没办法了……\n',
            '我回房间休息去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0108, 400)
    ChrTurnDirection(0x0101, 0x0108, 400)

    ChrTalk(
        0x0101,
        (
            '#0010121559V#506F嗯，好的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121560V#010F我们也一起回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeIn(1500, 0)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/T4262._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0009 offset: 0x3C61
@scena.Code('func_09_3C61')
def func_09_3C61():
    ChrWalkTo(0x00FE, -1600, 9000, 19000, 3000, 0x00)
    ChrWalkTo(0x00FE, -1600, 9000, 15470, 3000, 0x00)
    ChrWalkTo(0x00FE, 100, 9000, 14170, 3000, 0x00)
    ChrWalkTo(0x00FE, 4320, 9000, 14170, 3000, 0x00)
    ChrWalkTo(0x00FE, 8280, 7250, 13480, 3000, 0x00)
    ChrWalkTo(0x00FE, 13650, 4500, 9700, 3000, 0x00)

    Return()

# id: 0x000A offset: 0x3CDA
@scena.Code('func_0A_3CDA')
def func_0A_3CDA():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 0, 0x660)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3E34',
    )

    EventBegin(0x01)
    OP_4A(0x000D, 255)

    If(
        (
            (Expr.Eval, "OP_42(0x0037)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3DA1',
    )

    ChrTurnDirection(0x000D, 0x0000, 400)

    ChrTalk(
        0x000D,
        (
            '#4340120509V哎呀呀，这不是希尔丹夫人吗……\n',
            '到我们这儿来有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#4340120510V这里是情报部的值勤室。\n',
            '请不要随随便便靠近。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, -1500, 0, 0, 3000, 0x00)
    ChrSetDirection(0x000D, 270, 0)

    Jump('loc_3E29')

    def _loc_3DA1(): pass

    label('loc_3DA1')

    ChrTurnDirection(0x000D, 0x0000, 400)

    ChrTalk(
        0x000D,
        (
            '#4340120511V这里是情报部的值勤室。\n',
            '平民禁止入内。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#4340120512V不想被逮捕的话，\n',
            '就不要靠近。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, -1500, 0, 0, 3000, 0x00)
    ChrSetDirection(0x000D, 270, 0)

    def _loc_3E29(): pass

    label('loc_3E29')

    OP_4B(0x000D, 255)
    Sleep(50)

    EventEnd(0x04)

    def _loc_3E34(): pass

    label('loc_3E34')

    Return()

# id: 0x000B offset: 0x3E35
@scena.Code('func_0B_3E35')
def func_0B_3E35():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3E42',
    )

    Return()

    def _loc_3E42(): pass

    label('loc_3E42')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_3EE8',
    )

    EventBegin(0x01)
    OP_4A(0x0010, 255)
    OP_4A(0x0011, 255)

    ChrTalk(
        0x0011,
        (
            '#4200120516V哦？有什么事吗？\n',
            '现在不能打开城门。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#4200120191V很抱歉，\n',
            '你们请在城内好好放松吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    ChrSetDirection(0x0010, 0, 0)
    ChrSetDirection(0x0011, 0, 0)
    OP_4B(0x0010, 255)
    OP_4B(0x0011, 255)

    Jump('loc_4090')

    def _loc_3EE8(): pass

    label('loc_3EE8')

    EventBegin(0x01)
    OP_4A(0x000E, 255)
    OP_4A(0x000F, 255)

    If(
        (
            (Expr.Eval, "OP_42(0x0037)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3FC3',
    )

    ChrTurnDirection(0x000E, 0x0000, 400)
    ChrTurnDirection(0x000F, 0x0000, 400)

    ChrTalk(
        0x000E,
        (
            '#4320120192V哦，希尔丹夫人。都这么晚了还要外出吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#4330120193V您也是知道的，出于安全考虑，\n',
            '现在城门的开闭受到限制。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#4330120194V没有得到许可\n',
            '是不能从这里通行的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4066')

    def _loc_3FC3(): pass

    label('loc_3FC3')

    ChrTurnDirection(0x000E, 0x0000, 400)
    ChrTurnDirection(0x000F, 0x0000, 400)

    ChrTalk(
        0x000F,
        (
            '#4330120195V出于安全考虑，\n',
            '现在城门的开闭受到限制。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#4320120196V请在王城内\n',
            '随便活动吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#4320120197V你们应该不会觉得\n',
            '有什么不自由吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4066(): pass

    label('loc_4066')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    ChrSetDirection(0x000E, 0, 0)
    ChrSetDirection(0x000F, 0, 0)
    OP_4B(0x000E, 255)
    OP_4B(0x000F, 255)

    def _loc_4090(): pass

    label('loc_4090')

    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x000C offset: 0x4098
@scena.Code('func_0C_4098')
def func_0C_4098():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 1, 0x641)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_40A5',
    )

    Return()

    def _loc_40A5(): pass

    label('loc_40A5')

    EventBegin(0x01)
    OP_4A(0x0012, 255)
    ChrTurnDirection(0x0012, 0x0000, 400)

    If(
        (
            (Expr.Eval, "OP_42(0x0037)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_412F',
    )

    ChrTalk(
        0x0012,
        (
            '#4300120932V现在谒见大厅里\n',
            '正在进行一个重要会议。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#4300120933V非常抱歉，\n',
            '目前还不能进入，请稍等。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_419B')

    def _loc_412F(): pass

    label('loc_412F')

    ChrTalk(
        0x0012,
        (
            '#4300120934V现在谒见大厅里\n',
            '正在进行一个重要会议。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#4300120935V如果想参观的话，\n',
            '以后还有的是机会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_419B(): pass

    label('loc_419B')

    ChrSetDirection(0x0012, 180, 0)
    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    OP_4B(0x0012, 255)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x000D offset: 0x41C2
@scena.Code('func_0D_41C2')
def func_0D_41C2():
    TalkBegin(0x00FE)

    ChrTalk(
        0x0010,
        (
            '哎呀～\n',
            '感觉就像回到自己的家里一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '王城的警备\n',
            '还是应该由我们正规军来担当。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x421F
@scena.Code('func_0E_421F')
def func_0E_421F():
    TalkBegin(0x00FE)

    ChrTalk(
        0x0011,
        (
            '那位理查德上校\n',
            '竟然是政变的主谋……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '作为王国军一员的我，\n',
            '委实感觉心情难以言表。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x4280
@scena.Code('func_0F_4280')
def func_0F_4280():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.Eval, "OP_42(0x0037)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4300',
    )

    ChrTalk(
        0x0012,
        (
            '#4300120932V现在谒见大厅里\n',
            '正在进行一个重要会议。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#4300120933V非常抱歉，\n',
            '目前还不能进入，请稍等。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_435F')

    def _loc_4300(): pass

    label('loc_4300')

    ChrTalk(
        0x0012,
        (
            '现在谒见大厅里正在进行一个重要会议。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#4300120935V如果想参观的话，\n',
            '以后还有的是机会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_435F(): pass

    label('loc_435F')

    TalkEnd(0x00FE)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

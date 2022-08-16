import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import R2402_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R2402   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'R2402.x'
    header.mapIndex       = 103
    header.bgm            = 20
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
            word_3A         = 103,
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
        ('ED6_DT07/CH00341._CH', 'ED6_DT07/CH00341P._CP'),
        ('ED6_DT07/CH00151._CH', 'ED6_DT07/CH00151P._CP'),
        ('ED6_DT07/CH00152._CH', 'ED6_DT07/CH00152P._CP'),
        ('ED6_DT07/CH00260._CH', 'ED6_DT07/CH00260P._CP'),
        ('ED6_DT07/CH00340._CH', 'ED6_DT07/CH00340P._CP'),
        ('ED6_DT07/CH00341._CH', 'ED6_DT07/CH00341P._CP'),
        ('ED6_DT07/CH00342._CH', 'ED6_DT07/CH00342P._CP'),
        ('ED6_DT07/CH00344._CH', 'ED6_DT07/CH00344P._CP'),
        ('ED6_DT07/CH00260._CH', 'ED6_DT07/CH00260P._CP'),
        ('ED6_DT07/CH00261._CH', 'ED6_DT07/CH00261P._CP'),
        ('ED6_DT07/CH00262._CH', 'ED6_DT07/CH00262P._CP'),
        ('ED6_DT07/CH00264._CH', 'ED6_DT07/CH00264P._CP'),
        ('ED6_DT07/CH00265._CH', 'ED6_DT07/CH00265P._CP'),
        ('ED6_DT09/CH10520._CH', 'ED6_DT09/CH10520P._CP'),
        ('ED6_DT09/CH10521._CH', 'ED6_DT09/CH10521P._CP'),
        ('ED6_DT09/CH10340._CH', 'ED6_DT09/CH10340P._CP'),
        ('ED6_DT09/CH10341._CH', 'ED6_DT09/CH10341P._CP'),
        ('ED6_DT09/CH11040._CH', 'ED6_DT09/CH11040P._CP'),
        ('ED6_DT09/CH11041._CH', 'ED6_DT09/CH11041P._CP'),
        ('ED6_DT09/CH11070._CH', 'ED6_DT09/CH11070P._CP'),
        ('ED6_DT09/CH11071._CH', 'ED6_DT09/CH11071P._CP'),
        ('ED6_DT09/CH11080._CH', 'ED6_DT09/CH11080P._CP'),
        ('ED6_DT09/CH11081._CH', 'ED6_DT09/CH11081P._CP'),
    ]

# id: 0x10001 offset: 0x162
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '黑衣男子',
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
            name                = '黑衣男子',
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
            name                = '阿加特',
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
            name                = '蒙面队长',
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
        ScenaNpcData(
            name                = '卢安方向',
            x                   = -4970,
            z                   = 0,
            y                   = 153310,
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
            name                = '艾尔·雷登关所方向',
            x                   = -930,
            z                   = 0,
            y                   = -3800,
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

# id: 0x10002 offset: 0x242
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = 4300,
            z           = -30,
            y           = 113330,
            word_0C     = 0x00B4,
            word_0E     = 0x000F,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01AB,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -19510,
            z           = 210,
            y           = 102750,
            word_0C     = 0x00B4,
            word_0E     = 0x000D,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01AE,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -2490,
            z           = 110,
            y           = 49730,
            word_0C     = 0x00B4,
            word_0E     = 0x0011,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01AD,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 1490,
            z           = 740,
            y           = 62250,
            word_0C     = 0x00B4,
            word_0E     = 0x0015,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01B3,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x2B2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x2B2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -2060,
            triggerZ            = 0,
            triggerY            = 120820,
            triggerRange        = 1500,
            actorX              = -2060,
            actorZ              = 1500,
            actorY              = 120820,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -30,
            triggerZ            = 240,
            triggerY            = 75790,
            triggerRange        = 1000,
            actorX              = 360,
            actorZ              = 240,
            actorY              = 76370,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2FA
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_31F',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_02_368)

    ExecExpressionWithVar(
        0x1B,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x1A,
        (
            (Expr.PushLong, 0x1B58),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x00000004)

    def _loc_31F(): pass

    label('loc_31F')

    Return()

# id: 0x0001 offset: 0x320
@scena.Code('func_01_320')
def func_01_320():
    OP_16(0x02, 4000, -136000, -52000, 196645)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0098, 3, 0x4C3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_344',
    )

    OP_6F(0x0000, 0)

    Jump('loc_34B')

    def _loc_344(): pass

    label('loc_344')

    OP_6F(0x0000, 60)

    def _loc_34B(): pass

    label('loc_34B')

    OP_25(0x01C5, -3950, 1000, 135110, 10000, 40000, 0x64, 0x00000000)

    Return()

# id: 0x0002 offset: 0x368
@scena.Code('func_02_368')
def func_02_368():
    FadeIn(2000, 0)
    OP_77(0x41, 0x64, 0x82, 0x00, 0x00000000)
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(-4600, 3000, 117500, 0)
    CameraSetDistance(3400, 0)
    OP_67(0, 3300, -10000, 0)
    OP_6C(52000, 0)
    ChrSetPos(0x0008, -4900, 0, 125700, 0)
    ChrSetPos(0x0009, -3900, 0, 125000, 0)
    ChrSetPos(0x000A, 5300, 0, 139100, 0)

    @scena.Lambda('lambda_03EE')
    def lambda_03EE():
        OP_6C(45000, 5000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_03EE)

    CameraMove(-4600, 0, 117500, 5000)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)

    @scena.Lambda('lambda_041E')
    def lambda_041E():
        ChrWalkTo(0x00FE, -5700, 0, 115900, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_041E)

    @scena.Lambda('lambda_0439')
    def lambda_0439():
        ChrWalkTo(0x00FE, -4600, 0, 117500, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0439)

    WaitForThreadExit(0x0009, 0x0001)

    @scena.Lambda('lambda_0459')
    def lambda_0459():
        ChrSetDirection(0x0009, 0, 800)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0459)

    WaitForThreadExit(0x0008, 0x0001)

    @scena.Lambda('lambda_046C')
    def lambda_046C():
        ChrSetDirection(0x0008, 0, 800)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_046C)

    ChrTalk(
        0x0008,
        (
            '呼呼～～～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '这家伙怎么这么缠人呀！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_04A8')
    def lambda_04A8():
        OP_6C(21000, 3000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_04A8)

    CreateThread(0x000A, 0x01, 0x00, func_05_1CCC)

    ChrTalk(
        0x000A,
        (
            '#10A别逃！！（※假定）',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(200)

    CreateThread(0x0008, 0x01, 0x00, func_03_1B45)
    Sleep(200)

    CreateThread(0x0009, 0x01, 0x00, func_04_1C2B)
    OP_6A(0x0009)
    Sleep(600)

    ChrTalk(
        0x0009,
        (
            '#20A带着这么大把剑\n',
            '怎么还能追的上来呀！？',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(2400)

    ChrTalk(
        0x000A,
        (
            '#5P#10A呵，我和你们锻炼的方法可不一样啊。',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(1400)

    ChrTalk(
        0x000A,
        (
            '#5P呀啊～～～～～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x000A, 0x0001)

    @scena.Lambda('lambda_0581')
    def lambda_0581():
        OP_6C(348000, 4000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0581)

    ChrTalk(
        0x0008,
        (
            '唔……\n',
            '怎么都甩不掉吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_05AE')
    def lambda_05AE():
        OP_97(0x0008, -7300, 56400, 40000, 1500, 0x0002)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_05AE)

    ChrTalk(
        0x0009,
        (
            '#2630070008V没办法了，迎击吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_05EE')
    def lambda_05EE():
        OP_97(0x0009, -7300, 56400, -40000, 1500, 0x0002)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_05EE)

    ChrJumpTo(0x000A, -8000, 0, 58200, 500, 15000)
    OP_99(0x000A, 0x07, 0x00, 2000)

    ChrTalk(
        0x000A,
        (
            '#050F你们好像勉勉强强\n',
            '才撑到现在嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050070010V和你们捉迷藏追到你们厌烦，\n',
            '是件很开心的事哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620070011V被你穷追不舍的怨恨\n',
            '一定要你的死来补偿！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2630070012V愚蠢的家伙！\n',
            '2对1你还想赢吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#050F哈哈，\n',
            '当然是想赢的啰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620070014V什么……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#050F打架要全神贯注。\n',
            '在气魄上输了就完了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '在你们夹着尾巴逃跑的时候\n',
            '就注定你们是丧家之犬。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620070017V胡说！\n',
            '你这个游击会的狗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '看我们两个\n',
            '怎么折磨死你！（※假定发生自动战斗）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x000A, 0)
    ChrTurnDirection(0x0009, 0x000A, 0)

    @scena.Lambda('lambda_0806')
    def lambda_0806():
        OP_94(0x01, 0x00FE, 0x0000, 0x000007D0, 0x00002710, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0806)

    @scena.Lambda('lambda_081C')
    def lambda_081C():
        OP_94(0x01, 0x00FE, 0x0000, 0x000007D0, 0x00002710, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_081C)

    Sleep(500)

    Fade(1000)
    TerminateThread(0x000A, 0xFF)
    CameraSetDistance(3000, 0)
    OP_67(0, 8200, -10000, 0)
    OP_6C(45000, 0)
    ChrSetPos(0x0008, -8400, 0, 54200, 0)
    ChrSetPos(0x0009, -9800, 0, 54800, 0)
    ChrSetPos(0x000B, -6700, 0, 58700, 180)
    ChrSetPos(0x000A, -7300, 0, 56400, 0)
    ChrTurnDirection(0x000A, 0x0008, 0)
    ChrTurnDirection(0x0008, 0x000A, 0)
    ChrTurnDirection(0x0009, 0x000A, 0)

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

    ChrSetChipByIndex(0x0008, 7)
    ChrSetChipByIndex(0x0009, 7)

    ChrTalk(
        0x0008,
        (
            '唔～～～～～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '唔……\n',
            '怎么能在这里被抓住………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#050F哼，快点投降\n',
            '给我老实坦白吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050070022V你们是什么人\n',
            '有什么企图……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetRGBAMask(0x000B, 255, 255, 255, 0, 0)
    ChrClearFlags(0x000B, 0x0080)

    ExecExpressionWithVar(
        0x1A,
        (
            (Expr.PushLong, 0x4E20),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(500)
    ChrSetRGBAMask(0x000B, 255, 255, 255, 255, 500)

    ChrTalk(
        0x000B,
        (
            '青年的声音──那样的话会让我十分困扰呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_09BD')
    def lambda_09BD():
        ChrSetDirection(0x000A, 0, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_09BD)

    ChrTalk(
        0x000A,
        (
            '#050F#10A啊！？',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(300)

    ChrSetChipByIndex(0x000A, 1)
    ChrJumpTo(0x000A, -6000, 0, 55000, 1000, 10000)

    @scena.Lambda('lambda_0A01')
    def lambda_0A01():
        ChrTurnDirection(0x000A, 0x000B, 0)
        Yield()

        Jump('lambda_0A01')

    DispatchAsync2(0x000A, 0x0001, lambda_0A01)

    ChrTalk(
        0x000A,
        (
            '#050F你什么时候………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2620070026V啊，队长！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2630070027V您来救我们了吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0141070001V真拿你们没办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0140070029V我正想怎么联络比约定的时候晚，\n',
            '原来你们在这里玩耍呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0AD4')
    def lambda_0AD4():
        OP_99(0x0008, 0x03, 0x00, 500)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0AD4)

    ChrTalk(
        0x0008,
        (
            '#2620070030V实，实在是抱歉！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0B06')
    def lambda_0B06():
        OP_99(0x0009, 0x03, 0x00, 500)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0B06)

    ChrTalk(
        0x0009,
        (
            '#2630070031V有很多人在妨碍我们………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#050F原来如此……\n',
            '你就是首领啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '呵呵，\n',
            '我只不过是现场责任人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0140070034V对于部下的失礼我道歉。\n',
            '能不能在这放过我们一把呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#050F啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050070036V你刚才说什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '我说能不能放过我们一把。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0140070038V我们这里也不打算\n',
            '和游击士协会扯上什么关系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#050F你是傻瓜啊！\n',
            '我怎么可能会放过啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '哎呀哎呀～～～\n',
            '我本来不打算说难听的话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '……你们两个。\n',
            '这里有我来挡住他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0140070042V你们快点去汇合地点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x000A, 0xFF)

    ChrTalk(
        0x0008,
        (
            '#2620070043V是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0008, 5)

    @scena.Lambda('lambda_0D19')
    def lambda_0D19():
        ChrWalkTo(0x00FE, -8900, 0, 43900, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0D19)

    ChrTalk(
        0x0009,
        (
            '#2630070044V太感谢了，队长！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0009, 5)

    @scena.Lambda('lambda_0D5B')
    def lambda_0D5B():
        ChrWalkTo(0x00FE, -8900, 0, 43900, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0D5B)

    ChrSetDirection(0x000A, 225, 800)

    ChrTalk(
        0x000A,
        (
            '#050F想逃吗？喂！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x000B, 9)
    ChrWalkTo(0x000B, -7400, 0, 57000, 8000, 0x00)

    @scena.Lambda('lambda_0DAD')
    def lambda_0DAD():
        CameraMove(-8700, 0, 52500, 1000)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_0DAD)

    @scena.Lambda('lambda_0DC5')
    def lambda_0DC5():
        OP_97(0x00FE, -5100, 53300, -75000, 14000, 0x0001)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0DC5)

    ChrSetChipByIndex(0x000A, 1)
    ChrWalkTo(0x000A, -8300, 0, 53000, 8000, 0x00)
    ChrTurnDirection(0x000A, 0x000B, 0)

    @scena.Lambda('lambda_0E01')
    def lambda_0E01():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_0E01')

    DispatchAsync2(0x000B, 0x0000, lambda_0E01)

    ChrSetChipByIndex(0x000A, 2)

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0x7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x000B, 8)
    OP_94(0x01, 0x000A, 0x00B4, 0x000003E8, 0x00000BB8, 0x00)
    ChrTurnDirection(0x000A, 0x000B, 0)
    ChrTurnDirection(0x000B, 0x000A, 400)

    ChrTalk(
        0x000A,
        (
            '#050F你……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '哼，算了。\n',
            '那样我最多换个猎物抓。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050070049V你身上应该带着\n',
            '很重要的情报吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '呵呵……\n',
            '那么简单就想抓住我吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrJumpTo(0x000B, -10400, 0, 51000, 1000, 8000)

    @scena.Lambda('lambda_0EEC')
    def lambda_0EEC():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_0EEC')

    DispatchAsync2(0x000A, 0x0000, lambda_0EEC)

    ChrTalk(
        0x000A,
        (
            '#050F上等货色！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x000B, 0x0020)
    ChrSetChipByIndex(0x000A, 1)
    ChrSetFlags(0x000B, 0x0004)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)

    @scena.Lambda('lambda_0F2B')
    def lambda_0F2B():
        OP_6C(315000, 1000)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_0F2B)

    OP_94(0x01, 0x000A, 0x00B4, 0x0000012C, 0x000003E8, 0x00)

    ExecExpressionWithValue(
        0x000C,
        0x01,
        (
            (Expr.GetChrWork, 0xB, 0x1),
            (Expr.GetChrWork, 0xA, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x02,
        (
            (Expr.GetChrWork, 0xB, 0x2),
            (Expr.GetChrWork, 0xA, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x03,
        (
            (Expr.GetChrWork, 0xB, 0x3),
            (Expr.GetChrWork, 0xA, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x000C, 1000)
    CreateThread(0x0008, 0x01, 0x00, func_06_1E6F)
    OP_93(0x000A, 0x000B, 1100, 15000, 0x00)

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x000B, 12)
    ChrSetChipByIndex(0x000A, 2)

    @scena.Lambda('lambda_0FBA')
    def lambda_0FBA():
        OP_94(0x01, 0x00FE, 0x0000, 0x000000C8, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0FBA)

    @scena.Lambda('lambda_0FD0')
    def lambda_0FD0():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000000C8, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0FD0)

    OP_9E(0x000B, 30, 0, 300, 5000)
    WaitForThreadExit(0x000B, 0x0001)

    @scena.Lambda('lambda_0FFE')
    def lambda_0FFE():
        OP_94(0x01, 0x00FE, 0x0000, 0x000005DC, 0x00001B58, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0FFE)

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x000B, 8)
    ChrJumpTo(0x000B, -12300, 1300, 50300, 1300, 15000)
    Sleep(100)

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x000B, 10)

    @scena.Lambda('lambda_1050')
    def lambda_1050():
        ChrJumpTo(0x00FE, -10200, 1300, 50800, 1000, 10000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1050)

    @scena.Lambda('lambda_106E')
    def lambda_106E():
        OP_99(0x00FE, 0x00, 0x07, 2000)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_106E)

    Sleep(200)

    @scena.Lambda('lambda_1083')
    def lambda_1083():
        ChrJumpTo(0x00FE, -9200, 0, 53000, 1000, 10000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1083)

    ChrSetChipByIndex(0x000A, 1)
    WaitForThreadExit(0x000B, 0x0001)
    ChrJumpTo(0x000B, -9500, 0, 47800, 1000, 10000)

    @scena.Lambda('lambda_10C2')
    def lambda_10C2():
        OP_99(0x000B, 0x07, 0x0B, 1500)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_10C2)

    CameraSetDistance(2900, 1000)

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x000B, 9)
    ChrJumpTo(0x000B, -8300, 0, 49200, 500, 3000)

    @scena.Lambda('lambda_1102')
    def lambda_1102():
        CameraSetDistance(2500, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1102)

    ChrJumpTo(0x000B, -9900, 0, 50100, 500, 7000)

    @scena.Lambda('lambda_1129')
    def lambda_1129():
        ChrSetDirection(0x000A, 30, 500)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_1129)

    ChrJumpTo(0x000B, -7800, 0, 51800, 500, 10000)

    @scena.Lambda('lambda_114E')
    def lambda_114E():
        ChrJumpTo(0x000B, -9000, 0, 52000, 500, 10000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_114E)

    TerminateThread(0x000A, 0xFF)
    ChrSetDirection(0x000A, 315, 1300)

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x000B, 8)

    @scena.Lambda('lambda_1187')
    def lambda_1187():
        ChrJumpTo(0x00FE, -9500, 500, 51900, 1000, 7000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1187)

    ChrSetDirection(0x000A, 135, 1600)
    Sleep(350)

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x000B, 10)

    @scena.Lambda('lambda_11C1')
    def lambda_11C1():
        OP_99(0x00FE, 0x00, 0x02, 3000)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_11C1)

    ChrTurnDirection(0x000A, 0x000B, 0)
    ChrSetChipByIndex(0x000A, 2)
    OP_99(0x000A, 0x06, 0x07, 1500)

    @scena.Lambda('lambda_11E6')
    def lambda_11E6():
        OP_99(0x000A, 0x05, 0x00, 3000)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_11E6)

    @scena.Lambda('lambda_11F6')
    def lambda_11F6():
        OP_99(0x00FE, 0x02, 0x00, 3000)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_11F6)

    @scena.Lambda('lambda_1206')
    def lambda_1206():
        ChrJumpTo(0x000B, -8900, 0, 56800, 4000, 7000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1206)

    Sleep(200)

    @scena.Lambda('lambda_1229')
    def lambda_1229():
        ChrSetDirection(0x000A, 0, 500)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_1229)

    Sleep(300)

    @scena.Lambda('lambda_123C')
    def lambda_123C():
        OP_99(0x00FE, 0x00, 0x07, 3000)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_123C)

    @scena.Lambda('lambda_124C')
    def lambda_124C():
        ChrJumpTo(0x000A, -8900, 0, 55900, 2000, 10000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_124C)

    @scena.Lambda('lambda_126A')
    def lambda_126A():
        OP_99(0x000A, 0x00, 0x07, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_126A)

    Sleep(450)

    @scena.Lambda('lambda_127F')
    def lambda_127F():
        OP_99(0x00FE, 0x07, 0x0B, 1500)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_127F)

    ChrMoveTo(0x000B, -7350, 0, 56800, 15000, 0x00)
    WaitForThreadExit(0x000A, 0x0001)
    PlayEffect(0x12, 0xFF, 0x00FF, -8900, -1000, 56800, 0, 0, 0, 3000, 3000, 3000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0, 500, 3000, 100)
    ChrJumpTo(0x000B, -5000, 0, 56700, 1300, 5000)
    Sleep(1000)

    @scena.Lambda('lambda_130A')
    def lambda_130A():
        OP_99(0x000A, 0x07, 0x00, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_130A)

    @scena.Lambda('lambda_131A')
    def lambda_131A():
        ChrTurnDirection(0x000A, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_131A)

    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#050F呼，很不错嘛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '用厚重的铁块\n',
            '把激情全都释放出来吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0140070054V你……\n',
            '和我有点相似啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#050F………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050070056V……你说什么……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0141070002V你曾经因为\n',
            '自己的无用而被打败过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0141070003V你有那样的眼神。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#050F………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#050F呵呵呵，不错嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050070061V虽然我和你不相识，\n',
            '但却相当中意你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '我也和你一样，\n',
            '对不中用的男人感到讨厌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0140070063V我们就在这里\n',
            '互相和解怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#050F不要开玩笑！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    LoadEffect(0x00, 'battle\\\\mgaria0.eff')

    @scena.Lambda('lambda_1524')
    def lambda_1524():
        OP_9E(0x00FE, 30, 0, 1000, 5000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1524)

    PlayEffect(0x00, 0x00, 0x000A, 0, 200, 0, 0, 0, 0, 900, 900, 900, 0x00FF, 0, 0, 0, 0)

    ChrTalk(
        0x000A,
        (
            '#050F我没发话听你说，\n',
            '你就给我见风使舵的瞎扯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050070066V你真是个完完全全混淆视听的家伙！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0008, 0xFF)

    ChrTalk(
        0x000B,
        (
            '唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_15E5')
    def lambda_15E5():
        OP_9E(0x00FE, 30, 0, 1000, 5000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_15E5)

    ChrTalk(
        0x000A,
        (
            '#050F噢喔喔喔喔喔！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlayEffect(0x00, 0x01, 0x000B, 0, 200, 0, 0, 0, 0, 900, 900, 900, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_164D')
    def lambda_164D():
        OP_9E(0x00FE, 30, 0, 1000, 5000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_164D)

    ChrTalk(
        0x000B,
        (
            '呀啊啊啊啊啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x000B, 0xFF)
    ChrSetFlags(0x000B, 0x0040)
    ChrSetFlags(0x000A, 0x0040)
    OP_99(0x000A, 0x00, 0x03, 2000)

    @scena.Lambda('lambda_1692')
    def lambda_1692():
        OP_99(0x000A, 0x03, 0x07, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_1692)

    @scena.Lambda('lambda_16A2')
    def lambda_16A2():
        ChrTurnDirection(0x000A, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_16A2)

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x000B, 10)

    @scena.Lambda('lambda_16C0')
    def lambda_16C0():
        OP_99(0x00FE, 0x00, 0x03, 3000)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_16C0)

    @scena.Lambda('lambda_16D0')
    def lambda_16D0():
        ChrWalkTo(0x00FE, -8900, 0, 55900, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_16D0)

    @scena.Lambda('lambda_16EB')
    def lambda_16EB():
        ChrWalkTo(0x00FE, -5000, 0, 56700, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_16EB)

    Sleep(200)

    FadeOut(1, 16777215, -1)
    OP_0D()
    StopEffect(0x00, 0x00)
    StopEffect(0x01, 0x00)
    FadeIn(200, 16777215)

    @scena.Lambda('lambda_1725')
    def lambda_1725():
        OP_6C(0, 3000)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_1725)

    Sleep(3000)

    OP_99(0x000B, 0x03, 0x07, 1500)

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x000B, 11)
    OP_99(0x000B, 0x00, 0x03, 1300)

    ChrTalk(
        0x000B,
        (
            '哼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1768')
    def lambda_1768():
        OP_99(0x000A, 0x07, 0x00, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_1768)

    @scena.Lambda('lambda_1778')
    def lambda_1778():
        ChrTurnDirection(0x000A, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_1778)

    ChrTalk(
        0x000A,
        (
            '#050F呼～～\n',
            '你不止是个嘴上说说的家伙嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050070072V你们注定要\n',
            '被游击会完全盯上的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetRGBAMask(0x000B, 255, 255, 255, 100, 1000)

    ChrTalk(
        0x000A,
        (
            '#050F啊，什么！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetRGBAMask(0x000B, 255, 255, 255, 0, 1000)

    ChrTalk(
        0x000A,
        (
            '#050F这，这是……\n',
            '分身的战技！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '在昏暗树丛的空隙中\n',
            '有隐隐约约的人影漂浮着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('男人的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '《呵呵呵……》',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    TalkSetChrName('男人的声音')

    Talk(
        (
            '《那一击不错呀，\n',
            '不过现在好像很迷茫的样子啊。》',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkSetChrName('男人的声音')

    Talk(
        (
            '《那种迷茫会把刀法弄乱的。》',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ChrTalk(
        0x000A,
        (
            '#050F什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkSetChrName('男人的声音')

    Talk(
        (
            '《要成为修罗的话\n',
            '就必须要有舍弃一切的觉悟。》',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '《对于想活下去的人来说……\n',
            '愤怒和悲伤的事还是忘了比较好。》',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '《就这样吧，再见啰……》',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0141070004V《………………………》',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '树丛间漂浮的人影\n',
            '隐入黑暗消失了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    @scena.Lambda('lambda_1A2A')
    def lambda_1A2A():
        CameraMove(-5100, 1400, 56900, 1100)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_1A2A)

    Sleep(1100)

    ChrTalk(
        0x000A,
        (
            '#050F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '……竟然叫我忘了它……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '这种事……\n',
            '……怎么可能办得到嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1AA3')
    def lambda_1AA3():
        OP_9E(0x00FE, 30, 0, 2000, 5000)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_1AA3)

    @scena.Lambda('lambda_1ABD')
    def lambda_1ABD():
        CameraSetDistance(2400, 2000)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_1ABD)

    @scena.Lambda('lambda_1ACD')
    def lambda_1ACD():
        OP_67(0, 6000, -10000, 2300)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1ACD)

    @scena.Lambda('lambda_1AE5')
    def lambda_1AE5():
        OP_6C(54000, 2000)

        ExitThread()

    DispatchAsync(0x000B, 0x0000, lambda_1AE5)

    OP_99(0x000A, 0x00, 0x03, 2000)
    Fade(1000)

    @scena.Lambda('lambda_1B03')
    def lambda_1B03():
        OP_99(0x000A, 0x03, 0x07, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_1B03)

    ChrTalk(
        0x000A,
        (
            '#6P#20A呜喔喔喔喔喔！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(1500)

    FadeOut(2000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 7, 0x3FF))
    NewScene('ED6_DT01/T2100._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x1B45
@scena.Code('func_03_1B45')
def func_03_1B45():
    ChrSetFlags(0x00FE, 0x0040)
    OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x00000BB8, 0x00)
    ChrWalkTo(0x00FE, -8400, 0, 100000, 10000, 0x00)
    ChrWalkTo(0x00FE, -10700, 0, 86400, 10000, 0x00)

    @scena.Lambda('lambda_1B87')
    def lambda_1B87():
        OP_6C(324000, 3000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1B87)

    @scena.Lambda('lambda_1B97')
    def lambda_1B97():
        OP_67(0, 5200, -10000, 3000)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_1B97)

    @scena.Lambda('lambda_1BAF')
    def lambda_1BAF():
        CameraMove(-8000, 1300, 66400, 2700)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_1BAF)

    MapClearFlags(0x00000001)
    ChrWalkTo(0x00FE, -8000, 0, 72200, 12000, 0x00)
    ChrWalkTo(0x00FE, -6200, 0, 68800, 12000, 0x00)
    ChrWalkTo(0x00FE, -5100, 0, 64500, 13000, 0x00)
    ChrWalkTo(0x00FE, -6200, 0, 58700, 13000, 0x00)
    ChrWalkTo(0x00FE, -9600, 0, 48500, 13000, 0x00)

    Return()

# id: 0x0004 offset: 0x1C2B
@scena.Code('func_04_1C2B')
def func_04_1C2B():
    ChrSetFlags(0x00FE, 0x0040)
    OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x00000BB8, 0x00)
    ChrWalkTo(0x00FE, -8400, 0, 100000, 10000, 0x00)
    ChrWalkTo(0x00FE, -10700, 0, 86400, 11000, 0x00)
    ChrWalkTo(0x00FE, -8000, 0, 72200, 12000, 0x00)
    ChrWalkTo(0x00FE, -6200, 0, 68800, 12000, 0x00)
    ChrWalkTo(0x00FE, -5100, 0, 64500, 12000, 0x00)
    ChrWalkTo(0x00FE, -6200, 0, 58700, 12000, 0x00)
    ChrWalkTo(0x00FE, -8400, 0, 50800, 12000, 0x00)

    Return()

# id: 0x0005 offset: 0x1CCC
@scena.Code('func_05_1CCC')
def func_05_1CCC():
    ChrWalkTo(0x00FE, 0, 0, 133200, 12000, 0x00)
    ChrWalkTo(0x00FE, -8400, 0, 100000, 13000, 0x00)
    ChrWalkTo(0x00FE, -10700, 0, 86400, 14000, 0x00)
    ChrWalkTo(0x00FE, -8000, 0, 72200, 15000, 0x00)
    TerminateThread(0x0008, 0x02)
    TerminateThread(0x0008, 0x03)
    ChrSetFlags(0x00FE, 0x0004)
    ChrJumpTo(0x00FE, -8000, 1500, 66400, 2000, 8000)

    @scena.Lambda('lambda_1D46')
    def lambda_1D46():
        CameraMove(-7300, 0, 56400, 600)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_1D46)

    ChrSetFlags(0x000A, 0x0020)
    ChrSetChipByIndex(0x000A, 2)

    @scena.Lambda('lambda_1D68')
    def lambda_1D68():
        OP_99(0x000A, 0x00, 0x07, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_1D68)

    @scena.Lambda('lambda_1D78')
    def lambda_1D78():
        OP_6C(24000, 800)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_1D78)

    ChrJumpTo(0x00FE, -7300, 0, 56400, 2000, 8000)
    PlayEffect(0x12, 0xFF, 0x00FF, -6800, -1000, 55400, 0, 0, 0, 3000, 3000, 3000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0, 500, 3000, 100)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    ChrTurnDirection(0x0008, 0x000A, 0)
    ChrTurnDirection(0x0009, 0x000A, 0)

    @scena.Lambda('lambda_1DFB')
    def lambda_1DFB():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x00002710, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1DFB)

    @scena.Lambda('lambda_1E11')
    def lambda_1E11():
        ChrJumpTo(0x00FE, -5500, 0, 54700, 500, 6000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1E11)

    WaitForThreadExit(0x0009, 0x0001)
    ChrTurnDirection(0x0009, 0x000A, 400)

    @scena.Lambda('lambda_1E3B')
    def lambda_1E3B():
        OP_94(0x01, 0x00FE, 0x00B4, 0x0000012C, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1E3B)

    WaitForThreadExit(0x0008, 0x0001)

    @scena.Lambda('lambda_1E56')
    def lambda_1E56():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000001F4, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1E56)

    OP_6A(0x0000)
    MapClearFlags(0x00000001)

    Return()

# id: 0x0006 offset: 0x1E6F
@scena.Code('func_06_1E6F')
def func_06_1E6F():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1EC2',
    )

    ExecExpressionWithValue(
        0x000C,
        0x01,
        (
            (Expr.GetChrWork, 0xB, 0x1),
            (Expr.GetChrWork, 0xA, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x02,
        (
            (Expr.GetChrWork, 0xB, 0x2),
            (Expr.GetChrWork, 0xA, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x03,
        (
            (Expr.GetChrWork, 0xB, 0x3),
            (Expr.GetChrWork, 0xA, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x000C, 0)
    Yield()

    Jump('func_06_1E6F')

    def _loc_1EC2(): pass

    label('loc_1EC2')

    Return()

# id: 0x0007 offset: 0x1EC3
@scena.Code('func_07_1EC3')
def func_07_1EC3():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '北　卢安市\n',
            '南　艾尔·雷登　１７５塞尔矩',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0008 offset: 0x1F1D
@scena.Code('func_08_1F1D')
def func_08_1F1D():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0098, 3, 0x4C3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_200D',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x0287, 1)"),
            Expr.Return,
        ),
        'loc_1F93',
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
            '死之刃２',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0098, 3, 0x4C3))

    Jump('loc_200A')

    def _loc_1F93(): pass

    label('loc_1F93')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '死之刃２',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '死之刃２',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0)

    def _loc_200A(): pass

    label('loc_200A')

    Jump('loc_2043')

    def _loc_200D(): pass

    label('loc_200D')

    FadeOut(300, 0, 100)

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
    WaitEffect(0x0F, 0x8C)
    def _loc_2043(): pass

    label('loc_2043')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

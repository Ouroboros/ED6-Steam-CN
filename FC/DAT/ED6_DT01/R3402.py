import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import R3402_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R3402   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'R3402.x'
    header.mapIndex       = 1
    header.bgm            = 30
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
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT07/CH00061._CH', 'ED6_DT07/CH00061P._CP'),
        ('ED6_DT09/CH10130._CH', 'ED6_DT09/CH10130P._CP'),
        ('ED6_DT09/CH10131._CH', 'ED6_DT09/CH10131P._CP'),
        ('ED6_DT09/CH10750._CH', 'ED6_DT09/CH10750P._CP'),
        ('ED6_DT09/CH10751._CH', 'ED6_DT09/CH10751P._CP'),
        ('ED6_DT09/CH10760._CH', 'ED6_DT09/CH10760P._CP'),
        ('ED6_DT09/CH10761._CH', 'ED6_DT09/CH10761P._CP'),
        ('ED6_DT09/CH10770._CH', 'ED6_DT09/CH10770P._CP'),
        ('ED6_DT09/CH10771._CH', 'ED6_DT09/CH10771P._CP'),
    ]

# id: 0x10001 offset: 0xFA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '小女孩',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '艾尔·雷登关所方向',
            x                   = 320150,
            z                   = 0,
            y                   = -37050,
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
            name                = '蔡斯方向',
            x                   = 574100,
            z                   = 0,
            y                   = -54930,
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
            name                = '卡鲁迪亚钟乳洞方向',
            x                   = 400800,
            z                   = -30,
            y                   = 22800,
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

# id: 0x10002 offset: 0x17A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = 367410,
            z           = 10,
            y           = -42400,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01D3,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 389970,
            z           = 10,
            y           = -68740,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01D1,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 425100,
            z           = 0,
            y           = -71190,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01D2,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 467260,
            z           = 0,
            y           = -70580,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01D3,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 497850,
            z           = -20,
            y           = -51510,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01D1,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 506530,
            z           = 0,
            y           = -62560,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01D2,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 526430,
            z           = 30,
            y           = -100000,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01D3,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 402970,
            z           = -20,
            y           = -38570,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01D5,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 422790,
            z           = -10,
            y           = -33010,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01D6,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 407380,
            z           = -20,
            y           = -4320,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01D7,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x292
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 537500,
            y           = -1000,
            z           = -53500,
            range       = 532500,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFF09E8,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000002,
        ),
        ScenaEventData(
            x           = 558400,
            y           = -1000,
            z           = -50000,
            range       = 561500,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFF19EC,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000003,
        ),
    )

# id: 0x10004 offset: 0x2D2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 411920,
            triggerZ            = 0,
            triggerY            = -58300,
            triggerRange        = 1500,
            actorX              = 411920,
            actorZ              = 1500,
            actorY              = -58300,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 423050,
            triggerZ            = -40,
            triggerY            = -33400,
            triggerRange        = 1000,
            actorX              = 423660,
            actorZ              = -40,
            actorY              = -33400,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 499670,
            triggerZ            = -60,
            triggerY            = -114340,
            triggerRange        = 1000,
            actorX              = 499140,
            actorZ              = -60,
            actorY              = -114740,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 514840,
            triggerZ            = -20,
            triggerY            = -121220,
            triggerRange        = 1000,
            actorX              = 514850,
            actorZ              = -20,
            actorY              = -121830,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 551940,
            triggerZ            = 0,
            triggerY            = -50340,
            triggerRange        = 1500,
            actorX              = 551940,
            actorZ              = 1500,
            actorY              = -50340,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x386
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x387
@scena.Code('func_01_387')
def func_01_387():
    OP_16(0x02, 4000, 320000, -179000, 196665)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 2, 0x552)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3AA',
    )

    OP_1B(0x00, 0x00, 0x0004)

    def _loc_3AA(): pass

    label('loc_3AA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B2, 6, 0x596)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3BC',
    )

    OP_6F(0x0011, 0)

    Jump('loc_3C3')

    def _loc_3BC(): pass

    label('loc_3BC')

    OP_6F(0x0011, 60)

    def _loc_3C3(): pass

    label('loc_3C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B2, 7, 0x597)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3D5',
    )

    OP_6F(0x000F, 0)

    Jump('loc_3DC')

    def _loc_3D5(): pass

    label('loc_3D5')

    OP_6F(0x000F, 60)

    def _loc_3DC(): pass

    label('loc_3DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B3, 0, 0x598)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3EE',
    )

    OP_6F(0x0010, 0)

    Jump('loc_3F5')

    def _loc_3EE(): pass

    label('loc_3EE')

    OP_6F(0x0010, 60)

    def _loc_3F5(): pass

    label('loc_3F5')

    Return()

# id: 0x0002 offset: 0x3F6
@scena.Code('func_02_3F6')
def func_02_3F6():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 5, 0x505)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B16',
    )

    SetScenaFlags(ScenaFlag(0x00A0, 5, 0x505))
    EventBegin(0x00)
    Fade(1000)
    CameraMove(541390, 0, -59060, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2840, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 533830, 0, -55500, 135)
    ChrSetPos(0x0102, 534050, -20, -54120, 135)
    ChrSetPos(0x0008, 550900, 0, -55310, 270)
    OP_0D()

    @scena.Lambda('lambda_047F')
    def lambda_047F():
        ChrWalkTo(0x00FE, 539940, 0, -59860, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_047F)

    Sleep(500)

    @scena.Lambda('lambda_049F')
    def lambda_049F():
        ChrWalkTo(0x00FE, 539860, 0, -58530, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_049F)

    Sleep(2000)

    NpcTalk(
        0x0008,
        '声音',
        (
            '#0070070377V#1S#3P呼……呼……\n',
            '必、必须要赶快完成……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0102, 0x0001)
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0102, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrSetDirection(0x0101, 90, 400)
    ChrSetDirection(0x0102, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010070378V#004F咦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070379V#014F……好像有人过来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0008, 0x0080)
    ChrSetChipByIndex(0x0008, 1)
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrWalkTo(0x0008, 541660, 0, -58980, 6000, 0x00)
    ChrSetChipByIndex(0x0008, 0)
    ChrSetDirection(0x0008, 270, 400)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0070070380V#064F#2P啊……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070381V#010F哟，你好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070382V#501F怎么了，急成这个样子？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0070070383V#061F#2P啊，你们好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070384V#060F请问……\n',
            '姐姐你们是沿着这条隧道走来的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070385V#004F嗯，是呢。怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0070070386V#063F#2P那个那个……\n',
            '你们在途中有没有看到熄灭的照明灯？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070387V就是安装在\n',
            '隧道岩壁上的灯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 4, 0x504)),
            Expr.Return,
        ),
        'loc_7E4',
    )

    ChrTalk(
        0x0101,
        (
            '#0010070388V#006F熄灭的照明灯……\n',
            '没看到哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070389V不过，倒是看到过\n',
            '亮度非常强的灯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070390V#010F大概是跨过两条河的地方吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_87F')

    def _loc_7E4(): pass

    label('loc_7E4')

    ChrTalk(
        0x0101,
        (
            '#0010070391V#007F唔……不好意思。\n',
            '我一点也没注意到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070392V#010F虽说没见到过熄灭了的照明灯，\n',
            '不过跨过两条河的地方\n',
            '有一盏照明灯好像不太亮。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_87F(): pass

    label('loc_87F')

    ChrTalk(
        0x0008,
        (
            '#0070070393V#065F#2P就是那个！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070394V果、果然\n',
            '和我想的一样～……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070395V对不起。\n',
            '我得马上走了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrSetChipByIndex(0x0008, 1)

    @scena.Lambda('lambda_090E')
    def lambda_090E():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_090E')

    DispatchAsync2(0x0101, 0x0001, lambda_090E)

    @scena.Lambda('lambda_091F')
    def lambda_091F():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_091F')

    DispatchAsync2(0x0102, 0x0001, lambda_091F)

    @scena.Lambda('lambda_0930')
    def lambda_0930():
        CameraMove(539960, 0, -59290, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0930)

    ChrWalkTo(0x0008, 539420, 0, -57380, 6000, 0x00)
    ChrWalkTo(0x0008, 537140, -20, -57090, 6000, 0x00)
    ChrWalkTo(0x0008, 532960, 20, -53070, 6000, 0x00)
    ChrSetFlags(0x0008, 0x0080)
    Sleep(1000)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)

    ChrTalk(
        0x0102,
        (
            '#0020070396V#010F是蔡斯市的孩子吧，\n',
            '感觉那一身打扮好奇特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020070397V为什么那么慌张呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070398V#007F嗯～\n',
            '我有点担心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010070399V#002F约修亚，\n',
            '我们追过去看看吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020070400V#010F就知道你会这么说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020070401V让一个小女孩独自走到这种地方，\n',
            '的确也是太危险了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020070402V还是追上去比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070403V#006F嗯！\n',
            '我们快追吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    EventEnd(0x00)

    def _loc_B16(): pass

    label('loc_B16')

    Return()

# id: 0x0003 offset: 0xB17
@scena.Code('func_03_B17')
def func_03_B17():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 6, 0x506)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BC9',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B72',
    )

    ChrTalk(
        0x0101,
        (
            '#0010070404V#000F真是在意那个孩子啊………\n',
            '快点追上去看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BAE')

    def _loc_B72(): pass

    label('loc_B72')

    ChrTalk(
        0x0102,
        (
            '#0020070405V#010F如果要追那个孩子的话，\n',
            '最好快一点……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BAE(): pass

    label('loc_BAE')

    ChrMoveToRelative(0x0000, -1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_BC9(): pass

    label('loc_BC9')

    Return()

# id: 0x0004 offset: 0xBCA
@scena.Code('func_04_BCA')
def func_04_BCA():
    EventBegin(0x02)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 5, 0x555)),
            Expr.Return,
        ),
        'loc_D3D',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C32',
    )

    ChrTalk(
        0x0108,
        (
            '#0080081505V#073F哦，这边是相反方向。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080081506V现在要尽快赶回蔡斯。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D3A')

    def _loc_C32(): pass

    label('loc_C32')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C8D',
    )

    ChrTalk(
        0x0102,
        (
            '#0020081507V#012F走错路了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020081508V现在要赶快回蔡斯去才行。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D3A')

    def _loc_C8D(): pass

    label('loc_C8D')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CE5',
    )

    ChrTalk(
        0x0107,
        (
            '#0070081509V#064F啊，这边的路不对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070081510V不赶快回城的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D3A')

    def _loc_CE5(): pass

    label('loc_CE5')

    ChrTurnDirection(0x0102, 0x0000, 400)

    ChrTalk(
        0x0102,
        (
            '#0020081511V#012F应该不是走这边哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020081512V现在要赶快回蔡斯去。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D3A(): pass

    label('loc_D3A')

    Jump('loc_E82')

    def _loc_D3D(): pass

    label('loc_D3D')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_DB2',
    )

    ChrTurnDirection(0x0107, 0x0000, 400)

    ChrTalk(
        0x0107,
        (
            '#0070081499V#064F那个～\n',
            '我们好像走过头了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070081500V钟乳洞应该在刚才来这里的途中。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E82')

    def _loc_DB2(): pass

    label('loc_DB2')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E1E',
    )

    ChrTalk(
        0x0107,
        (
            '#0070081501V#064F啊，\n',
            '我们好像走过头了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070081502V钟乳洞应该在刚才来这里的途中。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E82')

    def _loc_E1E(): pass

    label('loc_E1E')

    ChrTurnDirection(0x0107, 0x0000, 400)

    ChrTalk(
        0x0107,
        (
            '#0070081503V#064F啊，\n',
            '我们好像走过头了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070081504V钟乳洞应该在刚才来这里的途中。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E82(): pass

    label('loc_E82')

    ChrMoveToRelative(0x0000, 1000, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0005 offset: 0xE9E
@scena.Code('func_05_E9E')
def func_05_E9E():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '北　钟乳洞\n',
            '※魔兽很多，危险！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0006 offset: 0xEEE
@scena.Code('func_06_EEE')
def func_06_EEE():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '东　蔡斯市\n',
            '西　艾尔·雷登　４４８塞尔矩',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0007 offset: 0xF48
@scena.Code('func_07_F48')
def func_07_F48():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B2, 6, 0x596)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1038',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0011, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01F6, 1)"),
            Expr.Return,
        ),
        'loc_FBE',
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
            '大回复药',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00B2, 6, 0x596))

    Jump('loc_1035')

    def _loc_FBE(): pass

    label('loc_FBE')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '大回复药',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '大回复药',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0011, 60)
    OP_70(0x0011, 0)

    def _loc_1035(): pass

    label('loc_1035')

    Jump('loc_106E')

    def _loc_1038(): pass

    label('loc_1038')

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
    WaitEffect(0x0F, 0x9F)
    def _loc_106E(): pass

    label('loc_106E')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0x107C
@scena.Code('func_08_107C')
def func_08_107C():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B2, 7, 0x597)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1166',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x000F, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01FD, 1)"),
            Expr.Return,
        ),
        'loc_10F0',
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
            '圣灵药',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00B2, 7, 0x597))

    Jump('loc_1163')

    def _loc_10F0(): pass

    label('loc_10F0')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '圣灵药',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '圣灵药',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x000F, 60)
    OP_70(0x000F, 0)

    def _loc_1163(): pass

    label('loc_1163')

    Jump('loc_119C')

    def _loc_1166(): pass

    label('loc_1166')

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
    WaitEffect(0x0F, 0xA0)
    def _loc_119C(): pass

    label('loc_119C')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0009 offset: 0x11AA
@scena.Code('func_09_11AA')
def func_09_11AA():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B3, 0, 0x598)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_129A',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0010, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01F6, 1)"),
            Expr.Return,
        ),
        'loc_1220',
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
            '大回复药',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00B3, 0, 0x598))

    Jump('loc_1297')

    def _loc_1220(): pass

    label('loc_1220')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '大回复药',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '大回复药',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0010, 60)
    OP_70(0x0010, 0)

    def _loc_1297(): pass

    label('loc_1297')

    Jump('loc_12D0')

    def _loc_129A(): pass

    label('loc_129A')

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
    WaitEffect(0x0F, 0xA1)
    def _loc_12D0(): pass

    label('loc_12D0')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

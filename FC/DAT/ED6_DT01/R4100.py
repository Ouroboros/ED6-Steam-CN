import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import R4100_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R4100   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'R4100.x'
    header.mapIndex       = 1
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
        ('ED6_DT07/CH00040._CH', 'ED6_DT07/CH00040P._CP'),
        ('ED6_DT06/CH20114._CH', 'ED6_DT06/CH20114P._CP'),
        ('ED6_DT07/CH02320._CH', 'ED6_DT07/CH02320P._CP'),
        ('ED6_DT07/CH00341._CH', 'ED6_DT07/CH00341P._CP'),
        ('ED6_DT09/CH10061._CH', 'ED6_DT09/CH10061P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT06/CH20115._CH', 'ED6_DT06/CH20115P._CP'),
        ('ED6_DT07/CH00041._CH', 'ED6_DT07/CH00041P._CP'),
        ('ED6_DT09/CH10060._CH', 'ED6_DT09/CH10060P._CP'),
        ('ED6_DT09/CH10780._CH', 'ED6_DT09/CH10780P._CP'),
        ('ED6_DT09/CH10781._CH', 'ED6_DT09/CH10781P._CP'),
        ('ED6_DT09/CH10790._CH', 'ED6_DT09/CH10790P._CP'),
        ('ED6_DT09/CH10791._CH', 'ED6_DT09/CH10791P._CP'),
        ('ED6_DT09/CH10050._CH', 'ED6_DT09/CH10050P._CP'),
        ('ED6_DT09/CH10051._CH', 'ED6_DT09/CH10051P._CP'),
        ('ED6_DT09/CH10800._CH', 'ED6_DT09/CH10800P._CP'),
        ('ED6_DT09/CH10801._CH', 'ED6_DT09/CH10801P._CP'),
        ('ED6_DT09/CH10810._CH', 'ED6_DT09/CH10810P._CP'),
        ('ED6_DT09/CH10811._CH', 'ED6_DT09/CH10811P._CP'),
        ('ED6_DT09/CH10820._CH', 'ED6_DT09/CH10820P._CP'),
        ('ED6_DT09/CH10821._CH', 'ED6_DT09/CH10821P._CP'),
        ('ED6_DT09/CH11220._CH', 'ED6_DT09/CH11220P._CP'),
        ('ED6_DT09/CH11221._CH', 'ED6_DT09/CH11221P._CP'),
        ('ED6_DT09/CH11230._CH', 'ED6_DT09/CH11230P._CP'),
        ('ED6_DT09/CH11231._CH', 'ED6_DT09/CH11231P._CP'),
    ]

# id: 0x10001 offset: 0x172
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '科洛丝',
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
            name                = '尤莉亚中尉',
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
            name                = '基库',
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
            dword_10            = 3,
            chipIndex           = 3,
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
            dword_10            = 3,
            chipIndex           = 3,
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
            dword_10            = 3,
            chipIndex           = 3,
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
            dword_10            = 4,
            chipIndex           = 4,
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
            dword_10            = 4,
            chipIndex           = 4,
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
            dword_10            = 4,
            chipIndex           = 4,
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
            dword_10            = 4,
            chipIndex           = 4,
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
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '圣海姆门方向',
            x                   = -41770,
            z                   = 0,
            y                   = -5530,
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
            name                = '艾尔贝周游道方向',
            x                   = 137370,
            z                   = -2050,
            y                   = 5100,
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
            name                = '王都格兰赛尔方向',
            x                   = -16930,
            z                   = 0,
            y                   = 111160,
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

# id: 0x10002 offset: 0x3D2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '炽炎草',
            x           = 13640,
            z           = -40,
            y           = -2250,
            word_0C     = 0x0000,
            word_0E     = 0x0009,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0295,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '炽炎草',
            x           = -16650,
            z           = 300,
            y           = 2360,
            word_0C     = 0x0000,
            word_0E     = 0x0009,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0295,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '地狱火爆麻雀',
            x           = 15450,
            z           = -30,
            y           = 56010,
            word_0C     = 0x0000,
            word_0E     = 0x0015,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x029B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '地狱火爆麻雀',
            x           = -13350,
            z           = 110,
            y           = 68880,
            word_0C     = 0x0000,
            word_0E     = 0x0015,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x029B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '沼泽剑齿吸血魔',
            x           = 60840,
            z           = 10,
            y           = 16239,
            word_0C     = 0x0000,
            word_0E     = 0x000D,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0297,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '沼泽剑齿吸血魔',
            x           = 105890,
            z           = -1980,
            y           = 18620,
            word_0C     = 0x0000,
            word_0E     = 0x000D,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0297,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x47A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 16690,
            y           = -1000,
            z           = 31700,
            range       = 36480,
            dword_10    = 0x000003E8,
            dword_14    = 0x00005546,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000003,
        ),
    )

# id: 0x10004 offset: 0x49A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 31170,
            triggerZ            = 0,
            triggerY            = 32450,
            triggerRange        = 1500,
            actorX              = 31170,
            actorZ              = 1700,
            actorY              = 32450,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 29270,
            triggerZ            = 0,
            triggerY            = 21060,
            triggerRange        = 1500,
            actorX              = 29270,
            actorZ              = 1800,
            actorY              = 21060,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 34440,
            triggerZ            = 0,
            triggerY            = 31310,
            triggerRange        = 1500,
            actorX              = 34440,
            actorZ              = 1700,
            actorY              = 31310,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x506
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_522',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x56),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x10000000)
    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_02_547)

    def _loc_522(): pass

    label('loc_522')

    ExecExpressionWithValue(
        0x000A,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0001 offset: 0x534
@scena.Code('func_01_534')
def func_01_534():
    OP_16(0x02, 4000, -88000, -94000, 196667)

    Return()

# id: 0x0002 offset: 0x547
@scena.Code('func_02_547')
def func_02_547():
    MapClearFlags(0x10000000)
    OP_B6(0x00)
    EventBegin(0x00)
    CameraMove(94030, -2000, 13780, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000A, 0x0001)
    ChrSetPos(0x0009, 103460, -2000, 12700, 270)
    ChrSetPos(0x0008, 104570, -2000, 10950, 270)
    ChrSetFlags(0x000A, 0x0004)
    ChrSetPos(0x000A, 96990, 7000, 16000, 90)
    ChrWalkTo(0x0009, 94900, -2000, 13720, 5000, 0x00)
    ChrSetChipByIndex(0x0009, 6)

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetFlags(0x0009, 0x0020)
    ChrSetDirection(0x0009, 135, 800)

    ChrTalk(
        0x0009,
        (
            '#0100100001V#172F这边，科洛丝！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0008, 7)

    @scena.Lambda('lambda_0643')
    def lambda_0643():
        ChrWalkTo(0x00FE, 85060, 40, 13180, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0643)

    Sleep(1000)

    ChrSetDirection(0x0009, 270, 800)
    ChrClearFlags(0x0009, 0x0020)
    ChrSetChipByIndex(0x0009, 1)

    @scena.Lambda('lambda_0674')
    def lambda_0674():
        ChrWalkTo(0x00FE, 84010, 80, 13820, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0674)

    @scena.Lambda('lambda_068F')
    def lambda_068F():
        OP_6C(57000, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_068F)

    @scena.Lambda('lambda_069F')
    def lambda_069F():
        CameraMove(84370, 60, 13300, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_069F)

    WaitForThreadExit(0x0009, 0x0001)

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0009, 6)
    ChrSetFlags(0x0009, 0x0020)
    ChrTurnDirection(0x0009, 0x0008, 800)

    @scena.Lambda('lambda_06D8')
    def lambda_06D8():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_06D8')

    DispatchAsync2(0x0009, 0x0001, lambda_06D8)

    WaitForThreadExit(0x0008, 0x0001)
    ChrSetChipByIndex(0x0008, 0)

    ChrTalk(
        0x0008,
        (
            '#0060100002V#043F呼呼……\n',
            '总算离开周游道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060100003V接下来我们该怎么办？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0100100004V#170F就这样顺着庭园大道去王都吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100100005V我的部下事先做了些伪装的行动，\n',
            '对方的警戒已经变得比较薄弱。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100100006V再说你打扮成这个样子，\n',
            '在到达协会之前应该不会被发现的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0060100007V#042F我知道了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060100008V啊，那么尤莉亚你呢……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0100100009V#170F我在这里挡住敌人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100100010V虽然没办法拖住太长时间，\n',
            '但也应该足够了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0060100011V#043F什么……那怎么可以！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060100012V只有我一个人逃走……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060100013V我也要和尤莉亚一起战斗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0100100014V#176F……人都有各自必须要守护的东西。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100100015V我留下来，\n',
            '是为了自己的信念和责任。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100100016V#170F虽然这样说有点失礼……\n',
            '不过我认为，您只是在感情用事罢了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100100017V请不要忘记，\n',
            '您不只是属于您自己一个人的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0060100018V#049F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060100019V#047F我明白了，尤莉亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060100020V#040F但是，请答应我，\n',
            '绝对不要做出危险的事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060100021V而且，等所有事件平息之后，\n',
            '我们还要好好坐在空中庭园，\n',
            '一起品尝祖母大人沏的红茶哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060100022V#041F我学会做新的点心了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0100100023V#171F我非常期待。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100100024V那么，请赶快走吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100100025V#172F……基库！\n',
            '好好地保护她！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0B9D')
    def lambda_0B9D():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0B9D)

    PlaySE(407, 0x00, 0x64)

    @scena.Lambda('lambda_0BB0')
    def lambda_0BB0():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_0BB0')

    DispatchAsync2(0x0008, 0x0001, lambda_0BB0)

    ChrSetFlags(0x000A, 0x0001)

    @scena.Lambda('lambda_0BC6')
    def lambda_0BC6():
        ChrWalkTo(0x00FE, 83090, 4000, 16270, 11000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0BC6)

    Sleep(200)

    ChrSetDirection(0x0008, 270, 300)
    ChrSetChipByIndex(0x0008, 7)

    @scena.Lambda('lambda_0BF2')
    def lambda_0BF2():
        ChrWalkTo(0x00FE, 68120, 0, 13180, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0BF2)

    @scena.Lambda('lambda_0C0D')
    def lambda_0C0D():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_0C0D')

    DispatchAsync2(0x0009, 0x0001, lambda_0C0D)

    Sleep(100)

    PlaySE(140, 0x00, 0x64)

    @scena.Lambda('lambda_0C28')
    def lambda_0C28():
        CameraMove(82000, 0, 13970, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0C28)

    WaitForThreadExit(0x000A, 0x0001)
    ChrWalkTo(0x000A, 64370, 2000, 16270, 9000, 0x00)
    TerminateThread(0x0009, 0xFF)
    ChrSetPos(0x000E, 108880, -2000, 5290, 0)
    ChrSetPos(0x000F, 110190, -2000, 6430, 0)
    ChrSetPos(0x0010, 111910, -2000, 6760, 0)
    ChrSetPos(0x0011, 109570, -2000, 3930, 0)
    ChrSetPos(0x0012, 110140, -2000, 2710, 0)
    ChrSetPos(0x000B, 111470, -2000, 4930, 0)
    ChrSetPos(0x000C, 112960, -2000, 5790, 0)
    ChrSetPos(0x000D, 112000, -2000, 3870, 0)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    WaitForThreadExit(0x0000, 0x0001)

    ChrTalk(
        0x0009,
        (
            '#0100100026V#176F那些人……\n',
            '也差不多该追上了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x000B, 400)

    @scena.Lambda('lambda_0D51')
    def lambda_0D51():
        OP_6C(314000, 6000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_0D51)

    @scena.Lambda('lambda_0D61')
    def lambda_0D61():
        CameraMove(100950, -2000, 14190, 2900)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0D61)

    Sleep(2000)

    @scena.Lambda('lambda_0D7E')
    def lambda_0D7E():
        ChrMoveToRelative(0x00FE, -8000, 0, 8000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0D7E)

    @scena.Lambda('lambda_0D99')
    def lambda_0D99():
        ChrMoveToRelative(0x00FE, -8000, 0, 8000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0D99)

    @scena.Lambda('lambda_0DB4')
    def lambda_0DB4():
        ChrMoveToRelative(0x00FE, -8000, 0, 8000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_0DB4)

    @scena.Lambda('lambda_0DCF')
    def lambda_0DCF():
        ChrMoveToRelative(0x00FE, -8000, 0, 8000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0DCF)

    @scena.Lambda('lambda_0DEA')
    def lambda_0DEA():
        ChrMoveToRelative(0x00FE, -8000, 0, 8000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_0DEA)

    @scena.Lambda('lambda_0E05')
    def lambda_0E05():
        ChrMoveToRelative(0x00FE, -8000, 0, 8000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_0E05)

    @scena.Lambda('lambda_0E20')
    def lambda_0E20():
        ChrMoveToRelative(0x00FE, -8000, 0, 8000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_0E20)

    @scena.Lambda('lambda_0E3B')
    def lambda_0E3B():
        ChrMoveToRelative(0x00FE, -8000, 0, 8000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_0E3B)

    Sleep(900)

    ChrSetPos(0x0009, 80010, 80, 13820, 0)
    ChrTurnDirection(0x0009, 0x000B, 0)

    @scena.Lambda('lambda_0E73')
    def lambda_0E73():
        OP_67(0, 6770, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_0E73)

    @scena.Lambda('lambda_0E8B')
    def lambda_0E8B():
        CameraSetDistance(3920, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_0E8B)

    @scena.Lambda('lambda_0E9B')
    def lambda_0E9B():
        CameraMove(88700, 0, 13370, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0E9B)

    Sleep(1000)

    @scena.Lambda('lambda_0EB8')
    def lambda_0EB8():
        ChrMoveToRelative(0x00FE, -11000, 0, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0EB8)

    @scena.Lambda('lambda_0ED3')
    def lambda_0ED3():
        ChrMoveToRelative(0x00FE, -11000, 0, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_0ED3)

    Sleep(100)

    @scena.Lambda('lambda_0EF3')
    def lambda_0EF3():
        ChrMoveToRelative(0x00FE, -11000, 0, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_0EF3)

    @scena.Lambda('lambda_0F0E')
    def lambda_0F0E():
        ChrMoveToRelative(0x00FE, -11000, 0, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_0F0E)

    Sleep(100)

    @scena.Lambda('lambda_0F2E')
    def lambda_0F2E():
        ChrMoveToRelative(0x00FE, -10500, 0, 700, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_0F2E)

    Sleep(200)

    @scena.Lambda('lambda_0F4E')
    def lambda_0F4E():
        ChrMoveToRelative(0x00FE, -10000, 0, 0, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0F4E)

    Sleep(100)

    @scena.Lambda('lambda_0F6E')
    def lambda_0F6E():
        ChrMoveToRelative(0x00FE, -10000, 0, 0, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0F6E)

    Sleep(100)

    @scena.Lambda('lambda_0F8E')
    def lambda_0F8E():
        ChrMoveToRelative(0x00FE, -10000, 0, -700, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_0F8E)

    WaitForThreadExit(0x000E, 0x0001)
    ChrSetChipByIndex(0x000E, 8)
    ChrSetChipByIndex(0x000F, 8)

    @scena.Lambda('lambda_0FB8')
    def lambda_0FB8():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_0FB8')

    DispatchAsync2(0x000E, 0x0000, lambda_0FB8)

    @scena.Lambda('lambda_0FCB')
    def lambda_0FCB():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_0FCB')

    DispatchAsync2(0x000F, 0x0000, lambda_0FCB)

    WaitForThreadExit(0x0010, 0x0001)
    ChrSetChipByIndex(0x0010, 8)
    ChrSetChipByIndex(0x0011, 8)

    @scena.Lambda('lambda_0FED')
    def lambda_0FED():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_0FED')

    DispatchAsync2(0x0010, 0x0000, lambda_0FED)

    @scena.Lambda('lambda_1000')
    def lambda_1000():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_1000')

    DispatchAsync2(0x0011, 0x0000, lambda_1000)

    WaitForThreadExit(0x0012, 0x0001)
    ChrSetChipByIndex(0x0012, 8)

    @scena.Lambda('lambda_101D')
    def lambda_101D():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_101D')

    DispatchAsync2(0x0012, 0x0000, lambda_101D)

    WaitForThreadExit(0x000D, 0x0001)

    ChrTalk(
        0x0009,
        (
            '#0100100027V#170F三个人……\n',
            '再加上五只狗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100100028V#176F哼，被小看了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1088')
    def lambda_1088():
        CameraMove(80740, 0, 14730, 1200)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1088)

    CameraSetDistance(3200, 1200)

    ChrTalk(
        0x0009,
        (
            '#0100100029V#176F那个人教我的剑法……\n',
            '是该派上用场的时候了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    PlaySE(504, 0x00, 0x64)

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(800)

    ChrTalk(
        0x0009,
        (
            '#0100100030V#172F王室亲卫队中队长……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100100031V#177F尤莉亚·舒华兹——候教了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    ChrClearFlags(0x0009, 0x0020)
    ChrSetChipByIndex(0x0009, 1)

    @scena.Lambda('lambda_1171')
    def lambda_1171():
        CameraMove(88700, 0, 13370, 2000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_1171)

    @scena.Lambda('lambda_1189')
    def lambda_1189():
        ChrWalkTo(0x00FE, 89660, -1000, 14130, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1189)

    Sleep(200)

    ChrSetChipByIndex(0x000E, 4)

    @scena.Lambda('lambda_11AE')
    def lambda_11AE():
        ChrWalkTo(0x00FE, 76060, 0, 13890, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_11AE)

    Sleep(50)

    ChrSetChipByIndex(0x000F, 4)
    ChrSetChipByIndex(0x0010, 4)

    @scena.Lambda('lambda_11D8')
    def lambda_11D8():
        ChrWalkTo(0x00FE, 76060, 0, 13890, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_11D8)

    @scena.Lambda('lambda_11F3')
    def lambda_11F3():
        ChrWalkTo(0x00FE, 76060, 0, 13890, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_11F3)

    Sleep(100)

    ChrSetChipByIndex(0x0011, 4)

    @scena.Lambda('lambda_1218')
    def lambda_1218():
        ChrWalkTo(0x00FE, 76060, 0, 13890, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_1218)

    Sleep(50)

    ChrSetChipByIndex(0x0012, 4)

    @scena.Lambda('lambda_123D')
    def lambda_123D():
        ChrWalkTo(0x00FE, 76060, 0, 13890, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_123D)

    @scena.Lambda('lambda_1258')
    def lambda_1258():
        ChrWalkTo(0x00FE, 76060, 0, 13890, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1258)

    Sleep(100)

    @scena.Lambda('lambda_1278')
    def lambda_1278():
        ChrWalkTo(0x00FE, 76060, 0, 13890, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1278)

    @scena.Lambda('lambda_1293')
    def lambda_1293():
        ChrWalkTo(0x00FE, 76060, 0, 13890, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1293)

    OP_0D()
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/R4101._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x12BB
@scena.Code('func_03_12BB')
def func_03_12BB():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 6, 0x606)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 7, 0x607)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1DED',
    )

    SetScenaFlags(ScenaFlag(0x00C0, 7, 0x607))
    EventBegin(0x00)
    ChrSetPos(0x0013, 23950, 0, 33710, 180)
    ChrSetPos(0x0014, 22810, 0, 34790, 180)
    ChrSetPos(0x0015, 25010, 0, 34710, 180)
    ChrSetPos(0x0016, 23120, 0, 36550, 180)
    ChrSetPos(0x0017, 24610, 0, 36760, 180)
    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0017, 0x0080)

    ChrTalk(
        0x0013,
        (
            '#4190100541V喂，你们等一下！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0013, 0)
    ChrTurnDirection(0x0102, 0x0013, 0)
    ChrTurnDirection(0x010E, 0x0013, 0)

    @scena.Lambda('lambda_1377')
    def lambda_1377():
        ChrWalkTo(0x00FE, 25510, 0, 30920, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0002, lambda_1377)

    @scena.Lambda('lambda_1392')
    def lambda_1392():
        ChrWalkTo(0x00FE, 24250, 0, 31660, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0002, lambda_1392)

    @scena.Lambda('lambda_13AD')
    def lambda_13AD():
        ChrWalkTo(0x00FE, 24070, 0, 33470, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0016, 0x0002, lambda_13AD)

    @scena.Lambda('lambda_13C8')
    def lambda_13C8():
        ChrWalkTo(0x00FE, 26270, 0, 32509, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0015, 0x0002, lambda_13C8)

    @scena.Lambda('lambda_13E3')
    def lambda_13E3():
        ChrWalkTo(0x00FE, 25800, 0, 33830, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0002, lambda_13E3)

    @scena.Lambda('lambda_13FE')
    def lambda_13FE():
        OP_6C(315000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_13FE)

    CameraMove(23860, 0, 33760, 2000)
    ChrSetPos(0x0101, 25010, 0, 20590, 0)
    ChrSetPos(0x0102, 23710, 0, 20590, 0)
    ChrSetPos(0x010E, 23720, 0, 19280, 0)

    @scena.Lambda('lambda_1452')
    def lambda_1452():
        ChrTurnDirection(0x00FE, 0x010E, 0)
        Yield()

        Jump('lambda_1452')

    DispatchAsync2(0x0013, 0x0001, lambda_1452)

    @scena.Lambda('lambda_1463')
    def lambda_1463():
        ChrTurnDirection(0x00FE, 0x010E, 0)
        Yield()

        Jump('lambda_1463')

    DispatchAsync2(0x0014, 0x0001, lambda_1463)

    @scena.Lambda('lambda_1474')
    def lambda_1474():
        ChrTurnDirection(0x00FE, 0x010E, 0)
        Yield()

        Jump('lambda_1474')

    DispatchAsync2(0x0015, 0x0001, lambda_1474)

    @scena.Lambda('lambda_1485')
    def lambda_1485():
        ChrTurnDirection(0x00FE, 0x010E, 0)
        Yield()

        Jump('lambda_1485')

    DispatchAsync2(0x0016, 0x0001, lambda_1485)

    @scena.Lambda('lambda_1496')
    def lambda_1496():
        ChrTurnDirection(0x00FE, 0x010E, 0)
        Yield()

        Jump('lambda_1496')

    DispatchAsync2(0x0017, 0x0001, lambda_1496)

    @scena.Lambda('lambda_14A7')
    def lambda_14A7():
        CameraMove(25030, 0, 29550, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_14A7)

    @scena.Lambda('lambda_14BF')
    def lambda_14BF():
        ChrWalkTo(0x00FE, 26150, 0, 28040, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_14BF)

    @scena.Lambda('lambda_14DA')
    def lambda_14DA():
        ChrWalkTo(0x00FE, 24890, 0, 27900, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_14DA)

    @scena.Lambda('lambda_14F5')
    def lambda_14F5():
        ChrWalkTo(0x00FE, 25370, 0, 26680, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x010E, 0x0001, lambda_14F5)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010100542V#004F（哎……？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100543V#012F（好像是军队呢……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0013, 0x0002)

    ChrTalk(
        0x0013,
        (
            '#4190100544V你们注意了。\n',
            '艾尔贝离宫禁止参观。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0014, 0x0002)

    ChrTalk(
        0x0013,
        (
            '#4190100545V就在昨天，\n',
            '格兰赛尔的街上不是贴有公告吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100546V#505F？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100547V#010F那个……\n',
            '我们并不是王都的市民。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100548V我们刚刚通过圣海姆门，\n',
            '正在赶往王都格兰赛尔的途中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#2440100549V什么，是旅行者啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#2490100550V在恐怖分子活动的期间\n',
            '沿着有这么多魔兽的街道徒步旅行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#2490100551V你们还真是大胆啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100552V#004F哎……\n',
            '先不说什么恐怖分子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100553V『艾尔贝离宫』是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010E,
        (
            '#0150100554V#130F应该是指坐落在王都东边的\n',
            '那座利贝尔王家的小型宫殿吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150100555V我听说那里作为市民的休憩场所，\n',
            '平常应该是自由开放的啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#4190100556V不好意思，现在那里禁止进入。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#4190100557V因为那里作为恐怖事件的搜查本部，\n',
            '现在暂由军队接管使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100558V#012F搜查本部吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#4190100559V艾尔贝离宫周边的街道\n',
            '虽然没有禁止进入……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#4190100560V不过，为了避免被认为是恐怖分子，\n',
            '我先在此劝诫你们别靠近那里。\n',
            '这也是为了你们自身的安全着想。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0013, 25580, 0, 30180, 3000, 0x00)

    @scena.Lambda('lambda_1942')
    def lambda_1942():
        ChrMoveTo(0x00FE, 23470, -10, 28800, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_1942)

    @scena.Lambda('lambda_195D')
    def lambda_195D():
        ChrMoveTo(0x00FE, 23580, -10, 27820, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_195D)

    @scena.Lambda('lambda_1978')
    def lambda_1978():
        ChrMoveTo(0x00FE, 23510, -10, 26370, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x010E, 0x0002, lambda_1978)

    @scena.Lambda('lambda_1993')
    def lambda_1993():
        ChrTurnDirection(0x00FE, 0x0013, 0)
        Yield()

        Jump('lambda_1993')

    DispatchAsync2(0x0101, 0x0001, lambda_1993)

    @scena.Lambda('lambda_19A4')
    def lambda_19A4():
        ChrTurnDirection(0x00FE, 0x0013, 0)
        Yield()

        Jump('lambda_19A4')

    DispatchAsync2(0x0102, 0x0001, lambda_19A4)

    @scena.Lambda('lambda_19B5')
    def lambda_19B5():
        ChrTurnDirection(0x00FE, 0x0013, 0)
        Yield()

        Jump('lambda_19B5')

    DispatchAsync2(0x010E, 0x0001, lambda_19B5)

    CreateThread(0x0013, 0x01, 0x00, func_04_1DEE)
    CreateThread(0x0016, 0x01, 0x00, func_05_1E1C)
    Sleep(100)

    CreateThread(0x0015, 0x01, 0x00, func_06_1E4A)
    CreateThread(0x0014, 0x01, 0x00, func_05_1E1C)
    Sleep(150)

    CreateThread(0x0017, 0x01, 0x00, func_06_1E4A)
    Sleep(1000)

    CameraMove(23230, -10, 27690, 3000)
    WaitForThreadExit(0x0017, 0x0001)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x010E, 0xFF)

    ChrTalk(
        0x010E,
        (
            '#0150100561V#130F真是严肃的气氛啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150100562V越是说不要靠近，\n',
            '我就越想靠近去看个究竟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x010E, 0x0101, 400)

    ChrTalk(
        0x010E,
        (
            '#0150100563V#130F怎么样，我们稍微绕个路，\n',
            '去那个离宫附近看看吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100564V#007F嗯、嗯……\n',
            '虽然我的好奇心也被勾起来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100565V#015F刚刚才被警告过，\n',
            '我们最好还是别去了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100566V正如那些士兵所说，\n',
            '那里很可能有恐怖分子埋伏着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010100567V#505F哎，但那个不是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100568V情报部把自己做的事\n',
            '嫁祸给亲卫队和游击士的吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020100569V#012F艾丝蒂尔！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x0102,
        (
            '#0020100570V#013F（尽量不要把这件事泄露出去比较好。）\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100571V（要是让一般人知道了，\n',
            '　说不定会被卷进这件事来的。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100572V#002F（说、说的也是……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x010E, 0x0102, 400)

    ChrTalk(
        0x010E,
        (
            '#0150100573V#131F？？？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150100574V情报……什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrTurnDirection(0x0101, 0x010E, 400)

    ChrTalk(
        0x0101,
        (
            '#0010100575V#506F哎，啊，嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100576V不好意思，我什么也没说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100577V#010F就是这样，\n',
            '所以我们还是赶快去王都吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010E,
        (
            '#0150100578V#130F啊……\n',
            '真是遗憾啊，不过也没有办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    def _loc_1DED(): pass

    label('loc_1DED')

    Return()

# id: 0x0004 offset: 0x1DEE
@scena.Code('func_04_1DEE')
def func_04_1DEE():
    ChrWalkTo(0x00FE, 25990, 0, 24860, 3000, 0x00)
    ChrWalkTo(0x00FE, 22000, 0, 16810, 3000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0005 offset: 0x1E1C
@scena.Code('func_05_1E1C')
def func_05_1E1C():
    ChrWalkTo(0x00FE, 24800, 0, 25940, 3000, 0x00)
    ChrWalkTo(0x00FE, 21180, 0, 17950, 3000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0006 offset: 0x1E4A
@scena.Code('func_06_1E4A')
def func_06_1E4A():
    ChrWalkTo(0x00FE, 26580, 0, 24230, 3000, 0x00)
    ChrWalkTo(0x00FE, 23560, 0, 17990, 3000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0007 offset: 0x1E78
@scena.Code('func_07_1E78')
def func_07_1E78():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '北　王都格兰赛尔　１７９塞尔矩',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0008 offset: 0x1EC9
@scena.Code('func_08_1EC9')
def func_08_1EC9():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '南　圣海姆门',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0009 offset: 0x1F08
@scena.Code('func_09_1F08')
def func_09_1F08():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '东　艾尔贝离宫　　２２４塞尔矩',
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

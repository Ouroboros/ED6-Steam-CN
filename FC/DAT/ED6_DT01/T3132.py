import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3132_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3132   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3132.x'
    header.mapIndex       = 1
    header.bgm            = 13
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
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH01350._CH', 'ED6_DT07/CH01350P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH02050._CH', 'ED6_DT07/CH02050P._CP'),
        ('ED6_DT07/CH02070._CH', 'ED6_DT07/CH02070P._CP'),
        ('ED6_DT07/CH01690._CH', 'ED6_DT07/CH01690P._CP'),
        ('ED6_DT07/CH02640._CH', 'ED6_DT07/CH02640P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
    ]

# id: 0x10001 offset: 0xF2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '玛尔奇娜主管',
            x                   = -1700,
            z                   = 0,
            y                   = 2400,
            direction           = 192,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '艾玛',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            name                = '多杰',
            x                   = -44500,
            z                   = 0,
            y                   = 7710,
            direction           = 82,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0016,
        ),
        ScenaNpcData(
            name                = '亚鲁瓦',
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
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            name                = '朵洛希',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            name                = '拉德米拉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '卡雷尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
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
        ScenaNpcData(
            name                = '西加罗',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '艾德尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
    )

# id: 0x10002 offset: 0x212
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x212
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x212
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -1290,
            triggerZ            = 0,
            triggerY            = 550,
            triggerRange        = 400,
            actorX              = -1700,
            actorZ              = 1500,
            actorY              = 2400,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0014,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -4000,
            triggerZ            = 0,
            triggerY            = 4000,
            triggerRange        = 800,
            actorX              = -4000,
            actorZ              = 1000,
            actorY              = 4000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0017,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x25A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_27C',
    )

    ChrSetPos(0x0009, 34920, 0, 91540, 240)
    CreateThread(0x0009, 0x00, 0x00, func_06_5ED)

    Jump('loc_548')

    def _loc_27C(): pass

    label('loc_27C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_2B2',
    )

    ChrSetPos(0x0009, 48750, 0, 137140, 170)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, 770, 0, 2490, 280)
    ChrSetFlags(0x000C, 0x0010)

    Jump('loc_548')

    def _loc_2B2(): pass

    label('loc_2B2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_2D4',
    )

    ChrSetPos(0x0009, 53820, 0, 136060, 76)
    CreateThread(0x0009, 0x00, 0x00, func_04_5A5)

    Jump('loc_548')

    def _loc_2D4(): pass

    label('loc_2D4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_34D',
    )

    ChrSetPos(0x0009, 53820, 0, 136060, 76)
    CreateThread(0x0009, 0x00, 0x00, func_04_5A5)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 35060, 0, 51880, 175)
    CreateThread(0x000B, 0x00, 0x00, func_08_635)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 35130, 0, 91450, 214)
    CreateThread(0x000D, 0x00, 0x00, func_09_659)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, 32420, 0, 95120, 302)
    CreateThread(0x000E, 0x00, 0x00, func_0A_67D)

    Jump('loc_548')

    def _loc_34D(): pass

    label('loc_34D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_38C',
    )

    ChrSetPos(0x0009, 4750, 0, 1370, 265)
    CreateThread(0x0009, 0x00, 0x00, func_05_5C9)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 68050, 0, 56260, 30)
    CreateThread(0x000A, 0x00, 0x00, func_07_611)

    Jump('loc_548')

    def _loc_38C(): pass

    label('loc_38C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_3FE',
    )

    ChrSetPos(0x0009, 5810, 0, 3490, 194)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 68050, 0, 56260, 30)
    CreateThread(0x000A, 0x00, 0x00, func_07_611)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 35130, 0, 91450, 214)
    CreateThread(0x000D, 0x00, 0x00, func_09_659)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, 2990, 0, 1550, 87)
    CreateThread(0x000E, 0x00, 0x00, func_0B_6A1)

    Jump('loc_548')

    def _loc_3FE(): pass

    label('loc_3FE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_453',
    )

    ChrSetPos(0x0009, 64750, 0, 95500, 3)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 35130, 0, 91450, 214)
    CreateThread(0x000D, 0x00, 0x00, func_09_659)
    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, 32420, 0, 95120, 302)
    CreateThread(0x000E, 0x00, 0x00, func_0A_67D)

    Jump('loc_548')

    def _loc_453(): pass

    label('loc_453')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_4BE',
    )

    ChrSetPos(0x0009, 53820, 0, 136060, 76)
    CreateThread(0x0009, 0x00, 0x00, func_04_5A5)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 66540, 0, 59500, 354)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 64450, 0, 95110, 275)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, 68300, 0, 90910, 151)
    CreateThread(0x0010, 0x00, 0x00, func_0C_6C5)

    Jump('loc_548')

    def _loc_4BE(): pass

    label('loc_4BE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_529',
    )

    ChrSetPos(0x0009, 53820, 0, 136060, 76)
    CreateThread(0x0009, 0x00, 0x00, func_04_5A5)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 66540, 0, 59500, 354)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 64450, 0, 95110, 275)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, 68300, 0, 90910, 151)
    CreateThread(0x0010, 0x00, 0x00, func_0C_6C5)

    Jump('loc_548')

    def _loc_529(): pass

    label('loc_529')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_548',
    )

    ChrSetPos(0x0009, 35090, 0, 51720, 32)
    CreateThread(0x0009, 0x00, 0x00, func_03_581)

    def _loc_548(): pass

    label('loc_548')

    Return()

# id: 0x0001 offset: 0x549
@scena.Code('func_01_549')
def func_01_549():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 2, 0x53A)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 0, 0x558)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_561',
    )

    OP_B1('t3132_y')

    Jump('loc_56A')

    def _loc_561(): pass

    label('loc_561')

    OP_B1('t3132_n')

    def _loc_56A(): pass

    label('loc_56A')

    Return()

# id: 0x0002 offset: 0x56B
@scena.Code('func_02_56B')
def func_02_56B():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_580',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_56B')

    def _loc_580(): pass

    label('loc_580')

    Return()

# id: 0x0003 offset: 0x581
@scena.Code('func_03_581')
def func_03_581():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5A4',
    )

    OP_8D(0x00FE, 33590, 49640, 36490, 53470, 3000)

    Jump('func_03_581')

    def _loc_5A4(): pass

    label('loc_5A4')

    Return()

# id: 0x0004 offset: 0x5A5
@scena.Code('func_04_5A5')
def func_04_5A5():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5C8',
    )

    OP_8D(0x00FE, 44740, 134200, 62330, 137000, 3000)

    Jump('func_04_5A5')

    def _loc_5C8(): pass

    label('loc_5C8')

    Return()

# id: 0x0005 offset: 0x5C9
@scena.Code('func_05_5C9')
def func_05_5C9():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5EC',
    )

    OP_8D(0x00FE, 1650, -310, 7710, 1910, 3000)

    Jump('func_05_5C9')

    def _loc_5EC(): pass

    label('loc_5EC')

    Return()

# id: 0x0006 offset: 0x5ED
@scena.Code('func_06_5ED')
def func_06_5ED():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_610',
    )

    OP_8D(0x00FE, 4059, 88790, 36250, 93240, 3000)

    Jump('func_06_5ED')

    def _loc_610(): pass

    label('loc_610')

    Return()

# id: 0x0007 offset: 0x611
@scena.Code('func_07_611')
def func_07_611():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_634',
    )

    OP_8D(0x00FE, 66680, 54350, 69610, 58920, 2000)

    Jump('func_07_611')

    def _loc_634(): pass

    label('loc_634')

    Return()

# id: 0x0008 offset: 0x635
@scena.Code('func_08_635')
def func_08_635():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_658',
    )

    OP_8D(0x00FE, 34200, 49490, 36490, 53440, 2000)

    Jump('func_08_635')

    def _loc_658(): pass

    label('loc_658')

    Return()

# id: 0x0009 offset: 0x659
@scena.Code('func_09_659')
def func_09_659():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_67C',
    )

    OP_8D(0x00FE, 33860, 89530, 36420, 93590, 1500)

    Jump('func_09_659')

    def _loc_67C(): pass

    label('loc_67C')

    Return()

# id: 0x000A offset: 0x67D
@scena.Code('func_0A_67D')
def func_0A_67D():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_6A0',
    )

    OP_8D(0x00FE, 31570, 94690, 33720, 95490, 3000)

    Jump('func_0A_67D')

    def _loc_6A0(): pass

    label('loc_6A0')

    Return()

# id: 0x000B offset: 0x6A1
@scena.Code('func_0B_6A1')
def func_0B_6A1():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_6C4',
    )

    OP_8D(0x00FE, 1090, -290, 4450, 2920, 3000)

    Jump('func_0B_6A1')

    def _loc_6C4(): pass

    label('loc_6C4')

    Return()

# id: 0x000C offset: 0x6C5
@scena.Code('func_0C_6C5')
def func_0C_6C5():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_6E8',
    )

    OP_8D(0x00FE, 67180, 88480, 69500, 93510, 1500)

    Jump('func_0C_6C5')

    def _loc_6E8(): pass

    label('loc_6E8')

    Return()

# id: 0x000D offset: 0x6E9
@scena.Code('func_0D_6E9')
def func_0D_6E9():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_775',
    )

    ChrTalk(
        0x00FE,
        (
            '今天我们要去\n',
            '附近有名的温泉胜地。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在回格兰赛尔之前，\n',
            '我想留在那里一段时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，这样我老婆\n',
            '也暂时不会买东西了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8B6')

    def _loc_775(): pass

    label('loc_775')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_8B6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_805',
    )

    ChrTalk(
        0x00FE,
        (
            '今天我们要去\n',
            '附近有名的温泉胜地。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在回格兰赛尔之前，\n',
            '我想留在那里一段时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，这样我老婆\n',
            '也暂时不会买东西了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8B6')

    def _loc_805(): pass

    label('loc_805')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '昨天晚上发生什么事了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '当时我很快就睡着了，\n',
            '完全不知道发生了什么事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……哎呀！\n',
            '不能再说了，\n',
            '必须快点准备行李才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天我们要去\n',
            '附近有名的温泉胜地。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8B6(): pass

    label('loc_8B6')

    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x8BA
@scena.Code('func_0E_8BA')
def func_0E_8BA():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_929',
    )

    ChrTalk(
        0x00FE,
        (
            '那个温泉小村\n',
            '听说相当不错啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像还有很名贵的特产，\n',
            '看来我可以好好享受一下购物乐趣了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_988')

    def _loc_929(): pass

    label('loc_929')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_988',
    )

    ChrTalk(
        0x00FE,
        (
            '我刚想要睡觉的时候，\n',
            '灯忽然全都灭掉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可笑的是\n',
            '我还把丈夫的床错搞成自己的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_988(): pass

    label('loc_988')

    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x98C
@scena.Code('func_0F_98C')
def func_0F_98C():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_D65',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0004, 0x00, 0x10)"),
            (Expr.TestScenaFlags, ScenaFlag(0x00B0, 3, 0x583)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_CA4',
    )

    SetScenaFlags(ScenaFlag(0x00B0, 3, 0x583))
    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哟，好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#014F……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#010F啊，我还以为是谁呢……\n',
            '真的是好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F嗯？是谁啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F呵呵，就是在洛连特\n',
            '寻找结晶回路碎片的那个孩子啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我们之前不是\n',
            '接受过他的委托去找那碎片吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '你要回卡尔瓦德共和国去了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '嗯，时间差不多了。\n',
            '不过在那之前要去中央工房。\n',
            '因为在格兰赛尔卖了些东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '老妈说要用那些米拉\n',
            '买些导力器回去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿，老妈也开始知道\n',
            '什么东西才是有价值的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#506F怎么样都好啦。\n',
            '你还是老样子，那么自大傲慢呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '是吗？我觉得自己 \n',
            '只不过是说了理所当然的话而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '尽管如此……\n',
            '那些巨大的飞艇\n',
            '真的是在这个城市里面建造的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天，我在中央工房里\n',
            '听到那些技师在商量\n',
            '关于新型导力引擎的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……了不起啊。\n',
            '能够建造出可以在天空中翱翔的飞艇。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是了不起啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D62')

    def _loc_CA4(): pass

    label('loc_CA4')

    ChrTalk(
        0x00FE,
        (
            '那些巨大的飞艇\n',
            '真的是在这个城市里面建造的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天，我在中央工房里\n',
            '听到那些技师在商量\n',
            '关于导力引擎的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……了不起啊。\n',
            '能够建造出可以在天空中翱翔的飞艇。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是了不起啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D62(): pass

    label('loc_D62')

    Jump('loc_141F')

    def _loc_D65(): pass

    label('loc_D65')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_1113',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0004, 0x00, 0x10)"),
            (Expr.TestScenaFlags, ScenaFlag(0x00B0, 3, 0x583)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_10C1',
    )

    SetScenaFlags(ScenaFlag(0x00B0, 3, 0x583))
    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哟，好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#014F……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#010F啊，我还以为是谁呢……\n',
            '真的是好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F嗯？是谁啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F呵呵，就是在洛连特\n',
            '寻找结晶回路碎片的那个孩子啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我们之前不是\n',
            '接受过他的委托去找那碎片吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '你要回卡尔瓦德共和国去了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '不，在那之前要先去中央工房。\n',
            '因为在格兰赛尔卖了些东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '老妈说要用那些米拉\n',
            '买些导力器回去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿，老妈也开始知道\n',
            '什么东西才是有价值的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#506F怎么样都好啦。\n',
            '你还是老样子，那么自大傲慢呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '是吗？我觉得自己 \n',
            '只不过是说了理所当然的话而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '尽管如此……\n',
            '从刚才开始外面就一直很吵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '出什么事了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F我们现在就去确认情况。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '因为可能会有危险，\n',
            '你千万不可以出去哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '你凭什么不让我出去啊。\n',
            '我又不是小孩子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#007F啊，\n',
            '你还真的挺自大的嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#002F哦，\n',
            '现在可不是说这种话的场合。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#012F嗯，我们快点去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1110')

    def _loc_10C1(): pass

    label('loc_10C1')

    ChrTalk(
        0x00FE,
        (
            '从刚才开始外面就一直很吵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果弄清楚是什么事情，\n',
            '记得回来告诉我哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1110(): pass

    label('loc_1110')

    Jump('loc_141F')

    def _loc_1113(): pass

    label('loc_1113')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_141F',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0004, 0x00, 0x10)"),
            (Expr.TestScenaFlags, ScenaFlag(0x00B0, 3, 0x583)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_13AD',
    )

    SetScenaFlags(ScenaFlag(0x00B0, 3, 0x583))
    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哟，好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#014F……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#010F啊，我还以为是谁呢……\n',
            '真的是好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F嗯？是谁啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F呵呵，就是在洛连特\n',
            '寻找结晶回路碎片的那个孩子啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我们之前不是\n',
            '接受过他的委托去找那碎片吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '你要回卡尔瓦德共和国去了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '不，在那之前要先去中央工房。\n',
            '因为在格兰赛尔卖了些东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '老妈说要用那些米拉\n',
            '买些导力器回去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿，老妈也开始知道\n',
            '什么东西才是有价值的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#506F怎么样都好啦。\n',
            '你还是老样子，那么自大傲慢呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '是吗？我觉得自己 \n',
            '只不过是说了理所当然的话而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '尽管如此……\n',
            '这个城市真不得了啊。\n',
            '到处都装着导力装置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且飞船也是\n',
            '在这个城市里建造的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_141F')

    def _loc_13AD(): pass

    label('loc_13AD')

    ChrTalk(
        0x00FE,
        (
            '这个城市，好厉害啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有可以活动的楼梯，\n',
            '钟表也是导力驱动的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且飞船也是\n',
            '在这个城市里建造的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_141F(): pass

    label('loc_141F')

    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x1423
@scena.Code('func_10_1423')
def func_10_1423():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_1600',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_14FF',
    )

    ChrTalk(
        0x00FE,
        (
            '今天，我去工房四处转了转，\n',
            '订购了一些导力相机。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明天把货品领回来，商谈就搞定了。\n',
            '这样就可以回国了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是我家的卡雷尔\n',
            '也能正正经经地\n',
            '给我帮忙到最后就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……唉，不能太期待了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15FD')

    def _loc_14FF(): pass

    label('loc_14FF')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '今天，我去工房四处转了转，\n',
            '订购了一些导力相机。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '操作简单的相机，\n',
            '在共和国也一定很好卖的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明天把货品领回来，商谈就搞定了。\n',
            '这样就可以回国了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，要是我家的卡雷尔\n',
            '能正正经经地\n',
            '给我帮忙到最后就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……唉，不能太过期待了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15FD(): pass

    label('loc_15FD')

    Jump('loc_1732')

    def _loc_1600(): pass

    label('loc_1600')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_16A5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_1659',
    )

    ChrTalk(
        0x00FE,
        (
            '……哎呀，\n',
            '卡雷尔还是不在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，\n',
            '那个孩子一点都不安分呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16A2')

    def _loc_1659(): pass

    label('loc_1659')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '呼啊啊啊……\n',
            '啊～好困。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，时间还早呢。\n',
            '还是下午去工房吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_16A2(): pass

    label('loc_16A2')

    Jump('loc_1732')

    def _loc_16A5(): pass

    label('loc_16A5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_1732',
    )

    ChrTalk(
        0x00FE,
        (
            '这个房间非常宽敞， \n',
            '让人感到十分舒适呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不愧是高级房间，\n',
            '花钱多一些也是值得的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那就好好休息吧。\n',
            '商谈从明天才开始呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1732(): pass

    label('loc_1732')

    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0x1736
@scena.Code('func_11_1736')
def func_11_1736():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_1835',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_179C',
    )

    ChrTalk(
        0x000C,
        (
            '#0280091652V#151F那个～不好意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280091653V可以借用一下\n',
            '这里的通信器吗～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1835')

    def _loc_179C(): pass

    label('loc_179C')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x000C,
        (
            '#0280091649V#150F奈尔前辈要我\n',
            '拍的照片已经拍好了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280091650V现在还是马上到\n',
            '下一个取材地点去吧～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280091651V啊，\n',
            '还是再联络总编问一下吧～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1835(): pass

    label('loc_1835')

    TalkEnd(0x00FE)

    Return()

# id: 0x0012 offset: 0x1839
@scena.Code('func_12_1839')
def func_12_1839():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_1ACC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_18AD',
    )

    ChrTalk(
        0x010E,
        (
            '#0150091673V#130F这个时间还在工作，\n',
            '做游击士也很辛苦啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150091674V那么，你们要加油哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1ACC')

    def _loc_18AD(): pass

    label('loc_18AD')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x010E,
        (
            '#0150091662V#130F哎呀……\n',
            '艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150091663V今天白天你们辛苦了吧。\n',
            '掌握到什么线索了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091664V#000F嗯……\n',
            '说到线索的话确实有一些吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010091665V……对不起，教授。\n',
            '现在有很急的事情要做呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010E,
        (
            '#0150091666V#130F哦，是吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150091667V竟然工作到这么晚……\n',
            '做游击士也很辛苦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091668V#000F今天比较特别嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091669V#010F那么，不好意思，\n',
            '我们就先告辞了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020091670V能向我们提供情报，\n',
            '真是多谢您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010E,
        (
            '#0150091671V#130F我能帮忙的事情\n',
            '也就只有这些了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150091672V那么，你们要加油哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1ACC(): pass

    label('loc_1ACC')

    TalkEnd(0x00FE)

    Return()

# id: 0x0013 offset: 0x1AD0
@scena.Code('func_13_1AD0')
def func_13_1AD0():
    TalkBegin(0x0008)
    FadeOut(300, 0, 100)

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
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '休息\n'),
            TXT(0x02, '离开\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1B2C',
    )

    OP_0D()
    OP_A9(0x3F)
    OP_56(0x00)
    TalkEnd(0x0008)

    Return()

    def _loc_1B2C(): pass

    label('loc_1B2C')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B3D',
    )

    TalkEnd(0x0008)

    Return()

    def _loc_1B3D(): pass

    label('loc_1B3D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_1C4D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1BDD',
    )

    ChrTalk(
        0x0008,
        (
            '今天也要和\n',
            '艾玛好好谈谈，\n',
            '让她努力工作才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '在下一批客人来之前，\n',
            '必须将全部客房\n',
            '收拾得一尘不染。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '经营酒店\n',
            '就是在和时间打仗呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C4A')

    def _loc_1BDD(): pass

    label('loc_1BDD')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '欢迎光临。\n',
            '这里是蔡恩拉德酒店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '现在随时可以给您\n',
            '准备您喜欢的房间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '请务必来我们这里住宿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C4A(): pass

    label('loc_1C4A')

    Jump('loc_231E')

    def _loc_1C4D(): pass

    label('loc_1C4D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_1D29',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1CB6',
    )

    ChrTalk(
        0x0008,
        (
            '唉，\n',
            '果然蔡斯这地方的孩子就是麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '……不过其实我自己\n',
            '也是个纯粹的蔡斯人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D26')

    def _loc_1CB6(): pass

    label('loc_1CB6')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '唉，\n',
            '还好我留意了艾玛的行动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '她似乎误解了\n',
            '我叮嘱她的话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '唉，\n',
            '果然蔡斯这地方的孩子就是麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D26(): pass

    label('loc_1D26')

    Jump('loc_231E')

    def _loc_1D29(): pass

    label('loc_1D29')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_1E5B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1DAD',
    )

    ChrTalk(
        0x0008,
        (
            '唉，真是的。\n',
            '提到艾玛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '她为什么要用那么大的声音\n',
            '和别人打招呼呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '要是吓走了客人，\n',
            '那该怎么办啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E58')

    def _loc_1DAD(): pass

    label('loc_1DAD')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '唉，真是的，\n',
            '我都那样提醒她了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '她为什么要用那么大的声音\n',
            '和别人打招呼呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '虽说我知道\n',
            '她作为新来的干活很卖力……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '可要是吓走了客人，\n',
            '那该怎么办啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E58(): pass

    label('loc_1E58')

    Jump('loc_231E')

    def _loc_1E5B(): pass

    label('loc_1E5B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_1E9A',
    )

    ChrTalk(
        0x0008,
        (
            '啊，欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '工作到这么晚，\n',
            '真是辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_231E')

    def _loc_1E9A(): pass

    label('loc_1E9A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_1F7A',
    )

    ChrTalk(
        0x0008,
        (
            '没想到工房竟然发生了袭击事件……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '虽然感到很震惊，\n',
            '不过连我们酒店从业员都表现出动摇的话，\n',
            '那么就会在客人中间散布不安的情绪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '一定要像平常那样\n',
            '为各位客人提供服务……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '那样客人们应该\n',
            '也会感到安心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_231E')

    def _loc_1F7A(): pass

    label('loc_1F7A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_1FBB',
    )

    ChrTalk(
        0x0008,
        (
            '从刚才开始，\n',
            '工房那边就很吵闹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '难道出事了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_231E')

    def _loc_1FBB(): pass

    label('loc_1FBB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_213C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_205E',
    )

    ChrTalk(
        0x0008,
        (
            '对蔡斯人来说\n',
            '就算被要求若无其事的服务，\n',
            '也是很难理解的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '总之，\n',
            '认真努力工作就是蔡斯人的本色。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '……当然如您所知，\n',
            '也有不少例外。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2139')

    def _loc_205E(): pass

    label('loc_205E')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '接待客人的时候，\n',
            '为了不让客人紧张，\n',
            '表现得镇定自如也是很重要的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '就算是向蔡斯人要求\n',
            '那种不加伪装自然的服务，\n',
            '也是很难理解的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '总之，\n',
            '认真努力工作就是蔡斯人的本色。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '无论如何\n',
            '也还是要加把劲呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2139(): pass

    label('loc_2139')

    Jump('loc_231E')

    def _loc_213C(): pass

    label('loc_213C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_21DB',
    )

    ChrTalk(
        0x0008,
        (
            '呼，\n',
            '昨晚真是给客人添麻烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不过总算是万幸，\n',
            '没用多长时间导力就恢复供应了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '没有导力灯的夜晚，\n',
            '自从导力革命后好像还是第一次。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_231E')

    def _loc_21DB(): pass

    label('loc_21DB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_22B4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_2235',
    )

    ChrTalk(
        0x0008,
        (
            '顺便提一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我们还是第一家实现\n',
            '全部由导力提供照明的酒店哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_22B1')

    def _loc_2235(): pass

    label('loc_2235')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '欢迎光临。\n',
            '这里是蔡恩拉德酒店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '本酒店是王国中仅有的\n',
            '几家历史悠久的酒店之一。\n',
            '而我已经是本酒店第六代负责人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_22B1(): pass

    label('loc_22B1')

    Jump('loc_231E')

    def _loc_22B4(): pass

    label('loc_22B4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_231E',
    )

    ChrTalk(
        0x0008,
        (
            '欢迎光临。\n',
            '这里是蔡恩拉德酒店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '本酒店会为您\n',
            '提供尽心周到的服务。\n',
            '我想一定能令您满意的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_231E(): pass

    label('loc_231E')

    TalkEnd(0x0008)

    Return()

# id: 0x0014 offset: 0x2322
@scena.Code('func_14_2322')
def func_14_2322():
    Call(0, 0x0013)

    Return()

# id: 0x0015 offset: 0x2327
@scena.Code('func_15_2327')
def func_15_2327():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_23FA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_2383',
    )

    ChrTalk(
        0x00FE,
        (
            '好的，那就……\n',
            '首先打扫这房间！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，艾玛。\n',
            '要拿出气势来哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23F7')

    def _loc_2383(): pass

    label('loc_2383')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '今天早上\n',
            '主管这么对我说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在没有客人的地方努力\n',
            '是可以的哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，今天到现在为止\n',
            '我都很努力哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_23F7(): pass

    label('loc_23F7')

    Jump('loc_2925')

    def _loc_23FA(): pass

    label('loc_23FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_2509',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_2463',
    )

    ChrTalk(
        0x00FE,
        (
            '我努力干活的样子被主管看见，\n',
            '又让她生气了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么接下来\n',
            '我就不这么努力干活了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2506')

    def _loc_2463(): pass

    label('loc_2463')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '好的，那就……\n',
            '这个房间已经打扫完了，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '剩下的只有隔壁了。\n',
            '那么，接下来也要加油……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……哦。\n',
            '不能太努力了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那，就马虎点。\n',
            '马虎点……就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2506(): pass

    label('loc_2506')

    Jump('loc_2925')

    def _loc_2509(): pass

    label('loc_2509')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_25EE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_257B',
    )

    ChrTalk(
        0x00FE,
        (
            '主管训斥我，\n',
            '说我『努力过度』什么的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我是个新来的，\n',
            '工作努力应该是\n',
            '理所当然的啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25EB')

    def _loc_257B(): pass

    label('loc_257B')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '主管训斥我，\n',
            '说我『努力过度』什么的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我是个新来的，\n',
            '工作努力应该是\n',
            '理所当然的啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_25EB(): pass

    label('loc_25EB')

    Jump('loc_2925')

    def _loc_25EE(): pass

    label('loc_25EE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_2665',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才，\n',
            '有个学者打扮的客人告诉我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没想到中央工房\n',
            '竟然被袭击了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '吓了一跳吧？\n',
            '我也很吃惊呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2925')

    def _loc_2665(): pass

    label('loc_2665')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_2749',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_26D8',
    )

    ChrTalk(
        0x00FE,
        (
            '唔～\n',
            '总觉得城里的气氛有点奇怪……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我问过主管，\n',
            '她也不告诉我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊，我有些在意呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2746')

    def _loc_26D8(): pass

    label('loc_26D8')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '唔～\n',
            '总觉得城里的气氛有点奇怪……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我问过主管，\n',
            '她也不告诉我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '总不能向客人打听吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2746(): pass

    label('loc_2746')

    Jump('loc_2925')

    def _loc_2749(): pass

    label('loc_2749')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_2781',
    )

    ChrTalk(
        0x00FE,
        (
            '欢迎光临～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '欢迎来到蔡恩拉德酒店！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2925')

    def _loc_2781(): pass

    label('loc_2781')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_27C8',
    )

    ChrTalk(
        0x00FE,
        (
            '好，\n',
            '这间房间也打扫干净了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那我就去打扫下一间吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2925')

    def _loc_27C8(): pass

    label('loc_27C8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_28CE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_2824',
    )

    ChrTalk(
        0x00FE,
        (
            '刚、刚才真的是失礼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '想要住宿的话，\n',
            '请一定要来我们酒店哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28CB')

    def _loc_2824(): pass

    label('loc_2824')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '你、你们好！\n',
            '我、我是新人艾玛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天我也会\n',
            '更加用心拼命努力的。\n',
            '希望你们也能在酒店住得舒服哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们看上去好像不是\n',
            '在这里住宿的客人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_28CB(): pass

    label('loc_28CB')

    Jump('loc_2925')

    def _loc_28CE(): pass

    label('loc_28CE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_2925',
    )

    ChrTalk(
        0x00FE,
        (
            '床单换好后，\n',
            '接下来要清点家具用品……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '工作量像山一样多，\n',
            '加油吧艾玛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2925(): pass

    label('loc_2925')

    TalkEnd(0x00FE)

    Return()

# id: 0x0016 offset: 0x2929
@scena.Code('func_16_2929')
def func_16_2929():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_29A1',
    )

    ChrTalk(
        0x00FE,
        (
            '似、似乎\n',
            '发生什么事情了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本来还打算\n',
            '一会儿去飞艇坪参观一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '或许改个日子\n',
            '会比较好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C67')

    def _loc_29A1(): pass

    label('loc_29A1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_2B13',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_2A10',
    )

    ChrTalk(
        0x00FE,
        (
            '毕竟是做大买卖的人，\n',
            '器量就是不一样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我要以那样的商人为目标，\n',
            '今后也要好好努力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B10')

    def _loc_2A10(): pass

    label('loc_2A10')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '昨天，在工房遇到了麻烦，\n',
            '幸好一位名叫鲁特尔的人帮助了我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '多亏了他，\n',
            '才能顺利地采购齐制暖用的导力器。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '据说鲁特尔是\n',
            '从事飞艇中介行业的商人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '毕竟是做大买卖的人，\n',
            '器量就是不一样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他利落地指挥着店员，\n',
            '很快就帮我找到目标商品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B10(): pass

    label('loc_2B10')

    Jump('loc_2C67')

    def _loc_2B13(): pass

    label('loc_2B13')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_2C67',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_2B7F',
    )

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '昨天晚上酒店的照明\n',
            '停了一会儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个导力灯，\n',
            '是不是寿命就要到了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C67')

    def _loc_2B7F(): pass

    label('loc_2B7F')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '不愧是利贝尔，真厉害。\n',
            '连照明都已经全部导力化了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们的村子位于\n',
            '气候严酷的共和国高原上，\n',
            '导力器还没有普及呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次我就是为了购买\n',
            '采暖用的导力器而来到蔡斯的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，稍微休息一下，\n',
            '然后就去有名的中央工房看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C67(): pass

    label('loc_2C67')

    TalkEnd(0x00FE)

    Return()

# id: 0x0017 offset: 0x2C6B
@scena.Code('func_17_2C6B')
def func_17_2C6B():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '布草间\n',
            '※工作人员以外禁止进入。',
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

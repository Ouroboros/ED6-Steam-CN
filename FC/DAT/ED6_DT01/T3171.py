import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3171_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3171   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '玛尔奇娜主管'),
    TXT(0x02, '艾玛'),
    TXT(0x03, '多杰'),
    TXT(0x04, '亚鲁瓦教授'),
    TXT(0x05, '朵洛希'),
    TXT(0x06, '拉德米拉'),
    TXT(0x07, '卡雷尔'),
    TXT(0x08, '西加罗'),
    TXT(0x09, '艾德尔'),
    TXT(0x0A, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3171.x'
    header.mapIndex       = 1
    header.bgm            = 84
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x2BF8
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
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

# id: 0x10001 offset: 0xA8
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
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
    ]

# id: 0x10002 offset: 0xF2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
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

# id: 0x10003 offset: 0x212
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x212
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x212
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
    )

# id: 0x0000 offset: 0x236
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_258',
    )

    SetChrPos(0x0009, 34920, 0, 91540, 240)
    CreateThread(0x0009, 0x00, 0x00, 0x0006)

    Jump('loc_524')

    def _loc_258(): pass

    label('loc_258')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_28E',
    )

    SetChrPos(0x0009, 48750, 0, 137140, 170)
    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x000C, 650, 0, 3140, 280)
    SetChrFlags(0x000C, 0x0010)

    Jump('loc_524')

    def _loc_28E(): pass

    label('loc_28E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_2B0',
    )

    SetChrPos(0x0009, 53820, 0, 136060, 76)
    CreateThread(0x0009, 0x00, 0x00, 0x0004)

    Jump('loc_524')

    def _loc_2B0(): pass

    label('loc_2B0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_329',
    )

    SetChrPos(0x0009, 53820, 0, 136060, 76)
    CreateThread(0x0009, 0x00, 0x00, 0x0004)
    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, 35060, 0, 51880, 175)
    CreateThread(0x000B, 0x00, 0x00, 0x0008)
    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, 35130, 0, 91450, 214)
    CreateThread(0x000D, 0x00, 0x00, 0x0009)
    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x000E, 32420, 0, 95120, 302)
    CreateThread(0x000E, 0x00, 0x00, 0x000A)

    Jump('loc_524')

    def _loc_329(): pass

    label('loc_329')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_368',
    )

    SetChrPos(0x0009, 4750, 0, 1370, 265)
    CreateThread(0x0009, 0x00, 0x00, 0x0005)
    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x000A, 68050, 0, 56260, 30)
    CreateThread(0x000A, 0x00, 0x00, 0x0007)

    Jump('loc_524')

    def _loc_368(): pass

    label('loc_368')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_3DA',
    )

    SetChrPos(0x0009, 5810, 0, 3490, 194)
    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x000A, 68050, 0, 56260, 30)
    CreateThread(0x000A, 0x00, 0x00, 0x0007)
    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, 35130, 0, 91450, 214)
    CreateThread(0x000D, 0x00, 0x00, 0x0009)
    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x000E, 2990, 0, 1550, 87)
    CreateThread(0x000E, 0x00, 0x00, 0x000B)

    Jump('loc_524')

    def _loc_3DA(): pass

    label('loc_3DA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_42F',
    )

    SetChrPos(0x0009, 64750, 0, 95500, 3)
    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, 35130, 0, 91450, 214)
    CreateThread(0x000D, 0x00, 0x00, 0x0009)
    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x000E, 32420, 0, 95120, 302)
    CreateThread(0x000E, 0x00, 0x00, 0x000A)

    Jump('loc_524')

    def _loc_42F(): pass

    label('loc_42F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_49A',
    )

    SetChrPos(0x0009, 53820, 0, 136060, 76)
    CreateThread(0x0009, 0x00, 0x00, 0x0004)
    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x000A, 66540, 0, 59500, 354)
    ClearChrFlags(0x000F, 0x0080)
    SetChrPos(0x000F, 64450, 0, 95110, 275)
    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x0010, 68300, 0, 90910, 151)
    CreateThread(0x0010, 0x00, 0x00, 0x000C)

    Jump('loc_524')

    def _loc_49A(): pass

    label('loc_49A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_505',
    )

    SetChrPos(0x0009, 53820, 0, 136060, 76)
    CreateThread(0x0009, 0x00, 0x00, 0x0004)
    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x000A, 66540, 0, 59500, 354)
    ClearChrFlags(0x000F, 0x0080)
    SetChrPos(0x000F, 64450, 0, 95110, 275)
    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x0010, 68300, 0, 90910, 151)
    CreateThread(0x0010, 0x00, 0x00, 0x000C)

    Jump('loc_524')

    def _loc_505(): pass

    label('loc_505')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_524',
    )

    SetChrPos(0x0009, 35090, 0, 51720, 32)
    CreateThread(0x0009, 0x00, 0x00, 0x0003)

    def _loc_524(): pass

    label('loc_524')

    Return()

# id: 0x0001 offset: 0x525
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0x526
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_53B',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_53B(): pass

    label('loc_53B')

    Return()

# id: 0x0003 offset: 0x53C
@scena.Code('func_03_53C')
def func_03_53C():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_55F',
    )

    OP_8D(0x00FE, 33590, 49640, 1108473283, 53470, 3000)

    Jump('func_03_53C')

    def _loc_55F(): pass

    label('loc_55F')

    Return()

# id: 0x0004 offset: 0x560
@scena.Code('func_04_560')
def func_04_560():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_583',
    )

    OP_8D(0x00FE, 44740, 134200, 62330, 137000, 3000)

    Jump('func_04_560')

    def _loc_583(): pass

    label('loc_583')

    Return()

# id: 0x0005 offset: 0x584
@scena.Code('func_05_584')
def func_05_584():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5A7',
    )

    OP_8D(0x00FE, 1650, -310, 7710, 1910, 3000)

    Jump('func_05_584')

    def _loc_5A7(): pass

    label('loc_5A7')

    Return()

# id: 0x0006 offset: 0x5A8
@scena.Code('func_06_5A8')
def func_06_5A8():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5CB',
    )

    OP_8D(0x00FE, 4059, 88790, 36250, 93240, 3000)

    Jump('func_06_5A8')

    def _loc_5CB(): pass

    label('loc_5CB')

    Return()

# id: 0x0007 offset: 0x5CC
@scena.Code('func_07_5CC')
def func_07_5CC():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5EF',
    )

    OP_8D(0x00FE, 66680, 54350, 69610, 58920, 2000)

    Jump('func_07_5CC')

    def _loc_5EF(): pass

    label('loc_5EF')

    Return()

# id: 0x0008 offset: 0x5F0
@scena.Code('func_08_5F0')
def func_08_5F0():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_613',
    )

    OP_8D(0x00FE, 34200, 49490, 36490, 53440, 1500)

    Jump('func_08_5F0')

    def _loc_613(): pass

    label('loc_613')

    Return()

# id: 0x0009 offset: 0x614
@scena.Code('func_09_614')
def func_09_614():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_637',
    )

    OP_8D(0x00FE, 33860, 89530, 36420, 93590, 2000)

    Jump('func_09_614')

    def _loc_637(): pass

    label('loc_637')

    Return()

# id: 0x000A offset: 0x638
@scena.Code('func_0A_638')
def func_0A_638():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_65B',
    )

    OP_8D(0x00FE, 31570, 94690, 33720, 95490, 3000)

    Jump('func_0A_638')

    def _loc_65B(): pass

    label('loc_65B')

    Return()

# id: 0x000B offset: 0x65C
@scena.Code('func_0B_65C')
def func_0B_65C():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_67F',
    )

    OP_8D(0x00FE, 1090, -290, 4450, 2920, 3000)

    Jump('func_0B_65C')

    def _loc_67F(): pass

    label('loc_67F')

    Return()

# id: 0x000C offset: 0x680
@scena.Code('func_0C_680')
def func_0C_680():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_6A3',
    )

    OP_8D(0x00FE, 67180, 88480, 69500, 93510, 2000)

    Jump('func_0C_680')

    def _loc_6A3(): pass

    label('loc_6A3')

    Return()

# id: 0x000D offset: 0x6A4
@scena.Code('func_0D_6A4')
def func_0D_6A4():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_730',
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

    Jump('loc_871')

    def _loc_730(): pass

    label('loc_730')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_871',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_7C0',
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

    Jump('loc_871')

    def _loc_7C0(): pass

    label('loc_7C0')

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

    def _loc_871(): pass

    label('loc_871')

    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x875
@scena.Code('func_0E_875')
def func_0E_875():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_8E4',
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

    Jump('loc_943')

    def _loc_8E4(): pass

    label('loc_8E4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_943',
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

    def _loc_943(): pass

    label('loc_943')

    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x947
@scena.Code('func_0F_947')
def func_0F_947():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_D16',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0004, 0x00, 0x10)"),
            (Expr.TestScenaFlags, ScenaFlag(0x00B0, 3, 0x583)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_C55',
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
            '寻找齿轮的那个孩子啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我们之前不是\n',
            '接受过他的委托去找齿轮吗。',
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

    Jump('loc_D13')

    def _loc_C55(): pass

    label('loc_C55')

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

    def _loc_D13(): pass

    label('loc_D13')

    Jump('loc_13BC')

    def _loc_D16(): pass

    label('loc_D16')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_10BA',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0004, 0x00, 0x10)"),
            (Expr.TestScenaFlags, ScenaFlag(0x00B0, 3, 0x583)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1068',
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
            '寻找齿轮的那个孩子啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我们之前不是\n',
            '接受过他的委托去找齿轮吗。',
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
            '#002F哦，现在可不是\n',
            '说这种话的场合。',
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

    Jump('loc_10B7')

    def _loc_1068(): pass

    label('loc_1068')

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

    def _loc_10B7(): pass

    label('loc_10B7')

    Jump('loc_13BC')

    def _loc_10BA(): pass

    label('loc_10BA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_13BC',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0004, 0x00, 0x10)"),
            (Expr.TestScenaFlags, ScenaFlag(0x00B0, 3, 0x583)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_134A',
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
            '寻找齿轮的那个孩子啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我们之前不是\n',
            '接受过他的委托去找齿轮吗。',
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

    Jump('loc_13BC')

    def _loc_134A(): pass

    label('loc_134A')

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

    def _loc_13BC(): pass

    label('loc_13BC')

    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x13C0
@scena.Code('func_10_13C0')
def func_10_13C0():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_159D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_149C',
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

    Jump('loc_159A')

    def _loc_149C(): pass

    label('loc_149C')

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

    def _loc_159A(): pass

    label('loc_159A')

    Jump('loc_16CF')

    def _loc_159D(): pass

    label('loc_159D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_1642',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_15F6',
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

    Jump('loc_163F')

    def _loc_15F6(): pass

    label('loc_15F6')

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

    def _loc_163F(): pass

    label('loc_163F')

    Jump('loc_16CF')

    def _loc_1642(): pass

    label('loc_1642')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_16CF',
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

    def _loc_16CF(): pass

    label('loc_16CF')

    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0x16D3
@scena.Code('func_11_16D3')
def func_11_16D3():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_17D5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1766',
    )

    ChrTalk(
        0x0110,
        (
            '#0280091659V#150F所以啊～\n',
            '就和奈尔前辈这样说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280091660V『嗯～\n',
            '这边已经没问题了～』',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280091661V『我已经拍了\n',
            '很多可爱的照片啦～』',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17D5')

    def _loc_1766(): pass

    label('loc_1766')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x0110,
        (
            '#0280091656V#150F『嗯～』的这样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280091657V哎呀～主编～\n',
            '我都说了不是啦～……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280091658V唉～\n',
            '我想说的是～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17D5(): pass

    label('loc_17D5')

    TalkEnd(0x00FE)

    Return()

# id: 0x0012 offset: 0x17D9
@scena.Code('func_12_17D9')
def func_12_17D9():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_1A2B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1843',
    )

    ChrTalk(
        0x000B,
        (
            '#0150091686V#130F这个时间还在工作，\n',
            '做游击士也很辛苦啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150091687V那么，你们要加油哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A2B')

    def _loc_1843(): pass

    label('loc_1843')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000B,
        (
            '#0150091675V#130F哎呀……\n',
            '艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150091676V今天白天你们辛苦了吧。\n',
            '掌握到什么线索了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091677V#000F嗯……\n',
            '说到线索的话确实有一些吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010091678V……对不起，教授。\n',
            '现在有很急的事情要做呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0150091679V#130F哦，是吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150091680V竟然工作到这么晚……\n',
            '做游击士也很辛苦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091681V#000F今天比较特别嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091682V#010F那么，不好意思，\n',
            '我们就先告辞了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020091683V能向我们提供情报，\n',
            '真是多谢您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0150091684V#130F我能帮忙的事情\n',
            '也就只有这些了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0150091685V那么，你们要加油哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A2B(): pass

    label('loc_1A2B')

    TalkEnd(0x00FE)

    Return()

# id: 0x0013 offset: 0x1A2F
@scena.Code('func_13_1A2F')
def func_13_1A2F():
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
        'loc_1A8B',
    )

    OP_0D()
    OP_A9(0x3F)
    OP_56(0x00)
    TalkEnd(0x0008)

    Return()

    def _loc_1A8B(): pass

    label('loc_1A8B')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A9C',
    )

    TalkEnd(0x0008)

    Return()

    def _loc_1A9C(): pass

    label('loc_1A9C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_1BAC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1B3C',
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

    Jump('loc_1BA9')

    def _loc_1B3C(): pass

    label('loc_1B3C')

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

    def _loc_1BA9(): pass

    label('loc_1BA9')

    Jump('loc_227D')

    def _loc_1BAC(): pass

    label('loc_1BAC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_1C88',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1C15',
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

    Jump('loc_1C85')

    def _loc_1C15(): pass

    label('loc_1C15')

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

    def _loc_1C85(): pass

    label('loc_1C85')

    Jump('loc_227D')

    def _loc_1C88(): pass

    label('loc_1C88')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_1DBA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1D0C',
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

    Jump('loc_1DB7')

    def _loc_1D0C(): pass

    label('loc_1D0C')

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

    def _loc_1DB7(): pass

    label('loc_1DB7')

    Jump('loc_227D')

    def _loc_1DBA(): pass

    label('loc_1DBA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_1DF9',
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

    Jump('loc_227D')

    def _loc_1DF9(): pass

    label('loc_1DF9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_1ED9',
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

    Jump('loc_227D')

    def _loc_1ED9(): pass

    label('loc_1ED9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_1F1A',
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

    Jump('loc_227D')

    def _loc_1F1A(): pass

    label('loc_1F1A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_209B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1FBD',
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

    Jump('loc_2098')

    def _loc_1FBD(): pass

    label('loc_1FBD')

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

    def _loc_2098(): pass

    label('loc_2098')

    Jump('loc_227D')

    def _loc_209B(): pass

    label('loc_209B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_213A',
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

    Jump('loc_227D')

    def _loc_213A(): pass

    label('loc_213A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_2213',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_2194',
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

    Jump('loc_2210')

    def _loc_2194(): pass

    label('loc_2194')

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

    def _loc_2210(): pass

    label('loc_2210')

    Jump('loc_227D')

    def _loc_2213(): pass

    label('loc_2213')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_227D',
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

    def _loc_227D(): pass

    label('loc_227D')

    TalkEnd(0x0008)

    Return()

# id: 0x0014 offset: 0x2281
@scena.Code('func_14_2281')
def func_14_2281():
    Call(0, 0x0013)

    Return()

# id: 0x0015 offset: 0x2286
@scena.Code('func_15_2286')
def func_15_2286():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_2359',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_22E2',
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

    Jump('loc_2356')

    def _loc_22E2(): pass

    label('loc_22E2')

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

    def _loc_2356(): pass

    label('loc_2356')

    Jump('loc_2884')

    def _loc_2359(): pass

    label('loc_2359')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_2468',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_23C2',
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

    Jump('loc_2465')

    def _loc_23C2(): pass

    label('loc_23C2')

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

    def _loc_2465(): pass

    label('loc_2465')

    Jump('loc_2884')

    def _loc_2468(): pass

    label('loc_2468')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_254D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_24DA',
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

    Jump('loc_254A')

    def _loc_24DA(): pass

    label('loc_24DA')

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

    def _loc_254A(): pass

    label('loc_254A')

    Jump('loc_2884')

    def _loc_254D(): pass

    label('loc_254D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_25C4',
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

    Jump('loc_2884')

    def _loc_25C4(): pass

    label('loc_25C4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_26A8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_2637',
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

    Jump('loc_26A5')

    def _loc_2637(): pass

    label('loc_2637')

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

    def _loc_26A5(): pass

    label('loc_26A5')

    Jump('loc_2884')

    def _loc_26A8(): pass

    label('loc_26A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_26E0',
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

    Jump('loc_2884')

    def _loc_26E0(): pass

    label('loc_26E0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_2727',
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

    Jump('loc_2884')

    def _loc_2727(): pass

    label('loc_2727')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_282D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_2783',
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

    Jump('loc_282A')

    def _loc_2783(): pass

    label('loc_2783')

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

    def _loc_282A(): pass

    label('loc_282A')

    Jump('loc_2884')

    def _loc_282D(): pass

    label('loc_282D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_2884',
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

    def _loc_2884(): pass

    label('loc_2884')

    TalkEnd(0x00FE)

    Return()

# id: 0x0016 offset: 0x2888
@scena.Code('func_16_2888')
def func_16_2888():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_2900',
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

    Jump('loc_2BC6')

    def _loc_2900(): pass

    label('loc_2900')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_2A72',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_296F',
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

    Jump('loc_2A6F')

    def _loc_296F(): pass

    label('loc_296F')

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

    def _loc_2A6F(): pass

    label('loc_2A6F')

    Jump('loc_2BC6')

    def _loc_2A72(): pass

    label('loc_2A72')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_2BC6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_2ADE',
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

    Jump('loc_2BC6')

    def _loc_2ADE(): pass

    label('loc_2ADE')

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

    def _loc_2BC6(): pass

    label('loc_2BC6')

    TalkEnd(0x00FE)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

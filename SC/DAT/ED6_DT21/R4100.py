import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
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
    header.bgm            = 29
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
        ('ED6_DT07/CH02470._CH', 'ED6_DT07/CH02470P._CP'),
        ('ED6_DT07/CH01600._CH', 'ED6_DT07/CH01600P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
    ]

# id: 0x10001 offset: 0x142
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '管家菲利普',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '士兵',
            x                   = 124800,
            z                   = -2000,
            y                   = 6110,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '士兵',
            x                   = 124800,
            z                   = -2000,
            y                   = 3950,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '红色的飞艇影子',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '红色的飞艇影子',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '红色的飞艇影子',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0185,
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

# id: 0x10002 offset: 0x262
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '炽炎草',
            x           = 13640,
            z           = -40,
            y           = -2250,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0296,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '炽炎草',
            x           = -16650,
            z           = 300,
            y           = 2360,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0296,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '地狱火爆麻雀',
            x           = 15450,
            z           = -30,
            y           = 56010,
            word_0C     = 0x0000,
            word_0E     = 0x000C,
            byte_10     = 0x41,
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
            word_0E     = 0x000C,
            byte_10     = 0x41,
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
            word_0E     = 0x0004,
            byte_10     = 0x41,
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
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0297,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x30A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 93600,
            y           = -6000,
            z           = 5400,
            range       = 97500,
            dword_10    = 0x000007D0,
            dword_14    = 0x000062D4,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000005,
        ),
        ScenaEventData(
            x           = 14000,
            y           = -2000,
            z           = 30430,
            range       = 37950,
            dword_10    = 0x000007D0,
            dword_14    = 0x00005F0A,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000006,
        ),
        ScenaEventData(
            x           = -31650,
            y           = -100,
            z           = -14830,
            range       = -30070,
            dword_10    = 0x000006B8,
            dword_14    = 0x00000B86,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000D,
        ),
        ScenaEventData(
            x           = 126430,
            y           = -2000,
            z           = 11520,
            range       = 127710,
            dword_10    = 0xFFFFFCAE,
            dword_14    = 0xFFFFFCC2,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000E,
        ),
    )

# id: 0x10004 offset: 0x38A
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
            talkFunctionIndex   = 0x000F,
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
            talkFunctionIndex   = 0x0010,
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
            talkFunctionIndex   = 0x0011,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x3F6
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 0, 0x1638)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_40C',
    )

    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)

    def _loc_40C(): pass

    label('loc_40C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_428',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2D),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_08_1B55)

    def _loc_428(): pass

    label('loc_428')

    Return()

# id: 0x0001 offset: 0x429
@scena.Code('func_01_429')
def func_01_429():
    OP_16(0x02, 4000, -88000, -94000, 2293819)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 5, 0x1625)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_465',
    )

    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0014, 0x0080)
    ChrSetFlags(0x0015, 0x0080)
    ChrSetFlags(0x0016, 0x0080)

    def _loc_465(): pass

    label('loc_465')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 0, 0x2038)),
            Expr.Return,
        ),
        'loc_47A',
    )

    MapSetFlags(0x02000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2D),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_47A(): pass

    label('loc_47A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 0, 0x1638)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_492',
    )

    OP_B1('R4100_y')

    Jump('loc_4AA')

    def _loc_492(): pass

    label('loc_492')

    OP_B1('R4100_n')
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    OP_71(0x0005, 0x0004)

    def _loc_4AA(): pass

    label('loc_4AA')

    Return()

# id: 0x0002 offset: 0x4AB
@scena.Code('func_02_4AB')
def func_02_4AB():
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
        'loc_4D0',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_563')

    def _loc_4D0(): pass

    label('loc_4D0')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4E9',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_563')

    def _loc_4E9(): pass

    label('loc_4E9')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_502',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_563')

    def _loc_502(): pass

    label('loc_502')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_51B',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_563')

    def _loc_51B(): pass

    label('loc_51B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_534',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_563')

    def _loc_534(): pass

    label('loc_534')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_54D',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_563')

    def _loc_54D(): pass

    label('loc_54D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_563',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    def _loc_563(): pass

    label('loc_563')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_578',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_563')

    def _loc_578(): pass

    label('loc_578')

    Return()

# id: 0x0003 offset: 0x579
@scena.Code('func_03_579')
def func_03_579():
    TalkBegin(0x0009)

    ChrTalk(
        0x00FE,
        (
            '因为紧急情况的缘故，\n',
            '整个艾尔贝周游道地区都被封锁了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '抱歉，你们不能过去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0009)

    Return()

# id: 0x0004 offset: 0x5D5
@scena.Code('func_04_5D5')
def func_04_5D5():
    TalkBegin(0x000A)

    ChrTalk(
        0x00FE,
        (
            '袭击艾尔贝离宫的\n',
            '武装集团似乎潜伏在\n',
            '周游道附近。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在正在开展封锁作战\n',
            '来追击他们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000A)

    Return()

# id: 0x0005 offset: 0x639
@scena.Code('func_05_639')
def func_05_639():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 0, 0x1618)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_646',
    )

    Return()

    def _loc_646(): pass

    label('loc_646')

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
        'loc_66A',
    )

    Call(0, 0x000A)
    Call(0, 0x000B)
    FormationAddMember(ChrTable['玲'], 0xFF, 0xFF)
    FadeIn(0, 0)

    def _loc_66A(): pass

    label('loc_66A')

    ChrSetPos(0x0008, 77770, 0, 14150, 90)

    NpcTalk(
        0x0008,
        '男性的声音',
        (
            '#0660250001V哎呀，你们是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    Fade(1000)
    CameraMove(94100, -2000, 12960, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0101, 95390, -2000, 11850, 270)
    ChrSetPos(0x0008, 86980, -250, 13060, 90)
    ChrSetPos(0x012F, 97900, -2000, 12150, 270)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7D4',
    )

    ChrSetPos(0x0105, 95530, -2000, 12900, 270)
    ChrSetPos(0x00F7, 96600, -2000, 12700, 270)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_790',
    )

    ChrSetPos(0x0104, 96820, -2000, 11620, 270)

    Jump('loc_7D1')

    def _loc_790(): pass

    label('loc_790')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7B2',
    )

    ChrSetPos(0x0107, 96820, -2000, 11620, 270)

    Jump('loc_7D1')

    def _loc_7B2(): pass

    label('loc_7B2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7D1',
    )

    ChrSetPos(0x0108, 96820, -2000, 11620, 270)

    def _loc_7D1(): pass

    label('loc_7D1')

    Jump('loc_807')

    def _loc_7D4(): pass

    label('loc_7D4')

    ChrSetPos(0x00F7, 95530, -2000, 12900, 270)
    ChrSetPos(0x00F8, 96670, -2000, 12700, 270)
    ChrSetPos(0x00F9, 96820, -2000, 11620, 270)
    def _loc_807(): pass

    label('loc_807')

    ChrWalkTo(0x0008, 93390, -2000, 12570, 2000, 0x00)
    OP_0D()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BA0',
    )

    ChrTalk(
        0x0101,
        (
            '#0010250002V#1004F咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060250003V#044F#2P啊……\n',
            '菲利普先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060250004V#040F好久不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0660250005V#720F#5P好久不见。\n',
            '科洛蒂娅殿下、艾丝蒂尔小姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660250006V你们几位去过艾尔贝离宫了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250007V#1006F嗯，是的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060250008V#542F#2P菲利普先生\n',
            '到王都去有事情吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0660250009V#720F#5P是的，公爵阁下\n',
            '吩咐我出来买东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660250010V#721F……莫非你们\n',
            '在离宫已经遇见殿下了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250011V#1016F嗯、嗯，算是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060250012V#045F#2P我们和久违多时的他\n',
            '稍微寒暄了一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0660250013V#722F#5P……看来\n',
            '他又得罪了你们吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660250014V实在是对不起。\n',
            '我以臣下的身份向各位道歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060250015V#047F#2P呵呵，您太客气了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060250016V#040F我听说叔叔他被软禁，\n',
            '所以感到有点担心……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060250017V不过他看起来很有精神，我也就放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0660250018V#720F#5P您能够这么说，我真是高兴。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660250019V那么我就先告辞了……\n',
            '各位，失陪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E44')

    def _loc_BA0(): pass

    label('loc_BA0')

    ChrTalk(
        0x0101,
        (
            '#0010250020V#1004F咦……\n',
            '这不是菲利普先生吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0660250021V#720F#5P艾丝蒂尔小姐。\n',
            '好久不见。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660250006V你们几位去过艾尔贝离宫了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250023V#1006F嗯，是的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250024V菲利普先生\n',
            '来王都办事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0660250009V#720F#5P是的，公爵阁下\n',
            '吩咐我出来买东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660250010V#721F……莫非你们\n',
            '在离宫已经遇见殿下了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250027V#1025F嗯、嗯，算是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0660250028V#722F#5P……看来他又无心\n',
            '得罪了你们吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660250014V实在是对不起。\n',
            '我以臣下的身份向各位道歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250030V#1016F也不是，他倒没\n',
            '说过什么失礼的话。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250031V#1006F我并不介意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0660250018V#720F#5P您能够这么说，我真是高兴。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660250019V那么我就先告辞了……\n',
            '各位，失陪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E44(): pass

    label('loc_E44')

    @scena.Lambda('lambda_0E4A')
    def lambda_0E4A():
        ChrWalkTo(0x00FE, 95100, -2000, 10770, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0E4A)

    @scena.Lambda('lambda_0E65')
    def lambda_0E65():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0E65')

    DispatchAsync2(0x0101, 0x0001, lambda_0E65)

    @scena.Lambda('lambda_0E76')
    def lambda_0E76():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0E76')

    DispatchAsync2(0x012F, 0x0001, lambda_0E76)

    @scena.Lambda('lambda_0E87')
    def lambda_0E87():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0E87')

    DispatchAsync2(0x00F7, 0x0001, lambda_0E87)

    @scena.Lambda('lambda_0E98')
    def lambda_0E98():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0E98')

    DispatchAsync2(0x00F8, 0x0001, lambda_0E98)

    @scena.Lambda('lambda_0EA9')
    def lambda_0EA9():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0EA9')

    DispatchAsync2(0x00F9, 0x0001, lambda_0EA9)

    WaitForThreadExit(0x0008, 0x0001)

    @scena.Lambda('lambda_0EBF')
    def lambda_0EBF():
        ChrWalkTo(0x00FE, 108070, -2000, 8520, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0EBF)

    @scena.Lambda('lambda_0EDA')
    def lambda_0EDA():
        CameraMove(99610, -2000, 11170, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0EDA)

    @scena.Lambda('lambda_0EF2')
    def lambda_0EF2():
        OP_67(0, 8680, -10000, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0EF2)

    WaitForThreadExit(0x0008, 0x0001)
    ChrSetFlags(0x0008, 0x0080)

    @scena.Lambda('lambda_0F14')
    def lambda_0F14():
        CameraMove(96350, -2000, 12530, 1600)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0F14)

    @scena.Lambda('lambda_0F2C')
    def lambda_0F2C():
        OP_67(0, 8680, -10000, 1600)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0F2C)

    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0101, 0x0003)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x012F, 0x01)
    TerminateThread(0x00F7, 0x01)
    TerminateThread(0x00F8, 0x01)
    TerminateThread(0x00F9, 0x01)

    ChrTalk(
        0x0101,
        (
            '#0010250034V#1007F呼～他还是\n',
            '那么辛苦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250035V#1015F他好像从公爵小时候起\n',
            '就一直负责照顾公爵的起居……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_10A1',
    )

    ChrSetDirection(0x0105, 180, 400)

    ChrTalk(
        0x0105,
        (
            '#0060250036V#040F#2P好像已经照顾了\n',
            '20年以上了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060250037V据说在那之前\n',
            '他是在亲卫队工作的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 360, 400)

    ChrTalk(
        0x0101,
        (
            '#0010250038V#1004F咦，真的吗！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250039V#1006F唔～果然是\n',
            '人不可貌相呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10A1(): pass

    label('loc_10A1')

    ChrTalk(
        0x012F,
        (
            '#0220250040V#264F#7P…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220250041V#263F刚才那爷爷……\n',
            '绝不是简单的人物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1109')
    def lambda_1109():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1109)

    Sleep(50)

    @scena.Lambda('lambda_111C')
    def lambda_111C():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_111C)

    Sleep(50)

    @scena.Lambda('lambda_112F')
    def lambda_112F():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_112F)

    Sleep(50)

    @scena.Lambda('lambda_1142')
    def lambda_1142():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_1142)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_119E',
    )

    ChrTalk(
        0x0101,
        (
            '#0010250042V#1004F哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070250043V#064F怎么了？小玲？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11DA')

    def _loc_119E(): pass

    label('loc_119E')

    ChrTalk(
        0x0101,
        (
            '#0010250044V#1004F啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250045V怎么突然这么说？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11DA(): pass

    label('loc_11DA')

    ChrTurnDirection(0x012F, 0x0101, 400)

    ChrTalk(
        0x012F,
        (
            '#0220250046V#260F因为，他可以\n',
            '闭着眼睛走路嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220250047V玲就绝对做不到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x00F7, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1288',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    Jump('loc_12C6')

    def _loc_1288(): pass

    label('loc_1288')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_12AF',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    Jump('loc_12C6')

    def _loc_12AF(): pass

    label('loc_12AF')

    OP_62(0x00F8, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    def _loc_12C6(): pass

    label('loc_12C6')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_12ED',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    Jump('loc_132B')

    def _loc_12ED(): pass

    label('loc_12ED')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1314',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    Jump('loc_132B')

    def _loc_1314(): pass

    label('loc_1314')

    OP_62(0x00F9, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    def _loc_132B(): pass

    label('loc_132B')

    Sleep(1500)

    ChrTalk(
        0x0101,
        (
            '#0010250048V#1016F唔，我想\n',
            '那不是闭着眼睛，\n',
            '应该是眯着眼睛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250049V#1006F而且他吃惊的时候，\n',
            '眼睛还是会睁得大大的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#0220250050V#264F哎呀？是吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220250051V#261F呵呵，我也好想\n',
            '看看他吃惊的样子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    SetScenaFlags(ScenaFlag(0x02C3, 0, 0x1618))
    EventEnd(0x00)

    Return()

# id: 0x0006 offset: 0x1417
@scena.Code('func_06_1417')
def func_06_1417():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 2, 0x2002)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 4, 0x2004)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 6, 0x2006)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 0, 0x2038)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_142E',
    )

    Return()

    def _loc_142E(): pass

    label('loc_142E')

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
        'loc_144E',
    )

    Call(0, 0x000A)
    Call(0, 0x000C)
    FadeIn(0, 0)

    def _loc_144E(): pass

    label('loc_144E')

    OP_20(0x000007D0)
    Fade(1000)
    ChrSetPos(0x0101, 26220, 0, 27190, 0)
    ChrSetPos(0x0102, 27510, 0, 27180, 0)
    ChrSetPos(0x00F8, 26280, 0, 25750, 0)
    ChrSetPos(0x00F9, 27640, 0, 25770, 0)
    CameraMove(27520, 0, 25330, 0)
    OP_67(0, 7360, -10000, 0)
    CameraSetDistance(2240, 0)
    OP_6C(147000, 0)
    OP_6E(349, 0)
    OP_0D()
    CreateThread(0x0101, 0x03, 0x00, func_07_1AC8)
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0102, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(100)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1531',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x26, 0x26, 0x000000FA, 0x01)

    Jump('loc_1565')

    def _loc_1531(): pass

    label('loc_1531')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1553',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x26, 0x26, 0x000000FA, 0x01)

    Jump('loc_1565')

    def _loc_1553(): pass

    label('loc_1553')

    OP_62(0x00F8, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)

    def _loc_1565(): pass

    label('loc_1565')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1587',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x26, 0x26, 0x000000FA, 0x01)

    Jump('loc_15BB')

    def _loc_1587(): pass

    label('loc_1587')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_15A9',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x26, 0x26, 0x000000FA, 0x01)

    Jump('loc_15BB')

    def _loc_15A9(): pass

    label('loc_15A9')

    OP_62(0x00F9, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)

    def _loc_15BB(): pass

    label('loc_15BB')

    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010380001V#1004F#6P咦……这是？',
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
            Expr.Return,
        ),
        'loc_1633',
    )

    ChrTalk(
        0x0106,
        (
            '#0050380040V#052F#2P什么啊，这不是\n',
            '飞船的引擎声吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16C2')

    def _loc_1633(): pass

    label('loc_1633')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_167F',
    )

    ChrTalk(
        0x0103,
        (
            '#0030380041V#023F#2P什么啊，这不是\n',
            '飞船的引擎声吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16C2')

    def _loc_167F(): pass

    label('loc_167F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_16C2',
    )

    ChrTalk(
        0x0108,
        (
            '#0080380042V#073F#2P这是……\n',
            '飞船的引擎声吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_16C2(): pass

    label('loc_16C2')

    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1712',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x18, 0x1B, 0x000000FA, 0x00)

    Jump('loc_1746')

    def _loc_1712(): pass

    label('loc_1712')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1734',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)

    Jump('loc_1746')

    def _loc_1734(): pass

    label('loc_1734')

    OP_62(0x00F8, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)

    def _loc_1746(): pass

    label('loc_1746')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_176D',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x18, 0x1B, 0x000000FA, 0x00)

    Jump('loc_17A1')

    def _loc_176D(): pass

    label('loc_176D')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_178F',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)

    Jump('loc_17A1')

    def _loc_178F(): pass

    label('loc_178F')

    OP_62(0x00F9, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)

    def _loc_17A1(): pass

    label('loc_17A1')

    Sleep(1500)

    OP_63(0x0101)
    OP_63(0x0102)
    OP_63(0x00F8)
    OP_63(0x00F9)
    Sleep(200)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1816',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_1854')

    def _loc_1816(): pass

    label('loc_1816')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_183D',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_1854')

    def _loc_183D(): pass

    label('loc_183D')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_1854(): pass

    label('loc_1854')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1880',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_18BE')

    def _loc_1880(): pass

    label('loc_1880')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_18A7',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_18BE')

    def _loc_18A7(): pass

    label('loc_18A7')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_18BE(): pass

    label('loc_18BE')

    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010380005V#1020F#6P等、等等！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1936',
    )

    ChrTalk(
        0x0107,
        (
            '#0070380044V#065F#2P这、这种时候\n',
            '飞船怎么还能飞……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19C5')

    def _loc_1936(): pass

    label('loc_1936')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_197E',
    )

    ChrTalk(
        0x0108,
        (
            '#0080380045V#076F#2P这种时候\n',
            '飞船怎么还能飞……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19C5')

    def _loc_197E(): pass

    label('loc_197E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_19C5',
    )

    ChrTalk(
        0x0103,
        (
            '#0030380046V#024F#2P这种时候\n',
            '飞船怎么还可以飞……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19C5(): pass

    label('loc_19C5')

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetDirection(0x0102, 135, 500)

    ChrTalk(
        0x0102,
        (
            '#0020380047V#1046F#6P在那里……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1A15')
    def lambda_1A15():
        CameraMove(35140, 0, 17330, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1A15)

    @scena.Lambda('lambda_1A2D')
    def lambda_1A2D():
        OP_67(0, 11840, -10000, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1A2D)

    @scena.Lambda('lambda_1A45')
    def lambda_1A45():
        CameraSetDistance(2700, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1A45)

    @scena.Lambda('lambda_1A55')
    def lambda_1A55():
        OP_6C(111000, 2500)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_1A55)

    @scena.Lambda('lambda_1A65')
    def lambda_1A65():
        OP_6E(427, 2500)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_1A65)

    @scena.Lambda('lambda_1A75')
    def lambda_1A75():
        ChrSetDirection(0x00FE, 135, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1A75)

    Sleep(50)

    @scena.Lambda('lambda_1A88')
    def lambda_1A88():
        ChrSetDirection(0x00FE, 135, 500)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_1A88)

    Sleep(50)

    @scena.Lambda('lambda_1A9B')
    def lambda_1A9B():
        ChrSetDirection(0x00FE, 135, 500)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_1A9B)

    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    MapSetFlags(0x00100000)
    SetScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    SetScenaFlags(ScenaFlag(0x021F, 0, 0x10F8))
    NewScene('ED6_DT21/E0810._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0007 offset: 0x1AC8
@scena.Code('func_07_1AC8')
def func_07_1AC8():
    PlaySE(121, 0x01, 0x32)
    Sleep(200)

    OP_24(0x0079, 0x35)
    Sleep(200)

    OP_24(0x0079, 0x38)
    Sleep(200)

    OP_24(0x0079, 0x3C)
    Sleep(200)

    OP_24(0x0079, 0x3F)
    Sleep(200)

    OP_24(0x0079, 0x42)
    Sleep(200)

    OP_24(0x0079, 0x46)
    Sleep(200)

    OP_24(0x0079, 0x49)
    Sleep(200)

    OP_24(0x0079, 0x4C)
    Sleep(200)

    OP_24(0x0079, 0x50)
    Sleep(200)

    OP_24(0x0079, 0x53)
    Sleep(200)

    OP_24(0x0079, 0x56)
    Sleep(200)

    OP_24(0x0079, 0x5A)
    Sleep(200)

    OP_24(0x0079, 0x5D)
    Sleep(200)

    OP_24(0x0079, 0x60)
    Sleep(200)

    OP_24(0x0079, 0x64)

    Return()

# id: 0x0008 offset: 0x1B55
@scena.Code('func_08_1B55')
def func_08_1B55():
    EventBegin(0x00)
    MapClearFlags(0x00100000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1B7A',
    )

    Call(0, 0x000A)
    Call(0, 0x000C)
    FadeIn(0, 0)

    def _loc_1B7A(): pass

    label('loc_1B7A')

    PlaySE(121, 0x01, 0x64)
    ChrSetPos(0x0101, 26590, 0, 26840, 135)
    ChrSetPos(0x0102, 28060, 0, 26570, 135)
    ChrSetPos(0x00F8, 26420, 0, 24940, 135)
    ChrSetPos(0x00F9, 27850, 0, 24990, 135)
    CameraMove(27140, 0, 26500, 0)
    OP_67(0, 8210, -10000, 0)
    CameraSetDistance(2900, 0)
    OP_6C(335000, 0)
    OP_6E(262, 0)
    OP_72(0x0000, 0x0004)
    OP_72(0x0001, 0x0004)
    OP_72(0x0002, 0x0004)
    OP_A1(0x000B, 0x0000)
    OP_A1(0x000C, 0x0001)
    OP_A1(0x000D, 0x0002)
    ChrSetPos(0x000B, 43360, 2000, 11200, 315)
    ChrSetPos(0x000C, 48360, 2000, 16200, 315)
    ChrSetPos(0x000D, 38360, 2000, 6200, 315)
    FadeIn(1000, 0)
    OP_0D()

    @scena.Lambda('lambda_1C61')
    def lambda_1C61():
        ChrMoveToRelative(0x00FE, -40000, 0, 40000, 30000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1C61)

    Sleep(800)

    @scena.Lambda('lambda_1C81')
    def lambda_1C81():
        ChrSetDirection(0x00FE, 315, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1C81)

    Sleep(50)

    @scena.Lambda('lambda_1C94')
    def lambda_1C94():
        ChrSetDirection(0x00FE, 315, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_1C94)

    Sleep(60)

    @scena.Lambda('lambda_1CA7')
    def lambda_1CA7():
        ChrSetDirection(0x00FE, 315, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0003, lambda_1CA7)

    Sleep(50)

    @scena.Lambda('lambda_1CBA')
    def lambda_1CBA():
        ChrSetDirection(0x00FE, 315, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0003, lambda_1CBA)

    @scena.Lambda('lambda_1CC8')
    def lambda_1CC8():
        ChrMoveToRelative(0x00FE, -40000, 0, 40000, 30000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1CC8)

    Sleep(1000)

    @scena.Lambda('lambda_1CE8')
    def lambda_1CE8():
        ChrMoveToRelative(0x00FE, -40000, 0, 40000, 30000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1CE8)

    WaitForThreadExit(0x000D, 0x0001)
    CreateThread(0x0102, 0x02, 0x00, func_09_1EAB)
    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)

    ChrTalk(
        0x0101,
        (
            '#0010380010V#1020F#6P『结社』的飞艇……\n',
            '为、为什么会在这里！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020380049V#1046F#4P不好……\n',
            '那是王都的方向！',
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
            Expr.Return,
        ),
        'loc_1DE0',
    )

    ChrTalk(
        0x0106,
        (
            '#0050380012V#057F#6P这可不是闹着玩的！\n',
            '我们赶快追上去吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E5E')

    def _loc_1DE0(): pass

    label('loc_1DE0')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1E28',
    )

    ChrTalk(
        0x0103,
        (
            '#0030380013V#022F#6P这……\n',
            '看来动作必须快一点了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E5E')

    def _loc_1E28(): pass

    label('loc_1E28')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1E5E',
    )

    ChrTalk(
        0x0108,
        (
            '#0080380014V#076F#6P赶快追上去吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E5E(): pass

    label('loc_1E5E')

    SetScenaFlags(ScenaFlag(0x0407, 0, 0x2038))
    OP_28(0x009C, 0x04, 0x02)
    OP_28(0x009C, 0x04, 0x08)
    OP_28(0x009C, 0x01, 0x0001)
    OP_28(0x00B5, 0x04, 0x40)
    OP_28(0x00B6, 0x04, 0x40)
    OP_28(0x00B7, 0x04, 0x40)
    OP_28(0x00B8, 0x04, 0x40)
    OP_28(0x00B9, 0x04, 0x40)
    OP_28(0x00BA, 0x04, 0x40)
    OP_28(0x00BB, 0x04, 0x40)
    OP_28(0x00BC, 0x04, 0x40)
    OP_28(0x00BD, 0x04, 0x40)
    OP_28(0x00BE, 0x04, 0x40)
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

# id: 0x0009 offset: 0x1EAB
@scena.Code('func_09_1EAB')
def func_09_1EAB():
    OP_24(0x0079, 0x5F)
    Sleep(300)

    OP_24(0x0079, 0x5A)
    Sleep(300)

    OP_24(0x0079, 0x55)
    Sleep(300)

    OP_24(0x0079, 0x50)
    Sleep(300)

    OP_24(0x0079, 0x4B)
    Sleep(300)

    OP_24(0x0079, 0x46)
    Sleep(300)

    OP_24(0x0079, 0x41)
    Sleep(300)

    OP_24(0x0079, 0x3C)
    Sleep(300)

    OP_24(0x0079, 0x37)
    Sleep(300)

    OP_24(0x0079, 0x32)
    Sleep(300)

    OP_24(0x0079, 0x2D)
    Sleep(300)

    OP_24(0x0079, 0x28)
    Sleep(300)

    OP_24(0x0079, 0x23)
    Sleep(300)

    OP_24(0x0079, 0x1E)
    Sleep(300)

    OP_24(0x0079, 0x19)
    Sleep(300)

    OP_24(0x0079, 0x14)
    Sleep(300)

    OP_23(0x0079)

    Return()

# id: 0x000A offset: 0x1F3F
@scena.Code('func_0A_1F3F')
def func_0A_1F3F():
    FadeOut(0, 0, -1)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)

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
        (0x00000000, 'loc_1FB9'),
        (0x00000001, 'loc_1FBF'),
        (-1, 'loc_1FC5'),
    )

    def _loc_1FB9(): pass

    label('loc_1FB9')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_1FC5')

    def _loc_1FBF(): pass

    label('loc_1FBF')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_1FC5')

    def _loc_1FC5(): pass

    label('loc_1FC5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_1FD3',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_1FD7')

    def _loc_1FD3(): pass

    label('loc_1FD3')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_1FD7(): pass

    label('loc_1FD7')

    Return()

# id: 0x000B offset: 0x1FD8
@scena.Code('func_0B_1FD8')
def func_0B_1FD8():
    MapClearFlags(0x00000001)
    CameraMove(106730, -1920, 53920, 0)
    Sleep(100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_201B',
    )

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['雪拉扎德'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            ChrTable['提妲'],
            ChrTable['金'],
            0xFFFF,
        ),
    )

    Jump('loc_2039')

    def _loc_201B(): pass

    label('loc_201B')

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['阿加特'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            ChrTable['提妲'],
            ChrTable['金'],
            0xFFFF,
        ),
    )

    def _loc_2039(): pass

    label('loc_2039')

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

# id: 0x000C offset: 0x2059
@scena.Code('func_0C_2059')
def func_0C_2059():
    MapClearFlags(0x00000001)
    CameraMove(106730, -1920, 53920, 0)
    Sleep(100)

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['雪拉扎德'],
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

# id: 0x000D offset: 0x20B2
@scena.Code('func_0D_20B2')
def func_0D_20B2():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 0, 0x1638)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_217C',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2118',
    )

    ChrTalk(
        0x0101,
        (
            '#0010271282V#1002F现在不是到处闲逛的时候。\n',
            '……要赶快返回协会才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2161')

    def _loc_2118(): pass

    label('loc_2118')

    ChrTalk(
        0x0109,
        (
            '#0180271283V#1063F现在不是到处闲逛的时候。\n',
            '……赶紧去王都的协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2161(): pass

    label('loc_2161')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_217C(): pass

    label('loc_217C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 2, 0x203A)),
            Expr.Return,
        ),
        'loc_2342',
    )

    EventBegin(0x01)

    Switch(
        (
            (Expr.PushValueByIndex, 0xA),
            Expr.Return,
        ),
        (0x00000000, 'loc_21A5'),
        (0x00000001, 'loc_21E5'),
        (0x00000002, 'loc_2225'),
        (0x00000005, 'loc_2264'),
        (0x00000007, 'loc_22A3'),
        (0x00000006, 'loc_22E4'),
        (-1, 'loc_231F'),
    )

    def _loc_21A5(): pass

    label('loc_21A5')

    ChrTalk(
        0x0101,
        (
            '#0010380015V#1002F没时间去别的地方了。\n',
            '快点前往王都吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_231F')

    def _loc_21E5(): pass

    label('loc_21E5')

    ChrTalk(
        0x0102,
        (
            '#0020380016V#1042F没时间去别处了。\n',
            '要尽快前往王都才行！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_231F')

    def _loc_2225(): pass

    label('loc_2225')

    ChrTalk(
        0x0103,
        (
            '#0030380017V#022F没时间去别的地方了。\n',
            '赶紧前往王都吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_231F')

    def _loc_2264(): pass

    label('loc_2264')

    ChrTalk(
        0x0106,
        (
            '#0050380018V#057F没时间去别的地方了。\n',
            '赶紧前往王都吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_231F')

    def _loc_22A3(): pass

    label('loc_22A3')

    ChrTalk(
        0x0108,
        (
            '#0080380019V#072F没时间去别的地方了啊。\n',
            '赶紧前往王都吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_231F')

    def _loc_22E4(): pass

    label('loc_22E4')

    ChrTalk(
        0x0107,
        (
            '#0070380020V#062F没时间去别处了。\n',
            '必须赶紧去王都！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_231F')

    def _loc_231F(): pass

    label('loc_231F')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    MapSetFlags(0x02000000)

    Jump('loc_24EB')

    def _loc_2342(): pass

    label('loc_2342')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 0, 0x2038)),
            Expr.Return,
        ),
        'loc_24EB',
    )

    EventBegin(0x01)

    Switch(
        (
            (Expr.PushValueByIndex, 0xA),
            Expr.Return,
        ),
        (0x00000000, 'loc_236B'),
        (0x00000001, 'loc_23A7'),
        (0x00000002, 'loc_23E3'),
        (0x00000005, 'loc_241C'),
        (0x00000007, 'loc_2455'),
        (0x00000006, 'loc_2488'),
        (-1, 'loc_24CB'),
    )

    def _loc_236B(): pass

    label('loc_236B')

    ChrTalk(
        0x0101,
        (
            '#0010380021V#1002F不，不是这边！\n',
            '……赶紧去王都吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24CB')

    def _loc_23A7(): pass

    label('loc_23A7')

    ChrTalk(
        0x0102,
        (
            '#0020380022V#1042F不，不是这边！\n',
            '……赶紧去王都吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24CB')

    def _loc_23E3(): pass

    label('loc_23E3')

    ChrTalk(
        0x0103,
        (
            '#0030380023V#022F不对，不是这边！\n',
            '赶紧去王都吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24CB')

    def _loc_241C(): pass

    label('loc_241C')

    ChrTalk(
        0x0106,
        (
            '#0050380024V#057F不对，不是这边！\n',
            '赶紧去王都吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24CB')

    def _loc_2455(): pass

    label('loc_2455')

    ChrTalk(
        0x0108,
        (
            '#0080380025V#072F不是这边。\n',
            '赶紧去王都吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24CB')

    def _loc_2488(): pass

    label('loc_2488')

    ChrTalk(
        0x0107,
        (
            '#0070380026V#065F那个那个……不是这边。\n',
            '要赶紧去王都才行！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24CB')

    def _loc_24CB(): pass

    label('loc_24CB')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    MapSetFlags(0x02000000)

    def _loc_24EB(): pass

    label('loc_24EB')

    Return()

# id: 0x000E offset: 0x24EC
@scena.Code('func_0E_24EC')
def func_0E_24EC():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 2, 0x203A)),
            Expr.Return,
        ),
        'loc_26D9',
    )

    EventBegin(0x02)

    Switch(
        (
            (Expr.PushValueByIndex, 0xA),
            Expr.Return,
        ),
        (0x00000000, 'loc_2515'),
        (0x00000001, 'loc_254F'),
        (0x00000002, 'loc_2589'),
        (0x00000005, 'loc_25C2'),
        (0x00000007, 'loc_25FB'),
        (0x00000006, 'loc_2634'),
        (-1, 'loc_2671'),
    )

    def _loc_2515(): pass

    label('loc_2515')

    ChrTalk(
        0x0101,
        (
            '#0010380015V#1002F没时间去别处了。\n',
            '赶紧去王都吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2671')

    def _loc_254F(): pass

    label('loc_254F')

    ChrTalk(
        0x0102,
        (
            '#0020380016V#1042F没时间去别处了。\n',
            '赶紧去王都吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2671')

    def _loc_2589(): pass

    label('loc_2589')

    ChrTalk(
        0x0103,
        (
            '#0030380017V#022F没时间去别处了。\n',
            '赶紧去王都吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2671')

    def _loc_25C2(): pass

    label('loc_25C2')

    ChrTalk(
        0x0106,
        (
            '#0050380018V#057F没时间去别处了。\n',
            '赶紧去王都吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2671')

    def _loc_25FB(): pass

    label('loc_25FB')

    ChrTalk(
        0x0108,
        (
            '#0080380019V#072F没时间去别处了。\n',
            '赶紧去王都吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2671')

    def _loc_2634(): pass

    label('loc_2634')

    ChrTalk(
        0x0107,
        (
            '#0070380020V#062F没时间去别处了。\n',
            '要赶紧去王都才行！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2671')

    def _loc_2671(): pass

    label('loc_2671')

    OP_59()
    Fade(1000)
    ChrSetPos(0x0000, 123990, -2000, 5010, 275)
    ChrSetPos(0x0001, 123990, -2000, 5010, 275)
    ChrSetPos(0x0002, 123990, -2000, 5010, 275)
    ChrSetPos(0x0003, 123990, -2000, 5010, 275)
    OP_69(0x0000, 0)
    OP_0D()
    ChrSetDirection(0x0000, 275, 0)
    Sleep(50)

    EventEnd(0x04)
    MapSetFlags(0x02000000)

    Jump('loc_28C5')

    def _loc_26D9(): pass

    label('loc_26D9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 0, 0x2038)),
            Expr.Return,
        ),
        'loc_28C5',
    )

    EventBegin(0x02)

    Switch(
        (
            (Expr.PushValueByIndex, 0xA),
            Expr.Return,
        ),
        (0x00000000, 'loc_2702'),
        (0x00000001, 'loc_273E'),
        (0x00000002, 'loc_2778'),
        (0x00000005, 'loc_27B1'),
        (0x00000007, 'loc_27EA'),
        (0x00000006, 'loc_281D'),
        (-1, 'loc_2860'),
    )

    def _loc_2702(): pass

    label('loc_2702')

    ChrTalk(
        0x0101,
        (
            '#0010380021V#1002F不，不是这边！\n',
            '……赶紧去王都吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2860')

    def _loc_273E(): pass

    label('loc_273E')

    ChrTalk(
        0x0102,
        (
            '#0020380022V#1042F不，不是这边！\n',
            '……赶紧去王都！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2860')

    def _loc_2778(): pass

    label('loc_2778')

    ChrTalk(
        0x0103,
        (
            '#0030380023V#022F不对，不是这边！\n',
            '赶紧去王都吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2860')

    def _loc_27B1(): pass

    label('loc_27B1')

    ChrTalk(
        0x0106,
        (
            '#0050380024V#057F不对，不是这边！\n',
            '赶紧去王都吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2860')

    def _loc_27EA(): pass

    label('loc_27EA')

    ChrTalk(
        0x0108,
        (
            '#0080380025V#072F不是这边。\n',
            '赶紧去王都吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2860')

    def _loc_281D(): pass

    label('loc_281D')

    ChrTalk(
        0x0107,
        (
            '#0070380026V#065F那个那个……不是这边。\n',
            '要赶紧去王都才行！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2860')

    def _loc_2860(): pass

    label('loc_2860')

    OP_59()
    Fade(1000)
    ChrSetPos(0x0000, 123990, -2000, 5010, 275)
    ChrSetPos(0x0001, 123990, -2000, 5010, 275)
    ChrSetPos(0x0002, 123990, -2000, 5010, 275)
    ChrSetPos(0x0003, 123990, -2000, 5010, 275)
    OP_69(0x0000, 0)
    OP_0D()
    ChrSetDirection(0x0000, 275, 0)
    Sleep(50)

    EventEnd(0x04)
    MapSetFlags(0x02000000)

    def _loc_28C5(): pass

    label('loc_28C5')

    Return()

# id: 0x000F offset: 0x28C6
@scena.Code('func_0F_28C6')
def func_0F_28C6():
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

# id: 0x0010 offset: 0x2917
@scena.Code('func_10_2917')
def func_10_2917():
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

# id: 0x0011 offset: 0x2956
@scena.Code('func_11_2956')
def func_11_2956():
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

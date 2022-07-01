import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import R4102_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R4102   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '管家菲利普'),
    TXT(0x02, '王国军士兵'),
    TXT(0x03, '王国军士兵'),
    TXT(0x04, '红色的飞艇影子'),
    TXT(0x05, '红色的飞艇影子'),
    TXT(0x06, '红色的飞艇影子'),
    TXT(0x07, '艾尔贝周游道方向'),
    TXT(0x08, '王都格兰赛尔方向'),
    TXT(0x09, '格鲁纳门方向'),
    TXT(0x0A, '火焰巨鹫'),
    TXT(0x0B, '丘陵毒蜂'),
    TXT(0x0C, '沼泽剑齿吸血魔'),
    TXT(0x0D, '丘陵毒蜂'),
    TXT(0x0E, '迅猛小鹫'),
    TXT(0x0F, '剑齿吸血魔'),
    TXT(0x10, '丘陵毒蜂'),
    TXT(0x11, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'R4102.x'
    header.mapIndex       = 1
    header.bgm            = 29
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x2C60
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
        ('ED6_DT09/CH10730._CH', 'ED6_DT09/CH10730P._CP'),
        ('ED6_DT09/CH10731._CH', 'ED6_DT09/CH10731P._CP'),
    ]

# id: 0x10002 offset: 0x152
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
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
            x                   = 152050,
            z                   = -2000,
            y                   = -76100,
            direction           = 0,
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
            x                   = 149980,
            z                   = -2000,
            y                   = -76100,
            direction           = 0,
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
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            x                   = 150880,
            z                   = -2000,
            y                   = -89600,
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
            x                   = 2420,
            z                   = 0,
            y                   = 4600,
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
            x                   = 177300,
            z                   = 0,
            y                   = 3160,
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
            x                   = 149700,
            z                   = -2000,
            y                   = -62310,
            direction           = 348,
            word_0E             = 19,
            dword_10            = 1245184,
            chipIndex           = 0,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x292
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = 47300,
            z           = 10,
            y           = -1820,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0295,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 50160,
            z           = 100,
            y           = -13420,
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
            x           = 114570,
            z           = -60,
            y           = -5920,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0295,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 140620,
            z           = -20,
            y           = 4510,
            word_0C     = 0x0000,
            word_0E     = 0x000E,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x029C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 97120,
            z           = 10,
            y           = -44670,
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
            x           = 145000,
            z           = -2040,
            y           = -47610,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0295,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x33A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 125500,
            y           = -2000,
            z           = -60800,
            range       = 130100,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFF5038,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000005,
        ),
        ScenaEventData(
            x           = 92840,
            y           = -500,
            z           = -32910,
            range       = 79430,
            dword_10    = 0x000005DC,
            dword_14    = 0xFFFF8788,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000D,
        ),
        ScenaEventData(
            x           = 85840,
            y           = -1000,
            z           = -25620,
            range       = 90190,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFFE516,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000006,
        ),
        ScenaEventData(
            x           = 167920,
            y           = -300,
            z           = 13000,
            range       = 166500,
            dword_10    = 0x000007D9,
            dword_14    = 0xFFFFECB4,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000E,
        ),
        ScenaEventData(
            x           = 156480,
            y           = -2100,
            z           = -79210,
            range       = 145460,
            dword_10    = 0xFFFFFC18,
            dword_14    = 0xFFFECF64,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000F,
        ),
        ScenaEventData(
            x           = 149700,
            y           = -3000,
            z           = -62310,
            range       = 3000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000010,
        ),
    )

# id: 0x10005 offset: 0x3FA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 84450,
            triggerZ            = 0,
            triggerY            = -13640,
            triggerRange        = 1500,
            actorX              = 84450,
            actorZ              = 1700,
            actorY              = -13640,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0011,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 87930,
            triggerZ            = 0,
            triggerY            = -13180,
            triggerRange        = 1500,
            actorX              = 87930,
            actorZ              = 1700,
            actorY              = -13180,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0012,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 88070,
            triggerZ            = 0,
            triggerY            = -25440,
            triggerRange        = 1500,
            actorX              = 88070,
            actorZ              = 1700,
            actorY              = -25440,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0013,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x466
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 0, 0x1638)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_47C',
    )

    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)

    def _loc_47C(): pass

    label('loc_47C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_498',
    )

    OP_A3(0x10F0)
    SetMapFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2D),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, 0x0008)

    def _loc_498(): pass

    label('loc_498')

    Return()

# id: 0x0001 offset: 0x499
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFF6B90, 0xFFFDA288, 0x0023003D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 5, 0x1625)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4D5',
    )

    SetChrFlags(0x0012, 0x0080)
    SetChrFlags(0x0013, 0x0080)
    SetChrFlags(0x0014, 0x0080)
    SetChrFlags(0x0015, 0x0080)
    SetChrFlags(0x0016, 0x0080)
    SetChrFlags(0x0017, 0x0080)

    def _loc_4D5(): pass

    label('loc_4D5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 0, 0x2038)),
            Expr.Return,
        ),
        'loc_4EA',
    )

    SetMapFlags(0x02000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2D),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_4EA(): pass

    label('loc_4EA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 0, 0x1638)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_502',
    )

    OP_B1('R4102_y')

    Jump('loc_51A')

    def _loc_502(): pass

    label('loc_502')

    OP_B1('R4102_n')
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    OP_71(0x0005, 0x0004)

    def _loc_51A(): pass

    label('loc_51A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Ez,
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_538',
    )

    SetChrFlags(0x0011, 0x0080)
    OP_B2(0x00, 0x05, 0x0080)

    Jump('loc_54A')

    def _loc_538(): pass

    label('loc_538')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02DF, 3, 0x16FB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_54A',
    )

    ClearChrFlags(0x0011, 0x0080)
    OP_B2(0x01, 0x05, 0x0080)

    def _loc_54A(): pass

    label('loc_54A')

    Return()

# id: 0x0002 offset: 0x54B
@scena.Code('ReInit')
def ReInit():
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
        'loc_570',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_603')

    def _loc_570(): pass

    label('loc_570')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_589',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000640)

    Jump('loc_603')

    def _loc_589(): pass

    label('loc_589')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5A2',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x0000060E)

    Jump('loc_603')

    def _loc_5A2(): pass

    label('loc_5A2')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5BB',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005DC)

    Jump('loc_603')

    def _loc_5BB(): pass

    label('loc_5BB')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5D4',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AA)

    Jump('loc_603')

    def _loc_5D4(): pass

    label('loc_5D4')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5ED',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x00000578)

    Jump('loc_603')

    def _loc_5ED(): pass

    label('loc_5ED')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_603',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x00000546)

    def _loc_603(): pass

    label('loc_603')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_618',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_603')

    def _loc_618(): pass

    label('loc_618')

    Return()

# id: 0x0003 offset: 0x619
@scena.Code('func_03_619')
def func_03_619():
    TalkBegin(0x0009)

    ChrTalk(
        0x00FE,
        (
            '现在王国军已经封锁了\n',
            '艾尔贝周游道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '任何人都\n',
            '不能过去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0009)

    Return()

# id: 0x0004 offset: 0x662
@scena.Code('func_04_662')
def func_04_662():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_6A7',
    )

    ChrTalk(
        0x00FE,
        (
            '这附近也\n',
            '未必安全。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '建议你们赶快\n',
            '回到城里去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_715')

    def _loc_6A7(): pass

    label('loc_6A7')

    ChrTalk(
        0x00FE,
        (
            '因为紧急情况的缘故，\n',
            '前面禁止任何人进入。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且这附近也\n',
            '未必安全。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '建议你们赶快\n',
            '回到城里去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_715(): pass

    label('loc_715')

    TalkEnd(0x000A)

    Return()

# id: 0x0005 offset: 0x719
@scena.Code('func_05_719')
def func_05_719():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 0, 0x1618)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_726',
    )

    Return()

    def _loc_726(): pass

    label('loc_726')

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
        'loc_74A',
    )

    Call(0, 0x000A)
    Call(0, 0x000B)
    FormationAddMember(ChrTable['玲'], 0xFF, 0xFF)
    FadeIn(0, 0)

    def _loc_74A(): pass

    label('loc_74A')

    SetChrPos(0x0008, 111020, 0, -52590, 90)

    NpcTalk(
        0x0008,
        '男性的声音',
        (
            '#0660250001V哟，你们是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    Fade(1000)
    OP_6D(127830, -2000, -52550, 0)
    OP_67(0, 9160, -10000, 0)
    OP_6B(2830, 0)
    OP_6C(224000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 120520, 0, -52830, 90)
    SetChrPos(0x0101, 128410, -2000, -51900, 270)
    SetChrPos(0x012F, 131050, -2000, -52330, 270)

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8B2',
    )

    SetChrPos(0x0105, 128500, -2000, -53020, 270)
    SetChrPos(0x00F7, 129840, -2000, -51660, 270)

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_86E',
    )

    SetChrPos(0x0104, 129840, -2000, -53020, 270)

    Jump('loc_8AF')

    def _loc_86E(): pass

    label('loc_86E')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_890',
    )

    SetChrPos(0x0107, 129840, -2000, -53020, 270)

    Jump('loc_8AF')

    def _loc_890(): pass

    label('loc_890')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8AF',
    )

    SetChrPos(0x0108, 129840, -2000, -53020, 270)

    def _loc_8AF(): pass

    label('loc_8AF')

    Jump('loc_8E5')

    def _loc_8B2(): pass

    label('loc_8B2')

    SetChrPos(0x00F7, 128500, -2000, -53020, 270)
    SetChrPos(0x00F8, 129840, -2000, -51660, 270)
    SetChrPos(0x00F9, 130000, -2000, -52830, 270)
    def _loc_8E5(): pass

    label('loc_8E5')

    OP_8E(0x0008, 126860, -2000, -52580, 2000, 0x00)
    OP_0D()

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C6D',
    )

    ChrTalk(
        0x0101,
        (
            '#0010250053V#1004F#6P咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060250054V#044F#6P啊……\n',
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
            '#0660250056V#720F好久不见。\n',
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
            '#0010250058V#1006F#6P嗯，是的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060250059V#542F#6P菲利普先生\n',
            '到王都去有事情吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0660250060V#720F是的，公爵阁下\n',
            '吩咐我出来买东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660250010V#721F……莫非你们在\n',
            '离宫遇见殿下了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250062V#1016F#6P嗯、嗯，算是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060250063V#045F#6P我们久违地\n',
            '和他寒暄了一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0660250064V#722F……看来\n',
            '他又得罪了你们吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660250014V实在是非常对不起。\n',
            '我以臣下的身份向各位道歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060250066V#047F#6P呵呵，您太客气了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060250016V#040F我听说叔叔他被软禁，\n',
            '所以感到有点担心……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060250017V不过他看来很有精神，我就放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0660250069V#720F您能够这么说，我真是高兴。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660250019V那么我就先告辞了……\n',
            '各位，失陪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F0F')

    def _loc_C6D(): pass

    label('loc_C6D')

    ChrTalk(
        0x0101,
        (
            '#0010250071V#1004F#6P咦……\n',
            '这不是菲利普先生吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0660250072V#720F艾丝蒂尔小姐。\n',
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
            '#0010250074V#1006F#6P嗯，是的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250024V菲利普先生\n',
            '到王都去办事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0660250060V#720F是的，公爵阁下\n',
            '吩咐我出来买东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660250010V#721F……莫非你们\n',
            '在离宫遇见阁下了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250078V#1025F#6P嗯、嗯，算是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0660250079V#722F……看来\n',
            '他又得罪了你们吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660250014V实在是非常对不起。\n',
            '我以臣下的身份向各位道歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250081V#1016F#6P也不是，他倒没有\n',
            '对我说过什么失礼的话。',
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
            '#0660250069V#720F您能这么说我真高兴。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660250019V那么我就先告辞了……\n',
            '各位，失陪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F0F(): pass

    label('loc_F0F')

    @scena.Lambda('lambda_0F15')
    def lambda_0F15():
        OP_8E(0x00FE, 127900, -2000, -54170, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0F15)

    @scena.Lambda('lambda_0F30')
    def lambda_0F30():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0F30')

    DispatchAsync2(0x0101, 0x0001, lambda_0F30)

    @scena.Lambda('lambda_0F41')
    def lambda_0F41():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0F41')

    DispatchAsync2(0x012F, 0x0001, lambda_0F41)

    @scena.Lambda('lambda_0F52')
    def lambda_0F52():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0F52')

    DispatchAsync2(0x00F7, 0x0001, lambda_0F52)

    @scena.Lambda('lambda_0F63')
    def lambda_0F63():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0F63')

    DispatchAsync2(0x00F8, 0x0001, lambda_0F63)

    @scena.Lambda('lambda_0F74')
    def lambda_0F74():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0F74')

    DispatchAsync2(0x00F9, 0x0001, lambda_0F74)

    WaitForThreadExit(0x0008, 0x0001)

    @scena.Lambda('lambda_0F8A')
    def lambda_0F8A():
        OP_8E(0x00FE, 142000, -2000, -54640, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0F8A)

    @scena.Lambda('lambda_0FA5')
    def lambda_0FA5():
        OP_6D(131000, -2000, -54400, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0FA5)

    @scena.Lambda('lambda_0FBD')
    def lambda_0FBD():
        OP_67(0, 8920, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0FBD)

    WaitForThreadExit(0x0008, 0x0001)
    SetChrFlags(0x0008, 0x0080)

    @scena.Lambda('lambda_0FDF')
    def lambda_0FDF():
        OP_6D(129240, -2000, -52490, 1600)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0FDF)

    @scena.Lambda('lambda_0FF7')
    def lambda_0FF7():
        OP_67(0, 8920, -10000, 1600)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0FF7)

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
            '#0010250085V#1007F#2P呼～他还是\n',
            '那么辛苦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250035V#1015F他好像从公爵小时候起\n',
            '就负责照顾公爵了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1170',
    )

    OP_8C(0x0105, 360, 400)

    ChrTalk(
        0x0105,
        (
            '#0060250087V#040F#5P听说已经照顾了\n',
            '二十年以上了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060250037V据说在那之前\n',
            '他是在亲卫队里工作的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010250089V#1004F#2P咦，真的吗！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250039V#1006F唔～果然是\n',
            '人不可貌相呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1170(): pass

    label('loc_1170')

    ChrTalk(
        0x012F,
        (
            '#0220250091V#264F#8P…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220250041V#263F刚才那位爷爷……\n',
            '绝不是个简单的人物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_11DC')
    def lambda_11DC():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_11DC)

    Sleep(50)

    @scena.Lambda('lambda_11EF')
    def lambda_11EF():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_11EF)

    Sleep(50)

    @scena.Lambda('lambda_1202')
    def lambda_1202():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_1202)

    Sleep(50)

    @scena.Lambda('lambda_1215')
    def lambda_1215():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_1215)

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_126F',
    )

    ChrTalk(
        0x0101,
        (
            '#0010250042V#1004F咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070250043V#064F怎么了？玲？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12AD')

    def _loc_126F(): pass

    label('loc_126F')

    ChrTalk(
        0x0101,
        (
            '#0010250044V#1004F咦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250045V怎么会突然这么说？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12AD(): pass

    label('loc_12AD')

    ChrTurnDirection(0x012F, 0x0101, 400)

    ChrTalk(
        0x012F,
        (
            '#0220250097V#260F#6P因为，他可以\n',
            '闭着眼睛走路嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220250047V玲绝对做不到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    OP_62(0x00F7, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_135C',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    Jump('loc_139A')

    def _loc_135C(): pass

    label('loc_135C')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1383',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    Jump('loc_139A')

    def _loc_1383(): pass

    label('loc_1383')

    OP_62(0x00F8, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    def _loc_139A(): pass

    label('loc_139A')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_13C1',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    Jump('loc_13FF')

    def _loc_13C1(): pass

    label('loc_13C1')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_13E8',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    Jump('loc_13FF')

    def _loc_13E8(): pass

    label('loc_13E8')

    OP_62(0x00F9, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    def _loc_13FF(): pass

    label('loc_13FF')

    Sleep(1500)

    ChrTalk(
        0x0101,
        (
            '#0010250048V#1016F唔，我想\n',
            '那不是闭着眼睛，\n',
            '应该是眯着眼睛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250049V#1006F而且他吃惊的时候\n',
            '眼睛还是会睁大的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#0220250101V#264F#6P哎呀？是吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220250051V#261F呵呵，我也好想\n',
            '看看他吃惊的样子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    OP_A2(0x1618)
    EventEnd(0x00)

    Return()

# id: 0x0006 offset: 0x14E8
@scena.Code('func_06_14E8')
def func_06_14E8():
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
        'loc_14FF',
    )

    Return()

    def _loc_14FF(): pass

    label('loc_14FF')

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
        'loc_151F',
    )

    Call(0, 0x000A)
    Call(0, 0x000C)
    FadeIn(0, 0)

    def _loc_151F(): pass

    label('loc_151F')

    OP_20(0x000007D0)
    Fade(1000)
    SetChrPos(0x0101, 87670, 0, -18210, 270)
    SetChrPos(0x0102, 87650, 0, -19540, 270)
    SetChrPos(0x00F8, 89210, 0, -18030, 270)
    SetChrPos(0x00F9, 89310, 0, -19440, 270)
    OP_6D(89370, 0, -19860, 0)
    OP_67(0, 7200, -10000, 0)
    OP_6B(1770, 0)
    OP_6C(134000, 0)
    OP_6E(431, 0)
    OP_0D()
    CreateThread(0x0101, 0x03, 0x00, 0x0007)
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
        'loc_1602',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x26, 0x26, 0x000000FA, 0x01)

    Jump('loc_1636')

    def _loc_1602(): pass

    label('loc_1602')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1624',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x26, 0x26, 0x000000FA, 0x01)

    Jump('loc_1636')

    def _loc_1624(): pass

    label('loc_1624')

    OP_62(0x00F8, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)

    def _loc_1636(): pass

    label('loc_1636')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1658',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x26, 0x26, 0x000000FA, 0x01)

    Jump('loc_168C')

    def _loc_1658(): pass

    label('loc_1658')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_167A',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x26, 0x26, 0x000000FA, 0x01)

    Jump('loc_168C')

    def _loc_167A(): pass

    label('loc_167A')

    OP_62(0x00F9, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)

    def _loc_168C(): pass

    label('loc_168C')

    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010380001V#1004F#5P咦……这是？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1704',
    )

    ChrTalk(
        0x0106,
        (
            '#0050380002V#052F#5P什么啊，这不是\n',
            '飞船的引擎声吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_178F')

    def _loc_1704(): pass

    label('loc_1704')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1750',
    )

    ChrTalk(
        0x0103,
        (
            '#0030380003V#023F#5P什么啊，这不是\n',
            '飞船的引擎声吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_178F')

    def _loc_1750(): pass

    label('loc_1750')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_178F',
    )

    ChrTalk(
        0x0108,
        (
            '#0080380004V#073F#5P这是……\n',
            '飞船的引擎声？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_178F(): pass

    label('loc_178F')

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
        'loc_17DF',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x18, 0x1B, 0x000000FA, 0x00)

    Jump('loc_1813')

    def _loc_17DF(): pass

    label('loc_17DF')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1801',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)

    Jump('loc_1813')

    def _loc_1801(): pass

    label('loc_1801')

    OP_62(0x00F8, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)

    def _loc_1813(): pass

    label('loc_1813')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_183A',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x18, 0x1B, 0x000000FA, 0x00)

    Jump('loc_186E')

    def _loc_183A(): pass

    label('loc_183A')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_185C',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)

    Jump('loc_186E')

    def _loc_185C(): pass

    label('loc_185C')

    OP_62(0x00F9, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)

    def _loc_186E(): pass

    label('loc_186E')

    Sleep(1500)

    OP_63(0x0101)
    OP_63(0x0102)
    OP_63(0x00F8)
    OP_63(0x00F9)
    Sleep(200)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_18E3',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_1921')

    def _loc_18E3(): pass

    label('loc_18E3')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_190A',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_1921')

    def _loc_190A(): pass

    label('loc_190A')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_1921(): pass

    label('loc_1921')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_194D',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_198B')

    def _loc_194D(): pass

    label('loc_194D')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1974',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_198B')

    def _loc_1974(): pass

    label('loc_1974')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_198B(): pass

    label('loc_198B')

    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010380005V#1020F#5P等、等等！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A03',
    )

    ChrTalk(
        0x0107,
        (
            '#0070380006V#065F#5P这、这种时候\n',
            '还能飞的飞船是……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A90')

    def _loc_1A03(): pass

    label('loc_1A03')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A4B',
    )

    ChrTalk(
        0x0108,
        (
            '#0080380007V#076F#5P这种时候\n',
            '还能飞的飞船是……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A90')

    def _loc_1A4B(): pass

    label('loc_1A4B')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A90',
    )

    ChrTalk(
        0x0103,
        (
            '#0030380008V#024F#5P这种时候\n',
            '还能飞的飞船是……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A90(): pass

    label('loc_1A90')

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_8C(0x0102, 135, 500)

    ChrTalk(
        0x0102,
        (
            '#0020380009V#1046F#6P是那个……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1AE0')
    def lambda_1AE0():
        OP_6D(97800, 0, -23000, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1AE0)

    @scena.Lambda('lambda_1AF8')
    def lambda_1AF8():
        OP_67(0, 12960, -10000, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1AF8)

    @scena.Lambda('lambda_1B10')
    def lambda_1B10():
        OP_6B(2160, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1B10)

    @scena.Lambda('lambda_1B20')
    def lambda_1B20():
        OP_6C(111000, 2500)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_1B20)

    @scena.Lambda('lambda_1B30')
    def lambda_1B30():
        OP_6E(460, 2500)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_1B30)

    @scena.Lambda('lambda_1B40')
    def lambda_1B40():
        OP_8C(0x00FE, 135, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1B40)

    Sleep(50)

    @scena.Lambda('lambda_1B53')
    def lambda_1B53():
        OP_8C(0x00FE, 135, 500)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_1B53)

    Sleep(50)

    @scena.Lambda('lambda_1B66')
    def lambda_1B66():
        OP_8C(0x00FE, 135, 500)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_1B66)

    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x00100000)
    OP_A2(0x10FF)
    OP_A2(0x10F9)
    NewScene('ED6_DT21/E0810._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0007 offset: 0x1B93
@scena.Code('func_07_1B93')
def func_07_1B93():
    OP_22(0x0079, 0x01, 0x32)
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

# id: 0x0008 offset: 0x1C20
@scena.Code('func_08_1C20')
def func_08_1C20():
    EventBegin(0x00)
    ClearMapFlags(0x00100000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1C45',
    )

    Call(0, 0x000A)
    Call(0, 0x000C)
    FadeIn(0, 0)

    def _loc_1C45(): pass

    label('loc_1C45')

    OP_22(0x0079, 0x01, 0x64)
    SetChrPos(0x0101, 88010, 0, -18190, 135)
    SetChrPos(0x0102, 87420, 0, -19640, 135)
    SetChrPos(0x00F8, 89730, 0, -18750, 135)
    SetChrPos(0x00F9, 89300, 0, -20100, 135)
    OP_6D(88080, 0, -19230, 0)
    OP_67(0, 8890, -10000, 0)
    OP_6B(2810, 0)
    OP_6C(260000, 0)
    OP_6E(262, 0)
    OP_72(0x0000, 0x0004)
    OP_72(0x0001, 0x0004)
    OP_72(0x0002, 0x0004)
    OP_A1(0x000B, 0x0000)
    OP_A1(0x000C, 0x0001)
    OP_A1(0x000D, 0x0002)
    SetChrPos(0x000B, 104090, 2000, -30210, 315)
    SetChrPos(0x000C, 109090, 2000, -25210, 315)
    SetChrPos(0x000D, 99090, 2000, -35210, 315)
    ChrTurnDirection(0x0101, 0x000B, 0)
    ChrTurnDirection(0x0102, 0x000B, 0)
    ChrTurnDirection(0x00F8, 0x000B, 0)
    ChrTurnDirection(0x00F9, 0x000B, 0)
    FadeIn(1000, 0)
    OP_0D()

    @scena.Lambda('lambda_1D48')
    def lambda_1D48():
        ChrTurnDirection(0x00FE, 0x000B, 400)
        Yield()

        Jump('lambda_1D48')

    DispatchAsync2(0x0101, 0x0003, lambda_1D48)

    @scena.Lambda('lambda_1D59')
    def lambda_1D59():
        ChrTurnDirection(0x00FE, 0x000B, 400)
        Yield()

        Jump('lambda_1D59')

    DispatchAsync2(0x0102, 0x0003, lambda_1D59)

    @scena.Lambda('lambda_1D6A')
    def lambda_1D6A():
        ChrTurnDirection(0x00FE, 0x000B, 400)
        Yield()

        Jump('lambda_1D6A')

    DispatchAsync2(0x00F8, 0x0003, lambda_1D6A)

    @scena.Lambda('lambda_1D7B')
    def lambda_1D7B():
        ChrTurnDirection(0x00FE, 0x000B, 400)
        Yield()

        Jump('lambda_1D7B')

    DispatchAsync2(0x00F9, 0x0003, lambda_1D7B)

    @scena.Lambda('lambda_1D8C')
    def lambda_1D8C():
        OP_90(0x00FE, -30000, 0, 30000, 30000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1D8C)

    Sleep(1000)

    @scena.Lambda('lambda_1DAC')
    def lambda_1DAC():
        OP_90(0x00FE, -30000, 0, 30000, 30000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1DAC)

    Sleep(1000)

    @scena.Lambda('lambda_1DCC')
    def lambda_1DCC():
        OP_90(0x00FE, -30000, 0, 30000, 30000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1DCC)

    WaitForThreadExit(0x000D, 0x0001)
    CreateThread(0x0102, 0x02, 0x00, 0x0009)
    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    TerminateThread(0x0101, 0x03)
    TerminateThread(0x0102, 0x03)
    TerminateThread(0x00F8, 0x03)
    TerminateThread(0x00F9, 0x03)

    ChrTalk(
        0x0101,
        (
            '#0010380010V#1020F#5P『结社』的飞艇……\n',
            '为、为什么会出现在这里！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020380011V#1046F#5P不好……\n',
            '那里是王都的方向！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1EDA',
    )

    ChrTalk(
        0x0106,
        (
            '#0050380012V#057F#6P这可不是闹着玩的！\n',
            '我们赶紧追上去吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F58')

    def _loc_1EDA(): pass

    label('loc_1EDA')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1F22',
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

    Jump('loc_1F58')

    def _loc_1F22(): pass

    label('loc_1F22')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1F58',
    )

    ChrTalk(
        0x0108,
        (
            '#0080380014V#076F#6P赶快追上去吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F58(): pass

    label('loc_1F58')

    OP_A2(0x2038)
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
    SetMapFlags(0x02000000)

    Return()

# id: 0x0009 offset: 0x1FA5
@scena.Code('func_09_1FA5')
def func_09_1FA5():
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

# id: 0x000A offset: 0x2039
@scena.Code('func_0A_2039')
def func_0A_2039():
    FadeOut(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
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
        (0x00000000, 'loc_20B3'),
        (0x00000001, 'loc_20B9'),
        (-1, 'loc_20BF'),
    )

    def _loc_20B3(): pass

    label('loc_20B3')

    OP_A2(0x1200)

    Jump('loc_20BF')

    def _loc_20B9(): pass

    label('loc_20B9')

    OP_A2(0x1201)

    Jump('loc_20BF')

    def _loc_20BF(): pass

    label('loc_20BF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_20CD',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_20D1')

    def _loc_20CD(): pass

    label('loc_20CD')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_20D1(): pass

    label('loc_20D1')

    Return()

# id: 0x000B offset: 0x20D2
@scena.Code('func_0B_20D2')
def func_0B_20D2():
    ClearMapFlags(0x00000001)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_2115',
    )

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            0x0000,
            0x0002,
            0x00FF,
            0x00FF,
        ),
        (
            0x0003,
            0x0004,
            0x0006,
            0x0007,
            0xFFFF,
        ),
    )

    Jump('loc_2133')

    def _loc_2115(): pass

    label('loc_2115')

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            0x0000,
            0x0005,
            0x00FF,
            0x00FF,
        ),
        (
            0x0003,
            0x0004,
            0x0006,
            0x0007,
            0xFFFF,
        ),
    )

    def _loc_2133(): pass

    label('loc_2133')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0x00000000)
    Sleep(1000)

    Return()

# id: 0x000C offset: 0x2153
@scena.Code('func_0C_2153')
def func_0C_2153():
    ClearMapFlags(0x00000001)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            0x0000,
            0x0001,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
            0x0006,
            0x0007,
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
    OP_69(0x0000, 0x00000000)
    Sleep(1000)

    Return()

# id: 0x000D offset: 0x21AC
@scena.Code('func_0D_21AC')
def func_0D_21AC():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 6, 0x1636)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 7, 0x1637)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_221E',
    )

    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0010260968V#1002F（格鲁纳门在东边！\n',
            '……………要快点才行！！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    SetChrPos(0x0101, 84130, 0, -28960, 0)
    OP_0D()
    Sleep(50)

    EventEnd(0x04)

    def _loc_221E(): pass

    label('loc_221E')

    Return()

# id: 0x000E offset: 0x221F
@scena.Code('func_0E_221F')
def func_0E_221F():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 2, 0x203A)),
            Expr.Return,
        ),
        'loc_23F3',
    )

    EventBegin(0x01)

    Switch(
        (
            (Expr.PushValueByIndex, 0xA),
            Expr.Return,
        ),
        (0x00000000, 'loc_2248'),
        (0x00000001, 'loc_2288'),
        (0x00000002, 'loc_22CC'),
        (0x00000005, 'loc_230B'),
        (0x00000007, 'loc_234A'),
        (0x00000006, 'loc_238B'),
        (-1, 'loc_23D0'),
    )

    def _loc_2248(): pass

    label('loc_2248')

    ChrTalk(
        0x0101,
        (
            '#0010380015V#1002F没时间去别的地方了。\n',
            '快点前往王都吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23D0')

    def _loc_2288(): pass

    label('loc_2288')

    ChrTalk(
        0x0102,
        (
            '#0020380016V#1042F没时间去别的地方了。\n',
            '要尽快前往王都才行！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23D0')

    def _loc_22CC(): pass

    label('loc_22CC')

    ChrTalk(
        0x0103,
        (
            '#0030380017V#022F没时间去别的地方了。\n',
            '赶紧前往王都吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23D0')

    def _loc_230B(): pass

    label('loc_230B')

    ChrTalk(
        0x0106,
        (
            '#0050380018V#057F没时间去别的地方了。\n',
            '赶紧前往王都吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23D0')

    def _loc_234A(): pass

    label('loc_234A')

    ChrTalk(
        0x0108,
        (
            '#0080380019V#072F没时间去别的地方了啊。\n',
            '赶紧前往王都吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23D0')

    def _loc_238B(): pass

    label('loc_238B')

    ChrTalk(
        0x0107,
        (
            '#0070380020V#062F没时间去别的地方了呢。\n',
            '要赶紧前往王都才行！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23D0')

    def _loc_23D0(): pass

    label('loc_23D0')

    OP_90(0x0000, -1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    SetMapFlags(0x02000000)

    Jump('loc_259C')

    def _loc_23F3(): pass

    label('loc_23F3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 0, 0x2038)),
            Expr.Return,
        ),
        'loc_259C',
    )

    EventBegin(0x01)

    Switch(
        (
            (Expr.PushValueByIndex, 0xA),
            Expr.Return,
        ),
        (0x00000000, 'loc_241C'),
        (0x00000001, 'loc_2458'),
        (0x00000002, 'loc_2494'),
        (0x00000005, 'loc_24CD'),
        (0x00000007, 'loc_2506'),
        (0x00000006, 'loc_2539'),
        (-1, 'loc_257C'),
    )

    def _loc_241C(): pass

    label('loc_241C')

    ChrTalk(
        0x0101,
        (
            '#0010380021V#1002F不，不是这边！\n',
            '……赶紧去王都吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_257C')

    def _loc_2458(): pass

    label('loc_2458')

    ChrTalk(
        0x0102,
        (
            '#0020380022V#1042F不，不是这边！\n',
            '……赶紧去王都吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_257C')

    def _loc_2494(): pass

    label('loc_2494')

    ChrTalk(
        0x0103,
        (
            '#0030380023V#022F不对，不是这边！\n',
            '赶紧去王都吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_257C')

    def _loc_24CD(): pass

    label('loc_24CD')

    ChrTalk(
        0x0106,
        (
            '#0050380024V#057F不对，不是这边！\n',
            '赶紧去王都吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_257C')

    def _loc_2506(): pass

    label('loc_2506')

    ChrTalk(
        0x0108,
        (
            '#0080380025V#072F不是这边。\n',
            '赶紧去王都吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_257C')

    def _loc_2539(): pass

    label('loc_2539')

    ChrTalk(
        0x0107,
        (
            '#0070380026V#065F那个那个……不是这边。\n',
            '要赶紧去王都才行！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_257C')

    def _loc_257C(): pass

    label('loc_257C')

    OP_90(0x0000, -1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    SetMapFlags(0x02000000)

    def _loc_259C(): pass

    label('loc_259C')

    Return()

# id: 0x000F offset: 0x259D
@scena.Code('func_0F_259D')
def func_0F_259D():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 2, 0x203A)),
            Expr.Return,
        ),
        'loc_278E',
    )

    EventBegin(0x01)

    Switch(
        (
            (Expr.PushValueByIndex, 0xA),
            Expr.Return,
        ),
        (0x00000000, 'loc_25C6'),
        (0x00000001, 'loc_2600'),
        (0x00000002, 'loc_263A'),
        (0x00000005, 'loc_2673'),
        (0x00000007, 'loc_26AC'),
        (0x00000006, 'loc_26E7'),
        (-1, 'loc_2726'),
    )

    def _loc_25C6(): pass

    label('loc_25C6')

    ChrTalk(
        0x0101,
        (
            '#0010380015V#1002F没时间去别处了。\n',
            '赶紧去王都吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2726')

    def _loc_2600(): pass

    label('loc_2600')

    ChrTalk(
        0x0102,
        (
            '#0020380016V#1042F没时间去别处了。\n',
            '赶紧去王都吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2726')

    def _loc_263A(): pass

    label('loc_263A')

    ChrTalk(
        0x0103,
        (
            '#0030380017V#022F没时间去别处了。\n',
            '赶紧去王都吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2726')

    def _loc_2673(): pass

    label('loc_2673')

    ChrTalk(
        0x0106,
        (
            '#0050380018V#057F没时间去别处了。\n',
            '赶紧去王都吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2726')

    def _loc_26AC(): pass

    label('loc_26AC')

    ChrTalk(
        0x0108,
        (
            '#0080380019V#072F没时间去别处了啊。\n',
            '赶紧去王都吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2726')

    def _loc_26E7(): pass

    label('loc_26E7')

    ChrTalk(
        0x0107,
        (
            '#0070380020V#062F没时间去别处了呢。\n',
            '要赶紧去王都才行！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2726')

    def _loc_2726(): pass

    label('loc_2726')

    OP_59()
    Fade(1000)
    SetChrPos(0x0000, 151000, -2000, -74190, 0)
    SetChrPos(0x0001, 151000, -2000, -74190, 0)
    SetChrPos(0x0002, 151000, -2000, -74190, 0)
    SetChrPos(0x0003, 151000, -2000, -74190, 0)
    OP_69(0x0000, 0x00000000)
    OP_0D()
    OP_8C(0x0000, 0, 0)
    Sleep(50)

    EventEnd(0x04)
    SetMapFlags(0x02000000)

    Jump('loc_297C')

    def _loc_278E(): pass

    label('loc_278E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 0, 0x2038)),
            Expr.Return,
        ),
        'loc_297C',
    )

    EventBegin(0x01)

    Switch(
        (
            (Expr.PushValueByIndex, 0xA),
            Expr.Return,
        ),
        (0x00000000, 'loc_27B7'),
        (0x00000001, 'loc_27F3'),
        (0x00000002, 'loc_282F'),
        (0x00000005, 'loc_2868'),
        (0x00000007, 'loc_28A1'),
        (0x00000006, 'loc_28D4'),
        (-1, 'loc_2917'),
    )

    def _loc_27B7(): pass

    label('loc_27B7')

    ChrTalk(
        0x0101,
        (
            '#0010380021V#1002F不，不是这边！\n',
            '……赶紧去王都吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2917')

    def _loc_27F3(): pass

    label('loc_27F3')

    ChrTalk(
        0x0102,
        (
            '#0020380022V#1042F不，不是这边！\n',
            '……赶紧去王都吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2917')

    def _loc_282F(): pass

    label('loc_282F')

    ChrTalk(
        0x0103,
        (
            '#0030380023V#022F不对，不是这边！\n',
            '赶紧去王都吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2917')

    def _loc_2868(): pass

    label('loc_2868')

    ChrTalk(
        0x0106,
        (
            '#0050380024V#057F不对，不是这边！\n',
            '赶紧去王都吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2917')

    def _loc_28A1(): pass

    label('loc_28A1')

    ChrTalk(
        0x0108,
        (
            '#0080380025V#072F不是这边。\n',
            '赶紧去王都吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2917')

    def _loc_28D4(): pass

    label('loc_28D4')

    ChrTalk(
        0x0107,
        (
            '#0070380026V#065F那个那个……不是这边。\n',
            '要赶紧去王都才行！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2917')

    def _loc_2917(): pass

    label('loc_2917')

    OP_59()
    Fade(1000)
    SetChrPos(0x0000, 151000, -2000, -74190, 0)
    SetChrPos(0x0001, 151000, -2000, -74190, 0)
    SetChrPos(0x0002, 151000, -2000, -74190, 0)
    SetChrPos(0x0003, 151000, -2000, -74190, 0)
    OP_69(0x0000, 0x00000000)
    OP_0D()
    OP_8C(0x0000, 0, 0)
    Sleep(50)

    EventEnd(0x04)
    SetMapFlags(0x02000000)

    def _loc_297C(): pass

    label('loc_297C')

    Return()

# id: 0x0010 offset: 0x297D
@scena.Code('func_10_297D')
def func_10_297D():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02DF, 3, 0x16FB)),
            Expr.Return,
        ),
        'loc_2985',
    )

    Return()

    def _loc_2985(): pass

    label('loc_2985')

    EventBegin(0x01)

    ExecExpressionWithValue(
        0x0000,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0001,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0002,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0003,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0004,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0005,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0006,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0007,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrSubChip(0x0000, 0)
    SetChrSubChip(0x0001, 0)
    SetChrSubChip(0x0002, 0)
    SetChrSubChip(0x0003, 0)
    SetChrSubChip(0x0004, 0)
    SetChrSubChip(0x0005, 0)
    SetChrSubChip(0x0006, 0)
    SetChrSubChip(0x0007, 0)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '大型魔兽正在四处游荡中。',
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
        0,
        (
            TXT(0x00, '【消灭它】\n'),
            TXT(0x01, '【放弃】\n'),
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
        (0x00000001, 'loc_2A6A'),
        (-1, 'loc_2A8D'),
    )

    def _loc_2A6A(): pass

    label('loc_2A6A')

    Fade(500)
    OP_89(0x0000, 145940, -2000, -57070, 143)
    OP_69(0x0000, 0x00000000)
    OP_30(0x01)
    OP_0D()
    EventEnd(0x00)

    Return()

    def _loc_2A8D(): pass

    label('loc_2A8D')

    Battle(0x00000EE5, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x01)
    OP_89(0x0000, 145940, -2000, -57070, 143)
    OP_69(0x0000, 0x00000000)
    OP_30(0x01)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000002, 'loc_2AC6'),
        (0x00000001, 'loc_2AC9'),
        (-1, 'loc_2ACC'),
    )

    def _loc_2AC6(): pass

    label('loc_2AC6')

    EventEnd(0x00)

    Return()

    def _loc_2AC9(): pass

    label('loc_2AC9')

    OP_B4(0x00)

    Return()

    def _loc_2ACC(): pass

    label('loc_2ACC')

    EventBegin(0x01)
    SetChrFlags(0x0011, 0x0080)
    OP_B2(0x00, 0x05, 0x0080)
    OP_0D()
    Sleep(400)

    OP_22(0x0017, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '消灭了通缉魔兽！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_A2(0x16FB)
    OP_28(0x00A9, 0x04, 0x10)
    OP_28(0x00A9, 0x04, 0x02)
    OP_28(0x00A9, 0x01, 0x0001)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x00)

    Return()

# id: 0x0011 offset: 0x2B38
@scena.Code('func_11_2B38')
def func_11_2B38():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '西　王都格兰赛尔　１６８塞尔矩',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0012 offset: 0x2B89
@scena.Code('func_12_2B89')
def func_12_2B89():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '东　洛连特市　　　３６８塞尔矩\n',
            '　　格鲁纳门',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0013 offset: 0x2BE7
@scena.Code('func_13_2BE7')
def func_13_2BE7():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '南　艾尔贝离宫　　２５６塞尔矩',
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

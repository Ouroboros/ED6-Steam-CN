import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import R3105_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R3105   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '霍夫曼上尉'),
    TXT(0x02, '士兵里诺'),
    TXT(0x03, '蔡斯方向'),
    TXT(0x04, '沃尔费堡垒方向'),
    TXT(0x05, '红莲之塔方向'),
    TXT(0x06, ''),
    TXT(0x07, ''),
    TXT(0x08, ''),
    TXT(0x09, ''),
    TXT(0x0A, ''),
    TXT(0x0B, ''),
    TXT(0x0C, ''),
    TXT(0x0D, ''),
    TXT(0x0E, ''),
    TXT(0x0F, ''),
    TXT(0x10, ''),
    TXT(0x11, ''),
    TXT(0x12, ''),
    TXT(0x13, ''),
    TXT(0x14, ''),
    TXT(0x15, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'R3105.x'
    header.mapIndex       = 144
    header.bgm            = 29
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1DD3
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
        ('ED6_DT09/CH10610._CH', 'ED6_DT09/CH10610P._CP'),
        ('ED6_DT09/CH10611._CH', 'ED6_DT09/CH10611P._CP'),
        ('ED6_DT09/CH10080._CH', 'ED6_DT09/CH10080P._CP'),
        ('ED6_DT09/CH10081._CH', 'ED6_DT09/CH10081P._CP'),
        ('ED6_DT09/CH10120._CH', 'ED6_DT09/CH10120P._CP'),
        ('ED6_DT09/CH10121._CH', 'ED6_DT09/CH10121P._CP'),
        ('ED6_DT09/CH10140._CH', 'ED6_DT09/CH10140P._CP'),
        ('ED6_DT09/CH10141._CH', 'ED6_DT09/CH10141P._CP'),
        ('ED6_DT09/CH10620._CH', 'ED6_DT09/CH10620P._CP'),
        ('ED6_DT09/CH10621._CH', 'ED6_DT09/CH10621P._CP'),
        ('ED6_DT09/CH10600._CH', 'ED6_DT09/CH10600P._CP'),
        ('ED6_DT09/CH10601._CH', 'ED6_DT09/CH10601P._CP'),
        ('ED6_DT09/CH10400._CH', 'ED6_DT09/CH10400P._CP'),
        ('ED6_DT09/CH10401._CH', 'ED6_DT09/CH10401P._CP'),
        ('ED6_DT09/CH11210._CH', 'ED6_DT09/CH11210P._CP'),
        ('ED6_DT09/CH11211._CH', 'ED6_DT09/CH11211P._CP'),
        ('ED6_DT09/CH11250._CH', 'ED6_DT09/CH11250P._CP'),
        ('ED6_DT09/CH11251._CH', 'ED6_DT09/CH11251P._CP'),
        ('ED6_DT07/CH01310._CH', 'ED6_DT07/CH01310P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
    ]

# id: 0x10002 offset: 0x14A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 1400,
            z                   = -40,
            y                   = 9260,
            direction           = 135,
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
            x                   = 2490,
            z                   = -30,
            y                   = 7960,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = -74130,
            z                   = 0,
            y                   = 3100,
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
            x                   = 64319,
            z                   = 10,
            y                   = -52920,
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
            x                   = 10040,
            z                   = -130,
            y                   = 67800,
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

# id: 0x10003 offset: 0x1EA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -36940,
            z           = -10,
            y           = 10890,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -28070,
            z           = 80,
            y           = 10280,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -17490,
            z           = 0,
            y           = -1540,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 4150,
            z           = -60,
            y           = 15540,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 32970,
            z           = -30,
            y           = 25660,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 26690,
            z           = 50,
            y           = 5570,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 13500,
            z           = -20,
            y           = -4890,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 34620,
            z           = -50,
            y           = -10530,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 37440,
            z           = -50,
            y           = -24530,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 15930,
            z           = 0,
            y           = -38970,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -35920,
            z           = -20,
            y           = -35400,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -29740,
            z           = -110,
            y           = -7150,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -19490,
            z           = 0,
            y           = -17710,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 12390,
            z           = 50,
            y           = -16010,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -5230,
            z           = 0,
            y           = -27150,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x020C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x38E
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x38E
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -3130,
            triggerZ            = 30,
            triggerY            = -11320,
            triggerRange        = 1000,
            actorX              = -3130,
            actorZ              = 30,
            actorY              = -10750,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 13630,
            triggerZ            = 0,
            triggerY            = 35620,
            triggerRange        = 1500,
            actorX              = 13630,
            actorZ              = 1200,
            actorY              = 35620,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000D,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 36850,
            triggerZ            = 80,
            triggerY            = 17250,
            triggerRange        = 1000,
            actorX              = 33720,
            actorZ              = -1000,
            actorY              = 13980,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000E,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x3FA
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_428',
    )

    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_428',
    )

    SetChrPos(0x0009, 5620, 20, -7270, 45)

    def _loc_428(): pass

    label('loc_428')

    OP_A2(0x0000)

    Return()

# id: 0x0001 offset: 0x42C
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFE0048, 0xFFFE13D0, 0x0023002F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x006E, 0x00, 0x08)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x006E, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x006E, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4E9',
    )

    If(
        (
            (Expr.GetChrWork, 0x104, 0x1C),
            (Expr.PushLong, 0x5B),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4E9',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4E9',
    )

    OP_CE(
        0x00,
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0xA),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_498',
    )

    OP_28(0x006E, 0x01, 0x0040)

    Jump('loc_4E9')

    def _loc_498(): pass

    label('loc_498')

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4AD',
    )

    OP_28(0x006E, 0x01, 0x0020)

    Jump('loc_4E9')

    def _loc_4AD(): pass

    label('loc_4AD')

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4C2',
    )

    OP_28(0x006E, 0x01, 0x0010)

    Jump('loc_4E9')

    def _loc_4C2(): pass

    label('loc_4C2')

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4D7',
    )

    OP_28(0x006E, 0x01, 0x0008)

    Jump('loc_4E9')

    def _loc_4D7(): pass

    label('loc_4D7')

    If(
        (
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4E9',
    )

    OP_28(0x006E, 0x01, 0x0004)

    def _loc_4E9(): pass

    label('loc_4E9')

    OP_A3(0x0000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A0, 6, 0x1506)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4FE',
    )

    OP_6F(0x0001, 0)

    Jump('loc_505')

    def _loc_4FE(): pass

    label('loc_4FE')

    OP_6F(0x0001, 60)

    def _loc_505(): pass

    label('loc_505')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_52A',
    )

    SetChrFlags(0x000F, 0x0080)
    SetChrFlags(0x0010, 0x0080)
    SetChrFlags(0x0012, 0x0080)
    SetChrFlags(0x0013, 0x0080)
    SetChrFlags(0x001A, 0x0080)

    def _loc_52A(): pass

    label('loc_52A')

    Return()

# id: 0x0002 offset: 0x52B
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_540',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('ReInit')

    def _loc_540(): pass

    label('loc_540')

    Return()

# id: 0x0003 offset: 0x541
@scena.Code('func_03_541')
def func_03_541():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0401, 7, 0x200F)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0401, 4, 0x200C)),
            (Expr.TestScenaFlags, ScenaFlag(0x0401, 6, 0x200E)),
            Expr.Or,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_55B',
    )

    Call(0, 0x0006)

    Jump('loc_8A1')

    def _loc_55B(): pass

    label('loc_55B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_72F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0419, 6, 0x20CE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6CC',
    )

    ChrTalk(
        0x00FE,
        (
            '呀，各位游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '温泉的修理\n',
            '还顺利吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F啊，嗯，托您的福。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F顺利解决了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '非常感谢您的帮助\n',
            '真是谢谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哦哦，很顺利吗。\n',
            '那就最好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样小的工作成果\n',
            '说不定能让市民们感到安心呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们王国军也会致力于\n',
            '治安的维持和地区的稳定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今后让我们互相配合，\n',
            '共同去克服这次的难关吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F嗯……明白了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x20CE)

    Jump('loc_72C')

    def _loc_6CC(): pass

    label('loc_6CC')

    ChrTalk(
        0x00FE,
        (
            '温泉的修理……\n',
            '成功是再好不过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，今后让我们互相配合，\n',
            '共同去克服这次的难关吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_72C(): pass

    label('loc_72C')

    Jump('loc_8A1')

    def _loc_72F(): pass

    label('loc_72F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0401, 7, 0x200F)),
            Expr.Return,
        ),
        'loc_799',
    )

    ChrTalk(
        0x00FE,
        (
            '正是在这种状况下\n',
            '心情的平和才显得重要。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '亚尔摩温泉的修复工作，\n',
            '请诸位务必要多加努力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8A1')

    def _loc_799(): pass

    label('loc_799')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_8A1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_84F',
    )

    ChrTalk(
        0x00FE,
        (
            '在前往蔡斯的途中，\n',
            '突然变得无法操纵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最后总算将飞艇\n',
            '降落在这片平原上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从状况看来，似乎是\n',
            '导力器无法运作了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……不过，到底发生了什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    Jump('loc_8A1')

    def _loc_84F(): pass

    label('loc_84F')

    ChrTalk(
        0x00FE,
        (
            '在前往蔡斯的途中，\n',
            '突然变得无法操纵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最后总算将飞艇\n',
            '降落在这片平原上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8A1(): pass

    label('loc_8A1')

    TalkEnd(0x0008)

    Return()

# id: 0x0004 offset: 0x8A5
@scena.Code('func_04_8A5')
def func_04_8A5():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0401, 7, 0x200F)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0401, 4, 0x200C)),
            (Expr.TestScenaFlags, ScenaFlag(0x0401, 6, 0x200E)),
            Expr.Or,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_8BF',
    )

    Call(0, 0x0006)

    Jump('loc_AE6')

    def _loc_8BF(): pass

    label('loc_8BF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_950',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_92A',
    )

    ChrTalk(
        0x00FE,
        (
            '为保险起见，\n',
            '目前正在检查机体。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎，说白了\n',
            '也就是打发时间而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0009, 45, 400)
    SetChrFlags(0x0009, 0x0010)
    OP_A2(0x0002)

    Jump('loc_94D')

    def _loc_92A(): pass

    label('loc_92A')

    ChrTalk(
        0x00FE,
        (
            '哼哼……\n',
            '支架好像没有异常啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_94D(): pass

    label('loc_94D')

    Jump('loc_AE6')

    def _loc_950(): pass

    label('loc_950')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0401, 7, 0x200F)),
            Expr.Return,
        ),
        'loc_A12',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9C7',
    )

    ChrTalk(
        0x00FE,
        (
            '亚尔摩温泉吗～\n',
            '好久没去了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，到时候真想\n',
            '悠闲地泡泡澡啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，修理要加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    Jump('loc_A0F')

    def _loc_9C7(): pass

    label('loc_9C7')

    ChrTalk(
        0x00FE,
        (
            '亚尔摩温泉吗～\n',
            '好久没去了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，到时候真想\n',
            '悠闲地泡泡澡啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A0F(): pass

    label('loc_A0F')

    Jump('loc_AE6')

    def _loc_A12(): pass

    label('loc_A12')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_AE6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A96',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，总算\n',
            '平安着陆了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '结果偏偏是降落在\n',
            '托兰特平原正中央啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '救援部队要过来\n',
            '恐怕还得等很久呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    Jump('loc_AE6')

    def _loc_A96(): pass

    label('loc_A96')

    ChrTalk(
        0x00FE,
        (
            '着陆的地方偏偏\n',
            '托兰特平原正中央啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '救援部队要过来\n',
            '恐怕还得等很久呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AE6(): pass

    label('loc_AE6')

    TalkEnd(0x0009)

    Return()

# id: 0x0005 offset: 0xAEA
@scena.Code('func_05_AEA')
def func_05_AEA():
    UnlockAchievement(0x02, 0xEF, 0x01, 0x00)
    SetMapFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A0, 6, 0x1506)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C09',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0001, 0x0000001E)
    OP_73(0x0001)
    OP_6F(0x0001, 30)
    AddSepith(0x00, 0x000A)
    AddSepith(0x01, 0x000A)
    AddSepith(0x02, 0x000A)
    AddSepith(0x03, 0x000A)
    AddSepith(0x04, 0x000A)
    AddSepith(0x05, 0x000A)
    AddSepith(0x06, 0x000A)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了\n',
            (TxtCtl.SetColor, 0x2),
            '#56I地之耀晶片×１０\n',
            (TxtCtl.SetColor, 0x2),
            '#57I水之耀晶片×１０\n',
            (TxtCtl.SetColor, 0x2),
            '#58I火之耀晶片×１０\n',
            (TxtCtl.SetColor, 0x2),
            '#59I风之耀晶片×１０\n',
            (TxtCtl.SetColor, 0x2),
            '#62I时之耀晶片×１０\n',
            (TxtCtl.SetColor, 0x2),
            '#60I空之耀晶片×１０\n',
            (TxtCtl.SetColor, 0x2),
            '#61I幻之耀晶片×１０\n',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1506)

    Jump('loc_C23')

    def _loc_C09(): pass

    label('loc_C09')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_C23(): pass

    label('loc_C23')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0xC35
@scena.Code('func_06_C35')
def func_06_C35():
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
        'loc_C5A',
    )

    Call(0, 0x000B)
    Call(0, 0x000C)
    FadeIn(0, 0)
    Sleep(100)

    def _loc_C5A(): pass

    label('loc_C5A')

    Fade(1000)
    OP_6D(2520, -50, 8109, 0)
    OP_67(0, 4960, -10000, 0)
    OP_6B(2840, 0)
    OP_6C(179000, 0)
    OP_6E(359, 0)
    SetChrPos(0x0101, 2690, -70, 10480, 225)
    SetChrPos(0x0102, 3500, -20, 9710, 225)
    SetChrPos(0x00F8, 3300, 50, 11900, 225)
    SetChrPos(0x00F9, 4280, 60, 11100, 225)
    OP_4A(0x0008, 255)
    OP_4A(0x0009, 255)
    OP_8C(0x0008, 45, 0)
    OP_8C(0x0009, 45, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#4040370488V#2P哎呀，你们是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370489V#1025F#6P那个，我们是\n',
            '游击士协会的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔等人说明了情况\n',
            '并试着询问了内燃引擎的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#4040370490V#2P是吗……因为那次骚动，\n',
            '我都完全忘记有这回事了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#4040370491V我记得，那个内燃引擎\n',
            '应该保管在货舱里才对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0009, 400)

    ChrTalk(
        0x0008,
        (
            '#4040370492V#4P里诺，帮个忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0008, 400)

    ChrTalk(
        0x0009,
        (
            '#4050370493V#5P明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(2000)

    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x0008, 0x0004)
    SetChrFlags(0x0009, 0x0004)

    @scena.Lambda('lambda_0E9E')
    def lambda_0E9E():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_0E9E')

    DispatchAsync2(0x0101, 0x0002, lambda_0E9E)

    @scena.Lambda('lambda_0EAF')
    def lambda_0EAF():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_0EAF')

    DispatchAsync2(0x0102, 0x0002, lambda_0EAF)

    @scena.Lambda('lambda_0EC0')
    def lambda_0EC0():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_0EC0')

    DispatchAsync2(0x00F8, 0x0002, lambda_0EC0)

    @scena.Lambda('lambda_0ED1')
    def lambda_0ED1():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_0ED1')

    DispatchAsync2(0x00F9, 0x0002, lambda_0ED1)

    OP_6D(2520, -50, 8109, 0)
    OP_67(0, 2970, -10000, 0)
    OP_6B(2840, 0)
    OP_6C(179000, 0)
    OP_6E(359, 0)
    FadeIn(1000, 0)
    OP_0D()

    @scena.Lambda('lambda_0F29')
    def lambda_0F29():
        OP_67(0, 4960, -10000, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0F29)

    SetChrPos(0x0008, 5830, 1000, 1450, 135)
    SetChrPos(0x0009, 5830, 1000, 1450, 315)
    ClearChrFlags(0x0008, 0x0080)

    @scena.Lambda('lambda_0F68')
    def lambda_0F68():
        OP_8F(0x00FE, 1350, -60, 8690, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0F68)

    Sleep(600)

    ClearChrFlags(0x0009, 0x0080)

    @scena.Lambda('lambda_0F8D')
    def lambda_0F8D():
        OP_8F(0x00FE, 2190, -60, 7790, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0F8D)

    WaitForThreadExit(0x0008, 0x0001)
    WaitForThreadExit(0x0101, 0x0001)
    TerminateThread(0x0101, 0x02)
    TerminateThread(0x0102, 0x02)
    TerminateThread(0x00F8, 0x02)
    TerminateThread(0x00F9, 0x02)
    Sleep(200)

    OP_8F(0x0008, 1350, -60, 8690, 2000, 0x00)
    WaitForThreadExit(0x0008, 0x0001)
    OP_8C(0x0008, 45, 400)
    WaitForThreadExit(0x0009, 0x0001)
    OP_8C(0x0009, 45, 400)

    ChrTalk(
        0x0008,
        (
            '#4040370494V#2P呀，让你们久等了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8F(0x0009, 2710, -50, 9450, 2000, 0x00)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.Item, ItemTable['内燃引擎']),
            (TxtCtl.SetColor, 0x0),
            '收下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    AddItem(ItemTable['内燃引擎'], 1)
    OP_8F(0x0009, 2190, -60, 7790, 2000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010370495V#1006F#6P嗯，我们确实收下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370496V#1040F#6P给您添麻烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#4040370497V#2P哪里哪里，\n',
            '劳驾你们特地过来拿\n',
            '才真是不好意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#4040370498V不过，在这危急状况下\n',
            '居然为了让大家能够泡温泉\n',
            '而展开行动……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#4040370499V看来游击士的\n',
            '行动基准果然和我们不同啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370500V#1013F#6P呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370501V#1043F#6P不好意思……\n',
            '在这么严重的时候我们还做这种事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#4040370502V#2P不，我并不是\n',
            '在讽刺你们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#4040370503V……对我们来说\n',
            '导力兵器不能使用\n',
            '是相当令人不安的状况。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#4040370504V我们光顾着考虑\n',
            '要如何去应对敌人才好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#4040370505V也许应该稍微学习一下\n',
            '你们这种从容不迫的态度呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370506V#1025F#6P嗯、嗯～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010370507V#1016F我们只是……\n',
            '随便找事情做而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_13C6',
    )

    ChrTalk(
        0x0108,
        (
            '#0080370508V#070F#6P老实说，我们也\n',
            '正为了该做些什么而迷惑。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080370509V我们大家都只能一边摸索，\n',
            '一边找到答案吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14D5')

    def _loc_13C6(): pass

    label('loc_13C6')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1451',
    )

    ChrTalk(
        0x0103,
        (
            '#0030370510V#027F#6P老实说，我们也\n',
            '正为了该做些什么而迷惑呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030370511V我们大家都只能一边摸索，\n',
            '一边找到答案吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14D5')

    def _loc_1451(): pass

    label('loc_1451')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_14D5',
    )

    ChrTalk(
        0x0106,
        (
            '#0050370512V#051F#6P其实，我们\n',
            '也正为该做些什么而迷惑啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050370513V我们大家都只能一边摸索，\n',
            '一边寻找答案吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14D5(): pass

    label('loc_14D5')

    ChrTalk(
        0x0008,
        (
            '#4040370514V#2P啊啊……是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#4040370515V不过，正是在这种状况下，\n',
            '心情的平和才显得重要。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#4040370516V亚尔摩温泉的修复工作，\n',
            '请诸位务必要多加努力。',
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
        'loc_15A0',
    )

    ChrTalk(
        0x0107,
        (
            '#0070370517V#061F#6P是、是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15A0(): pass

    label('loc_15A0')

    ChrTalk(
        0x0101,
        (
            '#0010370518V#1006F#6P嗯……交给我们吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(2000)

    OP_6D(15760, -50, -20140, 0)
    OP_67(0, 7310, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(320000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 15020, 10, -21640, 180)
    SetChrPos(0x0102, 15950, -30, -21640, 180)
    SetChrPos(0x00F8, 14650, 20, -20780, 180)
    SetChrPos(0x00F9, 16400, -30, -20780, 180)
    CreateThread(0x0101, 0x01, 0x00, 0x0007)
    CreateThread(0x0102, 0x01, 0x00, 0x0008)
    CreateThread(0x00F8, 0x01, 0x00, 0x0009)
    CreateThread(0x00F9, 0x01, 0x00, 0x000A)
    Sleep(400)

    @scena.Lambda('lambda_1685')
    def lambda_1685():
        OP_6D(15150, 70, -30990, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1685)

    @scena.Lambda('lambda_169D')
    def lambda_169D():
        OP_6C(45000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_169D)

    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x00F9, 0x0001)
    WaitForThreadExit(0x00F8, 0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1776',
    )

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
        0,
        (
            TXT(0x00, '【◇汽油到手了】\n'),
            TXT(0x01, '【◇没有汽油但有介绍信】\n'),
            TXT(0x02, '【◇汽油和介绍信都没有】\n'),
            TXT(0x03, '【◇不变更】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_175E'),
        (0x00000001, 'loc_1764'),
        (0x00000002, 'loc_176D'),
        (-1, 'loc_1776'),
    )

    def _loc_175E(): pass

    label('loc_175E')

    OP_A2(0x2011)

    Jump('loc_1776')

    def _loc_1764(): pass

    label('loc_1764')

    OP_A3(0x2011)
    OP_A2(0x2010)

    Jump('loc_1776')

    def _loc_176D(): pass

    label('loc_176D')

    OP_A3(0x2011)
    OP_A3(0x2010)

    Jump('loc_1776')

    def _loc_1776(): pass

    label('loc_1776')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 1, 0x2011)),
            Expr.Return,
        ),
        'loc_190D',
    )

    OP_28(0x00C2, 0x01, 0x1000)

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1844',
    )

    ChrTurnDirection(0x0101, 0x0107, 400)

    ChrTalk(
        0x0101,
        (
            '#0010370519V#1006F#6P好了……\n',
            '这样一来材料就齐全了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010370520V赶快返回亚尔摩\n',
            '开始改造水泵装置吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0101, 400)

    ChrTalk(
        0x0107,
        (
            '#0070370521V#061F#5P嗯，我是准备好了，\n',
            '随时ＯＫ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_190A')

    def _loc_1844(): pass

    label('loc_1844')

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010370519V#1006F#6P好了……\n',
            '这样一来材料就齐全了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010370523V#1015F到底还是只有提妲\n',
            '才能改造水泵装置吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020370524V#1040F#2P说得也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020370525V先返回协会\n',
            '和提妲会合吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_190A(): pass

    label('loc_190A')

    Jump('loc_1AD5')

    def _loc_190D(): pass

    label('loc_190D')

    ChrTalk(
        0x0101,
        (
            '#0010370526V#1006F#6P好了……\n',
            '这样内燃引擎就ＯＫ了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010370527V#1015F接下来是汽油……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 0, 0x2010)),
            Expr.Return,
        ),
        'loc_1A3C',
    )

    ChrTalk(
        0x0102,
        (
            '#0020370528V#1040F#2P据玛多克工房长所言，\n',
            '从共和国订购来的东西\n',
            '好像已经运抵了卢安的港口。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020370529V看来只有过去看看了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370530V#1006F#6P嗯，既然做到这一步，\n',
            '就必须坚持到最后才行！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AD5')

    def _loc_1A3C(): pass

    label('loc_1A3C')

    ChrTalk(
        0x0102,
        (
            '#0020370531V#1035F#2P说不定就像之前一样，\n',
            '有可能会保管在中央工房地下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020370532V#1040F先去那里确认一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010370533V#1006F#6P嗯，明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AD5(): pass

    label('loc_1AD5')

    OP_A2(0x200F)
    OP_28(0x00C2, 0x01, 0x0080)
    SetChrPos(0x0008, 1400, -40, 9260, 135)
    SetChrPos(0x0009, 2590, -40, 7810, 315)
    OP_4B(0x0008, 255)
    OP_4B(0x0009, 255)
    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0x1B0B
@scena.Code('func_07_1B0B')
def func_07_1B0B():
    OP_8E(0x00FE, 13970, 60, -32420, 2000, 0x00)
    OP_8C(0x00FE, 45, 400)

    Return()

# id: 0x0008 offset: 0x1B27
@scena.Code('func_08_1B27')
def func_08_1B27():
    Sleep(150)

    OP_8E(0x00FE, 15560, 80, -32080, 2000, 0x00)
    OP_8C(0x00FE, 270, 400)

    Return()

# id: 0x0009 offset: 0x1B48
@scena.Code('func_09_1B48')
def func_09_1B48():
    Sleep(350)

    OP_8E(0x00FE, 14080, 50, -30600, 2000, 0x00)
    OP_8C(0x00FE, 180, 400)

    Return()

# id: 0x000A offset: 0x1B69
@scena.Code('func_0A_1B69')
def func_0A_1B69():
    Sleep(350)

    OP_8E(0x00FE, 15710, 50, -30530, 2000, 0x00)
    OP_8C(0x00FE, 225, 400)

    Return()

# id: 0x000B offset: 0x1B8A
@scena.Code('func_0B_1B8A')
def func_0B_1B8A():
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
        (0x00000000, 'loc_1C04'),
        (0x00000001, 'loc_1C0A'),
        (-1, 'loc_1C10'),
    )

    def _loc_1C04(): pass

    label('loc_1C04')

    OP_A2(0x1200)

    Jump('loc_1C10')

    def _loc_1C0A(): pass

    label('loc_1C0A')

    OP_A2(0x1201)

    Jump('loc_1C10')

    def _loc_1C10(): pass

    label('loc_1C10')

    Return()

# id: 0x000C offset: 0x1C11
@scena.Code('func_0C_1C11')
def func_0C_1C11():
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

# id: 0x000D offset: 0x1C6A
@scena.Code('func_0D_1C6A')
def func_0D_1C6A():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '北　红莲之塔\n',
            '※魔兽较多，请注意！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x000E offset: 0x1CBE
@scena.Code('func_0E_1CBE')
def func_0E_1CBE():
    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0011860001V#1001F这里好像可以钓上什么来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1CF6')
    def lambda_1CF6():
        OP_6D(34900, 70, 15500, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_1CF6)

    @scena.Lambda('lambda_1D0E')
    def lambda_1D0E():
        OP_6B(3250, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_1D0E)

    @scena.Lambda('lambda_1D1E')
    def lambda_1D1E():
        OP_6C(270000, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_1D1E)

    Sleep(1000)

    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '钓鱼吗？',
            (TxtCtl.SetColor, 0x0),
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
        1,
        (
            TXT(0x00, '钓鱼\n'),
            TXT(0x01, '离开\n'),
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
    WaitForThreadExit(0x0000, 0x0001)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1DA5',
    )

    OP_C0(0x0E, 0x00000023, 0x00008FF2, 0x00000050, 0x00004362, 0x000000E1, 0x000083B8, 0xFFFFFC18, 0x0000369C)
    OP_0D()
    EventEnd(0x01)

    Jump('loc_1DB4')

    def _loc_1DA5(): pass

    label('loc_1DA5')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1DB4',
    )

    EventEnd(0x01)

    def _loc_1DB4(): pass

    label('loc_1DB4')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

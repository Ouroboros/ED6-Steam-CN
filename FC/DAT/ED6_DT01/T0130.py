import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T0130_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0130   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0130.x'
    header.mapIndex       = 3
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/T0130._SN', 'ED6_DT01/T0130_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x0000E678,
            dword_04        = 0x00000000,
            dword_08        = 0x00009C40,
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
            word_30         = 315,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 3,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
        ScenaEntryPoint(
            dword_00        = 0x0000E678,
            dword_04        = 0x00000000,
            dword_08        = 0x00009C40,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 8000,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2600,
            dword_2C        = 262,
            word_30         = 315,
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

# id: 0x10000 offset: 0xEC
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH01400._CH', 'ED6_DT07/CH01400P._CP'),
        ('ED6_DT07/CH01410._CH', 'ED6_DT07/CH01410P._CP'),
        ('ED6_DT07/CH01043._CH', 'ED6_DT07/CH01043P._CP'),
        ('ED6_DT07/CH01213._CH', 'ED6_DT07/CH01213P._CP'),
        ('ED6_DT07/CH01180._CH', 'ED6_DT07/CH01180P._CP'),
        ('ED6_DT07/CH01700._CH', 'ED6_DT07/CH01700P._CP'),
        ('ED6_DT07/CH01700._CH', 'ED6_DT07/CH01700P._CP'),
        ('ED6_DT07/CH02330._CH', 'ED6_DT07/CH02330P._CP'),
        ('ED6_DT07/CH01250._CH', 'ED6_DT07/CH01250P._CP'),
        ('ED6_DT07/CH01003._CH', 'ED6_DT07/CH01003P._CP'),
        ('ED6_DT07/CH02350._CH', 'ED6_DT07/CH02350P._CP'),
        ('ED6_DT07/CH01350._CH', 'ED6_DT07/CH01350P._CP'),
        ('ED6_DT07/CH00014._CH', 'ED6_DT07/CH00014P._CP'),
        ('ED6_DT07/CH00015._CH', 'ED6_DT07/CH00015P._CP'),
    ]

# id: 0x10001 offset: 0x15E
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '迪拜恩教区长',
            x                   = 58800,
            z                   = 1000,
            y                   = 52200,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '修女梅',
            x                   = -16832,
            z                   = 0,
            y                   = 42888,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '西加罗',
            x                   = 56090,
            z                   = 100,
            y                   = 46000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '艾德尔',
            x                   = 55330,
            z                   = 100,
            y                   = 45940,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '米蕾奴夫人',
            x                   = 58997,
            z                   = 1000,
            y                   = 50050,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '安莉尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0111,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '安莉尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0111,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '穿制服的少女',
            x                   = 58960,
            z                   = 1000,
            y                   = 49950,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '潘杜爷爷',
            x                   = 59170,
            z                   = 1000,
            y                   = 50210,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '拉欧老人',
            x                   = 61810,
            z                   = 0,
            y                   = 45970,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '克劳斯市长',
            x                   = 58997,
            z                   = 1000,
            y                   = 50050,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '玲达',
            x                   = 59070,
            z                   = 1000,
            y                   = 50010,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0195,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
    )

# id: 0x10002 offset: 0x2DE
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x2DE
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x2DE
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 58950,
            triggerZ            = 1000,
            triggerY            = 50290,
            triggerRange        = 400,
            actorX              = 58800,
            actorZ              = 2500,
            actorY              = 52200,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x302
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            Expr.Return,
        ),
        'loc_316',
    )

    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000C, 0x0008)

    Jump('loc_424')

    def _loc_316(): pass

    label('loc_316')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_32A',
    )

    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000C, 0x0008)

    Jump('loc_424')

    def _loc_32A(): pass

    label('loc_32A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 2, 0x252)),
            Expr.Return,
        ),
        'loc_36B',
    )

    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000C, 0x0008)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0012, 0x0008)

    If(
        (
            (Expr.Eval, "OP_29(0x0009, 0x01, 0x0020)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0009, 0x01, 0x0010)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0009, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_368',
    )

    ChrSetDirection(0x0008, 270, 0)

    def _loc_368(): pass

    label('loc_368')

    Jump('loc_424')

    def _loc_36B(): pass

    label('loc_36B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_3AC',
    )

    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000C, 0x0008)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0011, 0x0008)

    If(
        (
            (Expr.Eval, "OP_29(0x0009, 0x01, 0x0020)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0009, 0x01, 0x0010)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0009, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3A9',
    )

    ChrSetDirection(0x0008, 270, 0)

    def _loc_3A9(): pass

    label('loc_3A9')

    Jump('loc_424')

    def _loc_3AC(): pass

    label('loc_3AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_3D2',
    )

    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000C, 0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 6, 0x24E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3CF',
    )

    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x000F, 0x0080)

    def _loc_3CF(): pass

    label('loc_3CF')

    Jump('loc_424')

    def _loc_3D2(): pass

    label('loc_3D2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_3F5',
    )

    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000C, 0x0008)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x0013, 0x0080)

    Jump('loc_424')

    def _loc_3F5(): pass

    label('loc_3F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_413',
    )

    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000C, 0x0008)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0010, 0x0008)

    Jump('loc_424')

    def _loc_413(): pass

    label('loc_413')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_424',
    )

    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000C, 0x0008)

    def _loc_424(): pass

    label('loc_424')

    If(
        (
            (Expr.Eval, "OP_29(0x0009, 0x01, 0x0010)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0009, 0x01, 0x0008)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0009, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_44A',
    )

    OP_28(0x0009, 0x01, 0x0010)
    Event(1, 0x0006)

    def _loc_44A(): pass

    label('loc_44A')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x67),
            Expr.Equ,
            (Expr.Eval, "OP_29(0x0009, 0x01, 0x0020)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0009, 0x01, 0x0010)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0009, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_47F',
    )

    OP_28(0x0009, 0x01, 0x0020)
    OP_28(0x0009, 0x01, 0x0040)
    Event(1, 0x0007)

    def _loc_47F(): pass

    label('loc_47F')

    Return()

# id: 0x0001 offset: 0x480
@scena.Code('func_01_480')
def func_01_480():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_498',
    )

    OP_B1('t0130_y')

    Jump('loc_4A1')

    def _loc_498(): pass

    label('loc_498')

    OP_B1('t0130_n')

    def _loc_4A1(): pass

    label('loc_4A1')

    If(
        (
            (Expr.Eval, "OP_29(0x0009, 0x01, 0x0020)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0009, 0x01, 0x0010)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0009, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0009, 0x00, 0x04)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4C9',
    )

    OP_1B(0x01, 0x01, 0x0009)

    def _loc_4C9(): pass

    label('loc_4C9')

    Return()

# id: 0x0002 offset: 0x4CA
@scena.Code('func_02_4CA')
def func_02_4CA():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4DF',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_4CA')

    def _loc_4DF(): pass

    label('loc_4DF')

    Return()

# id: 0x0003 offset: 0x4E0
@scena.Code('func_03_4E0')
def func_03_4E0():
    Call(0, 0x0004)

    Return()

# id: 0x0004 offset: 0x4E5
@scena.Code('func_04_4E5')
def func_04_4E5():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_609',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0007, 0x00, 0x02)"),
            (Expr.Eval, "OP_29(0x0007, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x0386)"),
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x039F)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_50F',
    )

    Call(1, 0x0001)

    Jump('loc_606')

    def _loc_50F(): pass

    label('loc_50F')

    If(
        (
            (Expr.Eval, "OP_29(0x000D, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_5F0',
    )

    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_57C',
    )

    ChrTalk(
        0x0008,
        (
            '为我采集来了药材……\n',
            '真是辛苦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '那么，\n',
            '以后的旅程也一定要小心谨慎啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5EA')

    def _loc_57C(): pass

    label('loc_57C')

    ChrTalk(
        0x0008,
        (
            '那封信就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '教会在柏斯市的东侧，\n',
            '进城后很容易就可以找到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '愿你们能\n',
            '常受女神的保佑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5EA(): pass

    label('loc_5EA')

    TalkEnd(0x0008)

    Jump('loc_606')

    def _loc_5F0(): pass

    label('loc_5F0')

    If(
        (
            (Expr.Eval, "OP_29(0x000D, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_602',
    )

    Call(1, 0x0002)

    Jump('loc_606')

    def _loc_602(): pass

    label('loc_602')

    Call(1, 0x0000)

    def _loc_606(): pass

    label('loc_606')

    Jump('loc_13AF')

    def _loc_609(): pass

    label('loc_609')

    If(
        (
            (Expr.Eval, "OP_29(0x0009, 0x01, 0x0020)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0009, 0x01, 0x0010)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0009, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_669',
    )

    TalkBegin(0x0008)

    ChrTalk(
        0x0008,
        (
            '哦？怎么回事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '好像有什么动物\n',
            '跑进这里来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0008)

    Jump('loc_13AF')

    def _loc_669(): pass

    label('loc_669')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_75A',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0007, 0x00, 0x02)"),
            (Expr.Eval, "OP_29(0x0007, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x0386)"),
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x039F)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_697',
    )

    Call(1, 0x0004)

    Jump('loc_757')

    def _loc_697(): pass

    label('loc_697')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_709',
    )

    TalkBegin(0x0008)

    ChrTalk(
        0x0008,
        (
            '艾丝蒂尔、约修亚，\n',
            '真是非常的感谢你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '在你们二人走过的蓝天之下，\n',
            '空之女神会常伴左右。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0008)

    Jump('loc_757')

    def _loc_709(): pass

    label('loc_709')

    TalkBegin(0x0008)

    ChrTalk(
        0x0008,
        (
            '喔，\n',
            '你们俩都变得有些成熟了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '见到你们身心成长，\n',
            '我也很高兴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0008)

    def _loc_757(): pass

    label('loc_757')

    Jump('loc_13AF')

    def _loc_75A(): pass

    label('loc_75A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004A, 2, 0x252)),
            Expr.Return,
        ),
        'loc_82A',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0007, 0x00, 0x02)"),
            (Expr.Eval, "OP_29(0x0007, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x0386)"),
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x039F)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_784',
    )

    Call(1, 0x0004)

    Jump('loc_827')

    def _loc_784(): pass

    label('loc_784')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_7F6',
    )

    TalkBegin(0x0008)

    ChrTalk(
        0x0008,
        (
            '艾丝蒂尔、约修亚，\n',
            '真是非常的感谢你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '在你们二人走过的蓝天之下，\n',
            '空之女神会常伴左右。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0008)

    Jump('loc_827')

    def _loc_7F6(): pass

    label('loc_7F6')

    TalkBegin(0x0008)

    ChrTalk(
        0x0008,
        (
            '市长大人看来好像\n',
            '碰上了什么开心事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0008)

    def _loc_827(): pass

    label('loc_827')

    Jump('loc_13AF')

    def _loc_82A(): pass

    label('loc_82A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_A4E',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0007, 0x00, 0x02)"),
            (Expr.Eval, "OP_29(0x0007, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x0386)"),
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x039F)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_854',
    )

    Call(1, 0x0004)

    Jump('loc_A4B')

    def _loc_854(): pass

    label('loc_854')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_8C6',
    )

    TalkBegin(0x0008)

    ChrTalk(
        0x0008,
        (
            '艾丝蒂尔、约修亚，\n',
            '真是非常的感谢你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '在你们二人走过的蓝天之下，\n',
            '空之女神会常伴左右。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0008)

    Jump('loc_A4B')

    def _loc_8C6(): pass

    label('loc_8C6')

    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9E5',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '我已经在洛连特市\n',
            '住了近３０年了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '１０年前看着\n',
            '这个化作瓦砾的城镇， \n',
            '我和市民们一样感到绝望。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '但如今看着\n',
            '这个百业俱兴的城市，\n',
            '又不禁由衷感叹于人的坚强。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '脆弱与坚强，\n',
            '人同时拥有这两种相反特性的矛盾……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '但是， \n',
            '我却认为这样的人才真的可敬可爱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0008)

    Jump('loc_A48')

    def _loc_9E5(): pass

    label('loc_9E5')

    ChrTalk(
        0x0008,
        (
            '脆弱与坚强，\n',
            '人同时拥有这两种相反特性的矛盾……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '但是， \n',
            '我却认为这样的人才真的可敬可爱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A48(): pass

    label('loc_A48')

    TalkEnd(0x0008)

    def _loc_A4B(): pass

    label('loc_A4B')

    Jump('loc_13AF')

    def _loc_A4E(): pass

    label('loc_A4E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_CD0',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0007, 0x00, 0x02)"),
            (Expr.Eval, "OP_29(0x0007, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x0386)"),
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x039F)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_A78',
    )

    Call(1, 0x0004)

    Jump('loc_CCD')

    def _loc_A78(): pass

    label('loc_A78')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_AEA',
    )

    TalkBegin(0x0008)

    ChrTalk(
        0x0008,
        (
            '艾丝蒂尔、约修亚，\n',
            '真是非常的感谢你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '在你们二人走过的蓝天之下，\n',
            '空之女神会常伴左右。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0008)

    Jump('loc_CCD')

    def _loc_AEA(): pass

    label('loc_AEA')

    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0056, 5, 0x2B5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C5F',
    )

    SetScenaFlags(ScenaFlag(0x0056, 5, 0x2B5))

    ChrTalk(
        0x0008,
        (
            '光愈强，\n',
            '则影愈暗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '当曝身于耀眼的光芒下时，\n',
            '人类会意识到自己的丑恶，\n',
            '并为此感到悔恨。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '对往事耿耿于怀的人\n',
            '更是如此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#015F……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '但是，也有人因此\n',
            '而深知人世的伤痛与悲哀，\n',
            '从而成为胸怀广阔的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '重要的是对未来要有充分的心理准备，\n',
            '并明确自己要采取的行动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#007F嗯，真头疼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '教区长还是老样子，\n',
            '尽说些难懂的话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CCA')

    def _loc_C5F(): pass

    label('loc_C5F')

    ChrTalk(
        0x0008,
        (
            '当曝身于耀眼的光芒下时，\n',
            '人类会意识到自己的丑恶，\n',
            '并为此感到悔恨。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '对往事耿耿于怀的人\n',
            '更是如此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CCA(): pass

    label('loc_CCA')

    TalkEnd(0x0008)

    def _loc_CCD(): pass

    label('loc_CCD')

    Jump('loc_13AF')

    def _loc_CD0(): pass

    label('loc_CD0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_EB3',
    )

    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0056, 4, 0x2B4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E59',
    )

    SetScenaFlags(ScenaFlag(0x0056, 4, 0x2B4))

    ChrTalk(
        0x0008,
        (
            '艾丝蒂尔、约修亚，\n',
            '听说你们当上游击士了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '在满怀憧憬与期待的同时，\n',
            '想必也充满了紧张与不安吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '唔……\n',
            '看起来艾丝蒂尔\n',
            '似乎还有其它的心事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#004F哎……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#501F没、没这回事啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '亲人不在身边\n',
            '的确会让人心神难安……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#003F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '但是，\n',
            '人人都拥有着\n',
            '克服这种逆境的坚强。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '请把这看作女神给予的考验，\n',
            '好好加油吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F……嗯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0008)

    Jump('loc_EB0')

    def _loc_E59(): pass

    label('loc_E59')

    ChrTalk(
        0x0008,
        (
            '人人都拥有着\n',
            '克服这种逆境的坚强。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '请把这看作女神给予的考验，\n',
            '好好加油吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0008)

    def _loc_EB0(): pass

    label('loc_EB0')

    Jump('loc_13AF')

    def _loc_EB3(): pass

    label('loc_EB3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_FE9',
    )

    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0056, 3, 0x2B3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F91',
    )

    SetScenaFlags(ScenaFlag(0x0056, 3, 0x2B3))
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '艾丝蒂尔……\n',
            '你好像有什么烦恼呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#501F啊？没、没有啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '人是要伴随烦恼而成长的，\n',
            '这是女神对人的考验。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '女神啊，请引导苦恼的众生吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0008)

    Jump('loc_FE6')

    def _loc_F91(): pass

    label('loc_F91')

    ChrTalk(
        0x0008,
        (
            '无论将来会走上什么样的道路，\n',
            '希望你们不要忘记你们两人\n',
            '在一起走过的每时每刻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0008)

    def _loc_FE6(): pass

    label('loc_FE6')

    Jump('loc_13AF')

    def _loc_FE9(): pass

    label('loc_FE9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_1177',
    )

    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0056, 2, 0x2B2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1119',
    )

    SetScenaFlags(ScenaFlag(0x0056, 2, 0x2B2))
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '艾丝蒂尔，\n',
            '你看起来非常开心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '是不是有什么\n',
            '高兴的事情啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#001F呵呵呵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#018F饶了我吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '嗯， \n',
            '开心虽然是件好事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '但要记住，\n',
            '事情进行得很顺利的时候尤其要提高警觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '空之女神啊，\n',
            '请引导还未成熟的人们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0008)

    Jump('loc_1174')

    def _loc_1119(): pass

    label('loc_1119')

    ChrTalk(
        0x0008,
        (
            '事情进行得很顺利的时候\n',
            '尤其要提高警觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '空之女神啊，\n',
            '请引导还未成熟的人们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0008)

    def _loc_1174(): pass

    label('loc_1174')

    Jump('loc_13AF')

    def _loc_1177(): pass

    label('loc_1177')

    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0056, 1, 0x2B1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1358',
    )

    SetScenaFlags(ScenaFlag(0x0056, 1, 0x2B1))

    ChrTalk(
        0x0008,
        (
            '哦，好久不见你们俩了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '你们这么早就来教会，\n',
            '真是让我感动啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F教区长，早上好。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F早上好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '艾丝蒂尔，你在上主日学校的时候\n',
            '可是个迟到、逃学的惯犯呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '毕业之后的生活态度\n',
            '有没有改变一些呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#008F哈～哈哈，改了一些吧……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '……离做弥撒\n',
            '还有一些时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '难得你们专程赶来，\n',
            '我就给你们来一堂特别讲义如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#004F哎……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#506F不、不用了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#018F（为什么连我也给牵连进来了……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0008)

    Jump('loc_13AF')

    def _loc_1358(): pass

    label('loc_1358')

    ChrTalk(
        0x0008,
        (
            '离做弥撒\n',
            '还有一些时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '难得你们专程赶来，\n',
            '我就给你们来一堂特别讲义如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0008)

    def _loc_13AF(): pass

    label('loc_13AF')

    Return()

# id: 0x0005 offset: 0x13B0
@scena.Code('func_05_13B0')
def func_05_13B0():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_1498',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_146A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '之前上课的时候，\n',
            '我教给了孩子们游击士协会的相关知识。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '特别是那个\n',
            '叫鲁克的男孩子，\n',
            '他可是非常认真听我讲课呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '游击士果然是\n',
            '男孩子最为憧憬的职业啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1495')

    def _loc_146A(): pass

    label('loc_146A')

    ChrTalk(
        0x00FE,
        (
            '游击士果然是\n',
            '男孩子最为憧憬的职业啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1495(): pass

    label('loc_1495')

    Jump('loc_1990')

    def _loc_1498(): pass

    label('loc_1498')

    If(
        (
            (Expr.Eval, "OP_29(0x0009, 0x01, 0x0020)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0009, 0x01, 0x0010)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0009, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0009, 0x00, 0x04)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1503',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才我好像听到\n',
            '楼梯上有一阵脚步声……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……难道是我的错觉？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1990')

    def _loc_1503(): pass

    label('loc_1503')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_1565',
    )

    ChrTalk(
        0x00FE,
        (
            '最近， \n',
            '主日学校的孩子们\n',
            '在没课的时候也会来找我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我觉得成为修女\n',
            '真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1990')

    def _loc_1565(): pass

    label('loc_1565')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_15E4',
    )

    ChrTalk(
        0x00FE,
        (
            '主日学校的讲课\n',
            '比想象的顺利。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '多亏了教区长大人的意见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过鲁克\n',
            '可真是个顽皮的孩子。\n',
            '我可拿他没辙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1990')

    def _loc_15E4(): pass

    label('loc_15E4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_1636',
    )

    ChrTalk(
        0x00FE,
        (
            '我被安排去\n',
            '下一次主日学校讲课。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但愿孩子们\n',
            '都能听话就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1990')

    def _loc_1636(): pass

    label('loc_1636')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_179F',
    )

    ChrTurnDirection(0x0009, 0x0101, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_176E',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '啊……\n',
            '你是艾丝蒂尔小姐吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我听教区长大人\n',
            '说起过你很多事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#004F哎……\n',
            '都、都是些什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵， \n',
            '是你上主日学校时的种种事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F打瞌睡啊迟到啊\n',
            '翘课啊恶作剧啊\n',
            '她可是个大行家哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '教区长大人似乎挺喜欢\n',
            '艾丝蒂尔小姐的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#008F是、是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_179C')

    def _loc_176E(): pass

    label('loc_176E')

    ChrTalk(
        0x00FE,
        (
            '教区长大人\n',
            '似乎挺喜欢\n',
            '艾丝蒂尔小姐的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_179C(): pass

    label('loc_179C')

    Jump('loc_1990')

    def _loc_179F(): pass

    label('loc_179F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_17E6',
    )

    ChrTalk(
        0x0009,
        (
            '女神啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '非常感谢您赐予了我们\n',
            '这一天的和平安宁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1990')

    def _loc_17E6(): pass

    label('loc_17E6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_193E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_18C7',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x0009,
        (
            '我是这里的新任修女。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '是不久之前才从王都\n',
            '派到洛连特来任职的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这里充满了自然的气息，\n',
            '而且民风朴实， \n',
            '真是一个休闲的好地方呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '迪拜恩教区长\n',
            '虽然对我比较严厉，\n',
            '但是他真的很让人值得尊敬。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_193B')

    def _loc_18C7(): pass

    label('loc_18C7')

    ChrTalk(
        0x0009,
        (
            '我是不久之前才从王都\n',
            '派到洛连特来任职的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这里充满了自然的气息，\n',
            '而且民风朴实， \n',
            '真是一个休闲的好地方呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_193B(): pass

    label('loc_193B')

    Jump('loc_1990')

    def _loc_193E(): pass

    label('loc_193E')

    ChrTalk(
        0x0009,
        (
            '呀，\n',
            '就要到做弥撒的时间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '市长夫人也要来参加，\n',
            '我得马上去做准备才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1990(): pass

    label('loc_1990')

    TalkEnd(0x0009)

    Return()

# id: 0x0006 offset: 0x1994
@scena.Code('func_06_1994')
def func_06_1994():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_1A5B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A00',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000A,
        (
            '我们正在作巡礼之旅，\n',
            '要走遍王国各地的礼拜堂。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '刚刚才坐定期船\n',
            '到达洛连特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A58')

    def _loc_1A00(): pass

    label('loc_1A00')

    ChrTalk(
        0x000A,
        (
            '多亏有了定期船，\n',
            '旅行也变得轻松愉快了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '工作也不用请太长的假，\n',
            '真是帮大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A58(): pass

    label('loc_1A58')

    Jump('loc_1AA1')

    def _loc_1A5B(): pass

    label('loc_1A5B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_1A83',
    )

    ChrTalk(
        0x000A,
        (
            '我真的本应不出现在这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AA1')

    def _loc_1A83(): pass

    label('loc_1A83')

    ChrTalk(
        0x000A,
        (
            '我真的本应不出现在这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AA1(): pass

    label('loc_1AA1')

    TalkEnd(0x000A)

    Return()

# id: 0x0007 offset: 0x1AA5
@scena.Code('func_07_1AA5')
def func_07_1AA5():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_1B6D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1B2E',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x000B,
        (
            '呵呵， \n',
            '我是为了旅游和购物\n',
            '才跟着老公来这儿的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '洛连特这城市\n',
            '不单空气清新自然，\n',
            '而且气氛也很宁静祥和。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B6A')

    def _loc_1B2E(): pass

    label('loc_1B2E')

    ChrTalk(
        0x000B,
        (
            '洛连特这城市\n',
            '不单空气清新自然，\n',
            '而且气氛也很宁静祥和。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B6A(): pass

    label('loc_1B6A')

    Jump('loc_1BB3')

    def _loc_1B6D(): pass

    label('loc_1B6D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_1B95',
    )

    ChrTalk(
        0x000B,
        (
            '我真的本应不出现在这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BB3')

    def _loc_1B95(): pass

    label('loc_1B95')

    ChrTalk(
        0x000B,
        (
            '我真的本应不出现在这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1BB3(): pass

    label('loc_1BB3')

    TalkEnd(0x000B)

    Return()

# id: 0x0008 offset: 0x1BB7
@scena.Code('func_08_1BB7')
def func_08_1BB7():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C4D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x0101,
        (
            '#000F米蕾奴婶婶，早上好。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F早上好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '呀，是艾丝蒂尔和约修亚啊，\n',
            '早上好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '你们一大早就出门了？\n',
            '真是辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C74')

    def _loc_1C4D(): pass

    label('loc_1C4D')

    ChrTalk(
        0x000C,
        (
            '你们一大早就出门了？\n',
            '真是辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C74(): pass

    label('loc_1C74')

    TalkEnd(0x000C)

    Return()

# id: 0x0009 offset: 0x1C78
@scena.Code('func_09_1C78')
def func_09_1C78():
    TalkBegin(0x000F)

    ChrTalk(
        0x000F,
        (
            '#0090010448V原来如此…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090010449V高论，的确是高论啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000F)

    Return()

# id: 0x000A offset: 0x1CC3
@scena.Code('func_0A_1CC3')
def func_0A_1CC3():
    TalkBegin(0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D2F',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '一天又过去了， \n',
            '和平的日子实在是比什么都好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '战争什么的……\n',
            '千万不要再发生了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D83')

    def _loc_1D2F(): pass

    label('loc_1D2F')

    ChrTalk(
        0x00FE,
        (
            '战争什么的……\n',
            '千万不要再发生了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一想起十年前的那次战争\n',
            '我就忍不住颤抖。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D83(): pass

    label('loc_1D83')

    TalkEnd(0x0010)

    Return()

# id: 0x000B offset: 0x1D87
@scena.Code('func_0B_1D87')
def func_0B_1D87():
    TalkBegin(0x0011)

    If(
        (
            (Expr.Eval, "OP_29(0x0009, 0x01, 0x0020)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0009, 0x01, 0x0010)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0009, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0009, 0x00, 0x04)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1DED',
    )

    ChrTalk(
        0x00FE,
        (
            '怎么这么吵啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，\n',
            '这里可是神圣的祈祷场所啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EAD')

    def _loc_1DED(): pass

    label('loc_1DED')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1E7C',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '前几天，\n',
            '我悄悄去森林里看了看女婿的工作情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '原来他也在以\n',
            '自己的方式努力工作着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '总觉得似乎还是缺点什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EAD')

    def _loc_1E7C(): pass

    label('loc_1E7C')

    ChrTalk(
        0x00FE,
        (
            '女婿的辛劳我承认，\n',
            '但总觉得他还是缺点什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1EAD(): pass

    label('loc_1EAD')

    TalkEnd(0x0011)

    Return()

# id: 0x000C offset: 0x1EB1
@scena.Code('func_0C_1EB1')
def func_0C_1EB1():
    TalkBegin(0x0012)

    If(
        (
            (Expr.Eval, "OP_29(0x0009, 0x01, 0x0020)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0009, 0x01, 0x0010)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0009, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0009, 0x00, 0x04)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1F5B',
    )

    ChrTalk(
        0x00FE,
        (
            '#0340150729V#600F喔，是艾丝蒂尔和约修亚啊。\n',
            '七耀石的事真是麻烦你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340150730V看你们这么慌乱，\n',
            '到底发生了什么事情呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2018')

    def _loc_1F5B(): pass

    label('loc_1F5B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1FE2',
    )

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '#0340010421V#601F喔，是艾丝蒂尔和约修亚啊。\n',
            '七耀石的事真是麻烦你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0340010422V今天我来这里找教区长有点事。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2018')

    def _loc_1FE2(): pass

    label('loc_1FE2')

    ChrTalk(
        0x00FE,
        (
            '#0340010423V#601F今天我来这里找教区长有点事。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2018(): pass

    label('loc_2018')

    TalkEnd(0x0012)

    Return()

# id: 0x000D offset: 0x201C
@scena.Code('func_0D_201C')
def func_0D_201C():
    TalkBegin(0x0013)

    ChrTalk(
        0x00FE,
        (
            '女神啊……\n',
            '请保佑老爷和夫人永远健康……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0013)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

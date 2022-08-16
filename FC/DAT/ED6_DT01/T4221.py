import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4221_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4221   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4221.x'
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
        ('ED6_DT07/CH02620._CH', 'ED6_DT07/CH02620P._CP'),
        ('ED6_DT07/CH02030._CH', 'ED6_DT07/CH02030P._CP'),
        ('ED6_DT07/CH02460._CH', 'ED6_DT07/CH02460P._CP'),
        ('ED6_DT07/CH02230._CH', 'ED6_DT07/CH02230P._CP'),
        ('ED6_DT07/CH02240._CH', 'ED6_DT07/CH02240P._CP'),
        ('ED6_DT07/CH02140._CH', 'ED6_DT07/CH02140P._CP'),
        ('ED6_DT07/CH02470._CH', 'ED6_DT07/CH02470P._CP'),
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT07/CH01270._CH', 'ED6_DT07/CH01270P._CP'),
        ('ED6_DT07/CH01350._CH', 'ED6_DT07/CH01350P._CP'),
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT07/CH02020._CH', 'ED6_DT07/CH02020P._CP'),
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
    ]

# id: 0x10001 offset: 0x11A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '玛多克工房长',
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
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '理查德上校',
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
            name                = '杜南公爵',
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
            name                = '管家菲利普',
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
            name                = '雪拉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '雷沃尔',
            x                   = 141250,
            z                   = 0,
            y                   = 7610,
            direction           = 278,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '妮舒',
            x                   = 78740,
            z                   = 0,
            y                   = -1880,
            direction           = 194,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '提妲',
            x                   = 83500,
            z                   = 0,
            y                   = -53540,
            direction           = 87,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '拉赛尔',
            x                   = 86170,
            z                   = 0,
            y                   = -52670,
            direction           = 275,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '奥利维尔',
            x                   = 139300,
            z                   = 0,
            y                   = 5970,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
    )

# id: 0x10002 offset: 0x25A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x25A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x25A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 139320,
            triggerZ            = 0,
            triggerY            = 7540,
            triggerRange        = 400,
            actorX              = 141250,
            actorZ              = 1500,
            actorY              = 7610,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x27E
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_28C',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_0B_1E66)

    def _loc_28C(): pass

    label('loc_28C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_29A',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, func_0E_427E)

    def _loc_29A(): pass

    label('loc_29A')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x0000006A, 'loc_2AA'),
        (0x0000006C, 'loc_2C0'),
        (-1, 'loc_2D6'),
    )

    def _loc_2AA(): pass

    label('loc_2AA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 5, 0x645)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2BD',
    )

    SetScenaFlags(ScenaFlag(0x00C8, 6, 0x646))
    Event(0, func_0D_2F18)

    def _loc_2BD(): pass

    label('loc_2BD')

    Jump('loc_2D6')

    def _loc_2C0(): pass

    label('loc_2C0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CE, 0, 0x670)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2D3',
    )

    SetScenaFlags(ScenaFlag(0x00CE, 0, 0x670))
    Event(0, func_0F_4CA3)

    def _loc_2D3(): pass

    label('loc_2D3')

    Jump('loc_2D6')

    def _loc_2D6(): pass

    label('loc_2D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2F8',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, 38180, 0, -59720, 90)

    def _loc_2F8(): pass

    label('loc_2F8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_322',
    )

    ChrSetChipByIndex(0x0000, 2)
    ChrSetChipByIndex(0x0001, 3)
    ChrSetChipByIndex(0x0138, 4)
    ChrSetFlags(0x0000, 0x1000)
    ChrSetFlags(0x0001, 0x1000)
    ChrSetFlags(0x0138, 0x1000)

    def _loc_322(): pass

    label('loc_322')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_34C',
    )

    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, 37930, 0, 59370, 97)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0010, 0x0080)

    Jump('loc_3F2')

    def _loc_34C(): pass

    label('loc_34C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_36B',
    )

    ChrClearFlags(0x000E, 0x0080)

    If(
        (
            (Expr.Eval, "OP_29(0x0055, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_368',
    )

    ChrClearFlags(0x0011, 0x0080)

    def _loc_368(): pass

    label('loc_368')

    Jump('loc_3F2')

    def _loc_36B(): pass

    label('loc_36B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_390',
    )

    ChrSetFlags(0x000D, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, 37840, 0, -58890, 90)

    Jump('loc_3F2')

    def _loc_390(): pass

    label('loc_390')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_3B5',
    )

    ChrSetFlags(0x000D, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, 37840, 0, -58890, 90)

    Jump('loc_3F2')

    def _loc_3B5(): pass

    label('loc_3B5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_3D5',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, 37840, 0, -58890, 90)

    Jump('loc_3F2')

    def _loc_3D5(): pass

    label('loc_3D5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_3F2',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, 37840, 0, -58890, 90)

    def _loc_3F2(): pass

    label('loc_3F2')

    Return()

# id: 0x0001 offset: 0x3F3
@scena.Code('func_01_3F3')
def func_01_3F3():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CE, 0, 0x670)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_409',
    )

    OP_1B(0x00, 0x00, 0x0010)
    OP_1B(0x06, 0x00, 0x0011)

    def _loc_409(): pass

    label('loc_409')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_413',
    )

    Jump('loc_44A')

    def _loc_413(): pass

    label('loc_413')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_41D',
    )

    Jump('loc_44A')

    def _loc_41D(): pass

    label('loc_41D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_42B',
    )

    OP_64(0x00, 0x0001)

    Jump('loc_44A')

    def _loc_42B(): pass

    label('loc_42B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_439',
    )

    OP_64(0x00, 0x0001)

    Jump('loc_44A')

    def _loc_439(): pass

    label('loc_439')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_443',
    )

    Jump('loc_44A')

    def _loc_443(): pass

    label('loc_443')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_44A',
    )

    def _loc_44A(): pass

    label('loc_44A')

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0002 offset: 0x454
@scena.Code('func_02_454')
def func_02_454():
    ExecExpressionWithReg(
        0x0000,
        (
            Expr.Rand,
            (Expr.PushLong, 0xE),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_479',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_5BB')

    def _loc_479(): pass

    label('loc_479')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_492',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_5BB')

    def _loc_492(): pass

    label('loc_492')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4AB',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_5BB')

    def _loc_4AB(): pass

    label('loc_4AB')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4C4',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_5BB')

    def _loc_4C4(): pass

    label('loc_4C4')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4DD',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_5BB')

    def _loc_4DD(): pass

    label('loc_4DD')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4F6',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_5BB')

    def _loc_4F6(): pass

    label('loc_4F6')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_50F',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_5BB')

    def _loc_50F(): pass

    label('loc_50F')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_528',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_5BB')

    def _loc_528(): pass

    label('loc_528')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_541',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_5BB')

    def _loc_541(): pass

    label('loc_541')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_55A',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_5BB')

    def _loc_55A(): pass

    label('loc_55A')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_573',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_5BB')

    def _loc_573(): pass

    label('loc_573')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_58C',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_5BB')

    def _loc_58C(): pass

    label('loc_58C')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5A5',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_5BB')

    def _loc_5A5(): pass

    label('loc_5A5')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5BB',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_5BB(): pass

    label('loc_5BB')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5D0',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_5BB')

    def _loc_5D0(): pass

    label('loc_5D0')

    Return()

# id: 0x0003 offset: 0x5D1
@scena.Code('func_03_5D1')
def func_03_5D1():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.Eval, "OP_29(0x0055, 0x00, 0x02)"),
            Expr.Return,
        ),
        'loc_9B8',
    )

    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, 137920, 0, 6450, 90)
    ChrSetPos(0x0102, 137940, 0, 5220, 90)
    ChrSetDirection(0x0011, 270, 0)
    ChrSetSubChip(0x0011, 0)
    CameraMove(138940, 0, 6080, 1000)

    ChrTalk(
        0x0011,
        (
            '#0040181621V#030F哟，艾丝蒂尔君、约修亚君。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040181622V好不容易迎来了诞辰庆典，\n',
            '不到市区里面尽情玩乐，\n',
            '是不是有点可惜呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181623V#505F（我说约修亚啊……\n',
            '　公告板上委托寻找的对象……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181624V#015F（毫无疑问就是此人……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0040181625V#033F呵，难道说你们俩……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040181626V想要邀请我\n',
            '一起享受午后的风花岁月吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040181627V#032F这样三个人一起……\n',
            '……也许会更加刺激……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040181628V#031F不错嘛，\n',
            '我就欣然接受吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0102, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    OP_63(0x0101)
    OP_63(0x0102)

    ChrTalk(
        0x0101,
        (
            '#0010181629V#001F哎呀，真巧啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181630V有一个热情胜过我们百倍千倍的人\n',
            '正在等着奥利维尔你哦～\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0011, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0011,
        (
            '#0040181631V#033F#5S什、什么……！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0040181632V#032F这、这、这是真的吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181633V#019F嗯，如果可以的话，\n',
            '让我们带你去那个人的地方怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0040181634V#030F呵，既然这样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040181635V#031F请你们立刻就带我去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_21()
    SetScenaFlags(ScenaFlag(0x007F, 5, 0x3FD))
    NewScene('ED6_DT01/T4121._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_109C')

    def _loc_9B8(): pass

    label('loc_9B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DD, 5, 0x6ED)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E0F',
    )

    SetScenaFlags(ScenaFlag(0x00DD, 5, 0x6ED))

    ChrTalk(
        0x0101,
        (
            '#0010140666V#004F咦，是奥利维尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0040140667V#030F哟，艾丝蒂尔君、约修亚君。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040140668V我从卡西乌斯先生那里听说了，\n',
            '你们终于成为了正游击士对吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040140669V#031F呵呵，恭喜恭喜，\n',
            '不愧是我的小猫咪啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140670V#007F不管你是什么态度……\n',
            '还是要多谢你一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140671V#010F对了，奥利维尔，\n',
            '你怎么会在这里呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140672V虽然听说你和我们一样，\n',
            '也被邀请参加今天的晚宴……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140673V#580F对、对啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140674V一个比任何人都喜欢庆典的男人，\n',
            '居然一个人在这种安静的地方喝酒……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140675V#005F难道说你是个冒牌货！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0040140676V#035F呵呵，\n',
            '我会让你们在协会获得正游击士资格时\n',
            '那种愉快的心情得以尽情展现的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040140677V对了，我要在格兰竞技场前\n',
            '开一个即兴的音乐会。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040140678V我的狂热支持者\n',
            '肯定会让你们满意的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110468V#509F说谎～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140680V#018F让我想起在哈肯大门\n',
            '听到你的演奏时的事情了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0040140681V#030F算了，我就远离诞辰庆典的热闹，\n',
            '一个人静静地喝点小酒吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040140682V#035F我那充满孤独和忧郁的背影，\n',
            '真是一种残酷的美啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040140683V这就是所谓男人的美学。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140684V#017F还是不知道你到这里的原因……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_109C')

    def _loc_E0F(): pass

    label('loc_E0F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DE, 5, 0x6F5)),
            (Expr.TestScenaFlags, ScenaFlag(0x00DE, 6, 0x6F6)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_101F',
    )

    SetScenaFlags(ScenaFlag(0x00DE, 6, 0x6F6))

    ChrTalk(
        0x0101,
        (
            '#0010140685V#501F啊，对了……\n',
            '老爸赶来的时候……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140686V奥利维尔，\n',
            '当时你和老爸说的那些话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0040140687V#033F哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140688V#014F确实……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140689V你们应该从来没有见过面，\n',
            '但是看起来父亲他\n',
            '像是知道你的事情一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0040140690V#036F………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040140691V#031F哈·哈·哈。\n',
            '你们～在说什～么啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040140692V我们～那时候～可没有～\n',
            '说什么～重～要的～事情啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140693V#509F（更觉得可疑了……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140694V#015F（嗯……\n',
            '　肯定是有什么事情瞒着我们。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_109C')

    def _loc_101F(): pass

    label('loc_101F')

    ChrTalk(
        0x0011,
        (
            '#0040140695V#035F呵呵，年轻的人们，\n',
            '尽情享受庆典的火热吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040140696V我是悠远森林中的隐者，\n',
            '驰骋于过去和未来的奇想。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_109C(): pass

    label('loc_109C')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x10A0
@scena.Code('func_04_10A0')
def func_04_10A0():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CE, 0, 0x670)),
            Expr.Return,
        ),
        'loc_1124',
    )

    ChrTalk(
        0x010B,
        (
            '#0541270006V#100F七至宝之一的『辉之环』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0541270007V连陛下也不知道\n',
            '遗迹到底在什么地方，\n',
            '上校又是听谁说的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1241')

    def _loc_1124(): pass

    label('loc_1124')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_1181',
    )

    ChrTalk(
        0x010B,
        (
            '#0541270011V#100F虽然理查德上校的政变风波暂时平息了，\n',
            '但是还留下不少谜团。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1241')

    def _loc_1181(): pass

    label('loc_1181')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x010B,
        (
            '#0541270008V#100F虽然理查德上校的政变风波暂时平息了，\n',
            '但是还留下不少谜团。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0541270009V王城的地下竟然有古代导力文明的遗迹……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0541270010V今后要重新对其进行全面的调查才行。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1241(): pass

    label('loc_1241')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x1245
@scena.Code('func_05_1245')
def func_05_1245():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CE, 0, 0x670)),
            Expr.Return,
        ),
        'loc_12B6',
    )

    ChrTalk(
        0x0107,
        (
            '#0070890014V#060F爷爷，\n',
            '从刚才开始你好像就一直在沉思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070890015V嗯～\n',
            '我们什么时候回蔡斯去啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1306')

    def _loc_12B6(): pass

    label('loc_12B6')

    ChrTalk(
        0x0107,
        (
            '#0070890016V#060F王城里的饭菜真好吃啊～\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070890017V真是太令人惊讶了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1306(): pass

    label('loc_1306')

    Return()

# id: 0x0006 offset: 0x1307
@scena.Code('func_06_1307')
def func_06_1307():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CE, 0, 0x670)),
            Expr.Return,
        ),
        'loc_1393',
    )

    ChrTalk(
        0x000C,
        (
            '#0030840015V#020F啊？\n',
            '约修亚不在房间里吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030840016V他肯定会在城里的，\n',
            '你去找找他吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030840017V艾丝蒂尔，加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13ED')

    def _loc_1393(): pass

    label('loc_1393')

    ChrTalk(
        0x000C,
        (
            '#0030840013V#020F约修亚和老师的房间\n',
            '应该就在隔壁吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030840014V艾丝蒂尔，加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13ED(): pass

    label('loc_13ED')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x13F1
@scena.Code('func_07_13F1')
def func_07_13F1():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '嗯……\n',
            '这边是拉赛尔博士和\n',
            '提妲小姐的房间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他们二人\n',
            '现在好像外出了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x1449
@scena.Code('func_08_1449')
def func_08_1449():
    Call(0, 0x0009)

    Return()

# id: 0x0009 offset: 0x144E
@scena.Code('func_09_144E')
def func_09_144E():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_147D',
    )

    ChrTalk(
        0x000D,
        (
            '哟，今天怎么只有你一个人呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1623')

    def _loc_147D(): pass

    label('loc_147D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1551',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_14E2',
    )

    ChrTalk(
        0x000D,
        (
            '那位理查德上校竟然是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '我至今还认为\n',
            '他不应该是那种\n',
            '会反叛女王陛下的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_154E')

    def _loc_14E2(): pass

    label('loc_14E2')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x000D,
        (
            '理查德上校\n',
            '每晚都会到这里来\n',
            '向我打听一些事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '至今我还是觉得他不应该是\n',
            '会反叛女王陛下的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_154E(): pass

    label('loc_154E')

    Jump('loc_1623')

    def _loc_1551(): pass

    label('loc_1551')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_155B',
    )

    Jump('loc_1623')

    def _loc_155B(): pass

    label('loc_155B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_1565',
    )

    Jump('loc_1623')

    def _loc_1565(): pass

    label('loc_1565')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_15C9',
    )

    ChrTalk(
        0x000D,
        (
            '作为饭后的消遣，\n',
            '来一杯饮料如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '就算菜单上没有的种类\n',
            '也可以立刻调配出来的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1623')

    def _loc_15C9(): pass

    label('loc_15C9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_1623',
    )

    ChrTalk(
        0x000D,
        (
            '这里是谈话室。\n',
            '请在这里放松一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '如果客人\n',
            '需要酒水的话，\n',
            '请尽管吩咐我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1623(): pass

    label('loc_1623')

    TalkEnd(0x000D)

    Return()

# id: 0x000A offset: 0x1627
@scena.Code('func_0A_1627')
def func_0A_1627():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 4, 0x63C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_19F2',
    )

    SetScenaFlags(ScenaFlag(0x00C7, 4, 0x63C))
    EventBegin(0x00)
    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, 38180, 0, -57660, 171)
    ChrSetPos(0x0102, 36300, 0, -58410, 135)
    CameraMove(37860, 0, -58600, 1000)

    ChrTalk(
        0x0008,
        (
            '#800F哦哦……\n',
            '艾丝蒂尔、约修亚！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F工房长先生！\n',
            '您果然也被邀请了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F因为邀请的都是市长级别的人物，\n',
            '所以觉得工房长肯定也会来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#800F你们才是，\n',
            '真没想到能得到武术大会冠军\n',
            '被邀请来格兰赛尔城呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550120338V呀哈……\n',
            '不愧是卡西乌斯的孩子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嘿嘿……\n',
            '因为得到了很多人的帮助嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F对了，最近这些天\n',
            '有什么动静吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550120341V#800F嗯……\n',
            '你们刚出发去王都，\n',
            '情报部的凯诺娜上尉就来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550120342V虽然没办法拒绝出席晚宴，\n',
            '不过关于你们潜入要塞的事，\n',
            '不管怎么说还是瞒过去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550120343V逃走的拉赛尔博士他们，\n',
            '好像也没有被军队发现。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过，这种情况再持续下去，\n',
            '被抓住也只是时间上的问题了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0551250005V#800F刚才，我向凯诺娜上尉提出\n',
            '要探望女王陛下的要求，\n',
            '很轻易就被拒绝了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550120347V果然还是很难直接见面吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F好像是呢……\n',
            '不过别担心，已经有办法了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F不管怎么说，\n',
            '一定要把博士的传言带给女王陛下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Jump('loc_1E65')

    def _loc_19F2(): pass

    label('loc_19F2')

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_1AFB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CE, 0, 0x670)),
            Expr.Return,
        ),
        'loc_1A72',
    )

    ChrTalk(
        0x0008,
        (
            '#0550120363V#800F街上还是那么热闹啊。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550120364V难得来一趟王都。\n',
            '回去之前就去酒馆里\n',
            '放松一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AF8')

    def _loc_1A72(): pass

    label('loc_1A72')

    ChrTalk(
        0x0008,
        (
            '#0550120365V#800F我和拉赛尔博士\n',
            '这么长时间不在中央工房，\n',
            '真是担心那边的情况啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550120366V我打算明天就乘『林德号』\n',
            '返回蔡斯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AF8(): pass

    label('loc_1AF8')

    Jump('loc_1E62')

    def _loc_1AFB(): pass

    label('loc_1AFB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1B05',
    )

    Jump('loc_1E62')

    def _loc_1B05(): pass

    label('loc_1B05')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Return,
        ),
        'loc_1B0F',
    )

    Jump('loc_1E62')

    def _loc_1B0F(): pass

    label('loc_1B0F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            Expr.Return,
        ),
        'loc_1D96',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1B97',
    )

    ChrTalk(
        0x0008,
        (
            '#0550120367V#800F听说陛下的病情有了好转，\n',
            '让人松了一口气啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550120368V只要知道这件事，\n',
            '来王都这一趟就值得了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D93')

    def _loc_1B97(): pass

    label('loc_1B97')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x0008,
        (
            '#0550120352V#800F希尔丹夫人，好久不见了。\n',
            '看到您这么有精神，真是太好了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0138,
        (
            '#710F玛多克工房长也没变呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120354V还是老样子，\n',
            '总是闲不下来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0551250003V#800F哈～哈，话说回来，\n',
            '中央工房优秀的新人辈出，\n',
            '让人甚感欣慰啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '而且听说陛下的病情有了好转，\n',
            '让人松了一口气啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0138,
        (
            '#0650120357V#710F……嗯，我想再过不久\n',
            '就可以和陛下见面了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120358V玛多克工房长，\n',
            '如果您有什么需要的话，\n',
            '请别客气，尽量提出来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650120359V我们会马上为您准备好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0551250004V#800F哦，让您费心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D93(): pass

    label('loc_1D93')

    Jump('loc_1E62')

    def _loc_1D96(): pass

    label('loc_1D96')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Return,
        ),
        'loc_1DFA',
    )

    ChrTalk(
        0x0008,
        (
            '#0550120361V#800F哦，艾丝蒂尔和约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550120362V怎么样，和女王陛下\n',
            '见到面了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E62')

    def _loc_1DFA(): pass

    label('loc_1DFA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Return,
        ),
        'loc_1E62',
    )

    ChrTalk(
        0x0008,
        (
            '#0550120350V#800F情报部的那些人\n',
            '非常地狡猾。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550120351V你们两个务必要\n',
            '谨慎小心地行动哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E62(): pass

    label('loc_1E62')

    TalkEnd(0x00FE)

    def _loc_1E65(): pass

    label('loc_1E65')

    Return()

# id: 0x000B offset: 0x1E66
@scena.Code('func_0B_1E66')
def func_0B_1E66():
    EventBegin(0x00)
    CameraMove(142500, 4850, 7580, 0)
    OP_67(0, 4770, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(0, 0)
    OP_6E(343, 0)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, 143590, 4000, 7800, 270)
    ChrSetPos(0x0101, 141480, 4000, 7160, 90)
    ChrSetPos(0x0102, 141270, 4000, 8340, 90)

    ChrTalk(
        0x0009,
        (
            '#0130120848V#110F……第一次见到卡西乌斯上校时\n',
            '我还刚从士官学校毕业。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120849V当时就分配到他率领的\n',
            '独立机动部队去了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120850V从那以后，直到他辞去军衔，\n',
            '我都在工作和生活方面受他照顾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F呵、呵－呵……\n',
            '是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '嗯，当时的父亲留给\n',
            '上校您什么样的印象呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#110F一句话，就是『英雄』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120854V称为『剑圣』也毫不为过的精湛技艺。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120855V任何战况都可以灵活应对，\n',
            '立体的全方位指挥能力……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120856V而且不仅仅是拥有各种战术，\n',
            '还有高超的战略能力来指挥部队……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0131090007V不管哪一项都无人能及。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F总、总感觉听起来\n',
            '好像不是他本人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120859V#010F父亲辞退军衔和那个\n',
            '『百日战役』是同时的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#110F嗯……\n',
            '我当时在卡西乌斯上校的麾下战斗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120861V到现在我都还记得很清楚……\n',
            '他所部署的奇迹般的作战\n',
            '开始时所带来的热情与兴奋……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '一说起那个时候的事情，\n',
            '再有多少时间都不够，\n',
            '以后有机会我会和你们慢慢道来的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120863V但仅凭这些就可以断定了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '如果那时没有一位叫做卡西乌斯·布莱特\n',
            '的男人，这个利贝尔就已经被\n',
            '埃雷波尼亚给吸收吞并了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F不、不会吧！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120866V的确有些\n',
            '难以置信……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0130120867V#110F呵呵，能将难以置信之事\n',
            '化为可能的就是『英雄』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120868V而且在战争之后很快就退役了，\n',
            '拒绝了女王陛下授予的勋章，\n',
            '不让世人知道其威名……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120869V至今为止，在一部分军人之中\n',
            '还把卡西乌斯上校的名字作为英雄的代名词。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F唔－……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那个小气的老爸，这样的事情\n',
            '竟然一个字也没有给我提起过！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120872V#010F如果特地和女儿说这番话，\n',
            '也不见得她能听得进去啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120873V若是责备父亲的话，他也太可怜了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F可、可怜的是我们啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '……说起来，约修亚你\n',
            '似乎不是很吃惊啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120876V难道……\n',
            '刚才那些话你是都知道的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F理查德上校是\n',
            '父亲的部下这一点\n',
            '的确是不知道的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过……其他的我是明白的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F什、什么～！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120880V这么说约修亚就是共犯了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F冷、冷静一点，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120882V我是从别的地方得知的，父亲\n',
            '并没有告诉过我。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120883V而且父亲也不需要特地\n',
            '的来告诉你这些事情啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F唔～不太令人信服哦～……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '可真是的，回去之后\n',
            '一定要好好教训他一顿！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0130120886V#110F呵呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，这个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F非、非常抱歉。\n',
            '中途打断了您说话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#110F哪里……\n',
            '看见你们这样我也稍感安心了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120890V卡西乌斯先生要辞去军衔时，\n',
            '我拼命的想挽留住他……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120891V不过那样的选择\n',
            '对于他来说也许是最合适的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '有你们在他身旁陪伴，\n',
            '失去夫人的悲痛\n',
            '一定会逐渐化解掉的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F理查德上校……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2826')
    def lambda_2826():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_2826')

    DispatchAsync2(0x0101, 0x0001, lambda_2826)

    @scena.Lambda('lambda_2837')
    def lambda_2837():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_2837')

    DispatchAsync2(0x0102, 0x0001, lambda_2837)

    ChrMoveTo(0x0009, 143800, 4000, 6180, 2000, 0x00)

    ChrTalk(
        0x0009,
        (
            '#110F那么……\n',
            '多谢你们能陪我说会儿话。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120896V因为公爵大人\n',
            '还在等着的，\n',
            '我就先告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊……好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120898V#010F抱歉，我们完全是\n',
            '在听您怎么说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#110F不，你们让我得知了\n',
            '我最想知道的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '……这样一来我就没有什么可以留恋的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哎……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F这究竟……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#110F哈哈，最近一段时间\n',
            '我们还会有机会见面的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120904V那时就可以和卡西乌斯上校\n',
            '以及你们一起聊聊了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0102, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    CreateThread(0x0009, 0x01, 0x00, func_0C_2EC7)

    @scena.Lambda('lambda_2A27')
    def lambda_2A27():
        CameraMove(143890, 2750, 1780, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2A27)

    @scena.Lambda('lambda_2A3F')
    def lambda_2A3F():
        OP_6C(45000, 4000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_2A3F)

    Sleep(5000)

    OP_63(0x0101)
    OP_63(0x0102)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    CameraMove(142230, 4850, 7220, 2000)

    ChrTalk(
        0x0101,
        (
            '#000F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '刚才那个人\n',
            '真的是理查德上校吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F我说……\n',
            '你睡迷糊了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F可、可是他如此钦佩的\n',
            '说着老爸过去的事情……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120909V不过……\n',
            '和以往留下的印象不同啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F……的确。\n',
            '并不像是一个坏人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '可是，抛开这个不提，\n',
            '他肯定是有什么企图的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120912V否则怎么会对父亲的事情\n',
            '了解的那么清楚明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯……\n',
            '话是这么说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F丑话先说在前面……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120915V把我们这么亲切的找来\n',
            '也许是有什么目的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '像他那样的情报专家，\n',
            '要想欺骗我们这样的小孩，\n',
            '简直是易如反掌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F你、你确信刚才你说\n',
            '的那些没有言过其实吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F嗯……确信。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120919V防人之心不可无。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120920V你只要相信你自己\n',
            '的直觉就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F要做好各种准备，\n',
            '不可掉以轻心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120923V游击士所要做到的……\n',
            '我认为就是这样的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F约修亚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '嗯，我明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '虽然没有什么自信，不过\n',
            '我会牢记在心的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F……谢谢你，艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F什么～啊。\n',
            '约修亚你怎么和我讲起礼来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F接下来我们要立刻\n',
            '赶到希尔丹夫人那里去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120930V大概已经等的不耐烦了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F是呀……\n',
            '这就前去女佣休息室吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(300)

    Fade(1000)
    ChrSetPos(0x0101, 142340, 4000, 5440, 169)
    ChrSetPos(0x0102, 142340, 4000, 5440, 169)
    ChrSetFlags(0x0009, 0x0080)
    EventEnd(0x00)

    Return()

# id: 0x000C offset: 0x2EC7
@scena.Code('func_0C_2EC7')
def func_0C_2EC7():
    ChrWalkTo(0x00FE, 148120, 4000, 5230, 3000, 0x00)
    ChrWalkTo(0x00FE, 147920, 2000, -1500, 3000, 0x00)
    ChrWalkTo(0x00FE, 140850, 0, -1500, 3000, 0x00)
    ChrWalkTo(0x00FE, 132710, 0, 800, 3000, 0x00)

    Return()

# id: 0x000D offset: 0x2F18
@scena.Code('func_0D_2F18')
def func_0D_2F18():
    EventBegin(0x00)
    CameraMove(88610, 0, 6390, 0)
    ChrSetChipByIndex(0x0101, 3)
    ChrSetChipByIndex(0x0102, 4)
    ChrSetChipByIndex(0x0138, 2)
    ChrSetPos(0x0138, 87950, 0, 4590, 0)
    ChrSetPos(0x0101, 87640, 0, 6230, 90)
    ChrSetPos(0x0102, 89210, 0, 6370, 270)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '呼……\n',
            '约修亚你可真受欢迎啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那个家伙一听到约修亚的名字，\n',
            '顿时就两眼放光呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F哪、哪有那样的事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '倒是你呀，\n',
            '不还顶撞了他吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F我那个时候面对那个家伙\n',
            '一点紧张感都没有。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '呼，不管怎么说还是\n',
            '有些不够自信啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F我说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x000A, 93780, 0, 850, 90)
    ChrSetPos(0x000B, 93780, 0, 850, 90)

    ChrTalk(
        0x000A,
        (
            '#0640121375V嗝……\n',
            '什么东西吵吵嚷嚷的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x000A, 0x0080)
    ChrSetFlags(0x000A, 0x0040)

    @scena.Lambda('lambda_30CD')
    def lambda_30CD():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_30CD)

    @scena.Lambda('lambda_30DB')
    def lambda_30DB():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_30DB)

    @scena.Lambda('lambda_30E9')
    def lambda_30E9():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0138, 0x0001, lambda_30E9)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0138, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    CameraMove(90380, 0, 5100, 1000)

    @scena.Lambda('lambda_314D')
    def lambda_314D():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_314D')

    DispatchAsync2(0x0101, 0x0001, lambda_314D)

    @scena.Lambda('lambda_315E')
    def lambda_315E():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_315E')

    DispatchAsync2(0x0102, 0x0001, lambda_315E)

    @scena.Lambda('lambda_316F')
    def lambda_316F():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_316F')

    DispatchAsync2(0x0138, 0x0001, lambda_316F)

    @scena.Lambda('lambda_3180')
    def lambda_3180():
        CameraMove(89070, 0, 5570, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3180)

    @scena.Lambda('lambda_3198')
    def lambda_3198():
        ChrWalkTo(0x00FE, 90890, 0, 1590, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_3198)

    WaitForThreadExit(0x000A, 0x0001)
    ChrClearFlags(0x000B, 0x0080)

    @scena.Lambda('lambda_31BD')
    def lambda_31BD():
        ChrWalkTo(0x00FE, 89350, 0, 4440, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_31BD)

    @scena.Lambda('lambda_31D8')
    def lambda_31D8():
        ChrWalkTo(0x00FE, 90890, 0, 1590, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_31D8)

    WaitForThreadExit(0x000B, 0x0001)

    @scena.Lambda('lambda_31F8')
    def lambda_31F8():
        ChrWalkTo(0x00FE, 89760, 0, 3500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_31F8)

    WaitForThreadExit(0x000A, 0x0001)

    @scena.Lambda('lambda_3218')
    def lambda_3218():
        ChrTurnDirection(0x00FE, 0x0138, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_3218)

    ChrTalk(
        0x0138,
        (
            '#710F公爵大人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#220F我说什么呢，这不是女管家吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x000A, 0x0101, 400)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '#220F哦哟……\n',
            '怎么，那两个侍女是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640121379V嗝……\n',
            '以前没有见过的生面孔啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CE, 6, 0x676)),
            Expr.Return,
        ),
        'loc_334E',
    )

    ChrTalk(
        0x0138,
        (
            '#0650860009V#710F新来的实习侍女，\n',
            '莱娜和卡玲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121381V因为对城里还不熟悉，\n',
            '所以带领她们到处走走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_343B')

    def _loc_334E(): pass

    label('loc_334E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CE, 7, 0x677)),
            Expr.Return,
        ),
        'loc_33C5',
    )

    ChrTalk(
        0x0138,
        (
            '#0650860010V#710F新来的实习侍女，\n',
            '雪拉和卡玲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121381V因为对城里还不熟悉，\n',
            '所以带领她们到处走走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_343B')

    def _loc_33C5(): pass

    label('loc_33C5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CF, 0, 0x678)),
            Expr.Return,
        ),
        'loc_343B',
    )

    ChrTalk(
        0x0138,
        (
            '#0650860011V#710F新来的实习侍女，\n',
            '朵洛希和卡玲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121381V因为对城里还不熟悉，\n',
            '所以带领她们到处走走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_343B(): pass

    label('loc_343B')

    ChrTalk(
        0x000B,
        (
            '#720F哦哟……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x000B, 90180, 0, 4270, 2000, 0x00)
    ChrWalkTo(0x000B, 89920, 0, 5310, 2000, 0x00)
    ChrTurnDirection(0x000B, 0x0102, 400)
    Sleep(500)

    ChrTurnDirection(0x000B, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x000B,
        (
            '#720F…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F（啊……注意到了？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F（……糟糕了。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '（和这个人见过几次面，\n',
            '被注意到也不奇怪……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#220F怎么了，菲利普。\n',
            '目不转睛的盯着看……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '哇哈哈，对于你这样正经古板的人\n',
            '来说，这真是稀罕得很啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0660121393V#720F失礼了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660121394V因为和我的侄女比较相似，\n',
            '所以一下就呆住了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660121395V两位姑娘，\n',
            '我非常的抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，没关系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F请不要介意……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#220F呵，仔细一看不管哪一个\n',
            '都是精选的上等货色啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640121399V尤其是棕色头发那位，\n',
            '极为阳光啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F（喂喂……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#220F黑色头发的那位再稍微\n',
            '把腰挺直一些就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F……惶、惶恐之至。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#220F呼，那么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CE, 6, 0x676)),
            Expr.Return,
        ),
        'loc_3760',
    )

    ChrTalk(
        0x000A,
        (
            '#0641110002V#220F莱娜！\n',
            '我命令你今晚来伺候我！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_37DB')

    def _loc_3760(): pass

    label('loc_3760')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CE, 7, 0x677)),
            Expr.Return,
        ),
        'loc_379E',
    )

    ChrTalk(
        0x000A,
        (
            '#0641110003V#220F雪拉！\n',
            '我命令你今晚来伺候我！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_37DB')

    def _loc_379E(): pass

    label('loc_379E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CF, 0, 0x678)),
            Expr.Return,
        ),
        'loc_37DB',
    )

    ChrTalk(
        0x000A,
        (
            '#0641110004V#220F朵洛希！\n',
            '我命令你今晚来伺候我！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_37DB(): pass

    label('loc_37DB')

    ChrTalk(
        0x0101,
        (
            '#000F哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x000A, 400)

    ChrTalk(
        0x000B,
        (
            '#0660850001V#720F公、公爵大人！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F（咦，什么叫伺候呢？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F（唔，怎么说好呢……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0138,
        (
            '#0650860012V#710F大人，再怎么说，\n',
            '玩笑也开得有些过分了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121413V在城里工作的侍女全都是\n',
            '诚心服侍女王陛下的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121414V您忘记了这一点吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#220F我知道，我知道……\n',
            '连玩笑的开不起的家伙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '嗝，反正一周之后\n',
            '这个城就是我的了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640121417V到那时我再来好好\n',
            '享用这番乐趣吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0138,
        (
            '#710F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#720F大、大人！\n',
            '请适可而止！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660121420V暴饮暴食姑且不论，\n',
            '沉溺女色简直岂有此理！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660121421V我菲利普就算拼了老命\n',
            '也要劝阻大人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x000B, 400)

    ChrTalk(
        0x000A,
        (
            '#220F我已经说了\n',
            '我是开玩笑的！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640121423V够了！\n',
            '今晚赶快回去休息吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#720F大、大人\n',
            '所言极是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '大人您的房间就在前面，\n',
            ' ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3AC0')
    def lambda_3AC0():
        CameraMove(87270, 0, 5910, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3AC0)

    @scena.Lambda('lambda_3AD8')
    def lambda_3AD8():
        ChrWalkTo(0x00FE, 88470, 0, 5250, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_3AD8)

    Sleep(600)

    @scena.Lambda('lambda_3AF8')
    def lambda_3AF8():
        ChrWalkTo(0x00FE, 86510, 0, 5570, 1300, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_3AF8)

    WaitForThreadExit(0x000A, 0x0001)

    @scena.Lambda('lambda_3B18')
    def lambda_3B18():
        ChrWalkTo(0x00FE, 85560, 0, 5560, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_3B18)

    WaitForThreadExit(0x000A, 0x0001)
    Sleep(1000)

    @scena.Lambda('lambda_3B3D')
    def lambda_3B3D():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_3B3D')

    DispatchAsync2(0x000B, 0x0002, lambda_3B3D)

    @scena.Lambda('lambda_3B4E')
    def lambda_3B4E():
        ChrTurnDirection(0x000A, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_3B4E)

    ChrMoveTo(0x000A, 85650, 0, 6380, 1000, 0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CE, 6, 0x676)),
            Expr.Return,
        ),
        'loc_3B94',
    )

    ChrTalk(
        0x000A,
        (
            '#220F嗯～……\n',
            '对了，莱娜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3BE7')

    def _loc_3B94(): pass

    label('loc_3B94')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CE, 7, 0x677)),
            Expr.Return,
        ),
        'loc_3BBE',
    )

    ChrTalk(
        0x000A,
        (
            '#220F嗯～……\n',
            '对了，雪拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3BE7')

    def _loc_3BBE(): pass

    label('loc_3BBE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CF, 0, 0x678)),
            Expr.Return,
        ),
        'loc_3BE7',
    )

    ChrTalk(
        0x000A,
        (
            '#220F嗯～……\n',
            '对了，朵洛希。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3BE7(): pass

    label('loc_3BE7')

    ChrTalk(
        0x000A,
        (
            '#220F如果有什么困难\n',
            '不用顾虑，尽管找我商量。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640121428V新一代的国王我会\n',
            '亲自帮你解决的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊哈……哈哈……\n',
            '还要多谢你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#220F哇哈哈，可爱的宝贝儿。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '嗯……愉快愉快！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3CAB')
    def lambda_3CAB():
        CameraMove(83810, 0, 6600, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3CAB)

    ChrWalkTo(0x000A, 78870, 0, 6990, 1500, 0x00)
    ChrWalkTo(0x000A, 78870, 0, 9590, 1500, 0x00)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0138, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)

    @scena.Lambda('lambda_3CFF')
    def lambda_3CFF():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_3CFF')

    DispatchAsync2(0x0101, 0x0001, lambda_3CFF)

    @scena.Lambda('lambda_3D10')
    def lambda_3D10():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_3D10')

    DispatchAsync2(0x0102, 0x0001, lambda_3D10)

    @scena.Lambda('lambda_3D21')
    def lambda_3D21():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_3D21')

    DispatchAsync2(0x0138, 0x0001, lambda_3D21)

    @scena.Lambda('lambda_3D32')
    def lambda_3D32():
        CameraMove(88010, 0, 6080, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3D32)

    ChrSetDirection(0x000B, 90, 400)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x000B,
        (
            '#720F让你们受惊了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660121439V大人明天一早起来的时候，\n',
            '就什么也记不起来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660121440V请你们放心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0138,
        (
            '#710F……希望会是如此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0660121442V#720F真的非常抱歉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660121443V夫人、两位姑娘，\n',
            '那我就告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x000B, 84430, 0, 3640, 3000, 0x00)
    ChrWalkTo(0x000B, 81380, 0, 3930, 3000, 0x00)
    ChrWalkTo(0x000B, 79030, 0, 6280, 3000, 0x00)
    ChrWalkTo(0x000B, 79030, 0, 9870, 3000, 0x00)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0138, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)

    ChrTalk(
        0x0138,
        (
            '#710F唉，谈到那个男的啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121445V \n',
            '那样无益的负担呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0138, 400)

    ChrTalk(
        0x0101,
        (
            '#000F咦，希尔丹夫人\n',
            '和菲利普先生认识吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0138, 0x0101, 400)

    ChrTalk(
        0x0138,
        (
            '#710F在年幼的时候就认识了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650860013V可是到了今天，不管在工作方面\n',
            '还是在立场方面都有了距离……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0138, 400)

    ChrTalk(
        0x0102,
        (
            '#010F是这样的啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F的确，菲利普先生看起来\n',
            '就是一副饱经沧桑的感觉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '他对公爵被上校唆使这件事\n',
            '好像非常担心的样子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#010F很有可能……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '对了，艾丝蒂尔，\n',
            '你不也很受欢迎吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121454V公爵看来很喜欢你呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#000F哼，你好像有些\n',
            '幸灾乐祸啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '啊，到底那个\n',
            '『伺候』是什么意思呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F这、这个嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0138,
        (
            '#710F艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650121459V向异性提出这种问题，\n',
            '会让对方很难为情哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4129')
    def lambda_4129():
        ChrTurnDirection(0x00FE, 0x0138, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_4129)

    ChrTurnDirection(0x0101, 0x0138, 400)

    ChrTalk(
        0x0101,
        (
            '#000F哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0138,
        (
            '#0650121461V#710F……把耳朵凑过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 0)
    ChrWalkTo(0x0138, 87590, 0, 5700, 2000, 0x00)
    ChrSetDirection(0x0101, 270, 400)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '希尔丹夫人\n',
            '对艾丝蒂尔说了悄悄话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    ChrMoveTo(0x0138, 87950, 0, 4590, 1000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#000F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0138,
        (
            '#710F……明白了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0138, 400)

    ChrTalk(
        0x0101,
        (
            '#000F啊，哦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '…………知道了………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F（到底说了些什么呢……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T4214._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000E offset: 0x427E
@scena.Code('func_0E_427E')
def func_0E_427E():
    EventBegin(0x00)
    FormationDelMember(0x01, 0xFF)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, 33230, 0, 57840, 90)
    ChrSetPos(0x0101, 36130, 0, 59420, 0)
    CameraMove(36050, 0, 58110, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    @scena.Lambda('lambda_42ED')
    def lambda_42ED():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_42ED')

    DispatchAsync2(0x000C, 0x0001, lambda_42ED)

    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    ChrWalkTo(0x0101, 35980, 0, 56680, 2000, 0x00)
    Sleep(500)

    ChrSetDirection(0x0101, 0, 400)
    ChrWalkTo(0x0101, 36130, 0, 59420, 2000, 0x00)
    Sleep(500)

    ChrSetDirection(0x0101, 180, 400)
    ChrWalkTo(0x0101, 35980, 0, 56680, 2000, 0x00)
    Sleep(500)

    OP_63(0x0101)

    ChrTalk(
        0x0101,
        (
            '#000F唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0030141161V#020F怎么了，艾丝蒂尔。\n',
            '从刚才开始就静不下来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030141162V你在担心什么吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000C, 400)

    ChrTalk(
        0x0101,
        (
            '#000F嗯、嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我说，雪拉姐……\n',
            '约修亚的样子是不是很奇怪？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#020F？？？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030141167V奇怪的是你啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030141168V那孩子不是\n',
            '和平时一样沉着冷静吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F话是这样说没错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000C, 0x00000000, 2000, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000C,
        (
            '#020F哈哈。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030141171V是吗，原来是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F怎、怎么了突然……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4509')
    def lambda_4509():
        CameraMove(35600, 0, 56920, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4509)

    ChrWalkTo(0x000C, 35230, 0, 57100, 2000, 0x00)

    ChrTalk(
        0x000C,
        (
            '#020F你瞒不住我的～⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030141174V我感到那种气氛了呢……\n',
            '你自己也明白吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '你啊……\n',
            '是不是喜欢上约修亚了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F………呜…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '果、果然知道了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#020F不好意思哦～让我发现了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030141179V不过你这个样子，\n',
            '可没办法向约修亚传达真正的心意哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯……我也这样觉得……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '约修亚从以前开始，\n',
            '对这方面的事情就很迟钝……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#020F哎呀，真是单纯的想法啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030141184V那个不谙世事的艾丝蒂尔，\n',
            '也终于走到这一步了呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030141185V姐姐我真是感动啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F……再这样的话，\n',
            '我就不和雪拉姐说啦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#020F抱歉抱歉，\n',
            '我不开玩笑了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过，真是的啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030141189V仔细想想，你们\n',
            '在进入青春期以前就已经认识了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030141190V所以没有注意到对方心情的变化\n',
            '也是没办法的事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F是，是这样吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我在旅行的途中，\n',
            '开始慢慢有这种感觉……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '每次有这样的心情时，\n',
            '都会很快注意到……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '啊啊，真是的，\n',
            '这样根本不像我嘛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#020F呵呵……\n',
            '没有不会绽放的花蕾呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030141196V女孩子都是这样的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F雪拉姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#020F虽然不能轻率地\n',
            '就表达自己的心意……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030141199V不过，如果你已经下定决心的话，\n',
            '说出来不是更好吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030840018V如果不说的话，就什么也不会发生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯……\n',
            '其实，我已经下定决心了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141202V而且也和他约定过要听他说自己的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#020F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '好，这样才是我的妹妹嘛！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030141205V哎呀，\n',
            '姐姐我都要感动地哭了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F能不能给我适可而止啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过，谢谢你，雪拉姐。\n',
            '我好像有点勇气了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141208V我这就去\n',
            '约修亚那里看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#020F哎……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030141210V不、不会现在就要告白吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F不是啦，是另外的事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141212V刚才，约修亚的样子\n',
            '确实有点奇怪呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141213V我先问问他是怎么回事吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#020F是，是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过，你还真是\n',
            '对他的事情很了解啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '你和约修亚\n',
            '一定会进行得很顺利的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030141217V如果谈话的时候气氛不错，\n',
            '干脆就这样告白吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F呜……尽量吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那么，我走了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4C1E')
    def lambda_4C1E():
        CameraMove(34760, 0, 54010, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4C1E)

    ChrWalkTo(0x0101, 34890, 0, 50370, 5000, 0x00)

    @scena.Lambda('lambda_4C4A')
    def lambda_4C4A():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4C4A)

    ChrWalkTo(0x0101, 35020, 0, 48980, 5000, 0x00)

    ChrTalk(
        0x000C,
        (
            '#020F……初恋吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '如果能顺利就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    NewScene('ED6_DT01/T4221._SN', 101, 0, 0)
    IdleLoop()

    Return()

# id: 0x000F offset: 0x4CA3
@scena.Code('func_0F_4CA3')
def func_0F_4CA3():
    EventBegin(0x00)
    CameraMove(78150, 0, 55830, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 79820, 0, 50600, 0)
    CameraMove(89010, 0, 56310, 3000)
    ChrSetPos(0x0101, 79700, 0, 55220, 90)
    CameraMove(79690, 0, 55490, 2000)

    ChrTalk(
        0x0101,
        (
            '#000F哎……\n',
            '两个人都不在啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '对了，\n',
            '老爸说过还要开会……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141226V可是，约修亚呢……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrSetDirection(0x0101, 180, 400)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#000F约修亚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '是在哪里吹的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_1B(0x00, 0x00, 0xFFFF)
    OP_1B(0x06, 0x00, 0xFFFF)
    EventEnd(0x00)

    Return()

# id: 0x0010 offset: 0x4DDE
@scena.Code('func_10_4DDE')
def func_10_4DDE():
    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0010141222V#007F哎呀，我真是的。\n',
            '这是往哪里走啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141223V#000F……不赶快去约修亚的房间的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0011 offset: 0x4E67
@scena.Code('func_11_4E67')
def func_11_4E67():
    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0010141222V#007F哎呀，我真是的。\n',
            '这是往哪里走啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010141223V#000F……不赶快去约修亚的房间的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

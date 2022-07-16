import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3221_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3221   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '毛婆婆'),
    TXT(0x02, '艾德'),
    TXT(0x03, '拜舍尔'),
    TXT(0x04, '林'),
    TXT(0x05, '莉西亚'),
    TXT(0x06, '希利尔'),
    TXT(0x07, '艾缇'),
    TXT(0x08, '拉克'),
    TXT(0x09, '希玛'),
    TXT(0x0A, '库安'),
    TXT(0x0B, '西加罗'),
    TXT(0x0C, '艾德尔'),
    TXT(0x0D, '东方打扮的男人'),
    TXT(0x0E, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3221.x'
    header.mapIndex       = 1
    header.bgm            = 15
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x43E0
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
        ('ED6_DT07/CH02430._CH', 'ED6_DT07/CH02430P._CP'),
        ('ED6_DT07/CH01270._CH', 'ED6_DT07/CH01270P._CP'),
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH01160._CH', 'ED6_DT07/CH01160P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01060._CH', 'ED6_DT07/CH01060P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH01043._CH', 'ED6_DT07/CH01043P._CP'),
        ('ED6_DT07/CH01213._CH', 'ED6_DT07/CH01213P._CP'),
        ('ED6_DT07/CH00073._CH', 'ED6_DT07/CH00073P._CP'),
    ]

# id: 0x10002 offset: 0x122
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 2590,
            z                   = 250,
            y                   = 5360,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
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
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
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
            talkScenaIndex      = 0x0009,
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
            talkScenaIndex      = 0x000A,
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
            talkScenaIndex      = 0x000C,
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
            talkScenaIndex      = 0x000E,
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
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
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
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 14070,
            z                   = 0,
            y                   = 2040,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
    )

# id: 0x10003 offset: 0x2C2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x2C2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x2C2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 8960,
            triggerZ            = 250,
            triggerY            = 13840,
            triggerRange        = 1000,
            actorX              = 9100,
            actorZ              = 1750,
            actorY              = 13840,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0016,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 5290,
            triggerZ            = 0,
            triggerY            = 71030,
            triggerRange        = 800,
            actorX              = 5290,
            actorZ              = 1000,
            actorY              = 71030,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0017,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 2670,
            triggerZ            = 250,
            triggerY            = 3820,
            triggerRange        = 400,
            actorX              = 2590,
            actorZ              = 1750,
            actorY              = 5360,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0011,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 9940,
            triggerZ            = 0,
            triggerY            = 90,
            triggerRange        = 400,
            actorX              = 8490,
            actorZ              = 1500,
            actorY              = 340,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x352
@scena.Code('PreInit')
def PreInit():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_362'),
        (0x0000006D, 'loc_390'),
        (-1, 'loc_3A6'),
    )

    def _loc_362(): pass

    label('loc_362')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 5, 0x51D)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 4, 0x51C)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_375',
    )

    SetScenaFlags(ScenaFlag(0x00A3, 5, 0x51D))
    Event(0, 0x0013)

    def _loc_375(): pass

    label('loc_375')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 0, 0x520)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_38D',
    )

    SetMapFlags(0x10000000)
    SetScenaFlags(ScenaFlag(0x00A4, 0, 0x520))
    Event(0, 0x0014)

    def _loc_38D(): pass

    label('loc_38D')

    Jump('loc_3A6')

    def _loc_390(): pass

    label('loc_390')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 5, 0x525)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3A3',
    )

    SetScenaFlags(ScenaFlag(0x00A4, 6, 0x526))
    Event(0, 0x0015)

    def _loc_3A3(): pass

    label('loc_3A3')

    Jump('loc_3A6')

    def _loc_3A6(): pass

    label('loc_3A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_3DC',
    )

    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, -30310, -250, 8840, 81)
    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x000E, 8490, 0, 340, 102)

    Jump('loc_6E2')

    def _loc_3DC(): pass

    label('loc_3DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_45B',
    )

    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x000A, 10430, 0, 1740, 270)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, -30310, -250, 8840, 81)
    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, -1040, 0, 40770, 2)
    ClearChrFlags(0x0012, 0x0080)
    SetChrPos(0x0012, -28880, 0, 43500, 9)
    ClearChrFlags(0x0013, 0x0080)
    SetChrPos(0x0013, -28740, 0, 38750, 93)
    CreateThread(0x0013, 0x00, 0x00, 0x0003)

    Jump('loc_6E2')

    def _loc_45B(): pass

    label('loc_45B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_4D1',
    )

    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x000A, 10430, 0, 1740, 270)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, -30310, -250, 8840, 81)
    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x000E, 8490, 0, 340, 102)
    ClearChrFlags(0x0013, 0x0080)
    SetChrPos(0x0013, -28740, 0, 38750, 93)
    CreateThread(0x0013, 0x00, 0x00, 0x0003)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 0, 0x558)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4CE',
    )

    ClearChrFlags(0x0014, 0x0080)

    def _loc_4CE(): pass

    label('loc_4CE')

    Jump('loc_6E2')

    def _loc_4D1(): pass

    label('loc_4D1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_559',
    )

    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, -30310, -250, 8840, 81)
    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x000E, 8490, 0, 340, 102)
    ClearChrFlags(0x0012, 0x0080)
    SetChrChipByIndex(0x0012, 12)
    TerminateThread(0x0012, 0x00)
    SetChrFlags(0x0012, 0x0010)
    SetChrFlags(0x0012, 0x0004)
    SetChrPos(0x0012, 11260, 150, 10650, 180)
    ClearChrFlags(0x0013, 0x0080)
    SetChrChipByIndex(0x0013, 13)
    TerminateThread(0x0013, 0x00)
    SetChrFlags(0x0013, 0x0010)
    SetChrFlags(0x0013, 0x0004)
    SetChrPos(0x0013, 11070, 150, 8460, 358)

    Jump('loc_6E2')

    def _loc_559(): pass

    label('loc_559')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_5A5',
    )

    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x000A, 10430, 0, 1740, 270)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, -30310, -250, 8840, 81)
    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x000E, 8490, 0, 340, 102)

    Jump('loc_6E2')

    def _loc_5A5(): pass

    label('loc_5A5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_643',
    )

    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, -30310, -250, 8840, 81)
    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x000E, 8490, 0, 340, 102)
    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, -1040, 0, 40770, 2)
    ClearChrFlags(0x0012, 0x0080)
    SetChrChipByIndex(0x0012, 12)
    TerminateThread(0x0012, 0x00)
    SetChrFlags(0x0012, 0x0010)
    SetChrFlags(0x0012, 0x0004)
    SetChrPos(0x0012, 11260, 150, 10650, 180)
    ClearChrFlags(0x0013, 0x0080)
    SetChrChipByIndex(0x0013, 13)
    TerminateThread(0x0013, 0x00)
    SetChrFlags(0x0013, 0x0010)
    SetChrFlags(0x0013, 0x0004)
    SetChrPos(0x0013, 11070, 150, 8460, 358)

    Jump('loc_6E2')

    def _loc_643(): pass

    label('loc_643')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Return,
        ),
        'loc_679',
    )

    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x000A, 10430, 0, 1740, 270)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, 2230, 250, 3550, 0)

    Jump('loc_6E2')

    def _loc_679(): pass

    label('loc_679')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_699',
    )

    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, 11910, 0, 67870, 180)

    Jump('loc_6E2')

    def _loc_699(): pass

    label('loc_699')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_6E2',
    )

    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, -30310, -250, 8840, 81)
    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x000E, 8490, 0, 340, 102)
    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, -2080, 250, 6150, 195)

    def _loc_6E2(): pass

    label('loc_6E2')

    Return()

# id: 0x0001 offset: 0x6E3
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6FB',
    )

    OP_B1('t3221_y')

    Jump('loc_704')

    def _loc_6FB(): pass

    label('loc_6FB')

    OP_B1('t3221_n')

    def _loc_704(): pass

    label('loc_704')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 1, 0x529)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_718',
    )

    OP_72(0x0002, 0x0010)

    Jump('loc_71C')

    def _loc_718(): pass

    label('loc_718')

    OP_64(0x01, 0x0001)

    def _loc_71C(): pass

    label('loc_71C')

    Return()

# id: 0x0002 offset: 0x71D
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_732',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_732(): pass

    label('loc_732')

    Return()

# id: 0x0003 offset: 0x733
@scena.Code('func_03_733')
def func_03_733():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_756',
    )

    OP_8D(0x00FE, -30720, 37410, -25780, 40750, 1500)

    Jump('func_03_733')

    def _loc_756(): pass

    label('loc_756')

    Return()

# id: 0x0004 offset: 0x757
@scena.Code('func_04_757')
def func_04_757():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_764',
    )

    Jump('loc_91F')

    def _loc_764(): pass

    label('loc_764')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_7C2',
    )

    ChrTalk(
        0x00FE,
        (
            '回到王都以后\n',
            '又要开始忙碌的日子了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在那之前泡泡温泉，\n',
            '积蓄一些精力吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_91F')

    def _loc_7C2(): pass

    label('loc_7C2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_839',
    )

    ChrTalk(
        0x00FE,
        (
            '听客房的服务生说，\n',
            '蔡斯好像出事了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '连这种偏僻地方\n',
            '都已经听到了传闻，\n',
            '那边肯定是发生大乱子了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_91F')

    def _loc_839(): pass

    label('loc_839')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_88F',
    )

    ChrTalk(
        0x00FE,
        (
            '好好泡一下温泉，\n',
            '缓解旅途的劳累……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了接下来的采购\n',
            '养足精神吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_91F')

    def _loc_88F(): pass

    label('loc_88F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_899',
    )

    Jump('loc_91F')

    def _loc_899(): pass

    label('loc_899')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_904',
    )

    ChrTalk(
        0x00FE,
        (
            '呵呵，\n',
            '看到那些可爱的餐具，\n',
            '想也没想就买下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那家特产店里\n',
            '好像还可以淘到很多宝贝呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_91F')

    def _loc_904(): pass

    label('loc_904')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Return,
        ),
        'loc_90E',
    )

    Jump('loc_91F')

    def _loc_90E(): pass

    label('loc_90E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_918',
    )

    Jump('loc_91F')

    def _loc_918(): pass

    label('loc_918')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_91F',
    )

    def _loc_91F(): pass

    label('loc_91F')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x923
@scena.Code('func_05_923')
def func_05_923():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_930',
    )

    Jump('loc_B66')

    def _loc_930(): pass

    label('loc_930')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_99B',
    )

    ChrTalk(
        0x00FE,
        (
            '和妻子商量过了，\n',
            '最近就在这里\n',
            '好好放松一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在女王的诞辰庆典开始之前\n',
            '回王都就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B66')

    def _loc_99B(): pass

    label('loc_99B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_9A5',
    )

    Jump('loc_B66')

    def _loc_9A5(): pass

    label('loc_9A5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_A1A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_9D5',
    )

    ChrTalk(
        0x00FE,
        (
            '那么～\n',
            '这就去泡个晨澡吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A17')

    def _loc_9D5(): pass

    label('loc_9D5')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '你们要离开这里了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们暂时还会\n',
            '在这里休息一阵子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A17(): pass

    label('loc_A17')

    Jump('loc_B66')

    def _loc_A1A(): pass

    label('loc_A1A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_A24',
    )

    Jump('loc_B66')

    def _loc_A24(): pass

    label('loc_A24')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_B4B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_AAF',
    )

    ChrTalk(
        0x00FE,
        (
            '就在我没注意的一瞬间，\n',
            '妻子已经去特产店买了好多东西了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然买东西没什么不好，\n',
            '不过还是希望她想好了之后再去买。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B48')

    def _loc_AAF(): pass

    label('loc_AAF')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))
    OP_62(0x0012, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '就在我没注意的一瞬间，\n',
            '妻子已经去特产店买了好多东西了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然买东西没什么不好，\n',
            '不过还是希望她想好了之后再去买。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B48(): pass

    label('loc_B48')

    Jump('loc_B66')

    def _loc_B4B(): pass

    label('loc_B4B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Return,
        ),
        'loc_B55',
    )

    Jump('loc_B66')

    def _loc_B55(): pass

    label('loc_B55')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_B5F',
    )

    Jump('loc_B66')

    def _loc_B5F(): pass

    label('loc_B5F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_B66',
    )

    def _loc_B66(): pass

    label('loc_B66')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0xB6A
@scena.Code('func_06_B6A')
def func_06_B6A():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_C81',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_BF2',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀～\n',
            '好不容易闲下来啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，\n',
            '就趁现在赶快准备一下\n',
            '待会儿的饭菜吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天突然\n',
            '一下子来了很多客人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C7E')

    def _loc_BF2(): pass

    label('loc_BF2')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '哎呀～\n',
            '好不容易闲下来啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，\n',
            '为什么客人们\n',
            '都在同一天来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果每个人能把\n',
            '来的时间错开的话，\n',
            '就能更舒服地享受温泉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C7E(): pass

    label('loc_C7E')

    Jump('loc_106D')

    def _loc_C81(): pass

    label('loc_C81')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_CE4',
    )

    ChrTalk(
        0x00FE,
        (
            '怎么样，调查进展如何了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里和平常一样还是很忙啊。\n',
            '因为老是只有我一个人干活。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_106D')

    def _loc_CE4(): pass

    label('loc_CE4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_D6D',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，\n',
            '难道你们今天是来调查案件的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里也已经传来消息了。\n',
            '中央工房的东西被盗走了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '当游击士\n',
            '实在是很辛苦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_106D')

    def _loc_D6D(): pass

    label('loc_D6D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_DAA',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，要走了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以后有空的话\n',
            '要再来玩啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_106D')

    def _loc_DAA(): pass

    label('loc_DAA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_E7D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_E25',
    )

    ChrTalk(
        0x00FE,
        (
            '东方的料理\n',
            '不仅味道可口，\n',
            '而且对健康很有好处。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然做起来\n',
            '要花不少时间和精力，\n',
            '不过却相当值得。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E7A')

    def _loc_E25(): pass

    label('loc_E25')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '啊，要去泡澡了吗？\n',
            '慢慢享受吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我就趁这段时间给你们\n',
            '做好吃的东方料理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E7A(): pass

    label('loc_E7A')

    Jump('loc_106D')

    def _loc_E7D(): pass

    label('loc_E7D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_F23',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，\n',
            '刚才麻烦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听到客人平安无事，\n',
            '我也就放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，\n',
            '这下可以开始安心地准备晚饭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为来了不少新客人，\n',
            '我这边也变得更忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_106D')

    def _loc_F23(): pass

    label('loc_F23')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Return,
        ),
        'loc_F80',
    )

    ChrTalk(
        0x00FE,
        (
            '没想到竟然\n',
            '会有游击士在这里。\n',
            '这下就放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，\n',
            '这件事就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_106D')

    def _loc_F80(): pass

    label('loc_F80')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_F8A',
    )

    Jump('loc_106D')

    def _loc_F8A(): pass

    label('loc_F8A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_106D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1004',
    )

    ChrTalk(
        0x00FE,
        (
            '偶尔放松一下，\n',
            '给自己放个假虽然很好……\n',
            '但是时间久了就会消磨干劲了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '人啊，\n',
            '真是容易懒散下来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_106D')

    def _loc_1004(): pass

    label('loc_1004')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '啊～今天很闲啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '偶尔放松一下，\n',
            '给自己放个假虽然很好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是时间久了\n',
            '就会消磨干劲了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_106D(): pass

    label('loc_106D')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x1071
@scena.Code('func_07_1071')
def func_07_1071():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_107E',
    )

    Jump('loc_1328')

    def _loc_107E(): pass

    label('loc_107E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_1125',
    )

    ChrTalk(
        0x00FE,
        (
            '我觉得只有充分休息\n',
            '才能让身心都恢复活力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '总觉得有一种\n',
            '会钓到大型猎物的预感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好，最好抓紧时间。\n',
            '趁这种感觉还没消失，\n',
            '快赶到下一个钓场！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1328')

    def _loc_1125(): pass

    label('loc_1125')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_117D',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才听到了小道消息，\n',
            '说是蔡斯出事了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '最近的骚动真让人不安啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1328')

    def _loc_117D(): pass

    label('loc_117D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_1187',
    )

    Jump('loc_1328')

    def _loc_1187(): pass

    label('loc_1187')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_1202',
    )

    ChrTalk(
        0x00FE,
        (
            '嘿，\n',
            '你们也要在这里住宿吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，\n',
            '一定要泡露天温泉哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要体验过一次，\n',
            '你们就会迷上这个温泉的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1328')

    def _loc_1202(): pass

    label('loc_1202')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_120C',
    )

    Jump('loc_1328')

    def _loc_120C(): pass

    label('loc_120C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1321',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_12AE',
    )

    ChrTalk(
        0x00FE,
        (
            '就算不泡澡，\n',
            '也还有很多乐趣哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个『红叶亭』的\n',
            '正宗东方料理味道相当不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，这里确实是个天堂。\n',
            '我现在就开始期待晚餐了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_131E')

    def _loc_12AE(): pass

    label('loc_12AE')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '抽取温泉水的水泵\n',
            '好像有一点故障。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '算啦，\n',
            '这个温泉胜地已经有年头了。\n',
            '发生这种事情也没什么好奇怪的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_131E(): pass

    label('loc_131E')

    Jump('loc_1328')

    def _loc_1321(): pass

    label('loc_1321')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_1328',
    )

    def _loc_1328(): pass

    label('loc_1328')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x132C
@scena.Code('func_08_132C')
def func_08_132C():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x1333
@scena.Code('func_09_1333')
def func_09_1333():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x133A
@scena.Code('func_0A_133A')
def func_0A_133A():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_1347',
    )

    Jump('loc_1692')

    def _loc_1347(): pass

    label('loc_1347')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_142A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_13BB',
    )

    ChrTalk(
        0x00FE,
        (
            '不管怎么说，\n',
            '快点抓住那些\n',
            '袭击中央工房的犯人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '绝对不能让那种\n',
            '无法无天的家伙逍遥法外。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1427')

    def _loc_13BB(): pass

    label('loc_13BB')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '啊，是你们。\n',
            '还是这么忙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我从艾德那里听说了，\n',
            '你们是游击士对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请加油。\n',
            '我支持你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1427(): pass

    label('loc_1427')

    Jump('loc_1692')

    def _loc_142A(): pass

    label('loc_142A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_1434',
    )

    Jump('loc_1692')

    def _loc_1434(): pass

    label('loc_1434')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_143E',
    )

    Jump('loc_1692')

    def _loc_143E(): pass

    label('loc_143E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_1448',
    )

    Jump('loc_1692')

    def _loc_1448(): pass

    label('loc_1448')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_154E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 5, 0x525)),
            Expr.Return,
        ),
        'loc_1496',
    )

    ChrTalk(
        0x00FE,
        (
            '您好，欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '『柚子之间』\n',
            '是这里隔壁的房间哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_154B')

    def _loc_1496(): pass

    label('loc_1496')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_14FA',
    )

    ChrTalk(
        0x00FE,
        (
            '那么，趁现在还早，\n',
            '赶快收拾一下床铺吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '马上就是晚饭时间了，\n',
            '客人们都该回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_154B')

    def _loc_14FA(): pass

    label('loc_14FA')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '哎呀，太好了。\n',
            '有人来修理水泵了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们总是受到\n',
            '中央工房的照顾啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_154B(): pass

    label('loc_154B')

    Jump('loc_1692')

    def _loc_154E(): pass

    label('loc_154E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_168B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_15F1',
    )

    ChrTalk(
        0x00FE,
        (
            '唉，\n',
            '今天真难办啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为，\n',
            '温泉的水泵出了点故障。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不早点修理好的话\n',
            '会让客人们失望的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '客人们都是为了温泉\n',
            '才来这里的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1688')

    def _loc_15F1(): pass

    label('loc_15F1')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '欢迎。\n',
            '这里是温泉旅馆『红叶亭』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个旅馆的客房\n',
            '都有各自的名字哦。\n',
            '这里叫做『柚子之间』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '比起『２０１室』这类的名字\n',
            '更加有情调吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1688(): pass

    label('loc_1688')

    Jump('loc_1692')

    def _loc_168B(): pass

    label('loc_168B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_1692',
    )

    def _loc_1692(): pass

    label('loc_1692')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x1696
@scena.Code('func_0B_1696')
def func_0B_1696():
    Call(0, 0x000C)

    Return()

# id: 0x000C offset: 0x169B
@scena.Code('func_0C_169B')
def func_0C_169B():
    TalkBegin(0x000E)
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
            TXT(0x01, '买东西\n'),
            TXT(0x02, '欢迎品尝「诱惑山菜火锅」700米拉\n'),
            TXT(0x03, '离开\n'),
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
        'loc_1719',
    )

    OP_0D()
    OP_A9(0x46)
    OP_56(0x00)
    TalkEnd(0x000E)

    Return()

    def _loc_1719(): pass

    label('loc_1719')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_181B',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x12),
            (Expr.PushLong, 0x2BC),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_17E6',
    )

    SubMira(700)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    PlaySE(11, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x0),
            '尝了尝',
            (TxtCtl.SetColor, 0x2),
            '诱惑山菜火锅',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrStatus(0x0000, 0xFD, 700)
    SetChrStatus(0x0001, 0xFD, 700)
    SetChrStatus(0x0002, 0xFD, 700)
    SetChrStatus(0x0003, 0xFD, 700)
    SetChrStatus(0x0004, 0xFD, 700)
    SetChrStatus(0x0005, 0xFD, 700)
    SetChrStatus(0x0006, 0xFD, 700)
    SetChrStatus(0x0007, 0xFD, 700)

    If(
        (
            (Expr.Eval, "OP_40(0x020D)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_17D8',
    )

    If(
        (
            (Expr.Eval, "OP_AC(0x0004)"),
            Expr.Return,
        ),
        'loc_17AE',
    )

    Jump('loc_17D8')

    def _loc_17AE(): pass

    label('loc_17AE')

    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x0),
            '学会了',
            (TxtCtl.SetColor, 0x2),
            '诱惑山菜火锅',
            (TxtCtl.SetColor, 0x0),
            '的做法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17D8(): pass

    label('loc_17D8')

    OP_56(0x00)
    FadeIn(1000, 0)

    Jump('loc_180C')

    def _loc_17E6(): pass

    label('loc_17E6')

    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '没有足够的米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeIn(300, 0)
    def _loc_180C(): pass

    label('loc_180C')

    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x000E)

    Return()

    def _loc_181B(): pass

    label('loc_181B')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_182C',
    )

    TalkEnd(0x000E)

    Return()

    def _loc_182C(): pass

    label('loc_182C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_18FF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_188F',
    )

    ChrTalk(
        0x000E,
        (
            '只有这种时候\n',
            '才适合做扫除啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '一会儿旅馆又会挤满\n',
            '来这里泡温泉的客人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18FC')

    def _loc_188F(): pass

    label('loc_188F')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x000E,
        (
            '啊，欢迎光临。\n',
            '这里是『红叶亭』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '因为大家都去王都参加诞辰庆典了，\n',
            '所以能有客人来我们非常欢迎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18FC(): pass

    label('loc_18FC')

    Jump('loc_1B5F')

    def _loc_18FF(): pass

    label('loc_18FF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_1909',
    )

    Jump('loc_1B5F')

    def _loc_1909(): pass

    label('loc_1909')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_1994',
    )

    ChrTalk(
        0x000E,
        (
            '今天不管和谁说话，\n',
            '都是在谈论蔡斯的事件啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '难得来到这个温泉胜地，\n',
            '却只顾着谈论这么阴暗的话题……\n',
            '真是感到有些失落啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B5F')

    def _loc_1994(): pass

    label('loc_1994')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_19DF',
    )

    ChrTalk(
        0x000E,
        (
            '啊，已经要回去了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '下次来的时候，\n',
            '要慢慢好好享受哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B5F')

    def _loc_19DF(): pass

    label('loc_19DF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_1A32',
    )

    ChrTalk(
        0x000E,
        (
            '泡完澡出来享用东方料理，\n',
            '会更有一番风味呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '痛痛快快地出汗吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B5F')

    def _loc_1A32(): pass

    label('loc_1A32')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 4, 0x524)),
            Expr.Return,
        ),
        'loc_1A81',
    )

    ChrTalk(
        0x000E,
        (
            '差不多该去\n',
            '帮忙准备晚饭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '我们这里的东方料理是正宗的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B5F')

    def _loc_1A81(): pass

    label('loc_1A81')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_1AFC',
    )

    ChrTalk(
        0x000E,
        (
            '这次来修理水泵的\n',
            '好像是提妲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '明明年纪还很小，\n',
            '却这么了不起……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '再看我自己，\n',
            '连换个灯泡都不会呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B5F')

    def _loc_1AFC(): pass

    label('loc_1AFC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Return,
        ),
        'loc_1B06',
    )

    Jump('loc_1B5F')

    def _loc_1B06(): pass

    label('loc_1B06')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_1B10',
    )

    Jump('loc_1B5F')

    def _loc_1B10(): pass

    label('loc_1B10')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_1B5F',
    )

    ChrTalk(
        0x000E,
        (
            '啊，欢迎光临。\n',
            '这里是『红叶亭』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '请好好享受\n',
            '我们的东方料理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B5F(): pass

    label('loc_1B5F')

    TalkEnd(0x000E)

    Return()

# id: 0x000D offset: 0x1B63
@scena.Code('func_0D_1B63')
def func_0D_1B63():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#0080080670V#073F这里的东方料理挺正宗的。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080080671V#070F不过难得有机会来这里，\n',
            '还是想尝尝真正的利贝尔料理啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x1BDA
@scena.Code('func_0E_1BDA')
def func_0E_1BDA():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x1BE1
@scena.Code('func_0F_1BE1')
def func_0F_1BE1():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x1BE8
@scena.Code('func_10_1BE8')
def func_10_1BE8():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0x1BEF
@scena.Code('func_11_1BEF')
def func_11_1BEF():
    Call(0, 0x0012)

    Return()

# id: 0x0012 offset: 0x1BF4
@scena.Code('func_12_1BF4')
def func_12_1BF4():
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
        'loc_1C50',
    )

    OP_0D()
    OP_A9(0x45)
    OP_56(0x00)
    TalkEnd(0x0008)

    Return()

    def _loc_1C50(): pass

    label('loc_1C50')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1C61',
    )

    TalkEnd(0x0008)

    Return()

    def _loc_1C61(): pass

    label('loc_1C61')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 4, 0x524)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 5, 0x525)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_22B6',
    )

    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x00A4, 5, 0x525))
    OP_28(0x0040, 0x01, 0x0800)
    OP_28(0x0040, 0x04, 0x10)
    Fade(1000)
    SetChrDirection(0x0008, 180, 0)
    SetChrPos(0x0101, 1810, 250, 3490, 45)
    SetChrPos(0x0102, 2500, 250, 2380, 0)
    SetChrPos(0x0107, 3160, 250, 3550, 0)
    CameraMove(2080, 250, 5120, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0570080243V#680F提妲，谢谢你啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080244V多亏你的帮忙，\n',
            '水泵已经修好了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080245V#067F嘿嘿……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080246V经常受到婆婆您的照顾，\n',
            '这点小事也是我应该做的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570080247V#681F呵呵，这孩子不仅能干，\n',
            '而且小嘴还是那么的甜。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080248V#680F对了，还有这边两位。\n',
            '刚才也真是辛苦你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080249V那客人应该是你们的熟人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080250V#506F#1P啊哈哈，算是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 1700, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    SetChrDirection(0x0107, 270, 400)

    ChrTalk(
        0x0107,
        (
            '#0070080251V#064F发生了什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080252V#010F也没什么。\n',
            '算是做了点游击士的份内工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570080253V#681F总之，\n',
            '你们真是帮了大忙啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080254V为了聊表我的谢意，\n',
            '今天就在这里休息一晚吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080255V#004F#1P哎，可以吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0107, 0, 400)

    ChrTalk(
        0x0107,
        (
            '#0070080256V#065F那、那个，婆婆。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080257V我们没和爷爷说\n',
            '今天要住在这里的呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570080258V#680F啊，不用担心了。\n',
            '刚才拉赛尔已经和我联络过了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080259V他说『这里的工作明天才能完成，\n',
            '让他们今天就住在你那里吧』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080260V#064F爷爷这样说吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080261V#006F#1P嘿嘿～\n',
            '博士还真机灵嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080262V#019F既然如此，\n',
            '那就恭敬不如从命了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570080263V#680F嗯，不要客气啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080264V二楼的『柚子之间』是给你们准备的，\n',
            '去把行李放下吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080265V离晚饭还有段时间，\n',
            '你们先去泡泡温泉好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080266V#505F#1P饭前洗澡？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080267V唔……\n',
            '一般不都是睡觉前才洗的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570080268V#681F哎呀～你在说啥呀。\n',
            '难得来这一趟，当然要泡温泉才行啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080269V从早到晚，\n',
            '啥时候泡都是正常的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0107, 270, 400)

    ChrTalk(
        0x0107,
        (
            '#0070080270V#061F呵呵～～\n',
            '就算一天泡三次也是常有的事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080271V#008F#1P是、是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080272V嗯～虽然我很喜欢洗澡，\n',
            '但一天泡那么多次一定会晕……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080273V#010F哈哈，泡温泉之前，\n',
            '我们先把行李放到房间里吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Jump('loc_2CD6')

    def _loc_22B6(): pass

    label('loc_22B6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_2597',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_231E',
    )

    ChrTalk(
        0x0008,
        (
            '#0570100345V#680F有空的话\n',
            '你们可以随时来这里住。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570100346V那么，\n',
            '去王都的路上要小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2594')

    def _loc_231E(): pass

    label('loc_231E')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '#0570100332V#683F啊，是你们……\n',
            '犯人的调查已经告一段落了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570100333V#680F工作完成之后，\n',
            '就来好好歇歇吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570100334V上次多亏你们，客人们也十分满意。\n',
            '我可以把整个露天温泉包给你们哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100335V#506F嗯～\n',
            '我们也想这样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100336V不过，\n',
            '现在必须得去王都一趟呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100337V#010F非常抱歉，\n',
            '之前真是承蒙照顾了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570100338V#681F哪里，别这么客气嘛。\n',
            '就算是修理水泵的谢礼吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570100339V#680F提妲还是老样子，\n',
            '又在帮拉赛尔干活吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570100340V这样太勉强那个孩子了，\n',
            '你们俩要帮我\n',
            '和拉赛尔说说才行哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100341V#003F啊…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100342V#501F……嗯！\n',
            '我知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100343V#010F我们会转达的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570100344V#680F那么，\n',
            '去王都的路上要小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2594(): pass

    label('loc_2594')

    Jump('loc_2CD6')

    def _loc_2597(): pass

    label('loc_2597')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_2626',
    )

    ChrTalk(
        0x0008,
        (
            '#0570080306V#680F啊，是你们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080307V总是为了追捕犯人\n',
            '而东奔西走忙个不停啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080308V虽然很遗憾……\n',
            '不过在这一带\n',
            '没有听说什么线索。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2CD6')

    def _loc_2626(): pass

    label('loc_2626')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_275D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_26B3',
    )

    ChrTalk(
        0x0008,
        (
            '#0570080304V#680F听说中央工房发生了强盗事件，\n',
            '真是有点担心啊。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080305V不过看你们的样子好像没什么问题。\n',
            '呼，终于放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_275A')

    def _loc_26B3(): pass

    label('loc_26B3')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '#0570080301V#682F啊啊，是你们。\n',
            '不过应该没事吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080302V听说中央工房发生了强盗事件，\n',
            '真是有点担心啊。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080303V不过看你们的样子好像没什么问题。\n',
            '呼，终于放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_275A(): pass

    label('loc_275A')

    Jump('loc_2CD6')

    def _loc_275D(): pass

    label('loc_275D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_27AD',
    )

    ChrTalk(
        0x0008,
        (
            '#0570080299V#680F啊，怎么了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080300V是不是又想去\n',
            '露天温泉泡澡呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2CD6')

    def _loc_27AD(): pass

    label('loc_27AD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_282C',
    )

    ChrTalk(
        0x0008,
        (
            '#0570080309V#680F温泉和这里是分开的，\n',
            '从食堂里面的通道过去吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080310V请在我们引以为豪的露天温泉里\n',
            '慢慢享受一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2CD6')

    def _loc_282C(): pass

    label('loc_282C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_2B5A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 4, 0x524)),
            Expr.Return,
        ),
        'loc_28AB',
    )

    ChrTalk(
        0x0008,
        (
            '#0570080297V#680F你们的房间 \n',
            '是二楼的『柚子之间』哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080298V先把行李放好，\n',
            '然后可以一直在温泉里泡到吃晚饭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B57')

    def _loc_28AB(): pass

    label('loc_28AB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B1, 5, 0x58D)),
            Expr.Return,
        ),
        'loc_291C',
    )

    ChrTalk(
        0x0008,
        (
            '#0570080295V#680F那孩子和拉赛尔一样，\n',
            '一摸到机械就停不下手。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080296V麻烦你们去水泵小屋看看情况吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B57')

    def _loc_291C(): pass

    label('loc_291C')

    SetScenaFlags(ScenaFlag(0x00B1, 5, 0x58D))

    ChrTalk(
        0x0008,
        (
            '#0570080281V#680F哎呀，\n',
            '真是辛苦你们了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080282V那个客人是你们的熟人吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080283V#506F啊哈哈，算是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080284V#010F看来水泵的修理也顺利地完成了呢。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080285V外面的水井也开始有热水涌出来了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570080286V#680F啊，是吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080287V但是提妲还在小屋那里没回来呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080288V#000F啊，\n',
            '刚才应该先去小屋看看情况呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080289V#010F是啊，我们现在去看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570080290V#680F那就拜托你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080291V那孩子和拉赛尔一样，\n',
            '一摸到机械就停不下手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080292V#506F哈哈，没错呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080293V#010F那我们走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570080294V#680F麻烦你们了，\n',
            '又让你们跑一趟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B57(): pass

    label('loc_2B57')

    Jump('loc_2CD6')

    def _loc_2B5A(): pass

    label('loc_2B5A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Return,
        ),
        'loc_2BD6',
    )

    ChrTalk(
        0x0008,
        (
            '#0570080279V#680F不好意思，\n',
            '又给你们添麻烦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080280V无论如何请帮忙\n',
            '到平原道找到那个客人，\n',
            '并把她平安地带回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2CD6')

    def _loc_2BD6(): pass

    label('loc_2BD6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_2C60',
    )

    ChrTalk(
        0x0008,
        (
            '#0570080276V#680F怎么，\n',
            '忘了水泵小屋在哪里了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080277V走到村子的广场那里，\n',
            '从北面的斜坡上去就到了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080278V那就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2CD6')

    def _loc_2C60(): pass

    label('loc_2C60')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_2CD6',
    )

    ChrTalk(
        0x0008,
        (
            '#0570080274V#680F嘿～欢迎。\n',
            '本旅馆有我们引以为豪的天然温泉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080275V其中东方风格的露天澡堂\n',
            '特别受客人们欢迎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2CD6(): pass

    label('loc_2CD6')

    TalkEnd(0x0008)

    Return()

# id: 0x0013 offset: 0x2CDA
@scena.Code('func_13_2CDA')
def func_13_2CDA():
    EventBegin(0x00)
    ClearMapFlags(0x00000001)
    CameraMove(560, 250, 2580, 0)
    SetChrPos(0x0101, 490, 0, -1490, 0)
    SetChrPos(0x0102, 2040, 0, -1370, 0)
    SetChrPos(0x0107, 1200, 0, -430, 0)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0107,
        (
            '#0070080015V#061F您好，毛婆婆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4A(0x0008, 255)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0570080016V#681F哎呀，提妲，\n',
            '你总算来了呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2DA2')
    def lambda_2DA2():
        CameraMove(2050, 250, 4540, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2DA2)

    @scena.Lambda('lambda_2DBA')
    def lambda_2DBA():
        ChrWalkTo(0x00FE, 2680, 250, 3530, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_2DBA)

    Sleep(500)

    @scena.Lambda('lambda_2DDA')
    def lambda_2DDA():
        ChrWalkTo(0x00FE, 3570, 250, 2650, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2DDA)

    Sleep(300)

    @scena.Lambda('lambda_2DFA')
    def lambda_2DFA():
        ChrWalkTo(0x00FE, 2250, 250, 2520, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2DFA)

    WaitForThreadExit(0x0101, 0x0001)
    ChrTurnDirection(0x0101, 0x0008, 0)

    ChrTalk(
        0x0008,
        (
            '#0570080017V#680F就在刚刚，\n',
            '工房长和我联络过了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080018V说拉赛尔那家伙\n',
            '让你一个人来帮忙修理，\n',
            '自己却在搞啥乱七八糟的研究是吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080019V#065F不、不是那样呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080020V其实其实，\n',
            '爷爷他本来是打算亲自来的。\n',
            '是我硬求他让我来的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570080021V#680F哎呀～提妲可真是个\n',
            '又温柔又体贴的好孩子呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080022V不过嘛，\n',
            '太娇纵那老头子可不行哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080023V从以前开始就只知道研究啊研究，\n',
            '就这样放任不管的话，\n',
            '真不知会沉沦到啥地步呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080024V#067F啊、啊哈哈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080025V#506F（好健朗的婆婆啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080026V#010F（好像和博士很熟呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570080027V#683F啊，你们两位是……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080028V#560F啊，婆婆，\n',
            '我来介绍一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080029V这两位是艾丝蒂尔姐姐和约修亚哥哥。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080030V他们是游击士协会的游击士，\n',
            '这次是特地护送我来这里的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080031V#006F婆婆，您好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080032V#010F请多多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570080033V#681F哦，是这样啊。\n',
            '真是麻烦你们两位了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080034V#680F我是这个『红叶亭』的老板娘，\n',
            '你们叫我毛婆婆就行了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080035V拉赛尔和我是儿时玩伴，\n',
            '所以这孩子呀，就像我的亲孙女一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080036V#501F哎～是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080037V#067F嘿嘿……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080038V#064F对了，婆婆。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080039V那个导力泵\n',
            '真的是坏了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570080040V#682F啊啊，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080041V已经是４０年前的机械了，\n',
            '差不多快寿终正寝了吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080042V唉，虽说迟早要换新泵，\n',
            '眼下还是应急修理一下吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080043V提妲，没问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080044V#061F嗯，交给我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570080045V#680F好，那就把这个拿去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '借来了',
            (TxtCtl.SetColor, 0x2),
            '水泵小屋的钥匙',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    AddItem(0x0369, 1)

    ChrTalk(
        0x0008,
        (
            '#0570080046V#680F水泵小屋就在村里的广场北边，\n',
            '向北登上高台就是了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080047V那么就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0040, 0x01, 0x0004)
    OP_4B(0x0008, 255)
    EventEnd(0x00)

    Return()

# id: 0x0014 offset: 0x3401
@scena.Code('func_14_3401')
def func_14_3401():
    EventBegin(0x00)
    CameraMove(560, 250, 2580, 0)
    SetChrFlags(0x0009, 0x0080)
    SetChrPos(0x0101, 490, 0, -1490, 0)
    SetChrPos(0x0102, 2040, 0, -1370, 0)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_344A')
    def lambda_344A():
        CameraMove(1770, 250, 5380, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_344A)

    @scena.Lambda('lambda_3462')
    def lambda_3462():
        ChrWalkTo(0x00FE, 2350, 250, 3490, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3462)

    @scena.Lambda('lambda_347D')
    def lambda_347D():
        ChrWalkTo(0x00FE, 3640, 250, 3460, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_347D)

    OP_0D()
    OP_4A(0x0008, 255)
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    WaitForThreadExit(0x0101, 0x0001)
    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0008,
        (
            '#0570080079V#683F#2P哎呀，是你们啊。\n',
            '提妲她搞得怎么样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080080V#000F嗯，已经开始修理了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080081V既然我们帮不上什么忙，\n',
            '站在她旁边又反而会妨碍她工作，\n',
            '所以还是先在这里等等她吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570080082V#681F#2P啊哈哈，\n',
            '真是明智的选择。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080083V那孩子在某些方面，\n',
            '可是比拉赛尔更有天分呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080084V#501F天分……\n',
            '这么说来也的确是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080085V#010F年纪那么小\n',
            '就能在中央工房帮忙工作，\n',
            '在普通人看来已经是很不简单了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570080086V#680F#2P而且人又细心、又坚强，\n',
            '无论什么时候都面带开朗的笑容。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080087V虽说一开始摆弄机器\n',
            '就会马上迷了进去……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080088V总之，就是个非常好的孩子啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080089V#682F……不过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080090V…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080091V#004F怎么啦，婆婆？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570080092V#680F#2P不……没啥。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x0009, 970, 0, -2050, 0)
    OP_4A(0x0009, 255)

    ChrTalk(
        0x0009,
        (
            '#1990080093V#2P喂～毛婆婆！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0102, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    @scena.Lambda('lambda_37DC')
    def lambda_37DC():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_37DC)

    @scena.Lambda('lambda_37EA')
    def lambda_37EA():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_37EA)

    @scena.Lambda('lambda_37F8')
    def lambda_37F8():
        CameraMove(1070, 250, 4930, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_37F8)

    @scena.Lambda('lambda_3810')
    def lambda_3810():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_3810')

    DispatchAsync2(0x0101, 0x0001, lambda_3810)

    @scena.Lambda('lambda_3821')
    def lambda_3821():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_3821')

    DispatchAsync2(0x0102, 0x0001, lambda_3821)

    @scena.Lambda('lambda_3832')
    def lambda_3832():
        ChrWalkTo(0x00FE, 3330, 250, 2590, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3832)

    ClearChrFlags(0x0009, 0x0080)
    ChrSetRGBAMask(0x0009, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_385D')
    def lambda_385D():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_385D)

    ChrWalkTo(0x0009, 1990, 250, 3520, 3000, 0x00)
    ChrTurnDirection(0x0009, 0x0008, 400)

    ChrTalk(
        0x0008,
        (
            '#0570080094V#683F#2P艾德，你回来了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080095V那么着急的样子，\n',
            '发生啥事了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1990080096V#1P哎呀，那个……\n',
            '有件事我想打听一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1990080097V#1P那个从王都来的小姐\n',
            '回来了没有？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570080098V#680F#2P从王都来的……\n',
            '啊啊，你是说昨天来的那个客人吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080099V她说要去散步，\n',
            '到现在还没有回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1990080100V#1P果然是这样吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1990080101V#1P嗯……这下糟了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570080102V#683F#2P怎么了？\n',
            '她不在村子里吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1990080103V#1P不，那个……其实啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1990080104V#1P刚才我在村子的门口\n',
            '看到那个小姐了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1990080105V#1P她好像说为了找景色漂亮的地方，\n',
            '要到平原那里去散步……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570080106V#682F#2P去平原散步？\n',
            '那里有很多魔兽啊，怎么这么乱来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080107V#684F你这个大笨蛋！\n',
            '当时怎么不阻止她呀！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0009,
        (
            '#1990080108V#1P可、可是，我阻止过了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1990080109V#1P该怎么说呢，\n',
            '她是那种我行我素的类型啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1990080110V#1P刚才一点儿也不\n',
            '把我的劝阻当成一回事。\n',
            '所以我才担心，过来问你嘛。',
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
            '#0010080111V#002F那个，打扰一下可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTurnDirection(0x0009, 0x0101, 400)
    SetChrDirection(0x0008, 135, 400)

    ChrTalk(
        0x0009,
        (
            '#1990080112V#1P嗯？什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1990080113V#1P咦，来了新客人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080114V#012F#6P我想请问一下……\n',
            '您是在什么时候见到那位客人的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1990080115V#1P什么时候……\n',
            '我想大概是中午吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1990080116V#1P我正好吃完午饭回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080117V#006F中午……\n',
            '嗯，看来应该能赶得上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080118V#010F#6P我们马上去追吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1990080119V#1P我说……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080120V#006F别看我们这样年轻，\n',
            '其实我们两个都是协会的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080121V#010F#6P我们这就出发，\n',
            '去护送那位去平原的客人回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1990080122V#1P协会……你们是游击士！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1990080123V#1P这下可放心了。\n',
            '那我可就全拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0008, 180, 400)

    ChrTalk(
        0x0008,
        (
            '#0570080124V#684F#2P拜托这句话，你还好意思说吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080125V#682F#2P算了……\n',
            '客人的安全才是最重要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0008, 135, 400)

    ChrTalk(
        0x0008,
        (
            '#0570080126V#682F#2P虽然很不好意思，\n',
            '不过这次就麻烦你们两位了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0101, 0xFF)
    ChrTurnDirection(0x0102, 0x0008, 400)
    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010080127V#006F嗯，包在我们身上！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080128V#010F#6P那我们出发了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0040, 0x01, 0x0020)
    OP_28(0x0040, 0x01, 0x0040)
    ClearMapFlags(0x10000000)
    EventEnd(0x00)
    SetChrDirection(0x0008, 180, 0)
    OP_4B(0x0008, 255)
    OP_4B(0x0009, 255)

    Return()

# id: 0x0015 offset: 0x3FAF
@scena.Code('func_15_3FAF')
def func_15_3FAF():
    EventBegin(0x00)
    ClearMapFlags(0x00000001)
    CameraMove(28000, 0, 40030, 0)
    SetChrPos(0x0101, 33900, 0, 44790, 180)
    SetChrPos(0x0102, 34550, 0, 44500, 180)
    SetChrPos(0x0107, 33460, 0, 45000, 180)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_4009')
    def lambda_4009():
        CameraMove(32210, 0, 43130, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4009)

    ChrWalkTo(0x0101, 33910, 0, 42300, 2000, 0x00)
    SetChrDirection(0x0101, 270, 400)
    Sleep(500)

    SetChrDirection(0x0101, 90, 400)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010080324V#501F哎～这房间真不错啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080325V#010F#2P是啊，感觉的确很好。\n',
            '东方风格的装饰果然别具一格。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080326V#060F因为毛婆婆\n',
            '是东方出身的嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080327V婆婆还小的时候，\n',
            '就和家人一起搬来了利贝尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080328V这个村子里还有不少\n',
            '和婆婆一样东方出身的人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0107, 400)

    ChrTalk(
        0x0101,
        (
            '#0010080329V#006F原来是这样啊，\n',
            '怪不得感觉这里的氛围有点特别。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080330V已经开始期待这里的晚饭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080331V#010F#2P是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080332V不过，难得老板娘推荐，\n',
            '吃饭前还是先去泡泡温泉吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080333V#501F啊，对啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080334V#001F提妲，\n',
            '和我一起去吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080335V#067F嗯，好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080336V#010F#2P放好行李之后，\n',
            '我们就马上去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_429D')
    def lambda_429D():
        ChrWalkTo(0x00FE, 31850, 0, 39950, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_429D)

    Sleep(100)

    @scena.Lambda('lambda_42BD')
    def lambda_42BD():
        ChrWalkTo(0x00FE, 32880, 0, 40620, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_42BD)

    Sleep(300)

    @scena.Lambda('lambda_42DD')
    def lambda_42DD():
        ChrWalkTo(0x00FE, 32880, 0, 40620, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_42DD)

    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(1000)

    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T3223._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0016 offset: 0x430F
@scena.Code('func_16_430F')
def func_16_430F():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '露天澡堂在这边  ≡',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0017 offset: 0x4354
@scena.Code('func_17_4354')
def func_17_4354():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上贴着一张纸条。\n',
            '『熟睡中，请勿打扰。』',
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

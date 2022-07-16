import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3223_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3223   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '朵洛希'),
    TXT(0x02, '毛婆婆'),
    TXT(0x03, '艾德'),
    TXT(0x04, '拜舍尔'),
    TXT(0x05, '林'),
    TXT(0x06, '莉西亚'),
    TXT(0x07, '希利尔'),
    TXT(0x08, '艾缇'),
    TXT(0x09, '拉克'),
    TXT(0x0A, '希玛'),
    TXT(0x0B, '库安'),
    TXT(0x0C, '西加罗'),
    TXT(0x0D, '艾德尔'),
    TXT(0x0E, '艾德'),
    TXT(0x0F, '水果牛奶'),
    TXT(0x10, '水果牛奶'),
    TXT(0x11, '水果牛奶'),
    TXT(0x12, '水果牛奶'),
    TXT(0x13, '水果牛奶'),
    TXT(0x14, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3223.x'
    header.mapIndex       = 1
    header.bgm            = 84
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x2F11
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
        ('ED6_DT07/CH02070._CH', 'ED6_DT07/CH02070P._CP'),
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
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH01270._CH', 'ED6_DT07/CH01270P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
    ]

# id: 0x10002 offset: 0x122
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
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
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            x                   = 2590,
            z                   = 250,
            y                   = 5360,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
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
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
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
            talkScenaIndex      = 0x0007,
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
            talkScenaIndex      = 0x0008,
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
            talkScenaIndex      = 0x0009,
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
            talkScenaIndex      = 0x000A,
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
            talkScenaIndex      = 0x000C,
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
            talkScenaIndex      = 0x000F,
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
            talkScenaIndex      = 0x0010,
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
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
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
            direction           = 0,
            word_0E             = 0,
            dword_10            = 131086,
            chipIndex           = 14,
            npcIndex            = 0x01E6,
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
            dword_10            = 196622,
            chipIndex           = 14,
            npcIndex            = 0x01E6,
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
            dword_10            = 196622,
            chipIndex           = 14,
            npcIndex            = 0x01E6,
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
            dword_10            = 196622,
            chipIndex           = 14,
            npcIndex            = 0x01E6,
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
            dword_10            = 196622,
            chipIndex           = 14,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x382
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x382
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x382
@scena.ActorData('ActorData')
def ActorData():
    return (
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
            talkFunctionIndex   = 0x0015,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x3EE
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_401',
    )

    SetMapFlags(0x10000000)
    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x0013)

    def _loc_401(): pass

    label('loc_401')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_40F',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, 0x0014)

    def _loc_40F(): pass

    label('loc_40F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_445',
    )

    ClearChrFlags(0x0015, 0x0080)
    SetChrPos(0x0015, -30310, -250, 8840, 81)
    ClearChrFlags(0x000F, 0x0080)
    SetChrPos(0x000F, 8490, 0, 340, 102)

    Jump('loc_745')

    def _loc_445(): pass

    label('loc_445')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_4C4',
    )

    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, 14330, 0, 1850, 182)
    ClearChrFlags(0x0015, 0x0080)
    SetChrPos(0x0015, -30310, -250, 8840, 81)
    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x000E, -1040, 0, 40770, 2)
    ClearChrFlags(0x0013, 0x0080)
    SetChrPos(0x0013, -28880, 0, 43500, 9)
    ClearChrFlags(0x0014, 0x0080)
    SetChrPos(0x0014, -28740, 0, 38750, 93)
    CreateThread(0x0014, 0x00, 0x00, 0x0003)

    Jump('loc_745')

    def _loc_4C4(): pass

    label('loc_4C4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_52D',
    )

    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, 14330, 0, 1850, 182)
    ClearChrFlags(0x0015, 0x0080)
    SetChrPos(0x0015, -30310, -250, 8840, 81)
    ClearChrFlags(0x000F, 0x0080)
    SetChrPos(0x000F, 8490, 0, 340, 102)
    ClearChrFlags(0x0014, 0x0080)
    SetChrPos(0x0014, -28740, 0, 38750, 93)
    CreateThread(0x0014, 0x00, 0x00, 0x0003)

    Jump('loc_745')

    def _loc_52D(): pass

    label('loc_52D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_58F',
    )

    ClearChrFlags(0x0015, 0x0080)
    SetChrPos(0x0015, -30310, -250, 8840, 81)
    ClearChrFlags(0x000F, 0x0080)
    SetChrPos(0x000F, 8490, 0, 340, 102)
    ClearChrFlags(0x0013, 0x0080)
    SetChrPos(0x0013, 11260, 0, 10650, 175)
    ClearChrFlags(0x0014, 0x0080)
    SetChrPos(0x0014, 11070, 0, 8460, 358)

    Jump('loc_745')

    def _loc_58F(): pass

    label('loc_58F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_618',
    )

    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, -2470, 0, 39920, 270)
    ClearChrFlags(0x0015, 0x0080)
    SetChrPos(0x0015, -30310, -250, 8840, 81)
    ClearChrFlags(0x000F, 0x0080)
    SetChrPos(0x000F, 8490, 0, 340, 102)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 7, 0x527)),
            Expr.Return,
        ),
        'loc_615',
    )

    ClearChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0008, 0x0004)
    SetChrFlags(0x0008, 0x0010)
    SetChrPos(0x0008, 14070, 0, 2040, 180)
    ClearChrFlags(0x0016, 0x0080)
    SetChrPos(0x0016, 14600, 750, 1030, 0)

    def _loc_615(): pass

    label('loc_615')

    Jump('loc_745')

    def _loc_618(): pass

    label('loc_618')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_690',
    )

    ClearChrFlags(0x0015, 0x0080)
    SetChrPos(0x0015, -30310, -250, 8840, 81)
    ClearChrFlags(0x000F, 0x0080)
    SetChrPos(0x000F, 8490, 0, 340, 102)
    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x000E, -1040, 0, 40770, 2)
    ClearChrFlags(0x0013, 0x0080)
    SetChrPos(0x0013, 11260, 0, 10650, 175)
    ClearChrFlags(0x0014, 0x0080)
    SetChrPos(0x0014, 11070, 0, 8460, 358)

    Jump('loc_745')

    def _loc_690(): pass

    label('loc_690')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Return,
        ),
        'loc_6C6',
    )

    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, 14330, 0, 1850, 182)
    ClearChrFlags(0x0015, 0x0080)
    SetChrPos(0x0015, 970, 0, -2050, 0)

    Jump('loc_745')

    def _loc_6C6(): pass

    label('loc_6C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_6FC',
    )

    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, 14330, 0, 1850, 182)
    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x000E, -2080, 250, 6150, 195)

    Jump('loc_745')

    def _loc_6FC(): pass

    label('loc_6FC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_745',
    )

    ClearChrFlags(0x0015, 0x0080)
    SetChrPos(0x0015, -30310, -250, 8840, 81)
    ClearChrFlags(0x000F, 0x0080)
    SetChrPos(0x000F, 8490, 0, 340, 102)
    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x000E, -2080, 250, 6150, 195)

    def _loc_745(): pass

    label('loc_745')

    Return()

# id: 0x0001 offset: 0x746
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0x747
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_75C',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_75C(): pass

    label('loc_75C')

    Return()

# id: 0x0003 offset: 0x75D
@scena.Code('func_03_75D')
def func_03_75D():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_780',
    )

    OP_8D(0x00FE, -30720, 37410, -25780, 40750, 3000)

    Jump('func_03_75D')

    def _loc_780(): pass

    label('loc_780')

    Return()

# id: 0x0004 offset: 0x781
@scena.Code('func_04_781')
def func_04_781():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_78E',
    )

    Jump('loc_95A')

    def _loc_78E(): pass

    label('loc_78E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_7FD',
    )

    ChrTalk(
        0x00FE,
        (
            '呵呵，最后的目标是\n',
            '趁着女王诞辰庆典\n',
            '在王都做笔大买卖。',
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

    Jump('loc_95A')

    def _loc_7FD(): pass

    label('loc_7FD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_874',
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

    Jump('loc_95A')

    def _loc_874(): pass

    label('loc_874')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_8CA',
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

    Jump('loc_95A')

    def _loc_8CA(): pass

    label('loc_8CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_8D4',
    )

    Jump('loc_95A')

    def _loc_8D4(): pass

    label('loc_8D4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_93F',
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

    Jump('loc_95A')

    def _loc_93F(): pass

    label('loc_93F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Return,
        ),
        'loc_949',
    )

    Jump('loc_95A')

    def _loc_949(): pass

    label('loc_949')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_953',
    )

    Jump('loc_95A')

    def _loc_953(): pass

    label('loc_953')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_95A',
    )

    def _loc_95A(): pass

    label('loc_95A')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x95E
@scena.Code('func_05_95E')
def func_05_95E():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_96B',
    )

    Jump('loc_B5D')

    def _loc_96B(): pass

    label('loc_96B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_9E5',
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
            '然后预计在女王的\n',
            '诞辰庆典开始之前\n',
            '到达最终目的地王都。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B5D')

    def _loc_9E5(): pass

    label('loc_9E5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_9EF',
    )

    Jump('loc_B5D')

    def _loc_9EF(): pass

    label('loc_9EF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_A64',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_A1F',
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

    Jump('loc_A61')

    def _loc_A1F(): pass

    label('loc_A1F')

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

    def _loc_A61(): pass

    label('loc_A61')

    Jump('loc_B5D')

    def _loc_A64(): pass

    label('loc_A64')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_A6E',
    )

    Jump('loc_B5D')

    def _loc_A6E(): pass

    label('loc_A6E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_B42',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_AD3',
    )

    ChrTalk(
        0x00FE,
        (
            '艾德尔那家伙，\n',
            '已经去特产店买了好多东西了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，真是的。\n',
            '真是不能大意啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B3F')

    def _loc_AD3(): pass

    label('loc_AD3')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '就在我没注意的一瞬间，\n',
            '艾德尔那家伙\n',
            '已经去特产店买了好多东西了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，真是的。\n',
            '真是不能大意啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B3F(): pass

    label('loc_B3F')

    Jump('loc_B5D')

    def _loc_B42(): pass

    label('loc_B42')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Return,
        ),
        'loc_B4C',
    )

    Jump('loc_B5D')

    def _loc_B4C(): pass

    label('loc_B4C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_B56',
    )

    Jump('loc_B5D')

    def _loc_B56(): pass

    label('loc_B56')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_B5D',
    )

    def _loc_B5D(): pass

    label('loc_B5D')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0xB61
@scena.Code('func_06_B61')
def func_06_B61():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_C78',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_BE9',
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

    Jump('loc_C75')

    def _loc_BE9(): pass

    label('loc_BE9')

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

    def _loc_C75(): pass

    label('loc_C75')

    Jump('loc_1064')

    def _loc_C78(): pass

    label('loc_C78')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_CDB',
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

    Jump('loc_1064')

    def _loc_CDB(): pass

    label('loc_CDB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_D64',
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

    Jump('loc_1064')

    def _loc_D64(): pass

    label('loc_D64')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_DA1',
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

    Jump('loc_1064')

    def _loc_DA1(): pass

    label('loc_DA1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_E74',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_E1C',
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

    Jump('loc_E71')

    def _loc_E1C(): pass

    label('loc_E1C')

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

    def _loc_E71(): pass

    label('loc_E71')

    Jump('loc_1064')

    def _loc_E74(): pass

    label('loc_E74')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_F1A',
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

    Jump('loc_1064')

    def _loc_F1A(): pass

    label('loc_F1A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Return,
        ),
        'loc_F77',
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

    Jump('loc_1064')

    def _loc_F77(): pass

    label('loc_F77')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_F81',
    )

    Jump('loc_1064')

    def _loc_F81(): pass

    label('loc_F81')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_1064',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_FFB',
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

    Jump('loc_1064')

    def _loc_FFB(): pass

    label('loc_FFB')

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

    def _loc_1064(): pass

    label('loc_1064')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x1068
@scena.Code('func_07_1068')
def func_07_1068():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_1075',
    )

    Jump('loc_132B')

    def _loc_1075(): pass

    label('loc_1075')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_111C',
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

    Jump('loc_132B')

    def _loc_111C(): pass

    label('loc_111C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_1174',
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

    Jump('loc_132B')

    def _loc_1174(): pass

    label('loc_1174')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_117E',
    )

    Jump('loc_132B')

    def _loc_117E(): pass

    label('loc_117E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_1205',
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
            '等露天澡堂能用了，\n',
            '你们就赶快去试试吧。',
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

    Jump('loc_132B')

    def _loc_1205(): pass

    label('loc_1205')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_120F',
    )

    Jump('loc_132B')

    def _loc_120F(): pass

    label('loc_120F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1324',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_12B1',
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

    Jump('loc_1321')

    def _loc_12B1(): pass

    label('loc_12B1')

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

    def _loc_1321(): pass

    label('loc_1321')

    Jump('loc_132B')

    def _loc_1324(): pass

    label('loc_1324')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_132B',
    )

    def _loc_132B(): pass

    label('loc_132B')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x132F
@scena.Code('func_08_132F')
def func_08_132F():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x1336
@scena.Code('func_09_1336')
def func_09_1336():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x133D
@scena.Code('func_0A_133D')
def func_0A_133D():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_134A',
    )

    Jump('loc_1695')

    def _loc_134A(): pass

    label('loc_134A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_142D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_13BE',
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

    Jump('loc_142A')

    def _loc_13BE(): pass

    label('loc_13BE')

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

    def _loc_142A(): pass

    label('loc_142A')

    Jump('loc_1695')

    def _loc_142D(): pass

    label('loc_142D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_1437',
    )

    Jump('loc_1695')

    def _loc_1437(): pass

    label('loc_1437')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_1441',
    )

    Jump('loc_1695')

    def _loc_1441(): pass

    label('loc_1441')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_144B',
    )

    Jump('loc_1695')

    def _loc_144B(): pass

    label('loc_144B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_1551',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 5, 0x525)),
            Expr.Return,
        ),
        'loc_1499',
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

    Jump('loc_154E')

    def _loc_1499(): pass

    label('loc_1499')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_14FD',
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

    Jump('loc_154E')

    def _loc_14FD(): pass

    label('loc_14FD')

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

    def _loc_154E(): pass

    label('loc_154E')

    Jump('loc_1695')

    def _loc_1551(): pass

    label('loc_1551')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_168E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_15F4',
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

    Jump('loc_168B')

    def _loc_15F4(): pass

    label('loc_15F4')

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

    def _loc_168B(): pass

    label('loc_168B')

    Jump('loc_1695')

    def _loc_168E(): pass

    label('loc_168E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_1695',
    )

    def _loc_1695(): pass

    label('loc_1695')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x1699
@scena.Code('func_0B_1699')
def func_0B_1699():
    Call(0, 0x000C)

    Return()

# id: 0x000C offset: 0x169E
@scena.Code('func_0C_169E')
def func_0C_169E():
    TalkBegin(0x000F)
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
        'loc_171C',
    )

    OP_0D()
    OP_A9(0x46)
    OP_56(0x00)
    TalkEnd(0x000F)

    Return()

    def _loc_171C(): pass

    label('loc_171C')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_181E',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x12),
            (Expr.PushLong, 0x2BC),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_17E9',
    )

    SubMira(700)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    PlaySE(11, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x2),
            '诱惑山菜火锅',
            (TxtCtl.SetColor, 0x0),
            '品尝过了。',
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
        'loc_17DB',
    )

    If(
        (
            (Expr.Eval, "OP_AC(0x0004)"),
            Expr.Return,
        ),
        'loc_17B1',
    )

    Jump('loc_17DB')

    def _loc_17B1(): pass

    label('loc_17B1')

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

    def _loc_17DB(): pass

    label('loc_17DB')

    OP_56(0x00)
    FadeIn(1000, 0)

    Jump('loc_180F')

    def _loc_17E9(): pass

    label('loc_17E9')

    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '没有足够的米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeIn(300, 0)
    def _loc_180F(): pass

    label('loc_180F')

    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x000F)

    Return()

    def _loc_181E(): pass

    label('loc_181E')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_182F',
    )

    TalkEnd(0x000F)

    Return()

    def _loc_182F(): pass

    label('loc_182F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_1902',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1892',
    )

    ChrTalk(
        0x000F,
        (
            '只有这种时候\n',
            '才适合做扫除啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '一会儿旅馆又会挤满\n',
            '来这里泡温泉的客人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18FF')

    def _loc_1892(): pass

    label('loc_1892')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x000F,
        (
            '啊，欢迎光临。\n',
            '这里是『红叶亭』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '因为大家都去王都参加诞辰庆典了，\n',
            '所以能有客人来我们非常欢迎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18FF(): pass

    label('loc_18FF')

    Jump('loc_1AF4')

    def _loc_1902(): pass

    label('loc_1902')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_190C',
    )

    Jump('loc_1AF4')

    def _loc_190C(): pass

    label('loc_190C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_1997',
    )

    ChrTalk(
        0x000F,
        (
            '今天不管和谁说话，\n',
            '都是在谈论蔡斯的事件啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '难得来到这个温泉胜地，\n',
            '却只顾着谈论这么阴暗的话题……\n',
            '真是感到有些失落啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AF4')

    def _loc_1997(): pass

    label('loc_1997')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_19F1',
    )

    ChrTalk(
        0x000F,
        (
            '啊，已经要回去了吗？\n',
            '还是那么忙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '下次来的时候，\n',
            '要慢慢好好享受哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AF4')

    def _loc_19F1(): pass

    label('loc_19F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_1A44',
    )

    ChrTalk(
        0x000F,
        (
            '泡完澡出来享用东方料理，\n',
            '会更有一番风味呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '痛痛快快地出汗吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AF4')

    def _loc_1A44(): pass

    label('loc_1A44')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_1A91',
    )

    ChrTalk(
        0x000F,
        (
            '啊～欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '你们的房间在二楼。\n',
            '请从前台旁边的楼梯走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AF4')

    def _loc_1A91(): pass

    label('loc_1A91')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Return,
        ),
        'loc_1A9B',
    )

    Jump('loc_1AF4')

    def _loc_1A9B(): pass

    label('loc_1A9B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_1AA5',
    )

    Jump('loc_1AF4')

    def _loc_1AA5(): pass

    label('loc_1AA5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_1AF4',
    )

    ChrTalk(
        0x000F,
        (
            '啊，欢迎光临。\n',
            '这里是『红叶亭』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '请好好享受\n',
            '我们的东方料理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AF4(): pass

    label('loc_1AF4')

    TalkEnd(0x000F)

    Return()

# id: 0x000D offset: 0x1AF8
@scena.Code('func_0D_1AF8')
def func_0D_1AF8():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#0280080366V#151F泡过温泉之后\n',
            '喝杯水果牛奶真是好舒服啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280080367V泡得暖暖的身体\n',
            '都被这清凉和甘甜给感染了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x1B6A
@scena.Code('func_0E_1B6A')
def func_0E_1B6A():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x1B71
@scena.Code('func_0F_1B71')
def func_0F_1B71():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x1B78
@scena.Code('func_10_1B78')
def func_10_1B78():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0x1B7F
@scena.Code('func_11_1B7F')
def func_11_1B7F():
    Call(0, 0x0012)

    Return()

# id: 0x0012 offset: 0x1B84
@scena.Code('func_12_1B84')
def func_12_1B84():
    TalkBegin(0x0009)
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
        'loc_1BE0',
    )

    OP_0D()
    OP_A9(0x45)
    OP_56(0x00)
    TalkEnd(0x0009)

    Return()

    def _loc_1BE0(): pass

    label('loc_1BE0')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1BF1',
    )

    TalkEnd(0x0009)

    Return()

    def _loc_1BF1(): pass

    label('loc_1BF1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 4, 0x524)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 5, 0x525)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2082',
    )

    ClearMapFlags(0x00000001)
    OP_66(0x0000)
    OP_69(0x0009, 1000)
    SetScenaFlags(ScenaFlag(0x00A4, 5, 0x525))
    OP_28(0x0040, 0x01, 0x0800)
    OP_28(0x0040, 0x04, 0x10)

    ChrTalk(
        0x0009,
        (
            '#0570080243V#680F提妲，谢谢了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080244V泵好像\n',
            '已经修好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F呵呵……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080246V经常受你照顾，\n',
            '这点小事当然的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#680F呵呵，\n',
            '好甜的小嘴呀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '呀，刚才也\n',
            '真是辛苦你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080249V她好像和你们认识呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F呵呵呵～～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070890009V#060F？？？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '什么事呀？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F正好遇上\n',
            '游击士的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#680F你们真是\n',
            '帮了大忙啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080254V作为回礼，\n',
            '你们今天就住在这里休息吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哎，可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F啊，婆婆。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080257V我们没对爷爷说\n',
            '今天要住在这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0570080258V#680F呀，不用担心了，\n',
            '我刚才和拉赛尔连络过了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0571360001V他说『这里的作业明天才能完成，\n',
            '今晚就住在你那里了』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F爷爷吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哎！\n',
            '博士还真机灵呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F还不如说\n',
            '嘴比较甜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0570080263V#680F呀，不要客气呀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080264V二楼的『柚子之间』的房间\n',
            '已经给你们准备好了，把行李放下来吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080265V离晚饭还要点时间，\n',
            '你们先去泡温泉吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F饭前洗澡？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080267V洗澡一般不是\n',
            '在睡觉前的嘛？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#680F在说什么呢，\n',
            '难得的温泉呀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080269V从早到晚，\n',
            '什么时候泡都是很正常的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F呵呵，就算一天\n',
            '泡三次都是常有的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F是这样呀……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080272V嗯，我虽然很喜欢洗澡，\n',
            '但这么沉迷……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F到房间放行李的话\n',
            '还是快去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_69(0x0000, 1000)
    SetMapFlags(0x00000001)
    OP_66(0x0001)

    Jump('loc_2ABB')

    def _loc_2082(): pass

    label('loc_2082')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_230B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_20EE',
    )

    ChrTalk(
        0x0009,
        (
            '#0570100345V#680F有空的话\n',
            '你们可以随时来这里住。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0571360011V那么，到王都的路上\n',
            '你们要小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2308')

    def _loc_20EE(): pass

    label('loc_20EE')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0009,
        (
            '#680F啊，是你们……\n',
            '犯人的调查已经告一段落了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '如果做完的话\n',
            '就好好歇歇吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570100334V因为最近客人很多，\n',
            '露天温泉也都预订满了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯～\n',
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
            '#010F非常抱歉，\n',
            '之前真是承蒙照顾了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0571360012V#680F哪里，别这么客气嘛。\n',
            '就算是修水泵的谢礼吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '提妲还是那样子\n',
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
            '#000F啊…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '……嗯！\n',
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
        0x0009,
        (
            '#0570100344V#680F那么到王都的路上\n',
            '你们要小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2308(): pass

    label('loc_2308')

    Jump('loc_2ABB')

    def _loc_230B(): pass

    label('loc_230B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_23C6',
    )

    ChrTalk(
        0x0009,
        (
            '#0570080306V#680F啊，是你们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0571360004V总是为了追捕犯人\n',
            '而东奔西走忙个不停啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0571360005V唉……今天的晚饭又只有\n',
            '不过在这一带\n',
            '没有听说什么线索。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0571360006V呼～\n',
            '至少能帮上点忙也好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2ABB')

    def _loc_23C6(): pass

    label('loc_23C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_2564',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_24C9',
    )

    ChrTalk(
        0x0009,
        (
            '#0571360007V#680F哦，提妲你怎么了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0571360008V脸色看起来有点不好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070890010V#060F啊，不。\n',
            '没什么事啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070890011V我们有件事\n',
            '只是有些累了而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0571360009V#680F是吗，\n',
            '可不要太过勉强哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0571360010V你跟拉赛尔那家伙\n',
            '实在太像了。\n',
            '可不要学他乱来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2561')

    def _loc_24C9(): pass

    label('loc_24C9')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0009,
        (
            '#680F啊，是你们。\n',
            '不过应该没事吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080302V听说中央工房\n',
            '发生了强盗事件，\n',
            '真是有点担心啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080303V但如果是这样的话就没问题了。\n',
            '呼，终于放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2561(): pass

    label('loc_2561')

    Jump('loc_2ABB')

    def _loc_2564(): pass

    label('loc_2564')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_25B6',
    )

    ChrTalk(
        0x0009,
        (
            '#0571360003V#680F哦，回来的真快啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080300V是不是要去\n',
            '露天温泉泡澡呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2ABB')

    def _loc_25B6(): pass

    label('loc_25B6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_2635',
    )

    ChrTalk(
        0x0009,
        (
            '#0570080309V#680F温泉和这里是分开的，\n',
            '从食堂里面的通道过去吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080310V请在我们引以为荣的露天温泉里\n',
            '慢慢享受一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2ABB')

    def _loc_2635(): pass

    label('loc_2635')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_2941',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 4, 0x524)),
            Expr.Return,
        ),
        'loc_26AC',
    )

    ChrTalk(
        0x0009,
        (
            '#0570080297V#680F你们的房间 \n',
            '是二楼的『柚子房间』哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080298V放好行李之后，\n',
            '在晚饭之前都可以泡温泉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_293E')

    def _loc_26AC(): pass

    label('loc_26AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B1, 5, 0x58D)),
            Expr.Return,
        ),
        'loc_271B',
    )

    ChrTalk(
        0x0009,
        (
            '#0570080295V#680F那孩子和拉赛尔一样，\n',
            '一摸到机械就停不下手。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080296V麻烦你们去\n',
            '水泵小屋看看情况吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_293E')

    def _loc_271B(): pass

    label('loc_271B')

    SetScenaFlags(ScenaFlag(0x00B1, 5, 0x58D))

    ChrTalk(
        0x0009,
        (
            '#0570080281V#680F哎呀，\n',
            '真是辛苦你们了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080282V那个客人\n',
            '是你们的熟人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F呵呵呵～～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080284V#010F看来水泵的修理\n',
            '也顺利地完成了哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080285V外面的水井\n',
            '也开始有热水湧出来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0570080286V#680F啊，是吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080287V但是提妲\n',
            '还在小屋那里没回来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080288V#000F啊，刚才应该先去\n',
            '小屋看看情况呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080289V#010F是啊，走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0570080290V#680F那就拜托你们去看看吧。',
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
            '#000F哈哈，果然呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080293V#010F那我们就去看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0570080294V#680F那就拜托了。\n',
            '再麻烦你们跑一趟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_293E(): pass

    label('loc_293E')

    Jump('loc_2ABB')

    def _loc_2941(): pass

    label('loc_2941')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Return,
        ),
        'loc_29BF',
    )

    ChrTalk(
        0x0009,
        (
            '#0570080279V#680F又给你们添麻烦了，\n',
            '拜托你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080280V无论如何请帮忙\n',
            '到平原道找到那个客人，\n',
            '并把她平安地带回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2ABB')

    def _loc_29BF(): pass

    label('loc_29BF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_2A45',
    )

    ChrTalk(
        0x0009,
        (
            '#0570080276V#680F怎么，忘了\n',
            '水泵小屋在哪里？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080277V走到村子的广场那里，\n',
            '从北面的斜坡上去就到了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570080278V那么就拜托你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2ABB')

    def _loc_2A45(): pass

    label('loc_2A45')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_2ABB',
    )

    ChrTalk(
        0x0009,
        (
            '#0570080274V#680F嘿～欢迎。\n',
            '本旅馆有我们引以为豪的天然温泉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0571360002V其中东方风格的露天澡堂\n',
            '特别受客人们欢迎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2ABB(): pass

    label('loc_2ABB')

    TalkEnd(0x0009)

    Return()

# id: 0x0013 offset: 0x2ABF
@scena.Code('func_13_2ABF')
def func_13_2ABF():
    EventBegin(0x00)
    ClearMapFlags(0x00000001)
    CameraMove(10910, 0, 69600, 0)
    SetChrPos(0x0101, 11690, 0, 68340, 180)
    SetChrPos(0x0102, 11420, 0, 67000, 45)
    SetChrPos(0x0107, 12710, 0, 66950, 315)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010080337V#502F#2P好了。\n',
            '行李已经放好了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080338V#505F对了，温泉在哪呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080339V#560F#6P啊……\n',
            '后面不远处就是泡澡专用的温泉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080340V而且里面还有\n',
            '一个很大的露天温泉哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080341V#010F#1P说到露天温泉……\n',
            '就是在室外建造的澡堂吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080342V#006F#2P嘿嘿～好像很有趣嘛！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080343V#001F那么，我们出发吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearMapFlags(0x10000000)
    EventEnd(0x00)

    Return()

# id: 0x0014 offset: 0x2C57
@scena.Code('func_14_2C57')
def func_14_2C57():
    EventBegin(0x00)
    ClearMapFlags(0x00000001)
    CameraMove(12630, 0, 1940, 0)
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x0102, 0x0080)
    SetChrFlags(0x0107, 0x0080)
    SetChrFlags(0x0013, 0x0080)
    SetChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0008, 0x0004)
    SetChrPos(0x0008, 14070, 0, 2040, 180)
    ClearChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x0017, 0x0080)
    ClearChrFlags(0x0018, 0x0080)
    ClearChrFlags(0x0019, 0x0080)
    ClearChrFlags(0x001A, 0x0080)
    SetChrPos(0x0016, 14600, 750, 1030, 0)
    SetChrPos(0x0017, 13500, 700, 950, 0)
    SetChrPos(0x0018, 13380, 700, 500, 0)
    SetChrPos(0x0019, 13870, 700, 660, 0)
    SetChrPos(0x001A, 13800, 700, 310, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0280080573V#152F#2P唔，好慢啊～\n',
            '小艾他们去哪儿了嘛～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280080574V呼～还没吃晚饭，\n',
            '肚子就喝得这么涨了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x00000BB8)
    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(500)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '泡完温泉后的艾丝蒂尔他们\n',
            '先是安慰生气的朵洛希，\n',
            '接着一起品尝旅馆引以为豪的东方料理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '晚饭过后四人玩纸牌助兴，\n',
            '玩了一阵子之后又再去泡温泉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '就这样，\n',
            '众人在温泉乡度过了轻松有趣的一天。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    PlaySE(13, 0x00, 0x64)
    SetChrStatus(0x0000, 0xFE, 0)
    SetChrStatus(0x0001, 0xFE, 0)
    SetChrStatus(0x0002, 0xFE, 0)
    SetChrStatus(0x0003, 0xFE, 0)
    SetChrStatus(0x0004, 0xFE, 0)
    SetChrStatus(0x0005, 0xFE, 0)
    SetChrStatus(0x0006, 0xFE, 0)
    SetChrStatus(0x0007, 0xFE, 0)
    Sleep(5000)

    OP_21()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T3200._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0015 offset: 0x2EA0
@scena.Code('func_15_2EA0')
def func_15_2EA0():
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

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

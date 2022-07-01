import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4122_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4122   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '菲尔妲'),
    TXT(0x02, '莎夏'),
    TXT(0x03, '哈尔德'),
    TXT(0x04, '乘客'),
    TXT(0x05, '乘客'),
    TXT(0x06, '乘客'),
    TXT(0x07, '布露姆老奶奶'),
    TXT(0x08, '莉莉'),
    TXT(0x09, '丹顿'),
    TXT(0x0A, '蜜蒂'),
    TXT(0x0B, '艾德尔店长'),
    TXT(0x0C, '基蒂'),
    TXT(0x0D, '希娜'),
    TXT(0x0E, '特雷诺'),
    TXT(0x0F, '布露姆老奶奶'),
    TXT(0x10, '阿加特'),
    TXT(0x11, '雪拉扎德'),
    TXT(0x12, '提妲'),
    TXT(0x13, '穆拉'),
    TXT(0x14, '中年男子'),
    TXT(0x15, '戴眼镜的女性'),
    TXT(0x16, '玲'),
    TXT(0x17, '目标用照相机'),
    TXT(0x18, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4122.x'
    header.mapIndex       = 1
    header.bgm            = 14
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x6142
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
        ('ED6_DT07/CH01290._CH', 'ED6_DT07/CH01290P._CP'),
        ('ED6_DT07/CH01540._CH', 'ED6_DT07/CH01540P._CP'),
        ('ED6_DT27/CH03570._CH', 'ED6_DT27/CH03570P._CP'),
        ('ED6_DT27/CH03710._CH', 'ED6_DT27/CH03710P._CP'),
        ('ED6_DT27/CH03720._CH', 'ED6_DT27/CH03720P._CP'),
        ('ED6_DT27/CH03510._CH', 'ED6_DT27/CH03510P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01770._CH', 'ED6_DT07/CH01770P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH01010._CH', 'ED6_DT07/CH01010P._CP'),
        ('ED6_DT07/CH01013._CH', 'ED6_DT07/CH01013P._CP'),
        ('ED6_DT07/CH00050._CH', 'ED6_DT07/CH00050P._CP'),
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT27/CH03060._CH', 'ED6_DT27/CH03060P._CP'),
    ]

# id: 0x10002 offset: 0x132
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -1440,
            z                   = 0,
            y                   = 65550,
            direction           = 179,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 1970,
            z                   = 0,
            y                   = 65550,
            direction           = 175,
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
            x                   = -3140,
            z                   = 0,
            y                   = 63640,
            direction           = 6,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            x                   = -4370,
            z                   = 0,
            y                   = 62760,
            direction           = 92,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            x                   = 4950,
            z                   = 0,
            y                   = 60820,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            x                   = -3020,
            z                   = 0,
            y                   = 57190,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0016,
        ),
        ScenaNpcData(
            x                   = 3110,
            z                   = 250,
            y                   = 60150,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0195,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            x                   = 8790,
            z                   = 0,
            y                   = 10500,
            direction           = 196,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = 12170,
            z                   = 0,
            y                   = -4050,
            direction           = 163,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = -4540,
            z                   = 0,
            y                   = 9850,
            direction           = 270,
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
            x                   = -50,
            z                   = 0,
            y                   = 10,
            direction           = 204,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = -13690,
            z                   = 250,
            y                   = 11270,
            direction           = 191,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = -13060,
            z                   = 0,
            y                   = 6390,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = 13590,
            z                   = 0,
            y                   = -8540,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            x                   = -10100,
            z                   = 0,
            y                   = -7930,
            direction           = 200,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            x                   = 90,
            z                   = 0,
            y                   = 63630,
            direction           = 343,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0018,
        ),
        ScenaNpcData(
            x                   = 90,
            z                   = 0,
            y                   = 63630,
            direction           = 343,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0019,
        ),
        ScenaNpcData(
            x                   = 2900,
            z                   = 0,
            y                   = 3330,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001A,
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
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
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
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
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
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
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
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001B,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0080,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x412
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x412
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x412
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 8450,
            triggerZ            = 0,
            triggerY            = 8650,
            triggerRange        = 800,
            actorX              = 8790,
            actorZ              = 1500,
            actorY              = 10500,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 11970,
            triggerZ            = 0,
            triggerY            = -5950,
            triggerRange        = 800,
            actorX              = 12170,
            actorZ              = 1500,
            actorY              = -4050,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -6400,
            triggerZ            = 0,
            triggerY            = 9620,
            triggerRange        = 800,
            actorX              = -4540,
            actorZ              = 1500,
            actorY              = 9850,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -1370,
            triggerZ            = 0,
            triggerY            = 63610,
            triggerRange        = 800,
            actorX              = -1440,
            actorZ              = 1500,
            actorY              = 65550,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000F,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 1850,
            triggerZ            = 0,
            triggerY            = 63640,
            triggerRange        = 800,
            actorX              = 1970,
            actorZ              = 1500,
            actorY              = 65550,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0011,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x4C6
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_4EF',
    )

    SetChrFlags(0x0013, 0x0080)
    SetChrPos(0x0011, -13690, 250, 11270, 191)
    OP_64(0x02, 0x0001)
    SetChrFlags(0x0016, 0x0080)

    Jump('loc_586')

    def _loc_4EF(): pass

    label('loc_4EF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_51D',
    )

    SetChrFlags(0x0013, 0x0080)
    SetChrPos(0x0011, -13690, 250, 11270, 191)
    OP_64(0x02, 0x0001)
    SetChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x000E, 0x0080)

    Jump('loc_586')

    def _loc_51D(): pass

    label('loc_51D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_56A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 5, 0x161D)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_567',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_540',
    )

    ClearChrFlags(0x0017, 0x0080)

    Jump('loc_545')

    def _loc_540(): pass

    label('loc_540')

    ClearChrFlags(0x0018, 0x0080)

    def _loc_545(): pass

    label('loc_545')

    ClearChrFlags(0x0019, 0x0080)
    ClearChrFlags(0x001D, 0x0080)
    SetChrPos(0x001D, 5430, 0, 1900, 0)
    CreateThread(0x001D, 0x00, 0x00, 0x0002)

    def _loc_567(): pass

    label('loc_567')

    Jump('loc_586')

    def _loc_56A(): pass

    label('loc_56A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 5, 0x1205)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_586',
    )

    SetChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)

    def _loc_586(): pass

    label('loc_586')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_5A2'),
        (0x00000065, 'loc_5A2'),
        (0x00000066, 'loc_5A2'),
        (0x00000067, 'loc_5A2'),
        (0x00000068, 'loc_5BA'),
        (-1, 'loc_5D7'),
    )

    def _loc_5A2(): pass

    label('loc_5A2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 6, 0x162E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5B7',
    )

    SetMapFlags(0x10000000)
    Event(0, 0x0020)

    def _loc_5B7(): pass

    label('loc_5B7')

    Jump('loc_5D7')

    def _loc_5BA(): pass

    label('loc_5BA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 2, 0x1202)),
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 3, 0x1203)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5D4',
    )

    ClearMapFlags(0x00000010)
    SetMapFlags(0x10000000)
    Event(0, 0x001C)

    def _loc_5D4(): pass

    label('loc_5D4')

    Jump('loc_5D7')

    def _loc_5D7(): pass

    label('loc_5D7')

    Return()

# id: 0x0001 offset: 0x5D8
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5F4',
    )

    OP_B1('t4122_y')

    Jump('loc_5FD')

    def _loc_5F4(): pass

    label('loc_5F4')

    OP_B1('t4122_n')

    def _loc_5FD(): pass

    label('loc_5FD')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_615',
    )

    OP_10(0x06, 0x00)
    OP_10(0x05, 0x01)
    OP_10(0x04, 0x00)

    Jump('loc_644')

    def _loc_615(): pass

    label('loc_615')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_628',
    )

    OP_10(0x06, 0x00)
    OP_10(0x05, 0x00)
    OP_10(0x04, 0x01)

    Jump('loc_644')

    def _loc_628(): pass

    label('loc_628')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_63B',
    )

    OP_10(0x06, 0x00)
    OP_10(0x04, 0x00)
    OP_10(0x05, 0x01)

    Jump('loc_644')

    def _loc_63B(): pass

    label('loc_63B')

    OP_10(0x06, 0x00)
    OP_10(0x05, 0x00)
    OP_10(0x04, 0x01)

    def _loc_644(): pass

    label('loc_644')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_668',
    )

    OP_72(0x0000, 0x0010)
    OP_6F(0x0000, 59)
    OP_72(0x0001, 0x0010)
    OP_6F(0x0001, 59)

    def _loc_668(): pass

    label('loc_668')

    Return()

# id: 0x0002 offset: 0x669
@scena.Code('ReInit')
def ReInit():
    ExecExpressionWithReg(
        0x0001,
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
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_68E',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_7D0')

    def _loc_68E(): pass

    label('loc_68E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6A7',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000640)

    Jump('loc_7D0')

    def _loc_6A7(): pass

    label('loc_6A7')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6C0',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x0000060E)

    Jump('loc_7D0')

    def _loc_6C0(): pass

    label('loc_6C0')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6D9',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005DC)

    Jump('loc_7D0')

    def _loc_6D9(): pass

    label('loc_6D9')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6F2',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AA)

    Jump('loc_7D0')

    def _loc_6F2(): pass

    label('loc_6F2')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_70B',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x00000578)

    Jump('loc_7D0')

    def _loc_70B(): pass

    label('loc_70B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_724',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x00000546)

    Jump('loc_7D0')

    def _loc_724(): pass

    label('loc_724')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_73D',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000677)

    Jump('loc_7D0')

    def _loc_73D(): pass

    label('loc_73D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_756',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000645)

    Jump('loc_7D0')

    def _loc_756(): pass

    label('loc_756')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_76F',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x00000613)

    Jump('loc_7D0')

    def _loc_76F(): pass

    label('loc_76F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_788',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005E1)

    Jump('loc_7D0')

    def _loc_788(): pass

    label('loc_788')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7A1',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AF)

    Jump('loc_7D0')

    def _loc_7A1(): pass

    label('loc_7A1')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7BA',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x0000057D)

    Jump('loc_7D0')

    def _loc_7BA(): pass

    label('loc_7BA')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7D0',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x0000054B)

    def _loc_7D0(): pass

    label('loc_7D0')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_7E5',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_7D0')

    def _loc_7E5(): pass

    label('loc_7E5')

    Return()

# id: 0x0003 offset: 0x7E6
@scena.Code('func_03_7E6')
def func_03_7E6():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_809',
    )

    OP_8D(0x00FE, -11560, -6690, -7260, -10580, 1000)

    Jump('func_03_7E6')

    def _loc_809(): pass

    label('loc_809')

    Return()

# id: 0x0004 offset: 0x80A
@scena.Code('func_04_80A')
def func_04_80A():
    Call(0, 0x0005)

    Return()

# id: 0x0005 offset: 0x80F
@scena.Code('func_05_80F')
def func_05_80F():
    TalkBegin(0x000F)
    Call(6, 0x0004)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_846',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_834',
    )

    OP_A9(0xD8)

    Jump('loc_842')

    def _loc_834(): pass

    label('loc_834')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_840',
    )

    OP_A9(0xD7)

    Jump('loc_842')

    def _loc_840(): pass

    label('loc_840')

    OP_A9(0xD2)

    def _loc_842(): pass

    label('loc_842')

    TalkEnd(0x000F)

    Return()

    def _loc_846(): pass

    label('loc_846')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_857',
    )

    TalkEnd(0x000F)

    Return()

    def _loc_857(): pass

    label('loc_857')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_900',
    )

    ChrTalk(
        0x000F,
        (
            '欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '因为导力的停止，\n',
            '利贝尔通讯的最新一期\n',
            '只在王都发售哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '即便如此，我还是很佩服能按时\n',
            '制作出杂志的编辑和记者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '我也得努力贩卖啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BE9')

    def _loc_900(): pass

    label('loc_900')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_966',
    )

    ChrTalk(
        0x000F,
        (
            '今天从早上起大家就\n',
            '都在议论那起事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '能在签字仪式前抓获\n',
            '情报部的余党真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BE9')

    def _loc_966(): pass

    label('loc_966')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_A14',
    )

    ChrTalk(
        0x000F,
        (
            '尊敬的顾客，利贝尔通讯的\n',
            '最新一期已经到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '特辑可是卢安市长的\n',
            '选举结果哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '我虽然不能在工作时间阅读，\n',
            '不过封面还是能看清的，\n',
            '真是令人牵肠挂肚啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BE9')

    def _loc_A14(): pass

    label('loc_A14')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_A89',
    )

    ChrTalk(
        0x000F,
        (
            '对柏斯超市的考察\n',
            '似乎深深刺激了\n',
            '基蒂小姐呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '她说下次休假\n',
            '还要去柏斯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '难道基蒂小姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BE9')

    def _loc_A89(): pass

    label('loc_A89')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_BA7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B58',
    )

    ChrTalk(
        0x000F,
        (
            '前几天我们在店长的\n',
            '计划下去考察了柏斯超市。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '我还真担心对方\n',
            '会认出我是同行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '店长还向店员堂而皇之地\n',
            '咨询了进货的价格呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '那份爽快的气质似乎还\n',
            '很受柏斯市长的赏识……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    Jump('loc_BA4')

    def _loc_B58(): pass

    label('loc_B58')

    ChrTalk(
        0x000F,
        (
            '店长和柏斯市长还挺\n',
            '惺惺相惜的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '今后还会通过交换信息\n',
            '来相互合作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BA4(): pass

    label('loc_BA4')

    Jump('loc_BE9')

    def _loc_BA7(): pass

    label('loc_BA7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_BE9',
    )

    ChrTalk(
        0x000F,
        (
            '欢迎～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '艾德尔百货店从礼品\n',
            '到日用品应有尽有哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BE9(): pass

    label('loc_BE9')

    TalkEnd(0x000F)

    Return()

# id: 0x0006 offset: 0xBED
@scena.Code('func_06_BED')
def func_06_BED():
    Call(0, 0x0007)

    Return()

# id: 0x0007 offset: 0xBF2
@scena.Code('func_07_BF2')
def func_07_BF2():
    TalkBegin(0x0010)
    Call(6, 0x0004)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C0C',
    )

    OP_A9(0xD3)
    TalkEnd(0x0010)

    Return()

    def _loc_C0C(): pass

    label('loc_C0C')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C1D',
    )

    TalkEnd(0x0010)

    Return()

    def _loc_C1D(): pass

    label('loc_C1D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_C72',
    )

    ChrTalk(
        0x0010,
        (
            '我们店长很可靠吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '平日里那句『我在雪山上\n',
            '也要卖冰』可不是盖的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EAE')

    def _loc_C72(): pass

    label('loc_C72')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_CF8',
    )

    ChrTalk(
        0x0010,
        (
            '理查德上校在市民中\n',
            '很有人气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '我也能理解作为他直属部下的\n',
            '情报部的那群人的心情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '不过也不用出动坦克吧、坦克。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EAE')

    def _loc_CF8(): pass

    label('loc_CF8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_D6D',
    )

    ChrTalk(
        0x0010,
        (
            '卢安市长已经\n',
            '决定了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '希望这样一来各种\n',
            '交易都能顺利进行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '一定要请这位新\n',
            '市长多多努力了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EAE')

    def _loc_D6D(): pass

    label('loc_D6D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_DD5',
    )

    ChrTalk(
        0x0010,
        (
            '不过我从顾客那里听到\n',
            '一个传言，不知是真是假。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '好像说卢安的各地\n',
            '都出现了幽灵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EAE')

    def _loc_DD5(): pass

    label('loc_DD5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_E70',
    )

    ChrTalk(
        0x0010,
        (
            '真希望卢安的新市长\n',
            '能够快点选出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '自从戴尔蒙市长事件以来，\n',
            '卢安方向的物流就很混乱了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '也难怪，因为有很多手续\n',
            '必须有市长的许可。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EAE')

    def _loc_E70(): pass

    label('loc_E70')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_EAE',
    )

    ChrTalk(
        0x0010,
        (
            '欢迎光临，你们是观光吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '这里有各式\n',
            '礼品哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EAE(): pass

    label('loc_EAE')

    TalkEnd(0x0010)

    Return()

# id: 0x0008 offset: 0xEB2
@scena.Code('func_08_EB2')
def func_08_EB2():
    Call(0, 0x0009)

    Return()

# id: 0x0009 offset: 0xEB7
@scena.Code('func_09_EB7')
def func_09_EB7():
    TalkBegin(0x0011)
    Call(6, 0x0004)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_ED1',
    )

    OP_A9(0xD4)
    TalkEnd(0x0011)

    Return()

    def _loc_ED1(): pass

    label('loc_ED1')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_EE2',
    )

    TalkEnd(0x0011)

    Return()

    def _loc_EE2(): pass

    label('loc_EE2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_F86',
    )

    ChrTalk(
        0x0011,
        (
            '本是去柏斯的\n',
            '姐姐现在好像在洛连特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '呼，太好了……她没事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '我、我可没在担心她。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '都是因为我要和她堂堂正正\n',
            '地较量，夺取红茶销售员职务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13AD')

    def _loc_F86(): pass

    label('loc_F86')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1089',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1036',
    )

    ChrTalk(
        0x0011,
        (
            '姐姐为了开一间自己的店，\n',
            '好像要去柏斯学习。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '有可能就会辞去\n',
            '百货商店的工作……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '姐姐，别丢下我，\n',
            '我会寂寞的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    Jump('loc_1086')

    def _loc_1036(): pass

    label('loc_1036')

    ChrTalk(
        0x0011,
        (
            '姐姐有可能就要辞去\n',
            '百货商店的工作……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '姐姐，别丢下我，\n',
            '我会寂寞的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1086(): pass

    label('loc_1086')

    Jump('loc_13AD')

    def _loc_1089(): pass

    label('loc_1089')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_110E',
    )

    ChrTalk(
        0x0011,
        (
            '呼呼呼……\n',
            '来了……终于来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '在姐姐不在期间，\n',
            '由我负责红茶销售。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '看着吧，我要从姐姐那里\n',
            '抢走销售员的位子！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13AD')

    def _loc_110E(): pass

    label('loc_110E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1184',
    )

    ChrTalk(
        0x0011,
        (
            '最近姐姐好像\n',
            '一直在想心事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '看着吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '我要在她还在发呆的时候\n',
            '让她失去红茶销售员的职位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13AD')

    def _loc_1184(): pass

    label('loc_1184')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_12B7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_126D',
    )

    ChrTalk(
        0x0011,
        (
            '现在想想，姐姐从小到大\n',
            '都是一个人占便宜！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '因为她低血压，每天早上\n',
            '总是我去拿报纸！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '因为她害怕蟑螂，\n',
            '每次都是我负责消灭！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '明明是双胞胎，为什么\n',
            '只有我吃了甜的会发胖！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '每一条都令人无法原谅！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    Jump('loc_12B4')

    def _loc_126D(): pass

    label('loc_126D')

    ChrTalk(
        0x0011,
        (
            '看着吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '至少要让她把从我这里夺走的\n',
            '红茶销售员位子抢回来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12B4(): pass

    label('loc_12B4')

    Jump('loc_13AD')

    def _loc_12B7(): pass

    label('loc_12B7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_13AD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_136A',
    )

    ChrTalk(
        0x0011,
        (
            '嗯～泡出美味红茶的\n',
            '黄金秘诀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '……我这个人，\n',
            '一听到『学习』这两个字\n',
            '就犯困……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '啊，不可以不可以。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '一切都为了夺回姐姐的\n',
            '红茶销售员位子！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    Jump('loc_13AD')

    def _loc_136A(): pass

    label('loc_136A')

    ChrTalk(
        0x0011,
        (
            '可恶！绝不能睡着！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '一切都为了夺回姐姐的\n',
            '红茶销售员位子！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13AD(): pass

    label('loc_13AD')

    TalkEnd(0x0011)

    Return()

# id: 0x000A offset: 0x13B1
@scena.Code('func_0A_13B1')
def func_0A_13B1():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1463',
    )

    ChrTalk(
        0x00FE,
        (
            '没有货进来的话，\n',
            '只能我们自己去进货来卖了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '能卖的都要卖得一干二净！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为顾客需要\n',
            '我们的商品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算有些事我们没办法，\n',
            '可是还有一大堆可以做的事！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16AB')

    def _loc_1463(): pass

    label('loc_1463')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_14F0',
    )

    ChrTalk(
        0x00FE,
        (
            '我家在西街区，\n',
            '能听到港口传来很响的声音。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '想不到竟是情报部的坦克，\n',
            '连我也吓了一跳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还好房子没被那玩意儿\n',
            '给毁了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16AB')

    def _loc_14F0(): pass

    label('loc_14F0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_157B',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才出去的那女孩子，\n',
            '最近好像常见到……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像是个游客，\n',
            '可她父母呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有很多小孩子在这家店\n',
            '迷路，真有点担心她呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16AB')

    def _loc_157B(): pass

    label('loc_157B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_15C9',
    )

    ChrTalk(
        0x00FE,
        (
            '实在抱歉，\n',
            '本店很快就要打烊了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '欢迎您的\n',
            '再度光临～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16AB')

    def _loc_15C9(): pass

    label('loc_15C9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_1646',
    )

    ChrTalk(
        0x00FE,
        (
            '这种时节销售额\n',
            '很容易下滑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以更要利用签字仪式\n',
            '这一大事件了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好，我们要大搞条约\n',
            '缔结纪念的促销！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16AB')

    def _loc_1646(): pass

    label('loc_1646')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_16AB',
    )

    ChrTalk(
        0x00FE,
        (
            '欢迎光临，\n',
            '欢迎光临艾德尔百货店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们正在为了打倒柏斯超市\n',
            '这一目标而不懈地努力～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_16AB(): pass

    label('loc_16AB')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x16AF
@scena.Code('func_0B_16AF')
def func_0B_16AF():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_16FA',
    )

    ChrTalk(
        0x00FE,
        (
            '我从明天起要\n',
            '休假一阵子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '红茶角就交给\n',
            '妹妹蜜蒂了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_187D')

    def _loc_16FA(): pass

    label('loc_16FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1788',
    )

    ChrTalk(
        0x00FE,
        (
            '能被带去参观\n',
            '柏斯超市真让我\n',
            '受益匪浅。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不仅如此，我还……\n',
            '找到了自己前进的方向。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然现在还不能告诉\n',
            '妹妹蜜蒂……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_187D')

    def _loc_1788(): pass

    label('loc_1788')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_180E',
    )

    ChrTalk(
        0x00FE,
        (
            '欢迎光临！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '尊敬的客人，要不要\n',
            '来一杯美味的红茶？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果您想知道怎样\n',
            '泡出美味的红茶',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就问我吧，请不要客气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_187D')

    def _loc_180E(): pass

    label('loc_180E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_187D',
    )

    ChrTalk(
        0x00FE,
        (
            '前几天我和店里的同事们\n',
            '去参观了柏斯的市场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '超市里面的每个人\n',
            '都很努力……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这令我很感动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_187D(): pass

    label('loc_187D')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x1881
@scena.Code('func_0C_1881')
def func_0C_1881():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1906',
    )

    ChrTalk(
        0x00FE,
        (
            '最近，鱼都从钓公师团买，\n',
            '而不是从卢安了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本以为他们只是普通的兴趣团体，\n',
            '不过在导力停止后他们真是活跃啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A79')

    def _loc_1906(): pass

    label('loc_1906')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1960',
    )

    ChrTalk(
        0x00FE,
        (
            '城里很吵啊，\n',
            '是不是出了什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近我忙于家务，\n',
            '都有点不问世事了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A79')

    def _loc_1960(): pass

    label('loc_1960')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_19A8',
    )

    ChrTalk(
        0x00FE,
        (
            '好想吃久违的\n',
            '卢安海鲜啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近在这儿都\n',
            '很难买到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A79')

    def _loc_19A8(): pass

    label('loc_19A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_19E7',
    )

    ChrTalk(
        0x00FE,
        (
            '唔～今天来得太晚，\n',
            '都没什么好东西留下了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A79')

    def _loc_19E7(): pass

    label('loc_19E7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_1A18',
    )

    ChrTalk(
        0x00FE,
        (
            '为了健康也得\n',
            '让我家那口子吃蔬菜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A79')

    def _loc_1A18(): pass

    label('loc_1A18')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_1A79',
    )

    ChrTalk(
        0x00FE,
        (
            '最近在蔡斯似乎\n',
            '频繁发生着地震呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '近来我都没去了，\n',
            '也不知道亚尔摩温泉怎么样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A79(): pass

    label('loc_1A79')

    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x1A7D
@scena.Code('func_0D_1A7D')
def func_0D_1A7D():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1AD1',
    )

    ChrTalk(
        0x00FE,
        (
            '现在比起那些瓶瓶罐罐的，\n',
            '还是得先保存食品……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是不得了了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D15')

    def _loc_1AD1(): pass

    label('loc_1AD1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1B5E',
    )

    ChrTalk(
        0x00FE,
        (
            '昨晚我看见亲卫队的队员\n',
            '跑去西街区哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一架像大炮一样的东西\n',
            '从飞船坪移动过来了，\n',
            '那是什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这、这还闹得真不小……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D15')

    def _loc_1B5E(): pass

    label('loc_1B5E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_1BCB',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯？你们好像在赶时间？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '由我这个顾客来说可能不太合适，\n',
            '不过你们可别碰翻这些瓶瓶罐罐的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D15')

    def _loc_1BCB(): pass

    label('loc_1BCB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1C14',
    )

    ChrTalk(
        0x00FE,
        (
            '已经傍晚了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '得赶紧回去了，\n',
            '不然老婆要唠叨。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D15')

    def _loc_1C14(): pass

    label('loc_1C14')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_1C5E',
    )

    ChrTalk(
        0x00FE,
        (
            '哟，这壶是中世纪帝国的东西啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……真是个不错的壶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D15')

    def _loc_1C5E(): pass

    label('loc_1C5E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_1D15',
    )

    ChrTalk(
        0x00FE,
        (
            '做为政变的主犯之一……\n',
            '杜南公爵好像受到了女王\n',
            '陛下要求他谨慎而居的处分呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '自称是公爵管家的人\n',
            '时常来这家店买东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可不知为什么，\n',
            '每次来买的都是炸面圈和连环画。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D15(): pass

    label('loc_1D15')

    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x1D19
@scena.Code('func_0E_1D19')
def func_0E_1D19():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1D71',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我还是没能为儿子\n',
            '找到结婚对象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是羞愧又不甘心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F8F')

    def _loc_1D71(): pass

    label('loc_1D71')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_1E12',
    )

    ChrTalk(
        0x00FE,
        (
            '我为儿子找结婚对象很久了，\n',
            '不过仍然没有合适的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '王都的人是多，\n',
            '不过都是些吊儿郎当的孩子，\n',
            '怎么也看不上眼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，看来得换个街区了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F8F')

    def _loc_1E12(): pass

    label('loc_1E12')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1ECE',
    )

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '……我好像在哪儿见过你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '（嗯……好像\n',
            '#1015F　是在哪儿见过。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '（……她是谁？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我这几个月看过\n',
            '不少女孩子，\n',
            '不可能一个个都记住。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我可没有在发呆！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F8F')

    def _loc_1ECE(): pass

    label('loc_1ECE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_1F59',
    )

    ChrTalk(
        0x00FE,
        (
            '我是为了给儿子找结婚对象\n',
            '才来的王都。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果你们认识好的女孩子\n',
            '一定要介绍给我哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎么也找不到让我\n',
            '满意的女孩子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F8F')

    def _loc_1F59(): pass

    label('loc_1F59')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_1F8F',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '走得太累了，\n',
            '在这里休息一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F8F(): pass

    label('loc_1F8F')

    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x1F93
@scena.Code('func_0F_1F93')
def func_0F_1F93():
    Call(0, 0x0010)

    Return()

# id: 0x0010 offset: 0x1F98
@scena.Code('func_10_1F98')
def func_10_1F98():
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
            TXT(0x01, '买东西\n'),
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
    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1FF3'),
        (0x00000001, 'loc_24E6'),
        (-1, 'loc_251B'),
    )

    def _loc_1FF3(): pass

    label('loc_1FF3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_20A2',
    )

    ChrTalk(
        0x0008,
        (
            '一时间这里也聚集了不少人，\n',
            '不过在女王陛下的帮助下\n',
            '总算恢复了平静。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '听说不久前在蔡斯\n',
            '似乎也发生了\n',
            '相似的事件……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '想不到导力器不能用\n',
            '会令人如此不安……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24E3')

    def _loc_20A2(): pass

    label('loc_20A2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_2103',
    )

    ChrTalk(
        0x0008,
        (
            '听见情报部三个字我就火大。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '在他们的『帮助』下，\n',
            '我和公司都蒙受了巨大的损失。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24E3')

    def _loc_2103(): pass

    label('loc_2103')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 5, 0x1635)),
            Expr.Return,
        ),
        'loc_2171',
    )

    ChrTalk(
        0x0008,
        (
            '哟，工程船和林德号\n',
            '按计划进港了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '啊～能按计划开始\n',
            '工作真是太好了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '本来就应该是这样',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24E3')

    def _loc_2171(): pass

    label('loc_2171')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_21D7',
    )

    ChrTalk(
        0x0008,
        (
            '我们接到了要求紧急准备\n',
            '『埃尔赛尤』用的跑道的通知！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '得赶紧通知工作人员\n',
            '检查跑道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24E3')

    def _loc_21D7(): pass

    label('loc_21D7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2283',
    )

    ChrTalk(
        0x0008,
        (
            '1、2、3……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '嗯～这样一来指定的\n',
            '那段时间的名单就全了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '游击士协会让我们\n',
            '提供一份乘客名单。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '平时总受他们照顾，\n',
            '这点协助调查是理所应当的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24E3')

    def _loc_2283(): pass

    label('loc_2283')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_230A',
    )

    ChrTalk(
        0x0008,
        (
            '政变后真不得了了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '又要善后，还要兼顾\n',
            '定期船的正常\n',
            '运行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '现在回忆起那时每天加班的情景\n',
            '还是会让人掉眼泪啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24E3')

    def _loc_230A(): pass

    label('loc_230A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_239E',
    )

    ChrTalk(
        0x0008,
        (
            '最近的飞船都按\n',
            '计划在运行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '政变时因为\n',
            '军用船的出入和情报部的\n',
            '封锁而变得一团糟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我也『可喜可贺』地被\n',
            '克雷马负责人解职了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24E3')

    def _loc_239E(): pass

    label('loc_239E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_2444',
    )

    ChrTalk(
        0x0008,
        (
            '说起来关于新型引擎的\n',
            '内容应该询问作为开发方的\n',
            '中央工房，而非飞船公社啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '说到底，我们只负责维修\n',
            '兼临时保管。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '外国人大概是不太\n',
            '明白这一点的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24E3')

    def _loc_2444(): pass

    label('loc_2444')

    OP_A2(0x0000)

    ChrTalk(
        0x0008,
        (
            '呼，现在的人\n',
            '脾气都这么大啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '也难怪，因为那是\n',
            '高速巡洋舰『埃尔赛尤』搭载的\n',
            '新型引擎样本啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我理解他们那股子拼命劲儿，\n',
            '但毕竟是还没完成啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_24E3(): pass

    label('loc_24E3')

    Jump('loc_251E')

    def _loc_24E6(): pass

    label('loc_24E6')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_24F7',
    )

    OP_A9(0xD9)

    Jump('loc_2516')

    def _loc_24F7(): pass

    label('loc_24F7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_2503',
    )

    OP_A9(0xD1)

    Jump('loc_2516')

    def _loc_2503(): pass

    label('loc_2503')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2514',
    )

    OP_A9(0xD0)

    Jump('loc_2516')

    def _loc_2514(): pass

    label('loc_2514')

    OP_A9(0xCF)

    def _loc_2516(): pass

    label('loc_2516')

    OP_56(0x00)

    Jump('loc_251E')

    def _loc_251B(): pass

    label('loc_251B')

    Jump('loc_251E')

    def _loc_251E(): pass

    label('loc_251E')

    TalkEnd(0x0008)

    Return()

# id: 0x0011 offset: 0x2522
@scena.Code('func_11_2522')
def func_11_2522():
    Call(0, 0x0012)

    Return()

# id: 0x0012 offset: 0x2527
@scena.Code('func_12_2527')
def func_12_2527():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_256B',
    )

    ChrTalk(
        0x0009,
        (
            '现在所有的飞船都\n',
            '暂停飞行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '敬请大家谅解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C7F')

    def _loc_256B(): pass

    label('loc_256B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_25B3',
    )

    ChrTalk(
        0x0009,
        (
            '刚才林德号起飞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '接下来向西的赛希莉亚号要进港了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C7F')

    def _loc_25B3(): pass

    label('loc_25B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 5, 0x1635)),
            Expr.Return,
        ),
        'loc_25FD',
    )

    ChrTalk(
        0x0009,
        (
            '现在第２跑道停着\n',
            '中央工房的船。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '请注意不要\n',
            '搞错跑道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C7F')

    def _loc_25FD(): pass

    label('loc_25FD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_2659',
    )

    ChrTalk(
        0x0009,
        (
            '林德号即将到达。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '要搭乘的顾客，\n',
            '在买好票之后\n',
            '请到外面的接待处办理手续。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C7F')

    def _loc_2659(): pass

    label('loc_2659')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2713',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_26C0',
    )

    ChrTalk(
        0x0009,
        (
            '刚才来了一个\n',
            '银发的女游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '她询问了我们关于\n',
            '公司收到的恐吓信的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2710')

    def _loc_26C0(): pass

    label('loc_26C0')

    ChrTalk(
        0x0009,
        (
            '刚才来了一个\n',
            '红发的游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '她询问了我们关于\n',
            '公司收到的恐吓信的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2710(): pass

    label('loc_2710')

    Jump('loc_2C7F')

    def _loc_2713(): pass

    label('loc_2713')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_2775',
    )

    ChrTalk(
        0x0009,
        (
            '因为恐吓信的缘故，\n',
            '公司内部确实产生了动摇。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '希望别引发造成顾客\n',
            '困扰的事件……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C7F')

    def _loc_2775(): pass

    label('loc_2775')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_279E',
    )

    ChrTalk(
        0x0009,
        (
            '欢迎！\n',
            '欢迎光临飞船公社。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C7F')

    def _loc_279E(): pass

    label('loc_279E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 4, 0x1204)),
            Expr.Return,
        ),
        'loc_27EE',
    )

    ChrTalk(
        0x0009,
        (
            '#5P请把您的票\n',
            '交到外面的\n',
            '接待处。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#5P请在那里办理登船手续。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C7F')

    def _loc_27EE(): pass

    label('loc_27EE')

    EventBegin(0x00)
    Fade(1000)
    OP_4A(0x0009, 255)
    OP_8C(0x0009, 180, 0)
    OP_6D(1800, 0, 64920, 0)
    SetChrPos(0x00F7, 2190, 0, 63630, 0)
    SetChrPos(0x0101, 1250, 0, 63630, 0)
    OP_0D()

    ChrTalk(
        0x0009,
        (
            '#2780200544V#5P欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2780200545V#5P请问是要搭乘国内航班，\n',
            '还是要搭乘国际航班呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200546V#6P#1006F嗯～我们需要2张\n',
            '前往卢安的船票。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2780200547V#5P请稍等……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2780200548V#5P啊，小姐，\n',
            '你们是游击士协会的人吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2A9C',
    )

    ChrTalk(
        0x0009,
        (
            '#2780200549V#5P请问是艾丝蒂尔小姐和阿加特先生\n',
            '吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200550V#6P#1004F嗯、嗯，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2780200551V#5P王都支部的艾南先生\n',
            '已经替你们付了船票费用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2780200552V#5P请拿好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了２张',
            (TxtCtl.Item, ItemTable['船票']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['船票'], 2)

    ChrTalk(
        0x0101,
        (
            '#0010200553V#6P#1011F哦，是艾南先生啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050200554V#051F不愧是艾南。\n',
            '做事真是周到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C15')

    def _loc_2A9C(): pass

    label('loc_2A9C')

    ChrTalk(
        0x0009,
        (
            '#2780200555V#5P请问是艾丝蒂尔小姐和雪拉扎德小姐\n',
            '吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200550V#6P#1004F嗯、嗯，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2780200551V#5P王都支部的艾南先生\n',
            '已经替你们付了船票费用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2780200552V#5P请拿好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了２张',
            (TxtCtl.Item, ItemTable['船票']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['船票'], 2)

    ChrTalk(
        0x0101,
        (
            '#0010200553V#6P#1011F嘿嘿，是艾南先生啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030200560V#021F不愧是艾南先生。\n',
            '真是一如既往地细心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C15(): pass

    label('loc_2C15')

    ChrTalk(
        0x0009,
        (
            '#2780200561V#5P那么，请把票\n',
            '交到外面的\n',
            '接待处。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2780200562V#5P请在那里办理登船手续。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1204)
    OP_4B(0x0009, 255)
    EventEnd(0x00)

    Return()

    def _loc_2C7F(): pass

    label('loc_2C7F')

    TalkEnd(0x0009)

    Return()

# id: 0x0013 offset: 0x2C83
@scena.Code('func_13_2C83')
def func_13_2C83():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2CFD',
    )

    ChrTalk(
        0x000A,
        (
            '啊，这下玩儿完了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我努力促成的\n',
            '旅游路线这样一来\n',
            '也就泡汤了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '现在大家哪儿还\n',
            '顾得上旅游啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F72')

    def _loc_2CFD(): pass

    label('loc_2CFD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_2D85',
    )

    ChrTalk(
        0x000A,
        (
            '情报部的余党之前\n',
            '出现了，吓了我一跳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '治安一旦混乱，旅游的营业额\n',
            '就会一下子跌入谷底。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '他们都被逮捕真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F72')

    def _loc_2D85(): pass

    label('loc_2D85')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_2DF6',
    )

    ChrTalk(
        0x000A,
        (
            '唔，应该怎么办呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '安特洛丝餐厅的老板\n',
            '是个很\n',
            '固执的人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '应该不可能给旅游\n',
            '路线打折……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F72')

    def _loc_2DF6(): pass

    label('loc_2DF6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2E76',
    )

    ChrTalk(
        0x000A,
        (
            '唔，真难办。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我考虑了一下柏斯\n',
            '旅游路线的具体内容……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '如果在其中加上安特洛丝\n',
            '餐厅的话价格就会上升。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F72')

    def _loc_2E76(): pass

    label('loc_2E76')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_2F0D',
    )

    ChrTalk(
        0x000A,
        (
            '我准备和飞船公社\n',
            '合作筹划旅游路线。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我提议把前几天去考察的柏斯\n',
            '作为第一条路线，公司也表示赞同。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '接下来要确定\n',
            '路线的具体内容。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F72')

    def _loc_2F0D(): pass

    label('loc_2F0D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_2F72',
    )

    ChrTalk(
        0x000A,
        (
            '互不侵犯条约对旅游业应该是\n',
            '相当相当有利的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '真想以该条约为契机，\n',
            '多招揽些游客来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2F72(): pass

    label('loc_2F72')

    TalkEnd(0x00FE)

    Return()

# id: 0x0014 offset: 0x2F76
@scena.Code('func_14_2F76')
def func_14_2F76():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '刚才那两个人\n',
            '不知为什么气势汹汹的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看上去确实像有点\n',
            '来头的人，到底是谁呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0015 offset: 0x2FD3
@scena.Code('func_15_2FD3')
def func_15_2FD3():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '好、好可怕……\n',
            '这样一来终于可以买票了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0016 offset: 0x3007
@scena.Code('func_16_3007')
def func_16_3007():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '真是的，在这种场合\n',
            '发火就不嫌丢人吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真希望都能学学\n',
            '什么叫礼貌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0017 offset: 0x305C
@scena.Code('func_17_305C')
def func_17_305C():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '假定\n',
            '假定',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0018 offset: 0x3072
@scena.Code('func_18_3072')
def func_18_3072():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_30E2',
    )

    ChrTalk(
        0x00FE,
        (
            '#0050250365V#050F你们在这里就表示说\n',
            '要从大使馆开始调查？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050250366V#051F总之就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3196')

    def _loc_30E2(): pass

    label('loc_30E2')

    ChrTalk(
        0x00FE,
        (
            '#0050250367V#052F艾丝蒂尔，怎么了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050250368V#050F我现在正要去\n',
            '公社询问情况。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050250369V你们在这里就表示说\n',
            '要从大使馆开始调查？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050250366V#051F总之就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    def _loc_3196(): pass

    label('loc_3196')

    TalkEnd(0x00FE)

    Return()

# id: 0x0019 offset: 0x319A
@scena.Code('func_19_319A')
def func_19_319A():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_3201',
    )

    ChrTalk(
        0x00FE,
        (
            '#0030250371V#020F你们在这里就表示说\n',
            '要从大使馆开始调查？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030250372V就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_32A6')

    def _loc_3201(): pass

    label('loc_3201')

    ChrTalk(
        0x00FE,
        (
            '#0030250373V#023F咦，怎么了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030250374V#020F我现在正要去\n',
            '公社询问情况。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030250375V你们在这里就表示说\n',
            '要从大使馆开始调查？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030250372V就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_32A6(): pass

    label('loc_32A6')

    TalkEnd(0x00FE)

    Return()

# id: 0x001A offset: 0x32AA
@scena.Code('func_1A_32AA')
def func_1A_32AA():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02D1, 0, 0x1688)),
            Expr.Return,
        ),
        'loc_32E9',
    )

    ChrTalk(
        0x00FE,
        (
            '#0070250385V#560F我们还要在这里\n',
            '买点东西呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_33F3')

    def _loc_32E9(): pass

    label('loc_32E9')

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '#0070250386V#560F啊，姐姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250387V#1000F提妲，小玲就\n',
            '交给你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0070250388V#061F嗯，交给我吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070250389V#560F我有很多地方\n',
            '想和小玲一起去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250390V#1000F这样啊。\n',
            '可别迷路。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0070250391V#061F嗯～\n',
            '姐姐也要努力工作哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1688)

    def _loc_33F3(): pass

    label('loc_33F3')

    TalkEnd(0x00FE)

    Return()

# id: 0x001B offset: 0x33F7
@scena.Code('func_1B_33F7')
def func_1B_33F7():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02D0, 7, 0x1687)),
            Expr.Return,
        ),
        'loc_345E',
    )

    ChrTalk(
        0x00FE,
        (
            '#0220250392V#260F买好东西以后\n',
            '还想去些别的地方。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220250393V我要让提妲带我到处走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3758')

    def _loc_345E(): pass

    label('loc_345E')

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x0101,
        (
            '#0010250394V#1001F小玲，你在这里吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0220250395V#264F啊，姐姐……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220250396V#265F我说，姐姐你\n',
            '喜欢哪个布偶？。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250397V#1011F让我想想，那边的兔子\n',
            '挺可爱的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0220250398V#260F真的？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220250399V#261F真巧，玲也最喜欢\n',
            '那只兔子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250400V#1015F……看到布偶就让人\n',
            '想起亚妮拉丝。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250401V不知道她现在怎么样了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0220250402V#264F亚妮……拉丝？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250403V#1000F她和我同为游击士，\n',
            '是个很喜欢布偶的大姐姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010250404V#1001F一定会和小玲\n',
            '很合得来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0220250405V#264F哦……\n',
            '玲能见到那位姐姐吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250406V#1000F她现在不在王都，\n',
            '不过不久后应该能见到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0220250407V#265F不久是多久？\n',
            '明天？　还是后天？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250408V#1013F这个嘛……\n',
            '我就不知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0220250409V#267F啊？真没劲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1687)

    def _loc_3758(): pass

    label('loc_3758')

    TalkEnd(0x00FE)

    Return()

# id: 0x001C offset: 0x375C
@scena.Code('func_1C_375C')
def func_1C_375C():
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
        'loc_376F',
    )

    Call(0, 0x0021)

    def _loc_376F(): pass

    label('loc_376F')

    ClearChrFlags(0x001A, 0x0080)
    ClearChrFlags(0x001B, 0x0080)
    ClearChrFlags(0x001C, 0x0080)
    SetChrPos(0x001A, 1210, 0, 62900, 266)
    SetChrPos(0x001B, 800, 0, 62000, 270)
    SetChrPos(0x001C, -1180, 0, 62510, 90)
    SetChrPos(0x0101, 200, 0, 54480, 0)
    OP_9F(0x0101, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x00F7, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_6D(-90, -20, 56890, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3830',
    )

    SetChrPos(0x0106, 1160, 0, 54550, 0)

    Jump('loc_3841')

    def _loc_3830(): pass

    label('loc_3830')

    SetChrPos(0x0103, 1160, 0, 54550, 0)

    def _loc_3841(): pass

    label('loc_3841')

    FadeIn(1000, 0)

    @scena.Lambda('lambda_3850')
    def lambda_3850():
        OP_8E(0x0101, 450, 0, 56500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3850)

    @scena.Lambda('lambda_386B')
    def lambda_386B():
        OP_9F(0x0101, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_386B)

    Sleep(300)

    @scena.Lambda('lambda_3882')
    def lambda_3882():
        OP_8E(0x00F7, 1400, 0, 56300, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0000, lambda_3882)

    @scena.Lambda('lambda_389D')
    def lambda_389D():
        OP_9F(0x00F7, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_389D)

    WaitForThreadExit(0x00F7, 0x0000)
    WaitForThreadExit(0x00F7, 0x0001)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010200413V#5P#1004F咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_38DD')
    def lambda_38DD():
        OP_6D(1040, 0, 63300, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_38DD)

    @scena.Lambda('lambda_38F5')
    def lambda_38F5():
        OP_67(0, 6990, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_38F5)

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)

    NpcTalk(
        0x001C,
        '戴眼镜的女性',
        (
            '#0680200414V#6P#1112F这就叫自高自大的\n',
            '帝国贵族……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680200415V臭不可闻也得\n',
            '有个度吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x001B,
        '中年男子',
        (
            '#0670200416V#2P#1101F哼，臭不可闻的\n',
            '是你才对吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670200417V首先，关于提供引擎的问题，\n',
            '共和国凭什么指手画脚的？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670200418V这才是干涉内政吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x001C,
        '戴眼镜的女性',
        (
            '#0680200419V#6P#1111F这关乎国家安全。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680200420V贵国侵略利贝尔到现在\n',
            '还不满１０年吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680200421V#1113F让这种侵略性的国家得到\n',
            '最新技术实在是太不像话了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680200422V即便以利贝尔友邦的立场\n',
            '来看也不能不加以提醒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x001B,
        '中年男子',
        (
            '#0670200423V#2P#1103F什、什么友邦啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670200424V10年前也没有\n',
            '派兵援助他们！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670200425V一区区旁观者，\n',
            '少在旁边摆架子！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x001C,
        '戴眼镜的女性',
        (
            '#0680200426V#6P#1114F你、你说什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x001A, 0x001B, 400)

    ChrTalk(
        0x001A,
        (
            '#0110200427V#272F#5P达维尔大使……\n',
            '就到此为止吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110200428V会给其他旅客添麻烦的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x001B, 0, 400)

    ChrTalk(
        0x001B,
        (
            '#0670200429V#1101F可、可是穆拉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x001A, 266, 400)

    ChrTalk(
        0x001A,
        (
            '#0110200430V#270F#5P爱尔莎大使也请\n',
            '适当控制下自己的情绪吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110200431V关于刚才的问题，我们另找\n',
            '机会在双方的大使馆讨论吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '#0680200432V#6P#1113F……也对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680200433V虽然接受帝国军人的\n',
            '意见并不令人愉快。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0680200434V#1111F不过比自大蛮横、根子腐败不堪的\n',
            '帝国贵族可要好多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x001B, 0x001C, 500)

    ChrTalk(
        0x001B,
        (
            '#0670200435V#1103F#2P你、你说什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '#0680200436V#6P#1113F那么祝你们愉快。\n',
            '各位，我先告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x001C, 180, 400)

    @scena.Lambda('lambda_3DFE')
    def lambda_3DFE():
        OP_8E(0x001C, -800, 0, 54690, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001C, 0x0000, lambda_3DFE)

    @scena.Lambda('lambda_3E19')
    def lambda_3E19():
        OP_6D(670, 0, 59460, 2000)

        ExitThread()

    DispatchAsync(0x001A, 0x0002, lambda_3E19)

    @scena.Lambda('lambda_3E31')
    def lambda_3E31():
        OP_67(0, 6990, -10000, 2000)

        ExitThread()

    DispatchAsync(0x001A, 0x0003, lambda_3E31)

    @scena.Lambda('lambda_3E49')
    def lambda_3E49():
        ChrTurnDirection(0x001B, 0x001C, 0)
        Yield()

        Jump('lambda_3E49')

    DispatchAsync2(0x001B, 0x0001, lambda_3E49)

    @scena.Lambda('lambda_3E5A')
    def lambda_3E5A():
        ChrTurnDirection(0x001A, 0x001C, 0)
        Yield()

        Jump('lambda_3E5A')

    DispatchAsync2(0x001A, 0x0001, lambda_3E5A)

    @scena.Lambda('lambda_3E6B')
    def lambda_3E6B():
        ChrTurnDirection(0x0101, 0x001C, 0)
        Yield()

        Jump('lambda_3E6B')

    DispatchAsync2(0x0101, 0x0002, lambda_3E6B)

    @scena.Lambda('lambda_3E7C')
    def lambda_3E7C():
        ChrTurnDirection(0x00F7, 0x001C, 0)
        Yield()

        Jump('lambda_3E7C')

    DispatchAsync2(0x00F7, 0x0002, lambda_3E7C)

    Sleep(3500)

    @scena.Lambda('lambda_3E92')
    def lambda_3E92():
        OP_9F(0x001C, 0xFF, 0xFF, 0xFF, 0x00, 0x00000190)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_3E92)

    WaitForThreadExit(0x001C, 0x0000)
    WaitForThreadExit(0x001C, 0x0001)
    SetChrFlags(0x001C, 0x0080)
    TerminateThread(0x001A, 0x01)
    TerminateThread(0x001B, 0x01)
    TerminateThread(0x0101, 0x02)
    TerminateThread(0x00F7, 0x02)
    WaitForThreadExit(0x001A, 0x0002)
    WaitForThreadExit(0x001A, 0x0003)
    Sleep(1000)

    ChrTalk(
        0x001B,
        (
            '#0670200437V#1101F#6P怎、怎么有这么没礼貌的女人！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670200438V这就叫毫无历史和传统的\n',
            '平民暴发户……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x001A, 0x001B, 400)

    ChrTalk(
        0x001A,
        (
            '#0110200439V#272F#6P大使……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x001B, 270, 400)
    OP_8C(0x001B, 0, 400)

    ChrTalk(
        0x001B,
        (
            '#0670200440V#1102F#6P……哼，我明白。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0670200441V#1100F我先回大使馆了。\n',
            '关于那件事就交给你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '#0110200442V#270F#6P明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x001B, 400)
    ChrTurnDirection(0x00F7, 0x001B, 400)

    @scena.Lambda('lambda_4009')
    def lambda_4009():
        ChrTurnDirection(0x001A, 0x001B, 0)
        Yield()

        Jump('lambda_4009')

    DispatchAsync2(0x001A, 0x0001, lambda_4009)

    CreateThread(0x001B, 0x01, 0x00, 0x001D)
    Sleep(1000)

    @scena.Lambda('lambda_4026')
    def lambda_4026():
        OP_6D(1830, 0, 62950, 2000)

        ExitThread()

    DispatchAsync(0x001A, 0x0002, lambda_4026)

    @scena.Lambda('lambda_403E')
    def lambda_403E():
        OP_67(0, 6150, -10000, 2000)

        ExitThread()

    DispatchAsync(0x001A, 0x0003, lambda_403E)

    CreateThread(0x0101, 0x01, 0x00, 0x001E)
    Sleep(500)

    CreateThread(0x00F7, 0x01, 0x00, 0x001F)
    WaitForThreadExit(0x00F7, 0x0001)
    TerminateThread(0x001A, 0x01)

    @scena.Lambda('lambda_4072')
    def lambda_4072():
        ChrTurnDirection(0x0101, 0x001A, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4072)

    @scena.Lambda('lambda_4080')
    def lambda_4080():
        ChrTurnDirection(0x00F7, 0x001A, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4080)

    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x001A, 0x0002)
    WaitForThreadExit(0x001A, 0x0003)

    ChrTalk(
        0x0101,
        (
            '#0010200443V#1011F#6P你好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4151',
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
            TXT(0x00, '【◇奥利维尔捕获事件未完成】\n'),
            TXT(0x01, '【◇奥利维尔捕获事件已完成】\n'),
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
        (0x00000000, 'loc_4138'),
        (0x00000001, 'loc_4140'),
        (-1, 'loc_4148'),
    )

    def _loc_4138(): pass

    label('loc_4138')

    OP_28(0x0055, 0x03, 0x10)

    Jump('loc_4148')

    def _loc_4140(): pass

    label('loc_4140')

    OP_28(0x0055, 0x04, 0x10)

    Jump('loc_4148')

    def _loc_4148(): pass

    label('loc_4148')

    FadeIn(300, 0)

    def _loc_4151(): pass

    label('loc_4151')

    OP_62(0x001A, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    If(
        (
            (Expr.Eval, "OP_29(0x0055, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_41E4',
    )

    ChrTalk(
        0x001A,
        (
            '#0110200444V#273F#5P你是……\n',
            '我记得你叫艾丝蒂尔吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110200445V#277F好久不见。\n',
            '自从武术大会之后。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4263')

    def _loc_41E4(): pass

    label('loc_41E4')

    ChrTalk(
        0x001A,
        (
            '#0110200444V#273F#5P你是……\n',
            '我记得你叫艾丝蒂尔吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110200447V#277F好久不见。\n',
            '自从诞辰庆典麻烦你帮忙之后就一直没见过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4263(): pass

    label('loc_4263')

    ChrTalk(
        0x0101,
        (
            '#0010200448V#1016F#6P太好了。\n',
            '你还记得我。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200449V#1011F不过话说回来……\n',
            '刚才的争论真激烈。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200450V他们是什么人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '#0110200451V#277F#5P那位男子是\n',
            '埃雷波尼亚帝国的达维尔大使。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110200452V那位女性是\n',
            '卡尔瓦德共和国的爱尔莎大使。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110200453V双方都是各自国家在王都\n',
            '大使馆的负责人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200454V#1004F#6P这、这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_445A',
    )

    ChrTalk(
        0x0106,
        (
            '#0050200455V#551F#4P不过两位大使级人物的\n',
            '争论倒像是小孩子在吵架。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200456V这就是大使的工作作风？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200457V#1019F#6P等、等等，阿加特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_44DA')

    def _loc_445A(): pass

    label('loc_445A')

    ChrTalk(
        0x0103,
        (
            '#0030200458V#027F#4P哼，那就是大使啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200459V都用那种粗野的方式\n',
            '来进行外交？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200460V#1019F#6P雪、雪拉姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_44DA(): pass

    label('loc_44DA')

    ChrTalk(
        0x001A,
        (
            '#0110200461V#276F#5P唉，真不好意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110200462V#272F本来帝国和共和国\n',
            '的关系就不甚友好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110200463V而且那两个人在性格上\n',
            '也完全合不上拍。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110200464V#277F不过每次见面\n',
            '都要吵架，说不定也反证了\n',
            '他们其实很合得来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200465V#1016F#6P哈哈，可能也有点道理。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200466V#1015F不过……\n',
            '他们说的话挺令人在意的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200467V提供引擎和内政干涉什么的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '#0110200468V#270F#5P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200469V#1025F#6P啊，我是不是不该问的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '#0110200470V#272F#5P……不，没关系。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110200471V#277F引擎指的是中央工房现在\n',
            '正在开发的最新型号。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110200472V利贝尔有意在完成后\n',
            '将样品提供给\n',
            '帝国和共和国双方……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110200473V我们来协商这件事，\n',
            '就正好巧遇爱尔莎大使。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200474V#1000F#6P哦，原来如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200475V#1015F不过为了一个新型引擎\n',
            '有什么好吵的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_4874',
    )

    ChrTalk(
        0x0106,
        (
            '#0050200476V#555F#4P那可是左右飞船性能的\n',
            '最重要的零件。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200477V想想军舰搭载它之后会变得怎样，\n',
            '就知道这不是什么小事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4903')

    def _loc_4874(): pass

    label('loc_4874')

    ChrTalk(
        0x0103,
        (
            '#0030200478V#026F#4P导力引擎的性能\n',
            '可以直接左右飞船的性能。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200479V#020F想想军舰搭载它之后会变得怎样，\n',
            '就知道这里面牵扯得有多深了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4903(): pass

    label('loc_4903')

    ChrTalk(
        0x0101,
        (
            '#0010200480V#1002F#6P原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200481V#1007F确实，如果帝国军因此\n',
            '提升了战力，\n',
            '可就不好办了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200482V#1008F……啊，不好意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '#0110200483V#272F#5P不，你说得没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110200484V#277F通常来说，向别国提供最新技术\n',
            '是无法想象的，\n',
            '不过这也是女王陛下的想法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110200485V并不独占技术的高峰，\n',
            '而是通过向各国提供技术\n',
            '来确保各国间的和平……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110200486V这是她老人家的想法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200487V#1011F#6P原来如此……\n',
            '这听起来确实像是陛下说的话。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200488V#1001F唔～从这一点上来看\n',
            '女王陛下果然了不起。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200489V感觉这已经不是一种单纯的理想，\n',
            '而是有深谋远虑的\n',
            '外交政策了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '#0110200490V#272F#5P嗯，利贝尔的国民应该\n',
            '好好地以陛下为荣。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110200491V#277F……抱歉。\n',
            '有点谈得忘乎所以了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110200492V你们要买票吧？\n',
            '我就先告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200493V#1004F#6P啊，嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200494V#1015F对了，穆拉先生，\n',
            '奥利维尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200495V他已经回\n',
            '埃雷波尼亚了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '#0110200496V#273F#5P怎么？你不知道？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200497V#1007F#6P自从诞辰庆典之后\n',
            '一直没机会跟他打招呼。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200498V让我觉得有点抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '#0110200499V#277F#5P不用担心，\n',
            '那个轻佻的大赖皮蛋还留在利贝尔的境内。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110200500V说什么要『优雅地\n',
            '逗留在亚尔摩温泉』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_4DDB',
    )

    ChrTalk(
        0x0101,
        (
            '#0010200501V#1008F#6P噢，是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200502V#1012F呵呵……\n',
            '真像是奥利维尔的风格。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4E3B')

    def _loc_4DDB(): pass

    label('loc_4DDB')

    ChrTalk(
        0x0101,
        (
            '#0010200503V#1008F#6P哦，是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030200504V#027F#4P呵呵……\n',
            '像是奥利维尔的风格。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4E3B(): pass

    label('loc_4E3B')

    ChrTalk(
        0x001A,
        (
            '#0110200505V#277F#5P等那家伙回了大使馆，\n',
            '我就把你们的事告诉他。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110200506V至少让他在回国前\n',
            '联络一下协会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200507V#1017F#6P谢谢你，穆拉先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_4F06',
    )

    ChrTalk(
        0x0103,
        (
            '#0030200508V#021F#4P拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4F06')

    def _loc_4F06(): pass

    label('loc_4F06')

    ChrTalk(
        0x001A,
        (
            '#0110200509V#277F#5P我才要谢谢你们愿意\n',
            '陪着那个怪人呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110200510V那么就此别过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4F65')
    def lambda_4F65():
        OP_6D(670, 0, 59460, 2500)

        ExitThread()

    DispatchAsync(0x00F7, 0x0002, lambda_4F65)

    @scena.Lambda('lambda_4F7D')
    def lambda_4F7D():
        OP_67(0, 6990, -10000, 2500)

        ExitThread()

    DispatchAsync(0x00F7, 0x0003, lambda_4F7D)

    @scena.Lambda('lambda_4F95')
    def lambda_4F95():
        OP_8E(0x001A, -940, 0, 61300, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_4F95)

    @scena.Lambda('lambda_4FB0')
    def lambda_4FB0():
        ChrTurnDirection(0x0101, 0x001A, 0)
        Yield()

        Jump('lambda_4FB0')

    DispatchAsync2(0x0101, 0x0001, lambda_4FB0)

    @scena.Lambda('lambda_4FC1')
    def lambda_4FC1():
        ChrTurnDirection(0x00F7, 0x001A, 0)
        Yield()

        Jump('lambda_4FC1')

    DispatchAsync2(0x00F7, 0x0001, lambda_4FC1)

    WaitForThreadExit(0x001A, 0x0001)

    @scena.Lambda('lambda_4FD7')
    def lambda_4FD7():
        OP_8E(0x001A, -840, 0, 54500, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_4FD7)

    Sleep(1900)

    @scena.Lambda('lambda_4FF7')
    def lambda_4FF7():
        OP_9F(0x001A, 0xFF, 0xFF, 0xFF, 0x00, 0x00000190)

        ExitThread()

    DispatchAsync(0x001A, 0x0002, lambda_4FF7)

    Sleep(400)

    WaitForThreadExit(0x001A, 0x0001)
    SetChrFlags(0x001A, 0x0080)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x00F7, 0x01)
    WaitForThreadExit(0x00F7, 0x0002)
    WaitForThreadExit(0x00F7, 0x0003)

    @scena.Lambda('lambda_502A')
    def lambda_502A():
        OP_6D(1360, 0, 61620, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_502A)

    @scena.Lambda('lambda_5042')
    def lambda_5042():
        OP_67(0, 6990, -10000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5042)

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_5393',
    )

    OP_8C(0x0106, 280, 500)

    ChrTalk(
        0x0106,
        (
            '#0050200511V#555F#2P想不到这么一个严肃的军人\n',
            '会是那个金发男人的朋友。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200512V他是什么角色？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200513V#1006F#5P他是穆拉先生，\n',
            '帝国大使馆的常驻士官。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200514V不过我们也\n',
            '只见过一两次。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050200515V#552F#2P哦……\n',
            '言行得体又无懈可击。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200516V可以说是头藏起了\n',
            '獠牙的军用犬。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200517V#1007F#5P真是的，你真没礼貌。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200518V#1015F不过确实……\n',
            '给人的感觉是他很强。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050200519V#057F#2P哼，帝国的人都不可信赖，\n',
            '那个金发男人也一样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200520V好像和卡西乌斯大叔\n',
            '私下说过什么话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200521V也不知道他长居此地\n',
            '有什么目的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200522V#1015F#5P嗯～好像也有点道理。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200523V#1011F奥利维尔虽然有点怪，\n',
            '但不是个坏人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200524V穆拉先生看上去也\n',
            '不像是坏人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050200525V#053F#2P哼，天知道。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200526V#050F算了，我们赶紧去\n',
            '柜台买票吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5747')

    def _loc_5393(): pass

    label('loc_5393')

    OP_8C(0x0103, 280, 500)

    ChrTalk(
        0x0103,
        (
            '#0030200527V#021F#2P呵呵，想不到这么一个严肃的军人\n',
            '会是那个奥利维尔的朋友。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200528V#020F看上去是个帝国军人，\n',
            '他是什么角色？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200513V#1006F#5P他是穆拉先生，\n',
            '帝国大使馆的常驻士官。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200514V不过我们也\n',
            '只见过一两次。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030200531V#027F#2P哦～这么年轻就\n',
            '一脸沧桑了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200532V#021F真想有机会和他喝一杯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200533V#1007F#5P真是的，你那副表情好像\n',
            '在说我会丢利贝尔的脸一样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200534V#1011F对了，雪拉姐\n',
            '后来有没有见过奥利维尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030200535V#020F#2P嗯，在王都见了几次。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200536V其实他还约我去温泉呢，\n',
            '被我严肃地拒绝了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200537V#1004F#5P哎哎！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200538V#1013F就是说……\n',
            '是……是那种意思？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030200539V#027F#2P呵呵，天知道。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200540V#021F不过我最近一个月也很忙，\n',
            '根本没那个空闲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200541V要在平时的话，我就会让他负责\n',
            '全部住宿费然后拉他陪我喝酒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200542V#1016F#5P哈…哈…\n',
            '从某种意义上说，奥利维尔也真不幸。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200543V#1006F不说这些了。\n',
            '我们先去\n',
            '买票吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5747(): pass

    label('loc_5747')

    OP_A2(0x1203)
    EventEnd(0x00)

    Return()

# id: 0x001D offset: 0x574D
@scena.Code('func_1D_574D')
def func_1D_574D():
    OP_8E(0x00FE, -750, 0, 60220, 2000, 0x00)

    @scena.Lambda('lambda_5767')
    def lambda_5767():
        OP_8E(0x00FE, -670, 0, 54650, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0003, lambda_5767)

    Sleep(2500)

    @scena.Lambda('lambda_5787')
    def lambda_5787():
        OP_9F(0x001B, 0xFF, 0xFF, 0xFF, 0x00, 0x00000190)

        ExitThread()

    DispatchAsync(0x001B, 0x0002, lambda_5787)

    Sleep(400)

    WaitForThreadExit(0x001B, 0x0003)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x001E offset: 0x57A3
@scena.Code('func_1E_57A3')
def func_1E_57A3():
    OP_8E(0x0101, 570, 0, 61190, 2000, 0x00)

    Return()

# id: 0x001F offset: 0x57B8
@scena.Code('func_1F_57B8')
def func_1F_57B8():
    OP_8E(0x00F7, 1500, 0, 60720, 2000, 0x00)

    Return()

# id: 0x0020 offset: 0x57CD
@scena.Code('func_20_57CD')
def func_20_57CD():
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
        'loc_57E4',
    )

    Call(0, 0x0021)
    Call(0, 0x0022)

    def _loc_57E4(): pass

    label('loc_57E4')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_57FC'),
        (0x00000065, 'loc_5880'),
        (0x00000066, 'loc_5904'),
        (0x00000067, 'loc_5988'),
        (-1, 'loc_5A0C'),
    )

    def _loc_57FC(): pass

    label('loc_57FC')

    SetChrPos(0x0101, -9240, 0, 440, 90)
    SetChrPos(0x0107, -9330, 0, -480, 90)
    SetChrPos(0x00F7, -10150, 0, -550, 90)
    SetChrPos(0x00F9, -10150, 0, 520, 90)
    OP_6D(-9640, 0, 0, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    Jump('loc_5A0C')

    def _loc_5880(): pass

    label('loc_5880')

    SetChrPos(0x0101, 440, 0, 6410, 180)
    SetChrPos(0x0107, -480, 0, 6500, 180)
    SetChrPos(0x00F7, 550, 0, 7320, 180)
    SetChrPos(0x00F9, -520, 0, 7320, 180)
    OP_6D(0, 0, 6810, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    Jump('loc_5A0C')

    def _loc_5904(): pass

    label('loc_5904')

    SetChrPos(0x0101, 8570, 0, -480, 270)
    SetChrPos(0x0107, 8660, 0, 440, 270)
    SetChrPos(0x00F7, 9480, 0, 550, 270)
    SetChrPos(0x00F9, 9480, 0, -520, 270)
    OP_6D(8970, 0, 0, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    Jump('loc_5A0C')

    def _loc_5988(): pass

    label('loc_5988')

    SetChrPos(0x0101, -480, 0, -7240, 0)
    SetChrPos(0x0107, 440, 0, -7330, 0)
    SetChrPos(0x00F7, -520, 0, -8150, 0)
    SetChrPos(0x00F9, 550, 0, -8150, 0)
    OP_6D(0, 0, -7640, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    Jump('loc_5A0C')

    def _loc_5A0C(): pass

    label('loc_5A0C')

    SetChrFlags(0x0012, 0x0080)
    FadeIn(1000, 0)
    OP_0D()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010260612V#1004F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x001D, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_5A72'),
        (0x00000065, 'loc_5AFF'),
        (0x00000066, 'loc_5B81'),
        (0x00000067, 'loc_5C2F'),
        (-1, 'loc_5CBC'),
    )

    def _loc_5A72(): pass

    label('loc_5A72')

    SetChrPos(0x001D, 4530, 0, -10, 90)

    @scena.Lambda('lambda_5A89')
    def lambda_5A89():
        OP_6D(9530, 0, 0, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5A89)

    OP_8E(0x001D, 9530, 0, -10, 2000, 0x00)
    OP_72(0x0001, 0x0010)
    OP_6F(0x0001, 0)
    OP_70(0x0001, 0x0000003B)
    Sleep(1000)

    OP_8E(0x001D, 12490, 0, 0, 2000, 0x00)
    Sleep(500)

    SetChrFlags(0x001D, 0x0080)
    Fade(500)
    OP_6D(-9640, 0, 0, 0)
    OP_0D()

    Jump('loc_5CBC')

    def _loc_5AFF(): pass

    label('loc_5AFF')

    SetChrPos(0x001D, 0, 0, -3700, 180)

    @scena.Lambda('lambda_5B16')
    def lambda_5B16():
        OP_6D(0, 0, -8200, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5B16)

    OP_8E(0x001D, 0, 0, -9500, 2000, 0x00)

    @scena.Lambda('lambda_5B42')
    def lambda_5B42():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000190)

        ExitThread()

    DispatchAsync(0x001D, 0x0002, lambda_5B42)

    OP_8E(0x001D, 0, 0, -10500, 2000, 0x00)
    SetChrFlags(0x001D, 0x0080)
    Fade(1000)
    OP_6D(0, 0, 6810, 0)
    OP_0D()

    Jump('loc_5CBC')

    def _loc_5B81(): pass

    label('loc_5B81')

    SetChrPos(0x001D, -5200, 0, 0, 90)

    @scena.Lambda('lambda_5B98')
    def lambda_5B98():
        OP_6D(-10200, 0, 0, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5B98)

    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_8E(0x001D, -11490, 0, 0, 2000, 0x00)

    @scena.Lambda('lambda_5BF0')
    def lambda_5BF0():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000190)

        ExitThread()

    DispatchAsync(0x001D, 0x0002, lambda_5BF0)

    OP_8E(0x001D, -12490, 0, 0, 2000, 0x00)
    SetChrFlags(0x001D, 0x0080)
    Fade(1000)
    OP_6D(8970, 0, 0, 0)
    OP_0D()

    Jump('loc_5CBC')

    def _loc_5C2F(): pass

    label('loc_5C2F')

    SetChrPos(0x001D, 0, 0, 2870, 0)

    @scena.Lambda('lambda_5C46')
    def lambda_5C46():
        OP_6D(0, 0, 7370, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5C46)

    OP_8E(0x001D, 0, 0, 7370, 2000, 0x00)
    Sleep(500)

    OP_72(0x0000, 0x0010)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 0x0000003B)
    Sleep(1000)

    OP_8E(0x001D, 0, 0, 10490, 2000, 0x00)
    SetChrFlags(0x001D, 0x0080)
    Fade(1000)
    OP_6D(0, 0, -7640, 0)
    OP_0D()

    Jump('loc_5CBC')

    def _loc_5CBC(): pass

    label('loc_5CBC')

    Sleep(200)

    ChrTalk(
        0x0101,
        (
            '#0010260613V#1006F哟，在那儿！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070260614V#065F得、得赶紧追。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_5D22'),
        (0x00000065, 'loc_5DD3'),
        (0x00000066, 'loc_5E84'),
        (0x00000067, 'loc_5F35'),
        (-1, 'loc_5FE6'),
    )

    def _loc_5D22(): pass

    label('loc_5D22')

    @scena.Lambda('lambda_5D28')
    def lambda_5D28():
        OP_6D(-150, 0, -180, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_5D28)

    @scena.Lambda('lambda_5D40')
    def lambda_5D40():
        OP_90(0x00FE, 10000, 0, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5D40)

    @scena.Lambda('lambda_5D5B')
    def lambda_5D5B():
        OP_90(0x00FE, 10000, 0, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_5D5B)

    Sleep(100)

    @scena.Lambda('lambda_5D7B')
    def lambda_5D7B():
        OP_90(0x00FE, 10000, 0, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_5D7B)

    @scena.Lambda('lambda_5D96')
    def lambda_5D96():
        OP_90(0x00FE, 10000, 0, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_5D96)

    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(500)

    TerminateThread(0x0101, 0x00)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/T4101._SN', 106, 0, 0)
    IdleLoop()

    Jump('loc_5FE6')

    def _loc_5DD3(): pass

    label('loc_5DD3')

    @scena.Lambda('lambda_5DD9')
    def lambda_5DD9():
        OP_6D(-150, 0, -180, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_5DD9)

    @scena.Lambda('lambda_5DF1')
    def lambda_5DF1():
        OP_90(0x00FE, 0, 0, -10000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5DF1)

    @scena.Lambda('lambda_5E0C')
    def lambda_5E0C():
        OP_90(0x00FE, 0, 0, -10000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_5E0C)

    Sleep(100)

    @scena.Lambda('lambda_5E2C')
    def lambda_5E2C():
        OP_90(0x00FE, 0, 0, -10000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_5E2C)

    @scena.Lambda('lambda_5E47')
    def lambda_5E47():
        OP_90(0x00FE, 0, 0, -10000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_5E47)

    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(500)

    TerminateThread(0x0101, 0x00)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/T4101._SN', 107, 0, 0)
    IdleLoop()

    Jump('loc_5FE6')

    def _loc_5E84(): pass

    label('loc_5E84')

    @scena.Lambda('lambda_5E8A')
    def lambda_5E8A():
        OP_6D(-150, 0, -180, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_5E8A)

    @scena.Lambda('lambda_5EA2')
    def lambda_5EA2():
        OP_90(0x00FE, -10000, 0, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5EA2)

    @scena.Lambda('lambda_5EBD')
    def lambda_5EBD():
        OP_90(0x00FE, -10000, 0, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_5EBD)

    Sleep(100)

    @scena.Lambda('lambda_5EDD')
    def lambda_5EDD():
        OP_90(0x00FE, -10000, 0, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_5EDD)

    @scena.Lambda('lambda_5EF8')
    def lambda_5EF8():
        OP_90(0x00FE, -10000, 0, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_5EF8)

    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(500)

    TerminateThread(0x0101, 0x00)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/T4101._SN', 108, 0, 0)
    IdleLoop()

    Jump('loc_5FE6')

    def _loc_5F35(): pass

    label('loc_5F35')

    @scena.Lambda('lambda_5F3B')
    def lambda_5F3B():
        OP_6D(-150, 0, -180, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_5F3B)

    @scena.Lambda('lambda_5F53')
    def lambda_5F53():
        OP_90(0x00FE, 0, 0, 10000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5F53)

    @scena.Lambda('lambda_5F6E')
    def lambda_5F6E():
        OP_90(0x00FE, 0, 0, 10000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_5F6E)

    Sleep(100)

    @scena.Lambda('lambda_5F8E')
    def lambda_5F8E():
        OP_90(0x00FE, 0, 0, 10000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_5F8E)

    @scena.Lambda('lambda_5FA9')
    def lambda_5FA9():
        OP_90(0x00FE, 0, 0, 10000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_5FA9)

    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(500)

    TerminateThread(0x0101, 0x00)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/T4101._SN', 105, 0, 0)
    IdleLoop()

    Jump('loc_5FE6')

    def _loc_5FE6(): pass

    label('loc_5FE6')

    Return()

# id: 0x0021 offset: 0x5FE7
@scena.Code('func_21_5FE7')
def func_21_5FE7():
    FadeOut(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x09, 0xFF)

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
        (0x00000000, 'loc_6064'),
        (0x00000001, 'loc_606A'),
        (-1, 'loc_6070'),
    )

    def _loc_6064(): pass

    label('loc_6064')

    OP_A2(0x1200)

    Jump('loc_6070')

    def _loc_606A(): pass

    label('loc_606A')

    OP_A2(0x1201)

    Jump('loc_6070')

    def _loc_6070(): pass

    label('loc_6070')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_607E',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_6082')

    def _loc_607E(): pass

    label('loc_607E')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_6082(): pass

    label('loc_6082')

    Return()

# id: 0x0022 offset: 0x6083
@scena.Code('func_22_6083')
def func_22_6083():
    ClearMapFlags(0x00000001)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_60C2',
    )

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            0x0000,
            0x0002,
            0x0006,
            0x00FF,
        ),
        (
            0x0004,
            0x0007,
            0xFFFF,
        ),
    )

    Jump('loc_60DC')

    def _loc_60C2(): pass

    label('loc_60C2')

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            0x0000,
            0x0005,
            0x0006,
            0x00FF,
        ),
        (
            0x0004,
            0x0007,
            0xFFFF,
        ),
    )

    def _loc_60DC(): pass

    label('loc_60DC')

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

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0121_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0121   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '爱娜'),
    TXT(0x02, '雪拉扎德'),
    TXT(0x03, '阿加特'),
    TXT(0x04, '奥利维尔'),
    TXT(0x05, '科洛丝'),
    TXT(0x06, '提妲'),
    TXT(0x07, '金'),
    TXT(0x08, '克劳斯市长'),
    TXT(0x09, '里农'),
    TXT(0x0A, '利吉'),
    TXT(0x0B, '布露姆老奶奶'),
    TXT(0x0C, '基蒂'),
    TXT(0x0D, '菲特 '),
    TXT(0x0E, '加通老大'),
    TXT(0x0F, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0121.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT21/T0121._SN', 'ED6_DT21/T0121_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xC2A2
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
        ('ED6_DT07/CH02560._CH', 'ED6_DT07/CH02560P._CP'),
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT07/CH00050._CH', 'ED6_DT07/CH00050P._CP'),
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT07/CH00040._CH', 'ED6_DT07/CH00040P._CP'),
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP'),
        ('ED6_DT07/CH00023._CH', 'ED6_DT07/CH00023P._CP'),
        ('ED6_DT07/CH00053._CH', 'ED6_DT07/CH00053P._CP'),
        ('ED6_DT07/CH00033._CH', 'ED6_DT07/CH00033P._CP'),
        ('ED6_DT07/CH00073._CH', 'ED6_DT07/CH00073P._CP'),
        ('ED6_DT07/CH02350._CH', 'ED6_DT07/CH02350P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01760._CH', 'ED6_DT07/CH01760P._CP'),
        ('ED6_DT07/CH01010._CH', 'ED6_DT07/CH01010P._CP'),
        ('ED6_DT26/CH20241._CH', 'ED6_DT26/CH20241P._CP'),
        ('ED6_DT07/CH01770._CH', 'ED6_DT07/CH01770P._CP'),
        ('ED6_DT26/CH20311._CH', 'ED6_DT26/CH20311P._CP'),
        ('ED6_DT06/CH20049._CH', 'ED6_DT06/CH20049P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01530._CH', 'ED6_DT07/CH01530P._CP'),
    ]

# id: 0x10002 offset: 0x152
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 750,
            z                   = 0,
            y                   = 118600,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
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
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
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
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
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
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
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
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 3800,
            z                   = 0,
            y                   = 2000,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = -355,
            z                   = 0,
            y                   = 71450,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = 47500,
            z                   = 0,
            y                   = -1110,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = 46300,
            z                   = 0,
            y                   = -1110,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = 2110,
            z                   = 0,
            y                   = -1700,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x312
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x312
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 2380,
            y           = 0,
            z           = 109620,
            range       = 5580,
            dword_10    = 0x000007D0,
            dword_14    = 0x0001B0E4,
            dword_18    = 0x00010000,
            dword_1C    = 0x0000000C,
        ),
    )

# id: 0x10005 offset: 0x332
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 1271,
            triggerZ            = 0,
            triggerY            = 116402,
            triggerRange        = 800,
            actorX              = 750,
            actorZ              = 1500,
            actorY              = 118600,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 3810,
            triggerZ            = 0,
            triggerY            = 1080,
            triggerRange        = 800,
            actorX              = 3800,
            actorZ              = 1500,
            actorY              = 2000,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 4900,
            triggerZ            = 0,
            triggerY            = 112600,
            triggerRange        = 1400,
            actorX              = 4900,
            actorZ              = 2000,
            actorY              = 112600,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0000,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x39E
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_3F6',
    )

    SetChrFlags(0x0011, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3CD',
    )

    SetChrPos(0x0013, 6360, 0, -930, 90)
    CreateThread(0x0013, 0x00, 0x00, 0x0003)

    Jump('loc_3F3')

    def _loc_3CD(): pass

    label('loc_3CD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 6, 0x2086)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3E2',
    )

    SetChrFlags(0x0012, 0x0080)
    SetChrFlags(0x0013, 0x0080)

    Jump('loc_3F3')

    def _loc_3E2(): pass

    label('loc_3E2')

    SetChrPos(0x0013, 44360, 0, -2420, 270)

    def _loc_3F3(): pass

    label('loc_3F3')

    Jump('loc_4D4')

    def _loc_3F6(): pass

    label('loc_3F6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_441',
    )

    SetChrPos(0x0011, 4300, 0, 114900, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_426',
    )

    SetChrPos(0x0012, 44800, 0, 2410, 180)

    def _loc_426(): pass

    label('loc_426')

    SetChrPos(0x0013, 6360, 0, -930, 90)
    CreateThread(0x0013, 0x00, 0x00, 0x0003)

    Jump('loc_4D4')

    def _loc_441(): pass

    label('loc_441')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 3, 0x1823)),
            Expr.Return,
        ),
        'loc_474',
    )

    SetChrPos(0x0011, -1050, 0, 67400, 180)
    SetChrPos(0x0013, 6360, 0, -930, 90)
    CreateThread(0x0013, 0x00, 0x00, 0x0003)

    Jump('loc_4D4')

    def _loc_474(): pass

    label('loc_474')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_49B',
    )

    SetChrFlags(0x0011, 0x0080)
    SetChrPos(0x0013, 6360, 0, -930, 90)
    CreateThread(0x0013, 0x00, 0x00, 0x0003)

    Jump('loc_4D4')

    def _loc_49B(): pass

    label('loc_49B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_4AF',
    )

    SetChrFlags(0x0011, 0x0080)
    SetChrFlags(0x0013, 0x0080)

    Jump('loc_4D4')

    def _loc_4AF(): pass

    label('loc_4AF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_4CF',
    )

    SetChrFlags(0x0011, 0x0080)
    SetChrPos(0x0012, 47500, 0, -1110, 270)

    Jump('loc_4D4')

    def _loc_4CF(): pass

    label('loc_4CF')

    SetChrFlags(0x0013, 0x0080)

    def _loc_4D4(): pass

    label('loc_4D4')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x6A),
            Expr.Equ,
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x68),
            Expr.Equ,
            Expr.Or,
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x6),
            Expr.Lss,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 6, 0x181E)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 3, 0x1823)),
            Expr.Or,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5E8',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_52C',
    )

    ClearChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000A, 0x0004)
    SetChrChipByIndex(0x000A, 8)
    SetChrPos(0x000A, -790, 200, 69820, 360)

    def _loc_52C(): pass

    label('loc_52C')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_575',
    )

    ClearChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000B, 0x0004)

    If(
        (
            (Expr.Eval, "OP_29(0x0076, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_55F',
    )

    SetChrFlags(0x000B, 0x0002)
    SetChrSubChip(0x000B, 0)
    SetChrChipByIndex(0x000B, 18)

    Jump('loc_564')

    def _loc_55F(): pass

    label('loc_55F')

    SetChrChipByIndex(0x000B, 9)

    def _loc_564(): pass

    label('loc_564')

    SetChrPos(0x000B, 1060, 200, 69820, 360)

    def _loc_575(): pass

    label('loc_575')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_598',
    )

    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x000C, -1940, 0, 74490, 360)

    def _loc_598(): pass

    label('loc_598')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5BB',
    )

    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, -4290, 0, 73800, 360)

    def _loc_5BB(): pass

    label('loc_5BB')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5E8',
    )

    ClearChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000E, 0x0004)
    SetChrChipByIndex(0x000E, 10)
    SetChrPos(0x000E, 140, 200, 71510, 180)

    def _loc_5E8(): pass

    label('loc_5E8')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6A7',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_62A',
    )

    ClearChrFlags(0x0009, 0x0080)
    SetChrFlags(0x0009, 0x0004)
    SetChrChipByIndex(0x0009, 7)
    SetChrPos(0x0009, 1060, 200, 69820, 360)

    def _loc_62A(): pass

    label('loc_62A')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_657',
    )

    ClearChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000A, 0x0004)
    SetChrChipByIndex(0x000A, 8)
    SetChrPos(0x000A, -790, 200, 69820, 360)

    def _loc_657(): pass

    label('loc_657')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_67A',
    )

    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, -4290, 0, 73800, 360)

    def _loc_67A(): pass

    label('loc_67A')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_6A7',
    )

    ClearChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000E, 0x0004)
    SetChrChipByIndex(0x000E, 10)
    SetChrPos(0x000E, 140, 200, 71510, 180)

    def _loc_6A7(): pass

    label('loc_6A7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_6C6',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x21),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMapFlags(0x10000000)
    OP_A3(0x10F0)
    Event(1, 0x0004)

    Jump('loc_77B')

    def _loc_6C6(): pass

    label('loc_6C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_6DC',
    )

    SetMapFlags(0x10000000)
    OP_A3(0x10F1)
    Event(1, 0x0005)

    Jump('loc_77B')

    def _loc_6DC(): pass

    label('loc_6DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Return,
        ),
        'loc_6F2',
    )

    SetMapFlags(0x10000000)
    OP_A3(0x10F2)
    Event(0, 0x0024)

    Jump('loc_77B')

    def _loc_6F2(): pass

    label('loc_6F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 3, 0x10F3)),
            Expr.Return,
        ),
        'loc_708',
    )

    SetMapFlags(0x10000000)
    OP_A3(0x10F3)
    Event(1, 0x0003)

    Jump('loc_77B')

    def _loc_708(): pass

    label('loc_708')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 4, 0x10F4)),
            Expr.Return,
        ),
        'loc_71E',
    )

    SetMapFlags(0x10000000)
    OP_A3(0x10F4)
    Event(1, 0x0012)

    Jump('loc_77B')

    def _loc_71E(): pass

    label('loc_71E')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000067, 'loc_72A'),
        (-1, 'loc_77B'),
    )

    def _loc_72A(): pass

    label('loc_72A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 3, 0x2003)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_742',
    )

    SetMapFlags(0x10000000)
    Event(1, 0x0007)

    Jump('loc_778')

    def _loc_742(): pass

    label('loc_742')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 6, 0x181E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_75A',
    )

    SetMapFlags(0x10000000)
    Event(0, 0x0015)

    Jump('loc_778')

    def _loc_75A(): pass

    label('loc_75A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 3, 0x1823)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_778',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMapFlags(0x10000000)
    Event(0, 0x001E)

    def _loc_778(): pass

    label('loc_778')

    Jump('loc_77B')

    def _loc_77B(): pass

    label('loc_77B')

    Return()

# id: 0x0001 offset: 0x77C
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 5, 0x180D)),
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 6, 0x180E)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 7, 0x180F)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 0, 0x1810)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7A0',
    )

    OP_B1('t0121_y')

    Jump('loc_7A9')

    def _loc_7A0(): pass

    label('loc_7A0')

    OP_B1('t0121_n')

    def _loc_7A9(): pass

    label('loc_7A9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0308, 3, 0x1843)),
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7C2',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_7C2(): pass

    label('loc_7C2')

    Return()

# id: 0x0002 offset: 0x7C3
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
        'loc_7E8',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_92A')

    def _loc_7E8(): pass

    label('loc_7E8')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_801',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000640)

    Jump('loc_92A')

    def _loc_801(): pass

    label('loc_801')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_81A',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x0000060E)

    Jump('loc_92A')

    def _loc_81A(): pass

    label('loc_81A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_833',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005DC)

    Jump('loc_92A')

    def _loc_833(): pass

    label('loc_833')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_84C',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AA)

    Jump('loc_92A')

    def _loc_84C(): pass

    label('loc_84C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_865',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x00000578)

    Jump('loc_92A')

    def _loc_865(): pass

    label('loc_865')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_87E',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x00000546)

    Jump('loc_92A')

    def _loc_87E(): pass

    label('loc_87E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_897',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000677)

    Jump('loc_92A')

    def _loc_897(): pass

    label('loc_897')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8B0',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000645)

    Jump('loc_92A')

    def _loc_8B0(): pass

    label('loc_8B0')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8C9',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x00000613)

    Jump('loc_92A')

    def _loc_8C9(): pass

    label('loc_8C9')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8E2',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005E1)

    Jump('loc_92A')

    def _loc_8E2(): pass

    label('loc_8E2')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8FB',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AF)

    Jump('loc_92A')

    def _loc_8FB(): pass

    label('loc_8FB')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_914',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x0000057D)

    Jump('loc_92A')

    def _loc_914(): pass

    label('loc_914')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_92A',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x0000054B)

    def _loc_92A(): pass

    label('loc_92A')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_93F',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_92A')

    def _loc_93F(): pass

    label('loc_93F')

    Return()

# id: 0x0003 offset: 0x940
@scena.Code('func_03_940')
def func_03_940():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_9C0',
    )

    OP_8E(0x00FE, 6360, 0, -930, 2000, 0x00)
    OP_8C(0x00FE, 90, 400)
    Sleep(3000)

    OP_8E(0x00FE, 6360, 0, -2400, 2000, 0x00)
    OP_8C(0x00FE, 90, 400)
    Sleep(3000)

    OP_8E(0x00FE, 5680, 0, -3720, 2000, 0x00)
    OP_8E(0x00FE, 5910, 0, -4780, 2000, 0x00)
    OP_8C(0x00FE, 135, 400)
    Sleep(3000)

    Jump('func_03_940')

    def _loc_9C0(): pass

    label('loc_9C0')

    Return()

# id: 0x0004 offset: 0x9C1
@scena.Code('func_04_9C1')
def func_04_9C1():
    Call(0, 0x0006)

    Return()

# id: 0x0005 offset: 0x9C6
@scena.Code('func_05_9C6')
def func_05_9C6():
    Call(0, 0x0007)

    Return()

# id: 0x0006 offset: 0x9CB
@scena.Code('func_06_9CB')
def func_06_9CB():
    TalkBegin(0x0008)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C88',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_A3E',
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
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '报告\n'),
            TXT(0x02, '呼叫同伴\n'),
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

    Jump('loc_A42')

    def _loc_A3E(): pass

    label('loc_A3E')

    Call(6, 0x0005)

    def _loc_A42(): pass

    label('loc_A42')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BB0',
    )

    OP_0D()
    Sleep(200)

    If(
        (
            (Expr.Eval, "OP_29(0x00C0, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x00C0, 0x00, 0x20)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_AD4',
    )

    OP_28(0x00C3, 0x04, 0x20)
    OP_A9(0x03)

    ChrTalk(
        0x0008,
        (
            '#0350291561V#740F辛苦了。\n',
            '看来顺利达成目的了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350291562V完成了什么任务的话\n',
            '再来报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BAA')

    def _loc_AD4(): pass

    label('loc_AD4')

    If(
        (
            (Expr.Eval, "OP_A9(0x03)"),
            Expr.Return,
        ),
        'loc_B41',
    )

    ChrTalk(
        0x0008,
        (
            '#0350350520V#740F辛苦了。\n',
            '看来顺利达成目的了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350350521V完成了什么任务的话\n',
            '再来报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BAA')

    def _loc_B41(): pass

    label('loc_B41')

    ChrTalk(
        0x0008,
        (
            '#0350291563V#740F哎呀，现在\n',
            '好像没有可以报告的工作吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350291564V完成了什么任务的话\n',
            '再来报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BAA(): pass

    label('loc_BAA')

    OP_56(0x00)
    TalkEnd(0x0008)

    Return()

    def _loc_BB0(): pass

    label('loc_BB0')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C77',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_C73',
    )

    ChrTalk(
        0x0008,
        (
            '#0350350522V#740F要叫同伴来吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350350523V明白了。\n',
            '我马上去联络。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '联络各支部，\n',
            '集合了待命人员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeIn(1000, 0)
    OP_0D()

    def _loc_C73(): pass

    label('loc_C73')

    TalkEnd(0x0008)

    Return()

    def _loc_C77(): pass

    label('loc_C77')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C88',
    )

    TalkEnd(0x0008)

    Return()

    def _loc_C88(): pass

    label('loc_C88')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_DB0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_CFA',
    )

    ChrTalk(
        0x0008,
        (
            '#0350350524V#740F利吉和你们，\n',
            '今天都辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350350525V以后也请保持这个状态，\n',
            '继续努力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DAD')

    def _loc_CFA(): pass

    label('loc_CFA')

    ChrTalk(
        0x0008,
        (
            '#0350350526V#740F导力停止现象\n',
            '似乎影响到了\n',
            '意想不到的地方。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350350527V玛鲁加矿山的事件就是一个例子，\n',
            '今后也必须多加注意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350350528V你们也不要疏忽大意\n',
            '继续保持警戒哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DAD(): pass

    label('loc_DAD')

    Jump('loc_1EF7')

    def _loc_DB0(): pass

    label('loc_DB0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_F97',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F0F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 4, 0x2004)),
            Expr.Return,
        ),
        'loc_E30',
    )

    ChrTalk(
        0x0008,
        (
            '#0350350529V#740F刚刚才联络，\n',
            '哪能马上好呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350350530V如果要去王都，\n',
            '那时也顺便去一下支部吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F09')

    def _loc_E30(): pass

    label('loc_E30')

    ChrTalk(
        0x0008,
        (
            '#0350350531V#740F总之公告板的工作\n',
            '和附近的巡视就拜托了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350350532V其中玛鲁加矿山尤其令人在意。\n',
            '正好工程也预定开始了，\n',
            '利吉已经去警备了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350350533V考虑到可能发生万不得已的事态，\n',
            '你们能去看看情况就更好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F09(): pass

    label('loc_F09')

    OP_A2(0x0001)

    Jump('loc_F94')

    def _loc_F0F(): pass

    label('loc_F0F')

    ChrTalk(
        0x0008,
        (
            '#0350350531V#740F总之公告板的工作\n',
            '和附近的巡视就拜托了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350350535V特别是工程预定开始的矿山，\n',
            '就是希望去看看情况的地方之一。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_F94(): pass

    label('loc_F94')

    Jump('loc_1EF7')

    def _loc_F97(): pass

    label('loc_F97')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_13F5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_1227',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1188',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0076, 0x01, 0x0400)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_111E',
    )

    ChrTurnDirection(0x0008, 0x0104, 0)

    ChrTalk(
        0x0008,
        (
            '#0350470987V#740F哎呀，是奥利维尔啊。\n',
            '已经好了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040450590V#035F呼，当然。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040470989V这种程度的酒\n',
            '可醉不倒我哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350470990V#740F是吗，那就放心了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350470991V#741F那么，下次再邀请我哦。\n',
            '到时候可要大灌你一场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040470992V#037F哈，哈哈……\n',
            '我期待着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470993V#1016F（唔、嗯……\n',
            '　皮笑肉不笑啊。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0076, 0x01, 0x0400)

    Jump('loc_1185')

    def _loc_111E(): pass

    label('loc_111E')

    ChrTalk(
        0x0008,
        (
            '#0350470994V#740F不管怎样，\n',
            '好久没喝得像今天这么痛快了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350470995V那么，\n',
            '以后也要多加注意哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1185(): pass

    label('loc_1185')

    Jump('loc_1224')

    def _loc_1188(): pass

    label('loc_1188')

    ChrTalk(
        0x0008,
        (
            '#0350470996V#740F奥利维尔的话\n',
            '已经在２楼待命了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350470997V看起来稍微有点累，\n',
            '不过身体似乎没有大碍，\n',
            '就带他去吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350300084V那么，今后也请当心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1224(): pass

    label('loc_1224')

    Jump('loc_13F2')

    def _loc_1227(): pass

    label('loc_1227')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_12BC',
    )

    ChrTalk(
        0x0008,
        (
            '#0350300082V#740F去柏斯的票\n',
            '已经安排好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350300083V和飞船坪的阿兰说一下\n',
            '就可以马上办理手续了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350300084V那么，今后也请当心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13F2')

    def _loc_12BC(): pass

    label('loc_12BC')

    ChrTalk(
        0x0008,
        (
            '#0350300085V#740F关于定期船的票\n',
            '已经安排好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350300086V和飞船坪的阿兰说一下\n',
            '应该马上就可以办手续了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350300087V#744F这下没有被实验的地区\n',
            '就只剩下柏斯了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350300088V说不定会成为\n',
            '前所未有的严峻旅途……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350300089V#740F不过是你们的话，\n',
            '一定能渡过难关的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350300090V请加油吧。\n',
            '祝你们好运。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_13F2(): pass

    label('loc_13F2')

    Jump('loc_1EF7')

    def _loc_13F5(): pass

    label('loc_13F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_15AB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1483',
    )

    ChrTalk(
        0x0008,
        (
            '#0350291565V#740F既然是自投罗网，\n',
            '我就不说什么要当心之类的俗套话了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350291566V请尽量发挥游击士的实力，\n',
            '惩治犯人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15A8')

    def _loc_1483(): pass

    label('loc_1483')

    ChrTalk(
        0x0008,
        (
            '#0350291567V#740F我作为协会的接待员\n',
            '也支持你们的决定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350291568V虽说去神秘森林\n',
            '等于就是往陷阱里跳，\n',
            '但现在的形势下也没有别的办法了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350291569V既然是自投罗网，\n',
            '我就不说什么要当心之类的俗套话了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350291570V请尽量发挥游击士的实力，\n',
            '惩治犯人吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350291571V……我就说这些了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_15A8(): pass

    label('loc_15A8')

    Jump('loc_1EF7')

    def _loc_15AB(): pass

    label('loc_15AB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_1749',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_164B',
    )

    ChrTalk(
        0x0008,
        (
            '#0350291572V#740F去农场要从米尔西街道出去，\n',
            '然后向西，途中再向南拐弯就到了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350291573V虽然是你们很熟悉的道路，\n',
            '但行动也不可疏忽大意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1746')

    def _loc_164B(): pass

    label('loc_164B')

    ChrTalk(
        0x0008,
        (
            '#0350291574V#740F就麻烦你们\n',
            '帮助帕赛尔农场\n',
            '的人们避难吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350291575V去农场要从米尔西街道出去，\n',
            '然后向西，途中再向南拐弯就到了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350291576V雾比昨天更加浓，\n',
            '几乎看不清前方的路。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350291573V虽然是你们很熟悉的道路，\n',
            '但行动也不可疏忽大意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_1746(): pass

    label('loc_1746')

    Jump('loc_1EF7')

    def _loc_1749(): pass

    label('loc_1749')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_1C29',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 6, 0x180E)),
            Expr.Return,
        ),
        'loc_176B',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_176B(): pass

    label('loc_176B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 7, 0x180F)),
            Expr.Return,
        ),
        'loc_177C',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x2),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_177C(): pass

    label('loc_177C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 0, 0x1810)),
            Expr.Return,
        ),
        'loc_178D',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x4),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_178D(): pass

    label('loc_178D')

    Switch(
        (
            (Expr.PushReg, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_17B6'),
        (0x00000001, 'loc_18B2'),
        (0x00000002, 'loc_194B'),
        (0x00000004, 'loc_19E2'),
        (0x00000003, 'loc_1A79'),
        (0x00000005, 'loc_1AE3'),
        (0x00000006, 'loc_1B4F'),
        (0x00000007, 'loc_1BBB'),
        (-1, 'loc_1C23'),
    )

    def _loc_17B6(): pass

    label('loc_17B6')

    ChrTalk(
        0x0008,
        (
            '#0350291578V#740F总之就是想拜托你们\n',
            '确认一下雾扩张的范围。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350280814V南边的艾利兹街道，\n',
            '西边的米尔西街道，北边的玛鲁加山道。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350291580V希望你们去这三条道路确认\n',
            '雾到底蔓延到哪里了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350291581V现在到处视野都很差，\n',
            '无论如何调查都要慎重。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C26')

    def _loc_18B2(): pass

    label('loc_18B2')

    ChrTalk(
        0x0008,
        (
            '#0350291582V#740F辛苦了……\n',
            '调查似乎很顺利。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350291583V剩下西边的米尔西街道\n',
            '和北边的玛鲁加山道两处了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350291584V那么，请你们\n',
            '继续调查吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C26')

    def _loc_194B(): pass

    label('loc_194B')

    ChrTalk(
        0x0008,
        (
            '#0350291582V#740F辛苦了……\n',
            '调查似乎很顺利。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350291586V剩下南边的艾利兹街道\n',
            '和北边的玛鲁加山道两处了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350291587V那么，就请\n',
            '继续调查吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C26')

    def _loc_19E2(): pass

    label('loc_19E2')

    ChrTalk(
        0x0008,
        (
            '#0350291582V#740F辛苦了……\n',
            '调查似乎很顺利。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350291589V剩下南边的艾利兹街道\n',
            '西边的米尔西街道两处了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350291584V那么，请你们\n',
            '继续调查吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C26')

    def _loc_1A79(): pass

    label('loc_1A79')

    ChrTalk(
        0x0008,
        (
            '#0350291591V#740F调查方面也只剩下\n',
            '北边的玛鲁加山道。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350291592V那么，就拜托你们\n',
            '完成这任务了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C26')

    def _loc_1AE3(): pass

    label('loc_1AE3')

    ChrTalk(
        0x0008,
        (
            '#0350291593V#740F调查方面也只剩下\n',
            '西边的米尔西街道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350291592V那么，就拜托你们\n',
            '完成这任务了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C26')

    def _loc_1B4F(): pass

    label('loc_1B4F')

    ChrTalk(
        0x0008,
        (
            '#0350291595V#740F调查方面也只剩下\n',
            '南边的艾利兹街道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350291592V那么，就拜托你们\n',
            '完成这任务了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C26')

    def _loc_1BBB(): pass

    label('loc_1BBB')

    ChrTalk(
        0x0008,
        (
            '#0350291597V#743F对了，你不先回家\n',
            '看看家里的状况吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350291598V#740F雾的调查报告\n',
            '可以先等一等。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C23(): pass

    label('loc_1C23')

    Jump('loc_1C26')

    def _loc_1C26(): pass

    label('loc_1C26')

    Jump('loc_1EF7')

    def _loc_1C29(): pass

    label('loc_1C29')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 3, 0x1003)),
            Expr.Return,
        ),
        'loc_1EF7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0205, 5, 0x102D)),
            Expr.Return,
        ),
        'loc_1DEE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1C79',
    )

    ChrTalk(
        0x0008,
        (
            '#0350190290V#740F艾丝蒂尔……今天\n',
            '就请回家休息吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DEB')

    def _loc_1C79(): pass

    label('loc_1C79')

    ChrTurnDirection(0x0008, 0x0142, 0)

    ChrTalk(
        0x0008,
        (
            '#0350190283V#740F……你是七耀教会的人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0142,
        (
            '#0180190284V#1060F嗯，是的。\n',
            '我叫凯文·格拉汉姆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350190285V#742F（虽然不知道发生了什么事，\n',
            '　但这样的艾丝蒂尔还是第一次看到……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350190286V#740F（麻烦你暂时\n',
            '陪伴她一下吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0142,
        (
            '#0180190287V#1060F（我原本就是这样打算的。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350190288V#740F拜托了，凯文先生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190289V#505F？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_1DEB(): pass

    label('loc_1DEB')

    Jump('loc_1EF7')

    def _loc_1DEE(): pass

    label('loc_1DEE')

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    ChrTurnDirection(0x0008, 0x0101, 400)
    Sleep(600)

    OP_63(0x0008)

    ChrTalk(
        0x0008,
        (
            '#0350190278V#743F…………艾丝蒂尔！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350190279V怎么了？\n',
            '不是应该还在王都吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190280V#000F嗯，因为约修亚\n',
            '应该在家，我来接他的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350190281V#743F……接约修亚？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350190282V#742F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x102D)

    def _loc_1EF7(): pass

    label('loc_1EF7')

    TalkEnd(0x0008)

    Return()

# id: 0x0007 offset: 0x1EFB
@scena.Code('func_07_1EFB')
def func_07_1EFB():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 5, 0x181D)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 6, 0x181E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1F13',
    )

    Call(0, 0x0014)

    Jump('loc_3E5F')

    def _loc_1F13(): pass

    label('loc_1F13')

    TalkBegin(0x0010)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            (Expr.TestScenaFlags, ScenaFlag(0x0310, 5, 0x1885)),
            Expr.Nez64,
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            (Expr.TestScenaFlags, ScenaFlag(0x0413, 0, 0x2098)),
            Expr.Nez64,
            Expr.Or,
            Expr.Return,
        ),
        'loc_1F6C',
    )

    Call(6, 0x0004)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1F5B',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1F55',
    )

    OP_A9(0x06)

    Jump('loc_1F57')

    def _loc_1F55(): pass

    label('loc_1F55')

    OP_A9(0x02)

    def _loc_1F57(): pass

    label('loc_1F57')

    TalkEnd(0x0010)

    Return()

    def _loc_1F5B(): pass

    label('loc_1F5B')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1F6C',
    )

    TalkEnd(0x0010)

    Return()

    def _loc_1F6C(): pass

    label('loc_1F6C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2594',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0413, 0, 0x2098)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2175',
    )

    ChrTurnDirection(0x0010, 0x0101, 0)

    ChrTalk(
        0x0010,
        (
            '哦哦……\n',
            '这不是艾丝蒂尔和约修亚吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '呀～终于\n',
            '两人一起出现了呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1008F出、出现……\n',
            '我们又不是魔兽和幽灵来着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F里农先生也\n',
            '和平时一样，真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0102, 400)

    ChrTalk(
        0x0010,
        (
            '啊啊，托你的福呢。\n',
            '生意也不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '不，不过，倒是人生\n',
            '稍微有点危险……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1044F？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011F咦……发生什么事了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0101, 400)
    OP_62(0x0010, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(400)

    ChrTalk(
        0x0010,
        (
            '不，没事……\n',
            '当我没说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '哎，别说我了，\n',
            '约修亚可是好久没回故乡了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '虽说这时期非常忙碌，\n',
            '不过还是慢慢逛逛再走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1048F哦、哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)
    OP_A2(0x2098)

    Jump('loc_2591')

    def _loc_2175(): pass

    label('loc_2175')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 6, 0x2086)),
            Expr.Return,
        ),
        'loc_221F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_21D9',
    )

    ChrTalk(
        0x0010,
        (
            '刚才基蒂\n',
            '送货回来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '好像一直笑眯眯的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '发生什么好事了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    Jump('loc_221C')

    def _loc_21D9(): pass

    label('loc_21D9')

    ChrTalk(
        0x0010,
        (
            '送货回来以后基蒂\n',
            '好像一直笑眯眯的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '发生什么好事了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_221C(): pass

    label('loc_221C')

    Jump('loc_2591')

    def _loc_221F(): pass

    label('loc_221F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_234F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_228C',
    )

    ChrTalk(
        0x0010,
        (
            '虽说现在应该非常忙碌，\n',
            '还是慢慢逛逛再走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '特别约修亚隔了好久\n',
            '才回到洛连特的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_234C')

    def _loc_228C(): pass

    label('loc_228C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2301',
    )

    ChrTalk(
        0x0010,
        (
            '呀，艾丝蒂尔和约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '似乎矿山\n',
            '有什么麻烦的样子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '哎，导力器\n',
            '突然停了嘛。\n',
            '也难怪啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    Jump('loc_234C')

    def _loc_2301(): pass

    label('loc_2301')

    ChrTalk(
        0x0010,
        (
            '似乎矿山\n',
            '有什么麻烦的样子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '哎，导力器\n',
            '突然停了嘛。\n',
            '也难怪啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_234C(): pass

    label('loc_234C')

    Jump('loc_2591')

    def _loc_234F(): pass

    label('loc_234F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041A, 6, 0x20D6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_244F',
    )

    ChrTalk(
        0x0102,
        (
            '#1044F……对了，里农先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0102, 400)

    ChrTalk(
        0x0010,
        (
            '嗯？什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0013, 400)

    ChrTalk(
        0x0102,
        (
            '#1040F嗯，那位\n',
            '是新的店员吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '嗯，嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '说，说是打工呢～\n',
            '又好像客人一样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '是老妈带来\n',
            '帮店里忙的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1035F原、原来如此……\n',
            '（里农先生看来也挺辛苦的……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x20D6)

    Jump('loc_2591')

    def _loc_244F(): pass

    label('loc_244F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2507',
    )

    ChrTalk(
        0x0010,
        (
            '多亏基蒂，\n',
            '店里生意不错哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '和她相处也很融洽，\n',
            '现在就和家人一样的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '嗯，虽然说\n',
            '这是件好事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '不、不过我作为男人的一面\n',
            '却有一种被逼到死角的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    Jump('loc_2591')

    def _loc_2507(): pass

    label('loc_2507')

    ChrTalk(
        0x0010,
        (
            '和基蒂相处也很融洽，\n',
            '现在就和家人一样的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '嗯，虽然说\n',
            '这是件好事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '呼，呼……\n',
            '总觉得事情好像\n',
            '都在老妈的算计之中一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2591(): pass

    label('loc_2591')

    Jump('loc_3E5C')

    def _loc_2594(): pass

    label('loc_2594')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_2877',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034A, 6, 0x1A56)),
            Expr.Return,
        ),
        'loc_26BD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_2623',
    )

    ChrTalk(
        0x0010,
        (
            '基蒂暂时\n',
            '留在这里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '哎，有她在\n',
            '倒是帮了店里的大忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '总觉得有点害怕，事情好像\n',
            '都在老妈的算计里一样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26BA')

    def _loc_2623(): pass

    label('loc_2623')

    ChrTalk(
        0x0010,
        (
            '基蒂暂时\n',
            '留在这里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '说是为了以后自己\n',
            '开店来学习……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '感、感觉又高兴又害怕……\n',
            '真是复杂的心情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '哎，有她在\n',
            '倒是帮了店里的大忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_26BA(): pass

    label('loc_26BA')

    Jump('loc_2874')

    def _loc_26BD(): pass

    label('loc_26BD')

    ChrTurnDirection(0x0010, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x0010,
        (
            '呀，艾丝蒂尔和\n',
            '雪拉扎德。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '我听说了哦，你们似乎\n',
            '又要马上出发了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F就、就传开了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F呵呵，消息真灵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '托你们的福，商品也\n',
            '顺利地重新开始进货了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '有什么必要的东西\n',
            '就在出发前买好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F嗯，谢谢里农先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '要是进了斯托雷加的新鞋子\n',
            '记得帮我留着啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '哈哈，明白啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '那么，你们俩\n',
            '今后也要多努力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#027F嗯嗯，以后有机会\n',
            '再来慢慢挑东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1001F那么再见，里农先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1885)
    OP_A2(0x1A56)
    def _loc_2874(): pass

    label('loc_2874')

    Jump('loc_3E5C')

    def _loc_2877(): pass

    label('loc_2877')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_2D6B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_2954',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_28CD',
    )

    ChrTalk(
        0x0010,
        (
            '真不愧是在王都的\n',
            '百货店工作过的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '基蒂\n',
            '相当能干。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2951')

    def _loc_28CD(): pass

    label('loc_28CD')

    ChrTalk(
        0x0010,
        (
            '是啊是啊，关于那边\n',
            '的女人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '是王都来的，叫基蒂、\n',
            '现在在店里帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '感觉是打算在定期船开动之前\n',
            '进行短期的打工吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_2951(): pass

    label('loc_2951')

    Jump('loc_2D68')

    def _loc_2954(): pass

    label('loc_2954')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0310, 5, 0x1885)),
            Expr.Return,
        ),
        'loc_2ACB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_29AB',
    )

    ChrTalk(
        0x0010,
        (
            '基蒂……\n',
            '非常努力哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '要选择人生的搭档，\n',
            '就该选这样的人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2AC8')

    def _loc_29AB(): pass

    label('loc_29AB')

    ChrTalk(
        0x0010,
        (
            '基蒂……\n',
            '非常努力哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '说是来帮忙店里，一开始\n',
            '还以为是老妈暗地里安排的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '但看了基蒂的样子，\n',
            '感觉是真的喜欢工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '虽、虽然我不大喜欢\n',
            '老妈帮我安排相亲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '不过要选择人生的搭档，\n',
            '我还真想选这样的人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '不过既然是喜欢店里工作的人，\n',
            '感觉应该能发展顺利吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_2AC8(): pass

    label('loc_2AC8')

    Jump('loc_2D68')

    def _loc_2ACB(): pass

    label('loc_2ACB')

    OP_62(0x0010, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    ChrTurnDirection(0x0010, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x0010,
        (
            '哦！\n',
            '艾丝蒂尔，终于来了啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1017F里农先生……\n',
            '嘿嘿，好久不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '呀～我就听客人\n',
            '说你回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '不知道几时会来，\n',
            '一直等着你呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1025F这样啊。\n',
            '抱歉这么晚才来打招呼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '哪里哪里，没关系啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '不过你回来的\n',
            '可真不是时候啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '今天雾还是这么大啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1007F嗯，真的是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1015F话说回来……\n',
            '昨天夜里不要紧吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '没发生什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '呀，倒是\n',
            '没什么特别的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '啊啊，对了，睡觉之前\n',
            '有个红头发的游击士来过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '说是在巡逻中，\n',
            '是你们的伙伴吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F啊，嗯。\n',
            '他叫阿加特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#027F呵呵，看来\n',
            '很认真的在巡逻呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '这种时候，就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '有什么需要的东西，\n',
            '随时都可以来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)
    OP_A2(0x1885)
    def _loc_2D68(): pass

    label('loc_2D68')

    Jump('loc_3E5C')

    def _loc_2D6B(): pass

    label('loc_2D6B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_3524',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_34C9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 5, 0x181D)),
            Expr.Return,
        ),
        'loc_2F68',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_2DDF',
    )

    ChrTalk(
        0x0010,
        (
            '真不愧是在王都的\n',
            '百货店工作过的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '那个明亮的笑容\n',
            '真令人禁不住着迷啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F65')

    def _loc_2DDF(): pass

    label('loc_2DDF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_2EA6',
    )

    ChrTalk(
        0x0010,
        (
            '基蒂好像在王都的百货店\n',
            '卖红茶来着……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '所以她对茶和点心的事\n',
            '特别的清楚哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '商品的展示啊，\n',
            '小东西的选择都很有品味……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '更出色的是，那明亮的笑容\n',
            '和灵活的应对真是太棒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    Jump('loc_2F65')

    def _loc_2EA6(): pass

    label('loc_2EA6')

    ChrTalk(
        0x0010,
        (
            '咦，艾丝蒂尔。\n',
            '还有什么要买吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '对了对了，我想你应该见过了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '外面有个女人在工作吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '她叫基蒂，\n',
            '现在在店里帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '感觉是打算在定期船开动之前\n',
            '进行短期的打工吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)
    OP_A2(0x1885)

    def _loc_2F65(): pass

    label('loc_2F65')

    Jump('loc_34C6')

    def _loc_2F68(): pass

    label('loc_2F68')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_3051',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_2FB7',
    )

    ChrTalk(
        0x0010,
        (
            '真不愧是在王都的\n',
            '百货店工作过的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '基蒂\n',
            '相当能干。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_304E')

    def _loc_2FB7(): pass

    label('loc_2FB7')

    ChrTalk(
        0x0010,
        (
            '对了对了，我想你应该见过了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '外面有个女人在工作吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '她叫基蒂，\n',
            '现在在店里帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '感觉是打算在定期船开动之前\n',
            '进行短期的打工吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_304E(): pass

    label('loc_304E')

    Jump('loc_34C6')

    def _loc_3051(): pass

    label('loc_3051')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0310, 5, 0x1885)),
            Expr.Return,
        ),
        'loc_3229',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_30A0',
    )

    ChrTalk(
        0x0010,
        (
            '真不愧是在王都的\n',
            '百货店工作过的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '基蒂\n',
            '相当能干。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3226')

    def _loc_30A0(): pass

    label('loc_30A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_3167',
    )

    ChrTalk(
        0x0010,
        (
            '基蒂好像在王都的百货店\n',
            '卖红茶来着……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '所以她对茶和点心的事\n',
            '特别的清楚哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '商品的展示啊，\n',
            '小东西的选择都很有品味……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '更出色的是，那明亮的笑容\n',
            '和灵活的应对真是太棒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    Jump('loc_3226')

    def _loc_3167(): pass

    label('loc_3167')

    ChrTalk(
        0x0010,
        (
            '咦，艾丝蒂尔。\n',
            '还有什么要买吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '对了对了，我想你应该见过了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '外面有个女人在工作吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '她叫基蒂，\n',
            '现在在店里帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '感觉是打算在定期船开动之前\n',
            '进行短期的打工吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)
    OP_A2(0x1885)

    def _loc_3226(): pass

    label('loc_3226')

    Jump('loc_34C6')

    def _loc_3229(): pass

    label('loc_3229')

    OP_62(0x0010, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    ChrTurnDirection(0x0010, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x0010,
        (
            '哦！\n',
            '艾丝蒂尔，终于来了啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1017F里农先生……\n',
            '嘿嘿，好久不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '呀～我就听客人\n',
            '说你回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '不知道几时会来，\n',
            '一直等着你呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1025F这样啊。\n',
            '抱歉这么晚才来打招呼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '哪里哪里，没关系啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '不过你回来的\n',
            '可真不是时候啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '今天雾还是这么大啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1007F嗯，真的是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1015F话说回来……\n',
            '昨天夜里不要紧吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '没发生什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '呀，倒是\n',
            '没什么特别的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '啊啊，对了，睡觉之前\n',
            '有个红头发的游击士来过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '说是在巡逻中，\n',
            '是你们的伙伴吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F啊，嗯。\n',
            '他叫阿加特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#027F呵呵，看来\n',
            '很认真的在巡逻呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '这种时候，就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '有什么需要的东西，\n',
            '随时都可以来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)
    OP_A2(0x1885)
    def _loc_34C6(): pass

    label('loc_34C6')

    Jump('loc_3521')

    def _loc_34C9(): pass

    label('loc_34C9')

    ChrTalk(
        0x0010,
        (
            '有什么其他需要\n',
            '就不用客气尽管对她说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '从点心到杂志，\n',
            '她什么都会给你找到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_3521(): pass

    label('loc_3521')

    Jump('loc_3E5C')

    def _loc_3524(): pass

    label('loc_3524')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_3AA9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0310, 5, 0x1885)),
            Expr.Return,
        ),
        'loc_36C0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_35BF',
    )

    ChrTalk(
        0x0010,
        (
            '老妈从王都回来的时候，\n',
            '带来一个没见过的小姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '说、说不定真的\n',
            '是给我找来的媳妇人选。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '唉唉，真不该\n',
            '让她去什么王都……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_36BD')

    def _loc_35BF(): pass

    label('loc_35BF')

    ChrTalk(
        0x0010,
        (
            '我老妈也是搭刚才的定期船\n',
            '从王都回来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '让人伤脑筋的是，\n',
            '她居然带来个不认识的小姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '说是在定期船上认识的，\n',
            '不知道到底真的假的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '说、说不定真的\n',
            '是给我找来的媳妇人选。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '虽然觉得应该不可能……\n',
            '……但是老妈可是什么都做得出来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_36BD(): pass

    label('loc_36BD')

    Jump('loc_3AA6')

    def _loc_36C0(): pass

    label('loc_36C0')

    OP_62(0x0010, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    ChrTurnDirection(0x0010, 0x0101, 0)
    Sleep(400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0205, 4, 0x102C)),
            Expr.Return,
        ),
        'loc_3734',
    )

    ChrTalk(
        0x0010,
        (
            '哦，艾丝蒂尔。\n',
            '终于回来了吗～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F嗯，里农先生好久不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_37C7')

    def _loc_3734(): pass

    label('loc_3734')

    ChrTalk(
        0x0010,
        (
            '哦哦……这不是艾丝蒂尔吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '好久不见呢。\n',
            '几时回来的呀？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F嗯，就刚才呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '里农先生看起来也很不错呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '那可不，生龙活虎的啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_37C7(): pass

    label('loc_37C7')

    ChrTalk(
        0x0010,
        (
            '对了，听说\n',
            '你上哪里训练去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '那，成果怎样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1001F嘿嘿、当然是ＯＫ啰……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1015F……咦，里农先生\n',
            '是从哪儿知道训练的事的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '哈哈，可别小瞧\n',
            '街坊邻里的消息网哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '你去训练这点事，\n',
            '大家应该都知道吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F啊、啊哈哈……\n',
            '说来也是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F呵呵，这里\n',
            '看来一点也没变呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '对了对了，话说回来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '关于今天这雾，\n',
            '真的是有点诡异呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '前往柏斯的定期船\n',
            '好像也停了，不是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1007F嗯，其实我们也是\n',
            '因此才没法继续走的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#027F不过，打算停留期间\n',
            '也顺便调查一下这雾。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '协会也希望\n',
            '尽快搞清楚状况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0103, 400)

    ChrTalk(
        0x0010,
        (
            '是吗……\n',
            '那样可真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '但是，雪拉扎德你们\n',
            '也要多加注意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '这个雾实在奇怪。\n',
            '感觉没那么简单。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F是啊……我们会小心的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1002F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1000F那再见了，里农先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1885)
    def _loc_3AA6(): pass

    label('loc_3AA6')

    Jump('loc_3E5C')

    def _loc_3AA9(): pass

    label('loc_3AA9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 3, 0x1003)),
            Expr.Return,
        ),
        'loc_3E5C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0205, 4, 0x102C)),
            Expr.Return,
        ),
        'loc_3B0A',
    )

    ChrTalk(
        0x0010,
        (
            '话说回来，我老妈\n',
            '还在给我找新娘候选人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '唉哟……\n',
            '真希望她赶快死心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E5C')

    def _loc_3B0A(): pass

    label('loc_3B0A')

    ChrTalk(
        0x0010,
        (
            '哟…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '这不是艾丝蒂尔吗！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '好久不见了呢，\n',
            '何时回来的呀？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#001F里农先生，气色不错嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '那可不，生龙活虎的啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '对了对了，很快会有\n',
            '斯托雷加的新作运动鞋到货哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F咦～真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0142,
        (
            '#1060F记得是斯托雷加社创立５０周年的\n',
            'Anniversary限定款式吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '喔，小哥，你真了解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0142,
        (
            '#1061F因为，我可是\n',
            '斯托雷加的超级爱好者啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1062F看，现在穿的也是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0010, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    ChrTurnDirection(0x0010, 0x0142, 200)
    ChrTurnDirection(0x0101, 0x0142, 300)
    Sleep(500)

    ChrTalk(
        0x0010,
        (
            '喔喔!这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#004F我在杂志上看到过。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '记得是利贝尔买不到的\n',
            '外国限定款式啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0142,
        (
            '#1061F非常正确！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#007F虽然很想要，\n',
            '但是没办法买到呀～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0142,
        (
            '#1064F……咦，艾丝蒂尔\n',
            '莫非也是运动鞋迷？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#506F算，算是吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0142,
        (
            '#1061F呀～没想到\n',
            '有共同语言，太高兴了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1062F嗯嗯，这也\n',
            '一定是女神的指引呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#509F不过，七耀教会的\n',
            '神父穿运动鞋的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '咦，这个人，是神父？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0142,
        (
            '#1061F啊哈哈，别说\n',
            '这种死板的话嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x102C)

    def _loc_3E5C(): pass

    label('loc_3E5C')

    TalkEnd(0x0010)

    def _loc_3E5F(): pass

    label('loc_3E5F')

    Return()

# id: 0x0008 offset: 0x3E60
@scena.Code('func_08_3E60')
def func_08_3E60():
    TalkBegin(0x0011)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_3E6D',
    )

    Jump('loc_433F')

    def _loc_3E6D(): pass

    label('loc_3E6D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_40E2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034A, 7, 0x1A57)),
            Expr.Return,
        ),
        'loc_3F15',
    )

    ChrTalk(
        0x00FE,
        (
            '我也知道艾丝蒂尔你们的\n',
            '任务是非常辛苦的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以，支部的事情就交给我，\n',
            '你们集中于自己的工作就好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '交给支部的事，\n',
            '我一个人会想办法应付的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_40DF')

    def _loc_3F15(): pass

    label('loc_3F15')

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x00FE, 0x0103, 0)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '啊，雪拉前辈。\n',
            '我听爱娜小姐说了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像马上又要\n',
            '出发去柏斯了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F嗯嗯，是这么打算的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1007F抱歉哦，利吉先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '感觉总是\n',
            '麻烦你看家似的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '哪里，别介意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以前一直受卡西乌斯先生和\n',
            '雪拉前辈照顾的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了能独当一面，\n',
            '这点事当然要能胜任啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#526F呵呵，就是这股劲儿。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '还要再离开一段时间，\n',
            '洛连特的事就麻烦你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0103, 400)

    ChrTalk(
        0x00FE,
        (
            '嗯嗯，交给我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，祝前辈们\n',
            '去柏斯旅途顺风。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1A57)

    def _loc_40DF(): pass

    label('loc_40DF')

    Jump('loc_433F')

    def _loc_40E2(): pass

    label('loc_40E2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 3, 0x1823)),
            Expr.Return,
        ),
        'loc_41F0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_4143',
    )

    ChrTalk(
        0x00FE,
        (
            '听到铃声的方向……\n',
            '是神秘森林没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然很微弱，\n',
            '却是非常悦耳的音色。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_41ED')

    def _loc_4143(): pass

    label('loc_4143')

    ChrTalk(
        0x00FE,
        (
            '听到那个铃声的方向……\n',
            '是神秘森林那边吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然很微弱，\n',
            '但是非常悦耳的音色没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '话说回来，没想到\n',
            '出门期间竟然发生这样的事件……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也是时运不济啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    def _loc_41ED(): pass

    label('loc_41ED')

    Jump('loc_433F')

    def _loc_41F0(): pass

    label('loc_41F0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 3, 0x1003)),
            Expr.Return,
        ),
        'loc_433F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_423C',
    )

    ChrTalk(
        0x00FE,
        (
            '恭喜晋升正游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '期待再和你们\n',
            '一起在这里工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_433F')

    def _loc_423C(): pass

    label('loc_423C')

    ChrTalk(
        0x00FE,
        (
            '哎呀，这不是艾丝蒂尔吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我听爱娜小姐说了哦。\n',
            '恭喜晋升正游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#006F嘿嘿，谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说起来雪拉前辈和\n',
            '约修亚怎样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像没看到人啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F雪拉姐还在王都呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '约修亚应该先\n',
            '回家了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是吗，期待能再\n',
            '和你们一起在这里工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    def _loc_433F(): pass

    label('loc_433F')

    TalkEnd(0x0011)

    Return()

# id: 0x0009 offset: 0x4343
@scena.Code('func_09_4343')
def func_09_4343():
    TalkBegin(0x0012)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 6, 0x2086)),
            Expr.Return,
        ),
        'loc_43A8',
    )

    ChrTalk(
        0x00FE,
        (
            '今天的婚礼很不错呢。\n',
            '忍不住感动起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '里农要是也能举行\n',
            '那么棒的婚礼就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4A14')

    def _loc_43A8(): pass

    label('loc_43A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_4459',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_441A',
    )

    ChrTalk(
        0x00FE,
        (
            '店里好像\n',
            '一大早就很忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家都来\n',
            '买蜡烛和油灯了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天还有婚礼呢，\n',
            '真伤脑筋。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0006)

    Jump('loc_4456')

    def _loc_441A(): pass

    label('loc_441A')

    ChrTalk(
        0x00FE,
        (
            '店里好像\n',
            '一大早就很忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家都来\n',
            '买蜡烛和油灯了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4456(): pass

    label('loc_4456')

    Jump('loc_4A14')

    def _loc_4459(): pass

    label('loc_4459')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_46DA',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0075, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_4541',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_44A2',
    )

    ChrTalk(
        0x00FE,
        (
            '不过，也因此\n',
            '让我想起了\n',
            '那个久违的料理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_453E')

    def _loc_44A2(): pass

    label('loc_44A2')

    ChrTalk(
        0x00FE,
        (
            '哎呀，是艾丝蒂尔啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们也够辛苦呢。\n',
            '还得应付\n',
            '老爷爷耍性子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，也因此\n',
            '让我想起了\n',
            '那个久违的料理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这件事倒是得感谢\n',
            '拉欧爷爷啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0006)

    def _loc_453E(): pass

    label('loc_453E')

    Jump('loc_46D7')

    def _loc_4541(): pass

    label('loc_4541')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_459F',
    )

    ChrTalk(
        0x00FE,
        (
            '真是抱歉呢。\n',
            '似乎让你们有了过多的期待。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，人生在世\n',
            '可不能太慷慨呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_46D7')

    def _loc_459F(): pass

    label('loc_459F')

    If(
        (
            (Expr.Eval, "OP_29(0x0075, 0x01, 0x0008)"),
            (Expr.Eval, "OP_29(0x0075, 0x01, 0x0200)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0075, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0075, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_45CA',
    )

    Call(1, 0x0001)

    Jump('loc_46D7')

    def _loc_45CA(): pass

    label('loc_45CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_4626',
    )

    ChrTalk(
        0x00FE,
        (
            '里农似乎对基蒂\n',
            '也挺中意的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '接下来可不能鲁莽行事，\n',
            '要仔细观察情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_46D7')

    def _loc_4626(): pass

    label('loc_4626')

    ChrTalk(
        0x00FE,
        (
            '基蒂暂时\n',
            '会待在我们家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我当然再高兴不过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '里农似乎对基蒂\n',
            '也挺中意的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '接下来可不能鲁莽行事，\n',
            '要仔细观察情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '顺其自然、水到渠成\n',
            '才是最好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0006)

    def _loc_46D7(): pass

    label('loc_46D7')

    Jump('loc_4A14')

    def _loc_46DA(): pass

    label('loc_46DA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_478E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_472B',
    )

    ChrTalk(
        0x00FE,
        (
            '里农对基蒂\n',
            '也是很钦佩呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔……\n',
            '好像有不错的预感哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_478B')

    def _loc_472B(): pass

    label('loc_472B')

    ChrTalk(
        0x00FE,
        (
            '基蒂似乎\n',
            '工作很努力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '里农对那女孩\n',
            '也是很钦佩呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔……\n',
            '好像有不错的预感哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0006)

    def _loc_478B(): pass

    label('loc_478B')

    Jump('loc_4A14')

    def _loc_478E(): pass

    label('loc_478E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_47F2',
    )

    ChrTalk(
        0x00FE,
        (
            '今天早上开始基蒂\n',
            '就在下面工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '精神十足的声音这里\n',
            '都听得到，真令人心情愉快。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4A14')

    def _loc_47F2(): pass

    label('loc_47F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_4915',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_486C',
    )

    ChrTalk(
        0x00FE,
        (
            '这位小姐\n',
            '似乎预定去柏斯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '定期船停航了，\n',
            '真是运气不好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，暂时就\n',
            '让她待在我们家了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4912')

    def _loc_486C(): pass

    label('loc_486C')

    ChrTalk(
        0x00FE,
        (
            '这位小姐是\n',
            '定期船上认识的人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不凑巧由于这雾\n',
            '没法到达目的地了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看她一个人挺可怜的，就让她\n',
            '在船开动之前住在我家了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '困难的时候要互相帮助嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0006)

    def _loc_4912(): pass

    label('loc_4912')

    Jump('loc_4A14')

    def _loc_4915(): pass

    label('loc_4915')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 3, 0x1003)),
            Expr.Return,
        ),
        'loc_4A14',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_4976',
    )

    ChrTalk(
        0x00FE,
        (
            '我这么努力地帮儿子找媳妇， \n',
            '他却好像没什么兴趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，这个不孝子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4A14')

    def _loc_4976(): pass

    label('loc_4976')

    ChrTalk(
        0x00FE,
        (
            '呼…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '能嫁给里农的女孩\n',
            '可真难找呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……既然如此，\n',
            '只好出去旅行找儿媳妇了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '人多的地方……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对了，难得的机会\n',
            '就去王都看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0006)

    def _loc_4A14(): pass

    label('loc_4A14')

    TalkEnd(0x0012)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_4A25',
    )

    OP_8C(0x0012, 180, 0)

    def _loc_4A25(): pass

    label('loc_4A25')

    Return()

# id: 0x000A offset: 0x4A26
@scena.Code('func_0A_4A26')
def func_0A_4A26():
    TalkBegin(0x0013)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 6, 0x2086)),
            Expr.Return,
        ),
        'loc_4A96',
    )

    ChrTalk(
        0x00FE,
        (
            '哈，刚才\n',
            '真吓了一跳……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '居然接到了\n',
            '新娘捧花……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈哈，或许可以\n',
            '稍微期待一小下哟？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4ED9')

    def _loc_4A96(): pass

    label('loc_4A96')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_4B73',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4B16',
    )

    ChrTalk(
        0x00FE,
        (
            '欢迎！\n',
            '欢迎光临里农杂货铺。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '应该是因为导力器停了，\n',
            '今天客人可真多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家都来找\n',
            '应急用品了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0007)

    Jump('loc_4B70')

    def _loc_4B16(): pass

    label('loc_4B16')

    ChrTalk(
        0x00FE,
        (
            '应该是因为导力器停了，\n',
            '今天客人可真多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要找什么东西的话，\n',
            '就不要客气尽管说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4B70(): pass

    label('loc_4B70')

    Jump('loc_4ED9')

    def _loc_4B73(): pass

    label('loc_4B73')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_4C95',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_4BD8',
    )

    ChrTalk(
        0x00FE,
        (
            '去不成柏斯，\n',
            '那休假中就待在这里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了学习自己开店的经验，\n',
            '打算努力呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4C92')

    def _loc_4BD8(): pass

    label('loc_4BD8')

    ChrTalk(
        0x00FE,
        (
            '欢迎！\n',
            '欢迎光临里农杂货铺。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我会暂时\n',
            '在这里学习的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了学习自己开店的经验，\n',
            '打算努力呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且，店主里农先生\n',
            '也对我很好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '感觉像在自己家一样，\n',
            '真的很安心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0007)

    def _loc_4C92(): pass

    label('loc_4C92')

    Jump('loc_4ED9')

    def _loc_4C95(): pass

    label('loc_4C95')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_4D55',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_4CF2',
    )

    ChrTalk(
        0x00FE,
        (
            '向各位游击士们\n',
            '推荐的是这些方便的药哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '出门的时候\n',
            '请一定要购买！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4D52')

    def _loc_4CF2(): pass

    label('loc_4CF2')

    ChrTalk(
        0x00FE,
        (
            '欢迎！\n',
            '客人们是游击士吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那样的话，\n',
            '有方便的药哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '出门的时候\n',
            '请一定要购买！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0007)

    def _loc_4D52(): pass

    label('loc_4D52')

    Jump('loc_4ED9')

    def _loc_4D55(): pass

    label('loc_4D55')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_4DDF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_4D85',
    )

    ChrTalk(
        0x00FE,
        (
            '欢迎！\n',
            '请轻松愉快地观看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4DDC')

    def _loc_4D85(): pass

    label('loc_4D85')

    ChrTalk(
        0x00FE,
        (
            '欢迎！\n',
            '欢迎光临里农杂货铺。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从食品到杂货，\n',
            '应有尽有哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请随便看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0007)

    def _loc_4DDC(): pass

    label('loc_4DDC')

    Jump('loc_4ED9')

    def _loc_4DDF(): pass

    label('loc_4DDF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_4ED9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_4E4C',
    )

    ChrTalk(
        0x00FE,
        (
            '到定期船重新开始航行之前，\n',
            '决定承蒙关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '既然添了麻烦，\n',
            '就打算在店里多帮点忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4ED9')

    def _loc_4E4C(): pass

    label('loc_4E4C')

    ChrTalk(
        0x00FE,
        (
            '承蒙布露姆老奶奶的关照，\n',
            '决定留在这里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可以的话，打算\n',
            '在店里帮点忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我平时也在王都的\n',
            '百货店工作的。\n',
            '待客还算有点自信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0007)

    def _loc_4ED9(): pass

    label('loc_4ED9')

    TalkEnd(0x0013)

    Return()

# id: 0x000B offset: 0x4EDD
@scena.Code('func_0B_4EDD')
def func_0B_4EDD():
    TalkBegin(0x0014)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_5160',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0413, 3, 0x209B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_50C9',
    )

    ChrTalk(
        0x00FE,
        (
            '哦，艾丝蒂尔啊……\n',
            '这，这不是约修亚吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1030F好久不见了，菲特先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哟，才多久没见啊，\n',
            '就完全长成个男子汉了嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呀，这我就放心了。\n',
            '和艾丝蒂尔在游击士的道路上都\n',
            '做得很漂亮嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1030F是啊，拖您的福。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来王国中\n',
            '好象发生了严重的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '回归军队的卡西乌斯\n',
            '也忙得不可开交吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '作为游击士的你们两个\n',
            '可要努力，不能输给他哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F嗯嗯，在很努力工作呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1030F如果有什么困难\n',
            '就联系协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我会的。\n',
            '那么，两人都要小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)
    OP_A2(0x209B)

    Jump('loc_5160')

    def _loc_50C9(): pass

    label('loc_50C9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_510C',
    )

    ChrTalk(
        0x00FE,
        (
            '有什么事我\n',
            '会联络协会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，两人都要小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5160')

    def _loc_510C(): pass

    label('loc_510C')

    ChrTalk(
        0x00FE,
        (
            '今天早上起床的时候\n',
            '发现导力灯打不开了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之先想办法\n',
            '把照明问题解决了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5160(): pass

    label('loc_5160')

    TalkEnd(0x0014)

    Return()

# id: 0x000C offset: 0x5164
@scena.Code('func_0C_5164')
def func_0C_5164():
    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0xA, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x05,
        (
            (Expr.GetChrWork, 0xA, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x000A)
    ClearChrFlags(0x000A, 0x0010)
    ChrTurnDirection(0x000A, 0x0000, 0)

    ExecExpressionWithValue(
        0x000A,
        0x04,
        (
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x04,
        (
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0xA, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x05,
        (
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_51F4',
    )

    Jump('loc_5236')

    def _loc_51F4(): pass

    label('loc_51F4')

    If(
        (
            (Expr.GetChrWork, 0xA, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5210',
    )

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_5236')

    def _loc_5210(): pass

    label('loc_5210')

    If(
        (
            (Expr.GetChrWork, 0xA, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_522C',
    )

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_5236')

    def _loc_522C(): pass

    label('loc_522C')

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.GetChrWork, 0xA, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_5236(): pass

    label('loc_5236')

    ExecExpressionWithValue(
        0x000A,
        0x04,
        (
            (Expr.GetChrWork, 0x0, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrFlags(0x000A, 0x0010)

    ChrTalk(
        0x000A,
        (
            '#0050271304V#051F哟，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
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
            TXT(0x00, '【队伍组成】\n'),
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
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_52D7'),
        (-1, 'loc_5323'),
    )

    def _loc_52D7(): pass

    label('loc_52D7')

    ChrTalk(
        0x000A,
        (
            '#0050271305V#051F哦，知道了。\n',
            '要调整队伍吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_531C',
    )

    Call(0, 0x0013)

    Jump('loc_5320')

    def _loc_531C(): pass

    label('loc_531C')

    Call(0, 0x0012)

    def _loc_5320(): pass

    label('loc_5320')

    Jump('loc_537D')

    def _loc_5323(): pass

    label('loc_5323')

    ChrTalk(
        0x000A,
        (
            '#0050271306V#052F怎么，不调整了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050271307V#050F需要我的重剑时\n',
            '尽管开口吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_537D')

    def _loc_537D(): pass

    label('loc_537D')

    SetChrSubChip(0x000A, 0)
    TalkEnd(0x000A)

    Return()

# id: 0x000D offset: 0x5386
@scena.Code('func_0D_5386')
def func_0D_5386():
    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0xB, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x05,
        (
            (Expr.GetChrWork, 0xB, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x000B)
    ClearChrFlags(0x000B, 0x0010)
    ChrTurnDirection(0x000B, 0x0000, 0)

    ExecExpressionWithValue(
        0x000B,
        0x04,
        (
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x04,
        (
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0xB, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x05,
        (
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_5416',
    )

    Jump('loc_5458')

    def _loc_5416(): pass

    label('loc_5416')

    If(
        (
            (Expr.GetChrWork, 0xB, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5432',
    )

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_5458')

    def _loc_5432(): pass

    label('loc_5432')

    If(
        (
            (Expr.GetChrWork, 0xB, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_544E',
    )

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_5458')

    def _loc_544E(): pass

    label('loc_544E')

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.GetChrWork, 0xB, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_5458(): pass

    label('loc_5458')

    ExecExpressionWithValue(
        0x000B,
        0x04,
        (
            (Expr.GetChrWork, 0x0, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrFlags(0x000B, 0x0010)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_54A2',
    )

    ChrTalk(
        0x000B,
        (
            '◆没有台词。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0013)

    Jump('loc_5736')

    def _loc_54A2(): pass

    label('loc_54A2')

    If(
        (
            (Expr.Eval, "OP_29(0x0076, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_54F4',
    )

    ChrTalk(
        0x000B,
        (
            '#0041050030V#038F唔唔……诸位。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0041050031V有、有什么事……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_554D')

    def _loc_54F4(): pass

    label('loc_54F4')

    ChrTalk(
        0x000B,
        (
            '#0040240123V#030F呀，诸位。\n',
            '贵安。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040311416V看来好像有事……\n',
            '不过先来一曲怎样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_554D(): pass

    label('loc_554D')

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
            TXT(0x00, '【队伍组成】\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.Eval, "OP_29(0x0076, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_566F',
    )

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_55B0'),
        (-1, 'loc_560B'),
    )

    def _loc_55B0(): pass

    label('loc_55B0')

    ChrTalk(
        0x000B,
        (
            '#0040240128V#037F呵，原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040240129V看来是需要\n',
            '我这个天才的力量啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0012)

    Jump('loc_566C')

    def _loc_560B(): pass

    label('loc_560B')

    ChrTalk(
        0x000B,
        (
            '#0040271287V#037F哎呀，不要我了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040271288V呼，思恋我美妙的琴声时，\n',
            '尽管来找我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_566C')

    def _loc_566C(): pass

    label('loc_566C')

    Jump('loc_5736')

    def _loc_566F(): pass

    label('loc_566F')

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_567C'),
        (-1, 'loc_56D5'),
    )

    def _loc_567C(): pass

    label('loc_567C')

    ChrTalk(
        0x000B,
        (
            '#0040240128V#030F呵，原来如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040240129V看来是需要\n',
            '我这个天才的力量啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0012)

    Jump('loc_5736')

    def _loc_56D5(): pass

    label('loc_56D5')

    ChrTalk(
        0x000B,
        (
            '#0040271287V#030F哎呀，不要我了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040271288V呼，思恋我美妙的琴声时，\n',
            '尽管来找我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5736')

    def _loc_5736(): pass

    label('loc_5736')

    SetChrSubChip(0x000B, 0)
    TalkEnd(0x000B)

    Return()

# id: 0x000E offset: 0x573F
@scena.Code('func_0E_573F')
def func_0E_573F():
    TalkBegin(0x000C)

    ChrTalk(
        0x000C,
        (
            '#0060231330V#040F各位，辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060231331V有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
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
            TXT(0x00, '【队伍组成】\n'),
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
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_57DA'),
        (-1, 'loc_580F'),
    )

    def _loc_57DA(): pass

    label('loc_57DA')

    ChrTalk(
        0x000C,
        (
            '#0060231332V#040F明白了。\n',
            '要调整队伍吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0012)

    Jump('loc_585C')

    def _loc_580F(): pass

    label('loc_580F')

    ChrTalk(
        0x000C,
        (
            '#0060231333V#040F我在这里待命。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060231334V如果有事，\n',
            '请尽管开口。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_585C')

    def _loc_585C(): pass

    label('loc_585C')

    TalkEnd(0x000C)

    Return()

# id: 0x000F offset: 0x5860
@scena.Code('func_0F_5860')
def func_0F_5860():
    TalkBegin(0x000D)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_58B9',
    )

    ChrTalk(
        0x000D,
        (
            '#0070271308V#560F啊，阿加特哥哥。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070271309V那个，有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5950')

    def _loc_58B9(): pass

    label('loc_58B9')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_5905',
    )

    ChrTalk(
        0x000D,
        (
            '#0070271310V#060F啊、姐姐，是你们啊。\n',
            '怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5950')

    def _loc_5905(): pass

    label('loc_5905')

    ChrTalk(
        0x000D,
        (
            '#0070271311V#060F啊、姐姐，是你们啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070271309V那个，有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5950(): pass

    label('loc_5950')

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
            TXT(0x00, '【队伍组成】\n'),
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
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_59A9'),
        (-1, 'loc_5A43'),
    )

    def _loc_59A9(): pass

    label('loc_59A9')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_59F7',
    )

    ChrTalk(
        0x000D,
        (
            '#0070271313V#060F啊，嗯，明白了。\n',
            '要调整队伍吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5A29')

    def _loc_59F7(): pass

    label('loc_59F7')

    ChrTalk(
        0x000D,
        (
            '#0070271314V#560F啊，明白了。\n',
            '要调整队伍吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5A29(): pass

    label('loc_5A29')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5A3C',
    )

    Call(0, 0x0013)

    Jump('loc_5A40')

    def _loc_5A3C(): pass

    label('loc_5A3C')

    Call(0, 0x0012)

    def _loc_5A40(): pass

    label('loc_5A40')

    Jump('loc_5B20')

    def _loc_5A43(): pass

    label('loc_5A43')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_5ABC',
    )

    ChrTalk(
        0x000D,
        (
            '#0070271319V#064F咦，又不要了吗……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070271320V#060F我就在这里等，\n',
            '有什么事就来找我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5B1D')

    def _loc_5ABC(): pass

    label('loc_5ABC')

    ChrTalk(
        0x000D,
        (
            '#0070271319V#064F咦，又不要了吗……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070271322V#060F我会在这里等的，\n',
            '随时都可以来找我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5B1D(): pass

    label('loc_5B1D')

    Jump('loc_5B20')

    def _loc_5B20(): pass

    label('loc_5B20')

    TalkEnd(0x000D)

    Return()

# id: 0x0010 offset: 0x5B24
@scena.Code('func_10_5B24')
def func_10_5B24():
    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0xE, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x05,
        (
            (Expr.GetChrWork, 0xE, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x000E)
    ClearChrFlags(0x000E, 0x0010)
    ChrTurnDirection(0x000E, 0x0000, 0)

    ExecExpressionWithValue(
        0x000E,
        0x04,
        (
            (Expr.GetChrWork, 0xE, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x04,
        (
            (Expr.GetChrWork, 0xE, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0xE, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x05,
        (
            (Expr.GetChrWork, 0xE, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xE, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0xE, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0xE, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0xE, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_5BB4',
    )

    Jump('loc_5BF6')

    def _loc_5BB4(): pass

    label('loc_5BB4')

    If(
        (
            (Expr.GetChrWork, 0xE, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5BD0',
    )

    ExecExpressionWithValue(
        0x000E,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_5BF6')

    def _loc_5BD0(): pass

    label('loc_5BD0')

    If(
        (
            (Expr.GetChrWork, 0xE, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_5BEC',
    )

    ExecExpressionWithValue(
        0x000E,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_5BF6')

    def _loc_5BEC(): pass

    label('loc_5BEC')

    ExecExpressionWithValue(
        0x000E,
        0x08,
        (
            (Expr.GetChrWork, 0xE, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_5BF6(): pass

    label('loc_5BF6')

    ExecExpressionWithValue(
        0x000E,
        0x04,
        (
            (Expr.GetChrWork, 0x0, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrFlags(0x000E, 0x0010)

    ChrTalk(
        0x000E,
        (
            '#0080271327V#070F哦，情况怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
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
            TXT(0x00, '【队伍组成】\n'),
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
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_5C9B'),
        (-1, 'loc_5CDA'),
    )

    def _loc_5C9B(): pass

    label('loc_5C9B')

    ChrTalk(
        0x000E,
        (
            '#0080271328V#070F要调整队伍吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5CD3',
    )

    Call(0, 0x0013)

    Jump('loc_5CD7')

    def _loc_5CD3(): pass

    label('loc_5CD3')

    Call(0, 0x0012)

    def _loc_5CD7(): pass

    label('loc_5CD7')

    Jump('loc_5D15')

    def _loc_5CDA(): pass

    label('loc_5CDA')

    ChrTalk(
        0x000E,
        (
            '#0080291560V#070F我在这里等。\n',
            '需要的时候就说一声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5D15')

    def _loc_5D15(): pass

    label('loc_5D15')

    SetChrSubChip(0x000E, 0)
    TalkEnd(0x000E)

    Return()

# id: 0x0011 offset: 0x5D1E
@scena.Code('func_11_5D1E')
def func_11_5D1E():
    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0x9, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x05,
        (
            (Expr.GetChrWork, 0x9, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x0009)
    ClearChrFlags(0x0009, 0x0010)
    ChrTurnDirection(0x0009, 0x0000, 0)

    ExecExpressionWithValue(
        0x0009,
        0x04,
        (
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x04,
        (
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0x9, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x05,
        (
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0x9, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_5DAE',
    )

    Jump('loc_5DF0')

    def _loc_5DAE(): pass

    label('loc_5DAE')

    If(
        (
            (Expr.GetChrWork, 0x9, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5DCA',
    )

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_5DF0')

    def _loc_5DCA(): pass

    label('loc_5DCA')

    If(
        (
            (Expr.GetChrWork, 0x9, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_5DE6',
    )

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_5DF0')

    def _loc_5DE6(): pass

    label('loc_5DE6')

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.GetChrWork, 0x9, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_5DF0(): pass

    label('loc_5DF0')

    ExecExpressionWithValue(
        0x0009,
        0x04,
        (
            (Expr.GetChrWork, 0x0, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrFlags(0x0009, 0x0010)

    ChrTalk(
        0x0009,
        (
            '#0030271323V#020F嗯，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
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
            TXT(0x00, '【队伍组成】\n'),
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
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_5E91'),
        (-1, 'loc_5EC3'),
    )

    def _loc_5E91(): pass

    label('loc_5E91')

    ChrTalk(
        0x0009,
        (
            '#0030271324V#020F哎呀，要调整队伍吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0013)

    Jump('loc_5F18')

    def _loc_5EC3(): pass

    label('loc_5EC3')

    ChrTalk(
        0x0009,
        (
            '#0030271325V#020F呵呵，我就在这儿\n',
            '休息吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030271326V那么，之后就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5F18')

    def _loc_5F18(): pass

    label('loc_5F18')

    SetChrSubChip(0x0009, 0)
    TalkEnd(0x0009)

    Return()

# id: 0x0012 offset: 0x5F21
@scena.Code('func_12_5F21')
def func_12_5F21():
    OP_C9(
        0x01,
        (
            0x0000,
            0x0002,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0003,
            0x0004,
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

    Fade(1000)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000E, 0x0080)

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5F8C',
    )

    ClearChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000A, 0x0004)
    SetChrChipByIndex(0x000A, 8)
    SetChrPos(0x000A, -790, 200, 69820, 360)

    def _loc_5F8C(): pass

    label('loc_5F8C')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5FD5',
    )

    ClearChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000B, 0x0004)

    If(
        (
            (Expr.Eval, "OP_29(0x0076, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_5FBF',
    )

    SetChrFlags(0x000B, 0x0002)
    SetChrSubChip(0x000B, 0)
    SetChrChipByIndex(0x000B, 18)

    Jump('loc_5FC4')

    def _loc_5FBF(): pass

    label('loc_5FBF')

    SetChrChipByIndex(0x000B, 9)

    def _loc_5FC4(): pass

    label('loc_5FC4')

    SetChrPos(0x000B, 1060, 200, 69820, 360)

    def _loc_5FD5(): pass

    label('loc_5FD5')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5FF8',
    )

    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x000C, -1940, 0, 74490, 360)

    def _loc_5FF8(): pass

    label('loc_5FF8')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_601B',
    )

    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, -4290, 0, 73800, 360)

    def _loc_601B(): pass

    label('loc_601B')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_6048',
    )

    ClearChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000E, 0x0004)
    SetChrChipByIndex(0x000E, 10)
    SetChrPos(0x000E, 140, 200, 71510, 180)

    def _loc_6048(): pass

    label('loc_6048')

    OP_0D()

    Return()

# id: 0x0013 offset: 0x604A
@scena.Code('func_13_604A')
def func_13_604A():
    OP_C9(
        0x01,
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

    Fade(1000)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000E, 0x0080)
    OP_A3(0x0000)

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_60E7',
    )

    ClearChrFlags(0x0009, 0x0080)
    SetChrFlags(0x0009, 0x0004)
    SetChrChipByIndex(0x0009, 7)
    SetChrPos(0x0009, 1060, 200, 69820, 360)

    If(
        (
            (Expr.Eval, "OP_D5(0x02, 0x03)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_60CC',
    )

    EquipCmd(ChrTable['雪拉扎德'], 0x0000, 0x03)
    AddItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x0000)

    def _loc_60CC(): pass

    label('loc_60CC')

    If(
        (
            (Expr.Eval, "OP_D5(0x02, 0x04)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_60E7',
    )

    EquipCmd(ChrTable['雪拉扎德'], 0x0000, 0x04)
    AddItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x0000)

    def _loc_60E7(): pass

    label('loc_60E7')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_614A',
    )

    ClearChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000A, 0x0004)
    SetChrChipByIndex(0x000A, 8)
    SetChrPos(0x000A, -790, 200, 69820, 360)

    If(
        (
            (Expr.Eval, "OP_D5(0x05, 0x03)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_612F',
    )

    EquipCmd(ChrTable['阿加特'], 0x0000, 0x03)
    AddItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x0000)

    def _loc_612F(): pass

    label('loc_612F')

    If(
        (
            (Expr.Eval, "OP_D5(0x05, 0x04)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_614A',
    )

    EquipCmd(ChrTable['阿加特'], 0x0000, 0x04)
    AddItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x0000)

    def _loc_614A(): pass

    label('loc_614A')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_61A3',
    )

    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, -4290, 0, 73800, 360)

    If(
        (
            (Expr.Eval, "OP_D5(0x06, 0x03)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6188',
    )

    EquipCmd(ChrTable['提妲'], 0x0000, 0x03)
    AddItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x0000)

    def _loc_6188(): pass

    label('loc_6188')

    If(
        (
            (Expr.Eval, "OP_D5(0x06, 0x04)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_61A3',
    )

    EquipCmd(ChrTable['提妲'], 0x0000, 0x04)
    AddItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x0000)

    def _loc_61A3(): pass

    label('loc_61A3')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_6206',
    )

    ClearChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000E, 0x0004)
    SetChrChipByIndex(0x000E, 10)
    SetChrPos(0x000E, 140, 200, 71510, 180)

    If(
        (
            (Expr.Eval, "OP_D5(0x07, 0x03)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_61EB',
    )

    EquipCmd(ChrTable['金'], 0x0000, 0x03)
    AddItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x0000)

    def _loc_61EB(): pass

    label('loc_61EB')

    If(
        (
            (Expr.Eval, "OP_D5(0x07, 0x04)"),
            (Expr.PushLong, 0x151),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6206',
    )

    EquipCmd(ChrTable['金'], 0x0000, 0x04)
    AddItem(ItemTable['零力场发生器'], 1)
    OP_A2(0x0000)

    def _loc_6206(): pass

    label('loc_6206')

    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_6283',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※要待命的成员\n',
            '　装备着『零力场发生器』。\n',
            '　将其回收加入队伍的携带品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    def _loc_6283(): pass

    label('loc_6283')

    Return()

# id: 0x0014 offset: 0x6284
@scena.Code('func_14_6284')
def func_14_6284():
    EventBegin(0x00)
    OP_4A(0x0010, 255)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_631C',
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
            TXT(0x00, '【◇和里农第一次重逢】\n'),
            TXT(0x01, '【◇已经见过里农】\n'),
            TXT(0x02, '【◇不变更】\n'),
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
        (0x00000000, 'loc_6310'),
        (0x00000001, 'loc_6316'),
        (-1, 'loc_631C'),
    )

    def _loc_6310(): pass

    label('loc_6310')

    OP_A3(0x1885)

    Jump('loc_631C')

    def _loc_6316(): pass

    label('loc_6316')

    OP_A2(0x1885)

    Jump('loc_631C')

    def _loc_631C(): pass

    label('loc_631C')

    Fade(1000)
    OP_6D(4490, 0, 1340, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0101, 3390, 0, 50, 0)
    SetChrPos(0x0103, 4490, 0, 50, 0)
    SetChrPos(0x0107, 3240, 0, -1100, 0)
    SetChrPos(0x0105, 4350, 0, -1100, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0310, 5, 0x1885)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_653C',
    )

    ChrTalk(
        0x0010,
        (
            '#0870290339V#5P哦！\n',
            '艾丝蒂尔，终于来了啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290340V#1017F里农先生……\n',
            '嘿嘿，好久不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0870290341V#5P呀～从客人那里\n',
            '说你回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0870290342V#5P我一直期待\n',
            '你什么时候过来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290343V#1025F这样啊。\n',
            '抱歉这么晚才来打招呼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0870290344V#5P哪里哪里，没关系啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0870290345V#5P不过时机真是不好，\n',
            '回来的可真不是时候啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0870290346V#5P今天雾还是这么大啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6595')

    def _loc_653C(): pass

    label('loc_653C')

    ChrTalk(
        0x0010,
        (
            '#0870290347V#5P早啊，艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0870290348V#5P呀～\n',
            '今天一大早雾还是这么大啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6595(): pass

    label('loc_6595')

    ChrTalk(
        0x0101,
        (
            '#0010290349V#1007F是啊，没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290350V#1015F话说回来……\n',
            '昨天晚上没什么事吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290351V没发生什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0870290352V#5P？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0870290353V#5P不，起床后没发现\n',
            '有什么特别的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0870290354V#5P啊啊，睡觉前\n',
            '有个红头发的游击士来过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0870290355V#5P说是在巡逻，\n',
            '是你们的伙伴吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290356V#1006F啊，嗯。\n',
            '他叫阿加特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290357V#027F呵呵，看来\n',
            '很认真的在巡逻呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070290358V#064F#6P对了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070290359V#560F对了，姐姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070290360V要不要给阿加特哥哥他们\n',
            '买些吃的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_67BA')
    def lambda_67BA():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_67BA)

    Sleep(100)

    @scena.Lambda('lambda_67CD')
    def lambda_67CD():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_67CD)

    Sleep(100)

    @scena.Lambda('lambda_67E0')
    def lambda_67E0():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_67E0)

    Sleep(200)

    ChrTalk(
        0x0101,
        (
            '#0010290361V#1018F#5P啊……\n',
            '提妲，Nice idea！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060290362V#048F#2P呵呵，这样的话……\n',
            '好像甜食比较好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060290363V累的时候\n',
            '男人也会喜欢甜食的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0870290364V#5P那就推荐\n',
            '刚刚到货的巧克力吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0870290365V#5P微苦的味道也很适合男性。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#5P１个２００米拉就好哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_690C')
    def lambda_690C():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_690C)

    Sleep(100)

    @scena.Lambda('lambda_691F')
    def lambda_691F():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_691F)

    Sleep(100)

    @scena.Lambda('lambda_6932')
    def lambda_6932():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_6932)

    Sleep(200)

    ChrTalk(
        0x0101,
        (
            '#1006F这么说，\n',
            '３个就是６００米拉吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '话说奥利维尔\n',
            '有没有乖乖巡逻…\n',
            '真令人怀疑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#045F好啦好啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060290369V#542F那么就怀着感谢的心情\n',
            '大家一起付钱吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070290370V#061F#6P好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290371V#021F呵呵，偶尔\n',
            '这样也不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
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
            TXT(0x00, '【出１５０米拉】\n'),
            TXT(0x01, '【不出】\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6B13',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x12),
            (Expr.PushLong, 0x96),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_6AA5',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_6B13')

    def _loc_6AA5(): pass

    label('loc_6AA5')

    ChrTalk(
        0x0010,
        (
            '#0870290372V#5P给，谢谢惠顾！',
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
            '得到３个',
            (TxtCtl.Item, ItemTable['黑巧克力']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['黑巧克力'], 3)
    SubMira(150)

    def _loc_6B13(): pass

    label('loc_6B13')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6C1C',
    )

    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030290373V#023F#2P哎呀……\n',
            '钱不够吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290374V#025F没办法了。\n',
            '我先垫着吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0870290372V#5P给，谢谢惠顾！',
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
            '得到３个',
            (TxtCtl.Item, ItemTable['黑巧克力']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['黑巧克力'], 3)

    ChrTalk(
        0x0101,
        (
            '#0010290376V#1019F（呜……\n',
            '总觉得挺内疚的。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6C1C(): pass

    label('loc_6C1C')

    OP_A2(0x000A)
    OP_A2(0x181D)
    OP_A2(0x1885)
    OP_4B(0x0010, 255)
    EventEnd(0x00)

    Return()

# id: 0x0015 offset: 0x6C2C
@scena.Code('func_15_6C2C')
def func_15_6C2C():
    EventBegin(0x00)
    OP_4A(0x0008, 255)
    OP_6D(160, 0, 117520, 0)
    OP_67(0, 6400, -10000, 0)
    OP_6B(2790, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x0101, 0x0004)
    SetChrFlags(0x0107, 0x0004)
    SetChrFlags(0x0103, 0x0004)
    SetChrFlags(0x0105, 0x0004)
    SetChrPos(0x0101, 4410, 0, 109480, 0)
    SetChrPos(0x0107, 4410, 0, 109480, 0)
    SetChrPos(0x0103, 4410, 0, 109480, 0)
    SetChrPos(0x0105, 4410, 0, 109480, 0)
    SetChrPos(0x000A, 300, 0, 116600, 0)
    SetChrPos(0x000E, 1600, 0, 116590, 0)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(300)

    OP_22(0x0006, 0x00, 0x64)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010290377V#2P早～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_6D2D')
    def lambda_6D2D():
        ChrTurnDirection(0x000A, 0x0101, 400)
        Yield()

        Jump('lambda_6D2D')

    DispatchAsync2(0x000A, 0x0001, lambda_6D2D)

    @scena.Lambda('lambda_6D3E')
    def lambda_6D3E():
        ChrTurnDirection(0x000E, 0x0103, 400)
        Yield()

        Jump('lambda_6D3E')

    DispatchAsync2(0x000E, 0x0001, lambda_6D3E)

    ChrTalk(
        0x0107,
        (
            '#0070290378V#5P早安。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_6D6A')
    def lambda_6D6A():
        OP_6D(-150, 0, 116560, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_6D6A)

    CreateThread(0x0101, 0x01, 0x00, 0x0016)
    Sleep(700)

    CreateThread(0x0103, 0x01, 0x00, 0x0017)
    Sleep(700)

    CreateThread(0x0107, 0x01, 0x00, 0x0018)
    Sleep(700)

    CreateThread(0x0105, 0x01, 0x00, 0x0019)
    WaitForThreadExit(0x0105, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    ClearChrFlags(0x0101, 0x0004)
    ClearChrFlags(0x0107, 0x0004)
    ClearChrFlags(0x0103, 0x0004)
    ClearChrFlags(0x0105, 0x0004)
    TerminateThread(0x000A, 0x01)
    TerminateThread(0x000E, 0x01)

    ChrTalk(
        0x0008,
        (
            '#0350290379V#740F呀，早。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050290380V#051F#5P哦，来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0080290381V#070F#2P昨晚睡得好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290382V#1006F#6P啊，嗯。\n',
            '完全消除疲劳了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290383V#524F#6P谢谢你们俩了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290384V夜晚的巡逻，\n',
            '很辛苦吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070290385V#560F#6P那个那个。\n',
            '你们…辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0080290386V#071F#2P哪里，我们交班的时候\n',
            '都稍微睡了一下，不要紧的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050290387V#051F#5P虽说有个家伙\n',
            '现在还在旅馆呼呼大睡。',
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
        'loc_7012',
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
            TXT(0x00, '【◇在旅店没看到奥利维尔】\n'),
            TXT(0x01, '【◇在旅店看到了奥利维尔】\n'),
            TXT(0x02, '【◇不变更】\n'),
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
        (0x00000000, 'loc_7006'),
        (0x00000001, 'loc_700C'),
        (-1, 'loc_7012'),
    )

    def _loc_7006(): pass

    label('loc_7006')

    OP_A3(0x1886)

    Jump('loc_7012')

    def _loc_700C(): pass

    label('loc_700C')

    OP_A2(0x1886)

    Jump('loc_7012')

    def _loc_7012(): pass

    label('loc_7012')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0310, 6, 0x1886)),
            Expr.Return,
        ),
        'loc_70AB',
    )

    ChrTalk(
        0x0105,
        (
            '#0060290388V#542F#6P啊，是奥利维尔啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290389V#1006F#6P刚才看到他\n',
            '在旅馆里呼呼大睡呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290390V奥利维尔他\n',
            '也参加了巡逻吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7114')

    def _loc_70AB(): pass

    label('loc_70AB')

    ChrTalk(
        0x0105,
        (
            '#0060290391V#542F#6P啊……\n',
            '是奥利维尔吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290392V#1004F#6P咦，奥利维尔他也\n',
            '参加了巡逻吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7114(): pass

    label('loc_7114')

    ChrTalk(
        0x000E,
        (
            '#0080290393V#070F#2P哈哈，算是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080290394V虽说牢骚满腹，\n',
            '该做的事还是做得好好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290395V#021F#6P呵呵，待会儿\n',
            '得向他道谢才行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290396V#022F说回来……\n',
            '情况怎样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350290397V#744F多亏进行巡逻了，\n',
            '再没有昏睡的人出现。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350290398V#742F只是，昨天昏睡的人\n',
            '今天早上也没清醒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290399V#1007F#6P是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070290400V#063F#6P真担心啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290401V#022F#6P雾的情况怎样了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290402V和昨天比…\n',
            '感觉好像更浓了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350290403V#742F嗯嗯……\n',
            '浓度好象上升了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350290404V与之相应\n',
            '产生范围好象也扩大了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350290405V#744F直至玛鲁加山道尽头，\n',
            '几乎整个地区都被笼罩在雾里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290406V#1002F#6P这、这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060290407V#043F#6P看来情况\n',
            '越来越严重了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350290408V#740F也不光是坏消息。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350290409V接到我们的报告，\n',
            '军队决定派遣部队了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350290410V为了警备洛连特市。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290411V#1018F#6P真的！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350290412V#741F嗯嗯，威尔特桥方面已经\n',
            '派了两个小队来这边了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290413V#021F#6P这真令人振奋。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290414V城市交给军队的话，\n',
            '我们也能自由行动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050290415V#051F#5P啊啊，没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050290416V必须赶快找到『结社』的\n',
            '那些家伙并制服他们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0080290417V#074F#2P嗯，应该潜伏在\n',
            '洛连特近郊吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080290418V#072F不过现在还没有线索。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290419V#1007F#6P洛连特地方虽小，\n',
            '但也不可能调查到每一个角落……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290420V#1015F嗯……没什么\n',
            '具体能做的事吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350290421V#740F话虽如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350290422V首先协助\n',
            '民众避难如何。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290423V#1004F#6P民众避难？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350290424V#744F昏睡事件在雾的产生范围内\n',
            '再发生的可能性很高。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350290425V#742F而今天早上，\n',
            '这发生范围还更广了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350290426V连帕赛尔农场和玛鲁加矿山\n',
            '都覆盖到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290427V#1020F#6P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290428V#026F#6P原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290429V#020F要保证农场一家\n',
            '和矿工的安全吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350290430V#740F嗯嗯，这也是协会\n',
            '肩负的义务啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350290431V寻找敌人的所在处之前，\n',
            '能先处理这件工作吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050290432V#053F#5P没办法……\n',
            '看来这边优先啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0080290433V#070F#2P矿山和农场\n',
            '相隔好像比较远啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080290434V既然如此，就这样\n',
            '兵分两路比较好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290435V#027F#6P嗯嗯，这样比较有效率。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290436V#1015F#6P那，那样的话…\n',
            '我们去农场行不行？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290437V那是我朋友的家……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0080290438V#073F#2P哦，这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080290439V#070F那么我们\n',
            '去矿山吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050290440V#051F#5P啊啊，就这么定了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050290441V把奥利维尔那家伙叫起来，\n',
            '赶快出发吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x0006, 0x00, 0x64)
    Sleep(500)

    OP_22(0x00BE, 0x00, 0x64)
    Sleep(2000)

    SetChrPos(0x000B, 4250, 0, 108920, 0)

    NpcTalk(
        0x000B,
        '青年的声音',
        (
            '#0040290442V#2P呵呵，叫我？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9F(0x000B, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    SetChrChipByIndex(0x000B, 15)
    SetChrSubChip(0x000B, 0)
    ClearChrFlags(0x000B, 0x0080)

    @scena.Lambda('lambda_7AA0')
    def lambda_7AA0():
        OP_6D(2550, 0, 112570, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_7AA0)

    @scena.Lambda('lambda_7AB8')
    def lambda_7AB8():
        ChrTurnDirection(0x00FE, 0x000B, 400)
        Yield()

        Jump('lambda_7AB8')

    DispatchAsync2(0x0101, 0x0001, lambda_7AB8)

    Sleep(50)

    @scena.Lambda('lambda_7ACE')
    def lambda_7ACE():
        ChrTurnDirection(0x00FE, 0x000B, 400)
        Yield()

        Jump('lambda_7ACE')

    DispatchAsync2(0x000A, 0x0001, lambda_7ACE)

    Sleep(50)

    @scena.Lambda('lambda_7AE4')
    def lambda_7AE4():
        ChrTurnDirection(0x00FE, 0x000B, 400)
        Yield()

        Jump('lambda_7AE4')

    DispatchAsync2(0x0103, 0x0001, lambda_7AE4)

    Sleep(50)

    @scena.Lambda('lambda_7AFA')
    def lambda_7AFA():
        ChrTurnDirection(0x00FE, 0x000B, 400)
        Yield()

        Jump('lambda_7AFA')

    DispatchAsync2(0x000E, 0x0001, lambda_7AFA)

    Sleep(50)

    @scena.Lambda('lambda_7B10')
    def lambda_7B10():
        ChrTurnDirection(0x00FE, 0x000B, 400)
        Yield()

        Jump('lambda_7B10')

    DispatchAsync2(0x0107, 0x0001, lambda_7B10)

    Sleep(50)

    @scena.Lambda('lambda_7B26')
    def lambda_7B26():
        ChrTurnDirection(0x00FE, 0x000B, 400)
        Yield()

        Jump('lambda_7B26')

    DispatchAsync2(0x0105, 0x0001, lambda_7B26)

    Sleep(100)

    WaitForThreadExit(0x0101, 0x0000)
    CreateThread(0x000B, 0x01, 0x00, 0x001A)
    Sleep(500)

    @scena.Lambda('lambda_7B4D')
    def lambda_7B4D():
        OP_6D(650, 0, 116600, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_7B4D)

    WaitForThreadExit(0x000B, 0x0001)
    TerminateThread(0x000A, 0x01)
    TerminateThread(0x000E, 0x01)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0103, 0x01)
    TerminateThread(0x0107, 0x01)
    TerminateThread(0x0105, 0x01)
    OP_8C(0x0103, 180, 0)
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x000E,
        (
            '#0080290443V#071F#2P哦哦，起来啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290444V#1007F#5P干嘛还特地\n',
            '弹琴……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0040290445V#031F哈哈哈。\n',
            '因为今早天气也很不好嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040290446V至少希望用我华丽的演奏\n',
            '让气氛明快一点……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040290447V就当是我这名音乐家\n',
            '独特而美丽演出吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050290448V#551F#5P真是的，一大早\n',
            '情绪就这么高涨。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290449V#1006F#5P不过，奥利维尔\n',
            '似乎也认真巡逻了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290450V对你有点改观了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290451V#021F#2P呵呵，是啊。\n',
            '辛苦你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0040290452V#031F哈哈哈。\n',
            '作为绅士这是当然的义务啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040290453V#030F原本打算在\n',
            '巡逻的时候\n',
            '去艾丝蒂尔家打扰的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040290454V#034F但是视线比想象中更差，\n',
            '只好忍痛放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290455V#1019F#5P真是的……\n',
            '刚想改观就这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350290456V#740F那么，向奥利维尔\n',
            '简单说明情况吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_6D(10, 0, 116530, 0)
    OP_67(0, 6400, -10000, 0)
    OP_6B(2790, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x000B, -890, 0, 116590, 135)
    OP_8C(0x0101, 0, 0)
    OP_8C(0x0103, 0, 0)
    OP_8C(0x0107, 0, 0)
    OP_8C(0x0105, 0, 0)
    Sleep(1000)

    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000B,
        (
            '#0040290457V#033F#5P嗯，怎么说\n',
            '这都是游击士协会的工作呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040290458V#030F好吧。\n',
            '我也来帮忙吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040290459V#031F那么你们\n',
            '带我去农场吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x000B, 400)

    ChrTalk(
        0x000A,
        (
            '#0050290460V#555F#6P都～说你是\n',
            '和我们一起的～～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050290461V你就是来故意捣乱的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x000A, 400)

    ChrTalk(
        0x000B,
        (
            '#0040290462V#031F#5P讨厌啦，那么\n',
            '想和我在一起啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040290463V#037F阿加特兄真可爱㈱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050290464V#055F#6P少恶心了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(500)

    ChrTalk(
        0x0107,
        (
            '#0070290465V#065F#6P啊哇哇……\n',
            '真是、是这样吗～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0107, 400)

    ChrTalk(
        0x000A,
        (
            '#0050290466V#055F#5P啊～！\n',
            '这你都相信啊～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290467V#1007F#6P啊哈哈，感觉轻松了很多呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290468V#021F#6P呵呵……\n',
            '总比越来越沉重要好吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290469V#027F不过我们都还是\n',
            '赶快完成工作比较好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050290470V#551F#5P啊啊，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0080290471V#070F#2P那么我们\n',
            '就去矿山啦。',
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
        'loc_8275',
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
            TXT(0x00, '【◇没买巧克力】\n'),
            TXT(0x01, '【◇买了巧克力】\n'),
            TXT(0x02, '【◇不变更】\n'),
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
        (0x00000000, 'loc_8269'),
        (0x00000001, 'loc_826F'),
        (-1, 'loc_8275'),
    )

    def _loc_8269(): pass

    label('loc_8269')

    OP_A3(0x181D)

    Jump('loc_8275')

    def _loc_826F(): pass

    label('loc_826F')

    OP_A2(0x181D)

    Jump('loc_8275')

    def _loc_8275(): pass

    label('loc_8275')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 5, 0x181D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_830F',
    )

    ChrTurnDirection(0x000B, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x000B,
        (
            '#0040290472V#031F#5P呼，暂时要分别了。\n',
            '我可爱的小猫咪们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_82CE')
    def lambda_82CE():
        ChrTurnDirection(0x00FE, 0x000B, 400)
        Yield()

        Jump('lambda_82CE')

    DispatchAsync2(0x0101, 0x0001, lambda_82CE)

    @scena.Lambda('lambda_82DF')
    def lambda_82DF():
        ChrTurnDirection(0x00FE, 0x000B, 400)
        Yield()

        Jump('lambda_82DF')

    DispatchAsync2(0x0103, 0x0001, lambda_82DF)

    @scena.Lambda('lambda_82F0')
    def lambda_82F0():
        ChrTurnDirection(0x00FE, 0x000B, 400)
        Yield()

        Jump('lambda_82F0')

    DispatchAsync2(0x0105, 0x0001, lambda_82F0)

    @scena.Lambda('lambda_8301')
    def lambda_8301():
        ChrTurnDirection(0x00FE, 0x000B, 400)
        Yield()

        Jump('lambda_8301')

    DispatchAsync2(0x0107, 0x0001, lambda_8301)

    Jump('loc_89C0')

    def _loc_830F(): pass

    label('loc_830F')

    ChrTalk(
        0x0107,
        (
            '#0070290473V#064F#6P啊……\n',
            '姐姐，那些吃的啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(800)

    ChrTurnDirection(0x0101, 0x0107, 400)

    @scena.Lambda('lambda_8366')
    def lambda_8366():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_8366)

    @scena.Lambda('lambda_8374')
    def lambda_8374():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_8374)

    @scena.Lambda('lambda_8382')
    def lambda_8382():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_8382)

    ChrTalk(
        0x0101,
        (
            '#0010290474V#1006F#5P啊，是哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050290475V#052F#5P？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0080290476V#073F#2P怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8F(0x0101, 710, 0, 114500, 1500, 0x00)
    Sleep(500)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔把巧克力的包包递给提妲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    RemoveItem(ItemTable['黑巧克力'], 3)

    ChrTalk(
        0x0101,
        (
            '#0010290477V#1001F#5P快快。\n',
            '发起人来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070290478V#560F#6P嗯、嗯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_84B4')
    def lambda_84B4():
        OP_8F(0x00FE, -340, 0, 114780, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_84B4)

    @scena.Lambda('lambda_84CF')
    def lambda_84CF():
        OP_8C(0x00FE, 90, 200)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_84CF)

    Sleep(500)

    @scena.Lambda('lambda_84E2')
    def lambda_84E2():
        OP_8C(0x00FE, 315, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_84E2)

    @scena.Lambda('lambda_84F0')
    def lambda_84F0():
        OP_8C(0x00FE, 315, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_84F0)

    @scena.Lambda('lambda_84FE')
    def lambda_84FE():
        OP_8F(0x00FE, 470, 0, 115140, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_84FE)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_851E')
    def lambda_851E():
        OP_8C(0x00FE, 0, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_851E)

    WaitForThreadExit(0x0107, 0x0001)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0103, 0x01)
    TerminateThread(0x0105, 0x01)
    Sleep(500)

    ChrTalk(
        0x0107,
        (
            '#0070290479V#560F#6P阿加特哥哥、\n',
            '金先生，奥利维尔先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070290480V昨天真是\n',
            '辛苦你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070290481V#061F那个那个……\n',
            '这个，是慰劳品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8F(0x0107, 470, 0, 115770, 1500, 0x00)
    Sleep(500)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '提妲把黑巧克力交给了阿加特等人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    @scena.Lambda('lambda_863A')
    def lambda_863A():
        OP_8F(0x00FE, 470, 0, 115400, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_863A)

    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0050290482V#055F#5P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0040290483V#033F#5P哦哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0080290484V#073F#2P呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290485V#021F#6P呵呵，一点小意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060290486V#048F#6P钱也是大家\n',
            '一起出的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290487V#1006F#6P嗯，你们可要\n',
            '好好品尝哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0080290488V#071F#2P呀，疲劳的时候\n',
            '收到甜食做慰劳真令人高兴啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0040290489V#031F#5P呵，你们甜美的爱，\n',
            '我就收下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050290490V#555F#5P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070290491V#065F#6P啊，阿加特哥哥……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060290492V#043F#6P难不成\n',
            '你不喜欢吃甜食？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050290493V#552F#5P不……\n',
            '不至于不喜欢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050290494V#551F倒是你们……\n',
            '还做这么让人难为情的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290495V#1001F#6P啊哈哈，害羞啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290496V#027F#6P修行还不够呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050290497V#055F#5P啰嗦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050290498V#051F算了，肚子饿了\n',
            '我就随便吃吃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070290499V#067F#6P好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_8982')
    def lambda_8982():
        ChrTurnDirection(0x00FE, 0x000A, 400)
        Yield()

        Jump('lambda_8982')

    DispatchAsync2(0x0101, 0x0001, lambda_8982)

    @scena.Lambda('lambda_8993')
    def lambda_8993():
        ChrTurnDirection(0x00FE, 0x000A, 400)
        Yield()

        Jump('lambda_8993')

    DispatchAsync2(0x0103, 0x0001, lambda_8993)

    @scena.Lambda('lambda_89A4')
    def lambda_89A4():
        ChrTurnDirection(0x00FE, 0x000A, 400)
        Yield()

        Jump('lambda_89A4')

    DispatchAsync2(0x0105, 0x0001, lambda_89A4)

    @scena.Lambda('lambda_89B5')
    def lambda_89B5():
        ChrTurnDirection(0x00FE, 0x000A, 400)
        Yield()

        Jump('lambda_89B5')

    DispatchAsync2(0x0107, 0x0001, lambda_89B5)

    def _loc_89C0(): pass

    label('loc_89C0')

    @scena.Lambda('lambda_89C6')
    def lambda_89C6():
        OP_6D(2550, 0, 112570, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_89C6)

    CreateThread(0x000E, 0x01, 0x00, 0x001B)
    Sleep(100)

    CreateThread(0x000A, 0x01, 0x00, 0x001C)
    Sleep(700)

    CreateThread(0x000B, 0x01, 0x00, 0x001D)
    WaitForThreadExit(0x000B, 0x0001)
    WaitForThreadExit(0x0101, 0x0000)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0103, 0x01)
    TerminateThread(0x0105, 0x01)
    TerminateThread(0x0107, 0x01)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 5, 0x181D)),
            Expr.Return,
        ),
        'loc_8BCA',
    )

    @scena.Lambda('lambda_8A23')
    def lambda_8A23():
        OP_6D(-530, 0, 115950, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_8A23)

    Sleep(500)

    ChrTurnDirection(0x0101, 0x0103, 400)

    @scena.Lambda('lambda_8A47')
    def lambda_8A47():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_8A47)

    Sleep(50)

    @scena.Lambda('lambda_8A5A')
    def lambda_8A5A():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_8A5A)

    Sleep(50)

    @scena.Lambda('lambda_8A6D')
    def lambda_8A6D():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_8A6D)

    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0101,
        (
            '#0010290500V#1006F#5P好了，我们\n',
            '也向帕赛尔农场出发吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060290501V#041F嗯嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070290502V#560F#2P嗯，是姐姐的\n',
            '朋友家对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290503V#1011F#5P嗯，叫缇欧～\n',
            '是主日学校时代的好友。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290504V还有叔叔、阿姨、\n',
            '双胞胎姐弟总共５人的家族吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290505V#026F护卫对象中还有小孩，\n',
            '看来这工作不可大意了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8D74')

    def _loc_8BCA(): pass

    label('loc_8BCA')

    @scena.Lambda('lambda_8BD0')
    def lambda_8BD0():
        OP_6D(-530, 0, 115950, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_8BD0)

    Sleep(500)

    ChrTurnDirection(0x0101, 0x0105, 400)

    @scena.Lambda('lambda_8BF4')
    def lambda_8BF4():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_8BF4)

    Sleep(50)

    @scena.Lambda('lambda_8C07')
    def lambda_8C07():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_8C07)

    Sleep(50)

    @scena.Lambda('lambda_8C1A')
    def lambda_8C1A():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_8C1A)

    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0101,
        (
            '#0010290500V#1006F#5P好了，我们\n',
            '也向帕赛尔农场出发吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060290501V#041F嗯嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070290502V#560F#6P嗯，是姐姐的\n',
            '朋友家对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290503V#1011F#5P嗯，叫缇欧～\n',
            '是主日学校时代的好友。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290504V还有叔叔、阿姨、\n',
            '双胞胎姐弟总共５人的家族吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290505V#026F护卫对象中还有小孩，\n',
            '看来这工作不可大意了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8D74(): pass

    label('loc_8D74')

    ChrTurnDirection(0x0103, 0x0008, 400)

    @scena.Lambda('lambda_8D81')
    def lambda_8D81():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_8D81)

    @scena.Lambda('lambda_8D8F')
    def lambda_8D8F():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_8D8F)

    @scena.Lambda('lambda_8D9D')
    def lambda_8D9D():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_8D9D)

    ChrTalk(
        0x0103,
        (
            '#0030290506V#020F#6P那么爱娜。\n',
            '我们也走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350290507V#741F#2P嗯嗯，拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x181E)
    OP_28(0x0091, 0x04, 0x02)
    OP_28(0x0091, 0x04, 0x08)
    OP_28(0x0091, 0x01, 0x0001)
    OP_4B(0x0008, 255)
    EventEnd(0x00)

    Return()

# id: 0x0016 offset: 0x8E18
@scena.Code('func_16_8E18')
def func_16_8E18():
    OP_8E(0x00FE, 710, 0, 115000, 2500, 0x00)
    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x0017 offset: 0x8E34
@scena.Code('func_17_8E34')
def func_17_8E34():
    OP_8E(0x00FE, 2540, 0, 112550, 2500, 0x00)
    OP_8E(0x00FE, 1840, 0, 115000, 2500, 0x00)
    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x0018 offset: 0x8E64
@scena.Code('func_18_8E64')
def func_18_8E64():
    OP_8E(0x00FE, 740, 0, 113800, 2500, 0x00)
    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x0019 offset: 0x8E80
@scena.Code('func_19_8E80')
def func_19_8E80():
    OP_22(0x0007, 0x00, 0x64)
    OP_8E(0x00FE, 2540, 0, 112550, 2500, 0x00)
    OP_8E(0x00FE, 1840, 0, 113800, 2500, 0x00)
    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x001A offset: 0x8EB5
@scena.Code('func_1A_8EB5')
def func_1A_8EB5():
    @scena.Lambda('lambda_8EBB')
    def lambda_8EBB():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_8EBB)

    OP_8E(0x00FE, 3920, 0, 110550, 2000, 0x00)
    OP_8E(0x00FE, 1590, 0, 112440, 2000, 0x00)
    OP_8C(0x00FE, 0, 400)
    SetChrSubChip(0x0101, 0)

    Return()

# id: 0x001B offset: 0x8EFC
@scena.Code('func_1B_8EFC')
def func_1B_8EFC():
    OP_8E(0x00FE, 2700, 0, 116450, 2000, 0x00)
    OP_8E(0x00FE, 2620, 0, 111710, 2000, 0x00)
    OP_8E(0x00FE, 3960, 0, 109850, 2000, 0x00)

    @scena.Lambda('lambda_8F3E')
    def lambda_8F3E():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000001F4)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_8F3E)

    OP_8E(0x00FE, 4170, 0, 108510, 2000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x001C offset: 0x8F64
@scena.Code('func_1C_8F64')
def func_1C_8F64():
    OP_8E(0x00FE, 2700, 0, 116450, 2000, 0x00)
    OP_8E(0x00FE, 2620, 0, 111710, 2000, 0x00)
    OP_8E(0x00FE, 3960, 0, 109850, 2000, 0x00)

    @scena.Lambda('lambda_8FA6')
    def lambda_8FA6():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000001F4)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_8FA6)

    OP_8E(0x00FE, 4170, 0, 108510, 2000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x001D offset: 0x8FCC
@scena.Code('func_1D_8FCC')
def func_1D_8FCC():
    OP_8E(0x00FE, -970, 0, 114190, 2000, 0x00)
    OP_8E(0x00FE, 3920, 0, 110550, 2000, 0x00)
    OP_8E(0x00FE, 3960, 0, 109850, 2000, 0x00)

    @scena.Lambda('lambda_900E')
    def lambda_900E():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000001F4)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_900E)

    OP_8E(0x00FE, 4170, 0, 108510, 2000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x001E offset: 0x9034
@scena.Code('func_1E_9034')
def func_1E_9034():
    EventBegin(0x00)
    OP_4A(0x0008, 255)
    OP_20(0x000001F4)
    OP_6D(160, 0, 117520, 0)
    OP_67(0, 6400, -10000, 0)
    OP_6B(2790, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x0101, 0x0004)
    SetChrFlags(0x0107, 0x0004)
    SetChrFlags(0x0103, 0x0004)
    SetChrFlags(0x0105, 0x0004)
    SetChrPos(0x0101, 4410, 0, 109480, 0)
    SetChrPos(0x0107, 4410, 0, 109480, 0)
    SetChrPos(0x0103, 4410, 0, 109480, 0)
    SetChrPos(0x0105, 4410, 0, 109480, 0)
    SetChrPos(0x000B, -700, 0, 116590, 45)
    SetChrPos(0x000A, 500, 0, 116600, 0)
    SetChrPos(0x000E, 1800, 0, 116590, 0)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(300)

    OP_22(0x0006, 0x00, 0x64)
    Sleep(500)

    OP_62(0x000A, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x000E, 0x00000000, 2300, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x000B, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    @scena.Lambda('lambda_9170')
    def lambda_9170():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_9170')

    DispatchAsync2(0x000A, 0x0001, lambda_9170)

    @scena.Lambda('lambda_9181')
    def lambda_9181():
        ChrTurnDirection(0x00FE, 0x0103, 400)
        Yield()

        Jump('lambda_9181')

    DispatchAsync2(0x000E, 0x0001, lambda_9181)

    @scena.Lambda('lambda_9192')
    def lambda_9192():
        ChrTurnDirection(0x00FE, 0x0103, 400)
        Yield()

        Jump('lambda_9192')

    DispatchAsync2(0x000B, 0x0001, lambda_9192)

    @scena.Lambda('lambda_91A3')
    def lambda_91A3():
        OP_6D(-150, 0, 116560, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_91A3)

    CreateThread(0x0101, 0x01, 0x00, 0x001F)
    CreateThread(0x0103, 0x01, 0x00, 0x0020)
    CreateThread(0x0107, 0x01, 0x00, 0x0021)
    CreateThread(0x0105, 0x01, 0x00, 0x0022)
    WaitForThreadExit(0x0105, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    ClearChrFlags(0x0101, 0x0004)
    ClearChrFlags(0x0107, 0x0004)
    ClearChrFlags(0x0103, 0x0004)
    ClearChrFlags(0x0105, 0x0004)
    TerminateThread(0x000A, 0x01)
    TerminateThread(0x000E, 0x01)
    TerminateThread(0x000B, 0x01)

    ChrTalk(
        0x000A,
        (
            '#0050290738V#051F#5P哦，终于回来了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0080290739V#073F#2P怎样？\n',
            '怎么这么晚啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290740V#025F#6P嗯嗯，发生了不少事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290741V#1015F#6P阿加特你们\n',
            '已经去过矿山了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050290742V#051F#5P啊啊，早就\n',
            '回来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050290743V出发得快，\n',
            '所以意外地回来得早。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0080290744V#074F#2P不过，回来途中\n',
            '出现了奇怪的魔兽。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080290745V现在就正在说这事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290746V#1004F#6P奇怪的魔兽？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    OP_1D(0x21)
    Sleep(400)

    ChrTalk(
        0x000B,
        (
            '#0040290747V#032F#5P出现在雾中\n',
            '被打倒后就会消失的魔兽啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040290748V该称为『雾魔』吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290749V#1020F#6P那、那是……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060290750V#042F#6P和那个魔兽一样呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050290751V#052F#5P怎么，你们那儿\n',
            '也出现了吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050290752V没受伤吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070290753V#063F#6P嗯，我们\n',
            '倒是不要紧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290754V#1003F#6P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050290755V#555F#5P？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350290756V#742F好像发生了什么事呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350290757V能报告一下吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290758V#022F#6P嗯嗯，其实……',
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
            '把在农场发生的事情报告了一遍。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#0350290759V#745F是吗……\n',
            '看来晚了一步呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290760V#522F#6P……是我的失误。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290761V要是做得再好些，\n',
            '就能捉住犯人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290762V#1003F#6P不……\n',
            '完全不是雪拉姐的错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290763V错的是关键时刻\n',
            '却动弹不得的我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350290764V#742F别介意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350290765V看来你们\n',
            '是被人设了陷阱了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290766V#1004F#6P陷、陷阱！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0080290767V#074F#2P进入农场同时\n',
            '听到的铃声……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080290768V埋伏的雾之魔兽，\n',
            '还有上锁的正门……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080290769V#072F差之毫厘的时机\n',
            '让你们没赶上，\n',
            '感觉就像被算计了一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290770V#1020F#6P不，不只是偶然吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0040290771V#032F#5P不，经过对昏睡事件的思考，\n',
            '『黑衣女人』行事相当的巧妙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040290772V特地抢先让\n',
            '你们保护的人睡着……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040290773V#035F呵呵，说不定\n',
            '这是她对你们的挑衅呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250559V#1015F#6P嗯、嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290775V只知道是『黑衣女人』，\n',
            '其实也完全没有线索……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290776V也没有实际被挑衅的印象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290777V#522F#6P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(300)

    OP_22(0x0006, 0x00, 0x64)
    Sleep(1000)

    OP_9F(0x0011, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    SetChrPos(0x0011, 4250, 0, 108920, 0)
    ClearChrFlags(0x0011, 0x0080)
    OP_4A(0x0011, 255)

    NpcTalk(
        0x0011,
        '青年的声音',
        (
            '#3350290778V#2P呼，我回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(10)

    OP_62(0x0103, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(10)

    OP_62(0x0105, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x000B, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(10)

    OP_62(0x0107, 0x00000000, 1700, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x000E, 0x00000000, 2300, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(10)

    OP_62(0x000A, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    @scena.Lambda('lambda_9A8E')
    def lambda_9A8E():
        OP_6D(2550, 0, 112570, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_9A8E)

    Sleep(50)

    @scena.Lambda('lambda_9AAB')
    def lambda_9AAB():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_9AAB')

    DispatchAsync2(0x0101, 0x0001, lambda_9AAB)

    Sleep(50)

    @scena.Lambda('lambda_9AC1')
    def lambda_9AC1():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_9AC1')

    DispatchAsync2(0x0103, 0x0001, lambda_9AC1)

    Sleep(50)

    @scena.Lambda('lambda_9AD7')
    def lambda_9AD7():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_9AD7')

    DispatchAsync2(0x0105, 0x0001, lambda_9AD7)

    Sleep(50)

    @scena.Lambda('lambda_9AED')
    def lambda_9AED():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_9AED')

    DispatchAsync2(0x0107, 0x0001, lambda_9AED)

    Sleep(50)

    @scena.Lambda('lambda_9B03')
    def lambda_9B03():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_9B03')

    DispatchAsync2(0x000A, 0x0001, lambda_9B03)

    Sleep(50)

    @scena.Lambda('lambda_9B19')
    def lambda_9B19():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_9B19')

    DispatchAsync2(0x000B, 0x0001, lambda_9B19)

    Sleep(50)

    @scena.Lambda('lambda_9B2F')
    def lambda_9B2F():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_9B2F')

    DispatchAsync2(0x000E, 0x0001, lambda_9B2F)

    WaitForThreadExit(0x0101, 0x0000)
    CreateThread(0x0011, 0x01, 0x00, 0x0023)
    Sleep(500)

    @scena.Lambda('lambda_9B51')
    def lambda_9B51():
        OP_6D(650, 0, 116600, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_9B51)

    WaitForThreadExit(0x0011, 0x0001)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0103, 0x01)
    TerminateThread(0x0105, 0x01)
    TerminateThread(0x0107, 0x01)
    TerminateThread(0x000A, 0x01)
    TerminateThread(0x000B, 0x01)
    TerminateThread(0x000E, 0x01)
    TerminateThread(0x0008, 0x01)
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0101,
        (
            '#0010290779V#1004F#5P咦，利吉先生？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290780V#020F#2P说起来你是为了护卫工作\n',
            '去了王都吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3350290781V#6P嗯嗯，一早去了那边\n',
            '终于回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3350290782V#6P话说回来……\n',
            '到底发生了什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3350290783V#6P雾蔓延的范围也扩大了…\n',
            '士兵在城里巡逻的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350290784V#742F其实昨天傍晚时分\n',
            '发生了很多严重的事情。',
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
            '把昨天到今天的事情\n',
            '概括地向利吉说明了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0011,
        (
            '#3350290785V#6P哇……\n',
            '竟然有这种事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3350290786V#6P我出去的真不是时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290787V#1006F#5P哪里，别在意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290788V既然定期船停了，\n',
            '护卫也是十分重要的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290789V#027F#2P因为我们都没有\n',
            '余力来承担这些工作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290790V有你帮忙真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3350290791V#6P非，非常荣幸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3350290792V#6P这么说来……\n',
            '关于那个『铃声』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3350290793V#6P那是从雾的某处\n',
            '传来的对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290794V#025F#2P嗯嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290795V#1007F#5P虽然还不清楚\n',
            '为什么会出现铃声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3350290796V#6P是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290797V#023F#2P有什么线索吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3350290798V#6P刚才通过\n',
            '艾利兹街道的时候……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3350290799V#6P好像听到了微弱的铃声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(10)

    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(10)

    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(10)

    OP_62(0x0107, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x000E, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(10)

    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010290800V#1005F#5P你、你说什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290801V#024F#2P大概在\n',
            '艾利兹街道哪里听到的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3350290802V#6P唔、嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3350290803V#6P从格鲁纳门刚出来\n',
            '就听到了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3350290804V#6P应该是从神秘森林那边传来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290805V#022F#2P神秘森林……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0080290806V#072F#2P记得是洛连特地区\n',
            '东南方的森林吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3350290807V#6P一开始还以为有人在，\n',
            '就向发出声音的方向\n',
            '大声喊了一下看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3350290808V#6P但是没有任何回声，\n',
            '想来是我的错觉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0040290809V#032F#5P唔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040290810V很可能就是希望引起我们注意，\n',
            '而特地鸣响的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060290811V#042F#5P这算是……挑衅吗～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0050290812V#057F#5P哼、真是看不起人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290813V#1002F#5P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010290814V#1002F#5P雪拉姐……怎么办～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030211803V#026F#2P是啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x0103,
        (
            '#0030290816V#022F#4P虽然很可能是圈套，\n',
            '但也只能往里跳了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290817V就应邀拜访吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1500, 0, -1)
    OP_0D()
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000E, 0x0080)
    SetChrFlags(0x0011, 0x0080)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※进行队伍的重新编组。\n',
            '　请选择２名固定成员以外的同行者。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    OP_6D(17370, 0, 123310, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(100)

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
            0x0005,
            0x0003,
            0x0004,
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
    OP_4B(0x0008, 255)
    OP_A2(0x1823)
    OP_28(0x0092, 0x04, 0x02)
    OP_28(0x0092, 0x04, 0x08)
    OP_28(0x0092, 0x01, 0x0001)
    OP_20(0x000007D0)
    OP_21()
    Sleep(500)

    OP_6D(1370, 0, 113410, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, 1370, 0, 113410, 180)
    SetChrPos(0x0001, 1370, 0, 113410, 180)
    SetChrPos(0x0002, 1370, 0, 113410, 180)
    SetChrPos(0x0003, 1370, 0, 113410, 180)
    OP_69(0x0000, 0x00000000)
    OP_1D(0x0A)
    FadeIn(1000, 0)
    OP_0D()
    EventEnd(0x00)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0xA),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x001F offset: 0xA5BE
@scena.Code('func_1F_A5BE')
def func_1F_A5BE():
    OP_8E(0x00FE, 710, 0, 115000, 3000, 0x00)
    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x0020 offset: 0xA5DA
@scena.Code('func_20_A5DA')
def func_20_A5DA():
    Sleep(500)

    OP_8E(0x00FE, 2540, 0, 112550, 3000, 0x00)
    OP_8E(0x00FE, 1840, 0, 115000, 3000, 0x00)
    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x0021 offset: 0xA60F
@scena.Code('func_21_A60F')
def func_21_A60F():
    Sleep(500)

    Sleep(500)

    OP_8E(0x00FE, 740, 0, 113800, 3000, 0x00)
    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x0022 offset: 0xA635
@scena.Code('func_22_A635')
def func_22_A635():
    Sleep(500)

    Sleep(500)

    Sleep(500)

    @scena.Lambda('lambda_A64A')
    def lambda_A64A():
        OP_8E(0x00FE, 2540, 0, 112550, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0003, lambda_A64A)

    Sleep(300)

    OP_22(0x0007, 0x00, 0x64)
    WaitForThreadExit(0x0105, 0x0003)
    OP_8E(0x00FE, 1840, 0, 113800, 3000, 0x00)
    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x0023 offset: 0xA68A
@scena.Code('func_23_A68A')
def func_23_A68A():
    @scena.Lambda('lambda_A690')
    def lambda_A690():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_A690)

    OP_8E(0x00FE, 3920, 0, 110550, 2000, 0x00)
    OP_8E(0x00FE, 1590, 0, 112440, 2000, 0x00)
    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x0024 offset: 0xA6CC
@scena.Code('func_24_A6CC')
def func_24_A6CC():
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
        'loc_A6EC',
    )

    Call(0, 0x0027)
    FadeIn(0, 0)
    Call(0, 0x0028)

    def _loc_A6EC(): pass

    label('loc_A6EC')

    Call(0, 0x0025)
    OP_4A(0x0008, 255)
    OP_6D(400, 0, 117350, 0)
    OP_67(0, 6220, -10000, 0)
    OP_6B(2820, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 610, 0, 116590, 0)
    SetChrPos(0x0103, 1630, 0, 116600, 0)
    SetChrPos(0x0107, 1490, 0, 115380, 0)
    SetChrPos(0x0105, -10, 0, 115840, 0)
    SetChrPos(0x0108, 980, 0, 114460, 0)
    SetChrPos(0x0104, 2630, 0, 114990, 0)
    SetChrPos(0x0106, -240, 0, 114330, 0)
    ClearMapFlags(0x02000000)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0350291406V#744F是吗……\n',
            '竟然有这种事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030291407V#522F#6P对不起，爱娜。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030291408V如果我早点将心里的想法\n',
            '告诉你就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350291409V#740F呵呵，不用在意的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350291410V就算当时知道了她是你的旧识，\n',
            '也一样做不了什么啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350291411V#741F想道歉的话，下次请我喝酒就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030291412V#021F#6P哈哈～那是小事一桩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010291413V#1016F#6P厄…这两个人一起喝酒的话……\n',
            '怎么想也不可能是『小事』啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0104, 0x0000000F, 0x00000000, 0x0000012C, 0x00000FA0)
    Sleep(500)

    ChrTalk(
        0x0104,
        (
            '#0040291414V#034F呜啊啊啊（发抖）……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350291415V#740F雾散天晴，\n',
            '昏睡的人们也从梦中醒了过来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350291416V#741F大家辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350291417V这次的任务一共有好几个，\n',
            '报酬合在一起支付给你们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0090, 0x04, 0x10)
    OP_AF(0x03, 0x0090)
    Sleep(100)

    OP_28(0x0091, 0x04, 0x10)
    OP_AF(0x03, 0x0091)
    Sleep(100)

    OP_28(0x0092, 0x04, 0x10)
    OP_AF(0x03, 0x0092)
    Sleep(100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ChrTalk(
        0x0101,
        (
            '#0010291418V#1007F#6P不过，这次的问题\n',
            '也没有得到根本的解决。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291419V『福音』已经\n',
            '影响到了人的精神。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291420V#1015F看来凭现今的技术力\n',
            '还无法解释这个现象啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070291421V#063F#6P嗯，是的……\n',
            '这是目前为止最难以解释的事件。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070291422V等等要把报告书\n',
            '给爷爷传过去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050291423V#053F看来『福音』的秘密\n',
            '只能等老爷子来分析了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050291424V#050F更重要的是，总算能看清了一些\n',
            '『结社』的势力结构。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080291425V#074F嗯，结合这次的事件……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080291426V#072F一共已经有５名『执行者』\n',
            '的身份可以确定了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350291427V#744F是啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_20(0x000003E8)
    OP_21()
    OP_1D(0x6E)
    Sleep(500)

    OP_AD(0x00240089, 0x0000, 0x0000, 0x000001F4)
    Sleep(1000)

    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('爱娜')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0350291428V#742FＮＯ．Ⅹ。\n',
            '『怪盗绅士』布卢布兰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AE(0x000001F4)
    Sleep(1000)

    OP_AD(0x0024008A, 0x0000, 0x0000, 0x000001F4)
    Sleep(1000)

    SetChrName('爱娜')

    Talk(
        (
            '#0350291429V#742FＮＯ．Ⅷ。\n',
            '『瘦狼』瓦鲁特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AE(0x000001F4)
    Sleep(1000)

    OP_AD(0x002400D5, 0x0000, 0x0000, 0x000001F4)
    Sleep(1000)

    SetChrName('爱娜')

    Talk(
        (
            '#0350291430V#742FＮＯ．ⅩⅤ。\n',
            '『歼灭天使』玲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AE(0x000001F4)
    Sleep(1000)

    OP_AD(0x0024008C, 0x0000, 0x0000, 0x000001F4)
    Sleep(1000)

    SetChrName('爱娜')

    Talk(
        (
            '#0350291431V#742FＮＯ．Ⅵ。\n',
            '『幻惑之铃』露茜奥拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AE(0x000001F4)
    Sleep(1000)

    OP_AD(0x0024008D, 0x0000, 0x0000, 0x000001F4)
    Sleep(1000)

    SetChrName('爱娜')

    Talk(
        (
            '#0350291432V#742FＮＯ．０。\n',
            '『小丑』肯帕雷拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AE(0x000001F4)
    Sleep(1000)

    OP_AD(0x0024008E, 0x0000, 0x0000, 0x000001F4)
    Sleep(1000)

    SetChrName('爱娜')

    Talk(
        (
            '#0350291433V#744F然后，除了这５个人之外，\n',
            '另外还有『教授』和『莱维』\n',
            '这两个尚未确认的人物。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350291434V#742F或许其中的某一个\n',
            '就是洛伦斯少尉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(100, 280, -1, -1)
    OP_61(0x0101)

    Talk(
        (
            '#0010291435V#1003F嗯……\n',
            '这个可能性应该不低。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291436V两个人可能都是\n',
            '我认识的人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(200, 320, -1, -1)
    OP_61(0x0105)

    Talk(
        (
            '#0060291437V#043F确实，洛伦斯那个名字\n',
            '也有可能是假的名字。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(1000, 0)
    OP_AE(0x000001F4)
    Sleep(1500)

    OP_0D()

    ChrTalk(
        0x0106,
        (
            '#0050291438V#555F但是，仅仅只有７个人\n',
            '就干出了这番事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050291439V真是一帮令人头痛的家伙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030291440V#026F#6P是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030291441V#022F看来，我们也应该\n',
            '更小心行事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010291442V#1026F#5P雪拉姐……这样行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030291443V#524F#4P呵呵，我不是已经说过了吗？\n',
            '利贝尔就是我新的故乡。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030291444V保护自己的故乡难道还需要任何理由吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030291445V就算是和曾经的回忆产生冲突，\n',
            '我也绝对不会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200288V#1026F#5P雪拉姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0108, 0x00000000, 2300, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1500)

    OP_63(0x0108)
    Sleep(500)

    ChrTalk(
        0x0108,
        (
            '#0080291447V#070F我说，雪拉扎德。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080291448V我认为你并没有必要这么早\n',
            '就下定这种决心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0103, 0x0108, 400)

    ChrTalk(
        0x0103,
        (
            '#0030291449V#023F#2P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080291450V#074F我和瓦鲁特之间的战斗\n',
            '早已经是注定无可避免的了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080291451V因为我和他之间除了拳头之外，\n',
            '再没有更好的交流方式。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080291452V#070F但你们之间的关系\n',
            '却未必到了这种程度吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030291453V#522F#2P这个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291454V#1006F#5P我认为金先生说的没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291455V雪拉姐不必太早下定论，今后该怎么做，\n',
            '从现在开始慢慢考虑就可以了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291456V我也是……\n',
            '好不容易才想通的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030291457V#023F啊#4P……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 180, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010291458V#1011F#2P对了，各位。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291459V虽然现在状况不大好……不过\n',
            '还是有样东西希望大家看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_B4DB')
    def lambda_B4DB():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_B4DB)

    Sleep(100)

    ChrTurnDirection(0x00F9, 0x0101, 400)

    ChrTalk(
        0x0106,
        (
            '#0050291460V#052F啊……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060291461V#044F#6P艾丝蒂尔……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030291462V#023F#4P艾丝蒂尔，难道你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291463V#1012F#2P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291464V#1025F这是从杂志社那里\n',
            '拿到的照片……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    Fade(250)
    SetChrChipByIndex(0x0101, 17)
    SetChrSubChip(0x0101, 0)
    OP_0D()
    Sleep(500)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '给大家看朵洛希拍摄的照片。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_AD(0x00240091, 0x0000, 0x0000, 0x000001F4)
    Sleep(1500)

    SetMessageWindowPos(100, 280, -1, -1)
    OP_61(0x0106)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0050291465V#555F这不是……\n',
            '抢夺空贼艇事件的照片吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(200, 320, -1, -1)
    OP_61(0x0104)

    Talk(
        (
            '#0040291466V#033F原来如此……\n',
            '还真是有这样的东西啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(300, 280, -1, -1)
    OP_61(0x0108)

    Talk(
        (
            '#0080291467V#073F嗯，在左边的\n',
            '是出席了武术大会\n',
            '空贼团的女孩。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080291468V……右面的那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(100, 280, -1, -1)
    OP_61(0x0105)

    Talk(
        (
            '#0060291469V#043F#6P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(200, 320, -1, -1)
    OP_61(0x0107)

    Talk(
        (
            '#0070291470V#065F#6P约、约修亚哥哥！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_20(0x000003E8)
    OP_21()
    OP_AE(0x000000C8)
    Sleep(1500)

    Fade(250)
    SetChrChipByIndex(0x0101, 65535)
    SetChrSubChip(0x0101, 0)
    OP_0D()
    OP_1D(0x01)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010291471V#1007F#2P嗯……\n',
            '对不起，一直没有和大家说起。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291472V#1003F那时候很迷惑，\n',
            '不知道怎么说出来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070280780V#063F#6P姐姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060291474V#043F#6P艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291475V#1002F#2P约修亚想做什么\n',
            '我不是很清楚……不过',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291476V我猜，约修亚一定是想用自己的方法\n',
            '来接近『结社』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291477V就算和空贼们在一起\n',
            '并不意味肯定做了什么坏事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350291478V#744F是啊，我们都明白的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350291479V#740F照片也只照下了一半的脸，\n',
            '还不能成为决定性的证据。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350291480V这个情报就在协会内部\n',
            '留存就好，不要再传播了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010291481V#1017F#6P谢谢，爱娜姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060291482V#043F#6P但，但是……\n',
            '艾丝蒂尔，难道就如此罢休了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060291483V好不容易找到了约修亚的\n',
            '一点点线索……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010291463V#1012F#2P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291485V#1006F只要我还是我，\n',
            '和约修亚之间的缘分便不会就此断掉的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291486V只要这么一想的话，\n',
            '就不会太过焦急了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060291487V#044F#6P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291488V#1006F#2P虽然行走的道路不同，\n',
            '肯定最终的目标是相同的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291489V#1012F所以现在……\n',
            '我想走我自己的路。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291490V不这样的话，\n',
            '我就不能变坚强。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060291491V#542F#6P艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291492V#1008F#2P哈哈……\n',
            '多少还是有点好面子，所以……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291493V约修亚和那个男人婆之间的关系，\n',
            '我还是十分在意哟。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291494V#1007F这就是修行还远远不足的证据。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060291495V#045F#6P呵呵……\n',
            '艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030291496V#021F#4P呵呵，不是已经找到了\n',
            '想要的答案了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030291497V#027F看来，在森林中看到的梦…\n',
            '好像正朝好的方向发展了嘛？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010291498V#1017F#5P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291499V我再次深深的感觉到\n',
            '与约修亚之间的羁绊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291500V也能够感觉到\n',
            '妈妈的那种温馨。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291501V#1001F别的不说，单是这次的事件\n',
            '就应该感谢『福音』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070291502V#061F#6P呵呵，姐姐真是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050291503V#051F真是的……\n',
            '你还真是想得开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040291504V#031F呵，在艾丝蒂尔面前\n',
            '『福音』也变得一点不可怕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    Call(0, 0x0026)

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BEF6',
    )

    OP_A2(0x183C)

    def _loc_BEF6(): pass

    label('loc_BEF6')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BF07',
    )

    OP_A2(0x183D)

    def _loc_BF07(): pass

    label('loc_BF07')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BF18',
    )

    OP_A2(0x183E)

    def _loc_BF18(): pass

    label('loc_BF18')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BF29',
    )

    OP_A2(0x183F)

    def _loc_BF29(): pass

    label('loc_BF29')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BF3A',
    )

    OP_A2(0x1840)

    def _loc_BF3A(): pass

    label('loc_BF3A')

    OP_AD(0x002400B1, 0x0000, 0x0000, 0x00000064)
    Sleep(4000)

    OP_56(0x02)
    OP_A2(0x1843)

    ExecExpressionWithVar(
        0x31,
        (
            (Expr.PushLong, 0x126),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6D(100000, -100000, 100000, 0)
    FadeIn(0, 0)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    UnlockAchievement(0x11, 0x00, 0x00, 0x00)

    Menu(
        0,
        240,
        180,
        0,
        (
            TXT(0x00, '【保存进度】\n'),
            TXT(0x01, '【进入下一章】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BFBB',
    )

    ShowSaveMenu()

    def _loc_BFBB(): pass

    label('loc_BFBB')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_AE(0x000000C8)
    Sleep(2000)

    OP_A3(0x1843)

    ExecExpressionWithVar(
        0x04,
        (
            (Expr.PushLong, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A2(0x10F0)
    NewScene('ED6_DT21/C0705._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0025 offset: 0xBFF1
@scena.Code('func_25_BFF1')
def func_25_BFF1():
    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_C02A',
    )

    FormationAddMember(ChrTable['金'], 0xFA, 0xFF)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_C02A(): pass

    label('loc_C02A')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_C063',
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C04B',
    )

    FormationAddMember(ChrTable['科洛丝'], 0xFA, 0xFF)

    Jump('loc_C04F')

    def _loc_C04B(): pass

    label('loc_C04B')

    FormationAddMember(ChrTable['科洛丝'], 0xFB, 0xFF)

    def _loc_C04F(): pass

    label('loc_C04F')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x2),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_C063(): pass

    label('loc_C063')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_C0B0',
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C084',
    )

    FormationAddMember(ChrTable['奥利维尔'], 0xFA, 0xFF)

    Jump('loc_C09C')

    def _loc_C084(): pass

    label('loc_C084')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C098',
    )

    FormationAddMember(ChrTable['奥利维尔'], 0xFB, 0xFF)

    Jump('loc_C09C')

    def _loc_C098(): pass

    label('loc_C098')

    FormationAddMember(ChrTable['奥利维尔'], 0xFC, 0xFF)

    def _loc_C09C(): pass

    label('loc_C09C')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x8),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_C0B0(): pass

    label('loc_C0B0')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_C0FD',
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C0D1',
    )

    FormationAddMember(ChrTable['阿加特'], 0xFA, 0xFF)

    Jump('loc_C0E9')

    def _loc_C0D1(): pass

    label('loc_C0D1')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C0E5',
    )

    FormationAddMember(ChrTable['阿加特'], 0xFB, 0xFF)

    Jump('loc_C0E9')

    def _loc_C0E5(): pass

    label('loc_C0E5')

    FormationAddMember(ChrTable['阿加特'], 0xFC, 0xFF)

    def _loc_C0E9(): pass

    label('loc_C0E9')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x10),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_C0FD(): pass

    label('loc_C0FD')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_C122',
    )

    FormationAddMember(ChrTable['提妲'], 0xFC, 0xFF)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x4),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_C122(): pass

    label('loc_C122')

    Return()

# id: 0x0026 offset: 0xC123
@scena.Code('func_26_C123')
def func_26_C123():
    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_C133',
    )

    FormationDelMember(0x07, 0xFF)

    def _loc_C133(): pass

    label('loc_C133')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_C143',
    )

    FormationDelMember(0x04, 0xFF)

    def _loc_C143(): pass

    label('loc_C143')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x4),
            Expr.And,
            Expr.Return,
        ),
        'loc_C153',
    )

    FormationDelMember(0x06, 0xFF)

    def _loc_C153(): pass

    label('loc_C153')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x8),
            Expr.And,
            Expr.Return,
        ),
        'loc_C163',
    )

    FormationDelMember(0x03, 0xFF)

    def _loc_C163(): pass

    label('loc_C163')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_C173',
    )

    FormationDelMember(0x05, 0xFF)

    def _loc_C173(): pass

    label('loc_C173')

    Return()

# id: 0x0027 offset: 0xC174
@scena.Code('func_27_C174')
def func_27_C174():
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
        (0x00000000, 'loc_C1F1'),
        (0x00000001, 'loc_C1F7'),
        (-1, 'loc_C1FD'),
    )

    def _loc_C1F1(): pass

    label('loc_C1F1')

    OP_A2(0x1200)

    Jump('loc_C1FD')

    def _loc_C1F7(): pass

    label('loc_C1F7')

    OP_A2(0x1201)

    Jump('loc_C1FD')

    def _loc_C1FD(): pass

    label('loc_C1FD')

    Return()

# id: 0x0028 offset: 0xC1FE
@scena.Code('func_28_C1FE')
def func_28_C1FE():
    ClearMapFlags(0x00000001)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)

    OP_C9(
        0x00,
        (
            0x0000,
            0x0002,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0003,
            0x0004,
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

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

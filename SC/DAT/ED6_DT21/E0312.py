import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import E0312_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('E0312   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '拉赛尔博士'),
    TXT(0x02, '雪拉扎德'),
    TXT(0x03, '阿加特'),
    TXT(0x04, '提妲'),
    TXT(0x05, '金'),
    TXT(0x06, '凯文神父'),
    TXT(0x07, '乔丝特'),
    TXT(0x08, '雨果'),
    TXT(0x09, '露依赛'),
    TXT(0x0A, '亲卫队队员'),
    TXT(0x0B, '亲卫队队员'),
    TXT(0x0C, '雷伊'),
    TXT(0x0D, '库莱泽'),
    TXT(0x0E, '修理员佩顿'),
    TXT(0x0F, '菲'),
    TXT(0x10, '安东尼'),
    TXT(0x11, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Event'
    header.mapModel       = 'E0312.x'
    header.mapIndex       = 1
    header.bgm            = 116
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT21/E0312._SN', 'ED6_DT21/E0312_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xBAD4
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
        ('ED6_DT07/CH02020._CH', 'ED6_DT07/CH02020P._CP'),
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT07/CH00050._CH', 'ED6_DT07/CH00050P._CP'),
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP'),
        ('ED6_DT27/CH03080._CH', 'ED6_DT27/CH03080P._CP'),
        ('ED6_DT27/CH03100._CH', 'ED6_DT27/CH03100P._CP'),
        ('ED6_DT07/CH01680._CH', 'ED6_DT07/CH01680P._CP'),
        ('ED6_DT07/CH01430._CH', 'ED6_DT07/CH01430P._CP'),
        ('ED6_DT07/CH01320._CH', 'ED6_DT07/CH01320P._CP'),
        ('ED6_DT07/CH01220._CH', 'ED6_DT07/CH01220P._CP'),
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
        ('ED6_DT07/CH01550._CH', 'ED6_DT07/CH01550P._CP'),
        ('ED6_DT07/CH01700._CH', 'ED6_DT07/CH01700P._CP'),
        ('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP'),
    ]

# id: 0x10002 offset: 0x122
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
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
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
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
            direction           = 0,
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
            direction           = 0,
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
            direction           = 0,
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
            x                   = 360,
            z                   = 0,
            y                   = 63980,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = -5140,
            z                   = 0,
            y                   = 65400,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = -2670,
            z                   = 0,
            y                   = 5340,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            x                   = -2680,
            z                   = 0,
            y                   = 5370,
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
            x                   = -5340,
            z                   = 0,
            y                   = 60180,
            direction           = 270,
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
            x                   = -5340,
            z                   = 0,
            y                   = 58780,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            x                   = -30,
            z                   = 0,
            y                   = 60960,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            x                   = 400,
            z                   = 0,
            y                   = 63980,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            x                   = -6120,
            z                   = 0,
            y                   = 62560,
            direction           = 233,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
    )

# id: 0x10003 offset: 0x322
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x322
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -2680,
            y           = -1000,
            z           = 5370,
            range       = 3000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x0000002A,
        ),
    )

# id: 0x10005 offset: 0x342
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -5110,
            triggerZ            = 0,
            triggerY            = 65500,
            triggerRange        = 400,
            actorX              = -5410,
            actorZ              = 1500,
            actorY              = 65800,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0000,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -2980,
            triggerZ            = 0,
            triggerY            = 66830,
            triggerRange        = 800,
            actorX              = -2980,
            actorZ              = 1000,
            actorY              = 66830,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0027,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 60000,
            triggerZ            = 0,
            triggerY            = -36460,
            triggerRange        = 1200,
            actorX              = 60000,
            actorZ              = 2080,
            actorY              = -36230,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0028,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -2370,
            triggerZ            = 0,
            triggerY            = 60960,
            triggerRange        = 800,
            actorX              = -30,
            actorZ              = 1500,
            actorY              = 60960,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0029,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 62910,
            triggerZ            = 0,
            triggerY            = 4740,
            triggerRange        = 1200,
            actorX              = 62910,
            actorZ              = 800,
            actorY              = 4740,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0028,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x3F6
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x64),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_413',
    )

    OP_89(0x0000, 2980, 1200, 4200, 180)

    def _loc_413(): pass

    label('loc_413')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_5B9',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_43D',
    )

    SetChrPos(0x000B, -2830, 0, 65940, 90)
    ClearChrFlags(0x000B, 0x0080)

    def _loc_43D(): pass

    label('loc_43D')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_460',
    )

    SetChrPos(0x000D, 62920, 0, 8020, 0)
    ClearChrFlags(0x000D, 0x0080)

    def _loc_460(): pass

    label('loc_460')

    ClearChrFlags(0x0015, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 1, 0x2219)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4A9',
    )

    SetChrPos(0x0008, -950, 0, 65390, 0)
    ClearChrFlags(0x0008, 0x0080)

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_4A6',
    )

    SetChrPos(0x0009, -5340, 0, 59510, 270)
    ClearChrFlags(0x0009, 0x0080)

    def _loc_4A6(): pass

    label('loc_4A6')

    Jump('loc_5B6')

    def _loc_4A9(): pass

    label('loc_4A9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4CA',
    )

    SetChrPos(0x0008, -950, 0, 65390, 0)
    ClearChrFlags(0x0008, 0x0080)

    Jump('loc_5B6')

    def _loc_4CA(): pass

    label('loc_4CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_547',
    )

    SetChrPos(0x0008, -950, 0, 65390, 0)
    ClearChrFlags(0x0008, 0x0080)

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_50B',
    )

    SetChrPos(0x000B, -3510, 0, 5330, 0)
    ClearChrFlags(0x000B, 0x0080)

    def _loc_50B(): pass

    label('loc_50B')

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_52E',
    )

    SetChrPos(0x000E, -5340, 0, 60030, 270)
    ClearChrFlags(0x000E, 0x0080)

    def _loc_52E(): pass

    label('loc_52E')

    SetChrPos(0x0012, 63010, 0, -39310, 270)
    ClearChrFlags(0x0012, 0x0080)

    Jump('loc_5B6')

    def _loc_547(): pass

    label('loc_547')

    ClearChrFlags(0x0016, 0x0080)

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_56F',
    )

    SetChrPos(0x000E, -5340, 0, 60030, 270)
    ClearChrFlags(0x000E, 0x0080)

    def _loc_56F(): pass

    label('loc_56F')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_5A0',
    )

    TerminateThread(0x000A, 0x00)
    ClearChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000A, 0x0004)
    SetChrChipByIndex(0x000A, 15)
    SetChrPos(0x000A, 61300, 250, -40950, 0)

    def _loc_5A0(): pass

    label('loc_5A0')

    SetChrPos(0x0008, -950, 0, 65390, 0)
    ClearChrFlags(0x0008, 0x0080)

    def _loc_5B6(): pass

    label('loc_5B6')

    Jump('loc_877')

    def _loc_5B9(): pass

    label('loc_5B9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 6, 0x1E1E)),
            Expr.Return,
        ),
        'loc_680',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 3, 0x1E0B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5E6',
    )

    SetChrPos(0x0008, -5200, 0, 65530, 0)
    ClearChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0008, 0x0010)

    Jump('loc_5FC')

    def _loc_5E6(): pass

    label('loc_5E6')

    SetChrPos(0x0008, -950, 0, 65390, 0)
    ClearChrFlags(0x0008, 0x0080)

    def _loc_5FC(): pass

    label('loc_5FC')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_61F',
    )

    SetChrPos(0x000B, -860, 0, 64200, 45)
    ClearChrFlags(0x000B, 0x0080)

    def _loc_61F(): pass

    label('loc_61F')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_642',
    )

    SetChrPos(0x000D, 62920, 0, 8020, 0)
    ClearChrFlags(0x000D, 0x0080)

    def _loc_642(): pass

    label('loc_642')

    SetChrPos(0x0013, -6370, 0, 61080, 180)
    ClearChrFlags(0x0013, 0x0080)
    SetChrPos(0x0014, -5350, 0, 59530, 270)
    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0017, 0x0080)

    Jump('loc_877')

    def _loc_680(): pass

    label('loc_680')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 1, 0x1E11)),
            Expr.Return,
        ),
        'loc_716',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 3, 0x1E0B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6AD',
    )

    SetChrPos(0x0008, -5200, 0, 65530, 0)
    ClearChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0008, 0x0010)

    Jump('loc_6C3')

    def _loc_6AD(): pass

    label('loc_6AD')

    SetChrPos(0x0008, -950, 0, 65390, 0)
    ClearChrFlags(0x0008, 0x0080)

    def _loc_6C3(): pass

    label('loc_6C3')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_6E6',
    )

    SetChrPos(0x000B, -860, 0, 64200, 45)
    ClearChrFlags(0x000B, 0x0080)

    def _loc_6E6(): pass

    label('loc_6E6')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_709',
    )

    SetChrPos(0x000D, 62920, 0, 8020, 0)
    ClearChrFlags(0x000D, 0x0080)

    def _loc_709(): pass

    label('loc_709')

    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x0012, 0x0080)

    Jump('loc_877')

    def _loc_716(): pass

    label('loc_716')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 2, 0x1E0A)),
            Expr.Return,
        ),
        'loc_7A4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 3, 0x1E0B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_743',
    )

    SetChrPos(0x0008, -5200, 0, 65530, 0)
    ClearChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0008, 0x0010)

    Jump('loc_759')

    def _loc_743(): pass

    label('loc_743')

    SetChrPos(0x0008, -950, 0, 65390, 0)
    ClearChrFlags(0x0008, 0x0080)

    def _loc_759(): pass

    label('loc_759')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_77C',
    )

    SetChrPos(0x000D, 62920, 0, 8020, 0)
    ClearChrFlags(0x000D, 0x0080)

    def _loc_77C(): pass

    label('loc_77C')

    SetChrPos(0x0014, -6310, 0, 61050, 180)
    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0017, 0x0080)

    Jump('loc_877')

    def _loc_7A4(): pass

    label('loc_7A4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            Expr.Return,
        ),
        'loc_823',
    )

    SetChrPos(0x0008, -6370, 0, 61080, 180)
    ClearChrFlags(0x0008, 0x0080)

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_7E4',
    )

    SetChrPos(0x000B, -4420, 0, 62290, 225)
    ClearChrFlags(0x000B, 0x0080)

    def _loc_7E4(): pass

    label('loc_7E4')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_807',
    )

    SetChrPos(0x000D, 62920, 0, 8020, 0)
    ClearChrFlags(0x000D, 0x0080)

    def _loc_807(): pass

    label('loc_807')

    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0017, 0x0080)

    Jump('loc_877')

    def _loc_823(): pass

    label('loc_823')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 3, 0x1A23)),
            Expr.Return,
        ),
        'loc_83C',
    )

    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x0011, 0x0080)

    Jump('loc_877')

    def _loc_83C(): pass

    label('loc_83C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 6, 0x1A1E)),
            Expr.Return,
        ),
        'loc_877',
    )

    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    SetChrChipByIndex(0x000C, 14)
    SetChrSubChip(0x000C, 0)
    SetChrPos(0x000C, 62250, 0, -39280, 90)
    ClearChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000C, 0x0010)

    def _loc_877(): pass

    label('loc_877')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_883'),
        (-1, 'loc_896'),
    )

    def _loc_883(): pass

    label('loc_883')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 2, 0x1E0A)),
            (Expr.TestScenaFlags, ScenaFlag(0x03C9, 5, 0x1E4D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_893',
    )

    Event(0, 0x001A)

    def _loc_893(): pass

    label('loc_893')

    Jump('loc_896')

    def _loc_896(): pass

    label('loc_896')

    Return()

# id: 0x0001 offset: 0x897
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8B5',
    )

    ExecExpressionWithVar(
        0x3B,
        (
            (Expr.PushLong, 0x227),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x3C,
        (
            (Expr.PushLong, 0x10A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_8B5(): pass

    label('loc_8B5')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8E5',
    )

    OP_B2(0x00, 0x00, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Return,
        ),
        'loc_8D9',
    )

    OP_B1('E0312_1')

    Jump('loc_8E2')

    def _loc_8D9(): pass

    label('loc_8D9')

    OP_B1('E0312_2')

    def _loc_8E2(): pass

    label('loc_8E2')

    Jump('loc_906')

    def _loc_8E5(): pass

    label('loc_8E5')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8FD',
    )

    OP_B1('E0312_2')

    Jump('loc_906')

    def _loc_8FD(): pass

    label('loc_8FD')

    OP_B1('E0312_1')

    def _loc_906(): pass

    label('loc_906')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_93C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 3, 0x1A23)),
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_92F',
    )

    SetMapFlags(0x02000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x21),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_93C')

    def _loc_92F(): pass

    label('loc_92F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 3, 0x1A23)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_93C',
    )

    OP_22(0x007A, 0x01, 0x46)

    def _loc_93C(): pass

    label('loc_93C')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_967',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_967',
    )

    SetMapFlags(0x02000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x21),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_22(0x007A, 0x01, 0x46)

    def _loc_967(): pass

    label('loc_967')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_988',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_988',
    )

    SetMapFlags(0x02000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x3E),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_988(): pass

    label('loc_988')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_997',
    )

    OP_72(0x0005, 0x0004)

    Jump('loc_9D5')

    def _loc_997(): pass

    label('loc_997')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 2, 0x1E0A)),
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 3, 0x1E0B)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_9AF',
    )

    OP_64(0x00, 0x0001)
    OP_72(0x0005, 0x0004)

    Jump('loc_9D5')

    def _loc_9AF(): pass

    label('loc_9AF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            Expr.Return,
        ),
        'loc_9C6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 3, 0x1E0B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9BE',
    )

    def _loc_9BE(): pass

    label('loc_9BE')

    OP_72(0x0005, 0x0004)

    Jump('loc_9D5')

    def _loc_9C6(): pass

    label('loc_9C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 6, 0x1A1E)),
            Expr.Return,
        ),
        'loc_9D5',
    )

    OP_64(0x00, 0x0001)
    OP_64(0x03, 0x0001)

    def _loc_9D5(): pass

    label('loc_9D5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_A1C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 1, 0x2219)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9E7',
    )

    Jump('loc_A19')

    def _loc_9E7(): pass

    label('loc_9E7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9F2',
    )

    Jump('loc_A19')

    def _loc_9F2(): pass

    label('loc_9F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9FD',
    )

    Jump('loc_A19')

    def _loc_9FD(): pass

    label('loc_9FD')

    OP_D2(0x00070053, 0x0007005B, 0x0F)

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_A19',
    )

    SetChrChipByIndex(0x000A, 15)

    def _loc_A19(): pass

    label('loc_A19')

    Jump('loc_A7D')

    def _loc_A1C(): pass

    label('loc_A1C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 6, 0x1E1E)),
            Expr.Return,
        ),
        'loc_A30',
    )

    OP_D2(0x000600FC, 0x00060101, 0x0F)

    Jump('loc_A7D')

    def _loc_A30(): pass

    label('loc_A30')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 1, 0x1E11)),
            Expr.Return,
        ),
        'loc_A44',
    )

    OP_D2(0x000600FC, 0x00060101, 0x0F)

    Jump('loc_A7D')

    def _loc_A44(): pass

    label('loc_A44')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 2, 0x1E0A)),
            Expr.Return,
        ),
        'loc_A58',
    )

    OP_D2(0x000600FC, 0x00060101, 0x0F)

    Jump('loc_A7D')

    def _loc_A58(): pass

    label('loc_A58')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            Expr.Return,
        ),
        'loc_A6C',
    )

    OP_D2(0x000600FC, 0x00060101, 0x0F)

    Jump('loc_A7D')

    def _loc_A6C(): pass

    label('loc_A6C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 3, 0x1A23)),
            Expr.Return,
        ),
        'loc_A76',
    )

    Jump('loc_A7D')

    def _loc_A76(): pass

    label('loc_A76')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 6, 0x1A1E)),
            Expr.Return,
        ),
        'loc_A7D',
    )

    def _loc_A7D(): pass

    label('loc_A7D')

    Return()

# id: 0x0002 offset: 0xA7E
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
        'loc_AA3',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_BE5')

    def _loc_AA3(): pass

    label('loc_AA3')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_ABC',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000640)

    Jump('loc_BE5')

    def _loc_ABC(): pass

    label('loc_ABC')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AD5',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x0000060E)

    Jump('loc_BE5')

    def _loc_AD5(): pass

    label('loc_AD5')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AEE',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005DC)

    Jump('loc_BE5')

    def _loc_AEE(): pass

    label('loc_AEE')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B07',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AA)

    Jump('loc_BE5')

    def _loc_B07(): pass

    label('loc_B07')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B20',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x00000578)

    Jump('loc_BE5')

    def _loc_B20(): pass

    label('loc_B20')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B39',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x00000546)

    Jump('loc_BE5')

    def _loc_B39(): pass

    label('loc_B39')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B52',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000677)

    Jump('loc_BE5')

    def _loc_B52(): pass

    label('loc_B52')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B6B',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000645)

    Jump('loc_BE5')

    def _loc_B6B(): pass

    label('loc_B6B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B84',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x00000613)

    Jump('loc_BE5')

    def _loc_B84(): pass

    label('loc_B84')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B9D',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005E1)

    Jump('loc_BE5')

    def _loc_B9D(): pass

    label('loc_B9D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BB6',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AF)

    Jump('loc_BE5')

    def _loc_BB6(): pass

    label('loc_BB6')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BCF',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x0000057D)

    Jump('loc_BE5')

    def _loc_BCF(): pass

    label('loc_BCF')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BE5',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x0000054B)

    def _loc_BE5(): pass

    label('loc_BE5')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_BFA',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_BE5')

    def _loc_BFA(): pass

    label('loc_BFA')

    Return()

# id: 0x0003 offset: 0xBFB
@scena.Code('func_03_BFB')
def func_03_BFB():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_C1E',
    )

    OP_8D(0x00FE, -7430, 62910, -5150, 62070, 1000)

    Jump('func_03_BFB')

    def _loc_C1E(): pass

    label('loc_C1E')

    Return()

# id: 0x0004 offset: 0xC1F
@scena.Code('func_04_C1F')
def func_04_C1F():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0456, 0, 0x22B0)),
            (Expr.Eval, "OP_40(0x0417, 0x00)"),
            (Expr.PushLong, 0x1),
            Expr.Geq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_EC7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0456, 1, 0x22B1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C45',
    )

    Call(0, 0x0024)
    TalkEnd(0x00FE)

    Return()

    def _loc_C45(): pass

    label('loc_C45')

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
            TXT(0x00, '【上前说话】\n'),
            TXT(0x01, '【请求制作武器】\n'),
            TXT(0x02, '【什么也不做】\n'),
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
        'loc_EAD',
    )

    EventBegin(0x00)
    Fade(500)
    OP_6D(-770, 0, 64560, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -1430, 0, 64099, 0)
    SetChrPos(0x0102, -550, 0, 64099, 0)
    SetChrPos(0x00F8, -1450, 0, 63100, 0)
    SetChrPos(0x00F9, -550, 0, 63100, 0)
    OP_8C(0x0008, 180, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0540391048V#100F哦，决定要制作什么武器了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(30, 10, -1, -1)

    Talk(
        (
            TxtCtl.ShowAll,
            0x18,
            (TxtCtl.SetColor, 0x5),
            '<FIXME>どの武器を作成しますか？',
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

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        1,
        330,
        50,
        0,
        (
            TXT(0x00, '<FIXME>棒術具『麒麟具』\n'),
            TXT(0x01, '双剣  『鳳凰剣（鳳·凰）』\n'),
            TXT(0x02, '鞭    『天狼鞭』\n'),
            TXT(0x03, '導力銃『霊銃「久遠」』\n'),
            TXT(0x04, '片手剣『月読』\n'),
            TXT(0x05, '大剣  『奇剣「鬼喰い」』\n'),
            TXT(0x06, '導力砲『九龍砲』\n'),
            TXT(0x07, '手甲  『千手観音』\n'),
            TXT(0x08, '自動弓『破弓「綺羅星」』\n'),
            TXT(0x09, '【放弃】\n'),
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

    OP_5F(0x0001)
    OP_56(0x00)
    Call(0, 0x0025)
    TalkEnd(0x00FE)

    Return()

    def _loc_EAD(): pass

    label('loc_EAD')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_EBE',
    )

    TalkEnd(0x00FE)

    Return()

    def _loc_EBE(): pass

    label('loc_EBE')

    FadeIn(300, 0)

    def _loc_EC7(): pass

    label('loc_EC7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 3, 0x13)),
            Expr.Return,
        ),
        'loc_F71',
    )

    ChrTalk(
        0x0008,
        (
            '#0540391049V#100F呵呵，这回可真是\n',
            '让我积累了宝贵的经验呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391050V毕竟很少有机会\n',
            '能够处理古代金属啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391051V看来今后的研究也\n',
            '更加令人投入了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29C2')

    def _loc_F71(): pass

    label('loc_F71')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 2, 0x1E0A)),
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 3, 0x1E0B)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_F84',
    )

    Call(0, 0x0016)

    Jump('loc_29C2')

    def _loc_F84(): pass

    label('loc_F84')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 3, 0x1E0B)),
            Expr.Return,
        ),
        'loc_26AC',
    )

    If(
        (
            (Expr.Eval, "OP_40(0x03FE, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            (Expr.Eval, "OP_40(0x03FF, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Or,
            (Expr.Eval, "OP_40(0x0400, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Or,
            (Expr.Eval, "OP_40(0x0401, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Or,
            (Expr.Eval, "OP_40(0x0402, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Or,
            (Expr.Eval, "OP_40(0x0403, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Or,
            (Expr.Eval, "OP_40(0x0404, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Or,
            (Expr.Eval, "OP_40(0x0405, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Or,
            (Expr.Eval, "OP_40(0x0406, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Or,
            (Expr.Eval, "OP_40(0x0407, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Or,
            (Expr.Eval, "OP_40(0x0408, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Or,
            (Expr.Eval, "OP_40(0x0408, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_1025',
    )

    Call(0, 0x0017)

    Jump('loc_26A9')

    def _loc_1025(): pass

    label('loc_1025')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Return,
        ),
        'loc_12E8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1272',
    )

    ChrTalk(
        0x0008,
        (
            '#0540391052V#100F接下来要开始进行\n',
            '最终的飞翔引擎检查。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391053V通过的话，修理就算是完成了。\n',
            '可以保证最低限度的飞行能力。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391054V#104F当然，如果能修好左侧的\n',
            '舷外支架是再好不过了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391055V#100F考虑到也许无法修复，\n',
            '所以只是想先做一个测试。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391056V我正在进行中枢塔\n',
            '搜索结束后的返航准备工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0xE),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11EB',
    )

    ChrTalk(
        0x010F,
        (
            '#0100391057V#179F<FIXME>……宜しくお願いします。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540391058V#100F<FIXME>ほっほ、任せておけい。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_126C')

    def _loc_11EB(): pass

    label('loc_11EB')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1232',
    )

    ChrTalk(
        0x0008,
        (
            '#0540391059V#100F那么……\n',
            '提妲就拜托你们照顾了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_126C')

    def _loc_1232(): pass

    label('loc_1232')

    ChrTalk(
        0x0008,
        (
            '#0540391060V#100F那么……\n',
            '你们一定要平安无事地回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_126C(): pass

    label('loc_126C')

    OP_A2(0x0003)

    Jump('loc_12E5')

    def _loc_1272(): pass

    label('loc_1272')

    ChrTalk(
        0x00FE,
        (
            '#0540391061V#100F我正在进行中枢塔\n',
            '搜索结束后的返航准备工作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391062V所以……\n',
            '你们一定要平安无事地回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_12E5(): pass

    label('loc_12E5')

    Jump('loc_26A9')

    def _loc_12E8(): pass

    label('loc_12E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Return,
        ),
        'loc_142A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_13B0',
    )

    ChrTalk(
        0x0008,
        (
            '#0540391063V#104F说不定舷外支架\n',
            '会无法顺利回收……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391064V#100F届时我打算只拆下飞翔引擎，\n',
            '然后装设在埃尔赛尤号上。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391065V我想应该还可以作为\n',
            '辅助的推进器来使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    Jump('loc_1427')

    def _loc_13B0(): pass

    label('loc_13B0')

    ChrTalk(
        0x0008,
        (
            '#0540391066V#100F说不定舷外支架\n',
            '会无法顺利回收……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391067V为了预防这种情况发生，\n',
            '我打算先准备一套替代方案。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1427(): pass

    label('loc_1427')

    Jump('loc_26A9')

    def _loc_142A(): pass

    label('loc_142A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 3, 0x221B)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x045A, 2, 0x22D2)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x045A, 1, 0x22D1)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_17E8',
    )

    ChrTalk(
        0x0008,
        (
            '#0540391068V#100F哦，你们几个。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391069V怎么样？\n',
            '有没有什么有趣的发现啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010391070V#1015F嗯，虽然不知道\n',
            '算不算有趣啦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010391071V不过的确发现了一件让人在意的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#0540391072V#103F喔……\n',
            '发现了什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020391073V#1035F嗯，其实……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '将发现了再次发行『福音』的终端，\n',
            '并要求输入居民姓名一事向博士说明了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x0008,
        (
            '#0540391074V#104F原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391075V#100F为了再次发行『福音』\n',
            '必须输入登录者的姓名啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010391076V#1003F嗯，是这样没错……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010391077V#1007F不过即使是博士，\n',
            '也不会认识以前的居民吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#0540391078V#104F那当然。\n',
            '我可没有那么长寿。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391079V#102F不过，数据水晶里\n',
            '应该记录着过去所发生的事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391080V看看『卡佩尔』的分析资料的话，\n',
            '或许能够得到什么提示也说不定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020391081V#1044F原来如此……\n',
            '确实很有可能呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010391082V#1015F数据水晶吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010391083V嗯，反正也没其它线索，\n',
            '要立刻调查一下看看吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0014)
    OP_A2(0x22D2)

    Jump('loc_26A9')

    def _loc_17E8(): pass

    label('loc_17E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 1, 0x2219)),
            Expr.Return,
        ),
        'loc_1E15',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1C31',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0458, 2, 0x22C2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1BAF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 4, 0x14)),
            Expr.Return,
        ),
        'loc_1951',
    )

    ChrTalk(
        0x0008,
        (
            '#0540391084V#100F数据水晶中\n',
            '记录着过去所发生的事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391080V看看『卡佩尔』的分析资料的话，\n',
            '或许能够得到什么提示也说不定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A3(0x0014)
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x0008, 0x010B, 400)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#0540391086V#103F咦，那不是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391087V#101F什么嘛，那不是空贼姑娘吗。\n',
            '实在是好久不见了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391088V上回最后一次见面是\n',
            '在雷斯顿要塞的地下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19CB')

    def _loc_1951(): pass

    label('loc_1951')

    ChrTurnDirection(0x0008, 0x010B, 0)

    ChrTalk(
        0x0008,
        (
            '#0540391089V#101F哦，是空贼姑娘啊。\n',
            '似乎好久不见了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391088V上回最后一次见面是\n',
            '在雷斯顿要塞的地下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19CB(): pass

    label('loc_19CB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1A59',
    )

    ChrTalk(
        0x010B,
        (
            '#0090391091V#214F空，空贼姑娘是什么！\n',
            '不要取这种奇怪的简称啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090391092V#413F真是的，孙女是那副样子，\n',
            '做爷爷的也是这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A9D')

    def _loc_1A59(): pass

    label('loc_1A59')

    ChrTalk(
        0x010B,
        (
            '#0090391093V#214F空，空贼姑娘是什么！\n',
            '不要取这种奇怪的简称啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A9D(): pass

    label('loc_1A9D')

    ChrTalk(
        0x0008,
        (
            '#0540391094V#100F别说这些无关紧要的事了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391095V话说回来，我倒是听说\n',
            '你们的飞艇也坠落了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391096V虽然我不太了解帝国制的导力引擎，\n',
            '不过多少可以给你们些维修的建议。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391097V要是遇到麻烦\n',
            '就尽管来问我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090391098V#213F啊，嗯……\n',
            '我们会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x22C2)

    Jump('loc_1C2E')

    def _loc_1BAF(): pass

    label('loc_1BAF')

    ChrTurnDirection(0x0008, 0x010B, 0)

    ChrTalk(
        0x0008,
        (
            '#0540391099V#100F听说你们的飞艇\n',
            '也坠落了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391100V要是遇到麻烦\n',
            '就随时来问我吧。\n',
            '我会给你们一些修理上的建议。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1C2E(): pass

    label('loc_1C2E')

    Jump('loc_1E12')

    def _loc_1C31(): pass

    label('loc_1C31')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 4, 0x14)),
            Expr.Return,
        ),
        'loc_1CBE',
    )

    ChrTalk(
        0x0008,
        (
            '#0540391084V#100F数据水晶中\n',
            '记录着过去所发生的事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391080V看看『卡佩尔』的分析资料的话，\n',
            '或许能够得到什么提示也说不定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E12')

    def _loc_1CBE(): pass

    label('loc_1CBE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D95',
    )

    ChrTalk(
        0x0008,
        (
            '#0540391103V#100F哦，你们几个。\n',
            '听说你们救了空贼团的小姑娘吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391104V关于那个帝国制造的飞艇\n',
            '我也有很多想要调查的地方。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391105V#104F嗯，真想找时间促膝而坐，\n',
            '好好地跟她聊聊这个话题呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    Jump('loc_1E12')

    def _loc_1D95(): pass

    label('loc_1D95')

    ChrTalk(
        0x0008,
        (
            '#0540391106V#100F关于帝国制造的飞艇\n',
            '我也还有很多部分不太清楚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391107V真想找时间跟空贼姑娘\n',
            '好好地聊聊这个话题呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E12(): pass

    label('loc_1E12')

    Jump('loc_26A9')

    def _loc_1E15(): pass

    label('loc_1E15')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_20BB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0458, 1, 0x22C1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2035',
    )

    ChrTalk(
        0x0008,
        (
            '#0540391108V#100F导力引擎总算是发动起来了，\n',
            '但为了慎重起见，先把功率调低。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391109V待稍微观察一下情况后，\n',
            '再切换到普通驱动。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391110V大家就暂时在紧急照明下\n',
            '忍耐着点进行作业吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020391111V#1040F……明白了。\n',
            '在这种状态下\n',
            '不能要求太高呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010391112V#1015F是啊……\n',
            '必须尽量努力才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1FC6',
    )

    ChrTalk(
        0x0008,
        (
            '#0540391113V#100F你们几个\n',
            '也要多加小心啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391114V提妲\n',
            '就拜托你们照顾了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_202F')

    def _loc_1FC6(): pass

    label('loc_1FC6')

    ChrTalk(
        0x0008,
        (
            '#0540391113V#100F你们几个\n',
            '也要多加小心啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391116V如果有什么有趣的发现，\n',
            '请马上过来告诉我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_202F(): pass

    label('loc_202F')

    OP_A2(0x22C1)

    Jump('loc_20B8')

    def _loc_2035(): pass

    label('loc_2035')

    ChrTalk(
        0x0008,
        (
            '#0540391117V#100F目前这个阶段依然还在\n',
            '观察导力引擎的状况如何。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391118V没有问题的话将会从舰内照明\n',
            '开始逐步提升输出功率。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_20B8(): pass

    label('loc_20B8')

    Jump('loc_26A9')

    def _loc_20BB(): pass

    label('loc_20BB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 6, 0x1E1E)),
            Expr.Return,
        ),
        'loc_22CC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C5, 2, 0x1E2A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_20D1',
    )

    Call(0, 0x0005)

    Jump('loc_22C9')

    def _loc_20D1(): pass

    label('loc_20D1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_2189',
    )

    ChrTalk(
        0x0008,
        (
            '#0540391119V#100F我还要再持续\n',
            '进行一下装置的研究。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391120V需要武器或是结晶回路时，\n',
            '找那边的佩顿商量就好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391121V那里有我从中央工房\n',
            '收集而来的精选物品哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_22C9')

    def _loc_2189(): pass

    label('loc_2189')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2250',
    )

    ChrTalk(
        0x0008,
        (
            '#0540391122V#100F距离『装置』的试制品完成\n',
            '只差最后一步了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391123V当你们从塔返回的时候，\n',
            '应该就会成形了才对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391124V#101F哎呀呀，松了一口气。\n',
            '看这个样子似乎来得及呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    Jump('loc_22C9')

    def _loc_2250(): pass

    label('loc_2250')

    ChrTalk(
        0x0008,
        (
            '#0540391125V#100F距离『装置』的试作品完成\n',
            '只差最后一步了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391126V当你们从塔返回的时候，\n',
            '应该就会成形了才对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_22C9(): pass

    label('loc_22C9')

    Jump('loc_26A9')

    def _loc_22CC(): pass

    label('loc_22CC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 1, 0x1E11)),
            Expr.Return,
        ),
        'loc_24BD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C5, 2, 0x1E2A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_22E2',
    )

    Call(0, 0x0005)

    Jump('loc_24BA')

    def _loc_22E2(): pass

    label('loc_22E2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2407',
    )

    ChrTalk(
        0x0008,
        (
            '#0540391127V#100F关于笼罩在塔顶的结界，\n',
            '目前还不清楚详细情况如何。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391128V如果数据水晶的解读顺利，\n',
            '我想或许会得到什么线索……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391129V总而言之，除了『装置』之外，\n',
            '今后也要同时去进行这方面的研究。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391130V无论是『里塔』还是结界，\n',
            '都必定是内容充实的研究课题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    Jump('loc_24BA')

    def _loc_2407(): pass

    label('loc_2407')

    ChrTalk(
        0x0008,
        (
            '#0540391131V#100F无论是『里塔』还是结界，\n',
            '都必定是内容充实的研究课题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391132V#104F实话说，我真想亲自前去\n',
            '观察那些现象呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391133V#102F哼，要是再年轻十岁的话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_24BA(): pass

    label('loc_24BA')

    Jump('loc_26A9')

    def _loc_24BD(): pass

    label('loc_24BD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 2, 0x1E0A)),
            Expr.Return,
        ),
        'loc_26A9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C5, 2, 0x1E2A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_24D3',
    )

    Call(0, 0x0005)

    Jump('loc_26A9')

    def _loc_24D3(): pass

    label('loc_24D3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_2593',
    )

    ChrTalk(
        0x0008,
        (
            '#0540391134V#100F这阵子我会在这里\n',
            '继续进行装置的研究。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391120V需要武器或是结晶回路时，\n',
            '找那边的佩顿商量就好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391136V也请你们几个务必试试看\n',
            '第三级的结晶孔强化哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26A9')

    def _loc_2593(): pass

    label('loc_2593')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_262E',
    )

    ChrTalk(
        0x0008,
        (
            '#0540391137V#100F资料水晶的分析\n',
            '我打算先交给『卡佩尔』处理。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391138V毕竟除了『四轮之塔』的调查外，\n',
            '我还得同时开发那个『装置』呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    Jump('loc_26A9')

    def _loc_262E(): pass

    label('loc_262E')

    ChrTalk(
        0x0008,
        (
            '#0540391139V#100F如果获得了新的水晶，\n',
            '请拿来我这里吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540340994V我会立刻装在『卡佩尔』上，\n',
            '让它开始进行自动分析。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_26A9(): pass

    label('loc_26A9')

    Jump('loc_29C2')

    def _loc_26AC(): pass

    label('loc_26AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C5, 1, 0x1E29)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2910',
    )

    ChrTalk(
        0x0008,
        (
            '#0540391141V#100F怎么了，你们几个。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391142V莫非要进行\n',
            '导力器的调整吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010391143V#1011F嗯，也算是啦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010391144V博士你们在做什么呢？\n',
            '大家都聚在这种地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#0540391145V#100F嗯，我正在\n',
            '听取大家的意见。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540340643V因为刚才在研究中的『某装置』里\n',
            '发现了一些必须要解决的问题。',
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
        'loc_281B',
    )

    ChrTalk(
        0x0107,
        (
            '#0070340644V#064F某装置……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2843')

    def _loc_281B(): pass

    label('loc_281B')

    ChrTalk(
        0x0102,
        (
            '#0020340645V#1044F是某装置……吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2843(): pass

    label('loc_2843')

    ChrTalk(
        0x0101,
        (
            '#0010391149V#1015F好令人在意的说法呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540340647V#104F不好意思，\n',
            '目前只能透露这么多。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540340648V毕竟这或许只是\n',
            '我们杞人忧天的想法吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540340649V#101F总而言之请期待\n',
            '完成的那一刻吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1E29)

    Jump('loc_29C2')

    def _loc_2910(): pass

    label('loc_2910')

    ChrTalk(
        0x0008,
        (
            '#0540391134V#100F这阵子我会在这里\n',
            '继续进行装置的研究。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391120V需要武器或是结晶回路时，\n',
            '找那边的佩顿商量就好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391121V那里有我从中央工房\n',
            '收集而来的精选物品哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_29C2(): pass

    label('loc_29C2')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x29C6
@scena.Code('func_05_29C6')
def func_05_29C6():
    ChrTalk(
        0x0008,
        (
            '#0540340637V#100F嗯？怎么了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540340638V关于数据水晶\n',
            '还有什么问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340639V#1011F不，那个已经明白了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010340640V#1015F不过进行自动解析时，\n',
            '博士在做些什么事呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010340641V虽然说工作交给了『卡佩尔』处理，\n',
            '可是看上去还是很忙的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#0540340642V#100F嗯，其实我正在\n',
            '忙着修正理论。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540340643V因为刚才在研究中的『某装置』里\n',
            '发现了一些必须要解决的问题。',
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
        'loc_2B80',
    )

    ChrTalk(
        0x0107,
        (
            '#0070340644V#064F某装置……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2BA8')

    def _loc_2B80(): pass

    label('loc_2B80')

    ChrTalk(
        0x0102,
        (
            '#0020340645V#1044F是某装置……吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2BA8(): pass

    label('loc_2BA8')

    ChrTalk(
        0x0101,
        (
            '#0010340646V#1015F好、好令人在意的说法呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540340647V#104F不好意思，\n',
            '目前只能透露这么多。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540340648V毕竟这或许只是\n',
            '我们杞人忧天的想法吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540340649V#101F总而言之请期待\n',
            '完成的那一刻吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)
    OP_A2(0x1E2A)

    Return()

# id: 0x0006 offset: 0x2C7A
@scena.Code('func_06_2C7A')
def func_06_2C7A():
    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x00FE,
        0x05,
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x00FE)
    ClearChrFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0xFE, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x00FE,
        0x05,
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_2D0A',
    )

    Jump('loc_2D4C')

    def _loc_2D0A(): pass

    label('loc_2D0A')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2D26',
    )

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2D4C')

    def _loc_2D26(): pass

    label('loc_2D26')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2D42',
    )

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2D4C')

    def _loc_2D42(): pass

    label('loc_2D42')

    ExecExpressionWithValue(
        0x00FE,
        0x08,
        (
            (Expr.GetChrWork, 0xFE, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2D4C(): pass

    label('loc_2D4C')

    ExecExpressionWithValue(
        0x00FE,
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
        0x00FE,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrFlags(0x00FE, 0x0010)
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
            TXT(0x01, '队伍编成\n'),
            TXT(0x02, '放弃\n'),
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
        (0x00000000, 'loc_2DCF'),
        (0x00000001, 'loc_2F18'),
        (0x00000002, 'loc_2F44'),
        (-1, 'loc_2F47'),
    )

    def _loc_2DCF(): pass

    label('loc_2DCF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2E92',
    )

    ChrTalk(
        0x000A,
        (
            '#0050390785V#053F修理也告一段落了，\n',
            '暂时休息一下吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050390786V#050F一旦展开中枢塔的搜索，\n',
            '敌人的抵抗也会逐渐猛烈起来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050390787V可以休息的时候\n',
            '就必须好好地休息才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0010)

    Jump('loc_2F15')

    def _loc_2E92(): pass

    label('loc_2E92')

    ChrTalk(
        0x000A,
        (
            '#0050390788V#050F修理也告一段落了，\n',
            '暂时休息一下吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050390789V敌人的抵抗也会逐渐猛烈起来……\n',
            '能休息时就必须好好休息才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2F15(): pass

    label('loc_2F15')

    Jump('loc_2F47')

    def _loc_2F18(): pass

    label('loc_2F18')

    ChrTalk(
        0x000A,
        (
            '#0050340442V#050F要更换成员吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0015)

    Jump('loc_2F47')

    def _loc_2F44(): pass

    label('loc_2F44')

    Jump('loc_2F47')

    def _loc_2F47(): pass

    label('loc_2F47')

    SetChrSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x2F50
@scena.Code('func_07_2F50')
def func_07_2F50():
    TalkBegin(0x00FE)
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
            TXT(0x01, '队伍编成\n'),
            TXT(0x02, '放弃\n'),
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
        (0x00000000, 'loc_2FB1'),
        (0x00000001, 'loc_4F41'),
        (0x00000002, 'loc_4F6D'),
        (-1, 'loc_4F70'),
    )

    def _loc_2FB1(): pass

    label('loc_2FB1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 3, 0x13)),
            Expr.Return,
        ),
        'loc_306D',
    )

    ChrTalk(
        0x0107,
        (
            '#0070390633V#060F关于塞姆里亚石确切的构成，\n',
            '爷爷似乎也还不清楚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070390634V他说资料既然已经回收，\n',
            '之后再慢慢地分析就好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070390635V嘿嘿，回到工房后\n',
            '又要开始忙碌了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4F3E')

    def _loc_306D(): pass

    label('loc_306D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0447, 2, 0x223A)),
            Expr.Return,
        ),
        'loc_37CD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0448, 0, 0x2240)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3506',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0454, 3, 0x22A3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_346F',
    )

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x000B,
        (
            '#0070390636V#064F咦……\n',
            '姐姐，哥哥。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070390637V……你们怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010390638V#1025F嗯，我们\n',
            '有件事想告诉提妲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010390639V#1003F……玲她…………\n',
            '以执行者的身份出现了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000B,
        (
            '#0070390640V#065F啊？……小玲吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020390641V#1040F嗯……\n',
            '不过她平安无事，请放心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020390642V在和我们战斗之后，\n',
            '她就离开那个地方了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0070390643V#064F……这、这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070390644V#561F太、太好了……\n',
            '她平安无事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010390645V#1015F虽然不知道她有没有\n',
            '真正理解到我们的心意……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010390646V不过那女孩似乎\n',
            '自己开始思考些什么了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020390647V#1040F她在朝着好的方向发展，\n',
            '我想这一点是绝对错不了哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020390648V玲是个聪明的女孩，\n',
            '总有一天会觉察到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 0)

    ChrTalk(
        0x000B,
        (
            '#0070390649V#560F嗯，嗯！\n',
            '一定会的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070390650V#066F真希望有一天……\n',
            '还可以和她一起玩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010390651V#1017F嗯，绝对可以再见面的。\n',
            '只要相信就会成真……不是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010390652V因为我和约修亚一样\n',
            '也是这么重逢的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020390653V#1049F哈哈，说得也是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0070390654V#560F啊……嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x22A3)

    Jump('loc_3503')

    def _loc_346F(): pass

    label('loc_346F')

    ChrTalk(
        0x000B,
        (
            '#0070390655V#060F加入『结社』\n',
            '是一个错误……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070390656V玲她自己\n',
            '一定会察觉到这点的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070390657V要是将来有一天\n',
            '能够再一起去买东西就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3503(): pass

    label('loc_3503')

    Jump('loc_37CA')

    def _loc_3506(): pass

    label('loc_3506')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0454, 3, 0x22A3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3727',
    )

    ChrTalk(
        0x000B,
        (
            '#0070390658V#063F虽然不知道玲\n',
            '跑去了哪里……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070390659V但她一定会靠着\n',
            '自己的力量察觉到错误吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020390647V#1040F她在朝着好的方向发展，\n',
            '我想这一点是绝对错不了哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020390648V玲是个聪明的女孩，\n',
            '总有一天会觉察到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 0)

    ChrTalk(
        0x000B,
        (
            '#0070390649V#560F嗯，嗯！\n',
            '一定会的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070390650V#066F真希望有一天……\n',
            '还可以和她一起玩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010390651V#1017F嗯，绝对可以再见面的。\n',
            '只要相信就会成真……不是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010390652V因为我和约修亚一样\n',
            '也是这么重逢的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020390653V#1049F哈哈，说得也是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0070390654V#560F啊……嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x22A3)

    Jump('loc_37CA')

    def _loc_3727(): pass

    label('loc_3727')

    ChrTalk(
        0x000B,
        (
            '#0070390668V#560F玲她一定会靠着\n',
            '自己的力量察觉到错误吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070390669V我也要像姐姐一样\n',
            '去试着相信玲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070390670V#067F然后，将来有一天\n',
            '再和她一起去买东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_37CA(): pass

    label('loc_37CA')

    Jump('loc_4F3E')

    def _loc_37CD(): pass

    label('loc_37CD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Return,
        ),
        'loc_38B6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_384C',
    )

    ChrTalk(
        0x000B,
        (
            '#0070390671V#060F飞翔引擎的测试……\n',
            '不知道能不能顺利通过。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070390672V#067F唉……\n',
            '心里觉得好紧张。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    Jump('loc_38B3')

    def _loc_384C(): pass

    label('loc_384C')

    ChrTalk(
        0x000B,
        (
            '#0070390673V#060F飞翔引擎的测试……\n',
            '不知道能不能顺利通过。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070390674V#067F既、既紧张又兴奋……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_38B3(): pass

    label('loc_38B3')

    Jump('loc_4F3E')

    def _loc_38B6(): pass

    label('loc_38B6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 1, 0x2219)),
            Expr.Return,
        ),
        'loc_3FE7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0454, 2, 0x22A2)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Ez,
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0454, 2, 0x22A2)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Or,
            Expr.Return,
        ),
        'loc_3ADF',
    )

    ChrTurnDirection(0x00FE, 0x010B, 0)

    ChrTalk(
        0x000B,
        (
            '#0070390675V#064F啊，空贼姐姐……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070390676V#560F那个那个……\n',
            '我叫提妲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070390677V今、今后\n',
            '请多多指教。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0458, 2, 0x22C2)),
            Expr.Return,
        ),
        'loc_39D9',
    )

    ChrTalk(
        0x010B,
        (
            '#0090390678V#413F我说啊，\n',
            '我的名字叫乔丝特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090390679V你们所有人可不可以\n',
            '别再用奇怪的称呼叫我了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3A2C')

    def _loc_39D9(): pass

    label('loc_39D9')

    ChrTalk(
        0x010B,
        (
            '#0090390680V#213F空、空贼姐姐？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090390681V#215F我说啊，\n',
            '我的名字是乔丝特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3A2C(): pass

    label('loc_3A2C')

    OP_62(0x000B, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(400)

    ChrTalk(
        0x000B,
        (
            '#0070390682V#065F啊……！？\n',
            '对不起空贼姐姐……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070390683V#067F……不是的，\n',
            '是乔丝特小姐对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090390684V#216F（你、你是故意的吧？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0006)
    OP_A2(0x22A2)

    Jump('loc_3FE4')

    def _loc_3ADF(): pass

    label('loc_3ADF')

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3B6E',
    )

    ChrTurnDirection(0x00FE, 0x010B, 0)

    ChrTalk(
        0x000B,
        (
            '#0070390685V#560F那个，乔丝特小姐。\n',
            '今后请你多多指教。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070390686V大、大家能够和睦相处\n',
            '果然还是比较开心呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3FE4')

    def _loc_3B6E(): pass

    label('loc_3B6E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Return,
        ),
        'loc_3E89',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0459, 5, 0x22CD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3DE4',
    )

    ChrTalk(
        0x000B,
        (
            '#0070390687V#560F啊，欢迎回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010390688V#1006F提妲也辛苦了。\n',
            '你看起来非常努力呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x000B,
        (
            '#0070390689V#060F嗯，我正在检查照明设备。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070390690V虽然切换成普通照明了，\n',
            '但是万一因此加重负荷就不好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020390691V#1040F原来如此……\n',
            '修理的状况怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x000B,
        (
            '#0070390692V#060F爷爷他们\n',
            '已经开始调整飞翔引擎了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070390693V听说在调整结束之后，准备\n',
            '进行引擎的仿真升空测试。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3D56',
    )

    ChrTalk(
        0x010B,
        (
            '#0090390694V#213F哦，好厉害啊。\n',
            '已经做到这个地步了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3D93')

    def _loc_3D56(): pass

    label('loc_3D56')

    ChrTalk(
        0x0102,
        (
            '#0020390695V#1040F不愧是博士……\n',
            '已经进行到这个程度了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3D93(): pass

    label('loc_3D93')

    ChrTalk(
        0x000B,
        (
            '#0070390696V#067F嘿嘿，只差一点点哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070390697V我也会努力帮忙的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x22CD)

    Jump('loc_3E86')

    def _loc_3DE4(): pass

    label('loc_3DE4')

    ChrTalk(
        0x000B,
        (
            '#0070390692V#060F爷爷他们\n',
            '已经开始调整飞翔引擎了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070390699V听说在调整结束之后，准备\n',
            '进行引擎的仿真升空测试。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070390700V距离可以起飞\n',
            '只差一小步了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_3E86(): pass

    label('loc_3E86')

    Jump('loc_3FE4')

    def _loc_3E89(): pass

    label('loc_3E89')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3F75',
    )

    ChrTalk(
        0x000B,
        (
            '#0070390701V#060F预计再等一下就要\n',
            '切换回原来的照明系统。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070390702V所以现在正在为此\n',
            '进行导力系统的检查……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070390703V这个步骤结束后，\n',
            '就可以连接结晶回路了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070390704V#067F到时会变得很明亮，\n',
            '大家拭目以待吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    Jump('loc_3FE4')

    def _loc_3F75(): pass

    label('loc_3F75')

    ChrTalk(
        0x000B,
        (
            '#0070390705V#060F预计再等一下就要\n',
            '切换回原来的照明系统。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070390706V到时会变得很明亮，\n',
            '大家拭目以待吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3FE4(): pass

    label('loc_3FE4')

    Jump('loc_4F3E')

    def _loc_3FE7(): pass

    label('loc_3FE7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_4428',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0458, 0, 0x22C0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_43B6',
    )

    ChrTurnDirection(0x000B, 0x0101, 0)

    ChrTalk(
        0x000B,
        (
            '#0070271311V#060F啊，姐姐是你们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070390708V正如爷爷所说的，\n',
            '导力引擎好像没有问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070390709V其它飞翔引擎的情况\n',
            '必须等检查后才会知道……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070390710V不过也许比预想中更快\n',
            '就可以起飞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010390711V#1006F啊，这可真是个好消息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020390712V#1040F真是个让人开心的消息呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020390713V……提妲\n',
            '也要努力帮忙哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x0102, 400)

    ChrTalk(
        0x000B,
        (
            '#0070390714V#560F嗯，那当然！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070390715V#067F啊哈～，想不到竟然可以\n',
            '接触『埃尔赛尤』的飞翔引擎……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070390716V嘿、嘿嘿嘿……\n',
            '真是好开心呀～⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(60)

    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(120)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4246',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    Jump('loc_4284')

    def _loc_4246(): pass

    label('loc_4246')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_426D',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    Jump('loc_4284')

    def _loc_426D(): pass

    label('loc_426D')

    OP_62(0x00F8, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    def _loc_4284(): pass

    label('loc_4284')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_42AB',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    Jump('loc_42E9')

    def _loc_42AB(): pass

    label('loc_42AB')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_42D2',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    Jump('loc_42E9')

    def _loc_42D2(): pass

    label('loc_42D2')

    OP_62(0x00F9, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    def _loc_42E9(): pass

    label('loc_42E9')

    Sleep(1000)

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4359',
    )

    ChrTalk(
        0x0106,
        (
            '#0050390717V#551F看起来好像\n',
            '变了一个人似的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010390718V#1016F啊、啊哈哈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_43B0')

    def _loc_4359(): pass

    label('loc_4359')

    ChrTalk(
        0x0101,
        (
            '#0010191053V#1016F啊、啊哈哈……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010390720V……似乎燃起了\n',
            '她对于机械的狂热呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_43B0(): pass

    label('loc_43B0')

    OP_A2(0x22C0)

    Jump('loc_4425')

    def _loc_43B6(): pass

    label('loc_43B6')

    ChrTalk(
        0x000B,
        (
            '#0070390721V#067F啊哈～，『埃尔赛尤』的\n',
            '导力引擎和结晶回路吗～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070390722V嘿、嘿嘿嘿……\n',
            '真是好开心呀⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_4425(): pass

    label('loc_4425')

    Jump('loc_4F3E')

    def _loc_4428(): pass

    label('loc_4428')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 6, 0x1E1E)),
            Expr.Return,
        ),
        'loc_45AC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C8, 1, 0x1E41)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_456C',
    )

    ChrTurnDirection(0x000B, 0x0101, 0)

    ChrTalk(
        0x000B,
        (
            '#0070340582V#063F啊……\n',
            '姐姐，哥哥……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340583V#1010F没关系……\n',
            '我知道你想说什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010340584V#1000F玲的事情\n',
            '就交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340585V#1040F虽然不知道\n',
            '能不能顺利解决……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020340586V但无论如何，现在\n',
            '只能尽一切最大的努力了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x0102, 400)

    ChrTalk(
        0x000B,
        (
            '#0070340587V#063F嗯，嗯……拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1E41)

    Jump('loc_45A9')

    def _loc_456C(): pass

    label('loc_456C')

    ChrTurnDirection(0x000B, 0x0101, 0)

    ChrTalk(
        0x000B,
        (
            '#0070340588V#063F姐姐，哥哥……\n',
            '玲就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_45A9(): pass

    label('loc_45A9')

    Jump('loc_4F3E')

    def _loc_45AC(): pass

    label('loc_45AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 1, 0x1E11)),
            Expr.Return,
        ),
        'loc_48FB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C5, 3, 0x1E2B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_487F',
    )

    ChrTalk(
        0x000B,
        (
            '#0070340589V#060F啊，姐姐是你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340590V#1001F嗨，提妲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030340591V#020F博士的研究进展如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x0103, 400)

    ChrTalk(
        0x000B,
        (
            '#0070340592V#063F嗯、嗯嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070340593V#561F似乎就连神通广大的爷爷\n',
            '也正在为结界烦恼。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070340594V他说还是不明白它的原理……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340595V#1015F是、是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340596V#1043F结界与执行者的目的\n',
            '应该有着某种关联才对……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020340597V用普通的方法\n',
            '看来还是行不通的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030340598V#020F算了，在这里\n',
            '发牢骚也无济于事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030340599V研究就交给博士，\n',
            '我们几个向着塔进发吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030340600V如果塔的调查有所进展，\n',
            '应该会找到研究的线索才对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010340601V#1011F啊，嗯……\n',
            '还有数据水晶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0103, 400)

    ChrTalk(
        0x0102,
        (
            '#0020340602V#1040F说得也是。\n',
            '目前就集中在塔的调查上吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1E2B)

    Jump('loc_48F8')

    def _loc_487F(): pass

    label('loc_487F')

    ChrTalk(
        0x000B,
        (
            '#0070340603V#063F似乎就连神通广大的爷爷\n',
            '也正在为结界烦恼。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070340604V要是姐姐你们在调查中\n',
            '可以找到线索就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_48F8(): pass

    label('loc_48F8')

    Jump('loc_4F3E')

    def _loc_48FB(): pass

    label('loc_48FB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 2, 0x1E0A)),
            Expr.Return,
        ),
        'loc_4905',
    )

    Jump('loc_4F3E')

    def _loc_4905(): pass

    label('loc_4905')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            Expr.Return,
        ),
        'loc_4F3E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C5, 4, 0x1E2C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4EDD',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_49FC',
    )

    ChrTalk(
        0x000B,
        (
            '#0070340605V#060F阿、阿加特哥哥……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050340606V#051F哟，小鬼。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050340607V你这么迫不及待地\n',
            '跑来给爷爷添麻烦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0070340608V#063F我、我不是在添麻烦啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070340609V我、我只是看一下\n',
            '研究的情况而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4AAA')

    def _loc_49FC(): pass

    label('loc_49FC')

    ChrTalk(
        0x000B,
        (
            '#0070340610V#060F啊，姐姐，是你们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340611V#1001F啊哈哈，这么快\n',
            '就跑到博士这里来了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0070340612V#560F嗯、嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070340613V我来看一下\n',
            '研究的情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4AAA(): pass

    label('loc_4AAA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C5, 1, 0x1E29)),
            Expr.Return,
        ),
        'loc_4B30',
    )

    ChrTalk(
        0x0102,
        (
            '#0020340614V#1043F塔的现象分析以及\n',
            '那个『装置』的开发吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020340615V同时指挥着两项工作\n',
            '看来就算是博士也会很辛苦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4C7B')

    def _loc_4B30(): pass

    label('loc_4B30')

    ChrTalk(
        0x0102,
        (
            '#0020340616V#1040F已经开始对塔的现象\n',
            '着手进行分析了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x0102, 400)

    ChrTalk(
        0x000B,
        (
            '#0070340617V#060F嗯，正在分析中……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070340618V#561F不过爷爷似乎\n',
            '还在进行着别的研究。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340619V#1004F别、别的研究？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340620V#1044F不光是分析现象而已，\n',
            '一方面也在进行别的研究吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020340621V同时指挥着两项工作，\n',
            '看来就算是博士也会很辛苦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4C7B(): pass

    label('loc_4C7B')

    ChrTurnDirection(0x000B, 0x0102, 400)

    ChrTalk(
        0x000B,
        (
            '#0070340622V#060F嗯，所以说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070340623V如果有我能做的事，\n',
            '我会非常乐意帮忙的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070340624V当然，我也会帮姐姐你们\n',
            '进行调查……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340625V#1006F好啊。\n',
            '就这么决定吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010340626V需要提妲帮忙的时候\n',
            '我们会过来找你的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340627V#1049F说得也是。\n',
            '而且博士这边也需要助手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4E85',
    )

    ChrTalk(
        0x0106,
        (
            '#0050340628V#552F是啊，如果不管管老爷子的话，\n',
            '搞不好他的两项研究会变成三项呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050340629V……还是好好地看着他吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0070340630V#560F嘿嘿，也对……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070340631V阿加特哥哥……\n',
            '你也要多加小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4ED7')

    def _loc_4E85(): pass

    label('loc_4E85')

    ChrTalk(
        0x000B,
        (
            '#0070340632V#560F嗯，嗯！　我会努力的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070340633V姐姐你们要\n',
            '多加小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4ED7(): pass

    label('loc_4ED7')

    OP_A2(0x1E2C)

    Jump('loc_4F3E')

    def _loc_4EDD(): pass

    label('loc_4EDD')

    ChrTalk(
        0x000B,
        (
            '#0070340634V#060F虽然我正在担任\n',
            '爷爷的助手……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070340635V不过需要我的话\n',
            '请随时跟我说哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4F3E(): pass

    label('loc_4F3E')

    Jump('loc_4F70')

    def _loc_4F41(): pass

    label('loc_4F41')

    ChrTalk(
        0x000B,
        (
            '#0070340636V#060F要更换成员吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0015)

    Jump('loc_4F70')

    def _loc_4F6D(): pass

    label('loc_4F6D')

    Jump('loc_4F70')

    def _loc_4F70(): pass

    label('loc_4F70')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x4F74
@scena.Code('func_08_4F74')
def func_08_4F74():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_4F9C',
    )

    ChrTalk(
        0x00FE,
        (
            '#070F◆没有台词。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0015)

    Jump('loc_557C')

    def _loc_4F9C(): pass

    label('loc_4F9C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 6, 0x1A1E)),
            Expr.Return,
        ),
        'loc_557C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 2, 0x1A22)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_54EB',
    )

    @scena.Lambda('lambda_4FB1')
    def lambda_4FB1():
        ChrTurnDirection(0x000C, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_4FB1)

    SetChrChipByIndex(0x000C, 4)
    SetChrSubChip(0x000C, 0)
    WaitForThreadExit(0x000C, 0x0001)

    ChrTalk(
        0x000C,
        (
            '#0080310458V#070F哟，这不是艾丝蒂尔吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080310459V怎么跑到这里来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310460V#1000F金先生也是。\n',
            '在这种地方做什么呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310461V#1018F啊，莫非是在睡午觉？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0080310462V#071F哈哈，那倒也不错，\n',
            '不过我正想稍微训练一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080310463V一直待在狭小的地方不动，\n',
            '总觉得老是无法平静下来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080310464V#070F话说回来，你好像\n',
            '也正在四处散步啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310465V#1007F我也很不擅长待在\n',
            '同一个地方不动……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310466V#1015F不过虽说是训练……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 180, 400)
    Sleep(500)

    OP_8C(0x0101, 0, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010310467V#1015F……在这里运动\n',
            '不会太过狭窄吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0080310468V#070F怎么会，并非只有运动\n',
            '才可以算得上是训练。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080310469V只要有了这样的空间，\n',
            '可以做的事情很多呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000C, 400)

    ChrTalk(
        0x0101,
        (
            '#0010310470V#1000F咦，比如说呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0080310471V#074F瞑想或呼吸法这些就不用提了，\n',
            '形态的复习也是一种重要的锻炼。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080310472V我们游击士\n',
            '动不动就进行实战，很容易崩溃的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080310473V#070F有时候回归到基础层面，\n',
            '调整好自我也是很重要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310474V#1013F的确，我最近好像\n',
            '好像的确没怎么做形态练习。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010310475V听金先生这么一说，\n',
            '有点着急呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0080310476V#070F哈哈，别那么在意。\n',
            '我刚才说的只是一般的理论。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080310477V不过，要是你有这个想法的话，\n',
            '试着专心练习一下没有坏处的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080310478V如果不嫌弃，\n',
            '我很愿意当你练习的对手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310479V#1001F嘿嘿，到时候\n',
            '就拜托你了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0080310480V#070F嗯，我很期待。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000C, 90, 400)
    SetChrChipByIndex(0x000C, 14)
    SetChrSubChip(0x000C, 0)
    OP_A2(0x1A22)

    Jump('loc_557C')

    def _loc_54EB(): pass

    label('loc_54EB')

    @scena.Lambda('lambda_54F1')
    def lambda_54F1():
        ChrTurnDirection(0x000C, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_54F1)

    SetChrChipByIndex(0x000C, 4)
    SetChrSubChip(0x000C, 0)
    WaitForThreadExit(0x000C, 0x0001)

    ChrTalk(
        0x000C,
        (
            '#0080310481V#070F我打算在这里\n',
            '继续练习一阵子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080310482V在龙出现之前\n',
            '让身体慢慢地热起来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000C, 90, 400)
    SetChrChipByIndex(0x000C, 14)
    SetChrSubChip(0x000C, 0)

    def _loc_557C(): pass

    label('loc_557C')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x5580
@scena.Code('func_09_5580')
def func_09_5580():
    TalkBegin(0x00FE)
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
            TXT(0x01, '队伍编成\n'),
            TXT(0x02, '放弃\n'),
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
        (0x00000000, 'loc_55E1'),
        (0x00000001, 'loc_6B5D'),
        (0x00000002, 'loc_6B99'),
        (-1, 'loc_6B9C'),
    )

    def _loc_55E1(): pass

    label('loc_55E1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Return,
        ),
        'loc_579E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_570F',
    )

    ChrTalk(
        0x000D,
        (
            '#0180390802V#1060F剩下的探索地点是中枢塔……\n',
            '感觉终于要迎接最后结局了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180390803V『结社』的那些家伙\n',
            '应该也会认真起来了，\n',
            '用一般的方法大概行不通……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180390804V好了，既然已经走到这一步\n',
            '我们就要朝着圆满的结局去努力。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180390805V早点找到『辉之环』\n',
            '大家一起返回地面吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000C)

    Jump('loc_579B')

    def _loc_570F(): pass

    label('loc_570F')

    ChrTalk(
        0x000D,
        (
            '#0180390806V#1060F剩下的探索地点是中枢塔……\n',
            '有种要迎接最后结局的感觉呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180390807V不嫌弃的话，我会贡献一份力量。\n',
            '欢迎随时来找我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_579B(): pass

    label('loc_579B')

    Jump('loc_6B5A')

    def _loc_579E(): pass

    label('loc_579E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Return,
        ),
        'loc_591C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5899',
    )

    ChrTalk(
        0x000D,
        (
            '#0180390808V#1060F听说空贼团那些家伙\n',
            '要跟我们一起合作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180390809V嗯，我倒是很赞成。\n',
            '毕竟同伴越多越好嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180390810V其实，我也正在考虑\n',
            '自己可以帮上什么忙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180390811V像是提供药品之类的，\n',
            '总之先从这些方面开始做起吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000C)

    Jump('loc_5919')

    def _loc_5899(): pass

    label('loc_5899')

    ChrTalk(
        0x000D,
        (
            '#0180390812V#1060F我自己也在考虑\n',
            '能够对空贼团进行哪些协助。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180390811V像是提供药品之类的，\n',
            '总之先从这些方面开始做起吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5919(): pass

    label('loc_5919')

    Jump('loc_6B5A')

    def _loc_591C(): pass

    label('loc_591C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 1, 0x2219)),
            Expr.Return,
        ),
        'loc_5CE8',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.TestScenaFlags, ScenaFlag(0x0454, 4, 0x22A4)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5AD3',
    )

    ChrTurnDirection(0x00FE, 0x010B, 0)

    ChrTalk(
        0x000D,
        (
            '#0180390814V#1060F你叫乔丝特对吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180390815V我叫凯文·格拉汉姆。\n',
            '是七耀教会的神父。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180390816V#1061F我最欢迎可爱的女孩子，\n',
            '所以今后就请多多指教啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090390817V#215F嗯，嗯……\n',
            '多多指教倒是无妨……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090390818V#212F……不过你真的是神父吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0180390819V#1060F嗯！如假包换。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180390820V#1064F……喂，什么嘛，\n',
            '那摆明就是怀疑的眼神。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090390821V#212F（盯─────……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000D)
    OP_A2(0x22A4)

    Jump('loc_5CE5')

    def _loc_5AD3(): pass

    label('loc_5AD3')

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5B94',
    )

    ChrTurnDirection(0x00FE, 0x010B, 0)

    ChrTalk(
        0x000D,
        (
            '#0180390822V#1064F我说啊，我可是\n',
            '如假包换的神父啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180390823V#1068F唉，居然被一个小女孩怀疑，\n',
            '我真是太悲哀了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090390824V#413F（果、果然很可疑……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5CE5')

    def _loc_5B94(): pass

    label('loc_5B94')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5C63',
    )

    ChrTalk(
        0x000D,
        (
            '#0180390825V#1063F大概是体力劳动太多的缘故，\n',
            '受伤的人相当多。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180390826V不过，虽说只是擦伤而已，\n',
            '大家还是要多加小心才行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180390827V不知道得坚持到什么时候，\n',
            '而且药还是必须省着点用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000C)

    Jump('loc_5CE5')

    def _loc_5C63(): pass

    label('loc_5C63')

    ChrTalk(
        0x000D,
        (
            '#0180390825V#1063F大概是体力劳动太多的缘故，\n',
            '受伤的人相当多。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180390829V不过，虽说只是擦伤而已，\n',
            '大家还是要多加小心才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5CE5(): pass

    label('loc_5CE5')

    Jump('loc_6B5A')

    def _loc_5CE8(): pass

    label('loc_5CE8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_5E51',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5DD4',
    )

    ChrTalk(
        0x000D,
        (
            '#0180390830V#1062F哟，是艾丝蒂尔你们啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180390831V医务室也刚好\n',
            '收拾完毕了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180390832V#1066F由于迫降时的冲击，\n',
            '导致架子内部全都倒塌了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180390833V不过，如果身体不舒服的话\n',
            '可别客气，尽管来找我就是了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000C)

    Jump('loc_5E4E')

    def _loc_5DD4(): pass

    label('loc_5DD4')

    ChrTalk(
        0x000D,
        (
            '#0180390834V#1060F如果身体不舒服的话，\n',
            '随时来找我就是了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180390835V干我们这一行的，\n',
            '再怎么说，身体也都是本钱啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5E4E(): pass

    label('loc_5E4E')

    Jump('loc_6B5A')

    def _loc_5E51(): pass

    label('loc_5E51')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 6, 0x1E1E)),
            Expr.Return,
        ),
        'loc_63D3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C5, 6, 0x1E2E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_62BB',
    )

    ChrTalk(
        0x000D,
        (
            '#0180390836V#1067F哎呀呀……\n',
            '最后的执行者是那个小姑娘吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180390837V我还在心里暗自想着，\n',
            '她要是这次不会出现就好了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180390838V#1068F嗯，天底下毕竟\n',
            '不会有这么顺利的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010390839V#1003F嗯……\n',
            '一开始我也那么想……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010390840V#1002F不过换个角度来看，\n',
            '这也许这是个很好的机会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x0101, 400)

    ChrTalk(
        0x000D,
        (
            '#0180390841V#1064F咦……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010390842V#1015F我们希望她能退出结社，\n',
            '同时也有很多话想对她说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010390843V像这种想要传达什么事情时候，\n',
            '直接见面是无疑最好的方法了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0180390844V#1066F哈哈，原来如此。\n',
            '这种想法也是很有道理呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180390845V#1071F不愧是艾丝蒂尔。\n',
            '思考方式相当地乐观呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180390846V哎～，真是越来越………………\n',
            '……………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180390847V#1063F……咳咳，没什么没什么。\n',
            '只是不自觉就按平常的方式说话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    OP_22(0x0026, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010390848V#1011F越来越……怎样呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0180390849V#1068F啊，你就别去在意了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020390850V#1048F对不起，凯文先生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x0102, 400)

    ChrTalk(
        0x000D,
        (
            '#0180390851V#1066F没关系没关系。\n',
            '反正是我不好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180390852V原谅我吧，\n',
            '下次我会注意气氛的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010390853V#1019F……又是男人之间\n',
            '在悄悄地互通声气。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010390854V看起来真的好恶心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000C)
    OP_A2(0x1E2E)

    Jump('loc_63D0')

    def _loc_62BB(): pass

    label('loc_62BB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_6360',
    )

    ChrTalk(
        0x000D,
        (
            '#0180390855V#1060F不过，不管怎么说，\n',
            '像艾丝蒂尔这样乐观积极的\n',
            '思考方式是相当不错的呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180390856V哎，面对这样积极的女孩，\n',
            '大哥哥丝毫没有抵抗力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_63D0')

    def _loc_6360(): pass

    label('loc_6360')

    ChrTalk(
        0x000D,
        (
            '#0180390857V#1060F艾丝蒂尔说得对，\n',
            '我们要积极地行动下去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180390858V光是想着坏的一面\n',
            '是完全无济于事的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_63D0(): pass

    label('loc_63D0')

    Jump('loc_6B5A')

    def _loc_63D3(): pass

    label('loc_63D3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 1, 0x1E11)),
            Expr.Return,
        ),
        'loc_654E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_64EA',
    )

    ChrTalk(
        0x000D,
        (
            '#0180340549V#1064F不过，想不到居然能够\n',
            '一个人独自登上里塔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180340550V真是一位\n',
            '可怕的大姐姐呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180340551V#1064F看来我们这些男生\n',
            '也必须多加小心才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x0102, 400)

    ChrTalk(
        0x000D,
        (
            '#0180340552V#1061F……对吧，约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340553V#1048F……为、为什么问我？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000C)

    Jump('loc_654B')

    def _loc_64EA(): pass

    label('loc_64EA')

    ChrTalk(
        0x000D,
        (
            '#0180340554V#1060F想不到居然能够\n',
            '一个人独自登上里塔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180340555V女人的执念真是可怕极了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_654B(): pass

    label('loc_654B')

    Jump('loc_6B5A')

    def _loc_654E(): pass

    label('loc_654E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 2, 0x1E0A)),
            Expr.Return,
        ),
        'loc_66EA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_665D',
    )

    ChrTalk(
        0x000D,
        (
            '#0180340556V#1063F在塔内延伸开来的『里塔』\n',
            '以及塔顶的『福音β』吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180340557V虽然还不清楚敌人的目的，\n',
            '不过感觉是越来越可疑了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180340558V#1062F总之，这种时候\n',
            '必须要互相帮助才行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180340559V我也已经准备好了，\n',
            '需要的时候随时跟我说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000C)

    Jump('loc_66E7')

    def _loc_665D(): pass

    label('loc_665D')

    ChrTalk(
        0x000D,
        (
            '#0180340556V#1063F在塔内延伸开来的『里塔』\n',
            '以及塔顶的『福音β』吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180340561V虽然还不清楚敌人的目的，\n',
            '不过感觉是越来越可疑了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_66E7(): pass

    label('loc_66E7')

    Jump('loc_6B5A')

    def _loc_66EA(): pass

    label('loc_66EA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            Expr.Return,
        ),
        'loc_6B5A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C5, 5, 0x1E2D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6AEC',
    )

    ChrTalk(
        0x000D,
        (
            '#0180340562V#1062F哦，是艾丝蒂尔你们。\n',
            '现在要前往塔内吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340563V#1006F嗯，准备好就出发。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010340564V凯文先生在做什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x0101, 400)

    ChrTalk(
        0x000D,
        (
            '#0180340565V#1060F我刚刚参观完\n',
            '这艘船上的医疗设施。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180340566V毕竟等到要使用的时候\n',
            '再开始准备就太晚了嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340567V#1049F想不到您也具备现代医学的知识，\n',
            '真不愧是『星杯骑士』呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x0102, 400)

    ChrTalk(
        0x000D,
        (
            '#0180340568V#1066F哈哈，竟然会受到这种恭维。\n',
            '其实我只是赶鸭子上架而已啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180340569V再说，我也不是\n',
            '负责掌管这个房间的人。',
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
        'loc_6913',
    )

    ChrTalk(
        0x0105,
        (
            '#0060340570V#047F是啊，您说得没错呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_69BA')

    def _loc_6913(): pass

    label('loc_6913')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6947',
    )

    ChrTalk(
        0x0108,
        (
            '#0080340571V#070F啊，是啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_69BA')

    def _loc_6947(): pass

    label('loc_6947')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6983',
    )

    ChrTalk(
        0x0103,
        (
            '#0030340572V#026F嗯，跟您说的一样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_69BA')

    def _loc_6983(): pass

    label('loc_6983')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_69BA',
    )

    ChrTalk(
        0x0106,
        (
            '#0050340573V#050F嗯嗯，完全正确……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_69BA(): pass

    label('loc_69BA')

    ChrTalk(
        0x0101,
        (
            '#0010340574V#1002F为了不麻烦神父治疗，\n',
            '进行搜索时必须谨慎点才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340575V#1042F嗯，小心翼翼地前进吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020340576V而且也不知道塔本身\n',
            '还隐藏着什么样的危险。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0180340577V#1060F没错没错，这种\n',
            '小心谨慎的心态是最重要的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180340578V无论如何，大家都不要勉强，\n',
            '一起平平安安地回来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1E2D)

    Jump('loc_6B5A')

    def _loc_6AEC(): pass

    label('loc_6AEC')

    ChrTalk(
        0x000D,
        (
            '#0180340579V#1060F这个地方若是派不上用场，\n',
            '那就再好不过了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180340580V艾丝蒂尔你们\n',
            '也一定要多加小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6B5A(): pass

    label('loc_6B5A')

    Jump('loc_6B9C')

    def _loc_6B5D(): pass

    label('loc_6B5D')

    ChrTalk(
        0x000D,
        (
            '#0180340581V#1060F好了，来了。\n',
            '要调换成员是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0015)

    Jump('loc_6B9C')

    def _loc_6B99(): pass

    label('loc_6B99')

    Jump('loc_6B9C')

    def _loc_6B9C(): pass

    label('loc_6B9C')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x6BA0
@scena.Code('func_0A_6BA0')
def func_0A_6BA0():
    TalkBegin(0x00FE)
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
            TXT(0x01, '队伍编成\n'),
            TXT(0x02, '放弃\n'),
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
        (0x00000000, 'loc_6C01'),
        (0x00000001, 'loc_6F8B'),
        (0x00000002, 'loc_6FC2'),
        (-1, 'loc_6FC5'),
    )

    def _loc_6C01(): pass

    label('loc_6C01')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Return,
        ),
        'loc_6D64',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6CDB',
    )

    ChrTalk(
        0x000E,
        (
            '#0090391332V#210F『山猫号』的修理\n',
            '似乎也进展顺利。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090391333V航行控制的问题\n',
            '在接受拉赛尔博士的建议后，\n',
            '好像也已经设法解决了哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090391334V真不愧是王国第一的学者，\n',
            '连吉尔哥也深感佩服呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000F)

    Jump('loc_6D61')

    def _loc_6CDB(): pass

    label('loc_6CDB')

    ChrTalk(
        0x000E,
        (
            '#0090391332V#210F『山猫号』的修理\n',
            '似乎也进展顺利。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090391336V航行控制的问题\n',
            '在接受拉赛尔博士的建议后，\n',
            '好像也已经设法解决了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6D61(): pass

    label('loc_6D61')

    Jump('loc_6F88')

    def _loc_6D64(): pass

    label('loc_6D64')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Return,
        ),
        'loc_6F88',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0459, 6, 0x22CE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6F0B',
    )

    ChrTalk(
        0x000E,
        (
            '#0090391337V#210F喂，你们几个。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090391338V虽说我是联络员，\n',
            '不过有事也要让我帮忙啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090391339V而且你们还救了大哥他们，\n',
            '我可不想再继续欠人情了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010391340V#1007F呼，该说你这个人\n',
            '好强还是固执好呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020391341V#1040F不过，多亏有你帮忙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020391342V因为我们游击士\n',
            '没办法帮忙维护装备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000E, 0x0102, 400)

    ChrTalk(
        0x000E,
        (
            '#0090391343V#414F…………啊…………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090391344V#415F嗯，嗯！就交给我吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x22CE)

    Jump('loc_6F88')

    def _loc_6F0B(): pass

    label('loc_6F0B')

    ChrTalk(
        0x000E,
        (
            '#0090391345V#210F虽说我是联络员\n',
            '不过有事也要让我帮忙啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090391346V而且你们还救了大哥他们，\n',
            '我可不想再继续欠人情了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6F88(): pass

    label('loc_6F88')

    Jump('loc_6FC5')

    def _loc_6F8B(): pass

    label('loc_6F8B')

    ChrTalk(
        0x000E,
        (
            '#0090391347V#210F嘿嘿，\n',
            '果然没有我不行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0015)

    Jump('loc_6FC5')

    def _loc_6FC2(): pass

    label('loc_6FC2')

    Jump('loc_6FC5')

    def _loc_6FC5(): pass

    label('loc_6FC5')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x6FC9
@scena.Code('func_0B_6FC9')
def func_0B_6FC9():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 6, 0x1A1E)),
            Expr.Return,
        ),
        'loc_7173',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_710D',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然之前反复进行过\n',
            '挑战性能极限的测试……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是测试终究是测试。\n',
            '与实战中的机动完全是两回事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '新型引擎究竟能发挥多大作用，\n',
            '我们开发者也是怀着\n',
            '期待与不安各半的心情啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，只要顺利完成本次作战，\n',
            '这个引擎也就可以独当一面了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就让我像送别离巢的雏鸟那样，\n',
            '来记录下最后的数据吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_7173')

    def _loc_710D(): pass

    label('loc_710D')

    ChrTalk(
        0x00FE,
        (
            '虽说之前反复进行了测试\n',
            '但实战毕竟是完全不同的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们开发者也是怀着\n',
            '期待与不安各半的心情啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7173(): pass

    label('loc_7173')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x7177
@scena.Code('func_0C_7177')
def func_0C_7177():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 6, 0x1A1E)),
            Expr.Return,
        ),
        'loc_7266',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7222',
    )

    ChrTalk(
        0x00FE,
        (
            '好了……\n',
            '计量器的检查完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '毕竟作战中的引擎状态\n',
            '可不是每天都能测量到的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了今后导力引擎的开发，\n',
            '必须好好利用这次机会才行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    Jump('loc_7266')

    def _loc_7222(): pass

    label('loc_7222')

    ChrTalk(
        0x00FE,
        (
            '好了……\n',
            '计量器的检查完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，接下来\n',
            '就等龙出现了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7266(): pass

    label('loc_7266')

    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x726A
@scena.Code('func_0D_726A')
def func_0D_726A():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C9, 4, 0x1E4C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_73BF',
    )

    OP_22(0x0192, 0x00, 0x64)

    ChrTalk(
        0x00FE,
        (
            '喵～～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#1004F啊，安东尼！？',
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
        'loc_7314',
    )

    ChrTalk(
        0x0107,
        (
            '#067F嘿嘿嘿……\n',
            '很吃惊吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不管怎么看\n',
            '都像是雷伊哥哥带来的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_733D')

    def _loc_7314(): pass

    label('loc_7314')

    ChrTalk(
        0x0102,
        (
            '#1044F是中央工房的人\n',
            '带来的吗……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_733D(): pass

    label('loc_733D')

    OP_22(0x0192, 0x00, 0x64)

    ChrTalk(
        0x00FE,
        (
            '喵？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F唔～为什么会在\n',
            '这种紧张的形势下再次见面呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '呼，不管怎么说，\n',
            '这阵子还请多关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x0192, 0x00, 0x64)

    ChrTalk(
        0x00FE,
        (
            '喵～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1E4C)

    Jump('loc_73CE')

    def _loc_73BF(): pass

    label('loc_73BF')

    OP_22(0x0192, 0x00, 0x64)

    ChrTalk(
        0x00FE,
        (
            '喵？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_73CE(): pass

    label('loc_73CE')

    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x73D2
@scena.Code('func_0E_73D2')
def func_0E_73D2():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 6, 0x1A1E)),
            Expr.Return,
        ),
        'loc_74F8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_749C',
    )

    ChrTalk(
        0x00FE,
        (
            '哦……\n',
            '你就是大家所说的游击士吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没想到那个摩尔根将军\n',
            '竟然会提议让游击士同行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，王国军的风气\n',
            '也有了很大变化呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这就是准将的组织改革\n',
            '正在逐步推行的证据。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    Jump('loc_74F8')

    def _loc_749C(): pass

    label('loc_749C')

    ChrTalk(
        0x00FE,
        (
            '没想到那个摩尔根将军\n',
            '竟然会提议让游击士同行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，王国军的风气\n',
            '也有了很大变化呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_74F8(): pass

    label('loc_74F8')

    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x74FC
@scena.Code('func_0F_74FC')
def func_0F_74FC():
    TalkBegin(0x00FE)
    SetChrChipByIndex(0x00FE, 9)
    SetChrSubChip(0x00FE, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Return,
        ),
        'loc_75A6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7576',
    )

    ChrTalk(
        0x00FE,
        (
            '呼嗯～嗯……\n',
            '嗬，已经到换岗的时间了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然完全没睡，\n',
            '不过还是得赶快上岗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000A)

    Jump('loc_75A3')

    def _loc_7576(): pass

    label('loc_7576')

    ChrTalk(
        0x00FE,
        (
            '呼嗯～嗯……\n',
            '嗬，已经到换岗的时间了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_75A3(): pass

    label('loc_75A3')

    Jump('loc_7EDE')

    def _loc_75A6(): pass

    label('loc_75A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 6, 0x1E1E)),
            Expr.Return,
        ),
        'loc_7765',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_769F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7646',
    )

    ChrTalk(
        0x00FE,
        (
            '哦，公主殿下……\n',
            '每次都让您受累了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '陛下托付的使命\n',
            '看来也快要完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那，最后一座塔\n',
            '也请您鼓足干劲完成任务吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000A)

    Jump('loc_769C')

    def _loc_7646(): pass

    label('loc_7646')

    ChrTalk(
        0x00FE,
        (
            '陛下托付的使命\n',
            '看来也快要完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那，最后一座塔\n',
            '也请您鼓足干劲完成任务吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_769C(): pass

    label('loc_769C')

    Jump('loc_7762')

    def _loc_769F(): pass

    label('loc_769F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_772C',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀呀，\n',
            '看来整件事情就快要结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好了，一鼓作气\n',
            '把它解决掉吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '结局圆满即是一切圆满，\n',
            '过去的人经常这么说的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000B)

    Jump('loc_7762')

    def _loc_772C(): pass

    label('loc_772C')

    ChrTalk(
        0x00FE,
        (
            '一鼓作气\n',
            '把它解决掉吧。\n',
            '结局圆满即是一切圆满啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7762(): pass

    label('loc_7762')

    Jump('loc_7EDE')

    def _loc_7765(): pass

    label('loc_7765')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 1, 0x1E11)),
            Expr.Return,
        ),
        'loc_797F',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7880',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7819',
    )

    ChrTalk(
        0x00FE,
        (
            '继蔡斯之后，卢安也\n',
            '出现了结社的爪牙吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总觉得整个王国里\n',
            '好像都潜藏着敌人的爪牙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '公主殿下也要多加小心哦。\n',
            '不知道敌人会躲在哪里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000A)

    Jump('loc_787D')

    def _loc_7819(): pass

    label('loc_7819')

    ChrTalk(
        0x00FE,
        (
            '总觉得整个王国里\n',
            '好像都潜藏着敌人的爪牙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '公主殿下也要多加小心哦。\n',
            '不知道敌人会躲在哪里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_787D(): pass

    label('loc_787D')

    Jump('loc_797C')

    def _loc_7880(): pass

    label('loc_7880')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7922',
    )

    ChrTalk(
        0x00FE,
        (
            '总觉得整个王国里\n',
            '都潜藏着结社的爪牙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这种气氛与情报部\n',
            '发动政变时很相似。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，为什么这些\n',
            '图谋不轨的家伙们总是\n',
            '不断地涌现出来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000B)

    Jump('loc_797C')

    def _loc_7922(): pass

    label('loc_7922')

    ChrTalk(
        0x00FE,
        (
            '总觉得整个王国里\n',
            '都潜藏着结社的爪牙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这种气氛与情报部\n',
            '发动政变时越来越相似了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_797C(): pass

    label('loc_797C')

    Jump('loc_7EDE')

    def _loc_797F(): pass

    label('loc_797F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 2, 0x1E0A)),
            Expr.Return,
        ),
        'loc_7C6D',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7AE2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 2, 0x12)),
            Expr.Return,
        ),
        'loc_79F6',
    )

    ChrTalk(
        0x00FE,
        (
            '把古代的结晶回路\n',
            '装配在导力器中……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '实在令人难以想象啊。\n',
            '真是个不得了的老头子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7ADF')

    def _loc_79F6(): pass

    label('loc_79F6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7A87',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，公主殿下……\n',
            '来工作室有什么事情吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '拉赛尔博士正在里面\n',
            '分析那个黑色机器。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里乱七八糟的\n',
            '请留意不要被绊倒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000A)

    Jump('loc_7ADF')

    def _loc_7A87(): pass

    label('loc_7A87')

    ChrTalk(
        0x00FE,
        (
            '拉赛尔博士正在工作室里\n',
            '分析那个黑色机器。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '里面乱七八糟的\n',
            '请留意不要被绊倒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7ADF(): pass

    label('loc_7ADF')

    Jump('loc_7C6A')

    def _loc_7AE2(): pass

    label('loc_7AE2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 2, 0x12)),
            Expr.Return,
        ),
        'loc_7B46',
    )

    ChrTalk(
        0x00FE,
        (
            '把古代的结晶回路\n',
            '装配在导力器中……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '实在令人难以想象啊。\n',
            '真是个不得了的老头子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7C6A')

    def _loc_7B46(): pass

    label('loc_7B46')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7C12',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才博士好像拿着一个\n',
            '奇怪的黑东西进去了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难道说那个就是\n',
            '你们在塔里发现的东西吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '结社想用那种东西\n',
            '来做什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望博士的研究能进展顺利，\n',
            '早日弄清敌人的目的就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000B)

    Jump('loc_7C6A')

    def _loc_7C12(): pass

    label('loc_7C12')

    ChrTalk(
        0x00FE,
        (
            '结社想用那黑色机器\n',
            '来做什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '完全不明白敌人的目的，\n',
            '心情实在是非常糟糕啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7C6A(): pass

    label('loc_7C6A')

    Jump('loc_7EDE')

    def _loc_7C6D(): pass

    label('loc_7C6D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            Expr.Return,
        ),
        'loc_7EDE',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7E02',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7DA5',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀呀……\n',
            '没想到公主殿下亲临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '莫非您打算和游击士\n',
            '一起进入塔内吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F是啊，我是这个打算。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '现在不是一个人\n',
            '置身事外的时候了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼～，不愧是公主殿下。\n',
            '实在是很了不起的决心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '既然如此，请您先在\n',
            '工作室调整好装备吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '佩顿那家伙\n',
            '似乎在准备什么的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000A)

    Jump('loc_7DFF')

    def _loc_7DA5(): pass

    label('loc_7DA5')

    ChrTalk(
        0x00FE,
        (
            '若要前往塔内，请先在\n',
            '工作室调整好装备吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '战斗并不是光靠意志\n',
            '和气势就能取胜的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7DFF(): pass

    label('loc_7DFF')

    Jump('loc_7EDE')

    def _loc_7E02(): pass

    label('loc_7E02')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7E80',
    )

    ChrTalk(
        0x00FE,
        (
            '哦，辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从这里进去是工作室，\n',
            '往另一边走的话就是货舱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果要用升降机，\n',
            '就去货舱那边看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000B)

    Jump('loc_7EDE')

    def _loc_7E80(): pass

    label('loc_7E80')

    ChrTalk(
        0x00FE,
        (
            '这个房间就是工作室，\n',
            '往另一边走的话就是货舱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果要用升降机，\n',
            '就去货舱那边看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7EDE(): pass

    label('loc_7EDE')

    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x7EE2
@scena.Code('func_10_7EE2')
def func_10_7EE2():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 6, 0x1E1E)),
            Expr.Return,
        ),
        'loc_80AC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8025',
    )

    ChrTalk(
        0x00FE,
        (
            '理论的补充修正总算完成了，\n',
            '这下『装置』的制造也有了头绪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，虽然说理论已经完成了，\n',
            '但还只是数学公式的程度而已……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可笑的是，我们目前\n',
            '也不明白这公式的意义。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们证明了其正确性，\n',
            '却不知道我们证明的是什么东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这虽然是一件相当讽刺的事情，\n',
            '但在导力理论界里却是常有的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0007)

    Jump('loc_80A9')

    def _loc_8025(): pass

    label('loc_8025')

    ChrTalk(
        0x00FE,
        (
            '理论的补充修正总算完成了，\n',
            '这下『装置』的制造也有了头绪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是啊，这是一个艰难的研究项目\n',
            '不过也因此度过了一段充实的时光呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_80A9(): pass

    label('loc_80A9')

    Jump('loc_8224')

    def _loc_80AC(): pass

    label('loc_80AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            Expr.Return,
        ),
        'loc_8224',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_81BC',
    )

    ChrTalk(
        0x00FE,
        (
            '实验室终于开始\n',
            '培育新的农作物了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可我听说这里在进行一项有趣的研究，\n',
            '于是就急急忙忙地跑到这船上来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，从博士的话来看\n',
            '我的决定似乎是正确的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真想不到居然要\n',
            '从正面挑战那个问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，看来这将会是\n',
            '一项很刺激的计划哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0007)

    Jump('loc_8224')

    def _loc_81BC(): pass

    label('loc_81BC')

    ChrTalk(
        0x00FE,
        (
            '真想不到居然要\n',
            '从正面挑战那个问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀，不愧是拉赛尔博士。\n',
            '与那边的研究人员有着不同的志向。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8224(): pass

    label('loc_8224')

    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0x8228
@scena.Code('func_11_8228')
def func_11_8228():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 6, 0x1E1E)),
            Expr.Return,
        ),
        'loc_82A2',
    )

    ChrTalk(
        0x00FE,
        (
            '研究也总算是\n',
            '渐入佳境了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不知道什么原因，\n',
            '好像需要大量试制品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以现在准备要\n',
            '紧急进行组装。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_850B')

    def _loc_82A2(): pass

    label('loc_82A2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 2, 0x1E0A)),
            Expr.Return,
        ),
        'loc_83C3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8354',
    )

    ChrTalk(
        0x00FE,
        (
            '理论方面就交给博士和雷伊，\n',
            '我就专心负责回路的试作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要让这项工作成功\n',
            '不仅需要理论，也需要技术。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以拥有维修员经验的我\n',
            '才会被特地请来这里哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)

    Jump('loc_83C0')

    def _loc_8354(): pass

    label('loc_8354')

    ChrTalk(
        0x00FE,
        (
            '理论方面就交给博士和雷伊，\n',
            '我就专心负责回路的试作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这项工作不仅需要理论\n',
            '也很需要技术人员的能力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_83C0(): pass

    label('loc_83C0')

    Jump('loc_850B')

    def _loc_83C3(): pass

    label('loc_83C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            Expr.Return,
        ),
        'loc_850B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8481',
    )

    ChrTalk(
        0x00FE,
        (
            '以博士的研究小组成员名义\n',
            '接受征召，实在是无上的光荣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我会竭尽自己所能，\n',
            '决不拖累研究的进度，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为我还想将这一次的所见所闻\n',
            '说给在卢安等我的弟弟豆豆听呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)

    Jump('loc_850B')

    def _loc_8481(): pass

    label('loc_8481')

    ChrTalk(
        0x00FE,
        (
            '我会好好地努力，然后把这一次的\n',
            '所见所闻说给在卢安等我的弟弟豆豆听哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是跟豆豆说我乘坐了『埃尔赛尤』，\n',
            '想必那家伙会很羡慕吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_850B(): pass

    label('loc_850B')

    TalkEnd(0x00FE)

    Return()

# id: 0x0012 offset: 0x850F
@scena.Code('func_12_850F')
def func_12_850F():
    TalkBegin(0x0015)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 2, 0x12)),
            Expr.Return,
        ),
        'loc_8592',
    )

    ChrTalk(
        0x0015,
        (
            '第三级改造的事情……\n',
            '你们应该听博士说过了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '我准备好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '由于ＥＰ值也会提升，\n',
            '请各位积极地去尝试吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A3(0x0012)

    def _loc_8592(): pass

    label('loc_8592')

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
            TXT(0x01, '改造·换钱\n'),
            TXT(0x02, '买东西\n'),
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
        'loc_8601',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_85FB',
    )

    OP_A9(0x2E)

    Jump('loc_85FD')

    def _loc_85FB(): pass

    label('loc_85FB')

    OP_A9(0x28)

    def _loc_85FD(): pass

    label('loc_85FD')

    TalkEnd(0x0015)

    Return()

    def _loc_8601(): pass

    label('loc_8601')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8620',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_861A',
    )

    OP_A9(0x2D)

    Jump('loc_861C')

    def _loc_861A(): pass

    label('loc_861A')

    OP_A9(0x29)

    def _loc_861C(): pass

    label('loc_861C')

    TalkEnd(0x0015)

    Return()

    def _loc_8620(): pass

    label('loc_8620')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_863A',
    )

    FadeIn(300, 0)
    TalkEnd(0x0015)

    Return()

    def _loc_863A(): pass

    label('loc_863A')

    FadeIn(300, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Return,
        ),
        'loc_8737',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_86C8',
    )

    ChrTalk(
        0x0015,
        (
            '大家辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '在进行对中枢塔的搜索之前\n',
            '请先检查各自的装备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '否则战斗开始之后\n',
            '再后悔就为时已晚了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    Jump('loc_8734')

    def _loc_86C8(): pass

    label('loc_86C8')

    ChrTalk(
        0x0015,
        (
            '在进行对中枢塔的搜索之前\n',
            '请先检查各自的装备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '依照人形兵器的种类改变\n',
            '装饰品的搭配也是很有效的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8734(): pass

    label('loc_8734')

    Jump('loc_8F3A')

    def _loc_8737(): pass

    label('loc_8737')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Return,
        ),
        'loc_8841',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_87F0',
    )

    ChrTalk(
        0x0015,
        (
            '哎呀～，舰内突然就\n',
            '明亮起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '灰暗的心情也随之一扫而空，\n',
            '灯光果然很重要呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '那么，我也来调整心态，\n',
            '好好地努力工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '如果有事\n',
            '尽管来叫我啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    Jump('loc_883E')

    def _loc_87F0(): pass

    label('loc_87F0')

    ChrTalk(
        0x0015,
        (
            '哎呀～，舰内突然就\n',
            '明亮起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '我也来调整心态，\n',
            '好好地努力工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_883E(): pass

    label('loc_883E')

    Jump('loc_8F3A')

    def _loc_8841(): pass

    label('loc_8841')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 1, 0x2219)),
            Expr.Return,
        ),
        'loc_8ABA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0458, 5, 0x22C5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_89DE',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8925',
    )

    ChrTurnDirection(0x0015, 0x010B, 0)

    ChrTalk(
        0x0015,
        (
            '啊，你是乔丝特小姐……吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '我们也准备了\n',
            '适合你使用的防具哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '出发之前\n',
            '请记得先调整好装备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#211F嘿嘿，准备得挺周到的嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '嗯，如果有了这个心思\n',
            '我会请你们带我去看的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x22C5)

    Jump('loc_89D8')

    def _loc_8925(): pass

    label('loc_8925')

    ChrTalk(
        0x0015,
        (
            '听说空贼小姐\n',
            '正在寻找她的兄弟们呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '带她去进行探索的时候，\n',
            '请千万要检查好装备哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '特别是护具要仔细检查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '因为用枪的人，有时候身上\n',
            '并没有穿戴着合适的防具……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_89D8(): pass

    label('loc_89D8')

    OP_A2(0x0009)

    Jump('loc_8AB7')

    def _loc_89DE(): pass

    label('loc_89DE')

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8A46',
    )

    ChrTurnDirection(0x0015, 0x010B, 0)

    ChrTalk(
        0x0015,
        (
            '我想我所挑选的防具\n',
            '一定会适合她的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '若是方便的话，\n',
            '请一定要过来看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8AB7')

    def _loc_8A46(): pass

    label('loc_8A46')

    ChrTalk(
        0x0015,
        (
            '带空贼小姐\n',
            '去进行探索的时候，\n',
            '请千万要检查好装备哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '因为用枪的人，有时候身上\n',
            '并没有穿戴着合适的防具。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8AB7(): pass

    label('loc_8AB7')

    Jump('loc_8F3A')

    def _loc_8ABA(): pass

    label('loc_8ABA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_8B9F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8B56',
    )

    ChrTalk(
        0x0015,
        (
            '哎呀～导力器可以运作，\n',
            '真是一件很棒的事呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '这样一来，我也可以进行\n',
            '久违的结晶回路合成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '好了，如果需要什么\n',
            '请尽管说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    Jump('loc_8B9C')

    def _loc_8B56(): pass

    label('loc_8B56')

    ChrTalk(
        0x0015,
        (
            '总觉得好久没有\n',
            '合成结晶回路了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '如果需要什么\n',
            '请尽管说啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8B9C(): pass

    label('loc_8B9C')

    Jump('loc_8F3A')

    def _loc_8B9F(): pass

    label('loc_8B9F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 6, 0x1E1E)),
            Expr.Return,
        ),
        'loc_8CA8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8C37',
    )

    ChrTalk(
        0x0015,
        (
            '还剩一座塔……\n',
            '这么一来调查也接近尾声了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '接下来的战斗\n',
            '想必会十分严酷吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '请不要忘记进行\n',
            '导力器的调整和装备的检查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    Jump('loc_8CA5')

    def _loc_8C37(): pass

    label('loc_8C37')

    ChrTalk(
        0x0015,
        (
            '塔的调查也终于接近尾声了……\n',
            '战斗想必也会比以前更加严酷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '请不要忘记进行\n',
            '导力器的调整和装备的检查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8CA5(): pass

    label('loc_8CA5')

    Jump('loc_8F3A')

    def _loc_8CA8(): pass

    label('loc_8CA8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 1, 0x1E11)),
            Expr.Return,
        ),
        'loc_8DC0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8D75',
    )

    ChrTalk(
        0x0015,
        (
            '辛苦大家了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '博士的研究\n',
            '似乎碰上了一些问题呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '刚才研究人员们\n',
            '出去休息了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '唉，过于刨根究底\n',
            '反而会使事情的进展停滞不前……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '诸位，也偶尔到休息室去\n',
            '歇口气如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    Jump('loc_8DBD')

    def _loc_8D75(): pass

    label('loc_8D75')

    ChrTalk(
        0x0015,
        (
            '博士的研究\n',
            '似乎碰上了一些问题呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '刚才研究人员们\n',
            '出去休息了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8DBD(): pass

    label('loc_8DBD')

    Jump('loc_8F3A')

    def _loc_8DC0(): pass

    label('loc_8DC0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 2, 0x1E0A)),
            Expr.Return,
        ),
        'loc_8ECB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8E58',
    )

    ChrTalk(
        0x0015,
        (
            '博士他们似乎\n',
            '正在忙于研究呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '虽然我也看过了\n',
            '『装置』的设计图……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '但很遗憾，我完全无法理解。\n',
            '最尖端的研究好厉害啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    Jump('loc_8EC8')

    def _loc_8E58(): pass

    label('loc_8E58')

    ChrTalk(
        0x0015,
        (
            '博士他们正在研究的『装置』，\n',
            '好像是件很了不得的东西呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '很遗憾，虽说看了结构图\n',
            '我仍然搞不懂它的机能。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8EC8(): pass

    label('loc_8EC8')

    Jump('loc_8F3A')

    def _loc_8ECB(): pass

    label('loc_8ECB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            Expr.Return,
        ),
        'loc_8F3A',
    )

    ChrTalk(
        0x0015,
        (
            '需要调整导力器或结晶回路时\n',
            '请跟我说一声吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '这里武器和防具也很齐全，\n',
            '应该可以进行一般的准备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8F3A(): pass

    label('loc_8F3A')

    TalkEnd(0x0015)

    Return()

# id: 0x0013 offset: 0x8F3E
@scena.Code('func_13_8F3E')
def func_13_8F3E():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Return,
        ),
        'loc_8FD6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8FA3',
    )

    ChrTalk(
        0x00FE,
        (
            '导力引擎……驱动率固定在５０％。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '导力压正常……\n',
            '随时可以开始测试。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000E)

    Jump('loc_8FD6')

    def _loc_8FA3(): pass

    label('loc_8FA3')

    ChrTalk(
        0x00FE,
        (
            '驱动率固定在５０％……\n',
            '导力压正常，没有问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8FD6(): pass

    label('loc_8FD6')

    TalkEnd(0x00FE)

    Return()

# id: 0x0014 offset: 0x8FDA
@scena.Code('func_14_8FDA')
def func_14_8FDA():
    TalkBegin(0x00FE)
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
            TXT(0x01, '队伍编成\n'),
            TXT(0x02, '放弃\n'),
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
        (0x00000000, 'loc_903B'),
        (0x00000001, 'loc_9229'),
        (0x00000002, 'loc_925D'),
        (-1, 'loc_9260'),
    )

    def _loc_903B(): pass

    label('loc_903B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0458, 3, 0x22C3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_91C1',
    )

    ChrTalk(
        0x0009,
        (
            '#0030390791V#023F哎呀，你们几个。\n',
            '还没出发？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010390792V#1015F嗯，还在做各种准备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020390793V#1040F雪拉姐\n',
            '在整理房间吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x0009,
        (
            '#0030390794V#020F嗯嗯，算是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030390795V修理我也帮不上忙，\n',
            '整个人闲得发慌呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030390796V#525F干脆拿着鞭子\n',
            '去监督那群男人好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010390797V#1001F啊哈哈，那样倒也不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020390798V#1048F还、还请手下留情啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x22C3)

    Jump('loc_9226')

    def _loc_91C1(): pass

    label('loc_91C1')

    ChrTalk(
        0x0009,
        (
            '#0030390799V#020F那么……\n',
            '现在该做些什么呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030390800V要是能找到\n',
            '什么能帮上忙的事就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9226(): pass

    label('loc_9226')

    Jump('loc_9263')

    def _loc_9229(): pass

    label('loc_9229')

    ChrTalk(
        0x0009,
        (
            '#0030340489V#020F哎呀？要更换成员了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x0015)

    Jump('loc_9263')

    def _loc_925D(): pass

    label('loc_925D')

    Jump('loc_9263')

    def _loc_9260(): pass

    label('loc_9260')

    Jump('loc_9263')

    def _loc_9263(): pass

    label('loc_9263')

    TalkEnd(0x00FE)

    Return()

# id: 0x0015 offset: 0x9267
@scena.Code('func_15_9267')
def func_15_9267():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_92DE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x045A, 6, 0x22D6)),
            Expr.Return,
        ),
        'loc_9299',
    )

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
            0x0004,
            0x0003,
            0x0006,
            0x0007,
            0x0008,
            0x000A,
            0x000E,
            0x000F,
            0xFFFF,
        ),
    )

    Jump('loc_92DB')

    def _loc_9299(): pass

    label('loc_9299')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 1, 0x2219)),
            Expr.Return,
        ),
        'loc_92C0',
    )

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
            0x0004,
            0x0003,
            0x0006,
            0x0007,
            0x0008,
            0x000A,
            0xFFFF,
        ),
    )

    Jump('loc_92DB')

    def _loc_92C0(): pass

    label('loc_92C0')

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
            0x0004,
            0x0003,
            0x0006,
            0x0007,
            0x0008,
            0xFFFF,
        ),
    )

    def _loc_92DB(): pass

    label('loc_92DB')

    Jump('loc_935C')

    def _loc_92DE(): pass

    label('loc_92DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 6, 0x1E1E)),
            Expr.Return,
        ),
        'loc_9301',
    )

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
            0x0004,
            0x0007,
            0x0008,
            0xFFFF,
        ),
    )

    Jump('loc_935C')

    def _loc_9301(): pass

    label('loc_9301')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 1, 0x1E11)),
            Expr.Return,
        ),
        'loc_9322',
    )

    OP_C9(
        0x01,
        (
            0x0000,
            0x0001,
            0x0002,
            0x00FF,
        ),
        (
            0x0005,
            0x0006,
            0x0004,
            0x0008,
            0x0007,
            0xFFFF,
        ),
    )

    Jump('loc_935C')

    def _loc_9322(): pass

    label('loc_9322')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 2, 0x1E0A)),
            Expr.Return,
        ),
        'loc_9343',
    )

    OP_C9(
        0x01,
        (
            0x0000,
            0x0001,
            0x0007,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
            0x0006,
            0x0004,
            0x0008,
            0xFFFF,
        ),
    )

    Jump('loc_935C')

    def _loc_9343(): pass

    label('loc_9343')

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
            0x0004,
            0x0007,
            0x0008,
            0xFFFF,
        ),
    )

    def _loc_935C(): pass

    label('loc_935C')

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
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000E, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0440, 1, 0x2201)),
            Expr.Return,
        ),
        'loc_94B6',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_93B2',
    )

    SetChrPos(0x000B, -2830, 0, 65940, 90)
    ClearChrFlags(0x000B, 0x0080)

    def _loc_93B2(): pass

    label('loc_93B2')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_93D5',
    )

    SetChrPos(0x000D, 62920, 0, 8020, 0)
    ClearChrFlags(0x000D, 0x0080)

    def _loc_93D5(): pass

    label('loc_93D5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0443, 1, 0x2219)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9403',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_9400',
    )

    SetChrPos(0x0009, -5340, 0, 59510, 270)
    ClearChrFlags(0x0009, 0x0080)

    def _loc_9400(): pass

    label('loc_9400')

    Jump('loc_94B3')

    def _loc_9403(): pass

    label('loc_9403')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0445, 4, 0x222C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_940E',
    )

    Jump('loc_94B3')

    def _loc_940E(): pass

    label('loc_940E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_945F',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_9439',
    )

    SetChrPos(0x000E, -5340, 0, 60030, 270)
    ClearChrFlags(0x000E, 0x0080)

    def _loc_9439(): pass

    label('loc_9439')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_945C',
    )

    SetChrPos(0x000B, -3510, 0, 5330, 0)
    ClearChrFlags(0x000B, 0x0080)

    def _loc_945C(): pass

    label('loc_945C')

    Jump('loc_94B3')

    def _loc_945F(): pass

    label('loc_945F')

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_9482',
    )

    SetChrPos(0x000E, -5340, 0, 60030, 270)
    ClearChrFlags(0x000E, 0x0080)

    def _loc_9482(): pass

    label('loc_9482')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_94B3',
    )

    TerminateThread(0x000A, 0x00)
    ClearChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000A, 0x0004)
    SetChrChipByIndex(0x000A, 15)
    SetChrPos(0x000A, 61300, 250, -40950, 0)

    def _loc_94B3(): pass

    label('loc_94B3')

    Jump('loc_95D0')

    def _loc_94B6(): pass

    label('loc_94B6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 6, 0x1E1E)),
            Expr.Return,
        ),
        'loc_9506',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_94E0',
    )

    SetChrPos(0x000B, -860, 0, 64200, 45)
    ClearChrFlags(0x000B, 0x0080)

    def _loc_94E0(): pass

    label('loc_94E0')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_9503',
    )

    SetChrPos(0x000D, 62920, 0, 8020, 0)
    ClearChrFlags(0x000D, 0x0080)

    def _loc_9503(): pass

    label('loc_9503')

    Jump('loc_95D0')

    def _loc_9506(): pass

    label('loc_9506')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 1, 0x1E11)),
            Expr.Return,
        ),
        'loc_9556',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_9530',
    )

    SetChrPos(0x000B, -860, 0, 64200, 45)
    ClearChrFlags(0x000B, 0x0080)

    def _loc_9530(): pass

    label('loc_9530')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_9553',
    )

    SetChrPos(0x000D, 62920, 0, 8020, 0)
    ClearChrFlags(0x000D, 0x0080)

    def _loc_9553(): pass

    label('loc_9553')

    Jump('loc_95D0')

    def _loc_9556(): pass

    label('loc_9556')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C1, 2, 0x1E0A)),
            Expr.Return,
        ),
        'loc_9583',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_9580',
    )

    SetChrPos(0x000D, 62920, 0, 8020, 0)
    ClearChrFlags(0x000D, 0x0080)

    def _loc_9580(): pass

    label('loc_9580')

    Jump('loc_95D0')

    def _loc_9583(): pass

    label('loc_9583')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            Expr.Return,
        ),
        'loc_95D0',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_95AD',
    )

    SetChrPos(0x000B, -4420, 0, 62290, 225)
    ClearChrFlags(0x000B, 0x0080)

    def _loc_95AD(): pass

    label('loc_95AD')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_95D0',
    )

    SetChrPos(0x000D, 62920, 0, 8020, 0)
    ClearChrFlags(0x000D, 0x0080)

    def _loc_95D0(): pass

    label('loc_95D0')

    OP_0D()

    Return()

# id: 0x0016 offset: 0x95D2
@scena.Code('func_16_95D2')
def func_16_95D2():
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
        'loc_95F7',
    )

    Call(0, 0x0018)
    Call(0, 0x0019)
    FadeIn(0, 0)
    Sleep(100)

    def _loc_95F7(): pass

    label('loc_95F7')

    Fade(1000)
    OP_6D(-5110, 0, 64310, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -4820, 0, 63930, 0)
    SetChrPos(0x0102, -5720, 0, 63930, 0)
    SetChrPos(0x00F8, -4070, 0, 64340, 315)
    SetChrPos(0x00F9, -6300, 0, 64440, 45)
    OP_4A(0x0008, 255)

    @scena.Lambda('lambda_9687')
    def lambda_9687():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_9687')

    DispatchAsync2(0x0101, 0x0001, lambda_9687)

    @scena.Lambda('lambda_9698')
    def lambda_9698():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_9698')

    DispatchAsync2(0x0102, 0x0001, lambda_9698)

    @scena.Lambda('lambda_96A9')
    def lambda_96A9():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_96A9')

    DispatchAsync2(0x00F8, 0x0001, lambda_96A9)

    @scena.Lambda('lambda_96BA')
    def lambda_96BA():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_96BA')

    DispatchAsync2(0x00F9, 0x0001, lambda_96BA)

    OP_0D()
    ChrTurnDirection(0x0008, 0x0101, 400)
    Sleep(700)

    ChrTalk(
        0x0008,
        (
            '#0540340984V#101F哦哦，来得正是时候。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540340985V我刚刚把数据水晶\n',
            '装在了『卡佩尔』上面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540340986V之后只要放着它不管\n',
            '应该就会得到自动分析的结果。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340987V#1011F#4P这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340988V#1040F自动分析\n',
            '需要多长时间呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540340989V#100F与受损程度有关\n',
            '不能一概而论。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540340990V有时需要花费好几天\n',
            '所以你们就耐心地等待吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340991V#1040F原来如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340992V#1015F#4P嗯，既然这样，\n',
            '光是着急也没有用呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540340993V#100F那么，如果获得新的水晶，\n',
            '请拿来我这里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540340994V我会立刻装在『卡佩尔』上，\n',
            '让它开始进行自动分析。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8E(0x0008, -950, 0, 65390, 2000, 0x00)
    OP_8C(0x0008, 0, 400)
    OP_4B(0x0008, 255)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x00F8, 0x01)
    TerminateThread(0x00F9, 0x01)
    ClearChrFlags(0x0008, 0x0010)
    OP_65(0x00, 0x0001)
    OP_A2(0x1E0B)
    EventEnd(0x00)

    Return()

# id: 0x0017 offset: 0x994F
@scena.Code('func_17_994F')
def func_17_994F():
    ChrTalk(
        0x0008,
        (
            '#0540340995V#101F哦，你们好像又获得\n',
            '新的数据水晶了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540340996V我马上把它装在『卡佩尔』上，\n',
            '让它来进行自动分析。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340997V#1006F嗯，拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '交出了新获得的数据水晶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    RemoveItem(ItemTable['数据水晶１'], 1)
    RemoveItem(ItemTable['数据水晶２'], 1)
    RemoveItem(ItemTable['数据水晶３'], 1)
    RemoveItem(ItemTable['数据水晶４'], 1)
    RemoveItem(ItemTable['数据水晶５'], 1)
    RemoveItem(ItemTable['数据水晶６'], 1)
    RemoveItem(ItemTable['数据水晶７'], 1)
    RemoveItem(ItemTable['数据水晶８'], 1)
    RemoveItem(ItemTable['数据水晶９'], 1)
    RemoveItem(ItemTable['数据水晶１０'], 1)
    RemoveItem(ItemTable['数据水晶１１'], 1)
    RemoveItem(ItemTable['数据水晶１２'], 1)
    RemoveItem(ItemTable['数据水晶１３'], 1)
    RemoveItem(ItemTable['数据水晶１４'], 1)
    RemoveItem(ItemTable['数据水晶１５'], 1)

    Return()

# id: 0x0018 offset: 0x9A76
@scena.Code('func_18_9A76')
def func_18_9A76():
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
        (0x00000000, 'loc_9AF0'),
        (0x00000001, 'loc_9AF6'),
        (-1, 'loc_9AFC'),
    )

    def _loc_9AF0(): pass

    label('loc_9AF0')

    OP_A2(0x1200)

    Jump('loc_9AFC')

    def _loc_9AF6(): pass

    label('loc_9AF6')

    OP_A2(0x1201)

    Jump('loc_9AFC')

    def _loc_9AFC(): pass

    label('loc_9AFC')

    Return()

# id: 0x0019 offset: 0x9AFD
@scena.Code('func_19_9AFD')
def func_19_9AFD():
    FadeOut(0, 0, -1)
    OP_6D(-18870, 0, -1650, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            0x0000,
            0x0001,
            0x0007,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
            0x0006,
            0x0004,
            0x0008,
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

    Sleep(100)

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0x00000000)

    Return()

# id: 0x001A offset: 0x9B8A
@scena.Code('func_1A_9B8A')
def func_1A_9B8A():
    FadeOut(0, 0, -1)
    EventBegin(0x00)
    OP_6D(3300, 2800, 6000, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_9BE8',
    )

    Call(0, 0x0018)
    Call(0, 0x0019)

    def _loc_9BE8(): pass

    label('loc_9BE8')

    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x0102, 0x0080)
    SetChrFlags(0x00F8, 0x0080)
    SetChrFlags(0x00F9, 0x0080)
    SetChrPos(0x0008, -1060, 150, 7570, 0)
    OP_4A(0x0008, 255)

    @scena.Lambda('lambda_9C17')
    def lambda_9C17():
        OP_6D(1600, 0, 1900, 4500)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_9C17)

    FadeIn(1000, 0)
    CreateThread(0x0101, 0x01, 0x00, 0x001C)
    Sleep(100)

    CreateThread(0x0102, 0x01, 0x00, 0x001D)
    Sleep(100)

    CreateThread(0x00F8, 0x01, 0x00, 0x001E)
    Sleep(100)

    CreateThread(0x00F9, 0x01, 0x00, 0x001F)
    OP_0D()
    CreateThread(0x0008, 0x01, 0x00, 0x001B)
    WaitForThreadExit(0x0008, 0x0001)
    SetChrChipByIndex(0x0012, 15)
    SetChrSubChip(0x0012, 0)
    OP_4A(0x0012, 0)
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)

    @scena.Lambda('lambda_9C90')
    def lambda_9C90():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_9C90')

    DispatchAsync2(0x0008, 0x0001, lambda_9C90)

    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0540340998V#103F哦哦，你们几个。\n',
            '来得正好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)

    @scena.Lambda('lambda_9CEA')
    def lambda_9CEA():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_9CEA)

    Sleep(120)

    @scena.Lambda('lambda_9CFD')
    def lambda_9CFD():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_9CFD)

    @scena.Lambda('lambda_9D0B')
    def lambda_9D0B():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_9D0B)

    Sleep(120)

    @scena.Lambda('lambda_9D1E')
    def lambda_9D1E():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_9D1E)

    ChrTalk(
        0x0101,
        (
            '#0010340999V#1011F啊，拉赛尔博士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341000V#1044F#2P找我们有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0101, 0x01, 0x00, 0x0020)

    @scena.Lambda('lambda_9D88')
    def lambda_9D88():
        OP_6D(-260, 0, 4050, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_9D88)

    @scena.Lambda('lambda_9DA0')
    def lambda_9DA0():
        OP_67(0, 7140, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_9DA0)

    @scena.Lambda('lambda_9DB8')
    def lambda_9DB8():
        OP_6B(2680, 4000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_9DB8)

    Sleep(400)

    CreateThread(0x0102, 0x01, 0x00, 0x0021)
    Sleep(400)

    CreateThread(0x00F8, 0x01, 0x00, 0x0022)
    Sleep(600)

    CreateThread(0x00F9, 0x01, 0x00, 0x0023)
    WaitForThreadExit(0x00F9, 0x0001)
    WaitForThreadExit(0x0102, 0x0002)

    ChrTalk(
        0x0008,
        (
            '#0540341001V#100F嗯，其实呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540341002V在分析数据水晶的时候\n',
            '发现了一些有趣的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341003V#1015F有趣的事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540341004V#104F嗯，我们之前就已经知道\n',
            '古代也有类似结晶回路的东西……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540341005V#100F而现在终于发现了\n',
            '将古代的结晶回路装配在\n',
            '现代的导力器之中的方法。',
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
        'loc_9F63',
    )

    OP_62(0x0107, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0107,
        (
            '#0070341006V#064F真、真的吗，爷爷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9FA5')

    def _loc_9F63(): pass

    label('loc_9F63')

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010341007V#1004F是、是真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9FA5(): pass

    label('loc_9FA5')

    ChrTalk(
        0x0008,
        (
            '#0540341008V#101F呵呵，你们以为我是谁？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540341009V#100F……只不过，以你们现在的\n',
            '结晶孔是无法做到这一点的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540341010V所以针对结晶孔的强化……\n',
            '第三级的结晶孔改造就势在必行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341011V#1044F#2P也就是说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020341012V可以超越目前的极限，\n',
            '对结晶孔进行\n',
            '更进一步的强化是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540341013V#100F嗯，是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540341014V改造的准备已经做好了，\n',
            '有机会去问问工房那边吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540341015V等找到了类似那样的结晶回路之后\n',
            '一定要试试第三级的改造。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341016V#1006F嗯，明白了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341017V#1040F#2P到时就让我们多加利用吧。',
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
        'loc_A22B',
    )

    ChrTalk(
        0x0008,
        (
            '#0540341018V#100F我会继续进行分析。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540341019V提妲那孩子\n',
            '就请你们多多关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A278')

    def _loc_A22B(): pass

    label('loc_A22B')

    ChrTalk(
        0x0008,
        (
            '#0540341018V#100F我会继续进行分析。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540341021V塔的探索就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A278(): pass

    label('loc_A278')

    OP_8E(0x0008, -1060, 150, 7570, 2000, 0x00)
    OP_6F(0x0001, 15)
    OP_70(0x0001, 0x00000000)
    OP_73(0x0001)
    Sleep(500)

    SetChrPos(0x0008, -950, 0, 65390, 0)
    OP_4B(0x0008, 255)
    OP_A2(0x0012)
    OP_A2(0x1E4D)
    Fade(500)
    OP_6D(-1060, 0, 2880, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, -1060, 0, 2880, 180)
    SetChrPos(0x0001, -1060, 0, 2880, 180)
    SetChrPos(0x0002, -1060, 0, 2880, 180)
    SetChrPos(0x0003, -1060, 0, 2880, 180)
    CreateThread(0x0012, 0x01, 0x00, 0x002A)
    OP_0D()
    EventEnd(0x00)

    Return()

# id: 0x001B offset: 0xA34E
@scena.Code('func_1B_A34E')
def func_1B_A34E():
    Sleep(500)

    OP_6F(0x0001, 0)
    OP_70(0x0001, 0x0000000F)
    ClearChrFlags(0x00FE, 0x0080)
    OP_8E(0x00FE, -1060, 0, 4550, 2000, 0x00)

    Return()

# id: 0x001C offset: 0xA37B
@scena.Code('func_1C_A37B')
def func_1C_A37B():
    SetChrPos(0x00FE, 2700, 800, 4000, 180)
    ClearChrFlags(0x00FE, 0x0080)
    OP_90(0x00FE, 0, 0, -3000, 1000, 0x00)
    OP_90(0x00FE, -1500, 0, 0, 1000, 0x00)

    Return()

# id: 0x001D offset: 0xA3BA
@scena.Code('func_1D_A3BA')
def func_1D_A3BA():
    SetChrPos(0x00FE, 2700, 1800, 5000, 180)
    ClearChrFlags(0x00FE, 0x0080)
    OP_90(0x00FE, 0, 0, -3000, 1000, 0x00)
    OP_90(0x00FE, -1500, 0, 0, 1000, 0x00)

    Return()

# id: 0x001E offset: 0xA3F9
@scena.Code('func_1E_A3F9')
def func_1E_A3F9():
    SetChrPos(0x00FE, 3400, 1800, 4500, 180)
    ClearChrFlags(0x00FE, 0x0080)
    OP_90(0x00FE, 0, 0, -3500, 1000, 0x00)
    OP_90(0x00FE, -1000, 0, 0, 1000, 0x00)

    Return()

# id: 0x001F offset: 0xA438
@scena.Code('func_1F_A438')
def func_1F_A438():
    SetChrPos(0x00FE, 3400, 2800, 5500, 180)
    ClearChrFlags(0x00FE, 0x0080)
    OP_90(0x00FE, 0, 0, -3500, 1000, 0x00)
    OP_90(0x00FE, -1000, 0, 0, 1000, 0x00)

    Return()

# id: 0x0020 offset: 0xA477
@scena.Code('func_20_A477')
def func_20_A477():
    TerminateThread(0x0008, 0x01)

    @scena.Lambda('lambda_A481')
    def lambda_A481():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_A481)

    OP_8E(0x00FE, -1600, 0, 3410, 2000, 0x00)
    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x0021 offset: 0xA4A5
@scena.Code('func_21_A4A5')
def func_21_A4A5():
    OP_8E(0x00FE, -570, 0, 3410, 2000, 0x00)
    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x0022 offset: 0xA4C1
@scena.Code('func_22_A4C1')
def func_22_A4C1():
    OP_8E(0x00FE, -1810, 0, 2410, 2000, 0x00)
    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x0023 offset: 0xA4DD
@scena.Code('func_23_A4DD')
def func_23_A4DD():
    OP_8E(0x00FE, -400, 0, 2410, 2000, 0x00)
    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x0024 offset: 0xA4F9
@scena.Code('func_24_A4F9')
def func_24_A4F9():
    EventBegin(0x00)
    Fade(500)
    OP_6D(-770, 0, 64560, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -1430, 0, 64099, 0)
    SetChrPos(0x0102, -550, 0, 64099, 0)
    SetChrPos(0x00F8, -1450, 0, 63100, 0)
    SetChrPos(0x00F9, -550, 0, 63100, 0)
    OP_8C(0x0008, 180, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0540391405V#100F嗯？怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010391406V#1011F嗯，有个东西\n',
            '想要麻烦您调查一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020391407V#1040F其实，就是这个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.Item, ItemTable['数据水晶Ｚ']),
            (TxtCtl.SetColor, 0x0),
            '交出了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(ItemTable['数据水晶Ｚ'], 1)

    ChrTalk(
        0x0008,
        (
            '#0540391408V#100F哦，这不是\n',
            '数据水晶吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391409V嗯，似乎找不到\n',
            '什么破损的迹象。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391410V#101F稍等一下。\n',
            '我马上替你们分析。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Fade(1000)
    OP_6D(-5110, 0, 64310, 0)
    SetChrPos(0x0101, -4820, 0, 63930, 0)
    SetChrPos(0x0102, -5720, 0, 63930, 0)
    SetChrPos(0x00F8, -4070, 0, 64340, 315)
    SetChrPos(0x00F9, -6300, 0, 64440, 45)
    SetChrPos(0x0008, -5200, 0, 65530, 0)
    OP_62(0x0008, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_0D()
    Sleep(2000)

    OP_63(0x0008)

    ChrTalk(
        0x0008,
        (
            '#0540391411V#103F原来如此，\n',
            '这个东西相当不简单呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010391412V#1004F里、里面是什么内容？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0008, 180, 400)

    ChrTalk(
        0x0008,
        (
            '#0540391413V#100F似乎是关于\n',
            '古代武器制造方法的记录。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391414V看来好像要使用一种名叫\n',
            '塞姆里亚石的特殊金属……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x045B, 1, 0x22D9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A93E',
    )

    ChrTalk(
        0x0101,
        (
            '#0010391415V#1015F塞姆里亚石……\n',
            '好像在哪里听过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020391416V#1042F对了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020391417V#1040F那时候在王都的咖啡屋\n',
            '老板给我们的金属\n',
            '不就叫这个吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010391418V#1004F啊，的确如此！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010391419V#1001F……就是这种\n',
            '奇怪的金属。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A9CD')

    def _loc_A93E(): pass

    label('loc_A93E')

    ChrTalk(
        0x0101,
        (
            '#0010391420V#1015F<FIXME>ゼムリアストーン……\n',
            'それなら確か持ってるはずよ。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010391421V#1001F……このちょっと\n',
            '変わった金属のことでしょ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A9CD(): pass

    label('loc_A9CD')

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.Item, ItemTable['塞姆里亚石']),
            (TxtCtl.SetColor, 0x0),
            '交出了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0008,
        (
            '#0540391422V#103F哦，这真是太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391423V#101F有了这东西或许就好办多了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391424V#100F也许用这边的设施\n',
            '马上就能造出来呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391425V但是，在那之前必须\n',
            '让你们做一个选择。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010391426V#1015F选择？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540391427V#100F其实这里记录了两种武器\n',
            '的制造方法……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391428V但是从金属的量来看，\n',
            '只够做其中一种。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010391429V#1004F是吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010391430V#1007F唔，真难办呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540391431V#100F要制作哪一种，\n',
            '就交由你们来决定吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391432V#101F如何\n',
            '想要制作哪一种呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(30, 10, -1, -1)

    Talk(
        (
            TxtCtl.ShowAll,
            0x18,
            (TxtCtl.SetColor, 0x5),
            '<FIXME>どの武器を作成しますか？',
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

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        1,
        330,
        50,
        0,
        (
            TXT(0x00, '<FIXME>棒術具『麒麟具』\n'),
            TXT(0x01, '双剣  『鳳凰剣（鳳·凰）』\n'),
            TXT(0x02, '鞭    『天狼鞭』\n'),
            TXT(0x03, '導力銃『霊銃「久遠」』\n'),
            TXT(0x04, '片手剣『月読』\n'),
            TXT(0x05, '大剣  『奇剣「鬼喰い」』\n'),
            TXT(0x06, '導力砲『九龍砲』\n'),
            TXT(0x07, '手甲  『千手観音』\n'),
            TXT(0x08, '自動弓『破弓「綺羅星」』\n'),
            TXT(0x09, '【放弃】\n'),
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

    OP_5F(0x0001)
    OP_56(0x00)
    Call(0, 0x0025)
    OP_A2(0x22B1)

    Return()

# id: 0x0025 offset: 0xAD29
@scena.Code('func_25_AD29')
def func_25_AD29():
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_AD63'),
        (0x00000001, 'loc_AD63'),
        (0x00000002, 'loc_AD63'),
        (0x00000003, 'loc_AD63'),
        (0x00000004, 'loc_AD63'),
        (0x00000005, 'loc_AD63'),
        (0x00000006, 'loc_AD63'),
        (0x00000007, 'loc_AD63'),
        (0x00000008, 'loc_AD63'),
        (0x00000009, 'loc_B1F7'),
        (-1, 'loc_B2D7'),
    )

    def _loc_AD63(): pass

    label('loc_AD63')

    ChrTalk(
        0x0008,
        (
            '#0540391454V#100F<FIXME>うむ、判ったぞい。\n',
            'すぐに取りかかるとしよう。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_22(0x00B7, 0x00, 0x64)
    Sleep(2000)

    OP_6D(-770, 0, 64560, 0)
    SetChrPos(0x0101, -1430, 0, 64099, 0)
    SetChrPos(0x0102, -550, 0, 64099, 0)
    SetChrPos(0x00F8, -1450, 0, 63100, 0)
    SetChrPos(0x00F9, -550, 0, 63100, 0)
    SetChrPos(0x0008, -950, 0, 65390, 180)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0540391450V#101F好了，完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AEAE',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了#027i。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['麒麟具'], 1)

    Jump('loc_B15E')

    def _loc_AEAE(): pass

    label('loc_AEAE')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AF04',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了#049i。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['凤凰剑（凤·凰）'], 1)

    Jump('loc_B15E')

    def _loc_AF04(): pass

    label('loc_AF04')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AF5A',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了#079i。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['天狼鞭'], 1)

    Jump('loc_B15E')

    def _loc_AF5A(): pass

    label('loc_AF5A')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AFB0',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了#104i。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['枪６奥利维尔'], 1)

    Jump('loc_B15E')

    def _loc_AFB0(): pass

    label('loc_AFB0')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B006',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了#133i。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['刺剑6科洛丝'], 1)

    Jump('loc_B15E')

    def _loc_B006(): pass

    label('loc_B006')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B05C',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了#169i。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['奇剑「鬼灭之刃」'], 1)

    Jump('loc_B15E')

    def _loc_B05C(): pass

    label('loc_B05C')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B0B2',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了#192i。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['九龙炮'], 1)

    Jump('loc_B15E')

    def _loc_B0B2(): pass

    label('loc_B0B2')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B108',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了#221i。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['千手观音'], 1)

    Jump('loc_B15E')

    def _loc_B108(): pass

    label('loc_B108')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B15E',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了#231i。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(0x00E7, 1)

    Jump('loc_B15E')

    def _loc_B15E(): pass

    label('loc_B15E')

    RemoveItem(ItemTable['塞姆里亚石'], 1)

    ChrTalk(
        0x0101,
        (
            '#0010391451V#1001F多谢了，拉赛尔博士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020391452V#1040F我们一定\n',
            '会好好地使用它的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540391453V#100F嗯，今后探索时\n',
            '也要当心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B2D7')

    def _loc_B1F7(): pass

    label('loc_B1F7')

    ChrTalk(
        0x0101,
        (
            '#0010391459V#1016F嗯，真伤脑筋。\n',
            '可以暂时保留一下吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540391460V#100F没问题。\n',
            '考虑好之后再来就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    OP_6D(-2960, 0, 62700, 0)
    SetChrPos(0x0008, -950, 0, 65390, 0)
    SetChrPos(0x0101, -2960, 0, 62700, 0)
    SetChrPos(0x0102, -2960, 0, 62700, 0)
    SetChrPos(0x00F8, -2960, 0, 62700, 0)
    SetChrPos(0x00F9, -2960, 0, 62700, 0)
    OP_0D()

    Jump('loc_B2D7')

    def _loc_B2D7(): pass

    label('loc_B2D7')

    EventEnd(0x00)

    Return()

# id: 0x0026 offset: 0xB2DA
@scena.Code('func_26_B2DA')
def func_26_B2DA():
    EventBegin(0x00)
    Fade(500)
    OP_6D(-770, 0, 64560, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -1430, 0, 64099, 0)
    SetChrPos(0x0102, -550, 0, 64099, 0)
    SetChrPos(0x00F8, -1450, 0, 63100, 0)
    SetChrPos(0x00F9, -550, 0, 63100, 0)
    OP_8C(0x0008, 180, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0540391405V#100F嗯？怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010391406V#1011F嗯，有个东西\n',
            '想要麻烦您调查一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020391407V#1040F其实，就是这个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了#1048i。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(ItemTable['数据水晶Ｚ'], 1)

    ChrTalk(
        0x0008,
        (
            '#0540391408V#100F哦，这不是\n',
            '数据水晶吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391409V嗯，似乎找不到\n',
            '什么破损的迹象。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391410V#101F稍等一下。\n',
            '我马上替你们分析。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Fade(1000)
    OP_6D(-5110, 0, 64310, 0)
    SetChrPos(0x0101, -4820, 0, 63930, 0)
    SetChrPos(0x0102, -5720, 0, 63930, 0)
    SetChrPos(0x00F8, -4070, 0, 64340, 315)
    SetChrPos(0x00F9, -6300, 0, 64440, 45)
    SetChrPos(0x0008, -5200, 0, 65530, 0)
    OP_62(0x0008, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_0D()
    Sleep(1000)

    OP_63(0x0008)

    ChrTalk(
        0x0008,
        (
            '#0540391411V#103F原来如此、\n',
            '这个东西相当不简单呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010391412V#1004F里、里面是什么内容？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0008, 180, 400)

    ChrTalk(
        0x0008,
        (
            '#0540391413V#100F似乎是关于\n',
            '古代武器制造方法的记录。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391414V看来好像要使用一种名叫\n',
            '塞姆里亚石的特殊金属……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010391420V#1015F塞姆里亚石……\n',
            '记得我们应该有才对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010391421V#1001F……就是这个\n',
            '有些奇怪的金属吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了#1047i。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(ItemTable['塞姆里亚石'], 2)

    ChrTalk(
        0x0008,
        (
            '#0540391422V#103F哦，这真是太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391423V#101F有了这东西或许就好办多了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540391447V#100F也许用这边的设施\n',
            '马上就能造出来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010391448V#1001F真的吗？\n',
            '那么就拜托您了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540391449V#100F嗯，我明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x22B1)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_22(0x00B7, 0x00, 0x64)
    Sleep(2000)

    OP_6D(-770, 0, 64560, 0)
    SetChrPos(0x0101, -1430, 0, 64099, 0)
    SetChrPos(0x0102, -550, 0, 64099, 0)
    SetChrPos(0x00F8, -1450, 0, 63100, 0)
    SetChrPos(0x00F9, -550, 0, 63100, 0)
    SetChrPos(0x0008, -950, 0, 65390, 180)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0540391450V#101F好了，完成了。',
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
            '得到了',
            (TxtCtl.Item, ItemTable['麒麟具']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['凤凰剑（凤·凰）']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['凤凰剑（凤·凰）'], 1)
    AddItem(ItemTable['麒麟具'], 1)

    ChrTalk(
        0x0101,
        (
            '#0010391451V#1001F多谢了，拉赛尔博士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020391452V#1040F我们一定\n',
            '会好好地使用它的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540391453V#100F嗯，今后探索时\n',
            '也要当心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0013)
    EventEnd(0x00)

    Return()

# id: 0x0027 offset: 0xB959
@scena.Code('func_27_B959')
def func_27_B959():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　　　机关室\n',
            '※无关人员禁止入内',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0028 offset: 0xB9AB
@scena.Code('func_28_B9AB')
def func_28_B9AB():
    TalkBegin(0x00FF)
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
        32,
        1,
        (
            TXT(0x00, '在这里休息\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BA33',
    )

    OP_26(13)
    OP_20(0x00000BB8)
    FadeOut(1000, 0, -1)
    OP_22(0x000D, 0x00, 0x64)
    OP_0D()
    SetChrStatus(0x00FF, 0xFE, 0)
    OP_69(0x0000, 0x00000000)
    OP_30(0x01)
    Sleep(3500)

    OP_1E()
    FadeIn(1000, 0)
    OP_56(0x00)
    TalkEnd(0x00FF)

    Return()

    def _loc_BA33(): pass

    label('loc_BA33')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BA4D',
    )

    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

    def _loc_BA4D(): pass

    label('loc_BA4D')

    Return()

# id: 0x0029 offset: 0xBA4E
@scena.Code('func_29_BA4E')
def func_29_BA4E():
    Call(0, 0x0012)

    Return()

# id: 0x002A offset: 0xBA53
@scena.Code('func_2A_BA53')
def func_2A_BA53():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BA5C',
    )

    Return()

    def _loc_BA5C(): pass

    label('loc_BA5C')

    SetChrChipByIndex(0x0012, 15)
    SetChrSubChip(0x0012, 0)
    OP_4A(0x0012, 0)
    Sleep(2000)

    SetChrChipByIndex(0x0012, 9)
    SetChrSubChip(0x0012, 0)
    OP_4B(0x0012, 0)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

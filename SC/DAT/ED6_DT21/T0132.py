import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0132_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0132   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '奥利维尔'),
    TXT(0x02, '威诺'),
    TXT(0x03, '乘客'),
    TXT(0x04, '乘客'),
    TXT(0x05, '乘客'),
    TXT(0x06, '乘客'),
    TXT(0x07, '乘客'),
    TXT(0x08, '奥利维尔'),
    TXT(0x09, '安敦'),
    TXT(0x0A, '利库斯'),
    TXT(0x0B, '安敦'),
    TXT(0x0C, '林德号的乘客'),
    TXT(0x0D, '林德号的乘客'),
    TXT(0x0E, '林德号的乘客'),
    TXT(0x0F, '伊娜'),
    TXT(0x10, '安莉尔'),
    TXT(0x11, '小猫'),
    TXT(0x12, '小猫'),
    TXT(0x13, '小猫'),
    TXT(0x14, '利吉'),
    TXT(0x15, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0132.x'
    header.mapIndex       = 8
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x28FC
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
        ('ED6_DT26/CH20244._CH', 'ED6_DT26/CH20244P._CP'),
        ('ED6_DT07/CH01560._CH', 'ED6_DT07/CH01560P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
        ('ED6_DT07/CH01470._CH', 'ED6_DT07/CH01470P._CP'),
        ('ED6_DT26/CH20255._CH', 'ED6_DT26/CH20255P._CP'),
        ('ED6_DT07/CH01044._CH', 'ED6_DT07/CH01044P._CP'),
        ('ED6_DT07/CH01180._CH', 'ED6_DT07/CH01180P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01700._CH', 'ED6_DT07/CH01700P._CP'),
        ('ED6_DT27/CH03880._CH', 'ED6_DT27/CH03880P._CP'),
        ('ED6_DT27/CH03881._CH', 'ED6_DT27/CH03881P._CP'),
        ('ED6_DT27/CH03882._CH', 'ED6_DT27/CH03882P._CP'),
        ('ED6_DT07/CH01760._CH', 'ED6_DT07/CH01760P._CP'),
    ]

# id: 0x10002 offset: 0x12A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -83400,
            z                   = 600,
            y                   = 150180,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0187,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 4500,
            z                   = 0,
            y                   = 190660,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = -86920,
            z                   = 0,
            y                   = 152460,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = -87040,
            z                   = 0,
            y                   = 122170,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            x                   = -87150,
            z                   = 0,
            y                   = 118770,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            x                   = -45350,
            z                   = 0,
            y                   = 152520,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            x                   = -44610,
            z                   = 0,
            y                   = 153260,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = -83780,
            z                   = 0,
            y                   = 149780,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0105,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -82000,
            z                   = 200,
            y                   = 158050,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0195,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -83650,
            z                   = 0,
            y                   = 151440,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            x                   = -82000,
            z                   = -600,
            y                   = 158050,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0195,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            x                   = 5170,
            z                   = 0,
            y                   = 181750,
            direction           = 167,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0016,
        ),
        ScenaNpcData(
            x                   = -83940,
            z                   = 0,
            y                   = 152750,
            direction           = 256,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0017,
        ),
        ScenaNpcData(
            x                   = -48500,
            z                   = 0,
            y                   = 156140,
            direction           = 271,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0018,
        ),
        ScenaNpcData(
            x                   = -86540,
            z                   = 0,
            y                   = 119250,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            x                   = -85700,
            z                   = 0,
            y                   = 120430,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0195,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -87080,
            z                   = 0,
            y                   = 119580,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0019,
        ),
    )

# id: 0x10003 offset: 0x3AA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x3AA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x3AA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -83780,
            triggerZ            = 0,
            triggerY            = 150460,
            triggerRange        = 1000,
            actorX              = -84380,
            actorZ              = 1000,
            actorY              = 150260,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0013,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 6598,
            triggerZ            = 0,
            triggerY            = 190158,
            triggerRange        = 1000,
            actorX              = 4500,
            actorZ              = 1500,
            actorY              = 190662,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 3130,
            triggerZ            = 0,
            triggerY            = 192000,
            triggerRange        = 800,
            actorX              = 3130,
            actorZ              = 1000,
            actorY              = 192000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001A,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x416
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_43B',
    )

    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x0015, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_438',
    )

    ClearChrFlags(0x001B, 0x0080)

    def _loc_438(): pass

    label('loc_438')

    Jump('loc_4FF')

    def _loc_43B(): pass

    label('loc_43B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_46F',
    )

    ClearChrFlags(0x0011, 0x0080)

    If(
        (
            (Expr.Eval, "OP_29(0x0076, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_46C',
    )

    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    SetChrPos(0x0011, -83460, 0, 153000, 0)

    def _loc_46C(): pass

    label('loc_46C')

    Jump('loc_4FF')

    def _loc_46F(): pass

    label('loc_46F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_4B4',
    )

    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, -88460, 0, 155910, 268)
    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x000C, -84470, 0, 151460, 182)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000E, 0x0010)

    Jump('loc_4FF')

    def _loc_4B4(): pass

    label('loc_4B4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_4D7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 6, 0x181E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4C8',
    )

    ClearChrFlags(0x0008, 0x0080)

    def _loc_4C8(): pass

    label('loc_4C8')

    ClearChrFlags(0x000E, 0x0080)
    CreateThread(0x000E, 0x00, 0x00, 0x0002)

    Jump('loc_4FF')

    def _loc_4D7(): pass

    label('loc_4D7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_4FF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 6, 0x180E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4EB',
    )

    ClearChrFlags(0x000A, 0x0080)

    def _loc_4EB(): pass

    label('loc_4EB')

    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)

    def _loc_4FF(): pass

    label('loc_4FF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_509',
    )

    Jump('loc_65A')

    def _loc_509(): pass

    label('loc_509')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_513',
    )

    Jump('loc_65A')

    def _loc_513(): pass

    label('loc_513')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_653',
    )

    ClearChrFlags(0x0016, 0x0080)

    ExecExpressionWithValue(
        0x0018,
        0x2D,
        (
            (Expr.PushLong, 0x258),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0018,
        0x2E,
        (
            (Expr.PushLong, 0x258),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0018,
        0x2F,
        (
            (Expr.PushLong, 0x258),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0018,
        0x07,
        (
            (Expr.PushLong, 0x258),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0018,
        0x29,
        (
            (Expr.PushLong, 0x258),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0019,
        0x2D,
        (
            (Expr.PushLong, 0x258),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0019,
        0x2E,
        (
            (Expr.PushLong, 0x258),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0019,
        0x2F,
        (
            (Expr.PushLong, 0x258),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0019,
        0x07,
        (
            (Expr.PushLong, 0x258),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0019,
        0x29,
        (
            (Expr.PushLong, 0x258),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0019,
        0x28,
        (
            (Expr.PushLong, 0x10),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001A,
        0x2D,
        (
            (Expr.PushLong, 0x258),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001A,
        0x2E,
        (
            (Expr.PushLong, 0x258),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001A,
        0x2F,
        (
            (Expr.PushLong, 0x258),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001A,
        0x07,
        (
            (Expr.PushLong, 0x258),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001A,
        0x29,
        (
            (Expr.PushLong, 0x258),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearChrFlags(0x0017, 0x0080)
    ClearChrFlags(0x0018, 0x0080)
    ClearChrFlags(0x0019, 0x0080)
    ClearChrFlags(0x001A, 0x0080)
    SetChrFlags(0x0018, 0x0004)
    SetChrFlags(0x0019, 0x0004)
    SetChrFlags(0x0018, 0x0040)
    SetChrFlags(0x0019, 0x0040)
    SetChrPos(0x0016, -85600, 0, 119540, 0)
    SetChrPos(0x001A, -84190, 0, 123070, 330)
    SetChrPos(0x0019, -83500, 580, 117300, 270)
    SetChrPos(0x0018, -83030, 580, 116830, 315)
    CreateThread(0x001A, 0x01, 0x00, 0x0006)
    CreateThread(0x0019, 0x01, 0x00, 0x0007)
    CreateThread(0x0018, 0x01, 0x00, 0x0008)

    Jump('loc_65A')

    def _loc_653(): pass

    label('loc_653')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_65A',
    )

    def _loc_65A(): pass

    label('loc_65A')

    Return()

# id: 0x0001 offset: 0x65B
@scena.Code('Init')
def Init():
    OP_82(0x80, 0x00)
    OP_82(0x82, 0x00)

    If(
        (
            (Expr.Eval, "OP_29(0x0076, 0x00, 0x10)"),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_68F',
    )

    OP_25(0x01CB, 0xFFFEBFB0, 0x000004B0, 0x00026962, 0x000007D0, 0x00002710, 0x64, 0x00000000)

    Jump('loc_692')

    def _loc_68F(): pass

    label('loc_68F')

    OP_82(0x81, 0x00)

    def _loc_692(): pass

    label('loc_692')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 6, 0x181E)),
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_6A2',
    )

    OP_64(0x00, 0x0001)

    def _loc_6A2(): pass

    label('loc_6A2')

    Return()

# id: 0x0002 offset: 0x6A3
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_6C6',
    )

    OP_8D(0x00FE, -46050, 153320, -43570, 152040, 2000)

    Jump('ReInit')

    def _loc_6C6(): pass

    label('loc_6C6')

    Return()

# id: 0x0003 offset: 0x6C7
@scena.Code('func_03_6C7')
def func_03_6C7():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_703',
    )

    OP_9E(0x0010, 0x00000019, 0x00000000, 0x0000012C, 0x00000FA0)
    Sleep(400)

    OP_9E(0x0010, 0x00000019, 0x00000000, 0x0000012C, 0x00000FA0)
    Sleep(2500)

    Jump('func_03_6C7')

    def _loc_703(): pass

    label('loc_703')

    Return()

# id: 0x0004 offset: 0x704
@scena.Code('func_04_704')
def func_04_704():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_727',
    )

    OP_8D(0x00FE, -83510, 153450, -85710, 152080, 2000)

    Jump('func_04_704')

    def _loc_727(): pass

    label('loc_727')

    Return()

# id: 0x0005 offset: 0x728
@scena.Code('func_05_728')
def func_05_728():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_74B',
    )

    OP_8D(0x00FE, 4880, 177010, 6450, 182780, 2000)

    Jump('func_05_728')

    def _loc_74B(): pass

    label('loc_74B')

    Return()

# id: 0x0006 offset: 0x74C
@scena.Code('func_06_74C')
def func_06_74C():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_76F',
    )

    OP_8D(0x00FE, -85500, 124240, -83590, 123040, 1000)

    Jump('func_06_74C')

    def _loc_76F(): pass

    label('loc_76F')

    Return()

# id: 0x0007 offset: 0x770
@scena.Code('func_07_770')
def func_07_770():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_793',
    )

    OP_8D(0x00FE, -83000, 117760, -83510, 116930, 1000)

    Jump('func_07_770')

    def _loc_793(): pass

    label('loc_793')

    Return()

# id: 0x0008 offset: 0x794
@scena.Code('func_08_794')
def func_08_794():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_7B7',
    )

    OP_8D(0x00FE, -84200, 117760, -83500, 116930, 1000)

    Jump('func_08_794')

    def _loc_7B7(): pass

    label('loc_7B7')

    Return()

# id: 0x0009 offset: 0x7B8
@scena.Code('func_09_7B8')
def func_09_7B8():
    ClearChrFlags(0x00FE, 0x0001)
    def _loc_7BD(): pass

    label('loc_7BD')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_817',
    )

    OP_8C(0x00FE, 270, 400)
    OP_8E(0x00FE, -84140, 4019, 122290, 1000, 0x00)
    OP_8C(0x00FE, 180, 400)
    Sleep(1000)

    OP_8C(0x00FE, 90, 400)
    OP_8E(0x00FE, -81450, 4019, 122290, 1000, 0x00)
    OP_8C(0x00FE, 180, 400)
    Sleep(1000)

    Jump('loc_7BD')

    def _loc_817(): pass

    label('loc_817')

    Return()

# id: 0x000A offset: 0x818
@scena.Code('func_0A_818')
def func_0A_818():
    Call(0, 0x000B)

    Return()

# id: 0x000B offset: 0x81D
@scena.Code('func_0B_81D')
def func_0B_81D():
    TalkBegin(0x0009)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_854',
    )

    Call(6, 0x0006)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_843',
    )

    OP_A9(0x05)
    TalkEnd(0x0009)

    Return()

    def _loc_843(): pass

    label('loc_843')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_854',
    )

    TalkEnd(0x0009)

    Return()

    def _loc_854(): pass

    label('loc_854')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_B81',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0414, 4, 0x20A4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A28',
    )

    OP_62(0x0009, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x0009, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x0009,
        (
            '啊、是艾丝蒂尔……\n',
            '今天约修亚也一起来了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0102, 400)

    ChrTalk(
        0x0009,
        (
            '真是好久都没看见\n',
            '约修亚了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F嗯，确实啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '导力器已经不能用了，\n',
            '旅馆营业没问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '是，无论如何也要\n',
            '继续营业。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '因为滞留在飞船坪\n',
            '的人都要住在这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1026F是吗……\n',
            '坐定期船来的那些人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9EB',
    )

    ChrTalk(
        0x0103,
        (
            '#522F抱歉，还要请您\n',
            '再坚持一阵。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我们会尽全力去\n',
            '改善现在的状况的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9EB(): pass

    label('loc_9EB')

    ChrTalk(
        0x0009,
        (
            '嗯，我知道大家\n',
            '很努力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '我会继续支持你们的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x20A4)

    Jump('loc_B7E')

    def _loc_A28(): pass

    label('loc_A28')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 6, 0x2086)),
            Expr.Return,
        ),
        'loc_A93',
    )

    ChrTalk(
        0x0009,
        (
            '刚才听到结婚\n',
            '礼乐了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '结婚仪式算是最近\n',
            '少有的开心话题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '祝福那对年轻\n',
            '的新人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B7E')

    def _loc_A93(): pass

    label('loc_A93')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B29',
    )

    ChrTalk(
        0x0009,
        (
            '导力器不能使用\n',
            '对我们的营业\n',
            '有很大影响呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '不过我们还是努力\n',
            '维持着营业。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '滞留在飞船坪的那些人倒也算是\n',
            '提供了足够的客源。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_B7E')

    def _loc_B29(): pass

    label('loc_B29')

    ChrTalk(
        0x0009,
        (
            '导力器不能使用\n',
            '对我们的营业……\n',
            '总之状况很不好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '希望可以早点\n',
            '恢复正常吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B7E(): pass

    label('loc_B7E')

    Jump('loc_108F')

    def _loc_B81(): pass

    label('loc_B81')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_C5C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_BD8',
    )

    ChrTalk(
        0x0009,
        (
            '被限制行动的客人们\n',
            '也平安出发了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '希望他们下次\n',
            '旅行顺利啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C59')

    def _loc_BD8(): pass

    label('loc_BD8')

    ChrTalk(
        0x0009,
        (
            '定期船终于恢复了，\n',
            '被限制行动的客人们\n',
            '也平安出发了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '客人都平安的离开了，\n',
            '心情真好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '希望他们下次\n',
            '旅行顺利啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_C59(): pass

    label('loc_C59')

    Jump('loc_108F')

    def _loc_C5C(): pass

    label('loc_C5C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_CE5',
    )

    ChrTalk(
        0x0009,
        (
            '王国军的人\n',
            '好像也到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '洛连特这里来了\n',
            '很多穿军服的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这种状况下，这也是没办法的事。\n',
            '现在要以警备工作为优先。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_108F')

    def _loc_CE5(): pass

    label('loc_CE5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_E0D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 6, 0x181E)),
            Expr.Return,
        ),
        'loc_D5C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_D1E',
    )

    ChrTalk(
        0x0009,
        (
            '昨天谢谢了，\n',
            '欢迎下次光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D59')

    def _loc_D1E(): pass

    label('loc_D1E')

    ChrTalk(
        0x0009,
        (
            '巡逻到深夜还\n',
            '真是辛苦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '希望你们下次\n',
            '再来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_D59(): pass

    label('loc_D59')

    Jump('loc_E0A')

    def _loc_D5C(): pass

    label('loc_D5C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_DAA',
    )

    ChrTalk(
        0x0009,
        (
            '你们的伙伴正在房间\n',
            '中休息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '好像还在睡，\n',
            '看样子很累了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E0A')

    def _loc_DAA(): pass

    label('loc_DAA')

    ChrTalk(
        0x0009,
        (
            '啊，各位，\n',
            '早上好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '你们的伙伴正在房间\n',
            '中休息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '好像还在睡，\n',
            '看样子很累了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_E0A(): pass

    label('loc_E0A')

    Jump('loc_108F')

    def _loc_E0D(): pass

    label('loc_E0D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_F41',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_E75',
    )

    ChrTalk(
        0x0009,
        (
            '浓雾的事\n',
            '我也记不清楚了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '街道视线很差，\n',
            '可能会有危险哟。\n',
            '请不要贸然行动啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F3E')

    def _loc_E75(): pass

    label('loc_E75')

    ChrTalk(
        0x0009,
        (
            '艾丝蒂尔、\n',
            '还有雪拉扎德…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '欢迎光临浓雾中的\n',
            '洛连特旅馆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '…４位都要住宿吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F呜…不是呢，\n',
            '只是来看看而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这样状况不明，\n',
            '街道上就很危险了吧…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '无论如何请大家小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_F3E(): pass

    label('loc_F3E')

    Jump('loc_108F')

    def _loc_F41(): pass

    label('loc_F41')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 3, 0x1003)),
            Expr.Return,
        ),
        'loc_108F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_F9D',
    )

    ChrTalk(
        0x0009,
        (
            '艾丝蒂尔和\n',
            '约修亚是我们洛连特的骄傲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '没开玩笑，我真是那么想的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_108F')

    def _loc_F9D(): pass

    label('loc_F9D')

    ChrTalk(
        0x0009,
        (
            '啊……\n',
            '这不是艾丝蒂尔吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '听说你在各地十分活跃，\n',
            '还取得了武术大会的优胜啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '艾丝蒂尔和约修亚\n',
            '已经是洛连特的骄傲了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊啊～\n',
            '不要太夸赞我啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这不是夸赞，\n',
            '而是真心的想法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0142,
        (
            '#1060F（嘿……\n',
            '　真了不起呢……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_108F(): pass

    label('loc_108F')

    TalkEnd(0x0009)

    Return()

# id: 0x000C offset: 0x1093
@scena.Code('func_0C_1093')
def func_0C_1093():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_118E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1112',
    )

    ChrTalk(
        0x00FE,
        (
            '先去柏斯有急事，\n',
            '然后还要返回王都，\n',
            '都要用到飞船啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过有游击士的护送，\n',
            '算了，步行应该也可以。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_118E')

    def _loc_1112(): pass

    label('loc_1112')

    ChrTalk(
        0x00FE,
        (
            '我有些急事必须\n',
            '要去柏斯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '然后还要返回王都，\n',
            '都要用到飞船啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过有游击士的护送，\n',
            '算了，步行应该也可以。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_118E(): pass

    label('loc_118E')

    TalkEnd(0x000A)

    Return()

# id: 0x000D offset: 0x1192
@scena.Code('func_0D_1192')
def func_0D_1192():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_11D6',
    )

    ChrTalk(
        0x00FE,
        (
            '钱、钱包已经…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '接、接下来一定\n',
            '要节约一点了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12D0')

    def _loc_11D6(): pass

    label('loc_11D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_12D0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1231',
    )

    ChrTalk(
        0x00FE,
        (
            '真没想到要在这么豪华\n',
            '的旅馆住宿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可、可以吗？\n',
            '真是没心理准备，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12D0')

    def _loc_1231(): pass

    label('loc_1231')

    ChrTalk(
        0x00FE,
        (
            '本来想着在飞船公社\n',
            '住宿就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他们说是普通的住处，\n',
            '都没抱过什么期待。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真没想到要在这么豪华\n',
            '的旅馆住宿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可、可以吗？\n',
            '还没心理准备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_12D0(): pass

    label('loc_12D0')

    TalkEnd(0x000B)

    Return()

# id: 0x000E offset: 0x12D4
@scena.Code('func_0E_12D4')
def func_0E_12D4():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_136B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1321',
    )

    ChrTalk(
        0x00FE,
        (
            '真是很不错的店呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他给我买了好多\n',
            '的小礼物呢㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1368')

    def _loc_1321(): pass

    label('loc_1321')

    ChrTalk(
        0x00FE,
        (
            '商店街中有个\n',
            '不错的杂货店呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他给我买了好多\n',
            '的小礼物呢㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    def _loc_1368(): pass

    label('loc_1368')

    Jump('loc_13E5')

    def _loc_136B(): pass

    label('loc_136B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_13E5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_13B7',
    )

    ChrTalk(
        0x00FE,
        (
            '要是能免费住在这个房间的话，\n',
            '我就愿意原谅公社的过失。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13E5')

    def _loc_13B7(): pass

    label('loc_13B7')

    ChrTalk(
        0x00FE,
        (
            '哇～好棒的房间啊。\n',
            '疲劳马上就没有了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    def _loc_13E5(): pass

    label('loc_13E5')

    TalkEnd(0x000C)

    Return()

# id: 0x000F offset: 0x13E9
@scena.Code('func_0F_13E9')
def func_0F_13E9():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_1434',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯～要是带着\n',
            '扑克来就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是不错的\n',
            '亲子旅行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14D9')

    def _loc_1434(): pass

    label('loc_1434')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_14D9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_1484',
    )

    ChrTalk(
        0x00FE,
        (
            '不过，在雾散去之前\n',
            '要做什么好呢～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，真是烦恼呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14D9')

    def _loc_1484(): pass

    label('loc_1484')

    ChrTalk(
        0x00FE,
        (
            '呼，替我们准备好了住处，\n',
            '总算是放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不愧是公社啊。\n',
            '应对措施很完善。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    def _loc_14D9(): pass

    label('loc_14D9')

    TalkEnd(0x000D)

    Return()

# id: 0x0010 offset: 0x14DD
@scena.Code('func_10_14DD')
def func_10_14DD():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_1597',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_152F',
    )

    ChrTalk(
        0x00FE,
        (
            '看啊，爸爸。\n',
            '该轮到爸爸了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '特制的饼干中\n',
            '的干字哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1594')

    def _loc_152F(): pass

    label('loc_152F')

    ChrTalk(
        0x00FE,
        (
            '爸爸～要玩接龙吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，第一个词是\n',
            '特制的饼干。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，该轮到爸爸了。\n',
            '是饼干的干字哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0006)

    def _loc_1594(): pass

    label('loc_1594')

    Jump('loc_1631')

    def _loc_1597(): pass

    label('loc_1597')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_15D7',
    )

    ChrTalk(
        0x00FE,
        (
            '爸爸去飞船坪\n',
            '查看情况了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以我\n',
            '留在这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1631')

    def _loc_15D7(): pass

    label('loc_15D7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_1631',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1604',
    )

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，我最喜欢外宿了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1631')

    def _loc_1604(): pass

    label('loc_1604')

    ChrTalk(
        0x00FE,
        (
            '今天就住在这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，太好啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0006)

    def _loc_1631(): pass

    label('loc_1631')

    TalkEnd(0x000E)

    Return()

# id: 0x0011 offset: 0x1635
@scena.Code('func_11_1635')
def func_11_1635():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_1682',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_165B',
    )

    ChrTalk(
        0x00FE,
        (
            '呜——呜——',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1682')

    def _loc_165B(): pass

    label('loc_165B')

    ChrTalk(
        0x00FE,
        (
            '呜——呜——',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '心情真不好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0007)

    def _loc_1682(): pass

    label('loc_1682')

    TalkEnd(0x00FE)

    Return()

# id: 0x0012 offset: 0x1686
@scena.Code('func_12_1686')
def func_12_1686():
    TalkBegin(0x0011)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_17B8',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0076, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_1757',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_16E6',
    )

    ChrTalk(
        0x00FE,
        (
            '安敦那家伙\n',
            '好像很痛苦的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明明不会喝酒\n',
            '却喝那么多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1754')

    def _loc_16E6(): pass

    label('loc_16E6')

    ChrTalk(
        0x00FE,
        (
            '虽然有教区长\n',
            '在照顾他，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但安敦那家伙\n',
            '好像很痛苦的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过也许只能暂时\n',
            '把他扔在一边了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0008)

    def _loc_1754(): pass

    label('loc_1754')

    Jump('loc_17B8')

    def _loc_1757(): pass

    label('loc_1757')

    ChrTalk(
        0x00FE,
        (
            '安敦那家伙\n',
            '明明是没结果的单相思，\n',
            '却还是不死心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '算了，在他明白之前，\n',
            '我一直在这里等。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17B8(): pass

    label('loc_17B8')

    TalkEnd(0x0011)

    Return()

# id: 0x0013 offset: 0x17BC
@scena.Code('func_13_17BC')
def func_13_17BC():
    OP_62(0x000F, 0x00000000, 2000, 0x1C, 0x21, 0x000000FA, 0x00)
    Sleep(1000)

    OP_63(0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_181E',
    )

    ChrTalk(
        0x000F,
        (
            '#0040290328V#034F呜～呜……………\n',
            '……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AAC')

    def _loc_181E(): pass

    label('loc_181E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0310, 6, 0x1886)),
            Expr.Return,
        ),
        'loc_18E2',
    )

    ChrTalk(
        0x000F,
        (
            '#0040290329V#034F呜……呜……………\n',
            '……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040290330V已……已经不能……………\n',
            '…………再、再喝了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040290328V#034F呜～呜……………\n',
            '……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    Jump('loc_1AAC')

    def _loc_18E2(): pass

    label('loc_18E2')

    ChrTalk(
        0x000F,
        (
            '#0040290329V#034F呜……呜……………\n',
            '……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040290333V啊啊……雪拉小姐………\n',
            '……爱、爱娜……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040290334V已……已经不能……………\n',
            '…………再、再喝了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0008, 0x0000000F, 0x00000000, 0x0000012C, 0x00000FA0)

    ChrTalk(
        0x000F,
        (
            '#0040290335V#038F哇…………………\n',
            '……那个瓶子……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0008, 0x0000000F, 0x00000000, 0x0000012C, 0x00000FA0)

    ChrTalk(
        0x000F,
        (
            '#0040290336V#038F啊啊………………！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0008, 0x0000000F, 0x00000000, 0x0000012C, 0x00000FA0)

    ChrTalk(
        0x000F,
        (
            '#0040290337V#038F……○△×＄□￥～～！！',
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
            '#0010290338V#1019F（似乎做恶梦了啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_1AAC(): pass

    label('loc_1AAC')

    OP_A2(0x1886)
    TalkEnd(0x00FF)

    Return()

# id: 0x0014 offset: 0x1AB3
@scena.Code('func_14_1AB3')
def func_14_1AB3():
    TalkBegin(0x0016)

    If(
        (
            (Expr.Eval, "OP_29(0x0074, 0x01, 0x2000)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0074, 0x00, 0x08)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0074, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1BBC',
    )

    ChrTalk(
        0x00FE,
        (
            '啊～各位游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们看～～安莉尔\n',
            '当了妈妈回来了哦～',
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
            '#1004F咦咦！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '带、带着自己的宝宝们回来的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '嗯～是啊～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以，现在\n',
            '正在想名字哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯～怎样的名字\n',
            '才好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0074, 0x01, 0x2000)

    Jump('loc_1E49')

    def _loc_1BBC(): pass

    label('loc_1BBC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_1CEB',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0074, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_1CA4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_1C1B',
    )

    ChrTalk(
        0x00FE,
        (
            '雾好像\n',
            '一点要散去的迹象都没有啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '连阿姨都\n',
            '有点担心了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CA1')

    def _loc_1C1B(): pass

    label('loc_1C1B')

    ChrTalk(
        0x00FE,
        (
            '啊～各位游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是辛苦，在这种天气\n',
            '也要工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '雾好像\n',
            '一点要散去的迹象都没有啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊～洛连特究竟\n',
            '怎么了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    def _loc_1CA1(): pass

    label('loc_1CA1')

    Jump('loc_1CE8')

    def _loc_1CA4(): pass

    label('loc_1CA4')

    ChrTalk(
        0x00FE,
        (
            '雾好像\n',
            '一点要散去的迹象都没有啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '连阿姨都\n',
            '有点担心了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1CE8(): pass

    label('loc_1CE8')

    Jump('loc_1E49')

    def _loc_1CEB(): pass

    label('loc_1CEB')

    If(
        (
            (Expr.Eval, "OP_29(0x0074, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_1DEA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_1D63',
    )

    ChrTalk(
        0x00FE,
        (
            '今天又是这种鬼天气，\n',
            '阿姨在家休息了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要好好想想小猫们\n',
            '的名字啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼呼～阿姨好烦恼㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DE7')

    def _loc_1D63(): pass

    label('loc_1D63')

    ChrTalk(
        0x00FE,
        (
            '啊～各位游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼呼～～昨天\n',
            '真是多谢了㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天又是这种鬼天气，\n',
            '阿姨在家休息了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要好好想想小猫们\n',
            '的名字啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    def _loc_1DE7(): pass

    label('loc_1DE7')

    Jump('loc_1E49')

    def _loc_1DEA(): pass

    label('loc_1DEA')

    ChrTalk(
        0x00FE,
        (
            '雾好像\n',
            '越来越浓了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天好像不能\n',
            '在阳台午睡了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和小猫们一起在家\n',
            '好好休息吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E49(): pass

    label('loc_1E49')

    TalkEnd(0x0016)

    Return()

# id: 0x0015 offset: 0x1E4D
@scena.Code('func_15_1E4D')
def func_15_1E4D():
    TalkBegin(0x0017)
    OP_22(0x0192, 0x00, 0x64)

    ChrTalk(
        0x00FE,
        (
            '喵～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0017)

    Return()

# id: 0x0016 offset: 0x1E65
@scena.Code('func_16_1E65')
def func_16_1E65():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 6, 0x2086)),
            Expr.Return,
        ),
        'loc_1ECC',
    )

    ChrTalk(
        0x00FE,
        (
            '还在想为什么这么热闹，\n',
            '原来是结婚仪式啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，真不错啊。\n',
            '让人感到人性的坚强。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F20')

    def _loc_1ECC(): pass

    label('loc_1ECC')

    ChrTalk(
        0x00FE,
        (
            '洛连特暂时是没事了，\n',
            '但不知道别的城市怎么样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也许暂时待在\n',
            '这里比较好吧…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F20(): pass

    label('loc_1F20')

    TalkEnd(0x00FE)

    Return()

# id: 0x0017 offset: 0x1F24
@scena.Code('func_17_1F24')
def func_17_1F24():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_1F87',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才在城里转了转，\n',
            '大家比我想象的要冷静啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼～乡村城市\n',
            '还真是名不虚传啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_204F')

    def _loc_1F87(): pass

    label('loc_1F87')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1FD4',
    )

    ChrTalk(
        0x00FE,
        (
            '四处去看了看，\n',
            '哪里都没什么变化。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……我就在这里等着了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_204F')

    def _loc_1FD4(): pass

    label('loc_1FD4')

    ChrTalk(
        0x00FE,
        (
            '看了看飞船坪的情况，\n',
            '那里也有一些人，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过似乎都是被迫待在那里的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然指示灯还亮着，\n',
            '但飞船无法起飞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_204F(): pass

    label('loc_204F')

    TalkEnd(0x00FE)

    Return()

# id: 0x0018 offset: 0x2053
@scena.Code('func_18_2053')
def func_18_2053():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_20FA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_20A6',
    )

    ChrTalk(
        0x00FE,
        (
            '这种时候也没有工作了，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好好休息吧。\n',
            '等着定期船恢复。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20F7')

    def _loc_20A6(): pass

    label('loc_20A6')

    ChrTalk(
        0x00FE,
        (
            '王国中的导力器\n',
            '好像都瘫痪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这种时候也不会有工作，\n',
            '稍微歇一歇吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    def _loc_20F7(): pass

    label('loc_20F7')

    Jump('loc_21C5')

    def _loc_20FA(): pass

    label('loc_20FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_2158',
    )

    ChrTalk(
        0x00FE,
        (
            '雾散去之前\n',
            '就可以随意使用这房间哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说是第二次说……\n',
            '不过拜托饶了我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21C5')

    def _loc_2158(): pass

    label('loc_2158')

    ChrTalk(
        0x00FE,
        (
            '之前在洛连特\n',
            '也是因为大雾停留在这…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，那时候好像\n',
            '也是住在这房间哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，好厉害的巧合啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    def _loc_21C5(): pass

    label('loc_21C5')

    TalkEnd(0x00FE)

    Return()

# id: 0x0019 offset: 0x21C9
@scena.Code('func_19_21C9')
def func_19_21C9():
    TalkBegin(0x001B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_284C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0413, 7, 0x209F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_27CF',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_221B',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，艾丝蒂尔和约修亚～\n',
            '……还有雪拉前辈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2294')

    def _loc_221B(): pass

    label('loc_221B')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_225B',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，艾丝蒂尔和约修亚～\n',
            '还有阿加特先生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2294')

    def _loc_225B(): pass

    label('loc_225B')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2294',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，艾丝蒂尔和约修亚～\n',
            '还有金先生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2294(): pass

    label('loc_2294')

    ChrTalk(
        0x00FE,
        (
            '那个……在矿山\n',
            '麻烦你们了，真是感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2383',
    )

    ChrTalk(
        0x0103,
        (
            '#524F不用在意，\n',
            '你做很出色。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '真的…\n',
            '说老实话，要对你刮目相看了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0103, 400)

    ChrTalk(
        0x00FE,
        (
            '啊…？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F勇气十足地留在现场，\n',
            '保护了全体矿工。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '多余的话就不说了，\n',
            '总之，你做得很出色。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24B4')

    def _loc_2383(): pass

    label('loc_2383')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2414',
    )

    ChrTalk(
        0x0106,
        (
            '#051F不要介意，\n',
            '你干得已经很棒了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '在那种艰难的情形下做出最佳判断，\n',
            '真的很了不起。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '多余的话就不多说了，\n',
            '总之你做得很好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24B4')

    def _loc_2414(): pass

    label('loc_2414')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_24B4',
    )

    ChrTalk(
        0x0108,
        (
            '#070F不用介意啊。\n',
            '我认为你做得很出色。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '在那种艰难的情形下做出最佳判断，\n',
            '而且也达到了目的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '任何一个优秀的游击士\n',
            '也都会做出和你一样的判断。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_24B4(): pass

    label('loc_24B4')

    ChrTalk(
        0x0101,
        (
            '#1015F嗯，确实……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '毕竟利吉先生是\n',
            '一个人在奋战啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F我们只是来增援的，\n',
            '功劳可远不如你呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '啊、谢谢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可、可是…\n',
            '我还差得很远呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_25F3',
    )

    ChrTalk(
        0x0103,
        (
            '#025F哈哈，没自信\n',
            '就是你最大的缺点了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#027F你的实力很不错，\n',
            '所以应该拿出自信。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '只要有你在的话，\n',
            '我们即使离开也不会担心的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0103, 400)

    Jump('loc_270D')

    def _loc_25F3(): pass

    label('loc_25F3')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2689',
    )

    ChrTalk(
        0x0106,
        (
            '#551F缺乏自信\n',
            '就是你最大的弱点啦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#050F既然自己有实力，\n',
            '就应该拿出信心来！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '正因为有你在，\n',
            '所以雪拉扎德\n',
            '可以放心离开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0106, 400)

    Jump('loc_270D')

    def _loc_2689(): pass

    label('loc_2689')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_270D',
    )

    ChrTalk(
        0x0108,
        (
            '#070F不要说那种\n',
            '话啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '你的实力很不错，\n',
            '所以应该拿出自信来！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '正因为有你在，\n',
            '所以雪拉扎德\n',
            '可以放心离开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0108, 400)

    def _loc_270D(): pass

    label('loc_270D')

    ChrTalk(
        0x00FE,
        (
            '是、是的！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我今后也会继续努力，\n',
            '争取追上前辈们的！',
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
        'loc_2776',
    )

    ChrTalk(
        0x0108,
        (
            '#070F嗯！这样才对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27C9')

    def _loc_2776(): pass

    label('loc_2776')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_279E',
    )

    ChrTalk(
        0x0106,
        (
            '#051F嗯，努力吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27C9')

    def _loc_279E(): pass

    label('loc_279E')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_27C9',
    )

    ChrTalk(
        0x0103,
        (
            '#021F呵呵，就是要这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_27C9(): pass

    label('loc_27C9')

    OP_A2(0x209F)

    Jump('loc_284C')

    def _loc_27CF(): pass

    label('loc_27CF')

    ChrTalk(
        0x00FE,
        (
            '虽然身体还疼得很……\n',
            '但总觉得很充实呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真的……\n',
            '能当游击士真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '通过这次的事件，\n',
            '这种想法更加坚定了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_284C(): pass

    label('loc_284C')

    TalkEnd(0x001B)

    Return()

# id: 0x001A offset: 0x2850
@scena.Code('func_1A_2850')
def func_1A_2850():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　　　　　　　工作人员室　　　　　　　\n',
            '          ※无关人员请勿入内',
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

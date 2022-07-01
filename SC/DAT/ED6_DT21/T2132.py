import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T2132_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2132   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '奈尔'),
    TXT(0x02, '朵洛希'),
    TXT(0x03, '亚内斯特'),
    TXT(0x04, '诺曼'),
    TXT(0x05, '德尔斯'),
    TXT(0x06, '奈尔'),
    TXT(0x07, '海利欧'),
    TXT(0x08, '贝尔夫'),
    TXT(0x09, '森特'),
    TXT(0x0A, '海利欧'),
    TXT(0x0B, '巴克'),
    TXT(0x0C, '贝尔娜'),
    TXT(0x0D, '昆茨'),
    TXT(0x0E, '阿加特'),
    TXT(0x0F, '雪拉扎德'),
    TXT(0x10, '奥利维尔'),
    TXT(0x11, '目标用照相机'),
    TXT(0x12, '目标用照相机2'),
    TXT(0x13, '德尔斯'),
    TXT(0x14, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2132.x'
    header.mapIndex       = 1
    header.bgm            = 12
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT21/T2132._SN', 'ED6_DT21/T2132_1._SN', 'ED6_DT21/T2132_2._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x354B
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
            dword_28        = 2600,
            dword_2C        = 262,
            word_30         = 35,
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
        ('ED6_DT07/CH02063._CH', 'ED6_DT07/CH02063P._CP'),
        ('ED6_DT26/CH20285._CH', 'ED6_DT26/CH20285P._CP'),
        ('ED6_DT07/CH01570._CH', 'ED6_DT07/CH01570P._CP'),
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH02060._CH', 'ED6_DT07/CH02060P._CP'),
        ('ED6_DT07/CH01220._CH', 'ED6_DT07/CH01220P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01660._CH', 'ED6_DT07/CH01660P._CP'),
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
        ('ED6_DT06/CH20039._CH', 'ED6_DT06/CH20039P._CP'),
        ('ED6_DT07/CH00050._CH', 'ED6_DT07/CH00050P._CP'),
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT07/CH01043._CH', 'ED6_DT07/CH01043P._CP'),
        ('ED6_DT07/CH01390._CH', 'ED6_DT07/CH01390P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
    ]

# id: 0x10002 offset: 0x132
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
            npcIndex            = 0x0195,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0195,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            x                   = -1900,
            z                   = 0,
            y                   = 11500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = -2660,
            z                   = 0,
            y                   = 80950,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = -2570,
            z                   = 0,
            y                   = 79390,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = -2570,
            z                   = 0,
            y                   = 79390,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
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
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0001,
        ),
        ScenaNpcData(
            x                   = 650,
            z                   = 0,
            y                   = 43430,
            direction           = 95,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0002,
        ),
        ScenaNpcData(
            x                   = -46277,
            z                   = 0,
            y                   = 4360,
            direction           = 346,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0000,
        ),
        ScenaNpcData(
            x                   = 28130,
            z                   = 0,
            y                   = 49490,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            x                   = 1760,
            z                   = 0,
            y                   = 3430,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            x                   = 5100,
            z                   = 0,
            y                   = 8920,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
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
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x000A,
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
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0010,
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
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0010,
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
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x000B,
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
        ScenaNpcData(
            x                   = -4500,
            z                   = 250,
            y                   = 80360,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0195,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
    )

# id: 0x10003 offset: 0x392
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x392
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 22000,
            y           = -100,
            z           = 78170,
            range       = 22800,
            dword_10    = 0x000003E8,
            dword_14    = 0x00012818,
            dword_18    = 0x00010000,
            dword_1C    = 0x00000002,
        ),
        ScenaEventData(
            x           = 5280,
            y           = 1900,
            z           = 41390,
            range       = 7180,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00009C18,
            dword_18    = 0x00010000,
            dword_1C    = 0x00000003,
        ),
        ScenaEventData(
            x           = -1290,
            y           = -100,
            z           = 4070,
            range       = 2510,
            dword_10    = 0x000003E8,
            dword_14    = 0xFFFFFC4A,
            dword_18    = 0x00010000,
            dword_1C    = 0x0000000E,
        ),
        ScenaEventData(
            x           = -5120,
            y           = -100,
            z           = -900,
            range       = -1040,
            dword_10    = 0x000003E8,
            dword_14    = 0xFFFFFF9C,
            dword_18    = 0x00010000,
            dword_1C    = 0x0000000F,
        ),
    )

# id: 0x10005 offset: 0x412
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -2020,
            triggerZ            = 0,
            triggerY            = 10280,
            triggerRange        = 400,
            actorX              = -1900,
            actorZ              = 1500,
            actorY              = 11500,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 29950,
            triggerZ            = -200,
            triggerY            = 49030,
            triggerRange        = 500,
            actorX              = 29950,
            actorZ              = 1700,
            actorY              = 49030,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x45A
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_482',
    )

    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x0010, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0012, 0x0080)

    Jump('loc_696')

    def _loc_482(): pass

    label('loc_482')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_634',
    )

    ClearChrFlags(0x000F, 0x0080)
    SetChrFlags(0x0010, 0x0080)

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x40)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_4BD',
    )

    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x000E, -7590, 0, 82320, 188)

    Jump('loc_631')

    def _loc_4BD(): pass

    label('loc_4BD')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5FC',
    )

    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x001A, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    SetChrPos(0x000E, -3880, 0, 83810, 180)
    SetChrPos(0x000B, -430, 0, 80990, 225)
    SetChrPos(0x0014, -2450, 0, 80960, 180)
    SetChrFlags(0x000C, 0x0004)

    If(
        (
            (Expr.Eval, "OP_29(0x006A, 0x01, 0x0010)"),
            Expr.Return,
        ),
        'loc_5A6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_54E',
    )

    ClearChrFlags(0x0015, 0x0080)
    SetChrPos(0x0015, -3320, 0, 9510, 45)

    Jump('loc_56B')

    def _loc_54E(): pass

    label('loc_54E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_56B',
    )

    ClearChrFlags(0x0016, 0x0080)
    SetChrPos(0x0016, -3320, 0, 9510, 45)

    def _loc_56B(): pass

    label('loc_56B')

    ClearChrFlags(0x0017, 0x0080)
    SetChrPos(0x0017, -2620, 0, 8220, 0)
    SetChrPos(0x0014, -7880, 0, 83450, 0)
    SetChrPos(0x000E, -3740, 0, 78670, 0)

    Jump('loc_5F9')

    def _loc_5A6(): pass

    label('loc_5A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_5C6',
    )

    ClearChrFlags(0x0015, 0x0080)
    SetChrPos(0x0015, -2430, 0, 79710, 0)

    Jump('loc_5E3')

    def _loc_5C6(): pass

    label('loc_5C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_5E3',
    )

    ClearChrFlags(0x0016, 0x0080)
    SetChrPos(0x0016, -2430, 0, 79710, 0)

    def _loc_5E3(): pass

    label('loc_5E3')

    ClearChrFlags(0x0017, 0x0080)
    SetChrPos(0x0017, -1300, 0, 78180, 0)
    def _loc_5F9(): pass

    label('loc_5F9')

    Jump('loc_631')

    def _loc_5FC(): pass

    label('loc_5FC')

    ClearChrFlags(0x000E, 0x0080)

    If(
        (
            (Expr.Eval, "OP_29(0x006A, 0x01, 0x4000)"),
            Expr.Return,
        ),
        'loc_620',
    )

    SetChrPos(0x000E, 22470, 0, 76980, 90)

    Jump('loc_631')

    def _loc_620(): pass

    label('loc_620')

    SetChrPos(0x000E, 22470, 0, 76980, 90)

    def _loc_631(): pass

    label('loc_631')

    Jump('loc_696')

    def _loc_634(): pass

    label('loc_634')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_65E',
    )

    SetChrFlags(0x000B, 0x0010)
    ClearChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000D, 0x0010)
    SetChrPos(0x000C, -7340, 0, 81680, 142)

    Jump('loc_696')

    def _loc_65E(): pass

    label('loc_65E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 4, 0x121C)),
            Expr.Return,
        ),
        'loc_672',
    )

    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)

    Jump('loc_696')

    def _loc_672(): pass

    label('loc_672')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_685',
    )

    SetChrFlags(0x000C, 0x0080)

    Jump('loc_696')

    def _loc_685(): pass

    label('loc_685')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_696',
    )

    SetChrFlags(0x000B, 0x0010)
    SetChrFlags(0x000C, 0x0010)

    def _loc_696(): pass

    label('loc_696')

    If(
        (
            (Expr.Eval, "OP_29(0x0066, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_6A5',
    )

    SetChrFlags(0x0010, 0x0080)

    def _loc_6A5(): pass

    label('loc_6A5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 3, 0x1403)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6E2',
    )

    SetChrFlags(0x0009, 0x0004)
    SetChrPos(0x0008, 26640, 200, 48910, 270)
    SetChrPos(0x0009, 29690, 300, 48620, 180)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)

    def _loc_6E2(): pass

    label('loc_6E2')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x72),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_703',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 1, 0x1401)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 3, 0x1403)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_703',
    )

    Event(0, 0x0010)

    def _loc_703(): pass

    label('loc_703')

    Return()

# id: 0x0001 offset: 0x704
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 3, 0x1403)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_713',
    )

    Jump('loc_717')

    def _loc_713(): pass

    label('loc_713')

    OP_64(0x01, 0x0001)

    def _loc_717(): pass

    label('loc_717')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_755',
    )

    OP_72(0x0000, 0x0020)
    OP_72(0x0000, 0x0008)
    OP_72(0x0001, 0x0020)
    OP_72(0x0001, 0x0008)
    OP_72(0x0002, 0x0020)
    OP_72(0x0002, 0x0008)
    OP_72(0x0003, 0x0020)
    OP_72(0x0003, 0x0008)
    OP_72(0x0004, 0x0020)
    OP_72(0x0004, 0x0008)

    def _loc_755(): pass

    label('loc_755')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 3, 0x1403)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_766',
    )

    OP_72(0x000C, 0x0004)

    def _loc_766(): pass

    label('loc_766')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7A1',
    )

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000073, 'loc_794'),
        (0x00000074, 'loc_794'),
        (0x00000075, 'loc_794'),
        (-1, 'loc_7A1'),
    )

    def _loc_794(): pass

    label('loc_794')

    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x001A, 0x0080)

    Jump('loc_7A1')

    def _loc_7A1(): pass

    label('loc_7A1')

    Return()

# id: 0x0002 offset: 0x7A2
@scena.Code('ReInit')
def ReInit():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7C6',
    )

    Call(1, 0x0006)

    Jump('loc_9E7')

    def _loc_7C6(): pass

    label('loc_7C6')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_87C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_818',
    )

    ChrTalk(
        0x00FE,
        (
            '总之我会\n',
            '努力帮忙选举的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '首先从这里开始\n',
            '改变自己。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_879')

    def _loc_818(): pass

    label('loc_818')

    OP_A2(0x0006)

    ChrTalk(
        0x00FE,
        (
            '本来是想找个机会\n',
            '谈谈的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总觉得话太沉重\n',
            '越来越害怕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……自己也觉得丢脸啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_879(): pass

    label('loc_879')

    Jump('loc_9E7')

    def _loc_87C(): pass

    label('loc_87C')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x40)"),
            Expr.Return,
        ),
        'loc_91B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_8CE',
    )

    ChrTalk(
        0x00FE,
        (
            '总之我会\n',
            '努力帮忙选举的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '首先从这里开始\n',
            '改变自己。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_918')

    def _loc_8CE(): pass

    label('loc_8CE')

    OP_A2(0x0006)

    ChrTalk(
        0x00FE,
        (
            '刚才真是不得了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不知到底会变成怎样，\n',
            '说实话真捏了一把汗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_918(): pass

    label('loc_918')

    Jump('loc_9E7')

    def _loc_91B(): pass

    label('loc_91B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_96F',
    )

    ChrTalk(
        0x00FE,
        (
            '总之先打工吧，\n',
            '从帮忙选举开始。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然才刚刚开始，\n',
            '工作还算顺利。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9E7')

    def _loc_96F(): pass

    label('loc_96F')

    OP_A2(0x0006)

    ChrTalk(
        0x00FE,
        (
            '总之先打工吧，\n',
            '从帮忙选举开始。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然才刚刚开始，\n',
            '工作也还算是顺利吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '幸运的是父亲也很忙，\n',
            '没空管我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9E7(): pass

    label('loc_9E7')

    TalkEnd(0x00FE)

    Return()

# id: 0x0003 offset: 0x9EB
@scena.Code('func_03_9EB')
def func_03_9EB():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_A4C',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x1C, 0x21, 0x000000FA, 0x00)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#0280220129V#157F……嗯～……………\n',
            '………呜喵呜喵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x00FE)

    Jump('loc_B09')

    def _loc_A4C(): pass

    label('loc_A4C')

    OP_A2(0x0005)
    OP_62(0x00FE, 0x00000000, 2000, 0x1C, 0x21, 0x000000FA, 0x00)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#0280220130V#157F……嗯～……………\n',
            '…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280220131V抱……住…………\n',
            '是啊………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280220132V…………………………\n',
            '………呜喵呜喵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x00FE)

    def _loc_B09(): pass

    label('loc_B09')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0xB0D
@scena.Code('func_04_B0D')
def func_04_B0D():
    TalkBegin(0x00FE)
    ClearChrFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x12C),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_B32',
    )

    SetChrSubChip(0x00FE, 2)

    Jump('loc_B37')

    def _loc_B32(): pass

    label('loc_B32')

    SetChrSubChip(0x00FE, 1)

    def _loc_B37(): pass

    label('loc_B37')

    OP_8C(0x00FE, 270, 0)
    SetChrFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x024C, 1, 0x1261)),
            Expr.Return,
        ),
        'loc_BA7',
    )

    ChrTalk(
        0x0008,
        (
            '#0270441515V#141F嗯，那就先这样，\n',
            '有什么事再请多关照了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270441519V那么，保重啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_137B')

    def _loc_BA7(): pass

    label('loc_BA7')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x40)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_10C6',
    )

    OP_A2(0x1261)

    ChrTalk(
        0x0008,
        (
            '#0270441504V#143F嗯……？　怎么了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270441505V难道\n',
            '找到犯人了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_E67',
    )

    ChrTalk(
        0x0101,
        (
            '#0010441506V#1015F嗯，说找到\n',
            '也算是找到了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010441507V就结局来说，\n',
            '其实是没有犯人的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0270441508V#142F怎么回事？',
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
            '说明了事件是意外的事故。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#0270441509V#140F……哦～原来如此啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270441510V那确实是没有犯人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441511V#1000F能写成报导吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0270441512V#145F不，没可能吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270441513V没有事件性，\n',
            '就没有在杂志上刊登的意义了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441514V#1007F呜～这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0270441515V#141F嗯，那就先这样，\n',
            '有什么事再请多关照了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270441516V那么，我还得\n',
            '回去写稿子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441517V#1011F啊，嗯……\n',
            '那么，回头见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10C3')

    def _loc_E67(): pass

    label('loc_E67')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_EC4',
    )

    ChrTalk(
        0x0106,
        (
            '#0050441520V#050F啊啊，说找到也算找到了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050441521V但不是你期待的那样哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F1E')

    def _loc_EC4(): pass

    label('loc_EC4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_F1E',
    )

    ChrTalk(
        0x0103,
        (
            '#0030441522V#020F嗯嗯，说找到也算找到了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030441523V但不是你期待的那样哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F1E(): pass

    label('loc_F1E')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '说明了事件的梗概。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#0270441524V#140F……哦～原来如此啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441511V#1000F能写成报导吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0270441526V#145F不，不太可能吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270441527V这个程度的话，\n',
            '就没有在杂志上刊登的意义了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441514V#1007F呜～这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0270441515V#141F嗯，那就先这样，\n',
            '有什么事再请多关照了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270441516V那么，我还得\n',
            '回去写稿子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441531V#1006F嗯，那回头见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10C3(): pass

    label('loc_10C3')

    Jump('loc_137B')

    def _loc_10C6(): pass

    label('loc_10C6')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_1325',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x024C, 0, 0x1260)),
            Expr.Return,
        ),
        'loc_113E',
    )

    ChrTalk(
        0x0008,
        (
            '#0270441532V#140F嗯……？\n',
            '怎么了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270441533V#145F不好意思，让我专心写稿子吧。\n',
            '就快截稿了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1322')

    def _loc_113E(): pass

    label('loc_113E')

    OP_A2(0x1260)

    ChrTalk(
        0x0008,
        (
            '#0270441534V#140F嗯……？\n',
            '还没走吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441535V#1015F嗯，其实\n',
            '又发生了事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0270441536V#142F？？？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270441537V怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441538V#1000F简而言之……',
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
            '向奈尔说明了伤害事件的事。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#0270441539V#140F嗯～原来如此啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441540V#1011F咦？你好像没什么兴趣啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0270441541V#140F啊啊，我觉得还\n',
            '不足以写成报导啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270441542V不过，以防万一\n',
            '解决之后还是告诉我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010441543V#1006F嗯，好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1322(): pass

    label('loc_1322')

    Jump('loc_137B')

    def _loc_1325(): pass

    label('loc_1325')

    ChrTalk(
        0x0008,
        (
            '#0270441544V#141F要是发生什么事件\n',
            '一定要告诉我哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270441545V那么，小心点啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_137B(): pass

    label('loc_137B')

    SetChrSubChip(0x00FE, 0)
    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x1384
@scena.Code('func_05_1384')
def func_05_1384():
    OP_4A(0x000B, 255)
    OP_4A(0x000D, 255)

    ChrTalk(
        0x000D,
        (
            '#0270210762V#140F那么，下一个问题……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270210763V候选人里有\n',
            '旅游推进派对吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270210764V对于旅游业的活性化\n',
            '有怎样的对策？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2870210765V『旅游推进派』\n',
            '这个说法就免了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2870210766V说得好像我只会考虑\n',
            '旅游的事情似的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x000B, 255)
    OP_4B(0x000D, 255)

    Return()

# id: 0x0006 offset: 0x1480
@scena.Code('func_06_1480')
def func_06_1480():
    OP_4A(0x000B, 255)
    OP_4A(0x000C, 255)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1513',
    )

    ChrTalk(
        0x000B,
        (
            '对了，演讲会的地方\n',
            '已经决定了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '嗯嗯，预定在\n',
            '伦格兰德大桥附近。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '因为都是人来人往的地方嘛。\n',
            '一定能聚集很多听众。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15FB')

    def _loc_1513(): pass

    label('loc_1513')

    OP_A2(0x0001)

    ChrTalk(
        0x000C,
        (
            '对了，令郎的情况怎样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '呼，还是老样子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '不知道在怕什么，\n',
            '一直把自己关在房间里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '是吗……真可怜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '这个事\n',
            '我再怎么叹气也没办法啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '说到底\n',
            '还是儿子本人的问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '……还是谈谈工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '啊，是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15FB(): pass

    label('loc_15FB')

    OP_4B(0x000B, 255)
    OP_4B(0x000C, 255)

    Return()

# id: 0x0007 offset: 0x1604
@scena.Code('func_07_1604')
def func_07_1604():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1698',
    )

    OP_4A(0x000B, 255)

    ChrTalk(
        0x000D,
        (
            '#0270201199V#140F不过，诺曼候选人好象\n',
            '把旅游的活性化作为了承诺吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270201200V从市民的眼光来看，\n',
            '这样说也是可以理解的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x000B, 255)

    Jump('loc_16A2')

    def _loc_1698(): pass

    label('loc_1698')

    OP_A2(0x0001)
    OP_A2(0x0004)
    Call(0, 0x0005)

    def _loc_16A2(): pass

    label('loc_16A2')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x16A6
@scena.Code('func_08_16A6')
def func_08_16A6():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_16CA',
    )

    Call(1, 0x000C)

    Jump('loc_1A4C')

    def _loc_16CA(): pass

    label('loc_16CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_1864',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1733',
    )

    ChrTalk(
        0x00FE,
        (
            '我个人也觉得\n',
            '对港湾劳动者考虑不够。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以后为了不产生误解，\n',
            '打算积极与他们对话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1861')

    def _loc_1733(): pass

    label('loc_1733')

    OP_A2(0x0001)

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_17D0',
    )

    ChrTalk(
        0x00FE,
        (
            '哦哦，诸位游击士啊。\n',
            '今天真是表现精彩啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果不是诸位解决了问题，\n',
            '对立可会更加深化了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，以后也要为市民\n',
            '更加努力工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1861')

    def _loc_17D0(): pass

    label('loc_17D0')

    ChrTalk(
        0x00FE,
        (
            '哎呀，诸位游击士啊。\n',
            '之前真是辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总算解决了问题，真是帮大忙了。\n',
            '一时还在担心会怎样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，以后也要为市民\n',
            '更加努力工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1861(): pass

    label('loc_1861')

    Jump('loc_1A4C')

    def _loc_1864(): pass

    label('loc_1864')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_1902',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_18F8',
    )

    OP_4A(0x000D, 255)

    ChrTalk(
        0x00FE,
        (
            '旅游业和海运业\n',
            '原本是一体的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，考虑到将来\n',
            '旅游业的发展是第一大事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也就是说我主张\n',
            '把这个作为支柱产业。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x000D, 255)

    Jump('loc_18FF')

    def _loc_18F8(): pass

    label('loc_18F8')

    OP_A2(0x0001)
    Call(0, 0x0005)

    def _loc_18FF(): pass

    label('loc_18FF')

    Jump('loc_1A4C')

    def _loc_1902(): pass

    label('loc_1902')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1A41',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_199D',
    )

    ChrTalk(
        0x00FE,
        (
            '在港口工作的人的心情\n',
            '并不是不能理解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '前市长时代\n',
            '削减了港湾设施的预算，\n',
            '设备开始老朽化了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '港口的诸位害怕\n',
            '重蹈覆辙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A3E')

    def _loc_199D(): pass

    label('loc_199D')

    OP_A2(0x0001)

    ChrTalk(
        0x00FE,
        (
            '卢安市的未来\n',
            '和旅游业的发展密切相关。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果游客增加了，\n',
            '城市全体的景气就会变好，\n',
            '最后海运业也会繁盛起来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果市民们能更深刻地\n',
            '理解这件事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A3E(): pass

    label('loc_1A3E')

    Jump('loc_1A4C')

    def _loc_1A41(): pass

    label('loc_1A41')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_1A4C',
    )

    Call(0, 0x0006)

    def _loc_1A4C(): pass

    label('loc_1A4C')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x1A50
@scena.Code('func_09_1A50')
def func_09_1A50():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1A71',
    )

    Call(1, 0x000D)

    def _loc_1A71(): pass

    label('loc_1A71')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x1A75
@scena.Code('func_0A_1A75')
def func_0A_1A75():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_1B1A',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_1AD2',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，游击士。\n',
            '刚才真精彩啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没有犯人，\n',
            '说实话真松了一口气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B17')

    def _loc_1AD2(): pass

    label('loc_1AD2')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x40)"),
            Expr.Return,
        ),
        'loc_1B17',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，游击士。\n',
            '刚才辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呜呜，头还阵阵地疼呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B17(): pass

    label('loc_1B17')

    Jump('loc_1C34')

    def _loc_1B1A(): pass

    label('loc_1B1A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_1C29',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1B71',
    )

    ChrTalk(
        0x00FE,
        (
            '骚动的契机\n',
            '只是一点口角而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而转瞬间\n',
            '却引起那样的骚动……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C26')

    def _loc_1B71(): pass

    label('loc_1B71')

    OP_A2(0x0002)

    ChrTalk(
        0x00FE,
        (
            '刚才骚动的契机\n',
            '只是一点口角而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为演讲会的场所问题\n',
            '和波尔多斯阵营发生了点争执。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '相互争执着\n',
            '不知不觉就变成那样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，真是给诺曼先生丢脸，\n',
            '太对不起他了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C26(): pass

    label('loc_1C26')

    Jump('loc_1C34')

    def _loc_1C29(): pass

    label('loc_1C29')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_1C34',
    )

    Call(0, 0x0006)

    def _loc_1C34(): pass

    label('loc_1C34')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x1C38
@scena.Code('func_0B_1C38')
def func_0B_1C38():
    Call(0, 0x000C)

    Return()

# id: 0x000C offset: 0x1C3D
@scena.Code('func_0C_1C3D')
def func_0C_1C3D():
    TalkBegin(0x000A)

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1C5D',
    )

    Jump('loc_1C88')

    def _loc_1C5D(): pass

    label('loc_1C5D')

    Call(6, 0x0006)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1C77',
    )

    OP_0D()
    OP_A9(0x6B)
    OP_56(0x00)
    TalkEnd(0x000A)

    Return()

    def _loc_1C77(): pass

    label('loc_1C77')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1C88',
    )

    TalkEnd(0x000A)

    Return()

    def _loc_1C88(): pass

    label('loc_1C88')

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1CA9',
    )

    Call(1, 0x0009)

    Jump('loc_22E8')

    def _loc_1CA9(): pass

    label('loc_1CA9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_1DC7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D6E',
    )

    ChrTalk(
        0x000A,
        (
            '这家酒店的所有者\n',
            '是新市长诺曼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '前几天碰到他的时候\n',
            '看起来好像相当疲劳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '听说这几天都\n',
            '住在市长官邸里办公呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '市长的工作才刚刚开始。\n',
            '希望他不要勉强就好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_1DC4')

    def _loc_1D6E(): pass

    label('loc_1D6E')

    ChrTalk(
        0x000A,
        (
            '诺曼大人作为市长\n',
            '也在苦思对策的样子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '听说这几天都\n',
            '住在市长官邸里办公呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1DC4(): pass

    label('loc_1DC4')

    Jump('loc_22E8')

    def _loc_1DC7(): pass

    label('loc_1DC7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1EDE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1E69',
    )

    ChrTalk(
        0x000A,
        (
            '虽然照明和热水什么的\n',
            '都准备了代替的手段……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '要维持平常的服务质量，\n',
            '说实话目前相当困难。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '这样的状态\n',
            '到底要持续到什么时候呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_1EDB')

    def _loc_1E69(): pass

    label('loc_1E69')

    ChrTalk(
        0x000A,
        (
            '要维持平常的服务质量，\n',
            '说实话目前相当困难。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我身为这家酒店的代理管理者，\n',
            '无论如何也要想办法保持水准啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1EDB(): pass

    label('loc_1EDB')

    Jump('loc_22E8')

    def _loc_1EDE(): pass

    label('loc_1EDE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_211C',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0069, 0x00, 0x40)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1FF1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1F52',
    )

    ChrTalk(
        0x000A,
        (
            '光临卢安的时候\n',
            '请务必光临本酒店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '老板和工作人员\n',
            '都会衷心等候您的到来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1FEE')

    def _loc_1F52(): pass

    label('loc_1F52')

    OP_A2(0x0000)

    ChrTalk(
        0x000A,
        (
            '各位游击士，\n',
            '今天真是多谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我代表本酒店\n',
            '感谢你们\n',
            '解决了事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '再光临卢安的时候\n',
            '请务必光临本酒店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '老板和工作人员\n',
            '都会衷心等候的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1FEE(): pass

    label('loc_1FEE')

    Jump('loc_2119')

    def _loc_1FF1(): pass

    label('loc_1FF1')

    If(
        (
            (Expr.Eval, "OP_29(0x006A, 0x01, 0x4000)"),
            Expr.Return,
        ),
        'loc_203B',
    )

    ChrTalk(
        0x000A,
        (
            '似乎发生了\n',
            '很严重的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '还请各位……\n',
            '助一臂之力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2119')

    def _loc_203B(): pass

    label('loc_203B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_208E',
    )

    ChrTalk(
        0x000A,
        (
            '刚才诺曼大人\n',
            '向拉旺塔尔\n',
            '下了订单。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '好像是各位\n',
            '活动人员的午饭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2119')

    def _loc_208E(): pass

    label('loc_208E')

    OP_A2(0x0000)

    ChrTalk(
        0x000A,
        (
            '本酒店的客房服务\n',
            '还包括向卢安市内\n',
            '各饮食店下订单。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '可以在房间一边休息并\n',
            '一边享受各处的名产料理，\n',
            '这是我们引以为傲的客户服务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2119(): pass

    label('loc_2119')

    Jump('loc_22E8')

    def _loc_211C(): pass

    label('loc_211C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_2171',
    )

    ChrTalk(
        0x000A,
        (
            '在两阵营之间\n',
            '似乎有纠纷呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '真不希望用暴力,\n',
            '而是用政策来战斗啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_22E8')

    def _loc_2171(): pass

    label('loc_2171')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 4, 0x121C)),
            Expr.Return,
        ),
        'loc_21B3',
    )

    ChrTalk(
        0x000A,
        (
            '哎呀，客人。\n',
            '怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '好像相当\n',
            '慌张的样子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_22E8')

    def _loc_21B3(): pass

    label('loc_21B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_2227',
    )

    ChrTalk(
        0x000A,
        (
            '现在因为在选举期间，\n',
            '所以旅游的客人很少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '客房也有些空下来，\n',
            '可以为各位准备很不错的房间喔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_22E8')

    def _loc_2227(): pass

    label('loc_2227')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_22E8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_228D',
    )

    ChrTalk(
        0x000A,
        (
            '现在总统套房\n',
            '是市长候选人诺曼大人\n',
            '的选举事务所。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '诺曼大人是本酒店\n',
            '的老板。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_22E8')

    def _loc_228D(): pass

    label('loc_228D')

    OP_A2(0x0000)

    ChrTalk(
        0x000A,
        (
            '欢迎光临。\n',
            '欢迎来到布朗西酒店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '本酒店全部房间都能观赏海洋景观，\n',
            '请务必光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_22E8(): pass

    label('loc_22E8')

    TalkEnd(0x000A)

    Return()

# id: 0x000D offset: 0x22EC
@scena.Code('func_0D_22EC')
def func_0D_22EC():
    TalkBegin(0x0013)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_23B2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_236E',
    )

    ChrTalk(
        0x00FE,
        (
            '那些卷着印花头巾的人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看起来像是城里人，\n',
            '会不会是青年团？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，精神十足\n',
            '又清爽的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0011)

    Jump('loc_23AF')

    def _loc_236E(): pass

    label('loc_236E')

    ChrTalk(
        0x00FE,
        (
            '那些卷着印花头巾的人\n',
            '会不会是青年团？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '感觉精神又清爽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_23AF(): pass

    label('loc_23AF')

    Jump('loc_2497')

    def _loc_23B2(): pass

    label('loc_23B2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2497',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2455',
    )

    ChrTalk(
        0x00FE,
        (
            '我是从柏斯\n',
            '过来旅行的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是好像定期船\n',
            '又停运了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '上次来这里的时候，\n',
            '也是哪都不能去啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，我和定期船\n',
            '好像性格不合啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0011)

    Jump('loc_2497')

    def _loc_2455(): pass

    label('loc_2455')

    ChrTalk(
        0x00FE,
        (
            '定期船\n',
            '又停运了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好了，怎么办呢……\n',
            '要延长逗留时间吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2497(): pass

    label('loc_2497')

    TalkEnd(0x0013)

    Return()

# id: 0x000E offset: 0x249B
@scena.Code('func_0E_249B')
def func_0E_249B():
    TalkBegin(0x0011)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_2583',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 2, 0x12)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2536',
    )

    ChrTalk(
        0x00FE,
        (
            '市长身边有同辈的德尔斯\n',
            '留下当秘书……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听服务台的人说，\n',
            '好像相当忙碌的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔，定期船也不会来，\n',
            '可能该回去帮忙吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0012)

    Jump('loc_2580')

    def _loc_2536(): pass

    label('loc_2536')

    ChrTalk(
        0x00FE,
        (
            '诺曼市长的助理\n',
            '是德尔斯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '反正定期船也不会来\n',
            '要不要去帮忙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2580(): pass

    label('loc_2580')

    Jump('loc_26C9')

    def _loc_2583(): pass

    label('loc_2583')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_26C9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 2, 0x12)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2664',
    )

    ChrTalk(
        0x00FE,
        (
            '选举后的杂务也总算结束了，\n',
            '正想返回王都……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '结果那个贝壳一样的物体出现在天空，\n',
            '把导力器都停住了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，但是回王都\n',
            '到底是不能靠步行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要通过漆黑的卡鲁迪亚隧道\n',
            '对我来说是绝对不可能的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0012)

    Jump('loc_26C9')

    def _loc_2664(): pass

    label('loc_2664')

    ChrTalk(
        0x00FE,
        (
            '可是，到底什么时候\n',
            '定期船才会恢复原状呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是会继续延期，\n',
            '回去帮市长的忙\n',
            '可能会比较好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_26C9(): pass

    label('loc_26C9')

    TalkEnd(0x0011)

    Return()

# id: 0x000F offset: 0x26CD
@scena.Code('func_0F_26CD')
def func_0F_26CD():
    TalkBegin(0x0012)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_279E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 3, 0x13)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2727',
    )

    ChrTalk(
        0x00FE,
        (
            '南区的渡口\n',
            '在这边地下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要使用的人\n',
            '请从台阶到地下１层。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0013)

    Jump('loc_279B')

    def _loc_2727(): pass

    label('loc_2727')

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，差不多\n',
            '也习惯礼貌说话了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '开始觉得挺烦的，\n',
            '但现在却觉得很充实。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '能帮别人的忙，\n',
            '心情真是好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A3(0x0013)

    def _loc_279B(): pass

    label('loc_279B')

    Jump('loc_2879')

    def _loc_279E(): pass

    label('loc_279E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2879',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 3, 0x13)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2803',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯～南区的渡口\n',
            '可以从地下１层前往。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要使用的人请、请……\n',
            '请往下边走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0013)

    Jump('loc_2879')

    def _loc_2803(): pass

    label('loc_2803')

    ChrTalk(
        0x00FE,
        (
            '可、可恶。\n',
            '字到嘴边说不出来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要使用的人\n',
            '请．这．边．走……吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好，这样就顺畅了。\n',
            '不会再说错了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A3(0x0013)

    def _loc_2879(): pass

    label('loc_2879')

    TalkEnd(0x0012)

    Return()

# id: 0x0010 offset: 0x287D
@scena.Code('func_10_287D')
def func_10_287D():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_288E',
    )

    Call(0, 0x0015)

    def _loc_288E(): pass

    label('loc_288E')

    EventBegin(0x00)
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x00F7, 0x0080)
    SetChrFlags(0x0105, 0x0080)
    SetChrFlags(0x0104, 0x0080)
    OP_6D(25960, 0, 47550, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2440, 0)
    OP_6C(35000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    OP_0D()
    OP_22(0x0006, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_28FB')
    def lambda_28FB():
        OP_6D(27120, 0, 48140, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_28FB)

    CreateThread(0x0101, 0x01, 0x00, 0x0011)
    Sleep(500)

    CreateThread(0x0104, 0x01, 0x00, 0x0014)
    Sleep(500)

    CreateThread(0x00F7, 0x01, 0x00, 0x0012)
    Sleep(500)

    CreateThread(0x0105, 0x01, 0x00, 0x0013)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010220086V#1001F#6P你们好～',
            TxtCtl.Enter,
            '#1004F唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    SetChrSubChip(0x0008, 1)

    ChrTalk(
        0x0008,
        (
            '#0270220087V#143F#5P是、是你们啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270220088V#141F我听朵洛希说了。\n',
            '幽灵骚动好像解决了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_29F1')
    def lambda_29F1():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_29F1)

    Sleep(50)

    @scena.Lambda('lambda_2A04')
    def lambda_2A04():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_2A04)

    Sleep(50)

    @scena.Lambda('lambda_2A17')
    def lambda_2A17():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_2A17)

    Sleep(50)

    @scena.Lambda('lambda_2A2A')
    def lambda_2A2A():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_2A2A)

    WaitForThreadExit(0x0104, 0x0001)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010220089V#1015F嗯，算是吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220090V朵洛希怎么样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0270220091V#142F#5P报告事件的时候\n',
            '她就一直很困的样子……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270220092V刚一结束就大睡起来，\n',
            '没办法只好抬到床上去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2B61',
    )

    ChrTalk(
        0x0106,
        (
            '#0050220093V#051F#6P不过昨天一直忙到半夜，\n',
            '发生了很多事嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050220094V可能是太累了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2BC0')

    def _loc_2B61(): pass

    label('loc_2B61')

    ChrTalk(
        0x0103,
        (
            '#0030220095V#027F#6P不过昨天一直忙到半夜，\n',
            '她都陪着我们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030220096V会犯困也没办法吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2BC0(): pass

    label('loc_2BC0')

    ChrTalk(
        0x0008,
        (
            '#0270220097V#145F#5P哼，能够持续熬夜\n',
            '才是够格的记者啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270220098V#141F对了，光听这家伙的说明\n',
            '还是有点不是很明白……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270220099V关于此次的事件\n',
            '可以问几个问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220100V#1006F嗯，好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔等人一边回答奈尔的问题\n',
            '一边说明了事件的来龙去脉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0270220101V#145F#5P原来如此，大致明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270220102V#142F话说回来『怪盗Ｂ』\n',
            '竟然来了利贝尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220103V#1004F咦……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220104V#1005F奈尔竟然\n',
            '知道怪盗男！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0270220105V#142F#5P好像是在大陆各地大都市\n',
            '引起骚乱的有名盗贼哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270220106V瞄准了的猎物绝对不会放跑。\n',
            '华丽地偷盗然后离开……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270220107V好像就是个这么做作的盗贼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2E8F',
    )

    ChrTalk(
        0x0106,
        (
            '#0050220108V#555F#6P哼……\n',
            '同一个人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2EC6')

    def _loc_2E8F(): pass

    label('loc_2E8F')

    ChrTalk(
        0x0103,
        (
            '#0030220109V#022F#6P原来如此……\n',
            '像是同一个人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2EC6(): pass

    label('loc_2EC6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2F5F',
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
            TXT(0x00, '【◇完成了烛台失窃事件任务】\n'),
            TXT(0x01, '【◇未完成烛台失窃事件任务】\n'),
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
        (0x00000000, 'loc_2F46'),
        (0x00000001, 'loc_2F4E'),
        (-1, 'loc_2F56'),
    )

    def _loc_2F46(): pass

    label('loc_2F46')

    OP_28(0x0020, 0x03, 0x10)

    Jump('loc_2F56')

    def _loc_2F4E(): pass

    label('loc_2F4E')

    OP_28(0x0020, 0x04, 0x10)

    Jump('loc_2F56')

    def _loc_2F56(): pass

    label('loc_2F56')

    FadeIn(300, 0)

    def _loc_2F5F(): pass

    label('loc_2F5F')

    If(
        (
            (Expr.Eval, "OP_29(0x0020, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_2F9C',
    )

    ChrTalk(
        0x0101,
        (
            '#0010220110V#1007F本人也这么说了，\n',
            '应该没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2F9C(): pass

    label('loc_2F9C')

    ChrTalk(
        0x0008,
        (
            '#0270220111V#145F#5P不过，那个『怪盗Ｂ』\n',
            '竟然是结社的爪牙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270220112V『噬身之蛇』……\n',
            '真是群来路不明的家伙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060220113V#043F#6P那个，奈尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060220114V关于此次的事件\n',
            '打算报导多少呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0270220115V#140F#5P啊，其实协会和王国军\n',
            '拜托我控制\n',
            '关于结社的报导。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270220116V我想应该会写成\n',
            '『恶性愉快犯』所为吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040220117V#035F不过，政变也终结了，\n',
            '国内总算安定了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040220118V#030F考虑到市民的不安，\n',
            '这可说是妥当的判断吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0270220119V#145F#5P作为记者很不甘心，\n',
            '不过这个我也理解。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270220120V#141F不过作为补偿，如果再发生什么事\n',
            '也一定要告诉我们哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220121V#1006F嗯，明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220122V那么，我们\n',
            '就出发去蔡斯了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0270220123V#143F#5P哦哦，是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270220124V我还要写稿子\n',
            '没法去送行……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270220125V不过我去把朵洛希那家伙弄醒吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010220126V#1016F啊，不用了不用了。\n',
            '难得睡得那么香嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010220127V#1011F奈尔帮忙打个招呼吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0270220128V#141F#5P明白了。\n',
            '多加小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0008, 0)
    OP_A2(0x1401)
    EventEnd(0x00)

    Return()

# id: 0x0011 offset: 0x334A
@scena.Code('func_11_334A')
def func_11_334A():
    SetChrPos(0x00FE, 23940, 0, 47510, 90)
    ClearChrFlags(0x00FE, 0x0080)
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)

    @scena.Lambda('lambda_3371')
    def lambda_3371():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3371)

    OP_8E(0x00FE, 27120, 0, 47400, 2000, 0x00)
    OP_8C(0x00FE, 90, 400)

    Return()

# id: 0x0012 offset: 0x3399
@scena.Code('func_12_3399')
def func_12_3399():
    SetChrPos(0x00FE, 23940, 0, 47510, 90)
    ClearChrFlags(0x00FE, 0x0080)
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)

    @scena.Lambda('lambda_33C0')
    def lambda_33C0():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_33C0)

    OP_8E(0x00FE, 26110, 0, 47340, 2000, 0x00)
    OP_8C(0x00FE, 90, 400)

    Return()

# id: 0x0013 offset: 0x33E8
@scena.Code('func_13_33E8')
def func_13_33E8():
    SetChrPos(0x00FE, 23860, 0, 46420, 90)
    ClearChrFlags(0x00FE, 0x0080)
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)

    @scena.Lambda('lambda_340F')
    def lambda_340F():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_340F)

    OP_8E(0x00FE, 25990, 0, 46310, 2000, 0x00)
    OP_8C(0x00FE, 45, 400)

    Return()

# id: 0x0014 offset: 0x3437
@scena.Code('func_14_3437')
def func_14_3437():
    SetChrPos(0x00FE, 23860, 0, 46420, 90)
    ClearChrFlags(0x00FE, 0x0080)
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)

    @scena.Lambda('lambda_345E')
    def lambda_345E():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_345E)

    OP_8E(0x00FE, 27000, 0, 46300, 2000, 0x00)
    OP_8C(0x00FE, 45, 400)

    Return()

# id: 0x0015 offset: 0x3486
@scena.Code('func_15_3486')
def func_15_3486():
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
        (0x00000000, 'loc_3500'),
        (0x00000001, 'loc_3506'),
        (-1, 'loc_350C'),
    )

    def _loc_3500(): pass

    label('loc_3500')

    OP_A2(0x1200)

    Jump('loc_350C')

    def _loc_3506(): pass

    label('loc_3506')

    OP_A2(0x1201)

    Jump('loc_350C')

    def _loc_350C(): pass

    label('loc_350C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_351A',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_351E')

    def _loc_351A(): pass

    label('loc_351A')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_351E(): pass

    label('loc_351E')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

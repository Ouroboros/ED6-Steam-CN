import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4130_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4130   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4130.x'
    header.mapIndex       = 1
    header.bgm            = 14
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/T4130._SN', 'ED6_DT01/T4130_1._SN', 'ED6_DT01/T4130_2._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT07/CH02060._CH', 'ED6_DT07/CH02060P._CP'),
        ('ED6_DT07/CH02070._CH', 'ED6_DT07/CH02070P._CP'),
        ('ED6_DT07/CH01023._CH', 'ED6_DT07/CH01023P._CP'),
        ('ED6_DT07/CH01263._CH', 'ED6_DT07/CH01263P._CP'),
        ('ED6_DT07/CH01623._CH', 'ED6_DT07/CH01623P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01143._CH', 'ED6_DT07/CH01143P._CP'),
        ('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP'),
        ('ED6_DT06/CH20050._CH', 'ED6_DT06/CH20050P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH02480._CH', 'ED6_DT07/CH02480P._CP'),
        ('ED6_DT07/CH02490._CH', 'ED6_DT07/CH02490P._CP'),
        ('ED6_DT07/CH01100._CH', 'ED6_DT07/CH01100P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH01143._CH', 'ED6_DT07/CH01143P._CP'),
        ('ED6_DT07/CH01540._CH', 'ED6_DT07/CH01540P._CP'),
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT07/CH00053._CH', 'ED6_DT07/CH00053P._CP'),
        ('ED6_DT07/CH00063._CH', 'ED6_DT07/CH00063P._CP'),
        ('ED6_DT07/CH02023._CH', 'ED6_DT07/CH02023P._CP'),
        ('ED6_DT06/CH20048._CH', 'ED6_DT06/CH20048P._CP'),
        ('ED6_DT07/CH00003._CH', 'ED6_DT07/CH00003P._CP'),
        ('ED6_DT07/CH00013._CH', 'ED6_DT07/CH00013P._CP'),
        ('ED6_DT07/CH00033._CH', 'ED6_DT07/CH00033P._CP'),
        ('ED6_DT07/CH00073._CH', 'ED6_DT07/CH00073P._CP'),
        ('ED6_DT06/CH20045._CH', 'ED6_DT06/CH20045P._CP'),
        ('ED6_DT06/CH20039._CH', 'ED6_DT06/CH20039P._CP'),
        ('ED6_DT07/CH01490._CH', 'ED6_DT07/CH01490P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01043._CH', 'ED6_DT07/CH01043P._CP'),
        ('ED6_DT07/CH01123._CH', 'ED6_DT07/CH01123P._CP'),
        ('ED6_DT07/CH01260._CH', 'ED6_DT07/CH01260P._CP'),
        ('ED6_DT06/CH20063._CH', 'ED6_DT06/CH20063P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
        ('ED6_DT06/CH20020._CH', 'ED6_DT06/CH20020P._CP'),
    ]

# id: 0x10001 offset: 0x1DA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '奥利维尔',
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
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            name                = '奈尔',
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
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '朵洛希',
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
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '总编',
            x                   = -54100,
            z                   = 200,
            y                   = 61000,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '库拉茨',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x001B,
        ),
        ScenaNpcData(
            name                = '克鲁茨',
            x                   = 5260,
            z                   = 4130,
            y                   = 2290,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x001A,
        ),
        ScenaNpcData(
            name                = '科蕾蒂',
            x                   = 4560,
            z                   = 0,
            y                   = 2500,
            direction           = 186,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0019,
        ),
        ScenaNpcData(
            name                = '彭萨',
            x                   = 4500,
            z                   = 100,
            y                   = -3850,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0155,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0017,
        ),
        ScenaNpcData(
            name                = '金',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0016,
        ),
        ScenaNpcData(
            name                = '奥利维尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x01D6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            name                = '米亚尔',
            x                   = -3600,
            z                   = 0,
            y                   = -2029,
            direction           = 174,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            name                = '戈万',
            x                   = -3520,
            z                   = 0,
            y                   = -4540,
            direction           = 6,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '帕菲',
            x                   = 58600,
            z                   = 0,
            y                   = -1690,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            name                = '娜娜',
            x                   = 59980,
            z                   = 0,
            y                   = -1800,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            name                = '巴拉尔',
            x                   = 61020,
            z                   = 0,
            y                   = 2490,
            direction           = 197,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '科尼嘉',
            x                   = 65830,
            z                   = 0,
            y                   = -3420,
            direction           = 92,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0155,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '诺蒂亚',
            x                   = -57020,
            z                   = 0,
            y                   = 61110,
            direction           = 327,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '法尔茨',
            x                   = -59030,
            z                   = 100,
            y                   = 59540,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '莎莉亚',
            x                   = -56630,
            z                   = 0,
            y                   = 5500,
            direction           = 174,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '士兵丹',
            x                   = 1580,
            z                   = 0,
            y                   = 1800,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '士兵阿尔兹',
            x                   = 2580,
            z                   = 0,
            y                   = 530,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '阿加特',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '提妲',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '拉赛尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x0002,
        ),
        ScenaNpcData(
            name                = '比尔爷爷',
            x                   = 260,
            z                   = 4000,
            y                   = 3770,
            direction           = 215,
            word_0E             = 0,
            dword_10            = 30,
            chipIndex           = 30,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0002,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            name                = '酒杯',
            x                   = -4200,
            z                   = 600,
            y                   = -3000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 327716,
            chipIndex           = 36,
            npcIndex            = 0x01C6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '瓶子',
            x                   = -3600,
            z                   = 700,
            y                   = -3350,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1835045,
            chipIndex           = 37,
            npcIndex            = 0x01C6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '酒杯',
            x                   = -3320,
            z                   = 600,
            y                   = -3880,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 327716,
            chipIndex           = 36,
            npcIndex            = 0x01C6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x55A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x55A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x55A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 4530,
            triggerZ            = 0,
            triggerY            = 590,
            triggerRange        = 400,
            actorX              = 4560,
            actorZ              = 1500,
            actorY              = 2500,
            flags               = 0x007E,
            talkScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0018,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 60700,
            triggerZ            = 0,
            triggerY            = 550,
            triggerRange        = 400,
            actorX              = 61020,
            actorZ              = 1500,
            actorY              = 2490,
            flags               = 0x007E,
            talkScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x000F,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -56840,
            triggerZ            = 0,
            triggerY            = 3500,
            triggerRange        = 400,
            actorX              = -56630,
            actorZ              = 1500,
            actorY              = 5500,
            flags               = 0x007E,
            talkScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 57530,
            triggerZ            = 0,
            triggerY            = 400,
            triggerRange        = 800,
            actorX              = 57290,
            actorZ              = 900,
            actorY              = 340,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000E,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 2480,
            triggerZ            = -250,
            triggerY            = -3810,
            triggerRange        = 800,
            actorX              = 2480,
            actorZ              = 1100,
            actorY              = -3810,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000F,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x60E
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_630',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x48),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x10000000)
    OP_26(233)
    OP_26(137)
    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_06_C34)

    def _loc_630(): pass

    label('loc_630')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_644',
    )

    OP_26(190)
    OP_26(137)
    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, func_08_1CBA)

    def _loc_644(): pass

    label('loc_644')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 4, 0x3FC)),
            Expr.Return,
        ),
        'loc_652',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    Event(0, func_09_3235)

    def _loc_652(): pass

    label('loc_652')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 5, 0x3FD)),
            Expr.Return,
        ),
        'loc_66E',
    )

    MapSetFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007F, 5, 0x3FD))
    Event(0, func_0C_7F6E)

    def _loc_66E(): pass

    label('loc_66E')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000069, 'loc_67A'),
        (-1, 'loc_6A3'),
    )

    def _loc_67A(): pass

    label('loc_67A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 7, 0x627)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_68D',
    )

    SetScenaFlags(ScenaFlag(0x00C4, 7, 0x627))
    Event(0, func_0A_4398)

    def _loc_68D(): pass

    label('loc_68D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 6, 0x64E)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6A0',
    )

    SetScenaFlags(ScenaFlag(0x00C9, 6, 0x64E))
    Event(0, func_0B_6494)

    def _loc_6A0(): pass

    label('loc_6A0')

    Jump('loc_6A3')

    def _loc_6A3(): pass

    label('loc_6A3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 2, 0x64A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6CA',
    )

    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000C, 0x0040)
    ChrSetPos(0x000C, 5780, 0, 600, 0)

    def _loc_6CA(): pass

    label('loc_6CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_789',
    )

    ChrClearFlags(0x001E, 0x0080)
    ChrSetPos(0x001E, 57680, 200, -5000, 90)
    ChrClearFlags(0x001F, 0x0080)
    ChrSetPos(0x001F, 60140, 200, -4890, 270)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, 5240, 4130, -410, 0)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetChipByIndex(0x0010, 27)
    ChrSetFlags(0x0010, 0x0004)
    ChrSetFlags(0x0010, 0x0010)
    ChrSetPos(0x0010, -3800, 200, -2180, 180)
    ChrClearFlags(0x001D, 0x0080)
    ChrSetPos(0x001D, -3590, 200, -4680, 0)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, -55940, 0, 3500, 315)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, -54920, 0, 62590, 135)
    CreateThread(0x0009, 0x00, 0x00, func_02_BB2)

    Jump('loc_B34')

    def _loc_789(): pass

    label('loc_789')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_7E6',
    )

    ChrClearFlags(0x0014, 0x0080)
    ChrSetFlags(0x0014, 0x0010)
    ChrClearFlags(0x0015, 0x0080)
    ChrSetFlags(0x0015, 0x0010)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, -54200, 0, 63010, 194)
    CreateThread(0x000A, 0x00, 0x00, func_02_BB2)
    ChrSetPos(0x0018, -53520, 0, 123230, 98)
    CreateThread(0x0018, 0x00, 0x00, func_02_BB2)
    ChrClearFlags(0x001B, 0x0080)
    ChrClearFlags(0x001C, 0x0080)

    Jump('loc_B34')

    def _loc_7E6(): pass

    label('loc_7E6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_86C',
    )

    ChrClearFlags(0x0014, 0x0080)
    ChrSetFlags(0x0014, 0x0010)
    ChrClearFlags(0x0015, 0x0080)
    ChrSetFlags(0x0015, 0x0010)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, -54200, 0, 63010, 194)
    CreateThread(0x000A, 0x00, 0x00, func_02_BB2)
    ChrSetChipByIndex(0x000C, 34)
    CreateThread(0x000C, 0x00, 0x00, func_02_BB2)
    ChrSetPos(0x0018, -59890, 0, 120300, 180)
    CreateThread(0x0018, 0x00, 0x00, func_02_BB2)
    ChrSetPos(0x0019, -54350, 0, 1120, 265)
    ChrSetChipByIndex(0x0019, 15)
    CreateThread(0x0019, 0x00, 0x00, func_02_BB2)
    ChrClearFlags(0x0019, 0x0004)
    ChrClearFlags(0x0019, 0x0010)

    Jump('loc_B34')

    def _loc_86C(): pass

    label('loc_86C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_914',
    )

    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, 5860, 4100, -4760, 350)
    ChrSetFlags(0x000C, 0x0010)
    ChrClearFlags(0x0012, 0x0080)
    ChrSetPos(0x0012, -3400, 120, -4500, 0)
    ChrSetChipByIndex(0x0012, 32)
    TerminateThread(0x0012, 0x00)
    ChrSetFlags(0x0012, 0x0010)
    ChrSetFlags(0x0012, 0x0004)
    ChrClearFlags(0x0013, 0x0080)
    ChrSetPos(0x0013, -3700, 150, -2180, 180)
    ChrSetChipByIndex(0x0013, 33)
    TerminateThread(0x0013, 0x00)
    ChrSetFlags(0x0013, 0x0010)
    ChrSetFlags(0x0013, 0x0004)
    ChrClearFlags(0x0014, 0x0080)
    ChrSetFlags(0x0014, 0x0010)
    ChrClearFlags(0x0015, 0x0080)
    ChrSetFlags(0x0015, 0x0010)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 62780, 0, -3550, 162)
    CreateThread(0x000A, 0x00, 0x00, func_03_BC8)

    Jump('loc_B34')

    def _loc_914(): pass

    label('loc_914')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_91E',
    )

    Jump('loc_B34')

    def _loc_91E(): pass

    label('loc_91E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_9E7',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetChipByIndex(0x0008, 26)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetFlags(0x0008, 0x0010)
    ChrSetPos(0x0008, -3590, 200, -4680, 0)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetChipByIndex(0x0010, 27)
    ChrSetFlags(0x0010, 0x0004)
    ChrSetFlags(0x0010, 0x0010)
    ChrSetPos(0x0010, -3800, 200, -2180, 180)
    ChrClearFlags(0x0022, 0x0080)
    ChrClearFlags(0x0021, 0x0080)
    ChrClearFlags(0x0023, 0x0080)
    ChrSetPos(0x0019, -54350, 0, 1120, 265)
    ChrSetChipByIndex(0x0019, 15)
    CreateThread(0x0019, 0x00, 0x00, func_02_BB2)
    ChrClearFlags(0x0019, 0x0004)
    ChrClearFlags(0x0019, 0x0010)
    ChrSetPos(0x0018, -60680, 0, 122710, 160)
    CreateThread(0x0018, 0x00, 0x00, func_05_C10)
    ChrSetChipByIndex(0x000B, 31)
    ChrClearFlags(0x000B, 0x0040)
    ChrClearFlags(0x000B, 0x0010)
    ChrSetPos(0x000B, 58490, 0, -630, 0)
    CreateThread(0x000B, 0x01, 0x00, func_02_BB2)

    Jump('loc_B34')

    def _loc_9E7(): pass

    label('loc_9E7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_9F1',
    )

    Jump('loc_B34')

    def _loc_9F1(): pass

    label('loc_9F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_A71',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetChipByIndex(0x0008, 26)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetFlags(0x0008, 0x0010)
    ChrSetPos(0x0008, -3590, 200, -4680, 0)
    ChrClearFlags(0x0010, 0x0080)
    ChrSetChipByIndex(0x0010, 27)
    ChrSetFlags(0x0010, 0x0004)
    ChrSetFlags(0x0010, 0x0010)
    ChrSetPos(0x0010, -3800, 200, -2180, 180)
    ChrClearFlags(0x0022, 0x0080)
    ChrClearFlags(0x0021, 0x0080)
    ChrClearFlags(0x0023, 0x0080)
    ChrSetPos(0x0018, -63230, 0, 59560, 338)
    CreateThread(0x0018, 0x00, 0x00, func_02_BB2)
    ChrSetFlags(0x0019, 0x0080)

    Jump('loc_B34')

    def _loc_A71(): pass

    label('loc_A71')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_A7B',
    )

    Jump('loc_B34')

    def _loc_A7B(): pass

    label('loc_A7B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_B15',
    )

    ChrClearFlags(0x0020, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 3, 0x613)),
            Expr.Return,
        ),
        'loc_B12',
    )

    ChrSetPos(0x0008, 1490, 0, -3580, 225)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetFlags(0x0008, 0x0008)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0011, 0x0040)
    ChrSetPos(0x0011, 980, 0, -2990, 180)
    ChrSetPos(0x000E, 1410, -250, -4260, 8)
    ChrSetFlags(0x000E, 0x0010)
    ChrSetPos(0x0020, 1620, 0, -2610, 180)
    ChrSetChipByIndex(0x000F, 15)
    ChrClearFlags(0x000F, 0x0040)
    ChrClearFlags(0x000F, 0x0010)
    ChrSetPos(0x000F, 4059, 0, -2910, 215)
    CreateThread(0x000F, 0x01, 0x00, func_02_BB2)

    def _loc_B12(): pass

    label('loc_B12')

    Jump('loc_B34')

    def _loc_B15(): pass

    label('loc_B15')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_B34',
    )

    ChrSetPos(0x0018, -59890, 0, 120300, 180)
    CreateThread(0x0018, 0x00, 0x00, func_02_BB2)

    def _loc_B34(): pass

    label('loc_B34')

    Return()

# id: 0x0001 offset: 0xB35
@scena.Code('func_01_B35')
def func_01_B35():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 1, 0x631)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 3, 0x623)),
            Expr.Or,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 3, 0x61B)),
            Expr.Or,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 6, 0x616)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_B68',
    )

    OP_B1('t4130_y')

    Jump('loc_B71')

    def _loc_B68(): pass

    label('loc_B68')

    OP_B1('t4130_n')

    def _loc_B71(): pass

    label('loc_B71')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 2, 0x66A)),
            Expr.Return,
        ),
        'loc_B81',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x4B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_B81(): pass

    label('loc_B81')

    OP_72(0x0005, 0x0020)
    OP_72(0x0006, 0x0020)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_B95',
    )

    Jump('loc_BB1')

    def _loc_B95(): pass

    label('loc_B95')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_BAA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 3, 0x613)),
            Expr.Return,
        ),
        'loc_BA7',
    )

    OP_64(0x00, 0x0001)

    def _loc_BA7(): pass

    label('loc_BA7')

    Jump('loc_BB1')

    def _loc_BAA(): pass

    label('loc_BAA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_BB1',
    )

    def _loc_BB1(): pass

    label('loc_BB1')

    Return()

# id: 0x0002 offset: 0xBB2
@scena.Code('func_02_BB2')
def func_02_BB2():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_BC7',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_BB2')

    def _loc_BC7(): pass

    label('loc_BC7')

    Return()

# id: 0x0003 offset: 0xBC8
@scena.Code('func_03_BC8')
def func_03_BC8():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_BEB',
    )

    OP_8D(0x00FE, 61240, -1420, 64280, -5700, 2500)

    Jump('func_03_BC8')

    def _loc_BEB(): pass

    label('loc_BEB')

    Return()

# id: 0x0004 offset: 0xBEC
@scena.Code('func_04_BEC')
def func_04_BEC():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_C0F',
    )

    OP_8D(0x00FE, -57970, 64269, -56460, 57520, 3000)

    Jump('func_04_BEC')

    def _loc_C0F(): pass

    label('loc_C0F')

    Return()

# id: 0x0005 offset: 0xC10
@scena.Code('func_05_C10')
def func_05_C10():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_C33',
    )

    OP_8D(0x00FE, -62670, 124500, -59560, 120770, 3000)

    Jump('func_05_C10')

    def _loc_C33(): pass

    label('loc_C33')

    Return()

# id: 0x0006 offset: 0xC34
@scena.Code('func_06_C34')
def func_06_C34():
    MapClearFlags(0x10000000)
    EventBegin(0x00)
    CameraMove(9550, 0, 2380, 0)
    OP_67(0, 10810, -10950, 0)
    CameraSetDistance(3040, 0)
    OP_6C(44000, 0)
    OP_6E(280, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, -2570, 200, 1820, 90)
    ChrSetPos(0x0101, 420, -250, -4920, 0)
    ChrSetPos(0x0102, 1640, -250, -4860, 0)
    ChrTurnDirection(0x000E, 0x0008, 0)
    ChrSetChipByIndex(0x0008, 23)
    ChrSetFlags(0x0008, 0x0002)
    CreateThread(0x0008, 0x01, 0x00, func_07_1C9A)
    OP_1F(0x64, 0x0000012C)
    ChrSetFlags(0x0008, 0x0004)
    FadeIn(1500, 0)
    CameraMove(560, 0, 1680, 5000)
    Fade(1500)
    CameraMove(1580, 3350, 420, 0)
    OP_67(0, 4250, -10000, 0)
    CameraSetDistance(1430, 0)
    OP_6C(32000, 0)
    OP_6E(613, 0)
    CameraMove(1410, 0, 120, 3000)

    ChrTalk(
        0x0101,
        (
            '#0010101261V#007F#2P（果然是大赖皮蛋奥利维尔啊。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101262V#006F（不过，本来以为演奏家什么的\n',
            '　只是他自称的而已……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101263V#019F#2P（听起来水平相当的高啊。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101264V（自称职业演奏家这点应该是没错的吧。）\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101265V#008F#2P（嗯……\n',
            '　我听得有点入迷了呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CameraMove(-140, 0, 2720, 2500)
    Sleep(2500)

    OP_20(0x000007D0)
    OP_21()
    SetScenaFlags(ScenaFlag(0x0003, 0, 0x18))
    Sleep(1000)

    PlaySE(233, 0x00, 0x64)
    Sleep(1500)

    Fade(1000)
    ChrSetFlags(0x0008, 0x0020)

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TerminateThread(0x0008, 0x01)
    ChrSetChipByIndex(0x0008, 26)
    ChrClearFlags(0x0008, 0x0002)
    ChrTurnDirection(0x0008, 0x0101, 0)
    OP_0D()
    PlayBGM(14)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#0040101266V#035F#5P……刚才的曲子是『琥珀之爱』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040101267V本来这是只能用于歌剧的间奏曲……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040101268V#030F在此借用这首曲子，献上爱与真心的演奏， ',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040101269V以把我无尽的爱，\n',
            '毫无保留地赠与你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0FA2')
    def lambda_0FA2():
        CameraMove(-1740, 0, 1730, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0FA2)

    @scena.Lambda('lambda_0FBA')
    def lambda_0FBA():
        ChrWalkTo(0x00FE, -980, 0, -1570, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0FBA)

    Sleep(500)

    @scena.Lambda('lambda_0FDA')
    def lambda_0FDA():
        ChrWalkTo(0x00FE, -1480, 0, -230, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0FDA)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_0FFA')
    def lambda_0FFA():
        ChrWalkTo(0x00FE, -2460, 0, -220, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0FFA)

    WaitForThreadExit(0x0101, 0x0001)
    ChrTurnDirection(0x0101, 0x0008, 400)
    WaitForThreadExit(0x0102, 0x0001)
    ChrTurnDirection(0x0102, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010101270V#509F看来你还是老样子，\n',
            '总是喜欢在别人面前自我陶醉……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101271V#007F唉……\n',
            '本来很想感动一番的，气氛都被破坏了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101272V#010F很久不见了，奥利维尔。\n',
            '原来你也来王都了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0040101273V#031F当然，正如落入河中的人鱼眼泪\n',
            '终究会到达大海一样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040101274V本人是为了与黑发王子再次感人地相逢\n',
            '而千里迢迢从洛连特来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(137, 0x00, 0x64)
    OP_62(0x0008, 0x0000012C, 1300, 0x36, 0x39, 0x000000FA, 0x00)
    Sleep(1200)

    OP_62(0x0102, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020101275V#018F……真是一点也没变啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101276V#509F啊～好了好了。\n',
            '开玩笑也应该开够了吧。\n',
            '还不赶找个位置招待我们坐下？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101277V就会装模作样，\n',
            '一点也不会看人脸色。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x0008)
    OP_62(0x0008, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0040101278V#034F艾丝蒂尔君……\n',
            '不觉得这样说太过分了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    FadeOut(1000, 0, -1)
    OP_0D()
    ChrSetFlags(0x0101, 0x0004)
    ChrSetFlags(0x0102, 0x0004)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetChipByIndex(0x0101, 24)
    ChrSetChipByIndex(0x0102, 25)
    ChrSetPos(0x0008, -3600, 200, -2200, 180)
    ChrSetPos(0x0101, -3590, 200, -4680, 0)
    ChrSetPos(0x0102, -4940, 200, -4690, 0)
    CameraMove(-3340, 0, -3050, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    PlaySE(234, 0x00, 0x64)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010101279V#006F喂喂，我记得你不是\n',
            '和雪拉姐一起到洛连特去了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101280V什么时候来王都的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0040101281V#030F嗯……大概是一个月之前吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040101282V和你们分别之后，\n',
            '我与雪拉君在洛连特那里\n',
            '度过了一段既美好又快活的时光。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040101283V#034F可是……\n',
            '我到底是个漂泊的诗人兼演奏家……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040101284V最终还是狠心拒绝了雪拉君含泪的挽留，\n',
            '漂流到这美丽的王都来了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101285V#019F该怎么说呢……\n',
            '真是让人无法相信的解释啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101286V#507F肯定是每天晚上被雪拉姐强迫灌酒，\n',
            '结果实在忍受不了而逃出来了吧？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    OP_9E(0x0008, 15, 0, 300, 4000)

    ChrTalk(
        0x0008,
        (
            '#0040101287V#033F呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101288V#001F难道说……\n',
            '是和爱娜姐姐一起喝酒吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    ChrTalk(
        0x0101,
        (
            '#0010101289V#505F对了，\n',
            '奥利维尔还不认识爱娜姐姐吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101290V她是雪拉姐的朋友，\n',
            '洛连特支部的负责人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101291V据说她的酒量比雪拉姐还要高……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x0008)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#0040101292V#031F……哈哈哈，\n',
            '真讨厌啊，艾丝蒂尔君。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040101293V叫·这个·名字的人·\n',
            '我·没有·见过，也·没有·听说过哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101294V#509F你的声音完全把你给出卖了呢……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101295V#013F艾丝蒂尔……\n',
            '就这样放过他吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101296V#015F我想他一定是遇到了悲惨……\n',
            '不，应该是非常悲惨的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0040101297V#034F呜呜，没想到还有比雪拉君酒量更高的，\n',
            '简直是无底洞……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040101298V……啊啊啊…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#0040101299V#036F#3S不～要～再带着那迷人的微笑\n',
            '给我灌酒啦～！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101300V#004F回、回忆重现！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101301V#019F着实沉醉于爱娜小姐的最强传说中呢……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0040101302V#034F呼呼呼……\n',
            '唉，这个就先别提了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040101303V#030F你们两个不是走遍其他地方，\n',
            '然后来到王都了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040101304V都遇到过什么有趣的事情？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101305V#506F嗯，这可是短时间内\n',
            '没办法说清楚的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101306V#000F而且我们现在正在找人，\n',
            '下次见面的时候再说好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0040101307V#033F哎……\n',
            '你们是在找谁啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101308V#010F一位名叫『金』的从卡尔瓦德共和国来的\n',
            '武术家游击士。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101309V据说他经常来酒廊，\n',
            '奥利维尔，你有没有见过呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0040101310V#030F啊啊！\n',
            '那个像熊一样高大的老兄啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040101311V以前见过很多次，\n',
            '不过今天还没有看见他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101312V#007F是吗……\n',
            '今天没有来酒馆吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 2, 0x612)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C08',
    )

    ChrTalk(
        0x0102,
        (
            '#0020101313V#010F那么，\n',
            '在共和国大使馆那边的可能性就很高了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0040101314V#035F呵呵……\n',
            '那我们赶快去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C7A')

    def _loc_1C08(): pass

    label('loc_1C08')

    ChrTalk(
        0x0102,
        (
            '#0020101315V#010F那么，\n',
            '在艾尔贝周游道那边的可能性就很高了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0040101316V#035F呵呵……\n',
            '那我们赶快去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C7A(): pass

    label('loc_1C7A')

    SetScenaFlags(ScenaFlag(0x00C2, 3, 0x613))
    OP_28(0x0046, 0x01, 0x0004)
    FadeIn(1000, 0)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T4100._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0007 offset: 0x1C9A
@scena.Code('func_07_1C9A')
def func_07_1C9A():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0003, 0, 0x18)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1CAF',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)
    Yield()

    Jump('func_07_1C9A')

    def _loc_1CAF(): pass

    label('loc_1CAF')

    Sleep(50)

    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x0008 offset: 0x1CBA
@scena.Code('func_08_1CBA')
def func_08_1CBA():
    EventBegin(0x00)
    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0020, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0008, 0x0008)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetFlags(0x0102, 0x0004)
    ChrSetFlags(0x0108, 0x0004)
    ChrSetPos(0x0108, -3800, 0, -2180, 180)
    ChrSetPos(0x0101, -3590, 200, -4680, 0)
    ChrSetPos(0x0102, -4940, 200, -4690, 0)
    ChrSetPos(0x0008, -4500, 2000, 4700, 225)
    ChrSetChipByIndex(0x0008, 28)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x000E, 4620, 0, 2500, 180)
    CameraMove(-3340, 0, -3050, 0)
    PlaySE(234, 0x00, 0x64)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetFlags(0x0102, 0x0004)
    ChrSetFlags(0x0108, 0x0004)
    ChrSetChipByIndex(0x0101, 24)
    ChrSetChipByIndex(0x0102, 25)
    ChrSetChipByIndex(0x0108, 27)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0108,
        (
            '#0080101493V#070F……原来如此，是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080101494V我问你们一件事，\n',
            '为什么要参加武术大会呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101495V#506F嗯……看过预选赛之后，\n',
            '觉得自己身体已经按耐不住了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101496V所以情不自禁地想要\n',
            '和强大的对手大战一场呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101497V#010F我们现在以成为正游击士为目标\n',
            '在王国各地修炼旅行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101498V所以想借此机会\n',
            '测试一下至今为止的修行成果。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080101499V#074F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080101500V#070F可以啊。我们一起组队吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080101501V在明天大会开始之前，\n',
            '去竞技场的售票处报名就没问题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101502V#001F太好了～㈱',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101503V#004F……嗯，\n',
            '这么痛快地就答应，没关系吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080101504V#071F你们俩的实力，我之前已见识过了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080101505V作为协助我的人已经足够了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101506V#008F嘿嘿……\n',
            '谢谢，金先生！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101507V我会全力以赴的！  ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101508V#010F请多指教。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080101509V#070F彼此彼此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080101510V#074F不过，本来是打算挑战一下，\n',
            '只靠一个人能够到达什么程度的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080101511V现在既然有了协助的人，\n',
            '那就不能不想到要拿冠军了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101512V#006F那当然了！\n',
            '既然参加就要拿冠军！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101513V#013F不过，如果这样打算的话，\n',
            '还缺少一个人的我们还是很难办到的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101514V团体赛的人数是四个啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101515V#505F啊，是啊……\n',
            '还缺少一个人呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101516V#001F不管怎么样，\n',
            '只要鼓足干劲全力以赴就行了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080101517V#072F不，如果目标提高的话，\n',
            '就要做好万全的准备。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080101518V作战在拳脚相加之前就应该开始了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101519V#007F嗯……确实是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101520V这个时候，\n',
            '如果雪拉姐在就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0101, 1)

    ChrTalk(
        0x0101,
        (
            '#0010101521V#006F对了，不如我们去拜托艾南哥哥\n',
            '联络一下洛连特支部吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0102, 2)

    ChrTalk(
        0x0102,
        (
            '#0020101522V#017F嗯……\n',
            '但是雪拉姐姐一定会很忙的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101523V父亲和我们都不在，\n',
            '洛连特支部正人手不足呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101524V#509F是……是这样没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101525V#504F啊～真是的，不管是谁都好，\n',
            '有没有能帮我们的人啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_1F(0x46, 0x00000190)
    Sleep(400)

    PlaySE(190, 0x00, 0x64)
    Sleep(2000)

    NpcTalk(
        0x0008,
        '青年的声音',
        (
            '#0040101526V#4P呵呵……\n',
            '我就是在等这句话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_1F(0x64, 0x00000190)
    OP_62(0x0101, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x0102, 0)
    ChrSetSubChip(0x0108, 2)
    OP_66(0x0000)
    CameraMove(-2690, 0, 2590, 2500)

    ChrTalk(
        0x0101,
        (
            '#0010101527V#509F果然出现了～\n',
            '这个不要脸的赖皮演奏家。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101528V不会一直在二楼潜伏着吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101529V#010F难道……\n',
            '刚才的话你都听见了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    ChrSetFlags(0x0008, 0x0002)
    ChrSetChipByIndex(0x0008, 29)
    ChrSetSubChip(0x0008, 0)
    OP_0D()
    OP_99(0x0008, 0x00, 0x03, 2000)
    Sleep(200)

    OP_99(0x0008, 0x03, 0x0A, 1500)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#0040101530V#035F哈·哈·哈……\n',
            '一字不漏地全都听见了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040101531V于是我就想『这次轮到我出场了』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0008, 0x0002)
    ChrSetChipByIndex(0x0008, 0)
    ChrSetSubChip(0x0008, 0)

    @scena.Lambda('lambda_2660')
    def lambda_2660():
        CameraMove(-4170, 0, -2650, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2660)

    ChrWalkTo(0x0008, -4820, 0, 990, 3000, 0x00)
    ChrSetFlags(0x0008, 0x0004)
    ChrWalkTo(0x0008, -5700, 0, -1750, 3000, 0x00)
    ChrSetChipByIndex(0x0008, 26)
    ChrJumpTo(0x0008, -5020, 200, -2270, 600, 5000)
    PlaySE(209, 0x00, 0x64)
    OP_7C(0, 200, 3000, 100)

    ChrTalk(
        0x0101,
        (
            '#0010101532V#009F喂，等一下！\n',
            '怎么这么随便就坐下来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080101533V#073F这不是弹钢琴的那个演奏家小哥嘛。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080101534V是你们的熟人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101535V#007F该说是熟人呢，还是缘分的捉弄呢……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101536V#019F……还没有达到熟人这种程度吧？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0008, 1)

    ChrTalk(
        0x0008,
        (
            '#0040101537V#030F本人是奥利维尔·朗海姆。\n',
            '来自埃雷波尼亚的旅行演奏家。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040101538V和艾丝蒂尔君、约修亚君\n',
            '是在之前的事件中认识的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040101539V#031F自那以后，我们的关系变得很不一般呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101540V#582F请不要使用容易引起误会的方式说话！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080101541V#070F嗯，虽然不知道是怎么回事，\n',
            '不过我也来报个名字吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080101542V金·瓦赛克——\n',
            '来自卡尔瓦德共和国的游击士，\n',
            '以武侠之道为志向的武术家。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080101543V你的钢琴演奏我一直很欣赏呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0040101544V#035F呵呵……\n',
            '能得到夸奖真是光荣至极。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040101545V#030F本人也听说了，\n',
            '你在武术大会预选赛中的武勇事迹。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040101546V面对四个对手，\n',
            '只凭借一个人就获得压倒性胜利对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080101547V#070F遇到新手作为对手，只是运气好罢了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080101548V对了，不知道这位演奏家先生\n',
            '找我们到底有什么事情呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101549V#005F#3S给我等一下～～！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101550V#010F奥利维尔……\n',
            '我想确认一件事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101551V难道最近你没有事情可做吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0008, 0)

    ChrTalk(
        0x0008,
        (
            '#0040101552V#033F不愧是约修亚君，\n',
            '这个问题还真是尖锐啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040101553V#034F来到王都的这一个月……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040101554V观光游览一遍之后，\n',
            '只剩王城因为有士兵把守而无法进入。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040101555V本想去别的地方看看，\n',
            '可女王的诞辰庆典又快要到了，\n',
            '现在还舍不得离开这个美丽的王都……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101556V#509F总之，就是很闲是吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0040101557V#030F不过嘛，然后突然听到了\n',
            '你们『缺少一个队员』的谈话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040101558V而且最重要的是，\n',
            '优胜者会得到豪华晚宴的款待……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040101559V#031F简直是女神的启示！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101560V#007F呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101561V#017F我就知道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0040101562V#030F就是这个原因，\n',
            '能不能让我也成为参加武术大会的伙伴呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080101563V#070F为什么不呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1700, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010101564V#009F等、等一下金先生。\n',
            '这么简单就让这家伙……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010101565V你还不知道奥利维尔的战斗方法吧？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080101566V#070F他擅长的是导力枪对吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080101567V这样可以采取广泛的战术，\n',
            '我觉得能组成很好的队伍呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0008, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetSubChip(0x0008, 1)

    ChrTalk(
        0x0101,
        (
            '#0010101568V#004F哎～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0040101569V#033F这真是……让人吃惊啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040101570V请问你是不是从腰间的鼓起\n',
            '和走路的方式判断出来的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080101571V#070F还有视线移动的方式。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080101572V武术家和剑士捕捉移动的目标时\n',
            '视线是沿着线移动的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080101573V而你对别人行动的把握\n',
            '都是集中在一个一个点上的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080101574V这是使枪的人移动视线的特殊之处。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101575V#506F嘿哎，真是专业啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101576V#014F原来如此……\n',
            '确实非常有道理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0040101577V#035F嗯……\n',
            '今后我要注意一点了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040101578V#030F那么，在你这位高手的眼光看来，\n',
            '我已经算合格了对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080101579V#071F啊，请多关照啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010101580V#505F嗯～\n',
            '虽然感觉有点不安……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020101581V#010F总之比赛时候请多多指教了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_21()
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T4150._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0009 offset: 0x3235
@scena.Code('func_09_3235')
def func_09_3235():
    EventBegin(0x00)
    CameraMove(59950, 0, -3760, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ChrSetPos(0x0009, 59950, 0, -5070, 270)
    ChrSetPos(0x0101, 58770, 0, -3810, 180)
    ChrSetPos(0x0102, 58750, 0, -5890, 0)
    ChrClearFlags(0x0009, 0x0080)

    ChrTalk(
        0x0101,
        (
            '#000F哈～虽然有点辣，\n',
            '不过很好吃呢㈱',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '香脆的里脊肉\n',
            '和松软的蒸土豆，\n',
            '真的是绝配呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F饭后的咖啡也是一级棒呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '虽然听说过用玻璃器具泡咖啡\n',
            '有相当的难度……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#140F真是的，花别人的钱，\n',
            '就可以这么狼吞虎咽的吃……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110527V以为记者那点可怜的工资能干什么啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F好啦好啦。\n',
            '总之谢谢你招待我们啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '对了……\n',
            '你果然在为新闻素材伤脑筋吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#140F哼……\n',
            '新闻素材要多少有多少。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过，都是些关于亲卫队的恐怖活动、\n',
            '女王身体欠佳之类的，\n',
            '没有什么可信度的消息。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110532V明确地说，\n',
            '我想要的是没有经过军队过滤的，\n',
            '新鲜的情报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270110535V#140F我从朵洛希那里听说了一些\n',
            '关于蔡斯发生的绑架事件的消息……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110536V就开门见山地说吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110537V你们对理查德上校\n',
            '到底调查到什么程度了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F……该怎么说呢，真是一针见血啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F能提出这样的问题，\n',
            '应该已经有所推测了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#140F果然上校就是幕后黑手啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110541V我们杂志还因采访过他\n',
            '而人气大大增长呢，\n',
            '真是不想接受这个现实啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '反叛者马上就要有所行动了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F现在是否对女王陛下\n',
            '有反叛企图，我们还不知道。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '但是，他们把杜南公爵作为傀儡，\n',
            '在暗地企图什么是可以肯定的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#140F杜南公爵吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '趁着陛下身体欠佳，\n',
            '把自己当成格兰赛尔城的主人，\n',
            '肆意妄为……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110547V不可思议的是，\n',
            '军队的高官为什么听之任之呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F唉，那个是因为……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '……喂，约修亚。\n',
            '这个可以说出来吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F是呀……\n',
            '我们也要尽可能地\n',
            '收集相关的情报啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '如果是奈尔先生的话，\n',
            '一定能帮助我们的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#140F喂喂，怎么了。\n',
            '你们果然知道些什么吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F我事先说好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110554V接下来要说的事情，\n',
            '是不能作为报道写出来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F也就是说，先要做好心理准备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#140F可恶……\n',
            '这不是很糟糕的事情吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110557V算了，赶快说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    FadeIn(2000, 0)

    ChrTalk(
        0x0009,
        (
            '#140F………………………………\n',
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊～\n',
            '所以我说要做好心理准备嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#140F这怎么可能……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '喂……这是千真万确的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F虽然很遗憾，不过事实就是这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '空贼事件、孤儿院纵火事件，\n',
            '都是特务兵在背后操纵……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '绑架并且监禁王国第一的\n',
            '天才科学家拉赛尔博士……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '军队上层被抓住了弱点，\n',
            '摩尔根将军也被监禁……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '自导自演的恐怖事件，\n',
            '并且伪装成亲卫队所为……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#140F啊啊～真是的！\n',
            '怎么又是这样！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '可恶……\n',
            '这怎么能写成报道呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110569V最近我们杂志，\n',
            '也要受军队的检查……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '印刷的时候肯定会被拦下来的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F是、是这样吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#140F没办法，\n',
            '只好勉强报道一下\n',
            '没什么关系的武术大会了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '……啊，对了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110574V你们会参加武术大会，\n',
            '也是有什么理由的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110576V虽然和委托的内容有关，\n',
            '不能告诉你详细情况……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F知道是为了打开目前的局面\n',
            '所采取的行动就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#140F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110580V……好，我决定了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '虽然作为记者不能够做什么……\n',
            '不过，我也来帮你们忙吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '游击士协会调查不到的事情，\n',
            '就由我通过私人的途径来调查吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000FＴｈａｎｋ　ｙｏｕ，真是帮大忙了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F对手可是军队啊，\n',
            '这件事情太危险了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110585V即使这样，你也愿意帮忙吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#140F真啰嗦，这是我的战斗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110587V作为记者，\n',
            '我怎么能眼睁睁地看着笔输给剑呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F奈尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F我明白了……\n',
            '无论如何拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#140F哦，就交给我吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110591V那么，具体地来说\n',
            '你们想知道什么事情呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F这个嘛……\n',
            '应该是军队的动向吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '难道他们已经\n',
            '是不是都被逮捕了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110594V摩尔根将军\n',
            '被囚禁在哪里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#140F知道了，\n',
            '我会多加注意的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110596V只是调查这些事情……\n',
            ' ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F……那个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110598V情报部成员的经历，\n',
            '能调查一下吗？',
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
        0x0009,
        (
            '#140F经历吗……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F说具体一点，就是作为核心的\n',
            '理查德上校、凯诺娜上尉，\n',
            '以及洛伦斯少尉这三个人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110602V因为以后要和他们对决，\n',
            '所以想知道他们的一些详细经历……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#140F你的意思是，\n',
            '『知己知彼，百战不殆』吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F没错，除了上校，\n',
            '那个少尉的事情也想知道得更多一些。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '明天或者后天的比赛中\n',
            '说不定会和他们遭遇……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F奈尔先生，这件事拜托你行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#140F……我在军队里认识不少人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110608V机密情报先不说，\n',
            '如果是单纯的简历的话，\n',
            '说不定能弄到手。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '好吧，我就试试看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000FＴｈａｎｋ　ｙｏｕ，真是太感谢了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110611V#010F请多指教。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#140F哎呀，没什么大不了的啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110613V不过相对的，你们如果取得优胜，\n',
            '被招待进格兰赛尔城的话，\n',
            '一定要把事情都告诉我哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F果然是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110615V#010F明白了。\n',
            '只要是能说出来的都会告诉你的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '和奈尔道别之后，\n',
            '艾丝蒂尔他们\n',
            '回到了旅馆自己的房间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '因为比赛的紧张和疲劳，\n',
            '两个人早早地就休息了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '然后，第二天早晨——',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T4132._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000A offset: 0x4398
@scena.Code('func_0A_4398')
def func_0A_4398():
    EventBegin(0x00)
    CameraMove(-60260, 0, 66930, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ChrSetPos(0x0009, -56660, 0, 64750, 0)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0101, -61900, 0, 67420, 135)
    ChrSetPos(0x0102, -63460, 0, 66810, 135)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010110949V#006F喂～奈尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4440')
    def lambda_4440():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_4440)

    ChrTalk(
        0x0102,
        (
            '#0020110950V#010F打扰了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270110951V#141F……哦哦，终于来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110952V朵洛希那家伙，\n',
            '传话难得能成功一次呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_44CB')
    def lambda_44CB():
        CameraMove(-57890, 0, 65099, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_44CB)

    @scena.Lambda('lambda_44E3')
    def lambda_44E3():
        CameraSetDistance(2600, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_44E3)

    @scena.Lambda('lambda_44F3')
    def lambda_44F3():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_44F3')

    DispatchAsync2(0x0101, 0x0001, lambda_44F3)

    @scena.Lambda('lambda_4504')
    def lambda_4504():
        ChrWalkTo(0x00FE, -59150, 0, 64660, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4504)

    ChrWalkTo(0x0102, -60560, 0, 66670, 3000, 0x00)

    @scena.Lambda('lambda_4533')
    def lambda_4533():
        ChrWalkTo(0x00FE, -57490, 0, 64410, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_4533)

    ChrWalkTo(0x0102, -60490, 0, 64560, 3000, 0x00)
    ChrWalkTo(0x0102, -58840, 0, 63880, 3000, 0x00)
    ChrTurnDirection(0x0102, 0x0009, 400)

    ChrTalk(
        0x0009,
        (
            '#0270110953V#141F对了，今天你们也赢了吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110954V朵洛希那家伙，\n',
            '回来的时候兴高采烈的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110955V#502F嘿嘿，是吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110956V#012F那么奈尔先生，\n',
            '关于您调查的那些事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270110957V#143F哦，真是开门见山啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110958V#140F给你……\n',
            '主要成员的简历都收集到了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '奈尔拿出一本黑色封皮的文件夹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#0010110959V#004F这是……王国军的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270110960V#140F啊，虽然机密度不是很高，\n',
            '不过也不是随便就能拿出来的文件呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110961V好不容易说服军队中的熟人才借来的，\n',
            '总之你们千万不要往外透露啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110962V#012F我知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110963V#06F那么，我们就在这里看吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)
    OP_20(0x000005DC)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔和约修亚\n',
            '翻看着那本黑色封皮的文件夹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    PlayBGM(34)
    FadeOut(1500, 0, -56)
    OP_0D()
    Sleep(500)

    def _loc_4864(): pass

    label('loc_4864')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_524A',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
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

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CE, 3, 0x673)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CE, 4, 0x674)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00CE, 5, 0x675)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_48DD',
    )

    Menu(
        0,
        10,
        10,
        0,
        (
            TXT(0x00, '【关于理查德上校】\n'),
            TXT(0x01, '【凯诺娜上尉】\n'),
            TXT(0x02, '【洛伦斯少尉】\n'),
            TXT(0x03, '【关闭文件】\n'),
        ),
    )

    Jump('loc_4917')

    def _loc_48DD(): pass

    label('loc_48DD')

    Menu(
        0,
        10,
        10,
        0,
        (
            TXT(0x00, '【关于理查德上校】\n'),
            TXT(0x01, '【凯诺娜上尉】\n'),
            TXT(0x02, '【洛伦斯少尉】\n'),
        ),
    )

    def _loc_4917(): pass

    label('loc_4917')

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_4941'),
        (0x00000001, 'loc_4CCC'),
        (0x00000002, 'loc_4F3C'),
        (0x00000003, 'loc_5237'),
        (-1, 'loc_5247'),
    )

    def _loc_4941(): pass

    label('loc_4941')

    OP_AD('ED6_DT04/C_VIS033._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(1000)

    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            '#0270110964V',
            (TxtCtl.SetColor, 0x5),
            '亚兰·理查德上校。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0270110965V',
            (TxtCtl.SetColor, 0x5),
            '七耀历１１６８年，\n',
            '生于利贝尔王国卢安地区。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0270110966V',
            (TxtCtl.SetColor, 0x5),
            '作为士官学校的主席毕业之后，\n',
            '编入了卡西乌斯·布莱特上校率领的\n',
            '独立机动部队。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0270110967V',
            (TxtCtl.SetColor, 0x5),
            '１１９２年的百日战役中，\n',
            '作为卡西乌斯上校的部下\n',
            '在反攻作战中屡立战功。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0270110968V',
            (TxtCtl.SetColor, 0x5),
            '卡西乌斯上校退役之后，\n',
            '被提拔为军队作战中心的成员，\n',
            '在组织改革中建立了很多功绩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0270110969V',
            (TxtCtl.SetColor, 0x5),
            '１２０１年，作出了设立情报部的提案。\n',
            '之后获得了艾莉茜雅女王的承认，\n',
            '就任情报部首任指挥官。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CE, 3, 0x673)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4CBF',
    )

    SetScenaFlags(ScenaFlag(0x00CE, 3, 0x673))
    SetMessageWindowPos(75, 250, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010110970V',
            (TxtCtl.SetColor, 0x0),
            '#007F该怎么说呢……\n',
            '这就是所谓的精英吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110971V他可是主席呢，主席。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(150, 300, -1, -1)
    TalkSetChrName('约修亚')

    Talk(
        (
            '#0020110972V#012F确实是个很厉害的人物。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110973V希德少校说得没错，\n',
            '十年前战争的时候他确实是父亲的部下。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(75, 250, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010110974V#505F嗯，老爸真的当过上校呢……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110975V明明这么了不起，\n',
            '为什么要辞掉呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_4CBF(): pass

    label('loc_4CBF')

    OP_AE(0x000001F4)
    Sleep(500)

    Jump('loc_5247')

    def _loc_4CCC(): pass

    label('loc_4CCC')

    OP_AD('ED6_DT04/C_VIS034._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(1000)

    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            '#0270110976V',
            (TxtCtl.SetColor, 0x5),
            '凯诺娜·亚马尔迪亚上尉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0270110977V',
            (TxtCtl.SetColor, 0x5),
            '七耀历１１７５年，\n',
            '生于利贝尔王国王都格兰赛尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0270110978V',
            (TxtCtl.SetColor, 0x5),
            '以优秀的成绩从士官学校毕业之后，\n',
            '被提拔为军队作战中心的成员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0270110979V',
            (TxtCtl.SetColor, 0x5),
            '１２０１年，在情报部设立的同时，\n',
            '得到理查德上校的提拔并被调到了情报部。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0270110980V',
            (TxtCtl.SetColor, 0x5),
            '之后，作为理查德上校的副官，\n',
            '担当辅佐其进行作战指挥的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CE, 4, 0x674)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4F2F',
    )

    SetScenaFlags(ScenaFlag(0x00CE, 4, 0x674))
    SetMessageWindowPos(75, 250, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010110981V',
            (TxtCtl.SetColor, 0x0),
            '#509F『以优秀的成绩毕业』，\n',
            '看起来又是一个精英呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(150, 300, -1, -1)
    TalkSetChrName('约修亚')

    Talk(
        (
            '#0020110982V#015F自从担任军官以来，\n',
            '她好像一直在理查德上校手下做事。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110983V真是相当地忠诚呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_4F2F(): pass

    label('loc_4F2F')

    OP_AE(0x000001F4)
    Sleep(500)

    Jump('loc_5247')

    def _loc_4F3C(): pass

    label('loc_4F3C')

    OP_AD('ED6_DT04/C_VIS035._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(1000)

    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            '#0270110984V',
            (TxtCtl.SetColor, 0x5),
            '洛伦斯·博格少尉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0270110985V',
            (TxtCtl.SetColor, 0x5),
            '年龄、国籍不明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0270110986V',
            (TxtCtl.SetColor, 0x5),
            '原属佣兵部队『杰斯塔猎兵团』，\n',
            '应理查德上校的征召\n',
            '成为情报部的一员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            '#0270110987V',
            (TxtCtl.SetColor, 0x5),
            '在这之前的经历不明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CE, 5, 0x675)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_522A',
    )

    SetScenaFlags(ScenaFlag(0x00CE, 5, 0x675))
    SetMessageWindowPos(75, 250, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0270110988V',
            (TxtCtl.SetColor, 0x0),
            '#580F那个戴面具的家伙……\n',
            '不是利贝尔人啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110989V而且没有记载他作为原佣兵时的经历，\n',
            '……这是怎么一回事啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(150, 300, -1, -1)
    TalkSetChrName('约修亚')

    Talk(
        (
            '#0010110990V#013F……不知道。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110991V所谓『猎兵团』，\n',
            '是只有最高级别的佣兵部队\n',
            '才能获得的特殊称号……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(75, 250, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0020110992V#505F哎～是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110993V是不是因为战斗能力很强，\n',
            '所以才得到上校提拔的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(150, 300, -1, -1)
    TalkSetChrName('约修亚')

    Talk(
        (
            '#0010110994V#015F嗯……说不定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110995V『杰斯塔猎兵团』……\n',
            '这个名字好像在哪里听说过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_522A(): pass

    label('loc_522A')

    OP_AE(0x000001F4)
    Sleep(500)

    Jump('loc_5247')

    def _loc_5237(): pass

    label('loc_5237')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)

    Jump('loc_5247')

    def _loc_5247(): pass

    label('loc_5247')

    Jump('loc_4864')

    def _loc_524A(): pass

    label('loc_524A')

    FadeIn(1500, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010110996V#006F谢谢你，奈尔。\n',
            '不管怎么说，能看清敌人的底细了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270110997V#141F能帮上忙就再好不过了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110998V我在调查资料的时候，\n',
            '也发现了很多有趣的事情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0009, 400)

    ChrTalk(
        0x0102,
        (
            '#0020110999V#014F有趣的事情是指……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270111000V#141F比如，现在被通缉的\n',
            '亲卫队队长的尤莉亚中尉……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270111001V在士官学校就读的时候，\n',
            '是和凯诺娜上尉是同一年级的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111002V#004F哎～是吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111003V#014F不过看起来，\n',
            '那两个人的关系好像不是很好呢……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270111004V#145F不管怎么说，\n',
            '她们是互相竞争主席职位的对手。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270111005V文有凯诺娜，武有尤莉亚，\n',
            '两个人真是很好的对照呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111006V#010F原来如此……\n',
            '我大概能想象出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111007V#006F一看到尤莉亚中尉威风凛凛的英姿，\n',
            '我就觉得她好像过去的骑士呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270111008V#140F还有……\n',
            '虽然这个和军队没有关系。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270111009V你们听说过\n',
            '『科洛蒂娅公主』这个名字吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111010V#505F科洛蒂娅公主……\n',
            '好像在哪里听说过？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111011V#010F我记得，是在海难事故中去世的\n',
            '王太子夫妻的遗孤吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111012V是女王陛下的孙女……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270111013V#140F嗯，虽然不太有名，\n',
            '不过可是直系中的直系呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270111014V她好像一直生活在\n',
            '格兰赛尔城的女王宫里……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270111015V而且，好像某个人物正在寻找\n',
            '那位公主殿下的相亲对象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111016V#007F相亲对象啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111017V虽然对大户人家来说，\n',
            '不是什么新鲜事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111018V#003F不过觉得公主有点可怜呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111019V#017F艾丝蒂尔，重点不在那里吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111020V#012F应该注意的字眼是『某个人物』吧？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270111021V#141F呵呵，真是敏锐啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111022V#004F哎，那个人难道是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
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
        10,
        0,
        (
            TXT(0x00, '【艾莉茜雅女王】\n'),
            TXT(0x01, '【杜南公爵】\n'),
            TXT(0x02, '【理查德上校】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_58BD'),
        (0x00000001, 'loc_59C4'),
        (0x00000002, 'loc_5AC6'),
        (-1, 'loc_5BCC'),
    )

    def _loc_58BD(): pass

    label('loc_58BD')

    ChrTalk(
        0x0009,
        (
            '#0270111023V#142F啊，名义上是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270111024V不过实际上，\n',
            '派人去外国寻找合适的对象的人，\n',
            '正是那个理查德上校呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111025V#004F是、是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111026V#505F但是……这不是很奇怪吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111027V为什么会是理查德上校\n',
            '来寻找公主的结婚对象呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5BCC')

    def _loc_59C4(): pass

    label('loc_59C4')

    ChrTalk(
        0x0009,
        (
            '#0270111028V#142F没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270111029V不过实际上，\n',
            '派人去外国寻找合适的对象的人，\n',
            '正是那个理查德上校呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111025V#004F是、是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111026V#505F但是……这不是很奇怪吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111027V为什么会是理查德上校\n',
            '来寻找公主的结婚对象呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_2B(0x0045, 0x0001)

    Jump('loc_5BCC')

    def _loc_5AC6(): pass

    label('loc_5AC6')

    ChrTalk(
        0x0009,
        (
            '#0270111033V#141F哦，还真是聪明啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270111034V其实实际上，\n',
            '派人去外国寻找合适的对象的人，\n',
            '正是那个理查德上校呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111035V#007F果然……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111026V#505F但是……这不是很奇怪吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111027V为什么会是理查德上校\n',
            '来寻找公主的结婚对象呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_2B(0x0045, 0x0002)

    Jump('loc_5BCC')

    def _loc_5BCC(): pass

    label('loc_5BCC')

    ChrTalk(
        0x0009,
        (
            '#0270111038V#141F所以我说，\n',
            '到处充满了可疑的气味呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270111039V正因如此……\n',
            '有件事情想拜托你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111040V#004F哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111041V#015F——如果明天的比赛能获胜，\n',
            '被招待进王城参加晚餐的话，\n',
            '打听一下这方面的情报。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111042V#010F是这样没错吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111043V#509F啊，是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111044V#007F算了，反正你也挺大方地\n',
            '告诉了我们很多消息……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270111045V#141F我只是做了自己力所能及的事情罢了。\n',
            '总之，有来有往也是理所当然的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111046V#019F确实帮了我们很多忙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111047V#006F没办法呢～\n',
            '如果知道了什么，就告诉你吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270111048V#147F嘿嘿，早这样说不就好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270111049V#141F不过，就算不拜托你们，\n',
            '运气好的话今天也能……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(195, 0x00, 0x64)
    LoadEffect(0x00, 'map\\\\mp001_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, -55170, 2000, 64580, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#0270111050V#143F哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0009, 0xFF)
    ChrSetDirection(0x0009, 90, 400)

    @scena.Lambda('lambda_5F10')
    def lambda_5F10():
        CameraMove(-56140, 0, 65099, 1500)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_5F10)

    ChrWalkTo(0x0009, -56110, 0, 64019, 3000, 0x00)
    ChrWalkTo(0x0009, -55030, 0, 64019, 3000, 0x00)
    ChrSetDirection(0x0009, 0, 400)
    Sleep(500)

    WaitForThreadExit(0x0009, 0x0001)
    PlaySE(131, 0x00, 0x64)
    StopEffect(0x00, 0x00)
    LoadEffect(0x00, 'map\\\\mp001_01.eff')
    PlayEffect(0x00, 0x01, 0x00FF, -55170, 2000, 64580, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0270111051V#140F喂。\n',
            '这里是利贝尔通讯社……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270111052V#147F哦，是你啊！\n',
            '我一直在等你的联络呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270111053V#143F什么……现在就？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270111054V#141F啊，知道了。\n',
            '我立刻过去找你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(131, 0x00, 0x64)
    StopEffect(0x01, 0x00)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010111055V#501F怎么，发生什么事情了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 400)

    @scena.Lambda('lambda_60B3')
    def lambda_60B3():
        CameraMove(-57890, 0, 65099, 1200)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_60B3)

    ChrWalkTo(0x0009, -55690, 0, 64019, 2000, 0x00)
    ChrWalkTo(0x0009, -57490, 0, 64410, 2000, 0x00)
    ChrTurnDirection(0x0009, 0x0101, 400)
    WaitForThreadExit(0x0009, 0x0001)

    ChrTalk(
        0x0009,
        (
            '#0270111056V#141F稍微有点私事。\n',
            '现在要去和别人会面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111057V#014F很重要的事吗？\n',
            '现在的天色已经这么黑了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270111058V#145F本来我就是个夜猫子啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270111059V因为要带那个\n',
            '我行我素的丫头进行新人研修，\n',
            '才不得不把生物钟调整回来了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270111060V#142F唉，不说这件事情了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270111061V我要出去了，\n',
            '你们接着干你们的事情吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111062V#006F嗯，我知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010111063V要加油工作哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0270111064V#141F你们也是。\n',
            '明天的比赛一定不能输啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_62D1')
    def lambda_62D1():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_62D1')

    DispatchAsync2(0x0101, 0x0001, lambda_62D1)

    @scena.Lambda('lambda_62E2')
    def lambda_62E2():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_62E2')

    DispatchAsync2(0x0102, 0x0001, lambda_62E2)

    @scena.Lambda('lambda_62F3')
    def lambda_62F3():
        CameraMove(-59840, 0, 65099, 2000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_62F3)

    ChrWalkTo(0x0009, -58470, 0, 65300, 3000, 0x00)
    ChrWalkTo(0x0009, -60060, 0, 65300, 3000, 0x00)
    ChrWalkTo(0x0009, -60840, 0, 66460, 3000, 0x00)
    ChrWalkTo(0x0009, -63690, 0, 66460, 3000, 0x00)
    TerminateThread(0x0101, 0xFF)
    ChrWalkTo(0x0009, -63690, -2230, 62470, 3000, 0x00)
    ChrSetFlags(0x0009, 0x0080)
    TerminateThread(0x0102, 0xFF)
    WaitForThreadExit(0x0009, 0x0001)
    OP_20(0x000005DC)

    @scena.Lambda('lambda_6386')
    def lambda_6386():
        CameraMove(-57890, 0, 65099, 1500)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_6386)

    WaitForThreadExit(0x0009, 0x0001)
    OP_21()
    PlayBGM(14)
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010111065V#006F#5P接下来……\n',
            '我们该怎么办呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020111066V#010F是啊……\n',
            '总之，先顺路去协会，\n',
            '然后就回酒店休息吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020111067V最好把奈尔先生调查到的情报\n',
            '向协会报告一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111068V#006F#5P嗯，知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0048, 0x01, 0x0040)
    EventEnd(0x00)

    Return()

# id: 0x000B offset: 0x6494
@scena.Code('func_0B_6494')
def func_0B_6494():
    EventBegin(0x00)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, -56250, 0, 60940, 90)
    ChrSetPos(0x0101, -60190, 0, 65280, 135)
    ChrSetPos(0x0102, -61190, 0, 64849, 135)
    ChrSetPos(0x0108, -60700, 0, 66190, 135)
    ChrSetFlags(0x0018, 0x0080)
    ChrSetFlags(0x0019, 0x0080)
    OP_4A(0x000A, 255)
    CameraMove(-54490, 0, 61730, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x000A,
        (
            '#0280130249V#152F主编，真的好奇怪呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280130250V已经两天没有取得联络了呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2310130251V嗯，我想那家伙\n',
            '肯定是沉浸在寻找\n',
            '独家新闻的美梦当中了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2310130252V但是，在这个戒严时期\n',
            '不能取得联系的确有些奇怪……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000B,
        (
            '#2310130253V哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_6629')
    def lambda_6629():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_6629)

    CameraMove(-56640, 0, 63970, 1500)

    ChrTalk(
        0x000A,
        (
            '#0280130254V#151F啊，小艾你们来了啊～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130255V#006F#5P你好，朵洛希。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130256V#010F#5P打扰了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_66BF')
    def lambda_66BF():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_66BF')

    DispatchAsync2(0x000A, 0x0001, lambda_66BF)

    @scena.Lambda('lambda_66D0')
    def lambda_66D0():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_66D0')

    DispatchAsync2(0x0101, 0x0001, lambda_66D0)

    @scena.Lambda('lambda_66E1')
    def lambda_66E1():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_66E1')

    DispatchAsync2(0x0102, 0x0001, lambda_66E1)

    @scena.Lambda('lambda_66F2')
    def lambda_66F2():
        CameraMove(-55080, 0, 62180, 2000)

        ExitThread()

    DispatchAsync(0x0108, 0x0003, lambda_66F2)

    @scena.Lambda('lambda_670A')
    def lambda_670A():
        ChrWalkTo(0x00FE, -54540, 0, 62770, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_670A)

    Sleep(300)

    @scena.Lambda('lambda_672A')
    def lambda_672A():
        ChrWalkTo(0x00FE, -55820, 0, 62630, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_672A)

    Sleep(300)

    ChrWalkTo(0x0108, -59680, 0, 64599, 3000, 0x00)

    @scena.Lambda('lambda_675E')
    def lambda_675E():
        ChrWalkTo(0x00FE, -55430, 0, 63990, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_675E)

    WaitForThreadExit(0x0108, 0x0002)
    ChrSetDirection(0x0108, 180, 400)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0108, 0xFF)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CF, 7, 0x67F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_698E',
    )

    SetScenaFlags(ScenaFlag(0x00CF, 7, 0x67F))

    ChrTalk(
        0x000B,
        (
            '#2310130257V哦，武术大会的优胜者……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2310130258V先自我介绍一下，\n',
            '我是《利贝尔通讯》的主编。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2310130259V我从奈尔和朵洛希那里\n',
            '听说过你们的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2310130260V你们二位是游击士协会的\n',
            '艾丝蒂尔和约修亚吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130261V#008F#5P啊，您好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130262V#010F#5P初次见面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130263V《利贝尔通讯》的每一期\n',
            '都给我们带来了不少乐趣呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2310130264V哈哈哈。\n',
            '听你这么说我很高兴啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2310130265V话说回来，\n',
            '你们是来找奈尔的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130266V#501F啊，是的，可以这么说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6A11')

    def _loc_698E(): pass

    label('loc_698E')

    ChrTalk(
        0x000B,
        (
            '#2310130267V是你们啊……\n',
            '你们可总算来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130268V#006F您好，打扰了～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130269V我们是来找奈尔的，\n',
            '难道他出去了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6A11(): pass

    label('loc_6A11')

    ChrTalk(
        0x000B,
        (
            '#2310130270V我们刚才正在\n',
            '谈起这件事请呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2310130271V事实上奈尔他昨天和今天\n',
            '都没有到编辑部来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2310130272V完全不能和他取得联络。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130273V#580F什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130274V#012F昨天和今天都……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130275V我们前天傍晚还在这里和奈尔先生\n',
            '商讨一些事情……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x000A, 0xFF)
    ChrTurnDirection(0x000A, 0x0101, 400)

    ChrTalk(
        0x000A,
        (
            '#0280130276V#153F真、真的吗～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_6B61')
    def lambda_6B61():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_6B61)

    ChrTurnDirection(0x0101, 0x000A, 400)

    ChrTalk(
        0x0101,
        (
            '#0010130277V#007F什么真的假的啊，\n',
            '给奈尔捎口信的不就是朵洛希你吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130278V#002F半决赛之后，\n',
            '让我们到这里来向他打听情报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0280130279V#151F啊～我想起来了，\n',
            '就～是那件事情～啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280130280V#154F请问请问～\n',
            '奈尔前辈那时是怎么说的呢～？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280130281V他到哪里去了呢～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
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
        10,
        0,
        (
            TXT(0x00, '【去收集新闻了】\n'),
            TXT(0x01, '【有人叫他出去】\n'),
            TXT(0x02, '【一起去吃晚餐了】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_6D14'),
        (0x00000001, 'loc_6DC6'),
        (0x00000002, 'loc_6E34'),
        (-1, 'loc_6ED1'),
    )

    def _loc_6D14(): pass

    label('loc_6D14')

    ChrTalk(
        0x0102,
        (
            '#0020130282V#012F很有可能是到外面收集新闻了……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130283V准确地说，当时有人发联络叫他出去，\n',
            '于是他就到什么地方了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130284V#505F啊，的确是那样的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_2B(0x004B, 0x0001)

    Jump('loc_6ED1')

    def _loc_6DC6(): pass

    label('loc_6DC6')

    ChrTalk(
        0x0102,
        (
            '#0020130285V#012F嗯，没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130286V当时有人发联络叫他出去，\n',
            '于是他就不知道到什么地方去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_2B(0x004B, 0x0002)

    Jump('loc_6ED1')

    def _loc_6E34(): pass

    label('loc_6E34')

    ChrTalk(
        0x0102,
        (
            '#0020130287V#017F不，那是三天前的事情了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130288V#012F两天前的傍晚，\n',
            '奈尔先生是被某个人用通信器叫出去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130289V#505F啊，是这样吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6ED1')

    def _loc_6ED1(): pass

    label('loc_6ED1')

    ChrTalk(
        0x000B,
        (
            '#2310130290V你们说的是真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_6EFB')
    def lambda_6EFB():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_6EFB)

    ChrTurnDirection(0x0101, 0x000B, 400)

    ChrTalk(
        0x0102,
        (
            '#0020130291V#012F是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130292V大概这就是从那时开始到现在为止\n',
            '他都没有音信的原因吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0280130293V#152F怎、怎么会！\n',
            '前辈你不能死啊～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000A, 400)

    ChrTalk(
        0x0101,
        (
            '#0010130294V#509F哎，不要说那些莫名其妙的话啦！\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130295V#007F从今天开始定期船也停航了……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130296V#505F到昨天为止还是可以通航的，\n',
            '他会不会到别的地方去了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2310130297V已经到空港看过了，\n',
            '在登机名单上没有记载。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_709A')
    def lambda_709A():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_709A)

    @scena.Lambda('lambda_70A8')
    def lambda_70A8():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_70A8)

    ChrTalk(
        0x000B,
        (
            '#2310130298V也就是说……\n',
            '他应该还在王都这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080101499V#074F嗯～……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130300V#070F你们两个在和那个叫奈尔的记者\n',
            '最后一次见面的时候……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130301V那个记者没有提起过，\n',
            '说他得到了什么新闻材料吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_718E')
    def lambda_718E():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_718E)

    @scena.Lambda('lambda_719C')
    def lambda_719C():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_719C)

    ChrTurnDirection(0x0101, 0x0108, 400)

    ChrTalk(
        0x0101,
        (
            '#0010130302V#004F#4P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130303V#070F现在这种局势。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130304V大众传媒也被军队所管制吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130305V对吗，主编先生？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2310130306V是啊，的确如此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2310130307V特别是围绕情报部的话题，\n',
            '正处于被层层审批的状态之中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2310130308V能不能登出来就取决于他们的心情好坏。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130309V#074F……在这种状况下，\n',
            '可以报道的新闻自然就少了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130310V可是，作为一个记者，\n',
            '哪怕是有一点新的消息，\n',
            '都想尽快传达给读者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130311V#010F#4P原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130312V情报部的管制不成问题，\n',
            '以新的具有话题性的消息为重……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130313V关于这个，奈尔先生\n',
            '曾经是提起过什么的对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130314V#004F#4P啊，对了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
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
        10,
        0,
        (
            TXT(0x00, '【关于武术大会的优胜者】\n'),
            TXT(0x01, '【关于科洛蒂亚公主的婚姻】\n'),
            TXT(0x02, '【关于尤莉亚和凯诺娜的过去】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_74D8'),
        (0x00000001, 'loc_767F'),
        (0x00000002, 'loc_76BB'),
        (-1, 'loc_7858'),
    )

    def _loc_74D8(): pass

    label('loc_74D8')

    ChrTalk(
        0x0108,
        (
            '#0080130315V#072F要把这个作为新闻的话，\n',
            '也应该是在我们取得优胜之前的事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130316V作为现在的新消息就没有时效性了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130317V#505F#4P这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130318V的确，因为特务兵他们\n',
            '还是有取胜的可能性呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130319V#015F#4P还有一个线索。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130320V#012F奈尔先生对科洛蒂亚公主的婚姻事情\n',
            '似乎很有兴趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130321V#580F#4P啊……没错！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130322V#073F哦，晚宴时公爵所说的话……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_2B(0x004B, 0x0001)

    Jump('loc_7858')

    def _loc_767F(): pass

    label('loc_767F')

    ChrTalk(
        0x0108,
        (
            '#0080130322V#073F哦，晚宴时公爵所说的话……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_2B(0x004B, 0x0002)

    Jump('loc_7858')

    def _loc_76BB(): pass

    label('loc_76BB')

    ChrTalk(
        0x0108,
        (
            '#0080130324V#073F理查德上校的副官和通缉中的女亲卫队员\n',
            '在士官学校里是对手……\n',
            ' ',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130325V#070F虽然很有趣，不过对于情报部来说\n',
            '这种事情允许取材吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130326V#007F#4P嗯，确实……\n',
            '不能作为报道呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130319V#015F#4P还有一个线索。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130320V#012F奈尔先生对科洛蒂亚公主的婚姻事情\n',
            '似乎很有兴趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130321V#580F#4P啊……没错！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130322V#073F哦，晚宴时公爵所说的话……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_2B(0x004B, 0x0001)

    Jump('loc_7858')

    def _loc_7858(): pass

    label('loc_7858')

    ChrTalk(
        0x000B,
        (
            '#2310130331V什么？\n',
            '奈尔和你们谈到了这件事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_788F')
    def lambda_788F():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_788F)

    @scena.Lambda('lambda_789D')
    def lambda_789D():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_789D)

    ChrTalk(
        0x000B,
        (
            '#2310130332V如果是真的话，\n',
            '那就是个爆炸性的新闻啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2310130333V总算是可以获取\n',
            '一些内幕了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130334V#073F那个叫奈尔的记者\n',
            '怎么会知道这些事情？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130335V不是说与王家无关的人员\n',
            '都不知道这个情报的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0280130336V#150F他可能是从那个在艾尔贝离宫工作的\n',
            '朋友那里打听回来的吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280130337V#151F还有一个不能报道的消息，\n',
            '公主殿下也被恐怖分子列为目标了～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280130338V因此公主殿下在艾尔贝离宫里面\n',
            '被秘密保护了起来～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0108, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_7AAD')
    def lambda_7AAD():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_7AAD)

    @scena.Lambda('lambda_7ABB')
    def lambda_7ABB():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_7ABB)

    @scena.Lambda('lambda_7AC9')
    def lambda_7AC9():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_7AC9)

    ChrTalk(
        0x0101,
        (
            '#0010130339V#005F……果然！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130340V#070F呵呵呵，\n',
            '得来全不费工夫啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130341V#013F难道那天叫奈尔出去的\n',
            '就是他在离宫里面工作的朋友吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130342V这样一来……\n',
            '奈尔先生在离宫的可能性就很高了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2310130343V是、是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2310130344V也许奈尔为了\n',
            '去采访公主殿下，\n',
            '强行潜入了离宫……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2310130345V然后被士兵发现了，\n',
            '抓了起来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0280130346V#152F呀～啊！\n',
            '奈尔前辈死定了～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130347V#007F都说了不会死的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130348V#002F但是，如果这是事实的话，\n',
            '他是不会被轻易释放出来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130349V#012F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130350V他和科洛蒂娅公主\n',
            '处于同样境地的可能性比较高。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2310130351V我说年轻人啊……\n',
            '你们究竟知道了些什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2310130352V在这个王都……不，\n',
            '在利贝尔究竟发生了什么事，\n',
            '你们不会不知道其中的内幕吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_7DD0')
    def lambda_7DD0():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_7DD0)

    ChrTurnDirection(0x0101, 0x000B, 400)

    ChrTalk(
        0x0101,
        (
            '#0010130353V#007F唔～对不起。\n',
            '请恕我们无可奉告。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130354V#012F奈尔先生的事情，\n',
            '请交给我们游击士协会去办吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130355V如果的确是被拘捕了，\n',
            '那我们一定会把他解救出来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2310130356V太好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2310130357V我明白了，拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0280130358V#154F拜、拜托了～！小艾～！\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280130359V一定要救救奈尔前辈～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000A, 400)

    ChrTalk(
        0x0101,
        (
            '#0010130360V#006F嗯，交给我们吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x004B, 0x01, 0x0200)
    CreateThread(0x000A, 0x00, 0x00, func_02_BB2)
    EventEnd(0x00)

    Return()

# id: 0x000C offset: 0x7F6E
@scena.Code('func_0C_7F6E')
def func_0C_7F6E():
    MapClearFlags(0x10000000)
    EventBegin(0x00)
    ChrSetFlags(0x0019, 0x0080)
    CameraMove(-53570, 0, 62700, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(1650, 0)
    OP_6C(58000, 0)
    OP_6E(493, 0)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, -54290, 0, 62760, 109)
    ChrSetPos(0x000A, -60220, 0, 62930, 197)
    OP_4A(0x000A, 255)
    ChrSetChipByIndex(0x000A, 35)
    CreateThread(0x0101, 0x00, 0x00, func_0D_8220)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#0270131110V#142F嘁……\n',
            '终于开始了吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_802F')
    def lambda_802F():
        CameraMove(-56060, 0, 62820, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_802F)

    ChrSetDirection(0x0009, 289, 400)
    ChrWalkTo(0x0009, -56680, 0, 62880, 3000, 0x00)
    ChrTurnDirection(0x0009, 0x000A, 400)
    WaitForThreadExit(0x0000, 0x0001)

    ChrTalk(
        0x0009,
        (
            '#0270131111V#144F#2P出发，朵洛希！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270131112V必须要确保找到\n',
            '可以从远处眺望这场战斗的最佳位置！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrTurnDirection(0x000A, 0x0009, 400)

    ChrTalk(
        0x000A,
        (
            '#0280131113V#152F等、等一下好吗～！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280131114V感光结晶回路马上就可以设置好了～！\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2310131115V喂喂，到底是怎么回事啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2310131116V这三天来你去哪里游山玩水了啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0009, 109, 600)

    ChrTalk(
        0x0009,
        (
            '#0270131117V#144F这可是独家新闻！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270131118V『利贝尔通讯社』建社以来\n',
            '前所未有的超级无敌独家新闻啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T4240._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000D offset: 0x8220
@scena.Code('func_0D_8220')
def func_0D_8220():
    PlaySE(181, 0x00, 0x64)
    Sleep(2500)

    PlaySE(181, 0x00, 0x64)
    Sleep(2500)

    PlaySE(181, 0x00, 0x64)
    Sleep(2500)

    PlaySE(181, 0x00, 0x64)
    Sleep(2500)

    PlaySE(181, 0x00, 0x64)
    Sleep(2500)

    PlaySE(181, 0x00, 0x64)

    Return()

# id: 0x000E offset: 0x8258
@scena.Code('func_0E_8258')
def func_0E_8258():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '巴拉尔咖啡厅名菜！\n',
            '『巨匠咖喱饭』　　１０００米拉',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '使用秘传的香辛料精心烹制的辣味咖喱，\n',
            '请您走过路过不要错过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x000F offset: 0x82FD
@scena.Code('func_0F_82FD')
def func_0F_82FD():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '～　菜单　～\n',
            '　混合鸡尾酒　　　７５０米拉\n',
            '　香草派　　　　　４５０米拉',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '～　本店推荐　～\n',
            '　劲霸浓鱼汤　　　１０００米拉',
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

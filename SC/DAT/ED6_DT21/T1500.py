import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T1500_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1500   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1500.x'
    header.mapIndex       = 1
    header.bgm            = 15
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
        ('ED6_DT06/CH20045._CH', 'ED6_DT06/CH20045P._CP'),
        ('ED6_DT27/CH03003._CH', 'ED6_DT27/CH03003P._CP'),
        ('ED6_DT07/CH00023._CH', 'ED6_DT07/CH00023P._CP'),
        ('ED6_DT07/CH00053._CH', 'ED6_DT07/CH00053P._CP'),
        ('ED6_DT07/CH00033._CH', 'ED6_DT07/CH00033P._CP'),
        ('ED6_DT07/CH00043._CH', 'ED6_DT07/CH00043P._CP'),
        ('ED6_DT07/CH00063._CH', 'ED6_DT07/CH00063P._CP'),
        ('ED6_DT07/CH00073._CH', 'ED6_DT07/CH00073P._CP'),
        ('ED6_DT27/CH03083._CH', 'ED6_DT27/CH03083P._CP'),
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT07/CH00050._CH', 'ED6_DT07/CH00050P._CP'),
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT07/CH00040._CH', 'ED6_DT07/CH00040P._CP'),
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP'),
        ('ED6_DT27/CH03080._CH', 'ED6_DT27/CH03080P._CP'),
        ('ED6_DT07/CH02323._CH', 'ED6_DT07/CH02323P._CP'),
        ('ED6_DT26/CH20235._CH', 'ED6_DT26/CH20235P._CP'),
        ('ED6_DT26/CH20240._CH', 'ED6_DT26/CH20240P._CP'),
        ('ED6_DT26/CH20402._CH', 'ED6_DT26/CH20402P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
        ('ED6_DT26/CH20372._CH', 'ED6_DT26/CH20372P._CP'),
        ('ED6_DT26/CH20395._CH', 'ED6_DT26/CH20395P._CP'),
        ('ED6_DT26/CH20394._CH', 'ED6_DT26/CH20394P._CP'),
        ('ED6_DT26/CH20393._CH', 'ED6_DT26/CH20393P._CP'),
        ('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP'),
        ('ED6_DT07/CH00151._CH', 'ED6_DT07/CH00151P._CP'),
        ('ED6_DT07/CH00152._CH', 'ED6_DT07/CH00152P._CP'),
        ('ED6_DT07/CH00153._CH', 'ED6_DT07/CH00153P._CP'),
        ('ED6_DT07/CH00154._CH', 'ED6_DT07/CH00154P._CP'),
        ('ED6_DT07/CH00159._CH', 'ED6_DT07/CH00159P._CP'),
        ('ED6_DT06/CH20137._CH', 'ED6_DT06/CH20137P._CP'),
        ('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP'),
        ('ED6_DT07/CH00171._CH', 'ED6_DT07/CH00171P._CP'),
        ('ED6_DT07/CH00172._CH', 'ED6_DT07/CH00172P._CP'),
        ('ED6_DT07/CH00173._CH', 'ED6_DT07/CH00173P._CP'),
        ('ED6_DT07/CH00174._CH', 'ED6_DT07/CH00174P._CP'),
        ('ED6_DT07/CH00178._CH', 'ED6_DT07/CH00178P._CP'),
        ('ED6_DT07/CH01230._CH', 'ED6_DT07/CH01230P._CP'),
        ('ED6_DT07/CH01220._CH', 'ED6_DT07/CH01220P._CP'),
        ('ED6_DT27/CH03790._CH', 'ED6_DT27/CH03790P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT27/CH03860._CH', 'ED6_DT27/CH03860P._CP'),
        ('ED6_DT26/CH20408._CH', 'ED6_DT26/CH20408P._CP'),
    ]

# id: 0x10001 offset: 0x212
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '雪拉扎德',
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
            name                = '阿加特',
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
            name                = '奥利维尔',
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
            name                = '科洛丝',
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
            name                = '提妲',
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
            name                = '金',
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
            name                = '凯文神父',
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '基库',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '小船',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '小船',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '克鲁茨',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '诺琪',
            x                   = 3480,
            z                   = -2000,
            y                   = 43140,
            direction           = 128,
            word_0E             = 0,
            dword_10            = 38,
            chipIndex           = 38,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '赫穆特',
            x                   = 2070,
            z                   = -2000,
            y                   = 38510,
            direction           = 189,
            word_0E             = 0,
            dword_10            = 39,
            chipIndex           = 39,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '斯丁克',
            x                   = -9480,
            z                   = 0,
            y                   = 62260,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 40,
            chipIndex           = 40,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '罗伊德',
            x                   = -8170,
            z                   = 500,
            y                   = 40910,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 42,
            chipIndex           = 42,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '操舵士勒克司',
            x                   = -11480,
            z                   = -2000,
            y                   = 34670,
            direction           = 267,
            word_0E             = 0,
            dword_10            = 43,
            chipIndex           = 43,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '酒杯',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 327700,
            chipIndex           = 20,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '酒杯',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 327700,
            chipIndex           = 20,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '酒杯',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '酒杯',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '库瓦诺老人',
            x                   = -37610,
            z                   = -2000,
            y                   = 44850,
            direction           = 178,
            word_0E             = 0,
            dword_10            = 41,
            chipIndex           = 41,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '桶和魚',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 262188,
            chipIndex           = 44,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '桶和魚',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 262188,
            chipIndex           = 44,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '桶和魚',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 44,
            chipIndex           = 44,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '桶和魚',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 65580,
            chipIndex           = 44,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '安赛尔新街方向',
            x                   = -8640,
            z                   = 0,
            y                   = 96040,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x552
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x552
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -46710,
            y           = -2400,
            z           = 40980,
            range       = -43080,
            dword_10    = 0xFFFFFE70,
            dword_14    = 0x0000A604,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000017,
        ),
        ScenaEventData(
            x           = -5850,
            y           = -1000,
            z           = 80880,
            range       = -10140,
            dword_10    = 0x000007D0,
            dword_14    = 0x00014438,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000001A,
        ),
    )

# id: 0x10004 offset: 0x592
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -9910,
            triggerZ            = 500,
            triggerY            = 47790,
            triggerRange        = 800,
            actorX              = -9910,
            actorZ              = 1500,
            actorY              = 47790,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -4980,
            triggerZ            = 4000,
            triggerY            = 54310,
            triggerRange        = 800,
            actorX              = -4980,
            actorZ              = 5000,
            actorY              = 54310,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -5090,
            triggerZ            = 4000,
            triggerY            = 47820,
            triggerRange        = 800,
            actorX              = -5090,
            actorZ              = 5000,
            actorY              = 47820,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -2910,
            triggerZ            = -2000,
            triggerY            = 32500,
            triggerRange        = 1000,
            actorX              = -2980,
            actorZ              = -3000,
            actorY              = 29380,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001B,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x622
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_64A',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x19),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    OP_B1('T1500_n')
    Event(0, func_0C_29AB)

    Jump('loc_67A')

    def _loc_64A(): pass

    label('loc_64A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_67A',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    MapSetFlags(0x10000000)
    OP_B1('T1500_y')
    OP_71(0x0001, 0x0004)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x46),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_1F(0x64, 0x00000064)
    Event(0, func_18_42BB)

    def _loc_67A(): pass

    label('loc_67A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_6F5',
    )

    ChrClearFlags(0x0016, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_696',
    )

    ChrClearFlags(0x0017, 0x0080)

    Jump('loc_6F2')

    def _loc_696(): pass

    label('loc_696')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 0, 0x20E0)),
            Expr.Return,
        ),
        'loc_6BD',
    )

    ChrSetChipByIndex(0x0016, 42)
    ChrSetPos(0x0016, -8170, 500, 40910, 180)
    CreateThread(0x0016, 0x00, 0x00, func_02_80D)

    Jump('loc_6DC')

    def _loc_6BD(): pass

    label('loc_6BD')

    ChrSetChipByIndex(0x0016, 44)
    ChrSetFlags(0x0016, 0x0010)
    TerminateThread(0x0016, 0x00)
    ChrSetPos(0x0016, -45020, -2000, 38510, 180)

    def _loc_6DC(): pass

    label('loc_6DC')

    ChrSetPos(0x0015, -22540, 0, 47490, 180)
    ChrClearFlags(0x0015, 0x0080)

    def _loc_6F2(): pass

    label('loc_6F2')

    Jump('loc_751')

    def _loc_6F5(): pass

    label('loc_6F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 3, 0x1C03)),
            Expr.Return,
        ),
        'loc_6FF',
    )

    Jump('loc_751')

    def _loc_6FF(): pass

    label('loc_6FF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_724',
    )

    ChrClearFlags(0x001C, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrSetPos(0x0013, 2440, -2000, 38510, 159)

    Jump('loc_751')

    def _loc_724(): pass

    label('loc_724')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_740',
    )

    ChrClearFlags(0x0015, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034A, 3, 0x1A53)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_73D',
    )

    ChrSetFlags(0x0015, 0x0010)

    def _loc_73D(): pass

    label('loc_73D')

    Jump('loc_751')

    def _loc_740(): pass

    label('loc_740')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_751',
    )

    ChrClearFlags(0x0013, 0x0080)
    ChrClearFlags(0x0014, 0x0080)

    def _loc_751(): pass

    label('loc_751')

    Return()

# id: 0x0001 offset: 0x752
@scena.Code('func_01_752')
def func_01_752():
    OP_16(0x02, 4000, -145000, -73000, 2293830)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_790',
    )

    OP_B1('T1500_n')
    OP_71(0x0000, 0x0004)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 0, 0x20E0)),
            Expr.Return,
        ),
        'loc_783',
    )

    Jump('loc_78D')

    def _loc_783(): pass

    label('loc_783')

    LoadChip('ED6_DT06/CH20092._CH', 'ED6_DT06/CH20092P._CP', 44)

    def _loc_78D(): pass

    label('loc_78D')

    Jump('loc_7BF')

    def _loc_790(): pass

    label('loc_790')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_7A3',
    )

    OP_B1('T1500_n')

    Jump('loc_7BF')

    def _loc_7A3(): pass

    label('loc_7A3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 3, 0x1C03)),
            Expr.Return,
        ),
        'loc_7B6',
    )

    OP_B1('T1500_y')

    Jump('loc_7BF')

    def _loc_7B6(): pass

    label('loc_7B6')

    OP_B1('T1500_n')

    def _loc_7BF(): pass

    label('loc_7BF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 2, 0x1C02)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7F2',
    )

    OP_65(0x00, 0x0001)
    OP_65(0x01, 0x0001)
    OP_65(0x02, 0x0001)
    OP_10(0x02, 0x00)
    OP_10(0x03, 0x00)
    OP_10(0x04, 0x00)
    OP_72(0x0004, 0x0010)
    OP_72(0x0005, 0x0010)
    OP_72(0x0006, 0x0010)

    Jump('loc_807')

    def _loc_7F2(): pass

    label('loc_7F2')

    OP_64(0x00, 0x0001)
    OP_64(0x01, 0x0001)
    OP_64(0x02, 0x0001)
    OP_10(0x02, 0x01)
    OP_10(0x03, 0x01)
    OP_10(0x04, 0x01)

    def _loc_807(): pass

    label('loc_807')

    PlaySE(460, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x80D
@scena.Code('func_02_80D')
def func_02_80D():
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
        'loc_832',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_974')

    def _loc_832(): pass

    label('loc_832')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_84B',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_974')

    def _loc_84B(): pass

    label('loc_84B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_864',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_974')

    def _loc_864(): pass

    label('loc_864')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_87D',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_974')

    def _loc_87D(): pass

    label('loc_87D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_896',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_974')

    def _loc_896(): pass

    label('loc_896')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8AF',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_974')

    def _loc_8AF(): pass

    label('loc_8AF')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8C8',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_974')

    def _loc_8C8(): pass

    label('loc_8C8')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8E1',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_974')

    def _loc_8E1(): pass

    label('loc_8E1')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8FA',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_974')

    def _loc_8FA(): pass

    label('loc_8FA')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_913',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_974')

    def _loc_913(): pass

    label('loc_913')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_92C',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_974')

    def _loc_92C(): pass

    label('loc_92C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_945',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_974')

    def _loc_945(): pass

    label('loc_945')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_95E',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_974')

    def _loc_95E(): pass

    label('loc_95E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_974',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_974(): pass

    label('loc_974')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_989',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_974')

    def _loc_989(): pass

    label('loc_989')

    Return()

# id: 0x0003 offset: 0x98A
@scena.Code('func_03_98A')
def func_03_98A():
    TalkBegin(0x001C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_9E7',
    )

    ChrTalk(
        0x00FE,
        (
            '只有钓鱼是\n',
            '无论如何都不能停止的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我想就算被婆婆质问\n',
            '也会继续下去的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ACD')

    def _loc_9E7(): pass

    label('loc_9E7')

    ChrTalk(
        0x00FE,
        (
            '呼，哎呀哎呀\n',
            '终于回来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近的骚动也解决了，\n',
            '就慢慢享受钓鱼的乐趣吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀，只有钓鱼\n',
            '那可是无论如何都不会放弃的爱好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我想就算被婆婆质问\n',
            '也会继续下去的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0386, 2, 0x1C32)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AC7',
    )

    ChrTalk(
        0x0101,
        (
            '#1007F（好，好勇敢的发言呀……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AC7(): pass

    label('loc_AC7')

    SetScenaFlags(ScenaFlag(0x0386, 2, 0x1C32))
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_ACD(): pass

    label('loc_ACD')

    TalkEnd(0x001C)

    Return()

# id: 0x0004 offset: 0xAD1
@scena.Code('func_04_AD1')
def func_04_AD1():
    TalkBegin(0x0013)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_BF2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_B5B',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，多清爽的天气呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '钓鱼比赛又赢了老公，\n',
            '真是心情爽到了极点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，竟然想要向我挑战，\n',
            '还早个一百年！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BEF')

    def _loc_B5B(): pass

    label('loc_B5B')

    ChrTalk(
        0x00FE,
        (
            '呵呵，今天也是个\n',
            '清爽的天气呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和老公的旅行今天是最后一天了。\n',
            '晚上就要回王都了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为钓鱼赢了老公，\n',
            '今天可以高高兴兴地回家了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_BEF(): pass

    label('loc_BEF')

    Jump('loc_CFB')

    def _loc_BF2(): pass

    label('loc_BF2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_CFB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_C4F',
    )

    ChrTalk(
        0x00FE,
        (
            '我怎么说也是\n',
            '『钓公师团』的团员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对鱼竿的运用\n',
            '我可是很有自信的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CFB')

    def _loc_C4F(): pass

    label('loc_C4F')

    ChrTalk(
        0x00FE,
        (
            '我们是从王都\n',
            '大老远过来钓鱼的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊，我答应教老公钓鱼的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '别看我这个样子，怎么说\n',
            '我也是『钓公师团』的团员哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，对鱼竿的运用\n',
            '我可是很有自信的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_CFB(): pass

    label('loc_CFB')

    TalkEnd(0x0013)

    Return()

# id: 0x0005 offset: 0xCFF
@scena.Code('func_05_CFF')
def func_05_CFF():
    TalkBegin(0x0014)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_E08',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_D71',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，在这次旅行中\n',
            '多少要挽回些面子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是一直输给妻子\n',
            '这做丈夫的威严可就保不住了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E08')

    def _loc_D71(): pass

    label('loc_D71')

    ChrTalk(
        0x00FE,
        (
            '话说本来是我\n',
            '开始带她钓鱼的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不知什么时候\n',
            '妻子也迷上了钓鱼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '更可怕的是钓鱼技术\n',
            '已经超过我了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '稍微偷学点技术\n',
            '挽回点颜面吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_E08(): pass

    label('loc_E08')

    TalkEnd(0x0014)

    Return()

# id: 0x0006 offset: 0xE0C
@scena.Code('func_06_E0C')
def func_06_E0C():
    TalkBegin(0x0015)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 7, 0x35F)),
            Expr.Return,
        ),
        'loc_E19',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_E19(): pass

    label('loc_E19')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E95',
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
        100,
        0,
        (
            TXT(0x00, '【◇在前篇遇到过斯丁克】\n'),
            TXT(0x01, '【◇在前篇没遇到过斯丁克】\n'),
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
        (0x00000000, 'loc_E89'),
        (0x00000001, 'loc_E8F'),
        (-1, 'loc_E95'),
    )

    def _loc_E89(): pass

    label('loc_E89')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_E95')

    def _loc_E8F(): pass

    label('loc_E8F')

    ClearScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_E95')

    def _loc_E95(): pass

    label('loc_E95')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1DF2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034A, 3, 0x1A53)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1339',
    )

    ChrTalk(
        0x00FE,
        (
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1048',
    )

    ChrTalk(
        0x0101,
        (
            '#1000F啊、你是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '斯丁克……对吧？\n',
            '柏斯支部的游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '你是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '卢格兰老爷子提到的那个\n',
            '那个正游击士的新人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011F卢格兰爷爷说的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1041F这样的话，大概\n',
            '说的是我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们在之前龙的骚动中\n',
            '帮助过我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……非常感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F唔，那种情况下是当然的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近在拉文努村\n',
            '似乎没发生什么混乱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们就\n',
            '专心完成自己的工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1330')

    def _loc_1048(): pass

    label('loc_1048')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1099',
    )

    ChrTalk(
        0x0103,
        (
            '#020F好久不见，斯丁克。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x00FE, 0x0103, 400)

    Jump('loc_10F3')

    def _loc_1099(): pass

    label('loc_1099')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_10EC',
    )

    ChrTalk(
        0x0106,
        (
            '#050F很久不见了，斯丁克。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x00FE, 0x0106, 400)

    Jump('loc_10F3')

    def _loc_10EC(): pass

    label('loc_10EC')

    ChrTurnDirection(0x00FE, 0x0101, 400)

    def _loc_10F3(): pass

    label('loc_10F3')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1176',
    )

    ChrTalk(
        0x00FE,
        (
            '雪拉扎德吗…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们在之前龙的骚动中\n',
            '帮助过我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……非常感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F不，那种情况下是当然的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12E4')

    def _loc_1176(): pass

    label('loc_1176')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_11F9',
    )

    ChrTalk(
        0x00FE,
        (
            '阿加特吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们在之前龙的骚动中\n',
            '帮助过我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……非常感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#051F哪里，那是我们的义务啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12E4')

    def _loc_11F9(): pass

    label('loc_11F9')

    ChrTalk(
        0x00FE,
        (
            '你是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '卢格兰老爷子提到的那个\n',
            '那个正游击士的新人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011F卢格兰爷爷说的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1041F这样的话，大概\n',
            '我想是我们的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们在之前龙的骚动中\n',
            '帮助过我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……非常感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F唔，那种情况下是当然的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12E4(): pass

    label('loc_12E4')

    ChrTalk(
        0x00FE,
        (
            '最近在柏斯地区\n',
            '似乎没发生什么混乱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们就\n',
            '专心完成自己的工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1330(): pass

    label('loc_1330')

    SetScenaFlags(ScenaFlag(0x034A, 3, 0x1A53))
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_1DEF')

    def _loc_1339(): pass

    label('loc_1339')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_138F',
    )

    ChrTalk(
        0x00FE,
        (
            '最近在柏斯地区\n',
            '似乎没发生什么混乱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们就\n',
            '专心完成自己的工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DEF')

    def _loc_138F(): pass

    label('loc_138F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0408, 1, 0x2041)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D20',
    )

    EventBegin(0x00)
    ChrSetDirection(0x00FE, 180, 0)
    Fade(1000)
    CameraMove(-22140, 200, 48600, 0)
    OP_67(0, 7870, -10000, 0)
    CameraSetDistance(2650, 0)
    OP_6C(195000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, -21550, 0, 48540, 180)
    ChrSetPos(0x0102, -22930, 0, 48980, 180)
    ChrSetPos(0x00F8, -21110, 0, 50050, 180)
    ChrSetPos(0x00F9, -22490, 0, 50460, 180)
    OP_0D()

    ChrTalk(
        0x00FE,
        (
            '…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '<FIXME>ふむ、お前たちか……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00FE, 0, 400)
    Sleep(400)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_14C2',
    )

    ChrTalk(
        0x0106,
        (
            '#051F相変わらずだな、スティング。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            'ふ……これも性分でな。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_156E')

    def _loc_14C2(): pass

    label('loc_14C2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1514',
    )

    ChrTalk(
        0x0103,
        (
            '#020F相変わらずね、スティング。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            'ふ……これも性分でな。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_156E')

    def _loc_1514(): pass

    label('loc_1514')

    ChrTalk(
        0x0101,
        (
            '#1000Fこんにちは、スティングさん。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040Fお疲れ様です。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            'ああ……互いにな。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_156E(): pass

    label('loc_156E')

    OP_62(0x00FE, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1500)

    OP_63(0x00FE)
    Sleep(500)

    ChrTalk(
        0x00FE,
        (
            'そうだ、突然で悪いが\n',
            'お前たち……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            'こいつを見てくれないか？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1004Fえ……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            'スティングから\n',
            '黒光りする宝玉を見せてもらった。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    Sleep(500)

    ChrTalk(
        0x00FE,
        (
            '見た所、クオーツの\n',
            '類だとは思うんだが……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            'どうもオーブメントに\n',
            '嵌められそうになくてな。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015Fヨシュア、あれって……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1035Fうん、おそらく古代に\n',
            '使われていたクオーツだろうね。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            'ふむ、話には聞いていたが\n',
            'こいつがそうなのか……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '確かスロットを強化すれば、\n',
            '組み込めるという話だったな。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011Fうん、そうだけど……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1015Fスティングさんは一体\n',
            'どこでそれを手に入れたの？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            'ああ、実は……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '琥珀の塔の近くだったか……\n',
            '何とも変わった魔獣に出会ってな。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            'そいつを倒した時に拾ったんだ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '生きた化石というか……\n',
            'そんな感じの姿をした魔獣だった。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0420, 0, 0x2100)),
            (Expr.TestScenaFlags, ScenaFlag(0x0420, 1, 0x2101)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x0420, 2, 0x2102)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x0420, 3, 0x2103)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1933',
    )

    ChrTalk(
        0x0101,
        (
            '#1004Fそれって、もしかして……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1042Fうん、塔の屋上で倒した\n',
            '魔獣と同じ類かもしれない。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            'ほう、お前たちも\n',
            '遭遇していたか……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19BB')

    def _loc_1933(): pass

    label('loc_1933')

    ChrTalk(
        0x0101,
        (
            '#1002Fそれって、まさか……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1042Fうん、《裏の塔》が出現した\n',
            '影響かもしれない。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '《裏の塔》……\n',
            'あの時の異常事態のことか。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19BB(): pass

    label('loc_19BB')

    ChrTalk(
        0x00FE,
        (
            '……ともかく、俺の方では\n',
            'それっきり姿を見ていない。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            'ただ……そこらの魔獣に比べて\n',
            'かなり強力だったことは確かだ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '用心するに\n',
            '越したことはないだろう。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1002Fう、うん……そうね。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            'ふむ……そうだな。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.Item, ItemTable['驱动３']),
            (TxtCtl.SetColor, 0x0),
            'を受け取った。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    AddItem(ItemTable['驱动３'], 1)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0101,
        (
            '#1004Fえ……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1044Fスティングさん？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            'オーブメントの使えない今、\n',
            'それは俺にとって無用の長物……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            'だが聞けば、お前たちの任務には\n',
            'オーブメントが役に立つ……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……だったら、\n',
            '導き出される答えは一つだ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1004Fあ……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1C2A',
    )

    ChrTalk(
        0x0106,
        (
            '#051Fへっ、随分と\n',
            '気が利いているじゃねえか。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C96')

    def _loc_1C2A(): pass

    label('loc_1C2A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1C67',
    )

    ChrTalk(
        0x0103,
        (
            '#027Fふふ、随分と\n',
            '気が利いているわね。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C96')

    def _loc_1C67(): pass

    label('loc_1C67')

    ChrTalk(
        0x0102,
        (
            '#1040Fすみません、\n',
            'ありがとうございます。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C96(): pass

    label('loc_1C96')

    ChrTalk(
        0x00FE,
        (
            '……礼には及ばん。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            'お前たちは自分の責務を\n',
            '果たすことだけ考えろ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006Fうん……！\n',
            'ありがとう、スティングさん。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0408, 1, 0x2041))
    EventEnd(0x00)
    OP_4B(0x00FE, 255)

    Jump('loc_1DEF')

    def _loc_1D20(): pass

    label('loc_1D20')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1DA1',
    )

    ChrTalk(
        0x00FE,
        (
            '导力器停止现象\n',
            '是在王国全境发生的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个状况要\n',
            '持续到什么时候呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过……\n',
            '就现状也是毫无办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Jump('loc_1DEF')

    def _loc_1DA1(): pass

    label('loc_1DA1')

    ChrTalk(
        0x00FE,
        (
            '这样的状况拖太久的话\n',
            '就非常危险了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过……\n',
            '就现状也是毫无办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1DEF(): pass

    label('loc_1DEF')

    Jump('loc_216A')

    def _loc_1DF2(): pass

    label('loc_1DF2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_216A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034A, 3, 0x1A53)),
            Expr.Return,
        ),
        'loc_1F09',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1ECB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1E4D',
    )

    ChrTalk(
        0x00FE,
        (
            '琐碎的事\n',
            '就由我来做吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……龙的事情就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EC8')

    def _loc_1E4D(): pass

    label('loc_1E4D')

    ChrTalk(
        0x00FE,
        (
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们和军队协力\n',
            '一起追捕龙呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '琐碎的事\n',
            '就由我来做吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……那边就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_1EC8(): pass

    label('loc_1EC8')

    Jump('loc_1F06')

    def _loc_1ECB(): pass

    label('loc_1ECB')

    ChrTalk(
        0x00FE,
        (
            '琐碎的事\n',
            '就由我来做吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……龙的事情就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1F06(): pass

    label('loc_1F06')

    Jump('loc_216A')

    def _loc_1F09(): pass

    label('loc_1F09')

    ChrTalk(
        0x00FE,
        (
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1FD7',
    )

    ChrTalk(
        0x0101,
        (
            '#1011F啊、你是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '斯丁克……对吧？\n',
            '柏斯支部的游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '你是……\n',
            '那时的准游击士吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '噢，看样子已经升任正游击士了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2026')

    def _loc_1FD7(): pass

    label('loc_1FD7')

    ChrTalk(
        0x0101,
        (
            '#1015F（啊？这个人……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '（仔细看看的话，\n',
            '　竟然也戴着游击士的徽章啊？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2026(): pass

    label('loc_2026')

    ChrTalk(
        0x0106,
        (
            '#050F很久不见了，斯丁克。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '竟然来到这种地方，\n',
            '今天来是消灭通缉魔兽的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_63(0x00FE)
    ChrTurnDirection(0x00FE, 0x0106, 400)

    ChrTalk(
        0x00FE,
        (
            '阿加特……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是来调查龙的事件吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#050F啊啊，和军队一起。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '从这里出发\n',
            '向迷雾峡谷方向移动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '琐碎的事\n',
            '就由我来做吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……那边就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#051F喔，就交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x034A, 3, 0x1A53))
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_216A(): pass

    label('loc_216A')

    TalkEnd(0x0015)

    Return()

# id: 0x0007 offset: 0x216E
@scena.Code('func_07_216E')
def func_07_216E():
    TalkBegin(0x0016)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_23C8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 0, 0x20E0)),
            Expr.Return,
        ),
        'loc_22DF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2251',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，真没想到\n',
            '能钓到瓦雷利亚湖的『湖之主』呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，钓鱼就是和自然战斗，\n',
            '并且是一种挑战自我的过程。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算没有『湖之主』\n',
            '挑战的对手也数以万计。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对了，去外国远征\n',
            '说不定也可以呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    Jump('loc_22DC')

    def _loc_2251(): pass

    label('loc_2251')

    ChrTalk(
        0x00FE,
        (
            '就算没有『湖之主』\n',
            '挑战的对手也数以万计。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '钓鱼就是和自然战斗，\n',
            '并且是一种挑战自我的过程。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对了，去外国远征\n',
            '说不定也不错呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_22DC(): pass

    label('loc_22DC')

    Jump('loc_23C5')

    def _loc_22DF(): pass

    label('loc_22DF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_238E',
    )

    ChrTalk(
        0x00FE,
        (
            '………………………………\n',
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……喂，来吧……………\n',
            '瓦雷利亚湖的『湖之主』',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '………………………………\n',
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    Jump('loc_23C5')

    def _loc_238E(): pass

    label('loc_238E')

    ChrTalk(
        0x00FE,
        (
            '………………………………\n',
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_23C5(): pass

    label('loc_23C5')

    Jump('loc_2673')

    def _loc_23C8(): pass

    label('loc_23C8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2673',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 0, 0x20E0)),
            Expr.Return,
        ),
        'loc_250C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_248C',
    )

    ChrTalk(
        0x00FE,
        (
            '这次为了能钓上『湖之主』，\n',
            '我做好充分准备来的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，没想到\n',
            '被抢先了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说实话真是受打击了呀，但是\n',
            '钓鱼并没有结束。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '必须重新振作起来\n',
            '寻找新的目标。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    Jump('loc_2509')

    def _loc_248C(): pass

    label('loc_248C')

    ChrTalk(
        0x00FE,
        (
            '没想到被抢先\n',
            '钓上『湖之主』了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说实话真是受打击呀，但是\n',
            '钓鱼并没有结束。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '必须重新振作起来\n',
            '寻找新的目标。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2509(): pass

    label('loc_2509')

    Jump('loc_2673')

    def _loc_250C(): pass

    label('loc_250C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_25E2',
    )

    ChrTalk(
        0x00FE,
        (
            '这次为了能钓上『湖之主』，\n',
            '我做好充分准备来的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那，那个浮在天空中的\n',
            '像岛一样的物体到底是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '平时经常吃的黑鲑和\n',
            '鲑鱼也都钓不到了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也许是映在湖里的影子，\n',
            '对鱼产生了影响吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    Jump('loc_2673')

    def _loc_25E2(): pass

    label('loc_25E2')

    ChrTalk(
        0x00FE,
        (
            '这次为了能钓上『湖之主』，\n',
            '我做好充分准备来的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '平时经常吃的黑鲑和\n',
            '鲑鱼也都钓不到了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔唔，这也许是场\n',
            '比试忍耐力的较量吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2673(): pass

    label('loc_2673')

    TalkEnd(0x0016)

    Return()

# id: 0x0008 offset: 0x2677
@scena.Code('func_08_2677')
def func_08_2677():
    TalkBegin(0x0017)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 6, 0x2096)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2858',
    )

    ChrTalk(
        0x00FE,
        (
            '哟，游击士们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 5, 0x2095)),
            Expr.Return,
        ),
        'loc_2714',
    )

    ChrTalk(
        0x0101,
        (
            '#1000F啊，你好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F你是来购物的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '哈哈，消息真快。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没有错。\n',
            '被他缠了好久只好答应。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27C0')

    def _loc_2714(): pass

    label('loc_2714')

    ChrTalk(
        0x0101,
        (
            '#1001F啊，你好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1004F……嗯，咦！？\n',
            '怎么会有亲卫队的人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1044F从『埃尔赛尤』\n',
            '上面来的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '没错，划船过来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '其实我是被赶出来\n',
            '采购食物的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_27C0(): pass

    label('loc_27C0')

    ChrTalk(
        0x0101,
        (
            '#1016F啊哈哈，是这样呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '我是工作的时候\n',
            '被硬拉过来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本来这是利奥的工作，\n',
            '但那家伙跑了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈，我也真是\n',
            '个苯好人呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0412, 6, 0x2096))

    Jump('loc_28CF')

    def _loc_2858(): pass

    label('loc_2858')

    ChrTalk(
        0x00FE,
        (
            '不过，话说回来\n',
            '艾柯那家伙真慢呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过是买些食物，\n',
            '怎么会买这么久呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是，正是因为这样\n',
            '我才不想去的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_28CF(): pass

    label('loc_28CF')

    TalkEnd(0x0017)

    Return()

# id: 0x0009 offset: 0x28D3
@scena.Code('func_09_28D3')
def func_09_28D3():
    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上着锁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

# id: 0x000A offset: 0x291B
@scena.Code('func_0A_291B')
def func_0A_291B():
    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上着锁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

# id: 0x000B offset: 0x2963
@scena.Code('func_0B_2963')
def func_0B_2963():
    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上着锁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

# id: 0x000C offset: 0x29AB
@scena.Code('func_0C_29AB')
def func_0C_29AB():
    EventBegin(0x00)
    OP_DB()
    OP_72(0x0001, 0x0004)
    OP_71(0x0001, 0x0040)
    OP_72(0x0008, 0x0004)
    OP_71(0x0008, 0x0040)
    OP_71(0x0003, 0x0004)
    OP_A1(0x0010, 0x0008)
    OP_A1(0x0011, 0x0001)
    ChrSetFlags(0x0010, 0x0040)
    ChrSetFlags(0x0011, 0x0040)
    ChrSetPos(0x0010, -8530, -2500, 32509, 0)
    ChrSetPos(0x0011, -6040, -2500, 32020, 0)
    ChrClearFlags(0x000A, 0x0004)
    ChrClearFlags(0x000C, 0x0004)
    ChrClearFlags(0x0009, 0x0004)
    ChrClearFlags(0x000E, 0x0004)
    ChrClearFlags(0x000B, 0x0004)
    ChrClearFlags(0x000F, 0x0004)
    ChrClearFlags(0x0008, 0x0004)
    ChrClearFlags(0x000D, 0x0004)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetFlags(0x001C, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    ChrClearFlags(0x000A, 0x0001)
    ChrClearFlags(0x000C, 0x0001)
    ChrClearFlags(0x0009, 0x0001)
    ChrClearFlags(0x000E, 0x0001)
    ChrClearFlags(0x000B, 0x0001)
    ChrClearFlags(0x000F, 0x0001)
    ChrClearFlags(0x0008, 0x0001)
    ChrClearFlags(0x000D, 0x0001)
    ChrSetBattleFlags(0x000A, 0x0020)
    ChrSetBattleFlags(0x000C, 0x0020)
    ChrSetBattleFlags(0x0009, 0x0020)
    ChrSetBattleFlags(0x000E, 0x0020)
    ChrSetBattleFlags(0x000B, 0x0020)
    ChrSetBattleFlags(0x000F, 0x0020)
    ChrSetBattleFlags(0x0008, 0x0020)
    ChrSetBattleFlags(0x000D, 0x0020)
    ChrSetChipByIndex(0x0101, 1)
    ChrSetChipByIndex(0x000A, 0)
    Yield()
    OP_89(0x000A, -6050, -2400, 29730, 180)
    OP_89(0x000C, -6520, -2400, 31060, 180)
    OP_89(0x0009, -5840, -2400, 30990, 180)
    OP_89(0x000D, -6350, -2400, 32350, 180)
    OP_89(0x0101, -8940, -2400, 31400, 180)
    OP_89(0x000B, -8270, -2400, 31410, 180)
    OP_89(0x000E, -8950, -2400, 32740, 180)
    OP_89(0x000F, -8450, -2400, 30470, 0)
    OP_89(0x0008, -8280, -2400, 32740, 180)
    CameraMove(-6750, -2800, 30900, 0)
    OP_67(0, 9030, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(32000, 0)
    OP_6E(280, 0)

    @scena.Lambda('lambda_2B8E')
    def lambda_2B8E():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_2B8E')

    DispatchAsync2(0x000A, 0x0002, lambda_2B8E)

    LoadEffect(0x00, 'map\\\\mp013_00.eff')
    LoadEffect(0x01, 'map\\\\mp013_01.eff')
    PlayEffect(0x00, 0x00, 0x0010, 0, -300, 2200, 180, 0, 0, 600, 100, 3000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0x01, 0x0010, 0, -300, -1800, 180, 0, 0, 700, 700, 700, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0x02, 0x0011, 0, -300, 2200, 180, 0, 0, 600, 100, 3000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0x03, 0x0011, 0, -300, -1800, 180, 0, 0, 700, 700, 700, 0x00FF, 0, 0, 0, 0)
    FadeIn(1000, 0)
    Sleep(300)

    PlaySE(146, 0x00, 0x46)

    @scena.Lambda('lambda_2CB0')
    def lambda_2CB0():
        CameraMove(-5900, -2530, 24130, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2CB0)

    @scena.Lambda('lambda_2CC8')
    def lambda_2CC8():
        OP_67(0, 11840, -10000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2CC8)

    @scena.Lambda('lambda_2CE0')
    def lambda_2CE0():
        OP_6C(49000, 10000)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_2CE0)

    @scena.Lambda('lambda_2CF0')
    def lambda_2CF0():
        OP_6E(298, 10000)

        ExitThread()

    DispatchAsync(0x0010, 0x0003, lambda_2CF0)

    CreateThread(0x0010, 0x00, 0x00, func_13_3B41)
    Sleep(200)

    CreateThread(0x0011, 0x00, 0x00, func_14_3C9D)
    WaitForThreadExit(0x0010, 0x0001)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_23(0x0092)
    OP_DC()
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '上午，租借了小船\n',
            '在湖上戏耍，十分开心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TerminateThread(0x000A, 0x02)
    OP_DB()
    ChrClearFlags(0x0101, 0x0020)
    ChrClearFlags(0x000A, 0x0020)
    ChrClearFlags(0x000C, 0x0020)
    ChrClearFlags(0x0009, 0x0020)
    ChrClearFlags(0x000E, 0x0020)
    ChrClearFlags(0x000B, 0x0020)
    ChrClearFlags(0x000F, 0x0020)
    ChrSetFlags(0x000A, 0x0001)
    ChrSetFlags(0x000C, 0x0001)
    ChrSetFlags(0x0009, 0x0001)
    ChrSetFlags(0x000E, 0x0001)
    ChrSetFlags(0x000B, 0x0001)
    ChrSetFlags(0x000F, 0x0001)
    ChrSetFlags(0x0008, 0x0001)
    ChrSetFlags(0x000D, 0x0001)
    ChrClearBattleFlags(0x000A, 0x0020)
    ChrClearBattleFlags(0x000C, 0x0020)
    ChrClearBattleFlags(0x0009, 0x0020)
    ChrClearBattleFlags(0x000E, 0x0020)
    ChrClearBattleFlags(0x000B, 0x0020)
    ChrClearBattleFlags(0x000F, 0x0020)
    ChrClearBattleFlags(0x0008, 0x0020)
    ChrClearBattleFlags(0x000D, 0x0020)
    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x0008, 0)
    ChrSetSubChip(0x0009, 0)
    ChrSetSubChip(0x000A, 0)
    ChrSetSubChip(0x000B, 0)
    ChrSetSubChip(0x000C, 0)
    ChrSetSubChip(0x000D, 0)
    ChrSetSubChip(0x000E, 0)
    ChrSetChipByIndex(0x0101, 1)
    ChrSetChipByIndex(0x0008, 2)
    ChrSetChipByIndex(0x0009, 27)
    ChrSetChipByIndex(0x000A, 4)
    ChrSetChipByIndex(0x000B, 5)
    ChrSetChipByIndex(0x000C, 6)
    ChrSetChipByIndex(0x000D, 14)
    ChrSetChipByIndex(0x000E, 8)
    ChrSetSubChip(0x000B, 2)
    ChrSetSubChip(0x000C, 2)
    ChrSetPos(0x0101, -900, -650, 43530, 90)
    ChrSetPos(0x0008, -1320, -400, 42540, 90)
    ChrSetPos(0x000A, -1370, -650, 41510, 90)
    ChrSetPos(0x000B, 660, -1800, 48640, 90)
    ChrSetPos(0x000C, 660, -1800, 47590, 90)
    ChrSetPos(0x000E, -1010, -650, 44400, 90)
    ChrSetFlags(0x0009, 0x0800)
    ChrSetPos(0x0009, 2350, -2000, 40500, 0)
    ChrSetPos(0x000D, 2390, -2000, 45720, 180)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetChipByIndex(0x0009, 27)
    CameraMove(1600, -1260, 44290, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(295000, 0)
    OP_6E(272, 0)
    LoadEffect(0x00, 'scraft\\\\sc000_00.eff')
    LoadEffect(0x01, 'scraft\\\\sc000_11.eff')
    FadeIn(1000, 0)
    OP_0D()

    @scena.Lambda('lambda_2F58')
    def lambda_2F58():
        CameraMove(2290, -1260, 42460, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2F58)

    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0009, 31)
    ChrSetChipByIndex(0x000D, 32)
    Sleep(1000)

    CreateThread(0x0101, 0x00, 0x00, func_0D_39D3)
    PlaySE(163, 0x00, 0x64)
    ChrJumpTo(0x000D, 1560, -2000, 44040, 350, 4000)
    PlaySE(163, 0x00, 0x64)
    ChrJumpTo(0x000D, 2650, -2000, 43190, 350, 6000)
    PlaySE(163, 0x00, 0x64)

    @scena.Lambda('lambda_2FC8')
    def lambda_2FC8():
        ChrJumpTo(0x000D, 2260, -2000, 41840, 200, 8000)

        ExitThread()

    DispatchAsync(0x000D, 0x0000, lambda_2FC8)

    Sleep(100)

    ChrSetChipByIndex(0x000D, 34)

    @scena.Lambda('lambda_2FF0')
    def lambda_2FF0():
        OP_99(0x00FE, 0x00, 0x07, 2500)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_2FF0)

    PlaySE(520, 0x00, 0x64)

    @scena.Lambda('lambda_3005')
    def lambda_3005():
        ChrTurnDirection(0x00FE, 0x000D, 0)
        Yield()

        Jump('lambda_3005')

    DispatchAsync2(0x0009, 0x0002, lambda_3005)

    @scena.Lambda('lambda_3016')
    def lambda_3016():
        ChrJumpTo(0x0009, 3180, -2000, 41080, 250, 8000)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_3016)

    ChrSetChipByIndex(0x0009, 27)
    ChrSetSubChip(0x0009, 0)
    WaitForThreadExit(0x000D, 0x0001)
    WaitForThreadExit(0x000D, 0x0000)
    ChrTurnDirection(0x000D, 0x0009, 0)

    @scena.Lambda('lambda_304F')
    def lambda_304F():
        ChrJumpTo(0x000D, 1540, -2000, 41320, 250, 6000)

        ExitThread()

    DispatchAsync(0x000D, 0x0000, lambda_304F)

    ChrSetSubChip(0x000D, 0)
    ChrSetChipByIndex(0x000D, 32)
    Sleep(100)

    TerminateThread(0x0009, 0x02)

    @scena.Lambda('lambda_3080')
    def lambda_3080():
        OP_99(0x00FE, 0x00, 0x07, 2000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_3080)

    @scena.Lambda('lambda_3090')
    def lambda_3090():
        ChrMoveTo(0x00FE, 2310, -2000, 41130, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3090)

    Sleep(100)

    PlaySE(505, 0x00, 0x64)
    Sleep(100)

    ChrJumpTo(0x000D, 2390, -2000, 42000, 250, 7000)
    ChrTurnDirection(0x000D, 0x0009, 0)
    WaitForThreadExit(0x0009, 0x0002)
    ChrTurnDirection(0x0009, 0x000D, 0)
    ChrSetChipByIndex(0x0009, 30)

    @scena.Lambda('lambda_30E9')
    def lambda_30E9():
        OP_99(0x00FE, 0x00, 0x03, 2500)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_30E9)

    WaitForThreadExit(0x0009, 0x0001)

    @scena.Lambda('lambda_30FE')
    def lambda_30FE():
        OP_99(0x00FE, 0x0A, 0x0E, 2500)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_30FE)

    Sleep(100)

    CreateThread(0x0101, 0x00, 0x00, func_0F_3A1B)
    PlayEffect(0x01, 0x00, 0x000D, 0, 500, 1000, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    ChrSetSubChip(0x000D, 0)
    ChrSetChipByIndex(0x000D, 35)
    ChrJumpTo(0x000D, 2390, -2000, 43720, 250, 5000)
    ChrSetFlags(0x000D, 0x0020)
    ChrSetChipByIndex(0x000D, 36)
    ChrSetSubChip(0x000D, 3)
    ChrMoveTo(0x000D, 2390, -2000, 44720, 5000, 0x00)
    WaitForThreadExit(0x0009, 0x0001)
    ChrSetSubChip(0x0009, 0)
    ChrSetChipByIndex(0x0009, 26)
    ChrSetFlags(0x000D, 0x8000)
    ChrJumpTo(0x0009, 2210, -2000, 39850, 200, 4000)
    ChrSetChipByIndex(0x000D, 32)
    ChrSetSubChip(0x000D, 0)

    @scena.Lambda('lambda_31C8')
    def lambda_31C8():
        ChrMoveTo(0x0009, 2190, -2000, 42890, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_31C8)

    Sleep(300)

    PlaySE(163, 0x00, 0x64)

    @scena.Lambda('lambda_31ED')
    def lambda_31ED():
        ChrJumpTo(0x00FE, 2160, -2000, 43720, 400, 6000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_31ED)

    ChrSetChipByIndex(0x0009, 27)

    @scena.Lambda('lambda_3210')
    def lambda_3210():
        OP_99(0x0009, 0x00, 0x07, 2500)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3210)

    Sleep(100)

    PlaySE(505, 0x00, 0x64)
    Sleep(200)

    @scena.Lambda('lambda_322F')
    def lambda_322F():
        ChrSetDirection(0x00FE, 270, 800)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_322F)

    @scena.Lambda('lambda_323D')
    def lambda_323D():
        ChrMoveTo(0x00FE, 2690, -2000, 44580, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_323D)

    WaitForThreadExit(0x0009, 0x0001)
    ChrTurnDirection(0x0009, 0x000D, 0)
    ChrSetChipByIndex(0x0009, 30)

    @scena.Lambda('lambda_3269')
    def lambda_3269():
        OP_99(0x00FE, 0x00, 0x03, 2500)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3269)

    WaitForThreadExit(0x0009, 0x0001)

    @scena.Lambda('lambda_327E')
    def lambda_327E():
        OP_99(0x00FE, 0x0A, 0x0E, 2500)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_327E)

    @scena.Lambda('lambda_328E')
    def lambda_328E():
        ChrTurnDirection(0x000D, 0x0009, 0)

        ExitThread()

    DispatchAsync(0x000D, 0x0003, lambda_328E)

    Sleep(100)

    PlaySE(505, 0x00, 0x64)
    PlaySE(163, 0x00, 0x64)
    ChrSetFlags(0x000D, 0x0004)

    @scena.Lambda('lambda_32B0')
    def lambda_32B0():
        ChrJumpTo(0x000D, 3200, -1300, 46770, 1000, 6000)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_32B0)

    WaitForThreadExit(0x000D, 0x0002)
    CreateThread(0x0101, 0x00, 0x00, func_0E_39F7)
    Sleep(100)

    WaitForThreadExit(0x0009, 0x0001)
    ChrSetSubChip(0x0009, 0)
    ChrSetChipByIndex(0x0009, 31)
    ChrTurnDirection(0x0009, 0x000D, 0)
    ChrSetChipByIndex(0x000D, 34)
    PlaySE(163, 0x00, 0x64)

    @scena.Lambda('lambda_32FF')
    def lambda_32FF():
        ChrJumpTo(0x000D, 2200, -2000, 44340, 200, 7000)

        ExitThread()

    DispatchAsync(0x000D, 0x0000, lambda_32FF)

    Sleep(100)

    @scena.Lambda('lambda_3322')
    def lambda_3322():
        OP_99(0x00FE, 0x00, 0x07, 2000)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_3322)

    Sleep(100)

    PlaySE(507, 0x00, 0x64)
    OP_7C(100, 0, 5000, 1000)
    PlayEffect(0x01, 0x00, 0x0009, 0, 1000, -500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    ChrSetFlags(0x0009, 0x0020)
    CreateThread(0x0101, 0x00, 0x00, func_0F_3A1B)
    ChrMoveTo(0x0009, 1800, -2000, 42900, 6000, 0x00)
    WaitForThreadExit(0x000D, 0x0001)
    CreateThread(0x0101, 0x00, 0x00, func_10_3A3F)
    PlaySE(163, 0x00, 0x64)

    @scena.Lambda('lambda_33B3')
    def lambda_33B3():
        ChrJumpTo(0x00FE, 2070, -2000, 43670, 199, 0)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_33B3)

    ChrSetFlags(0x000D, 0x0010)
    ChrSetFlags(0x000D, 0x0020)
    ChrSetFlags(0x000D, 0x0002)
    ChrSetChipByIndex(0x000D, 37)
    ChrSetSubChip(0x000D, 0)
    OP_99(0x000D, 0x01, 0x03, 1800)

    @scena.Lambda('lambda_33F3')
    def lambda_33F3():
        OP_9E(0x00FE, 50, 0, 500, 2000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_33F3)

    OP_7C(100, 0, 5000, 1000)
    PlayEffect(0x01, 0x00, 0x0009, 0, 1300, 300, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    CreateThread(0x0106, 0x03, 0x00, func_12_3AE3)

    @scena.Lambda('lambda_345A')
    def lambda_345A():
        ChrMoveTo(0x0009, 1720, -2000, 42300, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_345A)

    Sleep(200)

    OP_7C(100, 0, 5000, 1000)

    @scena.Lambda('lambda_348B')
    def lambda_348B():
        OP_9E(0x00FE, 50, 0, 100, 5000)
        Yield()

        Jump('lambda_348B')

    DispatchAsync2(0x0009, 0x0001, lambda_348B)

    OP_99(0x000D, 0x08, 0x0B, 1500)
    OP_99(0x000D, 0x08, 0x0B, 1500)
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))
    OP_99(0x000D, 0x10, 0x12, 1500)

    @scena.Lambda('lambda_34C6')
    def lambda_34C6():
        OP_99(0x00FE, 0x18, 0x1B, 2000)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_34C6)

    PlayEffect(0x01, 0x00, 0x0009, 0, 1000, 300, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_7C(100, 0, 5000, 1000)
    PlaySE(554, 0x00, 0x64)
    PlaySE(554, 0x00, 0x64)
    PlaySE(554, 0x00, 0x64)
    ChrSetChipByIndex(0x0009, 28)
    CreateThread(0x0009, 0x01, 0x00, func_11_3A4F)
    WaitForThreadExit(0x000D, 0x0002)
    ChrSetSubChip(0x000D, 32)
    ChrClearFlags(0x000D, 0x0004)
    TerminateThread(0x000D, 0xFF)

    @scena.Lambda('lambda_354A')
    def lambda_354A():
        ChrJumpTo(0x00FE, 2200, -2000, 44340, 500, 4000)

        ExitThread()

    DispatchAsync(0x000D, 0x0000, lambda_354A)

    @scena.Lambda('lambda_3568')
    def lambda_3568():
        OP_99(0x00FE, 0x28, 0x2C, 1500)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_3568)

    WaitForThreadExit(0x000D, 0x0000)
    PlaySE(164, 0x00, 0x64)
    WaitForThreadExit(0x000D, 0x0002)
    ChrClearFlags(0x000D, 0x0002)
    ChrClearFlags(0x000D, 0x0010)
    ChrClearFlags(0x000D, 0x0040)
    ChrSetDirection(0x000D, 180, 0)
    ChrSetChipByIndex(0x000D, 32)
    ChrSetSubChip(0x000D, 0)
    WaitForThreadExit(0x0009, 0x0001)
    Sleep(1000)

    @scena.Lambda('lambda_35B1')
    def lambda_35B1():
        OP_9E(0x00FE, 30, 0, 5000, 2000)
        Yield()

        Jump('lambda_35B1')

    DispatchAsync2(0x0009, 0x0003, lambda_35B1)

    Sleep(200)

    OP_99(0x0009, 0x03, 0x00, 1500)
    Fade(250)
    TerminateThread(0x0009, 0x03)
    ChrSetFlags(0x0009, 0x0002)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0009, 31)
    ChrSetSubChip(0x0009, 3)
    OP_0D()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_DC()
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '中午，大家一起吃过午饭后，\n',
            '开心地做健身运动……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    ChrClearFlags(0x0009, 0x0002)
    ChrClearFlags(0x0009, 0x0800)
    ChrClearFlags(0x000D, 0x8000)
    OP_DB()
    OP_71(0x0001, 0x0004)
    OP_71(0x0003, 0x0004)
    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x000E, 0)
    ChrSetSubChip(0x000D, 0)
    ChrSetSubChip(0x0009, 0)
    ChrSetChipByIndex(0x0101, 21)
    ChrSetChipByIndex(0x000E, 24)
    ChrSetChipByIndex(0x000D, 23)
    ChrSetChipByIndex(0x0009, 22)
    ChrSetPos(0x0018, -11490, 1100, 41030, 0)
    ChrSetPos(0x0019, -10530, 1100, 41040, 0)
    ChrSetPos(0x001A, -5850, 1100, 41090, 0)
    ChrSetPos(0x001B, -4630, 1100, 41090, 0)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    ChrClearFlags(0x001A, 0x0080)
    ChrClearFlags(0x001B, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetFlags(0x0101, 0x0040)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetFlags(0x000A, 0x0004)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetFlags(0x000B, 0x0004)
    ChrSetFlags(0x000C, 0x0004)
    ChrSetPos(0x000D, -11840, -2300, 33400, 270)
    ChrSetPos(0x0101, -10130, -2300, 33190, 90)
    ChrSetPos(0x000E, -3920, -2300, 34150, 270)
    ChrSetPos(0x0009, -2100, -2300, 33480, 90)
    ChrSetPos(0x000A, -12850, 700, 41400, 90)
    ChrSetPos(0x0008, -9540, 700, 41200, 270)
    ChrSetPos(0x000C, -6940, 700, 41230, 90)
    ChrSetPos(0x000B, -3850, 700, 41270, 270)
    ChrSetPos(0x000F, -7030, 1400, 40400, 180)
    ChrSetSubChip(0x000A, 2)
    ChrSetSubChip(0x0008, 1)
    ChrSetSubChip(0x000B, 1)
    ChrSetSubChip(0x000C, 2)
    ChrSetChipByIndex(0x000A, 4)
    ChrSetChipByIndex(0x0008, 2)
    ChrSetChipByIndex(0x000B, 5)
    ChrSetChipByIndex(0x000C, 6)
    ChrClearFlags(0x001D, 0x0080)
    ChrClearFlags(0x001E, 0x0080)
    ChrClearFlags(0x001F, 0x0080)
    ChrClearFlags(0x0020, 0x0080)
    ChrSetPos(0x001D, -10730, -2000, 33190, 0)
    ChrSetPos(0x001E, -3320, -2000, 34150, 0)
    ChrSetPos(0x001F, -2700, -2000, 33480, 0)
    ChrSetPos(0x0020, -11140, -2000, 33500, 0)
    CameraMove(-8220, -2000, 45620, 0)
    OP_67(0, 6620, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(0, 0)
    OP_6E(370, 0)
    LoadEffect(0x00, 'scraft\\\\sc001_05.eff')

    @scena.Lambda('lambda_3880')
    def lambda_3880():
        OP_99(0x00FE, 0x00, 0x03, 1500)
        Yield()

        Jump('lambda_3880')

    DispatchAsync2(0x0101, 0x0003, lambda_3880)

    @scena.Lambda('lambda_3893')
    def lambda_3893():
        OP_99(0x00FE, 0x00, 0x03, 1500)
        Yield()

        Jump('lambda_3893')

    DispatchAsync2(0x000E, 0x0003, lambda_3893)

    @scena.Lambda('lambda_38A6')
    def lambda_38A6():
        OP_99(0x00FE, 0x00, 0x03, 1500)
        Yield()

        Jump('lambda_38A6')

    DispatchAsync2(0x000D, 0x0003, lambda_38A6)

    @scena.Lambda('lambda_38B9')
    def lambda_38B9():
        OP_99(0x00FE, 0x00, 0x03, 1500)
        Yield()

        Jump('lambda_38B9')

    DispatchAsync2(0x0009, 0x0003, lambda_38B9)

    Sleep(500)

    FadeIn(1000, 0)
    OP_0D()

    @scena.Lambda('lambda_38DB')
    def lambda_38DB():
        CameraMove(-7960, -2300, 38310, 6000)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_38DB)

    @scena.Lambda('lambda_38F3')
    def lambda_38F3():
        OP_67(0, 4840, -10000, 6000)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_38F3)

    @scena.Lambda('lambda_390B')
    def lambda_390B():
        OP_6C(341000, 6000)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_390B)

    @scena.Lambda('lambda_391B')
    def lambda_391B():
        OP_6E(465, 6000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_391B)

    WaitForThreadExit(0x000D, 0x0001)
    Sleep(1000)

    OP_DC()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '下午，一边垂钓\n',
            '一边悠闲地度过时间……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    FadeOut(2000, 0, -1)
    OP_0D()
    Sleep(1000)

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '快乐又安稳的时间\n',
            '很快就过去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    NewScene('ED6_DT21/T1510._SN', 111, 0, 0)
    IdleLoop()

    Return()

# id: 0x000D offset: 0x39D3
@scena.Code('func_0D_39D3')
def func_0D_39D3():
    ChrSetSubChip(0x000E, 2)
    Sleep(100)

    ChrSetSubChip(0x0101, 2)
    Sleep(100)

    ChrSetSubChip(0x0008, 2)
    Sleep(100)

    ChrSetSubChip(0x000A, 2)

    Return()

# id: 0x000E offset: 0x39F7
@scena.Code('func_0E_39F7')
def func_0E_39F7():
    ChrSetSubChip(0x000E, 1)
    Sleep(100)

    ChrSetSubChip(0x0101, 1)
    Sleep(100)

    ChrSetSubChip(0x0008, 1)
    Sleep(100)

    ChrSetSubChip(0x000A, 1)

    Return()

# id: 0x000F offset: 0x3A1B
@scena.Code('func_0F_3A1B')
def func_0F_3A1B():
    ChrSetSubChip(0x0101, 0)
    Sleep(100)

    ChrSetSubChip(0x0008, 0)
    Sleep(100)

    ChrSetSubChip(0x000A, 0)
    Sleep(100)

    ChrSetSubChip(0x000E, 0)

    Return()

# id: 0x0010 offset: 0x3A3F
@scena.Code('func_10_3A3F')
def func_10_3A3F():
    ChrSetSubChip(0x0101, 2)
    Sleep(100)

    ChrSetSubChip(0x000E, 2)

    Return()

# id: 0x0011 offset: 0x3A4F
@scena.Code('func_11_3A4F')
def func_11_3A4F():
    @scena.Lambda('lambda_3A55')
    def lambda_3A55():
        ChrMoveTo(0x00FE, 3040, -2000, 40840, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_3A55)

    Sleep(100)

    @scena.Lambda('lambda_3A75')
    def lambda_3A75():
        ChrMoveTo(0x00FE, 3040, -2000, 40840, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_3A75)

    Sleep(100)

    @scena.Lambda('lambda_3A95')
    def lambda_3A95():
        ChrMoveTo(0x00FE, 3040, -2000, 40840, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_3A95)

    Sleep(100)

    @scena.Lambda('lambda_3AB5')
    def lambda_3AB5():
        ChrMoveTo(0x00FE, 3040, -2000, 40840, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_3AB5)

    WaitForThreadExit(0x0009, 0x0002)
    ChrSetSubChip(0x0009, 0)
    ChrSetChipByIndex(0x0009, 29)
    OP_99(0x0009, 0x00, 0x03, 1500)

    Return()

# id: 0x0012 offset: 0x3AE3
@scena.Code('func_12_3AE3')
def func_12_3AE3():
    Sleep(200)

    def _loc_3AE8(): pass

    label('loc_3AE8')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3B40',
    )

    PlaySE(801, 0x00, 0x64)
    PlayEffect(0x01, 0x00, 0x0009, 0, 1000, 300, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_3B38',
    )

    OP_23(0x0321)

    Jump('loc_3B40')

    def _loc_3B38(): pass

    label('loc_3B38')

    Sleep(100)

    Jump('loc_3AE8')

    def _loc_3B40(): pass

    label('loc_3B40')

    Return()

# id: 0x0013 offset: 0x3B41
@scena.Code('func_13_3B41')
def func_13_3B41():
    @scena.Lambda('lambda_3B47')
    def lambda_3B47():
        ChrMoveTo(0x00FE, -10210, -2500, 13560, 100, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3B47)

    Sleep(300)

    @scena.Lambda('lambda_3B67')
    def lambda_3B67():
        ChrMoveTo(0x00FE, -10210, -2500, 13560, 300, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3B67)

    Sleep(300)

    @scena.Lambda('lambda_3B87')
    def lambda_3B87():
        ChrMoveTo(0x00FE, -10210, -2500, 13560, 500, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3B87)

    Sleep(300)

    @scena.Lambda('lambda_3BA7')
    def lambda_3BA7():
        ChrMoveTo(0x00FE, -10210, -2500, 13560, 800, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3BA7)

    Sleep(300)

    @scena.Lambda('lambda_3BC7')
    def lambda_3BC7():
        ChrMoveTo(0x00FE, -10210, -2500, 13560, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3BC7)

    Sleep(300)

    @scena.Lambda('lambda_3BE7')
    def lambda_3BE7():
        ChrMoveTo(0x00FE, -10210, -2500, 13560, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3BE7)

    Sleep(300)

    @scena.Lambda('lambda_3C07')
    def lambda_3C07():
        ChrMoveTo(0x00FE, -10210, -2500, 13560, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3C07)

    Sleep(300)

    @scena.Lambda('lambda_3C27')
    def lambda_3C27():
        ChrMoveTo(0x00FE, -10210, -2500, 13560, 1800, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3C27)

    Sleep(300)

    @scena.Lambda('lambda_3C47')
    def lambda_3C47():
        ChrMoveTo(0x00FE, -10210, -2500, 13560, 2100, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3C47)

    Sleep(300)

    @scena.Lambda('lambda_3C67')
    def lambda_3C67():
        ChrMoveTo(0x00FE, -10210, -2500, 13560, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3C67)

    Sleep(300)

    @scena.Lambda('lambda_3C87')
    def lambda_3C87():
        ChrMoveTo(0x00FE, -10210, -2500, 13560, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3C87)

    Return()

# id: 0x0014 offset: 0x3C9D
@scena.Code('func_14_3C9D')
def func_14_3C9D():
    @scena.Lambda('lambda_3CA3')
    def lambda_3CA3():
        ChrMoveTo(0x00FE, -3060, -2500, 13000, 100, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3CA3)

    Sleep(300)

    @scena.Lambda('lambda_3CC3')
    def lambda_3CC3():
        ChrMoveTo(0x00FE, -3060, -2500, 13000, 300, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3CC3)

    Sleep(300)

    @scena.Lambda('lambda_3CE3')
    def lambda_3CE3():
        ChrMoveTo(0x00FE, -3060, -2500, 13000, 500, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3CE3)

    Sleep(300)

    @scena.Lambda('lambda_3D03')
    def lambda_3D03():
        ChrMoveTo(0x00FE, -3060, -2500, 13000, 800, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3D03)

    Sleep(300)

    @scena.Lambda('lambda_3D23')
    def lambda_3D23():
        ChrMoveTo(0x00FE, -3060, -2500, 13000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3D23)

    Sleep(300)

    @scena.Lambda('lambda_3D43')
    def lambda_3D43():
        ChrMoveTo(0x00FE, -3060, -2500, 13000, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3D43)

    Sleep(300)

    @scena.Lambda('lambda_3D63')
    def lambda_3D63():
        ChrMoveTo(0x00FE, -3060, -2500, 13000, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3D63)

    Sleep(300)

    @scena.Lambda('lambda_3D83')
    def lambda_3D83():
        ChrMoveTo(0x00FE, -3060, -2500, 13000, 1800, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3D83)

    Sleep(300)

    @scena.Lambda('lambda_3DA3')
    def lambda_3DA3():
        ChrMoveTo(0x00FE, -3060, -2500, 13000, 2100, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3DA3)

    Sleep(300)

    @scena.Lambda('lambda_3DC3')
    def lambda_3DC3():
        ChrMoveTo(0x00FE, -3060, -2500, 13000, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3DC3)

    Sleep(6500)

    @scena.Lambda('lambda_3DE3')
    def lambda_3DE3():
        ChrMoveToRelativeAsync(0x00FE, 1000, 0, -10000, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3DE3)

    Return()

# id: 0x0015 offset: 0x3DF9
@scena.Code('func_15_3DF9')
def func_15_3DF9():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3E7D',
    )

    ChrSetDirection(0x00FE, 135, 0)
    Sleep(200)

    ChrSetDirection(0x00FE, 90, 0)
    Sleep(200)

    ChrSetDirection(0x00FE, 45, 0)
    Sleep(200)

    ChrSetDirection(0x00FE, 90, 0)
    Sleep(500)

    ChrSetDirection(0x00FE, 45, 0)
    Sleep(200)

    ChrSetDirection(0x00FE, 90, 0)
    Sleep(200)

    ChrSetDirection(0x00FE, 135, 0)
    Sleep(200)

    ChrSetDirection(0x00FE, 90, 0)
    Sleep(500)

    ChrSetDirection(0x00FE, 135, 0)
    Sleep(200)

    ChrSetDirection(0x00FE, 90, 0)
    Sleep(500)

    Jump('func_15_3DF9')

    def _loc_3E7D(): pass

    label('loc_3E7D')

    Return()

# id: 0x0016 offset: 0x3E7E
@scena.Code('func_16_3E7E')
def func_16_3E7E():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3F02',
    )

    ChrSetDirection(0x00FE, 315, 0)
    Sleep(300)

    ChrSetDirection(0x00FE, 270, 0)
    Sleep(300)

    ChrSetDirection(0x00FE, 225, 0)
    Sleep(200)

    ChrSetDirection(0x00FE, 270, 0)
    Sleep(180)

    ChrSetDirection(0x00FE, 225, 0)
    Sleep(400)

    ChrSetDirection(0x00FE, 270, 0)
    Sleep(250)

    ChrSetDirection(0x00FE, 315, 0)
    Sleep(400)

    ChrSetDirection(0x00FE, 270, 0)
    Sleep(350)

    ChrSetDirection(0x00FE, 315, 0)
    Sleep(250)

    ChrSetDirection(0x00FE, 270, 0)
    Sleep(400)

    Jump('func_16_3E7E')

    def _loc_3F02(): pass

    label('loc_3F02')

    Return()

# id: 0x0017 offset: 0x3F03
@scena.Code('func_17_3F03')
def func_17_3F03():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 4, 0x1C04)),
            Expr.Return,
        ),
        'loc_3F0B',
    )

    Return()

    def _loc_3F0B(): pass

    label('loc_3F0B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 3, 0x1C03)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3F14',
    )

    Return()

    def _loc_3F14(): pass

    label('loc_3F14')

    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, -44960, -2000, 41690, 180)
    CameraMove(-44990, -2000, 38500, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(312000, 0)
    OP_6E(262, 0)
    OP_69(0x0101, 0)
    OP_6A(0x0101)
    ChrWalkTo(0x0101, -44920, -2000, 38700, 1500, 0x00)
    Sleep(500)

    OP_6A(0x00FF)

    ChrTalk(
        0x0101,
        (
            '#0010320729V#1025F呼～……\n',
            '真是美丽的晚霞呀～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320730V和那时侯一样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    OP_AD('ED6_DT24/C_VIS173._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(1000)

    Sleep(2000)

    OP_AE(0x000001F4)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010320731V#1027F…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_403E')
    def lambda_403E():
        OP_67(0, 7200, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_403E)

    Sleep(1000)

    Fade(500)
    ChrSetSubChip(0x0101, 1)
    ChrSetChipByIndex(0x0101, 17)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010320732V#1003F无论是天空还是湖水还是晚霞\n',
            '都和那时侯一样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320733V和大家一起\n',
            '应当很开心才对，但是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320734V果然……完全不一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0101, 0)
    Sleep(500)

    OP_62(0x0101, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010320735V#1007F啊啊，这样可不行……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320736V好不容易找到了答案，\n',
            '要用自己的步调赶上他的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320737V这样的话，会被约修亚、\n',
            '还有母亲笑话的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0101, 1)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010320738V#1025F……对了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320739V只有上次在梦里\n',
            '成功的吹奏过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320740V再练习一下吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_DB()
    OP_20(0x000005DC)
    Sleep(1000)

    Fade(500)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0101, 18)
    OP_0D()
    Sleep(1000)

    OP_21()

    @scena.Lambda('lambda_4269')
    def lambda_4269():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_4269')

    DispatchAsync2(0x0101, 0x0000, lambda_4269)

    PlayBGM(70)
    OP_1F(0x64, 0x000000C8)

    @scena.Lambda('lambda_4284')
    def lambda_4284():
        CameraSetDistance(3200, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4284)

    Sleep(2000)

    Sleep(1500)

    Sleep(1500)

    MapSetFlags(0x02000000)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_DC()
    SetScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    NewScene('ED6_DT21/T1510._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0018 offset: 0x42BB
@scena.Code('func_18_42BB')
def func_18_42BB():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_DB()
    ChrSetPos(0x0101, -44920, -2000, 38700, 180)
    CameraMove(-44990, -2000, 38500, 0)
    OP_67(0, 7200, -10000, 0)
    CameraSetDistance(2900, 0)
    OP_6C(312000, 0)
    OP_6E(262, 0)
    ChrSetChipByIndex(0x0101, 18)

    @scena.Lambda('lambda_4321')
    def lambda_4321():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_4321')

    DispatchAsync2(0x0101, 0x0000, lambda_4321)

    FadeIn(1000, 0)
    OP_0D()
    OP_21()
    TerminateThread(0x0101, 0x00)
    Sleep(1000)

    OP_99(0x0101, 0x08, 0x09, 1500)
    Sleep(1000)

    Fade(500)
    ChrSetSubChip(0x0101, 10)
    OP_0D()
    PlaySE(123, 0x00, 0x64)
    Sleep(500)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_DC()
    ChrSetChipByIndex(0x0101, 17)
    ChrSetSubChip(0x0101, 1)

    ChrTalk(
        0x0101,
        (
            '#0010320741V#1004F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x000E, 15)
    ChrSetPos(0x000E, -40350, -2000, 48090, 188)
    ChrClearFlags(0x000E, 0x0080)

    @scena.Lambda('lambda_43CB')
    def lambda_43CB():
        CameraMove(-43510, -2000, 43790, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_43CB)

    @scena.Lambda('lambda_43E3')
    def lambda_43E3():
        OP_6C(331000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_43E3)

    Sleep(1000)

    @scena.Lambda('lambda_43F8')
    def lambda_43F8():
        ChrTurnDirection(0x0101, 0x000E, 400)
        Yield()

        Jump('lambda_43F8')

    DispatchAsync2(0x0101, 0x0003, lambda_43F8)

    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x000E,
        (
            '#0180320742V#1061F#6P嘿嘿，我听到了\n',
            '十分优美的曲调哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320743V#1015F#5P凯文先生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    PlayBGM(15)
    Sleep(500)

    @scena.Lambda('lambda_448C')
    def lambda_448C():
        CameraMove(-45120, -2000, 39640, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_448C)

    @scena.Lambda('lambda_44A4')
    def lambda_44A4():
        OP_6C(315000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_44A4)

    ChrMoveTo(0x000E, -44800, -2000, 43710, 2000, 0x00)

    @scena.Lambda('lambda_44C8')
    def lambda_44C8():
        ChrWalkTo(0x000E, -44970, -2000, 40710, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_44C8)

    WaitForThreadExit(0x000E, 0x0001)
    WaitForThreadExit(0x0101, 0x0001)
    TerminateThread(0x0101, 0x03)

    ChrTalk(
        0x000E,
        (
            '#0180320744V#1060F不过，我只是来看看\n',
            '是谁在吹奏……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320745V真没想到\n',
            '竟然是艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320746V#1061F只知道你喜欢钓鱼和收集鞋子，\n',
            '没想到你还有这样的兴趣？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320747V#1008F#6P嘿嘿……\n',
            '和我的形象不符吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0180320748V#1064F不，没那回事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320749V#1066F说实话，还是钓鱼方面\n',
            '更擅长一点……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320750V#1016F#6P哈哈，直接说\n',
            '吹得很糟糕就可以了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320751V就连我自己\n',
            '也不认为吹的好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0180320752V#1065F嗯，的确\n',
            '有些笨拙的地方，不过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320753V#1060F音乐最重要的是用心去演奏。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320754V这点，从刚才的\n',
            '吹奏中，已经很\n',
            '好的流露出来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320755V#1025F#6P是，是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320756V#1003F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0180320757V#1060F可以站到你旁边吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320758V#1025F#6P啊……\n',
            '啊，嗯，请。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_47E0')
    def lambda_47E0():
        CameraMove(-44990, -2000, 38510, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_47E0)

    @scena.Lambda('lambda_47F8')
    def lambda_47F8():
        ChrMoveTo(0x00FE, -45490, -2000, 38510, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_47F8)

    Sleep(50)

    ChrMoveTo(0x0101, -44600, -2000, 38520, 1000, 0x00)
    ChrSetDirection(0x0101, 270, 200)
    WaitForThreadExit(0x000E, 0x0001)
    WaitForThreadExit(0x0101, 0x0001)
    OP_62(0x000E, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    OP_63(0x000E)
    Sleep(500)

    ChrTalk(
        0x000E,
        (
            '#0180320759V#1065F#5P……我想问你一件事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320760V#1067F艾丝蒂尔，\n',
            '见到他之后你打算怎么办？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210711V#1004F#4P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000E, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x000E,
        (
            '#0180320762V#1060F#5P听说因为一些事\n',
            '从你们的面前消失了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320763V如果你再遇到他，你想\n',
            '对那家伙说些什么呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320764V你应该有想过吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320765V#1026F#4P…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320766V#1003F我曾经想过，\n',
            '就算揍扁他也要带他回来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320767V但是，这么鲁莽的事\n',
            '我想我也做不到……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320768V#1007F坦白说，我的话也许\n',
            '约修亚已经听不进去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0180320769V#1063F#5P即使知道这些……\n',
            '你也不会放弃他吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320770V#1003F#4P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320771V#1025F约修亚背负的痛苦…\n',
            '还有我自己的不成熟，\n',
            '我考虑了很多……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320772V结果，无论我怎么考虑\n',
            '都想不出要对约修亚\n',
            '说些什么才好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320773V#1010F因此──这些话\n',
            '还是等遇到他的时候再考虑吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0180320774V#1064F#5P……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320775V#1025F#4P可是，我的思念\n',
            '不仅仅是我自己的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320776V那是和约修亚在一起的时候\n',
            '自然培养起来的感情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320777V#1012F因此……遇到约修亚后\n',
            '我一定会知道该说些什么的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320778V#1017F只有我才能传达\n',
            '给约修亚的话语──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0180320779V#1064F#5P……………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320780V#1006F#4P因此，我决定还没见面以前\n',
            '就不再想这些只会令人烦恼的事了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320781V#1016F嘿嘿，虽然偶尔\n',
            '我也会像刚刚那样伤感……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320782V就当作那是少女的特权吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000E, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000E,
        (
            '#0180320783V#1068F#5P……哈，真没法子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320784V跟我原来的计划\n',
            '根本完全不一样嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320785V#1004F#4P啊……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0180320786V#1065F#5P①沉浸在伤感中的艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320787V#1063F②被我用尖锐言词刺激\n',
            '  感到不知所措的艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320788V#1062F③这时我温柔的安慰她。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320789V#1061F④艾丝蒂尔重新恢复了精神\n',
            '  ≡ 于是对我的好感度直线上升。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320790V#1062F──这是我准备好的\n',
            '必胜计划……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320791V#1068F结果②，③\n',
            '还没开始就结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320792V#1016F#4P啊哈哈，抱歉抱歉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320793V#1006F不过，凯文先生\n',
            '真是名很棒的神父啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320794V对像我这样的\n',
            '陷入苦恼的人\n',
            '总是那么关心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0180320795V#1068F#5P啊唔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320796V#1066F嗯，虽然这\n',
            '就是神父的工作……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320797V但对艾丝蒂尔关心，\n',
            '还有一半理由的是\n',
            '出于爱意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320798V#1004F#4P啊……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320799V你说什么哪──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000E, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrSetDirection(0x000E, 180, 400)

    ChrTalk(
        0x000E,
        (
            '#0180320800V#1063F#5P……稍等一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010320801V#1015F#4P？？？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320802V你突然怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0180320803V#1067F#5P不，从湖那边\n',
            '好像来了条小船……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180320804V好像上面\n',
            '躺着个人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)

    ChrTalk(
        0x0101,
        (
            '#0010320805V#1020F#4P啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    LoadEffect(0x00, 'map\\\\mp013_00.eff')
    LoadEffect(0x01, 'map\\\\mp013_02.eff')
    OP_72(0x0003, 0x0002)
    OP_71(0x0003, 0x0040)
    OP_A1(0x0010, 0x0003)
    ChrClearFlags(0x0012, 0x0080)
    ChrSetFlags(0x0012, 0x0002)
    ChrSetFlags(0x0012, 0x0020)
    ChrSetBattleFlags(0x0012, 0x0020)
    ChrSetFlags(0x0012, 0x0001)
    ChrSetSubChip(0x0012, 5)

    ExecExpressionWithValue(
        0x0012,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrClearFlags(0x0012, 0x0001)
    ChrSetFlags(0x0010, 0x0040)
    ChrSetPos(0x0010, -44030, -3000, 23480, 180)
    Yield()
    OP_89(0x0012, -43660, -3000, 24200, 0)

    @scena.Lambda('lambda_527C')
    def lambda_527C():
        CameraMove(-44650, -2000, 35970, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_527C)

    @scena.Lambda('lambda_5294')
    def lambda_5294():
        OP_67(0, 7280, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5294)

    @scena.Lambda('lambda_52AC')
    def lambda_52AC():
        OP_6C(229000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_52AC)

    Sleep(300)

    ChrSetDirection(0x0101, 180, 400)
    Sleep(1700)

    CreateThread(0x0010, 0x00, 0x00, func_19_5364)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(3000)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x00)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010320806V#1020F#2P#3S克，克鲁茨前辈！？',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/T1501._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0019 offset: 0x5364
@scena.Code('func_19_5364')
def func_19_5364():
    PlayEffect(0x00, 0x00, 0x0010, 0, -50, 2200, 180, 0, 0, 600, 100, 3000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_539F')
    def lambda_539F():
        ChrMoveTo(0x00FE, -44060, -3000, 35700, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_539F)

    Sleep(300)

    @scena.Lambda('lambda_53BF')
    def lambda_53BF():
        ChrMoveTo(0x00FE, -44060, -3000, 35700, 1600, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_53BF)

    Sleep(300)

    @scena.Lambda('lambda_53DF')
    def lambda_53DF():
        ChrMoveTo(0x00FE, -44060, -3000, 35701, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_53DF)

    WaitForThreadExit(0x0010, 0x0001)
    PlaySE(302, 0x00, 0x4B)
    PlayEffect(0x01, 0xFF, 0x0010, 0, -170, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(200)

    StopEffect(0x00, 0x00)

    @scena.Lambda('lambda_5441')
    def lambda_5441():
        ChrMoveTo(0x00FE, -44060, -3000, 34000, 200, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_5441)

    Sleep(200)

    @scena.Lambda('lambda_5461')
    def lambda_5461():
        ChrMoveTo(0x00FE, -44060, -3000, 34000, 400, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_5461)

    Sleep(200)

    @scena.Lambda('lambda_5481')
    def lambda_5481():
        ChrMoveTo(0x00FE, -44060, -3000, 34000, 600, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_5481)

    @scena.Lambda('lambda_549C')
    def lambda_549C():
        ChrMoveTo(0x00FE, -44060, -3000, 34000, 400, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_549C)

    Sleep(200)

    @scena.Lambda('lambda_54BC')
    def lambda_54BC():
        ChrMoveTo(0x00FE, -44060, -3000, 34000, 200, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_54BC)

    Sleep(200)

    @scena.Lambda('lambda_54DC')
    def lambda_54DC():
        ChrMoveTo(0x00FE, -44060, -3000, 34000, 100, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_54DC)

    WaitForThreadExit(0x0010, 0x0001)

    Return()

# id: 0x001A offset: 0x54F7
@scena.Code('func_1A_54F7')
def func_1A_54F7():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 3, 0x1C03)),
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 4, 0x1C04)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5559',
    )

    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0010320728V#1015F哎呀，瞒着大家\n',
            '出来似乎不太好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_5559(): pass

    label('loc_5559')

    Return()

# id: 0x001B offset: 0x555A
@scena.Code('func_1B_555A')
def func_1B_555A():
    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0011860001V#1001F这里好像可以钓上什么来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5592')
    def lambda_5592():
        CameraMove(-3550, -2000, 29080, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_5592)

    @scena.Lambda('lambda_55AA')
    def lambda_55AA():
        CameraSetDistance(2800, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_55AA)

    @scena.Lambda('lambda_55BA')
    def lambda_55BA():
        OP_6C(135000, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_55BA)

    Sleep(1000)

    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '钓鱼吗？',
            (TxtCtl.SetColor, 0x0),
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

    Menu(
        0,
        10,
        32,
        1,
        (
            TXT(0x00, '钓鱼\n'),
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
    WaitForThreadExit(0x0000, 0x0001)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5685',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_564A',
    )

    OP_C0(0x0E, 0x0000000C, 0xFFFFF470, 0xFFFFF830, 0x00007EF4, 0x000000B4, 0xFFFFF45C, 0xFFFFF448, 0x000072C4)

    Jump('loc_566C')

    def _loc_564A(): pass

    label('loc_564A')

    OP_C0(0x0E, 0x0000000D, 0xFFFFF470, 0xFFFFF830, 0x00007EF4, 0x000000B4, 0xFFFFF45C, 0xFFFFF448, 0x000072C4)

    def _loc_566C(): pass

    label('loc_566C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041B, 7, 0x20DF)),
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 0, 0x20E0)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_567F',
    )

    SetScenaFlags(ScenaFlag(0x041C, 0, 0x20E0))
    Call(0, 0x001C)

    def _loc_567F(): pass

    label('loc_567F')

    OP_0D()
    EventEnd(0x01)

    Jump('loc_5694')

    def _loc_5685(): pass

    label('loc_5685')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5694',
    )

    EventEnd(0x01)

    def _loc_5694(): pass

    label('loc_5694')

    Return()

# id: 0x001C offset: 0x5695
@scena.Code('func_1C_5695')
def func_1C_5695():
    FadeOut(0, 0, -1)
    EventBegin(0x00)
    CameraMove(-2850, -2000, 32880, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetFlags(0x00F7, 0x0008)
    ChrSetFlags(0x00F8, 0x0008)
    ChrSetFlags(0x00F9, 0x0008)
    ChrSetPos(0x0101, -2950, -2000, 33410, 180)
    ChrSetPos(0x0016, 1930, -2000, 40500, 225)
    ChrSetChipByIndex(0x0016, 42)
    OP_4A(0x0016, 255)
    OP_0D()
    FadeIn(1000, 0)
    OP_0D()
    Sleep(400)

    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010351219V#1020F#1P什，什么这条鱼……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(
        0x0016,
        (
            '#1230351220V#4P噢噢！！\n',
            '这，这条鱼！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)

    @scena.Lambda('lambda_57BE')
    def lambda_57BE():
        ChrTurnDirection(0x00FE, 0x0016, 400)
        Yield()

        Jump('lambda_57BE')

    DispatchAsync2(0x0101, 0x0001, lambda_57BE)

    CameraMove(-840, -2000, 38510, 1500)

    ChrTalk(
        0x0101,
        (
            '#0010351221V#1011F罗伊德大叔……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0016, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_581C')
    def lambda_581C():
        CameraMove(-2330, -2000, 34690, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_581C)

    ChrWalkTo(0x0016, 200, -2000, 38770, 5000, 0x00)
    ChrWalkTo(0x0016, -2970, -2000, 38520, 5000, 0x00)
    ChrWalkTo(0x0016, -2920, -2000, 34840, 5000, 0x00)
    WaitForThreadExit(0x0101, 0x0002)
    Sleep(1000)

    ChrTalk(
        0x0016,
        (
            '#1230351222V#1P红，红褐色的鳞片、\n',
            '像燃烧一般红色的眼睛……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#1230351223V#1P不，不会错的！\n',
            '就是那它……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#1230351224V#1P#4S『瓦雷利亚湖的湖之主』呀！！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010351225V#1004F#4P啊！！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010351226V这，这是传说的『湖之主』？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#1230351227V#1P嗯，没想到被你\n',
            '钓上来了呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#1230351228V#1P身为给你钓鱼手册的人，\n',
            '现在真是半分高兴半分悔恨的复杂心情呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#1230351229V#1P但，这也是女神的旨意……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#1230351230V#1P这次就坦白地承认你的实力，\n',
            '请收下这个吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['特级钓师认定证书']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['特级钓师认定证书'], 1)
    Sleep(500)

    ChrTalk(
        0x0016,
        (
            '#1230351231V#1P现在你已经被\n',
            '我们『钓公师团』公认\n',
            '成为『特级钓师』了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#1230351232V#1P不过！不要满足于现状，\n',
            '今后更要不断地向钓鱼之路迈进！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010351233V#1016F#4P啊哈哈……谢谢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010351234V#1015F嗯，不管怎么说\n',
            '还是谢谢你的礼物……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010351235V……请问，这个认证书是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#1230351236V#1P嗯，这是用来证明\n',
            '你身为钓师实力的身份证。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#1230351237V#1P拿着去『钓公师团』本部\n',
            '能得到很多好东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#1230351238V#1P有事去王都的时候\n',
            '请一定要过去一次。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010351239V#1000F#4P是这样啊。\n',
            '虽然不是很明白但好象很棒。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010351240V嗯，以后一定去看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#1230351241V#1P呵呵，应该有喜欢钓鱼的人\n',
            '做梦都想要的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#1230351242V#1P哎哟，我也不能认输。\n',
            '必须赶快制定下个目标。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#1230351243V#1P那么，再见了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0016, -2970, -2000, 38520, 5000, 0x00)
    ChrWalkTo(0x0016, 200, -2000, 38770, 5000, 0x00)
    ChrWalkTo(0x0016, 1930, -2000, 40500, 5000, 0x00)
    TerminateThread(0x0101, 0x01)
    ChrSetPos(0x0016, -8170, 500, 40910, 180)
    ChrSetChipByIndex(0x0016, 42)
    ChrClearFlags(0x0016, 0x0010)
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(-2950, -2000, 33410, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, -2950, -2000, 33410, 180)
    ChrSetPos(0x0001, -2950, -2000, 33410, 180)
    ChrSetPos(0x0002, -2950, -2000, 33410, 180)
    ChrSetPos(0x0003, -2950, -2000, 33410, 180)
    OP_30(0x00)
    ChrClearFlags(0x00F7, 0x0008)
    ChrClearFlags(0x00F8, 0x0008)
    ChrClearFlags(0x00F9, 0x0008)
    CreateThread(0x0016, 0x00, 0x00, func_02_80D)
    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))
    FadeIn(1000, 0)
    OP_0D()
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

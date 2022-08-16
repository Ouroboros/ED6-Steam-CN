import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C3604_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C3604   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'C3604.x'
    header.mapIndex       = 1
    header.bgm            = 60
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
        ('ED6_DT29/CH12660._CH', 'ED6_DT29/CH12660P._CP'),
        ('ED6_DT29/CH12661._CH', 'ED6_DT29/CH12661P._CP'),
        ('ED6_DT29/CH12670._CH', 'ED6_DT29/CH12670P._CP'),
        ('ED6_DT29/CH12671._CH', 'ED6_DT29/CH12671P._CP'),
        ('ED6_DT29/CH12680._CH', 'ED6_DT29/CH12680P._CP'),
        ('ED6_DT29/CH12681._CH', 'ED6_DT29/CH12681P._CP'),
        ('ED6_DT29/CH12690._CH', 'ED6_DT29/CH12690P._CP'),
        ('ED6_DT29/CH12691._CH', 'ED6_DT29/CH12691P._CP'),
        ('ED6_DT29/CH12700._CH', 'ED6_DT29/CH12700P._CP'),
        ('ED6_DT29/CH12701._CH', 'ED6_DT29/CH12701P._CP'),
        ('ED6_DT29/CH12710._CH', 'ED6_DT29/CH12710P._CP'),
        ('ED6_DT29/CH12711._CH', 'ED6_DT29/CH12711P._CP'),
        ('ED6_DT29/CH12720._CH', 'ED6_DT29/CH12720P._CP'),
        ('ED6_DT29/CH12721._CH', 'ED6_DT29/CH12721P._CP'),
    ]

# id: 0x10001 offset: 0x11A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '',
            x                   = 10040,
            z                   = -2600,
            y                   = 11460,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x13A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = -30540,
            z           = -50,
            y           = 17720,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0414,
            word_18     = 0x1EC6,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 34650,
            z           = 200,
            y           = -14550,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0414,
            word_18     = 0x1EC7,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 28640,
            z           = -50,
            y           = -21610,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0410,
            word_18     = 0x1EC8,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 30780,
            z           = -7650,
            y           = -48870,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0414,
            word_18     = 0x1EC9,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 32320,
            z           = -7450,
            y           = -57600,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0411,
            word_18     = 0x1ECA,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -10,
            z           = -4050,
            y           = -70900,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0410,
            word_18     = 0x1ECB,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -30670,
            z           = -4050,
            y           = -53210,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0414,
            word_18     = 0x1ECC,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x1FE
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x1FE
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 30780,
            triggerZ            = 400,
            triggerY            = 4440,
            triggerRange        = 1000,
            actorX              = 30780,
            actorZ              = 400,
            actorY              = 3740,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 18710,
            triggerZ            = 400,
            triggerY            = 11470,
            triggerRange        = 1000,
            actorX              = 18050,
            actorZ              = 400,
            actorY              = 11470,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 10,
            triggerZ            = -7200,
            triggerY            = -53840,
            triggerRange        = 1000,
            actorX              = 10,
            actorZ              = -7200,
            actorY              = -54500,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 11340,
            triggerZ            = -7200,
            triggerY            = -42070,
            triggerRange        = 1000,
            actorX              = 11870,
            actorZ              = -7200,
            actorY              = -42410,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -18680,
            triggerZ            = -7200,
            triggerY            = -11480,
            triggerRange        = 1000,
            actorX              = -18020,
            actorZ              = -7200,
            actorY              = -11480,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 9290,
            triggerZ            = -3600,
            triggerY            = 11460,
            triggerRange        = 1000,
            actorX              = 10040,
            actorZ              = -3600,
            actorY              = 11460,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -30750,
            triggerZ            = 400,
            triggerY            = -7010,
            triggerRange        = 1000,
            actorX              = -30750,
            actorZ              = 400,
            actorY              = -7710,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 17870,
            triggerZ            = 4400,
            triggerY            = 25200,
            triggerRange        = 1000,
            actorX              = 18400,
            actorZ              = 4400,
            actorY              = 24860,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 30790,
            triggerZ            = 400,
            triggerY            = -4460,
            triggerRange        = 1000,
            actorX              = 30790,
            actorZ              = 400,
            actorY              = -3800,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 13590,
            triggerZ            = -3600,
            triggerY            = -27580,
            triggerRange        = 1000,
            actorX              = 13030,
            actorZ              = -3600,
            actorY              = -27960,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000C,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 30,
            triggerZ            = -3600,
            triggerY            = -94270,
            triggerRange        = 1000,
            actorX              = 30,
            actorZ              = -3600,
            actorY              = -94970,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000D,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 17700,
            triggerZ            = -7200,
            triggerY            = -45730,
            triggerRange        = 1000,
            actorX              = 17120,
            actorZ              = -7200,
            actorY              = -45370,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000E,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 13700,
            triggerZ            = -10800,
            triggerY            = -95360,
            triggerRange        = 1000,
            actorX              = 13320,
            actorZ              = -10800,
            actorY              = -95950,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000F,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -14260,
            triggerZ            = -3600,
            triggerY            = -43720,
            triggerRange        = 1000,
            actorX              = -13650,
            actorZ              = -3600,
            actorY              = -43350,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0010,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -30720,
            triggerZ            = -3600,
            triggerY            = -33900,
            triggerRange        = 1000,
            actorX              = -30720,
            actorZ              = -3600,
            actorY              = -33240,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0011,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 1100,
            triggerZ            = -7200,
            triggerY            = -114690,
            triggerRange        = 1200,
            actorX              = 1100,
            actorZ              = -6000,
            actorY              = -114690,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001E,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x43E
@scena.Code('Init')
def Init():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_456'),
        (0x00000065, 'loc_45D'),
        (0x00000066, 'loc_464'),
        (0x00000067, 'loc_46B'),
        (-1, 'loc_472'),
    )

    def _loc_456(): pass

    label('loc_456')

    Event(0, func_12_1865)

    Jump('loc_472')

    def _loc_45D(): pass

    label('loc_45D')

    Event(0, func_14_19DD)

    Jump('loc_472')

    def _loc_464(): pass

    label('loc_464')

    Event(0, func_16_1B55)

    Jump('loc_472')

    def _loc_46B(): pass

    label('loc_46B')

    Event(0, func_18_1CCD)

    Jump('loc_472')

    def _loc_472(): pass

    label('loc_472')

    Return()

# id: 0x0001 offset: 0x473
@scena.Code('func_01_473')
def func_01_473():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EA, 0, 0x1F50)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_485',
    )

    OP_6F(0x0001, 0)

    Jump('loc_48C')

    def _loc_485(): pass

    label('loc_485')

    OP_6F(0x0001, 60)

    def _loc_48C(): pass

    label('loc_48C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EA, 2, 0x1F52)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_49E',
    )

    OP_6F(0x0002, 0)

    Jump('loc_4A5')

    def _loc_49E(): pass

    label('loc_49E')

    OP_6F(0x0002, 60)

    def _loc_4A5(): pass

    label('loc_4A5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EA, 3, 0x1F53)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4B7',
    )

    OP_6F(0x0003, 0)

    Jump('loc_4BE')

    def _loc_4B7(): pass

    label('loc_4B7')

    OP_6F(0x0003, 60)

    def _loc_4BE(): pass

    label('loc_4BE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EA, 5, 0x1F55)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4D0',
    )

    OP_6F(0x0004, 0)

    Jump('loc_4D7')

    def _loc_4D0(): pass

    label('loc_4D0')

    OP_6F(0x0004, 60)

    def _loc_4D7(): pass

    label('loc_4D7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EA, 6, 0x1F56)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4E9',
    )

    OP_6F(0x0005, 0)

    Jump('loc_4F0')

    def _loc_4E9(): pass

    label('loc_4E9')

    OP_6F(0x0005, 60)

    def _loc_4F0(): pass

    label('loc_4F0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EA, 7, 0x1F57)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_502',
    )

    OP_6F(0x0006, 0)

    Jump('loc_509')

    def _loc_502(): pass

    label('loc_502')

    OP_6F(0x0006, 60)

    def _loc_509(): pass

    label('loc_509')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EB, 1, 0x1F59)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_51B',
    )

    OP_6F(0x0007, 0)

    Jump('loc_522')

    def _loc_51B(): pass

    label('loc_51B')

    OP_6F(0x0007, 60)

    def _loc_522(): pass

    label('loc_522')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EB, 2, 0x1F5A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_534',
    )

    OP_6F(0x0008, 0)

    Jump('loc_53B')

    def _loc_534(): pass

    label('loc_534')

    OP_6F(0x0008, 60)

    def _loc_53B(): pass

    label('loc_53B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EB, 3, 0x1F5B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_54D',
    )

    OP_6F(0x0009, 0)

    Jump('loc_554')

    def _loc_54D(): pass

    label('loc_54D')

    OP_6F(0x0009, 60)

    def _loc_554(): pass

    label('loc_554')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EB, 4, 0x1F5C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_566',
    )

    OP_6F(0x000A, 0)

    Jump('loc_56D')

    def _loc_566(): pass

    label('loc_566')

    OP_6F(0x000A, 60)

    def _loc_56D(): pass

    label('loc_56D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EB, 6, 0x1F5E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_57F',
    )

    OP_6F(0x000B, 0)

    Jump('loc_586')

    def _loc_57F(): pass

    label('loc_57F')

    OP_6F(0x000B, 60)

    def _loc_586(): pass

    label('loc_586')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EB, 7, 0x1F5F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_598',
    )

    OP_6F(0x000C, 0)

    Jump('loc_59F')

    def _loc_598(): pass

    label('loc_598')

    OP_6F(0x000C, 60)

    def _loc_59F(): pass

    label('loc_59F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EC, 0, 0x1F60)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5B1',
    )

    OP_6F(0x000D, 0)

    Jump('loc_5B8')

    def _loc_5B1(): pass

    label('loc_5B1')

    OP_6F(0x000D, 60)

    def _loc_5B8(): pass

    label('loc_5B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EC, 2, 0x1F62)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5CA',
    )

    OP_6F(0x000E, 0)

    Jump('loc_5D1')

    def _loc_5CA(): pass

    label('loc_5CA')

    OP_6F(0x000E, 60)

    def _loc_5D1(): pass

    label('loc_5D1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EC, 3, 0x1F63)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5E3',
    )

    OP_6F(0x000F, 0)

    Jump('loc_5EA')

    def _loc_5E3(): pass

    label('loc_5E3')

    OP_6F(0x000F, 60)

    def _loc_5EA(): pass

    label('loc_5EA')

    LoadEffect(0x00, 'map\\\\mp049_21.eff')
    LoadEffect(0x01, 'map\\\\mp049_22.eff')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D8, 6, 0x1EC6)),
            Expr.Return,
        ),
        'loc_61E',
    )

    ChrSetFlags(0x0009, 0x0080)

    def _loc_61E(): pass

    label('loc_61E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D8, 7, 0x1EC7)),
            Expr.Return,
        ),
        'loc_62A',
    )

    ChrSetFlags(0x000A, 0x0080)

    def _loc_62A(): pass

    label('loc_62A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D9, 0, 0x1EC8)),
            Expr.Return,
        ),
        'loc_636',
    )

    ChrSetFlags(0x000B, 0x0080)

    def _loc_636(): pass

    label('loc_636')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D9, 1, 0x1EC9)),
            Expr.Return,
        ),
        'loc_642',
    )

    ChrSetFlags(0x000C, 0x0080)

    def _loc_642(): pass

    label('loc_642')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D9, 2, 0x1ECA)),
            Expr.Return,
        ),
        'loc_64E',
    )

    ChrSetFlags(0x000D, 0x0080)

    def _loc_64E(): pass

    label('loc_64E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D9, 3, 0x1ECB)),
            Expr.Return,
        ),
        'loc_65A',
    )

    ChrSetFlags(0x000E, 0x0080)

    def _loc_65A(): pass

    label('loc_65A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D9, 4, 0x1ECC)),
            Expr.Return,
        ),
        'loc_666',
    )

    ChrSetFlags(0x000F, 0x0080)

    def _loc_666(): pass

    label('loc_666')

    OP_1B(0x00, 0x00, 0x0013)
    OP_1B(0x01, 0x00, 0x0015)
    OP_1B(0x02, 0x00, 0x0017)
    OP_1B(0x03, 0x00, 0x0019)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6E5',
    )

    LoadEffect(0x02, 'map\\\\mp027_00.eff')
    PlayEffect(0x02, 0x02, 0x00FF, 1100, -6000, -114690, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    OP_71(0x0011, 0x0020)
    OP_6F(0x0011, 0)
    OP_70(0x0011, 250)

    Jump('loc_6F1')

    def _loc_6E5(): pass

    label('loc_6E5')

    OP_72(0x0011, 0x0020)
    OP_6F(0x0011, 250)

    def _loc_6F1(): pass

    label('loc_6F1')

    Return()

# id: 0x0002 offset: 0x6F2
@scena.Code('func_02_6F2')
def func_02_6F2():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_707',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_6F2')

    def _loc_707(): pass

    label('loc_707')

    Return()

# id: 0x0003 offset: 0x708
@scena.Code('func_03_708')
def func_03_708():
    UnlockAchievement(0x02, 0x00E9, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EA, 0, 0x1F50)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7E5',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['太极服'], 1)"),
            Expr.Return,
        ),
        'loc_77C',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['太极服']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03EA, 0, 0x1F50))

    Jump('loc_7E2')

    def _loc_77C(): pass

    label('loc_77C')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['太极服']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['太极服']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0)

    def _loc_7E2(): pass

    label('loc_7E2')

    Jump('loc_816')

    def _loc_7E5(): pass

    label('loc_7E5')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_816(): pass

    label('loc_816')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x824
@scena.Code('func_04_824')
def func_04_824():
    UnlockAchievement(0x02, 0x00EA, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EA, 2, 0x1F52)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_901',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅱ'], 1)"),
            Expr.Return,
        ),
        'loc_898',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅱ']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03EA, 2, 0x1F52))

    Jump('loc_8FE')

    def _loc_898(): pass

    label('loc_898')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅱ']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅱ']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0)

    def _loc_8FE(): pass

    label('loc_8FE')

    Jump('loc_932')

    def _loc_901(): pass

    label('loc_901')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_932(): pass

    label('loc_932')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x940
@scena.Code('func_05_940')
def func_05_940():
    UnlockAchievement(0x02, 0x00EB, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EA, 3, 0x1F53)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A1D',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0003, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['蓝色猎鹰'], 1)"),
            Expr.Return,
        ),
        'loc_9B4',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['蓝色猎鹰']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03EA, 3, 0x1F53))

    Jump('loc_A1A')

    def _loc_9B4(): pass

    label('loc_9B4')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['蓝色猎鹰']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['蓝色猎鹰']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0003, 60)
    OP_70(0x0003, 0)

    def _loc_A1A(): pass

    label('loc_A1A')

    Jump('loc_A4E')

    def _loc_A1D(): pass

    label('loc_A1D')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_A4E(): pass

    label('loc_A4E')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0xA5C
@scena.Code('func_06_A5C')
def func_06_A5C():
    UnlockAchievement(0x02, 0x00EC, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EA, 5, 0x1F55)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B39',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0004, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['大回复药'], 1)"),
            Expr.Return,
        ),
        'loc_AD0',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['大回复药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03EA, 5, 0x1F55))

    Jump('loc_B36')

    def _loc_AD0(): pass

    label('loc_AD0')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['大回复药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['大回复药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0004, 60)
    OP_70(0x0004, 0)

    def _loc_B36(): pass

    label('loc_B36')

    Jump('loc_B6A')

    def _loc_B39(): pass

    label('loc_B39')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_B6A(): pass

    label('loc_B6A')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0xB78
@scena.Code('func_07_B78')
def func_07_B78():
    UnlockAchievement(0x02, 0x00ED, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EA, 6, 0x1F56)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C55',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0005, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['圣灵药'], 1)"),
            Expr.Return,
        ),
        'loc_BEC',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['圣灵药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03EA, 6, 0x1F56))

    Jump('loc_C52')

    def _loc_BEC(): pass

    label('loc_BEC')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['圣灵药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['圣灵药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0005, 60)
    OP_70(0x0005, 0)

    def _loc_C52(): pass

    label('loc_C52')

    Jump('loc_C86')

    def _loc_C55(): pass

    label('loc_C55')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_C86(): pass

    label('loc_C86')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0xC94
@scena.Code('func_08_C94')
def func_08_C94():
    UnlockAchievement(0x02, 0x00EE, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EA, 7, 0x1F57)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E2C',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0006, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EB, 0, 0x1F58)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D78',
    )

    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    ChrTurnDirection(0x0008, 0x0000, 0)
    ChrMoveToRelativeAsync(0x0008, 0, 1000, 0, 0, 0x00)

    @scena.Lambda('lambda_0CEB')
    def lambda_0CEB():
        ChrMoveToRelativeAsync(0x00FE, 0, -1000, 0, 600, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0CEB)

    @scena.Lambda('lambda_0D06')
    def lambda_0D06():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 600)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0D06)

    ChrClearFlags(0x0008, 0x0080)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '魔兽出现了！',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Battle(0x00000418, 0x00000000, 0x00, 0x0000, 0xFF)
    ChrSetFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_D53'),
        (0x00000002, 'loc_D65'),
        (0x00000001, 'loc_D75'),
        (-1, 'loc_D78'),
    )

    def _loc_D53(): pass

    label('loc_D53')

    SetScenaFlags(ScenaFlag(0x03EB, 0, 0x1F58))
    OP_6F(0x0006, 60)
    Sleep(500)

    Jump('loc_D78')

    def _loc_D65(): pass

    label('loc_D65')

    OP_6F(0x0006, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

    def _loc_D75(): pass

    label('loc_D75')

    OP_B4(0x00)

    Return()

    def _loc_D78(): pass

    label('loc_D78')

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['长桶Ⅲ'], 1)"),
            Expr.Return,
        ),
        'loc_DC7',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['长桶Ⅲ']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03EA, 7, 0x1F57))

    Jump('loc_E29')

    def _loc_DC7(): pass

    label('loc_DC7')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['长桶Ⅲ']),
            (TxtCtl.SetColor, 0x0),
            '。 \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['长桶Ⅲ']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0006, 60)
    OP_70(0x0006, 0)

    def _loc_E29(): pass

    label('loc_E29')

    Jump('loc_E5B')

    def _loc_E2C(): pass

    label('loc_E2C')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_E5B(): pass

    label('loc_E5B')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0009 offset: 0xE69
@scena.Code('func_09_E69')
def func_09_E69():
    UnlockAchievement(0x02, 0x00EF, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EB, 1, 0x1F59)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F46',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0007, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅱ'], 1)"),
            Expr.Return,
        ),
        'loc_EDD',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅱ']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03EB, 1, 0x1F59))

    Jump('loc_F43')

    def _loc_EDD(): pass

    label('loc_EDD')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅱ']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅱ']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0007, 60)
    OP_70(0x0007, 0)

    def _loc_F43(): pass

    label('loc_F43')

    Jump('loc_F77')

    def _loc_F46(): pass

    label('loc_F46')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_F77(): pass

    label('loc_F77')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x000A offset: 0xF85
@scena.Code('func_0A_F85')
def func_0A_F85():
    UnlockAchievement(0x02, 0x00F0, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EB, 2, 0x1F5A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1062',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0008, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['还魂粉'], 1)"),
            Expr.Return,
        ),
        'loc_FF9',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['还魂粉']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03EB, 2, 0x1F5A))

    Jump('loc_105F')

    def _loc_FF9(): pass

    label('loc_FF9')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['还魂粉']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['还魂粉']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0008, 60)
    OP_70(0x0008, 0)

    def _loc_105F(): pass

    label('loc_105F')

    Jump('loc_1093')

    def _loc_1062(): pass

    label('loc_1062')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_1093(): pass

    label('loc_1093')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x000B offset: 0x10A1
@scena.Code('func_0B_10A1')
def func_0B_10A1():
    UnlockAchievement(0x02, 0x00F1, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EB, 3, 0x1F5B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_117E',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0009, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['大回复药'], 1)"),
            Expr.Return,
        ),
        'loc_1115',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['大回复药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03EB, 3, 0x1F5B))

    Jump('loc_117B')

    def _loc_1115(): pass

    label('loc_1115')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['大回复药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['大回复药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0009, 60)
    OP_70(0x0009, 0)

    def _loc_117B(): pass

    label('loc_117B')

    Jump('loc_11AF')

    def _loc_117E(): pass

    label('loc_117E')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_11AF(): pass

    label('loc_11AF')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x000C offset: 0x11BD
@scena.Code('func_0C_11BD')
def func_0C_11BD():
    UnlockAchievement(0x02, 0x00F2, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EB, 4, 0x1F5C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_129A',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x000A, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['苍耀珠'], 1)"),
            Expr.Return,
        ),
        'loc_1231',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['苍耀珠']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03EB, 4, 0x1F5C))

    Jump('loc_1297')

    def _loc_1231(): pass

    label('loc_1231')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['苍耀珠']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['苍耀珠']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x000A, 60)
    OP_70(0x000A, 0)

    def _loc_1297(): pass

    label('loc_1297')

    Jump('loc_12CB')

    def _loc_129A(): pass

    label('loc_129A')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_12CB(): pass

    label('loc_12CB')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x000D offset: 0x12D9
@scena.Code('func_0D_12D9')
def func_0D_12D9():
    UnlockAchievement(0x02, 0x00F3, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EB, 6, 0x1F5E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_13B6',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x000B, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['全回复药'], 1)"),
            Expr.Return,
        ),
        'loc_134D',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['全回复药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03EB, 6, 0x1F5E))

    Jump('loc_13B3')

    def _loc_134D(): pass

    label('loc_134D')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['全回复药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['全回复药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x000B, 60)
    OP_70(0x000B, 0)

    def _loc_13B3(): pass

    label('loc_13B3')

    Jump('loc_13E7')

    def _loc_13B6(): pass

    label('loc_13B6')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_13E7(): pass

    label('loc_13E7')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x000E offset: 0x13F5
@scena.Code('func_0E_13F5')
def func_0E_13F5():
    UnlockAchievement(0x02, 0x00F4, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EB, 7, 0x1F5F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_14D2',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x000C, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['大回复药'], 1)"),
            Expr.Return,
        ),
        'loc_1469',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['大回复药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03EB, 7, 0x1F5F))

    Jump('loc_14CF')

    def _loc_1469(): pass

    label('loc_1469')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['大回复药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['大回复药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x000C, 60)
    OP_70(0x000C, 0)

    def _loc_14CF(): pass

    label('loc_14CF')

    Jump('loc_1503')

    def _loc_14D2(): pass

    label('loc_14D2')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_1503(): pass

    label('loc_1503')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x000F offset: 0x1511
@scena.Code('func_0F_1511')
def func_0F_1511():
    UnlockAchievement(0x02, 0x00F5, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EC, 0, 0x1F60)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_15EE',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x000D, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['阴阳'], 1)"),
            Expr.Return,
        ),
        'loc_1585',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['阴阳']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03EC, 0, 0x1F60))

    Jump('loc_15EB')

    def _loc_1585(): pass

    label('loc_1585')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['阴阳']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['阴阳']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x000D, 60)
    OP_70(0x000D, 0)

    def _loc_15EB(): pass

    label('loc_15EB')

    Jump('loc_161F')

    def _loc_15EE(): pass

    label('loc_15EE')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_161F(): pass

    label('loc_161F')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0010 offset: 0x162D
@scena.Code('func_10_162D')
def func_10_162D():
    UnlockAchievement(0x02, 0x00F6, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EC, 2, 0x1F62)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_170A',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x000E, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['全回复药'], 1)"),
            Expr.Return,
        ),
        'loc_16A1',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['全回复药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03EC, 2, 0x1F62))

    Jump('loc_1707')

    def _loc_16A1(): pass

    label('loc_16A1')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['全回复药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['全回复药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x000E, 60)
    OP_70(0x000E, 0)

    def _loc_1707(): pass

    label('loc_1707')

    Jump('loc_173B')

    def _loc_170A(): pass

    label('loc_170A')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_173B(): pass

    label('loc_173B')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0011 offset: 0x1749
@scena.Code('func_11_1749')
def func_11_1749():
    UnlockAchievement(0x02, 0x00F7, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EC, 3, 0x1F63)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1826',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x000F, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['替身木偶'], 1)"),
            Expr.Return,
        ),
        'loc_17BD',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['替身木偶']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03EC, 3, 0x1F63))

    Jump('loc_1823')

    def _loc_17BD(): pass

    label('loc_17BD')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['替身木偶']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['替身木偶']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x000F, 60)
    OP_70(0x000F, 0)

    def _loc_1823(): pass

    label('loc_1823')

    Jump('loc_1857')

    def _loc_1826(): pass

    label('loc_1826')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_1857(): pass

    label('loc_1857')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0012 offset: 0x1865
@scena.Code('func_12_1865')
def func_12_1865():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(0, 4190, 36000, 0)
    ChrSetPos(0x0101, 500, 4190, 35500, 180)
    ChrSetPos(0x0102, -500, 4190, 35500, 180)
    ChrSetPos(0x00F8, 500, 4190, 36500, 180)
    ChrSetPos(0x00F9, -500, 4190, 36500, 180)
    ChrSetRGBAMask(0x0000, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0001, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0002, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0003, 255, 255, 255, 0, 0)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x001A)
    Call(0, 0x001C)
    Fade(500)
    CameraMove(90, 4190, 34080, 0)
    ChrSetPos(0x0000, 90, 4190, 34080, 180)
    ChrSetPos(0x0001, 90, 4190, 34080, 180)
    ChrSetPos(0x0002, 90, 4190, 34080, 180)
    ChrSetPos(0x0003, 90, 4190, 34080, 180)
    MapSetFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x0013 offset: 0x1965
@scena.Code('func_13_1965')
def func_13_1965():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(500)
    CameraMove(0, 4190, 36000, 0)
    ChrSetPos(0x0101, -500, 4190, 36500, 0)
    ChrSetPos(0x0102, 500, 4190, 36500, 0)
    ChrSetPos(0x00F8, -500, 4190, 35500, 0)
    ChrSetPos(0x00F9, 500, 4190, 35500, 0)
    OP_0D()
    Call(0, 0x001A)
    Call(0, 0x001D)
    NewScene('ED6_DT21/C3603._SN', 103, 0, 0)
    IdleLoop()

    Return()

# id: 0x0014 offset: 0x19DD
@scena.Code('func_14_19DD')
def func_14_19DD():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(30800, 190, 18500, 0)
    ChrSetPos(0x0101, 31300, 190, 18000, 180)
    ChrSetPos(0x0102, 30300, 190, 18000, 180)
    ChrSetPos(0x00F8, 31300, 190, 19000, 180)
    ChrSetPos(0x00F9, 30300, 190, 19000, 180)
    ChrSetRGBAMask(0x0000, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0001, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0002, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0003, 255, 255, 255, 0, 0)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x001A)
    Call(0, 0x001C)
    Fade(500)
    CameraMove(30800, 190, 16219, 0)
    ChrSetPos(0x0000, 30800, 190, 16219, 180)
    ChrSetPos(0x0001, 30800, 190, 16219, 180)
    ChrSetPos(0x0002, 30800, 190, 16219, 180)
    ChrSetPos(0x0003, 30800, 190, 16219, 180)
    MapSetFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x0015 offset: 0x1ADD
@scena.Code('func_15_1ADD')
def func_15_1ADD():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(500)
    CameraMove(30800, 190, 18500, 0)
    ChrSetPos(0x0101, 30300, 190, 19000, 0)
    ChrSetPos(0x0102, 31300, 190, 19000, 0)
    ChrSetPos(0x00F8, 30300, 190, 18000, 0)
    ChrSetPos(0x00F9, 31300, 190, 18000, 0)
    OP_0D()
    Call(0, 0x001A)
    Call(0, 0x001D)
    NewScene('ED6_DT21/C3603._SN', 101, 0, 0)
    IdleLoop()

    Return()

# id: 0x0016 offset: 0x1B55
@scena.Code('func_16_1B55')
def func_16_1B55():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(-30800, -7410, -17000, 0)
    ChrSetPos(0x0101, -30300, -7410, -17500, 180)
    ChrSetPos(0x0102, -31300, -7410, -17500, 180)
    ChrSetPos(0x00F8, -30300, -7410, -16500, 180)
    ChrSetPos(0x00F9, -31300, -7410, -16500, 180)
    ChrSetRGBAMask(0x0000, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0001, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0002, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0003, 255, 255, 255, 0, 0)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x001A)
    Call(0, 0x001C)
    Fade(500)
    CameraMove(-30660, -7410, -19230, 0)
    ChrSetPos(0x0000, -30660, -7410, -19230, 180)
    ChrSetPos(0x0001, -30660, -7410, -19230, 180)
    ChrSetPos(0x0002, -30660, -7410, -19230, 180)
    ChrSetPos(0x0003, -30660, -7410, -19230, 180)
    MapSetFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x0017 offset: 0x1C55
@scena.Code('func_17_1C55')
def func_17_1C55():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(500)
    CameraMove(-30800, -7410, -17000, 0)
    ChrSetPos(0x0101, -31300, -7410, -16500, 0)
    ChrSetPos(0x0102, -30300, -7410, -16500, 0)
    ChrSetPos(0x00F8, -31300, -7410, -17500, 0)
    ChrSetPos(0x00F9, -30300, -7410, -17500, 0)
    OP_0D()
    Call(0, 0x001A)
    Call(0, 0x001D)
    NewScene('ED6_DT21/C3603._SN', 102, 0, 0)
    IdleLoop()

    Return()

# id: 0x0018 offset: 0x1CCD
@scena.Code('func_18_1CCD')
def func_18_1CCD():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(0, -6530, -106500, 0)
    ChrSetPos(0x0101, 500, -6530, -107000, 180)
    ChrSetPos(0x0102, -500, -6530, -107000, 180)
    ChrSetPos(0x00F8, 500, -6530, -106000, 180)
    ChrSetPos(0x00F9, -500, -6530, -106000, 180)
    ChrSetRGBAMask(0x0000, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0001, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0002, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0003, 255, 255, 255, 0, 0)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x001B)
    Call(0, 0x001C)
    Fade(500)
    CameraMove(-20, -6880, -108860, 0)
    ChrSetPos(0x0000, -20, -6880, -108860, 180)
    ChrSetPos(0x0001, -20, -6880, -108860, 180)
    ChrSetPos(0x0002, -20, -6880, -108860, 180)
    ChrSetPos(0x0003, -20, -6880, -108860, 180)
    MapSetFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x0019 offset: 0x1DCD
@scena.Code('func_19_1DCD')
def func_19_1DCD():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(500)
    CameraMove(0, -6530, -106500, 0)
    ChrSetPos(0x0101, -500, -6530, -106000, 0)
    ChrSetPos(0x0102, 500, -6530, -106000, 0)
    ChrSetPos(0x00F8, -500, -6530, -107000, 0)
    ChrSetPos(0x00F9, 500, -6530, -107000, 0)
    OP_0D()
    Call(0, 0x001B)
    Call(0, 0x001D)
    NewScene('ED6_DT21/C3605._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x001A offset: 0x1E45
@scena.Code('func_1A_1E45')
def func_1A_1E45():
    PlayEffect(0x00, 0xFF, 0x0000, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0001, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0002, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0003, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(153, 0x00, 0x64)
    PlaySE(184, 0x00, 0x64)

    Return()

# id: 0x001B offset: 0x1F24
@scena.Code('func_1B_1F24')
def func_1B_1F24():
    PlayEffect(0x01, 0xFF, 0x0000, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0001, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0002, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0003, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(153, 0x00, 0x64)
    PlaySE(184, 0x00, 0x64)

    Return()

# id: 0x001C offset: 0x2003
@scena.Code('func_1C_2003')
def func_1C_2003():
    @scena.Lambda('lambda_2009')
    def lambda_2009():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_2009)

    @scena.Lambda('lambda_201B')
    def lambda_201B():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_201B)

    @scena.Lambda('lambda_202D')
    def lambda_202D():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_202D)

    @scena.Lambda('lambda_203F')
    def lambda_203F():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_203F)

    Sleep(2500)

    Return()

# id: 0x001D offset: 0x2051
@scena.Code('func_1D_2051')
def func_1D_2051():
    @scena.Lambda('lambda_2057')
    def lambda_2057():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_2057)

    @scena.Lambda('lambda_2069')
    def lambda_2069():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_2069)

    @scena.Lambda('lambda_207B')
    def lambda_207B():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_207B)

    @scena.Lambda('lambda_208D')
    def lambda_208D():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_208D)

    Sleep(2000)

    Return()

# id: 0x001E offset: 0x209F
@scena.Code('func_1E_209F')
def func_1E_209F():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_20F2',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '好像是导力停止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Jump('loc_2294')

    def _loc_20F2(): pass

    label('loc_20F2')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '这是一台可供旅行者回复体力的导力器装置。',
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
        'loc_2279',
    )

    FadeIn(100, 0)
    Sleep(500)

    OP_26(13)
    OP_72(0x0011, 0x0020)
    OP_6F(0x0011, 300)
    OP_70(0x0011, 500)
    OP_73(0x0011)
    OP_6F(0x0011, 500)
    OP_70(0x0011, 700)
    OP_71(0x0011, 0x0020)
    OP_20(0x00000BB8)
    PlaySE(12, 0x00, 0x64)
    StopEffect(0x02, 0x02)
    LoadEffect(0x03, 'map\\\\mp027_01.eff')
    PlayEffect(0x03, 0x03, 0x00FF, 1100, -6000, -114690, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    FadeOut(1500, 0, -1)
    Sleep(1500)

    PlaySE(13, 0x00, 0x64)
    OP_0D()
    ChrSetStatus(0x00FF, 0xFE, 0)
    OP_69(0x0000, 0)
    OP_30(0x01)
    Sleep(3500)

    StopEffect(0x03, 0x02)
    PlayEffect(0x02, 0x02, 0x00FF, 1100, -6000, -114690, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0011, 0)
    OP_70(0x0011, 250)
    OP_1E()
    FadeIn(1000, 0)
    OP_56(0x00)
    TalkEnd(0x00FF)

    Return()

    def _loc_2279(): pass

    label('loc_2279')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2293',
    )

    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

    def _loc_2293(): pass

    label('loc_2293')

    Return()

    def _loc_2294(): pass

    label('loc_2294')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

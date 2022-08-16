import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C1701_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1701   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'C1701.x'
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
        ('ED6_DT29/CH12800._CH', 'ED6_DT29/CH12800P._CP'),
        ('ED6_DT29/CH12801._CH', 'ED6_DT29/CH12801P._CP'),
        ('ED6_DT29/CH12810._CH', 'ED6_DT29/CH12810P._CP'),
        ('ED6_DT29/CH12811._CH', 'ED6_DT29/CH12811P._CP'),
        ('ED6_DT29/CH12820._CH', 'ED6_DT29/CH12820P._CP'),
        ('ED6_DT29/CH12821._CH', 'ED6_DT29/CH12821P._CP'),
        ('ED6_DT29/CH12830._CH', 'ED6_DT29/CH12830P._CP'),
        ('ED6_DT29/CH12831._CH', 'ED6_DT29/CH12831P._CP'),
        ('ED6_DT29/CH12840._CH', 'ED6_DT29/CH12840P._CP'),
        ('ED6_DT29/CH12841._CH', 'ED6_DT29/CH12841P._CP'),
        ('ED6_DT29/CH12850._CH', 'ED6_DT29/CH12850P._CP'),
        ('ED6_DT29/CH12851._CH', 'ED6_DT29/CH12851P._CP'),
        ('ED6_DT29/CH12860._CH', 'ED6_DT29/CH12860P._CP'),
        ('ED6_DT29/CH12861._CH', 'ED6_DT29/CH12861P._CP'),
    ]

# id: 0x10001 offset: 0x11A
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10002 offset: 0x11A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = -5970,
            z           = 400,
            y           = 45720,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F4,
            word_18     = 0x1FDF,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 5390,
            z           = 400,
            y           = 45270,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F6,
            word_18     = 0x1FE0,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 5120,
            z           = 400,
            y           = 34620,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F4,
            word_18     = 0x1FE1,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -5060,
            z           = 400,
            y           = 34970,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F7,
            word_18     = 0x1FE2,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -5260,
            z           = 400,
            y           = -35050,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F5,
            word_18     = 0x1FE3,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 4970,
            z           = 400,
            y           = -35230,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F8,
            word_18     = 0x1FE4,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 4920,
            z           = 400,
            y           = -45050,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F4,
            word_18     = 0x1FE5,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -5210,
            z           = 400,
            y           = -44800,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F6,
            word_18     = 0x1FE6,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -35820,
            z           = 400,
            y           = -28320,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F8,
            word_18     = 0x1FE7,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -22620,
            z           = 400,
            y           = -28510,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F4,
            word_18     = 0x1FE8,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -48840,
            z           = 400,
            y           = 2080,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F6,
            word_18     = 0x1FE9,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -41530,
            z           = 400,
            y           = 9460,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F5,
            word_18     = 0x1FEA,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -58380,
            z           = 400,
            y           = 18910,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F4,
            word_18     = 0x1FEB,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -68160,
            z           = 400,
            y           = 28510,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F7,
            word_18     = 0x1FEC,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 24510,
            z           = 400,
            y           = 32220,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F8,
            word_18     = 0x1FED,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 32299,
            z           = 400,
            y           = 24240,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F5,
            word_18     = 0x1FEE,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 28240,
            z           = 400,
            y           = -34620,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F4,
            word_18     = 0x1FEF,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 28550,
            z           = 400,
            y           = -22270,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F6,
            word_18     = 0x1FF0,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -35620,
            z           = 400,
            y           = 28020,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F5,
            word_18     = 0x1FF1,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -21380,
            z           = 400,
            y           = 27940,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F4,
            word_18     = 0x1FF2,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 49370,
            z           = 400,
            y           = 1840,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F7,
            word_18     = 0x1FF3,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 41470,
            z           = 400,
            y           = 9410,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F6,
            word_18     = 0x1FF4,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 56480,
            z           = 400,
            y           = 22770,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F4,
            word_18     = 0x1FF5,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 58240,
            z           = 400,
            y           = 29080,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F5,
            word_18     = 0x1FF6,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 64269,
            z           = 400,
            y           = 30680,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F6,
            word_18     = 0x1FF7,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 69700,
            z           = 400,
            y           = 25930,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F4,
            word_18     = 0x1FF8,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 68230,
            z           = 400,
            y           = 19540,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F8,
            word_18     = 0x1FF9,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 63650,
            z           = 400,
            y           = 17440,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03F5,
            word_18     = 0x1FFA,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x42A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x42A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -63050,
            triggerZ            = -50,
            triggerY            = 23470,
            triggerRange        = 1000,
            actorX              = -63580,
            actorZ              = -50,
            actorY              = 24000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 63180,
            triggerZ            = -50,
            triggerY            = 23570,
            triggerRange        = 1000,
            actorX              = 63680,
            actorZ              = -50,
            actorY              = 24060,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 40,
            triggerZ            = 0,
            triggerY            = 40700,
            triggerRange        = 1000,
            actorX              = 40,
            actorZ              = 0,
            actorY              = 39950,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 40,
            triggerZ            = 0,
            triggerY            = -39300,
            triggerRange        = 1000,
            actorX              = 40,
            actorZ              = 0,
            actorY              = -40050,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -44740,
            triggerZ            = 0,
            triggerY            = 5210,
            triggerRange        = 1000,
            actorX              = -45200,
            actorZ              = 0,
            actorY              = 5680,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -28740,
            triggerZ            = 0,
            triggerY            = -28820,
            triggerRange        = 1000,
            actorX              = -28270,
            actorZ              = 0,
            actorY              = -28350,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 27840,
            triggerZ            = 0,
            triggerY            = 27760,
            triggerRange        = 1000,
            actorX              = 28280,
            actorZ              = 0,
            actorY              = 28190,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -27740,
            triggerZ            = 0,
            triggerY            = 27880,
            triggerRange        = 1000,
            actorX              = -28270,
            actorZ              = 0,
            actorY              = 28280,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 28880,
            triggerZ            = 0,
            triggerY            = -28720,
            triggerRange        = 1000,
            actorX              = 28380,
            actorZ              = 0,
            actorY              = -28280,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 44780,
            triggerZ            = -50,
            triggerY            = 5110,
            triggerRange        = 1000,
            actorX              = 45180,
            actorZ              = -50,
            actorY              = 5630,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x592
@scena.Code('Init')
def Init():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_5B2'),
        (0x00000065, 'loc_5B9'),
        (0x00000066, 'loc_5C0'),
        (0x00000067, 'loc_5C7'),
        (0x00000068, 'loc_5CE'),
        (0x00000069, 'loc_5D5'),
        (-1, 'loc_5DC'),
    )

    def _loc_5B2(): pass

    label('loc_5B2')

    Event(0, func_0C_136B)

    Jump('loc_5DC')

    def _loc_5B9(): pass

    label('loc_5B9')

    Event(0, func_0E_14E3)

    Jump('loc_5DC')

    def _loc_5C0(): pass

    label('loc_5C0')

    Event(0, func_10_165B)

    Jump('loc_5DC')

    def _loc_5C7(): pass

    label('loc_5C7')

    Event(0, func_12_17D3)

    Jump('loc_5DC')

    def _loc_5CE(): pass

    label('loc_5CE')

    Event(0, func_14_1966)

    Jump('loc_5DC')

    def _loc_5D5(): pass

    label('loc_5D5')

    Event(0, func_16_1AF9)

    Jump('loc_5DC')

    def _loc_5DC(): pass

    label('loc_5DC')

    Return()

# id: 0x0001 offset: 0x5DD
@scena.Code('func_01_5DD')
def func_01_5DD():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F2, 2, 0x1F92)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5EF',
    )

    OP_6F(0x0000, 0)

    Jump('loc_5F6')

    def _loc_5EF(): pass

    label('loc_5EF')

    OP_6F(0x0000, 60)

    def _loc_5F6(): pass

    label('loc_5F6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F2, 4, 0x1F94)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_608',
    )

    OP_6F(0x0001, 0)

    Jump('loc_60F')

    def _loc_608(): pass

    label('loc_608')

    OP_6F(0x0001, 60)

    def _loc_60F(): pass

    label('loc_60F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F2, 6, 0x1F96)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_621',
    )

    OP_6F(0x0002, 0)

    Jump('loc_628')

    def _loc_621(): pass

    label('loc_621')

    OP_6F(0x0002, 60)

    def _loc_628(): pass

    label('loc_628')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F2, 7, 0x1F97)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_63A',
    )

    OP_6F(0x0003, 0)

    Jump('loc_641')

    def _loc_63A(): pass

    label('loc_63A')

    OP_6F(0x0003, 60)

    def _loc_641(): pass

    label('loc_641')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F3, 0, 0x1F98)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_653',
    )

    OP_6F(0x0004, 0)

    Jump('loc_65A')

    def _loc_653(): pass

    label('loc_653')

    OP_6F(0x0004, 60)

    def _loc_65A(): pass

    label('loc_65A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F3, 1, 0x1F99)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_66C',
    )

    OP_6F(0x0005, 0)

    Jump('loc_673')

    def _loc_66C(): pass

    label('loc_66C')

    OP_6F(0x0005, 60)

    def _loc_673(): pass

    label('loc_673')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F4, 0, 0x1FA0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_685',
    )

    OP_6F(0x0006, 0)

    Jump('loc_68C')

    def _loc_685(): pass

    label('loc_685')

    OP_6F(0x0006, 60)

    def _loc_68C(): pass

    label('loc_68C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F4, 1, 0x1FA1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_69E',
    )

    OP_6F(0x0007, 0)

    Jump('loc_6A5')

    def _loc_69E(): pass

    label('loc_69E')

    OP_6F(0x0007, 60)

    def _loc_6A5(): pass

    label('loc_6A5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F4, 2, 0x1FA2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6B7',
    )

    OP_6F(0x0008, 0)

    Jump('loc_6BE')

    def _loc_6B7(): pass

    label('loc_6B7')

    OP_6F(0x0008, 60)

    def _loc_6BE(): pass

    label('loc_6BE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F4, 3, 0x1FA3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6D0',
    )

    OP_6F(0x0009, 0)

    Jump('loc_6D7')

    def _loc_6D0(): pass

    label('loc_6D0')

    OP_6F(0x0009, 60)

    def _loc_6D7(): pass

    label('loc_6D7')

    LoadEffect(0x00, 'map\\\\mp049_21.eff')
    LoadEffect(0x01, 'map\\\\mp049_22.eff')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03FB, 7, 0x1FDF)),
            Expr.Return,
        ),
        'loc_70B',
    )

    ChrSetFlags(0x0008, 0x0080)

    def _loc_70B(): pass

    label('loc_70B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03FC, 0, 0x1FE0)),
            Expr.Return,
        ),
        'loc_717',
    )

    ChrSetFlags(0x0009, 0x0080)

    def _loc_717(): pass

    label('loc_717')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03FC, 1, 0x1FE1)),
            Expr.Return,
        ),
        'loc_723',
    )

    ChrSetFlags(0x000A, 0x0080)

    def _loc_723(): pass

    label('loc_723')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03FC, 2, 0x1FE2)),
            Expr.Return,
        ),
        'loc_72F',
    )

    ChrSetFlags(0x000B, 0x0080)

    def _loc_72F(): pass

    label('loc_72F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03FC, 3, 0x1FE3)),
            Expr.Return,
        ),
        'loc_73B',
    )

    ChrSetFlags(0x000C, 0x0080)

    def _loc_73B(): pass

    label('loc_73B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03FC, 4, 0x1FE4)),
            Expr.Return,
        ),
        'loc_747',
    )

    ChrSetFlags(0x000D, 0x0080)

    def _loc_747(): pass

    label('loc_747')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03FC, 5, 0x1FE5)),
            Expr.Return,
        ),
        'loc_753',
    )

    ChrSetFlags(0x000E, 0x0080)

    def _loc_753(): pass

    label('loc_753')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03FC, 6, 0x1FE6)),
            Expr.Return,
        ),
        'loc_75F',
    )

    ChrSetFlags(0x000F, 0x0080)

    def _loc_75F(): pass

    label('loc_75F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03FC, 7, 0x1FE7)),
            Expr.Return,
        ),
        'loc_76B',
    )

    ChrSetFlags(0x0010, 0x0080)

    def _loc_76B(): pass

    label('loc_76B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03FD, 0, 0x1FE8)),
            Expr.Return,
        ),
        'loc_777',
    )

    ChrSetFlags(0x0011, 0x0080)

    def _loc_777(): pass

    label('loc_777')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03FD, 1, 0x1FE9)),
            Expr.Return,
        ),
        'loc_783',
    )

    ChrSetFlags(0x0012, 0x0080)

    def _loc_783(): pass

    label('loc_783')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03FD, 2, 0x1FEA)),
            Expr.Return,
        ),
        'loc_78F',
    )

    ChrSetFlags(0x0013, 0x0080)

    def _loc_78F(): pass

    label('loc_78F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03FD, 3, 0x1FEB)),
            Expr.Return,
        ),
        'loc_79B',
    )

    ChrSetFlags(0x0014, 0x0080)

    def _loc_79B(): pass

    label('loc_79B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03FD, 4, 0x1FEC)),
            Expr.Return,
        ),
        'loc_7A7',
    )

    ChrSetFlags(0x0015, 0x0080)

    def _loc_7A7(): pass

    label('loc_7A7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03FD, 5, 0x1FED)),
            Expr.Return,
        ),
        'loc_7B3',
    )

    ChrSetFlags(0x0016, 0x0080)

    def _loc_7B3(): pass

    label('loc_7B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03FD, 6, 0x1FEE)),
            Expr.Return,
        ),
        'loc_7BF',
    )

    ChrSetFlags(0x0017, 0x0080)

    def _loc_7BF(): pass

    label('loc_7BF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03FD, 7, 0x1FEF)),
            Expr.Return,
        ),
        'loc_7CB',
    )

    ChrSetFlags(0x0018, 0x0080)

    def _loc_7CB(): pass

    label('loc_7CB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03FE, 0, 0x1FF0)),
            Expr.Return,
        ),
        'loc_7D7',
    )

    ChrSetFlags(0x0019, 0x0080)

    def _loc_7D7(): pass

    label('loc_7D7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03FE, 1, 0x1FF1)),
            Expr.Return,
        ),
        'loc_7E3',
    )

    ChrSetFlags(0x001A, 0x0080)

    def _loc_7E3(): pass

    label('loc_7E3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03FE, 2, 0x1FF2)),
            Expr.Return,
        ),
        'loc_7EF',
    )

    ChrSetFlags(0x001B, 0x0080)

    def _loc_7EF(): pass

    label('loc_7EF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03FE, 3, 0x1FF3)),
            Expr.Return,
        ),
        'loc_7FB',
    )

    ChrSetFlags(0x001C, 0x0080)

    def _loc_7FB(): pass

    label('loc_7FB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03FE, 4, 0x1FF4)),
            Expr.Return,
        ),
        'loc_807',
    )

    ChrSetFlags(0x001D, 0x0080)

    def _loc_807(): pass

    label('loc_807')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03FE, 5, 0x1FF5)),
            Expr.Return,
        ),
        'loc_813',
    )

    ChrSetFlags(0x001E, 0x0080)

    def _loc_813(): pass

    label('loc_813')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03FE, 6, 0x1FF6)),
            Expr.Return,
        ),
        'loc_81F',
    )

    ChrSetFlags(0x001F, 0x0080)

    def _loc_81F(): pass

    label('loc_81F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03FE, 7, 0x1FF7)),
            Expr.Return,
        ),
        'loc_82B',
    )

    ChrSetFlags(0x0020, 0x0080)

    def _loc_82B(): pass

    label('loc_82B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03FF, 0, 0x1FF8)),
            Expr.Return,
        ),
        'loc_837',
    )

    ChrSetFlags(0x0021, 0x0080)

    def _loc_837(): pass

    label('loc_837')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03FF, 1, 0x1FF9)),
            Expr.Return,
        ),
        'loc_843',
    )

    ChrSetFlags(0x0022, 0x0080)

    def _loc_843(): pass

    label('loc_843')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03FF, 2, 0x1FFA)),
            Expr.Return,
        ),
        'loc_84F',
    )

    ChrSetFlags(0x0023, 0x0080)

    def _loc_84F(): pass

    label('loc_84F')

    OP_1B(0x00, 0x00, 0x000D)
    OP_1B(0x01, 0x00, 0x000F)
    OP_1B(0x02, 0x00, 0x0011)
    OP_1B(0x03, 0x00, 0x0013)
    OP_1B(0x04, 0x00, 0x0015)
    OP_1B(0x05, 0x00, 0x0017)

    Return()

# id: 0x0002 offset: 0x86E
@scena.Code('func_02_86E')
def func_02_86E():
    UnlockAchievement(0x02, 0x0069, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F2, 2, 0x1F92)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_94B',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['太极服'], 1)"),
            Expr.Return,
        ),
        'loc_8E2',
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
    SetScenaFlags(ScenaFlag(0x03F2, 2, 0x1F92))

    Jump('loc_948')

    def _loc_8E2(): pass

    label('loc_8E2')

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
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0)

    def _loc_948(): pass

    label('loc_948')

    Jump('loc_97C')

    def _loc_94B(): pass

    label('loc_94B')

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
    def _loc_97C(): pass

    label('loc_97C')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x98A
@scena.Code('func_03_98A')
def func_03_98A():
    UnlockAchievement(0x02, 0x006A, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F2, 4, 0x1F94)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A67',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['蓝色猎鹰'], 1)"),
            Expr.Return,
        ),
        'loc_9FE',
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
    SetScenaFlags(ScenaFlag(0x03F2, 4, 0x1F94))

    Jump('loc_A64')

    def _loc_9FE(): pass

    label('loc_9FE')

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
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0)

    def _loc_A64(): pass

    label('loc_A64')

    Jump('loc_A98')

    def _loc_A67(): pass

    label('loc_A67')

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
    def _loc_A98(): pass

    label('loc_A98')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0xAA6
@scena.Code('func_04_AA6')
def func_04_AA6():
    UnlockAchievement(0x02, 0x006B, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F2, 6, 0x1F96)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B83',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['大回复药'], 1)"),
            Expr.Return,
        ),
        'loc_B1A',
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
    SetScenaFlags(ScenaFlag(0x03F2, 6, 0x1F96))

    Jump('loc_B80')

    def _loc_B1A(): pass

    label('loc_B1A')

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
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0)

    def _loc_B80(): pass

    label('loc_B80')

    Jump('loc_BB4')

    def _loc_B83(): pass

    label('loc_B83')

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
    def _loc_BB4(): pass

    label('loc_BB4')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0xBC2
@scena.Code('func_05_BC2')
def func_05_BC2():
    UnlockAchievement(0x02, 0x006C, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F2, 7, 0x1F97)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C9F',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0003, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅱ'], 1)"),
            Expr.Return,
        ),
        'loc_C36',
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
    SetScenaFlags(ScenaFlag(0x03F2, 7, 0x1F97))

    Jump('loc_C9C')

    def _loc_C36(): pass

    label('loc_C36')

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
    OP_6F(0x0003, 60)
    OP_70(0x0003, 0)

    def _loc_C9C(): pass

    label('loc_C9C')

    Jump('loc_CD0')

    def _loc_C9F(): pass

    label('loc_C9F')

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
    def _loc_CD0(): pass

    label('loc_CD0')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0xCDE
@scena.Code('func_06_CDE')
def func_06_CDE():
    UnlockAchievement(0x02, 0x006D, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F3, 0, 0x1F98)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DBB',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0004, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['还魂胶囊'], 1)"),
            Expr.Return,
        ),
        'loc_D52',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['还魂胶囊']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03F3, 0, 0x1F98))

    Jump('loc_DB8')

    def _loc_D52(): pass

    label('loc_D52')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['还魂胶囊']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['还魂胶囊']),
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

    def _loc_DB8(): pass

    label('loc_DB8')

    Jump('loc_DEC')

    def _loc_DBB(): pass

    label('loc_DBB')

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
    def _loc_DEC(): pass

    label('loc_DEC')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0xDFA
@scena.Code('func_07_DFA')
def func_07_DFA():
    UnlockAchievement(0x02, 0x006E, 0x00)
    MapSetFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F3, 1, 0x1F99)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_ECF',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0005, 30)
    OP_73(0x0005)
    OP_6F(0x0005, 30)
    AddSepith(0x00, 300)
    AddSepith(0x04, 100)
    AddSepith(0x05, 100)
    AddSepith(0x06, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#56I地之耀晶片×３００\n',
            (TxtCtl.SetColor, 0x2),
            '#62I时之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x2),
            '#60I空之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x2),
            '#61I幻之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    SetScenaFlags(ScenaFlag(0x03F3, 1, 0x1F99))

    Jump('loc_EE9')

    def _loc_ECF(): pass

    label('loc_ECF')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_EE9(): pass

    label('loc_EE9')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0xEFB
@scena.Code('func_08_EFB')
def func_08_EFB():
    UnlockAchievement(0x02, 0x006F, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F4, 0, 0x1FA0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_FD8',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0006, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['Ｓ－药片'], 1)"),
            Expr.Return,
        ),
        'loc_F6F',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['Ｓ－药片']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03F4, 0, 0x1FA0))

    Jump('loc_FD5')

    def _loc_F6F(): pass

    label('loc_F6F')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['Ｓ－药片']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['Ｓ－药片']),
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

    def _loc_FD5(): pass

    label('loc_FD5')

    Jump('loc_1009')

    def _loc_FD8(): pass

    label('loc_FD8')

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
    def _loc_1009(): pass

    label('loc_1009')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0009 offset: 0x1017
@scena.Code('func_09_1017')
def func_09_1017():
    UnlockAchievement(0x02, 0x0070, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F4, 1, 0x1FA1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_10F4',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0007, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['痊愈之药'], 1)"),
            Expr.Return,
        ),
        'loc_108B',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['痊愈之药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03F4, 1, 0x1FA1))

    Jump('loc_10F1')

    def _loc_108B(): pass

    label('loc_108B')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['痊愈之药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['痊愈之药']),
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

    def _loc_10F1(): pass

    label('loc_10F1')

    Jump('loc_1125')

    def _loc_10F4(): pass

    label('loc_10F4')

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
    def _loc_1125(): pass

    label('loc_1125')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x000A offset: 0x1133
@scena.Code('func_0A_1133')
def func_0A_1133():
    UnlockAchievement(0x02, 0x0071, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F4, 2, 0x1FA2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1210',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0008, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['幻影戒指'], 1)"),
            Expr.Return,
        ),
        'loc_11A7',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['幻影戒指']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03F4, 2, 0x1FA2))

    Jump('loc_120D')

    def _loc_11A7(): pass

    label('loc_11A7')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['幻影戒指']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['幻影戒指']),
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

    def _loc_120D(): pass

    label('loc_120D')

    Jump('loc_1241')

    def _loc_1210(): pass

    label('loc_1210')

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
    def _loc_1241(): pass

    label('loc_1241')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x000B offset: 0x124F
@scena.Code('func_0B_124F')
def func_0B_124F():
    UnlockAchievement(0x02, 0x0072, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03F4, 3, 0x1FA3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_132C',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0009, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['全回复药'], 1)"),
            Expr.Return,
        ),
        'loc_12C3',
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
    SetScenaFlags(ScenaFlag(0x03F4, 3, 0x1FA3))

    Jump('loc_1329')

    def _loc_12C3(): pass

    label('loc_12C3')

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
    OP_6F(0x0009, 60)
    OP_70(0x0009, 0)

    def _loc_1329(): pass

    label('loc_1329')

    Jump('loc_135D')

    def _loc_132C(): pass

    label('loc_132C')

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
    def _loc_135D(): pass

    label('loc_135D')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x000C offset: 0x136B
@scena.Code('func_0C_136B')
def func_0C_136B():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(0, 200, 66500, 0)
    ChrSetPos(0x0101, 500, 200, 66000, 180)
    ChrSetPos(0x0102, -500, 200, 66000, 180)
    ChrSetPos(0x00F8, 500, 200, 67000, 180)
    ChrSetPos(0x00F9, -500, 200, 67000, 180)
    ChrSetRGBAMask(0x0000, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0001, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0002, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0003, 255, 255, 255, 0, 0)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x0018)
    Call(0, 0x001A)
    Fade(500)
    CameraMove(70, 200, 64620, 0)
    ChrSetPos(0x0000, 70, 200, 64620, 180)
    ChrSetPos(0x0001, 70, 200, 64620, 180)
    ChrSetPos(0x0002, 70, 200, 64620, 180)
    ChrSetPos(0x0003, 70, 200, 64620, 180)
    MapSetFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x000D offset: 0x146B
@scena.Code('func_0D_146B')
def func_0D_146B():
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
    CameraMove(0, 200, 66500, 0)
    ChrSetPos(0x0101, -500, 200, 67000, 0)
    ChrSetPos(0x0102, 500, 200, 67000, 0)
    ChrSetPos(0x00F8, -500, 200, 66000, 0)
    ChrSetPos(0x00F9, 500, 200, 66000, 0)
    OP_0D()
    Call(0, 0x0018)
    Call(0, 0x001B)
    NewScene('ED6_DT21/C1700._SN', 101, 0, 0)
    IdleLoop()

    Return()

# id: 0x000E offset: 0x14E3
@scena.Code('func_0E_14E3')
def func_0E_14E3():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(-46600, 200, 47300, 0)
    ChrSetPos(0x0101, -46100, 200, 46800, 180)
    ChrSetPos(0x0102, -47100, 200, 46800, 180)
    ChrSetPos(0x00F8, -46100, 200, 47800, 180)
    ChrSetPos(0x00F9, -47100, 200, 47800, 180)
    ChrSetRGBAMask(0x0000, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0001, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0002, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0003, 255, 255, 255, 0, 0)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x0018)
    Call(0, 0x001A)
    Fade(500)
    CameraMove(-46580, 200, 45210, 0)
    ChrSetPos(0x0000, -46580, 200, 45210, 180)
    ChrSetPos(0x0001, -46580, 200, 45210, 180)
    ChrSetPos(0x0002, -46580, 200, 45210, 180)
    ChrSetPos(0x0003, -46580, 200, 45210, 180)
    MapSetFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x000F offset: 0x15E3
@scena.Code('func_0F_15E3')
def func_0F_15E3():
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
    CameraMove(-46600, 200, 47300, 0)
    ChrSetPos(0x0101, -47100, 200, 47800, 0)
    ChrSetPos(0x0102, -46100, 200, 47800, 0)
    ChrSetPos(0x00F8, -47100, 200, 46800, 0)
    ChrSetPos(0x00F9, -46100, 200, 46800, 0)
    OP_0D()
    Call(0, 0x0018)
    Call(0, 0x001B)
    NewScene('ED6_DT21/C1702._SN', 101, 0, 0)
    IdleLoop()

    Return()

# id: 0x0010 offset: 0x165B
@scena.Code('func_10_165B')
def func_10_165B():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(46700, 200, 47200, 0)
    ChrSetPos(0x0101, 47200, 200, 46700, 180)
    ChrSetPos(0x0102, 46200, 200, 46700, 180)
    ChrSetPos(0x00F8, 47200, 200, 47700, 180)
    ChrSetPos(0x00F9, 46200, 200, 47700, 180)
    ChrSetRGBAMask(0x0000, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0001, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0002, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0003, 255, 255, 255, 0, 0)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x0018)
    Call(0, 0x001A)
    Fade(500)
    CameraMove(46730, 200, 45190, 0)
    ChrSetPos(0x0000, 46730, 200, 45190, 180)
    ChrSetPos(0x0001, 46730, 200, 45190, 180)
    ChrSetPos(0x0002, 46730, 200, 45190, 180)
    ChrSetPos(0x0003, 46730, 200, 45190, 180)
    MapSetFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x0011 offset: 0x175B
@scena.Code('func_11_175B')
def func_11_175B():
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
    CameraMove(46700, 200, 47200, 0)
    ChrSetPos(0x0101, 46200, 200, 47700, 0)
    ChrSetPos(0x0102, 47200, 200, 47700, 0)
    ChrSetPos(0x00F8, 46200, 200, 46700, 0)
    ChrSetPos(0x00F9, 47200, 200, 46700, 0)
    OP_0D()
    Call(0, 0x0018)
    Call(0, 0x001B)
    NewScene('ED6_DT21/C1702._SN', 102, 0, 0)
    IdleLoop()

    Return()

# id: 0x0012 offset: 0x17D3
@scena.Code('func_12_17D3')
def func_12_17D3():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(0, 200, -66500, 0)
    OP_6C(135000, 0)
    ChrSetPos(0x0101, -500, 200, -66000, 0)
    ChrSetPos(0x0102, 500, 200, -66000, 0)
    ChrSetPos(0x00F8, -500, 200, -67000, 0)
    ChrSetPos(0x00F9, 500, 200, -67000, 0)
    ChrSetRGBAMask(0x0000, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0001, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0002, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0003, 255, 255, 255, 0, 0)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x0019)
    Call(0, 0x001A)
    Fade(500)
    CameraMove(-90, 200, -64500, 0)
    OP_6C(45000, 0)
    ChrSetPos(0x0000, -90, 200, -64500, 0)
    ChrSetPos(0x0001, -90, 200, -64500, 0)
    ChrSetPos(0x0002, -90, 200, -64500, 0)
    ChrSetPos(0x0003, -90, 200, -64500, 0)
    MapSetFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x0013 offset: 0x18E5
@scena.Code('func_13_18E5')
def func_13_18E5():
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
    CameraMove(0, 200, -66500, 0)
    OP_6C(135000, 0)
    ChrSetPos(0x0101, 500, 200, -67000, 180)
    ChrSetPos(0x0102, -500, 200, -67000, 180)
    ChrSetPos(0x00F8, 500, 200, -66000, 180)
    ChrSetPos(0x00F9, -500, 200, -66000, 180)
    OP_0D()
    Call(0, 0x0019)
    Call(0, 0x001B)
    NewScene('ED6_DT21/C1702._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0014 offset: 0x1966
@scena.Code('func_14_1966')
def func_14_1966():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(46600, 200, -47000, 0)
    OP_6C(135000, 0)
    ChrSetPos(0x0101, 46100, 200, -46500, 0)
    ChrSetPos(0x0102, 47100, 200, -46500, 0)
    ChrSetPos(0x00F8, 46100, 200, -47500, 0)
    ChrSetPos(0x00F9, 47100, 200, -47500, 0)
    ChrSetRGBAMask(0x0000, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0001, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0002, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0003, 255, 255, 255, 0, 0)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x0019)
    Call(0, 0x001A)
    Fade(500)
    CameraMove(46590, 200, -45090, 0)
    OP_6C(45000, 0)
    ChrSetPos(0x0000, 46590, 200, -45090, 0)
    ChrSetPos(0x0001, 46590, 200, -45090, 0)
    ChrSetPos(0x0002, 46590, 200, -45090, 0)
    ChrSetPos(0x0003, 46590, 200, -45090, 0)
    MapSetFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x0015 offset: 0x1A78
@scena.Code('func_15_1A78')
def func_15_1A78():
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
    CameraMove(46600, 200, -47000, 0)
    OP_6C(135000, 0)
    ChrSetPos(0x0101, 47100, 200, -47500, 180)
    ChrSetPos(0x0102, 46100, 200, -47500, 180)
    ChrSetPos(0x00F8, 47100, 200, -46500, 180)
    ChrSetPos(0x00F9, 46100, 200, -46500, 180)
    OP_0D()
    Call(0, 0x0019)
    Call(0, 0x001B)
    NewScene('ED6_DT21/C1702._SN', 103, 0, 0)
    IdleLoop()

    Return()

# id: 0x0016 offset: 0x1AF9
@scena.Code('func_16_1AF9')
def func_16_1AF9():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(-46600, 200, -47000, 0)
    OP_6C(135000, 0)
    ChrSetPos(0x0101, -47100, 200, -46500, 0)
    ChrSetPos(0x0102, -46100, 200, -46500, 0)
    ChrSetPos(0x00F8, -47100, 200, -47500, 0)
    ChrSetPos(0x00F9, -46100, 200, -47500, 0)
    ChrSetRGBAMask(0x0000, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0001, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0002, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0003, 255, 255, 255, 0, 0)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x0019)
    Call(0, 0x001A)
    Fade(500)
    CameraMove(-46720, 200, -45050, 0)
    OP_6C(45000, 0)
    ChrSetPos(0x0000, -46720, 200, -45050, 0)
    ChrSetPos(0x0001, -46720, 200, -45050, 0)
    ChrSetPos(0x0002, -46720, 200, -45050, 0)
    ChrSetPos(0x0003, -46720, 200, -45050, 0)
    MapSetFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x0017 offset: 0x1C0B
@scena.Code('func_17_1C0B')
def func_17_1C0B():
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
    CameraMove(-46600, 200, -47000, 0)
    OP_6C(135000, 0)
    ChrSetPos(0x0101, -46100, 200, -47500, 180)
    ChrSetPos(0x0102, -47100, 200, -47500, 180)
    ChrSetPos(0x00F8, -46100, 200, -46500, 180)
    ChrSetPos(0x00F9, -47100, 200, -46500, 180)
    OP_0D()
    Call(0, 0x0019)
    Call(0, 0x001B)
    NewScene('ED6_DT21/C1702._SN', 104, 0, 0)
    IdleLoop()

    Return()

# id: 0x0018 offset: 0x1C8C
@scena.Code('func_18_1C8C')
def func_18_1C8C():
    PlayEffect(0x00, 0xFF, 0x0000, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0001, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0002, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0003, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(153, 0x00, 0x64)
    PlaySE(184, 0x00, 0x64)

    Return()

# id: 0x0019 offset: 0x1D6B
@scena.Code('func_19_1D6B')
def func_19_1D6B():
    PlayEffect(0x01, 0xFF, 0x0000, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0001, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0002, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0003, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(153, 0x00, 0x64)
    PlaySE(184, 0x00, 0x64)

    Return()

# id: 0x001A offset: 0x1E4A
@scena.Code('func_1A_1E4A')
def func_1A_1E4A():
    @scena.Lambda('lambda_1E50')
    def lambda_1E50():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_1E50)

    @scena.Lambda('lambda_1E62')
    def lambda_1E62():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_1E62)

    @scena.Lambda('lambda_1E74')
    def lambda_1E74():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_1E74)

    @scena.Lambda('lambda_1E86')
    def lambda_1E86():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_1E86)

    Sleep(2500)

    Return()

# id: 0x001B offset: 0x1E98
@scena.Code('func_1B_1E98')
def func_1B_1E98():
    @scena.Lambda('lambda_1E9E')
    def lambda_1E9E():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_1E9E)

    @scena.Lambda('lambda_1EB0')
    def lambda_1EB0():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_1EB0)

    @scena.Lambda('lambda_1EC2')
    def lambda_1EC2():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_1EC2)

    @scena.Lambda('lambda_1ED4')
    def lambda_1ED4():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_1ED4)

    Sleep(2000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

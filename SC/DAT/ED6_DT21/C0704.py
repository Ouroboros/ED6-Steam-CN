import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C0704_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C0704   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
    TXT(0x02, ''),
    TXT(0x03, ''),
    TXT(0x04, ''),
    TXT(0x05, ''),
    TXT(0x06, ''),
    TXT(0x07, ''),
    TXT(0x08, ''),
    TXT(0x09, ''),
    TXT(0x0A, ''),
    TXT(0x0B, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0704.x'
    header.mapIndex       = 1
    header.bgm            = 60
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x2100
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
        ('ED6_DT29/CH12590._CH', 'ED6_DT29/CH12590P._CP'),
        ('ED6_DT29/CH12591._CH', 'ED6_DT29/CH12591P._CP'),
        ('ED6_DT29/CH12600._CH', 'ED6_DT29/CH12600P._CP'),
        ('ED6_DT29/CH12601._CH', 'ED6_DT29/CH12601P._CP'),
        ('ED6_DT29/CH12610._CH', 'ED6_DT29/CH12610P._CP'),
        ('ED6_DT29/CH12611._CH', 'ED6_DT29/CH12611P._CP'),
        ('ED6_DT29/CH12620._CH', 'ED6_DT29/CH12620P._CP'),
        ('ED6_DT29/CH12621._CH', 'ED6_DT29/CH12621P._CP'),
        ('ED6_DT29/CH12630._CH', 'ED6_DT29/CH12630P._CP'),
        ('ED6_DT29/CH12631._CH', 'ED6_DT29/CH12631P._CP'),
        ('ED6_DT29/CH12640._CH', 'ED6_DT29/CH12640P._CP'),
        ('ED6_DT29/CH12641._CH', 'ED6_DT29/CH12641P._CP'),
    ]

# id: 0x10002 offset: 0x10A
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0x10A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -4220,
            z           = 400,
            y           = -6080,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03EC,
            word_18     = 0x1FD4,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 6080,
            z           = 400,
            y           = -4800,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03E8,
            word_18     = 0x1FD5,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 5440,
            z           = 400,
            y           = 4640,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03EC,
            word_18     = 0x1FD6,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -4850,
            z           = 400,
            y           = 4550,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03E9,
            word_18     = 0x1FD7,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -190,
            z           = -4000,
            y           = 42600,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03EC,
            word_18     = 0x1FD8,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -4670,
            z           = -3600,
            y           = 37330,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03EA,
            word_18     = 0x1FD9,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -4680,
            z           = -3600,
            y           = 47440,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03EA,
            word_18     = 0x1FDA,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 5340,
            z           = -3600,
            y           = 47490,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03EA,
            word_18     = 0x1FDB,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 5120,
            z           = -3600,
            y           = 37300,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03EA,
            word_18     = 0x1FDC,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 21700,
            z           = -4050,
            y           = 20880,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x03EC,
            word_18     = 0x1FDD,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x222
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x222
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -20580,
            triggerZ            = -15200,
            triggerY            = 41200,
            triggerRange        = 1000,
            actorX              = -19850,
            actorZ              = -15200,
            actorY              = 40980,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 48480,
            triggerZ            = -7600,
            triggerY            = 5760,
            triggerRange        = 1000,
            actorX              = 48450,
            actorZ              = -7600,
            actorY              = 6350,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -25120,
            triggerZ            = -14800,
            triggerY            = 46340,
            triggerRange        = 1000,
            actorX              = -25520,
            actorZ              = -14800,
            actorY              = 46750,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -14570,
            triggerZ            = -14800,
            triggerY            = 46130,
            triggerRange        = 1000,
            actorX              = -14130,
            actorZ              = -14800,
            actorY              = 46610,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -14670,
            triggerZ            = -14800,
            triggerY            = 35810,
            triggerRange        = 1000,
            actorX              = -14270,
            actorZ              = -14800,
            actorY              = 35400,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -24890,
            triggerZ            = -14800,
            triggerY            = 35860,
            triggerRange        = 1000,
            actorX              = -25360,
            actorZ              = -14800,
            actorY              = 35390,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 43290,
            triggerZ            = -7200,
            triggerY            = 1360,
            triggerRange        = 1000,
            actorX              = 42850,
            actorZ              = -7200,
            actorY              = 920,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 43470,
            triggerZ            = -7200,
            triggerY            = 11820,
            triggerRange        = 1000,
            actorX              = 43000,
            actorZ              = -7200,
            actorY              = 12160,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 53990,
            triggerZ            = -7200,
            triggerY            = 11500,
            triggerRange        = 1000,
            actorX              = 54490,
            actorZ              = -7200,
            actorY              = 12000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 53690,
            triggerZ            = -7200,
            triggerY            = 1320,
            triggerRange        = 1000,
            actorX              = 54280,
            actorZ              = -7200,
            actorY              = 730,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 26950,
            triggerZ            = -3600,
            triggerY            = 26260,
            triggerRange        = 1000,
            actorX              = 27410,
            actorZ              = -3600,
            actorY              = 26680,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000C,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 26820,
            triggerZ            = -3600,
            triggerY            = 15820,
            triggerRange        = 1000,
            actorX              = 27280,
            actorZ              = -3600,
            actorY              = 15350,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000D,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 16460,
            triggerZ            = -3600,
            triggerY            = 15780,
            triggerRange        = 1000,
            actorX              = 16030,
            actorZ              = -3600,
            actorY              = 15340,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000E,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 16610,
            triggerZ            = -3600,
            triggerY            = 26290,
            triggerRange        = 1000,
            actorX              = 16140,
            actorZ              = -3600,
            actorY              = 26630,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000F,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -3930,
            triggerZ            = 4000,
            triggerY            = 98030,
            triggerRange        = 1200,
            actorX              = -3930,
            actorZ              = 5200,
            actorY              = 98030,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001C,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x43E
@scena.Code('PreInit')
def PreInit():
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

    Event(0, 0x0010)

    Jump('loc_472')

    def _loc_45D(): pass

    label('loc_45D')

    Event(0, 0x0012)

    Jump('loc_472')

    def _loc_464(): pass

    label('loc_464')

    Event(0, 0x0014)

    Jump('loc_472')

    def _loc_46B(): pass

    label('loc_46B')

    Event(0, 0x0016)

    Jump('loc_472')

    def _loc_472(): pass

    label('loc_472')

    Return()

# id: 0x0001 offset: 0x473
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E2, 0, 0x1F10)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_485',
    )

    OP_6F(0x0000, 0)

    Jump('loc_48C')

    def _loc_485(): pass

    label('loc_485')

    OP_6F(0x0000, 60)

    def _loc_48C(): pass

    label('loc_48C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E2, 2, 0x1F12)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_49E',
    )

    OP_6F(0x0001, 0)

    Jump('loc_4A5')

    def _loc_49E(): pass

    label('loc_49E')

    OP_6F(0x0001, 60)

    def _loc_4A5(): pass

    label('loc_4A5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E2, 4, 0x1F14)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4B7',
    )

    OP_6F(0x0002, 0)

    Jump('loc_4BE')

    def _loc_4B7(): pass

    label('loc_4B7')

    OP_6F(0x0002, 60)

    def _loc_4BE(): pass

    label('loc_4BE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E2, 5, 0x1F15)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4D0',
    )

    OP_6F(0x0003, 0)

    Jump('loc_4D7')

    def _loc_4D0(): pass

    label('loc_4D0')

    OP_6F(0x0003, 60)

    def _loc_4D7(): pass

    label('loc_4D7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E2, 6, 0x1F16)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4E9',
    )

    OP_6F(0x0004, 0)

    Jump('loc_4F0')

    def _loc_4E9(): pass

    label('loc_4E9')

    OP_6F(0x0004, 60)

    def _loc_4F0(): pass

    label('loc_4F0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E2, 7, 0x1F17)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_502',
    )

    OP_6F(0x0005, 0)

    Jump('loc_509')

    def _loc_502(): pass

    label('loc_502')

    OP_6F(0x0005, 60)

    def _loc_509(): pass

    label('loc_509')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E3, 0, 0x1F18)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_51B',
    )

    OP_6F(0x0006, 0)

    Jump('loc_522')

    def _loc_51B(): pass

    label('loc_51B')

    OP_6F(0x0006, 60)

    def _loc_522(): pass

    label('loc_522')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E3, 1, 0x1F19)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_534',
    )

    OP_6F(0x0007, 0)

    Jump('loc_53B')

    def _loc_534(): pass

    label('loc_534')

    OP_6F(0x0007, 60)

    def _loc_53B(): pass

    label('loc_53B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E3, 2, 0x1F1A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_54D',
    )

    OP_6F(0x0008, 0)

    Jump('loc_554')

    def _loc_54D(): pass

    label('loc_54D')

    OP_6F(0x0008, 60)

    def _loc_554(): pass

    label('loc_554')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E3, 3, 0x1F1B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_566',
    )

    OP_6F(0x0009, 0)

    Jump('loc_56D')

    def _loc_566(): pass

    label('loc_566')

    OP_6F(0x0009, 60)

    def _loc_56D(): pass

    label('loc_56D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E3, 4, 0x1F1C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_57F',
    )

    OP_6F(0x000A, 0)

    Jump('loc_586')

    def _loc_57F(): pass

    label('loc_57F')

    OP_6F(0x000A, 60)

    def _loc_586(): pass

    label('loc_586')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E3, 5, 0x1F1D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_598',
    )

    OP_6F(0x000B, 0)

    Jump('loc_59F')

    def _loc_598(): pass

    label('loc_598')

    OP_6F(0x000B, 60)

    def _loc_59F(): pass

    label('loc_59F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E3, 6, 0x1F1E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5B1',
    )

    OP_6F(0x000C, 0)

    Jump('loc_5B8')

    def _loc_5B1(): pass

    label('loc_5B1')

    OP_6F(0x000C, 60)

    def _loc_5B8(): pass

    label('loc_5B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E3, 7, 0x1F1F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5CA',
    )

    OP_6F(0x000D, 0)

    Jump('loc_5D1')

    def _loc_5CA(): pass

    label('loc_5CA')

    OP_6F(0x000D, 60)

    def _loc_5D1(): pass

    label('loc_5D1')

    LoadEffect(0x00, 'map\\\\mp049_21.eff')
    LoadEffect(0x01, 'map\\\\mp049_22.eff')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03FA, 4, 0x1FD4)),
            Expr.Return,
        ),
        'loc_605',
    )

    SetChrFlags(0x0008, 0x0080)

    def _loc_605(): pass

    label('loc_605')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03FA, 5, 0x1FD5)),
            Expr.Return,
        ),
        'loc_611',
    )

    SetChrFlags(0x0009, 0x0080)

    def _loc_611(): pass

    label('loc_611')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03FA, 6, 0x1FD6)),
            Expr.Return,
        ),
        'loc_61D',
    )

    SetChrFlags(0x000A, 0x0080)

    def _loc_61D(): pass

    label('loc_61D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03FA, 7, 0x1FD7)),
            Expr.Return,
        ),
        'loc_629',
    )

    SetChrFlags(0x000B, 0x0080)

    def _loc_629(): pass

    label('loc_629')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03FB, 0, 0x1FD8)),
            Expr.Return,
        ),
        'loc_635',
    )

    SetChrFlags(0x000C, 0x0080)

    def _loc_635(): pass

    label('loc_635')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03FB, 1, 0x1FD9)),
            Expr.Return,
        ),
        'loc_641',
    )

    SetChrFlags(0x000D, 0x0080)

    def _loc_641(): pass

    label('loc_641')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03FB, 2, 0x1FDA)),
            Expr.Return,
        ),
        'loc_64D',
    )

    SetChrFlags(0x000E, 0x0080)

    def _loc_64D(): pass

    label('loc_64D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03FB, 3, 0x1FDB)),
            Expr.Return,
        ),
        'loc_659',
    )

    SetChrFlags(0x000F, 0x0080)

    def _loc_659(): pass

    label('loc_659')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03FB, 4, 0x1FDC)),
            Expr.Return,
        ),
        'loc_665',
    )

    SetChrFlags(0x0010, 0x0080)

    def _loc_665(): pass

    label('loc_665')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03FB, 5, 0x1FDD)),
            Expr.Return,
        ),
        'loc_671',
    )

    SetChrFlags(0x0011, 0x0080)

    def _loc_671(): pass

    label('loc_671')

    ExecExpressionWithValue(
        0x000D,
        0x24,
        (
            (Expr.PushLong, 0xCF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x24,
        (
            (Expr.PushLong, 0xCF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x24,
        (
            (Expr.PushLong, 0xCF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0010,
        0x24,
        (
            (Expr.PushLong, 0xCF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_1B(0x00, 0x00, 0x0011)
    OP_1B(0x01, 0x00, 0x0013)
    OP_1B(0x02, 0x00, 0x0015)
    OP_1B(0x03, 0x00, 0x0017)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_71C',
    )

    LoadEffect(0x02, 'map\\\\mp027_00.eff')
    PlayEffect(0x02, 0x02, 0x00FF, -3930, 5200, 98030, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    OP_71(0x0010, 0x0020)
    OP_6F(0x0010, 0)
    OP_70(0x0010, 0x000000FA)

    Jump('loc_728')

    def _loc_71C(): pass

    label('loc_71C')

    OP_72(0x0010, 0x0020)
    OP_6F(0x0010, 250)

    def _loc_728(): pass

    label('loc_728')

    Return()

# id: 0x0002 offset: 0x729
@scena.Code('ReInit')
def ReInit():
    UnlockAchievement(0x02, 0x1C, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E2, 0, 0x1F10)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_806',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0000, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['轻钢靴'], 1)"),
            Expr.Return,
        ),
        'loc_79D',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['轻钢靴']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1F10)

    Jump('loc_803')

    def _loc_79D(): pass

    label('loc_79D')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['轻钢靴']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['轻钢靴']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0x00000000)

    def _loc_803(): pass

    label('loc_803')

    Jump('loc_837')

    def _loc_806(): pass

    label('loc_806')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    def _loc_837(): pass

    label('loc_837')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x845
@scena.Code('func_03_845')
def func_03_845():
    UnlockAchievement(0x02, 0x1D, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E2, 2, 0x1F12)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_922',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0001, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['蓝色猎鹰'], 1)"),
            Expr.Return,
        ),
        'loc_8B9',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

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
    OP_A2(0x1F12)

    Jump('loc_91F')

    def _loc_8B9(): pass

    label('loc_8B9')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0x00000000)

    def _loc_91F(): pass

    label('loc_91F')

    Jump('loc_953')

    def _loc_922(): pass

    label('loc_922')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    def _loc_953(): pass

    label('loc_953')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x961
@scena.Code('func_04_961')
def func_04_961():
    UnlockAchievement(0x02, 0x1E, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E2, 4, 0x1F14)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A3E',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0002, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['复苏药'], 1)"),
            Expr.Return,
        ),
        'loc_9D5',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['复苏药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1F14)

    Jump('loc_A3B')

    def _loc_9D5(): pass

    label('loc_9D5')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['复苏药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['复苏药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0x00000000)

    def _loc_A3B(): pass

    label('loc_A3B')

    Jump('loc_A6F')

    def _loc_A3E(): pass

    label('loc_A3E')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    def _loc_A6F(): pass

    label('loc_A6F')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0xA7D
@scena.Code('func_05_A7D')
def func_05_A7D():
    UnlockAchievement(0x02, 0x1F, 0x00, 0x00)
    SetMapFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E2, 5, 0x1F15)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B52',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0003, 0x0000001E)
    OP_73(0x0003)
    OP_6F(0x0003, 30)
    AddSepith(0x03, 0x012C)
    AddSepith(0x04, 0x0064)
    AddSepith(0x05, 0x0064)
    AddSepith(0x06, 0x0064)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#59I风之耀晶片×３００\n',
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
    OP_A2(0x1F15)

    Jump('loc_B6C')

    def _loc_B52(): pass

    label('loc_B52')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_B6C(): pass

    label('loc_B6C')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0xB7E
@scena.Code('func_06_B7E')
def func_06_B7E():
    UnlockAchievement(0x02, 0x20, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E2, 6, 0x1F16)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C5B',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0004, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['痊愈之药'], 1)"),
            Expr.Return,
        ),
        'loc_BF2',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

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
    OP_A2(0x1F16)

    Jump('loc_C58')

    def _loc_BF2(): pass

    label('loc_BF2')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0004, 60)
    OP_70(0x0004, 0x00000000)

    def _loc_C58(): pass

    label('loc_C58')

    Jump('loc_C8C')

    def _loc_C5B(): pass

    label('loc_C5B')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    def _loc_C8C(): pass

    label('loc_C8C')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0xC9A
@scena.Code('func_07_C9A')
def func_07_C9A():
    UnlockAchievement(0x02, 0x21, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E2, 7, 0x1F17)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D77',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0005, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅰ'], 1)"),
            Expr.Return,
        ),
        'loc_D0E',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1F17)

    Jump('loc_D74')

    def _loc_D0E(): pass

    label('loc_D0E')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0005, 60)
    OP_70(0x0005, 0x00000000)

    def _loc_D74(): pass

    label('loc_D74')

    Jump('loc_DA8')

    def _loc_D77(): pass

    label('loc_D77')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    def _loc_DA8(): pass

    label('loc_DA8')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0xDB6
@scena.Code('func_08_DB6')
def func_08_DB6():
    UnlockAchievement(0x02, 0x22, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E3, 0, 0x1F18)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E93',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0006, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['全回复药'], 1)"),
            Expr.Return,
        ),
        'loc_E2A',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

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
    OP_A2(0x1F18)

    Jump('loc_E90')

    def _loc_E2A(): pass

    label('loc_E2A')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0006, 60)
    OP_70(0x0006, 0x00000000)

    def _loc_E90(): pass

    label('loc_E90')

    Jump('loc_EC4')

    def _loc_E93(): pass

    label('loc_E93')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    def _loc_EC4(): pass

    label('loc_EC4')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0009 offset: 0xED2
@scena.Code('func_09_ED2')
def func_09_ED2():
    UnlockAchievement(0x02, 0x23, 0x00, 0x00)
    SetMapFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E3, 1, 0x1F19)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_FA7',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0007, 0x0000001E)
    OP_73(0x0007)
    OP_6F(0x0007, 30)
    AddSepith(0x03, 0x012C)
    AddSepith(0x04, 0x0064)
    AddSepith(0x05, 0x0064)
    AddSepith(0x06, 0x0064)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#59I风之耀晶片×３００\n',
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
    OP_A2(0x1F19)

    Jump('loc_FC1')

    def _loc_FA7(): pass

    label('loc_FA7')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_FC1(): pass

    label('loc_FC1')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x000A offset: 0xFD3
@scena.Code('func_0A_FD3')
def func_0A_FD3():
    UnlockAchievement(0x02, 0x24, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E3, 2, 0x1F1A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_10B0',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0008, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['圣灵药'], 1)"),
            Expr.Return,
        ),
        'loc_1047',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

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
    OP_A2(0x1F1A)

    Jump('loc_10AD')

    def _loc_1047(): pass

    label('loc_1047')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0008, 60)
    OP_70(0x0008, 0x00000000)

    def _loc_10AD(): pass

    label('loc_10AD')

    Jump('loc_10E1')

    def _loc_10B0(): pass

    label('loc_10B0')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    def _loc_10E1(): pass

    label('loc_10E1')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x000B offset: 0x10EF
@scena.Code('func_0B_10EF')
def func_0B_10EF():
    UnlockAchievement(0x02, 0x25, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E3, 3, 0x1F1B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_11CC',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0009, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['大回复药'], 1)"),
            Expr.Return,
        ),
        'loc_1163',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

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
    OP_A2(0x1F1B)

    Jump('loc_11C9')

    def _loc_1163(): pass

    label('loc_1163')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0009, 60)
    OP_70(0x0009, 0x00000000)

    def _loc_11C9(): pass

    label('loc_11C9')

    Jump('loc_11FD')

    def _loc_11CC(): pass

    label('loc_11CC')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    def _loc_11FD(): pass

    label('loc_11FD')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x000C offset: 0x120B
@scena.Code('func_0C_120B')
def func_0C_120B():
    UnlockAchievement(0x02, 0x26, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E3, 4, 0x1F1C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_12E8',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x000A, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['黑耀丸'], 1)"),
            Expr.Return,
        ),
        'loc_127F',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['黑耀丸']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1F1C)

    Jump('loc_12E5')

    def _loc_127F(): pass

    label('loc_127F')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['黑耀丸']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['黑耀丸']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x000A, 60)
    OP_70(0x000A, 0x00000000)

    def _loc_12E5(): pass

    label('loc_12E5')

    Jump('loc_1319')

    def _loc_12E8(): pass

    label('loc_12E8')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    def _loc_1319(): pass

    label('loc_1319')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x000D offset: 0x1327
@scena.Code('func_0D_1327')
def func_0D_1327():
    UnlockAchievement(0x02, 0x27, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E3, 5, 0x1F1D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1404',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x000B, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['绝缘胶带'], 1)"),
            Expr.Return,
        ),
        'loc_139B',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['绝缘胶带']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1F1D)

    Jump('loc_1401')

    def _loc_139B(): pass

    label('loc_139B')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['绝缘胶带']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['绝缘胶带']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x000B, 60)
    OP_70(0x000B, 0x00000000)

    def _loc_1401(): pass

    label('loc_1401')

    Jump('loc_1435')

    def _loc_1404(): pass

    label('loc_1404')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    def _loc_1435(): pass

    label('loc_1435')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x000E offset: 0x1443
@scena.Code('func_0E_1443')
def func_0E_1443():
    UnlockAchievement(0x02, 0x28, 0x00, 0x00)
    SetMapFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E3, 6, 0x1F1E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1518',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x000C, 0x0000001E)
    OP_73(0x000C)
    OP_6F(0x000C, 30)
    AddSepith(0x03, 0x012C)
    AddSepith(0x04, 0x0064)
    AddSepith(0x05, 0x0064)
    AddSepith(0x06, 0x0064)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#59I风之耀晶片×３００\n',
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
    OP_A2(0x1F1E)

    Jump('loc_1532')

    def _loc_1518(): pass

    label('loc_1518')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_1532(): pass

    label('loc_1532')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x000F offset: 0x1544
@scena.Code('func_0F_1544')
def func_0F_1544():
    UnlockAchievement(0x02, 0x29, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03E3, 7, 0x1F1F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1621',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x000D, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅱ'], 1)"),
            Expr.Return,
        ),
        'loc_15B8',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

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
    OP_A2(0x1F1F)

    Jump('loc_161E')

    def _loc_15B8(): pass

    label('loc_15B8')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x000D, 60)
    OP_70(0x000D, 0x00000000)

    def _loc_161E(): pass

    label('loc_161E')

    Jump('loc_1652')

    def _loc_1621(): pass

    label('loc_1621')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    def _loc_1652(): pass

    label('loc_1652')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0010 offset: 0x1660
@scena.Code('func_10_1660')
def func_10_1660():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6D(0, 250, -82450, 0)
    OP_6C(225000, 0)
    SetChrPos(0x0101, -500, 250, -82000, 0)
    SetChrPos(0x0102, 500, 250, -82000, 0)
    SetChrPos(0x00F8, -500, 250, -83000, 0)
    SetChrPos(0x00F9, 500, 250, -83000, 0)
    OP_9F(0x0000, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0001, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0002, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0003, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    FadeIn(1000, 0)
    OP_0D()
    Call(0, 0x0018)
    Call(0, 0x001A)
    Fade(500)
    OP_6D(-20, -50, -78290, 0)
    OP_6C(315000, 0)
    SetChrPos(0x0000, -20, -50, -78290, 0)
    SetChrPos(0x0001, -20, -50, -78290, 0)
    SetChrPos(0x0002, -20, -50, -78290, 0)
    SetChrPos(0x0003, -20, -50, -78290, 0)
    SetMapFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x0011 offset: 0x1772
@scena.Code('func_11_1772')
def func_11_1772():
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
    OP_6D(0, 250, -82450, 0)
    OP_6C(225000, 0)
    SetChrPos(0x0101, 500, 250, -83000, 180)
    SetChrPos(0x0102, -500, 250, -83000, 180)
    SetChrPos(0x00F8, 500, 250, -82000, 180)
    SetChrPos(0x00F9, -500, 250, -82000, 180)
    OP_0D()
    Call(0, 0x0018)
    Call(0, 0x001B)
    NewScene('ED6_DT21/C0703._SN', 103, 0, 0)
    IdleLoop()

    Return()

# id: 0x0012 offset: 0x17F3
@scena.Code('func_12_17F3')
def func_12_17F3():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6D(0, 3850, 105000, 0)
    SetChrPos(0x0101, 500, 3850, 104500, 180)
    SetChrPos(0x0102, -500, 3850, 104500, 180)
    SetChrPos(0x00F8, 500, 3850, 105500, 180)
    SetChrPos(0x00F9, -500, 3850, 105500, 180)
    OP_9F(0x0000, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0001, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0002, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0003, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    FadeIn(1000, 0)
    OP_0D()
    Call(0, 0x0019)
    Call(0, 0x001A)
    Fade(500)
    OP_6D(70, 3890, 102320, 0)
    SetChrPos(0x0000, 70, 3890, 102320, 180)
    SetChrPos(0x0001, 70, 3890, 102320, 180)
    SetChrPos(0x0002, 70, 3890, 102320, 180)
    SetChrPos(0x0003, 70, 3890, 102320, 180)
    SetMapFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x0013 offset: 0x18F3
@scena.Code('func_13_18F3')
def func_13_18F3():
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
    OP_6D(0, 3850, 105000, 0)
    SetChrPos(0x0101, -500, 3850, 105500, 0)
    SetChrPos(0x0102, 500, 3850, 105500, 0)
    SetChrPos(0x00F8, -500, 3850, 104500, 0)
    SetChrPos(0x00F9, 500, 3850, 104500, 0)
    OP_0D()
    Call(0, 0x0018)
    Call(0, 0x001B)
    NewScene('ED6_DT21/C0705._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0014 offset: 0x196B
@scena.Code('func_14_196B')
def func_14_196B():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6D(16000, -3750, -15500, 0)
    SetChrPos(0x0101, 16500, -3750, -15000, 90)
    SetChrPos(0x0102, 16500, -3750, -16000, 90)
    SetChrPos(0x00F8, 15500, -3750, -15000, 90)
    SetChrPos(0x00F9, 15500, -3750, -16000, 90)
    OP_9F(0x0000, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0001, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0002, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0003, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    FadeIn(1000, 0)
    OP_0D()
    Call(0, 0x0018)
    Call(0, 0x001A)
    Fade(500)
    OP_6D(18870, -3700, -15430, 0)
    SetChrPos(0x0000, 18870, -3700, -15430, 90)
    SetChrPos(0x0001, 18870, -3700, -15430, 90)
    SetChrPos(0x0002, 18870, -3700, -15430, 90)
    SetChrPos(0x0003, 18870, -3700, -15430, 90)
    SetMapFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x0015 offset: 0x1A6B
@scena.Code('func_15_1A6B')
def func_15_1A6B():
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
    OP_6D(16000, -3750, -15500, 0)
    SetChrPos(0x0101, 15500, -3750, -16000, 270)
    SetChrPos(0x0102, 15500, -3750, -15000, 270)
    SetChrPos(0x00F8, 16500, -3750, -16000, 270)
    SetChrPos(0x00F9, 16500, -3750, -15000, 270)
    OP_0D()
    Call(0, 0x0018)
    Call(0, 0x001B)
    NewScene('ED6_DT21/C0703._SN', 104, 0, 0)
    IdleLoop()

    Return()

# id: 0x0016 offset: 0x1AE3
@scena.Code('func_16_1AE3')
def func_16_1AE3():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6D(-17300, -3750, 14900, 0)
    OP_6C(45000, 0)
    SetChrPos(0x0101, -17800, -3750, 14400, 270)
    SetChrPos(0x0102, -17800, -3750, 15400, 270)
    SetChrPos(0x00F8, -16800, -3750, 14400, 270)
    SetChrPos(0x00F9, -16800, -3750, 15400, 270)
    OP_9F(0x0000, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0001, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0002, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0003, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    FadeIn(1000, 0)
    OP_0D()
    Call(0, 0x0018)
    Call(0, 0x001A)
    Fade(500)
    OP_6D(-21080, -3890, 14900, 0)
    OP_6C(315000, 0)
    SetChrPos(0x0000, -21080, -3890, 14900, 270)
    SetChrPos(0x0001, -21080, -3890, 14900, 270)
    SetChrPos(0x0002, -21080, -3890, 14900, 270)
    SetChrPos(0x0003, -21080, -3890, 14900, 270)
    SetMapFlags(0x00000001)
    EventEnd(0x02)

    Return()

# id: 0x0017 offset: 0x1BF5
@scena.Code('func_17_1BF5')
def func_17_1BF5():
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
    OP_6D(-17300, -3750, 14900, 0)
    OP_6C(45000, 0)
    SetChrPos(0x0101, -16800, -3750, 15400, 90)
    SetChrPos(0x0102, -16800, -3750, 14400, 90)
    SetChrPos(0x00F8, -17800, -3750, 15400, 90)
    SetChrPos(0x00F9, -17800, -3750, 14400, 90)
    OP_0D()
    Call(0, 0x0018)
    Call(0, 0x001B)
    NewScene('ED6_DT21/C0703._SN', 105, 0, 0)
    IdleLoop()

    Return()

# id: 0x0018 offset: 0x1C76
@scena.Code('func_18_1C76')
def func_18_1C76():
    PlayEffect(0x00, 0xFF, 0x0000, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0001, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0002, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0003, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x0099, 0x00, 0x64)
    OP_22(0x00B8, 0x00, 0x64)

    Return()

# id: 0x0019 offset: 0x1D55
@scena.Code('func_19_1D55')
def func_19_1D55():
    PlayEffect(0x01, 0xFF, 0x0000, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0001, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0002, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0003, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x0099, 0x00, 0x64)
    OP_22(0x00B8, 0x00, 0x64)

    Return()

# id: 0x001A offset: 0x1E34
@scena.Code('func_1A_1E34')
def func_1A_1E34():
    @scena.Lambda('lambda_1E3A')
    def lambda_1E3A():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_1E3A)

    @scena.Lambda('lambda_1E4C')
    def lambda_1E4C():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_1E4C)

    @scena.Lambda('lambda_1E5E')
    def lambda_1E5E():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_1E5E)

    @scena.Lambda('lambda_1E70')
    def lambda_1E70():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_1E70)

    Sleep(2500)

    Return()

# id: 0x001B offset: 0x1E82
@scena.Code('func_1B_1E82')
def func_1B_1E82():
    @scena.Lambda('lambda_1E88')
    def lambda_1E88():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_1E88)

    @scena.Lambda('lambda_1E9A')
    def lambda_1E9A():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_1E9A)

    @scena.Lambda('lambda_1EAC')
    def lambda_1EAC():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_1EAC)

    @scena.Lambda('lambda_1EBE')
    def lambda_1EBE():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_1EBE)

    Sleep(2000)

    Return()

# id: 0x001C offset: 0x1ED0
@scena.Code('func_1C_1ED0')
def func_1C_1ED0():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1F23',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

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

    Jump('loc_20C5')

    def _loc_1F23(): pass

    label('loc_1F23')

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
        'loc_20AA',
    )

    FadeIn(100, 0)
    Sleep(500)

    OP_26(13)
    OP_72(0x0010, 0x0020)
    OP_6F(0x0010, 300)
    OP_70(0x0010, 0x000001F4)
    OP_73(0x0010)
    OP_6F(0x0010, 500)
    OP_70(0x0010, 0x000002BC)
    OP_71(0x0010, 0x0020)
    OP_20(0x00000BB8)
    OP_22(0x000C, 0x00, 0x64)
    OP_82(0x02, 0x02)
    LoadEffect(0x03, 'map\\\\mp027_01.eff')
    PlayEffect(0x03, 0x03, 0x00FF, -3930, 5200, 98030, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    FadeOut(1500, 0, -1)
    Sleep(1500)

    OP_22(0x000D, 0x00, 0x64)
    OP_0D()
    SetChrStatus(0x00FF, 0xFE, 0)
    OP_69(0x0000, 0x00000000)
    OP_30(0x01)
    Sleep(3500)

    OP_82(0x03, 0x02)
    PlayEffect(0x02, 0x02, 0x00FF, -3930, 5200, 98030, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0010, 0)
    OP_70(0x0010, 0x000000FA)
    OP_1E()
    FadeIn(1000, 0)
    OP_56(0x00)
    TalkEnd(0x00FF)

    Return()

    def _loc_20AA(): pass

    label('loc_20AA')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_20C4',
    )

    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

    def _loc_20C4(): pass

    label('loc_20C4')

    Return()

    def _loc_20C5(): pass

    label('loc_20C5')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

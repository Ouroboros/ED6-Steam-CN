import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5610_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5610   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5610.x'
    header.mapIndex       = 1
    header.bgm            = 61
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
        ('ED6_DT29/CH12570._CH', 'ED6_DT29/CH12570P._CP'),
        ('ED6_DT29/CH12571._CH', 'ED6_DT29/CH12571P._CP'),
        ('ED6_DT29/CH12320._CH', 'ED6_DT29/CH12320P._CP'),
        ('ED6_DT29/CH12321._CH', 'ED6_DT29/CH12321P._CP'),
        ('ED6_DT29/CH12330._CH', 'ED6_DT29/CH12330P._CP'),
        ('ED6_DT29/CH12331._CH', 'ED6_DT29/CH12331P._CP'),
        ('ED6_DT29/CH12350._CH', 'ED6_DT29/CH12350P._CP'),
        ('ED6_DT29/CH12351._CH', 'ED6_DT29/CH12351P._CP'),
        ('ED6_DT29/CH12000._CH', 'ED6_DT29/CH12000P._CP'),
        ('ED6_DT29/CH12201._CH', 'ED6_DT29/CH12201P._CP'),
        ('ED6_DT07/CH01260._CH', 'ED6_DT07/CH01260P._CP'),
        ('ED6_DT07/CH00390._CH', 'ED6_DT07/CH00390P._CP'),
        ('ED6_DT26/CH20404._CH', 'ED6_DT26/CH20404P._CP'),
        ('ED6_DT26/CH20409._CH', 'ED6_DT26/CH20409P._CP'),
        ('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP'),
        ('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP'),
        ('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP'),
        ('ED6_DT07/CH00140._CH', 'ED6_DT07/CH00140P._CP'),
        ('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP'),
        ('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP'),
        ('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP'),
        ('ED6_DT29/CH12574._CH', 'ED6_DT29/CH12574P._CP'),
        ('ED6_DT27/CH03084._CH', 'ED6_DT27/CH03084P._CP'),
        ('ED6_DT27/CH03005._CH', 'ED6_DT27/CH03005P._CP'),
        ('ED6_DT29/CH12354._CH', 'ED6_DT29/CH12354P._CP'),
        ('ED6_DT26/CH20373._CH', 'ED6_DT26/CH20373P._CP'),
        ('ED6_DT07/CH00391._CH', 'ED6_DT07/CH00391P._CP'),
    ]

# id: 0x10001 offset: 0x18A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '',
            x                   = 80960,
            z                   = 1500,
            y                   = -9000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '库拉茨',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '哨兵235',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '哨兵570',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '哨兵235',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '零部件',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '零部件',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 131085,
            chipIndex           = 13,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '零部件',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 65549,
            chipIndex           = 13,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '零部件',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 196621,
            chipIndex           = 13,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '零部件',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 65549,
            chipIndex           = 13,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0007,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '零部件',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 131085,
            chipIndex           = 13,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0008,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '零部件',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 196621,
            chipIndex           = 13,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0009,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '零部件',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000A,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '零部件',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 65549,
            chipIndex           = 13,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x000B,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x34A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = -158630,
            z           = 0,
            y           = -17300,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x041D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 86870,
            z           = 0,
            y           = -9080,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x041D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 88230,
            z           = 0,
            y           = 105630,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x041D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 88000,
            z           = 0,
            y           = 95860,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x041D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 37720,
            z           = 0,
            y           = 125100,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x041D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -10490,
            z           = 0,
            y           = 109180,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x041D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x3F2
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 23010,
            y           = -1000,
            z           = 131280,
            range       = 3000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000026,
        ),
    )

# id: 0x10004 offset: 0x412
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -107320,
            triggerZ            = 0,
            triggerY            = 67990,
            triggerRange        = 1000,
            actorX              = -107980,
            actorZ              = 0,
            actorY              = 67990,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000C,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -4290,
            triggerZ            = 0,
            triggerY            = 32990,
            triggerRange        = 1000,
            actorX              = -5000,
            actorZ              = 0,
            actorY              = 32990,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000D,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -152290,
            triggerZ            = 0,
            triggerY            = -16970,
            triggerRange        = 1000,
            actorX              = -153000,
            actorZ              = 0,
            actorY              = -17010,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000E,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 80300,
            triggerZ            = 0,
            triggerY            = -9000,
            triggerRange        = 1000,
            actorX              = 80960,
            actorZ              = 0,
            actorY              = -9000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000F,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 70290,
            triggerZ            = 0,
            triggerY            = 44530,
            triggerRange        = 1000,
            actorX              = 70950,
            actorZ              = 0,
            actorY              = 44530,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0010,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 82290,
            triggerZ            = 0,
            triggerY            = 101030,
            triggerRange        = 1000,
            actorX              = 82990,
            actorZ              = 0,
            actorY              = 101030,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0011,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -12880,
            triggerZ            = 0,
            triggerY            = -18740,
            triggerRange        = 800,
            actorX              = -12880,
            actorZ              = 1000,
            actorY              = -18740,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0017,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -76940,
            triggerZ            = 0,
            triggerY            = 169050,
            triggerRange        = 800,
            actorX              = -76940,
            actorZ              = 1000,
            actorY              = 169050,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0022,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 28830,
            triggerZ            = 0,
            triggerY            = 25920,
            triggerRange        = 800,
            actorX              = 28830,
            actorZ              = 1200,
            actorY              = 25920,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0019,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 24650,
            triggerZ            = 0,
            triggerY            = 131700,
            triggerRange        = 800,
            actorX              = 24650,
            actorZ              = 1200,
            actorY              = 131700,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 28770,
            triggerZ            = 0,
            triggerY            = 11950,
            triggerRange        = 800,
            actorX              = 28770,
            actorZ              = 1200,
            actorY              = 11950,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -66710,
            triggerZ            = 0,
            triggerY            = 67500,
            triggerRange        = 800,
            actorX              = -66710,
            actorZ              = 1200,
            actorY              = 67500,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001C,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -9010,
            triggerZ            = 0,
            triggerY            = 138700,
            triggerRange        = 1200,
            actorX              = -9010,
            actorZ              = 1000,
            actorY              = 138700,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0027,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x5E6
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_5F7',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    Event(0, func_18_2318)

    Jump('loc_63C')

    def _loc_5F7(): pass

    label('loc_5F7')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x87),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_612',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 6, 0x1C06)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_60F',
    )

    Event(0, func_12_1135)

    def _loc_60F(): pass

    label('loc_60F')

    Jump('loc_63C')

    def _loc_612(): pass

    label('loc_612')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x78),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_62D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0381, 0, 0x1C08)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_62A',
    )

    Event(0, func_1E_2826)

    def _loc_62A(): pass

    label('loc_62A')

    Jump('loc_63C')

    def _loc_62D(): pass

    label('loc_62D')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x85),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_63C',
    )

    SetScenaFlags(ScenaFlag(0x0383, 2, 0x1C1A))

    def _loc_63C(): pass

    label('loc_63C')

    Return()

# id: 0x0001 offset: 0x63D
@scena.Code('func_01_63D')
def func_01_63D():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000080, 'loc_651'),
        (0x00000081, 'loc_651'),
        (0x00000087, 'loc_651'),
        (-1, 'loc_659'),
    )

    def _loc_651(): pass

    label('loc_651')

    PlaySE(160, 0x01, 0x64)

    Jump('loc_65F')

    def _loc_659(): pass

    label('loc_659')

    OP_23(0x00A0)

    Jump('loc_65F')

    def _loc_65F(): pass

    label('loc_65F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A0, 0, 0x1D00)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_671',
    )

    OP_6F(0x0000, 0)

    Jump('loc_678')

    def _loc_671(): pass

    label('loc_671')

    OP_6F(0x0000, 60)

    def _loc_678(): pass

    label('loc_678')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A0, 2, 0x1D02)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_68A',
    )

    OP_6F(0x0001, 0)

    Jump('loc_691')

    def _loc_68A(): pass

    label('loc_68A')

    OP_6F(0x0001, 60)

    def _loc_691(): pass

    label('loc_691')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A0, 4, 0x1D04)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6A3',
    )

    OP_6F(0x0002, 0)

    Jump('loc_6AA')

    def _loc_6A3(): pass

    label('loc_6A3')

    OP_6F(0x0002, 60)

    def _loc_6AA(): pass

    label('loc_6AA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A0, 5, 0x1D05)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6BC',
    )

    OP_6F(0x0003, 0)

    Jump('loc_6C3')

    def _loc_6BC(): pass

    label('loc_6BC')

    OP_6F(0x0003, 60)

    def _loc_6C3(): pass

    label('loc_6C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A0, 7, 0x1D07)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6D5',
    )

    OP_6F(0x0004, 0)

    Jump('loc_6DC')

    def _loc_6D5(): pass

    label('loc_6D5')

    OP_6F(0x0004, 60)

    def _loc_6DC(): pass

    label('loc_6DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A1, 0, 0x1D08)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6EE',
    )

    OP_6F(0x0005, 0)

    Jump('loc_6F5')

    def _loc_6EE(): pass

    label('loc_6EE')

    OP_6F(0x0005, 60)

    def _loc_6F5(): pass

    label('loc_6F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 7, 0x1C07)),
            Expr.Return,
        ),
        'loc_709',
    )

    OP_10(0x00, 0x01)
    OP_6F(0x001E, 60)

    Jump('loc_715')

    def _loc_709(): pass

    label('loc_709')

    OP_1B(0x00, 0x00, 0x0025)
    OP_6F(0x001E, 1)

    def _loc_715(): pass

    label('loc_715')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0382, 0, 0x1C10)),
            Expr.Return,
        ),
        'loc_72B',
    )

    OP_64(0x08, 0x0001)
    OP_71(0x000C, 0x0010)
    OP_10(0x1F, 0x01)

    Jump('loc_733')

    def _loc_72B(): pass

    label('loc_72B')

    OP_10(0x1F, 0x00)
    OP_72(0x000C, 0x0010)

    def _loc_733(): pass

    label('loc_733')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0382, 1, 0x1C11)),
            Expr.Return,
        ),
        'loc_749',
    )

    OP_64(0x09, 0x0001)
    OP_71(0x0017, 0x0010)
    OP_10(0x20, 0x01)

    Jump('loc_751')

    def _loc_749(): pass

    label('loc_749')

    OP_10(0x20, 0x00)
    OP_72(0x0017, 0x0010)

    def _loc_751(): pass

    label('loc_751')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0382, 2, 0x1C12)),
            Expr.Return,
        ),
        'loc_767',
    )

    OP_64(0x0A, 0x0001)
    OP_71(0x000B, 0x0010)
    OP_10(0x05, 0x01)

    Jump('loc_76F')

    def _loc_767(): pass

    label('loc_767')

    OP_10(0x05, 0x00)
    OP_72(0x000B, 0x0010)

    def _loc_76F(): pass

    label('loc_76F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0394, 0, 0x1CA0)),
            Expr.Return,
        ),
        'loc_785',
    )

    OP_64(0x0B, 0x0001)
    OP_71(0x0013, 0x0010)
    OP_10(0x1D, 0x01)

    Jump('loc_78D')

    def _loc_785(): pass

    label('loc_785')

    OP_10(0x1D, 0x00)
    OP_72(0x0013, 0x0010)

    def _loc_78D(): pass

    label('loc_78D')

    OP_74(0x001D, 0x00000000, 0x0000)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7EB',
    )

    LoadEffect(0x01, 'map\\\\mp027_00.eff')
    PlayEffect(0x01, 0x01, 0x00FF, -9010, 1000, 138700, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)

    def _loc_7EB(): pass

    label('loc_7EB')

    Return()

# id: 0x0002 offset: 0x7EC
@scena.Code('func_02_7EC')
def func_02_7EC():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_801',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_7EC')

    def _loc_801(): pass

    label('loc_801')

    Return()

# id: 0x0003 offset: 0x802
@scena.Code('func_03_802')
def func_03_802():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_83D',
    )

    ChrSetPos(0x00FE, -62120, 1500, 73320, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrMoveTo(0x00FE, -62120, 1500, 55700, 3000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Jump('func_03_802')

    def _loc_83D(): pass

    label('loc_83D')

    Return()

# id: 0x0004 offset: 0x83E
@scena.Code('func_04_83E')
def func_04_83E():
    Sleep(2000)

    def _loc_843(): pass

    label('loc_843')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_87E',
    )

    ChrSetPos(0x00FE, -62120, 1500, 73320, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrMoveTo(0x00FE, -62120, 1500, 55700, 3000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Jump('loc_843')

    def _loc_87E(): pass

    label('loc_87E')

    Return()

# id: 0x0005 offset: 0x87F
@scena.Code('func_05_87F')
def func_05_87F():
    Sleep(3800)

    def _loc_884(): pass

    label('loc_884')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_8BF',
    )

    ChrSetPos(0x00FE, -62120, 1500, 73320, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrMoveTo(0x00FE, -62120, 1500, 55700, 3000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Jump('loc_884')

    def _loc_8BF(): pass

    label('loc_8BF')

    Return()

# id: 0x0006 offset: 0x8C0
@scena.Code('func_06_8C0')
def func_06_8C0():
    Sleep(2000)

    def _loc_8C5(): pass

    label('loc_8C5')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_900',
    )

    ChrSetPos(0x00FE, -56020, 1500, 73390, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrMoveTo(0x00FE, -56020, 1500, 55750, 3000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Jump('loc_8C5')

    def _loc_900(): pass

    label('loc_900')

    Return()

# id: 0x0007 offset: 0x901
@scena.Code('func_07_901')
def func_07_901():
    Sleep(4000)

    def _loc_906(): pass

    label('loc_906')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_941',
    )

    ChrSetPos(0x00FE, -56020, 1200, 73390, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrMoveTo(0x00FE, -56020, 1500, 55750, 3000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Jump('loc_906')

    def _loc_941(): pass

    label('loc_941')

    Return()

# id: 0x0008 offset: 0x942
@scena.Code('func_08_942')
def func_08_942():
    Sleep(5800)

    def _loc_947(): pass

    label('loc_947')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_982',
    )

    ChrSetPos(0x00FE, -56020, 1200, 73390, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrMoveTo(0x00FE, -56020, 1500, 55750, 3000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Jump('loc_947')

    def _loc_982(): pass

    label('loc_982')

    Return()

# id: 0x0009 offset: 0x983
@scena.Code('func_09_983')
def func_09_983():
    Sleep(1000)

    def _loc_988(): pass

    label('loc_988')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_9C3',
    )

    ChrSetPos(0x00FE, -49970, 1500, 72960, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrMoveTo(0x00FE, -49970, 1500, 55740, 3000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Jump('loc_988')

    def _loc_9C3(): pass

    label('loc_9C3')

    Return()

# id: 0x000A offset: 0x9C4
@scena.Code('func_0A_9C4')
def func_0A_9C4():
    Sleep(3000)

    def _loc_9C9(): pass

    label('loc_9C9')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_A04',
    )

    ChrSetPos(0x00FE, -49970, 1500, 72960, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrMoveTo(0x00FE, -49970, 1500, 55740, 3000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Jump('loc_9C9')

    def _loc_A04(): pass

    label('loc_A04')

    Return()

# id: 0x000B offset: 0xA05
@scena.Code('func_0B_A05')
def func_0B_A05():
    Sleep(4800)

    def _loc_A0A(): pass

    label('loc_A0A')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_A45',
    )

    ChrSetPos(0x00FE, -49970, 1500, 72960, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrMoveTo(0x00FE, -49970, 1500, 55740, 3000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Jump('loc_A0A')

    def _loc_A45(): pass

    label('loc_A45')

    Return()

# id: 0x000C offset: 0xA46
@scena.Code('func_0C_A46')
def func_0C_A46():
    UnlockAchievement(0x02, 0x019F, 0x00)
    MapSetFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A0, 0, 0x1D00)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AC4',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 30)
    OP_73(0x0000)
    OP_6F(0x0000, 30)
    AddSepith(0x00, 200)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#56I地之耀晶片×２００\n',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    SetScenaFlags(ScenaFlag(0x03A0, 0, 0x1D00))

    Jump('loc_ADE')

    def _loc_AC4(): pass

    label('loc_AC4')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_ADE(): pass

    label('loc_ADE')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x000D offset: 0xAF0
@scena.Code('func_0D_AF0')
def func_0D_AF0():
    UnlockAchievement(0x02, 0x01A0, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A0, 2, 0x1D02)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BCD',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['金耀晚礼服'], 1)"),
            Expr.Return,
        ),
        'loc_B64',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['金耀晚礼服']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03A0, 2, 0x1D02))

    Jump('loc_BCA')

    def _loc_B64(): pass

    label('loc_B64')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['金耀晚礼服']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['金耀晚礼服']),
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

    def _loc_BCA(): pass

    label('loc_BCA')

    Jump('loc_BFE')

    def _loc_BCD(): pass

    label('loc_BCD')

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
    def _loc_BFE(): pass

    label('loc_BFE')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x000E offset: 0xC0C
@scena.Code('func_0E_C0C')
def func_0E_C0C():
    UnlockAchievement(0x02, 0x01A1, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A0, 4, 0x1D04)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CE9',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['预警之铃'], 1)"),
            Expr.Return,
        ),
        'loc_C80',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['预警之铃']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03A0, 4, 0x1D04))

    Jump('loc_CE6')

    def _loc_C80(): pass

    label('loc_C80')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['预警之铃']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['预警之铃']),
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

    def _loc_CE6(): pass

    label('loc_CE6')

    Jump('loc_D1A')

    def _loc_CE9(): pass

    label('loc_CE9')

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
    def _loc_D1A(): pass

    label('loc_D1A')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x000F offset: 0xD28
@scena.Code('func_0F_D28')
def func_0F_D28():
    UnlockAchievement(0x02, 0x0207, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A0, 5, 0x1D05)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_EC0',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0003, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A0, 6, 0x1D06)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E0C',
    )

    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    ChrTurnDirection(0x0008, 0x0000, 0)
    ChrMoveToRelativeAsync(0x0008, 0, 1000, 0, 0, 0x00)

    @scena.Lambda('lambda_0D7F')
    def lambda_0D7F():
        ChrMoveToRelativeAsync(0x00FE, 0, -1000, 0, 600, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0D7F)

    @scena.Lambda('lambda_0D9A')
    def lambda_0D9A():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 600)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0D9A)

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
    Battle(0x00000423, 0x00000000, 0x00, 0x0000, 0xFF)
    ChrSetFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_DE7'),
        (0x00000002, 'loc_DF9'),
        (0x00000001, 'loc_E09'),
        (-1, 'loc_E0C'),
    )

    def _loc_DE7(): pass

    label('loc_DE7')

    SetScenaFlags(ScenaFlag(0x03A0, 6, 0x1D06))
    OP_6F(0x0003, 60)
    Sleep(500)

    Jump('loc_E0C')

    def _loc_DF9(): pass

    label('loc_DF9')

    OP_6F(0x0003, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

    def _loc_E09(): pass

    label('loc_E09')

    OP_B4(0x00)

    Return()

    def _loc_E0C(): pass

    label('loc_E0C')

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['绞盘弓'], 1)"),
            Expr.Return,
        ),
        'loc_E5B',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['绞盘弓']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03A0, 5, 0x1D05))

    Jump('loc_EBD')

    def _loc_E5B(): pass

    label('loc_E5B')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['绞盘弓']),
            (TxtCtl.SetColor, 0x0),
            '。 \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['绞盘弓']),
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

    def _loc_EBD(): pass

    label('loc_EBD')

    Jump('loc_EEF')

    def _loc_EC0(): pass

    label('loc_EC0')

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
    def _loc_EEF(): pass

    label('loc_EEF')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0010 offset: 0xEFD
@scena.Code('func_10_EFD')
def func_10_EFD():
    UnlockAchievement(0x02, 0x01A2, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A0, 7, 0x1D07)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_FDA',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0004, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅱ'], 1)"),
            Expr.Return,
        ),
        'loc_F71',
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
    SetScenaFlags(ScenaFlag(0x03A0, 7, 0x1D07))

    Jump('loc_FD7')

    def _loc_F71(): pass

    label('loc_F71')

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
    OP_6F(0x0004, 60)
    OP_70(0x0004, 0)

    def _loc_FD7(): pass

    label('loc_FD7')

    Jump('loc_100B')

    def _loc_FDA(): pass

    label('loc_FDA')

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
    def _loc_100B(): pass

    label('loc_100B')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0011 offset: 0x1019
@scena.Code('func_11_1019')
def func_11_1019():
    UnlockAchievement(0x02, 0x01A3, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A1, 0, 0x1D08)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_10F6',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0005, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['防御４'], 1)"),
            Expr.Return,
        ),
        'loc_108D',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['防御４']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03A1, 0, 0x1D08))

    Jump('loc_10F3')

    def _loc_108D(): pass

    label('loc_108D')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['防御４']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['防御４']),
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

    def _loc_10F3(): pass

    label('loc_10F3')

    Jump('loc_1127')

    def _loc_10F6(): pass

    label('loc_10F6')

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
    def _loc_1127(): pass

    label('loc_1127')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0012 offset: 0x1135
@scena.Code('func_12_1135')
def func_12_1135():
    EventBegin(0x00)
    FadeOut(0, 0, -1)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1156',
    )

    Call(0, 0x0023)
    Call(0, 0x0024)

    def _loc_1156(): pass

    label('loc_1156')

    ChrSetPos(0x0101, -63620, 20, 50130, 45)
    ChrSetPos(0x0109, -63800, 20, 48690, 45)
    ChrSetPos(0x00F8, -64780, 20, 50340, 45)
    ChrSetPos(0x00F9, -65010, 0, 48600, 45)
    CameraMove(-52780, 0, 64129, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(290000, 0)
    OP_6E(341, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(2000)

    @scena.Lambda('lambda_11EC')
    def lambda_11EC():
        CameraMove(-64090, 20, 50870, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_11EC)

    @scena.Lambda('lambda_1204')
    def lambda_1204():
        OP_67(0, 5650, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1204)

    @scena.Lambda('lambda_121C')
    def lambda_121C():
        CameraSetDistance(3060, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_121C)

    @scena.Lambda('lambda_122C')
    def lambda_122C():
        OP_6C(349000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_122C)

    OP_6E(257, 6000)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010321059V#1020F#6P这、这里是什么地方……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_12B9',
    )

    ChrTalk(
        0x0107,
        (
            '#0070321060V#065F#6P像是某种\n',
            '零部件的工厂……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12F3')

    def _loc_12B9(): pass

    label('loc_12B9')

    ChrTalk(
        0x0109,
        (
            '#0180321061V#1064F#6P居然来到了这么\n',
            '古怪的地方啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12F3(): pass

    label('loc_12F3')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1337',
    )

    ChrTalk(
        0x0106,
        (
            '#0050321062V#552F#6P哼……\n',
            '似乎没有人的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1454')

    def _loc_1337(): pass

    label('loc_1337')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_137B',
    )

    ChrTalk(
        0x0108,
        (
            '#0080321063V#072F#6P唔……\n',
            '似乎没有人的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1454')

    def _loc_137B(): pass

    label('loc_137B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_13BF',
    )

    ChrTalk(
        0x0103,
        (
            '#0030321064V#022F#6P唔……\n',
            '似乎没有人的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1454')

    def _loc_13BF(): pass

    label('loc_13BF')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1405',
    )

    ChrTalk(
        0x0104,
        (
            '#0040321065V#032F#6P唔……\n',
            '似乎没有人的样子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1454')

    def _loc_1405(): pass

    label('loc_1405')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1454',
    )

    ChrTalk(
        0x0105,
        (
            '#0060321066V#042F#6P………………………\n',
            '似乎没有人的样子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1454(): pass

    label('loc_1454')

    PlaySE(303, 0x00, 0x64)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0109, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_14B3',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_14F1')

    def _loc_14B3(): pass

    label('loc_14B3')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_14DA',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_14F1')

    def _loc_14DA(): pass

    label('loc_14DA')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_14F1(): pass

    label('loc_14F1')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1518',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_1556')

    def _loc_1518(): pass

    label('loc_1518')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_153F',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_1556')

    def _loc_153F(): pass

    label('loc_153F')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_1556(): pass

    label('loc_1556')

    Sleep(1000)

    @scena.Lambda('lambda_1561')
    def lambda_1561():
        CameraMove(-58600, 20, 46370, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1561)

    @scena.Lambda('lambda_1579')
    def lambda_1579():
        CameraSetDistance(2500, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1579)

    @scena.Lambda('lambda_1589')
    def lambda_1589():
        OP_6C(315000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1589)

    ChrSetDirection(0x0101, 90, 400)
    ChrSetDirection(0x0109, 90, 400)
    ChrSetDirection(0x00F8, 90, 400)
    ChrSetDirection(0x00F9, 90, 400)
    WaitForThreadExit(0x0101, 0x0000)
    CreateThread(0x000A, 0x01, 0x00, func_14_2059)
    CreateThread(0x000B, 0x01, 0x00, func_15_20CB)
    CreateThread(0x000C, 0x01, 0x00, func_16_2142)
    CreateThread(0x000A, 0x03, 0x00, func_02_7EC)
    CreateThread(0x000B, 0x03, 0x00, func_02_7EC)
    CreateThread(0x000C, 0x03, 0x00, func_02_7EC)
    Sleep(1000)

    @scena.Lambda('lambda_15E9')
    def lambda_15E9():
        CameraMove(-62310, 0, 49610, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_15E9)

    @scena.Lambda('lambda_1601')
    def lambda_1601():
        OP_67(0, 5650, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1601)

    @scena.Lambda('lambda_1619')
    def lambda_1619():
        CameraSetDistance(3000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1619)

    @scena.Lambda('lambda_1629')
    def lambda_1629():
        OP_6E(318, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1629)

    WaitForThreadExit(0x0101, 0x0003)
    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x0109, 0)
    ChrSetSubChip(0x00F8, 0)
    ChrSetSubChip(0x00F9, 0)
    ChrSetChipByIndex(0x0101, 14)
    Sleep(100)

    ChrSetChipByIndex(0x0109, 21)
    Sleep(100)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_168B'),
        (0x00000005, 'loc_1693'),
        (0x00000003, 'loc_169B'),
        (0x00000004, 'loc_16A3'),
        (0x00000006, 'loc_16AB'),
        (0x00000007, 'loc_16B3'),
        (-1, 'loc_16BB'),
    )

    def _loc_168B(): pass

    label('loc_168B')

    ChrSetChipByIndex(0x00F8, 15)

    Jump('loc_16BB')

    def _loc_1693(): pass

    label('loc_1693')

    ChrSetChipByIndex(0x00F8, 16)

    Jump('loc_16BB')

    def _loc_169B(): pass

    label('loc_169B')

    ChrSetChipByIndex(0x00F8, 17)

    Jump('loc_16BB')

    def _loc_16A3(): pass

    label('loc_16A3')

    ChrSetChipByIndex(0x00F8, 18)

    Jump('loc_16BB')

    def _loc_16AB(): pass

    label('loc_16AB')

    ChrSetChipByIndex(0x00F8, 19)

    Jump('loc_16BB')

    def _loc_16B3(): pass

    label('loc_16B3')

    ChrSetChipByIndex(0x00F8, 20)

    Jump('loc_16BB')

    def _loc_16BB(): pass

    label('loc_16BB')

    Sleep(100)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_16E1'),
        (0x00000005, 'loc_16E9'),
        (0x00000003, 'loc_16F1'),
        (0x00000004, 'loc_16F9'),
        (0x00000006, 'loc_1701'),
        (0x00000007, 'loc_1709'),
        (-1, 'loc_1711'),
    )

    def _loc_16E1(): pass

    label('loc_16E1')

    ChrSetChipByIndex(0x00F9, 15)

    Jump('loc_1711')

    def _loc_16E9(): pass

    label('loc_16E9')

    ChrSetChipByIndex(0x00F9, 16)

    Jump('loc_1711')

    def _loc_16F1(): pass

    label('loc_16F1')

    ChrSetChipByIndex(0x00F9, 17)

    Jump('loc_1711')

    def _loc_16F9(): pass

    label('loc_16F9')

    ChrSetChipByIndex(0x00F9, 18)

    Jump('loc_1711')

    def _loc_1701(): pass

    label('loc_1701')

    ChrSetChipByIndex(0x00F9, 19)

    Jump('loc_1711')

    def _loc_1709(): pass

    label('loc_1709')

    ChrSetChipByIndex(0x00F9, 20)

    Jump('loc_1711')

    def _loc_1711(): pass

    label('loc_1711')

    OP_0D()
    Sleep(200)

    ChrTalk(
        0x0101,
        (
            '#0010321067V#1005F#5P这、这些是！？',
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
        'loc_1779',
    )

    ChrTalk(
        0x0106,
        (
            '#0050321068V#054F#5P人形兵器吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1866')

    def _loc_1779(): pass

    label('loc_1779')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_17B0',
    )

    ChrTalk(
        0x0103,
        (
            '#0030321069V#024F#5P人形兵器！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1866')

    def _loc_17B0(): pass

    label('loc_17B0')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_17F1',
    )

    ChrTalk(
        0x0105,
        (
            '#0060321070V#042F#5P难道是……人形兵器！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1866')

    def _loc_17F1(): pass

    label('loc_17F1')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_182E',
    )

    ChrTalk(
        0x0104,
        (
            '#0040321071V#030F#5P哦……人形兵器吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1866')

    def _loc_182E(): pass

    label('loc_182E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1866',
    )

    ChrTalk(
        0x0108,
        (
            '#0080321072V#076F#5P人形兵器吗……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1866(): pass

    label('loc_1866')

    WaitForThreadExit(0x0101, 0x0000)

    @scena.Lambda('lambda_1871')
    def lambda_1871():
        CameraMove(-63790, 20, 49470, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1871)

    @scena.Lambda('lambda_1889')
    def lambda_1889():
        CameraSetDistance(1980, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1889)

    ChrSetChipByIndex(0x000B, 1)

    @scena.Lambda('lambda_189E')
    def lambda_189E():
        ChrWalkTo(0x00FE, -62710, 0, 49280, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0000, lambda_189E)

    Sleep(50)

    ChrSetChipByIndex(0x000A, 7)

    @scena.Lambda('lambda_18C3')
    def lambda_18C3():
        ChrWalkTo(0x00FE, -62150, 0, 50580, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_18C3)

    Sleep(50)

    ChrSetChipByIndex(0x000C, 7)

    @scena.Lambda('lambda_18E8')
    def lambda_18E8():
        ChrWalkTo(0x00FE, -61830, 20, 47770, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0000, lambda_18E8)

    Sleep(300)

    TerminateThread(0x0101, 0x00)
    TerminateThread(0x0101, 0x02)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000C, 0xFF)
    Battle(0x00000422, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_192F'),
        (-1, 'loc_1934'),
    )

    def _loc_192F(): pass

    label('loc_192F')

    OP_B4(0x00)

    Jump('loc_1934')

    def _loc_1934(): pass

    label('loc_1934')

    Call(0, 0x0013)

    Return()

# id: 0x0013 offset: 0x1939
@scena.Code('func_13_1939')
def func_13_1939():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_0D()
    TerminateThread(0x000A, 0x01)
    TerminateThread(0x000C, 0x01)
    TerminateThread(0x0101, 0x00)
    TerminateThread(0x0101, 0x02)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetPos(0x0101, -60280, 20, 49830, 90)
    ChrSetPos(0x0109, -60280, 20, 48430, 90)
    ChrSetPos(0x00F8, -61780, 0, 49890, 90)
    ChrSetPos(0x00F9, -61660, 0, 48470, 90)
    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x0109, 0)
    ChrSetSubChip(0x00F8, 0)
    ChrSetSubChip(0x00F9, 0)
    ChrSetChipByIndex(0x0101, 14)
    ChrSetChipByIndex(0x0109, 21)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_19E8'),
        (0x00000005, 'loc_19F0'),
        (0x00000003, 'loc_19F8'),
        (0x00000004, 'loc_1A00'),
        (0x00000006, 'loc_1A08'),
        (0x00000007, 'loc_1A10'),
        (-1, 'loc_1A18'),
    )

    def _loc_19E8(): pass

    label('loc_19E8')

    ChrSetChipByIndex(0x00F8, 15)

    Jump('loc_1A18')

    def _loc_19F0(): pass

    label('loc_19F0')

    ChrSetChipByIndex(0x00F8, 16)

    Jump('loc_1A18')

    def _loc_19F8(): pass

    label('loc_19F8')

    ChrSetChipByIndex(0x00F8, 17)

    Jump('loc_1A18')

    def _loc_1A00(): pass

    label('loc_1A00')

    ChrSetChipByIndex(0x00F8, 18)

    Jump('loc_1A18')

    def _loc_1A08(): pass

    label('loc_1A08')

    ChrSetChipByIndex(0x00F8, 19)

    Jump('loc_1A18')

    def _loc_1A10(): pass

    label('loc_1A10')

    ChrSetChipByIndex(0x00F8, 20)

    Jump('loc_1A18')

    def _loc_1A18(): pass

    label('loc_1A18')

    Sleep(100)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_1A3E'),
        (0x00000005, 'loc_1A46'),
        (0x00000003, 'loc_1A4E'),
        (0x00000004, 'loc_1A56'),
        (0x00000006, 'loc_1A5E'),
        (0x00000007, 'loc_1A66'),
        (-1, 'loc_1A6E'),
    )

    def _loc_1A3E(): pass

    label('loc_1A3E')

    ChrSetChipByIndex(0x00F9, 15)

    Jump('loc_1A6E')

    def _loc_1A46(): pass

    label('loc_1A46')

    ChrSetChipByIndex(0x00F9, 16)

    Jump('loc_1A6E')

    def _loc_1A4E(): pass

    label('loc_1A4E')

    ChrSetChipByIndex(0x00F9, 17)

    Jump('loc_1A6E')

    def _loc_1A56(): pass

    label('loc_1A56')

    ChrSetChipByIndex(0x00F9, 18)

    Jump('loc_1A6E')

    def _loc_1A5E(): pass

    label('loc_1A5E')

    ChrSetChipByIndex(0x00F9, 19)

    Jump('loc_1A6E')

    def _loc_1A66(): pass

    label('loc_1A66')

    ChrSetChipByIndex(0x00F9, 20)

    Jump('loc_1A6E')

    def _loc_1A6E(): pass

    label('loc_1A6E')

    CameraMove(-61210, 0, 49410, 0)
    OP_67(0, 6540, -10000, 0)
    CameraSetDistance(2500, 0)
    OP_6C(315000, 0)
    OP_6E(305, 0)

    @scena.Lambda('lambda_1AB1')
    def lambda_1AB1():
        CameraSetDistance(2370, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1AB1)

    FadeIn(2000, 0)
    OP_0D()
    Fade(250)
    PlaySE(216, 0x00, 0x64)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0109, 65535)
    Sleep(100)

    ChrSetChipByIndex(0x00F8, 65535)
    ChrSetChipByIndex(0x00F9, 65535)
    OP_0D()
    Sleep(300)

    WaitForThreadExit(0x0101, 0x0002)

    @scena.Lambda('lambda_1AF9')
    def lambda_1AF9():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1AF9)

    Sleep(100)

    @scena.Lambda('lambda_1B0C')
    def lambda_1B0C():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_1B0C)

    Sleep(100)

    ChrSetDirection(0x00F8, 90, 400)

    If(
        (
            (Expr.Eval, "OP_29(0x007D, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_1BC4',
    )

    ChrTalk(
        0x0101,
        (
            '#0010321073V#1007F#2P呼～吓我一跳。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010321074V#1002F不过刚才的那些……\n',
            '和废坑中出现的一模一样呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010321075V果然是『结社』的\n',
            '人形兵器吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C28')

    def _loc_1BC4(): pass

    label('loc_1BC4')

    ChrTalk(
        0x0101,
        (
            '#0010321073V#1007F#2P呼～吓我一跳。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010321077V#1002F不过这个……\n',
            '就是『结社』的人形兵器吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C28(): pass

    label('loc_1C28')

    ChrTalk(
        0x0109,
        (
            '#0180321078V#1065F#6P啊啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180321079V#1063F和亚宁堡那里出现的一模一样，\n',
            '是用现代的导力技术制造的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1D43',
    )

    ChrTalk(
        0x0107,
        (
            '#0070321080V#062F#5P那、那么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070321081V这个区域，或许就是人形兵器的\n',
            '零部件制造工厂……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010321082V#1002F#2P确实到处散乱着\n',
            '一样的零件呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D43(): pass

    label('loc_1D43')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1DBD',
    )

    ChrTalk(
        0x0105,
        (
            '#0060321083V#049F#5P不过，真是不可思议……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060321084V刚才引起那样的骚动，\n',
            '却没有人过来看的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F7C')

    def _loc_1DBD(): pass

    label('loc_1DBD')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1E2F',
    )

    ChrTalk(
        0x0104,
        (
            '#0040321085V#034F#5P唔，真是奇怪。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040321086V刚才引起那样的骚动，\n',
            '却没有人过来看的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F7C')

    def _loc_1E2F(): pass

    label('loc_1E2F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1E9F',
    )

    ChrTalk(
        0x0108,
        (
            '#0080321087V#572F#5P真是奇怪……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080321088V刚才引起那样的骚动，\n',
            '却没有人过来看的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F7C')

    def _loc_1E9F(): pass

    label('loc_1E9F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1F17',
    )

    ChrTalk(
        0x0103,
        (
            '#0030321089V#522F#5P不过，真是奇怪啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030321090V刚才引起那样的骚动，\n',
            '却没有人过来看的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F7C')

    def _loc_1F17(): pass

    label('loc_1F17')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1F7C',
    )

    ChrTalk(
        0x0106,
        (
            '#0050321091V#552F#5P真是奇怪……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050321092V引起那样的骚动\n',
            '没有人聚集的样子啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F7C(): pass

    label('loc_1F7C')

    ChrTalk(
        0x0101,
        (
            '#0010321093V#1026F#2P的确……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010321094V#1003F……亚妮拉丝他们\n',
            '真的是被抓来这里的吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180321095V#1065F#6P这些大概是\n',
            '自动巡逻中的人形兵器吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180321096V#1063F总之其它的区域\n',
            '也一并调查看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0380, 6, 0x1C06))
    OP_28(0x0098, 0x01, 0x0004)
    EventEnd(0x00)

    Return()

# id: 0x0014 offset: 0x2059
@scena.Code('func_14_2059')
def func_14_2059():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, -55980, 0, 42910, 0)
    ChrSetFlags(0x00FE, 0x0040)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_2085')
    def lambda_2085():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2085)

    ChrSetChipByIndex(0x000A, 7)
    ChrWalkTo(0x00FE, -55980, 0, 45190, 5000, 0x00)
    ChrWalkTo(0x00FE, -57270, 0, 51560, 5000, 0x00)
    ChrSetChipByIndex(0x000A, 6)
    ChrSetDirection(0x00FE, 266, 400)

    Return()

# id: 0x0015 offset: 0x20CB
@scena.Code('func_15_20CB')
def func_15_20CB():
    Sleep(500)

    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, -55980, 0, 42910, 0)
    ChrSetFlags(0x00FE, 0x0040)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_20FC')
    def lambda_20FC():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_20FC)

    ChrSetChipByIndex(0x000B, 1)
    ChrWalkTo(0x00FE, -55980, 0, 45190, 5000, 0x00)
    ChrWalkTo(0x00FE, -58230, 0, 48960, 5000, 0x00)
    ChrSetChipByIndex(0x000B, 0)
    ChrSetDirection(0x00FE, 266, 400)

    Return()

# id: 0x0016 offset: 0x2142
@scena.Code('func_16_2142')
def func_16_2142():
    Sleep(1000)

    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, -55980, 0, 42910, 0)
    ChrSetFlags(0x00FE, 0x0040)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_2173')
    def lambda_2173():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2173)

    ChrSetChipByIndex(0x000A, 7)
    ChrWalkTo(0x00FE, -55980, 0, 45190, 5000, 0x00)
    ChrWalkTo(0x00FE, -57270, 0, 46240, 5000, 0x00)
    ChrSetChipByIndex(0x000A, 6)
    ChrSetDirection(0x00FE, 266, 400)

    Return()

# id: 0x0017 offset: 0x21B9
@scena.Code('func_17_21B9')
def func_17_21B9():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 7, 0x1C07)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_226D',
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
            TXT(0x00, '【扳动拉杆】\n'),
            TXT(0x01, '【什么也不做】\n'),
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
        'loc_2268',
    )

    Sleep(200)

    OP_B0(0x001E, 0x3C)
    OP_6F(0x001E, 1)
    OP_70(0x001E, 60)
    PlaySE(100, 0x00, 0x64)
    OP_73(0x001E)
    Sleep(200)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x0380, 7, 0x1C07))
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/C5601._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_226A')

    def _loc_2268(): pass

    label('loc_2268')

    EventEnd(0x01)

    def _loc_226A(): pass

    label('loc_226A')

    Jump('loc_2317')

    def _loc_226D(): pass

    label('loc_226D')

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
            TXT(0x00, '【扳动拉杆】\n'),
            TXT(0x01, '【什么也不做】\n'),
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
        'loc_2315',
    )

    Sleep(200)

    OP_B0(0x001E, 0x3C)
    OP_6F(0x001E, 60)
    OP_70(0x001E, 1)
    OP_73(0x001E)
    PlaySE(100, 0x00, 0x64)
    OP_73(0x001E)
    Sleep(200)

    FadeOut(1000, 0, -1)
    OP_0D()
    ClearScenaFlags(ScenaFlag(0x0380, 7, 0x1C07))
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    NewScene('ED6_DT21/C5601._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_2317')

    def _loc_2315(): pass

    label('loc_2315')

    EventEnd(0x01)

    def _loc_2317(): pass

    label('loc_2317')

    Return()

# id: 0x0018 offset: 0x2318
@scena.Code('func_18_2318')
def func_18_2318():
    EventBegin(0x00)
    ChrSetPos(0x0000, -12060, 0, -18650, 271)
    ChrSetPos(0x0001, -12060, 0, -18650, 271)
    ChrSetPos(0x0002, -12060, 0, -18650, 271)
    ChrSetPos(0x0003, -12060, 0, -18650, 271)
    CameraMove(-12060, 0, -18650, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    OP_0D()
    EventEnd(0x00)

    Return()

# id: 0x0019 offset: 0x23A8
@scena.Code('func_19_23A8')
def func_19_23A8():
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门被锁上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    Call(0, 0x001D)

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_241C',
    )

    PlaySE(157, 0x00, 0x64)
    Sleep(1000)

    OP_6F(0x000C, 0)
    OP_70(0x000C, 30)
    OP_73(0x000C)
    OP_64(0x08, 0x0001)
    OP_10(0x1F, 0x01)
    SetScenaFlags(ScenaFlag(0x0382, 0, 0x1C10))

    Jump('loc_2440')

    def _loc_241C(): pass

    label('loc_241C')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_2440',
    )

    PlaySE(171, 0x00, 0x64)
    Sleep(1000)

    Jump('loc_2440')

    def _loc_2440(): pass

    label('loc_2440')

    TalkEnd(0x00FF)

    Return()

# id: 0x001A offset: 0x2444
@scena.Code('func_1A_2444')
def func_1A_2444():
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门被锁上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    Call(0, 0x001D)

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_24B8',
    )

    PlaySE(157, 0x00, 0x64)
    Sleep(1000)

    OP_6F(0x000C, 0)
    OP_70(0x0017, 30)
    OP_73(0x0017)
    OP_64(0x09, 0x0001)
    OP_10(0x20, 0x01)
    SetScenaFlags(ScenaFlag(0x0382, 1, 0x1C11))

    Jump('loc_24DC')

    def _loc_24B8(): pass

    label('loc_24B8')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_24DC',
    )

    PlaySE(171, 0x00, 0x64)
    Sleep(1000)

    Jump('loc_24DC')

    def _loc_24DC(): pass

    label('loc_24DC')

    TalkEnd(0x00FF)

    Return()

# id: 0x001B offset: 0x24E0
@scena.Code('func_1B_24E0')
def func_1B_24E0():
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门被锁上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    Call(0, 0x001D)

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2554',
    )

    PlaySE(157, 0x00, 0x64)
    Sleep(1000)

    OP_6F(0x000B, 0)
    OP_70(0x000B, 30)
    OP_73(0x000B)
    OP_64(0x0A, 0x0001)
    OP_10(0x05, 0x01)
    SetScenaFlags(ScenaFlag(0x0382, 2, 0x1C12))

    Jump('loc_2578')

    def _loc_2554(): pass

    label('loc_2554')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_2578',
    )

    PlaySE(171, 0x00, 0x64)
    Sleep(1000)

    Jump('loc_2578')

    def _loc_2578(): pass

    label('loc_2578')

    TalkEnd(0x00FF)

    Return()

# id: 0x001C offset: 0x257C
@scena.Code('func_1C_257C')
def func_1C_257C():
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门被锁上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    Call(0, 0x001D)

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_25F0',
    )

    PlaySE(157, 0x00, 0x64)
    Sleep(1000)

    OP_6F(0x0013, 0)
    OP_70(0x0013, 30)
    OP_73(0x0013)
    OP_64(0x0B, 0x0001)
    OP_10(0x1D, 0x01)
    SetScenaFlags(ScenaFlag(0x0394, 0, 0x1CA0))

    Jump('loc_2614')

    def _loc_25F0(): pass

    label('loc_25F0')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_2614',
    )

    PlaySE(171, 0x00, 0x64)
    Sleep(1000)

    Jump('loc_2614')

    def _loc_2614(): pass

    label('loc_2614')

    TalkEnd(0x00FF)

    Return()

# id: 0x001D offset: 0x2618
@scena.Code('func_1D_2618')
def func_1D_2618():
    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0381, 1, 0x1C09)),
            Expr.Return,
        ),
        'loc_2633',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_2633(): pass

    label('loc_2633')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0381, 4, 0x1C0C)),
            Expr.Return,
        ),
        'loc_2644',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x2),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_2644(): pass

    label('loc_2644')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0381, 6, 0x1C0E)),
            Expr.Return,
        ),
        'loc_2655',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x4),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_2655(): pass

    label('loc_2655')

    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Switch(
        (
            (Expr.PushReg, 0x2),
            Expr.Return,
        ),
        (0x00000000, 'loc_2681'),
        (0x00000001, 'loc_268E'),
        (0x00000003, 'loc_26EA'),
        (0x00000007, 'loc_276A'),
        (-1, 'loc_280E'),
    )

    def _loc_2681(): pass

    label('loc_2681')

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_280E')

    def _loc_268E(): pass

    label('loc_268E')

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【使用红色密码卡】\n'),
            TXT(0x01, '【什么也不做】\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_26CD'),
        (0x00000001, 'loc_26DA'),
        (-1, 'loc_26E7'),
    )

    def _loc_26CD(): pass

    label('loc_26CD')

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_26E7')

    def _loc_26DA(): pass

    label('loc_26DA')

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_26E7')

    def _loc_26E7(): pass

    label('loc_26E7')

    Jump('loc_280E')

    def _loc_26EA(): pass

    label('loc_26EA')

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【使用红色密码卡】\n'),
            TXT(0x01, '【使用绿色密码卡】\n'),
            TXT(0x02, '【什么也不做】\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2740'),
        (0x00000001, 'loc_274D'),
        (0x00000002, 'loc_275A'),
        (-1, 'loc_2767'),
    )

    def _loc_2740(): pass

    label('loc_2740')

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2767')

    def _loc_274D(): pass

    label('loc_274D')

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2767')

    def _loc_275A(): pass

    label('loc_275A')

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2767')

    def _loc_2767(): pass

    label('loc_2767')

    Jump('loc_280E')

    def _loc_276A(): pass

    label('loc_276A')

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【使用红色密码卡】\n'),
            TXT(0x01, '【使用绿色密码卡】\n'),
            TXT(0x02, '【使用蓝色密码卡】\n'),
            TXT(0x03, '【什么也不做】\n'),
        ),
    )

    MenuEnd(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_27D7'),
        (0x00000001, 'loc_27E4'),
        (0x00000002, 'loc_27F1'),
        (0x00000003, 'loc_27FE'),
        (-1, 'loc_280B'),
    )

    def _loc_27D7(): pass

    label('loc_27D7')

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_280B')

    def _loc_27E4(): pass

    label('loc_27E4')

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_280B')

    def _loc_27F1(): pass

    label('loc_27F1')

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_280B')

    def _loc_27FE(): pass

    label('loc_27FE')

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_280B')

    def _loc_280B(): pass

    label('loc_280B')

    Jump('loc_280E')

    def _loc_280E(): pass

    label('loc_280E')

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

    Return()

# id: 0x001E offset: 0x2826
@scena.Code('func_1E_2826')
def func_1E_2826():
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
        'loc_283D',
    )

    Call(0, 0x0023)
    Call(0, 0x0024)

    def _loc_283D(): pass

    label('loc_283D')

    ChrSetPos(0x0009, -76750, 0, 162560, 0)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0101, -76130, 20, 154070, 0)
    ChrSetPos(0x0109, -77410, 0, 153960, 0)
    ChrSetPos(0x00F8, -76130, 0, 152870, 0)
    ChrSetPos(0x00F9, -77410, 0, 152790, 0)
    CameraMove(-77510, 0, 153430, 0)
    OP_67(0, 8189, -10000, 0)
    CameraSetDistance(2630, 0)
    OP_6C(315000, 0)
    OP_6E(271, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010321097V#1004F#6P咦……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    @scena.Lambda('lambda_290E')
    def lambda_290E():
        CameraMove(-77190, 20, 160620, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_290E)

    @scena.Lambda('lambda_2926')
    def lambda_2926():
        OP_67(0, 4880, -10000, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2926)

    @scena.Lambda('lambda_293E')
    def lambda_293E():
        CameraSetDistance(2680, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_293E)

    @scena.Lambda('lambda_294E')
    def lambda_294E():
        OP_6E(317, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_294E)

    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0101,
        (
            '#0010321098V#1018F#5P库拉茨前辈！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_298A')
    def lambda_298A():
        ChrWalkTo(0x00FE, -75910, 20, 158370, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_298A)

    Sleep(100)

    @scena.Lambda('lambda_29AA')
    def lambda_29AA():
        ChrWalkTo(0x00FE, -77440, 20, 158490, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_29AA)

    Sleep(130)

    @scena.Lambda('lambda_29CA')
    def lambda_29CA():
        ChrWalkTo(0x00FE, -75910, 0, 156960, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_29CA)

    Sleep(110)

    @scena.Lambda('lambda_29EA')
    def lambda_29EA():
        ChrWalkTo(0x00FE, -77440, 0, 157090, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_29EA)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0009,
        (
            '#0310321099V#5P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010321100V#1025F#6P太好了，你没事啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010321101V听克鲁茨前辈说明情况之后，\n',
            '我们也过来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180321102V#1063F#6P等等……他的表情很奇怪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010311209V#1004F#6P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2AF1')
    def lambda_2AF1():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2AF1)

    Sleep(200)

    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0009, 11)
    ChrSetSubChip(0x0009, 0)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#0310321104V#827F#2P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010301311V#1020F#6P啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2B6D')
    def lambda_2B6D():
        CameraMove(-77080, 20, 159880, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2B6D)

    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_2B97')
    def lambda_2B97():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -1500, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2B97)

    Sleep(50)

    OP_62(0x0109, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_2BC9')
    def lambda_2BC9():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -1500, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_2BC9)

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2C05',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x28, 0x2B, 0x00000064, 0x03)

    Jump('loc_2C39')

    def _loc_2C05(): pass

    label('loc_2C05')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2C27',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)

    Jump('loc_2C39')

    def _loc_2C27(): pass

    label('loc_2C27')

    OP_62(0x00F8, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    def _loc_2C39(): pass

    label('loc_2C39')

    @scena.Lambda('lambda_2C3F')
    def lambda_2C3F():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -1500, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_2C3F)

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2C7B',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x28, 0x2B, 0x00000064, 0x03)

    Jump('loc_2CAF')

    def _loc_2C7B(): pass

    label('loc_2C7B')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2C9D',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)

    Jump('loc_2CAF')

    def _loc_2C9D(): pass

    label('loc_2C9D')

    OP_62(0x00F9, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    def _loc_2CAF(): pass

    label('loc_2CAF')

    @scena.Lambda('lambda_2CB5')
    def lambda_2CB5():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -1500, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_2CB5)

    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2CFD',
    )

    ChrTalk(
        0x0106,
        (
            '#0050321106V#057F#6P……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2CFD(): pass

    label('loc_2CFD')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2D2F',
    )

    ChrTalk(
        0x0107,
        (
            '#0070321107V#065F#6P啊哇哇……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2D2F(): pass

    label('loc_2D2F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2D63',
    )

    ChrTalk(
        0x0103,
        (
            '#0030321108V#523F#6P难不成……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2D63(): pass

    label('loc_2D63')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2D99',
    )

    ChrTalk(
        0x0108,
        (
            '#0080321109V#077F#6P……中计了吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2D99(): pass

    label('loc_2D99')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2DCD',
    )

    ChrTalk(
        0x0105,
        (
            '#0060321110V#043F#6P怎么会……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2DCD(): pass

    label('loc_2DCD')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2E01',
    )

    ChrTalk(
        0x0104,
        (
            '#0040321111V#032F#6P糟糕了……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2E01(): pass

    label('loc_2E01')

    Sleep(200)

    CreateThread(0x000A, 0x00, 0x00, func_1F_2FD5)
    Sleep(200)

    CreateThread(0x000C, 0x00, 0x00, func_20_3033)
    Sleep(300)

    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x0109, 0)
    ChrSetSubChip(0x00F8, 0)
    ChrSetSubChip(0x00F9, 0)
    ChrSetChipByIndex(0x0101, 14)
    Sleep(100)

    ChrSetChipByIndex(0x0109, 21)
    Sleep(100)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_2E71'),
        (0x00000005, 'loc_2E79'),
        (0x00000003, 'loc_2E81'),
        (0x00000004, 'loc_2E89'),
        (0x00000006, 'loc_2E91'),
        (0x00000007, 'loc_2E99'),
        (-1, 'loc_2EA1'),
    )

    def _loc_2E71(): pass

    label('loc_2E71')

    ChrSetChipByIndex(0x00F8, 15)

    Jump('loc_2EA1')

    def _loc_2E79(): pass

    label('loc_2E79')

    ChrSetChipByIndex(0x00F8, 16)

    Jump('loc_2EA1')

    def _loc_2E81(): pass

    label('loc_2E81')

    ChrSetChipByIndex(0x00F8, 17)

    Jump('loc_2EA1')

    def _loc_2E89(): pass

    label('loc_2E89')

    ChrSetChipByIndex(0x00F8, 18)

    Jump('loc_2EA1')

    def _loc_2E91(): pass

    label('loc_2E91')

    ChrSetChipByIndex(0x00F8, 19)

    Jump('loc_2EA1')

    def _loc_2E99(): pass

    label('loc_2E99')

    ChrSetChipByIndex(0x00F8, 20)

    Jump('loc_2EA1')

    def _loc_2EA1(): pass

    label('loc_2EA1')

    Sleep(100)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_2EC7'),
        (0x00000005, 'loc_2ECF'),
        (0x00000003, 'loc_2ED7'),
        (0x00000004, 'loc_2EDF'),
        (0x00000006, 'loc_2EE7'),
        (0x00000007, 'loc_2EEF'),
        (-1, 'loc_2EF7'),
    )

    def _loc_2EC7(): pass

    label('loc_2EC7')

    ChrSetChipByIndex(0x00F9, 15)

    Jump('loc_2EF7')

    def _loc_2ECF(): pass

    label('loc_2ECF')

    ChrSetChipByIndex(0x00F9, 16)

    Jump('loc_2EF7')

    def _loc_2ED7(): pass

    label('loc_2ED7')

    ChrSetChipByIndex(0x00F9, 17)

    Jump('loc_2EF7')

    def _loc_2EDF(): pass

    label('loc_2EDF')

    ChrSetChipByIndex(0x00F9, 18)

    Jump('loc_2EF7')

    def _loc_2EE7(): pass

    label('loc_2EE7')

    ChrSetChipByIndex(0x00F9, 19)

    Jump('loc_2EF7')

    def _loc_2EEF(): pass

    label('loc_2EEF')

    ChrSetChipByIndex(0x00F9, 20)

    Jump('loc_2EF7')

    def _loc_2EF7(): pass

    label('loc_2EF7')

    OP_0D()
    WaitForThreadExit(0x000A, 0x0000)
    WaitForThreadExit(0x000C, 0x0000)
    Sleep(1000)

    @scena.Lambda('lambda_2F0D')
    def lambda_2F0D():
        CameraMove(-77520, 20, 158730, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2F0D)

    @scena.Lambda('lambda_2F25')
    def lambda_2F25():
        CameraSetDistance(2230, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2F25)

    ChrSetChipByIndex(0x0009, 27)

    @scena.Lambda('lambda_2F3A')
    def lambda_2F3A():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -4000, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_2F3A)

    Sleep(50)

    ChrSetChipByIndex(0x000A, 7)

    @scena.Lambda('lambda_2F5F')
    def lambda_2F5F():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -4000, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_2F5F)

    Sleep(50)

    ChrSetChipByIndex(0x000C, 7)

    @scena.Lambda('lambda_2F84')
    def lambda_2F84():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, -4000, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0000, lambda_2F84)

    Sleep(300)

    TerminateThread(0x0101, 0x00)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000C, 0xFF)
    Battle(0x0000041E, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_2FCB'),
        (-1, 'loc_2FD0'),
    )

    def _loc_2FCB(): pass

    label('loc_2FCB')

    OP_B4(0x00)

    Jump('loc_2FD0')

    def _loc_2FD0(): pass

    label('loc_2FD0')

    Call(0, 0x0021)

    Return()

# id: 0x001F offset: 0x2FD5
@scena.Code('func_1F_2FD5')
def func_1F_2FD5():
    CreateThread(0x00FE, 0x03, 0x00, func_02_7EC)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetFlags(0x00FE, 0x0004)
    ChrSetPos(0x00FE, -76000, 1200, 164220, 180)
    ChrClearFlags(0x00FE, 0x0080)
    PlaySE(529, 0x00, 0x64)
    PlaySE(533, 0x00, 0x64)

    @scena.Lambda('lambda_3012')
    def lambda_3012():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3012)

    ChrMoveTo(0x00FE, -76000, 0, 164220, 2000, 0x00)

    Return()

# id: 0x0020 offset: 0x3033
@scena.Code('func_20_3033')
def func_20_3033():
    CreateThread(0x00FE, 0x03, 0x00, func_02_7EC)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetFlags(0x00FE, 0x0004)
    ChrSetPos(0x00FE, -78260, 1200, 164170, 180)
    ChrClearFlags(0x00FE, 0x0080)
    PlaySE(529, 0x00, 0x64)
    PlaySE(533, 0x00, 0x64)

    @scena.Lambda('lambda_3070')
    def lambda_3070():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3070)

    ChrMoveTo(0x00FE, -78260, 0, 164170, 2000, 0x00)

    Return()

# id: 0x0021 offset: 0x3091
@scena.Code('func_21_3091')
def func_21_3091():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_0D()
    TerminateThread(0x0009, 0x00)
    TerminateThread(0x000A, 0x00)
    TerminateThread(0x000C, 0x00)
    TerminateThread(0x0101, 0x00)
    TerminateThread(0x0101, 0x01)
    ChrSetPos(0x0009, -76700, 20, 163790, 180)
    ChrSetChipByIndex(0x0009, 12)
    ChrSetSubChip(0x0009, 0)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetPos(0x0101, -76090, 20, 161510, 0)
    ChrSetPos(0x0109, -77180, 20, 161610, 0)
    ChrSetPos(0x00F8, -75650, 20, 160360, 0)
    ChrSetPos(0x00F9, -77190, 20, 160470, 0)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0109, 65535)
    ChrSetSubChip(0x0109, 0)
    ChrSetChipByIndex(0x00F8, 65535)
    ChrSetSubChip(0x00F8, 0)
    ChrSetChipByIndex(0x00F9, 65535)
    ChrSetSubChip(0x00F9, 0)
    CameraMove(-76900, 20, 162590, 0)
    OP_67(0, 5400, -10000, 0)
    CameraSetDistance(2740, 0)
    OP_6C(315000, 0)
    OP_6E(298, 0)
    FadeIn(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010321112V#1007F#6P呼呼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010321113V#1015F实、实在是……\n',
            '相当不好对付呢。',
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
        'loc_3257',
    )

    ChrTalk(
        0x0106,
        (
            '#0050321114V#552F#6P哼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050321115V『渡鸦帮』的那些人还好说，\n',
            '居然连游击士都能操纵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3390')

    def _loc_3257(): pass

    label('loc_3257')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_32AF',
    )

    ChrTalk(
        0x0105,
        (
            '#0060321116V#049F#6P……和在灯塔被操纵的\n',
            '『渡鸦帮』那些人一样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3390')

    def _loc_32AF(): pass

    label('loc_32AF')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_32FF',
    )

    ChrTalk(
        0x0103,
        (
            '#0030321117V#522F#6P伤脑筋了……\n',
            '没想到连游击士也能操纵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3390')

    def _loc_32FF(): pass

    label('loc_32FF')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_334B',
    )

    ChrTalk(
        0x0104,
        (
            '#0040321118V#034F#6P哎呀呀……\n',
            '居然连游击士也能操纵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3390')

    def _loc_334B(): pass

    label('loc_334B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3390',
    )

    ChrTalk(
        0x0108,
        (
            '#0080321119V#074F#6P唔……\n',
            '居然连游击士也能操纵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3390(): pass

    label('loc_3390')

    ChrTalk(
        0x0109,
        (
            '#0180321120V#1065F#6P接下来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_33BB')
    def lambda_33BB():
        CameraMove(-76780, 0, 163200, 1500)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_33BB)

    ChrWalkTo(0x0109, -76960, 20, 162600, 1500, 0x00)
    WaitForThreadExit(0x0109, 0x0001)
    Fade(500)
    ChrSetChipByIndex(0x0109, 26)
    ChrSetSubChip(0x0109, 0)
    Sleep(500)

    PlaySE(216, 0x00, 0x64)
    ChrSetSubChip(0x0109, 1)
    Sleep(1000)

    LoadEffect(0x00, 'scraft\\\\sc008_02.eff')
    PlayEffect(0x00, 0xFF, 0x0109, 300, 1100, 500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(2000)

    LoadEffect(0x00, 'scraft\\\\sc001_05.eff')
    PlayEffect(0x00, 0xFF, 0x0009, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1500)

    OP_9E(0x0009, 20, 0, 500, 3000)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#0310321121V#826F#2P唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Fade(500)
    ChrSetSubChip(0x0009, 1)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#0310321122V#825F#2P……抱歉……\n',
            '好像给你们添麻烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    ChrSetChipByIndex(0x0109, 65535)
    OP_0D()

    @scena.Lambda('lambda_3548')
    def lambda_3548():
        ChrMoveTo(0x00FE, -77180, 20, 161610, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_3548)

    ChrTalk(
        0x0101,
        (
            '#0010321123V#1025F#6P库拉茨前辈……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_35C8',
    )

    ChrTalk(
        0x0103,
        (
            '#0030321124V#020F#6P看来搞清楚\n',
            '状况了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_36D1')

    def _loc_35C8(): pass

    label('loc_35C8')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_360C',
    )

    ChrTalk(
        0x0106,
        (
            '#0050321125V#051F#6P哦，看来搞清楚\n',
            '状况了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_36D1')

    def _loc_360C(): pass

    label('loc_360C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_364C',
    )

    ChrTalk(
        0x0108,
        (
            '#0080321126V#070F#6P看来搞清楚\n',
            '状况了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_36D1')

    def _loc_364C(): pass

    label('loc_364C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3690',
    )

    ChrTalk(
        0x0104,
        (
            '#0040321127V#030F#6P呼，看来搞清楚\n',
            '状况了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_36D1')

    def _loc_3690(): pass

    label('loc_3690')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_36D1',
    )

    ChrTalk(
        0x0105,
        (
            '#0060321128V#542F#6P看来好像\n',
            '搞清楚状况了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_36D1(): pass

    label('loc_36D1')

    ChrTalk(
        0x0009,
        (
            '#0310321129V#823F#2P嗯嗯，虽然想不起对方长相，\n',
            '但确实被某人夺取了我的意识……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0310321130V#822F然后命令我在这里\n',
            '击退新的侵入者……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010321131V#1007F#6P是那个『教授』吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010321132V#1002F你知道亚妮拉丝和\n',
            '卡露娜她们在哪里吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0310321133V#824F#2P不……我们是分别被抓来的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0310321134V应该和我一样\n',
            '被抓到某处去了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0310321135V#826F呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x0009, 20, 0, 500, 3000)
    ChrSetSubChip(0x0009, 0)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010321136V#1020F#6P没、没事吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0101, -76050, 20, 162910, 2000, 0x00)
    Fade(250)
    ChrSetDirection(0x0101, 315, 400)
    ChrSetChipByIndex(0x0101, 24)
    ChrSetSubChip(0x0101, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010321137V#1025F#6P来，扶我的肩膀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010321138V悬崖下有条小船，\n',
            '我带你到那里去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0009, 1)
    Sleep(200)

    ChrTalk(
        0x0009,
        (
            '#0310321139V#824F#5P不、不要紧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0310321140V我知道这个建筑物的构造，\n',
            '一个人也可以逃出去……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Fade(250)
    ChrSetSubChip(0x0009, 0)
    ChrSetChipByIndex(0x0009, 10)
    OP_0D()
    Sleep(200)

    Fade(500)
    ChrSetChipByIndex(0x0101, 65535)
    OP_0D()
    ChrSetDirection(0x0101, 0, 400)
    ChrMoveTo(0x0101, -76090, 20, 161510, 2000, 0x00)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0310321141V#825F#2P而且我也不想\n',
            '再继续扯你们的后腿了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0310321142V就算是请你们代替我吧，\n',
            '卡露娜和亚妮拉丝就拜托了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010321143V#1026F#6P库拉茨前辈……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010321144V#1006F嗯……交给我们吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3A97')
    def lambda_3A97():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_3A97')

    DispatchAsync2(0x0101, 0x0001, lambda_3A97)

    @scena.Lambda('lambda_3AA8')
    def lambda_3AA8():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_3AA8')

    DispatchAsync2(0x0109, 0x0001, lambda_3AA8)

    @scena.Lambda('lambda_3AB9')
    def lambda_3AB9():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_3AB9')

    DispatchAsync2(0x00F8, 0x0001, lambda_3AB9)

    @scena.Lambda('lambda_3ACA')
    def lambda_3ACA():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_3ACA')

    DispatchAsync2(0x00F9, 0x0001, lambda_3ACA)

    @scena.Lambda('lambda_3ADB')
    def lambda_3ADB():
        CameraMove(-76640, 50, 156810, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3ADB)

    ChrWalkTo(0x0009, -74610, 20, 161680, 2000, 0x00)

    @scena.Lambda('lambda_3B07')
    def lambda_3B07():
        OP_9E(0x00FE, 20, 0, 1000, 3000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3B07)

    ChrWalkTo(0x0009, -74340, 20, 158200, 2500, 0x00)

    @scena.Lambda('lambda_3B35')
    def lambda_3B35():
        OP_9E(0x00FE, 20, 0, 1000, 3000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3B35)

    ChrWalkTo(0x0009, -76760, 0, 152830, 2000, 0x00)

    @scena.Lambda('lambda_3B63')
    def lambda_3B63():
        OP_9E(0x00FE, 20, 0, 1000, 3000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3B63)

    ChrWalkTo(0x0009, -76800, 0, 151200, 2500, 0x00)

    @scena.Lambda('lambda_3B91')
    def lambda_3B91():
        ChrWalkTo(0x00FE, -76810, 0, 150660, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3B91)

    ChrSetRGBAMask(0x0009, 255, 255, 255, 0, 500)
    WaitForThreadExit(0x0009, 0x0001)
    ChrSetFlags(0x0009, 0x0080)
    WaitForThreadExit(0x0101, 0x0000)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0109, 0x01)
    TerminateThread(0x00F8, 0x01)
    TerminateThread(0x00F9, 0x01)

    @scena.Lambda('lambda_3BD6')
    def lambda_3BD6():
        CameraMove(-76830, 0, 161490, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3BD6)

    ChrSetDirection(0x0101, 180, 400)
    ChrSetDirection(0x0109, 180, 400)
    ChrSetDirection(0x00F8, 180, 400)
    ChrSetDirection(0x00F9, 180, 400)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(200)

    ChrTalk(
        0x0101,
        (
            '#0010321145V#1015F#2P没、没问题吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0109, 90, 400)

    ChrTalk(
        0x0109,
        (
            '#0180321146V#1065F#5P现在只有相信那位老兄\n',
            '继续前进了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180321147V#1060F还剩两个人吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010321148V#1002F#4P嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3CCC')
    def lambda_3CCC():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_3CCC)

    Sleep(50)

    @scena.Lambda('lambda_3CDF')
    def lambda_3CDF():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_3CDF)

    WaitForThreadExit(0x00F9, 0x0001)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3D2E',
    )

    ChrTalk(
        0x0106,
        (
            '#0050321149V#057F#6P哎……\n',
            '看来动作要快了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E2E')

    def _loc_3D2E(): pass

    label('loc_3D2E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3D6D',
    )

    ChrTalk(
        0x0103,
        (
            '#0030321150V#022F#6P看来动作要快了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E2E')

    def _loc_3D6D(): pass

    label('loc_3D6D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3DAF',
    )

    ChrTalk(
        0x0104,
        (
            '#0040321151V#032F#6P唔……\n',
            '看来动作要快了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E2E')

    def _loc_3DAF(): pass

    label('loc_3DAF')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3DF0',
    )

    ChrTalk(
        0x0108,
        (
            '#0080321152V#072F#6P看来要抓紧时间了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E2E')

    def _loc_3DF0(): pass

    label('loc_3DF0')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3E2E',
    )

    ChrTalk(
        0x0105,
        (
            '#0060321153V#042F#6P看来要抓紧时间了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3E2E(): pass

    label('loc_3E2E')

    SetScenaFlags(ScenaFlag(0x0381, 0, 0x1C08))
    OP_28(0x0098, 0x01, 0x0008)
    OP_28(0x0098, 0x01, 0x0010)
    EventEnd(0x00)

    Return()

# id: 0x0022 offset: 0x3E40
@scena.Code('func_22_3E40')
def func_22_3E40():
    EventBegin(0x00)
    PlaySE(156, 0x00, 0x64)
    Sleep(500)

    PlaySE(157, 0x00, 0x64)
    OP_74(0x001D, 0x00000000, 0x0003)
    SetMessageWindowPos(-1, -1, 24, 5)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S『人形兵器的种类』\n',
            ' \n',
            '结社运用的人形兵器\n',
            '是使徒直属研究机关『十三工房』\n',
            '所开发的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_74(0x001D, 0x00000000, 0x0002)
    SetMessageWindowPos(-1, -1, 24, 5)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S此外，本设施中，\n',
            '除了预警机『哨兵２』类型以外，\n',
            '侦察机『目标探索者』，战斗机『亡命守护者』等\n',
            '旧型号的人形兵器也是主要生产的对象，\n',
            '但也有参考『守护者』开发新的型号……（※以下删除）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0381, 1, 0x1C09)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3FF5',
    )

    Sleep(500)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['红色密码卡']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['红色密码卡'], 1)
    Sleep(500)

    def _loc_3FF5(): pass

    label('loc_3FF5')

    SetScenaFlags(ScenaFlag(0x0381, 1, 0x1C09))
    OP_28(0x0098, 0x01, 0x0020)
    OP_74(0x001D, 0x00000000, 0x0000)
    PlaySE(156, 0x00, 0x64)
    Sleep(500)

    EventEnd(0x01)

    Return()

# id: 0x0023 offset: 0x4014
@scena.Code('func_23_4014')
def func_23_4014():
    FadeOut(0, 0, -1)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
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
        (0x00000000, 'loc_4091'),
        (0x00000001, 'loc_4097'),
        (-1, 'loc_409D'),
    )

    def _loc_4091(): pass

    label('loc_4091')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_409D')

    def _loc_4097(): pass

    label('loc_4097')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_409D')

    def _loc_409D(): pass

    label('loc_409D')

    Return()

# id: 0x0024 offset: 0x409E
@scena.Code('func_24_409E')
def func_24_409E():
    MapClearFlags(0x00000001)
    CameraMove(64510, 0, -14780, 92)
    Sleep(100)

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['凯文神父'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['雪拉扎德'],
            ChrTable['提妲'],
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            ChrTable['金'],
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
    OP_69(0x0000, 0)
    Sleep(1000)

    Return()

# id: 0x0025 offset: 0x40FB
@scena.Code('func_25_40FB')
def func_25_40FB():
    EventBegin(0x01)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门牢牢地关着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0026 offset: 0x4156
@scena.Code('func_26_4156')
def func_26_4156():
    SetScenaFlags(ScenaFlag(0x0393, 2, 0x1C9A))
    ClearScenaFlags(ScenaFlag(0x0393, 3, 0x1C9B))
    ClearScenaFlags(ScenaFlag(0x0393, 4, 0x1C9C))
    ClearScenaFlags(ScenaFlag(0x0393, 5, 0x1C9D))
    ClearScenaFlags(ScenaFlag(0x0393, 6, 0x1C9E))
    ClearScenaFlags(ScenaFlag(0x0393, 7, 0x1C9F))

    Return()

# id: 0x0027 offset: 0x4169
@scena.Code('func_27_4169')
def func_27_4169():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_41BA',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '导力好像停止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Jump('loc_4375')

    def _loc_41BA(): pass

    label('loc_41BA')

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
        'loc_435A',
    )

    FadeIn(100, 0)
    Sleep(500)

    OP_26(13)
    StopEffect(0x01, 0x02)
    PlayEffect(0x01, 0x01, 0x00FF, -9010, 1000, 138700, 0, 0, 0, 700, 700, 700, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x001F, 0)
    OP_70(0x001F, 50)
    OP_73(0x001F)
    OP_20(0x00000BB8)
    PlaySE(12, 0x00, 0x64)
    StopEffect(0x01, 0x02)
    LoadEffect(0x02, 'map\\\\mp027_01.eff')
    PlayEffect(0x02, 0x02, 0x00FF, -9010, 1000, 138700, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    FadeOut(1000, 0, -1)
    Sleep(700)

    PlaySE(13, 0x00, 0x64)
    OP_0D()
    ChrSetStatus(0x00FF, 0xFE, 0)
    OP_69(0x0000, 0)
    OP_30(0x01)
    Sleep(3500)

    StopEffect(0x02, 0x02)
    PlayEffect(0x01, 0x01, 0x00FF, -9010, 1000, 138700, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x001F, 0)
    OP_1E()
    FadeIn(1000, 0)
    OP_56(0x00)
    TalkEnd(0x00FF)

    Return()

    def _loc_435A(): pass

    label('loc_435A')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4374',
    )

    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

    def _loc_4374(): pass

    label('loc_4374')

    Return()

    def _loc_4375(): pass

    label('loc_4375')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

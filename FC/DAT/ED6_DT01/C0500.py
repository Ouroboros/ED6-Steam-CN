import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C0500_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C0500   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '目标用摄像机'),
    TXT(0x02, '肮脏甲鼠2'),
    TXT(0x03, '紫色飞蛾群2'),
    TXT(0x04, '肮脏甲鼠3'),
    TXT(0x05, '肮脏甲鼠4'),
    TXT(0x06, '肮脏甲鼠4'),
    TXT(0x07, '肮脏甲鼠'),
    TXT(0x08, '肮脏甲鼠'),
    TXT(0x09, '紫色飞蛾群'),
    TXT(0x0A, '紫色飞蛾群'),
    TXT(0x0B, '紫色飞蛾群'),
    TXT(0x0C, '肮脏甲鼠'),
    TXT(0x0D, '肮脏甲鼠'),
    TXT(0x0E, '紫色飞蛾群'),
    TXT(0x0F, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0500.x'
    header.mapIndex       = 20
    header.bgm            = 31
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x25AD
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
            word_32         = 45,
            word_34         = 45,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 20,
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
        ('ED6_DT09/CH10110._CH', 'ED6_DT09/CH10110P._CP'),
        ('ED6_DT09/CH10111._CH', 'ED6_DT09/CH10111P._CP'),
        ('ED6_DT09/CH10270._CH', 'ED6_DT09/CH10270P._CP'),
        ('ED6_DT09/CH10271._CH', 'ED6_DT09/CH10271P._CP'),
    ]

# id: 0x10002 offset: 0xCA
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
            npcIndex            = 0x0080,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 2000,
            z                   = 0,
            y                   = 10000,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0141,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -17000,
            z                   = 0,
            y                   = 14000,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0141,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -20000,
            z                   = 0,
            y                   = 28000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0141,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -24000,
            z                   = 460,
            y                   = 37000,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0141,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -28000,
            z                   = 0,
            y                   = 55800,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0141,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x18A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = 11000,
            z           = 0,
            y           = 0,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x002A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -1000,
            z           = 0,
            y           = 14000,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x002B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -20000,
            z           = 0,
            y           = 16000,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x002D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -4000,
            z           = 0,
            y           = 30000,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x002E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -20000,
            z           = 0,
            y           = 51000,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x002F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -24000,
            z           = 460,
            y           = 37000,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x002C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -28000,
            z           = 0,
            y           = 55800,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0030,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -19000,
            z           = 0,
            y           = 29000,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x002F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x26A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 2000,
            y           = 0,
            z           = 10000,
            range       = 3000,
            dword_10    = 0x000009C4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000005,
        ),
        ScenaEventData(
            x           = -17000,
            y           = 0,
            z           = 14000,
            range       = 3000,
            dword_10    = 0x000009C4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000006,
        ),
        ScenaEventData(
            x           = -20000,
            y           = 0,
            z           = 28000,
            range       = 3000,
            dword_10    = 0x000009C4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000007,
        ),
        ScenaEventData(
            x           = -24000,
            y           = 0,
            z           = 37000,
            range       = 3000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000008,
        ),
        ScenaEventData(
            x           = -28000,
            y           = 0,
            z           = 55800,
            range       = 3000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000009,
        ),
        ScenaEventData(
            x           = 6170,
            y           = -1000,
            z           = 2310,
            range       = 8320,
            dword_10    = 0x000009C4,
            dword_14    = 0xFFFFF5B0,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000D,
        ),
        ScenaEventData(
            x           = 4180,
            y           = -1000,
            z           = 1490,
            range       = -1300,
            dword_10    = 0x000009C4,
            dword_14    = 0x0000127A,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000C,
        ),
    )

# id: 0x10005 offset: 0x34A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 3200,
            triggerZ            = 0,
            triggerY            = -17000,
            triggerRange        = 800,
            actorX              = 3200,
            actorZ              = 1000,
            actorY              = -17000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -28000,
            triggerZ            = 0,
            triggerY            = 57000,
            triggerRange        = 800,
            actorX              = -28000,
            actorZ              = 1000,
            actorY              = 57000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -1500,
            triggerZ            = 0,
            triggerY            = 30000,
            triggerRange        = 800,
            actorX              = -1500,
            actorZ              = 1000,
            actorY              = 30000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000E,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -19960,
            triggerZ            = 0,
            triggerY            = 53960,
            triggerRange        = 800,
            actorX              = -19960,
            actorZ              = 1000,
            actorY              = 53960,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -19960,
            triggerZ            = 0,
            triggerY            = 53960,
            triggerRange        = 800,
            actorX              = -19960,
            actorZ              = 1000,
            actorY              = 53960,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -19960,
            triggerZ            = 0,
            triggerY            = 51810,
            triggerRange        = 800,
            actorX              = -19960,
            actorZ              = 0,
            actorY              = 51810,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 15800,
            triggerZ            = 0,
            triggerY            = -160,
            triggerRange        = 1000,
            actorX              = 15800,
            actorZ              = 1000,
            actorY              = -160,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000F,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x446
@scena.Code('PreInit')
def PreInit():
    SetChrPos(0x0101, 1370, 0, -15162, 0)
    SetChrPos(0x0102, 1370, 0, -15162, 0)
    OP_69(0x0101, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0051, 4, 0x28C)),
            Expr.Return,
        ),
        'loc_47B',
    )

    SetChrFlags(0x0014, 0x0080)

    def _loc_47B(): pass

    label('loc_47B')

    Return()

# id: 0x0001 offset: 0x47C
@scena.Code('Init')
def Init():
    ClearMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_4A4',
    )

    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000D, 0x0080)

    Jump('loc_625')

    def _loc_4A4(): pass

    label('loc_4A4')

    SetChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000F, 0x0080)
    SetChrFlags(0x0010, 0x0080)
    SetChrFlags(0x0011, 0x0080)
    SetChrFlags(0x0012, 0x0080)
    SetChrFlags(0x0013, 0x0080)
    SetChrFlags(0x0014, 0x0080)
    SetChrFlags(0x0015, 0x0080)

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x11),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_505',
    )

    Call(0, 0x0010)
    SetChrPos(0x0000, 2000, 0, 7000, 0)
    OP_30(0x00)
    OP_69(0x0101, 0)

    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x2),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_505',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    def _loc_505(): pass

    label('loc_505')

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x12),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_53E',
    )

    Call(0, 0x0010)
    SetChrPos(0x0000, -13680, 0, 14260, 270)
    OP_30(0x00)
    OP_69(0x0101, 0)

    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x2),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_53E',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_53E(): pass

    label('loc_53E')

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x13),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_577',
    )

    Call(0, 0x0010)
    SetChrPos(0x0000, -19860, 0, 24930, 0)
    OP_30(0x00)
    OP_69(0x0101, 0)

    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x2),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_577',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    def _loc_577(): pass

    label('loc_577')

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x10),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5B0',
    )

    Call(0, 0x0010)
    SetChrPos(0x0000, -21300, 150, 37200, 270)
    OP_30(0x00)
    OP_69(0x0101, 0)

    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x2),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5B0',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    def _loc_5B0(): pass

    label('loc_5B0')

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0xF),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5E9',
    )

    Call(0, 0x0010)
    SetChrPos(0x0000, -27900, 0, 53010, 0)
    OP_30(0x00)
    OP_69(0x0101, 0)

    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x2),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5E9',
    )

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    def _loc_5E9(): pass

    label('loc_5E9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_5F5',
    )

    SetChrFlags(0x0009, 0x0080)

    def _loc_5F5(): pass

    label('loc_5F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_601',
    )

    SetChrFlags(0x000A, 0x0080)

    def _loc_601(): pass

    label('loc_601')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_60D',
    )

    SetChrFlags(0x000B, 0x0080)

    def _loc_60D(): pass

    label('loc_60D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_619',
    )

    SetChrFlags(0x000C, 0x0080)

    def _loc_619(): pass

    label('loc_619')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_625',
    )

    SetChrFlags(0x000D, 0x0080)

    def _loc_625(): pass

    label('loc_625')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0051, 2, 0x28A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_637',
    )

    OP_6F(0x0001, 0)

    Jump('loc_63E')

    def _loc_637(): pass

    label('loc_637')

    OP_6F(0x0001, 60)

    def _loc_63E(): pass

    label('loc_63E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0051, 3, 0x28B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_650',
    )

    OP_6F(0x0002, 0)

    Jump('loc_657')

    def _loc_650(): pass

    label('loc_650')

    OP_6F(0x0002, 60)

    def _loc_657(): pass

    label('loc_657')

    If(
        (
            (Expr.Eval, "OP_29(0x0004, 0x01, 0x0004)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0004, 0x01, 0x0020)"),
            Expr.Or,
            (Expr.Eval, "OP_29(0x0004, 0x01, 0x8000)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_67A',
    )

    OP_64(0x05, 0x0001)

    Jump('loc_6C3')

    def _loc_67A(): pass

    label('loc_67A')

    LoadEffect(0x06, 'map\\\\evsepith.eff')
    PlayEffect(0x06, 0x06, 0x00FF, -19960, 200, 51810, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    def _loc_6C3(): pass

    label('loc_6C3')

    OP_6F(0x0000, 0)
    OP_72(0x0000, 0x0010)
    PlaySE(461, 0x01, 0x64)
    LoadEffect(0x00, 'map\\\\mp027_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, 15800, 1000, -160, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)

    Return()

# id: 0x0002 offset: 0x71E
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_733',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_733(): pass

    label('loc_733')

    Return()

# id: 0x0003 offset: 0x734
@scena.Code('func_03_734')
def func_03_734():
    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '铁门已经生锈得不能再打开了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

# id: 0x0004 offset: 0x783
@scena.Code('func_04_783')
def func_04_783():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_796',
    )

    NewScene('ED6_DT01/T0100._SN', 1, 0, 0)
    IdleLoop()

    Jump('loc_868')

    def _loc_796(): pass

    label('loc_796')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0051, 2, 0x28A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_848',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7FB',
    )

    ChrTalk(
        0x0102,
        (
            '#0020000584V#012F艾丝蒂尔，等等。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000585V#012F我们还没有回收搜索对象啊。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_841')

    def _loc_7FB(): pass

    label('loc_7FB')

    ChrTalk(
        0x0102,
        (
            '#0020000586V#012F在回到地上之前一定要把\n',
            '搜索对象回收了才算是完成任务。',
            TxtCtl.Enter,
        ),
    )

    def _loc_841(): pass

    label('loc_841')

    CloseMessageWindow()
    TalkEnd(0x00FF)

    Jump('loc_868')

    def _loc_848(): pass

    label('loc_848')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_85F',
    )

    SetScenaFlags(ScenaFlag(0x0045, 7, 0x22F))
    NewScene('ED6_DT01/T0100._SN', 2, 0, 0)
    IdleLoop()

    Jump('loc_868')

    def _loc_85F(): pass

    label('loc_85F')

    NewScene('ED6_DT01/T0100._SN', 0, 0, 0)
    IdleLoop()

    def _loc_868(): pass

    label('loc_868')

    Return()

# id: 0x0005 offset: 0x869
@scena.Code('func_05_869')
def func_05_869():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_871',
    )

    Return()

    def _loc_871(): pass

    label('loc_871')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_879',
    )

    Return()

    def _loc_879(): pass

    label('loc_879')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_885',
    )

    EventBegin(0x01)

    Jump('loc_9FB')

    def _loc_885(): pass

    label('loc_885')

    EventBegin(0x00)
    OP_92(0x0001, 0x0000, 800, 3000, 0x00)

    @scena.Lambda('lambda_089B')
    def lambda_089B():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_089B)

    @scena.Lambda('lambda_08A9')
    def lambda_08A9():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_08A9)

    OP_69(0x0009, 1000)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010000554V#002F……出现了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000555V#012F艾丝蒂尔，\n',
            '小心别让它绕到自己背后。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000556V#002F知道啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※魔兽的样子是无法从远处看到的。\n',
            '  在接近到一定距离后才能看清它们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※根据接触方式不同，战斗开始时的状况也会不同。\n',
            '  接触魔兽背后有利战斗，\n',
            '  被魔兽从背后接触则不利战斗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_9FB(): pass

    label('loc_9FB')

    @scena.Lambda('lambda_0A01')
    def lambda_0A01():
        OP_92(0x0000, 0x0009, 500, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0A01)

    @scena.Lambda('lambda_0A16')
    def lambda_0A16():
        OP_92(0x0001, 0x0009, 800, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0A16)

    Sleep(200)

    Battle(0x00000011, 0x0010000B, 0x00, 0x0000, 0x09)
    EventBegin(0x00)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrPos(0x0101, 1810, 0, 10700, 0)
    SetChrPos(0x0102, 1810, 0, 9370, 0)
    OP_69(0x0101, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010000557V#502F哼哼，比预想中轻松啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000558V#508F好！\n',
            '保持这种势头，继续前进吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020000559V#010F艾丝蒂尔，等一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000560V#010F我们先把刚才那种魔兽\n',
            '记录到魔兽手册中吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010000561V#008F啊，有道理。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000562V#502F（奋笔疾书）……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000563V#006F好，记下来啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※在战斗中所遇到的对手的情报\n',
            '  会被自动记录到魔兽手册中。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '※另外，取胜时记录的内容和逃\n',
            '  跑时记录的内容是不同的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    EventEnd(0x02)
    SetMapFlags(0x00000001)

    Return()

# id: 0x0006 offset: 0xC2C
@scena.Code('func_06_C2C')
def func_06_C2C():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_C34',
    )

    Return()

    def _loc_C34(): pass

    label('loc_C34')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_C3C',
    )

    Return()

    def _loc_C3C(): pass

    label('loc_C3C')

    If(
        (
            (Expr.Eval, "OP_BA(0x00, 0x000A)"),
            Expr.Ez,
            (Expr.Eval, "OP_BA(0x01, 0x000A)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_BA(0x00, 0x0014)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_BA(0x01, 0x0014)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_BA(0x00, 0x001E)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_BA(0x01, 0x001E)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_BA(0x00, 0x0032)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_BA(0x01, 0x0032)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_BA(0x00, 0x0041)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_BA(0x01, 0x0041)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_E0F',
    )

    EventBegin(0x00)
    OP_92(0x0001, 0x0000, 800, 3000, 0x00)

    @scena.Lambda('lambda_0C9B')
    def lambda_0C9B():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0C9B)

    @scena.Lambda('lambda_0CA9')
    def lambda_0CA9():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0CA9)

    OP_69(0x000A, 1000)
    Sleep(400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CE1',
    )

    ChrTalk(
        0x0101,
        (
            '#0010000564V#002F又出现了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CE1(): pass

    label('loc_CE1')

    ChrTalk(
        0x0102,
        (
            '#0020000565V#012F这类敌人比较特殊，\n',
            '有时候武器对他们也不管用。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000566V#012F如果普通攻击不起作用的话，\n',
            '就用魔法来攻击他们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000567V#002F嗯，知道啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※结晶回路的安装在[Orbment]界面进行。\n',
            '  要开启[Orbment]界面\n',
            '  只需在Camp中点击[Orbment]即可。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    EventEnd(0x00)
    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    Return()

    def _loc_E0F(): pass

    label('loc_E0F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_E1B',
    )

    EventBegin(0x02)

    Jump('loc_100A')

    def _loc_E1B(): pass

    label('loc_E1B')

    EventBegin(0x00)
    OP_92(0x0001, 0x0000, 800, 3000, 0x00)

    @scena.Lambda('lambda_0E31')
    def lambda_0E31():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0E31)

    @scena.Lambda('lambda_0E3F')
    def lambda_0E3F():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0E3F)

    OP_69(0x000A, 1000)
    Sleep(400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E77',
    )

    ChrTalk(
        0x0101,
        (
            '#0010000568V#002F又出现了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E77(): pass

    label('loc_E77')

    ChrTalk(
        0x0102,
        (
            '#0020000569V#012F这类敌人比较特殊，\n',
            '有时候武器对他们也不管用。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000570V#012F不光要用普通攻击来对付它们，\n',
            '还要用魔法才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000571V#005F好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※在普通攻击很难对敌人起效的情况下，魔法就很有效。\n',
            '魔法还可以远距离攻击，\n',
            '但发动魔法需要耗费一定时间（驱动时间）。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※使用魔法会消耗ＥＰ。\n',
            '  ＥＰ可以通过在酒店、旅馆等回复点休息，\n',
            '  或使用ＥＰ填充剂等回复物品来进行回复。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    def _loc_100A(): pass

    label('loc_100A')

    @scena.Lambda('lambda_1010')
    def lambda_1010():
        OP_92(0x0000, 0x000A, 500, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_1010)

    @scena.Lambda('lambda_1025')
    def lambda_1025():
        OP_92(0x0001, 0x000A, 800, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_1025)

    Sleep(200)

    Battle(0x00000012, 0x0010000B, 0x00, 0x0000, 0x0A)
    EventEnd(0x02)
    SetMapFlags(0x00000001)

    Return()

# id: 0x0007 offset: 0x104E
@scena.Code('func_07_104E')
def func_07_104E():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_1056',
    )

    Return()

    def _loc_1056(): pass

    label('loc_1056')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_105E',
    )

    Return()

    def _loc_105E(): pass

    label('loc_105E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_106A',
    )

    EventBegin(0x02)

    Jump('loc_11AE')

    def _loc_106A(): pass

    label('loc_106A')

    EventBegin(0x00)
    ClearMapFlags(0x00000001)
    OP_92(0x0001, 0x0000, 800, 3000, 0x00)

    @scena.Lambda('lambda_1085')
    def lambda_1085():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1085)

    @scena.Lambda('lambda_1093')
    def lambda_1093():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1093)

    OP_69(0x000B, 1000)
    Sleep(400)

    ChrTalk(
        0x0102,
        (
            '#0020000572V#012F艾丝蒂尔，\n',
            '这次我们来使用战技吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000573V战技除了攻击之外，\n',
            '还会有其他很多效果。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000574V#005F嗯，明白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※战技虽有范围限制，但可以即时发动。\n',
            '  使用战技所必需的ＣＰ会在\n',
            '  攻击敌人或被敌人攻击的时候自动积蓄起来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_11AE(): pass

    label('loc_11AE')

    @scena.Lambda('lambda_11B4')
    def lambda_11B4():
        OP_92(0x0101, 0x000B, 500, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_11B4)

    @scena.Lambda('lambda_11C9')
    def lambda_11C9():
        OP_92(0x0102, 0x000B, 800, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_11C9)

    Sleep(200)

    Battle(0x00000013, 0x0010000B, 0x00, 0x0000, 0x0B)
    EventEnd(0x02)
    SetMapFlags(0x00000001)

    Return()

# id: 0x0008 offset: 0x11F2
@scena.Code('func_08_11F2')
def func_08_11F2():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_11FA',
    )

    Return()

    def _loc_11FA(): pass

    label('loc_11FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_1202',
    )

    Return()

    def _loc_1202(): pass

    label('loc_1202')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_120E',
    )

    EventBegin(0x02)

    Jump('loc_1429')

    def _loc_120E(): pass

    label('loc_120E')

    EventBegin(0x00)
    ClearMapFlags(0x00000001)
    OP_92(0x0001, 0x0000, 800, 3000, 0x00)

    @scena.Lambda('lambda_1229')
    def lambda_1229():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1229)

    @scena.Lambda('lambda_1237')
    def lambda_1237():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1237)

    OP_69(0x000C, 1000)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010000575V#509F好讨厌～\n',
            '怎么还有啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000576V#509F真麻烦～\n',
            '快点把它们解决掉吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000577V#012F如果使用Ｓ战技或Ｓ爆发技，\n',
            '我想只需一击就能打倒这些魔兽。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000578V#012F不过，要注意的是一定要在\n',
            'ＣＰ值为１００以上的时候才能使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※ＣＰ超过１００后，\n',
            '  就能使用攻击力强劲的战技，\n',
            '  分别是Ｓ战技以及最强的Ｓ爆发技。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※Ｓ爆发技即无视ＡＴ（行动顺序）而直接发动Ｓ战技。\n',
            '  作为Ｓ爆发技发动的Ｓ战技，\n',
            '  可以在Camp的[Tactics]-[Ｓ爆发技登记]中变更。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_1429(): pass

    label('loc_1429')

    @scena.Lambda('lambda_142F')
    def lambda_142F():
        OP_92(0x0000, 0x000C, 500, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_142F)

    @scena.Lambda('lambda_1444')
    def lambda_1444():
        OP_92(0x0001, 0x000C, 800, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_1444)

    Sleep(200)

    Battle(0x00000010, 0x0010000B, 0x00, 0x0000, 0x0C)
    EventEnd(0x02)
    SetMapFlags(0x00000001)

    Return()

# id: 0x0009 offset: 0x146D
@scena.Code('func_09_146D')
def func_09_146D():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_1475',
    )

    Return()

    def _loc_1475(): pass

    label('loc_1475')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_147D',
    )

    Return()

    def _loc_147D(): pass

    label('loc_147D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1489',
    )

    EventBegin(0x02)

    Jump('loc_16B4')

    def _loc_1489(): pass

    label('loc_1489')

    EventBegin(0x00)
    ClearMapFlags(0x00000001)
    OP_92(0x0001, 0x0000, 800, 3000, 0x00)

    @scena.Lambda('lambda_14A4')
    def lambda_14A4():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_14A4)

    @scena.Lambda('lambda_14B2')
    def lambda_14B2():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_14B2)

    CameraMove(-28300, 0, 54500, 1000)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010000579V#000F那就是目标宝箱啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000580V#000F如果研修就到此为止的话，\n',
            '那也太轻松太简单了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000581V#010F看来已经开始得心应手了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000582V#010F那么这次注意一下\n',
            '战斗行动顺序的应用吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000583V#010F掌握好的话\n',
            '会有各种各样的好处哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※战斗中，随着ＡＴ（行动顺序）的不同，\n',
            '  角色有机会得到『攻击力上升』、『得到耀晶片』等各种ＡＴ奖励。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※这些ＡＴ奖励对敌我双方都发挥同样的效果。\n',
            '  熟练错开行动顺序的话，\n',
            '  更可以强行夺取敌人的ＡＴ奖励为己用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_16B4(): pass

    label('loc_16B4')

    @scena.Lambda('lambda_16BA')
    def lambda_16BA():
        OP_92(0x0000, 0x000D, 500, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_16BA)

    @scena.Lambda('lambda_16CF')
    def lambda_16CF():
        OP_92(0x0001, 0x000D, 800, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_16CF)

    Sleep(200)

    Battle(0x0000000F, 0x0010000B, 0x00, 0x0000, 0x0D)
    EventEnd(0x02)
    SetMapFlags(0x00000001)

    Return()

# id: 0x000A offset: 0x16F8
@scena.Code('func_0A_16F8')
def func_0A_16F8():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0051, 2, 0x28A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1B5E',
    )

    EventBegin(0x00)
    ClearMapFlags(0x00000001)
    OP_92(0x0001, 0x0000, 800, 3000, 0x00)
    ChrTurnDirectionByPos(0x0000, -28000, 57000, 0)
    ChrTurnDirectionByPos(0x0001, -28000, 57000, 0)

    ExecExpressionWithValue(
        0x0008,
        0x01,
        (
            (Expr.GetChrWork, 0x102, 0x1),
            (Expr.GetChrWork, 0x101, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x02,
        (
            (Expr.GetChrWork, 0x102, 0x2),
            (Expr.GetChrWork, 0x101, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x03,
        (
            (Expr.GetChrWork, 0x102, 0x3),
            (Expr.GetChrWork, 0x101, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x0008, 1500)
    OP_28(0x000A, 0x01, 0x0002)
    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了２个',
            (TxtCtl.SetColor, 0x2),
            '小箱子',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    AddItem(0x0373, 2)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0101,
        (
            '#0010000587V#505F咦～奇怪了，\n',
            '怎么宝箱里还是箱子啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000588V#501F奇怪的是有两个箱子呢。\n',
            '嗯～到底里面放了些什么东西呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000589V#014F艾丝蒂尔，\n',
            '这次的任务是搜索和回收哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000590V#014F我想这其中应该不包括调查吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000591V#502F哎呀～\n',
            '约修亚你真是死脑筋。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000592V#502F这又不是工作的问题，\n',
            '只不过是纯粹的好奇心嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000593V#502F……………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000594V#006F……我说，既然这里没有人，\n',
            '稍微打开看一下也不会露馅吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000595V#014F……………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000596V#015F要是你想考试不合格的话，\n',
            '那我也不阻止你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000597V#580F不、不合格？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000598V#010F有这种可能性啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000599V#010F如果这是真正的工作，\n',
            '那这箱子就是委托人的物品。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000600V#010F如果不是非法物品，\n',
            '我们就无权调查里面的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000601V#007F啊，这样说也有道理……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020000602V#019F既然你这么在意，\n',
            '就等考试结束后去问一下雪拉姐姐吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000603V#010F……好了，就这样决定吧。\n',
            '回去的路上也要小心谨慎一点哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000604V#006FＯＫ！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0051, 2, 0x28A))
    Sleep(30)

    EventEnd(0x00)

    Jump('loc_1B99')

    def _loc_1B5E(): pass

    label('loc_1B5E')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱里什么东西都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    TalkEnd(0x00FF)
    Sleep(30)

    def _loc_1B99(): pass

    label('loc_1B99')

    ClearMapFlags(0x08000000)

    Return()

# id: 0x000B offset: 0x1B9F
@scena.Code('func_0B_1B9F')
def func_0B_1B9F():
    SetMapFlags(0x08000000)
    EventBegin(0x00)
    StopEffect(0x06, 0x00)
    OP_84(0x06)
    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '结晶回路的碎片',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    Sleep(400)

    AddItem(0x0325, 1)
    OP_64(0x05, 0x0001)

    If(
        (
            (Expr.Eval, "OP_29(0x0004, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1DEB',
    )

    ChrTalk(
        0x0101,
        (
            '#0010150054V#000F哦～原来是这个啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150055V从排水沟那里看到的光\n',
            '好像就是这东西发出来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020150056V#010F好像是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150057V原来是结晶回路的碎片啊……\n',
            '怪不得会发光呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010150058V#000F真是好美的光啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150059V这也是用七耀石制成的东西吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150060V#010F虽然这种说法比较粗略，\n',
            '不过也没说错……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150061V详细的说明\n',
            '回去再慢慢告诉你吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150062V一直站在这里说话，\n',
            '感觉可不太舒服。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150063V#004F嗯，对啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010150064V这里的确是挺阴森森的，\n',
            '我们快点回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0004, 0x01, 0x0020)

    Jump('loc_1DF1')

    def _loc_1DEB(): pass

    label('loc_1DEB')

    OP_28(0x0004, 0x01, 0x8000)

    def _loc_1DF1(): pass

    label('loc_1DF1')

    EventEnd(0x00)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x000C offset: 0x1DF9
@scena.Code('func_0C_1DF9')
def func_0C_1DF9():
    If(
        (
            (Expr.Eval, "OP_29(0x000A, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_1E05',
    )

    Return()

    def _loc_1E05(): pass

    label('loc_1E05')

    EventBegin(0x00)
    OP_28(0x000A, 0x01, 0x8000)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1EA1',
    )

    ChrTurnDirection(0x0102, 0x0101, 0)
    Sleep(100)

    ChrTalk(
        0x0102,
        (
            '#0020000549V#010F那边好像有一个\n',
            '专门用来休息的回复点。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000550V如果ＨＰ和ＥＰ降低了，就到那儿休息吧。\n',
            '特别是在战斗之前。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F17')

    def _loc_1EA1(): pass

    label('loc_1EA1')

    ChrTurnDirection(0x0102, 0x0101, 0)
    Sleep(100)

    ChrTalk(
        0x0102,
        (
            '#0020000551V#010F艾丝蒂尔，等一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000552V那边有一个回复点，\n',
            '如果ＨＰ和ＥＰ降低了，就到那儿休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F17(): pass

    label('loc_1F17')

    Sleep(100)

    @scena.Lambda('lambda_1F22')
    def lambda_1F22():
        SetChrDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_1F22)

    @scena.Lambda('lambda_1F30')
    def lambda_1F30():
        SetChrDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_1F30)

    CameraMove(13300, 0, -130, 1500)
    ChrTurnDirection(0x0102, 0x0101, 0)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※回复点是一种\n',
            '  配置在危险地域中的导力回复装置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※靠近回复点会出现『！』的标记，\n',
            '  用右键点击会出现选择菜单。\n',
            '  选择『休息』即可让全员的ＨＰ、ＥＰ完全回复。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    Sleep(100)

    OP_69(0x0000, 1500)

    ChrTalk(
        0x0101,
        (
            '#0010000553V#000F嗯，明白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)

    Return()

# id: 0x000D offset: 0x203B
@scena.Code('func_0D_203B')
def func_0D_203B():
    If(
        (
            (Expr.Eval, "OP_29(0x000A, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_2047',
    )

    Return()

    def _loc_2047(): pass

    label('loc_2047')

    EventBegin(0x00)
    OP_28(0x000A, 0x01, 0x8000)
    SetChrDirection(0x0102, 90, 0)
    Sleep(100)

    ChrTalk(
        0x0102,
        (
            '#0020000546V#010F那边好像有一个\n',
            '专门用来休息的回复点。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000547V如果ＨＰ和ＥＰ降低了，就到那儿休息吧。\n',
            '特别是在战斗之前。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    @scena.Lambda('lambda_20DF')
    def lambda_20DF():
        SetChrDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_20DF)

    @scena.Lambda('lambda_20ED')
    def lambda_20ED():
        SetChrDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_20ED)

    CameraMove(13300, 0, -130, 1500)
    ChrTurnDirection(0x0102, 0x0101, 0)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※回复点是一种\n',
            '  配置在危险地域中的导力回复装置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※靠近回复点会出现『！』的标记，\n',
            '  用右键点击会出现选择菜单。\n',
            '  选择『休息』即可让全员的ＨＰ、ＥＰ完全回复。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    Sleep(100)

    OP_69(0x0000, 1500)

    ChrTalk(
        0x0101,
        (
            '#0010000548V#000F嗯，明白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)

    Return()

# id: 0x000E offset: 0x21F8
@scena.Code('func_0E_21F8')
def func_0E_21F8():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0051, 3, 0x28B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_22E2',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01FC, 1)"),
            Expr.Return,
        ),
        'loc_226C',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '复苏药',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0051, 3, 0x28B))

    Jump('loc_22DF')

    def _loc_226C(): pass

    label('loc_226C')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '复苏药',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '复苏药',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0)

    def _loc_22DF(): pass

    label('loc_22DF')

    Jump('loc_231A')

    def _loc_22E2(): pass

    label('loc_22E2')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱里什么东西都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    WaitEffect(0x0F, 0x08)
    def _loc_231A(): pass

    label('loc_231A')

    TalkEnd(0x00FF)
    Sleep(30)

    ClearMapFlags(0x08000000)

    Return()

# id: 0x000F offset: 0x2328
@scena.Code('func_0F_2328')
def func_0F_2328():
    OP_28(0x000A, 0x01, 0x8000)
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
            TXT(0x00, '在此休息\n'),
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
        'loc_2547',
    )

    FadeIn(100, 0)
    Sleep(500)

    OP_26(13)
    StopEffect(0x00, 0x02)
    PlayEffect(0x00, 0x02, 0x00FF, 15800, 1000, -160, 0, 0, 0, 700, 700, 700, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0003, 0)
    OP_70(0x0003, 50)
    OP_73(0x0003)
    OP_20(0x00000BB8)
    PlaySE(12, 0x00, 0x64)
    StopEffect(0x02, 0x02)
    LoadEffect(0x01, 'map\\\\mp027_01.eff')
    PlayEffect(0x01, 0x01, 0x00FF, 15800, 1000, -160, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    FadeOut(1000, 0, -1)
    Sleep(700)

    PlaySE(13, 0x00, 0x64)
    OP_0D()
    SetChrStatus(0x0000, 0xFE, 0)
    SetChrStatus(0x0001, 0xFE, 0)
    SetChrStatus(0x0002, 0xFE, 0)
    SetChrStatus(0x0003, 0xFE, 0)
    SetChrStatus(0x0004, 0xFE, 0)
    SetChrStatus(0x0005, 0xFE, 0)
    SetChrStatus(0x0006, 0xFE, 0)
    SetChrStatus(0x0007, 0xFE, 0)
    SetChrPos(0x0000, 14290, 0, -230, 92)
    SetChrPos(0x0001, 14290, 0, -230, 92)
    SetChrPos(0x0002, 14290, 0, -230, 92)
    SetChrPos(0x0003, 14290, 0, -230, 92)
    OP_69(0x0000, 0)
    OP_30(0x00)
    Sleep(3500)

    StopEffect(0x01, 0x02)
    LoadEffect(0x00, 'map\\\\mp027_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, 15800, 1000, -160, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0003, 0)
    OP_1E()
    FadeIn(1000, 0)
    OP_56(0x00)
    TalkEnd(0x00FF)

    Return()

    def _loc_2547(): pass

    label('loc_2547')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2561',
    )

    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

    def _loc_2561(): pass

    label('loc_2561')

    Return()

# id: 0x0010 offset: 0x2562
@scena.Code('func_10_2562')
def func_10_2562():
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)

    ExecExpressionWithValue(
        0x0101,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0102,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrSubChip(0x0101, 0)
    SetChrSubChip(0x0102, 0)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import R2202_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R2202   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '扎古'),
    TXT(0x02, '基库'),
    TXT(0x03, '目标用摄像机'),
    TXT(0x04, ''),
    TXT(0x05, '卷尾蟾蜍'),
    TXT(0x06, '卷尾蟾蜍'),
    TXT(0x07, '卢安方向'),
    TXT(0x08, '街景林道'),
    TXT(0x09, '玛诺利亚村方向'),
    TXT(0x0A, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'R2202.x'
    header.mapIndex       = 101
    header.bgm            = 20
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/R2202._SN', 'ED6_DT01/R2202_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1D45
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
            word_3A         = 101,
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
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
        ('ED6_DT07/CH02320._CH', 'ED6_DT07/CH02320P._CP'),
        ('ED6_DT07/CH00045._CH', 'ED6_DT07/CH00045P._CP'),
        ('ED6_DT09/CH10460._CH', 'ED6_DT09/CH10460P._CP'),
        ('ED6_DT09/CH10461._CH', 'ED6_DT09/CH10461P._CP'),
        ('ED6_DT09/CH10160._CH', 'ED6_DT09/CH10160P._CP'),
        ('ED6_DT09/CH10161._CH', 'ED6_DT09/CH10161P._CP'),
        ('ED6_DT09/CH10450._CH', 'ED6_DT09/CH10450P._CP'),
        ('ED6_DT09/CH10451._CH', 'ED6_DT09/CH10451P._CP'),
        ('ED6_DT09/CH10220._CH', 'ED6_DT09/CH10220P._CP'),
        ('ED6_DT09/CH10221._CH', 'ED6_DT09/CH10221P._CP'),
        ('ED6_DT09/CH10480._CH', 'ED6_DT09/CH10480P._CP'),
        ('ED6_DT09/CH10481._CH', 'ED6_DT09/CH10481P._CP'),
        ('ED6_DT09/CH10470._CH', 'ED6_DT09/CH10470P._CP'),
        ('ED6_DT09/CH10471._CH', 'ED6_DT09/CH10471P._CP'),
        ('ED6_DT09/CH11060._CH', 'ED6_DT09/CH11060P._CP'),
        ('ED6_DT09/CH11061._CH', 'ED6_DT09/CH11061P._CP'),
        ('ED6_DT09/CH11240._CH', 'ED6_DT09/CH11240P._CP'),
        ('ED6_DT09/CH11241._CH', 'ED6_DT09/CH11241P._CP'),
    ]

# id: 0x10002 offset: 0x142
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -7120,
            z                   = 0,
            y                   = 37380,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 800,
            z                   = 6130,
            y                   = -13810,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x01C5,
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
            npcIndex            = 0x0180,
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
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 137430,
            z                   = -2000,
            y                   = -152480,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 137430,
            z                   = -2000,
            y                   = -152480,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 146110,
            z                   = -2000,
            y                   = -272220,
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
        ScenaNpcData(
            x                   = 195320,
            z                   = -2000,
            y                   = -200020,
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
        ScenaNpcData(
            x                   = 117860,
            z                   = -1990,
            y                   = -86810,
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

# id: 0x10003 offset: 0x262
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = 108600,
            z           = -2090,
            y           = -127120,
            word_0C     = 0x00B4,
            word_0E     = 0x0003,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0185,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 127020,
            z           = -2029,
            y           = -168530,
            word_0C     = 0x00B4,
            word_0E     = 0x0009,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0186,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 131400,
            z           = -1930,
            y           = -226630,
            word_0C     = 0x00B4,
            word_0E     = 0x0005,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0181,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 113340,
            z           = -6030,
            y           = -111320,
            word_0C     = 0x00B4,
            word_0E     = 0x000D,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0190,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 118080,
            z           = -6670,
            y           = -145340,
            word_0C     = 0x0000,
            word_0E     = 0x0011,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x05DE,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 108600,
            z           = -2090,
            y           = -127120,
            word_0C     = 0x00B4,
            word_0E     = 0x0003,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0329,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 127020,
            z           = -2029,
            y           = -168530,
            word_0C     = 0x00B4,
            word_0E     = 0x0009,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x032A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 131400,
            z           = -1930,
            y           = -226630,
            word_0C     = 0x00B4,
            word_0E     = 0x0005,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0325,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 113340,
            z           = -6030,
            y           = -111320,
            word_0C     = 0x00B4,
            word_0E     = 0x000D,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0334,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 118080,
            z           = -6670,
            y           = -145340,
            word_0C     = 0x0000,
            word_0E     = 0x0011,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x05DF,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x37A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 143910,
            y           = 1000,
            z           = -192310,
            range       = 140270,
            dword_10    = 0xFFFFF448,
            dword_14    = 0xFFFCE4CE,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000003,
        ),
        ScenaEventData(
            x           = 144550,
            y           = 1000,
            z           = -193950,
            range       = 134900,
            dword_10    = 0xFFFFF448,
            dword_14    = 0xFFFD00EE,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000004,
        ),
        ScenaEventData(
            x           = 171570,
            y           = -3000,
            z           = -204390,
            range       = 173310,
            dword_10    = 0x000003E8,
            dword_14    = 0xFFFD053A,
            dword_18    = 0x00010000,
            dword_1C    = 0x00000001,
        ),
        ScenaEventData(
            x           = 140060,
            y           = -4000,
            z           = -151030,
            range       = 134200,
            dword_10    = 0x00000000,
            dword_14    = 0xFFFDA602,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000007,
        ),
    )

# id: 0x10005 offset: 0x3FA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 111300,
            triggerZ            = -6040,
            triggerY            = -229080,
            triggerRange        = 1400,
            actorX              = 111300,
            actorZ              = -5040,
            actorY              = -229080,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0000,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 145130,
            triggerZ            = -2029,
            triggerY            = -194770,
            triggerRange        = 1500,
            actorX              = 145130,
            actorZ              = -500,
            actorY              = -194770,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 143160,
            triggerZ            = -1960,
            triggerY            = -203990,
            triggerRange        = 1500,
            actorX              = 143160,
            actorZ              = -550,
            actorY              = -203990,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 123800,
            triggerZ            = -6110,
            triggerY            = -164160,
            triggerRange        = 1000,
            actorX              = 123890,
            actorZ              = -6040,
            actorY              = -164820,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 110610,
            triggerZ            = -2050,
            triggerY            = -169010,
            triggerRange        = 1000,
            actorX              = 111270,
            actorZ              = -1960,
            actorY              = -169020,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 114670,
            triggerZ            = -6010,
            triggerY            = -111030,
            triggerRange        = 1000,
            actorX              = 115310,
            actorZ              = -5950,
            actorY              = -111030,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x4D2
@scena.Code('PreInit')
def PreInit():
    ExecExpressionWithReg(
        0x0001,
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0009,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0001 offset: 0x4F0
@scena.Code('Init')
def Init():
    OP_16(0x02, 4000, 10000, -311000, 196648)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_51A',
    )

    OP_B1('R2202_y')

    Jump('loc_523')

    def _loc_51A(): pass

    label('loc_51A')

    OP_B1('R2202_n')

    def _loc_523(): pass

    label('loc_523')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_54B',
    )

    SetChrFlags(0x0011, 0x0080)
    SetChrFlags(0x0012, 0x0080)
    SetChrFlags(0x0013, 0x0080)
    SetChrFlags(0x0014, 0x0080)
    SetChrFlags(0x0015, 0x0080)

    Jump('loc_564')

    def _loc_54B(): pass

    label('loc_54B')

    SetChrFlags(0x0016, 0x0080)
    SetChrFlags(0x0017, 0x0080)
    SetChrFlags(0x0018, 0x0080)
    SetChrFlags(0x0019, 0x0080)
    SetChrFlags(0x001A, 0x0080)

    def _loc_564(): pass

    label('loc_564')

    If(
        (
            (Expr.Eval, "OP_29(0x001E, 0x01, 0x0010)"),
            (Expr.Eval, "OP_29(0x001E, 0x01, 0x4000)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_57B',
    )

    OP_64(0x00, 0x0001)

    def _loc_57B(): pass

    label('loc_57B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0097, 7, 0x4BF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_58D',
    )

    OP_6F(0x0001, 0)

    Jump('loc_594')

    def _loc_58D(): pass

    label('loc_58D')

    OP_6F(0x0001, 60)

    def _loc_594(): pass

    label('loc_594')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0098, 0, 0x4C0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5A6',
    )

    OP_6F(0x0002, 0)

    Jump('loc_5AD')

    def _loc_5A6(): pass

    label('loc_5A6')

    OP_6F(0x0002, 60)

    def _loc_5AD(): pass

    label('loc_5AD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0098, 1, 0x4C1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5BF',
    )

    OP_6F(0x0003, 0)

    Jump('loc_5C6')

    def _loc_5BF(): pass

    label('loc_5BF')

    OP_6F(0x0003, 60)

    def _loc_5C6(): pass

    label('loc_5C6')

    OP_B2(0x00, 0x03, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0098, 6, 0x4C6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5DD',
    )

    ClearChrFlags(0x000C, 0x0080)
    OP_B2(0x01, 0x03, 0x0080)

    def _loc_5DD(): pass

    label('loc_5DD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_5F6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0098, 7, 0x4C7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5F6',
    )

    ClearChrFlags(0x000D, 0x0080)
    OP_B2(0x01, 0x03, 0x0080)

    def _loc_5F6(): pass

    label('loc_5F6')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_60D',
    )

    SetChrFlags(0x0015, 0x0080)
    SetChrFlags(0x001A, 0x0080)

    def _loc_60D(): pass

    label('loc_60D')

    PlaySE(456, 0x01, 0x64)

    ExecExpressionWithVar(
        0x2A,
        (
            (Expr.PushLong, 0x1900),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0002 offset: 0x61D
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_632',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_632(): pass

    label('loc_632')

    Return()

# id: 0x0003 offset: 0x633
@scena.Code('func_03_633')
def func_03_633():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 5, 0x435)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_F4D',
    )

    SetScenaFlags(ScenaFlag(0x0086, 5, 0x435))
    OP_28(0x003E, 0x04, 0x02)
    OP_28(0x003E, 0x04, 0x04)
    OP_28(0x003E, 0x01, 0x0001)
    OP_28(0x001C, 0x04, 0x40)
    OP_28(0x0020, 0x04, 0x40)

    If(
        (
            (Expr.Eval, "OP_40(0x0334)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_66A',
    )

    OP_28(0x0021, 0x04, 0x40)

    def _loc_66A(): pass

    label('loc_66A')

    If(
        (
            (Expr.Eval, "OP_29(0x001E, 0x00, 0x04)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_67A',
    )

    OP_28(0x001E, 0x04, 0x40)

    def _loc_67A(): pass

    label('loc_67A')

    OP_28(0x0026, 0x04, 0x40)
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    Fade(1000)
    CameraMove(140150, -2000, -197420, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0105, 140170, -2000, -197360, 180)
    SetChrPos(0x0101, 140900, -2000, -198500, 0)
    SetChrPos(0x0102, 139540, -2000, -198900, 0)
    OP_0D()

    ChrTalk(
        0x0102,
        (
            '#0020060957V#010F好了，就在这里分手吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060060958V#047F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060060959V#048F这几天承蒙你们的帮忙，\n',
            '真是太感谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060960V#001F啊哈哈，别客气啦。\n',
            '而且我们两个也玩得很开心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010060961V#006F那么……\n',
            '替我们向特蕾莎院长他们问好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060060962V#041F嗯，我一定会转告的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x0008, 138530, -2000, -188460, 0)

    NpcTalk(
        0x0008,
        '青年的声音',
        (
            '#1500060963V#4P啊，是你们啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0847')
    def lambda_0847():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_0847')

    DispatchAsync2(0x0105, 0x0001, lambda_0847)

    @scena.Lambda('lambda_0858')
    def lambda_0858():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_0858')

    DispatchAsync2(0x0101, 0x0001, lambda_0858)

    @scena.Lambda('lambda_0869')
    def lambda_0869():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_0869')

    DispatchAsync2(0x0102, 0x0001, lambda_0869)

    ClearChrFlags(0x0008, 0x0080)
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrWalkTo(0x0008, 138910, -2000, -197360, 5000, 0x00)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0105, 0xFF)

    ChrTalk(
        0x0101,
        (
            '#0010060964V#004F咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020060965V#014F您是……\n',
            '玛诺利亚村的村民吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1500060966V#1P真的是你们啊！\n',
            '两位游击士！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1500060967V#1P大、大事不好了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060968V#002F大事不好……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)

    ChrTalk(
        0x0008,
        (
            '#1500060969V#1P哈啊哈啊哈啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1500060970V#1P稍、稍等一会儿。\n',
            '让、让我喘口气……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1500060971V#1P呼～呼～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1500060972V#1P…………………呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    PlayBGM(86)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#1500060973V#1P……特蕾莎老师和孩子们，\n',
            '在玛诺利亚附近被人袭击了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010060974V#005F什、什么～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060060975V#049F#1P………………啊………',
            TxtCtl.Enter,
        ),
    )

    OP_9E(0x0105, 30, 0, 400, 5000)
    CloseMessageWindow()

    @scena.Lambda('lambda_0AF4')
    def lambda_0AF4():
        OP_94(0x01, 0x0105, 0x00B4, 0x000001F4, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0002, lambda_0AF4)

    WaitForThreadExit(0x0105, 0x0002)
    Fade(500)
    SetChrChipByIndex(0x0105, 2)
    OP_0D()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0105, 400)

    @scena.Lambda('lambda_0B3D')
    def lambda_0B3D():
        OP_92(0x00FE, 0x0105, 600, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0B3D)

    ChrTurnDirection(0x0102, 0x0105, 400)
    ChrTurnDirection(0x0008, 0x0105, 400)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010060976V#004F你、你还好吧！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020060977V#012F……振作点。\n',
            '现在可不是倒下的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060060978V#047F#1P对、对不起……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x0105, 65535)
    OP_0D()
    OP_94(0x01, 0x0105, 0x0000, 0x000001F4, 0x000003E8, 0x00)
    ChrTurnDirection(0x0101, 0x0008, 400)
    ChrTurnDirection(0x0102, 0x0008, 400)

    ChrTalk(
        0x0105,
        (
            '#0060060979V#043F#1P拜托了……\n',
            '请告诉我们详细情形好吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1500060980V啊，好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1500060981V他们是在从王立学院回来的路上，\n',
            '被一群奇怪的家伙袭击的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1500060982V孩子们都没受伤，\n',
            '不过特蕾莎老师还有\n',
            '护送的游击士大姐都晕过去了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060983V#004F哎？卡露娜姐姐也！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020060984V#012F看来犯人很不简单……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060060985V#049F#1P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1500060986V本来想通知你们协会的，\n',
            '但旅店的通信器似乎坏了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1500060987V情急之下，\n',
            '我就只好急忙跑过来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020060988V#015F是这样吗……\n',
            '多谢您的紧急协助。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060989V#012F不过，如果可以的话，\n',
            '可以麻烦您去一趟卢安吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020060990V因为我们要马上赶去玛诺利亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0008, 180, 400)

    ChrTalk(
        0x0008,
        (
            '#1500060991V#1P好，知道了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0E7E')
    def lambda_0E7E():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_0E7E')

    DispatchAsync2(0x0105, 0x0001, lambda_0E7E)

    @scena.Lambda('lambda_0E8F')
    def lambda_0E8F():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_0E8F')

    DispatchAsync2(0x0101, 0x0001, lambda_0E8F)

    @scena.Lambda('lambda_0EA0')
    def lambda_0EA0():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_0EA0')

    DispatchAsync2(0x0102, 0x0001, lambda_0EA0)

    ChrWalkTo(0x0008, 136840, -2000, -203480, 5000, 0x00)
    SetChrFlags(0x0008, 0x0080)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0105, 0xFF)
    ChrTurnDirection(0x0102, 0x0105, 400)

    ChrTalk(
        0x0102,
        (
            '#0020060992V#012F好了，我们也快点吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010060993V#002F嗯、嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060060994V#042F#1P……………好的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000003E8)
    EventEnd(0x00)
    OP_21()
    PlayBGM(20)

    def _loc_F4D(): pass

    label('loc_F4D')

    Return()

# id: 0x0004 offset: 0xF4E
@scena.Code('func_04_F4E')
def func_04_F4E():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 6, 0x43E)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_13B1',
    )

    SetScenaFlags(ScenaFlag(0x0087, 6, 0x43E))
    EventBegin(0x00)
    FadeOut(500, 0, -1)
    OP_0D()
    CameraMove(139070, -2000, -192040, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2990, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 138410, -2009, -190790, 180)
    SetChrPos(0x0102, 139470, -2029, -190120, 180)
    SetChrPos(0x0105, 138400, -2009, -189000, 180)
    FadeIn(500, 0)

    @scena.Lambda('lambda_0FE9')
    def lambda_0FE9():
        CameraMove(139620, -2000, -195740, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0FE9)

    @scena.Lambda('lambda_1001')
    def lambda_1001():
        ChrWalkTo(0x00FE, 139240, -2000, -196860, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1001)

    @scena.Lambda('lambda_101C')
    def lambda_101C():
        ChrWalkTo(0x00FE, 140440, -2000, -196200, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_101C)

    @scena.Lambda('lambda_1037')
    def lambda_1037():
        ChrWalkTo(0x00FE, 139650, -2000, -194870, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_1037)

    WaitForThreadExit(0x0105, 0x0001)

    ChrTalk(
        0x0105,
        (
            '#0060061386V#043F……那个…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0105, 400)
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010061387V#004F科洛丝，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061388V#040F那个……\n',
            '艾丝蒂尔你们先去协会可以吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060061389V我想起有件事要办，\n',
            '所以想暂时离开一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060061390V很快就会追上你们的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061391V#014F我们倒没关系……\n',
            '你是要先回学院吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061392V#045F是、是的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060061393V我想先把事情\n',
            '向校长也汇报一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061394V#006F这样啊……\n',
            '嗯，我明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010061395V我们在协会等你！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0101, 180, 400)

    @scena.Lambda('lambda_11F5')
    def lambda_11F5():
        ChrWalkTo(0x00FE, 136730, -2000, -204400, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_11F5)

    SetChrDirection(0x0102, 180, 400)

    @scena.Lambda('lambda_1217')
    def lambda_1217():
        ChrWalkTo(0x00FE, 137660, -2000, -204180, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1217)

    WaitForThreadExit(0x0102, 0x0001)
    ChrSetRGBAMask(0x0101, 255, 255, 255, 0, 100)
    ChrSetRGBAMask(0x0102, 255, 255, 255, 0, 100)
    OP_69(0x0105, 1000)

    ChrTalk(
        0x0105,
        (
            '#0060061396V#049F#2P对不起……\n',
            '艾丝蒂尔、约修亚。',
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
            '科洛丝取出了身上的笔记本和笔，\n',
            '写下了几行字。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0105,
        (
            '#0060061397V#047F#2P嗯，这就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_12FC')
    def lambda_12FC():
        CameraMove(135220, -2040, -194820, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_12FC)

    SetChrDirection(0x0105, 270, 400)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0105,
        (
            '#0060061398V#042F#4P……基库！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, 121590, 7000, -203340, 90)
    PlaySE(140, 0x00, 0x64)
    OP_92(0x0009, 0x0105, 5000, 10000, 0x00)
    OP_92(0x0009, 0x0105, 4000, 8000, 0x00)
    OP_92(0x0009, 0x0105, 3000, 6000, 0x00)
    FadeOut(1000, 0, -1)
    OP_92(0x0009, 0x0105, 2000, 3000, 0x00)
    OP_92(0x0009, 0x0105, 1000, 1500, 0x00)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T2120._SN', 105, 0, 0)
    IdleLoop()

    def _loc_13B1(): pass

    label('loc_13B1')

    Return()

# id: 0x0005 offset: 0x13B2
@scena.Code('func_05_13B2')
def func_05_13B2():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '东　杰尼丝王立学院　２５２塞尔矩',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0006 offset: 0x1405
@scena.Code('func_06_1405')
def func_06_1405():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '南　卢安市\n',
            '北　玛诺利亚村　　　３１２塞尔矩',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0007 offset: 0x1463
@scena.Code('func_07_1463')
def func_07_1463():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_146F',
    )

    Call(0, 0x0008)

    Return()

    def _loc_146F(): pass

    label('loc_146F')

    EventBegin(0x01)

    ExecExpressionWithValue(
        0x0000,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0001,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0002,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0003,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0004,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0005,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0006,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0007,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrSubChip(0x0000, 0)
    SetChrSubChip(0x0001, 0)
    SetChrSubChip(0x0002, 0)
    SetChrSubChip(0x0003, 0)
    SetChrSubChip(0x0004, 0)
    SetChrSubChip(0x0005, 0)
    SetChrSubChip(0x0006, 0)
    SetChrSubChip(0x0007, 0)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '大型魔兽正在四处游荡中。',
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
        0,
        (
            TXT(0x00, '【消灭它】\n'),
            TXT(0x01, '【放弃】\n'),
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
        (0x00000001, 'loc_1554'),
        (-1, 'loc_1570'),
    )

    def _loc_1554(): pass

    label('loc_1554')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

    def _loc_1570(): pass

    label('loc_1570')

    Battle(0x000003FB, 0x00000000, 0x00, 0x0000, 0xFF)
    SetChrPos(0x0000, 137350, -2000, -149140, 180)
    SetChrPos(0x0001, 137350, -2000, -149140, 180)
    SetChrPos(0x0002, 137350, -2000, -149140, 180)
    SetChrPos(0x0003, 137350, -2000, -149140, 180)
    SetChrPos(0x0004, 137350, -2000, -149140, 180)
    SetChrPos(0x0005, 137350, -2000, -149140, 180)
    SetChrPos(0x0006, 137350, -2000, -149140, 180)
    SetChrPos(0x0007, 137350, -2000, -149140, 180)
    OP_69(0x0000, 0)
    OP_30(0x00)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000002, 'loc_161E'),
        (0x00000001, 'loc_1621'),
        (-1, 'loc_1624'),
    )

    def _loc_161E(): pass

    label('loc_161E')

    EventEnd(0x00)

    Return()

    def _loc_1621(): pass

    label('loc_1621')

    OP_B4(0x00)

    Return()

    def _loc_1624(): pass

    label('loc_1624')

    EventBegin(0x01)
    SetChrFlags(0x000C, 0x0080)
    OP_B2(0x00, 0x03, 0x0080)
    OP_0D()
    Sleep(400)

    PlaySE(23, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '成功消灭了梅威海道中被通缉的魔兽！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetScenaFlags(ScenaFlag(0x0098, 6, 0x4C6))
    OP_28(0x0024, 0x04, 0x10)
    OP_28(0x0024, 0x01, 0x0001)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x00)

    Return()

# id: 0x0008 offset: 0x169D
@scena.Code('func_08_169D')
def func_08_169D():
    EventBegin(0x01)

    ExecExpressionWithValue(
        0x0000,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0001,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0002,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0003,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0004,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0005,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0006,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0007,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrSubChip(0x0000, 0)
    SetChrSubChip(0x0001, 0)
    SetChrSubChip(0x0002, 0)
    SetChrSubChip(0x0003, 0)
    SetChrSubChip(0x0004, 0)
    SetChrSubChip(0x0005, 0)
    SetChrSubChip(0x0006, 0)
    SetChrSubChip(0x0007, 0)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '大型魔兽正在四处游荡中。',
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
        0,
        (
            TXT(0x00, '【消灭它】\n'),
            TXT(0x01, '【放弃】\n'),
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
        (0x00000001, 'loc_1782'),
        (-1, 'loc_179E'),
    )

    def _loc_1782(): pass

    label('loc_1782')

    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

    def _loc_179E(): pass

    label('loc_179E')

    Battle(0x000003FC, 0x00000000, 0x00, 0x0000, 0xFF)
    SetChrPos(0x0000, 137310, -2000, -155800, 0)
    SetChrPos(0x0001, 137310, -2000, -155800, 0)
    SetChrPos(0x0002, 137310, -2000, -155800, 0)
    SetChrPos(0x0003, 137310, -2000, -155800, 0)
    SetChrPos(0x0004, 137310, -2000, -155800, 0)
    SetChrPos(0x0005, 137310, -2000, -155800, 0)
    SetChrPos(0x0006, 137310, -2000, -155800, 0)
    SetChrPos(0x0007, 137310, -2000, -155800, 0)
    OP_69(0x0000, 0)
    OP_30(0x00)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000002, 'loc_184C'),
        (0x00000001, 'loc_184F'),
        (-1, 'loc_1852'),
    )

    def _loc_184C(): pass

    label('loc_184C')

    EventEnd(0x00)

    Return()

    def _loc_184F(): pass

    label('loc_184F')

    OP_B4(0x00)

    Return()

    def _loc_1852(): pass

    label('loc_1852')

    EventBegin(0x01)
    SetChrFlags(0x000D, 0x0080)
    OP_B2(0x00, 0x03, 0x0080)
    OP_0D()
    Sleep(400)

    PlaySE(23, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '成功消灭了梅威海道中被通缉的魔兽②！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetScenaFlags(ScenaFlag(0x0098, 7, 0x4C7))
    OP_28(0x0025, 0x04, 0x10)
    OP_28(0x0025, 0x01, 0x0001)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x00)

    Return()

# id: 0x0009 offset: 0x18CD
@scena.Code('func_09_18CD')
def func_09_18CD():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0097, 7, 0x4BF)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_19B7',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01F5, 1)"),
            Expr.Return,
        ),
        'loc_1941',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    FadeIn(300, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '回复药',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    SetScenaFlags(ScenaFlag(0x0097, 7, 0x4BF))

    Jump('loc_19B4')

    def _loc_1941(): pass

    label('loc_1941')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '回复药',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '回复药',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0)

    def _loc_19B4(): pass

    label('loc_19B4')

    Jump('loc_19ED')

    def _loc_19B7(): pass

    label('loc_19B7')

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
    WaitEffect(0x0F, 0x88)
    def _loc_19ED(): pass

    label('loc_19ED')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x000A offset: 0x19FB
@scena.Code('func_0A_19FB')
def func_0A_19FB():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0098, 0, 0x4C0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1AE5',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01F5, 1)"),
            Expr.Return,
        ),
        'loc_1A6F',
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
            '回复药',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0098, 0, 0x4C0))

    Jump('loc_1AE2')

    def _loc_1A6F(): pass

    label('loc_1A6F')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '回复药',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '回复药',
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

    def _loc_1AE2(): pass

    label('loc_1AE2')

    Jump('loc_1B1B')

    def _loc_1AE5(): pass

    label('loc_1AE5')

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
    WaitEffect(0x0F, 0x89)
    def _loc_1B1B(): pass

    label('loc_1B1B')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x000B offset: 0x1B29
@scena.Code('func_0B_1B29')
def func_0B_1B29():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0098, 1, 0x4C1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1CE9',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0003, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0098, 2, 0x4C2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C21',
    )

    ChrSetRGBAMask(0x000B, 255, 255, 255, 0, 0)
    SetChrPos(0x000B, 115310, -3500, -111030, 320)
    ChrTurnDirection(0x000B, 0x0000, 0)

    @scena.Lambda('lambda_1B78')
    def lambda_1B78():
        ChrMoveTo(0x00FE, 115310, -5000, -111030, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1B78)

    @scena.Lambda('lambda_1B93')
    def lambda_1B93():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1200)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_1B93)

    ClearChrFlags(0x000B, 0x0080)

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

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1BD6',
    )

    Battle(0x00000322, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_1BE3')

    def _loc_1BD6(): pass

    label('loc_1BD6')

    Battle(0x0000017E, 0x00000000, 0x00, 0x0000, 0xFF)

    def _loc_1BE3(): pass

    label('loc_1BE3')

    SetChrFlags(0x000B, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_1BFC'),
        (0x00000002, 'loc_1C0E'),
        (0x00000001, 'loc_1C1E'),
        (-1, 'loc_1C21'),
    )

    def _loc_1BFC(): pass

    label('loc_1BFC')

    SetScenaFlags(ScenaFlag(0x0098, 2, 0x4C2))
    OP_6F(0x0003, 60)
    Sleep(500)

    Jump('loc_1C21')

    def _loc_1C0E(): pass

    label('loc_1C0E')

    OP_6F(0x0003, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

    def _loc_1C1E(): pass

    label('loc_1C1E')

    OP_B4(0x00)

    Return()

    def _loc_1C21(): pass

    label('loc_1C21')

    If(
        (
            (Expr.Eval, "AddItem(0x00F9, 1)"),
            Expr.Return,
        ),
        'loc_1C75',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '战斗服',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0098, 1, 0x4C1))

    Jump('loc_1CE6')

    def _loc_1C75(): pass

    label('loc_1C75')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '战斗服',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '战斗服',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0003, 60)
    OP_70(0x0003, 0)

    def _loc_1CE6(): pass

    label('loc_1CE6')

    Jump('loc_1D1F')

    def _loc_1CE9(): pass

    label('loc_1CE9')

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
    WaitEffect(0x0F, 0x8A)
    def _loc_1D1F(): pass

    label('loc_1D1F')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

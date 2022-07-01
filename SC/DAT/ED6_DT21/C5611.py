import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5611_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5611   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '卡露娜'),
    TXT(0x02, '哨兵570'),
    TXT(0x03, '哨兵570'),
    TXT(0x04, ''),
    TXT(0x05, ''),
    TXT(0x06, ''),
    TXT(0x07, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5611.x'
    header.mapIndex       = 1
    header.bgm            = 61
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x24F8
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
        ('ED6_DT07/CH01240._CH', 'ED6_DT07/CH01240P._CP'),
        ('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT27/CH04001._CH', 'ED6_DT27/CH04001P._CP'),
        ('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP'),
        ('ED6_DT07/CH00121._CH', 'ED6_DT07/CH00121P._CP'),
        ('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP'),
        ('ED6_DT07/CH00151._CH', 'ED6_DT07/CH00151P._CP'),
        ('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP'),
        ('ED6_DT07/CH00131._CH', 'ED6_DT07/CH00131P._CP'),
        ('ED6_DT07/CH00140._CH', 'ED6_DT07/CH00140P._CP'),
        ('ED6_DT07/CH00141._CH', 'ED6_DT07/CH00141P._CP'),
        ('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP'),
        ('ED6_DT07/CH00161._CH', 'ED6_DT07/CH00161P._CP'),
        ('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP'),
        ('ED6_DT07/CH00171._CH', 'ED6_DT07/CH00171P._CP'),
        ('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP'),
        ('ED6_DT27/CH04081._CH', 'ED6_DT27/CH04081P._CP'),
        ('ED6_DT26/CH20405._CH', 'ED6_DT26/CH20405P._CP'),
        ('ED6_DT27/CH03084._CH', 'ED6_DT27/CH03084P._CP'),
        ('ED6_DT07/CH00400._CH', 'ED6_DT07/CH00400P._CP'),
        ('ED6_DT26/CH20373._CH', 'ED6_DT26/CH20373P._CP'),
        ('ED6_DT07/CH00401._CH', 'ED6_DT07/CH00401P._CP'),
    ]

# id: 0x10002 offset: 0x1AA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
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
    )

# id: 0x10003 offset: 0x20A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = 75020,
            z           = 0,
            y           = 90910,
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
            x           = 86930,
            z           = 0,
            y           = -61050,
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
            x           = -145090,
            z           = 0,
            y           = -59140,
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

# id: 0x10004 offset: 0x25E
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 18990,
            y           = -1000,
            z           = 151320,
            range       = 3000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000019,
        ),
        ScenaEventData(
            x           = 30960,
            y           = -1000,
            z           = 151350,
            range       = 3000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x0000001A,
        ),
    )

# id: 0x10005 offset: 0x29E
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -19300,
            triggerZ            = 0,
            triggerY            = 145970,
            triggerRange        = 1000,
            actorX              = -20000,
            actorZ              = 0,
            actorY              = 145970,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -140290,
            triggerZ            = 0,
            triggerY            = -59010,
            triggerRange        = 1000,
            actorX              = -141000,
            actorZ              = 0,
            actorY              = -59010,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -135290,
            triggerZ            = 0,
            triggerY            = 18060,
            triggerRange        = 1000,
            actorX              = -136000,
            actorZ              = 0,
            actorY              = 17970,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 70300,
            triggerZ            = 0,
            triggerY            = 95020,
            triggerRange        = 1000,
            actorX              = 70960,
            actorZ              = 0,
            actorY              = 95020,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 74300,
            triggerZ            = 0,
            triggerY            = 4460,
            triggerRange        = 1000,
            actorX              = 75000,
            actorZ              = 0,
            actorY              = 4550,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 82300,
            triggerZ            = 0,
            triggerY            = -57020,
            triggerRange        = 1000,
            actorX              = 83010,
            actorZ              = 0,
            actorY              = -57020,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -49710,
            triggerZ            = 0,
            triggerY            = 32470,
            triggerRange        = 1000,
            actorX              = -49050,
            actorZ              = 0,
            actorY              = 32509,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -93050,
            triggerZ            = 0,
            triggerY            = 131020,
            triggerRange        = 800,
            actorX              = -93050,
            actorZ              = 1000,
            actorY              = 131020,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0016,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 23370,
            triggerZ            = 0,
            triggerY            = -6800,
            triggerRange        = 800,
            actorX              = 23370,
            actorZ              = 1100,
            actorY              = -6800,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -92840,
            triggerZ            = 0,
            triggerY            = -56890,
            triggerRange        = 800,
            actorX              = -92840,
            actorZ              = 1100,
            actorY              = -56890,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 32759,
            triggerZ            = 0,
            triggerY            = 151710,
            triggerRange        = 800,
            actorX              = 32759,
            actorZ              = 1100,
            actorY              = 151710,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000C,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 14340,
            triggerZ            = 0,
            triggerY            = 146480,
            triggerRange        = 800,
            actorX              = 14340,
            actorZ              = 1100,
            actorY              = 146480,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000D,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -103760,
            triggerZ            = 0,
            triggerY            = 20520,
            triggerRange        = 800,
            actorX              = -103760,
            actorZ              = 1100,
            actorY              = 20520,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000E,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x472
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0381, 3, 0x1C0B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_48A',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x87),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_48A',
    )

    Event(0, 0x0010)

    def _loc_48A(): pass

    label('loc_48A')

    Return()

# id: 0x0001 offset: 0x48B
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x7F),
            Expr.Equ,
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x82),
            Expr.Equ,
            Expr.Or,
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x84),
            Expr.Equ,
            Expr.Or,
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x80),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_4BF',
    )

    OP_C4(0x00, 0x00000001)
    OP_78(0x00, 0x00, 0x00)

    Jump('loc_4C3')

    def _loc_4BF(): pass

    label('loc_4BF')

    OP_78(0x74, 0x6A, 0x7C)

    def _loc_4C3(): pass

    label('loc_4C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A2, 0, 0x1D10)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4D5',
    )

    OP_6F(0x0000, 0)

    Jump('loc_4DC')

    def _loc_4D5(): pass

    label('loc_4D5')

    OP_6F(0x0000, 60)

    def _loc_4DC(): pass

    label('loc_4DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A2, 2, 0x1D12)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4EE',
    )

    OP_6F(0x0001, 0)

    Jump('loc_4F5')

    def _loc_4EE(): pass

    label('loc_4EE')

    OP_6F(0x0001, 60)

    def _loc_4F5(): pass

    label('loc_4F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A2, 4, 0x1D14)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_507',
    )

    OP_6F(0x0002, 0)

    Jump('loc_50E')

    def _loc_507(): pass

    label('loc_507')

    OP_6F(0x0002, 60)

    def _loc_50E(): pass

    label('loc_50E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A2, 6, 0x1D16)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_520',
    )

    OP_6F(0x0003, 0)

    Jump('loc_527')

    def _loc_520(): pass

    label('loc_520')

    OP_6F(0x0003, 60)

    def _loc_527(): pass

    label('loc_527')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A2, 7, 0x1D17)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_539',
    )

    OP_6F(0x0004, 0)

    Jump('loc_540')

    def _loc_539(): pass

    label('loc_539')

    OP_6F(0x0004, 60)

    def _loc_540(): pass

    label('loc_540')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A3, 0, 0x1D18)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_552',
    )

    OP_6F(0x0005, 0)

    Jump('loc_559')

    def _loc_552(): pass

    label('loc_552')

    OP_6F(0x0005, 60)

    def _loc_559(): pass

    label('loc_559')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A3, 1, 0x1D19)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_56B',
    )

    OP_6F(0x0006, 0)

    Jump('loc_572')

    def _loc_56B(): pass

    label('loc_56B')

    OP_6F(0x0006, 60)

    def _loc_572(): pass

    label('loc_572')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0382, 3, 0x1C13)),
            Expr.Return,
        ),
        'loc_588',
    )

    OP_64(0x08, 0x0001)
    OP_10(0x0E, 0x01)
    OP_71(0x0011, 0x0010)

    Jump('loc_590')

    def _loc_588(): pass

    label('loc_588')

    OP_10(0x0E, 0x00)
    OP_72(0x0011, 0x0010)

    def _loc_590(): pass

    label('loc_590')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0382, 4, 0x1C14)),
            Expr.Return,
        ),
        'loc_5A6',
    )

    OP_64(0x09, 0x0001)
    OP_10(0x18, 0x01)
    OP_71(0x0013, 0x0010)

    Jump('loc_5AE')

    def _loc_5A6(): pass

    label('loc_5A6')

    OP_10(0x18, 0x00)
    OP_72(0x0013, 0x0010)

    def _loc_5AE(): pass

    label('loc_5AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0382, 5, 0x1C15)),
            Expr.Return,
        ),
        'loc_5C4',
    )

    OP_64(0x0A, 0x0001)
    OP_10(0x01, 0x01)
    OP_71(0x001A, 0x0010)

    Jump('loc_5CC')

    def _loc_5C4(): pass

    label('loc_5C4')

    OP_10(0x01, 0x00)
    OP_72(0x001A, 0x0010)

    def _loc_5CC(): pass

    label('loc_5CC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0382, 6, 0x1C16)),
            Expr.Return,
        ),
        'loc_5E2',
    )

    OP_64(0x0B, 0x0001)
    OP_10(0x02, 0x01)
    OP_71(0x0010, 0x0010)

    Jump('loc_5EA')

    def _loc_5E2(): pass

    label('loc_5E2')

    OP_10(0x02, 0x00)
    OP_72(0x0010, 0x0010)

    def _loc_5EA(): pass

    label('loc_5EA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0382, 7, 0x1C17)),
            Expr.Return,
        ),
        'loc_600',
    )

    OP_64(0x0C, 0x0001)
    OP_10(0x1E, 0x01)
    OP_71(0x0016, 0x0010)

    Jump('loc_608')

    def _loc_600(): pass

    label('loc_600')

    OP_10(0x1E, 0x00)
    OP_72(0x0016, 0x0010)

    def _loc_608(): pass

    label('loc_608')

    OP_74(0x0021, 0x00000000, 0x0000)

    Return()

# id: 0x0002 offset: 0x612
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_627',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('ReInit')

    def _loc_627(): pass

    label('loc_627')

    Return()

# id: 0x0003 offset: 0x628
@scena.Code('func_03_628')
def func_03_628():
    UnlockAchievement(0x02, 0xA4, 0x01, 0x00)
    SetMapFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A2, 0, 0x1D10)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6A6',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0000, 0x0000001E)
    OP_73(0x0000)
    OP_6F(0x0000, 30)
    AddSepith(0x03, 0x00C8)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#59I风之耀晶片×２００\n',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1D10)

    Jump('loc_6C0')

    def _loc_6A6(): pass

    label('loc_6A6')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_6C0(): pass

    label('loc_6C0')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x6D2
@scena.Code('func_04_6D2')
def func_04_6D2():
    UnlockAchievement(0x02, 0xA5, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A2, 2, 0x1D12)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7AF',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0001, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['兔跃靴'], 1)"),
            Expr.Return,
        ),
        'loc_746',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['兔跃靴']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1D12)

    Jump('loc_7AC')

    def _loc_746(): pass

    label('loc_746')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['兔跃靴']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['兔跃靴']),
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

    def _loc_7AC(): pass

    label('loc_7AC')

    Jump('loc_7E0')

    def _loc_7AF(): pass

    label('loc_7AF')

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
    def _loc_7E0(): pass

    label('loc_7E0')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x7EE
@scena.Code('func_05_7EE')
def func_05_7EE():
    UnlockAchievement(0x02, 0xA6, 0x01, 0x00)
    SetMapFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A2, 4, 0x1D14)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_86C',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0002, 0x0000001E)
    OP_73(0x0002)
    OP_6F(0x0002, 30)
    AddSepith(0x02, 0x00C8)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#58I火之耀晶片×２００\n',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1D14)

    Jump('loc_886')

    def _loc_86C(): pass

    label('loc_86C')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_886(): pass

    label('loc_886')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x898
@scena.Code('func_06_898')
def func_06_898():
    UnlockAchievement(0x02, 0xA7, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A2, 6, 0x1D16)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_975',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0003, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅰ'], 1)"),
            Expr.Return,
        ),
        'loc_90C',
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
    OP_A2(0x1D16)

    Jump('loc_972')

    def _loc_90C(): pass

    label('loc_90C')

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
    OP_6F(0x0003, 60)
    OP_70(0x0003, 0x00000000)

    def _loc_972(): pass

    label('loc_972')

    Jump('loc_9A6')

    def _loc_975(): pass

    label('loc_975')

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
    def _loc_9A6(): pass

    label('loc_9A6')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0x9B4
@scena.Code('func_07_9B4')
def func_07_9B4():
    UnlockAchievement(0x02, 0xA8, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A2, 7, 0x1D17)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A91',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0004, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['夜视眼镜'], 1)"),
            Expr.Return,
        ),
        'loc_A28',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['夜视眼镜']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1D17)

    Jump('loc_A8E')

    def _loc_A28(): pass

    label('loc_A28')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['夜视眼镜']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['夜视眼镜']),
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

    def _loc_A8E(): pass

    label('loc_A8E')

    Jump('loc_AC2')

    def _loc_A91(): pass

    label('loc_A91')

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
    def _loc_AC2(): pass

    label('loc_AC2')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0xAD0
@scena.Code('func_08_AD0')
def func_08_AD0():
    UnlockAchievement(0x02, 0xA9, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A3, 0, 0x1D18)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BAD',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0005, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['中回复药'], 1)"),
            Expr.Return,
        ),
        'loc_B44',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['中回复药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1D18)

    Jump('loc_BAA')

    def _loc_B44(): pass

    label('loc_B44')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['中回复药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['中回复药']),
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

    def _loc_BAA(): pass

    label('loc_BAA')

    Jump('loc_BDE')

    def _loc_BAD(): pass

    label('loc_BAD')

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
    def _loc_BDE(): pass

    label('loc_BDE')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0009 offset: 0xBEC
@scena.Code('func_09_BEC')
def func_09_BEC():
    UnlockAchievement(0x02, 0xAA, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03A3, 1, 0x1D19)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CC9',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0006, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['导力靴'], 1)"),
            Expr.Return,
        ),
        'loc_C60',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['导力靴']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1D19)

    Jump('loc_CC6')

    def _loc_C60(): pass

    label('loc_C60')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['导力靴']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['导力靴']),
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

    def _loc_CC6(): pass

    label('loc_CC6')

    Jump('loc_CFA')

    def _loc_CC9(): pass

    label('loc_CC9')

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
    def _loc_CFA(): pass

    label('loc_CFA')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x000A offset: 0xD08
@scena.Code('func_0A_D08')
def func_0A_D08():
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

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
    Call(0, 0x000F)

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D7C',
    )

    OP_22(0x009D, 0x00, 0x64)
    Sleep(1000)

    OP_6F(0x0011, 0)
    OP_70(0x0011, 0x0000001E)
    OP_73(0x0011)
    OP_64(0x08, 0x0001)
    OP_10(0x0E, 0x01)
    OP_A2(0x1C13)

    Jump('loc_DA0')

    def _loc_D7C(): pass

    label('loc_D7C')

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
        'loc_DA0',
    )

    OP_22(0x00AB, 0x00, 0x64)
    Sleep(1000)

    Jump('loc_DA0')

    def _loc_DA0(): pass

    label('loc_DA0')

    TalkEnd(0x00FF)

    Return()

# id: 0x000B offset: 0xDA4
@scena.Code('func_0B_DA4')
def func_0B_DA4():
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

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
    Call(0, 0x000F)

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_E18',
    )

    OP_22(0x009D, 0x00, 0x64)
    Sleep(1000)

    OP_6F(0x0013, 0)
    OP_70(0x0013, 0x0000001E)
    OP_73(0x0013)
    OP_64(0x09, 0x0001)
    OP_10(0x18, 0x01)
    OP_A2(0x1C14)

    Jump('loc_E3C')

    def _loc_E18(): pass

    label('loc_E18')

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
        'loc_E3C',
    )

    OP_22(0x00AB, 0x00, 0x64)
    Sleep(1000)

    Jump('loc_E3C')

    def _loc_E3C(): pass

    label('loc_E3C')

    TalkEnd(0x00FF)

    Return()

# id: 0x000C offset: 0xE40
@scena.Code('func_0C_E40')
def func_0C_E40():
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

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
    Call(0, 0x000F)

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_EB4',
    )

    OP_22(0x009D, 0x00, 0x64)
    Sleep(1000)

    OP_6F(0x001A, 0)
    OP_70(0x001A, 0x0000001E)
    OP_73(0x001A)
    OP_64(0x0A, 0x0001)
    OP_10(0x01, 0x01)
    OP_A2(0x1C15)

    Jump('loc_ED8')

    def _loc_EB4(): pass

    label('loc_EB4')

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
        'loc_ED8',
    )

    OP_22(0x00AB, 0x00, 0x64)
    Sleep(1000)

    Jump('loc_ED8')

    def _loc_ED8(): pass

    label('loc_ED8')

    TalkEnd(0x00FF)

    Return()

# id: 0x000D offset: 0xEDC
@scena.Code('func_0D_EDC')
def func_0D_EDC():
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

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
    Call(0, 0x000F)

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F50',
    )

    OP_22(0x009D, 0x00, 0x64)
    Sleep(1000)

    OP_6F(0x0010, 0)
    OP_70(0x0010, 0x0000001E)
    OP_73(0x0010)
    OP_64(0x0B, 0x0001)
    OP_10(0x02, 0x01)
    OP_A2(0x1C16)

    Jump('loc_F74')

    def _loc_F50(): pass

    label('loc_F50')

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
        'loc_F74',
    )

    OP_22(0x00AB, 0x00, 0x64)
    Sleep(1000)

    Jump('loc_F74')

    def _loc_F74(): pass

    label('loc_F74')

    TalkEnd(0x00FF)

    Return()

# id: 0x000E offset: 0xF78
@scena.Code('func_0E_F78')
def func_0E_F78():
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

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
    Call(0, 0x000F)

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_FEC',
    )

    OP_22(0x009D, 0x00, 0x64)
    Sleep(1000)

    OP_6F(0x0016, 0)
    OP_70(0x0016, 0x0000001E)
    OP_73(0x0016)
    OP_64(0x0C, 0x0001)
    OP_10(0x1E, 0x01)
    OP_A2(0x1C17)

    Jump('loc_1010')

    def _loc_FEC(): pass

    label('loc_FEC')

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
        'loc_1010',
    )

    OP_22(0x00AB, 0x00, 0x64)
    Sleep(1000)

    Jump('loc_1010')

    def _loc_1010(): pass

    label('loc_1010')

    TalkEnd(0x00FF)

    Return()

# id: 0x000F offset: 0x1014
@scena.Code('func_0F_1014')
def func_0F_1014():
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
        'loc_102F',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_102F(): pass

    label('loc_102F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0381, 4, 0x1C0C)),
            Expr.Return,
        ),
        'loc_1040',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x2),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_1040(): pass

    label('loc_1040')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0381, 6, 0x1C0E)),
            Expr.Return,
        ),
        'loc_1051',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x4),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_1051(): pass

    label('loc_1051')

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
        (0x00000000, 'loc_107D'),
        (0x00000001, 'loc_108A'),
        (0x00000003, 'loc_10E6'),
        (0x00000007, 'loc_1166'),
        (-1, 'loc_120A'),
    )

    def _loc_107D(): pass

    label('loc_107D')

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_120A')

    def _loc_108A(): pass

    label('loc_108A')

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
        (0x00000000, 'loc_10C9'),
        (0x00000001, 'loc_10D6'),
        (-1, 'loc_10E3'),
    )

    def _loc_10C9(): pass

    label('loc_10C9')

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_10E3')

    def _loc_10D6(): pass

    label('loc_10D6')

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_10E3')

    def _loc_10E3(): pass

    label('loc_10E3')

    Jump('loc_120A')

    def _loc_10E6(): pass

    label('loc_10E6')

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
        (0x00000000, 'loc_113C'),
        (0x00000001, 'loc_1149'),
        (0x00000002, 'loc_1156'),
        (-1, 'loc_1163'),
    )

    def _loc_113C(): pass

    label('loc_113C')

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1163')

    def _loc_1149(): pass

    label('loc_1149')

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1163')

    def _loc_1156(): pass

    label('loc_1156')

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1163')

    def _loc_1163(): pass

    label('loc_1163')

    Jump('loc_120A')

    def _loc_1166(): pass

    label('loc_1166')

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
        (0x00000000, 'loc_11D3'),
        (0x00000001, 'loc_11E0'),
        (0x00000002, 'loc_11ED'),
        (0x00000003, 'loc_11FA'),
        (-1, 'loc_1207'),
    )

    def _loc_11D3(): pass

    label('loc_11D3')

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1207')

    def _loc_11E0(): pass

    label('loc_11E0')

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1207')

    def _loc_11ED(): pass

    label('loc_11ED')

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1207')

    def _loc_11FA(): pass

    label('loc_11FA')

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1207')

    def _loc_1207(): pass

    label('loc_1207')

    Jump('loc_120A')

    def _loc_120A(): pass

    label('loc_120A')

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

# id: 0x0010 offset: 0x1222
@scena.Code('func_10_1222')
def func_10_1222():
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
        'loc_1239',
    )

    Call(0, 0x0017)
    Call(0, 0x0018)

    def _loc_1239(): pass

    label('loc_1239')

    SetChrChipByIndex(0x0008, 10)
    SetChrSubChip(0x0008, 0)
    SetChrPos(0x0008, -92720, 0, 128000, 0)
    SetChrPos(0x0008, -92720, 0, 127000, 0)
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0101, -92180, 20, 116110, 0)
    SetChrPos(0x0109, -93490, 20, 116110, 0)
    SetChrPos(0x00F8, -92180, 0, 114880, 0)
    SetChrPos(0x00F9, -93490, 0, 114830, 0)
    OP_6D(-93240, 20, 116200, 0)
    OP_67(0, 7620, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(315000, 0)
    OP_6E(271, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010321026V#1005F#6P啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_131E')
    def lambda_131E():
        OP_6D(-93030, 20, 123000, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_131E)

    @scena.Lambda('lambda_1336')
    def lambda_1336():
        OP_67(0, 5090, -10000, 2500)

        ExitThread()

    DispatchAsync(0x0109, 0x0002, lambda_1336)

    @scena.Lambda('lambda_134E')
    def lambda_134E():
        OP_6B(2610, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_134E)

    @scena.Lambda('lambda_135E')
    def lambda_135E():
        OP_6E(340, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_135E)

    Sleep(2000)

    @scena.Lambda('lambda_1373')
    def lambda_1373():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1373)

    Sleep(200)

    OP_22(0x00D8, 0x00, 0x64)
    SetChrChipByIndex(0x0008, 29)
    SetChrSubChip(0x0008, 0)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0320321233V#837F#2P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0101, 11)
    SetChrChipByIndex(0x0109, 25)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_13F1'),
        (0x00000005, 'loc_13F9'),
        (0x00000003, 'loc_1401'),
        (0x00000004, 'loc_1409'),
        (0x00000006, 'loc_1411'),
        (0x00000007, 'loc_1419'),
        (-1, 'loc_1421'),
    )

    def _loc_13F1(): pass

    label('loc_13F1')

    SetChrChipByIndex(0x00F8, 13)

    Jump('loc_1421')

    def _loc_13F9(): pass

    label('loc_13F9')

    SetChrChipByIndex(0x00F8, 15)

    Jump('loc_1421')

    def _loc_1401(): pass

    label('loc_1401')

    SetChrChipByIndex(0x00F8, 17)

    Jump('loc_1421')

    def _loc_1409(): pass

    label('loc_1409')

    SetChrChipByIndex(0x00F8, 19)

    Jump('loc_1421')

    def _loc_1411(): pass

    label('loc_1411')

    SetChrChipByIndex(0x00F8, 21)

    Jump('loc_1421')

    def _loc_1419(): pass

    label('loc_1419')

    SetChrChipByIndex(0x00F8, 23)

    Jump('loc_1421')

    def _loc_1421(): pass

    label('loc_1421')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_1442'),
        (0x00000005, 'loc_144A'),
        (0x00000003, 'loc_1452'),
        (0x00000004, 'loc_145A'),
        (0x00000006, 'loc_1462'),
        (0x00000007, 'loc_146A'),
        (-1, 'loc_1472'),
    )

    def _loc_1442(): pass

    label('loc_1442')

    SetChrChipByIndex(0x00F9, 13)

    Jump('loc_1472')

    def _loc_144A(): pass

    label('loc_144A')

    SetChrChipByIndex(0x00F9, 15)

    Jump('loc_1472')

    def _loc_1452(): pass

    label('loc_1452')

    SetChrChipByIndex(0x00F9, 17)

    Jump('loc_1472')

    def _loc_145A(): pass

    label('loc_145A')

    SetChrChipByIndex(0x00F9, 19)

    Jump('loc_1472')

    def _loc_1462(): pass

    label('loc_1462')

    SetChrChipByIndex(0x00F9, 21)

    Jump('loc_1472')

    def _loc_146A(): pass

    label('loc_146A')

    SetChrChipByIndex(0x00F9, 23)

    Jump('loc_1472')

    def _loc_1472(): pass

    label('loc_1472')

    @scena.Lambda('lambda_1478')
    def lambda_1478():
        OP_91(0x00FE, 0, 0, 3500, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1478)

    Sleep(60)

    @scena.Lambda('lambda_1498')
    def lambda_1498():
        OP_91(0x00FE, 0, 0, 3500, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_1498)

    Sleep(100)

    @scena.Lambda('lambda_14B8')
    def lambda_14B8():
        OP_91(0x00FE, 0, 0, 3500, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_14B8)

    Sleep(70)

    @scena.Lambda('lambda_14D8')
    def lambda_14D8():
        OP_91(0x00FE, 0, 0, 3500, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_14D8)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010321234V#1002F#6P果然卡露娜前辈也……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1560',
    )

    ChrTalk(
        0x0106,
        (
            '#0050321235V#057F#6P可恶，只能拚了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1603')

    def _loc_1560(): pass

    label('loc_1560')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1599',
    )

    ChrTalk(
        0x0103,
        (
            '#0030321236V#022F#6P只能拚了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1603')

    def _loc_1599(): pass

    label('loc_1599')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_15D6',
    )

    ChrTalk(
        0x0108,
        (
            '#0080321237V#072F#6P看来只能拚了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1603')

    def _loc_15D6(): pass

    label('loc_15D6')

    ChrTalk(
        0x0109,
        (
            '#0180321238V#1063F#6P看来只能拚了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1603(): pass

    label('loc_1603')

    Sleep(200)

    CreateThread(0x0009, 0x00, 0x00, 0x0013)
    Sleep(200)

    CreateThread(0x000A, 0x00, 0x00, 0x0014)
    Sleep(1000)

    @scena.Lambda('lambda_1626')
    def lambda_1626():
        OP_6D(-93220, 20, 124000, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1626)

    @scena.Lambda('lambda_163E')
    def lambda_163E():
        OP_6B(2130, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_163E)

    CreateThread(0x0101, 0x00, 0x00, 0x0011)
    CreateThread(0x0008, 0x00, 0x00, 0x0012)
    Sleep(300)

    TerminateThread(0x0008, 0x01)
    TerminateThread(0x0008, 0x02)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0109, 0xFF)
    TerminateThread(0x00F8, 0xFF)
    TerminateThread(0x00F9, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    Battle(0x0000041F, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_1694'),
        (-1, 'loc_1699'),
    )

    def _loc_1694(): pass

    label('loc_1694')

    OP_B4(0x00)

    Jump('loc_1699')

    def _loc_1699(): pass

    label('loc_1699')

    Call(0, 0x0015)

    Return()

# id: 0x0011 offset: 0x169E
@scena.Code('func_11_169E')
def func_11_169E():
    SetChrChipByIndex(0x0101, 12)
    SetChrChipByIndex(0x0109, 26)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_16C9'),
        (0x00000005, 'loc_16D1'),
        (0x00000003, 'loc_16D9'),
        (0x00000004, 'loc_16E1'),
        (0x00000006, 'loc_16E9'),
        (0x00000007, 'loc_16F1'),
        (-1, 'loc_16F9'),
    )

    def _loc_16C9(): pass

    label('loc_16C9')

    SetChrChipByIndex(0x00F8, 14)

    Jump('loc_16F9')

    def _loc_16D1(): pass

    label('loc_16D1')

    SetChrChipByIndex(0x00F8, 16)

    Jump('loc_16F9')

    def _loc_16D9(): pass

    label('loc_16D9')

    SetChrChipByIndex(0x00F8, 18)

    Jump('loc_16F9')

    def _loc_16E1(): pass

    label('loc_16E1')

    SetChrChipByIndex(0x00F8, 20)

    Jump('loc_16F9')

    def _loc_16E9(): pass

    label('loc_16E9')

    SetChrChipByIndex(0x00F8, 22)

    Jump('loc_16F9')

    def _loc_16F1(): pass

    label('loc_16F1')

    SetChrChipByIndex(0x00F8, 24)

    Jump('loc_16F9')

    def _loc_16F9(): pass

    label('loc_16F9')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_171A'),
        (0x00000005, 'loc_1722'),
        (0x00000003, 'loc_172A'),
        (0x00000004, 'loc_1732'),
        (0x00000006, 'loc_173A'),
        (0x00000007, 'loc_1742'),
        (-1, 'loc_174A'),
    )

    def _loc_171A(): pass

    label('loc_171A')

    SetChrChipByIndex(0x00F9, 14)

    Jump('loc_174A')

    def _loc_1722(): pass

    label('loc_1722')

    SetChrChipByIndex(0x00F9, 16)

    Jump('loc_174A')

    def _loc_172A(): pass

    label('loc_172A')

    SetChrChipByIndex(0x00F9, 18)

    Jump('loc_174A')

    def _loc_1732(): pass

    label('loc_1732')

    SetChrChipByIndex(0x00F9, 20)

    Jump('loc_174A')

    def _loc_173A(): pass

    label('loc_173A')

    SetChrChipByIndex(0x00F9, 22)

    Jump('loc_174A')

    def _loc_1742(): pass

    label('loc_1742')

    SetChrChipByIndex(0x00F9, 24)

    Jump('loc_174A')

    def _loc_174A(): pass

    label('loc_174A')

    SetChrFlags(0x0101, 0x1000)

    @scena.Lambda('lambda_1755')
    def lambda_1755():
        OP_91(0x00FE, 0, 0, 3500, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1755)

    Sleep(50)

    SetChrFlags(0x0109, 0x1000)

    @scena.Lambda('lambda_177A')
    def lambda_177A():
        OP_91(0x00FE, 0, 0, 3500, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_177A)

    Sleep(50)

    SetChrFlags(0x00F8, 0x1000)

    @scena.Lambda('lambda_179F')
    def lambda_179F():
        OP_91(0x00FE, 0, 0, 3500, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_179F)

    Sleep(50)

    SetChrFlags(0x00F9, 0x1000)

    @scena.Lambda('lambda_17C4')
    def lambda_17C4():
        OP_91(0x00FE, 0, 0, 3500, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_17C4)

    Return()

# id: 0x0012 offset: 0x17DA
@scena.Code('func_12_17DA')
def func_12_17DA():
    SetChrChipByIndex(0x0008, 31)

    @scena.Lambda('lambda_17E5')
    def lambda_17E5():
        OP_91(0x00FE, 0, 0, -4000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_17E5)

    Sleep(50)

    SetChrChipByIndex(0x0009, 1)

    @scena.Lambda('lambda_180A')
    def lambda_180A():
        OP_91(0x00FE, 0, 0, -4000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_180A)

    Sleep(50)

    SetChrChipByIndex(0x000A, 1)

    @scena.Lambda('lambda_182F')
    def lambda_182F():
        OP_91(0x00FE, 0, 0, -4000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_182F)

    Return()

# id: 0x0013 offset: 0x1845
@scena.Code('func_13_1845')
def func_13_1845():
    CreateThread(0x00FE, 0x03, 0x00, 0x0002)
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    SetChrFlags(0x00FE, 0x0004)
    SetChrPos(0x00FE, -91180, 1200, 128710, 180)
    ClearChrFlags(0x00FE, 0x0080)
    OP_22(0x0211, 0x00, 0x64)
    OP_22(0x0215, 0x00, 0x64)

    @scena.Lambda('lambda_1882')
    def lambda_1882():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1882)

    OP_8F(0x00FE, -91180, 0, 128710, 2000, 0x00)

    Return()

# id: 0x0014 offset: 0x18A3
@scena.Code('func_14_18A3')
def func_14_18A3():
    CreateThread(0x00FE, 0x03, 0x00, 0x0002)
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    SetChrFlags(0x00FE, 0x0004)
    SetChrPos(0x00FE, -94460, 1200, 128720, 180)
    ClearChrFlags(0x00FE, 0x0080)
    OP_22(0x0211, 0x00, 0x64)
    OP_22(0x0215, 0x00, 0x64)

    @scena.Lambda('lambda_18E0')
    def lambda_18E0():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_18E0)

    OP_8F(0x00FE, -94460, 0, 128720, 2000, 0x00)

    Return()

# id: 0x0015 offset: 0x1901
@scena.Code('func_15_1901')
def func_15_1901():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_0D()
    TerminateThread(0x0008, 0x00)
    TerminateThread(0x0008, 0x01)
    TerminateThread(0x0008, 0x02)
    TerminateThread(0x0008, 0x03)
    TerminateThread(0x0101, 0x00)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0109, 0x01)
    TerminateThread(0x00F8, 0x01)
    TerminateThread(0x00F9, 0x01)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrChipByIndex(0x0101, 65535)
    SetChrSubChip(0x0101, 0)
    SetChrChipByIndex(0x0109, 65535)
    SetChrSubChip(0x0109, 0)
    SetChrChipByIndex(0x00F8, 65535)
    SetChrSubChip(0x00F8, 0)
    SetChrChipByIndex(0x00F9, 65535)
    SetChrSubChip(0x00F9, 0)
    SetChrPos(0x0008, -92930, 20, 125700, 180)
    SetChrChipByIndex(0x0008, 27)
    SetChrSubChip(0x0008, 0)
    SetChrPos(0x0101, -92200, 20, 122860, 0)
    SetChrPos(0x0109, -93290, 20, 122860, 0)
    SetChrPos(0x00F8, -92200, 20, 121500, 0)
    SetChrPos(0x00F9, -93290, 20, 121500, 0)
    ClearChrFlags(0x0101, 0x1000)
    ClearChrFlags(0x0109, 0x1000)
    ClearChrFlags(0x00F8, 0x1000)
    ClearChrFlags(0x00F9, 0x1000)
    OP_6D(-93520, 20, 124240, 0)
    OP_67(0, 5700, -10000, 0)
    OP_6B(2840, 0)
    OP_6C(315000, 0)
    OP_6E(273, 0)
    FadeIn(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010321239V#1007F#6P果、果然是\n',
            '一场苦战……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180321240V#1060F#6P好，该我出场了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1A86')
    def lambda_1A86():
        OP_6D(-93520, 20, 125240, 1500)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_1A86)

    OP_8E(0x0109, -92900, 20, 123900, 1500, 0x00)
    WaitForThreadExit(0x0109, 0x0001)
    Fade(500)
    SetChrChipByIndex(0x0109, 30)
    SetChrSubChip(0x0109, 0)
    Sleep(500)

    OP_22(0x00D8, 0x00, 0x64)
    SetChrSubChip(0x0109, 1)
    Sleep(1000)

    LoadEffect(0x00, 'scraft\\\\sc008_02.eff')
    PlayEffect(0x00, 0xFF, 0x0109, 300, 1100, 500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(2000)

    LoadEffect(0x00, 'scraft\\\\sc001_05.eff')
    PlayEffect(0x00, 0xFF, 0x0008, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1500)

    OP_9E(0x0008, 0x00000014, 0x00000000, 0x000001F4, 0x00000BB8)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0320321241V#836F#2P唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    SetChrSubChip(0x0008, 1)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0320321242V#835F#2P你、你们……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320321243V竟然能跑到\n',
            '这种地方来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    SetChrChipByIndex(0x0109, 65535)
    OP_0D()

    @scena.Lambda('lambda_1C20')
    def lambda_1C20():
        OP_8F(0x0109, -93290, 20, 122860, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_1C20)

    ChrTalk(
        0x0101,
        (
            '#0010321244V#1020F#6P卡露娜前辈，你没事吧！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0320321245V#833F#2P啊啊……不要紧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320321246V#832F话说回来……\n',
            '找到其它人了吗？',
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
        'loc_1D29',
    )

    ChrTalk(
        0x0103,
        (
            '#0030321247V#020F#6P刚才把库拉茨\n',
            '救出来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030321248V#025F亚妮拉丝还没……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DEE')

    def _loc_1D29(): pass

    label('loc_1D29')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1D90',
    )

    ChrTalk(
        0x0106,
        (
            '#0050321249V#051F#6P刚才把库拉茨\n',
            '救出来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050321250V#053F还没找到亚妮拉丝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DEE')

    def _loc_1D90(): pass

    label('loc_1D90')

    ChrTalk(
        0x0101,
        (
            '#0010321251V#1006F#6P刚刚才把库拉茨\n',
            '前辈救出来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010321252V#1007F亚妮拉丝还没有……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1DEE(): pass

    label('loc_1DEE')

    ChrTalk(
        0x0008,
        (
            '#0320321253V#833F#2P是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320321254V#832F没有碰上那些\n',
            '『执行者』吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010321255V#1002F#6P没有，倒是跟那些\n',
            '人形兵器战斗了好几次……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010321256V这里好像完全\n',
            '没有人的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0320321257V#834F#2P好奇怪……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320321258V其它士兵和研究员\n',
            '应该还有几十人才对……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320321259V#833F或许已经……\n',
            '撤退了也说不定。',
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
        'loc_1F97',
    )

    ChrTalk(
        0x0108,
        (
            '#0080321260V#074F#6P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080321261V#070F虽然不可大意，\n',
            '但也有这个可能。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2014')

    def _loc_1F97(): pass

    label('loc_1F97')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1FD8',
    )

    ChrTalk(
        0x0105,
        (
            '#0060321262V#043F#6P这个可能性似乎很高……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2014')

    def _loc_1FD8(): pass

    label('loc_1FD8')

    ChrTalk(
        0x0101,
        (
            '#0010321265V#1015F#6P原来如此……\n',
            '这个可能性应该不低。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2014(): pass

    label('loc_2014')

    ChrTalk(
        0x0008,
        (
            '#0320321263V#835F#2P我可以想办法\n',
            '一个人逃出去……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0320321264V至于亚妮拉丝……\n',
            '请你们尽快找到她。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010321266V#1006F#6P嗯……交给我们吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1C0B)
    OP_28(0x0098, 0x01, 0x0040)
    OP_9E(0x0008, 0x00000014, 0x00000000, 0x0000012C, 0x00000BB8)
    Fade(500)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 10)
    OP_0D()
    Sleep(1000)

    @scena.Lambda('lambda_20E0')
    def lambda_20E0():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_20E0')

    DispatchAsync2(0x0101, 0x0001, lambda_20E0)

    @scena.Lambda('lambda_20F1')
    def lambda_20F1():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_20F1')

    DispatchAsync2(0x0109, 0x0001, lambda_20F1)

    @scena.Lambda('lambda_2102')
    def lambda_2102():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_2102')

    DispatchAsync2(0x00F8, 0x0001, lambda_2102)

    @scena.Lambda('lambda_2113')
    def lambda_2113():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_2113')

    DispatchAsync2(0x00F9, 0x0001, lambda_2113)

    @scena.Lambda('lambda_2124')
    def lambda_2124():
        OP_6D(-93050, 20, 118350, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2124)

    OP_8E(0x0008, -90640, 20, 123350, 2000, 0x00)

    @scena.Lambda('lambda_2150')
    def lambda_2150():
        OP_9E(0x00FE, 0x00000014, 0x00000000, 0x000003E8, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2150)

    OP_8E(0x0008, -90280, 0, 119950, 2500, 0x00)

    @scena.Lambda('lambda_217E')
    def lambda_217E():
        OP_9E(0x00FE, 0x00000014, 0x00000000, 0x000003E8, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_217E)

    OP_8E(0x0008, -92520, 0, 115560, 2000, 0x00)

    @scena.Lambda('lambda_21AC')
    def lambda_21AC():
        OP_9E(0x00FE, 0x00000014, 0x00000000, 0x000003E8, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_21AC)

    OP_8E(0x0008, -92990, 0, 113260, 2500, 0x00)

    @scena.Lambda('lambda_21DA')
    def lambda_21DA():
        OP_8E(0x00FE, -92750, 0, 112600, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_21DA)

    OP_9F(0x0008, 0xFF, 0xFF, 0xFF, 0x00, 0x000001F4)
    WaitForThreadExit(0x0008, 0x0001)
    SetChrFlags(0x0008, 0x0080)
    Sleep(1000)

    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0109, 0x01)
    TerminateThread(0x00F8, 0x01)
    TerminateThread(0x00F9, 0x01)
    WaitForThreadExit(0x0101, 0x0000)

    @scena.Lambda('lambda_2224')
    def lambda_2224():
        OP_6D(-93110, 20, 122720, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2224)

    WaitForThreadExit(0x0101, 0x0000)
    EventEnd(0x00)

    Return()

# id: 0x0016 offset: 0x223E
@scena.Code('func_16_223E')
def func_16_223E():
    EventBegin(0x00)
    OP_22(0x009C, 0x00, 0x64)
    Sleep(500)

    OP_22(0x009D, 0x00, 0x64)
    OP_74(0x0021, 0x00000000, 0x0003)
    SetMessageWindowPos(-1, -1, 24, 5)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S『对战斗员的处置』\n',
            ' \n',
            '对于从各地的猎兵团等处\n',
            '临时确保的战斗员，\n',
            '应该施予以下的处置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_74(0x0021, 0x00000000, 0x0004)
    SetMessageWindowPos(-1, -1, 24, 5)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '#1S①身体能力强化程序\n',
            '②战斗技术学习程序\n',
            '③命令系统植入程序\n',
            '④机密保持暗示程序（※以下删除）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0381, 4, 0x1C0C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2396',
    )

    Sleep(500)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['绿色密码卡']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['绿色密码卡'], 1)
    Sleep(500)

    def _loc_2396(): pass

    label('loc_2396')

    OP_A2(0x1C0C)
    OP_28(0x0098, 0x01, 0x0080)
    OP_74(0x0021, 0x00000000, 0x0000)
    OP_22(0x009C, 0x00, 0x64)
    Sleep(500)

    EventEnd(0x01)

    Return()

# id: 0x0017 offset: 0x23B5
@scena.Code('func_17_23B5')
def func_17_23B5():
    FadeOut(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
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
        (0x00000000, 'loc_2432'),
        (0x00000001, 'loc_2438'),
        (-1, 'loc_243E'),
    )

    def _loc_2432(): pass

    label('loc_2432')

    OP_A2(0x1200)

    Jump('loc_243E')

    def _loc_2438(): pass

    label('loc_2438')

    OP_A2(0x1201)

    Jump('loc_243E')

    def _loc_243E(): pass

    label('loc_243E')

    Return()

# id: 0x0018 offset: 0x243F
@scena.Code('func_18_243F')
def func_18_243F():
    ClearMapFlags(0x00000001)
    OP_6D(64510, 0, -14780, 92)
    Sleep(100)

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            0x0000,
            0x0008,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
            0x0006,
            0x0003,
            0x0004,
            0x0007,
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
    OP_69(0x0000, 0x00000000)
    Sleep(1000)

    Return()

# id: 0x0019 offset: 0x249C
@scena.Code('func_19_249C')
def func_19_249C():
    OP_A3(0x1C9A)
    OP_A2(0x1C9B)
    OP_A3(0x1C9C)
    OP_A3(0x1C9D)
    OP_A3(0x1C9E)
    OP_A3(0x1C9F)

    Return()

# id: 0x001A offset: 0x24AF
@scena.Code('func_1A_24AF')
def func_1A_24AF():
    OP_A3(0x1C9A)
    OP_A3(0x1C9B)
    OP_A2(0x1C9C)
    OP_A3(0x1C9D)
    OP_A3(0x1C9E)
    OP_A3(0x1C9F)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

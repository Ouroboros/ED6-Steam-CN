import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0310_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0310   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '卡西乌斯'),
    TXT(0x02, '雪拉扎德'),
    TXT(0x03, '凯文神父'),
    TXT(0x04, '目标用照相机'),
    TXT(0x05, '水壶'),
    TXT(0x06, '红茶'),
    TXT(0x07, '红茶'),
    TXT(0x08, '红茶'),
    TXT(0x09, '红茶'),
    TXT(0x0A, '药罐'),
    TXT(0x0B, '莱娜'),
    TXT(0x0C, '器皿'),
    TXT(0x0D, '器皿'),
    TXT(0x0E, '器皿'),
    TXT(0x0F, '沙拉'),
    TXT(0x10, '面包'),
    TXT(0x11, '餐具'),
    TXT(0x12, '餐具'),
    TXT(0x13, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0310.x'
    header.mapIndex       = 15
    header.bgm            = 15
    header.flags          = 0x0000
    header.entryFunction  = 0x0012
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x7B41
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
        ('ED6_DT27/CH03670._CH', 'ED6_DT27/CH03670P._CP'),
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT07/CH02003._CH', 'ED6_DT07/CH02003P._CP'),
        ('ED6_DT07/CH00023._CH', 'ED6_DT07/CH00023P._CP'),
        ('ED6_DT07/CH00003._CH', 'ED6_DT07/CH00003P._CP'),
        ('ED6_DT06/CH20020._CH', 'ED6_DT06/CH20020P._CP'),
        ('ED6_DT27/CH03003._CH', 'ED6_DT27/CH03003P._CP'),
        ('ED6_DT07/CH00053._CH', 'ED6_DT07/CH00053P._CP'),
        ('ED6_DT07/CH00033._CH', 'ED6_DT07/CH00033P._CP'),
        ('ED6_DT07/CH00043._CH', 'ED6_DT07/CH00043P._CP'),
        ('ED6_DT07/CH00063._CH', 'ED6_DT07/CH00063P._CP'),
        ('ED6_DT07/CH00073._CH', 'ED6_DT07/CH00073P._CP'),
        ('ED6_DT26/CH20320._CH', 'ED6_DT26/CH20320P._CP'),
        ('ED6_DT07/CH02003._CH', 'ED6_DT07/CH02003P._CP'),
        ('ED6_DT27/CH03740._CH', 'ED6_DT27/CH03740P._CP'),
        ('ED6_DT26/CH20332._CH', 'ED6_DT26/CH20332P._CP'),
        ('ED6_DT27/CH03743._CH', 'ED6_DT27/CH03743P._CP'),
        ('ED6_DT06/CH20008._CH', 'ED6_DT06/CH20008P._CP'),
        ('ED6_DT27/CH03740._CH', 'ED6_DT27/CH03740P._CP'),
        ('ED6_DT26/CH20239._CH', 'ED6_DT26/CH20239P._CP'),
        ('ED6_DT27/CH03740._CH', 'ED6_DT27/CH03740P._CP'),
        ('ED6_DT27/CH03080._CH', 'ED6_DT27/CH03080P._CP'),
        ('ED6_DT26/CH20232._CH', 'ED6_DT26/CH20232P._CP'),
        ('ED6_DT27/CH03673._CH', 'ED6_DT27/CH03673P._CP'),
        ('ED6_DT26/CH20263._CH', 'ED6_DT26/CH20263P._CP'),
        ('ED6_DT26/CH20278._CH', 'ED6_DT26/CH20278P._CP'),
    ]

# id: 0x10002 offset: 0x17A
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
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
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
            dword_10            = 1703941,
            chipIndex           = 5,
            npcIndex            = 0x01E6,
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
            dword_10            = 1638405,
            chipIndex           = 5,
            npcIndex            = 0x01E6,
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
            dword_10            = 1638405,
            chipIndex           = 5,
            npcIndex            = 0x01E6,
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
            dword_10            = 1638405,
            chipIndex           = 5,
            npcIndex            = 0x01E6,
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
            dword_10            = 1638405,
            chipIndex           = 5,
            npcIndex            = 0x01E6,
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
            dword_10            = 1703941,
            chipIndex           = 5,
            npcIndex            = 0x01E6,
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
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 655365,
            chipIndex           = 5,
            npcIndex            = 0x01E6,
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
            dword_10            = 655365,
            chipIndex           = 5,
            npcIndex            = 0x01E6,
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
            dword_10            = 655365,
            chipIndex           = 5,
            npcIndex            = 0x01E6,
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
            dword_10            = 458757,
            chipIndex           = 5,
            npcIndex            = 0x01E6,
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
            dword_10            = 1769477,
            chipIndex           = 5,
            npcIndex            = 0x01E6,
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
            dword_10            = 1376261,
            chipIndex           = 5,
            npcIndex            = 0x01E6,
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
            dword_10            = 1376261,
            chipIndex           = 5,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x3BA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x3BA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x3BA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 72990,
            triggerZ            = 0,
            triggerY            = -460,
            triggerRange        = 800,
            actorX              = 72990,
            actorZ              = 1000,
            actorY              = -460,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 9360,
            triggerZ            = 0,
            triggerY            = 68590,
            triggerRange        = 800,
            actorX              = 9260,
            actorZ              = 800,
            actorY              = 68720,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000E,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 70420,
            triggerZ            = 0,
            triggerY            = 148490,
            triggerRange        = 500,
            actorX              = 70420,
            actorZ              = 500,
            actorY              = 148490,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0011,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 146290,
            triggerZ            = 0,
            triggerY            = 144760,
            triggerRange        = 800,
            actorX              = 147910,
            actorZ              = 1500,
            actorY              = 144780,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0015,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 72010,
            triggerZ            = 0,
            triggerY            = 71390,
            triggerRange        = 800,
            actorX              = 72570,
            actorZ              = 1500,
            actorY              = 72600,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0015,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x46E
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_488',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x58),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10F0)
    Event(0, 0x0005)

    Jump('loc_4FA')

    def _loc_488(): pass

    label('loc_488')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_4A2',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x19),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10F1)
    Event(0, 0x0006)

    Jump('loc_4FA')

    def _loc_4A2(): pass

    label('loc_4A2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Return,
        ),
        'loc_4B3',
    )

    OP_A3(0x10F2)
    Event(0, 0x0007)

    Jump('loc_4FA')

    def _loc_4B3(): pass

    label('loc_4B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 3, 0x10F3)),
            Expr.Return,
        ),
        'loc_4C4',
    )

    OP_A3(0x10F3)
    Event(0, 0x0008)

    Jump('loc_4FA')

    def _loc_4C4(): pass

    label('loc_4C4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 4, 0x10F4)),
            Expr.Return,
        ),
        'loc_4DE',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x75),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10F4)
    Event(0, 0x0009)

    Jump('loc_4FA')

    def _loc_4DE(): pass

    label('loc_4DE')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x6F),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4FA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0307, 1, 0x1839)),
            (Expr.TestScenaFlags, ScenaFlag(0x0307, 2, 0x183A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4FA',
    )

    Event(0, 0x0010)

    def _loc_4FA(): pass

    label('loc_4FA')

    Return()

# id: 0x0001 offset: 0x4FB
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            (Expr.TestScenaFlags, ScenaFlag(0x0306, 4, 0x1834)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_530',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x75),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMapFlags(0x02000000)
    OP_10(0x08, 0x00)
    OP_10(0x09, 0x00)
    OP_10(0x0A, 0x01)
    OP_10(0x0B, 0x01)
    OP_64(0x03, 0x0001)
    OP_64(0x03, 0x0001)

    Jump('loc_53C')

    def _loc_530(): pass

    label('loc_530')

    OP_10(0x08, 0x01)
    OP_10(0x09, 0x01)
    OP_10(0x0A, 0x00)
    OP_10(0x0B, 0x00)

    def _loc_53C(): pass

    label('loc_53C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0306, 4, 0x1834)),
            (Expr.TestScenaFlags, ScenaFlag(0x0307, 1, 0x1839)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_554',
    )

    OP_72(0x0004, 0x0010)
    OP_65(0x00, 0x0001)

    Jump('loc_55D')

    def _loc_554(): pass

    label('loc_554')

    OP_71(0x0004, 0x0010)
    OP_64(0x00, 0x0001)

    def _loc_55D(): pass

    label('loc_55D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0306, 7, 0x1837)),
            (Expr.TestScenaFlags, ScenaFlag(0x0307, 0, 0x1838)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_570',
    )

    OP_65(0x01, 0x0001)

    Jump('loc_574')

    def _loc_570(): pass

    label('loc_570')

    OP_64(0x01, 0x0001)

    def _loc_574(): pass

    label('loc_574')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0306, 4, 0x1834)),
            (Expr.TestScenaFlags, ScenaFlag(0x0307, 3, 0x183B)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_587',
    )

    OP_65(0x02, 0x0001)

    Jump('loc_58B')

    def _loc_587(): pass

    label('loc_587')

    OP_64(0x02, 0x0001)

    def _loc_58B(): pass

    label('loc_58B')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_99F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0306, 4, 0x1834)),
            Expr.Return,
        ),
        'loc_5C8',
    )

    SetChrFlags(0x0008, 0x0020)
    SetChrFlags(0x0008, 0x0010)
    SetChrFlags(0x0008, 0x0004)
    SetChrPos(0x0008, 3070, 200, 71390, 180)
    SetChrChipByIndex(0x0008, 13)
    ClearChrFlags(0x0008, 0x0080)

    def _loc_5C8(): pass

    label('loc_5C8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0306, 4, 0x1834)),
            Expr.Return,
        ),
        'loc_99F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0306, 5, 0x1835)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5F7',
    )

    SetChrPos(0x0012, -1400, 0, 3140, 90)
    ClearChrFlags(0x0012, 0x0080)
    CreateThread(0x0012, 0x00, 0x00, 0x0002)

    Jump('loc_99F')

    def _loc_5F7(): pass

    label('loc_5F7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0306, 6, 0x1836)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_742',
    )

    SetChrPos(0x0012, -1400, 0, 3140, 90)
    SetChrFlags(0x0012, 0x0010)
    ClearChrFlags(0x0012, 0x0080)
    CreateThread(0x0012, 0x00, 0x00, 0x0002)
    SetChrPos(0x0011, -630, 800, 2940, 0)
    SetChrSubChip(0x0011, 31)
    ClearChrFlags(0x0011, 0x0080)
    SetChrPos(0x0013, -8290, 800, 1250, 0)
    SetChrPos(0x0014, -9800, 800, 1250, 0)
    SetChrPos(0x0015, -8290, 800, 290, 0)
    SetChrPos(0x0017, -7870, 800, 270, 0)
    SetChrPos(0x0018, -8000, 800, 1300, 0)
    SetChrPos(0x0019, -10450, 800, 1290, 0)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x0017, 0x0080)
    ClearChrFlags(0x0018, 0x0080)
    ClearChrFlags(0x0019, 0x0080)
    SetChrSubChip(0x0013, 1)
    SetChrSubChip(0x0014, 1)
    SetChrSubChip(0x0015, 1)
    SetChrSubChip(0x0017, 12)
    LoadEffect(0x01, 'map\\\\mp068_00.eff')
    PlayEffect(0x01, 0x01, 0x00FF, -630, 0, 2940, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_731'),
        (0x00000065, 'loc_731'),
        (0x00000068, 'loc_731'),
        (-1, 'loc_739'),
    )

    def _loc_731(): pass

    label('loc_731')

    OP_22(0x0119, 0x01, 0x5A)

    Jump('loc_73F')

    def _loc_739(): pass

    label('loc_739')

    OP_23(0x0119)

    Jump('loc_73F')

    def _loc_73F(): pass

    label('loc_73F')

    Jump('loc_99F')

    def _loc_742(): pass

    label('loc_742')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0307, 0, 0x1838)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7E5',
    )

    SetChrPos(0x0013, -8290, 800, 1250, 0)
    SetChrPos(0x0014, -9800, 800, 1250, 0)
    SetChrPos(0x0015, -8290, 800, 290, 0)
    SetChrPos(0x0017, -7870, 800, 270, 0)
    SetChrPos(0x0018, -8000, 800, 1300, 0)
    SetChrPos(0x0019, -10450, 800, 1290, 0)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x0017, 0x0080)
    ClearChrFlags(0x0018, 0x0080)
    ClearChrFlags(0x0019, 0x0080)
    SetChrSubChip(0x0013, 0)
    SetChrSubChip(0x0014, 0)
    SetChrSubChip(0x0015, 0)
    SetChrSubChip(0x0017, 12)

    Jump('loc_99F')

    def _loc_7E5(): pass

    label('loc_7E5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0307, 0, 0x1838)),
            (Expr.TestScenaFlags, ScenaFlag(0x0307, 3, 0x183B)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_8C6',
    )

    SetChrPos(0x0012, -1560, 0, 3990, 90)
    ClearChrFlags(0x0012, 0x0080)
    CreateThread(0x0012, 0x00, 0x00, 0x0002)
    SetChrPos(0x0013, -8290, 800, 1250, 0)
    SetChrPos(0x0014, -9800, 800, 1250, 0)
    SetChrPos(0x0015, -8290, 800, 290, 0)
    SetChrPos(0x0016, -640, 600, 4330, 0)
    SetChrPos(0x0017, -7870, 800, 270, 0)
    SetChrPos(0x0018, -8000, 800, 1300, 0)
    SetChrPos(0x0019, -10450, 800, 1290, 0)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x0017, 0x0080)
    ClearChrFlags(0x0018, 0x0080)
    ClearChrFlags(0x0019, 0x0080)
    SetChrSubChip(0x0013, 0)
    SetChrSubChip(0x0014, 0)
    SetChrSubChip(0x0015, 0)
    SetChrSubChip(0x0017, 12)
    OP_6F(0x0008, 0)

    Jump('loc_99F')

    def _loc_8C6(): pass

    label('loc_8C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0307, 3, 0x183B)),
            Expr.Return,
        ),
        'loc_99F',
    )

    SetChrPos(0x0012, -7000, 0, 1420, 270)
    ClearChrFlags(0x0012, 0x0080)
    CreateThread(0x0012, 0x00, 0x00, 0x0002)
    SetChrPos(0x0013, -8290, 800, 1250, 0)
    SetChrPos(0x0014, -9800, 800, 1250, 0)
    SetChrPos(0x0015, -8290, 800, 290, 0)
    SetChrPos(0x0016, -9200, 800, 800, 0)
    SetChrPos(0x0017, -7870, 800, 270, 0)
    SetChrPos(0x0018, -8000, 800, 1300, 0)
    SetChrPos(0x0019, -10450, 800, 1290, 0)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x0017, 0x0080)
    ClearChrFlags(0x0018, 0x0080)
    ClearChrFlags(0x0019, 0x0080)
    SetChrSubChip(0x0013, 0)
    SetChrSubChip(0x0014, 0)
    SetChrSubChip(0x0015, 0)
    SetChrSubChip(0x0017, 12)
    OP_6F(0x0008, 15)

    def _loc_99F(): pass

    label('loc_99F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0305, 0, 0x1828)),
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_9AE',
    )

    Jump('loc_9B8')

    def _loc_9AE(): pass

    label('loc_9AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 5, 0x180D)),
            Expr.Return,
        ),
        'loc_9B8',
    )

    OP_82(0x81, 0x00)

    def _loc_9B8(): pass

    label('loc_9B8')

    OP_82(0x80, 0x00)

    Return()

# id: 0x0002 offset: 0x9BC
@scena.Code('ReInit')
def ReInit():
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
        'loc_9E1',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_B23')

    def _loc_9E1(): pass

    label('loc_9E1')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9FA',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000640)

    Jump('loc_B23')

    def _loc_9FA(): pass

    label('loc_9FA')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A13',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x0000060E)

    Jump('loc_B23')

    def _loc_A13(): pass

    label('loc_A13')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A2C',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005DC)

    Jump('loc_B23')

    def _loc_A2C(): pass

    label('loc_A2C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A45',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AA)

    Jump('loc_B23')

    def _loc_A45(): pass

    label('loc_A45')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A5E',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x00000578)

    Jump('loc_B23')

    def _loc_A5E(): pass

    label('loc_A5E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A77',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x00000546)

    Jump('loc_B23')

    def _loc_A77(): pass

    label('loc_A77')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A90',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000677)

    Jump('loc_B23')

    def _loc_A90(): pass

    label('loc_A90')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AA9',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000645)

    Jump('loc_B23')

    def _loc_AA9(): pass

    label('loc_AA9')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AC2',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x00000613)

    Jump('loc_B23')

    def _loc_AC2(): pass

    label('loc_AC2')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_ADB',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005E1)

    Jump('loc_B23')

    def _loc_ADB(): pass

    label('loc_ADB')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AF4',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AF)

    Jump('loc_B23')

    def _loc_AF4(): pass

    label('loc_AF4')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B0D',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x0000057D)

    Jump('loc_B23')

    def _loc_B0D(): pass

    label('loc_B0D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B23',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x0000054B)

    def _loc_B23(): pass

    label('loc_B23')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_B38',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_B23')

    def _loc_B38(): pass

    label('loc_B38')

    Return()

# id: 0x0003 offset: 0xB39
@scena.Code('func_03_B39')
def func_03_B39():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            (Expr.TestScenaFlags, ScenaFlag(0x0306, 4, 0x1834)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_B50',
    )

    Call(0, 0x000C)

    Jump('loc_B68')

    def _loc_B50(): pass

    label('loc_B50')

    TalkBegin(0x0008)

    ChrTalk(
        0x0008,
        (
            '◆没有台词。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0008)

    def _loc_B68(): pass

    label('loc_B68')

    Return()

# id: 0x0004 offset: 0xB69
@scena.Code('func_04_B69')
def func_04_B69():
    Call(0, 0x000D)

    Return()

# id: 0x0005 offset: 0xB6E
@scena.Code('func_05_B6E')
def func_05_B6E():
    EventBegin(0x00)
    OP_6D(-900, 0, -2790, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(50000, 0)
    OP_6E(280, 0)
    SetChrFlags(0x0142, 0x0080)
    SetChrPos(0x0101, -1210, 0, -5810, 0)

    @scena.Lambda('lambda_0BC9')
    def lambda_0BC9():
        OP_8E(0x0101, -900, 0, -2790, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0BC9)

    WaitForThreadExit(0x0101, 0x0000)
    OP_8C(0x0101, 270, 400)
    Sleep(300)

    OP_8C(0x0101, 0, 400)
    OP_8C(0x0101, 90, 400)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010190309V#001F我回来了，约修亚！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190310V喂，你已经回来了对不对！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(2000)

    OP_63(0x0101)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010190311V#505F奇怪……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190312V约修亚……\n',
            '他应该已经回来了呀……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190313V#004F啊、一定是在老爸的书房。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_6A(0x0101)
    OP_8E(0x0101, 4750, 0, -1080, 5000, 0x00)
    OP_8C(0x0101, 0, 400)
    OP_72(0x0001, 0x0010)
    OP_6F(0x0001, 0)
    OP_70(0x0001, 0x00000013)
    OP_73(0x0001)
    FadeOut(1000, 0, -1)
    OP_8E(0x0101, 5470, 0, 2230, 5000, 0x00)
    OP_0D()
    SetChrPos(0x0101, 2910, 0, 65200, 0)
    OP_69(0x0101, 0x00000000)
    FadeIn(1000, 0)
    OP_8E(0x0101, 3370, 0, 67970, 5000, 0x00)
    OP_0D()
    OP_20(0x00001388)
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(2000)

    OP_63(0x0101)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010190314V#586F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x0142, 0x0080)
    OP_8C(0x0101, 180, 400)
    Sleep(500)

    FadeOut(1000, 0, -1)

    @scena.Lambda('lambda_0DE8')
    def lambda_0DE8():
        OP_8E(0x00FE, 2830, 0, 64330, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0DE8)

    Sleep(500)

    OP_9F(0x0101, 0x00, 0x00, 0x00, 0x00, 0x000001F4)
    OP_0D()
    SetChrPos(0x0142, -1200, 0, -5160, 0)
    OP_9F(0x0101, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000000)
    SetChrPos(0x0101, 5470, 0, 2230, 180)
    OP_69(0x0101, 0x00000000)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_0E51')
    def lambda_0E51():
        OP_8E(0x0142, -560, 0, -2870, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0E51)

    @scena.Lambda('lambda_0E6C')
    def lambda_0E6C():
        OP_8E(0x0101, 4800, 0, -2820, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0142, 0x0000, lambda_0E6C)

    Sleep(1000)

    WaitForThreadExit(0x0142, 0x0000)
    TerminateThread(0x0101, 0x00)

    @scena.Lambda('lambda_0E95')
    def lambda_0E95():
        ChrTurnDirection(0x0142, 0x0101, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0E95)

    @scena.Lambda('lambda_0EA3')
    def lambda_0EA3():
        OP_8E(0x0101, 10810, 2000, -3280, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0142, 0x0000, lambda_0EA3)

    WaitForThreadExit(0x0142, 0x0000)
    FadeOut(1000, 0, -1)

    @scena.Lambda('lambda_0ECD')
    def lambda_0ECD():
        OP_8E(0x0101, 10940, 2000, -1480, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0142, 0x0000, lambda_0ECD)

    WaitForThreadExit(0x0142, 0x0000)

    @scena.Lambda('lambda_0EED')
    def lambda_0EED():
        OP_8E(0x0101, 8690, 4000, -1310, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0142, 0x0000, lambda_0EED)

    OP_0D()
    SetChrPos(0x0101, 81350, 0, -1130, 270)
    OP_69(0x0101, 0x00000000)
    FadeIn(1000, 0)
    OP_8E(0x0101, 75190, 0, -950, 5000, 0x00)
    OP_0D()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010190315V#004F……对了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 90, 500)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010190316V#586F这么说的话………他有可能\n',
            '在我的房间里啊……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190317V#503F糟了，我的内衣\n',
            '好像都胡乱放在外面了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8E(0x0101, 78740, 0, -560, 5000, 0x00)
    OP_8C(0x0101, 0, 400)
    OP_72(0x0003, 0x0010)
    OP_6F(0x0003, 0)
    OP_70(0x0003, 0x00000013)
    OP_73(0x0003)
    FadeOut(1000, 0, -1)
    OP_8E(0x0101, 78660, 0, 1470, 5000, 0x00)
    OP_0D()
    SetChrPos(0x0101, 143760, 0, 139970, 0)
    OP_69(0x0101, 0x00000000)
    FadeIn(1000, 0)
    OP_8E(0x0101, 144890, 0, 143800, 5000, 0x00)
    OP_0D()
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(2000)

    OP_63(0x0101)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010190100V#587F…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190319V#506F还好……\n',
            '原来没有放在外面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190320V呼、不过如果是约修亚的话，\n',
            '就算看到我的内衣\n',
            '也不会有什么反应的………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190321V#586F…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 180, 400)
    Sleep(500)

    @scena.Lambda('lambda_119B')
    def lambda_119B():
        OP_8E(0x0101, 143760, 0, 139970, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_119B)

    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    TerminateThread(0x0101, 0x01)
    SetChrPos(0x0101, 78660, 0, 1470, 180)
    OP_69(0x0101, 0x00000000)
    FadeIn(1000, 0)
    OP_8E(0x0101, 78900, 0, -1500, 2000, 0x00)
    OP_0D()
    OP_8E(0x0101, 72810, 0, -1500, 2000, 0x00)
    OP_8E(0x0101, 72810, 0, -500, 2000, 0x00)
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(2000)

    OP_63(0x0101)
    Sleep(500)

    OP_22(0x0071, 0x00, 0x64)
    Sleep(300)

    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010190322V#586F约修亚……我进去了哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_72(0x0004, 0x0010)
    OP_6F(0x0004, 0)
    OP_70(0x0004, 0x00000013)
    OP_73(0x0004)
    Sleep(500)

    FadeOut(2000, 0, -1)
    ClearMapFlags(0x00000001)
    OP_8E(0x0101, 73200, 0, 1750, 1000, 0x00)
    OP_0D()
    OP_6D(70660, 0, 64780, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(50000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0101, 70820, 0, 64790, 0)
    Sleep(500)

    OP_C4(0x00, 0x00000002)
    OP_1D(0x50)
    FadeIn(1500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010190323V#587F…………啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_134F')
    def lambda_134F():
        OP_6D(70630, 0, 71190, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_134F)

    @scena.Lambda('lambda_1367')
    def lambda_1367():
        OP_67(0, 6000, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1367)

    Sleep(1000)

    @scena.Lambda('lambda_1384')
    def lambda_1384():
        OP_8E(0x0101, 70610, 0, 71230, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1384)

    Sleep(3000)

    @scena.Lambda('lambda_13A4')
    def lambda_13A4():
        OP_8E(0x0101, 70610, 0, 71230, 950, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_13A4)

    Sleep(2000)

    @scena.Lambda('lambda_13C4')
    def lambda_13C4():
        OP_8E(0x0101, 70610, 0, 71230, 900, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_13C4)

    Sleep(1000)

    @scena.Lambda('lambda_13E4')
    def lambda_13E4():
        OP_8E(0x0101, 70610, 0, 71230, 850, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_13E4)

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010190324V#586F唉……是…是吗…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    Fade(250)
    SetChrChipByIndex(0x0101, 22)
    SetChrSubChip(0x0101, 0)
    OP_22(0x00D1, 0x00, 0x50)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010190325V#588F我……真像个大傻瓜啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9F(0x0142, 0x00, 0x00, 0x00, 0x00, 0x00000000)
    SetChrPos(0x0142, 70840, 0, 64450, 50)

    @scena.Lambda('lambda_14A4')
    def lambda_14A4():
        OP_9F(0x0142, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)

        ExitThread()

    DispatchAsync(0x0142, 0x0000, lambda_14A4)

    OP_8E(0x0142, 70570, 0, 68000, 1500, 0x00)
    Sleep(500)

    ChrTalk(
        0x0142,
        (
            '#0180190326V#1067F#2P他……\n',
            '好像不在啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190327V#003F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0142,
        (
            '#0180190328V#2P#1060F那还有一种可能。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190329V他回来以后\n',
            '又跑到城里去了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190330V#588F#5P……不会的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0142,
        (
            '#0180190331V#2P#1065F呼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190332V#1063F你好像总算明白了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190333V#003F…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190334V#586F事实上……\n',
            '我早就明白的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190335V约修亚已经走了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190336V不会再回家…\n',
            '这些我都明白……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0142,
        (
            '#0180190337V#2P#1067F是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190338V#588F可是……\n',
            '这个房间是最后的希望了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190339V除此之外，我再也想不出\n',
            '约修亚会去的地方……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190340V所以……已经彻底没希望了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190341V我再也……\n',
            '见不到约修亚了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0142,
        (
            '#0180190342V#2P#1063F………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190343V#1065F现在就放弃未免太早了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190344V#587F…………？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1804')
    def lambda_1804():
        OP_6D(71130, 0, 71690, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1804)

    OP_8E(0x0142, 71660, 0, 71130, 2000, 0x00)
    OP_8C(0x0142, 270, 400)
    WaitForThreadExit(0x0101, 0x0003)
    Sleep(500)

    ChrTalk(
        0x0142,
        (
            '#0180190345V#2P#1060F命运这种东西，\n',
            '除了女神之外谁也不能断定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190346V不到最后一刻\n',
            '怎么能自己就先放弃呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190347V最重要的，你应该想想\n',
            '自己到底该怎么做？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190348V#003F#6P可、可是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190349V就算我想找约修亚\n',
            '也没有任何线索……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0142,
        (
            '#0180190350V#2P#1060F哎呀，那也没关系。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190351V虽然我不知道他是什么样的人，\n',
            '不过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190352V毕竟不可能没有任何理由\n',
            '就直接消失的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(150)

    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010190353V#587F#6P……啊………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0142,
        (
            '#0180190354V#2P#1063F最近你是否感觉到他的\n',
            '言行或态度和平时比有什么不同？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190355V或者…在他的身上\n',
            '是否发生了什么不正常的事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190356V你一直在他的身边，\n',
            '这些事总该有些了解吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190357V#580F#6P……啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    OP_20(0x000005DC)
    OP_AD(0x002400B8, 0x0000, 0x0000, 0x000003E8)
    Sleep(1200)

    OP_77(0x00, 0x00, 0x00, 0x00, 0x00000000)
    OP_AD(0x002400B9, 0x0000, 0x0000, 0x000003E8)
    Sleep(1200)

    OP_AD(0x002400BA, 0x0000, 0x0000, 0x000003E8)
    Sleep(1200)

    OP_AD(0x002400BB, 0x0000, 0x0000, 0x000003E8)
    Sleep(1200)

    OP_AD(0x002400BC, 0x0000, 0x0000, 0x000003E8)
    Sleep(1200)

    OP_AD(0x002400BD, 0x0000, 0x0000, 0x000003E8)
    Sleep(1200)

    OP_AD(0x002400BE, 0x0000, 0x0000, 0x000003E8)
    Sleep(1200)

    OP_AE(0x000003E8)
    Sleep(1000)

    SetChrName('艾丝蒂尔')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0010190358V#580F#3S啊啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_69(0x0101, 0x00000000)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrSubChip(0x0101, 0)
    OP_77(0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)
    Sleep(1500)

    ChrTalk(
        0x0101,
        (
            '#0010190359V#580F#6P约修亚的样子变得奇怪～？\n',
            '确实……是在我回到那休息处之后…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190360V……为什么……会这样？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190361V为什么我……\n',
            '一点也回忆不起那时遇到的人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0142,
        (
            '#0180190362V#2P#1063F没、没事吧？\n',
            '你的脸色好差啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(150)

    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010190363V#587F#6P呼…嗯……我不要紧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(200)

    Sleep(500)

    Fade(500)
    SetChrChipByIndex(0x0101, 65535)
    ClearChrFlags(0x0101, 0x0002)
    SetChrSubChip(0x0101, 0)
    OP_8C(0x0101, 0, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010190364V#002F#6P是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190365V约修亚的目的\n',
            '是要阻止邪恶的魔法师……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190366V#003F如果说…我当时遇到的那个人\n',
            '就是魔法师的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190367V如果那个人和政变的幕后黑手\n',
            '是同一个人的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190368V那他一定还会在利贝尔\n',
            '酝酿着什么邪恶的计划……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190369V#586F那么，如果我以游击士的身份\n',
            '前去阻止他的话，也许……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190370V……也许……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x0006, 0x00, 0x64)
    Sleep(500)

    SetChrPos(0x0008, 70740, 0, 64890, 0)

    NpcTalk(
        0x0008,
        '男人的声音',
        (
            '#0160190371V#1P……看来你终于理清思路了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_1D(0x76)
    Sleep(500)

    @scena.Lambda('lambda_1F47')
    def lambda_1F47():
        ChrTurnDirection(0x0142, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0142, 0x0000, lambda_1F47)

    @scena.Lambda('lambda_1F55')
    def lambda_1F55():
        OP_8C(0x0101, 180, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1F55)

    @scena.Lambda('lambda_1F63')
    def lambda_1F63():
        OP_6D(70790, 0, 70530, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1F63)

    @scena.Lambda('lambda_1F7B')
    def lambda_1F7B():
        OP_67(0, 6000, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1F7B)

    Sleep(500)

    ClearChrFlags(0x0008, 0x0080)
    OP_9F(0x0008, 0x00, 0x00, 0x00, 0x00, 0x00000000)

    @scena.Lambda('lambda_1FA8')
    def lambda_1FA8():
        OP_8E(0x0008, 70310, 0, 69050, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_1FA8)

    @scena.Lambda('lambda_1FC3')
    def lambda_1FC3():
        OP_9F(0x0008, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1FC3)

    Sleep(500)

    @scena.Lambda('lambda_1FDA')
    def lambda_1FDA():
        OP_8E(0x0142, 72130, 0, 70240, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0142, 0x0001, lambda_1FDA)

    WaitForThreadExit(0x0142, 0x0001)

    @scena.Lambda('lambda_1FFA')
    def lambda_1FFA():
        OP_8C(0x0142, 225, 400)

        ExitThread()

    DispatchAsync(0x0142, 0x0002, lambda_1FFA)

    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, 70740, 0, 64890, 0)
    OP_9F(0x0009, 0x00, 0x00, 0x00, 0x00, 0x00000000)

    @scena.Lambda('lambda_2029')
    def lambda_2029():
        OP_8E(0x0009, 71150, 0, 68210, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2029)

    @scena.Lambda('lambda_2044')
    def lambda_2044():
        OP_9F(0x0009, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2044)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010190372V#580F#5P老爸！？雪拉姐！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190373V你们…为什么会在这里…？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0142, 250, 400)
    Sleep(500)

    ChrTalk(
        0x0142,
        (
            '#0180190374V#1060F#2P……抱歉，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190375V在下船的时候，我就和\n',
            '协会的王都支部联系过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190376V#004F#5P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030190377V#025F你真是吓死我们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030190378V我到处找你，刚到协会时\n',
            '正好接到了消息。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030190379V#524F然后就和老师一起匆匆忙忙\n',
            '坐上了即将起飞的货船赶了过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190380V#586F#5P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160190381V#1125F#6P嗯，事情就是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0008, 55, 400)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0160190382V#1120F#6P你就是凯文神父吧？\n',
            '你这次的联络真是帮了大忙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160190383V非常感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0142, 225, 400)
    Sleep(300)

    ChrTalk(
        0x0142,
        (
            '#0180190384V#1061F#2P啊哈哈～没什么啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180190385V倒是我这个局外人在这里乱掺和，\n',
            '真是不好意思啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190386V#003F#5P那、那个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190387V老爸，我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0008, 6, 400)
    Sleep(200)

    OP_8C(0x0142, 250, 400)
    Sleep(200)

    ChrTalk(
        0x0008,
        (
            '#0160190388V#6P#1122F我明白。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160190389V#1125F……让你不要深入调查什么的，\n',
            '都只是我自私的想法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160190390V不管是身为男人还是身为父亲，\n',
            '我都不该把自己的意志强加给你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160190391V#1120F因为这个我还被雪拉扎德骂了一顿呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190392V#586F#5P雪拉姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030190393V#021F呵呵～姐姐这次可是\n',
            '完全站在你这边的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160190394V#6P#1125F虽然我早有心理准备……\n',
            '但这臭小子突然不辞而别，\n',
            '确实让我也很难承受。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160190395V所以我才不愿意你也踏上\n',
            '这条危险的道路。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160190396V莱娜用生命保护你了，\n',
            '我实在不想你也和莱娜一样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160190397V#1120F……但现在我明白了，\n',
            '我这种自私的想法不但对不起你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160190398V而且也对不起你妈妈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190399V#587F#5P老爸……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160190400V#6P#1122F……我现在军务缠身，\n',
            '实在不能离开。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160190401V不然就会让那些家伙\n',
            '有可乘之机……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160190402V因此这一次我可能完全\n',
            '帮不上你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160190403V即使如此，你的决心也没有改变吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190404V#003F#5P……嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190405V虽然我还远未成熟，不过…\n',
            '现在没有别的选择了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190406V#002F我必须要努力试试看了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190407V阻止『噬身之蛇』的阴谋，\n',
            '然后把约修亚带回来给你看！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160190408V#6P#1125F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160190409V#1122F那样的话我也就不必再多说了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160190410V……作为一名游击士，\n',
            '也作为一个普通的女孩子…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160190411V你就去走自己的路吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190412V#586F#5P……老爸……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_287E')
    def lambda_287E():
        OP_6D(70500, 0, 70000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_287E)

    SetChrFlags(0x0008, 0x0040)
    OP_8E(0x0101, 70320, 0, 69640, 3000, 0x00)
    SetChrPos(0x0101, 70300, 0, 69450, 180)
    SetChrFlags(0x0008, 0x0008)
    SetChrChipByIndex(0x0101, 24)
    SetChrFlags(0x0101, 0x0002)
    SetChrSubChip(0x0101, 12)

    @scena.Lambda('lambda_28D4')
    def lambda_28D4():
        OP_6B(2700, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_28D4)

    @scena.Lambda('lambda_28E4')
    def lambda_28E4():
        OP_8C(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x0142, 0x0003, lambda_28E4)

    OP_99(0x0101, 0x00, 0x03, 0x000003E8)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010190413V#5P#588F#40W我……我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160190414V#6P#1125F对了……\n',
            '有件最重要的事忘了说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190415V#5P#587F啊……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0101, 0x03, 0x06, 0x000003E8)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0160190416V#6P#1122F艾丝蒂尔，拜托你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160190417V──请一定帮我将约修亚…\n',
            '那个笨蛋儿子带回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190418V#5P#586F……啊………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0101, 0x09, 0x0B, 0x000003E8)
    OP_99(0x0101, 0x0B, 0x09, 0x000003E8)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010190419V#5P#1080F嗯……我知道了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190420V为了我们全家……\n',
            '能再次团聚在这里一起生活……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190421V#006F我一定会把约修亚带回来……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(3000, 0, -1)
    OP_0D()
    OP_20(0x00000FA0)
    OP_21()
    Sleep(1500)

    OP_C4(0x01, 0x00000002)
    FormationDelMember(0x41, 0xFF)
    SetChrChipByIndex(0x0101, 65535)
    ClearChrFlags(0x0101, 0x0002)
    SetChrSubChip(0x0101, 0)
    OP_C4(0x00, 0x00000010)
    FadeIn(10, 0)
    OP_0D()
    PlayMovie(0x00, 'ed6_2_op.avi', 0x0007, 0x0000)
    Sleep(2000)

    OP_56(0x02)
    FadeOut(2000, 0, -1)

    If(
        (
            (Expr.PushValueByIndex, 0x2D),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2B38',
    )

    OP_20(0x000007D0)

    def _loc_2B38(): pass

    label('loc_2B38')

    OP_21()
    OP_0D()
    PlayMovie(0x01, '', 0x0000, 0x0000)
    Sleep(2000)

    OP_C4(0x01, 0x00000010)
    Sleep(1000)

    OP_AD(0x002400A3, 0x0000, 0x0000, 0x00000064)
    Sleep(4000)

    OP_56(0x02)
    OP_AE(0x000000C8)
    Sleep(2000)

    ClearMapFlags(0x02000000)
    NewScene('ED6_DT21/T5100._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0006 offset: 0x2B7E
@scena.Code('func_06_2B7E')
def func_06_2B7E():
    OP_BB(0x00, 0x00, 0x00200042)
    OP_BB(0x00, 0x01, 0x0000001E)
    OP_BD()
    EventBegin(0x00)
    OP_6D(-7800, 200, 1380, 0)
    OP_67(0, 5720, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(45000, 0)
    OP_6E(246, 0)
    OP_82(0x81, 0x00)
    OP_77(0xD0, 0xAE, 0x5D, 0x00, 0x00000000)
    SetChrPos(0x0008, -8130, 200, 2260, 180)
    SetChrPos(0x0009, -9800, 200, 2200, 180)
    SetChrFlags(0x0101, 0x0004)
    SetChrPos(0x0101, -8220, 200, -630, 0)
    SetChrChipByIndex(0x0008, 23)
    SetChrChipByIndex(0x0009, 3)
    SetChrChipByIndex(0x0101, 4)
    SetChrSubChip(0x0008, 0)
    SetChrSubChip(0x0009, 0)
    SetChrSubChip(0x0101, 0)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    FadeIn(1500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0160190479V#5P#1125F──如之前所说，\n',
            '我并不会阻止你的行动。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160190480V但说实话，就凭你现在的实力，\n',
            '要与结社为敌实在是以卵击石。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160190481V#1122F所以，艾丝蒂尔……\n',
            '要不要去『卢·洛克尔』一趟呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190482V#587F『卢·洛克尔』？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160190483V#5P#1122F那是位于列曼自治州，\n',
            '游击士协会所有的训练场。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160190484V宿舍的周围有各种各样的\n',
            '专业训练设施。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160190485V#1125F训练内容涉及遗迹探索、突击、\n',
            '野外生存，反恐等等……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160190486V要想进行实战训练的话，\n',
            '再没有比那里更合适的地方了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190487V#505F有那样的地方吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190488V#003F不过…自治州的话…\n',
            '也就是说那个训练场在外国了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190489V#587F要是我……\n',
            '在这种时候离开利贝尔的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030190490V#026F#5P虽然从理论上说是外国，\n',
            '不过坐国际飞船的话也只是１天的路程而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030190491V训练时间嘛，嗯……\n',
            '有１个月就可以了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030190492V#020F在这期间如果有什么特殊情况的话\n',
            '我们会马上和你联络的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030190493V这样的话如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190494V#003F…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160190495V#5P#1122F当然了，我只是提个建议，\n',
            '最后的决定权在你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160190496V自己好好考虑一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190497V#500F……不用了，我已经决定了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190498V#002F我要接受这个训练。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030190499V#023F#5P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160190500V#5P#1120F嗯，竟然这么果断。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160190501V看来你是有\n',
            '自己的想法吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190502V#586F嗯……是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190503V#003F仔细想想的话，我至今为止\n',
            '一直都是在依赖着约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190504V不管发生什么事情\n',
            '也都是靠他来指引我。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190505V但是，从现在起\n',
            '我必须要依靠自己的判断力了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190506V#002F所以我……\n',
            '要去那个训练场好好锻炼一下自己。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030190507V#524F#5P艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160190508V#5P#1125F是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160190509V#1120F那么我明天就去\n',
            '洛连特支部向训练场',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160190510V提出训练申请。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190511V#006F嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030190512V#021F#5P那个，艾丝蒂尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030190513V在出发之前一起去\n',
            '王都的百货店逛逛如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190514V#004F啊，怎么了啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030190515V#027F#5P为了庆祝你成为正游击士啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030190516V难得有这么值得庆贺的大事，\n',
            '姐姐要给你买一身新衣服！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x0101, 65535)
    ClearChrFlags(0x0101, 0x0004)
    OP_77(0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_A2(0x10F1)
    NewScene('ED6_DT21/T5110._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0007 offset: 0x3429
@scena.Code('func_07_3429')
def func_07_3429():
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
        'loc_3449',
    )

    Call(0, 0x0013)
    FadeIn(0, 0)
    Call(0, 0x0014)

    def _loc_3449(): pass

    label('loc_3449')

    LoadEffect(0x00, 'map\\\\mpsmk0.eff')
    LoadEffect(0x01, 'map\\\\mp068_00.eff')
    OP_6D(-280, 0, 3400, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrFlags(0x0101, 0x0080)
    SetChrPos(0x0103, -1410, 0, 2670, 90)
    SetChrChipByIndex(0x0011, 25)
    SetChrSubChip(0x0011, 1)
    SetChrPos(0x0011, -600, 200, 2900, 0)
    SetChrPos(0x000C, -640, 600, 4330, 0)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    SetChrFlags(0x000C, 0x0004)
    SetChrFlags(0x0011, 0x0004)
    PlayEffect(0x00, 0x00, 0x00FF, -630, 700, 2940, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0x01, 0x00FF, -630, 0, 2940, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    SetChrFlags(0x00F8, 0x0004)
    SetChrFlags(0x00F9, 0x0004)
    SetChrPos(0x00F8, -9800, 200, -630, 0)
    SetChrPos(0x00F9, -8200, 200, -630, 0)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000005, 'loc_35B5'),
        (0x00000003, 'loc_35BD'),
        (0x00000004, 'loc_35C5'),
        (0x00000006, 'loc_35CD'),
        (0x00000007, 'loc_35D5'),
        (-1, 'loc_35DD'),
    )

    def _loc_35B5(): pass

    label('loc_35B5')

    SetChrChipByIndex(0x00F8, 7)

    Jump('loc_35DD')

    def _loc_35BD(): pass

    label('loc_35BD')

    SetChrChipByIndex(0x00F8, 8)

    Jump('loc_35DD')

    def _loc_35C5(): pass

    label('loc_35C5')

    SetChrChipByIndex(0x00F8, 9)

    Jump('loc_35DD')

    def _loc_35CD(): pass

    label('loc_35CD')

    SetChrChipByIndex(0x00F8, 10)

    Jump('loc_35DD')

    def _loc_35D5(): pass

    label('loc_35D5')

    SetChrChipByIndex(0x00F8, 11)

    Jump('loc_35DD')

    def _loc_35DD(): pass

    label('loc_35DD')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000005, 'loc_35FA'),
        (0x00000003, 'loc_3602'),
        (0x00000004, 'loc_360A'),
        (0x00000006, 'loc_3612'),
        (0x00000007, 'loc_361A'),
        (-1, 'loc_3622'),
    )

    def _loc_35FA(): pass

    label('loc_35FA')

    SetChrChipByIndex(0x00F9, 7)

    Jump('loc_3622')

    def _loc_3602(): pass

    label('loc_3602')

    SetChrChipByIndex(0x00F9, 8)

    Jump('loc_3622')

    def _loc_360A(): pass

    label('loc_360A')

    SetChrChipByIndex(0x00F9, 9)

    Jump('loc_3622')

    def _loc_3612(): pass

    label('loc_3612')

    SetChrChipByIndex(0x00F9, 10)

    Jump('loc_3622')

    def _loc_361A(): pass

    label('loc_361A')

    SetChrChipByIndex(0x00F9, 11)

    Jump('loc_3622')

    def _loc_3622(): pass

    label('loc_3622')

    FadeIn(1500, 0)

    @scena.Lambda('lambda_3631')
    def lambda_3631():
        OP_6D(-7440, 0, 2710, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3631)

    Sleep(4000)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_82(0x00, 0x00)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/T0300._SN', 103, 0, 0)
    IdleLoop()

    Return()

# id: 0x0008 offset: 0x3663
@scena.Code('func_08_3663')
def func_08_3663():
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
        'loc_3683',
    )

    Call(0, 0x0013)
    FadeIn(0, 0)
    Call(0, 0x0014)

    def _loc_3683(): pass

    label('loc_3683')

    OP_6D(-8260, 200, 1880, 0)
    OP_67(0, 4880, -10000, 0)
    OP_6B(2740, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrFlags(0x0101, 0x0004)
    SetChrFlags(0x0103, 0x0004)
    SetChrFlags(0x00F8, 0x0004)
    SetChrFlags(0x00F9, 0x0004)
    SetChrPos(0x0103, -8130, 200, 2260, 180)
    SetChrPos(0x0101, -9800, 200, 2200, 180)
    SetChrPos(0x00F8, -9800, 200, -630, 0)
    SetChrPos(0x00F9, -8200, 200, -630, 0)
    SetChrChipByIndex(0x0101, 6)
    SetChrChipByIndex(0x0103, 3)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000005, 'loc_373F'),
        (0x00000003, 'loc_3747'),
        (0x00000004, 'loc_374F'),
        (0x00000006, 'loc_3757'),
        (0x00000007, 'loc_375F'),
        (-1, 'loc_3767'),
    )

    def _loc_373F(): pass

    label('loc_373F')

    SetChrChipByIndex(0x00F8, 7)

    Jump('loc_3767')

    def _loc_3747(): pass

    label('loc_3747')

    SetChrChipByIndex(0x00F8, 8)

    Jump('loc_3767')

    def _loc_374F(): pass

    label('loc_374F')

    SetChrChipByIndex(0x00F8, 9)

    Jump('loc_3767')

    def _loc_3757(): pass

    label('loc_3757')

    SetChrChipByIndex(0x00F8, 10)

    Jump('loc_3767')

    def _loc_375F(): pass

    label('loc_375F')

    SetChrChipByIndex(0x00F8, 11)

    Jump('loc_3767')

    def _loc_3767(): pass

    label('loc_3767')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000005, 'loc_3784'),
        (0x00000003, 'loc_378C'),
        (0x00000004, 'loc_3794'),
        (0x00000006, 'loc_379C'),
        (0x00000007, 'loc_37A4'),
        (-1, 'loc_37AC'),
    )

    def _loc_3784(): pass

    label('loc_3784')

    SetChrChipByIndex(0x00F9, 7)

    Jump('loc_37AC')

    def _loc_378C(): pass

    label('loc_378C')

    SetChrChipByIndex(0x00F9, 8)

    Jump('loc_37AC')

    def _loc_3794(): pass

    label('loc_3794')

    SetChrChipByIndex(0x00F9, 9)

    Jump('loc_37AC')

    def _loc_379C(): pass

    label('loc_379C')

    SetChrChipByIndex(0x00F9, 10)

    Jump('loc_37AC')

    def _loc_37A4(): pass

    label('loc_37A4')

    SetChrChipByIndex(0x00F9, 11)

    Jump('loc_37AC')

    def _loc_37AC(): pass

    label('loc_37AC')

    SetChrChipByIndex(0x0011, 25)
    SetChrSubChip(0x0011, 1)
    SetChrPos(0x0011, -600, 200, 2900, 0)
    SetChrPos(0x000C, -9100, 800, 800, 0)
    SetChrPos(0x000C, -640, 600, 4330, 0)
    SetChrPos(0x000D, -9800, 800, 1100, 0)
    SetChrPos(0x000E, -8500, 800, 1100, 0)
    SetChrPos(0x000F, -9800, 800, 100, 0)
    SetChrPos(0x0010, -8500, 800, 100, 0)
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    FadeIn(1500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010280977V#1016F#5P呼～\n',
            '总算是到家了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280978V#1017F外边都是雾气，\n',
            '什么都看不清楚啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030280979V#021F呵呵，确实哦。',
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
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3A90',
    )

    ChrTalk(
        0x0106,
        (
            '#0050280980V#051F看起来、雪拉扎德。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050280981V你好像对这里的事情\n',
            '很了解啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030280982V#524F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030280983V我和这个家可是\n',
            '有着很深厚的感情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280984V#1015F#5P从我妈妈还活着的\n',
            '时候开始……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280985V#1001F到现在已经有１０几年了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030280986V#526F嗯，是呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070280987V#560F听说雪拉姐以前\n',
            '是四处旅行的艺人呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070280988V那后来是怎么和姐姐\n',
            '认识的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_49B3')

    def _loc_3A90(): pass

    label('loc_3A90')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3C48',
    )

    ChrTalk(
        0x0106,
        (
            '#0050280980V#051F看起来、雪拉扎德。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050280981V你好像对这里的事情\n',
            '很了解啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030280982V#524F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030280983V我和这个家可是\n',
            '有着很深厚的感情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280984V#1015F#5P从我妈妈还活着的\n',
            '时候开始……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280985V#1001F到现在已经有１０几年了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030280986V#526F嗯，是呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040280996V#030F雪拉以前好像是位\n',
            '周游各地的艺人吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040280997V是在怎样的机缘之下和艾丝蒂尔\n',
            '相识的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_49B3')

    def _loc_3C48(): pass

    label('loc_3C48')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3E00',
    )

    ChrTalk(
        0x0106,
        (
            '#0050280980V#051F看起来、雪拉扎德。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050280981V你好像对这里的事情\n',
            '很了解啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030280982V#524F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030280983V我和这个家可是\n',
            '有着很深厚的感情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280984V#1015F#5P从我妈妈还活着的\n',
            '时候开始……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280985V#1001F到现在已经有１０几年了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030280986V#526F嗯，是呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060281005V#048F听说雪拉小姐你以前是位\n',
            '周游各地的艺人吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060281006V那后来是怎么和艾丝蒂尔\n',
            '认识的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_49B3')

    def _loc_3E00(): pass

    label('loc_3E00')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3FAE',
    )

    ChrTalk(
        0x0106,
        (
            '#0050280980V#051F看起来、雪拉扎德。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050280981V你好像对这里的事情\n',
            '很了解啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030280982V#524F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030280983V我和这个家可是\n',
            '有着很深厚的感情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280984V#1015F#5P从我妈妈还活着的\n',
            '时候开始……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280985V#1001F到现在已经有１０几年了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030280986V#526F嗯，是呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080281014V#070F你以前好像是位\n',
            '周游各地的艺人吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080281015V后来是怎么和艾丝蒂尔\n',
            '认识的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_49B3')

    def _loc_3FAE(): pass

    label('loc_3FAE')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_415A',
    )

    ChrTalk(
        0x0104,
        (
            '#0040281016V#030F话说回来，雪拉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040281017V你对这里的事情\n',
            '还真是熟悉啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030280982V#524F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030280983V我和这个家可是\n',
            '有着很深厚的感情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280984V#1015F#5P从我妈妈还活着的\n',
            '时候开始……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280985V#1001F到现在已经有１０几年了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030280986V#526F嗯，是呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070280987V#560F听说雪拉姐以前\n',
            '是四处旅行的艺人呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070280988V那后来是怎么和姐姐\n',
            '认识的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_49B3')

    def _loc_415A(): pass

    label('loc_415A')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_42FA',
    )

    ChrTalk(
        0x0107,
        (
            '#0070281025V#560F雪拉姐好像对姐姐的家\n',
            '很熟悉呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030281026V#524F呵呵，这个嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030280983V我和这个家可是\n',
            '有着很深厚的感情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280984V#1015F#5P从我妈妈还活着的\n',
            '时候开始……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280985V#1001F到现在已经有１０几年了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030280986V#526F嗯，是呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060281005V#048F听说雪拉扎德你以前是位\n',
            '是四处旅行的艺人呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060281006V那后来是怎么和艾丝蒂尔\n',
            '认识的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_49B3')

    def _loc_42FA(): pass

    label('loc_42FA')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4490',
    )

    ChrTalk(
        0x0107,
        (
            '#0070281025V#560F雪拉姐好像对姐姐的家\n',
            '很熟悉呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030281026V#524F呵呵，这个嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030280983V我和这个家可是\n',
            '有着很深厚的感情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280984V#1015F#5P从我妈妈还活着的\n',
            '时候开始……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280985V#1001F到现在已经有１０几年了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030280986V#526F嗯，是呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080281014V#070F你以前好像是位\n',
            '是四处旅行的艺人呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080281015V后来是怎么和艾丝蒂尔\n',
            '认识的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_49B3')

    def _loc_4490(): pass

    label('loc_4490')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4648',
    )

    ChrTalk(
        0x0104,
        (
            '#0040281016V#030F话说回来，雪拉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040281017V你对这里的事情\n',
            '还真是熟悉啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030280982V#524F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030280983V我和这个家可是\n',
            '有着很深厚的感情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280984V#1015F#5P从我妈妈还活着的\n',
            '时候开始……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280985V#1001F到现在已经有１０几年了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030280986V#526F嗯，是呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060281005V#048F听说雪拉扎德你以前是位\n',
            '是四处旅行的艺人呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060281006V那后来是怎么和艾丝蒂尔\n',
            '认识的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_49B3')

    def _loc_4648(): pass

    label('loc_4648')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_47F6',
    )

    ChrTalk(
        0x0104,
        (
            '#0040281016V#030F话说回来，雪拉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040281017V你对这里的事情\n',
            '还真是熟悉啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030280982V#524F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030280983V我和这个家可是\n',
            '有着很深厚的感情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280984V#1015F#5P从我妈妈还活着的\n',
            '时候开始……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280985V#1001F到现在已经有１０几年了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030280986V#526F嗯，是呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080281014V#070F你以前好像是位\n',
            '是四处旅行的艺人呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080281015V后来是怎么和艾丝蒂尔\n',
            '认识的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_49B3')

    def _loc_47F6(): pass

    label('loc_47F6')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_49B3',
    )

    ChrTalk(
        0x0108,
        (
            '#0080281059V#070F对了，雪拉扎德。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080281060V你对这里的事情\n',
            '好象很熟悉的样子啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030281061V#524F呵呵，这个嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030280983V我和这个家可是\n',
            '有着很深厚的感情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010280984V#1015F#5P从我妈妈还活着的\n',
            '时候开始……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010280985V#1001F到现在已经有１０几年了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030280986V#526F嗯，是呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060281066V#040F雪拉小姐以前好像是个\n',
            '是四处旅行的艺人呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060281006V那后来是怎么和艾丝蒂尔\n',
            '认识的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_49B3(): pass

    label('loc_49B3')

    ChrTalk(
        0x0103,
        (
            '#0030281068V#021F呵呵，这个嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0101, 1)
    Sleep(300)

    OP_62(0x0101, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010281069V#1004F#1P等、等一下啦，雪拉姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0103, 0)
    Sleep(75)

    SetChrSubChip(0x0103, 2)

    ChrTalk(
        0x0103,
        (
            '#0030281070V#027F说说也没关系啦，反正是那么久之前的事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0103, 0)
    OP_63(0x0101)
    Sleep(500)

    ChrTalk(
        0x0103,
        (
            '#0030281071V#026F那是１２年前的事了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281072V我们的戏团来洛连特\n',
            '进行演出。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(1000)

    SetMessageWindowPos(90, 330, -1, -1)
    SetChrName('雪拉扎德')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0030281073V#027F那个时候的艾丝蒂尔\n',
            '好奇心只怕是比现在还要旺盛，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281074V在演出结束后总是一个人跑进\n',
            '我们的帐篷里玩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AD(0x0024007D, 0x0000, 0x0000, 0x000001F4)
    Sleep(1500)

    SetMessageWindowPos(90, 330, -1, -1)
    SetChrName('雪拉扎德')

    Talk(
        (
            '#0030281075V#524F……身为旅行艺人，\n',
            '说白了只不过是一群『流浪者』而已，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281076V一般来说，当地的市民是\n',
            '不会主动来接近我们的。\n',
            '所以一开始大家都有点不知所措……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281077V#021F呵呵，总之就是个天不怕地不怕的孩子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281078V之后她每天都跑来玩，没多久便和\n',
            '大家都混熟了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281079V#526F当然也包括我在内。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AE(0x000001F4)
    Sleep(1000)

    OP_AD(0x0024007E, 0x0000, 0x0000, 0x000001F4)
    Sleep(1500)

    SetMessageWindowPos(90, 330, -1, -1)
    SetChrName('雪拉扎德')

    Talk(
        (
            '#0030281080V#026F有一天，日暮时分\n',
            '玩到天黑才要回家……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281081V没办法，只能由我送她\n',
            '回家去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281082V#027F我和卡西乌斯老师，\n',
            '还有艾丝蒂尔的妈妈莱娜，\n',
            '就是在那个时候认识的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AE(0x000001F4)
    Sleep(1000)

    SetChrSubChip(0x0101, 0)
    SetChrSubChip(0x0103, 0)
    FadeIn(500, 0)
    OP_0D()
    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4E2E',
    )

    ChrTalk(
        0x0107,
        (
            '#0070281083V#061F哇……\n',
            '原来是那样的啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4F2B')

    def _loc_4E2E(): pass

    label('loc_4E2E')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4E6C',
    )

    ChrTalk(
        0x0106,
        (
            '#0050281084V#051F唉……\n',
            '竟然是这样的啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4F2B')

    def _loc_4E6C(): pass

    label('loc_4E6C')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4EAE',
    )

    ChrTalk(
        0x0104,
        (
            '#0040281085V#031F呼……\n',
            '原来发生过那样的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4F2B')

    def _loc_4EAE(): pass

    label('loc_4EAE')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4EEE',
    )

    ChrTalk(
        0x0105,
        (
            '#0060281086V#048F呼呼……\n',
            '原来是那样的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4F2B')

    def _loc_4EEE(): pass

    label('loc_4EEE')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4F2B',
    )

    ChrTalk(
        0x0108,
        (
            '#0080281087V#071F哈哈……\n',
            '竟然是这样的啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4F2B(): pass

    label('loc_4F2B')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4F75',
    )

    ChrTalk(
        0x0107,
        (
            '#0070281088V#061F嘿嘿，姐姐果然\n',
            '从小时候就是这样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_50CA')

    def _loc_4F75(): pass

    label('loc_4F75')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4FCD',
    )

    ChrTalk(
        0x0106,
        (
            '#0050281089V#051F呵～这天不怕地不怕的性格，\n',
            '原来从小时候就有了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_50CA')

    def _loc_4FCD(): pass

    label('loc_4FCD')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5023',
    )

    ChrTalk(
        0x0104,
        (
            '#0040281090V#031F呼～从小时候开始就是\n',
            '这种天不怕地不怕的性格啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_50CA')

    def _loc_5023(): pass

    label('loc_5023')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5077',
    )

    ChrTalk(
        0x0105,
        (
            '#0060281091V#048F呵呵，天不怕地不怕的性格\n',
            '从小时候就开始了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_50CA')

    def _loc_5077(): pass

    label('loc_5077')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_50CA',
    )

    ChrTalk(
        0x0108,
        (
            '#0080281092V#071F哈哈，天不怕地不怕的性格\n',
            '原来从小时候就有了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_50CA(): pass

    label('loc_50CA')

    ChrTalk(
        0x0101,
        (
            '#0010210256V#1016F#5P啊、啊哈哈……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281094V那时我才只有４岁嘛～\n',
            '都已经记不太清楚了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281095V#1017F不过，从那以后，\n',
            '雪拉姐每次再来洛连特演出时\n',
            '都会来我家玩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030281096V#021F呵呵，是啊。',
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
        'loc_52F7',
    )

    ChrTalk(
        0x0106,
        (
            '#0050281097V#050F不过，雪拉扎德，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050281098V身为旅行艺人的你，\n',
            '为什么会在利贝尔\n',
            '当起了游击士了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030281099V#524F……中间发生了好多事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281100V８年前，在我决定成为游击士的时候，\n',
            '所拜托的人就是卡西乌斯老师。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281101V自那以后我就一直留在利贝尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050281102V#053F是这样啊……\n',
            '你也是因为那个大叔…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_56CD')

    def _loc_52F7(): pass

    label('loc_52F7')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5437',
    )

    ChrTalk(
        0x0104,
        (
            '#0040281103V#030F不过，雪拉……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040281104V身为旅行艺人的你，\n',
            '为什么会在利贝尔当起了游击士？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030281099V#524F……中间发生了好多事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281100V８年前，在我决定成为游击士的时候，\n',
            '所拜托的人就是卡西乌斯老师。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281101V自那以后我就一直留在利贝尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040281108V#035F嗯，是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_56CD')

    def _loc_5437(): pass

    label('loc_5437')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_557F',
    )

    ChrTalk(
        0x0108,
        (
            '#0080281109V#073F不过，雪拉扎德，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080281110V身为旅行艺人的你，\n',
            '为什么会在利贝尔当起了游击士？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030281099V#524F……中间发生了好多事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281100V８年前，在我决定成为游击士的时候，\n',
            '所拜托的人就是卡西乌斯老师。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281101V自那以后我就一直留在利贝尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080281114V#070F原来如此，是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_56CD')

    def _loc_557F(): pass

    label('loc_557F')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_56CD',
    )

    ChrTalk(
        0x0107,
        (
            '#0070281115V#064F那个、所谓的旅行艺人，\n',
            '是要在各国巡回演出的吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070281116V为什么最后会留在利贝尔\n',
            '当游击士呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030281099V#524F……中间发生了好多事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281100V８年前，在我决定成为游击士的时候，\n',
            '所拜托的人就是卡西乌斯老师。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281101V自那以后我就一直留在利贝尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070281120V#560F是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_56CD(): pass

    label('loc_56CD')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_573D',
    )

    ChrTalk(
        0x0105,
        (
            '#0060281121V#044F啊，说起来的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060281122V#542F那个时候，约修亚\n',
            '已经来到你家了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5892')

    def _loc_573D(): pass

    label('loc_573D')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_57B3',
    )

    ChrTalk(
        0x0107,
        (
            '#0070281123V#064F啊，说起来的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070281124V#560F啊，那个时候，\n',
            '约修亚哥哥也在姐姐家了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5892')

    def _loc_57B3(): pass

    label('loc_57B3')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5823',
    )

    ChrTalk(
        0x0108,
        (
            '#0080281125V#074F嗯，说起来的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080281126V#070F约修亚那小子当时\n',
            '已经住在你家了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5892')

    def _loc_5823(): pass

    label('loc_5823')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5892',
    )

    ChrTalk(
        0x0104,
        (
            '#0040281127V#035F嗯，说起来的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040281128V#030F在那个时候，\n',
            '约修亚已经来到你家了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5892(): pass

    label('loc_5892')

    ChrTalk(
        0x0101,
        (
            '#0010281129V#1025F#5P啊，还没有……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281130V老爸收养约修亚\n',
            '是３年之后的事情了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0101, 1)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010281131V#1011F#5P就在雪拉姐为了成为正游击士\n',
            '而周游全国的时候，没错吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030281132V#027F嗯嗯，确实是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281133V#021F旅行归来的时候，\n',
            '忽然就介绍一个陌生的男孩给我认识，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281134V当时还真是吃了一惊呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1500, 0, -1)
    OP_0D()
    Sleep(500)

    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '之后，艾丝蒂尔一行人\n',
            '继续谈天说地……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '最后以茶代酒，约定\n',
            '以后再来此聚会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_82(0x81, 0x00)
    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000F, 0x0080)
    SetChrFlags(0x0010, 0x0080)
    SetChrPos(0x0000, -1160, 0, -2760, 171)
    SetChrPos(0x0001, -1160, 0, -2760, 171)
    SetChrPos(0x0002, -1160, 0, -2760, 171)
    SetChrPos(0x0003, -1160, 0, -2760, 171)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0103, 65535)
    SetChrChipByIndex(0x00F8, 65535)
    SetChrChipByIndex(0x00F9, 65535)
    ClearChrFlags(0x0101, 0x0004)
    ClearChrFlags(0x0103, 0x0004)
    ClearChrFlags(0x00F8, 0x0004)
    ClearChrFlags(0x00F9, 0x0004)
    OP_6D(-1160, 0, -2760, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    Sleep(1000)

    FadeIn(1000, 0)
    OP_A2(0x180D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 6, 0x180E)),
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 7, 0x180F)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 0, 0x1810)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5B47',
    )

    OP_28(0x008F, 0x01, 0x2000)
    OP_28(0x008F, 0x01, 0x4000)

    Jump('loc_5B4D')

    def _loc_5B47(): pass

    label('loc_5B47')

    OP_28(0x008F, 0x01, 0x0100)

    def _loc_5B4D(): pass

    label('loc_5B4D')

    EventEnd(0x00)

    Return()

# id: 0x0009 offset: 0x5B50
@scena.Code('func_09_5B50')
def func_09_5B50():
    EventBegin(0x00)
    OP_DB()
    SetChrChipByIndex(0x0011, 25)
    SetChrSubChip(0x0011, 1)
    SetChrPos(0x0011, -600, 200, 2900, 0)
    SetChrPos(0x000D, -9600, 800, 1100, 0)
    SetChrPos(0x0014, -9950, 800, 1250, 0)
    SetChrPos(0x000E, -8100, 800, 1100, 0)
    SetChrPos(0x0013, -8500, 800, 1250, 0)
    SetChrPos(0x000F, -8600, 800, 100, 0)
    SetChrPos(0x0015, -8100, 800, 290, 0)
    SetChrPos(0x0016, -9450, 800, 600, 0)
    SetChrPos(0x000C, -640, 600, 4330, 0)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    LoadEffect(0x00, 'map\\\\mpsmk0.eff')
    LoadEffect(0x01, 'map\\\\mp068_00.eff')
    SetChrFlags(0x0101, 0x0004)
    SetChrPos(0x0101, -8290, 200, -480, 0)
    SetChrChipByIndex(0x0101, 12)
    SetChrPos(0x0008, -9790, 200, 2290, 180)
    SetChrChipByIndex(0x0008, 13)
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0012, -1570, 0, 2810, 90)
    SetChrChipByIndex(0x0012, 14)
    ClearChrFlags(0x0012, 0x0080)
    OP_6D(-1610, 200, 3420, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(338, 0)
    PlayEffect(0x00, 0x00, 0x00FF, -630, 750, 2940, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0x01, 0x00FF, -630, 0, 2940, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    OP_82(0x00, 0x00)
    Sleep(1000)

    OP_8E(0x0012, -1510, 0, 4160, 1000, 0x00)
    OP_8C(0x0012, 90, 400)
    Sleep(300)

    OP_9F(0x000C, 0xFF, 0xFF, 0xFF, 0x00, 0x000000C8)
    SetChrChipByIndex(0x0012, 15)
    SetChrSubChip(0x0012, 3)
    Sleep(300)

    OP_8C(0x0012, 0, 300)
    OP_8C(0x0012, 270, 300)

    @scena.Lambda('lambda_5DA6')
    def lambda_5DA6():
        OP_6D(-8470, 200, 1050, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5DA6)

    @scena.Lambda('lambda_5DBE')
    def lambda_5DBE():
        OP_6E(270, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_5DBE)

    OP_8F(0x0012, -7000, 200, 870, 2000, 0x00)
    Sleep(500)

    SetChrPos(0x000C, -7750, 800, 800, 0)
    OP_9F(0x000C, 0xFF, 0xFF, 0xFF, 0xFF, 0x000000C8)
    SetChrChipByIndex(0x0012, 14)
    Sleep(500)

    OP_62(0x0101, 0x00000000, 1700, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(100)

    OP_62(0x0008, 0x00000000, 1700, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(1000)

    OP_8E(0x0012, -7000, 200, 2100, 1000, 0x00)
    OP_8E(0x0012, -7360, 200, 2100, 1000, 0x00)
    Fade(500)
    SetChrPos(0x0012, -8240, 200, 2200, 180)
    SetChrChipByIndex(0x0012, 16)
    OP_0D()
    Sleep(1000)

    OP_DC()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0010291026V一家三人围在餐桌上的早晨……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F3)
    NewScene('ED6_DT21/T0300._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000A offset: 0x5EEE
@scena.Code('func_0A_5EEE')
def func_0A_5EEE():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0307, 0, 0x1838)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5EFD',
    )

    Call(0, 0x000B)

    Jump('loc_5F01')

    def _loc_5EFD(): pass

    label('loc_5EFD')

    Call(0, 0x000F)

    def _loc_5F01(): pass

    label('loc_5F01')

    Return()

# id: 0x000B offset: 0x5F02
@scena.Code('func_0B_5F02')
def func_0B_5F02():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0306, 5, 0x1835)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6081',
    )

    Fade(1000)
    OP_6D(73010, 0, -730, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0101, 73010, 0, -730, 0)
    OP_0D()
    OP_22(0x0074, 0x00, 0x64)
    Sleep(300)

    OP_22(0x0074, 0x00, 0x64)
    Sleep(500)

    FadeOut(300, 0, 100)
    SetChrName('')

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

    ChrTalk(
        0x0101,
        (
            '#0010291120V#293F#6P啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291121V这个房间\n',
            '是做什么的呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291122V#296F嗯……～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1000)

    OP_63(0x0101)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010291123V#291F#6P……不知道呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291124V#290F去找爸爸和妈妈\n',
            '问问看吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1835)

    Jump('loc_60F7')

    def _loc_6081(): pass

    label('loc_6081')

    OP_22(0x0074, 0x00, 0x64)
    Sleep(300)

    OP_22(0x0074, 0x00, 0x64)
    Sleep(500)

    FadeOut(300, 0, 100)
    SetChrName('')

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

    ChrTalk(
        0x0101,
        (
            '#0010291124V#290F去找爸爸和妈妈\n',
            '问问看吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_60F7(): pass

    label('loc_60F7')

    EventEnd(0x00)
    SetMapFlags(0x02000000)

    Return()

# id: 0x000C offset: 0x60FF
@scena.Code('func_0C_60FF')
def func_0C_60FF():
    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0x8, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x05,
        (
            (Expr.GetChrWork, 0x8, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x0008)
    ClearChrFlags(0x0008, 0x0010)
    ChrTurnDirection(0x0008, 0x0000, 0)

    ExecExpressionWithValue(
        0x0008,
        0x04,
        (
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x04,
        (
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0x8, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x05,
        (
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_618F',
    )

    Jump('loc_61D1')

    def _loc_618F(): pass

    label('loc_618F')

    If(
        (
            (Expr.GetChrWork, 0x8, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_61AB',
    )

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_61D1')

    def _loc_61AB(): pass

    label('loc_61AB')

    If(
        (
            (Expr.GetChrWork, 0x8, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_61C7',
    )

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_61D1')

    def _loc_61C7(): pass

    label('loc_61C7')

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.GetChrWork, 0x8, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_61D1(): pass

    label('loc_61D1')

    ExecExpressionWithValue(
        0x0008,
        0x04,
        (
            (Expr.GetChrWork, 0x0, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrFlags(0x0008, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0306, 5, 0x1835)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_64BF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_63FD',
    )

    ChrTalk(
        0x0008,
        (
            '#0160291126V#080F怎么了，艾丝蒂尔？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160291127V果然还是想和爸爸\n',
            '一起玩吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291128V#291F嘿嘿～才不是呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160291129V#083F唉，是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291130V#290F爸爸你在看\n',
            '什么书呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160291131V#084F这本吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160291132V#080F是『各国的游击士协会』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291133V#293F油鸡石～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160291134V#080F这种书对你而言\n',
            '还有些难懂呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160291135V#081F对了，爸爸也像妈妈那样\n',
            '读小人书给你听怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291136V#291F嘿～今天不要啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160291137V#083F是、是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_64BC')

    def _loc_63FD(): pass

    label('loc_63FD')

    ChrTalk(
        0x0008,
        (
            '#0160291138V#085F利贝尔的游击士协会\n',
            '只有格兰赛尔一处。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160291139V如果能在各地都建立支部的话\n',
            '就可以分担军队的压力了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160291140V#082F嗯，等休假结束以后\n',
            '去找摩尔根将军商量一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_64BC(): pass

    label('loc_64BC')

    Jump('loc_6CD7')

    def _loc_64BF(): pass

    label('loc_64BF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0307, 0, 0x1838)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6855',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0306, 6, 0x1836)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_67F6',
    )

    EventBegin(0x00)
    Fade(1000)
    OP_6D(3860, 0, 71420, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0101, 4250, 0, 71160, 285)
    SetChrSubChip(0x0008, 1)
    OP_0D()
    Sleep(200)

    ChrTalk(
        0x0101,
        (
            '#0010291141V#290F#2P喂～爸爸～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291142V２楼最里面的那个房间\n',
            '里面有什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160291143V#080F#6P啊啊，那里\n',
            '只是储物用的房间而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291144V#293F#2P储物？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160291145V#080F#6P就是把平时不经常用的东西\n',
            '堆在里面存放的意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160291146V最近一直都没有进去过，\n',
            '里面也许都结出蜘蛛网了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291147V#296F#2P呼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291148V#290F那门的钥匙\n',
            '放在哪里了啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160291149V#080F#6P啊，那个啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160291150V#084F……等一下。\n',
            '你到那里要做什么啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291151V#291F#2P嗯…………\n',
            '人家想去探险呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160291152V#083F#6P那……就随你高兴吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160291153V#080F钥匙应该被你妈妈\n',
            '收到什么地方去了，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160291154V去问她好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291155V#291F#2P嗯！知道啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_82(0x01, 0x00)
    OP_A2(0x1836)
    EventEnd(0x00)
    SetMapFlags(0x02000000)

    Jump('loc_6852')

    def _loc_67F6(): pass

    label('loc_67F6')

    ChrTalk(
        0x0008,
        (
            '#0160291156V#080F储物室的钥匙应该被你妈妈\n',
            '收到什么地方去了，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160291154V去问她好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6852(): pass

    label('loc_6852')

    Jump('loc_6CD7')

    def _loc_6855(): pass

    label('loc_6855')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0307, 3, 0x183B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_699F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6926',
    )

    ChrTalk(
        0x0008,
        (
            '#0160291158V#080F哦，找到钥匙了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160291159V里面大概已经堆积了很多灰尘了，\n',
            '玩耍时不要把衣服弄得太脏啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160291160V不然妈妈可是会发火的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291161V#291F嗯，我知道啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    Jump('loc_699C')

    def _loc_6926(): pass

    label('loc_6926')

    ChrTalk(
        0x0008,
        (
            '#0160291162V#080F里面大概已经堆积了很多灰尘了，\n',
            '玩耍时不要把衣服弄得太脏啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160291160V不然妈妈可是会发火的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_699C(): pass

    label('loc_699C')

    Jump('loc_6CD7')

    def _loc_699F(): pass

    label('loc_699F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6C6F',
    )

    ChrTalk(
        0x0008,
        (
            '#0160291164V#084F啊，怎么？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160291165V很漂亮的\n',
            '口琴啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291166V#290F这个是在储物室里找到的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291167V不是\n',
            '爸爸的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160291168V#080F啊，不是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160291169V而且好像也不是莱娜的东西，\n',
            '究竟是哪里来的呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160291170V#084F嗯……拿给我看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291171V#293F嗯，给。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔把口琴交给卡西乌斯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#0160291172V#084F利威尔特社……\n',
            '这个东西不是帝国制造的吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160291173V#083F实在想不出来\n',
            '会是谁的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291098V#293F？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '卡西乌斯把口琴还给了艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#0160291175V#080F算了，既然被你发现了，\n',
            '就说明你和它有种缘分，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160291176V有兴趣的话学着吹吹吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291177V#290F嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    Jump('loc_6CD7')

    def _loc_6C6F(): pass

    label('loc_6C6F')

    ChrTalk(
        0x0008,
        (
            '#0160291175V#080F算了，既然被你发现了，\n',
            '就说明你和它有种缘分，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160291176V有兴趣的话学着吹吹吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6CD7(): pass

    label('loc_6CD7')

    SetChrSubChip(0x0008, 0)
    TalkEnd(0x0008)

    Return()

# id: 0x000D offset: 0x6CE0
@scena.Code('func_0D_6CE0')
def func_0D_6CE0():
    TalkBegin(0x0012)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0306, 5, 0x1835)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6EC3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6E3C',
    )

    ChrTalk(
        0x0012,
        (
            '#0700291180V#860F对了，昨天咱们吃的\n',
            '是砂锅……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291181V#861F那…今天晚上\n',
            '就吃煎蛋卷吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291182V#293F真的吗！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291183V#291F哇———太好了！\n',
            '我最喜欢吃妈妈做的\n',
            '煎蛋卷了～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0700291184V#864F哎呀～\n',
            '竟然那么高兴吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291185V#866F呵呵，妈妈和爸爸\n',
            '也都很喜欢那个，\n',
            '真是一家子煎蛋卷爱好者啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    Jump('loc_6EC0')

    def _loc_6E3C(): pass

    label('loc_6E3C')

    ChrTalk(
        0x0012,
        (
            '#0700291186V#865F今天的晚饭是\n',
            '你最爱吃的鸡肉煎蛋卷。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291187V配菜是\n',
            '洋葱奶汁烤菜\n',
            '和野菜沙拉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291188V要多吃一点哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6EC0(): pass

    label('loc_6EC0')

    Jump('loc_7249')

    def _loc_6EC3(): pass

    label('loc_6EC3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0306, 6, 0x1836)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6F28',
    )

    ChrTalk(
        0x0012,
        (
            '#0700291189V#860F对不起哦，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291190V妈妈现在要生火了，\n',
            '退后一点好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7249')

    def _loc_6F28(): pass

    label('loc_6F28')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0307, 0, 0x1838)),
            (Expr.TestScenaFlags, ScenaFlag(0x0307, 3, 0x183B)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_70A6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_701B',
    )

    ChrTalk(
        0x0012,
        (
            '#0700291191V#861F呵呵呵，把钥匙\n',
            '找到了啊，真了不起。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291192V#860F在里面不要挪动重物，\n',
            '也别摸看起来很锋利的东西哦，\n',
            '那样可是会受伤的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291193V还有～探险回来以后\n',
            '别忘了洗手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291194V#291F嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    Jump('loc_70A3')

    def _loc_701B(): pass

    label('loc_701B')

    ChrTalk(
        0x0012,
        (
            '#0700291192V#860F在里面不要挪动重物，\n',
            '也别摸看起来很锋利的东西哦，\n',
            '那样可是会受伤的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291193V还有～探险回来以后\n',
            '别忘了洗手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_70A3(): pass

    label('loc_70A3')

    Jump('loc_7249')

    def _loc_70A6(): pass

    label('loc_70A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0307, 3, 0x183B)),
            Expr.Return,
        ),
        'loc_7249',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_71DD',
    )

    ChrTalk(
        0x0012,
        (
            '#0700291197V#864F哎呀……\n',
            '好漂亮的口琴。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291198V#865F难道是在\n',
            '储物室发现的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291199V#291F嘿嘿……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291200V#290F这个是\n',
            '妈妈的东西吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0700291201V#860F不是啊，\n',
            '那个不是妈妈的东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291202V爸爸也是从来\n',
            '不吹口琴的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291203V到底是谁用过的东西呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    Jump('loc_7249')

    def _loc_71DD(): pass

    label('loc_71DD')

    ChrTalk(
        0x0012,
        (
            '#0700291204V#861F呵呵呵～看来你的大冒险\n',
            '成功完成了呀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0700291205V#866F马上就要开饭啦，\n',
            '快去洗手吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7249(): pass

    label('loc_7249')

    TalkEnd(0x0012)

    Return()

# id: 0x000E offset: 0x724D
@scena.Code('func_0E_724D')
def func_0E_724D():
    EventBegin(0x00)
    Fade(1000)
    OP_6D(8940, 0, 68850, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0101, 8950, 0, 68820, 90)
    OP_0D()
    Sleep(200)

    ChrTalk(
        0x0101,
        (
            '#0010291224V#296F#6P嗯嗯……\n',
            '最上面的抽屉是吧… ',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291225V#292F翻啊翻……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291226V#291F啊……找到啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['储物室钥匙']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['储物室钥匙'], 1)
    OP_64(0x01, 0x0001)
    OP_A2(0x1838)
    EventEnd(0x00)
    SetMapFlags(0x02000000)

    Return()

# id: 0x000F offset: 0x7371
@scena.Code('func_0F_7371')
def func_0F_7371():
    EventBegin(0x00)
    Fade(1000)
    OP_6D(73010, 0, -730, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0101, 73010, 0, -730, 0)
    OP_0D()
    OP_22(0x0074, 0x00, 0x64)
    Sleep(300)

    OP_22(0x0074, 0x00, 0x64)
    Sleep(500)

    FadeOut(300, 0, 100)
    SetChrName('')

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
            TXT(0x00, '【使用储物室钥匙】\n'),
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
    Sleep(100)

    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7480',
    )

    OP_22(0x0073, 0x00, 0x64)
    OP_71(0x0004, 0x0010)
    OP_64(0x00, 0x0001)
    OP_A2(0x1839)

    def _loc_7480(): pass

    label('loc_7480')

    EventEnd(0x00)
    SetMapFlags(0x02000000)

    Return()

# id: 0x0010 offset: 0x7488
@scena.Code('func_10_7488')
def func_10_7488():
    EventBegin(0x00)
    SetChrFlags(0x0101, 0x0080)
    OP_6D(71060, 0, 149350, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(31000, 0)
    OP_6E(237, 0)
    FadeIn(1000, 0)
    Sleep(500)

    @scena.Lambda('lambda_74E0')
    def lambda_74E0():
        OP_6D(70550, 0, 144740, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_74E0)

    @scena.Lambda('lambda_74F8')
    def lambda_74F8():
        OP_6E(280, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_74F8)

    @scena.Lambda('lambda_7508')
    def lambda_7508():
        OP_6C(45000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_7508)

    Sleep(1000)

    SetChrPos(0x0101, 70970, 0, 139960, 0)
    ClearChrFlags(0x0101, 0x0080)
    OP_8E(0x0101, 70550, 0, 144740, 2000, 0x00)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010291227V#291F哇……\n',
            '堆放着好多东西啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291228V#293F啊……可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 270, 400)
    Sleep(500)

    OP_8C(0x0101, 90, 400)
    Sleep(500)

    OP_8C(0x0101, 0, 400)
    Sleep(500)

    OP_62(0x0101, 0x00000000, 1700, 0x00, 0x01, 0x000000FA, 0x02)
    OP_22(0x0026, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010291229V#295F真奇怪啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291230V为什么胸口会有这种\n',
            '异样的感觉呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x183A)
    EventEnd(0x00)
    SetMapFlags(0x02000000)

    Return()

# id: 0x0011 offset: 0x7636
@scena.Code('func_11_7636')
def func_11_7636():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0307, 3, 0x183B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_77D5',
    )

    EventBegin(0x00)
    Fade(1000)
    OP_6D(70730, 0, 149460, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(28000, 0)
    OP_6E(233, 0)
    SetChrPos(0x0101, 70540, 0, 147820, 0)
    OP_0D()
    Sleep(1000)

    OP_6F(0x0008, 0)
    OP_70(0x0008, 0x0000000F)
    OP_22(0x002B, 0x00, 0x64)
    OP_73(0x0008)
    Sleep(500)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['口琴']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['口琴'], 1)

    ChrTalk(
        0x0101,
        (
            '#0010291231V#291F哇！真漂亮……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291232V#290F这个……\n',
            '是吹奏的乐器啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291233V要不要试着\n',
            '吹一下呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    SetChrPos(0x0101, 70340, 0, 147390, 0)
    OP_6D(70340, 0, 147390, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()
    OP_64(0x02, 0x0001)
    OP_A2(0x183B)
    EventEnd(0x00)
    SetMapFlags(0x02000000)

    def _loc_77D5(): pass

    label('loc_77D5')

    Return()

# id: 0x0012 offset: 0x77D6
@scena.Code('func_12_77D6')
def func_12_77D6():
    If(
        (
            (Expr.PushValueByIndex, 0x13),
            (Expr.PushLong, 0x3F9),
            Expr.Neq,
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Neq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_77EC',
    )

    Return()

    def _loc_77EC(): pass

    label('loc_77EC')

    SetMapFlags(0x00000080)
    OP_C2()
    Yield()
    EventBegin(0x00)
    Fade(500)
    SetChrChipByIndex(0x0101, 19)
    SetChrSubChip(0x0101, 0)
    OP_0D()
    OP_20(0x000005DC)
    OP_21()
    OP_DB()
    OP_22(0x011B, 0x00, 0x64)

    @scena.Lambda('lambda_7817')
    def lambda_7817():
        OP_99(0x0101, 0x00, 0x07, 0x000005DC)
        Yield()

        Jump('lambda_7817')

    DispatchAsync2(0x0101, 0x0002, lambda_7817)

    Sleep(10000)

    Sleep(2000)

    Sleep(1500)

    Sleep(1500)

    TerminateThread(0x0101, 0x02)
    OP_1D(0x75)
    Fade(500)
    SetChrSubChip(0x0101, 8)
    OP_0D()
    Sleep(500)

    OP_DC()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7901',
    )

    ChrTalk(
        0x0101,
        (
            '#0010291234V#290F声音很好听呢，不过……\n',
            '似乎有些难吹啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291235V#296F可是，真奇怪啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291236V这个声音……\n',
            '总觉得以前在哪里听过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x0101, 65535)
    SetChrSubChip(0x0101, 0)
    OP_0D()
    OP_A2(0x0006)

    Jump('loc_796B')

    def _loc_7901(): pass

    label('loc_7901')

    ChrTalk(
        0x0101,
        (
            '#0010291237V#296F这声音……\n',
            '以前在哪里听到过呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291238V就去那个地方吹吹看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x0101, 65535)
    SetChrSubChip(0x0101, 0)
    OP_0D()

    def _loc_796B(): pass

    label('loc_796B')

    EventEnd(0x00)
    SetMapFlags(0x02000000)

    Return()

# id: 0x0013 offset: 0x7973
@scena.Code('func_13_7973')
def func_13_7973():
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
        (0x00000000, 'loc_79F0'),
        (0x00000001, 'loc_79F6'),
        (-1, 'loc_79FC'),
    )

    def _loc_79F0(): pass

    label('loc_79F0')

    OP_A2(0x1200)

    Jump('loc_79FC')

    def _loc_79F6(): pass

    label('loc_79F6')

    OP_A2(0x1201)

    Jump('loc_79FC')

    def _loc_79FC(): pass

    label('loc_79FC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_7A0A',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_7A0E')

    def _loc_7A0A(): pass

    label('loc_7A0A')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_7A0E(): pass

    label('loc_7A0E')

    Return()

# id: 0x0014 offset: 0x7A0F
@scena.Code('func_14_7A0F')
def func_14_7A0F():
    ClearMapFlags(0x00000001)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)

    OP_C9(
        0x00,
        (
            0x0000,
            0x0002,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0003,
            0x0004,
            0x0006,
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

# id: 0x0015 offset: 0x7A61
@scena.Code('func_15_7A61')
def func_15_7A61():
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
        1,
        (
            TXT(0x00, '休息\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7AFA',
    )

    OP_20(0x00000BB8)
    FadeOut(1000, 0, -1)
    Sleep(700)

    OP_22(0x000D, 0x00, 0x64)
    OP_0D()
    SetChrStatus(ChrTable['艾丝蒂尔'], 0xFE, 0)
    SetChrStatus(ChrTable['约修亚'], 0xFE, 0)
    SetChrStatus(ChrTable['雪拉扎德'], 0xFE, 0)
    SetChrStatus(ChrTable['奥利维尔'], 0xFE, 0)
    SetChrStatus(ChrTable['科洛丝'], 0xFE, 0)
    SetChrStatus(ChrTable['阿加特'], 0xFE, 0)
    SetChrStatus(ChrTable['提妲'], 0xFE, 0)
    SetChrStatus(ChrTable['金'], 0xFE, 0)
    Sleep(3500)

    OP_1E()
    FadeIn(1000, 0)
    OP_56(0x00)
    TalkEnd(0x00FF)

    Return()

    def _loc_7AFA(): pass

    label('loc_7AFA')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7B14',
    )

    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

    def _loc_7B14(): pass

    label('loc_7B14')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

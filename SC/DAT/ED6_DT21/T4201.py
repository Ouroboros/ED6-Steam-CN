import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4201_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4201   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '卡西乌斯'),
    TXT(0x02, '雪拉扎德'),
    TXT(0x03, '怪盗布卢布兰'),
    TXT(0x04, '瘦狼瓦鲁特'),
    TXT(0x05, '歼灭天使玲'),
    TXT(0x06, '幻惑之铃露茜奥拉'),
    TXT(0x07, '艾莉茜雅女王'),
    TXT(0x08, '科洛蒂娅公主'),
    TXT(0x09, '基库'),
    TXT(0x0A, '希德中校'),
    TXT(0x0B, '理查德'),
    TXT(0x0C, '亲卫队队员'),
    TXT(0x0D, '亲卫队队员'),
    TXT(0x0E, '亲卫队队员'),
    TXT(0x0F, '亲卫队队员'),
    TXT(0x10, '亲卫队队员'),
    TXT(0x11, '亲卫队队员'),
    TXT(0x12, '亲卫队队员'),
    TXT(0x13, '布卢布兰的短剑'),
    TXT(0x14, '怪盗布卢布兰的残像'),
    TXT(0x15, '怪盗布卢布兰的残像'),
    TXT(0x16, '瘦狼瓦鲁特的残像'),
    TXT(0x17, '瘦狼瓦鲁特的残像'),
    TXT(0x18, '歼灭天使玲的残像'),
    TXT(0x19, '歼灭天使玲的残像'),
    TXT(0x1A, '幻惑之铃露茜奥拉的残像'),
    TXT(0x1B, '幻惑之铃露茜奥拉的残像'),
    TXT(0x1C, '亲卫队队员'),
    TXT(0x1D, '亲卫队队员'),
    TXT(0x1E, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4201.x'
    header.mapIndex       = 1
    header.bgm            = 17
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x793F
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0xFFFFF524,
            dword_04        = 0x00002EE0,
            dword_08        = 0x0000F6E0,
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
        ('ED6_DT07/CH01320._CH', 'ED6_DT07/CH01320P._CP'),
    ]

# id: 0x10002 offset: 0xC2
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
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
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
            direction           = 0,
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
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
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
            npcIndex            = 0x01E1,
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
            npcIndex            = 0x01E1,
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
            npcIndex            = 0x01E1,
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
            npcIndex            = 0x01E1,
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
            npcIndex            = 0x01E1,
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
            npcIndex            = 0x01E1,
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
            npcIndex            = 0x01E1,
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
            npcIndex            = 0x01E1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 4210,
            z                   = 18000,
            y                   = 103250,
            direction           = 183,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            x                   = -4250,
            z                   = 18000,
            y                   = 103250,
            direction           = 181,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
    )

# id: 0x10003 offset: 0x462
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x462
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 27460,
            y           = 11000,
            z           = 81540,
            range       = 32180,
            dword_10    = 0x000034BC,
            dword_14    = 0x0001444C,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000007,
        ),
        ScenaEventData(
            x           = -1730,
            y           = 19160,
            z           = 107150,
            range       = 1680,
            dword_10    = 0x000055E6,
            dword_14    = 0x0001A7A2,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000008,
        ),
        ScenaEventData(
            x           = -32759,
            y           = 15500,
            z           = 76820,
            range       = -35080,
            dword_10    = 0x00004074,
            dword_14    = 0x000116D4,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000009,
        ),
        ScenaEventData(
            x           = -4630,
            y           = 16000,
            z           = 86040,
            range       = 4660,
            dword_10    = 0x00002EE0,
            dword_14    = 0x00014974,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000001F,
        ),
    )

# id: 0x10005 offset: 0x4E2
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x4E2
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Return,
        ),
        'loc_4EC',
    )

    Jump('loc_525')

    def _loc_4EC(): pass

    label('loc_4EC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_500',
    )

    ClearChrFlags(0x0023, 0x0080)
    ClearChrFlags(0x0024, 0x0080)

    Jump('loc_525')

    def _loc_500(): pass

    label('loc_500')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_514',
    )

    ClearChrFlags(0x0023, 0x0080)
    ClearChrFlags(0x0024, 0x0080)

    Jump('loc_525')

    def _loc_514(): pass

    label('loc_514')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_525',
    )

    ClearChrFlags(0x0023, 0x0080)
    ClearChrFlags(0x0024, 0x0080)

    def _loc_525(): pass

    label('loc_525')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 2, 0x1002)),
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 4, 0x1004)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_551',
    )

    SetChrPos(0x0008, -43230, 16000, 80440, 270)
    SetChrFlags(0x0008, 0x0004)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0008, 0x0001)

    def _loc_551(): pass

    label('loc_551')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_570',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x72),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 0x000A)

    Jump('loc_5DA')

    def _loc_570(): pass

    label('loc_570')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_597',
    )

    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    SetChrPos(0x0101, 29990, 10500, 78720, 0)
    Event(0, 0x0006)

    Jump('loc_5DA')

    def _loc_597(): pass

    label('loc_597')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Return,
        ),
        'loc_5B3',
    )

    SetMapFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2C),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, 0x002E)

    Jump('loc_5DA')

    def _loc_5B3(): pass

    label('loc_5B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 3, 0x10F3)),
            Expr.Return,
        ),
        'loc_5C9',
    )

    OP_A3(0x10F3)
    SetMapFlags(0x10000000)
    Event(0, 0x000C)

    Jump('loc_5DA')

    def _loc_5C9(): pass

    label('loc_5C9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 2, 0x1002)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 3, 0x1003)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5DA',
    )

    Event(0, 0x0005)

    def _loc_5DA(): pass

    label('loc_5DA')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0001 offset: 0x5E5
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_601',
    )

    OP_B1('t4201_y')

    Jump('loc_60A')

    def _loc_601(): pass

    label('loc_601')

    OP_B1('t4201_n')

    def _loc_60A(): pass

    label('loc_60A')

    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_72(0x0002, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Return,
        ),
        'loc_62A',
    )

    OP_6F(0x0002, 0)

    Jump('loc_642')

    def _loc_62A(): pass

    label('loc_62A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 3, 0x1623)),
            Expr.Return,
        ),
        'loc_63B',
    )

    OP_6F(0x0002, 450)

    Jump('loc_642')

    def _loc_63B(): pass

    label('loc_63B')

    OP_6F(0x0002, 0)

    def _loc_642(): pass

    label('loc_642')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 2, 0x1002)),
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 4, 0x1004)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_65C',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_22(0x01C3, 0x01, 0x50)

    def _loc_65C(): pass

    label('loc_65C')

    OP_71(0x0001, 0x0004)

    ExecExpressionWithValue(
        0x0010,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Return,
        ),
        'loc_6C3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_68D',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2E),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_696')

    def _loc_68D(): pass

    label('loc_68D')

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2C),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_696(): pass

    label('loc_696')

    SetMapFlags(0x02000000)
    OP_72(0x0003, 0x0010)
    OP_72(0x0003, 0x0020)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 4, 0x203C)),
            Expr.Return,
        ),
        'loc_6B6',
    )

    OP_71(0x0002, 0x0004)
    OP_72(0x0003, 0x0004)

    def _loc_6B6(): pass

    label('loc_6B6')

    OP_77(0xFF, 0xBD, 0xA7, 0x00, 0x00000000)
    Call(0, 0x000B)

    def _loc_6C3(): pass

    label('loc_6C3')

    OP_71(0x0000, 0x0004)

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6E2',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_6EC')

    def _loc_6E2(): pass

    label('loc_6E2')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_6EC(): pass

    label('loc_6EC')

    Return()

# id: 0x0002 offset: 0x6ED
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_702',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('ReInit')

    def _loc_702(): pass

    label('loc_702')

    Return()

# id: 0x0003 offset: 0x703
@scena.Code('func_03_703')
def func_03_703():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_724',
    )

    ChrTalk(
        0x00FE,
        (
            '前边是女王宫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7BE')

    def _loc_724(): pass

    label('loc_724')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_77C',
    )

    ChrTalk(
        0x00FE,
        (
            '女王陛下现在正好\n',
            '在房间里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '刚才好象在谒见室\n',
            '听取了事件相关的报告。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7BE')

    def _loc_77C(): pass

    label('loc_77C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_7BE',
    )

    ChrTalk(
        0x00FE,
        (
            '这不是科洛蒂娅殿下吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '女王陛下现在\n',
            '在房间里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7BE(): pass

    label('loc_7BE')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x7C2
@scena.Code('func_04_7C2')
def func_04_7C2():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_819',
    )

    ChrTalk(
        0x00FE,
        (
            '女王陛下和科洛蒂娅殿下\n',
            '现在不在房间里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我看见\n',
            '她们两位出去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_879')

    def _loc_819(): pass

    label('loc_819')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_866',
    )

    ChrTalk(
        0x00FE,
        (
            '『埃尔赛尤』好像已经\n',
            '换上新的引擎了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真想早点见识一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_879')

    def _loc_866(): pass

    label('loc_866')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_879',
    )

    ChrTalk(
        0x00FE,
        (
            '请进。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_879(): pass

    label('loc_879')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x87D
@scena.Code('func_05_87D')
def func_05_87D():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_E6(0x01)
    OP_A2(0x1000)
    OP_1D(0x11)
    OP_11(0xFF, 0xFF, 0xFF, 0x000059D8, 0x0007C060, 0x00000000)
    SetChrFlags(0x0101, 0x0008)
    OP_77(0xE6, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_6D(10, 12000, 28900, 0)
    OP_67(-10, 3030, -10000, 0)
    OP_6B(4780, 0)
    OP_6C(0, 0)
    OP_6E(280, 0)
    OP_C8(0x0200, 0x0046, 'C_PLAC00._CH', 0x00, 0x0BB8)
    ShowPlaceName('格兰赛尔城')
    FadeIn(2000, 0)
    Sleep(1000)

    @scena.Lambda('lambda_0925')
    def lambda_0925():
        OP_6D(-13000, 16500, 75510, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0925)

    @scena.Lambda('lambda_093D')
    def lambda_093D():
        OP_67(-8000, 5500, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_093D)

    @scena.Lambda('lambda_0955')
    def lambda_0955():
        OP_6C(45000, 12000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0955)

    @scena.Lambda('lambda_0965')
    def lambda_0965():
        OP_6B(6000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0965)

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0003)

    @scena.Lambda('lambda_0984')
    def lambda_0984():
        OP_6D(150, 18500, 104610, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0984)

    @scena.Lambda('lambda_099C')
    def lambda_099C():
        OP_67(0, 7270, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_099C)

    @scena.Lambda('lambda_09B4')
    def lambda_09B4():
        OP_6B(7610, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_09B4)

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0101, 0x0003)
    AddItem(ItemTable['利贝尔王国地图'], 1)
    FadeOut(1500, 0, -1)
    OP_0D()
    NewScene('ED6_DT21/T4221._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0006 offset: 0x9EC
@scena.Code('func_06_9EC')
def func_06_9EC():
    EventBegin(0x00)
    FadeIn(1000, 0)
    OP_8E(0x0101, 29930, 12000, 83150, 5000, 0x00)
    OP_0D()
    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0xA0F
@scena.Code('func_07_A0F')
def func_07_A0F():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 2, 0x1002)),
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 3, 0x1003)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_A97',
    )

    EventBegin(0x00)

    ChrTalk(
        0x0101,
        (
            '#0010190040V#002F（老爸一定知道\n',
            '发生了什么事情……)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190041V(我必须尽快找到他……！)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_90(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_A97(): pass

    label('loc_A97')

    Return()

# id: 0x0008 offset: 0xA98
@scena.Code('func_08_A98')
def func_08_A98():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 2, 0x1002)),
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 3, 0x1003)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_B1E',
    )

    EventBegin(0x00)

    ChrTalk(
        0x0101,
        (
            '#0010190042V#002F（雪拉姐说，\n',
            '老爸去了空中庭园……)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190043V(我必须先找到他……！)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_90(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_B1E(): pass

    label('loc_B1E')

    Return()

# id: 0x0009 offset: 0xB1F
@scena.Code('func_09_B1F')
def func_09_B1F():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 2, 0x1002)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 3, 0x1003)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_B2C',
    )

    Return()

    def _loc_B2C(): pass

    label('loc_B2C')

    EventBegin(0x00)
    TerminateThread(0x0008, 0xFF)
    SetChrSubChip(0x0008, 0)
    ClearMapFlags(0x00000001)

    ChrTalk(
        0x0101,
        (
            '#0010190044V#587F#5P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 0)
    Sleep(200)

    @scena.Lambda('lambda_0B6E')
    def lambda_0B6E():
        OP_6D(-41470, 16000, 79880, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0B6E)

    @scena.Lambda('lambda_0B86')
    def lambda_0B86():
        OP_67(0, 7000, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0B86)

    @scena.Lambda('lambda_0B9E')
    def lambda_0B9E():
        OP_6B(1660, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0B9E)

    @scena.Lambda('lambda_0BAE')
    def lambda_0BAE():
        OP_6C(90000, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0BAE)

    @scena.Lambda('lambda_0BBE')
    def lambda_0BBE():
        OP_6E(532, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_0BBE)

    Sleep(3000)

    ChrTalk(
        0x0008,
        (
            '#0160190045V#1128F#6P艾丝蒂尔吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190046V#002F#6P老、老爸……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_92(0x0101, 0x0008, 0x000007D0, 0x00001770, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010190047V#005F啊，不好了……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160190048V#1125F#6P我知道……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160190049V约修亚他……\n',
            '走了是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_1D(0x1A)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010190050V#580F为、为什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190051V为什么老爸你会知道！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 500)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0160190052V#1122F#6P昨天我参加完军事会议回来时，\n',
            '你已经在床上睡着了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160190053V而桌子上就放着\n',
            '他留下的字条。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160190054V所以，大致情况我已经明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190055V#005F那、那!!!',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190056V那你为什么还在这里\n',
            '优哉游哉的啊！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190057V如果不早点去找约修亚的话──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160190058V#1125F#6P……放弃吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190059V#580F哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160190060V#1122F#6P如果他真想要消失的话，\n',
            '即使是我也不可能找到。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160190061V５年前，在遭遇到他的刺杀时，\n',
            '连我也都陷入了苦战。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190062V#587F……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190063V…………我……直到今天……\n',
            '一直都有个疑问……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190064V约修亚他……到底是什么人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160190065V#1128F#6P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0008, 270, 500)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0160190066V#1125F#6P『噬身之蛇』——\n',
            '集结着一群身份不明者的神秘组织。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160190067V由名为『盟主』的首领所领导，\n',
            '企图让世界陷入黑暗的结社。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160190068V约修亚好像也是此组织的成员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190069V#587F『噬身之蛇』………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160190070V#1122F#6P坦白地说，连游击士协会也\n',
            '无法掌握这个组织的真面目。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160190071V考虑到对社会的影响，\n',
            '一直对他们的存在遮遮掩掩。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160190072V然而，这个组织确实存在着，\n',
            '并企图完成某些不为人知的目的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160190073V……比如，类似这次的政变。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190074V#587F那、那就是说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190075V是那个洛伦斯少尉搞的鬼？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160190076V#1122F#6P嗯，错不了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160190077V不过，与此相关的人\n',
            '绝不仅仅只是那个少尉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160190078V#1125F……从某种意义上来说，\n',
            '约修亚也是他们的协助者之一。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010190079V#580F等、等一下……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190080V这是什么意思！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160190081V#1125F#6P他在留言中写清了事实。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160190082V约修亚在这５年间，\n',
            '一直地把游击士协会的情报\n',
            '提供给那个组织。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160190083V但他却无法察觉到自己的行为，\n',
            '好象受到了某些类似催眠术的心理暗示。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190084V#587F怎么会……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190085V#588F怎么会这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 500)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0160190086V#1122F#6P调查这个组织，不是你的力量能做到的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160190087V因此，不要再进一步介入了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190088V#004F…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190089V#586F啊……\n',
            '这是…什么意思……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190090V难道……\n',
            '老爸的意思是说不要管约修亚了吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160190091V#1122F#6P…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190092V#005F#3S喂！老爸！回答我！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160190093V#1125F#6P我早就知道……\n',
            '这一天迟早会到来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160190094V在５年前，约修亚\n',
            '被我收为养子之时就知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160190095V他曾经和我做过一个约定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190096V#587F什么约定……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160190097V#1122F#6P当他认为自己的存在\n',
            '会给我们带来困扰的时候……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160190098V当他以某种形式重新接触到\n',
            '自己身在结社的那段过去时……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160190099V他便会从我们的面前消失。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190100V#587F…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190101V………………怎么会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160190102V#1128F#6P你的心情我能体会……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160190103V同一屋檐下生活了多年的家人突然消失，\n',
            '自然不可能那么简单就割舍掉吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160190104V#1125F但是……\n',
            '男人心中总会有一条不能退让的底线。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160190105V#1122F所以，你也要理解\n',
            '约修亚的心情──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190106V#586F……你明明知道的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160190107V#1122F#6P什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190108V#586F你明明早就知道……\n',
            '约修亚总有一天会\n',
            '从我们的面前消失……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190109V老爸……你明明早就知道的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160190110V#1128F#6P…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160190111V#1125F………对不起……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x0009, -23950, 14000, 71460, 270)
    ClearChrFlags(0x0009, 0x0080)
    SetChrFlags(0x0009, 0x0040)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010190112V#583F#4S老爸是大笨蛋！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    CloseMessageWindow()
    OP_8C(0x0101, 90, 800)

    @scena.Lambda('lambda_19AA')
    def lambda_19AA():
        OP_8E(0x0101, -30490, 14000, 69770, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_19AA)

    @scena.Lambda('lambda_19C5')
    def lambda_19C5():
        OP_6D(-32960, 16000, 72720, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_19C5)

    @scena.Lambda('lambda_19DD')
    def lambda_19DD():
        OP_67(0, 7000, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_19DD)

    @scena.Lambda('lambda_19F5')
    def lambda_19F5():
        OP_8E(0x0009, -29800, 14000, 71060, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_19F5)

    WaitForThreadExit(0x0009, 0x0000)

    @scena.Lambda('lambda_1A15')
    def lambda_1A15():
        OP_8E(0x0009, -32210, 15500, 73820, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1A15)

    Sleep(1000)

    @scena.Lambda('lambda_1A35')
    def lambda_1A35():
        OP_8E(0x0101, -14590, 14000, 75920, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_1A35)

    WaitForThreadExit(0x0009, 0x0001)
    OP_8C(0x0009, 225, 400)
    OP_8C(0x0009, 135, 400)
    Sleep(1000)

    Sleep(1000)

    OP_8C(0x0009, 90, 400)
    Sleep(2000)

    ChrTurnDirection(0x0009, 0x0008, 400)

    @scena.Lambda('lambda_1A80')
    def lambda_1A80():
        OP_6D(-40820, 16000, 79520, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1A80)

    @scena.Lambda('lambda_1A98')
    def lambda_1A98():
        OP_67(0, 7000, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1A98)

    OP_8E(0x0009, -40010, 16000, 78280, 2000, 0x00)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0030190113V#522F#5P老师……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160190114V#1122F#6P雪拉扎德……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160190115V被你看到了难堪的场面啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030190116V#522F#5P不会…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030190117V……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160190118V#1128F#6P不想斥责我几句吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030190119V#524F#5P我也……经历过类似的事情，\n',
            '当时全靠老师的开导才重新振作……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030190120V所以，老师和约修亚的心情\n',
            '我都完全可以理解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160190121V#1125F#6P是吗……这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030190122V#025F#5P但是，站在女性的立场上，\n',
            '我还有一句话想说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0160190123V#1124F#6P哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030190124V#022F#5P老师和约修亚，你们都好差劲！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_24(0x01C3, 0x3C)
    Sleep(200)

    OP_24(0x01C3, 0x32)
    Sleep(200)

    OP_24(0x01C3, 0x28)
    OP_0D()
    SetMapFlags(0x02000000)
    NewScene('ED6_DT21/T4103._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000A offset: 0x1D2C
@scena.Code('func_0A_1D2C')
def func_0A_1D2C():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_DB()
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    SetChrPos(0x0000, 6360, 12000, 92750, 0)
    OP_6D(-1460, 12000, 55280, 0)
    OP_67(0, 6480, -10000, 0)
    OP_6B(9570, 0)
    OP_6C(21000, 0)
    OP_6E(350, 0)
    OP_12(0x00007D00, 0x00061A80, 0x00000000)
    OP_C8(0x0200, 0x0046, 'C_PLAC00._CH', 0x00, 0x0BB8)
    ShowPlaceName('格兰赛尔城')
    FadeIn(2000, 0)
    OP_12(0x00007D00, 0x000493E0, 0x00002710)

    @scena.Lambda('lambda_1DE5')
    def lambda_1DE5():
        OP_6D(750, 20000, 110490, 10000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_1DE5)

    @scena.Lambda('lambda_1DFD')
    def lambda_1DFD():
        OP_67(0, 6120, -10000, 10000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_1DFD)

    Sleep(1000)

    Sleep(1000)

    @scena.Lambda('lambda_1E1F')
    def lambda_1E1F():
        OP_6B(8280, 8000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_1E1F)

    @scena.Lambda('lambda_1E2F')
    def lambda_1E2F():
        OP_6C(33000, 8000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_1E2F)

    @scena.Lambda('lambda_1E3F')
    def lambda_1E3F():
        OP_6E(247, 8000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_1E3F)

    WaitForThreadExit(0x0000, 0x0000)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_DC()
    SetMapFlags(0x02000000)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/T4220._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000B offset: 0x1E6C
@scena.Code('func_0B_1E6C')
def func_0B_1E6C():
    LoadEffect(0x01, 'map\\\\mpsmk0.eff')
    LoadEffect(0x02, 'map\\\\mpfire2.eff')
    LoadEffect(0x03, 'map\\\\mpkaji0.eff')
    OP_22(0x0087, 0x01, 0x46)
    OP_22(0x00AE, 0x01, 0x46)
    PlayEffect(0x03, 0xFF, 0x00FF, -170, 12000, 68500, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x00FF, 30580, 16500, 91210, 0, 0, 0, 1500, 1600, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x00FF, 6310, 22500, 89250, 0, 0, 0, 1200, 1200, 1200, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x00FF, 16200, 15000, 54000, 0, 0, 0, 1400, 1800, 1400, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x00FF, -21680, 15000, 54280, 0, 0, 0, 1500, 1900, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x00FF, -40400, 20400, 74600, 0, 0, 0, 1500, 1800, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x00FF, -24100, 16700, 90680, 0, 0, 0, 1300, 1500, 1300, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x02, 0xFF, 0x00FF, 30580, 16000, 91210, 0, 0, 0, 2200, 2200, 2200, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x02, 0xFF, 0x00FF, 6310, 21950, 89250, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x02, 0xFF, 0x00FF, -40400, 19900, 74600, 0, 0, 0, 1900, 1900, 1900, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x02, 0xFF, 0x00FF, -24100, 16300, 90680, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)

    Return()

# id: 0x000C offset: 0x20F6
@scena.Code('func_0C_20F6')
def func_0C_20F6():
    EventBegin(0x00)
    OP_D2(0x002701C9, 0x002701CE, 0x03)
    OP_D2(0x00270267, 0x00270271, 0x04)
    OP_D2(0x002701C6, 0x002701CB, 0x05)
    OP_D2(0x00260052, 0x00260057, 0x06)
    OP_D2(0x00260003, 0x00260008, 0x07)
    OP_D2(0x0027023F, 0x00270249, 0x08)
    OP_D2(0x002701C8, 0x002701CD, 0x09)
    OP_D2(0x00270253, 0x0027025D, 0x0A)
    OP_D2(0x000600E8, 0x000600ED, 0x0B)
    OP_D2(0x000600E7, 0x000600EC, 0x0C)
    OP_D2(0x002601BC, 0x002601C1, 0x0D)
    OP_D2(0x002600A0, 0x002600A5, 0x22)
    SetChrChipByIndex(0x000C, 7)
    SetChrChipByIndex(0x000A, 3)
    SetChrChipByIndex(0x000B, 5)
    SetChrChipByIndex(0x000D, 9)
    SetChrPos(0x000A, 8600, 14000, 79010, 270)
    SetChrPos(0x000C, 9600, 14000, 77740, 270)
    SetChrPos(0x000D, 9800, 14000, 80570, 270)
    SetChrPos(0x000B, 10800, 14000, 79250, 270)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    OP_6D(8029, 14000, 79890, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(3400, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    LoadEffect(0x00, 'Craft\\\\cr161_00.eff')
    CreateThread(0x000A, 0x01, 0x00, 0x000D)
    CreateThread(0x000C, 0x01, 0x00, 0x000E)
    CreateThread(0x000D, 0x01, 0x00, 0x000F)
    CreateThread(0x000B, 0x01, 0x00, 0x0010)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_225A')
    def lambda_225A():
        OP_6D(-150, 14000, 82580, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_225A)

    @scena.Lambda('lambda_2272')
    def lambda_2272():
        OP_67(0, 6170, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2272)

    @scena.Lambda('lambda_228A')
    def lambda_228A():
        OP_6C(31000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_228A)

    @scena.Lambda('lambda_229A')
    def lambda_229A():
        OP_6B(3190, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_229A)

    @scena.Lambda('lambda_22AA')
    def lambda_22AA():
        OP_6E(346, 3000)

        ExitThread()

    DispatchAsync(0x000D, 0x0000, lambda_22AA)

    WaitForThreadExit(0x000D, 0x0001)
    Sleep(1000)

    OP_6D(730, 20000, 109310, 4000)
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0170380331V#230F#5P呼……\n',
            '那好象就是女王宫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0210380332V#240F#1P也就是终点呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    OP_6D(730, 14000, 82590, 0)
    OP_67(0, 4900, -10000, 0)
    OP_6B(2830, 0)
    OP_6C(32000, 0)
    OP_6E(319, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000B,
        (
            '#0200380333V#250F#6P真是不费吹灰之力……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200380334V只有那个老头子\n',
            '还算有点实力吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000D, 270, 400)

    ChrTalk(
        0x000D,
        (
            '#0210380335V#241F#2P呵呵，确实……\n',
            '相当厉害的高手呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000C, 90, 400)

    ChrTalk(
        0x000C,
        (
            '#0220380336V#269F#6P但想独自抵抗咱们四个人，\n',
            '完全不可能有任何胜算嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220380337V#263F真是，做傻事也要适可而止啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000A, 225, 400)

    ChrTalk(
        0x000A,
        (
            '#0170380338V#230F#5P呵呵，话也不能这么说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170380339V所谓的高贵和忠义\n',
            '就是指他这样的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170380340V#231F另外那个杜南公爵\n',
            '好像也和传闻中的有很大不同啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0210380341V#244F#2P是啊，并不像是个\n',
            '放荡怯懦的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210380342V#240F虽然只是轻轻碰一下\n',
            '就晕过去了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0013, 12)
    SetChrChipByIndex(0x0014, 12)
    SetChrChipByIndex(0x0015, 12)
    SetChrChipByIndex(0x0016, 12)
    SetChrChipByIndex(0x0017, 12)
    SetChrChipByIndex(0x0018, 12)
    SetChrChipByIndex(0x0019, 12)
    SetChrPos(0x0013, 380, 20000, 112380, 180)
    SetChrPos(0x0014, 380, 20000, 113380, 180)
    SetChrPos(0x0015, 380, 20000, 111380, 180)
    SetChrPos(0x0016, 380, 20000, 112380, 180)
    SetChrPos(0x0017, 380, 20000, 112380, 180)
    SetChrPos(0x0018, 380, 20000, 113380, 180)
    SetChrPos(0x0019, 380, 20000, 111380, 180)

    ChrTalk(
        0x0013,
        (
            '#4270380343V#4P来、来了……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(50)

    OP_62(0x000B, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x000D, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(50)

    OP_62(0x000C, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    Fade(500)
    OP_6D(550, 20000, 108990, 0)
    OP_67(0, 5640, -10000, 0)
    OP_6B(2830, 0)
    OP_6C(31000, 0)
    OP_6E(319, 0)

    @scena.Lambda('lambda_270D')
    def lambda_270D():
        OP_6D(250, 18000, 102900, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_270D)

    CreateThread(0x0013, 0x01, 0x00, 0x0011)
    Sleep(100)

    CreateThread(0x0014, 0x01, 0x00, 0x0012)
    Sleep(400)

    CreateThread(0x0015, 0x01, 0x00, 0x0013)
    Sleep(100)

    CreateThread(0x0016, 0x01, 0x00, 0x0014)
    Sleep(400)

    CreateThread(0x0017, 0x01, 0x00, 0x0015)
    Sleep(100)

    CreateThread(0x0018, 0x01, 0x00, 0x0016)
    Sleep(100)

    CreateThread(0x0019, 0x01, 0x00, 0x0017)
    WaitForThreadExit(0x0013, 0x0001)
    WaitForThreadExit(0x0014, 0x0001)
    WaitForThreadExit(0x0015, 0x0001)
    WaitForThreadExit(0x0016, 0x0001)
    WaitForThreadExit(0x0017, 0x0001)
    WaitForThreadExit(0x0018, 0x0001)
    WaitForThreadExit(0x0019, 0x0001)

    ChrTalk(
        0x0018,
        (
            '#4280380344V#5P唔……\n',
            '如果尤莉亚队长在就好了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#2690380345V#5P别说丧气话！\n',
            '拿出亲卫队的气势来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    OP_6D(730, 14000, 82590, 0)
    OP_67(0, 4900, -10000, 0)
    OP_6B(2830, 0)
    OP_6C(32000, 0)
    OP_6E(319, 0)
    OP_8C(0x000D, 0, 0)
    OP_8C(0x000C, 0, 0)
    OP_8C(0x000A, 0, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000B,
        (
            '#0200380346V#254F#6P哼……一帮杂鱼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0210380347V#244F#4P……还真扫兴啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000C, 90, 400)
    Sleep(300)

    ChrTalk(
        0x000C,
        (
            '#0220380348V#261F#6P呵呵，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220380349V#1306F不如我们来比赛好了，\n',
            '看看是谁先抓到女王陛下？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_292A')
    def lambda_292A():
        OP_8C(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_292A)

    @scena.Lambda('lambda_2938')
    def lambda_2938():
        OP_8C(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_2938)

    WaitForThreadExit(0x000A, 0x0001)
    Sleep(300)

    ChrTalk(
        0x000A,
        (
            '#0170380350V#231F#5P哦～！这倒是挺有意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0200380351V#252F哈哈哈，我当然奉陪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0210380352V#241F#2P那么──我们就开始吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_29DB')
    def lambda_29DB():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_29DB)

    Sleep(100)

    @scena.Lambda('lambda_29EE')
    def lambda_29EE():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_29EE)

    Sleep(100)

    OP_8C(0x000C, 0, 400)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearMapFlags(0x00000010)

    @scena.Lambda('lambda_2A16')
    def lambda_2A16():
        OP_6D(390, 19000, 105520, 3500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2A16)

    OP_7D(0x00, 0x000A, 0x000A, 0x0064)
    OP_7D(0x00, 0x000B, 0x000A, 0x0064)
    OP_7D(0x00, 0x000C, 0x000A, 0x0064)
    OP_7D(0x00, 0x000D, 0x000A, 0x0064)
    SetChrChipByIndex(0x000A, 4)

    @scena.Lambda('lambda_2A53')
    def lambda_2A53():
        OP_8E(0x00FE, 490, 19250, 106160, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_2A53)

    Sleep(100)

    SetChrChipByIndex(0x000C, 8)

    @scena.Lambda('lambda_2A78')
    def lambda_2A78():
        OP_8E(0x00FE, -1260, 19250, 106160, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_2A78)

    Sleep(100)

    SetChrChipByIndex(0x000D, 10)

    @scena.Lambda('lambda_2A9D')
    def lambda_2A9D():
        OP_8E(0x00FE, 1300, 19250, 106160, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_2A9D)

    Sleep(100)

    SetChrSubChip(0x000B, 2)
    SetChrChipByIndex(0x000B, 6)
    SetChrFlags(0x000B, 0x0020)

    @scena.Lambda('lambda_2ACC')
    def lambda_2ACC():
        OP_8E(0x00FE, -470, 19250, 106160, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_2ACC)

    CreateThread(0x0013, 0x01, 0x00, 0x0018)
    Sleep(100)

    CreateThread(0x0014, 0x01, 0x00, 0x0019)
    Sleep(100)

    CreateThread(0x0015, 0x01, 0x00, 0x001A)
    Sleep(100)

    CreateThread(0x0016, 0x01, 0x00, 0x001B)
    Sleep(100)

    CreateThread(0x0017, 0x01, 0x00, 0x001C)
    Sleep(100)

    CreateThread(0x0018, 0x01, 0x00, 0x001D)
    Sleep(100)

    CreateThread(0x0019, 0x01, 0x00, 0x001E)
    Sleep(1500)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_7D(0x01, 0x000A, 0x0000, 0x0000)
    OP_7D(0x01, 0x000C, 0x0000, 0x0000)
    OP_7D(0x01, 0x000B, 0x0000, 0x0000)
    OP_7D(0x01, 0x000D, 0x0000, 0x0000)
    OP_A2(0x10F1)
    NewScene('ED6_DT21/T4210._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000D offset: 0x2B6D
@scena.Code('func_0D_2B6D')
def func_0D_2B6D():
    OP_8E(0x00FE, 10, 14000, 80960, 2000, 0x00)
    OP_8E(0x00FE, -180, 14000, 82400, 2000, 0x00)

    Return()

# id: 0x000E offset: 0x2B96
@scena.Code('func_0E_2B96')
def func_0E_2B96():
    OP_8E(0x00FE, -1550, 14000, 80000, 2000, 0x00)
    OP_8E(0x00FE, -1550, 14000, 81170, 2000, 0x00)
    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x000F offset: 0x2BC6
@scena.Code('func_0F_2BC6')
def func_0F_2BC6():
    OP_8E(0x00FE, 1280, 14000, 81390, 2000, 0x00)
    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x0010 offset: 0x2BE2
@scena.Code('func_10_2BE2')
def func_10_2BE2():
    OP_8E(0x00FE, -270, 14000, 80020, 2000, 0x00)
    OP_8C(0x00FE, 0, 400)
    SetChrChipByIndex(0x000B, 34)
    SetChrSubChip(0x000B, 0)

    Return()

# id: 0x0011 offset: 0x2C08
@scena.Code('func_11_2C08')
def func_11_2C08():
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrFlags(0x00FE, 0x0040)

    @scena.Lambda('lambda_2C23')
    def lambda_2C23():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2C23)

    OP_8E(0x00FE, 90, 18000, 101600, 5000, 0x00)
    OP_8C(0x00FE, 180, 0)
    SetChrSubChip(0x00FE, 1)
    SetChrChipByIndex(0x00FE, 11)

    Return()

# id: 0x0012 offset: 0x2C55
@scena.Code('func_12_2C55')
def func_12_2C55():
    Sleep(200)

    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrFlags(0x00FE, 0x0040)

    @scena.Lambda('lambda_2C75')
    def lambda_2C75():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2C75)

    OP_8E(0x00FE, 920, 20000, 106650, 5000, 0x00)
    OP_8E(0x00FE, 1300, 18000, 100870, 5000, 0x00)
    OP_8C(0x00FE, 180, 0)
    SetChrSubChip(0x00FE, 1)
    SetChrChipByIndex(0x00FE, 11)

    Return()

# id: 0x0013 offset: 0x2CBB
@scena.Code('func_13_2CBB')
def func_13_2CBB():
    Sleep(200)

    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrFlags(0x00FE, 0x0040)

    @scena.Lambda('lambda_2CDB')
    def lambda_2CDB():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2CDB)

    OP_8E(0x00FE, -1080, 20000, 106650, 5000, 0x00)
    OP_8E(0x00FE, -1380, 18000, 100970, 5000, 0x00)
    OP_8C(0x00FE, 180, 0)
    SetChrSubChip(0x00FE, 1)
    SetChrChipByIndex(0x00FE, 11)

    Return()

# id: 0x0014 offset: 0x2D21
@scena.Code('func_14_2D21')
def func_14_2D21():
    Sleep(200)

    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrFlags(0x00FE, 0x0040)

    @scena.Lambda('lambda_2D41')
    def lambda_2D41():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2D41)

    OP_8E(0x00FE, -80, 20000, 106650, 5000, 0x00)
    OP_8E(0x00FE, 1010, 18000, 103310, 5000, 0x00)
    OP_8C(0x00FE, 180, 0)
    SetChrSubChip(0x00FE, 1)
    SetChrChipByIndex(0x00FE, 11)

    Return()

# id: 0x0015 offset: 0x2D87
@scena.Code('func_15_2D87')
def func_15_2D87():
    Sleep(200)

    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrFlags(0x00FE, 0x0040)

    @scena.Lambda('lambda_2DA7')
    def lambda_2DA7():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2DA7)

    OP_8E(0x00FE, -80, 20000, 106650, 5000, 0x00)
    OP_8E(0x00FE, -590, 18000, 102780, 5000, 0x00)
    OP_8C(0x00FE, 180, 0)
    SetChrSubChip(0x00FE, 1)
    SetChrChipByIndex(0x00FE, 11)

    Return()

# id: 0x0016 offset: 0x2DED
@scena.Code('func_16_2DED')
def func_16_2DED():
    Sleep(200)

    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrFlags(0x00FE, 0x0040)

    @scena.Lambda('lambda_2E0D')
    def lambda_2E0D():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2E0D)

    OP_8E(0x00FE, 920, 20000, 107600, 5000, 0x00)
    OP_8E(0x00FE, 2340, 18000, 102960, 5000, 0x00)
    OP_8C(0x00FE, 180, 0)
    SetChrSubChip(0x00FE, 1)
    SetChrChipByIndex(0x00FE, 11)

    Return()

# id: 0x0017 offset: 0x2E53
@scena.Code('func_17_2E53')
def func_17_2E53():
    Sleep(200)

    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrFlags(0x00FE, 0x0040)

    @scena.Lambda('lambda_2E73')
    def lambda_2E73():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2E73)

    OP_8E(0x00FE, -1080, 20000, 107600, 5000, 0x00)
    OP_8E(0x00FE, -1810, 18000, 103410, 5000, 0x00)
    OP_8C(0x00FE, 180, 0)
    SetChrSubChip(0x00FE, 1)
    SetChrChipByIndex(0x00FE, 11)

    Return()

# id: 0x0018 offset: 0x2EB9
@scena.Code('func_18_2EB9')
def func_18_2EB9():
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 12)

    @scena.Lambda('lambda_2EC9')
    def lambda_2EC9():
        OP_94(0x00, 0x00FE, 0x0000, 0x00004E20, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2EC9)

    Sleep(1300)

    OP_22(0x0209, 0x00, 0x64)
    PlayEffect(0x00, 0x00, 0x00FE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_2F1E')
    def lambda_2F1E():
        OP_96(0x00FE, 0xFFFFFD8A, 0x0000399E, 0x00014D8E, 0x00001388, 0x00001B58)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2F1E)

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    Sleep(300)

    TerminateThread(0x00FE, 0x02)
    WaitForThreadExit(0x00FE, 0x0003)
    OP_22(0x020C, 0x00, 0x64)
    SetChrFlags(0x00FE, 0x0020)
    SetChrFlags(0x00FE, 0x0002)
    ClearChrFlags(0x00FE, 0x0001)
    SetChrSubChip(0x00FE, 5)
    SetChrChipByIndex(0x00FE, 13)

    Return()

# id: 0x0019 offset: 0x2F74
@scena.Code('func_19_2F74')
def func_19_2F74():
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 12)

    @scena.Lambda('lambda_2F84')
    def lambda_2F84():
        OP_94(0x00, 0x00FE, 0x0000, 0x00004E20, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2F84)

    Sleep(1300)

    OP_22(0x0209, 0x00, 0x64)
    PlayEffect(0x00, 0x01, 0x00FE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_2FD9')
    def lambda_2FD9():
        OP_96(0x00FE, 0x00000AD2, 0x00003C8C, 0x00015342, 0x00000FA0, 0x00001B58)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2FD9)

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    Sleep(300)

    TerminateThread(0x00FE, 0x02)
    WaitForThreadExit(0x00FE, 0x0003)
    OP_22(0x020C, 0x00, 0x64)
    SetChrFlags(0x00FE, 0x0020)
    SetChrFlags(0x00FE, 0x0002)
    ClearChrFlags(0x00FE, 0x0001)
    SetChrSubChip(0x00FE, 6)
    SetChrChipByIndex(0x00FE, 13)

    Return()

# id: 0x001A offset: 0x302F
@scena.Code('func_1A_302F')
def func_1A_302F():
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 12)

    @scena.Lambda('lambda_303F')
    def lambda_303F():
        OP_94(0x00, 0x00FE, 0x0000, 0x00004E20, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_303F)

    Sleep(1300)

    OP_22(0x0209, 0x00, 0x64)
    PlayEffect(0x00, 0x02, 0x00FE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_3094')
    def lambda_3094():
        OP_96(0x00FE, 0xFFFFE9BC, 0x00004650, 0x00015662, 0x00001770, 0x00001B58)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_3094)

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    Sleep(300)

    TerminateThread(0x00FE, 0x02)
    WaitForThreadExit(0x00FE, 0x0003)
    OP_22(0x020C, 0x00, 0x64)
    SetChrFlags(0x00FE, 0x0020)
    SetChrFlags(0x00FE, 0x0002)
    ClearChrFlags(0x00FE, 0x0001)
    SetChrSubChip(0x00FE, 7)
    SetChrChipByIndex(0x00FE, 13)

    Return()

# id: 0x001B offset: 0x30EA
@scena.Code('func_1B_30EA')
def func_1B_30EA():
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 12)

    @scena.Lambda('lambda_30FA')
    def lambda_30FA():
        OP_94(0x00, 0x00FE, 0x0000, 0x00004E20, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_30FA)

    Sleep(1300)

    OP_22(0x0209, 0x00, 0x64)
    PlayEffect(0x00, 0x03, 0x00FE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_314F')
    def lambda_314F():
        OP_96(0x00FE, 0x00000B72, 0x00004074, 0x000179D0, 0x00000BB8, 0x00001B58)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_314F)

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    Sleep(300)

    TerminateThread(0x00FE, 0x02)
    WaitForThreadExit(0x00FE, 0x0003)
    OP_22(0x020C, 0x00, 0x64)
    SetChrFlags(0x00FE, 0x0020)
    SetChrFlags(0x00FE, 0x0002)
    ClearChrFlags(0x00FE, 0x0001)
    SetChrSubChip(0x00FE, 1)
    SetChrChipByIndex(0x00FE, 13)

    Return()

# id: 0x001C offset: 0x31A5
@scena.Code('func_1C_31A5')
def func_1C_31A5():
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 12)

    @scena.Lambda('lambda_31B5')
    def lambda_31B5():
        OP_94(0x00, 0x00FE, 0x0000, 0x00004E20, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_31B5)

    Sleep(1300)

    OP_22(0x0209, 0x00, 0x64)
    PlayEffect(0x00, 0x04, 0x00FE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_320A')
    def lambda_320A():
        OP_96(0x00FE, 0xFFFFF646, 0x0000445C, 0x000181BE, 0x00001388, 0x00001B58)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_320A)

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    Sleep(300)

    TerminateThread(0x00FE, 0x02)
    WaitForThreadExit(0x00FE, 0x0003)
    OP_22(0x020C, 0x00, 0x64)
    SetChrFlags(0x00FE, 0x0020)
    SetChrFlags(0x00FE, 0x0002)
    ClearChrFlags(0x00FE, 0x0001)
    SetChrSubChip(0x00FE, 6)
    SetChrChipByIndex(0x00FE, 13)

    Return()

# id: 0x001D offset: 0x3260
@scena.Code('func_1D_3260')
def func_1D_3260():
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 12)

    @scena.Lambda('lambda_3270')
    def lambda_3270():
        OP_94(0x00, 0x00FE, 0x0000, 0x00004E20, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3270)

    Sleep(1300)

    OP_22(0x0209, 0x00, 0x64)
    PlayEffect(0x00, 0x05, 0x00FE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_32C5')
    def lambda_32C5():
        OP_96(0x00FE, 0x0000170C, 0x00004650, 0x00017958, 0x00001B58, 0x00001B58)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_32C5)

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    Sleep(300)

    TerminateThread(0x00FE, 0x02)
    WaitForThreadExit(0x00FE, 0x0003)
    OP_22(0x020C, 0x00, 0x64)
    SetChrFlags(0x00FE, 0x0020)
    SetChrFlags(0x00FE, 0x0002)
    ClearChrFlags(0x00FE, 0x0001)
    SetChrSubChip(0x00FE, 5)
    SetChrChipByIndex(0x00FE, 13)

    Return()

# id: 0x001E offset: 0x331B
@scena.Code('func_1E_331B')
def func_1E_331B():
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 12)

    @scena.Lambda('lambda_332B')
    def lambda_332B():
        OP_94(0x00, 0x00FE, 0x0000, 0x00004E20, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_332B)

    Sleep(1300)

    OP_22(0x0209, 0x00, 0x64)
    PlayEffect(0x00, 0x06, 0x00FE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_3380')
    def lambda_3380():
        OP_96(0x00FE, 0x00000BC2, 0x00004650, 0x00018D9E, 0x00001770, 0x00001B58)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_3380)

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    Sleep(300)

    TerminateThread(0x00FE, 0x02)
    WaitForThreadExit(0x00FE, 0x0003)
    OP_22(0x020C, 0x00, 0x64)
    SetChrFlags(0x00FE, 0x0020)
    SetChrFlags(0x00FE, 0x0002)
    ClearChrFlags(0x00FE, 0x0001)
    SetChrSubChip(0x00FE, 3)
    SetChrChipByIndex(0x00FE, 13)

    Return()

# id: 0x001F offset: 0x33D6
@scena.Code('func_1F_33D6')
def func_1F_33D6():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 6, 0x203E)),
            Expr.Ez,
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Neq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_33E8',
    )

    Return()

    def _loc_33E8(): pass

    label('loc_33E8')

    EventBegin(0x00)
    FadeOut(500, 0, -1)
    OP_0D()

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_E9(0x01)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            (Expr.PushValueByIndex, 0xCA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Or,
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_34BC',
    )

    EventBegin(0x00)

    ExecExpressionWithVar(
        0xCA,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_E9(0x00)
    OP_6D(-250, 14000, 82500, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(3400, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0000, -250, 14000, 82500, 0)
    SetChrPos(0x0001, -250, 14000, 82500, 0)
    SetChrPos(0x0002, -250, 14000, 82500, 0)
    SetChrPos(0x0003, -250, 14000, 82500, 0)
    EventEnd(0x00)

    Return()

    def _loc_34BC(): pass

    label('loc_34BC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_34D1',
    )

    Call(0, 0x0038)
    Call(0, 0x0039)

    def _loc_34D1(): pass

    label('loc_34D1')

    OP_6D(460, 14750, 85440, 0)
    OP_67(0, 4790, -10000, 0)
    OP_6B(2410, 0)
    OP_6C(33000, 0)
    OP_6E(359, 0)
    SetChrPos(0x0101, -580, 14750, 85180, 0)
    SetChrPos(0x0102, 670, 14750, 85200, 0)
    SetChrPos(0x00F8, -830, 14250, 84010, 0)
    SetChrPos(0x00F9, 720, 14250, 84140, 0)
    OP_D2(0x002701C9, 0x002701CE, 0x03)
    OP_D2(0x00270268, 0x00270272, 0x04)
    OP_D2(0x002701C6, 0x002701CB, 0x05)
    OP_D2(0x0027022A, 0x00270234, 0x06)
    OP_D2(0x00260003, 0x00260008, 0x07)
    OP_D2(0x00270240, 0x0027024A, 0x08)
    OP_D2(0x002701C8, 0x002701CD, 0x09)
    OP_D2(0x00270254, 0x0027025E, 0x0A)
    OP_D2(0x00070141, 0x00070145, 0x0B)
    OP_D2(0x00260052, 0x00260057, 0x0C)
    OP_D2(0x00070182, 0x00070186, 0x0D)
    OP_D2(0x002702F0, 0x002702FA, 0x0E)
    OP_D2(0x0027026B, 0x00270275, 0x0F)
    OP_D2(0x00260068, 0x0026006D, 0x10)
    OP_D2(0x000704AA, 0x000704AE, 0x11)
    OP_D2(0x00070180, 0x00070184, 0x12)
    OP_D2(0x002702EA, 0x002702F4, 0x13)
    OP_D2(0x002702EB, 0x002702F5, 0x14)
    OP_D2(0x002702EC, 0x002702F6, 0x15)
    OP_D2(0x000702D2, 0x000702D9, 0x16)
    OP_D2(0x000702D3, 0x000702DA, 0x17)
    OP_D2(0x000702D4, 0x000702DB, 0x18)
    OP_D2(0x0007052B, 0x0007052F, 0x19)
    OP_D2(0x00270110, 0x00270120, 0x1A)
    OP_D2(0x00270111, 0x00270121, 0x1B)
    OP_D2(0x00270130, 0x00270140, 0x1C)
    OP_D2(0x00270131, 0x00270141, 0x1D)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000005, 'loc_3679'),
        (0x00000002, 'loc_3690'),
        (0x00000006, 'loc_36A7'),
        (0x00000007, 'loc_36BE'),
        (-1, 'loc_36D5'),
    )

    def _loc_3679(): pass

    label('loc_3679')

    OP_D2(0x00070218, 0x00070224, 0x1E)
    OP_D2(0x00070219, 0x00070225, 0x1F)

    Jump('loc_36D5')

    def _loc_3690(): pass

    label('loc_3690')

    OP_D2(0x000701D0, 0x000701DC, 0x1E)
    OP_D2(0x000701D1, 0x000701DD, 0x1F)

    Jump('loc_36D5')

    def _loc_36A7(): pass

    label('loc_36A7')

    OP_D2(0x00070230, 0x0007023C, 0x1E)
    OP_D2(0x00070231, 0x0007023D, 0x1F)

    Jump('loc_36D5')

    def _loc_36BE(): pass

    label('loc_36BE')

    OP_D2(0x00070248, 0x00070254, 0x1E)
    OP_D2(0x00070249, 0x00070255, 0x1F)

    Jump('loc_36D5')

    def _loc_36D5(): pass

    label('loc_36D5')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000005, 'loc_36EE'),
        (0x00000002, 'loc_3705'),
        (0x00000006, 'loc_371C'),
        (0x00000007, 'loc_3733'),
        (-1, 'loc_374A'),
    )

    def _loc_36EE(): pass

    label('loc_36EE')

    OP_D2(0x00070218, 0x00070224, 0x20)
    OP_D2(0x00070219, 0x00070225, 0x21)

    Jump('loc_374A')

    def _loc_3705(): pass

    label('loc_3705')

    OP_D2(0x000701D0, 0x000701DC, 0x20)
    OP_D2(0x000701D1, 0x000701DD, 0x21)

    Jump('loc_374A')

    def _loc_371C(): pass

    label('loc_371C')

    OP_D2(0x00070230, 0x0007023C, 0x20)
    OP_D2(0x00070231, 0x0007023D, 0x21)

    Jump('loc_374A')

    def _loc_3733(): pass

    label('loc_3733')

    OP_D2(0x00070248, 0x00070254, 0x20)
    OP_D2(0x00070249, 0x00070255, 0x21)

    Jump('loc_374A')

    def _loc_374A(): pass

    label('loc_374A')

    OP_D2(0x002600A0, 0x002600A5, 0x22)
    OP_D2(0x002600AE, 0x002600B3, 0x23)
    OP_D2(0x0026008F, 0x00260094, 0x24)
    LoadEffect(0x00, 'map\\mp009_00.eff')
    LoadEffect(0x04, 'Craft\\cr161_00.eff')
    OP_26(163)
    OP_26(164)
    OP_26(503)
    OP_26(505)
    OP_26(571)
    OP_26(155)
    OP_26(214)
    OP_26(213)
    OP_84(0x01)
    OP_84(0x02)
    OP_0D()
    SetChrChipByIndex(0x000A, 3)
    SetChrChipByIndex(0x000B, 34)
    SetChrChipByIndex(0x000C, 7)
    SetChrChipByIndex(0x000D, 9)
    SetChrChipByIndex(0x000E, 11)
    SetChrChipByIndex(0x000F, 13)
    SetChrPos(0x000C, -1510, 18000, 102060, 180)
    SetChrPos(0x000A, -220, 18000, 100200, 180)
    SetChrPos(0x000B, 890, 18000, 103470, 180)
    SetChrPos(0x000D, 1820, 18000, 101280, 180)
    SetChrPos(0x000E, -290, 18000, 101770, 180)
    SetChrPos(0x000F, 850, 18000, 101660, 180)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    FadeIn(500, 0)
    OP_0D()

    NpcTalk(
        0x000A,
        '男人的声音',
        (
            '#0170380353V#4P哟……是你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000001F4)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_38ED',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_392B')

    def _loc_38ED(): pass

    label('loc_38ED')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3914',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_392B')

    def _loc_3914(): pass

    label('loc_3914')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_392B(): pass

    label('loc_392B')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3957',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_3995')

    def _loc_3957(): pass

    label('loc_3957')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_397E',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_3995')

    def _loc_397E(): pass

    label('loc_397E')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_3995(): pass

    label('loc_3995')

    Sleep(500)

    OP_1D(0x6F)
    Sleep(500)

    @scena.Lambda('lambda_39A7')
    def lambda_39A7():
        OP_6D(850, 18000, 103170, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_39A7)

    @scena.Lambda('lambda_39BF')
    def lambda_39BF():
        OP_67(0, 4930, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_39BF)

    @scena.Lambda('lambda_39D7')
    def lambda_39D7():
        OP_6B(2410, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_39D7)

    @scena.Lambda('lambda_39E7')
    def lambda_39E7():
        OP_6C(23000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_39E7)

    @scena.Lambda('lambda_39F7')
    def lambda_39F7():
        OP_8F(0x00FE, -220, 16000, 92550, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_39F7)

    Sleep(100)

    @scena.Lambda('lambda_3A17')
    def lambda_3A17():
        OP_8F(0x00FE, 970, 16000, 92520, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3A17)

    Sleep(50)

    @scena.Lambda('lambda_3A37')
    def lambda_3A37():
        OP_8F(0x00FE, -260, 16000, 90910, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_3A37)

    Sleep(100)

    @scena.Lambda('lambda_3A57')
    def lambda_3A57():
        OP_8F(0x00FE, 950, 16000, 90910, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_3A57)

    WaitForThreadExit(0x0101, 0x0000)
    Sleep(100)

    ChrTalk(
        0x0101,
        (
            '#0010380354V#1020F#1P科洛丝！　女王陛下！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0101, 26)
    SetChrChipByIndex(0x0102, 28)
    SetChrChipByIndex(0x00F8, 30)
    SetChrChipByIndex(0x00F9, 32)

    ChrTalk(
        0x000F,
        (
            '#0060380355V#403F#5P艾丝蒂尔……\n',
            '……约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0630380356V#093F#5P各位……\n',
            '你们终于来了啊…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3B57',
    )

    ChrTalk(
        0x0107,
        (
            '#0070380357V#065F怎、怎么会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3BE6')

    def _loc_3B57(): pass

    label('loc_3B57')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3B87',
    )

    ChrTalk(
        0x0106,
        (
            '#0050380358V#057F可恶……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3BE6')

    def _loc_3B87(): pass

    label('loc_3B87')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3BB9',
    )

    ChrTalk(
        0x0103,
        (
            '#0030380359V#523F怎么会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3BE6')

    def _loc_3BB9(): pass

    label('loc_3BB9')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3BE6',
    )

    ChrTalk(
        0x0108,
        (
            '#0080380360V#077F可恶……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3BE6(): pass

    label('loc_3BE6')

    ChrTalk(
        0x0102,
        (
            '#0020380361V#1043F……还是没能赶上吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010380362V#1005F#1P你、你们……\n',
            '到底想干什么！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010380363V马上放了科洛丝她们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0220380364V#1306F#5P呵呵，这可不行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220380365V#261F因为教授向我们提了\n',
            '私人性质的请求。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010380366V#1020F#1P教、教授？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020380367V#1042F私人的……\n',
            '就是说和『福音计划』无关吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0220341570V#263F#5P呵呵，应该是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220380369V#1305F各位表现得比\n',
            '预期的要活跃，\n',
            '所以他要想些办法来试验你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010380370V#1019F#1P活、活跃……',
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
        'loc_3E6E',
    )

    ChrTalk(
        0x000B,
        (
            '#0200380371V#252F#5P哼哼，你们恢复了\n',
            '各地的通讯吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200380372V教授似乎对此\n',
            '很是不满哦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200380373V所以就想看看你们\n',
            '手足无措的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3F04')

    def _loc_3E6E(): pass

    label('loc_3E6E')

    ChrTalk(
        0x000D,
        (
            '#0210380374V#244F#5P你们恢复了各地的\n',
            '部分通讯吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210380375V#241F教授似乎对此\n',
            '有些扫兴呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210380376V所以就想看看你们\n',
            '痛苦困惑的样子哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3F04(): pass

    label('loc_3F04')

    ChrTalk(
        0x0101,
        (
            '#0010380377V#1005F#1P…………！\n',
            '开、开什么玩笑！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010380378V难道你们因为这种理由\n',
            '就来袭击王都！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020380379V#1043F……他本来就是这种人。',
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
        'loc_4073',
    )

    ChrTalk(
        0x000D,
        (
            '#0210380380V#244F#5P呵呵……\n',
            '算是恶趣味吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210380381V#241F浮游都市的控制\n',
            '已经交给莱维一个人了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210380382V我们实在闲得太无聊，\n',
            '就接受了教授的提议。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030380383V#022F露茜奥拉姐姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_414B')

    def _loc_4073(): pass

    label('loc_4073')

    ChrTalk(
        0x000B,
        (
            '#0200380384V#250F哼哼……\n',
            '确实是种恶趣味。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200380385V#252F浮游都市的控制\n',
            '全部都交给莱维一人了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200380386V我们几个闲着也是闲着，\n',
            '就来这里运动运动。',
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
        'loc_414B',
    )

    ChrTalk(
        0x0108,
        (
            '#0080380387V#077F瓦鲁特……你这家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_414B(): pass

    label('loc_414B')

    ChrTalk(
        0x000E,
        (
            '#0630380388V#094F#5P……我明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630380389V#093F那么只要我一个人\n',
            '成为阶下囚就行了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630380390V能不能请你们\n',
            '放过科洛蒂娅？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000F, 270, 400)

    ChrTalk(
        0x000F,
        (
            '#0060380391V#402F#2P这样不行，祖母大人！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060380392V要抓的话也应该抓我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0170380393V#230F#5P嗯，教授的要求\n',
            '确实是“只要抓住一个就好”……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170380394V哎呀呀，那该怎么办呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000D, 270, 400)

    ChrTalk(
        0x000D,
        (
            '#0210380395V#243F#2P对了，你不是\n',
            '很迷恋公主殿下吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000A, 90, 400)
    Sleep(300)

    ChrTalk(
        0x000A,
        (
            '#0170380396V#231F#6P呵呵，美丽的鸟儿一旦被囚禁\n',
            '在笼中，就失去了原本的魅力。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170380397V不过我倒是也很想欣赏一下她那\n',
            '身陷在囚笼中也坚韧不屈的气质……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000F, 225, 400)
    Sleep(300)

    ChrTalk(
        0x000F,
        (
            '#0060380398V#402F#5P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010380399V#1022F#1P你、你们……\n',
            '给我适可而止吧！！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010380400V#1005F这种事……\n',
            '我绝不会让你们得逞！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4431')
    def lambda_4431():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_4431)

    Sleep(50)

    @scena.Lambda('lambda_4444')
    def lambda_4444():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_4444)

    Sleep(50)

    @scena.Lambda('lambda_4457')
    def lambda_4457():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_4457)

    ChrTalk(
        0x000B,
        (
            '#0200380401V#252F#5P哼哼，别说笑了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200380402V就算没有人质，\n',
            '你觉得能战胜我们所有人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0220380403V#261F#5P呵呵，上次咱们\n',
            '曾有过约定，再度见面时\n',
            '要把你们杀光，对吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220380404V#1306F现在正是好机会……\n',
            '要不要就在这里开始呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010380405V#1020F#1P可恶……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    OP_6D(670, 16000, 93270, 0)
    OP_67(0, 6120, -10000, 0)
    OP_6B(2310, 0)
    OP_6C(23000, 0)
    OP_6E(359, 0)
    SetChrPos(0x0101, -220, 16000, 92550, 328)
    SetChrPos(0x0102, 970, 16000, 92520, 328)
    SetChrPos(0x00F8, -260, 16000, 90910, 328)
    SetChrPos(0x00F9, 950, 16000, 90910, 328)
    OP_0D()

    ChrTalk(
        0x0102,
        (
            '#0020380406V#1035F#2P（……要克制，艾丝蒂尔。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020380407V#1042F（他说得没错……\n',
            '双方的战斗力确实存在差距。)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020380408V(现在也只有耐心寻找胜机了。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010380409V#1003F#5P（可、可是……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0170380410V#231F#6P呵呵，没用的，约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170380411V凭你的隐形术，或许真的\n',
            '可以发现我们的破绽……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0210380412V#240F#6P但如今你已经现形，\n',
            '再想找出我们的破绽根本是不可能的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210380413V就算是你『漆黑之牙』也一样无能为力了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020380414V#1035F#4P……确实如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020380415V#1040F不过，制造破绽的工作\n',
            '也不一定要我来做啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000003E8)

    ChrTalk(
        0x000A,
        (
            '#0170380416V#232F#6P什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearMapFlags(0x00000010)
    Sleep(100)

    OP_1D(0x2C)
    Sleep(500)

    Fade(500)
    OP_6D(-3840, 18000, 103030, 0)
    OP_67(0, 4650, -10000, 0)
    OP_6B(2680, 0)
    OP_6C(45000, 0)
    OP_6E(330, 0)
    SetChrChipByIndex(0x0011, 21)
    SetChrSubChip(0x0011, 4)
    SetChrPos(0x0011, -14000, 18000, 101730, 90)
    ClearChrFlags(0x0011, 0x0080)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CreateThread(0x0011, 0x00, 0x00, 0x0021)
    Sleep(400)

    CreateThread(0x000C, 0x00, 0x00, 0x0022)

    @scena.Lambda('lambda_48DA')
    def lambda_48DA():
        OP_6D(-2250, 18000, 102720, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_48DA)

    @scena.Lambda('lambda_48F2')
    def lambda_48F2():
        OP_67(0, 4650, -10000, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_48F2)

    @scena.Lambda('lambda_490A')
    def lambda_490A():
        OP_6B(2420, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_490A)

    CreateThread(0x000E, 0x00, 0x00, 0x0024)
    WaitForThreadExit(0x0011, 0x0000)
    WaitForThreadExit(0x000C, 0x0000)
    ClearChrFlags(0x0011, 0x0020)
    ClearChrFlags(0x000C, 0x0020)
    OP_22(0x009B, 0x00, 0x64)
    OP_22(0x00D6, 0x00, 0x64)
    PlayEffect(0x00, 0x00, 0x000C, 0, 0, 500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0x000000C8, 0x000000C8, 0x00000BB8, 0x0000012C)

    @scena.Lambda('lambda_4985')
    def lambda_4985():
        OP_9E(0x00FE, 0x0000001E, 0x00000000, 0x0000012C, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_4985)

    @scena.Lambda('lambda_499F')
    def lambda_499F():
        OP_9E(0x00FE, 0x0000001E, 0x00000000, 0x0000012C, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0011, 0x0003, lambda_499F)

    @scena.Lambda('lambda_49B9')
    def lambda_49B9():
        OP_6E(391, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_49B9)

    @scena.Lambda('lambda_49C9')
    def lambda_49C9():
        OP_96(0x00FE, 0xFFFFFB6E, 0x00004650, 0x00019118, 0x000000C8, 0x00001388)

        ExitThread()

    DispatchAsync(0x000C, 0x0000, lambda_49C9)

    @scena.Lambda('lambda_49E7')
    def lambda_49E7():
        OP_96(0x00FE, 0xFFFFE746, 0x00004650, 0x00018F06, 0x000000C8, 0x00001388)

        ExitThread()

    DispatchAsync(0x0011, 0x0000, lambda_49E7)

    WaitForThreadExit(0x0011, 0x0000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_22(0x00A4, 0x00, 0x64)
    WaitForThreadExit(0x000C, 0x0000)
    OP_22(0x00A4, 0x00, 0x64)
    Sleep(500)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CreateThread(0x000A, 0x00, 0x00, 0x0023)
    Sleep(300)

    SetChrChipByIndex(0x0011, 19)
    SetChrSubChip(0x0011, 0)
    OP_22(0x00A3, 0x00, 0x64)
    OP_7D(0x00, 0x0011, 0x000A, 0x0064)
    OP_96(0x0011, 0xFFFFE57A, 0x00004650, 0x000188DA, 0x000000C8, 0x00001770)
    OP_7D(0x01, 0x0011, 0x0000, 0x0000)
    OP_22(0x00A4, 0x00, 0x64)
    WaitForThreadExit(0x0101, 0x0003)
    WaitForThreadExit(0x000A, 0x0000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010380417V#1004F#1P哎……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0011,
        (
            '#0620380418V#701F#5P哟，大家辛苦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620380419V#703F──陛下、殿下。\n',
            '我来晚了，请恕罪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_6D(-1270, 18000, 103090, 800)

    ChrTalk(
        0x000F,
        (
            '#0060380420V#409F#2P希德中校……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0630380421V#090F#2P……你来得正好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(225)
    OP_22(0x00D5, 0x00, 0x64)
    SetChrChipByIndex(0x000A, 15)
    SetChrSubChip(0x000A, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0170380422V#230F#2P喔……\n',
            '是『剑圣』的传人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0220380423V#1306F#5P呵呵……真可惜。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220380424V只差一点点就能\n',
            '抓住玲的破绽了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0620380425V#701F嗯，我确实很受打击啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620380426V#703F没想到全力施展的偷袭\n',
            '都奈何不了你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0200380427V#252F#5P哼哼，已经算是不错了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200380428V难得的好机会，不如和我们\n',
            '好好玩一玩吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0620380429V#703F多谢你的好意，不过不必了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620380430V#701F我的任务不过只是\n',
            '吸引你们的注意力而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0200380431V#254F#5P什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0210380432V#242F！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0010, 18)
    SetChrPos(0x0010, -15190, 21000, 88030, 45)
    SetChrFlags(0x0010, 0x0040)
    ClearChrFlags(0x0010, 0x0080)
    OP_22(0x0197, 0x00, 0x64)
    OP_22(0x008C, 0x00, 0x64)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6D(-2590, 18000, 100370, 800)
    CreateThread(0x0010, 0x00, 0x00, 0x0028)

    @scena.Lambda('lambda_4DE0')
    def lambda_4DE0():
        OP_6D(2640, 18000, 103890, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_4DE0)

    @scena.Lambda('lambda_4DF8')
    def lambda_4DF8():
        OP_67(0, 6720, -10000, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4DF8)

    @scena.Lambda('lambda_4E10')
    def lambda_4E10():
        OP_6B(2170, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4E10)

    @scena.Lambda('lambda_4E20')
    def lambda_4E20():
        OP_6C(21000, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_4E20)

    WaitForThreadExit(0x0010, 0x0001)
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x000D,
        (
            '#0210380433V#245F#5P…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0012, 0x00, 0x00, 0x0029)

    @scena.Lambda('lambda_4E63')
    def lambda_4E63():
        OP_6D(1730, 18750, 105300, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_4E63)

    @scena.Lambda('lambda_4E7B')
    def lambda_4E7B():
        OP_67(0, 6520, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4E7B)

    @scena.Lambda('lambda_4E93')
    def lambda_4E93():
        OP_6B(2170, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4E93)

    @scena.Lambda('lambda_4EA3')
    def lambda_4EA3():
        OP_6C(45000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_4EA3)

    WaitForThreadExit(0x0012, 0x0000)
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x000B,
        (
            '#0200380434V#259F#6P哼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4EDD')
    def lambda_4EDD():
        OP_6D(-2940, 18610, 101150, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_4EDD)

    @scena.Lambda('lambda_4EF5')
    def lambda_4EF5():
        OP_6B(2860, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4EF5)

    @scena.Lambda('lambda_4F05')
    def lambda_4F05():
        OP_6E(300, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4F05)

    Sleep(1000)

    CreateThread(0x0011, 0x00, 0x00, 0x0025)
    WaitForThreadExit(0x0011, 0x0000)
    OP_22(0x00A3, 0x00, 0x64)
    OP_7D(0x00, 0x000C, 0x0032, 0x0064)
    OP_7D(0x00, 0x000A, 0x0032, 0x0064)

    @scena.Lambda('lambda_4F3B')
    def lambda_4F3B():
        OP_8C(0x00FE, 180, 600)

        ExitThread()

    DispatchAsync(0x000C, 0x0000, lambda_4F3B)

    @scena.Lambda('lambda_4F49')
    def lambda_4F49():
        OP_96(0x00FE, 0xFFFFF90C, 0x0000474A, 0x00019668, 0x000001F4, 0x00001388)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_4F49)

    @scena.Lambda('lambda_4F67')
    def lambda_4F67():
        OP_8C(0x00FE, 0, 600)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_4F67)

    @scena.Lambda('lambda_4F75')
    def lambda_4F75():
        OP_96(0x00FE, 0xFFFFF98E, 0x00004650, 0x00018632, 0x000001F4, 0x00001388)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_4F75)

    WaitForThreadExit(0x000C, 0x0001)
    WaitForThreadExit(0x000A, 0x0001)

    ChrTalk(
        0x000A,
        (
            '#0170380435V#235F#10A#4P唔……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x000C,
        (
            '#0220380436V#1303F#10A#1P呀……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(800)

    OP_7D(0x00, 0x0011, 0x0032, 0x0064)
    OP_8C(0x0011, 0, 800)
    SetChrChipByIndex(0x0011, 21)

    @scena.Lambda('lambda_4FFF')
    def lambda_4FFF():
        OP_99(0x00FE, 0x00, 0x07, 0x000009C4)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_4FFF)

    @scena.Lambda('lambda_500F')
    def lambda_500F():
        OP_96(0x00FE, 0xFFFFF808, 0x00004650, 0x0001930C, 0x00000064, 0x00001388)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_500F)

    Sleep(200)

    OP_22(0x01F9, 0x00, 0x64)
    OP_22(0x00A3, 0x00, 0x64)

    @scena.Lambda('lambda_503C')
    def lambda_503C():
        OP_96(0x00FE, 0xFFFFFA06, 0x00004D26, 0x0001A2D4, 0x000007D0, 0x00001388)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_503C)

    WaitForThreadExit(0x0011, 0x0001)
    WaitForThreadExit(0x000C, 0x0001)
    SetChrChipByIndex(0x0011, 21)
    SetChrSubChip(0x0011, 0)
    OP_8C(0x0011, 180, 800)

    @scena.Lambda('lambda_5075')
    def lambda_5075():
        OP_99(0x00FE, 0x00, 0x07, 0x000009C4)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_5075)

    @scena.Lambda('lambda_5085')
    def lambda_5085():
        OP_96(0x00FE, 0xFFFFF93E, 0x00004650, 0x000189DE, 0x00000064, 0x00001388)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_5085)

    Sleep(200)

    OP_22(0x00A3, 0x00, 0x64)
    OP_22(0x01F9, 0x00, 0x64)
    OP_7D(0x00, 0x000A, 0x0032, 0x01F4)
    SetChrChipByIndex(0x000A, 36)

    @scena.Lambda('lambda_50BF')
    def lambda_50BF():
        OP_99(0x00FE, 0x00, 0x07, 0x000005DC)
        Yield()

        Jump('lambda_50BF')

    DispatchAsync2(0x000A, 0x0002, lambda_50BF)

    @scena.Lambda('lambda_50D2')
    def lambda_50D2():
        OP_96(0x00FE, 0xFFFFF920, 0x00005208, 0x00017E08, 0x00000DAC, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_50D2)

    ClearChrFlags(0x000A, 0x0001)
    WaitForThreadExit(0x0011, 0x0001)
    WaitForThreadExit(0x000A, 0x0001)
    OP_7D(0x01, 0x000A, 0x0000, 0x0000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(1000)

    SetChrChipByIndex(0x0011, 21)
    SetChrSubChip(0x0011, 0)

    @scena.Lambda('lambda_511F')
    def lambda_511F():
        ChrTurnDirection(0x00FE, 0x000A, 400)
        Yield()

        Jump('lambda_511F')

    DispatchAsync2(0x0011, 0x0002, lambda_511F)

    CreateThread(0x000A, 0x00, 0x00, 0x002D)
    Sleep(2000)

    ClearChrFlags(0x0012, 0x0020)
    SetChrChipByIndex(0x0012, 23)
    ClearChrFlags(0x0011, 0x0020)
    SetChrChipByIndex(0x0011, 20)

    @scena.Lambda('lambda_5150')
    def lambda_5150():
        OP_8F(0x00FE, 260, 18000, 102200, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_5150)

    @scena.Lambda('lambda_516B')
    def lambda_516B():
        OP_8F(0x00FE, -1220, 18000, 101600, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_516B)

    @scena.Lambda('lambda_5186')
    def lambda_5186():
        OP_8F(0x000E, -670, 18000, 100330, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_5186)

    @scena.Lambda('lambda_51A1')
    def lambda_51A1():
        OP_8F(0x000F, 540, 18000, 100570, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_51A1)

    @scena.Lambda('lambda_51BC')
    def lambda_51BC():
        OP_6D(960, 18500, 104830, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_51BC)

    @scena.Lambda('lambda_51D4')
    def lambda_51D4():
        OP_67(0, 5600, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_51D4)

    @scena.Lambda('lambda_51EC')
    def lambda_51EC():
        OP_6B(2910, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_51EC)

    @scena.Lambda('lambda_51FC')
    def lambda_51FC():
        OP_6C(33000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_51FC)

    @scena.Lambda('lambda_520C')
    def lambda_520C():
        OP_6E(321, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_520C)

    WaitForThreadExit(0x0011, 0x0001)
    SetChrChipByIndex(0x0011, 19)
    SetChrSubChip(0x0011, 0)
    WaitForThreadExit(0x0012, 0x0001)
    SetChrChipByIndex(0x0012, 22)
    SetChrSubChip(0x0012, 0)
    WaitForThreadExit(0x0101, 0x0000)
    OP_7D(0x01, 0x000C, 0x0000, 0x0000)
    OP_7D(0x01, 0x000A, 0x0000, 0x0000)

    NpcTalk(
        0x0012,
        '穿军服的男人',
        (
            '#0130380437V#115F#5P看来我来得正好啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0060380438V#409F你、你是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x0101, 1700, 16000, 92550, 328)
    SetChrPos(0x0102, 2910, 16000, 92520, 328)
    SetChrPos(0x00F8, 1700, 16000, 90910, 328)
    SetChrPos(0x00F9, 2910, 16000, 90910, 328)

    @scena.Lambda('lambda_52F1')
    def lambda_52F1():
        OP_6D(1120, 18500, 104420, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_52F1)

    @scena.Lambda('lambda_5309')
    def lambda_5309():
        OP_67(0, 6140, -10000, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_5309)

    @scena.Lambda('lambda_5321')
    def lambda_5321():
        OP_6B(2360, 2500)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_5321)

    @scena.Lambda('lambda_5331')
    def lambda_5331():
        OP_6E(401, 2500)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_5331)

    SetChrChipByIndex(0x0101, 26)

    @scena.Lambda('lambda_5346')
    def lambda_5346():
        OP_8E(0x00FE, 1700, 18000, 102050, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5346)

    Sleep(100)

    SetChrChipByIndex(0x0102, 28)

    @scena.Lambda('lambda_536B')
    def lambda_536B():
        OP_8E(0x00FE, 2910, 18000, 102070, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_536B)

    Sleep(50)

    SetChrChipByIndex(0x00F8, 30)

    @scena.Lambda('lambda_5390')
    def lambda_5390():
        OP_8E(0x00FE, 1760, 18000, 100500, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_5390)

    Sleep(100)

    SetChrChipByIndex(0x00F9, 32)

    @scena.Lambda('lambda_53B5')
    def lambda_53B5():
        OP_8E(0x00FE, 2860, 18000, 100500, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_53B5)

    WaitForThreadExit(0x0101, 0x0001)
    SetChrChipByIndex(0x0101, 26)
    WaitForThreadExit(0x0102, 0x0001)
    SetChrChipByIndex(0x0102, 28)
    WaitForThreadExit(0x00F8, 0x0001)
    SetChrChipByIndex(0x00F8, 30)
    WaitForThreadExit(0x00F9, 0x0001)
    SetChrChipByIndex(0x00F9, 32)
    WaitForThreadExit(0x0101, 0x0002)

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5424',
    )

    ChrTalk(
        0x0106,
        (
            '#0050380439V#055F喂喂……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5424(): pass

    label('loc_5424')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5451',
    )

    ChrTalk(
        0x0107,
        (
            '#0070380440V#065F啊……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5451(): pass

    label('loc_5451')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5480',
    )

    ChrTalk(
        0x0103,
        (
            '#0030380441V#023F不是吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5480(): pass

    label('loc_5480')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_54AF',
    )

    ChrTalk(
        0x0108,
        (
            '#0080380442V#073F怎么会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_54AF(): pass

    label('loc_54AF')

    ChrTalk(
        0x0101,
        (
            '#0010380443V#1004F#5P理、理、理……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010380444V#1005F#4S#5P理查德上校！？',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0130380445V#111F#5P哈哈……\n',
            '别来无恙吗，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130380446V#110F不过现在的我已经被剥夺了军衔，\n',
            '不过是个服刑中的政治犯罢了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130380447V所以就不要再叫我上校啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010380448V#1019F#5P不、不要叫……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0630380449V#096F#6P理查德先生。\n',
            '……真是好久不见了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0130380450V#115F#5P……陛下和公主殿下\n',
            '能够安康真是太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130380451V#112F我想准将应该已经\n',
            '向您禀报过了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130380452V请允许我暂时以带罪之身，\n',
            '保护陛下和公主脱离逆贼之手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0630380453V#091F#6P呵呵，那是当然的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0060380454V#401F#4P拜托你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0130380455V#111F#5P……荣幸之至。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010380456V#1016F#5P这、这是怎么回事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020380457V#1040F#2P看来在我们不知情的情况下，\n',
            '事态已经有所进展了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0170380458V#232F#6P『剑圣』的两名传人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170380459V再加上『漆黑之牙』和\n',
            '本领高强的游击士们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0210380460V#240F#6P呵呵……\n',
            '看来是稍微有些玩过头了哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0130380461V#115F#6P呼……\n',
            '现在的情势已经逆转了哦，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130380462V#111F顺便一说，街上的那群家伙\n',
            '我们也已经收拾掉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010380463V#1004F#5P咦……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5920')
    def lambda_5920():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5920)

    Sleep(50)

    @scena.Lambda('lambda_5933')
    def lambda_5933():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_5933)

    Sleep(50)

    @scena.Lambda('lambda_5946')
    def lambda_5946():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_5946)

    Sleep(50)

    @scena.Lambda('lambda_5959')
    def lambda_5959():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_5959)

    Sleep(50)

    SetChrFlags(0x000F, 0x0020)

    @scena.Lambda('lambda_5971')
    def lambda_5971():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_5971)

    @scena.Lambda('lambda_597F')
    def lambda_597F():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_597F)

    SetMapFlags(0x02000000)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F2)
    NewScene('ED6_DT21/T4101._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0020 offset: 0x59A4
@scena.Code('func_20_59A4')
def func_20_59A4():
    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x0010, 13300, 23000, 107640, 225)
    OP_22(0x008C, 0x00, 0x64)
    SetChrChipByIndex(0x0010, 18)
    OP_8E(0x0010, 1360, 19500, 100800, 4000, 0x00)
    OP_8C(0x0010, 315, 300)
    Sleep(500)

    OP_8F(0x0010, 980, 18300, 100790, 1000, 0x00)
    Fade(250)
    SetChrFlags(0x0010, 0x0080)
    SetChrPos(0x0010, 850, 18300, 100700, 3000)
    SetChrChipByIndex(0x000F, 15)
    OP_0D()

    Return()

# id: 0x0021 offset: 0x5A1A
@scena.Code('func_21_5A1A')
def func_21_5A1A():
    OP_7D(0x00, 0x0011, 0x0032, 0x0064)
    SetChrFlags(0x0011, 0x0004)
    SetChrChipByIndex(0x0011, 20)
    OP_8E(0x0011, -6140, 18000, 102150, 10000, 0x00)
    OP_22(0x023B, 0x00, 0x64)
    SetChrFlags(0x00FE, 0x0020)
    SetChrChipByIndex(0x00FE, 21)

    @scena.Lambda('lambda_5A55')
    def lambda_5A55():
        OP_8F(0x00FE, -4040, 18700, 101770, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_5A55)

    @scena.Lambda('lambda_5A70')
    def lambda_5A70():
        OP_99(0x00FE, 0x00, 0x07, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_5A70)

    WaitForThreadExit(0x00FE, 0x0001)
    OP_7D(0x01, 0x00FE, 0x0000, 0x0000)

    Return()

# id: 0x0022 offset: 0x5A88
@scena.Code('func_22_5A88')
def func_22_5A88():
    OP_8C(0x00FE, 270, 500)
    Sleep(200)

    OP_22(0x01F9, 0x00, 0x64)

    @scena.Lambda('lambda_5A9F')
    def lambda_5A9F():
        OP_99(0x00FE, 0x0D, 0x07, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_5A9F)

    SetChrFlags(0x00FE, 0x0004)
    SetChrChipByIndex(0x00FE, 8)
    OP_22(0x00A3, 0x00, 0x64)
    OP_7D(0x00, 0x00FE, 0x0032, 0x0064)
    ClearChrFlags(0x00FE, 0x0020)

    @scena.Lambda('lambda_5ACB')
    def lambda_5ACB():
        OP_8F(0x00FE, -2540, 18700, 102070, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_5ACB)

    Sleep(200)

    @scena.Lambda('lambda_5AEB')
    def lambda_5AEB():
        OP_99(0x00FE, 0x07, 0x00, 0x00000DAC)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_5AEB)

    WaitForThreadExit(0x00FE, 0x0001)
    OP_7D(0x01, 0x00FE, 0x0000, 0x0000)

    Return()

# id: 0x0023 offset: 0x5B03
@scena.Code('func_23_5B03')
def func_23_5B03():
    OP_7D(0x00, 0x00FE, 0x0032, 0x0064)
    SetChrFlags(0x00FE, 0x0004)
    SetChrChipByIndex(0x00FE, 4)

    @scena.Lambda('lambda_5B1B')
    def lambda_5B1B():
        OP_99(0x00FE, 0x00, 0x03, 0x000009C4)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_5B1B)

    WaitForThreadExit(0x00FE, 0x0002)
    OP_22(0x00A3, 0x00, 0x64)

    @scena.Lambda('lambda_5B35')
    def lambda_5B35():
        OP_99(0x00FE, 0x03, 0x06, 0x00000DAC)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_5B35)

    @scena.Lambda('lambda_5B45')
    def lambda_5B45():
        OP_96(0x00FE, 0xFFFFF8E4, 0x00004650, 0x000189F2, 0x000001F4, 0x00001388)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_5B45)

    Sleep(100)

    SetChrChipByIndex(0x001A, 35)
    SetChrSubChip(0x001A, 0)
    SetChrPos(0x001A, -1820, 18500, 100850, 0)
    ClearChrFlags(0x001A, 0x0080)
    SetChrFlags(0x001A, 0x0020)
    SetChrFlags(0x001A, 0x0040)
    OP_22(0x01F7, 0x00, 0x64)

    @scena.Lambda('lambda_5B97')
    def lambda_5B97():
        OP_8F(0x00FE, -7600, 18000, 101780, 24000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_5B97)

    WaitForThreadExit(0x00FE, 0x0001)
    SetChrSubChip(0x001A, 1)
    WaitForThreadExit(0x00FE, 0x0002)
    OP_7D(0x01, 0x00FE, 0x0000, 0x0000)

    Return()

# id: 0x0024 offset: 0x5BC4
@scena.Code('func_24_5BC4')
def func_24_5BC4():
    @scena.Lambda('lambda_5BCA')
    def lambda_5BCA():
        OP_8C(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_5BCA)

    Sleep(50)

    @scena.Lambda('lambda_5BDD')
    def lambda_5BDD():
        OP_8C(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_5BDD)

    Sleep(50)

    @scena.Lambda('lambda_5BF0')
    def lambda_5BF0():
        OP_8C(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_5BF0)

    Sleep(50)

    @scena.Lambda('lambda_5C03')
    def lambda_5C03():
        OP_8C(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_5C03)

    Sleep(50)

    @scena.Lambda('lambda_5C16')
    def lambda_5C16():
        OP_8C(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_5C16)

    Return()

# id: 0x0025 offset: 0x5C1F
@scena.Code('func_25_5C1F')
def func_25_5C1F():
    OP_7D(0x00, 0x00FE, 0x0032, 0x0064)
    SetChrFlags(0x00FE, 0x0020)
    SetChrFlags(0x00FE, 0x0004)
    SetChrChipByIndex(0x00FE, 20)
    SetChrSubChip(0x00FE, 0)

    @scena.Lambda('lambda_5C41')
    def lambda_5C41():
        OP_99(0x00FE, 0x01, 0x04, 0x000009C4)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_5C41)

    OP_22(0x00A3, 0x00, 0x64)
    OP_96(0x00FE, 0xFFFFEEB2, 0x00004A38, 0x00018628, 0x000003E8, 0x00001388)

    @scena.Lambda('lambda_5C6D')
    def lambda_5C6D():
        OP_8E(0x00FE, -4430, 18000, 99880, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_5C6D)

    TerminateThread(0x00FE, 0x01)
    SetChrChipByIndex(0x0011, 14)
    SetChrSubChip(0x00FE, 0)

    @scena.Lambda('lambda_5C96')
    def lambda_5C96():
        OP_6D(-680, 18000, 102860, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_5C96)

    OP_22(0x00A3, 0x00, 0x64)
    OP_96(0x00FE, 0xFFFFF5D8, 0x00004650, 0x00018DC6, 0x000001F4, 0x00001388)
    SetChrSubChip(0x00FE, 1)
    OP_22(0x01F9, 0x00, 0x64)
    WaitForThreadExit(0x0101, 0x0000)
    OP_7D(0x01, 0x00FE, 0x0000, 0x0000)

    Return()

# id: 0x0026 offset: 0x5CDC
@scena.Code('func_26_5CDC')
def func_26_5CDC():
    OP_9F(0x000A, 0xFF, 0xFF, 0xFF, 0x00, 0x0000012C)
    SetChrPos(0x000A, -1270, 18000, 101310, 270)
    SetChrSubChip(0x000A, 0)
    SetChrChipByIndex(0x000A, 4)
    OP_9F(0x000A, 0xFF, 0xFF, 0xFF, 0xFF, 0x0000012C)

    Return()

# id: 0x0027 offset: 0x5D0E
@scena.Code('func_27_5D0E')
def func_27_5D0E():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5D23',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000BB8)

    Jump('func_27_5D0E')

    def _loc_5D23(): pass

    label('loc_5D23')

    Return()

# id: 0x0028 offset: 0x5D24
@scena.Code('func_28_5D24')
def func_28_5D24():
    @scena.Lambda('lambda_5D2A')
    def lambda_5D2A():
        ChrTurnDirection(0x000D, 0x0010, 400)
        Yield()

        Jump('lambda_5D2A')

    DispatchAsync2(0x000D, 0x0001, lambda_5D2A)

    CreateThread(0x0010, 0x01, 0x00, 0x0027)
    OP_7D(0x00, 0x00FE, 0x0032, 0x0064)
    OP_8F(0x00FE, 2200, 18800, 101450, 28000, 0x00)
    SetChrChipByIndex(0x000D, 10)
    SetChrSubChip(0x000D, 0)
    OP_22(0x00A3, 0x00, 0x64)

    @scena.Lambda('lambda_5D6D')
    def lambda_5D6D():
        OP_96(0x00FE, 0x000009B0, 0x00004650, 0x000194BA, 0x000001F4, 0x00001770)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_5D6D)

    OP_8F(0x00FE, 9840, 23880, 107990, 16000, 0x00)
    OP_7D(0x01, 0x0010, 0x0000, 0x0000)
    SetChrFlags(0x00FE, 0x0080)
    WaitForThreadExit(0x000D, 0x0001)

    @scena.Lambda('lambda_5DB1')
    def lambda_5DB1():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_5DB1)

    Sleep(100)

    @scena.Lambda('lambda_5DC4')
    def lambda_5DC4():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0003, lambda_5DC4)

    Sleep(100)

    OP_8C(0x000E, 180, 400)
    OP_7D(0x01, 0x00FE, 0x0000, 0x0000)

    Return()

# id: 0x0029 offset: 0x5DE1
@scena.Code('func_29_5DE1')
def func_29_5DE1():
    OP_7D(0x00, 0x00FE, 0x0032, 0x0064)
    SetChrChipByIndex(0x0012, 23)
    SetChrPos(0x0012, 10480, 18000, 96630, 315)
    SetChrFlags(0x0012, 0x0040)
    ClearChrFlags(0x0012, 0x0080)
    OP_8E(0x0012, 6540, 18000, 98850, 10000, 0x00)
    OP_22(0x00A3, 0x00, 0x64)

    @scena.Lambda('lambda_5E28')
    def lambda_5E28():
        OP_8C(0x00FE, 180, 600)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_5E28)

    OP_96(0x0012, 0x000008F2, 0x00004650, 0x0001883A, 0x000007D0, 0x00001770)
    OP_22(0x00A4, 0x00, 0x64)

    @scena.Lambda('lambda_5E52')
    def lambda_5E52():
        OP_8C(0x00FE, 0, 800)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_5E52)

    SetChrChipByIndex(0x0012, 24)
    SetChrSubChip(0x0012, 0)
    WaitForThreadExit(0x0012, 0x0001)

    @scena.Lambda('lambda_5E6F')
    def lambda_5E6F():
        OP_99(0x00FE, 0x00, 0x04, 0x000007D0)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_5E6F)

    @scena.Lambda('lambda_5E7F')
    def lambda_5E7F():
        OP_99(0x00FE, 0x00, 0x09, 0x00000DAC)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_5E7F)

    @scena.Lambda('lambda_5E8F')
    def lambda_5E8F():
        OP_8F(0x00FE, 2400, 18000, 103000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_5E8F)

    WaitForThreadExit(0x00FE, 0x0001)
    OP_22(0x00D6, 0x00, 0x64)
    PlayEffect(0x00, 0x00, 0x000D, 0, 0, 500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0x000000C8, 0x000000C8, 0x00000BB8, 0x0000012C)

    @scena.Lambda('lambda_5EFA')
    def lambda_5EFA():
        OP_9E(0x00FE, 0x0000001E, 0x00000000, 0x0000012C, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x000D, 0x0003, lambda_5EFA)

    @scena.Lambda('lambda_5F14')
    def lambda_5F14():
        OP_9E(0x00FE, 0x0000001E, 0x00000000, 0x0000012C, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0012, 0x0003, lambda_5F14)

    CreateThread(0x000D, 0x01, 0x00, 0x002A)
    OP_8C(0x000B, 90, 800)
    SetChrChipByIndex(0x000B, 6)
    SetChrSubChip(0x000B, 0)
    CreateThread(0x0012, 0x02, 0x00, 0x002C)
    CreateThread(0x000B, 0x00, 0x00, 0x002B)
    OP_8C(0x000F, 0, 400)
    OP_8C(0x000E, 0, 400)
    WaitForThreadExit(0x000B, 0x0000)
    WaitForThreadExit(0x0012, 0x0002)
    OP_7D(0x01, 0x00FE, 0x0000, 0x0000)

    Return()

# id: 0x002A offset: 0x5F6F
@scena.Code('func_2A_5F6F')
def func_2A_5F6F():
    OP_7D(0x00, 0x00FE, 0x0032, 0x0064)

    @scena.Lambda('lambda_5F7D')
    def lambda_5F7D():
        OP_99(0x00FE, 0x09, 0x00, 0x000007D0)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_5F7D)

    OP_22(0x00A3, 0x00, 0x64)
    OP_96(0x00FE, 0x0000091A, 0x0000493E, 0x00019BB8, 0x000003E8, 0x00001388)
    OP_22(0x00A4, 0x00, 0x64)
    Sleep(100)

    OP_22(0x00A3, 0x00, 0x64)
    OP_96(0x00FE, 0x00000820, 0x00004C2C, 0x0001A1EE, 0x000005DC, 0x00000FA0)
    OP_22(0x00A4, 0x00, 0x64)
    WaitForThreadExit(0x00FE, 0x0002)
    OP_7D(0x01, 0x00FE, 0x0000, 0x0000)

    Return()

# id: 0x002B offset: 0x5FDC
@scena.Code('func_2B_5FDC')
def func_2B_5FDC():
    OP_7D(0x00, 0x00FE, 0x0032, 0x0064)
    Sleep(200)

    SetChrFlags(0x00FE, 0x0020)
    OP_22(0x00A3, 0x00, 0x64)

    @scena.Lambda('lambda_5FF9')
    def lambda_5FF9():
        OP_8C(0x00FE, 135, 600)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_5FF9)

    OP_96(0x00FE, 0x0000010E, 0x0000474A, 0x000197D0, 0x000001F4, 0x00001388)
    OP_22(0x00A4, 0x00, 0x64)
    Sleep(200)

    OP_22(0x00A3, 0x00, 0x64)

    @scena.Lambda('lambda_602D')
    def lambda_602D():
        OP_8C(0x00FE, 180, 600)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_602D)

    OP_96(0x00FE, 0x000003F2, 0x0000493E, 0x00019B40, 0x000001F4, 0x00001388)
    OP_22(0x00A4, 0x00, 0x64)
    Sleep(200)

    OP_22(0x00A3, 0x00, 0x64)
    SetChrChipByIndex(0x00FE, 12)
    SetChrSubChip(0x00FE, 0)
    OP_96(0x00FE, 0x00000212, 0x00004D26, 0x0001A374, 0x000005DC, 0x00000FA0)
    SetChrSubChip(0x00FE, 1)
    OP_22(0x00A4, 0x00, 0x64)
    Sleep(500)

    SetChrChipByIndex(0x00FE, 34)
    SetChrSubChip(0x00FE, 0)
    OP_7D(0x01, 0x00FE, 0x0000, 0x0000)

    Return()

# id: 0x002C offset: 0x609E
@scena.Code('func_2C_609E')
def func_2C_609E():
    OP_7D(0x00, 0x00FE, 0x0032, 0x0064)
    SetChrFlags(0x00FE, 0x0020)
    OP_8C(0x0012, 270, 800)
    SetChrChipByIndex(0x0012, 25)
    SetChrSubChip(0x0012, 2)

    @scena.Lambda('lambda_60C2')
    def lambda_60C2():
        OP_96(0x00FE, 0x000006D6, 0x00004650, 0x00019442, 0x00000064, 0x00001388)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_60C2)

    OP_99(0x00FE, 0x03, 0x05, 0x000007D0)
    WaitForThreadExit(0x00FE, 0x0001)
    OP_8C(0x00FE, 315, 800)

    @scena.Lambda('lambda_60F5')
    def lambda_60F5():
        OP_96(0x00FE, 0x0000047E, 0x00004650, 0x00019618, 0x00000064, 0x00001388)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_60F5)

    OP_99(0x00FE, 0x06, 0x08, 0x000007D0)
    WaitForThreadExit(0x00FE, 0x0001)
    OP_8C(0x00FE, 0, 800)

    @scena.Lambda('lambda_6128')
    def lambda_6128():
        OP_96(0x00FE, 0x000004BA, 0x0000474A, 0x00019802, 0x00000064, 0x00001388)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_6128)

    OP_99(0x00FE, 0x09, 0x0F, 0x000007D0)
    WaitForThreadExit(0x00FE, 0x0001)
    OP_7D(0x01, 0x00FE, 0x0000, 0x0000)

    Return()

# id: 0x002D offset: 0x6157
@scena.Code('func_2D_6157')
def func_2D_6157():
    OP_7D(0x00, 0x000A, 0x0032, 0x01F4)
    OP_97(0x000A, 0xFFFFFA24, 0x00018A88, 0x000249F0, 0x00001B58, 0x0001)
    OP_7D(0x01, 0x000A, 0x0000, 0x0000)
    OP_8C(0x000A, 180, 400)
    Sleep(500)

    SetChrSubChip(0x000A, 0)
    SetChrFlags(0x000A, 0x0020)
    OP_8F(0x000A, -1000, 19000, 106400, 4000, 0x00)
    TerminateThread(0x000A, 0x02)
    Fade(500)
    SetChrFlags(0x000A, 0x0001)
    ClearChrFlags(0x000A, 0x0004)
    SetChrPos(0x000A, -1000, 19500, 106400, 180)
    SetChrChipByIndex(0x000A, 4)
    SetChrSubChip(0x000A, 0)
    OP_22(0x00A4, 0x00, 0x64)
    TerminateThread(0x0011, 0x02)

    Return()

# id: 0x002E offset: 0x61DE
@scena.Code('func_2E_61DE')
def func_2E_61DE():
    EventBegin(0x00)
    OP_A3(0x10F2)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_61F8',
    )

    Call(0, 0x0038)
    Call(0, 0x0039)

    def _loc_61F8(): pass

    label('loc_61F8')

    OP_D2(0x00270266, 0x00270270, 0x03)
    OP_D2(0x0027026B, 0x00270275, 0x04)
    OP_D2(0x002701C6, 0x002701CB, 0x05)
    OP_D2(0x0027026C, 0x00270276, 0x06)
    OP_D2(0x00260003, 0x00260008, 0x07)
    OP_D2(0x00270257, 0x00270261, 0x08)
    OP_D2(0x00270252, 0x0027025C, 0x09)
    OP_D2(0x00270258, 0x00270262, 0x0A)
    OP_D2(0x00070141, 0x00070145, 0x0B)
    OP_D2(0x00070182, 0x00070186, 0x0F)
    OP_D2(0x002702EA, 0x002702F4, 0x13)
    OP_D2(0x002701D4, 0x002701D9, 0x14)
    OP_D2(0x000702D2, 0x000702D9, 0x16)
    OP_D2(0x002700B0, 0x002700B4, 0x17)
    OP_D2(0x000704AA, 0x000704AE, 0x18)
    OP_D2(0x00270110, 0x00270120, 0x1A)
    OP_D2(0x00270130, 0x00270140, 0x1C)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000005, 'loc_62BB'),
        (0x00000002, 'loc_62C8'),
        (0x00000006, 'loc_62D5'),
        (0x00000007, 'loc_62E2'),
        (-1, 'loc_62EF'),
    )

    def _loc_62BB(): pass

    label('loc_62BB')

    OP_D2(0x00070218, 0x00070224, 0x1E)

    Jump('loc_62EF')

    def _loc_62C8(): pass

    label('loc_62C8')

    OP_D2(0x000701D0, 0x000701DC, 0x1E)

    Jump('loc_62EF')

    def _loc_62D5(): pass

    label('loc_62D5')

    OP_D2(0x00070230, 0x0007023C, 0x1E)

    Jump('loc_62EF')

    def _loc_62E2(): pass

    label('loc_62E2')

    OP_D2(0x00070248, 0x00070254, 0x1E)

    Jump('loc_62EF')

    def _loc_62EF(): pass

    label('loc_62EF')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000005, 'loc_6308'),
        (0x00000002, 'loc_6315'),
        (0x00000006, 'loc_6322'),
        (0x00000007, 'loc_632F'),
        (-1, 'loc_633C'),
    )

    def _loc_6308(): pass

    label('loc_6308')

    OP_D2(0x00070218, 0x00070224, 0x20)

    Jump('loc_633C')

    def _loc_6315(): pass

    label('loc_6315')

    OP_D2(0x000701D0, 0x000701DC, 0x20)

    Jump('loc_633C')

    def _loc_6322(): pass

    label('loc_6322')

    OP_D2(0x00070230, 0x0007023C, 0x20)

    Jump('loc_633C')

    def _loc_632F(): pass

    label('loc_632F')

    OP_D2(0x00070248, 0x00070254, 0x20)

    Jump('loc_633C')

    def _loc_633C(): pass

    label('loc_633C')

    OP_D2(0x002600A0, 0x002600A5, 0x22)
    OP_D2(0x00060028, 0x0006002D, 0x23)
    SetChrChipByIndex(0x000A, 3)
    SetChrChipByIndex(0x000B, 34)
    SetChrChipByIndex(0x000C, 7)
    SetChrChipByIndex(0x000D, 9)
    SetChrChipByIndex(0x000E, 11)
    SetChrChipByIndex(0x000F, 15)
    SetChrChipByIndex(0x0011, 19)
    SetChrChipByIndex(0x0012, 22)
    SetChrChipByIndex(0x0101, 26)
    SetChrChipByIndex(0x0102, 28)
    SetChrChipByIndex(0x00F8, 30)
    SetChrChipByIndex(0x00F9, 32)
    SetChrPos(0x0101, 1700, 18000, 102050, 180)
    SetChrPos(0x0102, 2910, 18000, 102070, 180)
    SetChrPos(0x00F8, 1760, 18000, 100500, 180)
    SetChrPos(0x00F9, 2860, 18000, 100500, 180)
    SetChrPos(0x0011, -1220, 18000, 101600, 0)
    SetChrPos(0x0012, 260, 18000, 102200, 0)
    SetChrPos(0x000E, -670, 18000, 100330, 180)
    SetChrPos(0x000F, 540, 18000, 100570, 180)
    SetChrPos(0x000C, -1530, 19750, 107270, 180)
    SetChrPos(0x000A, -1000, 19500, 106400, 180)
    SetChrPos(0x000B, 530, 19750, 107170, 180)
    SetChrPos(0x000D, 1800, 19500, 106550, 180)
    SetChrPos(0x001A, -7600, 18000, 101780, 0)
    ClearChrFlags(0x001A, 0x0080)
    SetChrFlags(0x001A, 0x0002)
    SetChrChipByIndex(0x001A, 35)
    SetChrSubChip(0x001A, 15)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    LoadEffect(0x00, 'map\\\\mp046_00.eff')
    OP_6D(2280, 18000, 101560, 0)
    OP_67(0, 7560, -10000, 0)
    OP_6B(2150, 0)
    OP_6C(33000, 0)
    OP_6E(401, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010380477V#1004F#5P哇……\n',
            '猎兵们被压制住了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020380478V#1040F#5P嗯，真是名不虚传。',
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
        'loc_65A7',
    )

    ChrTalk(
        0x0103,
        (
            '#0030380479V#021F#5P呵呵……干得不错么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_661F')

    def _loc_65A7(): pass

    label('loc_65A7')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_65E5',
    )

    ChrTalk(
        0x0106,
        (
            '#0050380480V#051F#5P嘿……\n',
            '干得不错嘛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_661F')

    def _loc_65E5(): pass

    label('loc_65E5')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_661F',
    )

    ChrTalk(
        0x0108,
        (
            '#0080380481V#070F#5P喔……干得不错啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_661F(): pass

    label('loc_661F')

    @scena.Lambda('lambda_6625')
    def lambda_6625():
        OP_6D(720, 19000, 105800, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_6625)

    @scena.Lambda('lambda_663D')
    def lambda_663D():
        OP_67(0, 6080, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_663D)

    @scena.Lambda('lambda_6655')
    def lambda_6655():
        OP_6B(2740, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_6655)

    OP_8C(0x0012, 0, 400)
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0012,
        (
            '#0130380482V#112F#6P那么，你们准备怎么办？\n',
            '『噬身之蛇』的诸位。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130380483V已到了这种地步，\n',
            '仍然还打算同我们较量一下吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_66F1')
    def lambda_66F1():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_66F1)

    Sleep(50)

    @scena.Lambda('lambda_6704')
    def lambda_6704():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_6704)

    Sleep(50)

    @scena.Lambda('lambda_6717')
    def lambda_6717():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_6717)

    Sleep(50)

    @scena.Lambda('lambda_672A')
    def lambda_672A():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_672A)

    Sleep(50)

    @scena.Lambda('lambda_673D')
    def lambda_673D():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_673D)

    Sleep(50)

    SetChrFlags(0x000F, 0x0020)

    @scena.Lambda('lambda_6755')
    def lambda_6755():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_6755)

    Sleep(400)

    ChrTalk(
        0x000B,
        (
            '#0200380484V#254F#5P……哼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0220380485V#266F#5P……真讨厌。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220380486V#262F这样的话，我就只能\n',
            '把帕蒂尔·玛蒂尔叫来──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0170380487V#232F#5P不用了，玲。\n',
            '我们自己错失了大好机会。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170380488V再继续纠缠下去的话\n',
            '就太缺乏美感了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0210380489V#244F#5P俘虏女王陛下和公主殿下\n',
            '也只是在条件允许的情况下的任务。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210380490V#240F各位，咱们撤退吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0200380491V#250F#5P哼……没办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0220380492V#262F#5P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(250)
    SetChrChipByIndex(0x000A, 4)
    OP_0D()
    SetChrChipByIndex(0x000A, 6)
    PlayEffect(0x00, 0x00, 0x000A, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0x01, 0x000C, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0x02, 0x000B, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0x03, 0x000D, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x010A, 0x00, 0x64)

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(240)

    Sleep(500)

    SetChrSubChip(0x000A, 0)
    SetChrChipByIndex(0x000A, 4)
    Sleep(1500)

    ChrTalk(
        0x000A,
        (
            '#0170380493V#230F#5P那么诸位……\n',
            '我们就先告辞了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170380494V但是下一次的试练\n',
            '已经为你们准备完毕了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170380495V请一定不要松懈啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020380496V#1042F#4P下一次的试练……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010380497V#1020F#6P什、什么意思 ！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0210380498V#244F#5P呵呵……\n',
            '你们很快就会知道的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210380499V#241F那么各位，请多保重了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    SetChrChipByIndex(0x000D, 8)
    Sleep(200)

    SetChrChipByIndex(0x000D, 10)

    ExecExpressionWithValue(
        0x000D,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ExecExpressionWithValue(
        0x000D,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(240)

    OP_22(0x0118, 0x00, 0x64)
    CreateThread(0x001B, 0x00, 0x00, 0x0030)
    CreateThread(0x001C, 0x00, 0x00, 0x0031)
    CreateThread(0x001D, 0x00, 0x00, 0x0032)
    CreateThread(0x001E, 0x00, 0x00, 0x0033)
    CreateThread(0x001F, 0x00, 0x00, 0x0034)
    CreateThread(0x0020, 0x00, 0x00, 0x0035)
    CreateThread(0x0021, 0x00, 0x00, 0x0036)
    CreateThread(0x0022, 0x00, 0x00, 0x0037)
    Sleep(3000)

    SetChrSubChip(0x000D, 0)
    SetChrChipByIndex(0x000D, 8)
    OP_20(0x00000BB8)

    @scena.Lambda('lambda_6C1A')
    def lambda_6C1A():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000007D0)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_6C1A)

    @scena.Lambda('lambda_6C2C')
    def lambda_6C2C():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0021, 0x0001, lambda_6C2C)

    @scena.Lambda('lambda_6C3E')
    def lambda_6C3E():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_6C3E)

    Sleep(300)

    @scena.Lambda('lambda_6C55')
    def lambda_6C55():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000007D0)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_6C55)

    @scena.Lambda('lambda_6C67')
    def lambda_6C67():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000007D0)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_6C67)

    @scena.Lambda('lambda_6C79')
    def lambda_6C79():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000007D0)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_6C79)

    Sleep(300)

    @scena.Lambda('lambda_6C90')
    def lambda_6C90():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000007D0)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_6C90)

    @scena.Lambda('lambda_6CA2')
    def lambda_6CA2():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000007D0)

        ExitThread()

    DispatchAsync(0x001D, 0x0001, lambda_6CA2)

    @scena.Lambda('lambda_6CB4')
    def lambda_6CB4():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000007D0)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_6CB4)

    Sleep(300)

    @scena.Lambda('lambda_6CCB')
    def lambda_6CCB():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000007D0)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_6CCB)

    @scena.Lambda('lambda_6CDD')
    def lambda_6CDD():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000007D0)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_6CDD)

    @scena.Lambda('lambda_6CEF')
    def lambda_6CEF():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_6CEF)

    Sleep(300)

    OP_82(0x00, 0x02)
    OP_82(0x01, 0x02)
    OP_82(0x02, 0x02)
    OP_82(0x03, 0x02)
    CreateThread(0x000C, 0x03, 0x00, 0x002F)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010380500V#1026F#6P啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020380501V#1035F#4P撤退了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_21()
    Sleep(100)

    OP_1D(0x01)
    Sleep(600)

    @scena.Lambda('lambda_6D75')
    def lambda_6D75():
        OP_6D(1170, 18000, 102460, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_6D75)

    @scena.Lambda('lambda_6D8D')
    def lambda_6D8D():
        OP_67(0, 6050, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6D8D)

    @scena.Lambda('lambda_6DA5')
    def lambda_6DA5():
        OP_6B(2330, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_6DA5)

    @scena.Lambda('lambda_6DB5')
    def lambda_6DB5():
        OP_6C(33000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_6DB5)

    @scena.Lambda('lambda_6DC5')
    def lambda_6DC5():
        OP_6E(401, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_6DC5)

    WaitForThreadExit(0x0101, 0x0000)
    Fade(250)
    OP_22(0x00D5, 0x00, 0x64)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x00F8, 65535)
    SetChrChipByIndex(0x00F9, 65535)
    SetChrChipByIndex(0x0011, 20)
    SetChrChipByIndex(0x0012, 23)
    OP_0D()

    @scena.Lambda('lambda_6E03')
    def lambda_6E03():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_6E03)

    Sleep(50)

    @scena.Lambda('lambda_6E16')
    def lambda_6E16():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_6E16)

    Sleep(50)

    @scena.Lambda('lambda_6E29')
    def lambda_6E29():
        ChrTurnDirection(0x00FE, 0x0012, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6E29)

    Sleep(50)

    @scena.Lambda('lambda_6E3C')
    def lambda_6E3C():
        ChrTurnDirection(0x00FE, 0x0012, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_6E3C)

    Sleep(50)

    @scena.Lambda('lambda_6E4F')
    def lambda_6E4F():
        ChrTurnDirection(0x00FE, 0x0012, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_6E4F)

    Sleep(50)

    @scena.Lambda('lambda_6E62')
    def lambda_6E62():
        ChrTurnDirection(0x00FE, 0x0012, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_6E62)

    Sleep(400)

    ChrTalk(
        0x0012,
        (
            '#0130380502V#110F#5P嗯，这么一来，那些猎兵\n',
            '也要撤出市内了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130380503V很遗憾，不能深追，\n',
            '不过也别要求太高了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010380504V#1020F#2P嗯……等等，还有更重要的问题！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010380505V#1019F为什么上校会\n',
            '出现在这里！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010380506V你不是在服刑中吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0012, 90, 400)
    Sleep(300)

    ChrTalk(
        0x0012,
        (
            '#0130380507V#115F#6P所以都告诉过你\n',
            '我已经不是上校了……算了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0620380508V#701F#6P总之现在最要紧的是\n',
            '平息这场混乱。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620380509V你们也来帮忙吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010380510V#1006F#5P嗯、嗯……\n',
            '那当然。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020380511V#1040F#2P先去进行灭火和拯救伤员\n',
            '的工作吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    Sleep(1000)

    OP_22(0x0087, 0x01, 0x3C)
    OP_22(0x00AE, 0x01, 0x3C)
    Sleep(100)

    OP_22(0x0087, 0x01, 0x32)
    OP_22(0x00AE, 0x01, 0x32)
    Sleep(100)

    OP_22(0x0087, 0x01, 0x28)
    OP_22(0x00AE, 0x01, 0x28)
    Sleep(100)

    OP_22(0x0087, 0x01, 0x1E)
    OP_22(0x00AE, 0x01, 0x1E)
    Sleep(100)

    OP_22(0x0087, 0x01, 0x14)
    OP_22(0x00AE, 0x01, 0x14)
    Sleep(100)

    OP_22(0x0087, 0x01, 0x0A)
    OP_22(0x00AE, 0x01, 0x0A)
    Sleep(100)

    OP_23(0x0087)
    OP_23(0x00AE)
    OP_0D()
    Sleep(500)

    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '就这样……\n',
            '『结社』对王城的攻击终于被艰难地压制住了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔等人与军队一起\n',
            '进行灭火，并安抚混乱中的市民……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '在此期间，其他的同伴在收到联络后\n',
            '也一起赶了过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_28(0x009C, 0x04, 0x10)
    OP_AF(0xCD, 0x009C)
    Sleep(1000)

    OP_A2(0x10F1)
    NewScene('ED6_DT21/T4220._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x002F offset: 0x71D3
@scena.Code('func_2F_71D3')
def func_2F_71D3():
    Sleep(300)

    OP_24(0x010A, 0x5A)
    Sleep(300)

    OP_24(0x010A, 0x50)
    Sleep(300)

    OP_24(0x010A, 0x46)
    Sleep(300)

    OP_24(0x010A, 0x3C)
    Sleep(300)

    OP_24(0x010A, 0x32)
    Sleep(300)

    OP_24(0x010A, 0x28)
    Sleep(300)

    OP_24(0x010A, 0x1E)
    Sleep(300)

    OP_23(0x010A)

    Return()

# id: 0x0030 offset: 0x721B
@scena.Code('func_30_721B')
def func_30_721B():
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 4)
    SetChrPos(0x00FE, -1000, 19500, 106400, 180)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrFlags(0x00FE, 0x0040)
    SetChrFlags(0x00FE, 0x0020)
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x5A, 0x00000000)
    OP_91(0x00FE, 50, 0, 0, 300, 0x00)
    OP_91(0x00FE, -50, 0, 0, 300, 0x00)
    OP_91(0x00FE, 100, 0, 0, 300, 0x00)
    OP_91(0x00FE, -100, 0, 0, 300, 0x00)
    def _loc_72A0(): pass

    label('loc_72A0')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_72D4',
    )

    OP_91(0x00FE, 150, 0, 0, 300, 0x00)
    OP_91(0x00FE, -150, 0, 0, 300, 0x00)

    Jump('loc_72A0')

    def _loc_72D4(): pass

    label('loc_72D4')

    Return()

# id: 0x0031 offset: 0x72D5
@scena.Code('func_31_72D5')
def func_31_72D5():
    SetChrSubChip(0x00FE, 0)
    SetChrChipByIndex(0x00FE, 4)
    SetChrPos(0x00FE, -1000, 19500, 106400, 180)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrFlags(0x00FE, 0x0040)
    SetChrFlags(0x00FE, 0x0020)
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x5A, 0x00000000)
    OP_91(0x00FE, -50, 0, 0, 300, 0x00)
    OP_91(0x00FE, 50, 0, 0, 300, 0x00)
    OP_91(0x00FE, -100, 0, 0, 300, 0x00)
    OP_91(0x00FE, 100, 0, 0, 300, 0x00)
    def _loc_735A(): pass

    label('loc_735A')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_738E',
    )

    OP_91(0x00FE, -150, 0, 0, 300, 0x00)
    OP_91(0x00FE, 150, 0, 0, 300, 0x00)

    Jump('loc_735A')

    def _loc_738E(): pass

    label('loc_738E')

    Return()

# id: 0x0032 offset: 0x738F
@scena.Code('func_32_738F')
def func_32_738F():
    SetChrChipByIndex(0x00FE, 34)
    SetChrSubChip(0x00FE, 0)
    SetChrPos(0x00FE, 530, 19750, 107380, 180)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrFlags(0x00FE, 0x0040)
    SetChrFlags(0x00FE, 0x0020)
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x5A, 0x00000000)
    OP_91(0x00FE, 50, 0, 0, 300, 0x00)
    OP_91(0x00FE, -50, 0, 0, 300, 0x00)
    OP_91(0x00FE, 100, 0, 0, 300, 0x00)
    OP_91(0x00FE, -100, 0, 0, 300, 0x00)
    def _loc_7414(): pass

    label('loc_7414')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_7448',
    )

    OP_91(0x00FE, 150, 0, 0, 300, 0x00)
    OP_91(0x00FE, -150, 0, 0, 300, 0x00)

    Jump('loc_7414')

    def _loc_7448(): pass

    label('loc_7448')

    Return()

# id: 0x0033 offset: 0x7449
@scena.Code('func_33_7449')
def func_33_7449():
    SetChrChipByIndex(0x00FE, 34)
    SetChrSubChip(0x00FE, 0)
    SetChrPos(0x00FE, 530, 19750, 107380, 180)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrFlags(0x00FE, 0x0040)
    SetChrFlags(0x00FE, 0x0020)
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x5A, 0x00000000)
    OP_91(0x00FE, -50, 0, 0, 300, 0x00)
    OP_91(0x00FE, 50, 0, 0, 300, 0x00)
    OP_91(0x00FE, -100, 0, 0, 300, 0x00)
    OP_91(0x00FE, 100, 0, 0, 300, 0x00)
    def _loc_74CE(): pass

    label('loc_74CE')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_7502',
    )

    OP_91(0x00FE, -150, 0, 0, 300, 0x00)
    OP_91(0x00FE, 150, 0, 0, 300, 0x00)

    Jump('loc_74CE')

    def _loc_7502(): pass

    label('loc_7502')

    Return()

# id: 0x0034 offset: 0x7503
@scena.Code('func_34_7503')
def func_34_7503():
    SetChrChipByIndex(0x00FE, 7)
    SetChrSubChip(0x00FE, 0)
    SetChrPos(0x00FE, -1530, 19750, 107220, 180)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrFlags(0x00FE, 0x0040)
    SetChrFlags(0x00FE, 0x0020)
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x5A, 0x00000000)
    OP_91(0x00FE, 50, 0, 0, 300, 0x00)
    OP_91(0x00FE, -50, 0, 0, 300, 0x00)
    OP_91(0x00FE, 100, 0, 0, 300, 0x00)
    OP_91(0x00FE, -100, 0, 0, 300, 0x00)
    def _loc_7588(): pass

    label('loc_7588')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_75BC',
    )

    OP_91(0x00FE, 150, 0, 0, 300, 0x00)
    OP_91(0x00FE, -150, 0, 0, 300, 0x00)

    Jump('loc_7588')

    def _loc_75BC(): pass

    label('loc_75BC')

    Return()

# id: 0x0035 offset: 0x75BD
@scena.Code('func_35_75BD')
def func_35_75BD():
    SetChrChipByIndex(0x00FE, 7)
    SetChrSubChip(0x00FE, 0)
    SetChrPos(0x00FE, -1530, 19750, 107220, 180)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrFlags(0x00FE, 0x0040)
    SetChrFlags(0x00FE, 0x0020)
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x5A, 0x00000000)
    OP_91(0x00FE, -50, 0, 0, 300, 0x00)
    OP_91(0x00FE, 50, 0, 0, 300, 0x00)
    OP_91(0x00FE, -100, 0, 0, 300, 0x00)
    OP_91(0x00FE, 100, 0, 0, 300, 0x00)
    def _loc_7642(): pass

    label('loc_7642')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_7676',
    )

    OP_91(0x00FE, -150, 0, 0, 300, 0x00)
    OP_91(0x00FE, 150, 0, 0, 300, 0x00)

    Jump('loc_7642')

    def _loc_7676(): pass

    label('loc_7676')

    Return()

# id: 0x0036 offset: 0x7677
@scena.Code('func_36_7677')
def func_36_7677():
    SetChrChipByIndex(0x00FE, 8)
    SetChrSubChip(0x00FE, 0)
    SetChrPos(0x00FE, 2080, 19500, 106990, 180)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrFlags(0x00FE, 0x0040)
    SetChrFlags(0x00FE, 0x0020)
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x5A, 0x00000000)
    OP_91(0x00FE, 50, 0, 0, 300, 0x00)
    OP_91(0x00FE, -50, 0, 0, 300, 0x00)
    OP_91(0x00FE, 100, 0, 0, 300, 0x00)
    OP_91(0x00FE, -100, 0, 0, 300, 0x00)
    def _loc_76FC(): pass

    label('loc_76FC')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_7730',
    )

    OP_91(0x00FE, 150, 0, 0, 300, 0x00)
    OP_91(0x00FE, -150, 0, 0, 300, 0x00)

    Jump('loc_76FC')

    def _loc_7730(): pass

    label('loc_7730')

    Return()

# id: 0x0037 offset: 0x7731
@scena.Code('func_37_7731')
def func_37_7731():
    SetChrChipByIndex(0x00FE, 8)
    SetChrSubChip(0x00FE, 0)
    SetChrPos(0x00FE, 2080, 19500, 106990, 180)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrFlags(0x00FE, 0x0040)
    SetChrFlags(0x00FE, 0x0020)
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x5A, 0x00000000)
    OP_91(0x00FE, -50, 0, 0, 300, 0x00)
    OP_91(0x00FE, 50, 0, 0, 300, 0x00)
    OP_91(0x00FE, -100, 0, 0, 300, 0x00)
    OP_91(0x00FE, 100, 0, 0, 300, 0x00)
    def _loc_77B6(): pass

    label('loc_77B6')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_77EA',
    )

    OP_91(0x00FE, -150, 0, 0, 300, 0x00)
    OP_91(0x00FE, 150, 0, 0, 300, 0x00)

    Jump('loc_77B6')

    def _loc_77EA(): pass

    label('loc_77EA')

    Return()

# id: 0x0038 offset: 0x77EB
@scena.Code('func_38_77EB')
def func_38_77EB():
    FadeOut(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)

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
        (0x00000000, 'loc_7865'),
        (0x00000001, 'loc_786B'),
        (-1, 'loc_7871'),
    )

    def _loc_7865(): pass

    label('loc_7865')

    OP_A2(0x1200)

    Jump('loc_7871')

    def _loc_786B(): pass

    label('loc_786B')

    OP_A2(0x1201)

    Jump('loc_7871')

    def _loc_7871(): pass

    label('loc_7871')

    Return()

# id: 0x0039 offset: 0x7872
@scena.Code('func_39_7872')
def func_39_7872():
    ClearMapFlags(0x00000001)
    OP_6D(-67910, 0, 1890, 0)
    Sleep(100)

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            0x0000,
            0x0001,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
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

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

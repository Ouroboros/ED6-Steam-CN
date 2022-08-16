import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0400_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0400   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0400.x'
    header.mapIndex       = 13
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
        ('ED6_DT29/CH12890._CH', 'ED6_DT29/CH12890P._CP'),
        ('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT27/CH04001._CH', 'ED6_DT27/CH04001P._CP'),
        ('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP'),
        ('ED6_DT07/CH00161._CH', 'ED6_DT07/CH00161P._CP'),
        ('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP'),
        ('ED6_DT07/CH00121._CH', 'ED6_DT07/CH00121P._CP'),
        ('ED6_DT07/CH00140._CH', 'ED6_DT07/CH00140P._CP'),
        ('ED6_DT07/CH00141._CH', 'ED6_DT07/CH00141P._CP'),
        ('ED6_DT29/CH12891._CH', 'ED6_DT29/CH12891P._CP'),
        ('ED6_DT07/CH02480._CH', 'ED6_DT07/CH02480P._CP'),
        ('ED6_DT07/CH01060._CH', 'ED6_DT07/CH01060P._CP'),
        ('ED6_DT07/CH01070._CH', 'ED6_DT07/CH01070P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01710._CH', 'ED6_DT07/CH01710P._CP'),
        ('ED6_DT07/CH01720._CH', 'ED6_DT07/CH01720P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
    ]

# id: 0x10001 offset: 0x132
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '毒雾使者',
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
            name                = '毒雾使者',
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
            name                = '毒雾使者',
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
            name                = '缇欧',
            x                   = 40470,
            z                   = 0,
            y                   = 16320,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '维鲁',
            x                   = 21900,
            z                   = 0,
            y                   = 25300,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '查儿',
            x                   = 25100,
            z                   = 0,
            y                   = 23000,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '弗兰兹',
            x                   = 27590,
            z                   = -60,
            y                   = 34960,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '牛',
            x                   = 39010,
            z                   = 600,
            y                   = 22850,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0105,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '牛',
            x                   = 48160,
            z                   = 460,
            y                   = 18800,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0105,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '鸡',
            x                   = 44200,
            z                   = 0,
            y                   = 18540,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '鸡',
            x                   = 38780,
            z                   = 0,
            y                   = 19310,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '鸡',
            x                   = 51470,
            z                   = 0,
            y                   = 20950,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '鸡',
            x                   = 51470,
            z                   = 0,
            y                   = 20950,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 25880,
            z                   = 390,
            y                   = 53570,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 23960,
            z                   = 140,
            y                   = 43890,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0006,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '米尔西街道方向',
            x                   = 23910,
            z                   = 30,
            y                   = 66820,
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

# id: 0x10002 offset: 0x332
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x332
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 28330,
            y           = -1000,
            z           = 47700,
            range       = 30790,
            dword_10    = 0x000007D0,
            dword_14    = 0x0000DF66,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000022,
        ),
        ScenaEventData(
            x           = 20560,
            y           = -1000,
            z           = 57690,
            range       = 26700,
            dword_10    = 0x000007D0,
            dword_14    = 0x0000D8CC,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000023,
        ),
    )

# id: 0x10004 offset: 0x372
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 16370,
            triggerZ            = 570,
            triggerY            = 23100,
            triggerRange        = 800,
            actorX              = 16370,
            actorZ              = 1570,
            actorY              = 23100,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0024,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x396
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_3C5',
    )

    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrSetPos(0x000B, 29090, 0, 13250, 180)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)

    Jump('loc_430')

    def _loc_3C5(): pass

    label('loc_3C5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_3E5',
    )

    ChrSetPos(0x000B, 28990, 0, 13230, 180)
    ChrClearFlags(0x000E, 0x0080)

    Jump('loc_430')

    def _loc_3E5(): pass

    label('loc_3E5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_41C',
    )

    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0014, 0x0080)

    Jump('loc_430')

    def _loc_41C(): pass

    label('loc_41C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_430',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0313, 4, 0x189C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_430',
    )

    ChrSetFlags(0x000B, 0x0010)

    def _loc_430(): pass

    label('loc_430')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 7, 0x181F)),
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 0, 0x1820)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_445',
    )

    MapSetFlags(0x10000000)
    Event(0, func_10_1ECE)

    def _loc_445(): pass

    label('loc_445')

    Return()

# id: 0x0001 offset: 0x446
@scena.Code('func_01_446')
def func_01_446():
    OP_16(0x02, 4000, -96000, -96000, 2293764)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 1, 0x1821)),
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_46D',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x51),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_46D(): pass

    label('loc_46D')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_47F',
    )

    OP_10(0x04, 0x00)
    OP_10(0x05, 0x01)

    def _loc_47F(): pass

    label('loc_47F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 7, 0x181F)),
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_497',
    )

    OP_72(0x0000, 0x0010)
    OP_65(0x00, 0x0001)

    Jump('loc_49B')

    def _loc_497(): pass

    label('loc_497')

    OP_64(0x00, 0x0001)

    def _loc_49B(): pass

    label('loc_49B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_4A5',
    )

    Jump('loc_4C1')

    def _loc_4A5(): pass

    label('loc_4A5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_4C1',
    )

    MapSetFlags(0x00000010)
    OP_11(0xE6, 0xF0, 0xFF, 0, 60000, 0)

    def _loc_4C1(): pass

    label('loc_4C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4D0',
    )

    SetScenaFlags(ScenaFlag(0x0311, 0, 0x1888))

    def _loc_4D0(): pass

    label('loc_4D0')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4E2',
    )

    OP_C4(0x00, 0x00000004)

    def _loc_4E2(): pass

    label('loc_4E2')

    Return()

# id: 0x0002 offset: 0x4E3
@scena.Code('func_02_4E3')
def func_02_4E3():
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
        'loc_508',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_64A')

    def _loc_508(): pass

    label('loc_508')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_521',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_64A')

    def _loc_521(): pass

    label('loc_521')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_53A',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_64A')

    def _loc_53A(): pass

    label('loc_53A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_553',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_64A')

    def _loc_553(): pass

    label('loc_553')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_56C',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_64A')

    def _loc_56C(): pass

    label('loc_56C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_585',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_64A')

    def _loc_585(): pass

    label('loc_585')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_59E',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_64A')

    def _loc_59E(): pass

    label('loc_59E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5B7',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_64A')

    def _loc_5B7(): pass

    label('loc_5B7')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5D0',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_64A')

    def _loc_5D0(): pass

    label('loc_5D0')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5E9',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_64A')

    def _loc_5E9(): pass

    label('loc_5E9')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_602',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_64A')

    def _loc_602(): pass

    label('loc_602')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_61B',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_64A')

    def _loc_61B(): pass

    label('loc_61B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_634',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_64A')

    def _loc_634(): pass

    label('loc_634')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_64A',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_64A(): pass

    label('loc_64A')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_65F',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_64A')

    def _loc_65F(): pass

    label('loc_65F')

    Return()

# id: 0x0003 offset: 0x660
@scena.Code('func_03_660')
def func_03_660():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_683',
    )

    OP_8D(0x00FE, 19800, 21600, 24000, 30300, 3000)

    Jump('func_03_660')

    def _loc_683(): pass

    label('loc_683')

    Return()

# id: 0x0004 offset: 0x684
@scena.Code('func_04_684')
def func_04_684():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_6A7',
    )

    OP_8D(0x00FE, 19800, 21600, 28200, 24800, 3000)

    Jump('func_04_684')

    def _loc_6A7(): pass

    label('loc_6A7')

    Return()

# id: 0x0005 offset: 0x6A8
@scena.Code('func_05_6A8')
def func_05_6A8():
    ChrSetFlags(0x00FE, 0x0040)
    OP_8D(0x00FE, 28710, 33610, 41830, 44000, 0)

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            Expr.Rand,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_6D1(): pass

    label('loc_6D1')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_7F4',
    )

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0xBB8),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Gtr,
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0xBB8),
            Expr.Sub,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Lss,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0xBB8),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Gtr,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0xBB8),
            Expr.Sub,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7B9',
    )

    If(
        (
            (Expr.PushLong, 0x7026),
            (Expr.PushLong, 0x3E8),
            Expr.Add,
            (Expr.GetChrWork, 0xFE, 0x1),
            Expr.Lss,
            (Expr.PushLong, 0x834A),
            (Expr.PushLong, 0x3E8),
            Expr.Add,
            (Expr.GetChrWork, 0xFE, 0x3),
            Expr.Lss,
            Expr.Nez64,
            (Expr.PushLong, 0xA366),
            (Expr.PushLong, 0x3E8),
            Expr.Sub,
            (Expr.GetChrWork, 0xFE, 0x1),
            Expr.Gtr,
            Expr.Nez64,
            (Expr.PushLong, 0xABE0),
            (Expr.PushLong, 0x3E8),
            Expr.Sub,
            (Expr.GetChrWork, 0xFE, 0x3),
            Expr.Gtr,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_78E',
    )

    ChrSetFlags(0x00FE, 0x0020)
    ChrTurnDirection(0x00FE, 0x0000, 0)
    ChrClearFlags(0x00FE, 0x0020)

    @scena.Lambda('lambda_077B')
    def lambda_077B():
        OP_94(0x00, 0x00FE, 0x00B4, 0x0000012C, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_077B)

    Jump('loc_7B1')

    def _loc_78E(): pass

    label('loc_78E')

    @scena.Lambda('lambda_0794')
    def lambda_0794():
        OP_8D(0x00FE, 28710, 33610, 41830, 44000, 6000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0794)

    Sleep(200)

    def _loc_7B1(): pass

    label('loc_7B1')

    Sleep(30)

    Jump('loc_7F1')

    def _loc_7B9(): pass

    label('loc_7B9')

    Sleep(50)

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x28),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7F1',
    )

    TerminateThread(0x00FE, 0x02)

    @scena.Lambda('lambda_07D9')
    def lambda_07D9():
        OP_8D(0x00FE, 28710, 33610, 41830, 44000, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_07D9)

    def _loc_7F1(): pass

    label('loc_7F1')

    Jump('loc_6D1')

    def _loc_7F4(): pass

    label('loc_7F4')

    Return()

# id: 0x0006 offset: 0x7F5
@scena.Code('func_06_7F5')
def func_06_7F5():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_90B',
    )

    ChrWalkTo(0x00FE, 24040, 0, 39800, 2000, 0x00)
    ChrWalkTo(0x00FE, 19620, 0, 39650, 2000, 0x00)
    Sleep(2000)

    ChrWalkTo(0x00FE, 24040, 0, 39800, 2000, 0x00)
    ChrWalkTo(0x00FE, 24490, 0, 30670, 2000, 0x00)
    ChrWalkTo(0x00FE, 34190, 190, 31180, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)
    Sleep(2000)

    ChrWalkTo(0x00FE, 34070, 0, 18590, 2000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)
    Sleep(2000)

    ChrWalkTo(0x00FE, 29200, 0, 18510, 2000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)
    Sleep(2000)

    ChrWalkTo(0x00FE, 29030, 300, 22190, 2000, 0x00)
    ChrWalkTo(0x00FE, 23950, 0, 23280, 2000, 0x00)
    ChrWalkTo(0x00FE, 23820, 60, 54060, 2000, 0x00)
    Sleep(2000)

    ChrWalkTo(0x00FE, 23960, 140, 43890, 2000, 0x00)

    Jump('func_06_7F5')

    def _loc_90B(): pass

    label('loc_90B')

    Return()

# id: 0x0007 offset: 0x90C
@scena.Code('func_07_90C')
def func_07_90C():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_EBA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0415, 1, 0x20A9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D0E',
    )

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x0101,
        (
            '#1001F呀哈——缇欧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F啊，好久不见了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '艾丝蒂尔？\n',
            '还有约修亚！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F嘿嘿，久等了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F让缇欧担心了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哪里，没关系的。\n',
            '事情经过我也听说了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最担心你的\n',
            '还是艾丝蒂尔啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了你她可是大哭了好几次，\n',
            '让少女流泪可是很严重的罪过哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1008F别、别说啦缇欧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1054F呵呵……\n',
            '我已经深深反省过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '今后一定会用更多的时间\n',
            '来弥补自己的过失。',
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
        'loc_B14',
    )

    ChrTalk(
        0x00FE,
        (
            '……对了，你们…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和雪拉姐在一起行动，\n',
            '难道今天又有工作了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B41')

    def _loc_B14(): pass

    label('loc_B14')

    ChrTalk(
        0x00FE,
        (
            '……对了，你们，\n',
            '难道今天又有工作了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B41(): pass

    label('loc_B41')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 3, 0x2003)),
            Expr.Return,
        ),
        'loc_BD8',
    )

    ChrTalk(
        0x0101,
        (
            '#1006F嗯，正在洛连特的周边\n',
            '地区进行巡视。',
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
        'loc_BAE',
    )

    ChrTalk(
        0x0103,
        (
            '#020F顺便掌握一下\n',
            '这一带的情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BD5')

    def _loc_BAE(): pass

    label('loc_BAE')

    ChrTalk(
        0x0102,
        (
            '#1040F顺便掌握一下\n',
            '这一带的情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BD5(): pass

    label('loc_BD5')

    Jump('loc_C4C')

    def _loc_BD8(): pass

    label('loc_BD8')

    ChrTalk(
        0x0101,
        (
            '#1006F嗯，接下来\n',
            '要去洛连特。',
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
        'loc_C2C',
    )

    ChrTalk(
        0x0103,
        (
            '#020F有些东西要\n',
            '送到协会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C4C')

    def _loc_C2C(): pass

    label('loc_C2C')

    ChrTalk(
        0x0102,
        (
            '#1040F有东西要送到协会去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C4C(): pass

    label('loc_C4C')

    ChrTalk(
        0x00FE,
        (
            '是吗……\n',
            '游击士的工作果然很辛苦啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，难得２个人一起\n',
            '回到洛连特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '工作结束以后\n',
            '请一定再来玩啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F嗯！一定！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F现在的状况比较不稳定，\n',
            '缇欧也要加油啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0415, 1, 0x20A9))

    Jump('loc_EB7')

    def _loc_D0E(): pass

    label('loc_D0E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_D9D',
    )

    ChrTalk(
        0x00FE,
        (
            '听说连洛连特的导力器\n',
            '也全部瘫痪了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们水泵和温室现在都无法使用了，\n',
            '真是让人头疼呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼～好久没这样徒手\n',
            '拎水桶了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EB7')

    def _loc_D9D(): pass

    label('loc_D9D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E5B',
    )

    ChrTalk(
        0x00FE,
        (
            '还有警备艇的迫降\n',
            '也让人很吃惊啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然士兵们说过，\n',
            '已经提出救援请求了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过仔细想想，\n',
            '救援部队大概也做不了什么吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯…他们的撤退也可能\n',
            '只是时间问题吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_EB7')

    def _loc_E5B(): pass

    label('loc_E5B')

    ChrTalk(
        0x00FE,
        (
            '街道中那警备艇的\n',
            '迫降让我吃了一惊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，世上总是有\n',
            '让人意想不到的事情发生啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EB7(): pass

    label('loc_EB7')

    Jump('loc_1594')

    def _loc_EBA(): pass

    label('loc_EBA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_11DF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034C, 5, 0x1A65)),
            Expr.Return,
        ),
        'loc_F32',
    )

    ChrTalk(
        0x00FE,
        (
            '真是要感谢\n',
            '凯文神父啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不但在这里保护我们，\n',
            '而且还陪孩子们玩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是受了他\n',
            '太多照顾了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11DC')

    def _loc_F32(): pass

    label('loc_F32')

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '啊，艾丝蒂尔和雪拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1001F呀哈——缇欧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F身体已经没事了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0103, 400)

    ChrTalk(
        0x00FE,
        (
            '是的，已经完全好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '事情的经过已经听\n',
            '凯文神父说过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '真是让大家\n',
            '担心了…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，不用再担心了啦。\n',
            '大家都已经没事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1025F嗯、太好了……真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '刚醒来的时候\n',
            '还真是吃了一惊呢，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '忽然就发现眼前\n',
            '站着凯文神父。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F啊哈哈……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '确实会让人吓一跳呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#021F呵呵，不管怎么说，\n',
            '他其实是个很有意思的人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '其实我一开始也不大相信\n',
            '他会是神父，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但他却一直默默地\n',
            '守护着我们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然没办法对他作出什么回报，\n',
            '不过真的是非常感谢他呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在回去之前他还和孩子们\n',
            '一起玩了好久。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是受了他\n',
            '太多照顾了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x034C, 5, 0x1A65))

    def _loc_11DC(): pass

    label('loc_11DC')

    Jump('loc_1594')

    def _loc_11DF(): pass

    label('loc_11DF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_1594',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0313, 4, 0x189C)),
            Expr.Return,
        ),
        'loc_1247',
    )

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '查儿和维鲁也\n',
            '很想约修亚呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '等工作告一段落之后\n',
            '你们两个要一起来玩啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1594')

    def _loc_1247(): pass

    label('loc_1247')

    ChrTalk(
        0x0101,
        (
            '#1018F呀哈！缇欧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x00FE, 0x0101, 400)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '啊，艾丝蒂尔！\n',
            '好久没见了啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和雪拉姐在一起…\n',
            '艾丝蒂尔正在工作吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F嗯，是啊，\n',
            '我们正在调查中。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1006F不过不是什么严重事件，\n',
            '不用担心啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '嗯，那就好，不过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '……嘿，艾丝蒂尔。\n',
            '那件衣服，是怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F哈哈……你果然注意到了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那是雪拉姐为了庆祝我升为正游击士\n',
            '而买给我的礼物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿～雪拉姐\n',
            '的眼光真不错，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这身衣服真漂亮，\n',
            '非常适合你呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今后你也要多穿\n',
            '各种好看的裙子啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1008F嘿、嘿嘿……谢谢啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '约修亚的事情\n',
            '我也听伊莉莎说了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '艾丝蒂尔一定很难过吧…\n',
            '如果愿意的话随时来找我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在心情不好的时候，如果能找朋友\n',
            '倾诉就会舒服一些……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1025F啊、嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '谢谢你……\n',
            '我不会客气的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1006F嘿、缇欧。\n',
            '这么久没见了，再和你一起聊天真开心⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，我也是啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '艾丝蒂尔以后还要再来玩啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x000B, 0x0010)
    SetScenaFlags(ScenaFlag(0x0313, 4, 0x189C))

    def _loc_1594(): pass

    label('loc_1594')

    TalkEnd(0x000B)

    Return()

# id: 0x0008 offset: 0x1598
@scena.Code('func_08_1598')
def func_08_1598():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_17A2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034C, 6, 0x1A66)),
            Expr.Return,
        ),
        'loc_1627',
    )

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '以前就经常靠你们帮忙驱赶魔兽，\n',
            '这次又多亏了你们呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '像你们这样的游击士\n',
            '对我们来说真的是最可以依靠的人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17A2')

    def _loc_1627(): pass

    label('loc_1627')

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '喔，艾丝蒂尔和雪拉扎德啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊，从最初的驱赶魔兽工作开始\n',
            '就一直受你们的照顾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '具体事情我听凯文神父说了，\n',
            '真正的功劳还是你们的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1007F嗯嗯、哪里……\n',
            '我们的力量还远远不够呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '在这次的事件中\n',
            '更加认识到了这一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈，不要再谦虚了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在不断的经验中成长，\n',
            '可是你们年轻人的特权。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从今以后也要\n',
            '保持着这份信心啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x034C, 6, 0x1A66))

    def _loc_17A2(): pass

    label('loc_17A2')

    TalkEnd(0x000E)

    Return()

# id: 0x0009 offset: 0x17A6
@scena.Code('func_09_17A6')
def func_09_17A6():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_1824',
    )

    ChrTalk(
        0x00FE,
        (
            '凯文神父……\n',
            '真是个很好的人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说话和善风趣，\n',
            '还陪我们一起玩……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '让我不自觉地\n',
            '想起了约修亚呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_198E')

    def _loc_1824(): pass

    label('loc_1824')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_198E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0313, 5, 0x189D)),
            Expr.Return,
        ),
        'loc_1883',
    )

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '下次再来的时候……\n',
            '要带着约修亚一起哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '查儿会一直等你们的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_198E')

    def _loc_1883(): pass

    label('loc_1883')

    OP_62(0x00FE, 0x00000000, 1700, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '啊，艾丝蒂尔姐姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F早啊，查儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那、那个……\n',
            '约修亚呢……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F啊、嗯……他最近有点事，\n',
            '自己单独行动去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这，这样啊……\n',
            '………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个……\n',
            '到时要一起来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '查儿会一直等你们的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0313, 5, 0x189D))

    def _loc_198E(): pass

    label('loc_198E')

    TalkEnd(0x000D)

    Return()

# id: 0x000A offset: 0x1992
@scena.Code('func_0A_1992')
def func_0A_1992():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_1AAB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_19E2',
    )

    ChrTalk(
        0x00FE,
        (
            '神父哥哥真是个有趣的人！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，希望他以后再来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AA8')

    def _loc_19E2(): pass

    label('loc_19E2')

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '啊，艾丝蒂尔！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '刚一睁眼，发现旁边有个\n',
            '英俊又奇怪的神父，真吓了一跳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，他还真是个有意思的人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然身为神父，\n',
            '却带着那么帅气的武器。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，希望他以后再来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_1AA8(): pass

    label('loc_1AA8')

    Jump('loc_1BAA')

    def _loc_1AAB(): pass

    label('loc_1AAB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_1BAA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1B06',
    )

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '虽然好久没见了，\n',
            '不过，还有工作要去做。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，真是没意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BAA')

    def _loc_1B06(): pass

    label('loc_1B06')

    OP_62(0x00FE, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '啊～艾丝蒂尔！\n',
            '是来找我玩的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1007F呼、不好意思啦，\n',
            '这次是为工作而来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉～这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，真是没意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_1BAA(): pass

    label('loc_1BAA')

    TalkEnd(0x000C)

    Return()

# id: 0x000B offset: 0x1BAE
@scena.Code('func_0B_1BAE')
def func_0B_1BAE():
    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1C31',
    )

    CreateThread(0x00FE, 0x02, 0x00, func_0C_1C32)
    PlaySE(401, 0x00, 0x64)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Rand,
            (Expr.PushLong, 0xA),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1C31',
    )

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['新鲜鸡蛋'], 1)"),
            Expr.Return,
        ),
        'loc_1C31',
    )

    TalkBegin(0x00FE)
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['新鲜鸡蛋']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FE)

    def _loc_1C31(): pass

    label('loc_1C31')

    Return()

# id: 0x000C offset: 0x1C32
@scena.Code('func_0C_1C32')
def func_0C_1C32():
    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x7),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1C4D',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Yield()

    Jump('func_0C_1C32')

    def _loc_1C4D(): pass

    label('loc_1C4D')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x000D offset: 0x1C58
@scena.Code('func_0D_1C58')
def func_0D_1C58():
    PlaySE(400, 0x00, 0x64)

    Return()

# id: 0x000E offset: 0x1C5E
@scena.Code('func_0E_1C5E')
def func_0E_1C5E():
    TalkBegin(0x0015)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_1CCD',
    )

    ChrTalk(
        0x00FE,
        (
            '啊啊，救援部队还\n',
            '没有到来…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个农场能平安无事当然很好，\n',
            '不过我也很担心王国的其他地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DD1')

    def _loc_1CCD(): pass

    label('loc_1CCD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1DD1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D73',
    )

    ChrTalk(
        0x00FE,
        (
            '我是迫降在附近街道上的警备艇\n',
            '上的王国军士兵…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但经常受农场各位的照顾，\n',
            '如今也要帮忙警备才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我能做出的回报\n',
            '也只有这一点而已了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_1DD1')

    def _loc_1D73(): pass

    label('loc_1D73')

    ChrTalk(
        0x00FE,
        (
            '经常受农场各位的照顾，\n',
            '如今也要帮忙警备才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '街道的路灯已经全熄灭了，\n',
            '似乎很混乱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1DD1(): pass

    label('loc_1DD1')

    TalkEnd(0x0015)

    Return()

# id: 0x000F offset: 0x1DD5
@scena.Code('func_0F_1DD5')
def func_0F_1DD5():
    TalkBegin(0x0016)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_1E42',
    )

    ChrTalk(
        0x00FE,
        (
            '像这样悠闲自在度过的一天，\n',
            '已经很久没有享受到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像已经忘了\n',
            '现在处于紧急状况中呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1ECA')

    def _loc_1E42(): pass

    label('loc_1E42')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1ECA',
    )

    ChrTalk(
        0x00FE,
        (
            '这里的温室和水泵\n',
            '已经全都不能用了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要是使用导力的道具\n',
            '就全部瘫痪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们的飞艇坠落大概\n',
            '也是因为这种现象吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1ECA(): pass

    label('loc_1ECA')

    TalkEnd(0x0016)

    Return()

# id: 0x0010 offset: 0x1ECE
@scena.Code('func_10_1ECE')
def func_10_1ECE():
    EventBegin(0x00)
    OP_DB()
    ChrSetPos(0x0101, 23540, 0, 59780, 180)
    ChrSetPos(0x0103, 24540, 80, 59780, 180)
    ChrSetPos(0x0107, 23540, 0, 60780, 180)
    ChrSetPos(0x0105, 24540, 0, 60780, 180)
    CameraMove(44190, 0, 16580, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3830, 0)
    OP_6C(269000, 0)
    OP_6E(261, 0)
    OP_C8(0x0200, 0x0046, 'C_PLAC14._CH', 0x00, 0x07D0)
    ShowPlaceName('帕赛尔农场')
    FadeIn(2000, 0)

    @scena.Lambda('lambda_1F82')
    def lambda_1F82():
        OP_6C(0, 12000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1F82)

    CameraMove(22290, 0, 23280, 6000)

    @scena.Lambda('lambda_1FA3')
    def lambda_1FA3():
        CameraMove(24020, 0, 51850, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1FA3)

    Sleep(4000)

    CreateThread(0x0101, 0x01, 0x00, func_11_2877)
    Sleep(200)

    CreateThread(0x0103, 0x01, 0x00, func_12_28BC)
    Sleep(200)

    CreateThread(0x0107, 0x01, 0x00, func_13_2901)
    Sleep(200)

    CreateThread(0x0105, 0x01, 0x00, func_14_293A)
    WaitForThreadExit(0x0105, 0x0001)
    Sleep(500)

    Fade(1000)
    CameraMove(23830, 50, 51930, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_DC()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_20C5',
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
            TXT(0x00, '【◇之前曾经来访过】\n'),
            TXT(0x01, '【◇之前没有来访过】\n'),
            TXT(0x02, '【◇不变更】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_20B9'),
        (0x00000001, 'loc_20BF'),
        (-1, 'loc_20C5'),
    )

    def _loc_20B9(): pass

    label('loc_20B9')

    SetScenaFlags(ScenaFlag(0x0311, 0, 0x1888))

    Jump('loc_20C5')

    def _loc_20BF(): pass

    label('loc_20BF')

    ClearScenaFlags(ScenaFlag(0x0311, 0, 0x1888))

    Jump('loc_20C5')

    def _loc_20C5(): pass

    label('loc_20C5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0311, 0, 0x1888)),
            Expr.Return,
        ),
        'loc_2105',
    )

    ChrTalk(
        0x0101,
        (
            '#0010290576V#1026F#5P昨天这里\n',
            '都完全没有雾的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2172')

    def _loc_2105(): pass

    label('loc_2105')

    ChrTalk(
        0x0101,
        (
            '#0010290577V#1025F#5P缇欧的家……\n',
            '真是有些怀念呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290578V#1007F不过看来……\n',
            '这里的雾也很浓了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2172(): pass

    label('loc_2172')

    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030290579V#020F#6P还是赶快将事情\n',
            '向这里的主人说明吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290580V在现在这样的浓雾天气，\n',
            '应该不会出门吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010290581V#1015F#5P嗯、嗯嗯……\n',
            '我想应该不会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)
    Sleep(200)

    PlaySE(280, 0x00, 0x4B)
    Sleep(500)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0107, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_22AA')
    def lambda_22AA():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_22AA)

    ChrSetDirection(0x0101, 180, 400)

    ChrTalk(
        0x0107,
        (
            '#0070290582V#065F这、这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060290583V#042F#2P……难道……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290584V#1005F#5P雪拉姐！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290585V#024F#6P快去看看！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlayBGM(86)
    Sleep(300)

    @scena.Lambda('lambda_2358')
    def lambda_2358():
        CameraMove(23310, 0, 25480, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2358)

    @scena.Lambda('lambda_2370')
    def lambda_2370():
        OP_67(0, 5180, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2370)

    @scena.Lambda('lambda_2388')
    def lambda_2388():
        OP_6E(290, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2388)

    @scena.Lambda('lambda_2398')
    def lambda_2398():
        CameraSetDistance(3190, 4000)

        ExitThread()

    DispatchAsync(0x0103, 0x0002, lambda_2398)

    @scena.Lambda('lambda_23A8')
    def lambda_23A8():
        OP_6C(180000, 4000)

        ExitThread()

    DispatchAsync(0x0103, 0x0003, lambda_23A8)

    CreateThread(0x0101, 0x01, 0x00, func_15_2973)
    Sleep(300)

    CreateThread(0x0103, 0x01, 0x00, func_16_29B7)
    Sleep(200)

    CreateThread(0x0107, 0x01, 0x00, func_17_29FB)
    Sleep(300)

    CreateThread(0x0105, 0x01, 0x00, func_18_2A3F)
    SetScenaFlags(ScenaFlag(0x0304, 0, 0x1820))
    OP_28(0x0091, 0x01, 0x0004)
    LoadEffect(0x00, 'map\\\\mp107_00.eff')
    Sleep(2800)

    ChrSetPos(0x0008, 21820, 1200, 25100, 45)
    ChrSetPos(0x0009, 20580, 1300, 25650, 45)
    ChrSetPos(0x000A, 22800, 1300, 23640, 45)
    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0009, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x000A, 255, 255, 255, 0, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetFlags(0x0009, 0x0004)
    ChrSetFlags(0x000A, 0x0004)
    PlaySE(529, 0x00, 0x64)
    PlaySE(533, 0x00, 0x64)
    PlayEffect(0x00, 0x00, 0x0008, 0, 300, 0, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 1000)

    @scena.Lambda('lambda_24B6')
    def lambda_24B6():
        ChrMoveTo(0x00FE, 21820, 700, 25100, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_24B6)

    @scena.Lambda('lambda_24D1')
    def lambda_24D1():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_24D1)

    Sleep(300)

    PlaySE(529, 0x00, 0x64)
    PlaySE(533, 0x00, 0x64)
    PlayEffect(0x00, 0x01, 0x0009, 0, 300, 0, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 1000)

    @scena.Lambda('lambda_2527')
    def lambda_2527():
        ChrMoveTo(0x00FE, 20580, 800, 25650, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_2527)

    @scena.Lambda('lambda_2542')
    def lambda_2542():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2542)

    Sleep(300)

    PlaySE(529, 0x00, 0x64)
    PlaySE(533, 0x00, 0x64)
    PlayEffect(0x00, 0x02, 0x000A, 0, 300, 0, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 1000)

    @scena.Lambda('lambda_2598')
    def lambda_2598():
        ChrMoveTo(0x00FE, 22800, 800, 23640, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_2598)

    @scena.Lambda('lambda_25B3')
    def lambda_25B3():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_25B3)

    WaitForThreadExit(0x0101, 0x0003)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010290586V#1020F#6P啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x000A, 0x0001)
    Sleep(500)

    StopEffect(0x00, 0x02)
    StopEffect(0x01, 0x02)
    StopEffect(0x02, 0x02)

    ChrTalk(
        0x0101,
        (
            '#0010290587V#1005F#6P这、这些家伙！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060290588V#043F#6P雾魔……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070290589V#065F#6P呼啊啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290590V#024F#6P没有时间发呆！！\n',
            '打倒它们！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0101, 1)
    ChrSetSubChip(0x0101, 0)
    Sleep(50)

    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0103, 5)
    ChrSetSubChip(0x0103, 0)
    Sleep(50)

    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0105, 7)
    ChrSetSubChip(0x0105, 0)
    Sleep(50)

    PlaySE(216, 0x00, 0x64)
    ChrSetChipByIndex(0x0107, 3)
    ChrSetSubChip(0x0107, 0)
    OP_0D()
    Sleep(500)

    @scena.Lambda('lambda_270E')
    def lambda_270E():
        CameraMove(22500, 0, 26430, 200)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_270E)

    @scena.Lambda('lambda_2726')
    def lambda_2726():
        CameraSetDistance(2400, 200)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2726)

    ChrSetFlags(0x0101, 0x1000)
    ChrSetChipByIndex(0x0101, 2)

    @scena.Lambda('lambda_2740')
    def lambda_2740():
        ChrWalkTo(0x00FE, 22360, 0, 27580, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2740)

    ChrSetChipByIndex(0x0008, 9)

    @scena.Lambda('lambda_2760')
    def lambda_2760():
        ChrWalkTo(0x00FE, 22290, 500, 26150, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_2760)

    Sleep(50)

    ChrSetFlags(0x0103, 0x1000)
    ChrSetChipByIndex(0x0103, 6)

    @scena.Lambda('lambda_278A')
    def lambda_278A():
        ChrWalkTo(0x00FE, 23310, 0, 27060, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0000, lambda_278A)

    ChrSetChipByIndex(0x0009, 9)

    @scena.Lambda('lambda_27AA')
    def lambda_27AA():
        ChrWalkTo(0x00FE, 21240, 600, 26290, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_27AA)

    Sleep(50)

    ChrSetFlags(0x0107, 0x1000)
    ChrSetChipByIndex(0x0107, 4)

    @scena.Lambda('lambda_27D4')
    def lambda_27D4():
        ChrWalkTo(0x00FE, 22330, 0, 28610, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0000, lambda_27D4)

    ChrSetChipByIndex(0x000A, 9)

    @scena.Lambda('lambda_27F4')
    def lambda_27F4():
        ChrWalkTo(0x00FE, 23030, 700, 25300, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_27F4)

    Sleep(50)

    ChrSetFlags(0x0105, 0x1000)
    ChrSetChipByIndex(0x0105, 8)

    @scena.Lambda('lambda_281E')
    def lambda_281E():
        ChrWalkTo(0x00FE, 23310, 90, 27060, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0000, lambda_281E)

    Sleep(200)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0103, 0xFF)
    TerminateThread(0x0107, 0xFF)
    TerminateThread(0x0105, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    Battle(0x00000799, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_286D'),
        (-1, 'loc_2872'),
    )

    def _loc_286D(): pass

    label('loc_286D')

    OP_B4(0x00)

    Jump('loc_2872')

    def _loc_2872(): pass

    label('loc_2872')

    Call(0, 0x0019)

    Return()

# id: 0x0011 offset: 0x2877
@scena.Code('func_11_2877')
def func_11_2877():
    ChrWalkTo(0x00FE, 23540, 70, 51000, 2000, 0x00)
    Sleep(200)

    ChrSetDirection(0x00FE, 270, 400)
    Sleep(500)

    ChrSetDirection(0x00FE, 180, 400)
    Sleep(100)

    ChrSetDirection(0x00FE, 135, 400)
    Sleep(500)

    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x0012 offset: 0x28BC
@scena.Code('func_12_28BC')
def func_12_28BC():
    ChrWalkTo(0x00FE, 24540, 100, 51000, 2000, 0x00)
    Sleep(200)

    ChrSetDirection(0x00FE, 90, 400)
    Sleep(400)

    ChrSetDirection(0x00FE, 180, 400)
    Sleep(100)

    ChrSetDirection(0x00FE, 225, 400)
    Sleep(600)

    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x0013 offset: 0x2901
@scena.Code('func_13_2901')
def func_13_2901():
    ChrWalkTo(0x00FE, 23540, 220, 52000, 2000, 0x00)
    Sleep(200)

    ChrSetDirection(0x00FE, 270, 400)
    Sleep(100)

    ChrSetDirection(0x00FE, 315, 400)
    Sleep(500)

    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x0014 offset: 0x293A
@scena.Code('func_14_293A')
def func_14_293A():
    ChrWalkTo(0x00FE, 24540, 200, 52000, 2000, 0x00)
    Sleep(200)

    ChrSetDirection(0x00FE, 90, 400)
    Sleep(100)

    ChrSetDirection(0x00FE, 45, 400)
    Sleep(500)

    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x0015 offset: 0x2973
@scena.Code('func_15_2973')
def func_15_2973():
    ChrWalkTo(0x00FE, 24150, 0, 48270, 5000, 0x00)
    ChrWalkTo(0x00FE, 24100, 0, 36000, 5000, 0x00)
    ChrWalkTo(0x00FE, 23800, 80, 29860, 5000, 0x00)
    ChrSetDirection(0x00FE, 225, 400)

    Return()

# id: 0x0016 offset: 0x29B7
@scena.Code('func_16_29B7')
def func_16_29B7():
    ChrWalkTo(0x00FE, 24150, 0, 48270, 5000, 0x00)
    ChrWalkTo(0x00FE, 24100, 0, 37000, 5000, 0x00)
    ChrWalkTo(0x00FE, 24920, 60, 29280, 5000, 0x00)
    ChrSetDirection(0x00FE, 225, 400)

    Return()

# id: 0x0017 offset: 0x29FB
@scena.Code('func_17_29FB')
def func_17_29FB():
    ChrWalkTo(0x00FE, 24150, 0, 48270, 5000, 0x00)
    ChrWalkTo(0x00FE, 24100, 0, 38000, 5000, 0x00)
    ChrWalkTo(0x00FE, 24010, 20, 31410, 5000, 0x00)
    ChrSetDirection(0x00FE, 225, 400)

    Return()

# id: 0x0018 offset: 0x2A3F
@scena.Code('func_18_2A3F')
def func_18_2A3F():
    ChrWalkTo(0x00FE, 24150, 0, 48270, 5000, 0x00)
    ChrWalkTo(0x00FE, 24100, 0, 39000, 5000, 0x00)
    ChrWalkTo(0x00FE, 25060, 0, 30710, 5000, 0x00)
    ChrSetDirection(0x00FE, 225, 400)

    Return()

# id: 0x0019 offset: 0x2A83
@scena.Code('func_19_2A83')
def func_19_2A83():
    EventBegin(0x00)
    PlayBGM(81)
    FadeOut(0, 0, -1)
    OP_0D()
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    TerminateThread(0x0101, 0x00)
    TerminateThread(0x0103, 0x00)
    TerminateThread(0x0107, 0x00)
    TerminateThread(0x0105, 0x00)
    ChrClearFlags(0x0101, 0x1000)
    ChrClearFlags(0x0103, 0x1000)
    ChrClearFlags(0x0107, 0x1000)
    ChrClearFlags(0x0105, 0x1000)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0103, 65535)
    ChrSetSubChip(0x0103, 0)
    ChrSetChipByIndex(0x0107, 65535)
    ChrSetSubChip(0x0107, 0)
    ChrSetChipByIndex(0x0105, 65535)
    ChrSetSubChip(0x0105, 0)
    ChrSetPos(0x0101, 21610, 0, 25150, 225)
    ChrSetPos(0x0103, 22820, 0, 25050, 135)
    ChrSetPos(0x0107, 22880, 0, 26430, 90)
    ChrSetPos(0x0105, 21580, 0, 26380, 315)
    CameraMove(21690, 0, 25340, 0)
    OP_67(0, 8180, -10000, 0)
    CameraSetDistance(2470, 0)
    OP_6C(224000, 0)
    OP_6E(262, 0)
    CreateThread(0x0101, 0x01, 0x00, func_1E_2D03)
    CreateThread(0x0103, 0x01, 0x00, func_1F_2D34)
    CreateThread(0x0107, 0x01, 0x00, func_20_2D59)
    CreateThread(0x0105, 0x01, 0x00, func_21_2D7E)
    FadeIn(2000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010290591V#1026F打、打倒了……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0103, 0x0001)
    ChrSetDirection(0x0103, 270, 400)

    ChrTalk(
        0x0103,
        (
            '#0030290592V#022F嗯……\n',
            '不过这些家伙的目标只是为了牵制住我们而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290593V赶快找到这里的主人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2C3F')
    def lambda_2C3F():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2C3F)

    Sleep(100)

    @scena.Lambda('lambda_2C52')
    def lambda_2C52():
        ChrSetDirection(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_2C52)

    Sleep(100)

    ChrSetDirection(0x0105, 160, 400)

    ChrTalk(
        0x0101,
        (
            '#0010290594V#1005F嗯、嗯！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0304, 1, 0x1821))
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

# id: 0x001A offset: 0x2C93
@scena.Code('func_1A_2C93')
def func_1A_2C93():
    ChrWalkTo(0x00FE, 23370, 30, 29770, 5000, 0x00)
    ChrSetDirection(0x00FE, 203, 400)

    Return()

# id: 0x001B offset: 0x2CAF
@scena.Code('func_1B_2CAF')
def func_1B_2CAF():
    ChrWalkTo(0x00FE, 24470, 30, 29320, 5000, 0x00)
    ChrSetDirection(0x00FE, 203, 400)

    Return()

# id: 0x001C offset: 0x2CCB
@scena.Code('func_1C_2CCB')
def func_1C_2CCB():
    ChrWalkTo(0x00FE, 23620, 160, 31180, 5000, 0x00)
    ChrSetDirection(0x00FE, 203, 400)

    Return()

# id: 0x001D offset: 0x2CE7
@scena.Code('func_1D_2CE7')
def func_1D_2CE7():
    ChrWalkTo(0x00FE, 25190, 0, 30460, 5000, 0x00)
    ChrSetDirection(0x00FE, 203, 400)

    Return()

# id: 0x001E offset: 0x2D03
@scena.Code('func_1E_2D03')
def func_1E_2D03():
    Sleep(400)

    ChrSetDirection(0x00FE, 340, 400)
    Sleep(500)

    ChrSetDirection(0x00FE, 250, 400)
    Sleep(100)

    ChrSetDirection(0x00FE, 161, 400)
    Sleep(500)

    ChrSetDirection(0x00FE, 206, 400)

    Return()

# id: 0x001F offset: 0x2D34
@scena.Code('func_1F_2D34')
def func_1F_2D34():
    Sleep(550)

    ChrSetDirection(0x00FE, 250, 400)
    Sleep(200)

    ChrSetDirection(0x00FE, 120, 400)
    Sleep(500)

    ChrSetDirection(0x00FE, 70, 400)

    Return()

# id: 0x0020 offset: 0x2D59
@scena.Code('func_20_2D59')
def func_20_2D59():
    Sleep(450)

    ChrSetDirection(0x00FE, 70, 400)
    Sleep(600)

    ChrSetDirection(0x00FE, 300, 400)
    Sleep(500)

    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x0021 offset: 0x2D7E
@scena.Code('func_21_2D7E')
def func_21_2D7E():
    Sleep(500)

    ChrSetDirection(0x00FE, 340, 400)
    Sleep(200)

    ChrSetDirection(0x00FE, 116, 400)
    Sleep(400)

    ChrSetDirection(0x00FE, 250, 400)

    Return()

# id: 0x0022 offset: 0x2DA3
@scena.Code('func_22_2DA3')
def func_22_2DA3():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 0, 0x1820)),
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 1, 0x1821)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2F27',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2E01',
    )

    ChrTalk(
        0x0101,
        (
            '#0010290595V#1000F（我在干什么啊！\n',
            '  为什么要到这里来？！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F07')

    def _loc_2E01(): pass

    label('loc_2E01')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2E5E',
    )

    ChrTalk(
        0x0101,
        (
            '#0010290596V#1000F雪拉姐！\n',
            '不是那边啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290597V#020F！明白了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F07')

    def _loc_2E5E(): pass

    label('loc_2E5E')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2EBD',
    )

    ChrTalk(
        0x0101,
        (
            '#0010290598V#1000F科洛丝！\n',
            '不是那边啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060290599V#040F是！明白了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F07')

    def _loc_2EBD(): pass

    label('loc_2EBD')

    ChrTalk(
        0x0101,
        (
            '#0010290600V#1000F提妲！\n',
            '不是那边啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070290601V#060F嗯、嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2F07(): pass

    label('loc_2F07')

    ChrMoveToRelative(0x0000, -1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    MapSetFlags(0x02000000)

    def _loc_2F27(): pass

    label('loc_2F27')

    Return()

# id: 0x0023 offset: 0x2F28
@scena.Code('func_23_2F28')
def func_23_2F28():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 0, 0x1820)),
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_309F',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2F8A',
    )

    ChrTalk(
        0x0101,
        (
            '#0010290602V#1002F（我在干什么啊！\n',
            '  现在必须先赶快找到缇欧！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_307F')

    def _loc_2F8A(): pass

    label('loc_2F8A')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2FDF',
    )

    ChrTalk(
        0x0103,
        (
            '#0030290603V#022F（不能再耽误时间了！！\n',
            '  必须要赶快找到大家！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_307F')

    def _loc_2FDF(): pass

    label('loc_2FDF')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3034',
    )

    ChrTalk(
        0x0105,
        (
            '#0060290604V#042F（……那边是出口了啊，\n',
            '  现在要赶快找到大家！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_307F')

    def _loc_3034(): pass

    label('loc_3034')

    ChrTalk(
        0x0101,
        (
            '#0010290605V#1002F提妲！那边是出口啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070290606V#062F啊、嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_307F(): pass

    label('loc_307F')

    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    MapSetFlags(0x02000000)

    def _loc_309F(): pass

    label('loc_309F')

    Return()

# id: 0x0024 offset: 0x30A0
@scena.Code('func_24_30A0')
def func_24_30A0():
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
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3140',
    )

    ChrTalk(
        0x0101,
        (
            '#0010290607V#1004F啊，上着锁吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290608V#022F快去找找别的入口！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_3140(): pass

    label('loc_3140')

    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

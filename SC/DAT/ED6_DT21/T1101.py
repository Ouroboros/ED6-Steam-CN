import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T1101_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1101   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1101.x'
    header.mapIndex       = 1
    header.bgm            = 11
    header.flags          = 0x0001
    header.entryFunction  = 0x0000
    header.importTable    = ['ED6_DT21/T1101._SN', 'ED6_DT21/T1101_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
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
        ('ED6_DT07/CH02360._CH', 'ED6_DT07/CH02360P._CP'),
        ('ED6_DT07/CH02370._CH', 'ED6_DT07/CH02370P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT07/CH01160._CH', 'ED6_DT07/CH01160P._CP'),
        ('ED6_DT07/CH01170._CH', 'ED6_DT07/CH01170P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT27/CH03790._CH', 'ED6_DT27/CH03790P._CP'),
        ('ED6_DT07/CH01230._CH', 'ED6_DT07/CH01230P._CP'),
    ]

# id: 0x10001 offset: 0x102
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '梅贝尔市长',
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
            name                = '莉拉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '雅哈多老人',
            x                   = 48310,
            z                   = 0,
            y                   = 46460,
            direction           = 262,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '哈里',
            x                   = 35880,
            z                   = 0,
            y                   = 53880,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0111,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '米娜',
            x                   = 35880,
            z                   = 0,
            y                   = 52760,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0111,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '奥维德',
            x                   = 49430,
            z                   = 0,
            y                   = 47820,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0111,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '爱蕾吉娅',
            x                   = 63060,
            z                   = 0,
            y                   = 49000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '雷塔',
            x                   = 68240,
            z                   = 0,
            y                   = 53360,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '法娜',
            x                   = 68240,
            z                   = 0,
            y                   = 51940,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '斯丁克',
            x                   = 65250,
            z                   = 0,
            y                   = 61510,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '米拉诺',
            x                   = 19300,
            z                   = 0,
            y                   = 48720,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '西柏斯街道方向',
            x                   = 4530,
            z                   = 0,
            y                   = 45190,
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
            name                = '东柏斯街道方向',
            x                   = 87650,
            z                   = 0,
            y                   = 60410,
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
            name                = '柏斯市·南街区',
            x                   = 47990,
            z                   = -3000,
            y                   = 29310,
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
            name                = '柏斯国际空港',
            x                   = 47940,
            z                   = 0,
            y                   = 93220,
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

# id: 0x10002 offset: 0x2E2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x2E2
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 25200,
            y           = 0,
            z           = 57940,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000027,
        ),
        ScenaEventData(
            x           = 18880,
            y           = 0,
            z           = 76030,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000028,
        ),
        ScenaEventData(
            x           = 36200,
            y           = 0,
            z           = 79200,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000029,
        ),
        ScenaEventData(
            x           = 59000,
            y           = 0,
            z           = 79200,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000002A,
        ),
        ScenaEventData(
            x           = 38540,
            y           = 0,
            z           = 59990,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000002B,
        ),
        ScenaEventData(
            x           = 48040,
            y           = 100,
            z           = 69500,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000002B,
        ),
        ScenaEventData(
            x           = 57480,
            y           = 0,
            z           = 60010,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000002B,
        ),
        ScenaEventData(
            x           = 48010,
            y           = 0,
            z           = 50550,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000002B,
        ),
        ScenaEventData(
            x           = 67340,
            y           = -500,
            z           = 73070,
            range       = 1500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000002C,
        ),
        ScenaEventData(
            x           = 72240,
            y           = 0,
            z           = 44910,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000002D,
        ),
        ScenaEventData(
            x           = 47960,
            y           = 0,
            z           = 85570,
            range       = 1000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000002E,
        ),
        ScenaEventData(
            x           = 43880,
            y           = 0,
            z           = 39840,
            range       = 45290,
            dword_10    = 0x000003E8,
            dword_14    = 0x0000C4F4,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000001E,
        ),
        ScenaEventData(
            x           = 56070,
            y           = 0,
            z           = 39690,
            range       = 52630,
            dword_10    = 0x000003E8,
            dword_14    = 0x0000C36E,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000001F,
        ),
    )

# id: 0x10004 offset: 0x482
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 53860,
            triggerZ            = 0,
            triggerY            = 40250,
            triggerRange        = 1700,
            actorX              = 53860,
            actorZ              = 1000,
            actorY              = 40250,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001D,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x4A6
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_527',
    )

    ChrSetFlags(0x000D, 0x0080)
    ChrSetPos(0x000A, 52840, 0, 42530, 180)
    CreateThread(0x000A, 0x00, 0x06, func_02_6D8)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_4EA',
    )

    ChrSetFlags(0x0010, 0x0080)
    ChrSetPos(0x000F, 67450, 0, 52800, 260)

    Jump('loc_524')

    def _loc_4EA(): pass

    label('loc_4EA')

    ChrSetPos(0x000E, 49520, 0, 44390, 180)
    CreateThread(0x000E, 0x00, 0x06, func_02_6D8)
    ChrSetPos(0x000B, 50500, 0, 46500, 180)
    ChrSetPos(0x000C, 51550, 0, 46750, 180)

    def _loc_524(): pass

    label('loc_524')

    Jump('loc_57A')

    def _loc_527(): pass

    label('loc_527')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_57A',
    )

    ChrSetPos(0x000A, 46680, 0, 77450, 180)
    CreateThread(0x000A, 0x00, 0x06, func_02_6D8)
    ChrSetPos(0x000E, 66340, 0, 51290, 315)
    CreateThread(0x000E, 0x00, 0x06, func_02_6D8)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x0010, 0x0080)
    ChrClearFlags(0x0011, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034A, 3, 0x1A53)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_57A',
    )

    ChrSetFlags(0x0011, 0x0010)

    def _loc_57A(): pass

    label('loc_57A')

    If(
        (
            (Expr.Eval, "OP_29(0x007B, 0x01, 0x0008)"),
            Expr.Return,
        ),
        'loc_58A',
    )

    ChrSetFlags(0x000D, 0x0080)

    def _loc_58A(): pass

    label('loc_58A')

    If(
        (
            (Expr.Eval, "OP_29(0x007C, 0x01, 0x0002)"),
            (Expr.Eval, "OP_29(0x007C, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x007C, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5AA',
    )

    ChrClearFlags(0x0012, 0x0080)

    def _loc_5AA(): pass

    label('loc_5AA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 4, 0x10F4)),
            Expr.Return,
        ),
        'loc_5C9',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x73),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    MapSetFlags(0x10000000)
    Event(0, func_0D_2257)

    Jump('loc_681')

    def _loc_5C9(): pass

    label('loc_5C9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 3, 0x10F3)),
            Expr.Return,
        ),
        'loc_5DA',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    Event(0, func_12_29C5)

    Jump('loc_681')

    def _loc_5DA(): pass

    label('loc_5DA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_5F0',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    Event(0, func_15_357A)

    Jump('loc_681')

    def _loc_5F0(): pass

    label('loc_5F0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_606',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    MapSetFlags(0x10000000)
    Event(0, func_1A_3DB5)

    Jump('loc_681')

    def _loc_606(): pass

    label('loc_606')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Return,
        ),
        'loc_61C',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    MapSetFlags(0x10000000)
    Event(1, 0x0003)

    Jump('loc_681')

    def _loc_61C(): pass

    label('loc_61C')

    If(
        (
            (Expr.Eval, "OP_29(0x007C, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x007C, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x007C, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_642',
    )

    MapSetFlags(0x10000000)
    Event(1, 0x0006)

    Jump('loc_681')

    def _loc_642(): pass

    label('loc_642')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x67),
            Expr.Equ,
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x041D, 2, 0x20EA)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_663',
    )

    Event(0, func_21_4CFE)

    Jump('loc_681')

    def _loc_663(): pass

    label('loc_663')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x65),
            Expr.Equ,
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x041D, 2, 0x20EA)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_681',
    )

    Event(0, func_22_532B)

    def _loc_681(): pass

    label('loc_681')

    Return()

# id: 0x0001 offset: 0x682
@scena.Code('func_01_682')
def func_01_682():
    OP_16(0x02, 4000, -80000, -68000, 2293825)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_6CB',
    )

    OP_72(0x000A, 0x0010)
    OP_6F(0x000A, 59)
    OP_72(0x000B, 0x0010)
    OP_6F(0x000B, 59)
    OP_72(0x000C, 0x0010)
    OP_6F(0x000C, 59)
    OP_72(0x000D, 0x0010)
    OP_6F(0x000D, 59)

    def _loc_6CB(): pass

    label('loc_6CB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6D7',
    )

    OP_64(0x00, 0x0001)

    def _loc_6D7(): pass

    label('loc_6D7')

    Return()

# id: 0x0002 offset: 0x6D8
@scena.Code('func_02_6D8')
def func_02_6D8():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_7D4',
    )

    ChrWalkTo(0x00FE, 63060, 0, 72180, 2500, 0x00)
    ChrWalkTo(0x00FE, 62120, 0, 74260, 2500, 0x00)
    ChrWalkTo(0x00FE, 61300, 0, 74790, 2500, 0x00)
    ChrWalkTo(0x00FE, 35350, 0, 74790, 2500, 0x00)
    ChrWalkTo(0x00FE, 33690, 0, 73890, 2500, 0x00)
    ChrWalkTo(0x00FE, 32840, 0, 73270, 2500, 0x00)
    ChrWalkTo(0x00FE, 32840, 0, 48230, 2500, 0x00)
    ChrWalkTo(0x00FE, 33380, 0, 46100, 2500, 0x00)
    ChrWalkTo(0x00FE, 34280, 0, 45030, 2500, 0x00)
    ChrWalkTo(0x00FE, 60310, 0, 45030, 2500, 0x00)
    ChrWalkTo(0x00FE, 61730, 0, 45510, 2500, 0x00)
    ChrWalkTo(0x00FE, 63060, 0, 47220, 2500, 0x00)

    Jump('func_02_6D8')

    def _loc_7D4(): pass

    label('loc_7D4')

    Return()

# id: 0x0003 offset: 0x7D5
@scena.Code('func_03_7D5')
def func_03_7D5():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_8D1',
    )

    ChrWalkTo(0x00FE, 36420, 0, 46460, 2000, 0x00)
    ChrWalkTo(0x00FE, 35060, 0, 46960, 2000, 0x00)
    ChrWalkTo(0x00FE, 34640, 0, 47580, 2000, 0x00)
    ChrWalkTo(0x00FE, 34640, 0, 71890, 2000, 0x00)
    ChrWalkTo(0x00FE, 35010, 0, 72960, 2000, 0x00)
    ChrWalkTo(0x00FE, 35610, 0, 73290, 2000, 0x00)
    ChrWalkTo(0x00FE, 59910, 0, 73290, 2000, 0x00)
    ChrWalkTo(0x00FE, 60980, 0, 72890, 2000, 0x00)
    ChrWalkTo(0x00FE, 61510, 0, 72290, 2000, 0x00)
    ChrWalkTo(0x00FE, 61510, 0, 47940, 2000, 0x00)
    ChrWalkTo(0x00FE, 60770, 0, 46830, 2000, 0x00)
    ChrWalkTo(0x00FE, 60290, 0, 46460, 2000, 0x00)

    Jump('func_03_7D5')

    def _loc_8D1(): pass

    label('loc_8D1')

    Return()

# id: 0x0004 offset: 0x8D2
@scena.Code('func_04_8D2')
def func_04_8D2():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_91F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8F5',
    )

    Call(0, 0x0006)
    ChrClearFlags(0x000B, 0x0010)
    ChrClearFlags(0x000C, 0x0010)

    Jump('loc_91C')

    def _loc_8F5(): pass

    label('loc_8F5')

    ChrTalk(
        0x00FE,
        (
            '哑、哑口无言\n',
            '大概就是像这样吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_91C(): pass

    label('loc_91C')

    Jump('loc_9F5')

    def _loc_91F(): pass

    label('loc_91F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_965',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_962',
    )

    ChrTalk(
        0x00FE,
        (
            '怎么会\n',
            '变成这样…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我、我们该\n',
            '怎么办才好…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_962(): pass

    label('loc_962')

    Jump('loc_9F5')

    def _loc_965(): pass

    label('loc_965')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_9C9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_9B8',
    )

    ChrTalk(
        0x00FE,
        (
            '米娜说的\n',
            '一定没错的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好！只要努力的话\n',
            '就绝对会成功的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9C6')

    def _loc_9B8(): pass

    label('loc_9B8')

    Call(0, 0x0006)
    ChrClearFlags(0x000B, 0x0010)
    ChrClearFlags(0x000C, 0x0010)

    def _loc_9C6(): pass

    label('loc_9C6')

    Jump('loc_9F5')

    def _loc_9C9(): pass

    label('loc_9C9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_9F5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_9EC',
    )

    ChrTalk(
        0x00FE,
        (
            '………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9F5')

    def _loc_9EC(): pass

    label('loc_9EC')

    Call(0, 0x0006)
    ChrClearFlags(0x000C, 0x0010)

    def _loc_9F5(): pass

    label('loc_9F5')

    TalkEnd(0x000B)

    Return()

# id: 0x0005 offset: 0x9F9
@scena.Code('func_05_9F9')
def func_05_9F9():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_A65',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A12',
    )

    Call(0, 0x0006)

    Jump('loc_A62')

    def _loc_A12(): pass

    label('loc_A12')

    ChrTalk(
        0x00FE,
        (
            '在谈论经济之前\n',
            '还是先想想清楚吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '否则不管说多少好话\n',
            '也都是没用的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A62(): pass

    label('loc_A62')

    Jump('loc_B80')

    def _loc_A65(): pass

    label('loc_A65')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_AC7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AC4',
    )

    ChrTalk(
        0x00FE,
        (
            '那种巨大的东西\n',
            '竟然会漂浮在天上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '龙的出现也许\n',
            '就是这次事件的预兆吧…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AC4(): pass

    label('loc_AC4')

    Jump('loc_B80')

    def _loc_AC7(): pass

    label('loc_AC7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_B24',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_B13',
    )

    ChrTalk(
        0x00FE,
        (
            '看来劝说别人\n',
            '有时也需要说说谎啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是好麻烦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B21')

    def _loc_B13(): pass

    label('loc_B13')

    Call(0, 0x0006)
    ChrClearFlags(0x000B, 0x0010)
    ChrClearFlags(0x000C, 0x0010)

    def _loc_B21(): pass

    label('loc_B21')

    Jump('loc_B80')

    def _loc_B24(): pass

    label('loc_B24')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_B80',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_B77',
    )

    ChrTalk(
        0x00FE,
        (
            '哈里的想法\n',
            '总是很有跳跃性，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是多想想\n',
            '身边的事就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B80')

    def _loc_B77(): pass

    label('loc_B77')

    Call(0, 0x0006)
    ChrClearFlags(0x000C, 0x0010)

    def _loc_B80(): pass

    label('loc_B80')

    TalkEnd(0x000C)

    Return()

# id: 0x0006 offset: 0xB84
@scena.Code('func_06_B84')
def func_06_B84():
    OP_4A(0x000B, 255)
    OP_4A(0x000C, 255)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_C7F',
    )

    ChrTalk(
        0x000B,
        (
            '因为导力器瘫痪，\n',
            '定期船也都停运了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '这样下去的话\n',
            '超市的商品就无法补充了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '是啊，经济方面的影响\n',
            '确实不容忽视…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '比起那个，\n',
            '照明问题也很让人担心吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '晚上都不敢去厕所，\n',
            '这也是大问题啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E11')

    def _loc_C7F(): pass

    label('loc_C7F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_C89',
    )

    Jump('loc_E11')

    def _loc_C89(): pass

    label('loc_C89')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_D94',
    )

    ChrTalk(
        0x000B,
        (
            '喂，米娜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '你觉得我有没有\n',
            '商业的才能？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '当然有啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '真、真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '嗯，不但充满热情，\n',
            '而且人缘也不差。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '虽然有点老实过头了，\n',
            '不过这也算是有信用呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '……所以，我相信你会成功的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '是、是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '好！我会努力的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E11')

    def _loc_D94(): pass

    label('loc_D94')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_E11',
    )

    ChrTalk(
        0x000B,
        (
            '嗯、不管怎么样，\n',
            '只要成为商人就算成功了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '这个嘛，\n',
            '等当上商人才烦恼这个吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E11(): pass

    label('loc_E11')

    OP_4B(0x000B, 255)
    OP_4B(0x000C, 255)
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Return()

# id: 0x0007 offset: 0xE20
@scena.Code('func_07_E20')
def func_07_E20():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_E2C',
    )

    Call(1, 0x0001)

    Return()

    def _loc_E2C(): pass

    label('loc_E2C')

    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_F1A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_EBF',
    )

    ChrTalk(
        0x00FE,
        (
            '城里的状况\n',
            '总算是平静了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难道大家都忘了天上\n',
            '还漂浮着那个东西了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯嗯、虽然习惯了，\n',
            '但还是觉得可怕啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_F17')

    def _loc_EBF(): pass

    label('loc_EBF')

    ChrTalk(
        0x00FE,
        (
            '难道大家都忘了天上\n',
            '还漂浮着一个岛了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯嗯、虽然习惯了，\n',
            '但还是觉得可怕啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F17(): pass

    label('loc_F17')

    Jump('loc_122E')

    def _loc_F1A(): pass

    label('loc_F1A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1041',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_FD9',
    )

    ChrTalk(
        0x00FE,
        (
            '在这里看那个岛\n',
            '看得很清楚哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '它在夜空中出现的同时\n',
            '城里的灯就全部熄灭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '龙的袭击事件才刚过去，\n',
            '本以为不会再有事情了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们的柏斯还\n',
            '真是多灾多难啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_103E')

    def _loc_FD9(): pass

    label('loc_FD9')

    ChrTalk(
        0x00FE,
        (
            '在这里看那个岛\n',
            '看得很清楚哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为什么会出现\n',
            '那种东西呢…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们的柏斯还\n',
            '真是多灾多难啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_103E(): pass

    label('loc_103E')

    Jump('loc_122E')

    def _loc_1041(): pass

    label('loc_1041')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_1117',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1098',
    )

    ChrTalk(
        0x00FE,
        (
            '超市也\n',
            '重新开始营业了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼呼呼～\n',
            '还真是多灾多难的城市啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1114')

    def _loc_1098(): pass

    label('loc_1098')

    ChrTalk(
        0x00FE,
        (
            '超市也\n',
            '重新开始营业了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '定期船的国际航行也恢复了，\n',
            '总算是恢复了原状。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼呼呼～\n',
            '还真是多灾多难的城市啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_1114(): pass

    label('loc_1114')

    Jump('loc_122E')

    def _loc_1117(): pass

    label('loc_1117')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_122E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1169',
    )

    ChrTalk(
        0x00FE,
        (
            '柏斯的未来就跟今早的阳光一样，\n',
            '十分的光明啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼呼呼～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_122E')

    def _loc_1169(): pass

    label('loc_1169')

    ChrTalk(
        0x00FE,
        (
            '柏斯的超市\n',
            '算得上是王国的经济中心之一。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像要和帝国\n',
            '进行交易呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '互不侵犯条约签署之后，\n',
            '国际性的交易也会更多吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '柏斯的未来就跟今早的阳光一样，\n',
            '十分的光明啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼呼呼～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_122E(): pass

    label('loc_122E')

    TalkEnd(0x000A)

    Return()

# id: 0x0008 offset: 0x1232
@scena.Code('func_08_1232')
def func_08_1232():
    TalkBegin(0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_1287',
    )

    ChrTalk(
        0x00FE,
        (
            '超市似乎\n',
            '要开始大甩卖活动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在这种时期进行活动\n',
            '还真是不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13B9')

    def _loc_1287(): pass

    label('loc_1287')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1310',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_12E2',
    )

    ChrTalk(
        0x00FE,
        (
            '本来想去看看\n',
            '有没有什么便宜货……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过现在还是\n',
            '没工夫去啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    Jump('loc_130D')

    def _loc_12E2(): pass

    label('loc_12E2')

    ChrTalk(
        0x00FE,
        (
            '在这种时候，\n',
            '很少有地方会征打工的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_130D(): pass

    label('loc_130D')

    Jump('loc_13B9')

    def _loc_1310(): pass

    label('loc_1310')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_13B9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1358',
    )

    ChrTalk(
        0x00FE,
        (
            '我正在找新的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，果然还是\n',
            '超市最好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13B9')

    def _loc_1358(): pass

    label('loc_1358')

    ChrTalk(
        0x00FE,
        (
            '我正在找新的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是有薪水高的地方\n',
            '就最好不过了…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，果然还是\n',
            '超市最好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_13B9(): pass

    label('loc_13B9')

    TalkEnd(0x000F)

    Return()

# id: 0x0009 offset: 0x13BD
@scena.Code('func_09_13BD')
def func_09_13BD():
    TalkBegin(0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_142E',
    )

    ChrTalk(
        0x00FE,
        (
            '昨天晚上真恐怖啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '城里的人们一直\n',
            '愤怒地叫到了半夜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这种时候\n',
            '需要更齐心协力才对啊…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1515')

    def _loc_142E(): pass

    label('loc_142E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_1515',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_149B',
    )

    ChrTalk(
        0x00FE,
        (
            '『安特洛丝餐厅』的料理\n',
            '果然和传闻中一样完美啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在想起那味道\n',
            '还忍不住流口水呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1515')

    def _loc_149B(): pass

    label('loc_149B')

    ChrTalk(
        0x00FE,
        (
            '不久前我们去过\n',
            '那家『安特洛丝餐厅』呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那里的每道料理\n',
            '都十分美味啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在想起那味道\n',
            '还忍不住流口水呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    def _loc_1515(): pass

    label('loc_1515')

    TalkEnd(0x0010)

    Return()

# id: 0x000A offset: 0x1519
@scena.Code('func_0A_1519')
def func_0A_1519():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_15D3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_158C',
    )

    ChrTalk(
        0x00FE,
        (
            '因为超市里总能\n',
            '听见吵闹的声音。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要不就去试试\n',
            '推销一下吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一会准备\n',
            '去看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    Jump('loc_15D0')

    def _loc_158C(): pass

    label('loc_158C')

    ChrTalk(
        0x00FE,
        (
            '在超市外面都能\n',
            '听见商人的声音。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要不就去试试\n',
            '推销一下吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15D0(): pass

    label('loc_15D0')

    Jump('loc_177A')

    def _loc_15D3(): pass

    label('loc_15D3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1688',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1646',
    )

    ChrTalk(
        0x00FE,
        (
            '那、那究竟是什么啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还有，为什么导力器\n',
            '会突然瘫痪？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '够了！\n',
            '我什么也不想知道！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    Jump('loc_1685')

    def _loc_1646(): pass

    label('loc_1646')

    ChrTalk(
        0x00FE,
        (
            '那、那究竟是什么啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还有，为什么导力器\n',
            '会突然瘫痪？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1685(): pass

    label('loc_1685')

    Jump('loc_177A')

    def _loc_1688(): pass

    label('loc_1688')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_1729',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_16DB',
    )

    ChrTalk(
        0x00FE,
        (
            '真高兴啊！\n',
            '超市又开张了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是值得庆贺，\n',
            '去买点东西吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1726')

    def _loc_16DB(): pass

    label('loc_16DB')

    ChrTalk(
        0x00FE,
        (
            '呵呵，真高兴啊。\n',
            '超市又开张了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天值得庆祝，\n',
            '去买点东西吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    def _loc_1726(): pass

    label('loc_1726')

    Jump('loc_177A')

    def _loc_1729(): pass

    label('loc_1729')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_177A',
    )

    ChrTalk(
        0x00FE,
        (
            '呵呵，今天\n',
            '去买点东西吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近实在无聊，\n',
            '唯一的乐趣就是购物了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_177A(): pass

    label('loc_177A')

    TalkEnd(0x000E)

    Return()

# id: 0x000B offset: 0x177E
@scena.Code('func_0B_177E')
def func_0B_177E():
    If(
        (
            (Expr.Eval, "OP_29(0x007B, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x007B, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x007B, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1890',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1873',
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
        100,
        0,
        (
            TXT(0x00, '【◇完成过后篇一章【食材收集】委托】\n'),
            TXT(0x01, '【◇完成过前篇【寻找荧光菇】、【探索护卫】委托】\n'),
            TXT(0x02, '【◇没有完成】\n'),
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
        (0x00000000, 'loc_183D'),
        (0x00000001, 'loc_184F'),
        (0x00000002, 'loc_1861'),
        (-1, 'loc_1873'),
    )

    def _loc_183D(): pass

    label('loc_183D')

    OP_28(0x0065, 0x04, 0x10)
    OP_28(0x0005, 0x03, 0x10)
    OP_28(0x001F, 0x03, 0x10)

    Jump('loc_1873')

    def _loc_184F(): pass

    label('loc_184F')

    OP_28(0x0065, 0x03, 0x10)
    OP_28(0x0005, 0x04, 0x10)
    OP_28(0x001F, 0x04, 0x10)

    Jump('loc_1873')

    def _loc_1861(): pass

    label('loc_1861')

    OP_28(0x0065, 0x03, 0x10)
    OP_28(0x0005, 0x03, 0x10)
    OP_28(0x001F, 0x03, 0x10)

    Jump('loc_1873')

    def _loc_1873(): pass

    label('loc_1873')

    If(
        (
            (Expr.Eval, "OP_29(0x0065, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0005, 0x00, 0x10)"),
            Expr.Or,
            (Expr.Eval, "OP_29(0x001F, 0x00, 0x10)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1890',
    )

    Call(1, 0x0004)

    Return()

    def _loc_1890(): pass

    label('loc_1890')

    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_1932',
    )

    ChrTalk(
        0x000D,
        (
            '哟！超市\n',
            '终于恢复营业了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '在本地商人的帮助下，总算\n',
            '和『安特洛丝餐厅』进行商谈了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '……就是这样，为了计划的实现\n',
            '好！马上开始营业吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A1F')

    def _loc_1932(): pass

    label('loc_1932')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_1A1F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_19A0',
    )

    ChrTalk(
        0x000D,
        (
            '果然还是要\n',
            '老老实实开始营业啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '要和『安特洛丝餐厅』\n',
            '商谈的话，\n',
            '需要本地人的协助。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A1F')

    def _loc_19A0(): pass

    label('loc_19A0')

    ChrTalk(
        0x000D,
        (
            '嗯，这就是\n',
            '柏斯超市吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '果然还是要\n',
            '老老实实开始营业啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '要和『安特洛丝餐厅』\n',
            '商谈的话，\n',
            '需要本地人的协助。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_1A1F(): pass

    label('loc_1A1F')

    TalkEnd(0x000D)

    Return()

# id: 0x000C offset: 0x1A23
@scena.Code('func_0C_1A23')
def func_0C_1A23():
    TalkBegin(0x0011)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 7, 0x35F)),
            Expr.Return,
        ),
        'loc_1A30',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    def _loc_1A30(): pass

    label('loc_1A30')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1AAC',
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
        100,
        0,
        (
            TXT(0x00, '【◇在前篇遇到过斯丁克】\n'),
            TXT(0x01, '【◇在前篇没遇到过斯丁克】\n'),
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
        (0x00000000, 'loc_1AA0'),
        (0x00000001, 'loc_1AA6'),
        (-1, 'loc_1AAC'),
    )

    def _loc_1AA0(): pass

    label('loc_1AA0')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    Jump('loc_1AAC')

    def _loc_1AA6(): pass

    label('loc_1AA6')

    ClearScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    Jump('loc_1AAC')

    def _loc_1AAC(): pass

    label('loc_1AAC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0341, 5, 0x1A0D)),
            Expr.Return,
        ),
        'loc_2253',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034A, 3, 0x1A53)),
            Expr.Return,
        ),
        'loc_1B9E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1B5E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_1B09',
    )

    ChrTalk(
        0x0011,
        (
            '柏斯这边\n',
            '有我一个人就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '……谢谢你们的帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B5B')

    def _loc_1B09(): pass

    label('loc_1B09')

    ChrTalk(
        0x0011,
        (
            '是你们吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '柏斯这边\n',
            '有我一个人就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '……谢谢你们的帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    def _loc_1B5B(): pass

    label('loc_1B5B')

    Jump('loc_1B9B')

    def _loc_1B5E(): pass

    label('loc_1B5E')

    ChrTalk(
        0x0011,
        (
            '柏斯这边\n',
            '有我一个人就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '……谢谢你们的帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1B9B(): pass

    label('loc_1B9B')

    Jump('loc_2253')

    def _loc_1B9E(): pass

    label('loc_1B9E')

    ChrTalk(
        0x0011,
        (
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0011, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_1E75',
    )

    ChrTalk(
        0x0101,
        (
            '#1011F啊、你是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '斯丁克……对吧？\n',
            '柏斯支部的游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0011, 0x0101, 400)

    ChrTalk(
        0x0011,
        (
            '你是……\n',
            '那时的准游击士吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '呀，看样子已经晋升正游击士了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F嗯，是啊。',
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
        'loc_1D39',
    )

    ChrTalk(
        0x0103,
        (
            '#027F好久不见了，斯丁克。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0011, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_63(0x0011)
    ChrTurnDirection(0x0011, 0x0103, 400)

    ChrTalk(
        0x0011,
        (
            '雪拉扎德吗…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '这次的巨龙骚乱事件，\n',
            '全靠你们全力帮助才解决的，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '……非常感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#026F哪里，这是应该做的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E72')

    def _loc_1D39(): pass

    label('loc_1D39')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1E0B',
    )

    ChrTalk(
        0x0106,
        (
            '#051F好久不见，斯丁克。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0011, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_63(0x0011)
    ChrTurnDirection(0x0011, 0x0106, 400)

    ChrTalk(
        0x0011,
        (
            '阿加特吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '这次的巨龙骚乱事件，\n',
            '全靠你们全力帮助才解决的，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '……非常感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#051F哪里，这是我们的义务啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E72')

    def _loc_1E0B(): pass

    label('loc_1E0B')

    ChrTalk(
        0x0011,
        (
            '这次的巨龙骚乱事件，\n',
            '全靠你们全力帮助才解决的，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '……非常感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1002F嗯，这是应该的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E72(): pass

    label('loc_1E72')

    Jump('loc_21E9')

    def _loc_1E75(): pass

    label('loc_1E75')

    ChrTalk(
        0x0101,
        (
            '#1015F（啊？这个人……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '（仔细看看的话，\n',
            '　竟然也戴着游击士的徽章啊？）',
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
        'loc_1F82',
    )

    ChrTalk(
        0x0103,
        (
            '#027F好久不见了，斯丁克。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0011, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_63(0x0011)
    ChrTurnDirection(0x0011, 0x0103, 400)

    ChrTalk(
        0x0011,
        (
            '这次的巨龙骚乱事件，\n',
            '全靠你们全力帮助才解决的，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '……非常感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#026F哪里，这是应该做的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21E9')

    def _loc_1F82(): pass

    label('loc_1F82')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2054',
    )

    ChrTalk(
        0x0106,
        (
            '#051F好久不见，斯丁克。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0011, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_63(0x0011)
    ChrTurnDirection(0x0011, 0x0106, 400)

    ChrTalk(
        0x0011,
        (
            '阿加特吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '这次的巨龙骚乱事件，\n',
            '全靠你们全力帮助才解决的，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '……非常感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#051F哪里，这是我们的义务啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21E9')

    def _loc_2054(): pass

    label('loc_2054')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_208A',
    )

    ChrTalk(
        0x0108,
        (
            '#070F（嗯，看来他也是游击士。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_20BF')

    def _loc_208A(): pass

    label('loc_208A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_20BF',
    )

    ChrTalk(
        0x0104,
        (
            '#030F（嗯，看来也是个游击士啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_20BF(): pass

    label('loc_20BF')

    ChrTurnDirection(0x0011, 0x0101, 400)

    ChrTalk(
        0x0011,
        (
            '你是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '卢格兰老爷子提到的那个\n',
            '新人正游击士吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011F卢格兰爷爷说的？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1015F那应该就是我了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '这次的巨龙骚乱事件，\n',
            '全靠你们全力帮助才解决的，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '……非常感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1002F哪里，身为游击士，\n',
            '这是应该做的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '……真是让人信赖的回答啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_21E9(): pass

    label('loc_21E9')

    ChrTalk(
        0x0011,
        (
            '柏斯这边\n',
            '有我一个人就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '……你们也继续自己\n',
            '本来的任务吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '……谢谢你们的帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x034A, 3, 0x1A53))
    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    def _loc_2253(): pass

    label('loc_2253')

    TalkEnd(0x0011)

    Return()

# id: 0x000D offset: 0x2257
@scena.Code('func_0D_2257')
def func_0D_2257():
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
        'loc_226E',
    )

    Call(0, 0x0024)
    Call(0, 0x0026)

    def _loc_226E(): pass

    label('loc_226E')

    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x00F8, 0x0080)
    ChrSetFlags(0x00F9, 0x0080)
    OP_4A(0x000E, 255)
    OP_4A(0x000A, 255)
    CameraMove(59660, 480, 80570, 0)
    OP_67(0, 9550, -10000, 0)
    CameraSetDistance(2540, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    OP_0D()
    OP_6F(0x0003, 0)
    OP_70(0x0003, 59)
    OP_73(0x0003)
    Sleep(500)

    @scena.Lambda('lambda_22ED')
    def lambda_22ED():
        CameraMove(59380, 0, 76340, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_22ED)

    CreateThread(0x0101, 0x01, 0x00, func_0E_287E)
    Sleep(800)

    CreateThread(0x0102, 0x01, 0x00, func_0F_28C4)
    Sleep(800)

    CreateThread(0x00F8, 0x01, 0x00, func_10_290A)
    Sleep(800)

    CreateThread(0x00F9, 0x01, 0x00, func_11_2950)
    WaitForThreadExit(0x00F9, 0x0001)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010350183V#1015F那么……\n',
            '因为飞船无法使用，\n',
            '所以现在只能徒步旅行了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010350184V洛连特支部和卢安支部，\n',
            '要去哪边好呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350185V#1035F#6P恩……\n',
            '我觉得走哪边都无所谓。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020350186V#1043F因为每个地方的\n',
            '状况都一样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010310217V#1007F这样啊……的确。',
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
        'loc_24BD',
    )

    ChrTalk(
        0x0106,
        (
            '#0050350188V#053F嗯，在这种状况下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050350189V#050F走哪边都一样。\n',
            '反正也要确认一下\n',
            '各地的情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25A8')

    def _loc_24BD(): pass

    label('loc_24BD')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2538',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350190V#026F是啊、在这种状况下……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030350191V#524F不管走哪边\n',
            '反正也要确认一下\n',
            '各地的情况呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25A8')

    def _loc_2538(): pass

    label('loc_2538')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_25A8',
    )

    ChrTalk(
        0x0108,
        (
            '#0080350192V#074F在这种状况下，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080350193V#070F不管走哪边\n',
            '反正也要确认一下\n',
            '各地的情况呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_25A8(): pass

    label('loc_25A8')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_25FB',
    )

    ChrTalk(
        0x0107,
        (
            '#0070350194V#560F要是遇到有困难的人\n',
            '我们就顺便帮帮他们好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26A0')

    def _loc_25FB(): pass

    label('loc_25FB')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_264E',
    )

    ChrTalk(
        0x0108,
        (
            '#0080350195V#070F要是遇到有困难的人\n',
            '我们也可以顺便帮助他们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26A0')

    def _loc_264E(): pass

    label('loc_264E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_26A0',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350196V#524F要是遇到有困难的人\n',
            '我们也可以顺便帮助他们哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_26A0(): pass

    label('loc_26A0')

    ChrTalk(
        0x0101,
        (
            '#0010350197V#1006F嗯……说的对！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※在导力停止现象中，只有装备『零力场发生器』\n',
            '　的角色才可以使用魔法。\n',
            '　请在主选单的[Equip]选项内\n',
            '　将『零力场发生器』装备上吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '※另外，由于提妲的武器是导力炮，如\n',
            '　果不装备『零力场发生器』的话就连\n',
            '　普通攻击和战技也都无法使用。不过\n',
            '　由于S超杀技『炮射冲击II』是使用\n',
            '　火药式的枪械，所以可以正常使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_59()
    OP_C4(0x00, 0x00000008)
    OP_28(0x009A, 0x01, 0x1000)
    OP_28(0x009A, 0x01, 0x2000)
    OP_28(0x009B, 0x04, 0x02)
    OP_28(0x009B, 0x04, 0x08)
    OP_28(0x009B, 0x01, 0x0001)
    OP_28(0x009B, 0x01, 0x0002)
    OP_28(0x009B, 0x01, 0x0004)
    OP_28(0x009B, 0x01, 0x0010)
    OP_28(0x009B, 0x01, 0x0040)

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    AddItem(ItemTable['零力场发生器'], 4)
    OP_4B(0x000E, 255)
    OP_4B(0x000A, 255)
    OP_20(0x000003E8)
    OP_21()
    EventEnd(0x00)
    PlayBGM(26)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x1A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x000E offset: 0x287E
@scena.Code('func_0E_287E')
def func_0E_287E():
    ChrSetPos(0x00FE, 59000, 500, 81490, 180)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 59080, 0, 78450, 2000, 0x00)
    ChrWalkTo(0x00FE, 58970, 0, 75000, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x000F offset: 0x28C4
@scena.Code('func_0F_28C4')
def func_0F_28C4():
    ChrSetPos(0x00FE, 59000, 500, 81490, 180)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 59080, 0, 78450, 2000, 0x00)
    ChrWalkTo(0x00FE, 58000, 0, 76000, 2000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x0010 offset: 0x290A
@scena.Code('func_10_290A')
def func_10_290A():
    ChrSetPos(0x00FE, 59000, 500, 81490, 180)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 59080, 0, 78450, 2000, 0x00)
    ChrWalkTo(0x00FE, 60100, 0, 76000, 2000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)

    Return()

# id: 0x0011 offset: 0x2950
@scena.Code('func_11_2950')
def func_11_2950():
    ChrSetPos(0x00FE, 59000, 500, 81490, 180)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 59030, 480, 79580, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)
    Sleep(200)

    OP_72(0x0003, 0x0800)
    OP_6F(0x0003, 59)
    OP_70(0x0003, 0)
    OP_23(0x0006)
    PlaySE(7, 0x00, 0x64)
    OP_73(0x0003)
    OP_71(0x0003, 0x0800)
    ChrSetDirection(0x00FE, 180, 400)
    ChrWalkTo(0x00FE, 59040, 0, 76780, 2000, 0x00)

    Return()

# id: 0x0012 offset: 0x29C5
@scena.Code('func_12_29C5')
def func_12_29C5():
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
        'loc_29DC',
    )

    Call(0, 0x0024)
    Call(0, 0x0025)

    def _loc_29DC(): pass

    label('loc_29DC')

    Call(0, 0x0013)
    ChrSetPos(0x00F8, 60660, 0, 76570, 135)
    ChrSetPos(0x0101, 61720, 0, 76670, 135)
    ChrSetPos(0x00F7, 61830, 0, 77710, 135)
    ChrSetPos(0x00F9, 60400, 0, 77960, 135)
    ChrSetPos(0x00FA, 62880, 0, 75050, 315)
    ChrSetPos(0x00FB, 63770, 0, 75420, 315)
    ChrSetPos(0x00FC, 62310, 0, 74280, 315)
    CameraMove(61500, 0, 77120, 0)
    OP_67(0, 8670, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(324000, 0)
    OP_6E(262, 0)
    OP_4A(0x000E, 255)
    OP_4A(0x000A, 255)
    FadeIn(1000, 0)
    OP_0D()

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_2AFD',
    )

    ChrTalk(
        0x0106,
        (
            '#0050320249V#051F#6P那么，我们就先走一步，\n',
            '到『川蝉亭』等你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2BFD')

    def _loc_2AFD(): pass

    label('loc_2AFD')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Return,
        ),
        'loc_2B54',
    )

    ChrTalk(
        0x0103,
        (
            '#0030320250V#021F#6P那么，我们就先走一步，\n',
            '到『川蝉亭』等你们哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2BFD')

    def _loc_2B54(): pass

    label('loc_2B54')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_2BA9',
    )

    ChrTalk(
        0x0108,
        (
            '#0080320251V#071F#6P那么，我们就先走一步，\n',
            '到『川蝉亭』等你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2BFD')

    def _loc_2BA9(): pass

    label('loc_2BA9')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x8),
            Expr.And,
            Expr.Return,
        ),
        'loc_2BFD',
    )

    ChrTalk(
        0x0104,
        (
            '#0040320252V#031F#6P那么，我们就先走一步，\n',
            '到『川蝉亭』等你们啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2BFD(): pass

    label('loc_2BFD')

    ChrTalk(
        0x0101,
        (
            '#0010320253V#1006F#5P嗯，好的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320254V登记的事情就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2CA4',
    )

    ChrTalk(
        0x0103,
        (
            '#0030320255V#027F#5P卢格兰爷爷已经和他们联系过了，\n',
            '应该不会定不到房间的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2DC1')

    def _loc_2CA4(): pass

    label('loc_2CA4')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2D04',
    )

    ChrTalk(
        0x0106,
        (
            '#0050320256V#051F#5P卢格兰爷爷已经和他们联系过了，\n',
            '应该不会定不到房间的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2DC1')

    def _loc_2D04(): pass

    label('loc_2D04')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2D64',
    )

    ChrTalk(
        0x0108,
        (
            '#0080320257V#070F#5P卢格兰爷爷已经和他们联系过了，\n',
            '应该不会定不到房间的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2DC1')

    def _loc_2D64(): pass

    label('loc_2D64')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x8),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2DC1',
    )

    ChrTalk(
        0x0104,
        (
            '#0040320258V#030F#5P卢格兰爷爷已经和他们联系过了，\n',
            '应该不会定不到房间的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2DC1(): pass

    label('loc_2DC1')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x4),
            Expr.And,
            Expr.Return,
        ),
        'loc_2DFD',
    )

    ChrTalk(
        0x0107,
        (
            '#0070320259V#061F#6P好啦，交给我们吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2EAA')

    def _loc_2DFD(): pass

    label('loc_2DFD')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_2E37',
    )

    ChrTalk(
        0x0105,
        (
            '#0060320260V#048F#6P是，交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2EAA')

    def _loc_2E37(): pass

    label('loc_2E37')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x8),
            Expr.And,
            Expr.Return,
        ),
        'loc_2E71',
    )

    ChrTalk(
        0x0104,
        (
            '#0040320261V#031F#6P呼，包在我身上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2EAA')

    def _loc_2E71(): pass

    label('loc_2E71')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_2EAA',
    )

    ChrTalk(
        0x0108,
        (
            '#0080320262V#071F#6P啊啊～交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2EAA(): pass

    label('loc_2EAA')

    ChrSetDirection(0x00FA, 180, 400)

    @scena.Lambda('lambda_2EB7')
    def lambda_2EB7():
        ChrWalkTo(0x00FE, 63700, 0, 63000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FA, 0x0001, lambda_2EB7)

    Sleep(500)

    ChrSetDirection(0x00FB, 180, 400)

    @scena.Lambda('lambda_2EDE')
    def lambda_2EDE():
        ChrWalkTo(0x00FE, 64750, 0, 63000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FB, 0x0001, lambda_2EDE)

    Sleep(500)

    ChrSetDirection(0x00FC, 180, 400)

    @scena.Lambda('lambda_2F05')
    def lambda_2F05():
        ChrWalkTo(0x00FE, 62570, 0, 63000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FC, 0x0001, lambda_2F05)

    @scena.Lambda('lambda_2F20')
    def lambda_2F20():
        CameraMove(62540, 0, 74000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2F20)

    @scena.Lambda('lambda_2F38')
    def lambda_2F38():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_2F38)

    Sleep(100)

    @scena.Lambda('lambda_2F4B')
    def lambda_2F4B():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2F4B)

    Sleep(100)

    @scena.Lambda('lambda_2F5E')
    def lambda_2F5E():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_2F5E)

    Sleep(100)

    @scena.Lambda('lambda_2F71')
    def lambda_2F71():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_2F71)

    WaitForThreadExit(0x00FC, 0x0001)
    ChrSetFlags(0x00FA, 0x0080)
    ChrSetFlags(0x00FB, 0x0080)
    ChrSetFlags(0x00FC, 0x0080)
    WaitForThreadExit(0x0101, 0x0000)

    @scena.Lambda('lambda_2F98')
    def lambda_2F98():
        CameraMove(60780, 0, 77800, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2F98)

    WaitForThreadExit(0x0101, 0x0000)

    @scena.Lambda('lambda_2FB5')
    def lambda_2FB5():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_2FB5)

    Sleep(50)

    @scena.Lambda('lambda_2FC8')
    def lambda_2FC8():
        ChrSetDirection(0x00FE, 315, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2FC8)

    Sleep(50)

    @scena.Lambda('lambda_2FDB')
    def lambda_2FDB():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_2FDB)

    Sleep(50)

    @scena.Lambda('lambda_2FEE')
    def lambda_2FEE():
        ChrSetDirection(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_2FEE)

    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010320263V#1006F#6P那么，我们就再去\n',
            '确认一下留言板吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320264V不知道柏斯各地在龙的骚乱之后\n',
            '有没有顺利恢复正常…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_30E0',
    )

    ChrTalk(
        0x0106,
        (
            '#0050320265V#051F#5P嗯～老爷子难得\n',
            '这么大方一次。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050320266V尽快去湖边会合吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_322B')

    def _loc_30E0(): pass

    label('loc_30E0')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_314F',
    )

    ChrTalk(
        0x0103,
        (
            '#0030320267V#020F#5P好啦，卢格兰爷爷\n',
            '难得邀请咱们一次，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030320268V还是尽快\n',
            '去湖边吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_322B')

    def _loc_314F(): pass

    label('loc_314F')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_31BC',
    )

    ChrTalk(
        0x0108,
        (
            '#0080320269V#070F#5P哈哈，老爷爷\n',
            '特地邀请我们一次。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080320270V还是尽快\n',
            '到湖边去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_322B')

    def _loc_31BC(): pass

    label('loc_31BC')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x8),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_322B',
    )

    ChrTalk(
        0x0104,
        (
            '#0040320271V#035F#5P呼～那位老人\n',
            '特地邀请我们一次。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040320272V#030F还是尽早\n',
            '到湖畔去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_322B(): pass

    label('loc_322B')

    ChrTalk(
        0x0101,
        (
            '#0010320273V#1015F#6P说的也对啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010320274V#1001F嗯！那我们就尽快完成工作，\n',
            '然后就去瓦雷利亚湖吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x4),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_32C8',
    )

    ChrTalk(
        0x0107,
        (
            '#0070320275V#061F#5P嗯⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_335A')

    def _loc_32C8(): pass

    label('loc_32C8')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_32F7',
    )

    ChrTalk(
        0x0105,
        (
            '#0060320276V#041F#5P是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_335A')

    def _loc_32F7(): pass

    label('loc_32F7')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x8),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_332C',
    )

    ChrTalk(
        0x0104,
        (
            '#0040320277V#031F#5P呼，明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_335A')

    def _loc_332C(): pass

    label('loc_332C')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_335A',
    )

    ChrTalk(
        0x0108,
        (
            '#0080320278V#071F#5P噢噢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_335A(): pass

    label('loc_335A')

    Sleep(100)

    Call(0, 0x0014)
    Sleep(100)

    OP_4B(0x000A, 255)
    OP_4B(0x000E, 255)
    OP_28(0x0078, 0x04, 0x40)
    OP_28(0x0096, 0x01, 0x0800)
    OP_28(0x0096, 0x01, 0x1000)
    OP_28(0x0097, 0x04, 0x02)
    OP_28(0x0097, 0x04, 0x08)
    OP_28(0x0097, 0x01, 0x0001)
    OP_28(0x0097, 0x01, 0x0002)
    EventEnd(0x00)

    Return()

# id: 0x0013 offset: 0x339A
@scena.Code('func_13_339A')
def func_13_339A():
    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_33D3',
    )

    FormationAddMember(ChrTable['金'], 0xFA, 0xFF)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_33D3(): pass

    label('loc_33D3')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_340C',
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_33F4',
    )

    FormationAddMember(ChrTable['科洛丝'], 0xFA, 0xFF)

    Jump('loc_33F8')

    def _loc_33F4(): pass

    label('loc_33F4')

    FormationAddMember(ChrTable['科洛丝'], 0xFB, 0xFF)

    def _loc_33F8(): pass

    label('loc_33F8')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x2),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_340C(): pass

    label('loc_340C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_3459',
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_342D',
    )

    FormationAddMember(ChrTable['奥利维尔'], 0xFA, 0xFF)

    Jump('loc_3445')

    def _loc_342D(): pass

    label('loc_342D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3441',
    )

    FormationAddMember(ChrTable['奥利维尔'], 0xFB, 0xFF)

    Jump('loc_3445')

    def _loc_3441(): pass

    label('loc_3441')

    FormationAddMember(ChrTable['奥利维尔'], 0xFC, 0xFF)

    def _loc_3445(): pass

    label('loc_3445')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x8),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_3459(): pass

    label('loc_3459')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_34A6',
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_347A',
    )

    FormationAddMember(ChrTable['阿加特'], 0xFA, 0xFF)

    Jump('loc_3492')

    def _loc_347A(): pass

    label('loc_347A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_348E',
    )

    FormationAddMember(ChrTable['阿加特'], 0xFB, 0xFF)

    Jump('loc_3492')

    def _loc_348E(): pass

    label('loc_348E')

    FormationAddMember(ChrTable['阿加特'], 0xFC, 0xFF)

    def _loc_3492(): pass

    label('loc_3492')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x10),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_34A6(): pass

    label('loc_34A6')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_34F3',
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_34C7',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xFA, 0xFF)

    Jump('loc_34DF')

    def _loc_34C7(): pass

    label('loc_34C7')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_34DB',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xFB, 0xFF)

    Jump('loc_34DF')

    def _loc_34DB(): pass

    label('loc_34DB')

    FormationAddMember(ChrTable['雪拉扎德'], 0xFC, 0xFF)

    def _loc_34DF(): pass

    label('loc_34DF')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x20),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_34F3(): pass

    label('loc_34F3')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_3518',
    )

    FormationAddMember(ChrTable['提妲'], 0xFC, 0xFF)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x4),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_3518(): pass

    label('loc_3518')

    Return()

# id: 0x0014 offset: 0x3519
@scena.Code('func_14_3519')
def func_14_3519():
    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_3529',
    )

    FormationDelMember(0x07, 0xFF)

    def _loc_3529(): pass

    label('loc_3529')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_3539',
    )

    FormationDelMember(0x04, 0xFF)

    def _loc_3539(): pass

    label('loc_3539')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x4),
            Expr.And,
            Expr.Return,
        ),
        'loc_3549',
    )

    FormationDelMember(0x06, 0xFF)

    def _loc_3549(): pass

    label('loc_3549')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x8),
            Expr.And,
            Expr.Return,
        ),
        'loc_3559',
    )

    FormationDelMember(0x03, 0xFF)

    def _loc_3559(): pass

    label('loc_3559')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_3569',
    )

    FormationDelMember(0x05, 0xFF)

    def _loc_3569(): pass

    label('loc_3569')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x20),
            Expr.And,
            Expr.Return,
        ),
        'loc_3579',
    )

    FormationDelMember(0x02, 0xFF)

    def _loc_3579(): pass

    label('loc_3579')

    Return()

# id: 0x0015 offset: 0x357A
@scena.Code('func_15_357A')
def func_15_357A():
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
        'loc_358D',
    )

    Call(0, 0x0023)

    def _loc_358D(): pass

    label('loc_358D')

    OP_4A(0x000E, 255)
    OP_4A(0x000A, 255)
    CameraMove(59000, 400, 79200, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 59000, 500, 81490, 180)
    ChrSetPos(0x0106, 59000, 500, 81490, 180)
    ChrSetPos(0x00F8, 59000, 500, 81490, 180)
    ChrSetPos(0x00F9, 59000, 500, 81490, 180)
    FadeIn(2000, 0)
    OP_0D()
    OP_6F(0x0003, 0)
    OP_70(0x0003, 59)
    OP_73(0x0001)
    Sleep(500)

    CreateThread(0x0101, 0x01, 0x00, func_16_3CDA)
    Sleep(800)

    CreateThread(0x0106, 0x01, 0x00, func_17_3CF6)
    Sleep(800)

    CreateThread(0x00F8, 0x01, 0x00, func_18_3D26)
    Sleep(800)

    CreateThread(0x00F9, 0x01, 0x00, func_19_3D56)
    Sleep(1000)

    @scena.Lambda('lambda_366C')
    def lambda_366C():
        CameraMove(59010, 0, 74980, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_366C)

    @scena.Lambda('lambda_3684')
    def lambda_3684():
        OP_6C(65000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3684)

    WaitForThreadExit(0x00F9, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010300672V#1006F啊，这次被通缉的魔兽\n',
            '真是遍布各地啊…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300673V反正机会难得，\n',
            '不如顺便去一趟拉文努村怎么样？',
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
        'loc_3A35',
    )

    ChrTalk(
        0x0107,
        (
            '#0070300674V#560F啊……⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050300675V#555F我说你啊……\n',
            '为什么要用那么期待的眼神看我？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070300676V#067F嘿嘿嘿……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070300677V阿加特哥哥的故乡，\n',
            '我一直都很想去看一次的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070240379V#063F那个，不行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050300679V#053F……现在不行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050300680V#050F等我们将通缉魔兽\n',
            '全部解决之后再说吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070300681V#561F呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300682V#1019F真是的，小气鬼～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300683V难得提妲也在一起，\n',
            '你就不能破一次例吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050300684V#551F什、什么叫破例……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070300685V#065F姐、姐姐、没关系啦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070300686V把工作放在第一位\n',
            '是理所当然的事情…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070300687V#562F对不起，阿加特哥哥，\n',
            '我又任性了…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050300688V#552F不、不是的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050300689V#556F那个……总之。\n',
            '等工作完成之后我一定会带你去的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050300690V所以暂时先忍耐一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070300691V#061F是的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3CAA')

    def _loc_3A35(): pass

    label('loc_3A35')

    ChrTalk(
        0x0106,
        (
            '#0050300692V#555F我说你啊……\n',
            '在定期船上已经说过了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050300693V要去拉文努村的话，\n',
            '还是等柏斯的事件告一段落之后再说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300694V#1019F真是的，小气鬼～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3B5E',
    )

    ChrTalk(
        0x0104,
        (
            '#0040300695V#035F呼，阿加特兄\n',
            '说得没错啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040300696V#037F丢下提妲妹妹不管的话，\n',
            '我们去了\n',
            '也没意义呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3C5D')

    def _loc_3B5E(): pass

    label('loc_3B5E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3BE0',
    )

    ChrTalk(
        0x0105,
        (
            '#0060300697V#045F呵呵，也许正如阿加特\n',
            '说的那样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060300698V#542F丢下提妲不管的话，\n',
            '我们去了\n',
            '也没意义啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3C5D')

    def _loc_3BE0(): pass

    label('loc_3BE0')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3C5D',
    )

    ChrTalk(
        0x0103,
        (
            '#0030300699V#021F呵呵，也许正如\n',
            '阿加特所说啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030300700V#027F扔下提妲不管的话，\n',
            '我们去了\n',
            '也没意思嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3C5D(): pass

    label('loc_3C5D')

    ChrTalk(
        0x0101,
        (
            '#0010300701V#1001F哈，是这样的吗⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050300702V#055F真是无法理解！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3CAA(): pass

    label('loc_3CAA')

    SetScenaFlags(ScenaFlag(0x0341, 5, 0x1A0D))
    OP_28(0x0093, 0x04, 0x02)
    OP_28(0x0093, 0x04, 0x08)
    OP_28(0x0093, 0x01, 0x0001)
    OP_28(0x0093, 0x01, 0x0002)
    OP_28(0x0093, 0x01, 0x0010)
    OP_28(0x0093, 0x01, 0x0080)
    OP_4B(0x000E, 255)
    OP_4B(0x000A, 255)
    EventEnd(0x00)

    Return()

# id: 0x0016 offset: 0x3CDA
@scena.Code('func_16_3CDA')
def func_16_3CDA():
    ChrWalkTo(0x00FE, 59000, 0, 74190, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0017 offset: 0x3CF6
@scena.Code('func_17_3CF6')
def func_17_3CF6():
    ChrWalkTo(0x00FE, 59000, 0, 77890, 2000, 0x00)
    ChrWalkTo(0x00FE, 59750, 0, 74790, 2000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)

    Return()

# id: 0x0018 offset: 0x3D26
@scena.Code('func_18_3D26')
def func_18_3D26():
    ChrWalkTo(0x00FE, 59000, 0, 77890, 2000, 0x00)
    ChrWalkTo(0x00FE, 58160, 0, 75080, 2000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x0019 offset: 0x3D56
@scena.Code('func_19_3D56')
def func_19_3D56():
    ChrWalkTo(0x00FE, 59000, 400, 79200, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)
    OP_72(0x0003, 0x0800)
    OP_6F(0x0003, 59)
    OP_70(0x0003, 0)
    OP_23(0x0006)
    PlaySE(7, 0x00, 0x64)
    OP_73(0x0001)
    OP_71(0x0003, 0x0800)
    Sleep(500)

    ChrSetDirection(0x00FE, 180, 400)
    ChrWalkTo(0x00FE, 59000, 0, 75890, 2000, 0x00)

    Return()

# id: 0x001A offset: 0x3DB5
@scena.Code('func_1A_3DB5')
def func_1A_3DB5():
    EventBegin(0x00)
    CameraMove(63080, 0, 53130, 0)
    OP_67(0, 9460, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(0, 0)
    OP_6E(265, 0)
    ChrSetPos(0x000A, 62320, 0, 51020, 360)
    ChrClearFlags(0x000A, 0x0080)
    CreateThread(0x000A, 0x00, 0x06, func_02_6D8)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x0010, 0x0080)

    @scena.Lambda('lambda_3E35')
    def lambda_3E35():
        CameraMove(62390, 0, 58620, 3500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3E35)

    FadeIn(2000, 0)
    ChrWalkTo(0x000A, 62320, 0, 59140, 2000, 0x00)
    OP_4A(0x000A, 255)
    ChrSetPos(0x0008, 61930, 0, 68420, 180)
    ChrSetPos(0x0009, 62610, 0, 68980, 180)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)

    NpcTalk(
        0x0008,
        '女性的声音',
        (
            '#0360300805V#6P您好啊，雅哈多爷爷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_3EEA')
    def lambda_3EEA():
        CameraMove(62420, 0, 60760, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3EEA)

    @scena.Lambda('lambda_3F02')
    def lambda_3F02():
        OP_67(0, 9360, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3F02)

    @scena.Lambda('lambda_3F1A')
    def lambda_3F1A():
        OP_6E(272, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3F1A)

    @scena.Lambda('lambda_3F2A')
    def lambda_3F2A():
        ChrWalkTo(0x00FE, 61930, 0, 61310, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_3F2A)

    Sleep(100)

    @scena.Lambda('lambda_3F4A')
    def lambda_3F4A():
        ChrWalkTo(0x00FE, 62610, 0, 61700, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3F4A)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0008, 0x0001)

    ChrTalk(
        0x000A,
        (
            '#3510300806V啊，这不是市长吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3510300807V是要去教会做礼拜吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0360300808V#611F#5P不，准备去\n',
            '视察一下超市。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360300809V礼拜的话，准备之后再去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0009, 225, 400)

    ChrTalk(
        0x0009,
        (
            '#0370300810V#623F#2P小姐……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370300811V前几天您也是这么说的，\n',
            '但最后也是没去啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0009, 400)

    ChrTalk(
        0x0008,
        (
            '#0360300812V#615F#6P好啦，莉拉～\n',
            '那种事情何必记这么清楚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360300813V#612F今天我一定会去的啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3510300814V呵呵，工作虽然不能丢下，\n',
            '不过日常生活也是很重要的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3510300815V像你这种责任重大\n',
            '的人就更是如此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_415B')
    def lambda_415B():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_415B)

    Sleep(150)

    ChrSetDirection(0x0009, 180, 400)

    ChrTalk(
        0x0008,
        (
            '#0360300816V#617F#5P嗯，我会记住的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360300817V#611F那么我们就先\n',
            '失陪了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0370300818V#621F#5P失陪了。（点头致意）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    @scena.Lambda('lambda_41FC')
    def lambda_41FC():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_41FC')

    DispatchAsync2(0x000A, 0x0001, lambda_41FC)

    CreateThread(0x0008, 0x01, 0x00, func_1B_4514)
    Fade(1000)
    CameraMove(59360, 0, 60210, 0)
    OP_67(0, 10720, -10000, 0)
    CameraSetDistance(2710, 0)
    OP_6C(270000, 0)
    OP_6E(262, 0)
    Sleep(800)

    CreateThread(0x0009, 0x01, 0x00, func_1C_4537)
    WaitForThreadExit(0x0008, 0x0001)
    Sleep(300)

    OP_72(0x000B, 0x0010)
    OP_6F(0x000B, 0)
    OP_70(0x000B, 59)
    OP_73(0x000B)

    @scena.Lambda('lambda_4282')
    def lambda_4282():
        ChrWalkTo(0x00FE, 54550, 500, 60010, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_4282)

    Sleep(500)

    @scena.Lambda('lambda_42A2')
    def lambda_42A2():
        ChrWalkTo(0x00FE, 54550, 500, 60010, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_42A2)

    @scena.Lambda('lambda_42BD')
    def lambda_42BD():
        CameraMove(62320, 0, 59140, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_42BD)

    @scena.Lambda('lambda_42D5')
    def lambda_42D5():
        OP_67(0, 9500, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_42D5)

    @scena.Lambda('lambda_42ED')
    def lambda_42ED():
        OP_6C(242000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_42ED)

    @scena.Lambda('lambda_42FD')
    def lambda_42FD():
        OP_6E(262, 4000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_42FD)

    WaitForThreadExit(0x0008, 0x0001)
    ChrSetFlags(0x0008, 0x0080)
    OP_6F(0x000B, 59)
    OP_70(0x000B, 0)
    OP_71(0x000B, 0x0010)
    WaitForThreadExit(0x0009, 0x0001)
    ChrSetFlags(0x0009, 0x0080)
    TerminateThread(0x000A, 0x01)
    WaitForThreadExit(0x000A, 0x0002)

    ChrTalk(
        0x000A,
        (
            '#3510300819V#6P呼～自从她父亲去世之后，\n',
            '这孩子就马上被选为市长候补。\n',
            '当时我还在担心她承担不了…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3510300820V#6P但现在看来，\n',
            '她已经完全是个称职的市长了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#3510300821V#6P嗯，其实我也觉得\n',
            '她可以不用这么卖力的…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000A, 0, 400)
    ChrWalkTo(0x000A, 62320, 0, 59640, 2000, 0x01)
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetDirection(0x000A, 90, 400)
    OP_62(0x000A, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1500)

    OP_63(0x000A)

    ChrTalk(
        0x000A,
        (
            '#3510300822V#5P……那、那是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_449D')
    def lambda_449D():
        CameraMove(64379, 0, 59730, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_449D)

    @scena.Lambda('lambda_44B5')
    def lambda_44B5():
        OP_67(0, 7140, -10000, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_44B5)

    @scena.Lambda('lambda_44CD')
    def lambda_44CD():
        CameraSetDistance(3110, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_44CD)

    @scena.Lambda('lambda_44DD')
    def lambda_44DD():
        OP_6C(270000, 7000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_44DD)

    @scena.Lambda('lambda_44ED')
    def lambda_44ED():
        OP_6E(632, 7000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_44ED)

    Sleep(4000)

    FadeOut(2000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/T1121._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x001B offset: 0x4514
@scena.Code('func_1B_4514')
def func_1B_4514():
    ChrSetDirection(0x00FE, 270, 400)
    ChrWalkTo(0x00FE, 57480, 410, 60010, 2000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)

    Return()

# id: 0x001C offset: 0x4537
@scena.Code('func_1C_4537')
def func_1C_4537():
    ChrSetDirection(0x00FE, 270, 400)
    ChrWalkTo(0x00FE, 58480, 0, 60010, 2000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)

    Return()

# id: 0x001D offset: 0x455A
@scena.Code('func_1D_455A')
def func_1D_455A():
    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_AD('ED6_DT24/C_VIS182._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(500)

    OP_56(0x03)
    OP_AE(0x000001F4)
    Sleep(500)

    SetScenaFlags(ScenaFlag(0x041D, 2, 0x20EA))
    TalkEnd(0x00FF)

    Return()

# id: 0x001E offset: 0x4588
@scena.Code('func_1E_4588')
def func_1E_4588():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x041D, 2, 0x20EA)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_45A0',
    )

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))
    Call(0, 0x0020)

    def _loc_45A0(): pass

    label('loc_45A0')

    Return()

# id: 0x001F offset: 0x45A1
@scena.Code('func_1F_45A1')
def func_1F_45A1():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x041D, 2, 0x20EA)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_45B6',
    )

    Call(0, 0x0020)

    def _loc_45B6(): pass

    label('loc_45B6')

    Return()

# id: 0x0020 offset: 0x45B7
@scena.Code('func_20_45B7')
def func_20_45B7():
    EventBegin(0x00)
    Fade(1000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_460C',
    )

    ChrSetPos(0x0101, 46000, 0, 45140, 90)
    ChrSetPos(0x0102, 45600, 0, 44220, 90)
    ChrSetPos(0x00F8, 44800, 0, 45140, 90)
    ChrSetPos(0x00F9, 44400, 0, 44220, 90)

    Jump('loc_4650')

    def _loc_460C(): pass

    label('loc_460C')

    ChrSetPos(0x0101, 55500, 0, 45140, 270)
    ChrSetPos(0x0102, 55900, 0, 44220, 270)
    ChrSetPos(0x00F8, 56700, 0, 45140, 270)
    ChrSetPos(0x00F9, 57100, 0, 44220, 270)

    def _loc_4650(): pass

    label('loc_4650')

    OP_69(0x0101, 0)

    @scena.Lambda('lambda_465D')
    def lambda_465D():
        OP_94(0x00, 0x00FE, 0x0000, 0x000005DC, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_465D)

    Sleep(30)

    @scena.Lambda('lambda_4678')
    def lambda_4678():
        OP_94(0x00, 0x00FE, 0x0000, 0x000005DC, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_4678)

    Sleep(30)

    @scena.Lambda('lambda_4693')
    def lambda_4693():
        OP_94(0x00, 0x00FE, 0x0000, 0x000005DC, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_4693)

    Sleep(30)

    @scena.Lambda('lambda_46AE')
    def lambda_46AE():
        OP_94(0x00, 0x00FE, 0x0000, 0x000005DC, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_46AE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_470C',
    )

    @scena.Lambda('lambda_46CB')
    def lambda_46CB():
        CameraMove(47500, 0, 44800, 2000)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_46CB)

    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)

    Jump('loc_4750')

    def _loc_470C(): pass

    label('loc_470C')

    @scena.Lambda('lambda_4712')
    def lambda_4712():
        CameraMove(52500, 0, 44800, 2000)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_4712)

    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    def _loc_4750(): pass

    label('loc_4750')

    OP_0D()
    WaitForThreadExit(0x000D, 0x0001)
    Sleep(400)

    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010350198V#1015F#2P啊……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010350199V怎么回事\n',
            '这种地方为什么聚集了这么多人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrSetDirection(0x0102, 180, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_4842',
    )

    ChrTalk(
        0x0102,
        (
            '#0020350200V#1043F#3P原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020350201V#1035F……是这样吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_488B')

    def _loc_4842(): pass

    label('loc_4842')

    ChrTalk(
        0x0102,
        (
            '#0020350202V#1043F#4P原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020350201V#1035F……是这样吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_488B(): pass

    label('loc_488B')

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrSetDirection(0x0101, 180, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_48F1',
    )

    ChrTalk(
        0x0101,
        (
            '#0010350204V#1020F#2P啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()

    @scena.Lambda('lambda_48DC')
    def lambda_48DC():
        CameraMove(47500, 8000, 35000, 5500)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_48DC)

    Jump('loc_492F')

    def _loc_48F1(): pass

    label('loc_48F1')

    ChrTalk(
        0x0101,
        (
            '#0010350205V#1020F#1P啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()

    @scena.Lambda('lambda_491D')
    def lambda_491D():
        CameraMove(52500, 8000, 35500, 5500)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_491D)

    def _loc_492F(): pass

    label('loc_492F')

    @scena.Lambda('lambda_4935')
    def lambda_4935():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_4935)

    Sleep(100)

    @scena.Lambda('lambda_4948')
    def lambda_4948():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_4948)

    Sleep(1500)

    FadeOut(2000, 0, -1)
    OP_0D()
    TerminateThread(0x000D, 0x01)
    Sleep(1400)

    OP_AD('ED6_DT24/C_VIS182._CH', 0x0000, 0x0000, 0x000000C8)
    Sleep(2500)

    FadeIn(0, 0)

    ExecExpressionWithValue(
        0x000D,
        0x01,
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.GetChrWork, 0xF9, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x02,
        (
            (Expr.GetChrWork, 0x101, 0x2),
            (Expr.GetChrWork, 0xF9, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x03,
        (
            (Expr.GetChrWork, 0x101, 0x3),
            (Expr.GetChrWork, 0xF9, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x000D, 0)
    ChrSetDirection(0x00F8, 180, 0)
    ChrSetDirection(0x00F9, 180, 0)
    SetMessageWindowPos(100, 300, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010350206V#1020F浮、浮游都市……！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010350207V好、好巨大……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4A73',
    )

    SetMessageWindowPos(250, 320, -1, -1)
    TalkSetChrName('提妲')

    Talk(
        (
            '#0070350208V#065F浮、浮浮……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_4A73(): pass

    label('loc_4A73')

    SetMessageWindowPos(400, 340, -1, -1)
    TalkSetChrName('约修亚')

    Talk(
        (
            '#0020350209V#1042F从地面上看\n',
            '更能感到它的压迫力……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AE(0x000001F4)
    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4B8F',
    )

    ChrTalk(
        0x0106,
        (
            '#0050350210V#053F对一般人来说，\n',
            '感到不安也是正常的了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050350211V#050F这样的话，现在\n',
            '正是需要我们游击士的时候。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050350212V哪怕只能起到很微小的作用，\n',
            '也要努力让市民们安心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4CAD')

    def _loc_4B8F(): pass

    label('loc_4B8F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4C40',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350213V#022F市民们会\n',
            '感到不安也是当然的了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030350214V现在正是考验我们\n',
            '游击士的时候啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030350215V哪怕只能起到很微小的作用，\n',
            '我们也要拿出全力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4CAD')

    def _loc_4C40(): pass

    label('loc_4C40')

    ChrTalk(
        0x0108,
        (
            '#0080350216V#072F这样的话，市民们\n',
            '会害怕也是当然的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080350217V在这种时候，\n',
            '我们游击士就更要努力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4CAD(): pass

    label('loc_4CAD')

    ChrTalk(
        0x0101,
        (
            '#0010350218V#1002F嗯、嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350219V#1042F是啊……\n',
            '快行动吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x041D, 2, 0x20EA))
    EventEnd(0x00)

    Return()

# id: 0x0021 offset: 0x4CFE
@scena.Code('func_21_4CFE')
def func_21_4CFE():
    FadeOut(0, 0, -1)
    EventBegin(0x00)
    ChrSetPos(0x0101, 48500, 0, 49500, 180)
    ChrSetPos(0x0102, 47600, 250, 49900, 180)
    ChrSetPos(0x00F8, 48500, 250, 50700, 180)
    ChrSetPos(0x00F9, 47600, 250, 51100, 180)
    OP_69(0x0101, 0)

    @scena.Lambda('lambda_4D5B')
    def lambda_4D5B():
        OP_94(0x00, 0x00FE, 0x0000, 0x000005DC, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4D5B)

    Sleep(30)

    @scena.Lambda('lambda_4D76')
    def lambda_4D76():
        OP_94(0x00, 0x00FE, 0x0000, 0x000005DC, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_4D76)

    Sleep(30)

    @scena.Lambda('lambda_4D91')
    def lambda_4D91():
        OP_94(0x00, 0x00FE, 0x0000, 0x000005DC, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_4D91)

    Sleep(30)

    @scena.Lambda('lambda_4DAC')
    def lambda_4DAC():
        OP_94(0x00, 0x00FE, 0x0000, 0x000005DC, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_4DAC)

    @scena.Lambda('lambda_4DC2')
    def lambda_4DC2():
        CameraMove(48220, 0, 47000, 2000)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_4DC2)

    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x000D, 0x0001)
    ChrSetDirection(0x0101, 135, 400)

    @scena.Lambda('lambda_4DF0')
    def lambda_4DF0():
        ChrSetDirection(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_4DF0)

    Sleep(120)

    @scena.Lambda('lambda_4E03')
    def lambda_4E03():
        ChrSetDirection(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_4E03)

    Sleep(60)

    @scena.Lambda('lambda_4E16')
    def lambda_4E16():
        ChrSetDirection(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_4E16)

    Sleep(400)

    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010350220V#1015F#2P啊……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010350199V怎么回事\n',
            '这种地方为什么聚集了这么多人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrSetDirection(0x0102, 180, 400)

    ChrTalk(
        0x0102,
        (
            '#0020350222V#1043F#3P原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020350201V#1035F……是这样吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrSetDirection(0x0101, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010350224V#1020F#2P啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()

    @scena.Lambda('lambda_4F4A')
    def lambda_4F4A():
        CameraMove(48220, 8000, 35000, 5500)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_4F4A)

    @scena.Lambda('lambda_4F62')
    def lambda_4F62():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_4F62)

    Sleep(100)

    @scena.Lambda('lambda_4F75')
    def lambda_4F75():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_4F75)

    Sleep(1500)

    FadeOut(2000, 0, -1)
    OP_0D()
    TerminateThread(0x000D, 0x01)
    Sleep(1400)

    OP_AD('ED6_DT24/C_VIS182._CH', 0x0000, 0x0000, 0x000000C8)
    Sleep(2500)

    FadeIn(0, 0)

    ExecExpressionWithValue(
        0x000D,
        0x01,
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.GetChrWork, 0xF9, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x02,
        (
            (Expr.GetChrWork, 0x101, 0x2),
            (Expr.GetChrWork, 0xF9, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x03,
        (
            (Expr.GetChrWork, 0x101, 0x3),
            (Expr.GetChrWork, 0xF9, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x000D, 0)
    ChrSetDirection(0x00F8, 180, 0)
    ChrSetDirection(0x00F9, 180, 0)
    SetMessageWindowPos(100, 300, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010350206V#1020F浮、浮游都市……！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010350207V好、好巨大……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_50A0',
    )

    SetMessageWindowPos(250, 320, -1, -1)
    TalkSetChrName('提妲')

    Talk(
        (
            '#0070350227V#065F浮、浮浮……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_50A0(): pass

    label('loc_50A0')

    SetMessageWindowPos(400, 340, -1, -1)
    TalkSetChrName('约修亚')

    Talk(
        (
            '#0020350209V#1042F从地面上看\n',
            '更能感到它的压迫力……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AE(0x000001F4)
    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_51BC',
    )

    ChrTalk(
        0x0106,
        (
            '#0050350210V#053F对一般人来说，\n',
            '感到不安也是正常的了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050350211V#050F这样的话，现在\n',
            '正是需要我们游击士的时候。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050350212V哪怕只能起到很微小的作用，\n',
            '也要努力让市民们安心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_52DA')

    def _loc_51BC(): pass

    label('loc_51BC')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_526D',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350213V#022F市民们会\n',
            '感到不安也是当然的了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030350214V现在正是考验我们\n',
            '游击士的时候啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030350215V哪怕只能起到很微小的作用，\n',
            '我们也要拿出全力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_52DA')

    def _loc_526D(): pass

    label('loc_526D')

    ChrTalk(
        0x0108,
        (
            '#0080350216V#072F这样的话，市民们\n',
            '会害怕也是当然的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080350217V在这种时候，\n',
            '我们游击士就更要努力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_52DA(): pass

    label('loc_52DA')

    ChrTalk(
        0x0101,
        (
            '#0010210485V#1002F嗯、嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350219V#1042F是啊……\n',
            '快行动吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x041D, 2, 0x20EA))
    EventEnd(0x00)

    Return()

# id: 0x0022 offset: 0x532B
@scena.Code('func_22_532B')
def func_22_532B():
    FadeOut(0, 0, -1)
    EventBegin(0x00)
    ChrSetPos(0x0101, 49070, -750, 38730, 0)
    ChrSetPos(0x0102, 47920, -1000, 38550, 0)
    ChrSetPos(0x00F8, 49350, -1500, 37760, 0)
    ChrSetPos(0x00F9, 48170, -1750, 37520, 0)
    CameraMove(49500, -250, 39450, 0)
    OP_67(0, 9090, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    @scena.Lambda('lambda_53BE')
    def lambda_53BE():
        ChrWalkTo(0x00FE, 48840, 0, 42360, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_53BE)

    Sleep(30)

    @scena.Lambda('lambda_53DE')
    def lambda_53DE():
        ChrWalkTo(0x00FE, 47440, 0, 42320, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_53DE)

    Sleep(30)

    @scena.Lambda('lambda_53FE')
    def lambda_53FE():
        ChrWalkTo(0x00FE, 48720, 0, 41040, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_53FE)

    Sleep(30)

    @scena.Lambda('lambda_541E')
    def lambda_541E():
        ChrWalkTo(0x00FE, 47230, 0, 41020, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_541E)

    @scena.Lambda('lambda_5439')
    def lambda_5439():
        CameraMove(50030, 0, 43350, 3000)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_5439)

    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x000D, 0x0001)
    WaitForThreadExit(0x0101, 0x0001)
    ChrSetDirection(0x0101, 45, 400)
    WaitForThreadExit(0x00F7, 0x0001)

    @scena.Lambda('lambda_5471')
    def lambda_5471():
        ChrSetDirection(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_5471)

    Sleep(60)

    WaitForThreadExit(0x00F8, 0x0001)

    @scena.Lambda('lambda_5489')
    def lambda_5489():
        ChrSetDirection(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_5489)

    Sleep(60)

    WaitForThreadExit(0x00F9, 0x0001)

    @scena.Lambda('lambda_54A1')
    def lambda_54A1():
        ChrSetDirection(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_54A1)

    Sleep(400)

    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010350239V#1015F#2P啊……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010350199V怎么回事\n',
            '这种地方为什么聚集了这么多人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrSetDirection(0x0102, 180, 400)

    ChrTalk(
        0x0102,
        (
            '#0020350241V#1043F#3P原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020350201V#1035F……是这样吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrSetDirection(0x0101, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010350243V#1020F#2P啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()

    @scena.Lambda('lambda_55D5')
    def lambda_55D5():
        CameraMove(48220, 8000, 35000, 5500)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_55D5)

    @scena.Lambda('lambda_55ED')
    def lambda_55ED():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_55ED)

    Sleep(100)

    @scena.Lambda('lambda_5600')
    def lambda_5600():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_5600)

    Sleep(1500)

    FadeOut(2000, 0, -1)
    OP_0D()
    TerminateThread(0x000D, 0x01)
    Sleep(1400)

    OP_AD('ED6_DT24/C_VIS182._CH', 0x0000, 0x0000, 0x000000C8)
    Sleep(2500)

    FadeIn(0, 0)
    CameraMove(48890, 0, 42880, 0)
    OP_67(0, 9090, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetDirection(0x00F8, 180, 0)
    ChrSetDirection(0x00F9, 180, 0)
    SetMessageWindowPos(100, 300, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010350206V#1020F浮、浮游都市……！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010350207V好、好巨大……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5722',
    )

    SetMessageWindowPos(250, 320, -1, -1)
    TalkSetChrName('提妲')

    Talk(
        (
            '#0070350246V#065F浮、浮浮……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_5722(): pass

    label('loc_5722')

    SetMessageWindowPos(400, 340, -1, -1)
    TalkSetChrName('约修亚')

    Talk(
        (
            '#0020350209V#1042F从地面上看\n',
            '更能感到它的压迫力……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AE(0x000001F4)
    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_583E',
    )

    ChrTalk(
        0x0106,
        (
            '#0050350210V#053F对一般人来说，\n',
            '感到不安也是正常的了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050350211V#050F这样的话，现在\n',
            '正是需要我们游击士的时候。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050350212V哪怕只能起到很微小的作用，\n',
            '也要努力让市民们安心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_595C')

    def _loc_583E(): pass

    label('loc_583E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_58EF',
    )

    ChrTalk(
        0x0103,
        (
            '#0030350213V#022F市民们会\n',
            '感到不安也是当然的了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030350214V现在正是考验我们\n',
            '游击士的时候啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030350215V哪怕只能起到很微小的作用，\n',
            '我们也要拿出全力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_595C')

    def _loc_58EF(): pass

    label('loc_58EF')

    ChrTalk(
        0x0108,
        (
            '#0080350216V#072F这样的话，市民们\n',
            '会害怕也是当然的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080350217V在这种时候，\n',
            '我们游击士就更要努力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_595C(): pass

    label('loc_595C')

    ChrTalk(
        0x0101,
        (
            '#0010350218V#1002F嗯、嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020350219V#1042F是啊……\n',
            '快行动吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x041D, 2, 0x20EA))
    EventEnd(0x00)

    Return()

# id: 0x0023 offset: 0x59AD
@scena.Code('func_23_59AD')
def func_23_59AD():
    FadeOut(0, 0, -1)
    CameraMove(97010, 0, 95840, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
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
        (0x00000000, 'loc_5A64'),
        (0x00000001, 'loc_5A6A'),
        (-1, 'loc_5A70'),
    )

    def _loc_5A64(): pass

    label('loc_5A64')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_5A70')

    def _loc_5A6A(): pass

    label('loc_5A6A')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_5A70')

    def _loc_5A70(): pass

    label('loc_5A70')

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['阿加特'],
            0x00FF,
            0x00FF,
        ),
        (
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

    Return()

# id: 0x0024 offset: 0x5AAC
@scena.Code('func_24_5AAC')
def func_24_5AAC():
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
        (0x00000000, 'loc_5B29'),
        (0x00000001, 'loc_5B2F'),
        (-1, 'loc_5B35'),
    )

    def _loc_5B29(): pass

    label('loc_5B29')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_5B35')

    def _loc_5B2F(): pass

    label('loc_5B2F')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_5B35')

    def _loc_5B35(): pass

    label('loc_5B35')

    Return()

# id: 0x0025 offset: 0x5B36
@scena.Code('func_25_5B36')
def func_25_5B36():
    MapClearFlags(0x00000001)
    CameraMove(64510, 0, -14780, 92)
    FadeIn(0, 0)
    Sleep(100)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            0x00FF,
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

# id: 0x0026 offset: 0x5B93
@scena.Code('func_26_5B93')
def func_26_5B93():
    MapClearFlags(0x00000001)
    CameraMove(106730, -1920, 53920, 0)
    Sleep(100)

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['雪拉扎德'],
            ChrTable['提妲'],
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

# id: 0x0027 offset: 0x5BEC
@scena.Code('func_27_5BEC')
def func_27_5BEC():
    OP_13(0x002A)

    Return()

# id: 0x0028 offset: 0x5BF0
@scena.Code('func_28_5BF0')
def func_28_5BF0():
    OP_13(0x0026)

    Return()

# id: 0x0029 offset: 0x5BF4
@scena.Code('func_29_5BF4')
def func_29_5BF4():
    OP_13(0x0025)

    Return()

# id: 0x002A offset: 0x5BF8
@scena.Code('func_2A_5BF8')
def func_2A_5BF8():
    OP_13(0x0020)

    Return()

# id: 0x002B offset: 0x5BFC
@scena.Code('func_2B_5BFC')
def func_2B_5BFC():
    OP_13(0x0028)

    Return()

# id: 0x002C offset: 0x5C00
@scena.Code('func_2C_5C00')
def func_2C_5C00():
    OP_13(0x002B)

    Return()

# id: 0x002D offset: 0x5C04
@scena.Code('func_2D_5C04')
def func_2D_5C04():
    OP_13(0x0021)

    Return()

# id: 0x002E offset: 0x5C08
@scena.Code('func_2E_5C08')
def func_2E_5C08():
    OP_13(0x0027)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T1202_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1202   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1202.x'
    header.mapIndex       = 1
    header.bgm            = 15
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T1202_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
        ('ED6_DT26/CH20356._CH', 'ED6_DT26/CH20356P._CP'),
        ('ED6_DT07/CH02080._CH', 'ED6_DT07/CH02080P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT06/CH20137._CH', 'ED6_DT06/CH20137P._CP'),
        ('ED6_DT07/CH00151._CH', 'ED6_DT07/CH00151P._CP'),
        ('ED6_DT07/CH00054._CH', 'ED6_DT07/CH00054P._CP'),
        ('ED6_DT26/CH20355._CH', 'ED6_DT26/CH20355P._CP'),
        ('ED6_DT26/CH20357._CH', 'ED6_DT26/CH20357P._CP'),
        ('ED6_DT07/CH01490._CH', 'ED6_DT07/CH01490P._CP'),
        ('ED6_DT07/CH01060._CH', 'ED6_DT07/CH01060P._CP'),
        ('ED6_DT07/CH01470._CH', 'ED6_DT07/CH01470P._CP'),
        ('ED6_DT07/CH01070._CH', 'ED6_DT07/CH01070P._CP'),
        ('ED6_DT07/CH01230._CH', 'ED6_DT07/CH01230P._CP'),
        ('ED6_DT26/CH20354._CH', 'ED6_DT26/CH20354P._CP'),
        ('ED6_DT27/CH03540._CH', 'ED6_DT27/CH03540P._CP'),
        ('ED6_DT27/CH03790._CH', 'ED6_DT27/CH03790P._CP'),
        ('ED6_DT07/CH01180._CH', 'ED6_DT07/CH01180P._CP'),
    ]

# id: 0x10001 offset: 0x152
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '剑帝莱维',
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
            name                = '摩尔根将军',
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
            name                = '捧花',
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
            name                = '捧花',
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
            name                = '捧花',
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
            name                = '莱森村长',
            x                   = 33060,
            z                   = 8000,
            y                   = 36610,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '菲戈',
            x                   = 20640,
            z                   = -4000,
            y                   = 19180,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '贝斯卡',
            x                   = 19590,
            z                   = -4000,
            y                   = 16200,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '库赖老人',
            x                   = 17380,
            z                   = -4000,
            y                   = 9850,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '巴德斯',
            x                   = -120,
            z                   = 0,
            y                   = 28460,
            direction           = 225,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '鲁伊',
            x                   = -1120,
            z                   = 0,
            y                   = 26660,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '弗兰',
            x                   = -2120,
            z                   = 0,
            y                   = 28460,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '斯丁克',
            x                   = 4040,
            z                   = 0,
            y                   = 17210,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '碧尔奈婆婆',
            x                   = 33030,
            z                   = 8000,
            y                   = 35790,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '米拉诺',
            x                   = 25990,
            z                   = -4000,
            y                   = 14870,
            direction           = 270,
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
            name                = '目标用照相机',
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
            name                = '拉文努山道方向',
            x                   = -2080,
            z                   = 0,
            y                   = -80,
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
            name                = '拉文努废坑方向',
            x                   = 7170,
            z                   = 8000,
            y                   = 78890,
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

# id: 0x10002 offset: 0x392
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x392
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 5000,
            y           = 0,
            z           = 34240,
            range       = 1500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000001C,
        ),
        ScenaEventData(
            x           = 5150,
            y           = 4550,
            z           = 41780,
            range       = 1500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000001C,
        ),
        ScenaEventData(
            x           = 5310,
            y           = 0,
            z           = 23020,
            range       = 1500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000001D,
        ),
        ScenaEventData(
            x           = 6000,
            y           = 4400,
            z           = 54640,
            range       = 1500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000001E,
        ),
        ScenaEventData(
            x           = -3900,
            y           = -100,
            z           = 7250,
            range       = -100,
            dword_10    = 0x0000076C,
            dword_14    = 0x0000203A,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000019,
        ),
        ScenaEventData(
            x           = 5100,
            y           = 8000,
            z           = 67350,
            range       = 9000,
            dword_10    = 0x00002710,
            dword_14    = 0x00010AFE,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000019,
        ),
    )

# id: 0x10004 offset: 0x452
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 34960,
            triggerZ            = -3850,
            triggerY            = 8220,
            triggerRange        = 1000,
            actorX              = 35010,
            actorZ              = -4200,
            actorY              = 5190,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 33020,
            triggerZ            = 8000,
            triggerY            = 35080,
            triggerRange        = 1000,
            actorX              = 33020,
            actorZ              = 9200,
            actorY              = 35080,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001B,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x49A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_4BC',
    )

    SetScenaFlags(ScenaFlag(0x0380, 1, 0x1C01))

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x53),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    Event(0, func_11_36E6)

    Jump('loc_4DF')

    def _loc_4BC(): pass

    label('loc_4BC')

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
        'loc_4DF',
    )

    MapSetFlags(0x10000000)
    Event(1, 0x0000)

    def _loc_4DF(): pass

    label('loc_4DF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_56A',
    )

    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetPos(0x000F, 18320, -4000, 10850, 208)
    ChrSetPos(0x0011, 24450, -4000, 9390, 180)
    ChrSetPos(0x0013, 22320, -4000, 11950, 154)
    ChrSetPos(0x0012, 14750, -4000, 21340, 270)
    ChrSetPos(0x0010, 22180, -4000, 19220, 188)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_567',
    )

    ChrClearFlags(0x0014, 0x0080)
    ChrClearFlags(0x0015, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034A, 3, 0x1A53)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_564',
    )

    ChrSetFlags(0x0014, 0x0010)

    def _loc_564(): pass

    label('loc_564')

    Jump('loc_567')

    def _loc_567(): pass

    label('loc_567')

    Jump('loc_670')

    def _loc_56A(): pass

    label('loc_56A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_608',
    )

    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrSetPos(0x0011, 4720, 0, 28930, 225)
    CreateThread(0x0011, 0x00, 0x00, func_03_8BB)
    ChrSetPos(0x0013, 2730, 0, 27400, 45)
    CreateThread(0x0013, 0x00, 0x00, func_05_959)
    ChrSetPos(0x0012, 2610, 0, 28970, 135)
    ChrSetPos(0x0010, 18000, -4000, 22100, 345)
    ChrSetPos(0x000E, 13250, 4550, 33630, 180)
    CreateThread(0x0011, 0x00, 0x00, func_02_73E)
    ChrSetPos(0x000F, 18030, -4000, 11140, 244)

    If(
        (
            (Expr.Eval, "OP_29(0x007C, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_605',
    )

    ChrClearFlags(0x0016, 0x0080)

    def _loc_605(): pass

    label('loc_605')

    Jump('loc_670')

    def _loc_608(): pass

    label('loc_608')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_670',
    )

    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetPos(0x0011, 21720, 0, 30550, 163)
    CreateThread(0x0011, 0x00, 0x00, func_03_8BB)
    ChrSetPos(0x0010, 17940, -4000, 22470, 339)
    ChrSetPos(0x000E, 20170, -4000, 10980, 232)
    CreateThread(0x000E, 0x00, 0x00, func_04_935)
    ChrSetPos(0x000F, 13000, 4550, 33630, 191)

    def _loc_670(): pass

    label('loc_670')

    Return()

# id: 0x0001 offset: 0x671
@scena.Code('func_01_671')
def func_01_671():
    OP_16(0x02, 4000, -109000, -92000, 2293827)
    OP_B2(0x00, 0x04, 0x0080)
    OP_B2(0x00, 0x05, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_69C',
    )

    OP_71(0x0015, 0x0004)

    Jump('loc_724')

    def _loc_69C(): pass

    label('loc_69C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_6D3',
    )

    OP_71(0x000B, 0x0004)
    OP_71(0x000C, 0x0004)
    OP_71(0x000D, 0x0004)
    OP_71(0x000E, 0x0004)
    OP_71(0x000F, 0x0004)
    OP_71(0x0010, 0x0004)
    OP_71(0x0011, 0x0004)
    OP_71(0x0012, 0x0004)
    OP_71(0x0013, 0x0004)

    Jump('loc_724')

    def _loc_6D3(): pass

    label('loc_6D3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_724',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x1A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x02000000)
    OP_71(0x000B, 0x0004)
    OP_71(0x000C, 0x0004)
    OP_71(0x000D, 0x0004)
    OP_71(0x000E, 0x0004)
    OP_71(0x000F, 0x0004)
    OP_71(0x0010, 0x0004)
    OP_71(0x0011, 0x0004)
    OP_71(0x0012, 0x0004)
    OP_71(0x0013, 0x0004)
    OP_71(0x0014, 0x0004)
    OP_B2(0x01, 0x04, 0x0080)
    OP_B2(0x01, 0x05, 0x0080)

    def _loc_724(): pass

    label('loc_724')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0350, 2, 0x1A82)),
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_73D',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_73D(): pass

    label('loc_73D')

    Return()

# id: 0x0002 offset: 0x73E
@scena.Code('func_02_73E')
def func_02_73E():
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
        'loc_763',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_8A5')

    def _loc_763(): pass

    label('loc_763')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_77C',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_8A5')

    def _loc_77C(): pass

    label('loc_77C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_795',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_8A5')

    def _loc_795(): pass

    label('loc_795')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7AE',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_8A5')

    def _loc_7AE(): pass

    label('loc_7AE')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7C7',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_8A5')

    def _loc_7C7(): pass

    label('loc_7C7')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7E0',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_8A5')

    def _loc_7E0(): pass

    label('loc_7E0')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7F9',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_8A5')

    def _loc_7F9(): pass

    label('loc_7F9')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_812',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_8A5')

    def _loc_812(): pass

    label('loc_812')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_82B',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_8A5')

    def _loc_82B(): pass

    label('loc_82B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_844',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_8A5')

    def _loc_844(): pass

    label('loc_844')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_85D',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_8A5')

    def _loc_85D(): pass

    label('loc_85D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_876',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_8A5')

    def _loc_876(): pass

    label('loc_876')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_88F',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_8A5')

    def _loc_88F(): pass

    label('loc_88F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8A5',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_8A5(): pass

    label('loc_8A5')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_8BA',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_8A5')

    def _loc_8BA(): pass

    label('loc_8BA')

    Return()

# id: 0x0003 offset: 0x8BB
@scena.Code('func_03_8BB')
def func_03_8BB():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_911',
    )

    def _loc_8C2(): pass

    label('loc_8C2')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_90E',
    )

    ChrWalkTo(0x00FE, 5060, 0, 28370, 2000, 0x00)
    ChrSetDirection(0x00FE, 225, 500)
    Sleep(1000)

    ChrWalkTo(0x00FE, 3990, 0, 29380, 2000, 0x00)
    ChrSetDirection(0x00FE, 225, 500)
    Sleep(1000)

    Jump('loc_8C2')

    def _loc_90E(): pass

    label('loc_90E')

    Jump('loc_934')

    def _loc_911(): pass

    label('loc_911')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_934',
    )

    OP_8D(0x00FE, 20530, 32090, 23220, 29410, 2000)

    Jump('loc_911')

    def _loc_934(): pass

    label('loc_934')

    Return()

# id: 0x0004 offset: 0x935
@scena.Code('func_04_935')
def func_04_935():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_958',
    )

    OP_8D(0x00FE, 18440, 12240, 22280, 12290, 1000)

    Jump('func_04_935')

    def _loc_958(): pass

    label('loc_958')

    Return()

# id: 0x0005 offset: 0x959
@scena.Code('func_05_959')
def func_05_959():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_9ED',
    )

    ChrWalkTo(0x00FE, 3520, 0, 28170, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 500)
    Sleep(1000)

    ChrWalkTo(0x00FE, 4190, 0, 27460, 2000, 0x00)
    ChrSetDirection(0x00FE, 45, 500)
    Sleep(1000)

    ChrWalkTo(0x00FE, 3760, 0, 26070, 2000, 0x00)
    ChrWalkTo(0x00FE, 3010, 0, 26480, 2000, 0x00)
    ChrSetDirection(0x00FE, 45, 500)
    Sleep(1000)

    ChrWalkTo(0x00FE, 2730, 0, 27400, 2000, 0x00)

    Jump('func_05_959')

    def _loc_9ED(): pass

    label('loc_9ED')

    Return()

# id: 0x0006 offset: 0x9EE
@scena.Code('func_06_9EE')
def func_06_9EE():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_A11',
    )

    OP_8D(0x00FE, 14450, 14900, 22350, 7670, 1000)

    Jump('func_06_9EE')

    def _loc_A11(): pass

    label('loc_A11')

    Return()

# id: 0x0007 offset: 0xA12
@scena.Code('func_07_A12')
def func_07_A12():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_B06',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_AA3',
    )

    ChrTalk(
        0x00FE,
        (
            '我已经收下了\n',
            '金耀石结晶……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，七耀石的结晶\n',
            '竟能以自己的力量生出……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '龙这样的生物真是\n',
            '超越了人的常识范围。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B06')

    def _loc_AA3(): pass

    label('loc_AA3')

    ChrTalk(
        0x00FE,
        (
            '噢，是你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我已经收下了\n',
            '金耀石结晶……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '作为村子的修复资金，\n',
            '我会小心使用的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_B06(): pass

    label('loc_B06')

    TalkEnd(0x000D)

    Return()

# id: 0x0008 offset: 0xB0A
@scena.Code('func_08_B0A')
def func_08_B0A():
    TalkBegin(0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_C29',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BCE',
    )

    ChrTalk(
        0x00FE,
        (
            '导力器的事也\n',
            '略有些担心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看着这些小树苗，\n',
            '不安的心情也烟消云散了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '等它们结出果实的时候\n',
            '所有事情都能顺利平息……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……虽不知道为什么，\n',
            '就是这么觉得。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_C26')

    def _loc_BCE(): pass

    label('loc_BCE')

    ChrTalk(
        0x00FE,
        (
            '看着这些小树苗，\n',
            '不安的心情也烟消云散了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真希望它们能就这样继续\n',
            '茁壮成长呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C26(): pass

    label('loc_C26')

    Jump('loc_FAB')

    def _loc_C29(): pass

    label('loc_C29')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_D0A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CB7',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，看来导力器\n',
            '好像动不了了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以说太依赖那种东西\n',
            '是不行的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '稍微用一下是可以，\n',
            '但近来实在太依赖了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_D07')

    def _loc_CB7(): pass

    label('loc_CB7')

    ChrTalk(
        0x00FE,
        (
            '近来不管做什么\n',
            '都太依赖导力器了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对大自然的恩惠\n',
            '应该更加重视才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D07(): pass

    label('loc_D07')

    Jump('loc_FAB')

    def _loc_D0A(): pass

    label('loc_D0A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_E56',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_DAC',
    )

    ChrTalk(
        0x00FE,
        (
            '为了培育树苗，\n',
            '首先不耕地怎么行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '新栽的树要结果实\n',
            '当然需要一些时间……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '幸好我已经习惯等待了。\n',
            '只要耐心地注视着它们成长就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E53')

    def _loc_DAC(): pass

    label('loc_DAC')

    ChrTalk(
        0x00FE,
        (
            '为了培育树苗，\n',
            '首先不耕地怎么行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '当然到结果实\n',
            '还要花很长时间……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，没什么好担心的。\n',
            '我早就习惯等待了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '百日战役之后\n',
            '我们也忍耐了很久呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_E53(): pass

    label('loc_E53')

    Jump('loc_FAB')

    def _loc_E56(): pass

    label('loc_E56')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_FAB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_EBB',
    )

    ChrTalk(
        0x00FE,
        (
            '贝斯卡对果树园的关爱\n',
            '可是真心的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次对那些机械的力量\n',
            '也不得不认可啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FAB')

    def _loc_EBB(): pass

    label('loc_EBB')

    ChrTalk(
        0x00FE,
        (
            '昨天，和贝斯卡那家伙\n',
            '谈过了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '知道了贝斯卡那家伙\n',
            '是真心爱着果树园的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '投入机械的想法\n',
            '虽然之前还不能接受……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但要是没有拖拉机\n',
            '在这里耕作也够辛苦的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所以，这次也不得不\n',
            '认可机械的力量。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '当然，只是这次而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_FAB(): pass

    label('loc_FAB')

    TalkEnd(0x0010)

    Return()

# id: 0x0009 offset: 0xFAF
@scena.Code('func_09_FAF')
def func_09_FAF():
    TalkBegin(0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_10A2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_105B',
    )

    ChrTalk(
        0x00FE,
        (
            '埃米尔那家伙在发牢骚，\n',
            '因为流通路线好像也停了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没有运输手段\n',
            '我们的水果就不能出货，\n',
            '日用品也很快就会短缺了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '果，果然\n',
            '不太妙啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_109F')

    def _loc_105B(): pass

    label('loc_105B')

    ChrTalk(
        0x00FE,
        (
            '运输路线停止了，\n',
            '果然问题严重啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可不是\n',
            '该发呆的时候……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_109F(): pass

    label('loc_109F')

    Jump('loc_13DF')

    def _loc_10A2(): pass

    label('loc_10A2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_11A7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1144',
    )

    ChrTalk(
        0x00FE,
        (
            '刚还在想终于种好了树苗，\n',
            '但导力器又出麻烦了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '拖拉机停止运做\n',
            '是在帮忙做完耕种之后。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果在工作中停止了，\n',
            '我可就颜面扫地了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_11A4')

    def _loc_1144(): pass

    label('loc_1144')

    ChrTalk(
        0x00FE,
        (
            '刚还在想终于种好了树苗，\n',
            '但导力器又出麻烦了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '拖拉机停止运做\n',
            '是在帮忙做完耕种之后。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11A4(): pass

    label('loc_11A4')

    Jump('loc_13DF')

    def _loc_11A7(): pass

    label('loc_11A7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_1285',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1214',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然现在还是空地，\n',
            '不过马上打算栽培树苗了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '似乎捐款也募集齐了，\n',
            '总算感觉能行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1282')

    def _loc_1214(): pass

    label('loc_1214')

    ChrTalk(
        0x00FE,
        (
            '虽然现在还是空地，\n',
            '不过马上打算栽培树苗了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '捐款似乎\n',
            '也募集了不少……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总算感觉\n',
            '感觉能行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_1282(): pass

    label('loc_1282')

    Jump('loc_13DF')

    def _loc_1285(): pass

    label('loc_1285')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_13DF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1311',
    )

    ChrTalk(
        0x00FE,
        (
            '总之为了果树园的复活，\n',
            '我也来帮忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '库赖爷爷似乎也\n',
            '认同了拖拉机的有效性……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '修理回来之后\n',
            '就得积极使用了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13DF')

    def _loc_1311(): pass

    label('loc_1311')

    ChrTalk(
        0x00FE,
        (
            '总之为了果树园的复活，\n',
            '我也来帮忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '谈话中还说到了\n',
            '我买的拖拉机……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '意外的是库赖爷爷\n',
            '竟然也稍微认同其的有效性了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯～是不是稍微\n',
            '理解我的想法了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '修理回来之后\n',
            '就得积极使用了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_13DF(): pass

    label('loc_13DF')

    TalkEnd(0x000F)

    Return()

# id: 0x000A offset: 0x13E3
@scena.Code('func_0A_13E3')
def func_0A_13E3():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_14D4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1441',
    )

    ChrTalk(
        0x00FE,
        (
            '里面的废坑还留有\n',
            '士兵在警卫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是辛苦啊。\n',
            '看来得去慰问一下呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14D1')

    def _loc_1441(): pass

    label('loc_1441')

    ChrTalk(
        0x00FE,
        (
            '火灾后的痕迹虽然收拾过，\n',
            '但心情还得好好整理整理啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '里面的废坑还留有\n',
            '士兵在警卫……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来想一会半会儿\n',
            '忘记那个事件是不可能的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_14D1(): pass

    label('loc_14D1')

    Jump('loc_15A5')

    def _loc_14D4(): pass

    label('loc_14D4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_15A5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1531',
    )

    ChrTalk(
        0x00FE,
        (
            '这里的景色\n',
            '变得相当凄凉呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '必须和大家齐心协力\n',
            '努力重建才行啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15A5')

    def _loc_1531(): pass

    label('loc_1531')

    ChrTalk(
        0x00FE,
        (
            '总算把果树园\n',
            '收拾得差不多了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里的景色\n',
            '变得相当凄凉呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '必须和大家齐心协力\n',
            '努力重建才行啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    def _loc_15A5(): pass

    label('loc_15A5')

    TalkEnd(0x000E)

    Return()

# id: 0x000B offset: 0x15A9
@scena.Code('func_0B_15A9')
def func_0B_15A9():
    TalkBegin(0x0011)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_1627',
    )

    ChrTalk(
        0x00FE,
        (
            '啊～啊，一直除草\n',
            '到底是烦人啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，现在是\n',
            '要努力的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '村子情况严峻。\n',
            '我们不振作可不行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1878')

    def _loc_1627(): pass

    label('loc_1627')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1697',
    )

    ChrTalk(
        0x00FE,
        (
            '即使不能开动导力器…\n',
            '但是照顾树苗还是能行的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了让它们早点开花结果，\n',
            '可要努力照顾才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1878')

    def _loc_1697(): pass

    label('loc_1697')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_176D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1719',
    )

    ChrTalk(
        0x00FE,
        (
            '我以前都很讨厌\n',
            '做果园的活……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，从今以后\n',
            '打算努力照顾它们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为想早点\n',
            '看到它们开花结果嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_176A')

    def _loc_1719(): pass

    label('loc_1719')

    ChrTalk(
        0x00FE,
        (
            '听说果树园\n',
            '在种新树苗啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了让它们早点开花结果\n',
            '我也要努力帮忙啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_176A(): pass

    label('loc_176A')

    Jump('loc_1878')

    def _loc_176D(): pass

    label('loc_176D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_1878',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_17B8',
    )

    ChrTurnDirection(0x00FE, 0x0106, 0)

    ChrTalk(
        0x00FE,
        (
            '阿加特哥哥！\n',
            '要加油啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也会支持你的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1878')

    def _loc_17B8(): pass

    label('loc_17B8')

    OP_62(0x00FE, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x00FE, 0x0106, 0)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '啊，阿加特哥哥！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难道\n',
            '要去打龙吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#051F啊啊，是这个打算。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '嗯，放心等着吧。\n',
            '马上解决掉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不愧是哥哥！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '加油啊！\n',
            '我也会支持你的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_1878(): pass

    label('loc_1878')

    TalkEnd(0x0011)

    Return()

# id: 0x000C offset: 0x187C
@scena.Code('func_0C_187C')
def func_0C_187C():
    TalkBegin(0x0012)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1C01',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 4, 0x2094)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1ADE',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_18EF',
    )

    ChrTalk(
        0x00FE,
        (
            '咦，阿加特哥哥。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且……\n',
            '还有姐姐和哥哥。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#051F哟，这不是鲁伊吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_190F')

    def _loc_18EF(): pass

    label('loc_18EF')

    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '啊……\n',
            '姐姐和哥哥。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_190F(): pass

    label('loc_190F')

    ChrTalk(
        0x0101,
        (
            '#1001F呀嗬～鲁伊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F好久不见了呢。\n',
            '还好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '嗯，嗯！我很好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在，大家\n',
            '都在果树园里帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为导力器不能动了，\n',
            '爸爸他们似乎非常忙……',
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
        'loc_1A08',
    )

    ChrTalk(
        0x0106,
        (
            '#051F喔，很努力嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我们也要多多支持\n',
            '村子里的人们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1ABF')

    def _loc_1A08(): pass

    label('loc_1A08')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A69',
    )

    ChrTalk(
        0x0103,
        (
            '#020F呵呵，看来很努力呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '虽然暂时会辛苦一点，\n',
            '但大家要齐心协力撑过去哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1ABF')

    def _loc_1A69(): pass

    label('loc_1A69')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1ABF',
    )

    ChrTalk(
        0x0108,
        (
            '#070F哈哈，真孝顺啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '虽然暂时会辛苦一点，\n',
            '不过就努力点撑过去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1ABF(): pass

    label('loc_1ABF')

    ChrTalk(
        0x00FE,
        (
            '嗯，嗯！明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))
    SetScenaFlags(ScenaFlag(0x0412, 4, 0x2094))

    Jump('loc_1BFE')

    def _loc_1ADE(): pass

    label('loc_1ADE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_1BAE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_1B3F',
    )

    ChrTalk(
        0x00FE,
        (
            '大家都在\n',
            '都在果树园里帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为导力器不能动了，\n',
            '爸爸他们好像很忙嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BAB')

    def _loc_1B3F(): pass

    label('loc_1B3F')

    ChrTalk(
        0x00FE,
        (
            '即使没有导力器，\n',
            '我们村子也不要紧哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，爸爸他们\n',
            '好像在担心什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是不是有什么困难呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1BAB(): pass

    label('loc_1BAB')

    Jump('loc_1BFE')

    def _loc_1BAE(): pass

    label('loc_1BAE')

    ChrTalk(
        0x00FE,
        (
            '大家都在\n',
            '都在果树园里帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为导力器不能动了，\n',
            '爸爸他们好像很忙嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1BFE(): pass

    label('loc_1BFE')

    Jump('loc_1EB1')

    def _loc_1C01(): pass

    label('loc_1C01')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_1EB1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0349, 5, 0x1A4D)),
            Expr.Return,
        ),
        'loc_1C56',
    )

    ChrTalk(
        0x00FE,
        (
            '之前一直待在家里，\n',
            '今天要玩个痛快！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '姐姐你们\n',
            '来一起玩吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EB1')

    def _loc_1C56(): pass

    label('loc_1C56')

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '啊～姐姐！',
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
        'loc_1CAA',
    )

    ChrTalk(
        0x00FE,
        (
            '还有阿加特哥哥！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1CAA(): pass

    label('loc_1CAA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1CEE',
    )

    ChrTalk(
        0x0101,
        (
            '#1018F嗨～鲁伊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#051F哟，看来挺精神嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D1F')

    def _loc_1CEE(): pass

    label('loc_1CEE')

    ChrTalk(
        0x0101,
        (
            '#1001F嗨～鲁伊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '太好了……\n',
            '看来挺精神嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D1F(): pass

    label('loc_1D1F')

    ChrTalk(
        0x00FE,
        (
            '嗯，很好哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为那个可怕的龙\n',
            '已经不在了吧？',
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
        'loc_1DC2',
    )

    ChrTalk(
        0x0106,
        (
            '#051F啊啊，那种事\n',
            '绝对不会再发生第二次了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F所以，出门尽情\n',
            '玩耍也没问题哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E0E')

    def _loc_1DC2(): pass

    label('loc_1DC2')

    ChrTalk(
        0x0101,
        (
            '#1006F嗯，那种事\n',
            '不会再发生第二次了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '所以，出门尽情\n',
            '玩耍也没问题哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E0E(): pass

    label('loc_1E0E')

    ChrTalk(
        0x00FE,
        (
            '嗯！啊，对了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为能出去玩了，\n',
            '这本书就给姐姐吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['牌技师杰克 ８卷']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    AddItem(ItemTable['牌技师杰克 ８卷'], 1)
    SetScenaFlags(ScenaFlag(0x0217, 4, 0x10BC))
    OP_0D()

    ChrTalk(
        0x00FE,
        (
            '那么，姐姐再见！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0349, 5, 0x1A4D))

    def _loc_1EB1(): pass

    label('loc_1EB1')

    TalkEnd(0x0012)

    Return()

# id: 0x000D offset: 0x1EB5
@scena.Code('func_0D_1EB5')
def func_0D_1EB5():
    TalkBegin(0x0013)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_1F8B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1F3C',
    )

    ChrTalk(
        0x00FE,
        (
            '我们的村子\n',
            '意外的平安无事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过柏斯那样的大城市，\n',
            '一定很严重吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样看来\n',
            '待在乡下倒也不坏。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    Jump('loc_1F88')

    def _loc_1F3C(): pass

    label('loc_1F3C')

    ChrTalk(
        0x00FE,
        (
            '不过柏斯那样的大城市，\n',
            '一定很严重吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样看来\n',
            '待在乡下倒也不坏。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F88(): pass

    label('loc_1F88')

    Jump('loc_209F')

    def _loc_1F8B(): pass

    label('loc_1F8B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1FD6',
    )

    ChrTalk(
        0x00FE,
        (
            '巴德斯那家伙\n',
            '意外的有干劲呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，不知道会持续多久？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_209F')

    def _loc_1FD6(): pass

    label('loc_1FD6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_209F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_2031',
    )

    ChrTalk(
        0x00FE,
        (
            '巴德斯真是的，\n',
            '又说那种话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '之前种树苗的时候\n',
            '也说过同样的话吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_209F')

    def _loc_2031(): pass

    label('loc_2031')

    ChrTalk(
        0x00FE,
        (
            '巴德斯真是的，\n',
            '又说那种话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '之前种树苗的时候\n',
            '也说过同样的话吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '反正做三天\n',
            '又会开始厌烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    def _loc_209F(): pass

    label('loc_209F')

    TalkEnd(0x0013)

    Return()

# id: 0x000E offset: 0x20A3
@scena.Code('func_0E_20A3')
def func_0E_20A3():
    TalkBegin(0x0016)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_2113',
    )

    ChrTalk(
        0x0016,
        (
            '啊，是你们。\n',
            '今天真是辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '我打算\n',
            '继续视察一下村子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '你们回去的时候\n',
            '也要当心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2228')

    def _loc_2113(): pass

    label('loc_2113')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Return,
        ),
        'loc_217B',
    )

    ChrTalk(
        0x0016,
        (
            '和丈夫商量了一下，\n',
            '我们也得准备一些重建资金才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '不能从一开始\n',
            '就完全依赖捐款啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2228')

    def _loc_217B(): pass

    label('loc_217B')

    ChrTalk(
        0x0016,
        (
            '买树苗也\n',
            '需要很多费用……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '果树园的重建\n',
            '怎么说都需要资金啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '虽然有募集捐款，\n',
            '但可不能完全靠那个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '和丈夫商量了一下，\n',
            '我们也得准备一些重建资金才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    def _loc_2228(): pass

    label('loc_2228')

    TalkEnd(0x0016)

    Return()

# id: 0x000F offset: 0x222C
@scena.Code('func_0F_222C')
def func_0F_222C():
    TalkBegin(0x0014)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 7, 0x35F)),
            Expr.Return,
        ),
        'loc_2239',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_2239(): pass

    label('loc_2239')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_22B5',
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
        (0x00000000, 'loc_22A9'),
        (0x00000001, 'loc_22AF'),
        (-1, 'loc_22B5'),
    )

    def _loc_22A9(): pass

    label('loc_22A9')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    Jump('loc_22B5')

    def _loc_22AF(): pass

    label('loc_22AF')

    ClearScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    Jump('loc_22B5')

    def _loc_22B5(): pass

    label('loc_22B5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034A, 3, 0x1A53)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2758',
    )

    ChrTalk(
        0x00FE,
        (
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_2465',
    )

    ChrTalk(
        0x0101,
        (
            '#1000F请问，唔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '斯丁克先生……对吧？\n',
            '柏斯支部的游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '你是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '卢格兰老爷子提到的那个\n',
            '正游击士的新人吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011F卢格兰爷爷说的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1041F这样看来，大概\n',
            '说的是我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们在之前龙的骚动中\n',
            '帮助过我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……非常感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F不，在那种情况下这是当然的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近在拉文努村\n',
            '似乎没发生什么混乱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们就\n',
            '专心完成自己的工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_274F')

    def _loc_2465(): pass

    label('loc_2465')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_24B6',
    )

    ChrTalk(
        0x0103,
        (
            '#020F好久不见，斯丁克。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x00FE, 0x0103, 400)

    Jump('loc_2510')

    def _loc_24B6(): pass

    label('loc_24B6')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2509',
    )

    ChrTalk(
        0x0106,
        (
            '#050F很久不见了，斯丁克。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x00FE, 0x0106, 400)

    Jump('loc_2510')

    def _loc_2509(): pass

    label('loc_2509')

    ChrTurnDirection(0x00FE, 0x0101, 400)

    def _loc_2510(): pass

    label('loc_2510')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2597',
    )

    ChrTalk(
        0x00FE,
        (
            '雪拉扎德吗…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们在之前龙的骚动中\n',
            '帮助过我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……非常感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F不，在那种情况下这是当然的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2703')

    def _loc_2597(): pass

    label('loc_2597')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_261A',
    )

    ChrTalk(
        0x00FE,
        (
            '阿加特吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们在之前龙的骚动中\n',
            '帮助过我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……非常感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#051F哪里，那是我们的义务啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2703')

    def _loc_261A(): pass

    label('loc_261A')

    ChrTalk(
        0x00FE,
        (
            '你是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '卢格兰老爷子提到的那个\n',
            '正游击士的新人吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011F卢格兰爷爷说的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1041F这样看来，大概\n',
            '说的是我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们在之前龙的骚动中\n',
            '帮助过我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……非常感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F不，在那种情况下这是当然的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2703(): pass

    label('loc_2703')

    ChrTalk(
        0x00FE,
        (
            '最近在拉文努村\n',
            '似乎没发生什么混乱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们就\n',
            '专心完成自己的工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_274F(): pass

    label('loc_274F')

    SetScenaFlags(ScenaFlag(0x034A, 3, 0x1A53))
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    Jump('loc_34EF')

    def _loc_2758(): pass

    label('loc_2758')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_27AE',
    )

    ChrTalk(
        0x00FE,
        (
            '最近在拉文努村\n',
            '似乎没发生什么混乱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们就\n',
            '专心完成自己的工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_34EF')

    def _loc_27AE(): pass

    label('loc_27AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0408, 1, 0x2041)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_33C5',
    )

    EventBegin(0x00)
    ChrSetDirection(0x00FE, 90, 0)
    Fade(1000)
    CameraMove(2360, 500, 17530, 0)
    OP_67(0, 6610, -10000, 0)
    CameraSetDistance(2700, 0)
    OP_6C(55000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 2780, 0, 18120, 90)
    ChrSetPos(0x0102, 2540, 0, 16820, 90)
    ChrSetPos(0x00F8, 1370, 0, 18000, 90)
    ChrSetPos(0x00F9, 1100, 0, 16660, 90)
    OP_0D()

    ChrTalk(
        0x00FE,
        (
            '…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔，是你们啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00FE, 270, 400)
    Sleep(400)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_28D7',
    )

    ChrTalk(
        0x0106,
        (
            '#051F还是老样子啊，斯丁克。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '<FIXME>ふ……これも性分でな。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_298A')

    def _loc_28D7(): pass

    label('loc_28D7')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_292C',
    )

    ChrTalk(
        0x0103,
        (
            '#020F还是老样子呢，斯丁克。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '<FIXME>ふ……これも性分でな。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_298A')

    def _loc_292C(): pass

    label('loc_292C')

    ChrTalk(
        0x0101,
        (
            '#1000F你好，斯丁克先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '<FIXME>#1040Fお疲れ様です。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '<FIXME>ああ……互いにな。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_298A(): pass

    label('loc_298A')

    OP_62(0x00FE, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1500)

    OP_63(0x00FE)
    Sleep(500)

    ChrTalk(
        0x00FE,
        (
            '<FIXME>そうだ、突然で悪いが\n',
            'お前たち……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '<FIXME>こいつを見てくれないか？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '<FIXME>#1004Fえ……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '<FIXME>スティングから\n',
            '黒光りする宝玉を見せてもらった。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    Sleep(500)

    ChrTalk(
        0x00FE,
        (
            '<FIXME>見た所、クオーツの\n',
            '類だとは思うんだが……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '<FIXME>どうもオーブメントに\n',
            '嵌められそうになくてな。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '<FIXME>#1015Fヨシュア、あれって……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '<FIXME>#1035Fうん、おそらく古代に\n',
            '使われていたクオーツだろうね。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '<FIXME>ふむ、話には聞いていたが\n',
            'こいつがそうなのか……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '<FIXME>確かスロットを強化すれば、\n',
            '組み込めるという話だったな。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '<FIXME>#1011Fうん、そうだけど……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1015Fスティングさんは一体\n',
            'どこでそれを手に入れたの？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '<FIXME>ああ、実は……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '<FIXME>琥珀の塔の近くだったか……\n',
            '何とも変わった魔獣に出会ってな。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '<FIXME>そいつを倒した時に拾ったんだ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '<FIXME>生きた化石というか……\n',
            'そんな感じの姿をした魔獣だった。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0420, 0, 0x2100)),
            (Expr.TestScenaFlags, ScenaFlag(0x0420, 1, 0x2101)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x0420, 2, 0x2102)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x0420, 3, 0x2103)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_2DCD',
    )

    ChrTalk(
        0x0101,
        (
            '<FIXME>#1004Fそれって、もしかして……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '<FIXME>#1042Fうん、塔の屋上で倒した\n',
            '魔獣と同じ類かもしれない。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '<FIXME>ほう、お前たちも\n',
            '遭遇していたか……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E6A')

    def _loc_2DCD(): pass

    label('loc_2DCD')

    ChrTalk(
        0x0101,
        (
            '<FIXME>#1002Fそれって、まさか……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '<FIXME>#1042Fうん、《裏の塔》が出現した\n',
            '影響かもしれない。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '<FIXME>《裏の塔》……\n',
            'あの時の異常事態のことか。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2E6A(): pass

    label('loc_2E6A')

    ChrTalk(
        0x00FE,
        (
            '<FIXME>……ともかく、俺の方では\n',
            'それっきり姿を見ていない。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '<FIXME>ただ……そこらの魔獣に比べて\n',
            'かなり強力だったことは確かだ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '<FIXME>用心するに\n',
            '越したことはないだろう。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '<FIXME>#1002Fう、うん……そうね。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '<FIXME>………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '<FIXME>ところで……\n',
            'お前たちはオーブメントを\n',
            '使っているように見えるが。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '<FIXME>どういうことか、\n',
            '良ければ教えてくれないか。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '<FIXME>#1000Fあ、うん、それは……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '<FIXME>#1040F説明させていただきます。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '<FIXME>エステルたちは『零力場発生器』のことと\n',
            '自分たちの当面の任務について説明した。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x00FE,
        (
            '<FIXME>……なるほど、\n',
            'そんなことになっていたのか。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '<FIXME>ふむ……そうだな。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.Item, ItemTable['驱动３']),
            (TxtCtl.SetColor, 0x0),
            'を受け取った。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    AddItem(ItemTable['驱动３'], 1)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0101,
        (
            '<FIXME>#1004Fえ……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '<FIXME>#1044Fスティングさん？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '<FIXME>オーブメントの使えない今、\n',
            'それは俺にとって無用の長物……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '<FIXME>だが、お前たちの任務には\n',
            'オーブメントが役に立つ……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '<FIXME>……だったら、\n',
            '導き出される答えは一つだ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '<FIXME>#1004Fあ……',
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
        'loc_32AC',
    )

    ChrTalk(
        0x0106,
        (
            '<FIXME>#051Fへっ、随分と\n',
            '気が利いているじゃねえか。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3326')

    def _loc_32AC(): pass

    label('loc_32AC')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_32F0',
    )

    ChrTalk(
        0x0103,
        (
            '<FIXME>#027Fふふ、随分と\n',
            '気が利いているわね。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3326')

    def _loc_32F0(): pass

    label('loc_32F0')

    ChrTalk(
        0x0102,
        (
            '<FIXME>#1040Fすみません、\n',
            'ありがとうございます。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3326(): pass

    label('loc_3326')

    ChrTalk(
        0x00FE,
        (
            '<FIXME>……礼には及ばん。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '<FIXME>お前たちは自分の責務を\n',
            '果たすことだけ考えろ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '<FIXME>#1006Fうん……！\n',
            'ありがとう、スティングさん。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0408, 1, 0x2041))
    EventEnd(0x00)
    OP_4B(0x00FE, 255)

    Jump('loc_34EF')

    def _loc_33C5(): pass

    label('loc_33C5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3479',
    )

    ChrTalk(
        0x00FE,
        (
            '<FIXME>お前たちは自分の責務を\n',
            '果たすことだけ考えろ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '<FIXME>各人が各人に\n',
            '出来ることを尽くす……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '<FIXME>そうすれば、この状況にも\n',
            '活路が見出せるはずだ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    Jump('loc_34EF')

    def _loc_3479(): pass

    label('loc_3479')

    ChrTalk(
        0x00FE,
        (
            '<FIXME>お前たちは自分の責務を\n',
            '果たすことだけ考えろ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '<FIXME>そうすれば、この状況にも\n',
            '活路が見出せるはずだ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_34EF(): pass

    label('loc_34EF')

    TalkEnd(0x0014)

    Return()

# id: 0x0010 offset: 0x34F3
@scena.Code('func_10_34F3')
def func_10_34F3():
    TalkBegin(0x0015)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_36E2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3694',
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3621',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，阿加特……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '刚刚正在给\n',
            '你的妹妹祈祷呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#050F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '真不好意思。\n',
            '总是让您陪我妹妹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哪里，没那回事。\n',
            '对我来说她是个很好的倾诉对象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且以前也总是\n',
            '拜托她各种事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '刚刚就在为村子的事\n',
            '祈祷呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近世间\n',
            '似乎总是发生奇怪的事件……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_368E')

    def _loc_3621(): pass

    label('loc_3621')

    ChrTalk(
        0x00FE,
        (
            '所以要到女神身边为大家\n',
            '祈愿呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '祈求她们保佑\n',
            '这拉文努村……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近世间\n',
            '似乎总是发生奇怪的事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_368E(): pass

    label('loc_368E')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    Jump('loc_36E2')

    def _loc_3694(): pass

    label('loc_3694')

    ChrTalk(
        0x00FE,
        (
            '所以要到女神身边为大家\n',
            '祈愿呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近世间\n',
            '似乎总是发生奇怪的事件呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_36E2(): pass

    label('loc_36E2')

    TalkEnd(0x0015)

    Return()

# id: 0x0011 offset: 0x36E6
@scena.Code('func_11_36E6')
def func_11_36E6():
    EventBegin(0x00)
    OP_DB()
    ClearScenaFlags(ScenaFlag(0x0380, 1, 0x1C01))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3701',
    )

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)
    FormationAddMember(ChrTable['提妲'], 0xF8, 0xFF)

    def _loc_3701(): pass

    label('loc_3701')

    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x00F9, 0x0080)
    ChrSetFlags(0x0106, 0x0080)
    ChrSetFlags(0x0107, 0x0080)
    ChrSetPos(0x0101, 33050, 8000, 37090, 0)
    CameraMove(20530, 440, 8360, 0)
    OP_67(0, 13770, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(326000, 0)
    OP_6E(335, 0)
    ChrSetFlags(0x000D, 0x0080)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_3777')
    def lambda_3777():
        CameraMove(21820, 440, 6800, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3777)

    OP_67(0, 7790, -10000, 7000)
    Fade(500)
    CameraMove(26270, 5270, 52540, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0009, 32950, 8000, 37000, 180)
    ChrSetPos(0x0106, 26650, 5360, 52720, 0)
    ChrSetPos(0x0107, 25890, 5210, 52420, 0)
    ChrClearFlags(0x0106, 0x0080)
    ChrClearFlags(0x0107, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetChipByIndex(0x0107, 17)
    ChrSetPos(0x000A, 32990, 8000, 35450, 0)
    ChrSetFlags(0x000A, 0x0002)
    ChrSetFlags(0x000A, 0x0040)
    ChrSetFlags(0x000A, 0x0004)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetChipByIndex(0x000A, 10)
    ChrSetSubChip(0x000A, 15)
    CreateThread(0x0106, 0x01, 0x00, func_15_5847)
    CreateThread(0x0107, 0x01, 0x00, func_16_5884)
    OP_6A(0x0017)
    CreateThread(0x0017, 0x02, 0x00, func_17_58C1)
    WaitForThreadExit(0x0107, 0x0001)
    ChrSetSubChip(0x0107, 0)
    OP_62(0x0106, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_6A(0x00FF)
    TerminateThread(0x0017, 0x02)
    OP_DC()

    ChrTalk(
        0x0107,
        (
            '#0070311254V#064F#5P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050311255V#052F#5P你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_38DE')
    def lambda_38DE():
        CameraMove(32800, 8000, 38500, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_38DE)

    @scena.Lambda('lambda_38F6')
    def lambda_38F6():
        OP_6C(145000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_38F6)

    Sleep(4000)

    ChrSetPos(0x0106, 33360, 8000, 49000, 180)
    ChrSetPos(0x0107, 32439, 8000, 49000, 180)

    @scena.Lambda('lambda_392D')
    def lambda_392D():
        ChrWalkTo(0x00FE, 33360, 8000, 39830, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_392D)

    Sleep(200)

    @scena.Lambda('lambda_394D')
    def lambda_394D():
        ChrWalkTo(0x00FE, 32439, 8000, 40030, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_394D)

    Sleep(2000)

    ChrTalk(
        0x0009,
        (
            '#0600311256V#163F#6P你是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0106, 400)
    WaitForThreadExit(0x0107, 0x0001)
    ChrSetSubChip(0x0107, 0)

    ChrTalk(
        0x0106,
        (
            '#0050311257V#051F#6P没想到你\n',
            '会在这种地方。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050311258V什么风把你吹来的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0600311259V#163F#2P没什么……只不过是一时兴起。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600311260V#165F来祭拜妹妹的吧？\n',
            '我就不打扰了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050311261V#551F#6P喂喂。\n',
            '我可没说你碍事啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050311262V#050F那花……是你献的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0600311263V#166F#2P……算是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600311264V早知道是这样\n',
            '就考虑用别的颜色了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050311265V#051F#6P虽然知道每年都有人\n',
            '来献上和我的一样的花……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050311266V却没想到是你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0600311267V#163F#2P这可怎么说呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600311268V我也上了年纪了。\n',
            '已经忘了为什么了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050311269V#051F#6P哼，就知道你会这样说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070311270V#061F#6P嘿嘿……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070311271V#560F请问，我也可以\n',
            '献花吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0600311272V#161F#2P噢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0107, 400)
    Sleep(400)

    ChrTalk(
        0x0106,
        (
            '#0050311273V#051F#5P啊啊，拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3C94')
    def lambda_3C94():
        CameraMove(33700, 8000, 36340, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3C94)

    CreateThread(0x0009, 0x01, 0x00, func_18_590E)

    @scena.Lambda('lambda_3CB3')
    def lambda_3CB3():
        ChrWalkTo(0x00FE, 32870, 8000, 36350, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_3CB3)

    Sleep(500)

    ChrSetDirection(0x0106, 180, 400)
    Sleep(500)

    @scena.Lambda('lambda_3CDF')
    def lambda_3CDF():
        ChrWalkTo(0x00FE, 33460, 8000, 37300, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_3CDF)

    WaitForThreadExit(0x0107, 0x0001)
    ChrSetSubChip(0x0107, 0)
    WaitForThreadExit(0x0106, 0x0001)
    Sleep(500)

    WaitForThreadExit(0x0101, 0x0001)
    Fade(500)
    ChrSetFlags(0x0107, 0x0002)
    ChrSetSubChip(0x0107, 0)
    ChrSetChipByIndex(0x0107, 10)
    OP_0D()
    OP_99(0x0107, 0x00, 0x02, 1500)
    ChrSetPos(0x000B, 32689, 8000, 35750, 0)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetFlags(0x000B, 0x0004)
    ChrSetFlags(0x000B, 0x0040)
    ChrSetFlags(0x000B, 0x0002)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetChipByIndex(0x000B, 10)
    ChrSetSubChip(0x000B, 15)
    OP_0D()
    Sleep(1000)

    Fade(500)
    ChrClearFlags(0x0107, 0x0002)
    ChrSetChipByIndex(0x0107, 65535)
    ChrSetSubChip(0x0107, 0)
    OP_0D()

    @scena.Lambda('lambda_3D80')
    def lambda_3D80():
        ChrMoveTo(0x00FE, 32670, 8000, 37300, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_3D80)

    WaitForThreadExit(0x0107, 0x0001)
    Sleep(500)

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '阿加特和提妲\n',
            '默默祈祷了片刻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    Sleep(500)

    ChrTalk(
        0x0106,
        (
            '#0050311274V#053F#6P呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0107, 400)
    Sleep(500)

    ChrTalk(
        0x0106,
        (
            '#0050311275V#050F#5P不好意思，提妲。\n',
            '让你特地陪我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0107, 90, 400)
    Sleep(500)

    ChrTalk(
        0x0107,
        (
            '#0070311276V#066F#4P不，我也想\n',
            '好好地和米夏\n',
            '打个招呼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070311277V谢谢，阿加特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050311278V#051F#5P喂喂。\n',
            '要道谢的是我吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050311279V还有，答应过等工作告一段落\n',
            '之后让你见见她的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070311280V#067F#4P嘿嘿……是呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0600311281V#163F#5P呵呵……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600311282V#165F龙似乎也说过\n',
            '你似乎变了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600311283V给人的感觉\n',
            '变得沉稳了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0009, 400)
    Sleep(500)

    ChrTalk(
        0x0106,
        (
            '#0050311284V#551F#6P别说了，我还不够成熟。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050311285V#051F不过，我倒是感觉你\n',
            '好像也已有所觉悟了。\n',
            '从这次事件开始，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050311286V去改变自己以往的问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0600311287V#163F#5P唔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600311288V#160F……关于你所说过的，\n',
            '军队这个组织的弊病……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600311289V重新考虑过后，感觉\n',
            '你的话也有一番道理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050311290V#552F#6P那是……\n',
            '单纯的说气话罢了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050311291V我并不是说\n',
            '军队有什么错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0600311292V#163F#5P好了，听我说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600311293V#160F从这次事件也可以知道\n',
            '人和组织是不同的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600311294V军队的组织力派上了用场，\n',
            '但因为游击士的机动能力强，\n',
            '也将事件引导向好的结果。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600311295V无论缺了哪边，这次的事件\n',
            '都无法解决，你不这么认为吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050311296V#050F#6P……算是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050311297V有了你们提供的线索，\n',
            '才知道了龙的所在地。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0600311298V#166F#5P虽然不想借理查德说过的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600311299V导力器发明之后，\n',
            '物品和信息的流动，都变得更快更大了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600311300V为了更高效的处理物流和信息，\n',
            '组织就需要不断扩张，并且\n',
            '必须要做到细分化。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050311301V#555F#6P……军队就是个很好的例子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050311302V国境师团，飞行舰队，王室亲卫队，\n',
            '王都警备队，情报部……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0600310209V#163F#5P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600311304V#160F而这些，都可以说是\n',
            '对应时代潮流变化的产物。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600311305V虽说这变化中失去的东西\n',
            '也不在少数……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600311306V但后退是不可能了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050300233V#552F#6P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0009, 180, 400)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0600311308V#163F#5P所以你……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600311309V#165F你们游击士\n',
            '就用和我们不同的方法\n',
            '把该守护的东西守护好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050311310V#052F#6P……啊……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0600311311V#163F#5P为了彼此要守护的东西\n',
            '时而对立，时而配合……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600311312V以此彼此弥补，\n',
            '相互确认是否正确。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600311313V#160F你不认为这就是\n',
            '处理我们之间关系的正确做法吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050311314V#051F#6P……呵呵，没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050311315V嗯，今后我依然会\n',
            '毫不客气地批判你们的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050311316V做好心理准备哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0106, 400)

    ChrTalk(
        0x0009,
        (
            '#0600311317V#165F#5P呼，那也是我想说的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600311318V别再轻率行事，\n',
            '你要时时记在心上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070311319V#061F#4P嘻嘻……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0008, 32780, 8000, 45130, 180)
    ChrClearFlags(0x0008, 0x0080)

    NpcTalk(
        0x0008,
        '青年的声音',
        (
            '#0140311320V#2P呵呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '青年的声音',
        (
            '#0140311321V#2P不好意思，\n',
            '稍微打扰一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000003E8)
    OP_62(0x0106, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0107, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    Fade(500)
    CameraMove(32100, 8000, 40770, 0)
    OP_67(0, 5020, -10000, 0)
    CameraSetDistance(3680, 0)
    OP_6C(315000, 0)
    OP_6E(275, 0)

    @scena.Lambda('lambda_484E')
    def lambda_484E():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_484E')

    DispatchAsync2(0x0106, 0x0001, lambda_484E)

    Sleep(50)

    @scena.Lambda('lambda_4864')
    def lambda_4864():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_4864')

    DispatchAsync2(0x0009, 0x0001, lambda_4864)

    Sleep(50)

    @scena.Lambda('lambda_487A')
    def lambda_487A():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_487A')

    DispatchAsync2(0x0107, 0x0001, lambda_487A)

    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0106,
        (
            '#0050311322V#054F#6P#3S！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070311323V#065F#6P啊啊啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0600311324V#160F#6P你是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    PlayBGM(114)
    Sleep(800)

    ChrTalk(
        0x0008,
        (
            '#0140311325V#124F#2P和将军阁下是初次见面吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140311326V#120F我是『噬身之蛇』的执行者─\n',
            '莱恩哈特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140311327V以后请记住我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#0600311328V#161F#6P#3S什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(213, 0x00, 0x64)
    ChrSetSubChip(0x0106, 0)
    ChrSetChipByIndex(0x0106, 8)
    PlaySE(571, 0x00, 0x64)

    @scena.Lambda('lambda_49E1')
    def lambda_49E1():
        ChrJumpTo(0x00FE, 32920, 8000, 38180, 200, 3000)

        ExitThread()

    DispatchAsync(0x0106, 0x0002, lambda_49E1)

    Sleep(100)

    OP_62(0x0107, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_4A16')
    def lambda_4A16():
        ChrMoveToRelativeAsync(0x00FE, -200, 0, -200, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0002, lambda_4A16)

    WaitForThreadExit(0x0106, 0x0002)
    ChrSetSubChip(0x0106, 0)
    ChrSetChipByIndex(0x0106, 7)
    Sleep(500)

    ChrTalk(
        0x0106,
        (
            '#0050311329V#057F#6P……你小子……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050311330V打算干什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140311331V#121F#2P这里是死者长眠之地。\n',
            '只可能会来做一件事吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140311332V倒是你，打算在这里\n',
            '继续前几天的决斗吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050311333V#555F#6P呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070311334V#063F#6P阿加特哥哥……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050311335V#053F#6P……知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetSubChip(0x0106, 0)
    ChrSetChipByIndex(0x0106, 65535)
    OP_0D()
    Sleep(1000)

    @scena.Lambda('lambda_4B90')
    def lambda_4B90():
        ChrMoveTo(0x00FE, 33200, 8000, 36360, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_4B90)

    Sleep(1500)

    @scena.Lambda('lambda_4BB0')
    def lambda_4BB0():
        ChrMoveToRelativeAsync(0x00FE, -1200, 0, 0, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0002, lambda_4BB0)

    Sleep(200)

    @scena.Lambda('lambda_4BD0')
    def lambda_4BD0():
        ChrMoveToRelativeAsync(0x00FE, -1100, 0, 0, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0002, lambda_4BD0)

    Sleep(500)

    Fade(500)
    CameraMove(33220, 8000, 35580, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(145000, 0)
    OP_6E(262, 0)
    WaitForThreadExit(0x0008, 0x0001)
    Sleep(500)

    Fade(500)
    ChrSetFlags(0x0008, 0x0002)
    ChrSetChipByIndex(0x0008, 11)
    ChrSetSubChip(0x0008, 0)
    OP_0D()
    OP_99(0x0008, 0x00, 0x02, 1500)
    ChrSetPos(0x000C, 33290, 8000, 35750, 0)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetFlags(0x000C, 0x0040)
    ChrSetFlags(0x000C, 0x0002)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetChipByIndex(0x000C, 10)
    ChrSetSubChip(0x000C, 15)
    OP_0D()
    Sleep(500)

    Fade(500)
    ChrClearFlags(0x0008, 0x0002)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 18)
    OP_0D()

    @scena.Lambda('lambda_4CA4')
    def lambda_4CA4():
        ChrMoveTo(0x00FE, 33230, 8000, 36900, 1300, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_4CA4)

    WaitForThreadExit(0x0008, 0x0001)
    Sleep(500)

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '莱维静静的祈祷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0140311336V#124F#6P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0600311337V#160F#5P莱恩哈特……\n',
            '就是『剑帝』莱维吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600311338V我也同样不想打扰\n',
            '死者的长眠……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600311339V不过，就问一个问题行吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140311340V#124F#6P请便……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0600311341V#163F#5P这次事件中，\n',
            '你似乎为了不造成过大伤害\n',
            '而尽力控制住了龙的失控。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600311342V并且现在，也为了悼念死者\n',
            '而来此祈祷……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600311343V#160F但为什么你又\n',
            '要招来破坏和混沌？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600311344V是有什么……\n',
            '无法公开的内情吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140311345V#124F#6P……呵………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140311346V#121F控制龙的失控\n',
            '是为了正确进行实验。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140311347V除此以外别无他意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0600311348V#160F#5P但是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140311349V#124F#6P……我只是按照给我的命令，\n',
            '作为『结社』的部下来行动。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140311350V并不为任何人的意志所左右。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140311351V#123F别把我和将『哈梅尔』这个名字忘记的你们\n',
            '混为一谈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#0600311352V#161F#5P#4S！！！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050311353V#052F#6P你说『哈梅尔』？\n',
            '为什么知道那个名字……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1000)

    OP_63(0x0008)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0140311354V#125F#5P好了……\n',
            '阿加特·科洛斯纳。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140311355V#122F就算有坚定的意志，\n',
            '但没有相应的实力就毫无意义。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140311356V下次，可别以为只是碎了剑\n',
            '就可以了事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050311357V#051F#6P哼……正合我意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050311358V倒是你，别以为\n',
            '永远都能绰绰有余。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050311359V我很快就会赶上你，\n',
            '做好准备吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0140311360V#125F#5P呵……我期待着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 0, 400)
    Sleep(500)

    @scena.Lambda('lambda_5241')
    def lambda_5241():
        CameraMove(33420, 8000, 38810, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_5241)

    @scena.Lambda('lambda_5259')
    def lambda_5259():
        OP_67(0, 8500, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_5259)

    @scena.Lambda('lambda_5271')
    def lambda_5271():
        ChrWalkTo(0x00FE, 32350, 8000, 50540, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_5271)

    Sleep(1600)

    WaitForThreadExit(0x0008, 0x0001)
    WaitForThreadExit(0x0008, 0x0002)
    WaitForThreadExit(0x0008, 0x0003)
    ChrSetFlags(0x0008, 0x0080)
    TerminateThread(0x0106, 0x01)
    TerminateThread(0x0107, 0x01)
    TerminateThread(0x0009, 0x01)

    @scena.Lambda('lambda_52B1')
    def lambda_52B1():
        CameraMove(33100, 8000, 36700, 1500)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_52B1)

    WaitForThreadExit(0x0008, 0x0002)
    WaitForThreadExit(0x0008, 0x0003)
    Sleep(500)

    ChrTalk(
        0x0107,
        (
            '#0070311361V#063F#2P……那位哥哥。\n',
            '有着寂寞的眼神。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070311362V做祈祷的时候，一直……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050311363V#057F#5P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0009, 400)

    @scena.Lambda('lambda_536C')
    def lambda_536C():
        CameraMove(33800, 8000, 36470, 1000)

        ExitThread()

    DispatchAsync(0x0106, 0x0002, lambda_536C)

    ChrMoveTo(0x0106, 33080, 8000, 37240, 1500, 0x00)

    @scena.Lambda('lambda_5398')
    def lambda_5398():
        ChrTurnDirection(0x00FE, 0x0106, 400)
        Yield()

        Jump('lambda_5398')

    DispatchAsync2(0x0107, 0x0001, lambda_5398)

    WaitForThreadExit(0x0106, 0x0002)
    Sleep(500)

    ChrTalk(
        0x0106,
        (
            '#0050311364V#050F#6P喂……将军。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050311365V『哈梅尔』就是\n',
            '越过国境，\n',
            '帝国边界处的一座村子吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0009, 315, 400)

    ChrTalk(
        0x0009,
        (
            '#0600311366V#161F#5P你……\n',
            '知道那个名字吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050311367V#053F#6P爆发战争前、和拉文努村\n',
            '有过几次交流。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050311368V#555F现在似乎完全\n',
            '断绝了联系……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050311369V为什么会说到那个名字？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0600311370V#163F#5P…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600311371V#166F……关于这件事\n',
            '我是不能说的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600311372V因为关系到国家间的问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050311373V#052F#6P什么……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5592')
    def lambda_5592():
        CameraMove(34070, 8000, 34770, 2000)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_5592)

    @scena.Lambda('lambda_55AA')
    def lambda_55AA():
        OP_67(0, 6330, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0106, 0x0002, lambda_55AA)

    @scena.Lambda('lambda_55C2')
    def lambda_55C2():
        CameraSetDistance(2950, 2000)

        ExitThread()

    DispatchAsync(0x0106, 0x0003, lambda_55C2)

    @scena.Lambda('lambda_55D2')
    def lambda_55D2():
        OP_6C(157000, 2000)

        ExitThread()

    DispatchAsync(0x0107, 0x0002, lambda_55D2)

    Sleep(500)

    ChrSetDirection(0x0009, 180, 400)

    @scena.Lambda('lambda_55EE')
    def lambda_55EE():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_55EE)

    WaitForThreadExit(0x0106, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0600311374V#166F#6P只是，我就说一点。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600311375V如果，我的直觉\n',
            '是对的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600311376V#163F……那个叫莱维的男子、\n',
            '肯定见过相当恐怖的地狱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(1000)

    OP_AD('ED6_DT24/C_VIS155._CH', 0x0000, 0x0000, 0x00000064)
    Sleep(4000)

    OP_56(0x02)
    SetScenaFlags(ScenaFlag(0x0350, 2, 0x1A82))

    ExecExpressionWithVar(
        0x31,
        (
            (Expr.PushLong, 0x127),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(100000, -100000, 100000, 0)
    FadeIn(0, 0)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    UnlockAchievement(0x12, 0x0000, 0x00)

    Menu(
        0,
        240,
        180,
        0,
        (
            TXT(0x00, '【保存进度】\n'),
            TXT(0x01, '【进入下一章】\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5728',
    )

    ShowSaveMenu()

    def _loc_5728(): pass

    label('loc_5728')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_AE(0x000000C8)
    Sleep(2000)

    OP_20(0x00000BB8)
    OP_21()
    ClearScenaFlags(ScenaFlag(0x0350, 2, 0x1A82))

    ExecExpressionWithVar(
        0x04,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/E0101._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0012 offset: 0x5764
@scena.Code('func_12_5764')
def func_12_5764():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_57B0',
    )

    ChrWalkTo(0x00FE, 27390, -4000, 9350, 1200, 0x00)
    ChrSetDirection(0x00FE, 45, 400)
    Sleep(800)

    ChrWalkTo(0x00FE, 24320, -4000, 6250, 1200, 0x00)
    ChrSetDirection(0x00FE, 180, 400)
    Sleep(800)

    Jump('func_12_5764')

    def _loc_57B0(): pass

    label('loc_57B0')

    Return()

# id: 0x0013 offset: 0x57B1
@scena.Code('func_13_57B1')
def func_13_57B1():
    Sleep(500)

    def _loc_57B6(): pass

    label('loc_57B6')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5802',
    )

    ChrWalkTo(0x00FE, 13560, -4000, 11950, 1500, 0x00)
    ChrSetDirection(0x00FE, 270, 400)
    Sleep(1000)

    ChrWalkTo(0x00FE, 13270, -4000, 16810, 1500, 0x00)
    ChrSetDirection(0x00FE, 270, 400)
    Sleep(1000)

    Jump('loc_57B6')

    def _loc_5802(): pass

    label('loc_5802')

    Return()

# id: 0x0014 offset: 0x5803
@scena.Code('func_14_5803')
def func_14_5803():
    Sleep(250)

    def _loc_5808(): pass

    label('loc_5808')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5846',
    )

    ChrWalkTo(0x00FE, 21460, -4000, 9110, 1400, 0x00)
    Sleep(900)

    ChrWalkTo(0x00FE, 21710, -4000, 13730, 1400, 0x00)
    Sleep(900)

    Jump('loc_5808')

    def _loc_5846(): pass

    label('loc_5846')

    Return()

# id: 0x0015 offset: 0x5847
@scena.Code('func_15_5847')
def func_15_5847():
    ChrWalkTo(0x00FE, 26650, 8000, 58630, 2000, 0x00)
    ChrWalkTo(0x00FE, 32430, 8000, 58630, 2000, 0x00)
    ChrWalkTo(0x00FE, 32430, 8000, 54140, 2000, 0x00)

    Return()

# id: 0x0016 offset: 0x5884
@scena.Code('func_16_5884')
def func_16_5884():
    ChrWalkTo(0x00FE, 25890, 8000, 58830, 2000, 0x00)
    ChrWalkTo(0x00FE, 31370, 8000, 58830, 2000, 0x00)
    ChrWalkTo(0x00FE, 31370, 8000, 54140, 2000, 0x00)

    Return()

# id: 0x0017 offset: 0x58C1
@scena.Code('func_17_58C1')
def func_17_58C1():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_590D',
    )

    ExecExpressionWithValue(
        0x0017,
        0x01,
        (
            (Expr.GetChrWork, 0x106, 0x1),
            (Expr.GetChrWork, 0x107, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0017,
        0x02,
        (
            (Expr.GetChrWork, 0x106, 0x2),
            (Expr.GetChrWork, 0x107, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0017,
        0x03,
        (
            (Expr.GetChrWork, 0x106, 0x3),
            (Expr.GetChrWork, 0x107, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Yield()

    Jump('func_17_58C1')

    def _loc_590D(): pass

    label('loc_590D')

    Return()

# id: 0x0018 offset: 0x590E
@scena.Code('func_18_590E')
def func_18_590E():
    ChrWalkTo(0x00FE, 34400, 8000, 36190, 2000, 0x00)
    ChrSetDirection(0x00FE, 315, 400)

    Return()

# id: 0x0019 offset: 0x592A
@scena.Code('func_19_592A')
def func_19_592A():
    MapClearFlags(0x02000000)

    Return()

# id: 0x001A offset: 0x5930
@scena.Code('func_1A_5930')
def func_1A_5930():
    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0011860001V#1001F这里好像可以钓上什么来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5968')
    def lambda_5968():
        CameraMove(35190, -3850, 5430, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_5968)

    @scena.Lambda('lambda_5980')
    def lambda_5980():
        CameraSetDistance(2800, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_5980)

    @scena.Lambda('lambda_5990')
    def lambda_5990():
        OP_6C(225000, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_5990)

    Sleep(1000)

    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '钓鱼吗？',
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
            TXT(0x00, '钓鱼\n'),
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
    WaitForThreadExit(0x0000, 0x0001)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5A17',
    )

    OP_C0(0x0E, 0x0000000A, 0x00008976, 0xFFFFF0F6, 0x000021D4, 0x000000B4, 0x000088C2, 0xFFFFEF98, 0x00001446)
    OP_0D()
    EventEnd(0x01)

    Jump('loc_5A26')

    def _loc_5A17(): pass

    label('loc_5A17')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5A26',
    )

    EventEnd(0x01)

    def _loc_5A26(): pass

    label('loc_5A26')

    Return()

# id: 0x001B offset: 0x5A27
@scena.Code('func_1B_5A27')
def func_1B_5A27():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '七耀历１１９２年\n',
            '由于战火而失去的\n',
            '６个善良的灵魂，长眠与此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '雷夫、阿贝尔、尼高尔、\n',
            '维姆、依蕾娜、米夏。\n',
            '愿你们在女神的怀抱中得到安宁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x001C offset: 0x5AF3
@scena.Code('func_1C_5AF3')
def func_1C_5AF3():
    OP_13(0x002E)

    Return()

# id: 0x001D offset: 0x5AF7
@scena.Code('func_1D_5AF7')
def func_1D_5AF7():
    OP_13(0x002D)

    Return()

# id: 0x001E offset: 0x5AFB
@scena.Code('func_1E_5AFB')
def func_1E_5AFB():
    OP_13(0x002F)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

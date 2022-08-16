import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
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
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/T1101._SN', 'ED6_DT01/T1101_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x000088B8,
            dword_04        = 0x00000000,
            dword_08        = 0x00003E80,
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
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01160._CH', 'ED6_DT07/CH01160P._CP'),
        ('ED6_DT07/CH01170._CH', 'ED6_DT07/CH01170P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT07/CH01100._CH', 'ED6_DT07/CH01100P._CP'),
        ('ED6_DT07/CH02360._CH', 'ED6_DT07/CH02360P._CP'),
        ('ED6_DT07/CH02060._CH', 'ED6_DT07/CH02060P._CP'),
        ('ED6_DT07/CH02070._CH', 'ED6_DT07/CH02070P._CP'),
        ('ED6_DT07/CH02370._CH', 'ED6_DT07/CH02370P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01053._CH', 'ED6_DT07/CH01053P._CP'),
    ]

# id: 0x10001 offset: 0x112
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '罗卡斯',
            x                   = 64280,
            z                   = 0,
            y                   = 52300,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '爱蕾吉娅',
            x                   = 63060,
            z                   = 0,
            y                   = 49000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '哈里',
            x                   = 36520,
            z                   = 0,
            y                   = 52210,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '米娜',
            x                   = 36520,
            z                   = 0,
            y                   = 51220,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '雅哈多老人',
            x                   = 48310,
            z                   = 0,
            y                   = 46460,
            direction           = 262,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '马尔科',
            x                   = 66100,
            z                   = 0,
            y                   = 62200,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '雷塔',
            x                   = 67500,
            z                   = 0,
            y                   = 52540,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '法娜',
            x                   = 69170,
            z                   = 0,
            y                   = 52540,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x01D5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '梅贝尔市长',
            x                   = -620,
            z                   = -1000,
            y                   = -3500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '奈尔',
            x                   = -620,
            z                   = -1000,
            y                   = -3500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '朵洛希',
            x                   = -620,
            z                   = -1000,
            y                   = -3500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '莉拉',
            x                   = -620,
            z                   = -1000,
            y                   = -3500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '哈尔德',
            x                   = 23100,
            z                   = 0,
            y                   = 47200,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0001,
            talkScenaIndex      = 0x0000,
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
            x           = 17000,
            y           = -1000,
            z           = 50100,
            range       = 18000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00009D6C,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000011,
        ),
        ScenaEventData(
            x           = 27800,
            y           = -1000,
            z           = 57900,
            range       = 2000,
            dword_10    = 0x00002710,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000016,
        ),
        ScenaEventData(
            x           = 25200,
            y           = 0,
            z           = 57940,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000001A,
        ),
        ScenaEventData(
            x           = 18880,
            y           = 0,
            z           = 76030,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000001B,
        ),
        ScenaEventData(
            x           = 36200,
            y           = 0,
            z           = 79200,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000001C,
        ),
        ScenaEventData(
            x           = 59000,
            y           = 0,
            z           = 79200,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000001D,
        ),
        ScenaEventData(
            x           = 38540,
            y           = 0,
            z           = 59990,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000001E,
        ),
        ScenaEventData(
            x           = 48040,
            y           = 100,
            z           = 69500,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000001E,
        ),
        ScenaEventData(
            x           = 57480,
            y           = 0,
            z           = 60010,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000001E,
        ),
        ScenaEventData(
            x           = 48010,
            y           = 0,
            z           = 50550,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000001E,
        ),
        ScenaEventData(
            x           = 67340,
            y           = -500,
            z           = 73070,
            range       = 1500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000001F,
        ),
        ScenaEventData(
            x           = 72240,
            y           = 0,
            z           = 44910,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000020,
        ),
        ScenaEventData(
            x           = 47960,
            y           = 0,
            z           = 85570,
            range       = 1000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000021,
        ),
    )

# id: 0x10004 offset: 0x4D2
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x4D2
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_4E6',
    )

    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)

    Jump('loc_597')

    def _loc_4E6(): pass

    label('loc_4E6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_4FA',
    )

    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)

    Jump('loc_597')

    def _loc_4FA(): pass

    label('loc_4FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_51C',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0010, 0x01, 0x0002)"),
            (Expr.Eval, "OP_29(0x0010, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_519',
    )

    ChrClearFlags(0x0014, 0x0080)

    def _loc_519(): pass

    label('loc_519')

    Jump('loc_597')

    def _loc_51C(): pass

    label('loc_51C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 7, 0x317)),
            Expr.Return,
        ),
        'loc_53C',
    )

    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 66400, 0, 54570, 270)

    Jump('loc_597')

    def _loc_53C(): pass

    label('loc_53C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_546',
    )

    Jump('loc_597')

    def _loc_546(): pass

    label('loc_546')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_550',
    )

    Jump('loc_597')

    def _loc_550(): pass

    label('loc_550')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 1, 0x309)),
            Expr.Return,
        ),
        'loc_55A',
    )

    Jump('loc_597')

    def _loc_55A(): pass

    label('loc_55A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_597',
    )

    ChrClearFlags(0x0010, 0x0080)
    ChrSetFlags(0x0010, 0x0010)
    ChrSetPos(0x0010, 69070, 0, 48400, 0)
    ChrClearFlags(0x0013, 0x0080)
    ChrSetFlags(0x0013, 0x0010)
    ChrSetPos(0x0013, 69060, 0, 49440, 180)

    def _loc_597(): pass

    label('loc_597')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_5A5',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_14_382A)

    def _loc_5A5(): pass

    label('loc_5A5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_5B3',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, func_17_519A)

    def _loc_5B3(): pass

    label('loc_5B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 4, 0x3FC)),
            Expr.Return,
        ),
        'loc_5C1',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    Event(0, func_19_5E5F)

    def _loc_5C1(): pass

    label('loc_5C1')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000073, 'loc_5D5'),
        (0x0000006E, 'loc_5FA'),
        (0x00000074, 'loc_611'),
        (-1, 'loc_637'),
    )

    def _loc_5D5(): pass

    label('loc_5D5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 7, 0x307)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5E4',
    )

    SetScenaFlags(ScenaFlag(0x0060, 7, 0x307))
    Event(0, func_13_33D8)

    def _loc_5E4(): pass

    label('loc_5E4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 3, 0x313)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5F7',
    )

    SetScenaFlags(ScenaFlag(0x0062, 3, 0x313))
    Event(0, func_15_3B4D)

    def _loc_5F7(): pass

    label('loc_5F7')

    Jump('loc_637')

    def _loc_5FA(): pass

    label('loc_5FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 7, 0x317)),
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 4, 0x314)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 5, 0x315)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_611',
    )

    SetScenaFlags(ScenaFlag(0x0062, 5, 0x315))
    Event(0, func_18_58DD)

    def _loc_611(): pass

    label('loc_611')

    If(
        (
            (Expr.Eval, "OP_29(0x0010, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x0010, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0010, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_637',
    )

    OP_28(0x0010, 0x03, 0x08)
    FormationDelMember(0x34, 0xFF)
    Event(1, 0x0002)

    def _loc_637(): pass

    label('loc_637')

    Return()

# id: 0x0001 offset: 0x638
@scena.Code('func_01_638')
def func_01_638():
    OP_16(0x02, 4000, -80000, -68000, 196673)

    If(
        (
            (Expr.Eval, "OP_42(0x0033)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_65D',
    )

    OP_1B(0x0F, 0x00, 0x0010)

    def _loc_65D(): pass

    label('loc_65D')

    Return()

# id: 0x0002 offset: 0x65E
@scena.Code('func_02_65E')
def func_02_65E():
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
        'loc_683',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_7C5')

    def _loc_683(): pass

    label('loc_683')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_69C',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_7C5')

    def _loc_69C(): pass

    label('loc_69C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6B5',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_7C5')

    def _loc_6B5(): pass

    label('loc_6B5')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6CE',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_7C5')

    def _loc_6CE(): pass

    label('loc_6CE')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6E7',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_7C5')

    def _loc_6E7(): pass

    label('loc_6E7')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_700',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_7C5')

    def _loc_700(): pass

    label('loc_700')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_719',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_7C5')

    def _loc_719(): pass

    label('loc_719')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_732',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_7C5')

    def _loc_732(): pass

    label('loc_732')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_74B',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_7C5')

    def _loc_74B(): pass

    label('loc_74B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_764',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_7C5')

    def _loc_764(): pass

    label('loc_764')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_77D',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_7C5')

    def _loc_77D(): pass

    label('loc_77D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_796',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_7C5')

    def _loc_796(): pass

    label('loc_796')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7AF',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_7C5')

    def _loc_7AF(): pass

    label('loc_7AF')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7C5',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_7C5(): pass

    label('loc_7C5')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_7DA',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_7C5')

    def _loc_7DA(): pass

    label('loc_7DA')

    Return()

# id: 0x0003 offset: 0x7DB
@scena.Code('func_03_7DB')
def func_03_7DB():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_8D7',
    )

    ChrWalkTo(0x00FE, 64280, 0, 45050, 3000, 0x00)
    ChrWalkTo(0x00FE, 63220, 0, 44300, 3000, 0x00)
    ChrWalkTo(0x00FE, 61790, 0, 43420, 3000, 0x00)
    ChrWalkTo(0x00FE, 34300, 0, 43420, 3000, 0x00)
    ChrWalkTo(0x00FE, 32479, 0, 45370, 3000, 0x00)
    ChrWalkTo(0x00FE, 31720, 0, 47690, 3000, 0x00)
    ChrWalkTo(0x00FE, 31400, 0, 74910, 3000, 0x00)
    ChrWalkTo(0x00FE, 32430, 0, 75990, 3000, 0x00)
    ChrWalkTo(0x00FE, 33920, 0, 76660, 3000, 0x00)
    ChrWalkTo(0x00FE, 62870, 0, 76660, 3000, 0x00)
    ChrWalkTo(0x00FE, 63950, 0, 75520, 3000, 0x00)
    ChrWalkTo(0x00FE, 64280, 0, 74560, 3000, 0x00)

    Jump('func_03_7DB')

    def _loc_8D7(): pass

    label('loc_8D7')

    Return()

# id: 0x0004 offset: 0x8D8
@scena.Code('func_04_8D8')
def func_04_8D8():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_9D4',
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

    Jump('func_04_8D8')

    def _loc_9D4(): pass

    label('loc_9D4')

    Return()

# id: 0x0005 offset: 0x9D5
@scena.Code('func_05_9D5')
def func_05_9D5():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_AD1',
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

    Jump('func_05_9D5')

    def _loc_AD1(): pass

    label('loc_AD1')

    Return()

# id: 0x0006 offset: 0xAD2
@scena.Code('func_06_AD2')
def func_06_AD2():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_B7E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B61',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '事情解决了，\n',
            '好久没有这么愉快地\n',
            '在街上散步了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真想和对面走过来的人们\n',
            '打个招呼啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '柏斯万岁，小姐万岁！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B7B')

    def _loc_B61(): pass

    label('loc_B61')

    ChrTalk(
        0x00FE,
        (
            '柏斯万岁，小姐万岁！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B7B(): pass

    label('loc_B7B')

    Jump('loc_FB7')

    def _loc_B7E(): pass

    label('loc_B7E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_C60',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C09',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '听说飞艇的失踪\n',
            '都是空贼团干的好事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且他们竟然向王家\n',
            '要求天价的赎金……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎么会有如此无法无天的家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C5D')

    def _loc_C09(): pass

    label('loc_C09')

    ChrTalk(
        0x00FE,
        (
            '听说飞艇的失踪\n',
            '都是空贼团干的好事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且他们竟然向王家\n',
            '要求天价的赎金……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C5D(): pass

    label('loc_C5D')

    Jump('loc_FB7')

    def _loc_C60(): pass

    label('loc_C60')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_CE0',
    )

    ChrTalk(
        0x00FE,
        (
            '强盗案件也好，定期船失踪事件也好，\n',
            '希望都能够尽快得到解决。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近这几个月，\n',
            '总是发生一些让人心神不定的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FB7')

    def _loc_CE0(): pass

    label('loc_CE0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_D40',
    )

    ChrTalk(
        0x00FE,
        (
            '本来想在超市\n',
            '租一个摊位的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '却被告知现在暂停申请。\n',
            '最近还真是多事之秋啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FB7')

    def _loc_D40(): pass

    label('loc_D40')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_D9E',
    )

    ChrTalk(
        0x00FE,
        (
            '柏斯超市\n',
            '对于商人来说像登龙门一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果我要做生意，\n',
            '还是要从超市开始啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FB7')

    def _loc_D9E(): pass

    label('loc_D9E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_EB6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E8E',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '这个城市里\n',
            '有着各种各样的商人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '首先是在这个超市\n',
            '拥有摊位的各种商贩……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '然后就是在南街区自己\n',
            '搭建店铺的零售商……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还有像特里诺家和\n',
            '博尔德家那样的贸易商……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对了对了，\n',
            '本市的市长也是一位大商人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EB3')

    def _loc_E8E(): pass

    label('loc_E8E')

    ChrTalk(
        0x00FE,
        (
            '这个城市里\n',
            '有着各种各样的商人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EB3(): pass

    label('loc_EB3')

    Jump('loc_FB7')

    def _loc_EB6(): pass

    label('loc_EB6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_FB7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F5B',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '欢迎来到商业都市柏斯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里是利贝尔王国\n',
            '商业最繁荣的城市。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也是各地梦想成为\n',
            '成功商人的奋斗者的云集之地。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也是其中之一啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FB7')

    def _loc_F5B(): pass

    label('loc_F5B')

    ChrTalk(
        0x00FE,
        (
            '这里是利贝尔王国\n',
            '商业最繁荣的城市。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也是各地梦想成为\n',
            '成功商人的奋斗者的云集之地。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FB7(): pass

    label('loc_FB7')

    TalkEnd(0x0008)

    Return()

# id: 0x0007 offset: 0xFBB
@scena.Code('func_07_FBB')
def func_07_FBB():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_100A',
    )

    ChrTalk(
        0x00FE,
        (
            '所有的商店\n',
            '终于都能够进货了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样就可以\n',
            '尽情地购物了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1254')

    def _loc_100A(): pass

    label('loc_100A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_106A',
    )

    ChrTalk(
        0x00FE,
        (
            '最近都没有\n',
            '什么可以让人振奋的话题呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '去买买东西，\n',
            '也许心情就能放松很多吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1254')

    def _loc_106A(): pass

    label('loc_106A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_10DD',
    )

    ChrTalk(
        0x00FE,
        (
            '南街区都是士兵，\n',
            '现在可不是买东西的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我本来想去见识一下\n',
            '导力器工艺的，\n',
            '不过还是去超市吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1254')

    def _loc_10DD(): pass

    label('loc_10DD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_116D',
    )

    ChrTalk(
        0x00FE,
        (
            '最近，\n',
            '所有商店的商品种类都变少了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我想，\n',
            '大概是由于定期船\n',
            '不能前来运货的原因吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '想买的东西却买不到，\n',
            '真是无聊啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1254')

    def _loc_116D(): pass

    label('loc_116D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_11B8',
    )

    ChrTalk(
        0x00FE,
        (
            '今天想去买双鞋\n',
            '来搭配我昨天买的衣服……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到店里瞧瞧去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1254')

    def _loc_11B8(): pass

    label('loc_11B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_1201',
    )

    ChrTalk(
        0x00FE,
        (
            '今天要去买新衣服。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果能够找到\n',
            '我喜欢的样式就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1254')

    def _loc_1201(): pass

    label('loc_1201')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_1254',
    )

    ChrTalk(
        0x00FE,
        (
            '嘿嘿嘿，\n',
            '今天要买些什么好呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果能够找到\n',
            '我喜欢的衣服就好了㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1254(): pass

    label('loc_1254')

    TalkEnd(0x0009)

    Return()

# id: 0x0008 offset: 0x1258
@scena.Code('func_08_1258')
def func_08_1258():
    TalkBegin(0x000A)
    OP_4A(0x000B, 255)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_141E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1401',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    ChrTurnDirection(0x000A, 0x000B, 0)

    ChrTalk(
        0x000A,
        (
            '我说，米娜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x000A, 0)

    ChrTalk(
        0x000B,
        (
            '什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我一定会努力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '……啊啊，是说想成为商人的事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '这样说也没错，不过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '什么啊，赶快说啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '嗯，那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我想成为米娜\n',
            '理想中的那个人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000B,
        (
            '………………………………\n',
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '那么我就满怀期待了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '啊，嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000B, 270, 0)

    Jump('loc_141B')

    def _loc_1401(): pass

    label('loc_1401')

    ChrTalk(
        0x000A,
        (
            '（好！一定要加油！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_141B(): pass

    label('loc_141B')

    Jump('loc_1B48')

    def _loc_141E(): pass

    label('loc_141E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_152E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1511',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    ChrTurnDirection(0x000A, 0x000B, 0)

    ChrTalk(
        0x000A,
        (
            '那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x000A, 0)

    ChrTalk(
        0x000B,
        (
            '什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '米娜没有想过\n',
            '将来要干什么事情吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '有啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '啊，什么什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '想听？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '想成为大富豪的妻子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000B, 270, 0)

    Jump('loc_152B')

    def _loc_1511(): pass

    label('loc_1511')

    ChrTalk(
        0x000A,
        (
            '…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_152B(): pass

    label('loc_152B')

    Jump('loc_1B48')

    def _loc_152E(): pass

    label('loc_152E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_16C4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_168C',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    ChrTurnDirection(0x000A, 0x000B, 0)

    ChrTalk(
        0x000A,
        (
            '那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x000A, 0)

    ChrTalk(
        0x000B,
        (
            '什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我还是想成为商人，\n',
            '然后开一家属于自己的店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '反正有目标\n',
            '就是一件好事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '你自己是不是该好好考虑一下\n',
            '怎么做才能成功呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '对、对啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '我也会在力所能及的范围里帮你的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '真的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '就这样。\n',
            '就在力所能及的范围里哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000B, 270, 0)

    Jump('loc_16C1')

    def _loc_168C(): pass

    label('loc_168C')

    ChrTalk(
        0x000A,
        (
            '……我觉得这是米娜\n',
            '第一次对我这么温柔地说话呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_16C1(): pass

    label('loc_16C1')

    Jump('loc_1B48')

    def _loc_16C4(): pass

    label('loc_16C4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_1825',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_17F8',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    ChrTurnDirection(0x000A, 0x000B, 0)

    ChrTalk(
        0x000A,
        (
            '我说，米娜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x000A, 0)

    ChrTalk(
        0x000B,
        (
            '什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '米娜你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '对我说话这么冷淡，\n',
            '是不是讨厌我啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '……如果讨厌的话，\n',
            '就不会跟你在一起了不是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '你在害羞什么啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '我也没说喜欢你啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '哈哈，是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000B, 270, 0)

    Jump('loc_1822')

    def _loc_17F8(): pass

    label('loc_17F8')

    ChrTalk(
        0x00FE,
        (
            '是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '原来两个都不是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1822(): pass

    label('loc_1822')

    Jump('loc_1B48')

    def _loc_1825(): pass

    label('loc_1825')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_197D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1936',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    ChrTurnDirection(0x000A, 0x000B, 0)

    ChrTalk(
        0x000A,
        (
            '哈啊……\n',
            '虽然我是想成为一个商人的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '但是我不擅长算术，\n',
            '我到底适不适合当商人呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x000A, 0)

    ChrTalk(
        0x000B,
        (
            '不知道……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '反正，从一开始就对自己这么没自信，\n',
            '那么以后做什么都不可能成功的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(700)

    ChrTalk(
        0x000A,
        (
            '…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000B, 270, 0)

    Jump('loc_197A')

    def _loc_1936(): pass

    label('loc_1936')

    ChrTurnDirection(0x0101, 0x000A, 0)
    ChrClearFlags(0x000A, 0x0010)
    ChrTurnDirection(0x000A, 0x0101, 0)

    ChrTalk(
        0x000A,
        (
            '我能哭一场吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F我、我觉得可以吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_197A(): pass

    label('loc_197A')

    Jump('loc_1B48')

    def _loc_197D(): pass

    label('loc_197D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_1A5C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A4B',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    ChrTurnDirection(0x000A, 0x000B, 0)

    ChrTalk(
        0x000A,
        (
            '嗯～想成为商人\n',
            '到底该怎么做才好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x000A, 0)

    ChrTalk(
        0x000B,
        (
            '不知道……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '对于在主日学校算术学得\n',
            '一塌糊涂的人是不可能的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(700)

    ChrTalk(
        0x000A,
        (
            '…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000B, 270, 0)

    Jump('loc_1A59')

    def _loc_1A4B(): pass

    label('loc_1A4B')

    ChrTalk(
        0x000A,
        (
            '呜呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A59(): pass

    label('loc_1A59')

    Jump('loc_1B48')

    def _loc_1A5C(): pass

    label('loc_1A5C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_1B48',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1B2E',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    ChrTurnDirection(0x000A, 0x000B, 0)

    ChrTalk(
        0x000A,
        (
            '我什么时候才能成为商人，\n',
            '住在大大的房子里呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x000A, 0)

    ChrTalk(
        0x000B,
        (
            '……真是幼稚啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '商人并不是都能\n',
            '住在大大的房子里啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(700)

    ChrTalk(
        0x000A,
        (
            '…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000B, 270, 0)

    Jump('loc_1B48')

    def _loc_1B2E(): pass

    label('loc_1B2E')

    ChrTalk(
        0x000A,
        (
            '（呜～是这样吗……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B48(): pass

    label('loc_1B48')

    OP_4B(0x000B, 255)
    TalkEnd(0x000A)

    Return()

# id: 0x0009 offset: 0x1B50
@scena.Code('func_09_1B50')
def func_09_1B50():
    TalkBegin(0x000B)
    OP_4A(0x000A, 255)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_1D2A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D05',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    ChrSetDirection(0x000B, 270, 0)
    ChrTurnDirection(0x000A, 0x000B, 0)

    ChrTalk(
        0x000A,
        (
            '我说，米娜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x000A, 0)

    ChrTalk(
        0x000B,
        (
            '什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我一定会努力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '……啊啊，是说想成为商人的事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '这样说也没错，不过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '什么啊，赶快说啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '嗯，那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我想成为米娜\n',
            '理想中的那个人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000B,
        (
            '………………………………\n',
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '那么我就满怀期待了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '啊，嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000A, 270, 0)
    ChrClearFlags(0x000B, 0x0010)

    Jump('loc_1D27')

    def _loc_1D05(): pass

    label('loc_1D05')

    ChrTalk(
        0x000B,
        (
            '不过，拥有梦想是人的自由嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D27(): pass

    label('loc_1D27')

    Jump('loc_2481')

    def _loc_1D2A(): pass

    label('loc_1D2A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_1E3F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1E24',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    ChrSetDirection(0x000B, 270, 0)
    ChrTurnDirection(0x000A, 0x000B, 0)

    ChrTalk(
        0x000A,
        (
            '那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x000A, 0)

    ChrTalk(
        0x000B,
        (
            '什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '米娜没有想过\n',
            '将来要干什么事情吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '有啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '啊，什么什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '想听？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '想成为大富豪的妻子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000A, 270, 0)

    Jump('loc_1E3C')

    def _loc_1E24(): pass

    label('loc_1E24')

    ChrTalk(
        0x000B,
        (
            '（前路漫漫啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E3C(): pass

    label('loc_1E3C')

    Jump('loc_2481')

    def _loc_1E3F(): pass

    label('loc_1E3F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_1FC3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1FA4',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    ChrSetDirection(0x000B, 270, 0)
    ChrTurnDirection(0x000A, 0x000B, 0)

    ChrTalk(
        0x000A,
        (
            '那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x000A, 0)

    ChrTalk(
        0x000B,
        (
            '什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我还是想成为商人，\n',
            '然后开一家属于自己的店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '反正有目标\n',
            '就是一件好事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '你自己是不是该好考虑一下\n',
            '好怎么做才能成功呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '对、对啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '我也会在力所能及的范围里帮你的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '真的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '就这样。\n',
            '就在力所能及的范围里哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000A, 270, 0)

    Jump('loc_1FC0')

    def _loc_1FA4(): pass

    label('loc_1FA4')

    ChrTalk(
        0x000B,
        (
            '真的花了很多工夫啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1FC0(): pass

    label('loc_1FC0')

    Jump('loc_2481')

    def _loc_1FC3(): pass

    label('loc_1FC3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_2111',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_20FE',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    ChrSetDirection(0x000B, 270, 0)
    ChrTurnDirection(0x000A, 0x000B, 0)

    ChrTalk(
        0x000A,
        (
            '我说，米娜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x000A, 0)

    ChrTalk(
        0x000B,
        (
            '什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '米娜你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '对我说话这么冷淡，\n',
            '是不是讨厌我啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '……如果讨厌的话，\n',
            '就不会跟你在一起了不是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '你在害羞什么啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '我也没说喜欢你啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '哈哈，是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000A, 270, 0)

    Jump('loc_210E')

    def _loc_20FE(): pass

    label('loc_20FE')

    ChrTalk(
        0x00FE,
        (
            '真是的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_210E(): pass

    label('loc_210E')

    Jump('loc_2481')

    def _loc_2111(): pass

    label('loc_2111')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_225B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2229',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    ChrSetDirection(0x000B, 270, 0)
    ChrTurnDirection(0x000A, 0x000B, 0)

    ChrTalk(
        0x000A,
        (
            '哈啊……\n',
            '虽然我是想成为一个商人的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '但是我不擅长算术，\n',
            '对我来说是不是不合适啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x000A, 0)

    ChrTalk(
        0x000B,
        (
            '不知道……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '反正，从一开始就对自己这么没自信，\n',
            '那么以后做什么都不可能成功的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x000A,
        (
            '…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000A, 270, 0)

    Jump('loc_2258')

    def _loc_2229(): pass

    label('loc_2229')

    ChrTalk(
        0x000B,
        (
            '真是的，\n',
            '哈里就像个不折不扣的大少爷啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2258(): pass

    label('loc_2258')

    Jump('loc_2481')

    def _loc_225B(): pass

    label('loc_225B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_2366',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2330',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    ChrSetDirection(0x000B, 270, 0)
    ChrTurnDirection(0x000A, 0x000B, 0)

    ChrTalk(
        0x000A,
        (
            '嗯～想成为商人\n',
            '到底该怎么做才好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x000A, 0)

    ChrTalk(
        0x000B,
        (
            '不知道……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '对于在主日学校算术学得\n',
            '一塌糊涂的人是不可能的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(700)

    ChrTalk(
        0x000A,
        (
            '…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000A, 270, 0)

    Jump('loc_2363')

    def _loc_2330(): pass

    label('loc_2330')

    ChrTalk(
        0x000B,
        (
            '不擅长和数字打交道的商人\n',
            '从来没有听说过呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2363(): pass

    label('loc_2363')

    Jump('loc_2481')

    def _loc_2366(): pass

    label('loc_2366')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_2481',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_243F',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    ChrSetDirection(0x000B, 270, 0)
    ChrTurnDirection(0x000A, 0x000B, 0)

    ChrTalk(
        0x000A,
        (
            '我什么时候才能成为商人，\n',
            '住在大大的房子里呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x000A, 0)

    ChrTalk(
        0x000B,
        (
            '……真是幼稚啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '商人并不是都能\n',
            '住在大大的房子里啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(700)

    ChrTalk(
        0x000A,
        (
            '…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000A, 270, 0)

    Jump('loc_2481')

    def _loc_243F(): pass

    label('loc_243F')

    ChrTalk(
        0x000B,
        (
            '现实并不像\n',
            '想象那样简单。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '这样教训他一下，\n',
            '也是为他好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2481(): pass

    label('loc_2481')

    OP_4B(0x000A, 255)
    TalkEnd(0x000B)

    Return()

# id: 0x000A offset: 0x2489
@scena.Code('func_0A_2489')
def func_0A_2489():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_258D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_252C',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '柏斯和卢安之间的古罗尼连峰\n',
            '是个很危险的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是由峭壁山岩林立的\n',
            '险峻的山峰连绵而成。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果没做好准备的话\n',
            '最好不要踏足那里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_258A')

    def _loc_252C(): pass

    label('loc_252C')

    ChrTalk(
        0x00FE,
        (
            '柏斯和卢安之间的古罗尼连峰\n',
            '是个很危险的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果没做好准备的话\n',
            '最好不要踏足那里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_258A(): pass

    label('loc_258A')

    Jump('loc_2B23')

    def _loc_258D(): pass

    label('loc_258D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_26B6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_263F',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '柏斯地区的东北方\n',
            '有一个被称为迷雾峡谷的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那里全年都\n',
            '掩盖在迷漫的大雾之中……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在那种地形错综复杂的山谷中，\n',
            '可以看到许多平时见不到的奇观。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26B3')

    def _loc_263F(): pass

    label('loc_263F')

    ChrTalk(
        0x00FE,
        (
            '柏斯地区的东北方\n',
            '有一个被称为迷雾峡谷的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在那种地形错综复杂的山谷中，\n',
            '可以看到许多平时见不到的奇观。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_26B3(): pass

    label('loc_26B3')

    Jump('loc_2B23')

    def _loc_26B6(): pass

    label('loc_26B6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_272C',
    )

    ChrTalk(
        0x00FE,
        (
            '没想到不是游击士，\n',
            '而是由边境军队亲自出马……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '强盗案件和定期船失踪\n',
            '是不是存在着什么内在的关系呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B23')

    def _loc_272C(): pass

    label('loc_272C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_281C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_27BD',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '拉文努村的水果真的是绝品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果说洛连特的蔬菜最好的话，\n',
            '那么水果就要数柏斯了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这也是我们\n',
            '柏斯市民的骄傲吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2819')

    def _loc_27BD(): pass

    label('loc_27BD')

    ChrTalk(
        0x00FE,
        (
            '如果说洛连特的蔬菜最好的话，\n',
            '那么水果就要数柏斯了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这也是我们\n',
            '柏斯市民的骄傲吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2819(): pass

    label('loc_2819')

    Jump('loc_2B23')

    def _loc_281C(): pass

    label('loc_281C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_2933',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_28C8',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '说起摩尔根将军，\n',
            '他可是在百日战争中非常活跃的人物啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈肯大门可谓是\n',
            '王国军事上最重要的地方……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他把边境军队\n',
            '驻扎在那里也是理所当然的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2930')

    def _loc_28C8(): pass

    label('loc_28C8')

    ChrTalk(
        0x00FE,
        (
            '说起摩尔根将军，\n',
            '他可是在百日战争中非常活跃的猛将啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他把边境军队\n',
            '驻扎在那里也是理所当然的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2930(): pass

    label('loc_2930')

    Jump('loc_2B23')

    def _loc_2933(): pass

    label('loc_2933')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 3, 0x30B)),
            Expr.Return,
        ),
        'loc_2A30',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_29CB',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '梅贝尔市长虽然年轻，\n',
            '不过作为商人却很有手段。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '政治手腕也很高明，\n',
            '真是我们市民的骄傲啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵呵，\n',
            '而且还是个美人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A2D')

    def _loc_29CB(): pass

    label('loc_29CB')

    ChrTalk(
        0x00FE,
        (
            '梅贝尔市长虽然年轻，\n',
            '不过作为商人却很有手段。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '政治手腕也很高明，\n',
            '真是我们市民的骄傲啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A2D(): pass

    label('loc_2A2D')

    Jump('loc_2B23')

    def _loc_2A30(): pass

    label('loc_2A30')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_2B23',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2AE7',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '柏斯可是一个不输给\n',
            '王都格兰赛尔的繁荣都市。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里与帝国保持着频繁的交易，\n',
            '而且物产也算丰富。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵呵，\n',
            '像柏斯超市那样的场所\n',
            '王都格兰赛尔可是没有哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B23')

    def _loc_2AE7(): pass

    label('loc_2AE7')

    ChrTalk(
        0x00FE,
        (
            '呵呵呵，\n',
            '像柏斯超市那样的场所\n',
            '王都格兰赛尔可是没有哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B23(): pass

    label('loc_2B23')

    TalkEnd(0x000C)

    Return()

# id: 0x000B offset: 0x2B27
@scena.Code('func_0B_2B27')
def func_0B_2B27():
    TalkBegin(0x000D)

    ChrTalk(
        0x00FE,
        (
            '呼……\n',
            '终于来到柏斯市了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，\n',
            '在哈肯门滞留了那么长时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '作为帝国商人的我\n',
            '怎么能够一直呆在那种地方呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000D)

    Return()

# id: 0x000C offset: 0x2BAD
@scena.Code('func_0C_2BAD')
def func_0C_2BAD():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_2C12',
    )

    ChrTalk(
        0x00FE,
        (
            '最近超市里卖的服装\n',
            '还真是合我心意啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '款式设计相当不错，\n',
            '到底是什么牌子的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2CDE')

    def _loc_2C12(): pass

    label('loc_2C12')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_2C6F',
    )

    ChrTalk(
        0x00FE,
        (
            '为了再去安特洛丝餐厅吃饭，\n',
            '如今要先找一份工作才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还是要去柏斯超市啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2CDE')

    def _loc_2C6F(): pass

    label('loc_2C6F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_2CDE',
    )

    ChrTalk(
        0x00FE,
        (
            '法娜说，\n',
            '想再去一次安特洛丝餐厅。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，\n',
            '现在可不是说去就去的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '必须先打工存钱才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2CDE(): pass

    label('loc_2CDE')

    TalkEnd(0x000E)

    Return()

# id: 0x000D offset: 0x2CE2
@scena.Code('func_0D_2CE2')
def func_0D_2CE2():
    TalkBegin(0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_2D68',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2D40',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '超市蛋糕店卖的蛋糕\n',
            '据说很好吃。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我要不要\n',
            '到那里去看一下呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D65')

    def _loc_2D40(): pass

    label('loc_2D40')

    ChrTalk(
        0x00FE,
        (
            '超市蛋糕店卖的蛋糕\n',
            '据说很好吃。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2D65(): pass

    label('loc_2D65')

    Jump('loc_2EB0')

    def _loc_2D68(): pass

    label('loc_2D68')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_2DCA',
    )

    ChrTalk(
        0x00FE,
        (
            '我也要去打工。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要一想到\n',
            '可以品尝美味的食物，\n',
            '不管多么辛苦我都会努力工作哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2EB0')

    def _loc_2DCA(): pass

    label('loc_2DCA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_2EB0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2E5E',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '吃下了美味的食物后，\n',
            '就会觉得非常幸福。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '传闻中的安特洛丝餐厅\n',
            '的饭菜非常可口。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我想每年去那里一次\n',
            '好好奢侈一回。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2EB0')

    def _loc_2E5E(): pass

    label('loc_2E5E')

    ChrTalk(
        0x00FE,
        (
            '传闻中的安特洛丝餐厅\n',
            '的饭菜非常可口。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我想每年去那里一次\n',
            '好好奢侈一回。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2EB0(): pass

    label('loc_2EB0')

    TalkEnd(0x000F)

    Return()

# id: 0x000E offset: 0x2EB4
@scena.Code('func_0E_2EB4')
def func_0E_2EB4():
    TalkBegin(0x0010)

    NpcTalk(
        0x0010,
        '年轻女性',
        (
            '#0360020382V莉拉，求求你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0010,
        '年轻女性',
        (
            '#0360020383V如果不是这种非常时刻，\n',
            '我也不会去看的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0010)

    Return()

# id: 0x000F offset: 0x2F28
@scena.Code('func_0F_2F28')
def func_0F_2F28():
    TalkBegin(0x0013)

    NpcTalk(
        0x0013,
        '女佣',
        (
            '#0370020384V大小姐，\n',
            '您又做这样的事情啦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0013)

    Return()

# id: 0x0010 offset: 0x2F65
@scena.Code('func_10_2F65')
def func_10_2F65():
    EventBegin(0x02)
    ChrTurnDirection(0x0134, 0x0000, 400)

    ChrTalk(
        0x0134,
        (
            '#0370020529V#620F各位要到哪里去呢？\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370020530V市长应该就在\n',
            '柏斯超市视察。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, -1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0011 offset: 0x2FDF
@scena.Code('func_11_2FDF')
def func_11_2FDF():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 5, 0x35D)),
            Expr.Return,
        ),
        'loc_2FED',
    )

    Call(0, 0x0012)

    Jump('loc_31C0')

    def _loc_2FED(): pass

    label('loc_2FED')

    If(
        (
            (Expr.Eval, "OP_42(0x0033)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3077',
    )

    EventBegin(0x02)
    ChrTurnDirection(0x0134, 0x0000, 400)

    ChrTalk(
        0x0134,
        (
            '#0370020531V#620F各位要到哪里去呢？\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370020532V市长应该就在\n',
            '柏斯超市视察。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_31C0')

    def _loc_3077(): pass

    label('loc_3077')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 0, 0x308)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_31C0',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_311D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_30A2',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_30A9')

    def _loc_30A2(): pass

    label('loc_30A2')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_30A9(): pass

    label('loc_30A9')

    ChrTalk(
        0x0103,
        (
            '#0030020533V#020F先回协会支部\n',
            '确认一下现在的状况吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020534V想去别的地方，\n',
            '等以后办完事情再去也不晚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_31A5')

    def _loc_311D(): pass

    label('loc_311D')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3133',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_313A')

    def _loc_3133(): pass

    label('loc_3133')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_313A(): pass

    label('loc_313A')

    ChrTalk(
        0x0103,
        (
            '#0030020535V#020F先回协会支部\n',
            '确认一下现在的状况吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020536V柏斯支部在北街区。\n',
            '就在东口的附近。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_31A5(): pass

    label('loc_31A5')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_31C0(): pass

    label('loc_31C0')

    Return()

# id: 0x0012 offset: 0x31C1
@scena.Code('func_12_31C1')
def func_12_31C1():
    If(
        (
            (Expr.Eval, "OP_29(0x000D, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x000D, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 5, 0x35D)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_33D7',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_3228',
    )

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020150761V#010F出发之前，\n',
            '还是把教区长的信送到教会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_33BC')

    def _loc_3228(): pass

    label('loc_3228')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3302',
    )

    Sleep(100)

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x0102,
        (
            '#0020150714V#014F等一下，艾丝蒂尔，听我说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150763V迪拜恩教区长让我们送的信\n',
            '还没有送到呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010150764V#008F啊……差点忘了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150765V#010F出发之前，去教会一趟吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_33BC')

    def _loc_3302(): pass

    label('loc_3302')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020150766V#014F啊，说起来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020150763V迪拜恩教区长让我们送的信\n',
            '还没有送到呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150764V#008F啊……差点忘了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020150765V#010F出发之前，去教会一趟吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_33BC(): pass

    label('loc_33BC')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_33D7(): pass

    label('loc_33D7')

    Return()

# id: 0x0013 offset: 0x33D8
@scena.Code('func_13_33D8')
def func_13_33D8():
    EventBegin(0x00)
    MapClearFlags(0x00000001)
    CameraMove(48080, 5850, 59960, 0)
    OP_6C(225000, 0)
    OP_67(0, 5395, -10000, 0)
    CameraSetDistance(5350, 0)
    ChrSetPos(0x0103, 69550, 0, 60780, 270)
    ChrSetPos(0x0101, 70210, 0, 59570, 270)
    ChrSetPos(0x0102, 71260, 0, 60540, 270)
    OP_12(0x00009470, 0x00030D40, 0x00000000)

    @scena.Lambda('lambda_3459')
    def lambda_3459():
        OP_6C(270000, 8000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_3459)

    Sleep(3000)

    @scena.Lambda('lambda_346E')
    def lambda_346E():
        CameraMove(69410, 0, 60250, 5000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_346E)

    @scena.Lambda('lambda_3486')
    def lambda_3486():
        OP_67(0, 9500, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_3486)

    CameraSetDistance(2800, 5000)
    OP_12(0x00009470, 0x000186A0, 0x00001F40)

    ChrTalk(
        0x0103,
        (
            '#0030020360V#020F终于到了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020361V这里就是柏斯地区的中心，\n',
            '商业都市柏斯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020362V#004F哇～……\n',
            '果然是都市的感觉呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020363V#010F柏斯在利贝尔的五大都市之中，\n',
            '城市规模仅次于王都。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020020364V和洛连特相比，这里的建筑物都是石制的，\n',
            '给人一种巨大结实的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010020365V#000F哎，那边那间大得夸张的房子\n',
            '是做什么用的啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030020366V#020F那个是柏斯超市。\n',
            '一个汇集了各种商店的室内市场。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020367V食品、衣服、杂货、家具、书籍……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020368V除了武器和导力器以外的商品，\n',
            '在那里基本都能买到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020369V#501F不愧是商业都市，\n',
            '真是名副其实的繁华啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020370V#007F啊啊……\n',
            '要是为了购物来这里玩就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020020371V#010F那样的事以后还有机会。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020020372V我们还是先去趟协会支部，\n',
            '确认一下到底发生了什么事吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010020373V#002F……嗯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020374V#020F顺便说一下，\n',
            '柏斯支部就在前面很近的地方哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x0014 offset: 0x382A
@scena.Code('func_14_382A')
def func_14_382A():
    EventBegin(0x00)
    CameraMove(64470, 0, 73180, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(261, 0)
    OP_4A(0x0008, 255)
    OP_4A(0x0009, 255)
    OP_4A(0x000C, 255)
    TerminateThread(0x0010, 0xFF)
    TerminateThread(0x0013, 0xFF)
    ChrSetPos(0x0103, 63280, 0, 74260, 180)
    ChrSetPos(0x0101, 64540, 0, 74600, 180)
    ChrSetPos(0x0102, 65730, 0, 74040, 225)
    ChrSetPos(0x0010, 64220, 0, 71730, 0)
    ChrSetPos(0x0013, 65120, 0, 70810, 0)
    ChrTurnDirection(0x0101, 0x0010, 0)
    ChrTurnDirection(0x0102, 0x0010, 0)
    ChrTurnDirection(0x0103, 0x0010, 0)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrSetFlags(0x0010, 0x0040)
    ChrSetFlags(0x0013, 0x0040)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0010,
        (
            '#0360020631V#610F……那么各位，\n',
            '这件事无论如何拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020632V#006F嗯！交给我们吧！\n',
            '得到什么消息就通知您。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0360020633V#611F期待你们的好消息。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360020634V那么，祝一路平安。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0370020635V#620F……诸位请慢走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0010, 180, 400)

    @scena.Lambda('lambda_39FC')
    def lambda_39FC():
        ChrWalkTo(0x0010, 64420, 0, 64489, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_39FC)

    Sleep(500)

    ChrSetDirection(0x0013, 180, 400)
    ChrWalkTo(0x0013, 64420, 0, 64489, 3000, 0x00)

    @scena.Lambda('lambda_3A37')
    def lambda_3A37():
        OP_69(0x0101, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_3A37)

    Sleep(1000)

    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030020636V#020F好了，赶紧出发吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020637V去哈肯大门的话，\n',
            '要先通过东柏斯街道北面的钢壁之路。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)
    ChrTurnDirection(0x0102, 0x0103, 400)

    ChrTalk(
        0x0102,
        (
            '#0020020638V#010F也就是说，从城的东门出去，\n',
            '然后向北走就可以了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020639V#006F那么，我们出发吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x0008, 255)
    OP_4B(0x0009, 255)
    OP_4B(0x000C, 255)
    EventEnd(0x00)
    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x0013, 0x0080)

    Return()

# id: 0x0015 offset: 0x3B4D
@scena.Code('func_15_3B4D')
def func_15_3B4D():
    EventBegin(0x00)
    MapClearFlags(0x00000001)
    OP_4A(0x0008, 255)
    OP_4A(0x0009, 255)
    OP_4A(0x000C, 255)
    TerminateThread(0x0104, 0xFF)
    CameraMove(70630, 0, 62020, 0)
    OP_6C(315000, 0)
    ChrSetPos(0x0104, 70660, 0, 60750, 270)
    ChrSetPos(0x0103, 72300, 0, 59880, 270)
    ChrSetPos(0x0101, 71730, 0, 61730, 270)
    ChrSetPos(0x0102, 73360, 0, 61130, 270)
    FadeIn(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0104,
        (
            '#0040021038V#030F#1P哦～这就是柏斯市。\n',
            '比想象中还要繁华许多啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040021039V那边那座高大的建筑物\n',
            '是不是叫柏斯超市？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0104, 400)

    ChrTalk(
        0x0101,
        (
            '#0010021040V#000F#2P嗯，你知道的还挺多嘛。\n',
            '不是第一次来利贝尔王国吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0104, 0)
    ChrTurnDirection(0x0104, 0x0102, 400)

    ChrTalk(
        0x0104,
        (
            '#0040021041V#035F#1P呵呵，因为我旅行出发前\n',
            '买了一本观光手册啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040021042V是一家叫『利贝尔通讯社』的\n',
            '出版社出版的导游刊物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021043V#004F#2P观、观光手册～？\n',
            '这种东西也有卖的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021044V#010F怎么说呢，毕竟现在已经是\n',
            '做什么事都十分便利的时代了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021045V#020F那么你是不是\n',
            '打算去超市购物啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040021046V#030F#1P啊啊，超市只是一般逛逛，\n',
            '正餐倒是打算吃得豪华一点。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040021047V根据观光手册上说，\n',
            '这座城市有家三星级的高级饭店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021048V#000F#2P啊，就是我们和\n',
            '市长商量事情的地方吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010021049V#000F#1P就是那座建筑啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3EF2')
    def lambda_3EF2():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3EF2)

    @scena.Lambda('lambda_3F00')
    def lambda_3F00():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_3F00)

    @scena.Lambda('lambda_3F0E')
    def lambda_3F0E():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_3F0E)

    @scena.Lambda('lambda_3F1C')
    def lambda_3F1C():
        OP_6C(45000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3F1C)

    CameraMove(67520, 260, 72190, 3000)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020021050V#010F叫做『安特洛丝餐厅』，\n',
            '以正宗利贝尔料理闻名的饭店。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    CameraMove(70630, 0, 62020, 0)
    OP_6C(315000, 0)
    OP_0D()

    ChrTalk(
        0x0104,
        (
            '#0040021051V#031F#1P嗯，看样子就是这里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040021052V呵呵呵……今天开始要享福了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0104, 400)
    ChrTurnDirection(0x0102, 0x0104, 400)
    ChrTurnDirection(0x0103, 0x0104, 400)

    ChrTalk(
        0x0103,
        (
            '#0030021053V#020F但是，要享受高档的美食，\n',
            '花费还是相当的高哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021054V我劝你还是去普通的酒馆吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0104, 0x0102, 400)

    ChrTalk(
        0x0104,
        (
            '#0040021055V#030F#1P请不用担心。\n',
            '我带了很多的旅费呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040021056V而且如果真的不够用，\n',
            '本人还可以用自己的特技赚钱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021057V#014F特技……\n',
            '是指刚才的唱歌和演奏吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021058V#009F#2P打、打算靠那个赚钱？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040021059V#035F#1P呵呵，我还曾在帝都的大剧场\n',
            '担任过歌剧的主演呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040021060V那一次，虽然只有一个晚上，\n',
            '却赚了足足一百万米拉呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021061V#007F#2P（太假了吧～……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040021062V#030F#1P那么各位，你们辛苦了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040021063V直到命中注定的再次相会为止，\n',
            '让我们先暂时地分别吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040021064V#031FAdeus amigo！（葡萄牙语：再见朋友）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0104, 270, 400)
    Sleep(250)

    @scena.Lambda('lambda_42DC')
    def lambda_42DC():
        ChrTurnDirection(0x00FE, 0x0104, 0)
        Yield()

        Jump('lambda_42DC')

    DispatchAsync2(0x0101, 0x0001, lambda_42DC)

    @scena.Lambda('lambda_42ED')
    def lambda_42ED():
        ChrTurnDirection(0x00FE, 0x0104, 0)
        Yield()

        Jump('lambda_42ED')

    DispatchAsync2(0x0102, 0x0001, lambda_42ED)

    @scena.Lambda('lambda_42FE')
    def lambda_42FE():
        ChrTurnDirection(0x00FE, 0x0104, 0)
        Yield()

        Jump('lambda_42FE')

    DispatchAsync2(0x0103, 0x0001, lambda_42FE)

    OP_62(0x0104, 0x00000000, 2300, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    ChrWalkTo(0x0104, 61236, 0, 60640, 6000, 0x00)
    Sleep(1000)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0103, 0xFF)

    @scena.Lambda('lambda_434B')
    def lambda_434B():
        CameraMove(72130, 0, 62020, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_434B)

    ChrSetDirection(0x0101, 135, 400)
    ChrSetDirection(0x0103, 45, 400)
    WaitForThreadExit(0x0000, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010021065V#008F哈～……\n',
            '真是无可救药的家伙啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021066V埃雷波尼亚帝国的人\n',
            '是不是都像他那样奇怪的啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020021067V#018F#4P那个样子的话，\n',
            '一般的埃雷波尼亚人也会觉得困扰吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021068V#501F哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021069V#015F#4P没什么，\n',
            '我觉得还是朴实的人比较多。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020021070V曾经读过的书里说过，\n',
            '他们崇尚质朴刚健的民风。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021071V#000F唔～……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021072V这么说来，\n',
            '艺术家果然都是不正常的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021073V#021F哎呀哎呀。\n',
            '要是其他艺术家听到了可是会生气的哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021074V#020F接下来……\n',
            '我们到协会向卢格兰爷爷汇报一下\n',
            '从将军那里打听到的消息吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021075V#010F#4P报告完毕之后，\n',
            '最好再去市长官邸知会梅贝尔市长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021076V#006F协会和市长官邸啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021077V那我们赶快走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FormationDelMember(0x03, 0xFF)
    OP_B8(0x03)
    OP_4B(0x0008, 255)
    OP_4B(0x0009, 255)
    OP_4B(0x000C, 255)
    EventEnd(0x00)

    Return()

# id: 0x0016 offset: 0x4672
@scena.Code('func_16_4672')
def func_16_4672():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 3, 0x313)),
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 6, 0x316)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5199',
    )

    SetScenaFlags(ScenaFlag(0x0062, 6, 0x316))
    TerminateThread(0x0013, 0xFF)
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0013, 0x0080)
    ChrSetPos(0x0013, 24359, 500, 57973, 90)
    ChrSetPos(0x0011, 25364, 0, 57280, 270)
    ChrSetPos(0x0012, 25497, 0, 58710, 270)
    ChrTurnDirection(0x0011, 0x0013, 800)
    ChrTurnDirection(0x0012, 0x0013, 800)

    @scena.Lambda('lambda_46E2')
    def lambda_46E2():
        OP_6C(270000, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_46E2)

    CameraMove(24400, 0, 57655, 3000)

    ChrTalk(
        0x0011,
        (
            '#0270021107V#141F喂，小姐。\n',
            '拜托你通报一下吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270021108V只要市长一句话，\n',
            '做一下评论就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0280021109V#151F就是就是，\n',
            '之后再顺便照张相片就行了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0370021110V#620F#5P即使你们这么说……\n',
            '市长她现在的公务非常繁忙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370021111V而且你们没有事先预约，\n',
            '所以还是请回吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370021112V请务必谅解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0270021113V#144F怎能这样！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270021114V像这样的大事件，\n',
            '我们却什么情况都不知道……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270021115V一定要对读者有个交待才行呀！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0370021116V#623F#5P可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0280021117V#151F没错没错，就是那样的哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280021118V如果由那位传说中的美人市长作封面，\n',
            '销量绝对会大增的哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0370021119V#620F#5P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0011, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1200)

    @scena.Lambda('lambda_49A2')
    def lambda_49A2():
        ChrTurnDirection(0x00FE, 0x0012, 0)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_49A2)

    ChrTalk(
        0x0011,
        (
            '#0270021120V#144F喂，朵洛希！\n',
            '别说这么失礼的话！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_49E6')
    def lambda_49E6():
        ChrTurnDirection(0x00FE, 0x0011, 0)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_49E6)

    ChrTalk(
        0x0012,
        (
            '#0280021121V#153F哎～～\n',
            '这不是奈尔前辈你跟我说的吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280021122V如果没有什么新闻的话，\n',
            '就把美人市长塑造为吸引读者的偶像，\n',
            '作为杂志的封面人物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0270021123V#144F喂，笨蛋！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0370021124V#620F#5P………………………………\n',
            '………………………………\n',
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    ChrTurnDirection(0x0011, 0x0013, 0)
    Sleep(500)

    ChrTalk(
        0x0011,
        (
            '#0270021125V#143F我、我说，女佣小姐？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0370021126V#620F#5P真是非常有趣的客人呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370021127V你们二位的话，\n',
            '我会详细地向市长转达的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370021128V今天请二位先回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0270021129V#144F等、等一下！\n',
            '这之中稍微有点误会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0370021130V#624F#5P请·您·回·去·吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0270021131V#145F是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0280021132V#153F哎，美人市长的照片，\n',
            '不拍也没关系吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0270021133V#145F拜托……算我求你了……\n',
            '从现在开始不要再多嘴了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0011, 45, 400)

    @scena.Lambda('lambda_4CE4')
    def lambda_4CE4():
        ChrWalkTo(0x00FE, 31497, 0, 57900, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_4CE4)

    Sleep(300)

    @scena.Lambda('lambda_4D04')
    def lambda_4D04():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_4D04')

    DispatchAsync2(0x0012, 0x0001, lambda_4D04)

    OP_62(0x0012, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0012,
        (
            '#0280021134V#153F前、前辈！\n',
            '请等一下啦～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0012, 0xFF)
    ChrWalkTo(0x0012, 31497, 0, 57900, 3000, 0x00)

    ChrTalk(
        0x0013,
        (
            '#0370021135V#620F#5P呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    OP_62(0x0013, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTalk(
        0x0013,
        (
            '#0370021136V#622F#5P…………哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetPos(0x0101, 33497, 0, 57400, 0)
    ChrSetPos(0x0102, 33497, 0, 58550, 0)
    ChrSetPos(0x0103, 33497, 0, 57890, 0)

    @scena.Lambda('lambda_4E22')
    def lambda_4E22():
        CameraMove(25400, 0, 57800, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_4E22)

    @scena.Lambda('lambda_4E3A')
    def lambda_4E3A():
        ChrWalkTo(0x00FE, 27850, 0, 57400, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4E3A)

    Sleep(500)

    @scena.Lambda('lambda_4E5A')
    def lambda_4E5A():
        ChrWalkTo(0x00FE, 28000, 0, 58550, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_4E5A)

    Sleep(500)

    @scena.Lambda('lambda_4E7A')
    def lambda_4E7A():
        ChrWalkTo(0x00FE, 29360, 0, 57890, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_4E7A)

    WaitForThreadExit(0x0103, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010021137V#000F你好，莉拉小姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0370021138V#620F#1P啊，原来是诸位游击士啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370021139V你们刚从\n',
            '哈肯大门那边回来吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021140V#000F嗯，没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021141V话说回来，刚才的那些人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0370021142V#620F#1P都是不速之客。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021143V#501F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0370021144V#620F#1P都是些意图\n',
            '在小姐身上打主意的不法之徒。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370021145V在我的眼皮底下，\n',
            '他们休想碰小姐一根指头。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1200)

    ChrTalk(
        0x0101,
        (
            '#0010021146V#008F啊、啊哈哈……是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021147V#019F工、工作真是尽职尽责啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0370021148V#621F#1P因为那是我的责任。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370021149V好了，诸位请进吧。\n',
            '市长正等着你们呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0013, 270, 400)
    OP_6F(0x0006, 0)
    OP_70(0x0006, 60)
    OP_73(0x0006)
    ChrSetFlags(0x0013, 0x0040)
    ChrWalkTo(0x0013, 23375, 500, 58050, 3000, 0x00)

    @scena.Lambda('lambda_5143')
    def lambda_5143():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_5143)

    ChrSetFlags(0x0013, 0x0004)
    OP_94(0x00, 0x0013, 0x0000, 0x000001F4, 0x000005DC, 0x00)
    OP_72(0x0006, 0x0800)
    PlaySE(7, 0x00, 0x64)
    OP_6F(0x0006, 60)
    OP_70(0x0006, 0)
    OP_73(0x0006)
    OP_71(0x0006, 0x0800)
    ChrSetFlags(0x0013, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    EventEnd(0x00)

    def _loc_5199(): pass

    label('loc_5199')

    Return()

# id: 0x0017 offset: 0x519A
@scena.Code('func_17_519A')
def func_17_519A():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    ChrSetPos(0x0101, 28680, 0, 57870, 90)
    ChrSetPos(0x0102, 29950, 0, 59190, 180)
    ChrSetPos(0x0103, 30030, 0, 56790, 0)
    CameraMove(28840, 0, 57170, 0)
    OP_6C(225000, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010021205V#002F#2P嗯……\n',
            '市长姐姐她刚才怎么了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021206V听到老爸名字的时候，\n',
            '好像相当吃惊的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021207V#015F确实如此呢……\n',
            '不过也不难想象出来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020021208V也许父亲和市长\n',
            '还有摩尔根将军以前就认识了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021209V#501F#2P？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 4, 0x314)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_53CA',
    )

    ChrTalk(
        0x0103,
        (
            '#0030021210V#020F好了，先把这个放在一边吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021211V向市长报告完毕了，\n',
            '接着去游击士协会一趟吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021212V卢格兰爷爷\n',
            '一定在等着我们的报告了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021213V#006F#2P嗯，知道了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_58D5')

    def _loc_53CA(): pass

    label('loc_53CA')

    SetScenaFlags(ScenaFlag(0x0062, 5, 0x315))

    ChrTalk(
        0x0103,
        (
            '#0030021214V#020F好了，先把这个放在一边吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021215V接下来的问题就是\n',
            '我们该采取什么行动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021216V#002F#2P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021217V光是要找定期船和空贼团的隐藏地点\n',
            '就已经很困难了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021218V如果能轻易找得到的话，\n',
            '军队方面也应该早就发现才对啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 0)

    ChrTalk(
        0x0102,
        (
            '#0020021219V#014F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 0)

    ChrTalk(
        0x0103,
        (
            '#0030021220V#023F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)
    Sleep(200)

    ChrTurnDirection(0x0101, 0x0103, 400)
    Sleep(200)

    ChrSetDirection(0x0101, 90, 400)
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010021221V#000F#2P嗯，你们两个怎么了啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021222V#014F艾丝蒂尔，你变得成熟了呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020021223V如果是以前的你，肯定只会说出\n',
            '『彻底地搜查一遍不就好了』\n',
            '这样不经考虑的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021224V#021F没想到能从艾丝蒂尔的嘴里\n',
            '听到这么理智的分析……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021225V姐姐我真是太感动了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010021226V#009F#2P你们什么意思！\n',
            '真是没礼貌！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021227V#019F哈哈，这是在表扬你呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021228V#020F确实，和洛连特不同，\n',
            '柏斯地区幅员相当广阔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021229V现在最需要的就是线索。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021230V#003F#2P线索啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021231V#006F对了，刚才在市长家门前，\n',
            '不是看见奈尔他们了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021232V他们好像正在\n',
            '为报道取材的事烦恼着……\n',
            '会不会知道些什么线索呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021233V#010F也有道理，\n',
            '他们本来就比我们早一步到达柏斯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020021234V我觉得有打听一下的必要。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021235V#000F#2P那两个人去了哪里呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0035, 0x01, 0x0800)
    OP_28(0x0035, 0x01, 0x1000)

    def _loc_58D5(): pass

    label('loc_58D5')

    MapClearFlags(0x00400000)
    EventEnd(0x00)

    Return()

# id: 0x0018 offset: 0x58DD
@scena.Code('func_18_58DD')
def func_18_58DD():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    OP_4A(0x0008, 255)
    OP_4A(0x0009, 255)
    OP_4A(0x000C, 255)
    CameraMove(58940, 0, 77210, 0)
    ChrSetPos(0x0101, 58890, 0, 78180, 180)
    ChrSetPos(0x0102, 57570, 0, 76880, 90)
    ChrSetPos(0x0103, 59990, 0, 77000, 270)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0103,
        (
            '#0030021236V#020F#4P虽然已经向协会\n',
            '还有市长报告过了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021237V可是我们今后该如何行动才好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021238V#002F#1P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021239V光是要找定期船和空贼团的隐藏地点\n',
            '就已经很困难了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021240V如果能轻易找得到的话，\n',
            '军队方面也应该早就发现才对啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 0)

    ChrTalk(
        0x0102,
        (
            '#0020021241V#014F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 0)

    ChrTalk(
        0x0103,
        (
            '#0030021220V#023F#4P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)
    Sleep(200)

    ChrTurnDirection(0x0101, 0x0103, 400)
    Sleep(200)

    ChrSetDirection(0x0101, 180, 400)
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010021243V#000F#1P嗯，你们两个怎么了啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021244V#014F艾丝蒂尔，你变得成熟了呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020021245V如果是以前的你，肯定只会说出\n',
            '『彻底地搜查一遍不就好了』\n',
            '这样不经考虑的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021246V#021F#4P没想到能从艾丝蒂尔的嘴里\n',
            '听到这么理智的分析……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021247V姐姐我真是太感动了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010021248V#009F#1P你们什么意思！\n',
            '真是没礼貌！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021249V#019F哈哈，这是在表扬你呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021250V#020F#4P确实，和洛连特不同，\n',
            '柏斯地区幅员相当广阔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021251V现在最需要的就是线索。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021252V#003F#1P线索啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021253V#006F对了，刚才在市长家门前，\n',
            '不是看见奈尔他们了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010021254V他们好像正在\n',
            '为报道取材的事烦恼着……\n',
            '会不会知道些什么线索呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020021255V#010F也有道理，\n',
            '他们本来就比我们早一步到达柏斯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020021256V我觉得有打听一下的必要。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010021257V#000F#1P那两个人去了哪里呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0035, 0x01, 0x0800)
    OP_28(0x0035, 0x01, 0x1000)
    OP_4B(0x0008, 255)
    OP_4B(0x0009, 255)
    OP_4B(0x000C, 255)
    EventEnd(0x00)

    Return()

# id: 0x0019 offset: 0x5E5F
@scena.Code('func_19_5E5F')
def func_19_5E5F():
    EventBegin(0x00)
    CameraMove(49570, 0, 86360, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3240, 0)
    OP_6C(45000, 0)
    OP_6E(261, 0)
    OP_4A(0x0008, 255)
    OP_4A(0x0009, 255)
    OP_4A(0x000C, 255)
    OP_B8(0x02)
    OP_B8(0x03)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x03, 0xFF)
    ChrSetPos(0x0101, 47600, 3000, 91910, 180)
    ChrSetPos(0x0102, 48600, 3000, 92500, 180)

    @scena.Lambda('lambda_5EDC')
    def lambda_5EDC():
        ChrWalkTo(0x00FE, 47600, 0, 81680, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5EDC)

    @scena.Lambda('lambda_5EF7')
    def lambda_5EF7():
        ChrWalkTo(0x00FE, 48600, 0, 82950, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_5EF7)

    FadeIn(2000, 0)
    Sleep(3500)

    Fade(500)
    CameraMove(48040, 0, 83320, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(0, 0)
    OP_6E(261, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0001)
    ChrSetDirection(0x0101, 45, 400)
    WaitForThreadExit(0x0102, 0x0001)
    ChrSetDirection(0x0102, 225, 400)

    ChrTalk(
        0x0101,
        (
            '#0010040062V#000F接下来，要环游整个王国的话，\n',
            '那么下一个目的地就是卢安地区了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040063V走哪条路好呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040064V#014F#2P你这样说的话……\n',
            '真的决定不坐定期船了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040065V如果要步行，\n',
            '应该会绕不少弯路的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040066V#006F雪拉姐不是说过吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040067V要守护一片土地，\n',
            '首先就要自己脚踏实地去看一看。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040068V啊，这是父亲说的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040069V#010F#2P也对，我们的时间确实很充裕，\n',
            '我也觉得慢慢走路去也不错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040070V定期船的票钱也能节省下来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040071V#001F是啊是啊，\n',
            '就用省下来的钱去柏斯超市采购一番吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040072V空贼作乱的时候我们\n',
            '都没办法静下心来好好买东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040073V#501F就在出发前先逛逛超市吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040074V#017F#2P我倒没什么关系……\n',
            '只是希望你不要太乱花钱了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040075V#010F顺便说一下，要去卢安地区，\n',
            '就必须经过西面的古罗尼山峰。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040076V买好东西后就从城里的西门出发吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040077V#006FＯＫ！城里的西门是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x006B, 5, 0x35D))
    SetScenaFlags(ScenaFlag(0x006B, 6, 0x35E))
    SetScenaFlags(ScenaFlag(0x0080, 0, 0x400))

    ExecExpressionWithVar(
        0x04,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_4B(0x0008, 255)
    OP_4B(0x0009, 255)
    OP_4B(0x000C, 255)
    EventEnd(0x00)

    Return()

# id: 0x001A offset: 0x6311
@scena.Code('func_1A_6311')
def func_1A_6311():
    OP_13(0x002A)

    Return()

# id: 0x001B offset: 0x6315
@scena.Code('func_1B_6315')
def func_1B_6315():
    OP_13(0x0026)

    Return()

# id: 0x001C offset: 0x6319
@scena.Code('func_1C_6319')
def func_1C_6319():
    OP_13(0x0025)

    Return()

# id: 0x001D offset: 0x631D
@scena.Code('func_1D_631D')
def func_1D_631D():
    OP_13(0x0020)

    Return()

# id: 0x001E offset: 0x6321
@scena.Code('func_1E_6321')
def func_1E_6321():
    OP_13(0x0028)

    Return()

# id: 0x001F offset: 0x6325
@scena.Code('func_1F_6325')
def func_1F_6325():
    OP_13(0x002B)

    Return()

# id: 0x0020 offset: 0x6329
@scena.Code('func_20_6329')
def func_20_6329():
    OP_13(0x0021)

    Return()

# id: 0x0021 offset: 0x632D
@scena.Code('func_21_632D')
def func_21_632D():
    OP_13(0x0027)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

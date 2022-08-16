import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3400_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3400   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3400.x'
    header.mapIndex       = 1
    header.bgm            = 16
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
        ('ED6_DT07/CH01750._CH', 'ED6_DT07/CH01750P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT07/CH01520._CH', 'ED6_DT07/CH01520P._CP'),
        ('ED6_DT07/CH01350._CH', 'ED6_DT07/CH01350P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH01230._CH', 'ED6_DT07/CH01230P._CP'),
        ('ED6_DT07/CH01180._CH', 'ED6_DT07/CH01180P._CP'),
        ('ED6_DT07/CH01310._CH', 'ED6_DT07/CH01310P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
    ]

# id: 0x10001 offset: 0x122
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '冈多夫',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '士兵儒勒',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '士兵埃克托尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '士兵切斯利',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            name                = '阿鲁姆',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            name                = '艾娅莉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '士兵维恩',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '塔尔瓦托副长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '桑吉特',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '黛米',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '玛丽安',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '诺琪',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '塔丽娅',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '迪鲁队长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '士兵沃普',
            x                   = 35300,
            z                   = 0,
            y                   = -3600,
            direction           = 92,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '士兵欧鲁尼斯',
            x                   = 35310,
            z                   = 0,
            y                   = 3610,
            direction           = 92,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '利塔街道方向',
            x                   = -37360,
            z                   = 0,
            y                   = 960,
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
            name                = '庭园大道方向',
            x                   = 83520,
            z                   = 0,
            y                   = 630,
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

# id: 0x10002 offset: 0x362
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x362
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x362
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x362
@scena.Code('Init')
def Init():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x0000006A, 'loc_36E'),
        (-1, 'loc_384'),
    )

    def _loc_36E(): pass

    label('loc_36E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 5, 0x605)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 4, 0x604)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_381',
    )

    SetScenaFlags(ScenaFlag(0x00C0, 5, 0x605))
    Event(0, func_14_27F8)

    def _loc_381(): pass

    label('loc_381')

    Jump('loc_384')

    def _loc_384(): pass

    label('loc_384')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_38E',
    )

    Jump('loc_436')

    def _loc_38E(): pass

    label('loc_38E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_3AE',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, 9970, 0, 6140, 257)

    Jump('loc_436')

    def _loc_3AE(): pass

    label('loc_3AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_3B8',
    )

    Jump('loc_436')

    def _loc_3B8(): pass

    label('loc_3B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_3C2',
    )

    Jump('loc_436')

    def _loc_3C2(): pass

    label('loc_3C2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_3CC',
    )

    Jump('loc_436')

    def _loc_3CC(): pass

    label('loc_3CC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_3D6',
    )

    Jump('loc_436')

    def _loc_3D6(): pass

    label('loc_3D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_3E0',
    )

    Jump('loc_436')

    def _loc_3E0(): pass

    label('loc_3E0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_3EA',
    )

    Jump('loc_436')

    def _loc_3EA(): pass

    label('loc_3EA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_3F4',
    )

    Jump('loc_436')

    def _loc_3F4(): pass

    label('loc_3F4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_419',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, 9970, 0, 6140, 257)
    ChrSetFlags(0x0008, 0x0010)

    Jump('loc_436')

    def _loc_419(): pass

    label('loc_419')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_436',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, 3560, 0, -430, 90)

    def _loc_436(): pass

    label('loc_436')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_456',
    )

    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 15080, 11750, -60, 276)

    Jump('loc_6E7')

    def _loc_456(): pass

    label('loc_456')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_476',
    )

    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 15080, 11750, -60, 276)

    Jump('loc_6E7')

    def _loc_476(): pass

    label('loc_476')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_496',
    )

    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 15080, 11750, -60, 276)

    Jump('loc_6E7')

    def _loc_496(): pass

    label('loc_496')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_4B6',
    )

    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 15080, 11750, -60, 276)

    Jump('loc_6E7')

    def _loc_4B6(): pass

    label('loc_4B6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_4D6',
    )

    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 15080, 11750, -60, 276)

    Jump('loc_6E7')

    def _loc_4D6(): pass

    label('loc_4D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 6, 0x606)),
            Expr.Return,
        ),
        'loc_4F6',
    )

    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 15080, 11750, -60, 276)

    Jump('loc_6E7')

    def _loc_4F6(): pass

    label('loc_4F6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 5, 0x605)),
            Expr.Return,
        ),
        'loc_516',
    )

    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 15080, 11750, -60, 276)

    Jump('loc_6E7')

    def _loc_516(): pass

    label('loc_516')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_562',
    )

    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 10640, 0, -3930, 285)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, 10660, 0, 3380, 263)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 15080, 11750, -60, 276)

    Jump('loc_6E7')

    def _loc_562(): pass

    label('loc_562')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_5AE',
    )

    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 10640, 0, -3930, 285)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, 10660, 0, 3380, 263)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 15080, 11750, -60, 276)

    Jump('loc_6E7')

    def _loc_5AE(): pass

    label('loc_5AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_5FA',
    )

    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 10640, 0, -3930, 285)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, 10660, 0, 3380, 263)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 15080, 11750, -60, 276)

    Jump('loc_6E7')

    def _loc_5FA(): pass

    label('loc_5FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_672',
    )

    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 10640, 0, -3930, 285)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, 10660, 0, 3380, 263)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 15080, 11750, -60, 276)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, 26240, 7250, -33770, 101)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 26260, 7250, -34450, 85)

    Jump('loc_6E7')

    def _loc_672(): pass

    label('loc_672')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_6E7',
    )

    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x000A, 10640, 0, -3930, 285)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, 10660, 0, 3380, 263)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 15080, 11750, -60, 276)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, 26240, 7250, -33770, 101)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 26260, 7250, -34450, 85)

    def _loc_6E7(): pass

    label('loc_6E7')

    Return()

# id: 0x0001 offset: 0x6E8
@scena.Code('func_01_6E8')
def func_01_6E8():
    OP_16(0x02, 4000, -105000, -128000, 196694)
    OP_6F(0x0000, 160)
    OP_6F(0x0001, 160)
    OP_72(0x0000, 0x0010)
    OP_72(0x0001, 0x0010)
    OP_1C(0x02, 0x00, 0x0015)
    OP_1C(0x03, 0x00, 0x0015)
    OP_1C(0x04, 0x00, 0x0015)

    If(
        (
            (Expr.GetChrWork, 0x101, 0x1E),
            (Expr.PushLong, 0x11C),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_735',
    )

    OP_28(0x002A, 0x01, 0x8000)

    def _loc_735(): pass

    label('loc_735')

    Return()

# id: 0x0002 offset: 0x736
@scena.Code('func_02_736')
def func_02_736():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_74B',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_736')

    def _loc_74B(): pass

    label('loc_74B')

    Return()

# id: 0x0003 offset: 0x74C
@scena.Code('func_03_74C')
def func_03_74C():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_76F',
    )

    OP_8D(0x00FE, 7090, 6400, -600, -6500, 1500)

    Jump('func_03_74C')

    def _loc_76F(): pass

    label('loc_76F')

    Return()

# id: 0x0004 offset: 0x770
@scena.Code('func_04_770')
def func_04_770():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_7FF',
    )

    ChrTalk(
        0x00FE,
        (
            '听前辈说起过，\n',
            '国境守备队的摩尔根将军\n',
            '是个很可怕的人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但他毕竟是个\n',
            '在教科书中也提到的名人，\n',
            '一定是个很了不起的人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ADA')

    def _loc_7FF(): pass

    label('loc_7FF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_881',
    )

    ChrTalk(
        0x00FE,
        (
            '亲卫队里\n',
            '似乎也聚集着一群\n',
            '和特务部队一样强的人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是被那样的家伙们袭击……\n',
            '光是这么想想\n',
            '就觉得很恐怖了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ADA')

    def _loc_881(): pass

    label('loc_881')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_951',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Return,
        ),
        'loc_8D6',
    )

    ChrTalk(
        0x00FE,
        (
            '王国军的\n',
            '警戒等级提高了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '队长说这里也有\n',
            '被袭击的可能性。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_94E')

    def _loc_8D6(): pass

    label('loc_8D6')

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    ChrTalk(
        0x00FE,
        (
            '王国军的\n',
            '警戒等级提高了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '队长说这里也有\n',
            '被袭击的可能性。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这……这么一来，\n',
            '我现在连看守也觉得紧张了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_94E(): pass

    label('loc_94E')

    Jump('loc_ADA')

    def _loc_951(): pass

    label('loc_951')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_9B3',
    )

    ChrTalk(
        0x00FE,
        (
            '武术大会的正式赛是从今天开始吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在我小的时候，\n',
            '妈妈经常带我\n',
            '去竞技场看比赛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ADA')

    def _loc_9B3(): pass

    label('loc_9B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_A2A',
    )

    ChrTalk(
        0x00FE,
        (
            '呼～\n',
            '之前刚进行了防恐怖袭击训练，\n',
            '还没有从疲劳中恢复呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，现在是非常时期，\n',
            '不振作起来不行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ADA')

    def _loc_A2A(): pass

    label('loc_A2A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 7, 0x607)),
            Expr.Return,
        ),
        'loc_A6B',
    )

    ChrTalk(
        0x00FE,
        (
            '快要到诞辰庆典了，\n',
            '要是能早点抓住恐怖分子就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ADA')

    def _loc_A6B(): pass

    label('loc_A6B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 6, 0x606)),
            Expr.Return,
        ),
        'loc_AD3',
    )

    ChrTalk(
        0x00FE,
        (
            '我是刚刚被分配\n',
            '到这里的守备队来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里有很多严厉的前辈，\n',
            '弄得我一天到晚都很紧张。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ADA')

    def _loc_AD3(): pass

    label('loc_AD3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 5, 0x605)),
            Expr.Return,
        ),
        'loc_ADA',
    )

    def _loc_ADA(): pass

    label('loc_ADA')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0xADE
@scena.Code('func_05_ADE')
def func_05_ADE():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_BCE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Return,
        ),
        'loc_B55',
    )

    ChrTalk(
        0x00FE,
        (
            '武术大会结束了，\n',
            '但是还有诞辰庆典，\n',
            '不能松懈啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为不知道恐怖分子\n',
            '什么时候会袭击过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BCB')

    def _loc_B55(): pass

    label('loc_B55')

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))

    ChrTalk(
        0x00FE,
        (
            '没有异常！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '武术大会结束了，\n',
            '但是还有诞辰庆典，\n',
            '不能松懈啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为不知道恐怖分子\n',
            '什么时候会袭击过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BCB(): pass

    label('loc_BCB')

    Jump('loc_1067')

    def _loc_BCE(): pass

    label('loc_BCE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_C28',
    )

    ChrTalk(
        0x00FE,
        (
            '最近队长和副长\n',
            '好像都在为什么而烦恼着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来在军队里\n',
            '麻烦事也不少呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1067')

    def _loc_C28(): pass

    label('loc_C28')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_CF9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Return,
        ),
        'loc_C8B',
    )

    ChrTalk(
        0x00FE,
        (
            '我之前一直\n',
            '梦想当个游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '直到最后还在犹豫\n',
            '到底是要入伍还是当游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CF6')

    def _loc_C8B(): pass

    label('loc_C8B')

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))

    ChrTalk(
        0x00FE,
        (
            '你们是游击士吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我之前一直\n',
            '梦想当个游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '直到最后还在犹豫\n',
            '到底是要入伍还是当游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CF6(): pass

    label('loc_CF6')

    Jump('loc_1067')

    def _loc_CF9(): pass

    label('loc_CF9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_D86',
    )

    ChrTalk(
        0x00FE,
        (
            '前一阵子我在周游道\n',
            '发现了一种发光的魔兽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他们只是一直在闪着光，\n',
            '后来闪够了就走掉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是有着\n',
            '奇特魅力的小家伙啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1067')

    def _loc_D86(): pass

    label('loc_D86')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_EDE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Return,
        ),
        'loc_E1B',
    )

    ChrTalk(
        0x00FE,
        (
            '以前听说，\n',
            '恐怖分子伪装成了亲卫队\n',
            '对中央工房进行了袭击……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，实际上不就是\n',
            '亲卫队自己犯下案件，\n',
            '从王城中逃走失踪了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EDB')

    def _loc_E1B(): pass

    label('loc_E1B')

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))

    ChrTalk(
        0x00FE,
        (
            '以前听说，\n',
            '恐怖分子伪装成了亲卫队\n',
            '对中央工房进行了袭击……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，实际上不就是\n',
            '亲卫队自己犯下案件，\n',
            '从王城中逃走失踪了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果要和亲卫队交战的话，\n',
            '这里也不能保证平安无事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EDB(): pass

    label('loc_EDB')

    Jump('loc_1067')

    def _loc_EDE(): pass

    label('loc_EDE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 7, 0x607)),
            Expr.Return,
        ),
        'loc_F53',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才通过这里的部队，\n',
            '好像是为了抓捕恐怖分子\n',
            '而被派遣去的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总觉得他们趾高气扬，\n',
            '有点让人讨厌啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1067')

    def _loc_F53(): pass

    label('loc_F53')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 6, 0x606)),
            Expr.Return,
        ),
        'loc_1060',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Return,
        ),
        'loc_FD2',
    )

    ChrTalk(
        0x00FE,
        (
            '说不定通缉中的\n',
            '恐怖分子正潜藏在周围，\n',
            '要小心点哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '当然，\n',
            '这一带有王国军在巡逻，\n',
            '我想应该很安全的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_105D')

    def _loc_FD2(): pass

    label('loc_FD2')

    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))

    ChrTalk(
        0x00FE,
        (
            '哦？你们要去王都吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说不定通缉中的\n',
            '恐怖分子正潜藏在周围，\n',
            '要小心点哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '当然，\n',
            '这一带有王国军在巡逻，\n',
            '我想应该很安全的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_105D(): pass

    label('loc_105D')

    Jump('loc_1067')

    def _loc_1060(): pass

    label('loc_1060')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 5, 0x605)),
            Expr.Return,
        ),
        'loc_1067',
    )

    def _loc_1067(): pass

    label('loc_1067')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x106B
@scena.Code('func_06_106B')
def func_06_106B():
    Return()

# id: 0x0007 offset: 0x106C
@scena.Code('func_07_106C')
def func_07_106C():
    Return()

# id: 0x0008 offset: 0x106D
@scena.Code('func_08_106D')
def func_08_106D():
    Return()

# id: 0x0009 offset: 0x106E
@scena.Code('func_09_106E')
def func_09_106E():
    Return()

# id: 0x000A offset: 0x106F
@scena.Code('func_0A_106F')
def func_0A_106F():
    Return()

# id: 0x000B offset: 0x1070
@scena.Code('func_0B_1070')
def func_0B_1070():
    Return()

# id: 0x000C offset: 0x1071
@scena.Code('func_0C_1071')
def func_0C_1071():
    Return()

# id: 0x000D offset: 0x1072
@scena.Code('func_0D_1072')
def func_0D_1072():
    Return()

# id: 0x000E offset: 0x1073
@scena.Code('func_0E_1073')
def func_0E_1073():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_13EA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AF, 7, 0x57F)),
            Expr.Return,
        ),
        'loc_10D4',
    )

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，要消灭的魔兽太多，\n',
            '还真是麻烦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '简直要累死人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13E7')

    def _loc_10D4(): pass

    label('loc_10D4')

    SetScenaFlags(ScenaFlag(0x00AF, 7, 0x57F))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AF, 6, 0x57E)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AF, 5, 0x57D)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_112E',
    )

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '哟，是你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0106, 400)

    ChrTalk(
        0x00FE,
        (
            '……怎么，阿加特。\n',
            '这不是很有精神嘛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11A9')

    def _loc_112E(): pass

    label('loc_112E')

    ChrSetFlags(0x00FE, 0x0010)
    TalkBegin(0x00FE)
    ChrClearFlags(0x00FE, 0x0010)
    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(800)

    ChrTurnDirection(0x00FE, 0x0106, 400)

    ChrTalk(
        0x00FE,
        (
            '哦，我还以为是谁。\n',
            '原来是阿加特啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……怎么回事，\n',
            '这不是很有精神嘛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11A9(): pass

    label('loc_11A9')

    ChrTalk(
        0x0106,
        (
            '#051F哼，\n',
            '那种程度根本算不了什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈哈，\n',
            '你还是那么命大呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果不振作起来的话，\n',
            '背上的『重剑』也会哭的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#050F冈多夫。\n',
            '你就别说这么多废话了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我们还有要紧的事去做呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哦，对啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '再见了，\n',
            '博士的事就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#051F不用你说我也知道该怎么做啦。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AF, 6, 0x57E)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AF, 5, 0x57D)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1305',
    )

    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '你们这些准游击士\n',
            '也要加把劲哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1364')

    def _loc_1305(): pass

    label('loc_1305')

    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '哦，\n',
            '你们就是那些准游击士吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '事情我都听雾香说过了。\n',
            '你们要好好协助阿加特哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1364(): pass

    label('loc_1364')

    ChrTalk(
        0x0102,
        (
            '#012F嗯，我们会谨慎行动的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#002F嗯……\n',
            '你也小心行事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0000, 400)

    ChrTalk(
        0x00FE,
        (
            '那就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '愿你们得到\n',
            '女神爱德丝的保佑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13E7(): pass

    label('loc_13E7')

    Jump('loc_14CD')

    def _loc_13EA(): pass

    label('loc_13EA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_14CD',
    )

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_144E',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，真是的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '王那个家伙\n',
            '如果再能干一点的话，\n',
            '我就会轻松很多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14CD')

    def _loc_144E(): pass

    label('loc_144E')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '……真是麻烦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这边消灭魔兽的委托\n',
            '也太多了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过因为有不少没见过的魔兽，\n',
            '所以工作起来还是挺有乐趣的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14CD(): pass

    label('loc_14CD')

    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x14D1
@scena.Code('func_0F_14D1')
def func_0F_14D1():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_1527',
    )

    ChrTalk(
        0x00FE,
        (
            '欢迎来到圣海姆门。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要办通行手续的话，\n',
            '要过关的话请去里面登记。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17A9')

    def _loc_1527(): pass

    label('loc_1527')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_1626',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1584',
    )

    ChrTalk(
        0x00FE,
        (
            '听到解除盘查的命令时，\n',
            '连队长都大吃一惊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '会不会是\n',
            '哪里弄错了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1623')

    def _loc_1584(): pass

    label('loc_1584')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '还没抓住恐怖分子，\n',
            '就忽然下了解除盘查的命令。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然无法理解……\n',
            '但身为军人\n',
            '绝对不能怀疑上级的决定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了王国的和平，\n',
            '只有老老实实执行任务了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1623(): pass

    label('loc_1623')

    Jump('loc_17A9')

    def _loc_1626(): pass

    label('loc_1626')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_16C1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1651',
    )

    ChrTalk(
        0x00FE,
        (
            '…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16BE')

    def _loc_1651(): pass

    label('loc_1651')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

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
            '……现在正在执勤，\n',
            '请不要和我聊天。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '想参观的话\n',
            '还是过一段时间比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_16BE(): pass

    label('loc_16BE')

    Jump('loc_17A9')

    def _loc_16C1(): pass

    label('loc_16C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_1728',
    )

    ChrTalk(
        0x00FE,
        (
            '从这个圣海姆门\n',
            '可以登到长城\n',
            '『亚宁堡』的城墙上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是有空的话，\n',
            '推荐去上面看一看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17A9')

    def _loc_1728(): pass

    label('loc_1728')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_17A9',
    )

    ChrTalk(
        0x00FE,
        (
            '欢迎来到圣海姆门！\n',
            '如果有事的话请往里面走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个大门是\n',
            '『亚宁堡』长城遗迹的一部分。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '非常欢迎游客前来参观。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17A9(): pass

    label('loc_17A9')

    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x17AD
@scena.Code('func_10_17AD')
def func_10_17AD():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_1804',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，\n',
            '难道你们是去参加诞辰庆典的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '其他的游客们\n',
            '都已经去了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B76')

    def _loc_1804(): pass

    label('loc_1804')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_1925',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1894',
    )

    ChrTalk(
        0x00FE,
        (
            '难道说，\n',
            '恐怖分子已经抓到了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是就算是这样，\n',
            '也要向我们通知一声啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……算了，光是想也没用，\n',
            '还是不要管了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1922')

    def _loc_1894(): pass

    label('loc_1894')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '哟，盘查已经解除了哦。\n',
            '到底是怎么回事啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '算了，我们这种小兵\n',
            '也不可能知道内幕的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管怎么说，\n',
            '累人的任务结束了不是正好吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1922(): pass

    label('loc_1922')

    Jump('loc_1B76')

    def _loc_1925(): pass

    label('loc_1925')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_19B0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1963',
    )

    ChrTalk(
        0x00FE,
        (
            '要是在这里徘徊的话\n',
            '说不定会被抓起来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19AD')

    def _loc_1963(): pass

    label('loc_1963')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '……啊，对不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '中央工房发生了一些事情，\n',
            '现在需要进行盘查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19AD(): pass

    label('loc_19AD')

    Jump('loc_1B76')

    def _loc_19B0(): pass

    label('loc_19B0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_1B26',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1A0C',
    )

    ChrTalk(
        0x00FE,
        (
            '如此雄伟的城墙\n',
            '竟然是在没有导力的时代建造的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是令人佩服啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B23')

    def _loc_1A0C(): pass

    label('loc_1A0C')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '这座建筑拥有非常悠久的历史。\n',
            '作为观光地也非常有名。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们每天都能看到，\n',
            '所以已经习以为常了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……但是，如此雄伟的城墙\n',
            '竟然是在没有导力的时代建造的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '哦哦，我这是怎么了！\n',
            '说着说着我又开始感叹了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B23(): pass

    label('loc_1B23')

    Jump('loc_1B76')

    def _loc_1B26(): pass

    label('loc_1B26')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_1B76',
    )

    ChrTalk(
        0x00FE,
        (
            '你们好，有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '队长就在这里面。\n',
            '遇到麻烦的话就去找他吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B76(): pass

    label('loc_1B76')

    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0x1B7A
@scena.Code('func_11_1B7A')
def func_11_1B7A():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_1BE8',
    )

    ChrTalk(
        0x00FE,
        (
            '从那以后，\n',
            '蔡斯那边就好像\n',
            '再没出现过恐怖事件了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '或许恐怖分子\n',
            '已经逃到别的地方去了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23AE')

    def _loc_1BE8(): pass

    label('loc_1BE8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1C46',
    )

    ChrTalk(
        0x00FE,
        (
            '决赛马上就要开始了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也是王国军的士兵，\n',
            '所以当然要去\n',
            '声援特务部队呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23AE')

    def _loc_1C46(): pass

    label('loc_1C46')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_1C9E',
    )

    ChrTalk(
        0x00FE,
        (
            '现在格兰赛尔的街上\n',
            '应该很热闹吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是能早点抓住\n',
            '恐怖分子就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23AE')

    def _loc_1C9E(): pass

    label('loc_1C9E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_1CFF',
    )

    ChrTalk(
        0x00FE,
        (
            '我也想参加一次武术大会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是不在军队的预选赛中胜出的话，\n',
            '就没有出场的资格。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23AE')

    def _loc_1CFF(): pass

    label('loc_1CFF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_1D52',
    )

    ChrTalk(
        0x00FE,
        (
            '唉呀，一直保持警戒状态，\n',
            '都快累死了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '肩膀已经酸痛得不行了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23AE')

    def _loc_1D52(): pass

    label('loc_1D52')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 6, 0x606)),
            Expr.Return,
        ),
        'loc_1DC5',
    )

    ChrTalk(
        0x00FE,
        (
            '那边的那个人\n',
            '是学者还是别的什么人呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个『亚宁堡』\n',
            '也是相当古老的遗迹，\n',
            '经常会有人来考察的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23AE')

    def _loc_1DC5(): pass

    label('loc_1DC5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 5, 0x605)),
            Expr.Return,
        ),
        'loc_1EF1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1E5F',
    )

    ChrTalk(
        0x00FE,
        (
            '之前我看见了一艘陌生的飞艇，\n',
            '于是就向队长汇报了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是上面的人\n',
            '好像什么反应也没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个果然是\n',
            '试飞中的新型艇之类的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1EEE')

    def _loc_1E5F(): pass

    label('loc_1E5F')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '上次看到了一艘\n',
            '样子很奇怪的飞艇，\n',
            '于是就向队长汇报了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是上面的人\n',
            '好像什么反应也没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，我还以为立了功。\n',
            '真是个傻瓜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1EEE(): pass

    label('loc_1EEE')

    Jump('loc_23AE')

    def _loc_1EF1(): pass

    label('loc_1EF1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_2010',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1F71',
    )

    ChrTalk(
        0x00FE,
        (
            '那艘没见过的飞艇\n',
            '向西边飞去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说起西边，\n',
            '那是雷斯顿要塞的方向……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说不定是在\n',
            '测试新型飞艇吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_200D')

    def _loc_1F71(): pass

    label('loc_1F71')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '昨天晚上，在西边的天空，\n',
            '我看见了一艘陌生的飞艇。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我觉得应该和事件有关系，\n',
            '就向队长汇报了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '盘查都已经解除了，\n',
            '以后说不定就不再搜查了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_200D(): pass

    label('loc_200D')

    Jump('loc_23AE')

    def _loc_2010(): pass

    label('loc_2010')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_2132',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_2087',
    )

    ChrTalk(
        0x00FE,
        (
            '要是让恐怖分子逃跑了，\n',
            '守备队的面子可就丢尽了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不能松懈的日子\n',
            '好像还要一直持续下去呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_212F')

    def _loc_2087(): pass

    label('loc_2087')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '感觉犯人随时会从这茂密的树林中蹿出来，\n',
            '真让人感到不安啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是让恐怖分子逃跑了，\n',
            '守备队的面子可就丢尽了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不能松懈的日子\n',
            '好像还要一直持续下去呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_212F(): pass

    label('loc_212F')

    Jump('loc_23AE')

    def _loc_2132(): pass

    label('loc_2132')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_2263',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_21B9',
    )

    ChrTalk(
        0x00FE,
        (
            '就因为每天\n',
            '都这样眺望地平线，\n',
            '眼力也变的太过敏锐了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因此经常让\n',
            '当地的朋友感到不愉快。\n',
            '这也是一种职业病吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2260')

    def _loc_21B9(): pass

    label('loc_21B9')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '我们不是每天\n',
            '都要这样眺望地平线吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正因如此，\n',
            '眼力也变的过于敏锐了。\n',
            '经常让当地的朋友感到不愉快。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这也是一种职业病吧。\n',
            '我们可不是在打什么坏主意哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2260(): pass

    label('loc_2260')

    Jump('loc_23AE')

    def _loc_2263(): pass

    label('loc_2263')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_23AE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_22C9',
    )

    ChrTalk(
        0x00FE,
        (
            '微风迎面吹来，心情真不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天的天气不错，\n',
            '连卡鲁迪亚丘陵也能清楚地看到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23AE')

    def _loc_22C9(): pass

    label('loc_22C9')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '今天的利贝尔王国也很和平啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果说哪里有问题的话，\n',
            '那就是和平过了头，都让人想睡觉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼啊啊啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 1700, 0x1C, 0x21, 0x000000FA, 0x00)
    Sleep(3000)

    OP_63(0x000B)
    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_62(0x000B, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x00FE,
        (
            '糟、糟了……\n',
            '都支撑不到交接班了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_23AE(): pass

    label('loc_23AE')

    TalkEnd(0x00FE)

    Return()

# id: 0x0012 offset: 0x23B2
@scena.Code('func_12_23B2')
def func_12_23B2():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_23BF',
    )

    Jump('loc_259C')

    def _loc_23BF(): pass

    label('loc_23BF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_23C9',
    )

    Jump('loc_259C')

    def _loc_23C9(): pass

    label('loc_23C9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_23D3',
    )

    Jump('loc_259C')

    def _loc_23D3(): pass

    label('loc_23D3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_244A',
    )

    ChrTalk(
        0x00FE,
        (
            '啊啊～真是幸福啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在环境这么优美的地方\n',
            '和最爱的人在一起……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊～眼前整个世界都在闪闪发光。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_259C')

    def _loc_244A(): pass

    label('loc_244A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_259C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_24B1',
    )

    ChrTalk(
        0x00FE,
        (
            '其实我完全不记得\n',
            '周游道的景色是什么样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，\n',
            '那是因为一直在注视着她嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_259C')

    def _loc_24B1(): pass

    label('loc_24B1')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '为了参观女王诞辰庆典，\n',
            '我们从洛连特旅行来到这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难得来一次，\n',
            '我就邀请她一起到艾尔贝周游道散步。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵呵，在美丽的树林中和她牵着手，\n',
            '只有两个人的世界……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000C, 0x00000000, 2000, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '啊啊，\n',
            '简直就像做梦一样啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_259C(): pass

    label('loc_259C')

    TalkEnd(0x00FE)

    Return()

# id: 0x0013 offset: 0x25A0
@scena.Code('func_13_25A0')
def func_13_25A0():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_25AD',
    )

    Jump('loc_27F4')

    def _loc_25AD(): pass

    label('loc_25AD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_25B7',
    )

    Jump('loc_27F4')

    def _loc_25B7(): pass

    label('loc_25B7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_25C1',
    )

    Jump('loc_27F4')

    def _loc_25C1(): pass

    label('loc_25C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_2690',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_261E',
    )

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '这座城墙真是好壮观啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和威尔特桥的关口\n',
            '简直是天壤之别。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_268D')

    def _loc_261E(): pass

    label('loc_261E')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '才刚刚开始交往就一起出来旅行，\n',
            '稍微感到有些不安……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，但是我相信他。\n',
            '跟着他一起来真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_268D(): pass

    label('loc_268D')

    Jump('loc_27F4')

    def _loc_2690(): pass

    label('loc_2690')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_27F4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_2705',
    )

    ChrTalk(
        0x00FE,
        (
            '和他在周游道上散步，\n',
            '那真是美丽的绿色小道啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们两个人简直像是\n',
            '进入了童话中的世界一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27F4')

    def _loc_2705(): pass

    label('loc_2705')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '和他在周游道上散步，\n',
            '那真是美丽的绿色小道啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '沉稳颜色的石头路，\n',
            '弥漫着历史氛围和浪漫感……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们两个人简直像是\n',
            '进入了童话中的世界一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2000, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '呀～就像是变成了苍骑士奥斯卡\n',
            '和塞茜莉亚公主一样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_27F4(): pass

    label('loc_27F4')

    TalkEnd(0x00FE)

    Return()

# id: 0x0014 offset: 0x27F8
@scena.Code('func_14_27F8')
def func_14_27F8():
    EventBegin(0x00)
    CameraMove(29440, 0, 4420, 0)
    OP_67(0, 9960, -10000, 0)
    CameraSetDistance(10000, 0)
    OP_6C(62000, 0)
    OP_6E(262, 0)
    OP_12(0x000088B8, 0x00061A80, 0x00000000)
    ChrSetPos(0x0101, -11860, 0, 1880, 0)
    ChrSetPos(0x0102, -11610, 0, 330, 0)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_2875')
    def lambda_2875():
        OP_6C(45000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2875)

    Sleep(1000)

    @scena.Lambda('lambda_288A')
    def lambda_288A():
        CameraMove(7000, 0, 4630, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_288A)

    Sleep(2000)

    @scena.Lambda('lambda_28A7')
    def lambda_28A7():
        ChrWalkTo(0x00FE, 1660, 0, 1510, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_28A7)

    Sleep(600)

    @scena.Lambda('lambda_28C7')
    def lambda_28C7():
        ChrWalkTo(0x00FE, 1660, 0, -200, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_28C7)

    WaitForThreadExit(0x0101, 0x0002)
    Fade(500)
    CameraMove(4040, 0, -300, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3250, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_12(0x000088B8, 0x000249F0, 0x00000000)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0102, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010100347V#006F#1P这里就是圣海姆门啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100348V总觉得看起来\n',
            '和洛连特地区的格鲁纳门很像。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0102, 0x0001)

    ChrTalk(
        0x0102,
        (
            '#0020100349V#010F#6P因为都是建在包围王都地区的\n',
            '长城『亚宁堡』上的门。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100350V虽然是一千年以前建造的，\n',
            '不过真不愧是阻止过帝国军队进攻的建筑，\n',
            '坚固得简直就像监牢围墙一般啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100351V#001F#1P嗯嗯，我也觉得是。\n',
            '看上去被大炮击中都不会损坏呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100352V#501F不过，这里也是观光胜地，\n',
            '如果有时间的话真想登上去看看啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100353V#503F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020100354V#019F#6P哈哈，如果是你的话，\n',
            '一定是想沿着城墙一直全力奔跑下去吧？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrTurnDirection(0x0101, 0x0102, 600)

    ChrTalk(
        0x0101,
        (
            '#0010100355V#005F#1P才，才不是呢！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100356V#503F我想的是……\n',
            '两个人坐在上面慢慢地吃午饭……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100357V或者吹着风……\n',
            '谈些各种各样的话题之类的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100358V#010F#6P？？？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100359V为什么突然想起\n',
            '这些平时经常做的事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1200)

    ChrTalk(
        0x0101,
        (
            '#0010100360V#007F#1P唉……算了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100361V总之快点办完通行手续，\n',
            '加快脚步去王都吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100362V#014F#6P嗯……\n',
            '是我神经过敏吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100363V你是不是心情不好啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100364V#509F#1P的确是你神经过敏。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100365V哎呀～别再说无谓的话了。\n',
            '赶、赶快进去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020100366V#017F#6P（女孩子真是难懂啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x0015 offset: 0x2DED
@scena.Code('func_15_2DED')
def func_15_2DED():
    TalkBegin(0x00FF)
    Sleep(400)

    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

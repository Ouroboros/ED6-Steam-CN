import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T2511_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2511   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2511.x'
    header.mapIndex       = 1
    header.bgm            = 14
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
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
        ('ED6_DT07/CH02390._CH', 'ED6_DT07/CH02390P._CP'),
        ('ED6_DT07/CH02550._CH', 'ED6_DT07/CH02550P._CP'),
        ('ED6_DT27/CH03004._CH', 'ED6_DT27/CH03004P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH01360._CH', 'ED6_DT07/CH01360P._CP'),
        ('ED6_DT07/CH01590._CH', 'ED6_DT07/CH01590P._CP'),
        ('ED6_DT07/CH01080._CH', 'ED6_DT07/CH01080P._CP'),
        ('ED6_DT06/CH20063._CH', 'ED6_DT06/CH20063P._CP'),
        ('ED6_DT06/CH20064._CH', 'ED6_DT06/CH20064P._CP'),
        ('ED6_DT07/CH01580._CH', 'ED6_DT07/CH01580P._CP'),
        ('ED6_DT07/CH01370._CH', 'ED6_DT07/CH01370P._CP'),
        ('ED6_DT26/CH20396._CH', 'ED6_DT26/CH20396P._CP'),
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
        ('ED6_DT07/CH01660._CH', 'ED6_DT07/CH01660P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH01430._CH', 'ED6_DT07/CH01430P._CP'),
        ('ED6_DT07/CH01090._CH', 'ED6_DT07/CH01090P._CP'),
    ]

# id: 0x10001 offset: 0x132
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '乔儿',
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
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0016,
        ),
        ScenaNpcData(
            name                = '汉斯',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
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
            name                = '德波拉',
            x                   = 3500,
            z                   = 0,
            y                   = 4500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '罗迪',
            x                   = -31990,
            z                   = 0,
            y                   = 26660,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '莉秋儿',
            x                   = 29790,
            z                   = 0,
            y                   = 29100,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '米克',
            x                   = 5350,
            z                   = 0,
            y                   = -2630,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '朵洛希',
            x                   = 3450,
            z                   = 0,
            y                   = 240,
            direction           = 0,
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
            name                = '罗伊斯',
            x                   = -28450,
            z                   = 0,
            y                   = 27900,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '莫妮卡',
            x                   = 27930,
            z                   = 0,
            y                   = 28500,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '艾福托老师',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '拉迪奥老师',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '碧欧拉老师',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '米丽亚老师',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '黛拉',
            x                   = 30410,
            z                   = 0,
            y                   = 25950,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0017,
        ),
        ScenaNpcData(
            name                = '强化猎兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '强化猎兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '强化猎兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '强化猎兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '强化猎兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '强化猎兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '帕布尔',
            x                   = -31760,
            z                   = 0,
            y                   = 58850,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
    )

# id: 0x10002 offset: 0x3F2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x3F2
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -2200,
            y           = 0,
            z           = 50000,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000003B,
        ),
        ScenaEventData(
            x           = -2200,
            y           = 0,
            z           = 42000,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000003C,
        ),
        ScenaEventData(
            x           = 2130,
            y           = 0,
            z           = 42010,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000003D,
        ),
        ScenaEventData(
            x           = 2200,
            y           = 0,
            z           = 50000,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000003E,
        ),
    )

# id: 0x10004 offset: 0x472
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 3060,
            triggerZ            = 0,
            triggerY            = 2500,
            triggerRange        = 400,
            actorX              = 3500,
            actorZ              = 1500,
            actorY              = 4500,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x496
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_509',
    )

    ChrSetPos(0x0009, 30280, 0, 53800, 0)
    ChrSetPos(0x0008, 30850, 0, 55200, 270)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    CreateThread(0x0008, 0x00, 0x06, func_02_81A)
    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x0010, 5350, 0, -10, 0)
    ChrClearFlags(0x0016, 0x0080)
    ChrSetPos(0x0016, 31330, 0, 24430, 164)

    Jump('loc_69C')

    def _loc_509(): pass

    label('loc_509')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 7, 0x201F)),
            Expr.Return,
        ),
        'loc_5F0',
    )

    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x0010, 0x0080)
    ChrSetPos(0x0012, -31080, 0, 27210, 90)
    ChrClearFlags(0x0012, 0x0080)
    ChrSetPos(0x0013, -31090, 0, 25690, 90)
    ChrClearFlags(0x0013, 0x0080)
    ChrSetFlags(0x0011, 0x0080)
    ChrSetPos(0x0014, 30390, 0, 27920, 180)
    ChrClearFlags(0x0014, 0x0080)
    ChrSetPos(0x0015, 30980, 0, 26960, 270)
    ChrClearFlags(0x0015, 0x0080)
    ChrSetPos(0x000B, 30510, 0, 25690, 0)
    ChrClearFlags(0x000B, 0x0080)
    ChrSetFlags(0x000E, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0404, 1, 0x2021)),
            Expr.Return,
        ),
        'loc_5ED',
    )

    ChrClearFlags(0x0017, 0x0001)
    ChrSetFlags(0x0017, 0x0002)
    ChrSetChipByIndex(0x0017, 18)
    ChrSetSubChip(0x0017, 8)
    ChrClearFlags(0x0018, 0x0001)
    ChrSetFlags(0x0018, 0x0002)
    ChrSetChipByIndex(0x0018, 18)
    ChrSetSubChip(0x0018, 11)
    ChrSetPos(0x0017, 1340, 0, 39800, 0)
    ChrSetPos(0x0018, -2270, 0, 40010, 0)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0018, 0x0080)

    def _loc_5ED(): pass

    label('loc_5ED')

    Jump('loc_69C')

    def _loc_5F0(): pass

    label('loc_5F0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_61F',
    )

    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrClearFlags(0x001D, 0x0080)
    ChrSetPos(0x0011, 31110, 0, 53120, 90)

    Jump('loc_69C')

    def _loc_61F(): pass

    label('loc_61F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 2, 0x1222)),
            Expr.Return,
        ),
        'loc_646',
    )

    ChrSetPos(0x0008, 1400, 0, -2100, 180)
    ChrClearFlags(0x0008, 0x0080)
    CreateThread(0x0008, 0x00, 0x06, func_02_81A)

    Jump('loc_69C')

    def _loc_646(): pass

    label('loc_646')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 1, 0x1221)),
            Expr.Return,
        ),
        'loc_655',
    )

    ChrClearFlags(0x000E, 0x0080)

    Jump('loc_69C')

    def _loc_655(): pass

    label('loc_655')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 6, 0x121E)),
            Expr.Return,
        ),
        'loc_69C',
    )

    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, -28500, 0, 58160, 90)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0246, 3, 0x1233)),
            Expr.Return,
        ),
        'loc_697',
    )

    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, 5350, 0, -2630, 0)

    Jump('loc_69C')

    def _loc_697(): pass

    label('loc_697')

    ChrSetFlags(0x000E, 0x0080)

    def _loc_69C(): pass

    label('loc_69C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_6B2',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    Event(0, func_18_2EB0)

    Jump('loc_772')

    def _loc_6B2(): pass

    label('loc_6B2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_6D1',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x51),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    MapSetFlags(0x10000000)
    Event(0, func_20_58E4)

    Jump('loc_772')

    def _loc_6D1(): pass

    label('loc_6D1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Return,
        ),
        'loc_6E7',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    MapSetFlags(0x10000000)
    Event(0, func_21_5BA0)

    Jump('loc_772')

    def _loc_6E7(): pass

    label('loc_6E7')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000067, 'loc_6FF'),
        (0x0000006C, 'loc_712'),
        (0x0000006E, 'loc_742'),
        (0x0000006F, 'loc_75A'),
        (-1, 'loc_772'),
    )

    def _loc_6FF(): pass

    label('loc_6FF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 7, 0x201F)),
            (Expr.TestScenaFlags, ScenaFlag(0x0404, 1, 0x2021)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_70F',
    )

    Event(0, func_24_5DA0)

    def _loc_70F(): pass

    label('loc_70F')

    Jump('loc_772')

    def _loc_712(): pass

    label('loc_712')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            (Expr.TestScenaFlags, ScenaFlag(0x0418, 0, 0x20C0)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_72A',
    )

    MapSetFlags(0x10000000)
    Event(0, func_11_2171)

    Jump('loc_73F')

    def _loc_72A(): pass

    label('loc_72A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 1, 0x1221)),
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 2, 0x1222)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_73F',
    )

    MapSetFlags(0x10000000)
    Event(0, func_1D_4704)

    def _loc_73F(): pass

    label('loc_73F')

    Jump('loc_772')

    def _loc_742(): pass

    label('loc_742')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 7, 0x201F)),
            (Expr.TestScenaFlags, ScenaFlag(0x0404, 2, 0x2022)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_757',
    )

    MapSetFlags(0x10000000)
    Event(0, func_2F_638A)

    def _loc_757(): pass

    label('loc_757')

    Jump('loc_772')

    def _loc_75A(): pass

    label('loc_75A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 7, 0x201F)),
            (Expr.TestScenaFlags, ScenaFlag(0x0404, 3, 0x2023)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_76F',
    )

    MapSetFlags(0x10000000)
    Event(0, func_34_69CC)

    def _loc_76F(): pass

    label('loc_76F')

    Jump('loc_772')

    def _loc_772(): pass

    label('loc_772')

    Return()

# id: 0x0001 offset: 0x773
@scena.Code('func_01_773')
def func_01_773():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_77D',
    )

    Jump('loc_7C1')

    def _loc_77D(): pass

    label('loc_77D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 7, 0x201F)),
            Expr.Return,
        ),
        'loc_79C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0404, 1, 0x2021)),
            Expr.Return,
        ),
        'loc_795',
    )

    LoadChip('ED6_DT26/CH20501._CH', 'ED6_DT26/CH20501P._CP', 18)

    def _loc_795(): pass

    label('loc_795')

    OP_64(0x00, 0x0001)

    Jump('loc_7C1')

    def _loc_79C(): pass

    label('loc_79C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_7A6',
    )

    Jump('loc_7C1')

    def _loc_7A6(): pass

    label('loc_7A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 2, 0x1222)),
            Expr.Return,
        ),
        'loc_7B0',
    )

    Jump('loc_7C1')

    def _loc_7B0(): pass

    label('loc_7B0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 1, 0x1221)),
            Expr.Return,
        ),
        'loc_7BA',
    )

    Jump('loc_7C1')

    def _loc_7BA(): pass

    label('loc_7BA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 6, 0x121E)),
            Expr.Return,
        ),
        'loc_7C1',
    )

    def _loc_7C1(): pass

    label('loc_7C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 1, 0x1221)),
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7D9',
    )

    OP_B1('t2511_y')

    Jump('loc_7E2')

    def _loc_7D9(): pass

    label('loc_7D9')

    OP_B1('t2511_n')

    def _loc_7E2(): pass

    label('loc_7E2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_7EC',
    )

    Jump('loc_819')

    def _loc_7EC(): pass

    label('loc_7EC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 7, 0x201F)),
            Expr.Return,
        ),
        'loc_804',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x59),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x02000000)

    Jump('loc_819')

    def _loc_804(): pass

    label('loc_804')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 3, 0x2013)),
            Expr.Return,
        ),
        'loc_819',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x6E),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x02000000)

    def _loc_819(): pass

    label('loc_819')

    Return()

# id: 0x0002 offset: 0x81A
@scena.Code('func_02_81A')
def func_02_81A():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 1, 0x1221)),
            Expr.Return,
        ),
        'loc_822',
    )

    Return()

    def _loc_822(): pass

    label('loc_822')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x64),
            Expr.Equ,
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x65),
            Expr.Equ,
            Expr.Or,
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x66),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_843',
    )

    Jump('loc_844')

    def _loc_843(): pass

    label('loc_843')

    Return()

    def _loc_844(): pass

    label('loc_844')

    LoadEffect(0x00, 'map\\\\mp032_00.eff')
    def _loc_858(): pass

    label('loc_858')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_92C',
    )

    OP_8D(0x00FE, 2050, 280, 6480, 1790, 2000)

    ExecExpressionWithReg(
        0x0002,
        (
            Expr.Rand,
            (Expr.PushLong, 0x8),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x2),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_924',
    )

    ChrTurnDirectionByPos(0x00FE, 3770, 3960, 400)
    Sleep(400)

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    ChrSetChipByIndex(0x00FE, 8)
    Sleep(2000)

    def _loc_8B0(): pass

    label('loc_8B0')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_917',
    )

    PlaySE(124, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x000F, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)

    ExecExpressionWithReg(
        0x0002,
        (
            Expr.Rand,
            (Expr.PushLong, 0x8),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(800)

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_914',
    )

    Jump('loc_917')

    def _loc_914(): pass

    label('loc_914')

    Jump('loc_8B0')

    def _loc_917(): pass

    label('loc_917')

    Sleep(600)

    ChrSetChipByIndex(0x00FE, 7)
    ClearScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    def _loc_924(): pass

    label('loc_924')

    Sleep(400)

    Jump('loc_858')

    def _loc_92C(): pass

    label('loc_92C')

    Return()

# id: 0x0003 offset: 0x92D
@scena.Code('func_03_92D')
def func_03_92D():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_98E',
    )

    ChrTalk(
        0x00FE,
        (
            '听说旧校舍\n',
            '潜伏着可疑的人物？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然有点可怕……\n',
            '不过倒是很能激发想象力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A29')

    def _loc_98E(): pass

    label('loc_98E')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '刚才\n',
            '碰巧听说了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听说旧校舍\n',
            '潜伏着可疑的人物？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是令人吃惊啊。\n',
            '简直像小说中的情节呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也许有些不谨慎，\n',
            '但想象力马上被激起了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A29(): pass

    label('loc_A29')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0xA2D
@scena.Code('func_04_A2D')
def func_04_A2D():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 1, 0x1221)),
            Expr.Return,
        ),
        'loc_AB1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_A64',
    )

    ChrTalk(
        0x00FE,
        (
            '啊啊～今天又是\n',
            '劳累的一天啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AAE')

    def _loc_A64(): pass

    label('loc_A64')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '哟，你们的调查有进展吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '忙到现在还没吃饭吗？\n',
            '还真是辛苦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AAE(): pass

    label('loc_AAE')

    Jump('loc_AF4')

    def _loc_AB1(): pass

    label('loc_AB1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 6, 0x121E)),
            Expr.Return,
        ),
        'loc_AF4',
    )

    ChrTalk(
        0x00FE,
        (
            '那么、今天要吃什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还是和平时一样吃套餐吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AF4(): pass

    label('loc_AF4')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0xAF8
@scena.Code('func_05_AF8')
def func_05_AF8():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_B9A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_B47',
    )

    ChrTalk(
        0x00FE,
        (
            '乔儿她们好像\n',
            '是去什么地方了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听说是学生会有事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B97')

    def _loc_B47(): pass

    label('loc_B47')

    ChrTalk(
        0x00FE,
        (
            '啊，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '乔儿她们好像\n',
            '是去什么地方了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听说是学生会有事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    def _loc_B97(): pass

    label('loc_B97')

    Jump('loc_E7D')

    def _loc_B9A(): pass

    label('loc_B9A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 1, 0x1221)),
            Expr.Return,
        ),
        'loc_BE9',
    )

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，从明天起\n',
            '社团活动又要开始了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '终于可以再次拉弓了啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E7D')

    def _loc_BE9(): pass

    label('loc_BE9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 6, 0x121E)),
            Expr.Return,
        ),
        'loc_E7D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_C36',
    )

    ChrTalk(
        0x00FE,
        (
            '喂，喂？\n',
            '发生了什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '喂～好不好嘛？\n',
            '告诉我吧～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E7D')

    def _loc_C36(): pass

    label('loc_C36')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0246, 5, 0x1235)),
            Expr.Return,
        ),
        'loc_C89',
    )

    ChrTalk(
        0x00FE,
        (
            '考试期间的奇异事件，\n',
            '好像很有意思的样子啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最后到底怎么样啦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E7D')

    def _loc_C89(): pass

    label('loc_C89')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))
    SetScenaFlags(ScenaFlag(0x0246, 5, 0x1235))
    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x0101,
        (
            '#1000F那个，现在方便吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1002F嗯，想请教你一些事情…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔表示自己正在调查\n',
            '考试期间发生的奇异事件。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x00FE,
        (
            '考试期间的奇异事件吗～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '那是什么？很有趣的样子啊！\n',
            '喂～到底发生什么事了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#1019F这、这种反应……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#045F总、总之\n',
            '你是没发现什么对吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#1007F去找别人问问吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎，到底是怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '喂～好不好嘛？\n',
            '告诉我吧～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E7D(): pass

    label('loc_E7D')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0xE81
@scena.Code('func_06_E81')
def func_06_E81():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_F3E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_EF7',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，大家也来吃饭吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我经常会\n',
            '忽然觉得肚子饿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈，身体果然是\n',
            '最诚实的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    Jump('loc_F3B')

    def _loc_EF7(): pass

    label('loc_EF7')

    ChrTalk(
        0x00FE,
        (
            '总是忽然就觉得\n',
            '肚子很饿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈，身体果然是\n',
            '最诚实的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F3B(): pass

    label('loc_F3B')

    Jump('loc_137C')

    def _loc_F3E(): pass

    label('loc_F3E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_1061',
    )

    ChrTurnDirection(0x00FE, 0x0105, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_FA0',
    )

    ChrTalk(
        0x00FE,
        (
            '和科洛丝的对战\n',
            '要等到开学以后了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我要抓紧时间\n',
            '加强特训才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_105E')

    def _loc_FA0(): pass

    label('loc_FA0')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '听说科洛丝要开始\n',
            '放假了是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本来还期待和你对战呢，\n',
            '真是遗憾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#045F抱歉哦，罗伊斯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '这场比赛就等到\n',
            '我回来之后吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈，没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我会加强特训，\n',
            '到时和你一战！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_105E(): pass

    label('loc_105E')

    Jump('loc_137C')

    def _loc_1061(): pass

    label('loc_1061')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 1, 0x1221)),
            Expr.Return,
        ),
        'loc_10F3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_109E',
    )

    ChrTurnDirection(0x00FE, 0x0105, 0)

    ChrTalk(
        0x00FE,
        (
            '科洛丝，\n',
            '到时还请你手下留情了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10F0')

    def _loc_109E(): pass

    label('loc_109E')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '明天起\n',
            '又要开始在击剑部\n',
            '进行锻炼了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '趁现在赶快先\n',
            '检查一下用具吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10F0(): pass

    label('loc_10F0')

    Jump('loc_137C')

    def _loc_10F3(): pass

    label('loc_10F3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 6, 0x121E)),
            Expr.Return,
        ),
        'loc_137C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0246, 0, 0x1230)),
            Expr.Return,
        ),
        'loc_1152',
    )

    ChrTalk(
        0x00FE,
        (
            '考试期间没有发生什么\n',
            '特别的事情哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也没听说过什么\n',
            '值得注意的传闻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_137C')

    def _loc_1152(): pass

    label('loc_1152')

    SetScenaFlags(ScenaFlag(0x0246, 0, 0x1230))
    ChrTurnDirection(0x00FE, 0x0105, 0)

    ChrTalk(
        0x00FE,
        (
            '啊、科洛丝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '科洛丝也来\n',
            '准备社团活动吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F不…很可惜，\n',
            '现在没时间顾那个了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '现在有点事，\n',
            '正在校园内进行调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎，怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1002F嗯，是这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔表示自己正在调查\n',
            '考试期间发生的奇异事件。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '奇异的事件吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '很遗憾，\n',
            '记忆里好象没有什么特别的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '类似的传闻\n',
            '也从来没听过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F嗯、是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '算了，那也没办法。\n',
            '去问问其他人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没帮上忙，真对不起啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F哪里的话，不用介意啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那么，多谢帮忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哪里，没有的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_137C(): pass

    label('loc_137C')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x1380
@scena.Code('func_07_1380')
def func_07_1380():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x024C, 3, 0x1263)),
            Expr.Return,
        ),
        'loc_13EF',
    )

    ChrTalk(
        0x000F,
        (
            '#0280210969V#150F好～接下来\n',
            '要拍菜单了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280210970V嗯～上面的食物看起来都很美味的样子呢⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14F8')

    def _loc_13EF(): pass

    label('loc_13EF')

    SetScenaFlags(ScenaFlag(0x024C, 3, 0x1263))
    ChrTurnDirection(0x000F, 0x0101, 0)
    ChrSetChipByIndex(0x00FE, 7)
    ChrClearFlags(0x00FE, 0x0010)

    ChrTalk(
        0x0101,
        (
            '#0010210971V#1011F啊，朵洛希。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210972V在这种地方做什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0280210973V#150F在拍摄食堂的风景啦⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280210974V我拍了很多可爱的照片呢～\n',
            '#151F嘿嘿嘿～来笑一个吧～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210975V#1007F（真、真没办法……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00FE, 0, 0)
    ChrSetFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_14F8',
    )

    ChrSetChipByIndex(0x00FE, 8)

    def _loc_14F8(): pass

    label('loc_14F8')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x14FC
@scena.Code('func_08_14FC')
def func_08_14FC():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_153A',
    )

    ChrTalk(
        0x00FE,
        (
            '啊啊～今天就要和前辈分别了，\n',
            '还真是寂寞呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_162D')

    def _loc_153A(): pass

    label('loc_153A')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    ChrTurnDirection(0x00FE, 0x0105, 0)

    ChrTalk(
        0x00FE,
        (
            '啊！科洛丝前辈！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呜～真遗憾，本来还想\n',
            '一起参加社团活动呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#045F对不起啊～莉秋儿。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '等我的休假结束之后\n',
            '再和你一起努力吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，说好了哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也会继续练习，\n',
            '努力练得更强的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#041F嗯，那我就期待你的表现啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_162D(): pass

    label('loc_162D')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x1631
@scena.Code('func_09_1631')
def func_09_1631():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_170C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_16D2',
    )

    ChrTalk(
        0x00FE,
        (
            '游击士果然厉害啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近这种感觉\n',
            '更加强烈了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '艾丝蒂尔和约修亚\n',
            '都很了不起呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也希望自己将来\n',
            '可以从事这么棒的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_1709')

    def _loc_16D2(): pass

    label('loc_16D2')

    ChrTalk(
        0x00FE,
        (
            '游击士果然厉害啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近这种感觉\n',
            '更加强烈了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1709(): pass

    label('loc_1709')

    Jump('loc_17E0')

    def _loc_170C(): pass

    label('loc_170C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_175B',
    )

    ChrTalk(
        0x00FE,
        (
            '从今天开始又有社团活动了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '赶快做事前准备，\n',
            '占个好地方吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17E0')

    def _loc_175B(): pass

    label('loc_175B')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '从今天开始又有社团活动了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '赶快做事前准备，\n',
            '占个好地方吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这一阵一直在准备考前复习，\n',
            '真担心自己的射术已经退步了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17E0(): pass

    label('loc_17E0')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x17E4
@scena.Code('func_0A_17E4')
def func_0A_17E4():
    Call(0, 0x000B)

    Return()

# id: 0x000B offset: 0x17E9
@scena.Code('func_0B_17E9')
def func_0B_17E9():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0404, 3, 0x2023)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1893',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1860',
    )

    ChrTalk(
        0x000B,
        (
            '帮助别人当然很好，\n',
            '但自己也一定要小心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '不要抓狼反被狼咬，\n',
            '连自己的命都搭上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_188F')

    def _loc_1860(): pass

    label('loc_1860')

    ChrTalk(
        0x000B,
        (
            '帮助别人当然很好，\n',
            '但自己也一定要小心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_188F(): pass

    label('loc_188F')

    TalkEnd(0x000B)

    Return()

    def _loc_1893(): pass

    label('loc_1893')

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
            TXT(0x00, '对话\n'),
            TXT(0x01, '买东西\n'),
            TXT(0x02, '招牌菜『大小姐料理』　800米拉\n'),
            TXT(0x03, '离开\n'),
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
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_190C',
    )

    FadeIn(300, 0)
    OP_0D()
    OP_A9(0x72)
    OP_56(0x00)
    TalkEnd(0x000B)

    Return()

    def _loc_190C(): pass

    label('loc_190C')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A16',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x12),
            (Expr.PushLong, 0x320),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_19E1',
    )

    RemoveMira(800)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    PlaySE(11, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x2),
            '大小姐料理',
            (TxtCtl.SetColor, 0x0),
            '已经品尝过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetStatus(ChrTable['艾丝蒂尔'], 0xFD, 1200)
    ChrSetStatus(ChrTable['约修亚'], 0xFD, 1200)
    ChrSetStatus(ChrTable['雪拉扎德'], 0xFD, 1200)
    ChrSetStatus(ChrTable['奥利维尔'], 0xFD, 1200)
    ChrSetStatus(ChrTable['科洛丝'], 0xFD, 1200)
    ChrSetStatus(ChrTable['阿加特'], 0xFD, 1200)
    ChrSetStatus(ChrTable['提妲'], 0xFD, 1200)
    ChrSetStatus(ChrTable['金'], 0xFD, 1200)
    ChrSetStatus(ChrTable['凯文神父'], 0xFD, 1200)

    If(
        (
            (Expr.Eval, "OP_40(0x020D, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_19D3',
    )

    If(
        (
            (Expr.Eval, "OP_AC(0x0009)"),
            Expr.Return,
        ),
        'loc_19A9',
    )

    Jump('loc_19D3')

    def _loc_19A9(): pass

    label('loc_19A9')

    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            TxtCtl.ShowAll,
            (TxtCtl.SetColor, 0x2),
            '大小姐料理',
            (TxtCtl.SetColor, 0x0),
            '的做法已经学会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19D3(): pass

    label('loc_19D3')

    OP_56(0x00)
    FadeIn(1000, 0)

    Jump('loc_1A07')

    def _loc_19E1(): pass

    label('loc_19E1')

    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            '没有足够的米拉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeIn(300, 0)
    def _loc_1A07(): pass

    label('loc_1A07')

    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x000B)

    Return()

    def _loc_1A16(): pass

    label('loc_1A16')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A30',
    )

    FadeIn(300, 0)
    TalkEnd(0x000B)

    Return()

    def _loc_1A30(): pass

    label('loc_1A30')

    FadeIn(300, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_1AD2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A83',
    )

    ChrTalk(
        0x000B,
        (
            '呀，是你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '肚子饿了吧？\n',
            '来吃些东西吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_1ACF')

    def _loc_1A83(): pass

    label('loc_1A83')

    ChrTalk(
        0x000B,
        (
            '虽然没有导力器了，\n',
            '但还是可以制作料理的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '这就是\n',
            '家庭主妇的智慧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1ACF(): pass

    label('loc_1ACF')

    Jump('loc_1C25')

    def _loc_1AD2(): pass

    label('loc_1AD2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_1B31',
    )

    ChrTalk(
        0x000B,
        (
            '哈哈、学院也马上要放假了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '一到这个时候，学生们的表情\n',
            '马上变得开朗起来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C25')

    def _loc_1B31(): pass

    label('loc_1B31')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 1, 0x1221)),
            Expr.Return,
        ),
        'loc_1BE9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1B92',
    )

    ChrTalk(
        0x000B,
        (
            '考试结束之后\n',
            '接下来就是社团活动的季节了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '要多锻炼身体，\n',
            '多吃东西啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BE6')

    def _loc_1B92(): pass

    label('loc_1B92')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000B,
        (
            '阶段考试\n',
            '终于结束了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '这段时间大家\n',
            '都是早起晚睡，\n',
            '真担心他们的健康。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1BE6(): pass

    label('loc_1BE6')

    Jump('loc_1C25')

    def _loc_1BE9(): pass

    label('loc_1BE9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 6, 0x121E)),
            Expr.Return,
        ),
        'loc_1C25',
    )

    ChrTalk(
        0x000B,
        (
            '考试辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '肚子也饿了吧？\n',
            '来点些什么吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C25(): pass

    label('loc_1C25')

    TalkEnd(0x000B)

    Return()

# id: 0x000C offset: 0x1C29
@scena.Code('func_0C_1C29')
def func_0C_1C29():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_1CA0',
    )

    ChrTalk(
        0x0009,
        (
            '#0520210954V#731F全部解决好以后\n',
            '再来学校食堂吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520210955V#730F那么、你们两个\n',
            '接下来也要小心啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F0A')

    def _loc_1CA0(): pass

    label('loc_1CA0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0245, 2, 0x122A)),
            Expr.Return,
        ),
        'loc_1DC8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1D14',
    )

    ChrTalk(
        0x0009,
        (
            '#0520210956V#730F听说旧校舍是\n',
            '由古老的城塞改建的，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520210957V即使有秘密地下室\n',
            '也不奇怪吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DC5')

    def _loc_1D14(): pass

    label('loc_1D14')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x0009,
        (
            '#0520210958V#730F隐藏的楼梯吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520210959V资料中也没有\n',
            '记载那些东西啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520210960V只是听说旧校舍是\n',
            '以前的城塞改建的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520210961V即使有秘密地下室\n',
            '也很正常吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1DC5(): pass

    label('loc_1DC5')

    Jump('loc_1F0A')

    def _loc_1DC8(): pass

    label('loc_1DC8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 2, 0x1222)),
            Expr.Return,
        ),
        'loc_1E22',
    )

    ChrTalk(
        0x0009,
        (
            '#0520210962V#730F我在这种时候\n',
            '先在原地待命吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520210963V一定要小心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F0A')

    def _loc_1E22(): pass

    label('loc_1E22')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 7, 0x121F)),
            Expr.Return,
        ),
        'loc_1F03',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_1E80',
    )

    ChrTalk(
        0x0009,
        (
            '#0520210964V#730F耽误你们的时间了，真抱歉，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520210951V请继续调查吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F00')

    def _loc_1E80(): pass

    label('loc_1E80')

    ChrTalk(
        0x0009,
        (
            '#0520210966V#730F调查已经结束了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520210967V我这边的调查很顺利呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520210968V资料也不太多，\n',
            '一会儿就可以全部完成。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F00(): pass

    label('loc_1F00')

    Jump('loc_1F0A')

    def _loc_1F03(): pass

    label('loc_1F03')

    Call(0, 0x001C)
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    def _loc_1F0A(): pass

    label('loc_1F0A')

    TalkEnd(0x0009)

    Return()

# id: 0x000D offset: 0x1F0E
@scena.Code('func_0D_1F0E')
def func_0D_1F0E():
    TalkBegin(0x0012)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0404, 2, 0x2022)),
            Expr.Return,
        ),
        'loc_1F9B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1F70',
    )

    ChrTalk(
        0x00FE,
        (
            '自己什么也做不了，\n',
            '真是很不好意思……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过学生们的事\n',
            '就拜托了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    Jump('loc_1F9B')

    def _loc_1F70(): pass

    label('loc_1F70')

    ChrTalk(
        0x00FE,
        (
            '自己什么也做不了，\n',
            '真是很不好意思……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F9B(): pass

    label('loc_1F9B')

    TalkEnd(0x0012)

    Return()

# id: 0x000E offset: 0x1F9F
@scena.Code('func_0E_1F9F')
def func_0E_1F9F():
    TalkBegin(0x0013)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0404, 2, 0x2022)),
            Expr.Return,
        ),
        'loc_2057',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_202E',
    )

    ChrTalk(
        0x00FE,
        (
            '那么，有关学生们的事\n',
            '就请多关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是有什么情况，\n',
            '随时可以来和我说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们也会尽自己所能\n',
            '协助你们的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    Jump('loc_2057')

    def _loc_202E(): pass

    label('loc_202E')

    ChrTalk(
        0x00FE,
        (
            '那么，有关学生们的事\n',
            '就请多关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2057(): pass

    label('loc_2057')

    TalkEnd(0x0013)

    Return()

# id: 0x000F offset: 0x205B
@scena.Code('func_0F_205B')
def func_0F_205B():
    TalkBegin(0x0014)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0404, 3, 0x2023)),
            Expr.Return,
        ),
        'loc_20DF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_20B6',
    )

    ChrTalk(
        0x00FE,
        (
            '学生们的事……\n',
            '就请你们多多关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们也不要太勉强啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    Jump('loc_20DF')

    def _loc_20B6(): pass

    label('loc_20B6')

    ChrTalk(
        0x00FE,
        (
            '学生们的事……\n',
            '就请你们多多关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_20DF(): pass

    label('loc_20DF')

    TalkEnd(0x0014)

    Return()

# id: 0x0010 offset: 0x20E3
@scena.Code('func_10_20E3')
def func_10_20E3():
    TalkBegin(0x0015)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0404, 3, 0x2023)),
            Expr.Return,
        ),
        'loc_216D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2142',
    )

    ChrTalk(
        0x00FE,
        (
            '外边好像还是很危险……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们就在这里等待吧。\n',
            '学生们就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    Jump('loc_216D')

    def _loc_2142(): pass

    label('loc_2142')

    ChrTalk(
        0x00FE,
        (
            '我们就在这里等待吧。\n',
            '学生们就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_216D(): pass

    label('loc_216D')

    TalkEnd(0x0015)

    Return()

# id: 0x0011 offset: 0x2171
@scena.Code('func_11_2171')
def func_11_2171():
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
        'loc_2188',
    )

    Call(0, 0x0039)
    Call(0, 0x003A)

    def _loc_2188(): pass

    label('loc_2188')

    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x00F8, 0x0080)
    ChrSetFlags(0x00F9, 0x0080)
    OP_4A(0x0008, 255)
    OP_4A(0x0009, 255)
    ChrTurnDirection(0x0008, 0x0009, 0)
    CameraMove(31390, 0, 55630, 0)
    OP_67(0, 5510, -10000, 0)
    CameraSetDistance(2810, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    PlaySE(6, 0x00, 0x64)
    Sleep(500)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_223F')
    def lambda_223F():
        CameraMove(29500, 0, 55100, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_223F)

    CreateThread(0x0101, 0x01, 0x00, func_13_2B4B)
    CreateThread(0x0102, 0x01, 0x00, func_12_2AFC)
    CreateThread(0x00F8, 0x01, 0x00, func_15_2BF3)
    CreateThread(0x00F9, 0x01, 0x00, func_14_2B9F)
    ChrSetDirection(0x0009, 270, 400)
    ChrSetDirection(0x0008, 270, 400)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0008,
        (
            '#0510361192V#648F#5P啊，来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520361193V#731F#2P哟，二位辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010361194V#1016F#6P嘿嘿嘿，久等了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020361195V#1040F#6P汉斯你们\n',
            '已经很累了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520361196V#730F#2P什么话啊，\n',
            '我们只是在原地等而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510361197V#644F#5P那种程度都承受不住的话，\n',
            '哪还有资格当学生会委员嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510361198V#645F算了，真正的麻烦事\n',
            '从现在才开始呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020361199V#1035F#6P……确实如此呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020361200V#1043F要在这样的情况下\n',
            '迎接新学期吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010361201V#1004F#6P啊，想想的话确实呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010361202V#1015F……校园生活没问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520361203V#735F#2P也许吧…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520361204V#730F总之我们学生会\n',
            '也要好好思考对策。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510361205V#644F#5P毕竟是我们自己的学校啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510361206V总要尽可能做些\n',
            '力所能及的事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510361207V#648F而且，我们可不想输给你们，\n',
            '还有在王都努力的科洛丝啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010361208V#1017F#6P是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520361209V#731F#2P等你们闲下来的时候\n',
            '还要再来学院玩啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520361210V到时科洛丝也要一起来，\n',
            '咱们在食堂开个联欢会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510361211V#641F#5P还可以穿上舞台服，\n',
            '或者来个假面舞会什么的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510361212V#648F两个骑士和白色公主\n',
            '可是很难得才能聚集到一起呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010361213V#1018F#6P啊！这主意也不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020361214V#1052F#6P这是什么反应嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020361215V#1043F还有、我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010361216V#1026F#5P（约修亚……？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020361217V#1043F#6P那个、汉斯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020361218V…………我………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520361219V#733F#2P嗯、怎么了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520361220V#731F是吗！\n',
            '你果然还是无法忘记和我一起\n',
            '度过的那些时光吗！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520361221V#732F真是没办法，看来我也只能\n',
            '下定决心接受你的真心告白了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020361222V#1052F#6P在说什么啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020361223V#1048F……本来还想认真\n',
            '说些事情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520361224V#736F#2P想叙旧的话\n',
            '什么时候都可以。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520361225V#732F不过，无论叙不叙旧，\n',
            '也都不会改变什么啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020361226V#1044F#6P哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520361227V#731F#2P你和我是好朋友。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520361228V#730F……你已经回来了，\n',
            '并且现在站在我的眼前。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520361229V这才是最重要的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020361230V#1044F#6P啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020361231V#1053F嗯……确实如此啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0510361232V#649F#5P（哎呀呀……\n',
            '　男生怎么也都这个样子。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 400)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010361233V#1008F#6P（嘿嘿嘿……\n',
            '　这不是很好吗。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x0008, 255)
    OP_4B(0x0009, 255)
    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))
    SetScenaFlags(ScenaFlag(0x0418, 0, 0x20C0))
    EventEnd(0x00)

    Return()

# id: 0x0012 offset: 0x2AFC
@scena.Code('func_12_2AFC')
def func_12_2AFC():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, 25410, 0, 55980, 90)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_2B23')
    def lambda_2B23():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2B23)

    ChrWalkTo(0x00FE, 28330, 0, 54740, 2000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x0013 offset: 0x2B4B
@scena.Code('func_13_2B4B')
def func_13_2B4B():
    Sleep(600)

    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, 25410, 0, 55980, 90)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_2B77')
    def lambda_2B77():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2B77)

    ChrWalkTo(0x00FE, 28380, 0, 55650, 2000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x0014 offset: 0x2B9F
@scena.Code('func_14_2B9F')
def func_14_2B9F():
    Sleep(1200)

    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, 25410, 0, 55980, 90)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_2BCB')
    def lambda_2BCB():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2BCB)

    ChrWalkTo(0x00FE, 27290, 0, 55370, 2000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x0015 offset: 0x2BF3
@scena.Code('func_15_2BF3')
def func_15_2BF3():
    Sleep(1800)

    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, 25410, 0, 55980, 90)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_2C1F')
    def lambda_2C1F():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2C1F)

    ChrWalkTo(0x00FE, 27310, 0, 56200, 2000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x0016 offset: 0x2C47
@scena.Code('func_16_2C47')
def func_16_2C47():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_2D1F',
    )

    ChrTalk(
        0x0008,
        (
            '#0510361234V#644F学院的情况虽然很麻烦，\n',
            '但也只有试着努力克服困难了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510361235V#659F呵呵呵～假面舞会吗……\n',
            '真是太期待了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020361236V#1048F（难道是……………\n',
            '……………………认真的？)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    Jump('loc_2D9B')

    def _loc_2D1F(): pass

    label('loc_2D1F')

    ChrTalk(
        0x0008,
        (
            '#0510361234V#644F学院的情况虽然很麻烦，\n',
            '但也只有试着努力克服困难了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510361238V#659F那，我就强烈期待\n',
            '假面舞会了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2D9B(): pass

    label('loc_2D9B')

    TalkEnd(0x0008)

    Return()

# id: 0x0017 offset: 0x2D9F
@scena.Code('func_17_2D9F')
def func_17_2D9F():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_2EAC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2E48',
    )

    ChrTalk(
        0x00FE,
        (
            '难得的新学期，\n',
            '讨厌的事件却接连不断……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，到底什么时候\n',
            '才能恢复正常的校园生活啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真希望吹奏音乐部的课外活动\n',
            '也能早点重新开始。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    Jump('loc_2EAC')

    def _loc_2E48(): pass

    label('loc_2E48')

    ChrTalk(
        0x00FE,
        (
            '究竟要到什么时候\n',
            '才能恢复正常的校园生活啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真希望吹奏音乐部的课外活动\n',
            '也能早点重新开始。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2EAC(): pass

    label('loc_2EAC')

    TalkEnd(0x00FE)

    Return()

# id: 0x0018 offset: 0x2EB0
@scena.Code('func_18_2EB0')
def func_18_2EB0():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2EC1',
    )

    Call(0, 0x0039)

    def _loc_2EC1(): pass

    label('loc_2EC1')

    EventBegin(0x00)
    MapClearFlags(0x00000001)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    OP_4A(0x0009, 255)
    ChrSetPos(0x0101, 30850, 0, 56600, 315)
    ChrSetPos(0x00F7, 29800, 0, 53800, 0)
    ChrSetPos(0x0105, 30850, 0, 55280, 315)
    ChrSetPos(0x0104, 28700, 0, 55860, 45)
    ChrSetPos(0x0127, 28700, 0, 54720, 45)
    ChrSetPos(0x0008, 29800, 0, 58200, 180)
    ChrSetPos(0x0009, 28700, 0, 57000, 45)
    CameraMove(31490, 0, 57970, 0)
    OP_67(0, 5720, -10000, 0)
    CameraSetDistance(2900, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeIn(1500, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3069',
    )

    ChrTalk(
        0x0008,
        (
            '#0510210856V#647F#5P那么……\n',
            '大家来做个分工吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510210857V#640F我和阿加特先生就去\n',
            '职员室向老师们打听一下情况。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510210858V然后再向其他职员\n',
            '进行询问调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050210859V#051F噢，那就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3140')

    def _loc_3069(): pass

    label('loc_3069')

    ChrTalk(
        0x0008,
        (
            '#0510210856V#647F#5P那么……\n',
            '大家来做个分工吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510210861V#640F我和雪拉扎德姐姐就去\n',
            '职员室向老师们打听一下情况。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510210858V之后继续向其他职员\n',
            '进行探听调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030210863V#021F呵呵～那就麻烦你带路了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3140(): pass

    label('loc_3140')

    ChrTurnDirection(0x0008, 0x0009, 400)

    ChrTalk(
        0x0008,
        (
            '#0510210864V#640F#5P汉斯去资料室\n',
            '查一查过去有没有\n',
            '发生过类似的事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520210865V#730F#6P了解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#0510210866V#648F#5P艾丝蒂尔和科洛丝\n',
            '就负责向学生询问情报吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210867V#1006F#2PＯＫ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060210868V#040F#2P明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0104, 400)

    ChrTalk(
        0x0008,
        (
            '#0510210869V#641F#5P朵洛希小姐和奥利维尔先生\n',
            '就随便在学院里面逛逛吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510210870V凭借你们艺术家的直觉\n',
            '也许会有什么发现呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040210871V#035F#6P呵～交给我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0127,
        (
            '#0280210872V#151F我也要加油啦⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x00F7, 400)

    ChrTalk(
        0x0008,
        (
            '#0510210873V#644F#5P大家都要在傍晚前结束调查，\n',
            '然后回这里集合。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510210874V那么解散！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_337E')
    def lambda_337E():
        ChrTurnDirection(0x00FE, 0x0104, 0)
        Yield()

        Jump('lambda_337E')

    DispatchAsync2(0x0101, 0x0002, lambda_337E)

    @scena.Lambda('lambda_338F')
    def lambda_338F():
        ChrTurnDirection(0x00FE, 0x0104, 0)
        Yield()

        Jump('lambda_338F')

    DispatchAsync2(0x0105, 0x0001, lambda_338F)

    CreateThread(0x0104, 0x01, 0x00, func_19_38E6)
    Sleep(500)

    CreateThread(0x0127, 0x01, 0x00, func_19_38E6)
    Sleep(800)

    CreateThread(0x0009, 0x01, 0x00, func_19_38E6)
    Sleep(800)

    CreateThread(0x00F7, 0x01, 0x00, func_1A_3937)
    Sleep(800)

    CreateThread(0x0008, 0x01, 0x00, func_1B_39B0)
    WaitForThreadExit(0x0008, 0x0001)
    TerminateThread(0x0101, 0x02)
    TerminateThread(0x0105, 0x01)

    @scena.Lambda('lambda_33E4')
    def lambda_33E4():
        CameraMove(31890, 0, 57570, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_33E4)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010210875V#1006F#5P哈……\n',
            '乔儿还是这么能干啊，\n',
            '学院祭的时候也是这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210876V虽然平时经常胡闹，\n',
            '但真不愧是学生会长啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060210877V#041F#6P呵呵……\n',
            '乔儿的理想可是成为像梅贝尔市长\n',
            '那样的政治家呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060210878V#040F经常会抱怨说些\n',
            '『可惜没早生十年，不然这次\n',
            '就可以竞选市长了』之类的话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0105, 400)

    ChrTalk(
        0x0101,
        (
            '#0010210879V#1016F#5P好、好厉害。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210880V#1004F对了，说起来的话……\n',
            '乔儿她们对科洛丝的事…\n',
            '知道了多少呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060210881V#041F#6P呵呵……\n',
            '已经全部都知道了呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060210882V入学才半年左右，\n',
            '我的秘密就被他们两个发现了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060210883V#040F除了他们两个之外，学院中\n',
            '了解我王族身份的人就只有校长了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210884V#1011F#5P这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210885V但即使如此，\n',
            '他们两个对科洛丝的态度\n',
            '依旧是非常自然呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060210886V#048F#6P是啊……\n',
            '就像艾丝蒂尔一样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060210887V他们都是我最重要的朋友。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210888V#1016F#5P啊哈哈……\n',
            '忽然这么说…还真有点不好意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210889V#1006F好了，现在还是赶快在学院里\n',
            '收集一下情报吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210890V只要问大家『考试期间\n',
            '是否发生了什么奇怪的事件？』\n',
            '就可以了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060210891V#040F#6P嗯，这样问的话\n',
            '大家也都比较容易明白。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060210892V对了，另外也要去问问\n',
            '宿舍里的学生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210893V#1006F#5P嗯，ＯＫ。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210894V好，那现在就开始行动吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x26, 0xFF)
    SetScenaFlags(ScenaFlag(0x0243, 6, 0x121E))
    OP_28(0x0083, 0x01, 0x0002)
    OP_28(0x0083, 0x01, 0x0004)
    OP_28(0x0066, 0x04, 0x40)
    OP_28(0x0067, 0x04, 0x40)
    EventEnd(0x00)

    Return()

# id: 0x0019 offset: 0x38E6
@scena.Code('func_19_38E6')
def func_19_38E6():
    ChrSetDirection(0x00FE, 270, 400)
    ChrWalkTo(0x00FE, 26560, 0, 55980, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0004)

    @scena.Lambda('lambda_390C')
    def lambda_390C():
        ChrWalkTo(0x00FE, 24670, 0, 55900, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_390C)

    Sleep(400)

    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 400)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x001A offset: 0x3937
@scena.Code('func_1A_3937')
def func_1A_3937():
    ChrSetDirection(0x00FE, 270, 400)
    ChrWalkTo(0x00FE, 28430, 0, 53950, 2000, 0x00)
    ChrWalkTo(0x00FE, 27590, 0, 55750, 2000, 0x00)
    ChrWalkTo(0x00FE, 26560, 0, 55980, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0004)

    @scena.Lambda('lambda_3985')
    def lambda_3985():
        ChrWalkTo(0x00FE, 24670, 0, 55900, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_3985)

    Sleep(400)

    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 400)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x001B offset: 0x39B0
@scena.Code('func_1B_39B0')
def func_1B_39B0():
    ChrSetDirection(0x00FE, 270, 400)
    ChrWalkTo(0x00FE, 28900, 0, 58450, 2000, 0x00)
    ChrWalkTo(0x00FE, 27590, 0, 55750, 2000, 0x00)
    ChrWalkTo(0x00FE, 26560, 0, 55980, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0004)

    @scena.Lambda('lambda_39FE')
    def lambda_39FE():
        ChrWalkTo(0x00FE, 24670, 0, 55900, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_39FE)

    Sleep(400)

    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 400)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x001C offset: 0x3A29
@scena.Code('func_1C_3A29')
def func_1C_3A29():
    EventBegin(0x00)
    MapClearFlags(0x00000001)
    Fade(1000)
    ChrSetPos(0x0101, -29850, 0, 58500, 99)
    ChrSetPos(0x0105, -30230, 0, 57060, 31)
    ChrSetDirection(0x0009, 270, 0)
    ChrSetSubChip(0x0009, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)

    ExecExpressionWithVar(
        0x65,
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.GetChrWork, 0x9, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x66,
        (
            (Expr.GetChrWork, 0x101, 0x2),
            (Expr.GetChrWork, 0x9, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x67,
        (
            (Expr.GetChrWork, 0x101, 0x3),
            (Expr.GetChrWork, 0x9, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_0D()

    ChrTalk(
        0x0009,
        (
            '#0520210895V#730F哟～二位好。\n',
            '调查得怎么样啦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210896V#1016F#6P嗯……\n',
            '才刚开始而已啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060210897V#040F你这里进展得怎么样呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520210898V#730F资料并不算太多，\n',
            '应该花费不了多少时间。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520210899V#736F先不说这个……\n',
            '抱歉，虽然现在有正事要做，\n',
            '但我想占用你们一点时间，可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210900V#1004F#6P啊、嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210901V#1002F是想说……约修亚的事情吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520210902V#735F啊啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520210903V#732F虽然具体详情我不太清楚，\n',
            '但那家伙好像失踪了是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210904V#1025F#6P嗯……不过你不用担心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210905V他是自己消失不见的，\n',
            '这样……只能算是离家出走而已啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520210906V#736F……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520210907V#730F我和那家伙虽然一共\n',
            '也只相处了一周左右，不过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520210908V我们很投缘的，\n',
            '当时在一起天南地北聊了很多。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520210909V他还和我说了很多\n',
            '来到艾丝蒂尔家之后的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210718V#1008F#6P是、是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210911V还真是有点不好意思。\n',
            '小时候的我完全就是个野丫头……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210912V#1016F啊、其实现在也仍然一样吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520210913V#731F哈哈，总之他给我讲了很多\n',
            '有趣的事情呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520210914V#730F但是……\n',
            '以前的经历，他却对我只字未提。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210915V#1026F#6P……啊………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520210916V#736F有一次，我假装无意地问起他\n',
            '来洛连特之前的事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520210917V约修亚那时的眼神……\n',
            '我到现在也还记忆犹新。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520210918V#735F就在一瞬间，他的眼神完全失去了光彩，\n',
            '我似乎都听到了他心碎的声音。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520210919V#730F不过，他马上就强作笑容\n',
            '敷衍了过去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210920V#1003F#6P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520210921V#732F我虽然不知道这是为什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520210922V但约修亚如今会失踪，\n',
            '恐怕和他以前的经历也有关吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210923V#1026F#6P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210924V我想…大概是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520210925V#735F果然是这样吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520210926V#730F那时候…每天睡觉之前\n',
            '大家都会讨论当天发生的一些趣事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520210927V像是舞台剧的练习好累啦，\n',
            '今天的晚饭真好吃啦什么的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520210928V#736F那家伙…每到这时\n',
            '就会露出一副憧憬向往的表情……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520210929V就好像是在眺望着只能远观，\n',
            '却永远也无法得到的宝物一样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520210930V在他看来，这些东西似乎都是自己\n',
            '注定永远无法拥有的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520210931V他的表情就是这样说的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210932V#1026F#6P……约修亚………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210933V#1027F说什么永远无法拥有……\n',
            '真是个…大笨蛋……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060210934V#043F#4P艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520210935V#730F喂、艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520210936V虽然我和他交情不深，\n',
            '也许没有说这些话的立场，不过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520210937V我还是想拜托你一件事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210938V#1004F#6P哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520210939V#732F你找到那家伙以后，请替我告诉他，\n',
            '别再露出那种表情了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520210940V说什么永远也得不到，\n',
            '哪有那种混帐事啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520210941V那家伙和我们一样，\n',
            '可以欢笑，可以恋爱，\n',
            '一样拥有…得到幸福的权利。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520210942V嗯，就是这样了，没问题吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210943V#1025F#6P汉斯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210944V#1012F嗯！我一定会替你转告他的！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210945V#1018F就算是揍他一顿\n',
            '我也会让他清醒！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060210946V#041F#4P呵呵～艾丝蒂尔真是的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060210947V#048F不过如果不这样做的话\n',
            '约修亚可能\n',
            '永远都不会明白吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520210948V#734F啊啊～本来就是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520210949V#730F呼……\n',
            '说出来以后总算舒服一点了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520210950V抱歉，耽误了你们不少时间。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520210951V请继续忙正事吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210952V#1017F#6P嗯…明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0009, 400)

    ChrTalk(
        0x0105,
        (
            '#0060210953V#041F汉斯也\n',
            '要多多加油啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0009, 90, 400)
    SetScenaFlags(ScenaFlag(0x0243, 7, 0x121F))
    EventEnd(0x00)

    Return()

# id: 0x001D offset: 0x4704
@scena.Code('func_1D_4704')
def func_1D_4704():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4715',
    )

    Call(0, 0x0039)

    def _loc_4715(): pass

    label('loc_4715')

    EventBegin(0x00)
    FadeOut(0, 0, -1)
    MapClearFlags(0x00000001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_4734',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_4738')

    def _loc_4734(): pass

    label('loc_4734')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_4738(): pass

    label('loc_4738')

    FormationAddMember(ChrTable['奥利维尔'], 0xF8, 0xFF)
    FormationAddMember(ChrTable['朵洛希'], 0xFF, 0xFF)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    OP_4A(0x0009, 255)
    ChrSetPos(0x00F7, 29800, 0, 53800, 0)
    ChrSetPos(0x0104, 28700, 0, 55860, 90)
    ChrSetPos(0x0127, 28700, 0, 54720, 90)
    ChrSetPos(0x0008, 29800, 0, 58200, 180)
    ChrSetPos(0x0009, 28700, 0, 57000, 90)
    ChrSetPos(0x0101, 24710, 0, 55840, 90)
    ChrSetPos(0x0105, 24710, 0, 55840, 90)
    ChrSetRGBAMask(0x0101, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0105, 255, 255, 255, 0, 0)
    ChrClearFlags(0x0101, 0x0008)
    ChrClearFlags(0x0105, 0x0008)
    CameraMove(31490, 0, 57970, 0)
    OP_67(0, 5720, -10000, 0)
    CameraSetDistance(2900, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeIn(1000, 0)
    OP_0D()
    PlaySE(6, 0x00, 0x64)
    Sleep(800)

    @scena.Lambda('lambda_483C')
    def lambda_483C():
        CameraMove(29490, 0, 57970, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_483C)

    @scena.Lambda('lambda_4854')
    def lambda_4854():
        ChrMoveTo(0x0101, 27060, 0, 55380, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_4854)

    @scena.Lambda('lambda_486F')
    def lambda_486F():
        ChrSetRGBAMask(0x0101, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_486F)

    Sleep(200)

    @scena.Lambda('lambda_4886')
    def lambda_4886():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_4886)

    @scena.Lambda('lambda_4894')
    def lambda_4894():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0127, 0x0001, lambda_4894)

    @scena.Lambda('lambda_48A2')
    def lambda_48A2():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_48A2')

    DispatchAsync2(0x0009, 0x0001, lambda_48A2)

    @scena.Lambda('lambda_48B3')
    def lambda_48B3():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_48B3)

    @scena.Lambda('lambda_48C1')
    def lambda_48C1():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_48C1)

    Sleep(300)

    @scena.Lambda('lambda_48D4')
    def lambda_48D4():
        ChrMoveTo(0x0105, 26600, 0, 56250, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0000, lambda_48D4)

    @scena.Lambda('lambda_48EF')
    def lambda_48EF():
        ChrSetRGBAMask(0x0105, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_48EF)

    WaitForThreadExit(0x0104, 0x0001)
    WaitForThreadExit(0x0127, 0x0001)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0105, 0x0000)
    WaitForThreadExit(0x0105, 0x0001)
    TerminateThread(0x0009, 0x01)

    ChrTalk(
        0x0008,
        (
            '#0510211268V#644F#5P啊，回来了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510211269V#648F那么大家就来说说\n',
            '各自的调查结果吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    ChrSetPos(0x0101, 30850, 0, 56600, 270)
    ChrSetPos(0x0105, 30850, 0, 55280, 270)
    ChrSetPos(0x00F7, 29800, 0, 53800, 0)
    ChrSetPos(0x0104, 28700, 0, 55860, 90)
    ChrSetPos(0x0127, 28700, 0, 54720, 90)
    ChrSetPos(0x0008, 29800, 0, 58200, 180)
    ChrSetPos(0x0009, 28700, 0, 57000, 90)
    CameraMove(31490, 0, 57970, 0)
    OP_67(0, 5720, -10000, 0)
    CameraSetDistance(2900, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    Sleep(500)

    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_4B07',
    )

    ChrTalk(
        0x0106,
        (
            '#0050211270V#053F#2P我们问过了全部的校内职员……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050211271V#050F有个勤务员好像在学院里\n',
            '看见了奇怪的人影。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050211272V据说人影在通向旧校舍的后门那里\n',
            '突然消失不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4BB0')

    def _loc_4B07(): pass

    label('loc_4B07')

    ChrTalk(
        0x0103,
        (
            '#0030211273V#026F#2P我们问过了职员们……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030211274V#022F有一名勤务员在学院内\n',
            '目击到了奇怪的人影，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030211275V据说人影在通向旧校舍的后门那里\n',
            '之后就突然消失了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4BB0(): pass

    label('loc_4BB0')

    ChrTalk(
        0x0008,
        (
            '#0510211276V#644F#5P其它的老师都在为考试的事而忙，\n',
            '没注意到什么异常情况。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510211277V在学生食堂的阿姨和\n',
            '接待处的珐奥娜小姐那里\n',
            '也没有得到什么有用的情报～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211278V#1015F#5P是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211279V#1011F我们这边，有３个学生\n',
            '提供了有价值的情报……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '把巴托姆、米克、芙拉瑟的证言\n',
            '向其他人说明了。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0105,
        (
            '#0060211280V#043F#2P三条证言全部都提到了\n',
            '旧校舍那里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211281V这应该不是单纯的巧合。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0127,
        (
            '#0280211282V#150F那么～\n',
            '我也来发表一下我的成果吧～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280211283V#151F学生·老师们的照片３０张～\n',
            '学院内的风景照５０张～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280211284V嘿嘿。\n',
            '都拍摄得很可爱哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040211285V#030F#6P很遗憾，我这边\n',
            '没有什么太大的收获。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040211286V#031F呵呵，不过我的演奏\n',
            '却是吸引来很多可爱的\n',
            '小猫咪呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010211287V#1019F#5P真是的！你们两个\n',
            '完全都没有认真调查嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211288V#1007F虽然一开始就没抱什么期待……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0520211289V#735F最后轮到我了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520211290V#730F我查询过去的资料，\n',
            '想确认一下以前是否发生过\n',
            '类似事件，结果很有意思……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520211291V这所学院在建成新校舍以后\n',
            '几乎就没有再发生过什么怪谈事件了，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520211292V而仅有的几个恰好也都集中在旧校舍。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0009, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(50)

    OP_62(0x00F7, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0105, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(50)

    OP_62(0x0104, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0008, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(50)

    OP_62(0x0127, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1000)

    OP_63(0x0101)
    OP_63(0x00F7)
    OP_63(0x0105)
    OP_63(0x0104)
    OP_63(0x0127)
    OP_63(0x0008)
    OP_63(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_5138',
    )

    ChrTalk(
        0x0106,
        (
            '#0050211293V#552F#2P不管怎么想，\n',
            '看来最可疑的就是旧校舍了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050211294V那到底是个怎样的建筑物？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_51AE')

    def _loc_5138(): pass

    label('loc_5138')

    ChrTalk(
        0x0103,
        (
            '#0030211295V#025F#2P不管从哪方面考虑，\n',
            '最可疑的地方也都是旧校舍啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030211296V#020F那究竟是个怎样的建筑物呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_51AE(): pass

    label('loc_51AE')

    ChrTalk(
        0x0008,
        (
            '#0510211297V#644F#5P位于后门深处的旧校舍\n',
            '是个数百年前建造的古老建筑物。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510211298V直到２０年前还一直被人们使用，\n',
            '在新校舍建立好以后\n',
            '那里就被封锁了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010211299V#1015F#5P啊～学院祭的时候\n',
            '我们不是进去过旧校舍里面吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0105, 315, 400)

    ChrTalk(
        0x0105,
        (
            '#0060211300V#542F#2P后来发现里面栖息着魔兽，\n',
            '因为太过危险，就用锁把后门锁上了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211301V大概已经被荒置\n',
            '２、３个月了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040211302V#035F#6P呵……\n',
            '数百年前的石制建筑物吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040211303V#030F作为亡灵的栖息地，\n',
            '真是再适合不过的地方了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211304V#1007F#5P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211305V虽然有点不想去…\n',
            '不过现在看来似乎也没有别的办法了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211306V#1008F……今天已经太晚了，\n',
            '不如明天早上来调查怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040211307V#033F#6P啊，艾丝蒂尔。\n',
            '为什么说太晚了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010211308V#1016F#5P那、那个…现在天已经黑了啊！\n',
            '里面又有魔兽，也许很危险的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211309V那个地方就算白天去都觉得阴森森的，\n',
            '晚上进去的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040211310V#030F#6P哼哼，那不是正好嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040211311V#031F要想试胆量的话，深夜不是正好么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040211312V要想抓住幽灵的原形，\n',
            '夜晚是最合适的时间段了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0127,
        (
            '#0280211313V#151F嗯嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280211314V要想拍出灵异照片的话\n',
            '就必须要在晚上才行～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211315V#1019F#5P呜、嗯嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrSetDirection(0x0101, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010211316V#1004F#5P啊……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211317V#044F#2P艾丝蒂尔？\n',
            '怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211318V#1015F#5P嗯……\n',
            '我在窗外好像看见了什么东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5709')
    def lambda_5709():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_5709')

    DispatchAsync2(0x00F7, 0x0001, lambda_5709)

    @scena.Lambda('lambda_571A')
    def lambda_571A():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_571A')

    DispatchAsync2(0x0105, 0x0001, lambda_571A)

    @scena.Lambda('lambda_572B')
    def lambda_572B():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_572B')

    DispatchAsync2(0x0104, 0x0001, lambda_572B)

    @scena.Lambda('lambda_573C')
    def lambda_573C():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_573C')

    DispatchAsync2(0x0127, 0x0001, lambda_573C)

    @scena.Lambda('lambda_574D')
    def lambda_574D():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_574D')

    DispatchAsync2(0x0008, 0x0001, lambda_574D)

    @scena.Lambda('lambda_575E')
    def lambda_575E():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_575E')

    DispatchAsync2(0x0009, 0x0001, lambda_575E)

    @scena.Lambda('lambda_576F')
    def lambda_576F():
        CameraMove(30490, 0, 59490, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_576F)

    @scena.Lambda('lambda_5787')
    def lambda_5787():
        OP_67(0, 6150, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_5787)

    ChrWalkTo(0x0101, 31050, 0, 58560, 2000, 0x00)
    OP_20(0x00000BB8)
    ChrWalkTo(0x0101, 30490, 0, 59490, 2000, 0x00)
    ChrSetDirection(0x0101, 0, 400)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010211319V#1015F白白的一团影子，\n',
            '还以为是基库呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211320V#1019F……………………白影？！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    FadeIn(500, 0)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T2500._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x001E offset: 0x5870
@scena.Code('func_1E_5870')
def func_1E_5870():
    ChrWalkTo(0x0101, 28340, 0, 58250, 2000, 0x00)
    ChrWalkTo(0x0101, 31120, 0, 58700, 2000, 0x00)
    ChrWalkTo(0x0101, 30850, 0, 57000, 2000, 0x00)
    ChrSetDirection(0x0101, 284, 400)

    Return()

# id: 0x001F offset: 0x58B4
@scena.Code('func_1F_58B4')
def func_1F_58B4():
    ChrWalkTo(0x0105, 28430, 0, 58640, 2000, 0x00)
    ChrWalkTo(0x0105, 29800, 0, 58200, 2000, 0x00)
    ChrTurnDirection(0x0105, 0x0009, 400)

    Return()

# id: 0x0020 offset: 0x58E4
@scena.Code('func_20_58E4')
def func_20_58E4():
    ChrSetPos(0x0101, 30490, 0, 59490, 0)
    ChrSetPos(0x0105, 30850, 0, 55280, 270)
    ChrSetPos(0x00F7, 29800, 0, 53800, 0)
    ChrSetPos(0x0104, 28700, 0, 55860, 90)
    ChrSetPos(0x0127, 28700, 0, 54720, 90)
    ChrSetPos(0x0008, 29800, 0, 58200, 180)
    ChrSetPos(0x0009, 28700, 0, 57000, 90)
    ChrTurnDirection(0x00F7, 0x0101, 0)
    ChrTurnDirection(0x0105, 0x0101, 0)
    ChrTurnDirection(0x0104, 0x0101, 0)
    ChrTurnDirection(0x0127, 0x0101, 0)
    ChrTurnDirection(0x0008, 0x0101, 0)
    ChrTurnDirection(0x0009, 0x0101, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    OP_4A(0x0009, 255)
    CameraMove(30490, 0, 59490, 0)
    OP_67(0, 5720, -10000, 0)
    CameraSetDistance(2900, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    EventBegin(0x00)
    MapClearFlags(0x02000000)
    FadeIn(2000, 0)
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_0D()

    ChrTalk(
        0x0105,
        (
            '#0060211321V#043F#2P艾丝蒂尔？\n',
            '怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x0101)

    ChrTalk(
        0x0101,
        (
            '#0010211322V#1008F#5P啊哈……\n',
            '啊哈哈哈哈哈……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211323V#1007F啊、啊啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    PlaySE(524, 0x00, 0x64)
    ChrSetFlags(0x0101, 0x0002)
    ChrSetChipByIndex(0x0101, 2)
    ChrSetSubChip(0x0101, 1)
    OP_0D()
    Sleep(500)

    OP_62(0x00F7, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0104, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0127, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_5B5D',
    )

    ChrTalk(
        0x0106,
        (
            '#0050211324V#055F#2P喂、喂！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5B83')

    def _loc_5B5D(): pass

    label('loc_5B5D')

    ChrTalk(
        0x0103,
        (
            '#0030211325V#023F#2P艾丝蒂尔！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5B83(): pass

    label('loc_5B83')

    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(500)

    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T2812._SN', 115, 0, 0)
    IdleLoop()

    Return()

# id: 0x0021 offset: 0x5BA0
@scena.Code('func_21_5BA0')
def func_21_5BA0():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetPos(0x0017, 2350, 0, -610, 270)
    ChrSetPos(0x0018, 340, 0, -790, 90)
    ChrSetPos(0x0019, -80, 0, -4510, 180)
    ChrSetPos(0x001A, -2400, 0, -3520, 270)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    ChrClearFlags(0x001A, 0x0080)
    LoadChip('ED6_DT26/CH20208._CH', 'ED6_DT26/CH20208P._CP', 17)
    LoadChip('ED6_DT26/CH20209._CH', 'ED6_DT26/CH20209P._CP', 18)
    ChrSetChipByIndex(0x0017, 17)
    ChrSetChipByIndex(0x0018, 18)
    ChrSetChipByIndex(0x0019, 17)
    ChrSetChipByIndex(0x001A, 18)
    ChrSetSubChip(0x0017, 0)
    ChrSetSubChip(0x0018, 0)
    ChrSetSubChip(0x0019, 0)
    ChrSetSubChip(0x001A, 0)
    OP_62(0x0017, 0x00000000, 2100, 0x26, 0x27, 0x000000FA, 0x00)
    Sleep(50)

    OP_62(0x0018, 0x00000000, 2100, 0x26, 0x27, 0x000000FA, 0x00)
    CreateThread(0x0019, 0x01, 0x00, func_22_5CF8)
    CreateThread(0x001A, 0x01, 0x00, func_23_5D35)
    ChrSetFlags(0x000B, 0x0080)
    CameraMove(150, 2000, 4650, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeIn(1000, 0)
    CameraMove(-110, 0, -3080, 4000)
    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021F, 6, 0x10FE))
    SetScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    NewScene('ED6_DT21/T2500._SN', 108, 0, 0)
    IdleLoop()

    Return()

# id: 0x0022 offset: 0x5CF8
@scena.Code('func_22_5CF8')
def func_22_5CF8():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5D34',
    )

    ChrSetDirection(0x00FE, 135, 400)
    Sleep(700)

    ChrSetDirection(0x00FE, 180, 400)
    Sleep(700)

    ChrSetDirection(0x00FE, 225, 400)
    Sleep(700)

    ChrSetDirection(0x00FE, 180, 400)
    Sleep(700)

    Jump('func_22_5CF8')

    def _loc_5D34(): pass

    label('loc_5D34')

    Return()

# id: 0x0023 offset: 0x5D35
@scena.Code('func_23_5D35')
def func_23_5D35():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5D9F',
    )

    ChrWalkTo(0x00FE, -6030, 0, -2780, 2000, 0x00)
    ChrWalkTo(0x00FE, -5980, 0, -20, 2000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)
    ChrWalkTo(0x00FE, -6030, 0, -2780, 2000, 0x00)
    ChrWalkTo(0x00FE, -2400, 0, -3520, 2000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)

    Jump('func_23_5D35')

    def _loc_5D9F(): pass

    label('loc_5D9F')

    Return()

# id: 0x0024 offset: 0x5DA0
@scena.Code('func_24_5DA0')
def func_24_5DA0():
    Call(0, 0x0025)
    Call(0, 0x0026)

    Return()

# id: 0x0025 offset: 0x5DA9
@scena.Code('func_25_5DA9')
def func_25_5DA9():
    EventBegin(0x00)
    LoadChip('ED6_DT26/CH20208._CH', 'ED6_DT26/CH20208P._CP', 17)
    LoadChip('ED6_DT26/CH20501._CH', 'ED6_DT26/CH20501P._CP', 18)
    LoadChip('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP', 19)
    LoadChip('ED6_DT27/CH04001._CH', 'ED6_DT27/CH04001P._CP', 20)
    LoadChip('ED6_DT27/CH04010._CH', 'ED6_DT27/CH04010P._CP', 21)
    LoadChip('ED6_DT27/CH04011._CH', 'ED6_DT27/CH04011P._CP', 22)
    LoadChip('ED6_DT07/CH00420._CH', 'ED6_DT07/CH00420P._CP', 23)
    LoadChip('ED6_DT07/CH00421._CH', 'ED6_DT07/CH00421P._CP', 24)
    LoadChip('ED6_DT07/CH00410._CH', 'ED6_DT07/CH00410P._CP', 25)
    LoadChip('ED6_DT07/CH00411._CH', 'ED6_DT07/CH00411P._CP', 26)
    LoadChip('ED6_DT26/CH20209._CH', 'ED6_DT26/CH20209P._CP', 27)
    LoadChip('ED6_DT27/CH04621._CH', 'ED6_DT27/CH04621P._CP', 28)
    LoadChip('ED6_DT27/CH04611._CH', 'ED6_DT27/CH04611P._CP', 29)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x010A, 0x0080)
    ChrSetFlags(0x010E, 0x0080)
    ChrSetPos(0x0017, -1990, 0, 42080, 0)
    ChrSetPos(0x0018, 1610, 0, 41880, 0)
    ChrSetChipByIndex(0x0017, 17)
    ChrSetChipByIndex(0x0018, 27)
    ChrSetSubChip(0x0017, 0)
    ChrSetSubChip(0x0018, 0)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0018, 0x0080)
    CameraMove(550, 0, 52120, 0)
    OP_67(0, 5840, -10000, 0)
    CameraSetDistance(2300, 0)
    OP_6C(45000, 0)
    OP_6E(368, 0)
    FadeIn(1000, 0)
    OP_0D()
    CreateThread(0x0101, 0x01, 0x00, func_27_61E2)
    Sleep(500)

    CreateThread(0x0102, 0x01, 0x00, func_28_6232)
    Sleep(500)

    CreateThread(0x010A, 0x01, 0x00, func_29_6282)

    @scena.Lambda('lambda_5EED')
    def lambda_5EED():
        CameraMove(1460, 0, 48750, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_5EED)

    @scena.Lambda('lambda_5F05')
    def lambda_5F05():
        OP_67(0, 4940, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_5F05)

    @scena.Lambda('lambda_5F1D')
    def lambda_5F1D():
        OP_6E(322, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_5F1D)

    @scena.Lambda('lambda_5F2D')
    def lambda_5F2D():
        CameraSetDistance(3060, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_5F2D)

    Sleep(500)

    CreateThread(0x010E, 0x01, 0x00, func_2A_62D2)
    WaitForThreadExit(0x0102, 0x0003)

    ChrTalk(
        0x0017,
        (
            '#4210360822V#5P啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#4220360823V#5P你们是……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x010E, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010360824V#1005F#5P要开战了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120360825V#815F#5P我们上～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5FD8')
    def lambda_5FD8():
        CameraMove(1410, 0, 48310, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_5FD8)

    @scena.Lambda('lambda_5FF0')
    def lambda_5FF0():
        CameraSetDistance(2400, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_5FF0)

    CreateThread(0x0101, 0x01, 0x00, func_2B_6322)
    Sleep(30)

    CreateThread(0x010A, 0x01, 0x00, func_2D_634C)
    Sleep(50)

    CreateThread(0x010E, 0x01, 0x00, func_2E_6361)
    Sleep(30)

    CreateThread(0x0102, 0x01, 0x00, func_2C_6337)
    Sleep(100)

    ChrSetChipByIndex(0x0017, 28)
    ChrSetFlags(0x0017, 0x1000)

    @scena.Lambda('lambda_603A')
    def lambda_603A():
        ChrMoveTo(0x00FE, -1740, 0, 44830, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0000, lambda_603A)

    Sleep(30)

    ChrSetChipByIndex(0x0018, 29)
    ChrSetFlags(0x0018, 0x1000)

    @scena.Lambda('lambda_6064')
    def lambda_6064():
        ChrMoveTo(0x00FE, 1870, 0, 45210, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0000, lambda_6064)

    WaitForThreadExit(0x0101, 0x0003)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x010A, 0xFF)
    TerminateThread(0x010E, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0017, 0xFF)
    TerminateThread(0x0018, 0xFF)
    Battle(0x000007A1, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_60AF'),
        (-1, 'loc_60B4'),
    )

    def _loc_60AF(): pass

    label('loc_60AF')

    OP_B4(0x00)

    Jump('loc_60B4')

    def _loc_60B4(): pass

    label('loc_60B4')

    Return()

# id: 0x0026 offset: 0x60B5
@scena.Code('func_26_60B5')
def func_26_60B5():
    EventBegin(0x00)
    TerminateThread(0x0017, 0x00)
    TerminateThread(0x0018, 0x00)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x010A, 0x01)
    TerminateThread(0x010E, 0x01)
    TerminateThread(0x0102, 0x01)
    LoadChip('ED6_DT26/CH20501._CH', 'ED6_DT26/CH20501P._CP', 18)
    CameraMove(-150, 0, 42940, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x010A, 65535)
    ChrSetChipByIndex(0x010E, 65535)
    ChrClearFlags(0x0017, 0x0001)
    ChrSetFlags(0x0017, 0x0002)
    ChrSetChipByIndex(0x0017, 18)
    ChrSetSubChip(0x0017, 8)
    ChrClearFlags(0x0018, 0x0001)
    ChrSetFlags(0x0018, 0x0002)
    ChrSetChipByIndex(0x0018, 18)
    ChrSetSubChip(0x0018, 11)
    ChrSetPos(0x0000, -150, 0, 42940, 180)
    ChrSetPos(0x0001, -150, 0, 42940, 180)
    ChrSetPos(0x0002, -150, 0, 42940, 180)
    ChrSetPos(0x0003, -150, 0, 42940, 180)
    OP_69(0x0000, 0)
    ChrSetPos(0x0017, 1340, 0, 39800, 0)
    ChrSetPos(0x0018, -2270, 0, 40010, 0)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x0018, 0x0080)
    SetScenaFlags(ScenaFlag(0x0404, 1, 0x2021))
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

# id: 0x0027 offset: 0x61E2
@scena.Code('func_27_61E2')
def func_27_61E2():
    ChrSetChipByIndex(0x0101, 19)
    ChrSetPos(0x00FE, 0, -2000, 48020, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 0, 0, 52600, 5000, 0x00)
    ChrWalkTo(0x00FE, -1720, 0, 51770, 5000, 0x00)
    ChrSetSubChip(0x00FE, 0)
    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x0028 offset: 0x6232
@scena.Code('func_28_6232')
def func_28_6232():
    ChrSetChipByIndex(0x0102, 21)
    ChrSetPos(0x00FE, 0, -2000, 48020, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 0, 0, 52600, 5000, 0x00)
    ChrWalkTo(0x00FE, -1840, 0, 53090, 5000, 0x00)
    ChrSetSubChip(0x00FE, 0)
    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x0029 offset: 0x6282
@scena.Code('func_29_6282')
def func_29_6282():
    ChrSetChipByIndex(0x010A, 23)
    ChrSetPos(0x00FE, 0, -2000, 48020, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 0, 0, 52600, 5000, 0x00)
    ChrWalkTo(0x00FE, 1730, 0, 52510, 5000, 0x00)
    ChrSetSubChip(0x00FE, 0)
    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x002A offset: 0x62D2
@scena.Code('func_2A_62D2')
def func_2A_62D2():
    ChrSetChipByIndex(0x010E, 25)
    ChrSetPos(0x00FE, 0, -2000, 48020, 0)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 0, 0, 52600, 5000, 0x00)
    ChrWalkTo(0x00FE, 860, 0, 53200, 5000, 0x00)
    ChrSetSubChip(0x00FE, 0)
    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x002B offset: 0x6322
@scena.Code('func_2B_6322')
def func_2B_6322():
    ChrWalkTo(0x00FE, -1680, 0, 44560, 8000, 0x00)

    Return()

# id: 0x002C offset: 0x6337
@scena.Code('func_2C_6337')
def func_2C_6337():
    ChrWalkTo(0x00FE, -1980, 0, 45670, 8000, 0x00)

    Return()

# id: 0x002D offset: 0x634C
@scena.Code('func_2D_634C')
def func_2D_634C():
    ChrWalkTo(0x00FE, 1610, 0, 44280, 8000, 0x00)

    Return()

# id: 0x002E offset: 0x6361
@scena.Code('func_2E_6361')
def func_2E_6361():
    ChrWalkTo(0x00FE, 1940, 0, 52520, 8000, 0x00)
    ChrWalkTo(0x00FE, 1470, 0, 45660, 8000, 0x00)

    Return()

# id: 0x002F offset: 0x638A
@scena.Code('func_2F_638A')
def func_2F_638A():
    EventBegin(0x00)
    OP_4A(0x0012, 255)
    OP_4A(0x0013, 255)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x010A, 0x0080)
    ChrSetFlags(0x010E, 0x0080)
    ChrSetDirection(0x0012, 180, 0)
    ChrSetDirection(0x0013, 0, 0)
    CameraMove(-27920, 0, 27650, 0)
    OP_67(0, 5370, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    OP_72(0x0002, 0x0010)
    OP_70(0x0002, 29)
    OP_73(0x0002)
    Sleep(300)

    @scena.Lambda('lambda_641C')
    def lambda_641C():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_641C)

    Sleep(100)

    @scena.Lambda('lambda_642F')
    def lambda_642F():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_642F)

    @scena.Lambda('lambda_643D')
    def lambda_643D():
        CameraMove(-28660, 0, 27330, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_643D)

    CreateThread(0x0102, 0x01, 0x00, func_31_68A3)
    Sleep(250)

    CreateThread(0x0101, 0x01, 0x00, func_30_6854)
    Sleep(250)

    CreateThread(0x010A, 0x01, 0x00, func_32_6906)
    Sleep(250)

    CreateThread(0x010E, 0x01, 0x00, func_33_6969)
    OP_62(0x0012, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(100)

    OP_62(0x0013, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0012,
        (
            '#1910360826V#6P你们是……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#3870360827V#6P艾丝蒂尔和约修亚！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360828V#1016F#2P嘿嘿嘿，好久不见啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360829V#1035F#2P好久不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '将作战计划，以及为解救人质\n',
            '而来的事情向大家说明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0013,
        (
            '#3870360830V#6P是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#1910360831V#6P抱歉……太感谢你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#1910360832V#6P我们能不能协助你们\n',
            '一起营救学生？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010E,
        (
            '#0330360833V#842F#2P您的心情我很理解，\n',
            '不过敌人是职业的雇佣兵部队。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330360834V#843F为了安全着想，\n',
            '还是请在这里等着我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#1910360835V#6P是吗……我明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#3870360836V#6P学生们就…\n',
            '就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120360837V#816F#2P嗯！请放心交给我们吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '取出游击士手册，\n',
            '在拉迪奥老师，艾福托老师\n',
            '的名字上做了标记了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    Fade(500)
    OP_71(0x0002, 0x0010)
    OP_6F(0x0002, 0)
    CameraMove(-29240, 0, 25720, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ChrSetPos(0x0000, -29240, 0, 25720, 270)
    ChrSetPos(0x0001, -29240, 0, 25720, 270)
    ChrSetPos(0x0002, -29240, 0, 25720, 270)
    ChrSetPos(0x0003, -29240, 0, 25720, 270)
    OP_4B(0x0012, 255)
    OP_4B(0x0013, 255)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x0404, 2, 0x2022))
    OP_28(0x00C0, 0x01, 0x0040)
    OP_28(0x00C1, 0x02, 0x0004)
    OP_28(0x00C1, 0x01, 0x0008)
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

# id: 0x0030 offset: 0x6854
@scena.Code('func_30_6854')
def func_30_6854():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, -26460, 0, 25950, 270)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_687B')
    def lambda_687B():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_687B)

    ChrWalkTo(0x00FE, -29540, 0, 25930, 4000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)

    Return()

# id: 0x0031 offset: 0x68A3
@scena.Code('func_31_68A3')
def func_31_68A3():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, -26460, 0, 25950, 270)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_68CA')
    def lambda_68CA():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_68CA)

    ChrWalkTo(0x00FE, -28180, 0, 25870, 4000, 0x00)
    ChrWalkTo(0x00FE, -29330, 0, 27350, 4000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)

    Return()

# id: 0x0032 offset: 0x6906
@scena.Code('func_32_6906')
def func_32_6906():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, -26460, 0, 25950, 270)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_692D')
    def lambda_692D():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_692D)

    ChrWalkTo(0x00FE, -28180, 0, 25870, 4000, 0x00)
    ChrWalkTo(0x00FE, -28690, 0, 25360, 4000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)

    Return()

# id: 0x0033 offset: 0x6969
@scena.Code('func_33_6969')
def func_33_6969():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, -26460, 0, 25950, 270)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_6990')
    def lambda_6990():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_6990)

    ChrWalkTo(0x00FE, -28180, 0, 25870, 4000, 0x00)
    ChrWalkTo(0x00FE, -28140, 0, 26550, 4000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)

    Return()

# id: 0x0034 offset: 0x69CC
@scena.Code('func_34_69CC')
def func_34_69CC():
    EventBegin(0x00)
    OP_4A(0x0014, 255)
    OP_4A(0x0015, 255)
    OP_4A(0x000B, 255)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x010A, 0x0080)
    ChrSetFlags(0x010E, 0x0080)
    CameraMove(30820, 0, 27050, 0)
    OP_67(0, 5260, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    Sleep(500)

    PlaySE(6, 0x00, 0x64)
    Sleep(500)

    @scena.Lambda('lambda_6A4F')
    def lambda_6A4F():
        ChrSetDirection(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_6A4F)

    Sleep(100)

    @scena.Lambda('lambda_6A62')
    def lambda_6A62():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_6A62)

    Sleep(100)

    @scena.Lambda('lambda_6A75')
    def lambda_6A75():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_6A75)

    @scena.Lambda('lambda_6A83')
    def lambda_6A83():
        CameraMove(30250, 0, 27820, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_6A83)

    CreateThread(0x0101, 0x01, 0x00, func_35_7031)
    Sleep(250)

    CreateThread(0x0102, 0x01, 0x00, func_36_7094)
    Sleep(250)

    CreateThread(0x010A, 0x01, 0x00, func_37_70F7)
    Sleep(250)

    CreateThread(0x010E, 0x01, 0x00, func_38_715A)
    OP_62(0x0015, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(100)

    OP_62(0x0014, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(100)

    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x000B,
        (
            '#3890360838V#2P啊！你们是……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#3880360839V艾丝蒂尔和约修亚……\n',
            '你们怎么会在这里！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360840V#1016F#6P啊哈哈……\n',
            '真是让人吃惊啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360841V#1042F#6P是这样的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '将作战计划，以及解救人质\n',
            '的经过向大家说明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0014,
        (
            '#3880360842V原来如此，你们……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3880360843V是来救我们的吗？太感谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#2880360844V那么……\n',
            '学院内的情况怎样？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#2880360845V战斗还在继续吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010E,
        (
            '#0330360846V#843F#6P正门附近的战斗还没结束，\n',
            '现在的状况还没有完全稳定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330360847V#842F为了安全起见，\n',
            '老师们还是先在这里等着吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#2880360848V是吗……真没办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#3880360849V学生们的事……\n',
            '就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3890360850V#2P对了。\n',
            '你们把这个拿去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveTo(0x000B, 29440, 0, 26100, 2000, 0x00)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了４个',
            (TxtCtl.Item, ItemTable['营养果汁']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    AddItem(ItemTable['营养果汁'], 4)
    ChrMoveTo(0x000B, 30510, 0, 25690, 2000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010360851V#1011F#6P阿姨……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120360852V#811F#6P哇，可以收下吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3890360853V#2P啊，真是好东西啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3890360854V帮助别人当然很好，\n',
            '但一定要小心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360855V#1054F#6P……真是谢谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '取出游击士手册，\n',
            '在德波拉，碧欧拉老师，米丽亚老师\n',
            '的名字上做了标记了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    Fade(500)
    CameraMove(28370, 0, 26480, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ChrSetPos(0x0000, 28370, 0, 26480, 90)
    ChrSetPos(0x0001, 28370, 0, 26480, 90)
    ChrSetPos(0x0002, 28370, 0, 26480, 90)
    ChrSetPos(0x0003, 28370, 0, 26480, 90)
    OP_4B(0x0014, 255)
    OP_4B(0x0015, 255)
    OP_4B(0x000B, 255)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x0404, 3, 0x2023))
    OP_28(0x00C0, 0x01, 0x0080)
    OP_28(0x00C1, 0x02, 0x0010)
    OP_28(0x00C1, 0x01, 0x0020)
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

# id: 0x0035 offset: 0x7031
@scena.Code('func_35_7031')
def func_35_7031():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, 25350, 0, 25850, 270)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_7058')
    def lambda_7058():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_7058)

    ChrWalkTo(0x00FE, 27020, 0, 26070, 4000, 0x00)
    ChrWalkTo(0x00FE, 28720, 0, 26180, 4000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x0036 offset: 0x7094
@scena.Code('func_36_7094')
def func_36_7094():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, 25350, 0, 25850, 270)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_70BB')
    def lambda_70BB():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_70BB)

    ChrWalkTo(0x00FE, 27020, 0, 26070, 4000, 0x00)
    ChrWalkTo(0x00FE, 28730, 0, 27340, 4000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x0037 offset: 0x70F7
@scena.Code('func_37_70F7')
def func_37_70F7():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, 25350, 0, 25850, 270)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_711E')
    def lambda_711E():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_711E)

    ChrWalkTo(0x00FE, 27020, 0, 26070, 4000, 0x00)
    ChrWalkTo(0x00FE, 27560, 0, 27470, 4000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x0038 offset: 0x715A
@scena.Code('func_38_715A')
def func_38_715A():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, 25350, 0, 25850, 270)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_7181')
    def lambda_7181():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_7181)

    ChrWalkTo(0x00FE, 27260, 0, 25760, 4000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x0039 offset: 0x71A9
@scena.Code('func_39_71A9')
def func_39_71A9():
    FadeOut(0, 0, -1)
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
        (0x00000000, 'loc_7223'),
        (0x00000001, 'loc_7229'),
        (-1, 'loc_722F'),
    )

    def _loc_7223(): pass

    label('loc_7223')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_722F')

    def _loc_7229(): pass

    label('loc_7229')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_722F')

    def _loc_722F(): pass

    label('loc_722F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_723D',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_7241')

    def _loc_723D(): pass

    label('loc_723D')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_7241(): pass

    label('loc_7241')

    Return()

# id: 0x003A offset: 0x7242
@scena.Code('func_3A_7242')
def func_3A_7242():
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

# id: 0x003B offset: 0x729B
@scena.Code('func_3B_729B')
def func_3B_729B():
    OP_13(0x0071)

    Return()

# id: 0x003C offset: 0x729F
@scena.Code('func_3C_729F')
def func_3C_729F():
    OP_13(0x0072)

    Return()

# id: 0x003D offset: 0x72A3
@scena.Code('func_3D_72A3')
def func_3D_72A3():
    OP_13(0x0075)

    Return()

# id: 0x003E offset: 0x72A7
@scena.Code('func_3E_72A7')
def func_3E_72A7():
    OP_13(0x0070)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

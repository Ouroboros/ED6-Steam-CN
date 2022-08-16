import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4106_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4106   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4106.x'
    header.mapIndex       = 1
    header.bgm            = 14
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
        ('ED6_DT07/CH01540._CH', 'ED6_DT07/CH01540P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT07/CH01010._CH', 'ED6_DT07/CH01010P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT07/CH00040._CH', 'ED6_DT07/CH00040P._CP'),
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP'),
        ('ED6_DT27/CH03570._CH', 'ED6_DT27/CH03570P._CP'),
        ('ED6_DT27/CH03510._CH', 'ED6_DT27/CH03510P._CP'),
        ('ED6_DT07/CH02060._CH', 'ED6_DT07/CH02060P._CP'),
        ('ED6_DT07/CH02070._CH', 'ED6_DT07/CH02070P._CP'),
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT07/CH00050._CH', 'ED6_DT07/CH00050P._CP'),
        ('ED6_DT27/CH03080._CH', 'ED6_DT27/CH03080P._CP'),
        ('ED6_DT06/CH20063._CH', 'ED6_DT06/CH20063P._CP'),
        ('ED6_DT06/CH20064._CH', 'ED6_DT06/CH20064P._CP'),
        ('ED6_DT06/CH20038._CH', 'ED6_DT06/CH20038P._CP'),
        ('ED6_DT26/CH20311._CH', 'ED6_DT26/CH20311P._CP'),
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
        ('ED6_DT07/CH01550._CH', 'ED6_DT07/CH01550P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01770._CH', 'ED6_DT07/CH01770P._CP'),
    ]

# id: 0x10001 offset: 0x17A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '接待员菲丝',
            x                   = 58770,
            z                   = 250,
            y                   = 137000,
            direction           = 281,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '卡鲁尼洛',
            x                   = 83950,
            z                   = 1500,
            y                   = 142840,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '蒂法露',
            x                   = 82520,
            z                   = 1500,
            y                   = 142760,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '修理员佩顿',
            x                   = 72500,
            z                   = -10000,
            y                   = 163540,
            direction           = 76,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '鲁特尔',
            x                   = 68650,
            z                   = 250,
            y                   = 147890,
            direction           = 87,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '阿尔丹',
            x                   = 62500,
            z                   = -3000,
            y                   = 169170,
            direction           = 76,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '安敦',
            x                   = 55860,
            z                   = 250,
            y                   = 134560,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '利库斯',
            x                   = 54740,
            z                   = 250,
            y                   = 134560,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 24,
            chipIndex           = 24,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '基蒂',
            x                   = 56060,
            z                   = 250,
            y                   = 145340,
            direction           = 169,
            word_0E             = 0,
            dword_10            = 25,
            chipIndex           = 25,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '村中的老年男性',
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
            name                = '村中的老年女性',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '村中的中年男性',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '村中的中年女性',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '村中的青年男性',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '村中的青年女性',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '奥利维尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '科洛丝',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '提妲',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '金',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '穆拉',
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
            name                = '玲',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '奈尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '朵洛希',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '格雷特纳号的影子',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0189,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '格雷特纳号',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0189,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '雪拉扎德',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '阿加特',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '凯文神父',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '王都格兰赛尔·东街区',
            x                   = 51050,
            z                   = 0,
            y                   = 83440,
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

# id: 0x10002 offset: 0x51A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x51A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 73400,
            y           = 0,
            z           = 140700,
            range       = 76300,
            dword_10    = 0x000007D0,
            dword_14    = 0x00023730,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000016,
        ),
    )

# id: 0x10004 offset: 0x53A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 56800,
            triggerZ            = 250,
            triggerY            = 136940,
            triggerRange        = 800,
            actorX              = 58770,
            actorZ              = 1750,
            actorY              = 137000,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 53710,
            triggerZ            = 250,
            triggerY            = 137720,
            triggerRange        = 800,
            actorX              = 53710,
            actorZ              = 2450,
            actorY              = 137720,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0021,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 71160,
            triggerZ            = -10000,
            triggerY            = 151550,
            triggerRange        = 800,
            actorX              = 71160,
            actorZ              = -8500,
            actorY              = 151550,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0022,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x5A6
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_5BF',
    )

    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)

    Jump('loc_65D')

    def _loc_5BF(): pass

    label('loc_5BF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_608',
    )

    ChrSetPos(0x0009, 81810, 1500, 142750, 183)
    ChrSetPos(0x000A, 72490, -10000, 161070, 110)
    ChrSetFlags(0x000B, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 5, 0x1635)),
            Expr.Return,
        ),
        'loc_605',
    )

    ChrSetPos(0x000D, 57130, 250, 138200, 135)

    def _loc_605(): pass

    label('loc_605')

    Jump('loc_65D')

    def _loc_608(): pass

    label('loc_608')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_63D',
    )

    ChrSetPos(0x0009, 81810, 1500, 142750, 183)
    ChrSetPos(0x000A, 53400, 250, 145320, 183)
    ChrSetFlags(0x000B, 0x0080)

    Jump('loc_65D')

    def _loc_63D(): pass

    label('loc_63D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_64C',
    )

    ChrSetFlags(0x000B, 0x0080)

    Jump('loc_65D')

    def _loc_64C(): pass

    label('loc_64C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_65D',
    )

    ChrSetFlags(0x0009, 0x0010)
    ChrSetFlags(0x000B, 0x0080)

    def _loc_65D(): pass

    label('loc_65D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_685',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x23),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    OP_B1('T4106_4')
    Event(0, func_18_361E)

    Jump('loc_6CB')

    def _loc_685(): pass

    label('loc_685')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_6AD',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x23),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    MapSetFlags(0x10000000)
    OP_B1('T4106_4')
    Event(0, func_19_3E28)

    Jump('loc_6CB')

    def _loc_6AD(): pass

    label('loc_6AD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6CB',
    )

    MapSetFlags(0x10000000)
    OP_B1('T4106_1')
    Event(0, func_0D_1458)

    def _loc_6CB(): pass

    label('loc_6CB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 5, 0x1635)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 6, 0x1636)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_720',
    )

    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x001B, 0x0080)
    ChrSetFlags(0x001B, 0x0040)
    ChrSetPos(0x0017, 81740, 1500, 143050, 90)
    ChrSetPos(0x001B, 83170, 1500, 143050, 270)
    CreateThread(0x0017, 0x00, 0x00, func_02_7C1)
    CreateThread(0x001B, 0x00, 0x00, func_02_7C1)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000C, 0x0080)

    def _loc_720(): pass

    label('loc_720')

    Return()

# id: 0x0001 offset: 0x721
@scena.Code('func_01_721')
def func_01_721():
    OP_16(0x02, 4000, -43000, 29000, 2293855)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_74B',
    )

    OP_B1('T4106_4')

    Jump('loc_7C0')

    def _loc_74B(): pass

    label('loc_74B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 5, 0x1635)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 6, 0x1636)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_781',
    )

    OP_B1('T4106_2')
    OP_72(0x0005, 0x0004)
    OP_72(0x000A, 0x0004)
    OP_72(0x000B, 0x0004)
    OP_72(0x000C, 0x0004)
    OP_72(0x000D, 0x0004)
    OP_71(0x0009, 0x0004)

    Jump('loc_7C0')

    def _loc_781(): pass

    label('loc_781')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 5, 0x1625)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 6, 0x1626)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 4, 0x162C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7A1',
    )

    OP_B1('T4106_6')

    Jump('loc_7C0')

    def _loc_7A1(): pass

    label('loc_7A1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_7C0',
    )

    OP_B1('T4106_1')
    OP_71(0x0005, 0x0004)
    OP_71(0x000A, 0x0004)
    OP_71(0x000B, 0x0004)

    def _loc_7C0(): pass

    label('loc_7C0')

    Return()

# id: 0x0002 offset: 0x7C1
@scena.Code('func_02_7C1')
def func_02_7C1():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_7D6',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_7C1')

    def _loc_7D6(): pass

    label('loc_7D6')

    Return()

# id: 0x0003 offset: 0x7D7
@scena.Code('func_03_7D7')
def func_03_7D7():
    Call(0, 0x0004)

    Return()

# id: 0x0004 offset: 0x7DC
@scena.Code('func_04_7DC')
def func_04_7DC():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_841',
    )

    ChrTalk(
        0x0008,
        (
            '当前由于导力全部停止工作\n',
            '飞船无法运行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '退票工作\n',
            '在这边受理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '非常抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9D3')

    def _loc_841(): pass

    label('loc_841')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_84B',
    )

    Jump('loc_9D3')

    def _loc_84B(): pass

    label('loc_84B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_8E8',
    )

    ChrTalk(
        0x0008,
        (
            '欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 5, 0x1635)),
            Expr.Return,
        ),
        'loc_8BE',
    )

    ChrTalk(
        0x0008,
        (
            '由东边绕行的定期船，\n',
            '林德号马上就要起飞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '请准备搭乘的客人\n',
            '抓紧时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8E5')

    def _loc_8BE(): pass

    label('loc_8BE')

    ChrTalk(
        0x0008,
        (
            '由东边绕行的定期船，\n',
            '林德号到达。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8E5(): pass

    label('loc_8E5')

    Jump('loc_9D3')

    def _loc_8E8(): pass

    label('loc_8E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_937',
    )

    ChrTalk(
        0x0008,
        (
            '真对不起，本日的定期船\n',
            '航行全部结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '欢迎下次光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9D3')

    def _loc_937(): pass

    label('loc_937')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_972',
    )

    ChrTalk(
        0x0008,
        (
            '欢迎光临。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '需要买票的乘客\n',
            '请到这边来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9D3')

    def _loc_972(): pass

    label('loc_972')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_9D3',
    )

    ChrTalk(
        0x0008,
        (
            '十分感谢您\n',
            '搭乘定期飞行船。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '找公司办理业务的客人，\n',
            '请到那边的建筑物中的接待点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9D3(): pass

    label('loc_9D3')

    TalkEnd(0x0008)

    Return()

# id: 0x0005 offset: 0x9D7
@scena.Code('func_05_9D7')
def func_05_9D7():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_A61',
    )

    ChrTalk(
        0x00FE,
        (
            '赛希莉亚号和林德号\n',
            '好像分别停在\n',
            '柏斯和洛连特',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样的话也没办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只好将错就错\n',
            '一边进行飞船坪的修整一边等候吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BF2')

    def _loc_A61(): pass

    label('loc_A61')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_ABB',
    )

    ChrTalk(
        0x00FE,
        (
            '这个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到修整林德号\n',
            '的时间了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '蒂法露去哪儿了？\n',
            '已经走了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BF2')

    def _loc_ABB(): pass

    label('loc_ABB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 5, 0x1635)),
            Expr.Return,
        ),
        'loc_AC5',
    )

    Jump('loc_BF2')

    def _loc_AC5(): pass

    label('loc_AC5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_B00',
    )

    ChrTalk(
        0x00FE,
        (
            '这个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '蒂法露去哪儿了？\n',
            '已经走了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BF2')

    def _loc_B00(): pass

    label('loc_B00')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_B58',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本来是准备\n',
            '请蒂法露加班来着，\n',
            '但不太好意思，结果就没说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BF2')

    def _loc_B58(): pass

    label('loc_B58')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_B9B',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，检、检查表\n',
            '忘记交了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '得赶快制作才行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BF2')

    def _loc_B9B(): pass

    label('loc_B9B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_BF2',
    )

    ChrTalk(
        0x00FE,
        (
            '哎～蒂法露\n',
            '接下来的工作是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，对了，导力插头\n',
            '不是可以拜托订货吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BF2(): pass

    label('loc_BF2')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0xBF6
@scena.Code('func_06_BF6')
def func_06_BF6():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_C76',
    )

    ChrTalk(
        0x00FE,
        (
            '我还以为维修主任\n',
            '会比平时更惊慌失措呢',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没想到被逼到绝境时\n',
            '反而这么冷静。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是总是这么稳重，\n',
            '就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EB2')

    def _loc_C76(): pass

    label('loc_C76')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_D82',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 5, 0x1635)),
            Expr.Return,
        ),
        'loc_D1E',
    )

    ChrTalk(
        0x00FE,
        (
            '『ＸＧ－０２』\n',
            '查看了样品引擎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然在佩顿那里\n',
            '看到过作法，\n',
            '可是没想到居然能做成那么小……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘻嘻，看来，可以对工作起到很好的激励作用哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D7F')

    def _loc_D1E(): pass

    label('loc_D1E')

    ChrTalk(
        0x00FE,
        (
            '对不起，能不扰乱我吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '已经决定\n',
            '立即使用这边的航道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '必须得开始对各处的检查了…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D7F(): pass

    label('loc_D7F')

    Jump('loc_EB2')

    def _loc_D82(): pass

    label('loc_D82')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_DDB',
    )

    ChrTalk(
        0x00FE,
        (
            '今天的工作结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好了，要不要回去冲个凉\n',
            '然后和朋友去喝两杯呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EB2')

    def _loc_DDB(): pass

    label('loc_DDB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_E6A',
    )

    ChrTalk(
        0x00FE,
        (
            '唉，『埃尔赛尤』不在\n',
            '还真是寂寞呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '专职修理工佩顿\n',
            '就不能快点回来吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只有我和维修主任两个人的话，\n',
            '完全没有干劲嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EB2')

    def _loc_E6A(): pass

    label('loc_E6A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_EB2',
    )

    ChrTalk(
        0x00FE,
        (
            '我们的维修主任\n',
            '一如既往的软弱靠不住。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是没有办法……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EB2(): pass

    label('loc_EB2')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0xEB6
@scena.Code('func_07_EB6')
def func_07_EB6():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0xEBD
@scena.Code('func_08_EBD')
def func_08_EBD():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_F73',
    )

    ChrTalk(
        0x00FE,
        (
            '现在要返回蔡斯了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和爱尔莎大使纠缠了好久\n',
            '终于要答应让我们买定期船了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '『近期内会同意的』\n',
            '她是这么说的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗬，这么困难的贸易谈判\n',
            '还真是第一次见……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10D1')

    def _loc_F73(): pass

    label('loc_F73')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_FD5',
    )

    ChrTalk(
        0x00FE,
        (
            '今天的计划\n',
            '也被爱尔莎大使顶回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个人，总是很敏锐地\n',
            '击中我们的要害～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10D1')

    def _loc_FD5(): pass

    label('loc_FD5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_105C',
    )

    ChrTalk(
        0x00FE,
        (
            '不过终于要同意\n',
            '让共和国购买定期船了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '关于价格\n',
            '和对方一直谈不拢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个女共和国大使……\n',
            '是个不容小视的干将呢',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10D1')

    def _loc_105C(): pass

    label('loc_105C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_10D1',
    )

    ChrTalk(
        0x00FE,
        (
            '马上有一个和共和国大使馆\n',
            '的贸易谈判。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们去和共和国大使交涉,\n',
            '并请求购买\n',
            '与飞船定期船同型号的商品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10D1(): pass

    label('loc_10D1')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x10D5
@scena.Code('func_09_10D5')
def func_09_10D5():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_129E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 5, 0x1635)),
            Expr.Return,
        ),
        'loc_1241',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_11CE',
    )

    ChrTalk(
        0x00FE,
        (
            '不、不好了！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '刚才我偷听了\n',
            '从莱普尼兹号下来的修理员的谈话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听说正在雷斯顿要塞\n',
            '进行替换『埃尔赛尤』引擎的工作！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不能这样做啊。\n',
            '我必须马上返回蔡斯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '等等，『埃尔赛尤』！\n',
            '这次一定要抓住你！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_123E')

    def _loc_11CE(): pass

    label('loc_11CE')

    ChrTalk(
        0x00FE,
        (
            '这么说来，刚才运走一个\n',
            '我从没见过的引擎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那是什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……啊，更重要的是\n',
            '必须尽快搭乘林德号！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_123E(): pass

    label('loc_123E')

    Jump('loc_129B')

    def _loc_1241(): pass

    label('loc_1241')

    ChrTalk(
        0x00FE,
        (
            '这边的航道\n',
            '好像也在做着陆准备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '什么啊……\n',
            '是军用艇的紧急着陆吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_129B(): pass

    label('loc_129B')

    Jump('loc_143F')

    def _loc_129E(): pass

    label('loc_129E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_131A',
    )

    ChrTalk(
        0x00FE,
        (
            '真奇怪啊。\n',
            '我试着做了大量调查……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '『埃尔赛尤』现在并没有停在\n',
            '任何一个飞船坪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难道去国外了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_143F')

    def _loc_131A(): pass

    label('loc_131A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_137C',
    )

    ChrTalk(
        0x00FE,
        (
            '『埃尔赛尤』\n',
            '到哪里去了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '事已至此，一定要查明它的去处\n',
            '哪怕追到天涯海角！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_143F')

    def _loc_137C(): pass

    label('loc_137C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_143F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_13F4',
    )

    ChrTalk(
        0x00FE,
        (
            '为什么，为什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好不容易，来到了王都……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为什么『埃尔赛尤』\n',
            '不在这里啊───！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_143F')

    def _loc_13F4(): pass

    label('loc_13F4')

    ChrTalk(
        0x00FE,
        (
            '好不容易，来到了王都……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为什么『埃尔赛尤』\n',
            '不在这里啊───！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_143F(): pass

    label('loc_143F')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x1443
@scena.Code('func_0A_1443')
def func_0A_1443():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x144A
@scena.Code('func_0B_144A')
def func_0B_144A():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x1451
@scena.Code('func_0C_1451')
def func_0C_1451():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x1458
@scena.Code('func_0D_1458')
def func_0D_1458():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1469',
    )

    Call(0, 0x001D)

    def _loc_1469(): pass

    label('loc_1469')

    EventBegin(0x00)
    OP_DB()
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x0010, 0x0080)
    OP_11(0xFF, 0xFF, 0xFF, 80000, 350000, 0)
    OP_12(0x0000EA60, 0x00055730, 0x00000000)
    OP_12(0x0000AFC8, 0x00055730, 0x00002710)
    CameraMove(58630, 40000, 116260, 0)
    OP_67(0, 45000, -50000, 0)
    CameraSetDistance(800, 0)
    OP_6C(60000, 0)
    OP_6E(250, 0)
    OP_A1(0x001F, 0x000A)
    OP_72(0x000A, 0x0004)
    OP_72(0x000A, 0x0020)
    ChrSetPos(0x001F, 87140, 15900, 130979, 90)
    ChrSetFlags(0x001F, 0x0004)
    OP_A1(0x0020, 0x000B)
    OP_71(0x000B, 0x0002)
    OP_72(0x000B, 0x0004)
    ChrSetPos(0x0020, 87140, 5900, 130979, 90)
    ChrSetFlags(0x0020, 0x0004)
    OP_71(0x0009, 0x0004)
    OP_6F(0x0005, 100)
    OP_6F(0x000A, 60)
    OP_6F(0x000B, 0)
    PlaySE(121, 0x00, 0x64)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_1572',
    )

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    Jump('loc_1576')

    def _loc_1572(): pass

    label('loc_1572')

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    def _loc_1576(): pass

    label('loc_1576')

    CreateThread(0x0101, 0x00, 0x00, func_15_1E7C)
    OP_C8(0x0200, 0x0046, 'C_PLAC04._CH', 0x00, 0x07D0)
    ShowPlaceName('王都格兰赛尔')
    FadeIn(2000, 0)
    WaitForThreadExit(0x0101, 0x0000)
    Fade(1000)
    CameraMove(83040, 1500, 131020, 0)
    OP_67(0, 6970, -10000, 0)
    CameraSetDistance(3820, 0)
    OP_6C(148000, 0)
    OP_6E(262, 0)
    OP_12(0x000088B8, 0x00055730, 0x00000000)
    OP_0D()
    PlaySE(6, 0x00, 0x64)
    OP_6F(0x000A, 411)
    OP_70(0x000A, 450)
    Sleep(1300)

    CreateThread(0x0011, 0x01, 0x00, func_0E_1B95)
    Sleep(500)

    CreateThread(0x0012, 0x01, 0x00, func_0E_1B95)
    Sleep(800)

    CreateThread(0x0013, 0x01, 0x00, func_0E_1B95)
    Sleep(800)

    CreateThread(0x0014, 0x01, 0x00, func_0E_1B95)
    Sleep(1000)

    CreateThread(0x0101, 0x01, 0x00, func_0F_1BF2)
    Sleep(800)

    CreateThread(0x00F7, 0x01, 0x00, func_10_1C51)
    Sleep(800)

    CreateThread(0x0018, 0x01, 0x00, func_11_1CC4)
    Sleep(800)

    CreateThread(0x0017, 0x01, 0x00, func_12_1D37)
    Sleep(800)

    CreateThread(0x0019, 0x01, 0x00, func_13_1DAA)
    Sleep(800)

    CreateThread(0x001A, 0x01, 0x00, func_14_1E1D)
    Sleep(500)

    @scena.Lambda('lambda_1694')
    def lambda_1694():
        CameraMove(79270, 1500, 142560, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1694)

    WaitForThreadExit(0x001A, 0x0001)
    OP_DC()

    ChrTalk(
        0x0101,
        (
            '#0010240588V#1006F好了……\n',
            '又返回王都了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240589V无论如何\n',
            '先去游击士协会吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_174E',
    )

    ChrTalk(
        0x0106,
        (
            '#0050240590V#051F对啊，听听艾南那边\n',
            '的所谓的军队意见吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_178C')

    def _loc_174E(): pass

    label('loc_174E')

    ChrTalk(
        0x0103,
        (
            '#0030240591V#020F好的，听听艾南那边\n',
            '的所谓的军队意见吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_178C(): pass

    label('loc_178C')

    ChrTalk(
        0x0017,
        (
            '#0040240592V#033F对了，今天那只白色的船\n',
            '没停泊在飞船坪呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040240593V它是叫『埃尔赛尤』吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240594V#1015F咦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1812')
    def lambda_1812():
        ChrSetDirection(0x00FE, 360, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1812)

    Sleep(50)

    @scena.Lambda('lambda_1825')
    def lambda_1825():
        ChrSetDirection(0x00FE, 360, 400)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_1825)

    Sleep(50)

    @scena.Lambda('lambda_1838')
    def lambda_1838():
        ChrSetDirection(0x00FE, 360, 400)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_1838)

    Sleep(50)

    @scena.Lambda('lambda_184B')
    def lambda_184B():
        ChrSetDirection(0x00FE, 360, 400)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_184B)

    Sleep(500)

    Fade(1000)
    CameraMove(79890, 1500, 146670, 0)
    OP_67(0, 7730, -10000, 0)
    CameraSetDistance(1930, 0)
    OP_6C(33000, 0)
    OP_6E(589, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010240595V#1004F#6P啊，真的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '#0080240596V#070F我没记错的话那是王室的巡洋舰吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080240597V到哪里\n',
            '执行任务去了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    CameraMove(79270, 1500, 142560, 0)
    OP_67(0, 6970, -10000, 0)
    CameraSetDistance(3820, 0)
    OP_6C(148000, 0)
    OP_6E(262, 0)
    OP_0D()

    @scena.Lambda('lambda_196A')
    def lambda_196A():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_196A)

    Sleep(50)

    @scena.Lambda('lambda_197D')
    def lambda_197D():
        ChrSetDirection(0x00FE, 177, 400)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_197D)

    Sleep(50)

    @scena.Lambda('lambda_1990')
    def lambda_1990():
        ChrSetDirection(0x00FE, 177, 400)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_1990)

    Sleep(50)

    @scena.Lambda('lambda_19A3')
    def lambda_19A3():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_19A3)

    Sleep(500)

    ChrTalk(
        0x0018,
        (
            '#0060240598V#040F『埃尔赛尤』\n',
            '刚好去了雷斯顿要塞。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060240599V听说要在那里装载\n',
            '刚刚完成的新型引擎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '#0070240600V#061F啊，维修长他们也\n',
            '乘工房船\n',
            '去雷斯顿要塞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010240601V#1004F咦～是这样的吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240602V#1006F也就是说，那条很帅气的船\n',
            '要升级得更厉害了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010240603V不知会变成什么样子，值得期待。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '#0070240604V#560F只是换个引擎而已,\n',
            '我想外表不会有什么变化……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070240605V#061F不过会变成世界上最快的船，\n',
            '这一点应该是毫无疑问的⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(500)

    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T4121._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000E offset: 0x1B95
@scena.Code('func_0E_1B95')
def func_0E_1B95():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetBattleFlags(0x00FE, 0x0020)
    OP_89(0x00FE, 87110, 1500, 130990, 270)
    ChrWalkTo(0x00FE, 82940, 1500, 130970, 2000, 0x00)
    ChrWalkTo(0x00FE, 82940, 1500, 143070, 2000, 0x00)
    ChrWalkTo(0x00FE, 66850, 1500, 143270, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x000F offset: 0x1BF2
@scena.Code('func_0F_1BF2')
def func_0F_1BF2():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetBattleFlags(0x00FE, 0x0020)
    OP_89(0x00FE, 87110, 1500, 130990, 270)
    ChrWalkTo(0x00FE, 82940, 1500, 130970, 2000, 0x00)
    ChrWalkTo(0x00FE, 82940, 1500, 143070, 2000, 0x00)
    ChrWalkTo(0x00FE, 77990, 1500, 143060, 2000, 0x00)
    ChrSetDirection(0x00FE, 102, 400)

    Return()

# id: 0x0010 offset: 0x1C51
@scena.Code('func_10_1C51')
def func_10_1C51():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetBattleFlags(0x00FE, 0x0020)
    OP_89(0x00FE, 87110, 1500, 130990, 270)
    ChrWalkTo(0x00FE, 82940, 1500, 130970, 2000, 0x00)
    ChrWalkTo(0x00FE, 82940, 1500, 143070, 2000, 0x00)
    ChrWalkTo(0x00FE, 80980, 1500, 143080, 2000, 0x00)
    ChrWalkTo(0x00FE, 78920, 1500, 142160, 2000, 0x00)
    ChrSetDirection(0x00FE, 357, 400)

    Return()

# id: 0x0011 offset: 0x1CC4
@scena.Code('func_11_1CC4')
def func_11_1CC4():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetBattleFlags(0x00FE, 0x0020)
    OP_89(0x00FE, 87110, 1500, 130990, 270)
    ChrWalkTo(0x00FE, 82940, 1500, 130970, 2000, 0x00)
    ChrWalkTo(0x00FE, 82940, 1500, 143070, 2000, 0x00)
    ChrWalkTo(0x00FE, 80980, 1500, 143080, 2000, 0x00)
    ChrWalkTo(0x00FE, 78720, 1500, 143890, 2000, 0x00)
    ChrSetDirection(0x00FE, 177, 400)

    Return()

# id: 0x0012 offset: 0x1D37
@scena.Code('func_12_1D37')
def func_12_1D37():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetBattleFlags(0x00FE, 0x0020)
    OP_89(0x00FE, 87110, 1500, 130990, 270)
    ChrWalkTo(0x00FE, 82940, 1500, 130970, 2000, 0x00)
    ChrWalkTo(0x00FE, 82940, 1500, 143070, 2000, 0x00)
    ChrWalkTo(0x00FE, 80980, 1500, 143080, 2000, 0x00)
    ChrWalkTo(0x00FE, 79880, 1500, 142220, 2000, 0x00)
    ChrSetDirection(0x00FE, 357, 400)

    Return()

# id: 0x0013 offset: 0x1DAA
@scena.Code('func_13_1DAA')
def func_13_1DAA():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetBattleFlags(0x00FE, 0x0020)
    OP_89(0x00FE, 87110, 1500, 130990, 270)
    ChrWalkTo(0x00FE, 82940, 1500, 130970, 2000, 0x00)
    ChrWalkTo(0x00FE, 82940, 1500, 143070, 2000, 0x00)
    ChrWalkTo(0x00FE, 80980, 1500, 143080, 2000, 0x00)
    ChrWalkTo(0x00FE, 79960, 1500, 143880, 2000, 0x00)
    ChrSetDirection(0x00FE, 201, 400)

    Return()

# id: 0x0014 offset: 0x1E1D
@scena.Code('func_14_1E1D')
def func_14_1E1D():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetBattleFlags(0x00FE, 0x0020)
    OP_89(0x00FE, 87110, 1500, 130990, 270)
    ChrWalkTo(0x00FE, 82940, 1500, 130970, 2000, 0x00)
    ChrWalkTo(0x00FE, 82940, 1500, 143070, 2000, 0x00)
    ChrWalkTo(0x00FE, 80980, 1500, 143080, 2000, 0x00)
    ChrSetDirection(0x00FE, 261, 400)

    Return()

# id: 0x0015 offset: 0x1E7C
@scena.Code('func_15_1E7C')
def func_15_1E7C():
    @scena.Lambda('lambda_1E82')
    def lambda_1E82():
        CameraMove(58630, 30000, 116260, 8000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_1E82)

    @scena.Lambda('lambda_1E9A')
    def lambda_1E9A():
        ChrMoveTo(0x00FE, 87140, -5650, 130979, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_1E9A)

    @scena.Lambda('lambda_1EB5')
    def lambda_1EB5():
        ChrMoveTo(0x00FE, 87140, -5650, 130979, 500, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_1EB5)

    Sleep(100)

    @scena.Lambda('lambda_1ED5')
    def lambda_1ED5():
        ChrMoveTo(0x00FE, 87140, -5650, 130979, 700, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_1ED5)

    Sleep(100)

    @scena.Lambda('lambda_1EF5')
    def lambda_1EF5():
        ChrMoveTo(0x00FE, 87140, -5650, 130979, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_1EF5)

    Sleep(100)

    @scena.Lambda('lambda_1F15')
    def lambda_1F15():
        ChrMoveTo(0x00FE, 87140, -5650, 130979, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_1F15)

    Sleep(100)

    @scena.Lambda('lambda_1F35')
    def lambda_1F35():
        ChrMoveTo(0x00FE, 87140, -5650, 130979, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_1F35)

    Sleep(100)

    @scena.Lambda('lambda_1F55')
    def lambda_1F55():
        ChrMoveTo(0x00FE, 87140, -5650, 130979, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_1F55)

    Sleep(100)

    @scena.Lambda('lambda_1F75')
    def lambda_1F75():
        ChrMoveTo(0x00FE, 87140, -5650, 130979, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_1F75)

    Sleep(100)

    @scena.Lambda('lambda_1F95')
    def lambda_1F95():
        ChrMoveTo(0x00FE, 87140, -5650, 130979, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_1F95)

    Sleep(100)

    Sleep(4000)

    @scena.Lambda('lambda_1FBA')
    def lambda_1FBA():
        ChrMoveTo(0x00FE, 87140, -5650, 130979, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_1FBA)

    @scena.Lambda('lambda_1FD5')
    def lambda_1FD5():
        ChrMoveTo(0x00FE, 87140, -5650, 130979, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_1FD5)

    Sleep(300)

    @scena.Lambda('lambda_1FF5')
    def lambda_1FF5():
        ChrMoveTo(0x00FE, 87140, -5650, 130979, 2200, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_1FF5)

    Sleep(300)

    @scena.Lambda('lambda_2015')
    def lambda_2015():
        ChrMoveTo(0x00FE, 87140, -5650, 130979, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_2015)

    Sleep(300)

    @scena.Lambda('lambda_2035')
    def lambda_2035():
        ChrMoveTo(0x00FE, 87140, -5650, 130979, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_2035)

    Sleep(300)

    @scena.Lambda('lambda_2055')
    def lambda_2055():
        ChrMoveTo(0x00FE, 87140, -5650, 130979, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_2055)

    Sleep(300)

    @scena.Lambda('lambda_2075')
    def lambda_2075():
        ChrMoveTo(0x00FE, 87140, -5650, 130979, 700, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_2075)

    Sleep(300)

    @scena.Lambda('lambda_2095')
    def lambda_2095():
        ChrMoveTo(0x00FE, 87140, -5650, 130979, 600, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_2095)

    Sleep(300)

    @scena.Lambda('lambda_20B5')
    def lambda_20B5():
        ChrMoveTo(0x00FE, 87140, -5650, 130979, 500, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_20B5)

    Sleep(300)

    @scena.Lambda('lambda_20D5')
    def lambda_20D5():
        ChrMoveTo(0x00FE, 87140, -5650, 130979, 400, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_20D5)

    @scena.Lambda('lambda_20F0')
    def lambda_20F0():
        ChrMoveTo(0x00FE, 87140, -5650, 130979, 800, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_20F0)

    WaitForThreadExit(0x001F, 0x0001)
    WaitForThreadExit(0x0020, 0x0001)
    OP_23(0x0079)
    PlaySE(200, 0x00, 0x64)
    OP_7C(0, 100, 3000, 100)
    ChrSetPos(0x001F, 87140, -5650, 130979, 90)
    Sleep(1000)

    PlaySE(118, 0x00, 0x46)
    OP_6F(0x000A, 60)
    OP_70(0x000A, 1)
    Sleep(1300)

    PlaySE(120, 0x00, 0x64)
    OP_6F(0x0005, 100)
    OP_70(0x0005, 200)
    Sleep(2500)

    TerminateThread(0x0000, 0x01)

    Return()

# id: 0x0016 offset: 0x2173
@scena.Code('func_16_2173')
def func_16_2173():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 5, 0x1635)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 6, 0x1636)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_2180',
    )

    Return()

    def _loc_2180(): pass

    label('loc_2180')

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
        'loc_21A0',
    )

    Call(0, 0x001D)
    Call(0, 0x001E)
    FadeIn(0, 0)

    def _loc_21A0(): pass

    label('loc_21A0')

    PlaySE(166, 0x00, 0x64)
    Sleep(1000)

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('女性的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0880260807V前往蔡斯方向的定期飞船\n',
            '『林德号』就要起飞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    TalkSetChrName('女性的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0880260808V需要乘坐的旅客请立即登船。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Fade(1000)
    OP_71(0x0009, 0x0004)
    OP_6F(0x0005, 1)
    ChrClearFlags(0x0017, 0x0080)
    ChrClearFlags(0x001B, 0x0080)
    ChrSetFlags(0x001B, 0x0040)
    OP_4A(0x0017, 255)
    OP_4A(0x001B, 255)
    ChrSetPos(0x0017, 82970, 1500, 143180, 180)
    ChrSetPos(0x001B, 82970, 1500, 139130, 180)

    @scena.Lambda('lambda_2293')
    def lambda_2293():
        ChrWalkTo(0x00FE, 83050, 1500, 134000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_2293)

    CameraMove(82960, 1500, 138300, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(129000, 0)
    OP_6E(262, 0)
    PlaySE(117, 0x00, 0x64)
    OP_0D()
    WaitForThreadExit(0x001B, 0x0001)
    ChrSetDirection(0x001B, 0, 400)
    OP_E5(0x17, 0x00, 0x00)
    Sleep(500)

    ChrTalk(
        0x001B,
        (
            '#0110260809V#270F再见了，奥利维尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110260810V我不在的这段期间\n',
            '可别搞出什么问题来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#0040260811V#037F#1P哼，放心好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040260812V我做过什么\n',
            '让心爱的你担心的事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#0110260813V#272F过了这阵子\n',
            '我也担心不起来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110260814V你起码保证别出什么问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#0040260815V#031F#1P嗯，妥善处理吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A1(0x001F, 0x000A)
    OP_72(0x000A, 0x0004)
    OP_72(0x000A, 0x0020)
    ChrSetPos(0x001F, 87140, -5650, 130979, 90)
    ChrSetFlags(0x001F, 0x0004)
    OP_A1(0x0020, 0x000B)
    ChrSetPos(0x0020, 87140, -5650, 130979, 90)
    ChrSetFlags(0x0020, 0x0004)
    Fade(500)
    OP_72(0x000B, 0x0004)
    OP_0D()
    Call(0, 0x0017)
    Sleep(1000)

    CameraMove(82970, 1500, 143180, 0)
    OP_67(0, 6320, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(151000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 76000, 1500, 142810, 90)
    ChrSetPos(0x0107, 76000, 1500, 143700, 90)
    ChrSetPos(0x00F7, 76000, 1500, 144000, 90)
    ChrSetPos(0x00F9, 76000, 1500, 142470, 90)
    ChrSetPos(0x001C, 70560, 1500, 143120, 90)
    ChrClearFlags(0x001C, 0x0080)
    ChrSetPos(0x001C, 70560, 1500, 143120, 90)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010260816V#1P喂，奥利维尔！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0017, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTurnDirection(0x0017, 0x0101, 400)

    @scena.Lambda('lambda_2586')
    def lambda_2586():
        CameraMove(82140, 1500, 142960, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2586)

    @scena.Lambda('lambda_259E')
    def lambda_259E():
        ChrWalkTo(0x00FE, 80270, 1500, 142810, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_259E)

    Sleep(100)

    @scena.Lambda('lambda_25BE')
    def lambda_25BE():
        ChrWalkTo(0x00FE, 80370, 1500, 143700, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_25BE)

    Sleep(700)

    @scena.Lambda('lambda_25DE')
    def lambda_25DE():
        ChrWalkTo(0x00FE, 79340, 1500, 144000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_25DE)

    Sleep(100)

    @scena.Lambda('lambda_25FE')
    def lambda_25FE():
        ChrWalkTo(0x00FE, 79340, 1500, 142470, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_25FE)

    WaitForThreadExit(0x0101, 0x0003)
    WaitForThreadExit(0x00F9, 0x0001)

    ChrTalk(
        0x0017,
        (
            '#0040260817V#033F#5P哟，是你们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040260818V#031F难道是舍不得我\n',
            '所以找到这里来了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_267F')
    def lambda_267F():
        ChrWalkTo(0x00FE, 75560, 1500, 143120, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_267F)

    ChrTalk(
        0x0101,
        (
            '#0010260819V#1007F#2P怎么可能嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260820V#1015F不过……\n',
            '刚才那是穆拉吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2724',
    )

    ChrTalk(
        0x0106,
        (
            '#0050260821V#052F为什么帝国军人\n',
            '在使用飞船？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2758')

    def _loc_2724(): pass

    label('loc_2724')

    ChrTalk(
        0x0103,
        (
            '#0030260822V#023F为什么帝国的军人\n',
            '在使用飞船？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2758(): pass

    label('loc_2758')

    ChrTalk(
        0x0017,
        (
            '#0040260823V#030F#5P啊，好像是因为军务\n',
            '要去柏斯地区。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040260824V不是有空贼团\n',
            '用过的飞艇吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040260825V好像打算回收那个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260826V#1004F#2P空贼团的飞艇\n',
            '是那个绿色的小型艇吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260827V但是，为什么是穆拉去？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#0040260828V#035F#5P或许你已经知道\n',
            '那艘飞艇是埃雷波尼亚制的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040260829V使用它的空贼团\n',
            '好像至今没被捉住。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040260830V#030F作为帝国政府，想要回收证据\n',
            '以此配合搜查……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040260831V据说这样试探过王国。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260832V#1015F#2P嗯？\n',
            '真是难以理解的理由。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#0040260833V#031F#5P唉，空贼团\n',
            '是埃雷波尼亚原贵族这事\n',
            '传出去不大好听。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040260834V大概是想尽可能在缔结互不侵犯条约之前\n',
            '把事情不了了之地蒙混过去吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040260835V在共和国深入人心之前。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260836V#1015F#2P据说空贼团是原帝国贵族……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260837V#1020F哎，那个男人婆是……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#0040260838V#033F#5P咦，你不知道吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040260839V#030F据说是帝国北部\n',
            '一个叫做卡普亚男爵家的小领主。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040260840V据说数年前，由于负债累累\n',
            '而卖掉了领土。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260841V#1015F#2P有、有这种事吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260842V#1007F怎么说呢……\n',
            '这些家伙也算有点可怜吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2BAD',
    )

    ChrTalk(
        0x0106,
        (
            '#0050260843V#053F嘁，即使这样\n',
            '仍然让人完全无法同情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2BE5')

    def _loc_2BAD(): pass

    label('loc_2BAD')

    ChrTalk(
        0x0103,
        (
            '#0030260844V#027F是啊，即使这样\n',
            '也不太令人同情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2BE5(): pass

    label('loc_2BE5')

    ChrTalk(
        0x0017,
        (
            '#0040260845V#035F#5P好了，就是这么回事\n',
            '我是来送行的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040260846V#030F你们在空港做什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260847V#1015F#2P啊，其实我们是\n',
            '是来这里找玲的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260848V奥利维尔，你看到她了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#0040260849V#033F#5P玲？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040260850V那边那个\n',
            '不是玲吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260851V#1004F#2P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x001C, 0x0080)
    ChrSetPos(0x001C, 75560, 1500, 143120, 90)

    @scena.Lambda('lambda_2D23')
    def lambda_2D23():
        CameraMove(79810, 1500, 142310, 1600)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2D23)

    @scena.Lambda('lambda_2D3B')
    def lambda_2D3B():
        OP_67(0, 5590, -10000, 1600)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2D3B)

    @scena.Lambda('lambda_2D53')
    def lambda_2D53():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2D53)

    Sleep(100)

    @scena.Lambda('lambda_2D66')
    def lambda_2D66():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_2D66)

    Sleep(100)

    @scena.Lambda('lambda_2D79')
    def lambda_2D79():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_2D79)

    Sleep(100)

    @scena.Lambda('lambda_2D8C')
    def lambda_2D8C():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_2D8C)

    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x001C,
        (
            '#0220260852V#261F#2P嗯⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070260853V#065F#6P玲、玲！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260854V#1020F#5P你什么时候……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2E0A')
    def lambda_2E0A():
        CameraMove(78000, 1500, 142310, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2E0A)

    ChrWalkTo(0x0101, 77170, 1500, 143070, 2000, 0x00)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010260855V#1019F#5P喂，玲！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260856V真是的\n',
            '你怎么能突然玩失踪呢！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260857V而且牵连那么多人\n',
            '从我们身边逃跑～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '#0220260858V#268F#2P对不起……\n',
            '因为我很无聊啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220260859V#267F那个～\n',
            '我从百货店买了红茶和小甜饼干哟！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220260860V也有大家的份儿，\n',
            '所以拜托，别生气了好不好？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260861V#1015F#5P哼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2FFF',
    )

    ChrTalk(
        0x0108,
        (
            '#0080260862V#071F#5P哈哈，因为玲的胡闹，\n',
            '我们也得到了很多快乐啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080260863V这下就算扯平了，不也挺好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3059')

    def _loc_2FFF(): pass

    label('loc_2FFF')

    ChrTalk(
        0x0105,
        (
            '#0060260864V#048F#5P呵呵，我们也\n',
            '玩得很开心……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060260865V这样的话就算扯平\n',
            '了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3059(): pass

    label('loc_3059')

    ChrTalk(
        0x0101,
        (
            '#0010260866V#1007F#5P哈，真是没办法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260867V#1017F那就\n',
            '原谅你好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '#0220260868V#265F#2P真的吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070260869V#061F嘿嘿，太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3152',
    )

    ChrTalk(
        0x0106,
        (
            '#0050260870V#051F#5P那么\n',
            '先回游击士协会吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050260871V说不定\n',
            '会有什么情报呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_31A8')

    def _loc_3152(): pass

    label('loc_3152')

    ChrTalk(
        0x0103,
        (
            '#0030260872V#021F#5P那么\n',
            '先回游击士协会吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030260873V说不定\n',
            '会有什么情报呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_31A8(): pass

    label('loc_31A8')

    @scena.Lambda('lambda_31AE')
    def lambda_31AE():
        CameraMove(79810, 1500, 142310, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_31AE)

    ChrTurnDirection(0x0101, 0x0017, 400)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010260874V#1006F#2P嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#0040260875V#033F咦，出什么事了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260876V#1015F#2P好像是柏斯地区\n',
            '发生了什么事件。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010260877V#1004F唔……\n',
            '这么说来\n',
            '穆拉不是去了柏斯吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#0040260878V#032F啊，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040260879V唔……\n',
            '正想问你详情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00F7, 0x0017, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_332E',
    )

    ChrTalk(
        0x0106,
        (
            '#0050260880V#051F#6P好了，回到游击士协会之后\n',
            '我会给你们大致说明一下的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3379')

    def _loc_332E(): pass

    label('loc_332E')

    ChrTalk(
        0x0103,
        (
            '#0030260881V#020F#6P好了，等回到游击士协会之后\n',
            '我给你做详细的说明吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3379(): pass

    label('loc_3379')

    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(500)

    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    NewScene('ED6_DT21/T4100._SN', 103, 0, 0)
    IdleLoop()

    Return()

# id: 0x0017 offset: 0x3396
@scena.Code('func_17_3396')
def func_17_3396():
    PlaySE(120, 0x00, 0x64)
    OP_6F(0x0005, 0)
    OP_70(0x0005, 100)
    Sleep(1000)

    PlaySE(118, 0x00, 0x64)
    OP_6F(0x000A, 1)
    OP_70(0x000A, 60)
    OP_73(0x000A)
    Sleep(1000)

    OP_23(0x0075)
    PlaySE(119, 0x01, 0x64)
    OP_6F(0x000A, 61)
    OP_70(0x000A, 160)
    Fade(1000)
    ChrSetFlags(0x001B, 0x0080)
    OP_72(0x0009, 0x0004)
    MapClearFlags(0x00000010)
    CameraMove(63630, 30000, 116260, 0)
    OP_67(0, 45000, -50000, 0)
    CameraSetDistance(750, 0)
    OP_6C(60000, 0)
    OP_6E(262, 0)
    OP_73(0x0004)
    OP_71(0x000A, 0x0020)
    OP_6F(0x000A, 161)
    OP_70(0x000A, 260)
    ChrMoveToRelativeAsync(0x001F, 0, 300, 0, 300, 0x00)
    ChrMoveToRelativeAsync(0x001F, 0, 800, 0, 500, 0x00)
    Sleep(2000)

    @scena.Lambda('lambda_3479')
    def lambda_3479():
        CameraMove(75000, 30000, 116260, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3479)

    @scena.Lambda('lambda_3491')
    def lambda_3491():
        OP_94(0x01, 0x00FE, 0x0000, 0x000003E8, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_3491)

    OP_94(0x01, 0x001F, 0x0000, 0x000003E8, 0x000003E8, 0x00)

    @scena.Lambda('lambda_34B6')
    def lambda_34B6():
        OP_94(0x01, 0x00FE, 0x0000, 0x000004B0, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_34B6)

    OP_94(0x01, 0x001F, 0x0000, 0x000004B0, 0x000007D0, 0x00)

    @scena.Lambda('lambda_34DB')
    def lambda_34DB():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000578, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_34DB)

    OP_94(0x01, 0x001F, 0x0000, 0x00000578, 0x00000BB8, 0x00)

    @scena.Lambda('lambda_3500')
    def lambda_3500():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000640, 0x00000FA0, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_3500)

    OP_94(0x01, 0x001F, 0x0000, 0x00000640, 0x00000FA0, 0x00)

    @scena.Lambda('lambda_3525')
    def lambda_3525():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000708, 0x00001388, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_3525)

    OP_94(0x01, 0x001F, 0x0000, 0x00000708, 0x00001388, 0x00)

    @scena.Lambda('lambda_354A')
    def lambda_354A():
        OP_94(0x01, 0x00FE, 0x0000, 0x000007D0, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_354A)

    OP_94(0x01, 0x001F, 0x0000, 0x000007D0, 0x00001770, 0x00)

    @scena.Lambda('lambda_356F')
    def lambda_356F():
        OP_94(0x01, 0x00FE, 0x0000, 0x00000898, 0x00001B58, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_356F)

    OP_94(0x01, 0x001F, 0x0000, 0x00000898, 0x00001B58, 0x00)
    FadeOut(2000, 0, -1)

    @scena.Lambda('lambda_359E')
    def lambda_359E():
        OP_94(0x01, 0x00FE, 0x0000, 0x0000C350, 0x00001F40, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_359E)

    @scena.Lambda('lambda_35B4')
    def lambda_35B4():
        OP_94(0x01, 0x00FE, 0x0000, 0x0000C350, 0x00001F40, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_35B4)

    OP_24(0x0077, 0x5A)
    Sleep(100)

    OP_24(0x0077, 0x50)
    Sleep(100)

    OP_24(0x0077, 0x46)
    Sleep(100)

    OP_24(0x0077, 0x3C)
    Sleep(100)

    OP_24(0x0077, 0x32)
    Sleep(100)

    OP_24(0x0077, 0x28)
    Sleep(100)

    OP_24(0x0077, 0x1E)
    Sleep(100)

    OP_24(0x0077, 0x14)
    Sleep(100)

    OP_24(0x0077, 0x0A)
    Sleep(100)

    OP_23(0x0077)
    OP_0D()
    TerminateThread(0x0101, 0x00)

    Return()

# id: 0x0018 offset: 0x361E
@scena.Code('func_18_361E')
def func_18_361E():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_DB()
    CameraMove(84620, 1500, 135300, 0)
    OP_67(0, 4280, -10000, 0)
    CameraSetDistance(2920, 0)
    OP_6C(135000, 0)
    OP_6E(364, 0)
    CameraMove(118730, 1500, 138330, 0)
    OP_67(0, 4650, -10000, 0)
    CameraSetDistance(4810, 0)
    OP_6C(261000, 0)
    OP_6E(364, 0)
    OP_12(0x00009C40, 0x000493E0, 0x00000000)
    ChrSetPos(0x0101, 83430, 1700, 133650, 0)
    ChrSetPos(0x0102, 82500, 1700, 133620, 0)
    ChrSetPos(0x0021, 83700, 1700, 132200, 0)
    ChrSetPos(0x0018, 84600, 1700, 133240, 0)
    ChrSetPos(0x0019, 81670, 1700, 133310, 0)
    ChrSetPos(0x0022, 81540, 1700, 132400, 0)
    ChrSetPos(0x0023, 82880, 1700, 131700, 0)
    ChrSetPos(0x001A, 84900, 1700, 131800, 0)
    ChrSetPos(0x0017, 82910, 1700, 141060, 180)
    ChrClearFlags(0x0018, 0x0080)
    ChrClearFlags(0x0019, 0x0080)
    ChrClearFlags(0x0022, 0x0080)
    ChrClearFlags(0x0021, 0x0080)
    ChrClearFlags(0x0023, 0x0080)
    ChrClearFlags(0x001A, 0x0080)
    ChrClearFlags(0x0017, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x0010, 0x0080)
    OP_72(0x0005, 0x0004)
    OP_71(0x0009, 0x0004)
    OP_72(0x000A, 0x0004)
    OP_72(0x000B, 0x0004)
    OP_6F(0x0005, 200)
    OP_6F(0x000A, 0)
    OP_75(0x0B, 0x00000000, 0x00)
    OP_74(0x000B, 0x00000000, 0x0000)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_37D7')
    def lambda_37D7():
        CameraMove(81880, 1500, 137450, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_37D7)

    WaitForThreadExit(0x0101, 0x0001)
    Fade(1000)
    CameraMove(84620, 1500, 135300, 0)
    OP_67(0, 5710, -10000, 0)
    CameraSetDistance(2990, 0)
    OP_6C(135000, 0)
    OP_6E(364, 0)
    OP_12(0x00009C40, 0x0002BF20, 0x00000000)
    OP_0D()
    Sleep(500)

    OP_DC()

    ChrTalk(
        0x0101,
        (
            '#0010340227V#1007F#2P嗯，没想到奥利维尔\n',
            '竟然要返回帝国了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0021,
        (
            '#0030340228V#524F#2P是啊，真是突然啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#0040340229V#035F其实本来计划\n',
            '在早些时候就回国的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040340230V#030F由于艾丝蒂尔被抓走\n',
            '所以延期了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340231V#1025F#2P是这样啊……\n',
            '真对不起，因为我的缘故……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#0040340232V#031F不要放在心上。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040340233V多亏等你回来\n',
            '我才能再次\n',
            '与亲爱的约修亚相见啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340234V#1049F#2P哈哈，你真是一点儿没变啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020340235V#1043F……那个，奥利维尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#0040340236V#030F嗯？怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340237V#1042F#2P你……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020340238V#1035F……不，没什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020340239V#1040F感谢你在至今为止的旅途中\n',
            '对艾丝蒂尔的帮助。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#0040340240V#035F呵，是我自愿的啊\n',
            '不要说那么见外的话。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040340241V#037F不过，如果你一定要这么说\n',
            '那么来个拥抱以示感谢吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340242V#1019F#2P你给我适可而止。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010340243V#1025F真是的……至少最后该\n',
            '好好地告别一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#0040340244V#035F哈哈，我一直是\n',
            '很认真的啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040340245V#030F艾丝蒂尔、约修亚。\n',
            '雪拉，还有大家……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040340246V虽然会有各种各样的辛劳和危险\n',
            '大家当心就好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040340247V#031F奥利维尔会在帝国的天空中\n',
            '为你们的幸运而祈祷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340248V#1006F#2P嗯，谢谢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0021,
        (
            '#0030340249V#021F#2P呵呵……\n',
            '你也要当心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340250V#1054F#2P……保重了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '#0080340251V#071F有机会再一起喝酒吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0022,
        (
            '#0050340252V#051F下次改掉你那\n',
            '装怪的毛病啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '#0070340253V#067F#2P啊哈哈……\n',
            '那个那个……再见～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0023,
        (
            '#0180340254V#1061F啊，虽然只是短暂的交往\n',
            '可我非常开心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#0060340255V#048F多保重……\n',
            '承蒙关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1500, 0, -1)
    OP_0D()
    OP_B7(0x03)
    SetScenaFlags(ScenaFlag(0x021F, 0, 0x10F8))
    NewScene('ED6_DT21/E0310._SN', 106, 0, 0)
    IdleLoop()

    Return()

# id: 0x0019 offset: 0x3E28
@scena.Code('func_19_3E28')
def func_19_3E28():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_DB()
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x0010, 0x0080)
    CameraMove(73560, 250, 132340, 0)
    OP_67(0, 8020, -10000, 0)
    CameraSetDistance(5850, 0)
    OP_6C(285000, 0)
    OP_6E(404, 0)
    OP_12(0x00009C40, 0x000493E0, 0x00000000)
    ChrSetPos(0x0017, 82620, 1500, 143550, 135)
    ChrClearFlags(0x0017, 0x0080)
    OP_E5(0x17, 0x00, 0x00)
    OP_A1(0x001F, 0x000A)
    OP_72(0x000A, 0x0004)
    OP_72(0x000A, 0x0020)
    ChrSetPos(0x001F, 89000, 200, 130000, 90)
    ChrSetFlags(0x001F, 0x0004)
    OP_A1(0x0020, 0x000B)
    OP_72(0x000B, 0x0004)
    ChrSetFlags(0x0020, 0x0004)
    ChrSetPos(0x0020, 89000, -4800, 130000, 90)
    OP_75(0x0B, 0x00000000, 0x00)
    OP_74(0x000B, 0x00000000, 0x0000)
    OP_72(0x0005, 0x0004)
    OP_6F(0x0005, 200)
    OP_6F(0x000A, 1)
    PlaySE(117, 0x00, 0x64)

    @scena.Lambda('lambda_3F48')
    def lambda_3F48():
        CameraMove(93000, 1250, 131420, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3F48)

    @scena.Lambda('lambda_3F60')
    def lambda_3F60():
        OP_67(0, 4500, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3F60)

    @scena.Lambda('lambda_3F78')
    def lambda_3F78():
        CameraSetDistance(5850, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3F78)

    @scena.Lambda('lambda_3F88')
    def lambda_3F88():
        OP_6C(285000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3F88)

    @scena.Lambda('lambda_3F98')
    def lambda_3F98():
        OP_6E(471, 6000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3F98)

    FadeIn(2000, 0)
    Sleep(1000)

    PlaySE(120, 0x00, 0x64)
    OP_6F(0x0005, 200)
    OP_70(0x0005, 100)
    Sleep(1000)

    OP_23(0x0075)
    PlaySE(293, 0x00, 0x64)
    CreateThread(0x001F, 0x00, 0x00, func_1C_4C4C)
    Sleep(3000)

    ChrMoveToRelativeAsync(0x001F, 0, 500, 0, 400, 0x00)
    ChrMoveToRelativeAsync(0x001F, 0, 1000, 0, 800, 0x00)
    ChrMoveToRelativeAsync(0x001F, 0, 2000, 0, 1600, 0x00)
    ChrMoveToRelativeAsync(0x001F, 0, 500, 0, 800, 0x00)
    ChrMoveToRelativeAsync(0x001F, 0, 400, 0, 400, 0x00)

    @scena.Lambda('lambda_4046')
    def lambda_4046():
        CameraMove(105490, 1500, 130810, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4046)

    @scena.Lambda('lambda_405E')
    def lambda_405E():
        ChrMoveTo(0x00FE, 250000, 8200, 130000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_405E)

    @scena.Lambda('lambda_4079')
    def lambda_4079():
        ChrMoveTo(0x00FE, 250000, 8200, 130000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_4079)

    Sleep(200)

    @scena.Lambda('lambda_4099')
    def lambda_4099():
        ChrMoveTo(0x00FE, 250000, 8200, 130000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_4099)

    @scena.Lambda('lambda_40B4')
    def lambda_40B4():
        ChrMoveTo(0x00FE, 250000, 8200, 130000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_40B4)

    Sleep(200)

    @scena.Lambda('lambda_40D4')
    def lambda_40D4():
        ChrMoveTo(0x00FE, 250000, 8200, 130000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_40D4)

    @scena.Lambda('lambda_40EF')
    def lambda_40EF():
        ChrMoveTo(0x00FE, 250000, 8200, 130000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_40EF)

    Sleep(200)

    @scena.Lambda('lambda_410F')
    def lambda_410F():
        ChrMoveTo(0x00FE, 250000, 8200, 130000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_410F)

    @scena.Lambda('lambda_412A')
    def lambda_412A():
        ChrMoveTo(0x00FE, 250000, 8200, 130000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_412A)

    Sleep(200)

    @scena.Lambda('lambda_414A')
    def lambda_414A():
        ChrMoveTo(0x00FE, 250000, 8200, 130000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_414A)

    @scena.Lambda('lambda_4165')
    def lambda_4165():
        ChrMoveTo(0x00FE, 250000, 8200, 130000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_4165)

    Sleep(200)

    @scena.Lambda('lambda_4185')
    def lambda_4185():
        ChrMoveTo(0x00FE, 250000, 8200, 130000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_4185)

    @scena.Lambda('lambda_41A0')
    def lambda_41A0():
        ChrMoveTo(0x00FE, 250000, 8200, 130000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_41A0)

    Sleep(200)

    @scena.Lambda('lambda_41C0')
    def lambda_41C0():
        ChrMoveTo(0x00FE, 250000, 8200, 130000, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_41C0)

    @scena.Lambda('lambda_41DB')
    def lambda_41DB():
        ChrMoveTo(0x00FE, 250000, 8200, 130000, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_41DB)

    Sleep(200)

    @scena.Lambda('lambda_41FB')
    def lambda_41FB():
        ChrMoveTo(0x00FE, 250000, 8200, 130000, 13000, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_41FB)

    @scena.Lambda('lambda_4216')
    def lambda_4216():
        ChrMoveTo(0x00FE, 250000, 8200, 130000, 13000, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_4216)

    Sleep(200)

    @scena.Lambda('lambda_4236')
    def lambda_4236():
        ChrMoveTo(0x00FE, 250000, 8200, 130000, 16000, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_4236)

    @scena.Lambda('lambda_4251')
    def lambda_4251():
        ChrMoveTo(0x00FE, 250000, 8200, 130000, 16000, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_4251)

    Sleep(200)

    @scena.Lambda('lambda_4271')
    def lambda_4271():
        ChrMoveTo(0x00FE, 250000, 8200, 130000, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_4271)

    @scena.Lambda('lambda_428C')
    def lambda_428C():
        ChrMoveTo(0x00FE, 250000, 8200, 130000, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_428C)

    Sleep(200)

    @scena.Lambda('lambda_42AC')
    def lambda_42AC():
        ChrMoveTo(0x00FE, 250000, 8200, 130000, 25000, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_42AC)

    @scena.Lambda('lambda_42C7')
    def lambda_42C7():
        ChrMoveTo(0x00FE, 250000, 8200, 130000, 25000, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_42C7)

    Sleep(200)

    @scena.Lambda('lambda_42E7')
    def lambda_42E7():
        ChrMoveTo(0x00FE, 250000, 8200, 130000, 30000, 0x00)

        ExitThread()

    DispatchAsync(0x001F, 0x0001, lambda_42E7)

    @scena.Lambda('lambda_4302')
    def lambda_4302():
        ChrMoveTo(0x00FE, 250000, 8200, 130000, 30000, 0x00)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_4302)

    Sleep(2800)

    OP_24(0x0077, 0x5A)
    OP_24(0x0125, 0x5A)
    Sleep(100)

    OP_24(0x0077, 0x50)
    OP_24(0x0125, 0x50)
    Sleep(100)

    OP_24(0x0077, 0x46)
    OP_24(0x0125, 0x46)
    Sleep(100)

    OP_24(0x0077, 0x3C)
    OP_24(0x0125, 0x3C)
    Sleep(100)

    OP_24(0x0077, 0x32)
    OP_24(0x0125, 0x32)
    Sleep(100)

    OP_24(0x0077, 0x28)
    OP_24(0x0125, 0x28)
    Sleep(100)

    OP_24(0x0077, 0x1E)
    OP_24(0x0125, 0x1E)
    Sleep(100)

    OP_23(0x0077)
    OP_23(0x0125)
    Fade(1000)
    TerminateThread(0x0101, 0x03)
    OP_12(0x00009C40, 0x0002BF20, 0x00000000)
    CameraMove(83010, 1500, 142960, 0)
    OP_67(0, 6680, -10000, 0)
    CameraSetDistance(2700, 0)
    OP_6C(134000, 0)
    OP_6E(302, 0)
    ChrSetDirection(0x0017, 90, 0)
    OP_0D()
    Sleep(1000)

    OP_DC()

    ChrTalk(
        0x0017,
        (
            '#0040340291V#035F呼……\n',
            '悠闲的时光看来要结束了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040340292V#030F不，也许还有\n',
            '最后的机会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x001E, 71940, 750, 143010, 90)
    ChrSetChipByIndex(0x001E, 18)
    ChrSetPos(0x001D, 71700, 750, 144070, 90)
    ChrClearFlags(0x001D, 0x0080)

    @scena.Lambda('lambda_4474')
    def lambda_4474():
        OP_9E(0x00FE, 50, 0, 500, 1000)
        Yield()

        Jump('lambda_4474')

    DispatchAsync2(0x001D, 0x0001, lambda_4474)

    NpcTalk(
        0x001E,
        '女孩的声音',
        (
            '#0280340293V#1P等、等一下～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0017, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    @scena.Lambda('lambda_44D6')
    def lambda_44D6():
        ChrTurnDirection(0x00FE, 0x001E, 400)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_44D6)

    ChrClearFlags(0x001E, 0x0080)

    @scena.Lambda('lambda_44E9')
    def lambda_44E9():
        CameraMove(81940, 1500, 142800, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_44E9)

    @scena.Lambda('lambda_4501')
    def lambda_4501():
        ChrWalkTo(0x001E, 80360, 1500, 143310, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_4501)

    Sleep(500)

    @scena.Lambda('lambda_4521')
    def lambda_4521():
        ChrWalkTo(0x00FE, 78860, 1500, 143870, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x001D, 0x0002, lambda_4521)

    WaitForThreadExit(0x001E, 0x0001)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0017,
        (
            '#0040340294V#033F#5P咦，你们……',
            TxtCtl.Enter,
        ),
    )

    WaitForThreadExit(0x001D, 0x0002)
    TerminateThread(0x001D, 0x01)
    CloseMessageWindow()

    ChrTalk(
        0x001E,
        (
            '#0280340295V#152F#6P啊，走了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    LoadEffect(0x00, 'map\\\\mp032_00.eff')

    ChrTalk(
        0x001D,
        (
            '#0270340296V#145F呼哧呼哧……\n',
            '没、没赶得上吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#0040340297V#030F#5P怎么了，各位记者？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040340298V又打算像龙事件那时一样\n',
            '偷偷潜入吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001D,
        (
            '#0270340299V#141F啊，而且还听说\n',
            '约修亚回来了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270340300V#144F好了，朵洛希。\n',
            '赶紧拍摄『埃尔赛尤』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270340301V如果使用长焦镜头\n',
            '应该能拍到很不错的画面呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001E,
        (
            '#0280340302V#151F#6P了解！前辈！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0017, 180, 400)
    CreateThread(0x0017, 0x00, 0x00, func_1B_4C30)
    Sleep(300)

    @scena.Lambda('lambda_4720')
    def lambda_4720():
        CameraMove(88040, 1500, 142240, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_4720)

    @scena.Lambda('lambda_4738')
    def lambda_4738():
        OP_67(0, 5680, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4738)

    @scena.Lambda('lambda_4750')
    def lambda_4750():
        CameraSetDistance(2700, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4750)

    @scena.Lambda('lambda_4760')
    def lambda_4760():
        ChrWalkTo(0x001E, 87540, 1500, 143090, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x001E, 0x0000, lambda_4760)

    Sleep(300)

    @scena.Lambda('lambda_4780')
    def lambda_4780():
        ChrWalkTo(0x001D, 85260, 1500, 143520, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x001D, 0x0000, lambda_4780)

    WaitForThreadExit(0x001E, 0x0000)
    ChrSetSubChip(0x001E, 0)
    ChrSetChipByIndex(0x001E, 19)
    Sleep(500)

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    CreateThread(0x001E, 0x01, 0x00, func_1A_4BA7)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x001D, 0x0000)
    WaitForThreadExit(0x0017, 0x0000)
    Sleep(1000)

    ChrTalk(
        0x0017,
        (
            '#0040340303V#031F#2P呵呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrSetPos(0x001B, 67260, 0, 143120, 90)
    ChrClearFlags(0x001B, 0x0080)
    ChrSetDirection(0x0017, 0, 400)
    ChrWalkTo(0x0017, 82570, 1500, 143440, 2000, 0x00)

    @scena.Lambda('lambda_4825')
    def lambda_4825():
        ChrWalkTo(0x0017, 69950, 0, 143120, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0000, lambda_4825)

    Sleep(2500)

    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    Fade(1000)
    CameraMove(73250, 0, 141910, 0)
    OP_67(0, 5560, -10000, 0)
    CameraSetDistance(2570, 0)
    OP_6C(134000, 0)
    OP_6E(325, 0)
    OP_20(0x00000BB8)

    @scena.Lambda('lambda_488F')
    def lambda_488F():
        CameraMove(70250, 0, 141910, 3000)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_488F)

    WaitForThreadExit(0x0017, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0017, 0x0001)
    Sleep(500)

    ChrTalk(
        0x001B,
        (
            '#0110340304V#270F……打过招呼了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#0040340305V#035F#5P嗯，打过了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040340306V#030F那边的准备如何了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#0110340307V#277F叔父想了些办法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110340308V宰相阁下\n',
            '似乎也认为正是好时机。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#0040340309V#030F#5P的确，如果是他的话\n',
            '应该能接受王国的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040340310V#035F呵呵……事情要变得有趣起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#0110340311V#272F真是的……\n',
            '这是什么无聊的爱好啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110340312V#276F他们惊愕的表情\n',
            '好像马上就要浮现在眼前了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#0040340313V#031F#5P哈哈哈。\n',
            '那正是我的目标啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4A9E')
    def lambda_4A9E():
        CameraMove(71920, 750, 143050, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4A9E)

    @scena.Lambda('lambda_4AB6')
    def lambda_4AB6():
        OP_67(0, 4720, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4AB6)

    @scena.Lambda('lambda_4ACE')
    def lambda_4ACE():
        CameraSetDistance(2570, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_4ACE)

    @scena.Lambda('lambda_4ADE')
    def lambda_4ADE():
        OP_6C(122000, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_4ADE)

    @scena.Lambda('lambda_4AEE')
    def lambda_4AEE():
        OP_6E(325, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_4AEE)

    ChrSetDirection(0x0017, 90, 400)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(300)

    ChrTalk(
        0x0017,
        (
            '#0040340314V#030F#2P（下次再相见时\n',
            '彼此就是冤家对头了。)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040340315V#035F（请大家千万不要\n',
            '被『结社』之类的抢了先啊。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    OP_20(0x000007D0)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021F, 7, 0x10FF))
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/E0810._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x001A offset: 0x4BA7
@scena.Code('func_1A_4BA7')
def func_1A_4BA7():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_4C2F',
    )

    PlaySE(124, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x001E, 0, 1400, 500, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    PlaySE(124, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x001E, 0, 1400, 500, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    Jump('func_1A_4BA7')

    def _loc_4C2F(): pass

    label('loc_4C2F')

    Return()

# id: 0x001B offset: 0x4C30
@scena.Code('func_1B_4C30')
def func_1B_4C30():
    ChrWalkTo(0x00FE, 82870, 1700, 141600, 2000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x001C offset: 0x4C4C
@scena.Code('func_1C_4C4C')
def func_1C_4C4C():
    PlaySE(119, 0x00, 0x64)
    OP_6F(0x000A, 1)
    OP_70(0x000A, 150)
    OP_73(0x000A)
    OP_6F(0x000A, 151)
    OP_70(0x000A, 330)
    Sleep(3200)

    OP_75(0x0B, 0x00000000, 0x02)
    PlaySE(221, 0x00, 0x64)
    OP_74(0x000B, 0x00000000, 0x0001)
    Sleep(250)

    OP_74(0x000B, 0x00000000, 0x0002)
    Sleep(250)

    PlaySE(221, 0x00, 0x64)
    OP_74(0x000B, 0x00000000, 0x0003)
    Sleep(250)

    OP_74(0x000B, 0x00000000, 0x0004)
    Sleep(250)

    PlaySE(221, 0x00, 0x64)
    OP_74(0x000B, 0x00000000, 0x0005)
    Sleep(250)

    OP_74(0x000B, 0x00000000, 0x0006)
    Sleep(250)

    OP_74(0x000B, 0x00000000, 0x0007)
    OP_73(0x000A)
    OP_71(0x000A, 0x0020)
    OP_6F(0x000A, 330)
    OP_70(0x000A, 430)

    Return()

# id: 0x001D offset: 0x4CFF
@scena.Code('func_1D_4CFF')
def func_1D_4CFF():
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
        (0x00000000, 'loc_4D79'),
        (0x00000001, 'loc_4D7F'),
        (-1, 'loc_4D85'),
    )

    def _loc_4D79(): pass

    label('loc_4D79')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_4D85')

    def _loc_4D7F(): pass

    label('loc_4D7F')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_4D85')

    def _loc_4D85(): pass

    label('loc_4D85')

    Return()

# id: 0x001E offset: 0x4D86
@scena.Code('func_1E_4D86')
def func_1E_4D86():
    MapClearFlags(0x00000001)
    CameraMove(12790, 0, 144090, 0)
    Sleep(100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_4DC5',
    )

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['雪拉扎德'],
            ChrTable['提妲'],
            0x00FF,
        ),
        (
            ChrTable['科洛丝'],
            ChrTable['金'],
            0xFFFF,
        ),
    )

    Jump('loc_4DDF')

    def _loc_4DC5(): pass

    label('loc_4DC5')

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['阿加特'],
            ChrTable['提妲'],
            0x00FF,
        ),
        (
            ChrTable['科洛丝'],
            ChrTable['金'],
            0xFFFF,
        ),
    )

    def _loc_4DDF(): pass

    label('loc_4DDF')

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

# id: 0x001F offset: 0x4DFF
@scena.Code('func_1F_4DFF')
def func_1F_4DFF():
    MapClearFlags(0x00000001)
    CameraMove(12790, 0, 144090, 0)
    Sleep(100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_4E44',
    )

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['雪拉扎德'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['提妲'],
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            ChrTable['金'],
            0xFFFF,
        ),
    )

    Jump('loc_4E64')

    def _loc_4E44(): pass

    label('loc_4E44')

    FadeIn(0, 0)

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

    def _loc_4E64(): pass

    label('loc_4E64')

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

# id: 0x0020 offset: 0x4E84
@scena.Code('func_20_4E84')
def func_20_4E84():
    Sleep(2000)

    OP_C8(0x0200, 0x0046, 'C_PLAC04._CH', 0x00, 0x03E8)
    ShowPlaceName('王都格兰赛尔')

    Return()

# id: 0x0021 offset: 0x4EAD
@scena.Code('func_21_4EAD')
def func_21_4EAD():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '定期船起降坪\n',
            '≡　前往洛连特市\n',
            '≡　前往蔡斯市\n',
            '≡　去卡尔瓦德共和国',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※请勿携带易燃物和危险品\n',
            '　　　　『利贝尔飞船公社』',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0022 offset: 0x4F5A
@scena.Code('func_22_4F5A')
def func_22_4F5A():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　　　飞船坪塔台　　　　\n',
            '　※无关人员禁止入内　　\n',
            ' 『利贝尔飞船公社』　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

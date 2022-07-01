import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T3200_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3200   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '麻绪婆婆'),
    TXT(0x02, '艾德'),
    TXT(0x03, '艾缇'),
    TXT(0x04, '孩子'),
    TXT(0x05, '孩子'),
    TXT(0x06, '游客'),
    TXT(0x07, '游客'),
    TXT(0x08, '游客'),
    TXT(0x09, '拉克'),
    TXT(0x0A, '库安'),
    TXT(0x0B, '法尔茨'),
    TXT(0x0C, '格温副队长'),
    TXT(0x0D, '士兵科尔比'),
    TXT(0x0E, '士兵阿曼德'),
    TXT(0x0F, '莉西亚'),
    TXT(0x10, '猿羊'),
    TXT(0x11, '猿羊'),
    TXT(0x12, '猿羊'),
    TXT(0x13, '猿羊'),
    TXT(0x14, '猿羊'),
    TXT(0x15, '猿羊'),
    TXT(0x16, '村民'),
    TXT(0x17, '村民'),
    TXT(0x18, '村民'),
    TXT(0x19, '村民'),
    TXT(0x1A, '村民'),
    TXT(0x1B, '村民'),
    TXT(0x1C, '赫雷思老人'),
    TXT(0x1D, '托兰特平原道方向'),
    TXT(0x1E, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3200.x'
    header.mapIndex       = 1
    header.bgm            = 15
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT21/T3200._SN', 'ED6_DT21/T3200_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x40ED
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
        ('ED6_DT07/CH02430._CH', 'ED6_DT07/CH02430P._CP'),
        ('ED6_DT07/CH01270._CH', 'ED6_DT07/CH01270P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH01270._CH', 'ED6_DT07/CH01270P._CP'),
        ('ED6_DT07/CH01070._CH', 'ED6_DT07/CH01070P._CP'),
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH01220._CH', 'ED6_DT07/CH01220P._CP'),
        ('ED6_DT07/CH01160._CH', 'ED6_DT07/CH01160P._CP'),
        ('ED6_DT07/CH01060._CH', 'ED6_DT07/CH01060P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT09/CH10140._CH', 'ED6_DT09/CH10140P._CP'),
        ('ED6_DT09/CH10141._CH', 'ED6_DT09/CH10141P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT07/CH01010._CH', 'ED6_DT07/CH01010P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT26/CH20253._CH', 'ED6_DT26/CH20253P._CP'),
        ('ED6_DT26/CH20248._CH', 'ED6_DT26/CH20248P._CP'),
        ('ED6_DT26/CH20251._CH', 'ED6_DT26/CH20251P._CP'),
        ('ED6_DT26/CH20249._CH', 'ED6_DT26/CH20249P._CP'),
        ('ED6_DT26/CH20250._CH', 'ED6_DT26/CH20250P._CP'),
        ('ED6_DT26/CH20257._CH', 'ED6_DT26/CH20257P._CP'),
        ('ED6_DT09/CH11150._CH', 'ED6_DT09/CH11150P._CP'),
        ('ED6_DT09/CH11151._CH', 'ED6_DT09/CH11151P._CP'),
        ('ED6_DT29/CH12070._CH', 'ED6_DT29/CH12070P._CP'),
        ('ED6_DT29/CH12071._CH', 'ED6_DT29/CH12071P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
    ]

# id: 0x10002 offset: 0x1A2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 2590,
            z                   = 250,
            y                   = 5360,
            direction           = 180,
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
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 12020,
            z                   = 2000,
            y                   = 16870,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = 12020,
            z                   = 2000,
            y                   = 14160,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            x                   = 21790,
            z                   = 2000,
            y                   = 5570,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            x                   = 22880,
            z                   = 2000,
            y                   = 9470,
            direction           = 303,
            word_0E             = 0,
            dword_10            = 29,
            chipIndex           = 29,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            x                   = 8760,
            z                   = 2000,
            y                   = 13310,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 29,
            chipIndex           = 29,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0007,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 38180,
            z                   = 6000,
            y                   = 49000,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 29,
            chipIndex           = 29,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            x                   = 49580,
            z                   = 2500,
            y                   = -2390,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 30,
            chipIndex           = 30,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            x                   = 67620,
            z                   = 3420,
            y                   = 25770,
            direction           = 195,
            word_0E             = 0,
            dword_10            = 27,
            chipIndex           = 27,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 66090,
            z                   = 3020,
            y                   = 25680,
            direction           = 162,
            word_0E             = 0,
            dword_10            = 25,
            chipIndex           = 25,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 62800,
            z                   = 3020,
            y                   = 25140,
            direction           = 156,
            word_0E             = 0,
            dword_10            = 25,
            chipIndex           = 25,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 61950,
            z                   = 3020,
            y                   = 23550,
            direction           = 98,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 73010,
            z                   = 3020,
            y                   = 25590,
            direction           = 215,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 67620,
            z                   = 3420,
            y                   = 25770,
            direction           = 195,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
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
            dword_10            = 13,
            chipIndex           = 13,
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
            dword_10            = 14,
            chipIndex           = 14,
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
            dword_10            = 15,
            chipIndex           = 15,
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
            dword_10            = 16,
            chipIndex           = 16,
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
            dword_10            = 17,
            chipIndex           = 17,
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
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 13520,
            z                   = 2500,
            y                   = 13590,
            direction           = 312,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = -30790,
            z                   = -2000,
            y                   = 15330,
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

# id: 0x10003 offset: 0x542
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x542
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 28950,
            y           = 1000,
            z           = 4030,
            range       = 2500,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000027,
        ),
        ScenaEventData(
            x           = 980,
            y           = -250,
            z           = 18420,
            range       = 1250,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000028,
        ),
        ScenaEventData(
            x           = 42330,
            y           = 5750,
            z           = 36020,
            range       = 1250,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000029,
        ),
    )

# id: 0x10005 offset: 0x5A2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 40000,
            triggerZ            = 6000,
            triggerY            = 49730,
            triggerRange        = 800,
            actorX              = 40000,
            actorZ              = 7000,
            actorY              = 49730,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0017,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 43290,
            triggerZ            = 6250,
            triggerY            = 35890,
            triggerRange        = 800,
            actorX              = 43290,
            actorZ              = 6500,
            actorY              = 35890,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0018,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 53100,
            triggerZ            = 0,
            triggerY            = 3880,
            triggerRange        = 1000,
            actorX              = 48680,
            actorZ              = 0,
            actorY              = 2470,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0026,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x60E
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_65E',
    )

    SetChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x0015, 0x0080)
    SetChrPos(0x0010, 14240, 2500, 16350, 90)
    SetChrPos(0x0011, 14240, 2500, 17460, 90)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_656',
    )

    Jump('loc_65B')

    def _loc_656(): pass

    label('loc_656')

    ClearChrFlags(0x0016, 0x0080)

    def _loc_65B(): pass

    label('loc_65B')

    Jump('loc_766')

    def _loc_65E(): pass

    label('loc_65E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_68F',
    )

    SetChrFlags(0x0012, 0x0080)
    SetChrPos(0x0010, 12150, 2000, 16180, 90)
    SetChrPos(0x0011, 12150, 2000, 15380, 90)

    Jump('loc_766')

    def _loc_68F(): pass

    label('loc_68F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_6E7',
    )

    SetChrPos(0x0012, 15380, 2000, 12210, 0)
    SetChrFlags(0x0012, 0x0010)
    SetChrPos(0x0010, 12150, 2000, 20300, 90)
    SetChrPos(0x0011, 12150, 2000, 19500, 90)
    SetChrPos(0x0009, 21950, 2000, 14600, 270)
    ClearChrFlags(0x0009, 0x0080)

    Jump('loc_766')

    def _loc_6E7(): pass

    label('loc_6E7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_735',
    )

    SetChrFlags(0x0012, 0x0080)
    SetChrPos(0x0010, 12150, 2000, 15860, 180)
    SetChrPos(0x0011, 12150, 2000, 15150, 0)
    SetChrFlags(0x0010, 0x0010)
    SetChrFlags(0x0011, 0x0010)
    CreateThread(0x0010, 0x00, 0x00, 0x0004)
    CreateThread(0x0011, 0x00, 0x00, 0x0005)
    ClearChrFlags(0x0023, 0x0080)

    Jump('loc_766')

    def _loc_735(): pass

    label('loc_735')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_766',
    )

    CreateThread(0x0010, 0x00, 0x00, 0x0003)
    CreateThread(0x0011, 0x00, 0x00, 0x0003)
    CreateThread(0x0010, 0x01, 0x00, 0x0002)
    CreateThread(0x0011, 0x01, 0x00, 0x0002)
    CreateThread(0x0010, 0x02, 0x00, 0x0008)
    CreateThread(0x0011, 0x02, 0x00, 0x0009)

    def _loc_766(): pass

    label('loc_766')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_777',
    )

    OP_A3(0x10F0)
    Event(1, 0x0000)

    Jump('loc_7A2')

    def _loc_777(): pass

    label('loc_777')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_78D',
    )

    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(0, 0x0019)

    Jump('loc_7A2')

    def _loc_78D(): pass

    label('loc_78D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 1, 0x1421)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7A2',
    )

    SetMapFlags(0x10000000)
    Event(0, 0x0013)

    def _loc_7A2(): pass

    label('loc_7A2')

    Return()

# id: 0x0001 offset: 0x7A3
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFE8130, 0xFFFE5E08, 0x00230054)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7F0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7F0',
    )

    OP_82(0x83, 0x00)
    OP_82(0x84, 0x00)
    OP_82(0x85, 0x00)
    OP_82(0x86, 0x00)
    OP_82(0x87, 0x00)
    OP_82(0x88, 0x00)
    OP_82(0x89, 0x00)
    OP_82(0x8A, 0x00)
    OP_82(0x8B, 0x00)
    OP_82(0x8C, 0x00)
    OP_82(0x8D, 0x00)
    OP_82(0x8E, 0x00)
    OP_82(0x8F, 0x00)

    def _loc_7F0(): pass

    label('loc_7F0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0401, 0, 0x2008)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_804',
    )

    OP_72(0x0003, 0x0010)
    OP_65(0x01, 0x0001)

    Jump('loc_808')

    def _loc_804(): pass

    label('loc_804')

    OP_64(0x01, 0x0001)

    def _loc_808(): pass

    label('loc_808')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_812',
    )

    Jump('loc_A5B')

    def _loc_812(): pass

    label('loc_812')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_A4A',
    )

    PlayEffect(0x91, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x92, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x93, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x94, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x95, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x96, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x97, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x98, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x99, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x9A, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_25(0x010B, 0x000041E6, 0x000009C4, 0x000042EA, 0x000007D0, 0x000061A8, 0x64, 0x00000000)

    Jump('loc_A5B')

    def _loc_A4A(): pass

    label('loc_A4A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_A54',
    )

    Jump('loc_A5B')

    def _loc_A54(): pass

    label('loc_A54')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_A5B',
    )

    def _loc_A5B(): pass

    label('loc_A5B')

    OP_72(0x000B, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 2, 0x1422)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A6F',
    )

    OP_65(0x00, 0x0001)

    Jump('loc_A7D')

    def _loc_A6F(): pass

    label('loc_A6F')

    OP_64(0x00, 0x0001)
    OP_6F(0x000B, 120)
    OP_82(0x90, 0x00)

    def _loc_A7D(): pass

    label('loc_A7D')

    Return()

# id: 0x0002 offset: 0xA7E
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
        'loc_AA3',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_BE5')

    def _loc_AA3(): pass

    label('loc_AA3')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_ABC',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000640)

    Jump('loc_BE5')

    def _loc_ABC(): pass

    label('loc_ABC')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AD5',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x0000060E)

    Jump('loc_BE5')

    def _loc_AD5(): pass

    label('loc_AD5')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AEE',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005DC)

    Jump('loc_BE5')

    def _loc_AEE(): pass

    label('loc_AEE')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B07',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AA)

    Jump('loc_BE5')

    def _loc_B07(): pass

    label('loc_B07')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B20',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x00000578)

    Jump('loc_BE5')

    def _loc_B20(): pass

    label('loc_B20')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B39',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x00000546)

    Jump('loc_BE5')

    def _loc_B39(): pass

    label('loc_B39')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B52',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000677)

    Jump('loc_BE5')

    def _loc_B52(): pass

    label('loc_B52')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B6B',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000645)

    Jump('loc_BE5')

    def _loc_B6B(): pass

    label('loc_B6B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B84',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x00000613)

    Jump('loc_BE5')

    def _loc_B84(): pass

    label('loc_B84')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B9D',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005E1)

    Jump('loc_BE5')

    def _loc_B9D(): pass

    label('loc_B9D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BB6',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AF)

    Jump('loc_BE5')

    def _loc_BB6(): pass

    label('loc_BB6')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BCF',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x0000057D)

    Jump('loc_BE5')

    def _loc_BCF(): pass

    label('loc_BCF')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BE5',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x0000054B)

    def _loc_BE5(): pass

    label('loc_BE5')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_BFA',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_BE5')

    def _loc_BFA(): pass

    label('loc_BFA')

    Return()

# id: 0x0003 offset: 0xBFB
@scena.Code('func_03_BFB')
def func_03_BFB():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_C57',
    )

    OP_8E(0x00FE, 12020, 2000, 22330, 5000, 0x00)
    OP_8E(0x00FE, 22520, 2000, 22330, 5000, 0x00)
    OP_8E(0x00FE, 22520, 2000, 11860, 5000, 0x00)
    OP_8E(0x00FE, 12020, 2000, 11860, 5000, 0x00)

    Jump('func_03_BFB')

    def _loc_C57(): pass

    label('loc_C57')

    Return()

# id: 0x0004 offset: 0xC58
@scena.Code('func_04_C58')
def func_04_C58():
    CreateThread(0x00FE, 0x01, 0x00, 0x0002)
    def _loc_C5F(): pass

    label('loc_C5F')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_CC6',
    )

    Sleep(400)

    OP_8F(0x00FE, 12150, 2000, 17860, 6000, 0x00)
    OP_8F(0x00FE, 12150, 2000, 15860, 6000, 0x00)
    OP_62(0x00FE, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    OP_9E(0x00FE, 0x00000000, 0x0000001E, 0x000003E8, 0x000007D0)
    OP_A2(0x0008)
    OP_A6(0x0009)
    OP_A3(0x0009)

    Jump('loc_C5F')

    def _loc_CC6(): pass

    label('loc_CC6')

    Return()

# id: 0x0005 offset: 0xCC7
@scena.Code('func_05_CC7')
def func_05_CC7():
    CreateThread(0x00FE, 0x01, 0x00, 0x0002)
    def _loc_CCE(): pass

    label('loc_CCE')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_D35',
    )

    Sleep(400)

    OP_8F(0x00FE, 12150, 2000, 13150, 6000, 0x00)
    OP_8F(0x00FE, 12150, 2000, 15150, 6000, 0x00)
    OP_62(0x00FE, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    OP_9E(0x00FE, 0x0000001E, 0x0000000A, 0x000003E8, 0x000007D0)
    OP_A2(0x0009)
    OP_A6(0x0008)
    OP_A3(0x0008)

    Jump('loc_CCE')

    def _loc_D35(): pass

    label('loc_D35')

    Return()

# id: 0x0006 offset: 0xD36
@scena.Code('func_06_D36')
def func_06_D36():
    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_D40(): pass

    label('loc_D40')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xA),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_DDA',
    )

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            (Expr.PushLong, 0x2D),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Sleep(10)

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            (Expr.PushLong, 0x2D),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Sleep(10)

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            (Expr.PushLong, 0x2D),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Sleep(10)

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            (Expr.PushLong, 0x2D),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Sleep(10)

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            (Expr.PushLong, 0x2D),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Sleep(10)

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            (Expr.PushLong, 0x2D),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Sleep(10)

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            (Expr.PushLong, 0x2D),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Sleep(10)

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            (Expr.PushLong, 0x2D),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Sleep(10)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Jump('loc_D40')

    def _loc_DDA(): pass

    label('loc_DDA')

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            (Expr.PushLong, 0xB4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0007 offset: 0xDE6
@scena.Code('func_07_DE6')
def func_07_DE6():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_E5A',
    )

    OP_8E(0x00FE, -9500, -2000, 13030, 2000, 0x00)
    Sleep(2600)

    OP_8C(0x00FE, 0, 400)
    OP_8E(0x00FE, -9500, -2000, 16940, 2000, 0x00)
    OP_8E(0x00FE, 8760, 2000, 16700, 2000, 0x00)
    Sleep(2600)

    OP_8C(0x00FE, 180, 400)
    OP_8E(0x00FE, 8760, 2000, 13310, 2000, 0x00)

    Jump('func_07_DE6')

    def _loc_E5A(): pass

    label('loc_E5A')

    Return()

# id: 0x0008 offset: 0xE5B
@scena.Code('func_08_E5B')
def func_08_E5B():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_EC6',
    )

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0xD48),
            Expr.Add,
            (Expr.GetChrWork, 0x11, 0x1),
            Expr.Gtr,
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0xD48),
            Expr.Sub,
            (Expr.GetChrWork, 0x11, 0x1),
            Expr.Lss,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0xD48),
            Expr.Add,
            (Expr.GetChrWork, 0x11, 0x3),
            Expr.Gtr,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0xD48),
            Expr.Sub,
            (Expr.GetChrWork, 0x11, 0x3),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_EB3',
    )

    Sleep(100)

    OP_4B(0x00FE, 0)

    Jump('loc_EBE')

    def _loc_EB3(): pass

    label('loc_EB3')

    OP_4A(0x00FE, 0)
    ChrTurnDirection(0x00FE, 0x0011, 400)

    def _loc_EBE(): pass

    label('loc_EBE')

    Sleep(100)

    Jump('func_08_E5B')

    def _loc_EC6(): pass

    label('loc_EC6')

    Return()

# id: 0x0009 offset: 0xEC7
@scena.Code('func_09_EC7')
def func_09_EC7():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_F27',
    )

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0x44C),
            Expr.Add,
            (Expr.GetChrWork, 0x10, 0x1),
            Expr.Gtr,
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0x44C),
            Expr.Sub,
            (Expr.GetChrWork, 0x10, 0x1),
            Expr.Lss,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0x44C),
            Expr.Add,
            (Expr.GetChrWork, 0x10, 0x3),
            Expr.Gtr,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0x44C),
            Expr.Sub,
            (Expr.GetChrWork, 0x10, 0x3),
            Expr.Lss,
            Expr.Nez64,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F1B',
    )

    OP_4B(0x00FE, 0)

    Jump('loc_F1F')

    def _loc_F1B(): pass

    label('loc_F1B')

    OP_4A(0x00FE, 0)

    def _loc_F1F(): pass

    label('loc_F1F')

    Sleep(100)

    Jump('func_09_EC7')

    def _loc_F27(): pass

    label('loc_F27')

    Return()

# id: 0x000A offset: 0xF28
@scena.Code('func_0A_F28')
def func_0A_F28():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_F8D',
    )

    ChrTalk(
        0x0009,
        (
            '不过还真没想到温泉\n',
            '会被煮得沸沸腾腾的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '呼，还真不知道\n',
            '接下来会发生什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FD3')

    def _loc_F8D(): pass

    label('loc_F8D')

    ChrTalk(
        0x0009,
        (
            '源泉的调查就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '这样下去的话，\n',
            '我们没法营业了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000A)

    def _loc_FD3(): pass

    label('loc_FD3')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0xFD7
@scena.Code('func_0B_FD7')
def func_0B_FD7():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1016',
    )

    ChrTalk(
        0x00FE,
        (
            '哟！\n',
            '使出必杀技了吗？！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈。\n',
            '真过瘾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_106C')

    def _loc_1016(): pass

    label('loc_1016')

    ChrTalk(
        0x00FE,
        (
            '哈哈。\n',
            '好像在玩武术大会的游戏。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个村的孩子们\n',
            '是在悠闲的环境中成长起来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_106C(): pass

    label('loc_106C')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x1070
@scena.Code('func_0C_1070')
def func_0C_1070():
    TalkBegin(0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_114C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_10F5',
    )

    ChrTalk(
        0x00FE,
        (
            '太好了……\n',
            '泵好象修好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，其他的导力器\n',
            '看来还不能动弹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '中央工房的人现在\n',
            '也一定很忙吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    Jump('loc_1149')

    def _loc_10F5(): pass

    label('loc_10F5')

    ChrTalk(
        0x00FE,
        (
            '泵虽然修好了，不过\n',
            '其他的导力器还是不动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '中央工房的人现在\n',
            '也一定很忙吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1149(): pass

    label('loc_1149')

    Jump('loc_13D4')

    def _loc_114C(): pass

    label('loc_114C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_11A5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1190',
    )

    ChrTalk(
        0x00FE,
        (
            '水变冷了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '泵的导力器也\n',
            '停住了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    Jump('loc_11A2')

    def _loc_1190(): pass

    label('loc_1190')

    ChrTalk(
        0x00FE,
        (
            '水变冷了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11A2(): pass

    label('loc_11A2')

    Jump('loc_13D4')

    def _loc_11A5(): pass

    label('loc_11A5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_1237',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_11E8',
    )

    ChrTalk(
        0x00FE,
        (
            '呼～太好了～\n',
            '我还在想要是一直\n',
            '那样该怎么办。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1234')

    def _loc_11E8(): pass

    label('loc_11E8')

    ChrTalk(
        0x00FE,
        (
            '温泉能恢复真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果只有热水澡的话\n',
            '客人也一定不会来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_1234(): pass

    label('loc_1234')

    Jump('loc_13D4')

    def _loc_1237(): pass

    label('loc_1237')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_1271',
    )

    ChrTalk(
        0x00FE,
        (
            '开水咕噜咕噜地响着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还、还有这种事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13D4')

    def _loc_1271(): pass

    label('loc_1271')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_130A',
    )

    OP_4A(0x0010, 255)
    OP_4A(0x0011, 255)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_12B8',
    )

    ChrTalk(
        0x00FE,
        (
            '还没完呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x00FE, 0x02, 0x00, 0x0006)
    OP_95(0x00FE, 0x00000000, 0x000003E8, 0x00000000, 0x000007D0, 0x000007D0)

    Jump('loc_12FF')

    def _loc_12B8(): pass

    label('loc_12B8')

    ChrTalk(
        0x00FE,
        (
            '接招吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '剑技·八叶灭杀！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)
    CreateThread(0x00FE, 0x02, 0x00, 0x0006)
    OP_95(0x00FE, 0x00000000, 0x000003E8, 0x00000000, 0x000007D0, 0x000007D0)

    def _loc_12FF(): pass

    label('loc_12FF')

    OP_4B(0x0010, 255)
    OP_4B(0x0011, 255)

    Jump('loc_13D4')

    def _loc_130A(): pass

    label('loc_130A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_13D4',
    )

    OP_4A(0x00FE, 255)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_136D',
    )

    ChrTalk(
        0x00FE,
        (
            '竟然能获得大赛冠军，\n',
            '游击士真了不起啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好～接下来我来\n',
            '扮演游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13D0')

    def _loc_136D(): pass

    label('loc_136D')

    ChrTalk(
        0x00FE,
        (
            '诞辰庆典时的利贝尔通讯上\n',
            '登了武术大赛的内容！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说游击士队获得了冠军。\n',
            '游击士果然强啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_13D0(): pass

    label('loc_13D0')

    OP_4B(0x00FE, 255)

    def _loc_13D4(): pass

    label('loc_13D4')

    TalkEnd(0x0010)

    Return()

# id: 0x000D offset: 0x13D8
@scena.Code('func_0D_13D8')
def func_0D_13D8():
    TalkBegin(0x0011)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_1427',
    )

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，亚尔摩果然\n',
            '离不开温泉啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只有这个\n',
            '真是无可替代。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1621')

    def _loc_1427(): pass

    label('loc_1427')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1470',
    )

    ChrTalk(
        0x00FE,
        (
            '上回是沸腾，\n',
            '这次又变冷了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……这温泉真任性啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1621')

    def _loc_1470(): pass

    label('loc_1470')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_14FF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_14B6',
    )

    ChrTalk(
        0x00FE,
        (
            '游击士果然了不起啊。\n',
            '这武术大赛冠军可不是盖的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14FC')

    def _loc_14B6(): pass

    label('loc_14B6')

    ChrTalk(
        0x00FE,
        (
            '好像这次游击士\n',
            '也为我们解决了问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，果然了不起啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_14FC(): pass

    label('loc_14FC')

    Jump('loc_1621')

    def _loc_14FF(): pass

    label('loc_14FF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_1544',
    )

    ChrTalk(
        0x00FE,
        (
            '这、这样下去\n',
            '就没法做温泉蛋了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '很快就煮凝固了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1621')

    def _loc_1544(): pass

    label('loc_1544')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_15C7',
    )

    OP_4A(0x0010, 255)
    OP_4A(0x0011, 255)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_158C',
    )

    ChrTalk(
        0x00FE,
        (
            '接下来是分身战技！\n',
            '哼哼，你能看穿吗～～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15BC')

    def _loc_158C(): pass

    label('loc_158C')

    ChrTalk(
        0x00FE,
        (
            '接招，机枪速射！！\n',
            '哒哒哒哒哒哒～～～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_15BC(): pass

    label('loc_15BC')

    OP_4B(0x0010, 255)
    OP_4B(0x0011, 255)

    Jump('loc_1621')

    def _loc_15C7(): pass

    label('loc_15C7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_1621',
    )

    OP_4A(0x00FE, 255)

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，游击士是好，不过\n',
            '特务部队也很酷哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '反派角色也别有风味啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x00FE, 255)

    def _loc_1621(): pass

    label('loc_1621')

    TalkEnd(0x0011)

    Return()

# id: 0x000E offset: 0x1625
@scena.Code('func_0E_1625')
def func_0E_1625():
    TalkBegin(0x0012)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_174D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_1678',
    )

    ChrTalk(
        0x00FE,
        (
            '这、这是爆炸性新闻！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '得、得赶快准备\n',
            '照相机来摄影……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_174A')

    def _loc_1678(): pass

    label('loc_1678')

    ChrTalk(
        0x00FE,
        (
            '这、这是爆炸性新闻！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '得、得赶快准备\n',
            '照相机来摄影……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不、不，你等等\n',
            '应该先记录情况吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼～冷静一点～～\n',
            '冷静地考虑问题～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，嗯……\n',
            '还是应该先拍照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好、好……\n',
            '总、总之先拍！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_174A(): pass

    label('loc_174A')

    Jump('loc_1871')

    def _loc_174D(): pass

    label('loc_174D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_1871',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_17C2',
    )

    ChrTalk(
        0x00FE,
        (
            '每次来这个村庄都能感到\n',
            '其东方风格设计的妙趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈，有机会的话也想\n',
            '放下工作来享受一下啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1871')

    def _loc_17C2(): pass

    label('loc_17C2')

    ChrTalk(
        0x00FE,
        (
            '我是负责利贝尔通讯\n',
            '文化栏的记者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '每次来这个村庄都能感到\n',
            '其东方风格设计的妙趣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我以前也写过\n',
            '这里的旅馆……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过这次是准备为了饮食和\n',
            '体育来这里采访的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_1871(): pass

    label('loc_1871')

    TalkEnd(0x0012)

    Return()

# id: 0x000F offset: 0x1875
@scena.Code('func_0F_1875')
def func_0F_1875():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_1949',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_18FE',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，看来泵\n',
            '开始动了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过我记得这里的设备也\n',
            '应该是导力驱动的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……到底是\n',
            '怎么让它动起来的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    Jump('loc_1946')

    def _loc_18FE(): pass

    label('loc_18FE')

    ChrTalk(
        0x00FE,
        (
            '这里的泵也\n',
            '应该是导力驱动的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，那么是怎样\n',
            '让它动起来的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1946(): pass

    label('loc_1946')

    Jump('loc_1A62')

    def _loc_1949(): pass

    label('loc_1949')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1A62',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A20',
    )

    ChrTalk(
        0x00FE,
        (
            '我们是从沃尔费堡垒\n',
            '被派遣来的巡逻部队。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之现在亚尔摩村\n',
            '还保持着平静。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然很遗憾，温泉的泵也\n',
            '好像停下来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过好在是不影响日常生活的设施。\n',
            '就算保持那样也没什么问题吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    Jump('loc_1A62')

    def _loc_1A20(): pass

    label('loc_1A20')

    ChrTalk(
        0x00FE,
        (
            '温泉的泵也\n',
            '好象停下来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这也是那个\n',
            '停止现象造成的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A62(): pass

    label('loc_1A62')

    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x1A66
@scena.Code('func_10_1A66')
def func_10_1A66():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_1B58',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1B07',
    )

    ChrTalk(
        0x00FE,
        (
            '副队长也感到奇怪，\n',
            '为什么泵会动了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果能让那个动起来，真\n',
            '希望能让我们的枪恢复正常啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为不能使用枪\n',
            '是很令人不安的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    Jump('loc_1B55')

    def _loc_1B07(): pass

    label('loc_1B07')

    ChrTalk(
        0x00FE,
        (
            '因为不能使用枪\n',
            '是很令人不安的',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过在市民面前\n',
            '不能露出半点这种情绪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B55(): pass

    label('loc_1B55')

    Jump('loc_1C6F')

    def _loc_1B58(): pass

    label('loc_1B58')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1C6F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C11',
    )

    ChrTalk(
        0x00FE,
        (
            '我们是从雷斯顿要塞\n',
            '被派遣来的增援部队。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在在和沃尔费堡垒的副队长\n',
            '一起在村里巡逻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '亚尔摩村比我们\n',
            '想象的要安定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不愧是一直\n',
            '都很平静的地方啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    Jump('loc_1C6F')

    def _loc_1C11(): pass

    label('loc_1C11')

    ChrTalk(
        0x00FE,
        (
            '我们是从雷斯顿要塞\n',
            '被派遣来的增援部队。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在在和沃尔费堡垒的副队长\n',
            '一起在村里巡逻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C6F(): pass

    label('loc_1C6F')

    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0x1C73
@scena.Code('func_11_1C73')
def func_11_1C73():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_1CD0',
    )

    ChrTalk(
        0x00FE,
        (
            '水泵小屋的修理\n',
            '好象结束了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这种时候还要到处跑，\n',
            '游击士真不容易啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D6F')

    def _loc_1CD0(): pass

    label('loc_1CD0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1D6F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D38',
    )

    ChrTalk(
        0x00FE,
        (
            '前边是源泉所在的后山哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为是个危险的地方，\n',
            '慎重起见，还是警戒起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0006)

    Jump('loc_1D6F')

    def _loc_1D38(): pass

    label('loc_1D38')

    ChrTalk(
        0x00FE,
        (
            '前边是源泉所在的后山哦。\n',
            '是个危险的地方，请小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D6F(): pass

    label('loc_1D6F')

    TalkEnd(0x00FE)

    Return()

# id: 0x0012 offset: 0x1D73
@scena.Code('func_12_1D73')
def func_12_1D73():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_1E25',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1DDB',
    )

    ChrTalk(
        0x00FE,
        (
            '我是来看看澡堂的，\n',
            '泵好象真的修好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好～这样一来\n',
            '一定能恢复营业了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0007)

    Jump('loc_1E25')

    def _loc_1DDB(): pass

    label('loc_1DDB')

    ChrTalk(
        0x00FE,
        (
            '我们是打工的，\n',
            '所以客人少的话会很危险哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真希望客人\n',
            '快点回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E25(): pass

    label('loc_1E25')

    TalkEnd(0x00FE)

    Return()

# id: 0x0013 offset: 0x1E29
@scena.Code('func_13_1E29')
def func_13_1E29():
    EventBegin(0x00)
    FadeOut(0, 0, -1)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1E4A',
    )

    Call(0, 0x0024)
    Call(0, 0x0025)

    def _loc_1E4A(): pass

    label('loc_1E4A')

    SetChrPos(0x0101, -23960, -2000, 14980, 90)
    SetChrPos(0x0107, -23740, -2000, 16230, 90)
    SetChrPos(0x00F7, -25260, -2000, 15090, 90)
    SetChrPos(0x00F9, -25290, -2000, 16370, 90)
    SetChrPos(0x0008, -6810, -1250, 14740, 270)
    ClearChrFlags(0x0008, 0x0080)
    OP_6D(-21340, -2000, 15680, 0)
    OP_67(0, 8800, -10000, 0)
    OP_6B(2920, 0)
    OP_6C(45000, 0)
    OP_6E(275, 0)

    @scena.Lambda('lambda_1EE7')
    def lambda_1EE7():
        OP_6D(-19340, -2000, 15680, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1EE7)

    @scena.Lambda('lambda_1EFF')
    def lambda_1EFF():
        OP_8E(0x00FE, -19960, -2000, 14980, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1EFF)

    Sleep(100)

    @scena.Lambda('lambda_1F1F')
    def lambda_1F1F():
        OP_8E(0x00FE, -19740, -2000, 16230, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0000, lambda_1F1F)

    Sleep(100)

    @scena.Lambda('lambda_1F3F')
    def lambda_1F3F():
        OP_8E(0x00FE, -21260, -2000, 15090, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0000, lambda_1F3F)

    Sleep(100)

    @scena.Lambda('lambda_1F5F')
    def lambda_1F5F():
        OP_8E(0x00FE, -21290, -2000, 16370, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0000, lambda_1F5F)

    OP_C8(0x0080, 0x0046, 'C_PLAC10._CH', 0x01, 0x07D0)
    ShowPlaceName('亚尔摩村')
    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0107, 0x0000)

    NpcTalk(
        0x0008,
        '老婆婆的声音',
        (
            '#0570230856V#3P哟，你们来了啊。',
            TxtCtl.Enter,
        ),
    )

    WaitForThreadExit(0x00F7, 0x0000)
    WaitForThreadExit(0x00F9, 0x0000)
    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0107, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(100)

    OP_62(0x00F7, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_20D6',
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
            TXT(0x00, '【◇已经和麻绪婆婆重逢】\n'),
            TXT(0x01, '【◇尚未和麻绪婆婆重逢】\n'),
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
        (0x00000000, 'loc_20C1'),
        (0x00000001, 'loc_20C7'),
        (-1, 'loc_20CD'),
    )

    def _loc_20C1(): pass

    label('loc_20C1')

    OP_A2(0x1482)

    Jump('loc_20CD')

    def _loc_20C7(): pass

    label('loc_20C7')

    OP_A3(0x1482)

    Jump('loc_20CD')

    def _loc_20CD(): pass

    label('loc_20CD')

    FadeIn(300, 0)

    def _loc_20D6(): pass

    label('loc_20D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0290, 2, 0x1482)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2351',
    )

    ChrTalk(
        0x0101,
        (
            '#0010230857V#1004F#6P……麻绪婆婆！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_210F')
    def lambda_210F():
        OP_6D(-11110, -2000, 15260, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_210F)

    WaitForThreadExit(0x0000, 0x0000)

    @scena.Lambda('lambda_212C')
    def lambda_212C():
        OP_6D(-12380, -2000, 15930, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_212C)

    @scena.Lambda('lambda_2144')
    def lambda_2144():
        OP_67(0, 12500, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_2144)

    @scena.Lambda('lambda_215C')
    def lambda_215C():
        OP_6B(2590, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_215C)

    @scena.Lambda('lambda_216C')
    def lambda_216C():
        OP_6E(262, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_216C)

    @scena.Lambda('lambda_217C')
    def lambda_217C():
        OP_8E(0x0008, -11420, -2000, 15520, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_217C)

    @scena.Lambda('lambda_2197')
    def lambda_2197():
        OP_8E(0x00FE, -12960, -2000, 14980, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2197)

    Sleep(100)

    @scena.Lambda('lambda_21B7')
    def lambda_21B7():
        OP_8E(0x00FE, -12740, -2000, 16230, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0000, lambda_21B7)

    Sleep(100)

    @scena.Lambda('lambda_21D7')
    def lambda_21D7():
        OP_8E(0x00FE, -14260, -2000, 15090, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0000, lambda_21D7)

    Sleep(100)

    @scena.Lambda('lambda_21F7')
    def lambda_21F7():
        OP_8E(0x00FE, -14290, -2000, 16370, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0000, lambda_21F7)

    WaitForThreadExit(0x0008, 0x0002)

    ChrTalk(
        0x0008,
        (
            '#0570230858V#680F哟，艾丝蒂尔，好久不见。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570230859V与以前来的时候相比\n',
            '一下子变得更像大人了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230860V#1016F#6P嘿嘿……是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010230861V#1025F那个，其实我们过来\n',
            '是有事情要办的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570230862V#682F嗯，工房长刚才\n',
            '就已经联系过我了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570230863V好像是蔡斯的很多地方\n',
            '都发生了奇怪的地震是吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_250D')

    def _loc_2351(): pass

    label('loc_2351')

    ChrTalk(
        0x0107,
        (
            '#0070230864V#560F#6P 麻绪婆婆！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_237C')
    def lambda_237C():
        OP_6D(-11110, -2000, 15260, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_237C)

    WaitForThreadExit(0x0000, 0x0000)

    @scena.Lambda('lambda_2399')
    def lambda_2399():
        OP_6D(-12380, -2000, 15930, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_2399)

    @scena.Lambda('lambda_23B1')
    def lambda_23B1():
        OP_67(0, 12500, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_23B1)

    @scena.Lambda('lambda_23C9')
    def lambda_23C9():
        OP_6B(2590, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_23C9)

    @scena.Lambda('lambda_23D9')
    def lambda_23D9():
        OP_6E(262, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_23D9)

    @scena.Lambda('lambda_23E9')
    def lambda_23E9():
        OP_8E(0x0008, -11420, -2000, 15520, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_23E9)

    @scena.Lambda('lambda_2404')
    def lambda_2404():
        OP_8E(0x00FE, -12960, -2000, 14980, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2404)

    Sleep(100)

    @scena.Lambda('lambda_2424')
    def lambda_2424():
        OP_8E(0x00FE, -12740, -2000, 16230, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0000, lambda_2424)

    Sleep(100)

    @scena.Lambda('lambda_2444')
    def lambda_2444():
        OP_8E(0x00FE, -14260, -2000, 15090, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0000, lambda_2444)

    Sleep(100)

    @scena.Lambda('lambda_2464')
    def lambda_2464():
        OP_8E(0x00FE, -14290, -2000, 16370, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0000, lambda_2464)

    WaitForThreadExit(0x0008, 0x0002)

    ChrTalk(
        0x0008,
        (
            '#0570230865V#680F哟，提妲、艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570230866V刚才工房长\n',
            '很快就联系我了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570230863V好像是蔡斯的很多地方\n',
            '都发生了奇怪的地震是吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_250D(): pass

    label('loc_250D')

    ChrTalk(
        0x0101,
        (
            '#0010230868V#1007F#6P是吗……\n',
            '嗯，那话说起来就方便了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570230869V#682F其实就在刚才，我们\n',
            '这边也发生了奇怪的事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570230870V正准备要联系你们\n',
            '游击士协会呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070230871V#064F#6P呜哎……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230872V#1005F#6P莫非，是地震！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570230873V#685F不巧，倒不是地震……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570230874V#682F百闻不如一见。\n',
            '好了，你们亲自去确认一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0008, 90, 400)

    @scena.Lambda('lambda_267D')
    def lambda_267D():
        OP_90(0x0008, 20000, 0, -200, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_267D)

    @scena.Lambda('lambda_2698')
    def lambda_2698():
        OP_6D(17080, 2500, 17170, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2698)

    @scena.Lambda('lambda_26B0')
    def lambda_26B0():
        OP_67(0, 8820, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_26B0)

    @scena.Lambda('lambda_26C8')
    def lambda_26C8():
        OP_6B(3120, 11000)

        ExitThread()

    DispatchAsync(0x0107, 0x0002, lambda_26C8)

    @scena.Lambda('lambda_26D8')
    def lambda_26D8():
        OP_6C(57000, 11000)

        ExitThread()

    DispatchAsync(0x0107, 0x0003, lambda_26D8)

    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(100)

    OP_62(0x0107, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    @scena.Lambda('lambda_2716')
    def lambda_2716():
        OP_90(0x00FE, 20000, 0, -200, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2716)

    Sleep(200)

    @scena.Lambda('lambda_2736')
    def lambda_2736():
        OP_90(0x00FE, 20000, 0, -200, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_2736)

    Sleep(100)

    @scena.Lambda('lambda_2756')
    def lambda_2756():
        OP_90(0x00FE, 20000, 0, -200, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_2756)

    Sleep(100)

    @scena.Lambda('lambda_2776')
    def lambda_2776():
        OP_90(0x00FE, 20000, 0, -200, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_2776)

    WaitForThreadExit(0x0101, 0x0002)
    TerminateThread(0x0008, 0x01)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0107, 0x01)
    TerminateThread(0x00F7, 0x01)
    TerminateThread(0x00F9, 0x01)
    OP_8C(0x0101, 90, 0)
    OP_8C(0x0107, 90, 0)
    OP_8C(0x00F7, 90, 0)
    OP_8C(0x00F9, 90, 0)

    @scena.Lambda('lambda_27C6')
    def lambda_27C6():
        OP_8E(0x00FE, 13740, 2500, 15950, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_27C6)

    @scena.Lambda('lambda_27E1')
    def lambda_27E1():
        OP_8F(0x00FE, 14010, 2500, 16570, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_27E1)

    @scena.Lambda('lambda_27FC')
    def lambda_27FC():
        OP_8F(0x00FE, 13930, 2500, 17720, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_27FC)

    @scena.Lambda('lambda_2817')
    def lambda_2817():
        OP_8F(0x00FE, 12960, 2500, 18000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_2817)

    @scena.Lambda('lambda_2832')
    def lambda_2832():
        OP_8F(0x00FE, 12920, 2500, 16780, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_2832)

    WaitForThreadExit(0x0008, 0x0001)

    @scena.Lambda('lambda_2852')
    def lambda_2852():
        OP_8C(0x00FE, 275, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2852)

    @scena.Lambda('lambda_2860')
    def lambda_2860():
        OP_8E(0x00FE, 13770, 2500, 14550, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2860)

    WaitForThreadExit(0x0008, 0x0001)
    OP_8C(0x0008, 0, 400)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0107, 0x0001)
    WaitForThreadExit(0x00F7, 0x0001)
    WaitForThreadExit(0x00F9, 0x0001)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0107, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(100)

    OP_62(0x00F7, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010230875V#1020F#5P这、这是……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070230876V#065F#5P沸腾起来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2952')
    def lambda_2952():
        OP_6D(15000, 2500, 16149, 1300)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2952)

    @scena.Lambda('lambda_296A')
    def lambda_296A():
        OP_67(0, 8500, -10000, 1300)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_296A)

    @scena.Lambda('lambda_2982')
    def lambda_2982():
        OP_6B(2870, 1300)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2982)

    @scena.Lambda('lambda_2992')
    def lambda_2992():
        OP_8C(0x0107, 180, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_2992)

    @scena.Lambda('lambda_29A0')
    def lambda_29A0():
        OP_8C(0x00F7, 180, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_29A0)

    OP_8C(0x0101, 180, 400)
    OP_8C(0x00F9, 180, 400)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_29F6',
    )

    ChrTalk(
        0x0106,
        (
            '#0050230877V#057F到底是怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A1F')

    def _loc_29F6(): pass

    label('loc_29F6')

    ChrTalk(
        0x0103,
        (
            '#0030230878V#022F这到底是怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A1F(): pass

    label('loc_2A1F')

    ChrTalk(
        0x0008,
        (
            '#0570230879V#685F原因我也不清楚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570230880V#682F在接到工房长先生的联络之前不久，\n',
            '外面突然变得很嘈杂。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570230881V我就出来看了个究竟，\n',
            '结果就发现已经变成这样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070230882V#065F莫、莫非是\n',
            '泵装置坏掉了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230883V比如说发热系统出了故障……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570230884V#682F不，我刚才去看了，\n',
            '正常得和平时没两样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570230885V大概是源泉的温度\n',
            '一下子变高了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230886V#1015F#5P这不是很少见吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570230887V#685F我迁居这里已经５０年了，\n',
            '不过碰到这么奇怪的事还是第一次。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570230888V#682F总觉得有一种不祥的预感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2CC2',
    )

    ChrTalk(
        0x0104,
        (
            '#0040230889V#035F呼，说不定和那些\n',
            '地震有关系。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040230890V#030F比如说七耀脉的活性化──使得\n',
            '源泉的温度上升了之类的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D3E')

    def _loc_2CC2(): pass

    label('loc_2CC2')

    ChrTalk(
        0x0105,
        (
            '#0060230891V#047F……这可能和那些\n',
            '地震有关系。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060230892V#042F比如说七耀脉的活性化──使得\n',
            '源泉的温度上升了之类的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2D3E(): pass

    label('loc_2D3E')

    ChrTalk(
        0x0107,
        (
            '#0070230893V#065F我、我觉得\n',
            '很有可能。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070230894V如果温度再这么继续上升的话\n',
            '问题可能就严重了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230895V#1005F#5P这、不是很麻烦么……\n',
            '必须马上查找到原因！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2E47',
    )

    ChrTalk(
        0x0106,
        (
            '#0050230896V#050F喂，婆婆。\n',
            '源泉在哪里？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050230897V我们可以去确认一下吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E9B')

    def _loc_2E47(): pass

    label('loc_2E47')

    ChrTalk(
        0x0103,
        (
            '#0030230898V#020F我说，婆婆。\n',
            '源泉在哪里？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030230899V我们可以去确认一下吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2E9B(): pass

    label('loc_2E9B')

    ChrTalk(
        0x0008,
        (
            '#0570230900V#680F我就知道你们会这么想，\n',
            '所以早就准备好了这个。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570230901V#681F好，收下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8E(0x0008, 13970, 2500, 15800, 2000, 0x00)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.Item, ItemTable['后山的钥匙']),
            (TxtCtl.SetColor, 0x0),
            '收下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['后山的钥匙'], 1)
    OP_8F(0x0008, 13770, 2500, 15300, 1000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010230902V#1004F#5P这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0570230903V#680F#4P这是在水泵小屋左手边的\n',
            '栅门钥匙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570230904V里面就是亚尔摩温泉\n',
            '源泉涌出的洞窟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230905V#1018F#5P真的！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070230906V#560F还有那样的洞窟啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_307A',
    )

    ChrTalk(
        0x0106,
        (
            '#0050230907V#051F嘿嘿，多谢帮忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_30A7')

    def _loc_307A(): pass

    label('loc_307A')

    ChrTalk(
        0x0103,
        (
            '#0030230908V#021F呵呵，真是帮了我们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_30A7(): pass

    label('loc_30A7')

    ChrTalk(
        0x0008,
        (
            '#0570230909V#681F#4P哪里的话。\n',
            '是我们在请求你们帮忙啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570230910V#680F沸腾得这么厉害，\n',
            '很快就会没客人来了。\n',
            '而且也不能打扫卫生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0570230911V总之，就拜托你们在调查地震之余，\n',
            '也把这件事情解决吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010230912V#1006F#5P嗯，交给我们吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A3(0x0000)
    OP_8C(0x0008, 180, 400)
    CreateThread(0x0008, 0x01, 0x00, 0x0014)

    @scena.Lambda('lambda_31B6')
    def lambda_31B6():
        OP_6D(18120, 2000, 11950, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_31B6)

    @scena.Lambda('lambda_31CE')
    def lambda_31CE():
        OP_67(0, 8820, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_31CE)

    @scena.Lambda('lambda_31E6')
    def lambda_31E6():
        OP_6C(90000, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_31E6)

    Sleep(1000)

    @scena.Lambda('lambda_31FB')
    def lambda_31FB():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_31FB')

    DispatchAsync2(0x0101, 0x0002, lambda_31FB)

    Sleep(200)

    @scena.Lambda('lambda_3211')
    def lambda_3211():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_3211')

    DispatchAsync2(0x0107, 0x0002, lambda_3211)

    Sleep(200)

    @scena.Lambda('lambda_3227')
    def lambda_3227():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_3227')

    DispatchAsync2(0x00F7, 0x0002, lambda_3227)

    Sleep(200)

    @scena.Lambda('lambda_323D')
    def lambda_323D():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_323D')

    DispatchAsync2(0x00F9, 0x0002, lambda_323D)

    WaitForThreadExit(0x0008, 0x0000)
    WaitForThreadExit(0x0008, 0x0001)
    WaitForThreadExit(0x0008, 0x0002)
    WaitForThreadExit(0x0008, 0x0003)
    TerminateThread(0x0101, 0x02)
    TerminateThread(0x0107, 0x02)
    TerminateThread(0x00F7, 0x02)
    TerminateThread(0x00F9, 0x02)

    @scena.Lambda('lambda_3272')
    def lambda_3272():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3272)

    Sleep(100)

    @scena.Lambda('lambda_3285')
    def lambda_3285():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_3285)

    Sleep(100)

    @scena.Lambda('lambda_3298')
    def lambda_3298():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_3298)

    Sleep(100)

    @scena.Lambda('lambda_32AB')
    def lambda_32AB():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_32AB)

    @scena.Lambda('lambda_32B9')
    def lambda_32B9():
        OP_6D(13550, 2500, 16850, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_32B9)

    @scena.Lambda('lambda_32D1')
    def lambda_32D1():
        OP_6C(85000, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_32D1)

    Sleep(1000)

    @scena.Lambda('lambda_32E6')
    def lambda_32E6():
        OP_8C(0x0101, 315, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_32E6)

    Sleep(50)

    @scena.Lambda('lambda_32F9')
    def lambda_32F9():
        OP_8C(0x00F7, 45, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_32F9)

    Sleep(50)

    @scena.Lambda('lambda_330C')
    def lambda_330C():
        OP_8C(0x0107, 225, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_330C)

    Sleep(50)

    OP_8C(0x00F9, 120, 400)
    WaitForThreadExit(0x0101, 0x0002)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_33B1',
    )

    ChrTalk(
        0x0104,
        (
            '#0040230913V#035F源泉涌出的洞窟吗，\n',
            '有可能就是地震的震源地啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040230914V#030F呼，进去之前应该\n',
            '要做好万全的准备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_342B')

    def _loc_33B1(): pass

    label('loc_33B1')

    ChrTalk(
        0x0105,
        (
            '#0060230915V#047F源泉涌出的洞窟吗，\n',
            '有可能就是地震的震源地啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060230916V#042F进去之前应该\n',
            '先做好充分的准备哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_342B(): pass

    label('loc_342B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_348F',
    )

    ChrTalk(
        0x0106,
        (
            '#0050230917V#057F#4P嗯……\n',
            '十有八九，敌人就在里面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050230918V#057F打起精神来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_34E4')

    def _loc_348F(): pass

    label('loc_348F')

    ChrTalk(
        0x0103,
        (
            '#0030230919V#022F#4P嗯……\n',
            '十有八九，敌人就在里面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030230920V打起精神来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_34E4(): pass

    label('loc_34E4')

    OP_A2(0x1421)
    OP_28(0x0088, 0x01, 0x0002)
    OP_28(0x0088, 0x01, 0x0004)
    EventEnd(0x00)

    Return()

# id: 0x0014 offset: 0x34F6
@scena.Code('func_14_34F6')
def func_14_34F6():
    OP_8E(0x00FE, 13690, 2500, 13690, 2000, 0x00)
    OP_A2(0x0000)
    OP_8E(0x00FE, 15920, 2500, 13570, 2000, 0x00)
    OP_8E(0x00FE, 19810, 2000, 7290, 2000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0015 offset: 0x353B
@scena.Code('func_15_353B')
def func_15_353B():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_354F',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('func_15_353B')

    def _loc_354F(): pass

    label('loc_354F')

    Sleep(500)

    OP_8E(0x00FE, 14230, 2500, 13730, 1700, 0x00)
    OP_8E(0x00FE, 16000, 2500, 13650, 1700, 0x00)
    OP_8E(0x00FE, 15830, 2000, 8490, 1700, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0016 offset: 0x3596
@scena.Code('func_16_3596')
def func_16_3596():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_35AA',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('func_16_3596')

    def _loc_35AA(): pass

    label('loc_35AA')

    OP_8E(0x00FE, 14230, 2500, 13730, 1700, 0x00)
    OP_8E(0x00FE, 16000, 2500, 13650, 1700, 0x00)
    OP_8E(0x00FE, 15830, 2000, 8490, 1700, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0017 offset: 0x35EC
@scena.Code('func_17_35EC')
def func_17_35EC():
    OP_22(0x0074, 0x00, 0x64)
    Sleep(300)

    OP_22(0x0074, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '栅门锁着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 1, 0x1421)),
            Expr.Return,
        ),
        'loc_37B0',
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
            TXT(0x00, '【使用钥匙】\n'),
            TXT(0x01, '【不使用】\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_37AA',
    )

    EventBegin(0x00)
    Fade(1000)
    LoadEffect(0x01, 'map\\\\t32key00.eff')
    OP_6D(40670, 6000, 49640, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 40430, 6000, 48600, 360)
    SetChrPos(0x0107, 40580, 6000, 47300, 360)
    SetChrPos(0x00F7, 39450, 6000, 48600, 360)
    SetChrPos(0x00F9, 39490, 6000, 47300, 360)
    OP_0D()
    OP_22(0x0073, 0x00, 0x64)
    OP_72(0x000B, 0x0800)
    OP_6F(0x000B, 1)
    PlayEffect(0x01, 0x00, 0x00FF, 40000, 6500, 50100, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    OP_22(0x010C, 0x00, 0x64)
    OP_B0(0x000B, 0x1A)
    OP_6F(0x000B, 1)
    OP_70(0x000B, 0x0000000A)
    OP_73(0x000B)
    Sleep(1000)

    OP_6F(0x000B, 10)
    OP_70(0x000B, 0x00000046)
    OP_73(0x000B)
    OP_6F(0x000B, 120)
    OP_64(0x00, 0x0001)
    OP_A2(0x1422)
    EventEnd(0x00)

    Jump('loc_37AD')

    def _loc_37AA(): pass

    label('loc_37AA')

    TalkEnd(0x00FF)

    def _loc_37AD(): pass

    label('loc_37AD')

    Jump('loc_37BC')

    def _loc_37B0(): pass

    label('loc_37B0')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    def _loc_37BC(): pass

    label('loc_37BC')

    Return()

# id: 0x0018 offset: 0x37BD
@scena.Code('func_18_37BD')
def func_18_37BD():
    OP_22(0x0074, 0x00, 0x64)
    Sleep(300)

    OP_22(0x0074, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

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

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 7, 0x2007)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_380B',
    )

    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

    def _loc_380B(): pass

    label('loc_380B')

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
            TXT(0x00, '【使用水泵小屋的钥匙】\n'),
            TXT(0x01, '【不使用】\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3876',
    )

    OP_A2(0x2008)
    OP_22(0x0073, 0x00, 0x64)
    Sleep(1000)

    OP_64(0x01, 0x0001)
    OP_71(0x0003, 0x0010)

    Jump('loc_3876')

    def _loc_3876(): pass

    label('loc_3876')

    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

# id: 0x0019 offset: 0x3883
@scena.Code('func_19_3883')
def func_19_3883():
    EventBegin(0x00)
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    OP_6D(17090, 2500, 16680, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_4A(0x0010, 255)
    OP_4A(0x0011, 255)
    SetChrFlags(0x0010, 0x0080)
    SetChrFlags(0x0011, 0x0080)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    OP_22(0x00E3, 0x00, 0x64)
    Sleep(500)

    PlayEffect(0x8E, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    PlayEffect(0x8D, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_3976')
    def lambda_3976():
        OP_6D(17090, 2500, 16680, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3976)

    @scena.Lambda('lambda_398E')
    def lambda_398E():
        OP_67(0, 8130, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_398E)

    @scena.Lambda('lambda_39A6')
    def lambda_39A6():
        OP_6C(76000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_39A6)

    CreateThread(0x0010, 0x01, 0x00, 0x001A)
    CreateThread(0x0011, 0x01, 0x00, 0x001B)
    CreateThread(0x000B, 0x01, 0x00, 0x001C)
    CreateThread(0x000C, 0x01, 0x00, 0x001D)
    CreateThread(0x001D, 0x01, 0x00, 0x001E)
    CreateThread(0x001E, 0x01, 0x00, 0x001F)
    CreateThread(0x001F, 0x01, 0x00, 0x0020)
    CreateThread(0x0020, 0x01, 0x00, 0x0021)
    CreateThread(0x0021, 0x01, 0x00, 0x0022)
    CreateThread(0x0022, 0x01, 0x00, 0x0023)
    Sleep(8000)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_6D(70100, 1000, 24730, 0)
    OP_67(0, 7650, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(32000, 0)
    OP_6E(285, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    OP_22(0x00E3, 0x00, 0x64)
    Sleep(500)

    PlayEffect(0x8F, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    PlayEffect(0x87, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x88, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(2000)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene('ED6_DT21/T3221._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x001A offset: 0x3B1D
@scena.Code('func_1A_3B1D')
def func_1A_3B1D():
    SetChrPos(0x00FE, 6370, 1250, 16280, 90)
    ClearChrFlags(0x00FE, 0x0080)
    OP_8E(0x00FE, 10220, 2000, 16250, 3000, 0x00)
    OP_8E(0x00FE, 14250, 2500, 17960, 3000, 0x00)
    OP_8C(0x00FE, 90, 400)
    Sleep(800)

    OP_62(0x00FE, 0x00000000, 1700, 0x26, 0x27, 0x000000FA, 0x02)

    Return()

# id: 0x001B offset: 0x3B7A
@scena.Code('func_1B_3B7A')
def func_1B_3B7A():
    Sleep(500)

    SetChrPos(0x00FE, 6330, 1250, 15290, 90)
    ClearChrFlags(0x00FE, 0x0080)
    OP_8E(0x00FE, 9510, 2000, 15070, 3000, 0x00)
    OP_8E(0x00FE, 14240, 2500, 17330, 3000, 0x00)
    OP_8C(0x00FE, 90, 400)
    Sleep(800)

    OP_62(0x00FE, 0x00000000, 1700, 0x26, 0x27, 0x000000FA, 0x02)

    Return()

# id: 0x001C offset: 0x3BDC
@scena.Code('func_1C_3BDC')
def func_1C_3BDC():
    Sleep(2500)

    SetChrPos(0x00FE, 18640, 2000, 9920, 0)
    ClearChrFlags(0x00FE, 0x0080)
    OP_8E(0x00FE, 18230, 2500, 13720, 3000, 0x00)
    Sleep(800)

    OP_62(0x00FE, 0x00000000, 1700, 0x26, 0x27, 0x000000FA, 0x02)

    Return()

# id: 0x001D offset: 0x3C23
@scena.Code('func_1D_3C23')
def func_1D_3C23():
    Sleep(3000)

    SetChrPos(0x00FE, 14660, 2000, 26670, 180)
    ClearChrFlags(0x00FE, 0x0080)
    OP_8E(0x00FE, 14730, 2000, 22500, 3000, 0x00)
    OP_8E(0x00FE, 17030, 2000, 22540, 3000, 0x00)
    OP_8E(0x00FE, 17110, 2500, 20250, 3000, 0x00)
    Sleep(800)

    OP_62(0x00FE, 0x00000000, 1700, 0x26, 0x27, 0x000000FA, 0x02)

    Return()

# id: 0x001E offset: 0x3C92
@scena.Code('func_1E_3C92')
def func_1E_3C92():
    Sleep(3000)

    SetChrPos(0x00FE, 6540, 1500, 14110, 90)
    ClearChrFlags(0x00FE, 0x0080)
    OP_8E(0x00FE, 9620, 2000, 14120, 1500, 0x00)
    OP_8E(0x00FE, 11880, 2000, 15860, 1500, 0x00)
    OP_8E(0x00FE, 13250, 2500, 15880, 1500, 0x00)

    Return()

# id: 0x001F offset: 0x3CEA
@scena.Code('func_1F_3CEA')
def func_1F_3CEA():
    Sleep(1000)

    SetChrPos(0x00FE, 12940, 2000, 8490, 0)
    ClearChrFlags(0x00FE, 0x0080)
    OP_8E(0x00FE, 13330, 2000, 11240, 1000, 0x00)
    Sleep(800)

    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Return()

# id: 0x0020 offset: 0x3D36
@scena.Code('func_20_3D36')
def func_20_3D36():
    Sleep(3000)

    SetChrPos(0x00FE, 20900, 2000, 8650, 0)
    ClearChrFlags(0x00FE, 0x0080)
    OP_8E(0x00FE, 20860, 2000, 11090, 2000, 0x00)
    OP_8E(0x00FE, 17820, 2000, 11710, 2000, 0x00)
    OP_8E(0x00FE, 16239, 2500, 13700, 2000, 0x00)
    OP_8C(0x00FE, 0, 400)
    Sleep(800)

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)

    Return()

# id: 0x0021 offset: 0x3DAC
@scena.Code('func_21_3DAC')
def func_21_3DAC():
    Sleep(5000)

    SetChrPos(0x00FE, 20010, 2000, 6870, 0)
    ClearChrFlags(0x00FE, 0x0080)
    OP_8E(0x00FE, 19920, 2000, 11770, 2000, 0x00)

    Return()

# id: 0x0022 offset: 0x3DDC
@scena.Code('func_22_3DDC')
def func_22_3DDC():
    Sleep(4000)

    SetChrPos(0x00FE, 14510, 2000, 9450, 0)
    ClearChrFlags(0x00FE, 0x0080)
    OP_8E(0x00FE, 14510, 2000, 11880, 2000, 0x00)

    Return()

# id: 0x0023 offset: 0x3E0C
@scena.Code('func_23_3E0C')
def func_23_3E0C():
    Sleep(4000)

    OP_72(0x0002, 0x0010)
    OP_72(0x0002, 0x0020)
    OP_6F(0x0002, 0)
    OP_70(0x0002, 0x0000001D)
    OP_73(0x0002)
    SetChrPos(0x00FE, 21250, 2500, 25000, 180)
    ClearChrFlags(0x00FE, 0x0080)
    OP_8E(0x00FE, 20700, 2000, 22110, 2000, 0x00)
    OP_8E(0x00FE, 18810, 2000, 22070, 2000, 0x00)
    OP_8E(0x00FE, 18350, 2500, 20830, 2000, 0x00)

    Return()

# id: 0x0024 offset: 0x3E7F
@scena.Code('func_24_3E7F')
def func_24_3E7F():
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
        (0x00000000, 'loc_3EF9'),
        (0x00000001, 'loc_3EFF'),
        (-1, 'loc_3F05'),
    )

    def _loc_3EF9(): pass

    label('loc_3EF9')

    OP_A2(0x1200)

    Jump('loc_3F05')

    def _loc_3EFF(): pass

    label('loc_3EFF')

    OP_A2(0x1201)

    Jump('loc_3F05')

    def _loc_3F05(): pass

    label('loc_3F05')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_3F13',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_3F17')

    def _loc_3F13(): pass

    label('loc_3F13')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_3F17(): pass

    label('loc_3F17')

    Return()

# id: 0x0025 offset: 0x3F18
@scena.Code('func_25_3F18')
def func_25_3F18():
    ClearMapFlags(0x00000001)
    OP_6D(0, 0, 0, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_3F52',
    )

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            0x0000,
            0x0002,
            0x0006,
            0x00FF,
        ),
        (
            0x0003,
            0x0004,
            0xFFFF,
        ),
    )

    Jump('loc_3F6C')

    def _loc_3F52(): pass

    label('loc_3F52')

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            0x0000,
            0x0005,
            0x0006,
            0x00FF,
        ),
        (
            0x0003,
            0x0004,
            0xFFFF,
        ),
    )

    def _loc_3F6C(): pass

    label('loc_3F6C')

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0x00000000)

    Return()

# id: 0x0026 offset: 0x3F7E
@scena.Code('func_26_3F7E')
def func_26_3F7E():
    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0011860001V#1001F这里好像可以钓上什么来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3FB6')
    def lambda_3FB6():
        OP_6D(48400, 0, 3440, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_3FB6)

    @scena.Lambda('lambda_3FCE')
    def lambda_3FCE():
        OP_67(0, 9500, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_3FCE)

    @scena.Lambda('lambda_3FE6')
    def lambda_3FE6():
        OP_6B(2800, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_3FE6)

    @scena.Lambda('lambda_3FF6')
    def lambda_3FF6():
        OP_6C(135000, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_3FF6)

    Sleep(1000)

    SetChrName('')

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
        'loc_407D',
    )

    OP_C0(0x0E, 0x00000022, 0x0000CF58, 0x00000000, 0x00001126, 0x0000010E, 0x0000BE28, 0x00000000, 0x000009A6)
    OP_0D()
    EventEnd(0x01)

    Jump('loc_408C')

    def _loc_407D(): pass

    label('loc_407D')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_408C',
    )

    EventEnd(0x01)

    def _loc_408C(): pass

    label('loc_408C')

    Return()

# id: 0x0027 offset: 0x408D
@scena.Code('func_27_408D')
def func_27_408D():
    SetPlaceName(0x0088)

    Return()

# id: 0x0028 offset: 0x4091
@scena.Code('func_28_4091')
def func_28_4091():
    SetPlaceName(0x0087)

    Return()

# id: 0x0029 offset: 0x4095
@scena.Code('func_29_4095')
def func_29_4095():
    SetPlaceName(0x0089)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

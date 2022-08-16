import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T2510_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2510   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2510.x'
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
        ('ED6_DT07/CH02600._CH', 'ED6_DT07/CH02600P._CP'),
        ('ED6_DT07/CH02603._CH', 'ED6_DT07/CH02603P._CP'),
        ('ED6_DT07/CH02390._CH', 'ED6_DT07/CH02390P._CP'),
        ('ED6_DT07/CH02550._CH', 'ED6_DT07/CH02550P._CP'),
        ('ED6_DT07/CH02490._CH', 'ED6_DT07/CH02490P._CP'),
        ('ED6_DT07/CH01663._CH', 'ED6_DT07/CH01663P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH01213._CH', 'ED6_DT07/CH01213P._CP'),
        ('ED6_DT07/CH01430._CH', 'ED6_DT07/CH01430P._CP'),
        ('ED6_DT07/CH01433._CH', 'ED6_DT07/CH01433P._CP'),
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT07/CH00050._CH', 'ED6_DT07/CH00050P._CP'),
        ('ED6_DT07/CH01360._CH', 'ED6_DT07/CH01360P._CP'),
        ('ED6_DT07/CH01590._CH', 'ED6_DT07/CH01590P._CP'),
        ('ED6_DT07/CH01370._CH', 'ED6_DT07/CH01370P._CP'),
        ('ED6_DT07/CH01080._CH', 'ED6_DT07/CH01080P._CP'),
        ('ED6_DT07/CH01090._CH', 'ED6_DT07/CH01090P._CP'),
        ('ED6_DT07/CH01590._CH', 'ED6_DT07/CH01590P._CP'),
        ('ED6_DT07/CH01580._CH', 'ED6_DT07/CH01580P._CP'),
        ('ED6_DT27/CH03750._CH', 'ED6_DT27/CH03750P._CP'),
        ('ED6_DT07/CH01580._CH', 'ED6_DT07/CH01580P._CP'),
        ('ED6_DT07/CH01090._CH', 'ED6_DT07/CH01090P._CP'),
        ('ED6_DT27/CH03610._CH', 'ED6_DT27/CH03610P._CP'),
        ('ED6_DT07/CH01370._CH', 'ED6_DT07/CH01370P._CP'),
        ('ED6_DT07/CH01360._CH', 'ED6_DT07/CH01360P._CP'),
        ('ED6_DT07/CH01370._CH', 'ED6_DT07/CH01370P._CP'),
        ('ED6_DT26/CH20501._CH', 'ED6_DT26/CH20501P._CP'),
    ]

# id: 0x10001 offset: 0x182
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '科林兹校长',
            x                   = 116010,
            z                   = 200,
            y                   = 4800,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001B,
        ),
        ScenaNpcData(
            name                = '乔儿',
            x                   = 30700,
            z                   = 0,
            y                   = 55110,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            name                = '汉斯',
            x                   = 29460,
            z                   = 0,
            y                   = 53800,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001F,
        ),
        ScenaNpcData(
            name                = '珐奥娜',
            x                   = 41200,
            z                   = 0,
            y                   = 7500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001A,
        ),
        ScenaNpcData(
            name                = '拉迪奥老师',
            x                   = 87640,
            z                   = 200,
            y                   = 2820,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0019,
        ),
        ScenaNpcData(
            name                = '碧欧拉老师',
            x                   = 89300,
            z                   = 0,
            y                   = 1960,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0018,
        ),
        ScenaNpcData(
            name                = '米丽亚老师',
            x                   = 86880,
            z                   = 0,
            y                   = 4250,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0017,
        ),
        ScenaNpcData(
            name                = '雪拉扎德',
            x                   = 85540,
            z                   = 0,
            y                   = 4250,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0016,
        ),
        ScenaNpcData(
            name                = '阿加特',
            x                   = 85540,
            z                   = 0,
            y                   = 4250,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            name                = '罗迪',
            x                   = 29880,
            z                   = 0,
            y                   = -280,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '雅莉丝',
            x                   = 2630,
            z                   = 0,
            y                   = 1500,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            name                = '黛拉',
            x                   = 37090,
            z                   = 0,
            y                   = 1590,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            name                = '罗基克',
            x                   = 4800,
            z                   = 250,
            y                   = 28940,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '塞尔玛',
            x                   = 43890,
            z                   = 0,
            y                   = 34970,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '莉秋儿',
            x                   = 36990,
            z                   = 0,
            y                   = 30690,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '巴托姆',
            x                   = 47460,
            z                   = 0,
            y                   = 32880,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '基诺奇奥',
            x                   = 93000,
            z                   = 0,
            y                   = 31990,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '妮吉塔',
            x                   = 95320,
            z                   = 250,
            y                   = 33480,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '亚吉鲁',
            x                   = 44150,
            z                   = 0,
            y                   = 270,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '米克',
            x                   = -4120,
            z                   = 0,
            y                   = 5200,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '莫妮卡',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001C,
        ),
        ScenaNpcData(
            name                = '德尼斯',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 24,
            chipIndex           = 24,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001D,
        ),
        ScenaNpcData(
            name                = '蕾娜',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 25,
            chipIndex           = 25,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x001E,
        ),
        ScenaNpcData(
            name                = '基尔巴特',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '坎诺',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0020,
        ),
        ScenaNpcData(
            name                = '帕布尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0021,
        ),
        ScenaNpcData(
            name                = '强化猎兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
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
            dword_10            = 22,
            chipIndex           = 22,
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
            dword_10            = 22,
            chipIndex           = 22,
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
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
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
    )

# id: 0x10002 offset: 0x562
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x562
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 51000,
            y           = 0,
            z           = 1400,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000053,
        ),
        ScenaEventData(
            x           = 59000,
            y           = 0,
            z           = 1400,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000054,
        ),
        ScenaEventData(
            x           = 33000,
            y           = 0,
            z           = 1400,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000055,
        ),
        ScenaEventData(
            x           = 58990,
            y           = 0,
            z           = 31330,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000056,
        ),
        ScenaEventData(
            x           = 33000,
            y           = 0,
            z           = 31400,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000057,
        ),
    )

# id: 0x10004 offset: 0x602
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 41150,
            triggerZ            = 0,
            triggerY            = 5500,
            triggerRange        = 400,
            actorX              = 41200,
            actorZ              = 1700,
            actorY              = 7500,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 116010,
            triggerZ            = 0,
            triggerY            = 2750,
            triggerRange        = 400,
            actorX              = 116010,
            actorZ              = 1700,
            actorY              = 4800,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 51020,
            triggerZ            = 0,
            triggerY            = 31860,
            triggerRange        = 800,
            actorX              = 51020,
            actorZ              = 1500,
            actorY              = 31860,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0052,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x66E
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_72E',
    )

    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x001B, 0x0080)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0017, 0x0080)
    ChrSetPos(0x0020, -1060, 0, 2530, 180)
    ChrClearFlags(0x0020, 0x0080)
    ChrSetPos(0x0021, -1080, 0, 1310, 0)
    ChrClearFlags(0x0021, 0x0080)
    ChrSetPos(0x0015, -3670, 0, 33860, 90)
    ChrSetPos(0x0016, 2300, 0, 34190, 180)
    ChrClearFlags(0x0016, 0x0080)
    CreateThread(0x0016, 0x00, 0x06, func_02_E4E)
    ChrSetPos(0x0018, 92160, 0, 34030, 0)
    ChrSetPos(0x0019, 92160, 0, 35490, 180)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0418, 4, 0x20C4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_71F',
    )

    ChrSetFlags(0x0018, 0x0010)

    Jump('loc_726')

    def _loc_71F(): pass

    label('loc_71F')

    ChrSetDirection(0x0019, 0, 0)

    def _loc_726(): pass

    label('loc_726')

    ChrSetFlags(0x0019, 0x0010)

    Jump('loc_C31')

    def _loc_72E(): pass

    label('loc_72E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 7, 0x201F)),
            Expr.Return,
        ),
        'loc_A47',
    )

    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x001B, 0x0080)
    ChrSetFlags(0x0019, 0x0080)
    ChrSetFlags(0x0016, 0x0080)
    ChrSetPos(0x000B, 114760, 0, 5010, 90)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0404, 6, 0x2026)),
            Expr.Return,
        ),
        'loc_79A',
    )

    ChrSetPos(0x000A, 3470, 0, 2580, 180)
    ChrSetPos(0x0009, 3500, 0, 1470, 0)

    Jump('loc_7BC')

    def _loc_79A(): pass

    label('loc_79A')

    ChrSetPos(0x000A, 3470, 0, 2580, 270)
    ChrSetPos(0x0009, 3500, 0, 1470, 270)

    def _loc_7BC(): pass

    label('loc_7BC')

    ChrSetPos(0x0020, -240, 0, 3050, 90)
    ChrSetPos(0x0012, -550, 0, 1740, 90)
    ChrSetPos(0x0021, 350, 0, 1140, 90)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x0020, 0x0080)
    ChrClearFlags(0x0021, 0x0080)
    CreateThread(0x0012, 0x00, 0x06, func_02_E4E)
    ChrSetPos(0x0014, 260, 0, 32820, 225)
    ChrSetPos(0x001A, 170, 0, 30840, 0)
    ChrSetPos(0x0015, -1090, 0, 33310, 180)
    ChrSetPos(0x001C, -1100, 0, 31200, 45)
    ChrClearFlags(0x001A, 0x0080)
    ChrClearFlags(0x001C, 0x0080)
    ChrSetPos(0x0018, 92640, 0, 35500, 0)
    ChrSetPos(0x0017, 91490, 0, 35490, 0)
    ChrClearFlags(0x001D, 0x0080)
    ChrClearFlags(0x001E, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 1, 0x2029)),
            Expr.Return,
        ),
        'loc_8B0',
    )

    ChrSetPos(0x001D, 94990, 250, 35500, 233)
    ChrSetPos(0x001E, 94520, 250, 33430, 270)

    Jump('loc_8D2')

    def _loc_8B0(): pass

    label('loc_8B0')

    ChrSetPos(0x001D, 94550, 250, 34350, 180)
    ChrSetPos(0x001E, 94520, 250, 33430, 0)

    def _loc_8D2(): pass

    label('loc_8D2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0416, 7, 0x20B7)),
            Expr.Return,
        ),
        'loc_930',
    )

    ChrSetPos(0x0022, 42290, 0, 3240, 180)
    ChrSetPos(0x0023, 39710, 0, 1520, 180)
    ChrClearFlags(0x0022, 0x0080)
    ChrClearFlags(0x0023, 0x0080)
    ChrClearFlags(0x0022, 0x0001)
    ChrSetFlags(0x0022, 0x0002)
    ChrSetChipByIndex(0x0022, 26)
    ChrSetSubChip(0x0022, 10)
    ChrClearFlags(0x0023, 0x0001)
    ChrSetFlags(0x0023, 0x0002)
    ChrSetChipByIndex(0x0023, 26)
    ChrSetSubChip(0x0023, 13)

    Jump('loc_9E9')

    def _loc_930(): pass

    label('loc_930')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0417, 0, 0x20B8)),
            Expr.Return,
        ),
        'loc_98E',
    )

    ChrSetPos(0x0022, 54400, 0, 970, 90)
    ChrSetPos(0x0023, 55400, 0, -1460, 90)
    ChrClearFlags(0x0022, 0x0080)
    ChrClearFlags(0x0023, 0x0080)
    ChrClearFlags(0x0022, 0x0001)
    ChrSetFlags(0x0022, 0x0002)
    ChrSetChipByIndex(0x0022, 26)
    ChrSetSubChip(0x0022, 9)
    ChrClearFlags(0x0023, 0x0001)
    ChrSetFlags(0x0023, 0x0002)
    ChrSetChipByIndex(0x0023, 26)
    ChrSetSubChip(0x0023, 12)

    Jump('loc_9E9')

    def _loc_98E(): pass

    label('loc_98E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0417, 1, 0x20B9)),
            Expr.Return,
        ),
        'loc_9E9',
    )

    ChrSetPos(0x0022, 28800, 0, 700, 270)
    ChrSetPos(0x0023, 29240, 0, -1490, 270)
    ChrClearFlags(0x0022, 0x0080)
    ChrClearFlags(0x0023, 0x0080)
    ChrClearFlags(0x0022, 0x0001)
    ChrSetFlags(0x0022, 0x0002)
    ChrSetChipByIndex(0x0022, 26)
    ChrSetSubChip(0x0022, 10)
    ChrClearFlags(0x0023, 0x0001)
    ChrSetFlags(0x0023, 0x0002)
    ChrSetChipByIndex(0x0023, 26)
    ChrSetSubChip(0x0023, 12)

    def _loc_9E9(): pass

    label('loc_9E9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0404, 7, 0x2027)),
            Expr.Return,
        ),
        'loc_A44',
    )

    ChrSetPos(0x0024, 39960, 0, 29850, 0)
    ChrSetPos(0x0025, 42350, 0, 29860, 0)
    ChrClearFlags(0x0024, 0x0080)
    ChrClearFlags(0x0025, 0x0080)
    ChrClearFlags(0x0024, 0x0001)
    ChrSetFlags(0x0024, 0x0002)
    ChrSetChipByIndex(0x0024, 26)
    ChrSetSubChip(0x0024, 10)
    ChrClearFlags(0x0025, 0x0001)
    ChrSetFlags(0x0025, 0x0002)
    ChrSetChipByIndex(0x0025, 26)
    ChrSetSubChip(0x0025, 13)

    def _loc_A44(): pass

    label('loc_A44')

    Jump('loc_C31')

    def _loc_A47(): pass

    label('loc_A47')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_AF2',
    )

    ChrSetPos(0x000D, 5370, 250, 33230, 90)
    ChrSetPos(0x000E, 84100, 0, 4951, 0)
    ChrSetPos(0x0014, -3980, 0, 35495, 0)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0015, 0x0080)
    ChrSetFlags(0x0016, 0x0080)
    ChrSetFlags(0x001B, 0x0080)
    ChrSetPos(0x0013, 43530, 0, 1620, 270)
    CreateThread(0x0013, 0x00, 0x00, func_02_E4E)
    ChrSetPos(0x001A, 38230, 0, 1730, 180)
    ChrClearFlags(0x001A, 0x0080)
    ChrSetPos(0x0019, 86480, 0, 28510, 270)
    ChrSetPos(0x0018, 85350, 0, 28510, 90)
    ChrSetFlags(0x0019, 0x0010)

    Jump('loc_C31')

    def _loc_AF2(): pass

    label('loc_AF2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 2, 0x1222)),
            Expr.Return,
        ),
        'loc_AFC',
    )

    Jump('loc_C31')

    def _loc_AFC(): pass

    label('loc_AFC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 1, 0x1221)),
            Expr.Return,
        ),
        'loc_BBA',
    )

    ChrSetPos(0x0018, 88900, 0, 34610, 180)
    ChrSetPos(0x0019, 88910, 0, 33380, 0)
    ChrSetFlags(0x0019, 0x0010)
    ChrSetFlags(0x0018, 0x0010)
    ChrSetPos(0x0017, 92170, 0, 30030, 270)
    ChrSetPos(0x0015, 42770, 0, 5270, 0)
    ChrSetFlags(0x001B, 0x0080)
    ChrSetFlags(0x000D, 0x0004)
    ChrSetFlags(0x000D, 0x0040)
    ChrSetPos(0x000D, 84430, 200, 1120, 90)
    ChrSetFlags(0x000D, 0x0010)
    TerminateThread(0x000D, 0x00)
    ChrSetChipByIndex(0x000D, 7)
    ChrSetSubChip(0x000D, 0)
    ChrSetFlags(0x000E, 0x0004)
    ChrSetFlags(0x000E, 0x0040)
    ChrSetPos(0x000E, 84510, 200, 2890, 90)
    ChrSetFlags(0x000E, 0x0010)
    TerminateThread(0x000E, 0x00)
    ChrSetChipByIndex(0x000E, 9)
    ChrSetSubChip(0x000E, 0)
    ChrSetFlags(0x0011, 0x0080)

    Jump('loc_C31')

    def _loc_BBA(): pass

    label('loc_BBA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 6, 0x121E)),
            Expr.Return,
        ),
        'loc_C31',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_BD0',
    )

    ChrClearFlags(0x000F, 0x0080)

    Jump('loc_BD5')

    def _loc_BD0(): pass

    label('loc_BD0')

    ChrClearFlags(0x0010, 0x0080)

    def _loc_BD5(): pass

    label('loc_BD5')

    ChrClearFlags(0x0009, 0x0080)
    ChrSetFlags(0x000E, 0x0010)
    ChrClearFlags(0x001B, 0x0080)
    ChrSetPos(0x0009, 82950, 0, 4700, 90)
    ChrClearFlags(0x0009, 0x0080)
    CreateThread(0x0009, 0x00, 0x06, func_02_E4E)
    CreateThread(0x0019, 0x00, 0x00, func_06_EDE)
    CreateThread(0x0018, 0x00, 0x00, func_07_FB3)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0246, 2, 0x1232)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C1C',
    )

    ChrSetFlags(0x0017, 0x0010)

    def _loc_C1C(): pass

    label('loc_C1C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0246, 3, 0x1233)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C2C',
    )

    ChrSetFlags(0x001B, 0x0010)

    Jump('loc_C31')

    def _loc_C2C(): pass

    label('loc_C2C')

    ChrSetFlags(0x001B, 0x0080)

    def _loc_C31(): pass

    label('loc_C31')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_C47',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    Event(0, func_22_61FA)

    Jump('loc_DB3')

    def _loc_C47(): pass

    label('loc_C47')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_C5D',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    MapSetFlags(0x10000000)
    Event(0, func_23_6B68)

    Jump('loc_DB3')

    def _loc_C5D(): pass

    label('loc_C5D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Return,
        ),
        'loc_C73',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    MapSetFlags(0x10000000)
    Event(0, func_24_71A9)

    Jump('loc_DB3')

    def _loc_C73(): pass

    label('loc_C73')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 3, 0x10F3)),
            Expr.Return,
        ),
        'loc_C89',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    MapSetFlags(0x10000000)
    Event(0, func_25_7249)

    Jump('loc_DB3')

    def _loc_C89(): pass

    label('loc_C89')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 4, 0x10F4)),
            Expr.Return,
        ),
        'loc_C9F',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 4, 0x10F4))
    MapSetFlags(0x10000000)
    Event(0, func_26_72D1)

    Jump('loc_DB3')

    def _loc_C9F(): pass

    label('loc_C9F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 5, 0x10F5)),
            Expr.Return,
        ),
        'loc_CB5',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 5, 0x10F5))
    MapSetFlags(0x10000000)
    Event(0, func_27_754D)

    Jump('loc_DB3')

    def _loc_CB5(): pass

    label('loc_CB5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 6, 0x10F6)),
            Expr.Return,
        ),
        'loc_CCB',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 6, 0x10F6))
    MapSetFlags(0x10000000)
    Event(0, func_28_7875)

    Jump('loc_DB3')

    def _loc_CCB(): pass

    label('loc_CCB')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_CF3'),
        (0x00000067, 'loc_D0B'),
        (0x0000006A, 'loc_D23'),
        (0x0000006F, 'loc_D3B'),
        (0x00000072, 'loc_D53'),
        (0x00000074, 'loc_D6B'),
        (0x0000007B, 'loc_D83'),
        (0x00000079, 'loc_D9B'),
        (-1, 'loc_DB3'),
    )

    def _loc_CF3(): pass

    label('loc_CF3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 7, 0x201F)),
            (Expr.TestScenaFlags, ScenaFlag(0x0404, 4, 0x2024)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_D08',
    )

    MapSetFlags(0x10000000)
    Event(0, func_2F_8A28)

    def _loc_D08(): pass

    label('loc_D08')

    Jump('loc_DB3')

    def _loc_D0B(): pass

    label('loc_D0B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 7, 0x201F)),
            (Expr.TestScenaFlags, ScenaFlag(0x0404, 4, 0x2024)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_D20',
    )

    MapSetFlags(0x10000000)
    Event(0, func_2C_846E)

    def _loc_D20(): pass

    label('loc_D20')

    Jump('loc_DB3')

    def _loc_D23(): pass

    label('loc_D23')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 7, 0x201F)),
            (Expr.TestScenaFlags, ScenaFlag(0x0404, 4, 0x2024)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_D38',
    )

    MapSetFlags(0x10000000)
    Event(0, func_29_7E52)

    def _loc_D38(): pass

    label('loc_D38')

    Jump('loc_DB3')

    def _loc_D3B(): pass

    label('loc_D3B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 7, 0x201F)),
            (Expr.TestScenaFlags, ScenaFlag(0x0404, 6, 0x2026)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_D50',
    )

    MapSetFlags(0x10000000)
    Event(0, func_3B_99CA)

    def _loc_D50(): pass

    label('loc_D50')

    Jump('loc_DB3')

    def _loc_D53(): pass

    label('loc_D53')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 7, 0x201F)),
            (Expr.TestScenaFlags, ScenaFlag(0x0404, 5, 0x2025)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_D68',
    )

    MapSetFlags(0x10000000)
    Event(0, func_36_90E2)

    def _loc_D68(): pass

    label('loc_D68')

    Jump('loc_DB3')

    def _loc_D6B(): pass

    label('loc_D6B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 7, 0x201F)),
            (Expr.TestScenaFlags, ScenaFlag(0x0404, 7, 0x2027)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_D80',
    )

    MapSetFlags(0x10000000)
    Event(0, func_40_A553)

    def _loc_D80(): pass

    label('loc_D80')

    Jump('loc_DB3')

    def _loc_D83(): pass

    label('loc_D83')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 7, 0x201F)),
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 0, 0x2028)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_D98',
    )

    MapSetFlags(0x10000000)
    Event(0, func_47_AD91)

    def _loc_D98(): pass

    label('loc_D98')

    Jump('loc_DB3')

    def _loc_D9B(): pass

    label('loc_D9B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 7, 0x201F)),
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 1, 0x2029)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_DB0',
    )

    MapSetFlags(0x10000000)
    Event(0, func_4C_B6BC)

    def _loc_DB0(): pass

    label('loc_DB0')

    Jump('loc_DB3')

    def _loc_DB3(): pass

    label('loc_DB3')

    Return()

# id: 0x0001 offset: 0xDB4
@scena.Code('func_01_DB4')
def func_01_DB4():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_DBE',
    )

    Jump('loc_DF5')

    def _loc_DBE(): pass

    label('loc_DBE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 7, 0x201F)),
            Expr.Return,
        ),
        'loc_DCC',
    )

    OP_64(0x00, 0x0001)

    Jump('loc_DF5')

    def _loc_DCC(): pass

    label('loc_DCC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_DDA',
    )

    OP_64(0x01, 0x0001)

    Jump('loc_DF5')

    def _loc_DDA(): pass

    label('loc_DDA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 2, 0x1222)),
            Expr.Return,
        ),
        'loc_DE4',
    )

    Jump('loc_DF5')

    def _loc_DE4(): pass

    label('loc_DE4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 1, 0x1221)),
            Expr.Return,
        ),
        'loc_DEE',
    )

    Jump('loc_DF5')

    def _loc_DEE(): pass

    label('loc_DEE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 6, 0x121E)),
            Expr.Return,
        ),
        'loc_DF5',
    )

    def _loc_DF5(): pass

    label('loc_DF5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 1, 0x1221)),
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_E0D',
    )

    OP_B1('t2510_y')

    Jump('loc_E16')

    def _loc_E0D(): pass

    label('loc_E0D')

    OP_B1('t2510_n')

    def _loc_E16(): pass

    label('loc_E16')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_E20',
    )

    Jump('loc_E4D')

    def _loc_E20(): pass

    label('loc_E20')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0403, 7, 0x201F)),
            Expr.Return,
        ),
        'loc_E38',
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

    Jump('loc_E4D')

    def _loc_E38(): pass

    label('loc_E38')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 3, 0x2013)),
            Expr.Return,
        ),
        'loc_E4D',
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

    def _loc_E4D(): pass

    label('loc_E4D')

    Return()

# id: 0x0002 offset: 0xE4E
@scena.Code('func_02_E4E')
def func_02_E4E():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_E71',
    )

    OP_8D(0x00FE, 39890, 1860, 43300, -1658, 2000)

    Jump('func_02_E4E')

    def _loc_E71(): pass

    label('loc_E71')

    Return()

# id: 0x0003 offset: 0xE72
@scena.Code('func_03_E72')
def func_03_E72():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_E95',
    )

    OP_8D(0x00FE, 36600, 27090, 39800, 31770, 1500)

    Jump('func_03_E72')

    def _loc_E95(): pass

    label('loc_E95')

    Return()

# id: 0x0004 offset: 0xE96
@scena.Code('func_04_E96')
def func_04_E96():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_EB9',
    )

    OP_8D(0x00FE, 2080, 5500, 3800, -580, 2000)

    Jump('func_04_E96')

    def _loc_EB9(): pass

    label('loc_EB9')

    Return()

# id: 0x0005 offset: 0xEBA
@scena.Code('func_05_EBA')
def func_05_EBA():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_EDD',
    )

    OP_8D(0x00FE, 28190, -1470, 31790, 1270, 1000)

    Jump('func_05_EBA')

    def _loc_EDD(): pass

    label('loc_EDD')

    Return()

# id: 0x0006 offset: 0xEDE
@scena.Code('func_06_EDE')
def func_06_EDE():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_FB2',
    )

    ChrSetDirection(0x00FE, 90, 400)
    def _loc_EEE(): pass

    label('loc_EEE')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_F37',
    )

    Sleep(1000)

    OP_62(0x00FE, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)

    ExecExpressionWithReg(
        0x0002,
        (
            Expr.Rand,
            (Expr.PushLong, 0xA),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_F34',
    )

    OP_63(0x00FE)
    ChrSetDirection(0x00FE, 180, 400)

    Jump('loc_F37')

    def _loc_F34(): pass

    label('loc_F34')

    Jump('loc_EEE')

    def _loc_F37(): pass

    label('loc_F37')

    ChrWalkTo(0x00FE, 95320, 250, 30740, 1000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)
    def _loc_F52(): pass

    label('loc_F52')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_F9B',
    )

    Sleep(1000)

    OP_62(0x00FE, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)

    ExecExpressionWithReg(
        0x0002,
        (
            Expr.Rand,
            (Expr.PushLong, 0xA),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_F98',
    )

    OP_63(0x00FE)
    ChrSetDirection(0x00FE, 0, 400)

    Jump('loc_F9B')

    def _loc_F98(): pass

    label('loc_F98')

    Jump('loc_F52')

    def _loc_F9B(): pass

    label('loc_F9B')

    ChrWalkTo(0x00FE, 95320, 250, 33480, 1000, 0x00)

    Jump('func_06_EDE')

    def _loc_FB2(): pass

    label('loc_FB2')

    Return()

# id: 0x0007 offset: 0xFB3
@scena.Code('func_07_FB3')
def func_07_FB3():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_FD6',
    )

    OP_8D(0x00FE, 92190, 29990, 93420, 33800, 1000)

    Jump('func_07_FB3')

    def _loc_FD6(): pass

    label('loc_FD6')

    Return()

# id: 0x0008 offset: 0xFD7
@scena.Code('func_08_FD7')
def func_08_FD7():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 1, 0x1221)),
            Expr.Return,
        ),
        'loc_105B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 2, 0x12)),
            Expr.Return,
        ),
        'loc_100E',
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

    Jump('loc_1058')

    def _loc_100E(): pass

    label('loc_100E')

    SetScenaFlags(ScenaFlag(0x0002, 2, 0x12))

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

    def _loc_1058(): pass

    label('loc_1058')

    Jump('loc_1879')

    def _loc_105B(): pass

    label('loc_105B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 6, 0x121E)),
            Expr.Return,
        ),
        'loc_1879',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0246, 3, 0x1233)),
            Expr.Return,
        ),
        'loc_10DB',
    )

    ChrTalk(
        0x00FE,
        (
            '校舍后面\n',
            '平时都空无一人，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '想想的话也确实是\n',
            '妖怪最喜欢的地方啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可恶啊，\n',
            '看来以后不能去那里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1879')

    def _loc_10DB(): pass

    label('loc_10DB')

    SetScenaFlags(ScenaFlag(0x0246, 3, 0x1233))
    OP_28(0x0083, 0x01, 0x0010)
    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, -3000, 0, 4850, 270)
    ChrSetPos(0x0105, -2500, 0, 5500, 270)
    ChrClearFlags(0x00FE, 0x0010)

    ExecExpressionWithValue(
        0x0026,
        0x01,
        (
            (Expr.GetChrWork, 0x105, 0x1),
            (Expr.GetChrWork, 0xFE, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0026,
        0x02,
        (
            (Expr.GetChrWork, 0x105, 0x2),
            (Expr.GetChrWork, 0xFE, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0026,
        0x03,
        (
            (Expr.GetChrWork, 0x105, 0x3),
            (Expr.GetChrWork, 0xFE, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x0026, 0)
    OP_0D()

    ChrTalk(
        0x00FE,
        (
            '#1900211194V啊啊～\n',
            '都快饿死了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrSetDirection(0x00FE, 90, 400)

    ChrTalk(
        0x00FE,
        (
            '#1900211195V……啊？有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211196V#1000F啊、嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211197V其实是有点事\n',
            '想问你。',
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
            '#1900211198V奇异的事情吗……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211199V#1002F嗯，比如说有没有看到什么奇怪的东西，\n',
            '或听到可疑的声响之类的？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211200V只要是奇怪的东西，\n',
            '什么都可以。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1900211201V奇怪的东西……吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '#1900211202V……真是的，本来都\n',
            '不愿再想起那件讨厌的事情了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211203V#044F#1P嗯？到底是什么事情呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1900211204V啊啊，这件事我还\n',
            '没和任何人说过呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1900211205V其实我……\n',
            '看到过奇怪的人影。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211206V#1002F…………嗯！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211207V……可以再说的详细一点吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1900211208V啊、啊啊，当然没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1900211209V我在回家之前\n',
            '先到校舍后面转了转。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1900211210V因为学校考试，这里也没什么人，\n',
            '气氛非常不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1900211211V随便走了走，\n',
            '正准备要回去时…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1900211212V忽然发现有个白色的人影\n',
            '飘在空中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1900211213V我绝对没有看错，\n',
            '那肯定是个人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211214V#1015F（白色的人影吗……\n',
            '　与另外的证言相符。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211215V#1002F……那…之后又怎样了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1900211216V那家伙…\n',
            '之后就飞进了后门里边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1900211217V然后就那样\n',
            '消失不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211218V#1002F原来如此……\n',
            '消失在后门那边了吗…？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211219V嗯，这些话要好好\n',
            '记在手册上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211220V#040F#1P啊啊，这很重要的证言。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1900211221V……那么我可以走了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1900211222V我的肚子从刚才开始\n',
            '就饿得快受不了了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211223V#1004F啊啊，真不好意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211224V#1006F非常感谢您的帮忙，\n',
            '这些情报对我们非常有用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1900211225V呵呵，虽然不知道发生了什么事，\n',
            '你们加油吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_180B')
    def lambda_180B():
        ChrTurnDirection(0x0101, 0x001B, 400)
        Yield()

        Jump('lambda_180B')

    DispatchAsync2(0x0101, 0x0001, lambda_180B)

    @scena.Lambda('lambda_181C')
    def lambda_181C():
        ChrTurnDirection(0x0105, 0x001B, 400)
        Yield()

        Jump('lambda_181C')

    DispatchAsync2(0x0105, 0x0001, lambda_181C)

    ChrSetDirection(0x00FE, 180, 400)
    ChrWalkTo(0x00FE, -4070, 0, 80, 2000, 0x00)
    ChrWalkTo(0x00FE, -3200, 0, -1430, 2000, 0x00)
    ChrWalkTo(0x00FE, -590, 0, -1470, 2000, 0x00)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0105, 0x01)
    ChrSetFlags(0x00FE, 0x0080)
    EventEnd(0x00)

    def _loc_1879(): pass

    label('loc_1879')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x187D
@scena.Code('func_09_187D')
def func_09_187D():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 0, 0x2028)),
            Expr.Return,
        ),
        'loc_18CA',
    )

    ChrTalk(
        0x00FE,
        (
            '罗基克那小子\n',
            '好像害怕得要死，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼呼呼……\n',
            '真是丢脸啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_197B')

    def _loc_18CA(): pass

    label('loc_18CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Return,
        ),
        'loc_191E',
    )

    ChrTalk(
        0x00FE,
        (
            '好像有什么东西\n',
            '潜藏在旧校舍。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '或许是亡灵之类的东西\n',
            '也说不定啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_197B')

    def _loc_191E(): pass

    label('loc_191E')

    SetScenaFlags(ScenaFlag(0x0002, 1, 0x11))

    ChrTalk(
        0x00FE,
        (
            '好像有什么东西\n',
            '潜藏在旧校舍。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也许是亡灵之类的东西\n',
            '也说不定啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼呼呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_197B(): pass

    label('loc_197B')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x197F
@scena.Code('func_0A_197F')
def func_0A_197F():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_19F7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0418, 4, 0x20C4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1998',
    )

    Call(0, 0x000C)

    Jump('loc_19F4')

    def _loc_1998(): pass

    label('loc_1998')

    ChrTalk(
        0x00FE,
        (
            '没想到男人\n',
            '竟然会这么笨。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难道不知道这样会\n',
            '让别人很担心的吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '（嘟哝）……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19F4(): pass

    label('loc_19F4')

    Jump('loc_1BD6')

    def _loc_19F7(): pass

    label('loc_19F7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_1A99',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Return,
        ),
        'loc_1A45',
    )

    ChrTalk(
        0x00FE,
        (
            '为什么你要\n',
            '那么轻易就答应啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以后再想反悔也晚了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A96')

    def _loc_1A45(): pass

    label('loc_1A45')

    SetScenaFlags(ScenaFlag(0x0002, 0, 0x10))

    ChrTalk(
        0x00FE,
        (
            '家庭教师～？\n',
            '那也是应试对策吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你…接下那么大的事情\n',
            '真的没问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A96(): pass

    label('loc_1A96')

    Jump('loc_1BD6')

    def _loc_1A99(): pass

    label('loc_1A99')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 1, 0x1221)),
            Expr.Return,
        ),
        'loc_1B44',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Return,
        ),
        'loc_1AF2',
    )

    ChrTalk(
        0x00FE,
        (
            '正确答案是１吧？\n',
            '不是３啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这种问题都能搞错，\n',
            '真是败给你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B41')

    def _loc_1AF2(): pass

    label('loc_1AF2')

    SetScenaFlags(ScenaFlag(0x0002, 0, 0x10))

    ChrTalk(
        0x00FE,
        (
            '正确答案是１吧？\n',
            '不是３啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的……为什么你会\n',
            '这么粗心大意啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B41(): pass

    label('loc_1B41')

    Jump('loc_1BD6')

    def _loc_1B44(): pass

    label('loc_1B44')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 6, 0x121E)),
            Expr.Return,
        ),
        'loc_1BD6',
    )

    OP_63(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Return,
        ),
        'loc_1B95',
    )

    ChrTalk(
        0x00FE,
        (
            '考试期间什么事情\n',
            '也没有发生哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家都在忙着念书。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1BD6')

    def _loc_1B95(): pass

    label('loc_1B95')

    SetScenaFlags(ScenaFlag(0x0002, 0, 0x10))

    ChrTalk(
        0x00FE,
        (
            '啊，有什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '奇怪的事情吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像没什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1BD6(): pass

    label('loc_1BD6')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x1BDA
@scena.Code('func_0B_1BDA')
def func_0B_1BDA():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_1C70',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0418, 4, 0x20C4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1BF3',
    )

    Call(0, 0x000C)

    Jump('loc_1C6D')

    def _loc_1BF3(): pass

    label('loc_1BF3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 7, 0xF)),
            Expr.Return,
        ),
        'loc_1C30',
    )

    ChrTalk(
        0x00FE,
        (
            '啊……怎么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我说了什么\n',
            '不该说的话吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C6D')

    def _loc_1C30(): pass

    label('loc_1C30')

    ChrTalk(
        0x00FE,
        (
            '妮吉塔那家伙……\n',
            '为什么要发火啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯、嗯～不明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C6D(): pass

    label('loc_1C6D')

    Jump('loc_1E8B')

    def _loc_1C70(): pass

    label('loc_1C70')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 1, 0x2029)),
            Expr.Return,
        ),
        'loc_1CE0',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然在这种地方干等着很无聊，\n',
            '不过还是听从专业人士的意见吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请一定把其它的学生\n',
            '也救出来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E8B')

    def _loc_1CE0(): pass

    label('loc_1CE0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_1D93',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Return,
        ),
        'loc_1D3F',
    )

    ChrTalk(
        0x00FE,
        (
            '家庭教师的责任可是\n',
            '非常重大的啊～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '接下这任务以后\n',
            '还真是挺不安的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D90')

    def _loc_1D3F(): pass

    label('loc_1D3F')

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    ChrTalk(
        0x00FE,
        (
            '我开始担任假期时的\n',
            '家庭教师了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为要迎接考试，\n',
            '责任可是很重大的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D90(): pass

    label('loc_1D90')

    Jump('loc_1E8B')

    def _loc_1D93(): pass

    label('loc_1D93')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 1, 0x1221)),
            Expr.Return,
        ),
        'loc_1DFC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Return,
        ),
        'loc_1DC9',
    )

    ChrTalk(
        0x00FE,
        (
            '真是败了……\n',
            '本来是很有自信的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DF9')

    def _loc_1DC9(): pass

    label('loc_1DC9')

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    ChrTalk(
        0x00FE,
        (
            '啊～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那题的答案真的\n',
            '不是３啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1DF9(): pass

    label('loc_1DF9')

    Jump('loc_1E8B')

    def _loc_1DFC(): pass

    label('loc_1DFC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 6, 0x121E)),
            Expr.Return,
        ),
        'loc_1E8B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Return,
        ),
        'loc_1E3F',
    )

    ChrTalk(
        0x00FE,
        (
            '考试期间里发生的怪事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像没什么啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E8B')

    def _loc_1E3F(): pass

    label('loc_1E3F')

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))

    ChrTalk(
        0x00FE,
        (
            '嗯？有什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……考试期间中的\n',
            '奇怪事件吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像没有啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E8B(): pass

    label('loc_1E8B')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x1E8F
@scena.Code('func_0C_1E8F')
def func_0C_1E8F():
    OP_4A(0x0018, 255)
    OP_4A(0x0019, 255)

    ChrTalk(
        0x0018,
        (
            '呼～当人质\n',
            '也是很辛苦的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '是因为太紧张了吗…\n',
            '肩膀都觉得酸痛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '算了，这个无所谓啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '２个人能平安获救\n',
            '就已经很幸运了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '确实如此，不过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '我们也想和你们一起\n',
            '同那些家伙战斗啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '如果大家一起冲上去\n',
            '那些坏蛋就……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '……啊……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '妮吉塔……\n',
            '怎么了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(
        0x0019,
        (
            '#3S笨蛋！\n',
            '你在说什么啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0018, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(400)

    ChrTalk(
        0x0018,
        (
            '哇哇……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '勤务员先生\n',
            '被击伤了啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '你明明知道\n',
            '却还说那种蠢话？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '哇、那个…\n',
            '我明白的，不过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '那、那个、妮吉塔。\n',
            '为什么发这么大的火？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0019, 0, 400)

    ChrTalk(
        0x0019,
        (
            '不…不知道！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0019,
        (
            '你、你自己想吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 7, 0xF))
    SetScenaFlags(ScenaFlag(0x0418, 4, 0x20C4))
    ChrClearFlags(0x0018, 0x0010)
    OP_4B(0x0018, 255)
    OP_4B(0x0019, 255)

    Return()

# id: 0x000D offset: 0x20EE
@scena.Code('func_0D_20EE')
def func_0D_20EE():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 1, 0x2029)),
            Expr.Return,
        ),
        'loc_218A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2154',
    )

    ChrTalk(
        0x00FE,
        (
            '米克真是很\n',
            '幸运呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要不是他遇到大家的话，\n',
            '现在还不知道会怎样呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    Jump('loc_2187')

    def _loc_2154(): pass

    label('loc_2154')

    ChrTalk(
        0x00FE,
        (
            '米克真是很\n',
            '幸运呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之应该感谢他才对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2187(): pass

    label('loc_2187')

    Jump('loc_2BF3')

    def _loc_218A(): pass

    label('loc_218A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_22C9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_223B',
    )

    ChrTalk(
        0x00FE,
        (
            '那么说来，科洛丝。\n',
            '你现在正在放假是吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '其实我这些日子一直在\n',
            '努力练习剑术……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '假期结束后\n',
            '请一定和我再战一场吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F嗯嗯～我也不会输的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_22C6')

    def _loc_223B(): pass

    label('loc_223B')

    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    ChrTalk(
        0x00FE,
        (
            '我也听到事件的传闻了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像是有可疑的人物\n',
            '潜藏在旧校舍了对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是…藏在那种地方\n',
            '究竟要做什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是无法理解啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_22C6(): pass

    label('loc_22C6')

    Jump('loc_2BF3')

    def _loc_22C9(): pass

    label('loc_22C9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 1, 0x1221)),
            Expr.Return,
        ),
        'loc_235A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_2312',
    )

    ChrTalk(
        0x00FE,
        (
            '太阳已经快要\n',
            '下山了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '差不多\n',
            '该准备回去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2357')

    def _loc_2312(): pass

    label('loc_2312')

    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))

    ChrTalk(
        0x00FE,
        (
            '考试总算是\n',
            '熬过去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，这次我的成绩\n',
            '应该还过得去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2357(): pass

    label('loc_2357')

    Jump('loc_2BF3')

    def _loc_235A(): pass

    label('loc_235A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 6, 0x121E)),
            Expr.Return,
        ),
        'loc_2BF3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 5, 0xD)),
            Expr.Return,
        ),
        'loc_23C6',
    )

    ChrTalk(
        0x00FE,
        (
            '要是还有问题的话\n',
            '随时可以来找我问。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0105, 400)

    ChrTalk(
        0x00FE,
        (
            '那么，科洛丝，\n',
            '下次社团活动时再见吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2BF3')

    def _loc_23C6(): pass

    label('loc_23C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0246, 2, 0x1232)),
            Expr.Return,
        ),
        'loc_242E',
    )

    ChrTalk(
        0x00FE,
        (
            '那个白色人影的事情\n',
            '我还没对任何人说过呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只靠揣测来说明事情\n',
            '可不能称作科学的态度。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2BF3')

    def _loc_242E(): pass

    label('loc_242E')

    SetScenaFlags(ScenaFlag(0x0246, 2, 0x1232))
    OP_28(0x0083, 0x01, 0x0008)
    SetScenaFlags(ScenaFlag(0x0001, 5, 0xD))
    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, 46020, 0, 32509, 90)
    ChrSetPos(0x0105, 46140, 0, 33370, 90)
    ChrClearFlags(0x00FE, 0x0010)

    ExecExpressionWithValue(
        0x0026,
        0x01,
        (
            (Expr.GetChrWork, 0x105, 0x1),
            (Expr.GetChrWork, 0xFE, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0026,
        0x02,
        (
            (Expr.GetChrWork, 0x105, 0x2),
            (Expr.GetChrWork, 0xFE, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0026,
        0x03,
        (
            (Expr.GetChrWork, 0x105, 0x3),
            (Expr.GetChrWork, 0xFE, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x0026, 0)
    OP_0D()
    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x00FE, 0x0105, 400)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '#2910211226V啊，科洛丝。\n',
            '考试怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211227V#045F啊，还好吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211228V#040F对了，巴托姆…\n',
            '可以向你打听一些事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2910211229V当然，什么事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211230V#1015F嗯，其实呢……',
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
            '#2910211231V嗯…奇怪的事情吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2910211232V想想的话…\n',
            '说起来确实有……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211233V#1011F啊，就算不知道真相\n',
            '也没有关系哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211234V总之，请把你遇到的事\n',
            '如实地告诉我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2910211235V那样的话，\n',
            '我就试着说说看了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '#2910211236V其实…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2910211237V……我看见了在天空飞舞的人影。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(20)

    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    ChrTalk(
        0x0105,
        (
            '#0060211238V#042F…………！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211239V#1002F……可以把当时的\n',
            '情景详细说给我们听听吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2910211240V嗯，那是考试当天的晚上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2910211241V我留在教室\n',
            '念书……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2910211242V忽然就感觉窗外\n',
            '好像有什么动静。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2910211243V本来还以为是风吹进来了，\n',
            '就起来去关窗户……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2910211244V结果却发现外边\n',
            '飘浮着白色的人影。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211245V#1015F白色的人影……吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211246V#1002F那，之后那个人影\n',
            '怎么样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2910211247V不好意思，那就不清楚了，\n',
            '因为很快就消失了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2910211248V我记得好像是消失在\n',
            '正东方向了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211249V#042F正东方向的话……\n',
            '那不就是旧校舍那边吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211250V#1002F嗯，应该是吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211251V不过，我记得不是\n',
            '太清楚了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2910211252V嗯嗯，这是很有趣的现象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2910211253V我想以后好好研究一下，\n',
            '先简单记录在笔记本上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211254V#1004F研、研究～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060211255V#041F巴托姆\n',
            '是理科班的学生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211256V#1001F啊哈哈，原来是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0105, 0x00FE, 400)

    ChrTalk(
        0x00FE,
        (
            '#2910211257V这些情报对你们有用吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010211258V#1000F嗯，非常有用。\n',
            '是很重要的证言啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010211259V马上记在\n',
            '手册上吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211260V#040F巴托姆，\n',
            '实在是感激不尽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2910211261V哪里，不用客气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00FE, 0, 400)
    EventEnd(0x00)

    def _loc_2BF3(): pass

    label('loc_2BF3')

    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x2BF7
@scena.Code('func_0E_2BF7')
def func_0E_2BF7():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_2DAC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0418, 3, 0x20C3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2D2C',
    )

    OP_62(0x00FE, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '啊～艾丝蒂尔，\n',
            '约修亚………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个、承蒙帮助，\n',
            '真是太谢谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1000F哪里，没事就好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F这次真是天降横祸啊，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '真是的～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，原来科洛丝前辈\n',
            '就是科洛蒂娅公主殿下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '比起这次的事件，\n',
            '这个反而更让我吃惊呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))
    SetScenaFlags(ScenaFlag(0x0418, 3, 0x20C3))

    Jump('loc_2DA9')

    def _loc_2D2C(): pass

    label('loc_2D2C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_2DA9',
    )

    ChrTalk(
        0x00FE,
        (
            '科洛丝前辈竟然\n',
            '就是科洛蒂娅公主殿下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '平时从来都在一起活动，\n',
            '却从来没有注意到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈，我真是\n',
            '迟钝啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CloseMessageWindow()

    def _loc_2DA9(): pass

    label('loc_2DA9')

    Jump('loc_30E9')

    def _loc_2DAC(): pass

    label('loc_2DAC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 1, 0x1221)),
            Expr.Return,
        ),
        'loc_2EAF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_2E1B',
    )

    ChrTalk(
        0x00FE,
        (
            '这次我已经拼命努力了，\n',
            '大概可以取得好成绩吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿～不过和前辈\n',
            '肯定是无法相比的啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2EAC')

    def _loc_2E1B(): pass

    label('loc_2E1B')

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    ChrTalk(
        0x00FE,
        (
            '哈～不管怎么说，\n',
            '考试总算是结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次我已经拼命努力了，\n',
            '大概可以取得好成绩吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0105, 400)

    ChrTalk(
        0x00FE,
        (
            '不过和科洛丝前辈\n',
            '肯定是无法相比的啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2EAC(): pass

    label('loc_2EAC')

    Jump('loc_30E9')

    def _loc_2EAF(): pass

    label('loc_2EAF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 6, 0x121E)),
            Expr.Return,
        ),
        'loc_30E9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0246, 6, 0x1236)),
            Expr.Return,
        ),
        'loc_2F08',
    )

    ChrTalk(
        0x00FE,
        (
            '没记得有什么\n',
            '奇怪的事情发生哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈～没能帮上学姐\n',
            '真是遗憾啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_30E9')

    def _loc_2F08(): pass

    label('loc_2F08')

    SetScenaFlags(ScenaFlag(0x0246, 6, 0x1236))
    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x00FE, 0x0105, 0)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '啊，科洛丝前辈。\n',
            '是有什么东西忘了吗～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F不，只是有点事情\n',
            '要在学校里调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊～是什么事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F这个嘛……',
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
            '哎！？怪异的事件吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯……\n',
            '完全没有发现哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯嗯～真是抱歉。\n',
            '没能帮上你的忙……',
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
            '好，再去找别人问问吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F莉秋儿，谢谢你啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0105, 400)

    ChrTalk(
        0x00FE,
        (
            '哪里，别客气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_30E9(): pass

    label('loc_30E9')

    TalkEnd(0x00FE)

    Return()

# id: 0x000F offset: 0x30ED
@scena.Code('func_0F_30ED')
def func_0F_30ED():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_31D7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3184',
    )

    ChrTalk(
        0x00FE,
        (
            '事件虽然顺利解决了，\n',
            '但接下来也很麻烦呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没有导力器的生活\n',
            '大家都是第一次经历。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '很多不便之处\n',
            '一时还很难适应呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    Jump('loc_31D4')

    def _loc_3184(): pass

    label('loc_3184')

    ChrTalk(
        0x00FE,
        (
            '没有导力器的生活\n',
            '大家都是第一次经历。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '很多不便之处\n',
            '一时还很难适应呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_31D4(): pass

    label('loc_31D4')

    Jump('loc_33BB')

    def _loc_31D7(): pass

    label('loc_31D7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 0, 0x2028)),
            Expr.Return,
        ),
        'loc_3225',
    )

    ChrTalk(
        0x00FE,
        (
            '其它的各位\n',
            '也都平安无事吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '艾丝蒂尔，你们\n',
            '也要小心啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_33BB')

    def _loc_3225(): pass

    label('loc_3225')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 1, 0x1221)),
            Expr.Return,
        ),
        'loc_3313',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_3288',
    )

    ChrTalk(
        0x00FE,
        (
            '我和从王都来的叔叔\n',
            '约定在卢安见面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他会依约前来吗…\n',
            '还真是有些不安啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3310')

    def _loc_3288(): pass

    label('loc_3288')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '叔叔要从王都\n',
            '到卢安来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们已经好久没见了，\n',
            '所以这次准备在卢安见面…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过叔叔这个人比较怪，\n',
            '我担心他不会依约前来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3310(): pass

    label('loc_3310')

    Jump('loc_33BB')

    def _loc_3313(): pass

    label('loc_3313')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 6, 0x121E)),
            Expr.Return,
        ),
        'loc_33BB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_334B',
    )

    ChrTalk(
        0x00FE,
        (
            '考试中什么特别的事情\n',
            '也没发生哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_33BB')

    def _loc_334B(): pass

    label('loc_334B')

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '是……？\n',
            '奇怪的事情……吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，真不巧，\n',
            '我完全不知道呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不好意思，你们还是去\n',
            '问问其它人吧，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_33BB(): pass

    label('loc_33BB')

    TalkEnd(0x00FE)

    Return()

# id: 0x0010 offset: 0x33BF
@scena.Code('func_10_33BF')
def func_10_33BF():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_3608',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0418, 2, 0x20C2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_35BD',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，各位游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真了不起，你们把事件\n',
            '顺利解决了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真不知该怎么感谢你们才好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1001F哪里哪里，\n',
            '这是我们应该做的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1011F哎，怎么样了？\n',
            '稍微冷静一点了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '哈、哈哈，当然了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '沉着冷静\n',
            '可是我的代名词啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1028F嘿～是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1015F#1S虽、虽然有点\n',
            '害怕，不过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1035F（艾丝蒂尔……\n',
            '  不要莽撞行事哦。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1008F（啊，情况果然不容乐观吗？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管怎样\n',
            '大家没事就好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那、那么\n',
            '我就先失礼了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0418, 2, 0x20C2))

    Jump('loc_3605')

    def _loc_35BD(): pass

    label('loc_35BD')

    ChrTalk(
        0x00FE,
        (
            '我只、只不过是保持着\n',
            '应有的警戒心而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '绝、绝没有\n',
            '害怕的哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3605(): pass

    label('loc_3605')

    Jump('loc_3B1F')

    def _loc_3608(): pass

    label('loc_3608')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 0, 0x2028)),
            Expr.Return,
        ),
        'loc_36AD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_366F',
    )

    ChrTalk(
        0x00FE,
        (
            '按、按照指示，\n',
            '我们就在这里待命。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '所、所以拜托你们\n',
            '快点把我们救出来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    Jump('loc_36AA')

    def _loc_366F(): pass

    label('loc_366F')

    ChrTalk(
        0x00FE,
        (
            '越、越快越好！\n',
            '快点把我们救出来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '拜、拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_36AA(): pass

    label('loc_36AA')

    Jump('loc_3B1F')

    def _loc_36AD(): pass

    label('loc_36AD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_37E3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_36F5',
    )

    ChrTalk(
        0x00FE,
        (
            '那么，\n',
            '我也该去社团了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家也许都着急了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_37E0')

    def _loc_36F5(): pass

    label('loc_36F5')

    ChrTurnDirection(0x00FE, 0x0105, 0)
    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '科洛丝，我听说了啊。\n',
            '你开始休假了是吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F嗯，考试结束了，\n',
            '现在就开始休息了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '等假期过完后再见吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，多保重吧，\n',
            '期待下次见面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我准备在放假期间\n',
            '帮忙做些选举活动的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，休假结束后再见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_37E0(): pass

    label('loc_37E0')

    Jump('loc_3B1F')

    def _loc_37E3(): pass

    label('loc_37E3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 1, 0x1221)),
            Expr.Return,
        ),
        'loc_3937',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Return,
        ),
        'loc_384C',
    )

    ChrTalk(
        0x00FE,
        (
            '在我看来，两个候选人\n',
            '的政策都有些不足。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过综合比较的话\n',
            '还是诺曼更加有利些。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3934')

    def _loc_384C(): pass

    label('loc_384C')

    SetScenaFlags(ScenaFlag(0x0001, 2, 0xA))

    ChrTalk(
        0x00FE,
        (
            '卢安市的选举活动\n',
            '好像正在火热进行中呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但在我来看，无论哪个候选人\n',
            '都有政策上的欠缺。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '波尔多斯一方的策略是发展港口式经济，\n',
            '而诺曼一方是主张走观光路线。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我曾经向爸爸波尔多斯\n',
            '提过多次建议……\n',
            '但一点改善也没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3934(): pass

    label('loc_3934')

    Jump('loc_3B1F')

    def _loc_3937(): pass

    label('loc_3937')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 6, 0x121E)),
            Expr.Return,
        ),
        'loc_3B1F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0247, 0, 0x1238)),
            Expr.Return,
        ),
        'loc_3990',
    )

    ChrTalk(
        0x00FE,
        (
            '就我所知\n',
            '没发生什么奇怪的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们还是去问问\n',
            '其它的学生吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3B1F')

    def _loc_3990(): pass

    label('loc_3990')

    SetScenaFlags(ScenaFlag(0x0247, 0, 0x1238))
    ChrTurnDirection(0x00FE, 0x0105, 0)

    ChrTalk(
        0x00FE,
        (
            '呀，科洛丝。\n',
            '有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F嗯，其实有点事\n',
            '想向你打听一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哦，是什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1002F嗯，是这样的……',
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
            '啊，奇怪的事情……吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不好意思，没发现什么。\n',
            '没能帮上忙，真是抱歉啊。',
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
            '有什么需要的话请再来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3B1F(): pass

    label('loc_3B1F')

    TalkEnd(0x00FE)

    Return()

# id: 0x0011 offset: 0x3B23
@scena.Code('func_11_3B23')
def func_11_3B23():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_3BE6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_3B6A',
    )

    ChrTalk(
        0x00FE,
        (
            '罗基克，你好慢啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家都已经\n',
            '去练习了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3BE3')

    def _loc_3B6A(): pass

    label('loc_3B6A')

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '接下来是吹奏部的练习了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '已经到了集合时间了，\n',
            '却还是没几个人来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难得有个亚吉鲁\n',
            '按照规定的时间来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3BE3(): pass

    label('loc_3BE3')

    Jump('loc_3D4B')

    def _loc_3BE6(): pass

    label('loc_3BE6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 1, 0x1221)),
            Expr.Return,
        ),
        'loc_3C93',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_3C3D',
    )

    ChrTalk(
        0x00FE,
        (
            '明天起\n',
            '社团活动又要开始忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大概有很多天\n',
            '不能按时回去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3C90')

    def _loc_3C3D(): pass

    label('loc_3C3D')

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '啊，已经这个时间了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明天起\n',
            '吹奏音乐部会很忙，\n',
            '今天又不能早回去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3C90(): pass

    label('loc_3C90')

    Jump('loc_3D4B')

    def _loc_3C93(): pass

    label('loc_3C93')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 6, 0x121E)),
            Expr.Return,
        ),
        'loc_3D4B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_3CEA',
    )

    ChrTalk(
        0x00FE,
        (
            '和平时的考试\n',
            '简直没有区别啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从早到晚的念书\n',
            '已经够累人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3D4B')

    def _loc_3CEA(): pass

    label('loc_3CEA')

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '奇怪的事情吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯…和平时的考试\n',
            '简直没有区别啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从早到晚的念书\n',
            '已经够累人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3D4B(): pass

    label('loc_3D4B')

    TalkEnd(0x00FE)

    Return()

# id: 0x0012 offset: 0x3D4F
@scena.Code('func_12_3D4F')
def func_12_3D4F():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0404, 6, 0x2026)),
            Expr.Return,
        ),
        'loc_3DD9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3DAD',
    )

    ChrTalk(
        0x00FE,
        (
            '各、各位！\n',
            '请多关照！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽、虽然没有信心，\n',
            '但我会努力等的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    Jump('loc_3DD6')

    def _loc_3DAD(): pass

    label('loc_3DAD')

    ChrTalk(
        0x00FE,
        (
            '虽、虽然没有信心，\n',
            '但我会努力等的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3DD6(): pass

    label('loc_3DD6')

    Jump('loc_3FC0')

    def _loc_3DD9(): pass

    label('loc_3DD9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_3E95',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_3E39',
    )

    ChrTalk(
        0x00FE,
        (
            '啊～但是在放假之前\n',
            '应该可以拿到考试的成绩了吧～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊～真是不想看啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E92')

    def _loc_3E39(): pass

    label('loc_3E39')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，今天的\n',
            '课总算完了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要想着马上就可以放假了，\n',
            '念书也就不那么辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3E92(): pass

    label('loc_3E92')

    Jump('loc_3FC0')

    def _loc_3E95(): pass

    label('loc_3E95')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 1, 0x1221)),
            Expr.Return,
        ),
        'loc_3EE1',
    )

    ChrTalk(
        0x00FE,
        (
            '那么，接下来\n',
            '要做什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '偶尔把房间装饰\n',
            '一下也不错啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3FC0')

    def _loc_3EE1(): pass

    label('loc_3EE1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 6, 0x121E)),
            Expr.Return,
        ),
        'loc_3FC0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_3F44',
    )

    ChrTalk(
        0x00FE,
        (
            '考试结束之后\n',
            '就稍微休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，和妈妈说好了\n',
            '要一起去王都购物呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3FC0')

    def _loc_3F44(): pass

    label('loc_3F44')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '哎？考试期间的\n',
            '奇怪事件吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯…如果是说可爱的东西\n',
            '我倒天天都在找……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但要说奇怪的事情\n',
            '就一点也记不得了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3FC0(): pass

    label('loc_3FC0')

    TalkEnd(0x00FE)

    Return()

# id: 0x0013 offset: 0x3FC4
@scena.Code('func_13_3FC4')
def func_13_3FC4():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 1, 0x1221)),
            Expr.Return,
        ),
        'loc_4076',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_4021',
    )

    ChrTalk(
        0x00FE,
        (
            '哈，学院祭真开心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，下次学院祭之前\n',
            '就享受一下社团活动吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4073')

    def _loc_4021(): pass

    label('loc_4021')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '啊，学院祭真开心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '能再那样和大家一起热闹\n',
            '不知要等到什么时候了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4073(): pass

    label('loc_4073')

    Jump('loc_4128')

    def _loc_4076(): pass

    label('loc_4076')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 6, 0x121E)),
            Expr.Return,
        ),
        'loc_4128',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_40C5',
    )

    ChrTalk(
        0x00FE,
        (
            '终于……\n',
            '考试终于结束了啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊～希望不要\n',
            '不及格啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4128')

    def _loc_40C5(): pass

    label('loc_40C5')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '呼啊啊啊啊～……\n',
            '考试终于结束了啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎？什么？\n',
            '考试中的奇怪事件？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没什么印象了…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4128(): pass

    label('loc_4128')

    TalkEnd(0x00FE)

    Return()

# id: 0x0014 offset: 0x412C
@scena.Code('func_14_412C')
def func_14_412C():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0404, 6, 0x2026)),
            Expr.Return,
        ),
        'loc_422F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_41D0',
    )

    ChrTalk(
        0x0009,
        (
            '#0510211011V#640F没关系，我明白的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510211012V贸然行动的话\n',
            '只会成为你们的累赘呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510211013V#648F总之，就拜托你们把\n',
            '犯人打败了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    Jump('loc_422C')

    def _loc_41D0(): pass

    label('loc_41D0')

    ChrTalk(
        0x0009,
        (
            '#0510211014V#645F都、都说了没问题了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510211015V就算是我，在这种时候\n',
            '也不会乱来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_422C(): pass

    label('loc_422C')

    Jump('loc_43F0')

    def _loc_422F(): pass

    label('loc_422F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_4385',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_42C4',
    )

    ChrTalk(
        0x00FE,
        (
            '#0510211016V#642F不过话说回来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510211017V雪拉扎德姐姐\n',
            '身材还真是棒啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510211018V#645F呼啊～我也好想\n',
            '变成她那样子啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4382')

    def _loc_42C4(): pass

    label('loc_42C4')

    ChrTalk(
        0x00FE,
        (
            '#0510211016V#642F不过话说回来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510211020V阿加特先生\n',
            '还真是强壮啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510211021V#647F虽然柔弱型的美少年也不错，\n',
            '但男人果然还是强壮型最好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510211022V嗯～美学的世界果然深奥…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4382(): pass

    label('loc_4382')

    Jump('loc_43F0')

    def _loc_4385(): pass

    label('loc_4385')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '#0510211023V#640F啊，二位。\n',
            '探听的怎么样啦？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510211024V#648F这边交给我们，\n',
            '学生们就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_43F0(): pass

    label('loc_43F0')

    TalkEnd(0x00FE)

    Return()

# id: 0x0015 offset: 0x43F4
@scena.Code('func_15_43F4')
def func_15_43F4():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_445F',
    )

    ChrTalk(
        0x00FE,
        (
            '#0050211001V#050F没有听别人说过\n',
            '类似的传闻吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050211002V即使是一些微不足道的也可以。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_44C4')

    def _loc_445F(): pass

    label('loc_445F')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '#0050211003V#050F没有什么奇怪的事件吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050211004V只要是感觉在意的事，\n',
            '随便什么也都可以。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_44C4(): pass

    label('loc_44C4')

    TalkEnd(0x00FE)

    Return()

# id: 0x0016 offset: 0x44C8
@scena.Code('func_16_44C8')
def func_16_44C8():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_4531',
    )

    ChrTalk(
        0x00FE,
        (
            '#0030211005V#020F类似的传闻也\n',
            '没有听到过吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030211006V哪怕只是一点小事也没关系哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4596')

    def _loc_4531(): pass

    label('loc_4531')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '#0030211007V#020F没发生什么奇怪的事件吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030211008V只要是感觉在意的事，\n',
            '不管什么都可以。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4596(): pass

    label('loc_4596')

    TalkEnd(0x00FE)

    Return()

# id: 0x0017 offset: 0x459A
@scena.Code('func_17_459A')
def func_17_459A():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_466C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_45FC',
    )

    ChrTalk(
        0x00FE,
        (
            '这次我们班\n',
            '也是斗志十足。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，在考试成绩中\n',
            '应该就可以显现出结果了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4669')

    def _loc_45FC(): pass

    label('loc_45FC')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '好！评分终于结束了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次我们班\n',
            '干得真不错嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在超过碧欧拉老师的班之前\n',
            '还要继续努力才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4669(): pass

    label('loc_4669')

    Jump('loc_4865')

    def _loc_466C(): pass

    label('loc_466C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 1, 0x1221)),
            Expr.Return,
        ),
        'loc_47E4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_4701',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_46BF',
    )

    ChrTalk(
        0x00FE,
        (
            '算了，现在不是想\n',
            '那种事的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还是赶快工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_46FE')

    def _loc_46BF(): pass

    label('loc_46BF')

    ChrTalk(
        0x00FE,
        (
            '话说回来，现在的\n',
            '男孩子还真不错呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还是赶快工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_46FE(): pass

    label('loc_46FE')

    Jump('loc_47E1')

    def _loc_4701(): pass

    label('loc_4701')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_4767',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才来的那个游击士……\n',
            '身材实在很棒呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且如此的招摇，   \n',
            '到底想要干什么啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_47E1')

    def _loc_4767(): pass

    label('loc_4767')

    ChrTalk(
        0x00FE,
        (
            '刚才来的那个游击士……\n',
            '总之真的很有男子气概呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '火红色的头发，\n',
            '还有发达的二头肌…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵呵～还真是吸引人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_47E1(): pass

    label('loc_47E1')

    Jump('loc_4865')

    def _loc_47E4(): pass

    label('loc_47E4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 6, 0x121E)),
            Expr.Return,
        ),
        'loc_4865',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_482E',
    )

    ChrTalk(
        0x00FE,
        (
            '也没有听学生们\n',
            '提起过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没有其它的事情了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4865')

    def _loc_482E(): pass

    label('loc_482E')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '啊、奇怪的事件吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '抱歉，什么也没有呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4865(): pass

    label('loc_4865')

    TalkEnd(0x00FE)

    Return()

# id: 0x0018 offset: 0x4869
@scena.Code('func_18_4869')
def func_18_4869():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_4B3D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0419, 0, 0x20C8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4AEB',
    )

    ChrTurnDirection(0x00FE, 0x0102, 0)

    ChrTalk(
        0x00FE,
        (
            '艾丝蒂尔，约修亚，\n',
            '你们干得太好了啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵呵～不愧是我教导过的孩子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F在学院逗留的时候\n',
            '真是多亏了您的照顾。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '老师教过的课程\n',
            '直到现在都记得很清楚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '连艾丝蒂尔\n',
            '也都非常怀念呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#1004F哎………………………\n',
            '……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1016F………啊、嗯、对！\n',
            '是那样是那样！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    ChrTurnDirection(0x0102, 0x0101, 400)
    Sleep(400)

    ChrTalk(
        0x0102,
        (
            '#1048F（难道……\n',
            '你已经不记得了吗？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#1008F（只、只是一时\n',
            '　想不起来了而已。)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '（突、突然说出\n',
            '　那么久之前的事情…）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀，你们在说什么悄悄话？\n',
            '也让老师听听吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x00FE, 400)

    ChrTalk(
        0x0101,
        (
            '#1016F啊哈哈……\n',
            '没、没说什么啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1052F（真是的……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0419, 0, 0x20C8))

    Jump('loc_4B3A')

    def _loc_4AEB(): pass

    label('loc_4AEB')

    ChrTalk(
        0x00FE,
        (
            '艾丝蒂尔，约修亚，\n',
            '你们干得太好了啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵呵～不愧是我教导过的孩子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4B3A(): pass

    label('loc_4B3A')

    Jump('loc_4EE9')

    def _loc_4B3D(): pass

    label('loc_4B3D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_4C61',
    )

    ChrTurnDirection(0x00FE, 0x0105, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_4BA3',
    )

    ChrTalk(
        0x00FE,
        (
            '假期结束后\n',
            '还要打起精神来学校啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么、希望你们\n',
            '过个有意义的假期。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4C5E')

    def _loc_4BA3(): pass

    label('loc_4BA3')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '啊，科洛丝。\n',
            '我还以为你已经走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '假期结束后\n',
            '一定要打起精神来学校啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好吗？这是约定哦～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F好的，约定了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '碧欧拉老师也要多保重啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，有意义的\n',
            '假期吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4C5E(): pass

    label('loc_4C5E')

    Jump('loc_4EE9')

    def _loc_4C61(): pass

    label('loc_4C61')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 1, 0x1221)),
            Expr.Return,
        ),
        'loc_4D06',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_4CB1',
    )

    ChrTalk(
        0x00FE,
        (
            '考试已经够累人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管学生还是老师\n',
            '都有些睡眠不足。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4D03')

    def _loc_4CB1(): pass

    label('loc_4CB1')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '呜～都已经这个点了，\n',
            '但评分还是没完成。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊～真想早点评完去喝一杯啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4D03(): pass

    label('loc_4D03')

    Jump('loc_4EE9')

    def _loc_4D06(): pass

    label('loc_4D06')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 6, 0x121E)),
            Expr.Return,
        ),
        'loc_4EE9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_4D60',
    )

    ChrTurnDirection(0x00FE, 0x0105, 0)

    ChrTalk(
        0x00FE,
        (
            '积极参加社会活动\n',
            '是好事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请加油吧！\n',
            '老师也会支持你的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4EE9')

    def _loc_4D60(): pass

    label('loc_4D60')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0246, 7, 0x1237)),
            Expr.Return,
        ),
        'loc_4DBE',
    )

    ChrTalk(
        0x00FE,
        (
            '好了～稍微休息了一下，\n',
            '又该回到工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼～不过评分\n',
            '还真是辛苦的工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4EE9')

    def _loc_4DBE(): pass

    label('loc_4DBE')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    SetScenaFlags(ScenaFlag(0x0246, 7, 0x1237))
    ChrTurnDirection(0x00FE, 0x0105, 0)

    ChrTalk(
        0x00FE,
        (
            '啊，科洛丝。\n',
            '有什么问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F不，其实是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '啊，是刚才乔儿\n',
            '说的那件事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听说你们在搜寻\n',
            '可疑的人物…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F嗯～请让我帮忙\n',
            '一起进行调查吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，积极参加社会活动\n',
            '是好事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请加油吧！\n',
            '老师也会支持你的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#041F是，谢谢您。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4EE9(): pass

    label('loc_4EE9')

    TalkEnd(0x00FE)

    Return()

# id: 0x0019 offset: 0x4EED
@scena.Code('func_19_4EED')
def func_19_4EED():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_4FA9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4F65',
    )

    ChrTalk(
        0x00FE,
        (
            '勤务员先生的样子\n',
            '似乎也稳定下来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，没出大事就好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不如过一会儿\n',
            '去看看他吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_4FA6')

    def _loc_4F65(): pass

    label('loc_4F65')

    ChrTalk(
        0x00FE,
        (
            '勤务员先生的样子\n',
            '似乎也稳定下来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，没出大事就好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4FA6(): pass

    label('loc_4FA6')

    Jump('loc_518B')

    def _loc_4FA9(): pass

    label('loc_4FA9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_5027',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_4FDF',
    )

    ChrTalk(
        0x00FE,
        (
            '这次考试\n',
            '大家的成绩都相当好哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5024')

    def _loc_4FDF(): pass

    label('loc_4FDF')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '这次考试\n',
            '大家的成绩都相当好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来学生们\n',
            '也都很努力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5024(): pass

    label('loc_5024')

    Jump('loc_518B')

    def _loc_5027(): pass

    label('loc_5027')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 1, 0x1221)),
            Expr.Return,
        ),
        'loc_50E6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_5082',
    )

    ChrTalk(
        0x00FE,
        (
            '米克本来\n',
            '就是个很用功的学生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唯一的问题就是\n',
            '他那消极的人生观。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_50E3')

    def _loc_5082(): pass

    label('loc_5082')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '呀……？\n',
            '这份考卷…没有写名字啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯～编号是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……嗯，看来是\n',
            '米克的卷子啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_50E3(): pass

    label('loc_50E3')

    Jump('loc_518B')

    def _loc_50E6(): pass

    label('loc_50E6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 6, 0x121E)),
            Expr.Return,
        ),
        'loc_518B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_5140',
    )

    ChrTalk(
        0x00FE,
        (
            '考试结束对学生们来说\n',
            '就好像是无罪释放一样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈～真羡慕他们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_518B')

    def _loc_5140(): pass

    label('loc_5140')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '还没来得及评分的卷子\n',
            '就先收起来好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天就先改到\n',
            '这里吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_518B(): pass

    label('loc_518B')

    TalkEnd(0x00FE)

    Return()

# id: 0x001A offset: 0x518F
@scena.Code('func_1A_518F')
def func_1A_518F():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_5259',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5218',
    )

    ChrTalk(
        0x000B,
        (
            '学生们很快就恢复\n',
            '正常的校园生活了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '刚才的事件好像已经\n',
            '忘得一干二净了一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '呵呵～年轻\n',
            '真是好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_5256')

    def _loc_5218(): pass

    label('loc_5218')

    ChrTalk(
        0x000B,
        (
            '学生们看起来\n',
            '已经完全恢复了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '呵呵～年轻\n',
            '真是好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5256(): pass

    label('loc_5256')

    Jump('loc_5411')

    def _loc_5259(): pass

    label('loc_5259')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0404, 5, 0x2025)),
            Expr.Return,
        ),
        'loc_52AA',
    )

    ChrTalk(
        0x000B,
        (
            '武装的犯人们\n',
            '应该还潜藏在校园里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '各位，无论如何要小心啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5411')

    def _loc_52AA(): pass

    label('loc_52AA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_5349',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_52FD',
    )

    ChrTalk(
        0x000B,
        (
            '校长在不久前\n',
            '外出了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '好像是有什么事，\n',
            '具体就不清楚了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5346')

    def _loc_52FD(): pass

    label('loc_52FD')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x000B,
        (
            '啊，科洛丝。\n',
            '现在已经放假了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '注意身体，\n',
            '好好休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5346(): pass

    label('loc_5346')

    Jump('loc_5411')

    def _loc_5349(): pass

    label('loc_5349')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 2, 0x1222)),
            Expr.Return,
        ),
        'loc_5360',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_535A',
    )

    Jump('loc_535D')

    def _loc_535A(): pass

    label('loc_535A')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_535D(): pass

    label('loc_535D')

    Jump('loc_5411')

    def _loc_5360(): pass

    label('loc_5360')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 1, 0x1221)),
            Expr.Return,
        ),
        'loc_5389',
    )

    ChrTalk(
        0x000B,
        (
            '辛苦了。\n',
            '还在进行调查吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5411')

    def _loc_5389(): pass

    label('loc_5389')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 6, 0x121E)),
            Expr.Return,
        ),
        'loc_5411',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_53C7',
    )

    ChrTalk(
        0x000B,
        (
            '我们已经接到通知了。\n',
            '你们就随意调查吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5411')

    def _loc_53C7(): pass

    label('loc_53C7')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x000B,
        (
            '啊，你们是游击士吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '我们已经接到通知了。\n',
            '你们就随意调查吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5411(): pass

    label('loc_5411')

    TalkEnd(0x000B)

    Return()

# id: 0x001B offset: 0x5415
@scena.Code('func_1B_5415')
def func_1B_5415():
    TalkBegin(0x0008)
    ChrClearFlags(0x0008, 0x0010)
    ChrTurnDirection(0x0008, 0x0000, 0)

    If(
        (
            (Expr.PushLong, 0x1E),
            (Expr.GetChrWork, 0x8, 0x4),
            Expr.Lss,
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0xA0),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5445',
    )

    ChrSetSubChip(0x0008, 1)

    Jump('loc_546B')

    def _loc_5445(): pass

    label('loc_5445')

    If(
        (
            (Expr.PushLong, 0xD2),
            (Expr.GetChrWork, 0x8, 0x4),
            Expr.Lss,
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0x14A),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5466',
    )

    ChrSetSubChip(0x0008, 2)

    Jump('loc_546B')

    def _loc_5466(): pass

    label('loc_5466')

    ChrSetSubChip(0x0008, 0)

    def _loc_546B(): pass

    label('loc_546B')

    ChrSetDirection(0x0008, 180, 0)
    ChrSetFlags(0x0008, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_5845',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041E, 3, 0x20F3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_577D',
    )

    ChrTalk(
        0x0008,
        (
            '#0530361239V#783F艾丝蒂尔、约修亚。\n',
            '这次真是辛苦你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530361240V#780F全靠你们，\n',
            '学生们才能平安获救。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530361241V身为学院的代表，\n',
            '请允许我向你们表示诚挚的谢意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010361242V#1025F能把事情平安解决，\n',
            '我也松了口气。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010361243V学院竟然会遭到袭击，\n',
            '真是做梦也想不到啊…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020361244V#1043F是啊……\n',
            '看来我的想法太天真了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020361245V#1035F在这种状况下，\n',
            '哪里都不是绝对安全的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0530361246V#782F是『结社』吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530361247V这次事件的幕后黑手\n',
            '似乎是一群身份不明的家伙啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530361248V如果没有你们游击士的帮助，\n',
            '这次的危机根本不可能顺利解决。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530361249V为了早日恢复治安，\n',
            '今后大家也要一起加油。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530361250V这也是为了支持一个人在\n',
            '王都努力的科洛丝…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010361251V#1006F嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020361252V#1040F我们会竭尽全力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))
    SetScenaFlags(ScenaFlag(0x041E, 3, 0x20F3))

    Jump('loc_5842')

    def _loc_577D(): pass

    label('loc_577D')

    ChrTalk(
        0x0008,
        (
            '#0530361253V#780F这次事件的幕后黑手\n',
            '似乎是一群身份不明的家伙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530361254V今后也需要你们游击士\n',
            '多多帮忙了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530361255V一天也好，希望能早日恢复治安…\n',
            '在王都的科洛丝\n',
            '也一定是那样希望的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5842(): pass

    label('loc_5842')

    Jump('loc_5C60')

    def _loc_5845(): pass

    label('loc_5845')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0404, 5, 0x2025)),
            Expr.Return,
        ),
        'loc_5978',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5900',
    )

    ChrTalk(
        0x0008,
        (
            '#0530361256V#780F犯人在寻找王室的公主，\n',
            '但却没注意到是科洛丝。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530361257V这样的话，很可能\n',
            '会波及其它的女学生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530361258V抱歉，不过希望\n',
            '诸位能够事先小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    Jump('loc_5975')

    def _loc_5900(): pass

    label('loc_5900')

    ChrTalk(
        0x0008,
        (
            '#0530361259V#780F犯人在搜寻公主的过程中\n',
            '可能会危害到其它女学生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530361260V抱歉，不过希望\n',
            '诸位务必小心行事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5975(): pass

    label('loc_5975')

    Jump('loc_5C60')

    def _loc_5978(): pass

    label('loc_5978')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0244, 1, 0x1221)),
            Expr.Return,
        ),
        'loc_5AB1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_59EA',
    )

    ChrTalk(
        0x0008,
        (
            '#0530211025V#780F最好赶快回到\n',
            '学生会室。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530211026V要是等到天黑之后，\n',
            '就会有很多不便了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5AAE')

    def _loc_59EA(): pass

    label('loc_59EA')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x0008,
        (
            '#0530211027V#780F调查进展得如何了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211028V#040F啊、是的，现在我们\n',
            '要回学生会室了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0530211029V#780F那么，动作快一点吧，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530211030V要是等到天黑之后，\n',
            '调查就难以继续了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5AAE(): pass

    label('loc_5AAE')

    Jump('loc_5C60')

    def _loc_5AB1(): pass

    label('loc_5AB1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 6, 0x121E)),
            Expr.Return,
        ),
        'loc_5C60',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x024C, 4, 0x1264)),
            Expr.Return,
        ),
        'loc_5B30',
    )

    ChrTalk(
        0x0008,
        (
            '#0530211031V#780F要是还有什么需要帮忙的，\n',
            '不要客气，尽管开口就是了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530211032V我们一定会全力协助的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5C60')

    def _loc_5B30(): pass

    label('loc_5B30')

    SetScenaFlags(ScenaFlag(0x024C, 4, 0x1264))

    ChrTalk(
        0x0008,
        (
            '#0530211033V#780F调查好像已经开始了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530211034V科洛丝也\n',
            '开始帮忙了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060211035V#040F是的，毕竟这次的\n',
            '事件关系到我们的校园…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060211036V身为学院的学生，\n',
            '我也想贡献出自己的力量。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0530211037V#780F要是有需要的话，\n',
            '不要客气，尽管开口就是了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530211032V我们一定会全力协助的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5C60(): pass

    label('loc_5C60')

    ChrSetSubChip(0x0008, 0)
    TalkEnd(0x0008)

    Return()

# id: 0x001C offset: 0x5C69
@scena.Code('func_1C_5C69')
def func_1C_5C69():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 0, 0x2028)),
            Expr.Return,
        ),
        'loc_5CF3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 5, 0x15)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5CD9',
    )

    ChrTalk(
        0x00FE,
        (
            '要是有弓箭的话，\n',
            '我也想参加战斗的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里就拜托你们了！\n',
            '加油了！各位游击士！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0002, 5, 0x15))

    Jump('loc_5CF3')

    def _loc_5CD9(): pass

    label('loc_5CD9')

    ChrTalk(
        0x00FE,
        (
            '加油了！各位游击士！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5CF3(): pass

    label('loc_5CF3')

    TalkEnd(0x00FE)

    Return()

# id: 0x001D offset: 0x5CF7
@scena.Code('func_1D_5CF7')
def func_1D_5CF7():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '米克的话果然\n',
            '还是根据结果来下定论的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哼、哼……\n',
            '我才不会感谢呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x001E offset: 0x5D4C
@scena.Code('func_1E_5D4C')
def func_1E_5D4C():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 6, 0x16)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5DF3',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然很想尽快\n',
            '确认小姐的安全…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过现在的当务之急\n',
            '还是解救学院的全体成员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在这里拜托\n',
            '诸位了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……请一定把其它的学生\n',
            '也解救出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0002, 6, 0x16))

    Jump('loc_5E4B')

    def _loc_5DF3(): pass

    label('loc_5DF3')

    ChrTalk(
        0x00FE,
        (
            '现在的当务之急\n',
            '还是解救学院的全体成员……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……请一定把其它的学生\n',
            '也解救出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5E4B(): pass

    label('loc_5E4B')

    TalkEnd(0x00FE)

    Return()

# id: 0x001F offset: 0x5E4F
@scena.Code('func_1F_5E4F')
def func_1F_5E4F():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0404, 6, 0x2026)),
            Expr.Return,
        ),
        'loc_5EBE',
    )

    ChrTalk(
        0x000A,
        (
            '#0520360917V#732F那么，\n',
            '等事情解决之后再来吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520360918V艾丝蒂尔，约修亚……\n',
            '路上要小心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5EBE(): pass

    label('loc_5EBE')

    TalkEnd(0x00FE)

    Return()

# id: 0x0020 offset: 0x5EC2
@scena.Code('func_20_5EC2')
def func_20_5EC2():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_5FAF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 3, 0x13)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5F6A',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，各位游击士。\n',
            '刚才真是谢谢大家了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '能把事情平安解决\n',
            '真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然接下来还有不少困难，\n',
            '但只要大家一起努力\n',
            '就一定能克服的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0002, 3, 0x13))

    Jump('loc_5FAC')

    def _loc_5F6A(): pass

    label('loc_5F6A')

    ChrTalk(
        0x00FE,
        (
            '各位游击士。\n',
            '今天谢谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '能把事情平安解决\n',
            '真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5FAC(): pass

    label('loc_5FAC')

    Jump('loc_5FFE')

    def _loc_5FAF(): pass

    label('loc_5FAF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0404, 6, 0x2026)),
            Expr.Return,
        ),
        'loc_5FFE',
    )

    ChrTalk(
        0x00FE,
        (
            '呼嗯……\n',
            '拜托饶了我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那些家伙为什么\n',
            '要做出这么过分的事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5FFE(): pass

    label('loc_5FFE')

    TalkEnd(0x00FE)

    Return()

# id: 0x0021 offset: 0x6002
@scena.Code('func_21_6002')
def func_21_6002():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_618B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0218, 0, 0x10C0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6122',
    )

    ChrTalk(
        0x00FE,
        (
            '艾丝蒂尔，约修亚。\n',
            '真是谢谢你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然不是什么值钱的东西，\n',
            '但还是请你们收下。',
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
            (TxtCtl.Item, ItemTable['牌技师杰克 12卷']),
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
    AddItem(ItemTable['牌技师杰克 12卷'], 1)
    SetScenaFlags(ScenaFlag(0x0218, 0, 0x10C0))
    OP_0D()

    ChrTalk(
        0x00FE,
        (
            '以后有空的话，把这次的事件\n',
            '写成小说应该也不错吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过这个想法，\n',
            '也得等到恢复正常生活才行…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6188')

    def _loc_6122(): pass

    label('loc_6122')

    ChrTalk(
        0x00FE,
        (
            '以后有空的话，把这次的事件\n',
            '写成小说应该也不错吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过这个想法，\n',
            '也得等到恢复正常生活才行…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6188(): pass

    label('loc_6188')

    Jump('loc_61F6')

    def _loc_618B(): pass

    label('loc_618B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0404, 6, 0x2026)),
            Expr.Return,
        ),
        'loc_61F6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 4, 0x14)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_61D9',
    )

    ChrTalk(
        0x00FE,
        (
            '我们就在这里\n',
            '等着你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '各位，你们要小心啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0002, 4, 0x14))

    Jump('loc_61F6')

    def _loc_61D9(): pass

    label('loc_61D9')

    ChrTalk(
        0x00FE,
        (
            '我们就在这里\n',
            '待机不动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_61F6(): pass

    label('loc_61F6')

    TalkEnd(0x00FE)

    Return()

# id: 0x0022 offset: 0x61FA
@scena.Code('func_22_61FA')
def func_22_61FA():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_620B',
    )

    Call(0, 0x0051)

    def _loc_620B(): pass

    label('loc_620B')

    EventBegin(0x00)
    MapClearFlags(0x00000001)
    OP_4A(0x0009, 255)
    OP_4A(0x000A, 255)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetPos(0x0101, 116390, 0, 2740, 0)
    ChrSetPos(0x00F7, 115500, 0, 2730, 0)
    ChrSetPos(0x0105, 117550, 0, 3240, 270)
    ChrSetPos(0x0104, 116430, 0, 1630, 0)
    ChrSetPos(0x0127, 115580, 0, 1650, 0)
    ChrSetPos(0x0009, 117660, 0, 4320, 270)
    ChrSetPos(0x000A, 118370, 0, 3940, 270)
    CameraMove(116710, 0, 460, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    CameraMove(116480, 0, 3910, 2000)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0530210820V#783F#5P原来如此，我明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530210821V#780F你们是为了搜索\n',
            '在卢安各处出没的『白影』\n',
            '而到学院来调查的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210822V#1002F#4P对，就是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_6413',
    )

    ChrTalk(
        0x0106,
        (
            '#0050210823V#050F#6P协会派我们到\n',
            '学院来进行调查。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050210824V调查时大概要向学生们进行询问，\n',
            '您可以准许吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6487')

    def _loc_6413(): pass

    label('loc_6413')

    ChrTalk(
        0x0103,
        (
            '#0030210825V#020F#6P协会派我们到\n',
            '学院中进行调查……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030210826V并且还要对学生们进行一些询问，\n',
            '您可以准许吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6487(): pass

    label('loc_6487')

    ChrTalk(
        0x0008,
        (
            '#0530210827V#782F#5P不不，其实这件事\n',
            '我本来也是要拜托你们的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530210828V虽然不知道那个『白影』\n',
            '究竟是什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530210829V但恐怕会影响到选举，\n',
            '因此不能放任不管。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210830V#1016F#4P呼……\n',
            '非常感谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010210831V#1015F那么，在校园里有没有关于『白影』的\n',
            '古怪的传闻呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0530210832V#780F#5P没有……\n',
            '我没有听到任何有关的报告。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530210833V你们学生会那里呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0510210834V#645F#2P嗯……我们也没有\n',
            '听到这方面的消息呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510210835V#640F不过，毕竟现在\n',
            '是考试期间。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510210836V有可能是大家没空来\n',
            '这里商谈吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0530210837V#782F#5P原来如此……有这种可能。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 45, 400)

    @scena.Lambda('lambda_66D9')
    def lambda_66D9():
        ChrSetDirection(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_66D9)

    Sleep(50)

    @scena.Lambda('lambda_66EC')
    def lambda_66EC():
        ChrSetDirection(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_66EC)

    Sleep(50)

    @scena.Lambda('lambda_66FF')
    def lambda_66FF():
        ChrSetDirection(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x0127, 0x0001, lambda_66FF)

    ChrTalk(
        0x0101,
        (
            '#0010210838V#1004F#6P嗯？怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060210839V#542F#2P王立学院的定期测试\n',
            '是关系到能否晋级的重要考试…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060210840V所以就算真有学生看见了那些东西，\n',
            '也只能暂且不作考虑，\n',
            '集中精力准备考试。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0520210841V#734F#2P如果是我的话也会这样的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520210842V比其那些虚无缥缈的幻觉，\n',
            '我宁愿花时间\n',
            '背几条算式。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210843V#1007F#6P哎哎～……\n',
            '是这么回事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0127,
        (
            '#0280210844V#153F#6P啊～最近的学生\n',
            '还真是爱用功啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0520210845V#732F#2P不过，考试就在今天结束，\n',
            '大家也算是彻底解放了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520210846V如果有奇怪传闻的话，\n',
            '从今天开始应该就会流传开了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040210847V#035F#4P这种东西一旦广泛流传成了校园怪谈，\n',
            '真实性恐怕就会大大降低……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040210848V#030F因此现在正是直接寻找目击者\n',
            '进行询问的最好时机。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0530210849V#780F#5P唔，那你们就赶快\n',
            '在校园中进行调查吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530210850V乔儿、汉斯、\n',
            '还有科洛丝，你们也一起帮忙吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060210851V#041F#2P是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0520210852V#730F#2P明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0009, 225, 400)

    ChrTalk(
        0x0009,
        (
            '#0510210853V#644F#5P那么，要调查的话\n',
            '我们最好先找个集合的据点。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510210854V说不定会得到什么情报，\n',
            '就定在学生会室吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010210855V#1006F#6PＴＨＡＮＫ　ＹＯＵ～真是帮了大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(500)

    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T2511._SN', 108, 0, 0)
    IdleLoop()

    Return()

# id: 0x0023 offset: 0x6B68
@scena.Code('func_23_6B68')
def func_23_6B68():
    EventBegin(0x00)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x001F, 115970, 0, 2750, 0)
    ChrClearFlags(0x001F, 0x0080)
    CameraMove(116530, 0, 4170, 0)
    OP_67(0, 5950, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0530360607V#782F#5P基尔巴特……\n',
            '这到底是怎么回事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530360608V你为什么要做出这样的事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '#0480360609V#1226F#4P哼哼……目的有２个。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480360610V#1220F第一，我已接到上级的指示，\n',
            '要在全国范围内造成\n',
            '更大的混乱。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480360611V有情有义的我自然要选择\n',
            '深切怀念的母校作为舞台。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0530360612V#783F#5P……你变了，基尔巴特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530360613V#782F学生时代的你是那么\n',
            '坚定地追求自己的政治之道……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530360614V当初的那些热情和信念，\n',
            '难道都已经丢掉了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '#0480360615V#1221F#4P理想终究只是理想，\n',
            '现实可是无比丑陋的啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480360616V米拉和权利就是一切……\n',
            '这是担任戴尔蒙市长的秘书时，\n',
            '我所悟出的道理。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480360617V#1226F本想找机会把那市长整下台，\n',
            '然后自己坐上他的位子……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480360618V谁知道突然冒出了那群游击士，\n',
            '把我的计划全盘打乱了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480360619V#1220F不过无所谓了，现在的我\n',
            '已经用另一种方式将权利握在手中了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0530360620V#783F#5P你太愚蠢了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '#0480360621V#1226F#4P哼哼哼……\n',
            '随你怎么说吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480360622V#1221F至于我的另一个目的……\n',
            '那就是利贝尔王室的公主了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0530360623V#782F#5P！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '#0480360624V#1221F#4P听说她也是\n',
            '这所学院的学生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480360625V只是还不知道究竟是哪个学生，\n',
            '您能告诉我吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0530360626V#783F#5P……你到底在说什么？\n',
            '我一点也听不懂。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530360627V#782F我可以明确地告诉你……\n',
            '学院中根本就没有\n',
            '你说的那个人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530360628V你的情报似乎有误啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001F,
        (
            '#0480360629V#1221F#4P哈哈，想把我当成\n',
            '傻瓜一样愚弄过去吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480360630V#1226F算了，反正还有的是时间，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0480360631V我自己慢慢找就是了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0530360632V#782F#5P嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021F, 6, 0x10FE))
    SetScenaFlags(ScenaFlag(0x021E, 5, 0x10F5))
    NewScene('ED6_DT21/T2500._SN', 129, 0, 0)
    IdleLoop()

    Return()

# id: 0x0024 offset: 0x71A9
@scena.Code('func_24_71A9')
def func_24_71A9():
    EventBegin(0x00)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    CameraMove(87050, 0, 7080, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_7206')
    def lambda_7206():
        CameraMove(86660, 0, 2460, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_7206)

    OP_67(0, 6180, -10000, 3000)
    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021F, 6, 0x10FE))
    SetScenaFlags(ScenaFlag(0x021E, 6, 0x10F6))
    NewScene('ED6_DT21/T2500._SN', 129, 0, 0)
    IdleLoop()

    Return()

# id: 0x0025 offset: 0x7249
@scena.Code('func_25_7249')
def func_25_7249():
    EventBegin(0x00)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x001A, 0x0080)
    CameraMove(41510, -250, -3520, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    CameraMove(41760, 0, 9240, 4000)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021F, 6, 0x10FE))
    SetScenaFlags(ScenaFlag(0x021E, 7, 0x10F7))
    NewScene('ED6_DT21/T2500._SN', 129, 0, 0)
    IdleLoop()

    Return()

# id: 0x0026 offset: 0x72D1
@scena.Code('func_26_72D1')
def func_26_72D1():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    ChrSetFlags(0x0102, 0x0080)
    OP_4A(0x000A, 255)
    OP_4A(0x0009, 255)
    OP_4A(0x0020, 255)
    OP_4A(0x0012, 255)
    OP_4A(0x0021, 255)
    ChrSetPos(0x000A, 3470, 0, 2580, 180)
    ChrSetPos(0x0009, 3500, 0, 1470, 0)
    ChrSetPos(0x0020, -240, 0, 3050, 180)
    ChrSetPos(0x0012, -650, 0, 2060, 90)
    ChrSetPos(0x0021, 350, 0, 1140, 0)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x0020, 0x0080)
    ChrClearFlags(0x0021, 0x0080)
    CameraMove(-3290, 0, 2710, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    @scena.Lambda('lambda_73A2')
    def lambda_73A2():
        CameraMove(4140, 0, 2560, 3000)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_73A2)

    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x000A, 0x0000)
    PlaySE(113, 0x00, 0x5F)
    Sleep(1000)

    OP_62(0x000A, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '#0520360642V#732F#5P什么……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0510360643V#642F#4P刚才……\n',
            '好像有什么声音？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(113, 0x00, 0x5F)
    Sleep(1000)

    OP_62(0x000A, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrSetDirection(0x000A, 0, 400)

    ChrTalk(
        0x000A,
        (
            '#0520360644V#732F#4P……是这边吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x000A, 0x0001)

    @scena.Lambda('lambda_74B2')
    def lambda_74B2():
        ChrTurnDirection(0x00FE, 0x000A, 400)
        Yield()

        Jump('lambda_74B2')

    DispatchAsync2(0x0009, 0x0001, lambda_74B2)

    Sleep(100)

    @scena.Lambda('lambda_74C8')
    def lambda_74C8():
        CameraMove(2420, 0, 5620, 2500)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_74C8)

    ChrWalkTo(0x000A, 2080, 0, 5500, 2000, 0x00)
    ChrSetDirection(0x000A, 0, 400)
    WaitForThreadExit(0x0102, 0x0001)
    Sleep(500)

    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '#0520360645V#733F#4P什……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x021F, 6, 0x10FE))
    SetScenaFlags(ScenaFlag(0x021F, 0, 0x10F8))
    NewScene('ED6_DT21/T2500._SN', 128, 0, 0)
    IdleLoop()

    Return()

# id: 0x0027 offset: 0x754D
@scena.Code('func_27_754D')
def func_27_754D():
    EventBegin(0x00)
    ChrSetFlags(0x0102, 0x0080)
    LoadChip('ED6_DT07/CH02550._CH', 'ED6_DT07/CH02550P._CP', 27)
    OP_4A(0x000A, 255)
    OP_4A(0x0009, 255)
    OP_4A(0x0020, 255)
    OP_4A(0x0012, 255)
    OP_4A(0x0021, 255)
    ChrSetPos(0x000A, 2080, 0, 5500, 0)
    ChrSetPos(0x0009, 2600, 0, 4850, 0)
    ChrSetPos(0x0020, -240, 0, 3050, 180)
    ChrSetPos(0x0012, -650, 0, 2060, 90)
    ChrSetPos(0x0021, 350, 0, 1140, 0)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x0020, 0x0080)
    ChrClearFlags(0x0021, 0x0080)
    CameraMove(2170, 0, 5050, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    @scena.Lambda('lambda_761E')
    def lambda_761E():
        ChrMoveTo(0x00FE, 1870, 0, 5600, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_761E)

    Sleep(100)

    ChrMoveTo(0x000A, 1200, 0, 5650, 1000, 0x00)
    ChrSetDirection(0x000A, 45, 400)
    WaitForThreadExit(0x0009, 0x0001)

    ChrTalk(
        0x0009,
        (
            '#0510360652V#646F#2P（安静些，汉斯……\n',
            '  窗外边有人吗？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0520360653V#732F#6P（喂、不要推。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520360654V#730F（那个……\n',
            '  绝对不要大声叫啊？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000A, 45, 400)

    @scena.Lambda('lambda_7702')
    def lambda_7702():
        ChrMoveTo(0x00FE, 2430, 0, 5380, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_7702)

    Sleep(50)

    ChrMoveTo(0x000A, 1750, 0, 5460, 1000, 0x00)
    ChrSetDirection(0x000A, 0, 400)
    WaitForThreadExit(0x0009, 0x0001)

    ChrTalk(
        0x0009,
        (
            '#0510360655V#644F#2P（好啦好啦。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510360656V（我堂堂学生会长乔儿大人\n',
            '  怎么可能因为这些琐碎小事\n',
            '  而大声尖叫呢……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0009, 0x0001)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetDirection(0x000A, 45, 400)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '汉斯捂住了乔儿的嘴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0009,
        (
            '#0510360657V#643F#4S#2P（～～～呜！！！）',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x021F, 6, 0x10FE))
    SetScenaFlags(ScenaFlag(0x021F, 1, 0x10F9))
    NewScene('ED6_DT21/T2500._SN', 128, 0, 0)
    IdleLoop()

    Return()

# id: 0x0028 offset: 0x7875
@scena.Code('func_28_7875')
def func_28_7875():
    EventBegin(0x00)
    ChrSetFlags(0x0102, 0x0080)
    OP_4A(0x000A, 255)
    OP_4A(0x0009, 255)
    OP_4A(0x0020, 255)
    OP_4A(0x0012, 255)
    OP_4A(0x0021, 255)
    ChrSetPos(0x000A, 1750, 0, 5460, 0)
    ChrSetPos(0x0009, 2430, 0, 5380, 0)
    ChrSetPos(0x0020, -240, 0, 3050, 180)
    ChrSetPos(0x0012, -650, 0, 2060, 90)
    ChrSetPos(0x0021, 350, 0, 1140, 0)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x0020, 0x0080)
    ChrClearFlags(0x0021, 0x0080)
    CameraMove(2170, 0, 5050, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0520360663V#730F#6P（原来如此……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520360664V（总之就是为了解放学院\n',
            '  而来这里作战的啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(70, 0, -1, -1)
    TalkSetChrName('约修亚')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0020360665V#1040F（就是这样。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360666V（请把这消息告诉给大家吧，\n',
            '  这样可以让大家安心些。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ChrTalk(
        0x0009,
        (
            '#0510360667V#644F#4P（是吗，那可得救了。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510360668V（有没有什么\n',
            '　我们可以帮得上忙的？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(70, 0, -1, -1)
    TalkSetChrName('约修亚')

    Talk(
        (
            '#0020360669V#1043F（这样吗……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360670V#1042F（我想要一份学院内\n',
            ' 　所有学生和职员的名单。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360671V（这样在救助时就会心中有数了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ChrTalk(
        0x0009,
        (
            '#0510360672V#647F#4P（原来如此。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0520360673V#730F#6P（ＯＫ。\n',
            '　等我写给你。）',
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
            '乔儿和汉斯把记有学院中\n',
            '学生和职员名单的笔记本\n',
            '从窗缝中交给了约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '笔记本上写有全部人质的名单。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_28(0x00C1, 0x04, 0x02)
    OP_28(0x00C1, 0x04, 0x08)
    OP_28(0x00C1, 0x01, 0x0001)
    OP_28(0x00C1, 0x01, 0x0004)
    OP_28(0x00C1, 0x01, 0x0010)
    OP_28(0x00C1, 0x01, 0x0040)
    OP_28(0x00C1, 0x01, 0x0100)
    OP_28(0x00C1, 0x01, 0x0400)
    OP_28(0x00C1, 0x01, 0x1000)
    OP_28(0x00C1, 0x01, 0x4000)
    SetMessageWindowPos(70, 0, -1, -1)
    TalkSetChrName('约修亚')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0020360674V#1053F（……谢了。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360675V#1040F（再过不久，\n',
            '　我们就会开始正式行动。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360676V（在那之前，请大家先忍耐一阵。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ChrTalk(
        0x0009,
        (
            '#0510360677V#644F#4P（嗯嗯、明白了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0520360678V#732F#6P（倒是你们，\n',
            '　一定要小心行事啊！）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520360679V#734F（还有啊……等事情解决以后，\n',
            '　一起去食堂吃饭如何？）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520360680V#730F（我可还有一大堆事情\n',
            '　想要审问你这小子呢！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(70, 0, -1, -1)
    TalkSetChrName('约修亚')

    Talk(
        (
            '#0020360681V#1054F（哈哈……明白了。\n',
            '　到时一定还请手下留情啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021F, 6, 0x10FE))
    SetScenaFlags(ScenaFlag(0x021F, 2, 0x10FA))
    NewScene('ED6_DT21/T2500._SN', 128, 0, 0)
    IdleLoop()

    Return()

# id: 0x0029 offset: 0x7E52
@scena.Code('func_29_7E52')
def func_29_7E52():
    Call(0, 0x002A)
    Call(0, 0x002B)

    Return()

# id: 0x002A offset: 0x7E5B
@scena.Code('func_2A_7E5B')
def func_2A_7E5B():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    LoadChip('ED6_DT27/CH04621._CH', 'ED6_DT27/CH04621P._CP', 27)
    LoadChip('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP', 28)
    LoadChip('ED6_DT27/CH04001._CH', 'ED6_DT27/CH04001P._CP', 29)
    LoadChip('ED6_DT27/CH04010._CH', 'ED6_DT27/CH04010P._CP', 30)
    LoadChip('ED6_DT27/CH04011._CH', 'ED6_DT27/CH04011P._CP', 31)
    LoadChip('ED6_DT07/CH00420._CH', 'ED6_DT07/CH00420P._CP', 32)
    LoadChip('ED6_DT07/CH00421._CH', 'ED6_DT07/CH00421P._CP', 33)
    LoadChip('ED6_DT07/CH00410._CH', 'ED6_DT07/CH00410P._CP', 34)
    LoadChip('ED6_DT07/CH00411._CH', 'ED6_DT07/CH00411P._CP', 35)
    LoadChip('ED6_DT26/CH20209._CH', 'ED6_DT26/CH20209P._CP', 36)
    LoadChip('ED6_DT26/CH20208._CH', 'ED6_DT26/CH20208P._CP', 37)
    LoadChip('ED6_DT27/CH04611._CH', 'ED6_DT27/CH04611P._CP', 38)
    LoadChip('ED6_DT27/CH04620._CH', 'ED6_DT27/CH04620P._CP', 39)
    LoadChip('ED6_DT27/CH04610._CH', 'ED6_DT27/CH04610P._CP', 40)
    ChrSetPos(0x0101, 59470, 0, -750, 270)
    ChrSetPos(0x0102, 59520, 0, 670, 270)
    ChrSetPos(0x010A, 60580, 0, -780, 270)
    ChrSetPos(0x010E, 60740, 0, 980, 270)
    CameraMove(61210, 0, 1040, 0)
    OP_67(0, 5170, -10000, 0)
    CameraSetDistance(2070, 0)
    OP_6C(45000, 0)
    OP_6E(388, 0)
    ChrSetPos(0x0022, 50890, 0, 160, 0)
    ChrSetPos(0x0023, 46610, 0, -730, 90)
    ChrClearFlags(0x0023, 0x0080)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0022,
        (
            '#4210360856V#2P你们是……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x010A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x010E, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetPos(0x0022, 46610, 0, 600, 90)
    ChrClearFlags(0x0022, 0x0080)

    @scena.Lambda('lambda_8054')
    def lambda_8054():
        CameraMove(57420, 0, 710, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_8054)

    @scena.Lambda('lambda_806C')
    def lambda_806C():
        OP_67(0, 6150, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_806C)

    @scena.Lambda('lambda_8084')
    def lambda_8084():
        CameraSetDistance(1560, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_8084)

    @scena.Lambda('lambda_8094')
    def lambda_8094():
        OP_6E(530, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_8094)

    ChrSetChipByIndex(0x0022, 27)
    ChrSetFlags(0x0022, 0x1000)

    @scena.Lambda('lambda_80AE')
    def lambda_80AE():
        ChrWalkTo(0x00FE, 52890, 0, 600, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_80AE)

    Sleep(100)

    ChrSetChipByIndex(0x0023, 38)
    ChrSetFlags(0x0023, 0x1000)

    @scena.Lambda('lambda_80D8')
    def lambda_80D8():
        ChrWalkTo(0x00FE, 52890, 0, -730, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0023, 0x0001, lambda_80D8)

    WaitForThreadExit(0x0022, 0x0001)
    ChrSetChipByIndex(0x0022, 39)
    WaitForThreadExit(0x0023, 0x0001)
    ChrSetChipByIndex(0x0023, 40)
    WaitForThreadExit(0x0023, 0x0001)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(300)

    ChrTalk(
        0x0022,
        (
            '#4210360857V#6P游、游击士吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0101, 28)
    ChrSetChipByIndex(0x0102, 30)
    ChrSetChipByIndex(0x010A, 32)
    ChrSetChipByIndex(0x010E, 34)
    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x0102, 0)
    ChrSetSubChip(0x010A, 0)
    ChrSetSubChip(0x010E, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010360858V#1005F#2P要来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360859V#1042F#5P……解决他们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_81C4')
    def lambda_81C4():
        CameraMove(57500, 0, 830, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_81C4)

    @scena.Lambda('lambda_81DC')
    def lambda_81DC():
        CameraSetDistance(1300, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_81DC)

    @scena.Lambda('lambda_81EC')
    def lambda_81EC():
        ChrMoveToRelative(0x00FE, -3000, 0, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_81EC)

    Sleep(30)

    @scena.Lambda('lambda_820C')
    def lambda_820C():
        ChrMoveToRelative(0x00FE, -3000, 0, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_820C)

    Sleep(30)

    ChrSetChipByIndex(0x0022, 27)
    ChrSetFlags(0x0022, 0x1000)

    @scena.Lambda('lambda_8236')
    def lambda_8236():
        ChrMoveToRelative(0x00FE, 3000, 0, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_8236)

    @scena.Lambda('lambda_8251')
    def lambda_8251():
        ChrMoveToRelative(0x00FE, -3000, 0, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_8251)

    Sleep(30)

    @scena.Lambda('lambda_8271')
    def lambda_8271():
        ChrMoveToRelative(0x00FE, -3000, 0, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x010E, 0x0001, lambda_8271)

    ChrSetChipByIndex(0x0023, 38)
    ChrSetFlags(0x0023, 0x1000)

    @scena.Lambda('lambda_8296')
    def lambda_8296():
        ChrMoveToRelative(0x00FE, 3000, 0, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0023, 0x0001, lambda_8296)

    WaitForThreadExit(0x0101, 0x0002)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x010A, 0xFF)
    TerminateThread(0x010E, 0xFF)
    TerminateThread(0x0022, 0xFF)
    TerminateThread(0x0023, 0xFF)
    Battle(0x0000079D, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_82E1'),
        (-1, 'loc_82E6'),
    )

    def _loc_82E1(): pass

    label('loc_82E1')

    OP_B4(0x00)

    Jump('loc_82E6')

    def _loc_82E6(): pass

    label('loc_82E6')

    Return()

# id: 0x002B offset: 0x82E7
@scena.Code('func_2B_82E7')
def func_2B_82E7():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    ChrSetFlags(0x0022, 0x0080)
    ChrSetFlags(0x0023, 0x0080)
    TerminateThread(0x0022, 0x00)
    TerminateThread(0x0023, 0x00)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x010A, 0x01)
    TerminateThread(0x010E, 0x01)
    TerminateThread(0x0102, 0x01)
    Sleep(500)

    CameraMove(57200, 0, 140, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrClearFlags(0x0022, 0x0080)
    ChrClearFlags(0x0023, 0x0080)
    ChrSetPos(0x0022, 54400, 0, 970, 90)
    ChrSetPos(0x0023, 55400, 0, -1460, 90)
    ChrClearFlags(0x0000, 0x0080)
    ChrClearFlags(0x0001, 0x0080)
    ChrClearFlags(0x0002, 0x0080)
    ChrClearFlags(0x0003, 0x0080)
    ChrSetPos(0x0000, 57200, 0, 140, 270)
    ChrSetPos(0x0001, 57200, 0, 140, 270)
    ChrSetPos(0x0002, 57200, 0, 140, 270)
    ChrSetPos(0x0003, 57200, 0, 140, 270)
    OP_69(0x0000, 0)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x010A, 65535)
    ChrSetChipByIndex(0x010E, 65535)
    ChrClearFlags(0x0022, 0x0001)
    ChrSetFlags(0x0022, 0x0002)
    ChrSetChipByIndex(0x0022, 26)
    ChrSetSubChip(0x0022, 9)
    ChrClearFlags(0x0023, 0x0001)
    ChrSetFlags(0x0023, 0x0002)
    ChrSetChipByIndex(0x0023, 26)
    ChrSetSubChip(0x0023, 12)
    SetScenaFlags(ScenaFlag(0x0404, 4, 0x2024))
    SetScenaFlags(ScenaFlag(0x0417, 0, 0x20B8))
    OP_72(0x0000, 0x0800)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 0)
    OP_73(0x0000)
    OP_71(0x0000, 0x0800)
    OP_72(0x0000, 0x0002)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

# id: 0x002C offset: 0x846E
@scena.Code('func_2C_846E')
def func_2C_846E():
    Call(0, 0x002D)
    Call(0, 0x002E)

    Return()

# id: 0x002D offset: 0x8477
@scena.Code('func_2D_8477')
def func_2D_8477():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    LoadChip('ED6_DT27/CH04621._CH', 'ED6_DT27/CH04621P._CP', 27)
    LoadChip('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP', 28)
    LoadChip('ED6_DT27/CH04001._CH', 'ED6_DT27/CH04001P._CP', 29)
    LoadChip('ED6_DT27/CH04010._CH', 'ED6_DT27/CH04010P._CP', 30)
    LoadChip('ED6_DT27/CH04011._CH', 'ED6_DT27/CH04011P._CP', 31)
    LoadChip('ED6_DT07/CH00420._CH', 'ED6_DT07/CH00420P._CP', 32)
    LoadChip('ED6_DT07/CH00421._CH', 'ED6_DT07/CH00421P._CP', 33)
    LoadChip('ED6_DT07/CH00410._CH', 'ED6_DT07/CH00410P._CP', 34)
    LoadChip('ED6_DT07/CH00411._CH', 'ED6_DT07/CH00411P._CP', 35)
    LoadChip('ED6_DT26/CH20209._CH', 'ED6_DT26/CH20209P._CP', 36)
    LoadChip('ED6_DT26/CH20208._CH', 'ED6_DT26/CH20208P._CP', 37)
    LoadChip('ED6_DT27/CH04611._CH', 'ED6_DT27/CH04611P._CP', 38)
    LoadChip('ED6_DT27/CH04620._CH', 'ED6_DT27/CH04620P._CP', 39)
    LoadChip('ED6_DT27/CH04610._CH', 'ED6_DT27/CH04610P._CP', 40)
    ChrSetPos(0x0101, 24400, 0, -750, 90)
    ChrSetPos(0x0102, 24400, 0, 540, 90)
    ChrSetPos(0x010A, 22950, 0, -1000, 90)
    ChrSetPos(0x010E, 22950, 0, 390, 90)
    CameraMove(24680, 0, 950, 0)
    OP_67(0, 5520, -10000, 0)
    CameraSetDistance(2500, 0)
    OP_6C(45000, 0)
    OP_6E(301, 0)
    ChrSetPos(0x0022, 36490, 0, 600, 270)
    ChrSetPos(0x0023, 36490, 0, -730, 270)
    ChrClearFlags(0x0022, 0x0080)
    ChrClearFlags(0x0023, 0x0080)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0022,
        (
            '#4210360860V你们……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x010A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x010E, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_865A')
    def lambda_865A():
        CameraMove(27430, 0, 790, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_865A)

    @scena.Lambda('lambda_8672')
    def lambda_8672():
        CameraSetDistance(2050, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_8672)

    @scena.Lambda('lambda_8682')
    def lambda_8682():
        OP_6E(416, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_8682)

    ChrSetChipByIndex(0x0022, 27)

    @scena.Lambda('lambda_8697')
    def lambda_8697():
        ChrWalkTo(0x00FE, 30210, 0, 600, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_8697)

    Sleep(100)

    ChrSetChipByIndex(0x0023, 38)

    @scena.Lambda('lambda_86BC')
    def lambda_86BC():
        ChrWalkTo(0x00FE, 30210, 0, -730, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0023, 0x0001, lambda_86BC)

    WaitForThreadExit(0x0022, 0x0001)
    ChrSetChipByIndex(0x0022, 39)
    WaitForThreadExit(0x0023, 0x0001)
    ChrSetChipByIndex(0x0023, 40)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0023,
        (
            '#4220360861V#2P游、游击士吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0101, 28)
    ChrSetChipByIndex(0x0102, 30)
    ChrSetChipByIndex(0x010A, 32)
    ChrSetChipByIndex(0x010E, 34)
    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x0102, 0)
    ChrSetSubChip(0x010A, 0)
    ChrSetSubChip(0x010E, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010360862V#1005F#6P要来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360863V#1042F#6P……解决他们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_879E')
    def lambda_879E():
        CameraMove(27140, 0, 340, 250)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_879E)

    @scena.Lambda('lambda_87B6')
    def lambda_87B6():
        CameraSetDistance(1800, 250)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_87B6)

    @scena.Lambda('lambda_87C6')
    def lambda_87C6():
        ChrMoveToRelative(0x00FE, 2500, 0, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_87C6)

    Sleep(30)

    @scena.Lambda('lambda_87E6')
    def lambda_87E6():
        ChrMoveToRelative(0x00FE, 2500, 0, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_87E6)

    Sleep(30)

    ChrSetChipByIndex(0x0022, 27)
    ChrSetFlags(0x0022, 0x1000)

    @scena.Lambda('lambda_8810')
    def lambda_8810():
        ChrMoveToRelative(0x00FE, -2500, 0, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_8810)

    @scena.Lambda('lambda_882B')
    def lambda_882B():
        ChrMoveToRelative(0x00FE, 2500, 0, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_882B)

    Sleep(30)

    @scena.Lambda('lambda_884B')
    def lambda_884B():
        ChrMoveToRelative(0x00FE, 2500, 0, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x010E, 0x0001, lambda_884B)

    ChrSetChipByIndex(0x0023, 38)
    ChrSetFlags(0x0023, 0x1000)

    @scena.Lambda('lambda_8870')
    def lambda_8870():
        ChrMoveToRelative(0x00FE, -2500, 0, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0023, 0x0001, lambda_8870)

    WaitForThreadExit(0x0101, 0x0002)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x010A, 0xFF)
    TerminateThread(0x010E, 0xFF)
    TerminateThread(0x0022, 0xFF)
    TerminateThread(0x0023, 0xFF)
    Battle(0x0000079D, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_88BB'),
        (-1, 'loc_88C0'),
    )

    def _loc_88BB(): pass

    label('loc_88BB')

    OP_B4(0x00)

    Jump('loc_88C0')

    def _loc_88C0(): pass

    label('loc_88C0')

    Return()

# id: 0x002E offset: 0x88C1
@scena.Code('func_2E_88C1')
def func_2E_88C1():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    ChrSetFlags(0x0022, 0x0080)
    ChrSetFlags(0x0023, 0x0080)
    TerminateThread(0x0022, 0x00)
    TerminateThread(0x0023, 0x00)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x010A, 0x01)
    TerminateThread(0x010E, 0x01)
    TerminateThread(0x0102, 0x01)
    Sleep(500)

    CameraMove(28050, 0, -20, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrClearFlags(0x0022, 0x0080)
    ChrClearFlags(0x0023, 0x0080)
    ChrSetPos(0x0022, 28800, 0, 700, 270)
    ChrSetPos(0x0023, 29240, 0, -1490, 270)
    ChrClearFlags(0x0000, 0x0080)
    ChrClearFlags(0x0001, 0x0080)
    ChrClearFlags(0x0002, 0x0080)
    ChrClearFlags(0x0003, 0x0080)
    ChrSetPos(0x0000, 27220, 0, -10, 90)
    ChrSetPos(0x0001, 27220, 0, -10, 90)
    ChrSetPos(0x0002, 27220, 0, -10, 90)
    ChrSetPos(0x0003, 27220, 0, -10, 90)
    OP_69(0x0000, 0)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x010A, 65535)
    ChrSetChipByIndex(0x010E, 65535)
    ChrClearFlags(0x0022, 0x0001)
    ChrSetFlags(0x0022, 0x0002)
    ChrSetChipByIndex(0x0022, 26)
    ChrSetSubChip(0x0022, 10)
    ChrClearFlags(0x0023, 0x0001)
    ChrSetFlags(0x0023, 0x0002)
    ChrSetChipByIndex(0x0023, 26)
    ChrSetSubChip(0x0023, 12)
    SetScenaFlags(ScenaFlag(0x0404, 4, 0x2024))
    SetScenaFlags(ScenaFlag(0x0417, 1, 0x20B9))
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

# id: 0x002F offset: 0x8A28
@scena.Code('func_2F_8A28')
def func_2F_8A28():
    Call(0, 0x0030)
    Call(0, 0x0031)

    Return()

# id: 0x0030 offset: 0x8A31
@scena.Code('func_30_8A31')
def func_30_8A31():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    LoadChip('ED6_DT27/CH04621._CH', 'ED6_DT27/CH04621P._CP', 27)
    LoadChip('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP', 28)
    LoadChip('ED6_DT27/CH04001._CH', 'ED6_DT27/CH04001P._CP', 29)
    LoadChip('ED6_DT27/CH04010._CH', 'ED6_DT27/CH04010P._CP', 30)
    LoadChip('ED6_DT27/CH04011._CH', 'ED6_DT27/CH04011P._CP', 31)
    LoadChip('ED6_DT07/CH00420._CH', 'ED6_DT07/CH00420P._CP', 32)
    LoadChip('ED6_DT07/CH00421._CH', 'ED6_DT07/CH00421P._CP', 33)
    LoadChip('ED6_DT07/CH00410._CH', 'ED6_DT07/CH00410P._CP', 34)
    LoadChip('ED6_DT07/CH00411._CH', 'ED6_DT07/CH00411P._CP', 35)
    LoadChip('ED6_DT26/CH20209._CH', 'ED6_DT26/CH20209P._CP', 36)
    LoadChip('ED6_DT26/CH20208._CH', 'ED6_DT26/CH20208P._CP', 37)
    LoadChip('ED6_DT27/CH04611._CH', 'ED6_DT27/CH04611P._CP', 38)
    LoadChip('ED6_DT27/CH04620._CH', 'ED6_DT27/CH04620P._CP', 39)
    LoadChip('ED6_DT27/CH04610._CH', 'ED6_DT27/CH04610P._CP', 40)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x010A, 0x0080)
    ChrSetFlags(0x010E, 0x0080)
    ChrSetPos(0x0022, 41170, 0, 4220, 90)
    ChrSetPos(0x0023, 42610, 0, 4220, 270)
    ChrClearFlags(0x0022, 0x0080)
    ChrClearFlags(0x0023, 0x0080)
    ChrSetChipByIndex(0x0022, 37)
    ChrSetSubChip(0x0022, 0)
    ChrSetChipByIndex(0x0023, 36)
    ChrSetSubChip(0x0023, 0)
    CameraMove(42710, 0, 5190, 0)
    OP_67(0, 5580, -10000, 0)
    CameraSetDistance(2950, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    PlaySE(6, 0x00, 0x64)
    Sleep(500)

    @scena.Lambda('lambda_8B79')
    def lambda_8B79():
        CameraMove(42460, 0, 490, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_8B79)

    @scena.Lambda('lambda_8B91')
    def lambda_8B91():
        OP_6E(302, 1500)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_8B91)

    ChrSetChipByIndex(0x0101, 28)
    ChrSetChipByIndex(0x0102, 30)
    ChrSetChipByIndex(0x010A, 32)
    ChrSetChipByIndex(0x010E, 34)
    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x0102, 0)
    ChrSetSubChip(0x010A, 0)
    ChrSetSubChip(0x010E, 0)
    CreateThread(0x0101, 0x01, 0x00, func_32_8F97)
    CreateThread(0x0102, 0x01, 0x00, func_33_8FE6)
    CreateThread(0x010A, 0x01, 0x00, func_34_903A)
    CreateThread(0x010E, 0x01, 0x00, func_35_908E)
    OP_62(0x0022, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(100)

    @scena.Lambda('lambda_8C01')
    def lambda_8C01():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_8C01)

    OP_62(0x0023, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(100)

    @scena.Lambda('lambda_8C2B')
    def lambda_8C2B():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0023, 0x0001, lambda_8C2B)

    Sleep(1000)

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x010E, 0x0001)

    ChrTalk(
        0x0022,
        (
            '#4210360864V#5P你们……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0023,
        (
            '#4220360865V#5P游、游击士！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0022, 39)
    ChrSetSubChip(0x0022, 0)
    Sleep(50)

    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0023, 40)
    ChrSetSubChip(0x0023, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010360866V#1006F#6P速战速决！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360867V#1046F#4P……解决他们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_8D0D')
    def lambda_8D0D():
        CameraMove(42680, 0, 1100, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_8D0D)

    @scena.Lambda('lambda_8D25')
    def lambda_8D25():
        CameraSetDistance(2420, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_8D25)

    @scena.Lambda('lambda_8D35')
    def lambda_8D35():
        ChrMoveToRelative(0x00FE, 0, 0, 3000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_8D35)

    Sleep(30)

    @scena.Lambda('lambda_8D55')
    def lambda_8D55():
        ChrMoveToRelative(0x00FE, 0, 0, 3000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_8D55)

    Sleep(30)

    ChrSetChipByIndex(0x0022, 27)
    ChrSetFlags(0x0022, 0x1000)

    @scena.Lambda('lambda_8D7F')
    def lambda_8D7F():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0022, 0x0001, lambda_8D7F)

    @scena.Lambda('lambda_8D9A')
    def lambda_8D9A():
        ChrMoveToRelative(0x00FE, 0, 0, 3000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_8D9A)

    Sleep(30)

    @scena.Lambda('lambda_8DBA')
    def lambda_8DBA():
        ChrMoveToRelative(0x00FE, 0, 0, 3000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x010E, 0x0001, lambda_8DBA)

    ChrSetChipByIndex(0x0023, 38)
    ChrSetFlags(0x0023, 0x1000)

    @scena.Lambda('lambda_8DDF')
    def lambda_8DDF():
        ChrMoveToRelative(0x00FE, 0, 0, -3000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0023, 0x0001, lambda_8DDF)

    WaitForThreadExit(0x0101, 0x0003)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x010A, 0xFF)
    TerminateThread(0x010E, 0xFF)
    TerminateThread(0x0022, 0xFF)
    TerminateThread(0x0023, 0xFF)
    Battle(0x0000079D, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_8E2A'),
        (-1, 'loc_8E2F'),
    )

    def _loc_8E2A(): pass

    label('loc_8E2A')

    OP_B4(0x00)

    Jump('loc_8E2F')

    def _loc_8E2F(): pass

    label('loc_8E2F')

    Return()

# id: 0x0031 offset: 0x8E30
@scena.Code('func_31_8E30')
def func_31_8E30():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    ChrSetFlags(0x0022, 0x0080)
    ChrSetFlags(0x0023, 0x0080)
    TerminateThread(0x0022, 0x00)
    TerminateThread(0x0023, 0x00)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x010A, 0x01)
    TerminateThread(0x010E, 0x01)
    TerminateThread(0x0102, 0x01)
    Sleep(500)

    CameraMove(41790, 0, 1060, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrClearFlags(0x0022, 0x0080)
    ChrClearFlags(0x0023, 0x0080)
    ChrSetPos(0x0022, 42290, 0, 3240, 180)
    ChrSetPos(0x0023, 39710, 0, 1520, 180)
    ChrClearFlags(0x0000, 0x0080)
    ChrClearFlags(0x0001, 0x0080)
    ChrClearFlags(0x0002, 0x0080)
    ChrClearFlags(0x0003, 0x0080)
    ChrSetPos(0x0000, 41790, 0, 1060, 0)
    ChrSetPos(0x0001, 41790, 0, 1060, 0)
    ChrSetPos(0x0002, 41790, 0, 1060, 0)
    ChrSetPos(0x0003, 41790, 0, 1060, 0)
    OP_69(0x0000, 0)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x010A, 65535)
    ChrSetChipByIndex(0x010E, 65535)
    ChrClearFlags(0x0022, 0x0001)
    ChrSetFlags(0x0022, 0x0002)
    ChrSetChipByIndex(0x0022, 26)
    ChrSetSubChip(0x0022, 10)
    ChrClearFlags(0x0023, 0x0001)
    ChrSetFlags(0x0023, 0x0002)
    ChrSetChipByIndex(0x0023, 26)
    ChrSetSubChip(0x0023, 13)
    SetScenaFlags(ScenaFlag(0x0404, 4, 0x2024))
    SetScenaFlags(ScenaFlag(0x0416, 7, 0x20B7))
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

# id: 0x0032 offset: 0x8F97
@scena.Code('func_32_8F97')
def func_32_8F97():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, 41710, -500, -5250, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_8FBE')
    def lambda_8FBE():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_8FBE)

    ChrWalkTo(0x00FE, 41710, -250, -2860, 4000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0033 offset: 0x8FE6
@scena.Code('func_33_8FE6')
def func_33_8FE6():
    Sleep(80)

    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, 42810, -500, -5250, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_9012')
    def lambda_9012():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_9012)

    ChrWalkTo(0x00FE, 42810, -250, -2860, 4000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0034 offset: 0x903A
@scena.Code('func_34_903A')
def func_34_903A():
    Sleep(200)

    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, 41090, -500, -5250, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_9066')
    def lambda_9066():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_9066)

    ChrWalkTo(0x00FE, 41090, -250, -4200, 4000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0035 offset: 0x908E
@scena.Code('func_35_908E')
def func_35_908E():
    Sleep(350)

    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, 42620, -500, -5250, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_90BA')
    def lambda_90BA():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_90BA)

    ChrWalkTo(0x00FE, 42620, -250, -4160, 4000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0036 offset: 0x90E2
@scena.Code('func_36_90E2')
def func_36_90E2():
    EventBegin(0x00)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x010A, 0x0080)
    ChrSetFlags(0x010E, 0x0080)
    CameraMove(116200, 10, 5150, 0)
    OP_67(0, 5900, -10000, 0)
    CameraSetDistance(2770, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_4A(0x000B, 255)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    PlaySE(6, 0x00, 0x64)
    Sleep(500)

    @scena.Lambda('lambda_9158')
    def lambda_9158():
        CameraMove(117060, 0, 4540, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_9158)

    @scena.Lambda('lambda_9170')
    def lambda_9170():
        OP_6E(282, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_9170)

    CreateThread(0x0101, 0x01, 0x00, func_37_9843)
    CreateThread(0x0102, 0x01, 0x00, func_38_98A6)
    CreateThread(0x010A, 0x01, 0x00, func_39_990E)
    CreateThread(0x010E, 0x01, 0x00, func_3A_9976)
    OP_62(0x0008, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_91D4')
    def lambda_91D4():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_91D4)

    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0008,
        (
            '#0530360868V#780F#5P噢噢……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#3900360869V#5P大家……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360870V#1006F#6P嘿嘿，我们来帮忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360871V#1035F#4P……好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0530360872V#783F#5P艾丝蒂尔、约修亚。\n',
            '你们竟然来了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530360873V#780F后面的各位\n',
            '也是协会的游击士吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010E,
        (
            '#0330360874V#843F#4P是的。\n',
            '在下是克鲁茨·纳尔当。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120360875V#1310F#6P初次见面！\n',
            '我是亚妮拉丝·艾尔菲德。',
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
            '将事情的经过和学院解放计划做了说明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#0530360876V#783F#5P是吗……非常感谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530360877V#782F率领士兵侵袭这里的人是谁\n',
            '你们知道了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360878V#1007F#6P不就是前市长秘书基尔巴特吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010360879V#1019F听说那个家伙\n',
            '打起了科洛丝的主意……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0530360880V#782F#5P嗯～不过他好像\n',
            '并不知道科洛丝\n',
            '就是公主，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530360881V只不过是得到了\n',
            '公主在这间学院\n',
            '就读的情报而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260518V#1015F#6P这、这个嘛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010360883V但想想那个怪盗，\n',
            '他就算不知道也不奇怪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)
    Sleep(300)

    ChrTalk(
        0x0102,
        (
            '#0020360884V#1035F#2P执行者和普通战斗员的\n',
            '权限有着天壤之别。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360885V#1040F像这种情报应该\n',
            '不会告诉他的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010360886V#1016F#6P原来如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120360887V#817F#6P不过，那样的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120360888V#812F其它的女学生很可能\n',
            '也会被牵连进来的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010E,
        (
            '#0330360889V#842F#4P啊啊，确实有那种危险性。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_96A7')
    def lambda_96A7():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_96A7)

    ChrSetDirection(0x0101, 0, 400)

    ChrTalk(
        0x0008,
        (
            '#0530360890V#783F#5P我也很担心这一点呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530360891V#782F抱歉，\n',
            '只能拜托你们多费心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360892V#1002F#6P嗯，明白了！',
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
            '在科林兹校长、珐奥娜\n',
            '的名字上做了标记。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0404, 5, 0x2025))
    OP_28(0x00C0, 0x01, 0x0100)
    OP_28(0x00C1, 0x02, 0x0001)
    OP_28(0x00C1, 0x01, 0x0002)
    Fade(500)
    CameraMove(116280, 0, 2740, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, 116280, 0, 2740, 0)
    ChrSetPos(0x0001, 116280, 0, 2740, 0)
    ChrSetPos(0x0002, 116280, 0, 2740, 0)
    ChrSetPos(0x0003, 116280, 0, 2740, 0)
    OP_4B(0x000B, 255)
    OP_0D()
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

# id: 0x0037 offset: 0x9843
@scena.Code('func_37_9843')
def func_37_9843():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, 117010, 0, -3090, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_986A')
    def lambda_986A():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_986A)

    ChrWalkTo(0x00FE, 117050, 0, 1350, 4000, 0x00)
    ChrWalkTo(0x00FE, 115490, 0, 2750, 4000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0038 offset: 0x98A6
@scena.Code('func_38_98A6')
def func_38_98A6():
    Sleep(400)

    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, 117010, 0, -3090, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_98D2')
    def lambda_98D2():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_98D2)

    ChrWalkTo(0x00FE, 117050, 0, 1350, 4000, 0x00)
    ChrWalkTo(0x00FE, 116580, 0, 2680, 4000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0039 offset: 0x990E
@scena.Code('func_39_990E')
def func_39_990E():
    Sleep(800)

    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, 117010, 0, -3090, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_993A')
    def lambda_993A():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_993A)

    ChrWalkTo(0x00FE, 117050, 0, 740, 4000, 0x00)
    ChrWalkTo(0x00FE, 116300, 0, 1680, 4000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x003A offset: 0x9976
@scena.Code('func_3A_9976')
def func_3A_9976():
    Sleep(1200)

    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, 117010, 0, -3090, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_99A2')
    def lambda_99A2():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_99A2)

    ChrWalkTo(0x00FE, 117390, 0, 1570, 4000, 0x00)
    ChrSetDirection(0x00FE, 315, 400)

    Return()

# id: 0x003B offset: 0x99CA
@scena.Code('func_3B_99CA')
def func_3B_99CA():
    EventBegin(0x00)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x010A, 0x0080)
    ChrSetFlags(0x010E, 0x0080)
    CameraMove(2620, 0, 5110, 0)
    OP_67(0, 4990, -10000, 0)
    CameraSetDistance(2720, 0)
    OP_6C(45000, 0)
    OP_6E(295, 0)
    OP_4A(0x000A, 255)
    OP_4A(0x0009, 255)
    OP_4A(0x0020, 255)
    OP_4A(0x0012, 255)
    OP_4A(0x0021, 255)
    ChrSetPos(0x000A, 1470, 0, 5490, 0)
    ChrSetPos(0x0009, 2500, 0, 5490, 0)
    ChrSetPos(0x0020, -240, 0, 3050, 180)
    ChrSetPos(0x0012, -650, 0, 2060, 90)
    ChrSetPos(0x0021, 350, 0, 1140, 0)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x0020, 0x0080)
    ChrClearFlags(0x0021, 0x0080)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    PlaySE(192, 0x00, 0x64)
    Sleep(500)

    @scena.Lambda('lambda_9AB9')
    def lambda_9AB9():
        CameraMove(3110, 0, 3980, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_9AB9)

    @scena.Lambda('lambda_9AD1')
    def lambda_9AD1():
        OP_6E(327, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_9AD1)

    CreateThread(0x0101, 0x01, 0x00, func_3C_A424)
    CreateThread(0x0102, 0x01, 0x00, func_3D_A46C)
    CreateThread(0x010A, 0x01, 0x00, func_3E_A4B9)
    CreateThread(0x010E, 0x01, 0x00, func_3F_A506)
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_9B14')
    def lambda_9B14():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_9B14)

    Sleep(100)

    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_9B3E')
    def lambda_9B3E():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_9B3E)

    Sleep(100)

    OP_62(0x0020, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_9B68')
    def lambda_9B68():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0020, 0x0001, lambda_9B68)

    Sleep(50)

    OP_62(0x0012, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_9B92')
    def lambda_9B92():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_9B92)

    Sleep(50)

    OP_62(0x0021, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_9BBC')
    def lambda_9BBC():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0021, 0x0001, lambda_9BBC)

    Sleep(1000)

    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0009,
        (
            '#0510360893V#641F#5P啊！你们两个终于来了啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0520360894V#731F#5P哎呀～等啊等啊\n',
            '都已经等得不耐烦了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360895V#1008F#6P嘿嘿……\n',
            '抱歉，久等啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360896V#1040F#4P那之后情况有什么变化吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0510360897V#645F#5P嗯，其实呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_9CD0')
    def lambda_9CD0():
        CameraMove(3880, 0, 3670, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_9CD0)

    @scena.Lambda('lambda_9CE8')
    def lambda_9CE8():
        ChrMoveTo(0x00FE, 3380, 0, 4360, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_9CE8)

    Sleep(100)

    ChrWalkTo(0x000A, 2390, 0, 5290, 3000, 0x00)
    ChrWalkTo(0x000A, 2440, 0, 4460, 3000, 0x00)
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0009,
        (
            '#0510360898V#642F#5P（刚才基尔巴特来了一趟，\n',
            '  问王家的公主在不在这里。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510360899V（还说如果主动坦白的话\n',
            '  可以得到特别待遇。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360900V#1019F#6P（哎呀呀～……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360901V#1035F#4P（……还真是个彻底的蠢材啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0520360902V#734F#5P（嗯，总之我们就把他\n',
            '  搪塞过去了……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520360903V#732F（不过说不定他还会\n',
            '干出什么事呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360904V#1002F#6P（嗯，我们会留意他的。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#3910360905V#6P喂，喂……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0021,
        (
            '#3930360906V#6P那个，我们\n',
            '现在能做什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_9F1C')
    def lambda_9F1C():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_9F1C)

    @scena.Lambda('lambda_9F2A')
    def lambda_9F2A():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_9F2A)

    Sleep(80)

    @scena.Lambda('lambda_9F3D')
    def lambda_9F3D():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_9F3D)

    @scena.Lambda('lambda_9F4B')
    def lambda_9F4B():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x010E, 0x0001, lambda_9F4B)

    Sleep(80)

    @scena.Lambda('lambda_9F5E')
    def lambda_9F5E():
        ChrSetDirection(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_9F5E)

    ChrSetDirection(0x000A, 225, 400)

    ChrTalk(
        0x0101,
        (
            '#0010360907V#1004F#2P啊，不好意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010360908V#1006F在危机彻底解除之前，\n',
            '大家先待在这里别动可以吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010360909V外边的战斗现在还没结束呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0021,
        (
            '#3930360910V#6P明白啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0020,
        (
            '#3910360911V#6P呼……\n',
            '拜托饶了我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#3920360912V#6P真、真是紧张，\n',
            '但我会努力等的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360913V#1040F#2P抱歉，我们会尽快\n',
            '将事情解决的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0102, 0, 400)

    ChrTalk(
        0x0102,
        (
            '#0020360914V#1042F#4P汉斯、乔儿，你们也……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_A0F4')
    def lambda_A0F4():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_A0F4)

    Sleep(50)

    @scena.Lambda('lambda_A107')
    def lambda_A107():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_A107)

    Sleep(50)

    @scena.Lambda('lambda_A11A')
    def lambda_A11A():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_A11A)

    Sleep(50)

    @scena.Lambda('lambda_A12D')
    def lambda_A12D():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_A12D)

    Sleep(50)

    @scena.Lambda('lambda_A140')
    def lambda_A140():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_A140)

    Sleep(50)

    ChrSetDirection(0x010E, 0, 400)

    ChrTalk(
        0x0009,
        (
            '#0510360915V#644F#5P是是，我们明白。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510360916V#648F不会给你们添麻烦的，\n',
            '只会成为你们的累赘呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0520360917V#730F#5P等事情都搞定后再来吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520360918V到时的善后工作\n',
            '留给我们做就ＯＫ了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360919V#1049F#4P嗯，到时就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360920V#1006F#6P好了，那一会儿再见了！',
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
            '在乔儿、汉斯、坎诺、雅莉丝、\n',
            '帕布尔的名字上做了标记。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0404, 6, 0x2026))
    OP_28(0x00C0, 0x01, 0x0200)
    OP_28(0x00C1, 0x02, 0x4000)
    OP_28(0x00C1, 0x01, 0x8000)
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(2970, 0, 170, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x000A, 3470, 0, 2580, 180)
    ChrSetPos(0x0009, 3500, 0, 1470, 0)
    ChrSetPos(0x0020, -240, 0, 3050, 90)
    ChrSetPos(0x0012, -650, 0, 2060, 90)
    ChrSetPos(0x0021, 350, 0, 1140, 90)
    ChrSetPos(0x0000, 2970, 0, 170, 180)
    ChrSetPos(0x0001, 2970, 0, 170, 180)
    ChrSetPos(0x0002, 2970, 0, 170, 180)
    ChrSetPos(0x0003, 2970, 0, 170, 180)
    OP_69(0x0000, 0)
    OP_4B(0x000A, 255)
    OP_4B(0x0009, 255)
    OP_4B(0x0020, 255)
    OP_4B(0x0012, 255)
    OP_4B(0x0021, 255)
    ChrSetDirection(0x0020, 180, 0)
    ChrSetDirection(0x0012, 90, 0)
    ChrSetDirection(0x0021, 0, 0)
    OP_0D()
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

# id: 0x003C offset: 0xA424
@scena.Code('func_3C_A424')
def func_3C_A424():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, 3040, 0, -2940, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_A44B')
    def lambda_A44B():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_A44B)

    ChrWalkTo(0x00FE, 2430, 0, 2770, 4000, 0x00)

    Return()

# id: 0x003D offset: 0xA46C
@scena.Code('func_3D_A46C')
def func_3D_A46C():
    Sleep(400)

    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, 3040, 0, -2940, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_A498')
    def lambda_A498():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_A498)

    ChrWalkTo(0x00FE, 3480, 0, 2670, 4000, 0x00)

    Return()

# id: 0x003E offset: 0xA4B9
@scena.Code('func_3E_A4B9')
def func_3E_A4B9():
    Sleep(800)

    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, 3040, 0, -2940, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_A4E5')
    def lambda_A4E5():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_A4E5)

    ChrWalkTo(0x00FE, 2180, 0, 1340, 4000, 0x00)

    Return()

# id: 0x003F offset: 0xA506
@scena.Code('func_3F_A506')
def func_3F_A506():
    Sleep(1200)

    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, 3040, 0, -2940, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_A532')
    def lambda_A532():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_A532)

    ChrWalkTo(0x00FE, 3400, 0, 1350, 4000, 0x00)

    Return()

# id: 0x0040 offset: 0xA553
@scena.Code('func_40_A553')
def func_40_A553():
    Call(0, 0x0041)
    Call(0, 0x0042)

    Return()

# id: 0x0041 offset: 0xA55C
@scena.Code('func_41_A55C')
def func_41_A55C():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    LoadChip('ED6_DT27/CH04621._CH', 'ED6_DT27/CH04621P._CP', 27)
    LoadChip('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP', 28)
    LoadChip('ED6_DT27/CH04001._CH', 'ED6_DT27/CH04001P._CP', 29)
    LoadChip('ED6_DT27/CH04010._CH', 'ED6_DT27/CH04010P._CP', 30)
    LoadChip('ED6_DT27/CH04011._CH', 'ED6_DT27/CH04011P._CP', 31)
    LoadChip('ED6_DT07/CH00420._CH', 'ED6_DT07/CH00420P._CP', 32)
    LoadChip('ED6_DT07/CH00421._CH', 'ED6_DT07/CH00421P._CP', 33)
    LoadChip('ED6_DT07/CH00410._CH', 'ED6_DT07/CH00410P._CP', 34)
    LoadChip('ED6_DT07/CH00411._CH', 'ED6_DT07/CH00411P._CP', 35)
    LoadChip('ED6_DT26/CH20209._CH', 'ED6_DT26/CH20209P._CP', 36)
    LoadChip('ED6_DT26/CH20208._CH', 'ED6_DT26/CH20208P._CP', 37)
    LoadChip('ED6_DT27/CH04611._CH', 'ED6_DT27/CH04611P._CP', 38)
    LoadChip('ED6_DT27/CH04621._CH', 'ED6_DT27/CH04621P._CP', 39)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x010A, 0x0080)
    ChrSetFlags(0x010E, 0x0080)
    CameraMove(44540, 0, 38690, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetChipByIndex(0x0024, 36)
    ChrSetChipByIndex(0x0025, 37)
    ChrSetPos(0x0024, 32720, 0, 29970, 90)
    ChrSetPos(0x0025, 51040, 0, 29970, 270)
    ChrClearFlags(0x0024, 0x0080)
    ChrClearFlags(0x0025, 0x0080)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_A680')
    def lambda_A680():
        CameraMove(41850, 0, 30040, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_A680)

    @scena.Lambda('lambda_A698')
    def lambda_A698():
        ChrWalkTo(0x00FE, 40890, 0, 29970, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0024, 0x0001, lambda_A698)

    @scena.Lambda('lambda_A6B3')
    def lambda_A6B3():
        ChrWalkTo(0x00FE, 42730, 0, 29970, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_A6B3)

    WaitForThreadExit(0x0024, 0x0001)
    WaitForThreadExit(0x0025, 0x0001)
    ChrSetSubChip(0x0024, 0)
    ChrSetSubChip(0x0025, 0)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0024,
        (
            '#4230360921V#6P喂……\n',
            '你有没有听到外面有枪声？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0025,
        (
            '#4250360922V#2P……你也听到了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_A742')
    def lambda_A742():
        CameraMove(42070, 0, 27750, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_A742)

    @scena.Lambda('lambda_A75A')
    def lambda_A75A():
        ChrWalkTo(0x00FE, 40570, 0, 26740, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0024, 0x0001, lambda_A75A)

    Sleep(100)

    @scena.Lambda('lambda_A77A')
    def lambda_A77A():
        ChrWalkTo(0x00FE, 42430, 0, 26770, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_A77A)

    WaitForThreadExit(0x0024, 0x0001)
    WaitForThreadExit(0x0025, 0x0001)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0024,
        (
            '#4230360923V#5P不过正门的防线\n',
            '看起来还没有被突破啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0101, 46770, -2000, 38650, 270)

    ChrTalk(
        0x0101,
        (
            '#0010360924V#4P那只是佯攻而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0024, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(100)

    OP_62(0x0025, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_A84E')
    def lambda_A84E():
        CameraMove(42800, 0, 31350, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_A84E)

    @scena.Lambda('lambda_A866')
    def lambda_A866():
        OP_67(0, 6030, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_A866)

    @scena.Lambda('lambda_A87E')
    def lambda_A87E():
        OP_6E(337, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_A87E)

    @scena.Lambda('lambda_A88E')
    def lambda_A88E():
        CameraSetDistance(2500, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_A88E)

    @scena.Lambda('lambda_A89E')
    def lambda_A89E():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0024, 0x0001, lambda_A89E)

    CreateThread(0x0101, 0x01, 0x00, func_43_AC3D)
    Sleep(250)

    @scena.Lambda('lambda_A8B8')
    def lambda_A8B8():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0025, 0x0001, lambda_A8B8)

    CreateThread(0x0102, 0x01, 0x00, func_44_AC88)
    Sleep(250)

    CreateThread(0x010A, 0x01, 0x00, func_45_ACE7)
    Sleep(250)

    CreateThread(0x010E, 0x01, 0x00, func_46_AD32)
    WaitForThreadExit(0x0102, 0x0002)

    ChrTalk(
        0x0025,
        (
            '#4250360925V#4P什…么…！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0024,
        (
            '#4230360926V#6P怎、怎么会！？\n',
            '你们是怎么进来的！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360927V#1029F#6P哼哼，答案很简单……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120360928V#816F#5P因为我们是游击士！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360929V#1048F#6P（根本就是答非所问嘛……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_A9D3')
    def lambda_A9D3():
        CameraMove(42340, 0, 30650, 280)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_A9D3)

    @scena.Lambda('lambda_A9EB')
    def lambda_A9EB():
        CameraSetDistance(2320, 280)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_A9EB)

    OP_0D()

    @scena.Lambda('lambda_A9FC')
    def lambda_A9FC():
        OP_94(0x00, 0x00FE, 0x0000, 0x000009C4, 0x00001F40, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_A9FC)

    Sleep(30)

    ChrSetChipByIndex(0x0024, 38)
    ChrSetFlags(0x0024, 0x1000)

    @scena.Lambda('lambda_AA21')
    def lambda_AA21():
        OP_94(0x00, 0x00FE, 0x0000, 0x000009C4, 0x00001F40, 0x00)

        ExitThread()

    DispatchAsync(0x0024, 0x0001, lambda_AA21)

    @scena.Lambda('lambda_AA37')
    def lambda_AA37():
        OP_94(0x00, 0x00FE, 0x0000, 0x000009C4, 0x00001F40, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_AA37)

    Sleep(30)

    ChrSetChipByIndex(0x0025, 39)
    ChrSetFlags(0x0025, 0x1000)

    @scena.Lambda('lambda_AA5C')
    def lambda_AA5C():
        OP_94(0x00, 0x00FE, 0x0000, 0x000009C4, 0x00001F40, 0x00)

        ExitThread()

    DispatchAsync(0x0025, 0x0003, lambda_AA5C)

    @scena.Lambda('lambda_AA72')
    def lambda_AA72():
        OP_94(0x00, 0x00FE, 0x0000, 0x000009C4, 0x00001F40, 0x00)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_AA72)

    Sleep(30)

    @scena.Lambda('lambda_AA8D')
    def lambda_AA8D():
        OP_94(0x00, 0x00FE, 0x0000, 0x000009C4, 0x00001F40, 0x00)

        ExitThread()

    DispatchAsync(0x010E, 0x0001, lambda_AA8D)

    Sleep(150)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x010A, 0xFF)
    TerminateThread(0x010E, 0xFF)
    TerminateThread(0x0024, 0xFF)
    TerminateThread(0x0025, 0xFF)
    Battle(0x0000079F, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_AAD3'),
        (-1, 'loc_AAD8'),
    )

    def _loc_AAD3(): pass

    label('loc_AAD3')

    OP_B4(0x00)

    Jump('loc_AAD8')

    def _loc_AAD8(): pass

    label('loc_AAD8')

    Return()

# id: 0x0042 offset: 0xAAD9
@scena.Code('func_42_AAD9')
def func_42_AAD9():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    ChrSetFlags(0x0024, 0x0080)
    ChrSetFlags(0x0025, 0x0080)
    TerminateThread(0x0024, 0x00)
    TerminateThread(0x0025, 0x00)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x010A, 0x01)
    TerminateThread(0x010E, 0x01)
    TerminateThread(0x0102, 0x01)
    Sleep(500)

    CameraMove(41850, 0, 31500, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x010A, 65535)
    ChrSetChipByIndex(0x010E, 65535)
    ChrClearFlags(0x0024, 0x0080)
    ChrClearFlags(0x0025, 0x0080)
    ChrSetPos(0x0024, 39960, 0, 29850, 0)
    ChrSetPos(0x0025, 42350, 0, 29860, 0)
    ChrClearFlags(0x0024, 0x0001)
    ChrSetFlags(0x0024, 0x0002)
    ChrSetChipByIndex(0x0024, 26)
    ChrSetSubChip(0x0024, 12)
    ChrClearFlags(0x0025, 0x0001)
    ChrSetFlags(0x0025, 0x0002)
    ChrSetChipByIndex(0x0025, 26)
    ChrSetSubChip(0x0025, 10)
    ChrClearFlags(0x0000, 0x0080)
    ChrClearFlags(0x0001, 0x0080)
    ChrClearFlags(0x0002, 0x0080)
    ChrClearFlags(0x0003, 0x0080)
    ChrSetPos(0x0000, 41850, 0, 31500, 180)
    ChrSetPos(0x0001, 41850, 0, 31500, 180)
    ChrSetPos(0x0002, 41850, 0, 31500, 180)
    ChrSetPos(0x0003, 41850, 0, 31500, 180)
    OP_69(0x0000, 0)
    SetScenaFlags(ScenaFlag(0x0404, 7, 0x2027))
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

# id: 0x0043 offset: 0xAC3D
@scena.Code('func_43_AC3D')
def func_43_AC3D():
    ChrSetChipByIndex(0x0101, 28)
    ChrSetPos(0x00FE, 46560, -2000, 38540, 270)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 41750, 0, 38470, 6000, 0x00)
    ChrWalkTo(0x00FE, 40870, 0, 33610, 6000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x0044 offset: 0xAC88
@scena.Code('func_44_AC88')
def func_44_AC88():
    ChrSetChipByIndex(0x0102, 30)
    ChrSetPos(0x00FE, 46560, -2000, 38540, 270)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 41750, 0, 38470, 6000, 0x00)
    ChrWalkTo(0x00FE, 40730, 0, 35090, 6000, 0x00)
    ChrWalkTo(0x00FE, 42180, 0, 33560, 6000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x0045 offset: 0xACE7
@scena.Code('func_45_ACE7')
def func_45_ACE7():
    ChrSetChipByIndex(0x010A, 32)
    ChrSetPos(0x00FE, 46560, -2000, 38540, 270)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 41750, 0, 38470, 6000, 0x00)
    ChrWalkTo(0x00FE, 40920, 0, 34870, 6000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x0046 offset: 0xAD32
@scena.Code('func_46_AD32')
def func_46_AD32():
    ChrSetChipByIndex(0x010E, 34)
    ChrSetPos(0x00FE, 46560, -2000, 38540, 270)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 41750, 0, 38470, 6000, 0x00)
    ChrWalkTo(0x00FE, 40740, 0, 36500, 6000, 0x00)
    ChrWalkTo(0x00FE, 42350, 0, 35040, 6000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x0047 offset: 0xAD91
@scena.Code('func_47_AD91')
def func_47_AD91():
    EventBegin(0x00)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x010A, 0x0080)
    ChrSetFlags(0x010E, 0x0080)
    CameraMove(500, 0, 33070, 0)
    OP_67(0, 6800, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(272, 0)
    OP_4A(0x0014, 255)
    OP_4A(0x001A, 255)
    OP_4A(0x0015, 255)
    OP_4A(0x001C, 255)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    PlaySE(192, 0x00, 0x64)
    Sleep(500)

    @scena.Lambda('lambda_AE13')
    def lambda_AE13():
        CameraMove(2270, 0, 33520, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_AE13)

    @scena.Lambda('lambda_AE2B')
    def lambda_AE2B():
        OP_67(0, 6160, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_AE2B)

    @scena.Lambda('lambda_AE43')
    def lambda_AE43():
        CameraSetDistance(3040, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_AE43)

    @scena.Lambda('lambda_AE53')
    def lambda_AE53():
        OP_6E(267, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_AE53)

    CreateThread(0x0101, 0x01, 0x00, func_48_B571)
    CreateThread(0x010A, 0x01, 0x00, func_49_B5C0)
    CreateThread(0x0102, 0x01, 0x00, func_4A_B614)
    CreateThread(0x010E, 0x01, 0x00, func_4B_B668)
    OP_62(0x0014, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_AE96')
    def lambda_AE96():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_AE96)

    Sleep(100)

    OP_62(0x001A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_AEC0')
    def lambda_AEC0():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_AEC0)

    Sleep(100)

    OP_62(0x0015, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_AEEA')
    def lambda_AEEA():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_AEEA)

    Sleep(100)

    OP_62(0x001C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_AF14')
    def lambda_AF14():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x001C, 0x0001, lambda_AF14)

    Sleep(1000)

    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0014,
        (
            '#1930360930V#6P你、你们是……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#3940360931V#6P艾丝蒂尔，还有…\n',
            '约修亚！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360932V#1008F#5P嘿嘿，好久不见啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360933V#1054F#2P好久不见了，各位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0014, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0014,
        (
            '#1930360934V#6P你、你们为什么\n',
            '会在这里呢！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1930360935V难、难道\n',
            '你们也是他们一伙的吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x001C, 0x0014, 400)

    ChrTalk(
        0x001C,
        (
            '#3950360936V#6P罗基克你真是笨啦，\n',
            '这怎么可能嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001A,
        (
            '#3960360937V#6P各位游击士，\n',
            '你们是来救我们的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x001C, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010360938V#1006F#5P嗯，正是。',
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
            '#1930360939V#6P是、是吗……\n',
            '不好意思啊，搞错了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1930360940V那么……！\n',
            '我们现在该怎么做才好！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010E,
        (
            '#0330360941V#843F#2P在事态彻底平息之前，\n',
            '请大家先在这里不要动。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330360942V#840F贸然跑出去的话\n',
            '很有可能会被卷入战斗中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#1930360943V#6P可、可是，在这里待着的话\n',
            '也有可能会被他们抓住的啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120360944V#818F#2P嗯，虽然确实有这种可能，\n',
            '但总比到外边安全吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120360945V#819F外边现在到处是流弹和装甲兽，\n',
            '你可不想被那些猛兽吞下肚吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0014, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0014,
        (
            '#1930360946V#6P哇、哇啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360947V#1016F#6P好了啦～亚妮拉丝。\n',
            '你怎么可以吓唬人嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360948V#1040F#2P不过情况就是这样，请各位\n',
            '先待在这里不要动，可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#3940360949V#6P是……明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001C,
        (
            '#3950360950V#6P要加油啊！各位游击士！',
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
            '在罗基克、亚吉鲁、莫妮卡、塞尔玛\n',
            '的名字上做了标记。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0405, 0, 0x2028))
    OP_28(0x00C0, 0x01, 0x0400)
    OP_28(0x00C1, 0x02, 0x0400)
    OP_28(0x00C1, 0x01, 0x0800)
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(2880, 0, 31810, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, 2880, 0, 31810, 180)
    ChrSetPos(0x0001, 2880, 0, 31810, 180)
    ChrSetPos(0x0002, 2880, 0, 31810, 180)
    ChrSetPos(0x0003, 2880, 0, 31810, 180)
    OP_69(0x0000, 0)
    ChrSetDirection(0x0014, 225, 0)
    ChrSetDirection(0x001A, 0, 0)
    ChrSetDirection(0x0015, 180, 0)
    ChrSetDirection(0x001C, 45, 0)
    OP_4B(0x0014, 255)
    OP_4B(0x001A, 255)
    OP_4B(0x0015, 255)
    OP_4B(0x001C, 255)
    OP_0D()
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

# id: 0x0048 offset: 0xB571
@scena.Code('func_48_B571')
def func_48_B571():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, 2960, 0, 27000, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_B598')
    def lambda_B598():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_B598)

    ChrWalkTo(0x00FE, 2160, 0, 32630, 4000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)

    Return()

# id: 0x0049 offset: 0xB5C0
@scena.Code('func_49_B5C0')
def func_49_B5C0():
    Sleep(300)

    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, 2960, 0, 27000, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_B5EC')
    def lambda_B5EC():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_B5EC)

    ChrWalkTo(0x00FE, 3380, 0, 32990, 4000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)

    Return()

# id: 0x004A offset: 0xB614
@scena.Code('func_4A_B614')
def func_4A_B614():
    Sleep(600)

    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, 2960, 0, 27000, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_B640')
    def lambda_B640():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_B640)

    ChrWalkTo(0x00FE, 2170, 0, 31460, 4000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)

    Return()

# id: 0x004B offset: 0xB668
@scena.Code('func_4B_B668')
def func_4B_B668():
    Sleep(900)

    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, 2960, 0, 27000, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_B694')
    def lambda_B694():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_B694)

    ChrWalkTo(0x00FE, 3300, 0, 31620, 4000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)

    Return()

# id: 0x004C offset: 0xB6BC
@scena.Code('func_4C_B6BC')
def func_4C_B6BC():
    EventBegin(0x00)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x010A, 0x0080)
    ChrSetFlags(0x010E, 0x0080)
    CameraMove(94250, 0, 35630, 0)
    OP_67(0, 5240, -10000, 0)
    CameraSetDistance(2900, 0)
    OP_6C(45000, 0)
    OP_6E(268, 0)
    OP_4A(0x0018, 255)
    OP_4A(0x0017, 255)
    OP_4A(0x001D, 255)
    OP_4A(0x001E, 255)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    PlaySE(192, 0x00, 0x64)
    Sleep(500)

    @scena.Lambda('lambda_B73E')
    def lambda_B73E():
        CameraMove(94080, 0, 35020, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_B73E)

    @scena.Lambda('lambda_B756')
    def lambda_B756():
        OP_6E(277, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_B756)

    CreateThread(0x0101, 0x01, 0x00, func_4D_BEAE)
    CreateThread(0x010A, 0x01, 0x00, func_4F_BF51)
    CreateThread(0x0102, 0x01, 0x00, func_4E_BEFD)
    CreateThread(0x010E, 0x01, 0x00, func_50_BFA5)
    OP_62(0x001D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_B799')
    def lambda_B799():
        ChrSetDirection(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x001D, 0x0001, lambda_B799)

    Sleep(100)

    OP_62(0x001E, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_B7C3')
    def lambda_B7C3():
        ChrSetDirection(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_B7C3)

    Sleep(100)

    OP_62(0x0018, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_B7ED')
    def lambda_B7ED():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_B7ED)

    Sleep(100)

    OP_62(0x0017, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_B817')
    def lambda_B817():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_B817)

    Sleep(1000)

    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x001E,
        (
            '#2900360951V#5P你们是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360952V#1002F大家没事吧！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360953V#1040F好象没有\n',
            '受伤的人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0018,
        (
            '#3980360954V#5P艾丝蒂尔……\n',
            '连约修亚也在！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3980360955V为什么会在这里！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360956V#1006F嗯，是这样……',
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
            '把至今为止的作战状况\n',
            '向基诺奇奥等人说明了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0017,
        (
            '#2910360957V#5P原来如此……\n',
            '原来是那样的吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#2910360958V这样的话真是该\n',
            '感谢米克啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001D,
        (
            '#3970360959V#5P哼、哼……\n',
            '那家伙不但平时上课总是偷懒，\n',
            '这次又一个人逃跑，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#3970360960V简直是笑柄啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0018, 0x001D, 400)

    ChrTalk(
        0x0018,
        (
            '#3980360961V#5P别胡说了！德尼斯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_BA60')
    def lambda_BA60():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_BA60)

    Sleep(100)

    @scena.Lambda('lambda_BA73')
    def lambda_BA73():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_BA73)

    Sleep(100)

    @scena.Lambda('lambda_BA86')
    def lambda_BA86():
        ChrSetDirection(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_BA86)

    Sleep(100)

    @scena.Lambda('lambda_BA99')
    def lambda_BA99():
        ChrSetDirection(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_BA99)

    Sleep(100)

    ChrSetDirection(0x010A, 45, 400)

    ChrTalk(
        0x001E,
        (
            '#2900360962V#4P在这样的紧急情况下，\n',
            '他的行动非常正确合理。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#2900360963V多亏了他，艾丝蒂尔她们\n',
            '才会及时赶来救我们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#2900360964V再继续这样侮辱和贬低他，\n',
            '反而会降低自己的价值哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001D,
        (
            '#3970360965V#5P唔、唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360966V#1016F#6P好了好了，大家都冷静。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020360967V#1040F#4P总之，在确认情况彻底安全之前，\n',
            '希望大家待在这里别动，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020360968V可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0018, 180, 400)

    ChrTalk(
        0x0018,
        (
            '#3980360969V#5P可、可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_BC49')
    def lambda_BC49():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x001E, 0x0001, lambda_BC49)

    Sleep(100)

    @scena.Lambda('lambda_BC5C')
    def lambda_BC5C():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_BC5C)

    Sleep(100)

    @scena.Lambda('lambda_BC6F')
    def lambda_BC6F():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_BC6F)

    Sleep(100)

    @scena.Lambda('lambda_BC82')
    def lambda_BC82():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x010A, 0x0001, lambda_BC82)

    Sleep(100)

    @scena.Lambda('lambda_BC95')
    def lambda_BC95():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x010E, 0x0001, lambda_BC95)

    Sleep(500)

    ChrTalk(
        0x0018,
        (
            '#3980360970V#5P……我明白了，没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0017, 180, 400)
    ChrSetDirection(0x001E, 225, 400)

    ChrTalk(
        0x001E,
        (
            '#2900360971V#5P……其它的学生\n',
            '也请你们解救出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 45, 400)

    ChrTalk(
        0x0101,
        (
            '#0010360972V#1006F#6P嗯，就交给我们吧！',
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
            '在基诺奇奥、巴托姆、德尼斯、蕾娜\n',
            '的名字上做了标记。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0405, 1, 0x2029))
    OP_28(0x00C0, 0x01, 0x0800)
    OP_28(0x00C1, 0x02, 0x1000)
    OP_28(0x00C1, 0x01, 0x2000)
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(92940, 0, 32090, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, 92940, 0, 32090, 180)
    ChrSetPos(0x0001, 92940, 0, 32090, 180)
    ChrSetPos(0x0002, 92940, 0, 32090, 180)
    ChrSetPos(0x0003, 92940, 0, 32090, 180)
    OP_69(0x0000, 0)
    ChrSetDirection(0x0017, 90, 0)
    ChrSetDirection(0x0018, 270, 0)
    ChrSetPos(0x001D, 94990, 250, 35500, 233)
    ChrSetPos(0x001E, 94520, 250, 33430, 270)
    OP_4B(0x0018, 255)
    OP_4B(0x0017, 255)
    OP_4B(0x001D, 255)
    OP_4B(0x001E, 255)
    OP_0D()
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

# id: 0x004D offset: 0xBEAE
@scena.Code('func_4D_BEAE')
def func_4D_BEAE():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, 92950, 0, 26920, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_BED5')
    def lambda_BED5():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_BED5)

    ChrWalkTo(0x00FE, 92340, 0, 33310, 5000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x004E offset: 0xBEFD
@scena.Code('func_4E_BEFD')
def func_4E_BEFD():
    Sleep(300)

    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, 92950, 0, 26920, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_BF29')
    def lambda_BF29():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_BF29)

    ChrWalkTo(0x00FE, 93370, 0, 33220, 5000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x004F offset: 0xBF51
@scena.Code('func_4F_BF51')
def func_4F_BF51():
    Sleep(600)

    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, 92950, 0, 26920, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_BF7D')
    def lambda_BF7D():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_BF7D)

    ChrWalkTo(0x00FE, 92160, 0, 32049, 5000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0050 offset: 0xBFA5
@scena.Code('func_50_BFA5')
def func_50_BFA5():
    Sleep(900)

    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetPos(0x00FE, 92950, 0, 26920, 0)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_BFD1')
    def lambda_BFD1():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_BFD1)

    ChrWalkTo(0x00FE, 93440, 0, 32049, 5000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0051 offset: 0xBFF9
@scena.Code('func_51_BFF9')
def func_51_BFF9():
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
        (0x00000000, 'loc_C073'),
        (0x00000001, 'loc_C079'),
        (-1, 'loc_C07F'),
    )

    def _loc_C073(): pass

    label('loc_C073')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_C07F')

    def _loc_C079(): pass

    label('loc_C079')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_C07F')

    def _loc_C07F(): pass

    label('loc_C07F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_C08D',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_C091')

    def _loc_C08D(): pass

    label('loc_C08D')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_C091(): pass

    label('loc_C091')

    Return()

# id: 0x0052 offset: 0xC092
@scena.Code('func_52_C092')
def func_52_C092():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　　走　\n',
            '　　廊　\n',
            '　　里　\n',
            '　　请　\n',
            '　　安　\n',
            '　学静　\n',
            '　生！　\n',
            '　指　　\n',
            '　导　　\n',
            '　部　　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0053 offset: 0xC11E
@scena.Code('func_53_C11E')
def func_53_C11E():
    OP_13(0x006F)

    Return()

# id: 0x0054 offset: 0xC122
@scena.Code('func_54_C122')
def func_54_C122():
    OP_13(0x005E)

    Return()

# id: 0x0055 offset: 0xC126
@scena.Code('func_55_C126')
def func_55_C126():
    OP_13(0x006E)

    Return()

# id: 0x0056 offset: 0xC12A
@scena.Code('func_56_C12A')
def func_56_C12A():
    OP_13(0x0074)

    Return()

# id: 0x0057 offset: 0xC12E
@scena.Code('func_57_C12E')
def func_57_C12E():
    OP_13(0x0073)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

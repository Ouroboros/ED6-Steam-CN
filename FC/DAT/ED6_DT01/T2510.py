import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
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
        ('ED6_DT07/CH02600._CH', 'ED6_DT07/CH02600P._CP'),
        ('ED6_DT07/CH02393._CH', 'ED6_DT07/CH02393P._CP'),
        ('ED6_DT07/CH02553._CH', 'ED6_DT07/CH02553P._CP'),
        ('ED6_DT07/CH01360._CH', 'ED6_DT07/CH01360P._CP'),
        ('ED6_DT07/CH01370._CH', 'ED6_DT07/CH01370P._CP'),
        ('ED6_DT07/CH01430._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH02490._CH', 'ED6_DT07/CH02490P._CP'),
        ('ED6_DT07/CH01660._CH', 'ED6_DT07/CH01660P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH01430._CH', 'ED6_DT07/CH01430P._CP'),
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
        ('ED6_DT07/CH01360._CH', 'ED6_DT07/CH01360P._CP'),
        ('ED6_DT07/CH01580._CH', 'ED6_DT07/CH01580P._CP'),
        ('ED6_DT07/CH01590._CH', 'ED6_DT07/CH01590P._CP'),
        ('ED6_DT07/CH01370._CH', 'ED6_DT07/CH01370P._CP'),
        ('ED6_DT07/CH01090._CH', 'ED6_DT07/CH01090P._CP'),
        ('ED6_DT07/CH01080._CH', 'ED6_DT07/CH01080P._CP'),
        ('ED6_DT07/CH01580._CH', 'ED6_DT07/CH01580P._CP'),
        ('ED6_DT07/CH02360._CH', 'ED6_DT07/CH02360P._CP'),
        ('ED6_DT07/CH00003._CH', 'ED6_DT07/CH00003P._CP'),
        ('ED6_DT07/CH00013._CH', 'ED6_DT07/CH00013P._CP'),
        ('ED6_DT07/CH00043._CH', 'ED6_DT07/CH00043P._CP'),
        ('ED6_DT07/CH01363._CH', 'ED6_DT07/CH01363P._CP'),
        ('ED6_DT07/CH01083._CH', 'ED6_DT07/CH01083P._CP'),
        ('ED6_DT07/CH01583._CH', 'ED6_DT07/CH01583P._CP'),
        ('ED6_DT07/CH01373._CH', 'ED6_DT07/CH01373P._CP'),
        ('ED6_DT07/CH01663._CH', 'ED6_DT07/CH01663P._CP'),
        ('ED6_DT07/CH01213._CH', 'ED6_DT07/CH01213P._CP'),
        ('ED6_DT07/CH01433._CH', 'ED6_DT07/CH01433P._CP'),
        ('ED6_DT07/CH01463._CH', 'ED6_DT07/CH01463P._CP'),
        ('ED6_DT07/CH01593._CH', 'ED6_DT07/CH01593P._CP'),
        ('ED6_DT07/CH01093._CH', 'ED6_DT07/CH01093P._CP'),
        ('ED6_DT07/CH02603._CH', 'ED6_DT07/CH02603P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
    ]

# id: 0x10001 offset: 0x1BA
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
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0115,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '乔儿',
            x                   = 30700,
            z                   = 0,
            y                   = 55110,
            direction           = 270,
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
            name                = '汉斯',
            x                   = 29460,
            z                   = 0,
            y                   = 53800,
            direction           = 0,
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
            name                = '男学生',
            x                   = 29460,
            z                   = 0,
            y                   = 53800,
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
            name                = '男学生',
            x                   = 29460,
            z                   = 0,
            y                   = 53800,
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
            name                = '男学生',
            x                   = 29460,
            z                   = 0,
            y                   = 53800,
            direction           = 0,
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
            name                = '女学生',
            x                   = 29460,
            z                   = 0,
            y                   = 53800,
            direction           = 0,
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
            name                = '女教师',
            x                   = 29460,
            z                   = 0,
            y                   = 53800,
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
            name                = '珐奥娜',
            x                   = 41400,
            z                   = 0,
            y                   = 7500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '拉迪奥老师',
            x                   = 84450,
            z                   = 250,
            y                   = 1030,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '碧欧拉老师',
            x                   = 87700,
            z                   = 0,
            y                   = 2800,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '米丽亚老师',
            x                   = 84450,
            z                   = 250,
            y                   = 2790,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '艾福托老师',
            x                   = 87540,
            z                   = 250,
            y                   = 2770,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 29,
            chipIndex           = 29,
            npcIndex            = 0x0155,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '罗迪',
            x                   = 0,
            z                   = 0,
            y                   = 3100,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '坎诺',
            x                   = -2800,
            z                   = 0,
            y                   = 4000,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '雅莉丝',
            x                   = -700,
            z                   = 0,
            y                   = 4000,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '黛拉',
            x                   = 3500,
            z                   = 0,
            y                   = 2000,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '帕布尔',
            x                   = -3100,
            z                   = 0,
            y                   = 5400,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '罗基克',
            x                   = 4490,
            z                   = 250,
            y                   = 34880,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0105,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            name                = '罗伊斯',
            x                   = 4790,
            z                   = 250,
            y                   = -1130,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            name                = '莫妮卡',
            x                   = 5400,
            z                   = 300,
            y                   = 30500,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            name                = '塞尔玛',
            x                   = 3040,
            z                   = 0,
            y                   = 35050,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 15,
            chipIndex           = 15,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            name                = '基诺奇奥',
            x                   = 85800,
            z                   = 0,
            y                   = 30000,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            name                = '妮吉塔',
            x                   = 84080,
            z                   = 0,
            y                   = 30000,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            name                = '梅贝尔市长',
            x                   = -3900,
            z                   = 0,
            y                   = 3100,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 18,
            chipIndex           = 18,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            name                = '戴尔蒙市长',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = 'CH22000',
            x                   = 85590,
            z                   = 700,
            y                   = 3050,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1835041,
            chipIndex           = 33,
            npcIndex            = 0x0166,
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
            x           = 51000,
            y           = 0,
            z           = 1400,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000001B,
        ),
        ScenaEventData(
            x           = 59000,
            y           = 0,
            z           = 1400,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000001C,
        ),
        ScenaEventData(
            x           = 33000,
            y           = 0,
            z           = 1400,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000001D,
        ),
        ScenaEventData(
            x           = 58990,
            y           = 0,
            z           = 31330,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000001E,
        ),
        ScenaEventData(
            x           = 33000,
            y           = 0,
            z           = 31400,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000001F,
        ),
    )

# id: 0x10004 offset: 0x5BA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 33000,
            triggerZ            = 0,
            triggerY            = 2190,
            triggerRange        = 800,
            actorX              = 33000,
            actorZ              = 1000,
            actorY              = 2190,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0018,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 33000,
            triggerZ            = 0,
            triggerY            = 32200,
            triggerRange        = 800,
            actorX              = 33000,
            actorZ              = 1000,
            actorY              = 32200,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0018,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 59000,
            triggerZ            = 0,
            triggerY            = 32000,
            triggerRange        = 800,
            actorX              = 59000,
            actorZ              = 1000,
            actorY              = 32000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0018,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 41200,
            triggerZ            = 0,
            triggerY            = 5490,
            triggerRange        = 400,
            actorX              = 41400,
            actorZ              = 1500,
            actorY              = 7500,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
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
            talkFunctionIndex   = 0x0019,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 85590,
            triggerZ            = 700,
            triggerY            = 3400,
            triggerRange        = 1000,
            actorX              = 85590,
            actorZ              = 1000,
            actorY              = 3050,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001A,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x692
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_7A9',
    )

    ChrSetPos(0x0011, 5320, 250, 2110, 270)
    ChrSetPos(0x0016, -3060, 0, 3170, 45)
    ChrSetPos(0x0015, 560, 100, 240, 90)
    ChrSetChipByIndex(0x0015, 22)
    ChrSetFlags(0x0015, 0x0004)
    ChrSetFlags(0x0015, 0x0010)
    TerminateThread(0x0015, 0xFF)
    ChrSetPos(0x0012, 5300, 250, 32080, 180)
    ChrSetFlags(0x0012, 0x0010)
    ChrSetPos(0x001B, -1100, 0, 32240, 270)
    ChrSetChipByIndex(0x001D, 31)
    ChrSetPos(0x001D, -2660, 100, 32180, 90)
    ChrSetFlags(0x001D, 0x0004)
    ChrSetFlags(0x001D, 0x0010)
    TerminateThread(0x001D, 0xFF)
    ChrSetChipByIndex(0x001A, 23)
    ChrSetPos(0x001A, -5950, 100, 34220, 90)
    ChrSetFlags(0x001A, 0x0004)
    ChrSetFlags(0x001A, 0x0010)
    TerminateThread(0x001A, 0xFF)
    ChrClearFlags(0x001E, 0x0080)
    ChrSetPos(0x001E, 86430, 0, 31990, 90)
    ChrClearFlags(0x001F, 0x0080)
    ChrSetPos(0x001F, 95400, 250, 31050, 90)
    ChrClearFlags(0x001C, 0x0080)
    ChrSetChipByIndex(0x0013, 28)
    ChrSetFlags(0x0013, 0x0004)
    ChrSetFlags(0x0013, 0x0010)
    TerminateThread(0x0013, 0xFF)
    ChrSetFlags(0x0014, 0x0080)
    ChrSetFlags(0x0017, 0x0080)
    ChrSetFlags(0x0019, 0x0080)
    ChrSetChipByIndex(0x0008, 32)

    Jump('loc_A78')

    def _loc_7A9(): pass

    label('loc_7A9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_7F4',
    )

    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0014, 0x0080)
    ChrSetFlags(0x0015, 0x0080)
    ChrSetFlags(0x0016, 0x0080)
    ChrSetFlags(0x0017, 0x0080)
    ChrSetFlags(0x0018, 0x0080)
    ChrSetFlags(0x0019, 0x0080)
    ChrSetFlags(0x001A, 0x0080)
    ChrSetFlags(0x001D, 0x0080)
    ChrSetFlags(0x001B, 0x0080)
    ChrSetChipByIndex(0x0008, 32)

    Jump('loc_A78')

    def _loc_7F4(): pass

    label('loc_7F4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_886',
    )

    ChrSetPos(0x0011, 1710, 0, 4970, 180)
    ChrSetPos(0x0012, -6910, 0, 33220, 90)
    ChrSetPos(0x0013, 95370, 250, 34220, 225)
    ChrSetPos(0x0008, 42950, 0, 1120, 270)
    ChrSetPos(0x0016, -7060, 0, 1680, 90)
    ChrSetPos(0x0017, 920, 0, -1500, 0)
    ChrSetPos(0x0018, -1590, 0, 34700, 0)
    ChrSetPos(0x001A, 1300, 0, 28510, 90)

    Jump('loc_A78')

    def _loc_886(): pass

    label('loc_886')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_91B',
    )

    ChrSetPos(0x0011, 1710, 0, 4970, 180)
    ChrSetPos(0x0012, -6910, 0, 33220, 90)
    ChrSetPos(0x0013, 95370, 250, 34220, 225)
    ChrSetPos(0x0008, 43470, 0, 5280, 225)
    ChrSetFlags(0x0008, 0x0010)
    ChrSetFlags(0x0015, 0x0080)
    ChrSetFlags(0x0018, 0x0080)
    ChrSetPos(0x0016, -7060, 0, 1680, 90)
    ChrSetPos(0x0017, 920, 0, -1500, 0)
    ChrSetPos(0x001A, 1300, 0, 28510, 90)
    ChrClearFlags(0x0020, 0x0080)

    Jump('loc_A78')

    def _loc_91B(): pass

    label('loc_91B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_976',
    )

    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0014, 0x0080)
    ChrSetFlags(0x0015, 0x0080)
    ChrSetFlags(0x0018, 0x0080)
    ChrSetFlags(0x0019, 0x0080)
    ChrSetPos(0x0016, -5200, 0, 2050, 0)
    ChrSetPos(0x0017, 4500, 250, 4019, 270)
    ChrSetPos(0x001A, 790, 0, 34680, 0)
    ChrSetChipByIndex(0x0008, 32)

    Jump('loc_A78')

    def _loc_976(): pass

    label('loc_976')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_A27',
    )

    ChrSetPos(0x0012, 5300, 250, 32080, 90)
    ChrSetFlags(0x0014, 0x0080)
    ChrSetFlags(0x0015, 0x0080)
    ChrSetFlags(0x0018, 0x0080)
    ChrSetFlags(0x0019, 0x0080)
    ChrClearFlags(0x001E, 0x0080)
    ChrClearFlags(0x001F, 0x0080)
    ChrSetChipByIndex(0x0013, 28)
    ChrSetFlags(0x0013, 0x0004)
    ChrSetFlags(0x0013, 0x0010)
    TerminateThread(0x0013, 0xFF)
    ChrSetChipByIndex(0x0011, 26)
    ChrSetFlags(0x0011, 0x0004)
    ChrSetFlags(0x0011, 0x0010)
    TerminateThread(0x0011, 0xFF)
    ChrSetChipByIndex(0x0016, 24)
    ChrSetPos(0x0016, -2650, 100, 4200, 90)
    ChrSetFlags(0x0016, 0x0004)
    ChrSetFlags(0x0016, 0x0010)
    TerminateThread(0x0016, 0xFF)
    ChrSetChipByIndex(0x001F, 30)
    ChrSetPos(0x001F, 84120, 100, 30200, 90)
    ChrSetFlags(0x001F, 0x0004)
    ChrSetFlags(0x001F, 0x0010)
    TerminateThread(0x001F, 0xFF)
    ChrSetFlags(0x001B, 0x0080)
    ChrSetChipByIndex(0x0008, 32)

    Jump('loc_A78')

    def _loc_A27(): pass

    label('loc_A27')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 6, 0x42E)),
            Expr.Return,
        ),
        'loc_A78',
    )

    ChrSetFlags(0x0011, 0x0080)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetFlags(0x0013, 0x0080)
    ChrSetFlags(0x0015, 0x0080)
    ChrSetFlags(0x0016, 0x0080)
    ChrSetFlags(0x0017, 0x0080)
    ChrSetFlags(0x0018, 0x0080)
    ChrSetFlags(0x0019, 0x0080)
    ChrSetFlags(0x001A, 0x0080)
    ChrSetFlags(0x001B, 0x0080)
    ChrSetFlags(0x001D, 0x0080)
    TerminateThread(0x0008, 0xFF)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetFlags(0x0008, 0x0010)
    ChrSetChipByIndex(0x0008, 32)

    def _loc_A78(): pass

    label('loc_A78')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000072, 'loc_A84'),
        (-1, 'loc_AB5'),
    )

    def _loc_A84(): pass

    label('loc_A84')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 6, 0x42E)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_AB2',
    )

    SetScenaFlags(ScenaFlag(0x0085, 7, 0x42F))
    OP_71(0x0001, 0x0010)
    OP_71(0x0002, 0x0010)
    OP_71(0x0003, 0x0010)
    OP_64(0x00, 0x0001)
    OP_64(0x01, 0x0001)
    OP_64(0x02, 0x0001)
    Event(0, func_16_399B)

    def _loc_AB2(): pass

    label('loc_AB2')

    Jump('loc_AB5')

    def _loc_AB5(): pass

    label('loc_AB5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_ADB',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    ChrSetFlags(0x001A, 0x0080)
    ChrSetFlags(0x001B, 0x0080)
    ChrSetFlags(0x001D, 0x0080)
    Event(0, func_17_4225)
    OP_B1('t2510_n')

    def _loc_ADB(): pass

    label('loc_ADB')

    Return()

# id: 0x0001 offset: 0xADC
@scena.Code('func_01_ADC')
def func_01_ADC():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Or,
            Expr.Return,
        ),
        'loc_AFD',
    )

    OP_B1('t2510_y')

    Jump('loc_B06')

    def _loc_AFD(): pass

    label('loc_AFD')

    OP_B1('t2510_n')

    def _loc_B06(): pass

    label('loc_B06')

    OP_64(0x00, 0x0001)
    OP_64(0x01, 0x0001)
    OP_64(0x02, 0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_B39',
    )

    OP_72(0x0001, 0x0010)
    OP_72(0x0002, 0x0010)
    OP_72(0x0003, 0x0010)
    OP_65(0x00, 0x0001)
    OP_65(0x01, 0x0001)
    OP_65(0x02, 0x0001)

    def _loc_B39(): pass

    label('loc_B39')

    OP_64(0x05, 0x0001)

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0020)"),
            Expr.Return,
        ),
        'loc_B4C',
    )

    OP_65(0x05, 0x0001)

    def _loc_B4C(): pass

    label('loc_B4C')

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0080)"),
            Expr.Return,
        ),
        'loc_B60',
    )

    OP_64(0x05, 0x0001)
    ChrSetFlags(0x0022, 0x0080)

    def _loc_B60(): pass

    label('loc_B60')

    Return()

# id: 0x0002 offset: 0xB61
@scena.Code('func_02_B61')
def func_02_B61():
    ExecExpressionWithReg(
        0x0000,
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
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B86',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_CC8')

    def _loc_B86(): pass

    label('loc_B86')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B9F',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_CC8')

    def _loc_B9F(): pass

    label('loc_B9F')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BB8',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_CC8')

    def _loc_BB8(): pass

    label('loc_BB8')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BD1',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_CC8')

    def _loc_BD1(): pass

    label('loc_BD1')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BEA',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_CC8')

    def _loc_BEA(): pass

    label('loc_BEA')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C03',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_CC8')

    def _loc_C03(): pass

    label('loc_C03')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C1C',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_CC8')

    def _loc_C1C(): pass

    label('loc_C1C')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C35',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_CC8')

    def _loc_C35(): pass

    label('loc_C35')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C4E',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_CC8')

    def _loc_C4E(): pass

    label('loc_C4E')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C67',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_CC8')

    def _loc_C67(): pass

    label('loc_C67')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C80',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_CC8')

    def _loc_C80(): pass

    label('loc_C80')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C99',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_CC8')

    def _loc_C99(): pass

    label('loc_C99')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CB2',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_CC8')

    def _loc_CB2(): pass

    label('loc_CB2')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CC8',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_CC8(): pass

    label('loc_CC8')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_CDD',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_CC8')

    def _loc_CDD(): pass

    label('loc_CDD')

    Return()

# id: 0x0003 offset: 0xCDE
@scena.Code('func_03_CDE')
def func_03_CDE():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_EBE',
    )

    ChrClearFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x87),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_D0A',
    )

    ChrSetSubChip(0x00FE, 1)

    Jump('loc_D25')

    def _loc_D0A(): pass

    label('loc_D0A')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_D20',
    )

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_D25')

    def _loc_D20(): pass

    label('loc_D20')

    ChrSetSubChip(0x00FE, 2)

    def _loc_D25(): pass

    label('loc_D25')

    ChrSetDirection(0x00FE, 180, 0)
    ChrSetFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E35',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '#0530060093V#782F哦哦，是艾丝蒂尔和约修亚啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530060094V我和戴尔蒙市长交往多年了，\n',
            '自己也对这次事件深感震惊。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530060095V#783F他的行为的确难以原谅，\n',
            '而且也没有人会原谅他……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530060096V我祈祷他能对自己\n',
            '误入歧途犯下的罪行感到忏悔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EB6')

    def _loc_E35(): pass

    label('loc_E35')

    ChrTalk(
        0x00FE,
        (
            '#0530060097V#783F他的行为的确难以原谅，\n',
            '而且也没有人会原谅他……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530060098V我祈祷他能对自己\n',
            '误入歧途犯下的罪行感到忏悔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EB6(): pass

    label('loc_EB6')

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_1385')

    def _loc_EBE(): pass

    label('loc_EBE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_1084',
    )

    ChrClearFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x87),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_EE7',
    )

    ChrSetSubChip(0x00FE, 1)

    Jump('loc_F02')

    def _loc_EE7(): pass

    label('loc_EE7')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_EFD',
    )

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_F02')

    def _loc_EFD(): pass

    label('loc_EFD')

    ChrSetSubChip(0x00FE, 2)

    def _loc_F02(): pass

    label('loc_F02')

    ChrSetDirection(0x00FE, 180, 0)
    ChrSetFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1009',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '#0530060087V#780F艾丝蒂尔、约修亚。\n',
            '这次实在是麻烦你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530060088V舞台剧我看了哦，\n',
            '真的是十分精彩。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530060089V特别是约修亚饰演的塞茜莉亚公主，\n',
            '演技和扮相实在是太感人了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530060090V下次有机会的话\n',
            '请务必再到我们学院来玩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_107C')

    def _loc_1009(): pass

    label('loc_1009')

    ChrTalk(
        0x00FE,
        (
            '#0530060091V#780F话说回来，\n',
            '能帮上特蕾莎老师实在是太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530060092V那次纵火事件实在让孩子们受苦了啊。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_107C(): pass

    label('loc_107C')

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_1385')

    def _loc_1084(): pass

    label('loc_1084')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_1159',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1112',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '#0530850007V#780F哦，是你们。\n',
            '这次真是史无前例的盛况啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530060102V大家都很期待舞台剧，\n',
            '请务必让学园祭圆满成功。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1156')

    def _loc_1112(): pass

    label('loc_1112')

    ChrTalk(
        0x00FE,
        (
            '#0530060103V#780F大家都很期待舞台剧。\n',
            '请务必让学园祭圆满成功。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1156(): pass

    label('loc_1156')

    Jump('loc_1385')

    def _loc_1159(): pass

    label('loc_1159')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_12BB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_123C',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '#780F戴尔蒙市长，\n',
            '自从去年的王国会议之后我们也好久不见了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530060080V这段时间，你身体怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0021,
        (
            '#660F就像你看到的，结实着呢。\n',
            '科林兹校长也很精神嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0490060082V今天我打算好好放松一下。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0008, 0x0010)

    Jump('loc_12B8')

    def _loc_123C(): pass

    label('loc_123C')

    ChrTalk(
        0x00FE,
        (
            '#780F我还要找时间和市长先生谈谈\n',
            '关于学院运营的事情呢。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530850008V虽说是王立的教育机构，\n',
            '但也要重视地方上的建议。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12B8(): pass

    label('loc_12B8')

    Jump('loc_1385')

    def _loc_12BB(): pass

    label('loc_12BB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_1385',
    )

    ChrClearFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x87),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_12E4',
    )

    ChrSetSubChip(0x00FE, 1)

    Jump('loc_12FF')

    def _loc_12E4(): pass

    label('loc_12E4')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_12FA',
    )

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_12FF')

    def _loc_12FA(): pass

    label('loc_12FA')

    ChrSetSubChip(0x00FE, 2)

    def _loc_12FF(): pass

    label('loc_12FF')

    ChrSetDirection(0x00FE, 180, 0)
    ChrSetFlags(0x00FE, 0x0010)

    ChrTalk(
        0x00FE,
        (
            '#0530060085V#780F你们住宿的地方我们已经给安排好了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530060086V学院里也有食堂，\n',
            '你们就安心准备好舞台剧吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x00FE, 0)

    def _loc_1385(): pass

    label('loc_1385')

    TalkEnd(0x0008)

    Return()

# id: 0x0004 offset: 0x1389
@scena.Code('func_04_1389')
def func_04_1389():
    Call(0, 0x0005)

    Return()

# id: 0x0005 offset: 0x138E
@scena.Code('func_05_138E')
def func_05_138E():
    TalkBegin(0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_1436',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_13FD',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0010,
        (
            '啊，怎么了？\n',
            '你们要找人吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '现在正好是\n',
            '上课结束的时间。\n',
            '我想大家都在校园里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1433')

    def _loc_13FD(): pass

    label('loc_13FD')

    ChrTalk(
        0x0010,
        (
            '现在正好是\n',
            '上课结束的时间。\n',
            '我想大家都在校园里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1433(): pass

    label('loc_1433')

    Jump('loc_1A46')

    def _loc_1436(): pass

    label('loc_1436')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_1481',
    )

    ChrTalk(
        0x0010,
        (
            '呵呵，学园祭很成功呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '学生们正在\n',
            '礼堂那里庆祝胜利呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A46')

    def _loc_1481(): pass

    label('loc_1481')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
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
        'loc_14EA',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0010,
        (
            '说起来\n',
            '真是出乎意料的盛况啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '有很多带孩子来的家长，\n',
            '我担心会有孩子走失。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_152B')

    def _loc_14EA(): pass

    label('loc_14EA')

    ChrTalk(
        0x0010,
        (
            '请问您想找哪位呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '我可以使用广播\n',
            '来帮您寻找想找的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_152B(): pass

    label('loc_152B')

    Jump('loc_1A46')

    def _loc_152E(): pass

    label('loc_152E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_15F7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_15BC',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0010,
        (
            '各种活动都在\n',
            '校园和主楼里进行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '下午礼堂那边\n',
            '预定要演出舞台剧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '食堂作为休息场所开放，\n',
            '你们可以好好利用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15F4')

    def _loc_15BC(): pass

    label('loc_15BC')

    ChrTalk(
        0x0010,
        (
            '为了以防万一，\n',
            '学园祭举行的时候\n',
            '宿舍楼都是锁住的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15F4(): pass

    label('loc_15F4')

    Jump('loc_1A46')

    def _loc_15F7(): pass

    label('loc_15F7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_1688',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_165C',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0010,
        (
            '准备完成了吗？\n',
            '明天就要正式表演了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '到了明天\n',
            '就会有许多客人来参观了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1685')

    def _loc_165C(): pass

    label('loc_165C')

    ChrTalk(
        0x0010,
        (
            '准备完成了吗？\n',
            '明天就要正式表演了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1685(): pass

    label('loc_1685')

    Jump('loc_1A46')

    def _loc_1688(): pass

    label('loc_1688')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_1741',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1705',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0010,
        (
            '一到下课时间，\n',
            '校园里就会变得热闹起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '离学园祭没多久了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '同学们也都在\n',
            '拼命加油呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_173E')

    def _loc_1705(): pass

    label('loc_1705')

    ChrTalk(
        0x0010,
        (
            '离学园祭没多久了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '同学们也都在\n',
            '拼命加油呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_173E(): pass

    label('loc_173E')

    Jump('loc_1A46')

    def _loc_1741(): pass

    label('loc_1741')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 6, 0x42E)),
            Expr.Return,
        ),
        'loc_1865',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1819',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    ChrTurnDirection(0x0010, 0x0105, 0)

    ChrTalk(
        0x0010,
        (
            '啊，科洛丝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F对不起，珐奥娜，\n',
            '我到现在才回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '呵呵，回来就好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '要找校长的话，\n',
            '他就在办公室里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '他也很担心\n',
            '科洛丝你呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F啊，是的。\n',
            '我们现在就过去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1862')

    def _loc_1819(): pass

    label('loc_1819')

    ChrTurnDirection(0x0010, 0x0105, 0)

    ChrTalk(
        0x0010,
        (
            '要找校长的话，\n',
            '他就在办公室里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '他也很担心\n',
            '科洛丝你呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1862(): pass

    label('loc_1862')

    Jump('loc_1A46')

    def _loc_1865(): pass

    label('loc_1865')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_191C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_18F6',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0010,
        (
            '啊，科洛丝。\n',
            '你外出回来了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F啊，不是的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '对不起，\n',
            '我们还没有办完事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '是吗。\n',
            '外出时请务必要小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1919')

    def _loc_18F6(): pass

    label('loc_18F6')

    ChrTalk(
        0x0010,
        (
            '科洛丝，\n',
            '外出时请务必要小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1919(): pass

    label('loc_1919')

    Jump('loc_1A46')

    def _loc_191C(): pass

    label('loc_191C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 6, 0x41E)),
            Expr.Return,
        ),
        'loc_196E',
    )

    ChrTalk(
        0x0010,
        (
            '啊，是想参观吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '很抱歉，\n',
            '现在学生们正在上课，\n',
            '不能带您参观。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A46')

    def _loc_196E(): pass

    label('loc_196E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_1A46',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A16',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0010,
        (
            '啊，科洛丝。\n',
            '已经回来了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F不是，\n',
            '我正要带这两位朋友去卢安呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '是吗，难得的假日，\n',
            '就好好地放松一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F嗯，谢谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A46')

    def _loc_1A16(): pass

    label('loc_1A16')

    ChrTalk(
        0x0010,
        (
            '科洛丝，\n',
            '难得的假日，\n',
            '就好好地放松一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A46(): pass

    label('loc_1A46')

    TalkEnd(0x0010)

    Return()

# id: 0x0006 offset: 0x1A4A
@scena.Code('func_06_1A4A')
def func_06_1A4A():
    TalkBegin(0x0011)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_1A86',
    )

    ChrTalk(
        0x00FE,
        (
            '课虽然上完了，\n',
            '但还有学生们的问题要回答。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CC7')

    def _loc_1A86(): pass

    label('loc_1A86')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_1AD8',
    )

    ChrTalk(
        0x00FE,
        (
            '唔，\n',
            '我们班的同学干劲热火朝天啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家做布景\n',
            '也非常地努力嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CC7')

    def _loc_1AD8(): pass

    label('loc_1AD8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_1B28',
    )

    ChrTalk(
        0x00FE,
        (
            '学园祭的主角\n',
            '果然还是学生们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家都比平时\n',
            '要活跃许多呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CC7')

    def _loc_1B28(): pass

    label('loc_1B28')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_1C08',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1BC6',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '你们好像是\n',
            '从洛连特来的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '其实我也是\n',
            '洛连特出身的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说起来我父母\n',
            '也要来参观学园祭呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……我要是能招待他们就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C05')

    def _loc_1BC6(): pass

    label('loc_1BC6')

    ChrTalk(
        0x00FE,
        (
            '对了对了……\n',
            '舞台剧表演我也看了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那天真是很开心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C05(): pass

    label('loc_1C05')

    Jump('loc_1CC7')

    def _loc_1C08(): pass

    label('loc_1C08')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_1CC7',
    )

    ChrClearFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1C31',
    )

    ChrSetSubChip(0x00FE, 1)

    Jump('loc_1C62')

    def _loc_1C31(): pass

    label('loc_1C31')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x87),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1C47',
    )

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_1C62')

    def _loc_1C47(): pass

    label('loc_1C47')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x10E),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1C5D',
    )

    ChrSetSubChip(0x00FE, 2)

    Jump('loc_1C62')

    def _loc_1C5D(): pass

    label('loc_1C5D')

    ChrSetSubChip(0x00FE, 1)

    def _loc_1C62(): pass

    label('loc_1C62')

    ChrSetDirection(0x00FE, 90, 0)
    ChrSetFlags(0x00FE, 0x0010)

    ChrTalk(
        0x00FE,
        (
            '学园祭快到了，\n',
            '同学们就连上课\n',
            '都开始坐不安定了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，这也是没办法的呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x00FE, 0)

    def _loc_1CC7(): pass

    label('loc_1CC7')

    TalkEnd(0x0011)

    Return()

# id: 0x0007 offset: 0x1CCB
@scena.Code('func_07_1CCB')
def func_07_1CCB():
    TalkBegin(0x0012)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_1D77',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D4D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '唔唔，\n',
            '这个问题……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0012, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '怎么做好呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0012, 0x0010)

    Jump('loc_1D74')

    def _loc_1D4D(): pass

    label('loc_1D4D')

    ChrTalk(
        0x00FE,
        (
            '呼，这里的学生\n',
            '都很热心于学习呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D74(): pass

    label('loc_1D74')

    Jump('loc_1FAA')

    def _loc_1D77(): pass

    label('loc_1D77')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_1DD9',
    )

    ChrTalk(
        0x00FE,
        (
            '下午终于要上演\n',
            '万众瞩目的舞台剧了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '拜托你们二位了！\n',
            '我相信一定能取得成功的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1FAA')

    def _loc_1DD9(): pass

    label('loc_1DD9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_1E87',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1E63',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '嗯，\n',
            '我们班的同学相当认真呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然我觉得\n',
            '研究发表什么的太朴素了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过这样也好，\n',
            '有很多客人来看呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E84')

    def _loc_1E63(): pass

    label('loc_1E63')

    ChrTalk(
        0x00FE,
        (
            '决不能输给\n',
            '米丽亚的班级……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E84(): pass

    label('loc_1E84')

    Jump('loc_1FAA')

    def _loc_1E87(): pass

    label('loc_1E87')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_1FAA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1F83',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    ChrTurnDirection(0x00FE, 0x0105, 0)

    ChrTalk(
        0x00FE,
        (
            '啊，科洛丝。\n',
            '你回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F碧欧拉老师，\n',
            '我刚刚才回来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '对不起……\n',
            '我又没来上课。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，没关系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你不是有重要的事情吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有时间的话来一下办公室，\n',
            '我给你漏下的上课笔记。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F嗯，我过会儿就去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1FAA')

    def _loc_1F83(): pass

    label('loc_1F83')

    ChrTalk(
        0x00FE,
        (
            '我还是趁现在\n',
            '批改一下考试卷子吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1FAA(): pass

    label('loc_1FAA')

    TalkEnd(0x0012)

    Return()

# id: 0x0008 offset: 0x1FAE
@scena.Code('func_08_1FAE')
def func_08_1FAE():
    TalkBegin(0x0013)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_2068',
    )

    ChrClearFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1FDA',
    )

    ChrSetSubChip(0x00FE, 1)

    Jump('loc_200B')

    def _loc_1FDA(): pass

    label('loc_1FDA')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x87),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1FF0',
    )

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_200B')

    def _loc_1FF0(): pass

    label('loc_1FF0')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x10E),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2006',
    )

    ChrSetSubChip(0x00FE, 2)

    Jump('loc_200B')

    def _loc_2006(): pass

    label('loc_2006')

    ChrSetSubChip(0x00FE, 1)

    def _loc_200B(): pass

    label('loc_200B')

    ChrSetDirection(0x00FE, 90, 0)
    ChrSetFlags(0x00FE, 0x0010)

    ChrTalk(
        0x00FE,
        (
            '我是今年\n',
            '入学考试的出题老师。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我已经跃跃欲试了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x00FE, 0)

    Jump('loc_2320')

    def _loc_2068(): pass

    label('loc_2068')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_2105',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_20D7',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '为什么我们班的同学\n',
            '尽办些游戏和占卜的活动……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '维奥拉的班级\n',
            '都是很正经的东西呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2102')

    def _loc_20D7(): pass

    label('loc_20D7')

    ChrTalk(
        0x00FE,
        (
            '那个班的老师不行，\n',
            '学生们却都很优秀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2102(): pass

    label('loc_2102')

    Jump('loc_2320')

    def _loc_2105(): pass

    label('loc_2105')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_2139',
    )

    ChrTalk(
        0x00FE,
        (
            '人还真是多呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家都很闲吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2320')

    def _loc_2139(): pass

    label('loc_2139')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_21D6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_21A4',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '嗯，明天就能好好看到\n',
            '同学们努力的成果了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '无论怎样，\n',
            '那天我可不能再啰嗦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_21D3')

    def _loc_21A4(): pass

    label('loc_21A4')

    ChrTalk(
        0x00FE,
        (
            '嗯，明天就能好好看到\n',
            '同学们努力的成果了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_21D3(): pass

    label('loc_21D3')

    Jump('loc_2320')

    def _loc_21D6(): pass

    label('loc_21D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_2320',
    )

    ChrClearFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_21FF',
    )

    ChrSetSubChip(0x00FE, 1)

    Jump('loc_2230')

    def _loc_21FF(): pass

    label('loc_21FF')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x87),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2215',
    )

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_2230')

    def _loc_2215(): pass

    label('loc_2215')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x10E),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_222B',
    )

    ChrSetSubChip(0x00FE, 2)

    Jump('loc_2230')

    def _loc_222B(): pass

    label('loc_222B')

    ChrSetSubChip(0x00FE, 1)

    def _loc_2230(): pass

    label('loc_2230')

    ChrSetDirection(0x00FE, 90, 0)
    ChrSetFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_22C5',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '在学园祭的准备期间，\n',
            '大家学习都提不起精神来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就算在课上\n',
            '也开始不愿动脑筋了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要不要明天\n',
            '来次突击测验呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_231B')

    def _loc_22C5(): pass

    label('loc_22C5')

    ChrTalk(
        0x00FE,
        (
            '在学园祭的准备期间，\n',
            '大家学习都提不起精神来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要不要明天\n',
            '来次突击测验呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_231B(): pass

    label('loc_231B')

    ChrSetSubChip(0x00FE, 0)

    def _loc_2320(): pass

    label('loc_2320')

    TalkEnd(0x0013)

    Return()

# id: 0x0009 offset: 0x2324
@scena.Code('func_09_2324')
def func_09_2324():
    TalkBegin(0x0014)
    ChrClearFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x5A),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2349',
    )

    ChrSetSubChip(0x00FE, 2)

    Jump('loc_237A')

    def _loc_2349(): pass

    label('loc_2349')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_235F',
    )

    ChrSetSubChip(0x00FE, 1)

    Jump('loc_237A')

    def _loc_235F(): pass

    label('loc_235F')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2375',
    )

    ChrSetSubChip(0x00FE, 0)

    Jump('loc_237A')

    def _loc_2375(): pass

    label('loc_2375')

    ChrSetSubChip(0x00FE, 2)

    def _loc_237A(): pass

    label('loc_237A')

    ChrSetDirection(0x00FE, 270, 0)
    ChrSetFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_23D1',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，差不多该去巡视了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我要看看\n',
            '有没有同学太过懒散了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2657')

    def _loc_23D1(): pass

    label('loc_23D1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_24C1',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_244F',
    )

    ChrTalk(
        0x00FE,
        (
            '哦，昨天真是辛苦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我真是个不称职的老师啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了防止再发生突发事件，\n',
            '我在这里待命。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24BE')

    def _loc_244F(): pass

    label('loc_244F')

    ChrTalk(
        0x00FE,
        (
            '昨天，\n',
            '有学生说在旧校舍看到了魔兽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了慎重起见，\n',
            '我把旧校舍的门锁紧了。\n',
            '不过一会儿还是再去看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_24BE(): pass

    label('loc_24BE')

    Jump('loc_2657')

    def _loc_24C1(): pass

    label('loc_24C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 6, 0x42E)),
            Expr.Return,
        ),
        'loc_25CA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2563',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '这个学园一共设立了\n',
            '三个方向的专业。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我教的科目则是\n',
            '所有专业都必修的科目——体育。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在这个时候我没有课，\n',
            '就来整理一下教案了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25C7')

    def _loc_2563(): pass

    label('loc_2563')

    ChrTalk(
        0x00FE,
        (
            '我教的科目则是\n',
            '所有专业都必修的科目——体育。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在这个时候我没有课，\n',
            '就来整理一下教案了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_25C7(): pass

    label('loc_25C7')

    Jump('loc_2657')

    def _loc_25CA(): pass

    label('loc_25CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_2657',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2636',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '唔，怎么，\n',
            '你们是哪个班的学生？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在正在上课哦。\n',
            '要有外出许可证\n',
            '才能出去哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2657')

    def _loc_2636(): pass

    label('loc_2636')

    ChrTalk(
        0x00FE,
        (
            '要有外出许可证\n',
            '才能出去哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2657(): pass

    label('loc_2657')

    ChrSetSubChip(0x00FE, 0)
    TalkEnd(0x0014)

    Return()

# id: 0x000A offset: 0x2660
@scena.Code('func_0A_2660')
def func_0A_2660():
    TalkBegin(0x0015)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_26D8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_26B6',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '呼～\n',
            '今天的课总算上完了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '下午的课\n',
            '一定会睡着的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26D5')

    def _loc_26B6(): pass

    label('loc_26B6')

    ChrTalk(
        0x00FE,
        (
            '下午的课\n',
            '一定会睡着的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_26D5(): pass

    label('loc_26D5')

    Jump('loc_2795')

    def _loc_26D8(): pass

    label('loc_26D8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_2795',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_274F',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '我一直在照顾\n',
            '我们社团的店面呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '班里的活动\n',
            '就没办法参加了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，感觉真是很充实呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2795')

    def _loc_274F(): pass

    label('loc_274F')

    ChrTalk(
        0x00FE,
        (
            '我一直在照顾\n',
            '我们社团的店面呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '班里的活动\n',
            '就没办法参加了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2795(): pass

    label('loc_2795')

    TalkEnd(0x0015)

    Return()

# id: 0x000B offset: 0x2799
@scena.Code('func_0B_2799')
def func_0B_2799():
    TalkBegin(0x0016)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_27E5',
    )

    ChrTalk(
        0x00FE,
        (
            '那么，该去社团活动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天要把\n',
            '画到一半的绘画完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29D9')

    def _loc_27E5(): pass

    label('loc_27E5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_2828',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，\n',
            '茶座还是要办成这样才对啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '辛苦也值得了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29D9')

    def _loc_2828(): pass

    label('loc_2828')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_2880',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，不管怎么说\n',
            '准备工作还是赶上了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为通宵工作，\n',
            '现在好困啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29D9')

    def _loc_2880(): pass

    label('loc_2880')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_291A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_28CF',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '唔哇哇！\n',
            '怎么回事！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呆在这里\n',
            '会来不及准备的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2917')

    def _loc_28CF(): pass

    label('loc_28CF')

    ChrTalk(
        0x00FE,
        (
            '……难道说\n',
            '这样下去要通宵赶工了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '做衣服花了太多时间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2917(): pass

    label('loc_2917')

    Jump('loc_29D9')

    def _loc_291A(): pass

    label('loc_291A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_29D9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2985',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '啦啦啦～～⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我正在做\n',
            '摆摊时穿的衣服。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔～就是要在\n',
            '这种时候集中精力！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29D9')

    def _loc_2985(): pass

    label('loc_2985')

    ChrTalk(
        0x00FE,
        (
            '因为做这种东西\n',
            '是我最喜欢干的事情了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对了对了，\n',
            '接下来还要做房间的装饰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_29D9(): pass

    label('loc_29D9')

    TalkEnd(0x0016)

    Return()

# id: 0x000C offset: 0x29DD
@scena.Code('func_0C_29DD')
def func_0C_29DD():
    TalkBegin(0x0017)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_2A23',
    )

    ChrTalk(
        0x00FE,
        (
            '欢迎光临～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果需要的话，\n',
            '我可以帮你们找空位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B51')

    def _loc_2A23(): pass

    label('loc_2A23')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_2A69',
    )

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，这件制服很可爱吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '坎诺还为我准备了好多呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B51')

    def _loc_2A69(): pass

    label('loc_2A69')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_2AD3',
    )

    ChrTalk(
        0x00FE,
        (
            '一想时间还很充裕\n',
            '就不由自主地松懈了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过应该还来得及。\n',
            '努力把店面打扮得漂亮一些吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B51')

    def _loc_2AD3(): pass

    label('loc_2AD3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_2B51',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2B24',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '坎诺君的手\n',
            '可巧啦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次他缝了个\n',
            '布娃娃给我呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B51')

    def _loc_2B24(): pass

    label('loc_2B24')

    ChrTalk(
        0x00FE,
        (
            '就算是演出用的女佣服装\n',
            '也是他自己做的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B51(): pass

    label('loc_2B51')

    TalkEnd(0x0017)

    Return()

# id: 0x000D offset: 0x2B55
@scena.Code('func_0D_2B55')
def func_0D_2B55():
    TalkBegin(0x0018)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_2B9E',
    )

    ChrTalk(
        0x00FE,
        (
            '就算是再微小的问题，\n',
            '拉迪奥老师也会\n',
            '很仔细地给我讲解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C6F')

    def _loc_2B9E(): pass

    label('loc_2B9E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_2C6F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2C2A',
    )

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))

    ChrTalk(
        0x00FE,
        (
            '社会系各位的作品\n',
            '都是研究成果发表啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哇……真是厉害啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们系的同学\n',
            '只会办茶座或者\n',
            '鬼怪屋什么的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C6F')

    def _loc_2C2A(): pass

    label('loc_2C2A')

    ChrTalk(
        0x00FE,
        (
            '社会系各位的作品\n',
            '都是研究成果发表啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哇……真是厉害啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C6F(): pass

    label('loc_2C6F')

    TalkEnd(0x0018)

    Return()

# id: 0x000E offset: 0x2C73
@scena.Code('func_0E_2C73')
def func_0E_2C73():
    TalkBegin(0x0019)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_2CAD',
    )

    ChrTalk(
        0x00FE,
        (
            '欢迎光临。\n',
            '这里是我们的茶座『芳塔娜』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2CF0')

    def _loc_2CAD(): pass

    label('loc_2CAD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_2CF0',
    )

    ChrTalk(
        0x00FE,
        (
            '穿成这个样子\n',
            '虽然有点不好意思，\n',
            '但为了学园祭，忍了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2CF0(): pass

    label('loc_2CF0')

    TalkEnd(0x0019)

    Return()

# id: 0x000F offset: 0x2CF4
@scena.Code('func_0F_2CF4')
def func_0F_2CF4():
    TalkBegin(0x001A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_2D28',
    )

    ChrTalk(
        0x00FE,
        (
            '唔，\n',
            '今天也是很有意义的一课啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_32D8')

    def _loc_2D28(): pass

    label('loc_2D28')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_2E34',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2DE3',
    )

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '虽然办娱乐活动很有意思，\n',
            '不过让大家知道我们\n',
            '平日的研究成果也是很重要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '尤其是有很多前辈\n',
            '和市民们前来参观。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……虽说如此，\n',
            '考试也不会得到更高的分数。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E31')

    def _loc_2DE3(): pass

    label('loc_2DE3')

    ChrTalk(
        0x00FE,
        (
            '虽然办娱乐活动很有意思，\n',
            '不过让大家知道我们\n',
            '平日的研究成果也是很重要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2E31(): pass

    label('loc_2E31')

    Jump('loc_32D8')

    def _loc_2E34(): pass

    label('loc_2E34')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_30D0',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x1000)"),
            Expr.Return,
        ),
        'loc_2F1F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2EFA',
    )

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '我们社会系发表了\n',
            '从各种产业的经济指标上\n',
            '进行经济动向的预测的研究。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且也收集了\n',
            '通俗易懂的关于卢安地区\n',
            '历史和发展的资料。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果有兴趣的话就请看一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F1C')

    def _loc_2EFA(): pass

    label('loc_2EFA')

    ChrTalk(
        0x00FE,
        (
            '如果有兴趣的话就请看一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2F1C(): pass

    label('loc_2F1C')

    Jump('loc_30CD')

    def _loc_2F1F(): pass

    label('loc_2F1F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3023',
    )

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '我们社会系发表了\n',
            '从各种产业的经济指标上\n',
            '进行经济动向的预测的研究。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且也收集了\n',
            '通俗易懂的关于卢安地区\n',
            '历史和发展的资料。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然有几份资料没到手，\n',
            '但在这么点时间里，\n',
            '能做成这么完善的内容也算不错了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果有兴趣的话就请看一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_30CD')

    def _loc_3023(): pass

    label('loc_3023')

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0020)"),
            Expr.Return,
        ),
        'loc_30AB',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然没赶上这次发表，\n',
            '但是《卢安经济史》是很贵重的资料。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果你们看到那三本书的话，\n',
            '麻烦帮我放回资料室的书架上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_30CD')

    def _loc_30AB(): pass

    label('loc_30AB')

    ChrTalk(
        0x00FE,
        (
            '如果有兴趣的话就请看一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_30CD(): pass

    label('loc_30CD')

    Jump('loc_32D8')

    def _loc_30D0(): pass

    label('loc_30D0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_3187',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_315B',
    )

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))

    ChrTalk(
        0x00FE,
        (
            '唔，\n',
            '还是需要一些辅助研究的资料啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '时间不够了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过在有限的时间里，\n',
            '内容已经可算是做得很完善了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3184')

    def _loc_315B(): pass

    label('loc_315B')

    ChrTalk(
        0x00FE,
        (
            '唔，\n',
            '还是需要一些辅助研究的资料啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3184(): pass

    label('loc_3184')

    Jump('loc_32D8')

    def _loc_3187(): pass

    label('loc_3187')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_32D8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_32B3',
    )

    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))
    ChrTurnDirection(0x00FE, 0x0105, 0)

    ChrTalk(
        0x00FE,
        (
            '啊，科洛丝。\n',
            '你终于回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们班级的节目\n',
            '准备工作进展得很顺利啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们舞台剧方面怎么样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听说连主要演员\n',
            '都还没决定下来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F呵呵，罗基克，\n',
            '那件事已经解决了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '舞台剧方面我们不会输的。\n',
            '敬请期待哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哦，是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那我们互相加油吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_32D8')

    def _loc_32B3(): pass

    label('loc_32B3')

    ChrTurnDirection(0x00FE, 0x0105, 0)

    ChrTalk(
        0x00FE,
        (
            '科洛丝，我们互相加油吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_32D8(): pass

    label('loc_32D8')

    TalkEnd(0x001A)

    Return()

# id: 0x0010 offset: 0x32DC
@scena.Code('func_10_32DC')
def func_10_32DC():
    TalkBegin(0x001B)

    ChrTalk(
        0x00FE,
        (
            '这次的女王诞辰庆典上\n',
            '要召开武术大会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们的击剑部\n',
            '也好想参加啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x001B)

    Return()

# id: 0x0011 offset: 0x332F
@scena.Code('func_11_332F')
def func_11_332F():
    TalkBegin(0x001C)

    ChrTalk(
        0x00FE,
        (
            '啊，老师，是这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从这里开始\n',
            '就完全不明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x001C)

    Return()

# id: 0x0012 offset: 0x336F
@scena.Code('func_12_336F')
def func_12_336F():
    TalkBegin(0x001D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_33C6',
    )

    ChrTalk(
        0x00FE,
        (
            '啊～\n',
            '今天是弓道部的练习日。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一直在准备学园祭，\n',
            '好久没有休息了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_348C')

    def _loc_33C6(): pass

    label('loc_33C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3442',
    )

    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))
    ChrTurnDirection(0x00FE, 0x0105, 0)

    ChrTalk(
        0x00FE,
        (
            '啊，科洛丝。\n',
            '你回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们差不多\n',
            '该开始装饰教室了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '先从可以着手的地方\n',
            '开始进行吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_348C')

    def _loc_3442(): pass

    label('loc_3442')

    ChrTalk(
        0x00FE,
        (
            '我们差不多\n',
            '该开始装饰教室了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '先从可以着手的地方\n',
            '开始进行吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_348C(): pass

    label('loc_348C')

    TalkEnd(0x001D)

    Return()

# id: 0x0013 offset: 0x3490
@scena.Code('func_13_3490')
def func_13_3490():
    TalkBegin(0x001E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_34E0',
    )

    ChrTalk(
        0x00FE,
        (
            '今天的课上完了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也没参加社团活动，\n',
            '那就快点回家去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_352F')

    def _loc_34E0(): pass

    label('loc_34E0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_352F',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，\n',
            '首先是要去采购呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要把列表上的东西\n',
            '都买过来就行了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_352F(): pass

    label('loc_352F')

    TalkEnd(0x001E)

    Return()

# id: 0x0014 offset: 0x3533
@scena.Code('func_14_3533')
def func_14_3533():
    TalkBegin(0x001F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_35DE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_35A3',
    )

    SetScenaFlags(ScenaFlag(0x0002, 0, 0x10))

    ChrTalk(
        0x00FE,
        (
            '唔，我正想要问老师\n',
            '没听明白的地方呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '米丽亚老师一上完课\n',
            '就马上回办公室了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_35DB')

    def _loc_35A3(): pass

    label('loc_35A3')

    ChrTalk(
        0x00FE,
        (
            '我答应今天要去\n',
            '姐姐的店里帮忙，\n',
            '必须快点回去了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_35DB(): pass

    label('loc_35DB')

    Jump('loc_36A4')

    def _loc_35DE(): pass

    label('loc_35DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_36A4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_367F',
    )

    SetScenaFlags(ScenaFlag(0x0002, 0, 0x10))

    ChrTalk(
        0x00FE,
        (
            '真是的，\n',
            '为什么你老是那么草率啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大家都很忙，\n',
            '人手也不足，\n',
            '你提高点效率好不好？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了买东西在卢安\n',
            '和学园之间往返了好几次呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_36A4')

    def _loc_367F(): pass

    label('loc_367F')

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '基诺奇奥做事真是很粗心呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_36A4(): pass

    label('loc_36A4')

    TalkEnd(0x001F)

    Return()

# id: 0x0015 offset: 0x36A8
@scena.Code('func_15_36A8')
def func_15_36A8():
    TalkBegin(0x0020)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_3997',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3913',
    )

    SetScenaFlags(ScenaFlag(0x0002, 1, 0x11))

    ChrTalk(
        0x0101,
        (
            '#0011350001V#000F啊，梅贝尔市长？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0361290001V#610F啊，是艾丝蒂尔和约修亚！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0011350002V#000F您为什么会在这里呢？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0361290002V#610F呵呵，其实我是\n',
            '这个学院的毕业生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360060144V每年的学园祭都要来出席的。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010060145V#000F哦，是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#610F那么你们俩是为什么来这儿的啊？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0011350003V#000F嘿嘿，其实呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔\n',
            '向梅贝尔市长说明了事情的经过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ChrTalk(
        0x00FE,
        (
            '#610F哦，是协助演出啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我也认为演出是很考功夫的。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360060151V呵呵，连艾丝蒂尔\n',
            '和约修亚也参加演出的话，\n',
            '那我真要好好看看才行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020990002V#010F（唉，真不想让\n',
            '认识的人看到啊……）',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_3997')

    def _loc_3913(): pass

    label('loc_3913')

    ChrTalk(
        0x00FE,
        (
            '#0360060153V#610F我也认为演出是很考功夫的。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0360060154V呵呵，连艾丝蒂尔\n',
            '和约修亚也参加演出的话，\n',
            '那我真要好好看看才行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3997(): pass

    label('loc_3997')

    TalkEnd(0x0020)

    Return()

# id: 0x0016 offset: 0x399B
@scena.Code('func_16_399B')
def func_16_399B():
    EventBegin(0x00)
    MapClearFlags(0x00000001)
    CameraMove(116280, 0, 2160, 0)
    ChrSetPos(0x0101, 117450, 0, -1700, 0)
    ChrSetPos(0x0102, 116510, 0, -1950, 0)
    ChrSetPos(0x0105, 117000, 0, -1020, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0105,
        (
            '#0060051020V#040F校长，您好。\n',
            '我已经回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3A28')
    def lambda_3A28():
        CameraMove(117230, 0, 4590, 2000)

        ExitThread()

    DispatchAsync(0x0105, 0x0002, lambda_3A28)

    @scena.Lambda('lambda_3A40')
    def lambda_3A40():
        ChrWalkTo(0x00FE, 116880, 0, 1680, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_3A40)

    Sleep(500)

    @scena.Lambda('lambda_3A60')
    def lambda_3A60():
        ChrWalkTo(0x00FE, 117520, 0, 1680, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3A60)

    Sleep(300)

    @scena.Lambda('lambda_3A80')
    def lambda_3A80():
        ChrWalkTo(0x00FE, 116300, 0, 1490, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3A80)

    WaitForThreadExit(0x0105, 0x0001)

    @scena.Lambda('lambda_3AA0')
    def lambda_3AA0():
        ChrWalkTo(0x00FE, 116110, 0, 2550, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_3AA0)

    WaitForThreadExit(0x0105, 0x0001)
    ChrSetDirection(0x0105, 0, 400)
    WaitForThreadExit(0x0101, 0x0001)
    ChrTurnDirection(0x0101, 0x0105, 400)
    WaitForThreadExit(0x0102, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#0530051021V#780F#1P科洛丝，你回来了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530051022V哎哟？这两位是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051023V#000F初次见面，校长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020051024V#010F我们是游击士协会的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0530051025V#780F#1P呵呵，如此年轻就成为游击士，\n',
            '的确是后生可畏啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530051026V听说孤儿院发生了火灾，\n',
            '莫非你们是为那件事而来的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051027V#049F#4P是的，其实……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '科洛丝向科林兹校长\n',
            '说明了包括纵火事件在内的一系列事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#0530051028V#780F#1P是吗……\n',
            '那事情可就严重了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530051029V要是我们也能以什么方式\n',
            '给院长和孩子们帮上忙就好了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530051030V…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530051031V那么首先，一定要办好学园祭，\n',
            '不能辜负那些孩子对我们的期待……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530051032V而且也只能从这里做起了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051033V#047F是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051034V#040F校长，有件事想和您说说。\n',
            '这次我想请艾丝蒂尔和约修亚\n',
            '来协助参演今年的舞台剧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0530051035V#781F#1P这想法不错嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530051036V#780F艾丝蒂尔、约修亚。\n',
            '这次的舞台剧就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051037V#006F啊，是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020051038V#010F我们愿尽绵薄之力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0530051039V#780F#1P与舞台剧相关的工作\n',
            '是由学生会长乔儿全权负责的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530051040V导演也由她担任，\n',
            '所以详细情形向她请教就行了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530051041V而我这里就……\n',
            '帮你们两位安排宿舍吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051042V#004F哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020051043V#014F宿舍？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0530051044V#780F#1P毕竟学园祭\n',
            '已经迫在眉睫了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530051045V恐怕每天都需要\n',
            '排练到很晚呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530051046V这样一来，\n',
            '就需要有个住的地方对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051047V#501F啊，原来是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020051048V#019F这样的确方便多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(138, 0x00, 0x64)
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0102, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0105, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0530051049V#780F#1P刚好也下课了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530051050V科洛丝，你就马上\n',
            '把他们介绍给学生会长吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060051051V#041F好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0105, 135, 400)

    ChrTalk(
        0x0105,
        (
            '#0060051052V#040F#1P艾丝蒂尔、约修亚。\n',
            '接下来我带你们去学生会室吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051053V这座主楼的右边是社团大楼，\n',
            '而学生会室就在大楼的第二层。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010051054V#006F嗯，那我们走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x003D, 0x01, 0x0008)
    OP_28(0x003D, 0x01, 0x0010)
    EventEnd(0x00)

    Return()

# id: 0x0017 offset: 0x4225
@scena.Code('func_17_4225')
def func_17_4225():
    EventBegin(0x00)
    OP_77(0xFF, 0xC8, 0x96, 0x00, 0x00000000)
    CameraMove(-1190, 0, 33250, 0)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetFlags(0x0009, 0x0004)
    ChrSetFlags(0x000A, 0x0004)
    ChrSetFlags(0x000B, 0x0004)
    ChrSetFlags(0x000C, 0x0004)
    ChrSetFlags(0x000D, 0x0004)
    ChrSetFlags(0x000E, 0x0004)
    ChrSetFlags(0x0105, 0x0004)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetFlags(0x0102, 0x0004)
    ChrSetChipByIndex(0x0101, 19)
    ChrSetChipByIndex(0x0102, 20)
    ChrSetChipByIndex(0x0105, 21)
    ChrSetChipByIndex(0x000B, 23)
    ChrSetChipByIndex(0x000C, 24)
    ChrSetChipByIndex(0x000D, 22)
    ChrSetChipByIndex(0x000E, 25)
    ChrSetPos(0x0101, 500, 200, 32060, 90)
    ChrSetPos(0x0102, 500, 200, 29980, 90)
    ChrSetPos(0x0105, 520, 200, 34100, 90)
    ChrSetPos(0x000A, -2750, 200, 30010, 90)
    ChrSetPos(0x0009, -2750, 200, 32060, 90)
    ChrSetPos(0x000C, -2750, 100, 34060, 90)
    ChrSetPos(0x000B, -5900, 100, 30010, 90)
    ChrSetPos(0x000D, -5900, 100, 34160, 90)
    ChrSetPos(0x000E, -5900, 100, 31920, 90)
    ChrSetPos(0x000F, 5300, 250, 32119, 90)

    @scena.Lambda('lambda_4364')
    def lambda_4364():
        CameraMove(3580, 0, 33240, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4364)

    FadeIn(2000, 0)
    ChrWalkTo(0x000F, 5390, 250, 30460, 1000, 0x00)
    ChrSetDirection(0x000F, 90, 400)
    Sleep(500)

    ChrWalkTo(0x000F, 5370, 250, 31960, 1000, 0x00)
    ChrSetDirection(0x000F, 90, 400)
    Sleep(500)

    ChrWalkTo(0x000F, 5390, 250, 30460, 1000, 0x00)
    ChrSetDirection(0x000F, 270, 400)
    Sleep(1000)

    @scena.Lambda('lambda_43E5')
    def lambda_43E5():
        CameraMove(2000, 0, 33250, 1500)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_43E5)

    ChrWalkTo(0x000F, 3370, 0, 30480, 2000, 0x00)
    ChrWalkTo(0x000F, 2570, 0, 31600, 2000, 0x00)
    ChrTurnDirection(0x000F, 0x0101, 400)
    ChrSetSubChip(0x0102, 1)
    Sleep(100)

    ChrSetSubChip(0x0105, 2)
    OP_62(0x000F, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1500)

    OP_63(0x000F)
    Sleep(500)

    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1500)

    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1500)

    OP_63(0x0101)
    Sleep(500)

    OP_62(0x000F, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    Sleep(1500)

    Sleep(500)

    ChrTurnDirection(0x000F, 0x0102, 400)
    ChrSetSubChip(0x0101, 2)
    Sleep(500)

    OP_62(0x000F, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1500)

    OP_63(0x000F)
    Sleep(500)

    OP_62(0x0102, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    OP_63(0x0102)
    Sleep(500)

    OP_62(0x000F, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    Sleep(1000)

    Sleep(500)

    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0105, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0009, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x000A, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x000B, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x000C, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x000D, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x000E, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(1500)

    FadeOut(1000, 0, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '上午，他们和其他学生一起\n',
            '在老师的教导下接受正统的课程教育……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T2511._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0018 offset: 0x4602
@scena.Code('func_18_4602')
def func_18_4602():
    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4689',
    )

    ChrTurnDirection(0x0105, 0x0001, 400)

    ChrTalk(
        0x0105,
        (
            '#0060051016V#040F对不起，\n',
            '现在正在上课。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060051017V我们先去校长办公室吧。\n',
            '就在这个建筑物的一楼走廊里面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_46D7')

    def _loc_4689(): pass

    label('loc_4689')

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020051018V#010F现在好像在上课。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020051019V先去校长办公室吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_46D7(): pass

    label('loc_46D7')

    TalkEnd(0x00FF)

    Return()

# id: 0x0019 offset: 0x46DB
@scena.Code('func_19_46DB')
def func_19_46DB():
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
            '　　保　\n',
            '　学持　\n',
            '　生安　\n',
            '　指静　\n',
            '　导！　\n',
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

# id: 0x001A offset: 0x4767
@scena.Code('func_1A_4767')
def func_1A_4767():
    PlaySE(17, 0x00, 0x64)
    ChrSetFlags(0x0022, 0x0080)
    OP_64(0x05, 0x0001)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '卢安经济史·中',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(0x033E, 1)
    OP_28(0x0027, 0x01, 0x0080)
    TalkEnd(0x00FF)

    Return()

# id: 0x001B offset: 0x47CD
@scena.Code('func_1B_47CD')
def func_1B_47CD():
    OP_13(0x006F)

    Return()

# id: 0x001C offset: 0x47D1
@scena.Code('func_1C_47D1')
def func_1C_47D1():
    OP_13(0x005E)

    Return()

# id: 0x001D offset: 0x47D5
@scena.Code('func_1D_47D5')
def func_1D_47D5():
    OP_13(0x006E)

    Return()

# id: 0x001E offset: 0x47D9
@scena.Code('func_1E_47D9')
def func_1E_47D9():
    OP_13(0x0074)

    Return()

# id: 0x001F offset: 0x47DD
@scena.Code('func_1F_47DD')
def func_1F_47DD():
    OP_13(0x0073)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

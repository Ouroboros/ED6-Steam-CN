import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2510_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2510   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '科林兹校长'),
    TXT(0x02, '乔儿'),
    TXT(0x03, '汉斯'),
    TXT(0x04, '男学生'),
    TXT(0x05, '男学生'),
    TXT(0x06, '男学生'),
    TXT(0x07, '女学生'),
    TXT(0x08, '女教师'),
    TXT(0x09, '珐奥娜'),
    TXT(0x0A, '拉迪奥老师'),
    TXT(0x0B, '碧欧拉老师'),
    TXT(0x0C, '米丽亚老师'),
    TXT(0x0D, '艾福托老师'),
    TXT(0x0E, '罗迪'),
    TXT(0x0F, '坎诺'),
    TXT(0x10, '雅莉丝'),
    TXT(0x11, '黛拉'),
    TXT(0x12, '帕布尔'),
    TXT(0x13, '罗基克'),
    TXT(0x14, '罗伊斯'),
    TXT(0x15, '莫妮卡'),
    TXT(0x16, '塞尔玛'),
    TXT(0x17, '基诺奇奥'),
    TXT(0x18, '妮吉塔'),
    TXT(0x19, '梅贝尔市长'),
    TXT(0x1A, '戴尔蒙市长'),
    TXT(0x1B, 'CH22000'),
    TXT(0x1C, ''),
]

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

# id: 0xFFFF offset: 0x46C3
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

# id: 0x10002 offset: 0x1BA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
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

# id: 0x10003 offset: 0x51A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x51A
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

# id: 0x10005 offset: 0x5BA
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
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_7A9',
    )

    SetChrPos(0x0011, 5320, 250, 2110, 270)
    SetChrPos(0x0016, -3060, 0, 3170, 45)
    SetChrPos(0x0015, 560, 100, 240, 90)
    SetChrChipByIndex(0x0015, 22)
    SetChrFlags(0x0015, 0x0004)
    SetChrFlags(0x0015, 0x0010)
    TerminateThread(0x0015, 0xFF)
    SetChrPos(0x0012, 5300, 250, 32080, 180)
    SetChrFlags(0x0012, 0x0010)
    SetChrPos(0x001B, -1100, 0, 32240, 270)
    SetChrChipByIndex(0x001D, 31)
    SetChrPos(0x001D, -2660, 100, 32180, 90)
    SetChrFlags(0x001D, 0x0004)
    SetChrFlags(0x001D, 0x0010)
    TerminateThread(0x001D, 0xFF)
    SetChrChipByIndex(0x001A, 23)
    SetChrPos(0x001A, -5950, 100, 34220, 90)
    SetChrFlags(0x001A, 0x0004)
    SetChrFlags(0x001A, 0x0010)
    TerminateThread(0x001A, 0xFF)
    ClearChrFlags(0x001E, 0x0080)
    SetChrPos(0x001E, 86430, 0, 31990, 90)
    ClearChrFlags(0x001F, 0x0080)
    SetChrPos(0x001F, 95400, 250, 31050, 90)
    ClearChrFlags(0x001C, 0x0080)
    SetChrChipByIndex(0x0013, 28)
    SetChrFlags(0x0013, 0x0004)
    SetChrFlags(0x0013, 0x0010)
    TerminateThread(0x0013, 0xFF)
    SetChrFlags(0x0014, 0x0080)
    SetChrFlags(0x0017, 0x0080)
    SetChrFlags(0x0019, 0x0080)
    SetChrChipByIndex(0x0008, 32)

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

    SetChrFlags(0x0011, 0x0080)
    SetChrFlags(0x0012, 0x0080)
    SetChrFlags(0x0013, 0x0080)
    SetChrFlags(0x0014, 0x0080)
    SetChrFlags(0x0015, 0x0080)
    SetChrFlags(0x0016, 0x0080)
    SetChrFlags(0x0017, 0x0080)
    SetChrFlags(0x0018, 0x0080)
    SetChrFlags(0x0019, 0x0080)
    SetChrFlags(0x001A, 0x0080)
    SetChrFlags(0x001D, 0x0080)
    SetChrFlags(0x001B, 0x0080)
    SetChrChipByIndex(0x0008, 32)

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

    SetChrPos(0x0011, 1710, 0, 4970, 180)
    SetChrPos(0x0012, -6910, 0, 33220, 90)
    SetChrPos(0x0013, 95370, 250, 34220, 225)
    SetChrPos(0x0008, 42950, 0, 1120, 270)
    SetChrPos(0x0016, -7060, 0, 1680, 90)
    SetChrPos(0x0017, 920, 0, -1500, 0)
    SetChrPos(0x0018, -1590, 0, 34700, 0)
    SetChrPos(0x001A, 1300, 0, 28510, 90)

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

    SetChrPos(0x0011, 1710, 0, 4970, 180)
    SetChrPos(0x0012, -6910, 0, 33220, 90)
    SetChrPos(0x0013, 95370, 250, 34220, 225)
    SetChrPos(0x0008, 43470, 0, 5280, 225)
    SetChrFlags(0x0008, 0x0010)
    SetChrFlags(0x0015, 0x0080)
    SetChrFlags(0x0018, 0x0080)
    SetChrPos(0x0016, -7060, 0, 1680, 90)
    SetChrPos(0x0017, 920, 0, -1500, 0)
    SetChrPos(0x001A, 1300, 0, 28510, 90)
    ClearChrFlags(0x0020, 0x0080)

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

    SetChrFlags(0x0012, 0x0080)
    SetChrFlags(0x0014, 0x0080)
    SetChrFlags(0x0015, 0x0080)
    SetChrFlags(0x0018, 0x0080)
    SetChrFlags(0x0019, 0x0080)
    SetChrPos(0x0016, -5200, 0, 2050, 0)
    SetChrPos(0x0017, 4500, 250, 4019, 270)
    SetChrPos(0x001A, 790, 0, 34680, 0)
    SetChrChipByIndex(0x0008, 32)

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

    SetChrPos(0x0012, 5300, 250, 32080, 90)
    SetChrFlags(0x0014, 0x0080)
    SetChrFlags(0x0015, 0x0080)
    SetChrFlags(0x0018, 0x0080)
    SetChrFlags(0x0019, 0x0080)
    ClearChrFlags(0x001E, 0x0080)
    ClearChrFlags(0x001F, 0x0080)
    SetChrChipByIndex(0x0013, 28)
    SetChrFlags(0x0013, 0x0004)
    SetChrFlags(0x0013, 0x0010)
    TerminateThread(0x0013, 0xFF)
    SetChrChipByIndex(0x0011, 26)
    SetChrFlags(0x0011, 0x0004)
    SetChrFlags(0x0011, 0x0010)
    TerminateThread(0x0011, 0xFF)
    SetChrChipByIndex(0x0016, 24)
    SetChrPos(0x0016, -2650, 100, 4200, 90)
    SetChrFlags(0x0016, 0x0004)
    SetChrFlags(0x0016, 0x0010)
    TerminateThread(0x0016, 0xFF)
    SetChrChipByIndex(0x001F, 30)
    SetChrPos(0x001F, 84120, 100, 30200, 90)
    SetChrFlags(0x001F, 0x0004)
    SetChrFlags(0x001F, 0x0010)
    TerminateThread(0x001F, 0xFF)
    SetChrFlags(0x001B, 0x0080)
    SetChrChipByIndex(0x0008, 32)

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

    SetChrFlags(0x0011, 0x0080)
    SetChrFlags(0x0012, 0x0080)
    SetChrFlags(0x0013, 0x0080)
    SetChrFlags(0x0015, 0x0080)
    SetChrFlags(0x0016, 0x0080)
    SetChrFlags(0x0017, 0x0080)
    SetChrFlags(0x0018, 0x0080)
    SetChrFlags(0x0019, 0x0080)
    SetChrFlags(0x001A, 0x0080)
    SetChrFlags(0x001B, 0x0080)
    SetChrFlags(0x001D, 0x0080)
    TerminateThread(0x0008, 0xFF)
    SetChrFlags(0x0008, 0x0004)
    SetChrFlags(0x0008, 0x0010)
    SetChrChipByIndex(0x0008, 32)

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
    Event(0, 0x0016)

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
    SetChrFlags(0x001A, 0x0080)
    SetChrFlags(0x001B, 0x0080)
    SetChrFlags(0x001D, 0x0080)
    Event(0, 0x0017)
    OP_B1('t2510_n')

    def _loc_ADB(): pass

    label('loc_ADB')

    Return()

# id: 0x0001 offset: 0xADC
@scena.Code('Init')
def Init():
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
    SetChrFlags(0x0022, 0x0080)

    def _loc_B60(): pass

    label('loc_B60')

    Return()

# id: 0x0002 offset: 0xB61
@scena.Code('ReInit')
def ReInit():
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
        'loc_EA0',
    )

    ClearChrFlags(0x00FE, 0x0010)
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

    SetChrSubChip(0x00FE, 1)

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

    SetChrSubChip(0x00FE, 0)

    Jump('loc_D25')

    def _loc_D20(): pass

    label('loc_D20')

    SetChrSubChip(0x00FE, 2)

    def _loc_D25(): pass

    label('loc_D25')

    SetChrDirection(0x00FE, 180, 0)
    SetChrFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E21',
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

    Jump('loc_E98')

    def _loc_E21(): pass

    label('loc_E21')

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

    def _loc_E98(): pass

    label('loc_E98')

    SetChrSubChip(0x00FE, 0)

    Jump('loc_1321')

    def _loc_EA0(): pass

    label('loc_EA0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_1048',
    )

    ClearChrFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x87),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_EC9',
    )

    SetChrSubChip(0x00FE, 1)

    Jump('loc_EE4')

    def _loc_EC9(): pass

    label('loc_EC9')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_EDF',
    )

    SetChrSubChip(0x00FE, 0)

    Jump('loc_EE4')

    def _loc_EDF(): pass

    label('loc_EDF')

    SetChrSubChip(0x00FE, 2)

    def _loc_EE4(): pass

    label('loc_EE4')

    SetChrDirection(0x00FE, 180, 0)
    SetChrFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_FD7',
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

    Jump('loc_1040')

    def _loc_FD7(): pass

    label('loc_FD7')

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

    def _loc_1040(): pass

    label('loc_1040')

    SetChrSubChip(0x00FE, 0)

    Jump('loc_1321')

    def _loc_1048(): pass

    label('loc_1048')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_110E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_10CC',
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

    Jump('loc_110B')

    def _loc_10CC(): pass

    label('loc_10CC')

    ChrTalk(
        0x00FE,
        (
            '#0530060103V#780F大家都很期待舞台剧。\n',
            '请务必让学园祭圆满成功。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_110B(): pass

    label('loc_110B')

    Jump('loc_1321')

    def _loc_110E(): pass

    label('loc_110E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_1261',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_11E7',
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
    ClearChrFlags(0x0008, 0x0010)

    Jump('loc_125E')

    def _loc_11E7(): pass

    label('loc_11E7')

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

    def _loc_125E(): pass

    label('loc_125E')

    Jump('loc_1321')

    def _loc_1261(): pass

    label('loc_1261')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_1321',
    )

    ClearChrFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x87),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_128A',
    )

    SetChrSubChip(0x00FE, 1)

    Jump('loc_12A5')

    def _loc_128A(): pass

    label('loc_128A')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_12A0',
    )

    SetChrSubChip(0x00FE, 0)

    Jump('loc_12A5')

    def _loc_12A0(): pass

    label('loc_12A0')

    SetChrSubChip(0x00FE, 2)

    def _loc_12A5(): pass

    label('loc_12A5')

    SetChrDirection(0x00FE, 180, 0)
    SetChrFlags(0x00FE, 0x0010)

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
    SetChrSubChip(0x00FE, 0)

    def _loc_1321(): pass

    label('loc_1321')

    TalkEnd(0x0008)

    Return()

# id: 0x0004 offset: 0x1325
@scena.Code('func_04_1325')
def func_04_1325():
    Call(0, 0x0005)

    Return()

# id: 0x0005 offset: 0x132A
@scena.Code('func_05_132A')
def func_05_132A():
    TalkBegin(0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_13D2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1399',
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

    Jump('loc_13CF')

    def _loc_1399(): pass

    label('loc_1399')

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

    def _loc_13CF(): pass

    label('loc_13CF')

    Jump('loc_19E2')

    def _loc_13D2(): pass

    label('loc_13D2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Return,
        ),
        'loc_141D',
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

    Jump('loc_19E2')

    def _loc_141D(): pass

    label('loc_141D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_14CA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1486',
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

    Jump('loc_14C7')

    def _loc_1486(): pass

    label('loc_1486')

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

    def _loc_14C7(): pass

    label('loc_14C7')

    Jump('loc_19E2')

    def _loc_14CA(): pass

    label('loc_14CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_1593',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1558',
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

    Jump('loc_1590')

    def _loc_1558(): pass

    label('loc_1558')

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

    def _loc_1590(): pass

    label('loc_1590')

    Jump('loc_19E2')

    def _loc_1593(): pass

    label('loc_1593')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_1624',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_15F8',
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

    Jump('loc_1621')

    def _loc_15F8(): pass

    label('loc_15F8')

    ChrTalk(
        0x0010,
        (
            '准备完成了吗？\n',
            '明天就要正式表演了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1621(): pass

    label('loc_1621')

    Jump('loc_19E2')

    def _loc_1624(): pass

    label('loc_1624')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_16DD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_16A1',
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

    Jump('loc_16DA')

    def _loc_16A1(): pass

    label('loc_16A1')

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

    def _loc_16DA(): pass

    label('loc_16DA')

    Jump('loc_19E2')

    def _loc_16DD(): pass

    label('loc_16DD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 6, 0x42E)),
            Expr.Return,
        ),
        'loc_1801',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_17B5',
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

    Jump('loc_17FE')

    def _loc_17B5(): pass

    label('loc_17B5')

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

    def _loc_17FE(): pass

    label('loc_17FE')

    Jump('loc_19E2')

    def _loc_1801(): pass

    label('loc_1801')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_18B8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1892',
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

    Jump('loc_18B5')

    def _loc_1892(): pass

    label('loc_1892')

    ChrTalk(
        0x0010,
        (
            '科洛丝，\n',
            '外出时请务必要小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18B5(): pass

    label('loc_18B5')

    Jump('loc_19E2')

    def _loc_18B8(): pass

    label('loc_18B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 6, 0x41E)),
            Expr.Return,
        ),
        'loc_190A',
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

    Jump('loc_19E2')

    def _loc_190A(): pass

    label('loc_190A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_19E2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_19B2',
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

    Jump('loc_19E2')

    def _loc_19B2(): pass

    label('loc_19B2')

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

    def _loc_19E2(): pass

    label('loc_19E2')

    TalkEnd(0x0010)

    Return()

# id: 0x0006 offset: 0x19E6
@scena.Code('func_06_19E6')
def func_06_19E6():
    TalkBegin(0x0011)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_1A22',
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

    Jump('loc_1C63')

    def _loc_1A22(): pass

    label('loc_1A22')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_1A74',
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

    Jump('loc_1C63')

    def _loc_1A74(): pass

    label('loc_1A74')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_1AC4',
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

    Jump('loc_1C63')

    def _loc_1AC4(): pass

    label('loc_1AC4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_1BA4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1B62',
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

    Jump('loc_1BA1')

    def _loc_1B62(): pass

    label('loc_1B62')

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

    def _loc_1BA1(): pass

    label('loc_1BA1')

    Jump('loc_1C63')

    def _loc_1BA4(): pass

    label('loc_1BA4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_1C63',
    )

    ClearChrFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1BCD',
    )

    SetChrSubChip(0x00FE, 1)

    Jump('loc_1BFE')

    def _loc_1BCD(): pass

    label('loc_1BCD')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x87),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1BE3',
    )

    SetChrSubChip(0x00FE, 0)

    Jump('loc_1BFE')

    def _loc_1BE3(): pass

    label('loc_1BE3')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x10E),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1BF9',
    )

    SetChrSubChip(0x00FE, 2)

    Jump('loc_1BFE')

    def _loc_1BF9(): pass

    label('loc_1BF9')

    SetChrSubChip(0x00FE, 1)

    def _loc_1BFE(): pass

    label('loc_1BFE')

    SetChrDirection(0x00FE, 90, 0)
    SetChrFlags(0x00FE, 0x0010)

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
    SetChrSubChip(0x00FE, 0)

    def _loc_1C63(): pass

    label('loc_1C63')

    TalkEnd(0x0011)

    Return()

# id: 0x0007 offset: 0x1C67
@scena.Code('func_07_1C67')
def func_07_1C67():
    TalkBegin(0x0012)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_1D13',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1CE9',
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
    ClearChrFlags(0x0012, 0x0010)

    Jump('loc_1D10')

    def _loc_1CE9(): pass

    label('loc_1CE9')

    ChrTalk(
        0x00FE,
        (
            '呼，这里的学生\n',
            '都很热心于学习呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D10(): pass

    label('loc_1D10')

    Jump('loc_1F46')

    def _loc_1D13(): pass

    label('loc_1D13')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_1D75',
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

    Jump('loc_1F46')

    def _loc_1D75(): pass

    label('loc_1D75')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_1E23',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1DFF',
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

    Jump('loc_1E20')

    def _loc_1DFF(): pass

    label('loc_1DFF')

    ChrTalk(
        0x00FE,
        (
            '决不能输给\n',
            '米丽亚的班级……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E20(): pass

    label('loc_1E20')

    Jump('loc_1F46')

    def _loc_1E23(): pass

    label('loc_1E23')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_1F46',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1F1F',
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

    Jump('loc_1F46')

    def _loc_1F1F(): pass

    label('loc_1F1F')

    ChrTalk(
        0x00FE,
        (
            '我还是趁现在\n',
            '批改一下考试卷子吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F46(): pass

    label('loc_1F46')

    TalkEnd(0x0012)

    Return()

# id: 0x0008 offset: 0x1F4A
@scena.Code('func_08_1F4A')
def func_08_1F4A():
    TalkBegin(0x0013)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_2004',
    )

    ClearChrFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1F76',
    )

    SetChrSubChip(0x00FE, 1)

    Jump('loc_1FA7')

    def _loc_1F76(): pass

    label('loc_1F76')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x87),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1F8C',
    )

    SetChrSubChip(0x00FE, 0)

    Jump('loc_1FA7')

    def _loc_1F8C(): pass

    label('loc_1F8C')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x10E),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1FA2',
    )

    SetChrSubChip(0x00FE, 2)

    Jump('loc_1FA7')

    def _loc_1FA2(): pass

    label('loc_1FA2')

    SetChrSubChip(0x00FE, 1)

    def _loc_1FA7(): pass

    label('loc_1FA7')

    SetChrDirection(0x00FE, 90, 0)
    SetChrFlags(0x00FE, 0x0010)

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
    SetChrSubChip(0x00FE, 0)

    Jump('loc_22BC')

    def _loc_2004(): pass

    label('loc_2004')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_20A1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2073',
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

    Jump('loc_209E')

    def _loc_2073(): pass

    label('loc_2073')

    ChrTalk(
        0x00FE,
        (
            '那个班的老师不行，\n',
            '学生们却都很优秀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_209E(): pass

    label('loc_209E')

    Jump('loc_22BC')

    def _loc_20A1(): pass

    label('loc_20A1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_20D5',
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

    Jump('loc_22BC')

    def _loc_20D5(): pass

    label('loc_20D5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_2172',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2140',
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

    Jump('loc_216F')

    def _loc_2140(): pass

    label('loc_2140')

    ChrTalk(
        0x00FE,
        (
            '嗯，明天就能好好看到\n',
            '同学们努力的成果了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_216F(): pass

    label('loc_216F')

    Jump('loc_22BC')

    def _loc_2172(): pass

    label('loc_2172')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_22BC',
    )

    ClearChrFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_219B',
    )

    SetChrSubChip(0x00FE, 1)

    Jump('loc_21CC')

    def _loc_219B(): pass

    label('loc_219B')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x87),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_21B1',
    )

    SetChrSubChip(0x00FE, 0)

    Jump('loc_21CC')

    def _loc_21B1(): pass

    label('loc_21B1')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x10E),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_21C7',
    )

    SetChrSubChip(0x00FE, 2)

    Jump('loc_21CC')

    def _loc_21C7(): pass

    label('loc_21C7')

    SetChrSubChip(0x00FE, 1)

    def _loc_21CC(): pass

    label('loc_21CC')

    SetChrDirection(0x00FE, 90, 0)
    SetChrFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2261',
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

    Jump('loc_22B7')

    def _loc_2261(): pass

    label('loc_2261')

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

    def _loc_22B7(): pass

    label('loc_22B7')

    SetChrSubChip(0x00FE, 0)

    def _loc_22BC(): pass

    label('loc_22BC')

    TalkEnd(0x0013)

    Return()

# id: 0x0009 offset: 0x22C0
@scena.Code('func_09_22C0')
def func_09_22C0():
    TalkBegin(0x0014)
    ClearChrFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x5A),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_22E5',
    )

    SetChrSubChip(0x00FE, 2)

    Jump('loc_2316')

    def _loc_22E5(): pass

    label('loc_22E5')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0xE1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_22FB',
    )

    SetChrSubChip(0x00FE, 1)

    Jump('loc_2316')

    def _loc_22FB(): pass

    label('loc_22FB')

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_2311',
    )

    SetChrSubChip(0x00FE, 0)

    Jump('loc_2316')

    def _loc_2311(): pass

    label('loc_2311')

    SetChrSubChip(0x00FE, 2)

    def _loc_2316(): pass

    label('loc_2316')

    SetChrDirection(0x00FE, 270, 0)
    SetChrFlags(0x00FE, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_236D',
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

    Jump('loc_25F3')

    def _loc_236D(): pass

    label('loc_236D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_245D',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_23EB',
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

    Jump('loc_245A')

    def _loc_23EB(): pass

    label('loc_23EB')

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

    def _loc_245A(): pass

    label('loc_245A')

    Jump('loc_25F3')

    def _loc_245D(): pass

    label('loc_245D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 6, 0x42E)),
            Expr.Return,
        ),
        'loc_2566',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_24FF',
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

    Jump('loc_2563')

    def _loc_24FF(): pass

    label('loc_24FF')

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

    def _loc_2563(): pass

    label('loc_2563')

    Jump('loc_25F3')

    def _loc_2566(): pass

    label('loc_2566')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_25F3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_25D2',
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

    Jump('loc_25F3')

    def _loc_25D2(): pass

    label('loc_25D2')

    ChrTalk(
        0x00FE,
        (
            '要有外出许可证\n',
            '才能出去哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_25F3(): pass

    label('loc_25F3')

    SetChrSubChip(0x00FE, 0)
    TalkEnd(0x0014)

    Return()

# id: 0x000A offset: 0x25FC
@scena.Code('func_0A_25FC')
def func_0A_25FC():
    TalkBegin(0x0015)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_2674',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2652',
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

    Jump('loc_2671')

    def _loc_2652(): pass

    label('loc_2652')

    ChrTalk(
        0x00FE,
        (
            '下午的课\n',
            '一定会睡着的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2671(): pass

    label('loc_2671')

    Jump('loc_2731')

    def _loc_2674(): pass

    label('loc_2674')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_2731',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_26EB',
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

    Jump('loc_2731')

    def _loc_26EB(): pass

    label('loc_26EB')

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

    def _loc_2731(): pass

    label('loc_2731')

    TalkEnd(0x0015)

    Return()

# id: 0x000B offset: 0x2735
@scena.Code('func_0B_2735')
def func_0B_2735():
    TalkBegin(0x0016)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_2781',
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

    Jump('loc_2975')

    def _loc_2781(): pass

    label('loc_2781')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_27C4',
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

    Jump('loc_2975')

    def _loc_27C4(): pass

    label('loc_27C4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_281C',
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

    Jump('loc_2975')

    def _loc_281C(): pass

    label('loc_281C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_28B6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_286B',
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

    Jump('loc_28B3')

    def _loc_286B(): pass

    label('loc_286B')

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

    def _loc_28B3(): pass

    label('loc_28B3')

    Jump('loc_2975')

    def _loc_28B6(): pass

    label('loc_28B6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_2975',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2921',
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

    Jump('loc_2975')

    def _loc_2921(): pass

    label('loc_2921')

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

    def _loc_2975(): pass

    label('loc_2975')

    TalkEnd(0x0016)

    Return()

# id: 0x000C offset: 0x2979
@scena.Code('func_0C_2979')
def func_0C_2979():
    TalkBegin(0x0017)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_29BF',
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

    Jump('loc_2AED')

    def _loc_29BF(): pass

    label('loc_29BF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_2A05',
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

    Jump('loc_2AED')

    def _loc_2A05(): pass

    label('loc_2A05')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_2A6F',
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

    Jump('loc_2AED')

    def _loc_2A6F(): pass

    label('loc_2A6F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_2AED',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2AC0',
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

    Jump('loc_2AED')

    def _loc_2AC0(): pass

    label('loc_2AC0')

    ChrTalk(
        0x00FE,
        (
            '就算是演出用的女佣服装\n',
            '也是他自己做的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2AED(): pass

    label('loc_2AED')

    TalkEnd(0x0017)

    Return()

# id: 0x000D offset: 0x2AF1
@scena.Code('func_0D_2AF1')
def func_0D_2AF1():
    TalkBegin(0x0018)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_2B3A',
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

    Jump('loc_2C0B')

    def _loc_2B3A(): pass

    label('loc_2B3A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_2C0B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2BC6',
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

    Jump('loc_2C0B')

    def _loc_2BC6(): pass

    label('loc_2BC6')

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

    def _loc_2C0B(): pass

    label('loc_2C0B')

    TalkEnd(0x0018)

    Return()

# id: 0x000E offset: 0x2C0F
@scena.Code('func_0E_2C0F')
def func_0E_2C0F():
    TalkBegin(0x0019)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_2C49',
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

    Jump('loc_2C8C')

    def _loc_2C49(): pass

    label('loc_2C49')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_2C8C',
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

    def _loc_2C8C(): pass

    label('loc_2C8C')

    TalkEnd(0x0019)

    Return()

# id: 0x000F offset: 0x2C90
@scena.Code('func_0F_2C90')
def func_0F_2C90():
    TalkBegin(0x001A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_2CC4',
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

    Jump('loc_3274')

    def _loc_2CC4(): pass

    label('loc_2CC4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 2, 0x432)),
            Expr.Return,
        ),
        'loc_2DD0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2D7F',
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

    Jump('loc_2DCD')

    def _loc_2D7F(): pass

    label('loc_2D7F')

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

    def _loc_2DCD(): pass

    label('loc_2DCD')

    Jump('loc_3274')

    def _loc_2DD0(): pass

    label('loc_2DD0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_306C',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x1000)"),
            Expr.Return,
        ),
        'loc_2EBB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2E96',
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

    Jump('loc_2EB8')

    def _loc_2E96(): pass

    label('loc_2E96')

    ChrTalk(
        0x00FE,
        (
            '如果有兴趣的话就请看一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2EB8(): pass

    label('loc_2EB8')

    Jump('loc_3069')

    def _loc_2EBB(): pass

    label('loc_2EBB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2FBF',
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

    Jump('loc_3069')

    def _loc_2FBF(): pass

    label('loc_2FBF')

    If(
        (
            (Expr.Eval, "OP_29(0x0027, 0x01, 0x0020)"),
            Expr.Return,
        ),
        'loc_3047',
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

    Jump('loc_3069')

    def _loc_3047(): pass

    label('loc_3047')

    ChrTalk(
        0x00FE,
        (
            '如果有兴趣的话就请看一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3069(): pass

    label('loc_3069')

    Jump('loc_3274')

    def _loc_306C(): pass

    label('loc_306C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 0, 0x430)),
            Expr.Return,
        ),
        'loc_3123',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_30F7',
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

    Jump('loc_3120')

    def _loc_30F7(): pass

    label('loc_30F7')

    ChrTalk(
        0x00FE,
        (
            '唔，\n',
            '还是需要一些辅助研究的资料啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3120(): pass

    label('loc_3120')

    Jump('loc_3274')

    def _loc_3123(): pass

    label('loc_3123')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_3274',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_324F',
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

    Jump('loc_3274')

    def _loc_324F(): pass

    label('loc_324F')

    ChrTurnDirection(0x00FE, 0x0105, 0)

    ChrTalk(
        0x00FE,
        (
            '科洛丝，我们互相加油吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3274(): pass

    label('loc_3274')

    TalkEnd(0x001A)

    Return()

# id: 0x0010 offset: 0x3278
@scena.Code('func_10_3278')
def func_10_3278():
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

# id: 0x0011 offset: 0x32CB
@scena.Code('func_11_32CB')
def func_11_32CB():
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

# id: 0x0012 offset: 0x330B
@scena.Code('func_12_330B')
def func_12_330B():
    TalkBegin(0x001D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_3362',
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

    Jump('loc_3428')

    def _loc_3362(): pass

    label('loc_3362')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_33DE',
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

    Jump('loc_3428')

    def _loc_33DE(): pass

    label('loc_33DE')

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

    def _loc_3428(): pass

    label('loc_3428')

    TalkEnd(0x001D)

    Return()

# id: 0x0013 offset: 0x342C
@scena.Code('func_13_342C')
def func_13_342C():
    TalkBegin(0x001E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_347C',
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

    Jump('loc_34CB')

    def _loc_347C(): pass

    label('loc_347C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_34CB',
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

    def _loc_34CB(): pass

    label('loc_34CB')

    TalkEnd(0x001E)

    Return()

# id: 0x0014 offset: 0x34CF
@scena.Code('func_14_34CF')
def func_14_34CF():
    TalkBegin(0x001F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_357A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_353F',
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

    Jump('loc_3577')

    def _loc_353F(): pass

    label('loc_353F')

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

    def _loc_3577(): pass

    label('loc_3577')

    Jump('loc_3640')

    def _loc_357A(): pass

    label('loc_357A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 7, 0x42F)),
            Expr.Return,
        ),
        'loc_3640',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 0, 0x10)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_361B',
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

    Jump('loc_3640')

    def _loc_361B(): pass

    label('loc_361B')

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '基诺奇奥做事真是很粗心呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3640(): pass

    label('loc_3640')

    TalkEnd(0x001F)

    Return()

# id: 0x0015 offset: 0x3644
@scena.Code('func_15_3644')
def func_15_3644():
    TalkBegin(0x0020)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 1, 0x431)),
            Expr.Return,
        ),
        'loc_38FC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0002, 1, 0x11)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3882',
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

    Jump('loc_38FC')

    def _loc_3882(): pass

    label('loc_3882')

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

    def _loc_38FC(): pass

    label('loc_38FC')

    TalkEnd(0x0020)

    Return()

# id: 0x0016 offset: 0x3900
@scena.Code('func_16_3900')
def func_16_3900():
    EventBegin(0x00)
    ClearMapFlags(0x00000001)
    CameraMove(116280, 0, 2160, 0)
    SetChrPos(0x0101, 117450, 0, -1700, 0)
    SetChrPos(0x0102, 116510, 0, -1950, 0)
    SetChrPos(0x0105, 117000, 0, -1020, 0)
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

    @scena.Lambda('lambda_3988')
    def lambda_3988():
        CameraMove(117230, 0, 4590, 2000)

        ExitThread()

    DispatchAsync(0x0105, 0x0002, lambda_3988)

    @scena.Lambda('lambda_39A0')
    def lambda_39A0():
        ChrWalkTo(0x00FE, 116880, 0, 1680, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_39A0)

    Sleep(500)

    @scena.Lambda('lambda_39C0')
    def lambda_39C0():
        ChrWalkTo(0x00FE, 117520, 0, 1680, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_39C0)

    Sleep(300)

    @scena.Lambda('lambda_39E0')
    def lambda_39E0():
        ChrWalkTo(0x00FE, 116300, 0, 1490, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_39E0)

    WaitForThreadExit(0x0105, 0x0001)

    @scena.Lambda('lambda_3A00')
    def lambda_3A00():
        ChrWalkTo(0x00FE, 116110, 0, 2550, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_3A00)

    WaitForThreadExit(0x0105, 0x0001)
    SetChrDirection(0x0105, 0, 400)
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
    SetChrDirection(0x0105, 135, 400)

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

# id: 0x0017 offset: 0x40DB
@scena.Code('func_17_40DB')
def func_17_40DB():
    EventBegin(0x00)
    OP_77(0xFF, 0xC8, 0x96, 0x00, 0x00000000)
    CameraMove(-1190, 0, 33250, 0)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    SetChrFlags(0x0009, 0x0004)
    SetChrFlags(0x000A, 0x0004)
    SetChrFlags(0x000B, 0x0004)
    SetChrFlags(0x000C, 0x0004)
    SetChrFlags(0x000D, 0x0004)
    SetChrFlags(0x000E, 0x0004)
    SetChrFlags(0x0105, 0x0004)
    SetChrFlags(0x0101, 0x0004)
    SetChrFlags(0x0102, 0x0004)
    SetChrChipByIndex(0x0101, 19)
    SetChrChipByIndex(0x0102, 20)
    SetChrChipByIndex(0x0105, 21)
    SetChrChipByIndex(0x000B, 23)
    SetChrChipByIndex(0x000C, 24)
    SetChrChipByIndex(0x000D, 22)
    SetChrChipByIndex(0x000E, 25)
    SetChrPos(0x0101, 500, 200, 32060, 90)
    SetChrPos(0x0102, 500, 200, 29980, 90)
    SetChrPos(0x0105, 520, 200, 34100, 90)
    SetChrPos(0x000A, -2750, 200, 30010, 90)
    SetChrPos(0x0009, -2750, 200, 32060, 90)
    SetChrPos(0x000C, -2750, 100, 34060, 90)
    SetChrPos(0x000B, -5900, 100, 30010, 90)
    SetChrPos(0x000D, -5900, 100, 34160, 90)
    SetChrPos(0x000E, -5900, 100, 31920, 90)
    SetChrPos(0x000F, 5300, 250, 32119, 90)

    @scena.Lambda('lambda_421A')
    def lambda_421A():
        CameraMove(3580, 0, 33240, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_421A)

    FadeIn(2000, 0)
    ChrWalkTo(0x000F, 5390, 250, 30460, 1000, 0x00)
    SetChrDirection(0x000F, 90, 400)
    Sleep(500)

    ChrWalkTo(0x000F, 5370, 250, 31960, 1000, 0x00)
    SetChrDirection(0x000F, 90, 400)
    Sleep(500)

    ChrWalkTo(0x000F, 5390, 250, 30460, 1000, 0x00)
    SetChrDirection(0x000F, 270, 400)
    Sleep(1000)

    @scena.Lambda('lambda_429B')
    def lambda_429B():
        CameraMove(2000, 0, 33250, 1500)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_429B)

    ChrWalkTo(0x000F, 3370, 0, 30480, 2000, 0x00)
    ChrWalkTo(0x000F, 2570, 0, 31600, 2000, 0x00)
    ChrTurnDirection(0x000F, 0x0101, 400)
    SetChrSubChip(0x0102, 1)
    Sleep(100)

    SetChrSubChip(0x0105, 2)
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
    SetChrSubChip(0x0101, 2)
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

# id: 0x0018 offset: 0x44B8
@scena.Code('func_18_44B8')
def func_18_44B8():
    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4535',
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

    Jump('loc_4579')

    def _loc_4535(): pass

    label('loc_4535')

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

    def _loc_4579(): pass

    label('loc_4579')

    TalkEnd(0x00FF)

    Return()

# id: 0x0019 offset: 0x457D
@scena.Code('func_19_457D')
def func_19_457D():
    FadeOut(300, 0, 100)
    SetChrName('')
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

# id: 0x001A offset: 0x4609
@scena.Code('func_1A_4609')
def func_1A_4609():
    PlaySE(17, 0x00, 0x64)
    SetChrFlags(0x0022, 0x0080)
    OP_64(0x05, 0x0001)
    FadeOut(300, 0, 100)
    SetChrName('')
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

# id: 0x001B offset: 0x466F
@scena.Code('func_1B_466F')
def func_1B_466F():
    OP_13(0x006F)

    Return()

# id: 0x001C offset: 0x4673
@scena.Code('func_1C_4673')
def func_1C_4673():
    OP_13(0x005E)

    Return()

# id: 0x001D offset: 0x4677
@scena.Code('func_1D_4677')
def func_1D_4677():
    OP_13(0x006E)

    Return()

# id: 0x001E offset: 0x467B
@scena.Code('func_1E_467B')
def func_1E_467B():
    OP_13(0x0074)

    Return()

# id: 0x001F offset: 0x467F
@scena.Code('func_1F_467F')
def func_1F_467F():
    OP_13(0x0073)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0130_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0130   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '迪拜恩教区长'),
    TXT(0x02, '修女梅'),
    TXT(0x03, '凯文神父'),
    TXT(0x04, '矿工皮尔姆'),
    TXT(0x05, '乘务员库因特'),
    TXT(0x06, '矿工海涅'),
    TXT(0x07, '克露莎'),
    TXT(0x08, '阿鲁姆'),
    TXT(0x09, '艾娅莉'),
    TXT(0x0A, '安敦'),
    TXT(0x0B, '伴娘'),
    TXT(0x0C, '布露姆老奶奶'),
    TXT(0x0D, '亚尔丽 '),
    TXT(0x0E, '鲁克'),
    TXT(0x0F, '帕特'),
    TXT(0x10, '赛拉'),
    TXT(0x11, '托露塔'),
    TXT(0x12, '胡里奥'),
    TXT(0x13, '伊娜'),
    TXT(0x14, '安莉尔'),
    TXT(0x15, '临时演员'),
    TXT(0x16, '临时演员'),
    TXT(0x17, '临时演员'),
    TXT(0x18, '临时演员'),
    TXT(0x19, '临时演员'),
    TXT(0x1A, '新郎的亲属'),
    TXT(0x1B, '新郎的亲属'),
    TXT(0x1C, '新郎的亲属'),
    TXT(0x1D, '新娘的亲属'),
    TXT(0x1E, '新娘的亲属'),
    TXT(0x1F, '新娘的亲属'),
    TXT(0x20, '新娘的朋友'),
    TXT(0x21, '新娘的朋友'),
    TXT(0x22, '目标用照相机'),
    TXT(0x23, '小猫'),
    TXT(0x24, '小猫'),
    TXT(0x25, '小猫'),
    TXT(0x26, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0130.x'
    header.mapIndex       = 3
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T0130_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x5413
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
        ('ED6_DT07/CH01400._CH', 'ED6_DT07/CH01400P._CP'),
        ('ED6_DT07/CH01410._CH', 'ED6_DT07/CH01410P._CP'),
        ('ED6_DT27/CH03080._CH', 'ED6_DT27/CH03080P._CP'),
        ('ED6_DT07/CH01500._CH', 'ED6_DT07/CH01500P._CP'),
        ('ED6_DT07/CH01290._CH', 'ED6_DT07/CH01290P._CP'),
        ('ED6_DT07/CH01070._CH', 'ED6_DT07/CH01070P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01050._CH', 'ED6_DT07/CH01050P._CP'),
        ('ED6_DT07/CH01690._CH', 'ED6_DT07/CH01690P._CP'),
        ('ED6_DT27/CH03005._CH', 'ED6_DT27/CH03005P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH01013._CH', 'ED6_DT07/CH01013P._CP'),
        ('ED6_DT07/CH01033._CH', 'ED6_DT07/CH01033P._CP'),
        ('ED6_DT07/CH01160._CH', 'ED6_DT07/CH01160P._CP'),
        ('ED6_DT07/CH01060._CH', 'ED6_DT07/CH01060P._CP'),
        ('ED6_DT07/CH01133._CH', 'ED6_DT07/CH01133P._CP'),
        ('ED6_DT07/CH01043._CH', 'ED6_DT07/CH01043P._CP'),
        ('ED6_DT07/CH01700._CH', 'ED6_DT07/CH01700P._CP'),
        ('ED6_DT07/CH01053._CH', 'ED6_DT07/CH01053P._CP'),
        ('ED6_DT07/CH01223._CH', 'ED6_DT07/CH01223P._CP'),
        ('ED6_DT07/CH01593._CH', 'ED6_DT07/CH01593P._CP'),
        ('ED6_DT07/CH01233._CH', 'ED6_DT07/CH01233P._CP'),
        ('ED6_DT07/CH01183._CH', 'ED6_DT07/CH01183P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01200._CH', 'ED6_DT07/CH01200P._CP'),
        ('ED6_DT07/CH01470._CH', 'ED6_DT07/CH01470P._CP'),
        ('ED6_DT07/CH01490._CH', 'ED6_DT07/CH01490P._CP'),
        ('ED6_DT07/CH01230._CH', 'ED6_DT07/CH01230P._CP'),
        ('ED6_DT07/CH01480._CH', 'ED6_DT07/CH01480P._CP'),
        ('ED6_DT07/CH01213._CH', 'ED6_DT07/CH01213P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT26/CH20311._CH', 'ED6_DT26/CH20311P._CP'),
        ('ED6_DT07/CH01493._CH', 'ED6_DT07/CH01493P._CP'),
    ]

# id: 0x10002 offset: 0x1BA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 58800,
            z                   = 1000,
            y                   = 52200,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = -16830,
            z                   = 0,
            y                   = 42890,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 55420,
            z                   = 0,
            y                   = 46990,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = 58970,
            z                   = 0,
            y                   = 47900,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = 62060,
            z                   = 0,
            y                   = 43550,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = 56050,
            z                   = 0,
            y                   = 40700,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = 55340,
            z                   = 0,
            y                   = 47470,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = 64000,
            z                   = 0,
            y                   = 47270,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0111,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            x                   = 64000,
            z                   = 0,
            y                   = 48170,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            x                   = 58300,
            z                   = 0,
            y                   = 44200,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 57670,
            z                   = 0,
            y                   = 48880,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 55310,
            z                   = 150,
            y                   = 45960,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 56390,
            z                   = 150,
            y                   = 45990,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000F,
        ),
        ScenaNpcData(
            x                   = 54680,
            z                   = 0,
            y                   = 44910,
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
            x                   = 55400,
            z                   = 0,
            y                   = 44910,
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
            x                   = 56470,
            z                   = 150,
            y                   = 44510,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0018,
        ),
        ScenaNpcData(
            x                   = 56150,
            z                   = 0,
            y                   = 41510,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 16,
            chipIndex           = 16,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 61860,
            z                   = 150,
            y                   = 42920,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0195,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0019,
        ),
        ScenaNpcData(
            x                   = 62700,
            z                   = 150,
            y                   = 42950,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 62960,
            z                   = 0,
            y                   = 43610,
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
            x                   = 54500,
            z                   = 150,
            y                   = 42970,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 19,
            chipIndex           = 19,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 55920,
            z                   = 150,
            y                   = 42970,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 55090,
            z                   = 150,
            y                   = 41510,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 62110,
            z                   = 150,
            y                   = 41430,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 63630,
            z                   = 150,
            y                   = 41440,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 57680,
            z                   = 0,
            y                   = 43380,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 25,
            chipIndex           = 25,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0010,
        ),
        ScenaNpcData(
            x                   = 58780,
            z                   = 0,
            y                   = 46800,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0011,
        ),
        ScenaNpcData(
            x                   = 63110,
            z                   = 0,
            y                   = 46830,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0012,
        ),
        ScenaNpcData(
            x                   = 57650,
            z                   = 0,
            y                   = 42350,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 27,
            chipIndex           = 27,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0013,
        ),
        ScenaNpcData(
            x                   = -16100,
            z                   = 0,
            y                   = 45910,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 28,
            chipIndex           = 28,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0014,
        ),
        ScenaNpcData(
            x                   = 54130,
            z                   = 0,
            y                   = 50110,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 29,
            chipIndex           = 29,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0015,
        ),
        ScenaNpcData(
            x                   = 52890,
            z                   = 0,
            y                   = 48010,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0016,
        ),
        ScenaNpcData(
            x                   = 52980,
            z                   = 0,
            y                   = 46970,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0017,
        ),
        ScenaNpcData(
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
            x                   = 63200,
            z                   = 0,
            y                   = 43610,
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
            x                   = 63700,
            z                   = 0,
            y                   = 43610,
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
            x                   = 64099,
            z                   = 0,
            y                   = 43610,
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
    )

# id: 0x10003 offset: 0x65A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x65A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x65A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 58950,
            triggerZ            = 1000,
            triggerY            = 50290,
            triggerRange        = 400,
            actorX              = 58800,
            actorZ              = 2500,
            actorY              = 52200,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 52200,
            triggerZ            = 5000,
            triggerY            = 52260,
            triggerRange        = 600,
            actorX              = 52200,
            actorZ              = 5600,
            actorY              = 52260,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x6A2
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_7DC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_76C',
    )

    SetChrChipByIndex(0x0014, 24)
    ClearChrFlags(0x0014, 0x0004)
    ClearChrFlags(0x0014, 0x0080)
    SetChrPos(0x0014, -16010, 0, 43960, 180)
    CreateThread(0x0014, 0x00, 0x00, 0x0002)
    SetChrPos(0x0009, 59550, 0, 48300, 270)
    SetChrFlags(0x0009, 0x0010)
    SetChrPos(0x000F, 58560, 0, 48300, 90)
    SetChrFlags(0x000F, 0x0010)
    SetChrPos(0x0010, -15950, 0, 43090, 270)
    SetChrFlags(0x0010, 0x0010)
    SetChrChipByIndex(0x0017, 31)
    ClearChrFlags(0x0017, 0x0004)
    ClearChrFlags(0x0017, 0x0080)
    SetChrPos(0x0017, -15930, 0, 42250, 0)
    CreateThread(0x0017, 0x00, 0x00, 0x0002)
    ClearChrFlags(0x0021, 0x0080)
    ClearChrFlags(0x0022, 0x0080)
    ClearChrFlags(0x0023, 0x0080)
    ClearChrFlags(0x0024, 0x0080)
    ClearChrFlags(0x0025, 0x0080)
    ClearChrFlags(0x0026, 0x0080)
    ClearChrFlags(0x0027, 0x0080)
    ClearChrFlags(0x0028, 0x0080)

    Jump('loc_7D9')

    def _loc_76C(): pass

    label('loc_76C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 6, 0x2086)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_777',
    )

    Jump('loc_7D9')

    def _loc_777(): pass

    label('loc_777')

    SetChrChipByIndex(0x0014, 24)
    ClearChrFlags(0x0014, 0x0004)
    ClearChrFlags(0x0014, 0x0080)
    SetChrPos(0x0014, 56320, 0, 46950, 270)
    CreateThread(0x0014, 0x00, 0x00, 0x0002)
    SetChrFlags(0x000F, 0x0080)
    SetChrFlags(0x0010, 0x0080)
    SetChrChipByIndex(0x0019, 33)
    ClearChrFlags(0x0019, 0x0004)
    ClearChrFlags(0x0019, 0x0080)
    ClearChrFlags(0x0019, 0x0010)
    SetChrPos(0x0019, 55160, 0, 46950, 90)
    ClearChrFlags(0x0019, 0x0080)
    CreateThread(0x0019, 0x00, 0x00, 0x0002)

    def _loc_7D9(): pass

    label('loc_7D9')

    Jump('loc_83B')

    def _loc_7DC(): pass

    label('loc_7DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_7EB',
    )

    ClearChrFlags(0x000A, 0x0080)

    Jump('loc_83B')

    def _loc_7EB(): pass

    label('loc_7EB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_80E',
    )

    SetChrFlags(0x0010, 0x0010)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000E, 0x0080)

    Jump('loc_83B')

    def _loc_80E(): pass

    label('loc_80E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_822',
    )

    ClearChrFlags(0x000E, 0x0080)
    SetChrFlags(0x0010, 0x0010)

    Jump('loc_83B')

    def _loc_822(): pass

    label('loc_822')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_82C',
    )

    Jump('loc_83B')

    def _loc_82C(): pass

    label('loc_82C')

    SetChrFlags(0x0009, 0x0010)
    SetChrFlags(0x000F, 0x0080)
    SetChrFlags(0x0010, 0x0080)

    def _loc_83B(): pass

    label('loc_83B')

    If(
        (
            (Expr.Eval, "OP_29(0x0072, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x0072, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0072, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_40(0x0234, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_86B',
    )

    ClearChrFlags(0x0010, 0x0010)
    ClearChrFlags(0x000F, 0x0010)

    def _loc_86B(): pass

    label('loc_86B')

    If(
        (
            (Expr.Eval, "OP_29(0x0076, 0x01, 0x2000)"),
            (Expr.Eval, "OP_29(0x0076, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0076, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_88A',
    )

    Event(1, 0x0007)

    def _loc_88A(): pass

    label('loc_88A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 6, 0x2086)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_89F',
    )

    SetMapFlags(0x10000000)
    Event(0, 0x001A)

    def _loc_89F(): pass

    label('loc_89F')

    Return()

# id: 0x0001 offset: 0x8A0
@scena.Code('Init')
def Init():
    OP_64(0x01, 0x0001)

    If(
        (
            (Expr.Eval, "OP_29(0x0077, 0x00, 0x04)"),
            (Expr.Eval, "OP_29(0x0077, 0x01, 0x0008)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0077, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_8C3',
    )

    OP_65(0x01, 0x0001)

    def _loc_8C3(): pass

    label('loc_8C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_8EA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8D5',
    )

    Jump('loc_8EA')

    def _loc_8D5(): pass

    label('loc_8D5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 6, 0x2086)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8E0',
    )

    Jump('loc_8EA')

    def _loc_8E0(): pass

    label('loc_8E0')

    OP_D2(0x000700A8, 0x000700AC, 0x21)

    def _loc_8EA(): pass

    label('loc_8EA')

    Return()

# id: 0x0002 offset: 0x8EB
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
        'loc_910',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_A52')

    def _loc_910(): pass

    label('loc_910')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_929',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000640)

    Jump('loc_A52')

    def _loc_929(): pass

    label('loc_929')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_942',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x0000060E)

    Jump('loc_A52')

    def _loc_942(): pass

    label('loc_942')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_95B',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005DC)

    Jump('loc_A52')

    def _loc_95B(): pass

    label('loc_95B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_974',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AA)

    Jump('loc_A52')

    def _loc_974(): pass

    label('loc_974')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_98D',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x00000578)

    Jump('loc_A52')

    def _loc_98D(): pass

    label('loc_98D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9A6',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x00000546)

    Jump('loc_A52')

    def _loc_9A6(): pass

    label('loc_9A6')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9BF',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000677)

    Jump('loc_A52')

    def _loc_9BF(): pass

    label('loc_9BF')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9D8',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000645)

    Jump('loc_A52')

    def _loc_9D8(): pass

    label('loc_9D8')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9F1',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x00000613)

    Jump('loc_A52')

    def _loc_9F1(): pass

    label('loc_9F1')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A0A',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005E1)

    Jump('loc_A52')

    def _loc_A0A(): pass

    label('loc_A0A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A23',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AF)

    Jump('loc_A52')

    def _loc_A23(): pass

    label('loc_A23')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A3C',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x0000057D)

    Jump('loc_A52')

    def _loc_A3C(): pass

    label('loc_A3C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A52',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x0000054B)

    def _loc_A52(): pass

    label('loc_A52')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_A67',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_A52')

    def _loc_A67(): pass

    label('loc_A67')

    Return()

# id: 0x0003 offset: 0xA68
@scena.Code('func_03_A68')
def func_03_A68():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_A8B',
    )

    OP_8D(0x00FE, 54500, 46700, 56400, 48400, 2000)

    Jump('func_03_A68')

    def _loc_A8B(): pass

    label('loc_A8B')

    Return()

# id: 0x0004 offset: 0xA8C
@scena.Code('func_04_A8C')
def func_04_A8C():
    Call(0, 0x0005)

    Return()

# id: 0x0005 offset: 0xA91
@scena.Code('func_05_A91')
def func_05_A91():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_109C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0413, 6, 0x209E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D49',
    )

    ChrTurnDirection(0x0008, 0x0102, 0)

    ChrTalk(
        0x0008,
        (
            '啊……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_ADB',
    )

    ChrTalk(
        0x0008,
        (
            '不是约修亚吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AFC')

    def _loc_ADB(): pass

    label('loc_ADB')

    ChrTalk(
        0x0008,
        (
            '站在那里的…\n',
            '不是约修亚吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AFC(): pass

    label('loc_AFC')

    ChrTalk(
        0x0102,
        (
            '#1035F是的……\n',
            '我回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '……我一直在等你哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '嗯……\n',
            '表情很沉稳，很好～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '看来你已经找到自己\n',
            '的道路了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F是的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '……艾丝蒂尔，约修亚，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '如今的世界\n',
            '再次陷入了混乱，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '但是不管发生什么情况，\n',
            '也绝对不能迷失自己。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '引导我们的\n',
            '希望之光……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '并不在别处，\n',
            '而是在我们自己的心中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1002F嗯……我明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F您的话……\n',
            '我一定会牢记在心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 6, 0x2086)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D40',
    )

    ChrTalk(
        0x0008,
        (
            '嗯，那样再好不过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '好了，本来还想多和你们\n',
            '说几句话…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '但如今是非常时刻，\n',
            '就不多耽误你们的时间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F啊哈哈……说的也是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F是，那么改日再来拜访。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D40(): pass

    label('loc_D40')

    OP_A2(0x0001)
    OP_A2(0x209E)

    Jump('loc_1099')

    def _loc_D49(): pass

    label('loc_D49')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_DDD',
    )

    ChrTalk(
        0x0008,
        (
            '不管发生什么事情\n',
            '也绝对不能迷失自己。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '引导我们的希望之光，\n',
            '就在我们自己的心中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 6, 0x2086)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DDA',
    )

    ChrTalk(
        0x0008,
        (
            '那么… \n',
            '我也要开始准备婚礼仪式了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DDA(): pass

    label('loc_DDA')

    Jump('loc_1099')

    def _loc_DDD(): pass

    label('loc_DDD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 6, 0x2086)),
            Expr.Return,
        ),
        'loc_F3A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_ED5',
    )

    ChrTalk(
        0x0008,
        (
            '嗯，婚礼总算是\n',
            '顺利完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '艾丝蒂尔你们\n',
            '好像也出席了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011F啊，是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F嗯，只是最后的部分而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '这也是人生的一个重要部分，\n',
            '值得我们仔细体会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '当然了，对你们来说～\n',
            '还稍微有些遥远。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_F37')

    def _loc_ED5(): pass

    label('loc_ED5')

    ChrTalk(
        0x0008,
        (
            '这也是人生的一个重要部分，\n',
            '值得我们仔细体会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '毕竟这是我们每个人都要\n',
            '经历思考的事情啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F37(): pass

    label('loc_F37')

    Jump('loc_1099')

    def _loc_F3A(): pass

    label('loc_F3A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_100F',
    )

    ChrTalk(
        0x0008,
        (
            '今天教堂里准备举行\n',
            '结婚仪式。\n',
            '准备工作很忙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '即使在乌云之下，鸟儿也会鸣叫。\n',
            '即使在寒冷的冰雪中，草木也会发芽……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '因此，即使在如今这种混乱的世态下，\n',
            '我们也要努力继续\n',
            '过好自己的生活。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_1099')

    def _loc_100F(): pass

    label('loc_100F')

    ChrTalk(
        0x0008,
        (
            '即使在乌云之下，鸟儿也会鸣叫。\n',
            '即使在寒冷的冰雪中，草木也会发芽……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '因此，即使在如今这种混乱的世态下，\n',
            '也要继续过好自己的生活。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1099(): pass

    label('loc_1099')

    Jump('loc_222E')

    def _loc_109C(): pass

    label('loc_109C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_1672',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034B, 5, 0x1A5D)),
            Expr.Return,
        ),
        'loc_1428',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 6, 0xE)),
            Expr.Return,
        ),
        'loc_1142',
    )

    ChrTalk(
        0x0008,
        (
            '醉倒的两个人\n',
            '我已经安置好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '还好没有\n',
            '酒精中毒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '再怎么自信十足，\n',
            '也不该喝这么多酒啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '和爱娜拼酒\n',
            '简直是折磨自己的身体。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1425')

    def _loc_1142(): pass

    label('loc_1142')

    If(
        (
            (Expr.Eval, "OP_29(0x0076, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0076, 0x01, 0x0800)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1387',
    )

    ChrTalk(
        0x0008,
        (
            '对了，是之前\n',
            '的酒馆事件吗…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '醉倒的两个人\n',
            '我已经安置好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '还好没有\n',
            '酒精中毒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_12F4',
    )

    ChrTurnDirection(0x0008, 0x0104, 400)

    ChrTalk(
        0x0008,
        (
            '……哎呀。\n',
            '刚刚才说到你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '……奥利维尔…\n',
            '已经没关系了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#035F呵～总算没事了，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '给大家添麻烦了，\n',
            '不过现在已经不用担心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '嗯……\n',
            '所以……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '再怎么自信十足，\n',
            '也不该喝这么多酒啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '和爱娜拼酒\n',
            '简直是折磨自己的身体。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1007F确、确实……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#034F好、好好记下来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_137B')

    def _loc_12F4(): pass

    label('loc_12F4')

    ChrTalk(
        0x0008,
        (
            '再怎么自信十足，\n',
            '也不该喝这么多酒啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '和爱娜拼酒\n',
            '就是在破坏自己的身体呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1007F确、确实……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#025F呼，好好记下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_137B(): pass

    label('loc_137B')

    OP_28(0x0076, 0x01, 0x0800)
    OP_A2(0x000E)

    Jump('loc_1425')

    def _loc_1387(): pass

    label('loc_1387')

    ChrTurnDirection(0x0008, 0x0101, 0)

    ChrTalk(
        0x0008,
        (
            '看着艾丝蒂尔的成长，\n',
            '对我也是很有帮助的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '就算以后到其它地区工作，\n',
            '也别忘记今天的心情喔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '心中坚定的信念\n',
            '无论到任何时候也都不会改变的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1425(): pass

    label('loc_1425')

    Jump('loc_166F')

    def _loc_1428(): pass

    label('loc_1428')

    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x0008, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '啊，艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '你这次的活跃\n',
            '我也已经听说了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '你终于战胜了困难啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我身为一名市民，\n',
            '也要好好感谢你才是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1008F嘿嘿……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '教区长的赞扬\n',
            '实在是愧不敢当啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F应该道谢的其实是我们才对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '联络大圣堂还有照顾受害者……\n',
            '真是多亏了您的帮助。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0103, 400)

    ChrTalk(
        0x0008,
        (
            '哪里，我身为一名神父，\n',
            '这些都只是份内之事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '只是，在困难重重的处境下，\n',
            '看着艾丝蒂尔的成长，\n',
            '对我也是很有帮助的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '就算以后到其它地区工作，\n',
            '也别忘记今天的心情喔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F……是！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那么先就这样了、教区长…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '一路小心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我会祈愿女神\n',
            '保佑各位的…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1A5D)
    def _loc_166F(): pass

    label('loc_166F')

    Jump('loc_222E')

    def _loc_1672(): pass

    label('loc_1672')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_1B71',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0312, 2, 0x1892)),
            Expr.Return,
        ),
        'loc_1700',
    )

    ChrTalk(
        0x0008,
        (
            '力量不足或是失败…\n',
            '都不足为惧，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '现在我们唯一能做的\n',
            '就是拿出自己的全部力量。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '结果那应该是解决事件\n',
            '的最佳途径。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B6E')

    def _loc_1700(): pass

    label('loc_1700')

    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x0008, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '啊，艾丝蒂尔……\n',
            '还有雪拉扎德…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '你们已经见到\n',
            '凯文神父了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1025F啊，是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '他现在应该还在\n',
            '帕赛尔农场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '原来如此，是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '嗯，可是…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '……表情似乎\n',
            '很迷茫啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1026F啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '虽然没有完全理解，\n',
            '不过只能试试看了……\n',
            '状况已经是那个样子了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '所以，一定不要迷失自我，\n',
            '努力踏出自己的脚步就对了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '未来一定会\n',
            '越来越好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '也许是因为有优秀的前辈\n',
            '一直在指导吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1017F嘿嘿……\n',
            '确实如此呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1988',
    )

    ChrTalk(
        0x0104,
        (
            '#031F呵呵～听你这么说，\n',
            '还真是有点不好意思呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '呵呵，虽说艾丝蒂尔\n',
            '确实是我看着成长起来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0104, 400)

    ChrTalk(
        0x0101,
        (
            '#1007F……啊啊，为什么奥利维尔\n',
            '会在这时候出现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AAA')

    def _loc_1988(): pass

    label('loc_1988')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_19EE',
    )

    ChrTalk(
        0x0106,
        (
            '#051F嘿，真是少见。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '要是能一直这样\n',
            '那可就谢天谢地了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#021F呵呵，真是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AAA')

    def _loc_19EE(): pass

    label('loc_19EE')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A5D',
    )

    ChrTalk(
        0x0108,
        (
            '#071F喂喂，怎么了？\n',
            '竟然会这么老实。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '哈哈，这样\n',
            '可真不像你呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F呵呵，真是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AAA')

    def _loc_1A5D(): pass

    label('loc_1A5D')

    ChrTalk(
        0x0103,
        (
            '#021F呵呵，这还真少见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#1007F嗯……\n',
            '要是能一直这样就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AAA(): pass

    label('loc_1AAA')

    ChrTalk(
        0x0008,
        (
            '不管怎样，力量不足或是失败\n',
            '都不足为惧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '现在我们唯一能做的\n',
            '就是拿出自己的全部力量。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '结果那应该是解决事件\n',
            '的最佳途径。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#1006F嗯、教区长……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F嗯，就那么做吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1892)

    def _loc_1B6E(): pass

    label('loc_1B6E')

    Jump('loc_222E')

    def _loc_1B71(): pass

    label('loc_1B71')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_1D31',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1C17',
    )

    ChrTalk(
        0x0008,
        (
            '很遗憾，以手头的资料来看\n',
            '这是办不到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我为了保护人们的身心健康\n',
            '而学习医术和药理……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '但这片大地上似乎还有很多\n',
            '无法理解的神秘现象呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D2E')

    def _loc_1C17(): pass

    label('loc_1C17')

    ChrTalk(
        0x0008,
        (
            '啊，各位。\n',
            '很早嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '很遗憾，以手头的资料来看\n',
            '这是办不到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我为了保护人们的身心健康\n',
            '而学习医术和药理……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '但这片大地上似乎还有很多\n',
            '无法理解的神秘现象呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我们作为七耀教会的信徒，\n',
            '虽然知道追求真理之道遥远而艰辛，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '但只要还有希望\n',
            '就绝不能放弃努力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_1D2E(): pass

    label('loc_1D2E')

    Jump('loc_222E')

    def _loc_1D31(): pass

    label('loc_1D31')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_2007',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0312, 1, 0x1891)),
            Expr.Return,
        ),
        'loc_1DEB',
    )

    ChrTalk(
        0x0008,
        (
            '正因为无法看到，\n',
            '所以反而思考了不少东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '完全不用顾及外界的变化、\n',
            '静下心来重新审视了一下过去的自己。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '……仔细想想的话，\n',
            '这场大雾从某种意义上说也是好事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2004')

    def _loc_1DEB(): pass

    label('loc_1DEB')

    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x0008, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '……啊，这不是艾丝蒂尔\n',
            '和雪拉扎德吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '嗯，好久不见了，\n',
            '身体还好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1011F啊，是的……\n',
            '教区长，好久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F教区长身体健康\n',
            '就比什么都好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '你们两个都回来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '现在洛连特被浓雾笼罩，\n',
            '看东西都很困难。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不过，正因为什么都看不见，\n',
            '所以反而思考了不少东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '完全不用顾及外界的变化、\n',
            '静下心来重新审视了一下过去的自己。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '……仔细想想的话，\n',
            '这场大雾从某种意义上说也是好事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1007F（嗯、嗯……\n',
            '还是好难懂啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F（确实……\n',
            '  不过、很值得慢慢品味呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1891)

    def _loc_2004(): pass

    label('loc_2004')

    Jump('loc_222E')

    def _loc_2007(): pass

    label('loc_2007')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 3, 0x1003)),
            Expr.Return,
        ),
        'loc_222E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0206, 1, 0x1031)),
            Expr.Return,
        ),
        'loc_2067',
    )

    ChrTalk(
        0x0008,
        (
            '艾丝蒂尔，你终于回来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '空之女神爱德丝啊！\n',
            '请您引导彷徨的人们吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_222E')

    def _loc_2067(): pass

    label('loc_2067')

    ChrTalk(
        0x0008,
        (
            '……啊，这不是艾丝蒂尔吗…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0142, 400)

    ChrTalk(
        0x0008,
        (
            '你是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0142,
        (
            '#1060F初次见面，教区长。\n',
            '我是巡回神父凯文·格拉汉姆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '喔！说起来的话，听说有个\n',
            '从总教会被调派到王都的巡回神父，\n',
            '莫非就是…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0142,
        (
            '#1060F嗯！那就是我啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '……但…要说清楚为什么会在这里\n',
            '可就要花费很多时间了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0142, 400)

    ChrTalk(
        0x0008,
        (
            '（…………凯文神父。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0142,
        (
            '#1060F（嗯？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '（艾丝蒂尔那孩子……\n',
            '　就拜托你了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0142,
        (
            '#1063F……！！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1060F（是，我明白了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1031)

    def _loc_222E(): pass

    label('loc_222E')

    TalkEnd(0x0008)

    Return()

# id: 0x0006 offset: 0x2232
@scena.Code('func_06_2232')
def func_06_2232():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 6, 0x2086)),
            Expr.Return,
        ),
        'loc_2308',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_22C1',
    )

    ChrTalk(
        0x0009,
        (
            '结婚仪式顺利结束，\n',
            '总算是松了口气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '不过，竟然在现在这种时期\n',
            '举办结婚仪式…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '不愧是洛连特。\n',
            '真是惊人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    Jump('loc_2305')

    def _loc_22C1(): pass

    label('loc_22C1')

    ChrTalk(
        0x0009,
        (
            '在这种非常时期\n',
            '举办结婚仪式…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '不愧是洛连特。\n',
            '真是惊人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2305(): pass

    label('loc_2305')

    Jump('loc_2807')

    def _loc_2308(): pass

    label('loc_2308')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_236B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_231E',
    )

    Call(0, 0x0007)

    Jump('loc_2368')

    def _loc_231E(): pass

    label('loc_231E')

    ChrTalk(
        0x0009,
        (
            '交换戒指之后，\n',
            '接下来就是接吻了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '好啦、之前早已经\n',
            '练习好了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2368(): pass

    label('loc_2368')

    Jump('loc_2807')

    def _loc_236B(): pass

    label('loc_236B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_24A7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_23D2',
    )

    ChrTalk(
        0x00FE,
        (
            '亚尔特利亚法典国的事情\n',
            '我也不是太清楚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过那位神父应该就是\n',
            '出身于那里的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24A4')

    def _loc_23D2(): pass

    label('loc_23D2')

    ChrTalk(
        0x00FE,
        (
            '之前那位巡回神父和教区长\n',
            '聊了一阵…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听说那位巡回神父\n',
            '是从亚尔特利亚法典国的总部\n',
            '派遣过来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么年轻的人竟然就当上神父了，\n',
            '真是让人吃惊呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一直都以为总部的神父\n',
            '都是严肃古板的老头子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_24A4(): pass

    label('loc_24A4')

    Jump('loc_2807')

    def _loc_24A7(): pass

    label('loc_24A7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_259F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_2518',
    )

    ChrTalk(
        0x00FE,
        (
            '之前来的那位神父大人……\n',
            '和我印象中神父的形象完全不同。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那种风格也许在\n',
            '王都很流行吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_259C')

    def _loc_2518(): pass

    label('loc_2518')

    ChrTalk(
        0x00FE,
        (
            '刚才来过一位从王都大圣堂\n',
            '来的神父。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '无论是发型还是说话方式，\n',
            '都给人耳目一新的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难道王都现在流行\n',
            '那种风格吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_259C(): pass

    label('loc_259C')

    Jump('loc_2807')

    def _loc_259F(): pass

    label('loc_259F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_26EA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_2616',
    )

    ChrTalk(
        0x00FE,
        (
            '教区长结果一晚都没睡，\n',
            '好像不停的做着研究。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我身为教会的修女，\n',
            '也要努力做自己力所能及的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26E7')

    def _loc_2616(): pass

    label('loc_2616')

    ChrTalk(
        0x00FE,
        (
            '教区长结果一晚都没睡，\n',
            '好像不停的做着研究。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要自己还有一点力气，\n',
            '我就会继续努力祈祷的…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不知道什么时候就睡了过去，\n',
            '等醒来的时候都已经是早上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼～离教区长的境界…\n',
            '实在还差得很远呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_26E7(): pass

    label('loc_26E7')

    Jump('loc_2807')

    def _loc_26EA(): pass

    label('loc_26EA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_27BE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_275B',
    )

    ChrTalk(
        0x00FE,
        (
            '今天的礼拜雾气缭绕，\n',
            '真有点梦幻般的感觉呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然希望雾气赶快散去，\n',
            '天气晴起来也不错…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_27BB')

    def _loc_275B(): pass

    label('loc_275B')

    ChrTalk(
        0x00FE,
        (
            '今天的礼拜雾气缭绕，\n',
            '真有点梦幻般的感觉呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也不错…不过\n',
            '现在不是说那种话\n',
            '的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)

    def _loc_27BB(): pass

    label('loc_27BB')

    Jump('loc_2807')

    def _loc_27BE(): pass

    label('loc_27BE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 3, 0x1003)),
            Expr.Return,
        ),
        'loc_2807',
    )

    ChrTalk(
        0x00FE,
        (
            '空之女神爱德丝！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请您今天也继续\n',
            '守护洛连特的子民们吧… ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2807(): pass

    label('loc_2807')

    TalkEnd(0x0009)

    Return()

# id: 0x0007 offset: 0x280B
@scena.Code('func_07_280B')
def func_07_280B():
    OP_4A(0x0009, 255)
    OP_4A(0x000F, 255)

    ChrTalk(
        0x0009,
        (
            '接下来，\n',
            '请向前迈出一步——',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '请新郎将戒指戴到\n',
            '新娘的左手无名指。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '是、是的…明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '在婚礼开始之前\n',
            '还是多练习几次比较好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '不然太紧张的话，\n',
            '就算是最简单的动作也许都会失误。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0002)
    OP_A2(0x0008)
    ClearChrFlags(0x000F, 0x0010)
    OP_4B(0x0009, 255)
    OP_4B(0x000F, 255)

    Return()

# id: 0x0008 offset: 0x28ED
@scena.Code('func_08_28ED')
def func_08_28ED():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_2EAC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x034B, 6, 0x1A5E)),
            Expr.Return,
        ),
        'loc_2974',
    )

    ChrTalk(
        0x000A,
        (
            '#0180300116V#1060F我还有些事情，\n',
            '要在教会再待一阵子，\n',
            '暂时不能离开。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180300117V艾丝蒂尔，你们\n',
            '路上小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2EAC')

    def _loc_2974(): pass

    label('loc_2974')

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x000A,
        (
            '#0180300091V#1062F噢，艾丝蒂尔。\n',
            '这次也辛苦了啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300092V#1017F嗯！凯文先生也一样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300093V真是多亏你的帮忙了，\n',
            '缇欧她们的事……太感谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0180300094V#1061F哈哈～这是什么话，\n',
            '也太见外了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180300095V我之所以会这么努力，\n',
            '不全都是因为艾丝蒂尔嘛～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300096V#1008F又来了～真是个轻浮的家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2BF7',
    )

    ChrTalk(
        0x0103,
        (
            '#0030300097V#021F真是的，油嘴滑舌的程度\n',
            '简直和某人不相上下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040300098V#035F呼，说油嘴滑舌可太让我伤心了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040300099V#030F我一直都是很认真的呀！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300100V#1007F不用特意解释啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300101V#1011F……不、不好意思打断一下，\n',
            '凯文先生接下来有何打算？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C9E')

    def _loc_2BF7(): pass

    label('loc_2BF7')

    ChrTalk(
        0x0103,
        (
            '#0030300102V#021F真是的，油嘴滑舌的程度\n',
            '和奥利维尔有一拼啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300103V#1016F啊哈哈～这个嘛……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300104V#1011F话说回来，凯文先生\n',
            '接下来有什么打算吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C9E(): pass

    label('loc_2C9E')

    ChrTalk(
        0x000A,
        (
            '#0180300105V#1068F嗯，其实还要\n',
            '继续巡游一阵子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180300106V而且还有些事情…\n',
            '需要处理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300107V#1015F呼，需要处理的…事情吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300108V#1002F……看起来似乎是有\n',
            '重要的任务啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300109V来到这里应该\n',
            '也不是偶然吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0180300110V#1064F呜……艾丝蒂尔～\n',
            '你的感觉真是敏锐啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180300111V#1066F哈，总之在这里\n',
            '还有些事情…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180300112V不久的将来后\n',
            '咱们再见面吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010300113V#1006F嗯，好吧……\n',
            '到时拜托了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010300114V那么，\n',
            '凯文先生也要当心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0180300115V#1062F噢，艾丝蒂尔你们也一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1A5E)

    def _loc_2EAC(): pass

    label('loc_2EAC')

    TalkEnd(0x000A)

    Return()

# id: 0x0009 offset: 0x2EB0
@scena.Code('func_09_2EB0')
def func_09_2EB0():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_2F2A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_2EEB',
    )

    ChrTalk(
        0x00FE,
        (
            '能平安回来，\n',
            '真是要感谢女神啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2F2A')

    def _loc_2EEB(): pass

    label('loc_2EEB')

    ChrTalk(
        0x00FE,
        (
            '多亏女神\n',
            '才能平安回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今后也请继续\n',
            '守护我们吧…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_2F2A(): pass

    label('loc_2F2A')

    TalkEnd(0x000B)

    Return()

# id: 0x000A offset: 0x2F2E
@scena.Code('func_0A_2F2E')
def func_0A_2F2E():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_2F3A',
    )

    SetChrFlags(0x000C, 0x0010)

    def _loc_2F3A(): pass

    label('loc_2F3A')

    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_2FF1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_2F94',
    )

    ChrTalk(
        0x00FE,
        (
            '女神啊！\n',
            '请把这雾驱散吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看啊！！就像这样！\n',
            '一切拜托了！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2FF1')

    def _loc_2F94(): pass

    label('loc_2F94')

    ChrTalk(
        0x00FE,
        (
            '暂时也没事可做了，\n',
            '我就过来祈祷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈～虽然礼仪可能不对，\n',
            '但我也是诚心在祈祷呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    def _loc_2FF1(): pass

    label('loc_2FF1')

    TalkEnd(0x000C)

    Return()

# id: 0x000B offset: 0x2FF5
@scena.Code('func_0B_2FF5')
def func_0B_2FF5():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_3120',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_3071',
    )

    ChrTalk(
        0x00FE,
        (
            '真是的，皮尔姆那家伙\n',
            '还真是喜欢祈祷啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我对教会这种地方不是很熟悉，\n',
            '每次来就这样在这里待着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3120')

    def _loc_3071(): pass

    label('loc_3071')

    ChrTalk(
        0x00FE,
        (
            '真是的，皮尔姆那家伙\n',
            '还真是喜欢祈祷啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在吃饭之前\n',
            '一定会来礼拜堂的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在那家伙看来，\n',
            '一切都是因为女神的守护吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '却不想想全都多亏了\n',
            '送他到城里的游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0005)

    def _loc_3120(): pass

    label('loc_3120')

    TalkEnd(0x000D)

    Return()

# id: 0x000C offset: 0x3124
@scena.Code('func_0C_3124')
def func_0C_3124():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_31D2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_317A',
    )

    ChrTalk(
        0x00FE,
        (
            '教区长先生\n',
            '不告诉我重要的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯～那么目标\n',
            '改为修女吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_31CF')

    def _loc_317A(): pass

    label('loc_317A')

    ChrTalk(
        0x00FE,
        (
            '嗯～事情\n',
            '应该没错…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但教区长的话\n',
            '不是很明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '把目标换为修女好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0006)

    def _loc_31CF(): pass

    label('loc_31CF')

    Jump('loc_32D0')

    def _loc_31D2(): pass

    label('loc_31D2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_32D0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_3224',
    )

    ChrTalk(
        0x00FE,
        (
            '游击士这么早\n',
            '就开始一起行动… ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……果然是出了什么事呢!',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_32D0')

    def _loc_3224(): pass

    label('loc_3224')

    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x00FE, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '啊、艾丝蒂尔、雪拉！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这么早就\n',
            '开始行动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼～果然是昨夜\n',
            '发生了什么事件吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可不能这么悠闲了。\n',
            '克露莎也得赶快开始采访。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0006)

    def _loc_32D0(): pass

    label('loc_32D0')

    TalkEnd(0x000E)

    Return()

# id: 0x000D offset: 0x32D4
@scena.Code('func_0D_32D4')
def func_0D_32D4():
    TalkBegin(0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_3375',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_32ED',
    )

    Call(0, 0x0007)

    Jump('loc_3372')

    def _loc_32ED(): pass

    label('loc_32ED')

    ChrTalk(
        0x00FE,
        (
            '在这种时候举办婚礼，\n',
            '虽然亲属们也有反对的声音，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但还是想尽早\n',
            '结为正式夫妇呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我和艾娅莉商量之后，\n',
            '还是决定计划不变。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3372(): pass

    label('loc_3372')

    Jump('loc_39C6')

    def _loc_3375(): pass

    label('loc_3375')

    If(
        (
            (Expr.Eval, "OP_29(0x0072, 0x00, 0x02)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0072, 0x00, 0x10)"),
            Expr.Or,
            (Expr.Eval, "OP_29(0x0072, 0x00, 0x40)"),
            Expr.Or,
            (Expr.Eval, "OP_29(0x0072, 0x00, 0x08)"),
            (Expr.Eval, "OP_40(0x0234, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Nez64,
            Expr.Or,
            Expr.Return,
        ),
        'loc_399E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_33BF',
    )

    ChrTalk(
        0x00FE,
        (
            '啊啊～艾娅莉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_399B')

    def _loc_33BF(): pass

    label('loc_33BF')

    If(
        (
            (Expr.Eval, "OP_29(0x0072, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x0072, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0072, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3528',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 3, 0xB)),
            Expr.Return,
        ),
        'loc_342D',
    )

    ChrTalk(
        0x00FE,
        (
            '那么，游击士。\n',
            '戒指的事拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是发现了什么情况，\n',
            '请再来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3525')

    def _loc_342D(): pass

    label('loc_342D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_3481',
    )

    ChrTalk(
        0x00FE,
        (
            '那么，游击士。\n',
            '戒指的事拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要是发现了什么情况，\n',
            '请再来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3525')

    def _loc_3481(): pass

    label('loc_3481')

    OP_A2(0x0008)

    ChrTalk(
        0x00FE,
        (
            '啊，游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎、怎么样了？\n',
            '调查进行得如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F嗯，还在调查中呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '也许再等一会\n',
            '就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那、那样啊…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，明白了。\n',
            '我会一直等的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3525(): pass

    label('loc_3525')

    Jump('loc_399B')

    def _loc_3528(): pass

    label('loc_3528')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_35CA',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯～…………\n',
            '虽然大圣堂也很有吸引力，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但结婚仪式还是\n',
            '在家乡洛连特举办最好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在初次相遇的地方进行爱的宣誓… \n',
            '真有种神圣又纯粹的感觉啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_399B')

    def _loc_35CA(): pass

    label('loc_35CA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_3621',
    )

    ChrTalk(
        0x00FE,
        (
            '啊啊～～我可爱的艾娅莉啊～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我要像浓雾包裹城镇那样\n',
            '将你紧紧抱住～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_399B')

    def _loc_3621(): pass

    label('loc_3621')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_365F',
    )

    ChrTalk(
        0x00FE,
        (
            '再离我近一点，艾娅莉！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我只想看你的笑脸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_399B')

    def _loc_365F(): pass

    label('loc_365F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_399B',
    )

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3845',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0072, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_372D',
    )

    ChrTalk(
        0x00FE,
        (
            '你那美妙的颤抖，\n',
            '还有玫瑰花瓣一样的嘴唇……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从那里散落下来的… \n',
            '是你我相互间的承诺。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '终于…我们终于\n',
            '能在一起了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊！光是想一想\n',
            '就好激动！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3842')

    def _loc_372D(): pass

    label('loc_372D')

    ChrTalk(
        0x00FE,
        (
            '你那美妙的颤抖，\n',
            '还有玫瑰花瓣一样的嘴唇……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从那里散落下来的… \n',
            '是你我相互间的承诺。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '终于…我们终于\n',
            '能在一起了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊～～～尽管如此……\n',
            '女神难道没有慈悲之心吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，一定是想给我们的婚姻\n',
            '最后一次考验吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么一定要承受住。\n',
            '……艾娅莉，这都是为了你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3842(): pass

    label('loc_3842')

    Jump('loc_399B')

    def _loc_3845(): pass

    label('loc_3845')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_38F0',
    )

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x00FE,
        (
            '在突然的求婚之后，\n',
            '你那慌乱踌躇的眼神……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊～～陷入遐想之后\n',
            '那短暂的沉默…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……即使现在想起来，\n',
            '我的心脏也变得像要破裂了一样！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_399B')

    def _loc_38F0(): pass

    label('loc_38F0')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x00FE,
        (
            '啊啊！！美丽的诞辰庆典之夜！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '艾娅莉……每次看到你的脸，\n',
            '就会想起那个美妙的夜晚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在星空和花火的映衬下，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我鼓起勇气向你袒露\n',
            '心意的那个夜晚… ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_399B(): pass

    label('loc_399B')

    Jump('loc_39C6')

    def _loc_399E(): pass

    label('loc_399E')

    If(
        (
            (Expr.Eval, "OP_29(0x0072, 0x00, 0x08)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_39C2',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0072, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_39BB',
    )

    Call(1, 0x0001)

    Jump('loc_39BF')

    def _loc_39BB(): pass

    label('loc_39BB')

    Call(1, 0x0000)

    def _loc_39BF(): pass

    label('loc_39BF')

    Jump('loc_39C6')

    def _loc_39C2(): pass

    label('loc_39C2')

    Call(1, 0x0003)
    def _loc_39C6(): pass

    label('loc_39C6')

    TalkEnd(0x000F)

    Return()

# id: 0x000E offset: 0x39CA
@scena.Code('func_0E_39CA')
def func_0E_39CA():
    TalkBegin(0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_3AAF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3A5E',
    )

    ChrTalk(
        0x00FE,
        (
            '天堂的爸爸……\n',
            '你能听见吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '艾娅莉…\n',
            '马上就要做新娘了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不久之后\n',
            '将要穿上',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '美丽的婚纱，\n',
            '爸爸也会喜欢的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0009)

    Jump('loc_3AAC')

    def _loc_3A5E(): pass

    label('loc_3A5E')

    ChrTalk(
        0x00FE,
        (
            '天堂的爸爸……\n',
            '艾娅莉要做新娘了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今后也请您继续\n',
            '在天堂上守护我们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3AAC(): pass

    label('loc_3AAC')

    Jump('loc_3E87')

    def _loc_3AAF(): pass

    label('loc_3AAF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_3AC9',
    )

    ChrTalk(
        0x00FE,
        (
            '阿鲁姆……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E87')

    def _loc_3AC9(): pass

    label('loc_3AC9')

    If(
        (
            (Expr.Eval, "OP_29(0x0072, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x0072, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0072, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3B2B',
    )

    ChrTalk(
        0x00FE,
        (
            '我们在这里等着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然是很艰难的委托，\n',
            '但请努力坚持一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E87')

    def _loc_3B2B(): pass

    label('loc_3B2B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_3C07',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Return,
        ),
        'loc_3B8A',
    )

    ChrTalk(
        0x00FE,
        (
            '真想在王都的大圣堂\n',
            '举行婚礼仪式啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在充满回忆的地方\n',
            '开始新的生活㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3C04')

    def _loc_3B8A(): pass

    label('loc_3B8A')

    OP_A2(0x0009)

    ChrTalk(
        0x00FE,
        (
            '和他开始做\n',
            '结婚仪式的准备了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在我看来，在王都的大圣堂\n',
            '举行婚礼仪式啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在充满回忆的地方\n',
            '开始新的生活㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3C04(): pass

    label('loc_3C04')

    Jump('loc_3E87')

    def _loc_3C07(): pass

    label('loc_3C07')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_3C3C',
    )

    ChrTalk(
        0x00FE,
        (
            '喂～阿鲁姆。刚刚的句子\n',
            '有些不太美呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E87')

    def _loc_3C3C(): pass

    label('loc_3C3C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_3C78',
    )

    ChrTalk(
        0x00FE,
        (
            '好害羞啊，阿鲁姆……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '用那种眼神看着我…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E87')

    def _loc_3C78(): pass

    label('loc_3C78')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_3E87',
    )

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3D49',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x00FE,
        (
            '阿鲁姆就像小狗狗\n',
            '一样可怜巴巴地等着我的回答，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是好可怜的样子…\n',
            '所以我马上就答应了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如今……我们终于\n',
            '可以在一起了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼～这真是人生中\n',
            '最重大的一次事件啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E87')

    def _loc_3D49(): pass

    label('loc_3D49')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3DE8',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x00FE,
        (
            '幸福的感觉让我的胸口\n',
            '快要爆炸了一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我一边偷看他的表情\n',
            '一边思考。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵～阿鲁姆那时的表情，\n',
            '我大概一生也不会忘记呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E87')

    def _loc_3DE8(): pass

    label('loc_3DE8')

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x00FE,
        (
            '呵呵，诞辰庆典那天的事\n',
            '我现在也仿佛历历在目。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '眼前是纯白色的格兰赛尔城，\n',
            '头上是遍布繁星的夜空…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '然后他就说出了那句\n',
            '我期待了很久的话…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3E87(): pass

    label('loc_3E87')

    TalkEnd(0x0010)

    Return()

# id: 0x000F offset: 0x3E8B
@scena.Code('func_0F_3E8B')
def func_0F_3E8B():
    TalkBegin(0x0014)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 6, 0x2086)),
            Expr.Return,
        ),
        'loc_3FDA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3F79',
    )

    ChrTalk(
        0x00FE,
        (
            '结婚仪式非常完美，\n',
            '所以直到现在还沉浸在当时的情景中…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还要和老公\n',
            '在这里多待一会儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '和老公一起来礼拜堂，\n',
            '自结婚仪式之后这好像还是第一次…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵～偶尔像现在这样见证一下\n',
            '当时的誓言还是很有意义的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0007)

    Jump('loc_3FD7')

    def _loc_3F79(): pass

    label('loc_3F79')

    ChrTalk(
        0x00FE,
        (
            '结婚仪式非常完美，\n',
            '所以直到现在还沉浸在当时的情景中…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还要和老公\n',
            '在这里多待一会儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3FD7(): pass

    label('loc_3FD7')

    Jump('loc_40B6')

    def _loc_3FDA(): pass

    label('loc_3FDA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0410, 5, 0x2085)),
            Expr.Return,
        ),
        'loc_3FE4',
    )

    Jump('loc_40B6')

    def _loc_3FE4(): pass

    label('loc_3FE4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_40B6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4058',
    )

    ChrTalk(
        0x00FE,
        (
            '啊～不行哦。\n',
            '到这里来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '新娘马上就要\n',
            '穿礼服了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有意思的东西\n',
            '要留到仪式结束哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0007)

    Jump('loc_40B6')

    def _loc_4058(): pass

    label('loc_4058')

    ChrTalk(
        0x00FE,
        (
            '是纯白色的礼服，\n',
            '男方好像不怕花钱呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，果然不管怎样\n',
            '都会想到自己的结婚仪式呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_40B6(): pass

    label('loc_40B6')

    TalkEnd(0x0014)

    Return()

# id: 0x0010 offset: 0x40BA
@scena.Code('func_10_40BA')
def func_10_40BA():
    TalkBegin(0x0021)

    ChrTalk(
        0x00FE,
        (
            '哎呀～真是的，为什么\n',
            '非要选在这种日子呢… ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我对新郎劝说过好几次，\n',
            '让他延期举办。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但他顽固得很，\n',
            '根本就听不进去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0021)

    Return()

# id: 0x0011 offset: 0x4141
@scena.Code('func_11_4141')
def func_11_4141():
    TalkBegin(0x0022)

    ChrTalk(
        0x00FE,
        (
            '阿鲁姆哥哥\n',
            '看起来好像紧张呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有点担心他啊…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望不要失败……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0022)

    Return()

# id: 0x0012 offset: 0x4195
@scena.Code('func_12_4195')
def func_12_4195():
    TalkBegin(0x0023)

    ChrTalk(
        0x00FE,
        (
            '结婚仪式之后准备\n',
            '在附近的酒馆开个派对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听说那里的料理很不错，\n',
            '所以还蛮期待的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0023)

    Return()

# id: 0x0013 offset: 0x41F6
@scena.Code('func_13_41F6')
def func_13_41F6():
    TalkBegin(0x0024)

    ChrTalk(
        0x00FE,
        (
            '王国现在似乎\n',
            '处于动乱的状况中啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '孙女重要的结婚仪式…\n',
            '真希望能平安办成。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0024)

    Return()

# id: 0x0014 offset: 0x4251
@scena.Code('func_14_4251')
def func_14_4251():
    TalkBegin(0x0025)

    ChrTalk(
        0x00FE,
        (
            '附近的主妇们\n',
            '都来帮忙准备了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '洛连特的人还是\n',
            '这么热心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0025)

    Return()

# id: 0x0015 offset: 0x429C
@scena.Code('func_15_429C')
def func_15_429C():
    TalkBegin(0x0026)

    ChrTalk(
        0x00FE,
        (
            '这边的房间\n',
            '不让进去呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯…还想看看\n',
            '姐姐穿礼服的样子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0026)

    Return()

# id: 0x0016 offset: 0x42E7
@scena.Code('func_16_42E7')
def func_16_42E7():
    TalkBegin(0x0027)

    ChrTalk(
        0x00FE,
        (
            '艾娅莉要结婚了…\n',
            '一开始我完全不敢相信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼～被她抢在\n',
            '前面了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0027)

    Return()

# id: 0x0017 offset: 0x4338
@scena.Code('func_17_4338')
def func_17_4338():
    TalkBegin(0x0028)

    ChrTalk(
        0x00FE,
        (
            '来参加朋友的结婚仪式\n',
            '虽然很高兴…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但也替自己着急啊。\n',
            '必须要赶快寻找目标了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0028)

    Return()

# id: 0x0018 offset: 0x4395
@scena.Code('func_18_4395')
def func_18_4395():
    TalkBegin(0x0017)

    ChrTalk(
        0x00FE,
        (
            '啊，你们也要出席\n',
            '结婚仪式吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在时间还早呢。\n',
            '接下来新娘还要\n',
            '试穿礼服呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0017)

    Return()

# id: 0x0019 offset: 0x43F1
@scena.Code('func_19_43F1')
def func_19_43F1():
    TalkBegin(0x0019)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 2, 0xA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4477',
    )

    ChrTalk(
        0x00FE,
        (
            '呀～结婚仪式\n',
            '真是让人感动呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '让人不由自主得想起了\n',
            '自己当时的经历。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽、虽然不是家人…\n',
            '有些不好意思、',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x000A)

    Jump('loc_44C2')

    def _loc_4477(): pass

    label('loc_4477')

    ChrTalk(
        0x00FE,
        (
            '但结婚仪式真的让人感动呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然不是家人，\n',
            '但还是很替他们高兴啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_44C2(): pass

    label('loc_44C2')

    TalkEnd(0x0019)

    Return()

# id: 0x001A offset: 0x44C6
@scena.Code('func_1A_44C6')
def func_1A_44C6():
    EventBegin(0x00)
    OP_D2(0x0027020F, 0x00270214, 0x02)
    OP_D2(0x0027043F, 0x00270442, 0x03)
    OP_D2(0x00270440, 0x00270443, 0x04)
    OP_D2(0x00260221, 0x00260226, 0x06)
    OP_D2(0x00260220, 0x00260225, 0x07)
    SetChrChipByIndex(0x002A, 2)
    SetChrChipByIndex(0x002B, 3)
    SetChrChipByIndex(0x002C, 4)

    ExecExpressionWithValue(
        0x002A,
        0x2D,
        (
            (Expr.PushLong, 0x320),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x002A,
        0x2E,
        (
            (Expr.PushLong, 0x320),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x002A,
        0x2F,
        (
            (Expr.PushLong, 0x320),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x002A,
        0x07,
        (
            (Expr.PushLong, 0x320),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x002A,
        0x29,
        (
            (Expr.PushLong, 0x320),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x002B,
        0x2D,
        (
            (Expr.PushLong, 0x320),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x002B,
        0x2E,
        (
            (Expr.PushLong, 0x320),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x002B,
        0x2F,
        (
            (Expr.PushLong, 0x320),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x002B,
        0x07,
        (
            (Expr.PushLong, 0x320),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x002B,
        0x29,
        (
            (Expr.PushLong, 0x320),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x002C,
        0x2D,
        (
            (Expr.PushLong, 0x320),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x002C,
        0x2E,
        (
            (Expr.PushLong, 0x320),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x002C,
        0x2F,
        (
            (Expr.PushLong, 0x320),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x002C,
        0x07,
        (
            (Expr.PushLong, 0x320),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x002C,
        0x29,
        (
            (Expr.PushLong, 0x320),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_45C3',
    )

    Call(0, 0x001D)
    Call(0, 0x001E)

    def _loc_45C3(): pass

    label('loc_45C3')

    TerminateThread(0x000F, 0x00)
    TerminateThread(0x0010, 0x00)
    TerminateThread(0x0008, 0x00)
    TerminateThread(0x0009, 0x00)
    TerminateThread(0x000E, 0x00)
    TerminateThread(0x0021, 0x00)
    TerminateThread(0x0022, 0x00)
    TerminateThread(0x0023, 0x00)
    TerminateThread(0x0024, 0x00)
    TerminateThread(0x0025, 0x00)
    TerminateThread(0x0026, 0x00)
    TerminateThread(0x0027, 0x00)
    TerminateThread(0x0028, 0x00)
    SetChrPos(0x0010, 58450, 1000, 50290, 0)
    SetChrPos(0x000F, 59530, 1000, 50290, 0)
    SetChrPos(0x0008, 59000, 1000, 52160, 180)
    SetChrPos(0x0009, 60720, 1000, 52500, 180)
    ClearChrFlags(0x002A, 0x0080)
    ClearChrFlags(0x002B, 0x0080)
    ClearChrFlags(0x002C, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x0017, 0x0080)
    ClearChrFlags(0x0018, 0x0080)
    ClearChrFlags(0x0019, 0x0080)
    ClearChrFlags(0x001A, 0x0080)
    ClearChrFlags(0x001B, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x000E, 61680, 0, 44470, 0)
    ClearChrFlags(0x001C, 0x0080)
    ClearChrFlags(0x001D, 0x0080)
    ClearChrFlags(0x001E, 0x0080)
    ClearChrFlags(0x001F, 0x0080)
    ClearChrFlags(0x0020, 0x0080)
    ClearChrFlags(0x0021, 0x0080)
    ClearChrFlags(0x0022, 0x0080)
    ClearChrFlags(0x0023, 0x0080)
    ClearChrFlags(0x0024, 0x0080)
    ClearChrFlags(0x0025, 0x0080)
    ClearChrFlags(0x0026, 0x0080)
    ClearChrFlags(0x0027, 0x0080)
    ClearChrFlags(0x0028, 0x0080)
    SetChrFlags(0x0021, 0x0040)
    SetChrFlags(0x0021, 0x0004)
    SetChrFlags(0x0022, 0x0040)
    SetChrFlags(0x0022, 0x0004)
    SetChrFlags(0x0023, 0x0040)
    SetChrFlags(0x0023, 0x0004)
    SetChrFlags(0x0024, 0x0040)
    SetChrFlags(0x0024, 0x0004)
    SetChrFlags(0x0025, 0x0040)
    SetChrFlags(0x0025, 0x0004)
    SetChrFlags(0x0026, 0x0040)
    SetChrFlags(0x0026, 0x0004)
    SetChrFlags(0x0027, 0x0040)
    SetChrFlags(0x0027, 0x0004)
    SetChrFlags(0x0028, 0x0040)
    SetChrFlags(0x0028, 0x0004)
    SetChrChipByIndex(0x0023, 30)
    SetChrSubChip(0x0023, 0)
    SetChrChipByIndex(0x0024, 33)
    SetChrSubChip(0x0024, 0)
    SetChrChipByIndex(0x0025, 22)
    SetChrSubChip(0x0025, 0)
    SetChrPos(0x0021, 53270, 0, 45590, 45)
    SetChrPos(0x0022, 53920, 0, 45100, 0)
    SetChrPos(0x0023, 54210, 150, 45960, 0)
    SetChrPos(0x0024, 61700, 150, 45960, 0)
    SetChrPos(0x0025, 63570, 0, 45960, 0)
    SetChrPos(0x0026, 62600, 0, 45960, 0)
    SetChrPos(0x0027, 63880, 0, 44470, 0)
    SetChrPos(0x0028, 62690, 10, 44470, 0)
    SetChrPos(0x0101, 58510, 0, 40820, 0)
    SetChrPos(0x0102, 59450, 0, 40800, 0)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_481D',
    )

    SetChrPos(0x00F8, 57880, 0, 39620, 0)
    SetChrPos(0x00F9, 60090, 0, 39620, 0)

    Jump('loc_483F')

    def _loc_481D(): pass

    label('loc_481D')

    SetChrPos(0x00F9, 57880, 0, 39620, 0)
    SetChrPos(0x00F8, 60090, 0, 39620, 0)

    def _loc_483F(): pass

    label('loc_483F')

    OP_6D(58360, 0, 41870, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)
    OP_20(0x000003E8)
    Sleep(1000)

    OP_21()
    OP_1D(0x60)
    Sleep(1000)

    FadeIn(1000, 0)
    OP_0D()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010351140V#1011F#1P啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020351141V#1040F#2P哈哈，似乎……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020351142V来得正是\n',
            '好时候呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4920')
    def lambda_4920():
        OP_6C(330000, 4000)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_4920)

    OP_6D(59020, 1000, 50230, 4000)

    ChrTalk(
        0x0008,
        (
            '#1080351143V那么──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080351144V接下来就是交换戒指\n',
            '和宣誓之吻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0009, 0x01, 0x00, 0x001B)
    Sleep(200)

    CreateThread(0x0012, 0x01, 0x00, 0x001C)
    WaitForThreadExit(0x0012, 0x0001)
    Sleep(500)

    SetChrFlags(0x000F, 0x0040)
    SetChrFlags(0x0010, 0x0040)
    OP_8C(0x000F, 270, 400)
    OP_8C(0x0010, 90, 400)
    Sleep(500)

    @scena.Lambda('lambda_49C6')
    def lambda_49C6():
        OP_94(0x00, 0x00FE, 0x0000, 0x00000096, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_49C6)

    OP_94(0x00, 0x0010, 0x0000, 0x00000096, 0x000001F4, 0x00)
    Sleep(500)

    SetChrFlags(0x000B, 0x0008)
    SetChrFlags(0x000D, 0x0008)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000B, 59030, 1000, 50240, 330)
    SetChrPos(0x000D, 59300, 1000, 50400, 263)

    NpcTalk(
        0x000B,
        '阿鲁姆',
        (
            '#0970351145V#1P艾娅莉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000D,
        '艾娅莉',
        (
            '#0980351146V#2P阿鲁姆……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000D, 0x0080)

    @scena.Lambda('lambda_4A7C')
    def lambda_4A7C():
        OP_94(0x00, 0x00FE, 0x0000, 0x00000096, 0x000001F4, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_4A7C)

    OP_94(0x00, 0x0010, 0x0000, 0x00000096, 0x000001F4, 0x00)
    OP_62(0x000F, 0x00000000, 2000, 0x0A, 0x0B, 0x000000FA, 0x02)
    OP_22(0x000F, 0x00, 0x64)
    OP_62(0x0010, 0x00000000, 2000, 0x0A, 0x0B, 0x000000FA, 0x02)
    OP_22(0x000F, 0x00, 0x64)
    Sleep(1500)

    ChrTalk(
        0x0008,
        (
            '#1080351147V──我以伟大的创世女神\n',
            '爱德丝之名……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080351148V宣告你们二人从今日开始\n',
            '结为夫妇！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x00BF, 0x00, 0x64)
    OP_62(0x001E, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0021, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0022, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x001F, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x001D, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0016, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(120)

    OP_62(0x0017, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x001C, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0019, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x001A, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0028, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0023, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0024, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0018, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(120)

    OP_62(0x0020, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0015, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0012, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0025, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0026, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x000E, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0013, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0014, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0027, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(1000)

    Fade(1000)
    OP_6D(58360, 0, 41870, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_62(0x001E, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0021, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0022, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x001F, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x001D, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0016, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(120)

    OP_62(0x0017, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x001C, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0019, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x001A, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0028, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0023, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0024, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0018, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(120)

    OP_62(0x0020, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0015, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0012, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0025, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0026, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x000E, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0013, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0014, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    OP_62(0x0027, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4F06',
    )

    ChrTalk(
        0x0107,
        (
            '#0070351149V#067F哇～好棒啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4F06(): pass

    label('loc_4F06')

    ChrTalk(
        0x0101,
        (
            '#0010351150V#1017F#1P啊哈哈，还真是……\n',
            '令人感动呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020351151V#1053F#2P嗯……我也感觉是呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_508C',
    )

    ChrTalk(
        0x0106,
        (
            '#0050351152V#057F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0106, 400)

    ChrTalk(
        0x0101,
        (
            '#0010351153V#1019F#1P阿加特……\n',
            '为什么一直盯着新郎和新娘看啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050351154V#552F没，你们才是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050351155V为什么能目不转睛的\n',
            '看着这种令人害羞的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010351156V#1015F#1P是吗？不过我觉得这一幕很感人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_508C(): pass

    label('loc_508C')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_50EF',
    )

    ChrTalk(
        0x0108,
        (
            '#0080351157V#071F哈哈～来到这里\n',
            '也算是缘分。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080351158V我们也来\n',
            '祝福他们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_50EF(): pass

    label('loc_50EF')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_522B',
    )

    ChrTalk(
        0x0103,
        (
            '#0030351159V#025F呼～纯白的婚纱\n',
            '真是让人向往…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030351160V#020F那么，仪式虽然完毕了，\n',
            '但接下来才是高潮部分！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030351161V请新郎新娘退场，\n',
            '马上去外边！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010200318V#1011F#1P？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0103, 400)

    ChrTalk(
        0x0102,
        (
            '#0020351163V#1040F#2P啊啊～是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020351164V这可是身为女性\n',
            '绝对不能错过的事件啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_522B(): pass

    label('loc_522B')

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F3)
    NewScene('ED6_DT21/T0100._SN', 117, 0, 0)
    IdleLoop()

    Return()

# id: 0x001B offset: 0x5243
@scena.Code('func_1B_5243')
def func_1B_5243():
    OP_8E(0x00FE, 60720, 1000, 50290, 2000, 0x00)
    OP_8E(0x00FE, 60370, 1000, 50290, 2000, 0x00)
    OP_8C(0x000F, 90, 400)
    Sleep(1000)

    OP_8C(0x00FE, 0, 400)
    OP_8C(0x000F, 0, 400)
    OP_8E(0x00FE, 60720, 1000, 52500, 2000, 0x00)
    OP_8C(0x00FE, 180, 400)

    Return()

# id: 0x001C offset: 0x52A1
@scena.Code('func_1C_52A1')
def func_1C_52A1():
    OP_8E(0x00FE, 57670, 1000, 50290, 2000, 0x00)
    OP_8C(0x00FE, 90, 400)
    OP_8C(0x0010, 270, 400)
    Sleep(1000)

    OP_8C(0x00FE, 180, 400)
    OP_8C(0x0010, 0, 400)
    OP_8E(0x00FE, 57670, 0, 48880, 2000, 0x00)
    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x001D offset: 0x52F2
@scena.Code('func_1D_52F2')
def func_1D_52F2():
    FadeOut(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
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
        (0x00000000, 'loc_536F'),
        (0x00000001, 'loc_5375'),
        (-1, 'loc_537B'),
    )

    def _loc_536F(): pass

    label('loc_536F')

    OP_A2(0x1200)

    Jump('loc_537B')

    def _loc_5375(): pass

    label('loc_5375')

    OP_A2(0x1201)

    Jump('loc_537B')

    def _loc_537B(): pass

    label('loc_537B')

    Return()

# id: 0x001E offset: 0x537C
@scena.Code('func_1E_537C')
def func_1E_537C():
    ClearMapFlags(0x00000001)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)

    FadeIn(0, 0)

    OP_C9(
        0x00,
        (
            0x0000,
            0x0001,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
            0x0006,
            0x0007,
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
    OP_69(0x0000, 0x00000000)
    Sleep(1000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
